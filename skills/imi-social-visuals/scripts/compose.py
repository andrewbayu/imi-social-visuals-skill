#!/usr/bin/env python3
"""Compose an IMI social visual from a prepared photograph.

Requires Pillow. This script handles layout, typography and crop, not creative
photo editing or image generation.
"""

import argparse
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps


ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
FORMATS = {
    "1080x1350": {"size": (1080, 1350), "headline": 73, "sub": 29,
                  "sub_top_from_bottom": 207, "footer_from_bottom": 80,
                  "label_from_bottom": 31, "fade_start": 0.60},
    "1080x1920": {"size": (1080, 1920), "headline": 78, "sub": 31,
                  "sub_top_from_bottom": 310, "footer_from_bottom": 178,
                  "label_from_bottom": 98, "fade_start": 0.70},
    "1080x1080": {"size": (1080, 1080), "headline": 63, "sub": 26,
                  "sub_top_from_bottom": 175, "footer_from_bottom": 70,
                  "label_from_bottom": 27, "fade_start": 0.55},
}


def load_font(name, size, variation):
    font = ImageFont.truetype(str(ASSETS / name), size)
    font.set_variation_by_name(variation)
    return font


def fitted_font(draw, texts, name, variation, start_size, min_size, width):
    for size in range(start_size, min_size - 1, -1):
        font = load_font(name, size, variation)
        if all(draw.textbbox((0, 0), text, font=font)[2] <= width for text in texts):
            return font
    raise ValueError("Copy is too long for the format; shorten it instead of shrinking further.")


def center_text(draw, width, text, ink_top, font, fill):
    box = draw.textbbox((0, 0), text, font=font)
    x = round((width - (box[2] - box[0])) / 2 - box[0])
    y = round(ink_top - box[1])
    draw.text((x, y), text, font=font, fill=fill)
    return ink_top + box[3] - box[1]


def add_contrast_fades(image, fade_start):
    width, height = image.size
    overlay = Image.new("RGBA", image.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    rows = []
    for y in range(height):
        if y <= 230:
            alpha = 95
        elif y < 350:
            alpha = round(95 * (350 - y) / 120)
        elif y < height * fade_start:
            alpha = 0
        else:
            alpha = round(245 * (y - height * fade_start) / (height * (1 - fade_start)))
        rows.append((5, 13, 17, max(0, min(245, alpha))))
    for y, color in enumerate(rows):
        if color[3]:
            draw.line((0, y, width, y), fill=color)
    return Image.alpha_composite(image.convert("RGBA"), overlay)


def compose(args):
    cfg = FORMATS[args.format]
    width, height = cfg["size"]
    source = Image.open(args.image)
    if source.width < 800 or source.height < 800:
        raise ValueError("Background is too small for a sharp social export.")
    image = ImageOps.fit(
        source.convert("RGBA"), (width, height), Image.Resampling.LANCZOS,
        centering=(args.focal_x, args.focal_y),
    )
    image = add_contrast_fades(image, cfg["fade_start"])

    logo = Image.open(ASSETS / "imi-logo-white.png").convert("RGBA")
    logo = logo.crop(logo.getbbox())
    logo.thumbnail((330, 120), Image.Resampling.LANCZOS)
    image.alpha_composite(logo, (80, 80))

    draw = ImageDraw.Draw(image)
    headline = fitted_font(draw, args.headline_line, "Montserrat.ttf", "ExtraBold",
                           cfg["headline"], 48, width - 160)
    sub_font = fitted_font(draw, [args.subheadline], "Montserrat.ttf", "Medium",
                           cfg["sub"], 21, width - 160)
    footer_font = fitted_font(draw, [args.url], "Inter.ttf", "SemiBold",
                              30, 22, width - 160)
    white = (255, 255, 255, 255)

    sub_top = height - cfg["sub_top_from_bottom"]
    sub_bottom = center_text(draw, width, args.subheadline, sub_top, sub_font, white)
    if height - cfg["footer_from_bottom"] - 30 <= sub_bottom:
        raise ValueError("Subheadline collides with footer; shorten the copy.")

    # Work upwards from the subheadline, using visible glyph bounds.
    next_top = sub_top - 25
    for line in reversed(args.headline_line):
        box = draw.textbbox((0, 0), line, font=headline)
        ink_top = next_top - (box[3] - box[1])
        center_text(draw, width, line, ink_top, headline, white)
        next_top = ink_top - 10

    footer_box = draw.textbbox((0, 0), args.url, font=footer_font)
    footer_top = height - cfg["footer_from_bottom"] - (footer_box[3] - footer_box[1])
    center_text(draw, width, args.url, footer_top, footer_font, white)

    if args.source_type == "concept":
        label = "Ilustrasi konsep"
        label_font = load_font("Inter.ttf", 18, "Medium")
        box = draw.textbbox((0, 0), label, font=label_font)
        x = width - 80 - (box[2] - box[0]) - box[0]
        y = height - cfg["label_from_bottom"] - box[3]
        draw.text((x, y), label, font=label_font, fill=(220, 226, 227, 255))

    args.output.parent.mkdir(parents=True, exist_ok=True)
    image.convert("RGB").save(args.output, optimize=True)
    print(args.output)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--image", type=Path, required=True, help="Prepared background image")
    parser.add_argument("--format", choices=FORMATS, required=True)
    parser.add_argument("--headline-line", action="append", required=True,
                        help="One headline line; repeat for two or three lines")
    parser.add_argument("--subheadline", required=True)
    parser.add_argument("--url", default="inovasimaritim.com")
    parser.add_argument("--source-type", choices=("concept", "photo"), required=True)
    parser.add_argument("--focal-x", type=float, default=0.5)
    parser.add_argument("--focal-y", type=float, default=0.5)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if not 0 <= args.focal_x <= 1 or not 0 <= args.focal_y <= 1:
        parser.error("focal coordinates must be between 0 and 1")
    if len(args.headline_line) > 3:
        parser.error("Use at most three headline lines")
    compose(args)


if __name__ == "__main__":
    main()
