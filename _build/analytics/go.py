"""Shared generator for /go/<type>/ click-count pages (noindex, no content)."""
import os
TYPES = ["whatsapp", "call", "text", "email", "book", "form"]
def beacon(token):
    if not token:
        return ""
    return ('<script defer src="https://static.cloudflareinsights.com/beacon.min.js" '
            "data-cf-beacon='{\"token\": \"%s\"}'></script>" % token)
def go_html(t, token=""):
    return ('<!doctype html><html lang="en"><head><meta charset="utf-8">'
            '<meta name="robots" content="noindex, nofollow">'
            f'<title>{t} click</title>{beacon(token)}</head><body></body></html>\n')
def write_go(root, token="", types=TYPES):
    for t in types:
        d = os.path.join(root, "go", t)
        os.makedirs(d, exist_ok=True)
        open(os.path.join(d, "index.html"), "w").write(go_html(t, token))
JS = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "cwa-track.min.js")).read()
