# 10주차(2026-11-11) 요약정리 빌드
# 슬라이드 7, 9~24는 6주차 자료와 똑같음 → 6주차 요약정리 페이지를 재사용하고 번호만 overlay로 덮어씀.
# 나머지(표지, Q&A 2~6, 지난 시간 요약 8, Chapter 4 약물대사 26~65)는 content.py로 새로 작성.
#   python3 build.py  → intro.html(새 페이지), overlay.html(재사용 페이지 번호), order.json
#   node build.js     → intro.pdf, overlay.pdf
#   python3 merge.py  → 최종 PDF
import os, json
from content import PAGES

HERE = os.path.dirname(os.path.abspath(__file__))
FOOT = "신약개발개론 · 후보물질 탐색 및 발굴2 &amp; 약물대사 연구1 — 슬라이드별 번역·설명"
TOTAL = len(PAGES)

FONT = '<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700&display=swap" rel="stylesheet">'

CSS = """
@page { size: 841.92pt 594.96pt; margin: 0; }
:root{--navy:#22457a;--title:#1c3b6b;--orange:#e07b1a;--muted:#4b5563;--foot:#374151;}
*{box-sizing:border-box;}
html,body{margin:0;padding:0;background:#fff;}
body{font-family:'Noto Sans KR',sans-serif;color:#1f2937;-webkit-print-color-adjust:exact;print-color-adjust:exact;}
.page{width:841.92pt;height:594.96pt;padding:24pt 35.4pt 0 35.4pt;position:relative;overflow:hidden;page-break-after:always;}
header{display:flex;align-items:flex-start;border-bottom:1.4pt solid var(--navy);padding-bottom:5pt;height:43pt;}
.num{background:var(--navy);color:#fff;font-weight:700;font-size:12.7pt;border-radius:12pt;width:34.3pt;height:23.8pt;line-height:23.8pt;text-align:center;margin:7.5pt 10.7pt 0 0;flex:none;}
.ttl{flex:1;min-width:0;}
.ttl h1{margin:0;font-size:17.2pt;line-height:1.25;color:var(--title);font-weight:700;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;}
.ttl .sub{font-size:8.6pt;color:#374151;margin-top:1pt;}
.src{font-size:9pt;color:var(--muted);margin-top:7.5pt;white-space:nowrap;padding-left:8pt;}
.top{display:flex;gap:14pt;margin-top:7pt;height:var(--toph,232pt);}
.kw{width:var(--kww,182pt);flex:none;}
.lbl{font-size:9pt;font-weight:700;color:var(--title);margin-bottom:6pt;}
.chips{display:flex;flex-wrap:wrap;gap:5pt;}
.chip{background:#eef4fc;border:1px solid #9dbbe3;color:#1c3b6b;border-radius:11pt;padding:2.5pt 8pt;font-size:8.6pt;}
.img{flex:none;height:100%;display:flex;gap:6pt;align-items:flex-start;}
.img img{height:var(--imgh,100%);border-radius:4pt;box-shadow:0 1px 4px rgba(0,0,0,.25);}
.sum{flex:1;align-self:flex-start;background:#fff8dc;border:1px solid #f2dc8c;border-left:3.5pt solid #e6a700;border-radius:4pt;padding:10pt 12pt;}
.sum p{margin:0;font-size:9.6pt;line-height:1.75;}
.bottom{display:flex;gap:13pt;margin-top:9pt;font-size:var(--fs,9.6pt);line-height:1.6;}
.col.tr{width:var(--trw,342pt);flex:none;} .col.ex{flex:1;}
.badge{display:inline-block;color:#fff;font-weight:700;font-size:9.6pt;padding:3.5pt 8pt;border-radius:3pt;margin-bottom:6pt;}
.badge.b{background:var(--navy);} .badge.o{background:var(--orange);}
.body p{margin:0 0 4pt 0;}
.body ul,.body ol{margin:0 0 4pt 0;padding-left:14pt;} .body li{margin:0 0 2pt 0;}
.body h3{margin:0 0 4pt 0;font-size:1.04em;color:var(--title);}
.note{color:var(--muted);font-size:.9em;}
y{background:#fff07a;padding:0 2px;border-radius:2px;}
g{background:#a6eb8e;padding:0 2px;border-radius:2px;}
pk{background:#ffc4e3;padding:0 2px;border-radius:2px;}
.tag{display:inline-block;background:#ffc4e3;color:#7a1550;font-weight:700;font-size:.92em;padding:0 5px;border-radius:3px;margin-right:4px;}
.box{background:#fde8f3;border:1px solid #f3a6cf;border-left:3.5pt solid #e0559c;border-radius:4pt;padding:4pt 8pt;margin:4pt 0;}
table.t{border-collapse:collapse;width:100%;margin:2pt 0 5pt 0;font-size:.93em;line-height:1.45;}
table.t th{background:#e3edf8;color:#1c3b6b;text-align:left;font-weight:700;}
table.t th,table.t td{border:1px solid #b9c7d6;padding:2pt 5pt;vertical-align:top;}
footer{position:absolute;left:35.4pt;right:35.4pt;bottom:16pt;border-top:1px solid #d5dbe2;padding-top:5pt;display:flex;font-size:7.1pt;color:var(--foot);align-items:center;}
footer .l{flex:1;} footer .m{flex:1;display:flex;gap:8pt;align-items:center;justify-content:center;}
footer .r{flex:none;width:60pt;text-align:right;}
.sw{display:inline-block;width:11pt;height:7pt;margin-right:3pt;vertical-align:middle;}
"""

LEGEND = ('형광펜 <span><span class="sw" style="background:#fff07a"></span>핵심 개념</span>'
          '<span><span class="sw" style="background:#a6eb8e"></span>공식·정의·결론</span>'
          '<span><span class="sw" style="background:#ffc4e3"></span>시험 포인트 / Q&amp;A</span>')


def page_html(i, p):
    chips = "".join(f'<span class="chip">{k}</span>' for k in p["kw"])
    imgs = p["img"] if isinstance(p["img"], list) else [p["img"]]
    st = []
    if len(imgs) > 1:   # 두 장을 나란히: 이미지를 낮추고 키워드 칸을 좁힘
        st += ["--imgh:150pt", "--kww:150pt", "--toph:150pt"]
    st += p.get("style", [])
    style = f' style="{";".join(st)}"' if st else ""
    src = p.get("src") or "원본 슬라이드 " + p["slide"]
    img_html = "".join(f'<img src="{f}">' for f in imgs)
    return f'''<section class="page"{style}>
<header><div class="num">{i:02d}</div><div class="ttl"><h1>{p["title"]}</h1><div class="sub">{p["sub"]}</div></div><div class="src">{src}</div></header>
<div class="top"><div class="kw"><div class="lbl">핵심 키워드</div><div class="chips">{chips}</div></div>
<div class="img">{img_html}</div>
<div class="sum"><div class="lbl">한 줄 요약</div><p>{p["sum"]}</p></div></div>
<div class="bottom"><div class="col tr"><span class="badge b">{p.get("lab", "한글 번역")}</span><div class="body">{p["tr"]}</div></div>
<div class="col ex"><span class="badge o">상세 설명 · 풀이</span><div class="body">{p["ex"]}</div></div></div>
<footer><div class="l">{FOOT}</div><div class="m">{LEGEND}</div><div class="r">{i} / {TOTAL}</div></footer>
</section>'''


OV_CSS = """
@page { size: 841.92pt 594.96pt; margin: 0; }
html,body{margin:0;padding:0;background:transparent;}
body{font-family:'Noto Sans KR',sans-serif;-webkit-print-color-adjust:exact;print-color-adjust:exact;}
.page{width:841.92pt;height:594.96pt;position:relative;overflow:hidden;page-break-after:always;}
.w{position:absolute;background:#fff;}
.num{position:absolute;left:35.25pt;top:31.5pt;width:34.3pt;height:23.8pt;line-height:23.8pt;border-radius:12pt;background:#22457a;color:#fff;font-weight:700;font-size:12.7pt;text-align:center;}
.src{position:absolute;right:35.4pt;top:30.3pt;font-size:9pt;color:#4b5563;white-space:nowrap;background:#fff;padding-left:6pt;}
.src span{font-size:7.6pt;color:#8a94a3;}
.fl{position:absolute;left:35.4pt;top:565pt;font-size:7.1pt;color:#374151;white-space:nowrap;}
.fr{position:absolute;right:35.4pt;top:565pt;font-size:7.1pt;color:#374151;text-align:right;}
"""


def overlay_page(n, now, old):
    return f'''<section class="page">
<div class="w" style="left:33pt;top:29pt;width:40pt;height:29pt"></div><div class="num">{n:02d}</div>
<div class="w" style="left:690pt;top:28pt;width:125pt;height:15pt"></div>
<div class="src">원본 슬라이드 {now} <span>(6주차 {old})</span></div>
<div class="w" style="left:33pt;top:563pt;width:200pt;height:12pt"></div><div class="fl">{FOOT}</div>
<div class="w" style="left:760pt;top:563pt;width:50pt;height:12pt"></div><div class="fr">{n} / {TOTAL}</div>
</section>'''


def doc(title, css, body):
    return f'<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>{title}</title>{FONT}<style>{css}</style></head><body>{body}</body></html>'


new, ov, order = [], [], []
for i, p in enumerate(PAGES, 1):
    if "reuse" in p:   # (6주차 요약정리 쪽, 이번 슬라이드, 6주차 슬라이드)
        k, now, old = p["reuse"]
        ov.append(overlay_page(i, now, old)); order.append(["old", k])
    else:
        new.append(page_html(i, p)); order.append(["new"])

open(os.path.join(HERE, "intro.html"), "w").write(doc("10주차 요약정리", CSS, "".join(new)))
open(os.path.join(HERE, "overlay.html"), "w").write(doc("overlay", OV_CSS, "".join(ov)))
json.dump(order, open(os.path.join(HERE, "order.json"), "w"))
print("total pages", TOTAL, "new", len(new), "reused", len(ov))
