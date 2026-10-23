# -*- coding: utf-8 -*-
# 공통 헬퍼 (v3: 사고의 흐름 + 내 필기)
import os, math
HERE = os.path.dirname(os.path.abspath(__file__))
FOOT = '물리약학 4–6주차 · 확산 (Diffusion) — 마스터 요약본'
pages = []


def foot():
    return f'<div class="foot"><span>{FOOT}</span><span>{{PN}}</span></div>'


def J(t):
    return f'<span class="jk">[즉, {t}]</span>'


def sec(emoji, label, html):
    return f'<div class="sec"><div class="sh"><span class="e">{emoji}</span>{label}</div>{html}</div>'


def EXPL(h): return sec('📖', '상세 설명', h)
def FORM(h): return sec('📐', '중요 공식', h)
def EXAM(h): return sec('✍️', '예제 및 풀이', h)


def ana(t, label='🍬 비유'):
    return f'<div class="ana"><span class="t">{label}</span>{t}</div>'


def fbox(f, s=''):
    return f'<div class="fbox"><div class="f">{f}</div>' + (f'<div class="s">{s}</div>' if s else '') + '</div>'


def tbl(head, rows, cls=''):
    h = ''.join(f'<th>{c}</th>' for c in head)
    b = ''.join('<tr>' + ''.join(f'<td>{c}</td>' for c in r) + '</tr>' for r in rows)
    return f'<table class="{cls}"><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table>'


def warn(t, label='⚠️ 함정'):
    return f'<div class="warn"><b>{label}</b>{t}</div>'


def ul(items):
    return '<ul>' + ''.join(f'<li>{x}</li>' for x in items) + '</ul>'


def fig(svg, cap=''):
    return f'<div class="fig">{svg}' + (f'<div class="cap">{cap}</div>' if cap else '') + '</div>'


def img(name, cap='', h=None):
    st = f' style="max-height:{h}px"' if h else ''
    return f'<div class="img"><img src="img/{name}"{st}>' + (f'<div class="cap">{cap}</div>' if cap else '') + '</div>'


def mynote(html, label='📝 내 필기'):
    return f'<div class="mynote"><span class="nl">{label}</span>{html}</div>'


def fixnote(t):
    return f'<div class="fixnote"><b>🔧 바로잡기</b>{t}</div>'


KIND = {'see': ('👀', '단서'), 'ask': ('🤔', '질문'), 'link': ('💡', '연결'), 'calc': ('🧮', '계산'), 'chk': ('🔍', '함정 체크'), 'done': ('✅', '결론')}


def flow(items):
    out = ''
    for k, t in items:
        ic, tg = KIND[k]
        out += f'<div class="fl k-{k}"><span class="ic">{ic}</span><div class="tx"><span class="tg">{tg}</span>{t}</div></div>'
    return f'<div class="flow">{out}</div>'


def ex(q, items):
    return f'<div class="ex"><div class="q">Q. {q}</div>{flow(items)}</div>'


def hdr(badge, title, en, part):
    return f'<div class="hdr"><span class="badge">{badge}</span><div><h1>{title}</h1><div class="en">{en}</div></div><span class="part">{part}</span></div>'


PARTS = {0: '읽기 전에', 1: 'PART 1 · 확산 기초', 2: 'PART 2 · 얇은 막 · 투과도', 3: 'PART 3 · 다층 · 흡수', 4: 'PART 4 · 경피 패치', 5: '마무리'}


def concept(part, num, title, en, core, left, right, brain=None, cols='1fr 1fr', cont=False, dense=False):
    badge = f'개념 {num:02d}' + (' (계속)' if cont else '')
    c = '' if cont else f'<div class="core"><span class="lab">💡 핵심 개념</span><span>{core}</span></div>'
    b = f'<div class="brain"><span class="lab">🧠 뇌리에 박히는 한 줄</span><span>{brain}</span></div>' if brain else ''
    pages.append(f'''<section class="page p{part}{' dense' if dense else ''}">{hdr(badge, title, en, PARTS[part])}{c}
<div class="two" style="grid-template-columns:{cols}"><div>{left}</div><div>{right}</div></div>{b}<div style="height:13mm;flex:none"></div>{foot()}</section>''')


def problem(part, n, title, src, q, chs, ans, fl, rows=None, brain='', extra='', left_extra='', dense=False, mine=True):
    ch = ''.join(f'<div class="ch">{"①②③④⑤"[i]} {c}</div>' for i, c in enumerate(chs)) if chs else ''
    ct = ''
    if rows:
        ct = '<div class="sh">🔍 보기별 해설</div><table class="ctab"><tbody>' + ''.join(
            f'<tr{" class=ok" if ok else ""}><td class="m">{m}</td><td>{t}</td></tr>' for ok, m, t in rows) + '</tbody></table>'
    b = f'<div class="brain"><span class="lab">🧠 한 줄</span><span>{brain}</span></div>' if brain else ''
    mn = '<div class="mine"><span>✏️ 내 풀이 — 먼저 풀고 오른쪽을 보세요</span></div>' if mine else ''
    pages.append(f'''<section class="page p{part}{' dense' if dense else ''}">{hdr(f'문제 {n:02d}', title, src, PARTS[part])}
<div class="prob"><div class="pl"><div class="qcard"><span class="lb">문제</span><div class="qq">{q}</div>{ch}</div>{left_extra}{mn}</div>
<div class="sol"><span class="lb">정답 및 해설</span><div class="ans">정답 : {ans}</div><div class="sh">🧭 사고의 흐름 — 문제를 보면 이렇게 생각해요</div>{flow(fl)}{ct}{extra}{b}</div></div>{foot()}</section>''')


# ------------------------------------------------------------ SVG
def svg_steady(xi=False, w=360, h=190):
    xs = '<line x1="205" y1="22" x2="205" y2="150" stroke="#1d6fb5" stroke-width="2" stroke-dasharray="5 4"/><text x="186" y="166" font-size="11" fill="#1d6fb5" font-weight="700">특정 위치 xᵢ</text>' if xi else ''
    return f'''<svg viewBox="0 0 360 190" width="{w}" height="{h}">
<rect x="20" y="20" width="90" height="130" fill="#fdf1d6"/><rect x="110" y="20" width="160" height="130" fill="#f1eafb"/><rect x="270" y="20" width="80" height="130" fill="#e7f0fb"/>
<text x="65" y="38" font-size="11.5" text-anchor="middle" font-weight="800" fill="#9a6400">공여체</text><text x="65" y="53" font-size="10" text-anchor="middle">C = C₀ 일정</text>
<text x="190" y="38" font-size="11.5" text-anchor="middle" font-weight="800" fill="#6a2595">막 (두께 h)</text>
<text x="310" y="38" font-size="11.5" text-anchor="middle" font-weight="800" fill="#134e83">수용체</text><text x="310" y="53" font-size="10" text-anchor="middle">C ≈ 0 (싱크)</text>
<line x1="20" y1="65" x2="110" y2="65" stroke="#222" stroke-width="2.5"/>
<path d="M110,65 C114,110 125,140 140,150" fill="none" stroke="#64748b" stroke-width="2"/>
<path d="M110,65 C150,110 210,135 270,150" fill="none" stroke="#f08c00" stroke-width="2.2"/>
<line x1="110" y1="65" x2="270" y2="150" stroke="#0f8b78" stroke-width="2.6"/>
<line x1="270" y1="150" x2="350" y2="150" stroke="#e03131" stroke-width="4"/>
<text x="140" y="146" font-size="10" fill="#64748b">t = 0</text><text x="215" y="128" font-size="10" fill="#c26a00">tᵢ (곡선)</text><text x="208" y="92" font-size="10.5" fill="#0a6355" font-weight="700">정상상태 (직선)</text>
{xs}<text x="180" y="182" font-size="10.5" text-anchor="middle" fill="#555">시간이 지나면 곡선이 펴져 직선 = 정상상태 (dC/dx 일정, ∂C/∂t = 0)</text></svg>'''


def svg_kjump(w=340, h=180):
    return f'''<svg viewBox="0 0 340 180" width="{w}" height="{h}">
<rect x="15" y="15" width="100" height="130" fill="#fdf1d6"/><rect x="115" y="15" width="135" height="130" fill="#f1eafb"/><rect x="250" y="15" width="80" height="130" fill="#e7f0fb"/>
<line x1="15" y1="95" x2="115" y2="95" stroke="#222" stroke-width="2.5"/><text x="50" y="88" font-size="12" font-weight="800">C<tspan font-size="9" dy="3">d</tspan></text>
<line x1="115" y1="95" x2="115" y2="40" stroke="#e03131" stroke-width="2" stroke-dasharray="4 3"/><text x="72" y="64" font-size="11" fill="#e03131" font-weight="800">K배 점프</text>
<line x1="115" y1="40" x2="250" y2="140" stroke="#7c3aed" stroke-width="2.8"/><line x1="250" y1="140" x2="330" y2="140" stroke="#222" stroke-width="2.5"/>
<text x="120" y="34" font-size="11.5" fill="#6a2595" font-weight="800">C₁ = K·C<tspan font-size="9" dy="3">d</tspan></text><text x="254" y="133" font-size="11" fill="#134e83" font-weight="800">C₂ = K·Cᵣ ≈ 0</text>
<text x="65" y="162" font-size="11" text-anchor="middle" font-weight="700" fill="#9a6400">공여체 (Donor)</text><text x="182" y="162" font-size="11" text-anchor="middle" font-weight="700" fill="#6a2595">막 (두께 h)</text><text x="290" y="162" font-size="11" text-anchor="middle" font-weight="700" fill="#134e83">수용체 (Receptor)</text>
</svg>'''


def svg_lag(w=330, h=180, slope_lbl='기울기 = P·S·C<tspan font-size="8" dy="2">d</tspan>', tl='t<tspan font-size="8" dy="2">L</tspan>'):
    return f'''<svg viewBox="0 0 330 180" width="{w}" height="{h}">
<line x1="35" y1="150" x2="320" y2="150" stroke="#333"/><line x1="35" y1="150" x2="35" y2="12" stroke="#333"/>
<text x="296" y="167" font-size="11">시간 t</text><text x="4" y="14" font-size="11">누적 M</text>
<path d="M35,150 C70,149 95,140 120,122" fill="none" stroke="#f08c00" stroke-width="2.6"/>
<line x1="120" y1="122" x2="300" y2="30" stroke="#0f8b78" stroke-width="2.8"/>
<line x1="81" y1="150" x2="120" y2="122" stroke="#0f8b78" stroke-width="1.6" stroke-dasharray="4 3"/>
<circle cx="81" cy="150" r="3.5" fill="#e03131"/><text x="70" y="168" font-size="11" fill="#e03131" font-weight="800">{tl}</text>
<text x="52" y="135" font-size="10.5" fill="#c26a00">비정상 (곡선)</text><text x="200" y="62" font-size="11" fill="#0a6355" font-weight="700">정상상태 (직선)</text><text x="200" y="78" font-size="10.5" fill="#0a6355">{slope_lbl}</text>
</svg>'''


def svg_multi(w=340, h=170):
    return f'''<svg viewBox="0 0 340 170" width="{w}" height="{h}">
<rect x="10" y="15" width="70" height="120" fill="#fdf1d6"/><rect x="80" y="15" width="90" height="120" fill="#efe4f8"/><rect x="170" y="15" width="90" height="120" fill="#f5edfb"/><rect x="260" y="15" width="70" height="120" fill="#e7f0fb"/>
<polyline points="10,35 80,35 170,115 260,128 330,128" fill="none" stroke="#7c3aed" stroke-width="2.8"/>
<text x="45" y="150" font-size="11" text-anchor="middle" font-weight="700">공여체</text><text x="125" y="150" font-size="11" text-anchor="middle" font-weight="700">층1 (R₁ 큼)</text><text x="215" y="150" font-size="11" text-anchor="middle" font-weight="700">층2 (R₂ 작음)</text><text x="295" y="150" font-size="11" text-anchor="middle" font-weight="700">수용체</text>
<text x="95" y="60" font-size="10.5" fill="#6a2595" font-weight="700">가파름</text><text x="190" y="108" font-size="10.5" fill="#6a2595" font-weight="700">완만</text>
<text x="170" y="166" font-size="10.5" text-anchor="middle" fill="#555">J는 모든 층에서 같음 → 저항 큰 층에서 농도가 크게 떨어짐</text></svg>'''


def svg_stag(mode='all', w=360, h=185):
    # 5구간: 수층 | 정적층 ha | 막 hm | 정적층 ha | 수층
    xs = [10, 70, 130, 230, 290, 350]
    if mode == 'mem':
        pts = '10,40 70,40 130,46 130,30 230,140 230,146 290,152 350,152'
        cap = '막 제어 : 농도가 거의 막 안에서 떨어짐 → J = Pₘ·C₁'
    elif mode == 'aq':
        pts = '10,40 70,40 130,92 130,86 230,96 230,100 290,152 350,152'
        cap = '수층 제어 : 양쪽 정적층에서 떨어짐 (막 안은 평평) → J = Pₐ·C₁/2'
    else:
        pts = '10,40 70,40 130,70 130,52 230,128 230,134 290,152 350,152'
        cap = 'C₁ 수층 → C₂ 정적층 끝 → C₃ 막 입구(K배) → C₄ 막 출구 → C₅ 수용체(≈0)'
    lab = ''
    if mode == 'all':
        lab = '<text x="20" y="34" font-size="11" font-weight="800">C₁</text><text x="104" y="82" font-size="11" font-weight="800">C₂</text><text x="134" y="48" font-size="11" font-weight="800" fill="#6a2595">C₃</text><text x="208" y="126" font-size="11" font-weight="800" fill="#6a2595">C₄</text><text x="320" y="146" font-size="11" font-weight="800">C₅</text>'
    return f'''<svg viewBox="0 0 360 185" width="{w}" height="{h}">
<rect x="10" y="20" width="60" height="135" fill="#e7f0fb"/><rect x="70" y="20" width="60" height="135" fill="#f3f7fc" stroke="#9fb6d3" stroke-dasharray="4 3"/><rect x="130" y="20" width="100" height="135" fill="#efe4f8"/><rect x="230" y="20" width="60" height="135" fill="#f3f7fc" stroke="#9fb6d3" stroke-dasharray="4 3"/><rect x="290" y="20" width="60" height="135" fill="#e7f0fb"/>
<text x="40" y="14" font-size="10" text-anchor="middle">수층(공여)</text><text x="100" y="14" font-size="10" text-anchor="middle">정적층 hₐ</text><text x="180" y="14" font-size="10" text-anchor="middle">막 hₘ</text><text x="260" y="14" font-size="10" text-anchor="middle">정적층 hₐ</text><text x="320" y="14" font-size="10" text-anchor="middle">수층(수용)</text>
<polyline points="{pts}" fill="none" stroke="#c4501f" stroke-width="2.8"/>{lab}
<text x="180" y="176" font-size="10.5" text-anchor="middle" fill="#555">{cap}</text></svg>'''


def svg_ph(w=340, h=185):
    def curve(pka, acid=True):
        pts = []
        for i in range(0, 121):
            ph = i / 10
            f = 1 / (1 + 10 ** (ph - pka)) if acid else 1 / (1 + 10 ** (pka - ph))
            pts.append(f'{40 + ph * 24:.1f},{150 - f * 120:.1f}')
        return ' '.join(pts)
    ticks = ''.join(f'<text x="{40 + p * 24}" y="166" font-size="9.5" text-anchor="middle">{p}</text>' for p in range(0, 13, 2))
    return f'''<svg viewBox="0 0 340 185" width="{w}" height="{h}">
<line x1="40" y1="150" x2="330" y2="150" stroke="#333"/><line x1="40" y1="150" x2="40" y2="25" stroke="#333"/>{ticks}
<text x="2" y="34" font-size="10">100%</text><text x="10" y="94" font-size="10">50%</text><text x="24" y="153" font-size="10">0</text>
<line x1="40" y1="90" x2="330" y2="90" stroke="#ccc" stroke-dasharray="3 3"/>
<rect x="76" y="25" width="24" height="125" fill="#fdecec" opacity=".7"/><rect x="220" y="25" width="24" height="125" fill="#e7f0fb" opacity=".7"/>
<text x="88" y="22" font-size="10" text-anchor="middle" fill="#b42318" font-weight="700">위 pH 2</text><text x="232" y="22" font-size="10" text-anchor="middle" fill="#134e83" font-weight="700">소장 pH 8</text>
<polyline points="{curve(5, True)}" fill="none" stroke="#c4501f" stroke-width="2.6"/><polyline points="{curve(9, False)}" fill="none" stroke="#1d6fb5" stroke-width="2.6"/>
<text x="108" y="44" font-size="10.5" fill="#c4501f" font-weight="800">약산 pKa 5</text><text x="262" y="44" font-size="10.5" fill="#1d6fb5" font-weight="800">약염기 pKa 9</text>
<text x="185" y="182" font-size="10.5" text-anchor="middle" fill="#555">세로 = 비해리형(분자형) 비율 · 두 곡선 모두 pH = pKa에서 50%</text></svg>'''


def svg_curv(w=330, h=150):
    return f'''<svg viewBox="0 0 330 150" width="{w}" height="{h}">
<path d="M15,40 Q60,130 105,40" fill="none" stroke="#0f8b78" stroke-width="2.8"/><text x="60" y="140" font-size="11" text-anchor="middle" font-weight="700" fill="#0a6355">∂²C/∂x² &gt; 0 오목 ∪</text>
<line x1="125" y1="110" x2="205" y2="45" stroke="#333" stroke-width="2.8"/><text x="165" y="140" font-size="11" text-anchor="middle" font-weight="700">= 0 직선</text>
<path d="M225,110 Q270,20 315,110" fill="none" stroke="#c4501f" stroke-width="2.8"/><text x="270" y="140" font-size="11" text-anchor="middle" font-weight="700" fill="#933610">&lt; 0 볼록 ∩</text>
<text x="165" y="18" font-size="11" text-anchor="middle" fill="#555">휘어진 정도(2번 미분) = 그 지점에 약이 쌓이나(+) 빠지나(−)</text></svg>'''
