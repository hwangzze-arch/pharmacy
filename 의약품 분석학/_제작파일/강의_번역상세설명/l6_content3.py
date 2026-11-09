PAGES = [
# 17 (27)
dict(img=17, slide=27, title="Fick의 확산 제1법칙", sub="Fick’s first law of diffusion: J = −D (dc/dx)",
kw=["플럭스 J (mol·m⁻²·s⁻¹)", "확산계수 D (m²·s⁻¹)", "농도 기울기 dc/dx", "음(−)의 부호"],
sum="단위 면적을 지나가는 확산 플럭스 J는 농도 기울기와 확산계수 D에 비례한다. 고농도→저농도로 흐르니까 기울기와 반대 방향이라 (−) 부호가 붙는다.",
tr="""<p><b>Fick의 확산 제1법칙</b>: 단위 면적의 평면을 가로질러 확산하는 분자의 <b>플럭스(J)</b>는 <b>농도 기울기</b>와 <b>확산계수(D)</b>에 비례한다.</p>
<p class="eq">Flux (mol / m<sup>2</sup>·s) ≡ J = −D (dc/dx)</p>
<ul><li><b>플럭스 (J)</b>: 1초에 1 m<sup>2</sup>를 가로지르는 몰수 (단위: mol·m<sup>−2</sup>·s<sup>−1</sup>)</li>
<li><b>확산계수 (D)</b>: 비례상수 (단위: m<sup>2</sup>·s<sup>−1</sup>)</li>
<li><b>음의 부호</b>가 필요한 이유: 알짜 플럭스가 고농도 영역에서 저농도 영역으로 향하기 때문</li></ul>
<p>그림: 위치 x(농도 c)와 x + dx(농도 c − dc)의 두 평면 사이. 고농도 → 저농도로 플럭스 J (1초에 1 m<sup>2</sup>당 mol)</p>""",
ex="""<p>문장 그대로 식이 돼: “<y>얼마나 많이 흐르나(J)</y> = <y>얼마나 잘 움직이나(D)</y> × <y>농도 차가 얼마나 가파른가(dc/dx)</y>”.</p>
<p><b>부호 확인</b>: 오른쪽으로 갈수록 농도가 낮아지면 dc/dx < 0 → J = −D × (음수) = <g>양수 → 오른쪽(저농도 쪽)으로 흐름</g> ✓. 부호가 없으면 물질이 저농도에서 고농도로 모인다는 말이 돼서 틀려.</p>
<p><b>단위 확인</b>: D (m<sup>2</sup>/s) × dc/dx (mol/m<sup>3</sup> ÷ m = mol/m<sup>4</sup>) = <g>mol/(m<sup>2</sup>·s)</g> = J의 단위 ✓</p>
<p><b>예제</b>: D = 1.0 × 10<sup>−9</sup> m<sup>2</sup>/s, 1 mm(10<sup>−3</sup> m) 사이에 농도가 1.0 mol/m<sup>3</sup> 떨어짐<br>J = 1.0 × 10<sup>−9</sup> × (1.0 / 10<sup>−3</sup>) = <b>1.0 × 10<sup>−6</sup> mol·m<sup>−2</sup>·s<sup>−1</sup></b></p>
<div class="boxg">크로마토그래피에서: 띠 가운데(고농도)에서 앞뒤 가장자리(저농도)로 용질이 계속 새어 나가 → 띠가 넓어져. D가 클수록(작은 분자, 기체 속) 더 빨리 넓어져.</div>"""),

# 18 (28)
dict(img=18, slide=28, title="대표적인 확산계수 (298 K)", sub="TABLE 22-1 Representative diffusion coefficients",
kw=["액체 속 D ~10⁻⁹ m²/s", "기체 속 D ~10⁻⁵ m²/s", "큰 분자일수록 D 작음", "H⁺ 특이적으로 큼"],
sum="액체 속 작은 분자의 D는 약 10⁻⁹ m²/s, 기체 속은 약 10⁻⁵ m²/s로 1만 배 크다. 단백질처럼 큰 분자는 D가 작다(10⁻¹¹). 그래서 GC와 LC의 띠 넓어짐 양상이 다르다.",
tr="""<p><b>표 22-1 298 K에서의 대표적인 확산계수</b> (용질 / 용매 / 확산계수 m<sup>2</sup>/s)</p>
<ul><li>H<sub>2</sub>O / H<sub>2</sub>O: 2.3 × 10<sup>−9</sup> · 수크로스 / H<sub>2</sub>O: 0.52 × 10<sup>−9</sup> · 글라이신 / H<sub>2</sub>O: 1.1 × 10<sup>−9</sup> · CH<sub>3</sub>OH / H<sub>2</sub>O: 1.6 × 10<sup>−9</sup></li>
<li>리보뉴클레이스 (FM 13 700) / H<sub>2</sub>O (293 K): 0.12 × 10<sup>−9</sup> · 혈청 알부민 (FM 66 000) / H<sub>2</sub>O (293 K): 0.059 × 10<sup>−9</sup></li>
<li>I<sub>2</sub> / 헥세인: 4.0 × 10<sup>−9</sup> · CCl<sub>4</sub> / 헵테인: 3.2 × 10<sup>−9</sup> · N<sub>2</sub> / CCl<sub>4</sub>: 3.4 × 10<sup>−9</sup></li>
<li>CS<sub>2</sub>(g) / 공기 (293 K): <b>1.0 × 10<sup>−5</sup></b> · O<sub>2</sub>(g) / 공기 (273 K): <b>1.8 × 10<sup>−5</sup></b></li>
<li>H<sup>+</sup>: 9.3 × 10<sup>−9</sup> · OH<sup>−</sup>: 5.3 × 10<sup>−9</sup> · Li<sup>+</sup>: 1.0 × 10<sup>−9</sup> · Na<sup>+</sup>: 1.3 × 10<sup>−9</sup> · K<sup>+</sup>, Cl<sup>−</sup>, I<sup>−</sup>: 2.0 × 10<sup>−9</sup> (모두 H<sub>2</sub>O)</li></ul>""",
ex="""<p>숫자를 다 외울 필요는 없고 <y>자릿수와 경향</y>만 잡아.</p>
<table class="t"><tr><th>경우</th><th>D (m<sup>2</sup>/s)</th><th>의미</th></tr>
<tr><td>기체 속 작은 분자</td><td><b>~10<sup>−5</sup></b></td><td>액체보다 <pk>약 10<sup>4</sup>배</pk> 빠름</td></tr>
<tr><td>액체 속 작은 분자</td><td><b>~10<sup>−9</sup></b></td><td>물, 메탄올, 이온 대부분</td></tr>
<tr><td>액체 속 단백질</td><td>~10<sup>−11</sup></td><td>클수록 느림 (알부민 < 리보뉴클레이스)</td></tr></table>
<ul><li><b>크기 경향</b>: 글라이신(75) 1.1 > 수크로스(342) 0.52 > 리보뉴클레이스(13 700) 0.12 > 알부민(66 000) 0.059 (× 10<sup>−9</sup>). 무거울수록 D↓</li>
<li><b>H<sup>+</sup>, OH<sup>−</sup>가 유난히 큰 이유</b>: 물 분자 사이로 양성자가 “릴레이”처럼 전달되는 특별한 기전(그로투스 기전) 때문</li></ul>
<div class="boxg"><b>크로마토그래피 연결</b>: 세로 확산(B항, 슬라이드 40) ∝ D<sub>m</sub>. 기체 이동상은 D<sub>m</sub>이 1만 배 커서 <pk>GC에서는 B항이 중요</pk> → 유속을 빠르게 해서 칼럼에 머무는 시간을 줄여야 해. LC에서는 D<sub>m</sub>이 작아서 B항 영향이 작고, 대신 물질 전달(C항)이 문제야.</div>"""),

# 19 (29)
dict(img=19, slide=29, title="확산에 의한 띠 넓어짐 — σ = √(2Dt)", sub="Broadening of chromatography band by diffusion",
kw=["확률밀도함수", "c = m/√(4πDt)·e^(−x²/4Dt)", "2σ² = 4Dt", "σ = √(2Dt)", "w ∝ σ ∝ √t"],
sum="확산 방정식의 해가 정규분포 모양이고, 정규분포 식과 비교하면 2σ² = 4Dt → σ = √(2Dt). 띠 폭은 시간의 제곱근에 비례해서 넓어진다.",
tr="""<p><b>확산에 의한 크로마토그래피 띠 넓어짐</b></p>
<p class="eq">y = 1/(σ√(2π)) · e<sup>−(x−μ)<sup>2</sup>/2σ<sup>2</sup></sup> &nbsp;(확률밀도함수)</p>
<p class="eq">c = m/√(4πDt) · e<sup>−x<sup>2</sup>/(4Dt)</sup></p>
<p class="eq">c(x = 0에서) = m/√(4πDt)</p>
<p class="eq">2σ<sup>2</sup> = 4Dt &nbsp;→&nbsp; σ = √(2Dt)<br>띠 폭 (w) ∝ σ ∝ √t</p>
<ul><li>c: 용질 농도 (mol/m<sup>3</sup>) · D: 확산계수</li>
<li>m: 처음에 칼럼 단위 단면적당 넣은 용질 양 (mol/m<sup>2</sup>)</li>
<li>x: 현재 띠 중심으로부터 칼럼을 따라 잰 거리 · t: 시료 주입 후 시간</li></ul>
<p>그림: 표준정규분포 (평균 0 ± σ, 가운데 2σ 구간 표시)</p>""",
ex="""<p><b>두 식의 지수 부분을 비교</b>해 봐 (μ = 0, 띠 중심 기준).</p>
<p class="eq">정규분포: x<sup>2</sup>/<b>2σ<sup>2</sup></b> &nbsp;↔&nbsp; 확산 해: x<sup>2</sup>/<b>4Dt</b> → <g>2σ<sup>2</sup> = 4Dt → σ<sup>2</sup> = 2Dt</g></p>
<p>즉 <y>확산으로 퍼진 띠 = 표준편차가 √(2Dt)인 정규분포</y>. 슬라이드 24 Q의 수학적 답이야.</p>
<ul><li><b>c(x=0) = m/√(4πDt)</b>: 시간이 갈수록 피크 높이는 1/√t로 낮아져. 넓어지는 만큼 낮아져서 면적(m)은 보존돼.</li>
<li><b>w ∝ √t</b>: 시간이 4배면 폭은 2배. “선형”이 아니라 <pk>제곱근</pk>이라는 게 포인트.</li></ul>
<p><b>예제</b>: D = 1.0 × 10<sup>−9</sup> m<sup>2</sup>/s(액체 속 작은 분자), t = 600 s(10분)<br>σ = √(2 × 10<sup>−9</sup> × 600) = √(1.2 × 10<sup>−6</sup>) = <b>1.1 × 10<sup>−3</sup> m ≈ 1.1 mm</b><br>같은 시간 기체 속(D = 10<sup>−5</sup>)이면 σ = √(1.2 × 10<sup>−2</sup>) ≈ <b>11 cm</b>! → GC에서 세로 확산이 왜 큰 문제인지 보여줘.</p>"""),

# 20 (30)
dict(img=20, slide=30, title="이론단의 높이 H (HETP)", sub="Plate height: a measure of column efficiency",
kw=["σ² = Hx", "H = 2D/u_x = σ²/x", "HETP", "분별 증류의 단", "H 작을수록 좋음"],
sum="t = x/u_x를 σ² = 2Dt에 넣으면 σ² = (2D/u_x)x = Hx. 비례상수 H가 이론단 높이(HETP)로, 이동상과 고정상 사이 평형 1번에 필요한 칼럼 길이. H가 작을수록 피크가 좁고 분리가 좋다.",
tr="""<p><b>이론단의 높이 (plate height): 칼럼 효율의 척도</b></p>
<p class="eq">σ = √(2Dt), &nbsp; t = x/u<sub>x</sub><br>(x: 용질이 이동한 거리, u<sub>x</sub>: 용질의 길이 속도)</p>
<p class="eq">σ<sup>2</sup> = 2Dt = 2D(x/u<sub>x</sub>) = (2D/u<sub>x</sub>)x = Hx &nbsp;(H: 이론단 높이)</p>
<p class="eq">H = 2D/u<sub>x</sub> = σ<sup>2</sup>/x</p>
<p><b>이론단 높이</b>:</p>
<ul><li>띠의 분산(σ<sup>2</sup>)과 용질이 칼럼을 따라 이동한 거리(x) 사이의 비례상수</li>
<li><b>이론단 상당 높이(HETP)</b>라고도 한다</li>
<li>대략 용질이 이동상과 고정상 사이에서 <b>평형을 한 번</b> 이루는 데 필요한 칼럼 길이</li></ul>
<p><b>작은 이론단 높이 → 좁은 피크 → 높은 분리도 → 더 나은 분리</b></p>
<p>그림: 연속 분별 증류(정유탑) — 단마다 온도가 달라 휘발유·등유·경유 등으로 나뉨</p>""",
ex="""<p>이름의 유래는 오른쪽 <b>분별 증류탑</b>이야. 탑 안의 “단(plate)” 하나하나에서 증기와 액체가 평형을 이뤄. 단이 많을수록 끓는점이 비슷한 성분도 잘 갈라져.</p>
<p>크로마토그래피 칼럼엔 실제 판이 없지만, <y>“평형 한 번에 해당하는 길이”를 가상의 단 높이 H</y>로 정의한 거야.</p>
<div class="boxg"><b>σ<sup>2</sup> = Hx</b>: 분산은 이동 거리에 비례해 커져. 같은 거리를 가도 <b>H가 작은 칼럼일수록 띠가 덜 퍼져</b>.<br>H의 단위 = σ<sup>2</sup>/x = 길이<sup>2</sup>/길이 = <b>길이</b> (mm, μm)</div>
<ul><li><b>H = 2D/u<sub>x</sub></b>는 “확산만” 고려한 식이야. 유속이 빠르면 칼럼에 덜 머물러서 덜 퍼짐(H↓). 실제로는 다른 요인(A, C항)도 있어서 이걸 종합한 게 <pk>van Deemter 식</pk>(슬라이드 39)이야.</li>
<li><b>개념 정리</b>: H↓ → 같은 길이에 단이 많음(N↑) → 피크 폭↓ → 분리도↑</li></ul>
<p class="note">HPLC 칼럼 H는 보통 수 μm ~ 수십 μm (입자 지름의 2–3배 정도).</p>"""),

# 21 (31)
dict(img=21, slide=31, title="이론단수 N", sub="N: number of (theoretical) plates on column",
kw=["N = L/H", "N = 16t_r²/w²", "N = t_r²/σ²", "N = 5.55t_r²/w½²"],
sum="이론단수 N = 칼럼 길이 / 이론단 높이. σ² = HL과 w = 4σ를 쓰면 N = 16t_r²/w² = 5.55t_r²/w½². 크로마토그램에서 머무름시간과 피크 폭만 재면 계산된다.",
tr="""<p><b>이론단 높이: 칼럼 효율의 척도</b></p>
<p><b>N: 칼럼의 (이론)단 수 (이론단수)</b></p>
<p class="eq">N = L/H = Lx/σ<sup>2</sup> = L<sup>2</sup>/σ<sup>2</sup> = L<sup>2</sup>/(w/4)<sup>2</sup> = 16L<sup>2</sup>/w<sup>2</sup></p>
<p class="eq">N = 16t<sub>r</sub><sup>2</sup>/w<sup>2</sup> = t<sub>r</sub><sup>2</sup>/σ<sup>2</sup></p>
<p class="eq">N = 16t<sub>r</sub><sup>2</sup>/w<sup>2</sup> = 16t<sub>r</sub><sup>2</sup>/(1.70w<sub>1/2</sub>)<sup>2</sup> = 5.55t<sub>r</sub><sup>2</sup>/w<sub>1/2</sub><sup>2</sup></p>
<p>그림: 가우스 피크(w = 4σ, w<sub>1/2</sub> = 2.35σ). 아래: 길이 L인 칼럼을 높이 H인 단으로 나눈 그림</p>""",
ex="""<p><b>유도 따라가기</b>: 용질이 칼럼 끝(x = L)에 왔을 때 σ<sup>2</sup> = HL → H = σ<sup>2</sup>/L → <g>N = L/H = L<sup>2</sup>/σ<sup>2</sup></g>.</p>
<p>여기서 σ와 L은 “길이” 단위인데, 크로마토그램은 “시간” 축이지? 피크 중심까지 L ↔ t<sub>r</sub>, 폭 σ ↔ 시간 σ로 같은 비율로 바뀌니까 <g>N = t<sub>r</sub><sup>2</sup>/σ<sup>2</sup></g> (비율이라 단위 상관없음). 같은 단위로만 재면 돼.</p>
<table class="t"><tr><th>재는 폭</th><th>식</th><th>상수 유래</th></tr>
<tr><td>바닥폭 w (= 4σ)</td><td><b>N = 16t<sub>r</sub><sup>2</sup>/w<sup>2</sup></b></td><td>4<sup>2</sup> = 16</td></tr>
<tr><td>반높이 폭 w<sub>1/2</sub> (= 2.35σ)</td><td><b>N = 5.55t<sub>r</sub><sup>2</sup>/w<sub>1/2</sub><sup>2</sup></b></td><td>2.35<sup>2</sup> = 5.55</td></tr></table>
<p><b>예제</b>: t<sub>r</sub> = 10.0 min, w<sub>1/2</sub> = 0.20 min<br>N = 5.55 × (10.0/0.20)<sup>2</sup> = 5.55 × 2500 = <b>13 900단</b><br>칼럼 L = 15 cm면 H = 150 mm / 13 900 = <b>0.011 mm = 11 μm</b></p>
<div class="box"><span class="tag">주의</span>t<sub>r</sub>과 w는 반드시 <b>같은 단위</b>(둘 다 min 또는 둘 다 s). 그리고 <pk>N은 피크마다 다르게</pk> 계산될 수 있어(보통 늦게 나온 피크로 칼럼 성능 표시).</div>"""),

# 22 (32)
dict(img=22, slide=32, src="원본 슬라이드 32 (번호 없음)", title="실제 칼럼 성적서로 N, H 확인", sub="RESTEK LC Certificate of Analysis — Raptor BiPh column",
kw=["칼럼 성적서", "Plates/column 5335", "H = L/N = 5.6×10⁻³ mm", "k′ 4.19", "Symmetry 1.15"],
sum="실제 판매 칼럼(길이 30 mm, 입자 2.7 μm)의 성적서. 마지막 피크(바이페닐) t_r = 0.80 min, w½ = 0.03 min으로 N = 5335단, H = 30 mm / 5335 = 5.6 × 10⁻³ mm/plate.",
tr="""<p><b>RESTEK LC 분석 성적서 (Certificate of Analysis)</b> — 칼럼 성능 보고서</p>
<ul><li>충전물: Raptor BiPh · 칼럼 길이: <b>30 mm</b> · 안지름: 2.1 mm · 입자 크기: <b>2.7 μm</b></li>
<li>크로마토그램 (254 nm): 0.153 우라실 → 0.427 톨루엔 → 0.583 나프탈렌 → <b>0.796 바이페닐</b></li>
<li>이동상: 55/45 ACN/물 · 유속: 0.4 mL/min · 압력: 1090 psi · 파장: 254 nm · 시료량: 1.0 μL · 온도: 상온</li>
<li><b>마지막 피크의 성능 결과</b>: 머무름시간 0.80 min · k′ 4.19 · 반높이 폭 0.03 min · 10%에서의 대칭성 1.15 · 칼럼당 단수 <b>5335</b> · 미터당 단수 177832</li></ul>
<p class="eq">H = L/N = 30 mm / 5335 plates = <b>5.6 × 10<sup>−3</sup> mm/plate</b></p>""",
ex="""<p>앞에서 배운 식이 실제 제품 성적서에 다 들어 있어. 하나씩 검산해 보자.</p>
<table class="t"><tr><th>항목</th><th>검산</th></tr>
<tr><td><b>H</b></td><td>30 mm / 5335 = <b>5.6 × 10<sup>−3</sup> mm = 5.6 μm</b> (입자 2.7 μm의 약 2배 ✓)</td></tr>
<tr><td>Plates/meter</td><td>5335 / 0.030 m = <b>1.78 × 10<sup>5</sup></b> ✓</td></tr>
<tr><td><b>t<sub>m</sub></b> (k′로 역산)</td><td>k′ = (t<sub>r</sub> − t<sub>m</sub>)/t<sub>m</sub> → t<sub>m</sub> = 0.80/(1 + 4.19) = <b>0.154 min</b> → <pk>첫 피크 우라실(0.153)이 바로 t<sub>m</sub> 표지!</pk></td></tr>
<tr><td>N (반높이 폭)</td><td>5.55 × (0.80/0.03)<sup>2</sup> ≈ 3.9 × 10<sup>3</sup></td></tr></table>
<p class="note">N 검산이 5335와 다른 건 반높이 폭이 0.03으로 반올림돼 표시됐기 때문이야. 5335가 되려면 w<sub>1/2</sub> ≈ 0.0258 min. 소수 둘째 자리 반올림이 제곱으로 커진 거지.</p>
<ul><li><b>Symmetry at 10% = 1.15</b>: 다음 슬라이드의 비대칭 인자. 1.0–1.2면 양호.</li>
<li>우라실은 극성이 커서 역상 칼럼에 거의 안 붙어 → HPLC의 <g>비머무름 표지</g> (GC의 CH<sub>4</sub> 역할)</li></ul>"""),

# 23 (33)
dict(img=23, slide=33, title="꼬리 끄는 피크의 이론단수 · 비대칭 인자", sub="Estimation of N for an asymmetric tailing peak (Foley–Dorsey)",
kw=["tailing", "w₀.₁ = A + B", "비대칭 인자 A/B", "N ≈ 41.7(t_r/w₀.₁)²/(A/B + 1.25)", "As 1.0–1.05 우수"],
sum="꼬리 끄는 피크는 가우스 식으로 N을 구하면 틀린다. 높이 10%에서 앞쪽 폭 B, 뒤쪽 폭 A를 재서 N ≈ 41.7(t_r/w₀.₁)²/(A/B + 1.25)로 계산. 비대칭 인자 As = 1.0–1.05 우수, 1.2 허용, 2 불가.",
tr="""<p><b>비대칭으로 꼬리 끄는 피크의 이론단수 추정</b></p>
<p class="eq">N ≈ 41.7(t<sub>r</sub>/w<sub>0.1</sub>)<sup>2</sup> / (A/B + 1.25)</p>
<p>w<sub>0.1</sub> = A + B (높이의 1/10에서의 폭) · <b>A/B: 비대칭 인자 (asymmetry factor)</b></p>
<p>그림 왼쪽: 높이의 1/10에서 피크 중심 수직선 기준 앞쪽 폭 B, 뒤쪽(꼬리) 폭 A</p>
<p>그림 오른쪽: A<sub>s</sub> = B/A (여기서는 A = 앞쪽, B = 뒤쪽), 피크 높이 10%에서 측정</p>
<ul><li><b>우수</b>: A<sub>s</sub> = 1.0 – 1.05 · <b>허용</b>: A<sub>s</sub> = 1.2</li>
<li><b>허용 불가</b>: A<sub>s</sub> = 2 · <b>매우 나쁨</b>: A<sub>s</sub> = 4</li></ul>
<p>A<sub>s</sub>: 비대칭 인자</p>""",
ex="""<p><pk>두 그림의 A, B 표기가 반대</pk>야. 하지만 의미는 같아: <g>비대칭 인자 = 꼬리 쪽 폭 / 앞쪽 폭</g> (10% 높이). 대칭이면 1, 꼬리 끌수록 1보다 커.</p>
<p><b>예제</b>: t<sub>r</sub> = 10.0 min, 10% 높이에서 앞쪽 0.20, 꼬리 쪽 0.40 min → w<sub>0.1</sub> = 0.60, 비대칭 = 2.0<br>N ≈ 41.7 × (10.0/0.60)<sup>2</sup> / (2.0 + 1.25) = 41.7 × 278 / 3.25 ≈ <b>3.6 × 10<sup>3</sup></b></p>
<div class="box"><span class="tag">족보</span><b>“HPLC에서 tailing을 어떻게 막는지”</b> 주관식 출제.<br>
<b>원인 → 해결</b><br>
① 염기성 약물(아민)이 실리카 표면에 남은 <b>실라놀(Si–OH⁻)</b>과 이온 상호작용 → <b>엔드캡(end-capped) 칼럼</b> 사용, <b>이동상 pH를 낮춰</b>(산성 완충액, 0.1% TFA·포름산) 실라놀 이온화 억제, 트라이에틸아민 같은 <b>경쟁 염기 첨가</b><br>
② 시료 과부하 → 주입량·농도 줄이기<br>
③ 칼럼 입구 오염·공극(void) → <b>가드 칼럼</b> 사용, 칼럼 교체<br>
④ 연결 배관의 불필요한 부피(dead volume) → 짧고 가는 배관, 정확한 연결</div>"""),

# 24 (34)
dict(img=24, slide=34, title="분리도에 영향을 주는 요인 — R = (√N/4)(γ − 1)", sub="Factors affecting resolution",
kw=["R = (√N/4)(γ − 1)", "R ∝ √N ∝ √L ∝ 1/√H", "w ∝ σ ∝ √H ∝ 1/√N", "L-Phe vs L-Phe-D₅ 반복 통과"],
sum="분리도는 √N과 (γ − 1)에 비례. 칼럼 길이를 4배로 해야 분리도가 2배가 된다. 피크 폭은 √H에 비례, √N에 반비례. 거의 같은 두 물질(α = 1.03)도 칼럼을 여러 번 통과시키면 결국 분리된다.",
tr="""<p><b>분리도에 영향을 주는 요인</b></p>
<p class="eq">분리도 = (√N / 4)(γ − 1)</p>
<p>γ = u<sub>A</sub>/u<sub>B</sub> = t<sub>B</sub>/t<sub>A</sub>: 보정하지 않은 상대 머무름 (γ > 1)<br>u<sub>A</sub>, u<sub>B</sub>: 성분 A, B의 길이 속도 · t<sub>A</sub>, t<sub>B</sub>: 성분 A, B의 머무름시간</p>
<p class="eq">분리도 ∝ √N ∝ √L ∝ 1/√H &nbsp;(N: 피크 A의 단수)</p>
<p>Q: 피크 폭(w)과 H 및 N의 상관관계는? &nbsp; <b>w ∝ σ ∝ √H ∝ 1/√N</b></p>
<p>예: 0.5 mM L-Phe와 0.5 mM L-Phe-D<sub>5</sub>를 Hypersil C8 칼럼 한 쌍(25 cm × 4.6 mm)에 <b>반복 통과</b>시켜 분리. 이동상 10:90 아세토나이트릴:물(물에 25 mM Na<sub>2</sub>SO<sub>4</sub>, 0.1% TFA). 첫 통과의 상대 머무름 α = 1.03.</p>
<p>그림: 통과 횟수(n)가 늘수록 Phe-D<sub>5</sub>와 Phe 피크가 점점 갈라짐. 오른쪽: (분리도)<sup>2</sup> vs 통과 횟수 → 직선</p>""",
ex="""<p><b>R을 키우는 두 손잡이</b></p>
<ul><li><b>(γ − 1)</b> = 선택성: 이동상 조성, 고정상 종류, 온도를 바꿔 두 성분의 머무름 차이를 키움 (화학)</li>
<li><b>√N</b> = 효율: 칼럼을 길게(L↑) 하거나 H를 작게(입자 작게) 함 (물리)</li></ul>
<div class="boxg"><b>Q 정답</b>: σ<sup>2</sup> = HL → σ ∝ √H. N = L/H이니까 L 고정이면 √H ∝ 1/√N → <b>w ∝ σ ∝ √H ∝ 1/√N</b>. 단이 많을수록 피크가 좁아져.</div>
<p><b>계산 포인트</b> (√ 관계라서 시험에 잘 나와)</p>
<table class="t"><tr><th>바꾸면</th><th>N</th><th>R</th></tr>
<tr><td>L 2배</td><td>2배</td><td><b>√2 = 1.41배</b></td></tr>
<tr><td>R을 2배로 하려면</td><td><b>4배</b></td><td>2배 (칼럼 4배 길게)</td></tr>
<tr><td>H 절반 (작은 입자)</td><td>2배</td><td>1.41배</td></tr></table>
<p><b>L-Phe vs 중수소 표지 L-Phe-D<sub>5</sub></b>: 거의 똑같은 물질(α = 1.03)이라 한 번에는 안 갈라지지만, 칼럼을 n번 통과 = 칼럼이 n배 길어진 효과 → N ∝ n → <g>R<sup>2</sup> ∝ n</g> (오른쪽 그래프가 직선인 이유).</p>
<p><b>예제</b>: N = 10 000, γ = 1.05 → R = (100/4)(0.05) = <b>1.25</b>. R = 1.5가 되려면 √N = 1.5 × 4 / 0.05 = 120 → N = <b>14 400</b></p>"""),

# 25 (39)
dict(img=25, slide=39, title="van Deemter 식 — H = A + B/u_x + C·u_x", sub="Plate height equation: The van Deemter equation",
kw=["A: 여러 흐름 경로", "B/u_x: 세로 확산", "C·u_x: 평형 시간(물질 전달)", "u_opt = √(B/C)", "H_min"],
sum="이론단 높이는 세 항의 합: 유속과 무관한 A(여러 경로), 유속에 반비례하는 B/u_x(세로 확산), 유속에 비례하는 C·u_x(평형 시간). 그래서 H가 최소가 되는 최적 유속 u_opt = √(B/C)가 있다.",
tr="""<p><b>띠는 왜 퍼지는가 — 이론단 높이 식: van Deemter 식</b></p>
<ul><li>이론단 높이 H는 크로마토그래피 띠의 분산에 비례한다</li>
<li>van Deemter 식은 칼럼과 유속이 이론단 높이에 어떤 영향을 주는지 알려준다</li></ul>
<p class="eq">H ≈ A + B/u<sub>x</sub> + C·u<sub>x</sub></p>
<ul><li><b>A</b>: 여러 흐름 경로 (multiple flow paths)</li>
<li><b>B/u<sub>x</sub></b>: 세로 확산 (longitudinal diffusion)</li>
<li><b>C·u<sub>x</sub></b>: 평형 시간 (equilibration time)</li>
<li>A, B, C: 주어진 칼럼과 고정상에서의 상수</li></ul>
<p class="eq">u<sub>opt</sub>에서 B/u<sub>opt</sub> = C·u<sub>opt</sub> → u<sub>opt</sub> = √(B/C)<br>H<sub>min</sub> = A + B/u<sub>opt</sub> + C·u<sub>opt</sub></p>
<p>그래프: 이론단 높이(mm) vs 유속(mL/min). 점선 = A(수평), B/u<sub>x</sub>(감소 곡선), Cu<sub>x</sub>(증가 직선). 실선 = 세 항의 합. 약 30–40 mL/min에서 최소</p>""",
ex="""<p><pk>시험 최다 출제 슬라이드!</pk> 세 항이 유속에 어떻게 반응하는지가 핵심이야.</p>
<table class="t"><tr><th>항</th><th>원인</th><th>u<sub>x</sub>↑ 하면</th><th>줄이는 법</th></tr>
<tr><td><b>A</b></td><td>입자 사이 길이 다른 여러 경로</td><td>변화 없음</td><td>작고 균일한 입자, <b>개관 칼럼은 A = 0</b></td></tr>
<tr><td><b>B/u<sub>x</sub></b></td><td>띠가 앞뒤로 확산</td><td><g>감소</g> (칼럼에 덜 머묾)</td><td>빠른 유속, D<sub>m</sub> 작은 이동상</td></tr>
<tr><td><b>C·u<sub>x</sub></b></td><td>두 상 사이 평형이 느림</td><td><pk>증가</pk> (평형 못 따라감)</td><td>얇은 고정상, 작은 입자·가는 칼럼, 고온</td></tr></table>
<p><b>u<sub>opt</sub> 유도</b>: dH/du = −B/u<sup>2</sup> + C = 0 → <g>u<sub>opt</sub> = √(B/C)</g>, 이때 B/u = Cu(두 항이 같음) → <g>H<sub>min</sub> = A + 2√(BC)</g></p>
<p><b>예제</b>: A = 1.0 mm, B = 25 mm·mL/min, C = 0.025 mm·min/mL<br>u<sub>opt</sub> = √(25/0.025) = √1000 ≈ <b>32 mL/min</b>, H<sub>min</sub> = 1.0 + 2√(0.625) = <b>2.6 mm</b></p>
<div class="box"><span class="tag">족보</span><b>“van Deemter로 왜 입자 작은 칼럼이 유리한지, 발생하는 문제는?”</b><br>
<b>장점</b>: 입자↓ → 경로가 균일해져 <b>A↓</b>, 고정상 속 확산 거리가 짧아져 <b>C↓</b> → H<sub>min</sub>↓(N↑, 분리↑), 그리고 C가 작아 곡선 오른쪽이 평평 → <b>빠른 유속에서도 효율 유지</b>(분석 시간↓)<br>
<b>문제</b>: 입자 사이 틈이 좁아져 <b>역압(back pressure)이 급증</b> (대략 1/d<sub>p</sub><sup>2</sup>) → 고압 펌프(UHPLC) 필요, 칼럼 막힘, 마찰열</div>"""),

# 26 (40)
dict(img=26, slide=40, title="세로 확산 (B/u_x)", sub="Longitudinal diffusion",
kw=["세로 확산", "σ² = 2D_m t = 2D_m L/u_x", "H_D = 2D_m/u_x ≡ B/u_x", "빠른 유속 → 확산↓"],
sum="띠가 칼럼 축 방향(앞뒤)으로 확산해 넓어지는 것. 칼럼에 머무는 시간 t = L/u_x에 비례하니까 유속이 빠를수록 덜 퍼진다. H_D = 2D_m/u_x = B/u_x.",
tr="""<p><b>세로 확산 (Longitudinal diffusion)</b></p>
<p>그림: 칼럼에 짧게 머문 후의 용질 띠(좁음) → 세로 확산 (B/u<sub>x</sub>) → 칼럼에 오래 머문 후의 용질 띠(넓음). 이동 방향 →</p>
<p class="eq">H ≈ A + B/u<sub>x</sub> + C·u<sub>x</sub> &nbsp;(A: 여러 경로, B/u<sub>x</sub>: 세로 확산, C·u<sub>x</sub>: 평형 시간)</p>
<p><b>길이 유속이 빠를수록</b><br>→ 칼럼에서 보내는 시간이 짧다<br>→ 확산이 적다<br>→ 띠 넓어짐이 적다</p>
<p class="eq">σ<sup>2</sup> = 2D<sub>m</sub>t = 2D<sub>m</sub>L/u<sub>x</sub><br>H<sub>D</sub> = σ<sup>2</sup>/L = 2D<sub>m</sub>/u<sub>x</sub> ≡ B/u<sub>x</sub></p>
<p>D<sub>m</sub>: 이동상 속 확산계수 · H<sub>D</sub>: 세로 확산에 의한 이론단 높이 · L: 칼럼 길이 · u<sub>x</sub>: 길이 유속 · t: 시간</p>""",
ex="""<p>슬라이드 29–30에서 유도한 σ = √(2Dt), H = 2D/u<sub>x</sub>가 바로 이 <b>B항</b>이야. 이제 이름이 생긴 거지.</p>
<ul><li>칼럼을 통과하는 시간 t = L/u<sub>x</sub> → <y>유속이 2배면 머무는 시간 절반 → σ<sup>2</sup> 절반</y></li>
<li>그래서 <g>B = 2D<sub>m</sub></g> (실제 충전 칼럼에선 입자 때문에 길이 꼬불꼬불해져 약간 보정 계수가 붙음)</li></ul>
<table class="t"><tr><th></th><th>D<sub>m</sub></th><th>B항의 중요성</th></tr>
<tr><td><b>GC</b> (기체 이동상)</td><td>~10<sup>−5</sup> m<sup>2</sup>/s</td><td><pk>매우 큼</pk> → 너무 느린 유속은 치명적</td></tr>
<tr><td><b>LC</b> (액체 이동상)</td><td>~10<sup>−9</sup> m<sup>2</sup>/s</td><td>작음 → 보통 C항이 지배</td></tr></table>
<p><b>예제</b>: 유속을 1.0 → 0.5 mL/min으로 줄이면 B/u<sub>x</sub>는 <b>2배</b>가 돼 (C·u<sub>x</sub>는 절반).</p>
<p class="note">그래프 왼쪽(유속이 아주 느린 쪽)에서 H가 급격히 치솟는 이유가 이 항이야.</p>"""),

# 27 (41)
dict(img=27, slide=41, title="두 상 사이의 유한한 평형 시간 (C·u_x)", sub="Finite equilibration time between phases",
kw=["물질 전달", "느린 평형", "고정상 쪽 용질이 뒤처짐", "느린 유속 → 평형 완전"],
sum="용질이 이동상과 고정상 사이를 오가며 평형을 이루는 데 시간이 걸린다. 이동상은 계속 흘러가니까 고정상 속 용질은 뒤처지고 이동상 속 용질은 앞서 나가 띠가 넓어진다. 유속이 느릴수록 평형이 완전해 덜 퍼진다.",
tr="""<p><b>두 상 사이의 유한한 평형 시간</b></p>
<p>그림: 처음엔 이동상(위)과 고정상(아래)의 띠가 같은 위치(띠 폭). <b>느린 평형 (Cu<sub>x</sub>)</b> 때문에 얼마 이동한 후에는 이동상 쪽 띠는 앞서고 고정상 쪽 띠는 뒤처져 전체 띠 폭이 넓어짐. 용리 방향 →</p>
<p class="eq">H ≈ A + B/u<sub>x</sub> + C·u<sub>x</sub></p>
<p><b>길이 유속이 느릴수록</b><br>→ 평형이 더 완전하게 이루어진다<br>→ 띠 넓어짐이 적다</p>""",
ex="""<p><b>에스컬레이터 비유</b>: 친구 무리가 움직이는 에스컬레이터(이동상)와 옆 계단(고정상)을 계속 갈아타며 올라간다고 해 봐. 갈아타는 데 시간이 걸리면, 에스컬레이터에 있던 애들은 앞서가고 계단에 있던 애들은 뒤처져서 무리가 <y>길게 늘어져</y>.</p>
<ul><li>에스컬레이터가 <b>빠를수록</b>(u<sub>x</sub>↑) 그 사이에 더 많이 벌어짐 → <g>C·u<sub>x</sub>는 유속에 비례</g></li>
<li>느리면 갈아타기(평형)가 충분히 일어나서 무리가 뭉쳐 다님</li></ul>
<table class="t"><tr><th></th><th>유속↑</th><th>유속↓</th></tr>
<tr><td>B/u<sub>x</sub> (세로 확산)</td><td>감소 ✓</td><td>증가 ✗</td></tr>
<tr><td>C·u<sub>x</sub> (평형 시간)</td><td>증가 ✗</td><td>감소 ✓</td></tr></table>
<p>→ 두 항이 <pk>유속에 대해 반대로</pk> 움직이니까 그 사이 어딘가에 최적 유속(u<sub>opt</sub>)이 생기는 거야.</p>
<p class="note">HPLC에서 최적 유속보다 빠르게 돌릴 때 효율이 떨어지는 주원인이 이 C항이야. 다음 슬라이드가 C를 줄이는 방법이야.</p>"""),

# 28 (42)
dict(img=28, slide=42, title="물질 전달 항 C = C_s + C_m", sub="Plate height due to finite equilibration time (mass transfer term)",
kw=["C_s ∝ d²/D_s", "C_m ∝ r²/D_m", "얇은 고정상", "가는 칼럼", "고온 → D_s↑"],
sum="C항은 고정상 쪽(C_s)과 이동상 쪽(C_m) 물질 전달의 합. C_s는 고정상 두께 d²에 비례하고 D_s에 반비례, C_m은 칼럼 반지름 r²에 비례하고 D_m에 반비례. 얇게, 가늘게, 뜨겁게 하면 H가 줄어든다.",
tr="""<p><b>유한한 평형 시간에 의한 이론단 높이 (물질 전달 항):</b></p>
<p class="eq">H<sub>mass transfer</sub> = Cu<sub>x</sub> = (C<sub>s</sub> + C<sub>m</sub>)u<sub>x</sub></p>
<p>C<sub>s</sub>: 고정상을 통한 물질 전달 · C<sub>m</sub>: 이동상을 통한 물질 전달</p>
<p class="eq">C<sub>s</sub> = 2k / 3(k + 1)<sup>2</sup> · d<sup>2</sup>/D<sub>s</sub></p>
<p class="eq">C<sub>m</sub> = (1 + 6k + 11k<sup>2</sup>) / 24(k + 1)<sup>2</sup> · r<sup>2</sup>/D<sub>m</sub></p>
<p>k: 머무름 인자 · d: 고정상의 두께 · D<sub>s</sub>: 고정상 속 확산계수 · r: 칼럼 반지름 · D<sub>m</sub>: 이동상 속 확산계수</p>
<ul><li><b>d를 줄이면</b> 용질이 고정상에서 이동상으로 더 빨리 확산해 나올 수 있어 이론단 높이가 줄고 효율이 높아진다</li>
<li><b>r을 줄이면</b> 용질이 고정상까지 확산해 가야 하는 거리가 줄어 이론단 높이가 줄어든다</li>
<li><b>온도를 높이면</b> D<sub>s</sub>가 커져 이론단 높이가 줄어든다</li></ul>""",
ex="""<p>복잡한 분수(k에 관한 부분)는 외울 필요 없고, <y>거리<sup>2</sup> / 확산계수</y> 구조만 잡아. 확산으로 거리 ℓ을 가는 데 걸리는 시간 ∝ ℓ<sup>2</sup>/D (σ<sup>2</sup> = 2Dt에서 t = σ<sup>2</sup>/2D)니까 자연스러워.</p>
<table class="t"><tr><th>항</th><th>거리</th><th>확산계수</th><th>줄이는 법</th></tr>
<tr><td><b>C<sub>s</sub></b></td><td>고정상 두께 <b>d</b></td><td>D<sub>s</sub></td><td><g>얇은 고정상 막</g>, 온도↑(D<sub>s</sub>↑)</td></tr>
<tr><td><b>C<sub>m</sub></b></td><td>칼럼 반지름 <b>r</b> (충전 칼럼은 입자 사이 거리 ∝ 입자 지름)</td><td>D<sub>m</sub></td><td><g>가는 칼럼, 작은 입자</g></td></tr></table>
<ul><li><pk>제곱 관계</pk>: d를 절반으로 하면 C<sub>s</sub>는 1/4. r을 절반으로 해도 C<sub>m</sub>은 1/4.</li>
<li>모세관 GC 칼럼이 안지름 0.1–0.53 mm로 가늘고, 고정상 막이 0.1–5 μm로 얇은 이유가 이거야.</li>
<li>HPLC 입자를 5 → 3 → 1.7 μm로 줄여 온 이유도 같아 (C<sub>m</sub>↓).</li></ul>
<p class="note">k가 커질수록 C<sub>s</sub> 쪽 분수 2k/3(k+1)<sup>2</sup>은 k = 1에서 최대(1/6)가 됐다가 다시 작아져. 시험에선 d, r, D, 온도의 방향만 확실히.</p>"""),

# 29 (43)
dict(img=29, slide=43, title="온도를 높이면 빠르게, 분리도는 유지", sub="Finite equilibration time: effect of temperature (Figure 22-19)",
kw=["고온 → 물질 전달↑", "빠른 유속에서도 분리 유지", "30 °C 1 mL/min vs 100 °C 5 mL/min", "실리카는 60 °C 이하"],
sum="온도를 올리면 두 상 사이 물질 전달이 빨라져(C↓) 유속을 높여도 분리도가 유지된다. 30 °C·1 mL/min에서 12분 걸리던 분리가 100 °C·5 mL/min에서 1분 안에 끝난다.",
tr="""<ul><li>온도를 높이면 허용 가능한 분리도를 유지하면서 <b>길이 유속을 높일</b> 수 있다</li>
<li>고온에서 두 상 사이의 <b>물질 전달 속도가 빨라지므로</b> 분리도가 유지된다</li></ul>
<p><b>그림 22-19</b> 온도를 30 °C에서 100 °C로 올리면 분석 시간이 줄어드는 액체 크로마토그래피. 1, 우라실; 2, p-나이트로아닐린; 3, 메틸 벤조에이트; 4, 페네톨; 5, 톨루엔. 지름 4.6 mm × 길이 100 cm 칼럼에 2.1 wt% 폴리뷰타다이엔을 코팅한 4.5 μm 지르코니아(ZrO<sub>2</sub>)를 충전하고 20 vol% 아세토나이트릴 수용액으로 용리. 실리카 기반 고정상은 실리카의 가수분해를 막기 위해 보통 <b>60 °C 이하</b>로 유지한다.</p>
<p>위: <b>100 °C, 5 mL/min</b> (0–0.8 min) · 아래: <b>30 °C, 1 mL/min</b> (0–12 min) · 254 nm 흡광도</p>""",
ex="""<p>두 크로마토그램의 <y>x축 단위</y>를 꼭 봐: 위는 0–0.8 <b>분</b>, 아래는 0–12 <b>분</b>. 피크 다섯 개가 둘 다 잘 갈라져 있는데 시간은 <b>10배 이상</b> 짧아졌어.</p>
<p><b>왜 가능한가</b> (van Deemter로 설명)</p>
<ul><li>유속 5배 ↑ → 원래라면 C·u<sub>x</sub>가 5배 커져서 피크가 넓어져야 해</li>
<li>그런데 온도↑ → D<sub>s</sub>, D<sub>m</sub>↑ (그리고 이동상 점도↓) → <g>C 자체가 작아짐</g> → C·u<sub>x</sub>가 크게 늘지 않음</li>
<li>또 점도가 낮아져 역압도 줄어서 빠른 유속을 감당할 수 있어</li></ul>
<div class="box"><span class="tag">주의</span>보통 HPLC의 <b>실리카</b> 칼럼은 고온(약 60 °C 이상)에서 가수분해돼 망가져. 그래서 이 실험은 고온에 강한 <b>지르코니아(ZrO<sub>2</sub>)</b> 입자를 썼어. “온도 높이면 무조건 좋다”가 아니라 <pk>고정상이 버틸 수 있는 범위에서</pk>야.</div>
<p class="note">1번 우라실이 맨 처음 나오는 것도 확인: 역상에서 비머무름 표지(t<sub>m</sub>) 역할.</p>"""),

# 30 (44)
dict(img=30, slide=44, title="여러 흐름 경로 (A항)", sub="Multiple flow paths",
kw=["에디 확산", "경로 길이 차이", "작은 입자일수록 덜 심각", "개관 칼럼 A = 0"],
sum="충전 입자 사이로 용질 분자들이 서로 다른 길이의 경로를 지나 도착 시간이 달라지고 띠가 넓어진다. 입자가 작고 균일할수록 덜 심각하고, 입자가 없는 개관 칼럼은 A = 0.",
tr="""<p><b>여러 흐름 경로 (Multiple flow paths)</b></p>
<p>그림: 같은 위치에서 출발한 분자 1, 2, 3이 충전 입자 사이를 서로 다른 경로로 지나감. 출구에서 1은 먼저, 2는 중간, 3은 나중에 도착해 띠가 넓어짐</p>
<p><b>고정상 입자가 작을수록 이 문제는 덜 심각하다</b></p>
<p class="eq">H ≈ A + B/u<sub>x</sub> + C·u<sub>x</sub> &nbsp;(A: 여러 경로, B/u<sub>x</sub>: 세로 확산, C·u<sub>x</sub>: 평형 시간)</p>
<p>Q: 개관 칼럼에서 van Deemter 식의 A 값은 얼마인가?</p>""",
ex="""<p><b>비유</b>: 마라톤 주자들이 같은 출발선에서 같은 속도로 뛰는데, 장애물(입자) 사이로 각자 다른 골목을 지나가면 어떤 사람은 지름길, 어떤 사람은 돌아가는 길 → <y>도착 시간이 흩어져</y>.</p>
<ul><li>이걸 <b>에디 확산(eddy diffusion)</b>이라고도 해. 확산이라는 이름이지만 실제로는 “경로 길이 차이”야.</li>
<li><b>유속과 무관</b>: 경로 길이 차이는 흐름 속도와 상관없이 칼럼 구조(충전 상태)가 정하니까 그래프에서 수평선.</li>
<li><b>줄이는 법</b>: <g>작고 균일한 입자를 고르게 충전</g> → 골목 길이 차이가 작아짐</li></ul>
<div class="boxg"><b>Q 정답: A = 0</b><br>개관(open tubular) 칼럼은 속이 비어 있고 고정상이 벽에만 코팅돼 있어. 입자가 없으니 <b>여러 경로가 존재하지 않아</b> → H = B/u<sub>x</sub> + C·u<sub>x</sub> (이 식을 Golay 식이라고도 해)</div>
<div class="box"><span class="tag">족보</span>기말 복기 “Van Deemter eq for plate height, <b>multiple flow path</b>”, “<b>open tubular</b>”. A항이 무엇이고 개관 칼럼에서 왜 0인지 반드시.</div>"""),

# 31 (45)
dict(img=31, slide=45, title="개관 칼럼 vs 충전 칼럼", sub="Advantages of open tubular columns vs. packed columns (TABLE 22-3)",
kw=["낮은 압력", "빠른 유속", "A항 없음", "긴 칼럼 → N↑", "N 3290 vs 294 000"],
sum="개관 칼럼은 압력이 낮아 길게(100 m) 만들고 빠르게 흘릴 수 있으며 A항이 없다. 그래서 이론단수가 충전 칼럼의 약 90배, 분리도는 1.5 → 10.6으로 커진다.",
tr="""<p><b>충전 칼럼과 비교한 개관 칼럼의 장점</b></p>
<ul><li><b>낮은 압력</b></li>
<li>높은 길이 유속 → 세로 확산 감소 → 이론단 높이 감소 → 좁은 피크 → 높은 분리도</li>
<li>여러 경로 흐름 없음 → 이론단 높이 감소 → 좁은 피크 → 높은 분리도</li>
<li>긴 칼럼 길이 → 이론단수 증가 → 높은 분리도</li>
<li>높은 길이 유속 → 짧은 머무름시간 → 짧은 분석 시간</li></ul>
<p><b>표 22-3 충전 칼럼과 벽코팅 개관 칼럼의 성능 비교</b> (충전 / 개관)</p>
<ul><li>칼럼 길이 L: 2.4 m / <b>100 m</b> · 기체 길이 속도: 8 cm/s / 16 cm/s</li>
<li>메틸 올리에이트의 이론단 높이: 0.73 mm / 0.34 mm · 머무름 인자 k: 58.6 / 2.7</li>
<li>이론단수 N: <b>3 290 / 294 000</b> · 메틸 스테아레이트와 메틸 올리에이트의 분리도: <b>1.5 / 10.6</b></li>
<li>메틸 올리에이트의 머무름시간: 29.8 min / 38.5 min</li></ul>
<p class="note">a. 메틸 스테아레이트와 메틸 올리에이트를 180 °C에서 poly(diethylene glycol succinate) 고정상 칼럼으로 분리</p>""",
ex="""<p>지금까지 배운 걸 총정리하는 슬라이드야. 장점마다 “<y>어느 항이 줄어드나</y>”로 연결해 봐.</p>
<table class="t"><tr><th>장점</th><th>van Deemter / 식 연결</th></tr>
<tr><td>압력 낮음</td><td>입자가 없어 저항이 작음 → <b>길게(100 m)</b>, 빠르게 가능</td></tr>
<tr><td>빠른 유속</td><td><b>B/u<sub>x</sub>↓</b> (GC는 B항이 큼!)</td></tr>
<tr><td>여러 경로 없음</td><td><b>A = 0</b></td></tr>
<tr><td>긴 칼럼</td><td>N = L/H↑ → R ∝ √N↑</td></tr></table>
<p><b>표 검산</b></p>
<ul><li>N = L/H: 충전 2400 mm / 0.73 = <b>3 290</b> ✓ · 개관 100 000 mm / 0.34 = <b>294 000</b> ✓</li>
<li>N 비 = 294 000 / 3 290 ≈ <b>89배</b> → √89 ≈ 9.5배인데 실제 R 비는 10.6/1.5 ≈ 7배. 두 칼럼의 k와 선택성 조건이 달라서 √N 비만큼 정확히 커지진 않지만 경향은 같아.</li>
<li>칼럼이 40배 긴데 머무름시간은 29.8 → 38.5분으로 비슷: 유속이 2배이고 k가 훨씬 작아서(58.6 → 2.7, 고정상 막이 얇음).</li></ul>
<div class="boxg">그래서 현대 <b>GC는 거의 다 모세관(개관) 칼럼</b>이야. 반면 LC는 D<sub>m</sub>이 작아 가는 관 벽까지 확산이 너무 느려서(C<sub>m</sub> ∝ r<sup>2</sup>/D<sub>m</sub>) 충전 칼럼을 써.</div>"""),
]
