from lib import *

def build():
    chapter(4, 'Neural & Hormonal Communication')
    c = CH['color']
    page('CHAPTER 4', 'Principles of Neural and Hormonal Communication — 한 장 지도',
        chev([('4.1–4.2', '용어·등급전위', '#4c2fb0'), ('4.3 AP', '이온 흐름·불응기·전도', c), ('4.4 시냅스', 'EPSP·IPSP·가중', '#7048e8'), ('4.5 신호 전달', 'GPCR·2차 전령', '#6741d9'), ('4.6–4.8 호르몬', '친수 vs 친유 · 비교', '#3b2a8a')]) +
        grid('1fr 1fr',
            col(card('한 줄 요약', '뉴런은 막전위를 흔들어 말한다: <span class="hy">짧은 거리 = 등급전위, 먼 거리 = 활동전위</span>. AP는 <span class="hg">전압개폐 Na<sup>+</sup> 열림 → K<sup>+</sup> 열림</span>의 2막극. 시냅스에서 화학 신호로 바뀌어 EPSP/IPSP의 합으로 결정되고, 호르몬은 <span class="hp">친수성 = 막 수용체·2차 전령 / 친유성 = 세포 안 수용체·유전자</span>.', 'sum big'),
                card('💡 숫자', 'RMP −70 · 역치 <b>−50~−55</b> · 정점 <b>+30</b> · AP 크기 <b>~100 mV</b> · 도약 전도 <b>~50배</b> 빠름', 'tip')),
            card('🎯 이 장 단골 비교 5', tbl(['비교', '한 줄'], [
                ['Graded vs Action potential', '국소·가변·감쇠·가중 O vs 실무율·재생·불응기'],
                ['Absolute vs Relative refractory', '어떤 자극도 X vs 강한 자극이면 O'],
                ['EPSP vs IPSP', 'Na<sup>+</sup> 유입·탈분극 vs K<sup>+</sup>·Cl<sup>−</sup>·과분극'],
                ['Temporal vs Spatial summation', '같은 입력 반복 vs 여러 입력 동시'],
                ['Hydrophilic vs Lipophilic', '기존 단백질 변형 vs 새 단백질 합성'],
                ['Nervous vs Endocrine', 'wired·근접성 vs wireless·수용체']]), 'warn')), 'Slides 1–51')

    page('PART 01', '막전위 변화의 언어 — 등급전위 vs 활동전위',
        grid('1fr 1fr 1.15fr',
            col(card('📖 4가지 용어', tbl(['용어', '뜻 (−70 기준)'], [
                    ['Polarization', '막전위 ≠ 0 (휴지 상태도 분극)'],
                    ['<b>Depolarization</b>', '덜 음 — <span class="hy">양이온 순유입</span>(Na<sup>+</sup> in)'],
                    ['<b>Repolarization</b>', '탈분극 후 휴지 전위로 <b>복귀</b>'],
                    ['<b>Hyperpolarization</b>', '더 음 — <span class="hy">양이온 순유출</span>(K<sup>+</sup> out) 또는 Cl<sup>−</sup> in']])),
                img('c4-08', '탈분극 · 재분극 · 과분극', '46mm')),
            col(card('정의', '<b>Triggering event</b> → 개폐 통로 모양 변화 → <b>투과도 변화 → 이온 흐름 변화</b> = 막전위를 바꾸는 유일한 방법 (이온은 지질층 통과 불가)', 'def'),
                card('🚪 Gated channels 4종', tbl(['통로', '여는 신호'], [['Voltage-gated', '막전위 변화 (AP)'], ['Chemically gated', '화학 전령 (시냅스)'], ['Mechanically gated', '늘어남·압력 (촉각)'], ['Thermally gated', '온도']])),
                card('💡 자극 세기는?', 'AP는 크기가 늘 같으므로 <span class="hg">세기 = AP의 빈도(frequency)</span> (+ 동원 뉴런 수)', 'tip')),
            card('🆚 이 표 하나로 끝', tbl(['', 'Graded potential', 'Action potential'], [
                    ['거리', '<span class="hy">짧은 거리</span>, 국소', '<span class="hy">먼 거리</span>'],
                    ['크기', '자극 세기·길이에 따라 <b>가변</b>', '<b>All-or-none</b>, ~100 mV'],
                    ['전파', '수동 전류 → <b>감쇠</b>, 금방 소멸', '재생되며 <b>감쇠 없이</b>'],
                    ['가중', '<b>가능</b>', '불가'], ['불응기', '없음', '<b>있음</b>'],
                    ['방향', '탈분극 또는 과분극', '극성 <b>역전</b>(+30)'],
                    ['통로', '화학·기계·열', '<b>전압개폐 Na<sup>+</sup>·K<sup>+</sup></b>'],
                    ['예', 'EPSP/IPSP, <b>수용기전위</b>, <b>종판전위</b>, 박동조율전위', '신경 충격, 근섬유 흥분']]))), 'Slides 6–14')

    qpage('PART 01', '전위 용어 · 등급전위',
        TF([('A net inward flow of cations causes hyperpolarization.', '양이온 순유입은 과분극을 일으킨다.'),
            ('Graded potentials spread by passive current flow and die out over short distances.', '등급전위는 수동 전류로 퍼지며 짧은 거리에서 소멸한다.'),
            ('Graded potentials can summate, whereas action potentials cannot.', '등급전위는 가중될 수 있지만 활동전위는 그렇지 않다.'),
            ('The stronger a triggering event, the larger the resulting graded potential.', '유발 자극이 강할수록 등급전위가 커진다.'),
            ('End-plate potentials and receptor potentials are examples of action potentials.', '종판전위와 수용기전위는 활동전위의 예이다.')],
           'F T T T F', '(1) → <b>depolarization</b> (5) → examples of <b>graded</b> potentials.'),
        MC('Because action potentials are all-or-none, the strength of a stimulus is coded by ____.', '활동전위는 실무율을 따르므로 자극의 세기는 ____로 부호화된다.',
           [('the amplitude of each action potential', '각 AP의 크기'), ('the frequency of action potentials', 'AP의 빈도'), ('the duration of the refractory period', '불응기의 길이'),
            ('the direction of propagation', '전도 방향'), ('the type of neurotransmitter', 'NT의 종류')], '②', '크기는 늘 같다 → <b>빈도</b>.', stars=1),
        SA('Name the four types of gated channels and the stimulus that opens each.', '개폐 통로 4종과 각각을 여는 자극을 쓰시오.',
           'Voltage-gated (membrane potential), chemically gated (chemical messenger), mechanically gated (stretch/pressure), thermally gated (temperature)', 'AP = 전압, 시냅스 = 화학, 촉각 = 기계, 온도 수용기 = 열.', stars=2))

    page('PART 02', '활동전위 — 전압개폐 Na⁺ · K⁺ 통로의 2막극',
        grid('1fr 1.05fr 1fr',
            col(img('c4-18', '역치(−50) → 탈분극(+30) → 재분극 → 후과분극', '70mm'),
                card('🚪 문이 몇 개?', '<b>V-gated Na<sup>+</sup></b>: activation gate(역치에서 <b>빠르게</b> 열림) + inactivation gate(조금 늦게 닫힘) → 상태 3: closed-but-capable → open → <b>closed-and-not-capable</b><br><b>V-gated K<sup>+</sup></b>: 문 1개, <b>지연(delayed)</b> 열림', 'why')),
            card('⏱ 단계별 이온 흐름', tbl(['단계', 'mV', '무슨 일?'], [
                    ['① 휴지', '−70', '전압개폐 통로 모두 닫힘'],
                    ['② 역치', '−50~−55', 'Na<sup>+</sup> 활성화문 열림 → 유입 → 더 탈분극 → 더 열림 (<span class="hp">양성 되먹임</span>)'],
                    ['③ 상승기', '→ +30', 'P<sub>Na</sub> 폭증 (E<sub>Na</sub> 쪽으로)'],
                    ['④ 정점', '+30', 'Na<sup>+</sup> <b>불활성화문 닫힘</b> + K<sup>+</sup> 통로 열림'],
                    ['⑤ 하강기', '→ −70', '<b>K<sup>+</sup> 유출</b> → 재분극'],
                    ['⑥ 후과분극', '−80', 'K<sup>+</sup> 통로가 늦게 닫혀 계속 유출']]) +
                '<p style="margin-top:2mm"><b>Na<sup>+</sup>–K<sup>+</sup> 펌프</b>: AP 동안 움직인 이온은 <b>극소량</b> → 펌프가 <b>천천히</b> 기울기 복구. 재분극은 펌프가 아니라 <b>K<sup>+</sup> 유출</b>!</p>'),
            col(card('🛑 불응기', '<ul><li><b>Absolute</b>: Na<sup>+</sup> 통로가 열렸거나 <b>불활성</b> → <u>어떤 자극으로도</u> AP 불가</li><li><b>Relative</b>: 일부 Na<sup>+</sup> 회복 + K<sup>+</sup> 아직 열림 → <u>더 강한 자극</u>이면 가능</li><li>의미: <span class="hg">일방향 전도</span> + <span class="hg">빈도 상한</span></li></ul>', 'def'),
                img('c4-24', '뒤쪽은 불응 → 앞으로만 진행', '48mm'))), 'Slides 16–25')

    qpage('PART 02', '활동전위 · 불응기',
        MC('The rising (depolarizing) phase of an action potential is caused by ____.', '활동전위 상승기의 원인은?',
           [('opening of voltage-gated K<sup>+</sup> channels', '전압개폐 K<sup>+</sup> 통로 열림'), ('activation of the Na<sup>+</sup>–K<sup>+</sup> pump', '펌프 활성화'),
            ('rapid opening of voltage-gated Na<sup>+</sup> channels and Na<sup>+</sup> influx', '전압개폐 Na<sup>+</sup> 통로의 빠른 열림과 Na<sup>+</sup> 유입'), ('Cl<sup>−</sup> influx', 'Cl<sup>−</sup> 유입'), ('closing of K<sup>+</sup> leak channels', 'K<sup>+</sup> 누출 통로 닫힘')], '③',
           '역치 → Na<sup>+</sup> 활성화문 → Na<sup>+</sup> 유입 → 양성 되먹임 → +30.', stars=1),
        MC('Which TWO statements about the absolute refractory period are correct? <b>(Choose two.)</b>', '절대 불응기에 대한 옳은 설명 두 개는?',
           [('A second AP can be triggered only by a stronger-than-normal stimulus.', '더 강한 자극으로만 두 번째 AP 가능'), ('Voltage-gated Na<sup>+</sup> channels are open or inactivated.', 'Na<sup>+</sup> 통로가 열렸거나 불활성'),
            ('It ensures one-way propagation of action potentials.', 'AP의 일방향 전도를 보장'), ('It allows summation of action potentials.', 'AP 가중을 가능하게 함'), ('All K<sup>+</sup> channels are closed.', 'K<sup>+</sup> 통로가 모두 닫힘')], '②, ③',
           '① = <b>상대</b> 불응기 ④ AP는 가중 불가 ⑤ K<sup>+</sup> 통로는 열리는 중.', pick=2, stars=3),
        TF([('The Na<sup>+</sup>–K<sup>+</sup> pump is responsible for the repolarizing phase of an action potential.', '펌프가 AP의 재분극을 담당한다.'),
            ('The after-hyperpolarization results from slow closing of voltage-gated K<sup>+</sup> channels.', '후과분극은 전압개폐 K<sup>+</sup> 통로가 늦게 닫혀서 생긴다.'),
            ('During an action potential, a large fraction of the cell\'s K<sup>+</sup> leaves the cell.', 'AP 동안 세포 K<sup>+</sup>의 상당 부분이 빠져나간다.'),
            ('During the relative refractory period, a stronger-than-normal stimulus can trigger an AP.', '상대 불응기에는 정상보다 강한 자극으로 AP를 일으킬 수 있다.'),
            ('At the peak of the AP, Na<sup>+</sup> inactivation gates close.', 'AP 정점에서 Na<sup>+</sup> 불활성화문이 닫힌다.')],
           'F T F T T', '(1) → <b>K<sup>+</sup> efflux</b> through voltage-gated K<sup>+</sup> channels (3) → only a <b>tiny fraction</b> of ions move.'))

    page('PART 03', '전도와 화학 시냅스',
        grid('1.05fr 1fr 1fr',
            col(card('🏃 연속 vs 도약 전도', tbl(['', 'Contiguous', 'Saltatory'], [
                    ['섬유', '무수', '<b>유수</b>'], ['방식', '막 전체에서 차례로 AP', '<b>랑비에 결절</b>에서만 AP → 점프'],
                    ['속도', '느림', '<b>~50배 빠름</b>'], ['에너지', '많이', '<b>절약</b> (펌프 일 ↓)']]) +
                    '<ul><li>시작: <b>axon hillock(trigger zone)</b> → 축삭 말단</li><li>수초: <b>CNS = oligodendrocyte</b>, <b>PNS = Schwann cell</b></li><li><b>직경 ↑ → 속도 ↑</b> · 다발성 경화증 = CNS 수초 파괴</li></ul>'),
                img('c4-22', '축삭둔덕 → 결절 사이 도약', '50mm')),
            col(card('정의', '<b>Synapse</b> = 시냅스전·후 뉴런의 접합부<br><b>Electrical</b>: 간극연접, 빠름 · <b>Chemical</b>: NT가 틈을 건너 <b>한 방향</b> = <span class="hy">인체 대부분</span>', 'def'),
                card('⚗ 화학 시냅스 순서', flow('AP 도착', 'V-gated <b>Ca<sup>2+</sup></b> 열림', 'Ca<sup>2+</sup> 유입', 'NT 세포외유출', 'receptor-channel 결합', 'EPSP / IPSP', small=True) +
                    '<p>같은 NT–수용체 조합 = <b>항상 같은 반응</b>. 종료: 효소 분해, <b>재흡수</b>, 확산. 시냅스 지연(synaptic delay) 존재.</p>', 'tip')),
            card('⚖ EPSP vs IPSP', tbl(['', 'EPSP', 'IPSP'], [
                    ['통로', '비특이 양이온 (Na<sup>+</sup> in &gt; K<sup>+</sup> out)', '<b>K<sup>+</sup></b> 또는 <b>Cl<sup>−</sup></b>'],
                    ['전위', '작은 <b>탈분극</b> → 역치에 가까움', '작은 <b>과분극</b> → 역치에서 멂'],
                    ['NT 예', 'glutamate', 'GABA, glycine']]) +
                '<p style="margin-top:2mm">EPSP·IPSP는 <b>등급전위</b> — 하나만으론 보통 역치에 못 미침 → <b>가중</b>이 필요(PART 04).</p>')), 'Slides 22–31')

    page('PART 04', '뉴런 통합 — 가중 · 조절자 · 약물',
        grid('1.1fr 1fr 1fr',
            col(img('c4-31', '(a) 없음 (b) 시간적 (c) 공간적 (d) EPSP–IPSP 상쇄', '68mm'),
                card('', tbl(['가중', '정의'], [['<b>Temporal</b>', '<b>같은</b> 입력이 <b>빠르게 반복</b> → 겹침'], ['<b>Spatial</b>', '<b>여러</b> 입력이 <b>동시에</b>'], ['Cancellation', 'EPSP + IPSP 상쇄']]))),
            col(card('정의', '<b>GPSP(총 시냅스후 전위)</b> = 모든 입력의 합 → <b>축삭둔덕</b>에서 역치 넘으면 AP → 정보 처리·의사 결정·회로 정밀성', 'def'),
                card('🎛 조절자', '<ul><li><b>Neuromodulator</b>: EPSP/IPSP를 만들지 않고 <b>천천히·장기적으로</b> 시냅스 효율 조절</li><li><b>Presynaptic inhibition</b>: 제3 뉴런 → NT 방출 <b>↓</b></li><li><b>Presynaptic facilitation</b>: 제3 뉴런 → NT 방출 <b>↑</b></li><li>장점: 특정 입력 하나만 선택 조절</li></ul>')),
            col(card('💊 약물·질병', 'NT 합성·저장·방출 / 수용체 결합 / 재흡수·분해 / NT 대체<ul><li><b>코카인</b>: 도파민 재흡수 차단</li><li><b>파상풍 독소</b>: 억제성 NT 방출 차단 → 경직</li><li><b>SSRI</b>: 세로토닌 재흡수 차단</li><li><b>L-dopa</b>: 도파민 대체(5장)</li></ul>', 'why'),
                card('🧠 수렴 vs 발산', '<b>Convergence</b>: 많은 → 하나 (통합)<br><b>Divergence</b>: 하나 → 많은 (확산)', 'mint'))), 'Slides 29–33')

    qpage('PART 03', '전도 · 시냅스',
        MC('Which axon would conduct action potentials the fastest?', '활동전위를 가장 빠르게 전도하는 축삭은?',
           [('small-diameter, unmyelinated', '가늘고 무수'), ('large-diameter, unmyelinated', '굵고 무수'), ('small-diameter, myelinated', '가늘고 유수'),
            ('large-diameter, myelinated', '굵고 유수'), ('all equal (all-or-none)', '모두 같음(실무율)')], '④', '수초화 + 큰 직경. 실무율은 크기 얘기.', stars=1),
        MC('At a chemical synapse, entry of which ion into the presynaptic terminal triggers neurotransmitter release?', '화학 시냅스에서 시냅스전 말단으로 어떤 이온이 들어가야 NT가 방출되나?',
           [('Na<sup>+</sup>', ''), ('K<sup>+</sup>', ''), ('Ca<sup>2+</sup>', ''), ('Cl<sup>−</sup>', ''), ('Mg<sup>2+</sup>', '')], '③', '전압개폐 <b>Ca<sup>2+</sup></b> 통로 → 소포 세포외유출. NMJ(7장)도 동일.', stars=1),
        MC('An IPSP is produced by the opening of which TWO types of channels? <b>(Choose two.)</b>', 'IPSP를 만드는 통로 두 가지는?',
           [('K<sup>+</sup> channels', 'K<sup>+</sup> 통로'), ('nonspecific cation channels', '비특이 양이온 통로'), ('Cl<sup>−</sup> channels', 'Cl<sup>−</sup> 통로'),
            ('voltage-gated Na<sup>+</sup> channels', '전압개폐 Na<sup>+</sup> 통로'), ('voltage-gated Ca<sup>2+</sup> channels', '전압개폐 Ca<sup>2+</sup> 통로')], '①, ③', '② = EPSP.', pick=2))

    qpage('PART 04', '가중 · 통합',
        MC('When a single excitatory input fires repeatedly in rapid succession so that EPSPs add together, this is ____.', '하나의 흥분성 입력이 빠르게 반복 발화해 EPSP가 더해지는 것은?',
           [('spatial summation', '공간적 가중'), ('temporal summation', '시간적 가중'), ('presynaptic inhibition', '시냅스전 억제'), ('divergence', '발산'), ('saltatory conduction', '도약 전도')], '②',
           '같은 입력·반복 = 시간적 / 여러 입력·동시 = 공간적.', stars=1),
        SA('Where are synaptic inputs integrated and converted into action potentials? Why there?', '시냅스 입력이 통합되어 AP로 바뀌는 곳과 그 이유는?',
           'The axon hillock (trigger zone); it has the lowest threshold because of a high density of voltage-gated Na<sup>+</sup> channels.', 'GPSP가 여기서 역치를 넘으면 AP.', stars=2),
        TF([('Electrical synapses are the most common type in the human nervous system.', '전기 시냅스가 인체에서 가장 흔하다.'),
            ('Presynaptic inhibition decreases neurotransmitter release from a presynaptic terminal.', '시냅스전 억제는 시냅스전 말단의 NT 방출을 줄인다.'),
            ('Neuromodulators produce fast EPSPs and IPSPs.', '신경조절물질은 빠른 EPSP와 IPSP를 만든다.'),
            ('Convergence means many presynaptic neurons synapse on one neuron.', '수렴은 많은 시냅스전 뉴런이 한 뉴런에 시냅스하는 것이다.'),
            ('Each neurotransmitter–receptor combination always produces the same response.', '각 NT–수용체 조합은 항상 같은 반응을 낸다.')],
           'F T F T T', '(1) → <b>chemical</b> (3) → they act <b>slowly</b> and do not produce EPSPs/IPSPs.'))

    page('PART 05', '세포 간 소통과 신호 전달 — 2차 전령',
        grid('1fr 1.05fr 1fr',
            col(card('📨 화학 전령 4종', tbl(['전령', '거리·경로'], [
                    ['<b>Neurotransmitter</b>', '매우 짧음, 시냅스 틈'], ['<b>Paracrine</b> / Autocrine', '국소: 이웃 / <b>자기 자신</b>'],
                    ['<b>Hormone</b>', '먼 거리, 내분비샘 → <b>혈액</b>'], ['<b>Neurohormone</b>', '<b>신경분비 뉴런</b> → <b>혈액</b> (ADH, 옥시토신)']]) +
                    '<p>Direct 소통: 간극연접, tunneling nanotubes, 표면 표지 결합</p>'),
                card('정의', '<b>Signal transduction</b> = 세포외 전령의 신호가 표적 세포 안으로 전달되어 특정 반응으로 바뀌는 과정', 'def')),
            col(card('🔀 전달 경로', '<b>지용성</b>(스테로이드): 막 통과 → 세포 안 수용체 → <b>유전자 발현</b><br><b>수용성</b>(펩타이드·NT·측분비): 표면 수용체 →<ol><li><b>Chemically gated receptor-channel</b></li><li><b>Receptor-enzyme</b>: tyrosine kinase(인슐린), JAK/STAT</li><li><b>GPCR → 2차 전령</b> (가장 흔함): cAMP, IP<sub>3</sub>, DAG, Ca<sup>2+</sup></li></ol>'),
                card('cAMP 경로', flow('1차 전령', 'GPCR', 'G 단백질 α (GDP→GTP)', 'Adenylyl cyclase', 'ATP → <b>cAMP</b>', 'Protein kinase A', '단백질 인산화', '반응', small=True), 'tip'),
                card('Ca²⁺ 경로', flow('GPCR', 'G 단백질', 'Phospholipase C', 'PIP<sub>2</sub> → <b>IP<sub>3</sub></b> + <b>DAG</b>', small=True) + 'IP<sub>3</sub> → ER에서 <b>Ca<sup>2+</sup> 방출</b> · DAG → <b>protein kinase C</b>', 'mint')),
            col(img('c4-48', '연쇄 = 증폭: 1개 호르몬 → 수천만 개 산물', '70mm'),
                card('', '2차 전령의 장점: <span class="hg">증폭(amplification)</span>, 빠른 반응, 효과의 다양화', 'why'))), 'Slides 35–41, 47–48')

    page('PART 06', '측분비 · 호르몬 · 신경계 vs 내분비계',
        grid('1.05fr 1fr 1fr',
            col(card('🧪 Paracrines', '대부분 <b>Cytokines</b>(단백질, 면역 국소 조절) 또는 <b>Eicosanoids</b>(막 지방산 <b>아라키돈산</b> 유래 지질 — <b>prostaglandins</b>)'),
                card('💉 친수성 vs 친유성 호르몬', tbl(['', 'Hydrophilic', 'Lipophilic'], [
                    ['예', '<b>펩타이드</b>(인슐린), 카테콜아민', '<b>스테로이드</b>, 갑상샘호르몬'],
                    ['저장', '<b>소포에 저장</b> → 세포외유출', '필요할 때 합성, 저장 X'],
                    ['혈중', '혈장에 <b>용해</b>', '<b>혈장 단백질에 결합</b>'],
                    ['수용체', '<b>세포막 표면</b>', '<b>세포 안</b>'],
                    ['작용', '2차 전령 → <span class="hy">기존 단백질 변형</span>', '유전자 → <span class="hy">새 단백질 합성</span>'],
                    ['속도', '빠름·짧음', '느림·오래']]))),
            img('c4-46', '친수성(GPCR-cAMP) vs 친유성(핵 수용체-유전자)', '125mm'),
            col(card('🆚 신경계 vs 내분비계', tbl(['', 'Nervous', 'Endocrine'], [
                    ['구조', '<b>Wired</b>', '<b>Wireless</b>'], ['전령', 'NT → 시냅스 틈', '호르몬 → 혈액'],
                    ['특이성', '<span class="hg">해부학적 근접성</span>', '<span class="hg">수용체 특수화</span>'],
                    ['속도', '빠름(ms)', '느림(분~시간)'], ['지속', '짧음', '김'],
                    ['기능', '골격근·외분비샘, 빠르고 정밀', '대사·수분/전해질·성장']])),
                card('⚠ 함정', '호르몬은 혈액 타고 온몸에 가지만 <b>수용체 있는 세포만</b> 반응. 신경분비 뉴런의 호르몬 = <b>neurohormone</b>.', 'warn'))), 'Slides 42–51')

    qpage('PART 05–06', '신호 전달 · 호르몬',
        MC('Which TWO function as second messengers? <b>(Choose two.)</b>', '2차 전령 두 가지는?',
           [('cyclic AMP', 'cAMP'), ('epinephrine', '에피네프린'), ('inositol trisphosphate (IP<sub>3</sub>)', 'IP<sub>3</sub>'), ('adenylyl cyclase', '아데닐산 고리화효소'), ('G protein', 'G 단백질')], '①, ③',
           '2차 전령 = 세포 <b>안</b>의 작은 신호 분자. 에피네프린 = 1차, AC = 효소, G = 중계자.', pick=2),
        MC('Which statement correctly describes hydrophilic (peptide) hormones?', '친수성(펩타이드) 호르몬의 옳은 설명은?',
           [('They bind intracellular receptors and activate genes.', '세포 안 수용체 → 유전자'), ('They are synthesized on demand and not stored.', '필요 시 합성, 저장 X'),
            ('They bind surface receptors and alter preexisting proteins via second messengers.', '표면 수용체 → 2차 전령 → 기존 단백질 변형'), ('They travel bound to plasma proteins.', '혈장 단백질에 결합 운반'),
            ('Their effects are slower and longer-lasting than steroids.', '스테로이드보다 느리고 오래감')], '③', '나머지는 모두 <b>친유성</b> 특징.'),
        TF([('Lipophilic hormones are largely transported bound to plasma proteins.', '친유성 호르몬은 대부분 혈장 단백질에 결합해 운반된다.'),
            ('Steroid hormones are stored in secretory vesicles until needed.', '스테로이드 호르몬은 필요할 때까지 분비소포에 저장된다.'),
            ('Neurohormones are released into the blood by neurosecretory neurons.', '신경호르몬은 신경분비 뉴런이 혈액으로 방출한다.'),
            ('Endocrine specificity results from receptor specialization.', '내분비 특이성은 수용체 특수화에서 비롯된다.'),
            ('Most paracrines are cytokines or eicosanoids.', '대부분의 측분비물질은 사이토카인 또는 에이코사노이드이다.')],
           'T F T T T', '(2) → steroids are synthesized <b>on demand</b> and not stored (지질이라 막을 통과해버림).'))

    qpage('PART 02 · 05', '서술형',
        ES('Describe the changes in membrane permeability and ion movement during an action potential, from resting potential through after-hyperpolarization.', '휴지 전위부터 후과분극까지 AP 동안의 투과도·이온 이동 변화를 서술하시오.',
           'At rest (−70 mV) voltage-gated Na<sup>+</sup> and K<sup>+</sup> channels are closed. When a triggering event depolarizes the membrane to threshold (about −50 mV), the activation gates of voltage-gated Na<sup>+</sup> channels open rapidly; Na<sup>+</sup> rushes in, depolarizing the membrane further and opening more Na<sup>+</sup> channels (positive feedback), so the potential reverses to about +30 mV. At the peak, Na<sup>+</sup> inactivation gates close and slower voltage-gated K<sup>+</sup> channels open; K<sup>+</sup> leaves, repolarizing the membrane. Because K<sup>+</sup> channels close slowly, extra K<sup>+</sup> efflux causes a brief after-hyperpolarization. Only a tiny fraction of ions move, and the Na<sup>+</sup>–K<sup>+</sup> pump gradually restores the gradients.',
           '역치 · 활성화/불활성화문 · 양성 되먹임 · +30 · K<sup>+</sup> 지연 · 후과분극 · 펌프 역할.'),
        ES('Explain the cAMP second-messenger pathway activated by a hydrophilic hormone and why it produces signal amplification.', '친수성 호르몬의 cAMP 경로와 신호 증폭이 일어나는 이유를 설명하시오.',
           'The hormone (first messenger) binds a G-protein-coupled receptor. The receptor activates a G protein, whose α subunit exchanges GDP for GTP and activates adenylyl cyclase, which converts ATP into cAMP (second messenger). cAMP activates protein kinase A, which phosphorylates specific preexisting intracellular proteins, changing their shape and function to produce the response. Amplification occurs because each activated molecule activates many molecules at the next step, so one hormone molecule can produce millions of product molecules.',
           '순서 8단계 + "각 단계가 다음 단계 여러 개를 활성화".'), cols=2)

    memo([('⚡ 전위', '탈분극 = 양이온 in / 과분극 = K<sup>+</sup> out·Cl<sup>−</sup> in<br>Graded = 국소·가변·감쇠·가중 O<br>AP = all-or-none·재생·불응기<br>세기 = <b>빈도</b>'),
          ('🔺 AP', '역치 −50 → Na<sup>+</sup> in(양성 되먹임) → +30<br>정점: Na<sup>+</sup> 불활성 + K<sup>+</sup> 열림 → 재분극<br>후과분극 = K<sup>+</sup> 늦게 닫힘<br>절대 = 불가 / 상대 = 강하면 가능'),
          ('🔗 시냅스', 'Ca<sup>2+</sup> 유입 → NT 방출<br>EPSP = Na<sup>+</sup> / IPSP = K<sup>+</sup>·Cl<sup>−</sup><br>Temporal = 같은·반복 / Spatial = 여러·동시<br>축삭둔덕에서 판정 · 도약 = 유수·결절'),
          ('📨 호르몬', 'GPCR → G → AC → cAMP → PKA<br>PLC → IP<sub>3</sub>(Ca<sup>2+</sup>) + DAG(PKC)<br>친수 = 표면·기존 단백질 / 친유 = 안·새 단백질<br>Wired·근접 vs Wireless·수용체')],
         '<ol><li>재분극 = <b>K<sup>+</sup> 유출</b> (펌프 ✗)</li><li>AP 세기 = <b>빈도</b> (크기 ✗)</li><li>스테로이드 = <b>저장 X</b>, 단백질에 결합 운반</li></ol>',
         ['Graded potentials are local, decremental, and vary in magnitude, whereas action potentials are all-or-none and propagate without decrement.',
          'The refractory period ensures one-way propagation of action potentials and limits their frequency.',
          'Hydrophilic hormones alter preexisting proteins via second messengers, whereas lipophilic hormones activate genes to synthesize new proteins.'])
