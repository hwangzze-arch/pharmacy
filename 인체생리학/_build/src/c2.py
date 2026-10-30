from lib import *

def build():
    chapter(2, 'Cell Physiology')
    c = CH['color']
    page('CHAPTER 2', 'Cell Physiology — 한 장 지도',
        chev([('핵', '설계도 DNA', '#1f6f30'), ('RER', '단백질 생산', c), ('SER', '수송소포 포장', '#37a24d'), ('Golgi', '가공·분류', '#40b057'), ('분비소포', '세포외유출', '#2f9e44'), ('리소좀·퍼옥시좀', '분해·해독', '#237032'), ('미토콘드리아', 'ATP 발전소', '#1b5e28')]) +
        grid('1fr 1fr',
            col(card('한 줄 요약', '세포는 <span class="hy">작은 공장</span>이다. 핵(설계도) → <span class="hg">RER(생산) → SER(포장) → 골지(가공·분류) → 분비소포(출하)</span>, 리소좀(쓰레기 분해), 퍼옥시좀(독성 해독), 미토콘드리아(발전소), 세포골격(뼈대와 근육).', 'sum big'),
                card('💡 교수님 "Points to think" 3문항 = 서술형 후보', '<ol><li>What basic cellular functions are essential to a cell\'s survival?</li><li>What are some examples of specialized cellular tasks that promote homeostasis?</li><li>What are the stages of cellular respiration, and where is each accomplished?</li></ol><small>→ 1·2번은 1장 PART 01, 3번은 이 장 PART 03에서 답안 완성</small>', 'tip')),
            card('🎯 교수님 예시문제(Ch 2) → 이 장에서', tbl(['예시 문제', '정답', '핵심'], [
                ['Transport vesicles carry secretory proteins from the smooth ER to ____.', '<b>the Golgi complex</b>', 'RER → SER → <b>Golgi</b> → 분비소포 → 세포막'],
                ['Lysosomes ____.', '<b>contain hydrolytic enzymes</b>', 'catalase = 퍼옥시좀, ATP = 미토콘드리아'],
                ['(오답 보기) are smaller than peroxisomes', '✗', '퍼옥시좀이 더 작다'],
                ['(오답 보기) leave the cell via exocytosis', '✗', '리소좀 효소는 세포 <b>안</b>에서 일함']]), 'warn')), 'Slides 1–24')

    page('PART 01', '세포의 구획 · ER과 골지 — 단백질 공장 라인',
        grid('1fr 1fr 1.05fr',
            col(card('Cell theory (Table 2-1)', '<ul><li>The cell is the <b>smallest structural and functional unit</b> capable of carrying out life processes.</li><li>Function depends on structure.</li><li><b>All new cells arise only from preexisting cells.</b></li></ul>', 'def'),
                card('🧩 세포의 3구획', tbl(['구획', '내용'], [['Plasma membrane', '경계, 선택적 투과 (3장)'], ['Nucleus', '<b>DNA</b> — genome, proteome, epigenetics'], ['Cytoplasm', '핵 뺀 내부 전부 = 세포기관 + 세포골격 + 세포액']])),
                card('⚠ Cytoplasm vs Cytosol', '<b>Cytoplasm</b> = 핵을 뺀 <u>세포 내부 전부</u><br><b>Cytosol</b> = 세포기관을 둘러싼 <u>물 기반 젤리 액체</u>만 → cytosol ⊂ cytoplasm', 'warn')),
            col(card('🏭 공장 라인', flow('RER 리보솜', 'SER 포장', 'Golgi', '분비소포', 'Exocytosis', small=True) + tbl(['구조', '하는 일'], [
                    ['<b>Rough ER</b>', '<span class="hy">분비 단백질 + 막 단백질</span> 합성 → ER 내강으로'],
                    ['<b>Smooth ER</b>', '새 단백질을 <span class="hy">수송소포에 포장</span> → 골지로, 지질 합성'],
                    ['<b>Golgi</b>', '납작한 막주머니 더미, <b>서로 연결 X</b>(ER과 다름) · 주머니 간 이동 = <b>COPI</b> 피복 소포 · 분비세포에서 <b>세포외유출용 포장</b>']])),
                card('Segregated synthesis 분리된 합성', '<ul><li><b>자유 리보솜(세포액)</b> → 세포 <u>안</u>에서 쓸 단백질</li><li><b>ER 부착 리보솜</b> → <u>분비</u>·<u>막</u> 단백질</li></ul>왜? 소화효소가 세포 안에서 작동하면 세포를 녹이니까 → 막 안에 가둬서 이동.', 'why'),
                card('🗑 불량 단백질', '잘못 접힌 단백질 → <b>ubiquitin</b> 꼬리표 → <b>proteasome</b> 분해 = <span class="hg">ubiquitin–proteasome pathway</span> (리소좀 아님!)', 'mint')),
            img('c2-08', 'ER → 골지 → 분비소포 → 세포외유출 (Sherwood Fig. 2-3)', '128mm')), 'Slides 3–12')

    qpage('PART 01', '세포 구획 · ER · 골지',
        MC('Transport vesicles carry secretory proteins from the smooth ER to ____.', '수송소포는 분비 단백질을 활면소포체에서 ____(으)로 운반한다.',
           [('the Golgi complex', '골지 복합체'), ('lysosomes', '리소좀'), ('secretory vesicles', '분비소포'), ('the nucleus', '핵'), ('the plasma membrane', '세포막')], '①',
           'RER(합성) → SER(포장) → <b>Golgi</b>(가공·분류) → 분비소포 → 세포막. 분비소포는 골지에서 만들어지므로 ③은 그 다음 단계.', stars=1, prof=True),
        MC('Proteins that will be used <u>within the cytosol</u> are synthesized by ____.', '<u>세포액 안에서</u> 쓰일 단백질은 ____에 의해 합성된다.',
           [('ribosomes bound to the rough ER', '조면소포체 부착 리보솜'), ('free ribosomes in the cytosol', '세포액의 자유 리보솜'), ('the Golgi complex', '골지 복합체'), ('the smooth ER', '활면소포체'), ('proteasomes', '프로테아좀')], '②',
           '분리된 합성: 세포 내용 = 자유 리보솜, 분비·막 단백질 = ER 부착 리보솜.'),
        TF([('The cytosol includes all organelles, the cytoskeleton, and fluid outside the nucleus.', '세포액은 핵 밖의 모든 세포기관·세포골격·액체를 포함한다.'),
            ('Proteins destined for secretion are synthesized by ribosomes bound to the rough ER.', '분비될 단백질은 조면소포체 부착 리보솜이 합성한다.'),
            ('Misfolded proteins are mainly destroyed by lysosomes.', '잘못 접힌 단백질은 주로 리소좀이 파괴한다.'),
            ('Unlike the ER, the sacs of the Golgi complex are not physically continuous with one another.', 'ER과 달리 골지 주머니들은 서로 연결되어 있지 않다.'),
            ('All new cells arise only from preexisting cells.', '모든 새 세포는 이미 존재하는 세포로부터만 생긴다.')],
           'F T F T T', '(1) 그건 <b>cytoplasm</b>; cytosol = 액체 부분만 (3) → <b>ubiquitin–proteasome</b> pathway.'))

    page('PART 02', '분비 · 세포내유입 · 리소좀 vs 퍼옥시좀',
        grid('1fr 1fr 1fr',
            col(card('📤 Exocytosis 세포외유출', '<b>Secretion</b> = 세포가 만든 산물을 ECF로 방출. 전문 분비세포 = <b>내분비세포(호르몬)</b>, <b>소화샘 세포(효소)</b>.<ul><li>분비소포가 골지에서 떨어져 저장 → 신호 → <b>세포막과 융합</b> → 방출 = 분비의 주된 기전</li><li>분비소포는 <b>세포막에만</b> 결합(도킹 표지)</li><li>막 면적 일정 = <b>endocytosis 속도 = exocytosis 속도</b></li></ul>'),
                card('📥 Endocytosis 3종', tbl(['종류', '무엇을', '특징'], [
                    ['<b>Pinocytosis</b>', 'ECF 방울', '<span class="hp">비선택적</span> "세포가 마시기"'],
                    ['<b>Receptor-mediated</b>', '특정 큰 분자(LDL, 철)', '<span class="hg">선택적</span>, 수용체 + clathrin'],
                    ['<b>Phagocytosis</b>', '큰 입자(세균·잔해)', '위족으로 감쌈 → 리소좀과 융합']]) + '<p><b>Endosome</b> = 들어온 물질의 <span class="hy">중앙 분류소</span> (재활용 vs 리소좀행)</p>')),
            col(card('🧹 청소부 두 형제', tbl(['', 'Lysosome', 'Peroxisome'], [
                    ['효소', '<span class="hy">가수분해효소(hydrolytic)</span>, 산성', '<span class="hy">산화효소(oxidase) + catalase</span>'],
                    ['일', '들어온 물질 분해, <b>낡은 세포기관 제거</b>', 'O<sub>2</sub>로 H를 떼어 <b>H<sub>2</sub>O<sub>2</sub> 생성</b> → 독성 폐기물 해독'],
                    ['H<sub>2</sub>O<sub>2</sub>', '—', '만들고(oxidase) 바로 분해(catalase): 2H<sub>2</sub>O<sub>2</sub> → 2H<sub>2</sub>O + O<sub>2</sub>'],
                    ['크기', '더 큼', '<b>더 작음</b>']])),
                card('⚠ 교수님 예시 오답 보기', '<ul><li>"leave the cell via exocytosis" ✗ → 세포 안에서 일함</li><li>"contain catalases" ✗ → 퍼옥시좀</li><li>"are involved in ATP synthesis" ✗ → 미토콘드리아</li><li>"are smaller than peroxisomes" ✗</li></ul>', 'warn')),
            img('c2-14', '리소좀·퍼옥시좀 + 세포내유입 → 엔도좀 → 리소좀 경로', '125mm')), 'Slides 12–17')

    qpage('PART 02', '분비 · 리소좀 · 퍼옥시좀',
        MC('Lysosomes ____.', '리소좀은 ____.',
           [('contain hydrolytic enzymes', '가수분해효소를 가진다'), ('leave the cell via exocytosis', '세포외유출로 세포를 떠난다'), ('are smaller than peroxisomes', '퍼옥시좀보다 작다'),
            ('contain catalases', '카탈레이스를 가진다'), ('are involved in ATP synthesis', 'ATP 합성에 관여한다')], '①', '리소좀 = 가수분해효소 주머니. catalase = 퍼옥시좀, ATP = 미토콘드리아.', stars=1, prof=True),
        MC('Which TWO statements about peroxisomes are correct? <b>(Choose two.)</b>', '퍼옥시좀에 대한 옳은 설명 두 개는?',
           [('They contain oxidases that use O<sub>2</sub> to strip hydrogen from organic molecules.', 'O<sub>2</sub>로 유기분자에서 H를 떼는 산화효소를 가진다.'),
            ('They are the primary site of oxidative phosphorylation.', '산화적 인산화의 주된 장소이다.'), ('They contain catalase, which decomposes H<sub>2</sub>O<sub>2</sub>.', 'H<sub>2</sub>O<sub>2</sub>를 분해하는 카탈레이스를 가진다.'),
            ('They engulf bacteria by phagocytosis.', '식세포작용으로 세균을 삼킨다.'), ('They contain hydrolytic enzymes and are larger than lysosomes.', '가수분해효소를 가지며 리소좀보다 크다.')], '①, ③',
           '퍼옥시좀 = 산화효소(H<sub>2</sub>O<sub>2</sub> 생성) + 카탈레이스(분해). ② 미토콘드리아 ④ 백혈구 ⑤ 리소좀 특징 섞음.', pick=2, stars=3),
        MC('Selective uptake of specific large molecules such as LDL cholesterol into the cell occurs by ____.', 'LDL 콜레스테롤 같은 특정 큰 분자의 선택적 세포 유입은 ____이다.',
           [('pinocytosis', '음세포작용'), ('phagocytosis', '식세포작용'), ('receptor-mediated endocytosis', '수용체 매개 세포내유입'), ('exocytosis', '세포외유출'), ('simple diffusion', '단순 확산')], '③',
           '"선택적·특정 분자" = 수용체. pinocytosis = 비선택적, phagocytosis = 큰 <b>입자</b>.'))

    page('PART 03', '미토콘드리아 · 세포액 · 세포골격',
        grid('1.1fr 1fr 1fr',
            col(card('⚡ 미토콘드리아 = ATP 발전소', '이중막, <b>내막이 접혀 크리스타(cristae)</b> → 표면적↑, 내부 = <b>matrix</b>. 음식 에너지 → ATP = <span class="hg">세포 호흡</span>' + tbl(['단계', '장소', '요점'], [
                    ['① Glycolysis', '<span class="hp">Cytosol</span>', '포도당 → 피루브산 2, ATP 2, O<sub>2</sub> 불필요'],
                    ['② Pyruvate oxidation', 'Matrix', '→ 아세틸 CoA + CO<sub>2</sub>'],
                    ['③ Citric acid cycle', 'Matrix', 'CO<sub>2</sub>, NADH·FADH<sub>2</sub>, ATP 소량'],
                    ['④ Oxidative phosphorylation', '<span class="hp">Inner membrane</span>', '전자전달계 + ATP 합성효소, <b>O<sub>2</sub> = 최종 전자수용체 → H<sub>2</sub>O</b>, ATP 대부분']]) + '<small>무산소 2 ATP vs 유산소 약 32 ATP</small>'),
                card('🔥 Uncontrolled vs controlled oxidation', '<b>태우기</b>: 에너지가 폭발적으로 <b>열</b>로만 → 쓸 수 있는 에너지 0<br><b>몸 안</b>: 전자전달계에서 단계적 → 일부 <b>ATP</b>(움직임·합성·수송) + 나머지 <b>열</b>(체온) → 과잉 열은 환경으로', 'why')),
            col(card('🧪 Cytosol 세포 젤', '<ul><li><b>중간대사</b>의 효소적 조절</li><li><b>리보솜 단백질 합성</b></li><li><b>저장</b> = <span class="hy">inclusions 봉입체</span>: 지방방울·글리코겐·분비소포 — <b>막 없음</b>, 일시적, 세포 종류·상황 따라 다름</li></ul>'),
                card('⚠ 함정', '<ul><li>해당은 <b>세포액</b>(미토콘드리아 ✗)</li><li>산화적 인산화는 <b>내막</b>(기질 ✗)</li><li>봉입체는 <b>막이 없다</b></li></ul>', 'warn')),
            col(card('🦴 세포골격 3종', tbl(['요소', '재료', '역할'], [
                    ['<b>Microtubule</b><br><small>가장 굵음</small>', 'tubulin', '<span class="hy">비대칭 모양 유지</span> · 복잡한 이동: <b>축삭 수송</b>, 섬모·편모, <b>방추사</b>'],
                    ['<b>Microfilament</b><br><small>가장 가늚</small>', 'actin', '<span class="hy">수축</span>(근수축·아메바운동) · <b>기계적 보강재</b>(미세융모)'],
                    ['<b>Intermediate filament</b>', 'keratin 등', '<span class="hy">기계적 스트레스</span> 받는 부위(피부, 축삭)']]) + '<p>세포 모양·강성 결정 + <b>기계적 소통 시스템</b> + 세포 내 수송 방향 결정</p>'),
                card('🧠 암기', '<b>관 = 모양·이동 / 섬 = 수축 / 중 = 버팀</b><br>굵기: 미세소관 > 중간섬유 > 미세섬유', 'mint'))), 'Slides 18–24')

    qpage('PART 03', '미토콘드리아 · 세포골격',
        TF([('Glycolysis takes place in the mitochondrial matrix and requires O<sub>2</sub>.', '해당은 미토콘드리아 기질에서 일어나며 O<sub>2</sub>가 필요하다.'),
            ('The cristae are folds of the inner mitochondrial membrane.', '크리스타는 미토콘드리아 내막의 주름이다.'),
            ('Inclusions are membrane-enclosed organelles present in all cells.', '봉입체는 모든 세포에 있는 막으로 싸인 세포기관이다.'),
            ('Intermediate filaments are important in regions subject to mechanical stress.', '중간섬유는 기계적 스트레스를 받는 부위에서 중요하다.'),
            ('In the body, nutrient oxidation releases energy explosively as heat only.', '몸 안에서 영양소 산화는 에너지를 열로만 폭발적으로 방출한다.')],
           'F T F T F', '(1) → <b>cytosol</b>, O<sub>2</sub> 불필요 (3) → 막 없는 일시적 저장물 (5) → 단계적, 일부는 <b>ATP</b>로 포획.'),
        MC('Which TWO functions are performed by microtubules? <b>(Choose two.)</b>', '미세소관의 기능 두 가지는?',
           [('Forming the mitotic spindle', '방추사 형성'), ('Muscle contraction via actin–myosin', '액틴-마이오신 근수축'), ('Axonal transport in neurons', '뉴런의 축삭 수송'),
            ('Storing glycogen as inclusions', '글리코겐을 봉입체로 저장'), ('Forming the core of microvilli', '미세융모의 심 형성')], '①, ③', '② ⑤ = 미세섬유(actin), ④ = 세포액.', pick=2),
        SA('In which part of the mitochondrion does oxidative phosphorylation occur, and what is the final electron acceptor?', '산화적 인산화는 미토콘드리아 어디에서 일어나며 최종 전자수용체는?',
           'Inner mitochondrial membrane (cristae); O<sub>2</sub> (forming H<sub>2</sub>O)', '크리스타가 접힌 이유 = 표면적 ↑ → ATP ↑.', stars=2))

    qpage('PART 01–03', '서술형',
        ES('Trace the pathway of a secretory protein, such as a digestive enzyme, from its synthesis to its release from the cell. Name each organelle involved.',
           '소화효소 같은 분비 단백질이 합성되어 세포 밖으로 나갈 때까지의 경로를 세포기관 이름과 함께 서술하시오.',
           'The protein is synthesized by ribosomes on the <b>rough ER</b> and threaded into the ER lumen. It moves to the <b>smooth ER</b>, which packages it into <b>transport vesicles</b>. These fuse with the <b>Golgi complex</b>, where the protein is modified, sorted, and concentrated as it passes through the Golgi sacs (via COPI-coated vesicles). The product is packaged into <b>secretory vesicles</b> that bud off and are stored until an appropriate signal arrives; they then fuse with the plasma membrane and release their contents into the ECF by <b>exocytosis</b>.',
           '채점: RER → SER → transport vesicle → Golgi → secretory vesicle → exocytosis 순서.'),
        ES('Describe the stages of cellular respiration and where each occurs. Why is controlled oxidation in the body more useful than burning nutrients?',
           '세포 호흡 단계와 장소를 서술하고, 몸 안의 조절된 산화가 태우는 것보다 유용한 이유를 쓰시오.',
           'Glycolysis occurs in the <b>cytosol</b> and splits glucose into two pyruvate. Pyruvate oxidation and the citric acid cycle occur in the <b>mitochondrial matrix</b>, releasing CO<sub>2</sub> and generating hydrogen carriers (NADH, FADH<sub>2</sub>). Oxidative phosphorylation occurs at the <b>inner mitochondrial membrane (cristae)</b>, where the electron transport chain uses O<sub>2</sub> as the final electron acceptor and produces most of the ATP. Burning releases energy explosively as heat, so none is captured; controlled oxidation releases it step by step, capturing part as ATP for cellular work while the rest becomes heat that maintains body temperature.',
           '교수님 Points to think 3번 그대로. 장소 4개 + ATP vs 열.'), cols=2)

    memo([('🏭 공장 라인', 'RER(분비·막 단백질) → SER(수송소포) → <b>Golgi</b>(COPI, 가공) → 분비소포 → <b>exocytosis</b><br>자유 리보솜 = 세포 내용<br>불량 단백질 = ubiquitin–<b>proteasome</b>'),
          ('🧹 분해·해독', '<b>Lysosome</b> = hydrolytic enzymes, 낡은 기관 제거<br><b>Peroxisome</b> = oxidase(H<sub>2</sub>O<sub>2</sub> 생성) + <b>catalase</b>(분해), 더 작음<br>Pino(비선택) · RME(선택) · Phago(입자)<br>Endosome = 분류소'),
          ('⚡ ATP', '해당 = <b>cytosol</b>, O<sub>2</sub> X<br>피루브산 산화·TCA = <b>matrix</b><br>산화적 인산화 = <b>inner membrane</b>, O<sub>2</sub> → H<sub>2</sub>O<br>2 vs 32 ATP'),
          ('🦴 골격·세포액', 'Microtubule = 모양·축삭수송·방추사<br>Microfilament = actin·수축<br>Intermediate = 스트레스(keratin)<br>Inclusions = 막 없는 저장물<br>Cytosol ⊂ Cytoplasm')],
         '<ol><li>SER 다음은 <b>Golgi</b> (분비소포 ✗)</li><li>catalase = <b>퍼옥시좀</b> (리소좀 ✗)</li><li>해당 = <b>세포액</b> (미토콘드리아 ✗)</li></ol>',
         ['Transport vesicles carry newly synthesized proteins from the smooth ER to the Golgi complex, which modifies and packages them into secretory vesicles for exocytosis.',
          'Lysosomes contain hydrolytic enzymes; peroxisomes contain oxidases that produce H<sub>2</sub>O<sub>2</sub> and catalase that degrades it.',
          'Glycolysis occurs in the cytosol; the citric acid cycle in the mitochondrial matrix; oxidative phosphorylation at the inner mitochondrial membrane.'])
