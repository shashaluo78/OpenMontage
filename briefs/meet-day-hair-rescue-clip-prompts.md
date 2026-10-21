# Meet-Day Hair Rescue — Final Production Sheet

This replaces all earlier versions.

Vertical 9:16 · about 30 seconds · 6 video clips (3 story + 3 demos)

> **Update (fal.ai production):** Demo 7 is cut. All images are final (supplied by the user, saved in `projects/meet-day-hair-rescue/assets/images/`). The Demo 4 and Demo 6 prompts below were reworded to match the final start frames: Demo 4 uses her own hand, Demo 6 uses a stylist's gloved hands.

---

## PART 1 — Image checklist

### Already done (keep these)

| File | Status |
|---|---|
| `start.png` | ✅ keep |
| `brush.png` | ✅ keep |
| `demo4_before.png` / `demo4_after.png` | ✅ keep |
| `demo5_before.png` / `demo5_after.png` | ✅ keep |
| `demo6_before.png` / `demo6_after.png` | ✅ keep (the originals) |

### Still to make (5 images, in Gemini or ChatGPT)

| # | Save as | Upload these | Prompt |
|---|---|---|---|
| ~~1~~ | ~~`demo7_after.png`~~ (cut: Demo 7 dropped) | | |
| 2 | `demo4_start.png` | `demo4_before.png` + `brush.png` | **Prompt B** |
| 3 | `demo5_start.png` | `demo5_before.png` + `brush.png` | **Prompt B** |
| ~~4~~ | ~~`demo7_start.png`~~ (cut: Demo 7 dropped) | | |
| 5 | `demo6_start.png` | `demo6_before.png` + `brush.png` | **Prompt C** |

When uploading two images, upload the before/after image FIRST and `brush.png` SECOND.

**Prompt A** (fixes the outfit change in demo 7)
```
Edit this photo. Keep her orange sweater, the framing, the lighting and the background exactly the same. Do not add a cape and do not change any clothing. Remove the claw clip and make ALL of her hair perfectly sleek, straight and glossy, falling smoothly down her back over the orange sweater. Portrait 9:16.
```

**Prompt B** (stylist's hand from behind, used for demos 4, 5 and 7)
```
Edit the first photo. Keep the exact same framing as the original: do not zoom in or crop; the claw clip, her shoulders and the background must stay fully visible and unchanged. Add a stylist's hand wearing a black nitrile glove, coming in from the top right of the frame, wrist above the brush, holding the handle of the brush from the second image (same cream oval brush with silver-outlined back panel and yellow end cap) the normal way, like a paddle brush, fingers wrapped around the handle and thumb on top. The bristles press into her hair just under the claw clip at the centre, with the back of the brush facing the camera and the handle pointing up and to the right. Keep her hair, clothes, clip and background exactly the same. Portrait 9:16, photorealistic.
```

**Prompt C** (she brushes her own hair, side view, demo 6)
```
Edit the first photo. Keep the exact same framing as the original; do not zoom in or crop. Her own hand comes up from under the black salon cape, holding the brush from the second image (same cream oval brush with silver-outlined back panel and yellow end cap) the normal way, fingers wrapped around the handle, placed at the roots on the side of her hair nearest the camera, ready to brush down. Keep her face, hair, cape, lighting and background exactly the same. Portrait 9:16, photorealistic.
```

**Check every start image:**
- natural hand with five fingers
- same framing as the before image (nothing zoomed or cropped)
- the cream brush with the yellow cap

---

## PART 2 — Video checklist (Hailuo)

Settings for every clip: **MiniMax H3** · **Start/End Frame** · **768p** · **5s** · aspect ratio **Auto**

| # | Save as | Start Frame | End Frame | Prompt |
|---|---|---|---|---|
| 1 | `clip1.mp4` | `start.png` | (empty) | **Clip 1** |
| 2 | `clip2.mp4` | `clip2_start.jpg` | `clip2_end.jpg` | **Clip 2** |
| 3 | `clip3.mp4` | `clip3_start.png` (last frame of clip2) | `clip3_end.jpg` | **Clip 3** |
| 4 | `demo4.mp4` | `demo4_start.png` | `demo4_after.png` | **Demo 4** |
| 5 | `demo5.mp4` | `demo5_start.png` | `demo5_after.png` | **Demo 5** |
| 6 | `demo6.mp4` | `demo6_start.png` | `demo6_after.png` | **Demo 6** |

To get a "last frame", play the clip to the very end, pause it and take a screenshot. Crop the screenshot to just the video.

**Clip 1**
```
Vertical handheld smartphone video, slight natural camera shake, eye-level medium shot. Indoor gymnastics competition hall with folding chairs, blue banners and people walking in the blurred background. The woman behind the seated girl works the black comb through the girl's frizzy, tangled brown hair, and the comb gets stuck in a tangle. The girl pouts, rolls her eyes and slumps impatiently in the chair, clearly bored of waiting. The woman tries again, then sighs and looks toward the camera helplessly. The man beside them watches with a small knowing smile. Realistic, candid, real-time speed, no text. Audio: natural indoor crowd ambience only, no speech, no music.
```

**Clip 2** (start frame: `clip2_start.jpg`, dad already holding the brush; end frame: `clip2_end.jpg`, one sleek stripe)
```
Vertical handheld smartphone video, eye-level medium shot. The camera holds the same distance for the whole clip: no zoom, no push-in, and all three faces stay fully in frame. Indoor gymnastics competition hall with blue banners and people walking in the blurred background, bright even overhead lighting. The girl sits on the black folding chair in her blue sparkly leotard, pink backpack and gold medal, with her lavender headband on her head. The lavender headband stays on her head and clearly visible for the entire clip. The man in the denim shirt holds the brush already resting on top of her head: a cream-coloured oval paddle brush whose back is smooth cream with a silver-outlined oval panel, a small round cream button and a silver oval ring, on a slim cream handle with a small yellow end cap. The brush head is entirely cream with no yellow on it. With a confident little smile he pulls the brush slowly down through the frizzy hair on his side, from the top of her head down past her shoulder, in one smooth stroke, holding it by the handle with the back of the brush facing the camera. Only the strip of hair the brush touches turns smooth, straight and glossy, leaving one clear sleek stripe about the width of the brush through the frizz. All the rest of her hair stays frizzy and tangled. The woman stops combing, lowers the comb and leans in slightly with her eyebrows raised in disbelief. The girl's wince relaxes and she glances sideways with curious wide eyes. Realistic, candid, real-time speed, no text. Audio: natural indoor crowd ambience only, no speech, no music.
```

**Clip 3** (start frame: `clip3_start.png` = last frame of clip2; end frame: `clip3_end.jpg`, all hair sleek, girl standing)
```
Vertical handheld smartphone video, eye-level medium shot. The camera holds the same distance for the whole clip: no zoom, no push-in, and all three faces stay fully in frame. Indoor gymnastics competition hall with blue banners and people walking in the blurred background, bright even overhead lighting. The girl sits on the black folding chair in her blue sparkly leotard, black sparkly leggings, pink backpack and gold medal, with her lavender headband on her head. The lavender headband stays on her head and clearly visible for the entire clip. The man in the denim shirt quickly brushes her hair all over with the cream oval brush (smooth cream back with a silver-outlined oval panel, small round button and silver oval ring, slim cream handle with a small yellow end cap; no yellow on the brush head). He makes several smooth top-to-bottom strokes, working around her head section by section: the side nearest him, the back, then the side nearest the woman. Each section the brush passes turns smooth, straight and glossy, until all of her long brown hair is completely sleek with no frizz left. He lifts the brush, holding it firmly by the handle, and raises it beside his face in a small proud wave. The woman covers her mouth with both hands in happy surprise. The girl runs her fingers through her sleek hair, breaks into a huge delighted grin and hops up from the chair to stand in front of it. Realistic, candid, real-time speed, no text. Audio: natural indoor crowd ambience only, no speech, no music.
```

**Demo 4** (her own hand)
```
Vertical close-up from behind. Her own hand reaches back and slowly pulls the cream oval brush straight down from just under the claw clip through the centre of her hair to the ends, in one smooth stroke. Only the hair the brush passes turns sleek, straight and glossy; the clip, the hair above it and the hair on either side stay exactly as they are. At the end she lowers her arm and the brush out of frame. Steady camera, soft salon lighting, realistic hair, satisfying. Audio: soft brushing sound only, no speech, no music.
```

**Demo 5** (stylist's gloved hand)
```
Vertical close-up from behind. A stylist's black-gloved hand slowly pulls the cream oval brush straight down from just under the claw clip through the centre of her hair to the ends, in one smooth stroke. Only the hair the brush passes turns sleek, straight and glossy; the clip, the hair above it and the hair on either side stay exactly as they are. At the end the hand lifts the brush out of frame. Steady camera, soft salon lighting, realistic hair, satisfying. Audio: soft brushing sound only, no speech, no music.
```

**Demo 6** (stylist's gloved hands)
```
Vertical three-quarter side view. A stylist's black-gloved hand slowly pulls the cream oval brush from the crown down the side of her hair nearest the camera to the ends, while the stylist's other gloved hand smooths the section. Only that section turns sleek, straight and glossy; the rest of her hair stays wavy. The stroke finishes with the brush near the ends of her hair. She stays seated and still, looking down calmly. Steady camera, soft salon lighting, realistic. Audio: soft brushing sound only, no speech, no music.
```

---

## PART 3 — Upload to GitHub when done

https://github.com/shashaluo78/OpenMontage/upload/claude/nice-keller-7yqfpa

Upload: `clip1.mp4` `clip2.mp4` `clip3.mp4` `demo4.mp4` `demo5.mp4` `demo6.mp4`

Final order in the edit: clip1 → clip2 → clip3 → demo4 → demo5 → demo6
