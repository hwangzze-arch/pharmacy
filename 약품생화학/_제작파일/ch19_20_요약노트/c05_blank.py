from parts import *

# 백지 복습용 빈칸 그림: 막과 상자 틀만 있고 이름·화살표는 직접 채운다

CSS = """<style>
.bw{display:flex;gap:14px;margin-top:9px;flex:1;min-height:0;}
.bw .real{flex:1;display:flex;flex-direction:column;gap:6px;min-width:0;}
.bw .zoom{background:#fde8e8;border:1px solid #f5b5b5;border-radius:8px;color:#b91c1c;font-weight:700;text-align:center;font-size:.9em;padding:2px 6px;}
.bw .fig2{flex:1;min-height:0;background:#fff;border:1px solid var(--line);border-radius:12px;padding:6px;}
.bw .fig2 svg{width:100%;height:100%;}
.bw .rcol{flex:3;display:flex;flex-direction:column;gap:7px;min-width:0;}
.bw .chk{flex:none;display:flex;gap:7px;font-size:.9em;}
.bw ol.two{columns:2;column-gap:18px;}
.bw .chk ol{margin:0;padding-left:1.2em;} .bw .chk li{margin-bottom:3px;}
</style>"""


def svg_text(x, y, s, size=15, col="#6c7280", anchor="middle", w=500):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{col}" text-anchor="{anchor}" font-weight="{w}" font-family="Noto Sans KR">{s}</text>'


def blank_line(x, y, w):
    return f'<line x1="{x}" y1="{y}" x2="{x + w}" y2="{y}" stroke="#9aa0ac" stroke-width="1.4"/>'


def box(x, y, w, h, n, dash=True, r=14):
    d = ' stroke-dasharray="7 5"' if dash else ""
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="#fbfaf7" stroke="#8a8fa0" stroke-width="2"{d}/>'
            + svg_text(x + 14, y + 22, n, 14, "#c2410c", "start", 800) + blank_line(x + 12, y + h - 14, w - 24))


def membrane(y1, y2, W=1000):
    beads = "".join(f'<circle cx="{x}" cy="{y1}" r="5" fill="#e9d9b6"/><circle cx="{x}" cy="{y2}" r="5" fill="#e9d9b6"/>' for x in range(10, W, 14))
    return f'<rect x="0" y="{y1}" width="{W}" height="{y2 - y1}" fill="#fbf1d8"/>' + beads


def page(pid, n, title, sub, svg, checklist, grade, real, cap, match):
    rows = "".join(f"<tr><td>{a}</td><td>→ {b}</td></tr>" for a, b in match)
    return dict(t="r", id=pid, html=f"""{CSS}
<div class="hd"><span class="bd">백지 복습 {n}</span><div class="tt"><h1>{title}</h1><div class="sb">{sub}</div></div><span class="pt">{P0}</span></div>
<div class="bw"><div class="real"><div class="fig" style="padding:4px"><img src="img/{real}" style="max-height:255px"><div class="cap">{cap}</div></div>
<div class="zoom">🔍 빨간 원을 확대하면 → 오른쪽 그림</div>
<table class="t" style="margin:0;font-size:.9em"><tr><th colspan="2">실제 그림 ↔ 빈칸 그림 짝짓기</th></tr>{rows}</table></div>
<div class="rcol"><div class="fig2">{svg}</div>
<div class="chk"><div class="card tip" style="flex:3"><div class="ct">✏️ 이 순서로 채우기 &nbsp;<span style="font-weight:400;font-size:.92em"><b style="color:#1d4ed8">파랑</b> 전자 · <b style="color:#c2410c">빨강</b> H⁺(개수) · <b>검정</b> 이름·억제제 ✕</span></div><ol class="two">{checklist}</ol></div>
<div class="card trap" style="flex:1"><div class="ct">✅ 채점</div>{grade}</div></div></div></div>""")


def frame(body, top, bot, total):
    """위 라벨 / 그림(아래로 70 이동) / 아래 라벨 / 합계 줄 — 세로 700"""
    out = svg_text(20, 30, top, 17, "#2c3038", "start", 700)
    out += svg_text(20, 56, "가운데 노란 띠(막) = ______________", 15, "#8a6d2a", "start", 700)
    out += f'<g transform="translate(0,70)">{body}</g>'
    out += svg_text(20, 628, bot, 17, "#2c3038", "start", 700)
    out += f'<rect x="10" y="648" width="980" height="40" rx="10" fill="#fff7ed" stroke="#fed7aa"/>' + svg_text(500, 674, total, 15, "#9a3412", "middle", 700)
    return f'<svg viewBox="0 0 1000 700" preserveAspectRatio="xMidYMid meet">{out}</svg>'


# ── 미토콘드리아
W, H = 1000, 560
mtop = "P쪽 = ______________ (H⁺ 많음 · pH ___ · 전하 ___)"
mbot = "N쪽 = ______________ (H⁺ 적음 · pH ___ · 전하 ___)"
m = membrane(215, 305)
m += box(40, 150, 150, 230, "①")            # Complex I
m += box(225, 260, 110, 120, "②")           # Complex II (기질 쪽에만 붙음)
m += f'<ellipse cx="385" cy="260" rx="38" ry="24" fill="#fff" stroke="#8a8fa0" stroke-width="2" stroke-dasharray="6 4"/>' + svg_text(385, 266, "③", 14, "#c2410c", "middle", 800)
m += box(445, 150, 150, 230, "④")           # Complex III
m += f'<circle cx="640" cy="120" r="28" fill="#fff" stroke="#8a8fa0" stroke-width="2" stroke-dasharray="6 4"/>' + svg_text(640, 126, "⑤", 14, "#c2410c", "middle", 800)
m += box(670, 150, 140, 230, "⑥")           # Complex IV
# ATP 합성효소: F0(막 속) + F1(기질 쪽 공)
m += f'<rect x="860" y="205" width="90" height="110" rx="12" fill="#fbfaf7" stroke="#8a8fa0" stroke-width="2" stroke-dasharray="7 5"/>'
m += f'<rect x="896" y="315" width="18" height="40" fill="#fbfaf7" stroke="#8a8fa0" stroke-width="2" stroke-dasharray="5 4"/>'
m += f'<circle cx="905" cy="405" r="48" fill="#fbfaf7" stroke="#8a8fa0" stroke-width="2" stroke-dasharray="7 5"/>'
m += svg_text(872, 228, "⑦", 14, "#c2410c", "start", 800) + svg_text(905, 410, "⑧", 14, "#c2410c", "middle", 800)
# 출발·도착 빈칸
m += svg_text(70, 440, "______ → ______ + H⁺", 15, "#2c3038", "start", 700) + svg_text(70, 460, "(①에 전자를 주는 연료)", 12)
m += svg_text(240, 440, "______ → ______", 15, "#2c3038", "start", 700) + svg_text(240, 460, "(②의 기질)", 12)
m += svg_text(660, 440, "½O₂ + 2H⁺ → ______", 15, "#2c3038", "start", 700)
m += svg_text(905, 488, "ADP + Pᵢ → ______", 14, "#2c3038", "middle", 700)
for x in (115, 520, 740):
    m += svg_text(x, 112, "H⁺ × ___", 15, "#c2410c", "middle", 800)
m += svg_text(280, 112, "H⁺ × ___", 15, "#c2410c", "middle", 800)
mito_svg = frame(m, mtop, mbot, "합계: NADH에서 H⁺ ____개 → ATP ____개 (H⁺ ___개당 1)  ·  숙신산에서 H⁺ ____개 → ATP ____개")

mito = page("f-blank1", "①", "미토콘드리아 내막 — 빈칸 그림", "Respiratory chain + ATP synthase · 막과 상자 틀만 있어. 이름과 화살표는 네가 채운다",
    mito_svg,
    "<li>P쪽·N쪽·막의 이름과 pH·전하(+/−)</li><li>①–⑧ 상자 이름 (복합체·운반체·F₀·F₁)</li>"
    "<li><b style='color:#1d4ed8'>파랑</b>: NADH → … → O₂, 숙신산은 어디로 합류?</li><li><b style='color:#c2410c'>빨강</b>: 상자마다 H⁺ 몇 개, 어느 방향?</li>"
    "<li>물레방아: H⁺가 ⑦을 지나 ⑧로, γ축 회전 → ATP</li><li>억제제 ✕: 로테논 · 안티마이신 A · CN⁻/CO · 올리고마이신, 짝풀림제 DNP는 어디에 구멍?</li>",
    "다 그렸으면 {PAGE:f-map}쪽 큰 그림 · {REF:c-sum} · {REF:c-order}로 맞춰 보기",
    "real_mito.jpg", "원본 슬라이드 28 — 미토콘드리아 (빨간 원 = 크리스타 한 조각)",
    [("Outer membrane (외막)", "그림 밖 (포린 · 자유 통과)"), ("외막과 내막 사이", "____쪽 (이름: ________)"),
     ("Inner membrane · Cristae", "노란 띠 (H⁺ ____투과)"), ("Matrix (기질)", "____쪽 · TCA 회로가 도는 곳"),
     ("ATP synthase (F₀F₁)", "⑦ + ⑧ — F₁은 ____ 쪽으로 돌출")])

# ── 엽록체
ctop = "P쪽 = ______________ (H⁺ 많음 · pH 약 ___)"
cbot = "N쪽 = ______________ (H⁺ 적음 · pH 약 ___) — 여기서 캘빈 회로"
c = membrane(215, 305)
sun = lambda x: f'<circle cx="{x}" cy="420" r="16" fill="#fde68a" stroke="#f59e0b" stroke-width="2"/>' + svg_text(x, 455, "빛 (___ nm)", 13, "#b45309", "middle", 700)
c += box(40, 150, 150, 230, "①") + sun(115)            # PSII
c += f'<rect x="55" y="70" width="120" height="50" rx="10" fill="#fbfaf7" stroke="#8a8fa0" stroke-width="2" stroke-dasharray="6 4"/>' + svg_text(68, 92, "②", 14, "#c2410c", "start", 800)  # OEC
c += svg_text(115, 140, "____ → O₂ + ___H⁺", 13, "#2c3038", "middle", 700)
c += f'<ellipse cx="245" cy="260" rx="38" ry="24" fill="#fff" stroke="#8a8fa0" stroke-width="2" stroke-dasharray="6 4"/>' + svg_text(245, 266, "③", 14, "#c2410c", "middle", 800)
c += box(300, 150, 150, 230, "④")                      # b6f
c += f'<circle cx="505" cy="120" r="28" fill="#fff" stroke="#8a8fa0" stroke-width="2" stroke-dasharray="6 4"/>' + svg_text(505, 126, "⑤", 14, "#c2410c", "middle", 800)  # PC
c += box(550, 150, 150, 230, "⑥") + sun(625)           # PSI
c += f'<rect x="715" y="350" width="120" height="50" rx="10" fill="#fbfaf7" stroke="#8a8fa0" stroke-width="2" stroke-dasharray="6 4"/>' + svg_text(728, 372, "⑦", 14, "#c2410c", "start", 800)  # Fd·FNR
c += svg_text(775, 430, "NADP⁺ → ______", 14, "#2c3038", "middle", 700)
c += f'<rect x="860" y="205" width="90" height="110" rx="12" fill="#fbfaf7" stroke="#8a8fa0" stroke-width="2" stroke-dasharray="7 5"/>'
c += f'<rect x="896" y="315" width="18" height="40" fill="#fbfaf7" stroke="#8a8fa0" stroke-width="2" stroke-dasharray="5 4"/>'
c += f'<circle cx="905" cy="405" r="48" fill="#fbfaf7" stroke="#8a8fa0" stroke-width="2" stroke-dasharray="7 5"/>'
c += svg_text(872, 228, "⑧", 14, "#c2410c", "start", 800) + svg_text(905, 410, "⑨", 14, "#c2410c", "middle", 800)
c += svg_text(905, 488, "ADP + Pᵢ → ______", 14, "#2c3038", "middle", 700)
c += svg_text(375, 112, "H⁺ × ___", 15, "#c2410c", "middle", 800)
chl_svg = frame(c, ctop, cbot, "O₂ 1개당: 광자 ___개 · H⁺ ___개(②에서 ___ + ④에서 ___) · ΔpH ≈ ___ · ATP 약 ___개 · NADPH ___개")

chloro = page("f-blank2", "②", "엽록체 틸라코이드 막 — 빈칸 그림", "Z scheme + photophosphorylation · 미토콘드리아 그림과 나란히 놓고 비교하기",
    chl_svg,
    "<li>P쪽·N쪽·막의 이름과 pH (미토와 같은 자리!)</li><li>①–⑨ 이름 (광계·OEC·운반체·Fd/FNR·CF₀·CF₁)</li>"
    "<li><b style='color:#1d4ed8'>파랑</b>: H₂O → … → NADP⁺ (빛은 어디서 두 번?)</li><li><b style='color:#c2410c'>빨강</b>: H⁺가 쌓이는 곳 두 군데</li>"
    "<li>순환 흐름을 <b style='color:#1d4ed8'>점선 파랑</b>으로 (⑥ → ? → ④ → ⑤ → ⑥)</li><li>억제제 ✕: DCMU · 벤투리시딘(CF₀)</li>",
    "다 그렸으면 {PAGE:f-map}쪽 큰 그림 · {REF:c-zscheme} · {REF:c-photophos}(미토 비교표)로 맞춰 보기",
    "real_chl.jpg", "원본 슬라이드 97 — 엽록체 (빨간 원 = 틸라코이드 더미)",
    [("Outer · Inner membrane", "그림 밖 (내막엔 Pᵢ–삼탄당 인산 역수송체)"), ("Thylakoid membrane", "노란 띠 (광계·b₆f·CF₀CF₁)"),
     ("틸라코이드 안쪽 공간", "____쪽 (이름: ________)"), ("Stroma (스트로마)", "____쪽 · ________ 회로"),
     ("동전 탑 (Grana)", "PSII가 주로 있는 곳 = ①")])

E = [mito, chloro]
