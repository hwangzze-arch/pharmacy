PAGES = [
dict(img=1, slide=1, src="표지", title="21장 지질 생합성 — 강의 로드맵", sub="Lehninger Principles of Biochemistry · Chapter 21 Lipid Biosynthesis",
kw=["지방산 합성", "중성지방(TAG)", "막 인지질", "콜레스테롤", "지질단백질"],
sum="17장에서 지방을 ‘태우는’ 법(β-산화)을 배웠다면, 21장은 거꾸로 지방을 ‘만드는’ 법이야. 지방산 → 중성지방 → 막 인지질 → 콜레스테롤·스테로이드 → 혈액 속 운반(지질단백질) 순서로 가.",
tr="""<p><b>레닌저 생화학 원리 (5판)</b><br>David L. Nelson · Michael M. Cox</p>
<p><b>21장 지질 생합성 (Lipid Biosynthesis)</b></p>""",
ex="""<table class="t"><tr><th>절</th><th>내용</th><th>슬라이드</th></tr>
<tr><td><b>21.1</b></td><td>지방산 · 에이코사노이드 합성 (ACC, FAS, NADPH, 시트르산 셔틀, 불포화화, 프로스타글란딘)</td><td>2–39</td></tr>
<tr><td><b>21.2</b></td><td>중성지방(TAG) 합성 (포스파티드산, 인슐린, TAG 회로, 글리세롤신생)</td><td>40–50</td></tr>
<tr><td><b>21.3</b></td><td>막 인지질 (글리세로인지질, 스핑고지질, CDP 전략, 플라스말로겐)</td><td>51–66</td></tr>
<tr><td><b>21.4</b></td><td>콜레스테롤 · 스테로이드 (메발론산, HMG-CoA 환원효소, 스타틴, SREBP)</td><td>67–83</td></tr>
<tr><td>—</td><td>지질 운반 (킬로미크론, LDL, HDL, 수용체 매개 세포내이입)</td><td>84–96</td></tr></table>
<div class="box"><span class="tag">수업</span>11/10 수업에서 교수님이 21.1(지방산 합성)을 시작하셨어. “우리의 <b>뱃살</b>을 만드는” 과정이라고 소개하셨지. 약학 쪽에선 <y>스타틴(HMG-CoA 환원효소)</y>, <y>NSAID(COX)</y>, <y>TZD(PPARγ)</y>처럼 약물 표적이 많이 나오는 장이야.</div>"""),

dict(img=2, slide=2, title="지방은 어떻게 만들어질까", sub="Biosynthesis of fat",
kw=["남는 에너지 = 지방", "아세틸-CoA", "세포질"],
sum="밥(탄수화물)을 많이 먹어 남는 에너지는 아세틸-CoA를 거쳐 지방산이 되고, 지방조직에 중성지방으로 쌓여 뱃살이 돼.",
tr="""<p><b>지방의 생합성</b></p>
<p>그림: 줄자로 배 둘레를 재는 사진</p>""",
ex="""<p>먹은 포도당 → 해당과정 → 피루브산 → (미토콘드리아) 아세틸-CoA. ATP가 충분할 때 이 아세틸-CoA는 TCA로 다 태우지 않고 <y>지방산 합성 재료</y>로 쓰여.</p>
<p>지방산은 글리세롤에 3개 붙어 <b>중성지방(triacylglycerol, TAG)</b>이 되어 지방세포에 저장돼. 지방은 g당 약 9 kcal로 탄수화물(4 kcal)보다 두 배 넘게 에너지가 많은 ‘압축 저장’ 형태야.</p>
<div class="boxg">흐름 한 줄: <g>포도당 → 아세틸-CoA → 말로닐-CoA → 팔미트산(C16) → 중성지방</g></div>"""),

dict(img=3, slide=3, title="합성과 분해는 다른 길로 간다", sub="Biosynthesis and breakdown of fatty acids occur by different pathways",
kw=["세포질 vs 미토콘드리아", "지방산 합성효소 vs β-산화 효소", "말로닐-CoA"],
sum="지방산 합성은 세포질에서 지방산 합성효소가, 분해는 미토콘드리아에서 β-산화 효소가 한다. 합성의 중간체는 3탄소 말로닐-CoA야.",
tr="""<p><b>지방산의 합성과 분해는 서로 다른 경로로 일어난다</b></p>
<ol><li>어디서? (<b>세포질 / 미토콘드리아</b>)</li>
<li>효소는? (<b>지방산 합성효소 / β-산화 효소</b>)</li>
<li>중간체는? → <b>말로닐-CoA</b> (구조: ⁻OOC–CH₂–CO–S-CoA)</li></ol>""",
ex="""<table class="t"><tr><th></th><th>합성</th><th>분해 (β-산화)</th></tr>
<tr><td>장소</td><td><b>세포질</b></td><td><b>미토콘드리아</b> 기질</td></tr>
<tr><td>효소</td><td>지방산 합성효소(FAS) 한 덩어리</td><td>β-산화 효소 4종 따로</td></tr>
<tr><td>탄소 공급/산물</td><td><b>말로닐-CoA(3C)</b> → 2C씩 붙음</td><td>아세틸-CoA(2C)씩 떨어짐</td></tr>
<tr><td>운반체</td><td>ACP</td><td>CoA</td></tr>
<tr><td>조효소</td><td><b>NADPH</b> 소비</td><td>FAD, NAD⁺ 환원</td></tr></table>
<div class="box"><span class="tag">수업</span>왜 굳이 다르게? 합성과 분해가 똑같이 2탄소짜리면 너무 가역적이라 <b>만드는 족족 분해</b>되기 때문. 장소·효소·중간체를 다르게 해서 서로 독립적으로 조절해.</div>"""),

dict(img=4, slide=4, title="ACC — 아세틸-CoA를 말로닐-CoA로", sub="ACC (acetyl-CoA carboxylase) reaction and its biotinylation",
kw=["ACC", "말로닐-CoA", "ATP + CO₂(HCO₃⁻)", "비오틴", "속도 결정 단계"],
sum="지방산 합성의 첫 단계: ACC가 아세틸-CoA에 CO₂를 붙여 말로닐-CoA를 만든다. ATP 1개가 들고, 비오틴이 CO₂ 운반을 맡는다.",
tr="""<p><b>ACC (아세틸-CoA 카복실화효소) 반응</b></p>
<p class="eq">아세틸-CoA + CO₂ + ATP + H₂O → 말로닐-CoA + ADP + Pᵢ + H⁺</p>""",
ex="""<p>2탄소 아세틸기에 탄소 1개(CO₂, 실제로는 HCO₃⁻)를 붙여 <y>3탄소 말로닐-CoA</y>를 만들어. 이 반응이 <pk>지방산 합성의 속도 결정 단계(조절 지점)</pk>야.</p>
<ul><li>ATP가 들어가는 이유: CO₂를 붙이려면 먼저 <b>비오틴에 CO₂를 활성화</b>해 붙여야 하는데 그 에너지.</li>
<li>보조인자 <b>비오틴(비타민 B₇)</b> — 피루브산 카복실화효소(당신생)와 같은 비오틴 효소 무리.</li></ul>
<div class="boxg">말로닐-CoA의 CO₂는 다음 단계(축합)에서 <g>다시 빠져나가</g>. 결국 탄소는 2개만 남는데, 이 탈카복실화가 축합 반응을 강하게 앞으로 밀어 주는 ‘에너지 스프링’ 역할을 해.</div>"""),

dict(img=5, slide=5, title="ACC 반응 메커니즘 — 흔들리는 비오틴 팔", sub="The acetyl-CoA carboxylase reaction",
kw=["비오틴 카복실화효소", "비오틴 운반 단백질", "트랜스카복실화효소", "Lys 곁사슬 팔"],
sum="ACC는 도메인 3개: ① 비오틴 카복실화효소가 HCO₃⁻ + ATP로 비오틴에 CO₂를 붙이고 ② 비오틴 팔이 흔들려 ③ 트랜스카복실화효소 자리에서 아세틸-CoA에 넘긴다.",
tr="""<p><b>아세틸-CoA 카복실화효소 반응</b></p>
<p>그림: <b>비오틴</b>이 <b>Lys 곁사슬</b>에 붙은 긴 팔(<b>비오틴 운반 단백질</b>). HCO₃⁻ + ATP → ADP + Pᵢ로 <b>비오틴 카복실화효소</b> 자리에서 비오틴–COO⁻ 생성 → 팔이 <b>트랜스카복실화효소</b> 자리로 이동 → 아세틸-CoA에 CO₂ 전달 → <b>말로닐-CoA</b>.</p>""",
ex="""<p>비오틴은 Lys에 아마이드 결합으로 붙은 <y>긴 그네 팔</y>이야. 한쪽 작업대에서 CO₂를 받아 싣고, 반대쪽 작업대로 흔들려 가서 내려놓는 셔틀.</p>
<ol><li>① <b>비오틴 카복실화효소</b>: HCO₃⁻ + ATP → 카복시비오틴 (ATP 쓰임)</li>
<li>② <b>비오틴 운반 단백질(BCCP)</b>: 팔이 흔들려 이동</li>
<li>③ <b>트랜스카복실화효소</b>: 카복시기를 아세틸-CoA로 → 말로닐-CoA</li></ol>
<div class="box"><span class="tag">수업</span>교수님: “biotin is <b>swinging</b> through the active site of transcarboxylase.” 도메인 세 개의 이름을 짝지어 외워 둬.</div>
<p class="note">동물 ACC는 세 기능이 한 폴리펩타이드, 세균은 단백질 세 개로 나뉘어 있어.</p>"""),

dict(img=6, slide=6, title="지방산 합성효소 FAS I vs FAS II", sub="fatty acid synthase",
kw=["FAS I", "FAS II", "척추동물·곰팡이", "식물·세균"],
sum="척추동물·곰팡이는 모든 효소 기능이 한 덩어리(FAS I), 식물·세균은 단계마다 따로 된 효소(FAS II)를 쓴다.",
tr="""<p><b>지방산 합성효소</b></p>
<table class="t"><tr><th>FAS I</th><th>FAS II</th></tr>
<tr><td>척추동물 & 곰팡이</td><td>식물 & 세균</td></tr>
<tr><td>단일 폴리펩타이드, <b>동종이량체</b> 또는 이종 12량체(곰팡이)</td><td>단계마다 <b>분리된 효소</b></td></tr></table>""",
ex="""<p><b>FAS I</b>은 공장의 모든 기계가 한 줄 컨베이어로 붙은 ‘일체형 조립 라인’이야. 중간체가 효소 밖으로 나가지 않고 도메인 사이로 바로 넘어가서 빠르고 효율적이야.</p>
<p><b>FAS II</b>는 기계가 따로 떨어진 공장이라 중간체(ACP에 붙은 상태)가 효소 사이를 떠돌아. 식물에선 <y>엽록체</y>에 있어.</p>
<div class="box"><span class="tag">시험</span>“척추동물 FAS = 하나의 폴리펩타이드에 여러 활성(다기능 효소)” — O/X 단골. 항생제 일부(예: 이소니아지드, 트리클로산)는 <b>세균 FAS II</b>를 표적으로 해서 사람에겐 덜 해로워.</div>"""),

dict(img=7, slide=7, title="FAS I 구조 — 도메인 7개", sub="The structure of fatty acid synthase type I systems",
kw=["KS", "MAT", "DH", "ER", "KR", "ACP", "TE"],
sum="포유류 FAS 한 사슬에 KS · MAT · DH · ER · KR · ACP · TE 7개 도메인이 순서대로 있다. ACP는 효소가 아니라 아실기를 들고 다니는 팔, TE는 다 만든 팔미트산을 떼어 낸다.",
tr="""<p><b>FAS I 시스템의 구조</b></p>
<ul><li><b>KS</b> β-케토아실-ACP 합성효소</li><li><b>MAT</b> 말로닐/아세틸-CoA–ACP 전달효소</li>
<li><b>DH</b> β-하이드록시아실-ACP 탈수효소</li><li><b>ER</b> 에노일-ACP 환원효소</li>
<li><b>KR</b> β-케토아실-ACP 환원효소</li><li><b>ACP</b> 아실 운반 단백질</li>
<li>일곱 번째 <b>TE</b>(싸이오에스터 가수분해효소)는 합성이 끝나면 ACP에서 <b>팔미트산을 떼어 낸다</b>.</li></ul>""",
ex="""<table class="t"><tr><th>약자</th><th>하는 일</th><th>4단계 중</th></tr>
<tr><td><b>MAT</b></td><td>아세틸·말로닐을 CoA에서 FAS로 옮겨 실음</td><td>준비</td></tr>
<tr><td><b>KS</b></td><td>축합 (C–C 결합, CO₂ 방출)</td><td>①</td></tr>
<tr><td><b>KR</b></td><td>케톤 → 알코올 (NADPH)</td><td>②</td></tr>
<tr><td><b>DH</b></td><td>물 빼서 이중결합</td><td>③</td></tr>
<tr><td><b>ER</b></td><td>이중결합 → 단일결합 (NADPH)</td><td>④</td></tr>
<tr><td><b>ACP</b></td><td>팔(–SH)로 중간체 운반, 효소 아님</td><td>—</td></tr>
<tr><td><b>TE</b></td><td>C16 팔미트산 방출</td><td>끝</td></tr></table>
<div class="boxg">순서 외우기: <g>K-R-D-E</g> (KS → KR → DH → ER) = “<b>축-환-탈-환</b>”</div>"""),

dict(img=8, slide=8, title="팔미트산 합성 전체 — 2탄소씩 자란다", sub="The overall process of palmitate synthesis",
kw=["활성화된 말로닐", "CO₂ 방출", "2탄소씩", "7바퀴 → C16"],
sum="첫 아세틸기(C2)에 말로닐-CoA가 올 때마다 CO₂가 빠지며 2탄소씩 붙는다. 7바퀴 돌면 C16 팔미트산이 완성돼 떨어져 나온다.",
tr="""<p><b>팔미트산 합성의 전체 과정</b></p>
<p>활성화된 말로닐 → <b>CO₂를 방출</b>하며 → <b>2탄소 단위씩 자란다</b>. 매 바퀴 4H⁺ + 4e⁻(NADPH 2개) 사용. 네 번 더 붙이고 → <b>팔미트산(C16)</b>.</p>""",
ex="""<p>그림의 노란 칸 = 처음 아세틸기 C2, 분홍/파랑 칸 = 매 바퀴 붙는 C2. 말로닐(초록 COO⁻)의 CO₂는 매번 빠져.</p>
<ul><li>C2 → C4 → C6 → C8 → C10 → C12 → C14 → <b>C16</b></li>
<li>바퀴 수 = <pk>7</pk> → 말로닐-CoA <b>7개</b>, 아세틸-CoA(시작) <b>1개</b></li>
<li>매 바퀴 NADPH 2개 → 총 <pk>NADPH 14개</pk></li></ul>
<div class="boxg">왜 C16에서 멈출까? FAS의 KS 주머니가 C16까지만 들어가고, 그 길이에서 TE가 잘라내기 때문. 더 긴 지방산은 소포체에서 따로 늘려(엘롱게이션).</div>"""),

dict(img=9, slide=9, title="2탄소 붙이는 4단계 반응", sub="Addition of two carbons to a growing fatty acyl chain: a four-step sequence",
kw=["① 축합", "② 환원", "③ 탈수", "④ 환원", "트랜스-Δ²"],
sum="축합(CO₂ 방출) → 환원(NADPH) → 탈수(H₂O 방출) → 환원(NADPH). 아세토아세틸 → β-하이드록시부티릴 → 부텐오일(크로토닐) → 부티릴-ACP.",
tr="""<p><b>자라는 지방산 사슬에 탄소 2개 더하기: 4단계</b></p>
<ol><li><b>축합</b>: 말로닐기 + 아세틸기 → <b>아세토아세틸-ACP</b> + CO₂</li>
<li><b>환원</b> (NADPH): → <b>β-하이드록시부티릴-ACP</b></li>
<li><b>탈수</b>: → <b>부텐오일-ACP (크로토닐-ACP)</b> + H₂O</li>
<li><b>환원</b> (NADPH): → <b>부티릴-ACP</b> (포화 아실기, 탄소 2개 늘어남)</li></ol>""",
ex="""<table class="t"><tr><th>단계</th><th>효소</th><th>무엇이 바뀌나</th><th>나가는/드는 것</th></tr>
<tr><td>① 축합</td><td>KS</td><td>C2 + C3 → C4 β-케토</td><td>CO₂ 나감</td></tr>
<tr><td>② 환원</td><td>KR</td><td>C=O → CH–OH</td><td><b>NADPH</b></td></tr>
<tr><td>③ 탈수</td><td>DH</td><td>–OH와 H 빠져 C=C (trans-Δ²)</td><td>H₂O 나감</td></tr>
<tr><td>④ 환원</td><td>ER</td><td>C=C → C–C</td><td><b>NADPH</b></td></tr></table>
<div class="box"><span class="tag">수업</span>“겨우 두 개 붙이는데 네 단계를 거친다. β-산화도 두 개 떼는 데 네 단계였죠.” β-산화(산화 → 수화 → 산화 → 티올분해)를 <b>정확히 거꾸로</b> 돌리는 셈이야.</div>
<p class="note">하이드록시기 입체: 합성은 <b>D</b>-β-하이드록시, β-산화는 <b>L</b>-β-하이드록시 (서로 다름).</p>"""),

dict(img=10, slide=10, title="ACP — 4′-포스포판테테인 팔", sub="Acyl carrier protein (ACP)",
kw=["ACP", "4′-포스포판테테인", "Ser–OH", "판토텐산(B₅)", "–SH 싸이오에스터"],
sum="ACP의 보결분자단은 4′-포스포판테테인으로, Ser의 –OH에 공유결합돼 있다. 끝의 –SH에 말로닐·아실기가 싸이오에스터로 붙어 이 도메인 저 도메인을 돌아다닌다.",
tr="""<p><b>아실 운반 단백질(ACP)</b>. 보결분자단은 <b>4′-포스포판테테인</b>이며, ACP의 <b>Ser 잔기의 하이드록시기</b>에 공유결합되어 있다.</p>
<p>그림: Ser 곁사슬–CH₂–O–인산–<b>판토텐산</b>–β-알라닌–시스테아민–<b>SH</b>. 말로닐기는 이 <b>–SH에 에스터화</b>된다.</p>""",
ex="""<p>ACP의 긴 팔은 <y>판토텐산(비타민 B₅)</y>이 포함된 4′-포스포판테테인이야. 놀랍게도 <b>CoA에도 똑같은 부분</b>이 들어 있어서, CoA와 ACP 모두 끝의 –SH로 아실기를 싸이오에스터(–CO–S–)로 잡아.</p>
<ul><li>팔 길이가 약 2 nm → 효소의 여러 활성 부위 사이를 <b>흔들리며</b> 중간체를 배달 (ACC의 비오틴 팔과 같은 아이디어)</li>
<li>교수님: “ACP는 엔자임이 아니고 아실기를 옮겨 주는 도메인”, “터미널에 SH가 있어서 거기에 컨쥬게이션”</li></ul>
<div class="boxg">한 FAS에는 –SH가 두 개 있어: <g>ACP의 판테테인 –SH</g>(말로닐 자리)와 <g>KS의 Cys –SH</g>(자라는 사슬 자리).</div>"""),

dict(img=11, slide=11, title="준비 ① — 아세틸기가 KS에 붙는다", sub="ACP is flexible, then attached to KS · Acetyl group binds to KS",
kw=["MAT", "아세틸-CoA", "KS의 Cys–SH", "Figure 21-6 part 1"],
sum="MAT가 아세틸-CoA의 아세틸기를 ACP로 옮기고, 이것이 다시 KS의 Cys–SH로 넘어가 첫 번째 ‘머리’ 자리를 차지한다.",
tr="""<p><b>ACP는 유연해서 KS에 붙고, 아세틸기가 KS에 결합한다</b></p>
<p>그림: 아세틸-CoA → (MAT) → CoA-SH 방출, 아세틸기(CH₃–CO–S)가 <b>KS</b>에 붙은 FAS.</p>""",
ex="""<p>합성 시작 전 ‘장전’ 단계. 첫 아세틸기는 <y>시작 블록(primer)</y>이야. 이 C2가 나중에 팔미트산의 <b>메틸 끝(C15–C16)</b>이 돼.</p>
<ul><li>MAT(말로닐/아세틸 전달효소)가 CoA에서 떼어 FAS에 실어 줘.</li>
<li>아세틸기는 최종적으로 <b>KS의 Cys–SH</b>에 앉아서 기다려.</li></ul>
<div class="box"><span class="tag">수업</span>교수님: “MAT라는 효소에 의해서 아세틸기가 먼저 KS 도메인에 붙어요. 두 개짜리가 먼저 붙는 거예요.”</div>"""),

dict(img=12, slide=12, title="준비 ② — 말로닐기가 ACP에 붙는다", sub="Malonyl group binds to ACP",
kw=["MAT", "말로닐-CoA", "ACP–SH", "아세틸 + 말로닐 장전 완료"],
sum="MAT가 말로닐-CoA의 말로닐기를 ACP의 –SH로 옮긴다. 이제 KS에는 아세틸, ACP에는 말로닐 — 축합 준비 완료.",
tr="""<p><b>말로닐기가 ACP에 결합한다</b> (말로닐-아세틸-CoA ACP 전달효소, MAT)</p>
<p>그림: 말로닐-CoA → CoA-SH 방출 → “<b>아세틸기와 말로닐기가 장전된 FAS 복합체</b>”.</p>""",
ex="""<p>두 개의 손이 모두 찼어:</p>
<ul><li><b>KS의 Cys–SH</b> ← 아세틸기(C2)</li><li><b>ACP의 판테테인 –SH</b> ← 말로닐기(C3)</li></ul>
<p>그림의 파란 화살표는 다음 단계를 예고해: 말로닐의 COO⁻가 CO₂로 빠지면서 생긴 탄소 음이온이 아세틸기의 C=O를 공격해 C–C 결합을 만들어.</p>
<div class="boxg">MAT는 ‘아세틸도, 말로닐도’ 옮기는 효소라 이름에 malonyl/acetyl이 같이 들어가.</div>"""),

dict(img=13, slide=13, title="① 축합 (KS) — CO₂가 빠지며 C4", sub="β-ketoacyl ACP synthase (KS): Condensation, release of CO₂",
kw=["KS", "축합", "CO₂ 방출", "β-케토부티릴-ACP"],
sum="KS가 아세틸기와 말로닐기를 축합한다. 말로닐의 CO₂가 빠지면서 탄소 4개의 β-케토부티릴(아세토아세틸)-ACP가 ACP에 생긴다.",
tr="""<p><b>β-케토아실 ACP 합성효소 (KS)</b></p>
<p><b>축합, CO₂ 방출, ACP에 β-케토아실기 형성</b></p>
<p>그림: ① 축합(KS) → CO₂ → <b>β-케토부티릴-ACP</b> (CH₃–CO–CH₂–CO–S–ACP)</p>""",
ex="""<p>KS에 있던 아세틸기가 ACP 쪽 말로닐기 위로 옮겨 붙어. 결과물은 <b>ACP</b>에 달리고, KS의 –SH는 비게 돼.</p>
<ul><li>탄소 수: 2 + 3 − 1(CO₂) = <b>4</b></li>
<li>CO₂가 빠지는 이유: 탈카복실화가 반응을 열역학적으로 강하게 밀어 줌 → ACC에서 쓴 ATP 에너지가 여기서 회수되는 셈.</li></ul>
<div class="box"><span class="tag">시험</span>축합 효소 = <b>KS</b>(β-케토아실-ACP <b>합성효소</b>). 교수님도 강의 중 “MAT에 의해 축합”이라고 했다가 바로 “KS 반응에 의해서 컨덴세이션”으로 정정하셨어. <pk>축합 = KS</pk>.</div>"""),

dict(img=14, slide=14, title="② 환원 (KR) — 케톤이 알코올로", sub="β-ketoacyl ACP reductase (KR): Reduction of βKB to βHB",
kw=["KR", "NADPH", "β-케토 → β-하이드록시", "D-이성질체"],
sum="KR이 NADPH로 β-케토부티릴-ACP의 C=O를 CH–OH로 환원해 β-하이드록시부티릴-ACP를 만든다.",
tr="""<p><b>β-케토아실 ACP 환원효소 (KR)</b></p>
<p><b>β-케토부티릴(βKB)을 β-하이드록시부티릴(βHB)로 환원 — NADPH 필요</b></p>
<p>그림: ② β-케토기 환원(KR), NADPH + H⁺ → NADP⁺</p>""",
ex="""<p>β 위치(C3)의 케톤 C=O에 수소 2개(NADPH의 하이드라이드 + H⁺)가 붙어 <b>알코올 CH–OH</b>가 돼.</p>
<div class="boxg">교수님: “C=O 그룹이 CH-OH로, 하이드로젠이 하나씩 붙어서 리덕션.” 첫 번째 <g>NADPH</g> 사용 지점.</div>
<p class="note">생기는 하이드록시기는 <b>D</b> 입체배치야. β-산화 때 나오는 것은 <b>L</b>-β-하이드록시아실-CoA라 서로 다른 효소가 다뤄.</p>"""),

dict(img=15, slide=15, title="③ 탈수 (DH) — 물이 빠져 이중결합", sub="β-hydroxyacyl ACP dehydratase (DH): Dehydration of βHB to tButenoyl",
kw=["DH", "H₂O 방출", "trans-Δ²-부텐오일-ACP", "크로토닐"],
sum="DH가 C2–C3 사이에서 물을 빼 trans 이중결합을 만든다 → trans-Δ²-부텐오일-ACP.",
tr="""<p><b>β-하이드록시아실 ACP 탈수효소 (DH)</b></p>
<p><b>βHB를 trans-부텐오일로 탈수</b></p>
<p>그림: ③ 탈수(DH), H₂O 방출 → <b>trans-Δ²-부텐오일-ACP</b></p>""",
ex="""<p>C3의 –OH와 C2의 H가 물(H₂O)로 빠지며 C2=C3 이중결합이 생겨.</p>
<ul><li>Δ²: 카보닐 탄소(C1)부터 세어 <b>2번 탄소에서 시작하는</b> 이중결합</li>
<li><b>trans</b>: 사슬이 이중결합 양쪽 반대편 (β-산화의 엔오일-CoA도 trans-Δ²)</li></ul>
<div class="box"><span class="tag">수업</span>교수님: “CH-OH하고 CH₂에서 물이 빠져나가면서 더블 본드를 만드는 게… trans-delta2-butenoyl-ACP라고 합니다.”</div>"""),

dict(img=16, slide=16, title="④ 환원 (ER) — 이중결합이 단일결합으로", sub="Enoyl ACP reductase (ER): Reduction of tButenoyl to Butyryl",
kw=["ER", "NADPH", "부티릴-ACP", "포화 C4"],
sum="ER이 NADPH로 C=C를 환원해 포화된 부티릴-ACP(C4)를 만든다. 두 번째 NADPH 사용 — 한 바퀴 끝.",
tr="""<p><b>에노일 ACP 환원효소 (ER)</b></p>
<p><b>trans-부텐오일을 부티릴로 환원 — NADPH 필요</b></p>
<p>그림: ④ 이중결합 환원(ER), NADPH + H⁺ → NADP⁺ → <b>부티릴-ACP</b> (CH₃–CH₂–CH₂–CO–S–ACP)</p>""",
ex="""<p>이중결합에 수소 2개가 더해져 <y>포화 탄화수소 사슬</y>이 돼. 이로써 아세틸(C2) → 부티릴(C4), 탄소 2개 늘리기 완료.</p>
<div class="boxg">한 바퀴 장부: <g>NADPH 2개 쓰고, CO₂ 1개 · H₂O 1개 나감</g> (슬라이드 20)</div>
<p class="note">β-산화 첫 단계(아실-CoA 탈수소효소, FAD)를 거꾸로 한 반응이지만, 합성은 FAD가 아니라 <b>NADPH</b>를 써.</p>"""),

dict(img=17, slide=17, title="⑤ 자리 이동 — 부티릴을 KS로", sub="Translocation of butyryl to KS",
kw=["translocation", "KS의 Cys–SH", "ACP 비움"],
sum="완성된 부티릴기가 ACP에서 KS의 Cys–SH로 옮겨간다. ACP가 비어야 새 말로닐을 받을 수 있기 때문이다.",
tr="""<p><b>부티릴기를 KS로 자리 이동</b></p>
<p>⑤ 부티릴기가 β-케토아실-ACP 합성효소(KS)의 <b>Cys</b>로 옮겨감.</p>""",
ex="""<p>이제 부티릴기(C4)가 처음 아세틸기가 있던 자리(KS)로 돌아가. 즉 <y>KS = 자라는 사슬의 대기석</y>, <y>ACP = 새 재료(말로닐) 받는 손</y>.</p>
<div class="box"><span class="tag">수업</span>교수님: “ACP에 붙어 있던 elongated chain이 KS로 옮겨가 붙는 거죠… 요건 <b>translocation</b>.”</div>"""),

dict(img=18, slide=18, title="⑥ 재장전 — 두 번째 말로닐", sub="2nd Malonyl group attached to ACP",
kw=["MAT", "재장전", "두 번째 바퀴"],
sum="MAT가 새 말로닐-CoA를 비어 있는 ACP에 다시 붙인다. 이제 KS엔 부티릴(C4), ACP엔 말로닐 — 두 번째 바퀴 준비.",
tr="""<p><b>두 번째 말로닐기가 ACP에 붙음</b></p>
<p>⑥ 다른 말로닐기로 ACP 재충전 (MAT). “아세틸(여기선 부티릴)기와 말로닐기가 장전된 FAS 복합체.”</p>""",
ex="""<p>슬라이드 12와 같은 장면이지만 KS 쪽 사슬이 C2가 아니라 <b>C4</b>야. 이 패턴이 매 바퀴 반복돼.</p>
<div class="boxg">반복 단위: <g>장전(MAT) → 축합(KS) → 환원(KR) → 탈수(DH) → 환원(ER) → 자리 이동</g></div>"""),

dict(img=19, slide=19, title="두 번째 바퀴의 시작", sub="Beginning of the second round of the fatty acid synthesis cycle",
kw=["2nd round", "C4 + C3 → C6", "β-케토아실-ACP"],
sum="부티릴(C4)과 말로닐이 KS에서 축합해 C6 β-케토아실-ACP가 된다. 이후 같은 4단계를 반복한다.",
tr="""<p><b>지방산 합성 회로 두 번째 바퀴의 시작</b></p>
<p>부티릴기 + 말로닐-CoA(MAT) → 축합(KS), CO₂ 방출 → <b>β-케토아실-ACP</b> (C6)</p>""",
ex="""<p>C4 + C3 − CO₂ = <b>C6</b>. 이후 KR → DH → ER로 헥사노일(C6)이 되고, 다시 KS로 옮겨가.</p>
<p>이렇게 7바퀴: 4 → 6 → 8 → 10 → 12 → 14 → <b>16</b>. 마지막에 <b>TE</b>가 팔미토일-ACP를 가수분해해 자유 <b>팔미트산</b>을 내놓아.</p>"""),

dict(img=20, slide=20, title="한 바퀴 장부 — NADPH 2, CO₂ 1, H₂O 1", sub="Sequence of events during synthesis of a fatty acid",
kw=["2 NADPH", "1 CO₂", "1 H₂O", "Figure 21-6 전체"],
sum="한 바퀴(탄소 2개 추가)마다 NADPH 2개가 필요하고 CO₂ 1개와 H₂O 1개가 나온다.",
tr="""<p><b>지방산 합성 중 일어나는 일의 순서</b></p>
<ul><li><b>NADPH 2개</b> 필요</li><li><b>CO₂ 1개</b> 방출</li><li><b>H₂O 1개</b> 방출</li></ul>
<p>그림: Figure 21-6 전체(①–⑥) 순환도</p>""",
ex="""<table class="t"><tr><th>단계</th><th>들어감</th><th>나옴</th></tr>
<tr><td>장전</td><td>말로닐-CoA</td><td>CoA-SH</td></tr>
<tr><td>① 축합</td><td></td><td><b>CO₂</b></td></tr>
<tr><td>② 환원</td><td><b>NADPH</b></td><td>NADP⁺</td></tr>
<tr><td>③ 탈수</td><td></td><td><b>H₂O</b></td></tr>
<tr><td>④ 환원</td><td><b>NADPH</b></td><td>NADP⁺</td></tr></table>
<div class="box"><span class="tag">시험</span>팔미트산 1개 = 7바퀴 → NADPH <b>14</b>, CO₂ <b>7</b>(말로닐에서 나온 것), H₂O 7 생성(하나는 TE 가수분해에 쓰여 순 <b>6</b>).</div>"""),

dict(img=21, slide=21, title="전체 반응식 — 팔미트산 1개의 장부", sub="Overall reaction",
kw=["아세틸-CoA 8", "ATP 7", "NADPH 14", "H₂O 6"],
sum="말로닐-CoA 7개 만들 때 ATP 7개, 팔미트산 합성에 NADPH 14개. 합치면 아세틸-CoA 8 + ATP 7 + NADPH 14 → 팔미트산 + 6H₂O.",
tr="""<p class="eq">(1) 7 아세틸-CoA + 7 CO₂ + 7 ATP → 7 말로닐-CoA + 7 ADP + 7 Pᵢ</p>
<p class="eq">(2) 아세틸-CoA + 7 말로닐-CoA + 14 NADPH + 14 H⁺ → 팔미트산 + 7 CO₂ + 8 CoA + 14 NADP⁺ + 6 H₂O</p>
<p class="eq">(1+2) 8 아세틸-CoA + 7 ATP + 14 NADPH + 14 H⁺ → 팔미트산 + 8 CoA + 7 ADP + 7 Pᵢ + 14 NADP⁺ + 6 H₂O</p>""",
ex="""<p><b>숫자 맞추기 Step-by-Step</b></p>
<ol><li>C16 ÷ 2 = 아세틸 단위 <b>8개</b> → 1개는 시작(primer), <b>7개</b>는 말로닐로 바꿔야 함.</li>
<li>말로닐 1개 = ATP 1개 (ACC) → ATP <b>7</b>.</li>
<li>바퀴 1개 = NADPH 2개 × 7바퀴 = <b>14</b>.</li>
<li>CO₂는 ACC에서 7개 들어갔다가 축합에서 7개 나옴 → 순 0 (그래서 합친 식에서 사라짐).</li>
<li>H₂O: 탈수 7 생성 − TE 가수분해 1 사용 = 순 <b>6</b>.</li></ol>
<div class="box"><span class="tag">시험</span><pk>8 아세틸-CoA · 7 ATP · 14 NADPH</pk> 세 숫자는 빈칸 단골. 캘빈 회로 “포도당 = ATP 18 + NADPH 12”와 헷갈리지 말 것.</div>"""),

dict(img=22, slide=22, title="비교: β-산화 4단계 복습", sub="β-oxidation of saturated FA's (Chapter 17 review)",
kw=["탈수소(FAD)", "수화", "탈수소(NAD⁺, L 특이)", "티올분해"],
sum="β-산화는 ① 탈수소(FAD) ② 물 첨가 ③ 탈수소(NAD⁺, L-이성질체 특이) ④ 티올분해로 2탄소(아세틸-CoA)를 뗀다. 팔미토일-CoA 1개 → 아세틸-CoA 8 + FADH₂ 7 + NADH 7.",
tr="""<p><b>1) 포화지방산의 β-산화 — 기본 4단계</b></p>
<ol><li>Cₙ 아실-CoA의 <b>탈수소</b></li><li><b>물 첨가</b></li><li><b>탈수소: L-이성질체에 특이적</b></li><li><b>티올분해</b>: Cₙ₋₂ 아실-CoA + 아세틸-CoA</li></ol>
<p class="eq">팔미토일-CoA + 7 CoA + 7 FAD + 7 NAD⁺ + 7 H₂O → 8 아세틸-CoA + 7 FADH₂ + 7 NADH + 7 H⁺</p>""",
ex="""<table class="t"><tr><th>β-산화 (분해)</th><th>합성 (거꾸로)</th></tr>
<tr><td>④ 티올분해 (thiolase)</td><td>① 축합 (KS)</td></tr>
<tr><td>③ 탈수소 (NAD⁺ → NADH)</td><td>② 환원 (NADPH)</td></tr>
<tr><td>② 수화 (+H₂O)</td><td>③ 탈수 (−H₂O)</td></tr>
<tr><td>① 탈수소 (FAD → FADH₂)</td><td>④ 환원 (NADPH)</td></tr></table>
<div class="boxg">거울 관계: <g>분해는 산화제(FAD, NAD⁺)로 전자를 뽑고, 합성은 환원제(NADPH)로 전자를 넣는다.</g></div>
<p class="note">17장 시험대비 노트와 함께 보면 좋아. 하이드록시 입체: 분해 L, 합성 D.</p>"""),

dict(img=23, slide=23, title="지방산 합성은 어디서 일어날까?", sub="Where fatty acid synthesis take place?",
kw=["세포질(동물)", "엽록체(식물)"],
sum="질문 슬라이드. 답: 동물·효모는 세포질, 식물은 엽록체(스트로마).",
tr="""<p><b>지방산 합성은 어디서 일어날까?</b></p>""",
ex="""<p>다음 슬라이드(24)가 답이야.</p>
<ul><li><b>동물·효모</b>: <y>세포질</y> — NADPH가 풍부한 곳</li>
<li><b>식물</b>: <y>엽록체</y> — 광합성 명반응이 NADPH를 직접 공급</li></ul>
<div class="box"><span class="tag">시험</span>Summary 3: “지방산 합성은 많은 생물에서 세포질, 식물에선 엽록체에서 일어난다.”</div>"""),

dict(img=24, slide=24, title="세포 안 지질 대사의 위치", sub="Subcellular localization of lipid metabolism",
kw=["미토콘드리아: 산화", "세포질: 합성", "소포체: 인지질·스테롤·연장·불포화", "퍼옥시좀"],
sum="동물: 지방산 합성·NADPH 생산은 세포질, 산화·케톤체는 미토콘드리아, 인지질·스테롤 후반·사슬 연장·불포화는 소포체. 식물: 합성은 엽록체, 산화는 퍼옥시좀.",
tr="""<p><b>지질 대사의 세포 내 위치</b> (동물·효모 세포 / 식물 세포)</p>
<ul><li><b>미토콘드리아</b>: 지방산 산화, 아세틸-CoA 생산, 케톤체 합성, 지방산 연장 (식물: 지방산 산화 없음)</li>
<li><b>소포체</b>: 인지질 합성, 스테롤 합성(후반), 지방산 연장, 지방산 불포화화</li>
<li><b>세포질</b>: NADPH 생산(오탄당 인산 경로, 말산 효소), [NADPH]/[NADP⁺] 높음, 아이소프레노이드·스테롤 합성(초기), <b>지방산 합성</b></li>
<li><b>엽록체</b>: NADPH·ATP 생산, [NADPH]/[NADP⁺] 높음, <b>지방산 합성</b></li>
<li><b>퍼옥시좀</b>: 지방산 산화(→ H₂O₂), 카탈레이스·과산화효소(H₂O₂ → H₂O)</li></ul>""",
ex="""<table class="t"><tr><th>소기관</th><th>동물</th><th>식물</th></tr>
<tr><td>지방산 <b>합성</b></td><td>세포질</td><td>엽록체</td></tr>
<tr><td>지방산 <b>산화</b></td><td>미토콘드리아 (+퍼옥시좀)</td><td>퍼옥시좀</td></tr>
<tr><td>연장 · 불포화</td><td colspan="2">소포체 (연장은 미토도)</td></tr>
<tr><td>인지질 · 콜레스테롤 후반</td><td colspan="2">소포체</td></tr></table>
<div class="boxg">공통 원리: <g>합성은 NADPH가 넘치는 곳에서</g> (세포질의 오탄당 인산 경로·말산 효소, 엽록체의 명반응).</div>"""),
]
