from lib import *

def build():
    chapter(6, 'PNS: Afferent & Special Senses')
    c = CH['color']
    page('CHAPTER 6', 'The PNS: Afferent Division · Special Senses — 한 장 지도',
        chev([('6.1 수용기', '변환·적응', '#c94f0c'), ('6.2 통증', 'Aδ vs C', c), ('6.3 눈', '조절·광변환', '#f76707'), ('6.4 귀', 'Corti·전정', '#fd7e14'), ('6.5 화학감각', '미각·후각', '#d9480f')]) +
        grid('1fr 1fr',
            col(card('한 줄 요약', '수용기는 <span class="hy">자극 에너지 → 수용기전위(등급전위) → 활동전위</span>로 바꾸는 통역사. 통증은 <span class="hg">적응하지 않는 경보</span>, 눈은 <span class="hp">빛이 오면 오히려 과분극</span>, 귀는 <b>Corti 기관 털세포</b>로 소리를, <b>반고리관·이석기관</b>으로 균형을, 혀·코는 <b>화학수용기</b>로.', 'sum big'),
                card('💡 숫자', '미뢰당 수용기 세포 <b>~50</b> · 기본 맛 <b>5</b> · 반고리관 <b>3</b> · 이소골 <b>3</b> · 후각 수용기 교체 <b>~2개월</b>', 'tip')),
            card('🎯 교수님 예시문제(Ch 6) + 핵심 대비', tbl(['문제 / 비교', '정답 · 한 줄'], [
                ['The sense organ for hearing is the ____.', '<b>organ of Corti</b> (창·뼈·막·고막은 전달 구조)'],
                ['The retinal photoreceptor cells are ____.', '<b>rods and cones</b>'],
                ['Tonic vs Phasic', '느린 적응(근방추·통증) vs 빠른 적응(Pacinian)'],
                ['Aδ vs C fiber', '유수·날카로움 vs 무수·둔함(polymodal)'],
                ['Near vs Far vision', '섬모체근 수축·렌즈 둥글 vs 이완·납작'],
                ['Semicircular vs Otolith', '회전 vs 직선·중력']]), 'warn')), 'Slides 1–34')

    page('PART 01', '수용기 생리 — 자극을 전기로 번역하기',
        grid('1fr 1.05fr 1fr',
            col(card('정의', '<b>Stimulus</b> = 몸이 감지 가능한 변화 · <b>Sensory transduction</b> = <span class="hg">자극 에너지 → 수용기전위</span> · 각 수용기는 <b>adequate stimulus(적합 자극)</b>에 가장 민감', 'def'),
                card('🛰 수용기 6종', tbl(['수용기', '적합 자극'], [['Photo', '가시광선'], ['Mechano', '기계 에너지(촉각·소리·늘어남)'], ['Thermo', '열·냉'], ['Osmo', 'ECF 용질 농도'], ['Chemo', '특정 화학물질'], ['Noci', '통증·조직 손상']]))),
            col(card('⚡ Receptor potential', '자극 → 투과도 변화(보통 비특이 양이온 통로 → Na<sup>+</sup> 유입) → <b>등급전위</b>(국소 탈분극) → 강할수록 ↑ → AP <b>빈도</b> ↑<br><span class="hp">예외: 광수용기는 과분극</span>', 'tip'),
                card('수용기 형태 2가지', tbl(['형태', 'AP'], [['구심 뉴런의 <b>특수 말단</b>(촉각, Pacinian)', '수용기 <b>바로 옆 막</b>에서 AP'], ['<b>별도 수용기 세포</b>(미각·털세포·광수용기)', '수용기 세포가 <b>NT 방출</b> → 구심 뉴런 AP']])),
                img('c6-08', 'AP 개시: 구심 = 수용기 옆 / 사이신경·원심 = 축삭둔덕', '58mm')),
            col(card('🔁 적응 Adaptation', tbl(['', 'Tonic 긴장성', 'Phasic 위상성'], [['적응', '<b>안 하거나 느림</b>', '<b>빠름</b>'], ['정보', '자극 <b>지속</b>', '세기 <b>변화</b>, 제거 시 <b>off response</b>'], ['예', '근방추, 관절 수용기, <b>통증</b>', '<b>Pacinian</b>, 촉각(옷 감각 사라짐)']])),
                img('c6-09', '(a) 긴장성 (b) 위상성 + off 반응', '44mm'))), 'Slides 5–9')

    page('PART 02', '촉각 수용기 · 구심 경로 · 통증',
        grid('1fr 1fr 1fr',
            col(card('✋ 촉각 수용기 5종', tbl(['수용기', '적응', '감지'], [['Hair receptor', '빠름', '털 움직임, 가벼운 접촉'], ["<b>Merkel's disc</b>", '<b>느림</b>', '지속적 가벼운 접촉'], ['<b>Pacinian</b>', '빠름', '<b>진동</b>, 깊은 압력'], ['<b>Ruffini</b>', '<b>느림</b>', '지속 깊은 압력, 피부 늘어남'], ["Meissner's", '빠름', '가벼운 접촉, 간지럼']])),
                card('🧠 암기', '느린 적응 = <b>M·R</b> (Merkel, Ruffini)', 'mint')),
            col(card('🛤 구심 경로', tbl(['경로', '정보'], [['<b>Visceral afferent</b>', '체강 장기 — <b>무의식</b>'], ['<b>Sensory afferent</b>', '피부·근육·관절·특수감각기 — <b>의식</b>']]) +
                    '<p><b>Somatic sense</b>: 촉각·압각·진동·온도·통증·<b>고유감각</b><br><b>Special senses</b>: 시각(망막)·청각(Corti)·후각(후각상피)·미각(미뢰)·<b>평형(전정기관)</b></p>'),
                card('정의', '<b>Pain</b> = 위험 감지 <b>nociceptor</b> 자극으로 촉발되는 <b>보호 기전</b>. <span class="hy">Nociceptors do NOT adapt</span> → 손상이 있는 한 경고 · 통증 기억 → 미래 회피', 'def')),
            col(card('🔪 침해수용기 3종', tbl(['종류', '자극'], [['Mechanical', '자르기·으깨기·꼬집기'], ['Thermal', '극단적 온도'], ['<b>Polymodal</b>', '모든 손상 자극(손상 화학물질)']])),
                card('Aδ vs C', tbl(['', 'Fast (A-delta)', 'Slow (C)'], [['수초', '<b>유수</b>', '<b>무수</b>'], ['수용기', '기계·열', '<b>polymodal</b>'], ['통증', '<b>날카롭고 찌르는</b>', '<b>둔하고 쑤시고 타는</b>']]) + '통증 섬유 NT = <span class="hg">substance P + glutamate</span>', 'tip'),
                card('🔨 망치로 손가락', '① "앗!" 날카로운 첫 통증 = Aδ → ② 몇 초 뒤 욱신 = C', 'why'))), 'Slides 10–15')

    qpage('PART 01–02', '수용기 · 통증',
        TF([('Receptor potentials are action potentials propagated without decrement.', '수용기전위는 감쇠 없이 전파되는 AP이다.'),
            ('Phasic receptors adapt rapidly and signal changes in stimulus intensity.', '위상성 수용기는 빠르게 적응하며 자극 세기의 변화를 알린다.'),
            ('Nociceptors adapt rapidly to sustained stimulation.', '침해수용기는 지속 자극에 빠르게 적응한다.'),
            ("Merkel's discs are rapidly adapting receptors for vibration.", '메르켈 원반은 진동을 감지하는 빠른 적응 수용기이다.'),
            ('Visceral afferents carry subconscious information from internal organs.', '내장 구심은 내부 장기의 무의식적 정보를 전달한다.')],
           'F T F F T', '(1) → <b>graded</b> potentials (3) → do <b>not</b> adapt (4) → <b>slowly</b> adapting, sustained touch; vibration = Pacinian.'),
        MC('Which TWO statements describe slow pain fibers (C fibers)? <b>(Choose two.)</b>', 'C 섬유를 설명하는 두 개는?',
           [('They are unmyelinated.', '무수 섬유'), ('They produce sharp, pricking pain.', '날카로운 통증'), ('They are activated by polymodal nociceptors.', '다형 침해수용기가 활성화'),
            ('They are the fastest afferent fibers.', '가장 빠른 구심 섬유'), ('They release acetylcholine.', 'ACh 방출')], '①, ③', '날카로운 = Aδ. 통증 NT = substance P, glutamate.', pick=2),
        MC('Which tactile receptor is rapidly adapting and senses vibration and deep pressure?', '빠르게 적응하며 진동·깊은 압력을 감지하는 촉각 수용기는?',
           [("Merkel's disc", '메르켈 원반'), ('Ruffini ending', '루피니 종말'), ('Pacinian corpuscle', '파치니 소체'), ('muscle spindle', '근방추'), ('free nerve ending', '자유신경종말')], '③', 'Pacinian = 양파 모양 → 진동.', stars=1))

    page('PART 03', '눈 — 구조 · 홍채 · 원근 조절',
        grid('1fr 1fr 1fr',
            col(card('👁 구조 3층 + 2공간', tbl(['층', '구조'], [['바깥', '<b>Sclera</b>(흰자) + <b>Cornea</b>(투명, 굴절)'], ['중간', '<b>Choroid</b>(혈관 → 망막 영양) · <b>Ciliary body</b>(방수 생성 + 수정체 조절) · <b>Iris</b>'], ['안쪽', '<b>Retina</b> = 색소층 + 신경층(막대·원뿔)']]) +
                    '<p><b>Aqueous humor</b>(앞) / <b>Vitreous humor</b>(뒤) — 수정체로 분리<br>보호: 안와, 눈꺼풀, <b>눈물</b>(윤활·세척·살균), 속눈썹</p>'),
                card('🌗 홍채 = 자율신경 평활근', tbl(['상황', '신경', '근육', '동공'], [['밝음', '<b>부교감</b>', '<b>Circular</b>', '축소'], ['어두움·흥분', '<b>교감</b>', '<b>Radial</b>', '확대']]), 'tip')),
            col(card('🔍 Accommodation — 헷갈림 1위', '<ul><li><b>먼 곳</b>: 섬모체근 <b>이완</b> → 현수인대 <b>팽팽</b> → 수정체 <b>납작</b></li><li><b>가까운 곳</b>: 섬모체근 <b>수축</b>(부교감) → 인대 <b>느슨</b> → 수정체 <b>둥글</b>(강한 렌즈)</li><li>노안 = 수정체 탄력 ↓</li></ul>', 'def'),
                card('🧠 직관 교정', '"근육이 당겨서 렌즈를 둥글게"가 <b>아니라</b>, 근육이 수축하면 인대가 풀려서 렌즈가 <b>스스로</b>(탄성) 둥글어진다.', 'why')),
            img('c6-20', '이완(먼 곳, 납작) vs 수축(가까운 곳, 둥글)', '125mm')), 'Slides 17–20')

    page('PART 04', '광수용기와 광변환 — 빛이 오면 끈다',
        grid('1fr 1fr 1fr',
            col(card('📷 광수용기 3부분', '<b>Outer segment</b>(광색소, 빛 감지) · <b>Inner segment</b>(대사) · <b>Synaptic terminal</b>(NT 저장·방출)'),
                card('Rods vs Cones', tbl(['', 'Rods', 'Cones'], [['빛', '<b>희미한 빛</b>(야간), 민감', '<b>밝은 빛</b>'], ['색', '흑백', '<b>색</b>(적·녹·청)'], ['해상도', '낮음', '<b>높음</b>, 중심와 밀집']])),
                card('망막 신경층', '광수용기 → <b>bipolar</b> → <b>ganglion cell</b>(AP 생성, 축삭 = 시신경) + 옆 연결 horizontal·amacrine. <b>광수용기 = rods와 cones뿐</b>', 'mint')),
            card('⚡ Phototransduction', flow('빛', 'retinal 구조 변화', '(cGMP ↓)', 'Na<sup>+</sup> 통로 닫힘', '<b>과분극</b>', '<b>glutamate ↓</b>', 'bipolar 변화', '<b>ganglion AP</b>', '시각 지각', small=True) +
                '<p style="margin-top:2mm"><b>어둠</b>: Na<sup>+</sup> 통로 열림(암전류) → 탈분극 → glutamate <b>계속 방출</b><br><b>빛</b>: 이 방출을 <b>줄이는</b> 신호</p>', 'def'),
            col(card('⚠ 함정', '<ul><li>다른 감각 수용기 = 탈분극 / <b>광수용기 = 과분극</b></li><li>첫 AP = <b>ganglion cell</b> (광수용기·bipolar는 등급전위)</li><li>교수님 예시: bipolar·ganglion·amacrine은 광수용기 ✗</li></ul>', 'warn'),
                card('💡 비유', '광수용기는 "어둠 속에서 계속 말하다가 빛이 오면 입을 다무는" 세포 → 침묵이 곧 메시지', 'tip'))), 'Slides 21–22')

    qpage('PART 03–04', '눈',
        MC('The retinal photoreceptor cells are ____.', '망막의 광수용기 세포는 ____.',
           [('rods and cones', '막대와 원뿔'), ('bipolar and horizontal cells', '양극·수평세포'), ('ganglion and bipolar cells', '신경절·양극세포'), ('amacrine cells and rods', '아마크린·막대'), ('rods, cones and bipolar cells', '막대·원뿔·양극')], '①',
           '광색소를 가진 세포는 rods·cones뿐.', stars=1, prof=True),
        MC('When the eye focuses on a near object, ____.', '가까운 물체에 초점을 맞출 때 ____.',
           [('the ciliary muscle relaxes and the lens flattens', '섬모체근 이완, 렌즈 납작'), ('the ciliary muscle contracts, the suspensory ligaments slacken, and the lens rounds', '섬모체근 수축, 인대 느슨, 렌즈 둥글'),
            ('the ligaments become taut and the lens rounds', '인대 팽팽, 렌즈 둥글'), ('the iris radial muscle contracts', '홍채 방사근 수축'), ('the cornea changes shape', '각막 모양 변화')], '②', '근 수축 → 인대 느슨 → 렌즈 스스로 둥글게.'),
        TF([('In bright light, parasympathetic stimulation contracts the circular muscle of the iris.', '밝은 빛에서 부교감 자극은 홍채 환상근을 수축시킨다.'),
            ('When light strikes a photoreceptor, it depolarizes and releases more glutamate.', '빛을 받으면 광수용기는 탈분극되어 glutamate를 더 방출한다.'),
            ('Cones provide color vision and high acuity.', '원뿔세포는 색각과 높은 해상도를 담당한다.'),
            ('Ganglion cells are the first retinal cells to generate action potentials.', '신경절세포가 망막에서 처음 AP를 만든다.'),
            ('Rods are most useful in bright light.', '막대세포는 밝은 빛에서 가장 유용하다.')],
           'T F T T F', '(2) → <b>hyperpolarizes</b>, <b>decreases</b> glutamate (5) → rods = <b>dim light</b>.'))

    page('PART 05', '귀 — 청각',
        grid('1.1fr 1fr 1fr',
            col(card('🔊 소리의 길', flow('음파', 'Pinna·외이도', '<b>Tympanic membrane</b>', '<b>Malleus → Incus → Stapes</b>', '<b>Oval window</b>', '달팽이관 액체 파동', '<b>Basilar membrane</b>', '<b>Corti 털세포</b> 굽힘', '수용기전위 → NT → 청신경 AP', small=True), 'tip'),
                card('🌊 음파', '공기의 <b>압축(compression)</b>과 <b>희박(rarefaction)</b> · 액체는 관성이 커서 에너지가 더 필요 → <b>외이·중이가 증폭</b> · 외이 = 소리 <b>위치 파악</b>' + tbl(['성질', '물리량'], [['<b>Pitch</b>', '<b>진동수</b> (기저막 진동 위치)'], ['<b>Intensity</b>', '<b>진폭</b>'], ['<b>Timbre</b>', '<b>배음</b>']]))),
            card('🐌 Cochlea & Organ of Corti', '<ul><li><b>Cochlea</b> = 내이의 청각 부분, 완두콩 크기 달팽이, 액체 → 진동을 전기로</li><li><b>Organ of Corti</b> = <span class="hy">청각의 감각기관</span>, 기저막 위, 털세포</li><li><b>Inner hair cells</b>: 액체 진동 → <b>전기 신호(뇌로)</b></li><li><b>Outer hair cells</b>: 뇌에 신호 X, <b>미세기계적 증폭기</b> → 민감도·구별력 ↑</li></ul>', 'def'),
            col(card('⚠ 교수님 예시: sense organ for hearing', 'oval window(창) · ossicles(뼈) · basilar membrane(막) · tympanic membrane(고막) = 모두 <b>전달 구조</b><br>털세포를 가진 <b>감각기관</b> = <b>organ of Corti ✔</b>', 'warn'),
                card('🧠 암기', '이소골 = "<b>망·침·등</b>"(망치·모루·등자) = Malleus · Incus · Stapes', 'mint'))), 'Slides 24–29')

    page('PART 06', '평형감각 · 미각 · 후각',
        grid('1fr 1fr 1fr',
            col(card('⚖ Vestibular apparatus', tbl(['구조', '감지'], [['<b>Semicircular canals</b> (3: lateral·superior·posterior)', '<b>회전</b> 머리 운동, 회전 가속'], ['<b>Otolith organs</b>: Utricle · Saccule', '<b>직선 가속</b>, 중력, 머리 기울기 — <b>이석(CaCO<sub>3</sub>)</b>이 털세포를 굽힘']]) +
                    '<p>→ 눈과 협응(<b>vestibulo-ocular reflex</b>), 자세와 협응(<b>vestibulospinal reflex</b>)</p>', 'def'),
                card('🧠 암기', '"반고리 = <b>원</b> = 회전" · "이석 = <b>돌의 무게</b> = 중력·직선"', 'mint')),
            card('👅 Gustation 미각', '<ul><li>주로 혀의 <b>taste bud</b> — <b>~50개</b> 수용기 세포 + 지지세포</li><li><b>Taste pore</b>로 침에 녹은 물질 접촉</li><li>결합 → <b>수용기전위(탈분극)</b> → <b>V-gated Ca<sup>2+</sup></b> → NT 방출 → 감각 신경 AP</li><li>5맛: <b>salty, sour, sweet, bitter, umami</b> — 구별은 수용기 활동 <b>패턴</b></li><li>경로: 뇌간 → <b>시상</b> → 1차 미각 피질</li></ul><p>화학 감각 = 섭취 전 품질 검사 + 소화액·식욕에 영향</p>'),
            col(card('👃 Olfaction 후각', '후각 수용기 = <span class="hy">재생 가능한 구심 뉴런 자체</span>의 말단<ul><li><b>Receptor cells</b>: 냄새 감지</li><li><b>Supporting cells</b>: 점액 분비</li><li><b>Basal cells</b>: 전구체 → <b>~2개월마다 교체</b></li></ul>'),
                card('⚠ 대비', '미각 수용기 = <b>상피세포</b>(별도 세포, NT 방출)<br>후각 수용기 = <b>뉴런 자체</b>(교체되는 예외 뉴런)', 'warn'))), 'Slides 30–34')

    qpage('PART 05–06', '귀 · 화학 감각',
        MC('The sense organ for hearing is the ____.', '청각의 감각기관은 ____.',
           [('oval window', '난원창'), ('organ of Corti', '코르티 기관'), ('ossicles', '이소골'), ('basilar membrane', '기저막'), ('tympanic membrane', '고막')], '②', '털세포를 가진 구조 = Corti.', stars=1, prof=True),
        MC('Rotational acceleration is detected by the ____, whereas linear acceleration and head tilt are detected by the ____.', '회전 가속은 ____, 직선 가속·기울기는 ____이 감지한다.',
           [('cochlea; semicircular canals', '달팽이관; 반고리관'), ('semicircular canals; utricle and saccule', '반고리관; 타원낭·구형낭'), ('utricle; saccule', '타원낭; 구형낭'),
            ('organ of Corti; ossicles', '코르티; 이소골'), ('otolith organs; semicircular canals', '이석기관; 반고리관')], '②', '반고리 = 회전, 이석 = 직선·중력.'),
        TF([('Inner hair cells convert fluid vibration into electrical signals sent to the brain.', '내유모세포는 액체 진동을 뇌로 가는 전기 신호로 바꾼다.'),
            ('Outer hair cells send most auditory signals to the brain.', '외유모세포가 청각 신호 대부분을 뇌로 보낸다.'),
            ('Pitch depends on the frequency of sound waves.', '음높이는 음파의 진동수에 따라 달라진다.'),
            ('Olfactory receptor cells are never replaced.', '후각 수용기 세포는 절대 교체되지 않는다.'),
            ('Taste receptor depolarization opens voltage-gated Ca<sup>2+</sup> channels, triggering NT release.', '미각 수용기 탈분극은 전압개폐 Ca<sup>2+</sup> 통로를 열어 NT 방출을 일으킨다.')],
           'T F T F T', '(2) outer hair cells act as <b>amplifiers</b>, do not signal the brain (4) replaced about every <b>2 months</b> by basal cells.'))

    qpage('PART 03–06', '단답 · 객관식',
        MC('Which TWO are characteristics of cones? <b>(Choose two.)</b>', '원뿔세포의 특징 두 개는?',
           [('Provide color vision', '색각'), ('Most sensitive in dim light', '희미한 빛에서 가장 민감'), ('High acuity, concentrated in the fovea', '높은 해상도, 중심와 밀집'), ('Only black-and-white vision', '흑백만'), ('Their axons form the optic nerve', '축삭이 시신경을 이룸')], '①, ③',
           '② ④ = rods, ⑤ = ganglion cells.', pick=2),
        SA('Which characteristics of a sound wave determine (a) pitch, (b) loudness, and (c) timbre?', '음파의 어떤 성질이 (a) 음높이 (b) 크기 (c) 음색을 결정하나?', '(a) frequency (b) amplitude (c) overtones', 'Pitch–frequency · Intensity–amplitude · Timbre–overtones.'),
        MC('Which statement about olfactory receptor cells is correct?', '후각 수용기 세포의 옳은 설명은?',
           [('They are epithelial cells releasing NT onto afferent neurons.', '구심 뉴런에 NT를 방출하는 상피세포'), ('They are specialized endings of afferent neurons replaced about every two months.', '약 2개월마다 교체되는 구심 뉴런의 말단'),
            ('They are located in taste buds.', '미뢰에 있다'), ('They are mechanoreceptors.', '기계수용기'), ('They never regenerate.', '재생 안 됨')], '②', '① = <b>미각</b> 수용기 설명.'))

    qpage('PART 04–05', '서술형',
        ES('Trace the pathway by which sound waves in the air are converted into action potentials in the auditory nerve.', '공기 중 음파가 청신경 AP로 바뀌는 경로를 서술하시오.',
           'Sound waves are collected by the pinna and travel through the external auditory meatus to the tympanic membrane, which vibrates. The middle ear ossicles (malleus, incus, stapes) transmit and amplify the vibrations to the oval window, which sets up pressure waves in the cochlear fluid. These make the basilar membrane vibrate; different frequencies vibrate different regions. As it moves, the hairs of the hair cells in the organ of Corti are bent, opening mechanically gated channels and producing receptor potentials. Inner hair cells release neurotransmitter onto afferent neurons, generating action potentials in the auditory nerve; outer hair cells act as amplifiers.',
           '고막 → 이소골 → 난원창 → 액체 → 기저막 → 털세포 → 수용기전위 → NT → AP.'),
        ES('Describe how light is converted into a neural signal in the retina, and explain why this is unusual compared with other receptors.', '망막에서 빛이 신경 신호로 바뀌는 과정과, 다른 수용기와 비교해 특이한 점을 설명하시오.',
           'Rods and cones contain photopigments in their outer segments. In the dark, Na<sup>+</sup> channels in the outer segment are open, so the photoreceptor is depolarized and continuously releases glutamate. When light is absorbed, retinal changes shape, activating the photopigment and, through a cascade, closing the Na<sup>+</sup> channels. The photoreceptor hyperpolarizes and decreases glutamate release. This change alters bipolar cell activity, which is relayed to ganglion cells; ganglion cells generate action potentials that travel in the optic nerve to the brain. It is unusual because most receptors depolarize in response to their adequate stimulus, whereas photoreceptors hyperpolarize in response to light.',
           '"어둠 = 탈분극·glutamate 많음, 빛 = 과분극·적음" + 첫 AP = ganglion.'), cols=2)

    memo([('🛰 수용기', '변환 = 자극 → 수용기전위(등급)<br>Tonic = 느린 적응(근방추·통증)<br>Phasic = 빠름(Pacinian), off 반응<br>느린 촉각 = Merkel·Ruffini'),
          ('🔪 통증', 'Nociceptor = <b>적응 X</b><br>기계·열·<b>다형</b><br>Aδ = 유수·날카로움 / C = 무수·둔함<br>NT = substance P + glutamate'),
          ('👁 눈', '밝음 = 부교감·환상근·축소<br>가까이 = 섬모체근 수축·인대 느슨·렌즈 둥글<br>빛 → <b>과분극</b> → glutamate↓ → ganglion AP<br>Rods = 희미·흑백 / Cones = 색·중심와'),
          ('👂 귀·화학', '고막 → 망·침·등 → 난원창 → 기저막 → <b>Corti</b><br>Inner = 신호 / Outer = 증폭<br>반고리 = 회전 / 이석 = 직선·중력<br>미뢰 ~50 · 5맛 / 후각 = 뉴런, 2개월')],
         '<ol><li>청각 감각기관 = <b>organ of Corti</b></li><li>광수용기 = <b>과분극</b>, rods·cones만</li><li>침해수용기는 <b>적응 안 함</b></li></ol>',
         ['Sensory transduction is the conversion of stimulus energy into a receptor potential that may trigger action potentials in the afferent fiber.',
          'For near vision, the ciliary muscle contracts, the suspensory ligaments slacken, and the lens becomes rounder.',
          'The organ of Corti on the basilar membrane is the sense organ for hearing; its inner hair cells transduce fluid movement into electrical signals.'])
