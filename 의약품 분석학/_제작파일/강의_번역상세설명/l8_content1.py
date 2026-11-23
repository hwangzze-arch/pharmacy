PAGES = [
# 1 표지
dict(img=1, slide=1, src="표지", title="강의 표지 · 이번 강의 로드맵", sub="의약품분석학 II — Lecture 8 (제2장 분리분석법 · 2.5 고성능액체크로마토그래피)",
kw=["HPLC", "작은 입자·고압", "실리카·결합상·엔드캡", "순상 vs 역상", "등용매 vs 기울기 용리", "HPLC 검출기"],
sum="학기 마지막 기법 HPLC. 왜 LC는 충전 칼럼에 아주 작은 입자를 쓰고 고압이 필요한지 → 고정상(실리카, C18, 엔드캡) → 용리(순상·역상, 등용매·기울기) → 펌프와 검출기 순서야.",
tr="""<p><b>의약품분석학 II — 강의 8</b></p>
<p>의약품기기분석학<br>제2장. 분리분석법<br>&nbsp;&nbsp;2.5 고성능액체크로마토그래피</p>
<p class="note">※ 원본 슬라이드 번호가 건너뛰어(19, 31, 34–37, 43, 46–48). 강의자료에서 빠진 슬라이드라 이 노트에는 원본 번호를 그대로 적었어.</p>""",
ex="""<table class="t"><tr><th>파트</th><th>한 줄 핵심</th><th>꼭 챙길 것</th></tr>
<tr><td><b>① LC·HPLC 개요</b> (2–5)</td><td>이동상 액체, 고압, 충전 칼럼</td><td><pk>왜 LC는 개관 칼럼을 못 쓰나?</pk></td></tr>
<tr><td><b>② 작은 입자·고압</b> (6–10)</td><td>입자↓ → A·C항↓ → N↑, 압력↑</td><td>N ≈ 3000L/d<sub>p</sub>, P ∝ 1/d<sub>p</sub><sup>2</sup>, UHPLC</td></tr>
<tr><td><b>③ 칼럼·고정상</b> (11–18)</td><td>가드 칼럼, 가열, 실리카, 실라놀, 결합상, 엔드캡</td><td><pk>pH 2–8, tailing 원인과 해결</pk></td></tr>
<tr><td><b>④ 용리</b> (20–32)</td><td>용리 세기, 순상/역상, 등용매/기울기</td><td><pk>역상에서 B% 바꾸면?</pk></td></tr>
<tr><td><b>⑤ 펌프·검출기</b> (33–50)</td><td>이중 피스톤 펌프, UV·PDA·FLD·ELSD·ECD·RI</td><td>검출기별 특징, 기울기 용리 가능 여부</td></tr></table>
<p>연결고리: Lecture 6 van Deemter(<g>입자 작게 → A·C항↓</g>)와 tailing(실라놀), Lecture 7 GC(개관 칼럼·검출기)와 비교하면서 보면 쉬워.</p>
<div class="box"><span class="tag">족보</span>기말 복기: “<b>Column: 4.6 × 250 mm Hypersil ODS column (C18 on 5 μm silica)!</b>” (24번 슬라이드 Q), <b>guard column</b>·protecting, sample injection, 2025-2 주관식 <b>HPLC tailing 막는 법</b>, <b>반딤터로 입자 작은 칼럼 장단점</b>, 검출기를 언제 쓰나.</div>"""),

# 2
dict(img=2, slide=2, title="액체크로마토그래피란", sub="Liquid chromatography: mobile phase, stationary phase, analyte",
kw=["이동상 = 액체", "고정상 = 고체(흡착)·액체(분배)", "분석물 = 용액"],
sum="LC는 이동상이 액체. 고정상은 고체(흡착) 또는 액체(분배)이고, 분석물은 용액 상태면 돼서 휘발성이 필요 없어.",
tr="""<p><b>액체크로마토그래피 (Liquid chromatography)</b></p>
<ul><li><b>이동상</b>: 액체</li>
<li><b>고정상</b>: 고체(<b>흡착</b>) 또는 액체(<b>분배</b>)</li>
<li><b>분석물</b>: <b>용액</b></li></ul>""",
ex="""<p>Lecture 7 GC 슬라이드와 같은 틀로 비교해 봐.</p>
<table class="t"><tr><th></th><th>GC</th><th>LC (HPLC)</th></tr>
<tr><td>이동상</td><td>기체 (운반 기체, 용해력 없음)</td><td><b>액체</b> (용매 조성이 분리에 큰 영향)</td></tr>
<tr><td>고정상</td><td>비휘발성 액체 (가끔 고체)</td><td>고체(흡착) 또는 액체·결합상(분배)</td></tr>
<tr><td>분석물</td><td>기체·<b>휘발성</b> 물질</td><td><b>용액</b>에 녹기만 하면 됨</td></tr>
<tr><td>칼럼</td><td>개관(모세관)</td><td><b>충전</b></td></tr></table>
<ul><li><y>휘발성이 필요 없다</y>는 게 LC의 가장 큰 장점 → 대부분의 의약품(극성·열에 약함·큰 분자), 단백질·펩타이드도 분석 가능. 그래서 약대·제약 회사에서 압도적으로 많이 써.</li>
<li>GC는 이동상(기체)이 분리에 거의 관여 안 하지만, LC는 <g>이동상 조성(용매 세기)을 바꿔 머무름을 조절</g>할 수 있어 → 20번 이후 “용리” 파트의 핵심.</li></ul>"""),

# 3
dict(img=3, slide=3, title="고성능액체크로마토그래피(HPLC) 장치", sub="High-performance liquid chromatography: pump → injector → column → detector",
kw=["고압으로 이동상을 밀어냄", "아주 작은 입자", "진공 탈기기", "자동 시료 주입기", "칼럼 칸(온도)", "PDA 검출기"],
sum="HPLC는 고압 펌프로 용매를 아주 작은 입자가 채워진 닫힌 칼럼에 밀어 넣어 고분리를 얻어. 용매 → 탈기기 → 펌프 → 주입기 → 칼럼(온도 조절) → 검출기 → 데이터 순서.",
tr="""<p><b>고성능액체크로마토그래피 (HPLC)</b>: 아주 미세한 입자가 들어 있는 닫힌 칼럼에 <b>고압</b>으로 용매(이동상)를 밀어 넣어 <b>고분해능 분리</b>를 얻는다</p>
<p>도식: HPLC 용매 → HPLC 펌프 → 주입기(시료) → HPLC 칼럼 → 검출기 → 폐액 / 데이터 수집</p>
<p>Agilent HPLC 시스템 (위에서부터): HPLC 용매 · 용매 칸 · <b>진공 탈기기</b> · <b>HPLC 펌프</b> · <b>시료 주입기(자동 시료 주입기)</b> · <b>칼럼 칸</b> · <b>검출기(PDA)</b></p>""",
ex="""<table class="t"><tr><th>모듈</th><th>하는 일</th><th>관련 슬라이드</th></tr>
<tr><td>진공 탈기기</td><td>용매에 녹은 공기 제거 (기포, O₂의 UV 흡수 방지)</td><td>32</td></tr>
<tr><td><b>펌프</b></td><td>고압(수십–수백 bar)에서 <b>일정한</b> 유속</td><td>33</td></tr>
<tr><td>자동 시료 주입기</td><td>정확한 양(μL)을 고압 흐름에 주입</td><td></td></tr>
<tr><td>칼럼 칸</td><td>칼럼 <b>온도 조절</b> (재현성, 점도↓)</td><td>12</td></tr>
<tr><td>검출기</td><td>UV/PDA, 형광, ELSD, 전기화학, RI, MS</td><td>38–50</td></tr></table>
<ul><li>이름의 “고성능(high-performance)” = 작은 입자로 N이 커서 분리가 좋다는 뜻. 그 대가가 <b>고압</b> (“high-pressure”라고도 불렀어).</li>
<li>약대 실습 HPLC도 이 구성. 검출기는 대부분 <b>PDA</b>.</li></ul>
<div class="box"><span class="tag">족보</span>복기 키워드 “<b>Sample injection</b>”, “<b>protecting</b> / <b>guard column</b>”: 주입기와 칼럼 보호(11번 가드 칼럼)를 기억해.</div>"""),

# 4
dict(img=4, slide=4, title="액체크로마토그래피-질량분석 (LC-MS)", sub="LC-MS instruments",
kw=["HPLC + 질량분석기", "ESI·APCI 이온원", "탠덤 MS"],
sum="여러 LC-MS 장비 사진. HPLC 뒤에 질량분석기를 검출기로 붙인 것으로, Lecture 5에서 배운 ESI·APCI와 탠덤 MS가 여기서 쓰여.",
tr="""<p><b>액체크로마토그래피-질량분석 (LC-MS)</b></p>
<p>사진: HPLC 모듈(용매·펌프·주입기·칼럼) 옆에 연결된 여러 질량분석기 장비</p>""",
ex="""<p>Lecture 5 내용을 HPLC와 연결하는 슬라이드야.</p>
<ul><li>LC 용출액(액체)을 기체 이온으로 → <b>API: ESI, APCI, APPI</b> (Lecture 5 슬라이드 48–55)</li>
<li>검출 모드: <b>TIC, SIM, EIC</b>, 탠덤이면 <b>SRM(MRM)</b> — “선택을 두 번”, S/N↑</li>
<li>약대 장비: <b>삼중 사중극자(QQQ)</b>와 <b>Q-TOF</b>, 둘 다 ESI</li></ul>
<table class="t"><tr><th>검출기</th><th>선택성</th><th>감도</th></tr>
<tr><td>UV/PDA</td><td>빛 흡수하는 모든 것</td><td>ng</td></tr>
<tr><td><b>MS</b></td><td><b>m/z로 선택</b> (SIM·SRM)</td><td>ng–pg 이하</td></tr></table>
<p class="note">38번 표: MS 검출한계 0.1–1 ng, 기울기 용리 가능 “Yes”. 단 이동상에 비휘발성 완충액(인산염)을 쓰면 이온원이 막혀서 LC-MS에는 휘발성 완충액(포름산, 아세트산 암모늄)을 써.</p>"""),

# 5
dict(img=5, slide=5, title="크로마토그래피 과정 ① — 왜 LC는 개관 칼럼을 못 쓰나", sub="Open tubular (GC) vs packed (LC) columns",
kw=["개관 칼럼 장점", "GC = 개관", "LC = 충전", "D_m(액체) ≪ D_m(기체)", "C_m ∝ r²/D_m"],
sum="개관 칼럼은 장점이 많지만 LC에선 못 써. 액체 속 확산계수가 기체보다 약 1만 배 작아서 관이 아주 가늘지 않으면 C항(물질 전달)이 너무 커지기 때문이야. 그래서 LC는 작은 입자를 채운 충전 칼럼.",
tr="""<p><b>개관 칼럼의 장점 (충전 칼럼 대비)</b></p>
<ul><li>낮은 압력</li>
<li>높은 길이 유속 → 세로 확산↓ → 이론단 높이↓ → 좁은 피크 → 높은 분리도</li>
<li>여러 경로 흐름 없음 → 이론단 높이↓ → 좁은 피크 → 높은 분리도</li>
<li>긴 칼럼 → 이론단수↑ → 높은 분리도</li>
<li>높은 길이 유속 → 짧은 머무름시간 → 짧은 분석 시간</li></ul>
<p>칼럼: <b>개관 (GC)</b> / <b>충전 (LC)</b></p>
<p><b>왜 액체크로마토그래피에서는 개관 칼럼을 쓸 수 없을까?</b></p>""",
ex="""<div class="boxg"><b>Q 답</b>: van Deemter의 <b>C<sub>m</sub> ∝ r<sup>2</sup>/D<sub>m</sub></b> 때문.<br>
• 액체 속 확산계수 D<sub>m</sub> ≈ 10<sup>−9</sup> m²/s, 기체는 ≈ 10<sup>−5</sup> → <pk>약 10<sup>4</sup>배 느림</pk> (Lecture 6 표 22-1)<br>
• 그래서 액체가 흐르는 관에서 용질이 <b>벽의 고정상까지 확산해 가는 데 너무 오래</b> 걸려 → C항이 엄청 커져 피크가 넓어져<br>
• 이걸 GC 수준으로 맞추려면 관 반지름을 √10<sup>4</sup> = 100배쯤 줄여야(수 μm) → 시료 용량·주입·검출 부피가 너무 작아 실용적으로 어려움<br>
→ 대신 <y>아주 작은 입자(수 μm)를 채워</y> 이동상 속 확산 거리를 입자 사이 틈(≈ 입자 지름 수준)으로 줄인 게 HPLC의 충전 칼럼</div>
<ul><li>GC에서 개관 칼럼이 되는 이유는 반대로 <b>D<sub>m</sub>이 커서</b> 0.1–0.5 mm 관이어도 벽까지 금방 확산하기 때문.</li>
<li>B항(세로 확산 ∝ D<sub>m</sub>)은 LC에서 작아서 큰 문제가 아니고, LC의 주적은 <b>C항</b>이야.</li></ul>
<p class="note">🗣️ 넷째 수업: “GC는 오픈 튜뷸러, LC는 오픈 튜뷸러 칼럼을 쓸 수가 없어요. 전부 다 팩트 칼럼이에요.”</p>"""),

# 6
dict(img=6, slide=6, title="크로마토그래피 과정 ② — 작은 입자는 효율이 높지만 고압이 필요", sub="Effect of particle size: N = 2 000 (4 μm) vs 7 500 (1.7 μm)",
kw=["입자 4 μm → N 2 000", "입자 1.7 μm → N 7 500", "같은 길이유속", "용리 세기↑ → 빨라짐", "Q: (a) vs (b)"],
sum="같은 시료를 같은 길이유속으로 5 cm C18 칼럼에 흘렸을 때, 입자 4 μm(N 2 000)보다 1.7 μm(N 7 500)가 피크가 훨씬 좁아 분리가 좋아. (c)는 용매 세기를 올려 1분 남짓으로 빨라졌어.",
tr="""<p><b>작은 입자는 높은 효율을 주지만 높은 압력이 필요하다</b></p>
<p>(a) 입자 크기 = <b>4 μm</b>, <b>N = 2 000단</b> &nbsp; (b) 입자 크기 = <b>1.7 μm</b>, <b>N = 7 500단</b> &nbsp; (c) 입자 크기 = 1.7 μm, <b>용매의 용리 세기 증가</b> (1–1.2 min에 두 피크)</p>
<p>C<sub>18</sub>-실리카로 충전한 5.0 cm 칼럼에서 <b>같은 길이 속도</b>로 같은 시료를 분석한 크로마토그램</p>
<p>Q: (a)와 (b) 중 어느 쪽이 분리도가 더 좋은가?</p>""",
ex="""<div class="boxg"><b>Q 답: (b)</b>. 두 피크 위치(머무름시간)는 비슷하지만 (b)의 피크가 훨씬 <b>좁아</b>. R ∝ √N이므로 √(7 500/2 000) = √3.75 ≈ <b>1.9배</b> 분리도.</div>
<ul><li>왜 N이 커지나: 입자↓ → <b>A항↓</b>(경로 균일) + <b>C항↓</b>(확산 거리↓) → H↓ → N = L/H↑ (8번)</li>
<li>7번 근사식 N ≈ 3000L(cm)/d<sub>p</sub>(μm)로 검산: 5 cm, 4 μm → 3 750 / 1.7 μm → 8 800 → 실측 2 000·7 500과 경향이 같아(근사식은 최적 유속 기준).</li>
<li><b>(c)</b>: 분리도에 여유가 생기니까 <y>용매 세기를 올려(역상이면 유기용매 비율↑) 머무름시간을 확 줄인</y> 것. 분리도는 조금 줄지만 분석 시간이 3–4분 → 1분대. 작은 입자의 실용적 이점이 바로 이거야: <b>같은 분리를 더 빨리</b>.</li></ul>
<div class="box"><span class="tag">족보</span>2025-2 주관식 “반딤터 이용해서 왜 입자 작게 칼럼 만드는 게 유리한지, 발생하는 문제는?” → 6–10번 다섯 장이 정답 재료.</div>"""),

# 7
dict(img=7, slide=7, title="크로마토그래피 과정 ③ — 입자 크기별 van Deemter 곡선", sub="van Deemter curves for 5, 3.5, 2.7 (fused-core), 1.8 μm particles · N ≈ 3000L/d_p",
kw=["입자↓ → H↓", "입자 작으면 곡선 오른쪽이 평평", "N ≈ 3000·L(cm)/d_p(μm)", "2.7 μm 표면다공성(코어-쉘)"],
sum="입자가 작을수록 곡선 전체가 낮아지고(H↓), 빠른 유속에서도 H가 별로 안 커져. 최적 유속에서의 이론단수는 대략 N ≈ 3000 × 칼럼 길이(cm) / 입자 지름(μm).",
tr="""<p>그래프: 이론단 높이(μm) vs 길이 유속(mm/s) — <b>5 μm</b>(최저 약 10 μm, 오른쪽으로 가파르게 증가), <b>3.5 μm</b>(최저 약 7 μm), <b>2.7 μm 융합 코어 표면다공성</b>(파랑, 최저 약 4 μm), <b>1.8 μm</b>(최저 약 4 μm, 거의 평평)</p>
<p>van Deemter 곡선: C18-실리카(50 × 4.6 mm)에서 나프탈렌을 60 vol% 아세토나이트릴/40 vol% 물, 24 ℃로 용리해 측정</p>
<ul><li>입자가 <b>작을수록 이론단 높이가 낮다</b></li>
<li>입자가 작으면 이론단 높이가 <b>유속 증가에 별로 민감하지 않다</b></li></ul>
<p class="eq">최적 유속에서의 이론단수: N = L/H ≈ 3000 L(cm) / d<sub>p</sub>(μm) &nbsp; (L: 칼럼 길이, d<sub>p</sub>: 입자 지름)</p>""",
ex="""<ul><li><b>H<sub>min</sub> ≈ 2 × d<sub>p</sub></b>: 5 μm → ~10 μm, 1.8 μm → ~4 μm. 그래서 N = L/H ≈ L/(2d<sub>p</sub>)인데, 단위를 맞추면(L cm → μm는 ×10<sup>4</sup>) N ≈ 10<sup>4</sup>L/(2–3 d<sub>p</sub>) ≈ <g>3000 L(cm)/d<sub>p</sub>(μm)</g>.</li>
<li><b>오른쪽이 평평</b> = C항(기울기)이 작다 = 빠르게 흘려도 효율 유지 → <y>분석 시간 단축</y>. 5 μm는 빨리 흘리면 H가 확 올라감.</li>
<li><b>2.7 μm 융합 코어(fused-core, 코어-쉘, 표면다공성)</b>: 속은 단단한 실리카, 겉의 얇은 다공층만 고정상 → 확산 거리가 짧아 1.8 μm급 효율을 <b>더 낮은 압력</b>으로 얻음.</li></ul>
<p><b>계산</b>: 25 cm, 5 μm 칼럼 → N ≈ 3000 × 25/5 = <b>15 000</b> / 15 cm, 3 μm → 15 000 / 5 cm, 1.7 μm → 약 8 800</p>
<div class="box"><span class="tag">시험</span>“입자 크기를 절반으로 하면 N은?” → 약 <b>2배</b>(같은 길이). 압력은 훨씬 더 커짐(9–10번).</div>"""),

# 8
dict(img=8, slide=8, title="크로마토그래피 과정 ④ — 작은 입자는 A와 C를 줄인다", sub="A smaller particle size results in a decrease in A and C",
kw=["H = A + B/u + C·u", "입자↓ → A↓, C↓", "최저점이 왼쪽 아래 → 오른쪽 아래로", "빨간 점선: 최저점 이동"],
sum="같은 van Deemter 곡선에 최저점들을 이은 빨간 점선을 그렸어. 입자가 작아지면 A(여러 경로)와 C(평형 시간)가 줄어 최저 H가 낮아지고 최적 유속은 빨라져.",
tr="""<p>그래프: 7번과 같은 van Deemter 곡선 + 각 곡선의 최저점을 잇는 빨간 점선 (입자가 작을수록 최저점이 아래·오른쪽으로)</p>
<p class="eq">H ≈ A + B/u<sub>x</sub> + C·u<sub>x</sub> (A: 여러 흐름 경로, B/u<sub>x</sub>: 세로 확산, C·u<sub>x</sub>: 평형 시간, A·B·C: 주어진 칼럼과 고정상의 상수)</p>
<p><b>입자 크기가 작아지면 van Deemter 식의 A와 C가 감소한다.</b></p>""",
ex="""<table class="t"><tr><th>항</th><th>입자↓ 하면</th><th>이유</th></tr>
<tr><td><b>A</b></td><td>↓</td><td>입자 사이 경로가 더 균일 → 경로 길이 차↓</td></tr>
<tr><td>B</td><td>거의 그대로</td><td>세로 확산은 이동상 D<sub>m</sub>와 시간이 정함 (입자 크기와 무관)</td></tr>
<tr><td><b>C</b></td><td>↓</td><td>입자 속 구멍·입자 사이 틈이 작아 확산 거리↓ → 평형 빠름</td></tr></table>
<ul><li>u<sub>opt</sub> = √(B/C): B는 그대로인데 C↓ → <g>u<sub>opt</sub>↑</g> (빨간 점선이 오른쪽으로) → 최적 조건 자체가 더 빠른 유속</li>
<li>H<sub>min</sub> = A + 2√(BC): A↓, C↓ → <g>H<sub>min</sub>↓</g></li></ul>
<div class="boxg"><b>족보 답안 뼈대</b> (“반딤터로 입자 작은 칼럼이 유리한 이유와 문제점”)<br>
① 입자↓ → A↓(경로 균일), C↓(확산 거리↓) → H<sub>min</sub>↓, N↑, 분리도↑<br>
② C 기울기↓ → 곡선 오른쪽이 평평 → 빠른 유속에서도 효율 유지 → 분석 시간↓<br>
③ <b>문제</b>: 입자 사이 틈이 좁아 <b>역압 급증</b> (P ∝ 1/d<sub>p</sub><sup>2</sup>, 9번) → 고압 펌프(UHPLC), 막힘, 마찰열</div>"""),

# 9
dict(img=9, slide=9, title="크로마토그래피 과정 ⑤ — 칼럼 압력 식과 UHPLC", sub="Column pressure P = f·u_x·η·L / (πr²·d_p²) · HPLC vs UHPLC",
kw=["P ∝ u_x·η·L / (r²·d_p²)", "HPLC 0.5–5 mL/min, 70–400 bar", "UHPLC 1.5–2.0 μm, ~1000 bar", "점도 η"],
sum="칼럼 압력은 유속·점도·길이에 비례하고 반지름 제곱과 입자 지름 제곱에 반비례해. 일반 HPLC는 70–400 bar, 1.5–2 μm 입자를 쓰는 UHPLC는 약 1000 bar까지 올라가.",
tr="""<p class="eq">칼럼 압력 P = f · u<sub>x</sub>ηL / (πr<sup>2</sup>d<sub>p</sub><sup>2</sup>)</p>
<p>u<sub>x</sub>: 길이 유속 · η: 용매의 점도 · L: 칼럼 길이 · r: 칼럼 반지름 · d<sub>p</sub>: 입자 지름 · f: 입자 모양과 충전 상태에 따른 계수</p>
<p><b>일반적인 HPLC 칼럼 압력</b>: 유속 0.5–5 mL/min · 압력 약 7–40 MPa = 70–400 bar = 1 000–6 000 psi</p>
<p><b>초고성능 액체크로마토그래피 (UPLC 또는 UHPLC)</b>: 1.5–2.0 μm 입자 · 압력 약 100 MPa = 1000 bar = 150 000 psi (슬라이드 표기)</p>""",
ex="""<p><b>식 읽기</b>: 분자에 있는 건 압력을 <b>키우고</b>, 분모에 있는 건 <b>줄여</b>.</p>
<table class="t"><tr><th>바꾸면</th><th>압력</th><th>예</th></tr>
<tr><td>입자 지름 절반</td><td><b>4배</b> (같은 u<sub>x</sub>)</td><td>5 → 2.5 μm</td></tr>
<tr><td>칼럼 길이 2배</td><td>2배</td><td></td></tr>
<tr><td>유속 2배</td><td>2배</td><td></td></tr>
<tr><td>점도↓ (온도↑, ACN이 MeOH보다 낮음)</td><td>↓</td><td>12번 칼럼 가열</td></tr></table>
<ul><li>📝 단위 검산: 1 bar = 10<sup>5</sup> Pa, 1 MPa = 10 bar, 1 bar ≈ 14.5 psi → 400 bar ≈ 5 800 psi ✓, <pk>1000 bar ≈ 15 000 psi</pk> (슬라이드의 150 000은 0이 하나 더 붙은 오타로 보여)</li>
<li>입자를 줄이면 최적 유속도 빨라지니까(8번) <b>최적 조건에서의 압력</b>은 1/d<sub>p</sub><sup>3</sup>에 가깝게 늘어 → 10번 표 5 μm 19 bar → 1 μm 2 300 bar (약 5<sup>3</sup> = 125배 ✓)</li>
<li>UHPLC = 펌프·주입기·배관·칼럼을 모두 ~1000 bar급으로 만든 장비. 2 μm 이하 입자를 쓰려면 필수.</li></ul>"""),

# 10
dict(img=10, slide=10, title="크로마토그래피 과정 ⑥ — 입자 지름에 따른 성능 (표 24-1)", sub="TABLE 24-1 Performance as a function of particle diameter",
kw=["d_p 5 → 1 μm", "t_r 30 → 6 min", "N 25 000 → 125 000", "압력 19 → 2 300 bar"],
sum="입자를 5 μm에서 1 μm로 줄이면 분석 시간은 30분 → 6분, 이론단수는 2만 5천 → 12만 5천으로 좋아지지만, 필요한 압력은 19 bar → 2 300 bar로 폭증해.",
tr="""<p><b>표 24-1 입자 지름에 따른 성능</b> (입자 크기 d<sub>p</sub> μm / 머무름시간 min / 이론단수 N / 필요 압력 bar)</p>
<ul><li>5.0 / 30 / 25 000 / 19</li><li>3.0 / 18 / 42 000 / 87</li><li>1.5 / 9 / 83 000 / 700</li><li>1.0 / 6 / 125 000 / 2 300</li></ul>
<p class="note">참고: 지름 33 μm × 길이 25 cm 모세관에서, 머무름 인자 k = 2, 확산계수 6.7 × 10<sup>−10</sup> m²/s 용질이 물-아세토나이트릴 용리액일 때 최소 이론단 높이 조건의 이론 성능. 출처: MacNair, Patel, Jorgenson, Anal. Chem. 1999, 71, 700.</p>""",
ex="""<p>숫자에서 <b>비례 관계</b>를 읽어 봐 (d<sub>p</sub> 5 → 1 μm, 5배 작게).</p>
<table class="t"><tr><th>값</th><th>5 μm → 1 μm</th><th>비례</th></tr>
<tr><td>N</td><td>25 000 → 125 000 (<b>5배</b>)</td><td>N ∝ 1/d<sub>p</sub> (7번 근사식)</td></tr>
<tr><td>t<sub>r</sub></td><td>30 → 6 min (<b>1/5</b>)</td><td>u<sub>opt</sub> ∝ 1/d<sub>p</sub> → 더 빨리 흘려도 됨</td></tr>
<tr><td><b>압력</b></td><td>19 → 2 300 bar (<b>~120배</b>)</td><td>P ∝ u/d<sub>p</sub><sup>2</sup> ∝ <b>1/d<sub>p</sub><sup>3</sup></b> (5<sup>3</sup> = 125)</td></tr></table>
<div class="boxg"><b>한 줄</b>: 입자를 줄이면 <y>효율(N)과 속도는 1/d<sub>p</sub>로 좋아지지만, 압력은 1/d<sub>p</sub><sup>3</sup>로 나빠진다</y>. 그래서 무한정 작게 못 만들고, 현실적 한계가 1.5–2 μm(UHPLC ~1000 bar).</div>
<p class="note">이 표는 아주 가는 모세관 칼럼의 이론값이라 압력 숫자가 일반 4.6 mm 칼럼과 다를 수 있어. 경향(비례 관계)만 기억해.</p>"""),

# 11
dict(img=11, slide=11, title="크로마토그래피 과정 ⑦ — 칼럼 구조와 가드 칼럼", sub="The column: porous titanium frits, guard column, inner diameter 1–5 mm, length 2–30 cm",
kw=["다공성 타이타늄 프릿", "가드 칼럼", "주 칼럼(스테인리스·플라스틱)", "안지름 1–5 mm", "길이 2–30 cm"],
sum="HPLC 칼럼 양 끝엔 다공성 타이타늄 프릿이 있어 용매를 고르게 퍼뜨리고 고정상이 빠져나가지 않게 해. 주 칼럼 앞의 가드 칼럼은 같은 고정상으로 미세 입자와 강하게 붙는 물질을 먼저 잡아 주 칼럼을 보호해.",
tr="""<p>그림: 주입기 → 입구 → <b>가드 칼럼</b> → <b>다공성 타이타늄 프릿</b> → 양극산화 알루미늄 재킷 → <b>주 칼럼(플라스틱 또는 스테인리스)</b> → 다공성 타이타늄 프릿 → 출구 → 검출기 (용매 흐름은 위 → 아래)</p>
<p><b>다공성 타이타늄 프릿</b>: - 용매를 고르게 분배 - 고정상을 칼럼 안에 붙잡아 둠</p>
<p><b>가드 칼럼</b>: - 미세 입자와 강하게 흡착되는 용질을 붙잡아 <b>주 칼럼을 보호</b> - 주 칼럼과 <b>같은 고정상</b>을 담고 있음</p>
<ul><li>안지름: <b>1–5 mm</b></li><li>길이: <b>2–30 cm</b></li></ul>""",
ex="""<ul><li><b>프릿(frit)</b> = 아주 작은 구멍이 난 금속 필터 디스크. 입자(수 μm)는 못 지나가고 용매는 통과.</li>
<li><b>가드 칼럼</b> = 주 칼럼 앞에 다는 짧고 싼 칼럼. 시료 속 먼지·불용성 입자, 고정상에 영구히 붙어 버리는 물질(단백질, 지질 등)이 <y>주 칼럼 대신 여기에 쌓이게</y> 해. 더러워지면 가드만 교체 → 비싼 주 칼럼의 수명↑.</li>
<li><b>같은 고정상</b>이어야 하는 이유: 다른 고정상이면 분리에 영향(머무름이 달라짐).</li></ul>
<table class="t"><tr><th></th><th>GC (개관)</th><th>HPLC (충전)</th></tr>
<tr><td>안지름</td><td>0.1–0.53 mm</td><td><b>1–5 mm</b> (흔히 4.6, 2.1 mm)</td></tr>
<tr><td>길이</td><td>15–100 m</td><td><b>2–30 cm</b> (흔히 15, 25 cm)</td></tr></table>
<div class="box"><span class="tag">족보</span>복기 키워드 “<b>protecting</b>”, “<b>guard column</b>” + 2025-2 tailing 주관식의 해결책 하나가 “칼럼 입구 오염 → 가드 칼럼”. 역할 두 가지와 “주 칼럼과 같은 고정상”을 기억해.</div>"""),

# 12
dict(img=12, slide=12, title="크로마토그래피 과정 ⑧ — 칼럼 가열", sub="Heating a chromatography column",
kw=["점도↓ → 압력↓·빠른 유속", "머무름시간↓", "C항↓ → 분리도↑", "고정상 분해·수명↓", "실온 + 10 ℃ → 재현성↑"],
sum="칼럼을 가열하면 점도가 낮아져 압력이 줄거나 더 빨리 흘릴 수 있고, 머무름시간이 줄고, 확산이 빨라져 C항이 작아져. 대신 고정상이 분해돼 칼럼 수명이 줄 수 있어. 실온보다 10 ℃ 높게 고정하면 재현성이 좋아져.",
tr="""<p><b>크로마토그래피 칼럼 가열</b></p>
<ul><li>용매 <b>점도를 낮춤</b> → 필요한 압력을 줄이거나 더 빠른 용매 흐름이 가능</li>
<li><b>머무름시간을 줄임</b></li>
<li>이동상과 고정상 사이 용질의 확산을 빠르게 해 <b>분리도를 개선</b> (즉 van Deemter 식의 <b>C가 작아짐</b>)</li>
<li><b>그러나</b> 온도 상승은 고정상을 분해시키고 칼럼 수명을 줄일 수 있다 (빨간 글씨)</li>
<li><b>실온보다 10 ℃ 높게</b> 맞춘 칼럼 히터를 쓰면 머무름시간의 <b>재현성</b>과 정량 분석의 <b>정밀도</b>가 좋아진다 (파란 글씨)</li></ul>""",
ex="""<p>Lecture 6 슬라이드 42–43(온도 효과)을 HPLC에 적용한 정리야.</p>
<table class="t"><tr><th>온도↑ 효과</th><th>연결</th></tr>
<tr><td>점도 η↓</td><td>P ∝ η (9번) → 압력↓ 또는 유속↑</td></tr>
<tr><td>D<sub>s</sub>, D<sub>m</sub>↑</td><td>C<sub>s</sub> ∝ d²/D<sub>s</sub>, C<sub>m</sub> ∝ r²/D<sub>m</sub> → C↓ → 피크 좁아짐</td></tr>
<tr><td>K↓ (분배)</td><td>머무름시간↓ → 분석 빨라짐</td></tr>
<tr><td><pk>고정상 분해</pk></td><td>실리카 결합상의 가수분해 가속 (보통 실리카 칼럼은 ~60 ℃ 이하)</td></tr></table>
<ul><li><b>왜 “실온 + 10 ℃”?</b> 실험실 온도는 아침저녁·계절마다 변해 → 머무름시간이 흔들려. 실온보다 조금 높게 <y>일정하게 고정</y>하면 바깥 온도와 무관해짐 → 재현성↑. (실온보다 낮게 유지하려면 냉각 장치가 필요해서 “위로”)</li>
<li>🗣️ 넷째 수업: “실제로 우리가 분석할 때 온도 조절 거의 예외 없이 하고 합니다.”</li></ul>"""),

# 13
dict(img=13, slide=13, title="크로마토그래피 과정 ⑨ — 고정상 지지체: 실리카", sub="Silica support: highly pure, spherical, microporous · dissolves above pH 8",
kw=["고순도 구형 다공성 실리카", "넓은 표면적", "pH 8 이상에서 용해", "에틸렌 다리 실리카 → pH 12"],
sum="HPLC 고정상의 가장 흔한 지지체는 고순도·구형·다공성 실리카 입자야. 용매가 스며들고 표면적이 넓어. 단 염기에 녹아서 대부분 pH 8 이상에선 못 쓰고, 에틸렌 다리를 넣은 실리카는 pH 12까지 버텨.",
tr="""<ul><li>HPLC 고정상의 가장 흔한 지지체는 용매가 투과할 수 있고 표면적이 큰 <b>고순도, 구형, 미세다공성 실리카 입자</b>이다</li>
<li>대부분의 실리카는 <b>염기에 녹기 때문에 pH 8 이상에서 쓸 수 없다</b></li></ul>
<p>그림: 지름 <b>4.4 μm</b> 미세다공성 실리카 입자의 SEM 사진 · 일반 실리카 구조(수소결합 인접 실라놀, 고립 실라놀, 제미널 실라놀, 실록세인 결합) · pH에 따른 실리카 용해도 그래프(pH 8 넘어서 급증) · Si(OH)₄ + OH⁻ → 규산 이온 + H₂O · <b>에틸렌 다리(–CH₂–CH₂–)가 있는 실리카</b> — <b>pH 12까지 가수분해에 견딤</b></p>""",
ex="""<ul><li><b>구형 + 균일</b> → 고르게 채워져 A항↓(Lecture 6). <b>다공성</b> → 표면적↑ → 고정상 많음 → 머무름·시료 용량↑. 🗣️ 실리카겔은 “구멍이 숭숭 뚫린 스펀지”.</li>
<li><b>pH 8 이상</b>: OH⁻가 Si–O–Si를 공격해 실리카가 녹음 (그래프에서 pH 8 넘어 용해도 급증) → 칼럼이 무너짐(void) → 피크 모양 망가짐.</li>
<li><b>에틸렌 다리 하이브리드 실리카</b>: Si–O–Si 일부를 Si–CH₂–CH₂–Si로 바꿔 → 가수분해에 강해져 <g>pH 12까지</g>. 염기성 약물을 고pH에서(중성형으로) 분석할 때 유용.</li></ul>
<div class="boxg"><b>pH 범위 정리</b> (18번과 세트): 실리카 지지체 결합상은 <b>pH 2–8</b>.<br>• pH &lt; 2: 결합상의 실록세인 결합이 <b>산 가수분해</b>로 떨어짐<br>• pH &gt; 8: 실리카 자체가 <b>염기에 녹음</b></div>"""),

# 14
dict(img=14, slide=14, title="크로마토그래피 과정 ⑩ — 실라놀기와 tailing", sub="Silanol groups: protonated at pH 2–3, Si–O⁻ above pH 3, retain protonated bases",
kw=["실라놀 Si–OH", "pH 2–3에서 양성자화", "pH 3 이상 Si–O⁻", "–Si–O⁻ ⁺NHR₃", "염기성 약물 tailing"],
sum="실리카 표면의 실라놀(Si–OH)은 pH 2–3에선 중성이지만 pH 3 이상에선 Si–O⁻로 해리돼. 노출된 Si–O⁻가 양성자화된 염기(아민 약물)를 강하게 붙잡아 꼬리 끄는 피크가 생겨.",
tr="""<p>그림: 실리카 구조 — 수소결합한 인접 실라놀기, 고립 실라놀기, 제미널 실라놀기, 실록세인 결합</p>
<p><b>실라놀기 (Silanol groups)</b>:</p>
<ul><li><b>pH ~2–3</b>에서 양성자화되어 있다 (Si–OH)</li>
<li><b>pH 3 이상</b>에서 음전하 <b>Si–O⁻</b>로 해리된다</li>
<li>노출된 Si–O⁻기는 <b>양성자화된 염기를 강하게 붙잡아 tailing</b>을 일으킨다: <b>–Si–O⁻ ⁺NHR₃</b></li></ul>""",
ex="""<p>2025-2 기말 주관식 “<b>HPLC에서 tailing 어떻게 막는지</b>”의 <pk>원인</pk>이 바로 이 슬라이드야.</p>
<ul><li>대부분의 약물은 아민(염기) → 산성~중성 이동상에서 <b>R₃NH⁺</b>(양이온)</li>
<li>pH &gt; 3이면 실라놀이 <b>Si–O⁻</b>(음이온) → 둘이 <y>이온 결합(이온교환)</y> → 분배 외에 “끈적한” 추가 머무름 → 일부 분자만 늦게 떨어져 <b>꼬리</b></li>
<li>이 상호작용은 자리 수가 적고 세서 농도에 따라 포화 → 피크 모양이 비대칭(비대칭 인자 A/B &gt; 1)</li></ul>
<table class="t"><tr><th>해결책</th><th>원리</th><th>슬라이드</th></tr>
<tr><td><b>엔드캡</b></td><td>남은 실라놀을 TMS로 덮음</td><td>17</td></tr>
<tr><td>고순도 Type B/C 실리카</td><td>노출 실라놀·금속 불순물↓</td><td>15</td></tr>
<tr><td><b>이동상 pH ~2–3</b></td><td>실라놀을 Si–OH(중성)로 유지</td><td>14</td></tr>
<tr><td>경쟁 염기(트라이에틸아민)</td><td>Si–O⁻ 자리를 먼저 차지</td><td>(참고)</td></tr>
<tr><td>가드 칼럼·주입량↓</td><td>오염·과부하로 인한 tailing</td><td>11</td></tr></table>"""),

# 15
dict(img=15, slide=15, title="크로마토그래피 과정 ⑪ — 실리카 Type A · B · C", sub="Type A vs Type B silica: tricyclic antidepressants",
kw=["Type A: 실라놀·금속 불순물 → tailing", "Type B: 현재 표준, tailing↓", "Type C: 실라놀 90% → Si–H", "삼환계 항우울제"],
sum="염기성 삼환계 항우울제 4가지를 분석하면 구형 Type A 실리카(Zorbax-ODS)에선 피크가 넓고 꼬리를 끌지만, 불순물이 적은 Type B(Zorbax Rx-C18)에선 날카로워져. Type C는 실라놀의 90%를 Si–H로 바꿔 tailing이 더 적어.",
tr="""<p>(a) <b>Type A 실리카</b> Zorbax-ODS (다이메틸-C18): 피크가 넓고 꼬리 끎 · (b) <b>Type B 실리카</b> Zorbax Rx-C18 (다이메틸-C18): 피크가 날카로움</p>
<p>1 독세핀 0.125 μg · 2 데시프라민 0.25 μg · 3 아미트립틸린 0.25 μg · 4 트리미프라민 0.25 μg (구조: 삼환계 + 아민 곁사슬) · –Si–O⁻ ⁺NHR₃</p>
<ul><li>Type A 실리카에서는 <b>실라놀과 금속 불순물</b>이 tailing을 일으킨다</li>
<li>오늘날 가장 흔한 <b>Type B 실리카</b>는 노출된 실라놀과 금속 불순물이 적어 <b>tailing이 덜하다</b></li>
<li>실라놀기의 <b>90%를 Si–H 결합으로 바꾼 Type C 실리카</b>는 tailing이 더욱 적다</li></ul>""",
ex="""<ul><li>시료가 전부 <b>3차·2차 아민</b>(삼환계 항우울제) = 14번에서 본 “양성자화된 염기” → 실라놀 tailing을 보여 주기에 딱 좋은 예.</li>
<li>특히 <b>2 데시프라민</b>(2차 아민, N–H 있음)이 Type A에서 작고 넓어 → 실라놀과 수소결합·이온결합이 가장 강해서.</li>
<li><b>금속 불순물</b>(Fe, Al): 주변 실라놀을 더 산성으로 만들어 Si–O⁻가 더 쉽게 생기고, 킬레이트 가능한 분석물과 직접 결합 → tailing.</li></ul>
<table class="t"><tr><th>Type</th><th>특징</th><th>tailing</th></tr>
<tr><td>A</td><td>구형, 금속 불순물·산성 실라놀 많음</td><td>많음</td></tr>
<tr><td><b>B</b></td><td>고순도, 현재 표준</td><td>적음</td></tr>
<tr><td>C</td><td>실라놀 90% → Si–H (하이드라이드)</td><td>더 적음</td></tr></table>
<p class="note">같은 C18 고정상(다이메틸-C18)인데도 지지체 실리카의 순도만으로 피크 모양이 이렇게 달라져. “칼럼 바꿔서 tailing 해결”의 근거.</p>"""),

# 16
dict(img=16, slide=16, title="크로마토그래피 과정 ⑫ — 흡착용 실리카 vs 분배용 결합상", sub="Silica → adsorption stationary phase / bonded stationary phase (silanization)",
kw=["맨 실리카 = 흡착", "결합상 = 분배", "실레인화", "Si–O–Si(CH₃)₂–R"],
sum="실리카를 그대로 쓰면 흡착 크로마토그래피의 고정상, 표면 실라놀에 클로로실레인을 반응시켜 R기를 공유결합(실레인화)하면 분배 크로마토그래피의 결합 고정상이 돼.",
tr="""<p><b>실리카</b> → 흡착 크로마토그래피용 고정상 / 분배 크로마토그래피용 <b>결합 고정상</b></p>
<p>그림: 실리카 입자 표면 –Si–O–Si(CH₃)₂–<b>R</b> (결합 고정상)</p>
<p class="eq">≡Si–OH + Cl–Si(CH₃)₂–R → ≡Si–O–Si(CH₃)₂–R + HCl &nbsp; (<b>실레인화, silanization</b>)</p>""",
ex="""<p>Lecture 6 분류표의 “결합상(BPC)”이 어떻게 만들어지는지 보여 주는 슬라이드야.</p>
<table class="t"><tr><th></th><th>맨 실리카</th><th>결합상 (bonded phase)</th></tr>
<tr><td>표면</td><td>Si–OH (극성)</td><td>Si–O–Si–<b>R</b> (R에 따라 극성/비극성)</td></tr>
<tr><td>기전</td><td><b>흡착</b> (표면에 달라붙음)</td><td><b>분배</b> (R층에 녹아듦)</td></tr>
<tr><td>예</td><td>학생 실험 실리카겔 칼럼 (순상)</td><td>C18 역상 칼럼 (의약품 HPLC 주력)</td></tr></table>
<ul><li><b>실레인화</b>: 실라놀의 –OH와 클로로실레인의 Si–Cl이 반응, HCl이 빠지며 <y>Si–O–Si 공유결합</y> → R기가 표면에 “고정”. 액체처럼 행동하지만 씻겨 나가지 않는 고정상.</li>
<li>🗣️ 셋째 수업: 결합상이 “전 세계에서 가장 많이 사용되는 고정상”, 하지만 비싸서 대량 정제엔 맨 실리카.</li></ul>
<p class="note">R기가 큰 C18은 공간을 많이 차지해서 모든 실라놀과 반응하지 못해 → 남은 실라놀(14번 tailing의 원인) → 17번 엔드캡으로 처리.</p>"""),

# 17
dict(img=17, slide=17, title="크로마토그래피 과정 ⑬ — 결합상 종류와 엔드캡", sub="Polar & nonpolar bonded phases · C18 = ODS · end capping with ClSi(CH₃)₃",
kw=["극성: 아미노·사이아노·다이올", "비극성: C18·C8·페닐", "C18 = ODS", "엔드캡: 트라이메틸실릴"],
sum="결합상 R기로 극성(아미노, 사이아노, 다이올)과 비극성(C18, C8, 페닐) 고정상을 만들어. C18 = ODS(옥타데실실레인). 남은 실라놀은 ClSi(CH₃)₃와 반응시켜 트라이메틸실릴기로 덮는데, 이게 엔드캡이고 tailing을 줄여.",
tr="""<p><b>흔한 극성 고정상</b>: R = (CH₂)₃NH₂ <b>아미노</b> · R = (CH₂)₂CN <b>사이아노</b> · R = (CH₂)₂OCH₂CH(OH)CH₂OH <b>다이올</b></p>
<p><b>흔한 비극성 고정상</b>: R = (CH₂)₁₇CH₃ <b>옥타데실(C18)</b> · R = (CH₂)₇CH₃ <b>옥틸(C8)</b> · R = (CH₂)₃C₆H₅ <b>페닐</b></p>
<p><b>옥타데실 = C18 = ODS (OctaDecylSilane)</b></p>
<p><b>엔드캡(End capping)</b>: 실리카 표면에 남은 실라놀기를 ClSi(CH₃)₃와 반응시켜 <b>트라이메틸실릴기로 덮어</b>, tailing을 일으키는 극성 흡착 자리를 없앤다</p>
<p>그림: –Si–OH가 남은 표면 —(엔드캡, ClSi(CH₃)₃)→ –Si–O–Si(CH₃)₃로 바뀐 표면</p>""",
ex="""<table class="t"><tr><th>고정상</th><th>R</th><th>극성</th><th>주 용도</th></tr>
<tr><td><b>C18 (ODS)</b></td><td>(CH₂)₁₇CH₃, 탄소 18개</td><td>가장 비극성</td><td><b>역상 HPLC 표준</b>, 대부분의 약물</td></tr>
<tr><td>C8</td><td>탄소 8개</td><td>비극성 (C18보다 약함)</td><td>잘 안 떨어지는 소수성 물질 → 머무름↓</td></tr>
<tr><td>페닐</td><td>(CH₂)₃C₆H₅</td><td>비극성 + π–π</td><td>방향족 선택성</td></tr>
<tr><td>사이아노</td><td>(CH₂)₂CN</td><td>중간 극성</td><td>순상·역상 둘 다</td></tr>
<tr><td>아미노 · 다이올</td><td>–NH₂ / –OH 2개</td><td>극성</td><td>순상, 당류</td></tr></table>
<ul><li><b>ODS</b> 이름 풀이: <b>O</b>cta<b>D</b>ecyl<b>S</b>ilane (슬라이드의 빨간 O, d, S). 족보 “Hypersil <b>ODS</b> column (C18 on 5 μm silica)”이 바로 이것.</li>
<li><b>엔드캡 원리</b>: ClSi(CH₃)₃는 크기가 작아 C18 사슬 사이 틈의 실라놀까지 들어가 반응 → –OH를 비극성 –O–Si(CH₃)₃로 바꿔 <g>Si–O⁻ 자리 제거</g> → 염기성 약물 tailing↓.</li></ul>
<div class="box"><span class="tag">족보</span>tailing 주관식 답에 “<b>엔드캡 칼럼</b> 사용”을 꼭 넣어. 원리(남은 실라놀을 트라이메틸실릴로 덮어 극성 흡착 자리 제거)까지 쓰면 만점.</div>"""),

# 18
dict(img=18, slide=18, title="크로마토그래피 과정 ⑭ — 결합상의 pH 한계와 아이소뷰틸 보호기", sub="Siloxane bond hydrolyzes below pH 2 · silica dissolves above pH 8 · bulky isobutyl groups",
kw=["pH < 2: 실록세인 가수분해", "pH > 8: 실리카 용해", "사용 범위 pH 2–8", "부피 큰 아이소뷰틸기", "H₃O⁺ 공격 차단"],
sum="결합상의 Si–O–Si 결합은 pH 2 미만에서 가수분해되고, 실리카는 pH 8 초과에서 녹아. 그래서 실리카 결합상은 보통 pH 2–8에서만 써. 메틸 대신 부피 큰 아이소뷰틸기를 붙이면 H₃O⁺의 공격을 막아 저pH·고온에서도 오래 버텨.",
tr="""<ul><li><b>실록세인 결합은 pH 2 미만에서 가수분해</b>된다</li>
<li><b>실리카는 염기(pH &gt; 8)에 녹는다</b></li>
<li>⇒ 실리카 지지체 위의 결합 고정상 사용은 일반적으로 <b>pH 2–8 범위</b>로 제한된다</li>
<li><b>부피 큰 아이소뷰틸기</b>가 고정상을 <b>H₃O⁺의 공격으로부터 보호</b>한다</li>
<li>부피 큰 아이소뷰틸기를 가진 고정상은 <b>높은 온도에서도 낮은 pH에서 더 오래 안정</b>하다</li></ul>
<p>그림: (왼쪽) Si 위 CH₃ 두 개 — H₃O⁺와 :OH₂가 Si–O 결합을 공격 / (오른쪽) Si 위 <b>아이소뷰틸</b>(CH₂–CH(CH₃)₂) 두 개가 우산처럼 Si–O를 가림</p>""",
ex="""<p>13·14·17번과 합쳐서 <b>pH 정리</b>를 하자.</p>
<table class="t"><tr><th>pH</th><th>무슨 일</th><th>결과</th></tr>
<tr><td>&lt; 2</td><td>결합상 Si–O–Si(R) <b>산 가수분해</b></td><td>R기가 떨어져 나감(칼럼 블리드), 머무름↓</td></tr>
<tr><td>2–3</td><td>실라놀 Si–OH (중성)</td><td><g>tailing 최소</g> → 염기성 약물 분석에 흔히 씀</td></tr>
<tr><td>3–8</td><td>실라놀 Si–O⁻</td><td>염기성 약물 tailing 위험</td></tr>
<tr><td>&gt; 8</td><td>실리카 <b>용해</b></td><td>칼럼 붕괴 (에틸렌 다리 실리카는 pH 12까지)</td></tr></table>
<ul><li><b>입체 보호(steric protection)</b>: 메틸(작음) 대신 아이소뷰틸(큼)을 Si에 붙이면 <y>물리적으로 가려서</y> H₃O⁺·물이 Si–O에 접근 못 함 → 저pH 안정성↑.</li>
<li>그래서 0.1% TFA(pH 약 2) 같은 산성 이동상을 오래 쓰려면 이런 “입체 보호형” 칼럼을 골라.</li></ul>
<div class="box"><span class="tag">시험</span>“실리카 기반 결합상의 사용 pH 범위와 그 이유” → <b>2–8</b>, 아래는 실록세인 가수분해, 위는 실리카 용해.</div>"""),

# 19 (20)
dict(img=19, slide=20, title="크로마토그래피 과정 ⑯ — 용리 과정: 용매가 용질을 밀어낸다", sub="The elution process · adsorption chromatography · eluent strength",
kw=["용리(溶離)", "용매 분자 vs 용질 분자 경쟁", "용리 세기↑ → 더 쉽게 밀어냄"],
sum="용리는 고정상에 붙잡힌 물질을 이동상으로 떼어내는 것. 흡착 크로마토그래피에서는 용매 분자가 용질과 고정상 자리를 두고 경쟁하고, 용리 세기가 큰 용매일수록 용질을 쉽게 밀어내.",
tr="""<p><b>용리(溶離, elution)</b>: 크로마토그래피에서 고정상에 유지된 물질을 이동상을 사용하여 고정상에서 탈리시키는 것</p>
<p>그림 (흡착 크로마토그래피): (a) 고정상에 흡착된 용질(▲), 위에서 용매(□)가 흐름 / (b) 고정상에 흡착된 용매, 탈착된 용질</p>
<ul><li>용매 분자는 고정상의 결합 자리를 두고 <b>용질 분자와 경쟁</b>한다</li>
<li>용매의 <b>용리 세기(eluent strength)가 클수록</b> 용질을 더 쉽게 밀어낸다</li></ul>""",
ex="""<ul><li><b>의자 뺏기 놀이</b>: 고정상 표면의 자리 = 의자, 용질과 용매 분자가 서로 앉으려 함. 용매가 의자에 앉는 힘(흡착 에너지)이 셀수록 용질이 자리를 잃고 이동상으로 → 빨리 나옴.</li>
<li>LC는 GC와 달리 <y>이동상이 적극적으로 분리에 참여</y>해. 그래서 이동상 조성으로 머무름을 조절하는 게 LC 최적화의 핵심.</li></ul>
<table class="t"><tr><th>용리 세기</th><th>머무름시간 (t<sub>r</sub>, k′)</th><th>분리</th></tr>
<tr><td>↑ (센 용매)</td><td>↓ 빨리 나옴</td><td>너무 세면 다 같이 나와 분리↓</td></tr>
<tr><td>↓ (약한 용매)</td><td>↑ 오래 머묾</td><td>분리는 좋아지지만 시간↑, 피크 넓어짐</td></tr></table>
<p class="note">GC에서 머무름을 조절하는 손잡이가 “온도(승온 프로그램)”라면, LC에선 “<b>용매 세기</b>(기울기 용리)”야 (23번).</p>"""),

# 20 (21)
dict(img=20, slide=21, title="크로마토그래피 과정 ⑰ — 용리 서열과 UV 차단 파장 (표 24-2)", sub="TABLE 24-2 Eluotropic series and UV cutoff wavelengths for adsorption on silica",
kw=["용리 서열", "용리 세기 ε° (펜테인 = 0)", "헥세인 0.01 · 에틸 아세테이트 0.48 · 메탄올 0.70", "UV 차단 파장"],
sum="맨 실리카 흡착에서 용매를 용리 세기(ε°) 순서로 나열한 표. 펜테인 0을 기준으로 극성이 클수록 ε°가 커(메탄올 0.70). UV 차단 파장은 그 아래에서 용매 자체가 빛을 흡수해 검출을 방해하는 파장이야.",
tr="""<p><b>표 24-2 실리카 흡착 크로마토그래피용 용매의 용리 서열과 UV 차단 파장</b> (용매 / 용리 세기 ε° / UV 차단 nm) — 극성 ↓ 증가</p>
<ul><li>펜테인 0.00 / 190 · <b>헥세인 0.01 / 195</b> (빨간 상자) · 헵테인 0.01 / 200 · 트라이클로로트라이플루오로에테인 0.02 / 231 · 톨루엔 0.22 / 284 · 클로로폼 0.26 / 245 · 다이클로로메테인 0.30 / 233 · 다이에틸 에터 0.43 / 215 · <b>에틸 아세테이트 0.48 / 256</b> (빨간 상자) · 메틸 t-뷰틸 에터 0.48 / 210 · 다이옥세인 0.51 / 215 · <b>아세토나이트릴 0.52 / 190</b> · 아세톤 0.53 / 330 · 테트라하이드로퓨란 0.53 / 212 · 2-프로판올 0.60 / 205 · <b>메탄올 0.70 / 205</b></li></ul>
<ul><li><b>용리 서열(eluotropic series)</b>: 주어진 흡착제에서 용질을 밀어내는 상대적 능력으로 용매를 순위 매긴 것</li>
<li><b>용리 세기 ε°</b>: 용매 흡착 에너지의 척도. 맨 실리카 흡착에서 펜테인을 0으로 정의</li>
<li><b>UV 차단(cutoff)</b>: 그 파장 아래에서는 용매 자체가 빛을 상당히 흡수하는 파장</li></ul>""",
ex="""<ul><li>빨간 상자 = <b>헥세인 / 에틸 아세테이트</b>: 학생들이 실리카겔 칼럼·TLC에서 쓴 바로 그 이동상. 에틸 아세테이트 비율을 올리면 ε°↑ → 화합물이 빨리 내려와 (Rf↑).</li>
<li>극성 실리카 표면에 <y>극성 용매일수록 강하게 흡착</y> → 용질을 잘 밀어냄 → ε°가 큼. 이건 <b>순상(실리카)</b> 기준!</li>
<li><pk>역상(C18)에서는 반대</pk>: 비극성 고정상이라 <b>덜 극성인 용매(ACN, MeOH)가 센 용매</b>, 물이 약한 용매 (22번).</li></ul>
<p><b>UV 차단 활용</b>: UV 검출을 220 nm에서 할 때 → 아세톤(330 nm), 톨루엔(284), 에틸 아세테이트(256)는 이동상으로 못 씀. <g>아세토나이트릴(190)과 메탄올(205)</g>이 역상 HPLC의 표준 유기 용매인 이유 중 하나야.</p>
<p class="note">중간고사 범위(Lecture 2) “용매 cutoff: 물 200, MeOH 210, 아세톤 330 nm”와 같은 개념이야.</p>"""),
]
