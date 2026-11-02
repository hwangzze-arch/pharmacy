from lib import *

def build():
    chapter(8, 'Muscle Physiology')
    c = CH['color']
    page('CHAPTER 8', 'Muscle Physiology — 한 장 지도',
        chev([('8.1 구조', '근절·필라멘트', '#a61e1e'), ('8.2 분자 기전', '교차다리·E-C 연결', c), ('8.3 역학', '연축·가중·강축', '#e03131'),
              ('8.4 대사', 'ATP·섬유 종류', '#c2410c'), ('8.5 운동 조절', '근방추·골지힘줄', '#9c2a4a'), ('8.6 평활·심장근', '칼모듈린·불응기', '#7a1f2b')]) +
        grid('1.05fr 1fr',
            card('한 줄 요약', '골격근 섬유의 <b>근절</b>에서 <span class="hy">마이오신이 ATP를 써서 액틴을 중앙으로 당기면</span> 필라멘트가 미끄러져 근절이 짧아진다. 스위치는 <span class="hp">Ca²⁺</span> — T세관을 타고 내려간 활동전위가 근소포체의 Ca²⁺를 풀고, Ca²⁺가 <b>트로포닌</b>에 붙는다. 힘은 <b>운동단위 동원</b>과 <b>자극 빈도</b>로, ATP는 <b>크레아틴 인산·산화적 인산화·해당과정</b>으로 채운다. 평활근은 <b>칼모듈린</b>, 심장근은 <b>긴 불응기</b>.', 'sum big'),
            col(card('🎯 강의에서 교수님이 강조한 것 (10/29 · 11/2 녹취)', '<ol><li>수축해도 <b>A대는 그대로</b>, H대·I대만 짧아짐 — 필라멘트 길이는 불변</li><li>마이오신이 액틴에서 <b>떨어지려면 새 ATP</b> → 없으면 <b>사후경직</b></li><li><b>이완에도 ATP</b> (SERCA 펌프)</li><li>용어: Twitch = <b>연축</b>, Tetanus = <b>강축</b> (슬라이드엔 경련·경직)</li><li>마무리 퀴즈: 필라멘트 구성 · Ca²⁺가 붙는 곳(트로포닌) · T세관</li></ol>', 'warn'),
                card('💡 숫자', '활동전위 <b>1~2 ms</b> · 수축·이완 각 <b>15~50 ms</b> · 머리 <b>45°</b> · 교차다리 <b>6방향</b> · 평활근 <b>약 3초</b> · ATP <b>30+</b> vs <b>2</b>', 'tip'))), 'Slides 1–47')

    page('PART 01', '근육의 세 종류 · 골격근의 계층 구조',
        grid('1fr 1.15fr 1fr',
            col(card('정의', 'Muscle(근육) = <b>수축 전문가</b>. 몸에서 가장 큰 조직 무리(체중의 약 50%)<br>수축으로 ① 몸 전체·부분의 <b>움직임</b> ② 외부 물체 조작 ③ 속 빈 장기 안 내용물 <b>밀어내기</b> ④ 장기 내용물 <b>비우기</b>', 'def'),
                card('🏠 항상성에서의 역할', '<ul><li><b>Skeletal(골격근)</b>: 뼈를 움직임 · 음식 얻기·씹기·삼키기·호흡(에너지) · <b>열 생산</b>(떨림) · 위험 회피</li><li><b>Smooth(평활근)</b>: 속 빈 장기·관의 벽 → 혈액·음식·공기·소변의 흐름, 눈</li><li><b>Cardiac(심장근)</b>: 심장 벽에만 → 혈액 펌프</li></ul>'),
                card('⚠ 수의근인데 무의식?', '골격근은 <b>수의근</b>으로 분류하지만, <b>자세·균형·리듬 운동·반사</b>처럼 <b>무의식적(subconscious)</b>으로 조절되는 활동도 많다', 'warn')),
            col(card('🆚 두 가지 분류 기준', tbl(['', 'Skeletal', 'Cardiac', 'Smooth'], [
                    ['구조', '<b>가로무늬</b> 있음', '<b>가로무늬</b> 있음', '<b>없음</b>(민무늬)'],
                    ['조절', '<b>수의</b>', '불수의', '불수의'],
                    ['신경', '<b>체성</b>신경', '<b>자율</b>신경', '<b>자율</b>신경'],
                    ['핵', '<b>여러 개</b>(다핵)', '1개', '1개'],
                    ['특징', '뼈에 붙음, 길쭉', '<b>개재판</b>, 가지침', '방추형, 속 빈 장기 벽']]) +
                '<p style="margin-top:1.6mm">🧠 가로무늬 = 골격근·심장근 / 수의 = <b>골격근뿐</b> / 자율신경 = 심장근·평활근</p>'),
                img('c8-07', '세 근육의 현미경 모습: 골격근 · 심장근 · 평활근', '52mm')),
            col(card('🧱 골격근의 계층', flow('Muscle 근육', 'Fascicle 근육다발', 'Muscle fiber 근섬유', 'Myofibril 근원섬유', 'Thick·Thin filament', small=True) +
                    '<ul><li><b>Muscle fiber</b> = 골격근 <b>세포 하나</b>, <b>다핵</b>, 미토콘드리아 많음</li><li><b>Fascicle</b> = 근섬유 다발, <b>perimysium(근다발막)</b>이 감쌈</li><li><b>Myofibril</b> = 굵은·가는 필라멘트가 규칙적으로 배열</li><li><b>Thick filament</b> = <b>myosin</b> / <b>Thin filament</b> = 주로 <b>actin</b></li><li><b>Sarcolemma</b> = 근섬유의 세포막 · <b>Tendon(힘줄)</b>이 근육을 뼈에 붙임</li></ul>', 'tip'),
                img('c8-08', '근육 → 근육다발 → 근섬유 → 근원섬유 → 필라멘트', '50mm'))), 'Slides 3–8')

    page('PART 01', '근절 — 가로무늬의 정체 · 마이오신과 액틴',
        grid('1.1fr 1fr 1fr',
            col(card('📏 띠(band) 이름 — 전자현미경', tbl(['구조', '정체', '밝기·수축 시'], [
                    ['<b>A band</b>', '<b>굵은 필라멘트 전체</b> + 겹치는 가는 필라멘트', '어두움 · <span class="hp">그대로</span>'],
                    ['<b>I band</b>', 'A대로 들어가지 않은 <b>가는 필라멘트만</b>', '밝음 · <b>짧아짐</b>'],
                    ['<b>H zone</b>', 'A대 가운데, 가는 필라멘트가 <b>닿지 않는</b> 곳', '<b>짧아짐/사라짐</b>'],
                    ['<b>M line</b>', 'H대 가운데 <b>지지 단백질</b> 선', '근절 중심'],
                    ['<b>Z line</b>', 'I대 가운데의 진한 세로선, 가는 필라멘트가 붙음', '서로 <b>가까워짐</b>'],
                    ['<b>Sarcomere</b>', '<b>Z선~Z선</b> = 골격근의 <b>기능 단위</b>', '<b>짧아짐</b>']]) +
                '<p style="margin-top:1.4mm">가로무늬 = 정렬된 근절들의 <b>A대·I대가 반복</b>되어 생김</p>'),
                img('c8-17', '이완(위) vs 수축(아래): H대·I대 짧아짐, A대 그대로', '46mm')),
            col(card('🧬 Myosin — 굵은 필라멘트', '<ul><li>굵은 필라멘트 하나 = 마이오신 <b>수백 개</b></li><li>마이오신 = 똑같은 <b>골프채 모양</b> 소단위 2개, 꼬리끼리 꼬이고 둥근 <b>머리</b>가 바깥으로</li><li><b>경첩 2곳</b>: 목(neck), 꼬리 중간</li><li>머리 = <b>Cross bridge(교차다리)</b>: <span class="hy">Actin-binding site</span> + <span class="hy">Myosin ATPase site</span>(ATP 분해)</li><li>교차다리는 굵은 필라멘트에서 <b>6방향</b>으로 가는 필라멘트를 향해 튀어나옴</li></ul>'),
                card('🌀 Titin', 'Z선 → M선 → Z선을 잇는 <b>거대한 탄성 단백질</b> 한 가닥<ul><li><b>Scaffold(뼈대)</b>: 굵은 필라멘트 위치 고정</li><li><b>Spring(용수철)</b>: 근육 탄성 ↑</li><li><b>신호 전달</b>: 근력운동 → 근육 비대</li></ul>', 'why')),
            col(card('🔗 Actin — 가는 필라멘트', '<ul><li>둥근 액틴 분자가 <b>두 가닥 진주 목걸이</b>처럼 꼬인 뼈대</li><li>각 액틴에 <b>마이오신 결합 부위</b></li><li>액틴 + 교차다리 결합 → 수축</li></ul><b>조절 단백질</b> (이완 상태에서 수축을 막음)<ul><li><b>Tropomyosin</b>: 액틴의 결합 부위를 <span class="hp">덮어 가림</span></li><li><b>Troponin</b>: 세 부분이 각각 <b>tropomyosin · actin · Ca²⁺</b>에 결합</li></ul>', 'mint'),
                img('c8-13', '이완: 트로포마이오신이 가림 → 흥분: Ca²⁺가 트로포닌에 결합 → 결합 부위 노출', '62mm'))), 'Slides 8–13')

    qpage('PART 01', '근육의 종류 · 근절 구조',
        FQ('c8-17-q', 'The figure shows a relaxed sarcomere. Identify the structures labeled <b>A</b> to <b>H</b>.', '그림은 이완 상태의 근절이다. A~H가 가리키는 구조의 이름을 쓰시오.',
            [('A', '근절 Sarcomere'), ('B', 'Z선 Z line'), ('C', 'H대 H zone'), ('D', 'I대(명대) I band'), ('E', 'A대(암대) A band'), ('F', 'M선 M line'), ('G', '굵은 필라멘트(마이오신) Thick filament'), ('H', '가는 필라멘트(액틴) Thin filament')],
            W('A는 <b>Z선에서 Z선까지</b> = 근절. D(I대)는 가운데에 Z선이 있고 가는 필라멘트만 있는 곳, E(A대)는 굵은 필라멘트의 길이 전체.', 'C(H대)는 A대 가운데 가는 필라멘트가 닿지 않는 틈, F(M선)는 그 정중앙.') + K('Z선~Z선', 'A대 = 굵은 필라멘트 길이', 'I대 = 가는 필라멘트만'), stars=3, h='46mm'),
        TF([('Skeletal and cardiac muscles are striated, whereas smooth muscle lacks striations because its thick and thin filaments are not arranged in sarcomeres.', '골격근과 심장근은 가로무늬가 있지만, 평활근은 굵은·가는 필라멘트가 근절로 배열되지 않아 가로무늬가 없다.'),
            ('The A band is the region occupied only by thin filaments, which is why it appears light under the electron microscope.', 'A대는 가는 필라멘트만 있는 부분이라 전자현미경에서 밝게 보인다.'),
            ('A sarcomere, the functional unit of skeletal muscle, is defined as the area between two adjacent M lines.', '골격근의 기능 단위인 근절은 인접한 두 M선 사이의 부위로 정의된다.'),
            ('Titin is a giant elastic protein that runs from the Z line to the M line, stabilizing the thick filaments and increasing muscle elasticity.', '티틴은 Z선에서 M선까지 이어진 거대한 탄성 단백질로 굵은 필라멘트를 고정하고 근육의 탄성을 높인다.'),
            ('Troponin has three binding portions, one each for tropomyosin, actin, and Ca²⁺.', '트로포닌은 트로포마이오신·액틴·Ca²⁺에 각각 결합하는 세 부분을 가진다.')],
           'T F F T T', W('(2) ✗ 가는 필라멘트만 있어 <b>밝은</b> 곳은 <b>I대</b>. A대는 굵은 필라멘트 전체(+겹치는 가는 필라멘트)라 <b>어둡다</b>',
                          '(3) ✗ 근절은 <b>Z선과 Z선</b> 사이. M선은 근절의 정중앙'), stars=2), cols=2)

    qpage('PART 01', '필라멘트 · 근육의 분류',
        MC('Which TWO statements correctly describe the proteins that make up the thick and thin filaments of skeletal muscle? <b>(Choose two.)</b>', '골격근의 굵은·가는 필라멘트를 이루는 단백질을 옳게 설명한 문장 두 개는?',
           [('Each myosin molecule consists of two identical golf-club-shaped subunits whose globular heads form the cross bridges and contain both an actin-binding site and a myosin ATPase site.', '마이오신 분자는 골프채 모양의 똑같은 소단위 두 개로 되어 있고, 둥근 머리가 교차다리를 이루며 액틴 결합 부위와 마이오신 ATPase 부위를 모두 가진다.'),
            ('The thin filament is composed mainly of myosin, while actin serves only as a regulatory protein that covers the binding sites in relaxed muscle.', '가는 필라멘트는 주로 마이오신으로 되어 있고, 액틴은 이완된 근육에서 결합 부위를 덮는 조절 단백질일 뿐이다.'),
            ('In a relaxed muscle fiber, tropomyosin lies over the sites on actin that bind cross bridges, physically preventing myosin from attaching to actin.', '이완된 근섬유에서 트로포마이오신은 액틴의 교차다리 결합 부위를 덮어 마이오신이 액틴에 붙지 못하게 막는다.'),
            ('Calcium binds directly to tropomyosin, which then pulls troponin away from the binding sites located on the myosin heads.', '칼슘은 트로포마이오신에 직접 결합하고, 트로포마이오신이 마이오신 머리에 있는 결합 부위에서 트로포닌을 끌어낸다.'),
            ('Cross bridges project from each thin filament in six directions toward the surrounding thick filaments.', '교차다리는 각 가는 필라멘트에서 주변의 굵은 필라멘트를 향해 6방향으로 튀어나온다.')], '①, ③',
           W('① ✔ 마이오신 머리 = 교차다리, 액틴 결합 부위 + ATPase 부위', '② ✗ 가는 필라멘트의 주성분이 <b>액틴</b>, 굵은 필라멘트가 마이오신. 결합 부위를 덮는 것은 <b>트로포마이오신</b>',
             '③ ✔ 이완 상태 = 트로포마이오신이 가림', '④ ✗ Ca²⁺는 <b>트로포닌</b>에 붙고, 결합 부위는 마이오신이 아니라 <b>액틴</b>에 있다', '⑤ ✗ 교차다리는 <b>굵은</b> 필라멘트(마이오신)에서 가는 필라멘트를 향해 나온다'), pick=2, stars=2),
        MC('Which TWO statements about the three types of muscle and the organization of skeletal muscle are correct? <b>(Choose two.)</b>', '세 종류의 근육과 골격근의 구조에 대한 설명으로 옳은 것 두 개는?',
           [('Skeletal muscle is classified as voluntary, yet much of its activity, such as posture, balance, and reflexes, is also under subconscious involuntary control.', '골격근은 수의근으로 분류되지만 자세·균형·반사 같은 많은 활동은 무의식적인 불수의 조절도 받는다.'),
            ('Cardiac and smooth muscles are innervated by the somatic nervous system, which is why they contract only when we consciously decide to move.', '심장근과 평활근은 체성신경계의 지배를 받으므로 우리가 의식적으로 움직이려 할 때만 수축한다.'),
            ('A fascicle is a single multinucleated muscle cell that is surrounded by the sarcolemma and attached directly to bone without any tendon.', '근육다발은 근섬유막에 싸인 다핵 근육 세포 하나로, 힘줄 없이 뼈에 직접 붙는다.'),
            ('A skeletal muscle fiber is a single multinucleated cell containing many mitochondria and myofibrils made of regularly arranged thick and thin filaments.', '골격근 섬유는 미토콘드리아가 많은 다핵 세포 하나이며, 굵은·가는 필라멘트가 규칙적으로 배열된 근원섬유를 가진다.'),
            ('Smooth muscle is found mainly in the walls of the heart, where its intercalated discs allow the heart to pump blood throughout the body.', '평활근은 주로 심장 벽에 있으며, 개재판 덕분에 심장이 온몸으로 혈액을 펌프질한다.')], '①, ④',
           W('① ✔ 수의근이지만 자세·균형·리듬 운동·반사는 무의식 조절', '② ✗ 심장근·평활근은 <b>자율</b>신경계 지배, <b>불수의</b>근',
             '③ ✗ 세포 하나 = <b>근섬유</b>. 근육다발은 근섬유들을 <b>근다발막(perimysium)</b>이 감싼 다발이고, 근육은 <b>힘줄</b>로 뼈에 붙는다', '④ ✔ 근섬유 = 다핵 세포, 근원섬유 = 필라멘트 배열',
             '⑤ ✗ 심장 벽·개재판은 <b>심장근</b>. 평활근은 속 빈 장기·혈관·관의 벽'), pick=2, stars=1), cols=2)

    page('PART 02', '활주 필라멘트 기전 · 교차다리 주기',
        grid('1fr 1.15fr 1fr',
            col(card('정의 — Sliding filament mechanism', '근절 양쪽의 <b>가는 필라멘트</b>가 굵은 필라멘트 사이로 <b>A대 중앙 쪽으로 미끄러져</b> 들어감 → <b>Z선이 서로 가까워짐</b> → 근절이 짧아짐', 'def'),
                card('📐 수축 시 변화', tbl(['구조', '변화'], [['근절 · Z–Z 거리', '<b>짧아짐</b>'], ['I대', '<b>짧아짐</b>'], ['H대', '<b>짧아짐/사라짐</b>'], ['A대', '<span class="hp"><b>그대로</b></span>'], ['굵은·가는 필라멘트 길이', '<span class="hp"><b>그대로</b></span>']]) +
                    '<p style="margin-top:1.4mm">⚠ 짧아지는 것은 <b>근절</b>이지 <b>필라멘트(단백질)</b>가 아니다 — 교수님 강조</p>', 'warn'),
                card('🚣 Power stroke (마이오신 하나 수준)', '<ul><li>노 젓기처럼 가는 필라멘트를 <b>근절 중앙</b> 쪽으로 당김</li><li>마이오신 머리 2개 중 <b>하나만</b> 액틴에 붙어 <b>45°</b> 안쪽으로 기울어짐 → 떨어짐 → 원래 각도 → 반복</li><li>마이오신 = 가는 필라멘트를 따라 "걷는" <b>모터 단백질</b></li><li>모든 마이오신이 <b>동시에 움직이지 않음</b>: 일부는 붙잡고 일부는 떨어져 부드럽게 당김(밧줄 당기기)</li></ul>')),
            col(card('🔄 교차다리 주기 (ATP-powered cross-bridge cycling)', '<ol><li><b>Energized(장전)</b>: 마이오신 ATPase가 ATP → <b>ADP + Pi</b>. <span class="hy">액틴에 붙기 <b>전에</b> 분해</span> → 에너지가 마이오신에 저장(고에너지 마이오신, 머리가 꺾여 장전)</li><li><b>Binding(결합)</b>: 흥분 → Ca²⁺ 방출 → 트로포닌·트로포마이오신이 비켜남 → 마이오신이 액틴에 결합</li><li><b>Bending(힘내기, power stroke)</b>: 결합으로 머리가 굽음 → 액틴을 중앙으로 당김. <b>Pi는 도중에, ADP는 끝난 뒤</b> 떨어짐</li><li><b>Detachment(분리)</b>: <span class="hy">새 ATP가 붙어야</span> 액틴–마이오신 친화력 ↓ → 떨어짐 → 머리가 원래 모양 → ATP 분해 → 반복</li></ol>', 'tip'),
                card('☠ Rigor mortis (사후경직)', '죽으면 <b>ATP가 만들어지지 않음</b> → 마이오신이 액틴에 <b>붙은 채 떨어지지 못함</b>(rigor complex) → 근육이 뻣뻣하게 굳음<br>즉, ATP는 <b>당길 때</b>뿐 아니라 <b>떼어낼 때</b>도 필요', 'warn')),
            col(img('c8-23', '교차다리 주기: 장전 → 결합 → 굽힘(파워 스트로크) → 분리 / ATP 없으면 사후경직', '84mm'),
                img('c8-18', '파워 스트로크: 결합 → 굽힘 → 분리 → 다시 결합', '42mm'))), 'Slides 16–24')

    page('PART 02', '흥분-수축 연결 · 이완 · 잠복기',
        grid('1fr 1fr 1fr',
            col(card('⚡ Excitation-contraction coupling (흥분-수축 연결)', '<ol><li>신경근 접합부(NMJ)에서 <b>ACh</b> 방출 (7장)</li><li>근섬유막(<b>sarcolemma</b>) 전체에 <b>활동전위</b> 전도</li><li><b>T tubule(T세관)</b>: <b>A대와 I대의 경계</b>에서 근섬유막이 안으로 파고든 관 → 세포막과 이어져 AP가 <b>깊숙이</b> 전파</li><li>T세관의 AP → <b>근소포체(SR)</b>의 투과성 변화</li><li>SR의 <b>lateral sacs(측면 주머니)</b>가 저장한 <b>Ca²⁺를 세포질로 방출</b></li><li>Ca²⁺ + <b>troponin</b> → tropomyosin이 비켜남 → 교차다리 주기</li></ol><p>Ca²⁺가 있는 동안 교차다리 형성 계속 (<b>주기마다 ATP 1개</b>)</p>', 'tip'),
                card('🧱 Sarcoplasmic reticulum', '<b>변형된 활면소포체</b> — 각 근원섬유를 <b>그물 소매</b>처럼 감쌈 (A대·I대마다)<br><b>Lateral sacs</b> = 쉴 때 Ca²⁺ 저장, T세관과 맞닿음', 'def')),
            col(card('😌 Relaxation (이완)', '<ol><li>NMJ의 <b>AChE(아세틸콜린에스터레이스)</b>가 ACh 제거 → AP가 더 이상 안 생김</li><li><b>SERCA 펌프</b>(Sarco/endoplasmic reticulum Ca²⁺-ATPase)가 <span class="hy">ATP를 써서</span> Ca²⁺를 lateral sacs로 되돌림</li><li>트로포닌·트로포마이오신이 다시 결합 부위를 덮음 → 마이오신이 액틴에 못 붙음</li></ol>', 'mint'),
                card('⏱ 시간 — 슬라이드 수치', tbl(['단계', '시간·이유'], [
                    ['Action potential', '<b>1~2 ms</b> (아주 짧음)'],
                    ['Latent period (잠복기)', 'AP 뒤 <b>Ca²⁺ 방출·교차다리 활성화</b>에 시간이 걸림'],
                    ['Contraction time', '<b>15~50 ms</b> (최대 장력까지)'],
                    ['Relaxation time', '<b>15~50 ms</b> (Ca²⁺를 SR로 다 퍼 올려야)']]) +
                    '<p style="margin-top:1.4mm">수축이 AP보다 훨씬 길어 <b>가중</b>이 가능 (PART 03)</p>'),
                img('c8-25', 'AP(1~2 ms) vs 근연축: 잠복기 → 수축 → 이완', '34mm')),
            col(img('c8-26', '흥분-수축 연결 전체 과정: ACh → AP → T세관 → SR Ca²⁺ → 트로포닌 → 교차다리 → SERCA로 이완', '128mm'))), 'Slides 20–27')

    qpage('PART 02', '활주 · 교차다리 · 흥분-수축 연결 ①',
        TF([('During contraction, the A band keeps the same width while the H zone and I band become shorter as thin filaments slide toward the center of the A band.', '수축 중 가는 필라멘트가 A대 중앙 쪽으로 미끄러지면서 A대 너비는 그대로이고 H대와 I대는 짧아진다.'),
            ('Muscle contraction occurs because the thick and thin filaments themselves become shorter during each power stroke.', '근수축은 파워 스트로크마다 굵은·가는 필라멘트 자체가 짧아지기 때문에 일어난다.'),
            ('ATP is split by the myosin ATPase before the cross bridge binds to actin, so the energy is stored in a high-energy form of myosin.', 'ATP는 교차다리가 액틴에 붙기 전에 마이오신 ATPase에 의해 분해되어, 에너지가 고에너지 형태의 마이오신에 저장된다.'),
            ('During the power stroke, ADP is released first, and inorganic phosphate is released only after the stroke has been completed.', '파워 스트로크 중 ADP가 먼저 떨어지고, 무기인산은 스트로크가 끝난 뒤에야 떨어진다.'),
            ('Rigor mortis develops after death because, without fresh ATP, the myosin cross bridges cannot detach from actin.', '사후경직은 새 ATP가 없어 마이오신 교차다리가 액틴에서 떨어지지 못하기 때문에 생긴다.')],
           'T F T F T', W('(2) ✗ 필라멘트 길이는 <b>그대로</b>. 서로 겹치는 부분이 늘어 <b>근절</b>이 짧아질 뿐', '(4) ✗ 반대 — <b>Pi는 스트로크 도중</b>, <b>ADP는 끝난 뒤</b>에 떨어진다'), stars=2),
        BOX('Fill in blanks (1)–(10) with the most appropriate words from the box. Not all words are used.', '상자에서 가장 알맞은 단어를 골라 빈칸 (1)~(10)을 채우시오. 쓰지 않는 단어도 있다.',
            ['acetylcholine', 'sarcolemma', 'T tubule', 'Ca²⁺', 'lateral sacs', 'troponin', 'tropomyosin', 'cross bridges', 'acetylcholinesterase', 'SERCA', 'calmodulin', 'myoglobin'],
            'When <u>(1)</u> is released at the neuromuscular junction, an action potential spreads over the <u>(2)</u> and down the <u>(3)</u>. This triggers the release of <u>(4)</u> from the <u>(5)</u> of the sarcoplasmic reticulum. Ca²⁺ binds to <u>(6)</u>, which shifts <u>(7)</u> away from the binding sites on actin, so that energized myosin forms <u>(8)</u>. Relaxation begins when <u>(9)</u> breaks down ACh and the <u>(10)</u> pump uses ATP to return Ca²⁺ to the sarcoplasmic reticulum.',
            ['acetylcholine', 'sarcolemma', 'T tubule', 'Ca²⁺', 'lateral sacs', 'troponin', 'tropomyosin', 'cross bridges', 'acetylcholinesterase', 'SERCA'],
            W('해석: ACh 방출 → 근섬유막 → T세관으로 AP → SR 측면 주머니에서 Ca²⁺ → 트로포닌 → 트로포마이오신 이동 → 교차다리 → AChE가 ACh 분해, SERCA가 Ca²⁺ 회수', '함정: <b>calmodulin</b>은 <b>평활근</b>, <b>myoglobin</b>은 산소 저장 단백질') + K('ACh', 'T세관', 'lateral sacs', '트로포닌', 'SERCA'), stars=3), cols=2)

    qpage('PART 02', '활주 · 교차다리 · 흥분-수축 연결 ②',
        MC('Which TWO statements about excitation–contraction coupling and relaxation in skeletal muscle are correct? <b>(Choose two.)</b>', '골격근의 흥분-수축 연결과 이완에 대한 설명으로 옳은 것 두 개는?',
           [('T tubules are invaginations of the sarcolemma at the junction of the A and I bands, so that an action potential can spread deep into the interior of the muscle fiber.', 'T세관은 A대와 I대 경계에서 근섬유막이 안으로 파고든 것이어서 활동전위가 근섬유 깊숙이 퍼질 수 있다.'),
            ('Calcium for skeletal muscle contraction enters mainly from the extracellular fluid through voltage-gated channels in the sarcolemma.', '골격근 수축에 쓰이는 칼슘은 주로 근섬유막의 전압개폐 통로를 통해 세포외액에서 들어온다.'),
            ('Relaxation is a passive process that requires no ATP, because Ca²⁺ simply diffuses back into the sarcoplasmic reticulum.', '이완은 ATP가 필요 없는 수동 과정으로, Ca²⁺가 근소포체로 저절로 확산되어 돌아간다.'),
            ('Cross-bridge cycling continues as long as Ca²⁺ remains bound to troponin and ATP is available for each cycle.', 'Ca²⁺가 트로포닌에 붙어 있고 주기마다 쓸 ATP가 있는 한 교차다리 주기는 계속된다.'),
            ('The latent period occurs because the action potential in a muscle fiber lasts much longer than the resulting twitch.', '잠복기는 근섬유의 활동전위가 그로 인한 연축보다 훨씬 오래 지속되기 때문에 생긴다.')], '①, ④',
           W('① ✔ T세관 = A·I대 경계의 근섬유막 함입', '② ✗ 골격근의 Ca²⁺는 <b>근소포체(lateral sacs)</b>에서 나온다', '③ ✗ <b>SERCA 펌프</b>가 ATP를 써서 능동수송 — 이완에도 ATP 필요',
             '④ ✔ Ca²⁺ + ATP가 있는 동안 반복', '⑤ ✗ AP는 <b>1~2 ms</b>로 연축보다 훨씬 <b>짧다</b>. 잠복기는 Ca²⁺ 방출·교차다리 활성화에 걸리는 시간'), pick=2, stars=2),
        MC('Which TWO statements correctly explain the roles of ATP in the cross-bridge cycle? <b>(Choose two.)</b>', '교차다리 주기에서 ATP의 역할을 옳게 설명한 것 두 개는?',
           [('Hydrolysis of ATP at the myosin ATPase site energizes, or cocks, the myosin head before it attaches to actin.', '마이오신 ATPase 부위에서 ATP가 가수분해되어 마이오신 머리가 액틴에 붙기 전에 에너지를 얻는다(장전된다).'),
            ('The binding of a new ATP molecule to myosin lowers the affinity between actin and myosin, allowing the cross bridge to detach.', '새 ATP가 마이오신에 결합하면 액틴과 마이오신의 친화력이 낮아져 교차다리가 떨어질 수 있다.'),
            ('ATP is needed only for the power stroke; detachment of myosin from actin happens automatically once the stroke is finished.', 'ATP는 파워 스트로크에만 필요하고, 스트로크가 끝나면 마이오신은 저절로 액틴에서 떨어진다.'),
            ('In the absence of ATP, myosin heads remain detached from actin, which is why muscles become soft and flaccid after death.', 'ATP가 없으면 마이오신 머리가 액틴에서 떨어진 채로 있어 죽은 뒤 근육이 말랑하게 늘어진다.'),
            ('ATP binds to troponin and moves tropomyosin away from the myosin-binding sites on actin, which starts contraction.', 'ATP가 트로포닌에 결합해 트로포마이오신을 액틴의 마이오신 결합 부위에서 치워 수축을 시작한다.')], '①, ②',
           W('① ✔ 분해는 결합 <b>전</b> — 장전', '② ✔ 새 ATP = 분리 스위치', '③ ✗ 떨어지는 데에도 <b>새 ATP</b>가 필요(교수님 강조)',
             '④ ✗ 반대 — ATP가 없으면 <b>붙은 채</b> 굳는다 = <b>사후경직</b>', '⑤ ✗ 트로포닌에 붙어 결합 부위를 여는 것은 <b>Ca²⁺</b>'), pick=2, stars=2), cols=2)

    page('PART 03', '골격근 역학 — 힘줄 · 지렛대 · 힘의 조절',
        grid('1fr 1fr 1.1fr',
            col(card('🪢 Series-elastic component (SEC, 직렬탄성요소)', '<ul><li>장력은 <b>근절</b>에서 만들어져 <b>힘줄</b>을 거쳐 뼈로 전달된 뒤 뼈가 움직임</li><li>근섬유와 <b>직렬</b>로 놓인 힘줄(+티틴) = <b>용수철</b>: 탄성 에너지를 저장·방출 → 힘·효율 ↑</li><li>힘줄이 <b>충격 흡수</b>, 걷기·달리기의 대사 비용 ↓, 급히 늘어날 때 근육 <b>보호</b></li></ul>', 'def'),
                card('🦾 Origin vs Insertion', tbl(['', '뜻'], [['<b>Origin</b> (기시점)', '<b>덜 움직이는(고정된)</b> 뼈 쪽 끝'], ['<b>Insertion</b> (정지점)', '<b>움직이는</b> 뼈 쪽 끝']]) +
                    '<p style="margin-top:1.4mm">수축하면 정지점이 기시점 쪽으로 당겨짐<br>굴곡(flexion) = <b>이두근</b> 수축 / 신전(extension) = <b>삼두근</b> 수축 → 서로 반대로 작용(주동근 ↔ 길항근)</p>'),
                img('c8-29', '팔꿈치 굴곡(이두근) · 신전(삼두근)', '40mm')),
            col(card('⚡ Twitch (연축)', '<b>근섬유 하나</b>에서 <b>활동전위 하나</b>가 만드는 <b>짧고 약한</b> 수축<br><small>슬라이드는 "경련", 교수님은 <b>연축</b>으로 부름</small>', 'tip'),
                card('📈 근육 전체 장력 = ① × ②', '<ol><li><b>수축하는 근섬유의 수</b> = 몇 개의 <b>motor unit(운동단위)</b>을 <b>동원(recruit)</b>하느냐</li><li><b>근섬유 하나의 장력</b> = 자극 <b>빈도</b>(가중·강축)</li></ol><b>Motor unit</b> = 척수의 운동뉴런 <b>1개</b> + 그 뉴런이 지배하는 <b>근섬유 전부</b>'),
                card('🔍 동원의 규칙 (11/2 강의 영상)', '<ul><li><b>Size principle(크기의 원리)</b>: 약한 자극 → <b>작은</b> 운동단위 먼저 → 강할수록 큰 운동단위 → 약한 힘을 <b>정밀하게</b> 조절</li><li><b>Asynchronous recruitment(비동기 동원)</b>: 같은 힘을 오래 낼 때 운동단위들이 <b>번갈아</b> 수축 → 힘은 일정, 피로 ↓</li></ul>', 'why')),
            col(card('➕ Summation → Tetanus', '<ul><li><b>Twitch summation(연축 가중)</b>: <span class="hy">완전히 이완하기 <b>전에</b></span> 다시 자극 → 두 번째 수축이 더해져 장력 ↑ (<b>세포질 Ca²⁺가 높게 유지</b>)</li><li><b>Tetanus(강축)</b>: 이완할 틈 없이 매우 빠르게 자극 → <b>최대·지속</b> 수축 (장력 고원)</li><li>이유: SERCA가 Ca²⁺를 SR로 되돌릴 <b>시간이 없음</b></li></ul>', 'mint'),
                img('c8-31', '(a) 가중 없음 (b) 연축 가중 (c) 강축 → 자극 중단·피로', '56mm'),
                card('⚠ 강축은 정상', '임상의 Tetanus = <b>파상풍</b>(병)이지만, 생리학의 강축은 자세 유지·무거운 물건 들기에 쓰는 <b>정상 수축</b>. 계속되면 젖산 등이 쌓여 <b>피로</b>', 'warn'))), 'Slides 28–31')

    qpage('PART 03', '골격근 역학 ①',
        FQ('c8-31-q', 'The graph shows contractile responses of a skeletal muscle fiber to different frequencies of stimulation. Name the responses or events labeled <b>A</b> to <b>D</b>.', '그래프는 자극 빈도에 따른 골격근 섬유의 수축 반응이다. A~D가 가리키는 반응(또는 사건)의 이름을 쓰시오.',
            [('A', '단일 연축 Single twitch'), ('B', '연축 가중 Twitch summation'), ('C', '강축 Tetanus'), ('D', '자극 중단 또는 피로 시작 Stimulation ceases or fatigue begins')],
            W('A: 완전히 이완한 뒤 다시 자극 → 같은 크기의 연축 두 번(가중 없음)', 'B: 이완 <b>전</b> 재자극 → 더해져 커짐', 'C: 이완할 틈이 없는 빠른 자극 → 최대 지속 수축', 'D: 장력이 떨어지기 시작하는 곳') + K('이완 전 재자극', '세포질 Ca²⁺ 유지', '최대 지속 수축'), stars=2, h='44mm'),
        TF([('A twitch is a brief, weak contraction produced by a single action potential in a muscle fiber.', '연축은 근섬유에서 활동전위 하나가 만드는 짧고 약한 수축이다.'),
            ('Twitch summation occurs when a muscle fiber is restimulated after it has completely relaxed, so that the second twitch is added to the first.', '연축 가중은 근섬유가 완전히 이완한 뒤 다시 자극될 때 두 번째 연축이 첫 번째에 더해져 일어난다.'),
            ('In physiology, tetanus refers to a maximal sustained contraction that occurs when a fiber is stimulated so rapidly that it has no time to relax.', '생리학에서 강축은 근섬유가 이완할 틈 없이 매우 빠르게 자극될 때 생기는 최대 지속 수축을 말한다.'),
            ('According to the size principle, large motor units are recruited first so that weak contractions can be produced quickly.', '크기의 원리에 따르면 약한 수축을 빠르게 만들기 위해 큰 운동단위가 먼저 동원된다.'),
            ('The insertion is the end of a muscle attached to the more stationary part of the skeleton, while the origin is attached to the part that moves.', '정지점은 골격의 덜 움직이는 부분에 붙은 근육 끝이고, 기시점은 움직이는 부분에 붙은 끝이다.')],
           'T F T F F', W('(2) ✗ 완전히 이완한 <b>뒤</b>면 같은 크기의 연축(가중 없음). 가중은 이완하기 <b>전</b> 재자극', '(4) ✗ <b>작은</b> 운동단위가 먼저 → 약한 힘을 정밀 조절',
                          '(5) ✗ 반대 — 고정된 쪽 = <b>기시점(origin)</b>, 움직이는 쪽 = <b>정지점(insertion)</b>'), stars=2), cols=2)

    qpage('PART 03', '골격근 역학 ②',
        MC('Which TWO mechanisms allow the nervous system to increase the tension developed by a whole skeletal muscle? <b>(Choose two.)</b>', '신경계가 골격근 전체의 장력을 높이는 방법 두 가지는?',
           [('Recruiting a greater number of motor units so that more muscle fibers within the muscle contract at the same time.', '더 많은 운동단위를 동원해 근육 안에서 더 많은 근섬유가 동시에 수축하게 한다.'),
            ('Increasing the amplitude of each action potential in the motor neuron, because action potentials are graded according to stimulus strength.', '활동전위는 자극 세기에 따라 크기가 달라지므로 운동뉴런의 각 활동전위 크기를 키운다.'),
            ('Increasing the frequency of stimulation so that successive twitches summate because cytosolic Ca²⁺ remains elevated between action potentials.', '자극 빈도를 높여 활동전위 사이에 세포질 Ca²⁺가 높게 유지되므로 연축들이 가중되게 한다.'),
            ('Shortening the thick and thin filaments within each sarcomere so that every cross bridge can pull with a greater force.', '각 근절 안의 굵은·가는 필라멘트를 짧게 만들어 교차다리마다 더 큰 힘으로 당기게 한다.'),
            ('Stimulating the Golgi tendon organs, which directly excite the motor neurons of the same muscle to produce a maximal contraction.', '골지힘줄기관을 자극해 같은 근육의 운동뉴런을 직접 흥분시켜 최대 수축을 일으킨다.')], '①, ③',
           W('① ✔ 운동단위 동원(근섬유 수)', '② ✗ 활동전위는 <b>실무율</b> — 크기를 키울 수 없다', '③ ✔ 빈도 ↑ → 가중 → 강축(근섬유당 장력)',
             '④ ✗ 필라멘트 길이는 변하지 않는다', '⑤ ✗ 골지힘줄기관은 장력이 지나치면 <b>이완 반사</b>를 일으킨다'), pick=2, stars=2),
        MC('Which TWO statements about motor units and the mechanics of skeletal muscle are correct? <b>(Choose two.)</b>', '운동단위와 골격근 역학에 대한 설명으로 옳은 것 두 개는?',
           [('A motor unit consists of one motor neuron from the spinal cord together with all of the muscle fibers that it innervates.', '운동단위는 척수의 운동뉴런 하나와 그 뉴런이 지배하는 모든 근섬유로 이루어진다.'),
            ('Each skeletal muscle fiber is innervated by several motor neurons, so a single fiber belongs to many different motor units.', '골격근 섬유 하나는 여러 운동뉴런의 지배를 받으므로 한 근섬유가 여러 운동단위에 속한다.'),
            ('The series-elastic component, mainly the tendons, behaves like a spring that absorbs shock and transmits tension from the sarcomeres to the bone.', '직렬탄성요소(주로 힘줄)는 용수철처럼 충격을 흡수하고 근절의 장력을 뼈로 전달한다.'),
            ('During a sustained contraction, the same motor units must remain active the entire time, which is why holding a cup for a minute quickly causes fatigue.', '지속 수축 중에는 같은 운동단위가 내내 활동해야 하므로 컵을 1분만 들어도 금방 피로해진다.'),
            ('Tetanus is common in cardiac muscle because its long refractory period allows successive action potentials to summate.', '심장근은 긴 불응기 덕분에 연속된 활동전위가 가중되므로 강축이 흔하다.')], '①, ③',
           W('① ✔ 운동뉴런 1 + 근섬유 전부', '② ✗ 근섬유 하나에는 <b>NMJ가 하나</b> — 한 운동단위에만 속한다(7장)', '③ ✔ 힘줄 = 용수철·완충·전달',
             '④ ✗ 운동단위들이 <b>번갈아(비동기)</b> 활동해 힘을 일정하게 유지하고 피로를 줄인다', '⑤ ✗ 긴 불응기는 강축을 <b>막는다</b>'), pick=2, stars=2), cols=2)

    page('PART 04', '골격근 대사 — ATP는 어디에 쓰고 어디서 오나',
        grid('1fr 1.1fr 1fr',
            col(card('🔋 ATP가 쓰이는 4곳', '<ol><li><b>Myosin ATPase</b>가 ATP 분해 → 파워 스트로크 에너지</li><li><b>새 ATP 결합</b> → 교차다리 분리</li><li>이완 때 Ca²⁺를 lateral sacs로 <b>능동수송</b> (SERCA)</li><li>활동전위 뒤 <b>Na⁺–K⁺ 펌프</b></li></ol><p>ATP = 이 일들의 <b>유일한 직접</b> 에너지원. 근육에 저장된 ATP는 <b>운동 처음 몇 초</b>분뿐</p>', 'def'),
                card('🧭 쓰는 순서', flow('저장 ATP', '크레아틴 인산', '산화적 인산화 (O₂ 있음)', '해당과정 (O₂ 부족)', small=True) + '근섬유는 포도당을 <b>glycogen(글리코겐)</b>으로 저장', 'sum')),
            col(card('⚙ ATP를 보충하는 3가지 경로', tbl(['경로', '특징'], [
                    ['<b>Creatine phosphate</b><br><small>크레아틴 인산</small>', '<b>첫 번째</b> 에너지 저장고. <b>creatine kinase</b>가 Pi를 ADP에 넘겨 <b>즉시</b> ATP. 쉴 때는 반대로 ATP로 충전'],
                    ['<b>Oxidative phosphorylation</b><br><small>산화적 인산화</small>', '<b>미토콘드리아</b>, <b>O₂ 필요</b>, 지방산·포도당 사용. 다단계라 <b>느림</b>, 포도당당 <b>30개 이상</b> ATP. <b>Myoglobin</b>이 혈액의 O₂를 받아 저장'],
                    ['<b>Glycolysis</b><br><small>해당과정 (무산소)</small>', 'O₂가 없을 때 주 경로. <b>빠름</b>, 포도당 → 피루브산 2 + <b>ATP 2</b>. 피루브산은 산화적 인산화로, O₂ 없으면 <b>젖산(lactate)</b>']]) +
                '<p style="margin-top:1.4mm">🧠 속도: 크레아틴 인산 &gt; 해당과정 &gt; 산화적 인산화 / 효율: 산화적 인산화 ≫ 해당과정</p>', 'tip')),
            col(img('c8-34', '수축·이완 중 ATP 공급: 크레아틴 인산 · 산화적 인산화 · 해당과정', '90mm'))), 'Slides 33–34')

    page('PART 04', '골격근 섬유의 세 종류',
        grid('1.35fr 1fr',
            card('🧪 Table 8-1 — 속도(slow/fast) × 대사(산화/해당)', tbl(['특성', 'Slow-oxidative<br>Type I', 'Fast-oxidative<br>Type IIa', 'Fast-glycolytic<br>Type IIx'], [
                    ['Myosin ATPase 활성', '낮음', '<b>높음</b>', '<b>높음</b>'], ['수축 속도', '느림', '빠름', '빠름'],
                    ['피로 저항성', '<b>높음</b>', '중간', '<b>낮음</b>'], ['산화적 인산화 능력', '높음', '높음', '낮음'],
                    ['해당 효소', '낮음', '중간', '<b>높음</b>'], ['미토콘드리아 · 모세혈관', '많음', '많음', '적음'],
                    ['Myoglobin', '높음', '높음', '낮음'], ['색', '<b>적색</b>', '적색', '<b>백색</b>'], ['Glycogen', '낮음', '중간', '<b>높음</b>'],
                    ['쓰임 (녹취)', '자세 유지·하체·지구력', '중간', '팔·빠르고 강한 힘']])),
            col(card('⚡ 빠른 섬유가 빠른 이유', flow('Myosin ATPase 활성 ↑', 'ATP 빨리 분해', '교차다리 주기 빠름', '빠른 연축', small=True), 'mint'),
                card('🔴 적색근 vs ⚪ 백색근', '<b>Oxidative fiber</b> = <b>red fiber</b>: 미토콘드리아·마이오글로빈(빨간색)이 많아 유산소 ATP 생산 ↑, 젖산 축적 ↓ → <b>피로에 강함</b><br><b>Glycolytic fiber</b> = 글리코겐·해당 효소가 많음, 젖산이 쌓여 <b>빨리 지침</b><br><small>교수님: 섬유 비율은 사람마다 유전적으로 달라 잘하는 운동이 다름</small>'),
                img('c8-37', '빠른 연축 vs 느린 연축 · 단면의 세 섬유', '62mm'))), 'Slides 35–37')

    qpage('PART 04', '대사 · 섬유 종류 ①',
        BOX('Fill in blanks (1)–(10) with the most appropriate words from the box. Not all words are used.', '상자에서 가장 알맞은 단어를 골라 빈칸 (1)~(10)을 채우시오. 쓰지 않는 단어도 있다.',
            ['creatine phosphate', 'creatine kinase', 'oxidative phosphorylation', 'glycolysis', 'myoglobin', 'mitochondria', 'lactate', 'pyruvate', 'glycogen', 'Na⁺–K⁺ pump', 'calmodulin', 'troponin'],
            'At the onset of exercise, stored ATP and <u>(1)</u> are used first, because the enzyme <u>(2)</u> immediately transfers a phosphate to ADP. When enough O₂ is present, ATP is produced in the <u>(3)</u> by <u>(4)</u>, which yields more than 30 ATP per glucose, and <u>(5)</u> stores O₂ delivered from the blood. When O₂ is lacking, <u>(6)</u> rapidly converts glucose into two molecules of <u>(7)</u> and 2 ATP, and <u>(8)</u> is produced. Muscle fibers store glucose in the form of <u>(9)</u>. Besides myosin ATPase and the SERCA pump, the <u>(10)</u> also consumes ATP to restore ion gradients after action potentials.',
            ['creatine phosphate', 'creatine kinase', 'mitochondria', 'oxidative phosphorylation', 'myoglobin', 'glycolysis', 'pyruvate', 'lactate', 'glycogen', 'Na⁺–K⁺ pump'],
            W('해석: 크레아틴 인산 → 크레아틴 키나아제 / 미토콘드리아의 산화적 인산화(30+ ATP), 마이오글로빈이 O₂ 저장 / O₂ 부족 → 해당과정: 피루브산 2 + ATP 2, 젖산 / 글리코겐 저장 / Na⁺–K⁺ 펌프도 ATP 사용', '함정: calmodulin·troponin은 대사와 무관') + K('크레아틴 인산', '산화적 인산화', '해당과정', '마이오글로빈', '젖산'), stars=2),
        TF([('Fast fibers contract quickly because their myosin ATPase activity is higher than that of slow fibers, so they split ATP faster.', '빠른 섬유는 마이오신 ATPase 활성이 느린 섬유보다 높아 ATP를 빨리 분해하므로 빠르게 수축한다.'),
            ('Slow-oxidative (type I) fibers contain few mitochondria and little myoglobin, so they appear white and fatigue easily.', '느린 산화 섬유(Type I)는 미토콘드리아와 마이오글로빈이 적어 하얗게 보이고 쉽게 피로해진다.'),
            ('Fast-glycolytic (type IIx) fibers store large amounts of glycogen and glycolytic enzymes but fatigue rapidly as lactate accumulates.', '빠른 해당 섬유(Type IIx)는 글리코겐과 해당 효소가 많지만 젖산이 쌓여 빨리 피로해진다.'),
            ('Oxidative phosphorylation produces ATP faster than glycolysis because it involves fewer reaction steps.', '산화적 인산화는 반응 단계가 더 적어 해당과정보다 ATP를 빨리 만든다.'),
            ('Creatine phosphate is the first energy store used during exercise because it can immediately donate its phosphate to ADP.', '크레아틴 인산은 인산을 ADP에 즉시 줄 수 있어 운동 중 가장 먼저 쓰이는 에너지 저장고다.')],
           'T F T F T', W('(2) ✗ Type I은 미토콘드리아·마이오글로빈이 <b>많아</b> <b>적색</b>이고 <b>피로에 강하다</b> — 설명은 Type IIx', '(4) ✗ 산화적 인산화는 <b>다단계</b>라 <b>느리다</b>. 빠른 쪽은 해당과정(대신 ATP 2개뿐)'), stars=2), cols=2)

    qpage('PART 04', '대사 · 섬유 종류 ②',
        MC('Which TWO statements correctly compare the three types of skeletal muscle fibers? <b>(Choose two.)</b>', '골격근 섬유의 세 종류를 옳게 비교한 것 두 개는?',
           [('Slow-oxidative fibers are well suited to prolonged, low-intensity activity such as maintaining posture, because they have a high capacity for aerobic ATP production.', '느린 산화 섬유는 유산소 ATP 생산 능력이 높아 자세 유지 같은 오래 지속되는 저강도 활동에 알맞다.'),
            ('Fast-glycolytic fibers are red because they contain the highest concentration of myoglobin among the three fiber types.', '빠른 해당 섬유는 세 종류 중 마이오글로빈 농도가 가장 높아 빨간색이다.'),
            ('Fast-oxidative (type IIa) fibers have high myosin ATPase activity and intermediate resistance to fatigue, showing properties between the other two types.', '빠른 산화 섬유(Type IIa)는 마이오신 ATPase 활성이 높고 피로 저항성은 중간으로, 나머지 두 종류의 중간 성질을 보인다.'),
            ('Glycolytic fibers resist fatigue better than oxidative fibers, because glycolysis yields more ATP per glucose molecule than oxidative phosphorylation.', '해당과정이 산화적 인산화보다 포도당당 ATP를 더 많이 만들므로 해당 섬유가 산화 섬유보다 피로에 강하다.'),
            ('All three fiber types have the same speed of contraction and differ only in the color of their fibers.', '세 섬유 모두 수축 속도는 같고 섬유의 색만 다르다.')], '①, ③',
           W('① ✔ Type I = 지구력·자세', '② ✗ 빠른 해당 섬유는 마이오글로빈이 <b>적어 백색</b>', '③ ✔ Type IIa = 중간형',
             '④ ✗ 해당과정은 포도당당 <b>2 ATP</b>, 산화적 인산화는 <b>30+</b>. 피로에 강한 쪽은 <b>산화</b> 섬유', '⑤ ✗ 속도(마이오신 ATPase 활성)와 대사 방식이 다르다'), pick=2, stars=2),
        MC('Which TWO statements about ATP use and ATP supply in skeletal muscle are correct? <b>(Choose two.)</b>', '골격근의 ATP 사용과 공급에 대한 설명으로 옳은 것 두 개는?',
           [('ATP is the only energy source that can be used directly by the myosin ATPase, the SERCA pump, and the Na⁺–K⁺ pump.', 'ATP는 마이오신 ATPase, SERCA 펌프, Na⁺–K⁺ 펌프가 직접 쓸 수 있는 유일한 에너지원이다.'),
            ('Muscle fibers store enough ATP to support several minutes of intense exercise without using any other pathway.', '근섬유는 다른 경로 없이도 몇 분 동안 격렬한 운동을 할 수 있을 만큼 ATP를 저장한다.'),
            ('Myoglobin in oxidative fibers transfers and stores O₂ delivered from the blood for use in oxidative phosphorylation.', '산화 섬유의 마이오글로빈은 혈액에서 온 O₂를 받아 저장해 산화적 인산화에 쓰게 한다.'),
            ('Glycolysis requires oxygen and takes place in the mitochondria, producing more than 30 ATP per glucose molecule.', '해당과정은 산소가 필요하고 미토콘드리아에서 일어나며 포도당당 30개 이상의 ATP를 만든다.'),
            ('During exercise, creatine kinase converts ATP into creatine phosphate, consuming the cell\'s ATP to power contraction.', '운동 중 크레아틴 키나아제는 ATP를 크레아틴 인산으로 바꾸며 세포의 ATP를 소모해 수축에 쓴다.')], '①, ③',
           W('① ✔ ATP = 유일한 직접 에너지원', '② ✗ 저장 ATP는 <b>처음 몇 초</b>분뿐', '③ ✔ 마이오글로빈 = 근육의 O₂ 저장',
             '④ ✗ 설명은 <b>산화적 인산화</b>. 해당과정은 <b>O₂ 불필요</b>, ATP <b>2개</b>', '⑤ ✗ 운동 중에는 크레아틴 인산 → ADP로 인산을 넘겨 <b>ATP를 만든다</b>. ATP로 충전하는 것은 <b>쉴 때</b>'), pick=2, stars=2), cols=2)

    page('PART 05', '운동 조절 · 근육 수용기',
        grid('1fr 1fr 1.05fr',
            col(card('🎮 운동의 세 종류', tbl(['종류', '뜻 · 통합 중추'], [
                    ['<b>Reflex</b> (반사)', '의식 없이 자동으로 일어나는 골격근 수축 — <b>척수</b>(척수 반사) 또는 <b>뇌간</b>(뇌신경 반사)'],
                    ['<b>Voluntary</b> (수의 운동)', '복잡한 정보를 <b>대뇌피질</b>이 통합'],
                    ['<b>Rhythmic</b> (리듬 운동)', '걷기·씹기: <b>의식적으로 시작</b>, 의식 없이 <b>유지</b> (녹취: 척수·뇌간의 중추패턴발생기)']])),
                card('📥 운동뉴런으로 들어오는 입력', '<ul><li><b>구심성 뉴런</b> → 척수 반사</li><li><b>일차운동피질</b>의 <b>피라미드 세포</b>가 명령 (5장)</li><li><b>뇌간</b>: 운동피질·<b>소뇌</b>·<b>기저핵</b>(불필요한 움직임 억제)·구심성 뉴런의 입력을 받아 <span class="hy">고위 운동 중추와 골격근 수축을 잇는 마지막 연결</span></li></ul>', 'tip')),
            col(card('정의 — Proprioceptor (고유수용기)', '운동을 명령하기 전 CNS는 몸의 <b>시작 위치</b>를 알아야 함 → 근육·힘줄·관절의 감각신경 말단이 <b>움직임·자세·장력</b>을 감지해 근육 <b>길이</b>와 <b>장력</b> 정보를 계속 보냄', 'def'),
                card('🆚 Muscle spindle vs Golgi tendon organ', tbl(['', 'Muscle spindle<br>근방추', 'Golgi tendon organ<br>골지힘줄기관'], [
                    ['위치', '<b>근육 안</b>, 근섬유와 나란히', '<b>힘줄</b> 안'],
                    ['구조', '<b>Intrafusal fibers</b>(방추 속근) + 1차·2차 구심성 말단', '<b>콜라겐</b> 섬유 + 구심성 말단'],
                    ['감지', '근육 <b>길이·늘어남</b>', '근육 <b>장력</b>의 변화'],
                    ['반사', '길이 조절 반사(신장 반사)', '<b>반사적 이완</b> → 손상 방지']]) +
                    '<p style="margin-top:1.4mm">🧠 <b>방추 = 길이</b>, <b>힘줄 = 힘(장력)</b>. 일반 근섬유 = <b>extrafusal</b>(방추 외근)</p>', 'mint')),
            col(img('c8-41', '(a) 근방추: 방추 속근 + 구심성 말단 (b) 골지힘줄기관: 힘줄 속 콜라겐 + 구심성 섬유', '120mm'))), 'Slides 39–41')

    page('PART 06', '평활근과 심장근',
        grid('1fr 1fr 1fr',
            col(card('정의 — Smooth muscle', '세 근육 모두 <b>액틴·마이오신</b> 수축 장치와 <b>교차다리에 ATP</b>를 쓴다. 평활근 세포는<ul><li><b>작고 가로무늬 없음</b> — 근절 대신 필라멘트가 <b>dense bodies(치밀체)</b>에 사선으로 고정</li><li>위치: 속 빈 장기·혈관·관의 벽(소화·호흡·비뇨·생식관, 눈)</li><li><b>느리지만 경제적</b>: 한 번 수축 <b>약 3초</b> → ATP 덜 씀</li></ul>', 'def'),
                card('🔑 Ca²⁺ 스위치가 다르다', flow('세포질 Ca²⁺ ↑', '<b>Calmodulin</b> 결합', '<b>MLCK</b> 활성', '마이오신 경쇄 <b>인산화</b>', '교차다리 주기', small=True) +
                    '평활근은 <b>트로포닌이 없다</b> → Ca²⁺ 의존 <b>마이오신 인산화</b>로 켜짐<br><small>MLCK = Myosin light-chain kinase(마이오신 경쇄 키나아제)</small>', 'warn'),
                card('🔗 Single-unit smooth muscle', '<b>Gap junction</b>으로 연결 → AP가 퍼져 <b>한 덩어리로</b> 수축 · 뉴런 없이 <b>스스로 흥분</b>(self-excitable, 페이스메이커)', 'mint')),
            col(img('c8-43', '평활근 vs 골격근의 흥분-수축 연결: 칼모듈린 → MLCK vs 트로포닌', '50mm'),
                img('c8-44', '단일단위 평활근: 간극연접으로 함께 수축', '50mm')),
            col(card('❤ Cardiac muscle — 골격근 + 평활근의 혼합', tbl(['닮은 쪽', '특징'], [
                    ['골격근처럼', '<b>가로무늬</b>(근절), <b>troponin·tropomyosin</b>, 미토콘드리아·마이오글로빈·T세관·SR 많음'],
                    ['평활근처럼', '짧고 가늘다, 외부 자극 없이 <b>스스로 AP</b>, <b>intercalated disc(개재판)</b> 속 <b>gap junction</b>, <b>자율</b>신경 지배'],
                    ['심장근만', '<span class="hy"><b>긴 불응기</b> → 강축(tetanus)이 일어나지 않음</span>']])),
                card('왜 심장엔 강축이 없어야 하나', '심장은 <b>수축 → 이완(혈액 채우기)</b>를 반복해야 펌프가 된다. 불응기가 길어 수축이 끝나기 전에는 다음 AP가 생기지 않으므로 가중·강축이 불가능', 'why'))), 'Slides 43–46')

    page('PART 06', '세 근육 비교표 — 시험 직전 한 장',
        grid('1.5fr 1fr',
            card('📋 Skeletal vs Cardiac vs Smooth (Slide 46)', tbl(['', 'Skeletal', 'Cardiac', 'Smooth'], [
                    ['수축 기전', '활주 필라멘트', '활주 필라멘트', '활주 필라멘트'],
                    ['핵', '<b>여러 개</b>', '1개', '1개'],
                    ['신경 지배', '<b>체성</b>', '자율', '자율'],
                    ['조절', '수의 + 무의식', '불수의', '불수의'],
                    ['수축 개시', '<b>신경성</b>(neurogenic)', '<b>근원성</b>(myogenic)', '대부분 근원성'],
                    ['간극연접', '없음', '<b>있음</b>(개재판)', '<b>있음</b>'],
                    ['수축·이완 속도', '<b>빠름</b>', '느림, 자가흥분, 리듬', '<b>매우 느림</b>, 자가흥분, 리듬'],
                    ['Ca²⁺의 역할', '<b>트로포닌·트로포마이오신</b>', '<b>트로포닌·트로포마이오신</b>', '<b>칼모듈린 → MLCK</b>'],
                    ['T세관', '있음', '있음', '<b>없음</b>'],
                    ['근소포체', '잘 발달', '잘 발달', '<b>빈약</b>'],
                    ['가로무늬', '있음', '있음', '<b>없음</b>'],
                    ['필라멘트 배열', '근절', '근절', '흩어짐, <b>치밀체</b>에 고정'],
                    ['위치', '골격', '심장 벽', '속 빈 장기·혈관 벽']])),
            col(img('c8-07', '골격근(다핵·가로무늬) · 심장근(개재판) · 평활근(방추형)', '74mm'),
                card('🧠 세 줄로 외우기', '<ol><li>Ca²⁺가 붙는 곳: 골격·심장 = <b>트로포닌</b>, 평활 = <b>칼모듈린</b></li><li>강축: 골격근 <b>가능(정상)</b>, 심장근 <b>불가</b>(긴 불응기)</li><li>스스로 AP: 심장근·단일단위 평활근 (<b>간극연접</b>)</li></ol>', 'sum'))), 'Slides 46–47')

    qpage('PART 05–06', '운동 조절 · 평활근 · 심장근 ①',
        FQ('c8-41-q', 'The figure shows two types of muscle receptors. Identify the structures labeled <b>A</b> to <b>F</b>.', '그림은 두 종류의 근육 수용기다. A~F가 가리키는 구조의 이름을 쓰시오.',
            [('A', '방추 속근 섬유 Intrafusal (spindle) muscle fibers'), ('B', '골지힘줄기관 Golgi tendon organ'), ('C', '방추 외근(일반) 섬유 Extrafusal muscle fibers'), ('D', '구심성 뉴런 축삭 Afferent neuron axons'), ('E', '힘줄 Tendon'), ('F', '근방추 Muscle spindle (그림 (a) 전체)')],
            W('근방추(F)는 근육 <b>안</b>에서 길이·늘어남을, 골지힘줄기관(B)은 <b>힘줄(E)</b> 안에서 장력을 감지한다. 구심성 축삭(D)이 정보를 척수로 보낸다.') + K('근방추 = 길이', '골지힘줄기관 = 장력', 'intrafusal vs extrafusal'), stars=3, h='56mm'),
        TF([('Muscle spindles monitor muscle length and stretch, whereas Golgi tendon organs located in tendons detect changes in muscle tension.', '근방추는 근육 길이와 늘어남을, 힘줄 안의 골지힘줄기관은 근육 장력의 변화를 감지한다.'),
            ('When excessive tension is detected, Golgi tendon organs trigger a reflex that strengthens the contraction of the same muscle.', '장력이 지나치면 골지힘줄기관은 같은 근육의 수축을 더 세게 하는 반사를 일으킨다.'),
            ('The brain stem serves as the final link between higher motor centers and skeletal muscle contraction, receiving input from the motor cortex, cerebellum, and basal nuclei.', '뇌간은 운동피질·소뇌·기저핵의 입력을 받아 고위 운동 중추와 골격근 수축을 잇는 마지막 연결 역할을 한다.'),
            ('Smooth muscle contraction is switched on when Ca²⁺ binds to troponin, exactly as it is in skeletal muscle.', '평활근 수축은 골격근과 똑같이 Ca²⁺가 트로포닌에 결합할 때 켜진다.'),
            ('Cardiac muscle cannot be tetanized because its long refractory period prevents successive contractions from summating.', '심장근은 긴 불응기 때문에 연속된 수축이 가중되지 못해 강축이 일어나지 않는다.')],
           'T F T F T', W('(2) ✗ 골지힘줄기관은 근육을 <b>이완</b>시키는 반사를 일으켜 손상을 막는다', '(4) ✗ 평활근에는 <b>트로포닌이 없다</b> — Ca²⁺ + <b>칼모듈린</b> → MLCK → 마이오신 인산화'), stars=2), cols=2)

    qpage('PART 05–06', '운동 조절 · 평활근 · 심장근 ②',
        MC('Which TWO statements about smooth muscle are correct? <b>(Choose two.)</b>', '평활근에 대한 설명으로 옳은 것 두 개는?',
           [('Smooth muscle cells are small and unstriated because their thick and thin filaments are anchored to dense bodies rather than organized into sarcomeres.', '평활근 세포는 굵은·가는 필라멘트가 근절이 아니라 치밀체에 고정되어 있어 작고 가로무늬가 없다.'),
            ('In smooth muscle, Ca²⁺ binds to calmodulin, and the Ca²⁺–calmodulin complex activates myosin light-chain kinase, which phosphorylates myosin.', '평활근에서는 Ca²⁺가 칼모듈린에 결합하고, Ca²⁺–칼모듈린 복합체가 마이오신 경쇄 키나아제를 활성화해 마이오신을 인산화한다.'),
            ('Smooth muscle contracts faster than skeletal muscle and therefore consumes much more ATP during each contraction.', '평활근은 골격근보다 빨리 수축하므로 수축할 때마다 ATP를 훨씬 많이 쓴다.'),
            ('Single-unit smooth muscle cells cannot generate action potentials without input from motor neurons of the somatic nervous system.', '단일단위 평활근 세포는 체성신경계 운동뉴런의 입력 없이는 활동전위를 만들 수 없다.'),
            ('Smooth muscle has well-developed T tubules and sarcoplasmic reticulum, just like skeletal and cardiac muscle.', '평활근은 골격근·심장근처럼 T세관과 근소포체가 잘 발달해 있다.')], '①, ②',
           W('① ✔ 치밀체 → 근절·가로무늬 없음', '② ✔ 칼모듈린 → MLCK → 마이오신 경쇄 인산화', '③ ✗ <b>느리지만 경제적</b>(한 번 약 3초, ATP 덜 씀)',
             '④ ✗ 간극연접으로 연결되고 뉴런 없이 <b>스스로 흥분</b>한다(자율신경 지배)', '⑤ ✗ 평활근은 T세관 <b>없음</b>, 근소포체 <b>빈약</b>'), pick=2, stars=2),
        MC('Which TWO features does cardiac muscle share with smooth muscle rather than with skeletal muscle? <b>(Choose two.)</b>', '심장근이 골격근보다 평활근과 공유하는 특징 두 개는?',
           [('Cardiac muscle cells are joined by intercalated discs that contain gap junctions, allowing action potentials to spread rapidly from cell to cell.', '심장근 세포는 간극연접이 있는 개재판으로 연결되어 활동전위가 세포에서 세포로 빠르게 퍼진다.'),
            ('Cardiac muscle can initiate action potentials on its own without external influence, showing self-excitable pacemaker activity.', '심장근은 외부 자극 없이 스스로 활동전위를 시작하는 자가흥분성(페이스메이커 활동)을 보인다.'),
            ('Contraction of cardiac muscle is regulated by Ca²⁺ binding to troponin, which moves tropomyosin away from the binding sites on actin.', '심장근 수축은 Ca²⁺가 트로포닌에 결합해 트로포마이오신을 액틴 결합 부위에서 치우는 방식으로 조절된다.'),
            ('Cardiac muscle shows a highly organized banding pattern of thick and thin filaments arranged in sarcomeres, which produces striations.', '심장근은 굵은·가는 필라멘트가 근절로 정렬된 띠 무늬가 있어 가로무늬가 보인다.'),
            ('Cardiac muscle is innervated by the somatic nervous system, so its contraction is mainly under voluntary control.', '심장근은 체성신경계의 지배를 받아 수축이 주로 수의적으로 조절된다.')], '①, ②',
           W('① ✔ 간극연접(평활근과 공유)', '② ✔ 스스로 AP(평활근과 공유)', '③ ✗ 트로포닌 조절은 <b>골격근</b>과 공유',
             '④ ✗ 가로무늬·근절도 <b>골격근</b>과 공유', '⑤ ✗ 심장근은 <b>자율</b>신경, <b>불수의</b>'), pick=2, stars=3), cols=2)

    qpage('PART 05–06', '운동 조절 · 평활근 · 심장근 ③',
        BOX('Fill in blanks (1)–(10) with the most appropriate words from the box. Not all words are used.', '상자에서 가장 알맞은 단어를 골라 빈칸 (1)~(10)을 채우시오. 쓰지 않는 단어도 있다.',
            ['sarcomeres', 'dense bodies', 'Ca²⁺', 'calmodulin', 'troponin', 'myosin light-chain kinase', 'phosphorylation', 'gap junctions', 'intercalated discs', 'refractory period', 'tropomyosin', 'T tubules'],
            'Smooth muscle has no <u>(1)</u>; instead, its thick and thin filaments are anchored to <u>(2)</u>. When cytosolic <u>(3)</u> rises, it binds to <u>(4)</u> instead of <u>(5)</u>. This complex activates <u>(6)</u>, which causes <u>(7)</u> of the myosin light chain so that cross bridges can cycle. In single-unit smooth muscle, <u>(8)</u> allow action potentials to spread, so the cells contract as a unit. Cardiac muscle cells are linked by <u>(9)</u>, and their long <u>(10)</u> prevents tetanus.',
            ['sarcomeres', 'dense bodies', 'Ca²⁺', 'calmodulin', 'troponin', 'myosin light-chain kinase', 'phosphorylation', 'gap junctions', 'intercalated discs', 'refractory period'],
            W('해석: 근절 없음 → 치밀체 / Ca²⁺ → 트로포닌 대신 칼모듈린 → MLCK → 마이오신 경쇄 인산화 / 간극연접 → 한 덩어리 수축 / 심장근: 개재판, 긴 불응기 → 강축 없음', '함정: tropomyosin, T tubules는 평활근에 없다(또는 해당 없음)') + K('칼모듈린', 'MLCK', '인산화', '간극연접', '긴 불응기'), stars=3),
        MC('Which TWO statements about the control of motor movement are correct? <b>(Choose two.)</b>', '운동 조절에 대한 설명으로 옳은 것 두 개는?',
           [('Reflexes are automatic responses produced by skeletal muscle contraction without conscious effort and are integrated in the spinal cord or brain stem.', '반사는 의식적인 노력 없이 일어나는 골격근 수축 반응이며 척수나 뇌간에서 통합된다.'),
            ('Voluntary movements are ordered by pyramidal cells in the primary motor cortex, which integrates complex information before commands reach motor neurons.', '수의 운동은 복잡한 정보를 통합하는 일차운동피질의 피라미드 세포가 명령하고, 명령이 운동뉴런으로 전달된다.'),
            ('Rhythmic activities such as walking and chewing must be consciously controlled by the cerebral cortex at every single step.', '걷기·씹기 같은 리듬 운동은 매 순간 대뇌피질이 의식적으로 조절해야 한다.'),
            ('Proprioceptors are found only in the inner ear and provide no information about the length or tension of skeletal muscles.', '고유수용기는 내이에만 있고 골격근의 길이나 장력에 대한 정보는 주지 않는다.'),
            ('Muscle spindles are located within tendons, where they detect the amount of tension produced by the contracting muscle.', '근방추는 힘줄 안에 있어 수축하는 근육이 만드는 장력을 감지한다.')], '①, ②',
           W('① ✔ 반사 = 척수·뇌간', '② ✔ 수의 운동 = 대뇌피질(일차운동피질 피라미드 세포)', '③ ✗ 리듬 운동은 <b>의식적으로 시작</b>하고 <b>의식 없이 유지</b>',
             '④ ✗ 고유수용기는 <b>근육·힘줄·관절</b>에 있고 길이·장력 정보를 보낸다', '⑤ ✗ 힘줄 안에서 장력을 감지하는 것은 <b>골지힘줄기관</b>. 근방추는 근육 안에서 <b>길이</b>'), pick=2, stars=1), cols=2)

    qpage('PART 01–03', '서술형 ①',
        ES('Explain the sliding filament mechanism of skeletal muscle contraction. Describe how the sarcomere, A band, I band, and H zone change during contraction, and explain why the filaments themselves do not change in length.', '골격근 수축의 활주 필라멘트 기전을 설명하고, 수축 중 근절·A대·I대·H대가 어떻게 변하는지, 그리고 필라멘트 자체의 길이는 왜 변하지 않는지 서술하시오.',
           '근절 양쪽의 가는 필라멘트(액틴)가 마이오신 교차다리에 끌려 굵은 필라멘트 사이로 <b>A대 중앙(M선) 쪽으로 미끄러져</b> 들어간다. 그 결과 양쪽 <b>Z선이 가까워져 근절이 짧아진다</b>. 가는 필라멘트만 있던 <b>I대</b>와 가는 필라멘트가 닿지 않던 <b>H대</b>는 겹치는 부분이 늘면서 <b>짧아지거나 사라진다</b>. <b>A대</b>는 굵은 필라멘트의 길이 그 자체이므로 <b>너비가 그대로</b>다. 수축은 필라멘트가 <b>서로 겹치는 정도가 늘어나서</b> 생기는 것이지 단백질 자체가 줄어드는 것이 아니므로 굵은·가는 필라멘트의 길이는 변하지 않는다.',
           K('가는 필라멘트가 중앙으로 미끄러짐', 'Z선 접근 → 근절 짧아짐', 'I대·H대 짧아짐', 'A대 그대로', '겹침 증가') + '<div>🖊 그림(이완 vs 수축 근절)을 함께 그리면 좋다.</div>', stars=3),
        ES('Describe the four steps of the cross-bridge cycle, indicating where ATP is used, and explain why rigor mortis develops after death.', '교차다리 주기의 네 단계를 ATP가 쓰이는 곳을 밝혀 서술하고, 죽은 뒤 사후경직이 생기는 이유를 설명하시오.',
           '① <b>장전(Energized)</b>: 마이오신 ATPase가 ATP를 ADP + Pi로 분해하고, 그 에너지로 마이오신 머리가 고에너지 상태가 된다(액틴에 붙기 전). ② <b>결합(Binding)</b>: Ca²⁺가 트로포닌에 붙어 트로포마이오신이 비켜나면 마이오신 머리가 액틴에 결합한다. ③ <b>굽힘(Power stroke)</b>: 머리가 굽으며 가는 필라멘트를 근절 중앙으로 당긴다. Pi는 도중에, ADP는 끝난 뒤 떨어진다. ④ <b>분리(Detachment)</b>: <b>새 ATP가 결합</b>해야 액틴–마이오신 친화력이 낮아져 떨어지고, ATP가 다시 분해되어 주기가 반복된다. 죽으면 ATP가 만들어지지 않아 ④ 단계가 일어나지 못하므로 마이오신이 액틴에 <b>붙은 채 고정</b>되어 근육이 굳는다 = <b>사후경직</b>.',
           K('ATP 분해 = 장전', 'Ca²⁺–트로포닌', '파워 스트로크', '새 ATP = 분리', 'ATP 없음 → 사후경직'), stars=3), cols=2)

    qpage('PART 02–03', '서술형 ②',
        ES('Describe excitation–contraction coupling in skeletal muscle, from the release of acetylcholine at the neuromuscular junction to the start of cross-bridge cycling. Then explain how the muscle fiber relaxes.', '신경근 접합부의 아세틸콜린 방출부터 교차다리 주기 시작까지 골격근의 흥분-수축 연결을 서술하고, 근섬유가 이완되는 과정을 설명하시오.',
           '운동뉴런 말단에서 <b>ACh</b>가 방출되어 운동종판의 수용체에 결합하면 근섬유막(<b>sarcolemma</b>)에 <b>활동전위</b>가 생겨 표면 전체로 퍼진다. 활동전위는 A대·I대 경계에서 안으로 파고든 <b>T세관</b>을 따라 근섬유 깊숙이 전달되고, T세관과 맞닿은 <b>근소포체의 lateral sacs</b>가 저장한 <b>Ca²⁺를 세포질로 방출</b>한다. Ca²⁺가 <b>트로포닌</b>에 결합하면 <b>트로포마이오신</b>이 액틴의 결합 부위에서 비켜나고, 에너지를 가진 마이오신이 액틴에 붙어 교차다리 주기가 시작된다. 이완: <b>AChE</b>가 ACh를 분해해 활동전위가 멈추고, <b>SERCA 펌프</b>가 <b>ATP를 써서</b> Ca²⁺를 근소포체로 되돌린다. Ca²⁺가 트로포닌에서 떨어지면 트로포마이오신이 다시 결합 부위를 덮어 마이오신이 액틴에 붙지 못하고 근육이 이완된다.',
           K('ACh → 근섬유막 AP', 'T세관', 'SR lateral sacs Ca²⁺', '트로포닌 → 트로포마이오신', 'AChE', 'SERCA(ATP)'), stars=3),
        ES('Explain the two ways in which the tension of a whole skeletal muscle is graded, including motor unit recruitment, twitch summation, and tetanus. Then explain why cardiac muscle cannot undergo tetanus.', '골격근 전체 장력을 조절하는 두 가지 방법을 운동단위 동원, 연축 가중, 강축을 포함해 서술하고, 심장근에서 강축이 일어나지 않는 이유를 설명하시오.',
           '근육 전체 장력은 ① <b>수축하는 근섬유의 수</b>와 ② <b>근섬유 하나의 장력</b>으로 정해진다. ① 운동단위(운동뉴런 하나 + 그 뉴런이 지배하는 근섬유 전부)를 <b>더 많이 동원</b>할수록 수축하는 근섬유가 늘어난다. 약한 힘에는 <b>작은 운동단위</b>가 먼저 동원되어 정밀하게 조절된다(크기의 원리). ② 근섬유가 <b>완전히 이완하기 전에</b> 다시 자극되면 세포질 Ca²⁺가 높게 유지되어 두 번째 연축이 더해진다 = <b>연축 가중</b>. 자극이 매우 빨라 이완할 틈이 없으면 <b>최대 지속 수축</b>인 <b>강축</b>이 된다. 심장근은 활동전위의 <b>불응기가 매우 길어</b> 수축이 끝나기 전에 다음 활동전위가 생기지 않으므로 가중과 강축이 일어나지 않고, 덕분에 수축과 이완(혈액 채우기)을 반복할 수 있다.',
           K('운동단위 동원', '크기의 원리', '이완 전 재자극 → 가중', '강축 = 최대 지속 수축', '긴 불응기'), stars=3), cols=2)

    memo([('🧱 구조', '근절 = <b>Z선~Z선</b><br>A대 = 굵은 필라멘트 길이(어두움)<br>I대 = 가는 필라멘트만(밝음)<br>H대 = A대 가운데 / M선 = 정중앙<br>티틴 = Z–M–Z 용수철<br>트로포마이오신 = 가림 / 트로포닌 = Ca²⁺ 결합'),
          ('🔄 수축·이완', 'ACh → 근섬유막 AP → <b>T세관</b> → SR <b>lateral sacs</b> Ca²⁺ → <b>트로포닌</b> → 교차다리<br>ATP: 분해 = 장전, <b>새 ATP = 분리</b>(없으면 사후경직)<br>이완 = AChE + <b>SERCA(ATP)</b><br>AP 1~2 ms / 수축·이완 각 15~50 ms'),
          ('📈 역학·대사', '장력 = 운동단위 수 × 빈도<br>이완 <b>전</b> 재자극 = 가중 → 강축<br>작은 운동단위 먼저(크기의 원리)<br>ATP: 크레아틴 인산 → 산화적 인산화(30+) → 해당과정(2, 젖산)<br>Type I 적색·지구력 / IIx 백색·빨리 지침'),
          ('🧭 조절·평활·심장', '근방추 = <b>길이</b> / 골지힘줄기관 = <b>장력</b>(이완 반사)<br>뇌간 = 고위 중추 → 골격근 마지막 연결<br>평활근: Ca²⁺ → <b>칼모듈린 → MLCK</b>, 치밀체, 3초<br>심장근: 개재판·간극연접, <b>긴 불응기 → 강축 없음</b>')],
         '<ol><li>수축 시 <b>A대는 그대로</b> (H·I대만 짧아짐)</li><li>Ca²⁺ 결합: 골격근 = <b>트로포닌</b>, 평활근 = <b>칼모듈린</b></li><li>이완에도 <b>ATP</b> 필요 (SERCA), 분리에도 <b>새 ATP</b></li></ol>',
         ['수축 시 가는 필라멘트가 A대 중앙으로 미끄러져 Z선이 가까워지므로 근절·I대·H대는 짧아지지만 A대와 필라멘트 길이는 그대로다.',
          '교차다리 주기에서 ATP 분해는 마이오신 머리를 장전시키고, 새 ATP의 결합은 마이오신을 액틴에서 떼어낸다 — ATP가 없으면 사후경직이 생긴다.',
          '근섬유막의 활동전위가 T세관을 따라 내려가 근소포체에서 Ca²⁺를 방출시키고, Ca²⁺가 트로포닌에 결합해 트로포마이오신을 치우면 교차다리 주기가 시작된다.'])
