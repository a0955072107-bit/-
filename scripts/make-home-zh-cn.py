#!/usr/bin/env python3
"""官網簡體版：從 site/zh-TW/index.html 產生 site/zh-CN/index.html。
用法：python3 scripts/make-home-zh-cn.py（需要 pip install opencc-python-reimplemented）
改了繁體版之後跑一次，產生的檔案要一起 commit（建置時不會自動轉）。
標了 lang="zh-Hant" 的元素（手機示範的繁體畫面、語言選單的「繁體中文」）保持繁體。
"""
import pathlib, re, urllib.parse
import opencc

ROOT = pathlib.Path(__file__).resolve().parent.parent / 'site'
BASE = 'https://a0955072107-bit.github.io/-/'
conv = opencc.OpenCC('tw2sp')

src = (ROOT / 'zh-TW' / 'index.html').read_text(encoding='utf-8')

# 1. 先把要保持繁體的元素換成記號
keep = []
def stash(m):
    keep.append(m.group(0))
    return f'@@KEEP{len(keep) - 1}@@'
src = re.sub(r'<(?!html)(\w+)\b[^>]*\blang="zh-Hant"[^>]*>.*?</\1>', stash, src, flags=re.S)
# mailto 主旨是網址編碼的中文，先解開再轉
src = re.sub(r'subject=([^"]+)', lambda m: 'subject=' + urllib.parse.quote(conv.convert(urllib.parse.unquote(m.group(1)))), src)

out = conv.convert(src)
for i, k in enumerate(keep):
    out = out.replace(f'@@KEEP{i}@@', k)

# 2. 大陸用語
# OpenCC 會把「資料」轉成「数据」、「文字」轉成「文本」，這裡改回比較自然的說法
WORDS = [('网域', '域名'), ('信箱', '邮箱'), ('专案', '项目'), ('商家数据', '商家资料'), ('银行数据', '银行信息'),
         ('商家文件', '商家资料'), ('文本', '文字'), ('帐号', '账号'), ('工作天', '工作日'), ('范例', '示例'),
         ('「', '“'), ('」', '”')]
for a, b in WORDS:
    out = out.replace(a, b)

# 3. 語言、網址、字型
out = out.replace('<html lang="zh-Hant">', '<html lang="zh-Hans">', 1)
out = out.replace(f'href="{BASE}zh-TW/">\n<meta', f'href="{BASE}zh-CN/">\n<meta', 1)  # canonical
out = out.replace(f'<meta property="og:url" content="{BASE}zh-TW/">', f'<meta property="og:url" content="{BASE}zh-CN/">')
out = out.replace('img/dental-zh-TW.webp', 'img/dental-zh-CN.webp')
out = re.sub(r'src="\.\./img/(\w+)-zh-TW\.webp"', r'src="../img/\1-zh-CN.webp"', out)
out = re.sub(r'href="\.\./templates/(\w+)/zh-TW/"><img', r'href="../templates/\1/zh-CN/"><img', out)
out = out.replace('href="../templates/">', 'href="../templates/zh-CN/">')
# 範例卡片的語言連結：简体放第一個
out = re.sub(r'<p class="langs">(<a [^>]*>繁體</a>)(<a [^>]*>English</a>)(<a [^>]*>简体</a>)</p>', r'<p class="langs">\3\1\2</p>', out)
# 字型：標題用思源宋體簡體，手機示範的繁體字只下載用到的字
tc_chars = ''.join(sorted(set(c for c in '巷子裡的好日子食堂')))
out = out.replace('family=Noto+Serif+TC:wght@600&display=swap" rel="stylesheet">', 'family=Noto+Serif+SC:wght@600&display=swap" rel="stylesheet">')
out = re.sub(r'family=Noto\+Serif\+SC:wght@600&display=swap&text=[^"]+', 'family=Noto+Serif+TC:wght@600&display=swap&text=' + urllib.parse.quote(tc_chars), out)
out = out.replace('<!-- The phone demo shows Simplified Chinese too: only those characters are downloaded -->', '<!-- The phone demo shows Traditional Chinese too: only those characters are downloaded -->')
out = out.replace('--font-display: "Fraunces", "Noto Serif TC", "Noto Serif SC"', '--font-display: "Fraunces", "Noto Serif SC", "Noto Serif TC"')
out = out.replace('h1, h2, h3 { font-family: var(--font-serif-tc); }', 'h1, h2, h3 { font-family: var(--font-serif-sc); }')
out = out.replace('"PingFang TC", "Noto Sans TC", "Microsoft JhengHei"', '"PingFang SC", "Noto Sans SC", "Microsoft YaHei"')
out = out.replace('aria-label="繁体中文"', 'aria-label="繁體中文"')
# 語言選單：目前語言改成简
out = out.replace('<summary lang="zh-Hant">繁</summary>', '<summary lang="zh-Hans">简</summary>')
out = out.replace(' aria-current="page">繁體中文</a>', '>繁體中文</a>')
out = out.replace('<a href="./" hreflang="zh-Hant"', '<a href="../zh-TW/" hreflang="zh-Hant"')
out = out.replace('<a href="../zh-CN/" hreflang="zh-Hans" lang="zh-Hans">简体中文</a>', '<a href="./" hreflang="zh-Hans" lang="zh-Hans" aria-current="page">简体中文</a>')
# 手機示範一開始顯示简体
out = out.replace('value="tw" checked', 'value="tw"').replace('value="cn" aria-label', 'value="cn" checked aria-label')

assert 'zh-TW/"><img' not in out
dst = ROOT / 'zh-CN' / 'index.html'
dst.parent.mkdir(exist_ok=True)
dst.write_text(out, encoding='utf-8')
print('✓', dst)
