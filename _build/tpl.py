"""Shared config, icons and page template for the Junk Removal Big Bear static site."""
import json, html, os
SITE = 'https://www.junkremovalbigbear.com'
TODAY = '2026-09-30'
# ---------------------------------------------------------------------------
# PHONE: confirmed by Nicholas (Sep 2026). Primary takes texts, WhatsApp and calls; every sms:/WhatsApp
# link and the schema telephone use it. The secondary number also takes texts and is shown only as an
# "or text" line on the contact page and in the footer.
PHONE_E164 = '+14252332945'
PHONE_DISPLAY = '(425) 233-2945'
PHONE2_E164 = '+19097442305'
PHONE2_DISPLAY = '(909) 744-2305'
_PH = PHONE_E164
BIZ = {
    'name': 'Junk Removal Big Bear',
    'phone': PHONE_DISPLAY,
    'tel': PHONE_E164,
    'tel_link': 'tel:' + PHONE_E164,  # customers mostly text or call (Nicholas, Sep 30 2026)
    'sms': 'sms:' + _PH,
    'wa': 'https://wa.me/' + _PH.lstrip('+'),
    'phone2': PHONE2_DISPLAY, 'tel2': PHONE2_E164, 'sms2': 'sms:' + PHONE2_E164,
    'years': 'over 20 years',  # confirmed by Nicholas (Sep 2026); don't claim more than this
    'email': 'junkremovalbigbear@gmail.com',  # approved for public use by Nicholas (Sep 30 2026); set '' to hide every email line/link/schema field
    'hours_text': '8:00 AM – 10:00 PM, 7 days a week',  # confirmed by Nicholas (Sep 2026)
    'opens': '08:00', 'closes': '22:00',
    'area_text': 'the Big Bear Valley and nearby mountain communities',
    'gbp': 'https://www.google.com/maps/search/?api=1&query=Junk%20Removal%20Big%20Bear&query_place_id=ChIJ75uRnPdVmUIRqmXds4EM6wQ',
    'gbp_cid': 'https://maps.google.com/?cid=354390746886661546',
    # Yelp listing verified via its Apple Maps place card (Sep 26 2026). Note: Yelp still shows an old street address + hours; Nicholas to fix.
    'yelp': 'https://www.yelp.com/biz/junk-removal-big-bear-big-bear-lake',
}
PH_TODO = ''  # phone confirmed; kept so templates can still reference it
AREAS = [  # slug, name, note
    ('big-bear-lake', 'Big Bear Lake'), ('big-bear-city', 'Big Bear City'), ('moonridge', 'Moonridge'),
    ('sugarloaf', 'Sugarloaf'), ('fawnskin', 'Fawnskin'), ('erwin-lake-baldwin-lake', 'Erwin Lake & Baldwin Lake'),
]
SERVICES = [  # path, name, short blurb, icon
    ('/weed-abatement/', 'Weed Clearing & Abatement', 'Weeds, pine needles, brush and low limbs cleared to Big Bear Fire standards — and hauled away the same visit.', 'leaf'),
    ('/services/junk-removal/', 'Junk Hauling', 'Single items to full loads — furniture, mattresses, yard debris and everything in between.', 'truck'),
    ('/services/cabin-cleanouts/', 'Cabin, Garage & Home Cleanouts', 'Garages, attics, crawl spaces, sheds, storage units and whole-cabin clearances.', 'home'),
    ('/services/estate-cleanouts/', 'Estate Cleanouts', 'Respectful, organized cleanouts of inherited cabins and homes — manageable from off the mountain.', 'key'),
    ('/vacation-rental-turnovers/', 'Vacation Rental Turnovers', 'Bulky-item and junk removal for Airbnb and VRBO hosts, scheduled between guest stays.', 'calendar'),
    ('/services/appliance-e-waste-removal/', 'Appliance & E-Waste Removal', 'Fridges, freezers, washers, dryers, stoves, TVs and computers hauled away.', 'fridge'),
    ('/services/hot-tub-removal/', 'Hot Tub & Spa Removal', 'Dead spas drained, cut down, carried off the deck and hauled away.', 'tub'),
    ('/services/light-demolition/', 'Light Demolition', 'Minor tear-outs: small sheds, deck boards, fencing, cabinets and carpet — hauled off.', 'hammer'),
    ('/services/painting/', 'Painting (Minor Jobs)', 'Minor interior and exterior jobs — walls, ceilings and trim inside; siding touch-ups, decks and fences outside.', 'brush'),
]
FURNITURE = ('/services/furniture-removal/', 'Furniture & Mattress Removal', 'Sofas, beds, mattresses, dressers and patio sets carried out and hauled away.', 'sofa')
SERVICES_ALL = SERVICES + [FURNITURE]  # footer, schema, area pages, llms
LICENSE_NOTE = 'Junk Removal Big Bear is not a licensed contractor. Painting, light demolition and similar work is limited to minor jobs under $1,000 total (labor and materials) that don\'t need a building permit, as California law allows.'
_P = 'fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"'
ICONS = {
 'phone': f'<svg viewBox="0 0 24 24" {_P} aria-hidden="true"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/></svg>',
 'msg': f'<svg viewBox="0 0 24 24" {_P} aria-hidden="true"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>',
 'sofa': f'<svg viewBox="0 0 24 24" {_P} aria-hidden="true"><path d="M4 11V8a3 3 0 0 1 3-3h10a3 3 0 0 1 3 3v3"/><path d="M2 13a2 2 0 0 1 4 0v2h12v-2a2 2 0 0 1 4 0v5H2z"/><path d="M5 18v2M19 18v2"/></svg>',
 'fridge': f'<svg viewBox="0 0 24 24" {_P} aria-hidden="true"><rect x="5" y="2" width="14" height="20" rx="2"/><path d="M5 10h14M9 6v1M9 13v3"/></svg>',
 'home': f'<svg viewBox="0 0 24 24" {_P} aria-hidden="true"><path d="M3 11l9-7 9 7"/><path d="M5 10v10h14V10"/><path d="M10 20v-5h4v5"/></svg>',
 'key': f'<svg viewBox="0 0 24 24" {_P} aria-hidden="true"><circle cx="8" cy="15" r="4"/><path d="M11 12l9-9M17 6l3 3M14 9l2 2"/></svg>',
 'calendar': f'<svg viewBox="0 0 24 24" {_P} aria-hidden="true"><rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18M8 15l2 2 4-4"/></svg>',
 'tub': f'<svg viewBox="0 0 24 24" {_P} aria-hidden="true"><path d="M3 12h18v3a5 5 0 0 1-5 5H8a5 5 0 0 1-5-5z"/><path d="M6 12V5a2 2 0 0 1 4 0M7 20l-1 2M17 20l1 2"/></svg>',
 'hammer': f'<svg viewBox="0 0 24 24" {_P} aria-hidden="true"><path d="M15 12l-8.5 8.5a2.1 2.1 0 0 1-3-3L12 9"/><path d="M17.6 15L22 10.6 13.4 2 9 6.4z"/></svg>',
 'leaf': f'<svg viewBox="0 0 24 24" {_P} aria-hidden="true"><path d="M11 20A7 7 0 0 1 4 13c0-6 7-10 16-10 0 9-4 16-10 16z"/><path d="M4 21c4-4 7-7 11-10"/></svg>',
 'pin': f'<svg viewBox="0 0 24 24" {_P} aria-hidden="true"><path d="M12 22s7-6.2 7-12a7 7 0 0 0-14 0c0 5.8 7 12 7 12z"/><circle cx="12" cy="10" r="2.5"/></svg>',
 'truck': f'<svg viewBox="0 0 24 24" {_P} aria-hidden="true"><path d="M1 4h13v12H1zM14 8h4l4 4v4h-8z"/><circle cx="5.5" cy="18.5" r="2"/><circle cx="18.5" cy="18.5" r="2"/></svg>',
 'brush': f'<svg viewBox="0 0 24 24" {_P} aria-hidden="true"><path d="M18 2l4 4-9 9-4-4z"/><path d="M9 11c-3 0-5 2-5 5 0 2-2 3-3 3 2 2 5 3 8 1 2-1 3-3 3-5"/></svg>',
 'wa': f'<svg viewBox="0 0 24 24" {_P} aria-hidden="true"><path d="M3 21l1.6-4.7A8.5 8.5 0 1 1 8 19.6z"/><path d="M9 8.5c0 3.5 3 6.5 6.5 6.5l1-1.5-2-1-1 .8c-1-.4-2.4-1.8-2.8-2.8l.8-1-1-2z"/></svg>',
 'book': f'<svg viewBox="0 0 24 24" {_P} aria-hidden="true"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20V2H6.5A2.5 2.5 0 0 0 4 4.5z"/><path d="M4 19.5A2.5 2.5 0 0 0 6.5 22H20v-5"/></svg>',
}
def esc(s): return html.escape(s, quote=True)
def ld(obj): return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False, separators=(',', ':')) + '</script>'
AREA_NAMES = ['Big Bear Lake', 'Big Bear City', 'Moonridge', 'Sugarloaf', 'Fawnskin', 'Erwin Lake', 'Baldwin Lake']
_WIKI = 'https://en.wikipedia.org/wiki/'
# Only Wikipedia articles verified to exist (Sep 2026); Moonridge, Erwin Lake and Baldwin Lake have no specific article.
PLACE_SAMEAS = {'Big Bear Lake': _WIKI + 'Big_Bear_Lake,_California', 'Big Bear City': _WIKI + 'Big_Bear_City,_California',
                'Sugarloaf': _WIKI + 'Sugarloaf,_California', 'Fawnskin': _WIKI + 'Fawnskin,_California'}
_COUNTY = {'@type': 'AdministrativeArea', 'name': 'San Bernardino County, California'}
def place(n):
    """Big Bear Lake is an incorporated city; the others are unincorporated communities (schema.org Place)."""
    d = {'@type': 'City' if n == 'Big Bear Lake' else 'Place', 'name': n + ', CA', 'containedInPlace': _COUNTY}
    if n in PLACE_SAMEAS: d['sameAs'] = PLACE_SAMEAS[n]
    return d
def area_served(names=None):
    if names: return [place(n) for n in names]
    return [{'@type': 'Place', 'name': 'Big Bear Valley, CA', 'sameAs': _WIKI + 'Big_Bear_Valley', 'containedInPlace': _COUNTY}] + [place(n) for n in AREA_NAMES]
def business_ld():
    d = {
        '@context': 'https://schema.org', '@type': 'HomeAndConstructionBusiness', '@id': SITE + '/#business',
        'name': BIZ['name'], 'url': SITE + '/',
        'telephone': BIZ['tel'],
        'logo': {'@type': 'ImageObject', 'url': SITE + '/images/opt/logo-512.png', 'width': 512, 'height': 512},
        'image': [SITE + '/images/opt/logo-512.png', SITE + '/images/opt/og-junk-removal-big-bear.jpg'],
        'description': 'Junk removal, weed clearing and fire abatement, cabin, garage, estate and vacation-rental cleanouts, appliance and e-waste removal, hot tub removal, light demolition and minor interior and exterior painting in the Big Bear Valley, California. Free on-site quotes.',
        'areaServed': area_served(),
        'openingHours': 'Mo-Su 08:00-22:00',
        'openingHoursSpecification': [{'@type': 'OpeningHoursSpecification', 'dayOfWeek': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], 'opens': BIZ['opens'], 'closes': BIZ['closes']}],
        'sameAs': [BIZ['gbp_cid'], BIZ['yelp']],
        'hasMap': BIZ['gbp_cid'],
        **({'email': BIZ['email']} if BIZ['email'] else {}),
        'knowsAbout': ['Junk removal', 'Weed abatement', 'Weed and brush clearing', 'Defensible space clearing', 'Cabin cleanouts', 'Estate cleanouts', 'Hot tub removal',
                       'Appliance and e-waste removal', 'Furniture and mattress removal', 'Vacation rental turnovers', 'Light demolition (minor jobs)', 'Painting (minor jobs)', 'Big Bear Valley disposal rules'],
        'hasOfferCatalog': {'@type': 'OfferCatalog', 'name': 'Services', 'itemListElement': [
            {'@type': 'Offer', 'itemOffered': {'@type': 'Service', 'name': n, 'url': SITE + p}} for p, n, _, _ in SERVICES_ALL]},
    }
    if BIZ['tel2']: d['contactPoint'] = [
        {'@type': 'ContactPoint', 'contactType': 'customer service', 'telephone': BIZ['tel'], 'areaServed': 'US', 'availableLanguage': 'English',
         'description': 'Call or text', 'hoursAvailable': {'@type': 'OpeningHoursSpecification', 'dayOfWeek': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], 'opens': BIZ['opens'], 'closes': BIZ['closes']}},
        {'@type': 'ContactPoint', 'contactType': 'customer service', 'telephone': BIZ['tel2'], 'areaServed': 'US', 'availableLanguage': 'English', 'description': 'Secondary number, also takes texts'}]
    return d
def crumbs_ld(items):
    return {'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': [
        {'@type': 'ListItem', 'position': i + 1, 'name': n, 'item': SITE + p} for i, (n, p) in enumerate(items)]}
def strip_tags(s):
    import re
    return re.sub(r'\s+', ' ', re.sub(r'<!--.*?-->|<[^>]+>', '', s)).strip()
def faq_ld(faqs, path):
    return {'@context': 'https://schema.org', '@type': 'FAQPage', '@id': SITE + path + '#faq', 'mainEntity': [
        {'@type': 'Question', 'name': strip_tags(q), 'acceptedAnswer': {'@type': 'Answer', 'text': html.unescape(strip_tags(a))}} for q, a in faqs]}
def service_ld(name, desc, path, area_names=None, stype=None):
    return {'@context': 'https://schema.org', '@type': 'Service', 'name': name, 'serviceType': stype or name, 'description': desc,
            'url': SITE + path, 'provider': {'@id': SITE + '/#business'},
            'areaServed': area_served(area_names)}
def btns(dark=True):
    sec = 'btn-ghost' if dark else 'btn-line'
    return (f'<div class="cta-row">{PH_TODO}<a class="btn btn-amber" href="{BIZ["sms"]}">{ICONS["msg"]}Text photos for a free quote</a>'
            f'<a class="btn {sec}" href="{BIZ["tel_link"]}">{ICONS["phone"]}Call {BIZ["phone"]}</a></div>'
            f'<p class="cta-alt small">Prefer WhatsApp? <a href="{BIZ["wa"]}" rel="noopener">Message us on WhatsApp</a></p>')
def btns_light(): return btns(False)
PHOTOS = {  # name: (master width, master height) after the 4:3 crop - photos from the old site, see _build/images.py
    'junk-removal-crew-loading-truck': (1024, 768), 'junk-removal-crew-armchair-truck': (1024, 768), 'mattress-removal-crew': (1024, 768),
    'hot-tub-removal-deck': (1024, 768), 'junk-hauling-box-truck': (1024, 768), 'cabinet-tear-out': (1024, 768),
    'shrub-trimming-ladder-fuel': (1024, 768), 'weed-clearing-crew': (1024, 768), 'wildfire-dry-brush': (1024, 768),
    'appliances-electronics-pile': (794, 596), 'mountain-cabin-pines': (1024, 768), 'yard-junk-pile': (1024, 768)}
def photo_widths(W):
    """480/768/1024 variants, never upscaled; the master width is added only if it is well above the largest variant."""
    ws = [w for w in (480, 768, 1024) if w <= W]
    return ws + [W] if W - ws[-1] > 100 else ws
def _img(name, alt, sizes, eager=False):
    W, H = PHOTOS[name]; ws = photo_widths(W)
    srcset = ', '.join(f'/images/opt/{name}-{w}.webp {w}w' for w in ws)
    load = 'fetchpriority="high"' if eager else 'loading="lazy"'
    return (f'<img {load} decoding="async" src="/images/opt/{name}-{ws[0]}.webp" srcset="{srcset}" sizes="{sizes}" '
            f'width="{W}" height="{H}" alt="{esc(alt)}">')
def fig(name, alt, cap='', maxw=620):
    """Lazy, responsive figure for a photo from the old site. Neutral, descriptive alt text; no caption by default."""
    fc = f'<figcaption>{cap}</figcaption>' if cap else ''
    return (f'<figure class="photo nat" style="max-width:{maxw}px">'
            + _img(name, alt, f'(min-width: {maxw + 36}px) {maxw}px, calc(100vw - 36px)') + f'{fc}</figure>')
def hero_pic(name, alt):
    """Photo in the right column of a page hero (below the buttons on mobile). Not lazy: it can be the LCP element."""
    return '<figure class="hero-pic">' + _img(name, alt, '(min-width: 1120px) 420px, (min-width: 900px) 38vw, calc(100vw - 36px)', eager=True) + '</figure>'
def gallery(items):
    """Row of linked photos: items = [(name, alt, href, label)]."""
    return '<div class="gallery">' + ''.join(
        f'<a class="gal" href="{h}">' + _img(n, a, ('(min-width: 960px) 348px, calc(100vw - 36px)' if i == 0 else '(min-width: 1120px) 348px, (min-width: 960px) 31vw, calc(50vw - 24px)')) + f'<span>{l} →</span></a>'
        for i, (n, a, h, l) in enumerate(items)) + '</div>'
def photo_slot(what):
    """Placeholder for a real photo from Nicholas. Invisible in production; the preview build makes it visible."""
    return f'<!-- PHOTO-SLOT: {what} -->'
NAV = [('/', 'Home'), ('/services/', 'Services'), ('/location/', 'Service Areas'), ('/vacation-rental-turnovers/', 'Vacation Rentals'), ('/guides/', 'Guides'), ('/contact/', 'Contact')]
def header(path):
    def links():
        out = []
        for p, n in NAV:
            cur = ' aria-current="page"' if (p == path or (p != '/' and path.startswith(p))) else ''
            out.append(f'<a href="{p}"{cur}>{n}</a>')
        return ''.join(out)
    return f'''<a class="skip" href="#main">Skip to content</a>
<header class="site-head"><div class="wrap head-in">
<a class="brand" href="/"><img src="/images/opt/logo-96.webp" srcset="/images/opt/logo-96.webp 96w, /images/opt/logo-192.webp 192w" sizes="42px" width="42" height="42" alt="">Junk Removal <span>Big Bear</span></a>
<nav class="desk-nav" aria-label="Main">{links()}</nav>
<a class="btn btn-amber btn-sm head-call" href="{BIZ["sms"]}">{ICONS["msg"]}Text for a free quote</a>
<details class="menu"><summary>Menu</summary><nav aria-label="Main (mobile)">{links()}<a href="/weed-abatement/">Weed Abatement</a></nav></details>
</div></header>'''
def page_hero(crumbs, eyebrow, h1, lead, extra='', img=None):
    cr = ''.join(f'<li><a href="{p}">{esc(n)}</a></li>' if i < len(crumbs) - 1 else f'<li aria-current="page">{esc(n)}</li>' for i, (n, p) in enumerate(crumbs))
    txt = f'''<nav class="crumbs" aria-label="Breadcrumb"><ol>{cr}</ol></nav>
<span class="eyebrow">{eyebrow}</span><h1>{h1}</h1><p class="lead">{lead}</p>{btns()}{extra}'''
    if img: return f'<section class="hero page-hero has-pic"><div class="wrap hero-split"><div>{txt}</div>{hero_pic(*img)}</div></section>'
    return f'''<section class="hero page-hero"><div class="wrap">
{txt}
</div></section>'''
def faq_html(faqs, title='Frequently asked questions'):
    items = ''.join(f'<details><summary>{q}</summary><div><p>{a}</p></div></details>' for q, a in faqs)
    return f'<section class="alt" id="faq"><div class="wrap narrow"><h2>{title}</h2><div class="faq">{items}</div></div></section>'
def cta_band(h='Book your free on-site quote', p='Text us a few photos or give us a call, and we\'ll come out and look. Free, no obligation.'):
    return f'<section class="cta-band"><div class="wrap"><h2>{h}</h2><p>{p}</p>{btns()}</div></section>'
def EMAIL_LINE():
    return f'Email: <a href="mailto:{BIZ["email"]}">{BIZ["email"]}</a><br>' if BIZ['email'] else ''
def contact_box():
    return f'''<aside class="box sticky"><h2 style="font-size:1.15rem">Free on-site quote</h2>
<p class="muted small">Text 2–3 photos and your neighborhood, or call and ask us to come out and quote it in person — free, no obligation.</p>
{PH_TODO}<p><a class="btn btn-amber" style="width:100%" href="{BIZ["sms"]}">{ICONS["msg"]}Text photos</a></p>
<p><a class="btn btn-line" style="width:100%" href="{BIZ["tel_link"]}">{ICONS["phone"]}Call {BIZ["phone"]}</a></p>
<p><a class="btn btn-line" style="width:100%" href="{BIZ["wa"]}" rel="noopener">{ICONS["wa"]}WhatsApp us</a></p>
<p class="small muted">{EMAIL_LINE()}Hours: {BIZ["hours_text"]}</p></aside>'''
def footer():
    svc = ''.join(f'<li><a href="{p}">{n}</a></li>' for p, n, _, _ in SERVICES_ALL)
    areas = ''.join(f'<li><a href="/location/{s}/">{n}</a></li>' for s, n in AREAS)
    return f'''<footer class="site-foot"><div class="wrap"><div class="foot-grid">
<div><h2>{BIZ["name"]}</h2>
<p>Serving {BIZ["area_text"]}. We come to you.</p>
<p>Call or text: <a href="{BIZ["tel_link"]}">{BIZ["phone"]}</a> · <a href="{BIZ["sms"]}">Text</a> · <a href="{BIZ["wa"]}" rel="noopener">WhatsApp</a><br>
Or text: <a href="{BIZ["sms2"]}">{BIZ["phone2"]}</a><br>
{EMAIL_LINE()}Hours: {BIZ["hours_text"]}</p>
<p><a href="{BIZ["gbp"]}" rel="noopener">Find us on Google Maps</a></p></div>
<div><h2>Services</h2><ul>{svc}</ul></div>
<div><h2>Service areas</h2><ul>{areas}<li><a href="/location/">All service areas</a></li></ul></div>
<div><h2>Help</h2><ul><li><a href="/guides/">Local guides</a></li><li><a href="/guides/big-bear-fire-abatement-letter/">Fire abatement letter guide</a></li><li><a href="/guides/big-bear-dump-transfer-station-guide/">Big Bear dump &amp; transfer station</a></li><li><a href="/contact/">Contact &amp; free quotes</a></li></ul></div>
</div><p class="legal">© 2026 {BIZ["name"]}. {LICENSE_NOTE} We don't haul hazardous waste (paint, chemicals, oil, asbestos, propane tanks). Scenery photos: Unsplash (Joshua Chun, Dušan veverkolog).</p></div></footer>
<div class="callbar">{PH_TODO}<a class="c1" href="{BIZ["sms"]}">{ICONS["msg"]}Text photos</a><a class="c2" href="{BIZ["tel_link"]}">{ICONS["phone"]}Call</a></div>'''
def page(path, title, desc, body, schema, og_type='website', robots='index, follow', canonical=True):
    url = SITE + path
    schemas = ''.join(ld(s) for s in schema)
    can = f'<link rel="canonical" href="{url}">' if canonical else ''
    return f'''<!DOCTYPE html>
<html lang="en-US">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
{can}
<meta name="robots" content="{robots}">
<meta name="theme-color" content="#1d3a2e">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="stylesheet" href="/style.css">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="{BIZ["name"]}">
<meta property="og:locale" content="en_US">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/images/opt/og-junk-removal-big-bear.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Junk Removal Big Bear logo, services and phone number">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(desc)}">
<meta name="twitter:image" content="{SITE}/images/opt/og-junk-removal-big-bear.jpg">
{schemas}
</head>
<body>
{header(path)}
<main id="main">
{body}
</main>
{footer()}
</body>
</html>
'''
def write(path, content):
    """Production output: HTML comments (PHOTO-SLOT markers, TODO notes for Nicholas) are stripped unless KEEP_COMMENTS=1
    (make_preview.py needs them to draw the dashed photo-slot boxes)."""
    import re
    if path.endswith(('/', '.html')) and not os.environ.get('KEEP_COMMENTS'):
        content = re.sub(r'<!--.*?-->', '', content, flags=re.S)
    fp = path.lstrip('/')
    fp = fp + 'index.html' if (fp == '' or fp.endswith('/')) else fp
    d = os.path.dirname(fp)
    if d: os.makedirs(d, exist_ok=True)
    with open(fp, 'w') as f: f.write(content)
    return fp
