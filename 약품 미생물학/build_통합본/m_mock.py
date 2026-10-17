# -*- coding: utf-8 -*-
"""중간고사 대비 통합모의고사 (2-1학기 중간고사 기출 스타일 · 통합본 양식)"""
from core import RAW, S, SEC, Q, card, ul, table, img, MARKS
import svgs

LINK = "(연결이 옳은 것을 모두 고르시오)"

# ---------------------------------------------------------------- 객관식 데이터
# kw: 괄호 안 키워드 / link=True면 연결형 / part: gp|vr / ref: 통합본 단원
MC = [
 # ===================== 그람양성균
 dict(part="gp", ref="통합본 1-1", kw="class Clostridia", kwk="Clostridia 강",
      opts=["obligate anaerobes", "forming endospores", "highly polyphyletic", "most species are pathogenic to humans", "typical zoonotic pathogens"],
      topts=["절대 혐기성", "내생포자 형성", "다계통(모양·크기가 다양)", "대부분의 종이 사람에게 병원성", "대표적인 인수공통감염 병원체"],
      ans="①, ②, ③",
      exp=["O|①::Clostridia는 <b>모두 절대 혐기성</b>.", "O|②::모두 <b>내생포자(endospore)</b>를 만듦.", "O|③::강의 'highly polyphyletic: having various shapes and sizes'.",
           "X|④::Clostridium 대부분은 <b>부생균(saprophytic)</b>. 사람 병원균은 주요 5종뿐.", "X|⑤::동물을 감염시키지만 'infecting animals, but <b>not zoonotic</b>'.",
           "KEY|Clostridia = 혐기 · 포자 · 다양한 모양 · 대부분 부생균 · 인수공통 X"]),
 dict(part="gp", ref="통합본 1-1", kw="Clostridium botulinum", kwk="보툴리눔균",
      opts=["etymology: L. botulus (\"sausage\")", "toxin produced under aerobic conditions", "infant botulism by colonization of the digestive tract",
            "person-to-person transmission", "diagnosis: detection of botulinum toxin"],
      topts=["어원: 라틴어 botulus(소시지)", "독소는 산소가 있는 조건에서 만들어짐", "아기 장에 균이 정착해서 생기는 영아 보툴리누스증", "사람 간 전파", "진단: 보툴리눔 독소 검출"],
      ans="①, ③, ⑤",
      exp=["O|①::botulus = 소시지 (상한 소시지에서 발견).", "X|②::독소는 <b>혐기(anaerobic)</b> 조건에서 만들어지는 단백질 → 통조림·진공포장이 위험.",
           "O|③::3가지 경로: 음식(식중독형) · <b>영아 장 정착(영아형, 꿀)</b> · 상처형.", "X|④::사람→사람, 동물→사람 직접 전파는 <b>일어나지 않음</b>.",
           "O|⑤::검체에서 <b>독소</b>를 찾아 진단.", "TIP|보툴리눔은 '독'이 주인공 → 진단도 독소, 사람끼리는 안 옮음"]),
 dict(part="gp", ref="통합본 1-1", kw="tetanospasmin", kwk="파상풍 강직 독소",
      opts=["neurotoxin produced by <i>C. tetani</i>", "acting at several sites within the CNS", "flaccid (limp) paralysis", "lock-jaw and rigid, arched back", "prevented by DPT vaccine"],
      topts=["C. tetani가 만드는 신경독", "중추신경계(CNS)의 여러 곳에 작용", "축 늘어지는(이완성) 마비", "아관긴급(입이 안 벌어짐)과 활처럼 휜 등", "DPT 백신으로 예방"],
      ans="①, ②, ④, ⑤",
      exp=["O|①::tetanospasmin = 파상풍균의 <b>신경독</b>.", "O|②::강의 'acting at several sites within the CNS'.",
           "X|③::억제 신호(GABA·글리신)를 막아 <b>뻣뻣한 경련(강직)</b>. 이완성 마비는 <b>보툴리눔</b>.",
           "O|④::억지 웃음, <b>아관긴급(lock-jaw)</b>, 후궁반장(활처럼 휜 등), 발작.", "O|⑤::DPT의 <b>T</b> = Tetanus.",
           "KEY|보툴리눔 = 흐물흐물(스위치 OFF) / 파상풍 = 뻣뻣(브레이크 고장)"], fig=svgs.NEUROTOX, figw=40),
 dict(part="gp", ref="통합본 1-1", kw="Clostridioides difficile", kwk="디피실균",
      opts=["flourishes after antibiotic therapy (e.g. clindamycin)", "toxin A: cytotoxin, toxin B: enterotoxin", "pseudomembranous colitis",
            "toxic megacolon", "nosocomial infection"],
      topts=["항생제(예: 클린다마이신) 치료 후 번성", "독소 A = 세포독소, 독소 B = 장독소", "위막성 대장염", "중독성 거대결장", "원내(병원) 감염"],
      ans="①, ③, ④, ⑤",
      exp=["O|①::항생제가 정상균을 죽이면 <b>C. difficile이 폭증</b>.", "X|②::거꾸로! 독소 <b>A = 장독소(enterotoxin)</b>, 독소 <b>B = 세포독소(cytotoxin)</b>.",
           "O|③::항생제 관련 <b>위막성 대장염</b>.", "O|④::심하면 <b>toxic megacolon</b>(대장이 급격히 부풂).", "O|⑤::대표 <b>원내감염</b>균.",
           "TIP|A·B 순서 = '<b>A</b>(장, 알파벳 앞) → <b>B</b>(세포)' → '장세'로 외우기"], fig=svgs.CDIFF, figw=40),
 dict(part="gp", ref="통합본 1-1", kw=LINK, kwk="연결이 옳은 것을 모두 고르시오", link=True, kw2="C. perfringens",
      opts=["enterotoxin (CPE) - food poisoning", "alpha toxin - pigbel", "alpha toxin - gas gangrene (myonecrosis)", "beta toxin - necrotizing enteritis", "<i>C. welchii</i> - former name"],
      topts=["장독소(CPE) - 식중독", "알파 독소 - 피그벨(괴사성 장염)", "알파 독소 - 가스괴저(근괴사)", "베타 독소 - 괴사성 장염", "C. welchii - 옛 이름"],
      ans="①, ③, ④, ⑤",
      exp=["O|①::CPE → 가장 흔한 식중독 원인 중 하나 (가벼움).", "X|②::pigbel(괴사성 장염)은 <b>β 독소</b>.", "O|③::<b>α 독소 → 가스괴저</b>(근괴사, 치명적).",
           "O|④::β 독소 → 괴사성 장염(pigbel, 치사율 50%).", "O|⑤::<i>C. perfringens</i>의 옛 이름 = <i>C. welchii</i>.",
           "TIP|α = <b>가</b>스괴저 / β = <b>배</b>(장)가 썩는 pigbel / CPE = 흔한 식중독"], fig="g6.jpg", figw=24),
 dict(part="gp", ref="통합본 1-2", kw="genus Veillonella", kwk="베일로넬라 속",
      opts=["class Negativicutes", "normal flora in the oral mucosa", "ferments glucose and sucrose", "lactate → acetate + 2 propionate + CO<sub>2</sub> + H<sub>2</sub>O", "dental caries, calculus and periodontitis"],
      topts=["Negativicutes 강", "입 안 점막의 정상균", "포도당과 설탕을 발효", "젖산 → 아세트산 + 2 프로피온산 + CO₂ + H₂O", "충치, 치석, 치주염"],
      ans="①, ②, ④, ⑤",
      exp=["O|①::현재 <b>Negativicutes</b> 강 (옛날엔 Clostridia).", "O|②::포유류 <b>입 안 정상균</b> (인수공통 X).",
           "X|③::다른 탄수화물은 못 먹고 <b>다른 입속 균이 만든 젖산만</b> 발효.", "O|④::강의의 화학식 그대로.", "O|⑤::충치·치석·치주염 (드물게 골수염·심내막염).",
           "KEY|Veillonella = 입속 젖산 먹보"]),
 dict(part="gp", ref="통합본 1-2", kw="class Mollicutes", kwk="몰리큐트 강",
      opts=["no cell wall", "pleomorphism", "sensitive to β-lactams", "movement through gliding", "the smallest bacteria in physical and genomic size"],
      topts=["세포벽 없음", "다형성(모양이 제각각)", "β-락탐계(페니실린 등)에 감수성", "활주운동으로 이동", "몸 크기와 유전체 크기가 가장 작은 세균"],
      ans="①, ②, ④, ⑤",
      exp=["O|①::mollis(부드러운)+cutis(피부) → 세포벽 X.", "O|②::벽이 없어 모양이 제멋대로.", "X|③::세포벽이 없으니 β-락탐이 <b>공격할 곳이 없음 → not affected</b>.",
           "O|④::대부분 <b>gliding</b> (일부는 비틀기).", "O|⑤::가장 작은 세균 → 동식물에 기생.", "KEY|벽 없음 → 다형성 → 페니실린 무효"], fig=svgs.CELLWALL, figw=36),
 dict(part="gp", ref="통합본 1-2", kw="atypical pneumonia", kwk="이형(비정형) 폐렴의 원인균",
      opts=["<i>Mycoplasma pneumoniae</i>", "<i>Legionella pneumophila</i>", "<i>Streptococcus pneumoniae</i>", "<i>Coxiella burnetii</i>", "<i>Klebsiella pneumoniae</i>"],
      topts=["마이코플라스마 뉴모니애", "레지오넬라 뉴모필라", "폐렴구균", "콕시엘라 버네티", "클렙시엘라 뉴모니애"],
      ans="①, ②, ④",
      exp=["O|①::'walking pneumonia'의 대표.", "O|②::이형 폐렴 (냉방병).", "X|③::<b>전형(typical) 폐렴</b>의 대표.", "O|④::이형 폐렴 (Q열).", "X|⑤::<b>전형 폐렴</b> (S. aureus, H. influenzae, P. aeruginosa와 함께).",
           "TIP|이형 폐렴 4총사 = '마·레·코·클' (+ Chlamydophila pneumoniae)"]),
 dict(part="gp", ref="통합본 1-2", kw="Ureaplasma urealyticum", kwk="유레아플라스마",
      opts=["normal genital flora of both men and women", "found in about 70% of sexually active humans", "non-gonococcal urethritis (NGU)", "infertility and premature birth", "thick peptidoglycan layer"],
      topts=["남녀 모두의 생식기 정상균", "성생활하는 사람의 약 70%에서 발견", "비임균성 요도염", "불임과 조산", "두꺼운 펩티도글리칸 층"],
      ans="①, ②, ③, ④",
      exp=["O|①::생식기 정상균.", "O|②::약 70%.", "O|③::NGU, 신우신염.", "O|④::불임·사산·조산, 신생아 폐렴·수막염.", "X|⑤::Mollicutes → <b>세포벽 자체가 없음</b>.",
           "KEY|'정상균 vs 성병(?)' — 정상균이면서 병도 일으킴"]),
 dict(part="gp", ref="통합본 1-3", kw="phylum Actinomycetota", kwk="방선균 문",
      opts=["previously, Actinobacteria", "producing endospores", "formerly classified to fungi", "now classified to bacteria based on 16S rRNA", "secondary metabolites such as antibiotics"],
      topts=["옛 이름 Actinobacteria", "내생포자 생산", "옛날엔 곰팡이로 분류", "16S rRNA 등을 근거로 지금은 세균으로 분류", "항생제 같은 2차 대사산물"],
      ans="①, ③, ④, ⑤",
      exp=["O|①::Actinomycetota ← Actinobacteria.", "X|②::<b>무성포자</b>는 만들지만 <b>내생포자 X</b> (내생포자는 Clostridium).", "O|③::균사(mycelia) 때문에 곰팡이로 오해.",
           "O|④::세포벽 구조 + 16S rRNA → 세균.", "O|⑤::항생제 공장.", "KEY|내생포자 = Bacillota(Clostridium) / 무성포자·균사 = Actinomycetota"], fig=svgs.GP_TREE, figw=40),
 dict(part="gp", ref="통합본 1-3", kw=LINK, kwk="연결이 옳은 것을 모두 고르시오", link=True, kw2="속 - 생산물",
      opts=["<i>Micromonospora</i> - gentamicin", "<i>Streptomyces</i> - streptomycin", "<i>Corynebacterium glutamicum</i> - glutamate, lysine", "<i>Propionibacterium</i> - penicillin", "<i>Bifidobacterium</i> - probiotics"],
      topts=["마이크로모노스포라 - 겐타마이신", "스트렙토마이세스 - 스트렙토마이신", "C. glutamicum - 글루탐산·라이신", "프로피오니박테리움 - 페니실린", "비피도박테리움 - 프로바이오틱스(유익균)"],
      ans="①, ②, ③, ⑤",
      exp=["O|①::아미노글리코사이드 gentamicin·sisomicin.", "O|②::streptomycin·kanamycin·neomycin.", "O|③::산업용 비병원성 균.",
           "X|④::Propionibacterium은 <b>프로피온산</b>(치즈·방부제·향료). 페니실린은 곰팡이(<i>Penicillium</i>).", "O|⑤::대장 주요 유익균.",
           "TIP|-mi<b>c</b>in = Mi<b>c</b>romonospora / -m<b>y</b>cin = Strept<b>o</b>m<b>y</b>ces"]),
 dict(part="gp", ref="통합본 1-3", kw="Corynebacterium diphtheriae", kwk="디프테리아균",
      opts=["diphtheria toxin, an exotoxin", "club-shaped", "myocarditis in about 20% of severe cases", "DTaP vaccine", "forming endospores"],
      topts=["외독소인 디프테리아 독소", "곤봉 모양", "심한 경우 약 20%에서 심근염", "DTaP 백신", "내생포자 형성"],
      ans="①, ②, ③, ④",
      exp=["O|①::<b>외독소</b>가 병의 원인.", "O|②::club-shaped (곤봉).", "O|③::심근염 ~20%, 말초신경병 ~10%.", "O|④::강의 'vaccine: DTaP'.", "X|⑤::방선균류는 <b>내생포자 X</b>.",
           "KEY|디프테리아 = 외독소 · 곤봉균 · 인후 위막 · 심근염 · DTaP"], fig="g15b.jpg", figw=22),
 dict(part="gp", ref="통합본 1-3", kw="genus Mycobacterium", kwk="마이코박테리움 속",
      opts=["<i>M. tuberculosis</i> - tuberculosis", "<i>M. bovis</i> - bovine tuberculosis, zoonotic", "<i>M. leprae</i> - Hansen's disease", "order Actinomycetales", "family Mycobacteriaceae"],
      topts=["결핵균 - 결핵", "우결핵균 - 소 결핵, 인수공통", "나병균 - 한센병", "Actinomycetales 목", "Mycobacteriaceae 과"],
      ans="①, ②, ③, ⑤",
      exp=["O|①::결핵.", "O|②::강의 '<i>M. bovis</i>: bovine tuberculosis / zoonotic'.", "O|③::한센병(나병).", "X|④::목은 <b>Mycobacteriales</b>. Actinomycetales 목은 <i>Actinomyces</i>.",
           "O|⑤::Mycobacteriales > <b>Mycobacteriaceae</b> > <i>Mycobacterium</i>.", "TIP|과(-aceae)·목(-ales) 이름을 속 이름과 맞춰 보기"]),
 dict(part="gp", ref="통합본 1-3", kw="opportunistic infections in Actinomycetota", kwk="방선균류의 기회감염",
      opts=["<i>Actinomyces israelii</i> - actinomycosis", "<i>Nocardia asteroides</i> - slowly progressive pneumonia", "abscesses in the mouth, lungs and GI tract",
            "normal flora of the gingiva", "<i>Micromonospora</i> - gas gangrene"],
      topts=["A. israelii - 방선균증", "N. asteroides - 천천히 진행하는 폐렴", "입·폐·위장관의 농양", "잇몸의 정상균", "마이크로모노스포라 - 가스괴저"],
      ans="①, ②, ③, ④",
      exp=["O|①::방선균증(actinomycosis).", "O|②::폐 노카르디아증.", "O|③::방선균증의 특징 = <b>농양</b>.", "O|④::Actinomyces·Nocardia 모두 잇몸(치주낭)에 사는 정상균 → 면역↓ 때 기회감염.",
           "X|⑤::Micromonospora는 항생제(겐타마이신) 생산균. 가스괴저는 <i>C. perfringens</i>.", "KEY|평소 잇몸에 사는 균 → 기회감염"], fig="g14b.jpg", figw=24),
 # ===================== 바이러스
 dict(part="vr", ref="통합본 2-0", kw="바이러스", kwk="바이러스",
      opts=["크기: 20~400 nm", "filterable infectious agent", "일반적으로 광학현미경으로 관찰 가능", "절대기생체(obligate intracellular parasite)", "자신의 리보솜을 가짐"],
      topts=["크기 20~400 nm", "세균 거르는 필터를 통과하는 감염원", "보통 광학현미경으로 볼 수 있음", "세포 안에서만 증식하는 절대기생체", "자기 리보솜이 있음"],
      ans="①, ②, ④",
      exp=["O|①::20~400 nm (미미바이러스 최대 900 nm).", "O|②::'Small infectious agent (filterable)'.", "X|③::광학현미경 한계보다 작음 → <b>전자현미경</b>.",
           "O|④::숙주 없이 증식 불가.", "X|⑤::리보솜·미토콘드리아 등 <b>세포 구조 없음</b>.", "TIP|기출 1번과 같은 유형! '모든/항상' 단어 주의"], fig=svgs.SIZE, figw=40),
 dict(part="vr", ref="통합본 2-0", kw=LINK, kwk="연결이 옳은 것을 모두 고르시오", link=True, kw2="인물 - 업적",
      opts=["Edward Jenner - smallpox vaccination using vaccinia (cowpox)", "Louis Pasteur - rabies vaccine", "Charles Chamberland - filter with pores smaller than bacteria",
            "Wendell Stanley - virus being liquid", "Friedrich Loeffler - first animal virus (foot-and-mouth disease)"],
      topts=["제너 - 우두를 이용한 천연두 예방(종두법)", "파스퇴르 - 광견병 백신", "샹베를랑 - 세균보다 작은 구멍의 필터", "스탠리 - 바이러스는 액체", "뢰플러 - 최초의 동물 바이러스(구제역)"],
      ans="①, ②, ③, ⑤",
      exp=["O|①::종두법(jennerization).", "O|②::약하게 만든 병원체로 광견병 백신.", "O|③::Chamberland filter.",
           "X|④::'액체'라고 한 사람은 <b>Beijerinck</b>(틀린 주장). Stanley는 핵단백질 결정을 분리해 <b>입자(particulate)</b>임을 증명.",
           "O|⑤::구제역 바이러스.", "TIP|기출 3·5번 '인물-업적 연결' 유형"]),
 dict(part="vr", ref="통합본 2-0", kw="viral envelope", kwk="바이러스 외피",
      opts=["derived from portions of the host cell membranes", "sensitive to ether, chloroform and bile salts", "easier to sterilize than non-enveloped viruses",
            "resistant to desiccation and heat", "can cause persistent infections"],
      topts=["숙주 세포막 일부에서 유래", "에테르·클로로포름·담즙산염에 약함", "외피 없는 바이러스보다 소독이 쉬움", "건조와 열에 강함", "지속 감염을 일으킬 수 있음"],
      ans="①, ②, ③, ⑤",
      exp=["O|①::인지질(숙주) + 바이러스 당단백질.", "O|②::지용성 용매가 인지질을 녹임.", "O|③::강의 'easier to sterilize'.", "X|④::건조·열·세제에 <b>약함</b>.",
           "O|⑤::빠르게 변해 적응 → 지속 감염.", "KEY|외피 = 기름옷 → 기름(에테르)에 녹는다"], fig=svgs.VSTRUCT, figw=38),
 dict(part="vr", ref="통합본 2-0", kw="prion", kwk="프리온",
      opts=["PrP<sup>Sc</sup>: abnormal isoform rich in β-sheet", "containing RNA as genetic material", "extremely stable to heat and proteases",
            "spongiform architecture of brain tissue", "effective vaccine available in humans"],
      topts=["PrPSc: β-시트가 많은 비정상형", "유전물질로 RNA를 가짐", "열과 단백질분해효소에 매우 안정", "뇌 조직의 해면(스펀지) 모양", "사람용 효과적 백신이 있음"],
      ans="①, ③, ④",
      exp=["O|①::정상 PrP<sup>C</sup>가 잘못 접힌 형태(아밀로이드).", "X|②::<b>단백질만</b>으로 된 감염원 (핵산 X).", "O|③::그래서 일반 멸균으로 잘 안 죽음.",
           "O|④::신경세포에 구멍 → 해면상 뇌병증(광우병, CJD).", "X|⑤::백신·치료 없음 (쥐에서만 효과).", "KEY|프리온 = 단백질 · 잘못 접힘 · 잠복 김 · 스펀지 뇌"], fig="v11.jpg", figw=30),
 dict(part="vr", ref="통합본 2-0", kw=LINK, kwk="연결이 옳은 것을 모두 고르시오", link=True, kw2="Baltimore group - family",
      opts=["Group I (dsDNA) - Herpesviridae", "Group III (dsRNA) - Reoviridae", "Group IV (+ssRNA) - Orthomyxoviridae", "Group VI (ssRNA-RT) - Retroviridae", "Group VII (dsDNA-RT) - Hepadnaviridae"],
      topts=["I군(이중 DNA) - 헤르페스", "III군(이중 RNA) - 레오", "IV군((+)단일 RNA) - 오르토믹소", "VI군(역전사 RNA) - 레트로", "VII군(역전사 DNA) - 헤파드나"],
      ans="①, ②, ④, ⑤",
      exp=["O|①::헤르페스(+폭스·아데노·파포바).", "O|②::레오(로타).", "X|③::오르토믹소(인플루엔자)는 <b>V군 (−)ssRNA</b>. IV군은 코로나·피코르나·플라비·토가·칼리시.",
           "O|④::레트로(HIV).", "O|⑤::헤파드나(HBV).", "KEY|모든 바이러스는 결국 (+)mRNA를 만든다 — 그 경로로 분류"], fig=svgs.BALTIMORE, figw=44),
 dict(part="vr", ref="통합본 2-1", kw="Poxviridae", kwk="폭스바이러스과",
      opts=["enveloped, one of the largest viruses", "brick-shaped capsid lacking symmetry", "DNA replication in the nucleus", "variola virus (smallpox)", "live-attenuated vaccinia vaccine"],
      topts=["외피 있음, 가장 큰 바이러스 중 하나", "대칭이 없는 벽돌 모양 캡시드", "핵에서 DNA 복제", "바리올라 바이러스(천연두)", "약독화 생백신(백시니아)"],
      ans="①, ②, ④, ⑤",
      exp=["O|①::200~400 nm, 외피 O.", "O|②::벽돌/타원형.", "X|③::자기 DNA 중합효소로 <b>세포질</b>에서 복제 ('unusual cytoplasmic DNA virus').",
           "O|④::천연두.", "O|⑤::vaccinia 생백신 → 1979(1980) 박멸.", "KEY|DNA 바이러스는 보통 핵, <b>폭스만 세포질</b>"]),
 dict(part="vr", ref="통합본 2-1", kw="Adenoviridae", kwk="아데노바이러스과",
      opts=["the largest non-enveloped virus", "icosahedral nucleocapsid with 252 capsomers", "coxsackievirus-adenovirus receptor (CAR)", "specific antiviral drugs available", "vector for gene therapy"],
      topts=["외피 없는 바이러스 중 가장 큼", "캡소미어 252개의 정이십면체", "콕사키-아데노 수용체(CAR)", "특이 항바이러스제가 있음", "유전자 치료 벡터"],
      ans="①, ②, ③, ⑤",
      exp=["O|①::90~100 nm, 비외피 중 최대.", "O|②::펜톤 12 + 헥손 240.", "O|③::CAR + 보조수용체 αv 인테그린.", "X|④::<b>항바이러스제 X, 백신 X</b> → 손 씻기.",
           "O|⑤::E3 자리에 외래 유전자 삽입 → 재조합 백신, 유전자 치료.", "KEY|아데노 = 튼튼한 비외피 · 눈병·감기 · 약 X · 벡터"], fig="v8.jpg", figw=34),
 dict(part="vr", ref="통합본 2-2", kw=LINK, kwk="연결이 옳은 것을 모두 고르시오", link=True, kw2="herpesvirus - site of latency",
      opts=["HSV-1 - trigeminal ganglion", "HSV-2 - sacral ganglion", "VZV - cerebral or posterior root ganglia", "HCMV - neurons only", "HSV-1 - genital herpes mainly"],
      topts=["HSV-1 - 3차 신경절", "HSV-2 - 엉치(천골) 신경절", "VZV - 뇌·척수 후근 신경절", "CMV - 신경세포에만", "HSV-1 - 주로 생식기 포진"],
      ans="①, ②, ③",
      exp=["O|①::구순포진 → 3차 신경절.", "O|②::생식기 포진 → 엉치 신경절.", "O|③::수두 → 후근 신경절 → 대상포진.", "X|④::CMV 잠복 장소는 <b>단핵구·림프구</b>.",
           "X|⑤::HSV-1은 주로 <b>구순포진</b>(oral). 생식기는 HSV-2.", "TIP|숫자가 커지면 아래로: 1형 = 입, 2형 = 엉치"], fig=svgs.HERPES, figw=32),
 dict(part="vr", ref="통합본 2-2", kw="acyclovir", kwk="아시클로버",
      opts=["guanosine analogue", "activated by phosphorylation by viral thymidine kinase", "active for HSV-1 and HSV-2", "inhibits viral neuraminidase", "valacyclovir is its derivative"],
      topts=["구아노신 유사체", "바이러스 티미딘 인산화효소가 인산을 붙여 활성화", "HSV-1, HSV-2에 효과", "바이러스 뉴라미니다아제를 억제", "발라시클로버는 그 유도체"],
      ans="①, ②, ③, ⑤",
      exp=["O|①::구아노신 짝퉁.", "O|②::감염세포에서만 활성화 → 선택성.", "O|③::+VZV, CMV, EBV.", "X|④::NA 억제는 <b>oseltamivir·zanamivir</b>(독감). ACV는 <b>바이러스 DNA 중합효소</b> 억제.",
           "O|⑤::valacyclovir = 경구 흡수 좋은 전구약물.", "KEY|ACV → (바이러스 TK) → ACV-인산3 → DNA pol 억제"], fig=svgs.ACV, figw=40),
 dict(part="vr", ref="통합본 2-3", kw="human papillomavirus", kwk="사람 유두종바이러스",
      opts=["non-enveloped, circular dsDNA", "E6 and E7: oncogenes inactivating p53", "HPV 16, 18 - cervical cancer", "Pap smear for diagnosis", "live-attenuated vaccine (Gardasil)"],
      topts=["외피 없는 원형 이중가닥 DNA", "E6·E7 = p53을 불활성화하는 발암유전자", "HPV 16·18 - 자궁경부암", "Pap smear로 진단", "약독화 생백신(가다실)"],
      ans="①, ②, ③, ④",
      exp=["O|①::파포바: 비외피 원형 dsDNA.", "O|②::종양억제단백질 억제.", "O|③::고위험형.", "O|④::자궁경부 세포검사.",
           "X|⑤::Gardasil·Cervarix는 <b>VLP(바이러스 유사 입자) 백신</b> — L1 껍데기만, 생백신 아님.", "KEY|HPV 백신 = VLP (16·18 + Gardasil은 6·11까지)"]),
 dict(part="vr", ref="통합본 2-4", kw="rotavirus", kwk="로타바이러스",
      opts=["segmented dsRNA genome (family Reoviridae)", "the most common cause of severe diarrhea among infants", "fecal-oral transmission", "oral vaccine", "specific antiviral drugs available"],
      topts=["분절된 이중가닥 RNA (레오과)", "영유아 중증 설사의 가장 흔한 원인", "분변-경구 전파", "먹는 백신", "특이 항바이러스제 있음"],
      ans="①, ②, ③, ④",
      exp=["O|①::10~12 분절 dsRNA.", "O|②::로타 A가 >90%.", "O|③::환경에서 안정.", "O|④::경구 생백신 (1999 장중첩증으로 철수 → 2006 재개발).", "X|⑤::치료제 없음 → 수분 보충.",
           "TIP|로타 = 아기 설사 · 경구 백신 O / 노로 = 겨울 · 백신 X"]),
 dict(part="vr", ref="통합본 2-5", kw="Picornaviridae", kwk="피코르나바이러스과",
      opts=["non-enveloped, icosahedral", "(+) ssRNA genome", "poliovirus binds to CD155", "rhinovirus proliferates at 33-35 ℃", "replication in the nucleus"],
      topts=["외피 없는 정이십면체", "(+) 단일가닥 RNA", "폴리오바이러스는 CD155에 결합", "리노바이러스는 33~35℃에서 증식", "핵에서 복제"],
      ans="①, ②, ③, ④",
      exp=["O|①::pico = 작은.", "O|②::벗겨진 RNA 자체가 감염성.", "O|③::폴리오 'canyon' vs CD155.", "O|④::코 온도 → 코감기.", "X|⑤::피코르나는 <b>세포질</b>에서 복제.",
           "KEY|피코르나 = 폴리오·콕사키·에코·리노(엔테로) + HAV + 구제역"], fig="v95.jpg", figw=24),
 dict(part="vr", ref="통합본 2-6", kw=LINK, kwk="연결이 옳은 것을 모두 고르시오", link=True, kw2="virus - vector",
      opts=["Japanese encephalitis virus - <i>Culex</i>", "yellow fever virus - <i>Aedes aegypti</i>", "dengue virus - <i>Anopheles</i>", "Zika virus - <i>Aedes</i>", "hepatitis C virus - mosquito"],
      topts=["일본뇌염 - 집모기(Culex)", "황열 - 이집트숲모기(Aedes aegypti)", "뎅기 - 학질모기(Anopheles)", "지카 - 숲모기(Aedes)", "C형 간염 - 모기"],
      ans="①, ②, ④",
      exp=["O|①::C. tritaeniorhynchus.", "O|②::황열모기.", "X|③::뎅기도 <b>Aedes</b>. Anopheles는 말라리아(원충).", "O|④::Aedes (+수혈·성접촉).", "X|⑤::HCV는 <b>혈액·성접촉</b>.",
           "TIP|Aedes = 황열·뎅기·지카 / Culex = 일본뇌염·웨스트나일"]),
 dict(part="vr", ref="통합본 2-7", kw="Paramyxoviridae", kwk="파라믹소바이러스과",
      opts=["measles virus - Koplik spot", "mumps virus - swelling of the parotid glands", "RSV - forming syncytia by F protein", "segmented (−) ssRNA genome", "MMR: live-attenuated vaccine"],
      topts=["홍역 - 코플릭 반점", "볼거리 - 귀밑샘 부종", "RSV - F 단백질로 세포융합체 형성", "분절된 (−) 단일가닥 RNA", "MMR = 약독화 생백신"],
      ans="①, ②, ③, ⑤",
      exp=["O|①::입 안 흰 점.", "O|②::이하선염, 합병증 고환염.", "O|③::syncytial = 세포융합.", "X|④::파라믹소는 <b>비분절</b>. 분절은 인플루엔자(오르토믹소)·로타·번야.",
           "O|⑤::Measles·Mumps·Rubella 생백신.", "TIP|Para = 비분절 / Ortho(인플루엔자) = 8분절"], fig="v126.jpg", figw=20),
 dict(part="vr", ref="통합본 2-7", kw="rabies virus", kwk="광견병 바이러스",
      opts=["bullet-shaped (family Rhabdoviridae)", "Negri body", "neurotropic virus", "icosahedral capsid", "vaccine used for both prevention and therapy"],
      topts=["총알 모양 (랍도과)", "네그리 소체", "신경친화성 바이러스", "정이십면체 캡시드", "백신을 예방과 치료 모두에 사용"],
      ans="①, ②, ③, ⑤",
      exp=["O|①::rhabdos = 막대.", "O|②::세포질의 바이러스 공장.", "O|③::CNS 감염, 증상 후 거의 100% 사망.", "X|④::랍도는 <b>나선형(helical)</b> 캡시드 ('not icosahedral').",
           "O|⑤::잠복기가 길어 물린 뒤 백신이 효과 + 면역글로불린.", "KEY|광견병 = 총알 · 나선형 · Negri · 공수병 · 노출 후 백신"]),
 dict(part="vr", ref="통합본 2-8", kw="influenza A virus", kwk="A형 인플루엔자 바이러스",
      opts=["8-segmented (−) ssRNA genome", "hemagglutinin (HA) and neuraminidase (NA)", "antigenic shift - pandemic", "oseltamivir - M2 ion channel inhibitor", "replication in the nucleus"],
      topts=["8분절 (−) 단일가닥 RNA", "헤마글루티닌(HA)과 뉴라미니다아제(NA)", "항원 대변이 - 대유행", "오셀타미비르 - M2 이온통로 억제제", "핵에서 복제"],
      ans="①, ②, ③, ⑤",
      exp=["O|①::A·B = 8분절 (C = 7).", "O|②::H 18 × N 11 아형.", "O|③::분절 재편성 → 팬데믹.", "X|④::oseltamivir = <b>NA 억제제</b>. M2 억제제는 <b>amantadine·rimantadine</b>.",
           "O|⑤::RNA 바이러스지만 핵에서 복제.", "KEY|-amivir = NA / -adine = M2"], fig=svgs.FLU, figw=44),
 dict(part="vr", ref="통합본 2-9", kw="human immunodeficiency virus (HIV)", kwk="HIV",
      opts=["receptor: CD4", "co-receptor: CCR5 or CXCR4", "reverse transcriptase: RNA-dependent DNA polymerase", "provirus integrated into host DNA", "AZT (zidovudine): protease inhibitor"],
      topts=["수용체 CD4", "보조수용체 CCR5 또는 CXCR4", "역전사효소 = RNA 의존 DNA 중합효소", "숙주 DNA에 끼어든 프로바이러스", "AZT(지도부딘) = 단백분해효소 억제제"],
      ans="①, ②, ③, ④",
      exp=["O|①::gp120 ↔ CD4.", "O|②::M-향성 CCR5 / T-향성 CXCR4.", "O|③::(+)RNA → (−)DNA → (±)DNA.", "O|④::통합효소가 삽입.",
           "X|⑤::AZT = <b>NRTI</b>(뉴클레오사이드 역전사효소 억제제). PI는 <b>-navir</b>.", "KEY|HIV 약 = NRTI · NNRTI · PI · 융합/부착 억제 · 통합효소 억제 → HAART"], fig=svgs.RETRO, figw=44),
 dict(part="vr", ref="통합본 2-10", kw="hepatitis B virus (HBV)", kwk="B형 간염 바이러스",
      opts=["partially double-stranded, circular DNA", "Dane particle: complete, infectious virion", "HBsAg particle (~22 nm): infectious", "chronic hepatitis B in 80~90% of infected infants", "recombinant HBsAg vaccine"],
      topts=["부분 이중가닥 원형 DNA", "Dane 입자 = 완전한 감염성 바이러스", "HBsAg 입자(~22 nm) = 감염성", "감염된 영아의 80~90%가 만성 B형 간염", "재조합 HBsAg 백신"],
      ans="①, ②, ④, ⑤",
      exp=["O|①::부분 dsDNA, pregenomic RNA를 역전사.", "O|②::42~47 nm.", "X|③::HBsAg 입자는 DNA 없는 빈 껍데기 → <b>비감염성</b>.",
           "O|④::어릴수록 만성 (성인 5~10%).", "O|⑤::재조합 HBsAg.", "KEY|HBV = DNA인데 역전사 · Dane(감염성) vs HBsAg(비감염성)"], fig="v159.jpg", figw=24),
]

# ---------------------------------------------------------------- 서술형 데이터
ESSAY = [
 dict(part="gp", ref="통합본 기초", pts=1, term="zoonosis",
      tr="인수공통감염병(zoonosis)의 뜻을 쓰시오.",
      ans="동물과 사람 사이에서 전파되는 감염병 (인수공통감염병)",
      exp=["<b>모범답안</b>: 척추동물과 사람 사이에서 자연적으로 전파되는 감염병.",
           "강의 예: <i>M. bovis</i>(우결핵), 인플루엔자 A, MERS(박쥐→낙타→사람), 일본뇌염(돼지), 한타(쥐), 광견병, 엠폭스.",
           "반대 예(함정): Clostridium은 동물을 감염시키지만 'not zoonotic'.",
           "TIP|zoo(동물) + nosos(병) → 동물에서 오는 병"]),
 dict(part="gp", ref="통합본 1-1", pts=2, term="botulinum toxin vs. tetanospasmin (작용 기전과 증상 비교)",
      tr="보툴리눔 독소와 파상풍 독소(tetanospasmin)의 작용 기전과 증상을 비교하시오.",
      ans="보툴리눔 = 아세틸콜린 방출 차단 → 이완성(하향성) 마비 / 파상풍 = 억제성 전달물질(GABA·글리신) 방출 차단 → 강직성 경련",
      exp=["<b>채점 포인트 ① 기전 (1점)</b>: 보툴리눔 독소는 운동신경 말단에서 <b>아세틸콜린 방출</b>을 막음 / tetanospasmin은 CNS의 억제성 신경에서 <b>GABA·글리신 방출</b>을 막음.",
           "<b>채점 포인트 ② 증상 (1점)</b>: 보툴리눔 → 눈·삼킴·말하기·호흡 순으로 내려오는 <b>이완성 마비</b> / 파상풍 → 아관긴급, 억지 웃음, 후궁반장, 발작 등 <b>강직성 경련</b>.",
           "둘 다 혐기성 포자형성 그람양성 간균의 단백질 신경독(외독소).",
           "KEY|스위치 OFF(보툴리눔) vs 브레이크 고장(파상풍)"], fig=svgs.NEUROTOX, figw=44),
 dict(part="gp", ref="통합본 1-2", pts=2, term="Mollicutes and β-lactam antibiotics (정의 및 내성 이유)",
      tr="Mollicutes(마이코플라스마류)가 무엇인지 쓰고, β-락탐 항생제가 듣지 않는 이유를 설명하시오.",
      ans="세포벽 없는 가장 작은 세균(Mycoplasma, Ureaplasma) / β-락탐은 펩티도글리칸 세포벽 합성을 막는데, 세포벽이 없어 표적이 없음",
      exp=["<b>채점 포인트 ① 정의 (1점)</b>: Mycoplasmatota 문의 강, mollis(부드러운)+cutis(피부). <b>세포벽이 없고</b> 다형성, 활주운동, 몸·유전체가 가장 작은 세균. 예: <i>M. pneumoniae</i>(이형 폐렴), <i>U. urealyticum</i>(NGU).",
           "<b>채점 포인트 ② 이유 (1점)</b>: β-락탐(페니실린·세팔로스포린)은 <b>펩티도글리칸 합성(교차결합)을 억제</b>해 세포벽을 무너뜨림 → Mollicutes는 펩티도글리칸 자체를 만들지 않으니 <b>작용할 표적이 없음</b>.",
           "보너스: 벽 대신 세포막에 <b>콜레스테롤(스테롤)</b>을 넣어 버팀.",
           "KEY|표적이 없으면 약도 없다"], fig=svgs.CELLWALL, figw=38),
 dict(part="vr", ref="통합본 2-0", pts=2, term="Baltimore classification (정의, 분류 기준, 7 groups)",
      tr="볼티모어 분류의 정의와 분류 기준을 쓰고, 7개 그룹을 나열하시오.",
      ans="유전체가 (+)mRNA를 만드는 방식(복제 방식)에 따라 바이러스를 7군으로 나눈 분류: I dsDNA, II ssDNA, III dsRNA, IV (+)ssRNA, V (−)ssRNA, VI ssRNA-RT, VII dsDNA-RT",
      exp=["<b>채점 포인트 ① 정의·기준 (1점)</b>: 바이러스 <b>유전체의 복제 방식</b>, 즉 '유전체로부터 <b>(+) mRNA를 어떻게 만드는가</b>'를 기준으로 한 분류. (모든 바이러스는 단백질을 만들려면 (+)mRNA가 필요)",
           "<b>채점 포인트 ② 7군 (1점)</b>: I dsDNA(헤르페스·폭스) · II ssDNA(파보) · III dsRNA(레오) · IV (+)ssRNA(피코르나·코로나·플라비) · V (−)ssRNA(인플루엔자·파라믹소·랍도) · VI ssRNA-RT(레트로) · VII dsDNA-RT(헤파드나).",
           "비교: ICTV 분류 = 목(-virales) > 과(-viridae) > 아과(-virinae) > 속(-virus) > 종."], fig=svgs.BALTIMORE, figw=46),
 dict(part="vr", ref="통합본 2-2", pts=2, term="latent infection of Herpesviridae (정의 및 잠복 장소 예 2가지)",
      tr="헤르페스바이러스과의 잠복감염의 뜻을 쓰고, 잠복 장소의 예를 2가지 쓰시오.",
      ans="증상 없이 바이러스 유전체가 세포 안에 평생 숨어 있다가 면역 저하 시 재활성화되는 것 / 예: HSV-1 3차 신경절, HSV-2 엉치 신경절, VZV 후근 신경절, CMV 단핵구·림프구",
      exp=["<b>채점 포인트 ① 정의 (1점)</b>: 처음 감염 후 바이러스가 증식을 멈추고 <b>신경절 등에 숨어(LAT RNA 축적) 평생 지속</b>하다가, 스트레스·면역 저하 시 <b>재활성화</b>되어 다시 병을 일으키는 상태 (herpein = 기어가다).",
           "<b>채점 포인트 ② 예 2가지 (1점)</b>: HSV-1 → <b>3차 신경절</b> / HSV-2 → <b>엉치(천골) 신경절</b> / VZV → 뇌·척수 <b>후근 신경절</b>(대상포진) / CMV → 단핵구·림프구.",
           "그래서 acyclovir로 증식은 막아도 <b>완치는 안 됨</b>."], fig=svgs.HERPES, figw=32),
 dict(part="vr", ref="통합본 2-8", pts=2, term="antigenic drift vs. antigenic shift",
      tr="인플루엔자의 항원 소변이(drift)와 항원 대변이(shift)를 비교하여 설명하시오.",
      ans="drift = HA·NA 유전자의 점돌연변이 누적 → 계절 유행 / shift = 분절 유전체 재편성으로 새 아형 출현 → 대유행(A형만)",
      exp=["<b>채점 포인트 ① drift (1점)</b>: RNA 복제 오류로 HA·NA에 <b>점돌연변이가 조금씩 누적</b> → 기존 면역을 일부 회피 → <b>매년 계절 유행</b>, 그래서 백신을 매년 교체.",
           "<b>채점 포인트 ② shift (1점)</b>: 한 세포(주로 돼지)에 서로 다른 인플루엔자가 동시 감염 → 8개 <b>RNA 분절이 재편성(reassortment)</b> → 완전히 새로운 HA/NA 조합 → 아무도 면역 없음 → <b>대유행(팬데믹)</b>. 다양한 동물 숙주를 가진 <b>A형</b>에서만.",
           "TIP|drift = 표류(조금씩) / shift = 교대(통째로)"], fig=svgs.FLU, figw=46),
 dict(part="vr", ref="통합본 2-9", pts=2, term="life cycle of retroviruses (역전사 과정과 바이러스 효소 3가지)",
      tr="레트로바이러스의 생활사를 역전사 과정을 포함하여 설명하고, pol 유전자가 만드는 효소 3가지를 쓰시오.",
      ans="부착 → 침입 → 역전사((+)ssRNA → (−)DNA → (±)DNA) → 통합(provirus) → 전사·번역 → 단백분해·조립 → 출아 / 효소: 역전사효소, 통합효소, 단백분해효소",
      exp=["<b>채점 포인트 ① 과정 (1점)</b>: env가 수용체(HIV: CD4 + CCR5/CXCR4)에 부착 → RNA와 효소가 세포로 → <b>역전사: (+)ssRNA → (−)DNA → (±)DNA</b> → 숙주 염색체에 <b>통합 = provirus</b> → (+)mRNA 전사·번역 → 단백분해효소가 gag·pol 절단 → 조립·방출.",
           "<b>채점 포인트 ② 효소 3가지 (1점)</b>: <b>역전사효소</b>(RNA 의존 DNA 중합효소), <b>통합효소</b>(integrase), <b>단백분해효소</b>(protease). 모두 바이러스 자체 효소 → 약물 표적(NRTI·NNRTI / -gravir / -navir).",
           "유전체는 (+)ssRNA <b>2개(dimer)</b>, 유전자 gag·pol·env."], fig=svgs.RETRO, figw=46),
]

# ---------------------------------------------------------------- 렌더링
TOTAL_MC = len(MC)
TOTAL = TOTAL_MC + sum(e["pts"] for e in ESSAY)


def stem(i, d):
    if d.get("link"):
        return f"{i}. {LINK} <span class='kw2'>[{d['kw2']}]</span> 정답: <span class='uline'></span>"
    return f"{i}. ({d['kw']}) 정답: <span class='uline'></span>"


def tstem(i, d):
    if d.get("link"):
        return f"{i}. [{d['kw2']}] 연결이 <b>옳은</b> 것을 모두 고르시오."
    return f"{i}. (<b>{d['kwk']}</b>)에 대한 설명으로 옳거나 관련 있는 것을 <b>모두</b> 고르시오."


RAW(f'''<section class="page cover vr">
 <div class="l" style="background:linear-gradient(135deg,#5847d6 0%,#2a6fb5 55%,#0e8a6a 100%)">
  <div class="chip">약품미생물학 · 2026 가을학기 · 중간고사 대비</div>
  <h1>통합모의고사<br><span style="font-size:20pt;font-weight:700">그람양성균 + 바이러스</span></h1>
  <p>2-1학기 미생물학 중간고사 기출 스타일<br>"(키워드) 정답: ___" 모두 고르기 + 용어 서술형</p>
  <p style="margin-top:8mm;font-size:11pt;opacity:.9">총 {TOTAL}점 만점 · 객관식 {TOTAL_MC}문항(각 1점) · 서술형 {len(ESSAY)}문항</p>
 </div>
 <div class="r">
  <div style="font-weight:800;font-size:13pt">구성</div>
  <div class="toc"><!--TOC--></div>
  <div class="card2 warm" style="margin-top:3mm"><h4>추천 사용법</h4>
   <ul class="b"><li>① <b>실전 시험지</b>(4쪽)를 60분 타이머 켜고 풀기</li><li>② 문항별 페이지에서 정답·해설 확인</li><li>③ 맨 뒤 <b>빠른 정답표</b>로 채점 → 점수 기록</li><li>④ 틀린 문항의 '통합본 단원'을 다시 보기</li></ul></div>
 </div>
</section>''')

# ---------- 실전 시험지 (기출 스타일)
SEC("실전 시험지", "실전 시험지 (기출 스타일, 답 없음)")


def sheet_q(i, d):
    o = "".join(f"<li>{MARKS['circle'][k]} {t}</li>" for k, t in enumerate(d["opts"]))
    return f'<div class="sq"><div class="sqh">{stem(i, d)}</div><ol>{o}</ol></div>'


per = 12
chunks = [MC[k:k + per] for k in range(0, len(MC), per)]
n = 1
for ci, ch in enumerate(chunks):
    head = ('<div class="sheet-ins">▣ 아래 객관식 문항의 답은 답가지 번호에 표시하지 말고 "정답:" 옆에 답을 쓰시오.<br>'
            '※ 괄호 안의 키워드에 대한 설명이 옳거나 관련성이 있는 것을 모두 고르시오(각 1점).</div>') if ci == 0 else ""
    qs = ""
    for d in ch:
        qs += sheet_q(n, d)
        n += 1
    RAW(f'''<section class="page sheet vr"><div class="sheet-top"><b>2026년 2학기 약품미생물학 중간고사 대비 통합모의고사</b><span>총 {TOTAL}점 · 이름: ________ · 점수: ____ / {TOTAL}</span></div>{head}<div class="sheet-cols">{qs}</div></section>''')

es = ""
for k, e in enumerate(ESSAY):
    es += f'<div class="sq essay"><div class="sqh">{TOTAL_MC + k + 1}. ({e["pts"]}점) {e["term"]}</div><div class="eline"></div></div>'
RAW(f'''<section class="page sheet vr"><div class="sheet-top"><b>서술형</b><span>※ Please define and/or describe the following terms.</span></div><div class="sheet-cols ess">{es}</div></section>''')

# ---------- 문항별 정답·해설 (통합본 양식)
SEC("PART 1 · 객관식 해설", f"객관식 1~{TOTAL_MC}번 (원문 → 번역 → 풀이 → 정답·해설)")
for i, d in enumerate(MC, 1):
    topic = ("그람양성균 · " if d["part"] == "gp" else "바이러스 · ") + (d["kw2"] if d.get("link") else d["kw"])
    Q(d["part"], topic, d["ref"] + " 참고", stem(i, d), tstem(i, d), d["ans"], d["exp"],
      opts=d["opts"], topts=d["topts"], cols=1, fig=d.get("fig"), figw=d.get("figw", 34),
      qlabel=f"{i}번 · 1점", olabel="원문 (시험지)")

SEC("PART 2 · 서술형 해설", f"서술형 {TOTAL_MC + 1}~{TOTAL_MC + len(ESSAY)}번 (모범답안 + 채점 포인트)")
for k, e in enumerate(ESSAY):
    i = TOTAL_MC + k + 1
    Q(e["part"], "서술형 · " + e["term"].split(" (")[0], e["ref"] + " 참고",
      f"※ Please define and/or describe the following terms.<br>{i}. ({e['pts']}점) {e['term']}",
      f"{i}. ({e['pts']}점) {e['tr']}", e["ans"], e["exp"], fig=e.get("fig"), figw=e.get("figw", 34),
      qlabel=f"{i}번 · {e['pts']}점", olabel="원문 (시험지)")

# ---------- 빠른 정답표
SEC("채점", "빠른 정답표 · 점수 기록")
rows = []
for i, d in enumerate(MC, 1):
    rows.append([f"{i}", ("그람양성" if d["part"] == "gp" else "바이러스"), (d["kw2"] if d.get("link") else d["kw"]), f"<b>{d['ans']}</b>", d["ref"]])
half = (len(rows) + 1) // 2
t1 = table(["번호", "영역", "키워드", "정답", "복습"], rows[:half])
t2 = table(["번호", "영역", "키워드", "정답", "복습"], rows[half:])
S("vr", "채점", "빠른 정답표 (객관식, 각 1점 · 모두 맞혀야 1점)", f'<div class="row c2">{t1}{t2}</div>')
erows = [[f"{TOTAL_MC + k + 1}", f"{e['pts']}점", e["term"], e["ans"]] for k, e in enumerate(ESSAY)]
S("vr", "채점", "서술형 모범답안 요약 · 점수 기록",
  table(["번호", "배점", "용어", "모범답안 핵심"], erows) +
  '<div class="row c3">' +
  card("점수 기록", '<p style="font-size:1.1em;line-height:2.1">1회차: ____ / %d (객관식 ____ · 서술 ____)<br>2회차: ____ / %d<br>3회차: ____ / %d</p>' % (TOTAL, TOTAL, TOTAL), "soft") +
  card("채점 기준 (기출과 동일하게)", ul(["객관식은 <b>'모두 고르기'</b> → 정답 번호를 <b>전부 정확히</b> 써야 1점 (하나라도 빠지거나 더하면 0점)", "서술형은 채점 포인트별 부분 점수", "계산·서술은 근거가 있어야 점수"]), "warm") +
  card("틀렸다면", ul(["각 문항 머리의 <b>'통합본 단원'</b>을 다시 보기", "그람양성균: 통합본 1-0 ~ 1-3", "바이러스: 통합본 2-0 ~ 2-11"]), "") +
  '</div>')
