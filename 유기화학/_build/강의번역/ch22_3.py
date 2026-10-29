# -*- coding: utf-8 -*-
# 제22장 슬라이드 25–36 + 연습문제 22-37, 22-38, 22-42, 22-54
from fig import row, cap, svg

PHB1 = row(('m', 'N#CCc1ccccc1', 88, 60), ('a', 'EtOH', 'H⁺'),
           ('m', 'CCOC(=O)Cc1ccccc1', 120, 62), ('a', '(EtO₂C)₂', 'NaOEt'),
           ('m', 'CCOC(=O)C(=O)C(c1ccccc1)C(=O)OCC', 150, 82))
PHB2 = row(('a', '가열', '−CO'), ('m', 'CCOC(=O)C(c1ccccc1)C(=O)OCC', 100, 72),
           ('a', '1. NaOEt', '2. EtBr'), ('m', 'CCOC(=O)C(CC)(c1ccccc1)C(=O)OCC', 100, 78),
           ('a', '요소', 'NaOEt'), ('m', 'CCC1(c2ccccc2)C(=O)NC(=O)NC1=O', 95, 78))

# 22-37 정답: 산성 수소(분홍)
F37 = ('<div style="display:flex;flex-wrap:wrap;gap:4px 10px;align-items:flex-end">'
       + cap('CC[C]([H:1])(C)C(=O)C([H:1])([H:1])[H:1]', '(a) α-H 4개', 165, 125)
       + cap('O=C1C([H:1])([H:1])C(=O)C([H:1])([H:1])C1([H:1])[H:1]', '(b) α-H 6개 (C2가 가장 산성)', 165, 125)
       + cap('[H:1]OCC([H:1])([H:1])C(=O)C#CC', '(c) α-CH₂ + O–H', 185, 115)
       + cap('COC(=O)c1ccccc1C([H:1])([H:1])C#N', '(d) CH₂CN의 H 2개', 165, 125)
       + cap('ClC(=O)C1([H:1])CCCC1', '(e) α-H 1개', 140, 110)
       + cap('CC([H:1])([H:1])C(=O)C(C)=C', '(f) α-CH₂ 2개', 150, 110)
       + '</div>')

F38 = ('<div style="font-size:11px;margin-bottom:2px"><b>산성도 증가 순서</b> (약한 산 → 강한 산)</div>'
       '<div style="display:flex;align-items:center;flex-wrap:wrap;gap:0 2px">'
       + cap('CCN([H:1])CC', '(c) pKa ≈ 36', 95, 80) + '<b>&lt;</b>'
       + cap('CC(=O)C', '(d) 19', 80, 80) + '<b>&lt;</b>'
       + cap('CC[O][H:1]', '(b) 16', 80, 80) + '<b>&lt;</b>'
       + cap('CC(=O)CC(C)=O', '(e) 9', 110, 80)
       + '</div><div style="display:flex;align-items:center;gap:0 2px;margin-left:60px">'
       + '<b>&lt;</b>' + cap('CCC(=O)O[H:1]', '(a) 4.8', 100, 85) + '<b>&lt;</b>'
       + cap('ClC(Cl)(Cl)C(=O)O[H:1]', '(f) 0.7', 110, 90)
       + '</div><div class="note" style="margin-top:4px">분홍 = 실제로 떨어지는 H (표시 없는 (d)(e)는 α-H)</div>')

F42 = (row(('m', 'OC(=O)C1(C(=O)O)CCCCC1', 100, 62), ('a', '가열', ''),
           ('m', 'OC(=O)C1CCCCC1', 90, 62), ('t', '+ CO₂'), label='(a)')
       + row(('m', 'O=C1CCC(=O)C1', 80, 58), ('a', '1. NaOEt', '2. CH₃I'),
             ('m', 'CC1C(=O)CCC1=O', 85, 62), label='(b)')
       + row(('m', 'CCCC(=O)O', 80, 50), ('a', 'Br₂, PBr₃', ''),
             ('m', 'CCC(Br)C(=O)Br', 85, 58), ('a', 'H₂O', ''),
             ('m', 'CCC(Br)C(=O)O', 85, 58), label='(c)')
       + row(('m', 'CC(=O)c1ccccc1', 90, 58), ('a', 'NaOH, H₂O', 'I₂ (과량)'),
             ('m', '[O-]C(=O)c1ccccc1', 95, 58), ('t', 'Na⁺ + CHI₃↓'), label='(d)'))

F54 = (row(('m', 'COC(=O)C1CCCCC1=O', 105, 90), ('a', 'a', ''),
           ('m', 'COC(=O)C1(C)CCCCC1=O', 105, 90), ('a', 'b', ''),
           ('m', 'CC1CCCCC1=O', 85, 85), ('a', 'c', ''),
           ('m', 'CC1CCCC(C)C1=O', 105, 85))
       + '<table class="t" style="margin-top:8px;font-size:11.5px"><tr><th>칸</th><th>시약</th><th>반응</th></tr>'
       '<tr><td><b>a</b></td><td>1. NaOCH₃, CH₃OH &nbsp;2. CH₃I</td><td>β-케토 에스터 알킬화</td></tr>'
       '<tr><td><b>b</b></td><td>H₃O⁺, 가열</td><td>가수분해 + 탈카르복실화</td></tr>'
       '<tr><td><b>c</b></td><td>1. LDA, THF &nbsp;2. CH₃I</td><td>케톤 직접 알킬화</td></tr></table>')

PAGES = [
# 25
dict(img=25, slide=25, title="말론산 에스터 합성 ① — 엔올레이트 형성과 알킬화", sub="Formation of Enolate and Alkylation",
kw=["말론산 다이에틸", "NaOEt / EtOH", "소디오 말론산 에스터", "α-알킬 말론산 에스터"],
sum="말론산 에스터(pKa 13)는 에탄올 속 NaOEt로 쉽게 엔올레이트가 되고, 이 엔올레이트가 알킬 할라이드와 빠르게 반응해 α-치환 말론산 에스터가 된다.",
tr="""<ul><li>말론산 에스터(다이에틸 프로페인다이오에이트)는 에탄올 속 <b>소듐 에톡사이드</b>와 반응해 쉽게 엔올레이트 이온이 된다.</li>
<li>엔올레이트는 <b>좋은 친핵체</b>로, 알킬 할라이드와 빠르게 반응해 <b>α-치환 말론산 에스터</b>를 만든다.</li></ul>
<p class="note">그림: 다이에틸 프로페인다이오에이트(말론산 에스터) EtO₂C–CH₂–CO₂Et —Na⁺ ⁻OEt, EtOH→ [소디오 말론산 에스터(Sodio malonic ester) EtO₂C–CH⁻–CO₂Et Na⁺] —RX→ 알킬화 말론산 에스터(An alkylated malonic ester) EtO₂C–CHR–CO₂Et</p>""",
ex="""<p><b>왜 NaOEt면 충분?</b> 말론산 에스터 pKa 13 &lt; 에탄올 pKa 16 → 평형이 <y>엔올레이트 쪽으로 거의 완전히</y> 기울어 (슬 17).</p>
<p><b>왜 하필 NaOEt (NaOMe·NaOH 아님)?</b></p>
<ul><li>NaOMe를 쓰면 에톡시 에스터가 메톡시로 바뀌는 <b>에스터 교환</b>이 섞여(21장).</li>
<li>NaOH를 쓰면 에스터가 <b>가수분해</b>(비누화)돼 버려.</li>
<li>→ 에스터의 OR과 <g>같은 알콕사이드</g>를 쓰면 교환이 일어나도 같은 물질이라 문제없음.</li></ul>
<p><b>알킬화 메커니즘</b>: 엔올레이트 가운데 탄소(C⁻) → R–X의 C 공격, X⁻ 이탈 (S<sub>N</sub>2, 슬 22). R의 제약은 슬 23 그대로.</p>
<div class="box"><span class="tag">메커니즘 그리기</span>① EtO⁻가 가운데 CH₂의 H를 뗌 (엔올레이트 공명 3개 그려두면 가산점) ② C⁻가 R–X 공격 → X⁻ 이탈.</div>"""),

# 26
dict(img=26, slide=26, title="말론산 에스터 합성 ② — 다이알킬화", sub="Dialkylation",
kw=["남은 α-H", "두 번째 알킬화", "R ≠ R′ 가능", "이치환 아세트산"],
sum="모노알킬 말론산 에스터에도 산성 α-H가 하나 남아 있어서 NaOEt/R′X로 한 번 더 알킬화할 수 있다 → 다이알킬 말론산 에스터.",
tr="""<ul><li>생성물에 <b>산성 α-수소</b>가 남아 있어서 알킬화 과정을 <b>반복</b>할 수 있다.</li></ul>
<p class="note">그림: 알킬화 말론산 에스터(An alkylated malonic ester) EtO₂C–CHR–CO₂Et —Na⁺ ⁻OEt, EtOH→ [EtO₂C–C⁻R–CO₂Et Na⁺] —R′X→ 다이알킬화 말론산 에스터(A dialkylated malonic ester) EtO₂C–CRR′–CO₂Et</p>""",
ex="""<p>α 탄소에는 원래 H가 <b>2개</b>니까 알킬화도 <y>최대 2번</y>.</p>
<table class="t"><tr><th>알킬화 횟수</th><th>가수분해·탈카르복실화 후</th></tr>
<tr><td>1번 (R)</td><td>R–CH₂–COOH</td></tr>
<tr><td>2번 (R, R′)</td><td><g>RR′CH–COOH</g> (α 탄소에 가지 2개)</td></tr></table>
<p><b>순서</b>: 반드시 “NaOEt → RX”를 <b>한 세트씩</b> 두 번. NaOEt를 2당량 한꺼번에 넣고 RX, R′X를 섞으면 생성물이 뒤섞여.</p>
<p><b>두 번째가 첫 번째보다 느린 이유</b>: R이 붙어서 입체 장애 ↑, 알킬기가 전자를 밀어 음이온 안정성 ↓. 그래도 1°·메틸이면 잘 돼.</p>
<div class="box"><span class="tag">역합성 요령</span>목표 산의 α 탄소에 H가 <b>1개</b>만 남아 있으면 → 알킬화 2번 (R–X와 R′–X 둘 다 써야 해). 슬 29의 2-메틸헥산산 예.</div>"""),

# 27
dict(img=27, slide=27, title="말론산 에스터 합성 ③ — 가수분해와 탈카르복실화", sub="Hydrolysis and Decarboxylation",
kw=["H₃O⁺, 가열", "에스터 가수분해", "탈카르복실화(−CO₂)", "치환 아세트산"],
sum="알킬 말론산 에스터를 산성 수용액에서 가열하면 두 에스터가 가수분해되어 말론산이 되고, CO₂가 빠져(탈카르복실화) 치환된 모노카르복실산이 된다.",
tr="""<ul><li>말론산 에스터 유도체는 산에서 <b>가수분해</b>되고 <b>CO₂를 잃어(탈카르복실화)</b> 치환된 모노산을 만든다.</li></ul>
<p class="note">그림: 알킬화 말론산 에스터(An alkylated malonic ester) R–CH(CO₂Et)₂ —H₃O⁺, 가열(Heat)→ 카르복실산(A carboxylic acid) R–CH₂–CO₂H + CO₂ + 2 EtOH</p>""",
ex="""<p>H₃O⁺/가열 한 줄에 <b>두 반응</b>이 들어 있어.</p>
<ol><li><b>가수분해</b> (21장 산 촉매 에스터 가수분해): –CO₂Et 두 개 → –COOH 두 개 + 2 EtOH. 중간 생성물 = <y>치환 말론산 R–CH(COOH)₂</y></li>
<li><b>탈카르복실화</b>: COOH 하나가 CO₂로 빠짐 → <g>R–CH₂–COOH</g> (메커니즘은 다음 슬라이드)</li></ol>
<div class="boxg"><b>원자 장부</b> R–CH(CO₂Et)₂ + 2 H₂O → R–CH(CO₂H)₂ + 2 EtOH → R–CH₂–CO₂H + CO₂</div>
<p><b>왜 가열?</b> 탈카르복실화는 활성화 에너지가 커서 열(보통 100–150 °C)이 필요해.</p>
<div class="box"><span class="tag">생성물 예측</span>가열 조건에서 COOH가 같은 탄소에 2개(gem-이산) → 반드시 1개만 남아. 연습문제 22-42 (a) 사이클로헥세인-1,1-다이카르복실산이 바로 이거야.</div>"""),

# 28
dict(img=28, slide=28, title="β-케토산의 탈카르복실화 메커니즘", sub="Decarboxylation of β-Ketoacids",
kw=["β 위치 C=O 필요", "6원 고리 전이상태", "엔올 중간체", "토토머화"],
sum="탈카르복실화에는 –CO₂H에서 두 원자 떨어진 곳(β 위치)에 카르보닐이 있어야 한다. 6원 고리 전이상태에서 CO₂가 빠지며 엔올이 생기고, 엔올이 토토머화해 산 또는 케톤이 된다.",
tr="""<ul><li>탈카르복실화에는 –CO₂H에서 <b>두 원자 떨어진 곳에 카르보닐기</b>가 필요하다.</li></ul>
<p class="note">그림 위: 이산(A diacid) —−CO₂→ [산 엔올(An acid enol)] → 카르복실산(A carboxylic acid)</p>
<p class="note">그림 아래: β-케토산(A β-keto acid) —−CO₂→ [엔올(An enol)] → 케톤(A ketone)</p>""",
ex="""<p><b>6원 고리 고리형 메커니즘</b> (화살표 3개가 동시에)</p>
<ol><li>COOH의 <b>O–H 결합 전자쌍</b> → C=O를 하나 더 만들어 O=C=O(CO₂)가 될 준비.</li>
<li>COOH 탄소와 α 탄소 사이 <b>C–C 결합 전자쌍</b> → α 탄소와 옆 카르보닐 탄소 사이 <b>C=C</b> 형성 (CO₂ 떨어져 나감).</li>
<li>옆 카르보닐의 <b>C=O π 전자</b> → 산소가 COOH의 H를 받아 O–H가 됨.</li></ol>
<p>→ 결과: <y>엔올</y> + CO₂. 엔올은 곧바로 토토머화(슬 2–5)해서 <g>카르보닐 형태</g>로.</p>
<table class="t"><tr><th>출발물질</th><th>엔올</th><th>최종</th></tr>
<tr><td>말론산 (이산)</td><td>산 엔올</td><td>카르복실산</td></tr>
<tr><td>β-케토산</td><td>엔올</td><td>케톤</td></tr></table>
<div class="box"><span class="tag">메커니즘 그리기</span>시험 단골! <b>6원 고리</b>(O=C–C–C(=O)–O–H)를 그리고 화살표 3개 → 엔올 → 토토머화. “CO₂가 그냥 떨어진다”고만 쓰면 감점. 그리고 <b>γ-케토산(카르보닐이 더 멀면)은 탈카르복실화 안 됨</b>.</div>"""),

# 29
dict(img=29, slide=29, title="말론산 에스터 합성 — 전체 변환 예", sub="Overall Conversion · hexanoic acid & 2-methylhexanoic acid",
kw=["1-브로모뷰테인", "헥산산 75%", "CH₃I 두 번째 알킬화", "2-메틸헥산산 74%"],
sum="1-브로모뷰테인 + 말론산 에스터 → (NaOEt) 알킬화 → (H₃O⁺, 가열) 헥산산. 중간에 NaOEt/CH₃I로 한 번 더 알킬화하면 2-메틸헥산산.",
tr="""<ul><li>말론산 에스터 합성은 알킬 할라이드를 <b>탄소 사슬이 두 개 늘어난</b> 카르복실산으로 바꾼다.</li></ul>
<p class="note">그림: 1-브로모뷰테인(1-Bromobutane) + 말론산 에스터 —Na⁺ ⁻OEt, EtOH→ CH₃CH₂CH₂CH₂–CH(CO₂Et)₂ —H₃O⁺, 가열→ 헥산산(Hexanoic acid, 75%)</p>
<p class="note">↓ 1. Na⁺ ⁻OEt 2. CH₃I → CH₃CH₂CH₂CH₂–C(CH₃)(CO₂Et)₂ —H₃O⁺, 가열→ 2-메틸헥산산(2-Methylhexanoic acid, 74%)</p>""",
ex="""<p><b>탄소 세기</b></p>
<table class="t"><tr><th></th><th>R–X에서</th><th>말론산에서</th><th>합</th></tr>
<tr><td>헥산산 (C6)</td><td>뷰틸 C4</td><td>CH₂ + COOH = C2</td><td>C6 ○</td></tr>
<tr><td>2-메틸헥산산 (C7)</td><td>뷰틸 C4 + 메틸 C1</td><td>C + COOH = C2</td><td>C7 ○</td></tr></table>
<p><b>흐름</b>: “엔올레이트 → 알킬화 → (필요하면 반복) → 가수분해/탈카르복실화” 네 박자. 슬라이드 25–28을 한 장에 모은 거야.</p>
<div class="boxg"><b>시약 쓰기 정답 형식</b> ① Na⁺ ⁻OEt, EtOH ② CH₃(CH₂)₃Br ③ Na⁺ ⁻OEt, EtOH ④ CH₃I ⑤ H₃O⁺, 가열</div>
<div class="box"><span class="tag">반응 사다리</span>시험에서 “반응 순서 배열”로 나오면 <b>알킬화(들)이 반드시 가수분해·탈카르복실화보다 먼저</b>. 탈카르복실화하고 나면 α-H 산성도가 확 떨어져서(pKa 13 → ~25) NaOEt로는 더 알킬화가 안 돼.</div>"""),

# 30
dict(img=30, slide=30, title="사이클로알케인 카르복실산 만들기", sub="Preparation of Cycloalkane Carboxylic Acids",
kw=["1,4-다이브로모뷰테인", "분자 내 알킬화", "3–6원 고리", "사이클로펜탄카르복실산"],
sum="1,4-다이브로모뷰테인은 말론산 에스터와 두 번 반응(첫 번째는 분자 간, 두 번째는 분자 내)해서 고리를 만든다. 가수분해·탈카르복실화하면 사이클로펜탄카르복실산.",
tr="""<ul><li>1,4-다이브로모뷰테인은 <b>두 번 반응</b>해서 고리형 생성물을 만든다.</li>
<li>이 방법으로 <b>3, 4, 5, 6원 고리</b>를 만들 수 있다.</li></ul>
<p class="note">그림: 1,4-다이브로모뷰테인(1,4-Dibromobutane) + 말론산 에스터 엔올레이트 —Na⁺ ⁻OEt, EtOH→ Br(CH₂)₄CH(CO₂Et)₂ —Na⁺ ⁻OEt, EtOH→ (분자 내 S<sub>N</sub>2) 사이클로펜테인-1,1-다이카르복실산 다이에틸 —H₃O⁺, 가열→ 사이클로펜탄카르복실산(Cyclopentanecarboxylic acid) + CO₂ + 2 EtOH</p>""",
ex="""<ol><li><b>1차 알킬화(분자 간)</b>: 엔올레이트가 Br–CH₂(CH₂)₃–Br의 한쪽 끝을 공격 → Br(CH₂)₄–CH(CO₂Et)₂. 반대쪽 끝에 <y>Br이 하나 남아</y> 있어.</li>
<li><b>2차 알킬화(분자 내)</b>: NaOEt로 다시 엔올레이트 → 같은 분자의 C–Br을 공격 → <g>5원 고리</g> 형성. (말론산 탄소 1개 + 사슬 4개 = 5원)</li>
<li><b>가수분해·탈카르복실화</b> → 고리에 COOH 1개.</li></ol>
<table class="t"><tr><th>다이할라이드</th><th>고리 크기</th><th>생성물</th></tr>
<tr><td>Br(CH₂)₂Br</td><td>3원</td><td>사이클로프로페인카르복실산</td></tr>
<tr><td>Br(CH₂)₃Br</td><td>4원</td><td>사이클로뷰테인카르복실산</td></tr>
<tr><td>Br(CH₂)₄Br</td><td>5원</td><td>사이클로펜테인카르복실산</td></tr>
<tr><td>Br(CH₂)₅Br</td><td>6원</td><td>사이클로헥세인카르복실산</td></tr></table>
<div class="box"><span class="tag">공식</span>고리 크기 = (CH₂ 개수) + 1. 22-42 (a)의 사이클로헥세인-1,1-다이카르복실산은 Br(CH₂)₅Br로 만든 거야.</div>"""),

# 31
dict(img=31, slide=31, title="아세토아세트산 에스터 합성 (아세토아세트산 에틸)", sub="Acetoacetic Ester (Ethyl Acetoacetate) Synthesis",
kw=["β-케토 에스터", "pKa 11", "모노·다이알킬화", "메틸 케톤 합성"],
sum="아세토아세트산 에틸의 α 탄소는 두 카르보닐 사이에 있어 쉽게 엔올레이트가 되고, 알킬 할라이드로 한 번 또는 두 번 알킬화된다. 이후 가수분해·탈카르복실화하면 메틸 케톤.",
tr="""<ul><li>α 탄소가 <b>두 카르보닐기 사이</b>에 있으므로 쉽게 엔올레이트 이온이 된다.</li>
<li>이 엔올레이트는 알킬 할라이드로 알킬화될 수 있고, <b>두 번째 알킬 할라이드</b>와도 반응할 수 있다.</li></ul>
<p class="note">그림: 아세토아세트산 에틸(Ethyl acetoacetate) —Na⁺ ⁻OEt, EtOH→ [소디오 아세토아세트산 에스터] —RX→ 모노알킬화 아세토아세트산 에스터 —Na⁺ ⁻OEt, EtOH→ [엔올레이트] —R′X→ 다이알킬화 아세토아세트산 에스터</p>""",
ex="""<p>말론산 에스터 합성과 <b>쌍둥이</b>야. 차이는 끝 생성물뿐.</p>
<table class="t"><tr><th></th><th>말론산 에스터</th><th>아세토아세트산 에스터</th></tr>
<tr><td>구조</td><td>EtO₂C–CH₂–CO₂Et</td><td>CH₃CO–CH₂–CO₂Et</td></tr>
<tr><td>pKa</td><td>13</td><td>11</td></tr>
<tr><td>염기</td><td>NaOEt</td><td>NaOEt</td></tr>
<tr><td>H₃O⁺, 가열 후</td><td><g>카르복실산</g> R–CH₂–COOH</td><td><g>메틸 케톤</g> R–CH₂–COCH₃</td></tr>
<tr><td>탈카르복실화 형태</td><td>말론산(이산)</td><td>β-케토산 (슬 28 아래)</td></tr></table>
<p><b>역합성 요령</b>: 목표가 <y>CH₃–CO–CH₂–R(또는 CHRR′)</y> 모양의 메틸 케톤이면 아세토아세트산 에스터 합성. C=O 옆 CH₃는 아세토아세트산의 아세틸기에서 와.</p>
<div class="box"><span class="tag">시험 포인트</span>예: 2-헵타논 CH₃CO–CH₂–(CH₂)₃CH₃ = 아세토아세트산 에틸 + <b>1-브로모뷰테인</b>. 목표 산물 → 필요한 R–X를 거꾸로 찾는 문제가 잘 나와.</div>"""),

# 32
dict(img=32, slide=32, title="일반화 — β-케토 에스터의 알킬화", sub="Generalization: β-Keto Esters",
kw=["엔올레이트 형성", "알킬화", "가수분해/탈카르복실화", "2-치환 사이클로헥사논"],
sum="모든 β-케토 에스터에 같은 3단계(엔올레이트 → 알킬화 → 가수분해·탈카르복실화)가 통한다. 고리형 β-케토 에스터는 2-치환 사이클로헥사논을 준다.",
tr="""<ul><li><b>순서</b>
<ul><li>엔올레이트 이온 형성</li><li>알킬화</li><li>가수분해/탈카르복실화</li></ul></li>
<li><b>고리형 β-케토 에스터</b>는 <b>2-치환 사이클로헥사논</b>을 준다.</li></ul>
<p class="note">그림: 에틸 2-옥소사이클로헥세인카르복실레이트(Ethyl 2-oxocyclohexanecarboxylate, 고리형 β-케토 에스터) —1. Na⁺ ⁻OEt 2. PhCH₂Br→ 2-벤질-2-에톡시카르보닐 사이클로헥사논 —H₃O⁺, 가열→ 2-벤질사이클로헥사논(2-Benzylcyclohexanone, 77%) + CO₂ + EtOH</p>""",
ex="""<p><b>예시 단계별</b></p>
<ol><li><b>Na⁺ ⁻OEt</b>: C=O와 CO₂Et 사이 C–H(파란 H)를 떼어 엔올레이트.</li>
<li><b>PhCH₂Br</b>: 벤질 브로마이드 = 슬 23에서 가장 좋은 기질 → S<sub>N</sub>2로 <y>그 탄소에 벤질기</y>.</li>
<li><b>H₃O⁺, 가열</b>: 에스터 가수분해 → β-케토산 → 탈카르복실화(슬 28) → <g>2-벤질사이클로헥사논</g>.</li></ol>
<div class="boxg"><b>핵심 장점</b> 사이클로헥사논에 직접 염기 + PhCH₂Br을 쓰면 여러 번 알킬화되거나 위치가 섞이는데, β-케토 에스터를 쓰면 <b>CO₂Et가 “여기만 반응해”라고 위치를 지정</b>해 주고, 일 끝나면 CO₂로 날아가.</div>
<div class="box"><span class="tag">연결</span>연습문제 <b>22-54</b>가 바로 이 반응(a: 알킬화, b: 가수분해·탈카르복실화) + LDA 직접 알킬화(c) 조합이야.</div>"""),

# 33
dict(img=33, slide=33, title="페노바르비탈 합성 — 빈칸 채우기", sub="Synthesis of phenobarbital (Wikimedia Commons: Phenobarbital_synthesis)",
kw=["에스터화", "Claisen 축합(다이에틸 옥살레이트)", "탈카르보닐화", "말론산 에스터 알킬화", "요소와 고리화"],
sum="벤질 사이아나이드 → 페닐아세트산 에틸 → (옥살산 다이에틸) 축합 → 가열(−CO) 페닐말론산 다이에틸 → NaOEt/EtBr 알킬화 → 요소로 고리화 = 페노바르비탈.",
tr="""<p><b>페노바르비탈(phenobarbital)의 합성</b></p>
<ul><li>최초 시판: 1912년</li>
<li>약물 계열: <b>바르비튜레이트(Barbiturate)</b></li>
<li>주요 용도: <b>항경련제</b></li>
<li>식품의약품안전처(MFDS) / FDA 승인 제형: Sezaby (페노바르비탈 소듐 주사제)</li></ul>
<p class="note">그림: 벤질 사이아나이드 —EtOH/AcOH→ [ ? ] —다이에틸 옥살레이트(diethyl oxalate)→ [ ? ] —가열(Heat)→ 페닐말론산 다이에틸 —1. NaOEt 2. EtBr→ [ ? ] —요소(urea)→ 페노바르비탈</p>""",
ex=f"""<p><b>빈칸 정답</b></p>{PHB1}{PHB2}
<ol><li><b>EtOH / 산</b>: 니트릴의 산 촉매 알코올분해 → <y>페닐아세트산 에틸</y> PhCH₂CO₂Et.</li>
<li><b>다이에틸 옥살레이트</b> (NaOEt): 에스터 엔올레이트가 옥살산 에스터 C=O를 공격 → EtO⁻ 이탈 (다음 장 <b>Claisen 축합</b>). α-케토 에스터 생성.</li>
<li><b>가열</b>: CO가 빠져(탈카르보닐화) <g>페닐말론산 다이에틸</g>. 페닐은 S<sub>N</sub>2로 못 붙이니까(아릴 할라이드 ×, 슬 23) 이렇게 우회해.</li>
<li><b>1. NaOEt 2. EtBr</b>: 말론산 에스터 알킬화 (슬 25). 에틸페닐말론산 다이에틸.</li>
<li><b>요소</b>: 요소 NH₂가 두 에스터를 차례로 공격(친핵성 아실 치환 ×2) → 6원 고리 이미드.</li></ol>"""),

# 34
dict(img=34, slide=34, title="케톤·에스터·니트릴의 직접 알킬화 ① — 락톤과 에스터", sub="Direct Alkylation of Ketones, Esters, and Nitriles",
kw=["LDA, THF", "완전한 엔올레이트화", "뷰티로락톤", "2,2-다이메틸프로파노에이트"],
sum="케톤, 에스터, 니트릴은 THF 속 LDA(또는 비슷한 다이알킬아마이드 염기)로 엔올레이트를 만든 뒤 바로 알킬화할 수 있다. 1,3-다이카르보닐이 아니어도 된다.",
tr="""<ul><li>케톤, 에스터, 니트릴은 모두 THF 속 <b>LDA</b> 또는 관련된 다이알킬아마이드 염기를 이용해 알킬화될 수 있다.</li></ul>
<p class="note">그림 (락톤, Lactone): 뷰티로락톤(Butyrolactone) —LDA, THF→ [엔올레이트] —CH₃I→ 2-메틸뷰티로락톤(2-Methylbutyrolactone, 88%)</p>
<p class="note">그림 (에스터, Ester): 에틸 2-메틸프로파노에이트(Ethyl 2-methylpropanoate) —LDA, THF→ [엔올레이트] —CH₃I→ 에틸 2,2-다이메틸프로파노에이트(Ethyl 2,2-dimethylpropanoate, 87%)</p>""",
ex="""<p><b>왜 LDA가 필요해?</b> 에스터 α-H pKa ≈ 25 → NaOEt(16)로는 엔올레이트가 거의 안 생기고, 대신 에스터끼리 축합(Claisen, 23장)이 일어나. LDA(36)는 <y>빠르고 완전하게</y> 엔올레이트로 바꿔서 남은 에스터가 없으니 부반응이 없어.</p>
<table class="t"><tr><th></th><th>말론산/아세토아세트산 합성</th><th>LDA 직접 알킬화</th></tr>
<tr><td>기질</td><td>1,3-다이카르보닐만</td><td><g>단일 카르보닐도 OK</g></td></tr>
<tr><td>염기</td><td>NaOEt</td><td>LDA, THF, −78 °C</td></tr>
<tr><td>마지막 단계</td><td>가수분해·탈카르복실화 필요</td><td>필요 없음 (한 번에 끝)</td></tr></table>
<p><b>락톤 예</b>: 고리 에스터도 똑같이 α 위치(C=O 옆 CH₂)에 CH₃가 들어가.</p>
<p><b>에스터 예</b>: (CH₃)₂CH–CO₂Et의 α-H 하나 → CH₃ → (CH₃)₃C–CO₂Et. α 탄소가 3차여도 <b>친핵체 쪽</b>이니 괜찮아 (제약은 R–X 쪽에만).</p>
<div class="box"><span class="tag">함정</span>“α 탄소가 붐비면 알킬화 안 된다” ×. S<sub>N</sub>2 제약은 <b>알킬 할라이드</b>에만 적용돼.</div>"""),

# 35
dict(img=35, slide=35, title="직접 알킬화 ② — 비대칭 케톤과 니트릴", sub="Direct Alkylation: ketone regioselectivity · nitrile",
kw=["2-메틸사이클로헥사논", "덜 치환된 쪽 우세", "속도론적 엔올레이트", "페닐아세토니트릴"],
sum="2-메틸사이클로헥사논을 LDA로 처리하면 덜 붐비는 C6 쪽 엔올레이트가 주로 생겨 2,6-다이메틸(56%)이 2,2-다이메틸(6%)보다 많다. 니트릴도 α 위치가 알킬화된다.",
tr="""<p class="note">그림 (케톤, Ketone): 2-메틸사이클로헥사논(2-Methylcyclohexanone) —LDA, THF→ [두 엔올레이트] —CH₃I→ 2,6-다이메틸사이클로헥사논(2,6-Dimethylcyclohexanone, 56%) + 2,2-다이메틸사이클로헥사논(2,2-Dimethylcyclohexanone, 6%)</p>
<p class="note">그림 (니트릴, Nitrile): 페닐아세토니트릴(Phenylacetonitrile) —LDA, THF→ [음이온] —CH₃I→ 2-페닐프로페인니트릴(2-Phenylpropanenitrile, 71%)</p>
<p>(이 슬라이드는 그림만 있고 본문 문장은 없어.)</p>""",
ex="""<p><b>비대칭 케톤의 위치 선택성</b></p>
<table class="t"><tr><th></th><th>C6 쪽 (CH₂)</th><th>C2 쪽 (CH–CH₃)</th></tr>
<tr><td>α-H</td><td>2개, 덜 붐빔</td><td>1개, 붐빔</td></tr>
<tr><td>LDA, −78 °C</td><td><g>빨리 떼어짐 (주생성물)</g></td><td>느림</td></tr>
<tr><td>생성물</td><td>2,6-다이메틸 (56%)</td><td>2,2-다이메틸 (6%)</td></tr></table>
<p>부피 큰 LDA는 <y>입체적으로 쉬운 H</y>를 빨리 떼어내(속도론적 조절). 산성 조건 브로민화(슬 11)가 <b>더 치환된 쪽</b>이었던 것과 반대야!</p>
<div class="boxg"><b>정리</b> 산 촉매 엔올(열역학, 더 치환된 C=C) ↔ LDA 엔올레이트(속도론, 덜 치환된 쪽)</div>
<p><b>니트릴</b>: C≡N도 카르보닐처럼 α 음이온을 안정화해(⁻C–C≡N ↔ C=C=N⁻). 페닐까지 있어서 더 안정 → PhCH(CH₃)CN.</p>
<div class="box"><span class="tag">시약 쓰기</span>22-54 (c)처럼 “2-메틸사이클로헥사논 → 2,6-다이메틸” = <b>1. LDA, THF 2. CH₃I</b>.</div>"""),

# 36
dict(img=36, slide=36, title="그림 22.6 — 인돌릴피루브산에서 인돌마이신 생합성", sub="Figure 22.6 · Biosynthesis of Indolmycin from Indolylpyruvate",
kw=["생체 내 α-알킬화", "엔올화(염기·산)", "SAM 메틸화", "S<sub>N</sub>2", "인돌마이신(항생제)"],
sum="생체에서도 α-치환이 일어난다. 인돌릴피루브산이 효소의 염기·산 도움으로 엔올이 되고, 엔올의 α 탄소가 SAM의 CH₃를 S<sub>N</sub>2로 받아 α-메틸화 → 인돌마이신(항생제)으로.",
tr="""<p class="note">그림: 인돌릴피루브산(Indolylpyruvate) — 염기(:Base)가 α-H 제거, A–H가 C=O 산소 양성자화 → 엔올 → 엔올의 α 탄소가 SAM(S-아데노실메싸이오닌)의 S⁺–CH₃ 메틸을 공격 → α-메틸화 케토산 → (여러 단계) → 인돌마이신(Indolmycin, 항생제)</p>
<p>(그림만 있는 슬라이드야.)</p>""",
ex="""<p>실험실의 “엔올 → E⁺ 공격”이 <y>효소 안에서 그대로</y> 일어나는 예.</p>
<ol><li><b>엔올화</b>: 효소의 염기(:Base)가 α-H를 떼고, 산(A–H)이 C=O 산소에 H⁺를 줘 → 엔올. (산·염기 촉매가 동시에 — 슬 4·5의 합체)</li>
<li><b>메틸화</b>: 엔올의 C=C π 전자가 SAM의 CH₃를 공격, S가 이탈기(중성 황화물) → <g>S<sub>N</sub>2 α-메틸화</g>. 마지막에 다른 염기가 O–H의 H⁺ 제거 → C=O 재생.</li>
<li>이후 여러 단계를 거쳐 인돌마이신.</li></ol>
<table class="t"><tr><th>실험실</th><th>생체</th></tr>
<tr><td>LDA / NaOEt</td><td>효소의 염기 잔기</td></tr>
<tr><td>CH₃I (이탈기 I⁻)</td><td><b>SAM</b> (이탈기 = S-아데노실호모시스테인)</td></tr></table>
<div class="box"><span class="tag">연결</span>SAM은 “생체의 CH₃I”. 약대 생화학·약물대사(메틸화 반응)에서 다시 나와.</div>"""),

# 37 문제 22-37
dict(img="p37", src="연습문제 22-37 · 문제", title="문제 22-37 — 산성 수소(pKa &lt; 25) 찾기", sub="Problem 22-37 — Identify all the acidic hydrogens (pKa &lt; 25)",
kw=["α-H", "pKa &lt; 25", "1,3-다이카르보닐", "O–H도 포함"],
sum="pKa 25보다 작은 산성 수소를 모두 찾는 문제. α-H(카르보닐·니트릴 옆) + O–H를 체크하고, 표 22.1의 값과 비교해.",
tr_label="문제 원문 번역", ex_label="접근 방법 · 핵심 개념",
tr="""<p>다음 분자들에서 산성 수소(pKa &lt; 25)를 모두 찾으시오.</p>
<ul><li>(a) CH₃CH₂CH(CH₃)COCH₃ (3-메틸-2-펜탄온)</li>
<li>(b) 사이클로펜테인-1,3-다이온</li>
<li>(c) HOCH₂CH₂CO–C≡C–CH₃</li>
<li>(d) 2-(사이아노메틸)벤조산 메틸 (벤젠 고리에 –CO₂CH₃와 –CH₂CN)</li>
<li>(e) 사이클로펜테인카르보닐 클로라이드</li>
<li>(f) CH₃CH₂CO–C(CH₃)=CH₂</li></ul>""",
ex="""<ol><li>카르보닐(C=O)과 C≡N을 모두 동그라미 쳐.</li>
<li>그 <y>바로 옆 sp³ 탄소</y>(α 탄소)의 H를 체크. pKa: 케톤 19, 산염화물 16, 니트릴 25 부근.</li>
<li><b>O–H</b>(알코올 16, 카르복실산 5)도 pKa &lt; 25라서 포함!</li>
<li>다음은 <pk>α-H가 아니야</pk>: 벤젠 고리 H, C=C의 바이닐 H, 에스터 OCH₃의 H, sp 탄소 쪽.</li></ol>
<table class="t"><tr><th>확인할 것</th><th>대표 pKa</th></tr>
<tr><td>두 C=O 사이 CH₂</td><td>9–13</td></tr>
<tr><td>케톤 α-H</td><td>19</td></tr>
<tr><td>CH₂–C≡N (벤질이면 더 산성)</td><td>≤ 25</td></tr>
<tr><td>알코올 O–H</td><td>16</td></tr></table>
<div class="box"><span class="tag">힌트</span>(c)는 알킨 쪽에 α-H가 없어(C≡C–C=O). (f)도 C=C 쪽 탄소에는 α-H가 없어. 각 분자에서 α 탄소가 몇 개인지부터 세어봐.</div>"""),

# 38 풀이 22-37
dict(fig=F37, figw=610, src="연습문제 22-37 · 풀이", title="풀이 22-37 — 산성 수소(pKa &lt; 25)", sub="Solution 22-37 — 분홍 = 산성 수소",
kw=["α-H", "O–H", "1,3-다이온", "γ-H는 제외"],
sum="(a) α-H 4개 (b) 고리의 α-H 6개 (c) α-CH₂ + O–H (d) CH₂CN의 H 2개 (e) α-H 1개 (f) α-CH₂ 2개.",
tr_label="정답", ex_label="상세 풀이",
tr="""<ul><li>(a) C=O 양옆 α 탄소: <b>CH₃(3개)</b> + <b>CH(1개)</b> → 4개</li>
<li>(b) C2(두 C=O 사이) H 2개 <b>(pKa ≈ 9, 가장 산성)</b> + C4·C5 H 4개 → 6개</li>
<li>(c) C=O 옆 <b>CH₂</b> 2개 + 알코올 <b>O–H</b> 1개</li>
<li>(d) <b>CH₂CN</b>의 H 2개</li>
<li>(e) 고리의 <b>α-CH</b> 1개 (산염화물 α-H, pKa ≈ 16)</li>
<li>(f) 에틸의 <b>CH₂</b> 2개</li></ul>""",
ex="""<p><b>헷갈리는 것만 정리</b></p>
<ul><li>(b) C4–C5 H는 C=O 하나에만 α라 pKa ≈ 19–20. 그래도 25보다 작아서 <b>포함</b>. 가장 산성인 건 C2.</li>
<li>(c) <y>O–H(16)</y>를 빼먹기 쉬워. HO–CH₂의 C–H는 α가 아니야(C=O에서 두 칸 떨어짐). 알킨 탄소엔 H가 없어.</li>
<li>(d) 벤젠 고리 H(43), OCH₃ H는 ×. CH₂는 <b>니트릴 α + 벤질 위치</b>라 pKa 25 미만.</li>
<li>(e) 고리의 다른 CH₂는 α가 아니야.</li>
<li>(f) C(CH₃)=CH₂ 쪽은 sp² 탄소라 α-H 없음. CH₃는 <pk>γ 위치</pk>(C=O–C=C–CH₃)라 보통 답에서 빼.</li></ul>
<div class="boxg"><b>원칙</b> “카르보닐/니트릴 바로 옆 sp³ C–H” + “O–H”. 고리 H·바이닐 H·OCH₃는 항상 ×.</div>"""),

# 39 문제 22-38
dict(img="p38", src="연습문제 22-38 · 문제", title="문제 22-38 — 산성도 증가 순서", sub="Problem 22-38 — Rank the compounds in order of increasing acidity",
kw=["산 세기 순서", "pKa 표 22.1", "유발 효과", "1,3-다이케톤"],
sum="여섯 화합물을 산성도가 커지는 순서(약한 산 → 강한 산)로 배열. pKa 값을 떠올리고 큰 것부터 작은 것 순서로 쓰면 돼.",
tr_label="문제 원문 번역", ex_label="접근 방법 · 핵심 개념",
tr="""<p>다음 화합물들을 <b>산성도가 증가하는 순서</b>로 배열하시오.</p>
<ul><li>(a) CH₃CH₂CO₂H (프로판산)</li>
<li>(b) CH₃CH₂OH (에탄올)</li>
<li>(c) (CH₃CH₂)₂NH (다이에틸아민)</li>
<li>(d) CH₃COCH₃ (아세톤)</li>
<li>(e) CH₃COCH₂COCH₃ (2,4-펜탄다이온)</li>
<li>(f) CCl₃CO₂H (트라이클로로아세트산)</li></ul>""",
ex="""<ol><li>각 화합물에서 <y>가장 산성인 H 하나</y>를 정해 (O–H, N–H, α C–H).</li>
<li>표 22.1의 pKa를 붙여.</li>
<li>“증가하는 산성도” = <b>pKa가 큰 것 → 작은 것</b>.</li></ol>
<table class="t"><tr><th>그룹</th><th>pKa 기억</th></tr>
<tr><td>다이알킬아민 N–H</td><td>~36</td></tr>
<tr><td>케톤 α-H</td><td>19</td></tr>
<tr><td>알코올 O–H</td><td>16</td></tr>
<tr><td>1,3-다이케톤 α-H</td><td>9</td></tr>
<tr><td>카르복실산 O–H</td><td>~5</td></tr></table>
<div class="box"><span class="tag">힌트</span>(a)와 (f)는 둘 다 카르복실산이지만, Cl 3개의 <b>유발 효과(전자 끌기)</b>가 카르복실레이트 음이온을 크게 안정화해. 순서 문제에서 이런 “같은 작용기끼리 비교”가 함정이야.</div>"""),

# 40 풀이 22-38
dict(fig=F38, figw=600, src="연습문제 22-38 · 풀이", title="풀이 22-38 — 산성도 증가 순서", sub="Solution 22-38",
kw=["c &lt; d &lt; b &lt; e &lt; a &lt; f", "pKa 36 → 0.7"],
sum="(c) 다이에틸아민 36 &lt; (d) 아세톤 19 &lt; (b) 에탄올 16 &lt; (e) 2,4-펜탄다이온 9 &lt; (a) 프로판산 4.8 &lt; (f) 트라이클로로아세트산 0.7",
tr_label="정답", ex_label="상세 풀이",
tr="""<p class="eq"><b>(c) &lt; (d) &lt; (b) &lt; (e) &lt; (a) &lt; (f)</b></p>
<table class="t"><tr><th>순위</th><th>화합물</th><th>떨어지는 H</th><th>pKa</th></tr>
<tr><td>가장 약함</td><td>(c) (CH₃CH₂)₂NH</td><td>N–H</td><td>~36</td></tr>
<tr><td></td><td>(d) CH₃COCH₃</td><td>α C–H</td><td>19</td></tr>
<tr><td></td><td>(b) CH₃CH₂OH</td><td>O–H</td><td>16</td></tr>
<tr><td></td><td>(e) CH₃COCH₂COCH₃</td><td>α C–H (가운데)</td><td>9</td></tr>
<tr><td></td><td>(a) CH₃CH₂CO₂H</td><td>O–H</td><td>4.8</td></tr>
<tr><td>가장 강함</td><td>(f) CCl₃CO₂H</td><td>O–H</td><td>0.7</td></tr></table>""",
ex="""<p><b>이유를 짝지어 설명하기</b> (서술형 대비)</p>
<ul><li>(c) vs (b): N은 O보다 전기음성도가 작아 음전하를 덜 안정화 → 아민이 훨씬 약한 산.</li>
<li>(d) vs (b): 아세톤 엔올레이트는 공명 안정화되지만, 음전하가 탄소에도 걸쳐 있어 알콕사이드(산소에 집중)보다 덜 유리 → 에탄올(16)이 아세톤(19)보다 <y>약간 더 산성</y>. 여기가 가장 헷갈려!</li>
<li>(e): 음전하가 <b>두 C=O</b>에 퍼짐(슬 17) → 알코올보다도 산성.</li>
<li>(a): 카르복실레이트는 두 <b>산소</b>에 음전하가 같은 비율로 퍼짐 → 다이케톤보다 더 산성.</li>
<li>(f): Cl 3개가 전자를 끌어 카르복실레이트를 더 안정화(<g>유발 효과</g>) → 가장 강한 산.</li></ul>
<div class="box"><span class="tag">시험 포인트</span>알코올(16) &lt; 케톤(19) 순서 뒤집기, 유발 효과 비교가 산 세기 순서 문제의 대표 함정이야.</div>"""),

# 41 문제 22-42
dict(img="p42", src="연습문제 22-42 · 문제", title="문제 22-42 — 생성물 예측 4종", sub="Problem 22-42 — Predict the product(s) of the following reactions",
kw=["탈카르복실화", "1,3-다이온 알킬화", "HVZ", "할로폼(아이오도폼)"],
sum="(a) 1,1-이산 가열 (b) 1,3-다이온 + NaOEt/CH₃I (c) 카르복실산 + Br₂/PBr₃ → H₂O (d) 메틸 케톤 + NaOH/I₂. 22장 반응 4개를 하나씩 쓰는 문제.",
tr_label="문제 원문 번역", ex_label="접근 방법 · 핵심 개념",
tr="""<p>다음 반응들의 생성물을 예측하시오.</p>
<ul><li>(a) 사이클로헥세인-1,1-다이카르복실산 —가열→ ?</li>
<li>(b) 사이클로펜테인-1,3-다이온 —1. Na⁺ ⁻OEt 2. CH₃I→ ?</li>
<li>(c) CH₃CH₂CH₂COOH (뷰탄산) —Br₂, PBr₃→ ? —H₂O→ ?</li>
<li>(d) 아세토페논(PhCOCH₃) —NaOH, H₂O, I₂→ ?</li></ul>""",
ex="""<table class="t"><tr><th></th><th>조건이 말해주는 것</th><th>슬라이드</th></tr>
<tr><td>(a)</td><td>같은 탄소에 COOH 2개 + 가열 = <y>탈카르복실화</y></td><td>27–28</td></tr>
<tr><td>(b)</td><td>두 C=O 사이 CH₂(pKa 9) + NaOEt + CH₃I = <y>알킬화</y></td><td>17, 22, 25</td></tr>
<tr><td>(c)</td><td>Br₂ + PBr₃ = <y>HVZ</y>. 1단계 생성물은 산 브로마이드!</td><td>12–13</td></tr>
<tr><td>(d)</td><td>메틸 케톤 + 과량 염기·할로젠 = <y>할로폼</y></td><td>21</td></tr></table>
<div class="box"><span class="tag">힌트</span>(c)는 물음표가 2개야. H₂O 넣기 <b>전</b> 중간 생성물은 –COOH가 아니라 <b>–COBr</b>. (d)는 생성물이 2개 (탄소 하나 줄어든 것 + 노란 침전).</div>"""),

# 42 풀이 22-42
dict(fig=F42, figw=560, src="연습문제 22-42 · 풀이", title="풀이 22-42 — 생성물 예측", sub="Solution 22-42",
kw=["사이클로헥세인카르복실산", "2-메틸-1,3-다이온", "2-브로모뷰탄산", "벤조산염 + CHI₃"],
sum="(a) 사이클로헥세인카르복실산 + CO₂ (b) 2-메틸사이클로펜테인-1,3-다이온 (c) 2-브로모뷰타노일 브로마이드 → 2-브로모뷰탄산 (d) 벤조산 소듐 + 아이오도폼(CHI₃).",
tr_label="정답", ex_label="상세 풀이 · 메커니즘",
tr="""<ul><li>(a) <b>사이클로헥세인카르복실산</b> + CO₂</li>
<li>(b) <b>2-메틸사이클로펜테인-1,3-다이온</b> (CH₃가 두 C=O 사이 C2에)</li>
<li>(c) 1단계: <b>2-브로모뷰타노일 브로마이드</b> CH₃CH₂CHBrCOBr → 2단계: <b>2-브로모뷰탄산</b> CH₃CH₂CHBrCOOH</li>
<li>(d) <b>벤조산 소듐</b> PhCOO⁻ Na⁺ + <b>CHI₃</b>(아이오도폼, 노란 침전). 산 처리하면 벤조산.</li></ul>""",
ex="""<p><b>(a)</b> 한 COOH의 H가 다른 C=O 산소로 가는 6원 고리 전이상태 → CO₂ 이탈 → 산 엔올 → 토토머화.</p>
<p><b>(b)</b> EtO⁻가 <y>C2-H(pKa 9)</y>를 뗌 → 공명 안정화된 엔올레이트 → C2가 CH₃–I를 S<sub>N</sub>2 공격 → I⁻ 이탈. C4/C5보다 C2가 훨씬 산성이라 C2에만.</p>
<p><b>(c)</b> PBr₃: COOH → COBr → 엔올화 → Br₂ 공격 → α-브로모 산 브로마이드 → H₂O가 C=O에 첨가 → Br⁻ 이탈 (친핵성 아실 치환).</p>
<p><b>(d)</b> CH₃ → CI₃ (3번 할로젠화, 갈수록 빨라짐) → OH⁻가 C=O 첨가 → <g>⁻CI₃ 이탈</g> → PhCOOH + ⁻CI₃ → PhCOO⁻ + CHI₃.</p>
<div class="box"><span class="tag">메커니즘 그리기</span>시험처럼 “시약 + 출발물질만” 주면 (b)(d)가 그리기 좋은 문제야. 특히 (d)의 <b>⁻CX₃ 이탈</b> 화살표는 꼭 연습해 둬.</div>"""),

# 43 문제 22-54
dict(img="p54", src="연습문제 22-54 · 문제", title="문제 22-54 — 빠진 시약 a–c 채우기", sub="Problem 22-54 — Fill in the reagents a–c that are missing",
kw=["β-케토 에스터 알킬화", "가수분해·탈카르복실화", "LDA 직접 알킬화", "위치 선택성"],
sum="고리형 β-케토 에스터 → (a) 메틸화 → (b) CO₂CH₃ 제거 → (c) 반대쪽 α 탄소 메틸화. 세 단계 시약을 쓰는 문제.",
tr_label="문제 원문 번역", ex_label="접근 방법 · 핵심 개념",
tr="""<p>다음 반응 경로에서 빠진 시약 <b>a–c</b>를 채우시오.</p>
<ul><li>메틸 2-옥소사이클로헥세인카르복실레이트 —<b>a</b>→ 메틸 1-메틸-2-옥소사이클로헥세인카르복실레이트 —<b>b</b>→ 2-메틸사이클로헥사논 —<b>c</b>→ 2,6-다이메틸사이클로헥사논</li></ul>""",
ex="""<ol><li><b>a</b>: 무엇이 바뀌었나? C=O와 CO₂CH₃ 사이 탄소에 <y>CH₃가 추가</y> → β-케토 에스터 알킬화 (슬 32).</li>
<li><b>b</b>: <y>CO₂CH₃가 통째로 사라짐</y> → 가수분해 + 탈카르복실화 (슬 27–28).</li>
<li><b>c</b>: 이제 1,3-다이카르보닐이 아니라 그냥 케톤. 반대쪽(C6)에 CH₃ → <y>LDA 직접 알킬화</y> (슬 34–35).</li></ol>
<div class="box"><span class="tag">힌트</span>a의 염기는 에스터가 <b>메틸</b> 에스터라는 걸 보고 골라(슬 25: 에스터와 같은 알콕사이드). c에서 왜 C2가 아니라 C6에 들어가는지도 설명할 수 있어야 해.</div>"""),

# 44 풀이 22-54
dict(fig=F54, figw=630, src="연습문제 22-54 · 풀이", title="풀이 22-54 — 시약 a–c", sub="Solution 22-54",
kw=["a: NaOCH₃ / CH₃I", "b: H₃O⁺, 가열", "c: LDA / CH₃I", "속도론적 엔올레이트"],
sum="a = 1. NaOCH₃ 2. CH₃I · b = H₃O⁺, 가열 · c = 1. LDA, THF 2. CH₃I. 22장 알킬화 세 종류를 한 문제에 모았어.",
tr_label="정답", ex_label="상세 풀이 · 메커니즘",
tr="""<ul><li><b>a</b> = 1. Na⁺ ⁻OCH₃, CH₃OH &nbsp;2. CH₃I</li>
<li><b>b</b> = H₃O⁺, 가열</li>
<li><b>c</b> = 1. LDA, THF &nbsp;2. CH₃I</li></ul>
<p class="note">a는 NaOEt를 써도 생성물 뼈대는 같지만, 메틸 에스터와 에스터 교환이 섞일 수 있어 NaOCH₃가 깔끔해.</p>""",
ex="""<p><b>a</b>: CH₃O⁻가 두 C=O 사이 C–H(pKa ~11)를 뗌 → 엔올레이트 → CH₃I에 S<sub>N</sub>2 → 4차 탄소(CH₃ + CO₂CH₃).</p>
<p><b>b</b>: 에스터 산 가수분해 → β-케토산 → <g>6원 고리 전이상태로 CO₂ 이탈</g> → 엔올 → 토토머화 → 2-메틸사이클로헥사논.</p>
<p><b>c</b>: 2-메틸사이클로헥사논엔 α 탄소가 두 개(C2: H 1개, 붐빔 / C6: H 2개). 부피 큰 LDA가 저온에서 <y>덜 붐비는 C6-H</y>를 빨리 뗌(속도론적 엔올레이트, 슬 35) → CH₃I → <b>2,6-다이메틸</b>.</p>
<div class="boxg"><b>왜 b 다음에 c?</b> a 단계에서 CO₂CH₃가 C2 위치를 지정했고, b에서 그걸 없앤 뒤 c에서 LDA로 반대편을 골라 알킬화. “활성화기로 위치 지정 → 제거 → 직접 알킬화” 전략이야.</div>
<div class="box"><span class="tag">반응 사다리</span>순서를 바꿔서 c를 a 전에 하면? CO₂CH₃ 옆 C–H(pKa 11)가 먼저 떨어져서 원하는 위치에 안 들어가. 순서 배열 문제로 나오기 좋아.</div>"""),
]
