#!/usr/bin/env python3
"""Draw the 25 November 2026 front page: one 1024x1024 PNG.

Everything is drawn from scratch with Pillow primitives: no photos, no
network, no timestamps, no randomness, so every run writes identical bytes.
Run:  python3 draw.py   -> writes entry.png next to this file.
"""

import math
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "entry.png")

W = H = 1024
PAPER = (247, 241, 227)      # warm newsprint cream
CARD = (255, 255, 255)       # white story cards
INK = (26, 26, 26)           # near-black text
MUTED = (90, 86, 76)         # grey-brown secondary text
NAVY = (20, 38, 77)          # masthead navy
RED = (179, 39, 30)          # accent red
GOLD = (201, 162, 39)        # accent gold
TEAL = (15, 118, 110)        # accent teal
RULE = (216, 207, 192)       # hairline rule
BLUE = (31, 93, 168)         # accent blue

FONT_DIR = "/usr/share/fonts/truetype/dejavu"


def font(name, size):
    """Load a DejaVu font, falling back to the default bitmap font."""
    try:
        return ImageFont.truetype(os.path.join(FONT_DIR, name), size)
    except OSError:
        return ImageFont.load_default()


def wrap(draw, text, fnt, width):
    """Greedy word wrap returning a list of lines that fit `width` px."""
    lines = []
    for para in text.split("\n"):
        words = para.split()
        if not words:
            lines.append("")
            continue
        cur = words[0]
        for word in words[1:]:
            trial = cur + " " + word
            if draw.textlength(trial, font=fnt) <= width:
                cur = trial
            else:
                lines.append(cur)
                cur = word
        lines.append(cur)
    return lines


def draw_chip(draw, x, y, label, color):
    """Small coloured tag chip."""
    fnt = font("DejaVuSans-Bold.ttf", 15)
    tw = draw.textlength(label, font=fnt)
    pad_x, pad_y = 10, 5
    w, h = int(tw) + 2 * pad_x, 26
    draw.rounded_rectangle([x, y, x + w, y + h], radius=6, fill=color)
    draw.text((x + pad_x, y + pad_y - 1), label, font=fnt, fill=(255, 255, 255))


# ---------------------------------------------------------------- pictograms
def pic_breach(draw, x, y, s=104):
    """Monitor with a warning triangle: a cyber breach."""
    draw.rounded_rectangle([x + 8, y + 12, x + s - 8, y + s - 32],
                           radius=8, outline=NAVY, width=4, fill=(232, 238, 246))
    draw.line([x + s // 2 - 14, y + s - 28, x + s // 2 + 14, y + s - 28],
              fill=NAVY, width=4)
    draw.line([x + s // 2, y + s - 28, x + s // 2, y + s - 14],
              fill=NAVY, width=4)
    cx, cy, r = x + s // 2, y + 44, 24
    draw.polygon([(cx, cy - r), (cx + r, cy + r - 6), (cx - r, cy + r - 6)],
                 fill=RED)
    draw.line([cx, cy - 11, cx, cy + 5], fill=(255, 255, 255), width=4)
    draw.ellipse([cx - 2, cy + 11, cx + 2, cy + 15], fill=(255, 255, 255))


def pic_rocket(draw, x, y, s=104):
    """Rocket climbing past stars, with an orbit ring."""
    for sx, sy, r in [(x + 12, y + 14, 3), (x + s - 14, y + 22, 3),
                      (x + 20, y + s - 18, 2), (x + s - 22, y + s - 28, 2)]:
        draw.ellipse([sx - r, sy - r, sx + r, sy + r], fill=GOLD)
    draw.ellipse([x + 6, y + s - 42, x + s - 6, y + s - 4],
                 outline=TEAL, width=3)
    cx = x + s // 2
    draw.polygon([(cx, y + 6), (cx + 12, y + 32), (cx - 12, y + 32)],
                 fill=RED)
    draw.rounded_rectangle([cx - 12, y + 30, cx + 12, y + 62],
                           radius=6, fill=NAVY)
    draw.ellipse([cx - 6, y + 42, cx + 6, y + 54], fill=(255, 255, 255))
    draw.polygon([(cx - 12, y + 54), (cx - 24, y + 72), (cx - 12, y + 66)],
                 fill=RED)
    draw.polygon([(cx + 12, y + 54), (cx + 24, y + 72), (cx + 12, y + 66)],
                 fill=RED)
    draw.polygon([(cx - 5, y + 62), (cx + 5, y + 62), (cx, y + 84)],
                 fill=GOLD)


def pic_tower(draw, x, y, s=104):
    """Tall skyscraper with a small drone and an impact burst."""
    bx = x + s // 2 - 16
    draw.polygon([(bx, y + s - 6), (bx, y + 20), (bx + 16, y + 4),
                  (bx + 32, y + 20), (bx + 32, y + s - 6)],
                 fill=NAVY)
    for wy in (28, 44, 60, 76):
        draw.line([bx + 7, y + wy, bx + 25, y + wy], fill=GOLD, width=2)
    dx, dy = x + s - 30, y + 18
    draw.ellipse([dx - 6, dy - 6, dx + 6, dy + 6], fill=INK)
    draw.line([dx - 20, dy - 10, dx + 20, dy - 10], fill=INK, width=4)
    draw.ellipse([dx - 26, dy - 15, dx - 14, dy - 5], outline=INK, width=3)
    draw.ellipse([dx + 14, dy - 15, dx + 26, dy - 5], outline=INK, width=3)
    draw.line([dx - 4, dy + 6, dx - 4, dy + 14], fill=INK, width=3)
    draw.line([dx + 4, dy + 6, dx + 4, dy + 14], fill=INK, width=3)
    ix, iy = bx + 16, y + 42
    for ang in range(0, 360, 45):
        a = math.radians(ang)
        draw.line([ix, iy, ix + 19 * math.cos(a), iy + 19 * math.sin(a)],
                  fill=RED, width=3)
    draw.ellipse([ix - 5, iy - 5, ix + 5, iy + 5], fill=RED)


def pic_court(draw, x, y, s=104):
    """Courthouse: pediment, three columns, steps."""
    draw.polygon([(x + 8, y + 34), (x + s // 2, y + 10), (x + s - 8, y + 34)],
                 fill=NAVY)
    draw.ellipse([x + s // 2 - 6, y + 22, x + s // 2 + 6, y + 34],
                 fill=GOLD)
    draw.rectangle([x + 10, y + 34, x + s - 10, y + 42], fill=NAVY)
    for cx in (x + 22, x + s // 2, x + s - 22):
        draw.rectangle([cx - 6, y + 44, cx + 6, y + 76], fill=NAVY)
    draw.rectangle([x + 12, y + 78, x + s - 12, y + 84], fill=NAVY)
    draw.rectangle([x + 8, y + 86, x + s - 8, y + 92], fill=GOLD)


def pic_chart(draw, x, y, s=96):
    """Falling market chart: bars and a down arrow."""
    bars = [(14, 30), (30, 42), (46, 36), (62, 60), (78, 76)]
    for bx, bh in bars:
        draw.rectangle([x + bx, y + s - 12 - bh, x + bx + 12, y + s - 12],
                       fill=RED if bx >= 46 else NAVY)
    draw.line([x + 10, y + 20, x + 30, y + 30, x + 48, y + 26, x + 68,
               y + 48, x + s - 10, y + 72], fill=RED, width=4)
    draw.polygon([(x + s - 10, y + 72), (x + s - 24, y + 68),
                  (x + s - 12, y + 82)], fill=RED)


def pic_shield(draw, x, y, s=96):
    """Shield with a tick, over waves: a security pact."""
    draw.polygon([(x + s // 2, y + 4), (x + s - 8, y + 18),
                  (x + s - 8, y + 52), (x + s // 2, y + s - 8),
                  (x + 8, y + 52), (x + 8, y + 18)],
                 fill=TEAL)
    draw.line([x + s // 2 - 14, y + 44, x + s // 2 - 4, y + 56,
               x + s // 2 + 18, y + 28], fill=(255, 255, 255), width=5)
    for wy in (s - 2, s + 8):
        draw.arc([x + 2, y + wy - 8, x + s - 2, y + wy + 8], 0, 180,
                 fill=BLUE, width=3)


# ------------------------------------------------------------------- cards
def draw_card(draw, x, y, w, h, tag, tag_color, headline, body, pic):
    draw.rounded_rectangle([x, y, x + w, y + h], radius=10,
                           fill=CARD, outline=RULE, width=1)
    draw.line([x + 14, y + 10, x + w - 14, y + 10], fill=tag_color, width=3)
    draw_chip(draw, x + 16, y + 18, tag, tag_color)
    pic(draw, x + w - 122, y + 50)
    hf = font("DejaVuSans-Bold.ttf", 27)
    lines = wrap(draw, headline, hf, w - 140)
    ty = y + 52
    for line in lines[:3]:
        draw.text((x + 16, ty), line, font=hf, fill=INK)
        ty += 32
    bf = font("DejaVuSans.ttf", 18)
    blines = wrap(draw, body, bf, w - 32)
    by = y + h - 14 - 23 * min(len(blines), 4)
    for line in blines[:4]:
        draw.text((x + 16, by), line, font=bf, fill=(52, 48, 42))
        by += 23


def draw_strip(draw, x, y, w, h, tag, tag_color, headline, body, pic):
    draw.rounded_rectangle([x, y, x + w, y + h], radius=10,
                           fill=CARD, outline=RULE, width=1)
    draw.line([x + 14, y + 10, x + w - 14, y + 10], fill=tag_color, width=3)
    draw_chip(draw, x + 16, y + 14, tag, tag_color)
    pic(draw, x + w - 118, y + (h - 96) // 2)
    hf = font("DejaVuSans-Bold.ttf", 24)
    draw.text((x + 16, y + 46), headline, font=hf, fill=INK)
    bf = font("DejaVuSans.ttf", 17)
    blines = wrap(draw, body, bf, w - 150)
    by = y + 76
    for line in blines[:2]:
        draw.text((x + 16, by), line, font=bf, fill=(52, 48, 42))
        by += 21


def main():
    img = Image.new("RGB", (W, H), PAPER)
    draw = ImageDraw.Draw(img)

    # ---- masthead ------------------------------------------------------
    draw.rectangle([28, 24, 996, 150], fill=NAVY)
    draw.rectangle([28, 24, 996, 150], outline=GOLD, width=2)
    small = font("DejaVuSans-Bold.ttf", 15)
    kick = "ONE DAY  •  SIX STORIES  •  FROM ORBIT TO THE MARKETS"
    tw = draw.textlength(kick, font=small)
    draw.text(((W - tw) / 2, 33), kick, font=small, fill=GOLD)
    name = font("DejaVuSerif-Bold.ttf", 58)
    tw = draw.textlength("THE DAILY GLOBE", font=name)
    draw.text(((W - tw) / 2, 52), "THE DAILY GLOBE", font=name,
              fill=(255, 255, 255))
    date = font("DejaVuSans-Bold.ttf", 28)
    dtext = "WEDNESDAY, 25 NOVEMBER 2026"
    tw = draw.textlength(dtext, font=date)
    draw.text(((W - tw) / 2, 116), dtext, font=date, fill=(255, 255, 255))

    # ---- 2 x 2 story grid ----------------------------------------------
    grid_x, grid_y = 28, 164
    cw, ch, gap = 476, 252, 12
    stories = [
        ("CYBERATTACK · USA", RED,
         "CIA and spy chiefs hit by cyber breach",
         "Hackers hit the CIA and the Director of National "
         "Intelligence, exposing unclassified data on an open-source "
         "analysis system. Officials say no classified systems were hit.",
         pic_breach),
        ("SPACE · PAKISTAN", TEAL,
         "Pakistan's first astronaut reaches orbit",
         "Muhammad Zeeshan Ali rode China's Shenzhou-24 to the "
         "Tiangong station — the first Pakistani in orbit, and the "
         "first foreign astronaut aboard Tiangong.",
         pic_rocket),
        ("MIDDLE EAST · RIYADH", NAVY,
         "Drone hits Riyadh's tallest tower; 11 hurt",
         "A drone struck the 385-metre PIF tower in the Saudi "
         "capital, the second hit on the landmark in a week. Civil "
         "Defence reported 11 people wounded.",
         pic_tower),
        ("COURTS · USA", BLUE,
         "Huawei guilty on 10 of 12 counts",
         "A Brooklyn jury convicted the Chinese tech giant of bank "
         "fraud, wire fraud, sanctions violations and conspiring to "
         "steal US trade secrets. Sentencing is set for September 2027.",
         pic_court),
    ]
    for i, (tag, color, head, body, pic) in enumerate(stories):
        x = grid_x + (i % 2) * (cw + gap)
        y = grid_y + (i // 2) * (ch + gap)
        draw_card(draw, x, y, cw, ch, tag, color, head, body, pic)

    # ---- full-width strips ----------------------------------------------
    draw_strip(draw, 28, 692, 968, 116, "MARKETS · USA", RED,
               "AI rout: Nasdaq falls as tariff threat returns",
               "The Nasdaq slid 1.5% and the S&P 500 0.5% as chip stocks "
               "sank — Nvidia about 6%, Micron 11% — amid reports of "
               "tariff hikes on China, the EU and 14 more economies.",
               pic_chart)
    draw_strip(draw, 28, 820, 968, 116, "PACIFIC · DIPLOMACY", TEAL,
               "Solomon Islands picks Australia as top security partner",
               "Albanese and Wale signed a new treaty in Canberra, naming "
               "Australia the Solomons' top security partner as Honiara "
               "moves away from its 2022 pact with China.",
               pic_shield)

    # ---- footer ---------------------------------------------------------
    ff = font("DejaVuSans.ttf", 15)
    f1 = ("Every story above happened or was first reported on "
          "Wednesday, 25 November 2026.")
    tw = draw.textlength(f1, font=ff)
    draw.text(((W - tw) / 2, 948), f1, font=ff, fill=MUTED)
    f2 = ("Sources: CNN · Reuters · Xinhua · AP · WSJ    —    "
          "THE DAILY GLOBE: ONE PAGE, ONE DAY.")
    tw = draw.textlength(f2, font=ff)
    draw.text(((W - tw) / 2, 970), f2, font=ff, fill=MUTED)

    img.save(OUT, format="PNG")
    print("wrote", OUT, img.size)


if __name__ == "__main__":
    main()
