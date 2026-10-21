from parts import *
P = P6
E = [
dict(t="c", id="c-integ", part=P, title="신호의 세기 — 적분값 = 수소 개수의 비", sub="Signal intensity & integration",
core="피크 아래 <b>면적(적분값)</b>은 그 신호를 내는 화학적으로 동등한 <b>수소 수에 비례</b>. 적분비 = 수소 수의 비.",
detail="""<ul><li>스펙트럼 위의 계단 모양 선(적분 곡선) = 컴퓨터가 계산한 각 피크 아래 면적. 계단 높이의 비 = H 수의 비</li>
<li>히드록시아세톤(CH₃COCH₂OH): δ 4.3 (2H, CH₂) : 3.3 (1H, OH) : 2.2 (3H, CH₃) → <g>2 : 1 : 3</g></li>
<li>주의: <b>높이가 아니라 면적</b>. 갈라진 피크(삼중선 등)는 키가 작아 보여도 조각 면적을 합하면 H 수에 비례</li>
<li>적분은 ‘비’만 준다 → 실제 개수는 분자식의 총 H 수로 환산</li></ul>
<div class="term">＊[용어: 적분(integration) = 그래프 아래 넓이를 구하는 것. 여기선 “그 봉우리를 만드는 수소가 몇 개 몫인가”]</div>
<p><b>NMR 스펙트럼에서 얻는 정보 4가지</b>: ① 신호 개수 = 화학적으로 다른 H 종류 수 ② δ 위치 = 전자 환경 ③ 적분 = H 개수 비 ④ 갈라짐 = 이웃 H 개수 (다음 개념).</p>""",
example="""<b>예</b> 분자식 C₄H₈O₂, 신호 3개의 적분 높이 6 mm : 4 mm : 6 mm<br>
<b>Step 1</b> 가장 작은 값으로 나누기: 1.5 : 1 : 1.5 → 정수로 ×2 → 3 : 2 : 3<br>
<b>Step 2</b> 합 = 8 = 분자식 H 수 8 ✓ → 3H, 2H, 3H (예: 에틸 아세테이트 CH₃CO–, –OCH₂–, –CH₃)""",
side=[("img", "L4-12", "원본 슬라이드 12 — 히드록시아세톤 적분 2H : 1H : 3H", 230),
      ("ana", "적분 = <b>투표함 무게</b>. 봉우리마다 표(수소)가 몇 장 들었는지 무게로 재는 것. 표가 여러 칸(갈라진 피크)에 나뉘어 있어도 다 합쳐서 잰다.")],
one="적분비 = 수소 개수비. 높이 말고 면적! 총 H 수로 환산."),

dict(t="c", id="c-n1", part=P, title="스핀-스핀 짝지음 — n+1 법칙과 파스칼 삼각형", sub="Spin-spin coupling · n+1 rule · Pascal's triangle",
core="이웃 탄소에 화학적으로 다른 H가 <b>n개</b>면 내 신호는 <b>n+1개</b>로 갈라지고, 높이 비는 <b>파스칼 삼각형</b>을 따른다.",
detail="""<p>서로 인접한 탄소의 수소(또는 같은 탄소에 있지만 환경이 다른 수소)는 짝지음으로 서로에게 영향 → 피크가 갈라짐(spin splitting).</p>
<p><b>왜 갈라지나 — 확률 문제</b>: 이웃 H 하나는 ↑(+1/2) 또는 ↓(−1/2) 반반 → 내 핵이 느끼는 자기장이 살짝 커지거나 작아짐 → 2개 피크(1 : 1). 이웃 H 2개면 ↑↑ / ↑↓·↓↑ / ↓↓ → 3개(1 : 2 : 1). 3개면 1 : 3 : 3 : 1.</p>
<table class="t"><tr><th>n(이웃 H)</th><th>피크 수</th><th>강도비</th><th>이름</th></tr>
<tr><td>0</td><td>1</td><td>1</td><td>단일선 singlet (s)</td></tr>
<tr><td>1</td><td>2</td><td>1 1</td><td>이중선 doublet (d)</td></tr>
<tr><td>2</td><td>3</td><td>1 2 1</td><td>삼중선 triplet (t)</td></tr>
<tr><td>3</td><td>4</td><td>1 3 3 1</td><td>사중선 quartet (q)</td></tr>
<tr><td>4</td><td>5</td><td>1 4 6 4 1</td><td>오중선 pentet</td></tr>
<tr><td>6</td><td>7</td><td>1 6 15 20 15 6 1</td><td>칠중선 septet</td></tr></table>
<p><b>에탄올 CH₃CH₂OH</b>: CH₃는 이웃 CH₂(2H) → 2+1 = <b>삼중선</b>, CH₂는 이웃 CH₃(3H) → 3+1 = <b>사중선</b>.</p>
<p><b>주의</b>: 화학적으로 동등한 수소끼리는 서로 갈라지지 않는다(예: trans-2-뷰텐의 두 =CH).</p>""",
side=[("img", "L4-14", "원본 슬라이드 14 — 이웃 스핀 조합과 파스칼 삼각형", 200),
      ("ana", "이웃 H = <b>동전</b>. 동전 2개를 던지면 앞앞(1)·앞뒤/뒤앞(2)·뒤뒤(1) → 1 : 2 : 1. 피크 높이 = 그 조합이 나올 확률!"),
      ("tip", "🎯 녹음: “n+1 원칙인 이유, 피크 비율이 파스칼 삼각형인 이유 — 확률 때문”. 이웃 H 수를 알려 주는 게 짝지음의 가치.")],
one="이웃 H n개 → n+1개 봉우리, 높이 = 파스칼(동전 던지기 확률)."),

dict(t="c", id="c-j", part=P, title="짝지음 상수 J (Hz) — 누가 누구의 이웃인지 알려 주는 간격", sub="Coupling constant J · ¹J, ²J (geminal), ³J (vicinal)",
core="갈라진 피크 사이 간격 = J(Hz). 서로 짝짓는 두 신호는 <b>같은 J</b>를 공유한다. 해석에서 중요한 건 <b>³J(이웃자리, H–C–C–H)</b>, 보통 5–15 Hz.",
detail="""<ul><li>짝짓는 핵 사이 결합 수가 n이면 ⁿJ: <b>¹J</b> 직접(H–H) / <b>²J</b> 같은자리(geminal, H–C–H) / <b>³J</b> 이웃자리(vicinal, H–C–C–H) / &gt;³J 원거리</li>
<li>J는 <b>Hz로만</b> 표시, ³J는 보통 <b>5–15 Hz</b></li>
<li>서로 짝짓는 두 핵은 서로 같은 정도로 영향 → <y>두 신호의 갈라짐 간격(J)이 같다</y> → 짝 찾기의 열쇠</li></ul>
<div class="term">＊[용어: geminal(제미널, 원문 ‘germinal’은 오타) = 쌍둥이처럼 같은 탄소에 붙은 두 H / vicinal(비시널) = 이웃 탄소에 붙은 H]</div>
<p>🎯 녹음: 같은 탄소의 두 H는 대부분 화학적으로 동등해서 <b>geminal 짝지음은 “없다고 가정”</b> — “시험 문제 그런 거 안 나와”. <b>이웃자리(³J) 짝지음만 해석 잘하면 된다.</b></p>
<p><b>데이터 읽기</b>: “4.04 (t, J = 5.4 Hz, 2H)” = δ(다중도, J, H 수). 프로필 아세테이트(CH₃COOCH₂CH₂CH₃, 270 MHz):</p>
<table class="t"><tr><th>신호</th><th>δ</th><th>모양</th><th>정체</th></tr>
<tr><td>A</td><td>2.04</td><td>s, 3H</td><td>CH₃–C(=O) (이웃 H 없음)</td></tr>
<tr><td>D</td><td>4.04</td><td>t, 2H</td><td>–O–CH₂– (O 옆이라 왼쪽)</td></tr>
<tr><td>C</td><td>1.63–1.53</td><td>m, 2H</td><td>–CH₂– (이웃 2+3 = 5H → 다중선, triplet of quartet)</td></tr>
<tr><td>B</td><td>0.89</td><td>t, 3H</td><td>–CH₃</td></tr></table>""",
formula="""<span class="fx">J(Hz) = 갈라진 피크 간격(ppm) × ν₀(MHz)</span> &nbsp; 예) D의 바깥 두 피크 4.06 − 4.02 = 0.04 ppm = 2J → J = 0.02 × 270 = <b>5.4 Hz</b>""",
side=[("img", "L4-15", "원본 슬라이드 15 — 짝지음 상수와 프로필 아세테이트", 200),
      ("ana", "J = <b>짝꿍끼리 맞춘 커플링 반지 크기</b>. 같은 반지(같은 J)를 낀 두 신호가 서로 이웃이다."),
      ("trap", "삼중선의 <b>바깥 간격은 2J</b>(J가 두 번). 이웃한 두 줄 간격이 J.")],
one="J = 갈라짐 간격(Hz). 짝꿍은 같은 J. 해석은 ³J(이웃자리)만!"),

dict(t="c", id="c-field", part=P, title="자기장 세기와 스펙트럼 모양 — δ는 그대로, J는 Hz로 고정", sub="High field vs low field · J(ppm) = J(Hz)/ν₀(MHz)",
core="고자장 기기에서도 신호 <b>중심 위치(δ, ppm)는 같다</b>. J(Hz)는 자기장과 무관하게 고정이라 ppm 축에서는 <b>갈라짐 폭이 좁아져</b> 신호가 깔끔하게 분리된다.",
detail="""<p><span class="fx">J(ppm) = J(Hz) / ν₀(MHz)</span></p>
<ul><li>화학적 이동은 자기장 크기와 무관한 <b>차폐상수 차이</b> → 100 MHz든 600 MHz든 신호 중심 δ 일치</li>
<li>짝지음 상수는 자기장에 의존하지 않고 Hz로 정의 → 같은 J(예: 7 Hz)라도 100 MHz에선 0.07 ppm, 600 MHz에선 0.0117 ppm → <y>고자장일수록 다중선이 좁아 보임</y></li>
<li>그래서 저자장(60 MHz)에서 겹쳐 뭉개진 다중선이 고자장(300 MHz)에선 깨끗하게 분리 → 고자장 NMR의 장점(감도↑ + 분해↑)</li></ul>
<p><b>이소부틸 클로라이드 ((CH₃)₂CHCH₂Cl)</b>: a = 2×CH₃(6H, 이웃 CH 1개 → doublet), b = CH(이웃 6+2 = 8H → triplet of septet, 다중선), c = CH₂Cl(이웃 CH 1개 → doublet). 100 MHz(2.35 T) vs 600 MHz(14.1 T)에서 위치는 같고 갈라짐 폭만 좁아짐.</p>""",
side=[("img", "L4-17", "원본 슬라이드 17 — 100 MHz vs 600 MHz 스펙트럼", 210),
      ("ana", "<b>같은 사진을 더 큰 화면에 띄운 것</b>. 건물 위치(δ, %)는 그대로인데, 실제 길이가 고정된 물건(J, Hz)은 화면 비율상 작아 보여 서로 덜 겹친다.")],
one="고자장: δ 그대로, J(Hz) 그대로 → ppm 간격은 좁아져 다중선이 깔끔."),

dict(t="c", id="c-ft", part=P, title="NMR 분광기 — CW-NMR에서 펄스 푸리에변환(FT) NMR로", sub="Continuous Wave NMR · Pulse Fourier Transform NMR · FID · signal averaging",
core="FT-NMR = ① <b>RF 펄스</b>로 모든 핵을 한꺼번에 들뜨게 → ② 세차운동이 줄어드는 신호 <b>FID</b>(시간 함수)를 수신 → ③ <b>푸리에 변환</b>으로 진동수 스펙트럼.",
detail="""<p><b>CW-NMR(Continuous Wave, 연속파)</b>: 자석 양극 사이 시료(균일도 보정 코일, <b>압축공기로 시료관 고속 회전</b>해 불균일 상쇄). 라디오파를 일정 속도로 주사하다가 공명 순간 수신기(안테나)가 검출. 실제로는 <b>RF 주파수를 고정하고 자기장 세기를 변화</b>. 영구자석 최대 ~1.4 T → 1970년대까지 60 MHz. 현재는 <b>초전도자석</b>으로 최대 28.2 T(1.2 GHz).</p>
<p><b>FT-NMR(Pulse Fourier Transform, 펄스 푸리에변환)</b></p>
<ol><li>강한 <b>라디오 충격파(RF pulse)</b>를 주기적으로 → 모든 핵을 동시에 들뜨게</li>
<li>각 핵이 자기 고유진동수로 세차운동 → 수신기가 궤적(유도 교류전류)을 채취. 진폭은 <b>완화(relaxation)</b>로 점점 감소 → <b>FID(Free Induction Decay, 자유유도감쇠)</b> = 시간 스펙트럼(time domain)</li>
<li>FID엔 모든 핵의 공명 진동수 정보가 있지만 눈으로는 식별 불가 → <b>FT(Fourier Transform, 푸리에 변환)</b>로 진동수 스펙트럼(frequency domain)</li></ol>
<div class="term">＊[용어: 푸리에 변환 = 여러 음이 섞인 소리(시간에 따른 파형)를 “어떤 음높이가 얼마나 섞였나”(진동수별 세기)로 풀어 주는 수학 연산]</div>
<p><b>FT의 장점</b>: FID를 디지털로 저장·재처리(해상도↑ 또는 감도↑) / <y>여러 번 반복해 누적(signal averaging)</y> → 신호는 쌓이고 무질서한 잡음은 상쇄 → 감도↑, 측정 시간 단축(한 번에 전 영역).</p>""",
side=[("img", "L4-21", "원본 슬라이드 21 — RF 펄스 → FID → FT", 200),
      ("ana", "CW = <b>피아노 건반을 하나씩 눌러 보며</b> 어느 음에서 울리나 찾기. FT = <b>종을 한 번 ‘땡’ 치고</b> 울림(FID)을 녹음한 뒤, 컴퓨터로 어떤 음들이 섞였는지 분해."),
      ("tip", "<span class=\"tag j\">족보</span> “FT NMR 분석 순서” 주관식. 녹음: “크게 보면 세 단계 — <b>펄스를 주고, FID를 얻고, 푸리에 변환을 하면 NMR 스펙트럼</b>”. + signal averaging 장점.")],
one="펄스 → FID(시간 함수, 감쇠) → 푸리에 변환(진동수 함수). 반복 누적 = 잡음 상쇄 = 감도↑."),

dict(t="c", id="c-13c", part=P, title="¹³C-NMR — 탄소 골격을 보는 NMR", sub="Carbon-13 NMR · broadband decoupling",
core="¹³C도 I = 1/2라 NMR 가능하지만 γ가 ¹H의 1/4, 존재비 1.1 % → 감도 1.6 %(오래 걸림). δ 범위가 넓고(0–220 ppm), <b>광폭 짝풀림</b>으로 모든 신호가 단일선.",
detail="""<table class="t"><tr><th></th><th>¹H</th><th>¹³C</th></tr>
<tr><td>γ (×10⁶ rad/T·s)</td><td>267.53</td><td>67.28 (≈1/4)</td></tr>
<tr><td>자연 존재비</td><td>99.98 %</td><td><b>1.11 %</b></td></tr>
<tr><td>상대 감도</td><td>100 %</td><td><b>1.6 %</b></td></tr>
<tr><td>δ 범위</td><td>0–12 ppm</td><td><b>0–220 ppm</b></td></tr></table>
<ul><li>왜 δ 범위가 넓나? 전자가 6개인 ¹³C는 전자 1개인 ¹H보다 차폐 차이가 커서. 해석 순서는 ¹H와 비슷(TMS = 0, C=O가 가장 왼쪽)</li>
<li>¹³C–¹³C 짝지음: ¹³C가 1 %뿐 → 이웃이 둘 다 ¹³C일 확률 0.01 % → 무시</li>
<li>¹³C–¹H 짝지음은 실제로 있음(J 0–300 Hz) → 갈라지면 원래 약한 신호가 더 약해지고 복잡 → <b>광폭 짝풀림(broadband decoupling)</b>으로 제거 = <y>양성자 짝풀림 스펙트럼</y> → 화학적으로 다른 탄소마다 <b>단일선 하나</b></li>
<li>신호 세기(적분)는 탄소 수 비율과 다르지만 대략 <b>CH₃ &gt; CH₂ &gt; CH ≫ C(4차)</b></li></ul>
<div class="term">＊[용어: 짝풀림(decoupling) = ¹H 전체에 라디오파를 계속 쪼여 ¹H 스핀을 빠르게 뒤섞어서, ¹³C가 이웃 ¹H의 영향을 평균(0)으로 느끼게 만드는 기술]</div>
<p>🎯 녹음: 600 MHz면 ¹³C는 정확히 1/4인 150 MHz. 같은 스펙트럼을 얻는 데 ¹H보다 약 50배 이상 오래 걸리지만, 탄소 정보가 중요해서 찍는다. <b>“시험 범위는 여기까지”</b>(¹³C-NMR까지).</p>""",
side=[("img", "L4-24", "원본 슬라이드 24 — 벤질 프로피오네이트 ¹H vs ¹³C", 200),
      ("ana", "¹³C-NMR = <b>100명 중 1명만 말하는 사람</b>(1.1 %), 목소리도 작음(γ 1/4) → 오래 귀 기울여야(누적) 들린다. 대신 말하는 음역(0–220 ppm)이 넓어 서로 안 겹침.")],
one="¹³C: γ 1/4 · 1.1 % · 감도 1.6 % · 0–220 ppm · 짝풀림 → 전부 단일선 · CH₃>CH₂>CH≫C."),

dict(t="c", id="c-2d", part=P, title="2차원 NMR과 약전 확인시험 — 세프디토렌피복실", sub="2D NMR (COSY, HSQC/HMQC, HMBC, NOESY) · Cefditoren pivoxil identification",
core="2D NMR은 두 축 모두 진동수(δ)로 그려 ‘어떤 핵끼리 연결돼 있나’를 한눈에 보여 준다. 약전은 ¹H-NMR의 <b>δ·다중도·면적강도비</b>로 의약품을 확인한다.",
detail="""<p><b>2D NMR 종류(이름만)</b>: 결합을 통한 같은 핵 상관 — <b>COSY</b>(¹H–¹H), TOCSY, INADEQUATE / 다른 핵 상관 — <b>HSQC·HMQC</b>(¹H–¹³C 직접 결합), <b>HMBC</b>(먼 결합) / 공간을 통한 상관 — <b>NOESY</b>, ROESY.</p>
<div class="term">＊[용어: COSY = COrrelation SpectroscopY(상관 분광법), HSQC = Heteronuclear Single Quantum Coherence, HMQC = Heteronuclear Multiple Quantum Coherence, HMBC = Heteronuclear Multiple Bond Correlation, NOESY = Nuclear Overhauser Effect SpectroscopY]</div>
<p><b>세프디토렌피복실 확인시험</b>: 핵자기공명스펙트럼측정용 중수소화클로로포름(CDCl₃) 용액(1 → 50), 내부기준 TMS, ¹H 측정 →</p>
<table class="t"><tr><th>신호</th><th>δ (ppm)</th><th>모양</th><th>면적비</th><th>정체(추정)</th></tr>
<tr><td>A</td><td>1.1</td><td>단일선</td><td>9</td><td>피발로일 C(CH₃)₃ (t-뷰틸)</td></tr>
<tr><td>B</td><td>2.4</td><td>단일선</td><td>3</td><td>싸이아졸 고리의 CH₃</td></tr>
<tr><td>C</td><td>4.0</td><td>단일선</td><td>3</td><td>메톡시이미노 =N–OCH₃</td></tr>
<tr><td>D · E</td><td>6.4 · 6.7</td><td>이중선 · 이중선</td><td>1 · 1</td><td>서로 짝짓는 비닐 CH=CH (cis)</td></tr>
<tr><td>F</td><td>8.6</td><td>단일선</td><td>1</td><td>싸이아졸 고리 C–H (N·S 사이, 탈차폐)</td></tr></table>
<p>면적강도비 A : B : C : D : E : F ≈ <g>9 : 3 : 3 : 1 : 1 : 1</g>.</p>
<div class="term">＊[용어: 중수소화 클로로포름(CDCl₃) = H를 D로 바꾼 용매. 용매의 H가 신호를 덮지 않게 하려고 사용]</div>""",
side=[("img", "L4-27", "원본 슬라이드 27 — 세프디토렌피복실 ¹H-NMR 확인시험", 230),
      ("ana", "D와 E가 둘 다 이중선 = <b>서로 손잡은 단 둘</b>(이웃이 서로 1개씩). 단일선 A·B·C·F는 이웃 H가 없는 ‘혼자 서 있는’ 그룹.")],
one="약전 ¹H-NMR 확인 = δ + 다중도 + 면적비(9:3:3:1:1:1). 이중선 둘 = 서로 짝."),

# ---------- problems (second half)
dict(t="q", id="q-split", part=P, kind=["bl", "sa"], title="신호 개수 · 갈라짐 · 적분 예측 (이웃자리 짝지음만)", src=" 족보(spin-spin coupling) · 교재 예제 1-15·1-16",
q="""(1) 화학적으로 동등한 수소의 종류 수: 다이에틸 에터 <span class="blank">(가)</span>, 톨루엔 <span class="blank">(나)</span>, p-자일렌 <span class="blank">(다)</span>, 사이클로헥사논 <span class="blank">(라)</span><br>
(2) 메틸 프로파노에이트 CH₃CH₂CO₂CH₃의 ¹H-NMR을 예측하시오 (δ가 큰 순서, 다중도, 적분).<br>
(3) 아이소뷰테인 (CH₃)₃CH의 신호: CH₃ = <span class="blank">(마)</span>선(9H), CH = <span class="blank">(바)</span>개로 갈라짐(1H)<br>
(4) trans-2-뷰텐 CH₃CH=CHCH₃: =CH 신호는 <span class="blank">(사)</span>선. 두 =CH가 서로 갈라지지 않는 이유는?""",
a="(가) 2 (나) 4 (다) 2 (라) 3 / (2) OCH₃ ~3.7 s 3H > CH₂ ~2.3 q 2H > CH₃ ~1.1 t 3H / (마) 이중 (바) 10 / (사) 사중 — 두 =CH는 화학적으로 동등해서 서로 짝지음이 관찰되지 않음",
steps=[("다이에틸 에터: CH₃, CH₂ → 2 / 톨루엔: CH₃ + 고리 H 3종(ortho·meta·para) → 4 / p-자일렌: CH₃, 고리 H → 2 / 사이클로헥사논: C=O 기준 α·β·γ → 3", "대칭으로 겹쳐지는 H는 같은 종류."),
       ("메틸 프로파노에이트: –OCH₃(O 옆, 이웃 H 없음) → 단일선 3H, 가장 왼쪽 / –CH₂–(C=O 옆, 이웃 CH₃ 3H) → 사중선 2H / –CH₃(이웃 CH₂ 2H) → 삼중선 3H", "δ: O에 붙은 C–H(3–4) > C=O 옆(2–3) > 알킬(0–2)."),
       ("아이소뷰테인: CH₃ 9H는 이웃 CH 1개 → 이중선 / CH는 이웃 9H → 9+1 = 10개", "적분 9 : 1."),
       ("trans-2-뷰텐: =CH 이웃 = CH₃ 3H → 사중선(6H 이중선 + 2H 사중선)", "동등한 H끼리는 갈라짐이 안 보인다(n에 넣지 않음).")],
one="신호 수 = 환경 종류, 갈라짐 = 이웃 H + 1, 적분 = 개수. 동등한 H끼리는 안 갈라진다."),

dict(t="q", id="q-j", part=P, kind=["calc", "bl"], title="짝지음 상수 J 계산 · 고자장 효과", src=" 족보(짝지음 상수 계산) · 슬라이드 15·17·18",
q="""(1) 270 MHz ¹H-NMR에서 –OCH₂– 삼중선의 세 줄이 4.06, 4.04, 4.02 ppm이다. J = <span class="blank">(가)</span> Hz<br>
(2) 300 MHz에서 어떤 이중선이 1.240 ppm과 1.220 ppm에 나왔다. J = <span class="blank">(나)</span> Hz. 같은 시료를 600 MHz에서 재면 두 줄 간격은 <span class="blank">(다)</span> ppm, J는 <span class="blank">(라)</span> Hz, 중심 δ는 <span class="blank">(마)</span> ppm<br>
(3) 서로 짝짓는 두 신호를 스펙트럼에서 찾는 방법을 한 줄로 쓰시오.<br>
(4) O/X: 짝지음 상수(Hz)는 외부 자기장 세기가 커지면 비례해 커진다. ( )""",
a="(가) 5.4 (나) 6.0 (다) 0.010 (라) 6.0 (마) 1.230 / (3) 갈라진 간격 J(Hz)가 같은 두 신호를 찾는다 / (4) X",
steps=[("이웃한 두 줄 간격 = 0.02 ppm → J = 0.02 × 270 = 5.4 Hz", "ppm × MHz = Hz. 바깥 두 줄 간격 0.04 ppm은 2J."),
       ("0.020 ppm × 300 = 6.0 Hz", ""),
       ("600 MHz: J는 Hz로 고정 → 6.0/600 = 0.010 ppm, 중심 δ = 1.230 그대로", "J(ppm) = J(Hz)/ν₀(MHz)."),
       ("짝꿍은 서로에게 같은 정도로 영향 → 같은 J", ""),
       ("J(Hz)는 자기장과 무관 → X", "")],
one="J(Hz) = 간격(ppm) × MHz. 자석이 바뀌어도 J(Hz)·δ는 그대로, ppm 간격만 바뀐다."),

dict(t="q", id="q-ft", part=P, kind=["sa"], title="FT-NMR의 측정 순서와 장점", src=" 족보(FT NMR 분석순서 주관식) · 슬라이드 20–22",
q="""펄스 푸리에변환 NMR(FT-NMR) 분광기로 ¹H-NMR 스펙트럼을 얻는 과정을 순서대로 서술하고, 고전적인 CW-NMR에 비해 시료가 아주 적을 때 유리한 이유를 쓰시오.""",
a="① 초전도 자석의 강한 자기장 안에 시료를 넣는다 ② 강한 RF 펄스를 쪼여 모든 핵을 동시에 들뜨게 한다 ③ 각 핵이 고유진동수로 세차운동하며 만드는 유도 교류전류가 완화로 감쇠하는 FID(시간 함수)를 수신기로 얻는다 ④ FID를 푸리에 변환해 진동수 스펙트럼으로 바꾸고 TMS 기준 δ(ppm)로 표시한다. 장점: FID를 디지털로 저장해 여러 번 반복 측정·누적(signal averaging)하면 신호는 커지고 무질서한 잡음은 상쇄되어 감도가 증가하고, 한 번에 전 영역을 측정해 시간이 짧다.",
steps=[("펄스(RF pulse): 모든 핵을 한꺼번에 들뜨게", "CW처럼 진동수를 하나씩 훑지 않는다."),
       ("FID(Free Induction Decay, 자유유도감쇠) 수신: 세차운동 신호가 완화로 점점 줄어드는 시간 함수", "모든 핵의 진동수가 섞여 있어 눈으로는 해석 불가."),
       ("FT(Fourier Transform, 푸리에 변환): 시간 함수 → 진동수 함수 = NMR 스펙트럼", ""),
       ("장점: 저장·재처리 가능, <b>signal averaging</b>으로 S/N(신호대잡음비)↑, 측정 시간↓", "녹음: “시료가 적어 신호가 거의 안 나오면 밤새 FID를 반복해 평균 낸다.”")],
extra='<div class="card tip"><div class="ct">🔑 채점 핵심어</div>RF 펄스 · 세차운동 · FID(시간 함수, 완화로 감쇠) · 푸리에 변환 · 진동수 함수 · 반복 누적(signal averaging) · 잡음 상쇄 · 감도↑</div>',
one="펄스 → FID → 푸리에 변환. 반복 누적으로 잡음은 지워지고 신호는 쌓인다."),

dict(t="q", id="q-13c", part=P, kind=["tf"], title="¹³C-NMR · NMR 분광기 O/X", src=" 슬라이드 20·23–25",
q="""O 또는 X를 표시하시오.<br>
(1) ¹³C의 핵자기회전비는 ¹H의 약 1/4이므로 600 MHz NMR에서 ¹³C는 약 150 MHz에서 측정한다. ( )<br>
(2) ¹³C의 자연 존재비는 약 1.1 %이고 상대 감도는 ¹H의 약 1.6 %이다. ( )<br>
(3) ¹³C의 화학적 이동 범위(0–220 ppm)가 ¹H보다 넓은 것은 ¹³C 주변 전자가 더 많아 차폐 차이가 크기 때문이다. ( )<br>
(4) 일반적인 ¹³C 스펙트럼에서 ¹³C–¹³C 짝지음 때문에 모든 신호가 이중선으로 갈라진다. ( )<br>
(5) 광폭 짝풀림으로 ¹³C–¹H 짝지음을 제거하면 각 탄소가 단일선으로 나온다. ( )<br>
(6) ¹³C 스펙트럼의 적분비는 탄소 수의 비와 정확히 같다. ( )<br>
(7) CW-NMR은 실제로 RF 주파수를 고정하고 자기장 세기를 변화시키며 측정하였다. ( )""",
a="(1) O (2) O (3) O (4) X (5) O (6) X (7) O",
steps=[("(1) 67.28/267.53 ≈ 1/4 → 600/4 = 150 MHz ✓", ""),
       ("(2) 슬라이드 23 수치 ✓", ""),
       ("(3) 전자 6개 vs 1개 → 차폐 차이 큼 ✓", ""),
       ("(4) ¹³C–¹³C가 이웃할 확률 0.01 % → 무시 ✗", ""),
       ("(5) 양성자 짝풀림 스펙트럼 ✓", ""),
       ("(6) 탄소 비율과 다름, 대략 CH₃ &gt; CH₂ &gt; CH ≫ C ✗", "4차 탄소(H 없음)는 특히 약하다."),
       ("(7) ✓ 슬라이드 20", "")],
one="¹³C: 1/4 · 1.1 % · 1.6 % · 0–220 ppm · ¹³C–¹³C 무시 · 짝풀림=단일선 · 적분≠탄소 수."),

dict(t="q", id="q-cef", part=P, kind=["sa", "bl"], title="¹H-NMR에서 대응하는 수소 찾기 (세프디토렌피복실)", src=" 족보(H-NMR에서 대응하는 수소 찾기) · 슬라이드 27",
q="""세프디토렌피복실의 ¹H-NMR(CDCl₃, TMS): δ 1.1(단일선, A), 2.4(단일선, B), 4.0(단일선, C), 6.4(이중선, D), 6.7(이중선, E), 8.6(단일선, F), 면적강도비 A : B : C : D : E : F ≈ 9 : 3 : 3 : 1 : 1 : 1.<br>
분자 안의 부분 구조: ① 싸이아졸 고리의 CH₃ ② 피발로일기 –C(CH₃)₃ ③ 메톡시이미노 =N–OCH₃ ④ 서로 이웃한 비닐 H 두 개 –CH=CH– ⑤ N과 S 사이의 싸이아졸 고리 C–H<br><br>
A = <span class="blank">(가)</span>, B = <span class="blank">(나)</span>, C = <span class="blank">(다)</span>, D·E = <span class="blank">(라)</span>, F = <span class="blank">(마)</span><br>
D와 E가 서로 짝짓는 사이임을 확인하는 방법: <span class="blank">(바)</span>""",
a="(가) ② (나) ① (다) ③ (라) ④ (마) ⑤ / (바) D와 E의 이중선 간격(J, Hz)이 같은지 확인",
steps=[("면적 9 = 같은 H 9개 → t-뷰틸 C(CH₃)₃ → A(1.1, 알킬 영역, 이웃 H 없음 → 단일선)", "적분부터 보면 9H는 하나뿐."),
       ("3H 단일선 두 개: O에 붙은 CH₃(전기음성 O 옆 → 3–4 ppm) = C(4.0) / 고리에 붙은 CH₃(2–3 ppm) = B(2.4)", "δ로 O 옆인지 구별."),
       ("1H 이중선 두 개 = 서로를 1개씩 이웃으로 갖는 –CH=CH– → D, E (알켄 영역 5–7 ppm)", "n = 1 → 이중선. 같은 J를 공유."),
       ("1H 단일선 8.6 ppm = N·S 사이 방향족 고리 C–H (이웃 H 없음, 강한 탈차폐)", "")],
one="적분으로 개수 → δ로 환경 → 다중도로 이웃 → J로 짝 확인."),
]
