from parts import *
import math

# 확대 그림: 세포 → 소기관 → 막 한 조각 (직접 그린 SVG)
F = "Noto Sans KR"


def T(x, y, s, size=13, col="#2c3038", anchor="middle", w=500):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{col}" text-anchor="{anchor}" font-weight="{w}" font-family="{F}">{s}</text>'


def lead(x1, y1, x2, y2, col="#6c7280"):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{col}" stroke-width="1.2"/><circle cx="{x1}" cy="{y1}" r="2.5" fill="{col}"/>'


def panel(x, w, title, sub):
    return (f'<rect x="{x}" y="8" width="{w}" height="604" rx="16" fill="#fff" stroke="#e4dfd3" stroke-width="1.5"/>'
            + T(x + 16, 38, title, 17, "#23263a", "start", 800) + T(x + 16, 60, sub, 12.5, "#6c7280", "start"))


def zoom(box, tgt):
    """box = 확대할 빨간 네모 (x, y, w, h), tgt = 다음 패널의 왼쪽 위·아래 점"""
    x, y, w, h = box
    r = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="4" fill="none" stroke="#e03131" stroke-width="2.5"/>'
    for (sx, sy), (tx, ty) in zip([(x + w, y), (x + w, y + h)], tgt):
        r += f'<line x1="{sx}" y1="{sy}" x2="{tx}" y2="{ty}" stroke="#e03131" stroke-width="1.6" stroke-dasharray="6 5"/>'
    return r


def arrow_defs():
    return ('<defs><marker id="ar" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#c2410c"/></marker>'
            '<marker id="ab" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#1d4ed8"/></marker></defs>')


def hup(x, y1, y2, n, col="#c2410c"):
    m = "ar"
    return f'<line x1="{x}" y1="{y1}" x2="{x}" y2="{y2}" stroke="{col}" stroke-width="2.6" marker-end="url(#{m})"/>' + (T(x + 6, min(y1, y2) - 4, f"{n}H⁺", 12.5, col, "start", 800) if n else "")


def mito_small(cx, cy, rot=0, s=1.0):
    rx, ry = 26 * s, 12 * s
    zig = " ".join(f"L{cx - rx + 8 + i * 6 * s:.1f},{cy + (5 if i % 2 else -5) * s:.1f}" for i in range(int(7)))
    return (f'<g transform="rotate({rot} {cx} {cy})"><ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="#f6c9a8" stroke="#b5562a" stroke-width="1.8"/>'
            f'<path d="M{cx - rx + 4},{cy} {zig}" fill="none" stroke="#b5562a" stroke-width="1.3"/></g>')


# ═══════════════════ 미토콘드리아 ═══════════════════
def mito_svg():
    o = arrow_defs()
    # ── 패널 1: 세포
    o += panel(10, 430, "① 우리 몸의 세포 하나", "근육·간·뇌… 거의 모든 세포 (지름 약 10–30 μm)")
    o += '<ellipse cx="225" cy="345" rx="190" ry="230" fill="#fff6ec" stroke="#c08a6a" stroke-width="3"/>'
    o += '<path d="M80,250 q30,-14 60,0 t60,0" fill="none" stroke="#c9b7e6" stroke-width="2"/><path d="M90,450 q30,-14 60,0 t60,0" fill="none" stroke="#c9b7e6" stroke-width="2"/>'
    o += '<ellipse cx="190" cy="330" rx="62" ry="52" fill="#e8e2f5" stroke="#7c6bb3" stroke-width="2.5"/><circle cx="200" cy="322" r="14" fill="#c9b7e6"/>'
    for cx, cy, r in [(110, 190, 30), (300, 200, -20), (320, 300, 70), (110, 380, 10), (150, 500, -30), (270, 520, 25), (90, 300, 80), (225, 150, 5)]:
        o += mito_small(cx, cy, r)
    o += mito_small(330, 430, 15, 1.25)
    o += lead(225, 345 - 230, 300, 92) + T(304, 96, "세포막", 12.5, anchor="start")
    o += lead(190, 300, 60, 92) + T(20, 96, "핵 (DNA 대부분)", 12.5, anchor="start")
    o += lead(110, 190, 40, 150) + T(22, 146, "미토콘드리아", 12.5, "#b5562a", "start", 700)
    o += T(225, 598, "세포질 (해당과정이 일어나는 ‘거실’) · 미토콘드리아 수백~수천 개", 12, "#6c7280")
    o += zoom((295, 405, 72, 52), [(470, 120), (470, 590)])
    # ── 패널 2: 미토콘드리아
    o += panel(470, 450, "② 미토콘드리아 한 개", "콩 모양, 길이 약 1–2 μm · 막이 두 겹")
    cx, cy, rx, ry = 695, 345, 205, 125
    o += f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="#fde3cf" stroke="#b5562a" stroke-width="4"/>'
    irx, iry = rx - 18, ry - 18
    # 내막 = 끊기지 않은 한 줄. 안쪽으로 접혀 들어간 주름(크리스타)의 속은 막사이공간과 이어진다
    W2 = 8                                  # 주름 폭의 절반
    top_f = [575, 655, 735, 815]            # 위쪽에서 아래로 들어가는 주름
    bot_f = [615, 695, 775]                 # 아래쪽에서 위로 올라가는 주름

    def ey(x, sgn):
        return cy + sgn * iry * math.sqrt(max(0.0, 1 - ((x - cx) / irx) ** 2))

    def depth(x):
        return 0.62 * iry * math.sqrt(max(0.0, 1 - ((x - cx) / irx) ** 2))
    pts = []
    xs = [cx - irx + i * 2 for i in range(int(irx))]
    d = f"M{cx - irx},{cy} "
    x = cx - irx
    while x <= cx + irx:                    # 위쪽 테두리 (왼 → 오)
        f = next((fx for fx in top_f if fx - W2 <= x < fx - W2 + 2), None)
        if f:
            y0 = ey(f - W2, -1); y1 = ey(f + W2, -1); dp = depth(f)
            d += f"L{f - W2:.1f},{y0:.1f} L{f - W2:.1f},{y0 + dp:.1f} Q{f},{y0 + dp + 2 * W2:.1f} {f + W2:.1f},{y0 + dp:.1f} L{f + W2:.1f},{y1:.1f} "
            x = f + W2
        else:
            d += f"L{x:.1f},{ey(x, -1):.1f} "
        x += 2
    x = cx + irx
    while x >= cx - irx:                    # 아래쪽 테두리 (오 → 왼)
        f = next((fx for fx in bot_f if fx + W2 - 2 < x <= fx + W2), None)
        if f:
            y0 = ey(f + W2, 1); y1 = ey(f - W2, 1); dp = depth(f)
            d += f"L{f + W2:.1f},{y0:.1f} L{f + W2:.1f},{y0 - dp:.1f} Q{f},{y0 - dp - 2 * W2:.1f} {f - W2:.1f},{y0 - dp:.1f} L{f - W2:.1f},{y1:.1f} "
            x = f - W2
        else:
            d += f"L{x:.1f},{ey(x, 1):.1f} "
        x -= 2
    o += f'<path d="{d}Z" fill="#fff4d6" stroke="#c2410c" stroke-width="3" stroke-linejoin="round"/>'
    # ATP 합성효소: 주름 벽에서 기질 쪽으로 튀어나온 막대사탕 (F₁ 머리는 기질 쪽)
    for f in top_f + bot_f:
        sgn = -1 if f in top_f else 1
        base = ey(f, sgn)
        for t in (0.4, 0.8):
            yy = base - sgn * depth(f) * t
            for side in (-1, 1):
                x1 = f + side * W2
                o += f'<line x1="{x1}" y1="{yy:.0f}" x2="{x1 + side * 6}" y2="{yy:.0f}" stroke="#127a64" stroke-width="2"/><circle cx="{x1 + side * 10}" cy="{yy:.0f}" r="4" fill="#127a64"/>'
    for x, y in [(612, 335), (760, 330), (700, 360), (640, 385)]:
        o += f'<circle cx="{x}" cy="{y}" r="2.5" fill="#7c6bb3"/><circle cx="{x + 7}" cy="{y + 3}" r="2.5" fill="#7c6bb3"/>'
    o += '<ellipse cx="735" cy="350" rx="15" ry="9" fill="none" stroke="#9a4a12" stroke-width="1.6"/><ellipse cx="738" cy="352" rx="10" ry="5" fill="none" stroke="#9a4a12" stroke-width="1.2"/>'
    o += lead(cx, cy - ry, 610, 100) + T(560, 104, "외막 (포린 구멍 · 작은 분자 자유 통과)", 12.5, anchor="start")
    o += lead(cx + irx - 2, cy + 6, 905, 186) + T(905, 178, "내막 (H⁺ 못 지나감)", 12.5, anchor="end")
    tip = ey(655, -1) + depth(655) + 2 * W2
    o += lead(655, tip - 4, 512, 170) + T(486, 166, "크리스타 = 내막이 안으로 접힌 주름", 12.5, "#c2410c", "start", 700)
    o += lead(cx - rx + 9, cy, 490, 520) + T(486, 538, "막사이공간 (외막–내막 사이, 크리스타 속까지) = P쪽", 12, "#b5562a", "start", 700)
    o += lead(668, 330, 668, 515) + T(672, 556, "기질 (matrix) = N쪽 · TCA·β-산화", 12.5, "#9a4a12", "start", 700)
    o += lead(825, ey(815, -1) + depth(815) * 0.8, 905, 470) + T(905, 488, "ATP 합성효소 (머리 F₁ → 기질 쪽)", 12, "#127a64", "end", 700)
    o += lead(738, 352, 860, 512) + T(905, 524, "mtDNA · 리보솜", 12.5, "#7c6bb3", "end", 700)
    zt = ey(735, -1)
    o += zoom((718, zt - 6, 34, depth(735) + 26), [(950, 120), (950, 590)])
    # ── 패널 3: 내막 한 조각
    o += panel(950, 440, "③ 내막(크리스타 벽) 한 조각", "주름 벽 한 부분을 옆으로 눕혀 확대 · 복합체 ≈ 10–20 nm")
    X0, X1, y1, y2 = 962, 1378, 300, 362
    o += T(1170, 92, "막사이공간 (P쪽) — H⁺ 많음, 산성, ＋", 13, "#b5562a", "middle", 700)
    o += T(1170, 596, "기질 (N쪽) — H⁺ 적음, 알칼리, −", 13, "#9a4a12", "middle", 700)
    o += f'<rect x="{X0}" y="{y1}" width="{X1 - X0}" height="{y2 - y1}" fill="#fbf1d8"/>'
    o += "".join(f'<circle cx="{x}" cy="{y1}" r="4.5" fill="#e9d9b6"/><circle cx="{x}" cy="{y2}" r="4.5" fill="#e9d9b6"/>' for x in range(X0 + 4, X1, 11))

    def cx_(x, y, w, h, fill, label, sub=""):
        r = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{fill}" stroke="#3a3f4b" stroke-width="1.6"/>' + T(x + w / 2, y + h / 2 + 5, label, 15, "#23263a", "middle", 800)
        return r + (T(x + w / 2, y + h / 2 + 22, sub, 10.5, "#3a3f4b") if sub else "")
    o += cx_(972, 262, 62, 140, "#f6b9c3", "I", "FMN·Fe-S") + f'<rect x="985" y="402" width="36" height="58" rx="10" fill="#f6b9c3" stroke="#3a3f4b" stroke-width="1.6"/>'
    o += cx_(1042, 335, 44, 90, "#f9d29c", "II", "FAD")
    o += '<ellipse cx="1106" cy="331" rx="20" ry="13" fill="#fde68a" stroke="#a16207" stroke-width="1.6"/>' + T(1106, 336, "Q", 13, "#7a5300", "middle", 800)
    o += cx_(1130, 262, 64, 140, "#bcd3f5", "III", "b·c₁·Fe-S")
    o += '<circle cx="1216" cy="226" r="16" fill="#f6b9c3" stroke="#3a3f4b" stroke-width="1.6"/>' + T(1216, 231, "c", 13, "#23263a", "middle", 800)
    o += cx_(1236, 262, 62, 140, "#c5e8d4", "IV", "Cuₐ·a·a₃")
    o += '<rect x="1318" y="290" width="44" height="82" rx="8" fill="#d9d2f2" stroke="#3a3f4b" stroke-width="1.6"/><rect x="1334" y="372" width="12" height="32" fill="#d9d2f2" stroke="#3a3f4b" stroke-width="1.4"/><circle cx="1340" cy="436" r="32" fill="#d9d2f2" stroke="#3a3f4b" stroke-width="1.6"/>'
    o += T(1340, 330, "F₀", 13, "#23263a", "middle", 800) + T(1340, 441, "F₁", 13, "#23263a", "middle", 800)
    o += hup(1003, 255, 150, 4) + hup(1162, 255, 150, 4) + hup(1267, 255, 150, 2)
    o += f'<line x1="1350" y1="150" x2="1350" y2="250" stroke="#c2410c" stroke-width="2.6" marker-end="url(#ar)"/><line x1="1350" y1="250" x2="1342" y2="290" stroke="#c2410c" stroke-width="2.6"/>'
    o += T(1385, 142, "H⁺ 돌아옴", 11.5, "#c2410c", "end", 800)
    o += ('<path d="M995,505 L1003,410 L1003,345 L1086,335 L1140,330 L1180,270 L1210,240 L1245,270 L1262,400 L1262,500" fill="none" stroke="#1d4ed8" stroke-width="2.6" stroke-dasharray="7 4" marker-end="url(#ab)"/>')
    o += '<path d="M1064,470 L1064,425 L1092,345" fill="none" stroke="#1d4ed8" stroke-width="2.2" stroke-dasharray="5 4"/>'
    o += T(990, 525, "NADH → NAD⁺", 12.5, "#1d4ed8", "middle", 700) + T(1064, 488, "숙신산 → 푸마르산", 11.5, "#1d4ed8", "middle", 700)
    o += T(1262, 520, "½O₂ + 2H⁺ → H₂O", 12.5, "#1d4ed8", "middle", 700) + T(1340, 490, "ADP + Pᵢ → ATP", 12, "#127a64", "middle", 800)
    o += T(1170, 560, "파랑 점선 = 전자(e⁻) · 빨강 = H⁺ (4 + 4 + 2 = 10)", 12, "#6c7280")
    return f'<svg viewBox="0 0 1400 620" preserveAspectRatio="xMidYMid meet" style="width:100%;height:100%">{o}</svg>'


# ═══════════════════ 엽록체 ═══════════════════
def chloro_small(cx, cy, rot=0, s=1.0):
    rx, ry = 24 * s, 11 * s
    st = "".join(f'<line x1="{cx - rx + 7 + i * 7 * s:.1f}" y1="{cy - 5 * s:.1f}" x2="{cx - rx + 7 + i * 7 * s:.1f}" y2="{cy + 5 * s:.1f}" stroke="#2f6b1f" stroke-width="2.2"/>' for i in range(6))
    return f'<g transform="rotate({rot} {cx} {cy})"><ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="#8fd17a" stroke="#2f6b1f" stroke-width="1.8"/>{st}</g>'


def chl_svg():
    o = arrow_defs()
    # ── 패널 1: 잎 → 엽육세포
    o += panel(10, 430, "① 식물 잎의 엽육세포", "사람 몸엔 없음! 잎 속 초록 세포 (약 30–50 μm)")
    o += '<path d="M40,150 C60,90 150,80 190,110 C160,150 90,170 40,150 Z" fill="#9bd27f" stroke="#2f6b1f" stroke-width="2"/><line x1="40" y1="150" x2="185" y2="112" stroke="#2f6b1f" stroke-width="1.5"/>'
    o += T(118, 186, "잎", 12.5, "#2f6b1f", "middle", 700)
    o += f'<line x1="150" y1="120" x2="215" y2="215" stroke="#2f6b1f" stroke-width="1.4" stroke-dasharray="5 4"/>'
    o += '<rect x="70" y="210" width="320" height="370" rx="26" fill="#f2f8ec" stroke="#3f7d2a" stroke-width="7"/>'
    o += '<rect x="115" y="255" width="230" height="280" rx="40" fill="#e3f0fb" stroke="#8fb4d8" stroke-width="2"/>'
    o += '<ellipse cx="300" cy="510" rx="34" ry="26" fill="#e8e2f5" stroke="#7c6bb3" stroke-width="2"/>'
    for cx, cy, r in [(98, 250, 80), (98, 330, 90), (98, 420, 85), (98, 500, 95), (160, 233, 0), (240, 233, 5), (320, 233, -5), (362, 300, 90), (362, 390, 85), (160, 557, 0), (230, 557, -5)]:
        o += chloro_small(cx, cy, r)
    o += chloro_small(362, 470, 90, 1.25)
    o += T(230, 400, "액포 (물주머니)", 12.5, "#4a7aa8", "middle", 700)
    o += lead(70, 380, 30, 380) + T(24, 372, "세포벽", 11.5, "#3f7d2a", "start", 700)
    o += T(300, 515, "핵", 12, anchor="middle")
    o += zoom((336, 438, 52, 66), [(470, 120), (470, 590)])
    o += T(225, 600, "엽록체 수십 개가 세포 가장자리에 줄지어 있음", 12, "#2f6b1f", "middle", 700)
    # ── 패널 2: 엽록체
    o += panel(470, 450, "② 엽록체 한 개", "렌즈 모양, 길이 약 5–10 μm · 막 두 겹 + 틸라코이드")
    cx, cy, rx, ry = 695, 345, 205, 125
    o += f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="#f2f8ec" stroke="#2f6b1f" stroke-width="4"/>'
    o += f'<ellipse cx="{cx}" cy="{cy}" rx="{rx - 10}" ry="{ry - 10}" fill="#eaf6e2" stroke="#3f7d2a" stroke-width="2.5"/>'
    stacks = [(560, 330), (635, 290), (640, 395), (720, 330), (800, 290), (805, 395)]
    for i, (sx, sy) in enumerate(stacks[:-1]):
        nx, ny = stacks[i + 1]
        o += f'<line x1="{sx + 25}" y1="{sy}" x2="{nx - 25}" y2="{ny}" stroke="#2f6b1f" stroke-width="7" stroke-linecap="round"/><line x1="{sx + 25}" y1="{sy}" x2="{nx - 25}" y2="{ny}" stroke="#fde7d4" stroke-width="3" stroke-linecap="round"/>'
    for sx, sy in stacks:
        for k in range(5):
            o += f'<rect x="{sx - 28}" y="{sy - 27 + k * 11.5}" width="56" height="10" rx="5" fill="#fde7d4" stroke="#3f8f2c" stroke-width="2.4"/>'
    o += lead(cx, cy - ry, 610, 100) + T(560, 104, "외막 · 내막 (내막에 Pᵢ–삼탄당 인산 역수송체)", 12.5, anchor="start")
    o += lead(640, 395 - 4, 520, 520) + T(486, 538, "그라나 = 틸라코이드 동전 탑 (PSII 많음)", 12.5, "#2f6b1f", "start", 700)
    o += lead(762, 312, 900, 170) + T(905, 160, "스트로마 라멜라 (PSI·ATP 합성효소)", 12, "#4f9a3a", "end", 700)
    o += lead(760, 450, 760, 556) + T(764, 556, "스트로마 = N쪽 · 캘빈 회로", 12.5, "#9a4a12", "start", 700)
    o += lead(810, 299, 905, 470) + T(905, 488, "틸라코이드 내강(주머니 속) = P쪽", 12.5, "#b5562a", "end", 700)
    o += T(486, 586, "초록 테두리 = 틸라코이드 막 · 살구색 = 내강 · 연두 = 스트로마", 11.5, "#6c7280", "start")
    o += zoom((692, 296, 56, 26), [(950, 120), (950, 590)])
    # ── 패널 3: 틸라코이드 막 한 조각 (위 = 내강 P, 아래 = 스트로마 N)
    o += panel(950, 440, "③ 틸라코이드 막 한 조각", "명반응의 무대 (위 = 내강, 아래 = 스트로마)")
    X0, X1, y1, y2 = 962, 1378, 300, 362
    o += T(1170, 92, "틸라코이드 내강 (P쪽) — H⁺ 많음, pH ≈ 5", 13, "#b5562a", "middle", 700)
    o += T(1170, 596, "스트로마 (N쪽) — pH ≈ 8, 캘빈 회로", 13, "#9a4a12", "middle", 700)
    o += f'<rect x="{X0}" y="{y1}" width="{X1 - X0}" height="{y2 - y1}" fill="#fbf1d8"/>'
    o += "".join(f'<circle cx="{x}" cy="{y1}" r="4.5" fill="#e9d9b6"/><circle cx="{x}" cy="{y2}" r="4.5" fill="#e9d9b6"/>' for x in range(X0 + 4, X1, 11))

    def bx(x, y, w, h, fill, label, sub=""):
        r = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{fill}" stroke="#3a3f4b" stroke-width="1.6"/>' + T(x + w / 2, y + h / 2 + 5, label, 14, "#23263a", "middle", 800)
        return r + (T(x + w / 2, y + h / 2 + 21, sub, 10.5, "#3a3f4b") if sub else "")
    o += bx(970, 262, 70, 140, "#a8dca0", "PSII", "P680·Pheo")
    o += '<rect x="978" y="222" width="54" height="36" rx="8" fill="#f9d29c" stroke="#3a3f4b" stroke-width="1.4"/>' + T(1005, 245, "Mn₄", 12, "#23263a", "middle", 800)
    o += T(1005, 210, "2H₂O → O₂ + 4H⁺", 11.5, "#c2410c", "middle", 800)
    o += '<ellipse cx="1066" cy="331" rx="20" ry="13" fill="#fde68a" stroke="#a16207" stroke-width="1.6"/>' + T(1066, 336, "PQ", 11.5, "#7a5300", "middle", 800)
    o += bx(1092, 262, 64, 140, "#bcd3f5", "b₆f", "Q 회로")
    o += '<circle cx="1180" cy="226" r="17" fill="#9fc7ef" stroke="#3a3f4b" stroke-width="1.6"/>' + T(1180, 231, "PC", 11.5, "#23263a", "middle", 800)
    o += bx(1204, 262, 70, 140, "#a8dca0", "PSI", "P700·Fe-S")
    o += '<rect x="1214" y="410" width="54" height="34" rx="8" fill="#f6b9c3" stroke="#3a3f4b" stroke-width="1.4"/>' + T(1241, 432, "Fd·FNR", 11, "#23263a", "middle", 800)
    o += T(1241, 462, "NADP⁺ → NADPH", 11.5, "#1d4ed8", "middle", 800)
    o += '<rect x="1300" y="290" width="44" height="82" rx="8" fill="#d9d2f2" stroke="#3a3f4b" stroke-width="1.6"/><rect x="1316" y="372" width="12" height="32" fill="#d9d2f2" stroke="#3a3f4b" stroke-width="1.4"/><circle cx="1322" cy="436" r="32" fill="#d9d2f2" stroke="#3a3f4b" stroke-width="1.6"/>'
    o += T(1322, 330, "CF₀", 12, "#23263a", "middle", 800) + T(1322, 441, "CF₁", 12, "#23263a", "middle", 800)
    o += T(1322, 490, "ADP + Pᵢ → ATP", 12, "#127a64", "middle", 800)
    sun = lambda x, y, tx, ty: f'<circle cx="{x}" cy="{y}" r="12" fill="#fde68a" stroke="#f59e0b" stroke-width="2"/><line x1="{x}" y1="{y}" x2="{tx}" y2="{ty}" stroke="#f59e0b" stroke-width="2.4" stroke-dasharray="4 3"/>' + T(x, y - 17, "빛", 11.5, "#b45309", "middle", 800)
    o += sun(1072, 246, 1042, 272) + sun(1290, 232, 1272, 270)
    o += hup(1124, 410, 150, 0) + T(1130, 150, "H⁺ (b₆f)", 12, "#c2410c", "start", 800)
    o += f'<line x1="1352" y1="150" x2="1352" y2="250" stroke="#c2410c" stroke-width="2.6" marker-end="url(#ar)"/><line x1="1352" y1="250" x2="1340" y2="290" stroke="#c2410c" stroke-width="2.6"/>'
    o += T(1360, 142, "H⁺ 나옴", 11.5, "#c2410c", "end", 800)
    o += '<path d="M1005,262 L1030,340 L1066,331 L1100,310 L1150,250 L1180,240 L1215,280 L1240,400" fill="none" stroke="#1d4ed8" stroke-width="2.6" stroke-dasharray="7 4" marker-end="url(#ab)"/>'
    return f'<svg viewBox="0 0 1400 620" preserveAspectRatio="xMidYMid meet" style="width:100%;height:100%">{o}</svg>'


def page(pid, n, title, sub, svg, note, cards):
    cs = "".join(f'<div class="card {k}"><div class="ct">{t}</div>{b}</div>' for k, t, b in cards)
    return dict(t="r", id=pid, html=f"""
<div class="hd"><span class="bd">확대 그림 {n}</span><div class="tt"><h1>{title}</h1><div class="sb">{sub}</div></div><span class="pt">{P0}</span></div>
<div style="flex:1;min-height:0;margin-top:6px">{svg}</div>
<div class="cols3" style="flex:none;font-size:.95em">{cs}</div>
<div class="one" style="background:#127a64"><span class="lb">🔍 축척</span><span>{note}</span></div>""")


E = [
    page("f-zoom1", "①", "세포 → 미토콘드리아 → 내막: 어디를 확대한 걸까?", "Animal cell → mitochondrion → inner membrane · 빨간 네모를 따라 오른쪽으로 확대",
         mito_svg(), "세포(약 20 μm) → 미토콘드리아(약 1–2 μm, 약 10배 확대) → 막의 복합체(약 10 nm, 약 100배 더 확대). 거의 모든 세포에 있고, 성숙한 적혈구에만 없다.",
         [("", "① 세포에서 일어나는 일", "밥 → 포도당이 <b>세포질</b>에서 해당과정 → 피루브산·NADH가 미토콘드리아로. 근육·심장·간·뇌·갈색지방처럼 ATP를 많이 쓰는 세포일수록 미토가 많다."),
          ("ana", "② 미토콘드리아에서 일어나는 일", "<b>기질</b>: 피루브산 산화·TCA·β-산화로 NADH·FADH₂ 생산. <b>외막</b>은 체(구멍 많음), <b>내막</b>은 둑(H⁺ 불투과). 내막을 주름(크리스타)지게 해서 면적 ↑ = 발전기 수 ↑"),
          ("tip", "③ 내막에서 일어나는 일 (19장)", "NADH → I → Q → III → cyt c → IV → O₂ 동안 H⁺ 10개를 <b>막사이공간</b>으로 → ATP 합성효소로 돌아오며 ATP. 다음 쪽 빈칸 그림 ①이 바로 이 그림!")]),
    page("f-zoom2", "②", "잎 → 엽육세포 → 엽록체 → 틸라코이드 막", "Leaf mesophyll cell → chloroplast → thylakoid membrane · 사람 몸이 아니라 식물 잎!",
         chl_svg(), "엽육세포(약 40 μm) → 엽록체(약 5–10 μm) → 틸라코이드 막의 광계(약 10–20 nm). 뿌리·감자처럼 빛이 없는 곳엔 엽록체 대신 아밀로플라스트.",
         [("", "① 잎 세포에서 일어나는 일", "햇빛이 잘 드는 <b>잎 엽육세포</b>에 엽록체가 몰려 있다. 기공으로 CO₂가 들어오고 O₂가 나간다. 식물 세포에도 <b>미토콘드리아는 따로 있다</b>(밤엔 호흡만)."),
          ("ana", "② 엽록체에서 일어나는 일", "<b>틸라코이드 막</b>(동전 탑) = 명반응 → ATP·NADPH. <b>스트로마</b>(물) = 캘빈 회로 → G3P → 수크로스로 세포질에 출하. 미토의 ‘기질’ ↔ 엽록체의 ‘스트로마’."),
          ("tip", "③ 틸라코이드 막에서 일어나는 일", "H₂O → PSII → PQ → b₆f → PC → PSI → Fd → NADPH. H⁺는 <b>내강</b>에 쌓였다가(pH 5) CF₀CF₁으로 스트로마에 나오며 ATP. 다음 쪽 빈칸 그림 ②와 짝!")]),
]
