# -*- coding: utf-8 -*-
"""강의 슬라이드 번역·설명 PDF (CH21_약품유기화학2_번역본과 같은 형식).

사용:
  sh make_img.sh "../../CH22_약품유기화학2.pdf"     # img/s-01.jpg …
  python3 build.py                                   # index.html
  node render.js "../../CH22_약품유기화학2_번역본.pdf"   # PDF
"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from ch22_1 import PAGES as P1
from ch22_2 import PAGES as P2
from ch22_3 import PAGES as P3

PAGES = P1 + P2 + P3

# 메커니즘: 슬라이드 그림 바로 옆에 (그림이 많으면 '(계속)' 쪽에 슬라이드와 함께)
from mslides22 import MS, FIRST_ROWS, ANS_FULL
from mech import MECH_CSS


def _rows(html):
    parts = html.split('<div class="mrow')
    return ['<div class="mrow' + x for x in parts[1:]]

_out = []
for _p in PAGES:
    _k = _p.get("slide") if _p.get("slide") in MS else _p.get("img")
    if _k in MS:
        _figs = list(MS[_k])
        if _k in FIRST_ROWS:
            _r = _rows(_figs[0])
            _n = FIRST_ROWS[_k]
            if len(_r) > _n:
                _figs[0:1] = ["".join(_r[:_n]), "".join(_r[_n:])]
        if _k in ANS_FULL:
            _figs = [ANS_FULL[_k] + _f for _f in _figs]
        _left = {"a42": "p42", "a54": "p54"}.get(_k)  # 풀이 쪽 왼쪽엔 문제, 정답은 메커니즘 줄 위에
        _out.append(dict(_p, ms=_figs[0], **({"msimg": _left} if _left else {})))
        for _j, _f in enumerate(_figs[1:], 2):
            _out.append(dict(cont=True, img=_p["img"], ms=_f, **({"msimg": _left} if _left else {}), title=f'{_p["title"]} <span class="cont">(메커니즘 {_j})</span>',
                             sub=_p["sub"], src=(_p.get("src") or f'원본 슬라이드 {_p["slide"]}') + " · 계속"))
    else:
        _out.append(_p)
PAGES = _out
TOTAL = len(PAGES)
FOOT = "약품유기화학 2 · 제22장 카르보닐 알파 치환 반응 · 슬라이드별 번역·설명"

FONT = "".join(
    f"@font-face{{font-family:'NotoKR';font-weight:{w};src:url(fonts/noto-sans-kr-{s}-{w}-normal.woff2) format('woff2');}}"
    for s in ("korean", "latin", "latin-ext") for w in (400, 500, 700))

CSS = FONT + MECH_CSS + """
@page { size: 297mm 210mm; margin: 0; }
:root{--blue:#2c6aa0;--navy:#1f3f66;--orange:#d97a26;--line:#2c6aa0;--muted:#5f6b78;}
*{box-sizing:border-box;}
html,body{margin:0;padding:0;background:#fff;}
body{font-family:'NotoKR','WenQuanYi Zen Hei',sans-serif;color:#1d2530;-webkit-print-color-adjust:exact;print-color-adjust:exact;}
.page{width:297mm;height:210mm;padding:7mm 11mm 15mm 11mm;position:relative;overflow:hidden;page-break-after:always;display:flex;flex-direction:column;}
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
.img{flex:none;height:100%;max-width:640px;display:flex;align-items:flex-start;justify-content:center;}
.img img{max-height:100%;max-width:100%;border:1px solid #c9cfd6;border-radius:6px;box-shadow:0 1px 4px rgba(0,0,0,.18);}
.fig{flex:none;width:var(--figw,600px);height:100%;border:1px solid #c9cfd6;border-radius:6px;box-shadow:0 1px 4px rgba(0,0,0,.18);padding:6px 10px;overflow:hidden;font-size:11px;}
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
.box{background:#fde8f3;border:1px solid #f3a6cf;border-left:4px solid #e0559c;border-radius:5px;padding:5px 9px;margin:4px 0;}
.boxg{background:#ecf9e6;border:1px solid #a9db95;border-left:4px solid #4caf2c;border-radius:5px;padding:5px 9px;margin:4px 0;}
table.t{border-collapse:collapse;width:100%;margin:3px 0 5px 0;font-size:.95em;}
table.t th{background:#e3edf8;color:#1f3f66;text-align:left;font-weight:700;}
table.t th,table.t td{border:1px solid #b9c7d6;padding:2px 6px;vertical-align:top;}
.eq{background:#f3f6fa;border-radius:4px;padding:2px 8px;display:inline-block;margin:1px 0;}
.rx{display:flex;align-items:center;flex-wrap:nowrap;gap:2px;margin:2px 0;}
.rx .rl{font-weight:700;color:var(--navy);width:26px;flex:none;font-size:12px;}
.rx .mol svg{display:block;}
.rx .tx{font-size:11px;color:#333;padding:0 3px;}
.arw{display:inline-flex;flex-direction:column;align-items:center;min-width:62px;font-size:9.5px;line-height:1.2;color:#1f3f66;padding:0 3px;}
.arw .al{display:block;width:100%;height:0;border-top:1.4px solid #333;position:relative;margin:2px 0;}
.arw .al::after{content:'';position:absolute;right:-1px;top:-4.6px;border-left:7px solid #333;border-top:4px solid transparent;border-bottom:4px solid transparent;}
.cap{display:inline-flex;flex-direction:column;align-items:center;font-size:10px;color:#333;margin:0 4px;}
.cap svg{display:block;}
.mini{display:inline-block;vertical-align:middle;}
footer{position:absolute;left:11mm;right:11mm;bottom:5mm;border-top:1px solid #d5dbe2;padding-top:5px;display:flex;font-size:9.5px;color:var(--muted);align-items:center;}
footer .l{flex:1;} footer .m{flex:1;display:flex;gap:9px;align-items:center;justify-content:center;}
footer .r{flex:none;width:80px;text-align:right;}
.sw{display:inline-block;width:13px;height:8px;border-radius:2px;margin-right:3px;vertical-align:middle;}
.msrow{display:flex;gap:10px;margin-top:8px;flex:none;align-items:flex-start;}
.msimg{flex:none;width:300px;}
.msimg img{width:100%;border:1px solid #c9cfd6;border-radius:6px;box-shadow:0 1px 4px rgba(0,0,0,.18);}
.mfig{flex:1;min-width:0;border:1px solid #c9cfd6;border-radius:6px;padding:3px 6px;background:#fcfdfe;overflow:hidden;}
.sumbar{flex:none;margin-top:7px;background:#fff8dc;border:1px solid #f0d77a;border-left:5px solid #f2c200;border-radius:6px;padding:4px 10px;font-size:11.5px;line-height:1.5;}
.sumbar b{color:#7a5a00;margin-right:6px;}
.ms .bottom{margin-top:7px;}
.ms.cont .msimg{width:210px;}
.ansrow{margin:2px 0 0 0;}
.ansrow img.ans{height:78px;border:1px solid #e3e6ea;border-radius:4px;background:#fff;}
.mrow .ml.ansl{background:#7b5cd6;}
.ansrow img.ans.full{height:120px;}
.cont{color:#2a9d8f;font-size:.8em;}
"""


def ms_html(i, p):
    """슬라이드 그림(왼쪽) + 같은 그림의 메커니즘(오른쪽)."""
    im = p["img"]
    im = f"s-{im:02d}" if isinstance(im, int) else im
    src = p.get("src") or f'원본 슬라이드 {p["slide"]}'
    head = f'''<header><div class="num">{i:02d}</div><div class="ttl"><h1>{p["title"]}</h1><div class="sub">{p["sub"]}</div></div><div class="src">{src}</div></header>
<div class="msrow"><div class="msimg"><img src="img/{p.get("msimg", im)}.jpg"></div><div class="mfig">{p["ms"]}</div></div>'''
    if p.get("cont"):
        body = ""
    else:
        lab1 = p.get("tr_label", "한글 번역")
        lab2 = p.get("ex_label", "상세 설명 · 풀이")
        body = f'''<div class="sumbar"><b>한 줄 요약</b> {p["sum"]}</div>
<div class="bottom"><div class="col tr"><span class="badge b">{lab1}</span><div class="body">{p["tr"]}</div></div>
<div class="col ex"><span class="badge o">{lab2}</span><div class="body">{p["ex"]}</div></div></div>'''
    cls = "page ms cont" if p.get("cont") else "page ms"
    return f'''<section class="{cls}">
{head}
{body}
<footer><div class="l">{FOOT}</div><div class="m">곡선 화살표 = 전자쌍 이동 (출발: 비공유전자쌍 ·· 또는 결합 → 도착: 원자 또는 새 결합)</div><div class="r">{i} / {TOTAL}</div></footer>
</section>'''


def page_html(i, p):
    if p.get("ms"):
        return ms_html(i, p)
    chips = "".join(f'<span class="chip">{k}</span>' for k in p["kw"])
    src = p.get("src") or f'원본 슬라이드 {p["slide"]}'
    lab1 = p.get("tr_label", "한글 번역")
    lab2 = p.get("ex_label", "상세 설명 · 풀이")
    st = []
    if p.get("toph"):
        st.append(f'--toph:{p["toph"]}px')
    if p.get("figw"):
        st.append(f'--figw:{p["figw"]}px')
    style = f' style="{";".join(st)}"' if st else ""
    if p.get("fig"):
        vis = f'<div class="fig">{p["fig"]}</div>'
    else:
        im = p["img"]
        im = f"s-{im:02d}" if isinstance(im, int) else im
        vis = f'<div class="img"><img src="img/{im}.jpg"></div>'
    return f'''<section class="page"{style}>
<header><div class="num">{i:02d}</div><div class="ttl"><h1>{p["title"]}</h1><div class="sub">{p["sub"]}</div></div><div class="src">{src}</div></header>
<div class="top"><div class="kw"><div class="lbl">핵심 키워드</div><div class="chips">{chips}</div></div>
{vis}
<div class="sum"><div class="lbl">한 줄 요약</div><p>{p["sum"]}</p></div></div>
<div class="bottom"><div class="col tr"><span class="badge b">{lab1}</span><div class="body">{p["tr"]}</div></div>
<div class="col ex"><span class="badge o">{lab2}</span><div class="body">{p["ex"]}</div></div></div>
<footer><div class="l">{FOOT}</div><div class="m">형광펜 <span><span class="sw" style="background:#fff07a"></span>핵심 개념</span><span><span class="sw" style="background:#a6eb8e"></span>공식·정의·결론</span><span><span class="sw" style="background:#ffc4e3"></span>시험 포인트 / Q&amp;A</span></div><div class="r">{i} / {TOTAL}</div></footer>
</section>'''


html = f'''<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>CH22 카르보닐 알파 치환 반응 번역·설명</title><style>{CSS}</style></head><body>
{"".join(page_html(i+1, p) for i, p in enumerate(PAGES))}
</body></html>'''
open(os.path.join(os.path.dirname(__file__), "index.html"), "w").write(html)
print("pages", TOTAL)
