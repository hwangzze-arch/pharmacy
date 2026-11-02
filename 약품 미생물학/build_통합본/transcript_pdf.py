# -*- coding: utf-8 -*-
"""녹취록 마크다운(.md) → 가로형(삼성노트 16:10) PDF
사용: python3 transcript_pdf.py <입력.md> <출력.pdf>"""
import sys, os, subprocess, markdown

src, out = sys.argv[1], sys.argv[2]
md = open(src, encoding="utf-8").read()
title = md.splitlines()[0].lstrip("# ").strip()
body = markdown.markdown(md, extensions=["tables", "sane_lists"])
# 핵심 정리 / 원문 구분: '녹취록 원문' 제목부터는 원문 스타일
body = body.replace("<h2>녹취록 원문", '<div class="raw-start"></div><h2 class="raw">녹취록 원문', 1)
css = """
@page { size: 297mm 186mm; margin: 11mm 13mm 12mm; }
* { box-sizing: border-box; }
body { font-family: "Pretendard", sans-serif; color: #1d2330; font-size: 10.3pt; line-height: 1.55; word-break: keep-all; margin: 0; }
h1 { font-size: 19pt; font-weight: 900; color: #fff; background: linear-gradient(120deg,#5847d6,#2a6fb5); padding: 4mm 6mm; border-radius: 3mm; margin: 0 0 3mm; column-span: all; }
h1 + ul { column-span: all; background: #efedfd; border-radius: 2mm; padding: 2.5mm 6mm 2.5mm 9mm; margin: 0 0 4mm; }
h2 { font-size: 14pt; font-weight: 800; color: #5847d6; border-bottom: 2px solid #5847d6; padding-bottom: 1mm; margin: 4mm 0 2mm; column-span: all; break-after: avoid; }
h2.raw { color: #5d6678; border-color: #9aa1ae; break-before: page; }
h3 { font-size: 11.6pt; font-weight: 800; color: #fff; background: #5847d6; display: inline-block; padding: .6mm 3mm; border-radius: 1.5mm; margin: 3.5mm 0 1.5mm; break-after: avoid; }
h2.raw ~ h3 { background: #5d6678; }
.content { column-count: 2; column-gap: 9mm; column-rule: 1px solid #e3e6ec; }
p { margin: 1.2mm 0; }
ul, ol { margin: 1mm 0; padding-left: 5.5mm; }
li { margin: .5mm 0; }
strong { color: #3b2fb0; }
h2.raw ~ * strong { color: #1d2330; }
table { width: 100%; border-collapse: collapse; font-size: 9.2pt; margin: 2mm 0; break-inside: avoid; }
th { background: #5847d6; color: #fff; text-align: left; padding: 1mm 1.6mm; }
td { border-bottom: 1px solid #e3e6ec; padding: .9mm 1.6mm; vertical-align: top; }
tr:nth-child(even) td { background: #f7f7fb; }
hr { display: none; }
code { font-family: inherit; background: #f1f2f6; padding: 0 1mm; border-radius: 1mm; }
"""
html = f'<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>{title}</title><style>{css}</style></head><body><div class="content">{body}</div></body></html>'
tmp = os.path.splitext(out)[0] + ".tmp.html"
open(tmp, "w", encoding="utf-8").write(html)
js = """
const { chromium } = require('/opt/node22/lib/node_modules/playwright');
(async () => { const b = await chromium.launch(); const p = await b.newPage();
  await p.goto('file://' + process.argv[1]); await p.evaluate(() => document.fonts.ready);
  await p.pdf({ path: process.argv[2], preferCSSPageSize: true, printBackground: true,
    displayHeaderFooter: true, headerTemplate: '<span></span>',
    footerTemplate: '<div style="font-size:7pt;color:#9aa1ae;width:100%;text-align:right;padding-right:13mm"><span class=pageNumber></span> / <span class=totalPages></span></div>' });
  await b.close(); })();
"""
subprocess.run(["node", "-e", js, os.path.abspath(tmp), os.path.abspath(out)], check=True)
os.remove(tmp)
print("ok", out)
