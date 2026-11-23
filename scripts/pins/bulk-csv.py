#!/usr/bin/env python3
"""產生 Pinterest「批次建立 Pin」用的 CSV（每個檔案最多 200 列）。
用法：python3 scripts/pins/bulk-csv.py 2026-11-26 [每天張數，預設 15]
圖片網址指向 GitHub Pages 上的 /pins/，所以要先合併到 main、部署完成後再上傳 CSV。
發布時間分散在台灣時間 09:00～23:00（換成 UTC 寫進 CSV）。"""
import csv, sys, datetime, pathlib
root = pathlib.Path(__file__).resolve().parent.parent.parent
start = datetime.date.fromisoformat(sys.argv[1]); per = int(sys.argv[2]) if len(sys.argv) > 2 else 15
BASE = 'https://a0955072107-bit.github.io/-/pins/'
rows = []
for name in ('pins.csv', 'pins-2.csv'):
    rows += list(csv.DictReader(open(root / 'sales/pins' / name, encoding='utf-8-sig')))
out = []
for i, r in enumerate(rows):
    day, k = divmod(i, per)
    hour_tw = 9 + round(k * 14 / max(per - 1, 1))          # 09:00～23:00 台灣
    t = datetime.datetime.combine(start + datetime.timedelta(days=day), datetime.time(hour_tw)) - datetime.timedelta(hours=8)
    tags = [w.strip() for w in r['keywords'].split(',')][:3]
    desc = r['description'] + '\n\n' + ' '.join('#' + w.replace(' ', '') for w in tags)
    out.append({'Title': r['title'][:100], 'Media URL': BASE + r['file'], 'Pinterest board': r['board'],
                'Thumbnail': '', 'Description': desc[:500], 'Link': r['link'],
                'Publish date': t.strftime('%Y-%m-%dT%H:%M:%S'), 'Keywords': r['keywords']})
dst = root / 'sales/pins/pinterest-bulk.csv'
with open(dst, 'w', encoding='utf-8', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(out[0].keys())); w.writeheader(); w.writerows(out)
last = out[-1]['Publish date']
print(f'✓ {dst.name}：{len(out)} 張，{start} 起每天 {per} 張，最後一張 {last} UTC')
print('需要的看板：', sorted({r["Pinterest board"] for r in out}))
