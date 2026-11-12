from lib import *

def build():
    chapter(9, 'Cardiac Physiology')
    c = CH['color']
    page('CHAPTER 9', 'Cardiac Physiology — 한 장 지도',
        chev([('9.1 해부', '방·판막·개재판', '#a61e4d'), ('9.2 전기 활동', '박동조율·전도·ECG', c), ('9.3 심장 주기', '네 단계·심음', '#e64980'),
              ('9.4 심박출량', 'CO = HR × SV', '#c2255c'), ('9.5 관상순환', '이완기 70%', '#862e5c')]) +
        grid('1.05fr 1fr',
            card('한 줄 요약', '심장은 좌우 <b>두 펌프</b>로 같은 양을 동시에 내보내고, <b>판막</b>은 압력 차로 수동적으로 여닫혀 한 방향 흐름을 지킨다. <span class="hy">SA결절</span>이 스스로 만든 AP(funny → T형 → L형 Ca²⁺)가 <b>AV결절에서 잠깐 멈췄다가</b> 히스·푸르키네로 퍼지고, 수축세포의 <span class="hp">고원기</span> 때문에 불응기가 길어 강축이 없다. 펌프 성능은 <b>CO = HR × SV</b> — HR은 자율신경, SV는 <b>프랭크-스탈링</b>(EDV)과 교감(수축성)이 정한다. 심장근은 <b>이완기</b>에 관상동맥으로 피를 받는다.', 'sum big'),
            col(card('🎯 교수님 강조 (11/2 · 11/9 · 11/12 녹취)', '<ol><li>좌·우심실은 <b>동시에 같은 양</b>을 박출 (강의 끝 문제)</li><li>SA결절이 박동조율기 = <b>가장 빠르게</b> AP 생성 (강의 끝 문제)</li><li>심장근: <b>긴 불응기 → 강축 없음</b>, 신경 없이 수축 (단, Ca²⁺ 필요)</li><li>신경은 박동을 <b>시작하지 않고</b> 속도·강도만 조절</li><li>SV 조절: <b>내인성 vs 외인성</b>을 구분할 것</li></ol>', 'warn'),
                card('💡 숫자', 'SA <b>70–80</b> · AV <b>40–60</b> · His·Purkinje <b>20–40</b>회/분 · AV 지연 <b>~100 ms</b> · 심실 전도 <b>~30 ms</b> · 수축세포 <b>−90 → +30 mV</b>, AP <b>~250 ms</b> · EDV <b>135</b> / ESV <b>65</b> / SV <b>70 mL</b> · EF <b>52%</b> · 관상 혈류 <b>70%</b> 이완기', 'tip'))), 'Slides 1–45')

    page('PART 01', '심장의 구조 · 두 순환 · 판막 · 개재판',
        grid('1fr 1.05fr 1fr',
            col(card('정의', '순환계 = <b>심장(펌프, 압력 기울기를 만듦)</b> + <b>혈관(통로)</b> + <b>혈액(운반 매체)</b><br><b>폐순환</b>: 우심실 → 폐 → 좌심방 / <b>체순환</b>: 좌심실 → 온몸 → 우심방', 'def'),
                card('🫀 이중 펌프', tbl(['', '우심실', '좌심실'], [['순환', '폐 (저압·저저항)', '체 (<b>고압·고저항</b>)'], ['박출량', '<b>같다</b>', '<b>같다</b>'], ['벽', '얇음', '<b>두꺼움</b>']]) +
                    '<p style="margin-top:1.4mm">심방 = 정맥에서 <b>받는</b> 방, 심실 = 동맥으로 <b>쏘는</b> 방. 좌우는 <b>중격</b>이 막음</p>'),
                img('c9-08', '혈액 경로: 대정맥 → 우심방 → 우심실 → 폐동맥 → 폐정맥 → 좌심방 → 좌심실 → 대동맥', '62mm')),
            col(card('🚪 판막 — 압력 차로 <u>수동적으로</u> 여닫힘', tbl(['', '방실판 (AV)', '반월판'], [
                    ['위치', '심방–심실', '심실–동맥'], ['이름', '우 <b>삼첨판</b> / 좌 <b>승모판(이첨판)</b>', '<b>폐동맥판</b> / <b>대동맥판</b>'],
                    ['열림', '심방 압 &gt; 심실 압', '심실 압 &gt; 동맥 압'], ['닫힘 → 심음', '수축 시작 → <b>S1</b>', '이완 시작 → <b>S2</b>'],
                    ['지지', '<b>건삭 + 유두근</b> = 뒤집힘 방지', '반달 주머니 3개']]) +
                '<p style="margin-top:1.4mm">정맥–심방 사이엔 판막 <b>없음</b></p>', 'tip'),
                card('🦴 섬유골격', '판막 고리 → 근육이 붙는 뼈대 + <span class="hy">전기 절연</span> — 심방·심실 사이 전기 통로는 <b>AV결절뿐</b>', 'why')),
            col(card('🧱 심장벽 · 심장근', '<ul><li>3층: 심내막 · <b>심근층</b>(나선 배열 → 짜내기) · 심외막</li><li><b>개재판</b> = <b>데스모솜</b>(기계적 결합) + <b>간극연접</b>(AP 전달)</li><li>→ 심방끼리, 심실끼리 <b>기능적 합포체</b> (총 2개)</li></ul>', 'mint'),
                card('⚠ 함정', '<ul><li>"좌심실이 더 많은 양을 박출" ✗ — 양은 같고 <b>압력</b>이 다름</li><li>"건삭이 판막을 연다" ✗ — <b>뒤집힘만 막음</b></li><li>"심방·심실 근육이 간극연접으로 직접 연결" ✗</li></ul>', 'warn'))), 'Slides 2–14')

    page('PART 02', '전기 활동 — 박동조율 전위 · 전도 경로',
        grid('1fr 1.1fr 1fr',
            col(card('정의 — 자동능 (Autorhythmicity)', '신경 없이 스스로 AP를 만들어 박동. <b>수축세포 99%</b>(AP 시작 ✗, 수축 ✔) vs <b>자동능 세포 ~1%</b>(AP 시작 ✔, 수축 ✗)', 'def'),
                card('⚡ 박동조율 전위 — <u>휴지막전위가 없다</u>', '<ol><li>과분극(~−60 mV)에 <b>funny 채널(I<sub>f</sub>)</b> 열림 → <b>Na⁺ 유입</b> + K⁺ 유출 ↓</li><li><b>T형 Ca²⁺</b> 채널 → 역치(~−40 mV)까지</li><li><b>L형 Ca²⁺</b> 채널 → 상승기 (<b>Na⁺ 아님</b>)</li><li>K⁺ 채널 → 재분극 → SERCA·NCX·Na⁺/K⁺ 펌프로 복구</li></ol>', 'tip'),
                img('c9-17', '박동조율 세포의 AP: 느린 탈분극 → 역치 → Ca²⁺ 상승 → K⁺ 하강', '44mm')),
            col(img('c9-20', '(a) 특수 전도계 (b) 흥분 확산 — 섬유조직이 심방·심실을 전기적으로 분리', '58mm'),
                card('🛣 전도 순서와 속도', flow('SA결절', '심방(심방간·결절간 경로)', '<b>AV결절 ~100 ms 지연</b>', '히스다발', '푸르키네 (~30 ms)', small=True) +
                    tbl(['부위', '회/분', '역할'], [['<b>SA결절</b> (우심방, 상대정맥 입구)', '<b>70–80</b>', '정상 박동조율기 — 가장 빠름'], ['AV결절', '40–60', '유일한 통로 + 지연 → 심실 충만 시간'], ['히스·푸르키네', '20–40', '심실 전체 동시 흥분']]) +
                    '<p style="margin-top:1.4mm">SA 고장 → <b>AV결절</b>이 대신, 너무 느리면 인공 심박동기</p>')),
            col(card('🆚 박동조율 세포 vs 수축세포', tbl(['', '박동조율', '수축세포'], [['휴지막전위', '<b>없음</b>', '<b>−90 mV</b>'], ['상승 이온', '<b>Ca²⁺</b> (L형)', '<b>Na⁺</b> (→ +30)'], ['고원기', '없음', '<b>있음</b> (~250 ms)']]) +
                    '<p style="margin-top:1.4mm">고원기 = <b>L형 Ca²⁺ 유입 + K⁺ 투과성 ↓</b> → <span class="hp">긴 불응기 → 강축 없음</span></p>', 'mint'),
                img('c9-26', '수축세포 AP: Na⁺ 빠른 상승 → 고원기(Ca²⁺ 유입·K⁺ ↓) → K⁺ 재분극', '56mm'))), 'Slides 15–26')

    page('PART 02', 'Ca²⁺ 유발 Ca²⁺ 방출 · 심전도',
        grid('1fr 1.1fr 1fr',
            col(card('🔥 CICR (Ca²⁺-induced Ca²⁺ release)', '<ol><li>T세관의 <b>L형 Ca²⁺ 채널</b>로 ECF Ca²⁺가 <b>조금</b> 유입</li><li>이 Ca²⁺가 SR의 <b>라이아노딘 수용체</b>를 엶</li><li>SR Ca²⁺ <b>대량</b> 방출 → <b>트로포닌</b> → 교차다리</li></ol>', 'tip'),
                card('🆚 골격근(8장) vs 심장근', tbl(['', '골격근', '심장근'], [['Ca²⁺ 출처', 'SR만', '<b>ECF(소량) + SR(대량)</b>'], ['방아쇠', 'T세관 전압 변화', '<b>들어온 Ca²⁺</b>'], ['Ca²⁺ 결합', '트로포닌', '트로포닌'], ['강축', '가능', '<b>불가</b>']])),
                img('c9-27', 'CICR 흐름: AP → T세관 → 소량 Ca²⁺ → SR 대량 방출 → 수축', '58mm')),
            col(card('📈 심전도 (ECG)', '심장 전기가 체액을 타고 <b>몸 표면</b>에 닿은 것의 기록 (직접 기록 ✗)' + tbl(['파형·분절', '심장에서'], [
                    ['<b>P</b>', '심방 <b>탈분극</b>'], ['PR 분절', '<b>AV결절 지연</b>'], ['<b>QRS</b>', '심실 <b>탈분극</b> (심방 재분극은 묻힘)'],
                    ['ST 분절', '심실 <b>고원기</b> — 박출'], ['<b>T</b>', '심실 <b>재분극</b>'], ['TP 분절', '휴지, 이완·충만']]) +
                '<p style="margin-top:1.4mm">ECG로 심박수·리듬 이상, 심근 손상을 찾음</p>'),
                card('⚠ 함정', '"T파 = 심방 재분극" ✗ / 파형은 <b>전기</b> 사건, 수축은 그 <b>직후</b>', 'warn')),
            col(img('c9-29', '한 박동 동안의 ECG 구간과 흥분 부위', '100mm'))), 'Slides 27–29')

    qpage('PART 01–02', '해부 · 전기 활동 ①',
        FQ('c9-20-q', 'The figure shows the specialized conduction system of the heart. Identify the structures labeled <b>A</b> to <b>G</b>.', '그림은 심장의 특수 전도계다. A~G의 이름을 쓰시오.',
           [('A', '동방결절 SA node'), ('B', '방실결절 AV node'), ('C', '히스다발 좌각 Left branch of bundle of His'), ('D', '푸르키네 섬유 Purkinje fibers'), ('E', '결절간 경로 Internodal pathway'), ('F', '심방간 경로 Interatrial pathway'), ('G', '히스다발 우각 Right branch of bundle of His')],
           W('흥분 순서: A(SA) → F(좌심방으로) · E(AV로) → B(AV, ~100 ms 지연) → C·G(히스다발 좌·우각) → D(푸르키네) → 심실', 'SA결절은 <b>우심방</b>, 상대정맥 입구 근처') + K('SA → AV → His → Purkinje', '심방간 = 좌심방', '결절간 = AV결절'), stars=3, h='54mm'),
        TF([('The left and right ventricles contract at the same time and eject equal volumes of blood with each beat, although the left ventricle develops a much higher pressure.', '좌·우심실은 동시에 수축하고 박동마다 같은 양을 내보내지만, 좌심실이 훨씬 높은 압력을 만든다.'),
            ('Heart valves are opened and closed by contraction of the papillary muscles, which actively pull the cusps apart during ventricular filling.', '심장 판막은 유두근의 수축으로 여닫히며, 유두근이 심실 충만 중 판막 잎을 능동적으로 벌린다.'),
            ('The SA node is the normal pacemaker because it reaches threshold and fires action potentials faster than any other autorhythmic tissue.', 'SA결절은 다른 어떤 자동능 조직보다 빨리 역치에 도달해 AP를 만들기 때문에 정상 박동조율기다.'),
            ('In SA node cells, the rising phase of the action potential is caused mainly by a rapid influx of Na⁺ through fast voltage-gated Na⁺ channels.', 'SA결절 세포 AP의 상승기는 주로 빠른 전압개폐 Na⁺ 채널을 통한 Na⁺ 유입 때문이다.'),
            ('The AV nodal delay allows the atria to finish contracting and the ventricles to fill completely before ventricular contraction begins.', 'AV결절 지연 덕분에 심방이 수축을 마치고 심실이 다 찬 뒤 심실 수축이 시작된다.')],
           'T F T F T', W('(2) ✗ 판막은 <b>압력 차</b>로 수동적으로 여닫힘. 유두근·건삭은 방실판이 <b>뒤집히지 않게</b> 잡을 뿐', '(4) ✗ SA결절 상승기 = <b>L형 Ca²⁺</b> 유입. 빠른 Na⁺ 상승은 <b>수축세포</b>'), stars=2), cols=2)

    qpage('PART 02', '전기 활동 ②',
        MC('Which TWO statements correctly describe the action potential of cardiac contractile cells? <b>(Choose two.)</b>', '심장 수축세포의 활동전위를 옳게 설명한 것 두 개는?',
           [('Contractile cells have a stable resting potential of about −90 mV and depolarize rapidly to about +30 mV when voltage-gated Na⁺ channels open.', '수축세포는 약 −90 mV의 안정된 휴지막전위를 가지며, 전압개폐 Na⁺ 채널이 열리면 약 +30 mV까지 빠르게 탈분극한다.'),
            ('The plateau phase is maintained by slow influx of Ca²⁺ through L-type channels together with a marked decrease in K⁺ permeability.', '고원기는 L형 채널을 통한 느린 Ca²⁺ 유입과 K⁺ 투과도의 뚜렷한 감소로 유지된다.'),
            ('Because the refractory period is very short, successive action potentials can summate and produce tetanus in cardiac muscle.', '불응기가 매우 짧아 연속된 AP가 가중되어 심장근에 강축을 일으킬 수 있다.'),
            ('Contractile cells lack a resting potential and slowly drift toward threshold through funny channels between beats.', '수축세포는 휴지막전위가 없고 박동 사이에 funny 채널을 통해 역치 쪽으로 천천히 움직인다.'),
            ('All of the Ca²⁺ required for contraction enters the cytosol from the extracellular fluid, so the sarcoplasmic reticulum is not involved.', '수축에 필요한 Ca²⁺는 모두 세포외액에서 들어오므로 근소포체는 관여하지 않는다.')], '①, ②',
           W('① ✔ −90 → Na⁺ → +30', '② ✔ 고원기 = Ca²⁺ 유입 + K⁺ ↓', '③ ✗ 불응기가 <b>매우 길어</b> 강축이 <b>없다</b>', '④ ✗ 설명은 <b>박동조율(자동능) 세포</b>', '⑤ ✗ ECF Ca²⁺는 소량, 대부분은 <b>SR</b>에서 (CICR)'), pick=2, stars=2),
        BOX('Fill in blanks (1)–(10) with the most appropriate words from the box. Not all words are used.', '상자에서 알맞은 단어를 골라 빈칸 (1)~(10)을 채우시오. 쓰지 않는 단어도 있다.',
            ['funny channels', 'T-type Ca²⁺', 'L-type Ca²⁺', 'K⁺', 'SA node', 'AV node', 'bundle of His', 'Purkinje fibers', 'P wave', 'QRS complex', 'T wave', 'calmodulin'],
            'In autorhythmic cells, hyperpolarization opens <u>(1)</u>, and then <u>(2)</u> channels bring the membrane to threshold. The rising phase is produced by <u>(3)</u> channels, and repolarization by opening of <u>(4)</u> channels. Excitation starts in the <u>(5)</u>, is delayed about 100 ms in the <u>(6)</u>, and then travels rapidly through the <u>(7)</u> and the <u>(8)</u>. On the ECG, atrial depolarization appears as the <u>(9)</u>, and ventricular depolarization as the <u>(10)</u>.',
            ['funny channels', 'T-type Ca²⁺', 'L-type Ca²⁺', 'K⁺', 'SA node', 'AV node', 'bundle of His', 'Purkinje fibers', 'P wave', 'QRS complex'],
            W('함정: <b>T wave</b> = 심실 재분극, <b>calmodulin</b> = 평활근(8장)') + K('funny → T형 → L형 → K⁺', 'SA → AV → His → Purkinje', 'P · QRS'), stars=3), cols=2)

    page('PART 03', '심장 주기 — 네 단계 · 심음 · 압력-용적 고리',
        grid('1.15fr 1fr 1fr',
            col(card('🔄 네 단계 (좌심실 기준)', tbl(['단계', '판막', '부피·압력', 'ECG', '심음'], [
                    ['① 심실 충만', '방실판 <b>열림</b>', '부피 ↑, 끝에 <b>심방 수축</b>', '<b>P</b>', '—'],
                    ['② 등용적 수축', '<b>모두 닫힘</b>', '부피 같음, <b>압력 ↑</b>', '<b>QRS</b>', '<b>S1</b> 방실판'],
                    ['③ 박출', '반월판 <b>열림</b>', '부피 ↓', '<b>ST</b>', '—'],
                    ['④ 등용적 이완', '<b>모두 닫힘</b>', '부피 같음, <b>압력 ↓</b>', '<b>T</b>', '<b>S2</b> 반월판']]) +
                    '<p style="margin-top:1.4mm">수축기 = ②+③, 이완기 = ④+①. 판막이 열려 있으면 압력을 못 만들어 <b>둘 다 닫혀야</b> 함(교수님)</p>', 'tip'),
                card('⚠ 함정', '<ul><li>S1 = <b>방실판</b> 닫힘, S2 = <b>반월판</b> 닫힘 (열릴 땐 소리 없음)</li><li>등용적 = 부피 그대로 <b>압력만</b> 변화</li><li>좌우 심방·심실 수축은 <b>동시</b></li></ul>', 'warn')),
            col(img('c9-33', 'Wiggers 도표: ECG · 압력 · 용적 · 심음', '120mm')),
            col(card('📐 압력-용적 고리', '<b>EDV</b> 135 mL(이완기말) − <b>ESV</b> 65 mL(수축기말) = <b>SV 70 mL</b><br><b>EF = SV/EDV ≈ 52%</b><br>세로선 두 개 = 등용적 수축(오른쪽)·이완(왼쪽)', 'def'),
                img('c9-34-q', '좌심실 압력-용적 고리 (A·B·C는 9-③ 문제)', '64mm'))), 'Slides 30–34')

    page('PART 04', '심박출량 조절 — 심박수와 1회 박출량',
        grid('1fr 1.05fr 1fr',
            col(card('정의 — Cardiac output', '<b>심실 하나</b>가 <b>1분</b>에 내보내는 양 (한 번의 양 ✗, 두 심실 합 ✗)<br><span style="font-size:11pt"><b>CO = HR × SV</b></span> ≈ 70회 × 70 mL ≈ <b>5 L/분</b>', 'def'),
                card('💓 심박수 — 자율신경', tbl(['', '부교감 (미주신경)', '교감'], [['가는 곳', '<b>심방</b>(SA·AV)', '<b>심방 + 심실 + 정맥</b>'], ['전달물질·수용체', 'ACh → 무스카린 → <b>Gi</b>', 'NE → <b>β₁</b> → <b>Gs</b>'], ['cAMP', '↓', '↑'], ['HR', '↓', '↑'], ['심실 수축력', '<b>효과 거의 없음</b>', '↑']]) +
                    '<p style="margin-top:1.4mm">cAMP가 <b>funny 채널에 직접 결합</b> → 더 자주 열림 → HR ↑ / + PKA → L형 Ca²⁺ ↑<br>신경은 박동을 <b>시작하지 않는다</b> — 속도·강도만</p>', 'tip')),
            col(card('📏 1회 박출량 — 두 가지 조절', tbl(['', '내인성', '외인성'], [['무엇', '<b>EDV(전부하)</b>', '<b>교감신경 · E</b>'], ['기전', '길이-장력 = <b>프랭크-스탈링</b>', '① 정맥 수축 → 환류 ↑ ② <b>수축성 ↑</b>(Ca²⁺ ↑)'], ['그래프', '같은 곡선 따라 <b>오른쪽</b>', '곡선 자체가 <b>위로</b>']]), 'mint'),
                img('c9-39', '프랭크-스탈링: EDV ↑ → SV ↑ (최적 길이까지)', '52mm'),
                card('박출률 EF = SV / EDV', tbl(['', 'EDV', 'SV', 'ESV', 'EF'], [['정상', '135', '70', '65', '<b>51.9%</b>'], ['교감', '135', '100', '35', '<b>74.1%</b>'], ['교감+환류↑', '175', '140', '35', '<b>80.0%</b>']]))),
            col(img('c9-41', 'CO 조절 요약: HR(부교감 −, 교감 +) × SV(내인성 EDV, 외인성 교감)', '74mm'),
                card('🩸 관상순환 (9.5)', '<ul><li>방 안의 피는 못 씀(내피가 막고 벽이 두꺼움) → <b>관상동맥</b></li><li>수축기엔 눌림 + 대동맥판이 입구를 가림 → <b>70%가 이완기</b></li><li>수요 ↑ → ATP → <b>아데노신</b>(측분비) → 확장</li><li>연료 = <b>지방산</b>(주), 포도당·젖산 — 무산소로는 부족</li><li>막힌 곳이 위쪽일수록 경색 범위가 넓음</li></ul>', 'why'))), 'Slides 35–45')

    qpage('PART 03–04', '심장 주기 · 심박출량 ①',
        FQ('c9-34-q', 'The figure is the pressure–volume loop of the left ventricle. Name <b>A</b>, <b>B</b> and <b>C</b>, and state what happens at points 1, 4, 6 and 8.', '그림은 좌심실의 압력-용적 고리다. A·B·C의 이름과, 1·4·6·8 지점에서 일어나는 일을 쓰시오.',
           [('A', '수축기말 용적 ESV (65 mL)'), ('B', '1회 박출량 SV (70 mL)'), ('C', '이완기말 용적 EDV (135 mL)')],
           W('1 = 방실판 열림 · 4 = 방실판 닫힘(S1) · 6 = 대동맥판 열림 · 8 = 대동맥판 닫힘(S2)', '4→6 = 등용적 수축, 8→1 = 등용적 이완(세로선) / EF = 70/135 ≈ 52%') + K('EDV − ESV = SV', '세로선 = 등용적'), stars=3, h='50mm'),
        TF([('The first heart sound (S1) is produced by closure of the AV valves at the start of isovolumetric ventricular contraction.', '제1심음(S1)은 등용적 심실 수축이 시작될 때 방실판이 닫히며 난다.'),
            ('During isovolumetric contraction, the semilunar valves are open, so ventricular volume decreases while pressure rises.', '등용적 수축기에는 반월판이 열려 있어 압력이 오르는 동안 심실 용적이 줄어든다.'),
            ('Cardiac output is the volume of blood pumped by each ventricle per minute and equals heart rate multiplied by stroke volume.', '심박출량은 각 심실이 1분 동안 내보내는 혈액량이며 심박수와 1회 박출량의 곱이다.'),
            ('Parasympathetic stimulation markedly reduces ventricular contractility because the vagus nerve richly innervates the ventricular muscle.', '미주신경이 심실 근육에 풍부히 분포하므로 부교감 자극은 심실 수축력을 크게 줄인다.'),
            ('Most coronary blood flow occurs during diastole, because contracting myocardium compresses the coronary vessels during systole.', '수축기에는 수축하는 심근이 관상혈관을 누르므로 관상 혈류는 대부분 이완기에 흐른다.')],
           'T F T F T', W('(2) ✗ 등용적 = <b>모든 판막이 닫혀</b> 용적이 <b>변하지 않음</b>', '(4) ✗ 미주신경은 주로 <b>심방(SA·AV결절)</b> — 심실 수축력에는 효과가 거의 없음'), stars=2), cols=2)

    qpage('PART 04', '심박출량 ②',
        MC('Which TWO statements about the control of stroke volume are correct? <b>(Choose two.)</b>', '1회 박출량의 조절에 대한 설명으로 옳은 것 두 개는?',
           [('According to the Frank–Starling law, an increase in end-diastolic volume stretches cardiac muscle fibers and increases the stroke volume.', '프랭크-스탈링 법칙에 따르면 이완기말 용적이 늘면 심장근 섬유가 늘어나 1회 박출량이 증가한다.'),
            ('Sympathetic stimulation increases contractility by enhancing Ca²⁺ influx, so the heart ejects more blood at the same end-diastolic volume.', '교감 자극은 Ca²⁺ 유입을 늘려 수축성을 높이므로, 같은 이완기말 용적에서도 더 많은 피를 내보낸다.'),
            ('Increased venous return shifts the Frank–Starling curve upward, which is the definition of increased contractility.', '정맥 환류 증가는 프랭크-스탈링 곡선을 위로 이동시키며, 이것이 수축성 증가의 정의다.'),
            ('Parasympathetic stimulation is the main extrinsic factor that increases stroke volume through venoconstriction.', '부교감 자극은 정맥 수축을 통해 1회 박출량을 늘리는 주된 외인성 요인이다.'),
            ('The ejection fraction is calculated as end-systolic volume divided by stroke volume, and it falls during sympathetic stimulation.', '박출률은 수축기말 용적을 1회 박출량으로 나눈 값이며 교감 자극 때 감소한다.')], '①, ②',
           W('① ✔ 내인성', '② ✔ 외인성 — 곡선 자체가 위로', '③ ✗ 정맥 환류 ↑ = 같은 곡선 따라 <b>오른쪽</b>(EDV ↑). 위로 이동은 <b>수축성 ↑</b>', '④ ✗ SV를 조절하는 신경은 <b>교감</b>뿐', '⑤ ✗ EF = <b>SV/EDV</b>, 교감 시 <b>증가</b>(52 → 74%)'), pick=2, stars=3),
        MC('Which TWO statements explain how sympathetic stimulation increases heart rate? <b>(Choose two.)</b>', '교감 자극이 심박수를 높이는 기전을 옳게 설명한 것 두 개는?',
           [('Norepinephrine binds to β₁-adrenergic receptors coupled to a stimulatory G protein, raising cAMP in SA node cells.', '노르에피네프린이 자극성 G단백질과 연결된 β₁ 수용체에 붙어 SA결절 세포의 cAMP를 높인다.'),
            ('cAMP binds directly to funny channels and increases their opening, so the pacemaker potential reaches threshold sooner.', 'cAMP가 funny 채널에 직접 붙어 더 많이 열리게 하므로 박동조율 전위가 더 빨리 역치에 도달한다.'),
            ('Norepinephrine binds to muscarinic receptors and activates an inhibitory G protein that closes K⁺ channels.', '노르에피네프린이 무스카린 수용체에 붙어 K⁺ 채널을 닫는 억제성 G단백질을 활성화한다.'),
            ('Sympathetic nerves are required to initiate each heartbeat, because the SA node cannot fire without neural input.', 'SA결절은 신경 입력 없이 발화할 수 없으므로 교감신경이 매 박동을 시작하는 데 필요하다.'),
            ('Sympathetic stimulation lengthens the AV nodal delay so that the ventricles have more time to fill.', '교감 자극은 심실이 찰 시간을 더 주려고 AV결절 지연을 늘린다.')], '①, ②',
           W('① ✔ NE → β₁ → Gs → cAMP ↑', '② ✔ cAMP → funny 채널 ↑ (+ PKA → L형 Ca²⁺)', '③ ✗ 무스카린·Gi는 <b>ACh(부교감)</b>', '④ ✗ 신경은 박동을 <b>시작하지 않는다</b>', '⑤ ✗ 교감은 AV 지연을 <b>줄인다</b>'), pick=2, stars=2), cols=2)

    qpage('PART 02–04', '서술형',
        ES('Explain why cardiac muscle cannot be tetanized, describing the ionic basis of the plateau phase of the contractile-cell action potential.', '수축세포 활동전위 고원기의 이온 기전을 설명하고, 심장근에서 강축이 일어나지 않는 이유를 서술하시오.',
           '수축세포는 −90 mV에서 전압개폐 <b>Na⁺</b> 채널이 열려 +30 mV까지 빠르게 탈분극한 뒤, 일시적 K⁺ 유출로 잠깐 내려왔다가 <b>고원기</b>에 들어간다. 고원기는 느린 <b>L형 Ca²⁺ 채널</b>로 Ca²⁺가 계속 들어오고 <b>K⁺ 투과도가 크게 줄어</b> 수백 ms(약 250 ms) 동안 탈분극이 유지되는 시기다. 그래서 AP가 수축만큼 길고 <b>불응기</b>도 수축이 거의 끝날 때까지 이어진다. 수축 도중에는 다음 AP가 생길 수 없으므로 가중이나 강축이 일어나지 않고, 심장은 반드시 이완해 피를 다시 채울 수 있다.',
           K('Na⁺ 상승', 'L형 Ca²⁺ + K⁺ ↓ = 고원기', '긴 불응기', '이완해야 충만'), stars=3),
        ES('Describe how heart rate and stroke volume are regulated to change cardiac output, distinguishing intrinsic and extrinsic control of stroke volume.', '심박수와 1회 박출량이 어떻게 조절되어 심박출량을 바꾸는지, 1회 박출량의 내인성·외인성 조절을 구분해 서술하시오.',
           '<b>CO = HR × SV</b>. HR은 SA결절의 자발적 발화에 자율신경이 더해져 정해진다. 부교감(미주신경, ACh → 무스카린 → Gi → cAMP ↓)은 SA결절의 박동조율 전위를 느리게 해 HR ↓, 교감(NE → β₁ → Gs → cAMP ↑ → funny 채널·L형 Ca²⁺ ↑)은 HR ↑. SV의 <b>내인성</b> 조절은 <b>프랭크-스탈링 법칙</b>: 정맥 환류가 늘어 EDV(전부하)가 커지면 심장근이 늘어나 더 세게 수축해 SV가 커진다. <b>외인성</b> 조절은 교감신경·에피네프린으로, ① 정맥을 수축시켜 정맥 환류를 늘리고 ② Ca²⁺ 유입을 늘려 <b>수축성</b>을 높여 같은 EDV에서도 더 많이 내보낸다(곡선이 위로 이동, EF ↑). 부교감은 SV에 거의 영향이 없다.',
           K('CO = HR × SV', 'ACh·Gi vs NE·β₁·Gs', '프랭크-스탈링 = EDV', '수축성 = Ca²⁺', '부교감은 SV ✗'), stars=3), cols=2)

    memo([('🫀 구조', '좌·우 <b>같은 양</b>, 좌심실 고압<br>판막 = <b>압력 차</b>로 수동<br>S1 방실판 · S2 반월판<br>건삭 = 뒤집힘 방지<br>개재판 = 데스모솜 + 간극연접<br>섬유골격 = 전기 절연'),
          ('⚡ 전기', 'funny(Na⁺) → T형 → <b>L형 Ca²⁺</b> → K⁺<br>SA 70–80 · AV 40–60 · His·P 20–40<br>AV 지연 100 ms<br>수축세포 −90 → +30, <b>고원기</b><br>CICR: ECF 소량 → SR 대량<br>P · PR · QRS · ST · T'),
          ('🔄 주기', '충만(P) → 등용적 수축(QRS, S1) → 박출(ST) → 등용적 이완(T, S2)<br>EDV 135 · ESV 65 · SV 70<br>EF = SV/EDV ≈ 52%'),
          ('📈 CO', 'CO = HR × SV (1분, 심실 하나)<br>부교감: ACh·Gi → HR ↓ (SV ✗)<br>교감: NE·β₁·Gs·cAMP → funny ↑<br>내인성 = 프랭크-스탈링(EDV)<br>외인성 = 환류 ↑ + 수축성 ↑<br>관상 70% 이완기 · 아데노신')],
         '<ol><li>SA결절 상승기 = <b>Ca²⁺</b> (Na⁺ ✗)</li><li>S1 = <b>방실판</b>, S2 = <b>반월판</b></li><li>정맥 환류 ↑ = 곡선 <b>오른쪽</b>, 수축성 ↑ = 곡선 <b>위로</b></li></ol>',
         ['SA결절은 다른 자동능 조직보다 빨리 역치에 도달해 AP를 만들기 때문에 정상 박동조율기다.',
          '수축세포의 고원기는 L형 Ca²⁺ 유입과 K⁺ 투과도 감소로 유지되며, 긴 불응기 때문에 심장근에는 강축이 없다.',
          '프랭크-스탈링 법칙: 이완기말 용적(정맥 환류)이 늘면 심장근이 늘어나 1회 박출량이 증가한다.'])
