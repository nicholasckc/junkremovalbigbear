#!/usr/bin/env python3
"""Idempotent: add the first-party click counter (and, if a token is given and the page has
no Cloudflare beacon yet, the manual Cloudflare Web Analytics beacon) to every HTML page,
and write the /go/<type>/ count pages.
Usage: python3 inject.py <site_root> [--token TOKEN] [--exclude dir1,dir2]"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from go import JS, write_go, beacon
def run(root, token="", exclude=(), types=None):
    ex = set(exclude) | {".git", "_build", "node_modules", "go", "raw", "drafts", "outreach", "print", "lodgify", "directions"}
    n = 0
    for dp, dns, fns in os.walk(root):
        rel = os.path.relpath(dp, root)
        if rel != "." and rel.split(os.sep)[0] in ex:
            dns[:] = []; continue
        for fn in fns:
            if not fn.endswith(".html"): continue
            p = os.path.join(dp, fn)
            t = open(p, encoding="utf-8").read()
            if "</body>" not in t: continue
            t = re.sub(r"<!--cwa-->.*?<!--/cwa-->", "", t, flags=re.S)
            blk = "<!--cwa-->"
            if token and "cloudflareinsights.com/beacon" not in t:
                blk += beacon(token)
            blk += "<script>" + JS.strip() + "</script><!--/cwa-->"
            i = t.rfind("</body>")
            t = t[:i] + blk + t[i:]
            open(p, "w", encoding="utf-8").write(t); n += 1
    write_go(root, token, *( [types] if types else [] ))
    return n
if __name__ == "__main__":
    a = sys.argv[1:]; root = a[0]; tok = ""; exc = ()
    if "--token" in a: tok = a[a.index("--token") + 1]
    if "--exclude" in a: exc = a[a.index("--exclude") + 1].split(",")
    ty = a[a.index("--types") + 1].split(",") if "--types" in a else None
    print("cwa: injected", run(root, tok, exc, ty), "pages in", root)
