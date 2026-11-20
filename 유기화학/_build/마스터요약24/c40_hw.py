# -*- coding: utf-8 -*-
"""PART 4 — 과제 4문제 (CH24_2 강의자료 슬라이드 55–56). 물음표마다 구조를 모두 그림 (A·B·C 중간체 포함)."""
from parts import *
from textbook import hw

P = P4

def F(*rows):
    return '<div class="xsec">⚗️ 생성물 · 중간체</div><div class="mz">' + "".join(rows) + '</div>'

E = [
hw(32, "호프만 자리옮김 생성물과 메커니즘", ["prod", "mech"],
   "다음 반응의 생성물을 예측하고 메커니즘을 쓰시오. (a) 3-메틸뷰탄아마이드 —Br₂, NaOH, H₂O→ ? (b) 사이클로펜테인카복스아마이드 —Br₂, NaOH, H₂O→ ?",
   "(a) (CH₃)₂CHCH₂NH₂ (아이소뷰틸아민) + CO₂ (b) 사이클로펜틸아민 + CO₂",
   "<p>① OH⁻가 N–H 제거 → N⁻ ② Br₂ → N-브로모아마이드 ③ 남은 N–H 제거 ④ <b>R 이동 + Br⁻ 이탈</b> → 아이소사이아네이트 R–N=C=O ⑤ OH⁻/H₂O → 카밤산 ⑥ −CO₂ → R–NH₂. 생성 아민은 탄소 1개 적다. (해설집에는 (c)(d)도 있으나 과제는 (a)(b))</p>",
   extra=F(RX(('t', '(a)'), ('m', 'CC(C)CC(N)=O', 75, 45), ('a', 'Br₂, NaOH', 'H₂O'), ('m', 'CC(C)CN=C=O', 80, 40), ('t', '아이소사이아네이트'), ('a', 'H₂O', '−CO₂'), ('m', 'CC(C)CN', 55, 40)),
           RX(('t', '(b)'), ('m', 'NC(=O)C1CCCC1', 65, 50), ('a', 'Br₂, NaOH', 'H₂O'), ('m', 'O=C=NC1CCCC1', 70, 45), ('a', 'H₂O', '−CO₂'), ('m', 'NC1CCCC1', 50, 45)))),
hw(33, "커티어스 자리옮김 생성물과 메커니즘", ["prod", "mech"],
   "다음 반응의 생성물을 예측하고 메커니즘을 쓰시오. (a) 데칼린 고리 접합부의 산 염화물 —1. NaN₃ 2. H₂O, 가열→ ? (b) 3-뷰텐오일 클로라이드 —1. NaN₃ 2. H₂O, 가열→ ?",
   "(a) 고리 접합부 탄소에 –NH₂ (입체 배치 유지) + N₂ + CO₂ (b) CH₂=CHCH₂NH₂ (알릴아민) + N₂ + CO₂",
   "<p>① N₃⁻가 산 염화물에 아실 치환 → 아실 아자이드 ② 가열: <b>R 이동 + N₂ 이탈</b> → 아이소사이아네이트 ③ H₂O → 카밤산 → −CO₂ → 아민. 이동하는 R의 입체 배치는 그대로.</p>",
   extra=F(RX(('t', '(a)'), ('m', 'O=C(Cl)C12CCCCC1CCCC2', 75, 55), ('a', 'NaN₃', ''), ('m', '[N-]=[N+]=NC(=O)C12CCCCC1CCCC2', 90, 55), ('a', 'Δ', '−N₂'), ('m', 'O=C=NC12CCCCC1CCCC2', 80, 55), ('a', 'H₂O', '−CO₂'), ('m', 'NC12CCCCC1CCCC2', 65, 55)),
           RX(('t', '(b)'), ('m', 'C=CCC(=O)Cl', 60, 40), ('a', 'NaN₃', ''), ('m', 'C=CCC(=O)N=[N+]=[N-]', 85, 40), ('a', 'Δ', '−N₂'), ('m', 'C=CCN=C=O', 65, 35), ('a', 'H₂O', '−CO₂'), ('m', 'C=CCN', 45, 35)))),
hw(63, "톨루엔에서 3가지 합성", ["reag"],
   "다음 화합물을 톨루엔에서 어떻게 만들겠는가? 일부는 다이아조니오 치환 반응이 필요하다. (a) p-메틸아닐린 (b) p-메틸벤질아민 (c) 메틸 m-아이오도벤조에이트",
   "(a) HNO₃/H₂SO₄ → H₂, Pt (b) (a) → HNO₂/H₂SO₄ → CuCN → 1. LiAlH₄ 2. H₂O (c) KMnO₄, H₂O → HNO₃/H₂SO₄ → 1. SnCl₂, H₃O⁺ 2. NaOH → HNO₂/H₂SO₄ → NaI → CH₃OH, H⁺",
   "<p>(b) –CH₂NH₂ = –CN을 환원 → –CN은 다이아조늄 + CuCN으로만. (c) –CO₂CH₃와 I가 <b>메타</b> → –COOH(메타 지향) 상태에서 나이트로화. 에스터화는 마지막(피셔).</p>",
   extra=F(RX(('t', '(a)'), ('m', 'Cc1ccccc1', 45, 40), ('a', 'HNO₃', 'H₂SO₄'), ('m', 'Cc1ccc([N+](=O)[O-])cc1', 70, 45), ('a', 'H₂, Pt', 'EtOH'), ('m', 'Cc1ccc(N)cc1', 60, 40)),
           RX(('t', '(b)'), ('m', 'Cc1ccc(N)cc1', 55, 40), ('a', 'HNO₂', 'H₂SO₄'), ('m', 'Cc1ccc([N+]#N)cc1', 70, 40), ('a', 'CuCN', ''), ('m', 'Cc1ccc(C#N)cc1', 65, 40), ('a', '1. LiAlH₄', '2. H₂O'), ('m', 'Cc1ccc(CN)cc1', 65, 40)),
           RX(('t', '(c)'), ('m', 'Cc1ccccc1', 45, 40), ('a', 'KMnO₄', ''), ('m', 'OC(=O)c1ccccc1', 55, 40), ('a', 'HNO₃', '(메타)'), ('m', 'OC(=O)c1cccc([N+](=O)[O-])c1', 75, 45), ('a', 'SnCl₂', 'NaOH'), ('m', 'OC(=O)c1cccc(N)c1', 65, 45)),
           RX(('t', '　'), ('a', 'HNO₂', 'H₂SO₄'), ('m', 'OC(=O)c1cccc([N+]#N)c1', 75, 45), ('a', 'NaI', ''), ('m', 'OC(=O)c1cccc(I)c1', 65, 45), ('a', 'CH₃OH', 'H⁺'), ('m', 'COC(=O)c1cccc(I)c1', 70, 45)))),
hw(64, "A → B → C 예측", ["prod", "int"],
   "다음 반응의 생성물을 예측하시오. 생성물이 둘 이상이면 주생성물을 표시하시오. (a) 데카하이드로퀴놀린 —CH₃I(과량)→ A —Ag₂O, H₂O→ B —가열→ C (b) 벤조일 클로라이드 —NaN₃→ A —가열→ B —H₂O→ C (c) 프탈이미드 —KOH→ A —C₆H₅CH₂Br→ B —KOH, H₂O→ C (d) BrCH₂CH₂CH₂CH₂Br + CH₃NH₂ 1당량 —NaOH, H₂O→ ?",
   "(a) A 4차 암모늄 아이오다이드 · B 4차 암모늄 수산화물 · C 고리 열린 알켄 아민 (주: 말단 C=C) (b) A 벤조일 아자이드 · B 페닐 아이소사이아네이트 · C 아닐린 (c) A 프탈이미드 K⁺ · B N-벤질프탈이미드 · C 벤질아민 (d) N-메틸피롤리딘",
   "<p>(a) 호프만 제거 — 고리 N이라 E2 후 고리가 열림, 덜 치환된 말단 쪽이 주 (해설집: 고리 안 C=C 두 가지는 부). (b) 커티어스 (+ N₂, CO₂). (c) 가브리엘. (d) S<sub>N</sub>2 두 번: 분자 간 → 분자 내 고리(5원).</p>",
   extra=F(RX(('t', '(a)'), ('m', 'C1CCC2NCCCC2C1', 55, 45), ('a', 'CH₃I', '과량'), ('m', 'C[N+]1(C)CCCC2CCCCC21.[I-]', 75, 55), ('t', 'A'), ('a', 'Ag₂O', 'H₂O'), ('m', 'C[N+]1(C)CCCC2CCCCC21.[OH-]', 75, 55), ('t', 'B'), ('a', 'Δ', 'E2'), ('m', 'C=CCC1CCCCC1N(C)C', 75, 55), ('t', 'C (주)')),
           RX(('t', '(b)'), ('m', 'O=C(Cl)c1ccccc1', 55, 45), ('a', 'NaN₃', ''), ('m', '[N-]=[N+]=NC(=O)c1ccccc1', 85, 45), ('t', 'A'), ('a', 'Δ', '−N₂'), ('m', 'O=C=Nc1ccccc1', 70, 40), ('t', 'B'), ('a', 'H₂O', '−CO₂'), ('m', 'Nc1ccccc1', 45, 40), ('t', 'C')),
           RX(('t', '(c)'), ('m', 'O=C1NC(=O)c2ccccc21', 60, 45), ('a', 'KOH', ''), ('m', 'O=C1[N-]C(=O)c2ccccc21.[K+]', 70, 45), ('t', 'A'), ('a', 'PhCH₂Br', ''), ('m', 'O=C1N(Cc3ccccc3)C(=O)c2ccccc21', 85, 50), ('t', 'B'), ('a', 'KOH', 'H₂O'), ('m', 'NCc1ccccc1', 55, 40), ('t', 'C')),
           RX(('t', '(d)'), ('m', 'BrCCCCBr', 65, 35), ('t', '+ CH₃NH₂'), ('a', 'NaOH', 'S<sub>N</sub>2 ×2'), ('m', 'CN1CCCC1', 45, 40))) + '<p class="nt">(a) 부생성물: 고리 안 C=C 두 가지.</p>'),
]
