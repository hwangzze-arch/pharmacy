# -*- coding: utf-8 -*-
"""22장 마스터 요약본 설정 + 구조식 도우미. 다른 장은 CH·MODS·색만 바꿔 복사."""
import os, sys
D = os.path.dirname(os.path.abspath(__file__))
LEC = os.path.join(D, "..", "강의번역")
sys.path.insert(0, LEC)
from fig import svg as _svg, row as _row  # noqa: E402
from mech import panel, step, mrow, MECH_CSS  # noqa: E402
import mslides22  # noqa: E402

CH = 22
TITLE = "약품유기화학2 제22장 마스터 요약본"
FOOT = "약품유기화학 2 · 기말 대비 마스터 요약본 · 제22장 카르보닐 알파 치환 반응"
MODS = ["c00_front", "c10_p1", "c20_p2", "c30_p3", "c90_final"]
IMG = "../강의번역/img/"
COLOR = "#2b8a3e"      # 22장 색 (17 #2a6f97 · 18 #2a9d8f · 19 #7b5cd6 · 20 #e76f51 · 21 #d1495b)
COLOR_SOFT = "#e9f6ec"

P1 = "PART 1 · 엔올과 산성 α-치환"
P2 = "PART 2 · α-H 산성도와 엔올레이트"
P3 = "PART 3 · 엔올레이트 알킬화"
P0 = "읽기 전에"

FONT = "".join(
    f"@font-face{{font-family:'NotoKR';font-weight:{w};src:url(../강의번역/fonts/noto-sans-kr-{s}-{w}-normal.woff2) format('woff2');}}"
    for s in ("korean", "latin", "latin-ext") for w in (400, 500, 700))

CSS_EXTRA = FONT + MECH_CSS + f"""
:root{{--indigo:{COLOR};--indigo-soft:{COLOR_SOFT};}}
.sec{{color:{COLOR};}}
table.t th{{background:{COLOR_SOFT};color:{COLOR};}}
.card.rec{{background:#fff0f6;border-color:#f3a6cf;}} .card.rec .ct{{color:#a61e4d;}}
.card.my{{background:#fff5f5;border:1.5px dashed #f08c8c;}} .card.my .ct{{color:#c92a2a;}}
.mband{{flex:none;margin-top:7px;background:#fff;border:1px solid var(--line);border-radius:9px;padding:3px 8px 2px 8px;overflow:hidden;position:relative;}}
.mband .mbl{{position:absolute;top:4px;right:8px;font-size:10px;font-weight:700;color:{COLOR};background:{COLOR_SOFT};border-radius:6px;padding:0 7px;}}
.mz{{display:inline-block;transform-origin:0 0;}}
.fig.mfig{{text-align:left;overflow:hidden;}}
.afig{{background:#fff;border:1px solid #cfe5d8;border-radius:9px;padding:3px 6px;margin-top:6px;overflow:hidden;}}
.qk.draw{{background:#2b8a3e;}} .qk.reag{{background:#1971c2;}} .qk.ord{{background:#9a4a12;}} .qk.mech{{background:#a61e4d;}}
.qk.ex{{background:#c2255c;}} .qk.prod{{background:#5f3dc4;}} .qk.int{{background:#0b7285;}} .qk.sa{{background:#495057;}} .qk.bl{{background:#6a3d9a;}}
.mol{{display:inline-block;vertical-align:middle;}} .mol svg{{display:block;}}
.molrow{{display:flex;align-items:center;flex-wrap:wrap;gap:4px 14px;margin:3px 0;}}
.molrow .c{{display:inline-flex;flex-direction:column;align-items:center;font-size:.85em;}}
.rx{{display:flex;align-items:center;flex-wrap:nowrap;gap:2px;margin:3px 0;}}
.rx .rl{{font-weight:700;color:{COLOR};width:24px;flex:none;}}
.rx .mol svg{{display:block;}} .rx .tx{{font-size:.85em;padding:0 3px;}}
.arw{{display:inline-flex;flex-direction:column;align-items:center;min-width:60px;font-size:.78em;line-height:1.2;color:#1f3f66;padding:0 3px;}}
.arw .al{{display:block;width:100%;height:0;border-top:1.4px solid #333;position:relative;margin:2px 0;}}
.arw .al::after{{content:'';position:absolute;right:-1px;top:-4.6px;border-left:7px solid #333;border-top:4px solid transparent;border-bottom:4px solid transparent;}}
.cap2{{display:inline-flex;flex-direction:column;align-items:center;font-size:.82em;color:#333;}}
"""


def S(smiles, w=130, h=90, scale=22):
    """구조식 SVG 한 개."""
    return f'<span class="mol">{_svg(smiles, w, h, scale)}</span>'


def C(smiles, cap, w=130, h=90):
    """밑에 이름이 붙은 구조식."""
    return f'<span class="c cap2">{_svg(smiles, w, h)}<span>{cap}</span></span>'


def MOLS(*items):
    return '<div class="molrow">' + "".join(items) + '</div>'


RX = _row  # ('m', smiles, w, h) / ('a', 위, 아래) / ('t', 글자)


def MS(key, i=None):
    """번역본 슬라이드 옆 메커니즘 그림 재사용."""
    figs = mslides22.MS[key]
    return figs[i] if i is not None else "".join(figs)


def MSR(key, *idx):
    """번역본 메커니즘 그림에서 원하는 줄(0부터)만."""
    rows = []
    for f in mslides22.MS[key]:
        rows += ['<div class="mrow' + x for x in f.split('<div class="mrow')[1:]]
    return "".join(rows[i] for i in idx)
