"""Generate optimized WebP images, favicons and the OG image.
Run from repo root:  python3 _build/images.py   (needs Pillow)
Sources live in _build/img-src/ (not published):
  logo-original.png                    - Nicholas's original logo from the old site (main@c477b12), artwork unchanged
  old/*.jpg                            - the 12 photos from the old site (main@c477b12 images/), byte-identical originals"""
from PIL import Image, ImageDraw, ImageFont
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from tpl import PHONE_DISPLAY
SRC = '_build/img-src'; OUT = 'images/opt'; os.makedirs(OUT, exist_ok=True)
def save_webp(im, path, q=80): im.save(path, 'WEBP', quality=q, method=6)
logo = Image.open(f'{SRC}/logo-original.png').convert('RGBA')
# trim the transparent margin only, then pad back to an exact square (artwork itself is not altered)
logo = logo.crop(logo.getbbox()); S = max(logo.size)
sq = Image.new('RGBA', (S, S), (0, 0, 0, 0)); sq.paste(logo, ((S - logo.width) // 2, (S - logo.height) // 2)); logo = sq
def sized(n): return logo.resize((n, n), Image.LANCZOS)
for n in (96, 192, 384, 600): save_webp(sized(n), f'{OUT}/logo-{n}.webp', 82)   # header (42px @1-2x), hero badge (300px @1-2x)
sized(512).quantize(colors=256, method=Image.Quantize.FASTOCTREE, dither=Image.Dither.FLOYDSTEINBERG).save(f'{OUT}/logo-512.png', optimize=True)  # schema.org logo (crawlable PNG, 256-colour, visually identical)
sized(32).save('favicon-32x32.png', optimize=True)
logo.save('favicon.ico', sizes=[(16, 16), (32, 32), (48, 48)])
at = Image.new('RGBA', (180, 180), (29, 58, 46, 255)); m = sized(172); at.paste(m, (4, 4), m)
at.convert('RGB').save('apple-touch-icon.png', optimize=True)
# photos from the old site -> 4:3 responsive WebP (480/768/1024w). (master file, vertical crop position 0=top..1=bottom)
sys.path.insert(0, os.path.dirname(__file__))
from tpl import PHOTOS, photo_widths
QUALITY = {'shrub-trimming-ladder-fuel': 55, 'weed-clearing-crew': 62}  # busy foliage compresses poorly; default 70
PHOTO_SRC = {
    'junk-removal-crew-loading-truck': ('airbnb-turnover-cleanout-big-bear-lake.jpg', .30),
    'junk-removal-crew-armchair-truck': ('cabin-junk-removal-big-bear.jpg', .20),
    'mattress-removal-crew': ('furniture-swap-hauling-big-bear-str.jpg', .25),
    'hot-tub-removal-deck': ('hot-tub-removal-big-bear-airbnb.jpg', .50),
    'junk-hauling-box-truck': ('local-moving-hauling-big-bear.jpg', .35),
    'cabinet-tear-out': ('shed-demolition-removal-big-bear.jpg', .40),
    'shrub-trimming-ladder-fuel': ('tree-shrub-trimming-ladder-fuel-big-bear.jpg', .60),
    'weed-clearing-crew': ('weed-abatement-crew-big-bear.jpg', .60),
    'wildfire-dry-brush': ('weed-abatement-fire-risk-big-bear.jpg', .60),
    'appliances-electronics-pile': ('appliance-removal-big-bear-ca.jpg', .50),
    'mountain-cabin-pines': ('defensible-space-clearing-big-bear-cabin.jpg', .90),
    'yard-junk-pile': ('pine-needle-removal-fire-abatement-big-bear.jpg', .80),
}
for f in os.listdir(OUT):  # drop stale variants of these photos
    if any(f.startswith(n + '-') for n in PHOTO_SRC) and f.endswith('.webp'): os.remove(f'{OUT}/{f}')
for n, (f, pos) in PHOTO_SRC.items():
    im = Image.open(f'{SRC}/old/{f}').convert('RGB'); W, H = im.size; h = round(W * 3 / 4); y = round((H - h) * pos)
    im = im.crop((0, y, W, y + h))
    assert PHOTOS[n] == im.size, (n, im.size)
    for w in photo_widths(im.width):
        hh = round(im.height * w / im.width)
        save_webp(im.resize((w, hh), Image.LANCZOS) if w != im.width else im, f'{OUT}/{n}-{w}.webp', QUALITY.get(n, 70))
# OG image 1200x630
W, H = 1200, 630; og = Image.new('RGB', (W, H), (30, 58, 47)); d = ImageDraw.Draw(og)
d.polygon([(0, H), (260, 380), (420, 500), (640, 300), (900, 520), (1050, 420), (1200, 500), (1200, H)], fill=(20, 41, 33))
L = logo.resize((400, 400), Image.LANCZOS); og.paste(L, (740, 115), L)
def font(sz):
    for p in ['/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', '/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf']:
        if os.path.exists(p): return ImageFont.truetype(p, sz)
    return ImageFont.load_default()
d.text((70, 150), 'Junk Removal', font=font(72), fill='white')
d.text((70, 235), 'Big Bear', font=font(72), fill=(232, 163, 61))
d.text((70, 345), 'Junk removal · Weed clearing', font=font(34), fill=(230, 239, 233))
d.text((70, 395), 'Cleanouts · Hot tubs · E-waste', font=font(34), fill=(230, 239, 233))
d.text((70, 470), 'Free on-site quotes · 7 days', font=font(38), fill=(232, 163, 61))
if PHONE_DISPLAY: d.text((70, 530), f'Text {PHONE_DISPLAY}', font=font(38), fill='white')
og.save(f'{OUT}/og-junk-removal-big-bear.jpg', 'JPEG', quality=82, optimize=True, progressive=True)
for f in sorted(os.listdir(OUT)): print(f, os.path.getsize(f'{OUT}/{f}'))
for f in ['favicon.ico', 'favicon-32x32.png', 'apple-touch-icon.png']: print(f, os.path.getsize(f))
