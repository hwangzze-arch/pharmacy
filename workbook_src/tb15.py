# -*- coding: utf-8 -*-
"""15장 테스트뱅크 (lehninger6e_tb_ch15) — 49문제 모두 강의 범위."""
from helpers import *
from tblib import mcq, ans, sa
from exam15 import mm_curve, f26bp_switch, glycogen_tree, steady_state, amp_bars, mca_bars
from ch15 import cascade

TB = []


def add(**kw):
    kw.setdefault('kind', 'MC')
    TB.append(kw)


def bypass_table():
    return table(['해당 (비가역)', '당신생 우회 효소'], [['① 헥소키나아제', 'G6Pase'], ['③ PFK-1', 'FBPase-1'], ['⑩ 피루브산 키나아제', '피루브산 카복실화효소 + PEPCK']])


def futile():
    return align([('F6P + ATP', '→ F1,6BP + ADP', '(PFK-1)'), ('F1,6BP + H₂O', '→ F6P + Pᵢ', '(FBPase-1)'), ('합계', 'ATP + H₂O → ADP + Pᵢ + <b>열</b>', '')])


def gly_syn():
    return vflow(['포도당 + ATP → G6P (헥소키나아제)', 'G6P ⇌ G1P (포스포글루코뮤테이스)', 'G1P + UTP → UDP-포도당 + PPᵢ (UDP-포도당 피로포스포릴레이스)',
                  'UDP-포도당 + 글리코겐(n) → 글리코겐(n+1) + UDP (글리코겐 합성효소, α1→4)', '가지형성 효소 → (α1→6) 가지'],
                 colors=[C['navy'], C['navy'], C['orange'], C['green'], C['purple']], box_h=24, gap=12, width=540, font=10.5, bw=510)


# ================================================================ S1 (0) 상반 조절
add(n=11, sec=0, diff=2, title='당신생이 우회하는 세 효소',
    en=mcq('Gluconeogenesis must use “bypass reactions” to circumvent three reactions in the glycolytic pathway that are highly exergonic and essentially irreversible. Which three must be bypassed?<br>1) Hexokinase 2) Phosphoglycerate kinase 3) Phosphofructokinase-1 4) Pyruvate kinase 5) Triosephosphate isomerase', ['1, 2, 3', '1, 2, 4', '1, 4, 5', '1, 3, 4', '2, 3, 4']),
    ko=mcq('당신생이 우회해야 하는 해당과정의 비가역 반응 세 개는? 1) 헥소키나아제 2) PGK 3) PFK-1 4) 피루브산 키나아제 5) TPI', ['1, 2, 3', '1, 2, 4', '1, 4, 5', '<b>1, 3, 4</b>', '2, 3, 4']),
    answer=ans('D', '1, 3, 4', '헥소키나아제 · PFK-1 · 피루브산 키나아제'),
    explain=bypass_table() + key('ΔG가 크게 음수인 ①③⑩만 우회. PGK·TPI는 가역이라 공유.'))

add(n=34, sec=0, diff=2, kind='SA', title='비가역 3단계와 우회 · 경로를 나눈 장단점',
    en='<p>In the glycolytic path from glucose to pyruvate, three steps are practically irreversible. What are these steps, and how is each bypassed in gluconeogenesis? What advantages does an organism gain from having separate pathways for anabolic and catabolic metabolism? What are the disadvantages?</p>',
    ko='<p>포도당 → 피루브산 경로의 비가역 3단계는? 당신생에서는 각각 어떻게 우회하나? 동화·이화 경로를 따로 두는 장점과 단점은?</p>',
    answer=sa('Hexokinase (bypassed by glucose 6-phosphatase), PFK-1 (by FBPase-1), pyruvate kinase (by pyruvate carboxylase + PEP carboxykinase). Advantage: the two directions can be controlled separately, avoiding futile cycles. Disadvantage: separate sets of enzymes must be made.',
              '헥소키나아제 ↔ G6Pase, PFK-1 ↔ FBPase-1, PK ↔ PC + PEPCK. 장점: 두 방향을 따로 조절 → 헛된 회로 방지. 단점: 효소를 두 벌 만들어야 한다.'),
    explain=bypass_table() + key('“같은 길을 거꾸로 가면 한쪽을 켜면 다른 쪽도 켜진다” → 길을 따로 내서 따로 신호등을 단다.'))

add(n=35, sec=0, diff=3, kind='SA', title='헛된 회로(futile cycle)',
    en='<p>What is a “futile cycle”? Give an example of a potential futile cycle in carbohydrate metabolism, and describe methods used by cells to avoid its operation.</p>',
    ko='<p>“헛된 회로”란? 탄수화물 대사의 예를 들고, 세포가 이를 피하는 방법을 설명하라.</p>',
    answer=sa('A pair of reactions converting A → B and B → A; the net result is ATP hydrolysis and heat. Example: PFK-1 (F6P → F1,6BP) and FBPase-1 (F1,6BP → F6P). Cells use reciprocal regulation: when one is stimulated, the other is inhibited.',
              'A → B와 B → A가 동시에 돌아 ATP만 열로 낭비. 예: PFK-1과 FBPase-1. 방지: <b>상반 조절</b>(한쪽을 켜는 신호가 다른 쪽을 끈다).'),
    explain=futile() + key('예: AMP·F2,6BP → PFK-1 ▲, FBPase-1 ⊗.') + tip('일부러 돌려 열을 내기도 한다(벌의 비행근, 체온 유지).', '참고'))

add(n=49, sec=0, diff=2, kind='SA', title='역방향을 맡는 효소 짝짓기',
    en='<p>For each enzyme on the left, pick the enzyme on the right that carries out the reverse transformation.<br>a) hexokinase b) fructose 1,6-bisphosphatase c) glycogen synthase d) pyruvate kinase<br>1) glycogen phosphorylase 2) pyruvate carboxylase &amp; PEP carboxylase 3) phosphofructokinase-1 4) glucose-6-phosphatase</p>',
    ko='<p>왼쪽 효소의 반대 변환을 하는 오른쪽 효소를 고르라. a) 헥소키나아제 b) FBPase-1 c) 글리코겐 합성효소 d) 피루브산 키나아제 / 1) 글리코겐 인산화효소 2) PC & PEP 카복실화효소 3) PFK-1 4) G6Pase</p>',
    answer=sa('(a)-(4); (b)-(3); (c)-(1); (d)-(2)', 'a–4 · b–3 · c–1 · d–2'),
    explain=table(['정방향', '역방향'], [['헥소키나아제', 'G6Pase'], ['FBPase-1', 'PFK-1'], ['글리코겐 합성효소', '글리코겐 인산화효소'], ['피루브산 키나아제', 'PC + PEPCK']]) +
    warn('보기 2)의 “PEP carboxylase”는 테스트뱅크 오타 — 동물 당신생 효소는 <b>PEP 카복시키나아제(PEPCK)</b>.', '자료 오타'))

# ================================================================ S2 (1) HK
add(n=2, sec=1, diff=2, title='기질 농도 변화에 잘 반응하는 효소의 조건',
    en=mcq('For an enzyme to effectively change its activity in response to a change in substrate concentration, it is most favorable for:', ['Km to be less than cellular substrate concentrations.', 'Km to be equal to cellular substrate concentrations.', 'Km to be greater than cellular substrate concentrations.', 'Vmax to be at the diffusion limit.', 'The substrate to also be an allosteric effector.']),
    ko=mcq('기질 농도 변화에 따라 효소 활성이 효과적으로 바뀌려면 무엇이 가장 유리한가?', ['Km &lt; 세포 속 [S]', 'Km = [S]', 'Km &gt; [S]', 'Vmax가 확산 한계', '<b>기질이 알로스테릭 조절자이기도 할 것</b>']),
    answer=ans('E', 'The substrate to also be an allosteric effector.', '기질이 알로스테릭 효과도 낼 것 (협동성 → S자 곡선)',
               note='⚠️ MCA로 보면 Km ≥ [S](C)도 반응성이 크다(ε ≈ 1). 테스트뱅크 정답은 E — S자 곡선의 가파른 구간에서는 같은 [S] 변화에 활성이 훨씬 크게 바뀐다.'),
    explain=fig(mm_curve(), '') + steps('A(Km ≪ [S]): 이미 포화 → [S]가 바뀌어도 속도 그대로 (HK I).', '협동적(S자) 효소는 문턱 근처에서 스위치처럼 급변 → 가장 민감.') +
    key('간 HK IV(Km ≈ 10 mM, 협동성)가 혈당 센서인 이유.'))

# ================================================================ S4 (3) PFK / F2,6BP
add(n=12, sec=3, diff=2, title='F6P ⇌ F1,6BP 상반 조절 — 틀린 것',
    en=mcq('Reciprocal regulation of glycolytic and gluconeogenic reactions interconverting F6P and F1,6BP. Which statement is not correct?', ['Fructose-2,6-bisphosphate activates phosphofructokinase-1.', 'Fructose-2,6-bisphosphate inhibits fructose-1,6-bisphosphatase.', 'The fructose-1,6-bisphosphatase reaction is exergonic.', 'The phosphofructokinase-1 reaction is endergonic.', 'This regulation allows control of the direction of net metabolite flow through the pathway.']),
    ko=mcq('F6P ⇌ F1,6BP 상반 조절에 대해 틀린 것은?', ['F2,6BP는 PFK-1을 활성화한다', 'F2,6BP는 FBPase-1을 억제한다', 'FBPase-1 반응은 발에르곤이다', '<b>PFK-1 반응은 흡에르곤이다</b>', '이 조절로 알짜 흐름의 방향을 정한다']),
    answer=ans('D', 'The phosphofructokinase-1 reaction is endergonic.', '틀림 — PFK-1 반응은 ATP를 써서 강한 발에르곤(ΔG′° −14.2)'),
    explain=fig(f26bp_switch(), '') + key('두 방향 모두 발에르곤(비가역) → 그래서 둘 다 켜 두면 헛된 회로. 신호로 한쪽만 켠다.'))

add(n=13, sec=3, diff=2, title='PFK-2를 탈인산화해 켜는 것',
    en=mcq('An increase in which of these compounds leads to the dephosphorylation and activation of phosphofructokinase-2?', ['Glucagon', 'Xylulose-5-phosphate', 'Pyruvate', 'Citrate', 'ADP']),
    ko=mcq('증가하면 PFK-2를 탈인산화해 활성화하는 것은?', ['글루카곤', '<b>자일룰로스 5-인산(Xu5P)</b>', '피루브산', '시트르산', 'ADP']),
    answer=ans('B', 'Xylulose-5-phosphate', 'Xu5P → PP2A 활성 → PFK-2 탈인산화'),
    explain=fig(flow(['탄수화물 ↑ → Xu5P ↑', 'PP2A 활성', 'PFK-2 ON → F2,6BP ↑', '해당 ↑'], arrow_labels=['', '탈인산화', ''], colors=[C['orange'], C['green'], C['green'], C['green']], box_h=36, width=540, font=10), '') +
    warn('A(글루카곤)는 반대 — PKA로 <b>인산화</b> → PFK-2 OFF.', '함정'))

add(n=37, sec=3, diff=3, kind='SA', title='PFK-2/FBPase-2 인산화의 결과',
    en='<p>Under what circumstances does the bifunctional protein PFK-2/FBPase-2 become phosphorylated, and what are the consequences for glycolysis and gluconeogenesis?</p>',
    ko='<p>이중기능 효소 PFK-2/FBPase-2는 언제 인산화되며, 그 결과 해당과 당신생은 어떻게 되나?</p>',
    answer=sa('Low blood glucose → glucagon → cAMP → PKA phosphorylates PFK-2/FBPase-2: FBPase-2 ↑, PFK-2 ↓ → [F2,6BP] ↓ → PFK-1 ↓ (glycolysis ↓), FBPase-1 ↑ (gluconeogenesis ↑), so the liver releases glucose.',
              '혈당 ↓ → 글루카곤 → cAMP → PKA가 인산화 → FBPase-2 ON, PFK-2 OFF → F2,6BP ↓ → 해당 ↓, 당신생 ↑ → 간이 혈당 공급.'),
    explain=fig(f26bp_switch(), '') + key('인산화 = FBPase-2 = F2,6BP ↓ = 당신생. 거꾸로 외우지 않기!'))

add(n=36, sec=3, diff=2, kind='SA', title='시트르산이 중요한 조절 분자인 이유',
    en='<p>Why is citrate, in addition to being a metabolic intermediate in aerobic oxidation of fuels, an important control molecule for a variety of enzymes?</p>',
    ko='<p>시트르산은 대사 중간체일 뿐 아니라 여러 효소의 중요한 조절 분자다. 왜인가?</p>',
    answer=sa('Citrate sits at the junction of carbohydrate, fatty acid, and amino acid oxidation; high citrate signals that energy needs are met. It allosterically inhibits PFK-1 (enhancing ATP inhibition), slowing glycolysis.',
              '시트르산은 여러 연료 산화가 만나는 TCA 입구 → 많다 = 에너지 충분 신호. PFK-1을 알로스테릭 억제(ATP 억제 강화) → 해당 ↓.'),
    explain=table(['조절자', 'PFK-1'], [['ATP', '⊗'], ['<b>시트르산</b>', '⊗ (ATP 억제 강화)'], ['AMP · F2,6BP', '▲']]) + tip('시트르산은 세포질로 나가 지방산 합성 재료(ACC 활성화)도 된다.', '연결'))

add(n=15, sec=3, diff=2, title='동물 당신생에 대해 옳은 것',
    en=mcq('Which of the following statements about gluconeogenesis in animal cells is true?', ['A rise in the cellular level of fructose-2,6-bisphosphate stimulates the rate of gluconeogenesis.', 'An animal fed a large excess of fat will convert any fat not needed for energy into glycogen.', 'The conversion of fructose 1,6-bisphosphate to fructose 6-phosphate is not catalyzed by phosphofructokinase-1.', 'The conversion of glucose 6-phosphate to glucose is catalyzed by hexokinase.', 'The conversion of PEP to 2-phosphoglycerate occurs in two steps, including a carboxylation.']),
    ko=mcq('동물 세포의 당신생에 대해 옳은 것은?', ['F2,6BP가 늘면 당신생이 빨라진다', '남는 지방은 글리코겐으로 바뀐다', '<b>F1,6BP → F6P는 PFK-1이 아닌 효소(FBPase-1)가 촉매한다</b>', 'G6P → 포도당은 헥소키나아제가 촉매한다', 'PEP → 2PG는 카복실화를 포함한 2단계다']),
    answer=ans('C', 'F1,6BP → F6P is not catalyzed by phosphofructokinase-1.', 'FBPase-1이 따로 촉매한다'),
    explain=steps('A: F2,6BP는 FBPase-1을 <b>억제</b> → 당신생 ↓.', 'B: 지방산 → 포도당 불가 (동물).', 'D: G6Pase가 촉매.', 'E: 카복실화 2단계는 피루브산 → PEP (PC + PEPCK).') + fig(f26bp_switch(), ''))

# ================================================================ S5 (4) PK
add(n=14, sec=4, diff=2, title='피루브산 키나아제의 알로스테릭 억제자',
    en=mcq('Cellular isozymes of pyruvate kinase are allosterically inhibited by:', ['high concentrations of AMP.', 'high concentrations of ATP.', 'high concentrations of citrate.', 'low concentrations of acetyl-CoA.', 'low concentrations of ATP.']),
    ko=mcq('피루브산 키나아제 동종효소를 알로스테릭으로 억제하는 것은?', ['높은 AMP', '<b>높은 ATP</b>', '높은 시트르산', '낮은 아세틸-CoA', '낮은 ATP']),
    answer=ans('B', 'high concentrations of ATP', '높은 ATP'),
    explain=table(['조절자', 'PK'], [['ATP · 아세틸-CoA · 긴사슬 지방산 · 알라닌', '⊗'], ['F1,6BP (피드포워드)', '▲'], ['간 L형: PKA 인산화', 'OFF']]) + warn('C(시트르산)는 PFK-1의 억제자. D는 “높은” 아세틸-CoA여야 억제.', '함정'))

# ================================================================ S6 (5) 전사
add(n=16, sec=5, diff=2, title='해당·당신생 효소 전사 상향에 관여하지 않는 것',
    en=mcq('Which of the following is not involved in up-regulating the transcription of glycolytic or gluconeogenic enzymes?', ['Phosphofructokinase-2', 'Carbohydrate response element binding protein', 'Sterol response element binding protein', 'cAMP response element binding protein', 'FOXO1']),
    ko=mcq('해당·당신생 효소의 <b>전사</b> 상향 조절에 관여하지 않는 것은?', ['<b>PFK-2</b>', 'ChREBP', 'SREBP', 'CREB', 'FOXO1']),
    answer=ans('A', 'Phosphofructokinase-2', 'PFK-2 — 전사인자가 아니라 F2,6BP를 만드는 효소'),
    explain=table(['전사인자', '켜는 유전자'], [['ChREBP', '해당·지방 합성 (PK 등)'], ['SREBP-1', '해당·지방 합성 (PEPCK 프로모터에도 결합)'], ['CREB', 'PEPCK (글루카곤)'], ['FOXO1', 'PEPCK · G6Pase']]) + key('PFK-2는 알로스테릭 신호(F2,6BP)를 만드는 빠른 조절 — 유전자와 무관.'))

add(n=38, sec=5, diff=2, kind='SA', title='포도당이 PK 합성을 켜는 경로',
    en='<p>Briefly outline the pathway by which glucose activates the synthesis of pyruvate kinase.</p>',
    ko='<p>포도당이 피루브산 키나아제의 합성을 켜는 경로를 간단히 설명하라.</p>',
    answer=sa('Glucose → xylulose 5-phosphate → activates PP2A → PP2A dephosphorylates ChREBP in the cytosol → ChREBP enters the nucleus (further dephosphorylated), pairs with Mlx, and binds ChoRE to up-regulate the pyruvate kinase gene.',
              '포도당 → Xu5P → PP2A 활성 → ChREBP 탈인산화 → 핵으로 이동 → Mlx와 결합 → ChoRE에 붙어 PK 유전자 전사 ↑'),
    explain=fig(vflow(['포도당 ↑ → Xu5P ↑', 'PP2A → ChREBP 탈인산화', 'ChREBP 핵 이동 + Mlx', 'ChoRE → PK 유전자 전사 ↑'], colors=[C['orange'], C['green'], C['blue'], C['green']], box_h=24, gap=14, width=520, font=10.5, bw=400), ''))

add(n=39, sec=5, diff=2, kind='SA', title='인슐린이 올리는 해당 효소 · 내리는 당신생 효소',
    en='<p>Name three glycolytic enzymes whose expression is up-regulated in response to insulin and two gluconeogenic enzymes whose expression is down-regulated in response to insulin.</p>',
    ko='<p>인슐린에 의해 발현이 늘어나는 해당 효소 3개와 줄어드는 당신생 효소 2개를 써라.</p>',
    answer=sa('Up: phosphofructokinase-1, pyruvate kinase, hexokinase II/IV. Down: PEP carboxykinase, glucose 6-phosphatase.', '↑ PFK-1, 피루브산 키나아제, 헥소키나아제 II·IV / ↓ PEPCK, G6Pase'),
    explain=key('인슐린 = “저장하라” → 해당 ↑, 당신생 ↓. FOXO1이 PKB로 분해되어 PEPCK·G6Pase 전사 ↓.'))

# ================================================================ S7 (6) 글리코겐 분해
add(n=17, sec=6, diff=2, title='글리코겐 인산화효소',
    en=mcq('The enzyme glycogen phosphorylase:', ['catalyzes a cleavage of α(1→4) bonds.', 'catalyzes a hydrolytic cleavage of α(1→4) bonds.', 'is a substrate for a kinase.', 'uses glucose 6-phosphate as a substrate.', 'uses glucose as a substrate.']),
    ko=mcq('글리코겐 인산화효소는?', ['(α1→4) 결합을 자른다', '(α1→4) 결합을 <b>가수분해</b>로 자른다', '키나아제의 기질이다', 'G6P를 기질로 쓴다', '포도당을 기질로 쓴다']),
    answer=ans('A (및 C)', 'cleaves α(1→4) bonds (phosphorolysis); it is also a substrate for phosphorylase kinase', '(α1→4)를 인산분해로 자른다 + 인산화효소 키나아제의 기질',
               note='⚠️ 테스트뱅크 정답은 <b>B</b>로 되어 있지만, 인산화효소는 가수분해(H₂O)가 아니라 <b>인산분해(Pᵢ)</b>로 자른다. B는 틀린 문장이야. A와 C가 옳다 — 교수님께 확인 권장.'),
    explain=eq('글리코겐(n) + <b>Pᵢ</b> → 글리코겐(n−1) + G1P') + steps('인산분해 → 바로 G1P(인산 달림) → ATP 절약.', 'C: 인산화효소 b 키나아제가 Ser14를 인산화 → a형(ON).') + key('“phosphorylase” = 인산(Pᵢ)으로 자르는 효소.'))

add(n=18, sec=6, diff=1, title='글리코겐 → 단당류 효소',
    en=mcq('Glycogen is converted to monosaccharide units by:', ['glucokinase.', 'glucose-6-phosphatase', 'glycogen phosphorylase.', 'glycogen synthase.', 'glycogenase.']),
    ko=mcq('글리코겐을 단당 단위로 바꾸는 효소는?', ['글루코키나아제', 'G6Pase', '<b>글리코겐 인산화효소</b>', '글리코겐 합성효소', '글리코게네이스']),
    answer=ans('C', 'glycogen phosphorylase', '글리코겐 인산화효소 → G1P'),
    explain=key('14장 기출 14-19와 같은 문제.') + fig(glycogen_tree(), ''))

add(n=40, sec=6, diff=2, kind='SA', title='근육 글리코겐 분해 과정',
    en='<p>Describe the process of glycogen breakdown in muscle. Include the structure of glycogen, the nature of the breakdown reaction and product, and the required enzyme(s).</p>',
    ko='<p>근육의 글리코겐 분해 과정을 설명하라 (구조, 반응의 성질, 산물, 효소).</p>',
    answer=sa('Glycogen: α(1→4) chains with α(1→6) branches. Glycogen phosphorylase removes terminal residues from nonreducing ends by phosphorolysis → glucose 1-phosphate. Near branch points, debranching enzyme moves residues and removes the branch.',
              '(α1→4) 사슬 + (α1→6) 가지. 인산화효소가 비환원 말단에서 인산분해 → G1P. 가지점 근처는 가지제거 효소가 처리.'),
    explain=table(['단계', '효소', '산물'], [['① 끝 자르기', '글리코겐 인산화효소 (PLP)', 'G1P'], ['② 가지 처리', '가지제거 효소', '포도당 1 + 사슬 이동'], ['③', '포스포글루코뮤테이스', 'G6P → 해당 (근육)']], cls='left') + key('14장 기출 14-69와 같은 문제.'))

add(n=42, sec=6, diff=2, kind='SA', title='간: G1P → 해당 또는 혈당',
    en='<p>In mammalian liver, glucose 1-phosphate, the product of glycogen phosphorylase, can enter glycolysis or replenish blood glucose. Describe the reactions by which these two processes are carried out.</p>',
    ko='<p>간에서 글리코겐 인산화효소의 산물 G1P는 해당으로 가거나 혈당을 보충한다. 각각의 반응을 설명하라.</p>',
    answer=sa('Both start with phosphoglucomutase: G1P → G6P. For glycolysis, G6P continues into glycolysis; for blood glucose, glucose 6-phosphatase (ER) hydrolyzes G6P → glucose + Pᵢ, which leaves the cell.',
              '공통: 포스포글루코뮤테이스로 G1P → G6P. 해당: G6P가 그대로 해당으로. 혈당: G6Pase(소포체)가 G6P → 포도당 → 혈액.'),
    explain=fig(flow(['G1P', 'G6P', '해당 (근육·간)  /  포도당 → 혈액 (간만)'], arrow_labels=['뮤테이스', 'PGI  /  G6Pase'], colors=[C['navy'], C['orange'], C['green']], box_h=36, width=540, font=10), '') +
    warn('테스트뱅크 해설의 “glucose-1-phosphatase”는 오류. 혈당 보충은 G1P → G6P → <b>G6Pase</b>.', '자료 오타'))

# ================================================================ S8 (7) 글리코겐 합성
add(n=19, sec=7, diff=2, title='글리코겐 합성효소에 대해 틀린 것',
    en=mcq('Which statement about mammalian glycogen synthase is not correct?', ['It is especially predominant in liver and muscle.', 'The donor molecule is a sugar nucleotide.', 'The phosphorylated form of this enzyme is inactive.', 'This enzyme adds glucose units to the nonreducing end of glycogen branches.', 'This enzyme adds the initial glucose unit to a tyrosine residue in glycogenin.']),
    ko=mcq('글리코겐 합성효소에 대해 틀린 것은?', ['간·근육에 특히 많다', '공여체는 당 뉴클레오타이드(UDP-포도당)', '인산화형은 비활성이다', '비환원 말단에 포도당을 붙인다', '<b>글리코게닌의 Tyr에 첫 포도당을 붙인다</b>']),
    answer=ans('E', 'adds the initial glucose unit to a tyrosine residue in glycogenin', '틀림 — 첫 포도당은 글리코게닌이 스스로 붙인다'),
    explain=key('글리코게닌 = 프라이머 효소. 자기 Tyr에 포도당을 붙이고 짧은 사슬을 만든 뒤 GS에 넘긴다.') + fig(gly_syn(), ''))

add(n=20, sec=7, diff=2, title='가지형성 효소',
    en=mcq('The glycogen-branching enzyme catalyzes:', ['degradation of α(1→4) linkages in glycogen', 'formation of α(1→4) linkages in glycogen.', 'formation of α(1→6) linkages during glycogen synthesis.', 'glycogen degradation in tree branches.', 'removal of unneeded glucose residues at the ends of branches.']),
    ko=mcq('글리코겐 가지형성 효소가 촉매하는 것은?', ['(α1→4) 분해', '(α1→4) 형성', '<b>합성 중 (α1→6) 결합 형성</b>', '나뭇가지의 글리코겐 분해', '가지 끝 포도당 제거']),
    answer=ans('C', 'formation of α(1→6) linkages during glycogen synthesis', '(α1→6) 가지 결합 형성'),
    explain=fig(glycogen_tree(), '') + table(['효소', '결합'], [['글리코겐 합성효소', '(α1→4) 형성'], ['가지형성 효소', '<b>(α1→6) 형성</b>'], ['가지제거 효소', '(α1→6) 분해']]))

add(n=21, sec=7, diff=2, title='글리코게닌',
    en=mcq('Glycogenin:', ['catalyzes the conversion of starch into glycogen.', 'is the enzyme responsible for forming branches in glycogen.', 'is the gene that encodes glycogen synthase.', 'is the primer on which new glycogen chains are initiated.', 'regulates the synthesis of glycogen.']),
    ko=mcq('글리코게닌은?', ['녹말을 글리코겐으로 바꾼다', '가지를 만든다', 'GS 유전자', '<b>새 글리코겐 사슬이 시작되는 프라이머</b>', '글리코겐 합성을 조절한다']),
    answer=ans('D', 'the primer on which new glycogen chains are initiated', '새 사슬의 프라이머(출발점)'),
    explain=key('GS는 맨손으로 사슬을 시작하지 못한다 → 글리코게닌이 씨앗 역할.') + fig(glycogen_tree(), 'G = 글리코게닌'))

add(n=22, sec=7, diff=2, title='글리코겐 합성효소에 대해 옳은 것',
    en=mcq('Which of the following is true of glycogen synthase?', ['Activation of the enzyme involves a phosphorylation.', 'It catalyzes addition of glucose residues to the nonreducing end of a glycogen chain by formation of α(1→4) bonds.', 'It uses glucose-6-phosphate as donor of glucose units', 'It catalyzes addition of glucose residues at branch points by formation of α(1→6) bonds.', 'The enzyme has measurable activity only in liver.']),
    ko=mcq('글리코겐 합성효소에 대해 옳은 것은?', ['인산화로 활성화된다', '<b>비환원 말단에 (α1→4) 결합으로 포도당을 붙인다</b>', 'G6P를 공여체로 쓴다', '가지점에 (α1→6)을 만든다', '간에서만 활성이 있다']),
    answer=ans('B', 'adds glucose to the nonreducing end by α(1→4) bonds', '비환원 말단에 (α1→4)로 붙인다'),
    explain=steps('A: 인산화 = OFF.', 'C: 공여체는 UDP-포도당.', 'D: 가지형성 효소의 일.', 'E: 근육에도 많다.'))

add(n=41, sec=7, diff=3, kind='SA', title='합성 vs 분해: 기질 · 보조인자 · 조절',
    en='<p>Glycogen synthesis and breakdown are catalyzed by separate enzymes. Contrast the reactions in terms of substrate, cofactors (if any), and regulation.</p>',
    ko='<p>글리코겐 합성과 분해를 기질, 보조인자, 조절 면에서 비교하라.</p>',
    answer=sa('Synthesis: glycogen synthase, UDP-glucose donor; inactivated by phosphorylation, activated by dephosphorylation. Breakdown: glycogen phosphorylase with PLP; phosphorolysis by Pᵢ → G1P; activated by phosphorylation (phosphorylase kinase), inactivated by dephosphorylation.',
              '합성: GS, 기질 UDP-포도당, 인산화 = OFF. 분해: 인산화효소, 보조인자 PLP, Pᵢ로 인산분해 → G1P, 인산화 = ON.'),
    explain=table(['', '합성 (GS)', '분해 (인산화효소)'], [['기질', 'UDP-포도당 + 글리코겐', '글리코겐 + Pᵢ'], ['산물', '글리코겐(n+1) + UDP', 'G1P'], ['보조인자', '—', '<b>PLP</b> (B₆)'], ['인산화되면', '<b>OFF</b>', '<b>ON</b>']]) + key('같은 인산화 스위치가 반대로 작용 → 동시에 돌지 않는다.'))

add(n=43, sec=7, diff=3, kind='SA', title='포도당 → 글리코겐 경로',
    en='<p>Diagram the pathway from glucose to glycogen; show the participation of cofactors and name the enzymes involved.</p>',
    ko='<p>포도당 → 글리코겐 경로를 보조인자와 효소 이름을 넣어 그려라.</p>',
    answer=sa('Glucose + ATP → G6P (hexokinase) → G1P (phosphoglucomutase) → + UTP → UDP-glucose + PPᵢ (UDP-glucose pyrophosphorylase) → glycogen + UDP (glycogen synthase).', '포도당 → (헥소키나아제, ATP) G6P → (뮤테이스) G1P → (피로포스포릴레이스, UTP) UDP-포도당 → (GS) 글리코겐'),
    explain=fig(gly_syn(), '') + tip('PPᵢ → 2Pᵢ 가수분해가 반응을 강하게 앞으로 당긴다.', '포인트'))

add(n=44, sec=7, diff=2, kind='SA', title='글리코겐 합성효소의 반응',
    en='<p>Show the reaction catalyzed by glycogen synthase.</p>', ko='<p>글리코겐 합성효소가 촉매하는 반응을 써라.</p>',
    answer=sa('UDP-glucose + glycogen(n) → UDP + glycogen(n+1); glucose added to a nonreducing end by an α(1→4) linkage.', 'UDP-포도당 + 글리코겐(n) → UDP + 글리코겐(n+1), 비환원 말단에 (α1→4)'),
    explain=eq('UDP-포도당 + (포도당)ₙ → UDP + (포도당)ₙ₊₁') + key('포도당의 C1이 사슬 끝 포도당의 C4–OH에 결합.'))

add(n=45, sec=7, diff=1, kind='SA', title='가지가 많은 글리코겐의 이점',
    en='<p>What is the biological advantage of synthesizing glycogen with many branches?</p>', ko='<p>글리코겐이 가지를 많이 갖는 생물학적 이점은?</p>',
    answer=sa('Branched glycogen is more soluble and has many more nonreducing ends for glycogen synthase and phosphorylase, increasing the rate of synthesis and breakdown.', '① 물에 잘 녹는다 ② 비환원 말단이 많아 합성·분해가 빠르다'),
    explain=fig(glycogen_tree(), '') + key('끝의 수 = 동시에 일할 수 있는 효소 수.'))

add(n=46, sec=7, diff=2, kind='SA', title='글리코게닌의 역할',
    en='<p>Explain the role of glycogenin.</p>', ko='<p>글리코게닌의 역할을 설명하라.</p>',
    answer=sa('Glycogenin is the primer protein: it transfers glucose from UDP-glucose to its own tyrosine –OH and extends a short chain, then complexes with glycogen synthase. The first glucose becomes the reducing end of the glycogen molecule.',
              '프라이머 단백질. UDP-포도당의 포도당을 자기 Tyr–OH에 붙이고 짧은 사슬을 만든 뒤 GS와 결합. 첫 포도당이 글리코겐의 환원 말단이 된다.'),
    explain=fig(glycogen_tree(), '중심의 G = 글리코게닌') + key('글리코겐 한 분자에는 환원 말단이 하나뿐 — 글리코게닌에 붙어 있다.'))

# ================================================================ S10 (9) 분해 조절
add(n=23, sec=9, diff=2, title='근육 글리코겐 인산화효소에 대해 옳은 것',
    en=mcq('Which of the following statements is true of muscle glycogen phosphorylase?', ['It catalyzes phosphorolysis of the α(1→6) bonds at the branch points.', 'It catalyzes the degradation of glycogen by hydrolysis of glycosidic bonds.', 'It degrades glycogen to form glucose 6-phosphate.', 'It exists in an active (a) form and an inactive (b) form that is allosterically regulated by AMP.', 'It removes glucose residues from the reducing ends of the glycogen chains.']),
    ko=mcq('근육 글리코겐 인산화효소에 대해 옳은 것은?', ['가지점 (α1→6)을 인산분해한다', '가수분해로 분해한다', 'G6P를 만든다', '<b>활성 a형 / 비활성 b형이 있고, b형은 AMP로 알로스테릭 조절된다</b>', '환원 말단에서 떼어 낸다']),
    answer=ans('D', 'active (a) and inactive (b) forms; b is allosterically regulated by AMP', 'a/b형 + AMP 알로스테릭 활성화'),
    explain=fig(cascade(), '') + steps('A: 가지점은 가지제거 효소.', 'B: 인산분해.', 'C: 산물은 G1P.', 'E: 비환원 말단.') + key('근육: 에너지 부족(AMP ↑)이면 b형도 켜진다.'))

add(n=25, sec=9, diff=2, title='인산화효소 a를 알로스테릭으로 억제하는 것',
    en=mcq('Glycogen phosphorylase a can be inhibited at an allosteric site by:', ['AMP.', 'calcium.', 'GDP.', 'glucagon.', 'glucose.']),
    ko=mcq('글리코겐 인산화효소 a를 알로스테릭 부위에서 억제하는 것은?', ['AMP', '칼슘', 'GDP', '글루카곤', '<b>포도당</b>']),
    answer=ans('E', 'glucose', '포도당 (간의 혈당 센서)'),
    explain=steps('혈당 ↑ → 간세포 포도당 ↑ → 인산화효소 a에 결합.', 'Ser14-P가 드러나 PP1이 인산 제거 → b형 → 분해 정지.') + key('“혈당 충분하니 그만 꺼내.” A·B는 오히려 활성화.'))

add(n=47, sec=9, diff=2, kind='SA', title='글루카곤 → 글리코겐 분해: 순서',
    en='<p>Order the steps leading to glycogen breakdown resulting from stimulation of liver cells by glucagon: 1) Activation of PKA 2) cAMP levels rise 3) Phosphorylation of phosphorylase b 4) Phosphorylation of phosphorylase b kinase 5) Stimulation of adenylyl cyclase</p>',
    ko='<p>글루카곤이 간세포를 자극해 글리코겐 분해가 일어나는 순서를 매겨라: 1) PKA 활성 2) cAMP ↑ 3) 인산화효소 b 인산화 4) 인산화효소 b 키나아제 인산화 5) 아데닐산 고리화효소 자극</p>',
    answer=sa('5 → 2 → 1 → 4 → 3', '5 → 2 → 1 → 4 → 3'),
    explain=fig(cascade(), '') + key('호르몬 → AC → cAMP → PKA → 인산화효소 b 키나아제 → 인산화효소 b → a. 단계마다 증폭.'))

# ================================================================ S11 (10) 합성 조절
add(n=24, sec=10, diff=2, title='글리코겐 합성과 분해에 대해 옳은 것',
    en=mcq('Which of the following is true of glycogen synthesis and breakdown?', ['Phosphorylation activates the enzyme responsible for breakdown, and inactivates the synthetic enzyme.', 'Synthesis is catalyzed by the same enzyme that catalyzes breakdown.', 'The glycogen molecule “grows” at its reducing end.', 'The immediate product of glycogen breakdown is free glucose.', 'Under normal circumstances, synthesis and breakdown occur simultaneously and at high rates.']),
    ko=mcq('글리코겐 합성·분해에 대해 옳은 것은?', ['<b>인산화는 분해 효소를 켜고 합성 효소를 끈다</b>', '같은 효소가 합성과 분해를 한다', '환원 말단에서 자란다', '분해의 직접 산물은 포도당이다', '보통 합성과 분해가 동시에 빠르게 일어난다']),
    answer=ans('A', 'Phosphorylation activates breakdown and inactivates synthesis.', '인산화 → 분해 ON, 합성 OFF'),
    explain=table(['효소', '인산화되면'], [['글리코겐 인산화효소', 'ON (a형)'], ['글리코겐 합성효소', 'OFF (b형)']]) + key('E는 헛된 회로 — 상반 조절로 막는다.'))

add(n=26, sec=10, diff=2, title='글리코겐 합성효소를 직접 활성화하는 것',
    en=mcq('Which one of the following directly results in the activation of glycogen synthase?', ['Binding of glucose-6-phosphate', 'Dephosphorylation of multiple residues by phosphoprotein phosphatase-1 (PP1)', 'Phosphorylation of specific residues by casein kinase II (CKII)', 'Phosphorylation of specific residues by GSK-3', 'The presence of insulin']),
    ko=mcq('글리코겐 합성효소를 직접 활성화하는 것은?', ['G6P 결합', '<b>PP1에 의한 여러 잔기의 탈인산화</b>', 'CKII의 인산화', 'GSK3의 인산화', '인슐린의 존재']),
    answer=ans('B', 'Dephosphorylation of multiple residues by PP1', 'PP1의 탈인산화 → GS a형(ON)'),
    explain=steps('C·D: 인산화 → OFF.', 'E: 인슐린은 간접(PKB → GSK3 ⊗, PP1 ▲).', 'A: G6P는 b형을 알로스테릭 활성화하지만, 문제는 “직접 활성화(a형 전환)”로 PP1.') + key('GS를 켜는 손 = PP1, 끄는 손 = GSK3 (CKII 프라이밍 후).'))

add(n=27, sec=10, diff=2, title='PP1의 특징이 아닌 것',
    en=mcq('Which one of the following is not a characteristic of phosphoprotein phosphatase-1 (PP1)?', ['PP1 can be phosphorylated by protein kinase A (PKA).', 'PP1 can dephosphorylate glycogen phosphorylase, glycogen synthase, and phosphorylase kinase.', 'PP1 is allosterically activated by glucose-6-phosphate.', 'PP1 is inhibited by activated glycogen phosphorylase', 'PP1 is phosphorylated by glycogen synthase kinase-3 (GSK3).']),
    ko=mcq('PP1의 특징이 <b>아닌</b> 것은?', ['PKA에 의해 (조절 소단위 등이) 인산화될 수 있다', '인산화효소·GS·인산화효소 키나아제를 탈인산화한다', 'G6P로 알로스테릭 활성화된다', '활성화된 인산화효소(a)에 의해 억제된다', '<b>GSK3에 의해 인산화된다</b>']),
    answer=ans('E', 'PP1 is phosphorylated by GSK3.', 'GSK3의 표적은 PP1이 아니라 글리코겐 합성효소'),
    explain=key('GSK3 → GS 인산화(OFF). PP1은 PKA(GM 자리 2, 억제제-1)와 인산화효소 a로 억제된다.') + tip('간: 인산화효소 a가 PP1을 붙잡고 있다가 포도당이 붙으면 풀어 준다 → 분해 OFF + 합성 ON.', '연결'))

add(n=48, sec=10, diff=2, kind='SA', title='포도당 → 글리코겐 합성: 순서',
    en='<p>Order the steps leading to glycogen synthesis resulting from stimulation of liver cells by glucose: 1) Xylulose-5-phosphate is formed 2) Glucose is phosphorylated to glucose-6-phosphate 3) Glycogen synthase is dephosphorylated 4) Protein phosphatase 2A is activated</p>',
    ko='<p>포도당이 간세포를 자극해 글리코겐 합성이 일어나는 순서: 1) Xu5P 생성 2) 포도당 → G6P 3) GS 탈인산화 4) PP2A 활성화</p>',
    answer=sa('2 → 1 → 4 → 3', '2 → 1 → 4 → 3'),
    explain=fig(flow(['포도당 → G6P', 'PPP → Xu5P', 'PP2A ON', 'GS 탈인산화 → ON'], arrow_labels=['', '', ''], colors=[C['navy'], C['orange'], C['green'], C['green']], box_h=36, width=540, font=10), '') + key('Xu5P = “탄수화물 넘친다” 신호 → 저장 쪽으로.'))

# ================================================================ S13 (12) 15.1 기본
add(n=1, sec=12, diff=1, title='효소 활성 조절에 기여하지 않는 것',
    en=mcq('Which of the following does not contribute to the regulation of enzymatic activity?', ['Protein phosphorylation', 'Allosteric regulation', 'Protein stability', 'mRNA stability', 'DNA stability']),
    ko=mcq('효소 활성 조절에 기여하지 <b>않는</b> 것은?', ['단백질 인산화', '알로스테릭 조절', '단백질 안정성', 'mRNA 안정성', '<b>DNA 안정성</b>']),
    answer=ans('E', 'DNA stability', 'DNA 안정성'),
    explain=key('효소 양: 전사·mRNA 안정성·번역·단백질 분해 / 효소 활성: 기질·알로스테릭·인산화·조절 단백질. DNA 자체의 안정성은 조절 수단이 아니다.'))

add(n=7, sec=12, diff=2, title='효소 활성의 “가역적” 변화가 아닌 것',
    en=mcq('Which one of the following types of mechanisms is not known to play a role in the reversible alteration of enzyme activity?', ['Activation by cleavage of an inactive zymogen', 'Allosteric response to a regulatory molecule', 'Alteration of the synthesis or degradation rate of an enzyme', 'Covalent modification of the enzyme', 'Interactions between catalytic and regulatory subunits']),
    ko=mcq('효소 활성을 <b>가역적으로</b> 바꾸는 기전이 아닌 것은?', ['<b>비활성 효소원(zymogen)의 절단에 의한 활성화</b>', '조절 분자에 대한 알로스테릭 반응', '효소 합성·분해 속도 변화', '공유결합 변형', '촉매·조절 소단위 상호작용']),
    answer=ans('A', 'Activation by cleavage of an inactive zymogen', '효소원 절단 — 한 번 잘리면 되돌릴 수 없다(비가역)'),
    explain=key('트립시노겐 → 트립신처럼 펩타이드가 잘리는 활성화는 <b>비가역</b> (18장 소화).') + tip('인산화(D)는 포스파타아제로 되돌릴 수 있어 가역.', '비교'))

add(n=3, sec=12, diff=2, title='평형에서 먼 반응이 좋은 조절점인 이유',
    en=mcq('Reaction steps that are far from equilibrium are good control points in metabolic pathways because', ['the net flux through those steps is easily reversed.', 'the rate differences between the forward and reverse steps are often small.', 'these reactions occur most frequently in the cell.', 'these reactions are highly endergonic.', 'these reactions are highly exergonic.']),
    ko=mcq('평형에서 먼 반응이 좋은 조절 지점인 이유는?', ['흐름이 쉽게 역전된다', '정·역반응 속도 차가 작다', '세포에서 가장 자주 일어난다', '강한 흡에르곤이다', '<b>강한 발에르곤이다</b>']),
    answer=ans('E', 'these reactions are highly exergonic', '크게 발에르곤 → 거의 일방통행 → 효소 활성이 곧 흐름'),
    explain=fig(steady_state(), '') + table(['', '정 : 역', '조절'], [['평형에서 멂', '10.01 : 0.01', '효소를 바꾸면 흐름이 바뀜'], ['평형 근처', '200 : 190', '농도대로 저절로']]))

add(n=6, sec=12, diff=2, title='Q &gt; K′eq이면',
    en=mcq('If the mass action ratio, Q, for a reaction under cellular conditions is larger than the equilibrium constant, Keq, then:', ['the reaction will be at equilibrium.', 'the reaction will go backward and be endergonic.', 'the reaction will go backward and be exergonic.', 'the reaction will go forward and be endergonic.', 'the reaction will go forward and be exergonic.']),
    ko=mcq('세포 조건의 질량작용비 Q가 K′eq보다 크면?', ['평형이다', '역방향, 흡에르곤', '<b>역방향으로 가며, 그 역반응은 발에르곤</b>', '정방향, 흡에르곤', '정방향, 발에르곤']),
    answer=ans('C', 'the reaction will go backward and be exergonic', '역반응 쪽으로 진행 (역방향이 자발적·발에르곤)'),
    explain=eq('ΔG = RT ln (Q / K′eq)') + steps('Q &gt; K → ln &gt; 0 → 정방향 ΔG &gt; 0 → 역방향이 자발적.', '역방향으로 가는 반응은 그 방향으로 ΔG &lt; 0 = 발에르곤.') + key('생성물이 너무 많다 → 반응물 쪽으로 되돌아간다.'))

add(n=28, sec=12, diff=2, kind='SA', title='단백질이 계속 교체되어야 하는 이유',
    en='<p>Why is it important for proper cell function that proteins turn over rather than persisting indefinitely after being synthesized?</p>',
    ko='<p>단백질이 영원히 남지 않고 교체(분해·재합성)되는 것이 왜 중요한가?</p>',
    answer=sa('Turnover allows protein levels to change. If proteins were never degraded, enzyme activity could not be controlled by changing synthesis, since every enzyme ever made would remain.', '분해가 있어야 효소 양을 바꿀 수 있다. 분해가 없으면 합성을 줄여도 효소가 그대로 남아 조절이 안 된다.'),
    explain=key('물을 계속 버려야(분해) 수도꼭지(전사)로 수위(효소 양)를 조절할 수 있다.'))

add(n=29, sec=12, diff=1, kind='SA', title='항상성 vs 평형',
    en='<p>Explain the difference between homeostasis and equilibrium.</p>', ko='<p>항상성과 평형의 차이를 설명하라.</p>',
    answer=sa('Homeostasis is a steady state of constant conditions, usually far from equilibrium, with net flux through pathways. At equilibrium there is no net reaction — for a cell, that is death.', '항상성 = 흐름은 있는데 농도가 일정한 동적 정상 상태(평형에서 멂). 평형 = 알짜 반응 0 → 세포에겐 죽음.'),
    explain=fig(steady_state(), '') + key('정상 상태: V₁ = V₂ ≠ 0 / 평형: 알짜 흐름 = 0.'))

add(n=31, sec=12, diff=2, kind='SA', title='평형에서 먼 반응을 조절해야 하는 이유',
    en='<p>Explain why reactions that are far from equilibrium need to be regulated.</p>', ko='<p>평형에서 먼 반응을 조절해야 하는 이유는?</p>',
    answer=sa('If they were allowed to reach equilibrium, metabolite levels would go haywire: some intermediates (e.g., F1,6BP) would reach molar levels while others (e.g., ATP) would drop too low.', '그냥 평형까지 가게 두면 어떤 중간체(F1,6BP)는 몰 농도까지 쌓이고 어떤 것(ATP)은 바닥나 세포가 혼란에 빠진다.'),
    explain=key('조절 = 흐름을 필요한 만큼만 열어 두는 수도꼭지.'))

# ================================================================ S14 (13) ATP·AMP
add(n=4, sec=13, diff=2, title='세포의 가장 중요한 대사 관심사',
    en=mcq('Aside from maintaining the integrity of its hereditary material, the most important general metabolic concern of a cell is:', ['keeping its glucose levels high.', 'maintaining a constant supply and concentration of ATP.', 'preserving its ability to carry out oxidative phosphorylation.', 'protecting its enzymes from rapid degradation.', 'running all its major metabolic pathways at maximum efficiency.']),
    ko=mcq('유전 물질 보존 다음으로 세포의 가장 중요한 대사 관심사는?', ['포도당 높게 유지', '<b>ATP의 일정한 공급과 농도 유지</b>', '산화적 인산화 능력 보존', '효소 분해 방지', '모든 경로를 최대 효율로']),
    answer=ans('B', 'maintaining a constant supply and concentration of ATP', 'ATP를 일정하게 유지하기'),
    explain=key('세포는 [ATP]를 거의 일정하게 지키고, 작은 변화는 AMP·AMPK가 감지해 바로잡는다.'))

add(n=5, sec=13, diff=2, title='에너지 상태의 가장 민감한 지표',
    en=mcq('The most sensitive indicator of the energetic status of the cell is the concentration of', ['AMP.', 'ADP.', 'ATP.', 'cAMP.', 'glucose.']),
    ko=mcq('세포 에너지 상태의 가장 민감한 지표는?', ['<b>AMP</b>', 'ADP', 'ATP', 'cAMP', '포도당']),
    answer=ans('A', 'AMP', 'AMP'),
    explain=fig(amp_bars(), '') + key('ATP 10% ↓ → AMP 6배 ↑ (아데닐산 키나아제: 2ADP ⇌ ATP + AMP).'))

add(n=30, sec=13, diff=2, kind='SA', title='ATP는 높고 AMP는 낮다 — 조절의 의미',
    en='<p>What are the regulatory implications for the cell with regard to ATP and AMP, given that the former are generally high, and the latter are low?</p>',
    ko='<p>ATP는 보통 높고 AMP는 낮다. 이것이 조절에 갖는 의미는?</p>',
    answer=sa('[ATP] is 5–10 mM while [AMP] is &lt; 0.1 mM, so small changes in ATP become large relative changes in AMP. AMP is therefore a much more sensitive indicator, and many regulatory processes (PFK-1, AMPK, glycogen phosphorylase) respond to AMP.',
              '[ATP] 5–10 mM, [AMP] &lt; 0.1 mM → ATP의 작은 변화가 AMP의 큰 비율 변화로 증폭 → AMP가 예민한 경보. 그래서 PFK-1·AMPK·인산화효소가 AMP에 반응.'),
    explain=fig(amp_bars(), '') + tip('큰 저수지(ATP)가 조금 빠져도 옆 작은 컵(AMP)은 크게 출렁인다.', '비유'))

# ================================================================ S15 (14) MCA
add(n=8, sec=14, diff=2, title='플럭스 조절 계수(C)가 좌우되는 것',
    en=mcq('The flux control coefficient for an enzyme in a multistep pathway depends on:', ['the concentration of the enzyme itself.', 'the concentration of other enzymes in the pathway.', 'the levels of regulatory molecules.', 'the amounts of substrate molecules present at each step.', 'All of the above']),
    ko=mcq('여러 단계 경로에서 효소의 플럭스 조절 계수는 무엇에 좌우되나?', ['그 효소의 농도', '다른 효소들의 농도', '조절 분자 수준', '각 단계의 기질 양', '<b>모두</b>']),
    answer=ans('E', 'All of the above', '위의 모든 것'),
    explain=fig(mca_bars(), '') + key('C는 고정된 성질이 아니라 경로 전체 상황(효소·기질·조절자)에 따라 바뀐다. 합 = 1.'))

add(n=9, sec=14, diff=2, title='탄력성 계수(ε)가 좌우되는 것',
    en=mcq('The elasticity coefficient for an enzyme in a multistep pathway depends on:', ['the concentration of the enzyme itself.', 'the levels of regulatory molecules.', 'the amounts of substrate molecules present at each step.', 'both A and C.', 'both B and C.']),
    ko=mcq('탄력성 계수는 무엇에 좌우되나?', ['효소 자신의 농도', '조절 분자 수준', '기질 양', 'A와 C', '<b>B와 C</b>']),
    answer=ans('E', 'both B and C', '조절 분자와 기질의 농도'),
    explain=key('ε = 기질·조절자 농도 변화에 대한 <b>효소 한 개</b>의 반응성. [S] ≪ Km → ε ≈ 1, 포화 → ε ≈ 0.') + fig(mm_curve(), ''))

add(n=10, sec=14, diff=3, title='혈당 ↑ 때 “flux regulation”의 예',
    en=mcq('Which of the following is an example of flux regulation, not flux control, upon an increase in blood glucose levels?', ['Induction of insulin', 'Increased glucose transport into cells', 'Induction of the synthesis of hexokinase', 'Induction of the synthesis of phosphofructokinase-1', 'Activation of glycogen synthase']),
    ko=mcq('혈당이 오를 때 flux “control(통제)”이 아닌 “regulation(조절)”의 예는?', ['인슐린 유도', '세포 내 포도당 수송 증가', '헥소키나아제 합성 유도', '<b>PFK-1 합성 유도</b>', 'GS 활성화']),
    answer=ans('D', 'Induction of the synthesis of phosphofructokinase-1', 'PFK-1 합성 유도'),
    explain=table(['', 'Control (통제)', 'Regulation (조절)'], [['하는 일', 'flux의 양을 결정', '중간체 농도 균형 유지'], ['예', '포도당 수송·헥소키나아제 (C 큼)', '<b>PFK-1</b> (C 0.21)']]) + key('PFK-1을 늘려도 flux는 거의 안 변한다 — 대신 중간체가 쌓이지 않게 맞춰 준다.'))

add(n=32, sec=14, diff=3, kind='SA', title='C · ε · R의 차이',
    en='<p>Briefly explain the differences between the flux control, elasticity, and response coefficients.</p>', ko='<p>플럭스 조절 계수, 탄력성 계수, 반응 계수의 차이를 간단히 설명하라.</p>',
    answer=sa('C: each enzyme’s relative contribution to setting pathway flux (0–1, sum = 1). ε: responsiveness of a single enzyme to a change in a metabolite or regulator concentration. R: the observed change in pathway flux in response to an external signal (hormone); R = C × ε.',
              'C: 효소가 경로 flux를 정하는 몫(합 1). ε: 효소 하나가 기질·조절자 농도 변화에 반응하는 정도. R: 외부 신호에 대한 경로 flux 변화, <b>R = C × ε</b>.'),
    explain=fig(mca_bars(), '') + key('신호에 아무리 민감해도(ε 큼) C가 작으면 flux는 별로 안 바뀐다.'))

add(n=33, sec=14, diff=3, kind='SA', title='regulation vs control',
    en='<p>Explain the distinction between metabolic “regulation” and metabolic “control” in a multienzyme pathway.</p>', ko='<p>다효소 경로에서 대사 “조절(regulation)”과 “통제(control)”의 차이를 설명하라.</p>',
    answer=sa('Control determines the total flux through the pathway; regulation rebalances metabolite levels along the pathway in response to a change in flux.', 'Control = 경로 전체 flux를 결정. Regulation = flux가 변할 때 중간체 농도를 다시 맞추는 것.'),
    explain=table(['', '대표 효소', '비유'], [['Control', '헥소키나아제 (C 0.79)', '액셀'], ['Regulation', 'PFK-1 (C 0.21)', '서스펜션']]))
