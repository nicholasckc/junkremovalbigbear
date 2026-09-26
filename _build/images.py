"""Generate optimized WebP images, favicons and the OG image from images/ sources.
Run from repo root:  python3 _build/images.py   (needs Pillow)"""
from PIL import Image, ImageDraw, ImageFont
import os
SRC='images'; OUT='images/opt'; os.makedirs(OUT,exist_ok=True)
logo=Image.open(f'{SRC}/junk-removal-big-bear-logo.png').convert('RGBA')
# crop transparent/black border around the round badge
bbox=logo.getbbox(); logo=logo.crop(bbox)
def save_webp(im,path,q=80): im.save(path,'WEBP',quality=q,method=6)
for s in (96,192,384):
    save_webp(logo.resize((s,s),Image.LANCZOS),f'{OUT}/logo-{s}.webp',85)
# favicons
logo.resize((32,32),Image.LANCZOS).save('favicon-32x32.png',optimize=True)
logo.resize((180,180),Image.LANCZOS).convert('RGBA').save('apple-touch-icon.png',optimize=True)
logo.save('favicon.ico',sizes=[(16,16),(32,32),(48,48)])
# (AI-generated "crew" photos from the old site were removed; stock scenery lives in images/opt, see images/CREDITS.md)
# OG image 1200x630
W,H=1200,630; og=Image.new('RGB',(W,H),(30,58,47)); d=ImageDraw.Draw(og)
d.polygon([(0,H),(260,380),(420,500),(640,300),(900,520),(1050,420),(1200,500),(1200,H)],fill=(20,41,33))
L=logo.resize((400,400),Image.LANCZOS); og.paste(L,(740,115),L)
def font(sz,bold=True):
    for p in ['/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf','/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf']:
        if os.path.exists(p): return ImageFont.truetype(p,sz)
    return ImageFont.load_default()
d.text((70,170),'Junk Removal',font=font(72),fill='white')
d.text((70,255),'Big Bear',font=font(72),fill=(232,163,61))
d.text((70,365),'Junk removal · Weed clearing',font=font(34),fill=(230,239,233))
d.text((70,415),'Cleanouts · Hot tubs · E-waste',font=font(34),fill=(230,239,233))
d.text((70,500),'Free on-site quotes · 7 days',font=font(38),fill=(232,163,61))
og.save(f'{OUT}/og-junk-removal-big-bear.jpg','JPEG',quality=82,optimize=True,progressive=True)
for f in sorted(os.listdir(OUT)): print(f, os.path.getsize(f'{OUT}/{f}'))
for f in ['favicon.ico','favicon-32x32.png','apple-touch-icon.png']: print(f, os.path.getsize(f))
