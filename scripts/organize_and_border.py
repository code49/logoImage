import os
import shutil
from PIL import Image, ImageOps

BASE_DIR = os.path.expanduser("~/personal-work/logoImage")
ORIGINAL_DIR = os.path.join(BASE_DIR, "original")
WITH_BORDER_DIR = os.path.join(BASE_DIR, "with border")

# Create directories
os.makedirs(ORIGINAL_DIR, exist_ok=True)
os.makedirs(WITH_BORDER_DIR, exist_ok=True)

# Also create symlink logoImages -> logoImage if logoImages does not exist
ALT_BASE_DIR = os.path.expanduser("~/personal-work/logoImages")
if not os.path.exists(ALT_BASE_DIR):
    os.symlink(BASE_DIR, ALT_BASE_DIR)

# Move root image files into original/
files_to_move = [
    "logo.jpg",
    "logo_transparent.png",
    "logo_white_background.png",
    "logo_white_background.jpg",
    "logo_precise_transparent.png",
    "logo_precise_white.png",
    "logo_rembg.png",
    "logo_rembg_white.jpg"
]

for fname in files_to_move:
    src = os.path.join(BASE_DIR, fname)
    dst = os.path.join(ORIGINAL_DIR, fname)
    if os.path.exists(src) and not os.path.exists(dst):
        shutil.move(src, dst)
    elif os.path.exists(src) and os.path.exists(dst):
        os.remove(src)

print(f"Moved files into {ORIGINAL_DIR}")

# Function to add canvas border/padding around an image
def add_canvas_border(input_path, output_path, border_pixels=150, fill_color=(255, 255, 255, 0)):
    img = Image.open(input_path)
    
    if img.mode == 'RGBA':
        # Create a larger RGBA image
        new_width = img.width + (border_pixels * 2)
        new_height = img.height + (border_pixels * 2)
        padded_img = Image.new('RGBA', (new_width, new_height), fill_color)
        padded_img.paste(img, (border_pixels, border_pixels), img)
    else:
        # RGB image
        fill_rgb = fill_color[:3] if len(fill_color) == 4 else fill_color
        padded_img = ImageOps.expand(img, border=border_pixels, fill=fill_rgb)
        
    padded_img.save(output_path)
    print(f"Saved bordered image to {output_path}")

# Generate bordered versions for the main files in with border/
# 1. Transparent PNG with transparent border (150px padding)
add_canvas_border(
    os.path.join(ORIGINAL_DIR, "logo_transparent.png"),
    os.path.join(WITH_BORDER_DIR, "logo_transparent.png"),
    border_pixels=150,
    fill_color=(0, 0, 0, 0)
)

# 2. Transparent PNG with white border (150px padding)
add_canvas_border(
    os.path.join(ORIGINAL_DIR, "logo_transparent.png"),
    os.path.join(WITH_BORDER_DIR, "logo_transparent_white_border.png"),
    border_pixels=150,
    fill_color=(255, 255, 255, 255)
)

# 3. White background PNG with white border (150px padding)
add_canvas_border(
    os.path.join(ORIGINAL_DIR, "logo_white_background.png"),
    os.path.join(WITH_BORDER_DIR, "logo_white_background.png"),
    border_pixels=150,
    fill_color=(255, 255, 255)
)

# 4. White background JPG with white border (150px padding)
add_canvas_border(
    os.path.join(ORIGINAL_DIR, "logo_white_background.jpg"),
    os.path.join(WITH_BORDER_DIR, "logo_white_background.jpg"),
    border_pixels=150,
    fill_color=(255, 255, 255)
)

print("Finished generating bordered images.")
