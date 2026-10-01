# 🚀 Deployment Guide — junkremovalbigbear.com (GitHub Pages, domain registered at Wix)

Written for your exact setup: the old site was on Wix and **the domain is registered with Wix.com**. Good news — the domain stays right where it is; you'll just edit its DNS records inside Wix. Total hands-on time: ~25 minutes, then DNS wait (minutes to 48h).

**The one rule that prevents disasters:** keep your Wix **domain registration** subscription active forever (it's separate from the website Premium plan). Cancel only the *site* plan, and only after Part E.

---

## PART A — Put the site on GitHub (10 min)

**A1.** Go to **github.com** → **Sign up** (free) → verify your email.

**A2.** Click the **+** (top-right) → **New repository**.
- Repository name: `junkremovalbigbear`
- Visibility: **Public** ← required for free GitHub Pages
- Don't tick any checkboxes → **Create repository**

**A3.** Upload the files:
1. Unzip `junkremovalbigbear-site.zip` on your computer.
2. On the empty repo page, click the **"uploading an existing file"** link.
3. Open the unzipped folder, select **all the files and subfolders inside it** (Cmd+A / Ctrl+A) — not the folder itself — and drag them into the browser.
4. Confirm you can see `index.html` in the file list at the top level.
5. Click **Commit changes** and wait for the upload to finish.

**A4.** Turn on GitHub Pages:
1. Repo → **Settings** tab → **Pages** (left sidebar).
2. Source: **Deploy from a branch** → Branch: **main**, Folder: **/ (root)** → **Save**.
3. Wait 1–2 minutes, refresh. You'll see: *"Your site is live at https://YOUR-USERNAME.github.io/junkremovalbigbear/"*.

**A5.** ✅ Checkpoint: open that github.io link. All 5 pages, photos, and phone buttons should work. (Styling appears once the custom domain is set if anything looks off — don't worry yet.)

---

## PART B — Point the Wix domain at GitHub (10 min)

Your domain is registered with Wix, so DNS is edited in Wix. Nameservers **cannot** be changed on Wix-registered domains — that's fine, we only need record edits.

**B1.** Log in to Wix → click your avatar (top-right) → **Domains** (or manage.wix.com/account/domains).

**B2.** Next to `junkremovalbigbear.com`, click the **Domain Actions** icon (⋯) → **Manage DNS Records**.

**B3.** In the **A (Host)** section:
1. Delete the existing Wix A record(s) for the blank/@ host (they point to Wix's servers, e.g. 185.230.x.x).
2. Click **+ Add Record** four times and add these (Host Name blank or `@`):

| Host | Value |
|---|---|
| @ | `185.199.108.153` |
| @ | `185.199.109.153` |
| @ | `185.199.110.153` |
| @ | `185.199.111.153` |

3. **Save** each, and **Save Changes** in the pop-up.

**B4.** In the **CNAME (Aliases)** section:
1. Delete the existing `www` CNAME (it points to something like `cdn1.wixdns.net`).
2. **+ Add Record** → Host Name: `www` → Value: `YOUR-USERNAME.github.io` (your actual GitHub username, e.g. `nickychan.github.io`) → **Save**.

**B5.** Touch nothing else — leave MX and any other records alone (they handle email if you have it).

**B6.** Back in GitHub: **Settings → Pages → Custom domain** → enter `www.junkremovalbigbear.com` → **Save**. GitHub runs a DNS check — it may say "DNS check in progress" for a while.

**B7.** When the check passes (15 min–48 h; usually under an hour), tick **✅ Enforce HTTPS**. If the checkbox is greyed out, wait and refresh — it activates once GitHub issues the free SSL certificate.

**B8.** ✅ Checkpoint: **https://www.junkremovalbigbear.com** loads the new site with a padlock, and `junkremovalbigbear.com` (no www) redirects to it. 🎉 You're live.

*If the old Wix site still appears: your browser cached it — try a private/incognito window or your phone on cellular data. If it persists past 48h, one A or CNAME record wasn't replaced — recheck B3/B4.*

---

## PART C — Tell Google (10 min, same day)

**C1.** Go to **search.google.com/search-console** → **Add property** → choose **Domain** → `junkremovalbigbear.com`.

**C2.** Google shows a **TXT record** for verification. Add it in the same Wix panel: Manage DNS Records → **TXT (Text)** section → **+ Add Record** → paste the value → Save. Click **Verify** in Search Console (may need a few minutes).

**C3.** In Search Console: **Sitemaps** (left menu) → enter `sitemap.xml` → **Submit**.

**C4.** Claim your **Google Business Profile** at business.google.com: business name "Junk Removal Big Bear", category **Junk removal service**, phone **(425) 233-2945**, website `https://www.junkremovalbigbear.com`, service areas Big Bear Lake / Big Bear City / Moonridge / Sugarloaf / Fawnskin. This is the single biggest factor for appearing in Google Maps.

---

## PART D — What to do about your Wix subscriptions

Wix bills you for (up to) two separate things:

| Subscription | What it is | What to do |
|---|---|---|
| **Domain registration** (junkremovalbigbear.com, ~$15–25/yr) | Ownership of the domain name itself | **KEEP FOREVER.** Keep auto-renew ON. If this lapses, you lose the domain and the website goes down. |
| **Premium site plan** (the website builder plan) | The old Wix website | Cancel — but ONLY after Part E below. |

Optional, later: you can transfer the domain away from Wix to a cheaper registrar (Cloudflare, Namecheap) — but a domain can't transfer within 60 days of registration/renewal, and it's not required. Keeping it at Wix works fine indefinitely.

---

## PART E — Before cancelling the Wix Premium plan (one-time, 10 min)

The site's photos currently load from Wix's image servers, and the free localize script needs to run before those could ever disappear:

**E1.** On a Mac: open **Terminal**, `cd` into the unzipped site folder, run:
```bash
bash localize-images.sh
```
(Windows: install Git from git-scm.com and use **Git Bash**, or ask me for a Windows version.)

**E2.** The script downloads all 15 photos into an `images/` folder with SEO filenames and rewrites the site to use them.

**E3.** Upload the changes to GitHub: repo → **Add file → Upload files** → drag in the new `images/` folder AND all the changed `.html` files + `style.css` → **Commit changes**.

**E4.** Check the live site still shows every photo (incognito window).

**E5.** NOW it's safe to cancel the Wix **Premium site plan** (keep the domain subscription!). Wix → subscriptions → cancel the site plan only.

---

## ✅ Final verification checklist

- [ ] https://www.junkremovalbigbear.com loads with padlock (HTTPS)
- [ ] Bare `junkremovalbigbear.com` redirects to www
- [ ] All 5 pages + every photo load, on desktop AND your phone
- [ ] Call, text and WhatsApp buttons all go to **+1 (425) 233-2945**
- [ ] Bear logo shows in the browser tab (favicon)
- [ ] Search Console verified + sitemap submitted
- [ ] Google Business Profile claimed
- [ ] (Within ~1 week) Search Console shows pages "Indexed"
- [ ] Replace the 3 sample homepage testimonials with real reviews as they arrive

## Troubleshooting quick answers

- **"DNS check unsuccessful" in GitHub** → a record from B3/B4 is missing or an old Wix record is still there. Wix says changes can take up to 48h to propagate.
- **HTTPS checkbox greyed out** → normal; wait for the certificate (up to a day), refresh.
- **Site works at github.io but not the domain** → DNS still propagating, or CNAME value has a typo (must be `YOUR-USERNAME.github.io`, no `https://`, no trailing slash).
- **Email on the domain stopped** → an MX record was deleted in B5. Contact Wix support to restore it (Wix DNS keeps a history).
- **Want to edit the site later** → edit any `.html` file directly on github.com (pencil icon → Commit); it republishes in ~1 minute. Or just ask me.
