from lib import *

def build():
    chapter(13, 'The Respiratory System')
    c = CH['color']
    page('CHAPTER 13', 'The Respiratory System — 한 장 지도',
        chev([('13.1 해부', '기도·폐포·흉막', '#4c6ef5'), ('13.2 역학', '압력·근육·순응도', c), ('13.3 가스 교환', '분압 기울기', '#0c8599'), ('13.4 가스 운반', 'Hb·CO₂ 3형태', '#7048e8'), ('13.5 조절', '연수·화학수용기', '#1864ab')]) +
        grid('1.05fr 1fr',
            card('한 줄 요약', '근육은 폐가 아니라 <b>흉강</b>의 부피를 바꾼다 → 흉막내압(756)이 늘 폐포내압보다 낮아 <b>경벽압 4 mmHg</b>로 폐가 따라 늘어난다 → <b>보일의 법칙</b>으로 폐포내압이 759/761로 오르내리며 공기가 드나든다. 폐포에서는 <span class="hy">분압 기울기</span>로 O₂·CO₂가 <b>수동 확산</b>(160 → 폐포 100, 정맥혈 40/46)되고, O₂는 98.5%가 <b>헤모글로빈</b>(S자 해리곡선)에, CO₂는 60%가 <b>HCO₃⁻</b>로 운반된다. 리듬은 <b>연수(프리뵈트징거)</b>가 만들고, 환기량은 주로 <span class="hp">동맥 P<sub>CO2</sub></span>가 정한다.', 'sum big'),
            col(card('🎯 교수님 강조 (11/19 · 11/23 녹취)', '<ol><li><b>외늑간근 = 들숨, 내늑간근 = 날숨</b> — "구분해야 됩니다"</li><li>주 들숨근 = <b>횡격막 + 외늑간근</b> / 주 날숨근 = <b>복근 + 내늑간근</b></li><li>"<b>기압 차가 중요</b>" · 흉막 주머니 = 폐를 둘러싼 주머니</li><li>⚠️ 교과서 정정: 말초 화학수용기는 <b>경동맥체가 가장 중요</b>(O₂도 주로 경동맥체)</li><li>폐용적 세부 지표(IRV·ERV…)는 "<b>넘어가도록</b>"</li></ol>', 'warn'),
                card('💡 숫자', '대기 <b>760</b> · 흉막내압 <b>756</b> · 경벽압 <b>4</b> · 들숨 759 / 날숨 761 · TV <b>500</b> · RV <b>1.2 L</b> · 최대 5.7 L(남)/4.2 L(여) · 사강 <b>150</b> · 대기 P<sub>O2</sub> <b>160</b> → 폐포 <b>100</b> · 정맥혈 <b>40/46</b> · P<sub>H2O</sub> 47 · O₂ 용해 <b>1.5%</b> · CO₂ 10/30/<b>60%</b>', 'tip'))), 'Slides 1–49')

    page('PART 01', '호흡 해부 · 압력과 경벽압',
        grid('1fr 1.1fr 1fr',
            col(card('정의 — 외호흡 4단계', '<ol><li><b>환기</b>: 대기 ↔ 폐포</li><li><b>폐포 ↔ 폐모세혈관</b> 확산</li><li>혈액으로 <b>운반</b></li><li><b>체순환 모세혈관 ↔ 조직</b> 확산</li></ol>세포호흡(미토콘드리아)과 구분 · 가스 이동은 <b>능동수송 없음</b>', 'def'),
                card('🫁 기도와 폐포', tbl(['구조', '특징'], [['기관·기관지', '<b>연골 고리</b> → 늘 열림'], ['세기관지', '<b>평활근</b>(ANS) — 부교감 → 수축'], ['1형 폐포세포', '대부분, 납작 → <b>가스 교환</b>'], ['2형 폐포세포', '입방형 → <b>표면활성제</b> + 1형 재생']]) +
                    '<p style="margin-top:1.2mm">공기–혈액 두께 <b>0.5 μm</b> · 폐포 대식세포 · 폐엽 <b>왼쪽 2 · 오른쪽 3</b></p>', 'mint')),
            col(card('🎈 흉막 주머니', '폐 바로 바깥의 이중막 주머니(풍선에 막대사탕). 안쪽 <b>흉막강</b>은 흉막액으로 차 있어 폐를 흉벽에 붙잡는다. 근육은 <b>흉강</b> 부피를 바꾸고 폐는 <b>따라간다</b>(폐엔 근육 없음).', 'tip'),
                img('c13-12', '폐 · 흉막 주머니 · 흉벽 · 횡격막', '50mm'),
                card('⚖ 세 압력', tbl(['압력', '휴식', '들숨', '날숨'], [['대기압', '760', '760', '760'], ['폐포내압', '760', '<b>759</b>', '<b>761</b>'], ['흉막내압', '<b>756</b>', '754', '756']]) +
                    '<p style="margin-top:1.2mm"><b>경벽압 = 폐포내압 − 흉막내압 = 4</b> → 폐가 늘 부풀어 있음. 흉막내압은 정상 호흡 내내 <b>대기압보다 낮다</b>.</p>', 'sum')),
            col(img('c13-17', '들숨 전 · 들숨 중(순응도) · 날숨 중(탄력 반동) — mmHg', '46mm'),
                card('보일의 법칙', '<b>P₁V₁ = P₂V₂</b> — 흉강 ↑ → 폐포내압 ↓ → 공기 유입 / 흉강 ↓ → 폐포내압 ↑ → 공기 유출', 'why'),
                card('⚠ 함정', '<ul><li>"호흡근은 폐에 직접 작용한다" ✗ — <b>흉강</b></li><li>"흉막내압이 대기압보다 높다" ✗</li><li>"표면활성제는 1형 세포가" ✗ — <b>2형</b></li></ul>', 'warn'))), 'Slides 3–17')

    page('PART 02', '호흡근 · 기도 저항 · 폐의 성질 · 환기',
        grid('1fr 1.05fr 1fr',
            col(card('🎯 호흡근 — "구분해야 됩니다"', tbl(['상황', '근육'], [['조용한 들숨', '<b>횡격막</b>(위아래) + <b>외늑간근</b>(옆·앞뒤) 수축'], ['깊은 들숨', '+ 목 근육(보조)'], ['조용한 날숨', '들숨근 <b>이완</b> + 탄력 반동 = <b>수동</b>'], ['능동 날숨', '<b>복근</b>(복압 ↑ → 횡격막 ↑) + <b>내늑간근</b>']]), 'warn'),
                card('기도 저항', '<b>F = ΔP / R</b>, R ∝ 1/r⁴ — 기도가 조절하는 건 <b>반지름</b>' + tbl(['', '수축', '확장'], [['신경', '<b>부교감</b>', '교감(효과 약함)'], ['호르몬', '—', '<b>에피네프린</b>'], ['국소', 'CO₂ ↓', 'CO₂ ↑'], ['병리', '히스타민·류코트리엔·점액', '—']]), 'tip')),
            col(card('정의 — 순응도 vs 탄력 반동', tbl(['', '순응도', '탄력 반동'], [['뜻', '압력 차를 따라 <b>잘 늘어남</b>', '<b>원래대로</b> 줄어듦'], ['원인', '표면활성제', '<b>폐포액 표면장력</b>(주요) + 탄성섬유'], ['언제', '들숨', '날숨']]) +
                    '<p style="margin-top:1.2mm"><b>표면활성제</b>(2형): 수소결합 ↓ → 표면장력 ↓ → <b>탄력 반동 ↓, 순응도 ↑</b> → 폐포 허탈 방지 · 부족 = <b>신생아 호흡곤란증후군</b> · 폐 섬유화 = 뻣뻣</p>', 'def'),
                img('c13-24', '폐용적 — TV 500 · RV 1200 · 조용한 호흡 2200 ↔ 2700 mL', '50mm')),
            col(card('🌬 폐환기 vs 폐포환기', '<b>폐환기 = TV × 호흡수</b> · <b>폐포환기 = (TV − 사강 150) × 호흡수</b>' + tbl(['패턴', '폐환기', '폐포환기'], [['500 × 12', '6000', '<b>4200</b>'], ['1200 × 5', '6000', '<b>5250</b>'], ['150 × 40', '6000', '<b>0</b>']]) +
                    '<p style="margin-top:1.2mm">→ <b>자주보다 깊게</b>. 폐포 사강 = <b>폐색전증</b>(환기 ○, 혈류 ✗)</p>', 'mint'),
                card('🎯 국소 조절 — "CO₂는 공기, O₂는 혈액"', tbl(['변화', '대상', '반응'], [['CO₂ ↑', '세기관지', '확장'], ['CO₂ ↓', '세기관지', '수축'], ['O₂ ↓', '폐세동맥', '<b>수축</b>'], ['O₂ ↑', '폐세동맥', '확장']]) +
                    '<p style="margin-top:1.2mm">체순환 세동맥은 O₂ ↓에 <b>확장</b> — 폐와 반대 · 정상 V/Q ≈ 0.8</p>', 'sum'))), 'Slides 18–29')

    page('PART 03', '가스 교환 · O₂ 운반 · CO₂ 운반',
        grid('1fr 1.1fr 1fr',
            col(card('정의 — 분압', '<b>P<sub>gas</sub> = 대기압 × 비율</b> — "분자 하나가 같은 압력" → <b>몰 농도가 중요</b><br>N₂ 79% → <b>600</b> · O₂ 21% → <b>160</b> · CO₂ → <b>0.23</b>', 'def'),
                card('📍 분압 지도', tbl(['위치', 'P<sub>O2</sub>', 'P<sub>CO2</sub>'], [['대기', '160', '0.23'], ['폐포', '<b>100</b>', '<b>40</b>'], ['동맥혈', '100', '40'], ['조직', '&lt;40', '&gt;46'], ['정맥혈', '<b>40</b>', '<b>46</b>']]) +
                    '<p style="margin-top:1.2mm">폐포 P<sub>O2</sub>가 160보다 낮은 이유: 수증기 <b>P<sub>H2O</sub> 47</b> + 사강·잔기량의 헌 공기와 섞임</p>', 'sum'),
                card('교환 속도 요인', tbl(['요인', '영향'], [['분압 차', '<b>가장 주된 결정 요인</b>'], ['표면적', '↑ 빠름 · 운동 중 ↑ · 폐기종 ↓'], ['두께', '↑ 느림 · 부종·섬유화·폐렴'], ['확산계수', '<b>CO₂ = O₂의 20배</b> → 기울기 6으로 충분']]), 'tip')),
            col(card('🔴 O₂ 운반 — 헤모글로빈', '용해 <b>1.5%</b> / Hb 결합 <b>98.5%</b> · Hb 1개 = 헴 4개 = <b>O₂ 4개</b> · 포화도의 주된 요인 = <b>P<sub>O2</sub></b>' +
                    tbl(['구간', '위치', '의미'], [['<b>평탄부</b>', '폐(≈60 이상)', 'P<sub>O2</sub>가 좀 떨어져도 잘 <b>싣는다</b>'], ['<b>급경사부</b>', '조직(40 이하)', '조금만 떨어져도 많이 <b>내려놓는다</b>']]) +
                    '<p style="margin-top:1.2mm">Hb = 폐에선 <b>저장고</b>(혈장 P<sub>O2</sub>를 낮게 유지해 기울기 유지), 조직에선 <b>빠른 방출</b></p>', 'mint'),
                img('c13-39', 'O₂–Hb 해리곡선: 평탄부(폐) · 급경사부(조직)', '58mm')),
            col(card('➡ 오른쪽 이동 = 방출 ↑', '<b>CO₂ ↑ · H⁺ ↑(pH ↓) · 온도 ↑ · 2,3-BPG ↑</b> → Hb–O₂ <b>친화력 ↓</b> · CO₂·pH에 의한 이동 = <b>보어 효과</b> · 2,3-BPG = 적혈구 해당과정, <b>고산지대</b>에서 ↑', 'why'),
                card('🫧 CO₂ 운반 세 가지', tbl(['형태', '%'], [['용해', '10'], ['카바미노 Hb(글로빈 아미노기)', '30'], ['<b>HCO₃⁻</b>(탄산탈수효소)', '<b>60</b>']]) +
                    '<p style="margin-top:1.2mm"><b>염소 이동</b>: HCO₃⁻가 나가고 Cl⁻가 들어옴(전기적 중성) · 폐에서는 반대</p>', 'tip'),
                img('c13-42', '조직: CO₂ → HCO₃⁻ · 폐: 역반응', '38mm'),
                card('CO(일산화탄소)', 'Hb 친화력이 매우 높아 O₂ 대신 결합 → <b>질식</b>', 'warn'))), 'Slides 31–44')

    page('PART 04', '호흡 조절 — 뇌간과 화학수용기',
        grid('1fr 1.05fr 1fr',
            col(card('정의 — 리듬은 뇌간에서', '심장은 SA 결절이 스스로 박동하지만, 호흡근(골격근)은 <b>스스로 활동전위 ✗</b> → 뇌간 호흡 중추의 <b>주기적 신경 신호</b>가 있어야 수축(분당 약 12회). 말할 때처럼 <b>수의적</b> 조절도 가능.', 'def'),
                img('c13-47', '교뇌·연수 호흡 중추', '70mm')),
            col(card('🧠 연수 · 교뇌', tbl(['구조', '위치', '역할'], [['<b>DRG</b>(등쪽호흡군)', '연수', '<b>들숨 뉴런</b> → 횡격막·외늑간근'], ['<b>VRG</b>(배쪽호흡군)', '연수', '들숨 + 날숨 뉴런'], ['<b>프리뵈트징거</b>', 'VRG 안', '<b>리듬 생성</b>(박동조율)'], ['호흡조절중추(pneumotaxic)', '교뇌', '들숨 뉴런 <b>끄기</b> → 들숨 짧게'], ['지속흡식중추(apneustic)', '교뇌', '들숨 뉴런이 <b>꺼지지 않게</b>']]), 'mint'),
                card('⚠️ 교수님 교과서 정정', '"<b>가장 중요한 거는 목 쪽에 있는 경동맥 소체</b>", 대동맥 소체는 보조 · "O₂가 주로 캐로티드 바디에서 측정" → 슬라이드 48의 "mainly by aortic body"는 <b>오류</b>', 'warn')),
            col(card('🎯 화학 요인 (표 13-8)', tbl(['요인', '말초(경동맥체)', '중추(연수)'], [['P<sub>O2</sub> ↓', '&lt;60일 때만(<b>비상</b>)', '오히려 억제'], ['<b>P<sub>CO2</sub> ↑</b>', '약하게', '<b>강하게 — 주된 조절</b>'], ['동맥 H⁺ ↑', '자극', '영향 없음(<b>BBB</b>)']]) +
                    '<p style="margin-top:1.2mm">CO₂는 BBB 통과 → 뇌 ECF에서 <b>H⁺</b>가 되어 중추 자극 · "CO₂가 많으면 호흡을 증가시켜라"</p>', 'sum'),
                card('결과', 'CO₂ ↑ · pH ↓ → 연수 → 횡격막·외늑간근 더 강하게 → <b>1회 호흡량 ↑</b>(횟수보다 효과적) → 동맥 CO₂ ↓(음성 되먹임)', 'why'),
                card('🎯 강의 끝 요약 문제(11/23)', '표면활성제 → <b>②</b>(표면장력 ↓, 허탈 방지) · 해리곡선 오른쪽 이동 → <b>③</b>(CO₂ ↑ → pH ↓ · H⁺ ↑) · CO → 질식', 'tip'))), 'Slides 46–49')

    qpage('PART 01–02', '해부 · 역학 · 호흡근 ①',
        MC('Which TWO statements about respiratory muscles and the respiratory cycle are correct? <b>(Choose two.)</b>', '호흡근과 호흡 주기에 대한 설명으로 옳은 것 두 개는?',
           [('During quiet inspiration, contraction of the diaphragm and the external intercostal muscles enlarges the thoracic cavity in vertical, lateral and front-to-back dimensions.', '조용한 들숨 동안 횡격막과 외늑간근이 수축해 흉강을 위아래, 옆, 앞뒤로 넓힌다.'),
            ('Quiet expiration is normally a passive process in which the inspiratory muscles relax and the lungs recoil because of their elasticity.', '조용한 날숨은 보통 들숨근이 이완하고 폐가 탄성으로 되돌아가는 수동적 과정이다.'),
            ('The internal intercostal muscles are the major inspiratory muscles, and their contraction raises the ribs upward and outward.', '내늑간근은 주 들숨근이며, 수축하면 갈비뼈를 위쪽과 바깥쪽으로 들어 올린다.'),
            ('The respiratory muscles act directly on the lungs to change lung volume, without changing the volume of the thoracic cavity.', '호흡근은 흉강 부피를 바꾸지 않고 폐에 직접 작용해 폐 부피를 바꾼다.'),
            ('During forced expiration, the abdominal muscles relax so that the diaphragm moves downward and the thoracic cavity becomes smaller.', '강제 날숨 동안 복근이 이완하여 횡격막이 아래로 내려가고 흉강이 작아진다.')], '①, ②',
           W('① ✔ 횡격막 = 위아래, 외늑간근 = 옆·앞뒤', '② ✔ 들숨근 이완 + 탄력 반동 = 수동', '③ ✗ <b>외늑간근</b>이 들숨근, 내늑간근은 갈비뼈를 <b>아래</b>로(날숨)', '④ ✗ 근육은 <b>흉강</b>에 작용, 폐는 따라감', '⑤ ✗ 복근은 <b>수축</b> → 복압 ↑ → 횡격막 <b>위로</b>'), pick=2, stars=2, prof=True),
        TF([('At rest between breaths, intra-alveolar pressure equals atmospheric pressure (760 mm Hg), while intrapleural pressure is about 756 mm Hg.', '숨 사이 휴식 시 폐포내압은 대기압(760 mmHg)과 같고, 흉막내압은 약 756 mmHg다.'),
            ('The transmural pressure gradient of about 4 mm Hg pushes outward on the lungs and keeps them stretched to fill the thoracic cavity.', '약 4 mmHg의 경벽압 기울기가 폐를 바깥으로 밀어 흉강을 채우도록 늘려 둔다.'),
            ('During inspiration, intra-alveolar pressure rises above atmospheric pressure, so air flows into the lungs.', '들숨 동안 폐포내압이 대기압보다 높아져 공기가 폐로 들어온다.'),
            ('Type I alveolar cells secrete pulmonary surfactant, while type II alveolar cells form the thin walls for gas exchange.', '1형 폐포세포는 폐 표면활성제를 분비하고, 2형 폐포세포는 가스 교환을 위한 얇은 벽을 이룬다.'),
            ('According to Boyle\'s law, at constant temperature the pressure of a gas is inversely proportional to its volume.', '보일의 법칙에 따르면 온도가 일정할 때 기체의 압력은 부피에 반비례한다.')],
           'T T F F T', W('(3) ✗ 들숨 때 폐포내압은 대기압보다 <b>낮다</b>(759)', '(4) ✗ 반대 — <b>2형</b>이 표면활성제, <b>1형</b>이 가스 교환'), stars=2), cols=2)

    qpage('PART 02', '폐의 성질 · 환기 ②',
        MC('Which TWO statements about lung compliance, surfactant and ventilation are correct? <b>(Choose two.)</b>', '폐 순응도, 표면활성제, 환기에 대한 설명으로 옳은 것 두 개는?',
           [('Pulmonary surfactant, secreted by type II alveolar cells, lowers alveolar surface tension, which reduces elastic recoil and increases compliance.', '2형 폐포세포가 분비하는 폐 표면활성제는 폐포 표면장력을 낮춰 탄력 반동을 줄이고 순응도를 높인다.'),
            ('Because of the anatomic dead space, increasing tidal volume raises alveolar ventilation more effectively than increasing respiratory rate.', '해부학적 사강 때문에 호흡수를 늘리는 것보다 1회 호흡량을 늘리는 것이 폐포환기를 더 효과적으로 높인다.'),
            ('The major factor causing the alveoli to collapse is the elastin fibers of the lung, while surface tension plays only a minor role.', '폐포를 쪼그라뜨리는 주요 요인은 폐의 엘라스틴 섬유이며, 표면장력은 작은 역할만 한다.'),
            ('Parasympathetic stimulation dilates the bronchioles strongly, so it is the main way the body increases airflow during exercise.', '부교감 자극은 세기관지를 강하게 확장시키므로, 운동 중 공기 흐름을 늘리는 주된 방법이다.'),
            ('A local decrease in O₂ dilates pulmonary arterioles, just as it dilates systemic arterioles, so more blood flows to poorly ventilated alveoli.', '국소 O₂ 감소는 체순환 세동맥처럼 폐세동맥도 확장시켜, 환기가 나쁜 폐포로 피가 더 흐르게 한다.')], '①, ②',
           W('① ✔ 표면활성제 → 탄력 반동 ↓ · 순응도 ↑', '② ✔ 사강 150 때문에 <b>깊게</b>', '③ ✗ 주요 요인은 <b>폐포액 표면장력</b>', '④ ✗ 부교감 = 기관지 <b>수축</b>', '⑤ ✗ 폐세동맥은 O₂ ↓에 <b>수축</b>(체순환과 반대)'), pick=2, stars=2),
        BOX('Fill in blanks (1)–(10) with the most appropriate words from the box. Not all words are used.', '상자에서 알맞은 단어를 골라 빈칸 (1)~(10)을 채우시오. 쓰지 않는 단어도 있다.',
            ['500', '150', '350', '1200', '4200', '5250', '0', 'tidal volume', 'respiratory rate', 'residual volume', 'vital capacity', 'pulmonary embolism'],
            'During quiet breathing, the <u>(1)</u> is about <u>(2)</u> mL, but about <u>(3)</u> mL of it remains in the conducting airways as anatomic dead space, so only <u>(4)</u> mL of fresh air reaches the alveoli. Even after maximal expiration, about <u>(5)</u> mL of air, the <u>(6)</u>, remains in the lungs. With 12 breaths per minute, alveolar ventilation is <u>(7)</u> mL/min; deep, slow breathing (1200 mL × 5) gives <u>(8)</u> mL/min, whereas shallow, rapid breathing (150 mL × 40) gives <u>(9)</u> mL/min. Alveoli that are ventilated but not perfused, as in <u>(10)</u>, form alveolar dead space.',
            ['tidal volume', '500', '150', '350', '1200', 'residual volume', '4200', '5250', '0', 'pulmonary embolism'],
            W('함정: <b>respiratory rate · vital capacity</b>(4500)는 안 씀', '(500 − 150) × 12 = 4200 · (1200 − 150) × 5 = 5250 · (150 − 150) × 40 = 0') + K('폐포환기 = (TV − 사강) × 호흡수', 'RV 1.2 L', '폐색전증 = 폐포 사강'), stars=3), cols=2)

    qpage('PART 03', '가스 교환 · 운반 ③',
        MC('Which TWO statements about gas exchange and gas transport are correct? <b>(Choose two.)</b>', '가스 교환과 가스 운반에 대한 설명으로 옳은 것 두 개는?',
           [('Alveolar P<sub>O2</sub> (about 100 mm Hg) is lower than atmospheric P<sub>O2</sub> (about 160 mm Hg) partly because inspired air is humidified and mixes with old air in the lungs.', '들이쉰 공기가 가습되고 폐 속 헌 공기와 섞이는 등의 이유로 폐포 P<sub>O2</sub>(약 100 mmHg)는 대기 P<sub>O2</sub>(약 160 mmHg)보다 낮다.'),
            ('Although the partial pressure gradient for CO₂ (about 6 mm Hg) is much smaller than that for O₂, similar amounts are exchanged because CO₂ has a much larger diffusion constant.', 'CO₂의 분압 기울기(약 6 mmHg)는 O₂보다 훨씬 작지만, CO₂의 확산상수가 훨씬 커서 비슷한 양이 교환된다.'),
            ('Most O₂ in the blood is physically dissolved in plasma, and only about 1.5% is bound to hemoglobin.', '혈중 O₂ 대부분은 혈장에 물리적으로 녹아 있고, 헤모글로빈과 결합한 것은 약 1.5%뿐이다.'),
            ('Increased CO₂, increased H⁺ and increased temperature shift the O₂–Hb dissociation curve to the left, increasing hemoglobin\'s affinity for O₂ in the tissues.', 'CO₂·H⁺·온도의 증가는 O₂–Hb 해리곡선을 왼쪽으로 이동시켜 조직에서 헤모글로빈의 O₂ 친화력을 높인다.'),
            ('Most CO₂ is carried in the blood bound to the iron of heme, after hemoglobin releases its O₂ in the tissues.', '혈중 CO₂ 대부분은 조직에서 헤모글로빈이 O₂를 내놓은 뒤 헴의 철에 결합해 운반된다.')], '①, ②',
           W('① ✔ 수증기 P<sub>H2O</sub> 47 + 헌 공기', '② ✔ 확산계수 CO₂ = O₂의 20배', '③ ✗ 반대 — 용해 <b>1.5%</b>, Hb <b>98.5%</b>', '④ ✗ <b>오른쪽</b> 이동, 친화력 <b>감소</b>(보어 효과)', '⑤ ✗ 대부분 <b>HCO₃⁻(60%)</b>, Hb에 붙는 30%도 <b>글로빈 아미노기</b>'), pick=2, stars=2),
        TF([('Venous blood returning to the lungs has a P<sub>O2</sub> of about 40 mm Hg and a P<sub>CO2</sub> of about 46 mm Hg.', '폐로 돌아오는 정맥혈은 P<sub>O2</sub> 약 40 mmHg, P<sub>CO2</sub> 약 46 mmHg다.'),
            ('In the plateau portion of the O₂–Hb curve, hemoglobin remains highly saturated even if alveolar P<sub>O2</sub> falls moderately, which favors O₂ loading in the lungs.', 'O₂–Hb 곡선의 평탄부에서는 폐포 P<sub>O2</sub>가 어느 정도 떨어져도 헤모글로빈이 높은 포화도를 유지해 폐에서 O₂ 싣기에 유리하다.'),
            ('In the steep portion of the curve, a small drop in tissue P<sub>O2</sub> causes hemoglobin to release a large amount of O₂.', '곡선의 급경사부에서는 조직 P<sub>O2</sub>가 조금만 떨어져도 헤모글로빈이 많은 O₂를 내놓는다.'),
            ('Thickening of the alveolar–capillary membrane, as in pulmonary fibrosis or pneumonia, increases the rate of gas transfer.', '폐 섬유화나 폐렴에서처럼 폐포–모세혈관 막이 두꺼워지면 가스 이동 속도가 증가한다.'),
            ('Carbon monoxide binds hemoglobin with very high affinity, so it prevents O₂ transport and can cause suffocation.', '일산화탄소는 헤모글로빈에 매우 높은 친화력으로 결합해 O₂ 운반을 막아 질식을 일으킬 수 있다.')],
           'T T T F T', W('(4) ✗ 두께 ↑ → 이동 속도 <b>↓</b>', '(5) 교수님 요약 문제(11/23)'), stars=2), cols=2)

    qpage('PART 04', '호흡 조절 ④',
        FQ('c13-47-q', 'The figure shows the respiratory control centers in the brain stem. Identify the structures labeled <b>A</b> to <b>E</b>.', '그림은 뇌간의 호흡 조절 중추다. A~E의 이름을 쓰시오.',
           [('A', '호흡조절중추 Pneumotaxic center'), ('B', '지속흡식중추 Apneustic center'), ('C', '프리뵈트징거 복합체 Pre-Bötzinger complex'), ('D', '등쪽호흡군 DRG'), ('E', '배쪽호흡군 VRG')],
           W('A·B = <b>교뇌</b>(연수를 미세조정) · C·D·E = <b>연수</b>', 'A는 들숨 뉴런을 <b>끄고</b>, B는 <b>꺼지지 않게</b> · C = <b>리듬 생성</b>(VRG 안)') + K('pneumotaxic = 끄기', 'apneustic = 유지', '프리뵈트징거 = 리듬'), stars=2, h='52mm'),
        MC('Which TWO statements about the chemical control of ventilation are correct? <b>(Choose two.)</b>', '환기의 화학적 조절에 대한 설명으로 옳은 것 두 개는?',
           [('An increase in arterial P<sub>CO2</sub> is the most important input regulating the magnitude of ventilation, acting mainly through the central chemoreceptors.', '동맥 P<sub>CO2</sub> 증가는 환기량을 조절하는 가장 중요한 입력이며, 주로 중추 화학수용기를 통해 작용한다.'),
            ('Among the peripheral chemoreceptors, the carotid bodies in the neck play the most important role, including sensing arterial P<sub>O2</sub>.', '말초 화학수용기 중 목에 있는 경동맥체가 동맥 P<sub>O2</sub> 감지를 포함해 가장 중요한 역할을 한다.'),
            ('A fall in arterial P<sub>O2</sub> strongly stimulates ventilation at all times and is the main driver of breathing during normal exercise.', '동맥 P<sub>O2</sub> 저하는 항상 환기를 강하게 자극하며, 평상시 운동 중 호흡을 이끄는 주된 요인이다.'),
            ('Arterial H⁺ crosses the blood–brain barrier easily and directly stimulates the central chemoreceptors in the medulla.', '동맥혈의 H⁺는 혈뇌장벽을 쉽게 통과해 연수의 중추 화학수용기를 직접 자극한다.'),
            ('Like cardiac muscle, the respiratory muscles have their own pacemaker activity and continue to contract rhythmically without neural input.', '심장근처럼 호흡근도 자체 박동조율 활동이 있어 신경 입력 없이도 리듬 있게 계속 수축한다.')], '①, ②',
           W('① ✔ P<sub>CO2</sub>가 주된 조절(중추 → 뇌 ECF H⁺)', '② ✔ <b>교수님 정정</b>: 경동맥체가 가장 중요(슬라이드의 aortic body는 오류)', '③ ✗ P<sub>O2</sub> ↓는 &lt;60일 때만 — <b>비상</b> 기전', '④ ✗ 동맥 H⁺는 <b>BBB 통과 ✗</b> → 말초만', '⑤ ✗ 호흡근은 <b>뇌간의 주기적 신경 신호</b>가 필요'), pick=2, stars=3, prof=True), cols=2)

    qpage('PART 01–04', '서술형',
        ES('Explain how air flows into and out of the lungs during quiet breathing, using the roles of the respiratory muscles, the transmural pressure gradient and Boyle\'s law, and state how forced expiration differs.', '조용한 호흡에서 공기가 폐로 드나드는 과정을 호흡근, 경벽압 기울기, 보일의 법칙을 이용해 설명하고, 강제 날숨은 어떻게 다른지 쓰시오.',
           '폐에는 근육이 없어 호흡근은 <b>흉강</b>의 부피를 바꾼다. 들숨 때 <b>횡격막</b>이 수축해 내려가고 <b>외늑간근</b>이 갈비뼈를 들어 올려 흉강이 커지면 흉막내압이 756 → 754 mmHg로 떨어지고, 흉막내압이 늘 폐포내압보다 낮은 <b>경벽압 기울기(약 4 mmHg)</b> 때문에 폐가 따라 늘어난다. 부피가 커지면 <b>보일의 법칙(P₁V₁ = P₂V₂)</b>에 따라 폐포내압이 759 mmHg로 대기압보다 낮아져 공기가 들어온다(순응도). 조용한 날숨은 들숨근이 <b>이완</b>하고 폐와 흉벽이 <b>탄력 반동</b>으로 되돌아가 폐포내압이 761 mmHg로 높아지는 <b>수동</b> 과정이다. 강제 날숨에서는 <b>복근</b>이 수축해 복압을 올려 횡격막을 더 위로 밀고 <b>내늑간근</b>이 갈비뼈를 끌어내려 흉강을 더 줄이는 <b>능동</b> 과정이 된다.',
           K('흉강 ↑ → 흉막내압 ↓ → 폐 ↑', '경벽압 4', 'P₁V₁ = P₂V₂', '759 / 761', '복근 + 내늑간근'), stars=3),
        ES('Describe the forms in which O₂ and CO₂ are transported in the blood, and explain the physiological significance of the plateau and steep portions of the O₂–Hb dissociation curve and of a right shift.', '혈액에서 O₂와 CO₂가 운반되는 형태를 쓰고, O₂–Hb 해리곡선의 평탄부·급경사부와 오른쪽 이동의 생리적 의미를 설명하시오.',
           'O₂는 혈장에 녹은 것이 <b>1.5%</b>뿐이고 <b>98.5%</b>가 헤모글로빈(헴 4개, O₂ 4분자)에 결합해 운반되며, 포화도는 주로 <b>P<sub>O2</sub></b>가 정한다. 곡선의 <b>평탄부</b>에서는 폐포 P<sub>O2</sub>가 다소 떨어져도 포화도가 높게 유지되어 폐에서 O₂를 잘 <b>싣고</b>, <b>급경사부</b>에서는 조직 P<sub>O2</sub>가 조금만 떨어져도 많은 O₂를 <b>내려놓는다</b>. 활동 조직의 <b>CO₂ ↑, H⁺ ↑(pH ↓), 온도 ↑, 2,3-BPG ↑</b>는 곡선을 <b>오른쪽</b>으로 옮겨 Hb의 O₂ 친화력을 낮추고 방출을 늘린다(CO₂·pH에 의한 것 = <b>보어 효과</b>). CO₂는 <b>용해 10%</b>, <b>카바미노헤모글로빈 30%</b>, <b>HCO₃⁻ 60%</b>로 운반되며, 적혈구의 <b>탄산탈수효소</b>가 CO₂를 HCO₃⁻로 바꾸고 HCO₃⁻는 Cl⁻와 교환되어 혈장으로 나간다(<b>염소 이동</b>). 폐에서는 이 반응이 거꾸로 일어나 CO₂가 내쉬어진다.',
           K('1.5 / 98.5%', '평탄부 = 싣기, 급경사부 = 내리기', 'CO₂·H⁺·온도·2,3-BPG → 오른쪽', '10 / 30 / 60%', '염소 이동'), stars=3), cols=2)

    memo([('🫁 해부·역학', '외늑간근 = <b>들숨</b> · 내늑간근 = <b>날숨</b><br>주 들숨근 = 횡격막 + 외늑간근<br>760 / 756 · 경벽압 <b>4</b><br>들숨 759 · 날숨 761<br>2형 세포 = 표면활성제'),
          ('🌬 폐의 성질·환기', '표면활성제 → 탄력 반동 ↓ · 순응도 ↑<br>탄력 반동 주요인 = <b>표면장력</b><br>TV 500 · RV 1.2 L · 사강 150<br>폐포환기 = (TV − 150) × 호흡수<br>CO₂ → 세기관지 · O₂ → 폐세동맥'),
          ('🔴 교환·운반', '160 → 폐포 100 · 정맥혈 40/46<br>확산계수 CO₂ = O₂의 20배<br>O₂: 용해 1.5 · Hb 98.5%<br>오른쪽 이동 = CO₂·H⁺·온도·2,3-BPG ↑<br>CO₂: 10 · 30 · <b>60%(HCO₃⁻)</b>'),
          ('🧠 조절', 'DRG 들숨 · VRG 들숨+날숨<br>프리뵈트징거 = <b>리듬</b><br>pneumotaxic 끄기 · apneustic 유지<br>⚠️ 말초 = <b>경동맥체</b>가 가장 중요<br>주된 조절 = 동맥 <b>P<sub>CO2</sub></b>')],
         '<ol><li>근육은 폐가 아니라 <b>흉강</b>에 작용</li><li>오른쪽 이동 = 친화력 <b>감소</b>, 방출 증가</li><li>⚠️ 슬라이드 48 "aortic body" ✗ → <b>경동맥체</b>(교수님 정정)</li></ol>',
         ['흉막내압이 늘 폐포내압보다 낮아 생기는 경벽압 기울기가 폐를 흉강에 맞춰 늘려 두고, 근육이 흉강 부피를 바꾸면 보일의 법칙으로 폐포내압이 변해 공기가 드나든다.',
          'O₂는 대부분 헤모글로빈에 결합해, CO₂는 대부분 적혈구의 탄산탈수효소가 만든 중탄산 이온으로 운반된다.',
          '환기량을 가장 주요하게 조절하는 입력은 동맥 P<sub>CO2</sub> 증가이며, 말초 화학수용기 중에서는 경동맥체가 가장 중요하다.'])
