# -*- coding: utf-8 -*-
"""PART 4 — 23장-2 강의자료에서 새로 나온 것: 의약품 합성 빈칸 2개 (슬라이드 21·31) + 과제 5문제 (슬라이드 44–45)."""
from parts import *
from textbook import hw, qimg, I

P = P4


def lec(id, slide, title, kind, ko, a, exp, figure):
    return dict(t="q", id=id, toc=title, badge="강의", num=f"슬{slide}", part=P, kind=kind,
                src=f"강의자료 슬라이드 {slide} (23장-2 새 슬라이드)", title=title,
                q=qimg(id) + f'<div class="term" style="margin-top:6px">{ko}</div>',
                a=a, exp=exp, extra='<div class="xsec">⚗️ 빈칸 정답 그림</div><div class="mz">' + figure + '</div>', rec=True)


def ssp(n, title):
    """해설집 메커니즘 전용 쪽 (그림이 길어서 두 칸으로)."""
    return dict(t="r", id=f"ssp{n}", cls="ssp", html=f'''<div class="h21"><div class="b21"><span>해설집</span><b>23.{n}</b></div><div class="tt"><h1>과제 23-{n} — {title} · 해설집 메커니즘 전체</h1><div class="sb">OpenStax 10판 해설집(SSM) 23.{n} 그대로 · 왼쪽 → 오른쪽 순서</div></div><div class="pills"><span class="pill">{P}</span></div></div>
<div class="sscols"><img src="{I}ss{n:02d}a.jpg"><img src="{I}ss{n:02d}b.jpg"></div>''')


E = [
lec("lip", 21, "리피토(아토르바스타틴) — 알돌 빈칸", ["bl", "draw"],
    "빈칸(알데하이드 3)을 그리시오. ① c-Hex₂BCl·TEA 단계가 만드는 것은? ② 4와 3 사이 새 C–C 결합은 어디이며, 이 반응의 이름은?<br>(상품명 리피토 · 고콜레스테롤혈증 · HMG-CoA 환원효소 억제 · 1996년 FDA 승인)",
    "빈칸 3 = 피롤 N–CH₂CH₂–<b>CHO</b> (알데하이드) · ① 메틸 케톤 4의 CH₃ 쪽 <b>보론 엔올레이트</b> · ② 케톤 α 탄소(CH₃였던 탄소) – 알데하이드 C=O 탄소 → <b>(혼합) 알돌 반응</b> → β-하이드록시 케톤 5",
    "<p>5에서 새 C–C 결합을 찾는다: C=O 옆 CH₂(α) – CH(OH)(β). β 탄소의 –OH는 원래 받개의 C=O 산소 → 그 탄소가 <b>CHO</b>였다. 주개는 메틸 케톤 4의 α 탄소.</p><p>NaOH 대신 c-Hex₂BCl + Et₃N로 엔올레이트를 먼저 만들고 −78 °C에서 알데하이드를 넣는 이유: 자기 축합 없이 원하는 짝끼리만, 탈수 없이 알돌(β-OH)에서 멈추게. 이후 4단계 → 락톤 8 → NaOH, H₂O로 고리 열기 → 9.</p>",
    MS(21)),
lec("ada", 31, "아다그라십(크라자티) — β-케토 에스터 1 빈칸 3개", ["bl", "mech"],
    "빈칸 3개(①·③ 생성물, ② 시약)를 채우시오. 마지막 LiHMDS 단계는 어떤 반응인가?<br>(아다그라십 · KRAS G12C 표적 항암제 · 2022년 FDA 승인)",
    "① Ar–NH–CH₂CH₂CH₂–CO₂CH₃ (S<sub>N</sub>2 N-알킬화) · ② X–CH₂–CO–모르폴린 (2-할로아세틸 모르폴린) · ③ 고리형 β-케토 에스터 1 — LiHMDS = <b>분자 내 클라이젠(디크만형)</b>, 모르폴린 이탈",
    "<p>① 1차 아릴아민 N이 1° 브로마이드를 S<sub>N</sub>2 (NaHCO₃가 HBr 중화). ② 다음 구조에서 N에 새로 붙은 –CH₂CO–모르폴린 → 할로아세틸 아마이드로 두 번째 S<sub>N</sub>2. ③ LiHMDS가 에스터 α-H(pKa 25)를 떼어 엔올레이트 → 같은 분자의 아마이드 C=O 공격 → 6원 고리 사면체 → 모르폴린 이탈 → β-케토 에스터 (엔올형으로 그려짐).</p><p>디크만과 차이: 받개가 에스터가 아니라 <b>아마이드</b>(이탈기 = 모르폴린).</p>",
    MS(31)),
hw(29, "디크만 · 클라이젠 생성물과 메커니즘", ["prod", "mech"],
   "다음 반응의 생성물을 예측하고 메커니즘을 제시하시오. (a) 다이에틸 4-메틸헵탄다이오에이트 — 1. NaOCH₂CH₃ 2. H₃O⁺ (b) 메틸 페닐아세테이트 — 1. NaOCH₃ 2. H₃O⁺",
   "(a) 에틸 5-메틸-2-옥소사이클로헥세인카복실레이트 (디크만, 6원) · (b) PhCH₂CO–CH(Ph)–CO₂CH₃ (클라이젠)",
   "<p>(a) 1,7-다이에스터 → 6원 고리 (문제 23-14와 같은 화합물). ① EtO⁻가 α-H 제거 ② 엔올레이트 → 반대쪽 에스터 C=O ③ 사면체 → EtO⁻ 이탈 ④ 두 C=O 사이 H 제거(평형 끌어당김) ⑤ H₃O⁺.</p><p>(b) 메틸 에스터라 <b>NaOCH₃</b>. 공식 R–CH₂–CO–CH(R)–CO₂CH₃, R = Ph.</p>",
   extra='<div class="xsec">⚗️ 생성물</div><div class="mz">' + RX(('t', '(a)'), ('m', 'CCOC(=O)CCC(C)CCC(=O)OCC', 150, 50), ('a', '1. NaOEt', '2. H₃O⁺'), ('m', 'CCOC(=O)C1CC(C)CCC1=O', 95, 70), ('t', '(b)'), ('m', 'COC(=O)Cc1ccccc1', 85, 55), ('a', '1. NaOCH₃', '2. H₃O⁺'), ('m', 'COC(=O)C(c1ccccc1)C(=O)Cc1ccccc1', 115, 85)) + '</div>',
   ),
hw(30, "마이클 생성물과 메커니즘", ["prod", "mech"],
   "다음 반응의 생성물을 예측하고 메커니즘을 제시하시오. (a) 3-펜텐-2-온 + 에틸 사이아노아세테이트 (b) 에틸 프로페노에이트 + 에틸 아세토아세테이트 — 각각 1. NaOCH₂CH₃ 2. H₃O⁺",
   "(a) EtO₂C–CH(CN)–CH(CH₃)–CH₂–COCH₃ · (b) CH₃CO–CH(CO₂Et)–CH₂CH₂–CO₂Et",
   "<p>주개 = 두 EWG 사이 CH₂ (NC–CH₂–CO₂Et, CH₃CO–CH₂–CO₂Et) → EtO⁻가 그 H를 떼어 안정한 엔올레이트. 받개의 <b>β 탄소</b>(C=O에서 두 번째 탄소, (a)는 CH₃가 붙은 탄소) 공격 → 새 엔올레이트 → EtOH에서 H⁺ → 1,5-다이카르보닐.</p>",
   extra='<div class="xsec">⚗️ 생성물</div><div class="mz">' + RX(('t', '(a)'), ('m', 'C/C=C/C(C)=O', 60, 45), ('t', '+'), ('m', 'CCOC(=O)CC#N', 75, 45), ('a', 'NaOEt', 'H₃O⁺'), ('m', 'CCOC(=O)C(C#N)C(C)CC(C)=O', 110, 70))
   + RX(('t', '(b)'), ('m', 'C=CC(=O)OCC', 65, 45), ('t', '+'), ('m', 'CCOC(=O)CC(C)=O', 75, 45), ('a', 'NaOEt', 'H₃O⁺'), ('m', 'CCOC(=O)CCC(C(C)=O)C(=O)OCC', 110, 70)) + '</div>',
   ),
hw(31, "엔아민(스토크) 생성물과 메커니즘", ["prod", "mech"],
   "다음 반응의 생성물을 예측하고 메커니즘을 제시하시오. (a) 2-뷰텐알 + 2-뷰탄온의 다이메틸 엔아민 (b) 메틸 프로페노에이트 + 1-피롤리디노사이클로헥센 — 각각 1. THF 2. H₃O⁺",
   "(a) CH₃CO–CH(CH₃)–CH(CH₃)–CH₂–CHO + (CH₃)₂NH · (b) 메틸 3-(2-옥소사이클로헥실)프로파노에이트 + 피롤리딘",
   "<p>① N 전자쌍이 내려오며 엔아민 α 탄소가 받개 β 탄소 공격 → 이미늄 + 엔올레이트 ② 엔올레이트 양성자화 ③ H₂O가 C=N⁺ 공격 → 양성자 이동 → 2차 아민 이탈 → C=O 회복. (a) 받개 2-뷰텐알의 β 탄소에 CH₃ → 가지 두 개.</p>",
   extra='<div class="xsec">⚗️ 생성물</div><div class="mz">' + RX(('t', '(a)'), ('m', 'C/C=C/C=O', 55, 40), ('t', '+'), ('m', 'C/C=C(\\C)N(C)C', 65, 50), ('a', '1. THF', '2. H₃O⁺'), ('m', 'CC(=O)C(C)C(C)CC=O', 95, 55))
   + RX(('t', '(b)'), ('m', 'C=CC(=O)OC', 55, 40), ('t', '+'), ('m', 'C1=C(N2CCCC2)CCCC1', 75, 55), ('a', '1. THF', '2. H₃O⁺'), ('m', 'COC(=O)CCC1CCCCC1=O', 105, 60)) + '</div>',
   ),
hw(69, "빠진 시약 a–h — 반응 사다리", ["reag"],
   "다음 경로의 빠진 시약 a–h를 채우시오. (사이클로헥사논 → 사이클로헥센 → 다이에틸 헥산다이오에이트 → 에틸 2-옥소사이클로펜테인카복실레이트 → 2-메틸사이클로펜탄온)",
   "a LiAlH₄, 그다음 H₃O⁺ · b POCl₃, 피리딘 · c KMnO₄, H₃O⁺ · d CH₃CH₂OH, H⁺ · e Na⁺ ⁻OEt · f H₃O⁺ · g Na⁺ ⁻OEt, 그다음 CH₃Br · h H₃O⁺, 가열",
   "<p>a·b: 케톤 → 알코올(환원) → 탈수(알켄). c·d: C=C 산화 절단 → 아디프산 → 피셔 에스터화. e·f: <b>디크만</b>(1,6-다이에스터 → 5원). g·h: 두 C=O 사이 α 탄소 <b>알킬화</b> → <b>가수분해·탈카르복실화</b> (22장 아세토아세트산 에스터 합성과 같은 3단계). 22장 과제 22-54와 같은 형식.</p>",
   extra='<div class="xsec">⚗️ 전체 흐름</div><div class="mz">' + RX(('m', 'O=C1CCCCC1', 50, 45), ('a', 'a, b', ''), ('m', 'C1=CCCCC1', 50, 45), ('a', 'c, d', ''), ('m', 'CCOC(=O)CCCCC(=O)OCC', 120, 40), ('a', 'e, f', '디크만'), ('m', 'CCOC(=O)C1CCCC1=O', 70, 55), ('a', 'g, h', '알킬화 · −CO₂'), ('m', 'CC1CCCC1=O', 55, 50)) + '</div>'),
hw(70, "사이클로헥사논에서 4가지 만들기", ["reag"],
   "다음 화합물을 사이클로헥사논에서 어떻게 만들겠는가? (a) 2,6-다이벤질리덴사이클로헥사논 (b) 3-(2-옥소사이클로헥실)프로판나이트릴 (c) 2-알릴사이클로헥사논 (d) 에틸 2-옥소-2-(2-옥소사이클로헥실)아세테이트",
   "(a) 2 PhCHO, 1. NaOH, EtOH 2. 가열 (혼합 알돌 ×2) · (b) 피롤리딘 → 1. CH₂=CHCN 2. H₃O⁺ (스토크) · (c) 1. LDA 2. BrCH₂CH=CH₂ · (d) EtO₂C–CO₂Et, 1. NaOEt 2. H₃O⁺ (혼합 클라이젠)",
   "<p>생성물에서 새 결합을 찾아 반응을 고른다: (a) C=CHPh 두 개 = α-H 없는 벤즈알데하이드와 알돌 축합 양쪽 (b) α에 –CH₂CH₂CN = 받개 아크릴로나이트릴의 1,4-첨가 → 단일 케톤이라 엔아민 (c) α에 알릴 = S<sub>N</sub>2 알킬화 (LDA) (d) α에 –CO–CO₂Et = α-H 없는 옥살레이트를 받개로 한 혼합 클라이젠.</p>"),
]
