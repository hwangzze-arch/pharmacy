# -*- coding: utf-8 -*-
"""직접 그린 그림: 검정곡선 · 시차오차 · 실험 흐름"""

STYLE = """<style>
.chart,.svgf{width:100%;height:auto;display:block;}
.chart .grid{stroke:#e3e7ee;stroke-width:1;} .chart .zero{stroke:#333;stroke-width:1.4;}
.chart .band{fill:#e7f6ec;} .chart .tol{stroke:#1f7a3f;stroke-width:1.3;stroke-dasharray:6 4;}
.chart .tolt{fill:#1f7a3f;font-size:11px;font-weight:700;}
.chart .ln{fill:none;stroke:#4651c8;stroke-width:2.4;} .chart .pt{fill:#fff;stroke:#4651c8;stroke-width:2.4;}
.chart .lab{font-size:11px;fill:#4651c8;font-weight:700;} .chart .ax{font-size:11px;fill:#555;}
.chart .axt{font-size:12px;fill:#333;font-weight:700;} .chart .ttl{font-size:13px;font-weight:700;fill:#23263a;}
.svgf .tube{fill:#f4f8fd;stroke:#7a8aa3;stroke-width:2;} .svgf .liq{fill:#cfe2fb;}
.svgf .tick line{stroke:#333;stroke-width:1.6;} .svgf .tick text{font-size:12px;fill:#333;}
.svgf .eye{fill:#fff;stroke:#888;stroke-width:2;} .svgf .eye.ok{stroke:#1f7a3f;stroke-width:3;}
.svgf .sight{stroke:#1f7a3f;stroke-width:2;} .svgf .sight.dim{stroke:#c0392b;stroke-dasharray:5 4;stroke-width:1.5;}
.svgf .sm{font-size:11.5px;fill:#444;} .svgf .warn{fill:#c0392b;font-weight:700;} .svgf .okt{fill:#1f7a3f;font-weight:700;}
.svgf .box rect{fill:#fff;stroke:#a9c6e8;stroke-width:1.5;} .svgf .box rect.hl{fill:#eef0fd;stroke:#4651c8;stroke-width:2;}
.svgf .bt text{font-size:12.5px;text-anchor:middle;fill:#222;} .svgf .ar path{stroke:#4651c8;stroke-width:2.5;fill:none;}
</style>"""


def f2(x, sign=False):
    s = f"{x:+.2f}" if sign else f"{x:.2f}"
    return "0.00" if s in ("+0.00", "-0.00") else s.replace("-", "−")


def curve(points, title, ymax=0.12, tol=0.10, w=560, h=300, step=0.02):
    L, R, T, B = 58, 14, 28, 44
    pw, ph = w - L - R, h - T - B
    X = lambda x: L + x / 50 * pw
    Y = lambda y: T + (ymax - y) / (2 * ymax) * ph
    g = []
    for i in range(round(2 * ymax / step) + 1):
        y = -ymax + i * step
        g.append(f'<line x1="{L}" x2="{L+pw}" y1="{Y(y):.1f}" y2="{Y(y):.1f}" class="grid"/>'
                 f'<text x="{L-7}" y="{Y(y)+4:.1f}" class="ax" text-anchor="end">{f2(y, True)}</text>')
    for x in range(0, 51, 10):
        g.append(f'<line y1="{T}" y2="{T+ph}" x1="{X(x):.1f}" x2="{X(x):.1f}" class="grid"/>'
                 f'<text x="{X(x):.1f}" y="{T+ph+17}" class="ax" text-anchor="middle">{x}</text>')
    g.append(f'<rect x="{L}" y="{Y(tol):.1f}" width="{pw}" height="{Y(-tol)-Y(tol):.1f}" class="band"/>')
    for t in (tol, -tol):
        g.append(f'<line x1="{L}" x2="{L+pw}" y1="{Y(t):.1f}" y2="{Y(t):.1f}" class="tol"/>')
    g.append(f'<text x="{L+pw-4}" y="{Y(tol)-5:.1f}" class="tolt" text-anchor="end">허용오차 +0.10</text>')
    g.append(f'<text x="{L+pw-4}" y="{Y(-tol)+14:.1f}" class="tolt" text-anchor="end">−0.10</text>')
    g.append(f'<line x1="{L}" x2="{L+pw}" y1="{Y(0):.1f}" y2="{Y(0):.1f}" class="zero"/>')
    g.append('<polyline points="' + " ".join(f"{X(x):.1f},{Y(y):.1f}" for x, y in points) + '" class="ln"/>')
    for x, y in points:
        g.append(f'<circle cx="{X(x):.1f}" cy="{Y(y):.1f}" r="4.5" class="pt"/>'
                 f'<text x="{X(x):.1f}" y="{Y(y)-10:.1f}" class="lab" text-anchor="middle">{f2(y, True)}</text>')
    g.append(f'<text x="{L+pw/2}" y="{h-5}" class="axt" text-anchor="middle">x축 = 뷰렛 눈금 (mL)</text>')
    g.append(f'<text transform="translate(14,{T+ph/2}) rotate(-90)" class="axt" text-anchor="middle">y축 = 보정치 (mL)</text>')
    g.append(f'<text x="{L}" y="17" class="ttl">{title}</text>')
    return f'<svg viewBox="0 0 {w} {h}" class="chart">{"".join(g)}</svg>'


PARALLAX = """<svg viewBox="0 0 420 240" class="svgf">
<rect x="190" y="20" width="44" height="200" rx="4" class="tube"/>
<path d="M190 120 Q212 136 234 120 L234 220 L190 220 Z" class="liq"/>
<g class="tick"><line x1="190" x2="206" y1="100" y2="100"/><text x="242" y="104">19.6</text>
<line x1="190" x2="212" y1="128" y2="128"/><text x="242" y="132">19.7 ← 정답</text>
<line x1="190" x2="206" y1="156" y2="156"/><text x="242" y="160">19.8</text></g>
<circle cx="60" cy="40" r="11" class="eye"/><text x="78" y="30" class="sm">위에서 봄 → <tspan class="warn">작게(과소)</tspan></text>
<line x1="71" y1="45" x2="212" y2="128" class="sight dim"/>
<circle cx="60" cy="128" r="11" class="eye ok"/><text x="8" y="160" class="sm okt">눈높이 = 메니스커스 바닥</text>
<line x1="71" y1="128" x2="212" y2="128" class="sight"/>
<circle cx="60" cy="214" r="11" class="eye"/><text x="78" y="234" class="sm">아래에서 봄 → <tspan class="warn">크게(과대)</tspan></text>
<line x1="71" y1="209" x2="212" y2="128" class="sight dim"/>
<text x="300" y="60" class="sm">메니스커스의</text><text x="300" y="76" class="sm">맨 아랫부분(오목한</text><text x="300" y="92" class="sm">바닥)을 읽는다</text>
</svg>"""

FLOW = """<svg viewBox="0 0 680 112" class="svgf">
<g class="box"><rect x="4" y="14" width="120" height="66" rx="8"/><rect x="144" y="14" width="120" height="66" rx="8"/>
<rect x="284" y="14" width="120" height="66" rx="8"/><rect x="424" y="14" width="120" height="66" rx="8"/>
<rect x="564" y="14" width="112" height="66" rx="8" class="hl"/></g>
<g class="bt"><text x="64" y="41">뷰렛에서 ~10 mL</text><text x="64" y="61">한 방울씩</text>
<text x="204" y="41">눈금 읽기</text><text x="204" y="61">(소수 둘째 자리)</text>
<text x="344" y="41">저울로 무게</text><text x="344" y="61">(누적, g)</text>
<text x="484" y="41">무게 ÷ 밀도</text><text x="484" y="61">= 실제 부피</text>
<text x="620" y="41">실제 − 눈금</text><text x="620" y="61">= 보정치</text></g>
<g class="ar"><path d="M126 47 h14"/><path d="M266 47 h14"/><path d="M406 47 h14"/><path d="M546 47 h14"/></g>
<text x="340" y="104" class="sm" text-anchor="middle">10 → 20 → 30 → 40 → 50 mL까지 누적 반복 (유인물: 2회 반복)</text>
</svg>"""

# 녹취록 속 우리 조 데이터 (19 °C, ρ = 0.99842)
READ = [0.00, 9.98, 20.04, 29.95, 40.10, 50.00]
MASS = [45.32, 55.28, 65.33, 75.25, 85.38, 95.20]
RHO = 0.99842
ROWS = []
for r, m in zip(READ, MASS):
    w = round(m - MASS[0], 2)
    v = round(w / RHO, 2)
    ROWS.append((r, m, w, v, round(v - r, 2)))
OUR = [(r, c) for r, _, _, _, c in ROWS]
HAND = [(0.04, 0.00), (10.04, -0.01), (20.06, -0.07), (29.95, -0.05), (40.05, -0.11), (50.04, -0.09)]


def our_table(hide=False):
    tr = []
    for r, m, w, v, c in ROWS:
        if hide and r:
            cells = f'<td>{f2(r)}</td><td>{m:.2f}</td><td><span class="blank">?</span></td><td><span class="blank">?</span></td><td><span class="blank">?</span></td>'
        else:
            cells = f'<td>{f2(r)}</td><td>{m:.2f}</td><td>{w:.2f}</td><td>{v:.2f}</td><td><b>{f2(c, True)}</b></td>'
        tr.append(f"<tr>{cells}</tr>")
    return ('<table class="t"><tr><th>눈금 (mL)</th><th>플라스크+물 (g)</th><th>물 무게 (g)</th><th>실제 부피 (mL)</th><th>보정치 (mL)</th></tr>'
            + "".join(tr) + "</table>")
