# -*- coding: utf-8 -*-
# 12~13주차 계면현상 — 최종 요약본 (속도론 최종 요약과 같은 💡📖📐✍️🧠 형식 · 라벤더 표지)
# 실행: python3 gen.py && node render.js "$PWD" out.html "$PWD/out.pdf"
import os, math
HERE = os.path.dirname(os.path.abspath(__file__))
FOOT = '물리약학 12~13주차 · 계면현상 — 최종 요약본'
pages = []
exec(open(os.path.join(HERE, 'base.py'), encoding='utf-8').read())

PARTS = {0: '읽기 전에', 1: 'PART 1 · 표면장력과 표면자유에너지', 2: 'PART 2 · 부착 · 응집 · 퍼짐', 3: 'PART 3 · 액체계면 흡착 · 계면활성제',
         4: 'PART 4 · 고체계면 흡착', 5: 'PART 5 · 습윤 · 전기적 성질'}
g = lambda s: f'γ<sub>{s}</sub>'


# ------------------------------------------------------------ SVG 그림
def svg_forces(w=330, h=150):
    def mol(cx, cy, dirs, c):
        s = f'<circle cx="{cx}" cy="{cy}" r="11" fill="{c}" stroke="#333"/>'
        for dx, dy in dirs:
            s += (f'<line x1="{cx + dx * 13}" y1="{cy + dy * 13}" x2="{cx + dx * 40}" y2="{cy + dy * 40}" stroke="#c4501f" stroke-width="2.4" marker-end="url(#ar)"/>')
        return s
    return (f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}"><defs><marker id="ar" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#c4501f"/></marker></defs>'
            f'<rect x="0" y="34" width="{w}" height="{h - 34}" fill="#e6f1fb"/><line x1="0" y1="34" x2="{w}" y2="34" stroke="#1d6db1" stroke-width="2"/>'
            f'<text x="6" y="24" font-size="12" fill="#555">공기 (당기는 분자 거의 없음)</text>'
            + mol(90, 48, [(-1, 0), (1, 0), (0, 1)], '#ffd9c2') + mol(240, 102, [(-1, 0), (1, 0), (0, 1), (0, -1)], '#c9def5') +
            f'<text x="90" y="{h - 8}" font-size="12.5" text-anchor="middle" font-weight="700" fill="#933610">표면 분자: 알짜힘 ↓ (수직 아래)</text>'
            f'<text x="240" y="{h - 8}" font-size="12.5" text-anchor="middle" font-weight="700" fill="#134e83">내부 분자: 알짜힘 0</text></svg>')


def svg_capillary(w=250, h=180):
    return (f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}">'
            f'<rect x="10" y="120" width="{w - 20}" height="50" fill="#cfe3f7"/><line x1="10" y1="120" x2="{w - 10}" y2="120" stroke="#1d6db1" stroke-width="1.5"/>'
            f'<rect x="105" y="45" width="40" height="125" fill="#cfe3f7"/>'
            f'<path d="M105,45 Q125,62 145,45" fill="#fff" stroke="#1d6db1" stroke-width="1.5"/>'
            f'<line x1="103" y1="12" x2="103" y2="165" stroke="#333" stroke-width="2.5"/><line x1="147" y1="12" x2="147" y2="165" stroke="#333" stroke-width="2.5"/>'
            f'<line x1="170" y1="49" x2="170" y2="120" stroke="#c4501f" stroke-width="1.5" marker-start="url(#ah)" marker-end="url(#ah)"/>'
            f'<defs><marker id="ah" markerWidth="7" markerHeight="7" refX="3.5" refY="3.5" orient="auto"><path d="M0,0 L7,3.5 L0,7 z" fill="#c4501f"/></marker></defs>'
            f'<text x="176" y="90" font-size="14" font-weight="800" fill="#c4501f">h</text>'
            f'<line x1="105" y1="30" x2="145" y2="30" stroke="#555" stroke-dasharray="3 2"/><text x="125" y="26" font-size="12" text-anchor="middle">2r</text>'
            f'<text x="62" y="70" font-size="12" text-anchor="middle" fill="#0a6355" font-weight="700">↑ 2πrγ</text>'
            f'<text x="62" y="86" font-size="11" text-anchor="middle" fill="#555">(벽 부착 → 끌어올림)</text>'
            f'<text x="125" y="105" font-size="11" text-anchor="middle" fill="#134e83">πr²hρg</text><text x="125" y="118" font-size="11" text-anchor="middle" fill="#134e83">↓</text></svg>')


def svg_drop(theta=55, w=330, h=160, label=True, col=('#1d6db1', '#0f8b78', '#c4501f'), R=70, cx=140):
    G = h - 38
    t = math.radians(theta)
    d, a = R * math.cos(t), R * math.sin(t)
    large = 1 if theta > 90 else 0
    xr = cx + a
    s = (f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}"><defs><marker id="dv" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="context-stroke"/></marker></defs>'
         f'<rect x="10" y="{G}" width="{w - 20}" height="14" fill="#e4e7ee"/><line x1="10" y1="{G}" x2="{w - 10}" y2="{G}" stroke="#555" stroke-width="1.5"/>'
         f'<path d="M{cx - a:.1f},{G} A{R},{R} 0 {large} 1 {xr:.1f},{G} Z" fill="#cfe3f7" stroke="#1d6db1" stroke-width="2"/>')
    if label:
        L = 62
        tx, ty = xr - L * math.cos(t), G - L * math.sin(t)
        s += (f'<line x1="{xr:.1f}" y1="{G}" x2="{xr + 64:.1f}" y2="{G}" stroke="{col[2]}" stroke-width="3" marker-end="url(#dv)"/>'
              f'<text x="{xr + 66:.1f}" y="{G - 6}" font-size="14" font-weight="800" fill="{col[2]}">γ<tspan font-size="10" dy="3">S</tspan></text>'
              f'<line x1="{xr:.1f}" y1="{G}" x2="{xr - 60:.1f}" y2="{G}" stroke="{col[1]}" stroke-width="3" marker-end="url(#dv)"/>'
              f'<text x="{xr - 64:.1f}" y="{G + 26}" font-size="14" font-weight="800" fill="{col[1]}">γ<tspan font-size="10" dy="3">SL</tspan></text>'
              f'<line x1="{xr:.1f}" y1="{G}" x2="{tx:.1f}" y2="{ty:.1f}" stroke="{col[0]}" stroke-width="3" marker-end="url(#dv)"/>'
              f'<text x="{tx - 4:.1f}" y="{ty - 6:.1f}" font-size="14" font-weight="800" fill="{col[0]}">γ<tspan font-size="10" dy="3">L</tspan></text>'
              f'<path d="M{xr - 24:.1f},{G} A24,24 0 0 1 {xr - 24 * math.cos(t):.1f},{G - 24 * math.sin(t):.1f}" fill="none" stroke="#333"/>'
              f'<text x="{xr - 38:.1f}" y="{G - 6}" font-size="13" font-weight="700">θ</text>')
    return s + '</svg>'


def svg_three_drops(w=440, h=104):
    out = f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}">'
    for i, (th, lab, c) in enumerate([(12, 'θ ≈ 0° 완전 습윤 · S = 0', '#15803d'), (90, 'θ = 90°', '#555'), (150, 'θ → 180° 안 젖음', '#b91c1c')]):
        cx, G, R = 75 + i * 145, 70, 30 if th != 12 else 150
        t = math.radians(th)
        if th == 12:
            R = 120
        d, a = R * math.cos(t), R * math.sin(t)
        large = 1 if th > 90 else 0
        out += (f'<line x1="{cx - 68}" y1="{G}" x2="{cx + 68}" y2="{G}" stroke="#555" stroke-width="1.5"/>'
                f'<path d="M{cx - a:.1f},{G} A{R},{R} 0 {large} 1 {cx + a:.1f},{G} Z" fill="#cfe3f7" stroke="#1d6db1" stroke-width="1.8"/>'
                f'<text x="{cx}" y="{G + 22}" font-size="12" text-anchor="middle" font-weight="700" fill="{c}">{lab}</text>')
    return out + '</svg>'


def svg_hlb(w=440, h=200):
    rows = [('가용화제', 16, 18, '#8a3ab9'), ('세제', 13, 16, '#b5179e'), ('O/W 유화제', 8, 16, '#1d6db1'),
            ('습윤제', 6, 9, '#0f8b78'), ('W/O 유화제', 3, 8, '#c4501f'), ('소포제', 1, 3, '#6b7280')]
    x0, x1 = 96, w - 14
    sx = lambda v: x0 + (x1 - x0) * v / 18
    s = f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}">'
    for v in range(0, 19, 3):
        s += f'<line x1="{sx(v):.0f}" y1="8" x2="{sx(v):.0f}" y2="{h - 24}" stroke="#e4e7ee"/><text x="{sx(v):.0f}" y="{h - 9}" font-size="11.5" text-anchor="middle">{v}</text>'
    for i, (lab, a, b, c) in enumerate(rows):
        y = 12 + i * 27
        s += (f'<text x="{x0 - 8}" y="{y + 14}" font-size="12.5" text-anchor="end" font-weight="700">{lab}</text>'
              f'<rect x="{sx(a):.0f}" y="{y}" width="{sx(b) - sx(a):.0f}" height="18" rx="5" fill="{c}"/>'
              f'<text x="{(sx(a) + sx(b)) / 2:.0f}" y="{y + 13.5}" font-size="11.5" text-anchor="middle" fill="#fff" font-weight="800">{a}~{b}</text>')
    return s + f'<text x="{x0}" y="{h - 9}" font-size="11" fill="#c4501f" text-anchor="end">친유 ←</text><text x="{x1}" y="{h - 9}" font-size="11" fill="#1d6db1" text-anchor="start" dx="-34">→ 친수</text></svg>'


def svg_surfactant(w=330, h=130):
    s = (f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}"><rect x="0" y="56" width="{w}" height="{h - 56}" fill="#e6f1fb"/>'
         f'<line x1="0" y1="56" x2="{w}" y2="56" stroke="#1d6db1" stroke-width="2"/>'
         f'<text x="8" y="20" font-size="12" fill="#555">공기 · 기름 (비극성)</text><text x="8" y="{h - 10}" font-size="12" fill="#134e83">물 (극성)</text>')
    for i in range(7):
        x = 70 + i * 34
        s += (f'<path d="M{x},50 l-6,-8 l6,-8 l-6,-8 l6,-8" fill="none" stroke="#c4501f" stroke-width="2.4"/>'
              f'<circle cx="{x}" cy="58" r="8" fill="#1d6db1"/>')
    return s + (f'<text x="{w - 6}" y="20" font-size="12" text-anchor="end" fill="#c4501f" font-weight="700">소수성 tail ↑</text>'
                f'<text x="{w - 6}" y="84" font-size="12" text-anchor="end" fill="#1d6db1" font-weight="700">친수성 head ↓</text></svg>')


def svg_iso(w=470, h=112):
    fs = [('I', 'Langmuir', lambda t: 0.85 * (1 - math.exp(-7 * t))),
          ('II', 'BET', lambda t: 0.42 * (1 - math.exp(-9 * t)) + 0.5 * t ** 3),
          ('III', '비다공 응축', lambda t: 0.9 * t ** 2.6),
          ('IV', '다공 흡착', lambda t: 0.35 * (1 - math.exp(-9 * t)) + 0.55 * (1 / (1 + math.exp(-14 * (t - .55))) - 1 / (1 + math.exp(7.7)))),
          ('V', '다공 응축', lambda t: 0.9 * (1 / (1 + math.exp(-12 * (t - .55))) - 1 / (1 + math.exp(6.6))))]
    pw = w / 5
    s = f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}">'
    for i, (n, lab, f) in enumerate(fs):
        x0, x1, y0, y1 = i * pw + 10, (i + 1) * pw - 6, 18, h - 26
        s += (f'<rect x="{x0}" y="{y0}" width="{x1 - x0}" height="{y1 - y0}" fill="#fff" stroke="#c9cfdb"/>'
              f'<path d="{_curve(f, x0 + 3, x1 - 3, y0 + 4, y1)}" fill="none" stroke="#c4501f" stroke-width="2.3"/>'
              f'<text x="{(x0 + x1) / 2}" y="13" font-size="12" text-anchor="middle" font-weight="800">{n}형</text>'
              f'<text x="{(x0 + x1) / 2}" y="{h - 9}" font-size="11" text-anchor="middle" fill="#555">{lab}</text>')
    return s + '</svg>'


def svg_freundlich(w=250, h=140):
    x0, y0, x1, y1 = 40, 12, w - 10, h - 26
    return (f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}">{_axes(w, h, x0, y0, x1, y1, "log P", "log(x/m)")}'
            f'<line x1="{x0}" y1="{y1 - 30}" x2="{x1 - 10}" y2="{y0 + 14}" stroke="#c4501f" stroke-width="2.4"/>'
            f'<circle cx="{x0}" cy="{y1 - 30}" r="4" fill="#c4501f"/><text x="{x0 + 8}" y="{y1 - 34}" font-size="12" fill="#933610" font-weight="700">절편 log k</text>'
            f'<text x="{x0 + 110}" y="{y0 + 66}" font-size="12" fill="#933610" font-weight="700">기울기 1/n</text></svg>')


def svg_zisman(w=280, h=160):
    x0, y0, x1, y1 = 42, 14, w - 10, h - 28
    X = lambda v: x0 + (x1 - x0) * (v - 15) / 60
    Y = lambda c: y1 - (y1 - y0) * (c - 0.2) / 0.85
    f = lambda gl: 1 - 0.016 * (gl - 22)
    pts = ''.join(f'<circle cx="{X(v):.1f}" cy="{Y(f(v)):.1f}" r="4" fill="#1d6db1"/>' for v in (35, 45, 55, 65, 72))
    return (f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}">{_axes(w, h, x0, y0, x1, y1, "γ_L (액체 표면장력)", "cosθ")}'
            f'<line x1="{x0}" y1="{Y(1):.1f}" x2="{x1}" y2="{Y(1):.1f}" stroke="#999" stroke-dasharray="3 3"/><text x="{x0 - 4}" y="{Y(1) + 4:.1f}" font-size="11" text-anchor="end">1</text>'
            f'<line x1="{X(22):.1f}" y1="{Y(1):.1f}" x2="{X(35):.1f}" y2="{Y(f(35)):.1f}" stroke="#1d6db1" stroke-width="2" stroke-dasharray="5 4"/>'
            f'<line x1="{X(35):.1f}" y1="{Y(f(35)):.1f}" x2="{X(72):.1f}" y2="{Y(f(72)):.1f}" stroke="#1d6db1" stroke-width="2.2"/>{pts}'
            f'<line x1="{X(22):.1f}" y1="{Y(1):.1f}" x2="{X(22):.1f}" y2="{y1}" stroke="#c4501f" stroke-dasharray="3 3"/>'
            f'<circle cx="{X(22):.1f}" cy="{Y(1):.1f}" r="5" fill="#c4501f"/><text x="{X(22) + 6:.1f}" y="{y1 - 6}" font-size="13" font-weight="800" fill="#c4501f">γ<tspan font-size="10" dy="3">c</tspan></text>'
            f'<text x="{X(40):.1f}" y="{Y(1) + 16:.1f}" font-size="11" fill="#1d6db1">← 외삽 (θ = 0)</text></svg>')


def svg_potential(w=330, h=180, labels=('a', 'b', 'c')):
    x0, x1, yz = 44, w - 12, 92
    xa, xb, xc = x0, x0 + 70, x0 + 190
    top, bot = 16, h - 30
    def path(fn):
        pts = []
        for i in range(61):
            x = xa + (xc + 30 - xa) * i / 60
            pts.append(f'{x:.1f},{fn(x):.1f}')
        return 'M' + ' L'.join(pts)
    S1 = path(lambda x: yz - (yz - top) * max(0, 1 - ((x - xa) / (xc - xa)) ** 1.6) if x <= xc else yz)
    S2 = path(lambda x: yz - (yz - top) * max(0, 1 - (x - xa) / (xb - xa)) if x <= xb else yz)
    S3 = path(lambda x: (yz - (yz - top) + (bot - top + 10) * ((x - xa) / (xb - xa)) ** 1.2) if x <= xb else
              (yz + (bot - 6 - yz) * max(0, 1 - (x - xb) / (xc - 40 - xb)) ** 1.6))
    a, b, c = labels
    return (f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}">'
            f'<line x1="{x0}" y1="{yz}" x2="{x1}" y2="{yz}" stroke="#333" stroke-width="1.3"/><text x="{x1}" y="{yz - 5}" font-size="11.5" text-anchor="end">거리 →</text>'
            f'<text x="{x0 - 6}" y="{top + 6}" font-size="12" text-anchor="end">(+)</text><text x="{x0 - 6}" y="{bot}" font-size="12" text-anchor="end">(−)</text><text x="{x0 - 6}" y="{yz + 4}" font-size="12" text-anchor="end">0</text>'
            + ''.join(f'<line x1="{x}" y1="{top - 6}" x2="{x}" y2="{bot + 6}" stroke="#555" stroke-dasharray="4 3"/><text x="{x}" y="{h - 8}" font-size="12.5" text-anchor="middle" font-weight="800">{l}</text>' for x, l in ((xa, a), (xb, b), (xc, c))) +
            f'<path d="{S1}" fill="none" stroke="#1d6db1" stroke-width="2.4"/><path d="{S2}" fill="none" stroke="#0f8b78" stroke-width="2.4"/><path d="{S3}" fill="none" stroke="#c4501f" stroke-width="2.4"/>'
            f'<text x="{xb + 40}" y="{top + 22}" font-size="12.5" font-weight="800" fill="#1d6db1">S1</text><text x="{xb - 32}" y="{yz - 20}" font-size="12.5" font-weight="800" fill="#0f8b78">S2</text>'
            f'<text x="{xb + 8}" y="{bot - 2}" font-size="12.5" font-weight="800" fill="#c4501f">S3</text>'
            f'<text x="{(xa + xb) / 2}" y="{bot + 2}" font-size="10.5" text-anchor="middle" fill="#555">고정층</text><text x="{(xb + xc) / 2 + 20}" y="{bot + 2}" font-size="10.5" text-anchor="middle" fill="#555">확산층</text></svg>')


def svg_layers(w=330, h=118):
    s = f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}"><rect x="6" y="10" width="44" height="{h - 34}" fill="#9aa5b8"/><text x="28" y="{h / 2}" font-size="12" text-anchor="middle" fill="#fff" font-weight="800">입자</text>'
    for i in range(5):
        y = 20 + i * 17
        s += f'<text x="56" y="{y + 4}" font-size="12" font-weight="800" fill="#1d6db1">+</text><text x="76" y="{y + 4}" font-size="12" font-weight="800" fill="#c4501f">−</text>'
    import random
    rnd = random.Random(3)
    for i in range(16):
        x, y = 104 + rnd.random() * 90, 16 + rnd.random() * 70
        s += f'<text x="{x:.0f}" y="{y:.0f}" font-size="12" font-weight="800" fill="{"#c4501f" if i % 3 else "#1d6db1"}">{"−" if i % 3 else "+"}</text>'
    for i in range(12):
        x, y = 212 + rnd.random() * 100, 16 + rnd.random() * 70
        s += f'<text x="{x:.0f}" y="{y:.0f}" font-size="12" font-weight="800" fill="{"#c4501f" if i % 2 else "#1d6db1"}">{"−" if i % 2 else "+"}</text>'
    for x, l in ((52, 'a (표면)'), (94, 'b (전단면)'), (204, 'c (중성 시작)')):
        s += f'<line x1="{x}" y1="6" x2="{x}" y2="{h - 22}" stroke="#555" stroke-dasharray="4 3"/><text x="{x}" y="{h - 8}" font-size="11" text-anchor="middle" font-weight="700">{l}</text>'
    return s + '</svg>'


# ============================================================ 표지
def cover_fig():
    return svg_drop(68, w=300, h=175, R=78, cx=122, col=('#5b3fd6', '#8f7fe6', '#3d2a9e')).replace('#cfe3f7', '#e9e3ff').replace('#1d6db1', '#5b3fd6').replace('#e4e7ee', '#ece8fb').replace('stroke="#555"', 'stroke="#b9b0e6"')


cv_parts = [
    ('00', '읽기 전에', '기호 사전 · 수학 5개 (cos, 구 넓이·부피, 가중평균, log 직선, 미분 근사)', ''),
    ('01', '표면장력과 표면자유에너지', '계면 vs 표면 · 장력의 원인 · γ = F/2l · W = γΔA · Young-Laplace · 모세관', '문제 01–02'),
    ('02', '부착 · 응집 · 퍼짐', '부착일 W<sub>a</sub> · 응집일 W<sub>c</sub> · 퍼짐계수 S · 벤젠 예제', '문제 03'),
    ('03', '액체계면 흡착 · 계면활성제', '정·부흡착 · 계면활성제 · HLB 척도 · Span/Tween · 유제 · RHLB 계산', '문제 04–09'),
    ('04', '고체계면 흡착', '흡착매·흡착질 · 물리/화학 흡착 · Freundlich · 등온선 I~V형', '문제 10'),
    ('05', '습윤 · 전기적 성질', 'Young 식 · S = γ<sub>L</sub>(cosθ − 1) · Zisman · 테플론 · 네른스트/제타', '문제 11–17 · 한 장 정리'),
]
cv_cards = ''.join(
    f'<div class="cc"><div class="n">{n}</div><div class="b"><div class="t">{"PART " + str(int(n)) + " · " if n != "00" else ""}{t}</div>'
    f'<div class="d">{d}</div>' + (f'<div class="q">{q}</div>' if q else '') + '</div></div>' for n, t, d, q in cv_parts)
cv_steps = ''.join(f'<span class="s"><i>{i}</i>{t}</span>' for i, t in enumerate(['💡 핵심 개념', '📖 상세 설명', '📐 중요 공식', '✍️ 예제 및 풀이', '🧠 한 줄 요약'], 1))
pages.append(f'''<section class="page cv2">
<div class="glow"></div>
<div class="top"><div class="l">
<div class="eye"><span>PHYSICAL PHARMACY</span><b>물리약학 · 12–13주차 · CH.10</b></div>
<h1>계면현상</h1>
<h2>한 번 읽으면 각인되는 <em>최종 요약본</em></h2>
<div class="rule"></div>
<div class="src">12주차 계면현상 (1) · (2) 강의 영상 · 13주차 계면현상 3 (Summary + 기출 2016–2026)<br>녹취 12주차 영상 2편 · 11/26 현장강의를 한 권으로</div>
</div><div class="r"><div class="fig2">{cover_fig()}</div></div></div>
<div class="steps"><span class="lb">모든 개념은 이 순서로</span>{cv_steps}</div>
<div class="cards">{cv_cards}</div>
{foot()}</section>''')

# ============================================================ 읽기 전에 ① 기호
pages.append(f'''<section class="page p0 dense">{hdr('읽기 전에 ①', '기호 · 용어 사전 — 이 문서에 나오는 모든 기호', 'Symbols & terms', PARTS[0])}
<div class="two" style="grid-template-columns:1fr 1fr">
<div>{tbl(['기호', '이름', '뜻'], [
    ['γ', 'gamma (감마)', '표면장력 · 계면장력 — 단위 <b>dyne/cm</b> 또는 <b>N/m</b>'],
    [f'{g("LV")} · {g("SV")}', '액체/기체 · 고체/기체', '<b>표면</b>장력 (한쪽이 기체)'],
    [f'{g("LL")} · {g("LS")}', '액체/액체 · 액체/고체', '<b>계면</b>장력'],
    [f'{g("S")} · {g("L")} · {g("SL")}', '고체 · 액체 · 고-액', '습윤·퍼짐 식에 쓰는 줄임 표기'],
    ['W · ΔA', 'work · 면적 변화', '일 = 에너지. W = γΔA (표면자유에너지)'],
    ['ΔP · r', '압력차 · 반지름', 'Young-Laplace ΔP = 2γ/r'],
    ['h · ρ · g', '높이 · 밀도 · 중력가속도', '모세관 γ = ½rhρg'],
    ['W<sub>a</sub> · W<sub>c</sub>', 'adhesion · cohesion', '부착일 · 응집일'],
    ['S', 'spreading coefficient', '퍼짐계수 (S &gt; 0 퍼짐)'],
    ['θ', 'contact angle (접촉각)', '0° 완전 습윤 · 180° 전혀 안 젖음'],
    ['γ<sub>c</sub>', 'critical surface tension', '임계표면장력 (Zisman plot, cosθ = 1)'],
    ['x/m', '흡착량', '고체 m g당 흡착된 기체 x'],
    ['ζ (zeta)', 'zeta potential', '제타 전위 — 전단면 ↔ 중성 영역'],
], 'gl')}</div>
<div>{tbl(['용어', '뜻'], [
    ['HLB', 'Hydrophilic-Lipophilic Balance — 친수-친유 평형값 (클수록 친수)'],
    ['RHLB', 'Required HLB — 그 기름을 유화하는 데 <b>필요한</b> 계면활성제 HLB'],
    ['Surfactant', '계면활성제 — 친수 head + 소수 tail (양친매성)'],
    ['Positive · Negative adsorption', '정흡착 (표면으로, γ ↓) · 부흡착 (내부로, γ ↑)'],
    ['O/W · W/O', 'Oil in Water · Water in Oil — 앞이 방울, 뒤가 바다'],
    ['Span · Tween', '소르비탄 에스터 (친유) · 폴리옥시에틸렌 소르비탄 (친수)'],
    ['Adsorbent · Adsorbate', '흡착매 (고체) · 흡착질 (기체)'],
    ['Isotherm', '등온선 — 일정 온도에서 압력 vs 흡착량'],
    ['Wetting · Wetting agent', '습윤 (고체 위에 퍼짐) · 습윤제 (접촉각 ↓, HLB 6~9)'],
    ['Shear plane', '전단면 — 입자가 데리고 다니는 고정층의 바깥 경계'],
    ['Nernst potential', '네른스트 전위 — 고체 표면(a) ↔ 중성 영역'],
])}
<div class="ana"><span class="t">📌 읽는 요령</span>처음 나오는 어려운 말 옆에는 <span class="jk">[즉, ~라는 뜻]</span>이 붙어 있어요. 교수님 말씀은 <b>“ ”</b>로 인용하고 출처(12주차 영상 · 11/26 수업)를 붙였어요.</div></div>
</div>{foot()}</section>''')

# ============================================================ 읽기 전에 ② 수학
pages.append(f'''<section class="page p0">{hdr('읽기 전에 ②', '수학 겁먹지 않기 — 이 단원에 필요한 수학은 딱 5개', 'Math you actually need', PARTS[0])}
<div class="two" style="grid-template-columns:1fr 1fr">
<div>
{sec('➊', 'cos 값 3개 (습윤의 전부)', tbl(['θ', 'cosθ', '의미'], [['0°', '<b>1</b>', '완전 습윤 → S = 0 (최댓값)'], ['90°', '0', '젖음/안 젖음 경계'], ['180°', '<b>−1</b>', '전혀 안 젖음 → S = −2γ<sub>L</sub>']]) + '<p>θ가 작아질수록 cosθ는 <mark>커진다</mark> → 퍼짐계수 ↑.</p>')}
{sec('➋', '구의 넓이 · 부피 (Young-Laplace 유도)', '<p>넓이 A = <b>4πr²</b>, 부피 V = <b>(4/3)πr³</b>. 넓이를 r로 적분하면 부피 ' + J('dV = 4πr² dr') + '</p>')}
{sec('➌', '미분 근사 — (dr)²은 버린다', '<p>(r − dr)² = r² − 2r·dr + (dr)² ≈ r² − 2r·dr. 아주 작은 수의 제곱은 0으로 봐요.</p>')}
</div>
<div>
{sec('➍', '가중평균 (RHLB 계산)', '<p>혼합 값 = Σ(질량분율 × 값). 두 개를 섞을 때 x·A + (1 − x)·B = 목표 → <mark>x = (목표 − B)/(A − B)</mark>. 그래서 목표는 반드시 <b>A와 B 사이</b>.</p>')}
{sec('➎', 'log 취해 직선 만들기 (Freundlich)', '<p>y = k·p<sup>1/n</sup> → log y = log k + (1/n) log p. y절편 = log k, 기울기 = 1/n.</p>')}
<div class="ana"><span class="t">🍬 전체 그림</span>계면현상 = <b>경계면의 분자는 손해를 본다</b>는 한 문장에서 출발해요. 표면 분자는 안쪽으로만 당겨져서(장력), 표면을 줄이려 하고(자유에너지), 그 결과 방울은 둥글고(Young-Laplace), 관을 타고 오르고(모세관), 퍼지거나 뭉쳐요(퍼짐·습윤). 계면활성제는 그 경계면에 대신 서서 손해를 줄여 주는 분자예요.</div>
</div></div>{foot()}</section>''')

# ============================================================ PART 1
concept(1, 1, '계면과 표면 — 표면은 계면의 부분집합', 'Interface vs surface',
        '섞이지 않는 두 상의 경계 = <mark>계면</mark>. 그중 한쪽이 <mark>기체</mark>면 <mark>표면</mark>. 기체끼리는 섞여서 계면이 없다.',
        EXPL(ul(['계면(interface): 액체/액체, 액체/고체 ' + J('두 상이 맞닿은 면'),
                 '표면(surface): 액체-기체, 고체-기체 — 표면 ⊂ 계면',
                 '기체/기체는 섞이므로 계면 형성 <b>X</b>'])
             + tbl(['기호', '접촉', '구분'], [
                 [g('LV'), '액체 / 기체', '<b>표면</b>'], [g('SV'), '고체 / 기체', '<b>표면</b>'],
                 [g('LL'), '액체 / 액체', '<b>계면</b>'], [g('LS'), '액체 / 고체', '<b>계면</b>']])),
        sec('💊', '약학에서의 계면현상', ul(['유제 · 현탁제의 안정성 (기름방울·입자가 뭉치지 않게)', '정제 붕해·용출에서 <b>습윤</b> (물이 가루를 적셔야 녹음)', '계면활성제: 가용화 · 세정 · 유화 · 습윤 · 소포', '인공혈관 소재(테플론), 콜로이드 안정성(제타 전위)']))
        + ana('11/26 수업: “표면은 한쪽이 기체일 때 표면… 그 외에는 계면. <b>계면에 표면이 부분집합</b>으로 들어가는 거죠.”', '🎤 교수님')
        + warn('Summary 1: “(<b>계면</b>/표면): 액체/고체끼리의 접촉면”, “(계면/<b>표면</b>): 액체-기체, 고체-기체” — 기체가 끼면 표면!'),
        '기체가 끼면 표면, 아니면 계면 — 표면 ⊂ 계면')

concept(1, 2, '표면장력은 왜 생기나 — 표면 분자의 알짜힘은 아래', 'Origin of surface tension',
        '내부 분자는 사방에서 당겨져 <mark>알짜힘 0</mark>, 표면 분자는 위에서 당겨 줄 분자가 없어 <mark>알짜힘 = 수직 아래</mark> → 표면적을 줄이려는 힘 = 표면장력.',
        EXPL(fig(svg_forces()) + ul(['표면 분자는 안으로 들어가려 함 → 표면적 <b>최소화</b> (그래서 물방울은 구형)',
                                     '단위: 길이당 힘 <b>dyne/cm</b> 또는 <b>N/m</b> ' + J('1 dyne/cm = 1 mN/m')])),
        ana('물 위를 걷는 소금쟁이, 컵 위로 볼록 올라온 물 — 표면 분자들이 서로 손잡고 “막”처럼 버티는 것.')
        + ana('11/26 수업 (2016 Q12 풀이): “위로 잡아당기는 힘이 없잖아요. 나머지 다 상쇄가 되는데 결과적으로 <b>알짜 힘은 수면 아래</b>.”', '🎤 교수님')
        + warn('“중력” 아님, “수면과 나란한 방향”도 아님(좌우는 상쇄). 정답은 <b>수면 수직 아래</b>.', '⚠️ 기출 함정'),
        '표면 분자는 손잡을 이웃이 위에 없다 → 아래로 당겨진다')

concept(1, 3, '표면장력 > 계면장력 — 상대가 당겨 주면 줄어든다', 'Surface vs interfacial tension',
        '통상 <mark>표면장력이 계면장력보다 크다</mark>. 공기는 거의 안 당기지만 다른 액체는 위로 당겨 아래 알짜힘을 상쇄하기 때문. 예외: 물과 <mark>반발</mark>하는 클로로포름·벤젠.',
        EXPL(tbl(['물질 (20℃)', '표면장력', '물과의 계면장력', '변화'], [
            ['물', '72.8', '—', ''], ['올레산', '32.5', '15.6', '<b>감소</b> (통상)'], ['올리브유', '35.8', '22.9', '<b>감소</b>'],
            ['클로로포름', '27.1', '32.8', '<b style="color:#b91c1c">증가 (예외)</b>'], ['벤젠', '28.9', '35.0', '<b style="color:#b91c1c">증가 (예외)</b>']])
             + '<p>단위 dyne/cm. 올레산의 −COOH는 물과 친해 위로 당겨 줌(<b>인력</b>) → 계면장력 ↓. 클로로포름은 물과 <b>반발</b> → 오히려 ↑.</p>'),
        ana('줄다리기: 혼자 당겨지던 표면 분자(공기 쪽 상대 없음)에 반대편 팀(다른 액체)이 생기면 아래로 끌리는 힘이 줄어요. 반대편이 오히려 밀어내면(반발) 더 세게 끌려요.')
        + warn('Summary 1: “통상적으로 (계면/<b>표면</b>) 장력이 (<b>계면</b>/표면) 장력보다 큰 값” — 순서 바꿔치기 주의.')
        + warn('밀도와는 무관 — 교수님: “밀도 때문에 차이가 있는 건 아니에요.” 위아래 층을 그리려고 쓴 값.', '⚠️ 헷갈림'),
        '공기는 안 당기고 이웃 액체는 당긴다 → 보통 표면장력이 더 크다')

concept(1, 4, '표면장력 측정과 표면자유에너지 — 길이당 힘, 면적당 일', 'γ = F/2l · W = γΔA',
        'ㄷ자 철사 비누막은 <mark>앞뒤 2면</mark> → γ × 2l = F, <mark>γ = F/2l</mark>. 막을 넓히는 데 드는 일 = <mark>W = γΔA</mark> (표면자유에너지).',
        EXPL(ul(['클립(길이 l)을 F로 당기면 막이 끊어지려는 순간 F = γ × 2l',
                 '표면 분자는 안으로 들어가려는 퍼텐셜에너지를 가짐 = <b>표면자유에너지</b> ' + J('표면적을 줄이려는 에너지'),
                 'ds만큼 더 당기면 dW = F·ds = γ·2l·ds = γ·dA → W = γΔA'])
             + FORM(fbox('γ = F / 2l', '표면장력 = 길이당 힘 (dyne/cm)') + fbox('W = γ × ΔA', '표면자유에너지 = 면적당 일 (erg/cm²) — 같은 γ, 다른 해석'))),
        ana('비닐 랩을 팽팽하게 당겨 넓히려면 힘이 들죠. 넓힐수록(ΔA) 일(W)이 비례해서 늘어요.')
        + ana('11/26 수업: “표면장력은 <b>2l분의 F</b>, 길이에 걸리는 힘. 표면자유에너지는 <b>면적에 걸리는 일</b>, 일이 곧 에너지.”', '🎤 교수님')
        + warn('2l의 <b>2</b> = 막이 앞·뒤 두 장. l만 쓰면 γ가 2배로 계산됨.'),
        'γ = F/2l (막 2장) · W = γΔA (일 = 에너지)')

concept(1, 5, 'Young-Laplace 식 — 작은 방울일수록 안쪽 압력이 크다', 'ΔP = 2γ/r',
        '비눗방울 내부 압력과 대기압의 차이를 <mark>표면장력이 버틴다</mark>. 표면자유에너지 변화 = 압력차가 한 일 → <mark>ΔP = 2γ/r</mark>.',
        EXPL(steps([('반지름 r → r − dr: W = γ·4π(r − dr)² ≈ γ4πr² − <b>8πγr dr</b>', '(dr)²은 버림 → 변화량 −8πγr dr'),
                    ('압력차가 한 일: Δ(PV) = ΔP × 4πr² × (−dr)', '부피 변화 = 넓이 × 두께'),
                    ('두 식을 같게: ΔP·4πr² = 8πγr → <mark>ΔP = 2γ/r</mark>', '물리적 일 = 화학적 일')]))
        + FORM(fbox('ΔP = 2γ / r', 'Young-Laplace 식 — 곡계면에서의 압력차')),
        ana('작은 풍선이 처음 불 때 가장 힘들죠? r이 작을수록 ΔP가 커서 그래요. 두 비눗방울을 연결하면 <b>작은 쪽이 큰 쪽으로</b> 바람을 밀어 넣어요.')
        + ex('반지름 0.1 cm 물방울(γ = 72 dyne/cm)의 내외부 압력차는?', [('ΔP = 2 × 72 / 0.1', ''), ('= <b>1440 dyne/cm²</b>', 'r을 절반으로 → ΔP 2배')])
        + warn('“곡<b>계면</b>에서의 압력차 관계식” — 녹취 “표면에서의”는 받아쓰기 오류(11/26).'),
        'ΔP = 2γ/r — 작을수록 안쪽이 빵빵')

concept(1, 6, '모세관 상승법 — 부착력이 시작, 표면장력이 끌어올림', 'Capillary rise: γ = ½rhρg',
        '위로 당기는 <mark>2πrγ</mark>(cosθ ≈ 1) = 아래로 당기는 물기둥 무게 <mark>πr²hρg</mark> → <mark>γ = ½rhρg</mark>. 반지름 · 높이 · 밀도만 알면 γ.',
        EXPL(fig(svg_capillary()) + FORM(fbox('γ = ½ r h ρ g', '2πrγ = πr²hρg — 관이 가늘수록 h ↑'))),
        sec('🧪', '11/26 KAIST 면접 문제 — 모세관을 5 cm에서 자르면?',
            '<p>10 cm까지 올라갈 액체인데 관을 5 cm에서 자르면 → <mark>분수처럼 솟지 않고</mark>, 5 cm 끝에서 <b>볼록한 방울</b>로 멈춘다.</p>'
            + steps([('① 관 벽과의 <b>부착력</b>이 먼저 붙어 메니스커스 형성', '“부착력이 시작을 해 주고”'),
                     ('② <b>표면장력</b>이 가운데 분자들을 끌어올림', '“표면장력으로 끌고 올라가는 거다”'),
                     ('5 cm 위에는 잡아 줄 벽(부착력)이 없음 → 표면적 최소인 둥근 모양으로 정지', '표면장력만으로는 못 오른다')]))
        + warn('Summary 2 빈칸: 물의 (<b>표면장력</b>)과 중력의 평형 · 수직 성분 = (<b>물 높이</b>)에 해당하는 무게 · 관의 (<b>반지름</b>), 액체 (<b>밀도</b>)'),
        '모세관 = 부착력이 손잡이, 표면장력이 엔진 → γ = ½rhρg')

problem(1, 1, '수면의 물 분자에 작용하는 알짜힘', '2016 Q12 · 11/26 수업 풀이',
        '상온, 수면에서 공기와 접촉하고 있는 물 분자에 작용하는 알짜힘은?',
        ['중력', '수면과 나란한 방향', '수면 수직 아래', '수면 수직 위', '수면 아래 45° 방향'], '③ 수면 수직 아래',
        [('표면 분자: 위(공기)에서 당겨 주는 물 분자가 없음', '개념 02 그림'),
         ('좌우 인력은 서로 상쇄', '② 나란한 방향 = 상쇄돼서 0'),
         ('남는 것: 아래(내부)로 당기는 힘 → <b>수면 수직 아래</b>', '그래서 표면적을 줄이려 함 = 표면장력')],
        [(False, '①', '분자 사이 인력에 비해 중력은 무시'), (False, '②', '좌우는 상쇄'), (True, '③', '알짜힘 = 수직 아래 ✓'), (False, '④', '위에는 당길 분자가 없음'), (False, '⑤', '대각선 성분도 좌우 상쇄')],
        brain='위에 이웃이 없다 → 알짜힘은 수직 아래')

problem(1, 2, '모세관 상승의 원리 (사고 실험)', '11/26 수업 · KAIST 석사 면접 문제',
        '용매 A는 모세관에서 10 cm까지 올라가는 표면장력을 가진다. 같은 모세관을 <b>5 cm 높이에서 잘라</b> 꽂으면 어떻게 되는가? 그리고 모세관 상승이 일어나기 위해 먼저 있어야 하는 힘은?',
        [], '5 cm 끝에서 볼록한 방울로 멈춘다 · 먼저 필요한 힘 = 부착력',
        [('모세관 상승 순서: ① 벽과의 <b>부착력</b> → 메니스커스 ② <b>표면장력</b>이 가운데를 끌어올림', '“1번 부착력이 먼저 있어야 되고요”'),
         ('5 cm 위에는 벽이 없어 부착력이 더 잡아 줄 수 없음', '“치솟으려면 부착력이 있었기 때문에 10 cm까지 올라올 수 있었던 거지”'),
         ('표면장력만으로는 더 오를 수 없고, 표면적이 최소인 <b>둥근 방울</b>로 멈춤', '물방울이 동그랗게 생기는 것과 같은 원리'),
         ('“분수처럼 치솟는다”는 오답 유도 — 에너지 공급원이 없다', '교수님 은사님이 내던 함정')],
        brain='부착력이 시작, 표면장력이 끌어올림 — 벽이 끝나면 방울로 멈춘다',
        extra=ana('“이렇게 AI 시대 때 이렇게 생각해 보는 훈련을 해봐야 돼요.” (11/26)', '🎤 교수님'))

# ============================================================ PART 2
concept(2, 7, '부착일과 응집일 — 떼어 낼 때 새로 생기는 면의 에너지', 'Work of adhesion · cohesion',
        '<mark>부착일</mark> W<sub>a</sub> = 서로 다른 분자 간 인력을 깨는 일 = γ<sub>L</sub> + γ<sub>S</sub> − γ<sub>SL</sub>. <mark>응집일</mark> W<sub>c</sub> = 같은 액체를 둘로 나누는 일 = 2γ<sub>L</sub>.',
        EXPL(tbl(['', '부착일 W<sub>a</sub>', '응집일 W<sub>c</sub>'], [
            ['무엇을 떼나', '서로 다른 액체 L | S', '같은 액체 L | L'],
            ['새로 생기는 면', '표면 2개 (γ<sub>L</sub>, γ<sub>S</sub>)', '표면 2개 (γ<sub>L</sub>, γ<sub>L</sub>)'],
            ['사라지는 면', '계면 1개 (γ<sub>SL</sub>)', '없음 (같은 것끼리는 계면 X)'],
            ['식 (단위 면적)', '<b>γ<sub>L</sub> + γ<sub>S</sub> − γ<sub>SL</sub></b>', '<b>2γ<sub>L</sub></b>']]))
        + FORM(fbox('W<sub>a</sub> = γ<sub>L</sub> + γ<sub>S</sub> − γ<sub>SL</sub> &nbsp;·&nbsp; W<sub>c</sub> = 2γ<sub>L</sub>')),
        ana('양면테이프를 뗄 때(부착일) vs 찰흙 덩어리를 둘로 쪼갤 때(응집일). 떼어 내면 새 면이 생기고, 그 면의 표면자유에너지만큼 일이 든다.')
        + ana('11/26 수업: “같은 것들끼리는 계면이 존재하지 않기 때문에… <b>결합에너지랑 비슷한 개념</b>. 떨어졌을 때 새로 생기는 에너지만큼이 일로서 작용.”', '🎤 교수님')
        + warn('Summary 3 빈칸: 부착일 = 서로 다른 분자간의 (<b>인력</b>)을 깨뜨리는 에너지 · 응집일 = (<b>같은 액체</b>)를 독립적인 층으로 나누는 일'),
        '부착 = 남남 떼기 (−γ<sub>SL</sub>) · 응집 = 나를 쪼개기 (2γ<sub>L</sub>)')

concept(2, 8, '퍼짐계수 S — 붙으려는 힘이 뭉치려는 힘보다 크면 퍼진다', 'Spreading coefficient',
        '<mark>S = W<sub>a</sub> − W<sub>c</sub> = γ<sub>S</sub> − (γ<sub>L</sub> + γ<sub>SL</sub>)</mark>. S &gt; 0이면 퍼짐, S &lt; 0이면 렌즈(방울)로 남음.',
        EXPL(steps([('S = W<sub>a</sub> − W<sub>c</sub>', '부착하려는 경향 − 응집하려는 경향'),
                    ('= (γ<sub>L</sub> + γ<sub>S</sub> − γ<sub>SL</sub>) − 2γ<sub>L</sub>', ''),
                    ('= <mark>γ<sub>S</sub> − (γ<sub>L</sub> + γ<sub>SL</sub>)</mark>', 'S = 아래 액체(바닥), L = 떨어뜨린 액체')])
             + tbl(['조건', 'γ<sub>S</sub> vs γ<sub>L</sub> + γ<sub>SL</sub>', '결과'], [
                 ['S &gt; 0', '<b>클</b> 때', '바닥이 당기는 힘이 이김 → <b>퍼짐</b>'],
                 ['S &lt; 0', '<b>작을</b> 때', '렌즈를 만들려는 힘이 이김 → <b>퍼지지 않음</b>']])),
        EXAM(ex('20℃, 물 표면장력 60, 물-벤젠 계면장력 28, 벤젠 표면장력 30 (dyne/cm). 벤젠은 물 위에 퍼질까?', [
            ('바닥 S = 물(60), 떨어뜨린 L = 벤젠(30), 계면 SL = 28', ''),
            ('S = 60 − (30 + 28) = <b>2 &gt; 0</b>', '괄호 필수!'),
            ('→ <mark>퍼져나간다</mark>', '')]))
        + warn('슬라이드 숨김 원문 “60 − 28 + 30”은 <b>괄호가 빠진 오타</b>. 그대로 계산하면 62가 나와요. 정답은 60 − (30 + 28) = 2.', '⚠️ 원문 오류')
        + warn('액체 위 액체는 S &gt; 0(양수)도 가능하지만, <b>고체 위 액체(습윤)</b>의 최종 S는 최댓값 0 → 개념 18.', '⚠️ 두 가지 S'),
        'S = γ<sub>S</sub> − (γ<sub>L</sub> + γ<sub>SL</sub>) · 양수면 퍼진다')

problem(2, 3, '벤젠은 물 위에 퍼질까', '12주차 강의 예제 · Summary 3',
        '20℃에서 벤젠 한 방울을 물 위에 떨어뜨렸다. 물의 표면장력 60 dyne/cm, 물과 벤젠의 계면장력 28 dyne/cm, 벤젠의 표면장력 30 dyne/cm라고 할 때 퍼짐계수와 결과는?',
        ['S = −2, 렌즈 형성', 'S = 2, 퍼짐', 'S = 62, 퍼짐', 'S = 58, 퍼짐', 'S = −62, 렌즈 형성'], '② S = 2, 퍼짐',
        [('누가 바닥(S)이고 누가 떨어뜨린 액체(L)인지부터', '바닥 = 물 60, L = 벤젠 30'),
         ('S = γ<sub>S</sub> − (γ<sub>L</sub> + γ<sub>SL</sub>) = 60 − (30 + 28)', ''),
         ('= <b>2 &gt; 0</b> → 퍼진다', '')],
        [(False, '①', '부호 반대'), (True, '②', '✓'), (False, '③', '괄호를 빼고 60 − 28 + 30 (원문 오타 그대로)'), (False, '④', '60 − 30 + 28'), (False, '⑤', '③의 부호 반대')],
        brain='괄호 먼저: 60 − (30 + 28) = 2')

exec(open(os.path.join(HERE, 'gen_b.py'), encoding='utf-8').read())

total = len(pages)
html = ''.join(p.replace('{PN}', f'{i} / {total}') for i, p in enumerate(pages, 1))
css = open(os.path.join(HERE, 'style.css'), encoding='utf-8').read()
open(os.path.join(HERE, 'out.html'), 'w', encoding='utf-8').write(
    f'<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>계면현상 최종 요약본</title><style>{css}</style></head><body>{html}</body></html>')
print(total, 'pages')
