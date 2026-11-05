"""문서 작성 절대 규칙 자동 적용: 장(chapter)마다 처음 등장하는 약어/영어 용어/어려운 용어에 풀이를 붙인다."""
import re

# 1) 약어: raw-html 패턴 -> (Full name, 한글 뜻)
ABBR = [
    ('ECF', 'Extracellular fluid', '세포외액: 세포 바깥을 채운 액체'),
    ('ICF', 'Intracellular fluid', '세포내액: 세포 안의 액체'),
    ('ECM', 'Extracellular matrix', '세포외기질: 세포 사이를 채운 단백질 그물'),
    ('DNA', 'Deoxyribonucleic acid', '디옥시리보핵산: 유전 정보 설계도'),
    ('RER', 'Rough endoplasmic reticulum', '조면소포체: 리보솜이 붙어 오돌토돌한 소포체'),
    ('SER', 'Smooth endoplasmic reticulum', '활면소포체: 리보솜 없이 매끈한 소포체'),
    ('ER', 'Endoplasmic reticulum', '소포체: 단백질·지질을 만드는 막 공장'),
    ('COPI', 'Coat protein I', '피복 단백질 I: 소포를 감싸 모양을 잡는 코트'),
    ('ATP', 'Adenosine triphosphate', '아데노신삼인산: 세포의 에너지 화폐'),
    ('LDL', 'Low-density lipoprotein', '저밀도 지단백질: 콜레스테롤을 싣고 다니는 입자'),
    ('CoA', 'Coenzyme A', '조효소 A: 아세틸기를 나르는 도우미 분자'),
    ('NADH', 'Nicotinamide adenine dinucleotide (환원형)', '니코틴아마이드 아데닌 다이뉴클레오타이드: 전자를 실어 나르는 트럭'),
    ('FADH<sub>2</sub>', 'Flavin adenine dinucleotide (환원형)', '플라빈 아데닌 다이뉴클레오타이드: 또 하나의 전자 운반 트럭'),
    ('GLUT1', 'Glucose transporter 1', '포도당 수송체 1: 뇌 혈관의 포도당 전용 문'),
    ('GLUT', 'Glucose transporter', '포도당 수송체: 포도당 전용 회전문'),
    ('SGLT', 'Sodium-glucose linked transporter', '나트륨-포도당 공동수송체: Na⁺와 포도당을 함께 태우는 2인용 문'),
    ('CAMs', 'Cell adhesion molecules', '세포 접착 분자: 세포끼리 붙잡는 손'),
    ('RMP', 'Resting membrane potential', '휴지막전위: 아무 신호 없을 때의 막 전압'),
    ('EPSP', 'Excitatory postsynaptic potential', '흥분성 시냅스후전위: 역치 쪽으로 밀어주는 작은 + 신호'),
    ('IPSP', 'Inhibitory postsynaptic potential', '억제성 시냅스후전위: 역치에서 멀어지게 하는 작은 − 신호'),
    ('GPSP', 'Grand postsynaptic potential', '총 시냅스후전위: 들어온 모든 신호의 합계'),
    ('AP', 'Action potential', '활동전위: 뉴런이 쏘는 전기 신호 한 발'),
    ('NT', 'Neurotransmitter', '신경전달물질: 뉴런 사이를 건너는 화학 메시지'),
    ('GPCR', 'G protein-coupled receptor', 'G단백질 연결 수용체: 신호를 G단백질에 넘기는 막 수용체'),
    ('cAMP', 'cyclic adenosine monophosphate', '고리형 AMP: 대표적인 세포 안 2차 전령'),
    ('IP<sub>3</sub>', 'Inositol trisphosphate', '이노시톨 삼인산: ER에서 Ca²⁺를 풀어주는 2차 전령'),
    ('PIP<sub>2</sub>', 'Phosphatidylinositol bisphosphate', '포스파티딜이노시톨 이인산: IP₃와 DAG로 쪼개지는 막 지질'),
    ('DAG', 'Diacylglycerol', '다이아실글리세롤: 막에 남아 PKC를 켜는 2차 전령'),
    ('PKA', 'Protein kinase A', '단백질 인산화효소 A: cAMP가 켜는 인산 붙이는 효소'),
    ('PLC', 'Phospholipase C', '인지질 분해효소 C: PIP₂를 자르는 효소'),
    ('JAK/STAT', 'Janus kinase / Signal transducer and activator of transcription', '야누스 키나아제/전사 신호 전달자: 수용체 → 핵으로 바로 가는 신호 경로'),
    ('GDP', 'Guanosine diphosphate', '구아노신이인산: G단백질의 "꺼짐" 상태'),
    ('GTP', 'Guanosine triphosphate', '구아노신삼인산: G단백질의 "켜짐" 상태'),
    ('HRE', 'Hormone response element', '호르몬 반응 요소: 호르몬-수용체가 붙는 DNA 자리'),
    ('MS', 'Multiple sclerosis', '다발성 경화증: 수초가 망가지는 병'),
    ('SSRIs', 'Selective serotonin reuptake inhibitors', '선택적 세로토닌 재흡수 억제제'),
    ('SSRI', 'Selective serotonin reuptake inhibitor', '선택적 세로토닌 재흡수 억제제: 세로토닌을 시냅스에 오래 머물게 하는 약'),
    ('SNRIs', 'Serotonin-norepinephrine reuptake inhibitors', '세로토닌-노르에피네프린 재흡수 억제제'),
    ('SNRI', 'Serotonin-norepinephrine reuptake inhibitor', '세로토닌-노르에피네프린 재흡수 억제제'),
    ('MAOIs', 'Monoamine oxidase inhibitors', '모노아민 산화효소 억제제: 분해효소를 막아 NE·세로토닌을 늘리는 약'),
    ('MAOI', 'Monoamine oxidase inhibitor', '모노아민 산화효소 억제제: 분해효소를 막는 항우울제'),
    ('CNS', 'Central nervous system', '중추신경계: 뇌 + 척수'),
    ('PNS', 'Peripheral nervous system', '말초신경계: 뇌·척수 밖의 신경'),
    ('ENS', 'Enteric nervous system', '장신경계: 소화관 벽 속 신경망'),
    ('ANS', 'Autonomic nervous system', '자율신경계: 내 의지와 상관없이 내장을 조절'),
    ('BBB', 'Blood-brain barrier', '혈액-뇌 장벽: 혈액 속 물질이 뇌로 함부로 못 들어오게 막는 검문소'),
    ('CSF', 'Cerebrospinal fluid', '뇌척수액: 뇌와 척수를 감싸 띄우는 물'),
    ('NGF', 'Nerve growth factor', '신경성장인자: 뉴런 생존을 돕는 단백질'),
    ('ARAS', 'Ascending reticular activating system', '상행 망상 활성계: 뇌를 깨어 있게 하는 각성 스위치'),
    ('DRS', 'Descending reticular system', '하행 망상계: 운동·자세·자율 기능 조절'),
    ('EEG', 'Electroencephalogram', '뇌전도: 머리 표면에서 잰 뇌 전기 활동'),
    ('REM', 'Rapid eye movement', '빠른 눈 운동 수면: 꿈꾸는 역설수면'),
    ('LTP', 'Long-term potentiation', '장기 강화: 자주 쓰는 시냅스가 오래 강해지는 현상'),
    ('AMPA', 'α-amino-3-hydroxy-5-methyl-4-isoxazolepropionic acid (receptor)', 'AMPA 수용체: 글루탐산이 붙으면 Na⁺를 통과시키는 문'),
    ('NMDA', 'N-methyl-D-aspartate (receptor)', 'NMDA 수용체: 글루탐산 + 탈분극 둘 다 있어야 Ca²⁺를 통과시키는 이중 잠금 문'),
    ('NO', 'Nitric oxide', '산화질소: 시냅스후 → 시냅스전으로 거꾸로 가는 역행성 전령'),
    ('CREB', 'cAMP response element-binding protein', 'cAMP 반응 요소 결합 단백질: 장기기억용 단백질 합성을 켜는 스위치'),
    ('L-dopa', 'Levodopa', '레보도파: BBB를 통과해 뇌에서 도파민이 되는 전구체 약'),
    ('NMJ', 'Neuromuscular junction', '신경근 접합부: 운동뉴런과 골격근이 만나는 곳'),
    ('EPP', 'End-plate potential', '종판전위: 운동종판에 생기는 큰 등급전위'),
    ('AChE', 'Acetylcholinesterase', '아세틸콜린 분해효소: 일 끝난 ACh를 잘라 신호를 끄는 효소'),
    ('ACh', 'Acetylcholine', '아세틸콜린: 신경근 접합부·부교감의 신경전달물질'),
    ('NE', 'Norepinephrine', '노르에피네프린: 교감신경의 신경전달물질'),
    ('ALS', 'Amyotrophic lateral sclerosis', '근위축성 측삭 경화증(루게릭병): 운동뉴런이 죽는 병'),
    ('SR', 'Sarcoplasmic reticulum', '근소포체: 근육 속 Ca²⁺ 저장 창고'),
    ('mOsm', 'milliosmole', '밀리오스몰: 용질 입자 수의 단위'),
    ('Tm', 'Transport maximum', '최대 수송 속도: 운반체가 꽉 찼을 때의 속도 한계'),
    ('ADH', 'Antidiuretic hormone', '항이뇨호르몬: 소변을 줄여 물을 아끼게 하는 호르몬'),
]
ABBR_CH = {  # 장마다 뜻이 다른 약어
    2: [('TCA', 'Tricarboxylic acid (cycle)', '시트르산 회로: 미토콘드리아에서 CO₂를 떼어내는 회전 반응')],
    5: [('TCAs', 'Tricyclic antidepressants', '삼환계 항우울제'), ('TCA', 'Tricyclic antidepressant', '삼환계 항우울제: 고리 3개짜리 오래된 항우울제')],
}

# 2) 영어 용어/인명 -> 한글 (바로 뒤에 한글이나 괄호가 이미 있으면 건너뜀)
EN = {
    'Fick\'s law': '픽의 법칙', 'Nernst': '네른스트', 'Kandel': '캔델', 'Aplysia': '아플리시아, 군소',
    'Broca\'s area': '브로카 영역', 'Wernicke\'s area': '베르니케 영역', 'Broca': '브로카', 'Wernicke': '베르니케',
    'Parkinson\'s disease': '파킨슨병', 'Schwann cell': '슈반 세포', 'Ranvier': '랑비에', 'node of Ranvier': '랑비에 결절',
    'Pacinian corpuscle': '파치니 소체', 'Pacinian': '파치니', 'Merkel\'s disc': '메르켈 원반', 'Merkel': '메르켈',
    'Ruffini ending': '루피니 종말', 'Ruffini': '루피니', 'Meissner\'s corpuscle': '마이스너 소체', 'Meissner': '마이스너',
    'organ of Corti': '코르티 기관', 'Organ of Corti': '코르티 기관', 'Corti': '코르티', 'Golgi complex': '골지 복합체', 'Golgi': '골지',
    'Physiology': '생리학', 'Anatomy': '해부학', 'Homeostasis': '항상성', 'homeostasis': '항상성',
    'Negative feedback': '음성 되먹임', 'Positive feedback': '양성 되먹임', 'Feedforward': '전향 조절', 'feedforward': '전향 조절',
    'Intrinsic': '내인성', 'Extrinsic': '외인성', 'Interstitial fluid': '간질액', 'Plasma': '혈장',
    'Secretion': '분비', 'Exocytosis': '세포외유출', 'Endocytosis': '세포내유입', 'Pinocytosis': '음세포작용',
    'Phagocytosis': '식세포작용', 'Receptor-mediated endocytosis': '수용체 매개 세포내유입', 'Endosome': '엔도좀',
    'Lysosome': '리소좀', 'Peroxisome': '퍼옥시좀', 'catalase': '카탈레이스', 'oxidase': '산화효소',
    'ubiquitin': '유비퀴틴', 'proteasome': '프로테아좀', 'Cytoplasm': '세포질', 'Cytosol': '세포액', 'inclusions': '봉입체',
    'Microtubule': '미세소관', 'Microfilament': '미세섬유', 'Intermediate filament': '중간섬유', 'cristae': '크리스타, 내막 주름',
    'Glycolysis': '해당과정', 'Oxidative phosphorylation': '산화적 인산화', 'Citric acid cycle': '시트르산 회로',
    'fluid mosaic model': '유동 모자이크 모델', 'Tight junction': '밀착연접', 'Desmosome': '데스모솜', 'Gap junction': '간극연접',
    'collagen': '콜라겐', 'elastin': '엘라스틴', 'fibronectin': '피브로넥틴', 'connexon': '코넥손',
    'Osmosis': '삼투', 'Tonicity': '장성', 'Isotonic': '등장성', 'Hypotonic': '저장성', 'Hypertonic': '고장성',
    'Facilitated diffusion': '촉진확산', 'Primary active': '1차 능동', 'Secondary active': '2차 능동',
    'Symport': '공동수송', 'Antiport': '역수송', 'Uniport': '단일수송', 'Specificity': '특이성', 'Saturation': '포화', 'Competition': '경쟁',
    'Equilibrium potential': '평형전위', 'electrogenic': '기전성, 전위를 직접 만드는', 'Polarization': '분극',
    'Depolarization': '탈분극', 'Repolarization': '재분극', 'Hyperpolarization': '과분극', 'All-or-none': '실무율', 'all-or-none': '실무율',
    'Absolute': '절대 불응기', 'Relative': '상대 불응기', 'Contiguous': '연속 전도', 'Saltatory': '도약 전도',
    'axon hillock': '축삭둔덕', 'trigger zone': '방아쇠 구역', 'Synapse': '시냅스', 'Temporal': '시간적', 'Spatial': '공간적',
    'Neuromodulator': '신경조절물질', 'Presynaptic inhibition': '시냅스전 억제', 'Presynaptic facilitation': '시냅스전 촉진',
    'Convergence': '수렴', 'Divergence': '발산', 'Paracrine': '측분비', 'Autocrine': '자가분비', 'Neurohormone': '신경호르몬',
    'Signal transduction': '신호 전달', 'Cytokines': '사이토카인', 'Eicosanoids': '에이코사노이드', 'prostaglandins': '프로스타글란딘',
    'Adenylyl cyclase': '아데닐산 고리화효소', 'tyrosine kinase': '타이로신 키나아제', 'Hydrophilic': '친수성', 'Lipophilic': '친유성',
    'Wired': '유선', 'Wireless': '무선', 'Afferent': '구심성', 'Efferent': '원심성', 'Interneuron': '사이신경세포',
    'Astrocyte': '별아교세포', 'Oligodendrocyte': '희소돌기아교세포', 'Microglia': '미세아교세포', 'Ependymal': '뇌실막세포',
    'tripartite synapse': '삼자 시냅스', 'Meninges': '뇌막', 'Dura': '경막', 'Arachnoid': '거미막', 'Pia': '연막',
    'choroid plexus': '맥락총', 'Corpus callosum': '뇌량', 'Gray matter': '회백질', 'White matter': '백질',
    'pyramidal': '추체세포', 'stellate': '성상세포', 'Occipital': '후두엽', 'Temporal lobe': '측두엽', 'Parietal': '두정엽', 'Frontal': '전두엽',
    'Central sulcus': '중심고랑', 'postcentral gyrus': '중심후회', 'precentral gyrus': '중심전회', 'homunculus': '호문쿨루스, 뇌 속 작은 인간 지도',
    'contralateral': '반대쪽', 'Supplementary motor area': '보조운동영역', 'Premotor cortex': '전운동피질', 'Posterior parietal cortex': '후두정피질',
    'Plasticity': '가소성', 'Lateralization': '편재화', 'Prefrontal': '전전두', 'Basal nuclei': '기저핵', 'Thalamus': '시상', 'Hypothalamus': '시상하부',
    'Limbic system': '변연계', 'Cingulate gyrus': '대상회', 'Hippocampus': '해마', 'Amygdala': '편도체', 'Septal': '중격',
    'Habituation': '습관화', 'Sensitization': '민감화', 'Working memory': '작업기억', 'Consolidation': '공고화',
    'Cerebellum': '소뇌', 'Brain stem': '뇌간', 'Reticular formation': '망상체', 'Dorsal root': '후근', 'Ventral root': '전근',
    'Ganglion': '신경절', 'Nucleus': '핵', 'Dermatome': '피부분절', 'Monosynaptic': '단일시냅스', 'Polysynaptic': '다시냅스',
    'Sensory transduction': '감각 변환', 'adequate stimulus': '적합 자극', 'Tonic': '긴장성', 'Phasic': '위상성', 'off response': '꺼짐 반응',
    'Nociceptor': '침해수용기', 'Polymodal': '다형', 'Substance P': '물질 P', 'substance P': '물질 P',
    'Sclera': '공막', 'Cornea': '각막', 'Choroid': '맥락막', 'Ciliary body': '섬모체', 'Iris': '홍채', 'Retina': '망막',
    'Aqueous humor': '방수', 'Vitreous humor': '유리체', 'Accommodation': '원근 조절', 'Phototransduction': '광변환',
    'Rods': '막대세포', 'Cones': '원뿔세포', 'bipolar': '양극세포', 'ganglion cell': '신경절세포', 'fovea': '중심와',
    'Tympanic membrane': '고막', 'Malleus': '망치뼈', 'Incus': '모루뼈', 'Stapes': '등자뼈', 'Oval window': '난원창',
    'Basilar membrane': '기저막', 'Cochlea': '달팽이관', 'Semicircular canals': '반고리관', 'Otolith organs': '이석기관',
    'Utricle': '타원낭', 'Saccule': '구형낭', 'Taste bud': '미뢰', 'taste bud': '미뢰', 'umami': '감칠맛',
    'Preganglionic': '신경절전', 'Postganglionic': '신경절후', 'Sympathetic': '교감', 'Parasympathetic': '부교감',
    'Adrenal medulla': '부신수질', 'Dual innervation': '이중 신경지배', 'Nicotinic': '니코틴성', 'Muscarinic': '무스카린성',
    'Adrenergic': '아드레날린성', 'Cholinergic': '콜린성', 'Agonist': '작용제', 'Antagonist': '길항제', 'atropine': '아트로핀',
    'salbutamol': '살부타몰', 'Final common pathway': '최종 공통 경로', 'Motor end plate': '운동종판', 'terminal button': '말단 단추',
    'Botulinum toxin': '보툴리눔 독소', 'Curare': '큐라레', 'Organophosphates': '유기인제', 'Myasthenia gravis': '중증 근무력증',
    'neostigmine': '네오스티그민', 'Black widow': '검은과부거미', 'Amblyopia': '약시', 'Use it or lose it': '쓰지 않으면 잃는다',
}

# 3) 어려운 한글 용어 -> [즉, ~]
KO = {
    '항상성': '바깥이 변해도 몸 안 상태를 일정하게 지키는 것', '동적 평형': '가만히 멈춘 게 아니라 계속 움직이면서 균형을 맞춘 상태',
    '되먹임': '결과가 다시 원인을 조절하는 고리', '내부 환경': '세포가 실제로 몸을 담그고 사는 바닷물 같은 액체',
    '분화': '줄기 같은 세포가 특정 일을 하는 세포로 전문화되는 것', '외분비': '관을 통해 몸 밖이나 소화관으로 내보내는 것',
    '내분비': '관 없이 혈액으로 바로 내보내는 것', '분리된 합성': '쓸 곳에 따라 단백질을 만드는 장소를 따로 나누는 것',
    '세포외유출': '소포가 세포막과 합쳐져 내용물을 밖으로 쏟아내는 것', '세포내유입': '세포막이 움푹 들어가 바깥 물질을 감싸 삼키는 것',
    '가수분해효소': '물을 이용해 큰 분자를 잘게 자르는 가위 효소', '자가포식': '세포가 낡은 자기 부품을 스스로 먹어 치우는 것',
    '봉입체': '막 없이 세포 안에 잠시 쌓아둔 저장 덩어리', '세포 호흡': '음식을 산소로 천천히 태워 ATP를 뽑아내는 과정',
    '선택적 투과': '어떤 것은 통과시키고 어떤 것은 막는 성질', '인지질': '머리는 물을 좋아하고 꼬리는 물을 싫어하는 막 기름',
    '유동성': '막이 딱딱하지 않고 기름처럼 흐르는 성질', '농도 기울기': '진한 곳과 묽은 곳의 농도 차이 — 물질이 굴러 내려가는 비탈',
    '전기화학적 기울기': '농도 차이와 전기 끌림을 합친 총 비탈', '삼투': '물이 용질이 많은 쪽으로 빨려 가는 것',
    '장성': '바깥 용액이 세포를 부풀릴지 쪼그라뜨릴지를 정하는 힘', '용혈': '적혈구가 물을 너무 먹어 터지는 것',
    '능동수송': 'ATP를 써서 비탈을 거슬러 올리는 수송', '운반체': '물질을 붙잡고 모양을 바꿔 반대편에 내려주는 막 단백질',
    '막전위': '세포막 안팎의 전압 차이', '평형전위': '그 이온이 더 이상 한쪽으로 쏠려 움직이지 않는 전압',
    '휴지막전위': '아무 신호가 없을 때의 막 전압', '흥분성 세포': '전기 신호를 만들 수 있는 세포(뉴런·근육)',
    '탈분극': '막 안쪽이 덜 음(−)이 되는 것', '재분극': '흔들렸던 막전위가 원래로 돌아오는 것', '과분극': '막 안쪽이 평소보다 더 음(−)이 되는 것',
    '등급전위': '자극 크기에 따라 크기가 달라지는 짧은 거리용 작은 전기 신호', '역치': '활동전위가 터지는 최소 문턱 전압',
    '실무율': '문턱을 넘으면 항상 같은 크기로, 못 넘으면 아예 안 생기는 규칙', '불응기': '방금 신호를 쏜 자리가 잠깐 다시 못 쏘는 휴식 시간',
    '불활성화문': 'Na⁺ 통로를 안쪽에서 막아버리는 두 번째 문', '도약 전도': '수초 사이 결절만 골라 징검다리처럼 뛰어가는 전도',
    '수초': '축삭을 감싼 지방 절연 테이프', '시냅스': '두 뉴런이 신호를 주고받는 이음매', '시냅스 지연': '화학 신호가 틈을 건너느라 생기는 짧은 시간 지연',
    '가중': '작은 신호들이 겹쳐 더해지는 것', '재흡수': '분비한 신경전달물질을 다시 빨아들여 신호를 끄는 것',
    '2차 전령': '세포 밖 신호를 받아 세포 안에서 대신 전달하는 작은 분자', '증폭': '신호 하나가 단계마다 여러 배로 불어나는 것',
    '인산화': '단백질에 인산을 붙여 켜거나 끄는 스위치 조작', '측분비': '바로 옆 세포에만 작용하는 국소 신호',
    '사이신경세포': '뇌·척수 안에서 정보를 이어주고 판단하는 뉴런', '교세포': '신호는 안 보내고 뉴런을 돌보는 지원 세포',
    '삼자 시냅스': '두 뉴런 + 별아교세포 셋이 함께 만드는 시냅스', '시냅스 가지치기': '안 쓰는 시냅스를 잘라내 회로를 정리하는 것',
    '뇌실': '뇌 속에 뇌척수액이 차 있는 빈 방', '지주막하 공간': '거미막과 연막 사이, 뇌척수액이 흐르는 공간',
    '수두증': '뇌척수액이 빠지지 못해 뇌실이 부풀어 오르는 병', '회백질': '세포체가 모여 회색으로 보이는 처리 구역',
    '백질': '수초 덮인 축삭 다발이라 하얗게 보이는 전선 구역', '체성감각': '피부·근육·관절에서 오는 몸의 감각',
    '고유감각': '눈 감고도 팔다리 위치를 아는 감각', '연합 영역': '감각을 직접 받지 않고 여러 정보를 엮어 생각하는 영역',
    '편재화': '좌뇌·우뇌가 일을 나눠 맡는 것', '가소성': '쓰임에 따라 뇌 회로가 다시 짜이는 성질',
    '근긴장': '쉬고 있어도 근육에 남아 있는 약한 긴장', '공고화': '단기기억이 장기기억으로 굳어지는 과정',
    '습관화': '의미 없는 자극이 반복되면 반응이 줄어드는 것', '민감화': '강한 자극 뒤 약한 자극에도 크게 반응하는 것',
    '역행성 전령': '시냅스후 세포에서 시냅스전 세포로 거꾸로 보내는 신호', '망상체': '뇌간 전체에 그물처럼 퍼진 각성 조절 신경망',
    '서파수면': '뇌파가 느리고 큰 깊은 잠', '역설수면': '몸은 자는데 뇌파는 깨어 있는 듯한 꿈 수면',
    '신경절': '중추신경 밖에 뉴런 세포체가 모인 덩어리', '반사궁': '자극 → 판단 → 반응으로 이어지는 반사의 전선 회로',
    '수용기전위': '감각 수용기에 생기는 등급전위', '적응': '같은 자극이 계속되면 반응이 줄어드는 것',
    '침해수용기': '조직 손상(위험)을 감지하는 통증 수용기', '원근 조절': '가까운 곳·먼 곳에 맞춰 수정체 두께를 바꾸는 것',
    '현수인대': '수정체를 사방에서 당겨 매달고 있는 줄', '광변환': '빛 에너지를 전기 신호로 바꾸는 것', '광색소': '빛을 흡수하는 색소 단백질',
    '중심와': '망막 한가운데 원뿔세포가 빽빽한 가장 선명한 점', '이소골': '중이 속 소리를 전달·증폭하는 작은 뼈 3개',
    '이석': '털세포 위에 얹힌 탄산칼슘 돌가루', '신경절전': '중추신경에서 신경절까지 가는 첫 번째 뉴런',
    '신경절후': '신경절에서 장기까지 가는 두 번째 뉴런', '이중 신경지배': '한 장기를 교감·부교감이 함께 조절하는 것',
    '상반 조절': '한쪽은 가속, 한쪽은 브레이크로 반대로 당기는 정밀 조절', '최종 공통 경로': '골격근에 닿는 유일한 길(운동뉴런)',
    '운동종판': '운동뉴런 말단 아래 근육막의 ACh 수용체 밀집 부위', '종판전위': '운동종판에 생기는 큰 등급전위',
    '작용제': '수용체에 붙어 진짜 신호처럼 작동시키는 약', '길항제': '수용체 자리를 막아 신호를 못 오게 하는 약',
}

SKIP = {'chev', 'flow', 'pt', 'part', 'chip', 'qt', 'st', 'prof', 'e', 'ab', 'tp', 'tpart', 'foot', 'ox', 'pn', 'kw', 'cap', 'tr', 'n', 'ct'}
TOKEN = re.compile(r'(<!--.*?-->|<svg.*?</svg>|<img[^>]*>|<style.*?</style>|</?[a-zA-Z][^>]*>)', re.S)
INLINE = {'sub', 'sup', 'b', 'i', 'u', 'span', 'small', 'br'}
HANGUL = re.compile(r'[가-힣]')

def _cls(tag):
    m = re.search(r'class="([^"]*)"', tag)
    return set(m.group(1).split()) if m else set()

def annotate_chapter(htmls, ch):
    """htmls: list of page html of one chapter. 반환: 수정된 list."""
    abbr = ABBR_CH.get(ch, []) + ABBR
    done = set()
    en_items = sorted(EN.items(), key=lambda x: -len(x[0]))
    ko_items = sorted(KO.items(), key=lambda x: -len(x[0]))
    out = []
    for html in htmls:
        parts = TOKEN.split(html)
        stack = []
        res = []
        for tok in parts:
            if not tok:
                continue
            if tok.startswith('<'):
                if tok.startswith('</'):
                    name = re.match(r'</\s*([a-zA-Z0-9]+)', tok).group(1).lower()
                    for k in range(len(stack) - 1, -1, -1):
                        if stack[k][0] == name:
                            del stack[k:]
                            break
                elif not (tok.startswith('<!--') or tok.startswith('<svg') or tok.startswith('<img') or tok.startswith('<style') or tok.endswith('/>')):
                    m = re.match(r'<\s*([a-zA-Z0-9]+)', tok)
                    name = m.group(1).lower()
                    if name != 'br':
                        stack.append((name, _cls(tok)))
                res.append(tok)
                continue
            skip = any((c & SKIP) or n == 'th' for n, c in stack)
            if skip:
                res.append(tok)
                continue
            res.append(_ann(tok, abbr, en_items, ko_items, done))
        out.append(''.join(res))
    return out

def _free(text, a, b):
    for m in re.finditer(r'<span class="(?:ann|t)">.*?</span>', text):
        if m.start() < b and a < m.end():
            return False
    return True

def _first(rx, text):
    for m in rx.finditer(text):
        if _free(text, m.start(), m.end()):
            return m
    return None

def _ann(text, abbr, en_items, ko_items, done):
    # 약어
    for pat, full, ko in abbr:
        key = 'A:' + pat
        if key in done:
            continue
        plain = re.sub(r'<[^>]+>', '', pat)
        rx = re.compile(r'(?<![A-Za-z0-9가-힣])' + re.escape(plain) + r'(?![A-Za-z0-9])')
        m = _first(rx, text)
        if not m:
            continue
        done.add(key)
        after = text[m.end():m.end() + 3]
        if after.lstrip().startswith('('):
            continue
        ins = f' <span class="ann">({full}, {ko})</span>'
        text = text[:m.start()] + f'<span class="t">{m.group(0)}</span>' + ins + text[m.end():]
    # 영어 용어
    for term, ko in en_items:
        key = 'E:' + term
        if key in done:
            continue
        rx = re.compile(r'(?<![A-Za-z])' + re.escape(term) + r'(?![A-Za-z])')
        m = _first(rx, text)
        if not m:
            continue
        done.add(key)
        for t2, _ in en_items:
            if t2 != term and t2 in term:
                done.add('E:' + t2)
        e = m.end()
        if text[e:e + 2] == "'s":
            e += 2
        after = text[e:e + 4]
        if '(' in after or HANGUL.search(after) or '[' in after:
            text = text[:m.start()] + f'<span class="t">{text[m.start():e]}</span>' + text[e:]
            continue
        text = text[:m.start()] + f'<span class="t">{text[m.start():e]}</span> <span class="ann">({ko})</span>' + text[e:]
    # 어려운 한글 용어
    for term, ex in ko_items:
        key = 'K:' + term
        if key in done:
            continue
        m = _first(re.compile(r'(?<![가-힣])' + re.escape(term) + r'(?=[^가-힣]|[은는이가을를의에로와과도만으까란라처보부일])'), text)
        if not m:
            continue
        done.add(key)
        j = m.end()
        if text[j:j + 3].lstrip().startswith('['):
            continue
        text = text[:m.start()] + f'<span class="t">{m.group(0)}</span> <span class="ann">[즉, {ex}]</span>' + text[j:]
    return text
