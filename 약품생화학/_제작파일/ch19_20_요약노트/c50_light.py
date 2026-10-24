from parts import *
P = P5
E = [
dict(t="c", id="c-psov", part=P, title="광합성 큰 그림과 빛의 에너지 — 햇빛 → 화학에너지", sub="Photosynthesis: harvesting light energy · E = hν = hc/λ · Slides 91–95",
core="광합성 = <b>명반응</b>(빛으로 H<sub>2</sub>O를 쪼개 O<sub>2</sub>, <b>ATP·NADPH</b> 생산) + <b>탄소고정 반응</b>(그 ATP·NADPH로 CO<sub>2</sub>를 당으로). 빛 에너지는 <b>파장이 짧을수록 크다</b>.",
detail="""<p><span class="fx">nCO<sub>2</sub> + nH<sub>2</sub>O + 빛(photon) → (CH<sub>2</sub>O)<sub>n</sub> + nO<sub>2</sub></span></p>
<ul><li><b>Stage I · Light-dependent reactions (명반응)</b>: 엽록소가 빛 흡수 → H<sub>2</sub>O 분해(O<sub>2</sub> 발생) → <b>NADPH + ATP</b> = ‘에너지 원천(energy sources)’</li>
<li><b>Stage II · Carbon-assimilation reactions (탄소동화 반응)</b> = 빛과 무관한 반응(light-independent, 예전 이름 ‘암반응’) = <b>Calvin cycle (캘빈 회로)</b> → <b>G3P</b>(Glyceraldehyde 3-Phosphate, 글리세르알데하이드 3-인산, PGAL) → 포도당·수크로스·녹말</li>
<li>광합성 세포가 만든 O<sub>2</sub>·탄수화물 → 동물(종속영양 세포)이 연료로 써 ATP를 만들고 CO<sub>2</sub>·H<sub>2</sub>O를 돌려줌 = <b>생명의 순환</b>.</li></ul>
<div class="term">＊[용어: photon(포톤, 광자) = 빛 에너지의 최소 덩어리 / einstein(아인슈타인) = 광자 1몰 = 6.022 × 10<sup>23</sup>개]</div>""",
formula="""<span class="fx">E = hν = hc/λ</span> &nbsp; h = 플랑크(Planck) 상수 6.626 × 10<sup>−34</sup> J·s, ν = 진동수(1/s), c = 빛의 속도 3.00 × 10<sup>8</sup> m/s, λ = 파장<br>
1 einstein의 에너지 = E × 6.022 × 10<sup>23</sup> → 붉은빛 ≈ <b>150–170 kJ/einstein</b>, 380 nm(보라) ≈ 300 kJ/einstein<br>
→ <g>파장 ↓ = 에너지 ↑</g> (보라 &gt; 파랑 &gt; 초록 &gt; 빨강)""",
example="""<b>Q.</b> 700 nm 빛 1 einstein의 에너지는?<br>
<b>Step 1</b> 광자 1개: E = hc/λ = (6.626 × 10<sup>−34</sup> × 3.00 × 10<sup>8</sup>) ÷ (700 × 10<sup>−9</sup>) = 1.99 × 10<sup>−25</sup> ÷ 7.0 × 10<sup>−7</sup> ≈ <b>2.84 × 10<sup>−19</sup> J</b> 👉 nm는 반드시 m로(× 10<sup>−9</sup>).<br>
<b>Step 2</b> 1몰: 2.84 × 10<sup>−19</sup> × 6.022 × 10<sup>23</sup> ≈ 1.71 × 10<sup>5</sup> J = <b>171 kJ/einstein</b><br>
<b>Step 3</b> 680 nm면? 파장이 조금 짧으니 조금 큼: 171 × 700/680 ≈ <b>176 kJ</b>.""",
side=[("img", 94, "원본 슬라이드 94 — Stage I 명반응(NADPH·ATP) → Stage II 탄소동화(캘빈 회로 → G3P)", 175),
      ("img", 95, "원본 슬라이드 95 — 파장별 에너지(kJ/einstein): 380 nm 300 → 750 nm 170", 125),
      ("ana", "명반응 = <b>태양광 충전소</b>(빛으로 배터리 ATP·NADPH 충전), 캘빈 회로 = <b>공장</b>(충전된 배터리로 CO<sub>2</sub>를 조립해 설탕). 공장은 배터리만 있으면 밤에도 잠깐 돈다.")],
one="명반응 = 빛 + H₂O → O₂ + ATP + NADPH, 캘빈 = ATP + NADPH + CO₂ → G3P. E = hc/λ, 짧은 파장 = 센 빛."),

dict(t="c", id="c-chloro", part=P, title="엽록체의 구조 — 틸라코이드 안(내강)과 밖(스트로마)", sub="Photosynthesis takes place in chloroplasts · Slides 97–99",
core="엽록체 안의 납작한 주머니 <b>틸라코이드</b> 막에 광계·전자 운반체·ATP 합성효소가 박혀 있다. 틸라코이드 바깥 액체 = <b>스트로마(N쪽)</b>, 안쪽 공간 = <b>내강(lumen, P쪽)</b>.",
detail="""<ul><li><b>Chloroplast (클로로플라스트, 엽록체)</b>: 외막 + 내막(이중막) → 안쪽 액체 = <b>stroma (스트로마, 기질)</b> = 미토의 matrix에 해당. 캘빈 회로가 여기서.</li>
<li><b>Thylakoid (틸라코이드)</b>: 스트로마 속의 납작한 막 주머니. 동전처럼 쌓인 더미 = <b>grana (그라나, 단수 granum)</b>. 쌓인 부분 = appressed(밀착) 막, 스트로마에 노출된 부분 = stromal lamellae.</li>
<li><b>Lumen (루멘, 틸라코이드 내강)</b>: 틸라코이드 안쪽 공간 = 미토의 막사이공간처럼 <b>H<sup>+</sup>가 쌓이는 P쪽</b>.</li>
<li>틸라코이드 막의 배치(슬라이드 98): <b>PSII</b>는 주로 밀착된 그라나 막, <b>PSI과 ATP 합성효소</b>는 스트로마 쪽 노출 막, <b>cyt b<sub>6</sub>f</b>는 양쪽 다.</li></ul>
<table class="t"><tr><th></th><th>미토콘드리아</th><th>엽록체</th></tr>
<tr><td>N쪽 (ATP가 만들어지는 곳)</td><td>기질(matrix)</td><td>스트로마(stroma)</td></tr>
<tr><td>P쪽 (H<sup>+</sup>가 쌓이는 곳)</td><td>막사이공간</td><td>틸라코이드 내강(lumen)</td></tr>
<tr><td>에너지 막</td><td>내막(크리스타)</td><td>틸라코이드 막</td></tr></table>
<div class="term">＊[용어: 그라나 = 동전(틸라코이드)을 쌓아 올린 탑. 탑 사이를 잇는 다리 = 스트로마 라멜라]</div>""",
side=[("img", 98, "원본 슬라이드 98 — 틸라코이드·그라나·스트로마·내강, 광계와 ATP 합성효소 위치", 200),
      ("ana", "엽록체 = <b>물에 뜬 동전 탑들이 있는 수영장</b>. 수영장 물 = 스트로마(공장 작업장), 동전 = 틸라코이드, 동전 속 빈 공간 = 내강(양성자 저장 탱크)."),
      ("trap", "미토는 H<sup>+</sup>를 기질 → <b>바깥(막사이공간)</b>으로, 엽록체는 스트로마 → <b>안쪽(내강)</b>으로 퍼낸다. 방향 문제 단골!")],
one="스트로마 = N쪽(캘빈 회로·ATP 생성), 내강 = P쪽(H⁺ 저장). 틸라코이드 막 = 광계들의 무대."),

dict(t="c", id="c-pigment", part=P, title="광합성 색소 — 엽록소와 보조 색소가 빛을 나눠 잡는다", sub="Chlorophylls · Accessory pigments · LHCII · Slides 100–102",
core="엽록소는 <b>Mg<sup>2+</sup></b>를 품은 고리에 <b>단일·이중결합이 번갈아 있는(공액) 구조</b>라 가시광선을 흡수한다. 엽록소 a·b와 카로티노이드 등 <b>보조 색소</b>가 서로 다른 파장을 잡아 햇빛을 빈틈없이 쓴다.",
detail="""<ul><li><b>Chlorophyll a (클로로필 a, 엽록소 a)</b>: 포르피린 비슷한 고리(4개 피롤) 중심에 <b>Mg<sup>2+</sup></b>(헴은 Fe!), 긴 <b>phytol(파이톨) 꼬리</b>로 막에 고정.</li>
<li><b>Chlorophyll b</b>: a의 –CH<sub>3</sub> 하나가 <b>–CHO</b> → 흡수 파장이 약간 다름.</li>
<li><y>공액계(conjugated system, 단일결합·이중결합이 번갈아)</y> → 전자가 넓게 퍼져 낮은 에너지(가시광선)로도 들뜬다.</li>
<li><b>Accessory pigments (보조 색소)</b>: <b>β-carotene(베타카로틴)·lutein(루테인)</b>(카로티노이드, 400–500 nm 청록 흡수, 노랑·주황), 남세균·홍조류의 <b>phycoerythrin(피코에리트린)·phycocyanin(피코시아닌)</b>(500–650 nm). 엽록소가 못 잡는 초록 근처까지 메움.</li>
<li><b>LHCII</b>(Light-Harvesting Complex II, 집광 복합체 II): 단량체 1개에 <b>엽록소 a 7개 + 엽록소 b 5개 + 루테인 2개</b>, 실제로는 <b>삼량체(trimer)</b>로 존재 → 빛을 모아 PSII로 보냄.</li></ul>
<div class="term">＊[용어: 공액(conjugated) = 이중결합이 하나 건너 하나씩 이어진 ‘줄무늬’ 구조. 길수록 더 긴 파장(낮은 에너지)을 흡수]</div>""",
side=[("img", 102, "원본 슬라이드 102 — 엽록소 a·b, 카로틴, 루테인, 피코에리트린·피코시아닌의 흡수 스펙트럼", 185),
      ("img", 101, "원본 슬라이드 101 — 엽록소 a 구조: Mg²⁺ + 공액 고리 + 파이톨 꼬리", 130),
      ("ana", "<b>여러 색 그물을 겹쳐 친 어부</b>. 엽록소는 파랑·빨강 물고기만, 카로티노이드는 청록 물고기를 잡는다. 초록은 거의 안 잡혀서 튕겨 나오니 잎이 초록으로 보여.")],
one="엽록소 = Mg²⁺ + 공액 고리(가시광 흡수) + 파이톨 꼬리. b는 CHO. LHCII = 엽록소 a7·b5·루테인2, 삼량체."),

dict(t="c", id="c-exciton", part=P, title="들뜸 에너지 전달 — 안테나에서 반응 중심으로 ‘에너지 릴레이’", sub="Excitation · Exciton transfer · Charge separation in the reaction center · Slides 96, 103",
core="빛을 받은 엽록소의 들뜬 에너지는 ① 열·형광으로 버려지거나 ② <b>옆 분자로 넘어간다(exciton transfer)</b>. 안테나 색소들이 에너지를 <b>반응 중심</b>으로 몰아주면, 거기서 <b>전자가 실제로 튀어나가 전하 분리</b>가 일어난다.",
detail="""<ul><li>빛의 에너지 덩어리(quantum, 양자)가 분자의 <b>에너지 준위 차이와 딱 맞을 때만</b> 흡수 → 들뜬상태(excited state).</li>
<li>들뜬 분자의 3가지 운명 (슬라이드 96):<br>
· <b>열 + 형광(fluorescence)</b>: 다시 바닥상태로 떨어지며 빛 방출(낭비)<br>
· <b>Exciton transfer (엑시톤 전달, 공명 에너지 전달)</b>: 전자는 그대로, <b>에너지만</b> 이웃 엽록소로<br>
· <b>전자 전달</b>: 들뜬 전자가 아예 <b>전자 수용체</b>로 넘어감 (반응 중심에서만)</li>
<li><b>Antenna chlorophyll (안테나 엽록소)</b> 수백 개가 빛을 모아 → 엑시톤 전달 → <b>reaction center (반응 중심) 엽록소</b>(특별한 엽록소 쌍)를 들뜨게 함.</li>
<li>반응 중심: 들뜬 전자 → 전자 수용체로 → 반응 중심에 <b>(+) 구멍</b>, 수용체는 (−) = <b>charge separation (전하 분리)</b> → 구멍은 전자 주개가 채움 → 전자 흐름 시작.</li></ul>
<div class="term">＊[용어: 엑시톤(exciton) = ‘들뜸 에너지 꾸러미’. 공이 아니라 파도처럼 분자에서 분자로 옮겨 감]</div>""",
side=[("img", 103, "원본 슬라이드 103 — 안테나 → 엑시톤 전달 → 반응 중심의 전하 분리", 225),
      ("ana", "<b>운동장의 파도타기 응원</b>: 관중(안테나 엽록소)은 자리에서 일어났다 앉을 뿐(에너지만 전달), 파도가 결승 지점(반응 중심)에 오면 거기 선수(전자)가 <b>진짜로 공을 던진다</b>(전자 전달)."),
      ("tip", "Summary 2: “엽록소는 흡수한 에너지를 <b>엑시톤 전달</b>로 반응 중심에 모은다”.")],
one="안테나 = 에너지만 릴레이(엑시톤), 반응 중심 = 전자를 진짜로 던짐(전하 분리)."),

dict(t="c", id="c-psii", part=P, title="광계 II와 산소 발생 복합체 — 물을 쪼개 O₂를 만드는 유일한 효소", sub="Photosystem II (pheophytin-quinone type) · Oxygen-evolving complex (Mn₄) · Slides 104–106",
core="PSII의 반응 중심 <b>P680</b>이 빛을 받아 전자를 <b>페오피틴 → PQ<sub>A</sub> → PQ<sub>B</sub></b>로 보낸다. 전자를 잃은 <b>P680<sup>+</sup></b>(생물계 최강 산화제)는 <b>Mn<sub>4</sub> 클러스터</b>를 통해 물에서 전자를 빼앗아 <b>O<sub>2</sub></b>를 낸다.",
detail="""<ul><li><b>PSII</b> = <b>pheophytin-quinone (페오피틴-퀴논) 형</b> 반응 중심. 핵심 단백질 D1·D2.</li>
<li>경로: <b>P680</b>(680 nm 흡수 엽록소 쌍) → 빛 → <b>Pheo</b>(pheophytin, 페오피틴 = Mg 없는 엽록소) → <b>PQ<sub>A</sub></b> → <b>PQ<sub>B</sub></b>. PQ<sub>B</sub>가 전자 2개 + 스트로마 H<sup>+</sup> 2개를 받으면 <b>PQ<sub>B</sub>H<sub>2</sub></b>가 되어 막 속 PQ 풀로 떠남.</li>
<li><span class="fx">4 P680 + 4H<sup>+</sup> + 2PQ<sub>B</sub> + 4 photons → 4 P680<sup>+</sup> + 2PQ<sub>B</sub>H<sub>2</sub></span></li>
<li><b>OEC</b>(Oxygen-Evolving Complex, 산소 발생 복합체, water-splitting complex): <b>Mn 4개</b>(+Ca) 클러스터. P680<sup>+</sup>가 <b>Tyr<sub>Z</sub></b>(티로신 라디칼)을 통해 Mn 클러스터에서 전자를 하나씩 4번 빼앗음 → [Mn]<sup>0</sup> → [Mn]<sup>1+</sup> → … → <b>[Mn]<sup>4+</sup></b> → 그때 물 2분자에서 전자 4개 회수 → <b>O<sub>2</sub></b> 방출 + H<sup>+</sup> 4개는 <b>내강</b>으로.</li>
<li>광자 4개(엑시톤 4번)마다 O<sub>2</sub> 1개.</li></ul>""",
formula="""<span class="fx">2H<sub>2</sub>O → 4H<sup>+</sup> + 4e<sup>−</sup> + O<sub>2</sub></span> (내강에서)<br>
4P680<sup>+</sup> + 4Tyr → 4P680 + 4·Tyr &nbsp;/&nbsp; 4·Tyr + [Mn]<sup>0</sup> → 4Tyr + [Mn]<sup>4+</sup> &nbsp;/&nbsp; [Mn]<sup>4+</sup> + 2H<sub>2</sub>O → [Mn]<sup>0</sup> + 4H<sup>+</sup> + O<sub>2</sub><br>
<b>순반응: 2H<sub>2</sub>O + 2PQ<sub>B</sub> + 4 photons → O<sub>2</sub> + 2PQ<sub>B</sub>H<sub>2</sub></b>""",
side=[("img", 106, "원본 슬라이드 106 — 엑시톤 4번 → Mn₄가 0 → 4+ 충전 → 물 2분자 → O₂", 175),
      ("img", 105, "원본 슬라이드 105 — PSII: P680 → Pheo → PQ_A → PQ_B, 물 쪽엔 Mn₄·Tyr_Z", 150),
      ("ana", "OEC = <b>4칸 충전식 배터리</b>. 빛 한 번에 한 칸씩 (+) 충전, 4칸이 다 차면 물 두 분자를 한꺼번에 깨서 전자 4개를 되찾고 O<sub>2</sub>를 뱉는다. 반쪽짜리 산소(ROS)를 흘리지 않는 비결.")],
one="PSII: P680 → Pheo → PQ_A → PQ_B(H₂). P680⁺ → Tyr_Z → Mn₄(4번 충전) → 2H₂O → O₂ + 4H⁺(내강)."),

dict(t="c", id="c-psi", part=P, title="시토크롬 b₆f와 광계 I — PQH₂에서 NADPH까지", sub="Cytochrome b₆f · Plastocyanin · PSI (Fe-S type) · Ferredoxin · Slides 107–111",
core="PQH<sub>2</sub> → <b>cyt b<sub>6</sub>f</b>(Q 회로로 H<sup>+</sup>를 내강에 펌프) → <b>plastocyanin(Cu)</b> → <b>P700</b>(PSI) → 빛 → A<sub>0</sub> → A<sub>1</sub>(phylloquinone) → Fe-S → <b>ferredoxin</b> → <b>FNR</b> → <b>NADPH</b>.",
detail="""<p><b>① Cytochrome b<sub>6</sub>f complex (시토크롬 b6f 복합체)</b> — 미토 Complex III의 사촌. PSII와 PSI를 잇는 다리.</p>
<ul><li>구성: cyt b<sub>6</sub>(헴 b<sub>L</sub>, b<sub>H</sub>), <b>cyt f</b>(헴 f), <b>Rieske 철-황 단백질</b>, 헴 x(c<sub>i</sub>)</li>
<li><b>Q 회로</b>로 PQH<sub>2</sub>의 전자를 plastocyanin에 하나씩 넘기며 스트로마 H<sup>+</sup>를 <b>내강</b>으로 운반.</li></ul>
<p><b>② Plastocyanin (플라스토시아닌, PC)</b>: 내강의 <b>구리(Cu)</b> 단백질, 1전자 운반 (미토의 cyt c 역할).</p>
<p><b>③ Photosystem I (광계 I) = Fe-S 형 반응 중심</b></p>
<ul><li><b>P700</b>(700 nm 흡수) → 빛 → <b>A<sub>0</sub></b>(엽록소) → <b>A<sub>1</sub> = Q<sub>K</sub>(phylloquinone, 필로퀴논 = 비타민 K<sub>1</sub>)</b> → <b>F<sub>X</sub> → F<sub>A</sub> → F<sub>B</sub></b>(Fe-S 중심들) → <b>ferredoxin (페레독신, Fd)</b>(스트로마, 2Fe-2S)</li>
<li><b>FNR</b>(Ferredoxin:NADP<sup>+</sup> oxidoreductase, 페레독신-NADP<sup>+</sup> 산화환원효소, FAD 보유): Fd 2개의 전자 → <b>NADP<sup>+</sup> + H<sup>+</sup> → NADPH</b> (스트로마 쪽)</li>
<li>P700<sup>+</sup>의 구멍은 plastocyanin이 채움.</li></ul>
<p><b>전체 직선 경로 (슬라이드 111)</b>:</p>
<p><span class="fx">H<sub>2</sub>O → P680 → Pheo → PQ → b<sub>6</sub>f → PC → P700 → Fd → NADPH</span></p>
<div class="term">＊[용어: PQ(plastoquinone, 플라스토퀴논) = 엽록체판 유비퀴논. 막 속을 헤엄치며 전자 2개 + H<sup>+</sup> 2개 운반]</div>""",
side=[("img", 111, "원본 슬라이드 111 — H₂O → P680 → Pheo → PQ → b₆f → PC → P700 → Fd → NADPH", 175),
      ("img", 110, "원본 슬라이드 110 — PSI: P700 → A₀ → Q_K(필로퀴논) → F_X → F_A/F_B → 페레독신", 155),
      ("tip", "미토 ↔ 엽록체 짝: Q ↔ <b>PQ</b>, Complex III ↔ <b>cyt b<sub>6</sub>f</b>, cyt c ↔ <b>plastocyanin(Cu)</b>. PSII = 페오피틴-퀴논형, PSI = <b>Fe-S형</b>.")],
one="PQH₂ → b₆f(Q 회로, H⁺ → 내강) → PC(Cu) → P700 → A₀ → A₁(필로퀴논) → Fe-S → Fd → FNR → NADPH."),

dict(t="c", id="c-zscheme", part=P, title="Z 도식 — 두 광계가 직렬로, 비순환 vs 순환 전자 흐름", sub="Z scheme · Noncyclic and cyclic photophosphorylation · Slide 112",
core="물(E′° +0.82 V)에서 NADP<sup>+</sup>(−0.32 V)까지 <b>오르막</b>을 오르려면 빛을 <b>두 번</b>(PSII, PSI) 받아야 한다 → Z 모양. <b>비순환</b> = O<sub>2</sub> + NADPH + ATP, <b>순환</b>(PSI만) = <b>ATP만</b>.",
detail="""<ul><li>식물에선 <b>두 반응 중심이 직렬(tandem)</b>로 작동 (Summary 3). 각 광계가 전자 하나를 한 번씩 ‘퍼 올림’.</li>
<li>Z 도식(세로축 = E′°): P680 ↑(빛) → Pheo → PQ → <b>cyt b<sub>6</sub>f(내리막, H<sup>+</sup> 펌프)</b> → PC → P700 ↑(빛) → A<sub>0</sub> → … → Fd → NADP<sup>+</sup></li></ul>
<table class="t"><tr><th></th><th>비순환(noncyclic)</th><th>순환(cyclic)</th></tr>
<tr><td>관여</td><td>PSII + b<sub>6</sub>f + PSI</td><td><b>PSI + b<sub>6</sub>f만</b></td></tr>
<tr><td>전자 경로</td><td>H<sub>2</sub>O → … → NADP<sup>+</sup> (일방통행)</td><td>P700 → Fd → <b>cyt b<sub>6</sub>f</b> → PC → P700 (돌고 돎)</td></tr>
<tr><td>산물</td><td><b>O<sub>2</sub> + NADPH + ATP</b></td><td><b>ATP만</b> (O<sub>2</sub>·NADPH 없음)</td></tr>
<tr><td>언제</td><td>평소</td><td>[NADPH]/[NADP<sup>+</sup>] 높을 때 → 캘빈 회로에 필요한 <b>추가 ATP</b> 공급</td></tr></table>""",
formula="""<span class="fx">2H<sub>2</sub>O + 2NADP<sup>+</sup> + 8 photons → O<sub>2</sub> + 2NADPH + 2H<sup>+</sup></span> (전자 4개 이동)<br>
왜 광자 8개? 전자 4개 × 광계 2번 = 8.""",
side=[("img", 112, "원본 슬라이드 112 — Z 도식: PSII와 PSI가 직렬, 순환 경로는 ATP only", 230),
      ("ana", "<b>2단 점프대</b>: 물속(H<sub>2</sub>O)에서 높은 다이빙대(NADP<sup>+</sup>)까지 한 번에 못 오르니, 1단 트램펄린(PSII)으로 뛰어 중간 계단(b<sub>6</sub>f)을 내려오며 물레방아를 돌리고, 2단 트램펄린(PSI)으로 다시 뛰어오른다."),
      ("trap", "순환 흐름은 <b>PSII를 안 쓰므로 O<sub>2</sub> 발생 없음</b>, NADPH도 없음. ATP만!")],
one="Z 도식 = 빛 두 번(PSII → PSI). 비순환 = O₂ + NADPH + ATP(광자 8개당 O₂ 1), 순환 = ATP만."),

dict(t="c", id="c-photophos", part=P, title="광인산화 — 내강에 쌓인 H⁺로 ATP 만들기, 미토와 비교", sub="Photophosphorylation · CF₀CF₁ · Comparison of chemiosmotic mechanisms · Slides 113–114",
core="O<sub>2</sub> 1분자당 <b>H<sup>+</sup> 12개</b>(OEC 4 + b<sub>6</sub>f 8)가 내강에 쌓여 ΔpH ≈ <b>3</b>. 이 H<sup>+</sup>가 <b>CF<sub>o</sub>CF<sub>1</sub></b>을 지나 스트로마로 나올 때 <b>ATP 약 3개</b>.",
detail="""<p><span class="fx">2H<sub>2</sub>O + 8 photons + 2NADP<sup>+</sup> + ~3ADP + ~3P<sub>i</sub> → O<sub>2</sub> + ~3ATP + 2NADPH</span></p>
<ul><li>H<sup>+</sup> 12개 = OEC(물 분해)에서 <b>4개</b> + cyt b<sub>6</sub>f(Q 회로)에서 <b>8개</b> → 내강 pH ≈ 5, 스트로마 ≈ 8 → <b>ΔpH ≈ 3</b> (H<sup>+</sup> 농도 1000배 차!)</li>
<li>엽록체에선 Cl<sup>−</sup>·Mg<sup>2+</sup> 이동으로 전하 차(Δψ)가 거의 상쇄 → 구동력은 <b>주로 ΔpH</b> (미토는 Δψ가 주력).</li>
<li><b>CF<sub>o</sub>CF<sub>1</sub></b>(Chloroplast F<sub>o</sub>F<sub>1</sub>): 미토 ATP 합성효소와 같은 구조·회전 촉매. CF<sub>1</sub>이 <b>스트로마 쪽</b>으로 튀어나와 거기서 ATP 생성 → 캘빈 회로가 바로 사용.</li>
<li>시금치 CF<sub>o</sub>의 c 고리 = c<sub>14</sub> → 14 H<sup>+</sup> / 3 ATP ≈ 4.7 H<sup>+</sup>/ATP → 12 ÷ 4.7 ≈ <b>2.6 ≈ 3 ATP</b>.</li></ul>
<table class="t"><tr><th>비교 (슬라이드 114)</th><th>미토콘드리아</th><th>엽록체</th></tr>
<tr><td>전자 주개 → 받개</td><td>환원된 기질(NADH) → <b>O<sub>2</sub></b></td><td><b>H<sub>2</sub>O</b> → NADP<sup>+</sup></td></tr>
<tr><td>에너지 원천</td><td>연료의 산화</td><td><b>빛</b></td></tr>
<tr><td>H<sup>+</sup> 펌프 방향</td><td>기질 → 막사이공간 (<b>밖으로</b>)</td><td>스트로마 → 내강 (<b>안으로</b>)</td></tr>
<tr><td>ATP 생성 위치</td><td>기질 (N)</td><td>스트로마 (N)</td></tr>
<tr><td>구동력 주성분</td><td>Δψ + ΔpH</td><td><b>ΔpH</b></td></tr></table>""",
side=[("img", 113, "원본 슬라이드 113 — 틸라코이드의 양성자·전자 회로 (12H⁺: OEC 4 + b₆f 8)", 165),
      ("img", 114, "원본 슬라이드 114 — 미토콘드리아 vs 엽록체 화학삼투 비교", 150),
      ("ana", "미토와 엽록체는 <b>같은 물레방아(ATP 합성효소)를 쓰는 두 발전소</b>. 미토는 석탄(NADH)을 태워 물을 퍼 올리고, 엽록체는 태양광으로 물을 퍼 올린다. 물레방아 날개(F<sub>1</sub>)는 둘 다 <b>작업장(N쪽: 기질·스트로마)</b>을 향한다.")],
one="O₂ 1개 = H⁺ 12개(OEC 4 + b₆f 8) = ΔpH 3 = ATP ~3개. 엽록체는 안(내강)으로 펌프, ATP는 스트로마에서."),

# ───────────────────────────── 문제
dict(t="q", id="q-photon", part=P, kind=["calc", "bl"], title="빛 1 einstein의 에너지 계산", src="개념확인 · 슬라이드 95 (E = hc/λ)",
q="""h = 6.6 × 10<sup>−34</sup> J·s, c = 3.0 × 10<sup>8</sup> m/s, N<sub>A</sub> = 6.0 × 10<sup>23</sup>이라 하자.<br>
(1) 660 nm 광자 1개의 에너지 E = hc/λ = <span class="blank">(가)</span> J<br>
(2) 1 einstein(광자 1몰)의 에너지 ≈ <span class="blank">(나)</span> kJ<br>
(3) 330 nm 빛 1 einstein의 에너지는 660 nm의 <span class="blank">(다)</span>배<br>
(4) 1 einstein = 광자 <span class="blank">(라)</span>개""",
a="(가) 3.0 × 10⁻¹⁹ (나) 180 (다) 2 (라) 6.0 × 10²³ (아보가드로 수)",
steps=[("λ = 660 nm = 660 × 10<sup>−9</sup> m = <b>6.6 × 10<sup>−7</sup> m</b>", "공식의 c가 m/s라서 길이를 m로 맞춰."),
       ("hc = 6.6 × 10<sup>−34</sup> × 3.0 × 10<sup>8</sup> = 19.8 × 10<sup>−26</sup> J·m", "앞 숫자끼리 곱하고, 지수끼리 더하기: −34 + 8 = −26."),
       ("E = 19.8 × 10<sup>−26</sup> ÷ 6.6 × 10<sup>−7</sup> = <b>3.0 × 10<sup>−19</sup> J</b>", "19.8 ÷ 6.6 = 3, 지수 −26 − (−7) = −19."),
       ("× 6.0 × 10<sup>23</sup> = 18 × 10<sup>4</sup> J = <b>180 kJ</b>", "−19 + 23 = 4."),
       ("E ∝ 1/λ → 파장이 반(330 nm)이면 에너지 <b>2배</b>", "")],
one="E = hc/λ (λ는 m!) × 6.0×10²³. 파장 반 = 에너지 두 배."),

dict(t="q", id="q-emerson", part=P, kind=["txt", "sa"], title="680 nm + 700 nm를 함께 쬐면 더 좋은 이유", src="원서(5판) 19장 연습문제 26 · 솔루션 수록 (Emerson 증강 효과)",
en="The rate of photosynthesis, measured by O<sub>2</sub> production, is higher when illuminated with light of 680 nm than with 700 nm. However, illumination by a combination of 680 nm and 700 nm gives a higher rate than light of either wavelength alone. Explain.",
q="O<sub>2</sub> 발생으로 잰 광합성 속도는 700 nm보다 680 nm에서 높다. 그런데 680 + 700 nm를 함께 비추면 각각 따로일 때보다 더 높다. 설명하시오.",
a="680 nm는 PSII(P680)와 PSI 모두를, 700 nm는 주로 PSI(P700)만 들뜨게 한다. 비순환 전자 흐름은 두 광계가 직렬로 함께 일해야 최대가 되므로, 두 파장을 같이 주면 두 광계가 균형 있게 들떠 속도가 합보다 커진다(증강 효과).",
steps=[("O<sub>2</sub> 발생 = 물 분해 = <b>PSII</b>가 일해야 함", ""),
       ("700 nm: P680은 거의 못 들뜸 → PSII 느림 → O<sub>2</sub> 적음", "파장이 길어 에너지가 680보다 작음."),
       ("680 nm: PSII는 잘 되지만 PSI가 상대적으로 덜 들떠 병목", ""),
       ("둘 다: 두 광계가 균형 → Z 도식 전체가 막힘 없이 흐름 → <b>합보다 큰 속도</b>", "두 광계가 직렬이라는 증거(Emerson, 1957).")],
one="두 광계는 직렬 → 680(PSII) + 700(PSI)을 같이 줘야 최고 속도 (증강 효과)."),

dict(t="q", id="q-pheo", part=P, kind=["txt", "sa"], title="페오피틴을 막으면 PSII와 PSI는?", src="원서(5판) 19장 연습문제 30 · 솔루션 수록",
en="Predict how an inhibitor of electron passage through pheophytin would affect electron transfer through (a) photosystem II and (b) photosystem I. Explain your reasoning.",
q="페오피틴을 통한 전자 전달을 막는 억제제가 (a) 광계 II, (b) 광계 I의 전자 전달에 미치는 영향을 예측하시오.",
a="(a) PSII 전자 흐름 즉시 정지 — P680의 전자가 PQ로 못 감(O₂ 발생도 정지) (b) PSI는 PQ·b₆f·PC에 남은 전자를 다 쓰면 비순환 흐름이 멈춘다. 다만 순환 전자 흐름은 계속될 수 있다.",
steps=[("페오피틴 = P680 바로 다음 수용체 → 막히면 <b>PSII 출구 봉쇄</b>", "P680⁺도 안 생기니 물 분해도 멈춤."),
       ("PSI는 PC에서 전자를 받아야 하는데, 위에서 새 전자가 안 내려옴 → 남은 PQH<sub>2</sub>·PC를 다 소진하면 NADPH 생산 멈춤", "Z 도식은 직렬!"),
       ("단, PSI 주변의 <b>순환 흐름</b>(P700 → Fd → b<sub>6</sub>f → PC → P700)은 물이 필요 없어 계속 가능 → ATP는 조금 생성", "")],
one="Pheo 차단 → PSII·O₂ 즉시 정지, PSI 비순환은 재고 소진 후 정지(순환은 가능)."),

dict(t="q", id="q-darkatp", part=P, kind=["txt", "sa"], title="불을 끈 뒤에도 잠깐 ATP가 만들어지는 이유", src="원서(5판) 19장 연습문제 31 · 솔루션 수록",
en="A researcher illuminates spinach chloroplasts in the absence of ADP and P<sub>i</sub>, then turns the light off and adds ADP and P<sub>i</sub>. ATP synthesis occurs for a short time in the dark. Explain.",
q="ADP·P<sub>i</sub> 없이 엽록체에 빛을 비춘 뒤, 불을 끄고 ADP·P<sub>i</sub>를 넣었더니 어둠 속에서 잠깐 ATP가 합성되었다. 설명하시오.",
a="빛을 비추는 동안 전자 흐름이 H⁺를 내강으로 퍼내 ΔpH를 만들어 두었다(ADP가 없어 소비되지 않음). 어둠 속에서 ADP·Pᵢ를 넣으면 이 저장된 H⁺ 기울기가 CF₀CF₁을 돌려 ATP를 만들고, 기울기가 다 소진되면 멈춘다.",
steps=[("빛 → 전자 흐름 → H<sup>+</sup> 내강 축적 (ATP 합성효소가 쉬어도 펌프는 일함)", ""),
       ("기울기 = <b>충전된 배터리</b>", ""),
       ("ADP + P<sub>i</sub> 투입 → H<sup>+</sup>가 CF<sub>o</sub>를 지나며 ATP 합성 → 기울기 소진 → 정지", "화학삼투 이론의 강력한 증거(Jagendorf 산-염기 실험과 같은 원리).")],
one="빛 = H⁺ 배터리 충전, ADP = 방전 스위치. 배터리가 바닥나면 끝."),

dict(t="q", id="q-dcmu", part=P, kind=["txt", "sa"], title="제초제 DCMU는 어디를 막을까?", src="원서(5판) 19장 연습문제 32 · 솔루션 수록",
en="Treating chloroplasts with DCMU (3-(3,4-dichlorophenyl)-1,1-dimethylurea, diuron) causes O<sub>2</sub> evolution and photophosphorylation to cease. Adding a Hill reagent (an external electron acceptor) restores O<sub>2</sub> evolution, but not photophosphorylation. How does DCMU act as a weed killer? Suggest a location for its action.",
q="DCMU를 처리하면 O<sub>2</sub> 발생과 광인산화가 멈춘다. 외부 전자 수용체(Hill 시약)를 넣으면 O<sub>2</sub> 발생은 회복되지만 광인산화는 회복되지 않는다. DCMU의 작용 위치와 제초 원리는?",
a="DCMU는 PSII의 PQ_B 결합 자리에 Q 대신 붙어 PSII → 플라스토퀴논(→ cyt b₆f) 전자 흐름을 막는다. Hill 시약이 차단 지점 앞에서 전자를 받아 물 분해(O₂)는 재개되지만, 전자가 b₆f를 거치지 않으니 H⁺ 펌프가 없어 ATP가 안 만들어진다. 결국 식물은 ATP·NADPH를 못 만들어 죽는다.",
steps=[("Table 19-4: DCMU = “PSII의 Q<sub>B</sub> 결합 자리를 두고 <b>경쟁</b>”", ""),
       ("Q<sub>B</sub> 막힘 → PSII에서 PQ 풀로 전자 못 감 → P680<sup>+</sup> 재생 안 됨 → O<sub>2</sub> 정지 / b<sub>6</sub>f 안 돎 → H<sup>+</sup> 펌프 정지 → ATP 정지", ""),
       ("Hill 시약: 차단 <b>앞</b>(PSII 쪽)에서 전자를 가로챔 → 물 분해 재개 → O<sub>2</sub> 회복", "OEC의 H⁺ 4개는 생기지만 b₆f의 8개가 없어 ATP를 만들 만큼 기울기가 안 쌓임."),
       ("결과: ATP·NADPH 없음 → 캘빈 회로 정지 → 잡초 사망", "")],
one="DCMU = Q_B 자리 점령 → PSII → PQ → b₆f 차단. Hill 시약은 O₂만 살리고 ATP는 못 살린다."),

dict(t="q", id="q-ventur", part=P, kind=["txt", "sa"], title="벤투리시딘이 엽록체의 O₂ 발생에 미치는 영향", src="원서(5판) 19장 연습문제 33 · 솔루션 수록",
en="Venturicidin is a powerful inhibitor of the chloroplast ATP synthase, interacting with CF<sub>o</sub> and blocking proton passage. How would venturicidin affect O<sub>2</sub> evolution in well-illuminated chloroplasts? Would your answer change in the presence of an uncoupler such as DNP?",
q="벤투리시딘은 CF<sub>o</sub>의 양성자 통과를 막는다. 빛을 충분히 받는 엽록체에서 O<sub>2</sub> 발생은 어떻게 될까? DNP(짝풀림제)가 함께 있으면 답이 달라지는가?",
a="벤투리시딘만: H⁺가 내강에 꽉 차 역압이 걸려 전자 흐름이 느려지고 O₂ 발생이 크게 줄거나 멈춘다. DNP를 함께 넣으면 H⁺가 막을 그냥 빠져나가 기울기가 해소되므로 전자 흐름과 O₂ 발생은 회복(ATP는 여전히 0).",
steps=[("CF<sub>o</sub> 차단 → H<sup>+</sup>가 빠져나갈 길 없음 → ΔpH가 최대치 → 더 펌프하기 너무 힘듦 → 전자 흐름 ↓ → <b>O<sub>2</sub> ↓</b>", "미토의 올리고마이신과 똑같은 짝지음."),
       ("+ DNP → H<sup>+</sup> 누출 → 역압 해소 → 전자 흐름 재개 → <b>O<sub>2</sub> 회복</b>, 하지만 ATP 합성효소는 막혀 있어 ATP 없음", "")],
one="엽록체도 짝지어져 있다: ATP 합성 막으면 O₂도 멈춤, 짝풀림제로 O₂만 되살아남."),

dict(t="q", id="q-8photon", part=P, kind=["txt", "calc"], title="광자 8개로 O₂ 1개 — 자유에너지 장부", src="원서(5판) 19장 연습문제 37 · 솔루션 수록",
en="Pigments must absorb eight photons for every O<sub>2</sub> produced: 2H<sub>2</sub>O + 2NADP<sup>+</sup> + 8 photons → 2NADPH + 2H<sup>+</sup> + O<sub>2</sub>. ΔG′° for the light-independent production of O<sub>2</sub> is 440 kJ/mol (from Problem 36). Assuming photons of 700 nm and 100% efficiency, calculate the free-energy change for the process.",
q="2H<sub>2</sub>O + 2NADP<sup>+</sup> + 8 photons → 2NADPH + 2H<sup>+</sup> + O<sub>2</sub>. 빛 없는 상태의 ΔG′°는 +440 kJ/mol(5판 문제 36에서 계산). 700 nm 광자(1 einstein ≈ 170 kJ), 효율 100%라면 전체 자유에너지 변화는?",
a="약 −920 kJ/mol (440 − 8 × 170)",
steps=[("빛 없이 물 → NADPH: ΔG′° = <b>+440 kJ/mol</b> (큰 오르막 = 저절로 안 됨)", "물(+0.82 V)에서 NADP⁺(−0.32 V)로 전자를 ‘거꾸로’ 올림."),
       ("광자 8몰이 주는 에너지: 8 × 170 = <b>1360 kJ</b> (에너지 투입 = 계에 −1360)", "700 nm 1 einstein ≈ 171 kJ."),
       ("ΔG = +440 − 1360 = <b>−920 kJ/mol</b> → 빛 덕분에 크게 내리막", "남는 에너지는 H⁺ 기울기(ATP)와 열로.")],
one="오르막 +440을 빛 8 × 170 = 1360으로 덮는다 → ΔG ≈ −920 kJ/mol. (8판 수치 +400이면 −960)"),

dict(t="q", id="q-hill", part=P, kind=["txt", "sa"], title="Hill 시약(페리시안화물)을 넣으면 NADPH가 생길까?", src="원서(5판) 19장 연습문제 38 · 솔루션 수록",
en="Isolated spinach chloroplasts evolve O<sub>2</sub> when illuminated in the presence of potassium ferricyanide (a Hill reagent): 2H<sub>2</sub>O + 4Fe<sup>3+</sup> → O<sub>2</sub> + 4H<sup>+</sup> + 4Fe<sup>2+</sup>. Does this process produce NADPH? Explain.",
q="엽록체에 빛과 페리시안화칼륨(Hill 시약)을 주면 2H<sub>2</sub>O + 4Fe<sup>3+</sup> → O<sub>2</sub> + 4H<sup>+</sup> + 4Fe<sup>2+</sup>로 O<sub>2</sub>가 나온다. NADPH가 만들어지는가?",
a="아니다(거의 안 생긴다). 페리시안화물이 NADP⁺ 대신 최종 전자 수용체가 되어 전자를 가로채기 때문 — 물의 전자가 NADP⁺가 아니라 Fe³⁺로 간다.",
steps=[("Hill 반응 = 빛 + 물 + <b>인공 전자 수용체</b> → O<sub>2</sub>", "Robin Hill(1937): O₂는 CO₂가 아니라 물에서 온다는 걸 보여 줌."),
       ("솔루션: 페리시안화물이 <b>cyt b<sub>6</sub>f와 전자를 두고 경쟁</b>해 전자를 빼냄 → P700은 NADP<sup>+</sup>를 환원할 전자를 못 받음, PSII는 계속 산화되어 O<sub>2</sub>는 발생", ""),
       ("전자가 Fe<sup>3+</sup>로 빠져나가니 NADP<sup>+</sup>까지 가지 못함 → NADPH 없음", ""),
       ("의미: O<sub>2</sub> 발생(물 분해)과 CO<sub>2</sub> 고정은 별개 → 명반응만 따로 일어날 수 있다", "")],
one="Hill 시약 = 전자 가로채기 → O₂는 나오지만 NADPH는 없다."),

dict(t="q", id="q-680-700", part=P, kind=["txt", "sa"], title="700 nm는 산화시키고 680 nm는 환원시키는 이유", src="원서(5판) 19장 연습문제 40 · 솔루션 수록",
en="Illuminating chloroplasts with 700 nm light oxidizes cytochrome f, plastocyanin, and plastoquinone. Illuminating with 680 nm light, however, reduces these electron carriers. Explain.",
q="엽록체에 700 nm 빛을 비추면 cyt f·plastocyanin·plastoquinone이 <b>산화</b>되고, 680 nm 빛을 비추면 <b>환원</b>된다. 설명하시오.",
a="700 nm는 PSI만 들뜨게 해 PSI가 PC·cyt f·PQ의 전자를 끌어가기만 하고(PSII가 채워 주지 않음) → 산화. 680 nm는 PSII를 들뜨게 해 물의 전자를 PQ·b₆f·PC로 밀어 넣으므로 → 환원.",
steps=[("세 운반체는 <b>PSII와 PSI 사이</b>에 있다 (Z 도식의 중간 계단)", ""),
       ("700 nm → P700만 → 아래쪽(PSI)이 전자를 <b>빼감</b>, 위쪽(PSII)은 안 채움 → 중간이 텅 빔 = <b>산화</b>", "꽉 막힌 도로의 반대: 출구만 열림."),
       ("680 nm → P680 주로 → 위쪽이 전자를 <b>밀어 넣음</b>, PSI는 덜 빼감 → 중간이 가득 = <b>환원</b>", ""),
       ("→ 두 광계가 그 사이 운반체를 끼고 <b>직렬</b>로 있다는 증거", "")],
one="두 광계 사이 운반체: PSI만 켜면 비고(산화), PSII만 켜면 찬다(환원)."),

dict(t="q", id="q-cyclic", part=P, kind=["txt", "sa"], title="순환 광인산화의 기능", src="원서(5판) 19장 연습문제 41 · 솔루션 수록",
en="When the [NADPH]/[NADP<sup>+</sup>] ratio in chloroplasts is high, photophosphorylation is predominantly cyclic. Does cyclic electron transfer evolve O<sub>2</sub>? Does it produce NADPH? Explain. What is the main function of cyclic electron transfer?",
q="[NADPH]/[NADP<sup>+</sup>]가 높으면 광인산화는 주로 순환형이 된다. 순환 전자 흐름은 O<sub>2</sub>를 내는가? NADPH를 만드는가? 주된 기능은?",
a="O₂ 발생 없음(PSII 미관여), NADPH 생산 없음(전자가 NADP⁺ 대신 b₆f로 되돌아감). 기능 = 양성자 기울기를 만들어 ATP만 추가로 생산 → 캘빈 회로의 ATP:NADPH = 3:2 수요를 맞춤.",
steps=[("경로: P700 → Fd → <b>cyt b<sub>6</sub>f</b> → PC → P700 (돌고 돎)", "물도 NADP⁺도 등장하지 않음."),
       ("O<sub>2</sub>: PSII를 안 쓰니 <b>없음</b> / NADPH: 전자가 FNR로 안 가니 <b>없음</b>", ""),
       ("b<sub>6</sub>f를 지나며 H<sup>+</sup> 펌프 → <b>ATP만</b>", ""),
       ("캘빈 회로는 CO<sub>2</sub> 1개당 ATP 3 : NADPH 2 필요 → 비순환만으로는 ATP가 모자람 → 순환으로 보충", "NADPH가 남아돌 때(비율 ↑) 순환 모드 ON.")],
one="순환 = O₂ ×, NADPH ×, ATP ○. 캘빈 회로의 모자란 ATP를 채우는 보조 발전기."),

dict(t="q", id="q-compare", part=P, kind=["chk", "multi"], title="미토콘드리아 vs 엽록체 — 옳은 것 모두", src="개념확인 · 다답형 · 슬라이드 114",
q="미토콘드리아의 산화적 인산화와 엽록체의 광인산화를 비교한 설명으로 <b>옳은 것을 모두</b> 고르시오." + opts(
"두 경우 모두 ATP 합성효소의 F<sub>1</sub>(CF<sub>1</sub>)은 N쪽(기질, 스트로마)에서 ATP를 만든다.",
"미토는 H<sup>+</sup>를 기질에서 막사이공간으로, 엽록체는 스트로마에서 틸라코이드 내강으로 퍼낸다.",
"엽록체의 최종 전자 수용체는 O<sub>2</sub>, 미토의 최종 전자 수용체는 NADP<sup>+</sup>이다.",
"엽록체의 양성자 구동력은 주로 ΔpH(약 3 단위)로 이루어진다.",
"cyt b<sub>6</sub>f는 미토의 Complex III에, plastocyanin은 cyt c에 해당한다."),
a="①, ②, ④, ⑤",
opx=ox(("①", True, "F<sub>1</sub>은 언제나 N쪽."), ("②", True, "엽록체는 ‘안으로’ 펌프."), ("③", False, "반대: 미토 → O<sub>2</sub>, 엽록체 → NADP<sup>+</sup>."),
       ("④", True, "Δψ는 이온 이동으로 상쇄."), ("⑤", True, "둘 다 Q 회로 / 둘 다 수용성 1전자 운반체.")),
one="미토: NADH → O₂, 밖으로 펌프 / 엽록체: H₂O → NADP⁺, 안으로 펌프. ATP는 둘 다 N쪽."),
]
