# -*- coding: utf-8 -*-
from core import RAW, S, SEC, Q, card, ul, table, img
import svgs

P = "vr"
G2 = "PART 2 · 바이러스"

# =================================================================== VI Retro
SEC(G2, "2-9 VI군 ssRNA-RT 레트로 (HIV · HTLV)")
S(P, "2-9", "Retroviridae: 거꾸로 베끼는 바이러스",
  f'<div class="card2 mid">{svgs.RETRO}</div>' +
  '<div class="row c3">' +
  card("구조",
       ul(["~100 nm, <b>외피 O</b>(숙주 세포막 + env 당단백질)", "유전체: <span class='hl'>(+)ssRNA 2개(dimer, 이배체)</span>",
           "<b>gag</b>: 캡시드 등 구조 단백질", "<b>pol</b>: <b>역전사효소 · 통합효소 · 단백분해효소</b>", "<b>env</b>: 외피 단백질 (수용체 결합·진입)"]), "soft") +
  card("생활사 핵심",
       ul(["부착(env ↔ 수용체) → 침입: RNA + 3가지 효소가 세포로", "<b>역전사</b>: (+)RNA → (−)DNA → (±)DNA (역전사효소 = <b>RNA 의존 DNA 중합효소</b>)",
           "<b>통합</b>: dsDNA를 숙주 염색체에 삽입 = <b>provirus</b> (통합효소)", "전사·번역 → 단백분해효소가 gag·pol을 잘라 성숙 → 조립·방출"])) +
  card("속 분류",
       table(["속", "예"], [["Alpha", "<b>Rous 육종 바이러스</b>(1911 Rous, 첫 발암 레트로, 닭)"], ["Beta·Gamma", "쥐·고양이·원숭이 종양/백혈병"],
                          ["<b>Delta</b>", "<b>HTLV</b> (사람 T세포 백혈병)"], ["Epsilon", "물고기 피부 육종"], ["<b>Lenti</b>", "<b>HIV</b>, SIV, FIV"], ["Spuma", "역할 불명"]])) +
  '</div>')

S(P, "2-9", "HIV/AIDS와 HTLV",
  '<div class="row c32">' +
  card("HIV (Lentivirus, lenti = 느린)",
       ul(["AIDS: 면역계가 점점 무너져 <b>기회감염·암</b>으로 사망", "HIV-1(감염력·독성↑, 전 세계) / HIV-2(약함, 서아프리카)",
           "표적: <span class='hl'>CD4+ 세포</span>(도움 T세포, 대식세포)", "수용체 <b>CD4</b> ↔ env(gp160 → <b>gp120</b> + gp41) / 보조수용체 <b>CCR5</b>(M-향성) 또는 <b>CXCR4</b>(T-향성)",
           "전파: <b>성접촉</b>(정액·질액), <b>수혈</b>(혈액), <b>모유</b>",
           "초기: 발열·권태·발진·림프절 부종·구강 칸디다 → 항체 생성 / 말기(8~10년 후) AIDS: 칸디다증·헤르페스(CMV·HSV)·폐렴, 치매, <b>카포시 육종</b>·B세포 림프종",
           "진단: 항체 ELISA, 면역형광, PCR, 혈중 바이러스·<b>CD4+ T세포 수</b>",
           "치료: <b>NRTI · NNRTI · PI · 부착/융합 억제제 · 통합효소 억제제</b> → 병합요법 <b>HAART</b>(칵테일)"]), "soft") +
  img("v154.jpg", "HIV 감염 경과: CD4+ T세포(파랑)는 서서히 감소, 바이러스(빨강)는 말기에 급증", 100) +
  '</div>' +
  '<div class="row c2">' +
  card("HTLV (Deltaretrovirus)",
       ul(["사람 T세포 백혈병 바이러스, HTLV-I~IV", "<b>성인 T세포 백혈병·림프종(ATLL)</b> + 탈수초 질환(HAM/TSP)",
           "전파: <b>성접촉, 모유</b>", "대부분 무증상, ~5%가 30~50년 뒤 ATLL → 1년 내 사망", "남일본·카리브해·중앙아프리카",
           "특이 치료 X, <b>AZT + IFN-α</b> 부분 효과"])) +
  card("HIV 약 정리",
       table(["분류", "약 (끝 글자)"], [["NRTI (뉴클레오사이드 역전사 억제)", "<b>AZT=zidovudine</b>, lamivudine (-vudine)"],
                                     ["NNRTI (비뉴클레오사이드)", "<b>nevirapine, delavirdine, efavirenz</b>"],
                                     ["PI (단백분해효소 억제)", "<b>saquinavir, indinavir, ritonavir, nelfinavir</b> (-navir)"],
                                     ["통합효소 억제", "<b>raltegravir</b> (-gravir)"], ["융합 억제", "enfuvirtide"]]), "warm") +
  '</div>')

T = "역전사효소 · 레트로 복제"
Q(P, T, "교재 10장 44번",
  "역전사효소(reverse transcriptase)에 대한 설명으로 옳은 것을 모두 고르시오.",
  "<b>역전사효소</b>에 대해 옳은 것을 <b>모두</b> 고르시오.",
  "①, ②",
  ["O|①::레트로바이러스가 <b>pol 유전자</b>로 만드는 특이 효소 (HBV도 역전사 활성을 가진 중합효소 보유).",
   "O|②::RNA를 틀로 DNA를 만듦 = <b>RNA-dependent DNA polymerase</b> (강의 그대로).",
   "X|③::RNA 의존 <b>RNA</b> 중합효소(RdRp)는 RNA 바이러스(인플루엔자 등)의 복제 효소.",
   "X|④::DNA topoisomerase = DNA 꼬임을 푸는 효소.",
   "X|⑤::제한효소 = 세균이 가진 DNA 자르는 효소.",
   "TIP|이름 읽는 법: '<b>틀(주형)</b>-dependent <b>만드는 것</b> polymerase' → RNA 틀로 DNA 만듦 = 역전사"],
  opts=["Retrovirus가 가지고 있는 특이효소이다.", "RNA-dependent DNA polymerase이다.", "RNA-dependent RNA polymerase이다.", "DNA Topoisomerase이다.", "제한효소이다."],
  topts=["레트로바이러스의 특이 효소이다.", "RNA를 틀로 DNA를 만드는 중합효소이다.", "RNA를 틀로 RNA를 만드는 중합효소이다.", "DNA 꼬임을 푸는 효소이다.", "DNA를 자르는 제한효소이다."], cols=1,
  fig=svgs.RETRO, figw=44)

Q(P, T, "교재 10장 45번",
  "Retrovirus(예: HIV)에 대한 설명으로 옳은 것을 모두 고르시오.",
  "레트로바이러스(예: HIV)에 대해 옳은 것을 <b>모두</b> 고르시오.",
  "①, ③",
  ["O|①::강의: 'dimer of (+) single-stranded RNA' → 단일가닥 RNA가 <b>2개 한 쌍</b>(이배체). 교재는 이걸 '이중가닥 RNA를 함유'로 표현해 정답 처리.",
   "X|②::역전사효소는 <b>바이러스 자신의 효소</b>(pol 유전자). 숙주 세포엔 역전사효소가 없음.",
   "O|③::dsDNA를 만들어 숙주 염색체에 삽입 → <b>provirus</b>.",
   "X|④::단백분해효소도 <b>바이러스 자신의 것</b>(pol) → 그래서 PI(-navir)가 약이 됨.",
   "NOTE|①은 엄밀히 'dsRNA'(로타처럼 상보적 이중가닥)가 아니라 '(+)ssRNA 2개'입니다. 교재는 ①을 맞다고 하지만, 46번 ②('1개의 양성가닥 RNA' → 틀림)와 같은 포인트 = <b>RNA가 2개</b>라는 것만 기억하세요.",
   "KEY|레트로의 3효소(역전사·통합·단백분해) = <b>모두 바이러스가 직접 가져옴</b> → 모두 약물 표적"],
  opts=["유전물질로 이중가닥 RNA를 함유한다.", "숙주세포의 역전사효소(reverse transcriptase)를 이용한다.", "복제과정에서 이중가닥 DNA를 만들고 숙주세포 염색체에 삽입되어 프로바이러스(provirus) 형태를 만든다.",
        "숙주세포의 단백질분해효소(protease)를 이용한다."],
  topts=["유전물질로 두 가닥의 RNA를 가진다.", "숙주세포의 역전사효소를 쓴다.", "이중가닥 DNA를 만들어 숙주 염색체에 끼워 넣어 프로바이러스가 된다.", "숙주세포의 단백질분해효소를 쓴다."], cols=1)

Q(P, T, "교재 10장 46번",
  "레트로바이러스 증식 과정에 대한 설명 중 옳은 것을 모두 고르시오.",
  "레트로바이러스의 증식 과정에 대해 옳은 것을 <b>모두</b> 고르시오.",
  "①, ③, ④, ⑤",
  ["O|①::(+) 단일가닥이지만 mRNA로 쓰이지 않음 (6번 문제와 같음).",
   "X|②::캡시드 안에 (+)RNA가 <b>2개</b>(이배체) 들어 있음. '1개'가 틀림.",
   "O|③::역전사효소 필수.",
   "O|④::통합효소로 숙주 염색체에 <b>integration</b>.",
   "O|⑤::HIV(Lentivirus), HTLV(Deltaretrovirus).",
   "KEY|레트로 = (+)RNA <b>×2</b> · 역전사 · 통합(provirus) · HIV/HTLV"],
  opts=["핵산이 단일가닥이며 mRNA로서의 역할을 못 한다.", "1개의 양성 가닥 RNA 게놈이 캡시드 안에 들어 있고, 이 캡시드는 외피로 둘러싸여 있다.", "복제과정 중에 역전사효소가 필요하다.",
        "숙주 염색체에 integration하는 과정을 거친다.", "HIV, HTLV가 이에 속한다."],
  topts=["단일가닥이고 mRNA로 쓰이지 못한다.", "(+) RNA 유전체 1개가 캡시드 안에 있고 외피로 싸여 있다.", "복제할 때 역전사효소가 필요하다.", "숙주 염색체에 끼어 들어간다.", "HIV, HTLV가 여기에 속한다."], cols=1)

T = "HIV · HTLV"
Q(P, T, "교재 10장 9번 (T/F)",
  "HIV 바이러스는 CD8 세포 수용체에 결합한다.",
  "HIV는 <b>CD8</b> 세포 수용체에 결합한다. (T/F)",
  "F",
  ["HIV의 수용체는 <b>CD4</b> (도움 T세포, 대식세포 표면). 바이러스 env 단백질 <b>gp120</b>이 CD4에 결합.",
   "보조수용체: <b>CCR5</b>(대식세포 향성) 또는 <b>CXCR4</b>(T세포 향성).",
   "CD8은 바이러스 감염 세포를 죽이는 '살해 T세포'의 표지.",
   "HIV가 CD4+ T세포를 계속 파괴 → CD4 수 감소 → 면역결핍(AIDS).",
   "TIP|HIV는 '<b>4</b>'를 노린다: CD<b>4</b>"], fig="v154.jpg", figw=38)

Q(P, T, "교재 10장 102번",
  "사람면역결핍바이러스(HIV)에 관한 설명으로 옳은 것을 모두 고르시오.",
  "HIV에 대해 옳은 것을 <b>모두</b> 고르시오.",
  "①, ⑤",
  ["O|①::CD4+ T세포를 감염 → provirus로 <b>핵</b>의 숙주 DNA에 통합 → 핵에서 전사(유전체 RNA 생산).",
   "X|②::HAART로 바이러스를 거의 0으로 억제하지만, 통합된 provirus가 남아 <b>완치는 안 됨</b>.",
   "X|③::AZT(zidovudine)는 <b>역전사효소</b> 억제제(NRTI). 단백분해효소 억제제는 -navir.",
   "X|④::반대! 단일약제는 <b>내성</b>이 빨리 생겨서 <b>병합요법</b>(칵테일)이 원칙.",
   "O|⑤::만성 감염 후 CD4+ T세포 급감 → 면역결핍.",
   "KEY|HIV = CD4 · provirus(핵) · 완치 X · <b>병합요법</b> · AZT=NRTI"],
  opts=["CD4+ T 세포를 감염시킨 후 핵에서 바이러스 게놈을 복제한다.", "복합약제치료(combination therapy) 시 완치될 수 있다.", "항HIV 치료제 AZT(zidovudine)는 HIV의 단백질분해효소(protease)를 저해한다.",
        "바이러스의 내성발현 위험성 때문에 단일약제치료(monotherapy)가 선호된다.", "만성감염 후 CD4+ T 세포의 급격한 감소로 면역결핍증을 나타낸다."],
  topts=["CD4+ T세포를 감염시킨 뒤 핵에서 유전체를 복제한다.", "여러 약을 같이 쓰면 완치된다.", "AZT는 HIV 단백질분해효소를 막는다.", "내성 때문에 약 하나만 쓰는 것이 좋다.", "만성 감염 뒤 CD4+ T세포가 급감해 면역결핍이 된다."], cols=1)

Q(P, T, "교재 10장 47번",
  "후천성면역결핍증(AIDS) 환자에게서 주로 일어나는 2차 감염 질병을 모두 고르시오.",
  "AIDS 환자에게 잘 생기는 <b>2차(기회) 감염</b>을 <b>모두</b> 고르시오.",
  "①, ②, ③",
  ["O|①::<i>Pneumocystis jirovecii</i> 폐렴(PCP) = AIDS 대표 기회감염 (곰팡이).",
   "O|②::<i>Cryptococcus neoformans</i> 수막염 (곰팡이).",
   "O|③::<i>Toxoplasma gondii</i> 뇌염 (원충).",
   "X|④::<i>M. pneumoniae</i> 폐렴은 건강한 사람(젊은 층)에게도 흔한 '걸어 다니는 폐렴' → AIDS 특이 감염 아님.",
   "X|⑤::<i>C. difficile</i> 위막성 장염은 <b>항생제</b> 사용이 원인 (PART 1).",
   "KEY|강의: AIDS 기회감염 = 칸디다증, 헤르페스(CMV·HSV), 폐렴 + 암(카포시 육종, B세포 림프종)",
   "TIP|평소엔 T세포가 막는 '곰팡이·원충·헤르페스'가 CD4↓ 때 튀어나옴"],
  opts=["Pneumocystis jirovecii에 의한 폐렴", "Cryptococcus neoformans에 의한 수막염", "Toxoplasma gondii에 의한 뇌수막염", "Mycoplasma pneumoniae에 의한 폐렴", "Clostridium difficile에 의한 위막성 장염"],
  topts=["뉴모시스티스(곰팡이) 폐렴", "크립토코쿠스(곰팡이) 수막염", "톡소플라스마(원충) 뇌수막염", "마이코플라스마 폐렴", "C. difficile 위막성 장염"], cols=1)

Q(P, T, "교재 10장 48번",
  "HTLV(Human T-lymphotropic virus)에 대한 설명으로 옳은 것을 모두 고르시오.",
  "HTLV(사람 T세포 백혈병 바이러스)에 대해 옳은 것을 <b>모두</b> 고르시오.",
  "①, ④, ⑤",
  ["O|①::레트로바이러스(Deltaretrovirus) → <b>역전사효소</b> 보유.",
   "X|②::<b>Retroviridae</b>. Reoviridae는 로타바이러스 (철자 함정: Re<b>tro</b> vs Re<b>o</b>).",
   "X|③::(+)ssRNA 바이러스 (역전사로 DNA 중간체를 만들 뿐).",
   "O|④::레트로는 모두 <b>외피</b>를 가짐.",
   "O|⑤::<b>성인 T세포 백혈병·림프종(ATLL)</b> → 종양성.",
   "KEY|HTLV = 레트로(델타) · RT · 외피 · 성접촉/모유 · ATLL"],
  opts=["역전사 효소를 가지고 있다.", "Reoviridae에 속한 바이러스이다.", "DNA 바이러스이다.", "외피를 가지고 있다.", "종양성을 가진다."],
  topts=["역전사효소가 있다.", "레오바이러스과이다.", "DNA 바이러스이다.", "외피가 있다.", "암을 일으킨다."], cols=2)

T = "항HIV제"
Q(P, T, "교재 10장 49번",
  "후천성면역결핍증(AIDS) 치료제로 비뉴클레오사이드 역전사효소 억제제(non-nucleoside reverse transcriptase inhibitor)에 해당되는 것을 모두 고르시오.",
  "AIDS 치료제 중 <b>비뉴클레오사이드 역전사효소 억제제(NNRTI)</b>를 <b>모두</b> 고르시오.",
  "①, ②, ③",
  ["O|①::nevirapine = NNRTI.",
   "O|②::delavirdine = NNRTI.",
   "O|③::efavirenz = NNRTI.",
   "X|④::azidothymidine(AZT, zidovudine) = <b>NRTI</b> (티미딘 짝퉁 → 뉴클레오사이드형).",
   "X|⑤::saquinavir = <b>PI</b>(단백분해효소 억제제, -navir).",
   "NRTI는 '가짜 블록'으로 DNA 사슬을 끊고, NNRTI는 효소의 다른 자리(알로스테릭 부위)에 붙어 모양을 바꿔 막음.",
   "TIP|AZT는 이름에 '<b>thymidine</b>'(뉴클레오사이드)이 들어있음 → NRTI / -navir = PI / 나머지 '-pine, -dine, -renz' = NNRTI"],
  opts=["nevirapine", "delavirdine", "efavirenz", "azidothymidine", "saquinavir"],
  topts=["네비라핀", "델라비르딘", "에파비렌즈", "아지도티미딘(AZT)", "사퀴나비르"], cols=3, fig=svgs.RETRO, figw=44)

Q(P, T, "교재 10장 50번",
  "후천성면역결핍증(AIDS) 치료제로 단백질분해효소 억제제(protease inhibitor)에 해당하는 것을 모두 고르시오.",
  "AIDS 치료제 중 <b>단백질분해효소 억제제(PI)</b>를 <b>모두</b> 고르시오.",
  "①, ③, ⑤ (내용상 ②도 PI)",
  ["O|①::saquinavir = PI.",
   "?|②::nelfinavir도 실제로는 <b>PI</b>(-navir). 교재 정답에서는 빠져 있음.",
   "O|③::indinavir = PI.",
   "X|④::efavirenz = NNRTI.",
   "O|⑤::ritonavir = PI (다른 PI의 혈중 농도를 올리는 부스터로도 사용).",
   "X|⑥::nevirapine = NNRTI.",
   "NOTE|교재 정답은 ①③⑤이지만 nelfinavir(②)도 단백분해효소 억제제입니다. 시험에선 <b>'-navir' = PI</b> 규칙으로 판단하세요.",
   "KEY|PI는 바이러스 단백분해효소가 gag·pol 긴 단백질을 자르지 못하게 함 → 미성숙(감염력 없는) 바이러스"],
  opts=["saquinavir", "nelfinavir", "indinavir", "efavirenz", "ritonavir", "nevirapine"],
  topts=["사퀴나비르", "넬피나비르", "인디나비르", "에파비렌즈", "리토나비르", "네비라핀"], cols=3, fig=svgs.RETRO, figw=44)

# =================================================================== VII HBV + 간염
SEC(G2, "2-10 VII군 dsDNA-RT B형 간염 + 간염 바이러스 비교")
S(P, "2-10", "Hepadnaviridae: B형 간염 바이러스(HBV) + 간염 A~E 비교",
  '<div class="row c32">' +
  card("HBV 구조와 복제",
       ul(["가장 작은 동물 바이러스 중 하나", "<b>Dane 입자</b>(42~47 nm) = 완전한 바이러스 = <b>감염성 O</b>",
           "<b>HBsAg 입자</b>(~22 nm) = DNA 없는 빈 껍데기 = <b>감염성 X</b> (백신 재료)",
           "외피 O + 정이십면체 뉴클레오캡시드(DNA + <b>역전사 활성 DNA 중합효소</b>)",
           "<span class='hl'>부분 이중가닥 원형 DNA</span>", "dsDNA → <b>pregenomic RNA</b>((+)ssRNA) → 역전사 → (−)ssDNA → dsDNA",
           "pregenomic RNA = mRNA 역할 + 유전체 복제의 틀"]), "soft") +
  img("v159.jpg", "HBV 유전체: 부분 이중가닥 원형 DNA", 100) +
  '</div>' +
  '<div class="row c2">' +
  card("HBV 임상 · 관리",
       ul(["초기: 발열, 식욕부진, 피로, 구역 → 대부분 몇 달 내 회복",
           "<b>만성화</b>: 성인 5~10% · 어린이 30~50% · <span class='hl'>영아 80~90%</span> (어릴수록 만성!)",
           "만성 환자의 15~20% → 간경변·<b>간암</b>으로 사망", "전파: 혈액(수혈), 성접촉, 모자 감염",
           "진단: 항원·항체 ELISA", "예방: <b>재조합 HBsAg 백신</b>",
           "급성: 특이 치료 X, <b>HBIG</b>(노출 1주 내·신생아) / 만성: <b>lamivudine</b>, famciclovir, adefovir dipivoxil, IFN-α"]), "") +
  f'<div style="display:flex;flex-direction:column;gap:2mm"><div class="card2 short">{svgs.HEP}</div>' +
  table(["", "A", "B", "C", "D", "E"], [
      ["과", "피코르나", "헤파드나", "플라비", "델타(결손)", "헤페"],
      ["핵산", "RNA", "<b>DNA</b>", "RNA", "RNA", "RNA"],
      ["전파", "분변-경구", "혈액·성", "혈액·성", "혈액(B 필요)", "분변-경구"],
      ["만성", "X", "O", "<b>O(50~80%)</b>", "O", "드묾"],
      ["백신", "O(불활화)", "O(재조합)", "<b>X</b>", "B백신으로", "O(재조합)"]]) + '</div>' +
  '</div>')

T = "B형 간염 · 간염 비교"
Q(P, T, "교재 10장 41번",
  "B형 간염 바이러스(hepatitis B virus)에 대한 설명으로 옳은 것을 모두 고르시오.",
  "B형 간염 바이러스(HBV)에 대해 옳은 것을 <b>모두</b> 고르시오.",
  "②, ③, ⑤",
  ["X|①::Hepadnaviridae, 외피 있는 작은 바이러스 맞지만 <b>DNA</b> 바이러스 (부분 이중가닥 원형 DNA).",
   "O|②::pregenomic RNA를 <b>역전사</b>해서 DNA 유전체를 만듦 → 볼티모어 VII군(dsDNA-RT).",
   "O|③::혈액(수혈)·성접촉·모자 감염.",
   "X|④::성인 5~10%, 영아 80~90%가 <b>만성</b> → 간경변·간암.",
   "O|⑤::만성 치료: lamivudine, famciclovir, adefovir dipivoxil (+IFN-α).",
   "KEY|HBV = <b>DNA인데 역전사</b>하는 별종 (레트로는 RNA인데 DNA로, HBV는 DNA인데 RNA를 거쳐서)"],
  opts=["Hepadnaviridae에 속하며, 외피가 있는 작은 RNA 바이러스이다.", "역전사 과정(reverse transcription)을 수행한다.", "수혈 및 성 접촉을 통해 감염될 수 있다.",
        "감염되더라도 만성 간염으로는 진전되지 않는다.", "Lamivudine, famciclovir, adefovir dipivoxil 등의 치료제를 사용할 수 있다."],
  topts=["헤파드나과이며 외피가 있는 작은 RNA 바이러스이다.", "역전사 과정을 거친다.", "수혈과 성접촉으로 감염될 수 있다.", "만성 간염으로 진행하지 않는다.", "라미부딘, 팜시클로버, 아데포비어로 치료할 수 있다."], cols=1,
  fig="v159.jpg", figw=26)

Q(P, T, "추가 문제 (강의 슬라이드)",
  "Choose ALL correct statements about hepatitis B virus (HBV) particles and infection.",
  "B형 간염 바이러스(HBV)의 입자와 감염에 대해 옳은 것을 <b>모두</b> 고르시오.",
  "①, ③, ⑤",
  ["O|①::<b>Dane 입자</b>(42~47 nm) = DNA를 가진 완전한 바이러스 → 감염성.",
   "X|②::<b>HBsAg 입자</b>(~22 nm)는 DNA가 없는 빈 껍데기 → <b>감염성 없음</b> → 그래서 백신으로 씀.",
   "O|③::어릴수록 만성화: 영아 80~90% > 어린이 30~50% > 성인 5~10%.",
   "X|④::백신은 <b>재조합 HBsAg</b> 백신 (효모에서 만든 표면 단백질). 생백신 아님.",
   "O|⑤::급성 노출(1주 이내)·HBV 산모의 신생아에게 <b>B형 간염 면역글로불린(HBIG)</b>.",
   "KEY|Dane = 감염성 / HBsAg = 비감염성(백신) / 영아일수록 만성"],
  opts=["The Dane particle (42–47 nm) is the complete, infectious virion.",
        "The ~22 nm HBsAg particle contains viral DNA and is highly infectious.",
        "The younger the patient, the more likely chronic hepatitis B develops.",
        "Prevention uses a live-attenuated HBV vaccine.",
        "Hepatitis B immunoglobulin is given within 1 week after exposure or to newborn babies."],
  topts=["Dane 입자(42~47 nm)가 완전한 감염성 바이러스이다.", "22 nm HBsAg 입자는 DNA를 가지며 감염성이 높다.", "나이가 어릴수록 만성 B형 간염이 되기 쉽다.",
         "약독화 생백신으로 예방한다.", "노출 1주 이내나 신생아에게 B형 간염 면역글로불린을 준다."], cols=1)

Q(P, T, "교재 10장 42번",
  "바이러스성 간염(viral hepatitis)에 관한 설명으로 옳은 것을 모두 고르시오.",
  "바이러스 간염에 대해 옳은 것을 <b>모두</b> 고르시오.",
  "③, ⑤",
  ["X|①::A형은 <b>분변-경구</b> (물·음식).",
   "X|②::B·C형은 <b>혈액·성접촉</b>. 분변-경구는 A·E형.",
   "O|③::C형 간염 = (페그)인터페론 α + ribavirin 병합요법 (강의).",
   "X|④::B형은 <b>DNA</b> 바이러스.",
   "O|⑤::D형(delta)은 혼자 증식 못 하는 <b>결손 바이러스</b> → B형 표면항원(HBsAg)을 빌려 써야 함 → B형 환자에서만.",
   "KEY|A·E = 입 / B·C·D = 피 · B만 DNA · D는 B에 기생"],
  opts=["A형 간염은 주로 혈액을 매개로 감염된다.", "B형 및 C형 간염은 주로 분변과 경구의 오염을 통해 전파된다.", "C형 간염은 인터페론 알파(interferon-α)와 리바비린(ribavirin)의 혼합요법으로 치료한다.",
        "A형, B형, C형 간염 모두 RNA 바이러스에 의한 질환이다.", "D형 간염은 B형 간염 환자에서만 나타난다."],
  topts=["A형은 주로 혈액으로 감염된다.", "B·C형은 주로 대변-입으로 퍼진다.", "C형은 인터페론-α + 리바비린으로 치료한다.", "A·B·C형 모두 RNA 바이러스 병이다.", "D형은 B형 환자에게서만 생긴다."], cols=1,
  fig=svgs.HEP, figw=36)

Q(P, T, "교재 10장 98번 (T/F)",
  "B형 간염 바이러스 및 C형 간염 바이러스는 혈액 또는 장기 이식을 통해 전파되며, A형 간염 바이러스와 D형 간염 바이러스는 경구를 통해 전파된다.",
  "B·C형 간염 바이러스는 혈액이나 장기 이식으로, A·<b>D</b>형 간염 바이러스는 입(경구)으로 전파된다. (T/F)",
  "F",
  ["앞부분(B·C = 혈액·이식)은 맞음.",
   "틀린 곳: 경구 전파는 <b>A형과 E형</b>. <b>D형은 혈액</b>으로 전파 (B형과 함께).",
   "강의: E형 = 'fecal-oral route; via contaminated foods and water (\"E\" = enteric)'.",
   "TIP|모음 <b>A·E</b>는 입(mouth)으로 / 자음 <b>B·C·D</b>는 피(blood)로"], fig=svgs.HEP, figw=40)

# =================================================================== 종합
SEC(G2, "2-11 바이러스 종합 (종양 바이러스 · 전파 경로 · 약 총정리)")
S(P, "2-11", "종합 ① 종양 바이러스 · 선천 감염 · 신경 후유증",
  '<div class="row c2">' +
  card("종양(암) 바이러스 짝짓기",
       table(["바이러스", "핵산", "암"], [
           ["<b>HBV</b>", "DNA", "간암"], ["<b>HCV</b>", "RNA", "간암 (간암 주원인)"], ["<b>HPV</b> 16·18", "DNA", "자궁경부암"],
           ["<b>EBV</b> (HHV-4)", "DNA", "<b>버킷림프종</b>·호지킨림프종·<b>비인두암</b>"], ["<b>KSHV</b> (HHV-8)", "DNA", "<b>카포시 육종</b>"],
           ["<b>HTLV</b>", "RNA(레트로)", "성인 T세포 백혈병·림프종"], ["Rous 육종 바이러스", "RNA(레트로)", "닭 육종 (첫 발암 레트로)"],
           ["폴리오마/SV40, 아데노(E1A·B)", "DNA", "동물 종양/시험관 형질전환"],
           ["HIV", "RNA(레트로)", "직접 X, 면역저하로 카포시 육종·림프종 증가"]])) +
  '<div style="display:flex;flex-direction:column;gap:2.4mm">' +
  card("태반 통한 선천 감염 (TORCH 중 바이러스)",
       ul(["<b>풍진</b>: 선천성 풍진 증후군 (임신 초기)", "<b>CMV</b>: 거대세포 봉입체병 (40% 전파)", "<b>VZV</b>: 선천성 수두 증후군 (20주 이전)", "<b>지카</b>: 소두증",
           "HSV-2는 주로 <b>분만 시 산도</b>로 감염 (주산기)"]), "soft") +
  card("암기: EBV ↔ KSHV 바꿔치기 함정",
       ul(["<b>E</b>BV = 버킷림프종 (Epstein-Barr, '<b>E</b>BV는 <b>B</b>urkitt')", "HHV-<b>8</b> = KSHV = <b>K</b>aposi", "시험에선 둘을 바꿔 놓고 'X' 고르게 함"]), "warm") +
  '</div></div>')

S(P, "2-11", "종합 ② 전파 경로 · 매개체 · 봉입체 · 백신 · 치료제",
  '<div class="row c3">' +
  card("전파 경로",
       table(["경로", "바이러스"], [["분변-경구", "로타, 노로, <b>A·E형 간염</b>, 폴리오·콕사키·에코, 아데노"],
                                 ["호흡기(비말·공기)", "인플루엔자, 홍역, 볼거리, 풍진, RSV, 리노, 코로나, 천연두, VZV, 아데노"],
                                 ["혈액·성접촉", "<b>HIV, HBV, HCV, HDV</b>, HTLV, HSV-2, HPV, CMV"],
                                 ["동물 물림·침", "광견병, 한타(쥐 배설물)"],
                                 ["모기", "황열·뎅기·지카(Aedes), 일본뇌염·웨스트나일(Culex), 알파(말뇌염)"]])) +
  card("인수공통 (동물 → 사람)",
       ul(["인플루엔자 A(새·돼지), MERS(박쥐→낙타), 니파·헨드라(과일박쥐)", "광견병(개·야생동물), 한타(쥐), 일본뇌염(돼지)", "황열·뎅기·지카·웨스트나일, 엠폭스, 로타",
           "에볼라 출혈열·라사열(교재)"]), "soft") +
  card("특징 소견",
       table(["소견", "병"], [["Koplik 반점", "홍역"], ["Negri 소체", "광견병"], ["Guarnieri 소체", "천연두"], ["부엉이 눈 봉입체", "CMV"], ["다핵 거대세포", "HSV·VZV"],
                             ["세포융합(syncytia)", "RSV"], ["해면(스펀지) 뇌", "프리온"]])) +
  '</div>' +
  '<div class="row c2">' +
  card("백신 있음/없음 (강의 기준)",
       table(["있음", "없음"], [["천연두(생), 수두(생), MMR(생), 황열(생), 뎅기(생, 4가), 일본뇌염(사), A형 간염(사), 폴리오(사·생), 로타(경구 생), HPV(VLP), B형 간염(재조합), E형 간염(재조합), 광견병, 한타(Hantavax), 인플루엔자",
                                "아데노, 헤르페스(HSV), 코로나·MERS, 리노, 노로, 콕사키·에코, C형 간염, 웨스트나일(사람), 지카, 알파바이러스, RSV(예방 항체만), HIV, 프리온"]])) +
  card("항바이러스제 끝말 총정리",
       table(["끝말/약", "대상·작용"], [["-ciclovir (acyclovir 등)", "헤르페스 DNA pol (구아노신 유사체)"], ["ganciclovir·cidofovir·foscarnet", "CMV"],
                                     ["-amivir (oseltamivir·zanamivir)", "인플루엔자 NA"], ["amantadine·rimantadine", "인플루엔자 A M2"],
                                     ["-vudine (zidovudine·lamivudine)", "역전사효소(NRTI) → HIV, HBV(lamivudine)"], ["nevirapine·efavirenz·delavirdine", "NNRTI (HIV)"],
                                     ["-navir", "HIV 단백분해효소"], ["-gravir", "HIV 통합효소"], ["ribavirin", "구아노신 유사체: RSV, HCV(+IFN-α), 한타"],
                                     ["interferon-α·β", "숙주 표적 (항바이러스 상태 유도): HCV, HBV"]]), "warm") +
  '</div>')

T = "바이러스 종합"
Q(P, T, "교재 10장 21번",
  "옳게 기술된 것을 모두 고르시오.",
  "옳은 설명을 <b>모두</b> 고르시오.",
  "①, ③, ④",
  ["O|①::VZV는 1차 감염 수두, 재활성화 <b>대상포진</b>.",
   "X|②::한타바이러스는 <b>설치류(쥐)</b>의 침·배설물로 전파. 모기 X.",
   "O|③::로타바이러스 = 유아 설사의 가장 흔한 원인.",
   "O|④::광견병 = 동물 침(물림)으로 매개, 신경친화성(뇌).",
   "X|⑤::리노는 혈청형 105개, 교차면역 X → <b>백신 없음</b>.",
   "KEY|매개 경로 구별: 한타 = 쥐 / 일본뇌염 = 모기 / 광견병 = 물림"],
  opts=["Varicella zoster virus는 대상포진을 유발한다.", "Hantavirus의 감염은 모기에 의해 매개된다.", "Rotavirus는 유아에게 설사병을 유발한다.",
        "Rabies virus는 동물에 의하여 매개되며 뇌 조직에 대한 친화성을 보인다.", "Rhinovirus는 현재 상용화 백신에 의해 예방할 수 있다."],
  topts=["VZV는 대상포진을 일으킨다.", "한타바이러스는 모기가 옮긴다.", "로타바이러스는 아기에게 설사를 일으킨다.", "광견병 바이러스는 동물이 옮기며 뇌 조직을 좋아한다.", "리노바이러스는 백신으로 예방할 수 있다."], cols=1)

Q(P, T, "교재 10장 22번",
  "옳게 기술된 것을 모두 고르시오.",
  "옳은 설명을 <b>모두</b> 고르시오.",
  "①, ②, ③",
  ["O|①::홍역 = MMR 생백신으로 예방.",
   "O|②::광견병 → 인두 경련 → 물을 무서워함 = <b>공수병(hydrophobia)</b>.",
   "O|③::HBV → 만성 간염 → 간경변 → <b>간암</b>.",
   "X|④::인플루엔자 치료제 있음: oseltamivir, zanamivir, amantadine, baloxavir 등.",
   "X|⑤::폴리오 감염의 <b>95%는 무증상</b>, 마비성 소아마비는 <b>1% 미만</b>.",
   "TIP|'대부분의 경우'라는 표현 → 폴리오는 대부분 무증상!"],
  opts=["Measles virus는 현재 상용화 백신에 의해 예방이 가능하다.", "Rabies virus는 hydrophobia를 유발할 수 있다.", "Hepatitis B virus는 암을 유발할 수 있다.",
        "Influenza virus에 대한 치료제가 현재 개발되어 있지 않다.", "Poliovirus는 대부분의 경우 poliomyelitis를 유발한다."],
  topts=["홍역은 백신으로 예방할 수 있다.", "광견병은 공수병(물 공포)을 일으킬 수 있다.", "B형 간염 바이러스는 암을 일으킬 수 있다.", "인플루엔자 치료제는 아직 없다.", "폴리오는 대부분 소아마비(마비)를 일으킨다."], cols=1)

Q(P, T, "교재 10장 23번",
  "옳게 기술된 것을 모두 고르시오.",
  "바이러스와 소속 과(family)가 옳게 짝지어진 것을 <b>모두</b> 고르시오.",
  "①, ②",
  ["O|①::유두종바이러스 → <b>Papovaviridae</b> (현재는 Papillomaviridae로 분리).",
   "O|②::광견병 → <b>Rhabdoviridae</b>.",
   "X|③::인플루엔자 → <b>Orthomyxoviridae</b>. Paramyxo는 홍역·볼거리·RSV.",
   "X|④::C형 간염 → <b>Flaviviridae</b> (옛날엔 토가에 포함됐지만 지금은 플라비).",
   "X|⑤::노로 → <b>Caliciviridae</b>. Picorna는 폴리오·콕사키·리노·HAV.",
   "TIP|<b>Ortho</b>myxo = 인플루엔자(독감) / <b>Para</b>myxo = 홍역·볼거리·RSV"],
  opts=["유두종바이러스는 Papovaviridae에 속한다.", "광견병 바이러스는 Rhabdoviridae에 속한다.", "인플루엔자 바이러스는 Paramyxoviridae에 속한다.",
        "C형 간염 바이러스는 Togaviridae에 속한다.", "노로바이러스는 Picornaviridae에 속한다."],
  topts=["유두종 → 파포바과", "광견병 → 랍도과", "인플루엔자 → 파라믹소과", "C형 간염 → 토가과", "노로 → 피코르나과"], cols=1)

Q(P, T, "교재 10장 30번",
  "종양을 유발하는 RNA 바이러스를 모두 고르시오.",
  "암을 일으키는 <b>RNA</b> 바이러스를 <b>모두</b> 고르시오.",
  "교재: ①, ③ / 강의 기준: ②, ③ (+①)",
  ["?|①::HIV = RNA(레트로). 직접 암을 만들진 않지만 면역저하로 <b>카포시 육종·림프종</b>이 늘어나서 교재는 정답 처리 (67번 '에이즈-발암성 O'와 같은 관점).",
   "O|②::Rous sarcoma virus = RNA(알파레트로), <b>최초의 발암 레트로바이러스</b>(닭 육종). 강의 명시.",
   "O|③::HTLV = RNA(델타레트로) → 성인 T세포 백혈병.",
   "X|④::papillomavirus = <b>DNA</b>.",
   "X|⑤::EBV = <b>DNA</b>(헤르페스).",
   "X|⑥::KSHV = <b>DNA</b>(헤르페스).",
   "NOTE|교재 정답 ①③에는 ②가 빠져 있지만, 바로 다음 31번에서 Rous 육종 바이러스를 '종양 유발 RNA 바이러스'로 취급합니다. <b>②③은 확실한 정답</b>, ①은 교재 관점.",
   "KEY|발암 RNA 바이러스 = <b>레트로(HTLV, Rous)</b> + HCV / 나머지 발암 바이러스는 대부분 DNA"],
  opts=["human immunodeficiency virus", "Rous sarcoma virus", "human T-lymphotropic virus", "papilloma virus", "Epstein-Barr virus", "Kaposi's sarcoma-associated herpesvirus"],
  topts=["HIV", "라우스 육종 바이러스", "HTLV", "유두종바이러스", "EBV", "KSHV(HHV-8)"], cols=2)

Q(P, T, "교재 10장 31번",
  "종양을 유발하는 DNA 바이러스가 아닌 것을 모두 고르시오.",
  "'암을 일으키는 DNA 바이러스'가 <b>아닌</b> 것을 모두 고르시오.",
  "①, ②",
  ["X|①::VZV = DNA지만 <b>암을 일으키지 않음</b> (수두·대상포진).",
   "X|②::Rous sarcoma virus = 암은 일으키지만 <b>RNA</b>(레트로).",
   "O|③::폴리오마 = DNA 종양 바이러스 (SV40 등).",
   "O|④::HBV = DNA → 간암.",
   "O|⑤::KSHV = DNA → 카포시 육종.",
   "TIP|조건 두 개('DNA' + '종양') 중 하나라도 어긋나면 정답. VZV는 '종양' 탈락, Rous는 'DNA' 탈락"],
  opts=["varicella zoster virus", "Rous sarcoma virus", "Polyomavirus", "hepatitis B virus", "Kaposi's sarcoma-associated herpesvirus"],
  topts=["수두-대상포진 바이러스", "라우스 육종 바이러스", "폴리오마바이러스", "B형 간염 바이러스", "KSHV"], cols=1)

Q(P, T, "교재 10장 70번",
  "종양바이러스와 그에 관련된 대표적인 암의 종류가 바르게 연결된 것을 모두 고르시오.",
  "종양 바이러스와 대표 암이 <b>바르게</b> 연결된 것을 모두 고르시오.",
  "①, ③, ④",
  ["O|①::HBV → 간암.",
   "?|②::EBV의 대표 암은 <b>버킷림프종</b>. 강의엔 <b>비인두암</b>(두경부 종양)도 EBV 관련으로 나오지만, 교재는 '대표적인' 연결이 아니라고 보고 X 처리.",
   "O|③::HPV → 자궁경부암.",
   "O|④::HTLV → 성인 T세포 백혈병·<b>T 림프종</b>.",
   "X|⑤::HSV는 암과 무관. 자궁경부암은 <b>HPV</b>.",
   "NOTE|②는 강의 내용(EBV–nasopharyngeal carcinoma)으로 보면 맞을 수도 있어요. 시험에서 '대표적인 암'을 물으면 EBV = <b>버킷림프종</b>으로 답하세요.",
   "KEY|HBV-간암 · HPV-자궁경부암 · HTLV-T세포 백혈병 · EBV-버킷 · KSHV-카포시"],
  opts=["B형 간염 바이러스 - 간암", "엡스타인바 바이러스 - 암성 두경부종양", "인유두종바이러스 - 자궁경부암", "사람 T 세포 백혈병 바이러스 - T 림프종", "단순헤르페스바이러스 - 자궁경부암"],
  topts=["HBV - 간암", "EBV - 두경부(머리·목) 암", "HPV - 자궁경부암", "HTLV - T 림프종", "HSV - 자궁경부암"], cols=1)

Q(P, T, "교재 10장 87번",
  "종양 바이러스의 이름과 이와 관련된 암의 종류를 바르게 연결한 것을 모두 고르시오.",
  "종양 바이러스와 관련 암이 <b>바르게</b> 연결된 것을 모두 고르시오.",
  "①, ③, ⑤",
  ["O|①::HBV - 간암.",
   "X|②::HHV-8(KSHV)은 <b>카포시 육종</b>. 버킷림프종은 EBV.",
   "O|③::HPV - 자궁경부암.",
   "X|④::EBV는 <b>버킷림프종</b>. 카포시 육종은 KSHV.",
   "O|⑤::HTLV - T 림프종(성인 T세포 백혈병·림프종).",
   "TIP|②와 ④는 서로 <b>바꿔치기</b>한 함정! KSHV = <b>K</b>aposi(이름에 있음) / EBV = <b>B</b>urkitt"],
  opts=["HBV - 간암", "HHV-8(KSHV) - 버킷림프종", "HPV - 자궁경부암", "EBV - 카포시육종", "HTLV - T 림프종"], cols=2,
  topts=["HBV - 간암", "HHV-8(KSHV) - 버킷림프종", "HPV - 자궁경부암", "EBV - 카포시 육종", "HTLV - T 림프종"])

Q(P, T, "교재 10장 67번",
  "바이러스 감염병과 그 특징이 바르게 연결된 것을 모두 고르시오.",
  "바이러스 병과 특징이 <b>바르게</b> 연결된 것을 모두 고르시오.",
  "②, ③, ④",
  ["X|①::천연두는 <b>잠복감염 X</b> (나으면 끝, 강한 면역). 잠복감염은 헤르페스.",
   "O|②::로타바이러스 = <b>분절 게놈</b>(dsRNA 10~12조각).",
   "O|③::광견병 = <b>Negri 소체</b>.",
   "O|④::에이즈 = 면역저하로 카포시 육종·림프종 등 암 발생 ↑ → 교재는 '발암성' O.",
   "X|⑤::A형 간염은 <b>급성만</b>, 만성·간암 X.",
   "KEY|분절 게놈 = 로타 · 인플루엔자 · 한타 / 잠복 = 헤르페스 / 만성→암 = B·C형 간염"],
  opts=["천연두 - 잠복감염", "로타바이러스 감염증 - 분절 게놈", "광견병 - Negri 소체", "에이즈 - 발암성", "A형 간염 - 발암성"],
  topts=["천연두 - 잠복감염", "로타 - 조각난 유전체", "광견병 - 네그리 소체", "에이즈 - 암 발생", "A형 간염 - 암 발생"], cols=2)

Q(P, T, "교재 10장 68번",
  "신경성 후유증이 없는 바이러스 질환을 모두 고르시오.",
  "<b>신경 후유증이 없는</b> 바이러스 질환을 모두 고르시오.",
  "②, ⑥",
  ["X|①::광견병 = 중추신경계 감염.",
   "O|②::천연두 = 피부·전신 질환 (흉터는 남지만 신경 후유증은 아님).",
   "X|③::무균성 뇌척수막염 = 이름 그대로 뇌·척수막 (에코·콕사키).",
   "X|④::일본뇌염 = 뇌염 후유증(마비·지적장애).",
   "X|⑤::유행성 회백수염(소아마비) = 척수 회백질 → 마비 후유증.",
   "O|⑥::바이러스성 설사(로타·노로) = 장.",
   "TIP|이름에 '뇌·척수·수막·회백수'가 있거나 신경친화성(광견병)이면 신경계!"],
  opts=["광견병", "천연두", "무균성 뇌척수막염", "일본뇌염", "유행성회백수염", "바이러스성 설사"],
  topts=["광견병", "천연두", "무균성 뇌척수막염", "일본뇌염", "소아마비(유행성 회백수염)", "바이러스성 설사"], cols=3)

Q(P, T, "교재 10장 37번",
  "임산부의 태반 감염을 통한 선천성 감염 질환을 모두 고르시오.",
  "임신부의 <b>태반을 통해</b> 태아에게 생기는 선천성 감염을 <b>모두</b> 고르시오.",
  "②, ④ (교재 의도: ②, ③, ④)",
  ["X|①::홍역은 선천성 기형 감염의 대표가 아님.",
   "O|②::CMV = 선천성 <b>거대세포 봉입체병</b> (전파 확률 40%) — 강의.",
   "?|③::성기포진(HSV-2)은 주로 <b>분만 시 산도</b>를 통한 신생아 감염 (주산기 감염). 교재는 정답에 포함.",
   "O|④::풍진 = <b>선천성 풍진 증후군</b>, 강의: 'transplacental infection'.",
   "NOTE|교재 정답은 '②③⑤'로 인쇄됐지만 보기는 ①~④뿐이라 오타입니다. '태반 감염'이라는 조건에 엄밀히 맞는 건 <b>②④</b>, 교재 의도는 ②③④로 보입니다.",
   "KEY|선천성(태반) 감염 = 풍진 · CMV · VZV(20주 전) · 지카(소두증) / HSV = 분만 시"],
  opts=["홍역(measles)", "거대세포바이러스감염증(CMV)", "성기포진(genital herpes)", "풍진(rubella)"],
  topts=["홍역", "거대세포바이러스(CMV) 감염", "생식기 포진", "풍진"], cols=2)

Q(P, T, "교재 10장 86번",
  "경구를 통해 전파되는 바이러스를 모두 고르시오.",
  "<b>입(경구)</b>으로 전파되는 바이러스를 <b>모두</b> 고르시오.",
  "①, ③, ⑤, ⑦, ⑨, ⑩",
  ["O|①::로타 = 분변-경구.",
   "X|②::C형 간염 = 혈액.",
   "O|③::A형 간염 = 분변-경구.",
   "X|④::EBV = 침(키스병)이지만 소화관 감염 X, 교재 기준 경구 전파로 보지 않음.",
   "O|⑤::아데노 = 비말 + <b>분변-경구</b>(강의).",
   "X|⑥::HSV = 직접 접촉.",
   "O|⑦::아스트로 = 위장관염 (분변-경구).",
   "X|⑧::CMV = 침·소변·혈액·성접촉.",
   "O|⑨::노로 = 분변-경구 (조개류).",
   "O|⑩::소아마비(폴리오) = 분변-경구 (+호흡기).",
   "KEY|분변-경구 = <b>외피 없는</b> 튼튼한 바이러스가 대부분 (산·담즙을 견딤)"],
  opts=["로타바이러스", "C형 간염 바이러스", "A형 간염 바이러스", "엡스타인바 바이러스", "아데노바이러스", "단순헤르페스바이러스", "아스트로바이러스", "거대세포바이러스", "노로바이러스", "소아마비 바이러스"], cols=2,
  topts=["로타", "C형 간염", "A형 간염", "엡스타인-바(EBV)", "아데노", "단순헤르페스", "아스트로", "거대세포(CMV)", "노로", "소아마비(폴리오)"])

Q(P, T, "교재 10장 99번 (T/F)",
  "바이러스가 감염된 동물을 통해 전파되는 질병으로 에볼라출혈열, 신증후출혈열, 공수병, 라사열 등이 있다.",
  "감염된 <b>동물</b>을 통해 전파되는 바이러스 병으로 에볼라출혈열, 신증후출혈열, 공수병(광견병), 라사열 등이 있다. (T/F)",
  "T",
  ["<b>에볼라출혈열</b>: 박쥐 등 야생동물 → 사람 (필로바이러스).",
   "<b>신증후출혈열</b>: 쥐(등줄쥐) → 한타바이러스 (강의).",
   "<b>공수병</b> = 광견병: 감염 동물 침 (강의).",
   "<b>라사열</b>: 쥐(다유방쥐) 배설물 → 아레나바이러스.",
   "모두 <b>인수공통감염병(zoonosis)</b>.",
   "KEY|출혈열(에볼라·한타·라사)은 대부분 동물(박쥐·쥐) 유래"])

Q(P, T, "교재 10장 101번",
  "항바이러스제 가운데 숙주세포의 기능을 저해함으로써(host-targeting) 항바이러스 활성을 나타내는 약물을 모두 고르시오.",
  "바이러스가 아니라 <b>숙주세포</b> 쪽에 작용해서(host-targeting) 항바이러스 효과를 내는 약을 <b>모두</b> 고르시오.",
  "②, ③",
  ["X|①::ribavirin = 구아노신 유사체 → 주로 <b>바이러스 RNA 중합효소</b>·RNA 합성 방해 (교재 기준 바이러스 표적).",
   "O|②::interferon-α = 숙주 세포에 '항바이러스 상태'를 유도 (단백질 합성 억제, RNA 분해 효소 활성) → 숙주 표적.",
   "O|③::interferon-β = 같은 원리.",
   "X|④::ritonavir = <b>HIV 단백분해효소</b> 억제 (바이러스 표적).",
   "X|⑤::raltegravir = <b>HIV 통합효소</b> 억제 (바이러스 표적).",
   "KEY|인터페론 = 몸이 원래 만드는 '경보 단백질' → 주변 세포를 바이러스에 강하게 만듦 (C형 간염, B형 간염, 리노 치료에 사용)"],
  opts=["ribavirin", "interferon-a", "interferon-b", "ritonavir", "raltegravir"],
  topts=["리바비린", "인터페론-α", "인터페론-β", "리토나비르", "랄테그라비르"], cols=3)

# =================================================================== 마지막: 시험 직전 한 장
SEC("마무리", "시험 직전 한 장 요약")
S("gp", "FINAL", "시험 직전 한 장 요약 (그람양성균 + 바이러스)",
  '<div class="row c2">' +
  card("그람양성균 Top 12",
       ul(["Clostridium = <b>절대혐기 + 내생포자 + 외독소</b>, 인수공통 X",
           "보툴리눔 = ACh 차단 → <b>이완성·하향성 마비</b>, 꿀(영아), 독소는 열에 약함, 사람 간 전파 X",
           "파상풍 = tetanospasmin → GABA·글리신 차단 → <b>경련·아관긴급</b>, DPT",
           "C. difficile = <b>clindamycin</b> 후 <b>위막성 대장염</b>, 독소 A(장)·B(세포), 원내감염",
           "C. perfringens(=welchii) = CPE 식중독 / β pigbel / <b>α 가스괴저</b>",
           "Veillonella = 입속 <b>젖산</b> → 프로피온산, 충치·치주염",
           "Mycoplasma = <b>세포벽 X</b>, 가장 작음, 콜레스테롤, β-락탐 무효, <b>이형 폐렴</b>",
           "Ureaplasma = 생식기 정상균, <b>비임균성 요도염</b>, 조산·불임",
           "방선균 = 내생포자 X, 무성포자·균사, 옛날엔 곰팡이",
           "Actinomyces israelii = 방선균증(농양), 어금니 집락 / Nocardia = 기회 폐렴",
           "디프테리아 = <b>외독소</b>, 인후 <b>위막</b>, 이염성 과립, 심근염, DTaP",
           "결핵(Mycobacteriaceae) · <i>M. bovis</i> 인수공통 · <i>M. leprae</i> 배양 불가 / Streptomyces·Micromonospora = 항생제"]), "soft") +
  card("바이러스 Top 14",
       ul(["protomer &lt; capsomer &lt; capsid / 외피 = 에테르에 약함", "프리온 = 단백질만, 잠복 김, CJD·광우병, 치료 X",
           "볼티모어: 모두 (+)mRNA로 / DNA = 헤·아·폭·파·파·헤파", "폭스 = <b>세포질 복제 DNA</b>, 천연두(생백신, 1980 박멸, Guarnieri)",
           "아데노 = 외피 X 최대, 각결막염, 백신·약 X, 유전자치료 벡터", "헤르페스 = 잠복(HSV-1 3차/HSV-2 엉치/VZV 후근), <b>acyclovir</b>(TK)",
           "CMV = 부엉이 눈, 선천 감염, ganciclovir / EBV-버킷 / KSHV-카포시", "HPV = E6·E7 → p53·pRb 억제, 16·18 자궁경부암, Gardasil",
           "로타 = dsRNA 분절, 아기 설사, 경구 백신 / 노로 = 겨울, 굴, 배양 X", "피코르나: 폴리오(Sabin 경구 생·Salk 주사 사), 리노 33~35℃, HAV",
           "플라비: 일본뇌염(Culex·돼지·사백신), 황열·뎅기·지카(Aedes), HCV(만성→간암, IFN+ribavirin)", "파라믹소: 홍역(Koplik), 볼거리, RSV(palivizumab) → MMR 생백신",
           "랍도: 광견병(Negri, 공수병) / 번야: 한타(이호왕, 쥐, 신증후출혈열) / 인플루엔자: 8분절·핵 복제·drift vs shift·NA(-amivir)·M2(amantadine)",
           "레트로: (+)RNA×2, 역전사, provirus, CD4, NRTI·NNRTI·PI(-navir) / HBV: DNA인데 역전사, Dane 입자, 영아 만성 90%"]), "") +
  '</div>')
