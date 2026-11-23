#!/usr/bin/env bash
# 建置 GitHub Pages 線上 Demo 到 _site/，結構和買家拿到的 zip 一樣：
#   _site/templates/<款式>/{en,zh-TW,zh-CN}/index.html，加上語言入口與三語展示頁
#   用法：bash scripts/build-site.sh
set -euo pipefail
cd "$(dirname "$0")/.."
rm -rf _site && mkdir -p _site/templates
cp index.html _site/
python3 - <<'PY'
import pathlib, re, shutil, subprocess
T = pathlib.Path('templates'); S = pathlib.Path('_site/templates')
skip = {'en', 'zh-CN', 'ja', 'es', '_docs', 'motion', 'luxe'}
slugs = [p.name for p in T.iterdir() if p.is_dir() and p.name not in skip and (p / 'index.html').exists()]
for group in ('motion', 'luxe'):
    if (T / group).exists():
        slugs += [f'{group}/{p.name}' for p in (T / group).iterdir() if (p / 'index.html').exists()]
for s in slugs:
    for lang, src in (('zh-TW', T / s), ('en', T / 'en' / s), ('zh-CN', T / 'zh-CN' / s), ('ja', T / 'ja' / s), ('es', T / 'es' / s)):
        f = src / 'index.html'
        if f.exists():
            d = S / s / lang; d.mkdir(parents=True, exist_ok=True); shutil.copy(f, d / 'index.html')
    subprocess.run(['python3', 'scripts/lang-index.py', str(S / s)], check=True)
# 展示頁：連結改成新結構
def fix(text, prefix, lang):
    return re.sub(r"href: '([a-z0-9/-]+)/'", lambda m: f"href: '{prefix}{m.group(1)}/{lang}/'", text)
zh = (T / 'index.html').read_text(encoding='utf-8')
(S / 'index.html').write_text(fix(zh, '', 'zh-TW'), encoding='utf-8')
en = (T / 'en' / 'index.html').read_text(encoding='utf-8')
(S / 'en').mkdir(exist_ok=True); (S / 'en' / 'index.html').write_text(fix(en, '../', 'en'), encoding='utf-8')
try:
    import opencc
    cn = opencc.OpenCC('tw2sp').convert(zh).replace('lang="zh-Hant"', 'lang="zh-Hans"').replace('Noto+Sans+TC', 'Noto+Sans+SC').replace('"Noto Sans TC"', '"Noto Sans SC"')
    cn = cn.replace('href="en/"', 'href="../en/"')
    (S / 'zh-CN').mkdir(exist_ok=True); (S / 'zh-CN' / 'index.html').write_text(fix(cn, '../', 'zh-CN'), encoding='utf-8')
except ImportError:
    print('（沒有安裝 opencc，略過簡體展示頁）')
print('✓', len(slugs), '款')
PY
# 主動開發用的示範站：demos/<店> → _site/demo/<店>/（每頁都有 noindex，robots.txt 也擋掉 /demo/）
if [ -d demos ]; then
  mkdir -p _site/demo
  cp -R demos/. _site/demo/
  # 舊訊息裡有 /demos/ 的連結（11/23 寫錯），兩個路徑都放，避免連結失效
  mkdir -p _site/demos && cp -R demos/. _site/demos/
  echo "✓ 示範站 $(find demos -mindepth 1 -maxdepth 1 -type d | wc -l | tr -d ' ') 個 → _site/demo/"
fi
# Pinterest 批次上傳用的圖片：sales/pins/*.jpg → _site/pins/（Pinterest 依網址抓圖）
if [ -d sales/pins ]; then
  mkdir -p _site/pins && cp sales/pins/*.jpg _site/pins/
  echo "✓ Pinterest 圖 $(ls sales/pins/*.jpg | wc -l | tr -d ' ') 張 → _site/pins/"
fi
# Gumroad 封面（公開的宣傳圖，給擴充功能從網址抓）：sales/covers/en → _site/covers/
if [ -d sales/covers/en ]; then
  mkdir -p _site/covers && cp sales/covers/en/*.png _site/covers/
  echo "✓ 封面 $(ls sales/covers/en/*.png | wc -l | tr -d ' ') 張 → _site/covers/"
fi
printf 'User-agent: *\nDisallow: /demo/\nDisallow: /demos/\n' > _site/robots.txt
echo "✓ _site/ 建置完成"
