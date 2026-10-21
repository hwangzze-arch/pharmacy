from parts import *
F = "시험 직전 10분"

pairs = dict(t="r", id="f-pairs", html=f"""
<div class="hd"><span class="bd">최종 정리 ①</span><div class="tt"><h1>혼동 쌍 총정리 — 보기에서 단어 하나 바꿔치기 당하는 곳</h1><div class="sb">Confusing pairs</div></div><span class="pt">{F}</span></div>
<div class="body"><div class="main"><table class="t">
<tr><th>헷갈리는 쌍</th><th>왼쪽</th><th>오른쪽</th></tr>
<tr><td>A vs T</td><td>A = −log T, <b>b·c에 비례</b></td><td>T = 10⁻ᴬ, 곱셈으로 줄어듦</td></tr>
<tr><td>비흡광도 vs 비선광도</td><td>E = A/(b·c), c = <b>g/100 mL</b>, b = <b>cm</b></td><td>[α] = 100α/(l·c), c = <b>g/mL</b>, l = <b>mm</b></td></tr>
<tr><td>비선광도 vs 몰선광도</td><td>[α] = 100α/(l·c)</td><td>[M] = [α]·MW/<b>1000</b></td></tr>
<tr><td>D₂ vs W 램프</td><td>중수소 = UV, 110–400 nm, 아크방전</td><td>텅스텐(할로겐) = Vis·NIR, 320–2500 nm</td></tr>
<tr><td>연속 vs 선 광원</td><td>D₂·Xe·Hg-Xe (UV-Vis용)</td><td>중공음극램프 193–852 nm (AAS용)</td></tr>
<tr><td>석영 vs 유리 셀</td><td>석영 = UV + Vis</td><td>유리 = Vis만 (UV 흡수)</td></tr>
<tr><td>PMT vs PD vs PDA</td><td>PMT = 다이노드 90 V 계단, 10⁶배</td><td>PD = 빛→전류 반도체 / PDA = 배열, 전 파장 동시·S/N↑·튼튼</td></tr>
<tr><td>K띠 vs R띠</td><td>K = π→π*, ~240 nm, ε ~10⁴</td><td>R = n→π*, ~305 nm, ε ~10²</td></tr>
<tr><td>batho vs hypso</td><td>bathochromic = 장파장(적색) 이동</td><td>hypsochromic = 단파장(청색) 이동</td></tr>
<tr><td>hyper vs hypo</td><td>hyperchromic = 흡광 증가</td><td>hypochromic = 흡광 감소</td></tr>
<tr><td>발색단 vs 조색단</td><td>직접 흡수 (C=C, C=O)</td><td>자신은 흡수 못 함, λ·ε 변화 (–OH, –NH₂)</td></tr>
<tr><td>표준물첨가 vs 검량선</td><td>시료에 표준을 <b>섞음</b> → |X절편|</td><td>표준과 시료 <b>따로</b> → (A−b)/a</td></tr>
<tr><td>형광 vs 인광</td><td>S₁→S₀, 같은 스핀, 10⁻⁸–10⁻⁴ s</td><td>T₁→S₀, 다른 스핀, 10⁻⁴–10² s</td></tr>
<tr><td>내부전환 vs 계간전이</td><td>S₁→S₀ 열로</td><td>S₁→T₁ 스핀 뒤집힘</td></tr>
<tr><td>여기 vs 방출 스펙트럼</td><td>λex 스캔, λem 고정 (흡수 닮음)</td><td>λem 스캔, λex 고정 (거울상)</td></tr>
<tr><td>형광광도계 vs 발광광도계</td><td>광원 + 단색화장치 2개, 90°</td><td>광원·여기 단색화장치 없음</td></tr>
<tr><td>R/S vs (+)/(−)</td><td>명명 규칙(구조)</td><td>측정한 회전 방향 — 서로 무관</td></tr>
<tr><td>광학순도 vs ee</td><td>[α]비 × 100 (실험값)</td><td>%R − %S (조성) — 수치는 같다</td></tr>
</table></div><div class="side"><table class="t">
<tr><th>헷갈리는 쌍</th><th>정리</th></tr>
<tr><td>AES / AAS / AFS</td><td>열→발광 / 램프빛 흡수 / 흡수 후 재발광(90°)</td></tr>
<tr><td>HCL 원리 = AES?</td><td><b>O</b> (램프 안은 발광, 분석법은 AAS)</td></tr>
<tr><td>화염 vs 흑연로</td><td>&lt;1 s·mL·빠름 / 수 초·μL·감도↑·Ar</td></tr>
<tr><td>ICP-AES 간섭</td><td>화학 간섭 매우 적음, <b>스펙트럼 간섭 많음</b></td></tr>
<tr><td>흑연로 간섭</td><td><b>화학 간섭 매우 많음</b></td></tr>
<tr><td>차폐 vs 탈차폐</td><td>전자↑ = 차폐 = 진동수↓ = δ↓ = 오른쪽(높은 장)</td></tr>
<tr><td>낮은 장 vs 높은 장</td><td>낮은 장 = <b>왼쪽 = δ 큼</b></td></tr>
<tr><td>벤젠 vs 알카인</td><td>7.27 탈차폐 / 2–3 차폐 (이방성)</td></tr>
<tr><td>δ vs J</td><td>δ(ppm) 자기장 무관 / J(Hz) 자기장 무관, ppm 간격은 고자장에서 좁아짐</td></tr>
<tr><td>Δν(Hz)</td><td>자기장에 <b>비례</b>해 바뀜</td></tr>
<tr><td>²J vs ³J</td><td>geminal(무시) / <b>vicinal(해석의 핵심, 5–15 Hz)</b></td></tr>
<tr><td>CW vs FT</td><td>진동수 고정·자기장 스캔 / 펄스→FID→FT, 누적</td></tr>
<tr><td>¹H vs ¹³C</td><td>99.98 %·0–12 ppm·갈라짐 / 1.1 %·0–220 ppm·단일선(짝풀림)</td></tr>
</table></div></div>""")

nums = dict(t="r", html=f"""
<div class="hd"><span class="bd">최종 정리 ②</span><div class="tt"><h1>숫자 · 공식 카드 — 계산기 없이 바로 꺼내 쓰기</h1><div class="sb">Numbers & formulas to memorize</div></div><span class="pt">{F}</span></div>
<div class="body"><div class="main">
<div class="cols">
<div class="card"><div class="ct">📐 공식 12개</div>
c = λν · E = hν = hc/λ<br>
A = −log T = log(I₀/I) · T = 10⁻ᴬ<br>
A = εbc = abc · ε = E¹%₁cm × MW/10<br>
E¹%₁cm = A/(b·c) [c: g/100 mL]<br>
표준물첨가: x = s·Aₓ/(A_T − Aₓ) / 다점: |X절편| = y절편/기울기<br>
검량선: Cₓ = (Aₓ − b)/a · 표준품 비교: T = S × A_T/A_S<br>
형광(묽을 때): I = kP₀c<br>
[α] = 100α/(l·c) [l: mm, c: g/mL] · [M] = [α]·MW/1000<br>
포도당(mg) = α × 1895.4 · 광학순도 = ee = %R − %S<br>
한도시험: 표준 mL × 표준 ppm = 시료 g × 한도 ppm<br>
ν₀ = γB₀/2π · ΔE = γhB₀/2π · δ = Δν(Hz)/ν₀(Hz) × 10⁶<br>
J(ppm) = J(Hz)/ν₀(MHz) · 피크 수 = n + 1</div>
<div class="card"><div class="ct">🔢 숫자 카드</div>
UV ≈ 200–400 nm · Vis ≈ 400–800 nm<br>
이완 10⁻⁶–10⁻⁹ s · 흡수 10⁻¹⁵ s<br>
최적 A 0.3–1.5 · log 2 = 0.30, log 3 = 0.48<br>
D₂ 110–400 · W 320–2500 · HCL 193–852 nm<br>
PMT: 다이노드 +90 V, 10⁶배 · PDA &lt; 1 s<br>
공액 1개당 +30 nm, ε ×2 · 에텐 171 nm<br>
K띠 ~241–245 nm ε 10⁴ / R띠 ~305–308 nm ε 10²<br>
물 200 · MeOH 210 · 아세톤 330 nm (cutoff)<br>
형광 10⁻⁸–10⁻⁴ s · 인광 10⁻⁴–10² s<br>
흡수 10⁻⁶ M vs 형광 10⁻¹¹ M</div>
</div></div><div class="side">
<div class="card"><div class="ct">🔢 숫자 카드 (계속)</div>
Na D선 589 nm · 포도당 [α] +52.5~+53.0°<br>
원자선 폭 0.001 nm / 분자 10–100 nm<br>
HCL: Ne/Ar 1–5 Torr, 500 V<br>
아세틸렌–공기 2400–2700 K · 흑연로 2550 °C ≤7 s<br>
ICP 6000–10000 K · RF 27/41 MHz<br>
Na 589 · Ca 422.7(+La₂O₃) · Mg 285 · Zn 213.9 · Se 196.03 nm<br>
생약: Pb 5 · As 3 · Hg 0.2 · Cd 0.3 mg/kg<br>
NMR 핵 5개: ¹H ¹³C ¹⁵N ¹⁹F ³¹P<br>
¹H γ 267.53, ¹³C 67.28 (×10⁶) · 2.35 T = 100 MHz · 14.1 T = 600 MHz · 1.41 T = 60 MHz · 28.2 T = 1.2 GHz<br>
σ(H) 0–0.00002 · TMS 0 ppm (Si 1.9 &lt; H 2.2 &lt; C 2.5)<br>
알킬 0–2 · C=O 옆 2–3 · O 옆 3–4.5 · 알켄 4.5–6.5 · 방향족 6.5–8 · CHO 9–10 · COOH 10–12<br>
³J 5–15 Hz · ¹³C: 1.1 %, 감도 1.6 %, 0–220 ppm</div>
<div class="card trap"><div class="ct">⚠️ 마지막 체크</div>단위(mg→g, mm, g/mL) · 분취 배수(×10) · 공시험 빼기 · 정제는 표시량 대비 · [M]은 ÷1000 · 부호(−) 유지 · δ 분모는 Hz</div>
</div></div>""")

E = [pairs, nums]
