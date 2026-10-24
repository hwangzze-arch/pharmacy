from parts import *
P = P4
E = [
dict(t="c", id="c-thermo", part=P, title="열발생 — 갈색지방은 일부러 ‘짝을 풀어’ 난로가 된다", sub="(1) Thermogenesis · Brown adipose tissue · Thermogenin (UCP1) · Slides 71–73",
core="갈색지방(BAT)의 미토콘드리아 내막에는 <b>thermogenin(UCP1)</b>이라는 H<sup>+</sup> 통로가 있어, H<sup>+</sup>가 ATP 합성효소를 거치지 않고 돌아온다 → 전자전달 에너지가 <b>전부 열</b>로.",
detail="""<p>미토콘드리아는 ‘세포의 발전소’(피루브산 탈수소, 시트르산 회로, β-산화, 전자전달, ATP 합성)이지만 <b>그 밖에도</b> ① 열발생 ② 해독 ③ 스테로이드 합성 ④ 세포자멸사를 한다 (슬라이드 71).</p>
<ul><li><b>BAT</b>(Brown Adipose Tissue, 갈색지방조직): 미토콘드리아가 <b>아주 많아</b> 갈색(시토크롬의 철 색). 지방 방울이 작고 여러 개. ↔ 백색지방은 큰 지방 방울 하나 + 미토 적음.</li>
<li>어디에? <b>신생아</b>(목·어깨·등), 겨울잠 동물, 추위에 적응한 성인.</li>
<li><b>Thermogenin (써모제닌) = UCP1</b>(UnCoupling Protein 1, 짝풀림 단백질 1): 내막의 <b>양성자 통로</b> → H<sup>+</sup> 펌핑과 ATP 합성의 <b>짝을 풂</b> → 에너지가 열로 흩어짐.</li>
<li>지방산이 UCP1을 활성화(교감신경 → 노르에피네프린 → 지방 분해).</li></ul>
<div class="term">＊[용어: 갈색지방 = ‘태우는 지방’, 백색지방 = ‘쌓아 두는 지방’]</div>""",
side=[("img", 73, "원본 슬라이드 73 — Thermogenin이 H⁺ 지름길을 열어 에너지를 열로", 220),
      ("ana", "<b>일부러 구멍 낸 댐 = 온수기</b>. 물레방아(ATP)는 포기하고, 쏟아지는 물살의 마찰열로 아기를 따뜻하게. DNP(약)와 같은 원리를 몸이 <b>단백질로 조절하며</b> 안전하게 쓰는 것."),
      ("tip", "Table 19-4에서 thermogenin = “갈색지방 내막에 양성자 전도 통로를 만듦” → 짝풀림제 칸.")],
one="갈색지방 = 미토 가득 + UCP1(thermogenin) H⁺ 통로 → 짝풀림 → 열. 신생아의 난로!"),

dict(t="c", id="c-p450", part=P, title="시토크롬 P-450 — 해독과 스테로이드 합성의 ‘산소 붙이기’ 효소", sub="(2) Detoxification · (3) Steroid synthesis · Slides 74–76",
core="P-450은 O<sub>2</sub> 분자에서 산소 원자 하나는 기질에(R–H → <b>R–OH</b>), 하나는 물에 넣는 <b>혼합기능 산화효소</b>. 간에선 약물 해독, 부신 미토콘드리아에선 스테로이드 수산화.",
detail="""<p><b>② Detoxification (해독)</b> — 소포체·간의 P-450, 약물 대사의 ‘1차 방어선’</p>
<ul><li>지용성 약물·독성물질에 <b>산소를 붙여(oxygenation)</b> 물에 잘 녹게 → 소변·담즙으로 <b>배설</b>.</li>
<li>가끔 <pk>더 독한 물질</pk>을 만듦: <b>Tylenol (타이레놀, 아세트아미노펜)</b> → <b>CYP2E1</b> → <b>NAPQI</b>(N-Acetyl-p-BenzoQuinone Imine, N-아세틸-p-벤조퀴논이민) → 간 독성 (과량·음주 시).</li></ul>
<p><b>③ Steroid synthesis (스테로이드 합성)</b> — <b>부신 미토콘드리아</b>(스테로이드 합성에 특화, 내막 주름이 많음)의 P-450이 콜레스테롤 측쇄 절단, 11β-·18-수산화 등.</p>
<p><b>부신 P-450의 전자 경로</b>(슬라이드 76):</p>
<p><span class="fx">NADPH → 아드레노독신 환원효소(FAD) → 아드레노독신(2Fe-2S) → P-450 → O<sub>2</sub> + R–H</span></p>
<p>P-450 수산화효소는 <b>O<sub>2</sub>와 기질(R–H)에 직접</b> 작용해 <b>H<sub>2</sub>O와 R–OH</b>를 만든다.</p>
<div class="term">＊[용어: P-450 = 환원된 상태에서 CO와 결합하면 <b>450 nm</b> 빛을 흡수하는 색소(Pigment)라 붙은 이름]</div>
<div class="term">＊[용어: 수산화(hydroxylation) = 분자에 –OH를 붙이는 반응]</div>""",
formula="""<span class="fx">R–H + O<sub>2</sub> + NADPH + H<sup>+</sup> → R–OH + H<sub>2</sub>O + NADP<sup>+</sup></span> &nbsp; (혼합기능 산화: O 하나는 R에, 하나는 물에)""",
side=[("img", 76, "원본 슬라이드 76 — 부신 P-450: NADPH → 아드레노독신 환원효소 → 아드레노독신 → P-450", 150),
      ("ana", "P-450 = <b>손잡이 달아 주는 기계</b>. 기름 덩어리(지용성 약)에 –OH 손잡이를 달면 물(소변)로 씻겨 나간다. 가끔 손잡이를 잘못 달아 더 위험한 물건(NAPQI)이 되기도."),
      ("trap", "부신 P-450 전자 공급원은 <b>NADPH</b>(NADH 아님!). 순서: 환원효소(<b>FAD</b>) → 아드레노독신(<b>Fe-S</b>) → P-450.")],
one="P-450 = O₂의 O 하나를 R–H에 붙여 R–OH. 간: 해독(가끔 NAPQI), 부신 미토: 스테로이드. 전자는 NADPH → FAD → Fe-S → P-450."),

dict(t="c", id="c-apop", part=P, title="세포자멸사 — 미토콘드리아가 ‘자폭 버튼’ 시토크롬 c를 쥐고 있다", sub="(4) Apoptosis: programmed cell death · Role of cytochrome c · Slide 77",
core="스트레스·DNA 손상이 오면 미토콘드리아 외막이 열려 <b>시토크롬 c</b>가 세포질로 나온다 → <b>Apaf-1 + ATP</b>와 결합해 <b>apoptosome</b> → <b>caspase-9</b> → <b>caspase-3·7</b> → 세포 죽음.",
detail="""<p><b>Apoptosis (아폽토시스, 세포자멸사)</b> = 세포가 프로그램에 따라 스스로 깔끔하게 죽는 것 (발생, 손상된 세포 제거). 괴사(necrosis)처럼 터지지 않아 염증이 없다.</p>
<ol><li>신호: DNA 손상, 발생 신호, 스트레스, ROS</li>
<li><b>Permeability transition pore complex(투과성 전이 구멍 복합체)</b>가 열림 → 미토 팽창 → <b>cyt c</b>가 세포질로 방출</li>
<li>cyt c + <b>Apaf-1</b>(Apoptosis Protease Activating Factor-1, 아폽토시스 프로테이스 활성 인자 1) + <b>ATP</b> → 7개가 모인 바퀴 모양 <b>apoptosome(아폽토좀)</b></li>
<li>apoptosome이 <b>procaspase-9</b>(비활성) 이량체화 → <b>caspase-9</b>(활성)</li>
<li>caspase-9가 <b>procaspase-3, -7</b>을 잘라 활성화 → 세포 단백질 분해 → 세포 죽음과 흡수</li></ol>
<div class="term">＊[용어: caspase(카스페이스) = Cysteine-dependent ASPartate-specific proteASE. 아스파르트산 뒤를 자르는 단백질 분해효소. ‘pro-’가 붙으면 아직 잠든 형태]</div>""",
side=[("img", 77, "원본 슬라이드 77 — cyt c 방출 → Apaf-1 + ATP → apoptosome → caspase-9 → caspase-3/7", 210),
      ("ana", "평소 cyt c는 발전소(미토) 안의 <b>배달원</b>이지만, 밖으로 나오면 <b>자폭 버튼</b>. 버튼(cyt c) + 경비(Apaf-1) + 배터리(ATP) = 폭탄 조립(apoptosome) → 도화선 caspase-9 → 폭약 caspase-3·7."),
      ("tip", "같은 분자 cyt c의 <b>두 얼굴</b>: 막사이공간 = 전자 운반, 세포질 = 세포자멸사 신호.")],
one="cyt c 방출 → +Apaf-1 +ATP → apoptosome → caspase-9 → caspase-3·7 → 깔끔한 자살."),

dict(t="c", id="c-mtdna", part=P, title="미토콘드리아 유전체 — 엄마에게서만 오고, 평생 돌연변이가 쌓인다", sub="19.5 Mitochondrial genes · LHON · MERRF · Heteroplasmy · Slides 82–86, 88",
core="미토콘드리아 DNA(mtDNA)는 <b>모계 유전</b>, ROS가 많고 수선은 약해 <b>평생 돌연변이가 쌓인다</b>. 한 세포 안에 정상·돌연변이 mtDNA가 섞인 <b>이형세포질성(heteroplasmy)</b> 때문에 증상의 정도가 사람마다 다르다.",
detail="""<ul><li>사람 mtDNA: 원형 16,569 bp, <b>37개 유전자</b> = 단백질 13개(Complex I의 ND1–6·ND4L, III의 cyt b, IV의 COI–III, ATP 합성효소 ATPase6·8) + tRNA 22 + rRNA 2. 나머지 미토 단백질은 핵 유전자.</li>
<li><b>모계 유전</b>: 정자의 미토콘드리아는 수정 후 난자가 파괴 → 자녀의 미토는 <b>모두 엄마 것</b>. → <b>mitochondrial encephalomyopathies (미토콘드리아 뇌근육병증)</b>: 뇌와 골격근에 주로 영향, 항상 모계로 유전.</li>
<li><b>LHON</b>(Leber's Hereditary Optic Neuropathy, 레버 유전성 시신경병증): <b>ND4(Complex I)</b> 또는 <b>cyt b</b>의 <b>염기 하나 변화</b> → 중추신경(시신경) ATP 부족 → <b>실명</b>.</li>
<li><b>MERRF</b>(Myoclonic Epilepsy and Ragged-Red Fiber disease, 근간대성 간질 및 누더기 적색 섬유병): <b>tRNA<sup>Lys</sup></b> 돌연변이(8344) → 미토 단백질 합성 이상 → 비정상 미토(결정 모양 봉입체) → <b>근력 약화 · 통제 안 되는 근육 경련</b>.</li>
<li><b>Heteroplasmy (헤테로플라즈미, 이형세포질성)</b>: 세포 분열 때 미토가 <b>무작위로</b> 나뉨 → 딸세포마다 돌연변이 비율이 다름 → 같은 돌연변이라도 <b>증상의 경중이 다양</b>. 모두 같으면 homoplasmy(호모플라즈미).</li>
<li><b>노화 이론</b>: 미토 손상 누적 → 골격근·심장근 약화.</li>
<li><b>내공생설(endosymbiotic origin)</b>: 미토콘드리아는 옛날 진핵세포 조상에 들어온 <b>호기성 세균</b> → 자체 원형 DNA, 세균형 리보솜, 이중막 (슬라이드 88).</li></ul>""",
side=[("img", 84, "원본 슬라이드 84 — LHON(ND4·cyt b → 실명)과 MERRF(tRNA^Lys → 근육 경련)", 165),
      ("img", 86, "원본 슬라이드 86 — 이형세포질성: 딸세포마다 돌연변이 비율이 다르다", 140),
      ("ana", "미토 = <b>엄마가 물려준 구슬 주머니</b>. 주머니 속에 흰 구슬(정상)과 검은 구슬(돌연변이)이 섞여 있는데, 세포가 나뉠 때 <b>한 움큼씩 무작위로</b> 나눠 담는다 → 어떤 아이는 검은 구슬이 많아 증상이 심하다.")],
one="mtDNA = 엄마 것만, 37유전자(단백질 13). LHON = ND4/cyt b → 실명, MERRF = tRNA^Lys → 근육 경련. 이형세포질성 → 증상 제각각."),

dict(t="c", id="c-beta", part=P, title="췌장 β세포의 미토 결함 → 당뇨병", sub="Defective oxidative phosphorylation in pancreatic β cells blocks insulin secretion · Slide 87",
core="β세포는 <b>포도당 → 산화적 인산화 → ATP ↑</b>를 ‘혈당 센서’로 쓴다. ATP가 K<sup>+</sup> 통로를 닫아야 인슐린이 나오므로, 미토가 고장 나면 <b>인슐린 분비가 막혀 당뇨</b>가 된다.",
detail="""<ol><li>혈당 ↑ → GLUT2(포도당 수송체)로 포도당 유입 → <b>glucokinase(글루코키나아제)</b>로 인산화 → 해당 → 피루브산 → <b>미토 호흡</b> → <b>[ATP] ↑</b></li>
<li>ATP가 <b>ATP 개폐 K<sup>+</sup> 통로</b>를 <b>닫음</b> → K<sup>+</sup>가 못 나가 → 막 <b>탈분극</b></li>
<li>탈분극 → <b>전압 개폐 Ca<sup>2+</sup> 통로</b> 열림 → Ca<sup>2+</sup> 유입</li>
<li>Ca<sup>2+</sup> ↑ → <b>인슐린 과립 세포외배출</b> → 혈중 인슐린 ↑</li></ol>
<p>산화적 인산화 결함(mtDNA 돌연변이 등) → ATP 충분히 못 올라감 → K<sup>+</sup> 통로가 안 닫힘 → <b>인슐린 분비 ↓</b> → 당뇨. 예: glucokinase 한쪽 결함 = <b>MODY2</b>(Maturity-Onset Diabetes of the Young, 젊은이의 성인형 당뇨, 경증), 양쪽 결함 = 심한 신생아 당뇨 (원서 문제 23).</p>
<div class="term">＊[용어: 탈분극 = 세포막 안쪽의 (−) 전하가 줄어드는 것. ‘문 열어라’ 신호]</div>""",
side=[("img", 87, "원본 슬라이드 87 — β세포: 포도당 → ATP → K⁺ 통로 닫힘 → Ca²⁺ → 인슐린", 230),
      ("ana", "β세포 = <b>ATP 저울 달린 자동문</b>. 포도당이 많이 들어오면 미토가 ATP를 잔뜩 쌓아 저울이 기울고, 그게 K<sup>+</sup> 문을 닫아 → 인슐린 문이 열린다. 미토(저울)가 고장 나면 문이 안 열려.")],
one="포도당 → 미토 ATP ↑ → K⁺(ATP) 통로 닫힘 → 탈분극 → Ca²⁺ ↑ → 인슐린. 미토 고장 = 당뇨."),

# ───────────────────────────── 문제
dict(t="q", id="q-p450", part=P, kind=["chk", "bl"], title="부신 미토콘드리아 P-450의 전자 경로", src="개념확인 · 빈칸 · 슬라이드 76",
q="""부신 미토콘드리아의 스테로이드 수산화 반응에서 전자는<br>
<span class="blank">(가)</span> → 아드레노독신 환원효소(<span class="blank">(나)</span>) → 아드레노독신(<span class="blank">(다)</span>) → P-450 수산화효소 순으로 흐른다.<br>
P-450은 O<sub>2</sub>와 기질 R–H에 직접 작용해 <span class="blank">(라)</span>와 H<sub>2</sub>O를 만든다.<br>
간에서 타이레놀은 CYP2E1에 의해 독성 물질 <span class="blank">(마)</span>로 바뀔 수 있다.""",
a="(가) NADPH (나) FAD (다) 2Fe-2S (철-황 중심) (라) R–OH (마) NAPQI",
steps=[("공급원 = <b>NADPH</b> (생합성·해독용 환원력)", "NADH는 주로 ATP 생산용, NADPH는 만들기·해독용."),
       ("2전자(NADPH) → <b>FAD</b>(변압기) → 1전자 운반체 <b>Fe-S</b> → P-450의 헴", "호흡사슬의 NADH → FMN → Fe-S와 같은 패턴."),
       ("혼합기능 산화: R–H + O<sub>2</sub> → <b>R–OH</b> + H<sub>2</sub>O", ""), ("NAPQI = N-아세틸-p-벤조퀴논이민", "")],
one="NADPH → FAD → Fe-S → P-450 → R–OH. 타이레놀 과량 → NAPQI."),

dict(t="q", id="q-apop", part=P, kind=["chk", "mc"], title="세포자멸사 순서 맞추기", src="개념확인 · 슬라이드 77",
q="미토콘드리아가 시작하는 세포자멸사 과정의 순서로 옳은 것은?<br>(가) caspase-3·7 활성화 &nbsp;(나) 투과성 전이 구멍이 열려 cyt c가 세포질로 &nbsp;(다) cyt c + Apaf-1 + ATP → apoptosome &nbsp;(라) procaspase-9 → caspase-9" + opts(
"(가) → (나) → (다) → (라)", "(나) → (다) → (라) → (가)", "(나) → (라) → (다) → (가)", "(다) → (나) → (가) → (라)", "(라) → (다) → (나) → (가)"),
a="②",
steps=[("방아쇠: 스트레스·DNA 손상 → 구멍 열림 → <b>cyt c 방출</b>(나)", ""),
       ("조립: cyt c + Apaf-1 + ATP = <b>apoptosome</b>(다)", ""),
       ("개시 카스페이스: <b>caspase-9</b>(라) → 실행 카스페이스: <b>caspase-3·7</b>(가)", "9가 먼저 켜져서 3·7을 깨운다.")],
one="cyt c 방출 → apoptosome → caspase-9 → caspase-3·7."),

dict(t="q", id="q-mtdisease", part=P, kind=["chk", "multi"], title="미토콘드리아 유전병 — 맞는 것 모두", src="개념확인 · 다답형 · 슬라이드 83–86",
q="미토콘드리아 유전과 질환에 대한 설명으로 <b>옳은 것을 모두</b> 고르시오." + opts(
"포유류에서 미토콘드리아는 대개 어머니에게서만 유전된다.",
"LHON은 Complex I의 ND4 또는 cyt b 유전자의 염기 하나 변화로 시신경이 손상되어 실명에 이른다.",
"MERRF는 tRNA<sup>Lys</sup> 돌연변이로 비정상 미토콘드리아가 생기며 근력 약화와 근육 경련을 보인다.",
"미토콘드리아는 ROS 생성이 적고 DNA 수선 능력이 뛰어나 돌연변이가 잘 쌓이지 않는다.",
"이형세포질성 때문에 같은 mtDNA 돌연변이를 가진 사람들의 증상 정도가 다를 수 있다."),
a="①, ②, ③, ⑤",
opx=ox(("①", True, "정자의 미토는 수정 후 난자가 파괴."), ("②", True, "슬라이드 84."), ("③", True, "ragged-red fiber = 누더기 적색 섬유."),
       ("④", False, "반대: ROS <b>많고</b> 수선 <b>약해</b> 평생 쌓인다."), ("⑤", True, "원서 문제 22의 답.")),
one="모계 · LHON(ND4/cyt b, 실명) · MERRF(tRNA^Lys, 근육) · ROS↑ 수선↓ · 이형세포질성."),

dict(t="q", id="q-hetero", part=P, kind=["txt", "sa"], title="같은 돌연변이인데 왜 누구는 가볍고 누구는 심할까?", src="원서(5판) 19장 연습문제 20 · 솔루션 수록",
en="Different individuals with a disease caused by the same specific defect in the mitochondrial genome may have symptoms ranging from mild to severe. Explain why.",
q="미토콘드리아 유전체의 똑같은 결함으로 생긴 질환인데도 사람마다 증상이 가벼운 것부터 심한 것까지 다양하다. 이유를 설명하시오.",
a="이형세포질성(heteroplasmy) 때문 — 한 세포 안에 정상과 돌연변이 mtDNA가 섞여 있고, 세포 분열 때 무작위로 나뉘어 조직·사람마다 돌연변이 비율이 달라진다. 비율이 높은 조직(특히 에너지를 많이 쓰는 뇌·근육)일수록 증상이 심하다.",
steps=[("세포 하나에 미토 수백~수천 개, 각자 mtDNA 여러 벌", ""),
       ("난자 → 배아 → 조직으로 나뉠 때 미토가 <b>무작위 분배</b> → 돌연변이 비율 제각각", "구슬 주머니 비유."),
       ("<b>문턱(threshold)</b> 이상의 비율이 된 조직에서만 ATP 부족 → 증상. 에너지 수요가 큰 뇌·근육·심장이 먼저", "")],
one="이형세포질성 + 무작위 분배 + 조직별 문턱 → 증상 스펙트럼."),

dict(t="q", id="q-mody", part=P, kind=["txt", "sa"], title="글루코키나아제 결함 한쪽 vs 양쪽", src="원서(5판) 19장 연습문제 24 · 솔루션 수록",
en="Glucokinase is essential in the metabolism of glucose in pancreatic β cells. Humans with two defective copies of the glucokinase gene exhibit a severe, neonatal diabetes, whereas those with only one defective copy have a much milder form (MODY2). Explain in terms of the biology of the β cell.",
q="췌장 β세포에서 글루코키나아제 유전자가 양쪽 모두 결함이면 심한 신생아 당뇨, 한쪽만 결함이면 가벼운 MODY2가 된다. β세포 생물학으로 설명하시오.",
a="β세포는 글루코키나아제가 만드는 포도당 대사 → 미토 ATP 증가로 혈당을 감지한다. 양쪽 결함이면 포도당 → ATP 신호가 거의 없어 인슐린이 나오지 않고, 한쪽 결함이면 효소량이 절반이라 더 높은 혈당에서야 충분한 ATP가 만들어져 인슐린 분비 문턱만 올라간다.",
steps=[("글루코키나아제 = β세포의 <b>포도당 센서</b>(K<sub>m</sub>이 높아 혈당에 비례해 작동)", ""),
       ("포도당 → 해당 → 미토 산화적 인산화 → ATP ↑ → K<sub>ATP</sub> 통로 닫힘 → 인슐린 분비", ""),
       ("양쪽 결함: ATP ↑ 신호 없음 → 인슐린 거의 0 → 심한 당뇨", ""),
       ("한쪽 결함: 효소 50% → 같은 ATP를 만들려면 <b>혈당이 더 높아야</b> → 분비 문턱 ↑ → 경미한 고혈당(MODY2)", "")],
one="β세포 혈당 센서 = 글루코키나아제 → 미토 ATP. 효소 0% = 신생아 당뇨, 50% = 문턱만 올라간 MODY2."),
]
