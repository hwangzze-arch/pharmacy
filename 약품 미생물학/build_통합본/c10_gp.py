# -*- coding: utf-8 -*-
from core import RAW, S, SEC, Q, card, ul, table, img
import svgs

P = "gp"
G1 = "PART 1 · 그람양성균"

RAW('''<section class="page divider gp"><div class="num">PART 1</div><h1>그람양성균 (Gram-positive bacteria)</h1>
<p>Clostridium 5형제 · Veillonella · Mycoplasma/Ureaplasma · 방선균(Actinomycetota) 8속<br>요약 4쪽 + 문제 29개</p></section>''')

# ------------------------------------------------------------------ 큰 그림
SEC(G1, "1-0 큰 그림: 분류 지도")
S(P, "1-0", "큰 그림: 그람양성균 분류 지도",
  f'<div class="card2 mid">{svgs.GP_TREE}</div>' +
  '<div class="row c3">' +
  card("이름이 바뀌었어요 (시험 함정)",
       table(["새 이름", "옛 이름"], [["Bacillota", "Firmicutes"], ["Actinomycetota", "Actinobacteria"],
                                     ["Clostridioides difficile", "Clostridium difficile"], ["C. perfringens", "C. welchii"],
                                     ["Cutibacterium acnes", "Propionibacterium acnes"]])) +
  card("분류 단위 순서",
       '<p class="big" style="text-align:center;margin:2mm 0">문 → 강 → 목 → 과 → 속 → 종</p>' +
       ul(["phylum → class → order → family → genus → species",
           "학명 = <i>속명 + 종명</i> (예: <i>Clostridium tetani</i>)",
           "과(family) 이름은 <b>-aceae</b>로 끝남 (Mycobacteriaceae)"])) +
  card("한 줄 요약",
       ul(["Clostridium = <b>혐기성 + 포자 + 독소</b>",
           "Mycoplasma = <b>벽 없음, 제일 작음</b>",
           "방선균 = <b>흙 속 항생제 공장</b> + 결핵·디프테리아 같은 병원균도 포함"]), "soft") +
  '</div>')

# ------------------------------------------------------------------ Clostridium
SEC(G1, "1-1 Clostridium (보툴리눔·파상풍·디피실·퍼프린젠스·소르델리)")
S(P, "1-1", "Clostridia 강 · Clostridium 속 개요",
  '<div class="row c21">' +
  card("Clostridia 강의 공통점",
       ul(["모양·크기가 다양 (다계통, polyphyletic)",
           "<span class='hl'>모두 절대 혐기성</span> (산소가 있으면 못 삶) + <span class='hl'>내생포자</span> 형성",
           "Clostridium 속 = 이 강에서 가장 큰 속 (~100종), 대부분은 죽은 유기물 먹고 사는 <b>부생균</b>",
           "사람에게 병을 주는 주요 5종: <b>botulinum · tetani · difficile · perfringens · sordellii</b>",
           "대부분 동물도 감염시키지만 <b>사람에게 옮기는 인수공통감염은 아님</b>"]), "soft") +
  img("g2.jpg", "C. tetani: 끝에 포자가 달린 '북채(drumstick)' 모양", 100) +
  '</div>' +
  table(["균", "어디서?", "무엇으로?", "무슨 병?", "키워드"], [
      ["<i>C. botulinum</i>", "흙·물 → 통조림, 꿀, 상처", "보툴리눔 독소 (신경독)", "보툴리누스증 (식중독형·영아형·상처형)", "<b>축 늘어지는 마비</b>, 사람 간 전파 X"],
      ["<i>C. tetani</i>", "흙 → 깊은 상처(못)", "tetanospasmin (신경독)", "파상풍", "<b>근육 경련</b>, 아관긴급, DPT 백신"],
      ["<i>C. difficile</i>", "장 정상균(소수)", "독소 A(장독소)·B(세포독소)", "<b>위막성 대장염</b>", "항생제(clindamycin) 후, 원내감염, 중독성 거대결장"],
      ["<i>C. perfringens</i><br>(옛 C. welchii)", "자연·장 정상균", "α·β·ε·ι 독소 + 장독소(CPE)", "식중독 / 괴사성 장염 / <b>가스괴저</b>", "CPE→식중독, β→pigbel, α→가스괴저"],
      ["<i>C. sordellii</i>", "드묾", "-", "산후·유산 후 부인과 감염, 신생아 배꼽 감염", "매우 드물지만 치명적, 패혈증"],
  ]))

S(P, "1-1", "보툴리눔 vs 파상풍: 같은 신경독, 반대 증상",
  f'<div class="row c32"><div class="card2">{svgs.NEUROTOX}</div>' +
  '<div style="display:flex;flex-direction:column;gap:2.4mm">' +
  card("C. botulinum 정리",
       ul(["어원: 라틴어 botulus = <b>소시지</b> (상한 소시지에서 발견)",
           "독소는 <b>혐기 조건</b>에서 만들어지는 단백질 → 진공·통조림 음식이 위험",
           "걸리는 3가지 길: ① 음식 속 독소 섭취 ② 영아 장에 균 정착(<b>꿀</b>) ③ 상처 오염",
           "<b>사람→사람, 동물→사람 직접 전파 없음</b>",
           "치사율 70% → 지금 5~10% / 진단: 검체에서 <b>독소 검출</b>"]), "soft") +
  card("C. tetani 정리",
       ul(["어원: 그리스어 tetanos = <b>팽팽함</b>", "흙 속 포자 → <b>깊은 찔린 상처</b>로 감염",
           "tetanospasmin이 <b>중추신경계(CNS)</b> 여러 곳에 작용",
           "증상: 억지 웃음, <b>아관긴급(lock-jaw)</b>, 활처럼 휜 등, 발작, 호흡부전",
           "치사율 최대 40% (어린이 ~90%) / 예방: <b>DPT 백신</b>"]), "soft") +
  '</div></div>' +
  '<div class="one-line">보툴리눔 = 스위치 OFF (흐물흐물) · 파상풍 = 브레이크 고장 (뻣뻣) · 둘 다 <b>혐기성 포자형성 그람양성 간균</b>의 단백질 외독소</div>')

S(P, "1-1", "C. difficile · C. perfringens · C. sordellii",
  '<div class="row c2">' +
  '<div style="display:flex;flex-direction:column;gap:2.4mm">' +
  card("C. difficile → 항생제 관련 위막성 대장염", f'{svgs.CDIFF}' +
       ul(["평소 장에 <b>조금</b> 있는 정상균 → 항생제(예: <b>clindamycin</b>)로 다른 균이 죽으면 폭증",
           "독소 A = <b>장독소</b>(enterotoxin), 독소 B = <b>세포독소</b>(cytotoxin)",
           "악취 설사·발열·복통, 심하면 <b>중독성 거대결장</b>(대장이 급격히 부풂)",
           "병원에서 잘 퍼짐 = <b>원내감염</b>"]), "soft") +
  '</div>' +
  '<div style="display:flex;flex-direction:column;gap:2.4mm">' +
  card("C. perfringens (옛 이름 C. welchii) → 독소별로 병이 다름",
       table(["독소", "병", "특징"], [["장독소 <b>CPE</b>", "<b>식중독</b>", "가장 흔한 식중독 원인 중 하나, 복통·설사, 가벼움"],
                                     ["<b>β 독소</b>", "괴사성 장염 (pigbel)", "식중독보다 심함, 치사율 50%"],
                                     ["<b>α 독소</b>", "<b>가스괴저</b>(근괴사)", "조직 속에 가스 + 괴사, 치명적"],
                                     ["-", "패혈증", ""]]) +
       '<div class="row c2" style="margin-top:1.6mm">' + img("g6.jpg", "가스괴저", 100) + img("g5a.jpg", "위막성 대장염 내시경", 100) + '</div>', "") +
  card("C. sordellii",
       ul(["매우 드물지만(2000년 이후 연 1건 미만) <b>치명적</b>",
           "산후·유산 후 여성 부인과 감염, 마약 주사자, 외상, <b>신생아 배꼽</b> 감염",
           "폐렴·심내막염·관절염·복막염·근괴사·패혈증"]), "") +
  '</div></div>')

# ---- 문제: Clostridium
T = "Clostridium 공통 · 보툴리눔"
Q(P, T, "추가 문제 (강의 슬라이드)",
  "Which of the following is NOT correct about the class <i>Clostridia</i> and the genus <i>Clostridium</i>?",
  "<i>Clostridia</i> 강과 <i>Clostridium</i> 속에 대한 설명으로 옳지 <b>않은</b> 것은?",
  "②, ⑤",
  ["O|①::모든 Clostridia는 <b>절대 혐기성 + 내생포자</b>. 강의 그대로.",
   "X|②::반대! Clostridium의 <b>대부분은 부생균</b>(죽은 유기물 분해). 병원균은 5종 정도뿐.",
   "O|③::약 100종으로 Clostridia 강에서 <b>가장 큰 속</b>.",
   "O|④::사람에게 병 주는 5종 = botulinum, tetani, difficile, perfringens, sordellii.",
   "X|⑤::Clostridium들은 동물을 감염시키지만 <b>인수공통감염병은 아님</b>(슬라이드: 'infecting animals, but not zoonotic').",
   "KEY|Clostridium = <b>혐기 · 포자 · 독소</b>, 그리고 '동물도 걸리지만 동물→사람 전파 병은 아님'."],
  opts=["All members of <i>Clostridia</i> are obligate anaerobes and form endospores.",
        "Most species of <i>Clostridium</i> are pathogenic to humans.",
        "<i>Clostridium</i> is the largest genus (~100 species) in this class.",
        "Five main species cause human disease, including <i>C. botulinum</i> and <i>C. tetani</i>.",
        "<i>C. tetani</i> and <i>C. botulinum</i> are typical zoonotic pathogens."],
  topts=["Clostridia는 모두 절대 혐기성이고 내생포자를 만든다.",
         "Clostridium 속의 대부분 종은 사람에게 병원성이다.",
         "Clostridium은 이 강에서 가장 큰 속(약 100종)이다.",
         "주요 사람 병원균은 5종이며 C. botulinum, C. tetani가 포함된다.",
         "C. tetani와 C. botulinum은 대표적인 인수공통감염 병원균이다."], cols=1)

Q(P, T, "교재 9장 14번",
  "보툴리누스 독소에 대한 설명으로 옳지 않은 것을 고르시오.",
  "보툴리눔 독소(<i>C. botulinum</i>이 만드는 독)에 대한 설명 중 <b>틀린</b> 것은?",
  "③",
  ["O|①::자연에 있는 독 중 <b>가장 강력</b>. 아주 극미량으로도 사람을 죽일 수 있음.",
   "O|②::<b>꿀</b> 속 포자 → 아기 장에서 균이 자라 독소 생산 = <b>영아 보툴리누스증</b>. 그래서 1세 미만에겐 꿀 금지!",
   "X|③::독소는 <b>단백질</b> → 열에 <b>약함</b>(끓이면 파괴). 열에 강한 건 '포자'이지 '독소'가 아님.",
   "O|④::콜린성(아세틸콜린) 신경 말단에서 신호 전달을 막는 <b>신경독</b>.",
   "O|⑤::대표적인 <b>혐기성 + 포자형성</b> 균 (Clostridia 공통).",
   "O|⑥::음식 속 독소를 먹어서 생기는 <b>독소형 식중독</b>.",
   "O|⑦::독소 유전자는 균을 감염한 <b>박테리오파지</b>(세균 바이러스)가 넣어 줌.",
   "TIP|포자 = 단단한 씨앗(열에 강함) / 독소 = 단백질(열에 약함). 헷갈리면 '계란도 익으면 변한다' 떠올리기."],
  opts=["자연 독 중 가장 독성이 강하다.", "소아가 꿀을 섭취하여 발병하기도 한다.", "열에 대한 저항성이 강한 편이다.",
        "Choline성 신경절에서 신경전달을 방해하는 신경독이다.", "원인 세균은 대표적인 혐기성균이며 포자를 형성한다.",
        "일종의 식중독을 유발한다.", "독소 유전자는 bacteriophage가 세균에게 제공한다."],
  topts=["자연에 있는 독 중 독성이 가장 세다.", "아기가 꿀을 먹고 걸리기도 한다.", "열에 강한 편이다.",
         "아세틸콜린을 쓰는 신경에서 신호 전달을 막는 신경 독이다.", "원인균은 산소를 싫어하는 균이며 포자를 만든다.",
         "식중독의 한 종류를 일으킨다.", "독소 유전자는 세균을 감염하는 바이러스(파지)가 넣어 준다."], cols=1,
  fig="g3b.jpg", figw=26)

Q(P, T, "교재 9장 91번",
  "하향성 마비증(상체에서 하체로 진행되는 마비증상)이 나타나는 환자가 감염되었을 균으로 가장 먼저 의심할 수 있는 균은?",
  "마비가 <b>위(얼굴·눈)에서 아래(팔·다리)로</b> 내려오는 환자. 가장 먼저 의심할 균은?",
  "<i>Clostridium botulinum</i> (보툴리눔균)",
  ["보툴리눔 독소는 근육에 '움직여' 신호(아세틸콜린)가 못 가게 막아 <b>축 늘어지는 마비</b>를 일으켜요.",
   "강의 슬라이드의 증상 순서: <b>눈 움직임 → 씹기 → 삼키기 → 말하기 → 호흡</b> 장애 = 머리에서 아래로 내려옴.",
   "마지막에 <b>호흡근</b>까지 마비되면 사망 → 그래서 치명적.",
   "KEY|하향성(위→아래) + 이완성(흐물흐물) 마비 = <b>보툴리눔</b> / 뻣뻣한 경련 = <b>파상풍</b>"],
  fig=svgs.NEUROTOX, figw=46)

Q(P, T, "추가 문제 (강의 슬라이드)",
  "Choose ALL correct statements about botulism caused by <i>C. botulinum</i>.",
  "<i>C. botulinum</i>이 일으키는 보툴리누스증에 대해 옳은 것을 <b>모두</b> 고르시오.",
  "①, ②, ④",
  ["O|①::강의: 3가지 경로 = <b>음식(식중독형)</b>, <b>영아 장 정착(영아형)</b>, <b>상처 오염(상처형)</b>.",
   "O|②::독소는 <b>혐기 조건</b>에서 만들어지는 단백질 → 진공포장·통조림·병조림이 위험.",
   "X|③::<b>사람→사람, 동물→사람 직접 전파는 일어나지 않음</b> (강의 명시).",
   "O|④::진단은 환자 검체(혈청·대변·음식)에서 <b>독소를 검출</b>하는 것.",
   "X|⑤::치사율은 과거 70%였지만 현재는 치료(항독소·인공호흡)로 <b>5~10%</b>.",
   "KEY|'독'이 병의 핵심 → 진단도 독소 검출, 사람끼리는 안 옮음."],
  opts=["Disease can develop by ingestion of toxin in food, colonization of the infant gut, or wound contamination.",
        "Botulinum toxin is a protein produced under anaerobic conditions.",
        "It is easily transmitted from person to person by droplets.",
        "Diagnosis is made by detection of botulinum toxin in clinical specimens.",
        "Lethality is still about 70% even with modern treatment."],
  topts=["음식 속 독소 섭취, 영아 장 내 균 정착, 상처 오염으로 발병할 수 있다.",
         "보툴리눔 독소는 혐기 조건에서 만들어지는 단백질이다.",
         "비말로 사람 사이에 쉽게 전파된다.",
         "진단은 임상 검체에서 보툴리눔 독소를 검출하는 것이다.",
         "현대 치료를 해도 치사율이 여전히 약 70%이다."], cols=1)

T = "파상풍 (C. tetani)"
Q(P, T, "교재 9장 92번",
  "운동신경의 세포 내로 들어가서 억제성 신경전달물질인 glycine, GABA의 방출을 억제하여 근육 수축과 경련을 일으키는 독소를 생산하는 병원균은?",
  "운동신경 세포 안으로 들어가 '<b>멈춰</b>' 신호를 보내는 물질(글리신, GABA)이 못 나오게 막아서 <b>근육이 계속 수축·경련</b>하게 만드는 독소. 이 독소를 만드는 균은?",
  "<i>Clostridium tetani</i> (파상풍균)",
  ["근육은 '수축해!'(흥분) 신호와 '그만!'(억제) 신호의 균형으로 움직여요.",
   "파상풍 독소(<b>tetanospasmin</b>)는 억제 신호(<b>글리신·GABA</b>)를 막음 → 브레이크 고장 → 근육이 계속 수축.",
   "그래서 증상이 <b>아관긴급(입이 안 벌어짐)</b>, 억지 웃음, 활처럼 휜 등(후궁반장), 경련.",
   "KEY|억제성 신경전달물질 차단 = 파상풍 / 아세틸콜린 방출 차단 = 보툴리눔"],
  fig="g4c.jpg", figw=30)

Q(P, T, "교재 9장 87번",
  "Exotoxin으로서 tetanolysin, tetanospasmin을 생성하는 균은?",
  "외독소(세균이 밖으로 내뿜는 독)로 <b>tetanolysin</b>과 <b>tetanospasmin</b>을 만드는 균은?",
  "파상풍균, <i>Clostridium tetani</i>",
  ["이름에 답이 있어요: <b>tetano-</b> = tetanus(파상풍).",
   "<b>tetanospasmin</b>(파상풍 강직 독소): spasm = 경련 → 신경독, 파상풍 증상의 주범 (강의 슬라이드에 나옴).",
   "<b>tetanolysin</b>: lysin = 녹이다 → 세포(적혈구)를 녹이는 용혈 독소, 역할은 작음.",
   "KEY|tetanospasmin → 중추신경계에 작용 → 근육 경련. 예방은 <b>DPT 백신</b>의 T."],
  fig="g4a.jpg", figw=30)

Q(P, T, "교재 9장 150번",
  "DPT 백신으로 예방할 수 있는 질환은?",
  "DPT 백신으로 예방할 수 있는 병 3가지는?",
  "디프테리아(D), 백일해(P), 파상풍(T)",
  ["<b>D</b> = Diphtheria 디프테리아 (<i>Corynebacterium diphtheriae</i>, 이번 강의 방선균 파트)",
   "<b>P</b> = Pertussis 백일해 (<i>Bordetella pertussis</i>, 그람음성균)",
   "<b>T</b> = Tetanus 파상풍 (<i>Clostridium tetani</i>, 이번 강의)",
   "D와 T는 <b>독소</b>가 병의 원인 → 독소를 무독화한 <b>톡소이드</b>로 백신을 만듦.",
   "강의에선 디프테리아 백신을 <b>DTaP</b>로도 표기 (aP = 무세포 백일해).",
   "TIP|'<b>D</b>ㅣ<b>P</b>ㅣ<b>T</b> = 디·백·파' → 디프테리아·백일해·파상풍"])

T = "C. difficile · C. perfringens"
Q(P, T, "교재 9장 88번",
  "장기간 사용하면 Clostridium difficile의 증식을 유도하여 위막성 대장염의 원인이 되는 항생제는?",
  "오래 쓰면 <i>C. difficile</i>이 늘어나서 <b>위막성 대장염</b>을 일으키는 항생제는?",
  "clindamycin, lincomycin, 2·3세대 cephalosporin, amoxicillin, ampicillin 등 (강의 예시: <b>clindamycin</b>)",
  ["항생제는 나쁜 균만 골라 죽이지 못하고 <b>장의 착한 정상균</b>도 같이 죽여요.",
   "<i>C. difficile</i>은 이 항생제들에 잘 버팀 → 경쟁자가 사라지자 폭증 → 독소 A·B로 대장에 염증.",
   "대장 벽에 노란 막(<b>위막</b>, 가짜 막)이 덮여 보여서 '위막성' 대장염.",
   "KEY|가장 유명한 범인 = <b>clindamycin</b> (린코사마이드 계열)"],
  fig=svgs.CDIFF, figw=44)

Q(P, T, "교재 9장 89번",
  "지속적인 clindamycin의 사용으로 장내 정상 세균총이 파괴되고 그 결과 대장염 증상이 나타났다면 그 원인균으로 의심되는 세균은?",
  "clindamycin을 계속 써서 장 속 정상균이 망가졌고, 그 결과 대장염이 생겼다. 원인균은?",
  "<i>Clostridioides(Clostridium) difficile</i>",
  ["앞 문제와 같은 원리 (항생제 → 정상균 소실 → <i>C. difficile</i> 폭증).",
   "이렇게 항생제 때문에 내성균이 대신 번성해 생기는 병을 <b>균교대 현상</b>(superinfection)이라고 해요.",
   "증상: <b>악취 나는 설사</b>, 발열, 복통 → 심하면 <b>중독성 거대결장</b>(생명 위협).",
   "병원에서 잘 퍼지는 <b>원내감염</b>균.",
   "TIP|difficile = '어려운' → 항생제 쓰고 난 뒤 생기는 <b>까다로운</b> 설사"],
  fig="g5a.jpg", figw=28)

Q(P, T, "추가 문제 (강의 슬라이드)",
  "Choose ALL correct statements about <i>C. difficile</i>.",
  "<i>C. difficile</i>에 대해 옳은 것을 <b>모두</b> 고르시오.",
  "①, ②, ④",
  ["O|①::사람·동물 대장의 <b>소수 정상균</b>일 수 있음 (평소엔 숫자가 적어 조용함).",
   "O|②::독소 A = 장독소(enterotoxin), 독소 B = 세포독소(cytotoxin). 강의 그대로.",
   "X|③::C. difficile은 <b>Clostridia</b>이므로 <b>절대 혐기성</b> + 포자형성. 산소 좋아하는 호기성 아님.",
   "O|④::심한 경우 <b>toxic megacolon</b>(중독성 거대결장) = 대장이 급격히 부풀어 오름.",
   "X|⑤::병원 안에서 잘 퍼지는 대표 <b>원내감염(nosocomial)</b>균.",
   "KEY|정상균 소수 → 항생제 → 폭증 → 독소 A(장)·B(세포) → 위막성 대장염 → 중독성 거대결장"],
  opts=["It can be a minor normal component of colonic flora.",
        "It produces toxin A (enterotoxin) and toxin B (cytotoxin).",
        "It is a strict aerobe that does not form spores.",
        "Severe cases may cause toxic megacolon.",
        "It is never associated with hospital-acquired infection."],
  topts=["대장 정상균총의 소수 구성원일 수 있다.", "독소 A(장독소)와 독소 B(세포독소)를 만든다.",
         "포자를 만들지 않는 절대 호기성균이다.", "심하면 중독성 거대결장을 일으킬 수 있다.",
         "병원 내 감염과는 전혀 관계없다."], cols=1)

Q(P, T, "추가 문제 (강의 슬라이드)",
  "Match each toxin of <i>C. perfringens</i> (formerly <i>C. welchii</i>) with the disease it mainly causes.",
  "<i>C. perfringens</i>(옛 이름 <i>C. welchii</i>)의 독소와, 그 독소가 주로 일으키는 병을 짝지으시오.",
  "(1)-B, (2)-C, (3)-A",
  ["<b>(1) 장독소 CPE → B. 식중독</b>: 가장 흔한 식중독 원인 중 하나. 복통·설사·구토, 대개 가볍게 지나감.",
   "<b>(2) β 독소 → C. 괴사성 장염(pigbel)</b>: 장이 썩는 병, 식중독보다 훨씬 심함 (치사율 50%).",
   "<b>(3) α 독소 → A. 가스괴저(근괴사)</b>: 근육 조직 속에 가스가 차고 괴사. 가장 치명적인 형태.",
   "TIP|<b>α</b>(알파, 처음) = 근육 '<b>가</b>스괴저' / <b>β</b> = '<b>배</b>(장)'가 썩는 pigbel / <b>CPE</b> = 흔한 식중독",
   "KEY|같은 균이라도 <b>어떤 독소냐</b>에 따라 '가벼운 식중독 ~ 치명적 괴저'까지."],
  extra_orig='<div class="boxq">(1) enterotoxin (CPE) &nbsp; (2) beta-toxin &nbsp; (3) alpha-toxin<br>A. gas gangrene (clostridial myonecrosis) &nbsp; B. food poisoning &nbsp; C. necrotizing enteritis (pigbel)</div>',
  extra_trans='<div class="boxq">(1) 장독소(CPE) &nbsp; (2) 베타 독소 &nbsp; (3) 알파 독소<br>A. 가스괴저(근괴사) &nbsp; B. 식중독 &nbsp; C. 괴사성 장염(피그벨)</div>',
  fig="g6.jpg", figw=26)

T = "Clostridium 종합"
Q(P, T, "교재 9장 90번",
  "Clostridium속의 균들이 일으키는 병과 그 원인 균을 짝지으시오.",
  "<i>Clostridium</i> 속 균이 일으키는 병과 원인균을 짝지으시오.",
  "(1)-②, (2)-③, (3)-①, (4)-④",
  ["<b>(1) 가스괴저 → ② C. perfringens</b> (α 독소, 근육이 썩고 가스 발생)",
   "<b>(2) 보툴리눔 식중독 → ③ C. botulinum</b> (이름 그대로)",
   "<b>(3) 파상풍 → ① C. tetani</b> (tetanus = 파상풍)",
   "<b>(4) 위막성 대장염 → ④ C. difficile</b> (항생제 후 설사)",
   "TIP|이름 = 병: botulinum→botulism, tetani→tetanus. 남은 둘은 '<b>디</b>피실=<b>대</b>장', '퍼프린젠스=가스'로."],
  extra_orig='<div class="boxq">(1) 가스괴저 &nbsp;(2) 보툴리눔 식중독 &nbsp;(3) 파상풍 &nbsp;(4) 위막성 대장염<br>① C. tetani &nbsp;② C. perfringens &nbsp;③ C. botulinum &nbsp;④ C. difficile</div>',
  extra_trans='<div class="boxq">(1) 근육이 썩으며 가스가 차는 병 &nbsp;(2) 보툴리눔 독소 식중독 &nbsp;(3) 파상풍 &nbsp;(4) 항생제 후 생기는 대장염<br>① 파상풍균 &nbsp;② 퍼프린젠스균 &nbsp;③ 보툴리눔균 &nbsp;④ 디피실균</div>')

Q(P, T, "교재 9장 39번",
  "다음의 'C'가 Clostridium인 것을 모두 고르시오.",
  "다음 학명에서 앞글자 'C.'가 <i>Clostridium</i>을 뜻하는 것을 <b>모두</b> 고르시오.",
  "①, ③",
  ["O|①::<i>C. difficile</i> = <b>Clostridioides</b>(옛 Clostridium) difficile → 위막성 대장염",
   "X|②::<i>C. diphtheriae</i> = <b>Corynebacterium</b> diphtheriae → 디프테리아 (방선균 파트)",
   "O|③::<i>C. botulinum</i> = <b>Clostridium</b> botulinum → 보툴리누스증",
   "X|④::<i>C. psittaci</i> = <b>Chlamydia(Chlamydophila)</b> psittaci → 앵무새병 (강의 범위 밖)",
   "X|⑤::<i>C. trachomatis</i> = <b>Chlamydia</b> trachomatis → 트라코마 (강의 범위 밖)",
   "KEY|병 이름으로 거꾸로 추적: diphtheriae→디프테리아→<b>Coryne</b>bacterium / psittaci·trachomatis→<b>Chlamydia</b>"],
  opts=["C. difficile", "C. diphtheriae", "C. botulinum", "C. psittaci", "C. trachomatis"],
  topts=["디피실 (대장염)", "디프테리아 (목)", "보툴리눔 (식중독)", "시타시 (앵무새병)", "트라코마티스 (눈·성병)"], cols=3)

# ------------------------------------------------------------------ Veillonella + Mycoplasma
SEC(G1, "1-2 Veillonella · Mycoplasma · Ureaplasma")
S(P, "1-2", "Veillonella (Negativicutes) · Mollicutes (Mycoplasma, Ureaplasma)",
  '<div class="row c3">' +
  card("Veillonella (예: V. parvula)",
       ul(["분류: 강 <b>Negativicutes</b>(옛날엔 Clostridia) > Veillonellaceae",
           "사람 포함 포유류 <b>입 안 점막의 정상균</b> (인수공통 X)",
           "다른 입속 균이 만든 <b>젖산(lactate)</b>만 먹음 (다른 당은 못 먹음)",
           "<b>젖산 → 아세트산 + 2 프로피온산 + CO₂ + H₂O</b>",
           "<b>충치, 치석(tartar·plaque), 치주염</b>의 원인",
           "드물게 골수염·심내막염"]), "soft") +
  card("Mollicutes 강 (Mycoplasmatota 문)",
       ul(["어원: mollis(부드러운) + cutis(피부) = <b>'말랑한 피부'</b> → 세포벽이 없다는 뜻",
           "<span class='hl'>세포벽 없음</span> → 모양 제각각(<b>다형성</b>) → <b>β-락탐(페니실린) 안 들음</b>",
           "대부분 <b>활주운동(gliding)</b>으로 이동 (일부는 비틀기)",
           "몸 크기·유전체 모두 <b>가장 작은 세균</b> → 동식물에 기생",
           "옛날엔 Firmicutes로 분류"]), "soft") +
  card("Mycoplasmatales 목의 두 속",
       table(["균", "병"], [
           ["<i>M. pneumoniae</i>", "<b>이형(비정형) 폐렴</b> = '걸어 다니는 폐렴'"],
           ["<i>M. genitalium</i>", "성병: <b>비임균성 요도염(NGU/NSU)</b>, 자궁경부염, 골반염"],
           ["<i>M. hominis</i>", "정상균 vs 성병(?): 세균성 질염, 골반염, 산후 자궁내막염, 신우신염"],
           ["<i>U. urealyticum</i>", "남녀 생식기 정상균(성인 70%) → NGU, 신우신염, 불임·사산·조산, 신생아 폐렴·수막염"],
       ])) +
  '</div>' +
  '<div class="row c2">' +
  card("이형(비정형) 폐렴 vs 전형 폐렴 (시험 단골)",
       table(["구분", "원인균"], [
           ["<b>이형 폐렴</b> (atypical, walking)", "<i>M. pneumoniae</i>, <i>Legionella pneumophila</i>, <i>Coxiella burnetii</i>, <i>Chlamydophila pneumoniae</i>"],
           ["<b>전형 폐렴</b> (typical)", "<i>S. pneumoniae</i>, <i>S. aureus</i>, <i>H. influenzae</i>, <i>K. pneumoniae</i>, <i>P. aeruginosa</i>"]])) +
  card("왜 '걸어 다니는 폐렴'?",
       ul(["증상이 비교적 가벼워서 환자가 누워 있지 않고 돌아다님",
           "흉부 X선 소견에 비해 증상이 약함",
           "<b>세포벽이 없으니</b> 페니실린·세팔로스포린은 무효 → 단백질 합성 억제제(마크롤라이드 등)를 씀"]), "warm") +
  '</div>')

T = "Veillonella · Mycoplasma"
Q(P, T, "추가 문제 (강의 슬라이드)",
  "Choose ALL correct statements about the genus <i>Veillonella</i> (e.g. <i>V. parvula</i>).",
  "<i>Veillonella</i> 속(예: <i>V. parvula</i>)에 대해 옳은 것을 <b>모두</b> 고르시오.",
  "①, ③, ④",
  ["O|①::사람 포함 포유류 <b>입 안 점막의 정상균</b>.",
   "X|②::다른 탄수화물은 못 먹고 <b>다른 입속 균이 만든 젖산만</b> 발효함.",
   "O|③::젖산 → 아세트산 + 2 프로피온산 + CO₂ + H₂O. (화학식 그대로 외우기!)",
   "O|④::충치, 치석, 치주염의 원인. 드물게 골수염·심내막염.",
   "X|⑤::현재 분류는 <b>Negativicutes</b> 강 (옛날 Clostridia). 정상균이지만 <b>인수공통감염 아님</b>.",
   "KEY|Veillonella = '<b>입속 젖산 먹보</b>' → 충치·치석·치주염"],
  opts=["It is normal flora of the oral mucosa of mammals, including humans.",
        "It ferments various carbohydrates such as glucose and sucrose.",
        "It converts lactate into acetate, propionate, CO<sub>2</sub> and H<sub>2</sub>O.",
        "It is a cause of dental caries, calculus and periodontitis.",
        "It belongs to the class <i>Clostridia</i> and is zoonotic."],
  topts=["사람을 포함한 포유류 입 안 점막의 정상균이다.", "포도당, 설탕 등 여러 탄수화물을 발효한다.",
         "젖산을 아세트산, 프로피온산, CO₂, H₂O로 바꾼다.", "충치, 치석, 치주염의 원인이다.",
         "Clostridia 강에 속하며 인수공통감염균이다."], cols=1)

Q(P, T, "교재 9장 94번",
  "숙주 없이 배양이 가능한 가장 작은 세균으로 세포막에 콜레스테롤을 가지는 세균은?",
  "숙주 세포 없이도(인공 배지에서) 키울 수 있는 <b>가장 작은 세균</b>이고, 세포막에 <b>콜레스테롤</b>이 있는 균은?",
  "<i>Mycoplasma</i> spp. (예: <i>M. pneumoniae</i>)",
  ["강의: Mollicutes = 몸 크기와 유전체 크기 모두 <b>가장 작은 세균</b>.",
   "세포벽이 없으니 세포막을 튼튼하게 해 줄 무언가가 필요 → 세포막에 <b>스테롤(콜레스테롤)</b>을 넣어 버팀.",
   "화학 연결: 콜레스테롤은 막의 유동성을 조절하는 지질 → 벽 대신 막을 단단하게 함.",
   "'숙주 없이 배양 가능' = 바이러스나 리케차·클라미디아처럼 세포 안에서만 사는 게 아니라는 뜻.",
   "KEY|가장 작다 + 벽 없다 + 콜레스테롤 = <b>Mycoplasma</b>"],
  fig=svgs.CELLWALL, figw=40)

Q(P, T, "교재 9장 95번",
  "Peptidoglycan을 합성하지 않기 때문에 세포벽 합성 저해 항생제인 penicillin에 저항성을 나타내는 것은?",
  "세포벽 성분인 <b>펩티도글리칸을 만들지 않아서</b>, 세포벽 합성을 막는 페니실린이 안 듣는 균은?",
  "<i>Mycoplasma</i>",
  ["페니실린 = 세포벽(펩티도글리칸) 만드는 효소를 방해하는 약 (β-락탐계).",
   "Mycoplasma는 <b>처음부터 세포벽이 없음</b> → 방해할 대상이 없으니 약이 소용없음.",
   "강의 표현: 'no cell wall / pleomorphism / <b>not affected by β-lactams</b>'.",
   "그래서 Mycoplasma 폐렴엔 리보솜(단백질 합성)을 막는 약을 씀.",
   "TIP|'공사 방해꾼(페니실린)은 <b>공사장이 없는 곳</b>에선 할 일이 없다'"])

Q(P, T, "추가 문제 (강의 슬라이드)",
  "Which of the following is NOT a cause of atypical (\"walking\") pneumonia?",
  "이형(비정형, '걸어 다니는') 폐렴의 원인균이 <b>아닌</b> 것은?",
  "④",
  ["O|①::<i>M. pneumoniae</i> = 이형 폐렴의 대표.",
   "O|②::<i>Legionella pneumophila</i> = 이형 폐렴 (냉방병).",
   "O|③::<i>Coxiella burnetii</i> = 이형 폐렴 (Q열).",
   "X|④::<i>Streptococcus pneumoniae</i>(폐렴구균)는 <b>전형(typical) 폐렴</b>의 대표 원인균.",
   "O|⑤::<i>Chlamydophila pneumoniae</i> = 이형 폐렴.",
   "KEY|이형 폐렴 4총사: <b>Mycoplasma · Legionella · Coxiella · Chlamydophila</b> (세포 안에 숨거나 벽이 없는 '특이한' 균들)",
   "TIP|'<b>마·레·코·클</b>'은 걸어 다녀요."],
  opts=["<i>Mycoplasma pneumoniae</i>", "<i>Legionella pneumophila</i>", "<i>Coxiella burnetii</i>",
        "<i>Streptococcus pneumoniae</i>", "<i>Chlamydophila pneumoniae</i>"],
  topts=["마이코플라스마 뉴모니애", "레지오넬라 뉴모필라", "콕시엘라 버네티", "폐렴구균(스트렙토코커스 뉴모니애)", "클라미도필라 뉴모니애"], cols=1)

Q(P, T, "추가 문제 (강의 슬라이드)",
  "Choose ALL correct statements about the order <i>Mycoplasmatales</i>.",
  "<i>Mycoplasmatales</i> 목에 대해 옳은 것을 <b>모두</b> 고르시오.",
  "①, ②, ④",
  ["O|①::대표 2속 = <i>Mycoplasma</i>와 <i>Ureaplasma</i>.",
   "O|②::<i>M. genitalium</i> → 성병, 비임균성 요도염(NGU/NSU), 자궁경부염, 골반염(PID).",
   "X|③::<i>U. urealyticum</i>은 성생활하는 성인의 <b>약 70%</b>에서 발견되는 생식기 <b>정상균</b> (그런데 병도 일으킴 → '정상균 vs 성병?').",
   "O|④::<i>Ureaplasma</i>는 불임·사산·조산, 신생아 폐렴·기관지폐이형성증·수막염과 관련.",
   "X|⑤::Mollicutes는 <b>세포벽이 없고</b> 대부분 <b>활주운동</b>으로 움직임 (편모 아님).",
   "TIP|<b>U</b>reaplasma = <b>U</b>rea(요소) 분해 + <b>U</b>rethritis(요도염)"],
  opts=["Two representative genera are <i>Mycoplasma</i> and <i>Ureaplasma</i>.",
        "<i>M. genitalium</i> causes non-gonococcal urethritis (NGU).",
        "<i>U. urealyticum</i> is never found in healthy people.",
        "<i>Ureaplasma</i> is associated with infertility, premature birth and neonatal pneumonia.",
        "Members have a thick cell wall and move by flagella."],
  topts=["대표 속은 Mycoplasma와 Ureaplasma이다.", "M. genitalium은 비임균성 요도염을 일으킨다.",
         "U. urealyticum은 건강한 사람에게서는 절대 발견되지 않는다.",
         "Ureaplasma는 불임, 조산, 신생아 폐렴과 관련 있다.", "두꺼운 세포벽이 있고 편모로 움직인다."], cols=1)

# ------------------------------------------------------------------ Actinomycetota
SEC(G1, "1-3 Actinomycetota (방선균·디프테리아·결핵·노카르디아 등)")
S(P, "1-3", "Actinomycetota 문: 흙 속 항생제 공장 + 무서운 병원균",
  '<div class="row c2">' +
  card("공통 특징",
       ul(["흙과 물에 가장 흔한 생명체 중 하나 → <b>유기물 분해</b>(퇴비, 탄소 순환)",
           "<span class='hl'>2차 대사산물(항생제)</span> 생산 → 약학적으로 매우 중요",
           "일부는 곰팡이처럼 <b>가지 친 실(균사, mycelia)</b>을 만듦 (예: Actinomyces)",
           "<b>무성포자</b>는 만들지만 <b>내생포자는 X</b>",
           "옛날엔 <b>곰팡이로 분류</b> → 지금은 세균 (세포벽 성분, 16S rRNA가 세균형)",
           "높은 G+C 그람양성균"]), "soft") +
  card("분류 계통 (목 > 과 > 속)",
       table(["목", "과", "속"], [
           ["Actinomycetales", "Actinomycetaceae", "<i>Actinomyces</i>"],
           ["Mycobacteriales", "Corynebacteriaceae", "<i>Corynebacterium</i>"],
           ["Mycobacteriales", "Mycobacteriaceae", "<i>Mycobacterium</i>"],
           ["Mycobacteriales", "Nocardiaceae", "<i>Nocardia</i>"],
           ["Propionibacteriales", "Propionibacteriaceae", "<i>Propionibacterium</i>"],
           ["Micromonosporales", "Micromonosporaceae", "<i>Micromonospora</i>"],
           ["Streptomycetales", "Streptomycetaceae", "<i>Streptomyces</i>"],
           ["Bifidobacteriales", "Bifidobacteriaceae", "<i>Bifidobacterium</i>"]])) +
  '</div>' +
  '<div class="row c4">' +
  img("g14b.jpg", "방선균증(A. israelii): 입·턱 농양", 100) +
  img("g15b.jpg", "Corynebacterium: 곤봉(club) 모양", 100) +
  img("g16a.jpg", "Mycobacterium (결핵균)", 100) +
  card("기억법", ul(["<b>병 주는 4속</b>: Actinomyces, Coryne, Myco, Nocardia", "<b>돈 버는 4속</b>: Propioni(치즈·방부제), Micromono·Strepto(항생제), Bifido(유산균)"]), "warm") +
  '</div>')

S(P, "1-3", "방선균 8속 한 장 정리",
  table(["속", "어디 사나?", "좋은 일 / 나쁜 일", "꼭 외울 것"], [
      ["<i>Actinomyces</i>", "흙, <b>잇몸</b>(공생 정상균)", "퇴비 분해 효소 / <b>기회감염</b>", "<b>방선균증</b> (<i>A. israelii</i>): 입·폐·위장관 <b>농양</b>"],
      ["<i>Corynebacterium</i>", "-", "<i>C. glutamicum</i>: <b>글루탐산·라이신</b> 생산(식품·사료·의약) / <i>C. diphtheriae</i>: 디프테리아", "디프테리아 독소(<b>외독소</b>), 상기도, 직접 접촉(비말?), 심근염 20%·말초신경병 10%, <b>DTaP</b> 백신"],
      ["<i>Mycobacterium</i>", "-", "포유류에 심각한 병", "<i>M. tuberculosis</i> 결핵 / <i>M. bovis</i> <b>우결핵(인수공통)</b> / <i>M. leprae</i> <b>한센병</b>(나병)"],
      ["<i>Nocardia</i>", "흙, 건강한 잇몸·치주낭(입 정상균)", "<b>기회감염</b>", "<b>노카르디아증</b>(<i>N. asteroides</i>): 천천히 진행하는 폐렴, 전신 감염"],
      ["<i>Propionibacterium</i><br>(일부 → <i>Cutibacterium</i>)", "피부(<b>땀샘·피지샘</b>) 공생균", "<b>프로피온산</b> 생산 → 치즈, 프로바이오틱스, <b>방부제</b>(곰팡이 억제), 과일향 용매·향료", "<i>P. acnes</i>(<i>C. acnes</i>) → <b>여드름</b>"],
      ["<i>Micromonospora</i>", "흙", "항생제", "<b>겐타마이신</b>, 시소마이신 (아미노글리코사이드) — '-<b>micin</b>'"],
      ["<i>Streptomyces</i>", "흙", "항생제 (항생제 생산균이 <b>가장 많은 속</b>)", "<b>스트렙토마이신</b>, 카나마이신, 네오마이신 (아미노글리코사이드) — '-<b>mycin</b>'"],
      ["<i>Bifidobacterium</i>", "장(<b>대장 주요 균</b>)·질·입", "장내 균형, 유해균 억제, 알레르기↓, 항암 → 유익균", "<i>B. bifidum</i> (1960년대 전엔 '<i>Lactobacillus bifidus</i>')"],
  ]) +
  '<div class="row c2">' +
  card("디프테리아 증상 단계", ul(["가벼움: <b>피부</b>에만 국한", "심함: 인후통, 발열, 편도염, 인두염 + <b>위막</b>(목에 회색 막) → 기도 막힘",
                             "합병증: <b>심근염(~20%)</b>, <b>말초신경병(~10%)</b>"]), "soft") +
  card("마이신 철자 팁", ul(["Micromonospora → genta<b>micin</b> (i)", "Streptomyces → strepto<b>mycin</b> (y)", "둘 다 <b>아미노글리코사이드</b> 계열 항생제"]), "warm") +
  '</div>')

T = "방선균 공통 · Actinomyces"
Q(P, T, "추가 문제 (강의 슬라이드)",
  "Which statement about the phylum <i>Actinomycetota</i> is NOT correct?",
  "<i>Actinomycetota</i> 문에 대한 설명으로 옳지 <b>않은</b> 것은?",
  "④",
  ["O|①::흙·물에 가장 흔한 생명체 중 하나 → 유기물 분해, 탄소 순환에 필수.",
   "O|②::항생제 같은 <b>2차 대사산물</b> 생산 → 약학·산업적으로 중요.",
   "O|③::일부(예: Actinomyces)는 곰팡이 같은 <b>균사 그물</b>을 만듦.",
   "X|④::<b>무성포자</b>는 만들지만 <b>내생포자(endospore)는 만들지 않음</b>. 내생포자는 Clostridium(Bacillota)의 특징!",
   "O|⑤::옛날엔 곰팡이였지만, 세포벽 구조와 <b>16S rRNA</b>가 세균형이라 지금은 세균.",
   "KEY|내생포자 = Clostridium / 무성포자 + 균사 = 방선균"],
  opts=["They are among the most common life forms in soil and water.",
        "They produce secondary metabolites such as antibiotics.",
        "Some members form fungal-like branched networks of hyphae.",
        "They produce endospores like <i>Clostridium</i>.",
        "They are now classified as bacteria based on cell wall structure and 16S rRNA."],
  topts=["흙과 물에서 가장 흔한 생명체 중 하나이다.", "항생제 같은 2차 대사산물을 만든다.",
         "일부는 곰팡이 같은 가지 친 균사 그물을 만든다.", "Clostridium처럼 내생포자를 만든다.",
         "세포벽 구조와 16S rRNA를 근거로 현재 세균으로 분류된다."], cols=1)

Q(P, T, "교재 9장 103번",
  "배양 속도가 느리고, 백색의 어금니 모양의 집락을 형성하는 병원균은?",
  "천천히 자라고, 배지에서 <b>하얀 어금니 모양</b>의 덩어리(집락)를 만드는 병원균은?",
  "방선균, <i>Actinomyces israelii</i>",
  ["<i>Actinomyces</i>는 균사(실)를 뻗으며 자라서 집락이 울퉁불퉁 → '<b>어금니(molar tooth)</b>' 모양.",
   "강의: 평소 <b>잇몸</b>에 사는 공생균 → 면역이 떨어지면 <b>기회감염</b>.",
   "<b>방선균증(actinomycosis)</b>: 입, 폐, 위장관 등에 <b>농양(고름 주머니)</b> 형성. 대표 균 <i>A. israelii</i>.",
   "TIP|입(잇몸)에 사는 균 → 집락도 <b>이빨(어금니)</b> 모양!"],
  fig="g14b.jpg", figw=30)

T = "디프테리아 (Corynebacterium)"
Q(P, T, "교재 9장 15번",
  "다음 중 Corynebacterium diphtheriae와 관계없는 것을 모두 고르시오.",
  "디프테리아균(<i>Corynebacterium diphtheriae</i>)과 <b>관계없는</b> 것을 모두 고르시오.",
  "②, ⑥, ⑩, ⑪",
  ["O|①::DPT의 <b>D</b> = 디프테리아.",
   "X|②::병의 주범은 <b>외독소</b>(exotoxin, 디프테리아 독소). 내독소(LPS)는 그람음성균의 것.",
   "O|③::Schick test = 디프테리아 항체(면역) 유무 검사.",
   "O|④::Albert 염색 → <b>이염성 과립</b>(볼루틴) 관찰.",
   "O|⑤::목(인후)에 회색 <b>위막</b> 형성.",
   "X|⑥::발적독(erythrogenic toxin)은 <b>성홍열</b>균(<i>S. pyogenes</i>)의 독소.",
   "O|⑦::Neisser 염색 → 볼루틴(이염성 과립).",
   "O|⑧::독소가 원인이므로 <b>항독소 혈청</b>으로 중화 치료.",
   "O|⑨::그람양성 간균 (곤봉 모양).",
   "X|⑩::Ziehl-Neelsen은 <b>항산성 염색</b>(결핵균용). Neisser 소체는 Neisser 염색.",
   "X|⑪::편모 없음 (운동성 X).",
   "KEY|디프테리아 = 그람양성 곤봉균 · <b>외독소</b> · 위막 · 이염성 과립 · DPT · 항독소"],
  opts=["DPT 백신으로 예방한다.", "Endotoxin이 발병 주요 원인이다.", "Schick test로 항체 검사를 한다.",
        "Albert 염색 시 이염성 과립을 관찰할 수 있다.", "인후부에 pseudomembrane을 형성한다.",
        "Erythrogenic toxin을 생산한다.", "Neisser 염색 - volutin", "항독소혈청으로 치료할 수 있다.",
        "병원균은 그람양성 간균이다.", "Ziehl-Neelsen 염색 - Neisser 소체", "Flagella를 갖고 있다."],
  topts=["DPT 백신으로 예방한다.", "내독소가 병의 주요 원인이다.", "Schick 검사로 항체를 검사한다.",
         "Albert 염색에서 색이 다른 알갱이가 보인다.", "목에 가짜 막(위막)을 만든다.",
         "발적독(성홍열 독소)을 만든다.", "Neisser 염색 → 볼루틴 알갱이", "독을 중화하는 혈청으로 치료한다.",
         "그람양성 막대균이다.", "결핵균 염색법 → Neisser 소체", "편모가 있다."], cols=2)

Q(P, T, "교재 9장 96번",
  "인후점막에 침입하여 위막(pseudomembrane)을 형성하는 균은?",
  "목(인후) 점막에 들어가서 <b>위막(가짜 막)</b>을 만드는 균은?",
  "<i>Corynebacterium diphtheriae</i> (디프테리아균)",
  ["디프테리아 독소가 목 점막 세포를 죽임 → 죽은 세포 + 섬유소 + 백혈구가 엉겨 <b>회색 막</b>이 생김 = <b>위막</b>.",
   "이 막이 기도를 막으면 질식 위험 → 그래서 무서운 병.",
   "강의: 상기도 질환, 전염성, <b>직접 접촉(비말?)</b>으로 전파, 심하면 <b>심근염·말초신경병</b>.",
   "⚠ 헷갈림 주의: <b>위막성 대장염</b>은 <i>C. difficile</i>(대장), <b>인후 위막</b>은 <i>C. diphtheriae</i>(목). 둘 다 'C. di~'!",
   "TIP|<b>목</b>의 위막 = 디프<b>테리아</b> / <b>장</b>의 위막 = 디<b>피실</b>"],
  fig="g15b.jpg", figw=26)

Q(P, T, "추가 문제 (강의 슬라이드)",
  "Choose ALL correct statements about the genus <i>Corynebacterium</i>.",
  "<i>Corynebacterium</i> 속에 대해 옳은 것을 <b>모두</b> 고르시오.",
  "①, ③, ④",
  ["O|①::<i>C. glutamicum</i>은 병을 안 일으키는 착한 균 → <b>글루탐산(MSG 원료)·라이신</b> 산업 생산.",
   "X|②::디프테리아의 원인은 <b>외독소</b>(diphtheria toxin, an exotoxin).",
   "O|③::심한 경우 <b>심근염(~20%)</b>, <b>말초신경병(~10%)</b>.",
   "O|④::강의에 'vaccine: <b>DTaP</b>'로 나옴.",
   "X|⑤::Corynebacterium은 <b>곤봉(club) 모양</b>의 간균(막대균). 나선균 아님.",
   "KEY|같은 속 안에 '산업용 착한 균(glutamicum)'과 '병원균(diphtheriae)'이 함께 있음"],
  opts=["Non-pathogenic <i>C. glutamicum</i> is used to produce glutamate and lysine.",
        "Diphtheria is caused by an endotoxin (LPS).",
        "Severe diphtheria can cause myocarditis and peripheral neuropathy.",
        "Diphtheria can be prevented by the DTaP vaccine.",
        "<i>Corynebacterium</i> is a spiral-shaped bacterium."],
  topts=["비병원성 C. glutamicum은 글루탐산과 라이신 생산에 쓰인다.", "디프테리아는 내독소(LPS) 때문에 생긴다.",
         "심한 디프테리아는 심근염과 말초신경병을 일으킬 수 있다.", "DTaP 백신으로 예방할 수 있다.",
         "Corynebacterium은 나선 모양 세균이다."], cols=1)

T = "결핵 · 한센병 (Mycobacterium)"
Q(P, T, "교재 9장 5번",
  "결핵균에 대한 설명으로 옳은 것에 T, 틀린 것에 F를 표시하시오.",
  "결핵균(<i>Mycobacterium tuberculosis</i>)에 대한 설명이 맞으면 T, 틀리면 F.",
  "(1) T (2) T (3) F (4) T (5) T (6) F (7) F (8) F",
  ["O|(1)::세포벽에 왁스 같은 지질(<b>미콜산</b>)이 많아, 산-알코올로 씻어도 염료가 안 빠짐 = <b>항산성균</b>.",
   "O|(2)::산소가 필요한 <b>호기성</b> + 분류상 그람양성(Actinomycetota).",
   "X|(3)::결핵은 수개월~수년 가는 <b>만성</b> 감염병.",
   "O|(4)::기침·비말을 통해 주로 <b>호흡기</b>로 감염.",
   "O|(5)::강의: <i>M. bovis</i> = 우결핵, <b>인수공통(zoonotic)</b> → 사람도 감염 (예: 살균 안 한 우유).",
   "X|(6)::결핵 백신은 <b>BCG</b>. DPT는 디프테리아·백일해·파상풍.",
   "X|(7)::결핵균은 <b>엄청 느리게</b> 자람 (집락까지 수 주). 16시간 만에 자라는 건 대장균 같은 빠른 균.",
   "X|(8)::잠복기가 길고 천천히 발병 (만성).",
   "KEY|결핵균 = <b>항산성 · 호기성 · 느림 · 만성 · BCG</b> / <i>M. bovis</i>는 인수공통"],
  opts=["항산성(acid-fast)균이다.", "호기성 그람양성이다.", "급성 감염병이다.", "주로 호흡기로 감염된다.",
        "우형 결핵균도 인체에 감염된다.", "DPT 예방접종을 실시한다.", "37℃에서 16시간 정도 배양하면 집락을 형성한다.",
        "감염되면 24시간 이내에 발병한다."], mk="paren",
  topts=["산(알코올)으로 씻어도 염료가 안 빠지는 균이다.", "산소가 필요한 그람양성균이다.", "갑자기 생겼다 빨리 끝나는 병이다.",
         "주로 숨 쉬는 길(호흡기)로 감염된다.", "소의 결핵균도 사람에게 감염된다.", "DPT 백신을 맞는다.",
         "37℃에서 16시간 키우면 집락이 생긴다.", "감염되면 하루 안에 발병한다."], cols=2, fig="g16a.jpg", figw=22)

Q(P, T, "교재 9장 99번",
  "결핵의 원인균의 과(family)명과 속명 및 종명은?",
  "결핵 원인균의 <b>과 이름, 속 이름, 종 이름</b>을 쓰시오.",
  "과: Mycobacteriaceae / 속: <i>Mycobacterium</i> / 종: <i>M. tuberculosis</i>",
  ["강의 분류: Actinomycetota 문 > Actinomycetia 강 > <b>Mycobacteriales</b> 목 > <b>Mycobacteriaceae</b> 과 > <i>Mycobacterium</i> 속.",
   "과(family) 이름은 항상 <b>-aceae</b>로 끝나고, 이탤릭 안 씀.",
   "속명·종명은 <i>이탤릭</i>, 속명 첫 글자만 대문자: <i>Mycobacterium tuberculosis</i>.",
   "같은 속 친구들: <i>M. bovis</i>(우결핵, 인수공통), <i>M. leprae</i>(한센병).",
   "TIP|myco = 곰팡이(균사처럼 보여서), tubercul = 결절(덩어리) → '덩어리 만드는 곰팡이 같은 균'"])

Q(P, T, "교재 9장 16번",
  "다음 중 한센병과 관계없는 것을 모두 고르시오.",
  "한센병(나병)과 <b>관계없는</b> 것을 모두 고르시오.",
  "④, ⑥",
  ["O|①::promin = 초기 한센병 치료제(설폰계).",
   "O|②::대풍자유(chaulmoogra oil) = 옛날 한센병 민간 치료약.",
   "O|③::DDS(dapsone) = 대표적인 한센병 치료제.",
   "X|④::novobiocin은 한센병과 무관한 다른 항생제.",
   "O|⑤::원인균 = <i>Mycobacterium leprae</i> (강의: 한센병, 인수공통?).",
   "X|⑥::<i>M. leprae</i>는 <b>인공 배지에서 배양이 안 됨</b> (아르마딜로 발바닥 등에서만 증식) → '용이'는 틀림.",
   "O|⑦::rifampicin + dapsone 병합요법으로 치료.",
   "KEY|한센병 = <i>M. leprae</i> · <b>배양 불가</b> · dapsone(DDS)·rifampicin"],
  opts=["promin", "대풍자유(⼤楓⼦油)", "diaminodiphenyl sulfone(DDS)", "novobiocin", "Mycobacterium leprae",
        "실험실 배양이 용이", "rifampicin, dapsone 등으로 치료"],
  topts=["프로민 (옛 치료제)", "대풍자 기름 (옛 민간약)", "다이아미노다이페닐 설폰 = 댑손", "노보바이오신 (다른 항생제)",
         "나병균", "실험실에서 쉽게 키울 수 있음", "리팜피신, 댑손으로 치료"], cols=2)

T = "Nocardia · Propionibacterium · 항생제 생산균"
Q(P, T, "추가 문제 (강의 슬라이드)",
  "Match each genus of <i>Actinomycetota</i> with its correct description.",
  "방선균류의 속과 알맞은 설명을 짝지으시오.",
  "(1)-C, (2)-E, (3)-A, (4)-B, (5)-D",
  ["<b>(1) Nocardia → C</b>: 흙과 잇몸에 사는 정상균, <b>기회감염</b> 노카르디아증(<i>N. asteroides</i>) = 천천히 진행하는 폐렴.",
   "<b>(2) Propionibacterium → E</b>: <b>프로피온산</b> 생산 (치즈·방부제·향료), <i>P. acnes</i> → <b>여드름</b>.",
   "<b>(3) Micromonospora → A</b>: <b>겐타마이신</b>·시소마이신 (아미노글리코사이드).",
   "<b>(4) Streptomyces → B</b>: <b>스트렙토마이신</b>·카나마이신·네오마이신.",
   "<b>(5) Bifidobacterium → D</b>: 대장의 주요 유익균, 프로바이오틱스 (옛 이름 Lactobacillus bifidus).",
   "TIP|프로피온산(propionic acid) = <b>Propioni</b>bacterium, 이름에 산물이 들어 있음!"],
  extra_orig='<div class="boxq">(1) <i>Nocardia</i> (2) <i>Propionibacterium</i> (3) <i>Micromonospora</i> (4) <i>Streptomyces</i> (5) <i>Bifidobacterium</i><br>'
             'A. produces gentamicin and sisomicin<br>B. produces streptomycin, kanamycin and neomycin<br>C. opportunistic slowly progressive pneumonia<br>'
             'D. major genus of colon flora; probiotic benefits<br>E. generates propionic acid; causes acne</div>',
  extra_trans='<div class="boxq">(1) 노카르디아 (2) 프로피오니박테리움 (3) 마이크로모노스포라 (4) 스트렙토마이세스 (5) 비피도박테리움<br>'
              'A. 겐타마이신·시소마이신 생산<br>B. 스트렙토마이신·카나마이신·네오마이신 생산<br>C. 기회감염으로 천천히 진행하는 폐렴<br>'
              'D. 대장의 주요 균, 몸에 유익<br>E. 프로피온산 생산, 여드름 원인</div>')

Q(P, T, "교재 9장 148번",
  "항생물질 생산 균주가 가장 많이 소속된 속은? (보기: ㄱ. Mycobacterium ㄴ. Citrobacter ㄷ. Plasmodium ㄹ. Leptospira ㅁ. Shigella ㅂ. Trichomonas ㅅ. Streptomyces ㅇ. Salmonella ㅈ. Treponema ㅊ. Proteus)",
  "항생제를 만드는 균이 <b>가장 많이 속한 속</b>은? (보기 중 고르기)",
  "ㅅ. <i>Streptomyces</i>",
  ["<i>Streptomyces</i>는 흙 속에 사는 방선균 → 경쟁 균을 죽이려고 항생제를 만들어 냄.",
   "강의: 아미노글리코사이드 <b>스트렙토마이신, 카나마이신, 네오마이신</b> 생산.",
   "실제로 사람이 쓰는 천연 항생제의 약 2/3가 Streptomyces 출신.",
   "나머지 보기: 결핵균(ㄱ), 장내세균(ㄴ·ㅁ·ㅇ·ㅊ), 말라리아 원충(ㄷ), 스피로헤타(ㄹ·ㅈ), 트리코모나스 원충(ㅂ) → 항생제 생산과 무관.",
   "KEY|항생제 공장 1위 = <b>Streptomyces</b>, 겐타마이신은 <b>Micromonospora</b>"])

T = "그람양성균 종합"
Q(P, T, "교재 9장 152번",
  "다음 세균이 속하는 문(phylum)은 무엇인가? (1) M. tuberculosis (2) C. diphtheriae (3) B. anthracis (4) M. leprae (5) P. acnes (6) E. coli (7) P. aeruginosa (8) S. aureus",
  "다음 세균이 속한 <b>문(phylum)</b>을 쓰시오. (1) 결핵균 (2) 디프테리아균 (3) 탄저균 (4) 나병균 (5) 여드름균 (6) 대장균 (7) 녹농균 (8) 황색포도상구균",
  "(1)(2)(4)(5) Actinobacteria(=Actinomycetota, 고 G+C) · (3)(8) Firmicutes(=Bacillota, 저 G+C) · (6)(7) Proteobacteria",
  ["<b>Actinomycetota</b>(옛 Actinobacteria, 높은 G+C 그람양성): 결핵균·나병균(<i>Mycobacterium</i>), 디프테리아균(<i>Corynebacterium</i>), 여드름균(<i>Propionibacterium</i>) → 이번 강의 방선균 파트 그대로!",
   "<b>Bacillota</b>(옛 Firmicutes, 낮은 G+C 그람양성): 탄저균(<i>Bacillus</i>), 포도상구균(<i>Staphylococcus</i>) + 강의의 Clostridium도 여기.",
   "<b>Proteobacteria</b>: 대장균, 녹농균 같은 <b>그람음성균</b> (강의 범위 밖이지만 '그람음성 = 프로테오'만 기억).",
   "KEY|M·C·P(Myco·Coryne·Propioni) = Actino / B·S·Clostridium = Bacillota",
   "TIP|교재는 옛 이름(Firmicutes, Actinobacteria)으로 답함 → 둘 다 알아두기"], fig=svgs.GP_TREE, figw=40)
