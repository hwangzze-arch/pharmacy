from lib import *

def build():
    chapter(5, 'Central Nervous System')
    c = CH['color']
    page('CHAPTER 5', 'The Central Nervous System — 한 장 지도',
        chev([('5.1 조직', '뉴런 3·교세포 4', '#a61e4d'), ('5.2 보호', '뇌막·CSF·BBB', c), ('5.4 피질', '엽별 분업·언어', '#d6336c'), ('5.5–5.6', '기저핵·시상·변연계', '#e64980'), ('5.7 기억', '습관화·LTP', '#c2255c'), ('5.8–5.9', '소뇌·뇌간', '#a61e4d'), ('5.10 척수', '반사궁', '#7d1235')]) +
        grid('1fr 1fr',
            col(card('한 줄 요약', 'CNS(뇌+척수) = <span class="hy">입력(구심) → 통합(사이신경) → 출력(원심)</span>의 본부. 교세포·뇌막·CSF·<span class="hg">BBB</span>가 지키고, 피질(엽별 분업)·기저핵(운동 억제)·시상(중계)·시상하부(항상성)·변연계(감정·기억)·소뇌(협응)·뇌간(생명 중추)·척수(통로+<span class="hp">반사</span>)가 나눠 맡는다.', 'sum big'),
                card('💡 숫자', '교세포 = 신경계 세포의 <b>90%</b> · 뇌 O<sub>2</sub> <b>20%</b>/포도당 <b>50%</b> · 뇌량 <b>3억</b> 축삭 · 피질 <b>6층</b> · 소뇌 뉴런 <b>50–70%</b> · 척수신경 <b>31쌍</b>, 뇌신경 <b>12쌍</b> · 척수 끝 <b>L1–L2</b>', 'tip')),
            card('🎯 교수님 예시문제(Ch 5) 3개 → 정답', tbl(['문제', '정답'], [
                ['The spinal cord ____.', '<b>integrates reflexes between afferent input and efferent output without involving the brain</b>'],
                ['The primary motor cortex ____.', '<b>is the site of the initiation of voluntary motor activity</b>'],
                ['The blood-brain barrier ____.', '<b>allows oxygen to diffuse across the capillary walls</b>']]) +
                '<p style="margin-top:1.5mm">→ 오답 보기 해부는 PART 02 · 04 · 08 카드에. <b>5개 보기 각각이 왜 틀렸는지</b>까지 외우면 응용 문제도 끝.</p>', 'warn')), 'Slides 1–78')

    page('PART 01', '신경계 조직도 · 뉴런 3종 · 교세포 4종',
        grid('1fr 1.1fr 1fr',
            col(card('🗂 조직도', flow('CNS 뇌·척수', 'PNS', small=True) + flow('PNS', 'Afferent 구심', 'Efferent 원심', small=True) + flow('Efferent', 'Somatic(골격근)', 'Autonomic', small=True) + flow('Autonomic', 'Sympathetic', 'Parasympathetic', small=True) +
                     '+ <b>ENS</b>(소화관 벽 신경망) — 모두 <b>하나의 통합 신경계</b>'),
                card('🧠 뉴런 3종 (교재 기준!)', tbl(['뉴런', '역할'], [
                    ['<b>Afferent</b>', '환경 정보를 <b>CNS로</b> (세포체 = 후근 신경절)'],
                    ['<b>Interneuron</b>', '<b>전부 CNS</b>, 뉴런의 99%+ · 정보 <b>통합</b>·반응 결정·사고·기억'],
                    ['<b>Efferent</b>', 'CNS 명령을 <b>효과기(근육·샘)</b>로']]) + '<small style="color:#c92a2a">⚠ 슬라이드 10은 interneuron·efferent 설명이 뒤바뀜</small>'),
                card('👁 Use it or lose it', '발달기 과잉 생성 → 쓰는 경로만 남음. <b>약시</b> = 눈은 정상, <u>뇌 시각 경로 연결 소실</u>. 발달기에 좋은 눈을 가리면 회복.', 'tip')),
            card('🧩 CNS 교세포 4종 (신경계 세포의 90%)', '<p>AP를 만들지 않음(비흥분성) · 화학 신호로 소통 · 뉴런을 물리·대사·기능적으로 지원 · <span class="hp">계속 분열 → 뇌종양 대부분</span></p>' + tbl(['교세포', '핵심 기능'], [
                    ['<b>Astrocyte</b><br><small>최다, 별 모양</small>', '구조 지지("접착제"), 발달 시 뉴런 이동 <b>발판</b>, <span class="hy">BBB 형성 유도</span>, 혈액→뉴런 영양(젖산), <b>ECF K<sup>+</sup> 조절</b>, NT 흡수·분해, <b>삼자 시냅스</b>, 손상 시 <b>교세포 흉터</b>'],
                    ['<b>Oligodendrocyte</b>', '<span class="hy">CNS 수초</span> (한 세포가 여러 축삭)'],
                    ['<b>Microglia</b>', '<span class="hy">면역 방어</span>(단핵구 유사) · 평소 NGF 분비, <b>시냅스 가지치기</b> · 감염 시 이동·포식·파괴물질'],
                    ['<b>Ependymal</b>', '<span class="hy">뇌실·중심관 내벽</span>, 섬모 · <b>CSF 생성·이동</b> · 신경 줄기세포']]) +
                '<p><small>PNS 수초 = <b>Schwann cell</b></small></p>'),
            col(img('c5-11', '별아교세포(모세혈관·뉴런 연결), 희소돌기, 미세아교, 뇌실막', '62mm'),
                card('🧠 4종 암기', '<b>A</b>strocyte = <b>A</b>ll-round 지원 + BBB<br><b>O</b>ligo = <b>O</b>n 축삭(수초)<br><b>M</b>icroglia = <b>M</b>acrophage 같은 면역<br><b>E</b>pendymal = CSF', 'mint'))), 'Slides 3–15')

    qpage('PART 01', '조직 · 교세포',
        MC('Which glial cell forms myelin sheaths around axons in the CNS?', 'CNS에서 축삭의 수초를 형성하는 교세포는?',
           [('astrocyte', '별아교세포'), ('oligodendrocyte', '희소돌기아교세포'), ('microglia', '미세아교세포'), ('ependymal cell', '뇌실막세포'), ('Schwann cell', '슈반세포')], '②', 'CNS = oligodendrocyte, PNS = Schwann.', stars=1),
        MC('Which TWO are functions of astrocytes? <b>(Choose two.)</b>', '별아교세포의 기능 두 가지는?',
           [('Inducing brain capillaries to form the BBB', '뇌 모세혈관이 BBB를 형성하도록 유도'), ('Producing CNS myelin', 'CNS 수초 생성'), ('Regulating extracellular K<sup>+</sup>', '세포외 K<sup>+</sup> 조절'),
            ('Producing CSF as ciliated lining of the ventricles', '뇌실 섬모 내벽으로 CSF 생성'), ('Phagocytizing debris as monocyte-like immune cells', '단핵구 유사 면역세포로 포식')], '①, ③',
           '② oligodendrocyte ④ ependymal ⑤ microglia.', pick=2, stars=3),
        TF([('Glial cells generate and conduct action potentials like neurons.', '교세포는 뉴런처럼 AP를 만들고 전도한다.'),
            ('About 90% of the cells in the nervous system are glial cells.', '신경계 세포의 약 90%는 교세포이다.'),
            ('Interneurons lie entirely within the CNS.', '사이신경은 전부 CNS 안에 있다.'),
            ('Unlike neurons, glial cells keep dividing, so most brain tumors arise from glia.', '뉴런과 달리 교세포는 계속 분열하므로 뇌종양 대부분이 교세포 기원이다.'),
            ('In amblyopia, the weaker eye itself is structurally defective.', '약시에서 약한 눈 자체에 구조적 결함이 있다.')],
           'F T T T F', '(1) glia do <b>not</b> initiate or conduct impulses (5) 눈은 정상, <b>뇌 시각 경로의 연결 소실</b>.'))

    page('PART 02', '뇌의 보호와 영양 — 뇌막 · CSF · BBB',
        grid('1fr 1fr 1fr',
            col(card('🛡 4중 보호', '① 두개골·척추 ② <b>Meninges</b> ③ <b>CSF</b> ④ <b>BBB</b> — 연약하고 <b>대체 불가</b>한 뉴런 보호'),
                card('뇌막 (바깥 → 안) = D·A·P', tbl(['뇌막', '특징'], [['<b>Dura</b> 경막', '질기고 두꺼움'], ['<b>Arachnoid</b> 거미막', '아래 <b>지주막하 공간</b>에 CSF, <b>거미막 과립</b>이 CSF를 정맥으로 재흡수'], ['<b>Pia</b> 연막', '뇌 표면 밀착, 혈관 풍부']])),
                card('💧 CSF', '뇌실의 <span class="hy">맥락총(choroid plexus)</span>에서 생성 → 4개 뇌실 → 지주막하 공간 → 거미막 과립 재흡수. 역할: <b>완충(뇌가 떠 있음)</b> + 간질액과 물질 교환. 막히면 수두증.', 'mint')),
            col(card('🚧 Blood–brain barrier', '<ul><li>구조: 뇌 모세혈관의 <span class="hy">밀착연접</span> — <b>astrocyte가 유도</b></li><li>혈중 화학 변동·해로운 물질·<b>NT로도 작용하는 호르몬</b> 차단</li><li><b>통과 O</b>: 지용성(O<sub>2</sub>, CO<sub>2</sub>, 알코올, 마취제) · 포도당은 <b>GLUT1</b></li><li><b>통과 X</b>: 대부분 수용성, <b>많은 약물</b> (도파민 ✗ → <b>L-dopa ✔</b>)</li><li>뇌 전체 균일 X (시상하부 일부 없음)</li></ul>', 'def'),
                card('🍞 뇌는 왜 혈류에 목숨을 거나', '<b>무산소로 ATP 못 만듦</b> + <b>포도당 저장 못 함</b> → 체중 2%인데 휴식 시 <b>O<sub>2</sub> 20%, 포도당 50%</b> 사용 → 몇 분 허혈 = 손상(뇌졸중)', 'why')),
            col(img('c5-20', 'CSF 생성(맥락총) → 순환 → 재흡수(거미막 과립)', '72mm'),
                card('⚠ 교수님 예시 BBB 오답 해부', '① microglia 작용 ✗ → <b>astrocyte</b><br>② 지용성을 막음 ✗ → 지용성은 <u>통과</u><br>③ <b>O<sub>2</sub>가 확산 통과 ✔</b><br>④ K<sup>+</sup> 조절의 주 기전 ✗ → <b>astrocyte</b><br>⑤ 뇌 전체 균일 ✗', 'warn'))), 'Slides 17–22')

    qpage('PART 02', '뇌의 보호',
        MC('The blood-brain barrier ____.', '혈액-뇌 장벽은 ____.',
           [('results from the actions of microglia cells', '미세아교세포 작용의 결과이다'), ('prevents most lipid-soluble substances from moving between the blood and brain interstitial fluid', '대부분의 지용성 물질의 이동을 막는다'),
            ('allows oxygen to diffuse across the capillary walls', '산소가 모세혈관벽을 확산 통과하게 한다'), ('is the primary mechanism that controls K<sup>+</sup> levels in brain interstitial fluid', '뇌 간질액 K<sup>+</sup> 조절의 주 기전이다'), ('is uniform across the entire brain', '뇌 전체에 균일하다')], '③',
           'O<sub>2</sub> = 지용성 → 자유 확산. BBB 유도·K<sup>+</sup> 조절 = astrocyte.', stars=2, prof=True),
        MC('Cerebrospinal fluid is formed mainly by the ____ and circulates in the ____.', 'CSF는 주로 ____에서 생성되어 ____에서 순환한다.',
           [('arachnoid villi; epidural space', '거미막 융모; 경막외 공간'), ('choroid plexuses; ventricles and subarachnoid space', '맥락총; 뇌실과 지주막하 공간'), ('dura mater; subdural space', '경막; 경막하 공간'),
            ('astrocytes; capillaries', '별아교세포; 모세혈관'), ('pia mater; central canal only', '연막; 중심관만')], '②', '생성 = 맥락총, 흡수 = 거미막 과립.'),
        TF([('The brain cannot produce ATP without O<sub>2</sub> and cannot store glucose.', '뇌는 O<sub>2</sub> 없이 ATP를 못 만들고 포도당을 저장 못 한다.'),
            ('From outside to inside, the meninges are dura, arachnoid, and pia mater.', '바깥부터 뇌막은 경막·거미막·연막 순이다.'),
            ('Dopamine readily crosses the BBB, so it is given directly for Parkinson\'s disease.', '도파민은 BBB를 쉽게 통과하므로 파킨슨병에 직접 투여한다.'),
            ('The BBB is formed by tight junctions between brain capillary cells.', 'BBB는 뇌 모세혈관 세포 사이의 밀착연접으로 형성된다.'),
            ('At rest, the brain uses about 50% of the glucose consumed by the body.', '휴식 시 뇌는 몸이 쓰는 포도당의 약 50%를 사용한다.')],
           'T T F T T', '(3) dopamine <b>cannot</b> cross → precursor <b>levodopa</b> is given.'))

    page('PART 03', '뇌 지도 · 대뇌피질의 구조와 4개 엽',
        grid('1fr 1.05fr 1fr',
            col(card('🗺 뇌 구성 요소', tbl(['부위', '한 줄'], [
                    ['<b>Brain stem</b> (중뇌·교뇌·연수)', '생명 유지, 뇌신경, 망상체, 수면'],
                    ['<b>Cerebellum</b>', '균형·자세·<b>운동 협응</b>'],
                    ['<b>Hypothalamus</b>', '항상성 통합 중추'], ['<b>Thalamus</b>', '감각 중계소'],
                    ['<b>Basal nuclei</b>', '수의 운동 조절(억제)'], ['<b>Cerebral cortex</b>', '운동 개시·최종 지각·사고·언어']]) + '<small>아래(원시) → 위(고등) · 뇌 뉴런 약 850억</small>')),
            col(card('🧱 회백질 vs 백질', '<b>Gray matter</b> = 세포체·가지돌기·시냅스 = <span class="hy">처리 센터</span> → 피질<br><b>White matter</b> = <b>유수 축삭</b> = <span class="hy">전선</span>, 피질 아님<br>좌우 반구 ↔ <b>Corpus callosum</b>(약 3억 축삭)', 'def'),
                card('🧬 피질의 층과 기둥', '<b>6층</b> + 기능 단위 <b>기둥(column)</b>. Layer I = 교세포·축삭. 출력 = <b>추체세포(pyramidal)</b>, 입력·국소 = <b>성상세포(stellate)</b>. 영역 차이 = 독특한 세포가 아니라 <b>층 패턴·입출력 연결</b>.'),
                card('4개 엽', tbl(['엽', '기능'], [['<b>Occipital</b> 후두', '시각'], ['<b>Temporal</b> 측두', '청각'],
                    ['<b>Parietal</b> 두정', '<b>체성감각</b> — <b>postcentral gyrus</b>'], ['<b>Frontal</b> 전두', '<b>수의 운동</b>·말하기·사고 — <b>precentral gyrus</b>']]) + '<b>Central sulcus</b>: 앞 = 운동, 뒤 = 감각', 'tip')),
            img('c5-31', '4개 엽 · 중심고랑 · 외측고랑', '128mm')), 'Slides 24–31')

    page('PART 04', '운동·감각 피질 · 언어 · 연합 영역 · 편재화',
        grid('1fr 1fr 1fr',
            col(card('🎮 운동·감각 피질 3원칙', '<ul><li><b>반대쪽(contralateral)</b>: 왼쪽 피질 → 오른쪽 몸 (척수로 내려가기 전 교차)</li><li><b>체부위 배열(homunculus)</b></li><li>면적 ∝ <b>정밀도</b>(손·입·혀 큼)</li></ul>', 'def'),
                card('고위 운동 영역', tbl(['영역', '역할'], [['Supplementary motor area', '복잡한 운동 <b>프로그래밍·준비</b>'], ['Premotor cortex', '몸·팔을 <b>목표 쪽으로</b>'], ['Posterior parietal cortex', '전운동피질을 <b>안내</b>']])),
                card('⚠ 교수님 예시: primary motor cortex', '① parietal ✗ → <b>frontal</b><br>② 독립적으로 ✗ → 고위 운동영역·소뇌·기저핵과 협력<br>③ post-central ✗ → <b>pre</b>central<br>④ <b>수의 운동 개시 부위 ✔</b><br>⑤ Wernicke와 말하기 ✗ → <b>Broca</b>', 'warn')),
            col(card('🗣 언어 (보통 좌반구)', tbl(['영역', '기능 · 손상'], [
                    ['<b>Broca</b> — 좌 전두엽, 운동영역 근처', '<b>말하기</b>(말 근육) · 이해는 하나 유창하게 말 못함'],
                    ['<b>Wernicke</b> — 두정·측두·후두 교차부', '<b>언어 이해</b>(말·글) · 유창하지만 의미 없는 말']])),
                card('🧠 암기', '<b>Broca = 입(말하기)</b> / <b>Wernicke = 귀(이해)</b>', 'mint'),
                card('Plasticity', '요구에 따라 뇌가 <b>기능적으로 재구성</b>되는 능력', 'tip')),
            col(card('🤝 연합 영역', tbl(['영역', '기능'], [['<b>Prefrontal</b>', '계획·의사결정·창의성·<b>성격</b>·작업기억'], ['<b>Parietal–temporal–occipital</b>', '체성·청각·시각 통합 → 복합 지각, 언어'], ['<b>Limbic</b>', '측두엽 안쪽 — 동기·감정·기억']]) + '<small>피질 전체 = 운동·감각·언어 영역 + 연합 영역</small>'),
                card('↔ Lateralization 편재화', '<b>좌반구</b> = 논리·분석·순차·<b>언어</b><br><b>우반구</b> = 비언어(공간, 음악, 예술)', 'why'))), 'Slides 32–38')

    qpage('PART 03–04', '대뇌피질',
        MC('The primary motor cortex ____.', '1차 운동피질은 ____.',
           [('is located on the parietal lobe', '두정엽에 있다'), ('functions independently to control the movement of skeletal muscles', '골격근 운동을 독립적으로 조절한다'), ('is located on the post-central gyrus', '중심후회에 있다'),
            ('is the site of the initiation of voluntary motor activity', '수의 운동 활동이 개시되는 곳이다'), ("works in conjunction with Wernicke's area to produce spoken language", 'Wernicke 영역과 함께 말을 만든다')], '④',
           '전두엽 <b>precentral</b>. 협력 필요. 말하기 = Broca.', stars=2, prof=True),
        MC('Which TWO lobe–function pairs are correct? <b>(Choose two.)</b>', '엽-기능의 옳은 짝 두 개는?',
           [('Occipital lobe — visual cortex', '후두엽 — 시각 피질'), ('Temporal lobe — somatosensory processing', '측두엽 — 체성감각 처리'), ('Parietal lobe — primary motor cortex', '두정엽 — 1차 운동피질'),
            ('Frontal lobe — voluntary motor movement and speaking', '전두엽 — 수의 운동과 말하기'), ('Occipital lobe — auditory cortex', '후두엽 — 청각 피질')], '①, ④', '측두 = 청각, 두정 = 체성감각, 전두 = 운동.', pick=2),
        TF([('White matter consists mainly of neuronal cell bodies and is the site of integration.', '백질은 주로 세포체로 이루어져 통합이 일어나는 곳이다.'),
            ("Wernicke's area is concerned with language comprehension; Broca's area controls speech muscles.", 'Wernicke는 언어 이해, Broca는 말하기 근육 조절이다.'),
            ('The somatosensory cortex is located in the postcentral gyrus of the parietal lobe.', '체성감각 피질은 두정엽 중심후회에 있다.'),
            ('The left motor cortex controls muscles on the left side of the body.', '왼쪽 운동피질은 몸 왼쪽 근육을 조절한다.'),
            ('The cerebral cortex is organized into six layers.', '대뇌피질은 6층으로 구성된다.')],
           'F T T F T', '(1) → <b>gray</b> matter; white = myelinated axons (4) → the <b>right (opposite)</b> side.'))

    page('PART 05', '기저핵 · 시상 · 시상하부 · 변연계',
        grid('1fr 1fr 1.05fr',
            col(card('🎚 Basal nuclei', '대뇌 백질 깊숙한 회백질 · 운동에서 <span class="hy">억제적 역할</span><ol><li>근긴장 억제</li><li>목적 있는 운동 선택·유지, 불필요한 운동 억제</li><li>느리고 지속적인 수축(자세) 조정</li></ol>'),
                card('🩺 Parkinson\'s disease', '기저핵 <b>도파민 뉴런 파괴</b> → <b>근긴장↑·경직</b>, 원치 않는 움직임(떨림), <b>운동 느림</b> → 치료 <b>L-dopa</b> (도파민은 <span class="hp">BBB 통과 X</span>)', 'warn'),
                card('📡 Thalamus 시상', '<span class="hy">감각 중계소</span> — 불필요한 신호 거르고 중요한 신호를 알맞은 피질로 · <b>주의 집중</b>(밖의 차 vs 아기 울음) · 운동 조절에도', 'mint')),
            card('🌡 Hypothalamus 시상하부 — 항상성 통합 중추', '<b>ANS와 내분비계의 연결고리</b><ul><li>체온</li><li>갈증·소변량</li><li>음식 섭취</li><li><b>뇌하수체 전엽</b> 호르몬 분비 조절</li><li><b>뇌하수체 후엽</b> 호르몬(ADH, 옥시토신) <u>생산</u></li><li>자궁 수축·젖 분비</li><li><b>ANS 조절 중추</b></li><li>감정·행동 패턴</li><li>수면-각성 주기</li></ul>= <span class="hg">INTERNAL ENVIRONMENT REGULATION</span>', 'def'),
            col(card('💗 Limbic system = 기능적 시스템', '뇌간을 둘러싼 전뇌 구조의 고리 — 감정, 생존·종족 보존 행동, 동기, 학습, 기억' + tbl(['구성', '역할'], [
                    ['Cingulate gyrus', '감정 처리·조절'], ['<b>Hippocampus</b>', '<b>장기기억 형성</b>, 공간 탐색'], ['<b>Amygdala</b>', '<b>공포·불안·분노</b>, 투쟁-도피'],
                    ['Hypothalamus', '배고픔·갈증·수면·체온'], ['Septal·Basal nuclei', '보상·동기'], ['Olfactory bulbs', '냄새 ↔ 기억·감정']])),
                card('💊 감정과 NT', '<b>NE, dopamine, serotonin</b>. <span class="hy">모든 항우울제 = CNS의 NE·세로토닌 ↑</span>: <b>SSRI · SNRI · TCA · MAOI</b>', 'tip'))), 'Slides 40–50')

    qpage('PART 05', '기저핵 · 시상하부 · 변연계',
        MC('Which brain region is the main integrating center for homeostasis and links the autonomic nervous system with the endocrine system?', '항상성의 주 통합 중추이며 ANS와 내분비계를 잇는 부위는?',
           [('thalamus', '시상'), ('hypothalamus', '시상하부'), ('cerebellum', '소뇌'), ('basal nuclei', '기저핵'), ('medulla', '연수')], '②', '시상 = 감각 중계.', stars=1),
        SA('Name the limbic structure most associated with (a) fear and anxiety and (b) formation of long-term memory.', '(a) 공포·불안 (b) 장기기억 형성과 가장 관련된 변연계 구조는?',
           '(a) amygdala (b) hippocampus', '<b>A</b>mygdala = <b>A</b>fraid · <b>H</b>ippocampus = <b>H</b>istory.'),
        TF([("Parkinson's disease results from loss of dopamine-releasing neurons in the basal nuclei.", '파킨슨병은 기저핵의 도파민 분비 뉴런 소실로 생긴다.'),
            ('The basal nuclei play an important excitatory role, increasing muscle tone.', '기저핵은 근긴장을 높이는 흥분성 역할을 한다.'),
            ('The thalamus screens out unnecessary sensory signals and relays important ones to the cortex.', '시상은 불필요한 감각 신호를 거르고 중요한 신호를 피질로 보낸다.'),
            ('The limbic system is a single, discrete anatomical structure.', '변연계는 하나의 독립된 해부학적 구조이다.'),
            ('Effective antidepressants increase the availability of norepinephrine and serotonin in the CNS.', '유효한 항우울제는 CNS의 NE·세로토닌 가용성을 높인다.')],
           'T F T F T', '(2) → <b>inhibitory</b> role, inhibits muscle tone (4) → a <b>functional system</b> (ring of structures).'))

    page('PART 06', '학습과 기억 — 습관화 · 민감화 · LTP',
        grid('1fr 1fr 1.05fr',
            col(card('정의', '<b>Learning</b> = 경험으로 지식 획득(보상·처벌) · <b>Memory</b> = 저장, 단계적<br><b>Working memory</b> = 정보를 잠시 붙잡고 조작(전전두엽) · <b>Consolidation</b> = STM → LTM', 'def'),
                card('STM vs LTM', tbl(['', 'Short-term', 'Long-term'], [['지속', '초~시간', '일~년'], ['기전', '<span class="hy">기존 시냅스의 일시 변화</span>', '<span class="hy">단백질 합성 → 새 시냅스</span>'], ['예', '습관화·민감화', 'CREB, 즉시초기유전자']])),
                card('📍 기억 흔적 = 여러 곳', '<b>Hippocampus</b> = 서술(declarative, "무엇")<br><b>Cerebellum</b> = 절차(procedural, "어떻게")<br><b>Prefrontal</b> = 작업 기억', 'mint')),
            card('Habituation vs Sensitization', tbl(['', '습관화', '민감화'], [
                    ['정의', '무관한 자극 반복 → 반응 <b>↓</b>', '강한·해로운 자극 뒤 → 약한 자극에도 <b>↑</b>'],
                    ['예', '시계 소리 무시, 새 방 냄새', '트라우마 후 큰 소리에 과민'],
                    ['목적', '에너지 절약', '위협 대비'],
                    ['기전', '시냅스전 V-gated <b>Ca<sup>2+</sup> 통로 개방 ↓</b> → NT ↓', '<b>세로토닌</b> → <b>시냅스전 촉진</b> → Ca<sup>2+</sup> ↑ → NT ↑']]) +
                '<p style="margin-top:2mm"><b>Presynaptic facilitation</b>: 조절성 NT가 AP를 연장 → NT 방출 ↑ = 민감화의 기전, 반복되면 기억 형성에 기여.<br><small>Kandel의 군소(<i>Aplysia</i>) 연구</small></p>'),
            col(img('c5-57', 'LTP: 글루탐산 → AMPA(Na⁺) + NMDA(Ca²⁺) → 2차 전령·NO', '62mm'),
                card('LTP (long-term potentiation)', '<ul><li>기존 시냅스의 <b>지속적 강화</b> — 많이 쓸수록 강해짐, <b>해마</b>에서 두드러짐</li><li><b>AMPA</b>: 글루탐산 → <b>Na<sup>+</sup></b> → EPSP</li><li><b>NMDA</b>: <span class="hp">글루탐산 + 탈분극 둘 다</span> → <b>Ca<sup>2+</sup></b> → 2차 전령, 역행성 전령 <b>NO</b></li><li>시냅스전 NT↑ · 시냅스후 수용체 삽입↑</li></ul>', 'tip'))), 'Slides 51–60')

    qpage('PART 06', '학습과 기억',
        MC('Which TWO statements about LTP are correct? <b>(Choose two.)</b>', 'LTP에 대한 옳은 설명 두 개는?',
           [('NMDA receptors open only when glutamate binds and the postsynaptic membrane is depolarized.', 'NMDA는 글루탐산 결합 + 시냅스후 탈분극일 때만 열린다.'), ('AMPA receptors mainly permit Ca<sup>2+</sup> entry.', 'AMPA는 주로 Ca<sup>2+</sup>을 통과시킨다.'),
            ('LTP is prevalent in the hippocampus.', 'LTP는 해마에서 두드러진다.'), ('LTP weakens frequently used synapses.', 'LTP는 자주 쓰는 시냅스를 약화시킨다.'), ('LTP requires formation of new neurons.', 'LTP는 새 뉴런 생성이 필요하다.')], '①, ③',
           'AMPA = Na<sup>+</sup>, NMDA = Ca<sup>2+</sup>. 쓸수록 <b>강화</b>, 기존 시냅스.', pick=2, stars=3),
        MC('Becoming accustomed to a ticking clock is an example of ____, which results from ____.', '시계 소리에 익숙해지는 것은 ____의 예이며 ____ 때문이다.',
           [('sensitization; increased presynaptic Ca<sup>2+</sup> entry', '민감화; 시냅스전 Ca<sup>2+</sup> 유입 증가'), ('habituation; decreased opening of presynaptic voltage-gated Ca<sup>2+</sup> channels', '습관화; 시냅스전 Ca<sup>2+</sup> 통로 개방 감소'),
            ('LTP; insertion of AMPA receptors', 'LTP; AMPA 수용체 삽입'), ('habituation; increased serotonin release', '습관화; 세로토닌 방출 증가'), ('consolidation; new protein synthesis', '공고화; 새 단백질 합성')], '②', 'Ca<sup>2+</sup> ↓ → NT ↓ → 반응 ↓.'),
        SA('Name the brain region most associated with (a) declarative, (b) procedural, and (c) working memory.', '(a) 서술 (b) 절차 (c) 작업 기억과 관련된 부위는?',
           '(a) hippocampus (b) cerebellum (c) prefrontal cortex', '"무엇" = 해마, "어떻게" = 소뇌, "지금 들고 있기" = 전전두엽.', stars=2))

    page('PART 07', '소뇌 · 뇌간 · 수면',
        grid('1fr 1.1fr 1fr',
            col(card('🎯 Cerebellum', '후두엽 아래, 뇌간 뒤 · <b>뇌 뉴런의 50–70%</b> · 균형, 수의 운동 계획·실행 — <b>무의식적</b> 운동 조절. 손상 → 협응 장애(ataxia)', 'def'),
                card('소뇌 3부위', tbl(['부위', '역할'], [['<b>Vestibulo</b>cerebellum', '<b>균형</b>, 눈 운동'], ['<b>Spino</b>cerebellum', '<b>근긴장 강화</b>, 숙련 운동 협응'], ['<b>Cerebro</b>cerebellum', '수의 운동 <b>계획·개시</b>']]) + '<small>이름 = 입력원: 전정(귀) / 척수 / 대뇌</small>')),
            card('🌿 Brain stem 5기능 (중뇌·교뇌·연수)', '<ol><li>대부분의 <b>뇌신경(12쌍)</b> 기원 — 머리·목 감각·운동 · <b>X 미주신경</b>은 흉·복강까지(부교감)</li><li>심혈관·<b>호흡</b>·소화 중추 (주로 <b>연수</b>)</li><li>평형·자세 반사 (주로 <b>중뇌</b>)</li><li><b>Reticular formation</b> 망상체: 각성·운동·자율 허브<br>· <b>ARAS</b>(중뇌+상부 교뇌) = 피질 각성·<b>의식</b><br>· <b>DRS</b>(교뇌·연수) = 운동·자세·자율</li><li><b>수면</b> 중추 (주로 <b>교뇌</b>)</li></ol>'),
            col(card('😴 EEG와 수면', '<ul><li><b>EEG</b> = 피질 뉴런의 <b>시냅스후 전위</b> 기록</li><li>수면 = 능동적 과정: <b>서파수면(숙면)</b> ↔ <b>역설수면(REM)</b></li><li>주기 = 망상체 각성계 + 서파수면 중추(<b>시상하부</b>) + 역설수면 중추(<b>교뇌</b>)</li></ul>', 'tip'),
                card('⚠ 함정', '"최종 지각"은 피질, "언어 이해"는 Wernicke, "서술 기억"은 해마 — 뇌간 보기에 섞여 나옴', 'warn'))), 'Slides 62–67')

    page('PART 08', '척수 · 척수신경 · 반사',
        grid('1fr 1fr 1fr',
            col(card('🦴 척수', '<ul><li>길이 45 cm, 척주관 안 · 척주가 더 자라 <b>L1–L2</b>에서 끝</li><li><b>요추천자 L3–L4 / L4–L5</b></li><li>단면: <span class="hp">바깥 백질, 안 나비 모양 회백질</span> (뇌 피질과 반대!)</li><li>백질 = <b>tracts</b>: Ascending(감각↑) / Descending(운동↓), 이름 = 출발-도착</li></ul>'),
                img('c5-72', '회백질: 후각 · 측각 · 전각', '40mm'),
                card('', tbl(['뿔', '세포체'], [['<b>Dorsal</b>', '구심이 끝나는 <b>사이신경</b>'], ['<b>Ventral</b>', '골격근 <b>체성 운동뉴런</b>'], ['<b>Lateral</b>', '<b>자율</b> 원심 뉴런']]))),
            col(card('🔌 척수신경 31쌍', '<b>8C · 12T · 5L · 5S · 1Co</b><br><b>Dorsal root</b> = <span class="hy">구심 진입</span> (세포체 = <b>후근 신경절</b>)<br><b>Ventral root</b> = <span class="hy">원심 출구</span><br>척수신경 = 구심+원심 <b>혼합</b>', 'def'),
                card('용어', '<b>Ganglion</b> = CNS <b>밖</b> 세포체 모임 / <b>Nucleus</b> = CNS <b>안</b><br><b>Nerve</b> = PNS 축삭 다발 (CNS엔 nerve 없음 → tract)<br>PNS = 척수신경 31 + 뇌신경 12쌍<br><b>Dermatome</b> = 한 신경근이 담당하는 피부'),
                card('⚠ 교수님 예시: spinal cord', '① solely 통로 ✗ ② 회백질이 바깥 ✗ ③ <b>반사 통합 ✔</b> ④ 구심 = ventral ✗(dorsal) ⑤ L5 넘어 ✗(L1–L2)', 'warn')),
            col(card('🔁 반사궁 5요소', flow('Receptor', 'Afferent', 'Integrating center', 'Efferent', 'Effector', small=True) + '척수 역할 ① 뇌↔몸 <b>통로</b> ② 뇌 없이 <b>반사 통합</b>', 'tip'),
                card('반사 분류', tbl(['분류', '예'], [['Spinal', '무릎반사, 뜨거운 난로'], ['Cranial', '동공·각막반사, 재채기, 기침'], ['Innate / Conditioned', '회피 / 음식 냄새에 침·운동 기술'],
                    ['Somatic / Autonomic', '골격근 / 평활·심장근·샘'], ['<b>Monosynaptic</b>', '슬개건·발목·이두근(신장반사)'], ['<b>Polysynaptic</b>', '그 외 전부(회피반사)']])))), 'Slides 69–78')

    qpage('PART 07–08', '소뇌 · 뇌간 · 척수',
        MC('The spinal cord ____.', '척수는 ____.',
           [('functions solely as a pathway for signals originating in the cerebrum', '대뇌 신호의 통로로만 기능한다'), ('is organized similarly to the brain, with grey matter surrounding white matter', '뇌처럼 회백질이 백질을 둘러싼다'),
            ('integrates reflexes between afferent input and efferent output without involving the brain', '뇌 없이 구심 입력과 원심 출력 사이 반사를 통합한다'), ('receives afferent signals along the ventral root', '전근으로 구심 신호를 받는다'), ('extends past the fifth lumbar vertebra', '5번 요추를 지나 연장된다')], '③',
           '① solely ✗ ② 백질이 바깥 ④ dorsal ⑤ L1–L2.', stars=2, prof=True),
        MC('Which TWO functions are associated with the brain stem? <b>(Choose two.)</b>', '뇌간과 관련된 기능 두 개는?',
           [('Origin of most cranial nerves', '대부분 뇌신경의 기원'), ('Final perception of sensory input', '감각의 최종 지각'), ('Centers for respiration and cardiovascular control', '호흡·심혈관 중추'),
            ('Comprehension of language', '언어 이해'), ('Storage of declarative memories', '서술 기억 저장')], '①, ③', '② 피질 ④ Wernicke ⑤ 해마.', pick=2),
        MC('The patellar (knee-jerk) reflex is best classified as ____.', '슬개건 반사의 분류는?',
           [('cranial, conditioned, autonomic', '뇌, 조건, 자율'), ('spinal, innate, somatic, monosynaptic', '척수, 선천, 체성, 단일시냅스'), ('spinal, innate, autonomic, polysynaptic', '척수, 선천, 자율, 다시냅스'),
            ('cranial, innate, somatic, polysynaptic', '뇌, 선천, 체성, 다시냅스'), ('spinal, conditioned, somatic, monosynaptic', '척수, 조건, 체성, 단일')], '②', '사이신경 없이 구심 → 운동뉴런 직접.'))

    qpage('PART 07–08', '척수 · 반사 · 소뇌',
        TF([('Cell bodies of afferent neurons lie in the dorsal root ganglia; somatic motor neuron cell bodies lie in the ventral horn.', '구심 뉴런 세포체는 후근 신경절에, 체성 운동뉴런 세포체는 전각에 있다.'),
            ('A ganglion is a collection of neuronal cell bodies within the CNS.', '신경절은 CNS 안의 세포체 모임이다.'),
            ('A nerve contains complete neurons, including their cell bodies.', '신경은 세포체를 포함한 완전한 뉴런을 담고 있다.'),
            ('Most brain neurons are found in the cerebellum.', '뇌 뉴런의 대부분은 소뇌에 있다.'),
            ('Spinal taps are performed at L3–L4 or L4–L5 to avoid injuring the spinal cord.', '요추천자는 척수 손상을 피하려고 L3–L4 또는 L4–L5에서 한다.')],
           'T F F T T', '(2) → <b>outside</b> the CNS (inside = nucleus/center) (3) → only <b>axons</b>; there are no nerves in the CNS.'),
        SA('List, in order, the five components of a reflex arc.', '반사궁 5요소를 순서대로 쓰시오.',
           'Sensory receptor → afferent pathway → integrating center → efferent pathway → effector organ', '1장 조절계(감지 → 통합 → 조정)와 같은 구조.'),
        SA('Name the three functional parts of the cerebellum and one role of each.', '소뇌 세 부위와 역할을 쓰시오.',
           'Vestibulocerebellum — balance and eye movement; spinocerebellum — muscle tone and skilled voluntary movement; cerebrocerebellum — planning and initiating voluntary activity', '이름 = 입력원.', stars=2))

    qpage('PART 02 · 06', '서술형',
        ES('Describe the four major features that protect the CNS, and explain why the blood–brain barrier is both beneficial and a problem in medicine.', 'CNS를 보호하는 4가지 특징과, BBB가 이로우면서도 의학적으로 문제인 이유를 서술하시오.',
           'The CNS is protected by (1) the bony cranium and vertebral column; (2) three meninges — dura, arachnoid, and pia mater — which wrap and protect it; (3) cerebrospinal fluid, produced by the choroid plexuses of the ventricles, which cushions the brain and exchanges materials with brain interstitial fluid; and (4) the blood–brain barrier, formed by tight junctions between brain capillary cells induced by astrocytes. The BBB is beneficial because it limits exchange between blood and brain, protecting neurons from chemical fluctuations, harmful substances, and hormones that could act as neurotransmitters. However, many drugs cannot cross it, limiting treatment of brain disorders (e.g., dopamine must be given as L-dopa).',
           '4요소 + BBB 구조(tight junction, astrocyte) + 장·단점 각 1개.'),
        ES('Compare short-term and long-term memory, and explain habituation and sensitization at the synaptic level.', 'STM과 LTM을 비교하고 습관화·민감화를 시냅스 수준에서 설명하시오.',
           'Short-term memory lasts seconds to hours and involves transient modifications of preexisting synapses. Long-term memory lasts days to years and requires synthesis of new proteins (e.g., via CREB) leading to new synapses or permanent structural changes; information is transferred by consolidation. Habituation is a decreased response to a repeated indifferent stimulus: presynaptic voltage-gated Ca<sup>2+</sup> channels open less, so less Ca<sup>2+</sup> enters and less neurotransmitter is released. Sensitization is an increased response to mild stimuli after a strong or noxious stimulus: serotonin causes presynaptic facilitation, increasing Ca<sup>2+</sup> entry and neurotransmitter release.',
           '비교 3요소 + Ca<sup>2+</sup>↓ vs 세로토닌·Ca<sup>2+</sup>↑.'), cols=2)

    memo([('🧩 세포', 'Afferent → Interneuron(CNS, 99%) → Efferent<br>Astrocyte = BBB 유도·K<sup>+</sup>·NT<br>Oligo = CNS 수초 / Schwann = PNS<br>Microglia = 면역 / Ependymal = CSF'),
          ('🛡 보호', 'Dura → Arachnoid → Pia<br>CSF = 맥락총 → 거미막 과립<br>BBB = tight junction, 지용성·O<sub>2</sub> 통과, GLUT1<br>O<sub>2</sub> 20% · 포도당 50%'),
          ('🧠 피질·핵', 'Precentral(전두) = 운동 / Postcentral(두정) = 감각<br>반대쪽 · homunculus<br>Broca = 말 / Wernicke = 이해<br>기저핵 = 억제, 파킨슨 = 도파민↓<br>시상 = 중계 / 시상하부 = 항상성'),
          ('💾 기억·척수', '습관화 Ca<sup>2+</sup>↓ / 민감화 세로토닌↑<br>LTP: AMPA(Na<sup>+</sup>) · NMDA(Ca<sup>2+</sup>) · 해마<br>소뇌 = 절차 · 뇌간 = 호흡·망상체<br>척수: 백질 바깥, L1–L2 끝, dorsal = 감각')],
         '<ol><li>1차 운동피질 = <b>pre</b>central, <b>frontal</b></li><li>척수 = 백질이 <b>바깥</b>, 구심 = <b>dorsal</b></li><li>BBB: 지용성은 <b>통과</b>, 유도는 <b>astrocyte</b></li></ol>',
         ['The spinal cord serves as a link between the brain and the body and integrates reflex activity without involving the brain.',
          'The primary motor cortex in the precentral gyrus of the frontal lobe initiates voluntary movement on the opposite side of the body.',
          'Short-term memory involves transient changes in preexisting synapses, whereas long-term memory requires protein synthesis and new synaptic connections.'])
