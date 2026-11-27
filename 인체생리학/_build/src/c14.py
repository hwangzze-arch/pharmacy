from lib import *

def build():
    chapter(14, 'The Urinary System')
    c = CH['color']
    page('CHAPTER 14', 'The Urinary System — 한 장 지도',
        chev([('14.1 콩팥', '기능·네프론', '#5f3dc4'), ('14.2 여과', '55−30−15 · GFR', c), ('14.3 재흡수', 'Na⁺ · RAAS', '#9c36b5'), ('14.4 분비', 'H⁺ · K⁺ · 유기 이온', '#ae3ec9'), ('14.5 배설', '청소율 · 소변 농축', '#3b5bdb')]) +
        grid('1.05fr 1fr',
            card('한 줄 요약', '콩팥은 <b>소변 = 여과 − 재흡수 + 분비</b>로 체액의 부피·삼투농도·이온·pH를 지키고, <b>혈장량</b>을 바꿔 <span class="hy">혈압을 장기 조절</span>한다. 사구체에서 혈장의 20%가 <b>순여과압 10 mmHg</b>(55 − 30 − 15)로 걸러지고(GFR 125 mL/분), 124 mL가 재흡수된다. <b>근위세뇨관</b>이 조절 없이 대부분(Na⁺ 67%)을 되찾고, <b>원위·집합관</b>은 <span class="hp">알도스테론(Na⁺ ↑, K⁺ 분비)</span>과 <b>바소프레신(물)</b>으로 최종량을 정한다. 헨레 고리의 <b>역류 증폭</b>이 수질 기울기(300 → 1200)를 만들고 곧은혈관이 지킨다.', 'sum big'),
            col(card('🎯 교수님 강조 (11/26 · 11/30 녹화 강의)', '<ol><li>"<b>알도스테론과 안지오텐신 II</b> 기능을 잘 알아두시고"</li><li>RAAS = "신장이 혈압과 체액량을 조절하는 <b>가장 중요한 호르몬 시스템</b>" · 레닌·ACE·Ang II</li><li>"<b>Na⁺ 재흡수가 굉장히 중요</b>" — 콩팥 에너지의 80%</li><li>청소율 공식은 "<b>시험에 내지는 않겠습니다</b>" → 크레아티닌 ≈ GFR만</li><li>요관·방광·요도는 다루지 않음</li></ol>', 'warn'),
                card('💡 숫자', '네프론 <b>100만</b>/콩팥 · 겉질 80 : 속질곁 20 · 심박출량 <b>20–25%</b> · 여과 <b>20%</b> · 55 − 30 − 15 = <b>10</b> · GFR <b>125</b> → 124 재흡수 · Na⁺ <b>67 / 25 / 8%</b> · 물 65 / 15 / 20% · 요소 <b>50%</b> · 수질 <b>300 → 1200</b> · 소변 100 ~ 1200 mOsm/L', 'tip'))), 'Slides 1–47')

    page('PART 01', '콩팥의 기능 · 네프론 · 기본 과정',
        grid('1fr 1.1fr 1fr',
            col(card('정의 — 콩팥이 하는 일', '<ul><li>물·<b>삼투농도</b>·이온(Na⁺ K⁺ Ca²⁺ H⁺ HCO₃⁻ PO₄³⁻…)</li><li><b>혈장량 → 혈압의 장기 조절</b></li><li>산–염기(H⁺ 분비, HCO₃⁻)</li><li>노폐물·<b>약물</b> 배설(CO₂는 폐)</li><li><b>레닌</b> · <b>EPO</b> · <b>비타민 D</b> 활성화</li></ul><small>백혈구 생성 조절 ✗ (교수님 요약 문제)</small>', 'def'),
                img('c14-06', '1 여과 → 2 재흡수 → 3 분비 → 4 배설', '54mm')),
            col(card('🧩 네프론의 구성', tbl(['성분', '구조', '역할'], [
                    ['혈관', '<b>들세동맥</b> → 사구체 → <b>날세동맥</b>', '들세동맥이 더 굵어 사구체 압력 ↑'],
                    ['', '세뇨관 주위 모세혈관', '<b>재흡수·분비</b> 교환'],
                    ['', '<b>곧은혈관</b>(속질곁만)', '<b>역류 교환</b> → 기울기 보존'],
                    ['세뇨관', '보먼주머니 → <b>근위</b>(피질)', '<b>조절 X</b>, 대량 재흡수'],
                    ['', '<b>헨레 고리</b>(수질)', '수질 삼투 기울기'],
                    ['', '<b>원위</b>(피질) → 집합관', '<b>호르몬 조절</b>, K⁺·H⁺ 분비'],
                    ['복합', '<b>사구체옆장치</b>', '들세동맥 + 원위세뇨관 → <b>레닌</b>']]), 'mint'),
                card('겉질 vs 속질곁 네프론', tbl(['', '겉질', '속질곁'], [['비율', '80%', '20%'], ['헨레 고리', '짧음', '<b>수질 끝까지</b>'], ['모세혈관', '세뇨관 주위', '<b>곧은혈관</b>']]) + '<small>교수님 85 : 15 → 슬라이드 80 : 20 기준</small>')),
            col(card('🔁 기본 과정', '<b>배설 = 여과 − 재흡수 + 분비</b>' + tbl(['과정', '방향', '성격'], [['여과', '사구체 → 보먼', '<b>비선택적</b>, 20%'], ['재흡수', '세뇨관 → 혈액', '선택적'], ['분비', '혈액 → 세뇨관', '선택적']]) +
                    '<p style="margin-top:1.2mm">혈액 → 세뇨관 길은 <b>여과 + 분비</b> 두 번 · 80%는 날세동맥으로</p>', 'sum'),
                img('c14-16', 'GF · TR · TS — 20%만 여과', '62mm'))), 'Slides 3–16')

    page('PART 02', '사구체 여과 · GFR · 혈압 조절',
        grid('1fr 1fr 1.05fr',
            col(card('정의 — 사구체막 3층', '<ol><li>모세혈관 <b>내피</b> — 창(fenestration)</li><li><b>기저막</b> — 세포 없음</li><li>보먼주머니 안쪽층 <b>발세포</b> — 여과 틈새</li></ol>"어느 모세혈관보다 <b>투과성이 높다</b>" → 여과액 = <b>단백질 없는 혈장</b>(혈구가 나오면 혈뇨, 단백질이면 단백뇨)', 'def'),
                img('c14-18', '사구체막: 내피 구멍 · 기저막 · 발세포 틈새', '46mm')),
            col(card('⚖ 순여과압 (표 14-1)', tbl(['힘', 'mmHg', '방향'], [['사구체 모세혈관 혈압', '<b>55</b>', '여과 ↑'], ['혈장 교질 삼투압', '30', '여과 ↓'], ['보먼주머니 정수압', '15', '여과 ↓'], ['<b>순여과압</b>', '<b>10</b>', '여과 ↑']]) +
                    '<p style="margin-top:1.2mm"><b>GFR = K<sub>f</sub> × 순여과압</b> ≈ 125 mL/분 · K<sub>f</sub> = 표면적·투과성(사구체신염·당뇨병성 신증 → ↓)</p>', 'sum'),
                card('🎯 GFR 조절', '조절할 수 있는 건 <b>사구체 모세혈관 혈압</b>뿐 → <b>들세동맥</b>' + tbl(['', '들세동맥', 'GFR'], [['수축(저항 ↑)', '혈류 ↓', '<b>↓</b>'], ['확장(저항 ↓)', '혈류 ↑', '<b>↑</b>']]) +
                    '<p style="margin-top:1.2mm"><b>자가조절</b>(내인성): MAP가 변해도 GFR 일정 · <b>교감</b>(외인성): 일부러 GFR ↓ → 소변 ↓ (위급 시 override)</p>', 'mint')),
            col(card('🩸 혈압의 단기 vs 장기 조절', tbl(['', '단기', '장기'], [['기전', '압력수용기 반사(대동맥궁·경동맥동 → 뇌간 → 교감) → CO ↑ · TPR ↑', '교감 → <b>들세동맥 수축</b> → GFR ↓ → 소변 ↓ + 재흡수 ↑ + 갈증 → <b>혈장량 ↑</b>'], ['속도', '분', '시간~일']]), 'tip'),
                img('c14-22', '장기 조절: 들세동맥 수축 → GFR ↓ → 소변 ↓ → 혈압 ↑', '60mm'),
                card('콩팥 혈류', '심박출량의 <b>20–25%</b> — 자기 대사가 아니라 많은 혈장을 <b>걸러 주려고</b>', 'why'))), 'Slides 17–23')

    page('PART 03', '세뇨관 재흡수 · Na⁺ · RAAS · 분비',
        grid('1fr 1.1fr 1fr',
            col(card('정의 — 재흡수', '엄청나고·선택적이고·가변적: <b>125 중 124 mL/분</b> · 세포 사이는 치밀이음부 → <b>5개 장벽</b>(내강막 → 세포질 → 기저외측막 → 간질액 → 모세혈관 벽)' +
                    tbl(['수동', '능동'], [['물 · Cl⁻ · 요소', '포도당·아미노산(1단계, <b>SGLT</b>) · Na⁺(3단계, <b>Na⁺-K⁺ 펌프</b>)']]) +
                    '<p style="margin-top:1.2mm">💊 <b>SGLT2 억제제</b>(엠파·다파글리플로진) → 포도당 재흡수 ✗ → 2형 당뇨 혈당 ↓</p>', 'def'),
                card('⚡ Na⁺ 재흡수 — "굉장히 중요"', '콩팥 에너지의 <b>80%</b> · 엔진 = <b>기저외측 Na⁺-K⁺ 펌프</b>(한 곳에서만 ATP)' + tbl(['구간', 'Na⁺', '특징'], [['근위', '<b>67%</b>', '조절 X, 포도당·아미노산과 함께'], ['헨레 상행지', '<b>25%</b>', '<b>Na⁺-K⁺-2Cl⁻</b>, 물 불투과'], ['원위·집합관', '<b>8%</b>', '<b>알도스테론</b>']]), 'mint')),
            col(card('🎯 RAAS — "가장 중요한 호르몬 시스템"', '자극: <b>NaCl ↓ · ECF ↓ · 혈압 ↓</b>(콩팥 압력수용기, JGA의 NaCl 감지, 교감)' +
                    flow('<b>레닌</b>(콩팥)', '안지오텐시노겐(<b>간</b>) → Ang I', '<b>ACE</b>(폐)', '<b>Ang II</b>', '<b>알도스테론</b>(부신피질)', small=True) +
                    tbl(['호르몬', '작용'], [['<b>알도스테론</b>', '원위·집합관 <b>Na⁺ 재흡수 ↑, K⁺·H⁺ 분비 ↑</b> → Cl⁻·물 따라감 → 혈장량 ↑'], ['<b>Ang II</b>', '알도스테론 ↑ · <b>세동맥 수축</b> · <b>갈증</b> · <b>바소프레신</b> ↑'], ['자극 2', '<b>혈장 K⁺ ↑</b>도 알도스테론을 직접 ↑']]) +
                    '<p style="margin-top:1.2mm">💊 RAAS 저해제 = 고혈압 치료제(ACE 억제제, ARB, 스피로노락톤)</p>', 'warn'),
                img('c14-31', 'RAAS: 간 · 콩팥 · 폐 · 부신피질', '52mm')),
            col(card('🔄 세뇨관 분비', tbl(['물질', '의미'], [['<b>H⁺</b>', '<b>산–염기</b> — 근위·원위·집합관'], ['<b>K⁺</b>', '<b>알도스테론</b>, Na⁺ 재흡수와 짝 · 혈장 K⁺는 엄격 조절'], ['유기 이온', '근위 <b>비특이적 운반체</b> → 약물·농약·첨가물']]), 'tip'),
                card('근위 vs 원위·집합관 (표 14-2)', tbl(['', '근위', '원위·집합관'], [['재흡수', '<b>대부분</b>(Na⁺ 67 · 물 65 · 포도당 100 · 요소 50%)', 'Na⁺(알도스테론) · 물(바소프레신)'], ['분비', '<b>대부분</b>(H⁺ · 유기 이온), K⁺ 제외', '<b>K⁺</b> · H⁺'], ['성격', '양적 · 고정', '<b>질적 · 최종량</b>']]), 'sum'),
                card('Cl⁻ · 물 · 요소', 'Na⁺가 빠지면 Cl⁻(전기) → 물(삼투, 아쿠아포린) → 물이 빠져 <b>요소</b>가 농축 → <b>50%</b> 수동 재흡수', 'why'))), 'Slides 25–39')

    page('PART 04', '청소율 · 소변 농축 · 곧은혈관',
        grid('1fr 1.15fr 1fr',
            col(card('정의 — 혈장 청소율', '1분 동안 특정 물질이 <b>완전히 제거된 혈장의 부피</b>(양이 아님) · CL = U × V̇ / P <small>(교수님: 공식은 시험에 안 냄)</small><br>⭐ <b>크레아티닌</b>: 자유 여과, 재흡수 ✗, 약간 분비 → 청소율 ≈ <b>GFR</b> → 콩팥 기능 평가', 'def'),
                card('💧 수분 상태와 소변', tbl(['상태', 'ECF', '바소프레신', '소변'], [['물 부족', '고장성', '<b>↑</b>', '진함(최대 <b>1200</b>), 적게'], ['물 과잉', '저장성', '<b>없음</b>', '묽음(약 <b>100</b>), 많이']]), 'tip'),
                card('곧은혈관 = 역류 교환', '헨레 고리와 나란히 300 → 1200 → 300: 하행 = 물 나가고 NaCl 들어와 진해짐, 상행 = 다시 묽어짐 → 재흡수한 물은 가져가고 <b>기울기는 씻어내지 않음</b> · 나가는 피 = <b>등장성 300</b>', 'why')),
            col(card('🎯 역류 증폭 — 기울기 만들기', tbl(['헨레 고리', '물', 'NaCl'], [['하행지', '<b>투과</b>(빠져나감)', '—'], ['상행지', '<b>불투과</b> ← 원동력', '<b>능동 수송</b>']]) +
                    '<p style="margin-top:1.2mm">같은 높이에서 <b>200 차이</b> → 액체가 밀려 내려가며 반복 → <b>피질 300 → 수질 1200</b> = "작은 수평 차이를 <b>수직으로 증폭</b>" · 상행지를 나가는 액체 = <b>100</b></p>', 'sum'),
                img('c14-43', '역류 증폭 단계: 200 차이가 반복되어 1200까지', '66mm')),
            col(card('🧪 바소프레신(ADH)', '<b>뇌하수체 후엽</b> → 원위·집합관 주세포' + flow('V₂ 수용체(<b>기저외측</b>)', 'cAMP', '<b>AQP-2</b>를 내강막에 삽입', '물 재흡수 ↑', small=True) +
                    '물은 기저외측 <b>AQP-3/4</b>로 나가 혈액으로 · 있으면 <b>농축뇨</b>, 없으면 <b>희석뇨</b>', 'mint'),
                img('c14-45', '바소프레신 → V₂ → cAMP → AQP-2 삽입', '50mm'),
                card('⚠ 함정', '<ul><li>"곧은혈관이 기울기를 만든다" ✗ — <b>헨레 고리</b></li><li>"상행지는 물을 통과시킨다" ✗</li><li>"V₂ 수용체는 내강막에" ✗ — 기저외측</li><li>신부전 → 요독증 · 산증 · 고칼륨 · 고혈압 · <b>빈혈(EPO ↓)</b></li></ul>', 'warn'))), 'Slides 41–47')

    qpage('PART 01–02', '네프론 · 여과 ①',
        FQ('c14-16-q', 'The figure shows the three central renal processes. Identify the structures labeled <b>A</b> to <b>F</b>.', '그림은 콩팥의 세 중심 과정이다. A~F의 이름을 쓰시오.',
           [('A', '들세동맥 Afferent arteriole'), ('B', '날세동맥 Efferent arteriole'), ('C', '사구체 Glomerulus'), ('D', '보먼주머니 Bowman\'s capsule'), ('E', '세뇨관 주위 모세혈관 Peritubular capillary'), ('F', '세뇨관 Kidney tubule')],
           W('혈액: A → C(여과 GF, 20%) → B(80%) → E(재흡수 TR · 분비 TS 교환)', 'A가 B보다 굵어 사구체 모세혈관 혈압 55 mmHg 유지') + K('GF = 비선택적', 'TR = 세뇨관 → 혈액', 'TS = 혈액 → 세뇨관'), stars=2, h='52mm'),
        TF([('The net filtration pressure across the glomerular membrane is about 10 mm Hg, the difference between the glomerular capillary blood pressure (55) and the opposing plasma-colloid osmotic pressure (30) and Bowman\'s capsule hydrostatic pressure (15).', '사구체막의 순여과압은 약 10 mmHg로, 사구체 모세혈관 혈압(55)에서 반대 방향의 혈장 교질 삼투압(30)과 보먼주머니 정수압(15)을 뺀 값이다.'),
            ('Sympathetic stimulation dilates the afferent arterioles, increasing the GFR and urine volume to raise blood pressure.', '교감 자극은 들세동맥을 확장시켜 GFR과 소변량을 늘림으로써 혈압을 올린다.'),
            ('About 20% of the plasma entering the glomerulus is filtered, and the remaining 80% leaves through the efferent arteriole.', '사구체로 들어온 혈장의 약 20%가 여과되고, 나머지 80%는 날세동맥으로 나간다.'),
            ('Juxtamedullary nephrons have long loops of Henle that dip deep into the medulla and are accompanied by the vasa recta.', '속질곁 네프론은 수질 깊이 내려가는 긴 헨레 고리를 가지며 곧은혈관이 함께 있다.'),
            ('The kidneys regulate white blood cell production by secreting erythropoietin.', '콩팥은 에리트로포이에틴을 분비해 백혈구 생성을 조절한다.')],
           'T F T T F', W('(2) ✗ 교감 → 들세동맥 <b>수축</b> → GFR <b>↓</b> → 소변 ↓ → 혈장량 보존', '(5) ✗ EPO는 <b>적혈구</b> 생성 — 교수님 요약 문제 ④'), stars=2), cols=2)

    qpage('PART 02–03', 'GFR · RAAS ②',
        MC('Which TWO statements about the regulation of GFR and blood pressure by the kidneys are correct? <b>(Choose two.)</b>', 'GFR과 콩팥의 혈압 조절에 대한 설명으로 옳은 것 두 개는?',
           [('The glomerular capillary blood pressure is the only filtration force that is subject to physiological control, mainly by changing afferent arteriolar resistance.', '사구체 모세혈관 혈압은 생리적으로 조절되는 유일한 여과 힘이며, 주로 들세동맥 저항을 바꿔 조절된다.'),
            ('When arterial pressure falls, sympathetic constriction of the afferent arterioles lowers the GFR and urine volume, which helps conserve fluid and restore blood pressure over hours to days.', '동맥압이 떨어지면 교감신경에 의한 들세동맥 수축이 GFR과 소변량을 낮춰, 몇 시간에서 며칠에 걸쳐 체액을 보존하고 혈압을 회복시킨다.'),
            ('Dilation of the afferent arteriole lowers glomerular capillary blood pressure and therefore decreases the GFR.', '들세동맥 확장은 사구체 모세혈관 혈압을 낮추어 GFR을 감소시킨다.'),
            ('Autoregulation of the GFR works mainly by changing the plasma-colloid osmotic pressure.', 'GFR의 자가조절은 주로 혈장 교질 삼투압을 바꾸어 일어난다.'),
            ('An increase in mean arterial pressure is one of the main stimuli for renin release.', '평균 동맥압의 증가는 레닌 분비의 주요 자극 중 하나다.')], '①, ②',
           W('① ✔ 교질 삼투압·보먼 정수압은 조절 대상 ✗', '② ✔ 장기 조절', '③ ✗ 확장 → 혈류 ↑ → GFR <b>↑</b>(교수님 요약 문제 ②)', '④ ✗ 자가조절 = <b>들세동맥 지름</b>', '⑤ ✗ 레닌은 혈압 <b>↓</b>일 때 — MAP ↑이면 레닌 ↓(요약 문제 ①)'), pick=2, stars=2, prof=True),
        BOX('Fill in blanks (1)–(10) with the most appropriate words from the box. Not all words are used.', '상자에서 알맞은 단어를 골라 빈칸 (1)~(10)을 채우시오. 쓰지 않는 단어도 있다.',
            ['renin', 'angiotensinogen', 'angiotensin I', 'ACE', 'angiotensin II', 'aldosterone', 'vasopressin', 'adrenal cortex', 'liver', 'lungs', 'K⁺', 'erythropoietin'],
            'When NaCl, ECF volume or arterial pressure falls, the kidneys secrete <u>(1)</u>, which converts <u>(2)</u> made by the <u>(3)</u> into <u>(4)</u>. In the <u>(5)</u>, <u>(6)</u> converts it to <u>(7)</u>, which stimulates the <u>(8)</u> to secrete <u>(9)</u>. This hormone increases Na⁺ reabsorption and <u>(10)</u> secretion in the distal and collecting tubules, and water follows Na⁺ by osmosis.',
            ['renin', 'angiotensinogen', 'liver', 'angiotensin I', 'lungs', 'ACE', 'angiotensin II', 'adrenal cortex', 'aldosterone', 'K⁺'],
            W('함정: <b>vasopressin · erythropoietin</b>은 안 씀(바소프레신은 Ang II가 분비를 촉진하는 별도 호르몬)') + K('레닌(콩팥) → 간 → 폐(ACE) → 부신피질', '알도스테론 = Na⁺ ↑ · K⁺ 분비'), stars=3), cols=2)

    qpage('PART 03', '재흡수 · 분비 ③',
        MC('Which TWO statements about tubular reabsorption and secretion are correct? <b>(Choose two.)</b>', '세뇨관 재흡수와 분비에 대한 설명으로 옳은 것 두 개는?',
           [('About 67% of the filtered Na⁺ is reabsorbed in the proximal tubule, driven by the basolateral Na⁺–K⁺ pump, and this reabsorption is not subject to hormonal control.', '여과된 Na⁺의 약 67%는 기저외측 Na⁺–K⁺ 펌프의 힘으로 근위세뇨관에서 재흡수되며, 이 재흡수는 호르몬 조절을 받지 않는다.'),
            ('Aldosterone acts on the distal and collecting tubules to increase Na⁺ reabsorption and K⁺ secretion, and a rise in plasma K⁺ directly stimulates aldosterone secretion.', '알도스테론은 원위세뇨관과 집합관에 작용해 Na⁺ 재흡수와 K⁺ 분비를 늘리며, 혈장 K⁺ 상승은 알도스테론 분비를 직접 자극한다.'),
            ('Glucose and amino acids are reabsorbed by simple passive diffusion, so SGLT2 inhibitors have no effect on urinary glucose.', '포도당과 아미노산은 단순 수동 확산으로 재흡수되므로 SGLT2 억제제는 소변 포도당에 영향이 없다.'),
            ('Urea is not reabsorbed at all, because all metabolic wastes are completely excluded from tubular reabsorption.', '모든 대사 노폐물은 세뇨관 재흡수에서 완전히 제외되므로 요소는 전혀 재흡수되지 않는다.'),
            ('The distal and collecting tubules are the main sites for secreting drugs and other foreign organic ions through nonspecific carriers.', '원위세뇨관과 집합관은 비특이적 운반체를 통해 약물 등 외래 유기 이온을 분비하는 주된 장소다.')], '①, ②',
           W('① ✔ 근위 = 양적 · 고정', '② ✔ 알도스테론의 이중 조절', '③ ✗ 포도당·아미노산은 <b>능동</b>(SGLT) → SGLT2 억제제가 소변 포도당 ↑', '④ ✗ 요소는 <b>50%</b> 수동 재흡수', '⑤ ✗ 유기 이온 분비는 <b>근위세뇨관</b>'), pick=2, stars=2),
        TF([('Tubular reabsorption is tremendous: of the 125 mL of fluid filtered per minute, about 124 mL is reabsorbed.', '세뇨관 재흡수는 엄청나서, 1분에 여과되는 125 mL 중 약 124 mL가 재흡수된다.'),
            ('Angiotensin II causes arteriolar vasoconstriction, thirst and vasopressin release in addition to stimulating aldosterone secretion.', '안지오텐신 II는 알도스테론 분비 자극 외에도 세동맥 수축, 갈증, 바소프레신 분비를 일으킨다.'),
            ('H⁺ secretion occurs in the proximal, distal and collecting tubules and is important in acid–base balance.', 'H⁺ 분비는 근위·원위세뇨관과 집합관에서 일어나며 산–염기 균형에 중요하다.'),
            ('Angiotensin-converting enzyme (ACE) is produced mainly by the liver.', '안지오텐신 전환효소(ACE)는 주로 간에서 만들어진다.'),
            ('Creatinine is freely filtered, not reabsorbed and only slightly secreted, so its plasma clearance is used to estimate the GFR.', '크레아티닌은 자유롭게 여과되고 재흡수되지 않으며 약간만 분비되므로, 그 혈장 청소율로 GFR을 추정한다.')],
           'T T T F T', W('(4) ✗ ACE = <b>폐 모세혈관</b> 내피(간은 안지오텐시노겐)', '(5) ✔ 공식 계산은 안 냄 — 의미만'), stars=2), cols=2)

    qpage('PART 04', '소변 농축 ④',
        MC('Which TWO statements about urine concentration are correct? <b>(Choose two.)</b>', '소변 농축에 대한 설명으로 옳은 것 두 개는?',
           [('The ascending limb of the loop of Henle actively transports NaCl out but is impermeable to water, which is the driving force of countercurrent multiplication.', '헨레 고리 상행지는 NaCl을 능동적으로 내보내지만 물은 통과시키지 않으며, 이것이 역류 증폭의 원동력이다.'),
            ('When there is a water deficit, vasopressin binds V₂ receptors on the basolateral membrane of principal cells and, via cAMP, inserts AQP-2 water channels into the luminal membrane.', '물이 부족하면 바소프레신이 주세포 기저외측막의 V₂ 수용체에 결합하고, cAMP를 거쳐 AQP-2 물 통로를 내강막에 삽입한다.'),
            ('The vasa recta generate the vertical medullary osmotic gradient by actively pumping NaCl into the interstitial fluid.', '곧은혈관은 NaCl을 간질액으로 능동적으로 퍼내어 수질의 세로 삼투 기울기를 만든다.'),
            ('Fluid leaving the ascending limb and entering the distal tubule is hypertonic, at about 1200 mOsm/liter.', '상행지를 떠나 원위세뇨관으로 들어가는 액체는 약 1200 mOsm/L의 고장성이다.'),
            ('In the absence of vasopressin, the collecting ducts become highly permeable to water, so a small volume of concentrated urine is excreted.', '바소프레신이 없으면 집합관이 물에 매우 투과적이 되어 소량의 진한 소변이 배설된다.')], '①, ②',
           W('① ✔ 상행지 물 불투과', '② ✔ V₂ = 기저외측, AQP-2 = 내강막 삽입', '③ ✗ 기울기를 <b>만드는</b> 건 헨레 고리, 곧은혈관은 <b>지킨다</b>(역류 교환)', '④ ✗ 원위로 가는 액체는 <b>100</b>(저장성)', '⑤ ✗ 바소프레신 없으면 <b>불투과</b> → 다량의 <b>묽은</b> 소변'), pick=2, stars=3),
        TF([('The osmolarity of the medullary interstitial fluid increases from about 300 mOsm/liter near the cortex to about 1200 mOsm/liter in the deepest medulla.', '수질 간질액의 삼투농도는 피질 근처 약 300 mOsm/L에서 가장 깊은 수질의 약 1200 mOsm/L까지 높아진다.'),
            ('The descending limb of the loop of Henle is permeable to water, so water leaves it by osmosis as the fluid moves deeper into the medulla.', '헨레 고리 하행지는 물을 통과시키므로, 액체가 수질 깊이 내려갈수록 삼투로 물이 빠져나간다.'),
            ('Vasopressin is secreted by the anterior pituitary and acts mainly on the proximal tubule.', '바소프레신은 뇌하수체 전엽에서 분비되어 주로 근위세뇨관에 작용한다.'),
            ('Blood leaving the medulla through the vasa recta is essentially isotonic to the incoming arterial blood.', '곧은혈관을 통해 수질을 떠나는 혈액은 들어오는 동맥혈과 거의 등장성이다.'),
            ('Renal failure can cause anemia because the kidneys fail to produce enough erythropoietin.', '신부전은 콩팥이 에리트로포이에틴을 충분히 만들지 못해 빈혈을 일으킬 수 있다.')],
           'T T F T T', W('(3) ✗ <b>뇌하수체 후엽</b>, <b>원위세뇨관·집합관</b>에 작용'), stars=2), cols=2)

    qpage('PART 01–04', '서술형',
        ES('When blood pressure and ECF volume fall, explain how the kidneys help restore them, including the extrinsic control of GFR and the renin–angiotensin–aldosterone system.', '혈압과 ECF 부피가 떨어졌을 때 콩팥이 이를 회복시키는 과정을 GFR의 외인성 조절과 레닌–안지오텐신–알도스테론계를 포함해 설명하시오.',
           '혈압이 떨어지면 압력수용기 반사로 교감 활성이 커져 <b>들세동맥이 수축</b>하고, 사구체 모세혈관 혈압이 낮아져 <b>GFR과 소변량이 감소</b>한다(자가조절을 넘어서는 외인성 조절). 동시에 콩팥 압력수용기의 혈압 저하 감지, <b>사구체옆장치</b>의 NaCl 감소 감지, 교감 자극으로 콩팥이 <b>레닌</b>을 분비한다. 레닌은 <b>간</b>의 안지오텐시노겐을 안지오텐신 I으로 바꾸고, <b>폐 모세혈관의 ACE</b>가 이를 <b>안지오텐신 II</b>로 바꾼다. 안지오텐신 II는 <b>부신피질</b>에서 <b>알도스테론</b> 분비를 일으키고, 알도스테론은 원위세뇨관과 집합관의 <b>Na⁺-K⁺ 펌프</b>를 늘려 Na⁺ 재흡수(K⁺ 분비)를 높인다. Cl⁻가 전기적으로, 물이 삼투로 Na⁺를 따라가 <b>혈장량이 늘고</b> 혈압이 회복된다. 안지오텐신 II는 또 세동맥 수축(TPR ↑), 갈증, <b>바소프레신</b> 분비로 혈압과 체액을 함께 올린다.',
           K('교감 → 들세동맥 수축 → GFR ↓', '레닌(콩팥) → 간 → ACE(폐) → Ang II', '알도스테론: Na⁺ ↑ · K⁺ 분비', 'Ang II: 수축·갈증·바소프레신'), stars=3),
        ES('Explain how the kidneys produce concentrated urine during a water deficit, describing countercurrent multiplication in the loop of Henle, the action of vasopressin, and the role of the vasa recta.', '물이 부족할 때 콩팥이 진한 소변을 만드는 과정을 헨레 고리의 역류 증폭, 바소프레신의 작용, 곧은혈관의 역할을 들어 설명하시오.',
           '속질곁 네프론의 긴 헨레 고리에서 <b>상행지</b>는 NaCl을 능동적으로 내보내지만 <b>물은 통과시키지 않고</b>, <b>하행지</b>는 물을 통과시킨다. 그래서 같은 높이에서 상행지와 하행지·간질액 사이에 약 200 mOsm/L 차이가 생기고, 액체가 계속 밀려 내려가며 이 과정이 반복되어 수질 간질액에 <b>300 → 1200 mOsm/L</b>의 세로 삼투 기울기가 쌓인다(<b>역류 증폭</b>). 상행지를 나가는 액체는 약 100 mOsm/L로 묽다. 물이 부족하면 <b>뇌하수체 후엽</b>에서 <b>바소프레신</b>이 분비되어 원위세뇨관·집합관 주세포의 기저외측 <b>V₂ 수용체</b>에 결합하고, <b>cAMP</b>를 통해 <b>AQP-2</b>를 내강막에 삽입한다. 그러면 집합관이 진한 수질을 지나며 물을 빼앗겨 최대 1200 mOsm/L의 소량의 진한 소변이 된다. <b>곧은혈관</b>은 헨레 고리와 나란히 흐르며 <b>역류 교환</b>으로 재흡수된 물은 가져가되 수질 용질은 씻어내지 않아 기울기를 <b>보존</b>한다.',
           K('상행지 물 불투과 · NaCl 능동', '300 → 1200', '바소프레신 → V₂ → cAMP → AQP-2', '곧은혈관 = 기울기 보존'), stars=3), cols=2)

    memo([('🫘 콩팥·네프론', '소변 = 여과 − 재흡수 + 분비<br>여과 20% · 80%는 날세동맥<br>근위(피질) 조절 X · 원위 호르몬<br>JGA = 레닌 · 곧은혈관 = 속질곁<br>기능: 혈압 장기 조절 · 레닌 · EPO · 비타민 D'),
          ('⚖ 여과·GFR', '55 − 30 − 15 = <b>10</b><br>GFR 125 → 124 재흡수<br>들세동맥 수축 → GFR ↓<br>교감 → GFR ↓ → 소변 ↓<br>GFR = K<sub>f</sub> × 순여과압'),
          ('🎯 RAAS·재흡수', 'Na⁺ 67 / 25 / 8% · 에너지 80%<br>레닌(콩팥) → 간 → ACE(폐) → Ang II → 알도스테론(부신피질)<br>알도스테론 = Na⁺ ↑ · K⁺ 분비<br>Ang II = 수축 · 갈증 · 바소프레신<br>SGLT2 억제제 · 요소 50%'),
          ('💧 분비·농축', 'H⁺ = 산–염기 · K⁺ = 알도스테론<br>크레아티닌 청소율 ≈ GFR<br>상행지 물 ✗ → 역류 증폭 300 → 1200<br>바소프레신(후엽) → V₂ → cAMP → AQP-2<br>곧은혈관 = 역류 교환(보존)')],
         '<ol><li>교감 → 들세동맥 <b>수축</b> → GFR <b>↓</b></li><li>알도스테론 = Na⁺ 재흡수, K⁺ <b>분비</b>(재흡수 ✗)</li><li>기울기를 <b>만드는</b> 건 헨레 고리, 곧은혈관은 <b>지킨다</b></li></ol>',
         ['혈압이 떨어지면 교감신경이 들세동맥을 수축시켜 GFR과 소변량을 줄이고, 레닌–안지오텐신–알도스테론계가 Na⁺와 물을 보존해 혈장량과 혈압을 회복시킨다.',
          '알도스테론은 원위세뇨관과 집합관에서 Na⁺ 재흡수와 K⁺ 분비를 늘리고, 바소프레신은 AQP-2를 삽입해 물 재흡수를 늘린다.',
          '헨레 고리의 역류 증폭이 수질 삼투 기울기를 만들고, 곧은혈관의 역류 교환이 그 기울기를 보존한다.'])
