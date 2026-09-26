from tpl import BIZ, LICENSE_NOTE
P = BIZ['phone']
TRASH_RULES = '''<ul>
<li><b>City of Big Bear Lake (92315, incl. part of Moonridge):</b> Big Bear Disposal gives each residence one free curbside bulky-item pickup per year — up to 3 cubic yards or 4 large items. Extra pickups cost a fee. Call (909) 866-3942.</li>
<li><b>Big Bear City, Sugarloaf, Erwin Lake:</b> the Big Bear City CSD picks up standard household bulky items curbside for a per-item fee and runs periodic free community clean-up days. Call (909) 585-2565.</li>
<li><b>Clean Bear drop-off sites</b> don't take bulky items, construction debris or contractor loads, and are only for residents and visitors staying in the City of Big Bear Lake.</li>
<li><b>Big Bear Transfer Station</b>, 38550 Holcomb Valley Rd, takes self-haul loads Monday–Saturday, 8 AM–4:30 PM (call (909) 381-2404 to confirm hours and fees).</li>
</ul>'''
SERVICES_CONTENT = {
'furniture-removal': dict(
 name='Furniture & Mattress Removal', stype='Furniture removal',
 title='Furniture & Mattress Removal in Big Bear, CA | Junk Removal Big Bear',
 desc=f'Old sofa, bed, mattress or patio set? We carry it out of your Big Bear cabin — lofts, stairs and decks included — and haul it away. Free on-site quotes.',
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
  ('Can you take a mattress by itself?', f'Yes. Single items are fine — text or WhatsApp a photo for a quote.'),
  ('Do I need to move the furniture outside first?', 'No. We carry items out from inside the home, including lofts, basements and stairs.'),
  ('Can you take furniture if I am not in Big Bear?', 'Yes. Send photos, arrange access (lockbox, garage code or a neighbor), and we send before-and-after photos when the job is done.'),
  ('How is furniture removal priced?', 'By how much space the items take up in the truck. We give a free quote from photos or on-site, and confirm the price before we start.'),
 ],
 related=['/services/appliance-e-waste-removal/', '/services/cabin-cleanouts/', '/vacation-rental-turnovers/']),
'appliance-e-waste-removal': dict(
 name='Appliance & E-Waste Removal', stype='Appliance and electronic waste removal',
 title='Appliance & E-Waste Removal in Big Bear, CA | Junk Removal Big Bear',
 desc=f'Refrigerators, freezers, washers, dryers, stoves, TVs and computers removed from Big Bear homes and cabins. Free on-site quotes.',
 h1='Appliance &amp; E-Waste Removal in Big Bear',
 lead='Dead fridge in the garage? Old TV in the basement? We haul away appliances and electronics from homes, cabins and rentals across the Valley.',
 sections=[
  ('What we take', '''<ul>
<li>Refrigerators and freezers</li><li>Washers and dryers</li><li>Dishwashers, stoves, ranges and microwaves</li>
<li>TVs, monitors and computers</li><li>Printers, audio gear and other household electronics</li></ul>
<p class="note small">Please have gas, water and hard-wired electrical connections shut off and disconnected by a qualified person before pickup. <!-- TODO(Nicholas): confirm whether your crew disconnects anything (e.g. washer hoses) --></p>'''),
  ('Why electronics and appliances need special handling', '''<p>In California, TVs, monitors, computers and many other electronics are not allowed in household trash, and appliances that contain refrigerant (fridges, freezers, AC units) have to go to facilities set up to handle them. In the Big Bear Valley that means:</p>
<ul>
<li><b>Big Bear City CSD</b> does not accept TVs, computers or other electronics in curbside carts; it collects e-waste at periodic free community clean-up days at its Paradise Maintenance Yard. Call (909) 585-2565 for dates.</li>
<li><b>City of Big Bear Lake</b> customers can ask Big Bear Disposal (909) 866-3942 about appliance and e-waste options; one free bulky-item pickup per year is included.</li>
<li><b>Big Bear Transfer Station</b> (38550 Holcomb Valley Rd) — call the County at (909) 381-2404 about which appliances and electronics are accepted and at what fee.</li>
</ul>
<p>If you'd rather not load a fridge into a pickup truck yourself, text us a photo and we'll quote it.</p>'''),
 ],
 faqs=[
  ('Can you take a refrigerator with food still in it?', 'Please empty it first — food waste attracts bears and can\'t go in the truck.'),
  ('Do you take TVs and computers?', 'Yes. TVs, monitors, computers, printers and other household electronics are all fine.'),
  ('Can you remove an appliance from a basement or upstairs?', 'Yes. We carry appliances out from wherever they are, including stairs.'),
  ('Do you take propane tanks or paint?', 'No. Hazardous materials such as propane tanks, paint, chemicals, oil and asbestos can\'t go in our truck. San Bernardino County Fire runs household hazardous waste collection in Big Bear.'),
 ],
 related=['/services/furniture-removal/', '/services/cabin-cleanouts/', '/guides/big-bear-dump-transfer-station-guide/']),
'cabin-cleanouts': dict(
 name='Cabin & Garage Cleanouts', stype='Cleanout service',
 title='Cabin, Garage & Home Cleanouts in Big Bear, CA | Junk Removal Big Bear',
 desc=f'Garage, attic, crawl space, shed, storage unit and whole-cabin cleanouts across the Big Bear Valley. Free on-site quotes.',
 h1='Cabin &amp; Garage Cleanouts in Big Bear',
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
  ('Doing some of it yourself?', '''<p>Residential property owners in unincorporated areas (92314, 92386, 92333) may be eligible for a San Bernardino County Disposal Use Permit for self-haul loads to the Big Bear Transfer Station — call County Solid Waste at (909) 386-8701. For everything that doesn't fit in your truck, call us.</p>'''),
 ],
 faqs=[
  ('How long does a garage cleanout take?', 'It depends on the size and access; we give you a time estimate with the quote. Send photos for the fastest answer.'),
  ('Do I need to sort things first?', 'It helps to set aside anything you want to keep. We take everything else, except hazardous materials.'),
  ('Can you do a cleanout while I am off the mountain?', 'Yes. Quotes from photos, access by lockbox or code, and before-and-after photos when we finish.'),
  ('Do you sweep up afterwards?', 'Yes. We leave the cleared space broom-clean.'),
 ],
 related=['/services/estate-cleanouts/', '/services/furniture-removal/', '/vacation-rental-turnovers/']),
'estate-cleanouts': dict(
 name='Estate Cleanouts', stype='Estate cleanout',
 title='Estate Cleanouts in Big Bear, CA | Inherited Cabin Cleanouts',
 desc=f'Organized, respectful estate and inherited-cabin cleanouts in Big Bear — coordinated remotely for families off the mountain. Free on-site quotes.',
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
  ('Can we arrange an estate cleanout without traveling to Big Bear?', 'Yes. The walkthrough, quote, approval and completion photos can be handled remotely, with access through your realtor, a lockbox or a local contact.'),
  ('How is an estate cleanout priced?', 'By volume. We give a firm price after a free walkthrough or from photos, before any work starts.'),
  ('Can you leave some furniture for staging?', 'Yes. Mark or list what stays and we work around it.'),
 ],
 related=['/services/cabin-cleanouts/', '/guides/estate-cleanout-guide-big-bear/', '/services/furniture-removal/']),
'hot-tub-removal': dict(
 name='Hot Tub & Spa Removal', stype='Hot tub removal',
 title='Hot Tub & Spa Removal in Big Bear, CA | Junk Removal Big Bear',
 desc=f'Dead hot tub on the deck? We drain, cut down, carry out and haul away spas from Big Bear homes and vacation rentals. Free on-site quotes.',
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
  ('Do I need to disconnect the hot tub before removal?', 'Yes. A licensed electrician or spa technician needs to disconnect power and cap the plumbing first. After that, we handle the cut-down, carry-out and haul-away.'),
  ('Can you remove a hot tub from an upper or tiered deck?', 'Usually, yes. The tub is cut into sections and carried down stairs and paths. We confirm when we see the access.'),
  ('Can you remove a hot tub in winter?', 'Often, as long as the path from the tub to the truck is clear enough to work safely. Tell us about snow and ice when you book.'),
  ('How much does hot tub removal cost?', 'It depends on size, access and construction, so we quote it for free on-site or from photos.'),
 ],
 related=['/services/light-demolition/', '/vacation-rental-turnovers/', '/guides/hot-tub-removal-big-bear/']),
'light-demolition': dict(
 name='Light Demolition', stype='Light demolition and debris removal',
 title='Light Demolition & Tear-Outs in Big Bear, CA | Junk Removal Big Bear',
 desc='Small shed, rotted deck boards, old fence or dated cabinets? Minor tear-outs and debris haul-away across the Big Bear Valley. Free on-site quotes.',
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
 name='Junk Removal', stype='Junk removal',
 title='Junk Removal Service in Big Bear, CA | Single Items to Full Loads',
 desc='Junk removal in Big Bear: furniture, mattresses, yard debris, garage junk and more, loaded from wherever it sits. Free on-site quotes, 7 days a week.',
 h1='Junk Removal in Big Bear',
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
  ('Do you take single items?', 'Yes. One sofa, one fridge or one mattress is fine.'),
  ('Do I need to be home?', 'No. Many owners give us lockbox or gate access and we send before-and-after photos.'),
  ('Do you offer same-day junk removal?', f'Sometimes, depending on the schedule. We work {BIZ["hours_text"]}; message early for the best chance.'),
  ('How is junk removal priced?', 'By the job, based on how much there is and how hard it is to reach. Every quote is free, and we confirm the price before we start.'),
 ],
 related=['/services/cabin-cleanouts/', '/services/appliance-e-waste-removal/', '/weed-abatement/'])
SERVICES_CONTENT['painting'] = dict(
 name='Painting (Minor Jobs)', stype='Painting',
 title='Minor Interior & Exterior Painting in Big Bear, CA | Rooms, Trim, Decks & Fences',
 desc='Small interior and exterior painting jobs for Big Bear cabins and rentals: walls, ceilings, trim, doors, siding touch-ups, decks and fences — minor jobs only. Free on-site quotes.',
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
<li><b>Older cabins and lead paint.</b> Homes built before 1978 may have lead-based paint. Tell us the year the cabin was built; disturbing lead paint is regulated by the EPA and needs lead-safe certified handling. <!-- TODO(Nicholas): confirm whether you hold EPA RRP certification; if not, say you don't take jobs that disturb pre-1978 paint. --></li>
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

# Restored general-scene images (AI-generated, from the old site; no people, vehicles or equipment). (name, alt)
SERVICES_CONTENT['appliance-e-waste-removal']['img'] = ('appliances-electronics-pile', 'Old appliances and electronics stacked against a block wall: a mini fridge, microwaves, a small washer, a black mini fridge and a blue bin')
SERVICES_CONTENT['cabin-cleanouts']['img'] = ('mountain-cabin-pines', 'Two-story wood cabin with lit windows among tall pines, with a snow-patched forested hillside behind')
SERVICES_CONTENT['junk-removal']['img'] = ('yard-junk-pile', 'Backyard junk pile: a green bin full of scrap wood and a broken chair frame, with old tires and bagged debris on the lawn by a white fence')
