#!/usr/bin/env python3
"""Add a language to the switcher on every page that has one.

Usage: python3 scripts/add-lang.py ja JA 日本語
       python3 scripts/add-lang.py es ES Español

Adds to every page under templates/ that has <nav class="lang-switch">:
  - <link rel="alternate" hreflang="<code>" href="../<code>/"> in <head>
  - a header link <a href="../<code>/" hreflang lang>SHORT</a>
  - a footer link in .foot-lang with the full name
Only pages whose template has a templates/<code>/<slug>/index.html get the link,
so a language that covers some templates (e.g. a Spanish test) links only those.
Safe to run twice: pages that already link ../<code>/ are skipped.
Pages for the language itself (folder templates/<code>/) get aria-current.
"""
import pathlib, re, sys

code, short, full = sys.argv[1:4]
root = pathlib.Path(__file__).resolve().parent.parent / "templates"
href = f'../{code}/'
LANGS = {"en", "zh-CN", "ja", "es", "ko", "pt-BR", "de", "fr"}
changed = 0
for p in sorted(root.rglob("index.html")):
    parts = p.relative_to(root).parts[:-1]
    if not parts or parts[0] == "_docs":
        continue
    slug = "/".join(parts[1:] if parts[0] in LANGS else parts)
    if not slug or not (root / code / slug / "index.html").exists():
        continue
    html = p.read_text(encoding="utf-8")
    if 'class="lang-switch"' not in html or f'href="{href}"' in html:
        continue
    own = parts[0] == code
    cur = ' aria-current="page"' if own else ''
    # head alternate: insert before x-default
    html = re.sub(r'(<link rel="alternate" hreflang="x-default")',
                  f'<link rel="alternate" hreflang="{code}" href="{href}">\n\\1', html, count=1)
    # header switcher: insert before closing </nav> of lang-switch
    html = re.sub(r'(<nav class="lang-switch"[^>]*>.*?)(\n\s*</nav>)',
                  lambda m: m.group(1) + f'\n      <a href="{href}" hreflang="{code}" lang="{code}"{cur}>{short}</a>' + m.group(2),
                  html, count=1, flags=re.S)
    # footer links
    html = re.sub(r'(<p class="foot-lang">.*?)(</p>)',
                  lambda m: m.group(1) + f'<a href="{href}" hreflang="{code}" lang="{code}"{cur}>{full}</a>' + m.group(2),
                  html, count=1, flags=re.S)
    p.write_text(html, encoding="utf-8")
    changed += 1
print(f"added {code} to {changed} pages")
