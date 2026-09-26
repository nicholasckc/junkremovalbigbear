from tpl import BIZ
P = BIZ['phone']
SRC = {
 'bbd': ('Big Bear Disposal — residential services', 'https://bigbeardisposal.com/services/residential-services/'),
 'city_trash': ('City of Big Bear Lake — solid waste & recycling', 'https://www.citybigbearlake.com/index.php/en/services-main/recycling-programs'),
 'city_vr': ('City of Big Bear Lake — vacation rental program', 'http://citybigbearlake.com/index.php/en/departments/city-manager/transient-private-home-rental-tphr-program'),
 'csd': ('Big Bear City CSD — residential collection', 'https://www.bbccsd.org/index.php/solid-waste/residential-collection'),
 'county_str': ('San Bernardino County — short-term rentals', 'https://str.sbcounty.gov/'),
 'county_dup': ('San Bernardino County — Disposal Use Permit', 'https://dpw.sbcounty.gov/solid-waste-management/disposal-use-permit/'),
 'bbfd': ('Big Bear Fire — weed abatement FAQs', 'https://www.bigbearfire.org/office-of-the-fire-marshal/weed-abatement-notice-faqs'),
 'bbfd_insp': ('Big Bear Fire — inspections (incl. Fawnskin note)', 'https://www.bigbearfire.org/programs-services/fire-risk-reduction/fire-inspections'),
 'caltrans': ('Caltrans QuickMap — chain controls & closures', 'https://quickmap.dot.ca.gov/'),
 'cabb': ('Community Association of Big Bear — area descriptions', 'https://www.cabigbear.com/area-descriptions'),
 'cabb_trash': ('Community Association of Big Bear — trash & utilities by area', 'https://www.cabigbear.com/trash-recycling-utilities'),
 'hhw': ('San Bernardino County Fire — household hazardous waste', 'https://sbcfire.org/hhw/'),
}
TS = '<b>Big Bear Transfer Station</b>, 38550 Holcomb Valley Rd (off Hwy 18, north of Baldwin Lake) — Monday–Saturday 8 AM–4:30 PM; call (909) 381-2404 to confirm hours, fees and accepted materials'
ROADS = 'Chain controls on Highways 18, 38 and 330 change through the winter — check Caltrans QuickMap or call 1-800-427-7623 before a storm-day appointment.'
AREAS_CONTENT = {
'big-bear-lake': dict(
 name='Big Bear Lake', zip='92315',
 title='Junk Removal in Big Bear Lake, CA 92315 | Junk Removal Big Bear',
 desc=f'Junk removal, cleanouts and hot tub removal in the City of Big Bear Lake — the Village, Boulder Bay, Fox Farm and lakefront homes. Free on-site quotes.',
 lead='The City of Big Bear Lake has its own trash contractor, drop-off rules and vacation rental program. Here\'s what that means for getting rid of junk — and where we can help.',
 sections=[
  ('Neighborhoods we cover', '<p>The Village, Boulder Bay, Fox Farm, the lakefront, the city side of Moonridge and everything in between inside the 92315 ZIP code.</p>'),
  ('Trash and bulky items in the city', f'''<ul>
<li><b>Curbside trash</b> is handled by Big Bear Disposal under contract with the city. The city prohibits leaving cans at the curb for more than 24 hours because of wildlife.</li>
<li><b>One free bulky-item pickup per year</b> per residence — up to 3 cubic yards or 4 large items. Extra pickups cost a fee. Call Big Bear Disposal at (909) 866-3942.</li>
<li><b>Clean Bear Sites</b> (41790 Garstin Dr and 39690 Big Bear Blvd) are for residents and visitors staying in the city — bagged household trash and recycling only. No bulky items, construction debris, commercial waste or contractors.</li>
<li><b>Hazardous waste</b>: the household hazardous waste drop-off is at the Public Works Yard, 42040 Garstin Dr, normally Saturdays — check San Bernardino County Fire for current hours and closures.</li>
<li>{TS}.</li></ul>
<p>When the job is bigger than one free pickup, involves carrying things out of the house, or you aren't here to meet a pickup window, that's where we come in.</p>'''),
  ('Vacation rentals in Big Bear Lake', '''<p>Short-term rentals inside the city need a City of Big Bear Lake vacation rental license. Operational violations — trash is a common one — are fined $500 for a first violation, $1,000 for a second and $1,500 for a third within 12 months. Overflowing bins, bulky items left by guests and broken furniture are exactly the kind of thing we clear between stays. More on <a href="/vacation-rental-turnovers/">vacation rental cleanouts</a>.</p>'''),
  ('Access, snow and parking', f'''<p>Steep driveways are common around Boulder Bay and the south-side neighborhoods, and storms usually hit the west end of the valley first. After snow, tell us whether the driveway is plowed and where a truck can stop. {ROADS}</p>'''),
 ],
 faqs=[
  ('Can I take my old couch to a Clean Bear Site?', 'No. Clean Bear Sites don\'t accept bulky household items. Use your annual Big Bear Disposal bulky pickup, the Big Bear Transfer Station, or a haul-away service.'),
  ('Do you work in Big Bear Lake on weekends?', f'Yes, we work 7 days a week ({BIZ["hours_text"]}), subject to availability.'),
  ('Can you clear a vacation rental between guests?', 'Yes. Send photos and your checkout and check-in times, and we schedule inside that window.'),
 ],
 sources=['city_trash', 'bbd', 'city_vr', 'hhw', 'cabb', 'caltrans']),
'big-bear-city': dict(
 name='Big Bear City', zip='92314',
 title='Junk Removal in Big Bear City, CA 92314 | Junk Removal Big Bear',
 desc=f'Junk removal, garage cleanouts, appliance and furniture removal in Big Bear City. Local rules, bulky pickup and dump options explained. Free on-site quotes.',
 lead='Big Bear City is unincorporated San Bernardino County, with trash service from the Big Bear City Community Services District (CSD) — different rules from the city of Big Bear Lake.',
 sections=[
  ('Trash and bulky items in Big Bear City', f'''<ul>
<li><b>Curbside trash and recycling</b> come from the Big Bear City CSD. Carts can go out no more than 12 hours before collection and must be brought in within 24 hours after.</li>
<li><b>Bulky items</b>: the CSD collects standard household bulky items curbside for a per-item fee, rents dumpsters, and holds periodic free community clean-up days (including e-waste) at its Paradise Maintenance Yard. Call (909) 585-2565.</li>
<li><b>Not accepted curbside</b>: construction debris, tires, paint, oil, TVs, computers and other electronics.</li>
<li><b>Dump card</b>: residential property owners may be eligible for a San Bernardino County Disposal Use Permit for self-haul loads — call County Solid Waste at (909) 386-8701.</li>
<li>{TS}. It's on the east side of town, so it's the closest disposal option for most Big Bear City homes.</li></ul>'''),
  ('What we usually haul here', '<p>Big Bear City has more full-time residents than the city side of the lake, so a lot of our work here is garage and shed cleanouts, old appliances, furniture and yard debris. See <a href="/services/cabin-cleanouts/">cabin &amp; garage cleanouts</a> and <a href="/services/appliance-e-waste-removal/">appliance removal</a>.</p>'),
  ('Rentals and fire rules', f'''<ul>
<li><b>Short-term rentals</b> here need a San Bernardino County STR permit (not a city license). County rules require trash removal after each stay and animal-proof containers in the mountain region.</li>
<li><b>Weed abatement</b> notices in Big Bear City come from Big Bear Fire. See our <a href="/guides/big-bear-fire-abatement-letter/">abatement letter guide</a>.</li></ul>
<p>{ROADS}</p>'''),
 ],
 faqs=[
  ('Does Big Bear City have free bulky item pickup?', 'The Big Bear City CSD collects bulky items curbside for a per-item fee and holds periodic free community clean-up days. Call the CSD at (909) 585-2565 for current details.'),
  ('Where is the dump near Big Bear City?', 'The Big Bear Transfer Station is at 38550 Holcomb Valley Road, off Highway 18. It is normally open Monday–Saturday, 8 AM–4:30 PM. Call (909) 381-2404 to confirm.'),
  ('Can you empty my garage in Big Bear City?', f'Yes. Text or WhatsApp photos for a quote, or book a free on-site quote.'),
 ],
 sources=['csd', 'county_dup', 'county_str', 'bbfd', 'caltrans']),
'moonridge': dict(
 name='Moonridge', zip='92315 / 92314',
 title='Junk Removal in Moonridge, Big Bear | Junk Removal Big Bear',
 desc=f'Junk removal, hot tub removal and cabin cleanouts in Moonridge near Bear Mountain — steep streets, ski cabins and vacation rentals. Free on-site quotes.',
 lead='Moonridge sits on the hills near Bear Mountain and the Big Bear Alpine Zoo. It is split between the City of Big Bear Lake and unincorporated county, so the rules depend on which side your property is on.',
 sections=[
  ('City side or county side?', '''<p>Part of Moonridge is inside the City of Big Bear Lake (92315) and part is unincorporated San Bernardino County (92314). That affects:</p>
<ul>
<li><b>Trash service</b>: Big Bear Disposal on the city side (one free bulky pickup a year, cans at the curb no more than 24 hours); the Big Bear City CSD on the county side (bulky items for a per-item fee).</li>
<li><b>Vacation rentals</b>: a City of Big Bear Lake vacation rental license on the city side; a San Bernardino County STR permit on the county side.</li>
<li><b>Clean Bear Sites</b>: only available if the property is in the city.</li></ul>
<p>If you're not sure which side you're on, the City of Big Bear Lake can confirm your address.</p>'''),
  ('Steep streets and snow', f'''<p>Moonridge is hilly, with winding streets and steep driveways, and upper Moonridge gets more snow and can stay icy after a storm. We plan for that: tell us whether the driveway is clear and where a truck can park, and send a photo of the route from the item to the street. {ROADS}</p>'''),
  ('Ski cabins and rentals', '<p>Many Moonridge homes are second homes and short-term rentals. Common jobs are hot tub removal, furniture swaps between guest stays, and clearing garages and decks before the season. See <a href="/services/hot-tub-removal/">hot tub removal</a> and <a href="/vacation-rental-turnovers/">vacation rental cleanouts</a>.</p>'),
 ],
 faqs=[
  ('Is Moonridge in the City of Big Bear Lake?', 'Partly. Moonridge is split between the City of Big Bear Lake and unincorporated San Bernardino County, which changes trash service and rental permit rules.'),
  ('Can you get a hot tub off a steep Moonridge lot?', 'Usually. Spas are cut into sections and carried out; we confirm the route when we quote.'),
  ('Do you work in Moonridge in winter?', 'Yes, when access is safe. Tell us about snow on the driveway when you book.'),
 ],
 sources=['city_trash', 'csd', 'city_vr', 'county_str', 'cabb', 'caltrans']),
'sugarloaf': dict(
 name='Sugarloaf', zip='92386',
 title='Junk Removal in Sugarloaf, CA 92386 | Junk Removal Big Bear',
 desc=f'Junk removal, garage and cabin cleanouts, appliance and furniture removal in Sugarloaf, Big Bear. Local trash and dump options explained. Free on-site quotes.',
 lead='Sugarloaf is an unincorporated neighborhood south of Big Bear City, between Moonridge and Erwin Lake — mostly full-time residents, older cabins and narrow, sometimes steep streets.',
 sections=[
  ('Trash and bulky items in Sugarloaf', f'''<ul>
<li><b>Trash service</b> is provided by the Big Bear City CSD: carts out no more than 12 hours before pickup and back in within 24 hours after.</li>
<li><b>Bulky items</b> are collected by the CSD for a per-item fee; the CSD also holds periodic free community clean-up days. Call (909) 585-2565.</li>
<li><b>Dump card</b>: owners in the 92386 ZIP code may be eligible for a San Bernardino County Disposal Use Permit for self-haul loads — call (909) 386-8701.</li>
<li>{TS}.</li></ul>'''),
  ('Getting a truck in', f'''<p>Some Sugarloaf streets are steep and stay icy after storms, and many lots are small with tight driveways. We hand-carry items to the truck when it can't get close. {ROADS}</p>'''),
  ('Common Sugarloaf jobs', '<p>Inherited cabins and long-stored contents, garage and shed cleanouts, old appliances and furniture. See <a href="/services/estate-cleanouts/">estate cleanouts</a> and <a href="/services/cabin-cleanouts/">cabin &amp; garage cleanouts</a>. Weed abatement notices in Sugarloaf come from Big Bear Fire.</p>'),
 ],
 faqs=[
  ('Who picks up trash in Sugarloaf?', 'The Big Bear City Community Services District (CSD). Call (909) 585-2565 about bulky items and clean-up days.'),
  ('Can you clear out an inherited Sugarloaf cabin?', 'Yes. We can do a walkthrough with you or your realtor, give a firm price, and send photos when it\'s done.'),
  ('Do you work in Sugarloaf in winter?', 'Yes, when the street and driveway are safe to reach. Tell us about snow and ice when you book.'),
 ],
 sources=['csd', 'county_dup', 'bbfd', 'cabb', 'cabb_trash', 'caltrans']),
'fawnskin': dict(
 name='Fawnskin', zip='92333',
 title='Junk Removal in Fawnskin, CA 92333 | Junk Removal Big Bear',
 desc=f'Junk removal, cabin cleanouts and hot tub removal in Fawnskin on Big Bear\'s North Shore. Local trash, fire and rental rules explained. Free on-site quotes.',
 lead='Fawnskin is the small unincorporated community on the North Shore of Big Bear Lake, along Highway 38. It has different fire, trash and rental rules from the rest of the valley.',
 sections=[
  ('Fawnskin is different', '''<ul>
<li><b>Fire and weed abatement</b>: in Fawnskin (92333), weed abatement and AB 38 defensible-space inspections are handled by San Bernardino County Fire, not Big Bear Fire.</li>
<li><b>Trash</b>: residential service in Fawnskin is optional through Big Bear Disposal. City of Big Bear Lake Clean Bear drop-off sites are <em>not</em> available to Fawnskin properties.</li>
<li><b>Rentals</b>: short-term rentals need a San Bernardino County STR permit — including trash removal after each stay and animal-proof containers.</li>
<li><b>Dump card</b>: property owners in 92333 may be eligible for a County Disposal Use Permit for self-haul loads to the Big Bear Transfer Station — call (909) 386-8701.</li></ul>'''),
  ('Hillside cabins', f'''<p>A lot of Fawnskin is built on hillsides, so stairs and steep driveways are normal. Send photos of the route from the item to the road with your quote request. {ROADS}</p>'''),
  ('What we haul in Fawnskin', '<p>Cabin cleanouts, furniture and appliances, hot tubs, deck and yard debris, and cleanouts for second-home owners who aren\'t on the mountain. See <a href="/services/cabin-cleanouts/">cabin cleanouts</a> and <a href="/services/hot-tub-removal/">hot tub removal</a>.</p>'),
 ],
 faqs=[
  ('Who does weed abatement inspections in Fawnskin?', 'San Bernardino County Fire handles weed abatement and AB 38 defensible-space inspections in Fawnskin, not Big Bear Fire.'),
  ('Can Fawnskin residents use the Clean Bear Sites?', 'No. Clean Bear Sites are only for residents and visitors staying in the City of Big Bear Lake. Fawnskin properties use curbside service or the Big Bear Transfer Station.'),
  ('Do you serve Fawnskin?', f'Yes. Text or WhatsApp photos, or book a free on-site quote.'),
 ],
 sources=['bbfd_insp', 'county_str', 'county_dup', 'cabb', 'cabb_trash', 'caltrans']),
'erwin-lake-baldwin-lake': dict(
 name='Erwin Lake & Baldwin Lake', zip='92314',
 title='Junk Removal in Erwin Lake & Baldwin Lake, Big Bear | Junk Removal Big Bear',
 desc=f'Junk removal and cleanouts in Erwin Lake and Baldwin Lake on the east end of the Big Bear Valley — dirt roads, larger lots, no curbside service in Baldwin Lake. Free on-site quotes.',
 lead='The east end of the valley is rural: dirt roads, larger lots and fewer services. Baldwin Lake has no curbside trash pickup at all, which makes getting rid of big items harder.',
 sections=[
  ('Trash out east', f'''<ul>
<li><b>Erwin Lake</b> is served by the Big Bear City CSD — bulky items for a per-item fee, periodic free clean-up days. Call (909) 585-2565.</li>
<li><b>Baldwin Lake</b> has no curbside trash or recycling service; residents take waste to the transfer station themselves.</li>
<li>{TS}. It's close to Baldwin Lake, which helps for self-haul.</li>
<li><b>Dump card</b>: residential property owners may be eligible for a San Bernardino County Disposal Use Permit — call (909) 386-8701.</li></ul>'''),
  ('Roads and access', f'''<p>Most residential roads in Erwin Lake and around Baldwin Lake are dirt, and many are privately plowed. Tell us about road and driveway conditions when you book, especially after rain or snow. The east end usually gets less snow than the west end, and Highway 18 toward Lucerne Valley is typically the easiest route in winter. {ROADS}</p>'''),
  ('Common jobs', '<p>Shed and yard cleanouts, old appliances and furniture, trailer and outbuilding contents, and light demolition. Wild burros and other wildlife knock over bins out here — bagged trash left outside rarely survives the night.</p>'),
 ],
 faqs=[
  ('Is there trash pickup in Baldwin Lake?', 'No. Baldwin Lake has no curbside trash or recycling service; waste goes to the Big Bear Transfer Station on Holcomb Valley Road.'),
  ('Can your truck get down dirt roads?', 'Usually. Tell us about road and driveway conditions so we can confirm. <!-- TODO(Nicholas): confirm vehicle capability claims (current site says high-clearance trucks) -->'),
 ],
 sources=['csd', 'county_dup', 'cabb', 'cabb_trash', 'caltrans']),
}
