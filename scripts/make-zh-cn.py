"""從繁體中文版自動產生簡體中文版：templates/<slug>/ → templates/zh-CN/<slug>/
用法：python3 scripts/make-zh-cn.py [slug ...]（需要 pip install opencc-python-reimplemented）
"""
import sys, re, pathlib, opencc
root = pathlib.Path(__file__).resolve().parent.parent / 'templates'
conv = opencc.OpenCC('tw2sp')   # 台灣正體 → 大陸簡體，含常用詞轉換
skip = {'en', 'zh-CN', '_docs', 'motion'}
slugs = sys.argv[1:] or sorted([p.name for p in root.iterdir() if p.is_dir() and p.name not in skip and (p / 'index.html').exists()]
                               + ['motion/' + p.name for p in (root / 'motion').iterdir() if (p / 'index.html').exists()])
FONT = [('Noto+Sans+TC', 'Noto+Sans+SC'), ('Noto+Serif+TC', 'Noto+Serif+SC'), ('Noto Sans TC', 'Noto Sans SC'),
        ('Noto Serif TC', 'Noto Serif SC'), ('PingFang TC', 'PingFang SC'), ('Microsoft JhengHei', 'Microsoft YaHei'),
        ('lang="zh-Hant"', 'lang="zh-Hans"'), ('zh_TW', 'zh_CN'), ('"zh-TW"', '"zh-CN"'), ('"zh-Hant"', '"zh-Hans"')]
for slug in slugs:
    src = (root / slug / 'index.html').read_text(encoding='utf-8')
    out = conv.convert(src)
    for a, b in FONT: out = out.replace(a, b)
    dst = root / 'zh-CN' / slug / 'index.html'
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(out, encoding='utf-8')
    print('✓', slug)
