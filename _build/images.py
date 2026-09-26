"""Generate optimized WebP images, favicons and the OG image.
Run from repo root:  python3 _build/images.py   (needs Pillow)
Sources live in _build/img-src/ (not published):
  logo-1024.png / logo-mark-1024.png  - rendered from images/logo.svg / images/logo-mark.svg (see _build/logo.py)
  RESTORED photos                      - AI-generated scenes from the old site, cropped; general scenes only (see images/CREDITS.md)"""
from PIL import Image, ImageDraw, ImageFont
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from tpl import PHONE_DISPLAY
SRC = '_build/img-src'; OUT = 'images/opt'; os.makedirs(OUT, exist_ok=True)
def save_webp(im, path, q=80): im.save(path, 'WEBP', quality=q, method=6)
logo = Image.open(f'{SRC}/logo-1024.png').convert('RGBA')
mark = Image.open(f'{SRC}/logo-mark-1024.png').convert('RGBA')
# schema.org logo (PNG, crawlable; palette-quantized - flat art)
logo.resize((512, 512), Image.LANCZOS).quantize(colors=96, method=Image.Quantize.FASTOCTREE).save(f'{OUT}/logo-512.png', optimize=True)
# favicons from the compact mark (no small text)
mark.resize((32, 32), Image.LANCZOS).save('favicon-32x32.png', optimize=True)
mark.save('favicon.ico', sizes=[(16, 16), (32, 32), (48, 48)])
at = Image.new('RGBA', (180, 180), (29, 58, 46, 255)); m = mark.resize((164, 164), Image.LANCZOS); at.paste(m, (8, 8), m)
at.convert('RGB').save('apple-touch-icon.png', optimize=True)
# restored general-scene photos -> responsive WebP
RESTORED = ['appliances-electronics-pile', 'mountain-cabin-pines', 'yard-junk-pile']
for n in RESTORED:
    im = Image.open(f'{SRC}/{n}.jpg').convert('RGB')
    for w in (480, 800):
        if w > im.width: w = im.width
        h = round(im.height * w / im.width)
        save_webp(im.resize((w, h), Image.LANCZOS) if w != im.width else im, f'{OUT}/{n}-{w}.webp', 72)
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
for f in ['favicon.ico', 'favicon-32x32.png', 'apple-touch-icon.png', 'images/logo.svg', 'images/logo-mark.svg']: print(f, os.path.getsize(f))
