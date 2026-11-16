from lib import *

def build():
    chapter(11, 'The Blood')
    c = CH['color']
    page('CHAPTER 11', 'The Blood — 한 장 지도',
        chev([('11.1 혈장', '단백질 3종', '#c2410c'), ('11.2 적혈구', 'Hb·CA·EPO', c), ('11.3 백혈구', '다섯 종류', '#f08c00'), ('11.4 혈소판·지혈', '3단계·트롬빈', '#a63e00')]) +
        grid('1.05fr 1fr',
            card('한 줄 요약', '혈액은 체중의 <b>8%</b> — 혈장 55%(물 90%) + 세포 45%(거의 <b>적혈구</b>). 혈장 기능은 <b>혈장 단백질</b>(알부민·글로불린·피브리노겐)이 맡는다. <span class="hy">적혈구</span>는 핵·세포소기관 없이 <b>헤모글로빈</b>을 가득 담아 O₂를 나르고, <b>탄산탈수효소</b>로 CO₂를 HCO₃⁻로 바꿔 운반하며, <b>콩팥의 EPO</b>가 생성을 조절한다. 백혈구는 혈관 밖에서 방어하고, 혈소판(<b>거핵세포 조각</b>, TPO는 간)은 <span class="hp">혈관 수축 → 혈소판 마개 → 응고(트롬빈: 피브리노겐 → 피브린)</span>로 지혈한다.', 'sum big'),
            col(card('🎯 교수님 강조 (11/16 녹취)', '<ol><li>"<b>RBC의 대사가 좀 중요</b>" — 핵·DNA·RNA ✗, 단백질 합성 ✗, 해당과정, CO₂ 운반 ✔</li><li><b>탄산탈수효소</b>와 <b>염소 이동</b>(추가 슬라이드)</li><li>EPO = <b>콩팥</b>, TPO = <b>간</b></li><li>응고 연쇄는 "<b>아는 건 그렇게 중요하지 않다</b>" → 3단계 + 트롬빈</li><li>백혈구 기능은 면역학에서 — 표면적인 것만</li></ol>', 'warn'),
                card('💡 숫자', '체중 <b>8%</b> · 혈장 <b>55–58%</b>(물 90%) · 헤마토크릿 <b>42–45%</b> · WBC+혈소판 <b>&lt;1%</b> · 1 mm³당 WBC <b>7,000</b> / RBC <b>500만</b> / 혈소판 <b>25만</b> · 적혈구 수명 <b>120일</b> · 거핵세포 1개 → 혈소판 <b>1,000</b>', 'tip'))), 'Slides 37–53')

    page('PART 01', '혈장과 혈장 단백질 · 적혈구',
        grid('1fr 1.1fr 1fr',
            col(card('정의 — 혈액의 구성', tbl(['층', '비율', '내용'], [['혈장', '<b>55–58%</b>', '물 90% + 이온(Na⁺·Cl⁻)·단백질·영양·노폐물·가스·호르몬'], ['버피코트', '<b>&lt;1%</b>', '백혈구 + 혈소판'], ['헤마토크릿', '<b>42–45%</b>', '적혈구 (혈액 세포의 99%)']]) +
                    '<p style="margin-top:1.2mm">혈소판 = 세포가 아니라 <b>세포 조각</b></p>', 'def'),
                img('c10-40', '원심분리한 혈액: 혈장 · 버피코트 · 적혈구', '60mm')),
            col(card('🧪 혈장 단백질', '거대 분자 <b>콜로이드</b> → 모세혈관 구멍을 <b>못 지남</b> → 혈장에 남아 <b>삼투압</b>으로 물을 붙잡음(간질로 새지 않게) + 잔기로 <b>pH 완충</b>' +
                    tbl(['단백질', '역할'], [['<b>알부민</b>', '<span class="hy">가장 많음</span>, 교질 삼투압 최대, 잘 안 녹는 물질 <b>비특이</b> 운반'], ['<b>글로불린</b>', '<b>특이</b> 운반 · 응고 · 염분 균형, <b>γ = 면역글로불린(항체)</b>'], ['<b>피브리노겐</b>', '<b>응고</b> — 피브린의 재료']]), 'tip'),
                card('🔴 적혈구 — O₂ 운반 설계', '<ul><li><b>납작한 원반</b>: 표면적 ↑, 얇아 확산 ↑</li><li><b>유연한 막</b>: 좁은 모세혈관을 변형하며 통과</li><li><b>핵·세포소기관 없음</b> → 헤모글로빈 최대</li><li>미토콘드리아 ✗ → <b>해당과정</b>으로 ATP</li></ul>')),
            col(card('🧬 헤모글로빈', '<b>α 2 + β 2</b> 사슬 + <b>헴 4개(철 Fe)</b> — 적혈구에만<br>산소화되면 붉음, 탈산소면 더 짙은 붉은색<br>운반: <b>O₂ · CO₂ · H⁺ · CO · NO</b>', 'mint'),
                img('c10-43', '헤모글로빈: α·β 사슬과 철을 가진 헴', '44mm'),
                img('c10-44', '골수성 줄기세포 → 적아구 → 그물적혈구 → 적혈구(핵·소기관 소실)', '28mm'))), 'Slides 39–44')

    page('PART 02', 'CO₂ 운반 · 적혈구 생성 · 백혈구',
        grid('1fr 1fr 1fr',
            col(card('⚗ 탄산탈수효소 · 염소 이동', '<span style="font-size:10.5pt"><b>CO₂ + H₂O ⇌ H₂CO₃ ⇌ H⁺ + HCO₃⁻</b></span>' + tbl(['장소', '일'], [
                    ['체순환 모세혈관', 'CO₂ → <b>HCO₃⁻</b>, <b>AE1</b>이 HCO₃⁻ 내보내고 <b>Cl⁻ 들임</b>, H⁺는 Hb가 완충'],
                    ['폐 모세혈관', 'AE1 <b>반대 방향</b> → HCO₃⁻ → <b>CO₂</b> → 날숨']]) +
                    '<p style="margin-top:1.2mm"><b>Chloride shift = Hamburger effect</b>: HCO₃⁻ ↔ Cl⁻ 교환으로 전기적 중성 유지 <small>(교수님 추가 슬라이드)</small></p>', 'tip'),
                card('정의 — 적혈구 생성', '분열 ✗ → <b>골수</b>에서 계속 생성 · 수명 <b>120일</b> → <b>비장</b>에서 제거 · <b>조혈모세포</b> → 적혈구·백혈구·혈소판', 'def')),
            col(card('🫘 EPO 되먹임', flow('O₂ 운반 능력 ↓', '<b>콩팥</b>이 감지', '<b>EPO</b> 분비', '골수 적혈구 생성 ↑', 'O₂ 운반 능력 ↑ → EPO ↓', small=True) +
                    '음성 되먹임 · 빈혈 치료제 <b>에포젠·아라네스프</b> = EPO 재조합 단백질(바이오 의약품)', 'mint'),
                img('c10-45', 'EPO: 콩팥 → 골수 → 적혈구 ↑', '62mm')),
            col(card('🛡 백혈구 — 혈관 밖에서 방어', '<b>"정상 자기"가 아닌 것</b>을 제거·중화. 조직의 케모카인에 끌려 <b>혈관 밖으로</b> — 혈액은 <b>운반 통로</b>' +
                    tbl(['종류', '분류', '비율', '한 줄'], [['<b>호중구</b>', '과립', '<b>60–70%</b>', '세균 포식'], ['호산구', '과립', '1–4%', '알레르기·기생충'], ['호염기구', '과립', '0.25–0.5%', '히스타민·헤파린'], ['단핵구', '무과립', '2–6%', '식세포 → 대식세포'], ['<b>림프구</b>', '무과립', '<b>25–33%</b>', 'T·B, 특이 면역']]) +
                    '<p style="margin-top:1.2mm">골수성 → 과립구·단핵구 / 림프성 → 림프구 · <b>백혈병</b> = 통제되지 않는 증식</p>'),
                img('c10-49', '조혈 계통: 골수성 vs 림프성 줄기세포', '48mm'))), 'Slides 44–49')

    page('PART 03', '혈소판과 지혈',
        grid('1fr 1.1fr 1fr',
            col(card('정의 — 혈소판', '거대한 <b>거핵세포</b>(골수)가 찢어진 <b>세포 조각</b> · 1개 → <b>1,000개</b><br>핵 ✗, <b>세포소기관 ✔</b>(에너지·분비) · <b>액틴·마이오신</b> → 수축<br>분비·수축 기능이 지혈에 중요', 'def'),
                card('🆚 EPO vs TPO', tbl(['', '만드는 곳', '하는 일'], [['<b>EPO</b>', '<b>콩팥</b>', '골수 → 적혈구 ↑'], ['<b>TPO</b>', '<b>간</b>', '거핵세포 → 혈소판 ↑']]), 'warn'),
                img('c10-51', '거핵세포와 떨어져 나오는 혈소판', '48mm')),
            col(card('🩹 지혈 3단계', '<ol><li><b>혈관 수축</b>(vascular spasm): 다친 혈관이 즉시 수축 → 새는 피 ↓</li><li><b>혈소판 마개</b>: 평소엔 매끈한 내피에 안 붙음 → 찢어지면 <b>콜라겐 노출</b> → <b>부착</b> → 활성화 → <b>ADP·트롬복세인 A₂</b>로 더 모음 → 응집 → 마개 <small>(양성 되먹임)</small></li><li><b>응고</b>: <b>트롬빈</b>이 <b>피브리노겐(녹음) → 피브린(실, 안 녹음)</b> → 그물에 혈구·혈소판이 걸림</li></ol>', 'tip'),
                card('⚠ 함정', '<ul><li>"피브린 → 피브리노겐" ✗ (반대)</li><li>"혈소판엔 세포소기관이 없다" ✗</li><li>"TPO는 콩팥에서" ✗ — EPO가 콩팥</li></ul>', 'warn')),
            col(img('c10-53', '응고 연쇄: 내인성(XII)·외인성(조직 트롬보플라스틴) → X → 트롬빈 → 피브린', '92mm'),
                card('응고 연쇄', '두 경로가 <b>인자 X</b>에서 만나 → 트롬빈 → 피브린, <b>Ca²⁺</b> 필요. ⭐ 교수님: "아는 건 그렇게 중요하지 않다"', 'why'))), 'Slides 50–53')

    qpage('PART 01–02', '혈장 · 적혈구 ①',
        FQ('c10-48-q', 'The table shows the cellular elements of blood. Identify the cell types labeled <b>A</b> to <b>G</b>.', '표는 혈액의 세포 성분이다. A~G의 이름을 쓰시오.',
           [('A', '호중구 Neutrophil'), ('B', '호산구 Eosinophil'), ('C', '호염기구 Basophil'), ('D', '단핵구 Monocyte'), ('E', '림프구 Lymphocyte'), ('F', '적혈구 Erythrocyte'), ('G', '혈소판 Platelets')],
           W('A·B·C = 다형핵 <b>과립구</b>, D·E = 단핵 <b>무과립구</b>', '비율 단서: 60–70%(A, 가장 많음) · 25–33%(E) · 0.25–0.5%(C, 가장 적음)') + K('호중구 > 림프구 > 단핵구 > 호산구 > 호염기구'), stars=2, h='34mm'),
        TF([('Blood makes up about 8% of body weight, and erythrocytes account for most of the cellular elements, with a hematocrit of about 42–45%.', '혈액은 체중의 약 8%이며, 세포 성분 대부분은 적혈구로 헤마토크릿은 약 42–45%다.'),
            ('Plasma proteins easily diffuse out of capillaries into the interstitial fluid, so they do not contribute to plasma osmotic pressure.', '혈장 단백질은 모세혈관에서 간질액으로 쉽게 확산되므로 혈장 삼투압에 기여하지 않는다.'),
            ('Albumin is the most abundant plasma protein and nonspecifically binds poorly water-soluble substances for transport.', '알부민은 가장 많은 혈장 단백질이며, 물에 잘 녹지 않는 물질에 비특이적으로 결합해 운반한다.'),
            ('Mature erythrocytes contain mitochondria and produce most of their ATP by oxidative phosphorylation.', '성숙한 적혈구는 미토콘드리아를 가지고 있어 ATP 대부분을 산화적 인산화로 만든다.'),
            ('Each hemoglobin molecule consists of two α chains and two β chains, each with an iron-containing heme group that binds O₂.', '헤모글로빈 분자는 α 사슬 2개와 β 사슬 2개로 되어 있고, 각각 O₂와 결합하는 철 함유 헴을 가진다.')],
           'T F T F T', W('(2) ✗ 혈장 단백질은 너무 커서 <b>못 나감</b> → 혈장에 남아 <b>삼투압</b> 형성', '(4) ✗ 적혈구는 미토콘드리아가 <b>없어</b> <b>해당과정</b>으로 ATP'), stars=2), cols=2)

    qpage('PART 02', '적혈구 · CO₂ 운반 ②',
        MC('Which TWO statements about mature erythrocytes are correct? <b>(Choose two.)</b>', '성숙한 적혈구에 대한 설명으로 옳은 것 두 개는?',
           [('Because they lack a nucleus and organelles, mature erythrocytes cannot divide or synthesize new proteins.', '핵과 세포소기관이 없으므로 성숙한 적혈구는 분열하거나 새 단백질을 합성할 수 없다.'),
            ('Erythrocytes contain carbonic anhydrase, which converts CO₂ and H₂O into H⁺ and bicarbonate, the main form in which CO₂ is carried in the blood.', '적혈구에는 CO₂와 H₂O를 H⁺와 중탄산으로 바꾸는 탄산탈수효소가 있으며, 중탄산은 혈중 CO₂ 운반의 주된 형태다.'),
            ('Erythrocytes are produced mainly in the spleen, where they also divide to replace worn-out cells.', '적혈구는 주로 비장에서 만들어지며, 비장에서 분열해 낡은 세포를 대체한다.'),
            ('Hemoglobin carries only O₂ and cannot bind CO₂, H⁺, CO or NO.', '헤모글로빈은 O₂만 운반하고 CO₂·H⁺·CO·NO와는 결합할 수 없다.'),
            ('Erythropoietin is secreted by the liver when the O₂-carrying capacity of the blood increases.', '에리트로포이에틴은 혈액의 O₂ 운반 능력이 증가할 때 간에서 분비된다.')], '①, ②',
           W('① ✔ 교수님 강조 "RBC 대사"', '② ✔ 탄산탈수효소 → HCO₃⁻', '③ ✗ 생성은 <b>골수</b>, 비장은 낡은 적혈구 <b>제거</b>, 분열 ✗', '④ ✗ CO₂·H⁺·CO·NO도 결합', '⑤ ✗ EPO는 <b>콩팥</b>, O₂ 운반 능력이 <b>감소</b>할 때'), pick=2, stars=2),
        BOX('Fill in blanks (1)–(10) with the most appropriate words from the box. Not all words are used.', '상자에서 알맞은 단어를 골라 빈칸 (1)~(10)을 채우시오. 쓰지 않는 단어도 있다.',
            ['carbonic anhydrase', 'bicarbonate', 'chloride', 'AE1', 'lungs', 'hemoglobin', 'kidneys', 'erythropoietin', 'red bone marrow', 'spleen', 'liver', 'thrombopoietin'],
            'Inside erythrocytes, <u>(1)</u> converts CO₂ and H₂O into H⁺ and <u>(2)</u>, and H⁺ is buffered by <u>(3)</u>. The <u>(4)</u> antiporter moves HCO₃⁻ out of the cell in exchange for <u>(5)</u> ions, and the process reverses in the capillaries of the <u>(6)</u>, where CO₂ is exhaled. When the O₂-carrying capacity of the blood falls, the <u>(7)</u> secrete <u>(8)</u>, which stimulates erythrocyte production in the <u>(9)</u>. Worn-out erythrocytes are removed in the <u>(10)</u>.',
            ['carbonic anhydrase', 'bicarbonate', 'hemoglobin', 'AE1', 'chloride', 'lungs', 'kidneys', 'erythropoietin', 'red bone marrow', 'spleen'],
            W('함정: <b>liver·thrombopoietin</b>은 혈소판 쪽(TPO = 간)') + K('CA → HCO₃⁻', 'AE1 ↔ Cl⁻ (chloride shift)', 'EPO = 콩팥 → 골수', '비장 = 제거'), stars=3), cols=2)

    qpage('PART 02–03', '백혈구 · 지혈 ③',
        MC('Which TWO statements about platelets and hemostasis are correct? <b>(Choose two.)</b>', '혈소판과 지혈에 대한 설명으로 옳은 것 두 개는?',
           [('Platelets are cell fragments shed from megakaryocytes; they lack a nucleus but contain organelles and actin and myosin.', '혈소판은 거핵세포에서 떨어져 나온 세포 조각으로, 핵은 없지만 세포소기관과 액틴·마이오신을 가진다.'),
            ('When a vessel is damaged, platelets adhere to exposed collagen and release ADP and thromboxane A₂, which recruit more platelets to form a plug.', '혈관이 손상되면 혈소판이 노출된 콜라겐에 붙고 ADP와 트롬복세인 A₂를 내어 혈소판을 더 모아 마개를 만든다.'),
            ('During coagulation, fibrin is converted by plasmin into soluble fibrinogen, which forms a net over the wound.', '응고 중 피브린이 플라스민에 의해 녹는 피브리노겐으로 바뀌어 상처 위에 그물을 만든다.'),
            ('Thrombopoietin is produced by the kidneys and stimulates erythrocyte production in the bone marrow.', '트롬보포이에틴은 콩팥에서 만들어져 골수의 적혈구 생성을 촉진한다.'),
            ('Platelets normally adhere tightly to the smooth endothelium of intact vessels, which keeps blood from leaking.', '혈소판은 평소 손상되지 않은 혈관의 매끈한 내피에 단단히 붙어 피가 새지 않게 한다.')], '①, ②',
           W('① ✔ 거핵세포 조각, 소기관 ✔, 수축 ✔', '② ✔ 부착 → ADP·TXA₂ → 마개', '③ ✗ <b>트롬빈</b>이 <b>피브리노겐 → 피브린</b>(녹지 않는 실)', '④ ✗ TPO = <b>간</b>, <b>혈소판</b> 생성', '⑤ ✗ 평소에는 내피에 <b>붙지 않는다</b>'), pick=2, stars=2),
        TF([('The three major steps of hemostasis are vascular spasm, formation of a platelet plug, and blood coagulation.', '지혈의 세 주요 단계는 혈관 수축, 혈소판 마개 형성, 혈액 응고다.'),
            ('Leukocytes mainly perform their defensive functions inside the blood vessels and rarely leave the circulation.', '백혈구는 주로 혈관 안에서 방어 기능을 하며 순환계를 거의 떠나지 않는다.'),
            ('Neutrophils are the most abundant leukocytes, and lymphocytes provide specific immune defense.', '호중구는 가장 많은 백혈구이고, 림프구는 특이적 면역 방어를 맡는다.'),
            ('A single megakaryocyte produces about 1000 platelets, and thrombopoietin from the liver increases platelet production.', '거핵세포 하나는 혈소판 약 1000개를 만들고, 간의 트롬보포이에틴이 혈소판 생성을 늘린다.'),
            ('Leukemia is a condition in which too few leukocytes are produced because the bone marrow stops making them.', '백혈병은 골수가 백혈구 생성을 멈춰 백혈구가 너무 적게 만들어지는 상태다.')],
           'T F T T F', W('(2) ✗ 백혈구는 주로 <b>혈관 밖(조직)</b>에서 일함 — 혈액은 운반 통로', '(5) ✗ 백혈병 = 백혈구의 <b>통제되지 않는 증식</b>(암)'), stars=2), cols=2)

    qpage('PART 01–03', '서술형',
        ES('Explain how the structure and contents of erythrocytes make them suited for transporting O₂ and CO₂, including the role of carbonic anhydrase and the chloride shift.', '적혈구의 구조와 내용물이 O₂와 CO₂ 운반에 알맞은 이유를 탄산탈수효소와 염소 이동의 역할을 포함해 서술하시오.',
           '적혈구는 <b>납작한 원반</b>이라 표면적이 넓고 얇아 O₂ <b>확산</b>이 빠르며, <b>유연한 막</b>으로 좁은 모세혈관을 변형하며 지나간다. <b>핵과 세포소기관이 없어</b> 내부를 <b>헤모글로빈</b>(α2β2, 철 함유 헴 4개)으로 채우므로 혈장에 잘 녹지 않는 O₂를 대량 운반하고, CO₂·H⁺도 결합한다. 미토콘드리아가 없어 <b>해당과정</b>으로 ATP를 만든다. 조직에서는 <b>탄산탈수효소</b>가 CO₂ + H₂O → H⁺ + HCO₃⁻를 촉매하고, H⁺는 헤모글로빈이 완충하며, HCO₃⁻는 <b>AE1</b>을 통해 Cl⁻와 교환되어 혈장으로 나간다(<b>염소 이동</b>, 전기적 중성 유지). 폐에서는 이 과정이 반대로 일어나 HCO₃⁻가 CO₂로 바뀌어 날숨으로 나간다.',
           K('원반·유연한 막', '핵·소기관 ✗ → Hb 최대', '해당과정', 'CA: CO₂ ⇌ HCO₃⁻', 'AE1 Cl⁻ 교환'), stars=3),
        ES('Describe the three major steps of hemostasis, and compare how erythropoietin and thrombopoietin regulate blood cell production.', '지혈의 세 주요 단계를 서술하고, 에리트로포이에틴과 트롬보포이에틴이 혈액 세포 생성을 어떻게 조절하는지 비교하시오.',
           '① <b>혈관 수축</b>: 손상된 혈관이 즉시 수축해 그곳으로 흐르는 피를 줄인다. ② <b>혈소판 마개</b>: 평소 내피에 붙지 않던 혈소판이 손상 부위에 노출된 <b>콜라겐에 부착</b>하고 활성화되어 <b>ADP·트롬복세인 A₂</b>를 방출해 혈소판을 더 모아 응집시켜 마개를 만든다. ③ <b>응고</b>: 응고 인자의 연쇄 반응으로 생긴 <b>트롬빈</b>이 녹아 있는 <b>피브리노겐을 녹지 않는 실 모양의 피브린</b>으로 바꾸고, 피브린 그물이 혈구와 혈소판을 가둬 피떡을 만든다. <b>EPO</b>는 혈액의 O₂ 운반 능력이 떨어지면 <b>콩팥</b>에서 분비되어 골수의 <b>적혈구</b> 생성을 늘리는 음성 되먹임 호르몬이고, <b>TPO</b>는 <b>간</b>에서 만들어져 골수 <b>거핵세포</b>의 수와 혈소판 생성을 늘린다.',
           K('혈관 수축 → 혈소판 마개 → 응고', '콜라겐 · ADP · TXA₂', '트롬빈: 피브리노겐 → 피브린', 'EPO 콩팥 / TPO 간'), stars=3), cols=2)

    memo([('🧪 혈장', '체중 8% · 혈장 55% · Hct 42–45%<br>WBC+혈소판 &lt;1%<br>알부민 = 최다·삼투압<br>글로불린 γ = 항체<br>피브리노겐 = 응고'),
          ('🔴 적혈구', '원반·유연한 막<br>핵·소기관 ✗ → DNA·RNA ✗, 단백질 합성 ✗<br>해당과정 · Hb α2β2 + 헴 4<br>CA: CO₂ ⇌ HCO₃⁻ · AE1 Cl⁻ 교환<br>120일 · 비장 제거'),
          ('🏭 생성', 'EPO = <b>콩팥</b> → 골수 적혈구<br>TPO = <b>간</b> → 거핵세포 혈소판<br>골수성 → 과립구·단핵구·적혈구·거핵세포<br>림프성 → 림프구'),
          ('🩹 백혈구·지혈', '호중구 &gt; 림프구 &gt; 단핵구 &gt; 호산구 &gt; 호염기구<br>백혈구는 혈관 밖에서<br>혈관 수축 → 혈소판 마개(콜라겐·ADP·TXA₂) → 응고<br>트롬빈: 피브리노겐 → 피브린')],
         '<ol><li>EPO = <b>콩팥</b>, TPO = <b>간</b></li><li>트롬빈은 피브리노겐 → <b>피브린</b> (반대 ✗)</li><li>적혈구: 미토콘드리아 ✗ → <b>해당과정</b>, 단백질 합성 ✗</li></ol>',
         ['적혈구는 핵과 세포소기관이 없어 헤모글로빈을 최대로 담고, 해당과정으로 ATP를 만들며, 탄산탈수효소로 CO₂를 중탄산으로 바꿔 운반한다.',
          '혈액의 O₂ 운반 능력이 떨어지면 콩팥이 에리트로포이에틴을 분비해 골수의 적혈구 생성을 늘린다.',
          '지혈은 혈관 수축, 혈소판 마개 형성, 그리고 트롬빈이 피브리노겐을 피브린으로 바꾸는 응고의 세 단계로 일어난다.'])
