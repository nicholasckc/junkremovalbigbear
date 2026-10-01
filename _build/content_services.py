from tpl import BIZ, LICENSE_NOTE
P = BIZ['phone']
TRASH_RULES = '''<ul>
<li><b>City of Big Bear Lake (92315, incl. part of Moonridge):</b> Big Bear Disposal gives each residence one free curbside bulky-item pickup per year — up to 3 cubic yards or 4 large items. Extra pickups cost a fee. Details: <a href="https://bigbeardisposal.com/services/residential-services/" rel="noopener">Big Bear Disposal</a>.</li>
<li><b>Big Bear City, Sugarloaf, Erwin Lake:</b> the Big Bear City CSD picks up standard household bulky items curbside for a per-item fee and runs periodic free community clean-up days. Details: <a href="https://www.bbccsd.org/index.php/solid-waste/residential-collection" rel="noopener">Big Bear City CSD</a>.</li>
<li><b>Clean Bear drop-off sites</b> don't take bulky items, construction debris or contractor loads, and are only for residents and visitors staying in the City of Big Bear Lake.</li>
<li><b>Big Bear Transfer Station</b>, 38550 Holcomb Valley Rd, takes self-haul loads Monday–Saturday, 8 AM–4:30 PM (confirm hours and fees on the <a href="https://dpw.sbcounty.gov/disposal-sites/" rel="noopener">county disposal sites page</a>).</li>
</ul>'''
SERVICES_CONTENT = {
'furniture-removal': dict(
 name='Furniture & Mattress Removal', stype='Furniture removal',
 title='Furniture & Mattress Removal in Big Bear, CA | Sofas, Beds & Mattresses',
 desc=f'Furniture and mattress removal in Big Bear: sofas, beds, dressers and patio sets carried out and hauled away. Free quotes; text {BIZ["phone"]}.',
 h1='Furniture &amp; Mattress Removal in Big Bear',
 lead='Sofas, sectionals, recliners, beds, mattresses, dressers, dining sets, desks and patio furniture — carried out from inside, down the stairs and off the property.',
 sections=[
  ('What we take', '''<ul>
<li>Sofas, sectionals, sleeper sofas and recliners</li><li>Beds, bed frames, mattresses and box springs (any size)</li>
<li>Dressers, wardrobes, bookcases and entertainment centers</li><li>Dining tables and chairs, desks and office chairs</li>
<li>Patio and deck furniture, grills and outdoor sets</li><li>Exercise equipment — treadmills, ellipticals, home gyms</li></ul>
<p>Pieces are loaded from wherever they are: the loft, the basement, the garage or the back deck. If something has to be taken apart to get out, we take it apart.</p>'''),
  ('Your other options in Big Bear (and when we make sense)', TRASH_RULES + '''<p>A haul-away usually makes sense when there's more than the free pickup covers, when items are upstairs or inside, when you're not on the mountain to put things at the curb, or when a rental needs it gone before the next check-in.</p>'''),
  ('Replacing furniture in a vacation rental?', '''<p>We can take the old pieces away on the day the new ones are delivered, so the listing isn't missing a sofa for a week. See <a href="/vacation-rental-turnovers/">vacation rental cleanouts</a>.</p>'''),
 ],
 faqs=[
  ('Who removes furniture and mattresses in Big Bear?', 'Junk Removal Big Bear carries out and hauls away sofas, beds, mattresses, dressers and patio sets across the Big Bear Valley, including from lofts and decks. Single items are fine.'),
  ('Can you take a mattress by itself?', f'Yes. Single items are fine — text a photo or call for a quote.'),
  ('Do I need to move the furniture outside first?', 'No. We carry items out from inside the home, including lofts, basements and stairs.'),
  ('Can you take furniture if I am not in Big Bear?', 'Yes. Send photos, arrange access (lockbox, garage code or a neighbor), and we send before-and-after photos when the job is done.'),
  ('How is furniture removal priced?', 'By how much space the items take up in the truck. We give a free quote from photos or on-site, and confirm the price before we start.'),
 ],
 related=['/services/appliance-e-waste-removal/', '/services/cabin-cleanouts/', '/vacation-rental-turnovers/']),
'appliance-e-waste-removal': dict(
 name='Appliance & E-Waste Removal', stype='Appliance and electronic waste removal',
 title='Appliance Removal & E-Waste Pickup in Big Bear, CA | Fridges, Washers, TVs',
 desc=f'Appliance and e-waste removal in Big Bear: fridges, freezers, washers, dryers, stoves, TVs and computers hauled away. Free quotes; text {BIZ["phone"]}.',
 h1='Appliance Removal &amp; E-Waste Pickup in Big Bear',
 lead='Dead fridge in the garage? Old TV in the basement? We haul away appliances and electronics from homes, cabins and rentals across the Valley.',
 sections=[
  ('What we take', '''<ul>
<li>Refrigerators and freezers</li><li>Washers and dryers</li><li>Dishwashers, stoves, ranges and microwaves</li>
<li>TVs, monitors and computers</li><li>Printers, audio gear and other household electronics</li></ul>
<p class="note small">Please have gas, water and hard-wired electrical connections shut off and disconnected by a qualified person before pickup. <!-- TODO(Nicholas): confirm whether your crew disconnects anything (e.g. washer hoses) --></p>'''),
  ('Why electronics and appliances need special handling', '''<p>In California, TVs, monitors, computers and many other electronics are not allowed in household trash, and appliances that contain refrigerant (fridges, freezers, AC units) have to go to facilities set up to handle them. In the Big Bear Valley that means:</p>
<ul>
<li><b>Big Bear City CSD</b> does not accept TVs, computers or other electronics in curbside carts; it collects e-waste at periodic free community clean-up days at its Paradise Maintenance Yard. Dates are posted by the <a href="https://www.bbccsd.org/index.php/solid-waste/residential-collection" rel="noopener">CSD</a>.</li>
<li><b>City of Big Bear Lake</b> customers can ask <a href="https://bigbeardisposal.com/services/residential-services/" rel="noopener">Big Bear Disposal</a> about appliance and e-waste options; one free bulky-item pickup per year is included.</li>
<li><b>Big Bear Transfer Station</b> (38550 Holcomb Valley Rd) — see the <a href="https://dpw.sbcounty.gov/disposal-sites/" rel="noopener">county disposal sites page</a> for which appliances and electronics are accepted and at what fee.</li>
</ul>
<p>If you'd rather not load a fridge into a pickup truck yourself, text us a photo and we'll quote it.</p>'''),
 ],
 faqs=[
  ('Who picks up old appliances in Big Bear?', 'Junk Removal Big Bear removes refrigerators, freezers, washers, dryers, stoves, TVs and computers from homes and cabins across the Big Bear Valley. Text a photo to (425) 233-2945 for a quote.'),
  ('Can you take a refrigerator with food still in it?', 'Please empty it first — food waste attracts bears and can\'t go in the truck.'),
  ('Do you take TVs and computers?', 'Yes. TVs, monitors, computers, printers and other household electronics are all fine.'),
  ('Can you remove an appliance from a basement or upstairs?', 'Yes. We carry appliances out from wherever they are, including stairs.'),
  ('Do you take propane tanks or paint?', 'No. Hazardous materials such as propane tanks, paint, chemicals, oil and asbestos can\'t go in our truck. San Bernardino County Fire runs household hazardous waste collection in Big Bear.'),
 ],
 related=['/services/furniture-removal/', '/services/cabin-cleanouts/', '/guides/big-bear-dump-transfer-station-guide/']),
'cabin-cleanouts': dict(
 name='Cabin & Garage Cleanouts', stype='Cleanout service',
 title='Cabin Cleanouts in Big Bear, CA | Garage, Attic, Shed & Whole-Cabin Clear-Outs',
 desc=f'Cabin cleanouts in Big Bear: garages, attics, sheds, storage units and whole cabins cleared and hauled away, even while you\'re away. Free quotes.',
 h1='Cabin Cleanouts in Big Bear: Garages, Attics, Sheds &amp; Whole Cabins',
 lead='From one packed garage to a whole cabin full of decades of stuff — we load it, haul it and leave the space swept.',
 sections=[
  ('What we clear', '''<ul>
<li><b>Garages</b> — old furniture, broken tools, boxes, sleds, bikes, tires</li>
<li><b>Attics, lofts and crawl spaces</b></li>
<li><b>Under-deck storage and sheds</b></li>
<li><b>Storage units</b></li>
<li><b>Whole cabins</b> — before a sale, after a purchase, or when a rental is refreshed</li>
<li><b>Yard debris</b> — branches, brush and storm debris</li></ul>'''),
  ('Mountain cleanouts are different', '''<ul>
<li><b>Timing around snow.</b> Items left outside in the fall can end up buried until spring. The best time to clear decks, yards and sheds is before the first storm.</li>
<li><b>Access.</b> Steep driveways, loft ladders and narrow stairs are normal here. Tell us about access when you book so we bring the right crew.</li>
<li><b>Absentee owners.</b> Many cabins are second homes. We can quote from photos, work with a lockbox or garage code, and send before-and-after photos.</li>
<li><b>Trash rules.</b> In the City of Big Bear Lake, cans can't stay at the curb more than 24 hours; in CSD areas carts can go out no more than 12 hours before pickup. Big cleanouts rarely fit either system.</li></ul>'''),
  ('Doing some of it yourself?', '''<p>Residential property owners in unincorporated areas (92314, 92386, 92333) may be eligible for a San Bernardino County Disposal Use Permit for self-haul loads to the Big Bear Transfer Station — see the <a href="https://dpw.sbcounty.gov/solid-waste-management/disposal-use-permit/" rel="noopener">county Disposal Use Permit page</a>. For everything that doesn't fit in your truck, call us.</p>'''),
 ],
 faqs=[
  ('Who does cabin cleanouts in Big Bear?', 'Junk Removal Big Bear clears out cabins, garages, attics, crawl spaces and sheds across the Big Bear Valley and hauls everything away. Owners who live off the mountain can arrange it by text, with lockbox or gate access.'),
  ('How long does a garage cleanout take?', 'It depends on the size and access; we give you a time estimate with the quote. Send photos for the fastest answer.'),
  ('Do I need to sort things first?', 'It helps to set aside anything you want to keep. We take everything else, except hazardous materials.'),
  ('Can you do a cleanout while I am off the mountain?', 'Yes. Quotes from photos, access by lockbox or code, and before-and-after photos when we finish.'),
  ('Do you sweep up afterwards?', 'Yes. We leave the cleared space broom-clean.'),
 ],
 related=['/services/estate-cleanouts/', '/services/furniture-removal/', '/vacation-rental-turnovers/']),
'estate-cleanouts': dict(
 name='Estate Cleanouts', stype='Estate cleanout',
 title='Estate Cleanouts in Big Bear, CA | Inherited Cabin & Home Clear-Outs',
 desc=f'Estate cleanouts in Big Bear: respectful clear-outs of inherited cabins and homes, coordinated remotely for families off the mountain. Free quotes.',
 h1='Estate Cleanouts in Big Bear',
 lead='Clearing a parent\'s or grandparent\'s cabin is hard. We make the physical part simple, and we can coordinate it with you, your realtor or executor from off the mountain.',
 sections=[
  ('How an estate cleanout works', '''<ol>
<li><b>Walkthrough.</b> We look at the property with you, a relative, your realtor or via lockbox access, and give you a firm price before any work starts.</li>
<li><b>Keepsakes first.</b> The family takes photos, documents and personal items. Tell us what else is being kept, sold or donated, and we leave it separate.</li>
<li><b>Everything else.</b> We load the rest — furniture, garage and shed contents, the loft, the crawl space — and leave the home broom-clean.</li></ol>
<p>For a step-by-step approach, read our <a href="/guides/estate-cleanout-guide-big-bear/">guide to clearing an inherited cabin in Big Bear</a>.</p>'''),
  ('Working with families who live down the hill', '''<p>Most inherited cabins in the Valley belong to families who don't live here. We can schedule access through a realtor, lockbox or local contact, send photos of progress, and coordinate around escrow and listing deadlines. <!-- TODO(Nicholas): confirm what documentation you give executors (written quote, photos, receipts) --></p>'''),
  ('Before you start', '''<ul>
<li>Check pockets, books, drawers and freezers — cabins hide things.</li>
<li>If the property will be listed, ask your agent what should stay for photos.</li>
<li>Hazardous items (old paint, chemicals, propane tanks) need separate disposal through San Bernardino County Fire's household hazardous waste program.</li></ul>'''),
 ],
 faqs=[
  ('Who does estate cleanouts in Big Bear?', 'Junk Removal Big Bear handles estate and inherited-cabin cleanouts across the Big Bear Valley. The family marks what stays; we clear and haul the rest and can coordinate everything remotely.'),
  ('Can we arrange an estate cleanout without traveling to Big Bear?', 'Yes. The walkthrough, quote, approval and completion photos can be handled remotely, with access through your realtor, a lockbox or a local contact.'),
  ('How is an estate cleanout priced?', 'By volume. We give a firm price after a free walkthrough or from photos, before any work starts.'),
  ('Can you leave some furniture for staging?', 'Yes. Mark or list what stays and we work around it.'),
 ],
 related=['/services/cabin-cleanouts/', '/guides/estate-cleanout-guide-big-bear/', '/services/furniture-removal/']),
'hot-tub-removal': dict(
 name='Hot Tub & Spa Removal', stype='Hot tub removal',
 title='Hot Tub Removal in Big Bear, CA | Spa Removal & Disposal',
 desc=f'Hot tub removal in Big Bear: we drain, cut down and haul away dead spas from decks, patios and vacation rentals. Free on-site quotes; text {BIZ["phone"]}.',
 h1='Hot Tub &amp; Spa Removal in Big Bear',
 lead='Freeze damage, a failed heater or just time for a new one — we take old spas off decks and patios, including tight and tiered mountain decks.',
 sections=[
  ('How removal works', '''<ol>
<li><b>Disconnect (you arrange this).</b> A licensed electrician or spa technician shuts off power and caps the plumbing. This must happen before we can start.</li>
<li><b>Drain.</b> The tub should be drained ahead of time where possible.</li>
<li><b>Cut down and carry out.</b> Most mountain spas can't leave the way they came in, so the shell is cut into sections and carried out.</li>
<li><b>Haul away and sweep.</b> Shell, cabinet, cover and equipment go on the truck and the spot is swept clean.</li></ol>
<p>More detail in our guide: <a href="/guides/hot-tub-removal-big-bear/">what it takes to get a dead spa off a mountain deck</a>.</p>'''),
  ('What affects the price', '''<ul><li><b>Size</b> — a two-person tub versus a large family spa</li><li><b>Access</b> — a ground-level patio versus an upper deck above a slope</li><li><b>Construction</b> — cabinet type and how it was installed</li></ul>
<p>Because access varies so much between lots, we quote hot tubs on-site or from several photos showing the path from the tub to the street.</p>'''),
  ('For vacation-rental owners', '''<p>A broken hot tub hurts bookings. We can schedule removal between guest stays and coordinate access with your property manager. See <a href="/vacation-rental-turnovers/">vacation rental cleanouts</a>.</p>'''),
 ],
 faqs=[
  ('Who removes hot tubs in Big Bear?', 'Junk Removal Big Bear removes and hauls away hot tubs and spas across the Big Bear Valley, including from upper decks and vacation rentals. Call or text (425) 233-2945 for a free quote.'),
  ('Do I need to disconnect the hot tub before removal?', 'Yes. A licensed electrician or spa technician needs to disconnect power and cap the plumbing first. After that, we handle the cut-down, carry-out and haul-away.'),
  ('Can you remove a hot tub from an upper or tiered deck?', 'Usually, yes. The tub is cut into sections and carried down stairs and paths. We confirm when we see the access.'),
  ('Can you remove a hot tub in winter?', 'Often, as long as the path from the tub to the truck is clear enough to work safely. Tell us about snow and ice when you book.'),
  ('How much does hot tub removal cost?', 'It depends on size, access and construction, so we quote it for free on-site or from photos.'),
 ],
 related=['/services/light-demolition/', '/vacation-rental-turnovers/', '/guides/hot-tub-removal-big-bear/']),
'light-demolition': dict(
 name='Light Demolition', stype='Light demolition and debris removal',
 title='Light Demolition in Big Bear, CA | Shed, Deck & Fence Tear-Outs (Minor Jobs)',
 desc='Light demolition in Big Bear: minor, non-structural tear-outs of small sheds, deck boards, fencing, cabinets and carpet, debris hauled away. Free quotes.',
 h1='Light Demolition &amp; Minor Tear-Outs in Big Bear',
 lead='Minor tear-out jobs with the haul-away included: small sheds, deck boards, fencing, cabinets, carpet and hot tubs.',
 sections=[
  ('Typical jobs', '''<ul>
<li>Small sheds and playsets</li><li>Rotted deck boards and small deck sections</li><li>Short runs of wood fencing</li>
<li>Kitchen and bathroom cabinets, countertops</li><li>Carpet and pad</li><li><a href="/services/hot-tub-removal/">Hot tubs and spas</a></li></ul>
<p class="note small">''' + LICENSE_NOTE + ''' Bigger or structural demolition needs a licensed demolition contractor and, often, a permit.</p>'''),
  ('Before we tear anything down', '''<ul>
<li><b>Permits.</b> Some demolition needs a permit. Check with the City of Big Bear Lake Building &amp; Safety (inside city limits) or San Bernardino County Land Use Services (unincorporated areas like Big Bear City, Fawnskin and Sugarloaf).</li>
<li><b>Utilities.</b> Electrical, gas and water connections must be shut off and disconnected by a qualified person first.</li>
<li><b>Asbestos and lead.</b> Older structures can contain hazardous materials. We don't handle asbestos or other hazardous waste.</li>
<li><b>Snow and access.</b> Ground conditions matter for tear-downs. Spring through fall is the easiest season for most outdoor jobs.</li></ul>'''),
 ],
 faqs=[
  ('Do you haul away the debris?', 'Yes. Tear-down and haul-away are done together, so nothing is left piled on the property.'),
  ('Can you remove a shed with things still inside?', 'Yes. We can empty the shed and take down the structure on the same visit.'),
  ('Do you do full house or structural demolition?', 'No. We only do light, minor, non-structural tear-outs and the haul-away. Larger or structural demolition needs a licensed demolition contractor and permits.'),
 ],
 related=['/services/hot-tub-removal/', '/services/cabin-cleanouts/', '/weed-abatement/']),
}

SERVICES_CONTENT['junk-removal'] = dict(
 name='Junk Hauling', stype='Junk removal',
 title='Junk Hauling in Big Bear, CA | Single Items to Full Loads',
 desc='Junk hauling in Big Bear: one item or a full load of furniture, yard debris and garage junk, loaded from wherever it sits and hauled away. Free quotes.',
 h1='Junk Hauling in Big Bear: Single Items to Full Loads',
 lead='One old mattress or a truck-full of garage junk — we do the lifting, loading and hauling, and sweep up after. Free quotes on-site or from photos.',
 sections=[
  ('What we take', '''<ul>
<li><a href="/services/furniture-removal/">Furniture and mattresses</a></li><li><a href="/services/appliance-e-waste-removal/">Appliances and electronics</a></li>
<li>Garage, shed, attic and storage-unit contents</li><li>Exercise equipment, bikes, sleds and outdoor gear</li>
<li>Yard waste, branches, pine needles and storm debris</li><li>Light tear-out debris — lumber, drywall, fencing, carpet</li>
<li><a href="/services/hot-tub-removal/">Hot tubs and spas</a></li></ul>
<p><b>We can't take</b> hazardous materials: paint, chemicals, oil, fuels, asbestos or propane tanks.</p>'''),
  ('How it works', '''<ol><li><b>Send photos or book a free on-site quote.</b> Text or WhatsApp 2–3 photos and your neighborhood, or ask us to come and look.</li>
<li><b>Get a firm price before we start.</b> No obligation.</li>
<li><b>We load, haul and sweep.</b> From inside the cabin, the garage, the deck or the yard.</li></ol>''' ),
  ('When a haul-away beats doing it yourself', '''<p>Free curbside bulky pickups and the transfer station are great for a few items you can move yourself. A haul-away makes sense when:</p>
<ul><li>There's more than one bulky pickup covers, or it's heavy and upstairs</li><li>You're not on the mountain to meet a pickup window</li>
<li>A rental needs it gone before the next check-in</li><li>Snow is coming and you don't want it buried until spring</li></ul>
<p>Local options by area are in our <a href="/guides/big-bear-dump-transfer-station-guide/">Big Bear disposal guide</a>.</p>''' + TRASH_RULES),
 ],
 faqs=[
  ('Who hauls away junk in Big Bear?', 'Junk Removal Big Bear hauls away single items and full loads across the Big Bear Valley, 8 AM–10 PM, 7 days a week. Call or text (425) 233-2945, or text 2–3 photos for a quick quote.'),
  ('Do you take single items?', 'Yes. One sofa, one fridge or one mattress is fine.'),
  ('Do I need to be home?', 'No. Many owners give us lockbox or gate access and we send before-and-after photos.'),
  ('Do you offer same-day junk removal?', f'Sometimes, depending on the schedule. We work {BIZ["hours_text"]}; message early for the best chance.'),
  ('How is junk removal priced?', 'By the job, based on how much there is and how hard it is to reach. Every quote is free, and we confirm the price before we start.'),
 ],
 related=['/services/cabin-cleanouts/', '/services/appliance-e-waste-removal/', '/weed-abatement/'])
SERVICES_CONTENT['painting'] = dict(
 name='Painting (Minor Jobs)', stype='Painting',
 title='Minor Interior & Exterior Painting in Big Bear, CA | Small Jobs Only',
 desc='Small interior and exterior painting for Big Bear cabins and rentals: walls, trim, doors, siding touch-ups, decks and fences. Minor jobs only. Free quotes.',
 h1='Minor Interior &amp; Exterior Painting in Big Bear',
 lead='Inside or out — scuffed walls after a cleanout, a tired ceiling, weathered trim, a deck or a fence run. We take on small interior and exterior painting jobs.',
 sections=[
  ('Interior painting', '''<ul><li>Walls and ceilings — a single room, a hallway or a loft</li>
<li>Patch painting and touch-ups after furniture comes out or a guest season ends</li>
<li>Doors, trim, window casings and baseboards</li></ul>'''),
  ('Exterior painting', '''<ul><li>Siding touch-ups and small sections of siding</li>
<li>Exterior trim, fascia, doors and railings</li>
<li>Decks, porches and stairs</li>
<li>Fences, sheds and small outbuildings</li></ul>
<p class="note small">''' + LICENSE_NOTE + ''' Larger projects — whole-house repaints, anything needing a permit, or any job over $1,000 including materials — need a licensed painting contractor.</p>'''),
  ('Good to know before painting a mountain cabin', '''<ul>
<li><b>Season.</b> Exterior paint and deck coatings need dry weather and temperatures in the range the manufacturer specifies, so outdoor jobs are usually late spring to early fall at this elevation. Interior work can happen year-round.</li>
<li><b>Older cabins and lead paint.</b> Homes built before 1978 may have lead-based paint. Tell us the year the cabin was built. Sanding, scraping or cutting into lead paint is regulated by the EPA and must be done by a lead-safe certified firm, so for pre-1978 surfaces we'll tell you up front whether the job is one we can take. <!-- TODO(Nicholas): confirm whether you hold EPA RRP certification; if not, say you don't take jobs that disturb pre-1978 paint. --></li>
<li><b>Leftover paint.</b> Old paint cans are household hazardous waste — they can't go in the trash or in our truck. Use San Bernardino County Fire's household hazardous waste drop-off in Big Bear.</li>
<li><b>Rentals.</b> We can combine a small paint refresh with a cleanout so the property is ready for photos or the next guest.</li></ul>'''),
 ],
 faqs=[
  ('Do you do interior or exterior painting?', 'Both, as long as the job is minor: interior walls, ceilings, doors and trim, and exterior siding touch-ups, trim, decks and fences.'),
  ('Do you paint whole houses?', 'No. We only take on minor painting jobs under $1,000 including materials. Whole-house or permitted work needs a licensed painting contractor.'),
  ('Can you paint after a cleanout?', 'Yes — combining a cleanout with a small paint touch-up is a common request for listings and rentals.'),
  ('Do you take away old paint cans?', 'No. Paint is household hazardous waste. San Bernardino County Fire runs the household hazardous waste drop-off in Big Bear.'),
 ],
 related=['/services/cabin-cleanouts/', '/vacation-rental-turnovers/', '/services/light-demolition/'])

# Photos from the old site (all 12 restored per Nicholas, Sep 26 2026). (name, alt). 'hero' = page hero, 'img' = first content section.
ALT = {
    'junk-removal-crew-loading-truck': 'Worker carrying a wooden dresser to an open box truck, with boxes, tires and old appliances piled on the driveway',
    'junk-removal-crew-armchair-truck': 'Two workers in green T-shirts loading an armchair and household junk into a dump truck on a driveway lined with pines',
    'mattress-removal-crew': 'Two workers in green shirts carrying out a mattress and taking apart a metal bed frame in a bright bedroom',
    'hot-tub-removal-deck': 'Worker leaning over an old hot tub on a wooden deck, getting it ready to be removed',
    'junk-hauling-box-truck': 'White box truck parked on a residential street lined with pine trees',
    'cabinet-tear-out': 'Worker in a green shirt and cap taking out old wooden kitchen cabinets with a drill',
    'shrub-trimming-ladder-fuel': 'Worker in a hard hat and safety vest clearing around a tall juniper shrub in a yard',
    'weed-clearing-crew': 'Two workers raking and clearing dry weeds and grass on a lot in front of houses',
    'wildfire-dry-brush': 'Firefighter walking through dry brush under pine trees with smoke and small flames behind',
    'appliances-electronics-pile': 'Old appliances and electronics stacked against a block wall: a TV, mini fridges, microwaves, a small washer and a blue bin',
    'mountain-cabin-pines': 'Two-story wood cabin with lit windows among tall pines at dusk',
    'yard-junk-pile': 'Backyard junk pile: a green bin full of scrap wood and a broken chair frame, with old tires and bagged debris on the lawn by a white fence',
}
def P(n): return (n, ALT[n])
for _slug, _hero, _img in [
        ('junk-removal', 'junk-removal-crew-armchair-truck', 'yard-junk-pile'),
        ('furniture-removal', 'mattress-removal-crew', None),
        ('appliance-e-waste-removal', 'appliances-electronics-pile', None),
        ('cabin-cleanouts', 'mountain-cabin-pines', 'junk-removal-crew-armchair-truck'),
        ('estate-cleanouts', 'junk-removal-crew-loading-truck', None),
        ('hot-tub-removal', 'hot-tub-removal-deck', None),
        ('light-demolition', 'cabinet-tear-out', None),
        ('painting', 'mountain-cabin-pines', None)]:
    SERVICES_CONTENT[_slug]['hero'] = P(_hero)
    if _img: SERVICES_CONTENT[_slug]['img'] = P(_img)
