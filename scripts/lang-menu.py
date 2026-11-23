#!/usr/bin/env python3
"""Turn the header language links into a compact dropdown: "EN ▾" opens a list of all languages.

Why: with 4–5 languages the row of links no longer fits next to the logo and menu button.
A <details> dropdown works without JS, is keyboard accessible, and takes less room than 3 links.
The footer keeps the full list of language links.

Usage: python3 scripts/lang-menu.py [file ...]   (default: every template page)
Safe to run twice (pages that already have .lang-menu are skipped).
"""
import pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent / "templates"
SHORT = {"en": "EN", "zh-Hant": "繁", "zh-Hans": "简", "ja": "JA", "es": "ES"}
FULL = {"en": "English", "zh-Hant": "繁體中文", "zh-Hans": "简体中文", "ja": "日本語", "es": "Español"}

CSS = """
/* ==================== Language menu (header dropdown) ====================
   The header shows the current language; click it to choose another.
   Uses <details>, so it works with JS off. Colours come from the theme tokens. */
.lang-switch { position: relative; }
.lang-menu > summary { display: inline-flex; align-items: center; gap: .4rem; min-height: 36px; padding-inline: .55rem; border-radius: 10px; color: inherit; font-weight: 600; list-style: none; cursor: pointer; transition: background-color .2s; }
.lang-menu > summary::-webkit-details-marker { display: none; }
.lang-menu > summary::after { content: ""; width: .38em; height: .38em; border-right: 1.5px solid currentColor; border-bottom: 1.5px solid currentColor; transform: translateY(-2px) rotate(45deg); transition: transform .2s; }
.lang-menu[open] > summary::after { transform: translateY(1px) rotate(-135deg); }
.lang-menu > summary:hover { background: color-mix(in srgb, var(--brand) 10%, transparent); }
.lang-menu > summary:focus-visible { outline: 2px solid var(--brand); outline-offset: 1px; }
.lang-list { position: absolute; top: calc(100% + .4rem); inset-inline-end: 0; z-index: 80; display: grid; gap: .1rem; min-width: 9.5rem; padding: .35rem; background: var(--bg); color: var(--text); border: 1px solid var(--line); border-radius: 12px; box-shadow: 0 12px 32px color-mix(in srgb, var(--text) 16%, transparent); }
.lang-switch .lang-list a[hreflang][lang] { display: flex; align-items: center; justify-content: flex-start; min-height: 40px; padding: .5rem .75rem; color: var(--text); white-space: nowrap; }
@media (prefers-reduced-motion: reduce) { .lang-menu > summary::after { transition: none; } }
"""

JS = """<script>
/* Language menu: close when clicking outside it or pressing Escape */
document.addEventListener('click', function (e) {
  document.querySelectorAll('.lang-menu[open]').forEach(function (d) { if (!d.contains(e.target)) d.removeAttribute('open'); });
});
/* Open towards whichever side has room (e.g. when the switcher sits inside the mobile menu) */
document.querySelectorAll('.lang-menu').forEach(function (d) {
  d.addEventListener('toggle', function () {
    var list = d.querySelector('.lang-list');
    list.style.insetInlineStart = ''; list.style.insetInlineEnd = '';
    if (!d.open) return;
    var r = list.getBoundingClientRect();
    if (r.left < 8 || r.right > document.documentElement.clientWidth - 8) {
      var s = d.getBoundingClientRect();
      var roomRight = document.documentElement.clientWidth - s.left;
      if (roomRight >= r.width + 8) { list.style.insetInlineStart = '0'; list.style.insetInlineEnd = 'auto'; }
    }
  });
});
document.addEventListener('keydown', function (e) {
  if (e.key !== 'Escape') return;
  document.querySelectorAll('.lang-menu[open]').forEach(function (d) { d.removeAttribute('open'); d.querySelector('summary').focus(); });
});
</script>
"""


def convert(html):
    m = re.search(r'(<nav class="lang-switch"[^>]*>)(.*?)(\n(\s*)</nav>)', html, re.S)
    if not m or 'lang-menu' in m.group(2):
        return None
    indent = m.group(4)
    links = re.findall(r'<a [^>]*>[^<]*</a>', m.group(2))
    cur = None
    items = []
    for a in links:
        code = re.search(r'hreflang="([^"]+)"', a).group(1)
        if 'aria-current' in a:
            cur = code
        items.append(re.sub(r'>[^<]*</a>$', '>' + FULL.get(code, code) + '</a>', a))
    if cur is None:
        return None
    body = (f'\n{indent}  <details class="lang-menu">'
            f'\n{indent}    <summary lang="{cur}">{SHORT.get(cur, cur)}</summary>'
            f'\n{indent}    <div class="lang-list">'
            + ''.join(f'\n{indent}      {a}' for a in items)
            + f'\n{indent}    </div>'
            f'\n{indent}  </details>')
    html = html[:m.start(2)] + body + html[m.start(3):]
    html = html.replace('</style>', CSS + '</style>', 1)
    i = html.rfind('</body>')
    html = html[:i] + JS + html[i:]
    return html


files = [pathlib.Path(f) for f in sys.argv[1:]] or [
    p for p in sorted(ROOT.rglob('index.html')) if '_docs' not in p.parts]
n = 0
for p in files:
    html = p.read_text(encoding='utf-8')
    out = convert(html)
    if out:
        p.write_text(out, encoding='utf-8')
        n += 1
print(f'converted {n} pages')
