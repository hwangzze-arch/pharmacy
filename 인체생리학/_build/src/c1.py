from lib import *

def build():
    chapter(1, 'Physiology & Homeostasis')
    c = CH['color']
    # ---------- map ----------
    page('CHAPTER 1', 'Introduction to Physiology and Homeostasis — 한 장 지도',
        chev([('1.1 생리학', '기능 + 기전', c), ('1.2 구성 단계', '화학→개체 6층', '#14a394'), ('1.3 항상성', 'ECF를 일정하게', '#1aa59b'), ('1.4 조절계', '음성·양성·전향', '#0a6e66')]) +
        grid('1fr 1fr',
            col(card('한 줄 요약', '몸은 <span class="hy">화학 → 세포 → 조직 → 장기 → 계통 → 개체</span>로 쌓여 있고, 모든 계통은 결국 <span class="hg">세포를 둘러싼 ECF를 일정하게(항상성)</span> 지키려고 일한다. 그 기본 도구가 <span class="hp">음성 되먹임</span>.', 'sum big'),
                card('💡 숫자 4개만 먼저', '세포 <b>200종</b> · 기본 조직 <b>4</b> · 신체 계통 <b>11</b> · ECF = 간질액 <b>80%</b> + 혈장 <b>20%</b> (체액의 1/3)', 'tip')),
            card('🎯 교재 테스트뱅크가 노리는 곳', tbl(['포인트', '함정'], [
                ['모든 세포의 기본 기능', '<b>생식(reproducing)</b> — 신경·근육세포는 분열 X'],
                ['결합조직 고르기', '<b>척수 = 신경조직</b>, 혈액 = 결합조직'],
                ['구성 단계 순서', '조직(tissue) → 장기(organ) 순서 바꿔치기'],
                ['내부 환경', '<b>ECF</b> (ICF 아님)'],
                ['생식계', '항상성에 <b>필수 아님</b>'],
                ['신경 vs 내분비', '<b>speed</b> vs <b>duration</b>'],
                ['되먹임', '양성 = 출산, 전향 = 예측(먹기 전 침)']]), 'warn')), 'Slides 1–37')

    # ---------- P01 ----------
    page('PART 01', '생리학 · 몸의 구성 단계 · 4대 조직',
        grid('1fr 1fr 1fr',
            col(card('정의', '<b>Physiology</b> = 살아있는 몸의 <span class="hy">기능(function)</span>과 그 밑의 <b>기전(mechanism)</b>을 공부 — "how"를 묻는 학문<br><b>Anatomy</b> = <span class="hy">구조(structure)</span>를 공부<br>→ <span class="hg">Structure and function are inseparable</span>', 'def'),
                card('🧱 구성 단계 6층', flow('Chemical', 'Cell', 'Tissue', 'Organ', 'Body system', 'Organism', small=True) + tbl(['단계', '핵심'], [
                    ['Chemical', '주로 <b>O·C·H·N</b> · 단백질·탄수화물·지방·핵산'],
                    ['Cell', '<span class="hy">생명의 기본 단위</span>, 약 200종으로 분화'],
                    ['Tissue', '구조·특수화가 비슷한 세포 집단 → 4대 조직'],
                    ['Organ', '<b>2종 이상</b>의 조직이 모여 특정 기능'],
                    ['Body system', '관련 기능의 장기 모음, <b>11개</b>, 서로 의존'],
                    ['Organism', '성장·생식·대사·자극 반응이 가능한 개체']]))),
            col(card('🔬 세포 기능 2종', tbl(['Basic (모든 세포)', 'Specialized (세포별)'], [
                    ['음식·O<sub>2</sub> 획득<br>에너지 생성 반응<br>노폐물 제거<br>단백질·성분 합성<br>세포 내 물질 이동<br>환경에 반응<br>생식(번식)', '소화샘 → 효소 분비<br>신장 → 선택적 보존·배설<br>근육 → 수축<br>신경 → 전기 신호']]) +
                    '<p><span class="hg">기본 기능 = 세포 자신의 생존</span><br><span class="hg">특수 기능 + 세포 간 소통 = 몸 전체의 생존</span></p>'),
                card('⚠ 함정', '<ul><li>"생식"은 기본 기능 목록에 있지만 <b>성숙한 신경·근육세포는 분열 X</b> → "모든 세포가 하지 <u>않는</u> 것" 정답</li><li>특수 기능 = 기본 기능의 <b>변형·정교화</b> (근수축 = 세포 내 이동 극대화) → True</li></ul>', 'warn')),
            col(card('🧬 4대 기본 조직 — "근·신·상·결"', tbl(['조직', '한 마디'], [
                    ['Epithelial 상피', '장벽·교환 + <b>샘</b>: 외분비(관 → 체외: 땀·침) / 내분비(관 X → 혈액: <b>호르몬</b>)'],
                    ['Connective 결합', '연결·지지·고정, <b>ECM 풍부</b> — 뼈·<b>혈액</b>·힘줄·연골'],
                    ['Muscle 근육', '수축 → 움직임 (골격·심장·평활)'],
                    ['Nervous 신경', '전기 신호 개시·전달 — 뇌·<b>척수</b>']])),
                card('Tissue vs Organ', '<b>Tissue</b> = 비슷한 세포들이 함께 일하는 <u>구조적 벽돌</u><br><b>Organ</b> = 서로 다른 조직 2종 이상이 모인 <u>기능 단위</u> (위 = 상피+결합+근육+신경)', 'mint'),
                card('', '<b>Secretion 분비</b> = 적절한 자극에 반응해 세포가 스스로 합성한 산물을 방출하는 것', 'tip'))), 'Slides 8–21')

    qpage('PART 01', '구성 단계 · 조직',
        MC('Which of the following is <u>NOT</u> a type of connective tissue?', '다음 중 결합조직이 <u>아닌</u> 것은?',
           [('bone', '뼈'), ('blood', '혈액'), ('the spinal cord', '척수'), ('tendons', '힘줄'), ('cartilage', '연골')], '③',
           '척수 = <b>신경조직</b>(뇌와 함께 CNS). 결합조직 = ECM 풍부: 뼈·혈액(혈장이 ECM)·힘줄·연골.', stars=1),
        MC('Which of the following activities is <u>NOT</u> carried out by every cell in the body?', '다음 중 몸의 <u>모든</u> 세포가 수행하는 활동이 <u>아닌</u> 것은?',
           [('obtaining O<sub>2</sub> and nutrients', 'O<sub>2</sub>·영양분 획득'), ('performing energy-generating chemical reactions', '에너지 생성 화학반응'),
            ('eliminating wastes', '노폐물 제거'), ('synthesizing proteins', '단백질 합성'), ('reproducing (cell division)', '생식(세포 분열)')], '⑤',
           '성숙한 <b>신경·근육세포는 분열하지 않는다</b> → 공통 기능 아님.'),
        TF([('Organs are composed of two or more types of primary tissue organized to perform particular functions.', '장기는 특정 기능을 하도록 조직된 2종 이상의 기본 조직으로 구성된다.'),
            ('The proper order of organization is chemicals → cells → organs → tissues → body systems → organism.', '올바른 구성 순서는 화학물질 → 세포 → 장기 → 조직 → 계통 → 개체이다.'),
            ('Cell specializations are usually a modification or elaboration of one of the basic cell functions.', '세포의 특수화는 보통 기본 세포 기능 하나의 변형·정교화이다.'),
            ('Cells in a multicellular organism have little in common with single-celled organisms.', '다세포 생물의 세포는 단세포 생물과 공통점이 거의 없다.'),
            ('Exocrine glands secrete hormones into the blood.', '외분비샘은 호르몬을 혈액으로 분비한다.')],
           'T F T F F', '(2) → cells → <b>tissues → organs</b> (4) 기본 세포 기능은 단세포 생물과 <b>똑같다</b> (5) 그건 <b>endocrine</b>; exocrine = 관(duct)으로 체외.'))

    # ---------- P02 ----------
    page('PART 02', '항상성 — 세포가 사는 "내부 바다"를 지켜라',
        grid('1fr 1.25fr',
            col(card('정의', '<b>Homeostasis</b> = 외부 환경이 변해도 <span class="hy">내부 환경(internal environment)을 안정되게 유지</span>하는 것. 고정이 아니라 좁은 범위 안의 <b>동적 평형(dynamic steady state)</b>.<br><small>self-regulating process by which biological systems maintain internal stability while adjusting to changing external conditions</small>', 'def'),
                card('💧 체액 구획', tbl(['구획', '위치 · 비율'], [
                    ['<b>ICF</b>', '모든 세포 <b>안</b> (체액의 약 2/3)'],
                    ['<b>ECF</b> = 내부 환경', '세포 <b>밖</b> (약 1/3)'],
                    ['└ Interstitial fluid', '세포를 직접 적시고 영양 공급 (ECF의 ~80%)'],
                    ['└ Plasma', '혈액의 액체 부분 (ECF의 ~20%)']]) +
                    flow('세포 ICF', '간질액', '혈장', '외부 (폐·소화관·신장)', small=True)),
                card('📋 항상성으로 조절되는 7가지', '영양소 농도 · O<sub>2</sub>/CO<sub>2</sub> 농도 · 노폐물 농도 · <b>pH</b> · 물·염·전해질 농도 · <b>부피·압력</b> · <b>체온</b>', 'tip')),
            col(card('🫀 11개 신체 계통 — 각자 항상성에 기여', tbl(['계통', '항상성 기여 키워드'], [
                    ['Circulatory 순환', '<span class="hy">운반(transport)</span>'],
                    ['Digestive 소화', '음식 → 작은 영양 분자로 분해·흡수'],
                    ['Respiratory 호흡', 'O<sub>2</sub> 획득, CO<sub>2</sub> 배출 (pH에도 기여)'],
                    ['Urinary 비뇨', '과잉 물·염·산·전해질을 소변으로'],
                    ['Skeletal 골격', '지지·보호, <b>Ca<sup>2+</sup> 저장고</b>, <b>골수 = 혈구의 근원</b>'],
                    ['Muscular 근육', '움직임, <b>열 생성 → 체온 유지</b>'],
                    ['Integumentary 외피', '바깥 보호막, <b>체온 조절</b>'],
                    ['Immune 면역', '침입자·암세포 방어, 손상 세포 교체 도움'],
                    ['Nervous 신경', '<span class="hg">빠른(swift) 반응</span> 조절'],
                    ['Endocrine 내분비', '<span class="hg">지속(duration)</span> 필요한 활동 (성장)'],
                    ['Reproductive 생식', '종족 보존 — <span class="hp">항상성에 필수 아님</span>']])),
                card('⚠ 함정', '항상성이 지키는 건 <b>ECF</b>. 신경계(속도)와 내분비계(지속)가 <b>두 주요 조절 계통</b>. 항상성 이상 → 질병 → 심하면 사망.', 'warn'))), 'Slides 23–31')

    qpage('PART 02', '항상성 · 체액 · 계통',
        SA('Name the two components of the extracellular fluid, and state which one directly surrounds the cells.', '세포외액의 두 구성 성분을 쓰고, 그중 세포를 직접 둘러싸는 것은 무엇인지 쓰시오.',
           'Plasma and interstitial fluid; interstitial fluid', '간질액(약 80%) = 세포를 적시는 액체, 혈장(약 20%) = 혈액의 액체 부분.'),
        MC('Which body system is matched <u>INCORRECTLY</u> with its homeostatic function?', '항상성 기능과 <u>잘못</u> 짝지어진 계통은?',
           [('Skeletal — storage reservoir for calcium', '골격계 — 칼슘 저장고'), ('Muscular — generates heat to maintain body temperature', '근육계 — 열 생성으로 체온 유지'),
            ('Endocrine — controls activities that require swift responses', '내분비계 — 빠른 반응이 필요한 활동 조절'), ('Respiratory — eliminates CO<sub>2</sub>', '호흡계 — CO<sub>2</sub> 배출'),
            ('Circulatory — transports materials', '순환계 — 물질 운반')], '③', '빠른(swift) = <b>신경계</b>. 내분비계 = <b>지속(duration)</b>.'),
        TF([('The internal environment that the body homeostatically maintains is the intracellular fluid.', '몸이 항상성으로 유지하는 내부 환경은 세포내액이다.'),
            ('The reproductive system is not essential for homeostasis.', '생식계는 항상성에 필수적이지 않다.'),
            ('Interstitial fluid is the fluid portion of the blood.', '간질액은 혈액의 액체 부분이다.'),
            ('Bone marrow is the source of all blood cells.', '골수는 모든 혈구의 근원이다.'),
            ('Homeostasis means that the internal environment is held absolutely constant.', '항상성은 내부 환경이 절대적으로 일정하게 유지됨을 뜻한다.')],
           'F T F T F', '(1) → <b>extracellular fluid (ECF)</b> (3) → 그건 <b>plasma</b> (5) → 좁은 범위 안의 <b>dynamic steady state</b>.'))

    # ---------- P03 ----------
    fb = '''<svg viewBox="0 0 440 120" width="100%"><defs><marker id="a1" markerWidth="7" markerHeight="7" refX="5" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6Z" fill="#1d2747"/></marker><marker id="a2" markerWidth="7" markerHeight="7" refX="5" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6Z" fill="#c92a2a"/></marker></defs>
<g font-size="10" text-anchor="middle"><rect x="2" y="30" width="80" height="34" rx="6" fill="#fff0a6"/><text x="42" y="45" font-weight="700">자극(변화)</text><text x="42" y="58" font-size="8.5">체온 ↑</text>
<rect x="108" y="30" width="80" height="34" rx="6" fill="#e7ecfb"/><text x="148" y="45" font-weight="700">Sensor</text><text x="148" y="58" font-size="8.5">온도 수용기</text>
<rect x="214" y="30" width="100" height="34" rx="6" fill="#e7ecfb"/><text x="264" y="45" font-weight="700">Control center</text><text x="264" y="58" font-size="8.5">시상하부(set point 비교)</text>
<rect x="340" y="30" width="96" height="34" rx="6" fill="#e7ecfb"/><text x="388" y="45" font-weight="700">Effector</text><text x="388" y="58" font-size="8.5">땀샘·피부혈관</text>
<text x="220" y="16" font-weight="700" fill="#1d2747">감지(Detect) → 통합(Integrate) → 조정(Adjust)</text>
<text x="220" y="114" font-weight="700" fill="#c92a2a">체온 ↓ = 처음 변화와 반대 방향 → Negative feedback</text></g>
<g stroke="#1d2747" stroke-width="1.8" marker-end="url(#a1)"><line x1="82" y1="47" x2="105" y2="47"/><line x1="188" y1="47" x2="211" y2="47"/><line x1="314" y1="47" x2="337" y2="47"/></g>
<path d="M388,64 L388,98 L42,98 L42,67" fill="none" stroke="#c92a2a" stroke-width="2" marker-end="url(#a2)"/></svg>'''
    page('PART 03', '항상성 조절계 — 음성 · 양성 되먹임 · 전향 조절',
        grid('1.15fr 1fr',
            col(card('정의', '<b>Homeostatic control system</b> = 내부 환경의 한 요소를 최적 수준으로 유지하는 연결망. 반드시 ① <b>정상에서 벗어남 감지</b> ② <b>다른 정보와 통합</b> ③ <b>정상으로 되돌리는 조정</b>', 'def'),
                card('🌡 음성 되먹임 한 장 그림', fb),
                card('', tbl(['조절', '정의'], [
                    ['<b>Intrinsic</b> (local)', '장기 <b>안에서</b> 스스로 (운동 중 근육 O<sub>2</sub>↓ → 그 근육 혈관 확장)'],
                    ['<b>Extrinsic</b> (systemic)', '장기 <b>밖에서</b> 시작 — <span class="hy">신경계·내분비계</span>가 담당, 여러 장기를 한 번에 조정']]))),
            col(card('🔁 되먹임 3종 비교', tbl(['종류', '방향', '예'], [
                    ['<b>Negative</b>', '처음 변화와 <span class="hg">반대</span> → 상쇄. <b>가장 흔함</b>', '온도조절기, 체온, 혈압'],
                    ['<b>Positive</b>', '처음 변화와 <span class="hp">같은 방향</span>으로 증폭. 드묾', '<b>출산</b>(옥시토신↔수축), 혈액응고'],
                    ['<b>Feedforward</b>', '변화 <span class="hy">전에 예측</span>해 반응', '먹기 전 침·위액, 달리기 전 에너지↑']])),
                img('c1-35', '교재 그림: 음성(평형으로 수렴) vs 양성(계속 증폭)', '44mm'),
                card('⚠ 함정', '양성 되먹임은 스스로 멈추지 않음 → <b>외부 사건(분만)</b>이 끝내야 멈춤. Feedforward는 되먹임이 <b>아님</b>(변화 전).', 'warn'))), 'Slides 33–36')

    qpage('PART 03', '조절계 · 되먹임',
        MC('Which TWO of the following do <u>not</u> work by negative feedback? <b>(Choose two.)</b>', '다음 중 음성 되먹임으로 작동하지 <u>않는</u> 것 두 가지는?',
           [('Uterine contractions intensifying during childbirth', '출산 중 점점 강해지는 자궁 수축'), ('Sweating when body temperature rises', '체온 상승 시 땀'),
            ('Salivation at the sight of food before eating', '먹기 전 음식을 보고 침 분비'), ('Shivering when body temperature falls', '체온 하강 시 떨림'),
            ('A thermostat turning off a furnace as room temperature rises', '실온이 오르면 보일러를 끄는 온도조절기')], '①, ③',
           '① = <b>양성</b> 되먹임, ③ = <b>전향(feedforward)</b>. 나머지는 변화를 되돌리는 음성.', pick=2, stars=3),
        SA('____ controls are inherent to an organ, whereas ____ controls are regulatory mechanisms initiated outside an organ that alter the activity of the organ. These outside controls are accomplished by the ____ and ____ systems.',
           '____ 조절은 장기에 내재되어 있고, ____ 조절은 장기 밖에서 시작되어 장기 활동을 바꾼다. 이 외부 조절은 ____계와 ____계가 수행한다.',
           'Intrinsic; extrinsic; nervous; endocrine', '외인성 조절은 여러 장기를 동시에 조정할 수 있다는 장점.', stars=2),
        TF([('Positive feedback is the most common homeostatic mechanism.', '양성 되먹임이 가장 흔한 항상성 기전이다.'),
            ('In negative feedback, the response drives the controlled variable in the opposite direction of the initial change.', '음성 되먹임에서 반응은 조절 변수를 처음 변화의 반대 방향으로 움직인다.'),
            ('Childbirth is an example of positive feedback.', '출산은 양성 되먹임의 예이다.'),
            ('Feedforward mechanisms respond only after a change has occurred.', '전향 조절은 변화가 일어난 뒤에만 반응한다.'),
            ('A homeostatic control system must detect, integrate, and adjust.', '항상성 조절계는 감지·통합·조정을 해야 한다.')],
           'F T T F T', '(1) → <b>negative</b> feedback is most common (4) → in <b>anticipation</b> of a change (변화 <b>전</b>).'))

    qpage('PART 03', '서술형',
        ES('Compare negative feedback and positive feedback, giving one physiological example of each. Then explain how feedforward differs from both.',
           '음성·양성 되먹임을 각각 예와 함께 비교하고, 전향 조절이 둘과 어떻게 다른지 설명하시오.',
           'Negative feedback opposes the initial change: a change in a controlled variable triggers a response that drives the variable in the <b>opposite</b> direction, toward the set point (e.g., when body temperature rises, sweating and skin vasodilation lower it). It is the most common homeostatic mechanism. Positive feedback amplifies the initial change so the variable keeps moving in the <b>same</b> direction (e.g., in childbirth, contractions increase oxytocin release, which strengthens contractions until delivery ends the loop). Feedforward differs from both because it initiates responses <b>in anticipation of</b> a change, before the variable is disturbed (e.g., digestive secretions before eating).',
           '채점: ① 방향(반대 vs 같은) ② 예 각 1개 ③ feedforward = anticipation.'),
        ES('Define homeostasis and explain why the extracellular fluid must be kept stable for cells to survive. List at least four homeostatically regulated factors.',
           '항상성을 정의하고, 세포 생존을 위해 왜 ECF가 안정되어야 하는지 설명하시오. 조절되는 요소를 4가지 이상 쓰시오.',
           'Homeostasis is the maintenance of a relatively stable internal environment despite changes in the external environment. The internal environment is the extracellular fluid (plasma and interstitial fluid) surrounding the cells. Cells exchange nutrients, O<sub>2</sub>, CO<sub>2</sub>, and wastes with the ECF, so its composition must stay within a narrow range for cells to carry out life-sustaining activities. Regulated factors include concentrations of nutrients, O<sub>2</sub> and CO<sub>2</sub>, wastes, pH, water and electrolytes, volume and pressure, and temperature.',
           '"세포 → ECF와 교환 → ECF 일정해야 세포 생존 → 세포가 살아야 몸 생존"의 <b>순환 고리</b>가 만점 포인트.'), cols=2)

    memo([('🧱 구성·조직', '화학 → 세포 → <b>조직 → 장기</b> → 계통 → 개체<br>세포 200종 · 조직 4 · 계통 11<br>근·신·상·결 / 척수 = 신경, 혈액 = 결합<br>외분비 = 관 → 체외 / 내분비 = 혈액 → 호르몬'),
          ('💧 항상성', '내부 환경 = <b>ECF</b> = 간질액 80% + 혈장 20%<br>동적 평형(dynamic steady state)<br>조절 대상: 영양·O<sub>2</sub>/CO<sub>2</sub>·노폐물·pH·전해질·부피/압력·체온'),
          ('🫀 계통', '순환 = 운반 · 골격 = Ca 저장·골수<br>근육 = 열 · 외피 = 체온 · 면역 = 방어<br>신경 = <b>speed</b> / 내분비 = <b>duration</b><br>생식 = 항상성 필수 <b>X</b>'),
          ('🔁 조절', '감지 → 통합 → 조정<br>Intrinsic = 장기 안 / Extrinsic = 신경·내분비<br><b>Negative</b> = 반대, 가장 흔함<br><b>Positive</b> = 같은 방향, 출산<br><b>Feedforward</b> = 예측')],
         '<ol><li>척수 = <b>신경</b>조직, 혈액 = <b>결합</b>조직</li><li>내부 환경 = <b>ECF</b> (ICF ✗)</li><li>가장 흔한 조절 = <b>음성</b> 되먹임 / 출산 = 양성</li></ol>',
         ['Homeostasis is the maintenance of a relatively stable internal environment (the ECF) despite changes in the external environment.',
          'Negative feedback opposes an initial change; positive feedback amplifies it; feedforward responds in anticipation of a change.',
          'Intrinsic controls are inherent to an organ, whereas extrinsic controls are initiated outside the organ by the nervous or endocrine system.'])
