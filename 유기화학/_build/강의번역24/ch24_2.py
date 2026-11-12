# -*- coding: utf-8 -*-
# 제24장 슬라이드 21–40: 호프만·커티어스 자리옮김, 아민 아실화, 호프만 제거, 아릴아민 EAS, 다이아조늄염(산드마이어)
PAGES = [
# 21
dict(img=21, slide=21, title="호프만·커티어스 자리옮김 — 탄소 1개를 잃고 1차 아민", sub="Hofmann and Curtius Rearrangements",
kw=["호프만 자리옮김 (NaOH, Br₂)", "커티어스 자리옮김 (아실 아자이드, 가열)", "−CO₂", "탄소 1개 감소"],
sum="카복실산 유도체는 호프만 자리옮김(아마이드 + NaOH, Br₂)이나 커티어스 자리옮김(아실 아자이드 + 가열)으로 탄소 1개를 잃고 1차 아민이 된다.",
tr="""<ul><li>카복실산 유도체는 <b>호프만 자리옮김</b>과 <b>커티어스 자리옮김</b> 둘 다로 <b>탄소 원자 1개를 잃으며</b> 1차 아민으로 바뀔 수 있다.</li></ul>
<p class="note">그림: 호프만 — R–CO–NH₂(아마이드) —NaOH, Br₂, H₂O→ R–NH₂ + CO₂ · 커티어스 — R–CO–N=N⁺=N⁻(아실 아자이드) —H₂O, 가열→ R–NH₂ + CO₂ + N₂</p>""",
ex="""<p>공통점: R이 C=O 탄소에서 <b>옆 질소로 옮겨 가고</b>(자리옮김) → 아이소사이아네이트(R–N=C=O) → 물이 붙어 카밤산 → <y>CO₂가 빠져</y> R–NH₂.</p>
<table class="t"><tr><th></th><th>호프만</th><th>커티어스</th></tr>
<tr><td>출발</td><td>1차 아마이드 RCONH₂</td><td>아실 아자이드 RCON₃ (산 염화물 + NaN₃)</td></tr>
<tr><td>조건</td><td>NaOH, Br₂, H₂O</td><td>가열 (+ H₂O)</td></tr>
<tr><td>이탈기</td><td>Br⁻</td><td>N₂</td></tr></table>
<div class="box"><span class="tag">시험 포인트</span>생성 아민은 출발물보다 <b>탄소가 1개 적다</b>. R의 입체 배치는 그대로 유지.</div>"""),

# 22
dict(img=22, slide=22, title="그림 24.5 — 호프만 자리옮김 메커니즘 ①②③", sub="Figure 24.5 - Mechanism (1)",
kw=["① N–H 탈양성자화", "② Br₂와 α-치환 → N-브로모아마이드", "③ 두 번째 N–H 제거"],
sum="① 염기가 산성 N–H를 떼어 아마이드 음이온 ② 음이온이 Br₂와 반응해 N-브로모아마이드 ③ 남은 N–H를 염기가 떼어 공명 안정화된 브로모아마이드 음이온.",
tr="""<ol><li>염기가 산성인 N–H 양성자를 떼어 <b>아마이드 음이온</b>을 만든다.</li>
<li>음이온이 브로민과 <b>α-치환 반응</b>을 해 <b>N-브로모아마이드</b>가 된다.</li>
<li>남은 N–H 양성자를 염기가 떼어 공명 안정화된 <b>브로모아마이드 음이온</b>이 된다…</li></ol>""",
ex="""<p>아마이드 N–H는 C=O 옆이라 약산(pKa ≈ 17) → OH⁻가 뗄 수 있어. 생긴 N⁻는 22장 엔올레이트처럼 Br₂를 공격 (그래서 ‘α-치환’이라 부름 — 이번엔 탄소가 아니라 질소).</p>
<p>Br이 붙으면 남은 N–H가 더 산성 → 다시 탈양성자화 → R–C(=O)–N⁻–Br.</p>"""),

# 23
dict(img=23, slide=23, title="그림 24.5 — 호프만 자리옮김 메커니즘 ④⑤⑥", sub="Figure 24.5 - Mechanism (2)",
kw=["④ R 이동 + Br⁻ 이탈", "아이소사이아네이트", "⑤ 물 첨가 → 카밤산", "⑥ −CO₂ → 아민"],
sum="④ C=O에 붙은 R이 질소로 옮겨 가는 동시에 Br⁻가 떠나 아이소사이아네이트 ⑤ 물이 친핵성 첨가해 카밤산 ⑥ 카밤산이 저절로 CO₂를 잃고 아민.",
tr="""<ol start="4"><li>… 이것이 <b>자리옮김</b>한다: 카르보닐 탄소에 붙은 R기가 <b>질소로 이동</b>하는 동시에 브로민화 이온이 떠난다.</li>
<li>자리옮김으로 생긴 <b>아이소사이아네이트</b>에 물이 친핵성 첨가해 <b>카밤산</b>이 된다.</li>
<li>카밤산은 <b>저절로 CO₂를 잃고</b> 아민이 된다.</li></ol>""",
ex="""<p><b>④ 핵심 단계</b>: N⁻ 전자쌍이 C=N을 만들려 하면서 R–C 결합 전자쌍이 R을 데리고 N으로 이동, 동시에 N–Br 결합이 끊겨 Br⁻ 이탈 → R–N=C=O.</p>
<p><b>⑤⑥</b>: H₂O가 N=C=O의 가운데 탄소 공격 → R–NH–COOH(카밤산) → 불안정해서 CO₂ 방출 → R–NH₂.</p>
<div class="box"><span class="tag">외우기</span>아마이드 → (Br₂/OH⁻) → N-브로모 → <b>R 이동</b> → 아이소사이아네이트 → 카밤산 → <b>−CO₂</b> → 아민.</div>"""),

# 24
dict(img=24, slide=24, title="커티어스 자리옮김 — 아실 아자이드 가열", sub="Curtius Rearrangement",
kw=["산 염화물 + NaN₃", "아실 아자이드", "−N₂", "아이소사이아네이트", "H₂O → 아민 + CO₂"],
sum="산 염화물에서 만든 아실 아자이드를 가열하면 R이 C=O에서 옆 질소로 옮겨 가며 N₂가 떨어져 아이소사이아네이트가 되고, 물을 넣으면 아민 + CO₂.",
tr="""<ul><li><b>산 염화물</b>로부터 만든 <b>아실 아자이드</b>를 가열한다.</li>
<li>–R이 C=O에서 <b>이웃한 질소로 이동</b>하고, 동시에 <b>이탈기가 떨어진다</b>.</li></ul>
<p class="note">그림: RCOCl —NaN₃→ [R–CO–N⁻–N⁺≡N (아실 아자이드) → R–N=C=O (아이소사이아네이트) + N₂] —H₂O→ R–NH₂ + CO₂</p>""",
ex="""<p>호프만의 ④와 같은 이동인데, 이탈기가 Br⁻ 대신 <y>N₂(기체, 최고의 이탈기)</y> → 가열만으로 진행.</p>
<p>산 염화물 + NaN₃는 21장 친핵성 아실 치환 (Cl⁻ 이탈).</p>
<div class="box"><span class="tag">비교</span>아자이드 합성(슬 15, R–X + N₃⁻ → 환원) = 탄소 수 유지 / 커티어스 (RCOCl + N₃⁻ → 가열) = 탄소 1개 감소.</div>"""),

# 25
dict(img=25, slide=25, title="예제 — p-톨루이딘을 p-톨루산에서 (호프만·커티어스)", sub="Worked Example — Solution",
kw=["p-메틸벤조산", "SOCl₂", "NH₃ → 아마이드 → 호프만", "NaN₃ → 커티어스"],
sum="풀이: 전구체는 산 염화물이고, NaN₃ 다음 H₂O와 가열(커티어스)로 처리한다. 또는 산 염화물 → NH₃ → 아마이드 → Br₂, NaOH, H₂O(호프만).",
tr="""<ul><li>풀이:
<ul><li>전구체는 <b>산 염화물</b>이며, <b>NaN₃</b>로 처리한 뒤 <b>H₂O와 가열</b>한다.</li></ul></li></ul>
<p class="note">그림: H₃C–C₆H₄–CO₂H —SOCl₂→ H₃C–C₆H₄–COCl → ① NH₃ → H₃C–C₆H₄–CONH₂ —Br₂, NaOH, H₂O→ H₃C–C₆H₄–NH₂ / ② NaN₃ → H₃C–C₆H₄–CON₃ —H₂O, 가열→ H₃C–C₆H₄–NH₂</p>""",
ex="""<p>목표 p-톨루이딘(p-메틸아닐린)은 고리에 <b>N이 바로</b> 붙음 → 출발물 p-톨루산의 –COOH 탄소가 사라져야 → <y>탄소 1개를 잃는 자리옮김</y>.</p>
<p>두 경로 모두 공통 중간체 = 산 염화물 (SOCl₂).</p>
<div class="box"><span class="tag">역합성 신호</span>“Ar–COOH → Ar–NH₂” 또는 “R–COOH → R–NH₂ (탄소 하나 적음)” = 호프만/커티어스.</div>"""),

# 26
dict(img=26, slide=26, title="아민의 반응 ① — 아실화 (산 염화물 → 아마이드)", sub="Reactions of Amines — acylation",
kw=["친핵성 아실 치환", "NH₃ / RNH₂ / R₂NH", "피리딘 (HCl 제거)", "3차 아민은 ✗"],
sum="NH₃, 1차·2차 아민은 산 염화물과 친핵성 아실 치환을 해 1차·2차·3차 아마이드를 만든다. 피리딘이 생긴 HCl을 잡는다.",
tr="""<ul><li>1차·2차 아민도 <b>친핵성 아실 치환 반응</b>으로 <b>아실화</b>될 수 있다.</li></ul>
<p class="note">그림: RCOCl + NH₃ → RCONH₂ + HCl · RCOCl + R′NH₂ → RCONHR′ + HCl · RCOCl + R′₂NH → RCONR′₂ + HCl (각각 피리딘 용매)</p>""",
ex="""<p>21장 그대로: N 전자쌍 → C=O 공격 → 사면체 → Cl⁻ 이탈 → H⁺ 제거.</p>
<p>3차 아민(R₃N)은 N에 H가 없어 중성 아마이드를 못 만듦 → 아실화 ✗ (피리딘·Et₃N을 ‘HCl 받개’ 염기로 쓰는 이유).</p>
<div class="box"><span class="tag">중요</span>아실화된 N은 전자쌍이 C=O로 퍼져 <b>염기성·친핵성이 사라짐</b>(슬 7) → 한 번만 반응하고 멈춤, 아닐린 보호(슬 31–33)에 이용.</div>"""),

# 27
dict(img=27, slide=27, title="호프만 제거 ① — 아민 → 알켄 (CH₃I 과량 → 4차 암모늄)", sub="Hofmann Elimination",
kw=["–NH₂ 나쁜 이탈기", "알킬암모늄 이온", "CH₃I 과량 (완전 메틸화)", "4차 암모늄염", "Ag₂O, H₂O, 가열"],
sum="호프만 제거는 아민을 알켄으로 바꾼다. –NH₂⁻는 아주 나쁜 이탈기라 CH₃I 과량으로 완전히 메틸화해 4차 암모늄(좋은 이탈기)으로 만든 뒤 Ag₂O·가열로 제거.",
tr="""<ul><li>아민을 <b>알켄</b>으로 바꾼다.</li>
<li>NH₂⁻는 <b>아주 나쁜 이탈기</b>라서 좋은 이탈기인 <b>알킬암모늄 이온</b>으로 바꾼다.</li>
<li>아민을 <b>과량의 아이오도메테인</b>과 반응시켜 완전히 메틸화하면 해당 <b>4차 암모늄염</b>이 된다.</li></ul>
<p class="note">그림: 1-메틸펜틸아민 —CH₃I 과량→ (1-메틸펜틸)트라이메틸암모늄 아이오다이드 —Ag₂O, H₂O, 가열→ 1-헥센(60 %) + N(CH₃)₃</p>""",
ex="""<p>알코올 –OH를 –OH₂⁺로 바꿔 떼는 것과 같은 발상: –NH₂ → <y>–N⁺(CH₃)₃</y> (중성 N(CH₃)₃로 떨어짐 = 좋은 이탈기).</p>
<p>슬 14의 ‘과알킬화’를 일부러 끝까지 → 4차 암모늄.</p>
<div class="box"><span class="tag">결과 주목</span>2-헥센이 아니라 <b>1-헥센</b>(덜 치환된 알켄)이 주생성물 → 호프만 규칙 (슬 29).</div>"""),

# 28
dict(img=28, slide=28, title="호프만 제거 ② — Ag₂O가 OH⁻를 공급, E2", sub="Hofmann Elimination — silver oxide, E2",
kw=["Ag₂O", "I⁻ → OH⁻ 교환", "E2", "N(CH₃)₃ 이탈"],
sum="제거 단계에는 산화은(Ag₂O)을 쓴다. 4차 암모늄염의 I⁻를 OH⁻로 바꿔 제거에 필요한 염기를 공급하고, OH⁻가 β-H를 떼며 N(CH₃)₃가 떨어지는 E2가 일어난다.",
tr="""<ul><li>제거 단계에는 <b>산화은</b>을 쓴다.</li>
<li>4차 암모늄염의 <b>아이오다이드 이온을 수산화 이온으로 교환</b>해 제거에 필요한 염기를 제공한다.</li></ul>
<p class="note">그림: HO⁻가 β-H를 공격, C–H 전자쌍이 C=C로, C–N⁺(CH₃)₃ 결합이 끊어짐 (E2 반응) → 알켄 + H₂O + N(CH₃)₃</p>""",
ex="""<p>Ag₂O + H₂O + 2 R₄N⁺I⁻ → 2 AgI↓ + 2 R₄N⁺OH⁻. AgI가 침전으로 빠지니 깨끗하게 OH⁻ 염이 됨.</p>
<p>그다음 가열 → E2: 염기·β-H·이탈기가 <b>안티 평면</b>으로 한 번에.</p>
<div class="box"><span class="tag">메커니즘 그리기</span>화살표 3개: ① HO⁻ → β-H ② C–H 결합 → C=C ③ C–N 결합 → N (N⁺(CH₃)₃가 중성 N(CH₃)₃로).</div>"""),

# 29
dict(img=29, slide=29, title="호프만 제거의 방향 — 덜 치환된 알켄 (호프만 규칙)", sub="Orientation in Hofmann Elimination",
kw=["호프만 규칙", "덜 붐비는 β-H", "1-펜텐 94 %", "자이체프와 반대"],
sum="(1-메틸뷰틸)트라이메틸암모늄 수산화물의 호프만 제거: 덜 붐비고 접근하기 쉬운 CH₃의 H가 제거돼 1-펜텐(94 %)이 주생성물, 2-펜텐은 6 %.",
tr="""<p class="note">그림: (1-메틸뷰틸)트라이메틸암모늄 수산화물 — 안쪽 CH₂의 H: 더 붐빔, 접근 어려움 / 바깥 CH₃의 H: 덜 붐빔, 접근 쉬움 → 1-펜텐(94 %) + 2-펜텐(6 %)</p>""",
ex="""<p>이탈기 –N⁺(CH₃)₃가 <b>크고 부피가 커서</b>, 안티 배열을 맞추기 쉬운 쪽·염기가 다가가기 쉬운 쪽 = 말단 CH₃의 H를 뗀다 → <y>덜 치환된 알켄</y>.</p>
<table class="t"><tr><th></th><th>자이체프 (보통 E2·E1)</th><th>호프만 (4차 암모늄)</th></tr>
<tr><td>주생성물</td><td>더 치환된 알켄 (안정)</td><td><b>덜 치환된 알켄</b></td></tr>
<tr><td>이유</td><td>열역학</td><td>입체 (부피 큰 이탈기)</td></tr></table>
<div class="box"><span class="tag">22장 연결</span>LDA가 덜 붐비는 α-H를 떼는 것과 같은 ‘한산한 쪽’ 논리.</div>"""),

# 30
dict(img=30, slide=30, title="예제 — N-에틸사이클로헥실아민의 호프만 제거", sub="Worked Example — Hofmann elimination product",
kw=["β-H가 있는 두 방향", "에틸렌 (주)", "사이클로헥센 (부)", "N,N-다이메틸사이클로헥실아민"],
sum="N-에틸사이클로헥실아민을 호프만 제거하면 β-H가 에틸기 쪽(CH₃, 3개)과 고리 쪽(CH₂)에 있다. 덜 붐비는 에틸 쪽 → H₂C=CH₂(주) + N,N-다이메틸사이클로헥실아민, 고리 쪽 → 사이클로헥센(부) + (CH₃)₂NCH₂CH₃.",
tr="""<p class="note">그림: N-에틸사이클로헥실아민(*표시 = β 탄소) → H₂C=CH₂ (주) + N,N-다이메틸사이클로헥실아민 / 또는 사이클로헥센 (부) + (CH₃)₂NCH₂CH₃</p>""",
ex="""<ol><li>CH₃I 과량 → N에 메틸 2개 추가 → N⁺(CH₃)₂(에틸)(사이클로헥실).</li>
<li>β-H 후보: 에틸기의 CH₃ (1차, 덜 붐빔) / 고리의 C2·C6 CH₂ (2차, 붐빔).</li>
<li>호프만 규칙 → 덜 붐비는 <b>에틸 쪽</b>이 주로 제거 → 에틸렌 + 남는 아민.</li></ol>
<div class="box"><span class="tag">시험 포인트</span>호프만 제거 생성물은 <b>알켄 + 3차 아민</b> 두 개. 어느 β-H가 빠지느냐에 따라 아민 쪽 구조도 바뀐다.</div>"""),

# 31
dict(img=31, slide=31, title="아릴아민의 반응 ① — EAS: –NH₂는 강한 o,p-활성화기", sub="Reactions of Arylamines — electrophilic aromatic substitution",
kw=["강한 활성화기", "o,p-지향", "2,4,6-트라이브로모아닐린", "아마이드로 조절"],
sum="–NH₂는 EAS에서 강한 활성화·o,p-지향기다. 아닐린 + Br₂(물) → 2,4,6-트라이브로모아닐린 100 % (멈출 수 없음). 반응을 조절하려면 아마이드로 바꾼다.",
tr="""<ul><li><b>친전자성 방향족 치환</b>
<ul><li>아미노 치환기는 친전자성 방향족 치환 반응에서 <b>강한 활성화기</b>이며 <b>오쏘·파라 지향기</b>다.</li>
<li>반응은 <b>아마이드로 바꿔</b> 조절한다.</li></ul></li></ul>
<p class="note">그림: 아닐린 —3 Br₂, H₂O→ 2,4,6-트라이브로모아닐린(100 %)</p>""",
ex="""<p>슬 9의 공명으로 o·p 탄소에 전자가 몰려 있어 Br₂가 촉매 없이도 <b>세 자리 모두</b> 치환 → 모노브로민화가 안 됨.</p>
<p>해결: <y>아세틸화</y>(Ac₂O) → 아세트아닐라이드 (–NHCOCH₃, 전자쌍이 C=O로 일부 빠져 <b>약한</b> 활성화기, 여전히 o,p) → 원하는 치환 → 가수분해로 –NH₂ 복원.</p>"""),

# 32
dict(img=32, slide=32, title="아릴아민의 반응 ② — 프리델-크래프츠는 아마이드로", sub="Reactions of Arylamines — Friedel–Crafts via amide",
kw=["AlCl₃와 산–염기 착물", "(CH₃CO)₂O, 피리딘", "C₆H₅COCl, AlCl₃", "NaOH, H₂O", "4-아미노벤조페논 80 %"],
sum="–NH₂는 AlCl₃ 촉매와 산–염기 착물을 만들어 프리델-크래프츠를 막는다. 그래서 아세트아마이드로 바꿔 아실화한 뒤 가수분해 → 4-아미노벤조페논(80 %).",
tr="""<ul><li>아미노기는 <b>AlCl₃ 촉매와 산–염기 착물</b>을 만들어 반응을 막는다.</li>
<li>그래서 해당 <b>아마이드</b>를 사용한다.</li></ul>
<p class="note">그림: 아닐린 —(CH₃CO)₂O, 피리딘→ 아세트아닐라이드 —C₆H₅COCl, AlCl₃→ p-벤조일 아세트아닐라이드 —NaOH, H₂O→ 4-아미노벤조페논(80 %)</p>""",
ex="""<p>ArNH₂ + AlCl₃ → ArNH₂⁺–AlCl₃⁻: N이 양전하를 띠면 고리가 <b>강한 비활성화</b> + 촉매도 소모 → F-C 실패.</p>
<p>아마이드 N은 염기성이 없어(슬 7) AlCl₃와 착물을 안 만듦 → F-C 가능, 부피 때문에 <b>파라</b> 선택.</p>
<div class="box"><span class="tag">보호기 3단계</span>① Ac₂O로 보호 ② EAS ③ NaOH/H₂O(또는 H₃O⁺)로 탈보호.</div>"""),

# 33
dict(img=33, slide=33, title="아릴아민의 반응 ③ — 설파제 (설파닐아마이드) 합성", sub="Reactions of Arylamines — sulfa drugs",
kw=["아세트아닐라이드", "HOSO₂Cl (클로로설폰화)", "NH₃", "NaOH, H₂O", "설파닐아마이드"],
sum="아미노 벤젠의 반응성을 조절하면 여러 EAS를 할 수 있다. 아세트아닐라이드 → 클로로설폰산 → NH₃ → 가수분해 = 설파닐아마이드(최초의 항균 설파제).",
tr="""<ul><li>아미노 치환 벤젠의 <b>반응성을 조절</b>하면 여러 종류의 친전자성 방향족 치환을 할 수 있다.</li>
<li><b>설파제</b>는 세균 감염에 임상적으로 쓰인 최초의 의약품 중 하나였다.</li></ul>
<p class="note">그림: 아세트아닐라이드 —HOSO₂Cl→ p-(아세트아미도)벤젠설포닐 클로라이드 —NH₃→ p-(아세트아미도)벤젠설폰아마이드 —NaOH, H₂O→ 설파닐아마이드(설파제)</p>""",
ex="""<ol><li><b>클로로설폰화</b>: HOSO₂Cl이 파라 자리에 –SO₂Cl (EAS).</li>
<li><b>설폰아마이드화</b>: NH₃가 S=O에 아실 치환처럼 Cl⁻ 밀어냄 → –SO₂NH₂.</li>
<li><b>탈보호</b>: 아마이드만 가수분해 (설폰아마이드는 안 끊어짐) → H₂N–C₆H₄–SO₂NH₂.</li></ol>
<div class="box"><span class="tag">약학</span>설파닐아마이드는 세균의 p-아미노벤조산(PABA)을 흉내 내 엽산 합성을 막음 (구조가 닮은 길항제).</div>"""),

# 34
dict(img=34, slide=34, title="예제 — 벤젠에서 m-클로로아닐린", sub="Worked Example — m-chloroaniline from benzene",
kw=["순서가 핵심", "–NO₂ = m-지향", "Cl₂, FeCl₃", "SnCl₂, H₃O⁺ → NaOH"],
sum="벤젠 → (HNO₃, H₂SO₄) 나이트로벤젠 → (Cl₂, FeCl₃) m-클로로나이트로벤젠 → (1. SnCl₂, H₃O⁺ 2. NaOH, H₂O) m-클로로아닐린.",
tr="""<ul><li>벤젠에서 <b>m-클로로아닐린</b>을 합성하는 방법을 제시하시오.</li></ul>
<p class="note">그림: 벤젠 —HNO₃, H₂SO₄→ 나이트로벤젠 —Cl₂, FeCl₃→ m-클로로나이트로벤젠 —1. SnCl₂, H₃O⁺ 2. NaOH, H₂O→ m-클로로아닐린</p>""",
ex="""<p>–NH₂와 –Cl이 <b>메타</b> 관계 → –NH₂(o,p)를 먼저 만들면 메타가 안 됨. <y>–NO₂(메타 지향)일 때 Cl을 넣고 마지막에 환원</y>.</p>
<div class="box"><span class="tag">전략</span>“메타 아닐린” = 나이트로 상태에서 치환 → 환원. “파라 아닐린” = 아세트아닐라이드 상태에서 치환 → 탈보호.</div>"""),

# 35
dict(img=35, slide=35, title="다이아조늄염 ① — 아릴아민 + HNO₂ → ArN₂⁺", sub="Reactions of Arylamines — diazonium salts",
kw=["HNO₂ (NaNO₂ + 산)", "아렌다이아조늄염", "알케인다이아조늄은 불안정", "N₂ 이탈 → 치환"],
sum="1차 아릴아민은 HNO₂와 반응해 안정한 아렌다이아조늄염(ArN₂⁺ HSO₄⁻)을 만든다(알케인다이아조늄은 분리 불가). 다이아조니오기는 친핵체로 치환되며 N₂가 빠진다.",
tr="""<ul><li><b>다이아조늄염: 산드마이어 반응</b>
<ul><li>1차 아릴아민은 <b>HNO₂</b>와 반응해 안정한 <b>아렌다이아조늄염</b>을 만든다.
<ul><li>해당 알케인다이아조늄은 <b>분리할 수 없다</b>.</li></ul></li></ul></li>
<li>아렌다이아조늄염이 유용한 이유: 다이아조니오기가 <b>치환 반응에서 친핵체로 바뀔 수 있기</b> 때문.</li></ul>
<p class="note">그림: ArNH₂ + HNO₂ + H₂SO₄ → ArN₂⁺ HSO₄⁻ + 2 H₂O · ArN₂⁺ + :Nu⁻ → Ar–Nu + N₂</p>""",
ex="""<p>–N₂⁺는 <y>최고의 이탈기</y>(N₂ 기체로 날아감). 그래서 Ar–NH₂ 하나로 Ar–Cl, Br, I, CN, OH, H 등 무엇이든 만드는 ‘만능 중간체’.</p>
<p>아릴은 공명으로 안정해 0–5 °C에서 유지, 알킬 다이아조늄(R–N₂⁺)은 바로 N₂를 잃고 탄소 양이온 → 혼합물.</p>
<div class="box"><span class="tag">시약</span>HNO₂는 불안정해서 보통 NaNO₂ + HCl(또는 H₂SO₄)로 그 자리에서 만든다.</div>"""),

# 36
dict(img=36, slide=36, title="다이아조늄염 ② — 산드마이어: CuCl·CuBr → ArCl·ArBr, NaI → ArI", sub="Reactions of Arylamines — Sandmeyer reaction",
kw=["산드마이어 반응", "CuBr / CuCl", "NaI", "p-브로모톨루엔 73 %", "아이오도벤젠 67 %"],
sum="산드마이어 반응: 아렌다이아조늄염 + 구리(I) 할라이드 → 아릴 클로라이드·브로마이드. 아릴 아이오다이드는 NaI와 직접 반응으로 만든다.",
tr="""<ul><li><b>산드마이어 반응</b>: 아렌다이아조늄염을 해당 <b>구리(I) 할라이드</b>와 반응시켜 아릴 클로라이드·브로마이드를 얻는다.</li>
<li><b>아릴 아이오다이드</b>는 NaI와의 직접 반응으로 만들 수 있다.</li></ul>
<p class="note">그림: p-메틸아닐린 —HNO₂, H₂SO₄→ [다이아조늄] —HBr, CuBr→ p-브로모톨루엔(73 %) · 아닐린 —HNO₂, H₂SO₄→ [다이아조늄] —NaI→ 아이오도벤젠(67 %)</p>""",
ex="""<p>Cu(I)이 필요한 이유: 라디칼 경로(슬 39) — Cu⁺가 전자 하나를 줘 아릴 라디칼 + N₂.</p>
<p>I⁻는 스스로 전자를 줄 만큼 좋은 환원제라 Cu 없이도 됨.</p>
<div class="box"><span class="tag">외우기</span>CuCl → Cl · CuBr → Br · NaI(KI) → I · CuCN → CN · Cu₂O/H₂O → OH · H₃PO₂ → H.</div>"""),

# 37
dict(img=37, slide=37, title="다이아조늄염 ③ — CuCN → 니트릴 → 카복실산", sub="Reactions of Arylamines — nitriles, phenols, arenes",
kw=["KCN, CuCN", "ArCN", "H₃O⁺ 가수분해 → ArCO₂H", "–OH, –H로 치환"],
sum="아렌다이아조늄염 + CuCN → 니트릴 ArCN, 가수분해하면 다른 작용기(카복실산)로. 다이아조니오기는 –OH(페놀), –H(아렌)로도 바뀐다.",
tr="""<ul><li>아렌다이아조늄염과 <b>CuCN</b>은 <b>니트릴 ArCN</b>을 주고, 이것은 다른 작용기로 가수분해될 수 있다.</li>
<li>다이아조니오기는 <b>–OH로 바뀌어 페놀</b>, <b>–H로 바뀌어 아렌</b>이 될 수 있다.</li></ul>
<p class="note">그림: o-메틸아닐린 —HNO₂, H₂SO₄→ o-메틸벤젠다이아조늄 바이설페이트 —KCN, CuCN→ o-메틸벤조나이트릴 —H₃O⁺→ o-메틸벤조산</p>""",
ex="""<p>–CN은 EAS로 직접 붙일 방법이 없어 → 다이아조늄이 유일한 길. 니트릴은 20장처럼 COOH(가수분해), CH₂NH₂(LiAlH₄), 케톤(RMgX)으로 변신.</p>
<div class="box"><span class="tag">합성 포인트</span>Ar–NH₂ → Ar–COOH: 탄소 1개 <b>늘리기</b> (호프만/커티어스는 반대로 줄이기).</div>"""),

# 38
dict(img=38, slide=38, title="다이아조늄염 ④ — Cu₂O, Cu(NO₃)₂ 수용액 → 페놀", sub="Reactions of Arylamines — phenols",
kw=["Cu₂O", "Cu(NO₃)₂, H₂O", "p-크레솔 93 %"],
sum="아렌다이아조늄염을 Cu(NO₃)₂ 수용액에서 산화 구리(I)와 반응시키면 페놀. p-메틸아닐린(p-톨루이딘) → p-크레솔(93 %).",
tr="""<ul><li>아렌다이아조늄염을 <b>질산 구리(II) 수용액</b>에서 <b>산화 구리(I)</b>와 반응시키면 <b>페놀</b>이 생긴다.</li></ul>
<p class="note">그림: p-메틸아닐린(p-톨루이딘) —HNO₂, H₂SO₄→ 다이아조늄 —Cu₂O, Cu(NO₃)₂, H₂O→ p-크레솔(93 %)</p>""",
ex="""<p>그냥 물에서 가열해도 페놀이 되지만 수율이 낮아 → Cu₂O 조건이 깨끗.</p>
<div class="box"><span class="tag">17장 연결</span>페놀 합성법: 쿠멘법 · 설폰산 알칼리 용융 · <b>다이아조늄 가수분해</b>.</div>"""),

# 39
dict(img=39, slide=39, title="탄화수소로 환원 — H₃PO₂로 –N₂⁺ → –H", sub="Reduction to a Hydrocarbon",
kw=["차인산 H₃PO₂", "자리 표시자로 –NH₂ 쓰기", "3,5-다이브로모톨루엔", "라디칼 경로"],
sum="다이아조늄염을 차인산(H₃PO₂)으로 처리하면 –H로 바뀐다. –NH₂를 ‘임시 지향기’로 써서 직접 못 만드는 3,5-다이브로모톨루엔을 만든다. 다이아조늄 치환은 라디칼 경로.",
tr="""<ul><li>다이아조늄염을 <b>차인산 H₃PO₂</b>로 처리한다.</li></ul>
<p class="note">그림: p-메틸아닐린 —2 Br₂→ (–NH₂의 o 자리 2곳에 Br) —HNO₂, H₂SO₄→ 다이아조늄 —H₃PO₂→ 3,5-다이브로모톨루엔 · [비교: 톨루엔 —2 Br₂, FeBr₃→ 2,4-다이브로모톨루엔]</p>
<ul><li>다이아조늄 치환은 <b>라디칼 경로</b>로 일어난다.</li></ul>
<p class="note">그림: ArN₂⁺ + CuX → [Ar· (아릴 라디칼) + Cu(HSO₄)X + N₂] → Ar–X + CuHSO₄</p>""",
ex="""<p>톨루엔을 직접 브로민화하면 CH₃(o,p)가 이끌어 2,4-다이브로모. 3,5-(CH₃의 메타 둘)를 원하면 → <y>–NH₂를 파라에 잠깐 두고</y> 그 o 자리(= CH₃의 m)에 Br 두 개 → –NH₂를 다이아조늄 → H₃PO₂로 지워버림.</p>
<div class="box"><span class="tag">시험 포인트</span>“–NH₂ 지우기” = HNO₂ → H₃PO₂. 지향기로 쓰고 버리는 전략.</div>"""),

# 40
dict(img=40, slide=40, title="예제 — 벤젠에서 p-브로모벤조산 (다이아조늄 치환)", sub="Worked Example — p-bromobenzoic acid",
kw=["CH₃Cl, AlCl₃", "나이트로화 → 환원", "HNO₂ → CuBr", "KMnO₄ 산화"],
sum="벤젠 → (CH₃Cl, AlCl₃) 톨루엔 → (HNO₃, H₂SO₄) p-나이트로톨루엔 → (SnCl₂, H₃O⁺; NaOH) p-톨루이딘 → (HNO₂, H₂SO₄) 다이아조늄 → (CuBr) p-브로모톨루엔 → (KMnO₄, H₂O) p-브로모벤조산.",
tr="""<ul><li>다이아조늄 치환 반응을 써서 벤젠에서 <b>p-브로모벤조산</b>을 어떻게 만드는가?</li></ul>
<p class="note">그림: 벤젠 —CH₃Cl, AlCl₃→ 톨루엔 —HNO₃, H₂SO₄→ p-나이트로톨루엔 —1. SnCl₂, H₃O⁺ 2. NaOH, H₂O→ p-메틸아닐린 —HNO₂, H₂SO₄→ 다이아조늄 —CuBr→ p-브로모톨루엔 —KMnO₄, H₂O→ p-브로모벤조산</p>""",
ex="""<p>왜 Br₂/FeBr₃를 안 쓰나? 톨루엔 브로민화는 o + p 혼합물. 나이트로화로 <b>파라를 먼저 확보</b>하고(분리), –NO₂ → –NH₂ → –N₂⁺ → <y>–Br</y>로 바꾸면 깔끔한 파라.</p>
<p>마지막 KMnO₄: 벤질 CH₃ → COOH (16장 곁사슬 산화).</p>
<div class="box"><span class="tag">순서</span>CH₃를 COOH로 먼저 바꾸면 메타 지향이 되어 파라 치환이 어려움 → 산화는 <b>마지막</b>.</div>"""),
]
