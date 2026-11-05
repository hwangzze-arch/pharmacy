# -*- coding: utf-8 -*-
# 제23장 슬라이드 32–43: 마이클 반응, 스토크 엔아민, 로빈슨 고리화, 생체 축합
PAGES = [
# 32
dict(img=32, slide=32, title="콘쥬게이트 카르보닐 첨가 — 마이클 반응", sub="Conjugate Carbonyl Additions: The Michael Reaction",
kw=["1,4-첨가", "α,β-불포화 받개", "β 탄소 공격", "콘쥬게이트 첨가 생성물"],
sum="친핵성 엔올레이트가 α,β-불포화 화합물의 β 탄소에 첨가하는 반응 = 마이클 반응. C=O가 아니라 C=C 끝(β)을 공격해서 콘쥬게이트(1,4) 첨가 생성물이 된다.",
tr="""<ul><li>친핵성 엔올레이트 이온이 <b>α,β-불포화 화합물</b>과 반응해 <b>콘쥬게이트 첨가 생성물</b>을 만드는 과정.</li></ul>
<p class="note">그림: α,β-불포화 케톤 + :Nu–H ⇌ [엔올레이트 중간체(β 탄소에 Nu⁺–H)] ⇌ Conjugate addition product(콘쥬게이트 첨가 생성물: β 탄소에 Nu, α 탄소에 H)</p>""",
ex="""<p><b>왜 β 탄소?</b> C=C–C=O 콘쥬게이션 때문에 공명 구조에서 <y>β 탄소가 δ+</y> (⁺C–C=C–O⁻). 그래서 친핵체가 C=O 탄소(1,2-첨가) 대신 β 탄소(1,4-첨가)를 공격할 수 있어.</p>
<p><b>화살표</b>: Nu → β 탄소, C=C π → α–C(=O) 쪽으로 밀려 엔올레이트(O⁻) → 양성자화 → α 탄소에 H.</p>
<table class="t"><tr><th>첨가</th><th>공격 위치</th><th>잘 하는 친핵체</th></tr><tr><td>1,2-첨가</td><td>C=O 탄소</td><td>강한 친핵체 (RLi, RMgX)</td></tr><tr><td><g>1,4-첨가 (마이클)</g></td><td>β 탄소</td><td>안정한 엔올레이트, 아민, 큐프레이트</td></tr></table>
<div class="box"><span class="tag">시험 포인트</span>생성물에서 Nu와 C=O 사이를 세면 Nu가 <b>β 위치</b>. 엔올레이트가 Nu면 결과는 <b>1,5-다이카르보닐</b>.</div>"""),

# 33
dict(img=33, slide=33, title="마이클 반응의 최적 조건 — 안정한 엔올레이트 + 덜 붐비는 엔온", sub="Optimal Conditions for the Michael Reaction",
kw=["β-케토 에스터 주개", "3-뷰텐-2-온 받개", "1,5-다이카르보닐", "NaOEt 촉매"],
sum="마이클 반응은 특히 안정한 엔올레이트(β-케토 에스터 등)와 덜 붐비는 α,β-불포화 케톤 조합에서 잘 된다. 에틸 아세토아세테이트 + 3-뷰텐-2-온 → 1,5-다이카르보닐.",
tr="""<ul><li><b>특히 안정한</b> 엔올레이트 이온과 <b>입체 장애가 없는</b> α,β-불포화 케톤이 관여한다.</li></ul>
<p class="note">그림: Ethyl acetoacetate(에틸 아세토아세테이트) + 3-Buten-2-one(3-뷰텐-2-온) —1. Na⁺ ⁻OEt, ethanol 2. H₃O⁺→ 마이클 생성물 (CH₃COCH(CO₂Et)CH₂CH₂COCH₃)</p>""",
ex="""<p><b>왜 안정한 엔올레이트?</b> 1,3-다이카르보닐 엔올레이트(pKa 11)는 덜 반응성이라 C=O 직접 공격(1,2-첨가, 가역)보다 <y>열역학적으로 유리한 1,4-첨가</y>를 해. 단순 케톤 엔올레이트는 C=O를 공격하기 쉬워.</p>
<p><b>생성물</b>: 아세토아세테이트 가운데 탄소(분홍 CH₂) – CH₂CH₂COCH₃. 주개의 C=O와 받개의 C=O 사이에 탄소 3개 → <g>1,5-다이카르보닐</g>.</p>
<p>이 생성물을 22장처럼 H₃O⁺, 가열하면 탈카르복실화 → 2,6-헵탄다이온 → 분자 내 알돌(슬 18) → 사이클로헥센온. 이게 바로 로빈슨 고리화(슬 39)!</p>
<div class="box"><span class="tag">정리</span>마이클 주개 = 안정한 C⁻ (슬 35 표 오른쪽), 받개 = 덜 붐비는 엔온 (표 왼쪽).</div>"""),

# 34
dict(img=34, slide=34, title="그림 23.6 — 마이클 반응 메커니즘", sub="Figure 23.6 — Mechanism of the Michael Reaction",
kw=["① 엔올레이트 생성", "② β 탄소 공격", "새 엔올레이트", "③ 양성자 교환"],
sum="① 염기 촉매가 β-케토 에스터의 산성 α-H를 떼어 안정한 엔올레이트. ② 그 엔올레이트가 α,β-불포화 케톤의 β 탄소에 첨가 → 새 엔올레이트. ③ 새 엔올레이트가 용매나 출발물질에서 H⁺를 받아 생성물.",
tr="""<ol><li>염기 촉매가 출발 β-케토 에스터에서 산성 α 양성자를 떼어 <b>안정한 엔올레이트 친핵체</b>를 만든다.</li>
<li>친핵체가 마이클 반응으로 α,β-불포화 케톤 친전자체에 <b>첨가</b>해 생성물인 새 엔올레이트를 만든다.</li>
<li>엔올레이트 생성물이 용매나 출발 케토 에스터에서 산성 양성자를 떼어 <b>최종 첨가 생성물</b>이 된다.</li></ol>""",
ex="""<p><b>① 화살표</b>: EtO⁻ → 두 C=O 사이 H, C–H → C⁻.</p>
<p><b>② 화살표</b> (그림의 분홍): 엔올레이트 C⁻ → 3-뷰텐-2-온의 <b>말단 CH₂(β 탄소)</b> 공격, C=C π 전자가 C–C=O 쪽으로 이동해 새 엔올레이트 (O⁻, C=C).</p>
<p><b>③</b>: 새 엔올레이트의 α 탄소가 EtOH의 H를 받음 → 케톤 + EtO⁻ 재생 (그래서 <y>염기 촉매량</y>).</p>
<div class="box"><span class="tag">메커니즘 그리기</span>②에서 화살표는 C⁻ → <b>β 탄소</b>, β=α 결합 → α–C 결합, C=O π → O. 세 개가 한 번에 (콘쥬게이트 첨가).</div>"""),

# 35
dict(img=35, slide=35, title="표 23.1 — 마이클 받개와 마이클 주개", sub="Table 23.1 — Some Michael Acceptors and Some Michael Donors",
kw=["받개: α,β-불포화 C=O·C≡N·NO₂", "주개: 1,3-다이카르보닐", "β-케토 나이트릴", "나이트로 화합물"],
sum="마이클 받개는 C=C가 전자 끄는 기(CHO, COR, CO₂Et, CONH₂, CN, NO₂)와 콘쥬게이션된 화합물, 주개는 두 전자 끄는 기 사이 CH₂를 가진 화합물(β-다이케톤, β-케토 에스터, 말론산 다이에틸, β-케토 나이트릴, 나이트로 화합물).",
tr="""<table class="t"><tr><th>Michael acceptors (마이클 받개)</th><th>Michael donors (마이클 주개)</th></tr>
<tr><td>H₂C=CHCHO 프로펜알 (Propenal)</td><td>RCOCH₂COR′ β-다이케톤 (β-Diketone)</td></tr>
<tr><td>H₂C=CHCOCH₃ 3-뷰텐-2-온 (3-Buten-2-one)</td><td>RCOCH₂CO₂Et β-케토 에스터 (β-Keto ester)</td></tr>
<tr><td>H₂C=CHCO₂Et 에틸 프로펜오에이트 (Ethyl propenoate)</td><td>EtO₂CCH₂CO₂Et 말론산 다이에틸 (Diethyl malonate)</td></tr>
<tr><td>H₂C=CHCONH₂ 프로펜아마이드 (Propenamide)</td><td>RCOCH₂C≡N β-케토 나이트릴 (β-Keto nitrile)</td></tr>
<tr><td>H₂C=CHC≡N 프로펜나이트릴 (Propenenitrile)</td><td>RCH₂NO₂ 나이트로 화합물 (Nitro compound)</td></tr>
<tr><td>H₂C=CHNO₂ 나이트로에틸렌 (Nitroethylene)</td><td></td></tr></table>""",
ex="""<p><b>받개 공통점</b>: H₂C=CH–<y>EWG</y>(전자 끄는 기). EWG가 β 탄소를 δ+로 만들어.</p>
<p><b>주개 공통점</b>: EWG–CH₂–EWG (또는 CH₂NO₂). 두 EWG가 음전하를 나눠 안정 → 약염기(NaOEt) 촉매로 충분, 1,4-첨가 선택.</p>
<p>분홍색 CH₂/CH가 탈양성자되는 자리.</p>
<div class="box"><span class="tag">시험 포인트</span>“다음 중 마이클 주개/받개가 될 수 있는 것은?” 형태. 받개 = C=C–EWG, 주개 = 산성 CH (pKa 9–13)라고 기억해.</div>"""),

# 36
dict(img=36, slide=36, title="엔아민과의 카르보닐 축합 — 스토크 반응: 엔아민 만들기", sub="Carbonyl Condensations with Enamines: The Stork Reaction",
kw=["케톤 + 2차 아민", "엔아민", "피롤리딘", "−H₂O"],
sum="엔아민은 케톤과 2차 아민(피롤리딘 등)으로 만든다. 사이클로헥사논 + 피롤리딘 ⇌ 1-피롤리디노사이클로헥센(87 %) + H₂O.",
tr="""<ul><li><b>엔아민</b>은 케톤과 <b>2차 아민</b>으로부터 만들어진다.</li></ul>
<p class="note">그림: Cyclohexanone(사이클로헥사논) + Pyrrolidine(피롤리딘) ⇌ 1-Pyrrolidinocyclohexene(1-피롤리디노사이클로헥센, 87 %) + H₂O</p>""",
ex="""<p><b>19장 복습</b>: 케톤 + 1차 아민(RNH₂) → 이민(C=NR) / 케톤 + <y>2차 아민(R₂NH)</y> → 엔아민(C=C–NR₂).</p>
<p>2차 아민은 N에 H가 하나뿐 → 이미늄(C=N⁺R₂)에서 N이 H를 더 잃을 수 없어서 <b>α 탄소의 H</b>가 빠지며 C=C가 생겨.</p>
<p>메커니즘: 아민이 C=O 공격 → 카비놀아민 → OH 양성자화, H₂O 이탈 → 이미늄 이온 → α-H 제거 → 엔아민. 물을 제거하면 평형이 오른쪽.</p>
<div class="boxg">엔아민 = <b>중성인데 엔올레이트처럼</b> α 탄소가 친핵성 (다음 쪽). 강염기 없이 쓸 수 있는 ‘엔올레이트 대용품’.</div>"""),

# 37
dict(img=37, slide=37, title="엔아민은 친핵성이다", sub="Enamines Are Nucleophilic",
kw=["N 비공유전자쌍", "π 오비탈 겹침", "α 탄소 전자 밀도 ↑", "엔올레이트와 비교"],
sum="질소의 비공유전자쌍 오비탈이 C=C π 오비탈과 겹쳐 α 탄소의 전자 밀도를 높인다. 엔올레이트(O⁻)와 같은 원리로 α 탄소가 친핵성.",
tr="""<ul><li>질소 비공유전자쌍 오비탈과 이중결합 π 오비탈의 <b>겹침</b>이 α 탄소 원자의 <b>전자 밀도를 증가</b>시킨다.</li></ul>
<p class="note">그림: An enolate ion(엔올레이트) :O⁻–C=C ↔ O=C–C⁻ · An enamine(엔아민) :NR₂–C=C ↔ ⁺NR₂=C–C⁻ — Nucleophilic alpha carbon(친핵성 α 탄소). 오른쪽: 엔아민의 정전기 전위 지도 (α 탄소 쪽이 빨강 = 전자 풍부)</p>""",
ex="""<p><b>공명 비교</b></p>
<table class="t"><tr><th></th><th>엔올레이트</th><th>엔아민</th></tr>
<tr><td>밀어주는 원자</td><td>O⁻ (음전하)</td><td>N: (중성)</td></tr>
<tr><td>공명형</td><td>O=C–C⁻</td><td>⁺NR₂=C–C⁻</td></tr>
<tr><td>친핵성</td><td>강함</td><td>중간 (중성이라 약하지만 충분)</td></tr></table>
<p>N은 O보다 전기음성도가 작아 전자를 <y>더 잘 내줘</y> → 중성 엔올(C=C–OH)보다 엔아민이 훨씬 친핵성.</p>
<div class="box"><span class="tag">시험 포인트</span>“엔아민의 친핵성 탄소는?” → N이 붙은 탄소가 아니라 <b>C=C의 반대쪽 탄소(α 탄소)</b>. 지도의 빨간 부분.</div>"""),

# 38
dict(img=38, slide=38, title="엔아민 첨가와 가수분해 → 1,5-다이케톤", sub="Enamine Addition and Hydrolysis",
kw=["① 엔아민 생성", "② 마이클 첨가", "③ H₂O 가수분해", "1,5-다이케톤 71 %"],
sum="엔아민이 α,β-불포화 카르보닐 받개에 마이클 첨가하고, 생성물(이미늄/엔아민)을 물로 가수분해하면 1,5-다이카르보닐 화합물이 된다. 사이클로헥사논 → 엔아민 → 3-뷰텐-2-온 첨가 → H₂O → 1,5-다이케톤(71 %).",
tr="""<ul><li>엔아민이 <b>α,β-불포화 카르보닐 받개</b>에 첨가한다.</li>
<li>생성물을 가수분해하면 <b>1,5-다이카르보닐</b> 화합물이 된다.</li></ul>
<p class="note">그림: Cyclohexanone(사이클로헥사논) —① 피롤리딘→ An enamine(엔아민) —② H₂C=CHCOCH₃→ [이미늄 이온 → 엔아민] —③ H₂O→ 피롤리딘 + A 1,5-diketone(1,5-다이케톤, 71 %)</p>""",
ex="""<p><b>스토크 엔아민 반응 3단계</b></p>
<ol><li><b>엔아민 생성</b>: 케톤 + 피롤리딘 (−H₂O).</li>
<li><b>마이클 첨가</b>: 엔아민 α 탄소 → 3-뷰텐-2-온 β 탄소. N 전자쌍이 내려와 이미늄(C=N⁺) + 받개 쪽 엔올레이트 → 양성자 이동.</li>
<li><b>가수분해</b>: H₂O가 이미늄 C=N⁺ 공격 → 케톤 복구 + 피롤리딘 회수.</li></ol>
<p>결과: 사이클로헥사논 C2에 –CH₂CH₂COCH₃ = <g>2-(3-옥소뷰틸)사이클로헥사논</g>.</p>
<div class="box"><span class="tag">장점</span>강염기 없이 중성 조건 → 케톤 자기 알돌·다중 첨가 같은 부반응이 적어. 결과는 ‘케톤 엔올레이트로 마이클 한 것’과 같아.</div>"""),

# 39
dict(img=39, slide=39, title="로빈슨 고리화 반응 — 마이클 + 분자 내 알돌", sub="The Robinson Annulation Reaction",
kw=["2단계", "마이클 반응", "분자 내 알돌", "새 사이클로헥센온 고리"],
sum="로빈슨 고리화 = 마이클 반응 + 분자 내 알돌 축합. 친핵성 주개(β-케토 에스터, 엔아민 등)와 α,β-불포화 케톤 받개가 만나 새 6원 고리 엔온을 만든다.",
tr="""<ul><li><b>2단계</b> 과정
<ul><li><b>마이클 반응</b>과 <b>분자 내 알돌 반응</b>을 결합한다.</li></ul></li>
<li>필요한 반응물은 친핵성 주개(β-케토 에스터, 엔아민 등)와 α,β-불포화 케톤 받개이다.</li></ul>
<p class="note">그림: 3-Buten-2-one(3-뷰텐-2-온) + Ethyl acetoacetate(에틸 아세토아세테이트) —Na⁺ ⁻OEt, Michael reaction(마이클 반응)→ [Michael product(마이클 생성물, 1,5-다이케톤)] —Na⁺ ⁻OEt, Aldol reaction(알돌 반응)→ Annulation product(고리화 생성물)</p>
<p class="note">※ 슬라이드의 “Micheal”은 Michael의 오타.</p>""",
ex="""<p><b>단계</b></p>
<ol><li><b>마이클</b>: 아세토아세테이트 C⁻ → 뷰텐온 β 탄소 → 1,5-다이케톤 (CO₂Et 붙음).</li>
<li><b>분자 내 알돌</b>: 뷰텐온 쪽 말단 CH₃의 엔올레이트 → 아세토아세테이트 쪽 C=O 공격 → <y>6원 고리</y> (1,5-다이케톤 → 6원, 슬 18).</li>
<li><b>탈수</b> → 사이클로헥센온 (콘쥬게이션 엔온).</li></ol>
<p><b>‘annulation’</b> = 고리(annulus)를 하나 더 붙이기. 기존 고리 케톤을 주개로 쓰면 이환 화합물이 돼 (스테로이드, 다음 쪽).</p>
<div class="box"><span class="tag">역합성 요령</span>생성물에 사이클로헥센온이 있으면 → C=C의 β 탄소 쪽을 C=O로 되돌리고(알돌 역) → 그 1,5-다이케톤을 마이클로 끊어(주개 + 엔온). 시험에 자주 나오는 2단계 끊기.</div>"""),

# 40
dict(img=40, slide=40, title="그림 23.8 — 스테로이드 호르몬 에스트론 합성", sub="Figure 23.8 — Synthesis of the Steroid Hormone Estrone",
kw=["마이클 받개: α,β-불포화 케톤", "마이클 주개: β-다이케톤", "로빈슨 고리화", "에스트론"],
sum="로빈슨 고리화로 스테로이드 골격을 만든다. α,β-불포화 케톤 받개 + 2-메틸-1,3-사이클로펜탄다이온 주개 → 마이클 생성물 → 분자 내 알돌·탈수 → 로빈슨 고리화 생성물 → … → 에스트론.",
tr="""<p class="note">그림: Michael acceptor(마이클 받개, α,β-불포화 케톤) + Michael donor(마이클 주개, β-다이케톤: 2-메틸사이클로펜탄-1,3-다이온) —Base(염기)→ [Michael product(마이클 생성물)] —Base→ Robinson annulation product(로빈슨 고리화 생성물) ⟹ (여러 단계) Estrone(에스트론)</p>
<p>슬라이드는 그림뿐이야.</p>""",
ex="""<p><b>1. 마이클</b>: 2-메틸-1,3-사이클로펜탄다이온의 두 C=O 사이 C–H(분홍 H, pKa ~9) → 엔올레이트 → 받개의 말단 CH₂=(β 탄소) 공격.</p>
<p><b>2. 분자 내 알돌 + 탈수</b>: 받개에서 온 케톤 옆 CH₂가 엔올레이트 → 사이클로펜탄다이온의 C=O 하나를 공격 → 새 6원 고리 → 엔온.</p>
<p>결과: 메톡시페닐(A 고리) – 새 고리(C 고리) – 5원 고리(D 고리) 골격. 이후 몇 단계로 B 고리를 닫고 환원하면 <g>에스트론</g> (여성 호르몬).</p>
<div class="boxg">로빈슨 고리화는 스테로이드·테르펜처럼 6원 고리가 이어진 천연물 합성의 핵심 도구.</div>"""),

# 41
dict(img=41, slide=41, title="생체 카르보닐 축합 ① — 제1형 알돌레이스 (엔아민 경유)", sub="Some Biological Carbonyl Condensation Reactions",
kw=["탄수화물 대사", "제1형 알돌레이스", "효소 라이신 –NH₂", "엔아민 → 이미늄"],
sum="생체 알돌 반응은 탄수화물 대사에 흔하다. 동물·고등식물의 제1형 알돌레이스는 효소의 –NH₂가 다이하이드록시아세톤 포스페이트와 엔아민을 만들고, 그 엔아민이 글리세르알데하이드 3-인산에 알돌 → 이미늄 → 가수분해 → 과당 1,6-이인산.",
tr="""<ul><li>생체 알돌 반응은 <b>탄수화물 대사</b>에서 널리 발견된다.
<ul><li><b>제1형 알돌레이스</b>는 주로 동물과 고등식물에 있다.</li></ul></li></ul>
<p class="note">그림: Dihydroxyacetone phosphate(다이하이드록시아세톤 포스페이트) + Enz–NH₂ → Enamine(엔아민) + Glyceraldehyde 3-phosphate(글리세르알데하이드 3-인산) → Iminium ion(이미늄 이온) —H₂O→ Fructose 1,6-bisphosphate(과당 1,6-이인산)</p>""",
ex="""<p><b>스토크 반응(슬 36–38)의 생체판</b></p>
<ol><li>효소 라이신의 1차 아민(Enz–NH₂) + 케톤(DHAP) → 이민 → 엔아민 (α 탄소 친핵성).</li>
<li>엔아민 α 탄소 → 글리세르알데하이드 3-인산의 알데하이드 C=O 공격(H–A가 O에 H⁺ 제공) → 새 C–C 결합 + 이미늄.</li>
<li>H₂O로 이미늄 가수분해 → 케톤 복구 + 효소 회수 → 과당 1,6-이인산.</li></ol>
<p>해당과정(glycolysis)에서는 이 반응이 <y>역방향(역알돌)</y>으로 과당 1,6-이인산을 C3 두 개로 쪼개.</p>
<div class="boxg">C3 + C3 → C6 혼합 알돌. 주개 = 케톤(DHAP), 받개 = 알데하이드(G3P).</div>"""),

# 42
dict(img=42, slide=42, title="생체 카르보닐 축합 ② — 제2형 알돌레이스 (Zn²⁺ 엔올레이트)", sub="Some Biological Carbonyl Condensation Reactions",
kw=["제2형 알돌레이스", "균류·세균", "Zn²⁺ 루이스 산", "혼합 알돌"],
sum="균류·세균의 제2형 알돌레이스는 엔아민 대신 Zn²⁺가 받개 C=O를 활성화하고, 염기가 만든 엔올레이트가 공격한다. 알돌레이스 반응은 서로 다른 두 파트너 사이의 혼합 알돌이다.",
tr="""<ul><li><b>제2형 알돌레이스</b>는 주로 균류와 세균에 있다.</li>
<li>알돌레이스 촉매 반응은 서로 다른 두 파트너 사이에서 일어나는 <b>혼합 알돌 반응</b>이다.</li></ul>
<p class="note">그림: Dihydroxyacetone phosphate(다이하이드록시아세톤 포스페이트) —:Base가 α-H 제거, H–B⁺가 C=O 양성자화→ 엔다이올 → Glyceraldehyde 3-phosphate의 C=O(Zn²⁺ 배위)를 공격, H–A → Fructose 1,6-bisphosphate(과당 1,6-이인산)</p>""",
ex="""<p><b>제1형 vs 제2형</b></p>
<table class="t"><tr><th></th><th>제1형</th><th>제2형</th></tr>
<tr><td>분포</td><td>동물·고등식물</td><td>균류·세균</td></tr>
<tr><td>친핵체</td><td>엔아민 (효소 –NH₂)</td><td>엔올/엔올레이트 (효소 염기)</td></tr>
<tr><td>받개 활성화</td><td>H–A 양성자화</td><td><y>Zn²⁺</y> 루이스 산이 C=O 배위</td></tr></table>
<p>Zn²⁺가 알데하이드 산소에 붙으면 C=O 탄소가 더 δ+ → 엔올 공격이 쉬워 (실험실의 산 촉매 역할).</p>
<div class="box"><span class="tag">시험 포인트</span>두 효소 모두 결국 <b>케톤(주개) + 알데하이드(받개)</b> 혼합 알돌. 실험실에서 혼합 알돌이 어려운 문제(슬 14)를 효소는 위치를 정해 해결해.</div>"""),

# 43
dict(img=43, slide=43, title="생체 클라이젠 축합 — 지방산 생합성", sub="Biological Claisen Condensations",
kw=["말로닐 ACP", "탈카르복실화로 엔올레이트", "아세틸 싸이오에스터", "아세토아세틸 ACP"],
sum="생체 클라이젠 축합은 지방산 생합성 등 많은 경로에 있다. 말로닐 ACP가 CO₂를 잃으며 엔올레이트가 되고, 그것이 아세틸–S–합성효소를 공격해 아세토아세틸 ACP(β-케토 싸이오에스터)가 된다.",
tr="""<ul><li>많은 생체 경로에 널리 존재한다.
<ul><li><b>지방산 생합성</b></li></ul></li></ul>
<p class="note">그림: Malonyl ACP(말로닐 ACP) —CO₂ 이탈→ Enolate ion(엔올레이트) + Acetyl synthase(아세틸 합성효소, CH₃CO–S–Synthase) → 사면체 중간체(A–H) —Synthase–SH 이탈→ Acetoacetyl ACP(아세토아세틸 ACP)</p>""",
ex="""<p><b>단계</b></p>
<ol><li><b>탈카르복실화로 엔올레이트</b>: 말로닐 ACP의 ⁻OOC–CH₂–CO–SACP에서 CO₂가 빠지며 C⁻ (22장 탈카르복실화와 같은 원리: β-카르보닐).</li>
<li><b>클라이젠 첨가</b>: 엔올레이트 → CH₃C(=O)–S–Synthase의 C=O 공격 → 사면체 (H–A가 O 양성자화 도움).</li>
<li><b>이탈</b>: O⁻ → C=O 복구, <y>Synthase–S⁻ 이탈</y> (싸이올레이트 = 좋은 이탈기) → 아세토아세틸 ACP.</li></ol>
<p>실험실 클라이젠(에스터 + 에스터 → β-케토 에스터)과 같은 구조: 생체에서는 <g>싸이오에스터</g>를 써.</p>
<div class="boxg">이 C2 단위 추가가 반복되면 C16 팔미트산까지. 지방산 탄소 수가 대부분 <b>짝수</b>인 이유.</div>"""),
]
