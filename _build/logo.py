"""Generate the Junk Removal Big Bear logo SVGs (text converted to paths, no web fonts needed).
Usage (repo root): python3 _build/logo.py   (needs fontTools; font: Alfa Slab One, SIL OFL)
Writes images/logo.svg (full badge) and images/logo-mark.svg (compact mark for header/favicon)."""
import math, sys
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
FONT = sys.argv[1] if len(sys.argv) > 1 else '/usr/share/fonts/truetype/sand-box/google/Alfa Slab One/AlfaSlabOne-Regular.ttf'
f = TTFont(FONT); gs = f.getGlyphSet(); cmap = f.getBestCmap(); upm = f['head'].unitsPerEm
PINE, GREEN, CREAM, AMBER, BROWN = '#1d3a2e', '#2f5d46', '#f6efdc', '#e8a33d', '#6b4226'
def adv(ch): return gs[cmap[ord(ch)]].width
def arc_text(text, r, size, center_deg, bottom=False, spacing=0.06):
    """Glyph outlines placed along a circle centred at (256,256). Top text reads clockwise, bottom text counter-clockwise (upright)."""
    s = size / upm
    widths = [adv(c) * s + (size * spacing if i < len(text) - 1 else 0) for i, c in enumerate(text)]
    total = sum(widths); ang_total = total / r  # radians
    out = []
    a = math.radians(center_deg) - (ang_total / 2 if not bottom else -ang_total / 2)
    for c, w in zip(text, widths):
        gw = adv(c) * s
        mid = a + ((gw / 2) / r if not bottom else -(gw / 2) / r)
        if c != ' ':
            pen = SVGPathPen(gs)
            # glyph coords: x in [0,adv], y up. Centre glyph horizontally, flip y, then rotate onto the circle.
            th = mid  # angle from 12 o'clock, clockwise
            px, py = 256 + r * math.sin(th), 256 - r * math.cos(th)
            if not bottom:
                rot = th
                # baseline on circle radius r, glyph extends outward
                cos, sin = math.cos(rot), math.sin(rot)
                m = (s * cos, s * sin, s * sin, -s * cos, 0, 0)
            else:
                rot = th + math.pi
                cos, sin = math.cos(rot), math.sin(rot)
                m = (s * cos, s * sin, s * sin, -s * cos, 0, 0)
            # translate so glyph's horizontal centre sits on (px,py): offset -gw/2 along the tangent
            ox, oy = -(gw / 2) * cos, -(gw / 2) * sin
            tp = TransformPen(pen, (m[0], m[1], m[2], m[3], px + ox, py + oy))
            gs[cmap[ord(c)]].draw(tp)
            out.append(pen.getCommands())
        a += (w / r) if not bottom else -(w / r)
    return ''.join(out)
BEAR = ('M8 58C6 45 12 34 26 30C38 26 50 24 58 28C64 30 70 34 76 36C79 34 83 33 86 34L88 30L92 34C95 37 98 41 100 44'
        'L100 47C97 49 93 49 90 49C88 52 85 54 81 55L81 70L72 70L71 59C63 61 51 61 43 60L41 70L32 70L31 63'
        'C27 64 23 66 21 70L12 70C11 66 9 62 8 58Z')
def scene(cx=256, cy=256, r=150, uid='a'):
    """Mountains, pines and a walking bear inside a circle of radius r."""
    k = r / 150
    def P(x, y): return f'{cx + (x - 150) * k:.1f} {cy + (y - 150) * k:.1f}'
    mtn = f'M{P(0,190)}L{P(70,95)}L{P(105,135)}L{P(160,55)}L{P(230,150)}L{P(260,120)}L{P(300,175)}L{P(300,300)}L{P(0,300)}Z'
    snow = f'M{P(142,80)}L{P(160,55)}L{P(179,81)}L{P(168,76)}L{P(160,86)}L{P(151,76)}Z M{P(58,111)}L{P(70,95)}L{P(82,110)}L{P(75,107)}L{P(69,114)}L{P(63,107)}Z'
    def pine(x, base, h, w):
        return f'M{P(x,base-h)}L{P(x+w*.5,base-h*.55)}L{P(x+w*.25,base-h*.55)}L{P(x+w*.7,base-h*.15)}L{P(x+w*.1,base-h*.15)}L{P(x+w*.1,base)}L{P(x-w*.1,base)}L{P(x-w*.1,base-h*.15)}L{P(x-w*.7,base-h*.15)}L{P(x-w*.25,base-h*.55)}L{P(x-w*.5,base-h*.55)}Z'
    pines = ''.join(pine(*t) for t in [(38, 200, 95, 46), (72, 205, 70, 36), (236, 205, 88, 44), (268, 200, 62, 32)])
    bear_t = f'translate({cx - 72 * k:.1f} {cy + 18 * k:.1f}) scale({1.44 * k:.3f})'
    return (f'<clipPath id="c{uid}"><circle cx="{cx}" cy="{cy}" r="{r}"/></clipPath><g clip-path="url(#c{uid})">'
            f'<rect x="{cx-r}" y="{cy-r}" width="{2*r}" height="{2*r}" fill="#a9d3de"/>'
            f'<path d="{mtn}" fill="#5f8a9a"/><path d="{snow}" fill="#fff"/>'
            f'<path d="M{P(0,200)}C{P(80,180)} {P(220,180)} {P(300,200)}L{P(300,300)}L{P(0,300)}Z" fill="{GREEN}"/>'
            f'<path d="{pines}" fill="{PINE}"/>'
            f'<path d="M{P(0,258)}C{P(90,244)} {P(210,244)} {P(300,258)}L{P(300,300)}L{P(0,300)}Z" fill="{PINE}"/>'
            f'<path transform="{bear_t}" d="{BEAR}" fill="{BROWN}"/>'
            f'</g>')
def badge():
    top = arc_text('JUNK REMOVAL', 188, 46, 0)
    bot = arc_text('BIG BEAR', 188 + 34, 50, 180, bottom=True, spacing=0.1)
    dots = ''.join(f'<circle cx="{256 + 205 * math.sin(math.radians(d)):.1f}" cy="{256 - 205 * math.cos(math.radians(d)):.1f}" r="7" fill="{AMBER}"/>' for d in (-98, 98))
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" role="img" aria-label="Junk Removal Big Bear">'
            f'<title>Junk Removal Big Bear</title>'
            f'<circle cx="256" cy="256" r="254" fill="{PINE}"/><circle cx="256" cy="256" r="240" fill="{CREAM}"/>'
            f'<circle cx="256" cy="256" r="232" fill="none" stroke="{PINE}" stroke-width="3"/>'
            f'<path d="{top}" fill="{PINE}"/><path d="{bot}" fill="{PINE}"/>{dots}'
            f'<circle cx="256" cy="256" r="162" fill="{PINE}"/>' + scene(256, 256, 154, 'b') + '</svg>')
def mark():
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" role="img" aria-label="Junk Removal Big Bear">'
            f'<circle cx="256" cy="256" r="254" fill="{PINE}"/><circle cx="256" cy="256" r="232" fill="{CREAM}"/>'
            + scene(256, 256, 218, 'm') + '</svg>')
if __name__ == '__main__':
    for name, svg in [('images/logo.svg', badge()), ('images/logo-mark.svg', mark())]:
        open(name, 'w').write(svg); print(name, len(svg))
