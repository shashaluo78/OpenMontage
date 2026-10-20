#!/usr/bin/env bash
# Rebuild the four brush-wipe demo shots from the uploaded stills (run from repo root).
set -e
OUT=${1:-briefs/demo-render/out}; mkdir -p "$OUT"
S=briefs/demo-render/demo_wipe.py
python3 -I $S demo4_before.png demo4_after.png brush.png "$OUT/demo4.mp4" 3.6 --start 0.2
python3 -I $S demo5_before.png demo5_after.png brush.png "$OUT/demo5.mp4" 3.2 --start 0.18
python3 -I $S demo6_before.png demo6_after.png brush.png "$OUT/demo6.mp4" 2.8 --start 0.22 --brush-x 0.6
python3 -I $S demo5_after.png demo7_after.png brush.png "$OUT/demo7.mp4" 3.6 --start 0.05 --full-mask
