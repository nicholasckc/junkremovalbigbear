"""Build the static site into the repo root.  Usage (from repo root):  python3 _build/build.py
Edits made directly to generated HTML will be overwritten on the next build — edit the _build/*.py content instead."""
import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
from tpl import *
from content_services import SERVICES_CONTENT
from content_areas import AREAS_CONTENT, SRC
PAGES = []  # (path, priority)
def emit(path, html_, prio='0.7'):
    write(path, html_); PAGES.append((path, prio))
ALL_AREAS = ['Big Bear Lake', 'Big Bear City', 'Moonridge', 'Sugarloaf', 'Fawnskin', 'Erwin Lake', 'Baldwin Lake']
def svc_cards(items=SERVICES, cls='grid grid-3'):
    return f'<div class="{cls}">' + ''.join(
        f'<a class="card" href="{p}"><div class="ico">{ICONS[i]}</div><h3>{n}</h3><p>{d}</p><span class="more">Learn more →</span></a>' for p, n, d, i in items) + '</div>'
def area_chips():
    return '<ul class="chips">' + ''.join(f'<li><a href="/location/{s}/">{n}</a></li>' for s, n in AREAS) + '</ul>'
TAKE = '''<div class="grid grid-2"><div class="card"><h3>We take</h3><ul>
<li>Furniture and mattresses</li><li>Appliances and electronics</li><li>Hot tubs and spas</li><li>Garage, shed, attic and storage-unit contents</li>
<li>Exercise equipment</li><li>Yard waste, branches and storm debris</li><li>Light construction and tear-out debris — lumber, drywall, fencing, carpet</li><li>Whole-home and estate contents</li></ul></div>
<div class="card"><h3>We can't take</h3><ul><li>Paint and chemicals</li><li>Motor oil and fuels</li><li>Asbestos</li><li>Propane tanks</li></ul>
<p class="small">For these, use San Bernardino County Fire's household hazardous waste program — the Big Bear drop-off is at 42040 Garstin Dr (check current hours before you go).</p></div></div>'''
TRUST = f'''<ul class="facts">
<li><b>Over 20 years in business.</b> Hauling, cleanouts and yard clearing, done by people who know mountain properties.</li>
<li><b>Free on-site quotes.</b> We come out, look at the job and give you a firm price — free, no obligation. Photos by text or WhatsApp work too.</li>
<li><b>Price confirmed before we start.</b> No surprises on the day.</li>
<li><b>Open 7 days.</b> {BIZ["hours_text"]}. Same-day when the schedule allows.</li>
<li><b>Off-mountain owners welcome.</b> Lockbox or gate-code access, and before-and-after photos when we finish.</li>
<li><b>Clearing and hauling in one visit.</b> Weed clearing, cleanouts and tear-outs end with the debris gone, not piled at the curb.</li>
<li><b>Reviews on Google.</b> <a href="{BIZ["gbp"]}" rel="noopener">See what customers say on our Google profile</a>.</li>
</ul>'''
HOME_FAQ = [
 ('How much does junk removal or weed clearing cost?', 'Every mountain job is different, so we don\'t publish prices. We give free on-site quotes (or quotes from photos) and confirm the price before any work starts.'),
 ('Do you offer free on-site quotes?', 'Yes. We come to your property anywhere in the Big Bear Valley, look at the job and give you a firm price — free and with no obligation.'),
 ('I got a weed abatement letter. Can you help?', 'Yes. We clear weeds, pine needles, brush and low limbs to Big Bear Fire\'s defensible space checklist and haul the debris away the same visit. See our weed clearing page and abatement letter guide.'),
 ('Can you remove junk from my cabin if I\'m not in Big Bear?', 'Yes. Send photos, give us access (lockbox, gate code or a neighbor), and we send before-and-after photos when the job is done.'),
 ('What are your hours?', f'{BIZ["hours_text"]}.'),
 ('What areas do you serve?', 'The Big Bear Valley — Big Bear Lake, Big Bear City, Moonridge, Sugarloaf, Fawnskin, Erwin Lake and Baldwin Lake — and nearby mountain communities by arrangement.'),
 ('What can\'t you take?', 'Hazardous materials — paint, chemicals, oil, fuels, asbestos and propane tanks.'),
]
def home():
    body = f'''<section class="hero hero-photo"><img class="hero-bg" src="/images/opt/big-bear-lake-pines-800.webp" srcset="/images/opt/big-bear-lake-pines-800.webp 800w, /images/opt/big-bear-lake-pines-1400.webp 1400w" sizes="100vw" width="1400" height="933" alt="" fetchpriority="high">
<div class="wrap hero-grid"><div>
<span class="eyebrow">Free on-site quotes · 7 days a week</span>
<h1>Junk Removal &amp; Weed Clearing in Big Bear, CA</h1>
<p class="lead">Junk hauled, cabins and garages cleared out, and weeds and pine needles cleared to fire-department standards — by a local crew that hauls it all away.</p>
{btns()}
<ul class="ticks"><li>Over 20 years in business</li><li>Free on-site quotes — or text us photos</li><li>Weed abatement letter? We clear it and haul it in one visit</li><li>Open {BIZ["hours_text"]}</li></ul>
</div><img class="hero-badge" loading="lazy" decoding="async" src="/images/opt/logo-384.webp" srcset="/images/opt/logo-384.webp 384w, /images/opt/logo-600.webp 600w" sizes="300px" width="300" height="300" alt="Junk Removal Big Bear logo"></div></section>
{photo_slot('real photo of Nicholas/crew or truck at work (no customer faces or house numbers)')}
<section><div class="wrap"><h2>What we do</h2><p class="sec-intro">Everything except moving. Pick a service for details and local tips.</p>
{svc_cards()}</div></section>
<section class="alt"><div class="wrap two"><div>
<span class="eyebrow" style="color:#7a4d05">Fire season</span><h2>Got a weed abatement letter?</h2>
<p>Big Bear Fire mails abatement letters to property owners every year, and the letter <b>is</b> your warning — a separate notice before a citation isn't guaranteed. Their defensible-space checklist covers pine needles, weeds, brush, low limbs and even junk and lumber stored on the property.</p>
<p>We clear it to the checklist and haul everything away on the same visit, and we can do it while you're off the mountain.</p>
<p><a class="btn btn-amber" href="/weed-abatement/">{ICONS["leaf"]}Weed clearing &amp; abatement</a></p>
<p><a href="/guides/big-bear-fire-abatement-letter/">Read: what to do when you get the letter →</a></p></div>
<figure class="photo"><img loading="lazy" decoding="async" src="/images/opt/pine-cone-needles-800.webp" width="720" height="591" alt="Pine needles and pine cones"><figcaption>Pine needles and cones pile up fast under Big Bear's pines. (Stock photo)</figcaption></figure>
</div></section>
<section><div class="wrap"><h2>How it works</h2>
<ol class="steps"><li><b>Book a free on-site quote</b>Text or WhatsApp us, or send 2–3 photos for a quick answer.</li>
<li><b>Get a firm price</b>We confirm the price before any work starts. No obligation.</li>
<li><b>We clear, load and haul</b>From inside the cabin, the garage, the yard or the deck — then sweep up.</li></ol></div></section>
<section class="alt"><div class="wrap"><h2>Why Big Bear owners call us</h2>{TRUST}</div></section>
<section><div class="wrap"><h2>What we take (and what we can't)</h2>{TAKE}</div></section>
<section class="alt"><div class="wrap"><h2>Service areas</h2><p class="sec-intro">The whole Big Bear Valley, plus nearby mountain communities by arrangement. Each area page covers local trash rules, dump options and access tips.</p>{area_chips()}
<p style="margin-top:14px"><a href="/location/">See all service areas →</a></p></div></section>
<section><div class="wrap two"><div><h2>Why we quote on-site, for free</h2>
<p>Mountain jobs are all different — steep driveways, loft stairs, decks over a slope, snow. So we don't publish price lists. We come out, look at the job, and give you a firm quote before we touch anything. It costs you nothing, and there's no obligation.</p>{btns_light()}</div>
{fig('yard-junk-pile', 'Backyard junk pile: a green bin full of scrap wood and a broken chair frame, with old tires and bagged debris on the lawn by a white fence')}</div></section>
{faq_html(HOME_FAQ)}
<section class="alt"><div class="wrap"><h2>Local guides</h2><div class="grid grid-3">
<a class="card" href="/guides/big-bear-fire-abatement-letter/"><div class="ico">{ICONS["leaf"]}</div><h3>Got a fire abatement letter?</h3><p>What it means and how to comply.</p></a>
<a class="card" href="/guides/big-bear-dump-transfer-station-guide/"><div class="ico">{ICONS["pin"]}</div><h3>Where to take junk in Big Bear</h3><p>Transfer station, bulky pickup and drop-off rules by area.</p></a>
<a class="card" href="/guides/hot-tub-removal-big-bear/"><div class="ico">{ICONS["tub"]}</div><h3>Hot tub removal, explained</h3><p>Getting a dead spa off a mountain deck.</p></a></div></div></section>
{cta_band('Book your free on-site quote')}'''
    emit('/', page('/', 'Junk Removal & Weed Clearing in Big Bear, CA | Free On-Site Quotes',
        'Junk removal, weed clearing & fire abatement, cabin and estate cleanouts, hot tub removal and e-waste pickup across the Big Bear Valley. Free on-site quotes, 7 days a week.',
        body, [business_ld(), {'@context': 'https://schema.org', '@type': 'WebSite', '@id': SITE + '/#website', 'name': BIZ['name'], 'url': SITE + '/', 'publisher': {'@id': SITE + '/#business'}}, faq_ld(HOME_FAQ, '/')]), '1.0')

def services_hub():
    crumbs = [('Home', '/'), ('Services', '/services/')]
    extra = [('/services/furniture-removal/', 'Furniture & Mattress Removal', 'Sofas, beds, mattresses, dressers and patio sets carried out and hauled away.', 'sofa')]
    body = page_hero(crumbs, 'Services', 'Junk Removal, Cleanouts &amp; Weed Clearing Services in Big Bear', 'One local crew for hauling, cleanouts, weed clearing and minor tear-outs across the Big Bear Valley. Everything except moving.') + \
        f'<section><div class="wrap">{svc_cards(SERVICES + extra)}<p class="small muted" style="margin-top:16px">{LICENSE_NOTE}</p></div></section><section class="alt"><div class="wrap"><h2>What we take (and what we can\'t)</h2>{TAKE}</div></section>{cta_band()}'
    emit('/services/', page('/services/', 'Services | Junk Removal, Cleanouts & Weed Clearing in Big Bear, CA',
        'Junk removal, weed clearing, cabin, estate and vacation-rental cleanouts, appliance and e-waste removal, hot tub removal, light demolition and minor interior and exterior painting in Big Bear.',
        body, [business_ld(), crumbs_ld(crumbs)]), '0.8')

def service_pages():
    for slug, c in SERVICES_CONTENT.items():
        path = f'/services/{slug}/'
        crumbs = [('Home', '/'), ('Services', '/services/'), (c['name'], path)]
        secs = ''.join(f'<h2>{h}</h2>{b}' + (fig(*c['img']) if i == 0 and c.get('img') else '') for i, (h, b) in enumerate(c['sections']))
        rel = [s for s in SERVICES + [('/services/furniture-removal/', 'Furniture & Mattress Removal', 'Sofas, beds, mattresses and patio sets hauled away.', 'sofa')] if s[0] in c['related']]
        relg = [('/guides/' + x.split('/guides/')[1], x) for x in c['related'] if '/guides/' in x]
        guide_links = ''.join(f'<li><a href="{x}">Guide: {GUIDE_TITLES.get(x, "Local guide")}</a></li>' for _, x in relg)
        body = page_hero(crumbs, 'Free on-site quotes · Big Bear Valley', c['h1'], c['lead']) + photo_slot(f'real photo for {c["name"]} (crew/truck/finished result; no customer faces)') + f'''<section><div class="wrap two"><div class="prose">{secs}
<h2>Where we do this</h2><p>All over the Big Bear Valley:</p>{area_chips()}</div>{contact_box()}</div></section>
{faq_html(c['faqs'])}
<section><div class="wrap"><h2>Related</h2>{svc_cards(rel)}{'<ul style="margin-top:14px">' + guide_links + '</ul>' if guide_links else ''}</div></section>{cta_band()}'''
        emit(path, page(path, c['title'], c['desc'], body, [business_ld(), service_ld(c['name'], strip_tags(c['lead']), path, stype=c['stype']), faq_ld(c['faqs'], path), crumbs_ld(crumbs)]), '0.8')
VRT_FAQ = [
 ('Can you remove junk between guest checkout and check-in?', 'Yes. Send photos and your checkout and check-in times, and we schedule inside that window, 7 days a week, subject to availability.'),
 ('Can my property manager arrange everything?', 'Yes. Managers and co-hosts can send photos, approve quotes and arrange lockbox access. We send before-and-after photos when we lock up.'),
 ('Do you remove old hot tubs from rentals?', 'Yes. After a technician disconnects power and plumbing, we cut down, remove and haul away the spa.'),
 ('Do you do the regular cleaning?', 'No. We handle bulky items and junk — the things too big for your cleaning crew.'),
]
def vrt():
    path = '/vacation-rental-turnovers/'
    crumbs = [('Home', '/'), ('Vacation Rental Turnovers', path)]
    body = page_hero(crumbs, 'For Airbnb &amp; VRBO hosts and property managers', 'Vacation Rental Turnovers &amp; Cabin Cleanouts in Big Bear',
        'Broken furniture, a dead hot tub, guest-left junk or an overflowing bin — we clear the bulky stuff between checkout and check-in so the next guest never sees it.') + f'''
<section><div class="wrap two"><div class="prose">
<h2>What we handle for hosts</h2><ul>
<li><b>Furniture and mattress haul-away</b> — the old piece goes the day the new one arrives</li>
<li><b>Cabin cleanouts</b> — garages, lofts and storage rooms cleared between seasons</li>
<li><b>Weed clearing</b> — pine needles and brush cleared before fire season, hauled the same visit</li>
<li><b>Minor paint touch-ups</b> — scuffed walls and trim after furniture comes out</li>
<li><b>Guest-left bulky items</b> — broken sleds, chairs, coolers, holiday overflow</li>
<li><b>Hot tub removal</b> — failed spas cut down and hauled off the deck</li>
<li><b>Appliance haul-away</b> — the dead fridge or washer out</li>
<li><b>Deck, garage and storage clear-outs</b> — before listing photos or inspections</li>
<li><b>Full refresh cleanouts</b> — new owner, rebrand or sale</li></ul>
{fig('mountain-cabin-pines', 'Two-story wood cabin with lit windows among tall pines, with a snow-patched forested hillside behind')}
<!-- Removed from current site: handyman work, spa cleaning, "new furniture placed" (moving-type service). -->
<h2>Trash rules hosts get fined for</h2>
<p><b>Inside the City of Big Bear Lake (92315)</b> you need a city vacation rental license. Cans can't sit at the curb more than 24 hours, and operational violations are fined $500 for a first, $1,000 for a second and $1,500 for a third violation within 12 months.</p>
<p><b>Outside city limits</b> (Big Bear City, Fawnskin, Sugarloaf, the county side of Moonridge) you need a San Bernardino County short-term rental permit. County rules require animal-proof containers in the mountain region, trash removal after each stay, and containers out no sooner than 12 hours before pickup and back within 24 hours after.</p>
<p>When a holiday weekend overflows the bins, we can take the excess away before the next check-in. Read the <a href="/guides/airbnb-turnover-checklist-big-bear/">Big Bear host turnover checklist</a>.</p>
<h2>How scheduling works</h2><ol class="steps" style="margin-top:10px"><li><b>Send the job</b>Photos plus your checkout and check-in window.</li><li><b>We fit the gap</b>Firm quote, then a slot inside your window.</li><li><b>Photo proof</b>Before-and-after photos when we lock up.</li></ol>
<p class="small muted">Sources: <a href="{SRC['city_vr'][1]}" rel="noopener">City of Big Bear Lake vacation rental program</a> · <a href="{SRC['county_str'][1]}" rel="noopener">San Bernardino County STR program</a>. Rules change — check the current versions.</p>
</div>{contact_box()}</div></section>
{faq_html(VRT_FAQ)}
<section><div class="wrap"><h2>Related</h2>{svc_cards([s for s in SERVICES if s[0] in ('/services/hot-tub-removal/', '/services/furniture-removal/', '/services/cabin-cleanouts/')])}</div></section>{cta_band('Your next turnover, handled')}'''
    emit(path, page(path, 'Vacation Rental Turnovers & Cabin Cleanouts in Big Bear | Airbnb & VRBO',
        'Bulky-item and junk removal, cabin cleanouts and weed clearing for Big Bear Airbnb and VRBO hosts, scheduled between guest stays. Free on-site quotes.',
        body, [business_ld(), service_ld('Vacation rental cleanouts', 'Bulky-item and junk removal for short-term rental hosts, scheduled between guest stays.', path), faq_ld(VRT_FAQ, path), crumbs_ld(crumbs)]), '0.8')
WEED_FAQ = [
 ('When does Big Bear Fire send weed abatement letters?', 'Big Bear Fire mails weed abatement letters to property owners each year (the 2026 letter has been mailed). The letter is your warning: a separate notice of violation is not guaranteed before a citation.'),
 ('How much clearance does Big Bear Fire require?', 'Its defensible space checklist applies from 0 to 100 feet from all structures, or to your property line: pine needles and litter removed within 5 feet, high energy release vegetation cleared within 15 feet, weeds and grasses cut below 4 inches, forest litter reduced to about 2 inches, and lower tree limbs pruned (6 feet for trees under 45 feet, 12–15 feet for taller trees, no more than 25% of tree height).'),
 ('Do you haul away the debris?', 'Yes. Clearing and haul-away happen on the same visit, so nothing is left piled on the property or at the curb.'),
 ('Do vacant lots need weed abatement?', 'Yes, unless the parcel is on Big Bear Fire\'s special land-locked parcel list. Vacant lots must meet the same Priority Defensible Space Requirements.'),
 ('I live in Fawnskin. Is it the same?', 'Fawnskin (92333) is handled by San Bernardino County Fire, not Big Bear Fire. The clearing work is similar, but inspections and notices come from the County.'),
 ('Can you do it while I\'m not in Big Bear?', 'Yes. Send us the letter and a few photos, approve the quote remotely, give us access, and we send before-and-after photos you can keep as a record.'),
 ('Do you remove trees?', 'We prune lower limbs and clear brush and small shrubs. Removing trees is a job for a tree service — and inside the City of Big Bear Lake, removing a tree 6 inches or more in diameter needs a city permit.'),
]
WEED_ROWS = [
 ('0–5 ft from structures', 'Remove pine needles, forest litter, dead vegetation and mulch', 'Hand-clear around foundations, decks and stairs'),
 ('0–15 ft from structures', 'Remove high energy release vegetation — also around hydrants, poles, fencing and propane tanks', 'Cut and remove brush and flammable shrubs'),
 ('Roofs, gutters, decks', 'Remove pine needles from roofing, gutters, under and on decks, stairs, landings and parking pads', 'Needle removal from gutters, decks and parking pads (roof work: ask us)'),
 ('Chimneys and roof lines', 'Prune branches within 10 ft of a chimney or stovepipe, or overhanging the roof within 10 ft', 'Pruning of reachable limbs'),
 ('Whole property — ground', 'Cut weeds and grasses below 4 in; reduce needles and litter to about 2 in; remove downed limbs and pine cone piles', 'Weed-whip, rake, thin and bag or load'),
 ('Whole property — shrubs', 'Prune the lower 25% of shrubs and remove dead wood; space high energy release shrubs apart', 'Shrub pruning and thinning'),
 ('Whole property — trees', 'Under 45 ft: prune lower limbs up to 6 ft. Over 45 ft: 12–15 ft. No more than 25% of tree height. Remove dead limbs.', 'Lower-limb pruning (no tree removal)'),
 ('Whole property — junk', 'Remove combustible hazards: tires, lumber, junk and trash', 'That\'s our day job — loaded and hauled'),
 ('Roads and driveways', 'Clear high energy release vegetation within 20 ft; keep 14 ft of vertical clearance over the driveway', 'Brush clearing and pruning along the drive'),
]
def weed():
    path = '/weed-abatement/'
    crumbs = [('Home', '/'), ('Services', '/services/'), ('Weed Clearing & Abatement', path)]
    rows = ''.join(f'<tr><td><b>{a}</b></td><td>{b}</td><td>{c}</td></tr>' for a, b, c in WEED_ROWS)
    body = page_hero(crumbs, 'Fire-safety clearing + haul-away in one visit', 'Weed Clearing &amp; Fire Abatement in Big Bear',
        'Got a weed abatement letter from Big Bear Fire? We clear weeds, pine needles, brush and low limbs to the fire department\'s defensible space checklist — and haul every bit away the same visit. Free on-site quotes.') + \
        photo_slot('real before/after photo of a cleared lot (no house numbers or faces)') + f'''
<section><div class="wrap two"><div class="prose">
<h2>What we clear</h2><ul>
<li><b>Weeds and dry grass</b> — cut below 4 inches across the property</li>
<li><b>Pine needles and forest litter</b> — cleared around the house and reduced to about 2 inches elsewhere</li>
<li><b>Gutters, decks, stairs and parking pads</b> — needles and debris removed</li>
<li><b>Brush and flammable shrubs</b> — removed near structures, propane tanks and fences</li>
<li><b>Low limbs and dead wood</b> — lower branches pruned to the required height</li>
<li><b>Downed limbs, pine cone piles and storm debris</b></li>
<li><b>Junk, lumber and old tires</b> — also on the fire department's list, and exactly what we haul</li>
<li><b>Vacant lots</b> — cleared and photographed for your records</li></ul>
<p>Everything we cut or rake leaves on our truck the same day. Piles left on the property don't make it compliant.</p>
<h2>Big Bear Fire's defensible space checklist</h2>
<p>These are the Priority Defensible Space requirements Big Bear Fire applies from 0 to 100 feet around every structure, or up to your property line:</p>
<div class="tscroll"><table><tr><th>Where</th><th>Requirement (summary)</th><th>What we do</th></tr>{rows}</table></div>
<p class="small muted">Summarized from <a href="https://www.bigbearfire.org/office-of-the-fire-marshal/defensible-space" rel="noopener">Big Bear Fire — Defensible Space</a> (checked September 2026). Always check the current checklist; Big Bear Fire (909) 866-7566.</p>
<h2>Got the letter? What happens next</h2>
<ol>
<li><b>The letter is your warning.</b> Big Bear Fire says a notice of violation isn't guaranteed before a citation, so treat the letter as your deadline.</li>
<li><b>Get it cleared and documented.</b> Before-and-after photos are your record.</li>
<li><b>Want a second opinion first?</b> Big Bear Fire offers paid pre-inspections, and separate defensible-space inspections for insurance.</li>
<li><b>Need help paying?</b> Big Bear Fire points owners to the Mountain Rim Fire Safe Council (firesafenow.org), which has had grant funding to help with abatement notices — approval isn't guaranteed.</li></ol>
<p>Full step-by-step guide: <a href="/guides/big-bear-fire-abatement-letter/">Got a Big Bear fire abatement letter? Here's exactly what to do</a>.</p>
<div class="note"><b>Fawnskin is different.</b> In Fawnskin (92333), weed abatement and defensible-space inspections are handled by San Bernardino County Fire, not Big Bear Fire. The clearing work is similar; the notices and inspections come from the County.</div>
<h2>Year-round, not just letter season</h2>
<ul><li><b>Spring:</b> snowmelt uncovers a winter of needles and downed limbs — the best time to get ahead of the letter.</li>
<li><b>Summer:</b> peak fire danger; keep cleared zones cleared and deal with regrowth.</li>
<li><b>Fall:</b> the last needle drop — clear gutters and decks before the first snow.</li>
<li><b>Winter:</b> storm debris and downed limbs when access is safe.</li></ul>
<h2>Off the mountain?</h2><p>Send us the letter and a few photos, approve the quote remotely, and give us gate or lot access. We send before-and-after photos when the work is done.</p>
<figure class="photo" style="margin-top:18px"><img loading="lazy" decoding="async" src="/images/opt/pine-cone-needles-800.webp" width="720" height="591" alt="Pine needles and pine cones"><figcaption>Stock photo. <!-- PHOTO-SLOT: replace with a real photo of a cleared Big Bear lot --></figcaption></figure>
<p class="small muted">{LICENSE_NOTE} We don't remove trees.</p>
</div>{contact_box()}</div></section>
{faq_html(WEED_FAQ, 'Weed clearing &amp; abatement FAQ')}
<section><div class="wrap"><h2>Related</h2>{svc_cards([x for x in SERVICES if x[0] in ('/services/junk-removal/', '/services/cabin-cleanouts/', '/vacation-rental-turnovers/')])}</div></section>
{cta_band("Don't wait for the inspection", 'Book a free on-site quote for clearing and haul-away — text or WhatsApp us a few photos of the lot.')}'''
    emit(path, page(path, 'Weed Clearing & Fire Abatement Big Bear | Pine Needles, Brush & Haul-Away',
        'Weed abatement letter from Big Bear Fire? We clear weeds, pine needles, brush and low limbs to the defensible space checklist and haul it away the same visit. Free on-site quotes.',
        body, [business_ld(), service_ld('Weed clearing and fire abatement', 'Weed, pine needle, brush and low-limb clearing to Big Bear Fire defensible space requirements, with same-visit haul-away.', path, stype='Weed abatement'), faq_ld(WEED_FAQ, path), crumbs_ld(crumbs)]), '0.9')
LOC_FAQ = [
 ('What areas do you serve?', 'The Big Bear Valley: Big Bear Lake (including Boulder Bay, Fox Farm and the Village), Big Bear City, Moonridge, Sugarloaf, Fawnskin, Erwin Lake and Baldwin Lake.'),
 ('Do you work outside the Big Bear Valley?', 'Sometimes, in nearby mountain communities, by arrangement. Message us with the location and job.'),
 ('Do you offer free on-site quotes everywhere in the valley?', 'Yes. Anywhere in the Big Bear Valley, free and with no obligation.'),
]
def location_hub():
    path = '/location/'
    crumbs = [('Home', '/'), ('Service Areas', path)]
    cards = '<div class="grid grid-3">' + ''.join(
        f'<a class="card" href="/location/{s}/"><div class="ico">{ICONS["pin"]}</div><h3>{AREAS_CONTENT[s]["name"]} <span class="small muted">{AREAS_CONTENT[s]["zip"]}</span></h3><p>{strip_tags(AREAS_CONTENT[s]["lead"])[:150].rsplit(" ",1)[0]}…</p><span class="more">Local guide →</span></a>' for s, _ in AREAS) + '</div>'
    rows = ''.join(f'<tr><td>{a}</td><td>{b}</td><td>{c}</td></tr>' for a, b, c in [
        ('Big Bear Lake (92315)', 'Big Bear Disposal — 1 free bulky pickup/yr', 'City vacation rental license'),
        ('Moonridge', 'Depends on city/county side', 'City license or County permit'),
        ('Big Bear City (92314)', 'Big Bear City CSD — bulky items per-item fee', 'County STR permit'),
        ('Sugarloaf (92386)', 'Big Bear City CSD', 'County STR permit'),
        ('Erwin Lake (92314)', 'Big Bear City CSD', 'County STR permit'),
        ('Baldwin Lake (92314)', 'No curbside service — self-haul to transfer station', 'County STR permit'),
        ('Fawnskin (92333)', 'Optional Big Bear Disposal service', 'County STR permit; County Fire for abatement')])
    body = page_hero(crumbs, 'The whole Big Bear Valley', 'Junk Removal Service Areas in the Big Bear Valley',
        'The whole Big Bear Valley plus nearby mountain communities. Pick your area for local trash rules, dump options and access tips.') + f'''
<section><div class="wrap">{cards}</div></section>
<section class="alt"><div class="wrap"><h2>Who handles what, by area</h2><p class="sec-intro">Trash service and rental rules change depending on whether you're inside the City of Big Bear Lake or in unincorporated San Bernardino County.</p>
<div class="tscroll"><table><tr><th>Area</th><th>Curbside trash / bulky items</th><th>Short-term rentals</th></tr>{rows}</table></div>
<p class="small muted">Everyone can self-haul to the Big Bear Transfer Station, 38550 Holcomb Valley Rd (Mon–Sat 8 AM–4:30 PM; call (909) 381-2404 to confirm). Details and sources are on each area page.</p></div></section>
<section><div class="wrap narrow"><h2>Nearby mountain communities</h2><p>We also take jobs in nearby mountain communities by arrangement — message us with the location and what needs to go.</p></div></section>
{faq_html(LOC_FAQ, 'Service area questions')}{cta_band()}'''
    emit(path, page(path, 'Service Areas | Junk Removal Across the Big Bear Valley',
        'Junk removal and weed clearing in Big Bear Lake, Big Bear City, Moonridge, Sugarloaf, Fawnskin, Erwin Lake & Baldwin Lake — with local trash and dump rules for each area.',
        body, [business_ld(), faq_ld(LOC_FAQ, path), crumbs_ld(crumbs)]), '0.8')
def area_pages():
    for slug, c in AREAS_CONTENT.items():
        path = f'/location/{slug}/'
        crumbs = [('Home', '/'), ('Service Areas', '/location/'), (c['name'], path)]
        secs = ''.join(f'<h2>{h}</h2>{b}' for h, b in c['sections'])
        src = ''.join(f'<li><a href="{SRC[k][1]}" rel="noopener">{SRC[k][0]}</a></li>' for k in c['sources'])
        flag = f'<!-- {c["flag"]} -->' if c.get('flag') else ''
        others = '<ul class="chips">' + ''.join(f'<li><a href="/location/{s}/">{n}</a></li>' for s, n in AREAS if s != slug) + '</ul>'
        body = flag + page_hero(crumbs, f'Service area · {c["zip"]}', f'Junk Removal in {c["name"]}', c['lead']) + f'''
<section><div class="wrap two"><div class="prose">{secs}
<h2>Services in {c["name"]}</h2>{svc_cards(SERVICES, 'grid grid-2')}
<h2>Sources and where to check</h2><p class="small muted">Local rules change. We checked these in September 2026 — confirm with the agency before you rely on them.</p><ul class="small">{src}</ul>
</div>{contact_box()}</div></section>
{faq_html(c['faqs'], f'{c["name"]} junk removal FAQ')}
<section><div class="wrap"><h2>Nearby areas we serve</h2>{others}</div></section>{cta_band(f'Junk removal in {c["name"]}')}'''
        names = ['Erwin Lake', 'Baldwin Lake'] if slug == 'erwin-lake-baldwin-lake' else [c['name']]
        emit(path, page(path, c['title'], c['desc'], body, [business_ld(), service_ld(f'Junk removal in {c["name"]}', strip_tags(c['lead']), path, names, 'Junk removal'), faq_ld(c['faqs'], path), crumbs_ld(crumbs)]), '0.7')
def contact():
    path = '/contact/'
    crumbs = [('Home', '/'), ('Contact', path)]
    body = page_hero(crumbs, 'Free on-site quotes · No obligation', 'Contact Junk Removal Big Bear', 'Text or WhatsApp us to book a free on-site quote — or send 2–3 photos for a quick answer.') + f'''
<section><div class="wrap"><div class="grid grid-2">
<div class="card"><div class="ico">{ICONS["msg"]}</div><h2 style="font-size:1.25rem">Text us</h2><p>Send photos of the items or the lot, your neighborhood and any access notes (stairs, steep driveway, gate code). <a href="{BIZ["sms"]}">Text {BIZ["phone"]} →</a></p><p class="small muted">Or text our second number: <a href="{BIZ["sms2"]}">{BIZ["phone2"]}</a></p></div>
<div class="card"><div class="ico">{ICONS["wa"]}</div><h2 style="font-size:1.25rem">WhatsApp</h2><p>Same as text — photos and a short note are perfect. <a href="{BIZ["wa"]}" rel="noopener">WhatsApp {BIZ["phone"]} →</a></p></div>
<div class="card"><div class="ico">{ICONS["home"]}</div><h2 style="font-size:1.25rem">Free on-site quote</h2><p>For weed clearing, big cleanouts, hot tubs and tear-outs, we come out, look at the job and give you a firm price — free, anywhere in the Big Bear Valley.</p></div>
<div class="card"><div class="ico">{ICONS["book"]}</div><h2 style="font-size:1.25rem">Email</h2><p><a href="mailto:{BIZ["email"]}">{BIZ["email"]}</a> — good for property managers and multi-property jobs.<!-- TODO(Nicholas): confirm email --></p></div>
</div></div></section>
<section class="alt"><div class="wrap narrow"><h2>Business details</h2><div class="tscroll"><table>
<tr><td><b>Business</b></td><td>{BIZ["name"]}</td></tr>
<tr><td><b>Text / WhatsApp</b></td><td><a href="{BIZ["sms"]}">{BIZ["phone"]}</a> (text) · <a href="{BIZ["wa"]}" rel="noopener">WhatsApp</a></td></tr>
<tr><td><b>Or text</b></td><td><a href="{BIZ["sms2"]}">{BIZ["phone2"]}</a></td></tr>
<tr><td><b>In business</b></td><td>Over 20 years</td></tr>
<tr><td><b>Email</b></td><td><a href="mailto:{BIZ["email"]}">{BIZ["email"]}</a></td></tr>
<tr><td><b>Hours</b></td><td>{BIZ["hours_text"]}</td></tr>
<tr><td><b>Service area</b></td><td>The Big Bear Valley — Big Bear Lake, Big Bear City, Moonridge, Sugarloaf, Fawnskin, Erwin Lake, Baldwin Lake — and nearby mountain communities by arrangement. We come to you.</td></tr>
<tr><td><b>Google</b></td><td><a href="{BIZ["gbp"]}" rel="noopener">Google Business Profile</a></td></tr>
</table></div></div></section>{cta_band()}'''
    emit(path, page(path, 'Contact Junk Removal Big Bear | Free On-Site Quotes by Text or WhatsApp',
        f'Text or WhatsApp photos for a free junk removal or weed clearing quote in Big Bear, or book a free on-site quote. Open {BIZ["hours_text"]}.', body, [business_ld(), crumbs_ld(crumbs)]), '0.8')
GUIDES = json.load(open(os.path.join(os.path.dirname(__file__), 'content', 'guides.json')))
GUIDE_TITLES = {f'/guides/{g["slug"]}/': strip_tags(g['h1']) for g in GUIDES}
def guides():
    crumbs = [('Home', '/'), ('Guides', '/guides/')]
    cards = '<div class="grid grid-2">' + ''.join(f'<a class="card" href="/guides/{g["slug"]}/"><div class="ico">{ICONS["book"]}</div><h3>{g["h1"]}</h3><p>{esc(g["desc"])}</p><span class="more">Read the guide →</span></a>' for g in GUIDES) + '</div>'
    body = page_hero(crumbs, 'Local knowledge', 'Big Bear Junk Removal &amp; Property Guides', 'Practical, local answers: fire abatement letters, the transfer station, hot tub removal, rental turnovers and estate cleanouts.') + f'<section><div class="wrap">{cards}</div></section>{cta_band()}'
    emit('/guides/', page('/guides/', 'Big Bear Junk Removal & Property Guides | Local How-To Articles',
        f'Local guides for Big Bear owners: fire abatement letters, the transfer station, hot tub removal, Airbnb turnovers & estate cleanouts.', body,
        [business_ld(), crumbs_ld(crumbs), {'@context': 'https://schema.org', '@type': 'CollectionPage', 'name': 'Big Bear junk removal & property guides', 'url': SITE + '/guides/',
          'hasPart': [{'@type': 'Article', 'headline': strip_tags(g['h1']), 'url': f'{SITE}/guides/{g["slug"]}/'} for g in GUIDES]}]), '0.6')
    for g in GUIDES:
        path = f'/guides/{g["slug"]}/'
        crumbs = [('Home', '/'), ('Guides', '/guides/'), (strip_tags(g['h1'])[:60], path)]
        others = ''.join(f'<li><a href="/guides/{o["slug"]}/">{o["h1"]}</a></li>' for o in GUIDES if o is not g)
        body = page_hero(crumbs, g['eyebrow'], g['h1'], esc(g['desc'])) + f'''
<section><div class="wrap two"><article class="prose">
<div class="note"><h2 style="font-size:1.15rem;margin-top:0">{g["answer_q"]}</h2><p style="margin:0">{g["answer"]}</p></div>
{g["body"]}
<p class="small muted">Last reviewed: September 2026. Rules, hours and fees change — confirm with the agency before you go.</p>
<h2>More guides</h2><ul>{others}</ul>
<p>Related services: <a href="/services/">all services</a> · <a href="/location/">service areas</a>.</p>
</article>{contact_box()}</div></section>
{faq_html(g['faq'])}{cta_band('Want it handled instead?')}'''
        art = {'@context': 'https://schema.org', '@type': 'Article', 'headline': strip_tags(g['h1']), 'description': g['desc'], 'url': SITE + path,
               'mainEntityOfPage': SITE + path, 'datePublished': g['published'], 'dateModified': TODAY, 'image': SITE + '/images/opt/og-junk-removal-big-bear.jpg',
               'author': {'@type': 'Organization', 'name': BIZ['name'], 'url': SITE + '/'}, 'publisher': {'@id': SITE + '/#business'}}
        emit(path, page(path, g['title'], g['desc'], body, [business_ld(), art, faq_ld(g['faq'], path), crumbs_ld(crumbs)], og_type='article'), '0.6')
def notfound():
    body = page_hero([('Home', '/'), ('Page not found', '/404.html')], '404', 'That page got hauled away', 'The page you\'re looking for doesn\'t exist. Try one of these instead:') + \
        f'<section><div class="wrap">{svc_cards()}<p style="margin-top:16px"><a href="/">Home</a> · <a href="/location/">Service areas</a> · <a href="/guides/">Guides</a> · <a href="/contact/">Contact</a></p></div></section>'
    write('/404.html', page('/404.html', 'Page Not Found | Junk Removal Big Bear', 'Page not found — Junk Removal Big Bear, serving the Big Bear Valley.', body, [], robots='noindex, follow', canonical=False))
def extras():
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for p, pr in PAGES: sm.append(f'  <url><loc>{SITE}{p}</loc><lastmod>{TODAY}</lastmod><priority>{pr}</priority></url>')
    sm.append('</urlset>'); write('/sitemap.xml', '\n'.join(sm) + '\n')
    write('/robots.txt', f'User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n')
    svc = '\n'.join(f'- [{n}]({SITE}{p}): {d}' for p, n, d, _ in SERVICES)
    areas = '\n'.join(f'- [{AREAS_CONTENT[s]["name"]}]({SITE}/location/{s}/)' for s, _ in AREAS)
    gd = '\n'.join(f'- [{strip_tags(g["h1"])}]({SITE}/guides/{g["slug"]}/)' for g in GUIDES)
    write('/llms.txt', f'''# {BIZ["name"]}

> Junk removal and weed clearing company serving the Big Bear Valley in the San Bernardino Mountains, California: junk removal, weed clearing and fire abatement, cabin, garage, estate and vacation-rental cleanouts, appliance and e-waste removal, hot tub removal, light demolition and minor interior and exterior painting. No moving services. Free on-site quotes.

- Contact: text or WhatsApp {BIZ["phone"]} ({BIZ["tel"]}); also text {BIZ["phone2"]} — see {SITE}/contact/
- In business: over 20 years
- Email: {BIZ["email"]}
- Hours: {BIZ["hours_text"]}
- Service-area business (no storefront; we come to you)
- Service area: the Big Bear Valley (Big Bear Lake, Big Bear City, Moonridge, Sugarloaf, Fawnskin, Erwin Lake, Baldwin Lake) and nearby mountain communities by arrangement
- Pricing: no published prices; free on-site quotes; price confirmed before work starts.
- Not a licensed contractor: painting, light demolition and similar work limited to minor jobs under California's $1,000 minor-work limit.
- Not accepted: hazardous waste (paint, chemicals, oil, fuels, asbestos, propane tanks).
- Google Business Profile: {BIZ["gbp_cid"]}

## Services
{svc}
- [Furniture & mattress removal]({SITE}/services/furniture-removal/)

## Service areas
{areas}

## Guides
{gd}

## Contact
- [Contact and quotes]({SITE}/contact/)
''')
    write('/_config.yml', '# GitHub Pages (Jekyll) settings: keep build tooling and internal docs off the public site.\nexclude:\n  - _build\n  - README.md\n  - LAUNCH-GUIDE.md\n  - localize-images.sh\n')
if __name__ == '__main__':
    home(); services_hub(); service_pages(); vrt(); weed(); location_hub(); area_pages(); contact(); guides(); notfound(); extras()
    print(f'built {len(PAGES)} indexable pages + 404')
