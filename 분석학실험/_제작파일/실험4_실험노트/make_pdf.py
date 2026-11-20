# -*- coding: utf-8 -*-
"""실험4 실험노트: 오려 붙이는 Table I–IV + 손으로 옮겨 적을 초안 → note.html (1조, 수돗물, 1회 측정)
교수님 코멘트(실험 3 채점): 표정(표준액)과 적정을 구분해서 기재"""
import os

D = os.path.dirname(os.path.abspath(__file__))
FM, C0, VOL = 372.25, 0.01, 250.0
W_EDTA = 0.931
SAMPLE = 100.0
S_T, E_T = 25.35, 32.11      # 총경도: 시작, 최종
S_C, E_C = 32.11, 36.25      # Ca 경도: 시작, 최종

TH = C0 * VOL / 1000 * FM
F = round(W_EDTA / TH, 3)
A = round(E_T - S_T, 2)
B = round(E_C - S_C, 2)
TOT = round((A * F - 1) * 1000 / SAMPLE, 1)
CA = round(B * F * 1000 / SAMPLE, 1)
MG = round(TOT - CA, 1)
F995 = round(W_EDTA * 0.995 / TH, 3)
TOT995 = round((A * F995 - 1) * 1000 / SAMPLE, 1)
CA995 = round(B * F995 * 1000 / SAMPLE, 1)
MGMM = MG / 100.0869                       # Mg mmol/L
MGOH = MGMM * SAMPLE / 1000 * 58.32         # Mg(OH)₂ mg in 100 mL
KIND = "연수(단물)" if TOT <= 75 else "비교적 약한 경수" if TOT <= 150 else "경수" if TOT <= 300 else "아주 강한 경수"

FONTS = "".join(f'<link rel="stylesheet" href="file://{p}">' for p in (os.path.expanduser(f"~/.fonts/nskr/package/{w}.css") for w in (400, 700)) if os.path.exists(p))
TAG = '<div class="tag">분석학실험 노트 <b>1권</b> · 부착 p.____ · <span class="sig">간인(노트와 겹치게)</span></div>'


def tbl(rows):
    return '<table><tr><th>항목</th><th>값</th><th>계산 / 비고</th></tr>' + "".join(
        f"<tr><td class='l'>{a}</td><td><b>{b}</b></td><td class='l'>{c}</td></tr>" for a, b, c in rows) + "</table>"


T1 = tbl([("EDTA 칭량값", f"{W_EDTA:.3f} g", "disodium EDTA dihydrate (99.5%), 조에서 건조 안 함"),
          ("이론량", f"{TH:.4f} g", "0.01 mol/L × 0.2500 L × 372.25 g/mol"),
          ("규정도계수 f", f"{F:.3f}", f"{W_EDTA:.3f} ÷ {TH:.4f} (1차 표준물질 → 표정 생략)"),
          ("EDTA 표준액 농도", f"{C0 * F:.5f} M", "0.01 × f, 250 mL 용량플라스크")])
T2 = tbl([("시료", f"수돗물 {SAMPLE:.0f} mL", "메스실린더, 200 mL 삼각플라스크"),
          ("가한 시약", "KCN · MgCl₂ · 완충액 · EBT", "10% KCN 5방울, 0.01 M MgCl₂ 1.0 mL, pH 10 완충액 2 mL, EBT 3방울"),
          ("뷰렛 시작 → 최종 눈금", f"{S_T:.2f} → {E_T:.2f} mL", "적색 → 전부 청색"),
          ("EDTA 소비량 a", f"{A:.2f} mL", f"{E_T:.2f} − {S_T:.2f}"),
          ("총경도", f"{TOT:.1f} ppm", f"({A:.2f} × {F:.3f} − 1) × 1000 ÷ {SAMPLE:.0f}")])
T3 = tbl([("시료", f"수돗물 {SAMPLE:.0f} mL", "메스실린더, 200 mL 삼각플라스크"),
          ("가한 시약", "NaOH · KCN · NH₂OH·HCl · HNB", "20% NaOH 1 mL(pH ≈ 12), 10% KCN 5방울, 10% hydroxylamine HCl 5방울, 5분 방치, HNB 소량"),
          ("Mg(OH)₂ 침전", "눈에 띄지 않음", "육안 관찰"),
          ("뷰렛 시작 → 최종 눈금", f"{S_C:.2f} → {E_C:.2f} mL", "적색 → 전부 청색"),
          ("EDTA 소비량 b", f"{B:.2f} mL", f"{E_C:.2f} − {S_C:.2f}"),
          ("Ca 경도", f"{CA:.1f} ppm", f"{B:.2f} × {F:.3f} × 1000 ÷ {SAMPLE:.0f}")])
T4 = tbl([("총경도", f"{TOT:.1f} ppm CaCO₃", "Table II"),
          ("Ca 경도", f"{CA:.1f} ppm CaCO₃", "Table III"),
          ("Mg 경도", f"{MG:.1f} ppm CaCO₃", f"{TOT:.1f} − {CA:.1f}"),
          ("판정", KIND, "0–75 ppm 연수 · 음용수 기준 300 ppm 이하 만족")])

html = f"""<!doctype html><html lang="ko"><head><meta charset="utf-8">{FONTS}<title>실험4 실험노트</title><style>
@page {{ size: A4; margin: 13mm 15mm; }}
body {{ font-family:'Noto Sans KR','Pretendard',sans-serif; color:#222; font-size:10.4pt; line-height:1.6; margin:0; }}
h1 {{ font-size:15pt; margin:0 0 2px; }} .sub {{ color:#666; font-size:9pt; margin-bottom:9px; }}
.cut {{ border:1.4px dashed #888; padding:7px 12px 5px; margin:0 auto 10px; width:160mm; position:relative; break-inside:avoid; }}
.cut::before {{ content:'✂'; position:absolute; top:-11px; left:-4px; background:#fff; color:#888; font-size:13px; }}
.cut h3 {{ font-size:10.3pt; margin:0 0 4px; }}
table {{ border-collapse:collapse; width:100%; font-size:9.1pt; }}
th, td {{ border:1px solid #666; padding:2px 6px; text-align:center; }} th {{ background:#eee; }} td.l {{ text-align:left; }}
.tag {{ font-size:8.2pt; color:#555; margin-top:3px; text-align:right; }} .sig {{ border-bottom:1px solid #999; padding:0 18px; }}
.brk {{ break-before:page; }}
h2 {{ font-size:12pt; border-left:4px solid #4651c8; padding-left:8px; margin:12px 0 5px; }}
h3.s {{ font-size:10.6pt; margin:8px 0 3px; color:#2f3a8f; }}
.draft p, .draft li {{ margin:2px 0; }} ol, ul {{ margin:2px 0 6px; padding-left:20px; }}
.hint {{ background:#fff4cc; border:1px solid #efd27a; border-radius:6px; padding:6px 10px; font-size:9.3pt; margin:8px 0; }}
.eq {{ background:#f4f0fb; border-radius:6px; padding:3px 10px; margin:3px 0; display:inline-block; }}
</style></head><body>

<h1>실험 4. EDTA를 이용한 물의 세기(경도) 측정 — 실험노트 부착용 (1조)</h1>
<div class="sub">점선대로 오려 <b>4면 모두</b> 붙이고, <b>노트 번호(1권)와 부착 페이지 번호</b>를 적고, 부착물과 노트 공란에 <b>겹치게</b> 서명(간인)</div>

<div class="cut"><h3>Table I. [표준액] 0.01 M EDTA 표준액 조제 — 표정 생략, f 계산</h3>{T1}{TAG}</div>
<div class="cut"><h3>Table II. [적정 1] 총경도 (pH 10, EBT)</h3>{T2}{TAG}</div>
<div class="cut"><h3>Table III. [적정 2] Ca 경도 (pH 12, HNB)</h3>{T3}{TAG}</div>
<div class="cut"><h3>Table IV. 수돗물의 경도 (ppm as CaCO₃)</h3>{T4}{TAG}</div>

<div class="draft brk">
<h1>실험노트 초안 — 볼펜으로 옮겨 적기</h1>
<div class="hint">머리말/꼬리말: <b>1권 · p.__(실험 3에서 이어서) · 서명</b> (매 페이지) · 실험일자 2026. 11. 19.(목) · 1조. 큰 빈 공간만 빗금 한 줄. <b>원리 최소 반 페이지, 표정(표준액)과 적정 구분.</b></div>

<h2>제목</h2><p>실험 4. EDTA를 이용한 물의 세기(경도) 측정 (킬레이트 적정법)</p>

<h2>1. 목적</h2>
<p>1차 표준물질인 EDTA로 표준액을 조제하고, 킬레이트 적정법으로 수돗물의 총경도와 Ca 경도를 측정하여 Mg 경도를 구한다.</p>

<h2>2. 원리</h2>
<ul><li><b>물의 경도</b>: 천연수에 가장 많은 양이온인 Ca²⁺와 Mg²⁺의 양을 모두 CaCO₃의 양으로 환산하여 ppm으로 나타낸 것이다. 1 ppm = 1 g/10⁶ mL = 1 μg/mL이다. 0–75 ppm 연수, 75–150 비교적 약한 경수, 150–300 경수, 300 초과 아주 강한 경수이며, 우리나라 음용수 기준은 총경도 300 ppm 이하이다.</li>
<li><b>킬레이트 적정</b>: EDTA(Y⁴⁻)는 금속 이온과 1 : 1로 매우 안정한 킬레이트를 만든다.<br>
<span class="eq">Ca²⁺ + Y⁴⁻ → CaY²⁻ (log K<sub>f</sub> = 10.65)</span> &nbsp; <span class="eq">Mg²⁺ + Y⁴⁻ → MgY²⁻ (log K<sub>f</sub> = 8.79)</span><br>
EDTA는 선택성이 없어 Fe·Cu·Mn 등과도 반응하므로, 가리움제(KCN)로 다른 금속을 먼저 가린 뒤 Ca·Mg만 적정한다.</li>
<li><b>지시약</b>: 유리형(HIn²⁻)은 청색, 금속 결합형(MIn⁻)은 적색이다. 시료에 지시약을 넣으면 적색이 되고, EDTA가 자유 Ca²⁺·Mg²⁺를 모두 착물로 만든 뒤 지시약의 금속을 빼앗으면 청색이 된다.<br>
<span class="eq">M²⁺ + HIn²⁻(blue) → MIn⁻(red) + H⁺</span> &nbsp; <span class="eq">MIn⁻(red) + Y⁴⁻ + H⁺ → MY²⁻ + HIn²⁻(blue)</span></li>
<li><b>총경도</b>: pH 10(암모니아 완충액)에서 EBT로 Ca²⁺ + Mg²⁺를 적정한다. 종말점을 선명하게 하려고 0.01 M MgCl₂ 1.0 mL를 넣고, 같은 농도이므로 계산에서 1 mL를 뺀다.</li>
<li><b>Ca 경도</b>: 20% NaOH로 pH ≈ 12로 만들면 Mg가 Mg(OH)₂로 침전되므로, HNB로 Ca²⁺만 적정한다. Mg 경도는 총경도 − Ca 경도로 구한다.</li>
<li><b>표준액</b>: disodium EDTA dihydrate(99.5%)는 1차 표준물질이므로 표정하지 않고 f = 실제 칭량량 / 이론량으로 구한다. 0.01 M EDTA 1 mL ≡ CaCO₃ 1.000 mg.<br>
<span class="eq">총경도 = (a × f − 1) × 1000 / 시료 mL</span> &nbsp; <span class="eq">Ca 경도 = b × f × 1000 / 시료 mL</span></li></ul>

<h2>3. 시약 및 기구</h2>
<p>분석저울, magnetic stirrer, Erlenmeyer flask (200 mL), mess cylinder (100 mL), volumetric flask (250 mL), buret (50 mL), micropipette (1 mL), spatula, stand, clamp, 세척병, disodium EDTA dihydrate (FM 372.25), 수돗물(시료), 탈이온수, 제공된 시약: 암모니아 완충액(pH 10), EBT 지시약 용액, HNB 희석 분말, 10% KCN, 0.01 M MgCl₂, 20% NaOH, 10% hydroxylamine HCl</p>

<h2>4. 실험방법</h2>
<h3 class="s">[표준액] 0.01 M EDTA 표준액 조제 (표정 생략)</h3>
<ol><li>disodium EDTA dihydrate {W_EDTA:.3f} g을 칭량하여(조에서 건조하지 않음) 250 mL 용량플라스크에 넣고, 탈이온수로 완전히 녹인 뒤 표선까지 채우고 섞었다.</li>
<li>이론량 {TH:.4f} g과 비교하여 규정도계수 f를 구하였다.</li></ol>
<h3 class="s">[적정 1] 총경도</h3>
<ol><li>수돗물 100 mL를 메스실린더로 취해 200 mL 삼각플라스크에 넣었다.</li>
<li>10% KCN 5방울, 0.01 M MgCl₂ 1.0 mL(마이크로피펫), 암모니아 완충액(pH 10) 2 mL, EBT 지시약 3방울을 넣었다 (적색).</li>
<li>교반하면서 EDTA 표준액으로 적색이 전부 청색이 될 때까지 적정하였다 ({S_T:.2f} → {E_T:.2f} mL).</li></ol>
<h3 class="s">[적정 2] Ca 경도</h3>
<ol><li>수돗물 100 mL를 메스실린더로 취해 200 mL 삼각플라스크에 넣었다.</li>
<li>20% NaOH 1 mL(마이크로피펫), 10% KCN 5방울, 10% hydroxylamine HCl 5방울을 넣고 저은 뒤 5분간 방치하였다. Mg(OH)₂ 침전은 눈에 띄지 않았다.</li>
<li>HNB 희석 분말을 스패출러로 소량 넣고(적색), EDTA 표준액으로 전부 청색이 될 때까지 적정하였다 ({S_C:.2f} → {E_C:.2f} mL).</li></ol>
<p>각 적정은 1회씩 수행하였고, 공시험은 하지 않았다.</p>

<h2>5. 결과 (Table I–IV 부착)</h2>
<h3 class="s">[표준액] EDTA의 f</h3>
<p>이론량 = 0.01 × 0.2500 × 372.25 = {TH:.4f} g → <b>f = {W_EDTA:.3f} / {TH:.4f} = {F:.3f}</b></p>
<h3 class="s">[적정 1] 총경도</h3>
<p>a = {E_T:.2f} − {S_T:.2f} = {A:.2f} mL → 총경도 = ({A:.2f} × {F:.3f} − 1) × 1000 / {SAMPLE:.0f} = <b>{TOT:.1f} ppm</b></p>
<h3 class="s">[적정 2] Ca 경도</h3>
<p>b = {E_C:.2f} − {S_C:.2f} = {B:.2f} mL → Ca 경도 = {B:.2f} × {F:.3f} × 1000 / {SAMPLE:.0f} = <b>{CA:.1f} ppm</b></p>
<h3 class="s">Mg 경도</h3>
<p>Mg 경도 = {TOT:.1f} − {CA:.1f} = <b>{MG:.1f} ppm</b> (as CaCO₃)</p>

<h2>6. 고찰 및 결론</h2>
<ol><li>수돗물의 총경도는 {TOT:.1f} ppm으로 {KIND}(0–75 ppm)에 해당하며, 음용수 기준(300 ppm 이하)을 충분히 만족하였다. 총경도 중 Ca 경도가 {CA:.1f} ppm({CA / TOT * 100:.0f}%), Mg 경도가 {MG:.1f} ppm({MG / TOT * 100:.0f}%)으로 Ca가 대부분을 차지하였다.</li>
<li>Ca 경도 측정에서 Mg(OH)₂ 침전이 눈에 띄지 않았다. Mg 경도 {MG:.1f} ppm은 Mg 약 {MGMM:.2f} mmol/L이고, 시료 100 mL에서 생길 수 있는 Mg(OH)₂는 약 {MGOH:.1f} mg에 불과해 육안으로 보기 어려웠던 것으로 판단된다. 따라서 침전이 보이지 않은 것은 Mg가 없어서라기보다 양이 적었기 때문이다.</li>
<li>경도의 참값은 알 수 없으므로 오차를 단정할 수 없으나, 다음 요인이 결과에 영향을 줄 수 있다. ① 시료 100 mL를 메스실린더로 취해 ±1 mL 정도의 부피 오차가 있으며, 이는 경도에 약 ±1%로 반영된다. ② 낮은 온도에서 종말점 변색이 느려, 청색을 기다리는 동안 EDTA가 과량 들어가면 a·b가 커져 경도가 과대평가된다. ③ EDTA 순도 99.5%를 100%로 가정하였다. 순도를 반영하면 f = {F995:.3f}, 총경도 {TOT995:.1f} ppm, Ca 경도 {CA995:.1f} ppm으로 차이는 작다. EDTA를 조에서 건조하지 않아 수분이 있었다면 f가 과대평가된다. ④ Mg 경도는 두 적정값의 차이로 구하므로 두 적정의 오차가 모두 반영된다. pH 12에서 Ca가 Mg(OH)₂와 함께 일부 공침되면 Ca 경도가 작아지고 Mg 경도가 커진다. ⑤ MgCl₂ 1.0 mL의 부피 오차는 총경도에 직접 반영된다(0.1 mL당 1 ppm).</li>
<li>공시험을 하지 않아 탈이온수·시약에 의한 EDTA 소비와 지시약 오차를 보정하지 못하였다. 시료가 경도가 낮아 a가 6.76 mL로 작았으므로, 공시험값이 작더라도 상대적인 영향은 커질 수 있다.</li>
<li>각 적정을 1회만 수행하여 재현성을 확인하지 못하였다.</li>
<li>대책 및 개선 방안: EDTA를 80 °C에서 1시간 건조 후 데시케이터에서 식혀 사용한다. 시료를 100 mL transfer pipet으로 취한다. 종말점 근처에서는 한 방울씩 넣고 충분히 기다리며 적색 대조 플라스크와 비교한다. 탈이온수로 공시험을 한다. 경도가 낮은 물은 시료량을 늘려 적정량을 크게 한다. 3회 반복한다.</li></ol>
</div>
</body></html>"""
open(os.path.join(D, "note.html"), "w", encoding="utf-8").write(html)
print(f"TH={TH:.4f} f={F} a={A} b={B} total={TOT} Ca={CA} Mg={MG} {KIND} | 99.5%: f={F995} tot={TOT995} Ca={CA995} | Mg mmol/L={MGMM:.3f} MgOH2 mg={MGOH:.2f}")
