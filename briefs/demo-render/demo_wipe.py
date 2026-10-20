"""Render a before->after brush-wipe demo shot as an MP4.

usage: demo_wipe.py BEFORE AFTER BRUSH OUT DURATION [--full-mask] [--start S] [--end E]
"""
import argparse, subprocess
import numpy as np
from PIL import Image, ImageFilter

W, H, FPS = 1080, 1920, 30

def load(p):
    return Image.open(p).convert("RGB").resize((W, H), Image.LANCZOS)

def key_brush(p, width):
    im = Image.open(p).convert("RGB")
    a = np.asarray(im).astype(np.int16)
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    green = (g - np.maximum(r, b)).clip(0, 255)
    alpha = (255 - (green * 3).clip(0, 255)).astype(np.uint8)
    # despill: clamp green to max(r,b) on edge pixels
    a[..., 1] = np.where(green > 0, np.maximum(r, b), g)
    rgba = np.dstack([a.clip(0, 255).astype(np.uint8), alpha])
    br = Image.fromarray(rgba, "RGBA")
    br = br.crop(br.getchannel("A").point(lambda v: 255 if v > 128 else 0).getbbox())
    scale = width / br.width
    br = br.resize((width, int(br.height * scale)), Image.LANCZOS)
    al = np.asarray(br.getchannel("A")) > 128
    rows = np.where(al.any(axis=1))[0]
    head_rows = rows[: int(len(rows) * 0.45)]          # oval head = top ~45%
    ys, xs = np.nonzero(al[head_rows[0]:head_rows[-1]])
    anchor = (int(xs.mean()), int(head_rows[0] + ys.mean()))
    return br, anchor

def ease(t):
    return t * t * (3 - 2 * t)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("before"); ap.add_argument("after"); ap.add_argument("brush"); ap.add_argument("out")
    ap.add_argument("duration", type=float)
    ap.add_argument("--full-mask", action="store_true")
    ap.add_argument("--start", type=float, default=0.12, help="wipe start, fraction of frame height")
    ap.add_argument("--end", type=float, default=1.02, help="wipe end, fraction of frame height")
    ap.add_argument("--brush-x", type=float, help="brush centre x, fraction of frame width (default: centre of changed area)")
    ap.add_argument("--brush-width", type=float, default=0.36)
    args = ap.parse_args()

    before, after = load(args.before), load(args.after)
    A = np.asarray(before).astype(np.float32); B = np.asarray(after).astype(np.float32)
    if args.full_mask:
        mask = np.ones((H, W), np.float32)
    else:
        d = np.abs(A - B).mean(axis=2)
        m = Image.fromarray((d > 18).astype(np.uint8) * 255).filter(ImageFilter.MaxFilter(15)).filter(ImageFilter.GaussianBlur(18))
        mask = np.asarray(m).astype(np.float32) / 255
    cols = mask.sum(axis=0)
    cx = int((cols * np.arange(W)).sum() / max(cols.sum(), 1))
    if args.brush_x is not None:
        cx = int(args.brush_x * W)
    brush, (ax, ay) = key_brush(args.brush, int(W * args.brush_width))

    sa = brush.getchannel("A").filter(ImageFilter.GaussianBlur(16)).point(lambda v: int(v * 0.35))
    shadow = Image.new("RGBA", brush.size, (0, 0, 0, 0)); shadow.putalpha(sa)

    n = int(args.duration * FPS)
    hold_in, hold_out = int(0.35 * FPS), int(0.6 * FPS)
    sweep = max(n - hold_in - hold_out, 1)
    yy = np.arange(H, dtype=np.float32)[:, None]
    feather = 60.0
    ff = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
                           "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "18", args.out],
                          stdin=subprocess.PIPE)
    for i in range(n):
        t = ease(min(max((i - hold_in) / sweep, 0), 1))
        line = (args.start + (args.end - args.start) * t) * H
        reveal = np.clip((line - yy) / feather + 0.5, 0, 1) * mask
        frame = A * (1 - reveal[..., None]) + B * reveal[..., None]
        img = Image.fromarray(frame.clip(0, 255).astype(np.uint8))
        # slow push-in
        z = 1 + 0.05 * i / n
        cw, ch = int(W / z), int(H / z)
        img = img.crop(((W - cw) // 2, (H - ch) // 2, (W + cw) // 2, (H + ch) // 2)).resize((W, H), Image.LANCZOS)
        # brush rides the wipe line during the sweep, slides away after
        if hold_in <= i < n - hold_out // 2:
            bx = int(cx - ax); by = int(line - ay)
            if i >= hold_in + sweep:
                k = (i - hold_in - sweep) / max(hold_out // 2, 1)
                bx += int(k * W * 0.8)
            img.paste(shadow, (bx + 14, by + 22), shadow)
            img.paste(brush, (bx, by), brush)
        ff.stdin.write(img.tobytes())
    ff.stdin.close(); ff.wait()

if __name__ == "__main__":
    main()
