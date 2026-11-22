#!/usr/bin/env python3
"""Polyglot Pages outreach: build a free trilingual preview site for one lead.

Usage:
  python3 scripts/demo/make-demo.py <lead_id> [--csv sales/outreach/leads.csv] [--notes-zh "中文一句"]
  python3 scripts/demo/make-demo.py --all-new [--csv ...]

Reads the lead row, picks the base page by category (scripts/demo/base/<slug>/), fills in the
business details and writes demos/<shop-slug>/{index.html, en/, zh-TW/, zh-CN/}.
Then sets the lead's demo_url to demos/<shop-slug>/ and status to demo in the CSV.

Never fetches anything from the network and never uses the business's photos:
all images are the template's own CSS illustrations.
Needs: pip install opencc-python-reimplemented
"""
import argparse, csv, datetime, html, json, pathlib, re, subprocess, sys, urllib.parse

ROOT = pathlib.Path(__file__).resolve().parents[2]
BASE = ROOT / 'scripts/demo/base'
DEMOS = ROOT / 'demos'
CONTACT = 'polyglotpages.studio@gmail.com'
LANGS = ('en', 'zh-TW', 'zh-CN')

try:
    import opencc
    TW2SP = opencc.OpenCC('tw2sp')   # same converter the base zh-CN pages were made with
    S2T = opencc.OpenCC('s2t')       # shop names typed in simplified, shown on the traditional page
    T2S = opencc.OpenCC('t2s')       # shop names on the simplified page (character-level only)
except ImportError:
    sys.exit('需要 OpenCC：pip install opencc-python-reimplemented')

# ---------------------------------------------------------------- category -> base page
CATEGORY = {
    'restaurant': ('restaurant', None), 'restaurants': ('restaurant', None), 'food': ('restaurant', None),
    'dental': ('clinic', 'dental'), 'dentist': ('clinic', 'dental'), 'clinic': ('clinic', 'dental'),
    'tcm': ('clinic', 'tcm'), 'acupuncture': ('clinic', 'tcm'), 'chinese medicine': ('clinic', 'tcm'),
    'tutoring': ('education', None), 'education': ('education', None), 'school': ('education', None),
    'salon': ('beauty', None), 'hair': ('beauty', None), 'hair salon': ('beauty', None), 'beauty': ('beauty', None),
}
KIND = {  # for JSON-LD description when the lead has no notes
    ('restaurant', None): ('Chinese restaurant', '中餐館'),
    ('clinic', 'dental'): ('Dental office', '牙醫診所'),
    ('clinic', 'tcm'): ('Acupuncture and Chinese medicine clinic', '中醫針灸診所'),
    ('education', None): ('Tutoring and learning center', '補習班'),
    ('beauty', None): ('Hair salon', '美髮店'),
}
CLOSED_WORD = {'clinic': '休診'}
SCROLL_PAD = {'restaurant': '72px', 'clinic': '80px', 'education': '80px', 'beauty': '5rem'}
EXTRA_CSS = {  # per-template fixes for the banner offset
    'beauty': """.sec-head .demo-note { margin-inline: auto; }
@media (max-width: 760px) {
  .js .menu { padding-top: calc(5.5rem + var(--demo-h)); }
  .js .site-header.scrolled .menu { padding-top: 5.5rem; }
}
""",
}

# ---------------------------------------------------------------- places
TZ = {**{s: 'America/New_York' for s in 'NY NJ CT MA PA MD VA DC GA FL NC SC OH MI RI NH VT ME DE WV IN KY'.split()},
      **{s: 'America/Chicago' for s in 'TX IL MN WI MO IA LA AL MS AR OK KS NE TN ND SD'.split()},
      **{s: 'America/Denver' for s in 'CO UT NM MT WY ID'.split()},
      'AZ': 'America/Phoenix', 'HI': 'Pacific/Honolulu', 'AK': 'America/Anchorage'}
CITY_ZH = {
    'flushing': '法拉盛', 'new york': '紐約', 'brooklyn': '布魯克林', 'queens': '皇后區', 'manhattan': '曼哈頓', 'elmhurst': '艾姆赫斯特',
    'los angeles': '洛杉磯', 'san gabriel': '聖蓋博', 'arcadia': '阿凱迪亞', 'alhambra': '阿罕布拉', 'monterey park': '蒙特利公園市',
    'rosemead': '柔斯密', 'temple city': '天普市', 'el monte': '艾爾蒙地', 'rowland heights': '羅蘭崗', 'diamond bar': '鑽石吧',
    'walnut': '核桃市', 'hacienda heights': '哈仙達崗', 'pasadena': '帕薩迪納', 'irvine': '爾灣', 'torrance': '托倫斯',
    'san marino': '聖瑪利諾', 'west covina': '西科維納', 'chino hills': '奇諾岡',
    'san francisco': '舊金山', 'oakland': '奧克蘭', 'san jose': '聖荷西', 'cupertino': '庫比蒂諾', 'fremont': '佛利蒙',
    'milpitas': '苗必達', 'sunnyvale': '桑尼維爾', 'santa clara': '聖塔克拉拉', 'mountain view': '山景城', 'palo alto': '帕羅奧圖',
    'daly city': '戴利城', 'san mateo': '聖馬刁', 'millbrae': '密爾布瑞', 'dublin': '都柏林', 'pleasanton': '普萊森頓',
    'seattle': '西雅圖', 'bellevue': '貝爾維尤', 'redmond': '雷德蒙德', 'houston': '休士頓', 'sugar land': '糖城', 'katy': '凱蒂',
    'boston': '波士頓', 'chicago': '芝加哥', 'philadelphia': '費城',
}
DAYS_EN = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
DAYS_EN3 = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
DAYS_ZH = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日']
DAYS_ZH2 = ['週一', '週二', '週三', '週四', '週五', '週六', '週日']
SCHEMA_DAYS = DAYS_EN
CJK = re.compile(r'[㐀-鿿豈-﫿]')


# ---------------------------------------------------------------- parsing helpers
def split_name(raw):
    """'Golden Dumpling House / 金餃子館' -> ('Golden Dumpling House', '金餃子館')"""
    raw = ' '.join(raw.split())
    parts = [p.strip() for p in re.split(r'\s*[/／|｜]\s*', raw) if p.strip()]
    en = next((p for p in parts if not CJK.search(p)), '')
    zh = next((p for p in parts if CJK.search(p)), '')
    return (en or zh or raw), zh


def split_notes(raw):
    raw = ' '.join((raw or '').split())
    parts = [p.strip() for p in re.split(r'\s+/\s+|\s*／\s*', raw) if p.strip()]
    en = ' '.join(p for p in parts if not CJK.search(p))
    zh = ''.join(p for p in parts if CJK.search(p))
    return tidy(en), zh


def tidy(s):
    s = re.sub(r'\s*[—–]\s*', ', ', s.strip())   # Hallmark: no dashes in sentences
    s = s.replace(' · ', ', ')
    if s and s[-1] not in '.!?':
        s += '.'
    return s[:1].upper() + s[1:]


def parse_address(addr, city):
    addr = ' '.join(addr.split())
    m = re.match(r'^(?P<street>.+?),\s*(?P<city>[^,]+?),\s*(?P<state>[A-Z]{2})\.?\s+(?P<zip>\d{5}(?:-\d{4})?)(?:,\s*(?:USA|US|United States))?$', addr)
    if m:
        return m['street'], m['city'], m['state'], m['zip']
    m = re.search(r',\s*([A-Z]{2})\b', addr)
    return addr, city, (m.group(1) if m else ''), ''


def format_phone(raw):
    d = re.sub(r'\D', '', raw or '')
    if len(d) == 11 and d[0] == '1':
        d = d[1:]
    if len(d) == 10:
        return f'({d[:3]}) {d[3:6]}-{d[6:]}', f'+1{d}'
    return raw.strip(), ('+' + d if d else '')


def safe_maps_url(url, address):
    url = (url or '').strip()
    try:
        u = urllib.parse.urlparse(url)
        host = u.hostname or ''
    except ValueError:
        host = ''
    ok = url.startswith('https://') and (host in ('maps.app.goo.gl', 'goo.gl', 'g.page') or re.fullmatch(r'(www\.|maps\.)?google\.[a-z.]+', host))
    return url if ok else 'https://maps.google.com/?q=' + urllib.parse.quote_plus(address)


def parse_time(t):
    t = t.strip().lower().replace('.', '')
    m = re.fullmatch(r'(\d{1,2})(?::(\d{2}))?\s*(am|pm|a|p)?', t)
    if not m:
        return None
    h, mi, ap = int(m[1]), int(m[2] or 0), m[3]
    if ap:
        if h == 12:
            h = 0
        if ap.startswith('p'):
            h += 12
    elif m[2] is None:
        return None   # a bare number like "11" is too ambiguous
    if h == 24 and mi == 0:
        return '24:00'
    if h > 23 or mi > 59:
        return None
    return f'{h:02d}:{mi:02d}'


def parse_days(s):
    s = s.strip().lower()
    if s in ('daily', 'everyday', 'every day', '7 days', 'mon-sun', 'monday-sunday'):
        return list(range(7))
    out = []
    for part in re.split(r'\s*[,&/]\s*|\s+and\s+', s):
        ends = re.split(r'\s*(?:-|–|—|\bto\b|through|thru)\s*', part)
        idx = []
        for e in ends:
            e = e.strip()[:3]
            if e not in [d.lower() for d in DAYS_EN3]:
                return None
            idx.append([d.lower() for d in DAYS_EN3].index(e))
        if len(idx) == 1:
            out.append(idx[0])
        elif len(idx) == 2:
            a, b = idx
            out += [(a + i) % 7 for i in range((b - a) % 7 + 1)]
        else:
            return None
    return sorted(set(out))


def parse_hours(raw):
    """'Mon-Fri 11:00-21:00; Sat-Sun 10:00-22:00' -> {0: [('11:00','21:00')], ...} (0 = Monday), or None."""
    raw = (raw or '').strip()
    if not raw:
        return None
    week = {d: None for d in range(7)}
    seen = False
    for seg in re.split(r'\s*[;\n]\s*', raw):
        if not seg:
            continue
        m = re.match(r'^(?P<days>[A-Za-z][A-Za-z,&/\s\-–—]*?)\s*:?\s+(?P<times>(?:\d|closed).*)$', seg, re.I)
        if not m:
            return None
        days = parse_days(m['days'])
        if days is None:
            return None
        if m['times'].strip().lower() == 'closed':
            ranges = None
        else:
            ranges = []
            for r in re.split(r'\s*[,&]\s*|\s+and\s+', m['times']):
                p = re.split(r'\s*(?:-|–|—|\bto\b)\s*', r.strip())
                if len(p) != 2:
                    return None
                a, b = parse_time(p[0]), parse_time(p[1])
                if not a or not b:
                    return None
                ranges.append((a, b))
        for d in days:
            week[d] = ranges
        seen = True
    return week if seen and any(week.values()) else None


# ---------------------------------------------------------------- hours rendering
def t12(t):
    h, m = map(int, t.split(':'))
    suf = 'AM' if h % 24 < 12 else 'PM'
    return f'{(h % 12) or 12}:{m:02d} {suf}'


def fmt_ranges(ranges, lang):
    if lang == 'en':
        return ', '.join(f'{t12(a)}–{t12(b)}' for a, b in ranges)
    return '、'.join(f'{a}–{b}' for a, b in ranges)


def groups(week):
    """Consecutive days (Mon..Sun) with identical hours -> [(first, last, ranges)]"""
    out = []
    for d in range(7):
        if out and out[-1][2] == week[d] and out[-1][1] == d - 1:
            out[-1][1] = d
        else:
            out.append([d, d, week[d]])
    return out


def day_label(a, b, lang):
    if lang == 'en':
        if a == 0 and b == 6:
            return 'Daily'
        return DAYS_EN3[a] if a == b else (f'{DAYS_EN3[a]} and {DAYS_EN3[b]}' if b == a + 1 else f'{DAYS_EN3[a]} to {DAYS_EN3[b]}')
    if a == 0 and b == 6:
        return '每天'
    return DAYS_ZH2[a] if a == b else (f'{DAYS_ZH2[a]}、{DAYS_ZH2[b]}' if b == a + 1 else f'{DAYS_ZH2[a]}至{DAYS_ZH2[b]}')


def hours_tokens(week, lang, slug):
    zh = lang != 'en'
    closed = 'Closed' if not zh else CLOSED_WORD.get(slug, '公休')
    if week is None:
        msg = 'Please call or check Google Maps for current hours' if not zh else '營業時間請來電或查看 Google 地圖'
        return {
            'HOURS_ROWS': f'              <tr><th scope="row">{"Hours" if not zh else "時間"}</th><td>{msg}</td></tr>',
            'HOURS_LINES': msg, 'HOURS_DL': f'        <dt>{"Hours" if not zh else "時間"}</dt><dd>{msg}</dd>',
            'HOURS_LI': f'          <li>{msg}</li>', 'HOURS_SHORT': 'Call us' if not zh else '請來電',
            'HOURS_FACT': 'Call for opening hours' if not zh else '營業時間請來電詢問',
            'HOURS_JS': 'null', 'J_HOURS': '',
        }
    rows = []
    for d in range(7):
        r = week[d]
        label = (DAYS_EN if not zh else DAYS_ZH)[d]
        cell = f'<td>{fmt_ranges(r, lang)}</td>' if r else f'<td class="closed">{closed}</td>'
        rows.append(f'              <tr data-day="{(d + 1) % 7}"><th scope="row">{label}</th>{cell}</tr>')
    gs = groups(week)
    lines = []
    for a, b, r in gs:
        lab = day_label(a, b, lang)
        lines.append((lab, fmt_ranges(r, lang) if r else closed))
    open_groups = []   # runs of open days, whatever their hours (Mon-Fri 9-6 + Sat 9-2 -> Mon to Sat)
    for d in range(7):
        if week[d]:
            if open_groups and open_groups[-1][1] == d - 1:
                open_groups[-1][1] = d
            else:
                open_groups.append([d, d])
    short = ('7 days' if not zh else '每天') if all(week.values()) else (', ' if not zh else '、').join(day_label(a, b, lang) for a, b in open_groups)
    fact = ('Open 7 days' if not zh else '每天營業') if all(week.values()) else (f'Open {short}' if not zh else f'{short}營業')
    if slug == 'clinic' and zh:
        fact = fact.replace('營業', '看診')
    js = json.dumps({str((d + 1) % 7): ([list(x) for x in week[d]] if week[d] else None) for d in range(7)})
    spec = []
    for a, b, r in gs:
        if not r:
            continue
        for o, c in r:
            spec.append({'@type': 'OpeningHoursSpecification', 'dayOfWeek': SCHEMA_DAYS[a:b + 1], 'opens': o, 'closes': '23:59' if c == '24:00' else c})
    return {
        'HOURS_ROWS': '\n'.join(rows),
        'HOURS_LINES': '<br>'.join(f'{l} {v}' if not zh else f'{l} {v}' for l, v in lines),
        'HOURS_DL': '\n'.join(f'        <dt>{l}</dt><dd>{v}</dd>' for l, v in lines),
        'HOURS_LI': '\n'.join(f'          <li>{l} {v}</li>' for l, v in lines),
        'HOURS_SHORT': short, 'HOURS_FACT': fact, 'HOURS_JS': js,
        'J_HOURS': ',\n  "openingHoursSpecification": ' + json.dumps(spec, ensure_ascii=False),
    }


# ---------------------------------------------------------------- banner
BANNER = {
    'en': 'Free preview made by Polyglot Pages. This is not the official website of {name}. Contact: {mail}',
    'zh-TW': '這是 Polyglot Pages 免費製作的網站預覽，不是{name}的官方網站。聯絡：{mail}',
}
BANNER_CSS = """
/* ==================== Demo banner (added by scripts/demo/make-demo.py) ==================== */
:root { --demo-h: 2.6rem; }
@media (max-width: 1100px) { :root { --demo-h: 3.8rem; } }
@media (max-width: 760px) { :root { --demo-h: 5.2rem; } }
html { scroll-padding-top: calc(@PAD@ + var(--demo-h)); }
body { padding-top: var(--demo-h); }
.site-header { top: var(--demo-h); }
.demo-bar { position: fixed; inset: 0 0 auto; z-index: 100; display: flex; align-items: center; justify-content: center; height: var(--demo-h); overflow: hidden; padding: .4rem 1rem; background: var(--text); color: var(--bg); font: 400 .8rem/1.45 var(--font-body); letter-spacing: normal; text-align: center; }
.js .demo-bar { height: auto; }
.demo-bar p { max-width: 62rem; margin: 0; }
.demo-bar b { font-weight: 700; }
.demo-bar a { color: inherit; text-decoration: underline; text-underline-offset: 2px; overflow-wrap: anywhere; }
.demo-bar a:hover { text-decoration-thickness: 2px; }
.demo-bar a:active { opacity: .75; }
.demo-bar a:focus-visible { outline: 2px solid var(--bg); outline-offset: 2px; border-radius: 3px; }
.demo-note { display: block; width: fit-content; max-width: 42rem; padding: .45rem .8rem; border: 1px dashed color-mix(in srgb, var(--muted) 55%, transparent); border-radius: 10px; color: var(--muted); font-size: .88rem; line-height: 1.6; }
.center .demo-note, .sec-head.center .demo-note { margin-inline: auto; }
.site-footer .demo-note, .reserve .demo-note, .trial .demo-note { color: inherit; border-color: currentColor; }
"""
BANNER_JS = ("<script>(function(){var b=document.getElementById('demo-bar'),r=document.documentElement;"
             "function s(){r.style.setProperty('--demo-h',b.offsetHeight+'px');}s();addEventListener('resize',s);addEventListener('load',s);"
             "if(window.ResizeObserver)new ResizeObserver(s).observe(b);})();</script>")


def banner_html(lang, name):
    text = BANNER['zh-TW' if lang != 'en' else 'en']
    if lang == 'zh-CN':
        text = TW2SP.convert(text)
    mail = f'<a href="mailto:{CONTACT}">{CONTACT}</a>'
    shown = name if (lang == 'en' or CJK.search(name)) else f' {name} '
    text = html.escape(text).replace('Polyglot Pages', '<b>Polyglot Pages</b>').replace('{name}', html.escape(shown)).replace('{mail}', mail)
    return f'<!-- Demo banner: this page is a free preview, not the business\'s own website -->\n<div class="demo-bar" id="demo-bar" role="note"><p>{text}</p></div>\n{BANNER_JS}\n'


# ---------------------------------------------------------------- page building
def esc(s):
    return html.escape(str(s), quote=True)


def jstr(s):
    return json.dumps(s, ensure_ascii=False).replace('</', '<\\/')


def fill(page, lang, slug, variant, lead):
    zh = lang != 'en'
    cn = lang == 'zh-CN'
    conv = (lambda s: TW2SP.convert(s)) if cn else (lambda s: s)
    name_en, name_zh = lead['name_en'], lead['name_zh']
    if zh and name_zh:
        name = T2S.convert(name_zh) if cn else S2T.convert(name_zh)
        alt = f'<span lang="en">{esc(name_en)}</span>' if name_en != name_zh else ''
    else:
        name = name_en
        alt = f'<span lang="zh-Hant">{esc(S2T.convert(name_zh))}</span>' if (name_zh and not zh) else ''
    city_zh = CITY_ZH.get(lead['city'].lower(), lead['city'])
    city_zh = T2S.convert(city_zh) if cn else city_zh
    notes = lead['notes_en'] if not zh else (conv(lead['notes_zh']) if (lead['notes_zh'] and name_zh) else '')
    kind_en, kind_zh = KIND[(slug, variant)]
    desc = notes or (f'{kind_en} in {lead["city"]}, {lead["state"]}.' if not zh else conv(f'{city_zh}的{kind_zh}。'))

    # 1. category blocks
    for v in ('dental', 'tcm'):
        keep = v == variant
        page = re.sub(r'<!--IF:%s-->(.*?)<!--/IF:%s-->' % (v, v), (lambda m: m.group(1)) if keep else '', page, flags=re.S)
    # 2. simple tokens
    hours = hours_tokens(lead['week'], 'zh-TW' if zh else 'en', slug)
    if cn:
        hours = {k: (TW2SP.convert(v) if k not in ('HOURS_JS', 'J_HOURS') else v) for k, v in hours.items()}
    values = {
        'NAME': esc(name), 'CITY': esc(lead['city']), 'CITY_ZH': esc(city_zh) if CJK.search(city_zh) else f' {esc(city_zh)} ', 'STATE': esc(lead['state']),
        'ADDR': esc(lead['address']), 'ADDR_L1': esc(lead['street']),
        'ADDR_L2': esc(f'{lead["city"]}, {lead["state"]} {lead["zip"]}'.strip().rstrip(',')),
        'PHONE': esc(lead['phone']), 'TEL': esc(lead['tel']), 'MAPS': esc(lead['maps']), 'YELP': esc(lead['yelp']),
        'TZ': jstr(lead['tz']),
        'J_NAME': jstr(name), 'J_ALT': ('\n  "alternateName": ' + jstr(name_en if (zh and name_zh) else (name_zh or '')) + ',') if name_zh and name_zh != name_en else '',
        'J_DESC': jstr(desc), 'J_TEL': jstr(lead['tel'] or lead['phone']), 'J_MAP': jstr(lead['maps']),
        'J_ADDRESS': json.dumps({'@type': 'PostalAddress', 'streetAddress': lead['street'], 'addressLocality': lead['city'],
                                 'addressRegion': lead['state'], 'postalCode': lead['zip'], 'addressCountry': 'US'}, ensure_ascii=False),
        **{k: v for k, v in hours.items() if k.startswith('J_') or k == 'HOURS_JS'},
        **{k: v for k, v in hours.items() if not (k.startswith('J_') or k == 'HOURS_JS')},
    }
    page = re.sub(r'\{\{([A-Z0-9_]+)\}\}', lambda m: values[m.group(1)] if m.group(1) in values else m.group(0), page)
    # 3. tokens with a fallback: {{NOTES|...}}, {{NOTES_ZH|...}}, {{ALT_NAME|...}}
    fb = {'NOTES': esc(notes) if not zh else None, 'NOTES_ZH': esc(notes) if zh else None, 'ALT_NAME': alt or None}
    page = re.sub(r'\{\{(NOTES|NOTES_ZH|ALT_NAME)\|([^{}]*)\}\}', lambda m: fb[m.group(1)] or m.group(2), page)
    left = re.findall(r'\{\{[^}]*\}\}|<!--/?IF:', page)
    if left:
        raise SystemExit(f'底稿還有沒填的欄位：{sorted(set(left))[:5]}')
    # 4. preview banner, noindex, banner styles
    page = page.replace('<meta name="viewport" content="width=device-width, initial-scale=1">',
                        '<meta name="viewport" content="width=device-width, initial-scale=1">\n<meta name="robots" content="noindex,nofollow">', 1)
    css = BANNER_CSS.replace('@PAD@', SCROLL_PAD[slug]) + EXTRA_CSS.get(slug, '')
    page = page.replace('</style>', css + '</style>', 1)
    page = re.sub(r'(<body[^>]*>\n(?:<a class="skip"[^\n]*\n)?)', lambda m: m.group(1) + banner_html(lang, name), page, count=1)
    return page


def slugify(s):
    s = re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')
    return re.sub(r'-{2,}', '-', s)


def prepare(row, notes_zh_arg=None):
    cat = (row.get('category') or '').strip().lower()
    if cat not in CATEGORY:
        raise SystemExit(f'lead {row.get("id")}: 不認得的 category「{cat}」（要用 restaurant／dental／tcm／tutoring／salon）')
    slug, variant = CATEGORY[cat]
    name_en, name_zh = split_name(row.get('business', ''))
    if not name_en:
        raise SystemExit(f'lead {row.get("id")}: 沒有店名')
    street, city, state, zipc = parse_address(row.get('address', ''), (row.get('city') or '').strip())
    city = (row.get('city') or city or '').strip()
    phone, tel = format_phone(row.get('phone', ''))
    notes_en, notes_zh = split_notes(row.get('notes', ''))
    if notes_zh_arg:
        notes_zh = notes_zh_arg.strip()
    if notes_zh and notes_zh[-1] not in '。！？.!?':
        notes_zh += '。'
    address = ' '.join((row.get('address') or '').split())
    lead = dict(name_en=name_en, name_zh=name_zh, street=street, city=city, state=state or '', zip=zipc, address=address,
                phone=phone, tel=tel, notes_en=notes_en, notes_zh=notes_zh, week=parse_hours(row.get('hours', '')),
                tz=TZ.get(state, 'America/Los_Angeles'))
    lead['maps'] = safe_maps_url(row.get('google_maps_url', ''), address)
    lead['yelp'] = 'https://www.yelp.com/search?' + urllib.parse.urlencode({'find_desc': name_en, 'find_loc': f'{city}, {state}'.strip(', ')})
    return slug, variant, lead


def build(row, rows, notes_zh_arg=None, out_root=DEMOS):
    slug, variant, lead = prepare(row, notes_zh_arg)
    shop = slugify(f'{lead["name_en"]} {lead["city"]}') if not CJK.search(lead['name_en']) else ''
    shop = shop or f'lead-{row["id"]}'
    taken = {r.get('demo_url', '').strip('/').split('/')[-1] for r in rows if r is not row and r.get('demo_url')}
    if shop in taken:
        shop = f'{shop}-{row["id"]}'
    out = out_root / shop
    pages = {lang: fill((BASE / slug / lang / 'index.html').read_text(encoding='utf-8'), lang, slug, variant, lead) for lang in LANGS}
    for lang, page in pages.items():   # write only after all three languages built without errors
        d = out / lang
        d.mkdir(parents=True, exist_ok=True)
        (d / 'index.html').write_text(page, encoding='utf-8')
    # language entry page (same logic as the published templates), plus noindex and a small record for cleanup.py
    subprocess.run([sys.executable, str(ROOT / 'scripts/lang-index.py'), str(out)], check=True)
    idx = out / 'index.html'
    stamp = f'<!-- polyglot-demo lead={row["id"]} created={datetime.date.today().isoformat()} -->'
    t = idx.read_text(encoding='utf-8').replace('<meta name="viewport" content="width=device-width, initial-scale=1">',
                                                 '<meta name="viewport" content="width=device-width, initial-scale=1">\n<meta name="robots" content="noindex,nofollow">\n' + stamp, 1)
    idx.write_text(t, encoding='utf-8')
    warn = []
    if lead['week'] is None:
        warn.append(f'營業時間看不懂（{row.get("hours", "")!r}），先放「請來電」的通用文字')
    if lead['name_zh'] and not lead['notes_zh']:
        warn.append('有中文店名但沒有中文的 notes：中文版用通用句子（可加 --notes-zh "一句中文"）')
    if not lead['zip']:
        warn.append(f'地址格式看不懂（{lead["address"]!r}），JSON-LD 只放整串地址')
    return shop, variant, warn


def read_csv(path):
    with open(path, newline='', encoding='utf-8') as f:
        r = csv.DictReader(f)
        return r.fieldnames, list(r)


def write_csv(path, fields, rows):
    with open(path, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator='\n')
        w.writeheader()
        w.writerows(rows)


def main():
    ap = argparse.ArgumentParser(description='Build a free trilingual preview site for a lead.')
    ap.add_argument('lead_id', nargs='?')
    ap.add_argument('--csv', default=str(ROOT / 'sales/outreach/leads.csv'))
    ap.add_argument('--all-new', action='store_true', help='build every lead whose status is new')
    ap.add_argument('--notes-zh', help='Chinese version of the notes sentence (only used when the business has a Chinese name)')
    ap.add_argument('--out', default=str(DEMOS), help='output folder (default: demos/)')
    a = ap.parse_args()
    if not a.lead_id and not a.all_new:
        ap.error('give a lead_id or --all-new')
    fields, rows = read_csv(a.csv)
    for col in ('demo_url', 'status'):
        if col not in fields:
            fields.append(col)
    todo = [r for r in rows if (r.get('status') or '').strip() == 'new'] if a.all_new else [r for r in rows if (r.get('id') or '').strip() == a.lead_id]
    if not todo:
        sys.exit('找不到要做的 lead' if not a.all_new else '沒有 status 是 new 的 lead')
    out_root = pathlib.Path(a.out)
    for r in todo:
        shop, variant, warn = build(r, rows, a.notes_zh if not a.all_new else None, out_root)
        r['demo_url'] = f'demos/{shop}/'
        r['status'] = 'demo'
        label = r['category']
        print(f'✓ lead {r["id"]} {r["business"]} [{label}] → {out_root / shop}/')
        for w in warn:
            print('  ! ' + w)
    write_csv(a.csv, fields, rows)
    print(f'✓ 已更新 {a.csv}（demo_url、status=demo）')


if __name__ == '__main__':
    main()
