#!/usr/bin/env python3
"""Rebuild kids_mud_drawings.png on the Model Y 2025+ Premium UV template.

Place this next to template.png and run: python3 make_wrap.py
Output is a 1024x1024 PNG clipped to the paintable islands.
"""
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W = 1024
TEMPLATE = "template.png"
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
INK = (18, 16, 16, 235)

def text_layer(text, size, angle):
    font = ImageFont.truetype(FONT, size)
    tmp = Image.new("RGBA", (1, 1))
    d = ImageDraw.Draw(tmp)
    bbox = d.textbbox((0, 0), text, font=font)
    tw, th = bbox[2] - bbox[0] + 12, bbox[3] - bbox[1] + 12
    im = Image.new("RGBA", (tw, th), (0, 0, 0, 0))
    ImageDraw.Draw(im).text((6 - bbox[0], 6 - bbox[1]), text, font=font, fill=INK)
    return im.rotate(angle, expand=True, resample=Image.BICUBIC) if angle else im

def paste_center(base, layer, cx, cy):
    base.alpha_composite(layer, (int(cx - layer.width / 2), int(cy - layer.height / 2)))

def main():
    template = Image.open(TEMPLATE).convert("RGBA")
    mask = np.array(template)[:, :, 3] > 128
    rng = np.random.default_rng(7)
    noise = rng.normal(0, 1, (W, W))
    nimg = Image.fromarray(((noise - noise.min()) / (noise.ptp()) * 255).astype(np.uint8))
    ns = np.array(nimg.filter(ImageFilter.GaussianBlur(6))).astype(np.float32) / 255.0
    base = np.stack([150 + ns * 40, 140 + ns * 35, 128 + ns * 30], axis=-1)
    grid = np.sin(np.arange(W)[None, :] * 0.35 + ns * 4)
    base = np.clip(base * (0.86 + 0.14 * ((grid + 1) / 2)[..., None]), 0, 255).astype(np.uint8)
    mud = np.zeros((W, W, 4), dtype=np.uint8)
    mud[:, :, :3] = base
    mud[:, :, 3] = np.where(mask, 255, 0)
    canvas = Image.fromarray(mud, "RGBA")
    # left islands: driver, tops face center
    paste_center(canvas, text_layer("WE ARE COOL", 28, -90), 150, 560)
    paste_center(canvas, text_layer("I AM BOO BOO BAKU!", 22, -90), 190, 640)
    paste_center(canvas, text_layer("Boo Jesus", 24, -90), 210, 740)
    paste_center(canvas, text_layer("HI!", 32, -90), 145, 760)
    # right islands: passenger
    paste_center(canvas, text_layer("+ Boobackooo", 28, 90), 860, 560)
    paste_center(canvas, text_layer("Jesus", 22, 90), 900, 680)
    paste_center(canvas, text_layer("wow", 28, 90), 880, 760)
    # hatch
    paste_center(canvas, text_layer("HI HAVE A GOOD DAY!", 26, 0), 510, 910)
    out = np.array(canvas)
    out[:, :, 3] = np.where(mask, out[:, :, 3], 0)
    Image.fromarray(out, "RGBA").save("kids_mud_drawings.png", optimize=True)

if __name__ == "__main__":
    main()
