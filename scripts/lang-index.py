#!/usr/bin/env python3
"""Write a template's language entry page, listing only the languages it ships with.
Usage: python3 scripts/lang-index.py <template folder containing en/, zh-TW/, ...>"""
import pathlib, sys
d = pathlib.Path(sys.argv[1])
src = pathlib.Path(__file__).resolve().parent.parent / "templates/_docs/lang-index.html"
html = src.read_text(encoding="utf-8")
EXTRA = [("ja", "日本語"), ("es", "Español")]
links = "".join(f'  <a href="{c}/" hreflang="{c}" lang="{c}">{n}</a>\n' for c, n in EXTRA if (d / c / "index.html").exists())
alts = "".join(f'<link rel="alternate" hreflang="{c}" href="{c}/">\n' for c, n in EXTRA if (d / c / "index.html").exists())
html = html.replace("  <!-- extra languages -->\n", links)
html = html.replace('<link rel="alternate" hreflang="x-default"', alts + '<link rel="alternate" hreflang="x-default"', 1)
(d / "index.html").write_text(html, encoding="utf-8")
