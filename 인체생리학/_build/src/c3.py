from lib import *

def build():
    chapter(3, 'Plasma Membrane & Membrane Potential')
    c = CH['color']
    page('CHAPTER 3', 'The Plasma Membrane and Membrane Potential — 한 장 지도',
        chev([('3.1 막 구조', '유동 모자이크', '#0b5aa6'), ('3.2 부착', 'ECM·연접 3종', c), ('3.3–3.4 비보조', '확산·삼투·장성', '#228be6'), ('3.5 보조 수송', '운반체·능동수송', '#1c7ed6'), ('3.6 막전위', 'E<sub>K</sub>·E<sub>Na</sub>·RMP', '#174f8a')]) +
        grid('1fr 1fr',
            col(card('한 줄 요약', '세포막 = <span class="hy">기름 벽(지질 이중층) + 문(단백질)</span>. 기름에 녹는 것·작은 것은 그냥 통과, 이온·큰 것은 <span class="hg">통로·운반체</span>, 오르막이면 <span class="hp">ATP</span>. 이 선택적 투과 + Na<sup>+</sup>–K<sup>+</sup> 펌프 + K<sup>+</sup> 누출 = 안쪽이 음(−70 mV)인 <b>막전위</b>.', 'sum big'),
                card('💡 숫자 5개만 먼저', 'RMP <b>−70 mV</b> · E<sub>K</sub> <b>−90</b> · E<sub>Na</sub> <b>+60</b> · 펌프 <b>3 Na<sup>+</sup> out : 2 K<sup>+</sup> in</b> · 등장액 <b>300 mOsm</b>', 'tip')),
            card('🎯 이 장 서술형 단골 3', tbl(['질문', '키워드'], [
                ['RMP는 어떻게 생기나?', '펌프 · K<sup>+</sup> 유출(누출 통로) · Na<sup>+</sup> 소량 유입 · A<sup>−</sup>'],
                ['왜 RMP는 E<sub>K</sub>에 가까운가?', '휴지 막은 <b>K<sup>+</sup> 투과도</b>가 훨씬 큼'],
                ['통로 vs 운반체, 수송 종류 비교', 'S·S·C, Tm, ATP 직접/간접'],
                ['그래프: 단순 확산 vs 운반체', '직선 vs <b>Tm에서 평탄(포화)</b>'],
                ['장성과 적혈구', 'hypo → 부풂 · hyper → 쪼그라듦']]), 'warn')), 'Slides 1–39')

    page('PART 01', '막 구조 — 유동 모자이크 · 세포연접 3종',
        grid('1fr 1fr 1.1fr',
            col(card('정의', '세포막 = <span class="hy">단백질이 박힌 유동성 지질 이중층</span> (fluid mosaic model). 지질 + 단백질 + 소량의 탄수화물. 가장 많은 지질 = <b>인지질</b>.', 'def'),
                card('🧈 구성 요소', '<ul><li><b>인지질</b>: 친수성 머리(물 쪽) + 소수성 꼬리(안쪽) → 물속에서 저절로 이중층</li><li><b>콜레스테롤</b>: 인지질 사이에 끼어 꼬리가 <b>뭉쳐 결정화되는 것을 막음</b> → <span class="hg">유동성 + 안정성</span></li><li><b>막단백질</b>: Integral(내재: monotopic 한 층 / polytopic 관통) · Transmembrane(전체 관통) · Peripheral(표면, 비공유결합)</li><li><b>탄수화물</b>: 바깥면 당사슬 = <b>자기 인식 표지</b>, 세포 간 상호작용</li></ul>')),
            col(card('🔧 기능 표', tbl(['구성', '기능'], [
                    ['Lipid bilayer', '기본 구조, 유동성, <span class="hy">소수성 내부가 수용성 물질을 막음</span>'],
                    ['Proteins', '① Channels ② Carriers ③ Docking-marker acceptors ④ Receptors ⑤ CAMs(접착)'],
                    ['Carbohydrates', '자기 인식, 세포 간 상호작용, 조직 성장']])),
                card('🧠 막단백질 5기능 = "통·운·도·수·접"', '통로 · 운반체 · 도킹 수용체 · 수용체 · 접착분자', 'mint'),
                card('🧵 ECM', '세포를 묶는 접착제: <b>collagen</b>(인장), <b>elastin</b>(탄성), <b>fibronectin</b>(세포를 기질에 고정)')),
            col(card('🔗 세포연접 3종', tbl(['연접', '구조·기능', '어디'], [
                    ['<b>Tight</b>', '<span class="hp">틈을 봉함(impermeable)</span> → 세포 사이로 못 지나감, 두 구획 분리', '상피: 방광·장·신장'],
                    ['<b>Desmosome</b>', '"리벳" — 두 세포 <span class="hy">고정</span>, 물·이온은 통과 가능', '늘어나는 조직: 피부·장'],
                    ['<b>Gap</b>', 'connexon <span class="hg">터널</span> → 이온 직접 이동 = 소통 연접, AP 전파', '심장근·뉴런']])),
                img('c3-12', '밀착연접 · 데스모솜 · 간극연접', '62mm'),
                card('', '<b>Tight = 봉인 · Desmosome = 리벳 · Gap = 터널</b>', 'tip'))), 'Slides 3–12')

    qpage('PART 01', '막 구조 · 연접',
        MC('Which of the following is <u>NOT</u> a function of plasma membrane proteins?', '다음 중 막단백질의 기능이 <u>아닌</u> 것은?',
           [('forming water-filled channels', '물이 찬 통로 형성'), ('serving as carriers', '운반체'), ('acting as receptors', '수용체'),
            ('forming the hydrophobic barrier to water-soluble substances', '수용성 물질을 막는 소수성 장벽'), ('acting as cell adhesion molecules', '세포 접착 분자')], '④',
           '소수성 장벽 = <b>지질 이중층</b>. 단백질 = 통·운·도·수·접.'),
        MC('Which junction prevents materials from passing <u>between</u> cells and is found in epithelia of the intestine and kidney?', '세포 <u>사이로</u> 물질이 지나가지 못하게 하며 장·신장 상피에 있는 연접은?',
           [('desmosome', '데스모솜'), ('gap junction', '간극연접'), ('tight junction', '밀착연접'), ('synapse', '시냅스'), ('extracellular matrix', '세포외기질')], '③',
           '"impermeable · seal" = tight. 데스모솜은 고정만, 간극연접은 오히려 통로.', stars=1),
        TF([('Cholesterol makes the membrane rigid by causing fatty acid tails to crystallize.', '콜레스테롤은 지방산 꼬리를 결정화시켜 막을 단단하게 만든다.'),
            ('Gap junctions allow ions to pass directly between adjacent cells, spreading action potentials in cardiac muscle.', '간극연접은 이온이 인접 세포 사이로 직접 이동하게 해 심장근에서 AP를 퍼뜨린다.'),
            ('Desmosomes seal cells together so that nothing can pass between them.', '데스모솜은 세포를 봉합해 사이로 아무것도 지나가지 못하게 한다.'),
            ('Peripheral proteins span the entire lipid bilayer.', '표재성 단백질은 지질 이중층 전체를 관통한다.'),
            ('Membrane carbohydrates serve as self-recognition markers.', '막 탄수화물은 자기 인식 표지로 작용한다.')],
           'F T F F T', '(1) → <b>prevents</b> crystallization (3) → 그건 <b>tight junction</b>; desmosome = anchor (4) → <b>transmembrane</b> proteins span; peripheral = 표면.'))

    page('PART 02', '무엇이 막을 통과하나 — 확산 · 삼투 · 장성',
        grid('1fr 1fr 1fr',
            col(card('🚪 통과 여부', tbl(['물질', '방법'], [
                    ['지용성·비극성 (O<sub>2</sub>, CO<sub>2</sub>, 지방산)', '이중층 그대로 = simple diffusion'],
                    ['이온 (Na<sup>+</sup>, K<sup>+</sup>)', '<b>통로(channel)</b>'],
                    ['크고 비지용성 (포도당)', '<b>운반체(carrier)</b>'],
                    ['아주 큰 것 (단백질)', '<b>소포 수송</b>']]) + '<p><b>Passive</b> = 에너지 X (확산·삼투·촉진확산)<br><b>Active</b> = ATP (능동수송·소포수송)</p>'),
                card('➗ 확산', '<ul><li>무작위 운동 → 농도 기울기 <b>아래로</b></li><li><b>Net diffusion</b> = 두 방향 확산의 차 (10 − 2 = 8). 평형에서도 이동은 계속, 순이동 0</li><li>전기 기울기: 양이온은 음전하 쪽으로 · 화학 + 전기 = <span class="hg">electrochemical gradient</span></li></ul>')),
            col(card("📐 Fick's law — 확산 속도 5요인", tbl(['↑ 비례', '↓ 반비례'], [['① 농도 기울기<br>② 막 표면적<br>③ 지질 용해도', '④ 분자량(크기)<br>⑤ 거리(막 두께)']]) + '<small>폐포 = 얇고(거리↓) 넓음(표면적↑) → 빠른 기체 교환</small>', 'tip'),
                card('💧 삼투와 장성', '<b>Osmosis</b> = <span class="hy">물의 순확산</span>: 물 많은 쪽(용질 적은 쪽) → 용질 많은 쪽. "물은 용질을 따라간다"<br><b>Tonicity</b> = <span class="hg">비투과성 용질</span> 농도가 세포 부피에 미치는 효과' + tbl(['용액', '물 이동', '적혈구'], [
                    ['Isotonic 300 mOsm', '0', '그대로'], ['Hypotonic', '<b>안으로</b>', '부풂 → 용혈'], ['Hypertonic', '<b>밖으로</b>', '쪼그라듦(crenation)']])),
                card('⚠ 함정', '장성은 <b>비투과성</b> 용질만 결정. 통과하는 용질(요소)은 결국 평형 → 장성에 기여 X.', 'warn')),
            img('c3-25', '등장 · 저장 · 고장 용액의 적혈구', '128mm')), 'Slides 14–25')

    qpage('PART 02', '확산 · 삼투 · 장성',
        MC("According to Fick's law, which TWO changes would <u>increase</u> the rate of net diffusion? <b>(Choose two.)</b>", '픽의 법칙에 따라 순확산 속도를 <u>증가</u>시키는 변화 두 가지는?',
           [('Increasing membrane thickness', '막 두께 증가'), ('Increasing membrane surface area', '막 표면적 증가'), ('Increasing molecular weight', '분자량 증가'),
            ('Increasing lipid solubility', '지질 용해도 증가'), ('Decreasing the concentration gradient', '농도 기울기 감소')], '②, ④',
           '분자: 기울기·표면적·지질 용해도 / 분모: 분자량·거리.', pick=2),
        SA('A cell with an intracellular osmolarity of 300 mOsm is placed in a solution of 400 mOsm nonpenetrating solutes. Name the tonicity and describe what happens to the cell.',
           '세포내 300 mOsm인 세포를 비투과성 용질 400 mOsm 용액에 넣었다. 장성과 세포 변화를 쓰시오.',
           'Hypertonic; water leaves by osmosis and the cell shrinks (crenation).', '물은 용질 많은 쪽(400, 밖)으로.', stars=2),
        TF([('When a red blood cell is placed in a hypotonic solution, water leaves and the cell shrinks.', '적혈구를 저장액에 넣으면 물이 빠져나가 쪼그라든다.'),
            ('O<sub>2</sub> and CO<sub>2</sub> can cross the plasma membrane through the lipid bilayer without assistance.', 'O<sub>2</sub>와 CO<sub>2</sub>는 도움 없이 지질 이중층을 통과한다.'),
            ('At dynamic equilibrium, molecules stop moving across the membrane.', '동적 평형에서는 분자가 막을 가로질러 움직이지 않는다.'),
            ('The electrochemical gradient is the net of the chemical and electrical gradients.', '전기화학적 기울기는 화학 기울기와 전기 기울기의 합이다.'),
            ('Tonicity depends on the concentration of penetrating solutes.', '장성은 투과성 용질의 농도에 따라 달라진다.')],
           'F T F T F', '(1) water <b>enters</b>, cell <b>swells</b> (3) 이동은 계속, <b>net</b> 이동이 0 (5) → <b>nonpenetrating</b> solutes.'))

    page('PART 03', '보조 수송 — 통로 · 운반체 · 능동수송',
        grid('1fr 1fr 1.05fr',
            col(card('🆚 Channel vs Carrier', tbl(['', 'Channel', 'Carrier'], [
                    ['구조', '열린 구멍', '결합 → <b>모양 변화</b>로 ECF/ICF 번갈아'], ['속도', '<b>빠름</b>', '느림'],
                    ['방향', '수동만', '수동 <b>또는</b> 능동'], ['대상', '이온', '포도당·아미노산']])),
                card('운반체 3대 특징 (S·S·C)', '<ul><li><b>Specificity</b>: 특정 물질만</li><li><b>Saturation</b>: 운반체 수 한정 → 최대 속도 <b>Tm</b></li><li><b>Competition</b>: 비슷한 물질끼리 경쟁</li></ul>', 'def')),
            col(img('c3-29', '단순 확산(직선) vs 운반체 매개(Tm에서 평탄 = 포화)', '58mm'),
                card('📈 그래프 읽기', '단순 확산 = ECF 농도에 <b>정비례</b>(직선). 운반체 매개 = 다 차면 <b>Tm에서 평탄</b> → "plateau = 운반체 포화"', 'tip'),
                card('🧠 방향', '<b>Uniport</b> 1개 · <b>Symport</b> 같은 방향 · <b>Antiport</b> 반대 방향<br>Na<sup>+</sup>–K<sup>+</sup> 펌프 = antiport + <b>1차</b> / SGLT = symport + <b>2차</b>', 'mint')),
            col(card('⚡ 수송 4종', tbl(['종류', '에너지', '예'], [
                    ['<b>Facilitated diffusion</b>', 'ATP ✗', '운반체가 <b>downhill</b> — GLUT(포도당)'],
                    ['<b>Primary active</b>', '<span class="hp">ATP 직접</span>', '<b>Na<sup>+</sup>–K<sup>+</sup> ATPase: 3 Na<sup>+</sup> out, 2 K<sup>+</sup> in</b>, Ca<sup>2+</sup> 펌프'],
                    ['<b>Secondary active</b>', 'ATP 간접', '1차가 만든 <b>Na<sup>+</sup> 기울기</b> 이용 — <b>SGLT</b>(symport), Na<sup>+</sup>/H<sup>+</sup>(antiport)'],
                    ['<b>Vesicular</b>', 'ATP', 'endo/exocytosis, 속도 균형 → 막 면적 일정']])),
                card('⚠ 함정', '2차 능동수송의 운반체 자체는 ATP를 안 쓴다 — Na<sup>+</sup>가 내려가는 힘을 빌림. 펌프가 멈추면 결국 2차 수송도 멈춤.', 'warn'))), 'Slides 26–31')

    qpage('PART 03', '운반체 · 능동수송',
        MC('The rate of carrier-mediated transport levels off at high solute concentration because ____.', '높은 용질 농도에서 운반체 매개 수송 속도가 평평해지는 이유는?',
           [('the concentration gradient disappears', '농도 기울기가 사라져서'), ('all carrier binding sites are occupied (saturation)', '운반체 결합 부위가 모두 차서(포화)'),
            ('ATP is depleted', 'ATP 고갈'), ('the membrane becomes impermeable to water', '막이 물을 막아서'), ('channels close', '통로가 닫혀서')], '②', '운반체 개수 한정 → <b>Tm</b>.', stars=1),
        MC('Which TWO statements about the Na<sup>+</sup>–K<sup>+</sup> ATPase pump are correct? <b>(Choose two.)</b>', 'Na<sup>+</sup>–K<sup>+</sup> 펌프에 대한 옳은 설명 두 개는?',
           [('It moves 3 Na<sup>+</sup> out and 2 K<sup>+</sup> in per ATP.', 'ATP 1개당 Na<sup>+</sup> 3개 밖, K<sup>+</sup> 2개 안'), ('It is secondary active transport.', '2차 능동수송이다'),
            ('It moves both ions down their gradients.', '두 이온을 기울기 아래로 옮긴다'), ('It creates the Na<sup>+</sup> gradient used by SGLT.', 'SGLT가 쓰는 Na<sup>+</sup> 기울기를 만든다'), ('It is an always-open channel.', '항상 열린 통로이다')], '①, ④',
           '1차 능동, 두 이온 모두 <b>오르막</b>. 이 기울기가 2차 수송(SGLT)의 동력.', pick=2, stars=3),
        MC('The Na<sup>+</sup>–glucose cotransporter (SGLT), which moves glucose into intestinal cells against its gradient, is an example of ____.', '포도당을 기울기를 거슬러 장 세포로 옮기는 SGLT는 ____의 예이다.',
           [('simple diffusion', '단순 확산'), ('facilitated diffusion', '촉진확산'), ('primary active transport, antiport', '1차 능동, 역수송'), ('secondary active transport, symport', '2차 능동, 공동수송'), ('pinocytosis', '음세포작용')], '④',
           'Na<sup>+</sup>와 포도당이 <b>같은 방향</b>, 에너지는 Na<sup>+</sup> 기울기.'))

    nern = tbl(['이온', '밖', '안', '계산', 'E'], [['K<sup>+</sup>', '5', '150', '61 × log(5/150) = 61 × (−1.48)', '<b>≈ −90 mV</b>'], ['Na<sup>+</sup>', '150', '15', '61 × log(10) = 61 × 1', '<b>≈ +60 mV</b>']])
    page('PART 04', '막전위 — 왜 세포 안은 음(−)인가',
        grid('1fr 1fr 1.05fr',
            col(card('정의', '<b>Membrane potential</b> = 막을 사이에 둔 <span class="hy">반대 전하의 분리</span> (안쪽 음, 바깥 양), 단위 mV. 모든 세포가 가짐 → <b>흥분성 세포(뉴런·근육)</b>만 빠르게 바꿔 활동전위.', 'def'),
                card('🔋 이온 분포 (mM)', tbl(['이온', 'ECF', 'ICF', '휴지 투과도'], [['Na<sup>+</sup>', '<b>150</b>', '15', '낮음'], ['K<sup>+</sup>', '5', '<b>150</b>', '<b>높음</b> (누출 통로)'], ['A<sup>−</sup>', '0', '<b>65</b>', '0 (갇힘)']])),
                card('⚖ Equilibrium potential', '한 이온에 대해 <span class="hg">전기 기울기 = 농도 기울기</span>로 균형 → 그 이온의 순이동 0인 막전위<ul><li><b>E<sub>K</sub> = −90</b>: K<sup>+</sup> 밖으로 → 안 음 → 음전하가 다시 끌어당김</li><li><b>E<sub>Na</sub> = +60</b>: Na<sup>+</sup> 안으로 → 안 양 → 밀어냄</li></ul>')),
            col(card('🧮 Nernst (37 °C)', '<p style="text-align:center;font-size:10.5pt"><b>E = (61 / z) · log(C<sub>out</sub> / C<sub>in</sub>)</b></p>' + nern, 'why'),
                card('RMP = −70 mV — 4요소', '<ol><li><b>Na<sup>+</sup>–K<sup>+</sup> 펌프</b>: 기울기를 <b>만들고 유지</b> (3:2 → 약간의 직접 음전하, electrogenic)</li><li><b>K<sup>+</sup> 유출</b>: 누출 통로 많음 → <span class="hy">주된 원인</span>, E<sub>K</sub> 쪽으로</li><li><b>Na<sup>+</sup> 소량 유입</b>: 약간 상쇄 → −90이 아닌 −70</li><li><b>A<sup>−</sup></b>: 못 나가는 큰 음이온</li></ol>', 'tip')),
            col(img('c3-37', 'K⁺ 유출(큰 화살표) + Na⁺ 유입(작은 화살표) → −70 mV', '72mm'),
                card('⚠ 함정', '<ul><li>RMP가 <b>E<sub>K</sub>에 가까운</b> 이유 = K<sup>+</sup> 투과도가 훨씬 큼</li><li>펌프를 멈춰도 즉시 0이 되지 않음 (기울기가 천천히 무너짐)</li><li>ECF K<sup>+</sup>↑ → 덜 음(탈분극)</li><li>전하 분리는 막 바로 옆 극소수 이온뿐 — 전체 액체는 중성</li></ul>', 'warn'))), 'Slides 33–39')

    qpage('PART 04', '막전위',
        SA('Using the Nernst equation, calculate E<sub>K</sub> when [K<sup>+</sup>]<sub>o</sub> = 5 mM and [K<sup>+</sup>]<sub>i</sub> = 150 mM (z = +1).', '[K<sup>+</sup>]<sub>밖</sub> = 5, [K<sup>+</sup>]<sub>안</sub> = 150 mM일 때 E<sub>K</sub>를 계산하시오.',
           'E<sub>K</sub> = 61 × log(5/150) ≈ 61 × (−1.48) ≈ −90 mV', 'log(1/30) = −1.477. Na<sup>+</sup>: log(150/15) = 1 → +61 ≈ +60 mV.', stars=2),
        MC('The resting membrane potential of a neuron (−70 mV) is much closer to E<sub>K</sub> than to E<sub>Na</sub> because ____.', '뉴런의 휴지막전위가 E<sub>Na</sub>보다 E<sub>K</sub>에 훨씬 가까운 이유는?',
           [('the Na<sup>+</sup>–K<sup>+</sup> pump moves more K<sup>+</sup> than Na<sup>+</sup>', '펌프가 Na<sup>+</sup>보다 K<sup>+</sup>를 더 많이 옮겨서'), ('the resting membrane is much more permeable to K<sup>+</sup> than to Na<sup>+</sup>', '휴지 막의 K<sup>+</sup> 투과도가 Na<sup>+</sup>보다 훨씬 커서'),
            ('there is more K<sup>+</sup> in the ECF than in the ICF', 'ECF에 K<sup>+</sup>가 더 많아서'), ('Na<sup>+</sup> cannot cross the membrane at all', 'Na<sup>+</sup>는 전혀 통과 못해서'), ('A<sup>−</sup> diffuses out of the cell', 'A<sup>−</sup>가 밖으로 확산해서')], '②',
           'K<sup>+</sup> leak channels가 많음. ① 펌프는 오히려 Na<sup>+</sup> 3개를 더 옮김 ③ 반대 ④ 소량 유입은 있음 ⑤ A<sup>−</sup>는 못 나감.'),
        TF([('The equilibrium potential is the membrane potential at which there is no net movement of a particular ion.', '평형전위는 특정 이온의 순이동이 없는 막전위이다.'),
            ('Only excitable cells have a membrane potential.', '흥분성 세포만 막전위를 가진다.'),
            ('Large intracellular protein anions (A<sup>−</sup>) contribute to the negativity inside the cell.', '세포 안의 큰 단백질 음이온은 내부의 음전하에 기여한다.'),
            ('If the Na<sup>+</sup>–K<sup>+</sup> pump stops, the membrane potential immediately becomes 0 mV.', '펌프가 멈추면 막전위가 즉시 0이 된다.'),
            ('E<sub>Na</sub> is about +60 mV.', 'E<sub>Na</sub>는 약 +60 mV이다.')],
           'T F T F T', '(2) <b>all cells</b> have one; excitable cells can <b>change</b> it rapidly (4) 기울기가 <b>천천히</b> 무너짐.'))

    qpage('PART 03–04', '서술형',
        ES('Explain how the resting membrane potential of a neuron (−70 mV) is established. Include the roles of the Na<sup>+</sup>–K<sup>+</sup> pump, K<sup>+</sup> leak channels, Na<sup>+</sup> movement, and intracellular anions.',
           '뉴런의 휴지막전위가 어떻게 형성되는지 펌프, K<sup>+</sup> 누출 통로, Na<sup>+</sup> 이동, 세포내 음이온의 역할을 포함해 서술하시오.',
           'The Na<sup>+</sup>–K<sup>+</sup> pump actively transports 3 Na<sup>+</sup> out and 2 K<sup>+</sup> in, creating high [K<sup>+</sup>] inside and high [Na<sup>+</sup>] outside, and contributes slightly because it is electrogenic. At rest the membrane is much more permeable to K<sup>+</sup> because of abundant K<sup>+</sup> leak channels, so K<sup>+</sup> diffuses out down its concentration gradient, leaving behind large protein anions (A<sup>−</sup>) that cannot leave. This makes the inside negative and drives the potential toward E<sub>K</sub> (−90 mV). A small inward leak of Na<sup>+</sup> partially offsets this, so the resting potential settles at about −70 mV, closer to E<sub>K</sub> than to E<sub>Na</sub> (+60 mV).',
           '4요소 + "왜 E<sub>K</sub>에 가까운가" 한 문장 = 만점.'),
        ES('Compare channels and carriers, and distinguish facilitated diffusion, primary active transport, and secondary active transport with one example each.',
           '통로와 운반체를 비교하고, 촉진확산·1차·2차 능동수송을 예와 함께 구분하시오.',
           'Both are integral membrane proteins. Channels form open pores that allow rapid, passive movement of specific ions down their electrochemical gradients. Carriers bind specific molecules and change conformation to move them more slowly; carrier-mediated transport shows specificity, saturation (Tm), and competition. Facilitated diffusion is passive carrier-mediated transport down a gradient without ATP (glucose via GLUT). Primary active transport uses ATP directly to move substances against their gradient (Na<sup>+</sup>–K<sup>+</sup> ATPase). Secondary active transport uses the Na<sup>+</sup> gradient created by primary active transport to move another substance uphill by symport or antiport (SGLT).',
           '에너지원(없음 / ATP 직접 / Na<sup>+</sup> 기울기) 구분이 핵심.'), cols=2)

    memo([('🧈 막·연접', '유동 모자이크 · 콜레스테롤 = 결정화 방지<br>단백질 = 통·운·도·수·접<br>Tight = 봉인 / Desmosome = 리벳 / Gap = 터널<br>ECM = collagen·elastin·fibronectin'),
          ('💧 확산·삼투', "Fick ↑: 기울기·표면적·지질용해도<br>Fick ↓: 분자량·거리<br>Hypo → 부풂 / Hyper → 쪼그라듦<br>장성 = <b>비투과성</b> 용질"),
          ('🚚 수송', 'Channel = 빠름·수동 / Carrier = S·S·C·Tm<br>촉진확산 = ATP ✗ (GLUT)<br>1차 = ATP 직접 (3 Na out · 2 K in)<br>2차 = Na<sup>+</sup> 기울기 (SGLT symport)'),
          ('⚡ 막전위', 'E<sub>K</sub> −90 · E<sub>Na</sub> +60 · RMP −70<br>E = 61/z · log(out/in)<br>RMP ≈ E<sub>K</sub> ← K<sup>+</sup> 투과도 ↑<br>펌프 · K<sup>+</sup> 유출 · Na<sup>+</sup> 소량 · A<sup>−</sup>')],
         '<ol><li>Hypotonic = 세포 <b>부풂</b></li><li>SGLT = <b>2차</b>, 펌프 = <b>1차</b></li><li>RMP의 주된 원인 = <b>K<sup>+</sup> 유출</b> (펌프 ✗)</li></ol>',
         ['Carrier-mediated transport displays specificity, saturation (transport maximum, Tm), and competition.',
          'The equilibrium potential is the membrane potential at which the electrical gradient exactly balances the concentration gradient for an ion.',
          'The resting potential is close to E<sub>K</sub> because the resting membrane is much more permeable to K<sup>+</sup> than to Na<sup>+</sup>.'])
