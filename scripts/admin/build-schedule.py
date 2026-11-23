#!/usr/bin/env python3
"""產生後台排程 admin/schedule.json（Polyglot Pages｜後台用）。

資料來源（都在 repo 裡）：
  sales/videos/發片時程.md            每天的短影片（日期、檔名、內容、時間）
  sales/videos/<檔名>.txt             置頂留言
  sales/substack/notes.md             Substack Notes 第 X 週第 Y 天
  sales/substack/posts/0N-*.md        週二文章
  sales/今天上架總表.md、Gumroad上架步驟.md   Gumroad 上架清單
  sales/pins/*.csv                    Pinterest 批次檔
  sales/outreach/leads.csv            只取各狀態的「數量」當開發頁的起始值，不放店名、Email、連結

用法：python3 scripts/admin/build-schedule.py
隱私：輸出的檔案會公開在 GitHub Pages，這裡只放計畫與公開網址，不放客戶資料、Drive 連結或個人信箱。
"""
import csv
import datetime as dt
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[2]
SALES = ROOT / 'sales'
OUT = ROOT / 'admin' / 'schedule.json'

START = dt.date(2026, 11, 23)
END = dt.date(2027, 2, 28)
# 第 N 天 = 日期 − 11/23 + 1（11/23 已發第 1 則，11/24 是第 1 週第 2 天）。
# notes.md 開頭寫「第 1 週第 1 天＝11/24」；如果 11/23 其實沒發，把這裡改成 11/24 重新產生即可。
NOTES_DAY1 = dt.date(2026, 11, 23)
GH = 'https://github.com/a0955072107-bit/-/blob/main/'
STORE = 'https://polyglotpages.gumroad.com'
WD = '一二三四五六日'


def d2s(d):
    return d.isoformat()


def md(d):
    return f'{d.month}/{d.day}（{WD[d.weekday()]}）'


items = []


def add(date, time, title, who, cat, prompt=None, files=None, note=None, key=None, **extra):
    assert who in ('你', '擴充功能', 'Claude'), who
    assert cat in ('上架', 'Pinterest', '影片', 'Substack', '開發', '檢查'), cat
    it = {
        'id': f'{d2s(date)}-{key or time.replace(":", "")}',
        'date': d2s(date), 'time': time, 'title': title, 'who': who, 'cat': cat,
    }
    if prompt:
        it['prompt'] = prompt.strip()
    if files:
        it['files'] = files
    if note:
        it['note'] = note
    it.update(extra)
    items.append(it)


# ---------- 短影片時程 ----------
def parse_videos():
    text = (SALES / 'videos' / '發片時程.md').read_text(encoding='utf-8')
    out = []
    year_of = lambda m: 2026 if m >= 11 else 2027
    for m in re.finditer(r'^\|\s*(\d+)/(\d+)（.）\s*\|\s*`([^`]+)`\s*\|\s*([^|]+?)\s*\|\s*(\d\d:\d\d)\s*\|', text, re.M):
        mo, da, f, what, t = int(m[1]), int(m[2]), m[3], m[4], m[5]
        d = dt.date(year_of(mo), mo, da)
        txt = (SALES / 'videos' / f.replace('.mp4', '.txt')).read_text(encoding='utf-8')
        pin = re.search(r'置頂留言[^：]*：\s*(.+)', txt, re.S)
        caption = txt.split('置頂留言')[0].strip()
        out.append({'date': d, 'file': f, 'what': what, 'time': t, 'pin': pin[1].strip() if pin else '', 'caption': caption})
    return out


VIDEOS = parse_videos()
VID_BY_DATE = {v['date']: v for v in VIDEOS}


# ---------- Substack Notes ----------
def parse_notes():
    text = (SALES / 'substack' / 'notes.md').read_text(encoding='utf-8')
    weeks = re.split(r'^## 第 (\d) 週.*$', text, flags=re.M)
    notes = {}
    for i in range(1, len(weeks), 2):
        w = int(weeks[i])
        for m in re.finditer(r'^(\d)\. (.+)$', weeks[i + 1], re.M):
            notes[(w, int(m[1]))] = m[2].strip()
    return notes


NOTES = parse_notes()


def note_for(d):
    n = (d - NOTES_DAY1).days + 1          # 第 N 天
    if n < 1:
        return None
    w, day = (n - 1) // 7 + 1, (n - 1) % 7 + 1
    t = NOTES.get((w, day))
    return (w, day, t) if t else None


# ---------- 每天 08:31：影片置頂留言 ＋ Substack Note ----------
def video_part(v):
    return (f'1. 到 TikTok 和 YouTube Shorts，找今天 {v["time"]} 發出的影片（{v["file"]}，{v["what"]}），'
            f'留言貼上下面這段，然後把這則留言置頂：\n{v["pin"]}')


def note_part(w, day, text, num):
    return (f'{num}. 照 {GH}sales/substack/擴充功能發文.md 發第 {w} 週第 {day} 天的 Note：打開 Substack Notes，'
            f'貼上下面這則，不要按發布，我自己按。\n{text}')


d = START + dt.timedelta(days=1)
while d <= END:
    v, n = VID_BY_DATE.get(d), note_for(d)
    if v and v['time'] != '08:00':
        # 晚上發的影片（例：12/3 日文版 19:00）：Note 照樣 08:31，置頂留言改到發片後 31 分
        if n:
            add(d, '08:31', f'Substack Note 第 {n[0]} 週第 {n[1]} 天', '擴充功能', 'Substack',
                prompt=note_part(*n, 1), files=['sales/substack/notes.md'], key='note')
        hh, mm = v['time'].split(':')
        add(d, f'{hh}:31', f'影片置頂留言：{v["what"]}', '擴充功能', '影片',
            prompt=video_part(v), files=[f'sales/videos/{v["file"].replace(".mp4", ".txt")}'], key='video')
    elif v or n:
        parts, files = [], []
        if v:
            parts.append(video_part(v)); files.append(f'sales/videos/{v["file"].replace(".mp4", ".txt")}')
        if n:
            parts.append(note_part(*n, len(parts) + 1)); files.append('sales/substack/notes.md')
        title = ('影片置頂留言' if v else '') + ('＋' if v and n else '') + (f'Substack Note（第 {n[0]} 週第 {n[1]} 天）' if n else '')
        add(d, '08:31', title, '擴充功能', '影片' if v else 'Substack',
            prompt='今天兩件事，做完各回報一行：\n\n' + '\n\n'.join(parts) if len(parts) > 1 else parts[0],
            files=files, key='daily', sub=(v['what'] if v else None))
    d += dt.timedelta(days=1)

# ---------- 每週五 10:37：排下週 TikTok ----------
d = START
while d <= END:
    if d.weekday() == 4:
        mon = d + dt.timedelta(days=3)
        week = [VID_BY_DATE[mon + dt.timedelta(days=i)] for i in range(7) if (mon + dt.timedelta(days=i)) in VID_BY_DATE]
        if week:
            lines = '\n\n'.join(f'{i + 1}. {md(v["date"])} {v["time"]}　{v["file"]}（{v["what"]}）\n說明文字：\n{v["caption"]}'
                                for i, v in enumerate(week))
            add(d, '10:37', f'TikTok 預排下週 {len(week)} 支（{md(week[0]["date"])}～{md(week[-1]["date"])}）', '擴充功能', '影片',
                prompt=(f'照 {GH}sales/videos/發片時程.md，在電腦版 TikTok Studio 預排下面 {len(week)} 支影片（台灣時間）。'
                        '影片檔要我拖進上傳框，每支開始前告訴我檔名，等我說好再填。說明文字一字不改貼上，'
                        '加一首平台內建音樂並把音量調低。不要改帳號設定，遇到驗證就停下來問。每排好一支回報一行。\n\n' + lines),
                files=[f'sales/videos/{v["file"]}' for v in week], key='tiktok')
    d += dt.timedelta(days=1)

# ---------- 每週日 14:17：新模板（Claude 做，你合併 PR） ----------
d = START
while d <= END:
    if d.weekday() == 6 and d >= dt.date(2026, 11, 29):
        add(d, '14:17', '本週新模板（Claude 做好開 PR，你看過合併）', 'Claude', '上架',
            prompt=('照 sales/營運流程.md「每款新模板的製作流程」做本週的新模板：先看 Gumroad 與 Pinterest 數據挑行業，'
                    '做中英文版、封面、zip、上架文案（加進 sales/Gumroad上架步驟.md），再做 3 張 Pinterest 圖和一份小 CSV。'
                    '跑 bash scripts/lint-all.sh 確認 0 個 FAIL，然後開 PR 給我。'),
            files=['sales/營運流程.md', 'templates/SPEC.md'], key='template',
            note='PR 合併後，週一照上架文案上架這 1 款')
    d += dt.timedelta(days=1)

# ---------- 每週一 09:07：記上週數字 ----------
d = dt.date(2026, 11, 30)
while d <= END:
    if d.weekday() == 0:
        add(d, '09:07', '記上週數字（Pinterest、TikTok、YouTube、Substack、Gumroad）', '你', '檢查',
            note='到各平台後台看數字，填進後台「紀錄」→ 每週數字', key='weekly')
    d += dt.timedelta(days=1)

# ---------- 每天 13:07：寄開發信／私訊 ----------
d = START + dt.timedelta(days=1)
while d <= dt.date(2027, 2, 28):
    wk = (d - START).days // 7 + 1
    qty = 10 if wk == 1 else 20 if wk == 2 else 30
    add(d, '13:07', f'寄今天的開發信／私訊（約 {qty} 家）', '你', '開發',
        note=f'Claude 放在 sales/outreach/outbox/{d2s(d)}.md；寄完把數字加到「開發」頁。Instagram／FB 私訊新帳號一天最多 5～10 則',
        files=[f'sales/outreach/outbox/{d2s(d)}.md'], key='outreach')
    d += dt.timedelta(days=1)

# ---------- Gumroad 上架：11/24～11/26 每天 10 款 ----------
NAMES = {
    'clinic': '牙醫／診所', 'consulting': '律師／會計／顧問', 'studio': '設計工作室', 'bnb': '民宿 B&B', 'photographer': '攝影師',
    'pet': '寵物美容', 'education': '補習班', 'interior': '室內設計', 'bakery': '烘焙甜點', 'tea': '手搖飲',
    'auto': '汽車美容／保養', 'cleaning': '居家清潔', 'florist': '花店', 'yoga': '瑜珈／皮拉提斯', 'camping': '露營區',
    'coach': '諮商／教練', 'contractor': '水電修繕', 'nonprofit': '非營利／教會', 'linkinbio': 'Link-in-bio', 'barber': '男士理髮',
    'conference': '研討會活動', 'tattoo': '刺青工作室', 'coworking': '共享辦公室',
    'motion/saas': 'Motion SaaS', 'motion/portfolio': 'Motion 作品集', 'motion/restaurant': 'Motion 餐廳',
    'motion/wedding': 'Motion 婚禮', 'motion/realestate': 'Motion 豪宅',
    'bundle-all': '全套組合包', 'bundle-motion': 'Motion 組合包',
}
LISTING = [
    (dt.date(2026, 11, 24), ['clinic', 'consulting', 'studio', 'bnb', 'photographer', 'pet', 'education', 'interior', 'bakery', 'tea']),
    (dt.date(2026, 11, 25), ['auto', 'cleaning', 'florist', 'yoga', 'camping', 'coach', 'contractor', 'nonprofit', 'linkinbio', 'barber']),
    (dt.date(2026, 11, 26), ['conference', 'tattoo', 'coworking', 'motion/saas', 'motion/portfolio', 'motion/restaurant',
                             'motion/wedding', 'motion/realestate', 'bundle-all', 'bundle-motion']),
]
GUMROAD_BEFORE = 9   # 11/23 已上架：客製服務 2 ＋ 第 2 批 6 款 ＋ beauty
GUMROAD_TOTAL = 39
assert GUMROAD_BEFORE + sum(len(s) for _, s in LISTING) == GUMROAD_TOTAL


def cover(slug):
    return {'bundle-all': 'restaurant', 'bundle-motion': 'motion-wedding'}.get(slug, slug.replace('/', '-'))


def section(slug):
    if slug.startswith('motion/'):
        return '第 7 節 Motion'
    if slug == 'bundle-all':
        return '第 5 節＋第 9 節 Studio 版本'
    if slug == 'bundle-motion':
        return '第 7 節 Motion 全套組合包'
    return f'第 4 節「{NAMES[slug]}」'


for i, (d, slugs) in enumerate(LISTING):
    lst = '\n'.join(f'{k + 1}. {s}（{NAMES[s]}）：{section(s)}；封面 https://a0955072107-bit.github.io/-/covers/{cover(s)}-cover.png'
                    for k, s in enumerate(slugs))
    add(d, '11:15', f'Gumroad 上架 10 款（{"、".join(NAMES[s] for s in slugs[:3])}…）', '擴充功能', '上架',
        prompt=(f'照 {GH}sales/擴充功能上架.md 的規則上架，今天做下面 10 款，內容照 sales/Gumroad上架步驟.md 對應段落一字不改。'
                'zip 照 sales/擴充功能GoogleDrive交付.md 放進 Content 頁。只存草稿，不要按 Publish；每做完一款回報一行。\n\n' + lst),
        files=['sales/擴充功能上架.md', 'sales/今天上架總表.md', 'sales/Gumroad上架步驟.md'], key='gumroad',
        listing=len(slugs), products=[NAMES[s] for s in slugs],
        note='擴充功能存好草稿後，你逐一打開檢查再按 Publish')

# ---------- Pinterest ----------
def pin_rows(name):
    with open(SALES / 'pins' / name, encoding='utf-8') as f:
        return list(csv.DictReader(f))


for day, fname in ((dt.date(2026, 11, 24), 'pinterest-now2-2026-11-24.csv'), (dt.date(2026, 11, 25), 'pinterest-now2-2026-11-25.csv')):
    n = len(pin_rows(fname))
    add(day, '15:07', f'Pinterest 上傳 {n} 張（上架 10 款之後）', '你', 'Pinterest',
        note='Pinterest → 建立 → 批次建立 Pin → 上傳 CSV。Publish date 留空＝立即發布；有錯誤的列截圖給 Claude',
        files=[f'sales/pins/{fname}', 'sales/Pinterest批次上傳.md'], key='pins', pins=n)

# 11/23 先發的 17 張連到商店首頁，商品 11/26 上架後改成各商品頁
link_of = {}
for f in ('pinterest-bulk.csv', 'pinterest-bulk-fix.csv', 'pinterest-now2-2026-11-24.csv', 'pinterest-now2-2026-11-25.csv'):
    for r in pin_rows(f):
        link_of.setdefault(r['Media URL'].rsplit('/', 1)[1], r['Link'])
extra = pin_rows('pinterest-now-2026-11-23-extra.csv')
fix_lines = []
for k, r in enumerate(extra):
    img = r['Media URL'].rsplit('/', 1)[1]
    fix_lines.append(f'{k + 1}. {img}「{r["Title"]}」→ {link_of[img]}')
add(dt.date(2026, 11, 26), '15:13', f'修正 {len(extra)} 張 Pin 的連結（改連到商品頁）', '擴充功能', 'Pinterest',
    prompt=(f'11/23 發的這 {len(extra)} 張 Pinterest Pin 原本連到商店首頁，今天商品都上架了，請在 Pinterest 逐張打開 → 編輯 → '
            '把「連結」改成下面對應的網址，其他欄位不要動。改完每張回報一行。遇到驗證就停下來問。\n\n' + '\n'.join(fix_lines)),
    files=['sales/pins/pinterest-now-2026-11-23-extra.csv'], key='pinfix')

# ---------- 開發：Instagram、追問、Fiverr ----------
add(dt.date(2026, 11, 24), '09:13', '開 Instagram 私訊專用帳號', '你', '開發',
    note='只用來私訊店家、不發文；放 3 張 Pinterest 圖當門面。新帳號第一週一天最多 5 則私訊',
    files=['sales/帳號註冊.md', 'sales/outreach/README.md', 'sales/brand/avatar.png'], key='ig')
for day, sent in ((dt.date(2026, 11, 27), '11/23'), (dt.date(2026, 11, 29), '11/24、11/25')):
    add(day, '10:21', f'追問 {sent} 寄出、還沒回覆的店家', '你', '開發',
        prompt=(f'照 sales/outreach/README.md「4 天沒回覆追問一次」：把 leads.csv 裡 {sent} 寄出、status 還是 sent 的店家，'
                '依 sales/outreach/訊息範本.md 寫好追問訊息，放進今天的 outbox，寄完我再把 status 改成 followup。'),
        files=['sales/outreach/README.md', 'sales/outreach/訊息範本.md'], key='followup',
        note='把提示貼給 Claude 準備追問訊息，你再複製寄出；追問只做一次')
add(dt.date(2026, 11, 30), '10:43', '開 Fiverr 服務與 Upwork 個人檔案', '你', '開發',
    prompt='照 sales/營運流程.md 第 1 週：幫我準備 Fiverr 服務「I will build a modern business website」的標題、說明、3 個方案價格和作品集（6 款 Demo 網址），以及 Upwork 個人檔案文字。',
    files=['sales/營運流程.md', 'sales/行銷計畫.md'], key='fiverr')

# ---------- Substack 週二文章 ----------
posts = sorted((SALES / 'substack' / 'posts').glob('0*.md'))
tue = dt.date(2026, 12, 1)
for p in posts:
    num = int(p.name[:2])
    if num < 2:
        continue
    title = p.read_text(encoding='utf-8').splitlines()[0].lstrip('# ').strip()
    add(tue, '09:43', f'Substack 第 {num} 篇：{title}', '擴充功能', 'Substack',
        prompt=f'照 {GH}sales/substack/擴充功能發文.md 把第 {num} 篇存成 Substack 草稿。',
        files=[f'sales/substack/posts/{p.name}'], key='post', note='擴充功能存好草稿後，你看過再按發布')
    tue += dt.timedelta(days=7)

# ---------- 之後的上架與檢查 ----------
add(dt.date(2026, 12, 7), '10:07', '寄信給買過的人（附舊客優惠碼）', '你', '上架',
    note='Gumroad → Emails，介紹 Motion 系列；營運流程第 2～3 週', files=['sales/營運流程.md'], key='buyers')
add(dt.date(2026, 12, 21), '11:15', '上架 Website Care 維護月費（$19／$29）', '擴充功能', '上架',
    prompt=(f'照 {GH}sales/擴充功能上架.md 的規則，把 sales/Gumroad上架步驟.md 第 12 節「Website Care」建成 Membership 商品草稿：'
            'Name、URL website-care、兩個方案 Care $19/month、Care Plus $29/month、Description 一字不改。不要按 Publish。'),
    files=['sales/Gumroad上架步驟.md'], key='care')
add(dt.date(2026, 12, 23), '11:15', 'Commission 可以用了：把訂金商品改回 Commission', '擴充功能', '上架',
    prompt=('Gumroad 帳號滿 30 天，Commission 類型應該可以用了。照 sales/Gumroad上架步驟.md 第 3 節與第 8 節：'
            '先確認新增商品時有沒有 Commission 類型，沒有就停下來告訴我。有的話把「網站客製服務」和「三語店家網站代製」各建一個 Commission 草稿'
            '（50% 訂金），內容照原本的商品。不要刪除或下架舊的訂金商品，我確認後自己處理。'),
    files=['sales/Gumroad上架步驟.md', 'sales/交付流程.md'], key='commission',
    note='新的發布後，把舊的訂金商品設成不公開，交付流程的連結也要換')
for day, label in ((dt.date(2026, 12, 23), '第 1 個月'), (dt.date(2027, 1, 22), '第 2 個月'), (dt.date(2027, 2, 21), '第 3 個月')):
    add(day, '14:43', f'成長檢查（{label}）', 'Claude', '檢查',
        prompt=(f'這是 Polyglot Pages {label}的成長檢查。下面是我後台的數字，請照 sales/營運流程.md「要追蹤的數字」看：'
                '哪個管道帶來最多瀏覽和銷售、哪幾款瀏覽多但賣不好（要不要調價或換封面）、開發信回覆率要怎麼改，'
                '給我下個月最該做的 3 件事。\n\n{{summary}}'),
        files=['sales/營運流程.md', 'sales/行銷計畫.md'], key='growth', note='按「複製」會自動帶入你在後台記的數字')
add(dt.date(2026, 12, 28), '14:13', '評估要不要開 LinkedIn', '你', '檢查',
    prompt=('照 sales/行銷計畫.md 第 9 節評估 LinkedIn：工作室授權有沒有開始賣、客製案有沒有 5 個以上、有沒有想接美國中小企業案。'
            '任一個成立就幫我準備個人檔案文字和前 2 篇貼文。\n\n{{summary}}'),
    files=['sales/行銷計畫.md'], key='linkedin')

items.sort(key=lambda x: (x['date'], x['time'], x['id']))
ids = [x['id'] for x in items]
assert len(ids) == len(set(ids)), 'id 重複'

# ---------- 重要日期 ----------
MILESTONES = [
    ('2026-11-24', '第 1 支短影片、第 1 則 Substack Note'),
    ('2026-11-24', 'Gumroad 上架 10 款（到 19/39）'),
    ('2026-11-25', 'Gumroad 上架 10 款（到 29/39）'),
    ('2026-11-26', 'Gumroad 39 款全部上架；Pinterest 預排開始每天自動發'),
    ('2026-11-30', '第 1 週：開 Fiverr／Upwork，開發信每天 20 家'),
    ('2026-12-01', 'Substack 第 2 篇（之後每週二 1 篇）'),
    ('2026-12-03', '日文版短影片（19:00 發）'),
    ('2026-12-20', 'Substack Notes 28 則發完（之後請 Claude 寫下一批）'),
    ('2026-12-21', 'Website Care 維護月費上架'),
    ('2026-12-23', 'Gumroad 滿 30 天：改用 Commission；第 1 次成長檢查'),
    ('2026-12-28', '評估要不要開 LinkedIn'),
    ('2027-01-01', '最後 1 支已做好的短影片'),
    ('2027-01-22', '第 2 次成長檢查'),
    ('2027-02-21', '第 3 次成長檢查'),
]

# ---------- 計畫中的累計數字（總覽 KPI 用；使用者可以在後台改） ----------
pins_plan = [{'date': '2026-11-23', 'n': len(pin_rows('pinterest-now-2026-11-23.csv')) + len(extra), 'label': '11/23 立即發布'}]
for it in items:
    if it.get('pins'):
        pins_plan.append({'date': it['date'], 'n': it['pins'], 'id': it['id'], 'label': it['title']})
bulk = pin_rows('pinterest-bulk.csv')[:100]                      # 已預排的 100 張（Pinterest 同時最多 100 張）
for r in bulk:
    t = dt.datetime.fromisoformat(r['Publish date']) + dt.timedelta(hours=8)   # CSV 是 UTC
    pins_plan.append({'at': t.strftime('%Y-%m-%dT%H:%M'), 'n': 1})

# ---------- 開發：只取各狀態的數量 ----------
counts = {'sent': 0, 'replied': 0, 'demo': 0, 'won': 0, 'lost': 0}
with open(SALES / 'outreach' / 'leads.csv', encoding='utf-8') as f:
    for r in csv.DictReader(f):
        s = (r.get('status') or '').strip()
        if s in ('sent', 'followup', 'replied', 'won', 'lost', 'optout'):
            counts['sent'] += 1
        if s in ('replied', 'won'):
            counts['replied'] += 1
        if s == 'won':
            counts['won'] += 1
        if s in ('lost', 'optout'):
            counts['lost'] += 1

data = {
    'generated': dt.datetime.now().strftime('%Y-%m-%d %H:%M'),
    'tz': 'Asia/Taipei',
    'range': [d2s(START), d2s(END)],
    'gumroad': {'before': GUMROAD_BEFORE, 'beforeDate': '2026-11-23', 'total': GUMROAD_TOTAL},
    'pinsPlan': pins_plan,
    'videos': [{'date': d2s(v['date']), 'time': v['time'], 'file': v['file'], 'what': v['what']} for v in VIDEOS],
    'outreachSeed': counts,
    'milestones': MILESTONES,
    'items': items,
}

# 隱私檢查：不能出現 Email、Google Drive 連結、權杖
blob = json.dumps(data, ensure_ascii=False)
for pat in (r'[\w.+-]+@[\w-]+\.[\w.]+', r'drive\.google|docs\.google', r'gh[pousr]_[A-Za-z0-9]{20,}|github_pat_'):
    m = re.search(pat, blob)
    assert not m, f'schedule.json 不能包含：{m[0]}'

OUT.parent.mkdir(exist_ok=True)
OUT.write_text(json.dumps(data, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print(f'✓ {OUT.relative_to(ROOT)}：{len(items)} 件事，{len(MILESTONES)} 個重要日期，{OUT.stat().st_size // 1024} KB')
