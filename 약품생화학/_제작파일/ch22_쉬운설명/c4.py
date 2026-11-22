PAGES = [
dict(img=73, slide=73, title="IMP에서 AMP와 GMP 만들기", sub="Biosynthesis of AMP and GMP from inosine monophosphate (IMP)",
kw=["AMP 쪽: Asp + GTP", "GMP 쪽: NAD⁺ + Gln + ATP", "아데닐로숙신산", "잔틸산(XMP)", "엇갈린 에너지"],
sum="IMP → AMP: Asp의 N을 붙이고(GTP 사용) 푸마르산을 뗀다. IMP → GMP: 먼저 산화해 XMP(NAD⁺) → Gln의 N을 붙인다(ATP 사용). AMP 만들 땐 GTP, GMP 만들 땐 ATP를 쓴다.",
tr="""<p><b>이노신 일인산(IMP)으로부터 AMP와 GMP의 생합성</b></p>
<ul><li>IMP + <b>아스파르트산</b> + GTP → (<b>아데닐로숙신산 합성효소</b>, GDP + Pᵢ) <b>아데닐로숙신산</b> → (<b>아데닐로숙신산 분해효소</b>, 푸마르산) <b>아데닐산 (AMP)</b></li>
<li>IMP + H₂O + NAD⁺ → (<b>IMP 탈수소효소</b>, NADH + H⁺) <b>잔틸산 (XMP)</b> → + <b>Gln</b> + ATP + H₂O (<b>XMP-글루타민 아마이드기 전달효소</b>, Glu + AMP + PPᵢ) → <b>구아닐산 (GMP)</b></li></ul>""",
ex="""<table class="t"><tr><th></th><th>IMP → AMP</th><th>IMP → GMP</th></tr>
<tr><td>N 출처</td><td><b>Asp</b> (푸마르산으로 빠짐)</td><td><b>Gln</b> 아마이드 N</td></tr>
<tr><td>에너지</td><td><b>GTP</b></td><td><b>ATP</b></td></tr>
<tr><td>바뀌는 자리</td><td>6번 C=O → –NH₂</td><td>2번 산화(=O) → –NH₂</td></tr></table>
<p><y>엇갈린 에너지 사용</y>: A를 만들려면 G가, G를 만들려면 A가 있어야 → 두 뉴클레오타이드가 <b>균형</b> 있게 만들어져.</p>
<div class="box"><span class="tag">약학</span><b>IMP 탈수소효소 억제제</b>: <b>마이코페놀산</b>(면역억제제, 장기이식 — 림프구는 구제 경로가 약해 특히 민감), <b>리바비린</b>(항바이러스). Asp가 들어갔다 푸마르산으로 나가는 패턴은 요소 회로·퓨린 8단계와 같아.</div>"""),

dict(img=74, slide=74, title="E. coli의 아데닌 · 구아닌 뉴클레오타이드 합성 조절", sub="Regulatory mechanisms in the biosynthesis of adenine and guanine nucleotides in E. coli",
kw=["PRPP 합성효소 ⊣ ADP", "글루타민-PRPP 아마이드기 전달효소 ⊣ AMP · GMP · IMP", "갈림길: AMP ⊣ AMP 쪽, GMP ⊣ GMP 쪽"],
sum="세 겹의 되먹임: ① PRPP 합성효소는 ADP가 억제 ② 첫 전념 단계(글루타민-PRPP 아마이드기 전달효소)는 AMP·GMP·IMP가 억제 ③ 갈림길에서 AMP는 아데닐로숙신산 합성효소를, GMP는 IMP 탈수소효소를 억제.",
tr="""<p><b>E. coli에서 아데닌과 구아닌 뉴클레오타이드 생합성의 조절 메커니즘</b></p>
<ul><li>리보스 5-인산 → (<b>리보스 인산 피로인산키네이스, PRPP 합성효소</b>) PRPP ⊣ <b>ADP</b></li>
<li>PRPP → (<b>글루타민-PRPP 아마이드기 전달효소</b>) 5-포스포리보실아민 ⊣ <b>AMP, GMP, IMP</b></li>
<li>→ (9단계) IMP → (아데닐로숙신산 합성효소 ⊣ <b>AMP</b>) 아데닐로숙신산 → AMP</li>
<li>IMP → (IMP 탈수소효소 ⊣ <b>GMP</b>) XMP → GMP</li></ul>
<p><b>PRPP</b>: <b>P</b>hospho<b>r</b>ibosyl <b>p</b>yro<b>p</b>hosphate (포스포리보실 피로인산)</p>""",
ex="""<p>1단계 효소에는 AMP 자리와 GMP 자리가 따로 있어서 둘 다 많을 때 <y>협동적으로 강하게 억제</y>돼.</p>
<p>갈림길에서는 각자 자기 길만 막아 → 한쪽만 많으면 다른 쪽으로 흐름이 넘어가 균형 유지.</p>
<div class="box"><span class="tag">임상</span><b>PRPP 합성효소 과활성</b>이나 PRPP 증가(HGPRT 결핍, 슬라이드 86)는 퓨린 과다 생산 → 요산 ↑ → <b>통풍</b>. 조절 그림이 통풍 기전과 연결돼.</div>"""),

dict(img=75, slide=75, title="암세포는 뉴클레오타이드가 더 필요하다 — 글루타민 흉내 항암제", sub="Glutamine-mimic nucleotide biosynthesis inhibitors as chemotherapeutic agents",
kw=["아자세린", "아시비신", "글루타민 아마이드기 전달효소 억제", "비가역 (공유결합)"],
sum="빨리 분열하는 암세포는 뉴클레오타이드를 많이 만들어야 한다. 아자세린·아시비신은 글루타민을 닮아 글루타민 아마이드기 전달효소의 활성 부위에 들어가 Cys와 공유결합해 효소를 영구히 망가뜨린다.",
tr="""<p><b>암세포는 더 많은 뉴클레오타이드가 필요하다: 글루타민을 흉내 내는 뉴클레오타이드 생합성 억제제를 항암제로</b></p>
<p>그림: 글루타민 · <b>아자세린</b> · <b>아시비신</b> (분홍 = 글루타민 아마이드 부분과 닮은 곳)</p>
<p><b>아자세린과 아시비신 — 글루타민 아마이드기 전달효소의 억제제</b></p>""",
ex="""<ul><li><b>아자세린</b>: 다이아조기(N=N⁺=N⁻)가 반응성 → 활성 부위 <b>Cys–SH</b>를 알킬화(슬라이드 15의 그 Cys!).</li>
<li><b>아시비신</b>: 염소 달린 고리가 같은 Cys와 반응.</li></ul>
<p>글루타민 아마이드기 전달효소는 퓨린 합성 1·4단계, GMP 합성, CTP 합성(슬라이드 76), 카바모일 인산 합성효소 II까지 여러 곳 → <y>한 번에 여러 단계를 막음</y>.</p>
<div class="box"><span class="tag">시험</span>원리 정리: <b>항암 대사길항제 = 정상 기질(글루타민·엽산·염기)을 닮은 가짜</b>. 부작용은 빠르게 분열하는 정상 세포(골수, 장 점막, 모낭)에서 → 골수 억제, 구내염, 탈모.</div>"""),

dict(img=76, slide=76, title="피리미딘 뉴클레오타이드의 새로 합성 — 오로트산 경유 UTP · CTP", sub="De novo synthesis of pyrimidine nucleotides: biosynthesis of UTP and CTP via orotidylate",
kw=["카바모일 인산 + Asp", "아스파르트산 트랜스카바모일레이스(ATCase)", "오로트산", "PRPP는 나중에", "CTP 합성효소 (Gln)", "기질 채널링"],
sum="카바모일 인산 + Asp → (ATCase) N-카바모일아스파르트산 → 고리 닫기 → 다이하이드로오로트산 → (산화) 오로트산 → PRPP에 붙여 OMP → 탈카복실화 → UMP → 인산화 UTP → (Gln의 N) CTP. 피리미딘은 고리를 먼저 짓고 나중에 리보스에 붙인다.",
tr="""<p><b>피리미딘 뉴클레오타이드의 새로 합성: 오로티딜산을 거친 UTP와 CTP의 생합성</b></p>
<ol><li>CO₂ + NH₄⁺(세균) → <b>카바모일 인산</b> (카바모일 인산 합성효소)</li>
<li>+ <b>아스파르트산</b> → (<b>아스파르트산 트랜스카바모일레이스</b>, Pᵢ) N-카바모일아스파르트산</li>
<li>→ (<b>다이하이드로오로테이스</b>, H₂O) L-다이하이드로오로트산</li>
<li>→ (<b>다이하이드로오로트산 탈수소효소</b>, NAD⁺) <b>오로트산</b></li>
<li>+ <b>PRPP</b> → (<b>오로트산 포스포리보실전달효소</b>, PPᵢ) <b>오로티딜산 (OMP)</b></li>
<li>→ (<b>오로티딜산 탈카복실화효소</b>, CO₂) <b>유리딜산 (UMP)</b></li>
<li>→ (키네이스, 2ATP) <b>UTP</b> → (<b>사이티딜산 합성효소</b>, Gln + ATP) <b>CTP</b> (점선 ⊣ ATCase)</li></ol>
<p>오른쪽: <b>세균 카바모일 인산 합성효소에서 중간체의 채널링</b> (효소 안 터널, 약 96 Å)</p>""",
ex="""<table class="t"><tr><th></th><th>퓨린</th><th>피리미딘</th></tr>
<tr><td>PRPP는 언제?</td><td><b>처음부터</b> (그 위에 고리 조립)</td><td><b>고리 완성 후</b> (오로트산 + PRPP)</td></tr>
<tr><td>첫 산물</td><td>IMP</td><td>UMP</td></tr></table>
<p>사람은 카바모일 인산 합성효소 <b>II</b>(세포질, Gln 사용)를 쓰고, 처음 세 효소가 한 단백질(<b>CAD</b>)로 묶여 있어. 요소 회로의 CPS <b>I</b>(미토콘드리아, NH₃)과 구분!</p>
<div class="box"><span class="tag">약학·임상</span>다이하이드로오로트산 탈수소효소 억제제 <b>레플루노마이드</b>(류마티스 관절염), <b>오로트산뇨증</b>(UMP 합성효소 결핍) → <b>유리딘</b> 투여로 치료. 오로트산이 소변에 많으면 요소 회로 결함(OTC 결핍)도 의심.</div>"""),

dict(img=77, slide=77, title="ATCase의 알로스테릭 조절 — CTP와 ATP", sub="Allosteric regulation of aspartate transcarbamoylase by CTP and ATP",
kw=["S자 곡선", "CTP = 억제 (K₀.₅ 12 → 23 mM)", "ATP = 활성화", "피리미딘·퓨린 균형"],
sum="ATCase는 S자(시그모이드) 곡선의 대표 알로스테릭 효소. 최종 산물 CTP가 붙으면 Asp에 대한 K₀.₅가 12 → 23 mM로 올라 느려지고(억제), 퓨린인 ATP가 붙으면 그 억제가 풀린다.",
tr="""<p><b>CTP와 ATP에 의한 아스파르트산 트랜스카바모일레이스의 알로스테릭 조절</b></p>
<p>그래프: 가로축 [아스파르트산] (mM), 세로축 V₀ (µM/min)</p>
<ul><li><b>정상 활성 (CTP 없음)</b>: K₀.₅ = <b>12 mM</b></li><li><b>CTP + ATP</b>: 정상에 가까움</li><li><b>CTP</b>: K₀.₅ = <b>23 mM</b> (곡선이 오른쪽으로)</li></ul>""",
ex="""<p>S자 곡선 = 활성 부위끼리 <y>협동성</y>(기질 하나가 붙으면 다음이 쉽게 붙음). 효소는 촉매 소단위체 6 + 조절 소단위체 6.</p>
<ul><li><b>CTP</b>(피리미딘 최종 산물): T(덜 활성) 상태 안정화 → 같은 [Asp]에서 속도 ↓ — <b>되먹임 억제</b>.</li>
<li><b>ATP</b>(퓨린): R(활성) 상태 안정화 → “퓨린이 많으니 짝 맞출 피리미딘을 더 만들어라”.</li></ul>
<div class="box"><span class="tag">시험</span>K₀.₅(반최대 속도의 기질 농도)가 <b>커지면 억제</b>, Vmax는 거의 같음. 그래프 읽기 문제(“CTP는 K₀.₅를 증가시킨다” O) 단골. 5장 알로스테릭 효소의 교과서 예시.</div>"""),

dict(img=78, slide=78, title="리보뉴클레오타이드 환원효소 (RNR)", sub="Ribonucleotide reductase",
kw=["NDP → dNDP", "2′-OH → 2′-H", "DNA 재료"],
sum="DNA의 재료(데옥시뉴클레오타이드)는 따로 만들지 않고, RNA용 리보뉴클레오타이드 이인산(NDP)의 2′-OH를 H로 바꿔(환원) 만든다. 이 일을 하는 효소가 리보뉴클레오타이드 환원효소.",
tr="""<p><b>리보뉴클레오타이드 환원효소</b></p>
<p>리보뉴클레오타이드 이인산 (RNA, 2′-<b>OH</b>) → 데옥시리보뉴클레오타이드 이인산 (DNA, 2′-<b>H</b>)</p>""",
ex="""<ul><li>기질은 <b>이인산(NDP: ADP, GDP, CDP, UDP)</b> — 일인산·삼인산이 아님(세균 일부 제외).</li>
<li>4가지 dNDP를 <b>한 효소</b>가 다 만들어 → 균형 조절이 정교해야 함(슬라이드 82–83).</li>
<li>dTTP는 여기서 바로 안 나오고 dUDP → dUMP → <b>dTMP</b>(슬라이드 84) 길로.</li></ul>
<div class="box"><span class="tag">약학</span>RNR 억제제 <b>하이드록시유레아</b>: 라디칼(Tyr•)을 없애 효소를 끔 → 백혈병, 겸상적혈구병 치료. <b>젬시타빈</b>(이인산형)도 RNR을 비가역 억제.</div>"""),

dict(img=79, slide=79, title="NDP → dNDP 환원의 전자 공급", sub="Reduction of ribonucleotides to deoxyribonucleotides by ribonucleotide reductase",
kw=["NADPH", "글루타레독신 (GSH)", "티오레독신 (FAD)", "효소의 –SH 두 개"],
sum="RNR은 자기 Cys 두 개(–SH HS–)의 전자를 써서 NDP를 환원하고 S–S가 된다. 다시 –SH로 돌려놓는 전자는 NADPH에서 (a) 글루타티온 → 글루타레독신 또는 (b) FAD → 티오레독신을 거쳐 온다.",
tr="""<p><b>리보뉴클레오타이드 환원효소에 의한 리보뉴클레오타이드 → 데옥시리보뉴클레오타이드 환원</b></p>
<p>전자는 NADPH로부터 (a) <b>글루타레독신</b> 또는 (b) <b>티오레독신</b>을 거쳐 효소로 전달된다(파란 화살표).</p>
<ul><li>(a) NADPH → (<b>글루타티온 환원효소</b>) GSSG → 2GSH → (<b>글루타레독신 환원효소</b>) 글루타레독신(SH)₂ → RNR(S–S → SH SH)</li>
<li>(b) NADPH → FAD → FADH₂ → (<b>티오레독신 환원효소</b>) 티오레독신(SH)₂ → RNR</li>
<li>RNR(SH)₂ + NDP → RNR(S–S) + dNDP + H₂O</li></ul>""",
ex="""<p>전자 릴레이: <span class="eq">NADPH → (GSH → 글루타레독신 또는 FAD → 티오레독신) → RNR –SH → 2′-탄소</span></p>
<p>여기서도 <y>NADPH</y>가 생합성의 환원력(21장 지방산 합성과 같음). NADPH의 주 공급원은 오탄당 인산 경로 → 분열 세포에서 PPP가 활발한 이유.</p>
<div class="boxg">글루타티온(슬라이드 62)이 여기서도 등장 — 환원제로서 <g>DNA 합성까지 돕는다</g>.</div>"""),

dict(img=80, slide=80, title="리보뉴클레오타이드 환원효소의 구조", sub="Ribonucleotide reductase: R1 and R2 subunits",
kw=["R1 (α): 활성 부위 + 조절 자리 2개", "R2 (β): Tyr 라디칼 + 2Fe³⁺", "티로실 라디칼 → 티일 라디칼"],
sum="R1 소단위체 2개에 활성 부위(–SH)와 두 조절 자리(기질 특이성 자리, 주 조절 자리)가 있고, R2 소단위체 2개에 철 두 개가 지켜 주는 티로실 라디칼(Tyr–O•)이 있다. 이 라디칼이 활성 부위 Cys를 –S•로 만들어 반응을 시작한다.",
tr="""<p><b>리보뉴클레오타이드 환원효소</b></p>
<ul><li><b>조절 자리</b>: <b>기질 특이성 자리</b>(ATP, dATP, dGTP, dTTP) · <b>주 조절 자리</b>(ATP, dATP) — 알로스테릭 효과인자</li>
<li><b>활성 부위</b>: HS HS, XH — 기질 ADP, CDP, UDP, GDP</li>
<li><b>R1 소단위체</b> ×2, <b>R2 소단위체</b> ×2 (Fe³⁺–O–Fe³⁺, 티로실 라디칼)</li>
<li>HX: Cys의 HS</li></ul>
<p class="eq">Tyr–O• + –XH ⇌ Tyr–OH + –X•</p>
<p><b>티로실 라디칼이 활성 부위 라디칼(—X•, —S•)을 만든다</b></p>""",
ex="""<p>라디칼(홀전자)은 보통 위험한데, 이 효소는 그걸 <y>촉매 도구</y>로 써. 2′-OH 같은 안 움직이는 C–H/C–OH를 다루려면 라디칼만큼 센 반응성이 필요해서야.</p>
<ul><li>R2: 철 2개(이핵 철 중심)가 O₂를 써서 Tyr122에 라디칼을 만들고 안정하게 보관.</li>
<li>라디칼은 R2 → R1으로 약 35 Å을 <b>전자 이동</b>으로 건너가 활성 부위 Cys를 –S•로.</li></ul>
<div class="box"><span class="tag">약학</span>하이드록시유레아 = <b>Tyr 라디칼 소거제</b>. 철 킬레이트제도 R2를 약하게 해 RNR 활성 ↓.</div>"""),

dict(img=81, slide=81, title="리보뉴클레오타이드 환원효소의 제안된 메커니즘", sub="Proposed mechanism for ribonucleotide reductase",
kw=["3′-라디칼", "2′-OH 양성자화 → H₂O 제거", "다이싸이올 → 다이설파이드", "라디칼 재생"],
sum="① –S•가 3′-H를 빼앗아 3′-라디칼 ② 2′-OH에 양성자가 붙고 ③ 물로 빠져 라디칼 안정화 탄소양이온 ④ 효소의 두 –SH가 전자 2개를 2′-탄소에 줘 S–S가 됨 ⑤ ①을 되돌려 3′-H 복귀, 라디칼 재생 ⑥ 티오레독신이 S–S를 다시 –SH로.",
tr="""<p><b>리보뉴클레오타이드 환원효소의 제안된 메커니즘</b></p>
<ol><li><b>3′-리보뉴클레오타이드 라디칼</b>이 형성된다.</li>
<li><b>2′-하이드록실기가 양성자화</b>된다.</li>
<li><b>H₂O가 제거</b>되어 라디칼로 안정화된 탄소양이온이 된다.</li>
<li><b>다이싸이올이 효소에서 산화</b>된다: 전자 두 개가 2′-탄소로 전달된다.</li>
<li><b>1단계가 거꾸로</b> 일어나 효소의 티로실(티일) 라디칼이 재생된다.</li>
<li>효소의 다이싸이올이 환원되어 한 회전이 끝난다 (티오레독신 또는 글루타레독신).</li></ol>""",
ex="""<p>핵심 아이디어: 2′-OH를 직접 공격하지 않고 <y>옆(3′) 탄소에 라디칼을 만들어</y> 2′-OH가 물로 쉽게 떠나게 해.</p>
<ul><li>라디칼은 반응 끝에 <b>되돌아가 재생</b> — 촉매처럼 다시 쓰임.</li>
<li>2′-위치에 새로 들어온 H는 효소의 <b>Cys –SH</b>에서, 그 전자는 결국 <b>NADPH</b>에서.</li></ul>
<div class="box"><span class="tag">시험</span>“RNR 반응에서 2′-OH는 <b>물(H₂O)</b>로 떨어져 나간다”, “효소의 두 Cys가 <b>S–S</b>로 산화된다”가 출제 포인트. 세부 화살표보다 6단계의 흐름을 말로 설명할 수 있으면 충분.</div>"""),

dict(img=82, slide=82, title="리보뉴클레오타이드 환원효소의 조절", sub="Regulation of ribonucleotide reductase",
kw=["주 조절 자리: ATP ON / dATP OFF", "기질 특이성 자리: 어떤 NDP를 환원할지", "R1 · R2"],
sum="RNR은 두 조절 자리로 조절된다: 주 조절 자리는 전체 ON/OFF(ATP = 켬, dATP = 끔), 기질 특이성 자리는 네 가지 NDP 중 무엇을 환원할지 고른다(ATP·dATP·dGTP·dTTP).",
tr="""<p><b>리보뉴클레오타이드 환원효소의 조절</b></p>
<ul><li>조절 자리: <b>기질 특이성 자리</b> (파란 원) · <b>주 조절 자리</b> (빨간 원)</li>
<li>알로스테릭 효과인자: ATP, dATP, dGTP, dTTP / ATP, dATP</li>
<li>활성 부위, R1 소단위체 ×2, R2 소단위체 ×2, 기질 ADP · CDP · UDP · GDP</li></ul>""",
ex="""<table class="t"><tr><th>자리</th><th>무엇이 붙나</th><th>효과</th></tr>
<tr><td><b>주 조절 자리</b> (활성 스위치)</td><td>ATP / dATP</td><td>ATP → <g>전체 활성</g>, dATP → <pk>전체 억제</pk></td></tr>
<tr><td><b>기질 특이성 자리</b> (메뉴 선택)</td><td>ATP·dATP / dTTP / dGTP</td><td>어떤 NDP를 받을지 바꿈 (다음 슬라이드)</td></tr></table>
<p>목적: DNA 복제에 필요한 <y>네 가지 dNTP를 알맞은 비율로</y>. 한쪽만 넘치면 복제 오류(돌연변이) ↑.</p>
<div class="box"><span class="tag">임상</span><b>ADA 결핍</b>(슬라이드 87, 92): 아데노신 분해가 막혀 <b>dATP 폭증</b> → 주 조절 자리에서 RNR 전체 OFF → DNA 합성 정지 → 림프구 사멸 → <b>중증복합면역결핍(SCID)</b>. 이 슬라이드와 직결!</div>"""),

dict(img=83, slide=83, title="데옥시뉴클레오사이드 삼인산에 의한 RNR 조절", sub="Regulation of ribonucleotide reductase by deoxynucleoside triphosphates",
kw=["ATP · dATP → UDP · CDP 환원", "dTTP → GDP 환원", "dGTP → ADP 환원", "dATP → 전체 억제"],
sum="기질 특이성 자리의 신호 릴레이: ATP(또는 dATP)가 붙으면 피리미딘(UDP, CDP) 환원 → dTTP가 쌓이면 GDP 환원으로 전환 → dGTP가 쌓이면 ADP 환원으로 전환 → dATP가 많아지면 주 조절 자리에서 전체 억제.",
tr="""<p><b>데옥시뉴클레오사이드 삼인산에 의한 리보뉴클레오타이드 환원효소의 조절</b></p>
<p>왼쪽: <b>주 조절 자리에서의 조절</b> — ATP(초록) 활성화, dATP(빨강) 억제 → 네 가지 모두</p>
<p>오른쪽: <b>기질 특이성 자리에서의 조절</b></p>
<ul><li><b>ATP / dATP → UDP와 CDP 환원</b></li><li><b>dTTP / dGTP → GDP와 ADP 환원</b></li>
<li><b>dTTP가 많으면 → GDP 환원 선호</b></li><li><b>dGTP가 많으면 → ADP 환원 선호</b></li></ul>""",
ex="""<p>릴레이로 외우기: <span class="eq">ATP → (C, U) → dTTP → (G) → dGTP → (A) → dATP → STOP</span></p>
<p>각 산물이 <y>다음 차례 기질을 켜고 자기 쪽은 꺼서</y> 네 가지가 차례로 채워지는 구조.</p>
<div class="box"><span class="tag">시험</span>짝 맞추기 문제로 나오기 좋아: “dTTP가 기질 특이성 자리에 붙으면 → <b>GDP</b> 환원 촉진(그리고 CDP·UDP 환원 억제)”, “dGTP → <b>ADP</b> 환원”, “dATP → 주 조절 자리 → <b>모두 억제</b>”.</div>"""),

dict(img=84, slide=84, title="티미딜산(dTMP) 생합성", sub="Biosynthesis of thymidylate (dTMP)",
kw=["dUMP → dTMP", "티미딜산 합성효소", "N⁵,N¹⁰-메틸렌 THF", "DHF 환원효소", "세린 하이드록시메틸전달효소", "엽산 결핍 → DNA에 U"],
sum="dCDP·dUDP → dUTP → (dUTPase) dUMP → (티미딜산 합성효소) dTMP. 메틸기는 N⁵,N¹⁰-메틸렌 THF가 주고 다이하이드로엽산(DHF)이 된다. DHF는 DHF 환원효소(NADPH)로 THF가 되고, 세린이 다시 메틸렌기를 채운다.",
tr="""<p><b>티미딜산(dTMP)의 생합성</b></p>
<ul><li>CDP → (RNR) dCDP → (뉴클레오사이드 이인산 키네이스) dCTP → (탈아미노효소) dUTP</li>
<li>UDP → (RNR) dUDP → dUTP → (<b>dUTPase</b>) <b>dUMP</b> → (<b>티미딜산 합성효소</b>) <b>dTMP</b></li>
<li>엽산 회로: <b>N⁵,N¹⁰-메틸렌 THF</b> → (티미딜산 합성효소, 메틸기 줌) <b>7,8-다이하이드로엽산</b> → (<b>다이하이드로엽산 환원효소</b>, NADPH) <b>테트라하이드로엽산</b> → (<b>세린 하이드록시메틸전달효소</b>, PLP, 세린 → 글라이신) N⁵,N¹⁰-메틸렌 THF</li></ul>
<p><b>엽산 결핍 → DNA에 우라실이 비정상적으로 끼어듦</b></p>""",
ex="""<p>T = U + 메틸기(5번 자리). 메틸기를 줄 때 THF가 <y>전자까지 같이 줘서</y>(메틸렌 → 메틸은 환원) DHF로 산화돼 → 그래서 DHF 환원효소로 되살려야 해.</p>
<p>dUTPase가 중요한 이유: dUTP를 빨리 없애 DNA 중합효소가 U를 잘못 넣지 않게.</p>
<div class="box"><span class="tag">임상</span><b>엽산(또는 B₁₂) 결핍</b> → dTMP 부족 → dUMP/dUTP 쌓여 DNA에 U가 박힘 → 고치다 끊어짐 → 분열 정지 → <b>거대적모구 빈혈</b>. 임신 초기 엽산 부족은 <b>신경관 결손</b> → 엽산 보충 권장.</div>"""),

dict(img=85, slide=85, title="티미딜산 합성과 엽산 대사 — 항암제 표적", sub="Thymidylate synthesis and folate metabolism as targets of chemotherapy",
kw=["5-FU → FdUMP (티미딜산 합성효소)", "메토트렉세이트 · 아미노프테린 (DHFR)", "트라이메토프림 (세균 DHFR)", "자살 억제제"],
sum="dTMP 회로의 두 효소가 표적: ① 티미딜산 합성효소 ← 5-플루오로유라실이 변한 FdUMP(자살 억제) ② 다이하이드로엽산 환원효소 ← 메토트렉세이트·아미노프테린(항암), 트라이메토프림(세균 효소 선택적, 항생제).",
tr="""<p><b>티미딜산 합성과 엽산 대사는 화학요법의 표적</b></p>
<ul><li>dUMP → (<b>티미딜산 합성효소</b>) dTMP ⊣ <b>FdUMP (플루오로데옥시유리딘 일인산)</b></li>
<li>7,8-다이하이드로엽산 → (<b>다이하이드로엽산 환원효소</b>, NADPH) H₄ 엽산 ⊣ <b>메토트렉세이트, 아미노프테린, 트라이메토프림</b></li>
<li>H₄ 엽산 → (세린 하이드록시메틸전달효소, PLP, 세린 → 글라이신) N⁵,N¹⁰-메틸렌 H₄ 엽산</li></ul>
<p>구조: 플루오로유라실 · 트라이메토프림 · 메토트렉세이트 · 5-플루오로데옥시유리딘 일인산(FdUMP) · 아미노프테린</p>""",
ex="""<table class="t"><tr><th>약</th><th>표적</th><th>작용</th></tr>
<tr><td><b>5-FU</b> → FdUMP</td><td>티미딜산 합성효소</td><td>5번 자리 F가 메틸화 후 빠지지 않아 효소·THF와 <b>공유결합으로 갇힘</b> = <b>자살 억제제</b>(기전 기반 비활성화)</td></tr>
<tr><td><b>메토트렉세이트</b></td><td>DHFR (사람)</td><td>엽산 닮은꼴(분홍: –NH₂, N–CH₃), 결합력이 DHF의 ~1000배 → THF 고갈</td></tr>
<tr><td><b>트라이메토프림</b></td><td>DHFR (<b>세균</b>)</td><td>세균 효소에 수만 배 선택적 → 설파메톡사졸과 함께(<b>코트리목사졸</b>)</td></tr></table>
<div class="box"><span class="tag">약학</span>메토트렉세이트 고용량 후 <b>류코보린(폴린산, 5-포밀 THF)</b>으로 정상 세포를 ‘구조’(DHFR을 거치지 않고 THF 공급). 저용량 MTX는 류마티스 관절염·건선에도 쓰고 <b>주 1회</b> 복용 — 매일 복용 오류는 치명적인 투약 사고.</div>"""),

dict(img=86, slide=86, title="퓨린 · 피리미딘 염기의 구제 경로 (’22 약사국시)", sub="Salvage pathways of purine and pyrimidine bases",
kw=["APRT", "HGPRT", "염기 + PRPP → NMP + PPᵢ", "레쉬-니한 증후군", "’22 약시"],
sum="분해된 염기에 PRPP를 다시 붙여 재활용한다: 아데닌 + PRPP → AMP (APRT), 구아닌(하이포잔틴) + PRPP → GMP(IMP) (HGPRT). HGPRT가 없으면 레쉬-니한 증후군: 퓨린·요산 과다, 신경 장애, 자해 행동.",
tr="""<p><b>퓨린과 피리미딘 염기의 구제 경로</b></p>
<p class="eq">아데닌 + PRPP → AMP + PPᵢ (아데닌 포스포리보실전달효소)</p>
<p class="eq">구아닌 + PRPP → GMP + PPᵢ (하이포잔틴-구아닌 포스포리보실전달효소)</p>
<p><b>하이포잔틴-구아닌 포스포리보실전달효소 결핍 → 레쉬-니한 증후군</b> (’22 약시):</p>
<ul><li>퓨린과 요산의 과다 생산</li><li>신경계 장애</li><li>자해 행동</li></ul>""",
ex="""<p>구제 경로는 11단계 새로 합성보다 훨씬 싸(ATP 거의 안 듦). 뇌는 새로 합성이 약해 <y>구제 경로 의존도가 높아</y> → HGPRT 결핍 때 신경 증상.</p>
<p><b>왜 퓨린이 과다 생산?</b> ① 재활용 못 한 하이포잔틴·구아닌 → 전부 요산으로 ② 안 쓰인 <b>PRPP가 쌓여</b> 새로 합성 1단계(글루타민-PRPP 아마이드기 전달효소)를 강하게 밀어 줌.</p>
<div class="box"><span class="tag">약학</span>X-연관 열성(거의 남아). 알로퓨리놀로 요산은 낮출 수 있지만 <b>신경 증상·자해는 못 고침</b>. 항암제 <b>6-머캅토퓨린·6-싸이오구아닌</b>은 HGPRT가 활성화(뉴클레오타이드로)해야 효과 — 약사국시 연결 포인트.</div>"""),

dict(img=87, slide=87, title="퓨린 뉴클레오타이드의 분해 → 요산", sub="Catabolism of purine nucleotides",
kw=["뉴클레오티데이스", "아데노신 탈아미노효소 (ADA)", "하이포잔틴 → 잔틴 → 요산", "잔틴 산화효소", "사람은 요산에서 멈춤"],
sum="AMP → 아데노신 → (ADA) 이노신 → 하이포잔틴 → (잔틴 산화효소) 잔틴 → (잔틴 산화효소) 요산. GMP → 구아노신 → 구아닌 → (탈아미노) 잔틴 → 요산. 영장류는 요산으로 내보내고, 다른 포유류는 알란토인까지 더 분해한다.",
tr="""<p><b>퓨린 뉴클레오타이드의 분해</b></p>
<ul><li>AMP → (<b>5′-뉴클레오티데이스</b>, Pᵢ) 아데노신 → (<b>아데노신 탈아미노효소</b>, NH₃) 이노신 → (<b>뉴클레오시데이스</b>, 리보스) <b>하이포잔틴</b></li>
<li>GMP → (5′-뉴클레오티데이스) 구아노신 → (뉴클레오시데이스) 구아닌 → (<b>구아닌 탈아미노효소</b>, NH₃) 잔틴</li>
<li>하이포잔틴 → (<b>잔틴 산화효소</b>, O₂ → H₂O₂) <b>잔틴</b> → (<b>잔틴 산화효소</b>) <b>요산</b></li>
<li><b>ADA 결핍 → 면역결핍 질환</b></li></ul>
<p>오른쪽 표 (배설 형태): <b>요산</b> — 영장류, 조류, 파충류, 곤충 · (요산 산화효소) <b>알란토인</b> — 대부분의 포유류 · (알란토이네이스) <b>알란토산</b> — 경골어류 · (알란토이케이스) <b>요소</b> + 글리옥실산 — 양서류, 연골어류 · (유레이스) <b>NH₄⁺</b> — 해양 무척추동물 · <b>사람과 다른 고등 유인원</b>은 요산</p>""",
ex="""<p>사람은 <y>요산 산화효소(유리케이스) 유전자가 망가져</y> 요산에서 멈춰. 요산은 물에 잘 안 녹아 → 많으면 결정 → <b>통풍</b>(다음 슬라이드).</p>
<p>요산의 좋은 면: 혈중 <b>항산화제</b>(빌리루빈처럼).</p>
<div class="box"><span class="tag">약학</span><b>라스부리케이스</b>(재조합 요산 산화효소): 항암 치료로 암세포가 한꺼번에 깨질 때(<b>종양 용해 증후군</b>) 요산을 알란토인으로 바로 분해. <b>ADA 결핍</b> = SCID(슬라이드 82의 dATP 기전), 최초의 유전자 치료 대상 질환.</div>"""),

dict(img=88, slide=88, title="알로퓨리놀 — 잔틴 산화효소 억제제", sub="Allopurinol, an inhibitor of xanthine oxidase",
kw=["알로퓨리놀 ≈ 하이포잔틴", "옥시퓨리놀", "자살 억제", "통풍 (요산나트륨 결정)"],
sum="알로퓨리놀은 하이포잔틴과 N·C 자리 하나만 바뀐 닮은꼴. 잔틴 산화효소가 이것을 옥시퓨리놀로 바꾸는데, 옥시퓨리놀이 효소 활성 부위(Mo)에 꽉 붙어 효소를 막는다 → 요산 ↓ → 통풍 치료.",
tr="""<p><b>알로퓨리놀 — 잔틴 산화효소의 억제제</b></p>
<p>알로퓨리놀 (≈ 하이포잔틴 엔올형, 분홍 부분만 다름) → (<b>잔틴 산화효소</b>) <b>옥시퓨리놀</b></p>
<p>요산 → <b>요산나트륨 결정</b> → <b>통풍 (관절 통증)</b></p>
<p>통풍을 <b>알로퓨리놀 또는 옥시퓨리놀</b>로 치료 → <b>잔틴 산화효소 억제 → 요산 감소</b></p>""",
ex="""<p>5각 고리의 N과 C 위치가 바뀌었을 뿐이라 효소가 기질로 착각해. 그 산물(옥시퓨리놀)이 몰리브데넘(Mo) 중심에 단단히 붙어 효소를 못 쓰게 → <y>자살 억제(기전 기반 억제)</y>.</p>
<ul><li>쌓이는 하이포잔틴·잔틴은 요산보다 잘 녹아 소변으로 배설. 하이포잔틴은 구제 경로로 재활용도 됨.</li>
<li>잔틴 산화효소도 Mo 효소 — 질소고정효소(슬라이드 10)에 이어 두 번째 몰리브데넘 효소.</li></ul>
<div class="box"><span class="tag">약학</span><b>알로퓨리놀 + 아자티오프린/6-MP 병용 주의</b>: 6-MP도 잔틴 산화효소로 분해되는데 이걸 막아 6-MP 독성(골수 억제) 폭증 → 6-MP 용량을 1/3–1/4로. 페북소스타트는 비퓨린계 잔틴 산화효소 억제제. 급성 통풍 발작엔 NSAID·콜히친, 알로퓨리놀은 예방(시작 초기 발작 악화 가능).</div>"""),

dict(img=89, slide=89, title="통풍에 나쁜 음식 · 좋은 음식", sub="The worst foods for gout / The best foods for gout",
kw=["과당 시럽", "맥주 · 알코올", "붉은 고기 · 내장", "조개 · 새우 · 멸치", "체리 · 비타민 C · 커피 · 우유 · 물"],
sum="퓨린이 많거나 요산 배설을 방해하는 음식(과당, 맥주, 붉은 고기·간, 해산물)은 나쁘고, 체리·비타민 C, 커피, 저지방 우유, 물은 요산을 낮추는 데 도움이 된다.",
tr="""<p><b>통풍에 가장 나쁜 음식</b>: 고과당 옥수수 시럽 · 맥주와 알코올 · 사냥 고기, 붉은 고기와 간 · 조개류, 새우와 멸치</p>
<p><b>통풍에 가장 좋은 음식</b>: 체리와 비타민 C · 커피 · 우유 · 물</p>""",
ex="""<table class="t"><tr><th>음식</th><th>왜?</th></tr>
<tr><td><b>과당</b></td><td>간에서 과당 인산화에 ATP를 왕창 씀 → AMP ↑ → 분해 → 요산 ↑</td></tr>
<tr><td><b>맥주</b></td><td>퓨린(효모) + 알코올 → 젖산 ↑ → 콩팥 요산 배설 경쟁적으로 방해</td></tr>
<tr><td>내장 · 멸치 · 새우</td><td>세포(핵산) 밀도 높음 = 퓨린 많음</td></tr>
<tr><td>체리 · 비타민 C · 커피 · 우유 · 물</td><td>요산 배설 ↑ 또는 생성 ↓, 물은 소변으로 희석</td></tr></table>
<div class="box"><span class="tag">약학</span>복약지도 포인트: 통풍 환자에게 <b>물 하루 2L 이상, 금주(특히 맥주), 단 음료 줄이기</b>. 이뇨제(티아자이드), 저용량 아스피린은 요산 배설을 줄여 통풍을 악화시킬 수 있음.</div>"""),

dict(img=90, slide=90, title="알란토인이란?", sub="What is allantoin?",
kw=["알란토인", "보습 · 각질 용해", "상처 치유", "흉터 연고"],
sum="대부분의 포유류는 요산을 알란토인으로 더 분해해 내보낸다. 알란토인은 화장품·연고 성분으로 보습, 각질 제거, 상처 치유, 피부 진정 효과가 있다고 알려져 흉터 연고에 들어간다.",
tr="""<p><b>알란토인이란?</b></p>
<p>제조사들은 일반의약품 화장품의 유효 성분으로서 알란토인의 여러 효과를 내세운다: <b>보습 및 각질 용해 효과</b>(세포외 기질의 수분 증가, 상부 각질세포 탈락 촉진으로 피부를 매끄럽게), <b>세포 증식과 상처 치유 촉진</b>, 그리고 자극 물질·감작 물질과 복합체를 만들어 <b>진정·항자극·피부 보호</b> 효과.</p>
<p>2010년 동물 연구: 5% 알란토인 연고가 <b>염증 반응을 조절해 상처 치유</b>를 개선했다. 섬유모세포 증식과 세포외 기질 합성도 촉진하는 것으로 보인다.</p>
<p>2009년 연구: 알란토인이 든 국소 비스테로이드제로 <b>경증~중등도 아토피 피부염의 가려움</b>을 치료했다.</p>
<p>그림: 콘트라투벡스(<b>양파 추출물 Allium cepa</b> + 알란토인 + 헤파린), 메더마 — 흉터 연고</p>""",
ex="""<p>슬라이드 87 오른쪽 표와 연결: <span class="eq">요산 → (요산 산화효소) → 알란토인</span>. 사람은 이 효소가 없어서 몸에서 알란토인을 거의 못 만들어.</p>
<p>약국에서 보는 흉터 연고(콘트라투벡스 등)의 주성분 중 하나. 컴프리(식물)에서 처음 분리됐어.</p>
<div class="boxg">시험 포인트는 “<g>대부분의 포유류는 요산 → 알란토인, 사람·영장류는 요산에서 멈춤</g>”. 알란토인의 화장품 효능 자체는 참고용.</div>"""),

dict(img=91, slide=91, title="피리미딘의 분해", sub="Catabolism of a pyrimidine (thymine)",
kw=["다이하이드로유라실 탈수소효소 (NADPH)", "β-유레이도아이소뷰티르산", "NH₄⁺ → 요소", "β-아미노아이소뷰티르산 → 숙시닐-CoA"],
sum="티민 → (NADPH 환원) 다이하이드로티민 → (고리 열기) β-유레이도아이소뷰티르산 → (NH₄⁺ + HCO₃⁻ 방출 → 요소 합성) β-아미노아이소뷰티르산 → (아미노기 전달) 메틸말로닐 세미알데하이드 → 숙시닐-CoA(TCA로).",
tr="""<p><b>피리미딘(티민)의 분해</b></p>
<ol><li>티민 → (<b>다이하이드로유라실 탈수소효소</b>, NADPH) 다이하이드로티민</li>
<li>→ (<b>다이하이드로피리미디네이스</b>, H₂O) β-유레이도아이소뷰티르산</li>
<li>→ (<b>β-유레이도프로피오네이스</b>, H₂O) <b>NH₄⁺ + HCO₃⁻ → 요소 합성</b> + β-아미노아이소뷰티르산</li>
<li>→ (<b>아미노기 전달효소</b>, α-KG → Glu) <b>메틸말로닐 세미알데하이드 → 숙시닐-CoA</b></li></ol>""",
ex="""<table class="t"><tr><th></th><th>퓨린 분해</th><th>피리미딘 분해</th></tr>
<tr><td>고리</td><td><b>안 열림</b> → 요산 (잘 안 녹음)</td><td><b>열림</b> → 작은 조각</td></tr>
<tr><td>질소</td><td>요산으로 배설</td><td>NH₄⁺ → <b>요소</b></td></tr>
<tr><td>탄소</td><td>—</td><td>숙시닐-CoA(T), 말로닐-CoA → 아세틸-CoA(C, U) — 에너지로 재활용</td></tr></table>
<p>요약 6번: “퓨린 분해 → 요산, 피리미딘 분해 → 요소”.</p>
<div class="box"><span class="tag">약학</span><b>DPD(다이하이드로피리미딘 탈수소효소) 결핍</b> 환자는 <b>5-FU·카페시타빈</b>을 분해 못 해 치명적 독성 → 투여 전 유전자(DPYD) 검사 권고. 5-FU는 피리미딘이라 이 효소로 분해돼.</div>"""),

dict(img=92, slide=92, title="유전 질환 정리", sub="Genetic disorders",
kw=["엽산 결핍", "ADA 결핍", "HGPRT 결핍"],
sum="22.4에서 본 세 가지 질환: 엽산 결핍(dTMP 부족 → 빈혈, 신경관 결손), 아데노신 탈아미노효소 결핍(dATP ↑ → 면역결핍), HGPRT 결핍(레쉬-니한 증후군).",
tr="""<p><b>유전 질환</b></p>
<ul><li>엽산 결핍</li><li>아데노신 탈아미노효소(ADA) 결핍</li><li>하이포잔틴-구아닌 포스포리보실전달효소(HGPRT) 결핍</li></ul>""",
ex="""<table class="t"><tr><th>질환</th><th>막힌 곳</th><th>쌓이는 것 / 결과</th><th>슬라이드</th></tr>
<tr><td><b>엽산 결핍</b></td><td>N⁵,N¹⁰-메틸렌 THF ↓ → 티미딜산 합성 ↓</td><td>DNA에 U 혼입 → 거대적모구 빈혈, 신경관 결손</td><td>84</td></tr>
<tr><td><b>ADA 결핍</b></td><td>아데노신 → 이노신 ✕</td><td>dATP ↑ → RNR 전체 억제 → 림프구 사멸 → <b>SCID</b></td><td>82, 87</td></tr>
<tr><td><b>HGPRT 결핍</b></td><td>구제 경로 ✕</td><td>PRPP ↑ · 요산 ↑ → <b>레쉬-니한</b>: 통풍, 신경 장애, 자해</td><td>86</td></tr></table>
<div class="box"><span class="tag">시험</span>“어떤 효소 결핍 → 어떤 물질 ↑ → 어떤 증상” 3단 연결이 서술형·객관식 모두에 좋아. 특히 <b>ADA → dATP → RNR</b> 연결은 슬라이드 세 장을 엮는 고난도 포인트.</div>"""),

dict(img=93, slide=93, src="요약", title="22.4 요약", sub="Summary",
kw=["PRPP", "Asp · PRPP · 카바모일 인산", "되먹임 억제", "NMP → NTP", "NDP → dNDP", "요산 · 요소", "항암제 표적"],
sum="22.4의 7문장: 퓨린 새로 합성은 PRPP에서 시작 / 피리미딘은 Asp, PRPP, 카바모일 인산으로 / 뉴클레오타이드 합성은 되먹임 억제 / NMP → NTP로 전환 / 리보뉴클레오타이드가 데옥시리보뉴클레오타이드의 전구체 / 퓨린 → 요산, 피리미딘 → 요소 / 많은 항암제가 뉴클레오타이드 합성 효소를 표적.",
tr="""<p><b>요약</b></p>
<ol><li>퓨린 뉴클레오타이드의 새로 합성은 PRPP에서 시작한다</li>
<li>피리미딘 뉴클레오타이드는 아스파르트산, PRPP, 카바모일 인산으로 만든다</li>
<li>뉴클레오타이드 생합성은 되먹임 억제로 조절된다</li>
<li>뉴클레오사이드 일인산은 뉴클레오타이드 삼인산으로 전환된다</li>
<li>리보뉴클레오타이드는 데옥시리보뉴클레오타이드의 전구체다</li>
<li>퓨린과 피리미딘의 분해는 각각 요산과 요소를 만든다</li>
<li>많은 항암제가 뉴클레오타이드 생합성 경로의 효소를 표적으로 한다</li></ol>""",
ex="""<table class="t"><tr><th>문장</th><th>떠올릴 것</th></tr>
<tr><td>1</td><td>PRPP 위에서 11단계 → IMP → AMP(GTP) / GMP(ATP)</td></tr>
<tr><td>2</td><td>ATCase(CTP ⊣, ATP ⊕) → 오로트산 → +PRPP → UMP → UTP → CTP</td></tr>
<tr><td>3</td><td>글루타민-PRPP 아마이드기 전달효소, ATCase, RNR</td></tr>
<tr><td>4</td><td>키네이스: NMP → NDP → NTP (ATP 사용)</td></tr>
<tr><td>5</td><td>RNR: Tyr 라디칼, 티오레독신, 두 조절 자리</td></tr>
<tr><td>6</td><td>잔틴 산화효소 → 요산 (알로퓨리놀) / 피리미딘 고리 열림 → 요소, 숙시닐-CoA</td></tr>
<tr><td>7</td><td>아자세린·아시비신(Gln), 5-FU(TS), 메토트렉세이트(DHFR), 하이드록시유레아(RNR)</td></tr></table>"""),

dict(img=94, slide=94, title="세균 펩티도글리칸과 라세메이스 억제제", sub="Bacterial peptidoglycans and racemase inhibitors",
kw=["펩티도글리칸", "D-알라닌", "알라닌 라세메이스", "사이클로세린", "L-플루오로알라닌"],
sum="세균 세포벽(펩티도글리칸)에는 사람 단백질에 없는 D-알라닌이 들어간다. L-Ala ⇄ D-Ala를 바꾸는 알라닌 라세메이스(PLP 효소)를 막는 사이클로세린·플루오로알라닌은 항균제가 된다.",
tr="""<p><b>세균의 펩티도글리칸과 라세메이스 억제제</b></p>
<p>그림: 펩티도글리칸 — N-아세틸글루코사민(GlcNAc)과 N-아세틸무람산(Mur2Ac)이 (β1→4)로 번갈아 이어진 사슬, 짧은 펩타이드(L-Ala, D-Glu, L-Lys, D-Ala)와 펜타글라이신 다리로 교차결합 · 환원 말단</p>
<p class="eq">L-알라닌 ⇌ D-알라닌</p>
<p><b>알라닌 라세메이스는 항균제의 표적이다</b></p>
<p>구조: <b>L-플루오로알라닌</b> · <b>사이클로세린</b></p>""",
ex="""<p>사람 단백질은 L-아미노산만 쓰는데 세균 세포벽은 <y>D-Ala, D-Glu</y>를 써 → D형을 만드는 효소는 <b>세균에만</b> 있는 좋은 표적(선택 독성).</p>
<ul><li>알라닌 라세메이스: <b>PLP 효소</b>(α-H를 뗐다 반대쪽에 붙임).</li>
<li><b>사이클로세린</b>: D-Ala를 닮아 라세메이스와 D-Ala-D-Ala 연결효소를 막음 → <b>결핵 2차 약</b>(신경정신 부작용 주의, B₆ 병용).</li>
<li>참고: 페니실린은 D-Ala-D-Ala 끝을 닮아 교차결합 효소(트랜스펩티데이스)를, 반코마이신은 D-Ala-D-Ala에 직접 붙어 막아.</li></ul>
<div class="box"><span class="tag">시험</span>22장의 맺음: 아미노산 대사 효소(PLP)가 <b>항생제 표적</b>까지 이어진다. 슬라이드 31의 meso-DAP(라이신 경로)도 같은 세포벽 이야기.</div>"""),
]
