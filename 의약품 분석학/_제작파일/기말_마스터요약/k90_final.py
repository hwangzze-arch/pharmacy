from parts import *
F = "시험 직전 10분"

pairs = dict(t="r", id="f-pairs", html=f"""
<div class="hd"><span class="bd">최종 정리 ①</span><div class="tt"><h1>혼동 쌍 총정리 — 보기에서 단어 하나 바꿔치기 당하는 곳</h1><div class="sb">Confusing pairs · mass spectrometry</div></div><span class="pt">{F}</span></div>
<div class="body"><div class="main"><table class="t">
<tr><th>헷갈리는 쌍</th><th>왼쪽</th><th>오른쪽</th></tr>
<tr><td>질량 vs m/z</td><td>MS가 재는 것 = <b>항상 m/z</b></td><td>질량은 직접 못 잼 (z를 알아야 환산)</td></tr>
<tr><td>분자량 vs 정밀질량</td><td>평균 (108.965, C₂H₅Br)</td><td>단일동위원소 (107.958) = MS 피크 위치</td></tr>
<tr><td>exact vs accurate mass</td><td>분자식으로 계산한 이론값</td><td>HRMS로 측정한 실측값</td></tr>
<tr><td>양성자 vs H 원자</td><td>1.007276 ([M+H]⁺ 계산용)</td><td>1.007825 (분자식 질량 계산용)</td></tr>
<tr><td>EI vs CI</td><td>70 eV · 분석물 직접 · M⁺• · 하드</td><td>100–200 eV · 시약 기체 · [M+H]⁺ · 소프트</td></tr>
<tr><td>분자이온 vs 준분자 이온</td><td>M⁺• (홀전자)</td><td>[M+H]⁺, [M−H]⁻ (짝전자)</td></tr>
<tr><td>기준 피크 vs 분자이온</td><td>가장 센 피크 = 100%</td><td>분자 그 자체 — 다를 때가 많음</td></tr>
<tr><td>RP vs Resolution(Δm)</td><td>m/Δm, m/FWHM — 클수록 좋음</td><td>Δm = m/RP — 작을수록 좋음 (현실에선 RP 의미)</td></tr>
<tr><td>10% valley vs FWHM</td><td>두 피크, 실험적으로 어려움</td><td>피크 하나, 현재 표준, 약 2배 큰 값</td></tr>
<tr><td>질소 규칙</td><td>M⁺•: N 홀 ↔ 질량 홀</td><td>[M±H]±·짝전자 조각: 뒤집힘</td></tr>
<tr><td>M+1 vs M+2</td><td>M+1 = 탄소 (1.08n)</td><td>M+2 = Cl(32n)·Br(97.3n)·S(4.52n)</td></tr>
<tr><td>Cl vs Br</td><td>3 : 1</td><td>1 : 1 (쌍둥이)</td></tr>
<tr><td>α-절단 vs McLafferty</td><td>라디칼 손실 → 짝전자 (43, 85)</td><td>중성 분자 손실 → 홀전자 (58)</td></tr>
<tr><td>HRMS vs MS/MS</td><td>같은 명목질량·다른 분자식 구별</td><td>같은 분자식(이성질체) 구별</td></tr>
</table></div><div class="side"><table class="t">
<tr><th>헷갈리는 쌍</th><th>정리</th></tr>
<tr><td>사중극자 극성</td><td><b>DC</b>가 결정 (RF는 극성 없음)</td></tr>
<tr><td>+ 전극 vs − 전극 (양이온)</td><td>+ = high-mass(무거운 것 <b>통과</b>) / − = low-mass</td></tr>
<tr><td>음이온 분석 시</td><td>두 전극 역할 <b>반대</b></td></tr>
<tr><td>기울기 ↑</td><td>분해능 ↑, 통과 구간 ↓</td></tr>
<tr><td>사중극자 vs TOF</td><td>단위 분해능 / 고분해능</td></tr>
<tr><td>TOF t vs m/z</td><td>m/z ∝ t² (t ∝ √(m/z))</td></tr>
<tr><td>리플렉트론</td><td>빠른 이온 = 깊이 = 긴 경로</td></tr>
<tr><td>GC vs LC 이온화</td><td>EI·CI / ESI·APCI·APPI</td></tr>
<tr><td>ESI vs APCI</td><td>용액 vs 기체 · 휘발성 No vs Yes · 단백질 O vs X</td></tr>
<tr><td>약산 vs 약염기 (ESI)</td><td>음이온 모드 / 양이온 모드</td></tr>
<tr><td>SIM vs EIC</td><td>측정 전 선택 / 측정 후 추출</td></tr>
<tr><td>Product vs Precursor scan</td><td>SIM-On-Scan / Scan-On-SIM</td></tr>
<tr><td>SRM vs MRM</td><td>같은 말 (SIM-On-SIM)</td></tr>
<tr><td>CID vs CAD</td><td>같은 말</td></tr>
<tr><td>SRM의 S/N↑</td><td>신호↑ 아님, <b>잡음↓</b></td></tr>
</table></div></div>""")

nums = dict(t="r", html=f"""
<div class="hd"><span class="bd">최종 정리 ②</span><div class="tt"><h1>숫자 · 공식 카드 — 바로 꺼내 쓰기</h1><div class="sb">Numbers & formulas to memorize</div></div><span class="pt">{F}</span></div>
<div class="body"><div class="main">
<div class="cols">
<div class="card"><div class="ct">📐 공식</div>
M⁺• = M − 0.000549 · [M+H]⁺ = M + 1.007276<br>
RP = m/Δm = m/FWHM · Δm = m/RP<br>
필요 RP = m / (두 정밀질량 차)<br>
DBE = C − (H+X)/2 + N/2 + 1 (O·S 무시)<br>
M+1(%) ≈ 1.08·C + 0.012·H (+0.369·N + 0.038·O)<br>
C 수 ≈ M+1(%) ÷ 1.08<br>
C의 M+2 = 0.0058·n(n−1)<br>
Cl X+2 = 32.0n · Br X+2 = 97.3n, X+4 = 47.3n(n−1)<br>
자기장 섹터: m/z = B²r²e/2V<br>
TOF: ½mv² = zeV → m/z = (2eV/L²)·t²<br>
다가 이온: m/z = (M + n)/n</div>
<div class="card"><div class="ct">🔢 숫자 카드 ①</div>
EI: 70 eV · 분자에 12–15 eV · ~0.01%만 이온화<br>
이온화 에너지: n 11.0 &lt; π 14.1 &lt; σ 15.9 eV<br>
CI: 시약 기체 ~1 mbar · 전자 100–200 eV · CH₅⁺ · [M+29]⁺<br>
펜토바르비탈 226 → CI MH⁺ 227 · EI 기준 156<br>
솔라닌 868.5: RP 1,737 (FWHM 0.5) / 48,250 (0.018)<br>
C₅H₈O 84.0570 vs C₆H₁₂ 84.0934 → RP ≈ 2,300<br>
CO 27.995 · N₂ 28.006 · C₂H₄ 28.031<br>
벤젠 M+1 6.55% · 바이페닐 13.08% · 1-브로모뷰테인 M+1 4.4%, M+2 97.4%<br>
BSA ~66.5 kDa, C₂₉₃₄H₄₅₈₁N₇₈₂O₈₉₇S₃₉</div>
</div></div><div class="side">
<div class="card"><div class="ct">🔢 숫자 카드 ②</div>
사중극자: RF ~1 MHz (가정용 60 Hz) · 최대 ~0.3 Da<br>
TOF 가속 ~5,000 V · 소수점 셋째 자리<br>
진공: Orbitrap 10⁻¹⁰ &lt; TOF 10⁻⁹ &lt; Q 10⁻⁶ &lt; QIT 10⁻³ torr<br>
ESI: ±3,500 V (그림 −4,500 V) · 1984 개발 · 2002 노벨상<br>
APCI: ~500 °C · 코로나 니들 ~6,000 V · H₃O⁺<br>
부가 이온: +1, +18, +23, +39 / −1, +45, +59<br>
제초제 1 ppb · SIM m/z 312 · EIC m/z 202<br>
QQQ 모드: 3 × 2 × 3 = 18 → 실제 6<br>
EE2 [M−H]⁻ 295 → 159 + 145 · 3.6 ppt (ng/L)<br>
ppm 10⁻⁶ · ppb 10⁻⁹ · <b>ppt 10⁻¹²</b><br>
아세트아미노펜 151 · [M+H]⁺ 152 → 110 (−42 케텐) · [M−H]⁻ 150 → 107 (−43)<br>
니페디핀 346 · [M+H]⁺ 347 → 315 (−32 MeOH) · DBE 10</div>
<div class="card trap"><div class="ct">⚠️ 마지막 체크</div>m/z ≠ 질량 · 양성자 1.007276 · 질소 규칙 뒤집기 · Cl 3:1 / Br 1:1 · 기울기↑ = 분해능↑ · + 전극 = 고질량 <b>통과</b> · t² · ESI는 휘발성 X · SIM ≠ EIC · SRM = 잡음↓</div>
</div></div>""")


chrom = dict(t="r", html=f"""
<div class="hd"><span class="bd">최종 정리 ③</span><div class="tt"><h1>크로마토그래피 기초 — 혼동 쌍 · 숫자 · 공식</h1><div class="sb">Chromatography fundamentals</div></div><span class="pt">{F}</span></div>
<div class="body"><div class="main"><table class="t">
<tr><th>헷갈리는 쌍</th><th>왼쪽</th><th>오른쪽</th></tr>
<tr><td>추출 vs 크로마토그래피</td><td>두 상 모두 움직임</td><td>한 상은 <b>고정</b></td></tr>
<tr><td>eluent vs eluate</td><td>들어가는 이동상</td><td>나오는 용출액</td></tr>
<tr><td>이름 규칙</td><td>이동상이 결정 (GC/LC)</td><td>“기체-고체” = 앞 이동상, 뒤 고정상</td></tr>
<tr><td>칼럼 vs TLC 흐름 힘</td><td>중력</td><td>모세관</td></tr>
<tr><td>양이온 vs 음이온교환 수지</td><td>표면 <b>음전하</b>(–SO₃⁻), 양이온을 잡음</td><td>표면 <b>양전하</b>(–N(CH₃)₃⁺), 음이온을 잡음</td></tr>
<tr><td>크기배제 용출 순서</td><td><b>큰 분자 먼저</b></td><td>작은 분자(염)는 구멍 출입 → 늦게</td></tr>
<tr><td>t_m vs t′_r</td><td>이동상 시간 (공통)</td><td>고정상 시간 = t_r − t_m</td></tr>
<tr><td>α vs γ</td><td>t′_r 비 (중요)</td><td>t_r 비 (별로 안 씀)</td></tr>
<tr><td>H vs N</td><td>작을수록 좋음, <b>길이 단위</b></td><td>클수록 좋음, <b>단위 없음</b>, L에 비례</td></tr>
<tr><td>w vs w½</td><td>4σ (바닥폭) → R = Δt_r/w</td><td>2.35σ → R = 0.589Δt_r/w½</td></tr>
<tr><td>tailing vs fronting</td><td>A/B &gt; 1 (뒤로 꼬리, 흔함)</td><td>A/B &lt; 1 (앞으로)</td></tr>
<tr><td>B항 vs C항 (D↑)</td><td>B항 <b>나빠짐</b></td><td>C항 <b>좋아짐</b></td></tr>
<tr><td>u 느림 vs 빠름</td><td>B항이 H를 키움</td><td>C항이 H를 키움</td></tr>
<tr><td>개관 vs 충전</td><td>A = 0, 길게, 빠르게, 용량↓ (GC)</td><td>용량↑, 압력↑, N↓ (LC)</td></tr>
</table></div><div class="side">
<div class="card"><div class="ct">📐 공식</div>
K = [S]₂/[S]₁ · t′_r = t_r − t_m<br>
k′ = t′_r/t_m = K·V_s/V_m · α = t′_r2/t′_r1 = K₂/K₁ · γ = t_r2/t_r1<br>
V_r = t_r·u_v · u_x = u_v/πr² (개관)<br>
R = Δt_r/w_av = 0.589Δt_r/w½,av = (√N/4)(γ − 1)<br>
w = 4σ = 1.70w½ · w½ = 2.35σ<br>
J = −D dc/dx · σ = √(2Dt) · H = 2D/u_x = σ²/x<br>
N = L/H = 16t_r²/w² = 5.55t_r²/w½² · H = L/N<br>
N(비대칭) ≈ 41.7(t_r/w₀.₁)²/(A/B + 1.25)<br>
H = A + B/u + C·u · u_opt = √(B/C) · H_min = A + 2√(BC)<br>
Cₛ ∝ d²/Dₛ · Cₘ ∝ r²/Dₘ</div>
<div class="card"><div class="ct">🔢 숫자</div>
R 0.5/0.75/1.0/1.5 = 2σ/3σ/4σ/6σ · 목표 R ≥ 1.5<br>
비대칭 인자 허용 ~0.8–1.2 (우수 1.0–1.05, 불가 2)<br>
D: 기체 ~10⁻⁵ · 액체 ~10⁻⁹ · 단백질 ~10⁻¹¹ m²/s<br>
성적서: 30 mm, N 5335, H 5.6 μm, k′ 4.19<br>
온도: 30 ℃·1 mL/min ~10분 vs 100 ℃·5 mL/min &lt;1분<br>
표 22-3: 충전 2.4 m N 3 290 R 1.5 / 개관 100 m N 294 000 R 10.6</div>
<div class="card trap"><div class="ct">⚠️ 마지막 체크</div>α엔 t′_r · w인지 w½인지 · H에 단위 · N에 단위 X · L 2배 → R √2배 · 개관 = A가 0 (C 아님) · 크기배제 = 큰 것 먼저</div>
</div></div>""")

E = [pairs, nums, chrom]
