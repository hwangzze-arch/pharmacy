# -*- coding: utf-8 -*-
from core import RAW, S, SEC, Q, card, ul, table, img
import svgs

P = "vr"
G2 = "PART 2 · 바이러스"

RAW('''<section class="page divider vr"><div class="num">PART 2</div><h1>바이러스 (Viruses)</h1>
<p>기본 개념 → 볼티모어 7그룹(I dsDNA ~ VII dsDNA-RT) 순서로 정리<br>각 그룹 요약 뒤에 교재 10장 문제를 배치했습니다.</p></section>''')

SEC(G2, "2-0 바이러스 기본 (정의·구조·프리온·생활사·분류)")
S(P, "2-0", "바이러스란? 크기 · 역사 · 기원",
  '<div class="row c2">' +
  card("정의와 크기",
       ul(["다른 생물을 감염시키는 <b>작은 입자</b> = '<b>여과성</b>' 감염원 (세균 거르는 필터 통과)",
           "크기 <b>20~400 nm</b> (미미바이러스 최대 900 nm) → 광학현미경 X, <b>전자현미경</b> O",
           "감염 대상: 동물·식물·<b>세균(박테리오파지)·고세균</b>까지 모든 생물",
           "수백만 종, 자세히 밝혀진 건 약 5,000종 → <b>지구에서 가장 많은 생물학적 존재</b>"]), "soft") +
  img("v2.jpg", "파보·폴리오(20~30 nm) / 천연두(350~400 nm) / 미미바이러스(400~900 nm)", 100) +
  '</div>' +
  '<div class="row c2">' +
  card("역사 (인물 ↔ 업적 짝짓기)",
       table(["인물", "업적"], [
           ["Edward Jenner", "<b>종두법</b>: 우두(vaccinia)로 천연두 예방"],
           ["Louis Pasteur", "약하게 만든 병원체로 <b>광견병 백신</b>"],
           ["Charles Chamberland", "세균보다 작은 구멍의 <b>필터</b>"],
           ["Adolf Mayer", "<b>담배 모자이크병</b> 명명, 즙의 감염성 증명"],
           ["Ivanovsky", "TMD 원인 = 필터 통과 (세균 독소라 생각)"],
           ["Beijerinck", "'녹아 있는 살아있는 병원체' (액체라고 함 → 틀림)"],
           ["Wendell Stanley", "TMV를 <b>핵단백질 결정</b>으로 분리 → 입자임을 증명"],
           ["Friedrich Loeffler", "첫 <b>동물</b> 바이러스: <b>구제역</b>"]])) +
  card("바이러스는 어디서 왔을까? (3가지 가설)",
       table(["가설", "내용", "약점"], [
           ["① 진행(탈출) 가설", "플라스미드·점프 유전자 같은 유전물질이 세포 밖으로 나가는 능력 획득", "바이러스 단백질 존재 설명 X"],
           ["② 퇴행(축소) 가설", "세포 안 기생 세균(리케차·클라미디아)이 유전자를 잃어 바이러스가 됨", "가장 작은 기생 세균도 바이러스와 안 닮음"],
           ["③ 바이러스 먼저 가설", "세포보다 먼저 존재, 세포와 함께 진화", "복제엔 숙주가 꼭 필요하다는 사실과 모순"]]) +
       '<p style="margin-top:1.4mm"><b>생물 특성</b>: 유전자·진화·번식·자기조립 / <b>무생물 특성</b>: 숙주 필요(세포내 기생), 대사 X, 세포 구조 X(리보솜·미토콘드리아 없음)</p>', "") +
  '</div>')

S(P, "2-0", "바이러스 구조 용어 · 외피 · 비로이드 · 프로바이러스 · 프리온",
  '<div class="row c2">' +
  f'<div class="card2">{svgs.VSTRUCT}</div>' +
  card("구조 용어 (작은 것 → 큰 것)",
       '<p class="big" style="text-align:center">protomer &lt; capsomer &lt; capsid</p>' +
       ul(["<b>protomer</b>: 캡소미어의 하위 단위 (5~6개가 모여 캡소미어)",
           "<b>capsomer</b>: 캡시드의 기본 단위 '벽돌', 스스로 조립(self-assembly)",
           "<b>capsid</b>: 핵산을 감싸는 <b>단백질 껍질</b>",
           "캡시드 모양: <b>나선형</b>(원통, 담배모자이크바이러스) / <b>정이십면체</b>(정삼각형 20면, 거의 구형) / <b>복합형</b>(박테리오파지, 폭스)"]) +
       '<h4 style="margin-top:1.6mm">외피 바이러스(lipovirus)의 성질</h4>' +
       ul(["외피 = 숙주 세포막 조각(인지질) + 바이러스 당단백질 → 세포 진입을 도움",
           "<b>건조·열·세제·지용성 용매(에테르, 클로로포름, 담즙산염)</b>에 약함 → 소독 쉬움",
           "밖에서 오래 못 삶 → 숙주→숙주로 <b>직접</b> 전파해야 함",
           "적응력 크고 빨리 변함 → 지속 감염 가능"]), "soft") +
  '</div>' +
  '<div class="row c3">' +
  card("비로이드 (viroid)",
       ul(["1971 Diener 발견", "<b>단백질 껍질 없는</b> 작은 원형 <b>RNA</b>(240~600 nt)만!", "<b>식물</b> 병 (감자 방추괴경병, 코코넛 카당카당)", "RNA 침묵으로 유전자 발현 방해"])) +
  card("프로바이러스 (provirus)",
       ul(["숙주 DNA에 <b>끼어 들어간</b> 바이러스 유전체", "예: <b>레트로바이러스</b>", "(+)ssRNA → (−)DNA → (±)DNA → (+)mRNA → 단백질"])) +
  card("프리온 (prion)",
       ul(["1982 Prusiner, <b>단백질만</b>으로 된 감염원(PrP), 핵산 X",
           "정상 PrP<sup>C</sup> → 잘못 접힌 PrP<sup>Sc</sup>(β-시트, 아밀로이드) → 열·단백분해효소에 <b>극도로 안정</b>",
           "뇌에 <b>구멍(공포)</b> → 해면(스펀지) 모양 = <b>전염성 해면상 뇌병증</b>: 광우병, <b>CJD</b>",
           "치매·성격변화·근육강직 → 6개월 내 사망, <b>백신·치료 없음</b>, 잠복기 김"]), "red") +
  '</div>')

S(P, "2-0", "생활사 5단계와 볼티모어 7그룹 분류",
  f'<div class="card2 short">{svgs.LIFECYCLE}</div>' +
  '<div class="row c23">' +
  card("분류 방법 2가지",
       ul(["<b>ICTV</b>: 목(-virales) > 과(-viridae) > 아과(-virinae) > 속(-virus) > 종",
           "기준: 핵산 종류(RNA/DNA), 외피 유무, 캡시드 구조 등",
           "<b>볼티모어</b>(7그룹): <b>유전체가 어떻게 mRNA를 만드나</b>로 분류",
           "<span class='hl'>모든 바이러스는 결국 (+) mRNA를 만들어야</span> 단백질을 만들 수 있다!",
           "(+) 가닥 = mRNA와 같은 방향 → 바로 번역 가능 → <b>그 자체로 감염성</b>",
           "(−) 가닥 = 거꾸로 → 자기 <b>RNA 중합효소</b>를 들고 다녀야 함"]), "soft") +
  f'<div class="card2">{svgs.BALTIMORE}</div>' +
  '</div>')

S(P, "2-0", "볼티모어 그룹별 대표 과(family) 한 장 정리",
  table(["그룹", "유전체", "대표 과", "외피", "꼭 외울 사람 바이러스"], [
      ["I", "dsDNA", "Poxviridae · Herpesviridae · Adenoviridae · Papillomaviridae · Polyomaviridae", "폭스·헤르페스 O / 아데노·파포바 X", "천연두, HSV, VZV, CMV, EBV, KSHV, 아데노, HPV"],
      ["II", "ssDNA", "Parvoviridae", "X", "파보 B19 (전염성 홍반 = 제5병)"],
      ["III", "dsRNA", "Reoviridae", "X", "<b>로타바이러스</b> (분절 10~12개)"],
      ["IV", "(+)ssRNA", "Coronaviridae · Picornaviridae · Caliciviridae · Flaviviridae · Togaviridae · Hepeviridae", "코로나·플라비·토가 O / 피코르나·칼리시·헤페 X", "SARS·MERS, 폴리오·콕사키·리노·HAV, 노로, 황열·뎅기·일본뇌염·지카·HCV, 풍진, HEV"],
      ["V", "(−)ssRNA", "Paramyxoviridae · Rhabdoviridae · Bunyaviridae · Orthomyxoviridae", "모두 O", "홍역·볼거리·RSV, 광견병, 한타, 인플루엔자"],
      ["VI", "ssRNA-RT", "Retroviridae", "O", "HIV, HTLV, (Rous 육종 바이러스)"],
      ["VII", "dsDNA-RT", "Hepadnaviridae", "O", "<b>B형 간염(HBV)</b>"],
  ]) +
  '<div class="row c3">' +
  card("DNA 바이러스 외우기", '<p><b>"헤·아·폭·파·파·헤파"</b><br>헤르페스·아데노·폭스·파포바(유두종·폴리오마)·파보·헤파드나(HBV)</p><p>→ 이것 말고는 거의 다 <b>RNA</b>!</p>', "soft") +
  card("외피 없는(naked) 바이러스", '<p><b>"피코·칼리시·레오·아데노·파포바·파보·헤페"</b><br>→ 위장관(산·담즙)에서도 살아남는 것이 많음 → <b>분변-경구 전파</b></p>', "warm") +
  card("분절(segmented) 유전체", ul(["로타(레오) 10~12조각", "인플루엔자 8조각 (C형 7)", "번야(한타) 3조각 (L·M·S)", "→ 조각이 섞이면 신종 출현(대변이)"]), "") +
  '</div>')

# ----------------------------------------------------------------- 문제
T = "바이러스 일반 특징"
Q(P, T, "교재 10장 1번",
  "바이러스의 일반적인 특징과 관련 있는 것을 모두 고르시오.",
  "바이러스의 일반적인 특징으로 맞는 것을 <b>모두</b> 고르시오.",
  "①, ④",
  ["O|①::구조가 가장 단순하고 크기가 가장 작은 미생물 (20~400 nm).",
   "X|②::원핵생물(세균)은 '세포'. 바이러스는 세포가 아니므로 원핵도 진핵도 아님.",
   "X|③::'항상'이 함정! 세포를 망가뜨리는 변화(CPE)가 없는 경우(잠복감염·지속감염)도 많음.",
   "O|④::자기 유전물질(DNA <b>또는</b> RNA)을 가짐 → 생물 같은 특성.",
   "X|⑤::리보솜·미토콘드리아 같은 <b>세포소기관 없음</b> → 그래서 숙주에 기생.",
   "TIP|'항상', '모든', '절대' 같은 말이 있으면 일단 의심!"],
  opts=["단순한 구조를 가지는 크기가 가장 작은 미생물이다.", "원핵미생물에 속한다.",
        "증식과정에서 항상 세포병변효과(cytopathic effect)를 초래한다.", "자기 자신의 유전물질을 가지고 있다.", "세포소기관을 가지고 있다."],
  topts=["구조가 단순하고 가장 작은 미생물이다.", "원핵생물(세균 같은)에 속한다.",
         "증식할 때 항상 세포를 망가뜨리는 변화를 일으킨다.", "자기만의 유전물질을 가지고 있다.", "세포소기관(리보솜 등)을 가지고 있다."], cols=1)

Q(P, T, "교재 10장 2번",
  "바이러스의 일반적인 특징과 관련 있는 것을 모두 고르시오.",
  "바이러스의 일반적인 특징으로 맞는 것을 <b>모두</b> 고르시오.",
  "②, ③",
  ["X|①::거꾸로! 에테르 같은 <b>지용성 용매</b>는 인지질 <b>외피를 녹임</b> → <b>외피 있는</b> 바이러스가 약함. 외피 없는 건 오히려 강함.",
   "O|②::생활사 1단계 '부착': 바이러스 표면 단백질 = 열쇠, 세포 <b>수용체</b> = 자물쇠.",
   "O|③::대사·리보솜이 없으니 숙주 세포 없이는 복제 불가 (절대 세포내 기생).",
   "X|④::20~400 nm → 광학현미경 한계(~200 nm)보다 작아 <b>전자현미경</b>이 필요.",
   "X|⑤::DNA 또는 RNA 중 <b>하나만</b> 가짐. RNA 바이러스도 많음(인플루엔자, HIV…).",
   "KEY|화학 연결: 외피 = 인지질(기름) → '기름은 기름에 녹는다' → 에테르·클로로포름·세제에 파괴"],
  opts=["외피(envelope)가 없는 바이러스는 에테르(ether)와 같은 용매에 의해 쉽게 불활성화된다.",
        "특정 세포 수용체(receptor)와 결합하여 숙주세포 내로 침투한다.", "숙주세포가 없으면 증식할 수 없다.",
        "대부분의 바이러스는 광학현미경으로 관찰할 수 있다.", "다른 미생물들과 같이 모든 바이러스는 DNA를 유전물질로 갖는다."],
  topts=["외피가 없는 바이러스는 에테르 같은 용매에 쉽게 죽는다.", "세포의 특정 수용체에 붙어서 세포 안으로 들어간다.",
         "숙주세포가 없으면 늘어날 수 없다.", "대부분 광학현미경으로 볼 수 있다.", "모든 바이러스는 DNA를 유전물질로 가진다."], cols=1,
  fig=svgs.VSTRUCT, figw=36)

Q(P, T, "교재 10장 3번",
  "정이십면체 캡시드(icosahedral capsid)를 가지고 있는 바이러스를 모두 고르시오.",
  "<b>정이십면체</b>(정삼각형 20개로 된 공 모양) 캡시드를 가진 바이러스를 <b>모두</b> 고르시오.",
  "②, ③, ④, ⑤",
  ["X|①::담배모자이크바이러스(TMV) = <b>나선형</b>(원통 막대) 캡시드의 대표 (강의 예시).",
   "O|②::폴리오바이러스(피코르나) = 비외피 정이십면체.",
   "O|③::유두종바이러스(파포바) = 정이십면체.",
   "O|④::아데노바이러스 = 정이십면체, 캡소미어 252개 (펜톤 12 + 헥손 240).",
   "O|⑤::폴리오마바이러스(파포바) = 정이십면체.",
   "X|⑥::T4 파지 = 머리+꼬리가 있는 <b>복합형</b>.",
   "KEY|나선형 = TMV · 복합형 = 파지·폭스(벽돌형) · 나머지 대부분 = 정이십면체"],
  opts=["tobacco mosaic virus", "poliovirus", "papillomavirus", "adenovirus", "polyomavirus", "T4 phage"],
  topts=["담배모자이크바이러스", "폴리오(소아마비)바이러스", "유두종바이러스", "아데노바이러스", "폴리오마바이러스", "T4 박테리오파지"], cols=3,
  fig="v8.jpg", figw=44)

Q(P, T, "교재 10장 10번",
  "바이러스 구성물에 해당하는 세 가지 용어인 capsid, capsomer, protomer의 크기를 비교하시오.",
  "바이러스 껍질을 이루는 capsid, capsomer, protomer를 <b>크기 순서</b>로 나열하시오.",
  "protomer &lt; capsomer &lt; capsid",
  ["레고로 생각하기: <b>protomer</b>(작은 블록) 5~6개 → <b>capsomer</b>(한 칸 벽돌) → 여러 capsomer → <b>capsid</b>(완성된 집).",
   "강의: 'protomers aggregate to form the capsomer (5-6 protomers)', 'capsomers self-assemble to form the capsid'.",
   "capsid + 핵산 = <b>뉴클레오캡시드</b>, 여기에 외피를 두르면 완전한 바이러스 입자(<b>virion</b>).",
   "TIP|알파벳 길이와 반대: <b>P</b>rotomer → <b>C</b>apso<b>mer</b> → <b>C</b>apsid (mer = 조각)"],
  fig=svgs.VSTRUCT, figw=40)

Q(P, T, "교재 10장 4번",
  "다음 중 바이러스에 의한 질환을 모두 고르시오.",
  "다음 중 <b>바이러스</b>가 일으키는 병을 <b>모두</b> 고르시오.",
  "①, ④, ⑥, ⑦, ⑩",
  ["O|①::소아마비 = 폴리오바이러스 (피코르나).",
   "X|②::발진티푸스 = <i>Rickettsia prowazekii</i> (<b>세균</b>).",
   "X|③::탄저병 = <i>Bacillus anthracis</i> (세균).",
   "O|④::광견병 = 광견병 바이러스 (랍도).",
   "X|⑤::파상풍 = <i>C. tetani</i> (세균, PART 1).",
   "O|⑥::홍역 = 홍역 바이러스 (파라믹소).",
   "O|⑦::황열 = 황열 바이러스 (플라비).",
   "X|⑧::레슈마니아증 = <b>원충</b>.",
   "X|⑨::말라리아 = <i>Plasmodium</i> (원충).",
   "O|⑩::뎅기열 = 뎅기 바이러스 (플라비).",
   "TIP|'티푸스·탄저·파상풍' = 세균 / '말라리아·레슈마니아' = 원충"],
  opts=["소아마비", "발진티푸스", "탄저병", "광견병", "파상풍", "홍역", "황열", "레슈마니아증", "말라리아", "뎅기열"], cols=5,
  topts=["소아마비", "발진티푸스", "탄저병", "광견병", "파상풍", "홍역", "황열", "레슈마니아증", "말라리아", "뎅기열"])

T = "프리온 · 지발성 감염"
Q(P, T, "교재 10장 54번",
  "지발성 퇴행성 감염질환(slow virus infections causing degenerative diseases)으로 분류되는 것을 모두 고르시오.",
  "아주 천천히 진행되며 뇌가 망가지는 <b>지발성 퇴행성 감염 질환</b>에 해당하는 것을 <b>모두</b> 고르시오.",
  "①, ②, ④, ⑤",
  ["O|①::해면양(스펀지 모양) 뇌병증 = 프리온 병의 총칭 (광우병 등).",
   "O|②::프리온 = 잘못 접힌 단백질 → 뇌에 쌓여 천천히 신경세포 파괴.",
   "X|③::delta virus(D형 간염)는 <b>간</b>에 생기는 병, 퇴행성 뇌질환 아님.",
   "O|④::Kuru = 식인 풍습이 있던 파푸아뉴기니 부족의 프리온 병.",
   "O|⑤::CJD(크로이츠펠트-야코프병) = 사람 프리온 병 (변종 CJD는 광우병 관련).",
   "X|⑥::비로이드는 <b>식물</b> 병원체 (감자, 코코넛).",
   "KEY|프리온 병 = 해면상 뇌병증(광우병·CJD·Kuru) · 잠복기 김 · 치료·백신 없음"],
  opts=["해면양뇌병증", "프리온", "delta virus", "Kuru disease", "Creutzfeldt-Jacob disease(CJD)", "비로이드"],
  topts=["해면(스펀지)양 뇌병증", "프리온", "델타 바이러스(D형 간염)", "쿠루병", "크로이츠펠트-야코프병", "비로이드"], cols=2,
  fig="v12.jpg", figw=36)

Q(P, T, "교재 10장 97번 (T/F)",
  "프리온은 잠복 기간이 매우 짧으며 주로 퇴행성 신경질환을 일으킨다.",
  "프리온은 잠복기가 매우 <b>짧고</b>, 주로 퇴행성 신경질환을 일으킨다. (T/F)",
  "F",
  ["뒷부분(퇴행성 신경질환)은 맞지만 앞부분이 틀림: 프리온은 잠복기가 <b>매우 길다</b> (수년~수십 년).",
   "PrP<sup>Sc</sup>가 정상 PrP<sup>C</sup>를 하나씩 잘못 접히게 만들며 아주 천천히 쌓이기 때문.",
   "일단 증상(치매·성격 변화·환각·근육강직·운동실조)이 나오면 <b>6개월 안에 사망</b>하는 경우가 많음.",
   "열·단백질분해효소에 극도로 안정 → 일반 소독으로 잘 안 죽음.",
   "KEY|프리온 = <b>잠복은 길고, 발병 후 진행은 빠르고 치명적</b>"],
  fig="v11.jpg", figw=36)

T = "볼티모어 분류 · 복제 방식"
Q(P, T, "추가 문제 (강의 슬라이드)",
  "Match each Baltimore group with a representative virus family.",
  "볼티모어 그룹과 대표 바이러스 과를 짝지으시오.",
  "I-C, III-E, IV-A, V-D, VI-B, VII-F",
  ["<b>I dsDNA → C. Herpesviridae</b> (폭스·아데노·파포바도 I)",
   "<b>III dsRNA → E. Reoviridae</b> (로타바이러스)",
   "<b>IV (+)ssRNA → A. Picornaviridae</b> (코로나·플라비·토가·칼리시도 IV)",
   "<b>V (−)ssRNA → D. Orthomyxoviridae</b> (파라믹소·랍도·번야도 V)",
   "<b>VI ssRNA-RT → B. Retroviridae</b> (HIV)",
   "<b>VII dsDNA-RT → F. Hepadnaviridae</b> (B형 간염)",
   "KEY|분류 기준 = '유전체로부터 <b>(+) mRNA</b>를 어떻게 만드느냐' (모든 바이러스가 (+)mRNA를 거쳐야 함)"],
  extra_orig='<div class="boxq">Groups: I (dsDNA), III (dsRNA), IV (+ssRNA), V (−ssRNA), VI (ssRNA-RT), VII (dsDNA-RT)<br>'
             'A. Picornaviridae &nbsp; B. Retroviridae &nbsp; C. Herpesviridae &nbsp; D. Orthomyxoviridae &nbsp; E. Reoviridae &nbsp; F. Hepadnaviridae</div>',
  extra_trans='<div class="boxq">그룹: I(이중가닥 DNA), III(이중가닥 RNA), IV(+단일가닥 RNA), V(−단일가닥 RNA), VI(역전사 RNA), VII(역전사 DNA)<br>'
              'A. 피코르나 &nbsp; B. 레트로 &nbsp; C. 헤르페스 &nbsp; D. 오르토믹소(인플루엔자) &nbsp; E. 레오(로타) &nbsp; F. 헤파드나(B형 간염)</div>',
  fig=svgs.BALTIMORE, figw=46)

Q(P, T, "교재 10장 5번 (T/F)",
  "핵산이 단일가닥 (+) sense RNA의 경우 RNA 중합효소에 의해 (-) RNA를 합성한 후 이를 주형으로 (+) RNA를 복제한다.",
  "(+) 단일가닥 RNA 바이러스는 RNA 중합효소로 먼저 (−) RNA를 만들고, 이것을 틀(주형)로 삼아 (+) RNA를 복제한다. (T/F)",
  "T",
  ["(+) RNA는 mRNA와 같은 방향 → 들어가자마자 <b>바로 번역</b>되어 RNA 중합효소(RdRp)부터 만듦.",
   "복제할 땐: (+)RNA → <b>(−)RNA</b>(거울상 틀) → 그 틀로 새 <b>(+)RNA</b> 대량 생산.",
   "DNA 복제에서 상보적 가닥을 틀로 쓰는 것과 같은 원리 (A-U, G-C 짝).",
   "강의: '대부분의 (+) sense RNA 유전체는 그 자체로 감염성'.",
   "KEY|(+)RNA: 번역 바로 O / 복제는 (−)를 거쳐서"])

Q(P, T, "교재 10장 6번 (T/F)",
  "레트로바이러스는 핵산이 (+) sense RNA이나 mRNA로의 역할을 하지 못한다.",
  "레트로바이러스의 유전체는 (+) RNA이지만, mRNA로 쓰이지 못한다. (T/F)",
  "T",
  ["레트로바이러스 유전체는 (+)ssRNA (2개, dimer)이지만 <b>바로 번역하지 않음</b>.",
   "대신 <b>역전사효소</b>로 (+)RNA → (−)DNA → (±)DNA를 만들고, 숙주 DNA에 <b>통합(provirus)</b>한 다음, 거기서 새로 (+)mRNA를 전사.",
   "그래서 같은 (+)RNA라도 볼티모어 <b>IV군과 구별해 VI군(ssRNA-RT)</b>.",
   "KEY|(+)RNA인데 mRNA로 안 쓰고 DNA로 바꾸는 별종 = 레트로"],
  fig=svgs.RETRO, figw=46)

Q(P, T, "교재 10장 7번 (T/F)",
  "레트로바이러스는 핵산이 (-) sense RNA로서 이를 주형으로 하여 DNA를 역전사하며, 합성된 DNA는 숙주 세포 염색체 속으로 이입된다.",
  "레트로바이러스의 유전체는 (−) RNA이고, 이를 틀로 DNA를 역전사하여 숙주 염색체에 끼워 넣는다. (T/F)",
  "F",
  ["뒷부분(역전사 → 숙주 염색체에 통합)은 맞음.",
   "틀린 곳: 레트로바이러스 유전체는 <b>(+) sense</b> ssRNA (바로 앞 6번 문제와 연결).",
   "강의 식: <b>(+) ss RNA → (−) DNA → (±) DNA → (+) mRNA → 단백질</b>.",
   "TIP|부분적으로 맞고 한 단어만 틀린 문장 = 시험 단골 함정. (+)/(−) 부호를 꼭 확인!"])

T = "DNA 바이러스 vs RNA 바이러스"
Q(P, T, "교재 10장 11번",
  "RNA 바이러스에 해당하는 것을 모두 고르시오.",
  "<b>RNA</b> 바이러스를 <b>모두</b> 고르시오.",
  "②, ⑤, ⑥, ⑧, ⑨",
  ["X|①::adenovirus = dsDNA (I군).",
   "O|②::parainfluenza = (−)ssRNA, 파라믹소.",
   "X|③::papillomavirus = dsDNA (파포바).",
   "X|④::poxvirus = dsDNA (천연두).",
   "O|⑤::measles(홍역) = (−)ssRNA, 파라믹소.",
   "O|⑥::coxsackie = (+)ssRNA, 피코르나(엔테로).",
   "X|⑦::polyomavirus = dsDNA (파포바).",
   "O|⑧::rotavirus = <b>dsRNA</b>, 레오 (III군).",
   "O|⑨::mumps(볼거리) = (−)ssRNA, 파라믹소.",
   "X|⑩::human papillomavirus = dsDNA.",
   "TIP|DNA 바이러스는 '<b>헤·아·폭·파·파·헤파</b>'(헤르페스·아데노·폭스·파포바·파보·헤파드나)뿐 → 나머지는 RNA"],
  opts=["adenovirus", "parainfluenza virus", "papillomavirus", "poxvirus", "measles virus", "coxsackie virus", "polyomavirus",
        "rotavirus", "mumps virus", "human papillomavirus"], cols=2,
  topts=["아데노바이러스", "파라인플루엔자 바이러스", "유두종바이러스", "폭스바이러스", "홍역 바이러스", "콕사키 바이러스",
         "폴리오마바이러스", "로타바이러스", "볼거리 바이러스", "사람 유두종바이러스"])

Q(P, T, "교재 10장 12번",
  "DNA 바이러스인 것을 모두 고르시오.",
  "<b>DNA</b> 바이러스를 <b>모두</b> 고르시오.",
  "③, ⑥, ⑦ (교재 표기: ②, ③, ⑥, ⑦)",
  ["X|①::measles(홍역) = RNA (파라믹소).",
   "X|②::Rous sarcoma virus = <b>레트로바이러스</b>(RNA, 알파레트로, 닭 육종). 강의에 명시.",
   "O|③::smallpox(천연두) = dsDNA (폭스).",
   "X|④::influenza = RNA (오르토믹소).",
   "X|⑤::일본뇌염 = RNA (플라비).",
   "O|⑥::Epstein-Barr = dsDNA (헤르페스, HHV-4).",
   "O|⑦::사람 거대세포바이러스(CMV) = dsDNA (헤르페스, HHV-5).",
   "NOTE|교재 정답은 ②③⑥⑦이지만 Rous 육종 바이러스는 강의에서도 <b>레트로(RNA)바이러스</b>로 분류. 내용상 <b>③⑥⑦</b>이 맞습니다. (레트로가 DNA 중간체를 만들어서 생긴 혼동으로 보임)"],
  opts=["measles virus", "Rous sarcoma virus", "smallpox virus", "influenza virus", "일본뇌염 virus", "Epstein-Barr virus",
        "사람 거대세포 바이러스(human cytomegalovirus)"], cols=2,
  topts=["홍역 바이러스", "라우스 육종 바이러스", "천연두 바이러스", "인플루엔자 바이러스", "일본뇌염 바이러스", "엡스타인-바 바이러스",
         "사람 거대세포 바이러스(CMV)"])

Q(P, T, "교재 10장 20번",
  "RNA를 유전물질로 함유하고 있는 것을 모두 고르시오.",
  "<b>RNA</b>를 유전물질로 가진 것을 <b>모두</b> 고르시오.",
  "①, ②, ③",
  ["O|①::measles(홍역) = (−)ssRNA, 파라믹소.",
   "O|②::influenza = (−)ssRNA 8분절, 오르토믹소.",
   "O|③::poliovirus = (+)ssRNA, 피코르나.",
   "X|④::adenovirus = dsDNA.",
   "X|⑤::herpes simplex = dsDNA.",
   "X|⑥::human papillomavirus = dsDNA (원형).",
   "KEY|헤르페스·아데노·유두종 = DNA 3총사 / 홍역·인플루엔자·폴리오 = RNA"],
  opts=["measles virus", "influenza virus", "poliovirus", "adenovirus", "herpes simplex virus", "human papillomavirus"], cols=3,
  topts=["홍역", "인플루엔자", "폴리오", "아데노", "단순헤르페스", "사람 유두종"])
