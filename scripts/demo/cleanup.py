#!/usr/bin/env python3
"""Delete preview sites that should no longer be online.

Usage: python3 scripts/demo/cleanup.py [--dry-run] [--csv sales/outreach/leads.csv] [--days 60]

A folder demos/<slug>/ is deleted when its lead
  - has status optout or lost, or
  - is older than --days days (default 60), counted from the lead's sent_date (or the demo's
    creation date if it was never sent), and the status is not won or replied.
    Leads with status later or followup are kept until 14 days after their followup_date.
Folders whose lead is no longer in the CSV are treated the same way (age only).
The demo's creation date and lead id come from the stamp make-demo.py writes into
demos/<slug>/index.html; older folders fall back to the folder's modification time.
After deleting, the lead's demo_url is cleared in the CSV (the status is kept).
Rebuild the site afterwards (bash scripts/build-site.sh) so the preview disappears from GitHub Pages too.
"""
import argparse, csv, datetime, pathlib, re, shutil, sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
DEMOS = ROOT / 'demos'
REMOVE = {'optout', 'lost'}
KEEP = {'won', 'replied'}
WAIT = {'later', 'followup'}   # kept until followup_date + GRACE days
GRACE = 14


def stamp(folder):
    idx = folder / 'index.html'
    text = idx.read_text(encoding='utf-8', errors='replace') if idx.exists() else ''
    m = re.search(r'<!-- polyglot-demo lead=(\S+) created=(\d{4}-\d{2}-\d{2}) -->', text)
    if m:
        return m.group(1), datetime.date.fromisoformat(m.group(2))
    return None, datetime.date.fromtimestamp(folder.stat().st_mtime)


def main():
    ap = argparse.ArgumentParser(description='Delete preview sites for opted-out, lost or stale leads.')
    ap.add_argument('--dry-run', action='store_true', help='only list what would be deleted')
    ap.add_argument('--csv', default=str(ROOT / 'sales/outreach/leads.csv'))
    ap.add_argument('--days', type=int, default=60)
    ap.add_argument('--demos', default=str(DEMOS), help='demo folder (default: demos/)')
    a = ap.parse_args()

    with open(a.csv, newline='', encoding='utf-8') as f:
        r = csv.DictReader(f)
        fields, rows = r.fieldnames, list(r)
    by_id = {(x.get('id') or '').strip(): x for x in rows}
    by_url = {(x.get('demo_url') or '').strip().strip('/').split('/')[-1]: x for x in rows if x.get('demo_url')}

    demos = pathlib.Path(a.demos)
    if not demos.is_dir():
        print('沒有 demos/ 資料夾，不用清。')
        return
    today = datetime.date.today()
    removed, kept = [], 0
    for folder in sorted(p for p in demos.iterdir() if p.is_dir()):
        lead_id, created = stamp(folder)
        row = by_id.get(lead_id) if lead_id else None
        row = row or by_url.get(folder.name)
        status = (row.get('status') or '').strip().lower() if row else ''
        def day(v):
            try:
                return datetime.date.fromisoformat((v or '').strip())
            except ValueError:
                return None
        sent = day(row.get('sent_date')) if row else None
        fup = day(row.get('followup_date')) if row else None
        age = (today - (sent or created)).days
        reason = None
        if status in REMOVE:
            reason = f'status {status}'
        elif status in KEEP:
            pass
        elif status in WAIT and fup and today <= fup + datetime.timedelta(days=GRACE):
            pass
        elif age > a.days:
            reason = f'{"寄出" if sent else "做好"} {age} 天，status {status or "（名單裡找不到）"}'
        if not reason:
            kept += 1
            continue
        removed.append(folder.name)
        print(('[dry-run] 會刪除 ' if a.dry_run else '刪除 ') + f'demos/{folder.name}/（{reason}）')
        if not a.dry_run:
            shutil.rmtree(folder)
            if row is not None:
                row['demo_url'] = ''
    if removed and not a.dry_run:
        with open(a.csv, 'w', newline='', encoding='utf-8') as f:
            w = csv.DictWriter(f, fieldnames=fields, lineterminator='\n')
            w.writeheader()
            w.writerows(rows)
        print(f'已清空 {len(removed)} 筆的 demo_url：{a.csv}')
    print(f'完成：{"會刪除" if a.dry_run else "刪除"} {len(removed)} 個，保留 {kept} 個。' + ('記得重新建置網站：bash scripts/build-site.sh' if removed and not a.dry_run else ''))


if __name__ == '__main__':
    sys.exit(main())
