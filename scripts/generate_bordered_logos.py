#!/usr/bin/env python3
"""
Logo Border Generator
=====================
Usage:
    nix-shell -p python3Packages.pillow --run "python3 scripts/generate_bordered_logos.py --border 200"

This script takes the original logo versions in 'original/' and generates padded
border versions in 'with border/' with the specified pixel width.
"""

import os
import argparse
from PIL import Image, ImageOps

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(SCRIPT_DIR)
ORIGINAL_DIR = os.path.join(BASE_DIR, "original")
WITH_BORDER_DIR = os.path.join(BASE_DIR, "with_border")

def add_canvas_border(input_path, output_path, border_pixels, fill_color=(255, 255, 255, 0)):
    if not os.path.exists(input_path):
        print(f"Warning: {input_path} not found.")
        return

    img = Image.open(input_path)
    
    if img.mode == 'RGBA':
        new_width = img.width + (border_pixels * 2)
        new_height = img.height + (border_pixels * 2)
        padded_img = Image.new('RGBA', (new_width, new_height), fill_color)
        padded_img.paste(img, (border_pixels, border_pixels), img)
    else:
        fill_rgb = fill_color[:3] if len(fill_color) == 4 else fill_color
        padded_img = ImageOps.expand(img, border=border_pixels, fill=fill_rgb)
        
    padded_img.save(output_path)
    print(f"Saved {border_pixels}px bordered image to: {output_path}")

def main():
    parser = argparse.ArgumentParser(description="Generate bordered logo images with custom canvas padding.")
    parser.add_argument("--border", type=int, default=200, help="Border padding in pixels (default: 200)")
    args = parser.parse_args()

    os.makedirs(WITH_BORDER_DIR, exist_ok=True)
    border_px = args.border

    print(f"Generating bordered logos with {border_px}px border padding...")

    # 1. Transparent PNG with transparent border
    add_canvas_border(
        os.path.join(ORIGINAL_DIR, "logo_transparent.png"),
        os.path.join(WITH_BORDER_DIR, "logo_transparent.png"),
        border_pixels=border_px,
        fill_color=(0, 0, 0, 0)
    )

    # 2. Transparent PNG with solid white border canvas
    add_canvas_border(
        os.path.join(ORIGINAL_DIR, "logo_transparent.png"),
        os.path.join(WITH_BORDER_DIR, "logo_transparent_white_border.png"),
        border_pixels=border_px,
        fill_color=(255, 255, 255, 255)
    )

    # 3. White background PNG with white border
    add_canvas_border(
        os.path.join(ORIGINAL_DIR, "logo_white_background.png"),
        os.path.join(WITH_BORDER_DIR, "logo_white_background.png"),
        border_pixels=border_px,
        fill_color=(255, 255, 255)
    )

    # 4. White background JPG with white border
    add_canvas_border(
        os.path.join(ORIGINAL_DIR, "logo_white_background.jpg"),
        os.path.join(WITH_BORDER_DIR, "logo_white_background.jpg"),
        border_pixels=border_px,
        fill_color=(255, 255, 255)
    )

    print("Done!")

if __name__ == "__main__":
    main()
