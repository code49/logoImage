# logo assets

this repository contains processed versions of the mascot logo artwork, organized into subdirectories for original cuts and padded border variants.

## previews

| original (dot grid) | transparent background | solid white background | with border (transparent) | with border (solid white) |
| :---: | :---: | :---: | :---: | :---: |
| <img src="original/logo.jpg" alt="original logo" width="180" /> | <img src="original/logo_transparent.png" alt="transparent logo" width="180" /> | <img src="original/logo_white_background.png" alt="white background logo" width="180" /> | <img src="with_border/logo_transparent.png" alt="transparent logo with border" width="180" /> | <img src="with_border/logo_white_background.png" alt="white logo with border" width="180" /> |
| [`original/logo.jpg`](original/logo.jpg) | [`original/logo_transparent.png`](original/logo_transparent.png) | [`original/logo_white_background.png`](original/logo_white_background.png) | [`with_border/logo_transparent.png`](with_border/logo_transparent.png) | [`with_border/logo_white_background.png`](with_border/logo_white_background.png) |

---

## asset directory

### `original/`
contains unpadded source artwork and background removals:
- [`logo.jpg`](original/logo.jpg): original source artwork with dot-grid background.
- [`logo_transparent.png`](original/logo_transparent.png): high-precision transparent background PNG cutout.
- [`logo_white_background.png`](original/logo_white_background.png): clean solid-white background PNG.
- [`logo_white_background.jpg`](original/logo_white_background.jpg): clean solid-white background JPG.

### `with_border/`
contains padded variants with canvas margins added around the edges:
- [`logo_transparent.png`](with_border/logo_transparent.png): transparent background with extra canvas margin.
- [`logo_transparent_white_border.png`](with_border/logo_transparent_white_border.png): transparent logo centered on white canvas border.
- [`logo_white_background.png`](with_border/logo_white_background.png): solid white background with extra margin.
- [`logo_white_background.jpg`](with_border/logo_white_background.jpg): solid white JPG with extra margin.

---

## scripts

all image processing scripts are saved in the [`scripts/`](scripts/) directory:

- [`generate_bordered_logos.py`](scripts/generate_bordered_logos.py): generates custom border sizes around the images.

### custom border generation

to generate images with any custom border width (e.g. 250px or 300px), run:

```bash
nix-shell -p python3Packages.pillow --run "python3 scripts/generate_bordered_logos.py --border 250"
```
