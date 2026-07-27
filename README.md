# Junk Removal Big Bear — Website

Static site for **junkremovalbigbear.com**, built for GitHub Pages. Five pages, SEO/GEO-optimized copy, JSON-LD structured data, sitemap, robots.txt — no build step, no frameworks.

## Deploy (one time, ~10 minutes)

**Photos work out of the box** — all images (including the logo and favicon) load directly from the current live site's CDN, so nothing is broken on first open or first deploy.

**1. Push to GitHub:**

```bash
git init
git add .
git commit -m "Launch new site"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/junkremovalbigbear.git
git push -u origin main
```

**2. Enable GitHub Pages:** repo → Settings → Pages → Source: "Deploy from a branch" → Branch: `main`, folder `/ (root)` → Save.

**3. Connect the domain.** The repo already contains a `CNAME` file for `www.junkremovalbigbear.com`. At your DNS provider (wherever the domain is registered):

| Type | Host | Value |
|---|---|---|
| CNAME | `www` | `YOUR-USERNAME.github.io` |
| A | `@` | `185.199.108.153` |
| A | `@` | `185.199.109.153` |
| A | `@` | `185.199.110.153` |
| A | `@` | `185.199.111.153` |

Then in repo Settings → Pages → Custom domain, enter `www.junkremovalbigbear.com` and check **Enforce HTTPS** (appears after DNS propagates, up to 24h).

> ⚠️ If the domain is currently connected to Wix, disconnect it there first (Wix → Settings → Domains).

**4. Before cancelling Wix — bring the images home.** The photos currently load from Wix's CDN and will vanish if the Wix account is deleted. Run this once from the repo root, then commit and push:

```bash
bash localize-images.sh
```

It downloads every image into `images/` with SEO-friendly filenames and rewrites all HTML/CSS references automatically. After that, the site is fully self-contained and Wix can be cancelled safely.

**5. Tell Google:** create a free [Google Search Console](https://search.google.com/search-console) property for the domain and submit `https://www.junkremovalbigbear.com/sitemap.xml`. This site has no `noindex` problem — unlike the old Wix site, it's indexable from day one.

## Structure

```
index.html                        Homepage
weed-abatement/index.html         Weed abatement & fire safety
vacation-rental-turnovers/index.html  Airbnb/STR turnovers
location/index.html               Service areas
contact/index.html                Contact
404.html                          Not-found page
style.css                         All styling (one file)
localize-images.sh                Run before cancelling Wix (see step 4)
sitemap.xml · robots.txt · CNAME
```

## Editing

Everything is plain HTML — edit text directly in the page files. Each page's `<head>` contains its SEO title, meta description, canonical URL, and JSON-LD structured data (LocalBusiness on every page; FAQPage on the homepage and weed-abatement page). If you change an FAQ answer on the page, change it in the matching JSON-LD block too, so the visible text and structured data stay in sync.

## Post-launch checklist (highest-impact first)

1. **Claim a Google Business Profile** ("Junk removal service") — the #1 local ranking factor; a website alone can't win the Maps 3-pack.
2. Verify structured data with the [Rich Results Test](https://search.google.com/test/rich-results).
3. Add real customer reviews (Google/Yelp), then add `aggregateRating` to the LocalBusiness schema.
4. **Replace the placeholder testimonials** on the homepage ("What Big Bear Neighbors Say" section) with real customer reviews, quoted with permission — they're realistic samples, not real quotes.
5. Consider a local 909 forwarding number — the 425 area code reads as out-of-town to locals.
6. Before next abatement season (spring): add a blog post targeting "what to do when you get a Big Bear Fire abatement letter."
