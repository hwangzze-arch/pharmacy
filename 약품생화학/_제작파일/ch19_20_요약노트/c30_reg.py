from parts import *
P = P3
E = [
dict(t="c", id="c-regul", part=P, title="산화적 인산화의 조절 — 세포가 ATP를 쓸 때만 공장이 돈다", sub="Acceptor control · Acceptor control ratio · Mass-action ratio · Slides 63–64",
core="호흡 속도는 <b>ADP가 얼마나 있느냐</b>로 정해진다(<b>수용체 조절</b>). ATP를 쓰면 [ATP]/([ADP][P<sub>i</sub>])가 내려가고 → 호흡이 빨라진다.",
detail="""<ol><li><b>Acceptor control (억셉터 컨트롤, 수용체 조절)</b>: 인산기를 ‘받는(acceptor)’ <b>ADP</b>의 양이 호흡 속도를 조절.</li>
<li><b>Acceptor control ratio (수용체 조절비)</b> = ADP를 넣었을 때의 최대 O<sub>2</sub> 소비 속도 ÷ 기본 속도 → <b>10 이상</b> (ADP 하나로 10배 이상 빨라짐).</li>
<li><b>Mass-action ratio (질량작용비, Q)</b> = <span class="fx">[ATP] / ([ADP][P<sub>i</sub>])</span> — 평소에는 매우 높음.</li>
<li>에너지 쓰는 일(근육 수축 등) → ATP → ADP + P<sub>i</sub> → <b>질량작용비 ↓</b> → <b>호흡 속도 ↑</b> → ATP 다시 채움.</li></ol>
<p><b>ATP 만드는 경로들의 협동 조절</b>(슬라이드 64): 해당과정, 피루브산 탈수소효소, 시트르산 회로, 산화적 인산화가 같은 신호로 함께 켜지고 꺼진다.</p>
<table class="t"><tr><th>신호</th><th>높으면 →</th></tr>
<tr><td>[ATP]/([ADP][P<sub>i</sub>])</td><td>해당(PFK-1, 피루브산 키나아제) · PDH · 회로 효소 <b>억제</b></td></tr>
<tr><td>[NADH]/[NAD<sup>+</sup>]</td><td>PDH, 시트르산 합성효소, 아이소시트르산·α-KG 탈수소효소 <b>억제</b></td></tr>
<tr><td>[citrate] (시트르산)</td><td>PFK-1 <b>억제</b> → 해당 속도를 회로 속도에 맞춤</td></tr></table>
<div class="term">＊[용어: 질량작용비 = 반응물과 생성물의 실제 농도 비율. ‘창고에 완제품(ATP)이 재료(ADP·P<sub>i</sub>)보다 얼마나 많나’ 지표]</div>""",
side=[("img", 64, "원본 슬라이드 64 — ATP 생성 경로들의 협동 조절 (⊗ 억제, ⊕ 활성)", 230),
      ("ana", "<b>주문 생산 빵집</b>: 손님(ADP)이 와야 오븐(호흡사슬)을 켠다. 진열대에 빵(ATP)이 가득하면(질량작용비 ↑) 반죽(해당)·발효(회로)·오븐까지 전부 쉬어."),
      ("tip", "수용체 조절비 <b>≥ 10</b>, 질량작용비 <b>↓ → 호흡 ↑</b>. 숫자·방향 빈칸 문제.")],
one="ADP가 열쇠(수용체 조절)! ATP 쓰면 [ATP]/[ADP][Pᵢ] ↓ → 호흡 ↑. 해당·PDH·회로·산화적 인산화는 한 몸."),

dict(t="c", id="c-if1", part=P, title="IF₁ — 산소가 부족할 때 ATP 합성효소의 ‘역주행’을 막는 안전핀", sub="Inhibitory protein IF₁ prevents ATP hydrolysis during hypoxia · Slide 65",
core="저산소에선 전자전달이 멈춰 H<sup>+</sup> 기울기가 사라진다. 그러면 ATP 합성효소가 <b>거꾸로 돌아 ATP를 분해(가수분해)</b>할 수 있는데, <b>IF<sub>1</sub></b>이 F<sub>1</sub>에 끼어 이를 막아 ATP를 아낀다.",
detail="""<ul><li><b>IF<sub>1</sub></b> = Inhibitory Factor 1 (억제 인자 1), 84개 아미노산의 작은 단백질.</li>
<li><b>Hypoxia (하이폭시아, 저산소)</b> → 전자전달 ↓ → ATP 합성 ↓ → (그대로 두면 ATP 합성효소가 ATPase로 작동해 ATP를 태우며 H<sup>+</sup>를 퍼냄) → <b>IF<sub>1</sub>이 ATP 가수분해 차단</b> (ATP 절약).</li>
<li>스위치는 <b>pH</b>: 산소 부족 → 피루브산·<b>젖산 ↑</b> → 기질 <b>pH &lt; 6.5</b> → IF<sub>1</sub>이 <b>이량체(dimer)</b>로 활성화 → F<sub>1</sub> 두 개에 동시에 끼어 ATPase 억제 (슬라이드 65 구조: 두 F<sub>1</sub> 사이에 IF<sub>1</sub> 이량체).</li>
<li>산소가 돌아오면(호기성) → pH ↑ → IF<sub>1</sub> 이량체 불안정 → 떨어져 나감 → ATP 합성 재개.</li></ul>
<div class="term">＊[용어: 가수분해(hydrolysis) = 물을 넣어 결합을 끊는 반응. ATP + H<sub>2</sub>O → ADP + P<sub>i</sub>]</div>""",
side=[("img", 65, "원본 슬라이드 65 — 소 F₁-ATPase 2개를 붙잡은 IF₁ 이량체 + 작동 조건", 190),
      ("ana", "<b>정전된 수력발전소</b>: 물(H<sup>+</sup>)이 끊기면 발전기가 거꾸로 모터처럼 돌며 저장 전기(ATP)를 써 버린다. IF<sub>1</sub>은 그때 꽂는 <b>역회전 방지 핀</b> — 산성(pH ↓)일 때만 꽂힌다."),
      ("trap", "IF<sub>1</sub>은 ATP <b>합성</b>을 막는 게 아니라 ATP <b>가수분해</b>를 막는다. 활성 형태 = <b>이량체</b>, 조건 = <b>pH 6.5 미만</b>.")],
one="저산소 → 젖산 → pH < 6.5 → IF₁ 이량체 → ATP 가수분해(역주행) 차단 → ATP 절약."),

dict(t="c", id="c-ros", part=P, title="활성산소(ROS) — 호흡의 부산물과 세포의 방어", sub="ROS generated during oxidative phosphorylation · SOD · GPx · HIF-1 · Slides 66–69",
core="호흡에 쓰이는 O<sub>2</sub>의 <b>0.1–4%</b>는 전자 1개만 받아 <b>초과산화물 라디칼(·O<sub>2</sub><sup>−</sup>)</b>이 된다. 세포는 <b>SOD → 글루타티온 과산화효소</b> 사슬로 해독하고, 저산소에선 <b>HIF-1</b>으로 ROS 생성 자체를 줄인다.",
detail="""<p><b>ROS 사다리</b>: O<sub>2</sub> → <b>·O<sub>2</sub><sup>−</sup></b>(superoxide radical, 초과산화물) → <b>H<sub>2</sub>O<sub>2</sub></b>(hydrogen peroxide, 과산화수소) → <b>·OH</b>(hydroxyl radical, 하이드록실 라디칼, 가장 위험) → H<sub>2</sub>O. 원인: 산화적 인산화, 방사선, 염증, 금속, 약물.</p>
<p>주로 <b>Complex I과 III</b>(Q 부근)에서 전자가 새어 O<sub>2</sub>에 직접 붙어 생김.</p>
<p><b>해독 사슬</b>(슬라이드 66):</p>
<ol><li><b>SOD</b>(SuperOxide Dismutase, 초과산화물 불균등화효소): 2·O<sub>2</sub><sup>−</sup> + 2H<sup>+</sup> → H<sub>2</sub>O<sub>2</sub> + O<sub>2</sub></li>
<li><b>GPx</b>(Glutathione Peroxidase, 글루타티온 과산화효소, 활성부위에 <b>셀레노시스테인(Se)</b>): H<sub>2</sub>O<sub>2</sub> + 2GSH → 2H<sub>2</sub>O + GSSG</li>
<li><b>Glutathione reductase(글루타티온 환원효소)</b>: GSSG + <b>NADPH</b> → 2GSH (재생)</li>
<li>NADPH는 <b>nicotinamide nucleotide transhydrogenase(니코틴아마이드 뉴클레오타이드 전이수소효소)</b>가 NADH + 양성자 구동력으로 만듦.</li></ol>
<p><b>HIF-1</b>(Hypoxia-Inducible Factor 1, 저산소 유도 인자 1): 저산소 → 전자 입력과 전달의 불균형 → ROS ↑ → 미토 손상. 방어로 HIF-1 발현 →
① 해당과정 ↑(포도당 수송체·해당 효소·젖산 탈수소효소 ↑) ② <b>PDH ↓</b>(PDH 키나아제 ↑) → 호흡사슬로 가는 전자 ↓ ③ <b>ROS ↓</b> ④ Complex IV 소단위체 COX4-1 → <b>COX4-2</b>로 교체 → 낮은 O<sub>2</sub>에서 더 효율적.</p>
<div class="term">＊[용어: 라디칼(radical) = 짝 없는 전자를 가진 분자. 짝을 찾으려고 DNA·지질·단백질의 전자를 마구 빼앗는다]</div>""",
side=[("img", 66, "원본 슬라이드 66 — ROS 생성(I·III)과 SOD·GPx·글루타티온 환원효소 방어", 175),
      ("img", 69, "원본 슬라이드 69 — HIF-1: 해당 ↑, PDH ↓, ROS ↓, COX4-2", 165),
      ("ana", "ROS = <b>불꽃 튀는 용접 작업장의 불똥</b>. SOD는 불똥을 모아 물통(H<sub>2</sub>O<sub>2</sub>)에 담고, GPx는 물통을 하수구(H<sub>2</sub>O)로 버린다. HIF-1은 아예 <b>용접 속도를 늦춰</b> 불똥을 줄이는 현장 감독.")],
one="O₂의 0.1–4% → ·O₂⁻ → (SOD) → H₂O₂ → (GPx, Se, GSH) → H₂O. 저산소엔 HIF-1: 해당 ↑, PDH ↓, ROS ↓."),

# ───────────────────────────── 문제
dict(t="q", id="q-if1", part=P, kind=["chk", "bl"], title="IF₁ 작동 시나리오 빈칸", src="개념확인 · 슬라이드 65",
q="""저산소 상태가 되면 전자전달이 느려져 ATP 합성효소가 거꾸로 ATP를 <span class="blank">(가)</span>할 위험이 생긴다.
산소 부족 → 피루브산과 <span class="blank">(나)</span>이 쌓여 pH가 <span class="blank">(다)</span> 미만으로 떨어지면,
억제 단백질 IF<sub>1</sub>이 <span class="blank">(라)</span>(단량체/이량체)를 이루어 F<sub>1</sub>의 ATPase 활성을 억제한다.
산소가 다시 공급되면 pH가 <span class="blank">(마)</span>하여 IF<sub>1</sub>이 떨어지고 ATP 합성이 재개된다.""",
a="(가) 가수분해 (나) 젖산 (다) 6.5 (라) 이량체 (마) 상승",
steps=[("기울기가 없으면 F<sub>o</sub>F<sub>1</sub>은 ATP를 쪼개 H<sup>+</sup>를 퍼내는 ‘역방향’이 됨 → <b>가수분해</b>", ""),
       ("무산소 해당 → <b>젖산</b>·H<sup>+</sup> ↑ → pH ↓", ""),
       ("pH <b>6.5</b> 미만 → IF<sub>1</sub> <b>이량체</b> = 활성형", "이량체가 F₁ 두 개를 동시에 붙잡음."),
       ("호기성 → pH <b>상승</b> → 이량체 불안정 → 해제", "")],
one="저산소 → 젖산 → pH < 6.5 → IF₁ 이량체 → 가수분해 OFF."),

dict(t="q", id="q-hif", part=P, kind=["chk", "multi"], title="저산소 세포에서 HIF-1이 일으키는 변화 모두 고르기", src="개념확인 · 다답형 · 슬라이드 69",
q="저산소 상태의 세포에서 HIF-1 발현이 증가할 때 일어나는 변화로 <b>옳은 것을 모두</b> 고르시오." + opts(
"포도당 수송체와 해당과정 효소의 발현이 증가한다.",
"PDH 키나아제가 증가해 피루브산 탈수소효소(PDH)가 억제된다.",
"NADH·FADH<sub>2</sub>가 호흡사슬로 더 많이 공급되어 ROS가 증가한다.",
"Complex IV의 COX4-1이 COX4-2로 교체되어 낮은 O<sub>2</sub>에 적응한다.",
"젖산 탈수소효소 발현이 감소해 젖산 생성이 줄어든다."),
a="①, ②, ④",
opx=ox(("①", True, "ATP를 해당으로 보충."), ("②", True, "PDH ↓ → 아세틸-CoA·NADH 공급 ↓."), ("③", False, "반대: 호흡사슬로 가는 전자가 <b>줄어</b> ROS ↓."),
       ("④", True, "프로테이스가 COX4-1을 분해, COX4-2로 대체."), ("⑤", False, "LDH <b>증가</b> → 피루브산을 젖산으로 돌려 NAD<sup>+</sup> 재생.")),
one="HIF-1 = 해당 ↑ · LDH ↑ · PDH ↓ · ROS ↓ · COX4-2."),

]
