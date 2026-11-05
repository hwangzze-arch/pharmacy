# 통합모의고사 50문항 데이터
# kind: tf(1점) mc(2점) mc2(3점) sa(2점) es(3.5점)
Q = []
def tf(ch, en, ko, ans, why, keys=()):
    Q.append(dict(kind='tf', ch=ch, pts=1, en=en, ko=ko, ans=ans, why=why, keys=keys))
def mc(ch, en, ko, choices, ans, why, keys=(), two=False):
    Q.append(dict(kind='mc2' if two else 'mc', ch=ch, pts=3 if two else 2, en=en, ko=ko, choices=choices, ans=ans, why=why, keys=keys))
def sa(ch, en, ko, ans, keys, why=()):
    Q.append(dict(kind='sa', ch=ch, pts=2, en=en, ko=ko, ans=ans, why=why, keys=keys))
def es(ch, en, ko, model, keys, why=()):
    Q.append(dict(kind='es', ch=ch, pts=3.5, en=en, ko=ko, ans=model, why=why, keys=keys))

# ---------- PART I. True / False (1–14) ----------
tf('1', 'Homeostasis is maintained by directly regulating the intracellular fluid; the extracellular fluid is not regulated.', '항상성은 세포내액을 직접 조절해 유지되며, 세포외액은 조절되지 않는다.', 'F',
   ['✗ 항상성이 지키는 내부 환경은 <b>세포외액</b>이다. 세포는 세포외액과 물질을 주고받으므로 세포외액이 일정해야 산다.'], ['내부 환경 = 세포외액'])
tf('1', 'Extrinsic controls are accomplished mainly by the nervous and endocrine systems.', '외인성 조절은 주로 신경계와 내분비계가 수행한다.', 'T',
   ['✔ 장기 밖에서 시작되는 조절 = 신경계·내분비계. 여러 장기를 한꺼번에 조정할 수 있다.'], ['외인성 = 신경·내분비'])
tf('2', 'Ribosomes bound to the rough ER synthesize proteins destined for export or for insertion into membranes.', '조면소포체에 붙은 리보솜은 분비되거나 막에 삽입될 단백질을 합성한다.', 'T',
   ['✔ 분리된 합성: 분비·막 단백질 = ER 부착 리보솜, 세포 안에서 쓸 단백질 = 자유 리보솜.'], ['분리된 합성'])
tf('2', 'Catalase is the lysosomal enzyme that breaks down worn-out organelles.', '카탈레이스는 낡은 세포기관을 분해하는 리소좀 효소이다.', 'F',
   ['✗ 카탈레이스는 <b>퍼옥시좀</b>의 효소로 <b>과산화수소</b>를 분해한다. 낡은 세포기관 분해는 리소좀의 <b>가수분해효소</b>.'], ['카탈레이스 = 퍼옥시좀', '리소좀 = 가수분해효소'])
tf('3', 'Desmosomes are communicating junctions that allow ions to pass directly between cardiac cells.', '데스모솜은 심장 세포 사이로 이온이 직접 지나가게 하는 소통 연접이다.', 'F',
   ['✗ 이온이 지나가는 소통 연접은 <b>간극연접</b>. 데스모솜은 두 세포를 리벳처럼 <b>고정</b>하는 연접이다.'], ['간극연접 = 터널', '데스모솜 = 고정'])
tf('3', 'A red blood cell placed in a hypertonic solution shrinks.', '고장액에 넣은 적혈구는 쪼그라든다.', 'T',
   ['✔ 바깥에 비투과성 용질이 많음 → 물이 세포 밖으로 빠져나감 → 쪼그라듦.'], ['고장성', '물은 용질 많은 쪽으로'])
tf('3', 'Secondary active transport uses the energy of ATP hydrolysis directly.', '2차 능동수송은 ATP 분해 에너지를 직접 사용한다.', 'F',
   ['✗ ATP를 직접 쓰는 것은 <b>1차</b> 능동수송. 2차는 1차가 만든 <b>Na⁺ 농도 기울기</b>의 힘을 빌린다.'], ['2차 = Na⁺ 기울기'])
tf('4', 'A graded potential becomes smaller as it spreads away from its site of origin.', '등급전위는 발생 부위에서 멀어질수록 작아진다.', 'T',
   ['✔ 수동 전류가 막을 통해 새어 나가므로 거리에 따라 감쇠 → 먼 거리 신호는 활동전위가 맡는다.'], ['감쇠', '짧은 거리 신호'])
tf('4', 'During the absolute refractory period, a sufficiently strong stimulus can trigger a second action potential.', '절대 불응기에는 충분히 강한 자극이면 두 번째 활동전위를 일으킬 수 있다.', 'F',
   ['✗ 절대 불응기에는 Na⁺ 통로가 열려 있거나 불활성 상태라 <b>어떤 자극으로도</b> 불가능. 강한 자극으로 가능한 건 <b>상대</b> 불응기.'], ['절대 = 불가', '상대 = 강하면 가능'])
tf('4', 'Lipophilic hormones bind to intracellular receptors and alter gene expression.', '친유성 호르몬은 세포 안 수용체에 결합해 유전자 발현을 바꾼다.', 'T',
   ['✔ 지질막을 통과 → 세포질·핵 수용체 → 유전자 활성 → 새 단백질 합성.'], ['친유성 = 세포 안 수용체·새 단백질'])
tf('5', 'The thalamus is the main integrating center for regulating body temperature.', '시상은 체온 조절의 주 통합 중추이다.', 'F',
   ['✗ 체온·갈증·식욕 등 항상성 통합 중추는 <b>시상하부</b>. 시상은 감각 신호를 걸러 피질로 보내는 <b>중계소</b>.'], ['시상하부 = 항상성', '시상 = 중계'])
tf('5', 'Afferent fibers enter the spinal cord through the dorsal root.', '구심 섬유는 후근을 통해 척수로 들어간다.', 'T',
   ['✔ 감각은 등(후근)으로 들어오고 운동은 배(전근)로 나간다. 구심 뉴런 세포체는 후근 신경절.'], ['후근 = 감각 진입', '전근 = 운동 출구'])
tf('6', 'Photoreceptors hyperpolarize in response to light.', '광수용기는 빛에 반응해 과분극된다.', 'T',
   ['✔ 빛 → Na⁺ 통로 닫힘 → 과분극 → 글루탐산 방출 감소. 다른 수용기와 반대인 예외.'], ['빛 = 과분극'])
tf('7', 'Parasympathetic postganglionic fibers release norepinephrine onto adrenergic receptors.', '부교감 신경절후 섬유는 노르에피네프린을 아드레날린성 수용체에 방출한다.', 'F',
   ['✗ 부교감 신경절후 = <b>아세틸콜린 → 무스카린성</b> 수용체. 노르에피네프린 → 아드레날린성은 <b>교감</b> 신경절후.'], ['부교감 = ACh·무스카린성', '교감 = NE·아드레날린성'])

# ---------- PART II. Multiple choice, one answer (15–30) ----------
mc('1', 'A structure composed of two or more types of primary tissue that work together to perform a particular function is a(n) ____.', '두 종류 이상의 기본 조직이 함께 특정 기능을 수행하는 구조는 ____이다.',
   [('tissue', '조직'), ('organ', '장기'), ('body system', '신체 계통'), ('cell', '세포'), ('organism', '개체')], '②',
   ['① ✗ 조직 = 비슷한 <b>세포</b>의 모임(한 종류)', '② ✔ 여러 조직의 조합 = 장기 (위 = 상피+결합+근육+신경)', '③ ✗ 계통 = 관련 기능을 하는 <b>장기</b>들의 모음', '④ ✗ 세포 = 생명의 기본 단위', '⑤ ✗ 개체 = 계통이 모인 몸 전체'], ['조직 → 장기 → 계통'])
mc('1', 'Which of the following is an example of positive feedback?', '다음 중 양성 되먹임의 예는?',
   [('Insulin lowering a rising blood glucose', '오르는 혈당을 인슐린이 낮춤'), ('Sweating when body temperature rises', '체온 상승 시 땀'), ('Oxytocin release intensifying uterine contractions during childbirth', '출산 중 옥시토신이 자궁 수축을 더 강하게 함'),
    ('Shivering when body temperature falls', '체온 하강 시 떨림'), ('Lowering heart rate when blood pressure rises', '혈압 상승 시 심박수 감소')], '③',
   ['①②④⑤ ✗ 모두 처음 변화를 <b>되돌리는</b> 음성 되먹임', '③ ✔ 수축 → 옥시토신↑ → 더 센 수축: 같은 방향으로 증폭, 분만으로 끝남'], ['양성 = 같은 방향 증폭', '출산'])
mc('2', 'Which organelle contains oxidative enzymes that detoxify wastes such as alcohol and produce hydrogen peroxide?', '알코올 같은 노폐물을 해독하고 과산화수소를 만드는 산화효소를 가진 세포기관은?',
   [('lysosome', '리소좀'), ('peroxisome', '퍼옥시좀'), ('Golgi complex', '골지 복합체'), ('ribosome', '리보솜'), ('mitochondrion', '미토콘드리아')], '②',
   ['① ✗ 리소좀 = 가수분해효소로 분해', '② ✔ 산화효소 + 카탈레이스 = 해독', '③ ✗ 골지 = 단백질 가공·포장', '④ ✗ 리보솜 = 단백질 합성', '⑤ ✗ 미토콘드리아 = ATP 생산'], ['퍼옥시좀', '산화효소·카탈레이스'])
mc('2', 'The citric acid cycle takes place in the ____.', '시트르산 회로는 ____에서 일어난다.',
   [('cytosol', '세포액'), ('inner mitochondrial membrane', '미토콘드리아 내막'), ('mitochondrial matrix', '미토콘드리아 기질'), ('smooth ER', '활면소포체'), ('outer mitochondrial membrane', '미토콘드리아 외막')], '③',
   ['① ✗ 세포액 = <b>해당과정</b>', '② ✗ 내막 = <b>산화적 인산화</b>(전자전달계)', '③ ✔ 기질 = 피루브산 산화 + 시트르산 회로', '④ ✗ 활면소포체는 세포 호흡과 무관', '⑤ ✗ 외막에서 일어나는 단계는 없음'], ['해당 = 세포액', '시트르산 회로 = 기질', '산화적 인산화 = 내막'])
mc('3', 'Which of the following is <u>NOT</u> a characteristic of carrier-mediated transport?', '다음 중 운반체 매개 수송의 특징이 <u>아닌</u> 것은?',
   [('specificity', '특이성'), ('saturation', '포화'), ('competition', '경쟁'), ('a rate that increases without limit in proportion to concentration', '농도에 비례해 한없이 증가하는 속도'), ('conformational change of the carrier', '운반체의 모양 변화')], '④',
   ['①②③ ✗ 운반체 3대 특징(특이성·포화·경쟁)', '④ ✔ 한없이 비례 증가는 <b>단순 확산</b>의 특징. 운반체는 최대 수송 속도에서 멈춤', '⑤ ✗ 운반체는 모양을 바꿔 물질을 반대편에 내려준다'], ['특이성·포화·경쟁', '최대 수송 속도'])
mc('3', 'At rest, which ion is more concentrated inside the cell than outside?', '휴지 상태에서 세포 밖보다 안에 더 많은 이온은?',
   [('Na<sup>+</sup>', ''), ('K<sup>+</sup>', ''), ('Cl<sup>−</sup>', ''), ('Ca<sup>2+</sup>', ''), ('HCO<sub>3</sub><sup>−</sup>', '')], '②',
   ['① ✗ Na⁺는 밖에 많다(150 vs 15)', '② ✔ K⁺는 안에 많다(150 vs 5) — 펌프가 안으로 넣는다', '③ ✗ Cl⁻는 밖에 많다', '④ ✗ Ca²⁺는 밖에 훨씬 많다', '⑤ ✗ 중탄산 이온도 밖에 많다'], ['K⁺ = 안', 'Na⁺ = 밖'])
mc('3', 'The equilibrium potential for Na<sup>+</sup> is approximately ____.', 'Na<sup>+</sup>의 평형전위는 약 ____이다.',
   [('−90 mV', ''), ('−70 mV', ''), ('0 mV', ''), ('+30 mV', ''), ('+60 mV', '')], '⑤',
   ['① ✗ −90 = K⁺ 평형전위', '② ✗ −70 = 휴지막전위', '③ ✗ 0은 분극이 없는 상태', '④ ✗ +30 = 활동전위 정점', '⑤ ✔ 61 × log(150/15) = +61 ≈ +60'], ['E_Na +60', 'E_K −90', '휴지 −70'])
mc('4', 'Saltatory conduction occurs because action potentials are generated only at the ____.', '도약 전도는 활동전위가 ____에서만 생기기 때문에 일어난다.',
   [('axon hillock', '축삭둔덕'), ('nodes of Ranvier', '랑비에 결절'), ('Schwann cell bodies', '슈반 세포체'), ('myelin-covered internodes', '수초로 덮인 결절 사이'), ('dendrites', '가지돌기')], '②',
   ['① ✗ 축삭둔덕은 활동전위가 <b>시작</b>되는 곳', '② ✔ 수초가 없는 결절에서만 활동전위 → 징검다리 점프', '③ ✗ 슈반 세포는 수초를 만드는 세포일 뿐', '④ ✗ 수초 덮인 부분은 절연되어 활동전위가 안 생김', '⑤ ✗ 가지돌기는 입력을 받는 곳'], ['랑비에 결절', '도약 전도 = 빠름·절약'])
mc('4', 'Spatial summation occurs when ____.', '공간적 가중은 ____일 때 일어난다.',
   [('one presynaptic input fires repeatedly in rapid succession', '하나의 입력이 빠르게 반복 발화'), ('several presynaptic inputs fire simultaneously', '여러 입력이 동시에 발화'), ('an EPSP and IPSP cancel each other', 'EPSP와 IPSP가 상쇄'),
    ('a neuromodulator acts slowly', '신경조절물질이 천천히 작용'), ('an action potential jumps between nodes', '활동전위가 결절 사이를 뜀')], '②',
   ['① ✗ 그건 <b>시간적</b> 가중', '② ✔ 여러 입력 + 동시 = 공간적', '③ ✗ 상쇄(cancellation)', '④ ✗ 조절물질은 EPSP를 만들지 않음', '⑤ ✗ 도약 전도'], ['공간적 = 여러·동시', '시간적 = 같은·반복'])
mc('4', 'Which of the following is a neurohormone?', '다음 중 신경호르몬은?',
   [('histamine released by mast cells near a wound', '상처 근처 비만세포가 내는 히스타민'), ('ADH released into the blood from nerve endings in the posterior pituitary', '뇌하수체 후엽 신경 말단에서 혈액으로 방출되는 ADH'),
    ('insulin secreted by pancreatic cells', '췌장 세포가 분비하는 인슐린'), ('acetylcholine released at the neuromuscular junction', 'NMJ에서 방출되는 아세틸콜린'), ('prostaglandin acting on neighboring cells', '이웃 세포에 작용하는 프로스타글란딘')], '②',
   ['① ✗ 국소 작용 = 측분비', '② ✔ 신경분비 뉴런이 <b>혈액으로</b> 내보냄 = 신경호르몬', '③ ✗ 내분비샘 세포의 호르몬', '④ ✗ 시냅스 틈의 신경전달물질', '⑤ ✗ 측분비(에이코사노이드)'], ['신경호르몬 = 뉴런 → 혈액'])
mc('5', 'Which glial cells are ciliated cells that line the ventricles and help produce cerebrospinal fluid?', '뇌실 내벽을 이루는 섬모 세포로 뇌척수액 생성을 돕는 교세포는?',
   [('astrocytes', '별아교세포'), ('oligodendrocytes', '희소돌기아교세포'), ('microglia', '미세아교세포'), ('ependymal cells', '뇌실막세포'), ('Schwann cells', '슈반 세포')], '④',
   ['① ✗ BBB 유도·K⁺ 조절', '② ✗ 중추 수초', '③ ✗ 면역 방어', '④ ✔ 뇌실 내벽·뇌척수액·신경 줄기세포', '⑤ ✗ 말초 수초'], ['뇌실막세포 = 뇌척수액'])
mc('5', "Damage to Broca's area typically results in ____.", '브로카 영역이 손상되면 대개 ____.',
   [('inability to understand spoken language', '말을 이해하지 못함'), ('difficulty speaking although comprehension is relatively intact', '이해는 비교적 되지만 말하기가 어려움'), ('blindness in one eye', '한쪽 눈 실명'),
    ('loss of balance', '균형 상실'), ('loss of long-term memory formation', '장기기억 형성 불가')], '②',
   ['① ✗ 이해 장애 = <b>베르니케</b> 영역 손상', '② ✔ 브로카 = 말하기 근육 조절', '③ ✗ 시각 = 후두엽', '④ ✗ 균형 = 소뇌·전정기관', '⑤ ✗ 장기기억 형성 = 해마'], ['브로카 = 말하기', '베르니케 = 이해'])
mc('5', 'Which structure maintains cortical arousal and consciousness?', '대뇌피질의 각성과 의식을 유지하는 구조는?',
   [('reticular activating system of the brain stem', '뇌간의 망상 활성계'), ('cerebellum', '소뇌'), ('basal nuclei', '기저핵'), ('hippocampus', '해마'), ('corpus callosum', '뇌량')], '①',
   ['① ✔ 상행 망상 활성계 = 각성 스위치', '② ✗ 소뇌 = 운동 협응', '③ ✗ 기저핵 = 운동 억제 조절', '④ ✗ 해마 = 기억', '⑤ ✗ 뇌량 = 좌우 반구 연결'], ['망상체', '상행 망상 활성계 = 각성'])
mc('6', 'Which of the following receptors adapts slowly?', '다음 중 느리게 적응하는 수용기는?',
   [('Pacinian corpuscle', '파치니 소체'), ("Meissner's corpuscle", '마이스너 소체'), ('hair receptor', '털 수용기'), ("Merkel's disc", '메르켈 원반'), ('all of these adapt rapidly', '모두 빠르게 적응')], '④',
   ['①②③ ✗ 모두 빠른 적응(변화 감지)', '④ ✔ 메르켈 원반 = 느린 적응, 지속적 가벼운 접촉', '⑤ ✗ 메르켈은 느리다'], ['느린 적응 = 메르켈·루피니'])
mc('6', 'Vibrations of the tympanic membrane are transmitted to the oval window by the ____.', '고막의 진동은 ____에 의해 난원창으로 전달된다.',
   [('ossicles', '이소골'), ('basilar membrane', '기저막'), ('semicircular canals', '반고리관'), ('cochlear duct', '달팽이관 관'), ('auditory nerve', '청신경')], '①',
   ['① ✔ 망치뼈 → 모루뼈 → 등자뼈가 전달·증폭', '② ✗ 기저막은 난원창 <b>다음</b> 단계(달팽이관 안)', '③ ✗ 반고리관 = 회전 감지', '④ ✗ 달팽이관은 난원창 안쪽', '⑤ ✗ 청신경은 마지막 신호 출력'], ['이소골', '고막 → 이소골 → 난원창'])
mc('7', 'The adrenal medulla mainly secretes ____ into the blood.', '부신수질은 주로 ____을 혈액으로 분비한다.',
   [('acetylcholine', '아세틸콜린'), ('epinephrine', '에피네프린'), ('cortisol', '코르티솔'), ('dopamine', '도파민'), ('insulin', '인슐린')], '②',
   ['① ✗ 부신수질은 아세틸콜린을 <b>받는</b> 쪽', '② ✔ 에피네프린 약 80% + 노르에피네프린 약 20%', '③ ✗ 코르티솔 = 부신<b>피질</b>', '④ ✗ 도파민은 주 분비물이 아님', '⑤ ✗ 인슐린 = 췌장'], ['부신수질 = 변형된 교감신경절', '에피네프린'])

# ---------- PART III. Multiple choice, choose two (31–38) ----------
mc('2', 'Which TWO statements about the smooth ER are correct? <b>(Choose two.)</b>', '활면소포체에 대한 옳은 설명 두 개는?',
   [('It packages newly synthesized proteins into transport vesicles.', '새 단백질을 수송소포에 포장한다'), ('It is studded with ribosomes.', '리보솜이 박혀 있다'), ('It synthesizes lipids.', '지질을 합성한다'),
    ('It contains hydrolytic enzymes that digest bacteria.', '세균을 소화하는 가수분해효소를 가진다'), ('It is the site of oxidative phosphorylation.', '산화적 인산화가 일어나는 곳이다')], '①, ③',
   ['① ✔ 수송소포 포장 → 골지로', '② ✗ 리보솜이 붙은 건 <b>조면</b>소포체', '③ ✔ 지질 합성', '④ ✗ 가수분해효소 = 리소좀', '⑤ ✗ 산화적 인산화 = 미토콘드리아 내막'], ['활면소포체 = 포장·지질'], two=True)
mc('3', 'Which TWO substances cross the plasma membrane by simple diffusion through the lipid bilayer? <b>(Choose two.)</b>', '지질 이중층을 단순 확산으로 통과하는 물질 두 개는?',
   [('O<sub>2</sub>', ''), ('glucose', '포도당'), ('CO<sub>2</sub>', ''), ('Na<sup>+</sup>', ''), ('proteins', '단백질')], '①, ③',
   ['① ✔ 작고 비극성 → 바로 통과', '② ✗ 포도당 = 크고 수용성 → <b>운반체</b>', '③ ✔ 작고 비극성', '④ ✗ 이온 = <b>통로</b> 필요', '⑤ ✗ 단백질 = <b>소포 수송</b>'], ['지용성·작은 분자 = 단순 확산'], two=True)
mc('4', 'Which TWO are characteristics of action potentials but <u>not</u> graded potentials? <b>(Choose two.)</b>', '등급전위에는 없고 활동전위에만 있는 특징 두 개는?',
   [('all-or-none response', '실무율'), ('decremental spread', '감쇠 전파'), ('a refractory period', '불응기'), ('summation', '가중'), ('magnitude varies with stimulus strength', '자극 세기에 따라 크기 변화')], '①, ③',
   ['① ✔ 활동전위만 실무율', '② ✗ 감쇠는 <b>등급전위</b>의 특징', '③ ✔ 활동전위만 불응기', '④ ✗ 가중은 <b>등급전위</b>만 가능', '⑤ ✗ 크기 변화는 <b>등급전위</b>'], ['실무율', '불응기'], two=True)
mc('4', 'Which TWO second messengers are formed when phospholipase C cleaves PIP<sub>2</sub>? <b>(Choose two.)</b>', '인지질 분해효소 C가 PIP<sub>2</sub>를 자를 때 생기는 2차 전령 두 개는?',
   [('IP<sub>3</sub>', ''), ('DAG', ''), ('cAMP', ''), ('ATP', ''), ('GTP', '')], '①, ②',
   ['① ✔ IP₃ → 소포체에서 Ca²⁺ 방출', '② ✔ DAG → 단백질 인산화효소 C 활성', '③ ✗ cAMP는 <b>아데닐산 고리화효소</b>가 ATP로 만든다', '④ ✗ ATP는 cAMP의 재료', '⑤ ✗ GTP는 G단백질을 켜는 분자'], ['PIP₂ → IP₃ + DAG'], two=True)
mc('5', 'Which TWO are functions of the hypothalamus? <b>(Choose two.)</b>', '시상하부의 기능 두 개는?',
   [('regulating body temperature', '체온 조절'), ('final conscious perception of vision', '시각의 최종 의식적 지각'), ('producing posterior pituitary hormones', '뇌하수체 후엽 호르몬 생산'),
    ('coordinating skilled voluntary movement', '숙련된 수의 운동 협응'), ('relaying sensory input to the cortex', '감각 입력을 피질로 중계')], '①, ③',
   ['① ✔ 항상성 통합 중추', '② ✗ 최종 지각 = <b>후두엽 시각 피질</b>', '③ ✔ ADH·옥시토신 생산', '④ ✗ 운동 협응 = <b>소뇌</b>', '⑤ ✗ 감각 중계 = <b>시상</b>'], ['시상하부 = 체온·후엽 호르몬'], two=True)
mc('5', 'Which TWO are required for long-term memory storage? <b>(Choose two.)</b>', '장기기억 저장에 필요한 것 두 개는?',
   [('synthesis of new proteins', '새 단백질 합성'), ('activation of CREB', 'CREB 활성화'), ('decreased Ca<sup>2+</sup> entry into presynaptic terminals', '시냅스전 Ca<sup>2+</sup> 유입 감소'),
    ('only transient modification of existing synapses', '기존 시냅스의 일시적 변화만'), ('loss of synapses in the hippocampus', '해마 시냅스 소실')], '①, ②',
   ['① ✔ 장기기억 = 단백질 합성 필요', '② ✔ CREB가 단백질 합성 유전자를 켠다', '③ ✗ Ca²⁺ 감소 = <b>습관화</b>(단기)', '④ ✗ 일시적 변화만 = <b>단기</b>기억', '⑤ ✗ 시냅스 소실은 기억과 반대'], ['단백질 합성', 'CREB', '새 시냅스'], two=True)
mc('6', 'Which TWO statements about the otolith organs are correct? <b>(Choose two.)</b>', '이석기관에 대한 옳은 설명 두 개는?',
   [('They detect linear acceleration and head tilt.', '직선 가속과 머리 기울기를 감지한다'), ('They contain calcium carbonate crystals.', '탄산칼슘 결정을 가진다'), ('They detect rotational acceleration.', '회전 가속을 감지한다'),
    ('They are located in the cochlea.', '달팽이관에 있다'), ('They contain the organ of Corti.', '코르티 기관을 가진다')], '①, ②',
   ['① ✔ 타원낭·구형낭 = 직선·중력', '② ✔ 이석 = 탄산칼슘 돌가루', '③ ✗ 회전 = <b>반고리관</b>', '④ ✗ 전정기관에 있다(달팽이관 = 청각)', '⑤ ✗ 코르티 기관 = 달팽이관(청각)'], ['이석기관 = 직선·중력', '이석 = 탄산칼슘'], two=True)
mc('7', 'Which TWO events occur at the neuromuscular junction? <b>(Choose two.)</b>', '신경근 접합부에서 일어나는 사건 두 개는?',
   [('ACh binds to nicotinic receptors on the motor end plate.', 'ACh가 운동종판의 니코틴성 수용체에 결합'), ('Acetylcholinesterase degrades ACh.', '아세틸콜린 분해효소가 ACh를 분해'), ('Norepinephrine is released from the terminal button.', '말단 단추에서 노르에피네프린 방출'),
    ('The end-plate potential is an all-or-none action potential.', '종판전위는 실무율의 활동전위'), ('ACh binds to muscarinic receptors on skeletal muscle.', 'ACh가 골격근의 무스카린성 수용체에 결합')], '①, ②',
   ['① ✔ 운동종판 = 니코틴성', '② ✔ 분해로 신호 종료', '③ ✗ 운동뉴런은 <b>아세틸콜린</b>만 방출', '④ ✗ 종판전위는 <b>등급전위</b>', '⑤ ✗ 골격근은 <b>니코틴성</b>(무스카린성 = 부교감 효과기)'], ['니코틴성', '아세틸콜린 분해효소'], two=True)

# ---------- PART IV. Short answer (39–46) ----------
sa('1', 'Name the four primary tissue types.', '4대 기본 조직을 쓰시오.', '상피조직 · 결합조직 · 근육조직 · 신경조직', ['근·신·상·결'])
sa('2', 'Name the three forms of endocytosis and state which one is selective.', '세포내유입 세 가지를 쓰고, 그중 선택적인 것을 쓰시오.', '음세포작용 · 수용체 매개 세포내유입 · 식세포작용 — 선택적인 것은 수용체 매개 세포내유입', ['음세포 = 비선택', '수용체 매개 = 선택', '식세포 = 큰 입자'])
sa('3', 'Name the three types of specialized cell junctions and give one function of each.', '세포연접 세 가지와 각각의 기능을 쓰시오.', '밀착연접 — 틈을 봉해 물질이 세포 사이로 못 지나감 / 데스모솜 — 두 세포를 고정 / 간극연접 — 이온이 지나가는 통로(소통)', ['봉인', '고정', '터널'])
sa('3', 'Calculate E<sub>Na</sub> if [Na<sup>+</sup>]<sub>o</sub> = 150 mM and [Na<sup>+</sup>]<sub>i</sub> = 15 mM (z = +1).', '[Na<sup>+</sup>]<sub>밖</sub> = 150, [Na<sup>+</sup>]<sub>안</sub> = 15 mM일 때 E<sub>Na</sub>를 계산하시오.', 'E = 61 × log(150/15) = 61 × 1 = +61 mV (약 +60 mV)', ['네른스트 식', '61/z · log(밖/안)'])
sa('4', 'Classify hormones into two groups by solubility and state where the receptor of each is located.', '용해성에 따라 호르몬을 두 종류로 나누고 각 수용체의 위치를 쓰시오.', '친수성 호르몬(펩타이드) — 세포막 표면 수용체 / 친유성 호르몬(스테로이드) — 세포 안(세포질·핵) 수용체', ['친수성 = 표면', '친유성 = 세포 안'])
sa('5', 'Name the three meninges from outermost to innermost.', '뇌막 세 겹을 바깥부터 순서대로 쓰시오.', '경막 → 거미막 → 연막', ['경·거·연'])
sa('6', 'Name the two types of afferent pain fibers and the quality of pain each carries.', '두 종류의 구심성 통증 섬유와 각각이 전달하는 통증의 성질을 쓰시오.', 'A-델타 섬유(유수) — 날카롭고 찌르는 빠른 통증 / C 섬유(무수) — 둔하고 쑤시고 타는 느린 통증', ['A-델타 = 유수·날카로움', 'C = 무수·둔함'])
sa('7', 'Name the neurotransmitter and receptor type at (a) all autonomic ganglia, (b) parasympathetic effector organs, and (c) most sympathetic effector organs.', '(a) 모든 자율신경절 (b) 부교감 효과기 (c) 대부분의 교감 효과기에서의 신경전달물질과 수용체를 쓰시오.',
   '(a) 아세틸콜린 – 니코틴성 (b) 아세틸콜린 – 무스카린성 (c) 노르에피네프린 – 아드레날린성(α·β)', ['신경절 = 니코틴성', '부교감 = 무스카린성', '교감 = 아드레날린성'])

# ---------- PART V. Essay (47–50) ----------
es('3·4', 'Explain how the resting membrane potential is established and how an action potential is generated and propagated along a myelinated axon.',
   '휴지막전위가 형성되는 원리와, 유수 축삭에서 활동전위가 생성·전도되는 과정을 설명하시오.',
   '휴지막전위(약 −70 mV)는 Na⁺–K⁺ 펌프가 만든 농도 차이(안 K⁺, 밖 Na⁺)와, K⁺ 누출 통로를 통한 <b>K⁺ 유출</b> 때문에 생긴다. 자극으로 막이 <b>역치</b>(약 −50 mV)에 도달하면 전압개폐 <b>Na⁺ 통로</b>가 열려 Na⁺가 들어오고(양성 되먹임) 막전위가 +30 mV까지 뒤집힌다. 이어 Na⁺ 통로가 불활성화되고 전압개폐 <b>K⁺ 통로</b>가 열려 K⁺가 나가며 재분극된다. 유수 축삭에서는 수초가 절연하므로 활동전위가 <b>랑비에 결절</b>에서만 생기고, 국소 전류가 다음 결절을 역치까지 탈분극시켜 <b>도약 전도</b>가 일어난다. 불응기 때문에 한 방향으로만 진행하며, 도약 전도는 연속 전도보다 빠르고 에너지를 아낀다.',
   ['펌프·K⁺ 유출', '역치', 'Na⁺ 유입', 'K⁺ 유출 = 재분극', '랑비에 결절', '도약 전도', '불응기 = 한 방향'], ['채점: 휴지막전위 원인 + 활동전위 이온 흐름 + 도약 전도 3요소'])
es('4', 'Describe the events at a chemical synapse from the arrival of an action potential to the postsynaptic response, and explain how EPSPs and IPSPs determine whether the postsynaptic neuron fires.',
   '화학 시냅스에서 활동전위 도착부터 시냅스후 반응까지의 과정과, EPSP·IPSP가 시냅스후 뉴런의 발화를 어떻게 결정하는지 설명하시오.',
   '활동전위가 시냅스전 말단에 도착하면 전압개폐 <b>Ca²⁺ 통로</b>가 열리고 Ca²⁺ 유입으로 신경전달물질이 <b>세포외유출</b>된다. 신경전달물질은 틈을 건너 시냅스후 막의 수용체-통로에 결합한다. 흥분성 시냅스에서는 Na⁺ 유입으로 작은 탈분극(<b>EPSP</b>)이, 억제성 시냅스에서는 K⁺ 유출이나 Cl⁻ 유입으로 작은 과분극(<b>IPSP</b>)이 생긴다. 신경전달물질은 분해·재흡수로 빠르게 제거된다. 시냅스후 뉴런은 여러 입력을 <b>시간적·공간적 가중</b>으로 합산하며, EPSP와 IPSP는 서로 상쇄된다. 이 합(총 시냅스후전위)이 <b>축삭둔덕</b>에서 역치를 넘으면 활동전위가 발생한다.',
   ['Ca²⁺ 유입', '세포외유출', 'EPSP = 탈분극', 'IPSP = 과분극', '시간적·공간적 가중', '축삭둔덕 역치'], ['채점: 시냅스 순서 + 두 전위 + 통합(가중·축삭둔덕)'])
es('5', 'Describe long-term potentiation, including the roles of glutamate, AMPA receptors, and NMDA receptors, and explain why it is important for memory.',
   '장기 강화를 글루탐산, AMPA 수용체, NMDA 수용체의 역할을 포함해 설명하고, 기억에 중요한 이유를 쓰시오.',
   '장기 강화는 자주 쓰이는 시냅스의 효율이 <b>오래 강화</b>되는 현상으로 <b>해마</b>에서 두드러진다. 시냅스전 뉴런이 <b>글루탐산</b>을 방출하면 <b>AMPA 수용체</b>가 열려 Na⁺가 들어오고 EPSP가 생긴다. 시냅스후 막이 충분히 탈분극되면, 글루탐산과 탈분극이 <b>둘 다</b> 있어야 열리는 <b>NMDA 수용체</b>가 열려 Ca²⁺가 들어온다. Ca²⁺는 2차 전령 경로를 켜서 시냅스후 막에 AMPA 수용체를 더 넣고, 역행성 전령(산화질소)을 만들어 시냅스전 뉴런의 글루탐산 방출을 늘린다. 이렇게 같은 입력에 더 큰 반응이 나와 연결이 강해지므로, 단기기억을 장기기억으로 바꾸는 바탕이 된다.',
   ['해마', '글루탐산', 'AMPA = Na⁺·EPSP', 'NMDA = Ca²⁺·이중 조건', '수용체 삽입', '역행성 전령', '단기 → 장기기억'], ['채점: 두 수용체의 이온 + 조건 + 강화 결과'])
es('6·7', 'A person touches a hot stove and quickly withdraws the hand. Trace this reflex from receptor to effector, naming the receptor type, fiber types, spinal cord structures, and the neurotransmitter at the effector, and state one sympathetic response that may follow.',
   '뜨거운 난로를 만진 사람이 손을 재빨리 뗀다. 이 반사를 수용기부터 효과기까지 추적하며 수용기 종류, 섬유 종류, 척수 구조, 효과기의 신경전달물질을 쓰고, 뒤따를 수 있는 교감 반응 하나를 쓰시오.',
   '뜨거운 자극은 피부의 <b>열 침해수용기</b>(통증 수용기)를 자극해 <b>수용기전위</b>를 만들고, 구심 뉴런에 활동전위가 생긴다. 날카로운 첫 통증은 유수 <b>A-델타 섬유</b>로 빠르게 전달된다. 구심 섬유는 <b>후근</b>으로 척수에 들어가 <b>후각</b>의 <b>사이신경세포</b>와 시냅스하고(다시냅스 반사), 신호는 <b>전각</b>의 운동뉴런으로 전달된다. 운동뉴런 축삭은 <b>전근</b>으로 나가 굴근의 신경근 접합부에서 <b>아세틸콜린</b>을 방출하고, 니코틴성 수용체 → 종판전위 → 근수축으로 손을 뗀다. 이 반사는 뇌를 거치지 않는 척수 반사이며, 동시에 시상을 거쳐 두정엽이 통증을 지각한다. 놀란 뒤 <b>교감신경</b>이 활성화되어 심박수 증가나 동공 확대가 나타날 수 있다.',
   ['열 침해수용기', 'A-델타 섬유', '후근 → 사이신경세포 → 전각 운동뉴런', '전근', '아세틸콜린·니코틴성', '척수 반사', '교감: 심박↑·동공 확대'], ['채점: 반사궁 5요소를 실제 구조 이름으로'])
