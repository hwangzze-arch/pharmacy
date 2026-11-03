# -*- coding: utf-8 -*-
"""제22장 핵심 킬러 TOP 10 — 최종 실전 마스터북 (A4 세로, 흐르는 책 형식).
python3 build_book.py && node render_book.js ../../CH22_핵심킬러TOP10_마스터북.pdf"""
import os
from PIL import Image
from content import *

D = os.path.dirname(os.path.abspath(__file__))
FONT = "../강의번역/fonts"
GRADE = {1: ("1등급", "무조건 100% 출제! 교수님 지정 과제 4인방", "#e8a317", "#fff6dc", 5),
         2: ("2등급", "약대 전공 의약품 합성 & 서술형/빈칸 1순위", "#3a6ea5", "#eaf1fa", 4),
         3: ("3등급", "실전 응용력을 완성해 주는 알짜배기", "#2f8f6b", "#e8f6ef", 3)}


def img(name, cap="", scale=0.70, cls="fig"):
    w = Image.open(os.path.join(D, "img", name + ".png")).width / 3 * scale
    c = f'<figcaption>{cap}</figcaption>' if cap else ""
    return f'<figure class="{cls}"><img src="img/{name}.png" style="width:{w:.0f}px">{c}</figure>'


def table(rows, cls="tb"):
    h = "".join(f"<th>{c}</th>" for c in rows[0])
    b = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows[1:])
    return f'<table class="{cls}"><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table>'


def sec(num, title, body, sub="", wide=False):
    return f'<section class="dash{" wide" if wide else ""}"><div class="dh"><span class="dn">{num}</span><div><h2>{title}</h2><div class="ds">{sub}</div></div></div>{body}</section>'


# ───────── 표지 (따로 렌더 — 쪽 번호 없음)
def cover():
    tiers = ""
    for g in (1, 2, 3):
        nm, desc, col, soft, _ = GRADE[g]
        items = "".join(f'<li><b>{t["rank"]}위</b> 문제 {t["no"]} <span>{t["title"]}</span></li>' for t in TOP if t["grade"] == g)
        tiers += f'<div class="ct" style="--c:{col}"><div class="ctn">{nm}</div><div class="ctd">{desc}</div><ol>{items}</ol></div>'
    return f'''<div class="cover">
<div class="cv-k">약품유기화학 2 · 기말고사 직전 · 제22장 카르보닐 알파 치환 반응</div>
<div class="cv-big">KILLER<br><em>TOP 10</em></div>
<div class="cv-t">단번에 이해하는 최종 실전 마스터북</div>
<div class="cv-s">54쪽 마스터요약 + 삼성노트 내 필기 + 구조식 위 <i class="pr">빨강</i>·<i class="pg">초록</i>·<i class="pb">파랑</i> 펜 표시 논리를 하나로</div>
<div class="cv-tiers">{tiers}</div>
<div class="cv-f">이 책 하나만 보고 시험장에 들어간다 · PART 0 대시보드 → TOP 1~10 → 답안지</div>
</div>'''


# ───────── PART 0 대시보드
def part0():
    o = ['<div class="part"><div class="pk">PART 0</div><h1>시험 직전 한 장 요약 대시보드</h1><p>마스터요약 p.1 &amp; p.52~54 압축 — 조건을 보고 경로를 고르고, 시약을 보고 반응을 떠올린다.</p></div>']
    m = "".join(f'<div class="rt"><div class="rtt">{a}</div><div class="rtd">{b}</div></div>' for a, b in MAP)
    o.append(sec("1", "제22장 한 장 반응 지도", f'<div class="rmap">{m}</div>' + img("map", "마스터요약 p.1 반응 지도", 0.62), "탄소를 친핵체로 만들어 E⁺를 붙인다 (p.1)"))
    chips = "".join(f'<div class="chip" style="--c:{c}"><b>{a}</b><span>→ {b}</span></div>' for a, b, c in ROUTE)
    o.append(sec("2", "엔올(산성) vs 엔올레이트(염기)", table(ENOL_VS, "tb vs") + f'<div class="route"><div class="rl">조건을 보면 경로부터 결정</div>{chips}</div>', "핵심 비교표 (p.1)"))
    r = "".join(f'<div class="rule"><div class="rn">{i}</div><div><div class="rh">{a}</div><div class="rb">{b}</div></div></div>' for i, (a, b) in enumerate(RULES, 1))
    o.append(sec("3", "내가 만든 4대 만능 직관 공식", f'<div class="rules">{r}</div>', "p.1 &amp; p.3, 5, 17, 33"))
    o.append(sec("4", "시약을 보면 반응이 떠오르는 치트시트", table([("시약 및 조건", "하는 일", "최종 결과물", "관련")] + REAGENTS, "tb rg") + f'<p class="note">{REAGENT_NOTE}</p>', "p.52", True))
    # pKa 사다리: 눈금 막대 + 표
    marks = "".join(f'<div class="pm" style="left:{min(97, float(v.split()[0].split("/")[0]) / 36 * 100):.1f}%"><i></i><span>{v.split()[0].split("/")[0]}</span></div>' for _, _, v in PKA)
    half = (len(PKA) + 1) // 2
    rows = [("화합물 (산성 수소 위치)", "pK<sub>a</sub>", "화합물 (산성 수소 위치)", "pK<sub>a</sub>")]
    for i in range(half):
        a = PKA[i]; b = PKA[i + half] if i + half < len(PKA) else ("", "", "")
        rows.append((f"{a[0]} <small>({a[1]})</small>", f"<b>{a[2]}</b>", f"{b[0]} <small>({b[1]})</small>" if b[0] else "", f"<b>{b[2]}</b>"))
    bar = f'<div class="pbar"><div class="pgrad"></div>{marks}<div class="pl l">← 강한 산</div><div class="pl r">약한 산 →</div></div>'
    o.append(sec("5", "꼭 외울 pK<sub>a</sub> 산성도 사다리", bar + table(rows, "tb pk") + f'<p class="note">{PKA_NOTE}</p>', "p.17 &amp; p.52"))
    ten = "".join(f"<li>{t}</li>" for t in TEN)
    o.append(sec("6", "시험장 단골 혼동 쌍 12선 &amp; 시험 직전 10줄", table([("헷갈리는 쌍", "왼쪽 핵심 특징", "오른쪽 핵심 특징")] + PAIRS, "tb pr") + f'<div class="ten"><div class="tenh">시험 직전 머리에 새길 10줄 요약</div><ol>{ten}</ol></div>', "p.53", True))
    toc = ""
    for g in (1, 2, 3):
        nm, desc, col, soft, _ = GRADE[g]
        it = " → ".join(f'<b>{t["rank"]}위</b> 문제 {t["no"]} <small>({t["tag"]})</small>' for t in TOP if t["grade"] == g)
        toc += f'<div class="toc" style="--c:{col};--s:{soft}"><div class="tocn">{nm}</div><div><div class="tocd">{desc}</div><div class="toci">{it}</div></div></div>'
    o.append(sec("7", "출제 확률 순서 핵심 킬러 TOP 10 목차", toc, "p.54"))
    return o[0] + '<div class="cols">' + "".join(o[1:]) + "</div>"


# ───────── TOP 장
def chapter(t):
    nm, desc, col, soft, dots = GRADE[t["grade"]]
    meter = "".join(f'<i class="{"on" if k < dots else ""}"></i>' for k in range(5))
    o = [f'''<article class="ch" style="--c:{col};--s:{soft}">
<header class="hero"><div class="rk"><span>TOP</span><b>{t["rank"]}</b><span>위</span></div>
<div class="ht"><div class="hg">{nm} · {desc}</div><h1>문제 {t["no"]} — {t["title"]}</h1>
<div class="hm"><span class="tg">{t["tag"]}</span><span class="src">{t["src"]}</span><span class="mt">출제 확률 {meter}</span></div></div></header>''']
    o.append('<div class="blk flash"><div class="bh">⚡ 1초 직관 공식 &amp; 내 필기 핵심</div><ul>' + "".join(f"<li>{x}</li>" for x in t["flash"]) + "</ul></div>")
    if t.get("rules"):
        o.append('<div class="r3">' + "".join(f'<div class="r3c"><div class="r3n">{a}</div><div class="r3t">{b}</div><div class="r3b">{c}</div></div>' for a, b, c in t["rules"]) + "</div>")
    if t.get("reverse"):
        o.append('<div class="rev"><div class="revh">↩ 거꾸로 추적</div>' + '<span class="ra">⟵</span>'.join(f'<span class="rs">{x}</span>' for x in t["reverse"]) + "</div>")
    if t.get("ladder"):
        o.append('<div class="lad"><div class="ladh">약산 → 강산</div>' + '<span class="la">&lt;</span>'.join(f'<span class="ls"><b>{v}</b>{n}</span>' for n, v in t["ladder"]) + "</div>")
    if t.get("seesaw"):
        o.append('<div class="see"><div class="sl"><b>강산</b><small>pK<sub>a</sub> 작음 · H⁺를 잘 버림</small><span>→ 약염기</span></div><div class="sbar"></div><div class="sr"><b>약산</b><small>pK<sub>a</sub> 큼 · H⁺를 안 버림</small><span>→ 강염기</span></div></div>')
    p = t["prob"]
    figs = "".join(img(f, "", 1.25) for f in p["fig"])
    o.append(f'<div class="blk prob"><div class="bh">📋 문제 원문 &amp; 구조식 <span class="pens"><i class="pr">빨강</i> 핵심 원자·이탈 <i class="pg">초록</i> 새로 붙는/남는 것 <i class="pb">파랑</i> 날아가는 것·강조</span></div>{figs}<ul>' + "".join(f"<li>{x}</li>" for x in p["items"]) + "</ul></div>")
    if t.get("table"):
        o.append('<div class="blk"><div class="bh">🔁 짝산 분자식 1초 변환 5종 비교표 (금속 Na⁺/Li⁺ 떼고 → H 넣기)</div>' + table(t["table"], "tb sw") + "</div>")
    st = ['<div class="blk story"><div class="bh">🔍 단계별 원자 이동 &amp; 메커니즘 상세 해설</div>']
    if t.get("lead"):
        st.append(f'<p class="lead">{t["lead"]}</p>')
    if t.get("storyfig"):
        st.append(img(t["storyfig"][0], t["storyfig"][1], 1.3))
    st.append('<div class="tl">')
    for a, b, c, fs in t["acts"]:
        fh = "".join(img(f, cap, 1.3) for f, cap in fs)
        st.append(f'<div class="act"><div class="an">{a}</div><div class="ab"><div class="at">{b}</div>{c}{fh}</div></div>')
    st.append("</div></div>")
    o.append("".join(st))
    for a, b, f, c in t.get("bonus", []):
        figs = "".join(img(x, "", 1.0) for x in f.split("|"))
        o.append(f'<div class="blk bonus"><div class="bh">🎁 {a}</div><div class="bt">{b}</div>{figs}{c}</div>')
    rows = "".join(f'<div class="sr"><div class="sk">{a}</div><div class="sv">{b}</div></div>' for a, b in t["sheet"])
    sf = img(t["sheetfig"][0], t["sheetfig"][1], 1.1) if t.get("sheetfig") else ""
    o.append(f'<div class="blk sheet"><div class="shh"><span>시험 답안지용</span> 최종 모범 답안<i class="stamp">정답</i></div>{rows}{sf}</div>')
    o.append("</div></article>")
    return o[0] + '<div class="cols">' + "".join(o[1:])


CSS = open(os.path.join(D, "book.css")).read().replace("{FONT}", FONT)
body = part0() + "".join(chapter(t) for t in TOP)
open(os.path.join(D, "book.html"), "w").write(f'<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>제22장 핵심 킬러 TOP 10 마스터북</title><style>{CSS}</style></head><body>{body}</body></html>')
open(os.path.join(D, "cover.html"), "w").write(f'<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>표지</title><style>{CSS}</style></head><body class="cvb">{cover()}</body></html>')
print("ok", len(TOP))
