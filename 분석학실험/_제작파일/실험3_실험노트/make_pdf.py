# -*- coding: utf-8 -*-
"""실험3 실험노트: 오려 붙이는 Table I–III + 손으로 옮겨 적을 초안 → note.html (1조, 1회 측정)"""
import os

D = os.path.dirname(os.path.abspath(__file__))
FM, C0, VOL = 58.44, 0.1, 100.0
W_STD = 0.583
S1, E1, B1 = 19.87, 29.73, 0.03          # 표정: 시작, 최종, 공시험
W_SALT = 0.099
S2, E2, B2 = 32.60, 41.18, 0.03          # 시료: 시작, 최종, 공시험
M_AG = 0.2                               # AgNO₃ 규정 농도 (수업 중 0.1 → 0.2 M 정정)

TH = C0 * VOL / 1000 * FM
FP = round(W_STD / TH, 3)
MMOL = C0 * FP * 20.0
V1 = round(E1 - S1, 2)
F = round(MMOL / (M_AG * (V1 - B1)), 3)
V2 = round(E2 - S2, 2)
EQ = M_AG * FM
G = (V2 - B2) * F * EQ / 1000
PCT = round(G / W_SALT * 100, 1)
FP99 = round(W_STD * 0.99 / TH, 3)
F99 = round(C0 * FP99 * 20.0 / (M_AG * (V1 - B1)), 3)
PCT99 = round((V2 - B2) * F99 * EQ / 1000 / W_SALT * 100, 1)

FONTS = "".join(f'<link rel="stylesheet" href="file://{p}">' for p in (os.path.expanduser(f"~/.fonts/nskr/package/{w}.css") for w in (400, 700)) if os.path.exists(p))
TAG = '<div class="tag">분석학실험 노트 <b>1권</b> · 부착 p.____ · <span class="sig">간인(노트와 겹치게)</span></div>'


def tbl(rows):
    return '<table><tr><th>항목</th><th>값</th><th>계산 / 비고</th></tr>' + "".join(
        f"<tr><td class='l'>{a}</td><td><b>{b}</b></td><td class='l'>{c}</td></tr>" for a, b, c in rows) + "</table>"


T1 = tbl([("NaCl 표준품 칭량값", f"{W_STD:.3f} g", "순도 99% 시약, 100%로 가정, 건조 생략"),
          ("이론량", f"{TH:.4f} g", "0.1 mol/L × 0.1000 L × 58.44 g/mol"),
          ("규정도계수 f′", f"{FP:.3f}", f"{W_STD:.3f} ÷ {TH:.4f}"),
          ("NaCl 표준액 농도", f"{C0 * FP:.4f} M", "0.1 × f′, 100 mL 용량플라스크")])
T2 = tbl([("분취한 NaCl 표준액", "20.0 mL", "pipet, + 탈이온수 40 mL + 5% K₂CrO₄ 4방울"),
          ("NaCl 몰수", f"{MMOL:.4f} mmol", f"0.1 × {FP:.3f} × 20.0"),
          ("뷰렛 시작 → 최종 눈금", f"{S1:.2f} → {E1:.2f} mL", "AgNO₃ (규정 농도 0.2 M)"),
          ("AgNO₃ 소비량 V", f"{V1:.2f} mL", f"{E1:.2f} − {S1:.2f}"),
          ("공시험 b", f"{B1:.2f} mL", "탈이온수 약 70 mL + 지시약 4방울"),
          ("규정도계수 f", f"{F:.3f}", f"{MMOL:.4f} ÷ [0.2 × ({V1:.2f} − {B1:.2f})]")])
T3 = tbl([("시판 소금 칭량값", f"{W_SALT:.3f} g", "건조 생략, 탈이온수 50 mL에 녹임"),
          ("뷰렛 시작 → 최종 눈금", f"{S2:.2f} → {E2:.2f} mL", "5% K₂CrO₄ 4방울"),
          ("AgNO₃ 소비량 V", f"{V2:.2f} mL", f"{E2:.2f} − {S2:.2f}"),
          ("공시험 b", f"{B2:.2f} mL", "탈이온수 약 59 mL + 지시약 4방울"),
          ("대응량 E", f"{EQ:.3f} mg/mL", "0.2 M AgNO₃ 1 mL ≡ NaCl 0.2 × 58.44 mg"),
          ("NaCl 양", f"{G:.5f} g", f"({V2:.2f} − {B2:.2f}) × {F:.3f} × {EQ:.3f} × 10⁻³"),
          ("NaCl 함량", f"{PCT:.1f} %", f"{G:.5f} ÷ {W_SALT:.3f} × 100")])

html = f"""<!doctype html><html lang="ko"><head><meta charset="utf-8">{FONTS}<title>실험3 실험노트</title><style>
@page {{ size: A4; margin: 13mm 15mm; }}
body {{ font-family:'Noto Sans KR','Pretendard',sans-serif; color:#222; font-size:10.4pt; line-height:1.6; margin:0; }}
h1 {{ font-size:15pt; margin:0 0 2px; }} .sub {{ color:#666; font-size:9pt; margin-bottom:10px; }}
.cut {{ border:1.4px dashed #888; padding:8px 12px 6px; margin:0 auto 12px; width:160mm; position:relative; break-inside:avoid; }}
.cut::before {{ content:'✂'; position:absolute; top:-11px; left:-4px; background:#fff; color:#888; font-size:13px; }}
.cut h3 {{ font-size:10.5pt; margin:0 0 5px; }}
table {{ border-collapse:collapse; width:100%; font-size:9.3pt; }}
th, td {{ border:1px solid #666; padding:3px 6px; text-align:center; }} th {{ background:#eee; }} td.l {{ text-align:left; }}
.tag {{ font-size:8.4pt; color:#555; margin-top:4px; text-align:right; }} .sig {{ border-bottom:1px solid #999; padding:0 18px; }}
.brk {{ break-before:page; }}
h2 {{ font-size:12pt; border-left:4px solid #4651c8; padding-left:8px; margin:12px 0 5px; }}
.draft p, .draft li {{ margin:2px 0; }} ol, ul {{ margin:2px 0 6px; padding-left:20px; }}
.hint {{ background:#fff4cc; border:1px solid #efd27a; border-radius:6px; padding:6px 10px; font-size:9.3pt; margin:8px 0; }}
.eq {{ background:#f4f0fb; border-radius:6px; padding:3px 10px; margin:3px 0; display:inline-block; }}
</style></head><body>

<h1>실험 3. NaCl의 정량 (침전적정법, Mohr법) — 실험노트 부착용 (1조)</h1>
<div class="sub">점선대로 오려 <b>4면 모두</b> 붙이고, <b>노트 번호(1권)와 부착 페이지 번호</b>를 적고, 부착물과 노트 공란에 <b>겹치게</b> 서명(간인)</div>

<div class="cut"><h3>Table I. 0.1 M NaCl 표준액의 조제</h3>{T1}{TAG}</div>
<div class="cut"><h3>Table II. AgNO₃ 표준액의 표정 (1회)</h3>{T2}{TAG}</div>
<div class="cut"><h3>Table III. 시판 소금 중 NaCl 함량 (1회, f = {F:.3f} 사용)</h3>{T3}{TAG}</div>

<div class="draft brk">
<h1>실험노트 초안 — 볼펜으로 옮겨 적기</h1>
<div class="hint">머리말/꼬리말: <b>1권 · p.__(실험 2에서 이어서) · 서명</b> (매 페이지) · 실험일자 2026. __. __.(목, 실험한 날) · 1조. 큰 빈 공간만 빗금 한 줄. <b>원리는 최소 반 페이지.</b></div>

<h2>제목</h2><p>실험 3. NaCl의 정량 (침전적정법, Mohr법)</p>

<h2>1. 목적</h2>
<p>NaCl 표준액으로 AgNO₃ 용액을 표정하여 규정도계수를 구하고, Mohr법으로 시판 소금 중 NaCl의 함량(%)을 정량한다.</p>

<h2>2. 원리</h2>
<ul><li><b>은적정(argentometry)</b>: pH 6.5~10.5 사이에서 Cl⁻을 AgNO₃ 표준액으로 적정하면 난용성 AgCl(흰색)이 침전된다. NaCl과 AgNO₃는 1 : 1로 반응하며, 실제로 정량되는 것은 Cl⁻이므로 물에 녹아 Cl⁻을 내는 모든 물질(예: KCl)이 함께 정량되고, 이를 NaCl로 환산한다.<br>
<span class="eq">NaCl + AgNO₃ → AgCl↓ + NaNO₃</span> &nbsp; <span class="eq">AgCl(s) ⇌ Ag⁺ + Cl⁻, K<sub>sp</sub> = 1.8 × 10⁻¹⁰</span></li>
<li><b>Mohr법의 종말점</b>: 지시약 K₂CrO₄는 Cl⁻이 모두 AgCl로 침전된 후 과량의 Ag⁺와 반응하여 적갈색의 Ag₂CrO₄ 침전을 만든다. 이 적갈색 침전이 약 15초간 흔들어도 탈색되지 않을 때를 종말점으로 한다.<br>
<span class="eq">K₂CrO₄ + 2AgNO₃ → Ag₂CrO₄↓ + 2KNO₃</span> &nbsp; <span class="eq">Ag₂CrO₄(s) ⇌ 2Ag⁺ + CrO₄²⁻, K<sub>sp</sub> = 1.2 × 10⁻¹²</span></li>
<li>몰 용해도는 AgCl(√K<sub>sp</sub> ≈ 1.3 × 10⁻⁵ M)이 Ag₂CrO₄((K<sub>sp</sub>/4)<sup>1/3</sup> ≈ 6.7 × 10⁻⁵ M)보다 작으므로 AgCl이 먼저 침전되고, Cl⁻이 거의 없어진 뒤에 Ag₂CrO₄가 생긴다. 산성에서는 CrO₄²⁻가 HCrO₄⁻/Cr₂O₇²⁻로 바뀌어 종말점이 늦어지고, 강알칼리에서는 Ag⁺가 산화은으로 침전되므로 pH 범위를 지킨다.</li>
<li><b>공시험</b>: 종말점에서와 같은 부피의 물에 지시약만 넣고 적정해, 물에 있는 Cl⁻과 지시약 색이 나타나는 데 필요한 Ag⁺ 양(b)을 구해 빼 준다.</li>
<li><b>규정도계수</b>: NaCl 표준액은 f′ = 실제 칭량량 / 이론량(0.5844 g). AgNO₃는 <span class="eq">0.1 × f′ × 20.0 = M × f × (V − b)</span>로 f를 구한다.</li>
<li><b>함량 계산</b>: 0.1 M AgNO₃ 1 mL ≡ NaCl 5.844 mg (오늘 사용한 0.2 M은 11.69 mg). <span class="eq">NaCl(g) = (V − b) × f × E × 10⁻³</span> &nbsp; <span class="eq">함량(%) = NaCl(g) / 시료(g) × 100</span></li></ul>

<h2>3. 시약 및 기구</h2>
<p>분석저울, magnetic stirrer, Erlenmeyer flask (200 mL), volumetric flask (100 mL), buret (50 mL), pipet, mess cylinder (100 mL), stand, clamp, 세척병, NaCl 표준품(99%), 시판 소금, 제공된 AgNO₃ 용액(규정 농도 0.2 M, 갈색 병), 제공된 5% K₂CrO₄ 지시약, 탈이온수</p>

<h2>4. 실험방법</h2>
<ol><li>NaCl 표준품(순도 99%, 100%로 가정)을 건조하지 않고 {W_STD:.3f} g 칭량하여 100 mL 용량플라스크에 넣고 탈이온수로 녹인 뒤 표선까지 채우고 섞었다. 이론량 0.5844 g과 비교하여 f′를 구하였다.</li>
<li>5% K₂CrO₄ 지시약과 AgNO₃ 용액은 제공된 것을 사용하였다. AgNO₃의 규정 농도는 실험 중 0.2 M으로 정정되었다.</li>
<li>뷰렛을 AgNO₃로 헹군 뒤 기포 없이 채우고 시작 눈금을 읽었다.</li>
<li>NaCl 표준액 20.0 mL를 피펫으로 취해 200 mL 삼각플라스크에 넣고, 탈이온수 40 mL(메스실린더)와 지시약 4방울을 가한 뒤 교반하면서 AgNO₃로 적정하였다 ({S1:.2f} → {E1:.2f} mL). 옅은 적갈색이 약 15초간 사라지지 않는 점을 종말점으로 하였다.</li>
<li>공시험으로 탈이온수 약 70 mL에 지시약 4방울을 넣고 같은 색이 될 때까지 적정하였다 ({B1:.2f} mL).</li>
<li>시판 소금(건조 생략) {W_SALT:.3f} g을 200 mL 삼각플라스크에 넣고 탈이온수 50 mL에 녹인 뒤 지시약 4방울을 가하고 같은 방법으로 적정하였다 ({S2:.2f} → {E2:.2f} mL).</li>
<li>공시험으로 탈이온수 약 59 mL에 지시약 4방울을 넣고 적정하였다 ({B2:.2f} mL).</li>
<li>각 적정은 1회씩 수행하였다.</li></ol>

<h2>5. 결과 (Table I–III 부착)</h2>
<ul><li><b>f′</b>: 이론량 = 0.1 × 0.1000 × 58.44 = {TH:.4f} g → f′ = {W_STD:.3f} / {TH:.4f} = <b>{FP:.3f}</b></li>
<li><b>f</b>: NaCl = 0.1 × {FP:.3f} × 20.0 = {MMOL:.4f} mmol, V = {E1:.2f} − {S1:.2f} = {V1:.2f} mL<br>
f = {MMOL:.4f} / [0.2 × ({V1:.2f} − {B1:.2f})] = <b>{F:.3f}</b></li>
<li><b>NaCl 함량</b>: V = {E2:.2f} − {S2:.2f} = {V2:.2f} mL, V − b = {V2 - B2:.2f} mL<br>
NaCl = {V2 - B2:.2f} × {F:.3f} × {EQ:.3f} × 10⁻³ = {G:.5f} g → 함량 = {G:.5f} / {W_SALT:.3f} × 100 = <b>{PCT:.1f} %</b></li></ul>

<h2>6. 고찰 및 결론</h2>
<ol><li>AgNO₃의 규정도계수는 {F:.3f}이었고, 이를 이용한 시판 소금 중 NaCl 함량은 {PCT:.1f}%로 100%를 넘었다. 시판 소금은 수분과 다른 성분을 포함하므로 100%보다 낮아야 정상이며, 이 결과는 오차를 포함한다.</li>
<li>100%를 넘은 원인으로 다음을 유추할 수 있다.
 ① NaCl 표준품(순도 99%)을 100%로 가정하였다. 실제 NaCl이 칭량값보다 약 1% 적으므로 표정 V가 작아져 f가 과대평가되고 함량도 과대평가된다. 순도 99%를 반영하면 f′ = {FP99:.3f}, f = {F99:.3f}, 함량 = {PCT99:.1f}%이다.
 ② 표준품을 건조하지 않아 수분만큼 실제 NaCl이 적어 같은 방향의 오차가 생긴다.
 ③ 시료를 소수 셋째 자리({W_SALT:.3f} g)까지만 칭량하여 칭량 불확도(±0.0005 g)가 함량의 약 ±0.5%에 해당한다.
 ④ 시판 소금에 KCl 등 다른 염화물이 있으면 모두 NaCl로 환산되어 함량이 높게 나온다.
 ⑤ 시료 적정에서 흰 AgCl 현탁액 속의 적갈색을 늦게 판단하면 V가 커져 함량이 과대평가된다 (표정에서 늦으면 반대로 f가 작아진다).</li>
<li>AgNO₃ 농도가 0.1 M에서 0.2 M으로 정정되어 적정량이 약 10 mL로 작아졌다. 같은 눈금 읽기 오차(±0.02 mL)가 차지하는 비율이 커지므로 정확도가 떨어진다.</li>
<li>공시험은 표정 {B1:.2f} mL, 시료 {B2:.2f} mL로 한두 방울에 변색하였다. 사용한 탈이온수에 Cl⁻이 거의 없음을 확인하였고, 이 값을 빼서 지시약 오차를 보정하였다.</li>
<li>각 적정을 1회만 수행하여 평균과 표준편차를 구하지 못했고 재현성을 확인할 수 없었다.</li>
<li>대책 및 개선 방안: 표준품과 시료를 100~120 °C에서 2시간 건조하고 데시케이터에서 식혀 사용한다. 순도가 보증된 일차표준물질을 쓰거나 순도를 보정한다. 시료를 소수 넷째 자리까지 칭량하고, 적정량이 20 mL 이상이 되도록 시료량을 늘린다. 표정과 시료 적정의 종말점 색을 같게 맞추고 3회 반복한다.</li></ol>
</div>
</body></html>"""
open(os.path.join(D, "note.html"), "w", encoding="utf-8").write(html)
print(f"TH={TH:.4f} f'={FP} mmol={MMOL:.4f} V1={V1} f={F} V2={V2} G={G:.5f} pct={PCT} | 99%: f'={FP99} f={F99} pct={PCT99}")
