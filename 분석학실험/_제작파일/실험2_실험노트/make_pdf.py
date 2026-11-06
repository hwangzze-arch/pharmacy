# -*- coding: utf-8 -*-
"""실험2 실험노트: 오려 붙이는 Table I–III + 손으로 옮겨 적을 초안 → note.html (1조, 1회 측정)"""
import math, os

D = os.path.dirname(os.path.abspath(__file__))
FM, A0, VOL = 204.221, 2.042, 100.0
VB_STD, VB_VIN = 19.50, 20.92
C = A0 / FM / (VOL / 1000)
K1, K2 = 10 ** -2.9, 10 ** -5.5
PH = -math.log10(math.sqrt((K1 * K2 * C + K1 * 1e-14) / (K1 + C)))
A = A0 * 20 / VOL
MMOL = A * 1000 / FM
B = MMOL / VB_STD
F = round(B / 0.1, 3)
VIN = 10.00 * 20.00 / VOL
ACG = 0.1 * F * VB_VIN * 60.05e-3
ACID = round(ACG / VIN * 100, 2)
ACID1 = round(0.1 * VB_VIN * 60.05e-3 / VIN * 100, 2)

FONTS = "".join(f'<link rel="stylesheet" href="file://{p}">' for p in (os.path.expanduser(f"~/.fonts/nskr/package/{w}.css") for w in (400, 700)) if os.path.exists(p))
TAG = '<div class="tag">분석학실험 노트 <b>1권</b> · 부착 p.____ · <span class="sig">간인(노트와 겹치게)</span></div>'


def tbl(rows):
    return '<table><tr><th>항목</th><th>값</th><th>계산 / 비고</th></tr>' + "".join(
        f"<tr><td class='l'>{a}</td><td><b>{b}</b></td><td class='l'>{c}</td></tr>" for a, b, c in rows) + "</table>"


T1 = tbl([("KHP 칭량값 A₀", f"{A0:.3f} g", "정밀하게 칭량, 110 °C 건조 생략"),
          ("용량플라스크", f"{VOL:.1f} mL", "물 약 반 → 녹이고 → 표선"),
          ("KHP 몰농도", f"{C:.4f} M", f"{A0:.3f} g ÷ 204.221 g/mol ÷ 0.1000 L"),
          ("이론 pH (중간형)", f"{PH:.2f}", "[H⁺] = √[(K₁K₂C + K₁K<sub>w</sub>)/(K₁ + C)], pK₁ = 2.9, pK₂ = 5.5")])
T2 = tbl([("분취한 KHP 용액", "20.00 mL", "pipet (100 mL 중 20%)"),
          ("적정한 KHP 양 A", f"{A:.4f} g", f"{A0:.3f} × 20.00/100.0"),
          ("KHP 몰수", f"{MMOL:.4f} mmol", "A × 10³ / 204.221"),
          ("뷰렛 시작 → 최종 눈금", "15.00 → 34.50 mL", "지시약 페놀프탈레인 2방울, 무색 → 옅은 분홍"),
          ("NaOH 소비량 V<sub>b</sub>", f"{VB_STD:.2f} mL", "34.50 − 15.00"),
          ("NaOH 농도 B", f"{B:.5f} mmol/mL", "KHP mmol ÷ V<sub>b</sub>"),
          ("규정도계수 f", f"{F:.3f}", "B / 0.100 (제조사 표기 1.000)")])
T3 = tbl([("식초 원액 분취 → 희석", "10.00 mL → 100 mL", "pipet, 용량플라스크"),
          ("희석액 분취량", "20.00 mL", "+ 물 20 mL, 지시약 2방울"),
          ("실제 적정한 식초 원액", f"{VIN:.3f} mL", "10.00 × 20.00/100.0"),
          ("NaOH 소비량 V<sub>b</sub>", f"{VB_VIN:.2f} mL", "표정과 같은 분홍색에서 멈춤"),
          ("초산 (환산량)", f"{ACG:.4f} g", f"0.1 × {F:.3f} × {VB_VIN:.2f} × 60.05 × 10⁻³"),
          ("총산도", f"{ACID:.2f} w/v%", f"{ACG:.4f} g ÷ {VIN:.3f} mL × 100")])

html = f"""<!doctype html><html lang="ko"><head><meta charset="utf-8">{FONTS}<title>실험2 실험노트</title><style>
@page {{ size: A4; margin: 13mm 15mm; }}
body {{ font-family:'Noto Sans KR','Pretendard',sans-serif; color:#222; font-size:10.4pt; line-height:1.6; margin:0; }}
h1 {{ font-size:15pt; margin:0 0 2px; }} .sub {{ color:#666; font-size:9pt; margin-bottom:10px; }}
.cut {{ border:1.4px dashed #888; padding:8px 12px 6px; margin:0 auto 13px; width:160mm; position:relative; break-inside:avoid; }}
.cut::before {{ content:'✂'; position:absolute; top:-11px; left:-4px; background:#fff; color:#888; font-size:13px; }}
.cut h3 {{ font-size:10.5pt; margin:0 0 5px; }}
table {{ border-collapse:collapse; width:100%; font-size:9.4pt; }}
th, td {{ border:1px solid #666; padding:3px 6px; text-align:center; }} th {{ background:#eee; }} td.l {{ text-align:left; }}
.tag {{ font-size:8.4pt; color:#555; margin-top:4px; text-align:right; }} .sig {{ border-bottom:1px solid #999; padding:0 18px; }}
.brk {{ break-before:page; }}
h2 {{ font-size:12pt; border-left:4px solid #4651c8; padding-left:8px; margin:13px 0 5px; }}
.draft p, .draft li {{ margin:2px 0; }} ol, ul {{ margin:2px 0 6px; padding-left:20px; }}
.hint {{ background:#fff4cc; border:1px solid #efd27a; border-radius:6px; padding:6px 10px; font-size:9.3pt; margin:8px 0; }}
.eq {{ background:#f4f0fb; border-radius:6px; padding:4px 10px; margin:3px 0; display:inline-block; }}
</style></head><body>

<h1>실험 2. 식초 중의 총 산도 측정 — 실험노트 부착용 (1조)</h1>
<div class="sub">점선대로 오려 <b>4면 모두</b> 붙이고, <b>노트 번호(1권)와 부착 페이지 번호</b>를 적고, 부착물과 노트 공란에 <b>겹치게</b> 서명(간인)</div>

<div class="cut"><h3>Table I. KHP 일차표준용액의 제조 (1조 제조)</h3>{T1}{TAG}</div>
<div class="cut"><h3>Table II. 0.1 M NaOH 표준액의 표정 (1회)</h3>{T2}{TAG}</div>
<div class="cut"><h3>Table III. 식초의 총 산도 (1회, f = {F:.3f} 사용)</h3>{T3}{TAG}</div>

<div class="draft brk">
<h1>실험노트 초안 — 볼펜으로 옮겨 적기</h1>
<div class="hint">머리말/꼬리말: <b>1권 · p.__ · 서명</b> (매 페이지) · 실험일자 2026. __. __.(목, 실험한 날) · 1조. 큰 빈 공간만 빗금 한 줄.</div>

<h2>제목</h2><p>실험 2. 지시약을 이용한 식초 중의 총 산도 측정</p>

<h2>1. 목적</h2>
<p>표정을 통해 염기 표준액의 정확한 농도를 결정하고, 중화적정법의 예로서 이 표준액을 이용하여 식초 중의 총 산도를 측정한다.</p>

<h2>2. 원리</h2>
<ul><li><b>NaOH 표준액의 표정</b>: 일차표준물질 KHP(potassium hydrogen phthalate, FM 204.221, pK₁ = 2.9, pK₂ = 5.5)는 프탈산의 중간형으로, 남은 –COOH 하나가 NaOH와 1 : 1로 반응한다.<br>
<span class="eq">KHP + NaOH → KNaP + H₂O</span><br>
<span class="eq">A(g) / 204.221 × 10³ = B(mmol/mL) × V<sub>b</sub>(mL)</span> &nbsp; <span class="eq">f = B / 0.100</span></li>
<li><b>페놀프탈레인</b>: 산성형 무색(pH &lt; 8.0) → 염기성형 분홍(pH &gt; 9.6). 산을 강염기로 적정하므로 옅은 분홍이 지속되는 점을 종말점으로 한다.</li>
<li><b>총산도</b>: 식초 중 적정 가능한 모든 유기산을 초산으로 간주하여 환산한 농도(w/v%, 식초 100 mL 중 초산 g).<br>
<span class="eq">CH₃COOH + NaOH → CH₃COONa + H₂O</span><br>
<span class="eq">초산(g) = 0.1 × f × V<sub>b</sub> × 60.05 × 10⁻³</span> &nbsp; <span class="eq">총산도(w/v%) = 초산(g) / 식초(mL) × 100</span></li></ul>

<h2>3. 시약 및 기구</h2>
<p>0.1 M NaOH standard solution, KHP, phenolphthalein 지시약 용액, buret (50 mL) &amp; stand, buret holder, volumetric flask (100 mL), Erlenmeyer flask (100 mL), pipet (10, 20 mL), pipet aid, chemical balance, magnetic stirrer &amp; bar, 탈이온수</p>

<h2>4. 실험방법</h2>
<ol><li>KHP {A0:.3f} g을 정밀하게 달아 100 mL 용량플라스크에 넣고, 탈이온수를 약 반 정도 넣어 녹인 후 표선까지 채우고 섞었다. (110 °C 건조와 CO₂ 제거 증류수 사용은 생략하였다.)</li>
<li>뷰렛을 NaOH 표준액으로 헹구고 채운 뒤 기포를 제거하고 시작 눈금을 읽었다.</li>
<li>KHP 용액 20.00 mL를 피펫으로 취해 삼각플라스크에 넣고 페놀프탈레인 2방울을 가한 뒤, 교반하면서 옅은 분홍색이 지속될 때까지 NaOH로 적정하였다.</li>
<li>식초 10.00 mL를 피펫으로 취해 100 mL 용량플라스크에 넣고 표선까지 희석하였다.</li>
<li>희석한 식초 20.00 mL를 삼각플라스크에 넣고 물 20 mL와 지시약 2방울을 가한 뒤, 표정 때와 같은 분홍색에서 멈추도록 NaOH로 적정하였다.</li>
<li>표정과 식초 적정은 각각 1회 수행하였다.</li></ol>

<h2>5. 결과 (Table I–III 부착)</h2>
<ul><li><b>[과제] KHP 용액</b>: C = {A0:.3f} ÷ 204.221 ÷ 0.1000 = {C:.4f} M<br>
[H⁺] = √[(K₁K₂C + K₁K<sub>w</sub>)/(K₁ + C)] = √[(1.26×10⁻³ × 3.16×10⁻⁶ × {C:.4f}) / (1.26×10⁻³ + {C:.4f})] = 6.27 × 10⁻⁵ M → <b>pH = {PH:.2f}</b> (근사식 (pK₁ + pK₂)/2 = 4.2와 일치)</li>
<li><b>표정</b>: 적정한 KHP = {A0:.3f} × 20.00/100.0 = {A:.4f} g = {MMOL:.4f} mmol<br>
V<sub>b</sub> = 34.50 − 15.00 = {VB_STD:.2f} mL, B = {MMOL:.4f} / {VB_STD:.2f} = {B:.5f} mmol/mL → <b>f = {B:.5f} / 0.100 = {F:.3f}</b></li>
<li><b>총산도</b>: 초산 = 0.1 × {F:.3f} × {VB_VIN:.2f} × 60.05 × 10⁻³ = {ACG:.4f} g<br>
적정한 식초 원액 = 10.00 × 20.00/100.0 = {VIN:.3f} mL → <b>총산도 = {ACG:.4f} / {VIN:.3f} × 100 = {ACID:.2f} w/v%</b></li></ul>

<h2>6. 고찰 및 결론</h2>
<ol><li>직접 표정한 NaOH의 규정도계수는 {F:.3f}로, 제조사 표기값 1.000(0.999~1.001)보다 {(F - 1) * 100:.1f}% 컸다. 이 f를 사용한 식초의 총산도는 {ACID:.2f} w/v%였다. (f = 1.000을 쓰면 {ACID1:.2f} w/v%로, f 차이만큼 결과가 달라진다.)</li>
<li>f가 1.000보다 크게 나온 원인으로는 다음을 유추할 수 있다. ① KHP를 110 °C에서 건조하지 않아, 흡착된 수분만큼 실제 KHP 양이 칭량값보다 적었을 수 있다. 그러면 V<sub>b</sub>가 작아져 f가 과대평가된다. ② 피펫·용량플라스크의 표선 맞춤 오차와 칭량 오차. ③ 종말점을 늦게 또는 이르게 판단한 지시약 오차.</li>
<li>CO₂를 제거하지 않은 탈이온수를 사용하였다. 녹아 있는 CO₂(탄산)가 NaOH와 반응하면 NaOH 소비량이 늘어난다. 식초 희석수에서는 총산도가 과대평가되고, KHP 용해수에서는 f가 과소평가되는 방향의 오차가 된다.</li>
<li>표정과 식초 적정의 종말점 분홍색을 같게 맞추어 지시약 오차가 서로 상쇄되도록 하였다.</li>
<li>식초 적정은 시작·최종 눈금을 기록하지 못하고 소비량(20.92 mL)만 남겼다. 원래 읽은 값이 없어 검정곡선 보정을 할 수 없으므로, 다음 실험부터는 두 눈금을 모두 기록한다.</li>
<li>표정(유인물 2회)과 식초 적정(유인물 3회)을 각 1회만 수행하여 평균과 표준편차를 구하지 못했고 재현성을 확인할 수 없었다.</li>
<li>대책 및 개선 방안: KHP를 110 °C에서 1시간 건조하고 데시케이터에서 식혀 사용한다. 끓여서 CO₂를 제거한 물을 사용한다. 표정 2회 이상, 시료 적정 3회 이상 반복한다. 실험 1에서 구한 뷰렛 검정곡선으로 시작·최종 눈금을 보정한다.</li></ol>
</div>
</body></html>"""
open(os.path.join(D, "note.html"), "w", encoding="utf-8").write(html)
print(f"C={C:.5f} pH={PH:.3f} A={A:.4f} mmol={MMOL:.4f} B={B:.5f} f={F} acid_g={ACG:.4f} acidity={ACID} (f=1: {ACID1})")
