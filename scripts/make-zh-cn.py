"""從繁體中文版自動產生簡體中文版：templates/<slug>/ → templates/zh-CN/<slug>/
用法：python3 scripts/make-zh-cn.py [slug ...]（需要 pip install opencc-python-reimplemented）
"""
import sys, re, pathlib, opencc
root = pathlib.Path(__file__).resolve().parent.parent / 'templates'
conv = opencc.OpenCC('tw2sp')   # 台灣正體 → 大陸簡體，含常用詞轉換
skip = {'en', 'zh-CN', 'ja', 'es', '_docs', 'motion', 'luxe'}
slugs = sys.argv[1:] or sorted([p.name for p in root.iterdir() if p.is_dir() and p.name not in skip and (p / 'index.html').exists()]
                               + ['motion/' + p.name for p in (root / 'motion').iterdir() if (p / 'index.html').exists()])
FONT = [('Noto+Sans+TC', 'Noto+Sans+SC'), ('Noto+Serif+TC', 'Noto+Serif+SC'), ('Noto Sans TC', 'Noto Sans SC'),
        ('Noto Serif TC', 'Noto Serif SC'), ('PingFang TC', 'PingFang SC'), ('Microsoft JhengHei', 'Microsoft YaHei'),
        ('内文本型', '内文字体'),
        ('Songti TC', 'Songti SC'), ('构图标意', '构图示意'),
        ('接口文本', '界面文字'), ('标示今天字段', '标示今天栏位'), ('窗櫺', '窗棂'),
        ('方程序', '方程式'), ('仿真考', '模拟考'), ('萤光笔', '荧光笔'), ('左右卷动', '左右滑动'), ('可复选', '可多选'), ('数据只用来', '资料只用来'),  # opencc 會把「內文字型」斷成「内文本型」
        ('zh_TW', 'zh_CN'), ('"inLanguage": "zh-TW"', '"inLanguage": "zh-CN"'), ('"inLanguage":"zh-TW"', '"inLanguage":"zh-CN"'),
        ('"inLanguage": "zh-Hant"', '"inLanguage": "zh-Hans"'), ('"inLanguage":"zh-Hant"', '"inLanguage":"zh-Hans"')]

def fix_lang(html):
    # 只改 <html lang>，語言切換裡「繁」的 hreflang／lang 保持 zh-Hant
    html = re.sub(r'<html([^>]*?)lang="zh-Hant"', r'<html\1lang="zh-Hans"', html, count=1)
    # 「目前語言」標記從 繁 移到 简
    def tag(m):
        t = m.group(0)
        if 'href="../zh-TW/"' in t:
            t = re.sub(r'\s+aria-current="page"', '', t)
        elif 'href="../zh-CN/"' in t and 'aria-current' not in t:
            t = t[:-1] + ' aria-current="page">'
        return t
    html = re.sub(r'<a\b[^>]*>', tag, html)
    # 頁首語言下拉：目前語言顯示「简」；「繁體中文」這個語言名稱保持繁體
    html = html.replace('<summary lang="zh-Hant">繁</summary>', '<summary lang="zh-Hans">简</summary>')
    html = re.sub(r'(hreflang="zh-Hant" lang="zh-Hant"[^>]*>)繁体中文<', r'\1繁體中文<', html)
    html = re.sub(r'(hreflang="ja" lang="ja"[^>]*>)日本语<', r'\1日本語<', html)
    return html
for slug in slugs:
    src = (root / slug / 'index.html').read_text(encoding='utf-8')
    out = conv.convert(src)
    for a, b in FONT: out = out.replace(a, b)
    out = fix_lang(out)
    dst = root / 'zh-CN' / slug / 'index.html'
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(out, encoding='utf-8')
    print('✓', slug)
