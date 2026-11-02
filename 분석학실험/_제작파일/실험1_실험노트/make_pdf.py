# -*- coding: utf-8 -*-
"""실험1 실험노트: 오려 붙이는 Table I · II · Figure 1 + 손으로 옮겨 적을 초안 → note.html"""
import os, sys
D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(D, "..", "실험1_요약정리"))
from svgs import curve, f2, STYLE

READ = [0.00, 10.00, 20.00, 30.00, 39.98, 50.00]
MASS = [59.0550, 69.0390, 79.0397, 89.0361, 98.9286, 108.8970]
RHO = 0.99842
ROWS = []
for r, m in zip(READ, MASS):
    w = round(m - MASS[0], 4)
    v = round(w / RHO, 2)
    ROWS.append((r, m, w, v, round(v - r, 2)))
INT = [(f"{ROWS[i][0]:.0f} → {ROWS[i+1][0]:.0f}", round(ROWS[i+1][0] - ROWS[i][0], 2), round(ROWS[i+1][3] - ROWS[i][3], 2))
       for i in range(5)]
CMIN, CMAX = min(r[4] for r in ROWS), max(r[4] for r in ROWS)

t1 = "".join(f"<tr><td>{r:.2f}</td><td>{m:.4f}</td><td>{w:.4f}</td><td>{v:.2f}</td><td><b>{f2(c, True)}</b></td></tr>" for r, m, w, v, c in ROWS)
t2 = "".join(f"<tr><td>{a}</td><td>{b:.2f}</td><td>{c:.2f}</td><td><b>{f2(round(c - b, 2), True)}</b></td></tr>" for a, b, c in INT)
fig = curve([(r, c) for r, _, _, _, c in ROWS], "Figure 1. 50 mL 뷰렛의 검정곡선 (수온 19.0 °C, 1회 측정)", w=560, h=300)

FONTS = "".join(f'<link rel="stylesheet" href="file://{p}">' for p in (os.path.expanduser(f"~/.fonts/nskr/package/{w}.css") for w in (400, 700)) if os.path.exists(p))
html = f"""<!doctype html><html lang="ko"><head><meta charset="utf-8">{FONTS}<title>실험1 실험노트</title><style>
@page {{ size: A4; margin: 14mm 15mm; }}
body {{ font-family: 'Noto Sans KR','Pretendard',sans-serif; color:#222; font-size:10.5pt; line-height:1.6; margin:0; }}
h1 {{ font-size:15pt; margin:0 0 2px; }} .sub {{ color:#666; font-size:9pt; margin-bottom:10px; }}
.cut {{ border:1.4px dashed #888; padding:9px 12px; margin:0 auto 14px; width:160mm; position:relative; break-inside:avoid; }}
.cut::before {{ content:'✂'; position:absolute; top:-11px; left:-4px; background:#fff; color:#888; font-size:13px; }}
.cut h3 {{ font-size:10.5pt; margin:0 0 5px; }}
table {{ border-collapse:collapse; width:100%; font-size:9.6pt; }}
th, td {{ border:1px solid #666; padding:3px 6px; text-align:center; }} th {{ background:#eee; }}
.note {{ font-size:8.6pt; color:#555; margin-top:4px; }}
.brk {{ break-before:page; }}
h2 {{ font-size:12pt; border-left:4px solid #4651c8; padding-left:8px; margin:14px 0 6px; }}
.draft p, .draft li {{ margin:2px 0; }} ol, ul {{ margin:2px 0 6px; padding-left:20px; }}
.hint {{ background:#fff4cc; border:1px solid #efd27a; border-radius:6px; padding:6px 10px; font-size:9.4pt; margin:8px 0; }}
{STYLE.replace("<style>", "").replace("</style>", "")}
</style></head><body>

<h1>실험 1. 뷰렛의 검정 — 실험노트 부착용</h1>
<div class="sub">점선대로 오려서 노트에 <b>4면 모두</b> 붙이고, 노트와 종이에 걸쳐 <b>간인(서명)</b>할 것</div>

<div class="cut"><h3>Table I. 50 mL 뷰렛의 검정 결과 (수온 19.0 °C, ρ = 0.99842 g/mL, 1회 측정)</h3>
<table><tr><th>뷰렛 눈금 (mL)</th><th>플라스크 + 물 (g)</th><th>물 무게 (g)</th><th>실제 부피 (mL)</th><th>보정치 (mL)</th></tr>{t1}</table>
<div class="note">물 무게 = (플라스크 + 물) − 59.0550 g · 실제 부피 = 물 무게 ÷ 0.99842 g/mL · 보정치 = 실제 부피 − 뷰렛 눈금 · 40 mL 측정 중 소량 흘림</div></div>

<div class="cut"><h3>Table II. 구간별 보정치</h3>
<table><tr><th>구간 (mL)</th><th>눈금 차 (mL)</th><th>실제 부피 차 (mL)</th><th>구간 보정치 (mL)</th></tr>{t2}</table></div>

<div class="cut">{fig}<div class="note">초록 점선 = 제조사 허용오차 ±0.10 mL · 모든 점이 허용오차 이내</div></div>

<div class="draft brk">
<h1>실험노트 초안 — 볼펜으로 옮겨 적기</h1>
<div class="hint">맨 위: <b>실험일자</b> 2026. __. __.(목, 실험한 날) · <b>분석학실험 No.1</b> · p.__ · <b>서명</b>. 매 페이지 서명·페이지 번호, 남는 공간은 사선 + "여백".</div>

<h2>제목</h2><p>실험 1. 뷰렛의 검정 (Buret Calibration)</p>

<h2>1. 목적</h2>
<p>부피측정용 유리기구에 대해 제작자의 허용오차 범위 내에서 실제 유리측용기로 정확한 부피 측정이 이루어질 수 있는지 검정한다.</p>

<h2>2. 원리</h2>
<ul><li>증류수를 담은 뷰렛에서 일정 눈금만큼 물을 유출시켜 저울로 질량을 재고, 그 온도에서의 물의 밀도로 나누어 실제 부피를 구한다. (V = m / ρ)</li>
<li>보정치 = 실제 부피 − 뷰렛 눈금. 보정된 부피 = 읽은 눈금 + 보정치.</li>
<li>수용(TC, To Contain) 측용기는 용기 안에 담긴 부피를 보증하고(예: 부피플라스크), 출용(TD, To Deliver) 측용기는 다른 용기로 옮긴 부피를 보증한다(예: 뷰렛, 피펫).</li>
<li>뷰렛은 TD 기구이며, 허용오차는 20 °C에서 ±0.1 mL이다.</li></ul>

<h2>3. 시약 및 기구</h2>
<p>buret (50 mL) &amp; stand, buret holder, Erlenmeyer flask (100 mL), beaker (100 mL), washing bottle, chemical balance, 탈이온수</p>

<h2>4. 실험방법</h2>
<ol><li>뷰렛을 탈이온수로 헹군 뒤 물을 채워 누출 여부를 확인하였다.</li>
<li>스톱콕을 열어 기포를 제거하고, 눈높이를 메니스커스에 맞추어 0.00 mL에 맞추었다.</li>
<li>빈 삼각플라스크의 무게를 측정하였다. (59.0550 g)</li>
<li>탈이온수를 한 방울씩 유출시켜 10.00 mL에서 멈추고, 플라스크 + 물의 무게를 측정하였다.</li>
<li>같은 저울로 20.00, 30.00, 39.98, 50.00 mL까지 누적하여 반복하였다. (40 mL 측정 도중 소량 흘림)</li>
<li>수온 19.0 °C에서의 물의 밀도 0.99842 g/mL로 실제 부피와 보정치를 계산하고 검정곡선을 작성하였다.</li></ol>

<h2>5. 결과</h2>
<ul><li>수온 19.0 °C, 물의 밀도 ρ = 0.99842 g/mL (유인물 Table 1.2)</li>
<li>Table I, Table II, Figure 1 (부착)</li>
<li>보정치 범위: {f2(CMIN, True)} ~ {f2(CMAX, True)} mL</li></ul>

<h2>6. 고찰 및 결론</h2>
<ol><li>보정치는 {f2(CMIN, True)} ~ {f2(CMAX, True)} mL로 모두 제조사 허용오차(±0.1 mL) 이내였으므로, 사용한 뷰렛은 보증 정확도를 만족한다.</li>
<li>0–30 mL 구간의 보정치는 0.00 ~ +0.03 mL로 작았으나, 40 mL와 50 mL에서는 각각 −0.04, −0.08 mL로 음수였다. 40 mL 측정 도중 물을 소량 흘려 30 → 40 mL 구간의 보정치가 −0.07 mL로 다른 구간(−0.04 ~ +0.02 mL)보다 크게 음수였고, 무게를 누적 측정하였으므로 이 손실은 50 mL 값에도 그대로 포함된다. 따라서 40, 50 mL의 보정치는 실제보다 음의 방향으로 치우쳐 있다고 판단된다.</li>
<li>그 밖의 오차 원인으로는 눈금 읽기의 시차오차, 0.01 mL 자리의 눈대중 읽기, 수온 측정 오차, 플라스크 외벽의 물방울 및 입구에서의 증발 등을 생각할 수 있다.</li>
<li>유인물은 2회 반복 측정을 요구하나 이번 실험은 1회만 수행하여 재현성을 확인하지 못하였다. 특히 물을 흘린 40–50 mL 구간은 재측정이 필요하다.</li>
<li>이후 적정에서는 이 검정곡선으로 시작 눈금과 최종 눈금을 각각 보정하여 실제 유출 부피를 구한다.</li></ol>
</div>
</body></html>"""
open(os.path.join(D, "note.html"), "w", encoding="utf-8").write(html)
for r in ROWS: print(r)
for i in INT: print(i)
