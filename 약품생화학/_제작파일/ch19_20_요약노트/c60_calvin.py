from parts import *
P = P6
E = [
dict(t="c", id="c-calvin", part=P, title="캘빈 회로 큰 그림 — CO₂ 3개를 넣으면 G3P 1개가 나온다", sub="20.1 Photosynthetic carbohydrate synthesis · Calvin cycle 3 stages · Slides 117–121",
core="캘빈 회로 = ① <b>고정</b>(CO<sub>2</sub> + RuBP → 3-PG, 루비스코) ② <b>환원</b>(3-PG → G3P, ATP·NADPH 사용) ③ <b>재생</b>(G3P 5개 → RuBP 3개, ATP 사용). CO<sub>2</sub> 3개마다 <b>G3P 1개</b>가 밖으로 나간다.",
detail="""<p><b>Calvin cycle (캘빈 회로)</b> = 환원적 펜토스 인산 경로, 탄소 고정 반응. <b>스트로마</b>에서, 명반응의 <b>ATP와 NADPH</b>를 받아 돌아간다.</p>
<table class="t"><tr><th>단계</th><th>무엇이</th><th>CO<sub>2</sub> 3개 기준</th></tr>
<tr><td>① Fixation 고정</td><td>3 RuBP(C<sub>5</sub>) + 3 CO<sub>2</sub> → 6 3-PG(C<sub>3</sub>) — <b>루비스코</b></td><td>탄소 15 + 3 = 18</td></tr>
<tr><td>② Reduction 환원</td><td>6 3-PG → 6 G3P</td><td><b>ATP 6 + NADPH 6</b></td></tr>
<tr><td>③ Regeneration 재생</td><td>5 G3P(5×3 = 15 C) → 3 RuBP(3×5 = 15 C)</td><td><b>ATP 3</b></td></tr>
<tr><td>산물</td><td colspan="2"><b>1 G3P</b> → 세포질로(수크로스) 또는 녹말·해당과정</td></tr></table>
<p>→ G3P 1개 = <g>ATP 9 + NADPH 6</g>, 포도당 1개(G3P 2개) = <g>ATP 18 + NADPH 12</g>.</p>
<p><b>“1 P<sub>i</sub> is needed”</b>(슬라이드 120): ATP 9개가 ADP 9개가 되지만 풀려나는 P<sub>i</sub>는 8개 → 1개는 G3P에 붙어 밖으로 나감 → 그만큼 P<sub>i</sub>를 세포질에서 들여와야 함 ({REF:c-antiport}).</p>
<div class="term">＊[용어: RuBP(Ribulose 1,5-BisPhosphate, 리불로스 1,5-이인산) = 탄소 5개 당에 인산 2개. CO<sub>2</sub>를 받아 주는 ‘수용체’]</div>
<div class="term">＊[용어: 3-PG(3-PhosphoGlycerate, 3-인산글리세르산) = 탄소 3개, 고정 직후 첫 안정 산물 → 그래서 ‘C<sub>3</sub> 식물’]</div>""",
formula="""<span class="fx">3CO<sub>2</sub> + 9ATP + 6NADPH + 5H<sub>2</sub>O → G3P + 9ADP + 8P<sub>i</sub> + 6NADP<sup>+</sup></span><br>
비율 <b>ATP : NADPH = 3 : 2</b> (비순환 흐름만으로는 ATP가 살짝 부족 → 순환 흐름이 보충)""",
side=[("img", 121, "원본 슬라이드 121 — 3RuBP + 3CO₂ → 6 3PG → 6 G3P → 1 G3P 산물 + 5 G3P → 3RuBP", 230),
      ("ana", "<b>회전 초밥 레일</b>: 빈 접시(RuBP) 3개가 돌다가 CO<sub>2</sub> 3개를 얹고(고정), 주방에서 양념(ATP·NADPH)을 쳐 G3P 6개 완성(환원). 손님이 1개 가져가고, 나머지 5개는 다시 빈 접시 3개로 재조립(재생)."),
      ("tip", "숫자 공식: <b>3 · 6 · 6 · 1 · 5 · 3</b> (CO<sub>2</sub> 3, 3PG 6, G3P 6, 산물 1, 재생 5, RuBP 3) + <b>ATP 9, NADPH 6</b>.")],
one="CO₂ 3 + RuBP 3 → 3PG 6 → G3P 6 → 1개 출하 + 5개 → RuBP 3. G3P 1개 = ATP 9 + NADPH 6."),

dict(t="c", id="c-rubisco", part=P, title="루비스코 — 지구에서 가장 많고 가장 느린 효소, Mg²⁺와 카바모일-Lys로 켜진다", sub="Ribulose 1,5-bisphosphate carboxylase/oxygenase · Rubisco activase · Slides 122–125",
core="<b>Rubisco</b>는 RuBP에 CO<sub>2</sub>를 붙여 3-PG 2개를 만든다. 활성화하려면 <b>rubisco activase</b>(ATP 사용)가 막고 있던 RuBP를 치우고, <b>Lys<sup>201</sup></b>이 CO<sub>2</sub>로 <b>카바모일화</b>된 뒤 <b>Mg<sup>2+</sup></b>가 붙어야 한다.",
detail="""<ul><li><b>Rubisco (루비스코)</b> = Ribulose 1,5-bisphosphate carboxylase/oxygenase. 엽록체 단백질의 절반, 지구에서 가장 흔한 단백질. 촉매 속도는 매우 느림(초당 ~3회).</li>
<li><b>Form I</b>(식물·조류·남세균): 큰 소단위체 8 + 작은 소단위체 8 (L<sub>8</sub>S<sub>8</sub>, 약 550 kDa) / <b>Form II</b>(일부 광합성 세균, Rhodospirillum rubrum): 큰 소단위체 2개(L<sub>2</sub>)만.</li></ul>
<p><b>활성화 3단계</b> (슬라이드 123–124)</p>
<ol><li>비활성: RuBP가 <b>변형 안 된 Lys<sup>201</sup></b> 자리에 꽉 붙어 있음</li>
<li><b>Rubisco activase (루비스코 활성화효소)</b>가 <b>ATP</b>를 써서 그 RuBP를 떼어냄 → Lys<sup>201</sup>의 ε-아미노기 노출</li>
<li>CO<sub>2</sub>(기질이 아닌 ‘활성화용’ CO<sub>2</sub>)가 ε-NH<sub>2</sub>에 붙어 <b>카바모일-Lys(–NH–COO<sup>−</sup>)</b> → <b>Mg<sup>2+</sup></b>가 결합 → <b>활성</b>. 활성 부위에서 Mg<sup>2+</sup>는 카바모일-Lys, Asp<sup>203</sup>, Glu<sup>204</sup>, 기질과 배위.</li></ol>
<p><b>반응 메커니즘</b> (슬라이드 125): ① RuBP → <b>엔다이올레이트</b>(enediolate) ② Mg<sup>2+</sup> 옆에서 분극된 CO<sub>2</sub>를 엔다이올레이트가 공격 → 가지 달린 <b>6탄소 β-케토산 중간체</b> ③ C-3 카보닐에 물 첨가(수화) ④ 절단 → 3-PG 1개 ⑤ 카바니온에 양성자 → 두 번째 3-PG.</p>
<div class="term">＊[용어: 카바모일화(carbamoylation) = 아미노기(–NH<sub>2</sub>)에 CO<sub>2</sub>가 붙어 –NH–COO<sup>−</sup>가 되는 것. 음전하가 생겨 Mg<sup>2+</sup>를 붙잡는 ‘손’이 됨]</div>""",
side=[("img", 123, "원본 슬라이드 123 — activase(ATP)가 RuBP 제거 → Lys²⁰¹ 카바모일화 → Mg²⁺ 결합 → 활성", 175),
      ("ana", "루비스코 = <b>자물쇠 3개 달린 공장 문</b>: ① 문 앞을 막은 짐(RuBP)을 지게차(activase, ATP)로 치우고 ② 손잡이(Lys)에 고리(CO<sub>2</sub>)를 달고 ③ 열쇠(Mg<sup>2+</sup>)를 꽂아야 열린다."),
      ("trap", "카바모일화에 쓰이는 CO<sub>2</sub>는 <b>기질 CO<sub>2</sub>가 아니다</b>. activase는 <b>ATP</b>를 쓴다(GTP 아님).")],
one="Rubisco 켜기 = activase(ATP)로 RuBP 치우기 → Lys²⁰¹ + CO₂(카바모일) → Mg²⁺. 반응 = 엔다이올레이트 + CO₂ → 6C → 3PG 2개."),

dict(t="c", id="c-antiport", part=P, title="환원 단계와 Pᵢ–삼탄당 인산 역수송체 — 설탕 원료를 내보내고 인산을 들인다", sub="Second stage (3-PG → G3P) · Pᵢ–triose phosphate antiporter · Slides 126–128",
core="3-PG는 ATP·NADPH로 <b>G3P</b>가 되고, 삼탄당 인산(DHAP)은 <b>P<sub>i</sub>–삼탄당 인산 역수송체</b>로 세포질에 나가 수크로스가 된다. 대신 P<sub>i</sub> 1개가 엽록체로 들어와 인산이 바닥나지 않게 한다.",
detail="""<p><b>환원 단계</b> (스트로마):</p>
<ol><li>3-PG + ATP → <b>1,3-BPG</b>(1,3-bisphosphoglycerate) + ADP — 3-phosphoglycerate kinase(인산글리세르산 키나아제)</li>
<li>1,3-BPG + <b>NADPH</b> + H<sup>+</sup> → <b>G3P</b> + NADP<sup>+</sup> + P<sub>i</sub> — 엽록체 G3P 탈수소효소(<b>NADPH</b> 특이적; 해당과정의 것은 NAD<sup>+</sup>)</li>
<li>G3P ⇌ <b>DHAP</b> — triose phosphate isomerase(삼탄당 인산 이성질화효소)</li></ol>
<p>→ 스트로마에선 녹말 합성, 세포질로 나가면 수크로스 합성·해당과정.</p>
<p><b>P<sub>i</sub>–triose phosphate antiporter (P<sub>i</sub>–삼탄당 인산 역수송체)</b> — 엽록체 <b>내막</b></p>
<ul><li>삼탄당 인산(DHAP) <b>1개 나감</b> ⇄ P<sub>i</sub> <b>1개 들어옴</b> (1:1 교환) → “Product move to cytosol, P<sub>i</sub> move to stroma”</li>
<li>왜? 캘빈 회로가 G3P를 내보낼 때마다 인산 1개가 같이 빠져나감 → 세포질에서 수크로스 만들며 풀려난 P<sub>i</sub>를 돌려받아야 회로가 계속 돎.</li>
<li><b>ATP·환원력(NAD(P)H)의 간접 수출</b>(슬라이드 128): 엽록체 내막은 ATP·NADPH를 통과시키지 않음 → DHAP로 내보낸 뒤 세포질에서 DHAP → G3P → (G3P 탈수소효소) <b>NADH</b> 생성 → 1,3-BPG → (PGK) <b>ATP</b> 생성 → 3-PG는 다시 역수송체로 엽록체에 돌아옴.</li></ul>
<div class="term">＊[용어: 역수송체(antiporter) = 두 물질을 서로 반대 방향으로 맞바꾸는 회전문]</div>""",
side=[("img", 127, "원본 슬라이드 127 — DHAP는 세포질로(수크로스), Pᵢ는 스트로마로", 165),
      ("img", 128, "원본 슬라이드 128 — 역수송체로 ATP와 환원력을 간접적으로 세포질에 수출", 165),
      ("ana", "<b>빈 병 보증금 제도</b>: 엽록체가 설탕 원료(DHAP)를 한 병 내보낼 때마다 세포질은 빈 병(P<sub>i</sub>)을 하나 돌려준다. 빈 병이 안 돌아오면 공장(캘빈 회로)은 병(인산)이 없어 멈춘다.")],
one="3PG → (ATP) → 1,3-BPG → (NADPH) → G3P ⇌ DHAP. DHAP 나가고 Pᵢ 들어오는 1:1 역수송체 = 인산 보증금 + ATP·NADH 간접 수출."),

dict(t="c", id="c-regen", part=P, title="재생 단계 — 탄소 블록 맞추기로 G3P 5개를 RuBP 3개로", sub="Third stage: G3P → RuBP · Transketolase (TPP) · Slides 129–131",
core="G3P 5개(C<sub>3</sub>×5 = 15 C)를 알돌레이스·포스파테이스·<b>트랜스케톨레이스</b>로 섞고 쪼개 오탄당 3개(C<sub>5</sub>×3 = 15 C)로 바꾼 뒤, <b>ribulose 5-phosphate kinase</b>가 ATP로 인산을 붙여 RuBP를 되살린다.",
detail="""<table class="t"><tr><th>#</th><th>효소</th><th>반응 (탄소 수)</th></tr>
<tr><td>①</td><td>Aldolase 알돌레이스</td><td>G3P + DHAP → FBP (3+3=6)</td></tr>
<tr><td>②</td><td>FBPase-1 (과당 1,6-이인산 가수분해효소)</td><td>FBP → F6P + P<sub>i</sub></td></tr>
<tr><td>③</td><td><b>Transketolase</b> 트랜스케톨레이스</td><td>F6P + G3P → E4P + Xu5P (<b>6+3 = 4+5</b>)</td></tr>
<tr><td>④</td><td>Aldolase</td><td>E4P + DHAP → SBP (4+3=7)</td></tr>
<tr><td>⑤</td><td>SBPase (세도헵툴로스 1,7-이인산 가수분해효소)</td><td>SBP → S7P + P<sub>i</sub></td></tr>
<tr><td>⑥</td><td><b>Transketolase</b></td><td>S7P + G3P → R5P + Xu5P (<b>7+3 = 5+5</b>)</td></tr>
<tr><td>⑦</td><td>Ribose 5-P isomerase 이성질화효소</td><td>R5P → Ru5P</td></tr>
<tr><td>⑧</td><td>Ribulose 5-P epimerase 에피머화효소</td><td>Xu5P → Ru5P</td></tr>
<tr><td>⑨</td><td><b>Ribulose 5-P kinase</b></td><td>Ru5P + <b>ATP</b> → RuBP (×3 = ATP 3개)</td></tr></table>
<p><b>Transketolase (트랜스케톨레이스)</b>: 케톤당(주개)의 <b>C-1·C-2 두 탄소 조각</b>을 알도스(받개)에 옮김. 보조인자 <b>TPP</b>(Thiamine PyroPhosphate, 티아민 피로인산 = 비타민 B<sub>1</sub>)의 티아졸륨 고리가 <b>카바니온</b>을 만들어 2탄소 조각을 잠시 들고 있음(공명 안정화).</p>
<div class="term">＊[용어: E4P = 에리트로스 4-인산(4C), Xu5P = 자일룰로스 5-인산, R5P = 리보스 5-인산, Ru5P = 리불로스 5-인산(5C), S7P = 세도헵툴로스 7-인산(7C)]</div>""",
side=[("img", 130, "원본 슬라이드 130 — 트랜스케톨레이스: 6+3 = 4+5, 7+3 = 5+5", 185),
      ("img", 131, "원본 슬라이드 131 — TPP가 2탄소 조각을 카바니온으로 운반", 140),
      ("ana", "<b>레고 블록 재조립</b>: 3칸짜리 블록 5개를 6칸·4칸·7칸으로 붙였다 뗐다(알돌레이스, 트랜스케톨레이스) 하면서 결국 5칸짜리 3개로. 트랜스케톨레이스는 늘 <b>2칸짜리 조각</b>만 옮기는 손.")],
one="5 G3P(15C) → 6+3=4+5, 7+3=5+5 (트랜스케톨레이스·TPP) → 3 Ru5P → +ATP 3 → 3 RuBP."),

dict(t="c", id="c-biomass", part=P, title="고정된 탄소의 행방 — 수크로스 · 녹말 · 셀룰로스, 그리고 색소체", sub="Assimilation of CO₂ into biomass · Plastids · Slides 132–133",
core="삼탄당 인산 → 육탄당 인산 → <b>수크로스(운반용)</b>, <b>녹말(저장용)</b>, <b>셀룰로스(세포벽)</b>. 오탄당 인산·대사 중간체는 DNA·RNA·단백질·지질의 재료가 된다.",
detail="""<ul><li>빛 의존 반응(ATP, NADPH) + CO<sub>2</sub>, H<sub>2</sub>O → <b>삼탄당 인산(triose phosphates)</b> → <b>육탄당 인산(hexose phosphates)</b> / <b>오탄당 인산(pentose phosphates)</b></li>
<li>육탄당 인산 → <b>Sucrose (수크로스, 설탕)</b> = 식물 몸속 <b>수송</b> 형태 (세포질에서 합성) / <b>Starch (녹말)</b> = <b>저장</b> 형태 (엽록체·아밀로플라스트에서) / <b>Cellulose (셀룰로스)</b> = <b>세포벽</b> 재료</li>
<li>대사 중간체 → <b>DNA, RNA, 단백질, 지질</b></li>
<li><b>Plastids (색소체)</b>: 식물·조류에만 있는 소기관 무리. <b>Proplastid (원색소체)</b>에서 출발해 → <b>chloroplast (엽록체)</b>, <b>amyloplast (아밀로플라스트, 녹말 다량 저장, 예: 감자)</b>, etioplast 등으로 서로 바뀜.</li></ul>
<div class="term">＊[용어: 바이오매스(biomass) = 생물이 만들어 낸 유기물의 총량. 결국 모두 CO<sub>2</sub> 고정에서 출발]</div>""",
side=[("img", 132, "원본 슬라이드 132 — 삼탄당·육탄당·오탄당 인산 → 수크로스·녹말·셀룰로스·DNA·RNA·단백질·지질", 170),
      ("img", 133, "원본 슬라이드 133 — 색소체: 원색소체 ↔ 엽록체 ↔ 아밀로플라스트", 150),
      ("ana", "식물의 탄소 = <b>현금(수크로스, 이동용)</b>, <b>적금(녹말, 저장용)</b>, <b>건물(셀룰로스, 구조용)</b>.")],
one="수크로스 = 운반, 녹말 = 저장(아밀로플라스트), 셀룰로스 = 세포벽. 모두 캘빈 회로의 G3P에서."),

# ───────────────────────────── 문제
dict(t="q", id="q-calvin-count", part=P, kind=["chk", "bl"], title="캘빈 회로 숫자 장부 채우기", src="개념확인 · 빈칸 · 슬라이드 120–121",
q="""CO<sub>2</sub> 3분자가 고정될 때:<br>
3 RuBP + 3 CO<sub>2</sub> → <span class="blank">(가)</span> 3-PG (효소: <span class="blank">(나)</span>)<br>
6 3-PG → 6 G3P에 ATP <span class="blank">(다)</span>개와 NADPH 6개 사용<br>
G3P <span class="blank">(라)</span>개는 RuBP 3개로 재생(ATP 3개), 나머지 1개가 산물<br>
→ 포도당 1분자를 만들려면 ATP <span class="blank">(마)</span>개, NADPH 12개가 필요.""",
a="(가) 6 (나) 루비스코(rubisco) (다) 6 (라) 5 (마) 18",
steps=[("고정: RuBP(5C) 1개 + CO<sub>2</sub> 1개 → 6C → 3-PG(3C) <b>2개</b> → ×3 = <b>6</b>", ""),
       ("환원: 3-PG 1개당 ATP 1(인산화) + NADPH 1(환원) → ×6 = ATP <b>6</b>, NADPH 6", ""),
       ("재생: 15 C → 15 C, G3P <b>5</b>개 → Ru5P 3개 → ATP 3개로 RuBP 3개", ""),
       ("포도당 = G3P 2개 = 2 × (ATP 9, NADPH 6) = ATP <b>18</b>, NADPH 12", "CO₂ 6개 고정.")],
one="3 · 6 · 6 · 1 · 5 · 3, G3P 하나 = ATP 9 + NADPH 6, 포도당 = 18 + 12."),

dict(t="q", id="q-transk", part=P, kind=["chk", "bl"], title="트랜스케톨레이스 블록 맞추기", src="개념확인 · 빈칸 · 슬라이드 130–131",
q="""트랜스케톨레이스는 케톤당 주개의 <span class="blank">(가)</span>탄소 조각을 알도스 받개에 옮긴다. 보조인자는 <span class="blank">(나)</span>(비타민 B<sub>1</sub> 유래)이다.<br>
반응 1: 과당 6-인산 + G3P → <span class="blank">(다)</span>(4C) + 자일룰로스 5-인산 &nbsp;(6 + 3 = 4 + 5)<br>
반응 2: 세도헵툴로스 7-인산 + G3P → <span class="blank">(라)</span>(5C) + 자일룰로스 5-인산 &nbsp;(7 + 3 = 5 + 5)<br>
마지막으로 리불로스 5-인산은 <span class="blank">(마)</span>에 의해 ATP로 인산화되어 RuBP가 된다.""",
a="(가) 2 (나) TPP(티아민 피로인산) (다) 에리트로스 4-인산 (라) 리보스 5-인산 (마) 리불로스 5-인산 키나아제",
steps=[("2탄소 조각(C-1, C-2)이 TPP의 카바니온에 잠시 붙어 이동", ""),
       ("F6P(6) − 2 = <b>E4P</b>(4), G3P(3) + 2 = Xu5P(5)", "탄소 수 보존: 6 + 3 = 4 + 5."),
       ("S7P(7) − 2 = <b>R5P</b>(5), G3P(3) + 2 = Xu5P(5)", "7 + 3 = 5 + 5."),
       ("R5P → Ru5P(이성질화), Xu5P → Ru5P(에피머화) → <b>Ru5P 키나아제</b> + ATP → RuBP", "")],
one="트랜스케톨레이스 = TPP로 2탄소 배달: 6+3=4+5, 7+3=5+5."),

dict(t="q", id="q-calvin-multi", part=P, kind=["chk", "multi"], title="캘빈 회로 — 옳은 것 모두", src="개념확인 · 다답형",
q="캘빈 회로에 대한 설명으로 <b>옳은 것을 모두</b> 고르시오." + opts(
"캘빈 회로는 엽록체 스트로마에서 일어난다.",
"CO<sub>2</sub> 고정의 첫 안정 산물은 탄소 3개짜리 3-인산글리세르산이다.",
"엽록체의 G3P 탈수소효소는 NAD<sup>+</sup>를 사용해 G3P를 산화한다.",
"G3P 1분자 생산에 ATP 9개와 NADPH 6개가 소비된다.",
"Ribulose 5-phosphate kinase는 재생 단계에서 ATP를 사용한다."),
a="①, ②, ④, ⑤",
opx=ox(("①", True, "명반응 = 틸라코이드 막, 캘빈 = 스트로마."), ("②", True, "그래서 ‘C<sub>3</sub> 경로’."),
       ("③", False, "엽록체 효소는 <b>NADPH</b>로 1,3-BPG를 G3P로 <b>환원</b>."), ("④", True, "6 + 3 = 9 ATP, 6 NADPH."), ("⑤", True, "Ru5P + ATP → RuBP.")),
one="스트로마 · 3PG · NADPH로 환원 · ATP 9/NADPH 6 · Ru5P 키나아제(ATP)."),
]
