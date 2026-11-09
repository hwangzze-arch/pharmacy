# -*- coding: utf-8 -*-
"""23장 강의 녹취록 PDF (A4 세로). python3 ch23_transcript.py → index.html → node render.js out.pdf"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.relpath(os.path.join(HERE, "..", "강의번역", "fonts"), HERE)
FONT = "".join(
    f"@font-face{{font-family:'NotoKR';font-weight:{w};src:url({FONTS}/noto-sans-kr-{s}-{w}-normal.woff2) format('woff2');}}"
    for s in ("korean", "latin", "latin-ext") for w in (400, 500, 700))

CSS = FONT + """
@page{size:A4;margin:16mm 16mm 16mm 16mm;}
*{box-sizing:border-box;}
body{font-family:'NotoKR','WenQuanYi Zen Hei',sans-serif;color:#1d2530;font-size:10.6pt;line-height:1.62;margin:0;-webkit-print-color-adjust:exact;print-color-adjust:exact;}
h1{font-size:19pt;color:#1f3f66;margin:0 0 2px 0;}
.sub{color:#5f6b78;font-size:10pt;margin-bottom:8px;}
.intro{background:#f3f6fa;border-left:4px solid #2a9d8f;padding:7px 11px;font-size:9.6pt;color:#333;margin:8px 0 14px 0;border-radius:4px;}
h2{font-size:12.6pt;color:#fff;background:#2a9d8f;padding:4px 10px;border-radius:5px;margin:16px 0 7px 0;break-after:avoid;}
h2 .t{font-weight:400;font-size:10pt;opacity:.9;margin-right:6px;}
h3{font-size:11pt;color:#1f3f66;margin:10px 0 4px 0;break-after:avoid;}
p{margin:0 0 6px 0;}
ul,ol{margin:0 0 6px 0;padding-left:1.4em;}
li{margin:0 0 3px 0;}
.pf{background:#fde8f3;border:1px solid #f3a6cf;border-left:4px solid #e0559c;border-radius:5px;padding:5px 10px;margin:6px 0;break-inside:avoid;}
.pf b.k{color:#a4185f;}
.nt{color:#5f6b78;font-size:9.4pt;}
.fix{background:#fff8dc;border:1px solid #f0d77a;border-left:4px solid #f2c200;border-radius:5px;padding:4px 10px;margin:5px 0;font-size:9.6pt;break-inside:avoid;}
.sl{display:inline-block;background:#e8f1fb;border:1px solid #a9c8e8;color:#1f3f66;border-radius:10px;padding:0 7px;font-size:8.6pt;margin-left:4px;vertical-align:1px;}
table{border-collapse:collapse;width:100%;margin:4px 0 8px 0;font-size:9.6pt;break-inside:avoid;}
th{background:#e3f4f1;color:#1f5f56;text-align:left;}
th,td{border:1px solid #b9cfcb;padding:3px 7px;vertical-align:top;}
.rec{display:block;width:max-content;break-after:avoid;background:#1f3f66;color:#fff;border-radius:4px;padding:1px 8px;font-size:9pt;margin:10px 0 2px 0;}
"""


def _unused_S(n):
    return f'<span class="sl">슬라이드 {n}</span>'


from ch23_body import BODY

html = f'<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>CH23 강의 녹취록</title><style>{CSS}</style></head><body>{BODY}</body></html>'
open(os.path.join(HERE, "index23.html"), "w").write(html)
print("ok")
