# -*- coding: utf-8 -*-
# 제22장 슬라이드 14–24: 부프로피온 합성, 엔올레이트, pKa 표, 할로폼, 알킬화, 말론산 에스터 합성
from fig import row

BUP = row(('m', 'N#Cc1cccc(Cl)c1', 92, 70), ('a', '1. EtMgBr', '2. H₃O⁺'),
          ('m', 'CCC(=O)c1cccc(Cl)c1', 105, 70), ('a', 'Br₂', 'DCM'),
          ('m', 'CC(Br)C(=O)c1cccc(Cl)c1', 110, 78))
BUP2 = row(('a', 't-BuNH₂', 'ACN'), ('m', 'CC(NC(C)(C)C)C(=O)c1cccc(Cl)c1', 140, 82), ('a', 'HCl', ''), ('t', '부프로피온 염산염'))

PAGES = [
# 14
dict(img=14, slide=14, title="부프로피온 염산염 합성 — 빈칸 채우기", sub="Synthesis of bupropion hydrochloride (Synthetic Communications 40: 1566–1573, 2010)",
kw=["Grignard + 니트릴 → 케톤", "α-브로민화", "S<sub>N</sub>2 아민화", "염산염", "아미노케톤 항우울제"],
sum="3-클로로벤조니트릴 → (EtMgBr, H₃O⁺) 케톤 → (Br₂) α-브로모 케톤 → (t-BuNH₂) α-아미노 케톤 = 부프로피온 → HCl 염. 22장 α-브로민화가 핵심 단계야.",
tr="""<p><b>부프로피온 염산염(bupropion hydrochloride)의 합성</b></p>
<ul><li>약물 계열: <b>아미노케톤 계열 항우울제</b></li>
<li>미국 최초 승인: 1985년</li>
<li>주요 적응증: 우울증 및 금연 보조 치료</li></ul>
<p class="note">그림: 3-클로로벤조니트릴 —1. EtMgBr 2. H₃O⁺, H₂O→ [ ? ] —Br₂, DCM→ [ ? ] —t-BuNH₂(tert-부틸아민), ACN→ [ ? ] —HCl→ 부프로피온 염산염. 사진: 국내 시판 부프로피온 제품.</p>
<p class="note">ACN = 아세토나이트릴(용매), DCM = 다이클로로메테인(용매).</p>""",
ex=f"""<p><b>빈칸 정답</b></p>{BUP}{BUP2}
<ol><li><b>EtMgBr → H₃O⁺</b>: Grignard가 C≡N 탄소에 첨가 → 이민 음이온(Mg염) → 산 가수분해로 <y>케톤</y> (20장 니트릴 반응). 3'-클로로프로피오페논.</li>
<li><b>Br₂, DCM</b>: <g>α-브로민화</g> (슬 8–9). α 탄소(CH₂)에 Br 하나. 생기는 HBr이 엔올화 촉매.</li>
<li><b>t-BuNH₂</b>: 아민 N이 C–Br 탄소를 공격 → Br⁻ 이탈 (<b>S<sub>N</sub>2</b>). C=O 옆 탄소라 S<sub>N</sub>2가 아주 빨라.</li>
<li><b>HCl</b>: 아민을 염산염으로 → 물에 잘 녹고 안정한 의약품 형태.</li></ol>
<div class="box"><span class="tag">시험 포인트</span>빈칸형 합성 문제로 딱 좋아. “α-할로 케톤 + 아민 = α-아미노 케톤” 연결을 기억해.</div>"""),

# 15
dict(img=15, slide=15, title="α 수소의 산성도 ① — 엔올레이트 이온 형성", sub="Acidity of Alpha Hydrogen Atoms: Enolate Ion Formation",
kw=["약산", "sp³ → sp²", "p 오비탈 겹침", "NaH · LDA", "공명 안정화"],
sum="카르보닐 화합물은 약산(α-H pKa 19–20)이라 엔올레이트를 완전히 만들려면 강염기(NaH, LDA)가 필요하다. α 탄소가 sp²가 되며 C=O π와 겹쳐 음전하가 퍼진다.",
tr="""<ul><li>카르보닐 화합물은 <b>약산</b>으로 작용할 수 있다.</li>
<li>엔올레이트 이온 형성에는 <b>강염기</b>가 필요하다.</li>
<li>수소화 소듐(<b>NaH</b>) 또는 리튬 다이아이소프로필아마이드 [LiN(i-C₃H₇)₂] (<b>LDA</b>)는 엔올레이트를 만들 만큼 충분히 강하다.</li></ul>
<p class="note">그림: sp³ 혼성 α 탄소 —염기(Base)→ sp² 혼성 탄소 ↔ 공명 구조. 정전기 지도: 탄소와 산소 양쪽이 “Electron-rich”.</p>""",
ex="""<p><b>그림 읽기</b>: α-H가 빠지면 α 탄소가 sp³ → <y>sp²</y>로 바뀌어. 남은 전자쌍이 들어간 p 오비탈이 C=O의 π 오비탈과 <b>나란히 겹쳐서</b> 음전하가 O까지 퍼져(공명).</p>
<p><b>얼마나 약한 산?</b> 아세톤 pKa ≈ 19. 일반 알케인 C–H ≈ 50이니까 10³¹배 산성이지만, 물(15.7)·알코올(16)보다는 약해.</p>
<table class="t"><tr><th>염기</th><th>짝산 pKa</th><th>케톤(19)을 완전히?</th></tr>
<tr><td>NaOH</td><td>15.7</td><td>× 일부만 (평형)</td></tr>
<tr><td>NaOEt</td><td>16</td><td>× 일부만</td></tr>
<tr><td>NaH</td><td>35 (H₂)</td><td>○ 완전</td></tr>
<tr><td><b>LDA</b></td><td><b>36</b></td><td><g>○ 완전 · 빠르게</g></td></tr></table>
<div class="boxg"><b>규칙</b> 산–염기 평형은 <b>pKa가 큰 쪽(더 약한 산)</b>으로 기울어. 염기의 짝산 pKa가 α-H pKa보다 충분히 크면 엔올레이트로 완전히 전환돼.</div>
<div class="box"><span class="tag">산 세기 순서</span>이 비교가 시험의 “산 강도 순서” 문제와 직결돼. 다음 슬라이드들(17–18)의 pKa 값과 같이 외워.</div>"""),

# 16
dict(img=16, slide=16, title="α 수소의 산성도 ② — LDA", sub="Lithium diisopropylamide (LDA)",
kw=["BuLi + 다이아이소프로필아민", "pKa 36", "THF · 저온", "부피 큰 염기", "친핵성 약함"],
sum="LDA는 BuLi와 다이아이소프로필아민(pKa 36)으로 만든다. 유기용매에 잘 녹고 저온에서도 효과적이며, 부피가 커서 C=O를 공격하지 않고 α-H만 뗀다.",
tr="""<ul><li>LDA는 <b>뷰틸리튬(BuLi)</b>과 <b>다이아이소프로필아민</b>(pKa = 36)으로부터 만든다.</li>
<li>유기 용매에 녹고, 많은 화합물에 대해 <b>저온에서 효과적</b>이다.</li></ul>
<p class="note">그림: 다이아이소프로필아민 —C₄H₉Li, THF→ 리튬 다이아이소프로필아마이드(LDA) + C₄H₁₀(뷰테인) / 사이클로헥사논 —LDA, 테트라하이드로퓨란(THF) 용매→ 사이클로헥사논 엔올레이트 이온(Li⁺) + 다이아이소프로필아민</p>""",
ex="""<p><b>LDA 만들기</b>: BuLi(짝산 뷰테인 pKa ~50)가 N–H(pKa 36)를 떼어 → LDA + 뷰테인. 산–염기 반응이야.</p>
<p><b>LDA가 좋은 이유 3가지</b></p>
<ol><li><y>충분히 강함</y>: 짝산 pKa 36 ≫ 케톤 19 → 엔올레이트로 <b>완전 전환</b>(되돌아가지 않음).</li>
<li><y>부피가 큼</y>: 아이소프로필 2개가 N을 가려서 C=O 탄소를 공격(친핵 첨가)하지 못해 → <g>염기로만 작용</g>.</li>
<li><y>저온(−78 °C)·THF에서 작동</y>: 부반응이 적고, 비대칭 케톤에서 <b>덜 치환된 쪽(입체적으로 쉬운 쪽)</b> α-H를 빠르게 뗀다(속도론적 엔올레이트, 슬 35).</li></ol>
<div class="box"><span class="tag">비교 포인트</span>NaOEt는 엔올레이트를 조금만 만들고 남은 케톤과 반응(알돌, 23장)할 수 있어. LDA는 케톤을 <b>전부</b> 엔올레이트로 바꾸니 알킬화만 깨끗하게 돼.</div>"""),

# 17
dict(img=17, slide=17, title="α 수소의 산성도 ③ — 두 카르보닐 사이의 수소", sub="1,3-Dicarbonyl compounds: 2,4-pentanedione (pKa = 9)",
kw=["1,3-다이카르보닐", "pKa 9", "음전하 3곳 분산", "약한 염기로 충분"],
sum="두 카르보닐 사이에 낀 α-H는 훨씬 산성이다(2,4-펜탄다이온 pKa 9). 엔올레이트의 음전하가 두 산소와 탄소 세 곳에 퍼지기 때문.",
tr="""<ul><li>수소 원자가 <b>두 카르보닐기 사이</b>에 있으면 산성도가 커진다.</li>
<li>엔올레이트의 음전하가 <b>두 카르보닐기 모두</b>에 걸쳐 비편재화된다.</li></ul>
<p class="note">그림: 2,4-펜탄다이온(2,4-Pentanedione, pKa = 9) —염기(Base)→ 공명 구조 3개 (왼쪽 O⁻ ↔ 가운데 C⁻ ↔ 오른쪽 O⁻)</p>""",
ex="""<p><b>공명 구조 3개</b>: 음전하가 ① 왼쪽 산소 ② 가운데 탄소 ③ 오른쪽 산소. 퍼질 곳이 많을수록 음이온이 안정 → 짝산(원래 분자)이 강한 산.</p>
<table class="t"><tr><th>화합물</th><th>α-H를 끼고 있는 기</th><th>pKa</th></tr>
<tr><td>아세톤 CH₃COCH₃</td><td>C=O 하나</td><td>19</td></tr>
<tr><td>아세토아세트산 에틸 (β-케토 에스터)</td><td>C=O + CO₂Et</td><td>11</td></tr>
<tr><td>2,4-펜탄다이온 (β-다이케톤)</td><td>C=O + C=O</td><td><g>9</g></td></tr>
<tr><td>말론산 다이에틸 (1,3-다이에스터)</td><td>CO₂Et + CO₂Et</td><td>13</td></tr></table>
<p><b>왜 다이케톤 &gt; 케토에스터 &gt; 다이에스터?</b> 에스터의 OR 산소가 자기 C=O에 전자를 밀어줘서 C=O가 음전하를 덜 받아들여. 그래서 <y>에스터가 많을수록 산성이 약해</y>.</p>
<div class="boxg"><b>쓸모</b> pKa 9–13이면 <b>NaOEt(짝산 16)</b>로도 완전히 엔올레이트가 돼 → 말론산 에스터·아세토아세트산 에스터 합성에서 LDA 없이 NaOEt를 쓰는 이유(슬 25, 31).</div>"""),

# 18
dict(img=18, slide=18, title="표 22.1 — 유기 화합물의 산도 상수(pKa)", sub="Table 22.1 · Acidity Constants for Some Organic Compounds",
kw=["pKa 표", "작을수록 강한 산", "1,3-다이카르보닐 9–13", "에스터·니트릴 25", "다이아이소프로필아민 36"],
sum="pKa 작을수록 강한 산: 카르복실산 5 < 1,3-다이케톤 9 < 3-케토 에스터 11 < 1,3-다이에스터 13 < 알코올 16 = 산염화물 16 < 알데하이드 17 < 케톤 19 < 싸이오에스터 21 < 에스터 25 = 니트릴 25 < 다이알킬아마이드 30 < 다이알킬아민 36.",
tr="""<table class="t"><tr><th>작용기</th><th>예</th><th>pKa</th></tr>
<tr><td>카르복실산</td><td>CH₃COOH</td><td>5</td></tr>
<tr><td>1,3-다이케톤</td><td>CH₃COCH₂COCH₃</td><td>9</td></tr>
<tr><td>3-케토 에스터</td><td>CH₃COCH₂CO₂CH₃</td><td>11</td></tr>
<tr><td>1,3-다이에스터</td><td>CH₃OCOCH₂CO₂CH₃</td><td>13</td></tr>
<tr><td>알코올</td><td>CH₃OH</td><td>16</td></tr>
<tr><td>산염화물</td><td>CH₃COCl</td><td>16</td></tr>
<tr><td>알데하이드</td><td>CH₃CHO</td><td>17</td></tr>
<tr><td>케톤</td><td>CH₃COCH₃</td><td>19</td></tr>
<tr><td>싸이오에스터</td><td>CH₃COSCH₃</td><td>21</td></tr>
<tr><td>에스터</td><td>CH₃CO₂CH₃</td><td>25</td></tr>
<tr><td>니트릴</td><td>CH₃C≡N</td><td>25</td></tr>
<tr><td>N,N-다이알킬아마이드</td><td>CH₃CON(CH₃)₂</td><td>30</td></tr>
<tr><td>다이알킬아민</td><td>HN(i-C₃H₇)₂</td><td>36</td></tr></table>""",
ex="""<p><b>외우는 요령</b>: “α-H 산성도 = 21장 반응성 순서와 같은 원리”야.</p>
<ul><li>카르보닐에 붙은 기가 <y>전자를 덜 밀어줄수록</y>(산염화물 Cl) C=O가 음전하를 잘 받아 → α-H 산성 ↑</li>
<li>전자를 많이 밀어줄수록(아마이드 N) → α-H 산성 ↓</li></ul>
<p>그래서 단일 카르보닐 α-H: <g>산염화물(16) &gt; 알데하이드(17) &gt; 케톤(19) &gt; 싸이오에스터(21) &gt; 에스터(25) ≈ 니트릴(25) &gt; 아마이드(30)</g> (산 세기 순, 숫자는 pKa).</p>
<p><b>주의할 함정</b></p>
<ul><li>표에서 카르복실산(5)·알코올(16)은 <b>O–H</b>의 pKa, 아민(36)은 <b>N–H</b>의 pKa. 나머지는 모두 <b>α C–H</b>.</li>
<li>알데하이드(17) &gt; 케톤(19): 케톤의 알킬기가 전자를 밀어줘서 음이온을 불안정하게 해.</li></ul>
<div class="box"><span class="tag">산 세기 순서</span>시험 단골! “다음을 산 세기 순서로” → 이 표 값으로 줄 세우기. 연습문제 22-38이 정확히 이 유형이야.</div>""", toph=262),

# 19
dict(img=19, slide=19, title="엔올레이트 이온의 반응성 — O 반응 vs C 반응", sub="Reactivity of Enolate Ions",
kw=["바이닐 알콕사이드", "α-케토 카르보음이온", "양쪽성 친핵체", "C 반응 = α-치환"],
sum="엔올레이트는 C=C–O⁻(바이닐 알콕사이드)로도, ⁻C–C=O(α-케토 카르보음이온)로도 볼 수 있다. 산소에서 반응하면 엔올 유도체, 탄소에서 반응하면 α-치환 카르보닐이 된다.",
tr="""<ul><li>엔올레이트 이온은 <b>바이닐 알콕사이드</b>(C=C–O⁻)로도, <b>α-케토 카르보음이온</b>(⁻C–C=O)으로도 볼 수 있다.
<ul><li>엔올레이트 이온은 친전자체와 반응할 수 있다.</li></ul></li>
<li><b>산소에서 반응</b>하면 엔올 유도체가 생긴다.</li>
<li><b>탄소에서 반응</b>하면 α-치환 카르보닐 화합물이 생긴다.</li></ul>
<p class="note">그림 라벨: Reaction here(여기서 반응) — Vinylic alkoxide → An enol derivative / α-Keto carbanion → An α-substituted carbonyl compound</p>""",
ex="""<p>엔올레이트는 친핵 자리가 <b>두 곳</b>(O와 C)인 <y>양쪽성 친핵체(ambident nucleophile)</y>야.</p>
<table class="t"><tr><th></th><th>O에서 반응</th><th>C에서 반응</th></tr>
<tr><td>공명 구조</td><td>C=C–O⁻</td><td>⁻C–C=O</td></tr>
<tr><td>생성물</td><td>엔올 에터·엔올 에스터 (C=C–O–E)</td><td><g>α-치환 케톤 (E–C–C=O)</g></td></tr>
<tr><td>이 장에서</td><td>거의 안 다룸</td><td><b>주인공</b> (할로젠화, 알킬화)</td></tr></table>
<p><b>왜 대부분 C에서?</b> C–E 결합 + C=O가 남는 생성물이 훨씬 안정해(C=O가 강하니까). 할로젠(Br₂)이나 알킬 할라이드(RX)는 거의 항상 탄소에서 반응해.</p>
<p><b>엔올 vs 엔올레이트</b>: 엔올레이트는 <b>음전하</b>가 있어서 중성인 엔올보다 훨씬 강한 친핵체야. 그래서 알킬 할라이드 같은 약한 친전자체와도 반응(S<sub>N</sub>2)할 수 있어.</p>"""),

# 20
dict(img=20, slide=20, title="엔올레이트의 반응 ① — 염기 촉진 α-할로젠화", sub="Base-promoted α halogenation",
kw=["NaOH, H₂O", "약한 염기로 충분", "엔올레이트 + Br₂", "염기 촉진(촉매 아님)"],
sum="알데하이드·케톤은 염기 존재에서도 α-할로젠화된다. 케톤을 엔올레이트로 완전히 바꿀 필요가 없어서 NaOH 같은 약한 염기로 충분하다.",
tr="""<ul><li>알데하이드와 케톤은 <b>염기 촉진 α 할로젠화</b>를 겪는다.</li>
<li>케톤을 엔올레이트 이온으로 완전히 바꿀 필요가 없기 때문에 <b>약한 염기</b>도 할로젠화에 효과적이다.</li></ul>
<p class="note">그림: 케톤 —NaOH, H₂O→ [엔올레이트] —Br₂→ α-브로모 케톤 + Br⁻</p>""",
ex="""<p><b>메커니즘 2단계</b></p>
<ol><li>OH⁻가 α-H를 떼어 → 엔올레이트 (평형, 아주 조금만 생김)</li>
<li>엔올레이트의 α 탄소가 Br–Br 공격 → <g>α-브로모 케톤 + Br⁻</g></li></ol>
<p><b>약한 염기로 충분한 이유</b>: 엔올레이트가 아주 조금만 있어도 Br₂와 빨리 반응해서 소모되면, 평형이 다시 엔올레이트를 만들어(르샤틀리에). 슬라이드 3의 “엔올 미량” 논리와 같아.</p>
<p><b>“촉매”가 아니라 “촉진(promoted)”</b>: OH⁻가 H⁺와 만나 H₂O가 되면서 <y>소모</y>돼. 산 촉매(슬 9)에서는 HBr이 오히려 더 생겼던 것과 대비.</p>
<div class="box"><span class="tag">산성 vs 염기성 비교</span>
산성: <b>한 번만</b> 할로젠화, 더 치환된 쪽 / 염기성: 할로젠 들어갈수록 <b>더 빨라져서 여러 번</b> 할로젠화, 덜 치환된 쪽(특히 CH₃) → 다음 슬라이드 할로폼 반응.</div>"""),

# 21
dict(img=21, slide=21, title="엔올레이트의 반응 ② — 할로폼 반응", sub="Haloform reaction of methyl ketones",
kw=["메틸 케톤", "3중 할로젠화", "⁻CX₃ 이탈기", "카르복실산염 + CHX₃", "아이오도폼 시험"],
sum="염기·할로젠이 과량이면 메틸 케톤의 CH₃가 CX₃까지 할로젠화된 뒤 OH⁻가 C=O를 공격하고, 할로젠으로 안정화된 ⁻CX₃가 이탈기로 떨어져 카르복실산염 + 할로폼(CHX₃)이 된다.",
tr="""<ul><li>염기 촉진 할로젠화는 (합성에) 잘 쓰이지 않는다.</li>
<li>염기와 할로젠을 과량 쓰면, 메틸 케톤은 <b>세 번 할로젠화</b>된 뒤 <b>할로폼 반응</b>에서 염기에 의해 끊어진다.
<ul><li>할로젠으로 안정화된 카르보음이온이 <b>이탈기</b>로 작용한다.</li></ul></li></ul>
<p class="note">그림: 메틸 케톤(A methyl ketone) R–CO–CH₃ —X₂, NaOH→ [R–CO–CX₃ —OH⁻ 첨가→ 사면체 중간체] → R–COOH + ⁻CX₃ → R–COO⁻ + CHX₃ (X = Cl, Br, I)</p>""",
ex="""<p><b>단계별</b></p>
<ol><li><b>3중 할로젠화</b>: CH₃ → CH₂X → CHX₂ → CX₃. X가 들어갈수록 남은 H가 <y>더 산성</y>이 돼서(X의 전자 끌기) 점점 빨라져. 그래서 중간에 멈출 수 없어.</li>
<li><b>OH⁻ 첨가</b>: R–CO–CX₃의 C=O에 OH⁻ 첨가 → 사면체 중간체 (21장 친핵성 아실 치환처럼!)</li>
<li><b>⁻CX₃ 이탈</b>: 보통 C⁻는 이탈 못 하지만 ⁻CX₃는 할로젠 3개가 음전하를 안정화해서 <g>이탈기 가능</g>.</li>
<li><b>산–염기</b>: R–COOH + ⁻CX₃ → <g>R–COO⁻ + CHX₃</g> (비가역).</li></ol>
<div class="box"><span class="tag">시험 포인트</span><b>아이오도폼 시험</b>: I₂/NaOH에서 노란 침전(CHI₃) → 메틸 케톤(또는 CH₃CH(OH)– 구조) 확인. 생성물은 탄소 하나 줄어든 <b>카르복실산염</b>. 연습문제 22-42 (d)!</div>""", toph=270),

# 22
dict(img=22, slide=22, title="엔올레이트 이온의 알킬화", sub="Alkylation of Enolate Ions",
kw=["엔올레이트 = 친핵체", "알킬 할라이드", "S<sub>N</sub>2", "새 C–C 결합"],
sum="염기로 엔올레이트를 만든 뒤 알킬 할라이드(R–X)와 S<sub>N</sub>2 반응시키면 α 탄소에 알킬기가 붙어 새 C–C 결합이 생긴다.",
tr="""<ul><li>염기 촉진 반응은 <b>엔올레이트 이온 중간체</b>를 거쳐 일어난다.</li></ul>
<p class="note">그림: 카르보닐 화합물(α-H) —염기(Base)→ [엔올레이트 이온(Enolate ion)] —R–X, S<sub>N</sub>2 반응(SN2 reaction)→ α-알킬화 카르보닐 + X⁻</p>""",
ex="""<p>이 장에서 가장 중요한 반응이야. <y>C–C 결합을 새로 만들어</y> 탄소 골격을 키우거든.</p>
<p><b>메커니즘 (2단계)</b></p>
<ol><li><b>엔올레이트 형성</b>: 염기가 α-H 제거 (슬 15–17).</li>
<li><b>S<sub>N</sub>2</b>: 엔올레이트 α 탄소의 전자쌍이 R–X의 탄소를 <b>뒤쪽에서</b> 공격, X⁻ 이탈 → <g>α-R 카르보닐</g>.</li></ol>
<p><b>그림 속 화살표</b>: 엔올레이트 C⁻ → R–X의 C, C–X 결합 전자 → X. 이게 S<sub>N</sub>2 한 단계(동시 진행).</p>
<table class="t"><tr><th>방법</th><th>기질</th><th>염기</th><th>결과</th></tr>
<tr><td>말론산 에스터 합성</td><td>CH₂(CO₂Et)₂</td><td>NaOEt</td><td>RCH₂COOH (슬 24–30)</td></tr>
<tr><td>아세토아세트산 에스터 합성</td><td>CH₃COCH₂CO₂Et</td><td>NaOEt</td><td>RCH₂COCH₃ (슬 31–32)</td></tr>
<tr><td>직접 알킬화</td><td>케톤·에스터·니트릴</td><td>LDA</td><td>α-R 화합물 (슬 34–35)</td></tr></table>
<div class="box"><span class="tag">메커니즘 그리기</span>“염기 + R–X” 조건 = 엔올레이트 형성 → S<sub>N</sub>2. 21장처럼 C=O에 첨가하는 화살표를 그리면 틀려!</div>"""),

# 23
dict(img=23, slide=23, title="엔올레이트 알킬화의 제약 조건", sub="Constraints on Enolate Alkylation",
kw=["S<sub>N</sub>2 규칙 그대로", "이탈기 OTs > I > Br > Cl", "1°·메틸·알릴·벤질", "3°는 E2"],
sum="알킬화는 S<sub>N</sub>2라서 S<sub>N</sub>2 규칙을 그대로 따른다. 이탈기는 토실레이트 > I > Br > Cl, R은 알릴·벤질 > 메틸 > 1°. 2°는 잘 안 되고 3°는 제거 반응만 일어난다.",
tr="""<ul><li><b>S<sub>N</sub>2 반응</b> — 이탈기 X는 염화물, 브로민화물, 아이오딘화물, 토실레이트가 될 수 있다.</li>
<li>R은 <b>1차 또는 메틸</b>이어야 하고, 가급적 <b>알릴 또는 벤질</b>이 좋다.</li>
<li><b>2차</b> 할라이드는 반응이 잘 안 되고, <b>3차</b> 할라이드는 경쟁하는 <b>제거 반응</b> 때문에 전혀 반응하지 않는다.</li></ul>
<p class="note">그림: R–X에서 –X: 토실레이트(Tosylate) &gt; –I &gt; –Br &gt; –Cl / R–: 알릴(Allylic) ≈ 벤질(Benzylic) &gt; H₃C– &gt; RCH₂–</p>""",
ex="""<p>새로운 규칙이 아니라 <y>S<sub>N</sub>2 단원(유기1) 복습</y>이야.</p>
<table class="t"><tr><th>요인</th><th>좋은 쪽</th><th>이유</th></tr>
<tr><td>이탈기 X</td><td>OTs &gt; I &gt; Br &gt; Cl</td><td>약한 염기일수록 잘 떨어짐</td></tr>
<tr><td>R (기질)</td><td>알릴 ≈ 벤질 &gt; CH₃ &gt; 1°</td><td>입체 장애 ↓, 전이상태 π 안정화</td></tr>
<tr><td>2°</td><td>느림·수율 낮음</td><td>입체 장애</td></tr>
<tr><td>3°</td><td><pk>× (E2만)</pk></td><td>엔올레이트가 염기로 작용해 H 떼어냄</td></tr></table>
<p><b>왜 알릴·벤질이 메틸보다 빨라?</b> S<sub>N</sub>2 전이상태의 p 오비탈이 옆 π 결합과 겹쳐 안정화돼.</p>
<p><b>바이닐·아릴 할라이드</b>(C=C–X, Ar–X)도 S<sub>N</sub>2가 안 돼 → 알킬화 불가.</p>
<div class="box"><span class="tag">함정 문제</span>“(CH₃)₃CBr로 말론산 에스터 알킬화” → <b>반응 안 함 / 알켄(아이소뷰틸렌) 생성</b>이 정답. 3°는 무조건 ×.</div>"""),

# 24
dict(img=24, slide=24, title="말론산 에스터 합성 — 개요", sub="Malonic Ester Synthesis",
kw=["R–X → RCH₂COOH", "탄소 2개 연장", "말론산 다이에틸", "카르복실산 합성"],
sum="말론산 에스터 합성은 알킬 할라이드 R–X를 탄소 2개 늘어난 카르복실산 R–CH₂–COOH로 바꾼다.",
tr="""<ul><li>알킬 할라이드로부터 <b>탄소 사슬을 두 개 늘리면서</b> 카르복실산을 만드는 방법.</li></ul>
<p class="note">그림: R–X —말론산 에스터 합성(Malonic ester synthesis)→ R–CH₂–CO₂H</p>""",
ex="""<p><b>탄소 계산</b>: R에 붙는 건 말론산 에스터의 <b>CH₂ + COOH</b> 두 탄소. 나머지 CO₂Et 하나는 마지막에 CO₂로 날아가(탈카르복실화).</p>
<div class="boxg"><b>전체 흐름</b> ① NaOEt로 엔올레이트 (슬 25) → ② R–X로 알킬화 (슬 25) → (③ 한 번 더 알킬화 가능, 슬 26) → ④ H₃O⁺, 가열: 가수분해 + 탈카르복실화 (슬 27–28)</div>
<p><b>역합성으로 생각하기</b> (시험 풀이 요령)</p>
<ol><li>목표 카르복실산에서 <y>α 탄소</y>를 찾는다 (COOH 바로 옆).</li>
<li>α 탄소에 붙은 알킬기(H 아닌 것)를 떼어낸다 → 그게 R–X에서 온 것.</li>
<li>α 탄소 + COOH = 말론산 에스터에서 온 부분.</li></ol>
<p>예: 헥산산 CH₃CH₂CH₂CH₂–CH₂–COOH → α 탄소에 붙은 건 뷰틸 → <g>1-브로모뷰테인 + 말론산 에스터</g> (슬 29).</p>
<div class="box"><span class="tag">시험 포인트</span>“다음 카르복실산을 말론산 에스터 합성으로 만들 때 필요한 알킬 할라이드는?” 단골. α 탄소에 치환기가 2개면 알킬화 2번.</div>"""),
]
