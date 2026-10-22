import os, sys, importlib
sys.path.insert(0, os.path.dirname(__file__))
from content1 import PAGES as P1
from content2 import PAGES as P2
from content3 import PAGES as P3

PAGES = P1 + P2 + P3
TOTAL = len(PAGES)
FOOT = "의약품분석학 II · Lecture 5 (질량분석법) — 슬라이드별 번역·설명"

CSS = """
@page { size: 297mm 210mm; margin: 0; }
:root{--blue:#2c6aa0;--navy:#1f3f66;--orange:#d97a26;--line:#2c6aa0;--muted:#5f6b78;}
*{box-sizing:border-box;}
html,body{margin:0;padding:0;background:#fff;}
body{font-family:'Noto Sans KR',sans-serif;color:#1d2530;-webkit-print-color-adjust:exact;print-color-adjust:exact;}
.page{width:297mm;height:210mm;padding:7mm 11mm 0 11mm;position:relative;overflow:hidden;page-break-after:always;display:flex;flex-direction:column;}
header{display:flex;align-items:flex-start;border-bottom:2.5px solid var(--line);padding-bottom:4px;}
.num{background:var(--blue);color:#fff;font-weight:700;font-size:13px;border-radius:14px;padding:5px 13px;margin:5px 12px 0 0;}
.ttl{flex:1;}
.ttl h1{margin:0;font-size:19px;line-height:1.3;color:var(--navy);font-weight:700;}
.ttl .sub{font-size:11px;color:var(--muted);}
.src{font-size:10.5px;color:var(--muted);margin-top:10px;white-space:nowrap;}
.top{display:flex;gap:16px;margin-top:9px;height:var(--toph,292px);flex:none;}
.kw{width:205px;flex:none;}
.lbl{font-size:10.5px;font-weight:700;color:var(--blue);margin-bottom:5px;}
.chips{display:flex;flex-wrap:wrap;gap:5px;}
.chip{background:#e8f1fb;border:1px solid #a9c8e8;color:#1f3f66;border-radius:12px;padding:2px 9px;font-size:10.5px;}
.img{flex:none;height:100%;display:flex;align-items:flex-start;justify-content:center;}
.img img{height:100%;border:1px solid #c9cfd6;border-radius:6px;box-shadow:0 1px 4px rgba(0,0,0,.18);}
.sum{flex:1;align-self:flex-start;background:#fff8dc;border:1px solid #f0d77a;border-left:5px solid #f2c200;border-radius:6px;padding:9px 13px;}
.sum .lbl{color:#7a5a00;}
.sum p{margin:0;font-size:12px;line-height:1.6;}
.bottom{display:flex;gap:22px;margin-top:11px;flex:1;min-height:0;font-size:var(--fs,12.5px);line-height:1.55;}
.col{min-height:0;overflow:hidden;}
.col.tr{width:46%;}
.col.ex{width:54%;}
.badge{display:inline-block;color:#fff;font-weight:700;font-size:12.5px;padding:2px 10px;border-radius:5px;margin-bottom:6px;}
.badge.b{background:var(--blue);} .badge.o{background:var(--orange);}
.body p{margin:0 0 4px 0;}
.body ul,.body ol{margin:0 0 4px 0;padding-left:1.25em;}
.body li{margin:0 0 2px 0;}
.tr ul{list-style:none;padding-left:.9em;}
.tr ul li{position:relative;}
.tr ul li::before{content:'';position:absolute;left:-.85em;top:.62em;width:5px;height:5px;background:var(--blue);border-radius:1px;}
.note{color:var(--muted);font-size:.92em;}
y{background:#fff07a;padding:0 2px;border-radius:2px;}
g{background:#a6eb8e;padding:0 2px;border-radius:2px;}
pk{background:#ffc4e3;padding:0 2px;border-radius:2px;}
.tag{display:inline-block;background:#ffc4e3;color:#7a1550;font-weight:700;font-size:.9em;padding:0 5px;border-radius:3px;margin-right:4px;}
.tag.g{background:#a6eb8e;color:#1d5a0c;}
.tag.y{background:#fff07a;color:#6b5600;}
.box{background:#fde8f3;border:1px solid #f3a6cf;border-left:4px solid #e0559c;border-radius:5px;padding:5px 9px;margin:4px 0;}
.boxg{background:#ecf9e6;border:1px solid #a9db95;border-left:4px solid #4caf2c;border-radius:5px;padding:5px 9px;margin:4px 0;}
table.t{border-collapse:collapse;width:100%;margin:3px 0 5px 0;font-size:.95em;}
table.t th{background:#e3edf8;color:#1f3f66;text-align:left;font-weight:700;}
table.t th,table.t td{border:1px solid #b9c7d6;padding:2px 6px;vertical-align:top;}
.eq{font-family:'Noto Sans KR',sans-serif;background:#f3f6fa;border-radius:4px;padding:2px 8px;display:inline-block;margin:1px 0;}
footer{position:absolute;left:11mm;right:11mm;bottom:5mm;border-top:1px solid #d5dbe2;padding-top:5px;display:flex;font-size:9.5px;color:var(--muted);align-items:center;}
footer .l{flex:1;} footer .m{flex:1;display:flex;gap:9px;align-items:center;justify-content:center;}
footer .r{flex:none;width:80px;text-align:right;}
.sw{display:inline-block;width:13px;height:8px;border-radius:2px;margin-right:3px;vertical-align:middle;}
.page{padding-bottom:15mm;}
"""

def page_html(i, p):
    chips = "".join(f'<span class="chip">{k}</span>' for k in p["kw"])
    src = p.get("src") or f'원본 슬라이드 {p["slide"]}'
    lab2 = p.get("tr_label", "한글 번역")
    toph = p.get("toph")
    style = f' style="--toph:{toph}px"' if toph else ""
    return f'''<section class="page"{style}>
<header><div class="num">{i:02d}</div><div class="ttl"><h1>{p["title"]}</h1><div class="sub">{p["sub"]}</div></div><div class="src">{src}</div></header>
<div class="top"><div class="kw"><div class="lbl">핵심 키워드</div><div class="chips">{chips}</div></div>
<div class="img"><img src="img/s-{p["img"]:02d}.jpg"></div>
<div class="sum"><div class="lbl">한 줄 요약</div><p>{p["sum"]}</p></div></div>
<div class="bottom"><div class="col tr"><span class="badge b">{lab2}</span><div class="body">{p["tr"]}</div></div>
<div class="col ex"><span class="badge o">상세 설명 · 풀이</span><div class="body">{p["ex"]}</div></div></div>
<footer><div class="l">{FOOT}</div><div class="m">형광펜 <span><span class="sw" style="background:#fff07a"></span>핵심 개념</span><span><span class="sw" style="background:#a6eb8e"></span>공식·정의·결론</span><span><span class="sw" style="background:#ffc4e3"></span>시험 포인트 / Q&amp;A</span></div><div class="r">{i} / {TOTAL}</div></footer>
</section>'''

html = f'''<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>Lecture 5 질량분석법 번역·설명</title><style>{CSS}</style></head><body>
{"".join(page_html(i+1, p) for i, p in enumerate(PAGES))}
</body></html>'''
open(os.path.join(os.path.dirname(__file__), "index.html"), "w").write(html)
print("pages", TOTAL)
