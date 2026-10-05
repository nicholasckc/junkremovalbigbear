"""One-off: pull the five existing guides from the main branch into _build/content/guides.json,
applying the factual/claim fixes agreed for the 2026 redesign. Re-running is safe (reads from main)."""
import re, json, subprocess, html
SLUGS=['big-bear-fire-abatement-letter','big-bear-dump-transfer-station-guide','hot-tub-removal-big-bear','airbnb-turnover-checklist-big-bear','estate-cleanout-guide-big-bear']
def show(p): return subprocess.run(['git','show','main:'+p],capture_output=True,text=True,check=True).stdout
out=[]
for slug in SLUGS:
    s=show(f'guides/{slug}/index.html')
    g={'slug':slug}
    g['title']=html.unescape(re.search(r'<title>(.*?)</title>',s).group(1))
    g['desc']=html.unescape(re.search(r'name="description" content="(.*?)"',s).group(1))
    g['h1']=re.search(r'<h1>(.*?)</h1>',s,re.S).group(1)
    g['eyebrow']=re.search(r'<span class="tag">(.*?)</span>',s).group(1).split('·')[0].strip()
    m=re.search(r'<div class="answer">\s*<h2>(.*?)</h2>\s*<p>(.*?)</p>',s,re.S); g['answer_q'],g['answer']=m.group(1),m.group(2)
    art=re.search(r'<div class="article">(.*?)</div></div>\s*</section>',s,re.S).group(1)
    art=re.sub(r'<div class="callout">🚙.*?</div>','',art,flags=re.S)
    g['body']=art.strip()
    g['faq']=[(q,a) for q,a in re.findall(r'<details[^>]*><summary>(.*?)</summary><p>(.*?)</p></details>',s)]
    mp=re.search(r'"datePublished":\s*"([^"]+)"',s); g['published']=mp.group(1) if mp else '2026-07-26'
    out.append(g)
def fix(g,old,new,field='body',count=1):
    if old not in g[field]: raise SystemExit(f'fix not found in {g["slug"]}/{field}: {old[:60]}')
    g[field]=g[field].replace(old,new,count)
G={g['slug']:g for g in out}
# --- factual + claim fixes ---
d=G['big-bear-dump-transfer-station-guide']
fix(d,'''<p>If you have residential service with Big Bear Disposal, you likely get <b>one free bulky-item pickup per year</b> (up to about 3 cubic yards or 4 large items) — schedule through Big Bear Disposal; extra pickups cost a fee. Two bear-country rules worth knowing: carts shouldn't sit at the curb more than about 12 hours, and bear-resistant carts are available for a one-time fee. Part-time residents and visitors can also use the Clean Bear drop-off program for bagged trash.</p>''',
'''<p>Curbside options depend on where the property is:</p>
<ul>
<li><b>City of Big Bear Lake (92315):</b> Big Bear Disposal gives each residence <b>one free curbside bulky-item pickup per year</b> (up to 3 cubic yards or 4 large items); extra pickups cost a fee. Schedule through <a href="https://bigbeardisposal.com/services/residential-services/" rel="noopener">Big Bear Disposal</a>. Bear-resistant carts are available for a one-time fee.</li>
<li><b>Big Bear City, Sugarloaf and Erwin Lake:</b> the Big Bear City Community Services District (CSD) collects standard household bulky items curbside for a per-item fee, rents dumpsters, and holds periodic free community clean-up days. Details: <a href="https://www.bbccsd.org/index.php/solid-waste/residential-collection" rel="noopener">Big Bear City CSD</a>.</li>
<li><b>Clean Bear drop-off sites</b> (41790 Garstin Dr and 39690 Big Bear Blvd) are only for residents and visitors staying in the City of Big Bear Lake, and only for bagged household trash and recycling — no bulky items, construction debris, or contractor loads.</li>
</ul>
<p>Cart timing rules differ too: the City of Big Bear Lake prohibits leaving cans at the curb more than 24 hours, and the CSD allows carts out no more than 12 hours before collection and requires them back within 24 hours after.</p>''')
fix(d,'sorted for donation and recycling first, and legally disposed of.','and taken to a facility that accepts it. <!-- TODO(Nicholas): confirm whether you want to mention donation/recycling at all (neutral wording only) -->')
fix(d,'''San Bernardino County runs household hazardous waste collection; ask when you call the county line, and we're glad to point you to the current option when we're on-site.''','''San Bernardino County Fire runs household hazardous waste (HHW) collection; the Big Bear location is at the City of Big Bear Lake Public Works Yard, 42040 Garstin Drive, normally on Saturdays. Hours and temporary closures change, so check with San Bernardino County Fire's HHW program before you go.''')
d['faq_fix']='In the City of Big Bear Lake, Big Bear Disposal gives each residence one free curbside bulky-item pickup per year (up to 3 cubic yards or 4 large items) — see Big Bear Disposal\'s website. In Big Bear City, Sugarloaf and Erwin Lake, the Big Bear City CSD picks up bulky items for a per-item fee — see the CSD\'s website.'
f=G['big-bear-fire-abatement-letter']
fix(f,'Each spring, Big Bear Fire Department mails','Each year, Big Bear Fire Department mails')
fix(f,'The full standards are on <a href="https://www.bigbearfire.org" target="_blank" rel="noopener">bigbearfire.org</a>, and the department offers pre-inspections for a small fee — see bigbearfire.org to confirm current requirements for your parcel.','The full standards are on <a href="https://www.bigbearfire.org" target="_blank" rel="noopener">bigbearfire.org</a>, and the department takes requests for defensible-space (AB 38) inspections — see bigbearfire.org to confirm current requirements for your parcel. <b>Fawnskin (92333) is different:</b> weed abatement and AB 38 inspections there are handled by San Bernardino County Fire, not Big Bear Fire. If cost is the obstacle, Big Bear Fire points owners to the Mountain Rim Fire Safe Council (firesafenow.org), which has had grant funding to help some owners with abatement notices — an application does not guarantee approval.')
fix(f,'(or hire a licensed abatement service)','(or hire help)','answer')
h=G['hot-tub-removal-big-bear']
fix(h,'hauled the same visit, with metals recycled','hauled the same visit')
a=G['airbnb-turnover-checklist-big-bear']
fix(a,'Old sofa out, new sofa placed, packaging hauled — one visit, zero days off-market, and usable pieces get donated rather than landfilled.','Old sofa out the day the new one arrives, packaging hauled — one visit, fewer days off-market.')
fix(a,'''Your cleaning crew handles linens and surfaces; this checklist covers everything bigger.''','''Your cleaning crew handles linens and surfaces; this checklist covers everything bigger. (Outside city limits — Big Bear City, Fawnskin, Sugarloaf — the County's short-term rental permit rules apply instead, including removing trash after each stay and using animal-proof containers.)''')
e=G['estate-cleanout-guide-big-bear']
fix(e,"We sort for donation as we load, and usable pieces go to donation partners rather than the landfill.","Tell us what's going to family, sale or donation and we'll keep it separate from the haul-away. <!-- TODO(Nicholas): confirm whether you drop off donations yourself -->")
fix(e,'For probate and fiduciary situations, we provide the documentation your attorney or executor needs.','For probate and fiduciary situations, ask for a written quote and before/after photos for the file. <!-- TODO(Nicholas): confirm what documentation you provide -->')
for g in out:
    for fld in ('body','answer','h1','desc'):
        g[fld]=g[fld].replace('+1 (425) 233-2945','(425) 233-2945')
    g['faq']=[(q,a.replace('+1 (425) 233-2945','(425) 233-2945')) for q,a in g['faq']]
# faq fixes
d['faq']=[(q,(d.pop('faq_fix') if q.startswith('Does Big Bear have free bulky') else a)) for q,a in d['faq']]
e['faq']=[(q,("Loads are sorted as they're packed: anything the family wants kept, sold or donated is set aside first, and the remainder is hauled away. <!-- TODO(Nicholas): confirm donation handling -->" if q.startswith('What happens to items') else a)) for q,a in e['faq']]
import re as _re
def nophone(t):
    t=t.replace(' at (425) 233-2945','').replace('Call (425) 233-2945 to schedule one.','Text or WhatsApp us to schedule one.').replace('Call (425) 233-2945.','Text or WhatsApp us for one.')
    t=t.replace('(425) 233-2945','us')
    return t
for g in out:
    for fld in ('body','answer','desc','h1','title'): g[fld]=nophone(g[fld])
    g['faq']=[(q,nophone(a)) for q,a in g['faq']]
fix(d,'a haul-away crew is usually cheaper than people expect once dump fees, truck time, and a lost weekend are counted.','a haul-away crew often makes more sense than people expect once dump fees, truck time, and a lost weekend are counted.')
d['faq']=[(('Should I do a dump run or hire junk removal?' if q.startswith('Is junk removal cheaper') else q),a) for q,a in d['faq']]
json.dump(out,open('_build/content/guides.json','w'),indent=1,ensure_ascii=False)
print('ok',[ (g['slug'],len(g['body']),len(g['faq'])) for g in out])
