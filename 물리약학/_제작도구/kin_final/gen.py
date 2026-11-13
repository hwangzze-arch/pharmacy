# -*- coding: utf-8 -*-
# 9~11주차 화학반응속도론 및 안정성 — 최종 요약본 (7주차 최종 요약과 같은 💡📖📐✍️🧠 형식)
# 실행: python3 gen.py && node render.js "$PWD" out.html "$PWD/out.pdf"
import os, math
HERE = os.path.dirname(os.path.abspath(__file__))
FOOT = '물리약학 9~11주차 · 화학반응속도론 및 안정성 — 최종 요약본'
pages = []


def foot():
    return f'<div class="foot"><span>{FOOT}</span><span>{{PN}}</span></div>'


def J(t):
    return f'<span class="jk">[즉, {t}]</span>'


def sec(emoji, label, html):
    return f'<div class="sec"><div class="sh"><span class="e">{emoji}</span>{label}</div>{html}</div>'


def EXPL(html):
    return sec('📖', '상세 설명', html)


def FORM(html):
    return sec('📐', '중요 공식', html)


def EXAM(html):
    return sec('✍️', '예제 및 풀이', html)


def ana(t, label='🍬 비유'):
    return f'<div class="ana"><span class="t">{label}</span>{t}</div>'


def fbox(f, s=''):
    return f'<div class="fbox"><div class="f">{f}</div>' + (f'<div class="s">{s}</div>' if s else '') + '</div>'


def tbl(head, rows, cls=''):
    h = ''.join(f'<th>{c}</th>' for c in head)
    b = ''.join('<tr>' + ''.join(f'<td>{c}</td>' for c in r) + '</tr>' for r in rows)
    return f'<table class="{cls}"><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table>'


def steps(items):
    out = ''
    for i, it in enumerate(items, 1):
        t, why = (it if isinstance(it, tuple) else (it, ''))
        w = f'<span class="why">👉 왜? {why}</span>' if why else ''
        out += f'<div class="st"><i>Step {i}</i><div>{t}{w}</div></div>'
    return out


def ex(q, st):
    return f'<div class="ex"><div class="q">Q. {q}</div>{steps(st)}</div>'


def warn(t, label='⚠️ 함정'):
    return f'<div class="warn"><b>{label}</b>{t}</div>'


def ul(items):
    return '<ul>' + ''.join(f'<li>{x}</li>' for x in items) + '</ul>'


def fig(svg, cap=''):
    return f'<div class="fig">{svg}' + (f'<div class="cap">{cap}</div>' if cap else '') + '</div>'


def hdr(badge, title, en, part):
    return f'<div class="hdr"><span class="badge">{badge}</span><div><h1>{title}</h1><div class="en">{en}</div></div><span class="part">{part}</span></div>'


PARTS = {0: '읽기 전에', 1: 'PART 1 · 반응 속도 기초', 2: 'PART 2 · 0 · 1 · 2차 반응', 3: 'PART 3 · 복합 반응', 4: 'PART 4 · 온도와 속도',
         5: 'PART 5 · 촉매 · pH · 안정성'}


def concept(part, num, title, en, core, left, right, brain=None, cols='1fr 1fr', dense=False):
    c = f'<div class="core"><span class="lab">💡 핵심 개념</span><span>{core}</span></div>'
    b = f'<div class="brain"><span class="lab">🧠 뇌리에 박히는 한 줄</span><span>{brain}</span></div>' if brain else ''
    pages.append(f'''<section class="page p{part}{' dense' if dense else ''}">{hdr(f'개념 {num:02d}', title, en, PARTS[part])}{c}
<div class="two" style="grid-template-columns:{cols}"><div>{left}</div><div>{right}</div></div>{b}<div style="height:13mm;flex:none"></div>{foot()}</section>''')


def problem(part, n, title, src, q, chs, ans, st, rows=None, brain='', extra=''):
    ch = ''.join(f'<div class="ch">{"①②③④⑤"[i]} {c}</div>' for i, c in enumerate(chs)) if chs else ''
    ct = ''
    if rows:
        ct = '<div class="sh">🔍 보기별 해설</div><table class="ctab"><tbody>' + ''.join(
            f'<tr{" class=ok" if ok else ""}><td class="m">{m}</td><td>{t}</td></tr>' for ok, m, t in rows) + '</tbody></table>'
    b = f'<div class="brain"><span class="lab">🧠 한 줄</span><span>{brain}</span></div>' if brain else ''
    pages.append(f'''<section class="page p{part}">{hdr(f'문제 {n:02d}', title, src, PARTS[part])}
<div class="prob"><div class="pl"><div class="qcard"><span class="lb">문제</span><div class="qq">{q}</div>{ch}</div><div class="mine"><span>✏️ 내 풀이 — 먼저 풀고 오른쪽을 보세요</span></div></div>
<div class="sol"><span class="lb">정답 및 해설</span><div class="ans">정답 : {ans}</div><div class="sh">🪜 Step-by-Step 풀이</div>{steps(st)}{ct}{extra}{b}</div></div>{foot()}</section>''')


# ------------------------------------------------------------ SVG 그림
def _axes(w, h, x0, y0, x1, y1, xl, yl):
    return (f'<line x1="{x0}" y1="{y1}" x2="{x1}" y2="{y1}" stroke="#333" stroke-width="1.3"/>'
            f'<line x1="{x0}" y1="{y0}" x2="{x0}" y2="{y1}" stroke="#333" stroke-width="1.3"/>'
            f'<text x="{x1}" y="{y1 + 15}" font-size="12" text-anchor="end">{xl}</text>'
            f'<text x="{x0 - 5}" y="{y0 + 10}" font-size="12" text-anchor="end">{yl}</text>')


def _curve(f, x0, x1, y0, y1, n=40):
    pts = []
    for i in range(n + 1):
        t = i / n
        pts.append(f'{x0 + (x1 - x0) * t:.1f},{y1 - (y1 - y0) * f(t):.1f}')
    return 'M' + ' L'.join(pts)


def svg_panel(kind, w=150, h=118, yl='[A]', note='', color='#c4501f'):
    x0, y0, x1, y1 = 34, 12, w - 8, h - 22
    f = {'line_down': lambda t: 0.95 - 0.9 * t, 'line_up': lambda t: 0.1 + 0.85 * t,
         'exp': lambda t: 0.95 * math.exp(-3 * t), 'inv': lambda t: 0.95 / (1 + 7 * t),
         'sat': lambda t: 0.9 * (1 - math.exp(-3.5 * t))}[kind]
    return (f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}">{_axes(w, h, x0, y0, x1, y1, "t", yl)}'
            f'<path d="{_curve(f, x0 + 2, x1 - 6, y0, y1)}" fill="none" stroke="{color}" stroke-width="2.4"/>'
            f'<text x="{(x0 + x1) / 2 + 10}" y="{y0 + 12}" font-size="11.5" fill="#b91c1c" font-weight="700">{note}</text></svg>')


def svg_orders():
    cols = [('0차', [('line_down', '[A]', '직선 −k'), ('exp', '', '')]), ]
    rows = [('0차', 'line_down', '[A]', '기울기 −k'), ('1차', 'line_down', 'ln[A]', '기울기 −k'), ('2차', 'line_up', '1/[A]', '기울기 +k')]
    out = '<div style="display:flex;gap:6px;justify-content:center">'
    for name, kind, yl, note in rows:
        out += f'<div style="text-align:center;font-size:12.5px;font-weight:800">{name}<br>{svg_panel(kind, 150, 112, yl, note)}</div>'
    return out + '</div>'


def svg_arrhenius(w=320, h=150):
    x0, y0, x1, y1 = 40, 12, w / 2 - 12, h - 26
    a = (f'{_axes(w, h, x0, y0, x1, y1, "1/T", "log k")}'
         f'<path d="M{x0 + 6},{y0 + 8} L{x1 - 8},{y1 - 8}" stroke="#c4501f" stroke-width="2.4"/>'
         f'<text x="{(x0 + x1) / 2 + 4}" y="{y0 + 16}" font-size="11.5" fill="#b91c1c" font-weight="700">−Ea/2.303R</text>')
    x2 = w / 2 + 40
    b = (f'{_axes(w, h, x2, y0, w - 8, y1, "1/T", "log t½")}'
         f'<path d="M{x2 + 6},{y1 - 8} L{w - 16},{y0 + 8}" stroke="#1d6db1" stroke-width="2.4"/>'
         f'<text x="{(x2 + w) / 2 - 18}" y="{y0 + 16}" font-size="11.5" fill="#1d4ed8" font-weight="700">+Ea/2.303R</text>')
    return f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}">{a}{b}</svg>'


def svg_vph(w=300, h=150):
    x0, y0, x1, y1 = 44, 10, w - 10, h - 24
    xm = x0 + (x1 - x0) * 0.32
    ym = y1 - 18
    return (f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}">{_axes(w, h, x0, y0, x1, y1, "pH", "log kobs")}'
            f'<path d="M{x0 + 6},{y0 + 22} L{xm - 12},{ym} L{xm + 12},{ym} L{x1 - 8},{y0 + 4}" fill="none" stroke="#1d6db1" stroke-width="2.6"/>'
            f'<text x="{x0 + 10}" y="{y0 + 44}" font-size="11.5" fill="#b91c1c" font-weight="700">산촉매 −1</text>'
            f'<text x="{x1 - 92}" y="{y0 + 44}" font-size="11.5" fill="#1d4ed8" font-weight="700">염기촉매 +1</text>'
            f'<text x="{xm - 26}" y="{ym - 8}" font-size="11" fill="#0a6355" font-weight="700">물 k₀ (최저)</text>'
            f'<text x="{xm - 4}" y="{y1 + 14}" font-size="11" fill="#333">pH 3 부근</text></svg>')


def svg_energy(w=320, h=160):
    x0, y0, x1, y1 = 34, 10, w - 10, h - 22

    def hump(hgt, col, dash=''):
        return (f'<path d="M{x0 + 4},{y1 - 40} L{x0 + 60},{y1 - 40} C{x0 + 110},{y1 - 40} {x0 + 115},{y1 - 40 - hgt} {x0 + 150},{y1 - 40 - hgt} '
                f'C{x0 + 185},{y1 - 40 - hgt} {x0 + 195},{y1 - 12} {x0 + 240},{y1 - 12} L{x1 - 6},{y1 - 12}" fill="none" stroke="{col}" stroke-width="2.2" {dash}/>')
    return (f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}">{_axes(w, h, x0, y0, x1, y1, "반응 경로", "E")}'
            + hump(95, '#c62828') + hump(68, '#7c8a95', 'stroke-dasharray="5 4"') + hump(38, '#15803d') +
            f'<text x="{x0 + 160}" y="{y1 - 132}" font-size="11" fill="#c62828" font-weight="700">부촉매 Ea ↑</text>'
            f'<text x="{x0 + 160}" y="{y1 - 104}" font-size="11" fill="#555">촉매 없음</text>'
            f'<text x="{x0 + 160}" y="{y1 - 74}" font-size="11" fill="#15803d" font-weight="700">정촉매 Ea ↓</text>'
            f'<text x="{x0 + 6}" y="{y1 - 46}" font-size="11">반응물</text><text x="{x1 - 50}" y="{y1 - 18}" font-size="11">생성물</text></svg>')


def svg_mm(w=320, h=150):
    x0, y0, x1, y1 = 34, 12, w / 2 - 10, h - 24
    a = (f'{_axes(w, h, x0, y0, x1, y1, "[S]", "V")}<path d="{_curve(lambda t: 0.85 * (6 * t) / (1 + 6 * t), x0 + 2, x1 - 4, y0, y1)}" fill="none" stroke="#8a3ab9" stroke-width="2.4"/>'
         f'<line x1="{x0}" y1="{y1 - (y1 - y0) * 0.85}" x2="{x1}" y2="{y1 - (y1 - y0) * 0.85}" stroke="#999" stroke-dasharray="4 3"/>'
         f'<text x="{x1 - 4}" y="{y1 - (y1 - y0) * 0.85 - 4}" font-size="11" text-anchor="end">Vm</text>')
    x2 = w / 2 + 34
    b = (f'{_axes(w, h, x2, y0, w - 8, y1, "1/[S]", "1/V")}<path d="M{x2 - 20},{y1 - 4} L{w - 14},{y0 + 8}" stroke="#8a3ab9" stroke-width="2.4"/>'
         f'<text x="{x2 + 4}" y="{y1 - 30}" font-size="10.5" fill="#632590" font-weight="700">절편 1/Vm</text>'
         f'<text x="{w - 76}" y="{y0 + 40}" font-size="10.5" fill="#632590" font-weight="700">기울기 Km/Vm</text>'
         f'<text x="{x2 - 26}" y="{y1 + 14}" font-size="10" fill="#b91c1c">−1/Km</text>')
    return f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}">{a}{b}</svg>'


def svg_parallel(w=300, h=140):
    x0, y0, x1, y1 = 36, 12, w - 10, h - 22
    return (f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}">{_axes(w, h, x0, y0, x1, y1, "t", "농도")}'
            f'<path d="{_curve(lambda t: 0.95 * math.exp(-3 * t), x0 + 2, x1 - 6, y0, y1)}" fill="none" stroke="#333" stroke-width="2.2"/>'
            f'<path d="{_curve(lambda t: 0.6 * (1 - math.exp(-3 * t)), x0 + 2, x1 - 6, y0, y1)}" fill="none" stroke="#8a3ab9" stroke-width="2.2"/>'
            f'<path d="{_curve(lambda t: 0.3 * (1 - math.exp(-3 * t)), x0 + 2, x1 - 6, y0, y1)}" fill="none" stroke="#0f8b78" stroke-width="2.2"/>'
            f'<text x="{x0 + 12}" y="{y0 + 14}" font-size="11">P (1차 감소)</text>'
            f'<text x="{x1 - 70}" y="{y1 - (y1 - y0) * 0.6 - 4}" font-size="11" fill="#8a3ab9" font-weight="700">A (k₁)</text>'
            f'<text x="{x1 - 70}" y="{y1 - (y1 - y0) * 0.3 - 4}" font-size="11" fill="#0f8b78" font-weight="700">N (k₂)</text></svg>')


def svg_t90(w=300, h=140):
    x0, y0, x1, y1 = 40, 12, w - 10, h - 22
    out = f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}">{_axes(w, h, x0, y0, x1, y1, "1/T", "log t₉₀")}'
    out += f'<path d="M{x0 + 10},{y1 - 12} L{x1 - 50},{y0 + 26}" stroke="#1d6db1" stroke-width="2.4"/>'
    out += f'<path d="M{x1 - 50},{y0 + 26} L{x1 - 14},{y0 + 8}" stroke="#1d6db1" stroke-width="2.2" stroke-dasharray="5 4"/>'
    for i, lab in enumerate(['70°', '60°', '50°', '40°']):
        x = x0 + 22 + i * 45
        y = y1 - 12 - (y1 - y0 - 38) * (x - x0 - 10) / (x1 - 60 - x0)
        out += f'<circle cx="{x:.0f}" cy="{y:.0f}" r="4" fill="#1d6db1"/><text x="{x - 8:.0f}" y="{y + 16:.0f}" font-size="10">{lab}</text>'
    out += f'<circle cx="{x1 - 14}" cy="{y0 + 8}" r="5" fill="#c62828"/><text x="{x1 - 70}" y="{y0 + 10}" font-size="11" fill="#c62828" font-weight="700">25℃ 외삽</text></svg>'
    return out


# ============================================================ 표지
pages.append(f'''<section class="page cover">
<div class="k">PHYSICAL PHARMACY · WEEK 9–11 · CH.14</div>
<h1>화학반응속도론 및 안정성<br>한 번 읽으면 각인되는 최종 요약본</h1>
<div class="sub">9주차 속도론 (1) · 10주차 Recap + 기출 · 11주차 속도론 (2) · 2-1 Recap + 기출 · 수업 녹취(10/27 · 11/3 · 11/6 · 11/10)를 한 권으로</div>
<div class="how">모든 개념은 이 순서 → <span class="p">💡 핵심 개념</span><span class="p">📖 상세 설명</span><span class="p">📐 중요 공식</span><span class="p">✍️ 예제 및 풀이</span><span class="p">🧠 한 줄 요약</span></div>
<div class="parts">
<div><b>읽기 전에</b>약어 사전 · 수학 5개 (log, ln, 적분, 지수, 역수 그래프)</div>
<div><b>PART 1 · 반응 속도 기초</b>안정성과 속도론 · 속도의 정의 · 속도 법칙 · k와 차수 · k 단위 → 문제 01–02</div>
<div><b>PART 2 · 0·1·2차</b>적분식 · 반감기 · 직선 그래프 · 차수 결정 · t₉₀ → 문제 03–10</div>
<div><b>PART 3 · 복합 반응</b>가역 · 평행 · 정류 상태 · Michaelis-Menten · 혈액 응고 캐스케이드</div>
<div><b>PART 4 · 온도와 속도</b>속도 결정 단계 · Arrhenius · 온도와 반감기 · Q₁₀ → 문제 11–14</div>
<div><b>PART 5 · 촉매 · pH · 안정성</b>촉매 · 특정/일반 산-염기 · 분해 방어 · 가속 시험 · 유사 0차 → 문제 15–20 · 한 장 정리</div>
</div>{foot()}</section>''')

# ============================================================ 읽기 전에 ① 약어
pages.append(f'''<section class="page p0 dense">{hdr('읽기 전에 ①', '약어 · 기호 사전 — 이 문서에 나오는 모든 기호', 'Abbreviations & symbols', PARTS[0])}
<div class="two" style="grid-template-columns:1fr 1fr">
<div>{tbl(['기호', '이름 (읽는 법)', '뜻'], [
    ['k', 'rate constant (레이트 컨스턴트)', '속도 상수 = 비반응속도상수(specific rate constant)'],
    ['k<sub>obs</sub>', 'observed rate constant', '실제로 관찰되는 속도 상수 (pH 등 포함)'],
    ['[A]<sub>0</sub> · [A]<sub>t</sub>', '초기 농도 · t시간 뒤 농도', '대괄호 [ ] = 몰 농도'],
    ['t<sub>1/2</sub>', 'half-life (하프 라이프)', '반감기 — 농도가 절반이 되는 시간'],
    ['t<sub>90</sub>', '티 나인티 · shelf life', '유효기간 — 효력이 <b>90%로</b> 떨어질 때까지'],
    ['E<sub>a</sub>', 'activation energy', '활성화 에너지 — 넘어야 할 언덕 높이'],
    ['A (Arrhenius 식)', 'frequency factor', '아레니우스 상수 (빈도 인자)'],
    ['R', 'gas constant', '기체 상수 8.314 J/mol·K = 1.987 cal/mol·K'],
    ['Q<sub>10</sub>', '큐 텐', '10℃ 올릴 때 속도 상수의 비 k<sub>T+10</sub>/k<sub>T</sub>'],
    ['k<sub>f</sub> · k<sub>r</sub>', 'forward · reverse', '정반응 · 역반응 속도 상수'],
    ['K', 'equilibrium constant', '평형 상수 (대문자!) = k<sub>f</sub>/k<sub>r</sub>'],
    ['K<sub>m</sub> · V<sub>m</sub>', 'Michaelis constant · V max', 'Michaelis-Menten 상수 · 최대 속도'],
    ['K<sub>w</sub>', 'ion product of water', '[H⁺][OH⁻] = 10⁻¹⁴'],
], 'gl')}</div>
<div>{tbl(['용어', '뜻'], [
    ['Rate-determining step', '속도 결정 단계 — 가장 <b>느린</b> 단계'],
    ['Steady-state approximation', '정류 상태 근사법 — 중간체 농도 <b>일정</b> 가정'],
    ['Reversible · Parallel reaction', '가역 반응 · 평행 반응 (복합 반응)'],
    ['Specific acid-base catalysis', '특정 산-염기 촉매 — H⁺ / OH⁻만 촉매 (기울기 ±1)'],
    ['General acid-base catalysis', '일반 산-염기 촉매 — 완충제 성분도 촉매 (기울기 ±1 아님)'],
    ['Nucleophilic · Free radical', '친핵 (가수분해·이성질체화) · 자유 래디컬 (산화·광분해)'],
    ['Accelerated stability test', '가속 안정성 시험 — 고온·고습에서 측정 → 상온 외삽'],
    ['Pseudo-zero-order', '유사(겉보기) 0차 — 현탁액처럼 농도가 포화로 유지'],
    ['Extrapolation', '외삽 — 그래프 직선을 측정 범위 밖으로 연장'],
    ['Saponification', '비누화 — 에스터 + NaOH (단일 단계, 2차)'],
])}
<div class="ana"><span class="t">📌 읽는 요령</span>본문에서 처음 나오는 어려운 말 옆에는 <span class="jk">[즉, ~라는 뜻]</span>이 붙어 있어요. 교수님 말씀은 <b>“ ”</b>로 인용하고 날짜를 붙였어요 (예: 11/10 수업).</div></div>
</div>{foot()}</section>''')

# ============================================================ 읽기 전에 ② 수학
pages.append(f'''<section class="page p0">{hdr('읽기 전에 ②', '수학 겁먹지 않기 — 이 단원에 필요한 수학은 딱 5개', 'Math you actually need', PARTS[0])}
<div class="two" style="grid-template-columns:1fr 1fr">
<div>
{sec('➊', '로그 성질', '<p>log A − log B = <mark>log(A/B)</mark> · log(aⁿ) = n·log a · ln x = <b>2.303</b> log x</p><p>외울 값: <b>ln 2 = 0.693</b>, <b>ln 10 = 2.303 (≈ 2.3)</b>, ln(1/0.9) = <b>0.105</b>, ln 100 = 4.6, log 2 = 0.301</p>')}
{sec('➋', '적분 공식 4개 (교수님 11/3: “어디에 쓰였는지” 연결)', tbl(['공식', '쓰인 곳'], [
    ['∫ 1/x dx = ln x', '1차 적분식'],
    ['∫ 1/x² dx = <b>−</b>1/x', '2차 적분식'],
    ['∫ 1/(ax+b) dx = (1/a) ln(ax+b)', '가역 반응'],
    ['∫₀ᵗ e<sup>−kt</sup> dt = (1/k)(1 − e<sup>−kt</sup>)', '평행 반응'],
]))}
</div>
<div>
{sec('➌', '지수 ↔ 로그', '<p>ln e<sup>−kt</sup> = −kt → ln[A] = −kt + ln[A]<sub>0</sub> ⇔ <mark>[A] = [A]<sub>0</sub>e<sup>−kt</sup></mark></p>')}
{sec('➍', '직선 읽기 y = ax + b', '<p>속도론 그래프는 전부 “무엇을 y·x로 잡으면 <b>직선</b>이 되나” 문제예요. 기울기 a와 절편 b에서 k, E<sub>a</sub>, V<sub>m</sub>, K<sub>m</sub>을 읽어요.</p>')}
{sec('➎', '역수 축 (1/T, 1/[S])', '<p>x축이 1/T면 <b>오른쪽으로 갈수록 온도가 낮아져요</b>. 거꾸로 읽는 습관이 함정 1순위.</p>')}
<div class="ana"><span class="t">🍬 전체 그림</span>9주차 = <b>농도</b>가 속도에 얼마나 기여하나(0·1·2차), 11주차 = <b>k 자체</b>를 바꾸는 요인(온도·촉매·pH) <span class="jk">[즉, 11/10 수업 “두 번째 시간부터는 이 k에 초점을 맞춘 것”]</span>. 둘 다 결국 <b>유효기간 t₉₀</b>을 정하려는 공부.</div>
</div></div>{foot()}</section>''')

# ============================================================ PART 1
concept(1, 1, '속도론을 왜 배우나 — 약의 분해와 유효기간', 'Why kinetics: stability & shelf life',
        '약은 <mark>온도 · 습도 · 빛 · pH</mark>로 분해된다. 분해 속도를 알아야 <mark>유효기간과 보관 조건</mark>을 정한다.',
        EXPL(ul(['분해 요인 4개: 온도, 습도, 빛, pH ' + J('약이 망가지는 원인들'),
                 '분해 속도 → <b>저장 유효 기간</b> 및 <b>저장 조건</b> 확립',
                 '약물을 <b>배합</b>할 경우 <mark>pH</mark>에 따른 분해 속도를 알아야 함',
                 '분해가 문제인 이유: ① <b>효능 상실</b> ② 외형 변화 → <b>복약 순응도</b> ↓ ③ <b>독성 분해산물</b>'])
             + tbl(['약', '안정한 pH', '불안정'], [
                 ['티아민 HCl (비타민 B1)', 'pH 2–3 (산성)', 'pH 6 이상 · pH 8–9 완충액 → 추가 희석 고려'],
                 ['클라불린 (아목시실린)', 'pH 6', 'pH 3.5 등 산성 혼합 조제 → 약효 ↓'],
             ])),
        ana('<b>우유 유통기한</b>: 냉장(저온)이면 길고 상온이면 짧죠. 유통기한을 정하려면 “상하는 속도”부터 알아야 해요 — 그게 속도론.') +
        warn('Summary 1: “약물을 <b>배합</b>할 경우 (온도 / <b>pH</b>)” → 정답 pH. 분해 <b>요인</b>에는 온도도 있지만 “배합” 문장은 pH.') +
        warn('티아민은 <b>산성에서 안정</b>, 클라불린은 <b>산성에서 불안정</b> — 방향이 반대!', '⚠️ 바꿔치기') +
        ana('11/10 수업: “우리가 화학 반응 속도론 및 안정성을 배우는 목적 자체는 <b>안정성 평가 및 유효 기간 산정</b>에 있습니다.”', '🎤 교수님'),
        '분해 속도를 알아야 유효기간이 나온다 — 배합은 pH!')

concept(1, 2, '반응 속도의 정의 — 계수로 나눠야 하나가 된다', 'Reaction rate',
        '반응 속도 = <mark>반응물이 소비되는 속도 = 생성물이 생성되는 속도</mark>. 계수가 있으면 <mark>계수로 나눈다</mark>.',
        EXPL('<p>A → B에서 A는 줄어들어 d[A]/dt가 <b>음수</b> → 앞에 <b>−</b>를 붙여 양수로 만들어요. 생성물은 늘어나니 <b>+</b>.</p>')
        + FORM(fbox('rate = −d[A]/dt = +d[B]/dt', 'A → B')
               + fbox('rate = −(1/a)d[A]/dt = −(1/b)d[B]/dt = (1/c)d[C]/dt = (1/d)d[D]/dt', 'aA + bB → cC + dD'))
        + warn('2A → B면 rate = <b>−½</b> d[A]/dt = d[B]/dt. A가 2배 빨리 줄어드니 2로 나눠 맞춤.'),
        EXAM(ex('2N₂O₅ → 4NO₂ + O₂, t 동안 N₂O₅ 0.4 → 0.2 M. 각 속도는? (11/3 수업)', [
            ('N₂O₅ 소멸속도 = 0.2/t', '줄어든 양 0.2 M ÷ t'),
            ('NO₂ 생성속도 = 0.4/t (2배), O₂ 생성속도 = 0.1/t (½배)', '계수비 2 : 4 : 1'),
            ('<b>전체 반응 속도</b> = 각 속도 ÷ 계수 = <mark>0.1/t</mark>로 모두 같아짐', '½×0.2 = ¼×0.4 = 1×0.1'),
            ('반응 종료 시 NO₂ = <b>0.4 M</b> (교수님 풀이: 0.2 M이 된 시점이 종료)', 'N₂O₅가 0까지 분해된다고 보면 0.8 M — 문제 조건 확인!')]))
        + ana('11/3 수업: “<b>전체 반응속도</b>를 물어보는 것인지 개별 물질의 <b>소멸속도/생성속도</b>를 물어보는 것인지 명확히 구분하셔야 합니다.”', '🎤 교수님'),
        '속도는 계수로 나눠서 하나 — 전체 속도 ≠ 개별 소멸속도!')

concept(1, 3, '속도 법칙 · 속도 상수 · 반응 차수', 'Rate law, rate constant, reaction order',
        '속도 = <mark>k[A]ˣ[B]ʸ</mark>. k는 <mark>농도와 무관</mark>(종류·온도·촉매에 의존), 차수 x, y는 <mark>실험적으로만</mark> 구한다.',
        EXPL(ul(['<b>속도 법칙</b>: 화학 반응 속도를 <b>속도 상수</b>와 <b>반응물 농도</b>의 지수로 표현',
                 '<b>k</b>: 반응물의 종류, <b>온도</b>에 따라 변하지만 반응물의 <b>농도와는 무관</b>',
                 '<b>차수</b>: x = A에 대한 차수, y = B에 대한 차수, x + y = 전체 차수',
                 '계수 ≠ 차수: F₂ + <b>2</b>ClO₂ → 2FClO₂ 의 속도 = k[F₂]¹[ClO₂]<b>¹</b> (전체 2차)'])
             + FORM(fbox('rate = k[A]ˣ[B]ʸ', '지수는 반응식 계수가 아니라 실험값'))),
        tbl(['바꾸면?', '속도', 'k'], [
            ['반응물 농도 ↑', '↑ (0차 제외)', '<b>그대로</b>'],
            ['온도 ↑', '↑', '<b>↑</b> (Arrhenius)'],
            ['정촉매', '↑', '<b>↑</b> (E<sub>a</sub> ↓)'],
            ['부촉매', '↓', '↓'],
        ])
        + warn('“k는 반응물 농도에 영향을 받는다” → <b>X</b> (11/3 OX 4·5번, Summary 1). 농도가 바꾸는 건 속도지 k가 아님.')
        + warn('11/3 교수님 강조: “화학반응속도식은 <b>항상</b> 속도 상수와 반응물 농도의 곱으로만 이루어진다” → <b>X</b>. 촉매(효소) 농도가 들어가거나 생성물이 분모에 들어가기도 함.', '⚠️ 1학년 기출')
        + ana('11/10 OX 5번: “촉매는 반응 속도 상수 값을 변화시킨다” → <b>O</b>.', '🎤 교수님'),
        'k는 농도로는 안 변하고 온도·촉매로만 변한다 — 차수는 실험!')

concept(1, 4, 'k의 단위 — 차수가 단위를 정한다', 'Units of k',
        'k = 속도 ÷ [A]ⁿ → 단위 = <mark>(mol/L)<sup>1−n</sup> · s<sup>−1</sup></mark>. 단위만 보고 차수를 안다.',
        tbl(['차수 n', 'k 단위', '기억법'], [
            ['0차', '<b>mol/L·s</b> (M·s⁻¹)', '속도와 같은 단위'],
            ['1차', '<b>s⁻¹</b> (h⁻¹, day⁻¹ …)', '<mark>시간의 역수만</mark>'],
            ['2차', '<b>L/mol·s</b> (M⁻¹s⁻¹)', '농도가 분모로'],
            ['3차', 'L²/mol²·s (M⁻²s⁻¹)', '초기속도법 예제'],
        ])
        + warn('11/3 OX 8번: “k의 단위가 시간의 역수(s⁻¹)면 2차 반응” → <b>X</b>. M¹⁻ⁿ에서 M이 사라지려면 n = <b>1</b> → 1차.')
        + warn('11/3 OX 2번: “k의 단위는 반응차수와 관련이 없다” → <b>X</b>.', '⚠️ OX'),
        EXAM(ex('A + 2B → C, 실험 1: [A] 0.1, [B] 0.1 → 0.02 / 실험 2: [B]만 0.2 → 0.04 / 실험 3: [A]만 0.2 → 0.08. 속도식과 k는? (9·10주차 예제)', [
            ('1 → 2: [B] ×2 → 속도 ×2 → <b>y = 1</b>', '한 번에 한 물질만 바뀐 쌍을 찾는다'),
            ('1 → 3: [A] ×2 → 속도 ×4 → <b>x = 2</b>', '2ˣ = 4'),
            ('rate = k[A]²[B] (전체 <b>3차</b>)', '계수(A 1, B 2)와 차수(A 2, B 1)가 뒤바뀜!'),
            ('k = 0.02 / (0.1² × 0.1) = <mark>20 L²/mol²·s</mark>', '(mol/L·s) ÷ (mol/L)³')]))
        + ana('2021 Q14처럼 “비반응속도상수 k = 2.3×10⁻³ <b>h⁻¹</b>”만 줘도 1차로 풀라는 뜻 (11/10 수업).', '🎤 교수님'),
        '시간의 역수만 남으면 1차 — 단위가 차수를 말해 준다!')

problem(1, 1, '초기속도법 — 속도식과 k 구하기', '9·10주차 예제 · 11/3 수업',
        'A + 2B → C 반응의 초기 반응 속도 측정 결과가 표와 같을 때, 반응 속도식과 k값과 단위를 구하시오.'
        + tbl(['실험', '[A] (M)', '[B] (M)', 'C 생성속도 (M/s)'], [['1', '0.1', '0.1', '0.02'], ['2', '0.1', '0.2', '0.04'], ['3', '0.2', '0.1', '0.08']]),
        None, 'rate = k[A]²[B], k = 20 M⁻²s⁻¹',
        [('실험 1 → 2: [A] 고정, [B] 2배 → 속도 2배 → [B]에 <b>1차</b>', '2ʸ = 2'),
         ('실험 1 → 3: [B] 고정, [A] 2배 → 속도 4배 → [A]에 <b>2차</b>', '2ˣ = 4'),
         ('C의 계수 1 → C 생성속도 = 반응 속도 = k[A]²[B]', '계수가 1이 아니면 나눠야 함'),
         ('k = 0.02 / (0.01 × 0.1) = 0.02 / 0.001 = <b>20</b>', '2×10⁻² / 10⁻³'),
         ('단위: 전체 3차 → M<sup>1−3</sup>·s⁻¹ = <b>M⁻²s⁻¹</b> (L²/mol²·s)', '11/3 교수님 풀이 그대로')],
        brain='한 변수만 바뀐 쌍 → 배수로 차수 → 실험 1 대입으로 k')

problem(1, 2, '계수가 1이 아닐 때 — 소멸·생성·전체 속도', '10주차 예제 · 11/3 수업',
        '2N₂O₅ → 4NO₂ + O₂ 반응이 t시간 동안 진행되어 종료되었을 때 N₂O₅ 농도가 0.4 M에서 0.2 M이 되었다.<br>'
        '(1) 반응 종료 시 NO₂ 농도 (2) N₂O₅ 소멸속도 (3) NO₂ 생성속도 (4) O₂ 생성속도 (5) 전체 반응 속도', None,
        '(1) 0.4 M (2) 0.2/t (3) 0.4/t (4) 0.1/t (5) 0.1/t',
        [('N₂O₅ 변화량 −0.2 M → 소멸속도 <b>0.2/t</b>', ''),
         ('계수비 2 : 4 : 1 → NO₂ +0.4 M (<b>0.4/t</b>), O₂ +0.1 M (<b>0.1/t</b>)', 'N₂O₅ 2개 없어질 때 NO₂ 4개, O₂ 1개'),
         ('종료 시 NO₂ = 0 + 0.4 = <b>0.4 M</b>', '교수님 풀이: 0.2 M이 된 시점이 “종료”'),
         ('전체 속도 = −½ d[N₂O₅]/dt = ¼ d[NO₂]/dt = d[O₂]/dt = <b>0.1/t</b>', '계수로 정규화(normalizing)')],
        [(False, '함정', 'O₂ 생성속도(0.1/t) = 전체 속도(0.1/t)는 같지만, N₂O₅ 소멸속도(0.2/t)·NO₂ 생성속도(0.4/t)는 전체 속도와 다름'),
         (True, 'OX', '“N₂O₅ 소멸속도 = NO₂ 생성속도” → X (NO₂가 2배)')],
        brain='“전체 반응 속도”는 계수로 나눈 값 하나뿐!')

# ============================================================ PART 2
concept(2, 5, '0차 반응 — 일정한 양씩 줄어든다', 'Zero-order reaction',
        '속도가 <mark>농도와 무관</mark>. [A]가 <mark>직선</mark>으로 감소, 반감기는 <mark>초기 농도에 비례</mark>.',
        FORM(fbox('[A]<sub>t</sub> = −kt + [A]<sub>0</sub>', '−d[A]/dt = k · [A] vs t 직선, 기울기 −k')
             + fbox('t<sub>1/2</sub> = [A]<sub>0</sub> / 2k · t<sub>90</sub> = 0.1[A]<sub>0</sub> / k'))
        + EXPL(ul(['k = 기울기의 절대값 · 단위 mol/L·s',
                   '0차가 나오는 곳: 반응에 <b>금속 표면이나 효소</b>가 필요한 경우 (N₂O 분해는 <b>뜨거운 백금 표면</b>에서만)',
                   '약학 예: <b>현탁액·과포화 약물</b> → 겉보기(유사) 0차 (PART 5)'])),
        fig(svg_panel('line_down', 220, 140, '[A]', '기울기 −k'), '[A] vs t가 직선이면 0차')
        + ana('<b>계산대 3개인 마트</b>: 줄이 10명이든 100명이든 1분에 계산되는 사람 수는 같아요. 계산대 = 금속 표면·효소 자리.')
        + warn('11/3 OX 3번: “0차 반응속도는 반응물의 농도에 비례한다” → <b>X</b> (v = k, 농도 무관).')
        + warn('2017 Q13: “일정한 기울기로 감소” = 0차. y축이 <b>로그가 아닌 농도</b>임을 확인 (11/10 수업).', '⚠️ 기출'),
        '같은 양씩 줄면 0차 — 반감기는 처음 양에 비례!')

concept(2, 6, '1차 반응 — 같은 비율씩 줄어든다', 'First-order reaction',
        '속도 ∝ [A]¹. <mark>ln[A]가 직선</mark>, 반감기 <mark>0.693/k로 초기 농도와 무관</mark>. 약물 분해의 대부분.',
        FORM(fbox('ln[A]<sub>t</sub> = −kt + ln[A]<sub>0</sub> ⇔ [A]<sub>t</sub> = [A]<sub>0</sub>e<sup>−kt</sup>', 'ln[A] vs t 직선, 기울기 −k')
             + fbox('t<sub>1/2</sub> = 0.693 / k · t<sub>90</sub> = 0.105 / k', 'ln 2 = 0.693, ln(1/0.9) = 0.105'))
        + EXPL(ul(['계산 공식 한 줄: <mark>ln([A]<sub>0</sub>/[A]) = kt</mark> (log면 kt/2.303)',
                   '반감기 n번 → (½)ⁿ 남음: 50% → 25% → 12.5%',
                   'k 단위 시간⁻¹ · log[A]로 그리면 기울기 −k/2.303'])),
        fig(svg_panel('exp', 160, 128, '[A]', '지수 곡선') + svg_panel('line_down', 160, 128, 'ln[A]', '기울기 −k'), '[A]는 곡선, ln[A]는 직선')
        + ana('<b>매시간 10%씩 증발하는 향수</b>: 처음엔 많이, 나중엔 조금씩 줄지만 “절반이 되는 시간”은 늘 같아요.')
        + warn('11/3 OX 7번: “초기 농도와 상관없이 반감기가 일정한 반응은 0차” → <b>X</b> (1차).')
        + ana('11/10 수업: “1차 반응의 정의, 시간에 따른 농도 관계식, 반감기, <b>k의 단위까지</b> 머릿속에 있어야 돼요.”', '🎤 교수님'),
        '같은 비율씩 줄면 1차 — 반감기 0.693/k는 처음 양과 무관!')

concept(2, 7, '2차 반응 — 역수가 직선, 반감기는 반비례', 'Second-order reaction',
        '속도 ∝ [A]². <mark>1/[A]가 기울기 +k 직선</mark>, 반감기 <mark>1/k[A]₀로 초기 농도에 반비례</mark>.',
        FORM(fbox('1/[A]<sub>t</sub> = kt + 1/[A]<sub>0</sub>', '∫1/x² dx = −1/x → 부호 정리하면 +kt')
             + fbox('t<sub>1/2</sub> = 1 / (k[A]<sub>0</sub>)', '[A]=½[A]₀ 대입 → 2/[A]₀ − 1/[A]₀ = kt½'))
        + EXPL(ul(['[A] vs t는 <b>반비례 곡선</b> ([A] = [A]₀/(kt[A]₀ + 1))',
                   '단위 L/mol·s',
                   '대표 예: <b>비누화</b> (에틸아세테이트 + NaOH) — <b>단일 단계 반응(소반응)</b>이라 반응식 계수가 그대로 차수 → v = k[에스터][OH⁻] (11/10 수업)'])),
        fig(svg_panel('inv', 160, 128, '[A]', '반비례 곡선') + svg_panel('line_up', 160, 128, '1/[A]', '기울기 +k'), '2차만 기울기가 양수')
        + warn('2020 Q13: 두 반응물 초기 농도가 같은 a → t<sub>1/2</sub> = 1/ka → <b>a에 반비례</b> (a²에 반비례 아님).')
        + ana('2차는 두 분자가 <b>만나야</b> 반응 — 농도가 낮아지면 만날 확률이 확 줄어 반감기가 점점 길어져요.'),
        '역수가 직선이면 2차 — 반감기는 처음 양에 반비례!')

concept(2, 8, '0 · 1 · 2차 한 표 + 차수 결정법', 'Summary table & determining order',
        '<mark>그대로 · 로그 · 역수</mark> 중 무엇이 직선인가 = 차수. 반감기와 [A]₀: <mark>비례 · 무관 · 반비례</mark>.',
        tbl(['차수', '속도식', '적분식', '반감기', 'k 단위'], [
            ['0차', '−d[A]/dt = k', '[A] = −kt + [A]₀', '[A]₀/2k', 'mol/L·s'],
            ['1차', '−d[A]/dt = k[A]', 'ln[A] = −kt + ln[A]₀', '0.693/k', 's⁻¹'],
            ['2차', '−d[A]/dt = k[A]²', '1/[A] = kt + 1/[A]₀', '1/k[A]₀', 'L/mol·s'],
        ])
        + tbl(['항목', '0차', '1차', '2차'], [
            ['감소 모양', '직선', '지수적', '반비례'],
            ['속도와 농도', '변하지 않음', '1제곱에 비례', '2제곱에 비례'],
            ['반감기 vs [A]₀', '<mark>비례</mark>', '<mark>무관</mark>', '<mark>반비례</mark>'],
            ['직선 그래프', '[A] vs t', 'ln[A] vs t', '1/[A] vs t'],
        ]),
        fig(svg_orders(), '그래프법 — 직선이 되는 축 = 차수')
        + EXPL(ul(['<b>대입법</b>: 데이터를 각 적분식에 넣어 k가 일정한 차수',
                   '<b>그래프법</b>: 직선이 되는 그래프 (아조메탄 분해: ln P vs t 직선 → 1차, k = 2.55×10⁻³ s⁻¹)',
                   '<b>반감기법</b>: [A]₀를 바꿔 반감기 비교 — 2025 Q13 (11/10 수업)']))
        + warn('Summary 2 선택형: 1차는 농도의 (<b>1</b>)제곱에 (<b>비례함</b>), 2차는 (<b>반비례</b>)로 감소, 반감기 (<b>반비례</b>).'),
        '그대로·로그·역수 — 비례·무관·반비례!')

problem(2, 3, '1차 반응 — 20일 후 lnC', '2026 Q13 · 11/10 수업 풀이',
        '25℃에서 반감기가 6.93일인 약물 A의 분해는 1차 반응을 따른다. 초기농도가 100 mg/mL일 때, 20일 후 약물 농도가 C mg/mL이다. lnC는? (단, ln2 = 0.693, ln100 = 4.6)',
        ['1.3', '2.3', '2.6', '3.9', '4.6'], '③ 2.6',
        [('1차 → t<sub>1/2</sub> = 0.693/k → k = 0.693/6.93 = <b>0.1 day⁻¹</b>', ''),
         ('ln C = −kt + ln 100 = −0.1 × 20 + 4.6', '1차 적분식'),
         ('= −2 + 4.6 = <b>2.6</b>', '검산: 20일 ≈ 반감기 2.9번 → C ≈ 13.5, ln 13.5 ≈ 2.6')],
        brain='반감기 → k → 적분식 대입, 세 줄이면 끝')

problem(2, 4, '그래프로 차수 판단 (반감기법)', '2025 Q13 · 11/10 수업 풀이',
        '25℃, 서로 다른 초기농도(600, 400)에서 시간에 따른 약물 A의 농도 변화 그래프가 주어졌다. 600 → 300, 300 → 150, 400 → 200, 200 → 100이 모두 약 30일 걸렸다. 분해반응 차수는?',
        ['0차', '1차', '2차', '3차', '유사 0차'], '② 1차',
        [('반감기를 본다: 일정한가? 늘어나나? 줄어드나?', '교수님: “반감기를 한번 보시면 돼요.”'),
         ('600 → 300, 300 → 150 모두 <b>30일</b> / 400 → 200, 200 → 100도 <b>30일</b>', ''),
         ('반감기가 <b>초기 농도와 무관하게 일정</b> → 1차', '0차라면 반감기가 농도에 비례해 점점 짧아지고, 2차라면 점점 길어짐')],
        [(False, '①', '0차 — 직선 감소여야 함, 그래프는 곡선'), (True, '②', '1차 — 반감기 일정 ✓'),
         (False, '③', '2차 — 반감기가 점점 길어져야 함'), (False, '⑤', '유사 0차 — 현탁액처럼 농도 유지될 때 (문제 20)')],
        brain='반감기가 일정하면 1차 — 표를 머릿속에!')

problem(2, 5, '두 약의 반감기 비교', '2024 Q13 · 11/10 수업 풀이',
        '25℃에서 약물 A와 B는 각각 1차 반응으로 분해된다. A의 1차 속도상수 0.1×10⁻⁵ h⁻¹, B는 1×10⁻⁵ h⁻¹일 때 A의 반감기는?',
        ['B의 반감기 × 0.693', 'B의 반감기 × 2', 'B의 반감기 × 2.303', 'B의 반감기 × 5', 'B의 반감기 × 10'], '⑤ B의 반감기 × 10',
        [('k<sub>A</sub> = 1×10⁻⁶, k<sub>B</sub> = 1×10⁻⁵ → k<sub>A</sub> = k<sub>B</sub>/10', ''),
         ('t<sub>1/2</sub> = 0.693/k → k에 반비례', '1차 반감기는 농도와 무관하지만 <b>k</b>에는 영향'),
         ('A의 반감기 = B × <b>10</b>', '0.693, 2.303은 공식 속 숫자로 만든 함정')],
        brain='k가 1/10이면 반감기는 10배')

problem(2, 6, '1차 반응 — 10% 분해까지 시간 (t₉₀)', '2024 Q14 · 11/10 수업 풀이',
        '25℃에서 1차 반응으로 분해되는 약물의 k = 1.05×10⁻⁵ h⁻¹이다. 초기농도 200 unit/mL가 180 unit/mL가 될 때까지 걸리는 시간(h)은? (단, ln(200/180) = 0.105)',
        ['100', '1,000', '10,000', '100,000', '1,000,000'], '③ 10,000',
        [('ln 180 = −kt + ln 200 → kt = ln(200/180) = 0.105', '1차 적분식'),
         ('t = 0.105 / (1.05×10⁻⁵) = 0.1×10⁵ = <b>10⁴ h</b>', '1.05×10⁻¹ / 1.05×10⁻⁵'),
         ('180/200 = 90% → 이게 바로 <b>t₉₀</b> = 0.105/k', '유효기간 공식')],
        brain='90% 남을 때까지 = 0.105/k')

problem(2, 7, '1차 반응 — 농도가 1/10이 되는 시간', '2021 Q14 · 11/10 수업 풀이',
        '25℃에서 어떤 주사제의 분해반응 비반응속도상수 k는 2.3×10⁻³ h⁻¹이다. 초기농도 5 mg/mL가 0.5 mg/mL로 되는 데 걸리는 시간(h)은? (단, lnA = 2.3 logA)',
        ['1.0×10²', '2.0×10²', '6.9×10²', '1.0×10³', '1.0×10⁴'], '④ 1.0×10³',
        [('단위 h⁻¹ → <b>1차</b>', '교수님: “단위만 보고도 몇 차인지 알 수 있는지를 묻는 것”'),
         ('kt = ln(5/0.5) = ln 10 = 2.3 log 10 = <b>2.3</b>', ''),
         ('t = 2.3 / 2.3×10⁻³ = <b>10³ h</b>', '비반응속도상수 = 속도 상수 (specific rate constant)')],
        brain='단위가 h⁻¹이면 1차 — ln 10 = 2.3')

problem(2, 8, '비누화 반응의 반감기', '2020 Q13 · 11/10 수업 풀이',
        'CH₃COOC₂H₅ + NaOH → CH₃COONa + C₂H₅OH. 에틸아세테이트와 NaOH의 초기농도가 각각 a로 같을 때 반감기와 a의 관계로 옳은 것은?',
        ['t½은 a와 관계없다', 't½은 a에 비례한다', 't½은 a에 반비례한다', 't½은 a²에 비례한다', 't½은 a²에 반비례한다'], '③ a에 반비례',
        [('비누화 = <b>단일 단계 반응(소반응)</b> → 반응식 계수 = 차수', '교수님: “국시에 가실 때쯤이면 아시게 될 거고”'),
         ('v = k[에스터][OH⁻] → <b>2차</b>', ''),
         ('농도가 같으면 t<sub>1/2</sub> = 1/(ka) → <b>a에 반비례</b>', '⑤ a²에 반비례는 3차 반감기 함정')],
        brain='비누화 = 단일 단계 2차 = 반감기 반비례')

problem(2, 9, '일정한 기울기로 감소 → 몇 차?', '2017 Q13 · 11/10 수업 풀이',
        '어떤 과포화된 약물의 유효기간을 결정하려고 한다. 일정한 온도에서 시간에 따른 약물의 함량이 일정한 기울기로 감소하였다. 이 약물의 분해과정은 몇 차 반응인가?',
        ['0차 반응', '1차 반응', '2차 반응', '유사 1차 반응', '유사 2차 반응'], '① 0차 반응',
        [('“일정한 기울기” + y축이 <b>농도</b>(로그 아님) → 직선', '수업 중 학생들이 1차로 헷갈렸던 문제'),
         ('[A] = −kt + [A]₀ → <b>0차</b>', ''),
         ('0차 = 반응 속도는 반응물 농도에 영향을 받지 않는다', '교수님이 정리한 0차 설명'),
         ('과포화 → 녹은 만큼 계속 보충 → 농도 일정 → 겉보기 0차', '문제 20(현탁액)과 같은 원리')],
        brain='농도 그래프가 직선 = 0차 (로그 축인지 꼭 확인)')

problem(2, 10, '표에서 shelf life 구하기', '2021 Q13 · 11/10 수업 풀이',
        '실온 보관 시 농도: 0개월 100, 0.5개월 99, 1개월 98, 2개월 96, 3개월 94 (mg/mL). 실온에서의 shelf life(t₉₀, 개월)는?',
        ['5', '10', '20', '50', '100'], '① 5',
        [('0.5개월마다 1씩, 한 달에 <b>2 mg/mL</b>씩 일정 감소 → <b>0차</b>', '교수님: “0.5, 1.5를 넣어 헷갈리게 한 트릭”'),
         ('t₉₀ = 90 mg/mL까지 = 10 감소', '90% <b>남을 때</b>'),
         ('t = 10 / 2 = <b>5개월</b>', '1차로 풀어도 ≈ 5.1개월 — 초반 10%에선 차이 작음')],
        brain='같은 양씩 줄면 0차 — t₉₀ = 0.1[A]₀/k')

exec(open(os.path.join(HERE, 'gen_b.py'), encoding='utf-8').read())

total = len(pages)
html = ''.join(p.replace('{PN}', f'{i} / {total}') for i, p in enumerate(pages, 1))
css = open(os.path.join(HERE, 'style.css'), encoding='utf-8').read()
open(os.path.join(HERE, 'out.html'), 'w', encoding='utf-8').write(
    f'<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>화학반응속도론 및 안정성 최종 요약본</title><style>{css}</style></head><body>{html}</body></html>')
print(total, 'pages')
