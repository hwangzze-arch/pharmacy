from parts import *
P = P2
E = [
dict(t="c", id="c-coupling", part=P, title="화학삼투의 증거와 ‘짝지음’ — 하나가 멈추면 둘 다 멈춘다", sub="Chemiosmosis evidence · Coupling of electron transfer and ATP synthesis · Slides 44–47",
core="전자전달과 ATP 합성은 <b>짝지어져(coupled)</b> 있다: 전자전달을 막으면 ATP 합성이 멈추고, ATP 합성을 막으면 전자전달(O<sub>2</sub> 소비)도 멈춘다. 둘을 잇는 끈 = H<sup>+</sup> 기울기.",
detail="""<p><b>증거 ① 인공 양성자 기울기 실험</b>(슬라이드 46): 미토콘드리아를 pH 9 용액에 담가 두었다가 갑자기 pH 7로 옮기고 <b>valinomycin(발리노마이신)</b>을 넣음(K<sup>+</sup> 없음).</p>
<ul><li>바깥이 산성 → 인공 ΔpH 생김 / 발리노마이신이 K<sup>+</sup>를 밖으로 내보냄 → 안쪽이 (−) → 인공 Δψ 생김</li>
<li>→ <b>전자전달 없이도 ATP가 합성됨</b> → <pk>양성자 구동력만으로 ATP 합성이 충분하다</pk>!</li></ul>
<p><b>증거 ② 짝지음 실험</b>(슬라이드 47, O<sub>2</sub> 소비 & ATP 합성 그래프)</p>
<ul><li>ADP + P<sub>i</sub>만 넣음 → 거의 변화 없음. <b>숙신산(기질)</b> 추가 → O<sub>2</sub> 소비 ↑ + ATP 합성 ↑</li>
<li><b>CN<sup>−</sup></b>(전자전달 억제) 추가 → 둘 다 멈춤</li>
<li><b>venturicidin(벤투리시딘)·oligomycin(올리고마이신)</b>(ATP 합성효소 억제) 추가 → ATP 합성 멈춤 → <y>O<sub>2</sub> 소비도 멈춤</y> (H<sup>+</sup>가 못 돌아오니 기울기가 꽉 차서 펌프가 더 못 밀어냄)</li>
<li>그 상태에서 <b>DNP(짝풀림제)</b> 추가 → <b>O<sub>2</sub> 소비만 다시 시작</b>, ATP는 여전히 0 = <b>Uncoupled(짝풀림)</b></li></ul>
<div class="term">＊[용어: 짝지음(coupling) = 두 반응이 톱니바퀴처럼 물려 있어 한쪽이 돌아야 다른 쪽도 도는 상태]</div>""",
side=[("img", 47, "원본 슬라이드 47 — 기질·CN⁻·올리고마이신·DNP를 넣었을 때 O₂ 소비(검정)와 ATP 합성(빨강)", 175),
      ("img", 46, "원본 슬라이드 46 — 인공 pH 기울기 + K⁺ 유출만으로 ATP 합성", 150),
      ("ana", "<b>자전거 체인</b>: 페달(전자전달)과 뒷바퀴(ATP 합성)가 체인(H<sup>+</sup> 기울기)으로 연결. 뒷바퀴를 잡으면(올리고마이신) 페달도 안 돌아가. 체인을 끊으면(DNP) 페달은 헛돌고 바퀴는 멈춘다.")],
one="전자전달 막기 → ATP도 멈춤, ATP 합성 막기 → O₂ 소비도 멈춤. DNP = 체인 끊기: O₂는 소비, ATP는 0."),

dict(t="c", id="c-uncoupler", part=P, title="짝풀림제와 이온운반체 — 댐에 구멍을 뚫는 분자들", sub="Chemical uncouplers (DNP, FCCP) · Ionophores · Slide 48",
core="<b>짝풀림제(uncoupler)</b>는 H<sup>+</sup>를 ATP 합성효소를 거치지 않고 막을 건너 기질로 되돌려 보낸다 → 전자전달·O<sub>2</sub> 소비는 계속(오히려 ↑), ATP는 못 만들고 에너지는 <b>열</b>로 사라진다.",
detail="""<ul><li><b>DNP</b>(2,4-DiNitroPhenol, 2,4-다이나이트로페놀), <b>FCCP</b>(Carbonylcyanide-p-trifluoromethoxyphenylhydrazone, 카보닐사이아나이드-p-트라이플루오로메톡시페닐하이드라존)</li>
<li>공통점 = <y>소수성(기름에 녹는) 약산</y>: 막을 자유롭게 확산. P쪽(산성)에서 H<sup>+</sup>를 붙잡아 중성 형태로 막을 통과 → N쪽(알칼리)에서 H<sup>+</sup>를 내놓음 → 다시 음이온으로 돌아감 → 반복.</li>
<li><b>Ionophore (아이오노포어, 이온운반체)</b>: 이온을 막 너머로 실어 나르는 분자. 예: <b>valinomycin</b> = <b>K<sup>+</sup></b> 운반체 → Δψ(전하 차)를 없앰.</li>
<li>결과: H<sup>+</sup> 기울기가 계속 무너지니 호흡사슬은 기울기를 다시 만들려고 <b>더 빨리</b> 돌아감 → O<sub>2</sub> 소비 ↑, NADH 산화 ↑, <b>P/O 비 ↓(0에 가까움)</b>, 체온 ↑ · 땀.</li>
<li>생체 속 천연 짝풀림 단백질 = <b>thermogenin (써모제닌, UCP1)</b> → 갈색지방 열 생산 ({REF:c-thermo}).</li></ul>
<div class="term">＊[용어: 약산 = H<sup>+</sup>를 붙였다 뗐다 할 수 있는 분자. 산성 쪽에선 H<sup>+</sup>를 붙잡고, 알칼리 쪽에선 놓는다]</div>""",
side=[("img", 48, "원본 슬라이드 48 — DNP와 FCCP: 소수성 약산, 막을 자유 확산", 175),
      ("ana", "<b>댐 옆에 몰래 판 구멍</b>. 물(H<sup>+</sup>)이 물레방아(ATP 합성효소)를 안 거치고 새어 나가니 전기(ATP)는 없고, 펌프(호흡사슬)는 물을 채우려 쉬지 않고 돌다가 <b>열만 펄펄</b>."),
      ("trap", "DNP를 넣으면 O<sub>2</sub> 소비가 <b>줄어든다</b> ❌ → <b>늘어난다</b>. 줄어드는 건 ATP 합성과 P/O 비. 옛날 다이어트약 → 고열로 사망 사고.")],
one="짝풀림제 = 기름에 녹는 약산 H⁺ 셔틀(DNP·FCCP). O₂ 소비 ↑, ATP ↓, 열 ↑, P/O ↓."),

dict(t="c", id="c-synthase", part=P, title="ATP 합성효소의 구조 — 막 속 터빈(F₀) + 바깥 발전기(F₁)", sub="Structure of ATP synthase (F₀F₁) · Slides 50, 54",
core="ATP 합성효소 = <b>F<sub>o</sub></b>(막에 박힌 <b>양성자 통로</b>, 올리고마이신 감수성) + <b>F<sub>1</sub></b>(기질 쪽으로 튀어나온 <b>ATP 합성·가수분해</b> 부위). H<sup>+</sup>가 F<sub>o</sub>를 지나며 <b>c 고리와 γ축을 돌린다</b>.",
detail="""<table class="t"><tr><th>부분</th><th>소단위체 구성</th><th>역할</th></tr>
<tr><td><b>F<sub>1</sub></b> (기질 쪽, N side)</td><td><b>α<sub>3</sub>β<sub>3</sub>γδε</b></td><td>β에 촉매 자리 3개 → ATP 합성(&amp; 분리하면 가수분해). <b>γ = 가운데 회전축(central shaft)</b></td></tr>
<tr><td><b>F<sub>o</sub></b> (막 속)</td><td><b>a b<sub>2</sub> c<sub>8–15</sub></b></td><td>c 소단위체들이 둥근 <b>c 고리</b>, a는 고정된 반통로, b<sub>2</sub>는 F<sub>1</sub>을 붙잡는 <b>고정자(stator) 팔</b></td></tr></table>
<ul><li>F<sub>o</sub>의 ‘o’ = <b>oligomycin(올리고마이신)</b> 감수성의 o (숫자 0 아님!).</li>
<li><b>회전자(rotor)</b> = c 고리 + γ + ε (함께 돈다) / <b>고정자(stator)</b> = a + b<sub>2</sub> + δ + α<sub>3</sub>β<sub>3</sub> (가만히 있음).</li>
<li>c 고리의 c 소단위체 수: 소 8개, 효모 10개, 시금치 엽록체 14개, 호열성 세균 10개 → 종마다 다름(슬라이드 57).</li>
<li>H<sup>+</sup> 경로: P쪽에서 a의 <b>반통로(half-channel)</b> → c 소단위체의 <b>Asp</b> 잔기에 결합 → 고리가 한 바퀴 돌아 → a의 N쪽 반통로로 방출. a의 <b>Arg<sup>210</sup></b>가 H<sup>+</sup>를 밀어냄.</li></ul>
<div class="term">＊[용어: 감수성(sensitive) = 그 약에 의해 기능이 꺼지는 성질. 올리고마이신은 F<sub>o</sub>의 양성자 통로를 막는다]</div>""",
side=[("img", 50, "원본 슬라이드 50 — F₁(α₃β₃γδε)과 F₀(a b₂ c₁₀), 올리고마이신 감수성", 200),
      ("ana", "<b>수력 발전소</b>: F<sub>o</sub> = 물(H<sup>+</sup>)이 지나가며 도는 <b>터빈</b>, γ = 터빈과 연결된 <b>회전축</b>, F<sub>1</sub>의 α<sub>3</sub>β<sub>3</sub> = 축이 돌 때 모양이 바뀌며 전기(ATP)를 만드는 <b>발전기</b>, b<sub>2</sub> = 발전기가 같이 돌지 않게 붙잡는 <b>버팀대</b>."),
      ("tip", "“F<sub>o</sub> = 양성자 통로·올리고마이신 / F<sub>1</sub> = ATP 합성·가수분해” 짝짓기 + <b>α<sub>3</sub>β<sub>3</sub>γδε / ab<sub>2</sub>c<sub>n</sub></b> 구성.")],
one="F₀(ab₂cₙ) = 막 속 H⁺ 터빈(올리고마이신), F₁(α₃β₃γδε) = 바깥 발전기. γ축이 돌며 β를 비튼다."),

dict(t="c", id="c-f1cat", part=P, title="F₁ 표면의 비밀 — 에너지는 ATP를 ‘만들 때’가 아니라 ‘떼어낼 때’ 든다", sub="Catalytic mechanism of F₁ · ATP stabilized relative to ADP on F₁ · Slides 51–53",
core="F<sub>1</sub> 표면에서는 ADP + P<sub>i</sub> ⇌ ATP가 거의 <b>공짜</b>(ΔG′° ≈ 0)로 일어난다. 대신 ATP가 효소에 너무 꽉 붙어서, <b>ATP를 떼어내는 데</b> 양성자 구동력 에너지가 쓰인다.",
detail="""<ul><li>용액 속: ATP + H<sub>2</sub>O → ADP + P<sub>i</sub>, ΔG′° = <b>−30.5 kJ/mol</b> (ATP 만들기 = 큰 오르막)</li>
<li>F<sub>1</sub> 표면: Enz-ATP ⇌ Enz-(ADP + P<sub>i</sub>), <b>K′<sub>eq</sub> ≈ 2.4 → ΔG′° ≈ 0</b> → 쉽게 왔다 갔다(가역).</li>
<li><b>동위원소 교환 실험</b>: <sup>18</sup>O로 표시한 물을 넣으면 효소 위 ATP의 P<sub>i</sub>에 <sup>18</sup>O가 최대 <b>4개</b>까지 들어감 → 효소 위에서 ATP가 몇 번이고 만들어졌다 깨졌다 반복한다는 증거.</li>
<li>왜 ATP 쪽으로 기울까? F<sub>o</sub>F<sub>1</sub>은 <b>ATP를 매우 강하게(K<sub>d</sub> ≤ 10<sup>−12</sup> M)</b>, ADP는 약하게(K<sub>d</sub> ≈ 10<sup>−5</sup> M) 잡는다 → 결합 에너지 차이(약 40 kJ/mol)가 ATP를 안정화 → <g>평형을 ATP 쪽으로 끌어당김</g>.</li>
<li>반응 좌표 그래프(슬라이드 53): 보통 효소는 ES → 전이상태 언덕이 가장 높지만, ATP 합성효소는 <pk>ATP가 효소에서 빠져나가는 마지막 언덕</pk>이 가장 높다 → 그 에너지를 <b>양성자 흐름</b>이 공급.</li></ul>
<div class="term">＊[용어: K<sub>d</sub>(해리상수) = 절반이 떨어져 나가는 농도. 작을수록 꽉 붙어 있다. 10<sup>−12</sup>은 ‘초강력 접착제’ 수준]</div>
<div class="term">＊[용어: K′<sub>eq</sub>(평형상수) ≈ 1이면 양쪽이 비슷 → ΔG′° = −RT ln K′<sub>eq</sub> ≈ 0]</div>""",
side=[("img", 53, "원본 슬라이드 53 — 보통 효소 vs ATP 합성효소의 반응 좌표 (ATP 방출에 에너지 필요)", 165),
      ("ana", "<b>자석 퍼즐판</b>: 판(F<sub>1</sub>) 위에선 ADP와 P<sub>i</sub> 조각이 저절로 딱 붙어 ATP가 돼. 문제는 판이 ATP를 <b>너무 세게 끌어당겨서</b> 떼어내기가 힘들다는 것 — 그 ‘떼는 힘’을 양성자 흐름이 준다."),
      ("tip", "<span class=\"tag s\">슬라이드 Q</span> “에너지는 ATP 합성에 필요한가, ATP 방출에 필요한가?” → <b>방출(release)</b>!")],
one="F₁ 위에서 ATP 만들기 = 공짜(K′eq 2.4, ΔG≈0). 비싼 건 꽉 붙은 ATP(Kd 10⁻¹²)를 떼어내는 것 → 양성자가 지불."),

dict(t="c", id="c-rotation", part=P, title="회전 촉매 — γ축이 돌 때마다 β가 ‘빈 → 느슨 → 꽉’으로 바뀐다", sub="Binding-change model (결합 변화 모델, Boyer) · Rotational catalysis · Slides 55–57",
core="세 β 소단위체는 늘 서로 다른 모양: <b>β-ATP(꽉)</b>, <b>β-ADP(느슨)</b>, <b>β-empty(빈)</b>. γ가 120°씩 돌 때마다 모양이 차례로 바뀌어 ATP가 풀려나고, ADP + P<sub>i</sub>가 들어오고, ATP가 만들어진다.",
detail="""<ul><li>Paul Boyer (폴 보이어)의 <b>binding-change model (바인딩 체인지 모델, 결합 변화 모델)</b>, 1997 노벨상.</li>
<li>γ축은 비대칭 → 한 번에 β 하나에만 닿음. <b>γ와 닿은 β는 ‘빈(empty)’ 모양</b>이 된다(슬라이드 55 “γ associated β-empty”).</li>
<li>γ 회전 → <b>β-empty</b>가 됨 → <b>ATP 방출</b> → <b>ADP + P<sub>i</sub> 결합</b>(느슨) → 다음 회전에 <b>ATP 형성</b>(꽉) → 반복</li>
<li>γ 1회전(360°) = 120° × 3 → <g>ATP 3개</g>. 회전 1번에 필요한 H<sup>+</sup> = c 소단위체 수(소 c<sub>8</sub> → 8 H<sup>+</sup> / 3 ATP).</li>
<li><b>회전의 직접 증거</b>(슬라이드 56, Yoshida·Kinosita): F<sub>1</sub>의 β에 His 꼬리를 달아 Ni 판에 거꾸로 고정, γ(또는 c)에 비오틴-아비딘으로 <b>형광 액틴 필라멘트</b>를 붙임 → ATP를 넣으니 필라멘트가 <b>한 방향으로</b> 빙글빙글(ATP 가수분해 방향) → 현미경으로 관찰!</li></ul>
<div class="term">＊[용어: 아비딘-비오틴 = 세상에서 가장 강한 비공유 결합 짝. 실험에서 ‘초강력 찍찍이’로 씀]</div>""",
side=[("img", 55, "원본 슬라이드 55 — γ 회전 → β-empty → ATP 방출 → ADP 결합 → ATP 형성", 190),
      ("img", 56, "원본 슬라이드 56 — 형광 액틴 필라멘트가 한 방향으로 회전", 120),
      ("ana", "<b>회전문 3칸짜리 공장 출입구</b>: 한 칸은 비어서 완제품(ATP)을 내보내고, 한 칸은 재료(ADP + P<sub>i</sub>)를 느슨히 받고, 한 칸은 꽉 눌러 조립 중. 문(γ)이 120° 돌 때마다 역할이 바뀐다.")],
one="β 세 개 = 빈·느슨·꽉, γ가 120° 돌 때마다 교대. 한 바퀴 = ATP 3개. 액틴 필라멘트가 돌아가는 걸 눈으로 봤다!"),

dict(t="c", id="c-po", part=P, title="P/O 비와 수송 비용 — NADH 하나에 ATP 2.5개인 이유", sub="Nonintegral stoichiometry · ANT · Phosphate translocase · MPC · Slides 58–60",
core="NADH 1개 → H<sup>+</sup> 10개, ATP 1개 = H<sup>+</sup> 4개(합성 3 + 수송 1) → <b>P/O = 10/4 = 2.5</b>, 숙신산 → 6/4 = <b>1.5</b>. 화학삼투에서는 <b>정수가 아니어도 된다</b>.",
detail="""<p><b>P/O ratio (P/O 비)</b> = O 원자 1개(½O<sub>2</sub>, 전자 2개)가 환원될 때 만들어지는 ATP 수.</p>
<p><span class="fx">x ADP + x P<sub>i</sub> + ½O<sub>2</sub> + H<sup>+</sup> + NADH → x ATP + H<sub>2</sub>O + NAD<sup>+</sup></span></p>
<ul><li>예전에는 화학반응처럼 정수(NADH 3, FADH<sub>2</sub> 2)라고 믿었지만, 화학삼투 모델에선 H<sup>+</sup>라는 ‘중간 화폐’를 거치므로 <y>P/O가 정수일 필요가 없다</y>(아직 문헌엔 3/2도 흔함).</li>
<li>측정: 전자쌍당 H<sup>+</sup> <b>10개(NADH)</b>, <b>6개(숙신산)</b> / ATP 1개당 H<sup>+</sup> <b>4개</b>.</li></ul>
<p><b>왜 ATP 1개 = H<sup>+</sup> 4개? → 수송비 1개 포함</b> (슬라이드 60)</p>
<ul><li><b>ANT</b>(Adenine Nucleotide Translocase, 아데닌 뉴클레오타이드 전위효소) = <b>역수송체(antiporter)</b>: ATP<sup>4−</sup>를 내보내고 ADP<sup>3−</sup>를 들임 → 바깥으로 (−)전하 1개가 나가는 셈 → <b>Δψ를 소비</b>. 억제제 <b>atractyloside(아트락틸로사이드)</b>.</li>
<li><b>Phosphate translocase(인산 전위효소)</b> = <b>공동수송체(symporter)</b>: H<sub>2</sub>PO<sub>4</sub><sup>−</sup>와 <b>H<sup>+</sup></b>를 함께 기질로 → <b>ΔpH를 소비</b>.</li>
<li>합쳐서 ATP 1개를 밖으로 내보내는 데 H<sup>+</sup> ≈ 1개 값. (합성 자체는 c<sub>8</sub>일 때 8H<sup>+</sup>/3ATP ≈ 2.7개)</li>
<li><b>MPC</b>(Mitochondrial Pyruvate Carrier, 미토콘드리아 피루브산 운반체): 세포질 피루브산을 기질로 들임(슬라이드 59).</li></ul>""",
side=[("img", 60, "원본 슬라이드 60 — ANT(ATP⁴⁻/ADP³⁻ 역수송) + 인산 전위효소(H₂PO₄⁻ + H⁺ 공동수송)", 175),
      ("ana", "<b>환전소</b>: NADH 1장 = 양성자 코인 10개. ATP 한 개 값은 코인 3개 + <b>배송비 1개</b> = 4개. 그래서 10 ÷ 4 = 2.5개. 거스름돈이 소수여도 괜찮은 이유 = 코인(H<sup>+</sup>)으로 계산하니까."),
      ("trap", "ANT는 <b>역수송</b>(ATP 나가고 ADP 들어옴), 인산 전위효소는 <b>공동수송</b>(P<sub>i</sub>와 H<sup>+</sup>가 같이 들어옴). 이름 바꿔 내는 문제 주의.")],
one="P/O = 10/4 = 2.5 (NADH), 6/4 = 1.5 (숙신산). ATP 1개 = H⁺ 3(합성) + 1(ANT·인산 수송)."),

# ───────────────────────────── 문제
dict(t="q", id="q-uncoupler", part=P, kind=["txt", "sa"], title="짝풀림제를 먹으면 왜 열이 나고 살이 빠질까?", src="원서(5판) 19장 연습문제 6 · 솔루션 수록",
en="""In normal mitochondria, electron transfer is tightly coupled to ATP demand; P/O ≈ 2.5 with NADH.<br>
a. Predict the effect of a low and a high concentration of uncoupler on the rate of electron transfer and the P/O ratio.<br>
b. Ingestion of uncouplers causes profuse sweating and an increase in body temperature. Explain. What happens to P/O?<br>
c. How could DNP serve as a weight-reducing aid? Why might uncouplers cause death?""",
q="(a) 짝풀림제 농도가 낮을 때/높을 때 전자전달 속도와 P/O 비 변화 (b) 땀·체온 상승의 분자적 이유 (c) DNP가 체중 감량제가 될 수 있는 원리와 사망 원인",
a="(a) 전자전달 속도 ↑, P/O ↓ (고농도일수록 P/O → 0) (b) H⁺ 기울기 에너지가 ATP 대신 열로 (c) 같은 ATP를 얻으려 연료(지방)를 더 태움 / 고열·ATP 고갈로 사망",
steps=[("(a) 짝풀림제 = H<sup>+</sup> 새는 구멍 → 기울기 ↓ → 호흡사슬이 더 빨리 돈다(<b>O<sub>2</sub> 소비 ↑</b>). 같은 O<sub>2</sub>당 만드는 ATP는 ↓ → <b>P/O ↓</b>. 농도가 높으면 거의 모든 H<sup>+</sup>가 새서 <b>P/O ≈ 0</b>", "구멍이 크면 물레방아는 거의 안 돈다."),
       ("(b) 기울기에 저장된 에너지가 ATP로 안 가고 <b>열</b>로 흩어짐 → 체온 ↑ → 식히려고 땀", ""),
       ("(c) ATP 효율이 떨어지니 필요한 ATP를 채우려 <b>지방·당을 더 많이 태움</b> → 체중 ↓. 그러나 조절이 안 돼 <b>치명적 고열</b> + 뇌·심장 ATP 부족 → 사망", "1930년대 실제 다이어트약 → 금지.")],
one="짝풀림 = 연비 나쁜 엔진: 연료(O₂·지방)는 펑펑, ATP는 찔끔, 나머지는 열."),

dict(t="q", id="q-valino", part=P, kind=["txt", "sa"], title="발리노마이신: 짝풀림제일까, 억제제일까?", src="원서(5판) 19장 연습문제 7 · 솔루션 수록",
en="When valinomycin is added to actively respiring mitochondria, the yield of ATP decreases, the rate of O<sub>2</sub> consumption increases, heat is released, and the pH gradient across the inner membrane increases. Does valinomycin act as an uncoupler or as an inhibitor? Explain in terms of its ability to transfer K<sup>+</sup>.",
q="호흡 중인 미토콘드리아에 발리노마이신을 넣으면 ATP 수율 ↓, O<sub>2</sub> 소비 ↑, 열 발생, <b>pH 기울기는 오히려 ↑</b>. 짝풀림제인가 억제제인가? K<sup>+</sup> 운반 능력으로 설명하시오.",
a="짝풀림제 — K⁺를 기질로 실어 날라 Δψ(전기 기울기)를 없애므로, 호흡사슬이 H⁺를 더 퍼내 ΔpH는 커지지만 전체 구동력이 부족해 ATP는 줄고 에너지는 열로 사라진다.",
steps=[("O<sub>2</sub> 소비 ↑ + ATP ↓ + 열 → <b>짝풀림제</b>의 전형적 징후", "억제제라면 O₂ 소비가 ↓여야 함."),
       ("발리노마이신 = K<sup>+</sup> 이온운반체. 양성자 펌프로 기질이 (−)가 되면 K<sup>+</sup>(+)가 <b>기질 안으로</b> 쏟아져 들어감 → <b>Δψ 소멸</b>", ""),
       ("Δψ가 사라지면 H<sup>+</sup>를 밖으로 퍼내기 쉬워져 호흡사슬이 더 빨리 돌고 → H<sup>+</sup>가 더 많이 쌓여 <b>ΔpH는 ↑</b>", "전하 반발이 없어져 펌프가 가벼워짐."),
       ("하지만 구동력(ΔpH + Δψ)의 큰 몫인 Δψ를 잃어 ATP 합성은 ↓", "")],
one="발리노마이신 = K⁺ 운반 → Δψ 제거 → 짝풀림(O₂ ↑, ATP ↓, 열). 대신 ΔpH는 커진다."),

dict(t="q", id="q-adp", part=P, kind=["txt", "sa"], title="ATP 합성 속도는 왜 Pᵢ가 아니라 ADP가 정할까?", src="원서(5판) 19장 연습문제 11 · 솔루션 수록",
en="Although ATP synthesis requires both ADP and P<sub>i</sub>, the rate of synthesis depends mainly on the concentration of ADP, not P<sub>i</sub>. Why?",
q="ATP 합성에는 ADP와 P<sub>i</sub>가 모두 필요한데, 속도는 주로 ADP 농도에 따라 정해진다. 왜일까?",
a="세포 속 Pᵢ는 늘 충분히(수 mM) 있어 포화 상태지만 ADP는 농도가 낮고, ATP를 쓸 때만 늘어나므로 ADP가 속도를 결정하는 ‘제한 기질’이 된다.",
steps=[("P<sub>i</sub>: 세포 내 농도가 높고 거의 일정 → 효소가 이미 포화 → 조금 변해도 속도 그대로", ""),
       ("ADP: 평소 매우 낮음, ATP를 쓰면(근육 수축 등) 바로 ↑ → 합성 속도가 ADP 농도를 따라감", "Michaelis-Menten에서 K_m 근처 농도 = 속도가 민감하게 변함."),
       ("이것이 <b>acceptor control(수용체 조절)</b> — ADP(인산기를 받는 ‘수용체’)가 호흡 속도를 조절 ({REF:c-regul})", "")],
one="Pᵢ는 늘 넘치고 ADP는 쓸 때만 생긴다 → ADP가 브레이크/액셀 (수용체 조절)."),

dict(t="q", id="q-po", part=P, kind=["calc", "bl"], title="H⁺ 동전으로 ATP 개수 세기", src="개념확인 · 슬라이드 58",
q="""(1) NADH의 전자 2개가 O<sub>2</sub>까지 가면 H<sup>+</sup> <span class="blank">(가)</span>개가 펌프된다 (I 4 + III 4 + IV 2).<br>
(2) 숙신산에서 출발하면 <span class="blank">(나)</span>개.<br>
(3) ATP 1개 합성·수송에 H<sup>+</sup> 4개 → NADH의 P/O = <span class="blank">(다)</span>, 숙신산의 P/O = <span class="blank">(라)</span><br>
(4) ATP 1개당 H<sup>+</sup> 4개 중 1개는 <span class="blank">(마)</span>와 인산 전위효소가 ATP·ADP·P<sub>i</sub>를 옮기는 데 쓰인다.""",
a="(가) 10 (나) 6 (다) 2.5 (라) 1.5 (마) ANT(아데닌 뉴클레오타이드 전위효소)",
steps=[("NADH: 4 + 4 + 2 = <b>10</b>", ""), ("숙신산: Complex II는 펌프 0 → 0 + 4 + 2 = <b>6</b>", ""),
       ("P/O = 펌프된 H<sup>+</sup> ÷ 4 → 10/4 = <b>2.5</b>, 6/4 = <b>1.5</b>", "O 원자 1개 = 전자 2개 기준."),
       ("수송비: ANT(ATP<sup>4−</sup> ↔ ADP<sup>3−</sup>, Δψ 소비) + 인산 전위효소(P<sub>i</sub> + H<sup>+</sup>, ΔpH 소비)", "")],
one="10 → 2.5, 6 → 1.5. 4개 중 1개는 ANT·인산 수송 ‘배송비’."),

dict(t="q", id="q-synth-multi", part=P, kind=["chk", "multi"], title="ATP 합성효소에 대한 설명 모두 고르기", src="개념확인 · 다답형",
q="ATP 합성효소에 대한 설명으로 <b>옳은 것을 모두</b> 고르시오." + opts(
"F<sub>1</sub>은 α<sub>3</sub>β<sub>3</sub>γδε로 구성되며 ATP 합성의 촉매 자리는 주로 β 소단위체에 있다.",
"F<sub>o</sub>의 ‘o’는 올리고마이신 감수성을 뜻하며, F<sub>o</sub>는 양성자 통로다.",
"F<sub>1</sub> 표면에서 ADP + P<sub>i</sub> → ATP 반응의 ΔG′°는 약 −30.5 kJ/mol로 매우 불리하다.",
"F<sub>o</sub>F<sub>1</sub>은 ADP보다 ATP를 훨씬 강하게 결합하며, ATP 방출에 양성자 구동력 에너지가 쓰인다.",
"γ 소단위체는 고정자(stator)로서 회전하지 않고 b<sub>2</sub>와 함께 α<sub>3</sub>β<sub>3</sub>를 붙잡는다."),
a="①, ②, ④",
opx=ox(("①", True, "β에 촉매 자리, α는 주로 조절/구조."), ("②", True, "F<sub>o</sub> = oligomycin-sensitive 양성자 통로."),
       ("③", False, "효소 표면에선 K′<sub>eq</sub> ≈ 2.4, <b>ΔG′° ≈ 0</b>. −30.5는 <b>용액 속</b> 가수분해 값."),
       ("④", True, "K<sub>d</sub>(ATP) ≤ 10<sup>−12</sup> M vs K<sub>d</sub>(ADP) ≈ 10<sup>−5</sup> M."), ("⑤", False, "γ는 <b>회전자</b>(central shaft). 고정자는 a·b<sub>2</sub>·δ.")),
one="F₁ 표면 ΔG≈0, 비싼 건 ATP 방출. γ는 도는 축, b₂·δ는 붙잡는 팔."),

dict(t="q", id="q-tb-binding", part=P, kind=["chk", "mc"], title="결합 변화 모델에서 β 소단위체의 상태", src="개념확인 (영어 원문 연습)",
en="According to the binding-change model of ATP synthase, which statement is correct?" + eopts(
"All three β subunits have identical conformations at any moment.",
"The γ subunit stays fixed while the α<sub>3</sub>β<sub>3</sub> hexamer rotates.",
"At any moment, one β site is empty, one binds ADP + P<sub>i</sub> loosely, and one binds ATP tightly; rotation of γ interconverts them.",
"Energy from proton flow is used mainly to form the phosphoanhydride bond of ATP on the enzyme.",
"One full 360° rotation of γ produces one ATP."),
q="ATP 합성효소의 결합 변화 모델에 대한 설명으로 옳은 것은?",
a="C", aen="One β is empty (open), one loose (ADP + Pᵢ), one tight (ATP); γ rotation interconverts them.",
steps=[("세 β는 γ와의 접촉면이 달라 <b>항상 서로 다른 모양</b>", ""),
       ("γ가 돈다(회전자), α<sub>3</sub>β<sub>3</sub>는 b<sub>2</sub>·δ에 붙잡혀 고정", ""),
       ("양성자 에너지 = ATP <b>방출</b>에 쓰임 / 360° = 3 ATP", "")],
opx=ox(("A", False, "셋은 항상 다르다."), ("B", False, "반대: γ가 돈다."), ("D", False, "결합 형성은 ΔG ≈ 0, 에너지는 방출에."), ("E", False, "한 바퀴 = 3 ATP.")),
one="빈·느슨·꽉 — γ가 돌 때마다 교대, 한 바퀴 ATP 3개."),

dict(t="q", id="q-coupling-ox", part=P, kind=["chk", "tf"], title="짝지음 실험 그래프 O/X", src="개념확인 · O/X · 슬라이드 46–47",
q="""다음 문장이 맞으면 O, 틀리면 X.<br>
(1) 전자전달이 없어도 인공 pH 기울기와 K<sup>+</sup> 유출(Δψ)만 있으면 ATP가 합성될 수 있다. ( )<br>
(2) CN<sup>−</sup>을 넣으면 O<sub>2</sub> 소비는 멈추지만 ATP 합성은 계속된다. ( )<br>
(3) ATP 합성효소를 억제하면 O<sub>2</sub> 소비도 멈춘다. ( )<br>
(4) 짝풀림제는 ATP 합성효소를 직접 억제하는 물질이다. ( )<br>
(5) 미토콘드리아 내막은 H<sup>+</sup>를 자유롭게 통과시키므로 기울기를 유지하려면 펌프가 계속 일해야 한다. ( )""",
a="(1) O (2) X (3) O (4) X (5) X",
steps=[("(1) O — 슬라이드 46 실험: 양성자 구동력만으로 충분", ""),
       ("(2) X — 전자전달이 멈추면 기울기가 사라져 ATP 합성도 멈춤", ""),
       ("(3) O — 짝지음: H<sup>+</sup>가 못 돌아오면 펌프도 멈춤", ""),
       ("(4) X — 짝풀림제는 H<sup>+</sup>를 막 너머로 나르는 <b>약산</b>. 효소 억제제(올리고마이신)와 다름", ""),
       ("(5) X — 내막은 H<sup>+</sup>를 <b>통과시키지 않는다</b>(그래서 기울기 유지). 자유 통과는 외막(포린)", "")],
one="양성자 구동력만으로 ATP OK · 한쪽 막으면 둘 다 멈춤 · 짝풀림제 ≠ 효소 억제제 · 내막은 H⁺ 불투과."),
]
