import os
from PIL import Image, ImageOps

BASE_DIR = os.path.expanduser("~/personal-work/logoImage")
ORIGINAL_DIR = os.path.join(BASE_DIR, "original")
WITH_BORDER_DIR = os.path.join(BASE_DIR, "with border")

os.makedirs(WITH_BORDER_DIR, exist_ok=True)

def add_canvas_border(input_path, output_path, border_pixels=200, fill_color=(255, 255, 255, 0)):
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
    print(f"Saved 200px bordered image to {output_path}")

# 1. Transparent PNG with transparent border (200px padding)
add_canvas_border(
    os.path.join(ORIGINAL_DIR, "logo_transparent.png"),
    os.path.join(WITH_BORDER_DIR, "logo_transparent.png"),
    border_pixels=200,
    fill_color=(0, 0, 0, 0)
)

# 2. Transparent PNG with white border (200px padding)
add_canvas_border(
    os.path.join(ORIGINAL_DIR, "logo_transparent.png"),
    os.path.join(WITH_BORDER_DIR, "logo_transparent_white_border.png"),
    border_pixels=200,
    fill_color=(255, 255, 255, 255)
)

# 3. White background PNG with white border (200px padding)
add_canvas_border(
    os.path.join(ORIGINAL_DIR, "logo_white_background.png"),
    os.path.join(WITH_BORDER_DIR, "logo_white_background.png"),
    border_pixels=200,
    fill_color=(255, 255, 255)
)

# 4. White background JPG with white border (200px padding)
add_canvas_border(
    os.path.join(ORIGINAL_DIR, "logo_white_background.jpg"),
    os.path.join(WITH_BORDER_DIR, "logo_white_background.jpg"),
    border_pixels=200,
    fill_color=(255, 255, 255)
)

print("Finished updating images with 200px border.")
