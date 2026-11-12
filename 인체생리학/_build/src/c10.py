from lib import *

def build():
    chapter(10, 'Blood Vessels & Blood Pressure')
    c = CH['color']
    page('CHAPTER 10', 'Blood Vessels & Blood Pressure — 한 장 지도',
        chev([('10.1 흐름의 물리', 'F = ΔP/R', '#0b7285'), ('10.2 동맥', '압력 저장소', c), ('10.3 세동맥', '저항·TPR', '#1098ad'),
              ('10.4 모세혈관', '교환·림프', '#15aabf'), ('10.5 정맥', '저장소·환류', '#3bc9db'), ('10.6 혈압', 'MAP = CO × TPR', '#0b5e6b')]) +
        grid('1.05fr 1fr',
            card('한 줄 요약', '피는 <b>압력 차</b>를 따라 흐르고(F = ΔP/R), 저항은 <span class="hy">반지름의 4제곱에 반비례</span>한다. 동맥은 탄성 반동으로 <b>압력을 저장</b>하고, 평활근이 많은 <b>세동맥</b>이 반지름을 바꿔 <b>CO를 분배</b>(국소 조절)하고 <b>혈압을 조절</b>(교감 α, 외인성)한다. 모세혈관은 <b>교환</b>, 정맥은 <b>혈액 저장소(64%)</b>. 모두 합치면 <span class="hp">MAP = CO × TPR</span>.', 'sum big'),
            col(card('🎯 교수님 강조 (11/12 녹취)', '<ol><li>MAP 결정 요인 총정리 그림은 <b>"그림을 주고 해석하라"</b>고 낼 것 같다</li><li>구체적인 것보다 <b>기본 원리</b> 위주</li><li>저항 조절은 <b>반지름</b> — 점성은 느리고 길이는 고정</li><li>세동맥에는 <b>부교감 없음</b> — 확장은 교감 ↓ + NO</li><li>유량은 어디서나 같고 <b>유속</b>만 모세혈관에서 느림</li></ol>', 'warn'),
                card('💡 숫자', '세동맥 <b>50만</b> · 모세혈관 <b>100억</b> · 세포는 모세혈관 <b>0.1 mm</b> 이내 · ECF = 간질액 <b>80</b> + 혈장 <b>20</b>% · 림프 <b>20 − 17 = 3 L/일</b> · 정맥 <b>64%</b> · MAP <b>~93 mmHg</b>(이완기 2/3) · 정맥 진입 <b>17</b> → 심방 <b>0 mmHg</b> · r ½ → R <b>16배</b>', 'tip'))), 'Slides 1–36')

    page('PART 01', '흐름의 물리 · 혈관 4종 · 동맥과 MAP',
        grid('1fr 1.1fr 1fr',
            col(card('정의 — 흐름의 공식', '<span style="font-size:11pt"><b>F = ΔP / R</b> · <b>R ∝ ηL / r⁴</b></span><br>푸아죄유: <b>Q = πΔPr⁴ / 8ηL</b>', 'def'),
                card('📐 무엇이 흐름을 정하나', '<ul><li>ΔP = 처음과 끝의 압력 <b>차이</b> — 절대값 ✗ (90→10과 180→100은 같은 흐름)</li><li>점성 η: 적혈구 수 — 바꾸는 데 <b>오래 걸림</b></li><li>길이 L: <b>고정</b></li><li><span class="hy">반지름 r: 평활근으로 계속 조절 → 주 결정 요인</span></li><li>r × 2 → R 1/16 → F 16배 / r × ½ → R 16배</li></ul>', 'tip'),
                img('c10-07', 'Flow ∝ ΔP: 절대 압력이 달라도 ΔP가 같으면 흐름도 같다', '44mm')),
            col(card('🆚 혈관 4종', tbl(['', '동맥', '세동맥', '모세혈관', '정맥'], [
                    ['개수', '수백', '50만', '<b>100억</b>', '수백'], ['벽', '<b>탄성</b>(엘라스틴)', '<b>평활근</b>, 교감', '<b>내피 1층</b>', '잘 늘어남, 판막'],
                    ['역할', '<b>압력 저장소</b>', '<b>주 저항</b>', '<b>교환</b>', '<b>혈액 저장소</b>']])),
                img('c10-11', '혈관 비교표와 벽의 층 두께', '74mm')),
            col(card('🎈 동맥 — 압력 저장소', '수축기에 늘어났다가 이완기에 <b>탄성 반동</b> → 모세혈관 흐름이 <b>끊기지 않음</b><br>콜라겐 = 인장 강도, 엘라스틴 = 탄성', 'mint'),
                card('📊 평균 동맥압 (MAP)', '주기 내내 피를 미는 평균 압력 = 혈류의 원동력<br>이완기가 <b>2/3</b> → <b>이완기압 쪽</b>: 이완기압 + ⅓ 맥압 ≈ 93 mmHg<br>압력이 가장 크게 떨어지는 곳 = <b>세동맥</b>'),
                img('c10-13', '혈관별 압력: 세동맥에서 크게 떨어지고 진동이 사라짐', '46mm'))), 'Slides 3–13')

    page('PART 02', '세동맥 — 국소 조절(분배) vs 외인성 조절(혈압)',
        grid('1fr 1.1fr 1fr',
            col(card('정의', '세동맥 = <b>주 저항 혈관</b>(모세혈관 ✗). 평활근 + <b>교감신경</b>, <span class="hp">부교감 없음</span><br>두 임무: ① 기관별 <b>CO 분배</b> ② <b>혈압</b> 조절', 'def'),
                img('c10-16', '(b) 정상 긴장도 (c) 수축 원인 (d) 확장 원인', '92mm')),
            col(card('🆚 수축 vs 확장', tbl(['수축 (저항 ↑ 혈류 ↓)', '확장 (저항 ↓ 혈류 ↑)'], [
                    ['O₂ ↑, CO₂·대사물 ↓', '<b>O₂ ↓, CO₂·K⁺·산·삼투압 ↑, 아데노신</b>'], ['교감 ↑ (NE → α)', '교감 ↓'],
                    ['바소프레신, 안지오텐신 II, 엔도텔린', '<b>NO</b>(전단응력), <b>히스타민</b>'], ['근원성 반응(늘어나면)', '—'], ['추위', '열']]), 'tip'),
                card('🏠 국소(내인성) 조절 = 분배', '<ul><li>대사 변화 → 일하는 조직에 피를 더</li><li><b>근원성 반응</b>: 늘어나면 스스로 수축 → 혈류 일정 = <b>자동조절</b></li><li><b>전단응력</b> → 내피 <b>NO</b> → 확장</li><li>히스타민(비만세포), 열·냉</li></ul>', 'mint')),
            col(card('🧠 외인성 조절 = 혈압', '<ul><li>교감 <b>NE → α₁</b> → 수축 → <b>TPR ↑</b></li><li><span class="hy"><b>MAP = CO × TPR</b></span></li><li>확장은 교감 ↓ + NO</li><li><b>연수 심혈관 조절 중추</b> → HR·수축력·세동맥</li><li>호르몬: <b>E·NE</b>(부신수질), <b>바소프레신</b>(뇌하수체 후엽), <b>안지오텐신 II</b>(폐 내피에서 전환) — 물·염분 보존 + 혈관수축</li></ul>', 'warn'),
                img('c10-21', 'TPR = 세동맥 반지름(국소·외인성) + 점성(적혈구 수)', '74mm'))), 'Slides 14–21')

    page('PART 03', '모세혈관 · 간질액 · 림프계',
        grid('1fr 1fr 1fr',
            col(card('정의 — 교환의 장소', '확산에 최적: <b>거리</b> 짧음(내피 1층, 세포는 0.1 mm 이내) · <b>면적</b> 넓음(100억 개) · <b>시간</b> 충분(가장 느림)<br>O₂·CO₂ = 막 직접 · 작은 수용성 = <b>물로 찬 구멍</b> · 큰 혈장 단백질 = 못 지남 → 삼투압', 'def'),
                card('⚖ 유량 vs 유속', '<b>유량(mL/분)은 어디서나 같다 = CO</b><br><b>유속은 총 단면적에 반비례</b> → 모세혈관에서 가장 느림', 'tip'),
                img('c10-24', '유량 일정 · 총 단면적 최대 · 유속 최소 (모세혈관)', '60mm')),
            col(card('🚪 모세혈관 앞 괄약근', '휴식 시 대부분 닫힘, 대사 ↑ → 열림. 괄약근 = <b>문지기</b>(모세혈관 자체에는 평활근 없음) · 후세동맥 = 세동맥–모세혈관 잇는 짧은 혈관'),
                img('c10-25', '(a) 연속 모세혈관 (b) 괄약근 이완 (c) 수축', '36mm'),
                card('💧 간질액', 'ECF = <b>간질액 80% + 혈장 20%</b> — 세포가 닿는 진짜 내부 환경<br>혈장↔간질액 = 주로 <b>수동</b>(확산) · 간질액↔세포 = 수동 + 능동<br>각 용질은 <b>자기 농도 기울기대로</b> 독립적', 'mint')),
            col(card('🟢 림프계', '<ul><li>여과 <b>20</b> − 재흡수 <b>17</b> = <b>3 L/일</b> → 림프</li><li>초기 림프관: 투과성 ↑, 내피가 겹쳐 <b>한 방향</b></li><li>→ 림프관(판막) → <b>림프절</b>(필터·면역) → 정맥</li><li>기능: 액체 회수 · 방어 · <b>지방 운반</b> · 단백질 회수</li><li>막히면 <b>부종</b></li></ul>', 'why'),
                img('c10-28', '림프계와 순환계 · 하루 20 / 17 / 3 L', '74mm'))), 'Slides 22–28')

    page('PART 04', '정맥 · 정맥 환류 · 혈압 총정리',
        grid('1fr 1.15fr 1fr',
            col(card('정의 — 정맥 = 혈액 저장소', '팽창성 ↑ → 피의 <b>64%</b>가 체정맥 (동맥은 <b>압력</b> 저장소)<br>정맥 용량 ↑ → 유효 순환 혈액량 ↓ → 환류 ↓', 'def'),
                img('c10-30', '휴식 시 혈액 분포: 체정맥 64%', '44mm'),
                card('🔁 정맥 환류', '1분에 정맥에서 <b>각 심방</b>으로 들어오는 양 → EDV → SV → CO (9장 프랭크-스탈링)<br>내인성: 정맥 진입 <b>17</b> vs 심방 <b>0 mmHg</b>', 'tip')),
            col(card('➕ 환류를 늘리는 외인성 5요인', '<ol><li><b>교감</b> → 정맥 수축 → 용량 ↓</li><li><b>골격근 펌프</b> — 근육이 정맥을 짬</li><li><b>정맥 판막</b> — 역류 방지 (②와 한 세트)</li><li><b>호흡 펌프</b> — 흉강 음압</li><li><b>심장 흡인</b> — 이완기 심실 압력 ↓</li></ol>+ 혈액량 자체 ↑(물 재흡수)', 'mint'),
                img('c10-32', '정맥 환류 요인 · 골격근 펌프와 정맥 판막', '56mm')),
            col(card('🧭 MAP = CO × TPR — 총정리', tbl(['신경', '표적 → 결과'], [['부교감', '<b>심장만</b> → HR ↓ → CO ↓'], ['교감', '심장(HR·수축력 ↑) · <b>세동맥</b> 수축(TPR ↑) · <b>정맥</b> 수축(환류 ↑ → SV ↑)']]) +
                    '<p style="margin-top:1.4mm">① CO 요인 + ② TPR 요인 + ③ 정맥 환류(→ SV) = 전체 지도</p>', 'warn'),
                img('c10-36', '평균 동맥압 결정 요인 전체 지도 — "주고 해석하라" 후보', '74mm'))), 'Slides 29–36')

    qpage('PART 01–02', '흐름 · 세동맥 ①',
        FQ('c10-34-q', 'The figure shows how autonomic stimulation changes blood pressure. Fill in boxes <b>A</b> to <b>E</b>.', '그림은 자율신경 자극이 혈압을 바꾸는 경로다. A~E 칸을 채우시오.',
           [('A', '↓ 심박수 Heart rate'), ('B', '↑ 심장 수축 강도 Contractile strength'), ('C', '↑ 혈관 수축 Vasoconstriction (세동맥)'), ('D', '↑ 총말초저항 TPR'), ('E', '↑ 정맥 환류 Venous return')],
           W('부교감은 <b>심장만</b>(HR ↓ → CO ↓). 교감은 세 갈래: 심장(HR·수축력 → SV) · 세동맥(수축 → TPR) · 정맥(수축 → 환류 → SV → CO)', 'MAP = CO × TPR — 교수님이 "그림 주고 해석" 예고한 계열') + K('부교감 = HR만', '세동맥 → TPR', '정맥 → 환류 → SV'), stars=3, h='44mm'),
        TF([('Doubling the radius of an arteriole decreases its resistance to one-sixteenth and, at the same pressure gradient, increases flow sixteenfold.', '세동맥 반지름이 2배가 되면 저항은 16분의 1로 줄고, 같은 압력 기울기에서 흐름은 16배가 된다.'),
            ('Blood flow through a vessel depends on the absolute pressure at its beginning, so a vessel with 180 mmHg at its start always carries more blood than one with 90 mmHg.', '혈관의 흐름은 시작점의 절대 압력에 달려 있어서, 시작점이 180 mmHg인 혈관이 90 mmHg인 혈관보다 항상 피를 더 많이 나른다.'),
            ('Arteries act as a pressure reservoir, because elastic recoil of their walls keeps blood flowing through the capillaries during diastole.', '동맥은 압력 저장소 역할을 하며, 벽의 탄성 반동이 이완기에도 모세혈관 흐름을 유지한다.'),
            ('Arterioles receive both sympathetic and parasympathetic innervation, and parasympathetic stimulation is the main cause of vasodilation.', '세동맥은 교감·부교감 지배를 모두 받으며, 부교감 자극이 혈관 확장의 주된 원인이다.'),
            ('In the myogenic response, stretch of the arteriolar wall causes the smooth muscle to contract, keeping organ blood flow relatively constant.', '근원성 반응에서는 세동맥 벽이 늘어나면 평활근이 수축해 장기 혈류를 비교적 일정하게 유지한다.')],
           'T F T F T', W('(2) ✗ 흐름은 압력의 <b>차이(ΔP)</b>에 비례 — 180→100과 90→10은 ΔP가 같아 흐름도 같다', '(4) ✗ 세동맥에는 <b>부교감 지배가 없다</b> — 확장은 교감 ↓ + NO'), stars=2), cols=2)

    qpage('PART 02–03', '세동맥 · 모세혈관 ②',
        MC('Which TWO local changes would cause arterioles in an actively working tissue to dilate? <b>(Choose two.)</b>', '활발히 일하는 조직의 세동맥을 확장시키는 국소 변화 두 개는?',
           [('A decrease in local O₂ together with an increase in CO₂, H⁺, K⁺ and other metabolites produced by the active cells.', '활동 중인 세포가 만든 CO₂·H⁺·K⁺ 등 대사물의 증가와 함께 국소 O₂가 감소하는 것'),
            ('Increased shear stress on the endothelium, which causes endothelial cells to release nitric oxide.', '내피에 가해지는 전단응력이 늘어 내피세포가 산화질소를 방출하는 것'),
            ('Increased sympathetic release of norepinephrine acting on α₁-adrenergic receptors of the arteriolar smooth muscle.', '세동맥 평활근의 α₁ 수용체에 작용하는 교감 노르에피네프린 방출 증가'),
            ('Increased secretion of vasopressin and angiotensin II to conserve salt and water.', '염분과 물을 보존하기 위한 바소프레신·안지오텐신 II 분비 증가'),
            ('Stretch of the arteriolar wall by a sudden rise in arterial pressure, which triggers a myogenic response.', '동맥압이 갑자기 올라 세동맥 벽이 늘어나 근원성 반응이 일어나는 것')], '①, ②',
           W('① ✔ 대사 변화 → 확장 (능동 충혈)', '② ✔ 전단응력 → NO → 확장', '③ ✗ 교감 α₁ → <b>수축</b>', '④ ✗ 바소프레신·안지오텐신 II = <b>혈관수축제</b>', '⑤ ✗ 근원성 반응 → <b>수축</b>'), pick=2, stars=2),
        MC('Which TWO statements about capillaries and the lymphatic system are correct? <b>(Choose two.)</b>', '모세혈관과 림프계에 대한 설명으로 옳은 것 두 개는?',
           [('The flow rate is the same at every level of the circulation, but flow velocity is slowest in the capillaries because their total cross-sectional area is greatest.', '유량은 순환의 모든 단계에서 같지만, 모세혈관은 총 단면적이 가장 커서 유속이 가장 느리다.'),
            ('Slightly more fluid is filtered out of the capillaries than is reabsorbed, and the excess is returned to the blood by the lymphatic system.', '모세혈관에서 여과되는 액체가 재흡수되는 양보다 약간 많고, 남는 액체는 림프계가 혈액으로 돌려보낸다.'),
            ('Capillaries are the major resistance vessels, and their smooth muscle walls constrict in response to sympathetic stimulation.', '모세혈관은 주 저항 혈관이며, 평활근 벽이 교감 자극에 반응해 수축한다.'),
            ('Plasma proteins such as albumin pass freely through capillary pores, so they make no contribution to plasma osmotic pressure.', '알부민 같은 혈장 단백질은 모세혈관 구멍을 자유롭게 지나므로 혈장 삼투압에 기여하지 않는다.'),
            ('Exchange between plasma and interstitial fluid occurs mainly by ATP-dependent active transport across the capillary wall.', '혈장과 간질액 사이 교환은 주로 모세혈관 벽을 건너는 ATP 의존 능동수송으로 일어난다.')], '①, ②',
           W('① ✔ 유량 = CO, 유속 ∝ 1/총 단면적', '② ✔ 20 − 17 = 3 L/일 → 림프', '③ ✗ 주 저항 = <b>세동맥</b>, 모세혈관엔 평활근이 <b>없다</b>', '④ ✗ 큰 단백질은 구멍을 <b>못 지나</b> → 삼투압 유지', '⑤ ✗ 주로 <b>수동</b>(확산)'), pick=2, stars=2), cols=2)

    qpage('PART 04', '정맥 · 혈압 ③',
        BOX('Fill in blanks (1)–(10) with the most appropriate words from the box. Not all words are used.', '상자에서 알맞은 단어를 골라 빈칸 (1)~(10)을 채우시오. 쓰지 않는 단어도 있다.',
            ['cardiac output', 'total peripheral resistance', 'arterioles', 'α₁-adrenergic', 'parasympathetic', 'venous return', 'skeletal muscle pump', 'venous valves', 'respiratory pump', 'cardiac suction', 'capillaries', 'β₂'],
            'Mean arterial pressure equals <u>(1)</u> multiplied by <u>(2)</u>. Sympathetic norepinephrine acts on <u>(3)</u> receptors to constrict the <u>(4)</u>, the major resistance vessels; there is no <u>(5)</u> innervation of these vessels. Veins act as a blood reservoir, and the volume entering the atria each minute is called <u>(6)</u>. It is increased by sympathetic venoconstriction, by the <u>(7)</u>, which squeezes veins during muscle contraction, by <u>(8)</u>, which prevent backflow, by the <u>(9)</u>, which lowers thoracic pressure, and by <u>(10)</u> during ventricular relaxation.',
            ['cardiac output', 'total peripheral resistance', 'α₁-adrenergic', 'arterioles', 'parasympathetic', 'venous return', 'skeletal muscle pump', 'venous valves', 'respiratory pump', 'cardiac suction'],
            W('함정: <b>capillaries</b>는 교환 혈관(저항 ✗), <b>β₂</b>는 수축이 아니라 이완 쪽 수용체') + K('MAP = CO × TPR', 'α₁ → 세동맥', '정맥 환류 5요인'), stars=3),
        TF([('Veins contain about 64% of the blood volume at rest, so they serve as a blood reservoir that can be mobilized by venoconstriction.', '휴식 시 정맥에는 혈액의 약 64%가 있어, 정맥 수축으로 동원할 수 있는 혈액 저장소 역할을 한다.'),
            ('An increase in venous capacity increases venous return, because more blood is stored in the veins.', '정맥 용량이 늘면 정맥에 피가 더 저장되므로 정맥 환류가 증가한다.'),
            ('Because about two-thirds of the cardiac cycle is spent in diastole, mean arterial pressure is closer to diastolic than to systolic pressure.', '심장 주기의 약 3분의 2가 이완기이므로 평균 동맥압은 수축기압보다 이완기압에 더 가깝다.'),
            ('Parasympathetic stimulation lowers blood pressure mainly by dilating arterioles throughout the body.', '부교감 자극은 주로 온몸의 세동맥을 확장시켜 혈압을 낮춘다.'),
            ('Blood viscosity is rarely used for rapid control of blood pressure, because changing the number of red blood cells takes a long time.', '적혈구 수를 바꾸는 데 오래 걸리므로 혈액 점성은 혈압의 빠른 조절에 거의 쓰이지 않는다.')],
           'T F T F T', W('(2) ✗ 정맥 용량 ↑ → 정맥에 고이는 피 ↑ → 환류 <b>↓</b>', '(4) ✗ 부교감은 <b>심장(HR)</b>에만 작용 — 세동맥엔 부교감 지배가 없다'), stars=2), cols=2)

    qpage('PART 01–04', '서술형',
        ES('Explain why the arteriolar radius is the major determinant of vascular resistance, and describe how intrinsic and extrinsic control of arteriolar radius serve different purposes.', '세동맥 반지름이 혈관 저항의 주된 결정 요인인 이유를 설명하고, 세동맥 반지름의 내인성·외인성 조절이 어떤 목적을 가지는지 서술하시오.',
           '저항은 R ∝ ηL/r⁴로 점성·길이에 비례하고 반지름의 <b>4제곱에 반비례</b>한다. 점성은 적혈구 수를 바꿔야 해 오래 걸리고, 길이는 해부학적으로 고정이라 실제로 바뀌는 것은 반지름뿐이다. 반지름이 반으로 줄면 저항은 <b>16배</b>가 되어 작은 변화로 큰 효과를 낸다. 반지름을 바꾸는 평활근이 풍부한 곳이 <b>세동맥</b>이다. <b>내인성(국소) 조절</b>은 O₂ ↓·CO₂·대사물 ↑, NO, 히스타민(확장)과 근원성 반응(수축)으로 각 장기의 필요에 맞게 <b>CO를 분배</b>한다. <b>외인성 조절</b>은 교감 NE가 α₁ 수용체를 통해 세동맥을 수축시켜 <b>TPR</b>을 올리는 것으로, MAP = CO × TPR이므로 <b>전신 혈압</b>을 조절한다(부교감 지배는 없음, E·NE·바소프레신·안지오텐신 II도 수축).',
           K('R ∝ ηL/r⁴', '반지름 ½ → 16배', '국소 = 분배', '외인성 = 혈압', 'MAP = CO × TPR'), stars=3),
        ES('List the factors that increase venous return and explain how venous return affects mean arterial pressure.', '정맥 환류를 늘리는 요인을 나열하고, 정맥 환류가 평균 동맥압에 어떤 영향을 주는지 설명하시오.',
           '정맥 환류는 1분에 정맥에서 각 심방으로 들어오는 혈액량이다. 기본 동력은 정맥 진입부(약 17 mmHg)와 심방(약 0 mmHg)의 작은 압력 기울기이고, 이를 돕는 외인성 요인은 ① <b>교감신경</b>에 의한 정맥 수축(정맥 용량 ↓) ② <b>골격근 펌프</b> ③ 역류를 막는 <b>정맥 판막</b> ④ 흉강 압력을 낮추는 <b>호흡 펌프</b> ⑤ 이완기 심실 압력이 떨어져 생기는 <b>심장 흡인</b>이며, 혈액량 자체가 늘어도 환류가 늘어난다. 환류가 늘면 EDV가 커져 <b>프랭크-스탈링 법칙</b>으로 1회 박출량이 증가하고, CO = HR × SV가 커지므로 <b>MAP = CO × TPR</b>도 올라간다.',
           K('교감 · 골격근 펌프 · 판막 · 호흡 · 심장 흡인', 'EDV ↑ → SV ↑', 'CO ↑ → MAP ↑'), stars=3), cols=2)

    memo([('📐 물리', 'F = ΔP/R (<b>차이</b>)<br>R ∝ ηL/r⁴ → <b>반지름</b><br>r ½ → R 16배<br>Q = πΔPr⁴/8ηL'),
          ('🩸 혈관', '동맥 = <b>압력</b> 저장소(탄성 반동)<br>세동맥 = <b>주 저항</b>, 부교감 ✗<br>모세혈관 = 교환, 유속 최소<br>정맥 = <b>혈액</b> 저장소 64%<br>MAP ≈ 이완기 + ⅓ 맥압'),
          ('🎛 세동맥 조절', '국소 = <b>분배</b>: O₂↓·CO₂↑·아데노신·NO·히스타민 → 확장, 근원성 → 수축<br>외인성 = <b>혈압</b>: 교감 NE → α₁ → TPR ↑<br>바소프레신·안지오텐신 II = 수축'),
          ('🔁 환류·혈압', '림프 20 − 17 = 3 L/일<br>ECF = 간질액 80 + 혈장 20<br>환류 5요인: 교감·근육 펌프·판막·호흡·심장 흡인<br><b>MAP = CO × TPR</b><br>부교감 = HR만')],
         '<ol><li>주 저항 혈관 = <b>세동맥</b> (모세혈관 ✗)</li><li>유량은 어디서나 같고 <b>유속</b>만 모세혈관에서 느림</li><li>세동맥 확장 = 교감 ↓ + NO (부교감 ✗)</li></ol>',
         ['저항은 반지름의 4제곱에 반비례하므로 세동맥 반지름이 혈관 저항과 혈류의 주된 결정 요인이다.',
          '세동맥의 국소 조절은 장기별 혈류 분배를, 교감신경에 의한 외인성 조절은 TPR을 바꿔 혈압을 조절한다.',
          '평균 동맥압은 심박출량과 총말초저항의 곱이다(MAP = CO × TPR).'])
