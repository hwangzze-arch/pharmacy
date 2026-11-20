# -*- coding: utf-8 -*-
"""CH24 과제(24-32·33·63·64) 손글씨 제출용 간단 풀이 → 유기화학/CH24_과제_손글씨용_풀이.pdf"""
import os, sys
D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(D, "..", "강의번역24"))
from fig import row as RX
from mech import MECH_CSS
from mechs import HOF, CUR
IMG = "../마스터요약24/img/"

def page(num, title, img, ans, body, tip, qh="42mm"):
    return f'''<section class="page" style="--qh:{qh}"><header><span class="no">과제 {num}</span><h1>{title}</h1></header>
<div class="q"><img src="{IMG}{img}.jpg"></div>
<div class="sec">✏️ 정답 (구조)</div><div class="ans">{ans}</div>
{body}
<div class="tip"><b>손글씨 요령</b> {tip}</div></section>'''

P = []
P.append(page("24-32", "호프만 자리옮김 — 생성물 + 메커니즘", "hw32",
  RX(('t', '(a)'), ('m', 'CC(C)CC(N)=O', 80, 50), ('a', 'Br₂, NaOH', 'H₂O'), ('m', 'CC(C)CN', 65, 45), ('t', '+ CO₂'))
  + RX(('t', '(b)'), ('m', 'NC(=O)C1CCCC1', 70, 55), ('a', 'Br₂, NaOH', 'H₂O'), ('m', 'NC1CCCC1', 55, 50), ('t', '+ CO₂')),
  '<div class="sec">✏️ 메커니즘 (R로 한 번만) — (a) R = (CH₃)₂CHCH₂–  (b) R = 사이클로펜틸</div><div class="mz">' + "".join(HOF) + '</div>',
  "(a)(b)는 R만 다르고 단계가 같다 → 메커니즘은 <b>R로 한 번</b> 그리고 아래에 R이 무엇인지만 적기. "
  "꼭 써야 할 것: ① N–H 떼기 ② N–Br 만들기 ③ 또 N–H 떼기 ④ <b>R 이동 + Br⁻ 이탈</b> → R–N=C=O ⑤ 물 첨가 → 카밤산 ⑥ −CO₂. 탄소 1개 줄어든 아민."))
P.append(page("24-33", "커티어스 자리옮김 — 생성물 + 메커니즘", "hw33",
  RX(('t', '(a)'), ('m', 'O=C(Cl)[C@@]12CCCC[C@@]1([H])CCCC2', 85, 60), ('a', '1. NaN₃', '2. H₂O, Δ'), ('m', 'N[C@@]12CCCC[C@@]1([H])CCCC2', 80, 65), ('t', '+ N₂ + CO₂ (트랜스 그대로)'))
  + RX(('t', '(b)'), ('m', 'C=CCC(=O)Cl', 65, 45), ('a', '1. NaN₃', '2. H₂O, Δ'), ('m', 'C=CCN', 50, 40), ('t', '+ N₂ + CO₂')),
  '<div class="sec">✏️ 메커니즘 (R로 한 번만) — (a) R = 데칼린 고리 접합부  (b) R = CH₂=CHCH₂–</div><div class="mz">' + "".join(CUR) + '</div>',
  "꼭 써야 할 것: ① N₃⁻가 C=O 탄소 공격, Cl⁻ 이탈 → 아실 아자이드 ② 가열: <b>R 이동 + N₂ 이탈</b> → R–N=C=O ③ 물 첨가 → 카밤산 → −CO₂. "
  "(a)는 R이 이동해도 <b>입체 배치 유지</b>라고 한 줄."))
P.append(page("24-63", "톨루엔에서 3가지 합성 (시약만)", "hw63",
  RX(('t', '(a)'), ('m', 'Cc1ccccc1', 45, 40), ('a', 'HNO₃', 'H₂SO₄'), ('m', 'Cc1ccc([N+](=O)[O-])cc1', 75, 45), ('a', 'H₂, Pt', ''), ('m', 'Cc1ccc(N)cc1', 60, 40))
  + RX(('t', '(b)'), ('m', 'Cc1ccc(N)cc1', 55, 40), ('a', 'HNO₂', 'H₂SO₄'), ('m', 'Cc1ccc([N+]#N)cc1', 75, 40), ('a', 'CuCN', ''), ('m', 'Cc1ccc(C#N)cc1', 65, 40), ('a', '1. LiAlH₄', '2. H₂O'), ('m', 'Cc1ccc(CN)cc1', 65, 40))
  + RX(('t', '(c)'), ('m', 'Cc1ccccc1', 45, 40), ('a', 'KMnO₄', ''), ('m', 'OC(=O)c1ccccc1', 55, 40), ('a', 'HNO₃', 'H₂SO₄'), ('m', 'OC(=O)c1cccc([N+](=O)[O-])c1', 75, 45), ('a', '1. SnCl₂, H₃O⁺', '2. NaOH'), ('m', 'OC(=O)c1cccc(N)c1', 65, 45))
  + RX(('t', ''), ('a', 'HNO₂', 'H₂SO₄'), ('m', 'OC(=O)c1cccc([N+]#N)c1', 80, 45), ('a', 'NaI', ''), ('m', 'OC(=O)c1cccc(I)c1', 65, 45), ('a', 'CH₃OH', 'H⁺'), ('m', 'COC(=O)c1cccc(I)c1', 70, 45)),
  "", "메커니즘은 묻지 않음 → <b>구조 + 화살표 위 시약</b>만. (b) –CH₂NH₂는 –CN 환원 → –CN은 다이아조늄 + CuCN. "
  "(c) –COOH가 메타 지향이라 <b>먼저 산화</b> 후 나이트로화, 에스터화는 마지막."))
P.append(page("24-64", "A → B → C 예측", "hw64",
  RX(('t', '(a)'), ('m', 'C1CCC2NCCCC2C1', 55, 45), ('a', 'CH₃I', '과량'), ('m', 'C[N+]1(C)CCCC2CCCCC21.[I-]', 75, 55), ('t', 'A'), ('a', 'Ag₂O', 'H₂O'), ('m', 'C[N+]1(C)CCCC2CCCCC21.[OH-]', 75, 55), ('t', 'B'), ('a', 'Δ', ''), ('m', 'C=CCC1CCCCC1N(C)C', 75, 55), ('t', 'C (주)'))
  + RX(('t', '(b)'), ('m', 'O=C(Cl)c1ccccc1', 55, 45), ('a', 'NaN₃', ''), ('m', '[N-]=[N+]=NC(=O)c1ccccc1', 75, 45), ('t', 'A'), ('a', 'Δ', '−N₂'), ('m', 'O=C=Nc1ccccc1', 85, 45), ('t', 'B'), ('a', 'H₂O', '−CO₂'), ('m', 'Nc1ccccc1', 45, 40), ('t', 'C'))
  + RX(('t', '(c)'), ('m', 'O=C1NC(=O)c2ccccc21', 60, 45), ('a', 'KOH', ''), ('m', 'O=C1[N-]C(=O)c2ccccc21.[K+]', 70, 45), ('t', 'A'), ('a', 'PhCH₂Br', ''), ('m', 'O=C1N(Cc3ccccc3)C(=O)c2ccccc21', 85, 50), ('t', 'B'), ('a', 'KOH', 'H₂O'), ('m', 'NCc1ccccc1', 55, 40), ('t', 'C'))
  + RX(('t', '(d)'), ('m', 'BrCCCCBr', 65, 35), ('t', '+ CH₃NH₂ (1당량)'), ('a', 'NaOH', 'H₂O'), ('m', 'CN1CCCC1', 45, 40)),
  "", "A·B·C를 <b>전부 구조로</b>. (a) 호프만 제거: 덜 치환된 쪽 C=C가 주생성물(고리 안 C=C 두 가지는 부, ‘부생성물’이라고만 적어도 됨). "
  "(b) 커티어스 (c) 가브리엘 (d) S<sub>N</sub>2 두 번 → 5원 고리.", qh="75mm"))

CSS = MECH_CSS + """
@page{size:A4 landscape;margin:0}
*{box-sizing:border-box} body{margin:0;font-family:'Noto Sans KR','Noto Sans CJK KR',sans-serif;color:#222;background:#fff}
.page{width:297mm;height:210mm;padding:9mm 12mm;page-break-after:always;overflow:hidden;display:flex;flex-direction:column;gap:5px}
header{display:flex;align-items:center;gap:10px;border-bottom:2.5px solid #7048e8;padding-bottom:5px}
header .no{background:#f76707;color:#fff;font-weight:700;border-radius:6px;padding:2px 10px}
h1{font-size:20px;margin:0;color:#5f3dc4}
.q img{max-height:var(--qh,42mm);max-width:100%;display:block}
.sec{font-weight:700;color:#5f3dc4;font-size:13px;margin-top:3px}
.ans .rx,.mz .mrow{zoom:1.25}
.rx{display:flex;align-items:center;flex-wrap:nowrap;gap:2px;margin:1px 0}
.rx .mol svg{display:block} .rx .tx{font-size:11px;padding:0 3px;white-space:nowrap}
.arw{display:inline-flex;flex-direction:column;align-items:center;min-width:60px;font-size:9.5px;line-height:1.2;color:#1f3f66;padding:0 3px;white-space:nowrap}
.arw .al{display:block;width:100%;height:0;border-top:1.1px solid #333;position:relative;margin:2px 0}
.arw .al::after{content:'';position:absolute;right:-1px;top:-4.6px;border-left:7px solid #333;border-top:4px solid transparent;border-bottom:4px solid transparent}
.stp .al{border-top-width:1.1px}
.tip{margin-top:auto;background:#ebfbee;border-left:4px solid #40c057;padding:6px 10px;font-size:12.5px;line-height:1.55;border-radius:4px}
.tip b:first-child{color:#2b8a3e;margin-right:6px}
"""
open(os.path.join(D, "index.html"), "w").write(f'<!doctype html><meta charset="utf-8"><style>{CSS}</style>' + "".join(P))
