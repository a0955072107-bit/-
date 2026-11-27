#!/usr/bin/env python3
"""產生後台排程 admin/schedule.json（Polyglot Pages｜後台用）。

資料來源（都在 repo 裡）：
  sales/80萬計畫.md                    目標、關卡、暖身上限（這份為準；數字寫在下面 PLAN）
  sales/videos/發片時程.md            每天的短影片（日期、檔名、內容、時間）
  sales/videos/<檔名>.txt             置頂留言
  sales/substack/README.md            文章發文表（一週兩篇，週二、週五 22:00）
  sales/substack/notes.md             Substack Notes（第 1 週第 1 天＝11/24，台灣 21:00）
  sales/outreach/outbox/2026-12-followups.md   追問信：哪一組、哪天早上排
  sales/outreach/outbox/*.md          各批開發信（Gmail 已排程的時間寫在下面 SENDS）
  sales/今天上架總表.md、Gumroad上架步驟.md   Gumroad 上架清單
  sales/pins/*.csv                    Pinterest 批次檔
  sales/outreach/leads.csv、linkedin.csv   只取「數量」，不放店名、人名、Email、連結

用法：python3 scripts/admin/build-schedule.py（scripts/build-site.sh 每次部署都會跑；只用標準函式庫）
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
# notes.md：第 1 週第 1 天＝11/24（二），之後每天 1 則。
NOTES_DAY1 = dt.date(2026, 11, 24)
NOTES_SCHEDULED_TO = dt.date(2026, 12, 7)    # notes.md：11/27 已在 Substack 定時到 12/7（台灣 21:00）
TPE = dt.timezone(dt.timedelta(hours=8))
# 計畫數字（sales/80萬計畫.md，11/26、11/27 版）
PLAN = {
    'goalTwd': 800000, 'goalDate': '2027-07-31', 'grossUsd': [28000, 29000],
    'basic': 299, 'pro': 499, 'care': 49,
    # Email 暖身上限（24 小時內合計，追問信也算）：[開始日, 上限文字]
    'emailCap': [['2026-11-22', '15'], ['2026-12-01', '20'], ['2026-12-08', '30'], ['2026-12-15', '40～50']],
    'replyRate': '3～5%',
}
GH = 'https://github.com/a0955072107-bit/-/blob/main/'
STORE = 'https://polyglotpages.gumroad.com'
WD = '一二三四五六日'


def d2s(d):
    return d.isoformat()


def md(d):
    return f'{d.month}/{d.day}（{WD[d.weekday()]}）'


items = []


def add(date, time, title, who, cat, prompt=None, files=None, note=None, key=None, **extra):
    assert who in ('你', '擴充功能', 'Claude', '自動'), who
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


# ---------- 每天：影片發出後 31 分，貼置頂留言 ----------
# Substack Notes 不再每天手動發：已定時到 12/7，之後每週五排下一週（見下面「每週五」）。
for v in VIDEOS:
    if v['date'] <= START:
        continue
    hh = v['time'].split(':')[0]
    add(v['date'], f'{hh}:31', f'影片置頂留言：{v["what"]}', '擴充功能', '影片',
        prompt=(f'到 TikTok 和 YouTube Shorts，找今天 {v["time"]} 發出的影片（{v["file"]}，{v["what"]}），'
                f'留言貼上下面這段，然後把這則留言置頂：\n{v["pin"]}'),
        files=[f'sales/videos/{v["file"].replace(".mp4", ".txt")}'], key='video')


# ---------- Substack 文章（README 發文表：一週兩篇，台灣 22:00） ----------
def parse_posts():
    text = (SALES / 'substack' / 'README.md').read_text(encoding='utf-8')
    out = []
    for m in re.finditer(r'^\|\s*(\d+)/(\d+)（.）\s*\|\s*([^|]*?)\s*\|\s*([^|]*?)\s*\|', text, re.M):
        mo, da = int(m[1]), int(m[2])
        d = dt.date(2026 if mo >= 11 else 2027, mo, da)
        f = re.search(r'`(posts/[^`]+)`', m[3])
        if f:
            path = SALES / 'substack' / f[1]
            title = path.read_text(encoding='utf-8').splitlines()[0].lstrip('# ').strip()
            out.append({'date': d, 'file': f'sales/substack/{f[1]}', 'num': int(path.name[:2]), 'title': title,
                        'kind': m[4], 'done': '已發' in m[4]})
        else:
            out.append({'date': d, 'file': None, 'num': None, 'title': '新文章（還沒寫，Claude 先起草）', 'kind': m[4], 'done': False})
    return out


POSTS = parse_posts()
for p in POSTS:
    if p['done'] or p['date'] <= START:
        continue
    if p['file']:
        add(p['date'], '22:00', f'Substack 文章發出：{p["title"]}', '自動', 'Substack',
            note='已用 Schedule 排在台灣 22:00（美東早上 9 點）的話不用做事；發出後看一眼有沒有上線', files=[p['file']], key='post')
    else:
        add(p['date'], '22:00', 'Substack 文章：這篇要新寫（Claude 12/15 前起草）', '你', 'Substack',
            note='一週兩篇先試 4 週，今天看訂閱數和取消訂閱數；取消變多就改回一週一篇', files=['sales/substack/README.md'], key='post')


def notes_week_for(tue):
    """從 tue（週二）開始的 7 則 Notes：[(日期, 內容)]。"""
    out = []
    for i in range(7):
        d = tue + dt.timedelta(days=i)
        n = note_for(d)
        if n and d > NOTES_SCHEDULED_TO:
            out.append((d, n[2]))
    return out


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
        # Substack：下週二、週五的文章（22:00）＋下週二起 7 則 Notes（21:00）
        tue = d + dt.timedelta(days=4)
        nxt_posts = [p for p in POSTS if tue <= p['date'] <= tue + dt.timedelta(days=3) and p['file']]
        nxt_notes = notes_week_for(tue)
        if nxt_posts or nxt_notes:
            parts = []
            for p in nxt_posts:
                parts.append(f'{len(parts) + 1}. 文章 {p["file"]}：貼成新文章，用 Schedule 排在台灣 {md(p["date"])} 22:00。不要直接發布。')
            if nxt_notes:
                parts.append(f'{len(parts) + 1}. Notes：下面 {len(nxt_notes)} 則，各自定時在那一天的台灣 21:00（一天一則）：\n'
                             + '\n'.join(f'{md(nd)}：{t}' for nd, t in nxt_notes))
            what = '、'.join(x for x in (f'文章 {len(nxt_posts)} 篇' if nxt_posts else '', f'Notes {len(nxt_notes)} 則' if nxt_notes else '') if x)
            add(d, '10:47', f'Substack 預排下週（{what}）', '擴充功能', 'Substack',
                prompt=(f'照 {GH}sales/substack/擴充功能發文.md，在 Substack 排下週的內容。內容一字不改；每排好一項回報一行，'
                        '第 1 項排好先停下來給我看時間對不對。遇到驗證就停下來問。\n\n' + '\n\n'.join(parts)),
                files=[p['file'] for p in nxt_posts] + (['sales/substack/notes.md'] if nxt_notes else []), key='substack')
        # 總表：這週五要排哪些
        todo = []
        if week:
            todo.append(f'TikTok {len(week)} 支')
        if nxt_posts or nxt_notes:
            todo.append('Substack ' + what)
        if d >= dt.date(2026, 12, 4):
            todo.append('小紅書 7 篇（README 的稿只排到 12/7，之後的要先請 Claude 寫）')
            if not nxt_notes:
                todo.append('Substack Notes（28 則 12/21 發完，之後的要先請 Claude 寫）')
            if not week:
                todo.append('短影片（已做好的 1/2 發完，之後的要先做）')
            if any(p['file'] is None and tue <= p['date'] <= tue + dt.timedelta(days=3) for p in POSTS):
                todo.append('下週二的 Substack 文章要新寫（Claude 起草）')
        else:
            todo.append('小紅書、Substack Notes 已排到 12/7，這週不用排')
        add(d, '10:27', '排下週的內容（TikTok、小紅書、Substack）', '你', '檢查',
            note='這週要排：' + '；'.join(todo) + '。另外每週 1 篇「代做網站」內容（虛構範例店），TikTok／小紅書／Pinterest 各一',
            files=['sales/videos/發片時程.md', 'sales/xiaohongshu/README.md', 'sales/substack/README.md', 'sales/行銷計畫.md'], key='friday')
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
        add(d, '09:17', '每週一檢討（聯絡、回覆、成交、收入、Care，跟目標的差距）', 'Claude', '檢查',
            prompt=('這是 Polyglot Pages 的每週一檢討，照 sales/80萬計畫.md「每週一檢討」：看聯絡數、回覆數、成交數、收入、Care 訂閱數，'
                    '跟計畫目標差多少；再照 7 件事（價格、留存、每家多收、產能、管道、提早、時間效率）至少提 1 個附估計的建議，'
                    '標成「建議（待使用者決定）」。也看「80 萬之後」的觸發條件有沒有到。\n\n{{summary}}'),
            files=['sales/80萬計畫.md', 'sales/outreach/leads.csv'], key='review', note='按「複製提示」會自動帶入你在後台記的數字')
    d += dt.timedelta(days=1)

# ---------- 開發：已排程的開發信、追問信、表單、IG、LinkedIn ----------
OB = 'sales/outreach/outbox/'
CAP_NOTE = 'Email 暖身上限（24 小時內合計，追問信也算）：11/30 前 15、12/1 起 20、12/8 起 30、12/15 起 40～50'
# Gmail 已排好、會自動寄出的開發信（台灣時間；封數是實際排進 Gmail 的數量）
SENDS = [
    (dt.date(2026, 11, 30), '22:30', '第 7 批紐約＋補寄', 8, ['2026-11-30-batch7.md', '2026-11-30-extra3.md']),
    (dt.date(2026, 12, 1), '01:30', '第 7 批加州＋補寄', 11, ['2026-11-30-batch7.md', '2026-11-30-extra3.md']),
    (dt.date(2026, 12, 2), '01:30', '第 8 批加州', 14, ['2026-12-02-batch8.md']),
    (dt.date(2026, 12, 3), '03:10', '補寄（改寄 Email 的 4 家）', 4, ['2026-12-03-fb4.md']),
    (dt.date(2026, 12, 5), '01:30', '第 9 批加州', 10, ['2026-12-05-batch9.md']),
]
for day, t, label, n, fs in SENDS:
    add(day, t, f'Gmail 自動寄出：{label} {n} 封', '自動', '開發',
        note='已在 Gmail 排好，不用做事。起床後看收件匣：有回信照 sales/outreach/回信範本.md 當天回；有退信告訴 Claude',
        files=[OB + f for f in fs] + ['sales/outreach/回信範本.md'], key='send', emails=n)

# 第 10 批（新行業：會計、保險、移民律師、地產）：12/8 排，12/9 晚上～12/10 凌晨寄
add(dt.date(2026, 12, 8), '09:43', '排第 10 批開發信 12 封（紐約 6、加州＋華盛頓州 6）', '擴充功能', '開發',
    prompt=(f'照 {GH}{OB}2026-12-09-batch10.md，在品牌 Gmail 用「排定傳送時間」排這批 12 封：紐約 6 封從台灣 12/9（三）22:30 起、'
            '加州＋華盛頓州 6 封從台灣 12/10（四）02:00 起，每 5 分鐘一封。標題和內文一字不改，確認信件最下面有簽名的地址。'
            '用元素定位、按之前先截圖；第 1 封排好先停下來給我看；畫面出現「已寄出」立刻停下來告訴我。'),
    files=[OB + '2026-12-09-batch10.md'], key='batch10', note='12/8 起上限 30 封；跟追問信合計不要超過')
for day, t, label, n in ((dt.date(2026, 12, 9), '22:30', '第 10 批紐約', 6), (dt.date(2026, 12, 10), '02:00', '第 10 批加州＋華盛頓州', 6)):
    add(day, t, f'Gmail 自動寄出：{label} {n} 封', '自動', '開發',
        note='12/8 排好的話不用做事。起床後看收件匣：有回信照 sales/outreach/回信範本.md 當天回；有退信告訴 Claude',
        files=[OB + '2026-12-09-batch10.md', 'sales/outreach/回信範本.md'], key='send', emails=n)


# 追問信：2026-12-followups.md 每一組的「台灣 M/D（週）HH:MM …（N 封）」和下一行「> M/D … 排」
def parse_followups():
    text = (SALES / 'outreach' / 'outbox' / '2026-12-followups.md').read_text(encoding='utf-8')
    out = []
    for m in re.finditer(r'^#{2,3} 台灣 (\d+)/(\d+)（.）(\d\d:\d\d)[^\n]*（(\d+) 封）\n> (\d+)/(\d+)', text, re.M):
        send = dt.date(2026, int(m[1]), int(m[2]))
        on = dt.date(2026, int(m[5]), int(m[6]))
        moved = None
        if on == send and m[3] < '09:00':        # 寄出時間在「排」那天早上之前 → 只能前一天排
            moved, on = on, on - dt.timedelta(days=1)
        out.append({'send': send, 'time': m[3], 'n': int(m[4]), 'on': on, 'moved': moved})
    return out


FOLLOWUPS = parse_followups()
by_on = {}
for g in FOLLOWUPS:
    by_on.setdefault(g['on'], []).append(g)
for on, groups in sorted(by_on.items()):
    groups.sort(key=lambda g: (g['send'], g['time']))
    n = sum(g['n'] for g in groups)
    names = '、'.join(f'「台灣 {md(g["send"])}{g["time"]}」那組 {g["n"]} 封' for g in groups)
    when = '、'.join(f'{g["send"].month}/{g["send"].day} {g["time"]}' for g in groups)
    note = '排之前你先看收件匣：已經回信、退信、自動回覆換信箱的不要追。追問只做一次'
    for g in groups:
        if g['moved']:
            note += f'。注意：總表寫「{g["moved"].month}/{g["moved"].day} 早上排」，但這組台灣 {md(g["send"])} {g["time"]} 就要寄，所以放在今天；請跟 Claude 確認'
    add(on, '09:33', f'排追問信 {n} 封（台灣 {when} 寄）', '擴充功能', '開發',
        prompt=(f'照 {GH}{OB}2026-12-followups.md 排追問信：{names}。'
                '先看 Gmail 收件匣，對方已經回信（包括說不用了）、退信、或自動回覆說換信箱的，跳過並告訴我。'
                '在原本那封信的信件串按「回覆」（不要開新信），貼上總表的追問內文，只換店名和網址，用「排定傳送時間」排在那組寫的台灣時間，每 5 分鐘一封。'
                '用元素定位、按之前先截圖；第 1 封排好先停下來給我看；畫面出現「已寄出」立刻停下來告訴我。'),
        files=[OB + '2026-12-followups.md'], key='followup', note=note, emails=n)
DATED_TO = max(list(by_on) + [dt.date(2026, 12, 10)])   # 有確定日期的開發工作到這天

# IG：11/26 被限制後暫停 48 小時，11/28 起照新規則
for day in (dt.date(2026, 11, 28), dt.date(2026, 11, 29)):
    add(day, '10:13', 'IG 私訊：最多 3 則（第一則不放連結）', '你', '開發',
        note='對象：有預覽、沒有 Email、有 IG 的店。每則至少隔 30 分鐘，盡量用手機傳；對方回覆才傳預覽連結。出現傳送失敗或「動作已被封鎖」就停 48 小時，不按重試',
        files=['sales/outreach/README.md', 'sales/outreach/訊息範本.md'], key='ig')
# 聯絡表單：11/30 台灣白天填
add(dt.date(2026, 11, 30), '10:13', '填聯絡表單（第 8 批 1 家；其他有預覽、沒 Email 的店一天 10～15 家以內）', '你', '開發',
    note='Name、Email 照 outbox 寫的填；必填欄位要填假資料（病人姓名、生日）的表單不要送，告訴 Claude。表單不算在 Email 暖身上限裡',
    files=[OB + '2026-12-02-batch8.md', 'sales/outreach/README.md'], key='forms')
# LinkedIn：平日送邀請（11/27 起用本人帳號）
d = dt.date(2026, 11, 30)
while d <= END:
    if d.weekday() < 5:
        add(d, '11:07', 'LinkedIn：送邀請（最多 15 個，不附留言）、看誰接受了', '你', '開發',
            note='接受的人傳第一則訊息（不放連結），7 天後只追一次；大公司的業務員用「介紹夥伴」說法。記在 linkedin.csv。每週合計 ≤100；出現邀請上限或驗證就停一週',
            files=['sales/outreach/LinkedIn.md', 'sales/outreach/linkedin.csv'], key='linkedin')
    d += dt.timedelta(days=1)
# 有確定日期的資料用完之後：平日一件通用的，照暖身上限寫
d = DATED_TO + dt.timedelta(days=1)
while d <= END:
    if d.weekday() < 5:
        cap = '≤30 封' if d < dt.date(2026, 12, 15) else '40～50 封'
        add(d, '13:07', f'排今天的開發信＋追問信（24 小時內合計 {cap}）', '你', '開發',
            note=('追問信約佔一半，新開發信大約是上限的一半；前提是沒有 Gmail 警告、退信率 <2%。表單（一天 10～15）、IG（一天 ≤3）另計。'
                  '排追問前先看收件匣；寄完把數字加到「開發」頁'),
            files=['sales/outreach/README.md', 'sales/outreach/leads.csv'], key='outreach')
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

# ---------- 開發：Instagram 帳號 ----------
add(dt.date(2026, 11, 24), '09:13', '開 Instagram 私訊專用帳號', '你', '開發',
    note='只用來私訊店家、不發文；放 3 張 Pinterest 圖當門面。新帳號第一週一天最多 5 則私訊',
    files=['sales/帳號註冊.md', 'sales/outreach/README.md', 'sales/brand/avatar.png'], key='ig')
# ---------- 之後的上架與檢查 ----------
add(dt.date(2026, 12, 7), '10:07', '寄信給買過的人（附舊客優惠碼）', '你', '上架',
    note='Gumroad → Emails，介紹 Motion 系列；營運流程第 2～3 週', files=['sales/營運流程.md'], key='buyers')
add(dt.date(2026, 11, 30), '11:15', '上架 Website Care 維護月費（$49／月）', '擴充功能', '上架',
    prompt=(f'照 {GH}sales/擴充功能上架.md 的規則，把 sales/Gumroad上架步驟.md 第 12 節「Website Care」建成 Membership 商品草稿：'
            'Name、URL website-care、單一方案 $49/month、Description 一字不改。不要按 Publish。'),
    files=['sales/Gumroad上架步驟.md', 'sales/交付流程.md'], key='care',
    note='你看過再按 Publish。12/1 起每個代製客人交件時都推（第 1 個月免費）')
add(dt.date(2026, 12, 23), '11:15', 'Commission 可以用了：把訂金商品改回 Commission', '擴充功能', '上架',
    prompt=('Gumroad 帳號滿 30 天，Commission 類型應該可以用了。照 sales/Gumroad上架步驟.md 第 3 節與第 8 節：'
            '先確認新增商品時有沒有 Commission 類型，沒有就停下來告訴我。有的話把「網站客製服務」和「三語店家網站代製」各建一個 Commission 草稿'
            '（50% 訂金），內容照原本的商品。不要刪除或下架舊的訂金商品，我確認後自己處理。'),
    files=['sales/Gumroad上架步驟.md', 'sales/交付流程.md'], key='commission',
    note='手上有進行中的案子時先不要換（outreach/README.md）。新的發布後，把舊的訂金商品設成不公開，交付流程的連結也要換')
add(dt.date(2026, 12, 9), '14:13', '12/9 數據檢討（A/B 只檢查資料有沒有記錯，不用來定價）', 'Claude', '檢查',
    prompt=('這是 Polyglot Pages 12/9 的數據檢討，照 sales/80萬計畫.md「11/27 檢討與決定」和 sales/行銷計畫.md 最後一節：'
            '1. sales/outreach/ab-test.csv 的 $299／$499 只檢查資料有沒有記錯，不用來定價（樣本太少）；定價看回信內容和實際成交。'
            '2. 各平台（TikTok、YouTube、小紅書、Substack、Pinterest）哪個有效：有效的之後加量，沒效的降頻；小紅書看每篇收藏、私訊數，決定要不要改成 8:2。'
            '3. 列出要我決定的事，標成「建議（待使用者決定）」。\n\n{{summary}}'),
    files=['sales/80萬計畫.md', 'sales/行銷計畫.md', 'sales/outreach/ab-test.csv'], key='data', note='按「複製提示」會自動帶入你在後台記的數字')
add(dt.date(2026, 12, 12), '14:13', '提早警訊：11/23～12/5 寄出那批的回覆率有沒有到 1%', 'Claude', '檢查',
    prompt=('照 sales/80萬計畫.md「提早警訊」：算 sales/outreach/leads.csv 裡 11/23～12/5 寄出那批的回覆率（有 reply_date 的 ÷ 寄出數）。'
            '低於 1% 就不用等 12/23，先提出開發信開頭的新寫法給我看（先講要改什麼，我同意再改）。\n\n{{summary}}'),
    files=['sales/80萬計畫.md', 'sales/outreach/leads.csv', 'sales/outreach/訊息範本.md'], key='warning')
add(dt.date(2026, 12, 23), '14:43', '12/23 關卡：有沒有至少 1 家付訂金', 'Claude', '檢查',
    prompt=('這是 Polyglot Pages 的 12/23 關卡（sales/80萬計畫.md 階段 1）。目標：累積聯絡 300 家、成交 3 家；關卡：至少 1 家付訂金，'
            '0 家就要改開發信寫法或價格。請看：聯絡數、回覆數、成交數、收入跟目標的差距；西語市場要不要做（最快 2 月）；'
            '起號 30 天各平台的數字（哪個管道帶來最多瀏覽和銷售）。給我下個月最該做的 3 件事，標成「建議（待使用者決定）」。\n\n{{summary}}'),
    files=['sales/80萬計畫.md', 'sales/行銷計畫.md', 'sales/outreach/leads.csv'], key='gate', note='按「複製提示」會自動帶入你在後台記的數字')
for day, label in ((dt.date(2027, 1, 22), '1 月'), (dt.date(2027, 2, 21), '2 月')):
    add(day, '14:43', f'成長檢查（{label}；階段 2 關卡：每月收入 ≥ $2,500）', 'Claude', '檢查',
        prompt=(f'這是 Polyglot Pages {label}的成長檢查。照 sales/80萬計畫.md 階段 2（每月成交 5～7 家、Care 開始累積；關卡：每月收入 ≥ $2,500）看：'
                '哪個管道帶來最多回覆和成交、開發信回覆率要怎麼改、哪幾款模板瀏覽多但賣不好，給我下個月最該做的 3 件事。\n\n{{summary}}'),
        files=['sales/80萬計畫.md', 'sales/營運流程.md'], key='growth', note='按「複製提示」會自動帶入你在後台記的數字')

items.sort(key=lambda x: (x['date'], x['time'], x['id']))
ids = [x['id'] for x in items]
assert len(ids) == len(set(ids)), 'id 重複'

# ---------- 重要日期 ----------
LAST_VIDEO = max(VIDEOS, key=lambda v: v['date'])
NOTES_END = NOTES_DAY1 + dt.timedelta(days=len(NOTES) - 1)
MILESTONES = [
    ('2026-11-24', '第 1 支短影片、第 1 則 Substack Note'),
    ('2026-11-24', 'Gumroad 上架 10 款（到 19/39）'),
    ('2026-11-25', 'Gumroad 上架 10 款（到 29/39）'),
    ('2026-11-26', 'Gumroad 39 款全部上架；Pinterest 預排開始每天自動發'),
    ('2026-11-27', 'Substack 改成一週兩篇（週二、週五 22:00）'),
    ('2026-11-28', 'IG 私訊照新規則重新開始（一天最多 3 則、第一則不放連結）'),
    ('2026-11-30', 'Website Care 維護月費上架（$49／月），12/1 開始賣'),
    ('2026-11-30', '感恩節後第一批開發信自動寄出（到 12/5 共 47 封）'),
    ('2026-12-01', 'Email 暖身上限 20 封／天（含追問）'),
    ('2026-12-03', '日文版短影片（19:00 發）'),
    ('2026-12-07', '小紅書每天 1 篇、Substack Notes 已排到今天（之後每週五排下一週）'),
    ('2026-12-08', 'Email 暖身上限 30 封／天；排第 10 批（新行業 12 封）'),
    ('2026-12-09', '數據檢討（A/B 只檢查資料，不用來定價）'),
    ('2026-12-12', '提早警訊：回覆率 <1% 就先改開發信開頭'),
    ('2026-12-15', 'Email 暖身上限 40～50 封／天（沒有 Gmail 警告、退信率 <2% 才加）'),
    (d2s(NOTES_END), f'Substack Notes {len(NOTES)} 則發完（之後請 Claude 寫下一批）'),
    ('2026-12-22', 'Substack 一週兩篇試滿 4 週：看訂閱和取消數，決定要不要改回一篇'),
    ('2026-12-23', '關卡：至少 1 家付訂金（0 家就改開發信或價格）；決定西語市場'),
    ('2026-12-23', 'Gumroad 滿 30 天：可以改用 Commission'),
    (d2s(LAST_VIDEO['date']), f'最後 1 支已做好的短影片（{LAST_VIDEO["file"]}）'),
    ('2027-01-22', '1 月成長檢查（階段 2：每月收入 ≥ $2,500）'),
    ('2027-02-21', '2 月成長檢查'),
    ('2027-04-01', '關卡：累計收入 ≥ $10,000'),
    ('2027-07-01', '關卡：累計收入 ≥ $20,000'),
    ('2027-07-31', '目標：淨收入 NT$800,000'),
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

# ---------- 開發：只取數量（狀態、管道），不取任何店名或聯絡資料 ----------
CONTACTED = ('sent', 'followup', 'replied', 'later', 'won', 'lost', 'optout')
now = dt.datetime.now(TPE)
us_today = (now - dt.timedelta(hours=16)).date().isoformat()     # leads.csv 的日期是美國日期（用太平洋時間算）
L = {'total': 0, 'sent': 0, 'scheduled': 0, 'replied': 0, 'won': 0, 'lost': 0, 'hold': 0, 'todo': 0,
     'channel': {'email': 0, 'form': 0, 'instagram': 0, 'linkedin': 0}}
with open(SALES / 'outreach' / 'leads.csv', encoding='utf-8') as f:
    for r in csv.DictReader(f):
        s_ = (r.get('status') or '').strip()
        L['total'] += 1
        if s_ in CONTACTED:
            # 已在 Gmail 排程、還沒到寄出日的，leads.csv 也先記成 sent：分開算
            if s_ == 'sent' and (r.get('sent_date') or '') > us_today:
                L['scheduled'] += 1
                continue
            L['sent'] += 1
            ch = (r.get('channel') or '').strip()
            if ch in L['channel']:
                L['channel'][ch] += 1
            if s_ in ('replied', 'later', 'won') or (r.get('reply_date') or '').strip():
                L['replied'] += 1
            if s_ == 'won':
                L['won'] += 1
            if s_ in ('lost', 'optout'):
                L['lost'] += 1
        elif s_ in ('hold', 'skip'):
            L['hold'] += 1
        else:                                   # new、demo：還沒聯絡
            L['todo'] += 1
LI = {'invited': 0, 'accepted': 0}
li_csv = SALES / 'outreach' / 'linkedin.csv'
if li_csv.exists():
    with open(li_csv, encoding='utf-8') as f:
        for r in csv.DictReader(f):
            LI['invited'] += 1
            if (r.get('status') or '').strip() != 'invited':
                LI['accepted'] += 1
L['channel']['linkedin'] += LI['invited']       # LinkedIn 以送出的邀請數計
L['linkedin'] = LI
L['asOf'] = us_today
counts = {'sent': L['sent'], 'replied': L['replied'], 'demo': 0, 'won': L['won'], 'lost': L['lost']}

data = {
    'generated': now.strftime('%Y-%m-%d %H:%M'),
    'tz': 'Asia/Taipei',
    'range': [d2s(START), d2s(END)],
    'gumroad': {'before': GUMROAD_BEFORE, 'beforeDate': '2026-11-23', 'total': GUMROAD_TOTAL},
    'pinsPlan': pins_plan,
    'videos': [{'date': d2s(v['date']), 'time': v['time'], 'file': v['file'], 'what': v['what']} for v in VIDEOS],
    'plan': PLAN,
    'outreachSeed': counts,
    'leads': L,
    'milestones': MILESTONES,
    'items': items,
}

# 隱私檢查：不能出現 Email、Google Drive 連結、權杖
blob = json.dumps(data, ensure_ascii=False)
for pat in (r'[\w.+-]+@[\w-]+\.[\w.]+', r'drive\.google|docs\.google', r'gh[pousr]_[A-Za-z0-9]{20,}|github_pat_'):
    m = re.search(pat, blob)
    assert not m, f'schedule.json 不能包含：{m[0]}'
# 開發名單的店名、人名也不能出現（只放數量）
for fname, col in (('leads.csv', 'business'), ('linkedin.csv', 'name')):
    fp = SALES / 'outreach' / fname
    if fp.exists():
        with open(fp, encoding='utf-8') as f:
            for r in csv.DictReader(f):
                for part in re.split(r'\s*/\s*', (r.get(col) or '').strip()):
                    assert len(part) < 6 or part not in blob, f'schedule.json 不能包含名單裡的名稱：{part}'

OUT.parent.mkdir(exist_ok=True)
OUT.write_text(json.dumps(data, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print(f'✓ {OUT.relative_to(ROOT)}：{len(items)} 件事，{len(MILESTONES)} 個重要日期，追問 {sum(g["n"] for g in FOLLOWUPS)} 封／{len(FOLLOWUPS)} 組，'
      f'名單 {L["total"]} 家（已聯絡 {L["sent"]}、已排程 {L["scheduled"]}），{OUT.stat().st_size // 1024} KB')
