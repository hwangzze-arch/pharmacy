# -*- coding: utf-8 -*-
"""실험 1 (뷰렛의 검정) 요약 정리 HTML 생성 → render.js 로 PDF 변환"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))

# 녹취록 속 우리 조 데이터 (수온 19 °C)
READ = [0.00, 9.98, 20.04, 29.95, 40.10, 50.00]          # 뷰렛 눈금 (mL, 누적)
MASS = [45.32, 55.28, 65.33, 75.25, 85.38, 95.20]        # 플라스크+물 (g, 누적)
RHO = 0.99842                                            # 19.0 °C 물의 밀도 (유인물 Table 1.2)

rows = []
for r, m in zip(READ, MASS):
    w = round(m - MASS[0], 2)
    v = round(w / RHO, 2)
    rows.append((r, m, w, v, round(v - r, 2)))


def f2(x, sign=False):
    s = f"{x:+.2f}" if sign else f"{x:.2f}"
    return "0.00" if s in ("+0.00", "-0.00") else s


def table_html():
    tr = []
    for r, m, w, v, c in rows:
        cls = ' class="pos"' if c > 0 else (' class="neg"' if c < 0 else "")
        tr.append(f"<tr><td>{f2(r)}</td><td>{m:.2f}</td><td>{w:.2f}</td><td>{v:.2f}</td>"
                  f"<td{cls}><b>{f2(c, True)}</b></td></tr>")
    return "".join(tr)


def curve_svg(points, title, ymax=0.12, tol=0.10, w=640, h=300, step=0.02):
    L, R, T, B = 62, 20, 30, 46
    pw, ph = w - L - R, h - T - B
    X = lambda x: L + x / 50 * pw
    Y = lambda y: T + (ymax - y) / (2 * ymax) * ph
    g = []
    n = round(2 * ymax / step)
    for i in range(n + 1):
        y = -ymax + i * step
        g.append(f'<line x1="{L}" x2="{L+pw}" y1="{Y(y):.1f}" y2="{Y(y):.1f}" class="grid"/>'
                 f'<text x="{L-8}" y="{Y(y)+4:.1f}" class="ax" text-anchor="end">{f2(y, True)}</text>')
    for x in range(0, 51, 10):
        g.append(f'<line y1="{T}" y2="{T+ph}" x1="{X(x):.1f}" x2="{X(x):.1f}" class="grid"/>'
                 f'<text x="{X(x):.1f}" y="{T+ph+18}" class="ax" text-anchor="middle">{x}</text>')
    g.append(f'<rect x="{L}" y="{Y(tol):.1f}" width="{pw}" height="{Y(-tol)-Y(tol):.1f}" class="band"/>')
    for t in (tol, -tol):
        g.append(f'<line x1="{L}" x2="{L+pw}" y1="{Y(t):.1f}" y2="{Y(t):.1f}" class="tol"/>')
    g.append(f'<text x="{L+pw-4}" y="{Y(tol)-5:.1f}" class="tolt" text-anchor="end">제조사 허용오차 +0.10 mL</text>')
    g.append(f'<text x="{L+pw-4}" y="{Y(-tol)+14:.1f}" class="tolt" text-anchor="end">−0.10 mL</text>')
    g.append(f'<line x1="{L}" x2="{L+pw}" y1="{Y(0):.1f}" y2="{Y(0):.1f}" class="zero"/>')
    pts = " ".join(f"{X(x):.1f},{Y(y):.1f}" for x, y in points)
    g.append(f'<polyline points="{pts}" class="ln"/>')
    for x, y in points:
        g.append(f'<circle cx="{X(x):.1f}" cy="{Y(y):.1f}" r="4.5" class="pt"/>'
                 f'<text x="{X(x):.1f}" y="{Y(y)-10:.1f}" class="lab" text-anchor="middle">{f2(y, True)}</text>')
    g.append(f'<text x="{L+pw/2}" y="{h-6}" class="axt" text-anchor="middle">뷰렛 눈금 (mL) — x축</text>')
    g.append(f'<text transform="translate(16,{T+ph/2}) rotate(-90)" class="axt" text-anchor="middle">보정치 (mL) — y축</text>')
    g.append(f'<text x="{L}" y="18" class="ttl">{title}</text>')
    return f'<svg viewBox="0 0 {w} {h}" class="chart">{"".join(g)}</svg>'


PARALLAX = """
<svg viewBox="0 0 420 240" class="fig">
  <rect x="190" y="20" width="44" height="200" rx="4" class="tube"/>
  <path d="M190 120 Q212 136 234 120 L234 220 L190 220 Z" class="liq"/>
  <g class="tick">
    <line x1="190" x2="206" y1="100" y2="100"/><text x="242" y="104">19.6</text>
    <line x1="190" x2="212" y1="128" y2="128"/><text x="242" y="132">19.7 ← 정답</text>
    <line x1="190" x2="206" y1="156" y2="156"/><text x="242" y="160">19.8</text>
  </g>
  <circle cx="60" cy="40" r="11" class="eye"/><text x="78" y="30" class="sm">위에서 봄 → <tspan class="warn">작게(과소)</tspan></text>
  <line x1="71" y1="45" x2="212" y2="128" class="sight dim"/>
  <circle cx="60" cy="128" r="11" class="eye ok"/><text x="8" y="160" class="sm okt">눈높이 = 메니스커스 바닥</text>
  <line x1="71" y1="128" x2="212" y2="128" class="sight"/>
  <circle cx="60" cy="214" r="11" class="eye"/><text x="78" y="234" class="sm">아래에서 봄 → <tspan class="warn">크게(과대)</tspan></text>
  <line x1="71" y1="209" x2="212" y2="128" class="sight dim"/>
  <text x="300" y="60" class="sm">메니스커스의</text>
  <text x="300" y="76" class="sm">맨 아랫부분(오목한</text>
  <text x="300" y="92" class="sm">바닥)을 읽는다</text>
</svg>
"""

FLOW = """
<svg viewBox="0 0 680 120" class="fig">
  <g class="box">
    <rect x="4" y="20" width="120" height="70" rx="8"/><rect x="144" y="20" width="120" height="70" rx="8"/>
    <rect x="284" y="20" width="120" height="70" rx="8"/><rect x="424" y="20" width="120" height="70" rx="8"/>
    <rect x="564" y="20" width="112" height="70" rx="8" class="hl"/>
  </g>
  <g class="bt">
    <text x="64" y="48">뷰렛에서 ~10 mL</text><text x="64" y="68">흘려보냄</text>
    <text x="204" y="48">눈금 읽기</text><text x="204" y="68">(소수 둘째 자리)</text>
    <text x="344" y="48">저울로 무게</text><text x="344" y="68">(물 g)</text>
    <text x="484" y="48">무게 ÷ 밀도</text><text x="484" y="68">= 실제 부피</text>
    <text x="620" y="48">실제 − 눈금</text><text x="620" y="68">= 보정치</text>
  </g>
  <g class="ar"><path d="M126 55 h14"/><path d="M266 55 h14"/><path d="M406 55 h14"/><path d="M546 55 h14"/></g>
  <text x="340" y="112" class="sm" text-anchor="middle">10 → 20 → 30 → 40 → 50 mL까지 누적으로 반복</text>
</svg>
"""


def build():
    pts = [(r, c) for r, _, _, _, c in rows]
    hand = [(0.04, 0.00), (10.04, -0.01), (20.06, -0.07), (29.95, -0.05), (40.05, -0.11), (50.04, -0.09)]
    tpl = open(os.path.join(HERE, "template.html"), encoding="utf-8").read()
    out = (tpl.replace("{{TABLE}}", table_html())
              .replace("{{CURVE}}", curve_svg(pts, "우리 조 뷰렛 검정곡선 (녹취록 데이터, 19 °C)"))
              .replace("{{CURVE_HAND}}", curve_svg(hand, "유인물 예시 데이터로 그려 본 검정곡선", ymax=0.14, w=640, h=260))
              .replace("{{PARALLAX}}", PARALLAX)
              .replace("{{FLOW}}", FLOW))
    open(os.path.join(HERE, "out.html"), "w", encoding="utf-8").write(out)
    for r in rows:
        print(r)


if __name__ == "__main__":
    build()
