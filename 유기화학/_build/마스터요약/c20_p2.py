# -*- coding: utf-8 -*-
from parts import *
from textbook import T2

P = P2
KS = 'C[C:3](C)([H:4])[C:1](=[O:2])C'
DIK = mrow(panel('CC(=O)[CH:3]([H:4])[C:1](=[O:2])C.[*:5]', [(5,4,0.5),((3,4),(1,3),0.8),((1,2),2,-1.0)], w=190, h=140, ori={0:(1,2,90)}, pos=[(4,5,1.3,-0.6)], labels={5:'B<sup>-</sup>'}, note='① 가운데 α-H 제거 (pKa 9)'),
           step(),
           panel('C[C:9](=[O:8])[CH:3]=[C:1]([O-:2])C', [(2,(1,2),0.8),((1,3),3,0.8)], w=150, h=130, ori={0:(1,2,90)}, note='O⁻ (오른쪽)'),
           step('', '공명', rev=True),
           panel('C[C:9](=[O:8])[CH-:3][C:1](=[O:2])C', [(3,(3,9),0.8),((9,8),8,0.9)], w=150, h=130, ori={0:(1,2,90)}, note='C⁻ (가운데)'),
           step('', '공명', rev=True),
           panel('C[C:9]([O-:8])=[CH:3][C:1](=[O:2])C', w=150, h=130, ori={0:(1,2,90)}, note='O⁻ (왼쪽)'), label='3곳 분산')

E = [
# ── 개념 08
dict(t="c", id="c-acid", part=P, title="α-H의 산성도와 엔올레이트 — 강염기 NaH · LDA", sub="Enolate ion formation · LDA · 슬라이드 15–16",
core="케톤 α-H pKa ≈ 19 → NaOH/NaOEt(짝산 16)로는 일부만. <b>완전히</b> 엔올레이트로 만들려면 <b>NaH(35) · LDA(36)</b>.",
detail="""<ul><li>α-H가 빠지면 α 탄소 sp³ → <y>sp²</y>(평면), p 오비탈이 C=O π와 겹쳐 음전하가 O까지 퍼짐(공명).</li>
<li>평형은 <b>약한 산(pKa 큰 쪽)</b>으로 기운다 → 염기의 짝산 pKa ≫ α-H pKa여야 완전 전환.</li></ul>
<table class="t"><tr><th>염기</th><th>짝산 pKa</th><th>케톤(19) 완전 전환?</th></tr>
<tr><td>NaOH / NaOEt</td><td>15.7 / 16</td><td>✗ 약 0.1 %만</td></tr>
<tr><td>NaH</td><td>35 (H₂ 기체로 날아감)</td><td>○</td></tr>
<tr><td><b>LDA</b></td><td><b>36</b></td><td><g>○ 빠르고 완전</g></td></tr></table>
<p><b>LDA</b> = 다이아이소프로필아민 + BuLi(뷰테인 날림). ① 강함(36) ② <b>부피 큼</b> → C=O 공격 못 하고 H만 뗌 ③ −78 °C, THF에서 작동, <y>덜 붐비는 쪽</y> α-H를 빠르게(속도론적). 이온성이지만 헥세인 같은 유기 용매에도 녹음.</p>""",
side=[("img", "s-16", "슬라이드 16 — BuLi + 다이아이소프로필아민 → LDA"),
      ("rec", "“아무 베이스나 쓰면 안 되고 <b>강한 베이스</b>를 써야. 엔올레이트를 99% 이상 만들려면 NaH나 LDA.” “LDA는 벌키해서 스테릭 힌드런스로 특정 사이트를 찾아간다.” 알코올 16 vs 케톤 19 → 약 1000배."),
      ("my", "<b>Q.</b> 왜 BuLi를 그냥 안 쓰고 LDA를? → BuLi는 날렵해서 α-H 대신 C=O 탄소를 직접 공격(친핵성 첨가)해 버림. 그래서 날개 두 개 달린 뚱보 LDA!")],
mech=MSR(16, 0, 1),
one="엔올레이트 100 % = 짝산 pKa가 훨씬 큰 강염기(NaH·LDA). LDA = 강하고 뚱뚱해서 H만!"),

# ── 개념 09
dict(t="c", id="c-pka", part=P, title="1,3-다이카르보닐과 pKa 표 22.1 — 산 세기 순서의 모든 것", sub="Acidity constants · 슬라이드 17–18",
core="두 C=O 사이 H는 음전하가 <b>3곳</b>(O·C·O)에 퍼져 pKa 9–13 → <b>NaOEt로도 완전 전환</b>. 단일 카르보닐은 옆 기가 전자를 밀수록 산성 ↓.",
detail="""<table class="t"><tr><th>α-H (또는 표시한 H)</th><th>pKa</th><th>α-H</th><th>pKa</th></tr>
<tr><td>카복실산 O–H</td><td>5</td><td>알데하이드</td><td>17</td></tr>
<tr><td><b>1,3-다이케톤</b></td><td><b>9</b></td><td>케톤</td><td>19</td></tr>
<tr><td>3-케토 에스터</td><td>11</td><td>싸이오에스터</td><td>21</td></tr>
<tr><td>1,3-다이에스터(말론산)</td><td>13</td><td>에스터 · 니트릴</td><td>25</td></tr>
<tr><td>알코올 O–H</td><td>16</td><td>N,N-다이알킬아마이드</td><td>30</td></tr>
<tr><td>산염화물</td><td>16</td><td>다이알킬아민 N–H</td><td>36</td></tr></table>
<ul><li><b>다이케톤 &gt; 케토에스터 &gt; 다이에스터</b>: 에스터의 OR이 자기 C=O에 전자를 밀어 넣어 음전하를 덜 받아줌.</li>
<li><b>케톤(19) vs 니트릴(25)</b>: 케톤 엔올레이트는 음전하를 <b>O⁻</b>가, 니트릴은 덜 전기음성인 <b>N⁻</b>가 받고, C=C=N⁻는 뻣뻣한 누적 이중결합 → 케톤이 10⁶배 산성.</li>
<li>함정: 카복실산·알코올·아민 값은 O–H·N–H. 나머지는 α C–H.</li></ul>""",
side=[("img", "s-18", "슬라이드 18 — 표 22.1", 180),
      ("my", "<b>산성도 만능 공식</b>: 옆에서 전자를 밀어주는 방해꾼(N ＞ O ＞ CH₃)이 없을수록 → 카르보닐의 전자 끌기 ↑ → α-H가 쉽게 떨어짐 → 작은 pKa!"),
      ("rec", "“페놀 pKa 10, 아세트산 4.75 … 양쪽에 케톤이 있는 α 위치는 pKa 9 정도. 레저넌스가 3개 존재하면서 안정화.”")],
mech=DIK,
one="다이케톤 9 · 케토에스터 11 · 말론산 에스터 13 · 알코올 16 · 케톤 19 · 에스터 25 · LDA 36!"),

# ── 개념 10
dict(t="c", id="c-haloform", part=P, title="엔올레이트의 반응성 · 염기 할로젠화 · 할로폼 반응", sub="Enolate reactivity · base-promoted halogenation · haloform · 슬라이드 19–21",
core="엔올레이트는 O·C 양쪽 친핵체지만 <b>C에서 반응</b>(C=O 복구). 염기 할로젠화는 할로젠이 들어갈수록 <b>빨라져</b> 멈추지 않음 → 메틸 케톤은 <b>할로폼</b>.",
detail="""<ul><li><b>C vs O</b>: C에 E가 붙으면 강한 C=O가 남아 생성물이 훨씬 안정 → α-치환.</li>
<li><b>염기 촉진</b>: OH⁻가 α-H 제거 → 엔올레이트 + Br₂. OH⁻는 소모 → “촉매” 아니라 “촉진”. 약한 염기로 충분(조금만 생겨도 Br₂와 바로 반응).</li>
<li><b>폭주</b>: 들어간 X가 남은 H의 산성을 높임 → CH₃ → CX₃까지.</li>
<li><b>할로폼</b>: R–CO–CX₃ + OH⁻ → 사면체 → <y>⁻CX₃ 이탈</y>(X 3개가 음전하 안정화) → 산–염기 → <g>R–COO⁻ + CHX₃</g> (탄소 1개 줄어든 산).</li>
<li><b>아이오도폼 시험</b>: I₂/NaOH → 노란 침전 CHI₃ → 메틸 케톤 확인.</li></ul>
<table class="t"><tr><th></th><th>산성 (Br₂/AcOH)</th><th>염기성 (Br₂/NaOH)</th></tr>
<tr><td>경로</td><td>엔올</td><td>엔올레이트</td></tr><tr><td>횟수</td><td><b>1번</b></td><td><b>여러 번</b>(폭주)</td></tr>
<tr><td>산·염기</td><td>촉매 (HBr 재생)</td><td>촉진 (OH⁻ 소모)</td></tr></table>""",
side=[("img", "s-21", "슬라이드 21 — 할로폼 반응"),
      ("my", "<b>Q.</b> 왜 염기 조건은 1번에서 안 멈추나? → 첫 X의 전자 끌기로 같은 탄소의 남은 H가 훨씬 산성 → OH⁻가 그 탄소만 빛의 속도로 마저 뽑아 –CX₃까지!"),
      ("tip", "연습문제 22-42 (d) 아세토페논 + NaOH, I₂ → 벤조산염 + CHI₃. ⁻CX₃가 떨어지는 화살표를 꼭 그려 보기.")],
mech=MS(21),
one="산성은 한 번, 염기성은 끝까지. CX₃가 되면 OH⁻가 C=O 치고 ⁻CX₃ 쫓아냄 → 산염 + 할로폼!"),

# ── 문제 08 — 과제 22-37
dict(t="q", part=P, kind=["sa"], src="과제 22-37 (강의자료 마지막 슬라이드)", title="산성 수소(pKa < 25) 모두 찾기",
q="""다음 분자에서 pKa &lt; 25인 산성 수소를 <b>모두</b> 표시하시오.
<div class="molrow">""" + C('CCC(C)C(C)=O', '(a)', 110, 70) + C('O=C1CCC(=O)C1', '(b)', 90, 70) + C('OCCC(=O)C#CC', '(c)', 130, 70) + "</div><div class='molrow'>" + C('COC(=O)c1ccccc1CC#N', '(d)', 120, 90) + C('ClC(=O)C1CCCC1', '(e)', 100, 70) + C('CCC(=O)C(C)=C', '(f)', 110, 70) + "</div>",
a="(a) CH 1 + CH₃ 3 · (b) 고리 H 6개 (C2 가장) · (c) O–H + α-CH₂ + <b>알킨 끝 CH₃</b> · (d) CH₂CN 2 · (e) α-H 1 · (f) 에틸 CH₂ 2",
steps=[("카르보닐·니트릴 바로 옆 sp³ C–H + O–H를 체크.", "고리 H·바이닐 H·OCH₃는 항상 ✗."),
       ("(b) C2(두 C=O 사이, pKa ≈ 9) + C4·C5(각 C=O의 α, ≈ 19) → 6개.", ""),
       ("(c) <b>함정</b>: C≡C 건너 CH₃도 산성 — H가 빠지면 ⁻CH₂–C≡C–C=O ↔ CH₂=C=C=C–O⁻로 음전하가 산소까지.", "π로 이어지면 멀어도 산성."),
       ("(f) C(CH₃)=CH₂ 쪽 α 탄소는 sp²라 H 없음.", "해설집도 CH₂만 표시.")],
afig='<img src="../강의번역/img/a37.jpg" style="width:100%">',
one="α-H + O–H + ‘C=O와 π로 이어진 끝의 C–H’. 바이닐·고리·OCH₃는 ✗."),

# ── 문제 09 — 과제 22-38 + 22.8
dict(t="q", part=P, kind=["ord", "draw"], src="과제 22-38 (강의자료 마지막 슬라이드)", title="산성도 증가 순서 — 알코올 vs 케톤 함정",
q="""(1) 산성도가 <b>증가하는</b> 순서로 배열하시오: (a) CH₃CH₂CO₂H (b) CH₃CH₂OH (c) (CH₃CH₂)₂NH (d) CH₃COCH₃ (e) CH₃COCH₂COCH₃ (f) CCl₃CO₂H<br>(2) 에탄올과 아세톤 중 더 강한 산은? 이유는?""",
a="(1) c &lt; d &lt; b &lt; e &lt; a &lt; f · (2) 에탄올(16) — 알콕사이드는 음전하가 전부 O에",
steps=[("pKa: 아민 36 · 케톤 19 · 알코올 16 · 다이케톤 9 · 프로판산 4.8 · 트라이클로로아세트산 0.7.", "큰 pKa → 작은 pKa 순서가 ‘증가’."),
       ("<b>함정 1</b>: 에탄올(16) &gt; 아세톤(19) 산성 — 알콕사이드는 음전하가 100 % O.", ""),
       ("<b>함정 2</b>: 같은 카복실산끼리는 Cl 3개 유발 효과 → (f) 최강.", ""),
],
afig='<img src="../강의번역/img/a38.jpg" style="width:100%;margin-top:4px">',
one="아민 36 < 케톤 19 < 알코올 16 < 다이케톤 9 < 카복실산 5 < CCl₃COOH 0.7."),

# ── 문제 11 — 변형: 염기 고르기
dict(t="q", part=P, kind=["ord", "reag"], src="예상 변형 (반응성 사다리)", title="염기 고르기 — 어느 염기가 완전히 엔올레이트를?",
q="""(1) 다음 염기를 염기성이 <b>증가</b>하는 순서로: NaOH, NaOEt, LDA, NaH, CH₃COONa<br>
(2) 각 기질을 <b>완전히</b> 엔올레이트로 바꾸는 데 쓸 수 있는 염기를 위에서 모두 고르시오.<br>
&nbsp;(가) 말론산 다이에틸(13) (나) 사이클로헥사논(19) (다) 아세트산 에틸(25)<br>
(3) (다)에 NaOEt를 쓰면 생기는 문제는?""",
a="(1) CH₃COONa &lt; NaOH ≈ NaOEt &lt; NaH &lt; LDA · (2)(가) NaOH·NaOEt·NaH·LDA (실제론 NaOEt) (나) NaH·LDA (다) LDA (NaH) · (3) 엔올레이트가 조금만 생겨 남은 에스터와 축합(Claisen)",
steps=[("짝산 pKa: 아세트산 5 · 물 15.7 · 에탄올 16 · H₂ 35 · 다이아이소프로필아민 36.", "짝산 pKa가 클수록 강한 염기."),
       ("완전 전환 조건: 짝산 pKa ≫ 기질 pKa.", "(가) 13 &lt; 16 → NaOEt 충분. 에스터라 NaOH는 가수분해 위험 → <b>같은 알콕사이드 NaOEt</b>."),
       ("(나) 19 &gt; 16 → NaOEt ✗, NaH·LDA ○.", ""),
       ("(다) 25 → LDA. NaOEt면 조금 생긴 엔올레이트가 남은 에스터 C=O를 공격(23장 Claisen).", "")],
one="염기는 짝산 pKa로 줄 세운다: 아세트산염 < OH⁻·EtO⁻ < H⁻ < LDA."),
]
E[3:3] = T2
