# -*- coding: utf-8 -*-
"""실험5 실험노트: 오려 붙이는 Table I–V + 손으로 옮겨 적을 초안 → note.html (1조, 각 1회)
반영한 피드백: 표정과 적정 구분(실험 3), 결론 한 줄(실험 4), 팩터 셋째 자리"""
import os

D = os.path.dirname(os.path.abspath(__file__))
F_I2 = 1.003                               # I₂ 표준액 라벨
V_I2 = 10.00
S_S, E_S = 25.55, 35.00                    # Na₂S₂O₃ 표정
V_POV = 10.00
S_P, E_P = 35.00, 42.42                    # 포비돈요오드액
W_AA = 0.1997
S_A1, E_A1, S_A2, E_A2 = 29.75, 50.00, 39.10, 41.18   # 아스코르브산 (중간 재충전)
EQ_I2, EQ_AA = 12.691, 8.806
POV_LO, POV_HI, AA_LO = 85.0, 120.0, 99.0  # 참고 기준 — 대한약전 원문 확인

VS = round(E_S - S_S, 2)
FP = round(F_I2 * V_I2 / VS, 3)
VP = round(E_P - S_P, 2)
LABEL = V_POV * 10.0
I_MG = VP * FP * EQ_I2
POV = round(I_MG / LABEL * 100, 1)
VA1, VA2 = round(E_A1 - S_A1, 2), round(E_A2 - S_A2, 2)
VA = round(VA1 + VA2, 2)
AA_MG = VA * F_I2 * EQ_AA
AA = round(AA_MG / (W_AA * 1000) * 100, 1)
EXP_A = W_AA * 1000 / EQ_AA / F_I2
POV_OK = POV_LO <= POV <= POV_HI
AA_OK = AA >= AA_LO

FONTS = "".join(f'<link rel="stylesheet" href="file://{p}">' for p in (os.path.expanduser(f"~/.fonts/nskr/package/{w}.css") for w in (400, 700)) if os.path.exists(p))
TAG = '<div class="tag">분석학실험 노트 <b>1권</b> · 부착 p.____ · <span class="sig">간인(노트와 겹치게)</span></div>'


def tbl(rows):
    return '<table><tr><th>항목</th><th>값</th><th>계산 / 비고</th></tr>' + "".join(
        f"<tr><td class='l'>{a}</td><td><b>{b}</b></td><td class='l'>{c}</td></tr>" for a, b, c in rows) + "</table>"


T1 = tbl([("0.05 M I₂ 표준액 (= 0.1 N)", f"f = {F_I2:.3f}", "구매한 표준액, 병 라벨의 f 사용 (표정하지 않음)")])
T2 = tbl([("분취한 I₂ 표준액", f"{V_I2:.2f} mL", "pipet, 100 mL 삼각플라스크, 탈이온수 40 mL"),
          ("뷰렛 시작 → 최종 눈금", f"{S_S:.2f} → {E_S:.2f} mL", "미황색에서 전분 1 mL → 청색 소실"),
          ("Na₂S₂O₃ 소비량", f"{VS:.2f} mL", f"{E_S:.2f} − {S_S:.2f}"),
          ("규정도계수 f′", f"{FP:.3f}", f"{F_I2:.3f} × {V_I2:.2f} ÷ {VS:.2f}")])
T3 = tbl([("분취량", f"{V_POV:.2f} mL", "요오드로서 100 mg 상당, transfer pipet, 전체 약 50 mL"),
          ("뷰렛 시작 → 최종 눈금", f"{S_P:.2f} → {E_P:.2f} mL", "미황색에서 전분 1 mL → 청색 소실"),
          ("Na₂S₂O₃ 소비량", f"{VP:.2f} mL", f"{E_P:.2f} − {S_P:.2f}"),
          ("요오드 양", f"{I_MG:.2f} mg", f"{VP:.2f} × {FP:.3f} × {EQ_I2:.3f}"),
          ("표시량 대비", f"{POV:.1f} %", f"{I_MG:.2f} ÷ {LABEL:.0f} × 100")])
T4 = tbl([("아스코르브산 칭량값", f"{W_AA:.4f} g", "조에서 건조 안 함, 메타인산용액 50 mL, 전분 1 mL"),
          ("1차 눈금", f"{S_A1:.2f} → {E_A1:.2f} mL", f"{VA1:.2f} mL — 적정액 부족, 뷰렛 재충전"),
          ("2차 눈금", f"{S_A2:.2f} → {E_A2:.2f} mL", f"{VA2:.2f} mL — 지속적인 청색"),
          ("I₂ 소비량 합계", f"{VA:.2f} mL", f"{VA1:.2f} + {VA2:.2f}"),
          ("아스코르브산 양", f"{AA_MG:.2f} mg", f"{VA:.2f} × {F_I2:.3f} × {EQ_AA:.3f}"),
          ("함량", f"{AA:.1f} %", f"{AA_MG:.2f} ÷ {W_AA * 1000:.1f} × 100")])
T5 = tbl([("포비돈요오드액 (완제)", f"{POV:.1f} %", f"기준 {POV_LO:.1f}~{POV_HI:.1f}% → <b>{'만족' if POV_OK else '불만족'}</b>"),
          ("아스코르브산 (원료)", f"{AA:.1f} %", f"기준 {AA_LO:.1f}% 이상 → <b>{'만족' if AA_OK else '불만족'}</b>")])

html = f"""<!doctype html><html lang="ko"><head><meta charset="utf-8">{FONTS}<title>실험5 실험노트</title><style>
@page {{ size: A4; margin: 12mm 15mm; }}
body {{ font-family:'Noto Sans KR','Pretendard',sans-serif; color:#222; font-size:10.3pt; line-height:1.58; margin:0; }}
h1 {{ font-size:14.5pt; margin:0 0 2px; }} .sub {{ color:#666; font-size:8.8pt; margin-bottom:8px; }}
.cut {{ border:1.4px dashed #888; padding:6px 11px 4px; margin:0 auto 8px; width:160mm; position:relative; break-inside:avoid; }}
.cut::before {{ content:'✂'; position:absolute; top:-11px; left:-4px; background:#fff; color:#888; font-size:13px; }}
.cut h3 {{ font-size:10.1pt; margin:0 0 3px; }}
table {{ border-collapse:collapse; width:100%; font-size:8.9pt; }}
th, td {{ border:1px solid #666; padding:2px 6px; text-align:center; }} th {{ background:#eee; }} td.l {{ text-align:left; }}
.tag {{ font-size:8pt; color:#555; margin-top:2px; text-align:right; }} .sig {{ border-bottom:1px solid #999; padding:0 18px; }}
.brk {{ break-before:page; }}
h2 {{ font-size:12pt; border-left:4px solid #4651c8; padding-left:8px; margin:11px 0 4px; }}
h3.s {{ font-size:10.5pt; margin:7px 0 2px; color:#2f3a8f; }}
.draft p, .draft li {{ margin:2px 0; }} ol, ul {{ margin:2px 0 5px; padding-left:20px; }}
.hint {{ background:#fff4cc; border:1px solid #efd27a; border-radius:6px; padding:6px 10px; font-size:9.2pt; margin:7px 0; }}
.eq {{ background:#f4f0fb; border-radius:6px; padding:2px 9px; margin:2px 0; display:inline-block; }}
.concl {{ border:2px solid #4651c8; border-radius:8px; padding:6px 11px; margin:6px 0; background:#eef0fd; }}
</style></head><body>

<h1>실험 5. 요오드 적정 (산화환원 적정) — 실험노트 부착용 (1조)</h1>
<div class="sub">점선대로 오려 <b>4면 모두</b> 붙이고, <b>노트 번호(1권)와 부착 페이지 번호</b>를 적고, 부착물과 노트 공란에 <b>겹치게</b> 서명(간인)</div>
<div class="cut"><h3>Table I. [표준액] 0.05 M I₂ 표준액</h3>{T1}{TAG}</div>
<div class="cut"><h3>Table II. [표정] 0.1 M Na₂S₂O₃액 — 간접법 (아이오도메트리)</h3>{T2}{TAG}</div>
<div class="cut"><h3>Table III. [적정 1] 포비돈요오드액 중 요오드 (아이오도메트리)</h3>{T3}{TAG}</div>
<div class="cut"><h3>Table IV. [적정 2] 아스코르브산 (아이오디메트리)</h3>{T4}{TAG}</div>
<div class="cut"><h3>Table V. 대한약전 기준 판정</h3>{T5}{TAG}</div>

<div class="draft brk">
<h1>실험노트 초안 — 볼펜으로 옮겨 적기</h1>
<div class="hint">머리말/꼬리말: <b>1권 · p.__(실험 4에서 이어서) · 서명</b> (매 페이지) · 실험일자 2026. 11. 26.(목) · 1조. 큰 빈 공간만 빗금 한 줄. <b>원리 최소 반 페이지 · 표정과 적정 구분 · 결론 한 줄 · 팩터 셋째 자리.</b><br>
⚠ 판정 기준값(포비돈요오드액 85.0~120.0%, 아스코르브산 99.0% 이상)은 참고값 → <b>대한약전 원문으로 확인</b> 후 옮겨 적기.</div>

<h2>제목</h2><p>실험 5. 요오드 적정 (산화환원 적정)</p>

<h2>1. 목적</h2>
<p>요오드 적정법의 iodimetry와 iodometry 방법을 이용하여 아스코르브산과 포비돈요오드액 중 요오드의 함량을 각각 분석하고, 대한약전 기준을 만족하는지 판정한다.</p>

<h2>2. 원리</h2>
<ul><li><b>Iodimetry</b>는 I₂ 표준액으로 환원성 물질을 직접 적정하는 방법(I₂가 뷰렛)이고, <b>iodometry</b>는 플라스크의 I₂를 Na₂S₂O₃ 표준액으로 적정하는 방법(Na₂S₂O₃가 뷰렛)이다.</li>
<li><b>표준액</b>: 0.05 M I₂ 표준액은 구매한 표준액으로 라벨의 f를 사용한다. I₂ 1 mol은 2당량이므로 0.05 M = 0.1 N이다. 0.1 M Na₂S₂O₃액은 I₂ 표준액(2차 표준물질)으로 간접법 표정하여 f′를 구한다 (KIO₃를 이용한 직접법은 생략).<br>
<span class="eq">I₂ + 2Na₂S₂O₃ → 2NaI + Na₂S₄O₆</span> &nbsp; 0.1 M Na₂S₂O₃ 1 mL ≡ 0.05 M I₂ 1 mL &nbsp; <span class="eq">f′ = f × V(I₂) / V(Na₂S₂O₃)</span></li>
<li><b>포비돈요오드액</b>(10 w/v%, 유효 요오드로서 1 w/v%)의 I₂를 Na₂S₂O₃로 적정한다. 0.1 M Na₂S₂O₃ 1 mL ≡ 0.05 mmol I₂ ≡ 12.691 mg I₂.</li>
<li><b>아스코르브산</b>(C₆H₈O₆, FM 176.12)은 I₂에 의해 1 : 1로 산화된다. 공기 산화를 막기 위해 메타인산용액에 녹인다.<br>
<span class="eq">C₆H₈O₆ + I₂ → C₆H₆O₆ + 2HI</span> &nbsp; 0.05 M I₂ 1 mL ≡ 0.05 mmol ≡ 8.806 mg 아스코르브산</li>
<li><b>전분 지시약</b>: I₂가 전분에 들어가면 짙은 청색이 된다. Iodometry에서는 I₂가 많을 때 넣으면 전분에 강하게 붙잡혀 종말점이 늦어지므로 미황색이 된 종말점 직전에 넣고 청색이 사라지는 점을, iodimetry에서는 처음부터 넣고 지속적인 청색이 나타나는 점을 종말점으로 한다.</li></ul>

<h2>3. 시약 및 기구</h2>
<p>분석저울, magnetic stirrer, Erlenmeyer flask (100, 200 mL), buret (50 mL), amber buret (50 mL), mass cylinder (100 mL), transfer pipet (10 mL), micropipette (1 mL), stand, clamp, 세척병, weighing boat, 아스코르브산(FM 176.12), 포비돈요오드액(10 w/v%), 0.05 M I₂ 표준액(f = {F_I2:.3f}), 탈이온수, 제공된 시약: 0.1 M Na₂S₂O₃액, 전분 지시약(1 w/v% soluble starch), 메타인산용액(1→50)</p>

<h2>4. 실험방법</h2>
<h3 class="s">[표준액] 0.05 M I₂ 표준액</h3>
<p>구매한 표준액을 표정하지 않고 라벨의 f({F_I2:.3f})를 사용하였다.</p>
<h3 class="s">[표정] 0.1 M Na₂S₂O₃액 — 간접법</h3>
<ol><li>I₂ 표준액 {V_I2:.2f} mL를 피펫으로 100 mL 삼각플라스크에 넣고 탈이온수 40 mL(메스실린더)를 가하였다.</li>
<li>Na₂S₂O₃액으로 적정하다가 미황색이 되었을 때 전분 지시약 1 mL를 넣고, 청색이 완전히 사라질 때까지 적정하였다 ({S_S:.2f} → {E_S:.2f} mL).</li></ol>
<h3 class="s">[적정 1] 포비돈요오드액</h3>
<ol><li>요오드로서 100 mg에 해당하는 포비돈요오드액 {V_POV:.2f} mL를 transfer pipet으로 100 mL 삼각플라스크에 넣고, 전체 약 50 mL가 되도록 탈이온수를 가하였다.</li>
<li>Na₂S₂O₃액으로 적정하다가 미황색에서 전분 지시약 1 mL를 넣고 청색이 사라질 때까지 적정하였다 ({S_P:.2f} → {E_P:.2f} mL).</li></ol>
<h3 class="s">[뷰렛 교체]</h3>
<p>Na₂S₂O₃액을 버리고 수돗물, 탈이온수로 씻은 뒤 I₂ 표준액 소량으로 2~3회 헹구고 I₂ 표준액을 채웠다.</p>
<h3 class="s">[적정 2] 아스코르브산</h3>
<ol><li>아스코르브산(조에서 건조하지 않음) {W_AA:.4f} g을 200 mL 삼각플라스크에 넣고 제공된 메타인산용액 50 mL로 녹였다.</li>
<li>전분 지시약 1 mL를 처음부터 넣고(무색), I₂ 표준액으로 적정하였다. {S_A1:.2f} → {E_A1:.2f} mL에서 적정액이 부족하여 뷰렛을 다시 채운 뒤 {S_A2:.2f} → {E_A2:.2f} mL에서 지속적인 청색이 나타났다.</li></ol>
<p>각 적정은 1회씩 수행하였다.</p>

<h2>5. 결과 (Table I–V 부착)</h2>
<h3 class="s">[표정] f′</h3>
<p>V = {E_S:.2f} − {S_S:.2f} = {VS:.2f} mL → <b>f′ = {F_I2:.3f} × {V_I2:.2f} / {VS:.2f} = {FP:.3f}</b></p>
<h3 class="s">[적정 1] 포비돈요오드액</h3>
<p>V = {E_P:.2f} − {S_P:.2f} = {VP:.2f} mL → 요오드 = {VP:.2f} × {FP:.3f} × {EQ_I2:.3f} = {I_MG:.2f} mg → <b>표시량(100 mg) 대비 {POV:.1f}%</b></p>
<h3 class="s">[적정 2] 아스코르브산</h3>
<p>V = ({E_A1:.2f} − {S_A1:.2f}) + ({E_A2:.2f} − {S_A2:.2f}) = {VA1:.2f} + {VA2:.2f} = {VA:.2f} mL → 아스코르브산 = {VA:.2f} × {F_I2:.3f} × {EQ_AA:.3f} = {AA_MG:.2f} mg → <b>함량 = {AA_MG:.2f} / {W_AA * 1000:.1f} × 100 = {AA:.1f}%</b></p>

<h2>6. 고찰 및 결론</h2>
<ol><li>Na₂S₂O₃액의 f′는 {FP:.3f}로 1보다 컸다. 실험실에서 만든 용액이 규정 농도보다 약간 진하게 만들어졌거나, 표정 시 종말점을 일찍 판단해 V가 작게 측정되었을 수 있다. 이 f′를 그대로 사용하였으므로 포비돈요오드액 결과에도 같은 방향으로 반영된다.</li>
<li>포비돈요오드액의 요오드는 표시량의 {POV:.1f}%로 이론 종말점(100 / 12.691 / {FP:.3f} = {LABEL / EQ_I2 / FP:.2f} mL)과 거의 일치하였다.</li>
<li>아스코르브산은 {AA:.1f}%로 측정되어 참고 기준(99.0% 이상)보다 약간 낮았다. 100%라면 소비량이 {EXP_A:.2f} mL여야 하나 {VA:.2f} mL가 들었다. 원인으로 다음을 유추할 수 있다. ① 유인물은 "건조된 아스코르브산"을 쓰도록 하나 조에서 건조하지 않아, 수분만큼 실제 아스코르브산이 칭량값보다 적었을 수 있다(함량 과소). ② 적정 도중 적정액이 부족해 뷰렛을 다시 채우는 동안 아스코르브산 용액이 공기에 노출되어 일부가 공기 중 산소로 산화되었을 수 있다(소비량 감소, 함량 과소). ③ 뷰렛 눈금을 네 번 읽어 읽기 오차(±0.02 mL씩)가 더해졌고, 50.00 mL는 눈금 맨 아래라 읽기가 어려웠다.</li>
<li>공시험을 하지 않았고 각 적정을 1회만 수행하여 재현성을 확인하지 못하였다. I₂ 표준액의 f는 라벨 값을 그대로 믿었다.</li>
<li>대책 및 개선 방안: 아스코르브산을 건조해 사용한다. 시료량으로 소비량을 미리 계산해(0.2 g → 약 22.6 mL) 적정 전에 뷰렛을 충분히 채우거나 시료량을 줄여 재충전이 없도록 한다. 시료를 녹인 즉시 적정한다. 공시험과 3회 반복을 한다.</li></ol>
<div class="concl"><b>결론</b><br>
1. 포비돈요오드액의 유효 요오드는 표시량의 {POV:.1f}%로 대한약전 기준({POV_LO:.1f}~{POV_HI:.1f}%)을 <b>{'만족한다' if POV_OK else '만족하지 않는다'}</b>.<br>
2. 아스코르브산의 함량은 {AA:.1f}%로 대한약전 기준({AA_LO:.1f}% 이상)을 <b>{'만족한다' if AA_OK else '만족하지 않는다'}</b>{'' if AA_OK else ' (단, 시료를 건조하지 않았고 적정 중 재충전이 있어 재측정이 필요하다)'}.</div>
</div>
</body></html>"""
open(os.path.join(D, "note.html"), "w", encoding="utf-8").write(html)
print(f"VS={VS} f'={FP} VP={VP} I={I_MG:.2f} mg {POV}% | VA={VA} AA={AA_MG:.2f} mg {AA}% exp={EXP_A:.2f} | POV_OK={POV_OK} AA_OK={AA_OK}")
