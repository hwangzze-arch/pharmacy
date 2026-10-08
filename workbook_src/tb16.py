# -*- coding: utf-8 -*-
"""16장 테스트뱅크 (lehninger6e_tb_ch16). 제외(강의 범위 밖·과도한 난이도): 7·11·46(숙신산 대칭에 따른 탄소 추적), 24(프로키랄성), 42(회로 효소 유전병)."""
from helpers import *
from tblib import mcq, ans, sa
from exam16 import carbon_flow, pdh_arm, yield_bars, pdh_switch, glyox, amphibolic
from ch16 import tca_wheel

TB = []


def add(**kw):
    kw.setdefault('kind', 'MC')
    TB.append(kw)


def wheel():
    return tca_wheel(width=520, height=330)


def cof_table():
    return table(['조효소', '비타민', '하는 일', '효소'], [['TPP', 'B₁', '피루브산 탈카복실화, 히드록시에틸 운반', 'E1'], ['리포산', '—', '아세틸기 운반 + 전자 (S–S ↔ SH)', 'E2'], ['CoA', 'B₅', '아세틸기를 받아 아세틸-CoA', 'E2'], ['FAD', 'B₂', '환원된 리포산을 재산화', 'E3'], ['NAD⁺', 'B₃', 'FADH₂의 전자를 받아 NADH', 'E3']], cls='left')


def tca_steps(rows):
    return table(['#', '효소', '반응', '보조인자/산물'], rows, cls='left')


R3 = ['③', '아이소시트르산 탈수소효소', '아이소시트르산 → α-KG', 'NAD⁺ → NADH, CO₂, Mn²⁺']
R4 = ['④', 'α-KG 탈수소효소 복합체', 'α-KG → 숙시닐-CoA', 'NAD⁺ → NADH, CO₂, TPP·리포산·CoA·FAD']
R5 = ['⑤', '숙시닐-CoA 합성효소', '숙시닐-CoA → 숙신산', 'GDP + Pᵢ → GTP']
R6 = ['⑥', '숙신산 탈수소효소', '숙신산 → 푸마르산', 'FAD → FADH₂']
R7 = ['⑦', '푸마레이스', '푸마르산 → L-말산', '+ H₂O']
R8 = ['⑧', '말산 탈수소효소', 'L-말산 → OAA', 'NAD⁺ → NADH']

# ================================================================ S1 (0)
add(n=34, sec=0, diff=2, kind='SA', title='아세틸-CoA의 세 가지 공급원',
    en='<p>The citric acid cycle begins with the condensation of acetyl-CoA with oxaloacetate. Describe three possible sources for the acetyl-CoA.</p>',
    ko='<p>시트르산 회로는 아세틸-CoA와 OAA의 축합으로 시작한다. 아세틸-CoA의 공급원 세 가지는?</p>',
    answer=sa('(1) Pyruvate (from glycolysis) via the pyruvate dehydrogenase complex; (2) β-oxidation of fatty acids; (3) degradation of certain amino acids.', '① 피루브산(PDH) ② 지방산 β-산화 ③ 일부 아미노산 분해'),
    explain=fig(carbon_flow(), '') + key('세포호흡 1단계 = 모든 연료를 아세틸-CoA로 모으는 단계 (슬라이드 4, 37).'))

add(n=35, sec=0, diff=1, kind='SA', title='PDH와 해당·TCA의 관계',
    en='<p>Briefly describe the relationship of the pyruvate dehydrogenase complex reaction to glycolysis and the citric acid cycle.</p>',
    ko='<p>PDH 복합체 반응과 해당과정·시트르산 회로의 관계를 간단히 설명하라.</p>',
    answer=sa('PDH converts pyruvate, the end product of glycolysis, into acetyl-CoA, the starting material of the citric acid cycle.', 'PDH는 해당의 최종 산물(피루브산)을 TCA의 출발 물질(아세틸-CoA)로 바꾸는 다리.'),
    explain=fig(flow(['해당 (세포질) → 피루브산', '아세틸-CoA', 'TCA (미토콘드리아 기질)'], arrow_labels=['PDH (비가역, CO₂ + NADH)', ''], colors=[C['navy'], C['orange'], C['green']], box_h=36, width=540, font=10), ''))

add(n=52, sec=0, diff=3, kind='SA', title='O₂를 직접 안 쓰는데 왜 산소 의존적?',
    en='<p>The citric acid cycle is frequently described as the major pathway of aerobic catabolism. However, none of its reactions directly involves oxygen as a reactant. Why is the pathway oxygen-dependent?</p>',
    ko='<p>시트르산 회로는 유산소 이화의 중심이라 불리지만, 어떤 반응도 O₂를 직접 쓰지 않는다. 그런데 왜 산소에 의존하나?</p>',
    answer=sa('The cycle produces NADH (and FADH₂), which are reoxidized only by passing electrons to O₂ through the respiratory chain. Without O₂, NADH accumulates, NAD⁺ runs out, and the cycle stops.', 'NADH·FADH₂는 전자전달계로 O₂에 전자를 넘겨야 다시 NAD⁺·FAD가 된다. O₂가 없으면 NAD⁺가 바닥나 회로가 멈춘다.'),
    explain=key('NAD⁺ = 빈 트럭. 산소(하역장)가 없으면 트럭이 못 돌아와 회로가 멈춘다.') + tip('같은 이유를 묻는 기출: TB 16-45.', '연결'))

# ================================================================ S2 (1) PDH
add(n=1, sec=1, diff=2, title='PDH 반응에 대해 틀린 것',
    en=mcq('Which of the following is not true of the reaction catalyzed by the pyruvate dehydrogenase complex?', ['Biotin participates in the decarboxylation.', 'Both NAD⁺ and a flavin nucleotide act as electron carriers.', 'The reaction occurs in the mitochondrial matrix.', 'The substrate is held by the lipoyl-lysine “swinging arm.”', 'Two different cofactors containing —SH groups participate.']),
    ko=mcq('PDH 복합체 반응에 대해 틀린 것은?', ['<b>비오틴이 탈카복실화에 참여한다</b>', 'NAD⁺와 플라빈 뉴클레오타이드가 전자 운반체', '미토콘드리아 기질에서 일어난다', '리포일라이신 “흔들리는 팔”이 기질을 잡는다', '–SH를 가진 두 보조인자(CoA, 환원 리포산)가 참여']),
    answer=ans('A', 'Biotin participates in the decarboxylation.', '틀림 — 탈카복실화는 TPP. 비오틴은 카복실화(PC)'),
    explain=cof_table() + warn('비오틴 = CO₂를 <b>붙이는</b> 효소(PC, ACC), TPP = CO₂를 <b>떼는</b> 효소(PDH).', '함정'))

add(n=4, sec=1, diff=2, title='유산소 동물세포의 피루브산 산화적 탈카복실화',
    en=mcq('Which of the following statements about the oxidative decarboxylation of pyruvate in aerobic animal cells is correct?', ['One of the products of the PDH complex reactions is a thioester of acetate.', 'The methyl (—CH₃) group is eliminated as CO₂.', 'The process occurs in the cytosolic compartment.', 'PDH uses NAD⁺, lipoic acid, pyridoxal phosphate (PLP), and FAD.', 'PDH operates at full speed under all conditions.']),
    ko=mcq('피루브산의 산화적 탈카복실화에 대해 옳은 것은?', ['<b>산물 중 하나는 아세트산의 티오에스터(아세틸-CoA)다</b>', '메틸기가 CO₂로 빠진다', '세포질에서 일어난다', 'NAD⁺·리포산·PLP·FAD를 쓴다', '항상 최대 속도로 일한다']),
    answer=ans('A', 'One of the products is a thioester of acetate.', '아세틸-CoA = 아세트산의 티오에스터'),
    explain=steps('B: CO₂로 빠지는 건 <b>카복실기</b>.', 'C: 미토콘드리아 기질.', 'D: PLP가 아니라 TPP.', 'E: 인산화·산물로 조절된다 (S11).') + fig(pdh_arm(), ''))

add(n=5, sec=1, diff=3, title='[3,4-¹⁴C]포도당 → 아세틸-CoA의 표지',
    en=mcq('Glucose labeled with ¹⁴C in C-3 and C-4 is completely converted to acetyl-CoA via glycolysis and the PDH complex. What percentage of acetyl-CoA molecules will be labeled, and where?', ['100% labeled at C-1 (carboxyl).', '100% labeled at C-2.', '50% labeled, all at C-2 (methyl).', 'No label will be found in the acetyl-CoA molecules.', 'Not enough information is given.']),
    ko=mcq('C-3, C-4가 표지된 포도당이 해당 + PDH로 아세틸-CoA가 되면 표지는?', ['100% C-1', '100% C-2', '50%, C-2', '<b>아세틸-CoA에는 표지가 없다</b>', '알 수 없다']),
    answer=ans('D', 'No label will be found in the acetyl-CoA molecules.', '표지 없음 — 모두 CO₂로 빠진다'),
    explain=steps('포도당 C3·C4 → 피루브산의 <b>카복실 탄소</b>(14장).', 'PDH가 떼어 내는 CO₂ = 피루브산의 카복실 → 표지가 전부 CO₂로.') + key('14장 탄소 지도: C1·C6 → 메틸, C2·C5 → 카보닐, C3·C4 → 카복실(CO₂).'))

add(n=36, sec=1, diff=3, kind='SA', title='PDH 복합체의 효소·보조인자·산물',
    en='<p>Describe the enzymes, cofactors, intermediates, and products of the pyruvate dehydrogenase complex.</p>',
    ko='<p>PDH 복합체의 효소, 보조인자, 중간체, 산물을 설명하라.</p>',
    answer=sa('E1 (pyruvate dehydrogenase, TPP) decarboxylates pyruvate → hydroxyethyl-TPP + CO₂, then oxidizes it to an acetyl group on lipoyllysine (thioester). E2 (dihydrolipoyl transacetylase) transfers the acetyl to CoA → acetyl-CoA. E3 (dihydrolipoyl dehydrogenase) reoxidizes dihydrolipoate via FAD → NAD⁺ → NADH.',
              'E1(TPP): 탈카복실화 → 히드록시에틸-TPP + CO₂ → 리포산에 아세틸 전달. E2(리포산·CoA): 아세틸-CoA 생성. E3(FAD·NAD⁺): 환원 리포산 재산화 → NADH.'),
    explain=fig(pdh_arm(), '') + cof_table())

add(n=39, sec=1, diff=3, kind='SA', title='피루브산 탄소와 무관한 두 단계',
    en='<p>Two steps in the oxidative decarboxylation of pyruvate to acetyl-CoA do not involve the three carbons of pyruvate, yet are essential. Explain.</p>',
    ko='<p>PDH 반응 중 두 단계는 피루브산의 탄소와 무관하지만 꼭 필요하다. 설명하라.</p>',
    answer=sa('The two E3 steps regenerate oxidized lipoate: dihydrolipoate is reoxidized by FAD (→ FADH₂), then FADH₂ is reoxidized by NAD⁺ (→ NADH). Without them, lipoate stays reduced and the complex stops.', 'E3의 두 단계(④ FAD가 환원 리포산을 산화, ⑤ NAD⁺가 FADH₂를 산화)는 리포산 팔을 다시 쓸 수 있게 되돌린다. 없으면 팔이 환원된 채 멈춘다.'),
    explain=fig(pdh_arm(), '') + key('④⑤ = 전자를 NAD⁺까지 옮겨 리포산 팔을 “리셋”.'))

# ================================================================ S3 (2) 조효소
add(n=2, sec=2, diff=2, title='피루브산 → 아세틸-CoA에 필요 없는 것',
    en=mcq('Which is not required for the oxidative decarboxylation of pyruvate to form acetyl-CoA?', ['ATP', 'CoA-SH', 'FAD', 'Lipoic acid', 'NAD⁺']),
    ko=mcq('피루브산 → 아세틸-CoA에 필요 없는 것은?', ['<b>ATP</b>', 'CoA-SH', 'FAD', '리포산', 'NAD⁺']), answer=ans('A', 'ATP', 'ATP'),
    explain=cof_table() + key('5가지 조효소: TPP · 리포산 · CoA · FAD · NAD⁺. ATP는 필요 없다(에너지를 내놓는 반응).'))

add(n=3, sec=2, diff=2, title='피루브산 → 아세틸-CoA 보조인자 조합',
    en=mcq('Which combination of cofactors is involved in the conversion of pyruvate to acetyl-CoA?', ['Biotin, FAD, and TPP', 'Biotin, NAD⁺, and FAD', 'NAD⁺, biotin, and TPP', 'Pyridoxal phosphate, FAD, and lipoic acid', 'TPP, lipoic acid, and NAD⁺']),
    ko=mcq('피루브산 → 아세틸-CoA에 관여하는 보조인자 조합은?', ['비오틴·FAD·TPP', '비오틴·NAD⁺·FAD', 'NAD⁺·비오틴·TPP', 'PLP·FAD·리포산', '<b>TPP·리포산·NAD⁺</b>']),
    answer=ans('E', 'TPP, lipoic acid, and NAD⁺', 'TPP · 리포산 · NAD⁺'), explain=key('비오틴·PLP가 들어간 보기는 모두 탈락.') + cof_table())

add(n=37, sec=2, diff=3, kind='SA', title='피루브산 ↑ 환자 — 유전 결함 vs 비타민 결핍',
    en='<p>A patient has overly high pyruvate in blood and urine. One cause is a genetic defect in pyruvate dehydrogenase; another is a specific vitamin deficiency. Which vitamin, why, and how would you tell which explanation is correct?</p>',
    ko='<p>혈액·소변의 피루브산이 높은 환자. 원인은 PDH 유전 결함일 수도, 특정 비타민 결핍일 수도 있다. 어떤 비타민이며 왜? 어떻게 구별하나?</p>',
    answer=sa('Thiamine (B₁): without it, TPP cannot be made, so PDH cannot oxidize pyruvate, which accumulates. Test: give thiamine supplements and see whether urinary pyruvate falls.', '<b>티아민(B₁)</b> → TPP 부족 → PDH 정지 → 피루브산 축적. 구별: 티아민을 보충해 피루브산이 줄면 결핍증.'),
    explain=key('보충해서 좋아지면 비타민 결핍, 그대로면 효소 유전 결함.') + tip('티아민 결핍 = 각기병 (TB 16-41).', '연결'))

add(n=38, sec=2, diff=2, kind='SA', title='PDH 보조인자와 역할 짝짓기',
    en='<p>Match the cofactors with their roles: A. CoA-SH B. NAD⁺ C. TPP D. FAD E. Lipoic acid (oxidized).<br>__ attacks and attaches to the central carbon of pyruvate<br>__ oxidizes FADH₂<br>__ accepts the acetyl group from reduced lipoic acid<br>__ oxidizes the reduced form of lipoic acid<br>__ initial electron acceptor in oxidation of pyruvate</p>',
    ko='<p>보조인자 A CoA-SH, B NAD⁺, C TPP, D FAD, E 산화형 리포산을 역할과 짝지어라: 피루브산 가운데 탄소를 공격·결합 / FADH₂ 산화 / 환원 리포산의 아세틸기를 받음 / 환원 리포산을 산화 / 피루브산 산화의 첫 전자 수용체</p>',
    answer=sa('C; B; A; D; E', 'TPP · NAD⁺ · CoA · FAD · 리포산 (C, B, A, D, E)'),
    explain=cof_table() + steps('첫 전자 수용체 = 산화형 리포산: 히드록시에틸이 아세틸로 산화될 때 S–S가 전자를 받는다.'))

add(n=40, sec=2, diff=3, kind='SA', title='PDH에서 FAD의 기능과 재생',
    en='<p>What is the function of FAD in the pyruvate dehydrogenase complex? How is it regenerated?</p>', ko='<p>PDH 복합체에서 FAD의 기능은? 어떻게 재생되나?</p>',
    answer=sa('FAD (E3) accepts electrons from dihydrolipoate, reoxidizing it, becoming FADH₂; FADH₂ is reoxidized by passing electrons to NAD⁺ (→ NADH).', 'FAD는 환원 리포산의 전자를 받아 재산화(→ FADH₂), FADH₂는 NAD⁺에 전자를 넘겨 재생(→ NADH).'),
    explain=fig(pdh_arm(), '') + key('전자 경로: 피루브산 → 리포산 → FAD → NAD⁺.'))

add(n=41, sec=2, diff=2, kind='SA', title='각기병과 피루브산 ↑',
    en='<p>Beriberi is caused by thiamine deficiency. People with severe beriberi have high pyruvate in blood and urine. Explain in terms of specific enzymatic reaction(s).</p>',
    ko='<p>각기병(티아민 결핍) 환자는 혈액·소변 피루브산이 높다. 효소 반응으로 설명하라.</p>',
    answer=sa('Thiamine is needed to make TPP. Without TPP, PDH (E1) cannot decarboxylate pyruvate to acetyl-CoA, so pyruvate from glycolysis accumulates.', '티아민 → TPP. TPP가 없으면 PDH E1이 피루브산을 탈카복실화하지 못해 피루브산이 쌓인다.'),
    explain=key('α-KG DH도 TPP → 회로도 막혀 ATP ↓, 포도당 의존적인 뇌·신경이 먼저 손상.'))

add(n=58, sec=2, diff=3, kind='SA', title='보조인자 ↔ 기능',
    en='<p>Match the cofactor with its function (a function may be used more than once or not at all): (a) NAD⁺/NADH (b) FAD/FADH₂ (c) CoA (d) thiamine (e) biotin — (1) carries O₂ (2) carries small carbon-containing molecules (3) carries e⁻ (4) carries small nitrogen-containing molecules</p>',
    ko='<p>보조인자와 기능을 짝지어라 (중복·미사용 가능): (a) NAD (b) FAD (c) CoA (d) 티아민 (e) 비오틴 — (1) O₂ 운반 (2) 작은 탄소 분자 운반 (3) 전자 운반 (4) 작은 질소 분자 운반</p>',
    answer=sa('(a)-3; (b)-3; (c)-2; (d)-2; (e)-2', 'a–3 · b–3 · c–2 · d–2 · e–2'),
    explain=table(['보조인자', '나르는 것'], [['NAD · FAD', '전자'], ['CoA', '아세틸·아실기'], ['TPP', '히드록시에틸기(2C)'], ['비오틴', 'CO₂']]) + tip('(1)·(4)는 쓰이지 않는다. 질소 운반은 PLP(18장).', '참고'))

# ================================================================ S4 (3) 8단계
add(n=9, sec=3, diff=1, title='회로 중간체가 아닌 것',
    en=mcq('Which of the following is not an intermediate of the citric acid cycle?', ['Acetyl-CoA', 'Citrate', 'Oxaloacetate', 'Succinyl-CoA', 'α-Ketoglutarate']),
    ko=mcq('시트르산 회로의 중간체가 아닌 것은?', ['<b>아세틸-CoA</b>', '시트르산', 'OAA', '숙시닐-CoA', 'α-KG']),
    answer=ans('A', 'Acetyl-CoA', '아세틸-CoA (회로에 들어오는 연료)'), explain=fig(wheel(), '') + key('중간체 = 회로를 돌며 재생되는 것. 아세틸-CoA는 소모되는 연료.'))

add(n=10, sec=3, diff=2, title='회로에서 일어나지 않는 것',
    en=mcq('In mammals, each of the following occurs during the citric acid cycle except:', ['formation of α-ketoglutarate.', 'generation of NADH and FADH₂.', 'metabolism of acetate to carbon dioxide and water.', 'net synthesis of oxaloacetate from acetyl-CoA.', 'oxidation of acetyl-CoA.']),
    ko=mcq('포유류의 시트르산 회로에서 일어나지 <b>않는</b> 것은?', ['α-KG 생성', 'NADH·FADH₂ 생성', '아세트산 → CO₂ + H₂O', '<b>아세틸-CoA로부터 OAA 순합성</b>', '아세틸-CoA 산화']),
    answer=ans('D', 'net synthesis of oxaloacetate from acetyl-CoA', 'OAA 순합성 — 불가능'),
    explain=key('아세틸 2C가 들어오면 CO₂ 2개가 나간다 → OAA 수는 그대로. (식물은 글리옥실산 회로로 가능)'))

add(n=13, sec=3, diff=2, title='회로의 기질 산화와 관련 없는 것',
    en=mcq('Which one of the following is not associated with the oxidation of substrates by the citric acid cycle?', ['All of the below are involved.', 'CO₂ production', 'Flavin reduction', 'Lipoic acid present in some of the enzyme systems', 'Pyridine nucleotide oxidation']),
    ko=mcq('회로의 기질 산화와 관련 <b>없는</b> 것은?', ['아래 모두 관련', 'CO₂ 생성', '플라빈 환원', '일부 효소계에 리포산', '<b>피리딘 뉴클레오타이드(NAD⁺)의 산화</b>']),
    answer=ans('E', 'Pyridine nucleotide oxidation', 'NAD는 산화가 아니라 <b>환원</b>된다 (NAD⁺ → NADH)'),
    explain=key('기질이 산화될 때 NAD⁺·FAD는 환원된다.') + tip('리포산은 α-KG DH 복합체에 있다.', '참고'))

add(n=14, sec=3, diff=3, title='첫 바퀴의 CO₂ 2개는 어디서?',
    en=mcq('The two moles of CO₂ produced in the first turn of the citric acid cycle have their origin in the:', ['carboxyl and methylene carbons of oxaloacetate', 'carboxyl group of acetate and a carboxyl group of oxaloacetate.', 'carboxyl group of acetate and the keto group of oxaloacetate.', 'two carbon atoms of acetate.', 'two carboxyl groups derived from oxaloacetate.']),
    ko=mcq('첫 바퀴에서 나오는 CO₂ 2개의 탄소는 어디서 왔나?', ['OAA의 카복실·메틸렌 탄소', '아세트산 카복실 + OAA 카복실', '아세트산 카복실 + OAA 케토', '아세트산의 두 탄소', '<b>OAA에서 온 두 카복실기</b>']),
    answer=ans('E', 'two carboxyl groups derived from oxaloacetate', 'OAA 유래 카복실기 2개'),
    explain=warn('이번 바퀴에 나가는 CO₂는 방금 들어온 아세틸 탄소가 <b>아니다</b> — OAA의 탄소. 아세틸 탄소는 다음 바퀴 이후에 나간다 (슬라이드 16).', '함정'))

add(n=44, sec=3, diff=3, kind='SA', title='아이소시트르산 → 푸마르산',
    en='<p>Draw the citric acid cycle from isocitrate to fumarate only, showing and naming each intermediate, where high-energy phosphate compounds or reduced carriers are produced, and the enzyme for each step.</p>',
    ko='<p>아이소시트르산부터 푸마르산까지 회로를 중간체, 고에너지 화합물·환원 운반체, 효소와 함께 그려라.</p>',
    answer=sa('Isocitrate → (isocitrate DH; NADH, CO₂) α-KG → (α-KG DH complex; NADH, CO₂) succinyl-CoA → (succinyl-CoA synthetase; GTP) succinate → (succinate DH; FADH₂) fumarate', '아이소시트르산 →(IDH: NADH, CO₂) α-KG →(α-KG DH: NADH, CO₂) 숙시닐-CoA →(합성효소: GTP) 숙신산 →(SDH: FADH₂) 푸마르산'),
    explain=tca_steps([R3, R4, R5, R6]))

add(n=45, sec=3, diff=2, kind='SA', title='NADH를 만드는 세 반응과 산소',
    en='<p>Show the three reactions in the citric acid cycle in which NADH is produced. None involves O₂, but all are strongly inhibited by anaerobic conditions; explain why.</p>',
    ko='<p>NADH를 만드는 세 반응을 쓰라. O₂를 직접 쓰지 않는데 무산소에서 강하게 억제되는 이유는?</p>',
    answer=sa('Isocitrate DH, α-KG DH complex, malate DH. NADH must be reoxidized to NAD⁺ by the respiratory chain using O₂; without O₂, NAD⁺ is depleted.', 'IDH, α-KG DH, MDH. NADH가 전자전달계로 O₂에 전자를 넘겨야 NAD⁺가 재생되는데, 무산소면 NAD⁺가 바닥난다.'),
    explain=tca_steps([R3, R4, R8]))

add(n=49, sec=3, diff=3, kind='SA', title='산화-환원 반응의 산화제·환원제',
    en='<p>Show reactants and products for two of the four redox reactions in the citric acid cycle. Indicate cofactors and label reactants, products, and cofactors as oxidants or reductants.</p>',
    ko='<p>회로의 산화-환원 반응 4개 중 2개를 골라 반응물·산물·보조인자를 쓰고 산화제·환원제를 표시하라.</p>',
    answer=sa('E.g., isocitrate DH: isocitrate (reductant) + NAD⁺ (oxidant) → α-KG + CO₂ + NADH (Mn²⁺). Malate DH: L-malate (reductant) + NAD⁺ (oxidant) → OAA + NADH.', '예: IDH — 아이소시트르산(환원제) + NAD⁺(산화제) → α-KG + CO₂ + NADH. MDH — 말산(환원제) + NAD⁺(산화제) → OAA + NADH.'),
    explain=table(['반응', '환원제 (산화됨)', '산화제 (환원됨)'], [['③ IDH', '아이소시트르산', 'NAD⁺'], ['④ α-KG DH', 'α-KG', 'NAD⁺ (TPP·리포산·FAD 경유)'], ['⑥ SDH', '숙신산', 'FAD'], ['⑧ MDH', '말산', 'NAD⁺']]) + key('전자를 <b>주는</b> 쪽 = 환원제 = 자기는 산화됨.'))

# ================================================================ S5 (4) ①②
add(n=51, sec=4, diff=3, kind='SA', title='플루오로시트르산이 치명적인 이유',
    en='<p>Explain why fluorocitrate, a potent inhibitor of aconitase, is a deadly poison.</p>', ko='<p>아코니테이스의 강력한 억제제인 플루오로시트르산이 치명적인 독인 이유는?</p>',
    answer=sa('Blocking aconitase stops the citric acid cycle, preventing oxidation of acetyl-CoA from carbohydrates and fats; ATP production collapses, which is lethal.', '아코니테이스가 막히면 회로 전체가 멈춰 탄수화물·지방의 아세틸-CoA를 산화하지 못한다 → ATP 급감 → 사망.'),
    explain=fig(flow(['아세틸-CoA + OAA', '시트르산 ↑↑', '✕ 아이소시트르산 …'], arrow_labels=['시트르산 생성효소', '✕ 아코니테이스'], colors=[C['navy'], C['red'], C['gray']], box_h=36, width=520), '') + tip('플루오로아세트산(쥐약) → 플루오로시트르산으로 바뀌어 독성 (치사 합성).', '참고'))

# ================================================================ S6 (5) ③④⑤
add(n=15, sec=5, diff=2, title='α-KG 산화적 탈카복실화에 필요 없는 것',
    en=mcq('The oxidative decarboxylation of α-ketoglutarate requires all but one of the following cofactors. Which one is not required?', ['ATP', 'Coenzyme A', 'Lipoic acid', 'NAD⁺', 'Thiamine pyrophosphate']),
    ko=mcq('α-KG의 산화적 탈카복실화에 필요 없는 것은?', ['<b>ATP</b>', 'CoA', '리포산', 'NAD⁺', 'TPP']), answer=ans('A', 'ATP', 'ATP'),
    explain=key('α-KG DH = PDH와 같은 5 조효소 (TPP·리포산·CoA·FAD·NAD⁺).'))

add(n=16, sec=5, diff=2, title='PDH와 가장 닮은 회로 반응',
    en=mcq('The reaction of the citric acid cycle most similar to the PDH-catalyzed conversion of pyruvate to acetyl-CoA is the conversion of:', ['citrate to isocitrate.', 'fumarate to malate.', 'malate to oxaloacetate.', 'succinyl-CoA to succinate.', 'α-ketoglutarate to succinyl-CoA.']),
    ko=mcq('PDH 반응과 가장 닮은 회로 반응은?', ['시트르산 → 아이소시트르산', '푸마르산 → 말산', '말산 → OAA', '숙시닐-CoA → 숙신산', '<b>α-KG → 숙시닐-CoA</b>']),
    answer=ans('E', 'α-ketoglutarate to succinyl-CoA', 'α-KG → 숙시닐-CoA'),
    explain=table(['', 'PDH', 'α-KG DH'], [['기질', '피루브산', 'α-KG'], ['산물', '아세틸-CoA + CO₂ + NADH', '숙시닐-CoA + CO₂ + NADH'], ['조효소', '5개', '같음'], ['E3', '같은 효소', '같은 효소']]))

add(n=17, sec=5, diff=2, title='티아민 결핍으로 줄어드는 효소',
    en=mcq('Which one of the following enzymatic activities would be decreased by thiamine deficiency?', ['Fumarase', 'Isocitrate dehydrogenase', 'Malate dehydrogenase', 'Succinate dehydrogenase', 'α-Ketoglutarate dehydrogenase complex']),
    ko=mcq('티아민 결핍으로 활성이 줄어드는 효소는?', ['푸마레이스', 'IDH', 'MDH', 'SDH', '<b>α-KG 탈수소효소 복합체</b>']),
    answer=ans('E', 'α-Ketoglutarate dehydrogenase complex', 'α-KG DH 복합체 (TPP 필요)'), explain=key('TPP를 쓰는 회로 효소는 α-KG DH 하나 (+ 회로 입구의 PDH).'))

add(n=18, sec=5, diff=1, title='GTP를 만드는 기질수준 인산화',
    en=mcq('The reaction of the citric acid cycle that produces an ATP equivalent (GTP) by substrate-level phosphorylation is the conversion of:', ['citrate to isocitrate.', 'fumarate to malate.', 'malate to oxaloacetate.', 'succinate to fumarate.', 'succinyl-CoA to succinate.']),
    ko=mcq('기질수준 인산화로 GTP를 만드는 반응은?', ['시트르산 → 아이소시트르산', '푸마르산 → 말산', '말산 → OAA', '숙신산 → 푸마르산', '<b>숙시닐-CoA → 숙신산</b>']),
    answer=ans('E', 'succinyl-CoA to succinate', '숙시닐-CoA → 숙신산 (⑤)'), explain=tca_steps([R5]) + key('티오에스터 에너지 → 포스포히스티딘 → GDP.'))

add(n=48, sec=5, diff=2, kind='SA', title='6탄소 → 첫 4탄소 중간체',
    en='<p>Show the steps in which a six-carbon compound is converted into the first four-carbon intermediate. Show substrates and products, enzymes, and cofactors.</p>',
    ko='<p>6탄소 화합물이 첫 4탄소 중간체가 되기까지의 단계를 효소·보조인자와 함께 쓰라.</p>',
    answer=sa('Isocitrate (6C) → isocitrate DH (NAD⁺, Mn²⁺; −CO₂) → α-KG (5C) → α-KG DH complex (TPP, lipoate, CoA, FAD, NAD⁺; −CO₂) → succinyl-CoA (4C).', '아이소시트르산(6C) →(IDH, NAD⁺, −CO₂) α-KG(5C) →(α-KG DH, 5 조효소, −CO₂) 숙시닐-CoA(4C)'),
    explain=tca_steps([R3, R4]) + tip('테스트뱅크 해설은 숙시닐-CoA 합성효소까지 포함했지만, 숙시닐-CoA가 이미 첫 4C 중간체.', '참고'))

add(n=53, sec=5, diff=2, kind='SA', title='5C → 활성화된 4C (α-KG DH)',
    en='<p>In the citric acid cycle, a five-carbon compound is decarboxylated to yield an activated four-carbon compound. Show the substrate and product, and indicate cofactor(s).</p>',
    ko='<p>5탄소 화합물이 탈카복실화되어 활성화된 4탄소 화합물이 되는 단계의 기질·산물·보조인자를 쓰라.</p>',
    answer=sa('α-Ketoglutarate + CoA + NAD⁺ → succinyl-CoA + CO₂ + NADH; cofactors: TPP, lipoate, CoA, FAD, NAD⁺.', 'α-KG + CoA + NAD⁺ → 숙시닐-CoA + CO₂ + NADH (TPP·리포산·CoA·FAD·NAD⁺)'),
    explain=tca_steps([R4]) + key('“활성화” = 고에너지 티오에스터(숙시닐-CoA) → 다음 단계에서 GTP.'))

add(n=54, sec=5, diff=3, kind='SA', title='CO₂를 내는 두 반응',
    en='<p>CO₂ is produced in two reactions of the citric acid cycle. Name reactant and product, the enzyme, and the cofactors for each.</p>', ko='<p>CO₂가 생기는 두 반응의 반응물·산물·효소·보조인자를 쓰라.</p>',
    answer=sa('Isocitrate DH: isocitrate → α-KG + CO₂ (NAD⁺, Mn²⁺). α-KG DH complex: α-KG → succinyl-CoA + CO₂ (TPP, lipoate, CoA, FAD, NAD⁺).', 'IDH: 아이소시트르산 → α-KG + CO₂ / α-KG DH: α-KG → 숙시닐-CoA + CO₂'),
    explain=tca_steps([R3, R4]))

add(n=55, sec=5, diff=2, kind='SA', title='기질수준 인산화는 어디서?',
    en='<p>In which reaction of the citric acid cycle does substrate-level phosphorylation occur?</p>', ko='<p>회로에서 기질수준 인산화가 일어나는 반응은?</p>',
    answer=sa('Succinyl-CoA synthetase: succinyl-CoA + GDP + Pᵢ → succinate + CoA + GTP.', '숙시닐-CoA 합성효소 (숙시닐-CoA → 숙신산, GTP 생성)'), explain=tca_steps([R5]))

# ================================================================ S7 (6) ⑥⑦⑧
add(n=6, sec=6, diff=3, title='시트르산 회로에 대해 틀린 것',
    en=mcq('Which of the following is not true of the citric acid cycle?', ['All enzymes of the cycle are located in the cytoplasm, except succinate dehydrogenase, which is bound to the inner mitochondrial membrane.', 'In the presence of malonate, one would expect succinate to accumulate.', 'Oxaloacetate is used as a substrate but is not consumed in the cycle.', 'Succinate dehydrogenase channels electrons directly into the electron transfer chain.', 'The condensing enzyme is subject to allosteric regulation by ATP and NADH.']),
    ko=mcq('시트르산 회로에 대해 틀린 것은?', ['<b>SDH만 빼고 모든 효소가 세포질에 있다</b>', '말론산이 있으면 숙신산이 쌓인다', 'OAA는 기질이지만 소모되지 않는다', 'SDH는 전자를 전자전달계로 바로 보낸다', '시트르산 생성효소는 ATP·NADH로 조절된다']),
    answer=ans('A', 'All enzymes are located in the cytoplasm (except SDH).', '틀림 — 회로 효소는 미토콘드리아 <b>기질</b>에 있다'),
    explain=key('SDH = 내막(복합체 II), 나머지 = 기질. 세포질이 아니다.'))

add(n=8, sec=6, diff=1, title='말론산을 넣으면 줄어드는 것',
    en=mcq('Malonate is a competitive inhibitor of succinate dehydrogenase. If malonate is added to mitochondria oxidizing pyruvate, which would decrease in concentration?', ['Citrate', 'Fumarate', 'Isocitrate', 'Pyruvate', 'Succinate']),
    ko=mcq('말론산(SDH 경쟁적 억제제)을 넣으면 농도가 줄어드는 것은?', ['시트르산', '<b>푸마르산</b>', '아이소시트르산', '피루브산', '숙신산']),
    answer=ans('B', 'Fumarate', '푸마르산 (SDH의 산물)'),
    explain=fig(flow(['숙시닐-CoA', '숙신산 ↑', '푸마르산 ↓'], arrow_labels=['', '✕ SDH (말론산)'], colors=[C['navy'], C['red'], C['gray']], box_h=36, width=480), '') + key('막힌 곳 앞(숙신산)은 쌓이고 뒤(푸마르산)는 줄어든다.'))

add(n=19, sec=6, diff=3, title='숙신산·푸마르산·FAD·FADH₂ 1 M 혼합',
    en=mcq('Fumarate/succinate E′° = +0.031 V; FAD/FADH₂ E′° = −0.219 V. If all four were mixed at 1 M with succinate dehydrogenase, what would happen initially?', ['Fumarate and succinate oxidized; FAD and FADH₂ reduced.', 'Fumarate would become reduced; FADH₂ would become oxidized.', 'No reaction (already standard concentrations).', 'Succinate oxidized; FAD reduced.', 'Succinate oxidized; FADH₂ unchanged.']),
    ko=mcq('네 물질 모두 1 M, SDH 존재 시 처음 일어나는 일은?', ['둘 다 산화 / 둘 다 환원', '<b>푸마르산 환원, FADH₂ 산화</b>', '반응 없음', '숙신산 산화, FAD 환원', '숙신산 산화, FADH₂ 그대로']),
    answer=ans('B', 'Fumarate reduced; FADH₂ oxidized.', '전자: FADH₂(−0.219) → 푸마르산(+0.031)'),
    explain=key('13장 기출 13-28과 같은 문제. 표준 조건에서 전자는 낮은 E′° → 높은 E′°.') + warn('세포에서는 반대(숙신산 → 푸마르산)로 간다 — 효소에 결합한 FAD의 실제 전위와 농도가 다르기 때문.', '함정'))

add(n=20, sec=6, diff=3, title='말산 → OAA (ΔG′° +29.7)',
    en=mcq('For L-Malate + NAD⁺ → oxaloacetate + NADH + H⁺, ΔG′° = 29.7 kJ/mol. The reaction as written:', ['can never occur in a cell.', 'can only occur if coupled to a reaction with positive ΔG′°.', 'can only occur in a cell in which NADH is converted to NAD⁺ by electron transport.', 'may occur in cells at certain concentrations of substrate and product.', 'would always proceed at a very slow rate']),
    ko=mcq('말산 + NAD⁺ → OAA + NADH (ΔG′° +29.7)는?', ['세포에서 절대 안 일어난다', 'ΔG′° 양수 반응과 짝지어야 한다', 'NADH가 전자전달로 재산화되는 세포에서만', '<b>기질·산물 농도에 따라 일어날 수 있다</b>', '항상 매우 느리다']),
    answer=ans('D', 'may occur at certain concentrations of substrate and product', '농도에 따라 일어날 수 있다'),
    explain=eq('ΔG = +29.7 + RT ln ([OAA][NADH]/[말산][NAD⁺])') + key('OAA가 시트르산 생성효소(−32.2)로 즉시 소모되어 [OAA]가 매우 낮다 → ΔG ≈ 0.'))

add(n=56, sec=6, diff=3, kind='SA', title='말산 → OAA가 진행하는 조건 (정량)',
    en='<p>Explain in quantitative terms the circumstances under which L-malate + NAD⁺ → OAA + NADH + H⁺ (ΔG′° = +29.7 kJ/mol) can proceed.</p>', ko='<p>ΔG′° = +29.7인 말산 → OAA 반응이 진행할 수 있는 조건을 정량적으로 설명하라.</p>',
    answer=sa('It proceeds when ΔG &lt; 0. ΔG = ΔG′° + RT ln([OAA][NADH]/[malate][NAD⁺]); if [OAA] is kept very low (removed by citrate synthase), the log term becomes very negative.', 'ΔG = +29.7 + RT ln Q &lt; 0 이 되려면 Q &lt; e<sup>−12</sup> ≈ 6 × 10⁻⁶. OAA를 시트르산 생성효소가 계속 치워 아주 낮게 유지.'),
    explain=steps('ln Q &lt; −29.7 / 2.48 = −12.0', 'Q &lt; e<sup>−12</sup> ≈ 6 × 10⁻⁶ → [OAA]가 말산보다 수십만 배 적어야 한다.') + tip('13장 기출 13-38(시트르산 → 아이소시트르산)과 같은 계산.', '연결'))

add(n=21, sec=6, diff=1, title='NAD⁺가 아닌 전자 수용체를 쓰는 효소',
    en=mcq('All of the oxidative steps of the citric acid cycle are linked to the reduction of NAD⁺ except the reaction catalyzed by:', ['isocitrate dehydrogenase.', 'malate dehydrogenase.', 'pyruvate dehydrogenase', 'succinate dehydrogenase.', 'the α-ketoglutarate dehydrogenase complex.']),
    ko=mcq('NAD⁺ 대신 다른 수용체를 쓰는 산화 단계는?', ['IDH', 'MDH', 'PDH', '<b>SDH</b>', 'α-KG DH']), answer=ans('D', 'succinate dehydrogenase', 'SDH (FAD)'),
    explain=key('C–C → C=C 산화는 에너지가 작아 NAD⁺ 대신 FAD.'))

add(n=22, sec=6, diff=1, title='숙신산 → 푸마르산의 보조인자',
    en=mcq('Which cofactor is required for the conversion of succinate to fumarate?', ['ATP', 'Biotin', 'FAD', 'NAD⁺', 'NADP⁺']),
    ko=mcq('숙신산 → 푸마르산에 필요한 보조인자는?', ['ATP', '비오틴', '<b>FAD</b>', 'NAD⁺', 'NADP⁺']), answer=ans('C', 'FAD', 'FAD'), explain=tca_steps([R6]))

add(n=23, sec=6, diff=1, title='플라빈 조효소가 필요한 단계',
    en=mcq('In the citric acid cycle, a flavin coenzyme is required for:', ['condensation of acetyl-CoA and oxaloacetate.', 'oxidation of fumarate.', 'oxidation of isocitrate.', 'oxidation of malate.', 'oxidation of succinate.']),
    ko=mcq('플라빈 조효소가 필요한 단계는?', ['축합', '푸마르산 산화', '아이소시트르산 산화', '말산 산화', '<b>숙신산 산화</b>']), answer=ans('E', 'oxidation of succinate', '숙신산 산화 (SDH)'),
    explain=key('같은 개념을 묻는 기출 3연속: 16-21, 22, 23 → “FAD = SDH”.') + tip('α-KG DH 복합체 E3에도 FAD가 있지만 최종 수용체는 NAD⁺.', '참고'))

add(n=47, sec=6, diff=3, kind='SA', title='α-KG → 말산',
    en='<p>Show the reactions by which α-ketoglutarate is converted to malate in the citric acid cycle.</p>', ko='<p>α-KG가 말산이 되는 반응들을 쓰라.</p>',
    answer=sa('α-KG DH complex (→ succinyl-CoA, NADH, CO₂); succinyl-CoA synthetase (→ succinate, GTP); succinate DH (→ fumarate, FADH₂); fumarase (+ H₂O → L-malate).', 'α-KG DH → 숙시닐-CoA → 합성효소(GTP) → 숙신산 → SDH(FADH₂) → 푸마르산 → 푸마레이스 → 말산'),
    explain=tca_steps([R4, R5, R6, R7]))

add(n=50, sec=6, diff=3, kind='SA', title='숙시닐-CoA → OAA',
    en='<p>Show the steps from succinyl-CoA to oxaloacetate. For each, show substrate and product, enzyme, and cofactors.</p>', ko='<p>숙시닐-CoA부터 OAA까지 각 단계의 기질·산물·효소·보조인자를 쓰라.</p>',
    answer=sa('Succinyl-CoA synthetase (GDP → GTP) → succinate → succinate DH (FAD → FADH₂) → fumarate → fumarase (H₂O) → L-malate → malate DH (NAD⁺ → NADH) → OAA.', '합성효소(GTP) → 숙신산 → SDH(FADH₂) → 푸마르산 → 푸마레이스(H₂O) → 말산 → MDH(NADH) → OAA'),
    explain=tca_steps([R5, R6, R7, R8]))

# ================================================================ S8 (7) 수확
add(n=12, sec=7, diff=1, title='아세틸-CoA 1 mol → 2 CO₂의 알짜 산물',
    en=mcq('Conversion of 1 mol of acetyl-CoA to 2 mol of CO₂ and CoA via the citric acid cycle results in the net production of:', ['1 mol of citrate.', '1 mol of FADH₂.', '1 mol of NADH.', '1 mol of oxaloacetate.', '7 mol of ATP.']),
    ko=mcq('아세틸-CoA 1 mol이 회로에서 2 CO₂ + CoA가 될 때 알짜 산물은?', ['시트르산 1', '<b>FADH₂ 1</b>', 'NADH 1', 'OAA 1', 'ATP 7']),
    answer=ans('B', '1 mol of FADH₂', 'FADH₂ 1 mol (NADH는 3 mol이라 C 틀림)'), explain=fig(yield_bars(), '') + key('1바퀴 = NADH 3 + FADH₂ 1 + GTP 1 + CO₂ 2.'))

add(n=27, sec=7, diff=2, title='피루브산 1 mol → 3 CO₂',
    en=mcq('The conversion of 1 mol of pyruvate to 3 mol of CO₂ via PDH and the citric acid cycle also yields ___ NADH, ___ FADH₂, ___ ATP (GTP).', ['2; 2; 2', '3; 1; 1', '3; 2; 0', '4; 1; 1', '4; 2; 1']),
    ko=mcq('피루브산 1 mol → CO₂ 3 mol (PDH + 회로) 때 NADH·FADH₂·ATP(GTP)는?', ['2·2·2', '3·1·1', '3·2·0', '<b>4·1·1</b>', '4·2·1']),
    answer=ans('D', '4; 1; 1', 'NADH 4 · FADH₂ 1 · GTP 1'), explain=table(['단계', 'NADH', 'FADH₂', 'GTP', 'CO₂'], [['PDH', '1', '', '', '1'], ['회로', '3', '1', '1', '2'], ['<b>합</b>', '<b>4</b>', '<b>1</b>', '<b>1</b>', '<b>3</b>']]))

# ================================================================ S9 (8) 양방향·보충
add(n=25, sec=8, diff=2, title='보충 반응(anaplerotic)',
    en=mcq('Anaplerotic reactions', ['produce oxaloacetate and malate to maintain constant levels of citric acid cycle intermediates', 'produce biotin needed by pyruvate carboxylase', 'recycle pantothenate used to make CoA', 'produce pyruvate and citrate to maintain constant levels of intermediates', 'All of the above']),
    ko=mcq('보충 반응은?', ['<b>OAA·말산을 만들어 회로 중간체 농도를 유지한다</b>', 'PC에 필요한 비오틴을 만든다', '판토텐산을 재활용한다', '피루브산·시트르산을 만든다', '모두']),
    answer=ans('A', 'produce oxaloacetate and malate to maintain constant levels of intermediates', 'OAA·말산 등을 채워 중간체 유지'), explain=fig(amphibolic(), ''))

add(n=26, sec=8, diff=2, title='회로 중간체로 만드는 것',
    en=mcq('Intermediates in the citric acid cycle are used as precursors in the biosynthesis of:', ['amino acids.', 'nucleotides.', 'fatty acids.', 'sterols.', 'All of the above']),
    ko=mcq('회로 중간체가 전구체로 쓰이는 생합성은?', ['아미노산', '뉴클레오타이드', '지방산', '스테롤', '<b>모두</b>']), answer=ans('E', 'All of the above', '모두'),
    explain=fig(amphibolic(), '') + table(['중간체', '산물'], [['OAA · α-KG', '아미노산 · 뉴클레오타이드'], ['시트르산', '지방산 · 스테롤'], ['숙시닐-CoA', '헴']]))

add(n=28, sec=8, diff=2, title='PC 반응에서 CO₂가 붙지 않는 것',
    en=mcq('During the reaction of pyruvate carboxylase, CO₂ is covalently attached to all the following except:', ['phosphate.', 'biotin.', 'pyruvate.', 'lysine.', 'All of the above']),
    ko=mcq('PC 반응에서 CO₂가 공유결합하지 <b>않는</b> 것은?', ['인산 (카복시인산)', '비오틴 (카복시비오틴)', '피루브산 (→ OAA)', '<b>라이신</b>', '모두']), answer=ans('D', 'lysine', '라이신 — 비오틴을 효소에 매다는 끈일 뿐'),
    explain=fig(flow(['HCO₃⁻ + ATP', '카복시인산', '카복시비오틴', 'OAA'], arrow_labels=['', 'CO₂ → 비오틴', 'CO₂ → 피루브산'], colors=[C['navy'], C['orange'], C['orange'], C['green']], box_h=36, width=540, font=10), '') + key('비오틴은 Lys에 붙은 “긴 팔” (슬라이드 53–54).'))

add(n=57, sec=8, diff=3, kind='SA', title='광합성 세균에도 회로 효소가 필요할까?',
    en='<p>You are engineering a bacterium that derives all ATP from sunlight. Will you put the enzymes of the citric acid cycle in it? Why or why not?</p>', ko='<p>모든 ATP를 햇빛으로 얻는 세균을 설계한다. 시트르산 회로 효소를 넣을까? 이유는?</p>',
    answer=sa('Yes. Even if not needed for energy, the cycle provides biosynthetic precursors: α-KG and OAA for amino acids, succinyl-CoA for heme, citrate for lipids, etc.', '넣는다. 에너지용이 아니어도 아미노산(α-KG·OAA), 헴(숙시닐-CoA) 등의 재료를 만들어야 하니까 (양방향성).'),
    explain=fig(amphibolic(), '') + key('회로 = 발전소이자 재료 공장.'))

# ================================================================ S11 (10) PDH 조절
add(n=29, sec=10, diff=2, title='아세틸-CoA의 회로 진입이 줄어들 때',
    en=mcq('Entry of acetyl-CoA into the citric acid cycle is decreased when:', ['[AMP] is high.', 'NADH is rapidly oxidized through the respiratory chain.', 'the ratio of [ATP]/[ADP] is low', 'the ratio of [ATP]/[ADP] is high.', 'the ratio of [NAD⁺]/[NADH] is high.']),
    ko=mcq('아세틸-CoA의 회로 진입이 줄어드는 때는?', ['AMP 높음', 'NADH가 빨리 산화될 때', '[ATP]/[ADP] 낮음', '<b>[ATP]/[ADP] 높음</b>', '[NAD⁺]/[NADH] 높음']),
    answer=ans('D', 'the ratio of [ATP]/[ADP] is high', '[ATP]/[ADP]가 높을 때 (에너지 충분)'), explain=fig(pdh_switch(), '') + key('ATP ↑ → PDH 인산화(OFF) + 시트르산 생성효소 ⊗. 나머지 보기는 모두 “에너지 부족” 신호.'))

# ================================================================ S12 (11) 세 효소
add(n=30, sec=11, diff=2, title='시트르산 생성효소·IDH의 억제자',
    en=mcq('Citrate synthase and the NAD⁺-specific isocitrate dehydrogenase are inhibited by:', ['acetyl-CoA and fructose 6-phosphate.', 'AMP and/or NAD⁺.', 'AMP and/or NADH.', 'ATP and/or NAD⁺.', 'ATP and/or NADH.']),
    ko=mcq('시트르산 생성효소와 IDH를 억제하는 것은?', ['아세틸-CoA·F6P', 'AMP·NAD⁺', 'AMP·NADH', 'ATP·NAD⁺', '<b>ATP·NADH</b>']),
    answer=ans('E', 'ATP and/or NADH', 'ATP · NADH (고에너지 신호)'), explain=table(['효소', '⊗', '▲'], [['시트르산 생성효소', 'NADH, 숙시닐-CoA, 시트르산, ATP', 'ADP'], ['IDH', 'ATP', 'Ca²⁺, ADP'], ['α-KG DH', '숙시닐-CoA, NADH', 'Ca²⁺']]))

# ================================================================ S13 (12) 채널링
add(n=43, sec=12, diff=3, kind='SA', title='센트죄르지의 숙신산 실험',
    en='<p>Preparing a muscle extract dramatically decreases citric acid cycle intermediates. Szent-Györgyi (1935) showed that CO₂ production increased when succinate was added — many moles of CO₂ per mole of succinate. Explain.</p>',
    ko='<p>근육 추출물을 만들면 회로 중간체가 크게 줄어든다. 숙신산을 넣었더니 넣은 양보다 훨씬 많은 CO₂가 나왔다(1935). 설명하라.</p>',
    answer=sa('Succinate is a cycle intermediate that is regenerated, not consumed. Adding it replenishes the depleted intermediates (→ OAA), so the cycle restarts and oxidizes many acetyl-CoA to CO₂ — it acts catalytically.', '숙신산은 소모되지 않고 재생되는 중간체 → 넣으면 OAA까지 채워져 회로가 다시 돌고, 한 분자가 여러 바퀴 돌며 많은 아세틸-CoA를 CO₂로 태운다(촉매처럼).'),
    explain=fig(wheel(), '') + key('회로 중간체 = 회전목마 좌석. 좌석을 하나 넣으면 손님(아세틸)을 계속 태운다.') + tip('세포를 깨면 희석되어 중간체·복합체가 줄어든다 (슬라이드 45).', '연결'))

# ================================================================ S14 (13) 글리옥실산
add(n=31, sec=13, diff=2, title='발아 종자에 글리옥실산 경로가 중요한 이유',
    en=mcq('During seed germination, the glyoxylate pathway is important because it enables plants to:', ['carry out the net synthesis of glucose from acetyl-CoA.', 'form acetyl-CoA from malate.', 'get rid of isocitrate formed from the aconitase reaction.', 'obtain glyoxylate for cholesterol biosynthesis.', 'obtain glyoxylate for pyrimidine synthesis.']),
    ko=mcq('발아 종자에 글리옥실산 경로가 중요한 이유는?', ['<b>아세틸-CoA로 포도당을 순합성할 수 있다</b>', '말산으로 아세틸-CoA를 만든다', '아이소시트르산을 제거한다', '콜레스테롤 재료', '피리미딘 재료']),
    answer=ans('A', 'net synthesis of glucose from acetyl-CoA', '아세틸-CoA(지방)로 포도당 순합성'), explain=fig(glyox(), ''))

add(n=32, sec=13, diff=2, title='글리옥실산 회로 + TCA의 기능',
    en=mcq('A function of the glyoxylate cycle, in conjunction with the citric acid cycle, is to accomplish the:', ['complete oxidation of acetyl-CoA to CO₂.', 'net conversion of lipid to carbohydrate.', 'net synthesis of four-carbon dicarboxylic acids from acetyl-CoA.', 'net synthesis of long-chain fatty acids.', 'Both B and C are correct.']),
    ko=mcq('글리옥실산 회로가 TCA와 함께 하는 일은?', ['아세틸-CoA 완전 산화', '지질 → 탄수화물 순전환', '아세틸-CoA로 4C 다이카복실산 순합성', '긴사슬 지방산 합성', '<b>B와 C 모두</b>']),
    answer=ans('E', 'Both B and C', '지질 → 탄수화물 + 4C(숙신산) 순합성'), explain=key('아세틸-CoA 2 → 숙신산 1 (CO₂ 손실 없음) → 포도당신생.'))

add(n=33, sec=13, diff=2, title='글리옥실산 회로는?',
    en=mcq('The glyoxylate cycle is:', ['a means of using acetate for both energy and biosynthetic precursors.', 'an alternative path of glucose metabolism in cells without enough O₂.', 'defective in people with phenylketonuria.', 'is not active in a mammalian liver.', 'the most direct way of providing precursors for nucleic acids.']),
    ko=mcq('글리옥실산 회로는?', ['<b>아세트산을 에너지와 생합성 재료 둘 다로 쓰는 방법</b>', '산소 부족 시 포도당 대사 우회로', 'PKU에서 결손', '포유류 간에서 활성이 없다', '핵산 재료의 가장 직접적 공급']),
    answer=ans('A', 'using acetate for both energy and biosynthetic precursors', '아세트산을 에너지·재료로 모두 쓰게 한다',
               note='⚠️ D(포유류 간에서는 활성 없음)도 사실은 맞는 문장이야. 테스트뱅크 정답은 A — 시험에서는 A를 고르되 D도 사실임을 알아 두자.'),
    explain=key('아세트산만으로 사는 미생물·종자의 생존 전략 (슬라이드 52).'))

add(n=59, sec=13, diff=3, kind='SA', title='식물은 되고 동물은 안 되는 지방 → 포도당',
    en='<p>Germinating seeds can convert stored fatty acids into oxaloacetate and carbohydrates. Animals cannot. What accounts for this difference?</p>', ko='<p>발아 종자는 지방산을 OAA·탄수화물로 바꾸지만 동물은 못 한다. 이유는?</p>',
    answer=sa('Plants have the glyoxylate cycle (isocitrate lyase, malate synthase), converting two acetyl-CoA into a four-carbon compound used for gluconeogenesis. Animals lack it; each acetyl group entering the citric acid cycle leaves as two CO₂, so there is no net synthesis of oxaloacetate.', '식물: 글리옥실산 회로(아이소시트르산 분해효소 + 말산 생성효소)로 아세틸-CoA 2 → 4C → 당신생. 동물: 회로가 없어 아세틸 2C가 CO₂ 2개로 다 나가 OAA 순증가 없음.'),
    explain=fig(glyox(), '') + key('동물: PDH 비가역 + 글리옥실산 회로 없음 → 지방산 → 포도당 ✕.'))
