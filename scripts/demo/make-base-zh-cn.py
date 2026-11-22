#!/usr/bin/env python3
"""示範站底稿：從繁體版產生簡體版 scripts/demo/base/<slug>/zh-TW/ → zh-CN/
用法：python3 scripts/demo/make-base-zh-cn.py [slug ...]（需要 pip install opencc-python-reimplemented）
和 scripts/make-zh-cn.py 一樣用 OpenCC tw2sp，並套用同樣的字型與語言標記修正。
產生後請打開 zh-CN 版用眼睛看一次（尤其是 tw2sp 的詞彙轉換）。
"""
import pathlib, re, sys
import opencc

BASE = pathlib.Path(__file__).resolve().parent / 'base'
conv = opencc.OpenCC('tw2sp')
FONT = [('Noto+Sans+TC', 'Noto+Sans+SC'), ('Noto+Serif+TC', 'Noto+Serif+SC'), ('Noto Sans TC', 'Noto Sans SC'),
        ('Noto Serif TC', 'Noto Serif SC'), ('PingFang TC', 'PingFang SC'), ('Microsoft JhengHei', 'Microsoft YaHei'),
        ('Songti TC', 'Songti SC'), ('zh_TW', 'zh_CN'), ("toLocaleDateString('zh-TW'", "toLocaleDateString('zh-CN'")]
# tw2sp 轉完之後，美國華人簡體用語的微調（左：tw2sp 的結果，右：想要的寫法）
WORDS = [('过敏纪录', '过敏记录'), ('范例文本', '示例文字'), ('范例', '示例'), ('查找给付范围', '查询保险覆盖范围'),
         ('有给付针灸', '涵盖针灸'), ('帮您查找', '帮您查询'), ('俐落', '利落')]


def fix_lang(html):
    # 只改 <html lang>，語言切換裡「繁」的 hreflang／lang 保持 zh-Hant
    html = re.sub(r'<html([^>]*?)lang="zh-Hant"', r'<html\1lang="zh-Hans"', html, count=1)

    def tag(m):
        t = m.group(0)
        if 'href="../zh-TW/"' in t:
            t = re.sub(r'\s+aria-current="page"', '', t)
        elif 'href="../zh-CN/"' in t and 'aria-current' not in t:
            t = t[:-1] + ' aria-current="page">'
        return t
    html = re.sub(r'<a\b[^>]*>', tag, html)
    html = html.replace('<summary lang="zh-Hant">繁</summary>', '<summary lang="zh-Hans">简</summary>')
    html = re.sub(r'(hreflang="zh-Hant" lang="zh-Hant"[^>]*>)繁体中文<', r'\1繁體中文<', html)
    return html


def convert(html):
    out = conv.convert(html)
    for a, b in FONT + WORDS:
        out = out.replace(a, b)
    return fix_lang(out)


if __name__ == '__main__':
    slugs = sys.argv[1:] or sorted(p.name for p in BASE.iterdir() if (p / 'zh-TW' / 'index.html').exists())
    for slug in slugs:
        src = (BASE / slug / 'zh-TW' / 'index.html').read_text(encoding='utf-8')
        dst = BASE / slug / 'zh-CN' / 'index.html'
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_text(convert(src), encoding='utf-8')
        print('✓', slug, 'zh-CN')
