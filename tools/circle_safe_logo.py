#!/usr/bin/env python3
"""Pad a logo so the whole artwork fits inside the app's circular crop.

ReWallet draws merchant logos in a 50px circle with BoxFit.cover, which
center-crops anything that is not circle-shaped (wide wordmarks lose their
first and last letters; tall lockups lose their text). This finds the ink,
centres it, and pads with the logo's own background colour (sampled from the
top-left corner) until every ink pixel sits inside the inscribed circle.

usage: circle_safe_logo.py <src> <out.png> [size=1024] [margin=1.06]
"""
import math, sys
from PIL import Image

src, out = sys.argv[1], sys.argv[2]
size = int(sys.argv[3]) if len(sys.argv) > 3 else 1024
margin = float(sys.argv[4]) if len(sys.argv) > 4 else 1.06

im = Image.open(src).convert("RGBA")
bgc = im.getpixel((2, 2))
bgc = (255, 255, 255) if bgc[3] == 0 else bgc[:3]
flat = Image.new("RGBA", im.size, bgc + (255,))
flat.alpha_composite(im)
rgb = flat.convert("RGB")

# Ink = anything that differs from the background colour.
px = rgb.load()
w, h = rgb.size
ink = []
for y in range(h):
    for x in range(w):
        p = px[x, y]
        if abs(p[0]-bgc[0]) + abs(p[1]-bgc[1]) + abs(p[2]-bgc[2]) > 30:
            ink.append((x, y))
if not ink:
    sys.exit("no ink found")
xs = [p[0] for p in ink]; ys = [p[1] for p in ink]
cx = (min(xs) + max(xs)) / 2; cy = (min(ys) + max(ys)) / 2
R = max(math.hypot(x-cx, y-cy) for x, y in ink) * margin
side = int(math.ceil(2*R))
canvas = Image.new("RGB", (side, side), bgc)
canvas.paste(rgb, (int(round(side/2 - cx)), int(round(side/2 - cy))))
canvas.resize((size, size), Image.LANCZOS).save(out, optimize=True)
print(f"{out}: bg={bgc} ink_bbox=({min(xs)},{min(ys)},{max(xs)},{max(ys)}) R={R:.0f} side={side}")
