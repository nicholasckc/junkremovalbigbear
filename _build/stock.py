"""Free-licensed stock photos (Pexels License) -> 4:3 responsive WebP (480/768/1024/1400w).
Run from repo root:  python3 _build/stock.py   (needs Pillow). Masters: _build/img-src/stock/ (not published).
These are illustrative stock photos. They are never captioned or presented as Junk Removal Big Bear's crew, truck or jobs;
no visible credit is shown (the Pexels License does not require one); sources are logged privately in _build/IMAGE-SOURCES.md."""
from PIL import Image
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from tpl import STOCK, PHOTOS, photo_widths
SRC = '_build/img-src/stock'; OUT = 'images/opt'
for n, s in STOCK.items():
    im = Image.open(f'{SRC}/{n}.jpg').convert('RGB'); pos = s['pos']
    if s.get('pre'): a, b, c, d = s['pre']; im = im.crop((round(im.width * a), round(im.height * b), round(im.width * c), round(im.height * d)))
    W, H = im.size
    if W / H > 4 / 3:   # landscape wider than 4:3 -> crop width
        w = round(H * 4 / 3); x = round((W - w) * pos); im = im.crop((x, 0, x + w, H))
    else:               # portrait / square -> crop height
        h = round(W * 3 / 4); y = round((H - h) * pos); im = im.crop((0, y, W, y + h))
    if im.width > 1400: im = im.resize((1400, round(im.height * 1400 / im.width)), Image.LANCZOS)
    assert PHOTOS[n] == im.size, (n, im.size)
    for f in os.listdir(OUT):
        if f.startswith(n + '-') and f.endswith('.webp'): os.remove(f'{OUT}/{f}')
    for w in photo_widths(im.width):
        hh = round(im.height * w / im.width)
        (im.resize((w, hh), Image.LANCZOS) if w != im.width else im).save(f'{OUT}/{n}-{w}.webp', 'WEBP', quality=s.get('q', 68), method=6)
    print(n, im.size, [(w, os.path.getsize(f'{OUT}/{n}-{w}.webp')) for w in photo_widths(im.width)])
