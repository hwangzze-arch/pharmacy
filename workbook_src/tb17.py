# -*- coding: utf-8 -*-
"""17장 테스트뱅크 (lehninger6e_tb_ch17). 제외: 39(수화 반응의 위치 선택성 — 유기화학 기전, 강의 범위 밖)."""
from helpers import *
from tblib import mcq, ans, sa
from exam17 import fuel_bars, absorb, mobilize, glycerol_fate, yield_bars, malonyl_switch, ketone_make, ketone_use, ketone_liver
from ch17 import beta_cycle, carnitine, odd_chain

TB = []


def add(**kw):
    kw.setdefault('kind', 'MC')
    TB.append(kw)


def beta_table():
    return table(['#', '효소', '반응', '보조인자'], [['①', '아실-CoA 탈수소효소', 'Cₙ 아실-CoA → trans-Δ²-엔오일-CoA', 'FAD → FADH₂'], ['②', '엔오일-CoA 수화효소', '+ H₂O → L-β-하이드록시아실-CoA', '—'], ['③', 'β-하이드록시아실-CoA 탈수소효소', '→ β-케토아실-CoA', 'NAD⁺ → NADH'], ['④', '티올레이스', '+ CoA → Cₙ₋₂ 아실-CoA + 아세틸-CoA', 'CoA-SH']], cls='left')


def atp_formula():
    return eq('Cₙ 아실-CoA ATP = 4 × (n/2 − 1) + 10 × (n/2)', '유리 지방산이면 − 2 (활성화)')


# ================================================================ S1 (0)
add(n=32, sec=0, diff=1, kind='SA', title='지방이 글리코겐보다 효율적인 저장 연료인 이유',
    en='<p>Why is it more efficient to store energy as lipid rather than as glycogen?</p>', ko='<p>에너지를 글리코겐보다 지방으로 저장하는 것이 왜 더 효율적인가?</p>',
    answer=sa('Lipid yields ~38 kJ/g vs ~17 kJ/g for carbohydrate, and lipid is stored anhydrous while glycogen carries about twice its weight in water, lowering its effective yield to ~6 kJ/g.', '① 지방 38 kJ/g vs 탄수화물 17 kJ/g ② 지방은 물 없이, 글리코겐은 물 2배와 함께 저장 → 실제 ≈ 6 kJ/g'),
    explain=fig(fuel_bars(), '') + key('더 환원됨(–CH₂–) + 비극성(물 없음).'))

# ================================================================ S2 (1)
add(n=1, sec=1, diff=2, title='지단백질 리파아제(LPL)의 작용',
    en=mcq('Lipoprotein lipase acts in:', ['hydrolysis of triacylglycerols of plasma lipoproteins to supply fatty acids to various tissues.', 'intestinal uptake of dietary fat.', 'intracellular lipid breakdown of lipoproteins.', 'lipoprotein breakdown to supply needed amino acids.', 'none of the above.']),
    ko=mcq('지단백질 리파아제가 하는 일은?', ['<b>혈장 지단백질의 TG를 가수분해해 조직에 지방산 공급</b>', '장의 식이 지방 흡수', '세포 안 지단백질 분해', '아미노산 공급용 분해', '정답 없음']),
    answer=ans('A', 'hydrolysis of TG in plasma lipoproteins to supply fatty acids to tissues', '모세혈관에서 킬로미크론 TG → 지방산'), explain=fig(absorb(), '') + key('LPL은 근육·지방 모세혈관 내피에 붙어 있고 apoC-II가 켠다 (⑥단계).'))

add(n=33, sec=1, diff=2, kind='SA', title='장과 혈액 모두에 리파아제가 필요한 이유',
    en='<p>Explain why lipases are required in both the intestine and in the bloodstream.</p>', ko='<p>리파아제가 장과 혈액 모두에 필요한 이유는?</p>',
    answer=sa('Dietary TG must be hydrolyzed to fatty acids by intestinal lipases to be absorbed; inside mucosal cells they are re-esterified to TG and packed into chylomicrons. To enter target tissues, the TG must again be hydrolyzed — by lipoprotein lipase in capillaries.', '흡수하려면 장에서 TG → FA(장 리파아제). 점막에서 다시 TG로 묶여 킬로미크론으로 운반. 조직에 들어가려면 다시 TG → FA(혈관의 LPL).'),
    explain=key('TG → FA → TG → FA → TG: 막을 지날 땐 작게, 운반할 땐 포장해서.') + fig(absorb(), ''))

# ================================================================ S3 (2)
add(n=2, sec=2, diff=2, title='혈중 유리 지방산의 운반',
    en=mcq('Free fatty acids in the bloodstream are:', ['bound to hemoglobin.', 'carried by the protein serum albumin.', 'freely soluble in the aqueous phase of the blood.', 'nonexistent.', 'present at levels independent of epinephrine.']),
    ko=mcq('혈중 유리 지방산은?', ['헤모글로빈에 결합', '<b>혈청 알부민에 실려 운반</b>', '혈장에 자유롭게 녹아 있음', '존재하지 않음', '에피네프린과 무관']),
    answer=ans('B', 'carried by the protein serum albumin', '혈청 알부민'), explain=fig(mobilize(), '') + warn('E: 에피네프린이 지방 동원을 일으켜 혈중 FA를 올린다.', '함정'))

add(n=3, sec=2, diff=2, title='호르몬 민감성 리파아제(HSL)의 역할',
    en=mcq('The role of hormone-sensitive triacylglycerol lipase is to:', ['hydrolyze lipids stored in the liver.', 'hydrolyze membrane phospholipids in hormone-producing cells.', 'hydrolyze triacylglycerols stored in adipose tissue.', 'synthesize lipids in adipose tissue.', 'synthesize triacylglycerols in the liver.']),
    ko=mcq('HSL의 역할은?', ['간 지질 가수분해', '호르몬 생산 세포의 인지질 분해', '<b>지방조직에 저장된 TG 가수분해</b>', '지방조직 지질 합성', '간 TG 합성']),
    answer=ans('C', 'hydrolyze triacylglycerols stored in adipose tissue', '지방세포 TG → 지방산 + 글리세롤'), explain=fig(mobilize(), ''))

add(n=4, sec=2, diff=2, title='글리세롤이 해당과정으로 들어가는 형태',
    en=mcq('The glycerol produced from the hydrolysis of triacylglycerides enters glycolysis as:', ['glucose.', 'glucose-6-phosphate.', 'dihydroxyacetone phosphate.', 'pyruvate.', 'glyceryl CoA.']),
    ko=mcq('TG에서 나온 글리세롤은 무엇으로 해당과정에 들어가나?', ['포도당', 'G6P', '<b>DHAP</b>', '피루브산', '글리세릴-CoA']),
    answer=ans('C', 'dihydroxyacetone phosphate', 'DHAP (→ TPI → G3P)'), explain=fig(glycerol_fate(), ''))

# ================================================================ S4 (3)
add(n=5, sec=3, diff=1, title='지방산의 미토콘드리아 수송에 필요한 것',
    en=mcq('Transport of fatty acids from the cytoplasm to the mitochondrial matrix requires:', ['ATP, carnitine, and coenzyme A.', 'ATP, carnitine, and pyruvate dehydrogenase.', 'ATP, coenzyme A, and hexokinase.', 'ATP, coenzyme A, and pyruvate dehydrogenase.', 'carnitine, coenzyme A, and hexokinase.']),
    ko=mcq('지방산을 세포질에서 기질로 옮기는 데 필요한 것은?', ['<b>ATP · 카르니틴 · CoA</b>', 'ATP · 카르니틴 · PDH', 'ATP · CoA · 헥소키나아제', 'ATP · CoA · PDH', '카르니틴 · CoA · 헥소키나아제']),
    answer=ans('A', 'ATP, carnitine, and coenzyme A', 'ATP · 카르니틴 · CoA'), explain=fig(carnitine(), ''))

add(n=6, sec=3, diff=2, title='아실기를 카르니틴으로 옮기는 이유',
    en=mcq('Fatty acids are activated to acyl-CoAs and the acyl group is further transferred to carnitine because:', ['acyl-carnitines readily cross the mitochondrial inner membrane, but acyl-CoAs do not.', 'acyl-CoAs easily cross the mitochondrial membrane, but fatty acids will not.', 'carnitine is required to oxidize NAD⁺ to NADH.', 'fatty acids cannot be oxidized by FAD unless in the acyl-carnitine form.', 'None of the above is true.']),
    ko=mcq('아실기를 카르니틴으로 옮기는 이유는?', ['<b>아실-카르니틴은 내막을 지나지만 아실-CoA는 못 지난다</b>', '아실-CoA는 쉽게 지난다', '카르니틴이 NAD⁺를 산화', 'FAD 산화에 아실-카르니틴 형태가 필요', '정답 없음']),
    answer=ans('A', 'acyl-carnitines cross the inner membrane; acyl-CoAs do not', '아실-카르니틴만 내막 수송체를 지난다'), explain=fig(carnitine(), '') + key('CoA 풀이 세포질과 기질로 분리되어 있다.'))

add(n=7, sec=3, diff=2, title='카르니틴은?',
    en=mcq('Carnitine is:', ['a 15-carbon fatty acid.', 'an essential cofactor for the citric acid cycle.', 'essential for intracellular transport of fatty acids.', 'one of the amino acids commonly found in protein.', 'present only in carnivorous animals.']),
    ko=mcq('카르니틴은?', ['15탄소 지방산', 'TCA 필수 보조인자', '<b>세포 안 지방산 수송에 필수</b>', '단백질 아미노산', '육식동물에만 있음']),
    answer=ans('C', 'essential for intracellular transport of fatty acids', '지방산을 미토콘드리아로 나르는 운반체'), explain=fig(carnitine(), ''))

add(n=8, sec=3, diff=2, title='미토콘드리아 내막을 지날 수 있는 것',
    en=mcq('Which of these is able to cross the inner mitochondrial membrane?', ['Acetyl–CoA', 'Fatty acyl–carnitine', 'Fatty acyl–CoA', 'Malonyl–CoA', 'None of the above can cross.']),
    ko=mcq('미토콘드리아 내막을 지날 수 있는 것은?', ['아세틸-CoA', '<b>지방 아실-카르니틴</b>', '지방 아실-CoA', '말로닐-CoA', '모두 못 지남']),
    answer=ans('B', 'Fatty acyl–carnitine', '지방 아실-카르니틴 (교환 수송체)'), explain=key('CoA가 붙은 분자는 내막을 못 지난다.') + fig(carnitine(), ''))

add(n=34, sec=3, diff=2, kind='SA', title='활성화 반응을 더 유리하게 만드는 것',
    en='<p>R–COOH + ATP + CoA–SH → R–CO–S–CoA + AMP + PPᵢ, ΔG′° = −15 kJ/mol. What makes the reaction even more favorable in a cell?</p>', ko='<p>지방산 활성화(ΔG′° −15)를 세포에서 더 유리하게 만드는 것은?</p>',
    answer=sa('Hydrolysis of PPᵢ by inorganic pyrophosphatase (ΔG′° ≈ −19 kJ/mol) removes a product and makes the overall reaction more negative.', '무기 피로인산가수분해효소가 PPᵢ → 2Pᵢ (−19)로 산물을 치워 전체 ΔG를 더 음수로.'),
    explain=align([('FA + ATP + CoA → 아실-CoA + AMP + PPᵢ', '−15', ''), ('PPᵢ + H₂O → 2Pᵢ', '−19', ''), ('합계', '<b>−34 kJ/mol</b>', '')]) + key('그래서 활성화 = ATP 2개 분.'))

add(n=35, sec=3, diff=1, kind='SA', title='미토콘드리아에서 카르니틴이 산화를 촉진하는 이유',
    en='<p>The oxidation of acetyl-CoA (fatty acyl groups) added to isolated, intact mitochondria is stimulated strongly by carnitine. Why?</p>', ko='<p>분리한 온전한 미토콘드리아에 아세틸-CoA(지방 아실기)를 넣으면 카르니틴이 산화를 크게 촉진한다. 왜?</p>',
    answer=sa('CoA esters cannot cross the inner membrane; carnitine carries the acyl (or acetyl) groups into the matrix, where oxidation occurs.', 'CoA가 붙은 분자는 내막을 못 지나므로 카르니틴에 실어야 기질로 들어가 산화될 수 있다.'),
    explain=fig(carnitine(), '') + tip('아세틸기도 카르니틴 아세틸전이효소로 아세틸-카르니틴이 되어 건너갈 수 있다.', '참고'))

# ================================================================ S5 (4) β-산화 4단계
add(n=9, sec=4, diff=2, title='β-산화 효소 순서',
    en=mcq('Correct order of β-oxidation enzymes? 1. β-Hydroxyacyl-CoA dehydrogenase 2. Thiolase 3. Enoyl-CoA hydratase 4. Acyl-CoA dehydrogenase', ['1, 2, 3, 4', '3, 1, 4, 2', '4, 3, 1, 2', '1, 4, 3, 2', '4, 2, 3, 1']),
    ko=mcq('β-산화 효소 순서는? 1 β-하이드록시아실-CoA 탈수소효소 2 티올레이스 3 엔오일-CoA 수화효소 4 아실-CoA 탈수소효소', ['1·2·3·4', '3·1·4·2', '<b>4·3·1·2</b>', '1·4·3·2', '4·2·3·1']),
    answer=ans('C', '4, 3, 1, 2', '탈수소(FAD) → 수화 → 탈수소(NAD⁺) → 티올분해'), explain=fig(beta_cycle(), ''))

add(n=14, sec=4, diff=1, title='β-산화에 대해 맞는 것 고르기',
    en=mcq('Which apply to β-oxidation? 1. occurs in the cytosol 2. carbons removed one at a time 3. fatty acids must first be converted to CoA derivatives 4. NADP⁺ is the electron acceptor 5. products can directly enter the citric acid cycle', ['1 and 3 only', '1, 2, and 3', '1, 2, and 5', '3 and 5 only', '4 only']),
    ko=mcq('β-산화에 해당하는 것은? 1 세포질 2 탄소를 하나씩 3 먼저 CoA 유도체로 4 NADP⁺가 수용체 5 산물이 바로 TCA로', ['1·3', '1·2·3', '1·2·5', '<b>3·5만</b>', '4만']),
    answer=ans('D', '3 and 5 only', '3·5'), explain=steps('1 ✕ 미토콘드리아 기질.', '2 ✕ 2개씩(아세틸-CoA).', '4 ✕ NAD⁺와 FAD.'))

add(n=15, sec=4, diff=3, title='β-산화에 대해 옳은 것',
    en=mcq('Which statement concerning β-oxidation is true?', ['About 1200 ATP are produced per 20-carbon fatty acid.', 'One FADH₂ and two NADH are produced for each acetyl-CoA.', 'The fatty acid must be carboxylated by a biotin-dependent reaction first.', 'The free fatty acid must be converted to a thioester before β-oxidation commences.', 'Two NADH are produced for each acetyl-CoA.']),
    ko=mcq('β-산화에 대해 옳은 것은?', ['C20 지방산당 약 1200 ATP', '아세틸-CoA당 FADH₂ 1 + NADH 2', '먼저 비오틴으로 카복실화', '<b>시작 전에 티오에스터(아실-CoA)로 바뀌어야 한다</b>', '아세틸-CoA당 NADH 2']),
    answer=ans('D', 'must be converted to a thioester first', '아실-CoA(티오에스터)로 활성화가 먼저'), explain=steps('A: C20 ≈ 134 ATP.', 'B·E: 한 바퀴당 FADH₂ 1 + NADH 1.', 'C: 비오틴 카복실화는 지방산 <b>합성</b>(ACC).'))

add(n=17, sec=4, diff=1, title='β-산화의 중간체',
    en=mcq('Which compound is an intermediate of the β-oxidation of fatty acids?', ['CH₃–(CH₂)₂₀–CO–COOH', 'CH₃–CH₂–CO–CH₂–CO–OPO₃²⁻', 'CH₃–CH₂–CO–CH₂–OH', 'CH₃–CH₂–CO–CO–S–CoA', 'CH₃–CO–CH₂–CO–S–CoA']),
    ko=mcq('β-산화의 중간체는?', ['α-케토산', '아실 인산', '하이드록시케톤', 'α-케토아실-CoA', '<b>CH₃–CO–CH₂–CO–S-CoA (아세토아세틸-CoA = β-케토아실-CoA)</b>']),
    answer=ans('E', 'CH₃–CO–CH₂–CO–S–CoA', 'β-케토아실-CoA (C4: 아세토아세틸-CoA)'), explain=key('③ 산물 = <b>β</b> 탄소(카보닐에서 두 번째)에 C=O가 있고 <b>CoA</b> 티오에스터.') + steps('D는 α 위치에 C=O → β-산화 중간체 아님.'))

add(n=18, sec=4, diff=2, title='C16 → C14 + 아세틸-CoA 한 바퀴의 산물',
    en=mcq('Conversion of palmitoyl-CoA (16:0) to myristoyl-CoA (14:0) and 1 acetyl-CoA by β-oxidation results in net formation of:', ['1 FADH₂ and 1 NADH.', '1 FADH₂ and 1 NADPH.', '1 FADH₂, 1 NADH, and 1 ATP.', '2 FADH₂ and 2 NADH.', '2 FADH₂, 2 NADH, and 1 ATP.']),
    ko=mcq('팔미토일-CoA → 미리스토일-CoA + 아세틸-CoA (한 바퀴)의 산물은?', ['<b>FADH₂ 1 + NADH 1</b>', 'FADH₂ 1 + NADPH 1', 'FADH₂ · NADH · ATP 1', '각 2개', '각 2개 + ATP']),
    answer=ans('A', '1 FADH₂ and 1 NADH', 'FADH₂ 1 + NADH 1'), explain=fig(beta_cycle(), ''))

add(n=36, sec=4, diff=2, kind='SA', title='β-산화 1·2단계',
    en='<p>Draw the first two steps of β-oxidation of saturated fatty acids. Show structures and cofactors.</p>', ko='<p>포화 지방산 β-산화의 1·2단계를 구조와 보조인자와 함께 그려라.</p>',
    answer=sa('① Acyl-CoA dehydrogenase: R–CH₂–CH₂–CO–SCoA + FAD → trans-Δ² R–CH=CH–CO–SCoA + FADH₂. ② Enoyl-CoA hydratase: + H₂O → L-β-hydroxyacyl-CoA R–CH(OH)–CH₂–CO–SCoA.', '① 아실-CoA 탈수소효소(FAD → FADH₂): α–β 사이에 trans 이중결합 ② 엔오일-CoA 수화효소(+ H₂O): β 탄소에 –OH'),
    explain=beta_table() + key('TCA 숙신산 → 푸마르산 → 말산과 같은 패턴.'))

add(n=37, sec=4, diff=3, kind='SA', title='β-산화 3·4단계',
    en='<p>Draw the third and fourth steps of β-oxidation of a saturated fatty acid. Show structures, enzymes, and cofactors.</p>', ko='<p>β-산화 3·4단계를 구조·효소·보조인자와 함께 그려라.</p>',
    answer=sa('③ β-Hydroxyacyl-CoA dehydrogenase: L-β-hydroxyacyl-CoA + NAD⁺ → β-ketoacyl-CoA + NADH. ④ Thiolase: β-ketoacyl-CoA + CoA-SH → acyl-CoA (n−2) + acetyl-CoA (reverse Claisen).', '③ β-하이드록시아실-CoA 탈수소효소(NAD⁺ → NADH): –OH → C=O ④ 티올레이스(+ CoA): Cα–Cβ 절단 → 아세틸-CoA + 짧아진 아실-CoA'),
    explain=beta_table() + tip('④는 Claisen 축합의 역반응 (13장 보충 13.2).', '연결'))

add(n=38, sec=4, diff=3, kind='SA', title='물 첨가 다음 단계',
    en='<p>One step in mitochondrial fatty acid oxidation adds water across a double bond. What is the next step? Show structures and cofactor(s).</p>', ko='<p>이중결합에 물을 첨가하는 단계 다음은? 구조·보조인자를 보여라.</p>',
    answer=sa('③ β-Hydroxyacyl-CoA dehydrogenase: L-β-hydroxyacyl-CoA + NAD⁺ → β-ketoacyl-CoA + NADH + H⁺.', '③ β-하이드록시아실-CoA 탈수소효소: L-β-하이드록시아실-CoA + NAD⁺ → β-케토아실-CoA + NADH'),
    explain=beta_table() + warn('L-이성질체에만 작용.', '포인트'))

add(n=40, sec=4, diff=2, kind='SA', title='TCA의 숙신산 → 푸마르산과 닮은 반응',
    en='<p>In the citric acid cycle, a double bond is introduced into a four-carbon compound containing –CH₂–CH₂–, producing fumarate. Show a similar reaction in β-oxidation.</p>', ko='<p>TCA에서 –CH₂–CH₂–에 이중결합을 넣어 푸마르산을 만든다. β-산화에서 비슷한 반응은?</p>',
    answer=sa('Acyl-CoA dehydrogenase: R–CH₂–CH₂–CO–SCoA + FAD → trans-Δ²-enoyl-CoA + FADH₂.', '① 아실-CoA 탈수소효소 (FAD → FADH₂, trans 이중결합)'),
    explain=table(['TCA', 'β-산화', '보조인자'], [['숙신산 → 푸마르산', '아실-CoA → 엔오일-CoA', 'FAD'], ['푸마르산 → 말산', '→ 하이드록시아실-CoA', 'H₂O'], ['말산 → OAA', '→ 케토아실-CoA', 'NAD⁺']]))

add(n=41, sec=4, diff=3, kind='SA', title='팔미토일-CoA β-산화의 균형식',
    en='<p>Write a balanced equation for the β-oxidation of palmitoyl-CoA (16:0) and indicate how much of each product is formed.</p>', ko='<p>팔미토일-CoA β-산화의 균형식과 산물의 양을 써라.</p>',
    answer=sa('Palmitoyl-CoA + 7CoA-SH + 7FAD + 7NAD⁺ + 7H₂O → 8 acetyl-CoA + 7FADH₂ + 7NADH + 7H⁺', '팔미토일-CoA + 7CoA + 7FAD + 7NAD⁺ + 7H₂O → 8 아세틸-CoA + 7FADH₂ + 7NADH + 7H⁺'),
    explain=key('7바퀴 → 아세틸-CoA 8 (마지막 바퀴에 2개).'))

add(n=44, sec=4, diff=3, kind='SA', title='뷰티르산(4:0)의 산화',
    en='<p>Describe how cells oxidize butyrate (4:0) to the fragments that enter the citric acid cycle. Show intermediates and cofactors.</p>', ko='<p>뷰티르산(C4)이 TCA에 들어갈 조각이 되기까지의 경로를 설명하라.</p>',
    answer=sa('Activation: butyrate + ATP + CoA → butyryl-CoA + AMP + PPᵢ. (Short chains enter mitochondria directly.) One round of β-oxidation: FAD → FADH₂, + H₂O, NAD⁺ → NADH, thiolase + CoA → 2 acetyl-CoA.', '활성화(ATP → AMP) → 1바퀴 β-산화 (FADH₂ 1 + NADH 1) → 아세틸-CoA 2개'),
    explain=beta_table() + tip('C12 이하 짧은 사슬은 카르니틴 없이 미토콘드리아로 들어간다(슬라이드 18). 테스트뱅크 해설은 카르니틴 셔틀을 거친다고 적었지만 강의 기준으로는 불필요.', '참고'))

# ================================================================ S7 (6) 수지 계산
add(n=10, sec=6, diff=2, title='팔미트산 1개의 ATP 수율',
    en=mcq('If palmitate (16:0) is oxidized completely to CO₂ and H₂O and all energy-conserving products drive ATP synthesis, the net yield of ATP per palmitate is:', ['3.', '10.', '25.', '108.', '1000.']),
    ko=mcq('팔미트산 1개를 완전 산화할 때 알짜 ATP는?', ['3', '10', '25', '<b>108</b>', '1000']),
    answer=ans('D', '108', '108 (가장 가까운 값)', note='⚠️ 정확히는 팔미토일-CoA 108, 유리 팔미트산은 활성화 비용을 빼서 <b>106</b>. 보기 중 가장 가까운 D.'),
    explain=fig(yield_bars(), ''))

add(n=11, sec=6, diff=2, title='아세틸-CoA 하나를 떼어 낼 때마다 ATP',
    en=mcq('Under aerobic conditions, how many ATP would be produced as a consequence of removal of each acetyl-CoA (by β-oxidation)?', ['2', '3', '4', '5', '6']),
    ko=mcq('β-산화로 아세틸-CoA 하나를 떼어 낼 때마다 생기는 ATP는?', ['2', '3', '<b>4</b>', '5', '6']),
    answer=ans('C', '4', 'FADH₂ 1.5 + NADH 2.5 = 4'), explain=key('한 바퀴 = 4 ATP. 떨어진 아세틸-CoA 자체의 10 ATP는 별도.'))

add(n=12, sec=6, diff=2, title='팔미트산 산화에 대해 맞는 것',
    en=mcq('Which are true of the oxidation of 1 mol palmitate by β-oxidation, beginning with free fatty acid? 1. activation requires two ATP equivalents 2. PPᵢ is produced 3. carnitine is an electron acceptor 4. 8 mol FADH₂ 5. 8 mol acetyl-CoA 6. no direct involvement of NAD⁺', ['1 and 5 only', '1, 2, and 5', '1, 2, and 6', '1, 3, and 5', '5 only']),
    ko=mcq('팔미트산 β-산화에 대해 맞는 것? 1 활성화 = ATP 2개 분 2 PPᵢ 생성 3 카르니틴은 전자 수용체 4 FADH₂ 8 5 아세틸-CoA 8 6 NAD⁺ 무관', ['1·5', '<b>1·2·5</b>', '1·2·6', '1·3·5', '5만']),
    answer=ans('B', '1, 2, and 5', '1 · 2 · 5'), explain=steps('3 ✕ 카르니틴은 아실기 운반체.', '4 ✕ FADH₂는 7.', '6 ✕ NAD⁺가 ③단계에 쓰인다.'))

add(n=16, sec=6, diff=3, title='CH₃(CH₂)₁₀COOH의 β-산화 균형식',
    en=mcq('The balanced equation for the degradation of CH₃(CH₂)₁₀COOH via β-oxidation is:', ['… + 5FAD + 5NAD⁺ + 6CoA + 5H₂O + ATP → 6 acetyl-CoA + 5FADH₂ + 5NADH + 5H⁺ + AMP + PPᵢ', '… + 5FAD + 5NAD⁺ + 6CoA + 5H₂O → 6 acetyl-CoA + 5FADH₂ + 5NADH + 5H⁺', '… + 6FAD + 6NAD⁺ + 6CoA + 6H₂O + ATP → 6 acetyl-CoA + 6FADH₂ + 6NADH + 6H⁺ + AMP + PPᵢ', '… + 6FAD + 6NAD⁺ + 6CoA + 6H₂O → 6 acetyl-CoA + 6FADH₂ + 6NADH + 6H⁺']),
    ko=mcq('라우르산(C12)의 β-산화 균형식은?', ['<b>FAD 5 · NAD⁺ 5 · CoA 6 · H₂O 5 · ATP → 아세틸-CoA 6 + … + AMP + PPᵢ</b>', 'ATP 없이 5바퀴', '6바퀴 + ATP', '6바퀴']),
    answer=ans('A', '5 FAD, 5 NAD⁺, 6 CoA, 5 H₂O, ATP → 6 acetyl-CoA + … + AMP + PPᵢ', '5바퀴 + 활성화'), explain=steps('C12 → n/2 − 1 = <b>5바퀴</b>, 아세틸-CoA 6.', 'CoA 6 = 활성화 1 + 티올레이스 5.', '유리 지방산이니 활성화(ATP → AMP + PPᵢ) 포함.'))

add(n=19, sec=6, diff=2, title='팔미트산 산화에 대해 틀린 것',
    en=mcq('Which is not true regarding the oxidation of 1 mol palmitate by β-oxidation?', ['1 mol of ATP is needed.', '8 mol of acetyl-CoA are formed.', '8 mol of FADH₂ are formed.', 'AMP and PPᵢ are formed.', 'The reactions occur in the mitochondria.']),
    ko=mcq('팔미트산 β-산화에 대해 틀린 것은?', ['ATP 1 mol 필요', '아세틸-CoA 8', '<b>FADH₂ 8</b>', 'AMP·PPᵢ 생성', '미토콘드리아에서']),
    answer=ans('C', '8 mol of FADH₂ are formed.', '틀림 — FADH₂는 7 (바퀴 수)'), explain=key('아세틸-CoA = n/2 = 8, FADH₂·NADH = 바퀴 수 = 7.'))

add(n=20, sec=6, diff=3, title='mol당 에너지 순서',
    en=mcq('If an aerobic organism were fed each compound as an energy source, the energy yield per mole would be in the order:', ['alanine &gt; glucose &gt; palmitate', 'glucose &gt; alanine &gt; palmitate', 'glucose &gt; palmitate &gt; alanine', 'palmitate &gt; alanine &gt; glucose', 'palmitate &gt; glucose &gt; alanine']),
    ko=mcq('mol당 에너지 순서는?', ['알라닌 &gt; 포도당 &gt; 팔미트산', '포도당 &gt; 알라닌 &gt; 팔미트산', '포도당 &gt; 팔미트산 &gt; 알라닌', '팔미트산 &gt; 알라닌 &gt; 포도당', '<b>팔미트산 &gt; 포도당 &gt; 알라닌</b>']),
    answer=ans('E', 'palmitate &gt; glucose &gt; alanine', '팔미트산(106) &gt; 포도당(≈32) &gt; 알라닌(≈13)'), explain=table(['연료', '탄소', 'ATP/mol'], [['팔미트산', '16', '≈ 106'], ['포도당', '6', '≈ 30–32'], ['알라닌', '3', '≈ 13–15']]))

add(n=42, sec=6, diff=3, kind='SA', title='탄소 2개 늘 때마다 늘어나는 ATP',
    en='<p>For each two-carbon increase in the length of a saturated fatty acid, how many additional ATP can be formed on complete oxidation?</p>', ko='<p>포화 지방산이 탄소 2개 길어질 때마다 ATP는 몇 개 더 생기나?</p>',
    answer=sa('14 ATP: one more β-oxidation round (FADH₂ 1.5 + NADH 2.5 = 4) plus one more acetyl-CoA through the citric acid cycle (10).', '<b>14</b> = 한 바퀴 더(4) + 아세틸-CoA 하나 더(10)'), explain=atp_formula() + steps('C16 → 106, C18 → 120 (유리 지방산 기준) → 차이 14.'))

# ================================================================ S8 (7) 불포화
add(n=13, sec=7, diff=2, title='ATP를 가장 많이 내는 지방산',
    en=mcq('Complete oxidation of 1 mole of which fatty acid would yield the most ATP?', ['16-carbon saturated', '18-carbon mono-unsaturated', '16-carbon mono-unsaturated', '16-carbon poly-unsaturated', '14-carbon saturated']),
    ko=mcq('완전 산화 시 ATP가 가장 많은 지방산은?', ['C16 포화', '<b>C18 단일불포화</b>', 'C16 단일불포화', 'C16 다중불포화', 'C14 포화']),
    answer=ans('B', '18-carbon mono-unsaturated', 'C18:1 (≈ 118.5)'), explain=key('길이가 먼저: 탄소 2개 = +14 ATP. 이중결합 1개 = −1.5 ATP 정도.') + table(['지방산', '유리 FA ATP'], [['C18:1', '≈ 118.5'], ['C16:0', '106'], ['C16:1', '≈ 104.5'], ['C14:0', '92']]))

# ================================================================ S9 (8) 홀수
add(n=21, sec=8, diff=2, title='긴사슬 지방산 β-산화에 대해 맞는 것',
    en=mcq('Which are true of β-oxidation of long-chain fatty acids? 1. the enzyme complex contains biotin 2. FADH₂ is an electron carrier 3. NADH is an electron carrier 4. oxidation of an 18-carbon fatty acid produces six propionyl-CoA 5. oxidation of a 15-carbon fatty acid produces at least one propionyl-CoA', ['1, 2, and 3', '1, 2, and 5', '2, 3, and 4', '2, 3, and 5', '3 and 5 only']),
    ko=mcq('맞는 것은? 1 비오틴 함유 2 FADH₂ 3 NADH 4 C18 → 프로피오닐-CoA 6개 5 C15 → 프로피오닐-CoA 최소 1개', ['1·2·3', '1·2·5', '2·3·4', '<b>2·3·5</b>', '3·5']),
    answer=ans('D', '2, 3, and 5', '2 · 3 · 5'), explain=steps('1 ✕ 비오틴은 PCC·ACC.', '4 ✕ 짝수 C18은 프로피오닐-CoA 0.', '5 ✔ 홀수는 마지막에 C3 하나.'))

add(n=22, sec=8, diff=2, title='¹⁴CH₃(CH₂)₉COOH의 표지 행방',
    en=mcq('¹⁴CH₃(CH₂)₉COOH (methyl carbon labeled) is fed to an animal. After 30 min of β-oxidation, the label would most likely be in:', ['acetyl-CoA.', 'β-hydroxybutyryl-CoA.', 'both acetyl-CoA and propionyl-CoA.', 'palmitoyl-CoA.', 'propionyl-CoA.']),
    ko=mcq('메틸(ω) 탄소가 표지된 C11 지방산을 주면 표지는?', ['아세틸-CoA', 'β-하이드록시뷰티릴-CoA', '둘 다', '팔미토일-CoA', '<b>프로피오닐-CoA</b>']),
    answer=ans('E', 'propionyl-CoA', '프로피오닐-CoA'), explain=key('β-산화는 카복실 쪽부터 2개씩 자른다 → 반대쪽 끝(메틸) 3개가 마지막 프로피오닐-CoA로 남는다.') + steps('C11 → 4바퀴 → 아세틸-CoA 4 + 프로피오닐-CoA 1 (C9–C11, 표지 포함).'))

add(n=23, sec=8, diff=2, title='홀수 지방산 탄소의 TCA 진입 형태',
    en=mcq('Carbons from an odd-numbered fatty acid enter the citric acid cycle as acetyl-CoA and:', ['butyrate.', 'citrate.', 'malate.', 'succinyl-CoA.', 'α-ketoglutarate.']),
    ko=mcq('홀수 지방산 탄소는 아세틸-CoA와 무엇으로 TCA에 들어가나?', ['뷰티르산', '시트르산', '말산', '<b>숙시닐-CoA</b>', 'α-KG']),
    answer=ans('D', 'succinyl-CoA', '숙시닐-CoA'), explain=fig(odd_chain(), ''))

add(n=24, sec=8, diff=2, title='B₁₂ 결핍(스프루)에서 가장 영향받는 지방산',
    en=mcq('In sprue, vitamin B₁₂ is poorly absorbed. Which fatty acid’s oxidation would be most affected?', ['CH₃(CH₂)₁₀COOH', 'CH₃(CH₂)₁₁COOH', 'CH₃(CH₂)₁₂COOH', 'CH₃(CH₂)₁₄COOH', 'CH₃(CH₂)₁₈COOH']),
    ko=mcq('B₁₂ 흡수 장애(스프루) 환자에게 가장 영향이 큰 지방산은?', ['C12', '<b>C13 (CH₃(CH₂)₁₁COOH)</b>', 'C14', 'C16', 'C20']),
    answer=ans('B', 'CH₃(CH₂)₁₁COOH', 'C13 — 유일한 홀수 지방산'), explain=key('탄소 수 = CH₃ 1 + (CH₂)ₙ + COOH 1 = n + 2. 홀수만 프로피오닐-CoA → 메틸말로닐-CoA 뮤테이스(B₁₂) 필요.'))

add(n=27, sec=8, diff=2, title='비타민 B₁₂에 대해 틀린 것',
    en=mcq('Which is not true about vitamin B₁₂?', ['Vitamin B₁₂ contains a porphyrin ring.', 'Vitamin B₁₂ contains a carbon–cobalt bond.', 'Vitamin B₁₂ readily undergoes homolytic bond cleavage.', 'Deficiency of vitamin B₁₂ causes pernicious anemia.', 'Vitamin B₁₂ catalyzes hydrogen atom exchange with solvent H₂O.']),
    ko=mcq('B₁₂에 대해 틀린 것은?', ['포르피린 고리를 가진다', 'C–Co 결합이 있다', '균일 분해가 쉽다', '결핍 시 악성빈혈', '<b>용매(물)와 수소 원자를 교환하는 반응을 촉매한다</b>']),
    answer=ans('E', 'catalyzes hydrogen atom exchange with solvent H₂O', '틀림 — H는 분자 <b>안</b>에서 자리를 바꿀 뿐, 물과 교환하지 않는다',
               note='⚠️ 엄밀히는 A도 틀려. B₁₂는 포르피린이 아니라 <b>코린(corrin)</b> 고리(18장 슬라이드 59). 테스트뱅크 정답은 E.'),
    explain=key('B₁₂ 반응 = 이웃 탄소의 H와 X 자리바꿈 (라디칼, 분자 내부).') + tip('18장 S13에서 자세히.', '연결'))

add(n=43, sec=8, diff=3, kind='SA', title='펠라곤산(C9)의 완전 산화 균형식',
    en='<p>Write a balanced equation for the complete oxidation (to acetyl-CoA and other products) of pelargonic acid, CH₃(CH₂)₇COOH.</p>', ko='<p>펠라곤산(C9)을 아세틸-CoA 등으로 완전 산화하는 균형식을 써라.</p>',
    answer=sa('Pelargonic acid + 4CoA + 3FAD + 3NAD⁺ + 3H₂O + 2ATP + HCO₃⁻ → 3 acetyl-CoA + succinyl-CoA + 3FADH₂ + 3NADH + 3H⁺ + AMP + PPᵢ + ADP + Pᵢ', 'C9 → 3바퀴 → 아세틸-CoA 3 + 프로피오닐-CoA → (PCC: ATP, HCO₃⁻) → 숙시닐-CoA'),
    explain=steps('활성화: ATP → AMP + PPᵢ, CoA 1.', 'C9: 3바퀴 → FADH₂ 3, NADH 3, 아세틸-CoA 3 + 프로피오닐-CoA(CoA 3 추가).', '프로피오닐-CoA 카복실화효소: HCO₃⁻ + ATP → ADP + Pᵢ.') +
    warn('테스트뱅크 답에는 ATP가 1개뿐(활성화)이고 PCC의 ATP → ADP + Pᵢ가 빠져 있어. 위처럼 ATP 2개가 맞아.', '자료 오류') + fig(odd_chain(), ''))

add(n=45, sec=8, diff=3, kind='SA', title='발레르산(5:0)의 산화',
    en='<p>Describe how cells oxidize valerate (5:0) to fragments that enter the citric acid cycle.</p>', ko='<p>발레르산(C5)이 TCA에 들어갈 조각이 되는 경로를 설명하라.</p>',
    answer=sa('Activation to valeryl-CoA (ATP → AMP + PPᵢ); one round of β-oxidation → acetyl-CoA + propionyl-CoA; propionyl-CoA → (biotin carboxylase) D-methylmalonyl-CoA → (epimerase) L → (B₁₂ mutase) succinyl-CoA.', '활성화 → 1바퀴 → 아세틸-CoA + 프로피오닐-CoA → 숙시닐-CoA (비오틴, B₁₂)'), explain=fig(odd_chain(), ''))

add(n=46, sec=8, diff=3, kind='SA', title='C11 산화에 CO₂가 필요하고 아비딘이 막는 이유',
    en='<p>Liver extracts completely oxidized palmitate, but undecanoic acid (11:0) was incompletely oxidized unless CO₂ was bubbled in. Avidin (binds biotin) prevented complete oxidation of undecanoate even with CO₂, but had no effect on palmitate. Explain.</p>', ko='<p>팔미트산은 완전 산화되는데 C11은 CO₂를 넣어야만 완전 산화된다. 비오틴 결합 단백질 아비딘을 넣으면 C11만 막힌다. 설명하라.</p>',
    answer=sa('Odd-chain oxidation leaves propionyl-CoA, which must be carboxylated (CO₂ + ATP) by biotin-dependent propionyl-CoA carboxylase to methylmalonyl-CoA. Avidin binds biotin, blocking this step; palmitate yields only acetyl-CoA and is unaffected.', '홀수 → 프로피오닐-CoA → PCC(비오틴, CO₂ 필요) → 메틸말로닐-CoA. 아비딘이 비오틴을 잡아 이 단계만 막힌다. 짝수는 무관.'),
    explain=fig(odd_chain(), '') + tip('날달걀 흰자의 아비딘 → 비오틴 결핍 (17장 S11).', '연결'))

add(n=47, sec=8, diff=3, kind='SA', title='프로피온산 대사의 비오틴과 B₁₂',
    en='<p>Biotin and vitamin B₁₂ play crucial roles in propionate metabolism. Show the steps in which each is essential.</p>', ko='<p>프로피온산 대사에서 비오틴과 B₁₂가 필요한 단계를 보여라.</p>',
    answer=sa('Biotin: propionyl-CoA carboxylase (propionyl-CoA + HCO₃⁻ + ATP → D-methylmalonyl-CoA). B₁₂: methylmalonyl-CoA mutase (L-methylmalonyl-CoA → succinyl-CoA).', '비오틴 = 프로피오닐-CoA 카복실화효소 / B₁₂ = 메틸말로닐-CoA 뮤테이스'), explain=fig(odd_chain(), ''))

add(n=48, sec=8, diff=3, kind='SA', title='홀수 지방산의 X는?',
    en='<p>Total degradation of an odd-numbered fatty acid yields acetyl-CoA and compound X. Show X and how it becomes a citric acid cycle intermediate.</p>', ko='<p>홀수 지방산 분해의 산물 X와, X가 TCA 중간체가 되는 경로를 보여라.</p>',
    answer=sa('X = propionyl-CoA (CH₃–CH₂–CO–SCoA) → carboxylase (biotin, ATP) → D-methylmalonyl-CoA → epimerase → L-methylmalonyl-CoA → mutase (B₁₂) → succinyl-CoA.', 'X = 프로피오닐-CoA → (비오틴) → (에피머화) → (B₁₂) → 숙시닐-CoA'), explain=fig(odd_chain(), ''))

# ================================================================ S10 (9) 조절
add(n=25, sec=9, diff=2, title='β-산화의 주요 조절점',
    en=mcq('Which enzyme is the major regulatory control point for β-oxidation?', ['Pyruvate carboxylase', 'Carnitine acyl transferase I', 'Acetyl CoA dehydrogenase', 'Enoyl CoA isomerase', 'Methylmalonyl CoA mutase']),
    ko=mcq('β-산화의 주요 조절점은?', ['PC', '<b>카르니틴 아실전이효소 I (CAT I)</b>', '아세틸-CoA 탈수소효소', '엔오일-CoA 이성질화효소', '메틸말로닐-CoA 뮤테이스']),
    answer=ans('B', 'Carnitine acyl transferase I', 'CAT I (입구)'), explain=fig(malonyl_switch(), ''))

add(n=26, sec=9, diff=2, title='CAT I을 조절하는 대사물',
    en=mcq('The metabolite that regulates the activity of carnitine acyl transferase I is:', ['acetyl-CoA.', 'carnitine-CoA.', 'malonyl-CoA.', 'NADH.', 'CoA.']),
    ko=mcq('CAT I을 조절하는 대사물은?', ['아세틸-CoA', '카르니틴-CoA', '<b>말로닐-CoA</b>', 'NADH', 'CoA']),
    answer=ans('C', 'malonyl-CoA', '말로닐-CoA (억제)'), explain=fig(malonyl_switch(), '') + key('지방산 합성 중(말로닐-CoA ↑)엔 분해 입구를 닫는다.'))

# ================================================================ S12 (11) 퍼옥시좀·ω
add(n=28, sec=11, diff=2, title='퍼옥시좀에서만 생기는 것',
    en=mcq('During β-oxidation of fatty acids, ______ is produced in peroxisomes but not in mitochondria.', ['acetyl-CoA', 'FADH₂', 'H₂O', 'H₂O₂', 'NADH']),
    ko=mcq('β-산화 중 퍼옥시좀에서만 생기는 것은?', ['아세틸-CoA', 'FADH₂', 'H₂O', '<b>H₂O₂</b>', 'NADH']),
    answer=ans('D', 'H₂O₂', '과산화수소 (아실-CoA 산화효소의 FADH₂ → O₂)'), explain=key('퍼옥시좀: FADH₂의 전자 → O₂ 직접 → H₂O₂ (카탈레이스가 분해), ATP 없음.'))

add(n=29, sec=11, diff=2, title='β-산화 vs ω-산화',
    en=mcq('Comparing β-oxidation and ω-oxidation, which statement is correct?', ['Both occur in the cytoplasm.', 'β-oxidation occurs at the carboxyl end, whereas ω-oxidation occurs at the methyl end.', 'β-oxidation occurs at the methyl end, ω-oxidation at the carboxyl end.', 'β-oxidation mainly in the cytoplasm, ω-oxidation mainly in mitochondria.', 'β-oxidation mainly in mitochondria, ω-oxidation mainly in the cytoplasm.']),
    ko=mcq('β-산화와 ω-산화 비교로 옳은 것은?', ['둘 다 세포질', '<b>β는 카복실 끝, ω는 메틸 끝</b>', 'β는 메틸, ω는 카복실', 'β 세포질, ω 미토', 'β 미토, ω 세포질']),
    answer=ans('B', 'β at the carboxyl end, ω at the methyl end', 'β = 카복실 쪽, ω = 메틸 쪽'), explain=warn('E 함정: ω-산화는 세포질이 아니라 <b>소포체(ER)</b>.', '함정'))

add(n=49, sec=11, diff=3, kind='SA', title='미토콘드리아 vs 퍼옥시좀 β-산화의 두 차이',
    en='<p>What are the two major differences between β-oxidation in mitochondria and in peroxisomes?</p>', ko='<p>미토콘드리아와 퍼옥시좀 β-산화의 두 가지 큰 차이는?</p>',
    answer=sa('(1) In the first step, peroxisomal FADH₂ is reoxidized directly by O₂ producing H₂O₂ (no ATP), whereas mitochondrial FADH₂ feeds the respiratory chain. (2) Peroxisomal enzymes act on very-long-chain (e.g., C26) fatty acids.', '① 1단계 FADH₂: 퍼옥시좀은 O₂로 → H₂O₂(ATP 없음), 미토는 전자전달계 ② 퍼옥시좀은 매우 긴 사슬(C26 등)을 담당'),
    explain=table(['', '미토콘드리아', '퍼옥시좀'], [['1단계 효소', '아실-CoA 탈수소효소', '아실-CoA 산화효소'], ['FADH₂ 전자', '호흡 사슬 → ATP', 'O₂ → H₂O₂'], ['대상', '일반', 'VLCFA·가지 FA']]))

add(n=50, sec=11, diff=2, kind='SA', title='ω-산화의 기본 개념',
    en='<p>Briefly explain the basic concept of ω-oxidation.</p>', ko='<p>ω-산화의 기본 개념을 간단히 설명하라.</p>',
    answer=sa('In the ER, the ω (methyl) carbon of medium-chain (10–12C) fatty acids is oxidized in three steps (P450 hydroxylation, alcohol and aldehyde dehydrogenases) to a second carboxyl group; the dicarboxylic acid then undergoes β-oxidation from both ends, giving succinate or adipate.', '소포체에서 메틸(ω) 끝을 3단계(P450 → 알코올 → 알데하이드 탈수소효소)로 –COOH로 만들어 다이카복실산 → 양쪽에서 β-산화 → 숙신산·아디프산'),
    explain=key('β-산화가 막혔을 때 쓰는 보조 경로 (슬라이드 40).'))

# ================================================================ S13 (12) 케톤체
add(n=30, sec=12, diff=2, title='간 밖으로 운반되는 케톤체의 주 형태',
    en=mcq('Ketone bodies are formed in the liver and transported to extrahepatic tissues mainly as:', ['acetoacetyl-CoA.', 'acetone.', 'β-hydroxybutyric acid.', 'β-hydroxybutyryl-CoA.', 'lactic acid.']),
    ko=mcq('간에서 만든 케톤체가 주로 운반되는 형태는?', ['아세토아세틸-CoA', '아세톤', '<b>β-하이드록시뷰티르산</b>', 'β-하이드록시뷰티릴-CoA', '젖산']),
    answer=ans('C', 'β-hydroxybutyric acid', 'β-하이드록시뷰티르산 (혈중 가장 많음)'), explain=fig(ketone_make(), '') + warn('CoA가 붙은 형태(A·D)는 막을 못 지나 운반 불가. 아세톤은 소량, 호흡으로 배출.', '함정'))

add(n=31, sec=12, diff=1, title='아세토아세트산이 주로 만들어지는 곳',
    en=mcq('The major site of formation of acetoacetate from fatty acids is the:', ['adipose tissue.', 'intestinal mucosa.', 'kidney.', 'liver.', 'muscle.']),
    ko=mcq('지방산으로부터 아세토아세트산이 주로 만들어지는 곳은?', ['지방조직', '장 점막', '신장', '<b>간</b>', '근육']),
    answer=ans('D', 'liver', '간 (미토콘드리아)'), explain=key('간은 만들기만, 쓰지 못한다(β-케토아실-CoA 전이효소 없음).') + fig(ketone_use(), '간 외 조직의 사용'))

add(n=52, sec=12, diff=2, kind='SA', title='케톤체 구조와 소변에 많아지는 상황',
    en='<p>Draw the structure of one ketone body, and describe circumstances under which you would expect high concentrations of it in human urine.</p>', ko='<p>케톤체 하나의 구조를 그리고, 소변에 많이 나오는 상황을 설명하라.</p>',
    answer=sa('Acetoacetate CH₃–CO–CH₂–COO⁻ (also β-hydroxybutyrate CH₃–CH(OH)–CH₂–COO⁻, acetone CH₃–CO–CH₃). High in untreated diabetes and prolonged fasting, when fatty acids are the main fuel.', '아세토아세트산 CH₃–CO–CH₂–COO⁻ (β-하이드록시뷰티르산, 아세톤). 치료 안 된 당뇨, 장기 공복.'),
    explain=table(['케톤체', '구조'], [['아세토아세트산', 'CH₃–CO–CH₂–COO⁻'], ['D-β-하이드록시뷰티르산', 'CH₃–CH(OH)–CH₂–COO⁻'], ['아세톤', 'CH₃–CO–CH₃']]))

# ================================================================ S14 (13) 공복·당뇨
add(n=51, sec=13, diff=2, kind='SA', title='소변 케톤체 ↑ 환자',
    en='<p>A lab report shows a high concentration of ketone bodies in a patient’s urine. What disease would you suspect, and why do ketone bodies accumulate?</p>', ko='<p>소변 케톤체가 높게 나온 환자. 어떤 질환을 의심하며, 왜 케톤체가 쌓이나?</p>',
    answer=sa('Untreated diabetes (or fasting). Without usable glucose, the liver increases gluconeogenesis, withdrawing oxaloacetate from the citric acid cycle; acetyl-CoA from fatty acid oxidation cannot enter the cycle and is converted to ketone bodies, which are exported.', '치료 안 된 (1형) 당뇨 또는 공복. 포도당을 못 써 간이 당신생 ↑ → OAA가 빠져 TCA 정지 → 지방산 산화로 생긴 아세틸-CoA가 케톤체로.'),
    explain=fig(ketone_liver(), ''))
