from parts import *
P = P1
E = [
# ───────────────────────────── 개념
dict(t="c", id="c-big", part=P, title="19장 큰 그림 — 전자는 내려가고, 양성자는 올라가고, ATP가 나온다", sub="Oxidative phosphorylation (산화적 인산화) · Slides 4–10",
core="NADH·FADH<sub>2</sub>가 가져온 전자가 호흡사슬을 따라 O<sub>2</sub>까지 ‘내리막’을 타고, 그 낙차 에너지로 H<sup>+</sup>를 퍼 올린 뒤, H<sup>+</sup>가 돌아올 때 ATP를 만든다.",
detail="""<p><b>Oxidative phosphorylation (옥시데이티브 포스포릴레이션, 산화적 인산화)</b> = 세포 호흡의 <b>3단계</b>. 1단계(해당·피루브산 산화·아세틸-CoA 생성), 2단계(시트르산 회로)에서 모아 둔 전자를 여기서 ‘현금(ATP)’으로 바꿔.</p>
<div class="term">＊[용어: 산화 = 전자를 잃음 / 환원 = 전자를 얻음 / 인산화 = ADP에 인산(P<sub>i</sub>)을 붙여 ATP로 만듦]</div>
<ul><li>전자 운반체: <b>NADH</b>(Nicotinamide Adenine Dinucleotide, 환원형 니코틴아마이드 아데닌 다이뉴클레오타이드)와 <b>FADH<sub>2</sub></b>(Flavin Adenine Dinucleotide, 환원형 플래빈 아데닌 다이뉴클레오타이드)</li>
<li>전자는 <b>respiratory chain (레스퍼러토리 체인, 호흡사슬 = 전자전달 사슬)</b>의 단백질들을 거쳐 진핵생물에선 <y>최종적으로 O<sub>2</sub>가 받는다</y> → H<sub>2</sub>O.</li>
<li>전자가 흐르며 나온 에너지 → <b>H<sup>+</sup> 기울기(gradient)</b> → ATP 합성.</li></ul>
<p>포도당 1개가 완전히 타면 <g>NADH 10개 + FADH<sub>2</sub> 2개</g>가 생겨 (해당 2 · 피루브산 산화 2 · 시트르산 회로 6 NADH / 2 FADH<sub>2</sub>).</p>
<table class="t"><tr><th>과정 (포도당 1개당)</th><th>직접 생성물</th><th>최종 ATP</th></tr>
<tr><td>해당과정 Glycolysis (글라이콜리시스)</td><td>2 NADH(세포질) + 2 ATP</td><td>3 또는 5 + 2</td></tr>
<tr><td>피루브산 산화 (×2)</td><td>2 NADH(기질)</td><td>5</td></tr>
<tr><td>시트르산 회로 (×2)</td><td>6 NADH + 2 FADH<sub>2</sub> + 2 ATP(GTP)</td><td>15 + 3 + 2</td></tr>
<tr><td colspan="2"><b>합계</b></td><td><b><pk>30 또는 32</pk></b></td></tr></table>""",
formula="""<span class="fx">NADH 1개 → 2.5 ATP &nbsp;|&nbsp; FADH<sub>2</sub> 1개 → 1.5 ATP</span><br>
세포질 NADH 2개가 어떤 셔틀로 들어오느냐에 따라 3(글리세롤 3-인산 셔틀: 2×1.5) 또는 5(말산-아스파르트산 셔틀: 2×2.5) → 그래서 <b>30 또는 32</b>.""",
example="""<b>Q.</b> 포도당 1개 → ATP 32개를 직접 세어 보자 (말산-아스파르트산 셔틀).<br>
<b>Step 1</b> NADH 개수: 해당 2 + 피루브산 2 + 회로 6 = 10개 → 10 × 2.5 = <b>25</b><br>
<b>Step 2</b> FADH<sub>2</sub> 2개 × 1.5 = <b>3</b><br>
<b>Step 3</b> 기질수준 인산화(ATP를 바로 만드는 것): 해당 2 + 회로 2 = <b>4</b><br>
<b>Step 4</b> 25 + 3 + 4 = <b>32</b>. 👉 셔틀이 글리세롤 3-인산이면 세포질 NADH 2개가 1.5씩만 → 32 − 2 = <b>30</b>.""",
side=[("img", 7, "원본 슬라이드 7 — Table 19-5 포도당 완전 산화의 ATP 수율", 190),
      ("ana", "<b>물레방아 발전소</b>를 떠올려. 전자 = 산 위에서 굴러 내려오는 공, 공이 떨어질 때마다 펌프가 물(H<sup>+</sup>)을 댐 위로 퍼 올린다. 댐 물이 물레방아(ATP 합성효소)를 돌리며 쏟아질 때 전기(ATP)가 나와."),
      ("trap", "“포도당 1개 = 36~38 ATP”는 옛 교과서 숫자(NADH 3, FADH<sub>2</sub> 2로 계산). 이 강의 기준은 <b>2.5 / 1.5 → 30 또는 32</b>.")],
one="전자 ↓ (NADH → O₂) · 양성자 ↑ (기질 → 막사이공간) · ATP ← 양성자가 돌아올 때. 포도당 하나 = 30/32 ATP!"),

dict(t="c", id="c-carrier", part=P, title="보편적 전자 수용체 — NAD⁺와 FAD/FMN", sub="(1) Electrons are funneled to universal electron acceptors · Slides 8–9",
core="여러 탈수소효소가 뜯어낸 전자는 일단 <b>NAD<sup>+</sup>(또는 NADP<sup>+</sup>)</b>나 <b>FMN·FAD</b>라는 ‘공용 장바구니’에 담겨 호흡사슬로 깔때기처럼 모인다.",
detail="""<ul><li><b>NAD<sup>+</sup> / NADP<sup>+</sup></b>: 니코틴아마이드 고리가 <b>하이드라이드 이온(:H<sup>−</sup>, 전자 2개 + 양성자 1개)</b>을 받아 NADH가 됨. 효소에 느슨하게 붙어 자유롭게 돌아다니는 ‘수용성 운반체’.</li>
<li>NADH는 <y>340 nm 빛을 흡수</y>하고 NAD<sup>+</sup>는 안 함 → 340 nm 흡광도로 반응을 실시간 추적 가능.</li>
<li><b>FMN</b>(Flavin MonoNucleotide, 플래빈 모노뉴클레오타이드)·<b>FAD</b>: 아이소알록사진(isoalloxazine) 고리가 전자를 받음. 단백질에 <b>단단히(때로는 공유결합으로) 붙어 있는 보결분자단</b>.</li>
<li>플래빈은 전자를 <b>1개씩도, 2개씩도</b> 받을 수 있어: FAD → FADH·(반퀴논, semiquinone, 전자 1개) → FADH<sub>2</sub>(완전 환원). → 2전자 운반체(NADH)와 1전자 운반체(Fe-S, 시토크롬)를 잇는 <b>변압기</b> 역할.</li>
<li><pk>FAD·FMN의 표준환원전위(E′°)는 어떤 단백질에 붙어 있느냐에 따라 달라진다</pk> (슬라이드 9 빨간 글씨).</li></ul>
<div class="term">＊[용어: 보결분자단(prosthetic group, 프로스테틱 그룹) = 단백질에 단단히 붙어서 떨어지지 않는 비단백질 도우미 분자]</div>
<div class="term">＊[용어: 표준환원전위 E′° = “전자를 얼마나 끌어당기나” 점수. 높을수록(+) 전자를 잘 받고, 낮을수록(−) 잘 내준다]</div>""",
side=[("img", 9, "원본 슬라이드 9 — FAD/FMN의 산화·반퀴논·완전환원 형태", 200),
      ("ana", "NAD<sup>+</sup>는 <b>택배 트럭</b>(떨어져서 돌아다님), FAD는 <b>공장에 붙박이 컨베이어</b>(효소에 고정). 둘 다 전자를 실어 나르지만, FAD는 낱개(1개)로도 나눠 담을 수 있어."),
      ("tip", "“NADH만 340 nm 흡수” · “FAD 전위는 단백질에 따라 다름” · “플래빈 = 1전자/2전자 둘 다” — 객관식 보기 단골.")],
one="NAD⁺ = 돌아다니는 2전자 트럭(340 nm), FAD/FMN = 효소에 붙박이, 1·2전자 둘 다 OK인 변압기."),

dict(t="c", id="c-qcytfes", part=P, title="막 속 전자 운반체 3인방 — 유비퀴논 · 시토크롬 · 철-황 단백질", sub="(2) Electrons pass through a series of membrane-bound carriers · Slides 14–15, 20–21",
core="호흡사슬에서 전자를 나르는 건 <b>유비퀴논(Q)</b>, <b>시토크롬(헴)</b>, <b>철-황(Fe-S) 단백질</b> 세 종류. Q만 2전자+양성자를 함께 나르고, 나머지 둘은 전자를 <b>1개씩</b> 나른다.",
detail="""<p><b>① Ubiquinone (유비퀴논) = Coenzyme Q (코엔자임 큐, Q)</b></p>
<ul><li><y>지용성</y> 벤조퀴논 + 긴 아이소프레노이드 꼬리 → 막 지질 속을 <b>자유롭게 헤엄침</b>.</li>
<li>Q + e<sup>−</sup> + H<sup>+</sup> → ·QH(반퀴논 라디칼) + e<sup>−</sup> + H<sup>+</sup> → <b>QH<sub>2</sub>(ubiquinol, 유비퀴놀)</b>. 전자 2개를 받으면 <b>양성자도 2개</b> 집어 듦 → 막 한쪽에서 다른 쪽으로 <b>전자 + 양성자</b>를 함께 운반.</li></ul>
<p><b>② Cytochrome (사이토크롬, 시토크롬) a · b · c</b> — 철을 품은 <b>헴(heme)</b> 보결분자단. Fe<sup>3+</sup> ⇌ Fe<sup>2+</sup>로 전자 <b>1개</b>씩. 헴 종류로 a, b, c 구분 (헴 c만 Cys와 <b>공유결합</b>). 환원형 cyt c는 α(≈550 nm)·β·γ(Soret, ≈415 nm) 흡수띠가 뚜렷.</p>
<p><b>③ Iron-sulfur (Fe-S, 철-황) protein</b> — Fe-4S(=Fe 1개), 2Fe-2S, 4Fe-4S. 철이 Cys의 S와 무기 S에 묶임. <y>전자 1개씩</y> 전달. Complex I 등 여러 곳에 있고, Complex III의 것은 <b>Rieske (리스키) 철-황 단백질</b>(His 2개가 배위).</p>
<div class="term">＊[용어: 아이소프레노이드 = 탄소 5개짜리 ‘아이소프렌’ 블록을 기차처럼 이어 붙인 기름진 꼬리. 사람 Q는 10개(Q<sub>10</sub>)]</div>
<div class="term">＊[용어: 헴(heme) = 포르피린 고리 가운데 철 원자가 박힌 납작한 분자. 헤모글로빈의 빨간색도 헴]</div>""",
side=[("img", 15, "원본 슬라이드 15 — Q → ·QH → QH₂ (전자 2개 + H⁺ 2개)", 175),
      ("img", 14, "원본 슬라이드 14 — Fe-S 중심 3종류 (전자 1개씩)", 120),
      ("ana", "Q는 막 속 <b>셔틀버스</b>(승객 = 전자 + 양성자, 막 양쪽을 오감). 시토크롬·Fe-S는 <b>릴레이 바통</b> — 한 번에 하나씩만 건넨다.")],
one="Q = 지용성 셔틀(2e⁻ + 2H⁺) · 시토크롬 = 헴 철(1e⁻) · Fe-S = Cys에 묶인 철(1e⁻)."),

dict(t="c", id="c-c1", part=P, title="Complex I — NADH 탈수소효소: 전자 2개로 양성자 4개를 퍼 올리는 L자 펌프", sub="NADH:ubiquinone oxidoreductase (NADH 탈수소효소) · Slides 11–13",
core="Complex I은 NADH의 전자 2개를 <b>FMN → Fe-S 사슬 → Q</b>로 넘기면서, 그 에너지로 기질의 H<sup>+</sup> <b>4개</b>를 막사이공간으로 퍼낸다.",
detail="""<ul><li>모양: 기질 쪽으로 뻗은 팔(matrix arm) + 막에 박힌 팔(membrane arm) → <b>L자</b>. 포유류 43개 소단위체(세균 14), 850 kDa, 보결분자단 <b>FMN, Fe-S</b>.</li>
<li>전자 경로: NADH → <b>FMN</b> → 여러 Fe-S 중심 → 마지막 <b>N-2</b> → Q → QH<sub>2</sub></li>
<li>두 가지 일을 동시에 (짝지어진 반응):<br>(1) NADH + H<sup>+</sup> + Q → NAD<sup>+</sup> + QH<sub>2</sub> (산화환원, 에너지 방출)<br>(2) 기질 → 막사이공간으로 <b>H<sup>+</sup> 4개</b> 이동 (에너지 사용) = <b>양성자 펌프</b></li>
<li>펌프 원리(슬라이드 13): Q가 환원될 때의 <b>구조 변화</b>가 막 팔에 ‘전기 펄스’를 보내고, 막 팔에 줄지은 양성자화 가능한 잔기(염기성·산성 아미노산)들이 차례로 H<sup>+</sup>를 넘긴다.</li></ul>
<div class="term">＊[용어: N side(Negative, 음성 쪽) = 기질(matrix) 쪽 / P side(Positive, 양성 쪽) = 막사이공간(intermembrane space) 쪽. H<sup>+</sup>를 퍼내서 P쪽이 + 가 됨]</div>
<div class="term">＊[용어: oxidoreductase(옥시도리덕테이스, 산화환원효소) = 한 분자는 산화하고 다른 분자는 환원시키는 효소]</div>""",
formula="""<span class="fx">NADH + 5H<sup>+</sup><sub>N</sub> + Q → NAD<sup>+</sup> + QH<sub>2</sub> + 4H<sup>+</sup><sub>P</sub></span><br>
5H<sup>+</sup><sub>N</sub> = Q 환원에 쓰이는 1개(+NADH의 H) + 퍼내는 4개. 오른쪽 4H<sup>+</sup><sub>P</sub> = 막사이공간으로 나간 양성자.<br>
억제제: <b>rotenone(로테논, 살충제·물고기 독)</b>, <b>amytal(아미탈, 바르비투르산염)</b>, <b>piericidin A(피에리시딘 A)</b> → Fe-S에서 Q로 가는 길 차단.""",
side=[("img", 12, "원본 슬라이드 12 — Complex I: (1) NADH → Q, (2) 4H⁺ 펌프", 200),
      ("ana", "<b>수동 펌프 달린 정수기</b>: 손잡이(전자 2개)를 한 번 누르면 물(H<sup>+</sup>) 4컵이 위층으로 올라간다. 손잡이 쪽(기질 팔)과 펌프 쪽(막 팔)이 L자로 연결."),
      ("trap", "Complex I이 펌프하는 H<sup>+</sup> 수는 <b>4</b> (전자 2개당). III도 4, IV는 2 → 합 10.")],
one="Complex I = NADH → FMN → Fe-S(N-2) → Q, 그리고 H⁺ 4개 펌프. 로테논이 막는다!"),

dict(t="c", id="c-c2", part=P, title="Complex II — 숙신산 탈수소효소: 펌프 없는 옆문 입구", sub="Succinate dehydrogenase · Slides 16–17",
core="Complex II는 시트르산 회로의 숙신산을 산화해 전자를 <b>FAD → Fe-S → Q</b>로 넘긴다. <pk>양성자를 퍼내지 않는다</pk> → FADH<sub>2</sub> 경로가 ATP를 덜 만드는 이유.",
detail="""<ul><li>시트르산 회로 효소 중 <b>유일하게 막에 박힌</b> 효소. 4개 소단위체, 보결분자단 <b>FAD(공유결합), Fe-S 3개, 헴 b</b>.</li>
<li>경로: 숙신산 → 푸마르산 (전자 2개) → <b>FAD</b> → <b>Fe-S 3개</b> → Q 결합부위 → QH<sub>2</sub></li>
<li><b>헴 b의 역할</b>: 전자의 직접 경로에 있지 않지만, 숙신산에서 새는 전자가 O<sub>2</sub>로 가서 <b>활성산소(ROS: H<sub>2</sub>O<sub>2</sub>, 초과산화물 O<sub>2</sub><sup>−</sup>)</b>가 되는 걸 막는 안전장치(슬라이드 16).</li>
<li><b>Q로 모이는 다른 입구들</b>(슬라이드 17) — 모두 FAD 거쳐 Q로, 그래서 모두 Complex I을 건너뜀:<br>
· 지방산 β-산화의 <b>acyl-CoA dehydrogenase(아실-CoA 탈수소효소)</b> → ETF(Electron-Transferring Flavoprotein, 전자전달 플래빈단백질) → ETF:Q 산화환원효소 → Q<br>
· 세포질 글리세롤 3-인산 → 미토콘드리아 <b>glycerol 3-phosphate dehydrogenase(글리세롤 3-인산 탈수소효소)</b>(막 바깥면) → Q</li></ul>
<div class="term">＊[용어: ROS(Reactive Oxygen Species, 활성산소종) = 산소가 전자를 하나둘 덜 받아서 생긴, 아무거나 공격하는 위험한 산소 분자들]</div>""",
side=[("img", 17, "원본 슬라이드 17 — NADH·숙신산·지방아실-CoA·글리세롤 3-인산이 모두 Q로 모인다", 210),
      ("ana", "Q는 <b>고속도로 합류 지점</b>. Complex I은 유료 정문(통과할 때 H<sup>+</sup> 4개 펌프), Complex II·ETF·글리세롤 3-인산 탈수소효소는 <b>펌프 없는 옆문</b> — 그래서 같은 전자 2개라도 ATP가 덜 나온다."),
      ("tip", "“양성자 펌프가 <b>아닌</b> 복합체는?” → <b>Complex II</b>. TB 단골.")],
one="Complex II = 숙신산 → FAD → Fe-S → Q. 펌프 0개! 헴 b는 ROS 새는 걸 막는 안전장치."),

dict(t="c", id="c-c3", part=P, title="Complex III와 Q 회로 — 2전자를 1전자로 쪼개며 양성자 4개 내보내기", sub="Cytochrome bc₁ complex (시토크롬 bc₁ 복합체) · Q cycle · Slides 18–19",
core="Complex III는 QH<sub>2</sub>의 전자를 <b>시토크롬 c</b>로 넘긴다. QH<sub>2</sub>는 전자 2개, cyt c는 1개만 받으므로 <b>Q 회로</b>로 나눠 처리하며 P쪽으로 H<sup>+</sup> <b>4개</b>를 내보낸다.",
detail="""<ul><li>이름: <b>ubiquinone:cytochrome c oxidoreductase</b>. 이량체, 단량체당 11개 소단위체. 핵심 = 시토크롬 b(헴 b<sub>L</sub>, 헴 b<sub>H</sub>), 시토크롬 c<sub>1</sub>, <b>Rieske 철-황 단백질</b>(2Fe-2S).</li>
<li>Q 결합 자리 2곳: <b>Q<sub>P</sub></b> = 막사이공간(P) 쪽 / <b>Q<sub>N</sub></b> = 기질(N) 쪽 (슬라이드 18).</li>
<li><b>Q cycle (큐 사이클)</b> 1단계: Q<sub>P</sub>에서 QH<sub>2</sub> 1개 산화 → 전자 1은 Rieske → cyt c<sub>1</sub> → cyt c, 전자 2는 b<sub>L</sub> → b<sub>H</sub> → Q<sub>N</sub>의 Q를 ·Q<sup>−</sup>로. H<sup>+</sup> 2개 → P쪽.<br>
2단계: 두 번째 QH<sub>2</sub>가 같은 일 → Q<sub>N</sub>의 ·Q<sup>−</sup>가 전자 + 기질 H<sup>+</sup> 2개를 받아 QH<sub>2</sub>로 재생.</li>
<li>결과: QH<sub>2</sub> 2개 산화, 1개 재생 → <b>순 1개 QH<sub>2</sub>가 전자 2개를 cyt c 2개에</b> 주고, P쪽에 H<sup>+</sup> 4개.</li>
<li><b>Cytochrome c</b>: 막사이공간의 작은 <b>수용성</b> 단백질(13 kDa, 헴 c). III → IV로 전자 1개씩 배달.</li></ul>
<div class="term">＊[용어: 이량체(dimer) = 똑같은 단위 두 개가 짝지어 한 덩어리로 일함]</div>""",
formula="""<span class="fx">QH<sub>2</sub> + 2 cyt c<sub>1</sub>(산화) + 2H<sup>+</sup><sub>N</sub> → Q + 2 cyt c<sub>1</sub>(환원) + 4H<sup>+</sup><sub>P</sub></span><br>
억제제: <b>antimycin A(안티마이신 A)</b> — cyt b → cyt c<sub>1</sub> 전달(Q<sub>N</sub> 자리) 차단 (Table 19-4).""",
side=[("img", 19, "원본 슬라이드 19 — Q 회로 두 단계와 순반응식", 220),
      ("ana", "Q 회로 = <b>2인용 자전거 승객을 1인용 킥보드로 나눠 태우기</b>. 한 명(전자1)은 바로 cyt c 킥보드로, 다른 한 명(전자2)은 대기실(Q<sub>N</sub>)에서 다음 손님과 합쳐 다시 2인용(QH<sub>2</sub>)으로 재출발 → 그 사이 H<sup>+</sup>가 2배로 나간다."),
      ("trap", "순반응식에서 <b>왼쪽은 2H<sup>+</sup><sub>N</sub>, 오른쪽은 4H<sup>+</sup><sub>P</sub></b>. 숫자를 바꿔 쓰는 빈칸 문제 주의.")],
one="Complex III = QH₂ → (Q 회로) → cyt c. 2전자를 1전자 둘로 쪼개며 H⁺ 4개 → P쪽. 안티마이신 A가 막는다."),

dict(t="c", id="c-c4", part=P, title="Complex IV — 시토크롬 산화효소: 산소에게 전자 4개를 몰아주는 종착역", sub="Cytochrome oxidase (시토크롬 c 산화효소) · Slides 22–23",
core="Complex IV는 cyt c 4개의 전자를 모아 O<sub>2</sub> 1분자를 물 2분자로 환원한다. 전자 경로는 <b>cyt c → Cu<sub>A</sub> → 헴 a → 헴 a<sub>3</sub>–Cu<sub>B</sub>(Fe-Cu 중심) → O<sub>2</sub></b>.",
detail="""<ul><li>소 미토콘드리아: <b>13개 소단위체</b>, 핵심 4개.<br>
· 소단위체 <b>II</b>: Cu 이온 2개가 Cys와 결합한 <b>Cu<sub>A</sub> 이핵 중심(binuclear center)</b> — cyt c에서 전자를 처음 받음<br>
· 소단위체 <b>I</b>: <b>헴 a, 헴 a<sub>3</sub>, Cu<sub>B</sub></b> — 헴 a<sub>3</sub>와 Cu<sub>B</sub>가 함께 <b>Fe-Cu 이핵 중심</b>(O<sub>2</sub>가 붙는 곳)<br>
· 소단위체 <b>III</b>: 소단위체 II를 통한 <b>빠른 양성자 이동</b>에 필수</li>
<li>O<sub>2</sub> → O<sub>2</sub><sup>2−</sup> → 2H<sub>2</sub>O: 전자 4개가 <b>중간 산물을 놓치지 않고</b> 한 자리에 차곡차곡 모여야 안전(새면 ROS).</li>
<li>H<sup>+</sup> 사용: 기질 H<sup>+</sup> 8개 중 <b>4개는 물 만드는 재료(substrate)</b>, <b>4개는 P쪽으로 펌프</b>. 전자 2개 기준 → 2H<sup>+</sup> 펌프.</li></ul>
<div class="term">＊[용어: 이핵 중심(binuclear center) = 금속 원자 두 개가 바짝 붙어 한 팀으로 전자를 다루는 자리]</div>""",
formula="""<span class="fx">4 cyt c(환원) + 8H<sup>+</sup><sub>N</sub> + O<sub>2</sub> → 4 cyt c(산화) + 4H<sup>+</sup><sub>P</sub> + 2H<sub>2</sub>O</span><br>
억제제: <b>CN<sup>−</sup>(사이안화물, 청산가리)</b>, <b>CO(일산화탄소)</b>, (N<sub>3</sub><sup>−</sup> 아자이드) → 헴 a<sub>3</sub>–Cu<sub>B</sub>에 O<sub>2</sub> 대신 붙음.""",
side=[("img", 23, "원본 슬라이드 23 — cyt c → Cu_A → 헴 a → Fe-Cu 중심, 4e⁻ → 4H⁺ 펌프", 215),
      ("ana", "<b>구슬 4개를 모아야 열리는 금고</b>(O<sub>2</sub>). 직원(Cu<sub>A</sub> → 헴 a)이 cyt c 택배를 하나씩 받아 금고 앞(Fe-Cu 중심)에 쌓고, 4개가 차면 물 2병으로 바꿔 내보낸다."),
      ("trap", "8H<sup>+</sup><sub>N</sub>을 전부 펌프로 착각 ❌ → <b>4개는 물(재료), 4개만 펌프</b>.")],
one="Complex IV = cyt c → Cu_A → 헴 a → 헴 a₃·Cu_B → O₂ → 2H₂O. 전자 4개당 H⁺ 4개 펌프. CN⁻·CO가 막는다."),

dict(t="c", id="c-sum", part=P, title="호흡사슬 총정리 — 전자 2개로 양성자 10개, 에너지 −220 kJ", sub="Summary of electron & proton flow · ΔG′° = −nℱΔE′° · respirasome · Slides 24–25, 31",
core="NADH 1개의 전자 2개가 I → Q → III → cyt c → IV → O<sub>2</sub>를 지나면 H<sup>+</sup> <b>10개</b>(4+4+2)가 P쪽으로 나가고, 자유에너지 <b>약 −220 kJ/mol</b>이 방출된다.",
detail="""<table class="t"><tr><th>복합체</th><th>이름</th><th>보결분자단</th><th>H<sup>+</sup>/2e<sup>−</sup></th></tr>
<tr><td>I</td><td>NADH dehydrogenase</td><td>FMN, Fe-S</td><td><b>4</b></td></tr>
<tr><td>II</td><td>Succinate dehydrogenase</td><td>FAD, Fe-S (헴 b)</td><td><b>0</b></td></tr>
<tr><td>III</td><td>Cytochrome bc<sub>1</sub></td><td>헴 b·c<sub>1</sub>, Fe-S</td><td><b>4</b></td></tr>
<tr><td>cyt c</td><td>(수용성, 복합체 아님)</td><td>헴 c</td><td>—</td></tr>
<tr><td>IV</td><td>Cytochrome oxidase</td><td>헴 a·a<sub>3</sub>, Cu<sub>A</sub>, Cu<sub>B</sub></td><td><b>2</b></td></tr></table>
<p>NADH에서 시작: 4 + 4 + 2 = <g>10 H<sup>+</sup></g> / 숙신산(FADH<sub>2</sub>)에서 시작: 0 + 4 + 2 = <g>6 H<sup>+</sup></g></p>
<p><b>Respirasome (레스퍼러좀, 호흡초복합체)</b>: 복합체들이 따로 떠다니지 않고 <b>I+III</b> 또는 <b>III+IV</b>처럼 뭉쳐 있어 전자를 빨리, 새지 않게 넘김(슬라이드 24).</p>
<div class="term">＊[용어: ℱ(패러데이 상수) = 전자 1몰이 가진 전하량 = 96.5 kJ/V·mol. n = 옮겨지는 전자 수]</div>""",
formula="""<span class="fx">NADH + H<sup>+</sup> + ½O<sub>2</sub> → NAD<sup>+</sup> + H<sub>2</sub>O</span><br>
<span class="fx">NADH + 11H<sup>+</sup><sub>N</sub> + ½O<sub>2</sub> → NAD<sup>+</sup> + 10H<sup>+</sup><sub>P</sub> + H<sub>2</sub>O</span><br>
<span class="fx">ΔG′° = −nℱΔE′°</span> &nbsp; ΔE′° = E′°(받는 쪽) − E′°(주는 쪽)""",
example="""<b>Q.</b> NADH → O<sub>2</sub>의 ΔG′°는? (E′°: NAD<sup>+</sup>/NADH = −0.320 V, ½O<sub>2</sub>/H<sub>2</sub>O = +0.816 V)<br>
<b>Step 1</b> 전자 받는 쪽(O<sub>2</sub>) − 주는 쪽(NADH): ΔE′° = 0.816 − (−0.320) = <b>1.136 V</b> 👉 왜? 전자는 낮은 전위 → 높은 전위로 ‘내리막’.<br>
<b>Step 2</b> n = 2 (NADH는 전자 2개), ℱ = 96.5 kJ/V·mol<br>
<b>Step 3</b> ΔG′° = −2 × 96.5 × 1.136 ≈ <b>−219 kJ/mol ≈ −220 kJ/mol</b> (음수 = 저절로 일어나는 반응, 에너지 방출)""",
side=[("img", 25, "원본 슬라이드 25 — 네 복합체를 지나는 전자·양성자 흐름 총정리", 175),
      ("ana", "<b>10층 계단을 내려오는 공 2개</b>: I층(4칸 펌프) → III층(4칸) → IV층(2칸). FADH<sub>2</sub>는 I층을 건너뛰고 Q에서 탔으니 6칸만."),
      ("tip", "숫자 3종 세트: <b>H<sup>+</sup> 10(NADH) / 6(숙신산)</b>, <b>ΔE′° 1.14 V</b>, <b>ΔG′° −220 kJ/mol</b>.")],
one="I(4) + III(4) + IV(2) = 10 H⁺. ΔG = −nℱΔE = −2 × 96.5 × 1.14 ≈ −220 kJ/mol."),

dict(t="c", id="c-pmf", part=P, title="양성자 구동력과 화학삼투 모델 — 댐에 갇힌 물의 두 가지 힘", sub="Proton-motive force (양성자 구동력) · Chemiosmotic model (화학삼투 모델, Mitchell) · Slides 26–28",
core="퍼낸 H<sup>+</sup>는 <b>농도 차(ΔpH, 화학적 퍼텐셜)</b>와 <b>전하 차(Δψ, 전기적 퍼텐셜)</b>를 함께 만든다. 이 합 = <b>양성자 구동력</b>, H<sup>+</sup>가 ATP 합성효소를 통해 기질로 돌아올 때 ATP가 만들어진다.",
detail="""<ul><li><b>Chemiosmotic model (케미오스모틱 모델, 화학삼투 모델)</b> — Peter Mitchell (피터 미첼, 1978 노벨상): 전자전달과 ATP 합성은 <b>막을 가로지른 H<sup>+</sup> 기울기</b>로 연결(짝지음, coupling)되어 있다.</li>
<li>P쪽(막사이공간): H<sup>+</sup> 많음, <b>산성 · + 전하</b> / N쪽(기질): H<sup>+</sup> 적음, <b>알칼리성 · − 전하</b>.</li>
<li><b>미토콘드리아 내막</b>은 H<sup>+</sup>를 포함한 대부분의 이온·작은 분자를 <y>통과시키지 않음</y> → 기울기가 유지됨. (외막은 포린(porin) 통로로 작은 분자 자유 통과)</li>
<li>H<sup>+</sup>는 <b>수동적으로(passively)</b> ATP 합성효소의 통로로만 돌아옴 → ATP 합성.</li>
<li>미토콘드리아 기질에는 해당과정을 <b>제외한</b> 모든 연료 산화 경로가 있다: 피루브산 탈수소효소, 시트르산 회로, β-산화, 아미노산 산화 (슬라이드 28).</li></ul>
<div class="term">＊[용어: 퍼텐셜(potential) = 무언가를 움직이려는 ‘밀어내는 힘’. 농도 차도, 전하 차도 이온을 밀어낸다]</div>""",
formula="""<span class="fx">ΔG = RT ln(C<sub>2</sub>/C<sub>1</sub>) + Zℱ Δψ = 2.3RT ΔpH + ℱ Δψ</span><br>
C<sub>2</sub> = P쪽 [H<sup>+</sup>], C<sub>1</sub> = N쪽 [H<sup>+</sup>], Z = 이온 전하(H<sup>+</sup>는 1), R = 8.315 J/mol·K, T = 절대온도, Δψ = 막전위(V)<br>
첫째 항 = <b>화학적</b>(농도) 에너지, 둘째 항 = <b>전기적</b>(전하) 에너지""",
example="""<b>Q.</b> 활발히 호흡하는 미토콘드리아: ΔpH = 0.75, Δψ = 0.15–0.2 V. 25 °C에서 H<sup>+</sup> 1몰을 퍼내는 데 드는 ΔG는?<br>
<b>Step 1</b> 2.3RT = 2.3 × 8.315 J × 298 K ≈ 5.7 kJ/mol → 5.7 × 0.75 ≈ <b>4.3 kJ/mol</b> (화학 항)<br>
<b>Step 2</b> ℱΔψ = 96.5 × 0.15~0.2 ≈ <b>14.5~19.3 kJ/mol</b> (전기 항)<br>
<b>Step 3</b> 합 ≈ <b>약 19 kJ/mol</b> (H<sup>+</sup> 1몰당). 👉 미토콘드리아에선 <b>전기 항이 더 크다</b>.""",
side=[("img", 27, "원본 슬라이드 27 — 화학적 퍼텐셜 ΔpH + 전기적 퍼텐셜 Δψ = 양성자 구동력", 190),
      ("ana", "<b>댐</b>: 위쪽 물 높이 차(농도 차, ΔpH) + 물에 실린 ‘자석의 끌림’(전하 차, Δψ). 둘 다 물을 아래로 밀어내. 수문 = ATP 합성효소, 물레방아가 돌며 ATP를 찍어낸다."),
      ("trap", "“H<sup>+</sup>가 ATP 합성효소를 지날 때 에너지를 <b>소모</b>” ❌ — 기울기를 따라 <b>내려가며 에너지를 방출</b>하고, 그걸 ATP 합성에 쓴다.")],
one="양성자 구동력 = 2.3RTΔpH(농도) + ℱΔψ(전하). P쪽 산성·(+), N쪽 알칼리·(−). 미첼의 화학삼투!"),

dict(t="c", id="c-order", part=P, title="전자 운반체의 순서는 어떻게 알았나 — 세 가지 실험", sub="Determining the sequence: reduction potentials · oxidation rate · inhibitors · Slides 30–36",
core="순서 = <b>NADH → Q → cyt b → cyt c<sub>1</sub> → cyt c → cyt (a+a<sub>3</sub>) → O<sub>2</sub></b>. ① 환원전위가 낮은 것 → 높은 것 순, ② O<sub>2</sub>를 넣으면 O<sub>2</sub>에 가까운 것부터 먼저 산화, ③ 억제제 앞은 환원·뒤는 산화.",
detail="""<p><b>먼저 쪼개기</b>(슬라이드 30): 미토콘드리아를 <b>digitonin(디지토닌)</b>으로 처리 → 외막 제거, 삼투 파열 → 내막 조각 → 세제로 녹여 <b>이온교환 크로마토그래피</b>로 Complex I·II·III·IV·ATP 합성효소를 따로 분리 → 각각 무슨 반응을 하는지 시험관에서 확인.</p>
<p><b>방법 ① 환원전위 순서</b>(Table 19-2): 전자는 E′°가 <b>낮은(−) 곳 → 높은(+) 곳</b>으로 흐른다.</p>
<table class="t"><tr><th>반쪽 반응</th><th>E′° (V)</th></tr>
<tr><td>NAD<sup>+</sup>/NADH</td><td>−0.320</td></tr><tr><td>Q/QH<sub>2</sub> (유비퀴논)</td><td>+0.045</td></tr>
<tr><td>cyt b</td><td>+0.077</td></tr><tr><td>cyt c<sub>1</sub></td><td>+0.22</td></tr><tr><td>cyt c</td><td>+0.254</td></tr>
<tr><td>cyt a / a<sub>3</sub></td><td>+0.29 / +0.35</td></tr><tr><td>½O<sub>2</sub>/H<sub>2</sub>O</td><td>+0.816</td></tr></table>
<p><b>방법 ② 산화 속도</b>: 모든 운반체를 먼저 환원시킨 뒤 O<sub>2</sub>를 넣으면 <y>O<sub>2</sub>에 가장 가까운 운반체가 가장 먼저</y> 산화된다.</p>
<p><b>방법 ③ 억제제</b>: 억제 지점 <b>앞(위쪽)은 환원 상태로 쌓이고</b>, <b>뒤(아래쪽)는 산화 상태</b>로 남는다 → 막힌 위치 파악.</p>
<div class="term">＊[용어: 억제제(inhibitor) = 특정 지점에 끼어 전자 흐름을 막는 ‘바리케이드’ 분자]</div>""",
side=[("img", 35, "원본 슬라이드 35 — 로테논 · 안티마이신 A · CN⁻/CO: 앞은 환원(파랑), 뒤는 산화(분홍)", 165),
      ("card", """<table class="t" style="margin:0"><tr><th>억제제</th><th>막는 곳</th></tr>
<tr><td>Rotenone 로테논 · Amytal 아미탈 · Piericidin A</td><td>Complex I (Fe-S → Q)</td></tr>
<tr><td>Antimycin A 안티마이신 A</td><td>Complex III (cyt b → c<sub>1</sub>)</td></tr>
<tr><td>CN<sup>−</sup> · CO</td><td>Complex IV</td></tr>
<tr><td>Oligomycin 올리고마이신 · Venturicidin</td><td>ATP 합성효소 F<sub>o</sub></td></tr>
<tr><td>DNP · FCCP</td><td>짝풀림(H<sup>+</sup> 운반)</td></tr>
<tr><td>Atractyloside 아트락틸로사이드</td><td>ATP-ADP 교환(ANT)</td></tr></table>""", "📋 Table 19-4 억제제 한눈에"),
      ("ana", "<b>꽉 막힌 도로</b>: 사고 지점 앞에는 차(전자)가 줄줄이 쌓이고(환원), 뒤쪽은 텅 빈다(산화).")],
one="전위 낮음 → 높음 순서. 억제제 앞 = 환원(차 막힘), 뒤 = 산화(텅 빔). 로테논 I · 안티마이신 III · CN⁻ IV."),

dict(t="c", id="c-shuttle", part=P, title="세포질 NADH의 입국 심사 — 말산-아스파르트산 셔틀 vs 글리세롤 3-인산 셔틀", sub="Shuttle systems for cytosolic NADH · Slides 37–39",
core="미토콘드리아 내막은 <b>NADH를 통과시키지 않는다</b>. 그래서 전자만 ‘다른 분자에 태워’ 들여보낸다: 간·심장·신장은 <b>말산-아스파르트산 셔틀(2.5 ATP)</b>, 골격근·뇌는 <b>글리세롤 3-인산 셔틀(1.5 ATP)</b>.",
detail="""<p><b>① Malate-aspartate shuttle (말산-아스파르트산 셔틀)</b> — 간, 신장, 심장</p>
<ol><li>세포질: OAA(옥살로아세트산) + NADH → <b>말산</b> + NAD<sup>+</sup> (말산 탈수소효소)</li>
<li>말산-α-케토글루타르산 수송체로 말산이 기질로 들어감</li>
<li>기질: 말산 + NAD<sup>+</sup> → OAA + <b>NADH</b> → Complex I로 (2.5 ATP)</li>
<li>OAA는 막을 못 지나니 아스파르트산 아미노기전이효소가 <b>아스파르트산</b>으로 바꿔 글루탐산-아스파르트산 수송체로 다시 내보냄 → 세포질에서 다시 OAA</li></ol>
<p>순결과: NADH(세포질, P) → NADH(기질, N). <b>가역적</b>, 에너지 손실 없음.</p>
<p><b>② Glycerol 3-phosphate shuttle (글리세롤 3-인산 셔틀)</b> — 골격근, 뇌</p>
<ol><li>세포질: DHAP(다이하이드록시아세톤 인산) + NADH → 글리세롤 3-인산 (세포질 글리세롤 3-인산 탈수소효소)</li>
<li>내막 바깥면의 <b>미토콘드리아 글리세롤 3-인산 탈수소효소(FAD)</b>가 산화 → FADH<sub>2</sub> → <b>Q</b> → Complex III</li></ol>
<p>Complex I을 건너뛰므로 <pk>1.5 ATP / 2e<sup>−</sup></pk>. 대신 막을 ‘통과’할 필요가 없어 <b>빠르다</b>.</p>
<div class="term">＊[용어: 셔틀(shuttle) = 실제 물건은 그대로 두고 ‘내용물(전자)’만 다른 운반체로 갈아 태워 나르는 왕복 시스템]</div>
<div class="term">＊[용어: 환원당량(reducing equivalent) = 전자(+H)를 들고 있는 상태, 즉 ‘환원시킬 힘’]</div>""",
side=[("img", 38, "원본 슬라이드 38 — 말산-아스파르트산 셔틀 (순결과 NADH_P → NADH_N)", 175),
      ("img", 39, "원본 슬라이드 39 — 글리세롤 3-인산 셔틀: FADH₂ → Q, 1.5 ATP", 140),
      ("ana", "국경(내막)을 NADH 여권으로는 못 넘는다. 간·심장은 <b>짐을 말산 가방에 옮겨 정식 입국</b>(손실 0, 2.5), 근육·뇌는 <b>국경 담 너머로 짐만 던져 주는 급행</b>(빠르지만 1.5).")],
one="NADH는 내막을 못 넘는다! 간·심장 = 말산-아스파르트산(2.5), 근육·뇌 = 글리세롤 3-인산 → FAD → Q(1.5)."),

# ───────────────────────────── 문제
dict(t="q", id="q-yield", part=P, kind=["chk", "bl"], title="포도당 1개의 ATP 장부 채우기", src="개념확인 · Table 19-5", sub="빈칸 채우기 연습 (2026 중간 빈칸 3문제 대비)",
q="""포도당 1분자의 완전 산화에서 (말산-아스파르트산 셔틀 사용):<br>
· NADH 총 <span class="blank">(가)</span> 개 → ATP <span class="blank">(나)</span> 개<br>
· FADH<sub>2</sub> 총 <span class="blank">(다)</span> 개 → ATP 3개<br>
· 기질수준 인산화로 ATP 4개<br>
· 합계 ATP <span class="blank">(라)</span> 개. 글리세롤 3-인산 셔틀을 쓰면 <span class="blank">(마)</span> 개.""",
a="(가) 10 (나) 25 (다) 2 (라) 32 (마) 30",
steps=[("NADH: 해당 2 + 피루브산 산화 2 + 시트르산 회로 6 = <b>10</b>", "회로는 한 바퀴에 NADH 3개, 포도당 하나면 두 바퀴."),
       ("10 × 2.5 = <b>25</b> ATP", "NADH 1개 → H<sup>+</sup> 10개, ATP 1개 = H<sup>+</sup> 4개 → 10/4 = 2.5."),
       ("FADH<sub>2</sub>: 숙신산 탈수소효소 1개 × 2바퀴 = <b>2</b> → 2 × 1.5 = 3", ""),
       ("25 + 3 + 4 = <b>32</b>", "기질수준 = 해당 ATP 2 + 회로 GTP(ATP) 2."),
       ("글리세롤 3-인산 셔틀: 세포질 NADH 2개가 2.5 대신 1.5 → 2 × 1 = 2개 손해 → <b>30</b>", "")],
one="10 NADH(25) + 2 FADH₂(3) + 4(기질수준) = 32, 근육·뇌 셔틀이면 30."),

dict(t="q", id="q-redox1", part=P, kind=["txt", "sa"], title="Complex I 속 산화-환원 반응 해부하기", src="원서(5판) 19장 연습문제 1 · 솔루션 수록",
en="""Complex I promotes the following reactions (Fe<sup>3+</sup>/Fe<sup>2+</sup> = iron in Fe-S centers):<br>
1. NADH + H<sup>+</sup> + E-FMN → NAD<sup>+</sup> + E-FMNH<sub>2</sub><br>2. E-FMNH<sub>2</sub> + 2Fe<sup>3+</sup> → E-FMN + 2Fe<sup>2+</sup> + 2H<sup>+</sup><br>3. 2Fe<sup>2+</sup> + 2H<sup>+</sup> + Q → 2Fe<sup>3+</sup> + QH<sub>2</sub><br>
For each reaction identify (a) the electron donor, (b) the electron acceptor, (c) the conjugate redox pair, (d) the reducing agent, (e) the oxidizing agent.""",
q="Complex I의 세 반응 각각에서 (a) 전자 주개, (b) 전자 받개, (c) 짝 산화환원쌍, (d) 환원제, (e) 산화제를 쓰시오.",
a="① 주개·환원제 NADH, 받개·산화제 E-FMN ② 주개·환원제 E-FMNH₂, 받개·산화제 Fe³⁺ ③ 주개·환원제 Fe²⁺, 받개·산화제 Q",
steps=[("<b>규칙</b>: 전자를 주는 놈 = <b>환원제</b>(자신은 산화됨), 전자를 받는 놈 = <b>산화제</b>(자신은 환원됨)", "‘환원제’는 남을 환원시키는 약, 그러니 자기는 전자를 내준다."),
       ("반응 1: NADH → NAD<sup>+</sup> (전자 잃음) → 주개/환원제 = <b>NADH</b>, 받개/산화제 = <b>E-FMN</b>. 짝: NAD<sup>+</sup>/NADH, E-FMN/E-FMNH<sub>2</sub>", ""),
       ("반응 2: 주개/환원제 = <b>E-FMNH<sub>2</sub></b>, 받개/산화제 = <b>Fe<sup>3+</sup></b>. 짝: E-FMN/E-FMNH<sub>2</sub>, Fe<sup>3+</sup>/Fe<sup>2+</sup>", "FMNH₂가 전자 2개를 Fe-S 2개에 하나씩 → 플래빈의 ‘변압기’ 역할."),
       ("반응 3: 주개/환원제 = <b>Fe<sup>2+</sup></b>, 받개/산화제 = <b>Q</b>. 짝: Fe<sup>3+</sup>/Fe<sup>2+</sup>, Q/QH<sub>2</sub>", "")],
one="주개 = 환원제(자기는 산화), 받개 = 산화제(자기는 환원). NADH → FMN → Fe-S → Q 순서 그대로!"),

dict(t="q", id="q-fad", part=P, kind=["txt", "sa"], title="숙신산 탈수소효소는 왜 NAD⁺ 대신 FAD를 쓸까?", src="원서(5판) 19장 연습문제 3 · 솔루션 수록",
en="All the dehydrogenases of glycolysis and the citric acid cycle use NAD<sup>+</sup> (E′° = −0.32 V) except succinate dehydrogenase, which uses covalently bound FAD (E′° = 0.050 V). Suggest why FAD is a more appropriate electron acceptor, based on E′° of fumarate/succinate (0.031 V).",
q="숙신산 탈수소효소만 NAD<sup>+</sup>(−0.32 V) 대신 공유결합 FAD(+0.050 V)를 쓰는 이유를 푸마르산/숙신산 전위(+0.031 V)로 설명하시오.",
a="숙신산(0.031 V)에서 NAD⁺(−0.32 V)로 전자를 주는 건 오르막(ΔE′° < 0, ΔG > 0)이라 안 되지만, FAD(0.050 V)로는 내리막(ΔE′° > 0)이라 저절로 일어난다.",
steps=[("전자는 E′°가 <b>낮은 곳 → 높은 곳</b>으로만 저절로 흐른다", "물이 아래로 흐르듯."),
       ("숙신산 → NAD<sup>+</sup>: ΔE′° = −0.32 − 0.031 = <b>−0.35 V</b> → ΔG′° = −2 × 96.5 × (−0.35) ≈ <b>+68 kJ/mol</b> → 불가능", "ΔG가 +면 저절로 안 일어남."),
       ("숙신산 → FAD: ΔE′° = 0.050 − 0.031 = <b>+0.019 V</b> → ΔG′° ≈ <b>−3.7 kJ/mol</b> → 가능", "")],
extra='<div class="card tip" style="margin-top:4px"><div class="ct">📌 연결</div>그래서 FADH<sub>2</sub>의 전자는 이미 ‘조금 내려온 위치’(Q 근처)에서 출발 → Complex I을 못 거침 → ATP 1.5개.</div>',
one="숙신산의 전위(0.031 V)는 NAD⁺보다 훨씬 높아 NAD⁺에 전자를 못 준다. 바로 옆 FAD(0.050 V)라야 내리막!"),

dict(t="q", id="q-redstate", part=P, kind=["txt", "sa"], title="상황별로 운반체의 산화 상태 예측하기", src="원서(5판) 19장 연습문제 4 · 솔루션 수록",
en="Predict the state of oxidation of ubiquinone and cytochromes b, c<sub>1</sub>, c, and a + a<sub>3</sub> under each condition:<br>a. Abundant NADH and O<sub>2</sub>, but cyanide added<br>b. Abundant NADH, but O<sub>2</sub> exhausted<br>c. Abundant O<sub>2</sub>, but NADH exhausted<br>d. Abundant NADH and O<sub>2</sub>",
q="다음 조건에서 Q, cyt b, c<sub>1</sub>, c, a+a<sub>3</sub>의 산화 상태를 예측하시오. (a) NADH·O<sub>2</sub> 충분 + 사이안화물 (b) NADH 충분, O<sub>2</sub> 고갈 (c) O<sub>2</sub> 충분, NADH 고갈 (d) NADH·O<sub>2</sub> 모두 충분",
a="(a) 전부 환원 (b) 전부 환원 (c) 전부 산화 (d) 앞쪽일수록 더 환원, O₂ 쪽일수록 더 산화(정상 상태)",
steps=[("(a) CN<sup>−</sup>은 <b>Complex IV(사슬 맨 끝)</b>을 막는다 → 막힌 곳 ‘앞’ = 모든 운반체 → <b>모두 환원</b>", "사고가 맨 끝에 나면 도로 전체가 막힘."),
       ("(b) O<sub>2</sub>가 없으면 최종 받개가 없음 → (a)와 똑같이 <b>모두 환원</b>", "전자를 버릴 쓰레기통이 없다."),
       ("(c) 전자를 넣어 줄 NADH가 없음 → O<sub>2</sub>가 다 빼앗아 감 → <b>모두 산화</b>", ""),
       ("(d) 정상 흐름: Q는 가장 많이 환원, a+a<sub>3</sub>는 가장 많이 산화 (O<sub>2</sub>에 가까울수록 빨리 비워짐)", "슬라이드 34: O₂에 가까운 운반체가 먼저 산화.")],
one="막힌 곳 앞 = 환원, 뒤 = 산화. CN⁻·O₂ 없음 → 전부 환원 / NADH 없음 → 전부 산화."),

dict(t="q", id="q-roten", part=P, kind=["txt", "sa"], title="로테논과 안티마이신 A — 누가 더 센 독일까?", src="원서(5판) 19장 연습문제 5 · 솔루션 수록",
en="Rotenone strongly inhibits NADH dehydrogenase of insect and fish mitochondria. Antimycin A strongly inhibits the oxidation of ubiquinol.<br>a. Explain why rotenone ingestion is lethal to some insect and fish species.<br>b. Explain why antimycin A is a poison.<br>c. If they are equally effective at their sites, which would be a more potent poison? Explain.",
q="(a) 로테논이 곤충·물고기에게 치명적인 이유 (b) 안티마이신 A가 독인 이유 (c) 두 억제제가 각자의 자리를 똑같이 잘 막는다면 어느 쪽이 더 강한 독인가?",
a="(a)(b) 전자전달이 막혀 ATP 합성이 멈추기 때문 (c) 안티마이신 A — NADH와 FADH₂ 경로를 모두 막기 때문",
steps=[("(a) 로테논 → Complex I 차단 → NADH 전자가 Q로 못 감 → 양성자 펌프 정지 → <b>ATP 고갈</b> → 죽음", "물고기 잡는 독, 유기농 살충제로 쓰였음."),
       ("(b) 안티마이신 A → Complex III(QH<sub>2</sub> 산화) 차단 → 이후 전자 흐름 정지 → ATP 고갈", ""),
       ("(c) 로테논을 먹어도 숙신산(FADH<sub>2</sub>)·지방산의 전자는 <b>Q로 우회</b>해 III·IV로 계속 흐름. 안티마이신 A는 <b>Q 다음</b>을 막으니 <b>모든 입구</b>가 막힘 → <b>안티마이신 A가 더 강력</b>", "합류 지점(Q) 뒤를 막는 게 더 치명적.")],
one="Q 앞(로테논)을 막으면 옆문(II·ETF)으로 우회 가능, Q 뒤(안티마이신)를 막으면 모든 길이 끊긴다."),

dict(t="q", id="q-dg", part=P, kind=["calc", "bl"], title="ΔE′°로 ΔG′° 구하기 — 숙신산에서 O₂까지", src="개념확인 · Table 19-2 · 슬라이드 25", sub="계산기 없이 풀 수 있게 숫자를 골랐어",
q="""FADH<sub>2</sub>(숙신산 탈수소효소 속 FAD, E′° ≈ +0.05 V)의 전자 2개가 O<sub>2</sub>(E′° = +0.816 V ≈ 0.82 V)로 갈 때:<br>
(1) ΔE′° = <span class="blank">(가)</span> V<br>
(2) ΔG′° = −nℱΔE′° = −<span class="blank">(나)</span> × 96.5 × ΔE′° ≈ <span class="blank">(다)</span> kJ/mol<br>
(3) NADH에서 출발할 때(−220 kJ/mol)와 비교하면 에너지가 <span class="blank">(라)</span>(많다/적다) → 펌프되는 H<sup>+</sup>도 10개가 아니라 <span class="blank">(마)</span>개.""",
a="(가) 0.77 (나) 2 (다) 약 −149 (라) 적다 (마) 6",
steps=[("ΔE′° = 받는 쪽 − 주는 쪽 = 0.82 − 0.05 = <b>0.77 V</b>", "항상 ‘전자 받는 쪽 − 주는 쪽’."),
       ("n = 2 (FADH<sub>2</sub>는 전자 2개)", ""),
       ("ΔG′° = −2 × 96.5 × 0.77 ≈ −193 × 0.77 ≈ <b>−149 kJ/mol</b>", "193 × 0.77 = 193 × 0.8 − 193 × 0.03 ≈ 154 − 6 = 148."),
       ("−149 &gt; −220 (덜 음수) → 에너지 <b>적다</b> → Complex I을 건너뛰어 H<sup>+</sup> <b>6개</b>(III 4 + IV 2)", "")],
one="ΔG′° = −nℱ(E받개 − E주개). 출발점이 높을수록(FADH₂) 내리막이 짧아 에너지도 H⁺도 적다."),

dict(t="q", id="q-pump", part=P, kind=["chk", "multi"], title="양성자를 퍼내는 복합체 모두 고르기", src="개념확인 · 다답형", sub="2026 중간처럼 ‘맞는 것 모두’ — 보기 하나하나 O/X로",
q="""미토콘드리아 호흡사슬에 대한 설명으로 <b>옳은 것을 모두</b> 고르시오.""" + opts(
"Complex I은 전자 2개당 H<sup>+</sup> 4개를 막사이공간으로 퍼낸다.",
"Complex II는 숙신산의 전자를 FAD → Fe-S → Q로 넘기며 H<sup>+</sup> 2개를 퍼낸다.",
"Complex III의 Q 회로 순반응에서 P쪽으로 H<sup>+</sup> 4개가 나간다.",
"Cytochrome c는 막에 박힌 지용성 운반체로 III에서 IV로 전자 2개를 한 번에 나른다.",
"Complex IV는 기질의 H<sup>+</sup> 8개 중 4개를 물 생성에, 4개를 펌프에 쓴다(O<sub>2</sub> 1분자당)."),
a="①, ③, ⑤",
opx=ox(("①", True, "I = 4H<sup>+</sup>/2e<sup>−</sup>."), ("②", False, "Complex II는 양성자 펌프가 <b>없다</b>(0개)."), ("③", True, "QH<sub>2</sub> + 2cyt c<sub>1</sub> + 2H<sup>+</sup><sub>N</sub> → … + 4H<sup>+</sup><sub>P</sub>."),
       ("④", False, "cyt c는 막사이공간의 <b>수용성</b> 단백질, 전자 <b>1개</b>씩."), ("⑤", True, "4cyt c + 8H<sup>+</sup><sub>N</sub> + O<sub>2</sub> → … + 4H<sup>+</sup><sub>P</sub> + 2H<sub>2</sub>O.")),
one="펌프 개수 4·0·4·2. cyt c = 수용성, 1전자. IV의 8H⁺ = 4(물) + 4(펌프)."),

dict(t="q", id="q-tb-order", part=P, kind=["chk", "mc"], title="전자 운반체의 올바른 순서", src="개념확인 (영어 원문 연습)",
en="Which of the following is the correct sequence for the order of electron carriers in the mitochondrial respiratory chain?" + eopts(
"NADH → cyt c → Q → cyt b → cyt (a + a<sub>3</sub>) → O<sub>2</sub>",
"NADH → Q → cyt b → cyt c<sub>1</sub> → cyt c → cyt (a + a<sub>3</sub>) → O<sub>2</sub>",
"NADH → Q → cyt c<sub>1</sub> → cyt b → cyt (a + a<sub>3</sub>) → cyt c → O<sub>2</sub>",
"FADH<sub>2</sub> → NADH → Q → cyt c → cyt b → O<sub>2</sub>",
"NADH → cyt b → cyt c → Q → cyt (a + a<sub>3</sub>) → O<sub>2</sub>"),
q="미토콘드리아 호흡사슬의 전자 운반체 순서로 옳은 것은? (보기 A–E는 원문과 같음)",
a="B", aen="NADH → Q → cyt b → cyt c₁ → cyt c → cyt (a + a₃) → O₂",
steps=[("E′°가 낮은 순서로 나열: NADH(−0.32) &lt; Q(0.045) &lt; b(0.077) &lt; c<sub>1</sub>(0.22) &lt; c(0.254) &lt; a(0.29) &lt; a<sub>3</sub>(0.35) &lt; O<sub>2</sub>(0.816)", "전자는 낮은 전위 → 높은 전위로 흐름."),
       ("암기법: <b>“N-Q-B-C1-C-A-O”</b> → “엔큐! 비씨원씨 에이오”", "")],
one="NADH → Q → b → c₁ → c → a·a₃ → O₂. 전위가 낮은 데서 높은 데로!"),

dict(t="q", id="q-tb-shuttle", part=P, kind=["chk", "mc"], title="뇌·골격근에서 세포질 NADH의 운명", src="개념확인 (영어 원문 연습)",
en="In skeletal muscle and brain, the glycerol 3-phosphate shuttle delivers electrons from cytosolic NADH to:" + eopts(
"Complex I, yielding about 2.5 ATP per NADH", "cytochrome c directly", "ubiquinone (Q) via FAD, yielding about 1.5 ATP per NADH", "NADP<sup>+</sup> in the matrix", "Complex IV directly"),
q="골격근과 뇌에서 글리세롤 3-인산 셔틀은 세포질 NADH의 전자를 어디로 전달하는가?",
a="C", aen="ubiquinone (Q) via FAD, yielding about 1.5 ATP per NADH",
steps=[("세포질: DHAP + NADH → 글리세롤 3-인산 + NAD<sup>+</sup>", ""),
       ("내막 바깥면 미토콘드리아 글리세롤 3-인산 탈수소효소(<b>FAD</b>) → FADH<sub>2</sub> → <b>Q</b>", "Complex I을 건너뜀."),
       ("Q → III → IV: H<sup>+</sup> 6개 → 6/4 = <b>1.5 ATP</b>", "")],
opx=ox(("A", False, "Complex I로 가는 건 말산-아스파르트산 셔틀(간·심장·신장)."), ("B·E", False, "cyt c·Complex IV로 직접 가는 셔틀은 없다."), ("D", False, "NADP<sup>+</sup>가 아니라 FAD → Q.")),
one="근육·뇌 = 글리세롤 3-인산 → FAD → Q → 1.5 ATP. 간·심장 = 말산-아스파르트산 → NADH → I → 2.5 ATP."),

dict(t="q", id="q-tb-q", part=P, kind=["chk", "mc"], title="유비퀴논(Q)에 대해 틀린 설명", src="개념확인 · 원서(5판) 19장 연습문제 2 응용",
en="Which one of the following statements about ubiquinone (coenzyme Q) is <b>not</b> correct?" + eopts(
"It is a lipid-soluble benzoquinone with a long isoprenoid side chain.",
"It can accept one electron to form the semiquinone radical (·QH).",
"Upon accepting two electrons, it picks up two protons to form ubiquinol (QH<sub>2</sub>).",
"It is a covalently bound prosthetic group of Complex I.",
"It can diffuse freely within the inner mitochondrial membrane."),
q="유비퀴논(코엔자임 Q)에 대한 설명으로 <b>틀린</b> 것은?",
a="D", aen="It is NOT a covalently bound prosthetic group — it moves freely in the membrane (mobile carrier).",
steps=[("Q의 정체: <b>지용성, 움직이는(mobile) 운반체</b>. 어느 복합체에도 고정돼 있지 않다", "그래서 I·II·ETF·글리세롤 3-인산 탈수소효소의 전자를 전부 모아 III로 나름."),
       ("긴 아이소프레노이드 꼬리의 기능 = 막 지질 속에 녹아 있게 함 (원서 문제 2의 답)", "")],
opx=ox(("A", True, "벤조퀴논 + 아이소프레노이드(사람 Q<sub>10</sub>)."), ("B", True, "전자 1개 → 반퀴논 라디칼."), ("C", True, "2e<sup>−</sup> + 2H<sup>+</sup> → QH<sub>2</sub>."), ("D", False, "공유결합 보결분자단은 FMN(I), FAD(II) 쪽. Q는 자유롭게 움직인다."), ("E", True, "막 속 셔틀버스.")),
one="Q = 막 속을 헤엄치는 지용성 셔틀. 아이소프레노이드 꼬리 = 막에 녹아 있게 하는 닻."),
]
