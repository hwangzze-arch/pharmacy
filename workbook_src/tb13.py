# -*- coding: utf-8 -*-
"""13장 테스트뱅크 (lehninger6e_tb_ch13) — 강의 범위 문제만. 13.2 화학 반응 논리(친핵·친전자: 15, 16, 17, 43번)는 강의 범위 밖이라 제외."""
from helpers import *
from tblib import mcq, ans, sa
from exam13 import hill, ksign, std_state, two_step, redox_ladder_big, nad_svg, carbon_ox, atp_struct

DG = 'ΔG′°'
TB = []


def add(**kw):
    kw.setdefault('kind', 'MC')
    TB.append(kw)


def dg_k_table():
    return table(['K′eq', 'ln K′eq', 'ΔG′° = −RT ln K′eq', '방향'], [
        ['&gt; 1', '+', '<b>음수</b>', '정반응 쪽 (생성물 많음)'], ['= 1', '0', '0', '반반'], ['&lt; 1', '−', '<b>양수</b>', '역반응 쪽 (반응물 많음)']])


RT = 'RT = (8.315 J/mol·K)(298 K) = <b>2.48 kJ/mol</b>'

# ================================================================ S2 ATP (idx 1)
add(n=20, sec=1, diff=2, title='“고에너지” 화합물의 큰 −ΔG 이유가 아닌 것',
    en=mcq('All of the following contribute to the large, negative, free-energy change upon hydrolysis of “high-energy” compounds <b>except</b>:',
           ['electrostatic repulsion in the reactant.', 'low activation energy of forward reaction.', 'stabilization of products by extra resonance forms.', 'stabilization of products by ionization.', 'stabilization of products by solvation.']),
    ko=mcq('다음 중 “고에너지” 화합물이 가수분해될 때 ΔG가 크게 음수가 되는 이유가 <b>아닌</b> 것은?',
           ['반응물 속 전하끼리의 반발', '정반응의 낮은 활성화 에너지', '추가 공명 구조로 생성물이 안정해짐', '이온화로 생성물이 안정해짐', '용매화(물 분자에 둘러싸임)로 생성물이 안정해짐']),
    answer=ans('B', 'low activation energy of forward reaction', '정반응의 낮은 활성화 에너지'),
    explain=key('ΔG는 <b>출발점과 도착점의 높이 차</b>. 활성화 에너지는 중간에 넘는 <b>언덕</b> — 높이 차와 무관하고 속도만 정한다.') +
    fig(hill(), '') +
    steps('A·C·D·E는 모두 “반응물은 불안정, 생성물은 안정” → 높이 차를 키운다.',
          'B(활성화 에너지)는 반응이 <b>얼마나 빨리</b> 일어나는지에만 영향. ΔG와는 관계없다.') +
    tip('ATP 가수분해가 −30.5 kJ/mol인 4가지 이유: 전하 반발 ↓, 공명 ↑, 이온화, 용매화 (슬라이드 9–13).', '연결'))

add(n=21, sec=1, diff=1, title='ATP가 물속에서 안정한 이유',
    en=mcq(f'The hydrolysis of ATP has a large negative {DG}; nevertheless it is stable in solution due to:',
           ['entropy stabilization.', 'ionization of the phosphates.', 'resonance stabilization.', 'the hydrolysis reaction being endergonic.', 'the hydrolysis reaction having a large activation energy.']),
    ko=mcq(f'ATP 가수분해의 {DG}는 크게 음수인데도 ATP가 용액 속에서 안정한 이유는?',
           ['엔트로피 안정화', '인산기의 이온화', '공명 안정화', '가수분해가 흡에르곤 반응이라서', '가수분해의 <b>활성화 에너지가 커서</b>']),
    answer=ans('E', 'the hydrolysis reaction having a large activation energy', '가수분해 반응의 활성화 에너지가 크기 때문'),
    explain=key('“열역학적으로는 불안정, <b>속도론적으로는 안정</b>.” 언덕(Eₐ)이 높아 효소 없이는 거의 안 깨진다.') +
    fig(hill(), '') +
    steps('ΔG가 음수 = 내려갈 수 있다 ≠ 지금 바로 내려간다.', '효소가 언덕을 낮춰야 비로소 빠르게 가수분해 → 세포가 ATP를 <b>필요한 곳에서만</b> 쓸 수 있다.') +
    tip('높은 산 위의 바위: 떨어지면 에너지가 크지만, 앞에 턱(활성화 에너지)이 있어 가만히 있다.', '비유'))

# ================================================================ S3 ΔGp (idx 2)
add(n=44, sec=2, diff=2, kind='SA', title='세포 속 ATP 가수분해의 ΔG ≠ ΔG′°',
    en=f'<p>Why is the actual free energy (ΔG) of hydrolysis of ATP in the cell different from the standard free energy ({DG})?</p>',
    ko=f'<p>세포 안에서 ATP 가수분해의 실제 자유에너지(ΔG)가 표준 자유에너지({DG})와 다른 이유는?</p>',
    answer=sa('Concentrations of ATP, ADP, and Pᵢ are not 1 M (also pH, temperature, Mg²⁺ differ from standard).', 'ATP·ADP·Pᵢ 농도가 1 M이 아니고, pH·온도·Mg²⁺도 표준 조건과 다르기 때문'),
    explain=key(f'{DG}는 “모두 1 M”이라는 <b>가상의 조건</b>. 세포는 그렇지 않다.') +
    eq('ΔG = ΔG′° + RT ln ([ADP][Pᵢ] / [ATP])') +
    steps('세포에서 [ATP]는 높고 [ADP]·[Pᵢ]는 낮다 → ln 항이 음수 → ΔG가 더 음수.', '적혈구 예: ΔGp ≈ −52 kJ/mol (표준 −30.5보다 훨씬 큼).') +
    tip('세포 속 실제 값 ΔGp(인산화 퍼텐셜)는 보통 −50 ~ −65 kJ/mol (슬라이드 14).', '숫자'))

# ================================================================ S4 Gibbs (idx 3)
add(n=1, sec=3, diff=1, title='ΔG′°가 음수인 반응',
    en=mcq(f'If the {DG} of the reaction A → B is –40 kJ/mol, under standard conditions the reaction:',
           ['is at equilibrium.', 'will never reach equilibrium.', 'will not occur spontaneously.', 'will proceed at a rapid rate.', 'will proceed spontaneously from A to B.']),
    ko=mcq(f'A → B 반응의 {DG}가 −40 kJ/mol이면, 표준 조건에서 이 반응은?',
           ['평형 상태이다.', '절대 평형에 도달하지 않는다.', '자발적으로 일어나지 않는다.', '빠른 속도로 진행한다.', 'A에서 B로 자발적으로 진행한다.']),
    answer=ans('E', 'will proceed spontaneously from A to B', 'A → B로 자발적으로 진행한다'),
    explain=key('ΔG 음수 = <b>방향</b>(자발적)만 알려 준다. <b>속도</b>는 알려 주지 않는다.') +
    steps('표준 조건에서 ΔG = ΔG′° = −40 &lt; 0 → 정반응이 자발적.', 'D(빠르다)는 함정: 속도는 활성화 에너지·효소가 결정.') +
    warn('“자발적” ≠ “빠르다”. 시험 단골!', '함정'))

add(n=32, sec=3, diff=2, kind='SA', title='질서 · 엔트로피 · 자유에너지의 관계',
    en='<p>Explain the relationships among the change in the degree of order, the change in entropy, and the change in free energy that occur during a chemical reaction.</p>',
    ko='<p>화학 반응에서 질서도의 변화, 엔트로피 변화, 자유에너지 변화 사이의 관계를 설명하라.</p>',
    answer=sa('Entropy is a measure of disorder: more order → lower entropy. Since ΔG = ΔH − TΔS, an increase in entropy decreases free energy.',
              '엔트로피 = 무질서도. 질서가 늘면 엔트로피 ↓. ΔG = ΔH − TΔS이므로 엔트로피가 늘면(ΔS &gt; 0) 자유에너지는 줄어든다.'),
    explain=eq('ΔG = ΔH − TΔS') +
    table(['변화', 'ΔS', 'ΔG에 주는 영향'], [['더 무질서해짐 (분해, 퍼짐)', '+', '−TΔS가 음수 → ΔG ↓ (유리)'], ['더 질서 정연해짐 (합성, 정렬)', '−', '−TΔS가 양수 → ΔG ↑ (불리)']]) +
    steps('엔트로피(S) = 무질서한 정도. 방이 어지러워질수록 S ↑.', 'ΔS가 양수면 −TΔS가 음수가 되어 ΔG를 낮춘다 → 반응이 자발적 쪽으로.') +
    tip('생물은 질서(엔트로피 ↓)를 만들지만, 그 대가로 열과 작은 분자(CO₂, H₂O)를 내보내 <b>우주 전체</b>의 엔트로피는 늘린다.', '연결'))

# ================================================================ S5 standard states (idx 4)
add(n=36, sec=4, diff=2, kind='SA', title='ΔG와 ΔG′°의 차이',
    en=f'<p>What is the difference between ΔG and {DG} of a chemical reaction? Describe, quantitatively, the relationship between them.</p>',
    ko=f'<p>화학 반응의 ΔG와 {DG}의 차이는 무엇인가? 둘의 관계를 식으로 설명하라.</p>',
    answer=sa(f'{DG} is a constant (standard conditions); ΔG is a variable that depends on {DG}, temperature, and actual concentrations: ΔG = {DG} + RT ln([products]/[reactants]).',
              f'{DG}는 표준 조건에서의 <b>상수</b>, ΔG는 실제 농도·온도에 따라 바뀌는 <b>변수</b>. ΔG = {DG} + RT ln([생성물]/[반응물]).'),
    explain=fig(std_state(), '') + eq('ΔG = ΔG′° + RT ln Q') +
    steps('Q = 지금 순간의 [생성물]/[반응물].', 'Q = 1(모두 1 M)이면 ln Q = 0 → ΔG = ΔG′°.', '생성물이 적을수록(Q 작을수록) ΔG가 더 음수.') +
    tip('ΔG′° = 정가, ΔG = 오늘의 실제 가격(재고 상황에 따라 변함).', '비유'))

add(n=39, sec=4, diff=2, kind='SA', title='틀린 문장 고치기',
    en=f'<p>Explain why each of the following statements is false.</p><p>(a) In a reaction under standard conditions, only the reactants are fixed at 1 M.<br>(b) When {DG} is positive, K′eq &gt; 1.<br>(c) ΔG and {DG} mean the same thing.<br>(d) When {DG} = 1.0 kJ/mol, K′eq = 1.</p>',
    ko=f'<p>다음 문장이 각각 왜 틀렸는지 설명하라.</p><p>(a) 표준 조건에서는 반응물만 1 M으로 고정된다.<br>(b) {DG}가 양수이면 K′eq &gt; 1이다.<br>(c) ΔG와 {DG}는 같은 뜻이다.<br>(d) {DG} = 1.0 kJ/mol이면 K′eq = 1이다.</p>',
    answer=sa(f'(a) Reactants AND products are 1 M. (b) {DG} &gt; 0 → K′eq &lt; 1. (c) {DG} is a constant; ΔG depends on actual conditions. (d) K′eq = 1 only when {DG} = 0; at +1.0 kJ/mol, K′eq &lt; 1 (≈ 0.67).',
              f'(a) 반응물·생성물 <b>모두</b> 1 M. (b) {DG} &gt; 0이면 K′eq &lt; 1. (c) {DG}는 상수, ΔG는 실제 조건의 변수. (d) K′eq = 1은 {DG} = 0일 때뿐. +1.0이면 K′eq ≈ 0.67 (&lt; 1).'),
    explain=dg_k_table() + eq('ΔG′° = −RT ln K′eq') +
    steps('(d) 계산: ln K′eq = −1.0 / 2.48 = −0.40 → K′eq = e<sup>−0.40</sup> ≈ <b>0.67</b>.') +
    warn('테스트뱅크 해설의 (b)에 “ΔG′° &lt; 0”이라고 오타가 있어. 올바른 내용은 “ΔG′° &gt; 0 → K′eq &lt; 1”.', '자료 오타'))

# ================================================================ S6 ΔG′° & K (idx 5)
add(n=2, sec=5, diff=1, title='평형에 도달하지 못한 반응',
    en=mcq(f'For the reaction A → B, {DG} = –60 kJ/mol. The reaction is started with 10 mmol of A; no B is initially present. After 24 hours, analysis reveals the presence of 2 mmol of B, 8 mmol of A. Which is the most likely explanation?',
           ['A and B have reached equilibrium concentrations.', 'An enzyme has shifted the equilibrium toward A.', 'B formation is kinetically slow; equilibrium has not been reached by 24 hours.', 'Formation of B is thermodynamically unfavorable.', f'The result described is impossible, given the fact that {DG} is –60 kJ/mol.']),
    ko=mcq(f'A → B의 {DG} = −60 kJ/mol. A 10 mmol로 시작(B 없음). 24시간 뒤 B 2 mmol, A 8 mmol. 가장 그럴듯한 설명은?',
           ['A와 B가 평형 농도에 도달했다.', '효소가 평형을 A 쪽으로 옮겼다.', 'B 생성이 <b>느려서</b> 24시간 동안 평형에 도달하지 못했다.', 'B 생성은 열역학적으로 불리하다.', f'{DG}가 −60이므로 이 결과는 불가능하다.']),
    answer=ans('C', 'B formation is kinetically slow; equilibrium has not been reached', 'B 생성이 느려(속도론) 아직 평형에 도달하지 않았다'),
    explain=key(f'{DG} −60 → K′eq ≈ 10<sup>10</sup>: 평형이면 B가 거의 전부여야 한다. 아직 8 mmol의 A가 있다 = <b>아직 가는 중</b>.') +
    steps('A(평형)는 틀림: 평형이면 B/A ≈ 10<sup>10</sup>.', 'B(효소가 평형 이동)는 틀림: 효소는 속도만 바꾸고 평형은 못 바꾼다.', 'E(불가능)는 틀림: 열역학은 방향만, 속도는 모른다.') +
    tip('내리막 길이라도 길이 험하면(활성화 에너지 큼) 천천히 내려간다.', '비유'))

add(n=6, sec=5, diff=1, title='A + B → C, ΔG′° = −20 kJ/mol',
    en=mcq(f'The reaction A + B → C has a {DG} of –20 kJ/mol at 25 °C. Starting under standard conditions, one can predict that:',
           ['at equilibrium, the concentration of B will exceed the concentration of A.', 'at equilibrium, the concentration of C will be less than the concentration of A.', 'at equilibrium, the concentration of C will be much greater than the concentration of A or B.', 'C will rapidly break down to A + B.', 'when A and B are mixed, the reaction will proceed rapidly toward formation of C.']),
    ko=mcq(f'25 °C에서 A + B → C의 {DG} = −20 kJ/mol. 표준 조건에서 시작할 때 예측할 수 있는 것은?',
           ['평형에서 [B] &gt; [A]', '평형에서 [C] &lt; [A]', '평형에서 [C]가 [A]나 [B]보다 <b>훨씬 크다</b>', 'C가 빠르게 A + B로 분해된다', 'A와 B를 섞으면 C 쪽으로 빠르게 진행한다']),
    answer=ans('C', 'at equilibrium, [C] will be much greater than [A] or [B]', '평형에서 C의 농도가 A나 B보다 훨씬 크다'),
    explain=eq('K′eq = e<sup>−ΔG′°/RT</sup> = e<sup>20/2.48</sup> = e<sup>8.07</sup> ≈ 3 × 10<sup>3</sup>') +
    steps('K′eq ≫ 1 → 평형에서 생성물(C)이 압도적으로 많다.', 'E는 “빠르게”가 함정 — 속도는 알 수 없다.', 'A는 판단 불가: A와 B는 1:1로 같이 소모돼서 둘의 비는 처음과 같다.') +
    key('ΔG′° 음수 ↔ K′eq &gt; 1 ↔ 생성물 쪽'))

add(n=9, sec=5, diff=1, title='K′eq = 10⁴',
    en=mcq('For the reaction A → B, the K′eq is 10<sup>4</sup>. If a reaction mixture originally contains 1 mmol of A and no B, which one of the following must be true?',
           ['At equilibrium, there will be far more B than A.', 'The rate of the reaction is very slow.', 'The reaction requires coupling to an exergonic reaction in order to proceed.', 'The reaction will proceed toward B at a very high rate.', f'{DG} for the reaction will be large and positive.']),
    ko=mcq('A → B의 K′eq = 10<sup>4</sup>. A 1 mmol, B 0으로 시작하면 반드시 참인 것은?',
           ['평형에서 B가 A보다 <b>훨씬 많다</b>', '반응 속도가 매우 느리다', '진행하려면 발에르곤 반응과 짝지어야 한다', '매우 빠르게 B 쪽으로 진행한다', f'{DG}가 크게 양수이다']),
    answer=ans('A', 'At equilibrium, there will be far more B than A', '평형에서 B가 A보다 훨씬 많다 ([B]/[A] = 10,000)'),
    explain=fig(ksign(), '') + steps('K′eq = [B]/[A] = 10⁴ → B가 A의 1만 배.', f'{DG} = −2.48 × ln 10⁴ = −2.48 × 9.21 ≈ <b>−22.8 kJ/mol</b> (음수 → E 틀림).', 'B·D: 속도는 K로 알 수 없다.') +
    key('K는 “어디로 가는가”, 속도는 “얼마나 빨리”. 별개!'))

add(n=10, sec=5, diff=1, title='K′eq = 10⁻⁶ (정답 2개)',
    en=mcq('For the reaction A → B, the K′eq is 10<sup>−6</sup>. If a reaction mixture originally contains 1 mmol of A and 1 mmol of B, which one of the following must be true?',
           ['At equilibrium, there will still be equal levels of A and B.', 'The rate of the reaction is very slow.', 'At equilibrium, the amount of A will greatly exceed the amount of B.', 'The reaction will proceed toward B at a very high rate.', f'{DG} for the reaction will be large and positive.']),
    ko=mcq('A → B의 K′eq = 10<sup>−6</sup>. A 1 mmol, B 1 mmol로 시작하면 반드시 참인 것은?',
           ['평형에서도 A와 B는 같다', '반응 속도가 매우 느리다', '평형에서 A가 B보다 <b>훨씬 많다</b>', '매우 빠르게 B 쪽으로 진행한다', f'{DG}가 <b>크게 양수</b>이다']),
    answer=ans('C, E', 'A will greatly exceed B at equilibrium; ΔG′° is large and positive', '평형에서 A ≫ B, 그리고 ΔG′°는 크게 양수 (정답 2개)'),
    explain=fig(ksign(), '') + steps('[B]/[A] = 10⁻⁶ → A가 B의 100만 배 → C 참.', f'{DG} = −2.48 × ln 10⁻⁶ = −2.48 × (−13.8) ≈ <b>+34 kJ/mol</b> → E 참.', '처음 1:1이었으므로 반응은 B → A(역방향)로 진행한다.') +
    warn('교수님 자료에 정답이 C, E 두 개로 되어 있어. “하나만 고르라”는 문장과 다르니 둘 다 기억!', '주의'))

add(n=33, sec=5, diff=2, kind='SA', title='K′eq가 큰 수일 때 ΔG′°는?',
    en=f'<p>Consider the reaction: A + B → C + D. If the equilibrium constant for this reaction is a large number (say, 10,000), what do we know about the standard free-energy change ({DG}) for the reaction? Describe the relationship between K′eq and {DG}.</p>',
    ko=f'<p>A + B → C + D의 평형상수가 큰 수(예: 10,000)라면 {DG}에 대해 무엇을 알 수 있는가? K′eq와 {DG}의 관계를 설명하라.</p>',
    answer=sa(f'{DG} = −RT ln K′eq. A large K′eq gives a large negative {DG} (≈ −22.8 kJ/mol for 10⁴).', f'{DG} = −RT ln K′eq. K′eq가 크면 {DG}는 크게 음수 (10⁴이면 약 −22.8 kJ/mol).'),
    explain=dg_k_table() + steps('ln 10,000 = 9.21', f'{DG} = −2.48 × 9.21 = <b>−22.8 kJ/mol</b>') +
    tip('K가 10배 커질 때마다 ΔG′°는 약 5.7 kJ/mol씩 더 음수가 된다 (25 °C).', '외우기'))

add(n=3, sec=5, diff=2, title='평형에서 2-PG가 3-PG의 6배',
    en=mcq(f'When a mixture of 3-phosphoglycerate and 2-phosphoglycerate is incubated at 25 °C with phosphoglycerate mutase until equilibrium is reached, the final mixture contains six times as much 2-phosphoglycerate as 3-phosphoglycerate. Which statement is most nearly correct for 3-phosphoglycerate → 2-phosphoglycerate? (R = 8.315 J/mol·K; T = 298 K)',
           [f'{DG} is –4.44 kJ/mol.', f'{DG} is zero.', f'{DG} is +12.7 kJ/mol.', f'{DG} is incalculably large and positive.', f'{DG} cannot be calculated from the information given.']),
    ko=mcq('3-포스포글리세르산(3-PG)과 2-PG를 포스포글리세르산 뮤테이스와 25 °C에서 평형까지 두었더니 2-PG가 3-PG의 6배였다. 3-PG → 2-PG 반응에 대해 가장 맞는 것은?',
           [f'{DG} = −4.44 kJ/mol', f'{DG} = 0', f'{DG} = +12.7 kJ/mol', f'{DG}가 계산할 수 없을 만큼 크고 양수', '주어진 정보로 계산 불가']),
    answer=ans('A', f'{DG} is –4.44 kJ/mol', f'{DG} = −4.44 kJ/mol'),
    explain=align([('K′eq', '[2-PG]/[3-PG] = 6', ''), ('ΔG′°', '−RT ln K′eq', ''), ('', '−(2.48 kJ/mol)(ln 6)', ''), ('', '−(2.48)(1.79) = <b>−4.44 kJ/mol</b>', '')]) +
    key('평형 농도비 = K′eq. 생성물이 더 많으면(K &gt; 1) ΔG′°는 음수.'))

add(n=4, sec=5, diff=2, title='평형에서 G6P가 F6P의 2배',
    en=mcq(f'When a mixture of glucose 6-phosphate and fructose 6-phosphate is incubated with phosphohexose isomerase until equilibrium is reached, the final mixture contains twice as much glucose 6-phosphate as fructose 6-phosphate. Which statement best applies to glucose 6-phosphate → fructose 6-phosphate? (R = 8.315 J/mol·K; T = 298 K)',
           [f'{DG} is incalculably large and negative.', f'{DG} is –1.72 kJ/mol.', f'{DG} is zero.', f'{DG} is +1.72 kJ/mol.', f'{DG} is incalculably large and positive.']),
    ko=mcq('G6P와 F6P를 포스포헥소스 이성질화효소와 평형까지 두었더니 G6P가 F6P의 2배였다. G6P → F6P에 대해 가장 맞는 것은?',
           [f'{DG}가 계산 불가할 만큼 크고 음수', f'{DG} = −1.72 kJ/mol', f'{DG} = 0', f'{DG} = +1.72 kJ/mol', f'{DG}가 계산 불가할 만큼 크고 양수']),
    answer=ans('D', f'{DG} is +1.72 kJ/mol', f'{DG} = +1.72 kJ/mol'),
    explain=align([('K′eq', '[F6P]/[G6P] = 1/2 = 0.5', ''), ('ΔG′°', '−(2.48)(ln 0.5)', ''), ('', '−(2.48)(−0.693) = <b>+1.72 kJ/mol</b>', '')]) +
    warn('K′eq는 항상 <b>생성물/반응물</b>. 반응식 방향(G6P → F6P)을 보고 분자에 F6P를 놓아야 해. 거꾸로 놓으면 B(−1.72)를 고르게 된다.', '함정') +
    tip('해당과정 2단계(14장)의 실제 값이 +1.7 kJ/mol.', '연결'))

add(n=5, sec=5, diff=1, title='G6P 가수분해가 99% 진행',
    en=mcq('Hydrolysis of 1 M glucose 6-phosphate catalyzed by glucose 6-phosphatase is 99% complete at equilibrium (i.e., only 1% of the substrate remains). Which of the following statements is most nearly correct? (R = 8.315 J/mol·K; T = 298 K)',
           [f'{DG} is –11 kJ/mol.', f'{DG} is –5 kJ/mol.', f'{DG} is 0 kJ/mol.', f'{DG} is +11 kJ/mol.', f'{DG} cannot be determined from the information given.']),
    ko=mcq('1 M 포도당 6-인산을 포도당 6-인산가수분해효소로 가수분해하면 평형에서 99%가 반응했다(1%만 남음). 가장 맞는 것은?',
           [f'{DG} = −11 kJ/mol', f'{DG} = −5 kJ/mol', f'{DG} = 0', f'{DG} = +11 kJ/mol', '알 수 없다']),
    answer=ans('A', f'{DG} is –11 kJ/mol', f'{DG} ≈ −11 kJ/mol'),
    explain=align([('평형 농도', '[G6P] = 0.01 M, [포도당] = [Pᵢ] = 0.99 M', ''), ('K′eq', '(0.99)(0.99)/0.01 ≈ 98', ''), ('ΔG′°', '−(2.48)(ln 98) = −(2.48)(4.58) ≈ <b>−11.4 kJ/mol</b>', '')]) +
    tip('간단히 99/1 ≈ 99로 해도 ln 99 = 4.6 → −11.4. 답은 같다.', '빠르게'))

add(n=35, sec=5, diff=3, kind='SA', title='G1P → G6P의 K′eq와 ΔG′° 계산',
    en=f'<p>If a 0.1 M solution of glucose 1-phosphate is incubated with a catalytic amount of phosphoglucomutase, glucose 1-phosphate is transformed to glucose 6-phosphate until equilibrium is reached. At equilibrium, [glucose 1-phosphate] = 4.5 × 10<sup>−3</sup> M and [glucose 6-phosphate] = 8.6 × 10<sup>−2</sup> M. Set up the expressions for the calculation of K′eq and {DG} for this reaction (in the direction of glucose 6-phosphate formation). (R = 8.315 J/mol·K; T = 298 K)</p>',
    ko=f'<p>0.1 M 포도당 1-인산(G1P)을 소량의 포스포글루코뮤테이스와 두면 평형까지 G6P로 바뀐다. 평형에서 [G1P] = 4.5 × 10<sup>−3</sup> M, [G6P] = 8.6 × 10<sup>−2</sup> M. G6P가 생기는 방향으로 K′eq와 {DG}를 구하는 식을 세워라.</p>',
    answer=sa(f'K′eq = [G6P]/[G1P] = 0.086/0.0045 ≈ 19; {DG} = −RT ln K′eq = −(8.315)(298)(ln 19) ≈ −7.3 kJ/mol', f'K′eq ≈ 19, {DG} ≈ −7.3 kJ/mol'),
    explain=align([('K′eq', '0.086 / 0.0045 = <b>19.1</b>', ''), ('ln 19.1', '2.95', ''), ('ΔG′°', '−(8.315 J/mol·K)(298 K)(2.95)', ''), ('', '= −7,300 J/mol = <b>−7.3 kJ/mol</b>', '')]) +
    warn('R의 단위는 J. 마지막에 1000으로 나눠 kJ로 바꾸는 걸 잊지 말자.', '함정') +
    tip('교과서 값 −7.3 kJ/mol (글리코겐 분해 후 G1P → G6P, 15장).', '연결'))

add(n=34, sec=5, diff=2, kind='SA', title='ATP·ADP·Pᵢ 모두 1 M에서 시작하면?',
    en=f'<p>The standard free energy change ({DG}) for ATP hydrolysis is –30.5 kJ/mol. ATP, ADP, and Pᵢ are mixed together at initial concentrations of 1 M each, then left alone until the reaction ADP + Pᵢ → ATP has come to equilibrium. For each species, indicate whether the concentration will be equal to 1 M, less than 1 M, or greater than 1 M.</p>',
    ko=f'<p>ATP 가수분해의 {DG} = −30.5 kJ/mol. ATP, ADP, Pᵢ를 각각 1 M로 섞고 ADP + Pᵢ → ATP 반응이 평형에 이를 때까지 두었다. 각 물질의 농도는 1 M과 같은가, 작은가, 큰가?</p>',
    answer=sa('ATP &lt; 1 M; ADP &gt; 1 M; Pᵢ &gt; 1 M', 'ATP는 1 M보다 작고, ADP와 Pᵢ는 1 M보다 크다'),
    explain=key('ADP + Pᵢ → ATP의 ΔG′° = <b>+30.5</b> (가수분해의 반대) → 실제로는 <b>ATP가 분해되는 쪽</b>으로 간다.') +
    steps('출발점 = 표준 조건(모두 1 M) → ΔG = ΔG′° = +30.5 → 쓰여진 방향은 불리.', '그래서 반대 방향(ATP → ADP + Pᵢ)으로 진행 → ATP ↓, ADP ↑, Pᵢ ↑.') +
    warn('문제의 반응식 방향(합성)을 보고 ATP가 늘어난다고 착각하기 쉽다.', '함정'))

add(n=37, sec=5, diff=2, kind='SA', title='ΔG = ΔG′° + RT ln K′eq가 틀린 이유',
    en=f'<p>The expression ΔG = {DG} + RT ln K′eq for the actual free-energy change for the reaction A + B → C + D is incorrect. Why is it wrong, and what is the correct expression?</p>',
    ko=f'<p>A + B → C + D의 실제 자유에너지 변화를 ΔG = {DG} + RT ln K′eq로 쓰는 것은 틀렸다. 왜 틀렸고, 올바른 식은?</p>',
    answer=sa(f'Correct: ΔG = {DG} + RT ln([C][D]/[A][B]) using actual concentrations. K′eq is only valid at equilibrium, where ΔG = 0.',
              f'올바른 식: ΔG = {DG} + RT ln([C][D]/[A][B]) (실제 농도). K′eq를 넣는 것은 평형일 때만 맞고, 그때 ΔG = 0.'),
    explain=eq('ΔG = ΔG′° + RT ln Q &nbsp; (Q = 지금의 농도비)', '평형이면 Q = K′eq, ΔG = 0 → ΔG′° = −RT ln K′eq') +
    steps('Q는 순간순간 변하는 실제 비율, K′eq는 평형에서만의 고정값.', '둘을 혼동하면 ΔG가 늘 0이 되어 버린다.') +
    key('“ln 뒤에는 Q(실제), K는 평형에서만”'))

add(n=8, sec=5, diff=1, title='ΔG′° = +29.7인 말산 탈수소효소 반응',
    en=mcq(f'For the following reaction, {DG} = +29.7 kJ/mol.<br>L-Malate + NAD<sup>+</sup> → oxaloacetate + NADH + H<sup>+</sup><br>The reaction as written:',
           ['can never occur in a cell.', f'can occur in a cell only if it is coupled to another reaction for which {DG} is positive.', 'can occur only in a cell in which NADH is converted to NAD<sup>+</sup> by electron transport.', 'cannot occur because of its large activation energy.', 'may occur in cells at some concentrations of substrate and product.']),
    ko=mcq(f'L-말산 + NAD⁺ → 옥살로아세트산 + NADH + H⁺, {DG} = +29.7 kJ/mol. 이 반응은?',
           ['세포에서 절대 일어날 수 없다', f'{DG}가 양수인 다른 반응과 짝지을 때만 일어난다', 'NADH가 전자전달로 NAD⁺로 바뀌는 세포에서만 일어난다', '활성화 에너지가 커서 일어날 수 없다', '기질·생성물 <b>농도에 따라</b> 세포에서 일어날 수 있다']),
    answer=ans('E', 'may occur in cells at some concentrations of substrate and product', '기질과 생성물의 농도에 따라 세포에서 일어날 수 있다'),
    explain=eq('ΔG = +29.7 + RT ln ([OAA][NADH] / [말산][NAD⁺])') +
    steps('세포 속 [OAA]는 아주 낮다(다음 반응인 시트르산 생성효소가 바로 써 버림).', 'ln 항이 크게 음수 → ΔG ≈ 0 또는 음수 → 진행.') +
    tip('16장 TCA 8단계: ΔG′° +29.7인데도 잘 돈다 — 바로 이 이유.', '연결'))

add(n=11, sec=5, diff=2, title='알돌레이스 (ΔG′° = +23.8) 진행 조건',
    en=mcq(f'In glycolysis, fructose 1,6-bisphosphate is converted to two products with a standard free-energy change ({DG}) of 23.8 kJ/mol. Under what conditions encountered in a normal cell will the free-energy change (ΔG) be negative, enabling the reaction to proceed spontaneously to the right?',
           ['Under standard conditions, enough energy is released to drive the reaction to the right.', f'The reaction will not go to the right spontaneously under any conditions because the {DG} is positive.', 'The reaction will proceed spontaneously to the right if there is a high concentration of products relative to the concentration of fructose 1,6-bisphosphate.', 'The reaction will proceed spontaneously to the right if there is a high concentration of fructose 1,6-bisphosphate relative to the concentration of products.', 'None of the above conditions is sufficient.']),
    ko=mcq(f'해당과정에서 과당 1,6-이인산(FBP)이 두 산물로 쪼개지는 반응의 {DG} = +23.8 kJ/mol. 정상 세포의 어떤 조건에서 ΔG가 음수가 되어 오른쪽으로 자발적으로 진행하나?',
           ['표준 조건에서도 충분한 에너지가 나와 오른쪽으로 진행한다', f'{DG}가 양수라 어떤 조건에서도 오른쪽으로 자발적으로 가지 않는다', '생성물 농도가 FBP보다 높으면 오른쪽으로 진행한다', '<b>FBP 농도가 생성물보다 높으면</b> 오른쪽으로 진행한다', '위의 어떤 조건도 충분하지 않다']),
    answer=ans('D', 'if [fructose 1,6-bisphosphate] is high relative to [products]', 'FBP가 생성물보다 훨씬 많으면 오른쪽으로 진행',
               note='⚠️ 테스트뱅크 정답 표기는 “A”이지만, ΔG′° = +23.8 &gt; 0이라 표준 조건에서는 오른쪽으로 가지 않아. 식으로 보면 정답은 D. 시험에서 같은 문제가 나오면 교수님께 확인해 보자.'),
    explain=eq('ΔG = +23.8 + RT ln ([DHAP][GAP] / [FBP])') +
    steps('ln 항을 크게 음수로 만들려면 분모(FBP) ↑, 분자(생성물) ↓.', '세포에서는 GAP가 다음 단계로 바로 쓰여 낮게 유지 → 실제 ΔG ≈ −6 kJ/mol (14장).', 'A는 틀림(표준 조건에서는 ΔG = +23.8), C는 반대.') +
    key('ΔG′°가 양수여도 <b>반응물 ↑, 생성물 ↓</b>면 진행한다.'))

add(n=38, sec=5, diff=3, kind='SA', title='시트르산 → 아이소시트르산 (ΔG′° = +13.3)',
    en=f'<p>Explain in quantitative terms the circumstances under which the following reaction can proceed.<br>Citrate → isocitrate &nbsp; {DG} = +13.3 kJ/mol</p>',
    ko=f'<p>다음 반응이 진행할 수 있는 조건을 정량적으로 설명하라.<br>시트르산 → 아이소시트르산 &nbsp; {DG} = +13.3 kJ/mol</p>',
    answer=sa('It proceeds when ΔG &lt; 0: ΔG = +13.3 + RT ln([isocitrate]/[citrate]). If [isocitrate] is kept very low (removed by the next step), the log term is negative enough.',
              'ΔG &lt; 0이면 진행. ΔG = +13.3 + RT ln([아이소시트르산]/[시트르산]). 다음 단계가 아이소시트르산을 계속 치워 낮게 유지하면 ln 항이 충분히 음수가 된다.'),
    explain=steps('ΔG &lt; 0 이 되려면 RT ln Q &lt; −13.3 → ln Q &lt; −13.3/2.48 = −5.36', 'Q &lt; e<sup>−5.36</sup> ≈ <b>0.0047</b> → [아이소시트르산]/[시트르산] &lt; 약 1/200') +
    key('“정량적으로” = 비율이 약 1:200보다 작으면 진행한다고 숫자로 말하기.') +
    tip('세포에서는 아이소시트르산 탈수소효소(ΔG′° −20.9)가 곧바로 끌어간다 (16장).', '연결'))

# ================================================================ S7 additivity (idx 6)
add(n=12, sec=6, diff=2, title='G1P → G6P → F6P 전체 ΔG′°',
    en=mcq(f'During glycolysis, glucose 1-phosphate is converted to fructose 6-phosphate in two successive reactions:<br>Glucose 1-phosphate → glucose 6-phosphate &nbsp; {DG} = –7.1 kJ/mol<br>Glucose 6-phosphate → fructose 6-phosphate &nbsp; {DG} = +1.7 kJ/mol<br>{DG} for the overall reaction is:',
           ['–8.8 kJ/mol', '–7.1 kJ/mol', '–5.4 kJ/mol', '+5.4 kJ/mol', '+8.8 kJ/mol']),
    ko=mcq(f'G1P → G6P ({DG} −7.1), G6P → F6P ({DG} +1.7). 전체 반응 G1P → F6P의 {DG}는?', ['−8.8', '−7.1', '−5.4', '+5.4', '+8.8']),
    answer=ans('C', '–5.4 kJ/mol', '−5.4 kJ/mol'),
    explain=align([('G1P → G6P', '−7.1', ''), ('G6P → F6P', '+1.7', ''), ('G1P → F6P', '−7.1 + 1.7 = <b>−5.4 kJ/mol</b>', '')]) +
    key('반응식을 더하면 ΔG′°도 그대로 더한다 (가산성).'))

add(n=13, sec=6, diff=2, title='포스포크레아틴 + ADP → 크레아틴 + ATP',
    en=mcq(f'Phosphocreatine → creatine + Pᵢ &nbsp; {DG} = –43.0 kJ/mol<br>ATP → ADP + Pᵢ &nbsp; {DG} = –30.5 kJ/mol<br>What is the overall {DG} for: Phosphocreatine + ADP → creatine + ATP?',
           ['–73.5 kJ/mol', '–12.5 kJ/mol', '+12.5 kJ/mol', '+73.5 kJ/mol', f'{DG} cannot be calculated without K′eq.']),
    ko=mcq(f'포스포크레아틴 가수분해 −43.0, ATP 가수분해 −30.5. 포스포크레아틴 + ADP → 크레아틴 + ATP의 {DG}는?', ['−73.5', '−12.5', '+12.5', '+73.5', 'K′eq 없이는 계산 불가']),
    answer=ans('B', '–12.5 kJ/mol', '−12.5 kJ/mol'),
    explain=align([('포스포크레아틴 → 크레아틴 + Pᵢ', '−43.0', ''), ('ADP + Pᵢ → ATP (뒤집음)', '+30.5', ''), ('합계', '−43.0 + 30.5 = <b>−12.5 kJ/mol</b>', '')]) +
    steps('ATP를 <b>만드는</b> 쪽이니 ATP 가수분해 식을 뒤집고 부호도 바꾼다.') +
    tip('근육은 포스포크레아틴으로 ATP를 몇 초간 빠르게 재충전 (크레아틴 키네이스).', '연결'))

add(n=14, sec=6, diff=2, title='아세틸-CoA 가수분해의 ΔG′°',
    en=mcq(f'OAA + acetyl-CoA + H₂O → citrate + CoASH &nbsp; {DG} = –32.2 kJ/mol (citrate synthase)<br>OAA + acetate → citrate &nbsp; {DG} = –1.9 kJ/mol (citrate lyase)<br>What is the {DG} for the hydrolysis of acetyl-CoA: Acetyl-CoA + H₂O → acetate + CoASH + H<sup>+</sup>?',
           ['–34.1 kJ/mol', '–32.2 kJ/mol', '–30.3 kJ/mol', '+61.9 kJ/mol', '+34.1 kJ/mol']),
    ko=mcq(f'시트르산 생성효소 반응 −32.2, 시트르산 분해효소 반응(OAA + 아세트산 → 시트르산) −1.9. 아세틸-CoA 가수분해의 {DG}는?', ['−34.1', '−32.2', '−30.3', '+61.9', '+34.1']),
    answer=ans('C', '–30.3 kJ/mol', '−30.3 kJ/mol'),
    explain=align([('OAA + 아세틸-CoA + H₂O → 시트르산 + CoA', '−32.2', ''), ('시트르산 → OAA + 아세트산 (두 번째 식 뒤집음)', '+1.9', ''), ('아세틸-CoA + H₂O → 아세트산 + CoA', '−32.2 + 1.9 = <b>−30.3</b>', '')]) +
    steps('원하는 식에 OAA·시트르산이 없으니, 둘이 지워지도록 두 번째 식을 뒤집어 더한다.') +
    key('티오에스터(아세틸-CoA) 가수분해 ≈ −31.4 kJ/mol — ATP급 고에너지 (슬라이드 32).'))

add(n=41, sec=6, diff=2, kind='SA', title='“표준 자유에너지 변화는 더할 수 있다”',
    en='<p>Explain what is meant by the statement: “Standard free-energy changes are additive.” Give an example of the usefulness of this additive property in understanding how cells carry out thermodynamically unfavorable chemical reactions.</p>',
    ko='<p>“표준 자유에너지 변화는 더할 수 있다”는 말의 뜻을 설명하고, 이 성질이 세포가 열역학적으로 불리한 반응을 어떻게 수행하는지 이해하는 데 어떻게 쓰이는지 예를 들어라.</p>',
    answer=sa('If two reactions sum to a third, the ΔG′° of the third is the sum of the two. E.g., glucose + Pᵢ → G6P (+13.8) coupled with ATP → ADP + Pᵢ (−30.5) gives glucose + ATP → G6P + ADP (−16.7): unfavorable made favorable.',
              '두 반응을 더해 세 번째 반응이 되면 ΔG′°도 더한 값. 예: 포도당 + Pᵢ → G6P (+13.8)에 ATP 가수분해(−30.5)를 짝지으면 포도당 + ATP → G6P + ADP (−16.7) → 불리한 반응이 유리해진다.'),
    explain=align([('포도당 + Pᵢ → G6P', '+13.8', '불리'), ('ATP → ADP + Pᵢ', '−30.5', ''), ('포도당 + ATP → G6P + ADP', '<b>−16.7</b>', '유리 (헥소키나아제)')]) +
    key('세포의 전략 = <b>짝지음(coupling)</b>: 불리한 반응에 ATP 가수분해를 더해 전체를 음수로.'))

add(n=42, sec=6, diff=2, kind='SA', title='ATP + 포도당 → G6P + ADP의 ΔG′°',
    en=f'<p>Given {DG}: (1) ATP → ADP + Pᵢ, −30.5 kJ/mol; (2) glucose 6-phosphate → glucose + Pᵢ, −13.8 kJ/mol. Show how you would calculate {DG} for (3) ATP + glucose → glucose 6-phosphate + ADP.</p>',
    ko=f'<p>(1) ATP → ADP + Pᵢ, −30.5 kJ/mol, (2) G6P → 포도당 + Pᵢ, −13.8 kJ/mol. (3) ATP + 포도당 → G6P + ADP의 {DG}를 구하는 방법을 보여라.</p>',
    answer=sa(f'(3) = (1) + reverse of (2): {DG} = −30.5 + 13.8 = −16.7 kJ/mol', f'(3) = (1) + (2)의 역반응: {DG} = −30.5 + 13.8 = <b>−16.7 kJ/mol</b>'),
    explain=align([('ATP → ADP + Pᵢ', '−30.5', ''), ('포도당 + Pᵢ → G6P (2 뒤집음)', '+13.8', ''), ('ATP + 포도당 → ADP + G6P', '<b>−16.7 kJ/mol</b>', '')]) +
    steps('양변의 Pᵢ가 지워지는지 확인 → 맞게 더한 것.') + tip('반응을 뒤집으면 ΔG′°의 부호만 바뀐다.', '규칙'))

add(n=40, sec=6, diff=3, kind='SA', title='피루브산 키나아제의 K′eq',
    en=f'<p>Pyruvate kinase catalyzes: Phosphoenolpyruvate + ADP → pyruvate + ATP. Given (1) ATP → ADP + Pᵢ, {DG} = −30.5 kJ/mol and (2) PEP → pyruvate + Pᵢ, {DG} = −61.9 kJ/mol, show how you would calculate the equilibrium constant. (R = 8.315 J/mol·K; T = 298 K)</p>',
    ko=f'<p>피루브산 키나아제: PEP + ADP → 피루브산 + ATP. (1) ATP 가수분해 −30.5, (2) PEP → 피루브산 + Pᵢ −61.9 kJ/mol일 때 평형상수를 구하는 방법을 보여라.</p>',
    answer=sa(f'{DG} = −61.9 + 30.5 = −31.4 kJ/mol; ln K′eq = 31,400/(8.315 × 298) = 12.67; K′eq ≈ 3.2 × 10⁵',
              f'{DG} = −31.4 kJ/mol → ln K′eq = 12.67 → K′eq ≈ <b>3.2 × 10⁵</b>'),
    explain=align([('PEP → 피루브산 + Pᵢ', '−61.9', ''), ('ADP + Pᵢ → ATP', '+30.5', ''), ('PEP + ADP → 피루브산 + ATP', '<b>−31.4 kJ/mol</b>', ''),
                   ('ln K′eq', '−ΔG′°/RT = 31,400 / 2,478 = 12.67', ''), ('K′eq', 'e<sup>12.67</sup> ≈ <b>3.2 × 10⁵</b>', '')]) +
    key('① 가산성으로 ΔG′° → ② K′eq = e<sup>−ΔG′°/RT</sup>. 두 단계 조합 문제.'))

# ================================================================ S8 group transfer (idx 7)
add(n=18, sec=7, diff=2, title='ATP → ADP + Pᵢ 반응의 종류',
    en=mcq('The reaction ATP → ADP + Pᵢ is an example of a ______ reaction.', ['homolytic cleavage', 'internal rearrangement', 'free radical', 'group transfer', 'oxidation/reduction']),
    ko=mcq('ATP → ADP + Pᵢ 반응은 어떤 종류의 반응인가?', ['균일 분해', '분자 내 재배열', '자유 라디칼', '<b>작용기 전달</b>', '산화-환원']),
    answer=ans('D', 'group transfer', '작용기 전달 반응 (인산기를 물에 전달)'),
    explain=key('가수분해 = 인산기(작용기)를 <b>물</b>에게 넘기는 것. 그래서 작용기 전달.') +
    steps('전자의 이동이 없으므로 산화-환원(E)이 아니다.', '라디칼(A, C)도 생기지 않는다(전자쌍이 함께 이동).') +
    tip('세포 속 ATP는 대부분 물이 아닌 다른 분자(포도당, 글루탐산 …)에 인산을 넘긴다 = 작용기 전달.', '연결'))

add(n=46, sec=7, diff=3, kind='SA', title='ATP는 왜 “가수분해”보다 “인산 전달”로 일하나',
    en='<p>In general, when ATP hydrolysis is coupled to an energy-requiring reaction, the actual reaction often consists of the transfer of a phosphate group from ATP to another substrate, rather than an actual hydrolysis of the ATP. Explain.</p>',
    ko='<p>ATP 가수분해가 에너지가 필요한 반응과 짝지어질 때, 실제로는 ATP가 가수분해되기보다 인산기를 다른 기질로 전달하는 경우가 많다. 설명하라.</p>',
    answer=sa('Simple hydrolysis would release the energy as heat. Transferring the γ-phosphate to the substrate makes a high-energy phosphorylated intermediate that then reacts exergonically to form the product.',
              '그냥 가수분해하면 에너지가 <b>열</b>로 날아간다. γ-인산을 기질에 붙여 <b>고에너지 인산화 중간체</b>를 만들면, 그 중간체가 다음 단계에서 쉽게(발에르곤) 생성물이 된다.'),
    explain=fig(two_step(), '글루타민 합성효소: 2단계 짝지음 (슬라이드 22)') +
    steps('① 글루탐산 + ATP → γ-글루타밀 인산 + ADP (인산 전달 = 활성화)', '② γ-글루타밀 인산 + NH₃ → 글루타민 + Pᵢ (발에르곤)') +
    tip('돈(에너지)을 바닥에 뿌리면(가수분해) 사라지지만, 상대 계좌로 이체하면(인산 전달) 그 돈으로 일을 시킬 수 있다.', '비유'))

add(n=24, sec=7, diff=1, title='DNA·RNA 합성의 직접 전구체',
    en=mcq('The immediate precursors of DNA and RNA synthesis in the cell all contain:', ["3′ triphosphates.", "5′ triphosphates.", 'adenine.', 'deoxyribose.', 'ribose.']),
    ko=mcq('세포에서 DNA와 RNA 합성의 직접 전구체가 모두 가진 것은?', ["3′ 삼인산", "<b>5′ 삼인산</b>", '아데닌', '디옥시리보스', '리보스']),
    answer=ans('B', "5′ triphosphates", "5′ 삼인산 (dNTP · NTP)"),
    explain=key('DNA = dNTP, RNA = NTP. 모두 당의 5′ 탄소에 인산 3개.') +
    steps('중합효소가 α-인산을 공격시켜 뉴클레오타이드를 붙이고 <b>PPᵢ</b>를 내보낸다.', 'PPᵢ → 2Pᵢ (가수분해)로 반응이 강하게 비가역 (슬라이드 26, 34).',
          'D·E 틀림: DNA는 디옥시리보스, RNA는 리보스 — “모두”가 아님. C도 A만 아님.') +
    tip('정보 거대분자 조립에는 ATP의 α 자리 공격 → PPᵢ 방출이 쓰인다.', '연결'))

add(n=25, sec=7, diff=2, title='근육 수축의 에너지 변환',
    en=mcq('Muscle contraction involves the conversion of:', ['chemical energy to kinetic energy.', 'chemical energy to potential energy.', 'kinetic energy to chemical energy.', 'potential energy to chemical energy.', 'potential energy to kinetic energy.']),
    ko=mcq('근육 수축에서 일어나는 에너지 변환은?', ['<b>화학 에너지 → 운동 에너지</b>', '화학 에너지 → 위치 에너지', '운동 에너지 → 화학 에너지', '위치 에너지 → 화학 에너지', '위치 에너지 → 운동 에너지']),
    answer=ans('A', 'chemical energy to kinetic energy', '화학 에너지(ATP) → 운동 에너지(움직임)'),
    explain=key('ATP 가수분해(화학) → 마이오신 머리가 움직여 액틴을 당김(운동).') +
    table(['예', '변환'], [['근육 수축', '화학 → 기계(운동)'], ['능동수송', '화학 → 농도 기울기(삼투)'], ['반딧불이 빛', '화학 → 빛'], ['광합성', '빛 → 화학']]) +
    tip('ATP의 3가지 일: 정보 분자 조립, 능동수송, 근육 수축 (슬라이드 34).', '연결'))

add(n=47, sec=7, diff=2, kind='SA', title='생물의 에너지 변환 4가지',
    en='<p>The first law of thermodynamics states that the amount of energy in the universe is constant, but that the various forms of energy can be interconverted. Describe four different types of such energy transduction that occur in living organisms and provide one example for each.</p>',
    ko='<p>열역학 제1법칙은 우주의 에너지 총량은 일정하지만 여러 형태로 바뀔 수 있다고 말한다. 생물에서 일어나는 에너지 변환 4가지를 예와 함께 설명하라.</p>',
    answer=sa('Chemical → osmotic (ATP-driven active transport); light → electrical (light-driven electron flow in chloroplasts); chemical → light (firefly bioluminescence); chemical → mechanical (muscle contraction).',
              '화학 → 농도 기울기(능동수송) · 빛 → 전기(엽록체 전자 흐름) · 화학 → 빛(반딧불이) · 화학 → 기계(근육 수축)'),
    explain=table(['변환', '예', '주인공'], [['화학 → 삼투(농도 차)', 'Na⁺/K⁺ 펌프', 'ATP'], ['빛 → 전기', '광합성 전자 흐름', '엽록소'], ['화학 → 빛', '반딧불이', '루시페린 + ATP'], ['화학 → 기계', '근육 수축', '마이오신 + ATP']], cls='left') +
    tip('반딧불이는 ATP의 α 자리를 공격(루시페린-AMP)해 빛을 낸다 (슬라이드 23, 34).', '연결'))

# ================================================================ S9 high-energy (idx 8)
add(n=7, sec=8, diff=1, title='가수분해 ΔG′°가 가장 큰 음수인 것',
    en=mcq(f'Which of the following compounds has the largest negative value for the standard free-energy change ({DG}) upon hydrolysis?', ['Acetic anhydride', 'Glucose 6-phosphate', 'Glutamine', 'Glycerol 3-phosphate', 'Lactose']),
    ko=mcq(f'가수분해의 {DG}가 가장 큰 음수인 것은?', ['<b>아세트산 무수물</b>', '포도당 6-인산', '글루타민', '글리세롤 3-인산', '락토스']),
    answer=ans('A', 'Acetic anhydride', '아세트산 무수물 (−91.1 kJ/mol)'),
    explain=table(['화합물', 'ΔG′° (kJ/mol)', '결합'], [['<b>아세트산 무수물</b>', '<b>−91.1</b>', '산 무수물'], ['글루타민', '−14.2', '아미드'], ['포도당 6-인산', '−13.8', '인산 에스터'], ['락토스', '−15.9', '글리코시드'], ['글리세롤 3-인산', '−9.2', '인산 에스터']], cls='left') +
    key('<b>무수물</b>(–CO–O–CO–) 결합 = 두 산이 물을 빼고 붙은 것 → 가수분해 에너지 큼. ATP의 인산무수물 결합도 같은 종류.'))

add(n=23, sec=8, diff=1, title='고에너지 화합물이 아닌 것',
    en=mcq('Which one of the following compounds does not have a large negative free energy of hydrolysis?', ['1,3-bisphosphoglycerate', '3-phosphoglycerate', 'ADP', 'Phosphoenolpyruvate', 'Thioesters (e.g. acetyl-CoA)']),
    ko=mcq('가수분해 자유에너지가 크게 음수가 <b>아닌</b> 것은?', ['1,3-비스포스포글리세르산', '<b>3-포스포글리세르산</b>', 'ADP', 'PEP', '티오에스터 (아세틸-CoA)']),
    answer=ans('B', '3-phosphoglycerate', '3-포스포글리세르산 (평범한 인산 에스터)'),
    explain=table(['화합물', 'ΔG′° 가수분해', '등급'], [['PEP', '−61.9', '최강'], ['1,3-BPG', '−49.3', '고에너지'], ['티오에스터 (아세틸-CoA)', '−31.4', '고에너지'], ['ADP (→ AMP + Pᵢ)', '−32.8', '고에너지'], ['<b>3-PG</b>', '<b>약 −12</b>', '저에너지 (에스터)']], cls='left') +
    key('고에너지 = ATP(−30.5)보다 크거나 비슷. 인산 <b>에스터</b>(3-PG, G6P)는 저에너지.') +
    tip('1,3-BPG → 3-PG에서 인산을 ADP에 넘겨 ATP를 만든다(해당과정 7단계) — 그래서 3-PG는 이미 “다 쓴” 상태.', '연결'))

add(n=22, sec=8, diff=3, title='PEP 가수분해가 −62 kJ/mol인 이유',
    en=mcq('The hydrolysis of phosphoenolpyruvate proceeds with a ΔG′° of about –62 kJ/mol. The greatest contributing factors are the destabilization of the reactants by electrostatic repulsion and stabilization of the product pyruvate by:', ['electrostatic attraction.', 'ionization.', 'polarization.', 'resonance.', 'tautomerization.']),
    ko=mcq('PEP 가수분해는 ΔG′° ≈ −62 kJ/mol. 가장 큰 요인은 반응물의 전하 반발과, 생성물 피루브산이 무엇으로 안정해지기 때문인가?', ['정전기적 인력', '이온화', '분극', '공명', '<b>토토머화(호변이성)</b>']),
    answer=ans('E', 'tautomerization', '토토머화 — 엔올형 → 케토형 피루브산'),
    explain=fig(flow(['PEP', '엔올 피루브산', '케토 피루브산'], arrow_labels=['가수분해 (−Pᵢ)', '토토머화 (자발적)'], colors=[C['navy'], C['orange'], C['green']], box_h=38, width=520), '') +
    steps('가수분해로 먼저 <b>엔올형</b> 피루브산이 생긴다.', '엔올형은 불안정해서 곧바로 훨씬 안정한 <b>케토형</b>으로 바뀐다 → 큰 에너지 방출.', 'PEP는 인산이 붙어 있어 토토머화가 막혀 있다 = 꽉 눌린 스프링.') +
    tip('토토머화 = H 하나와 이중결합 위치가 바뀌는 이성질화 (C=C–OH ⇌ CH–C=O).', '용어'))

add(n=45, sec=8, diff=2, kind='SA', title='PEP의 큰 −ΔG′°를 화학적으로 설명',
    en='<p>The free energy of hydrolysis of phosphoenolpyruvate is –61.9 kJ/mol. Rationalize this large, negative value for ΔG′° in chemical terms.</p>',
    ko='<p>PEP 가수분해 자유에너지는 −61.9 kJ/mol이다. 이 큰 음수 값을 화학적으로 설명하라.</p>',
    answer=sa('Hydrolysis gives enol pyruvate, which quickly tautomerizes to the much more stable keto pyruvate; PEP itself cannot tautomerize.',
              '가수분해로 생긴 엔올 피루브산이 곧바로 훨씬 안정한 케토 피루브산으로 토토머화한다. PEP는 인산 때문에 토토머화할 수 없다.'),
    explain=fig(flow(['PEP (엔올 고정)', '엔올 피루브산', '케토 피루브산'], arrow_labels=['−Pᵢ', '토토머화'], colors=[C['navy'], C['orange'], C['green']], box_h=38, width=520), '') +
    key('생성물이 “한 번 더” 안정해지는 단계(토토머화)가 있어 전체 에너지 차가 커진다.') +
    tip('바로 앞 기출(TB 13-22) 객관식과 같은 내용 — 서술형으로도 나온다!', '연결'))

# ================================================================ S10 redox (idx 9)
add(n=26, sec=9, diff=1, title='생물학적 산화-환원에 항상 있는 것',
    en=mcq('Biological oxidation-reduction reactions always involve:', ['direct participation of oxygen.', 'formation of water.', 'mitochondria.', 'transfer of electron(s).', 'transfer of hydrogens.']),
    ko=mcq('생물학적 산화-환원 반응에 <b>항상</b> 포함되는 것은?', ['산소의 직접 참여', '물 생성', '미토콘드리아', '<b>전자 이동</b>', '수소 이동']),
    answer=ans('D', 'transfer of electron(s)', '전자의 이동'),
    explain=key('산화 = 전자를 잃음, 환원 = 전자를 얻음. 정의 자체가 전자 이동.') +
    table(['전자가 이동하는 4가지 방식 (슬라이드 41)', '예'], [['전자만 (e⁻)', 'Fe³⁺ → Fe²⁺ (시토크롬)'], ['수소 원자 (H⁺ + e⁻)', '탈수소효소'], ['하이드라이드 (H⁻ = H⁺ + 2e⁻)', 'NAD⁺ → NADH'], ['산소와 직접 결합', '산소화효소']], cls='left') +
    warn('E(수소 이동)는 “항상”이 아님 — 시토크롬은 전자만 옮긴다.', '함정'))

add(n=27, sec=9, diff=2, title='생물학적 산화-환원에 절대 없는 것',
    en=mcq('Biological oxidation-reduction reactions never involve:', ['transfer of e<sup>−</sup> from one molecule to another.', 'formation of free e<sup>−</sup>.', 'transfer of H<sup>+</sup> (or H₃O<sup>+</sup>) from one molecule to another.', 'formation of free H<sup>+</sup> (or H₃O<sup>+</sup>).', 'none of the above.']),
    ko=mcq('생물학적 산화-환원 반응에서 <b>절대 일어나지 않는</b> 것은?', ['분자 사이 전자 이동', '<b>자유 전자의 생성</b>', '분자 사이 H⁺ 이동', '자유 H⁺ 생성', '정답 없음']),
    answer=ans('B', 'formation of free e<sup>−</sup>', '자유 전자(혼자 떠다니는 전자)의 생성'),
    explain=key('전자는 혼자 돌아다니지 않는다 → 주는 쪽과 받는 쪽이 <b>동시에</b> 있어야 한다 = 짝반응.') +
    steps('H⁺는 물속에 자유롭게 있을 수 있다(D 가능).', '전자는 항상 한 분자에서 다른 분자로 직접 넘어간다(A).') + tip('공을 던지는 사람(환원제)과 받는 사람(산화제)이 함께 있어야 공(전자)이 이동.', '비유'))

add(n=48, sec=9, diff=1, kind='SA', title='산화와 환원의 정의',
    en='<p>What is an oxidation? What is a reduction? Can an oxidation occur without a simultaneous reduction? Why or why not?</p>',
    ko='<p>산화란? 환원이란? 산화가 환원 없이 일어날 수 있는가? 이유는?</p>',
    answer=sa('Oxidation is loss of electrons; reduction is gain of electrons. No — free electrons do not exist, so every electron released by oxidation must be accepted in a reduction.',
              '산화 = 전자를 잃음, 환원 = 전자를 얻음. 불가능 — 자유 전자는 존재하지 않아, 산화로 나온 전자는 반드시 다른 물질이 받아야(환원) 한다.'),
    explain=key('외우기: <b>OIL RIG</b> — Oxidation Is Loss, Reduction Is Gain.') +
    steps('산화되는 물질 = 전자를 주는 쪽 = <b>환원제</b>.', '환원되는 물질 = 전자를 받는 쪽 = <b>산화제</b>.') + tip('바로 앞 기출(TB 13-27)의 서술형 버전.', '연결'))

add(n=19, sec=9, diff=2, title='산화-환원에 대한 옳은 설명',
    en=mcq('Which of the following is true about oxidation-reduction reactions?', ['They usually proceed through homolytic cleavage.', 'During oxidation a compound gains electrons.', 'Dehydrogenases typically remove two electrons and two hydrides.', 'There are four commonly accessed oxidation states of carbon.', 'Every oxidation must be accompanied by a reduction.']),
    ko=mcq('산화-환원 반응에 대해 옳은 것은?', ['보통 균일 분해로 진행한다', '산화될 때 화합물은 전자를 얻는다', '탈수소효소는 보통 전자 2개와 하이드라이드 2개를 뗀다', '탄소가 흔히 갖는 산화 상태는 4가지이다', '<b>모든 산화에는 환원이 따른다</b>']),
    answer=ans('E', 'Every oxidation must be accompanied by a reduction.', '모든 산화는 반드시 환원과 함께 일어난다'),
    explain=steps('B: 산화는 전자를 <b>잃음</b>.', 'C: 탈수소효소는 전자 2개 + 양성자 2개(= 하이드라이드 1개 + H⁺ 1개)를 뗀다. “하이드라이드 2개” 틀림.',
                  'D: 탄소 산화 상태는 메테인부터 CO₂까지 5단계 이상 (S10 그림).', 'A: 생물의 산화-환원은 대부분 전자쌍 이동(불균일).') +
    fig(carbon_ox(), '') + key('전자는 혼자 못 다닌다 → 산화와 환원은 늘 짝.'))

add(n=52, sec=9, diff=1, kind='SA', title='더 환원된 쪽 고르기',
    en='<p>For each pair, indicate which is the more highly reduced species: (a) Co²⁺/Co⁺ (b) Glucose/CO₂ (c) Fe³⁺/Fe²⁺ (d) Acetate/CO₂ (e) Ethanol/acetic acid (f) Acetic acid/acetaldehyde</p>',
    ko='<p>각 쌍에서 더 환원된 것을 고르라: (a) Co²⁺/Co⁺ (b) 포도당/CO₂ (c) Fe³⁺/Fe²⁺ (d) 아세트산/CO₂ (e) 에탄올/아세트산 (f) 아세트산/아세트알데하이드</p>',
    answer=sa('(a) Co⁺ (b) glucose (c) Fe²⁺ (d) acetate (e) ethanol (f) acetaldehyde', '(a) Co⁺ (b) 포도당 (c) Fe²⁺ (d) 아세트산 (e) 에탄올 (f) 아세트알데하이드'),
    explain=key('환원 = 전자가 많다. 이온은 <b>양전하가 작을수록</b>, 탄소는 <b>H가 많고 O가 적을수록</b> 환원.') + fig(carbon_ox(), '') +
    steps('(a)(c) 전자를 하나 더 가진 쪽(전하가 작은 쪽).', '(b)(d) CO₂는 탄소의 최종 산화 상태 → 상대방이 더 환원.', '(e)(f) 에탄올(–CH₂OH) &gt; 아세트알데하이드(–CHO) &gt; 아세트산(–COOH).'))

# ================================================================ S11 E′° (idx 10)
add(n=28, sec=10, diff=2, title='숙신산·푸마르산·FAD·FADH₂를 섞으면',
    en=mcq('Fumarate + 2H⁺ + 2e⁻ → succinate, E′° = +0.031 V; FAD + 2H⁺ + 2e⁻ → FADH₂, E′° = −0.219 V. If you mixed succinate, fumarate, FAD, and FADH₂ together, all at 1 M, with succinate dehydrogenase, which would happen initially?',
           ['Fumarate and succinate would become oxidized; FAD and FADH₂ would become reduced.', 'Fumarate would become reduced; FADH₂ would become oxidized.', 'No reaction would occur because all reactants and products are already at their standard concentrations.', 'Succinate would become oxidized; FAD would become reduced.', 'Succinate would become oxidized; FADH₂ would be unchanged because it is a cofactor.']),
    ko=mcq('푸마르산/숙신산 E′° = +0.031 V, FAD/FADH₂ E′° = −0.219 V. 네 물질을 모두 1 M로 숙신산 탈수소효소와 섞으면 처음에 일어나는 일은?',
           ['푸마르산·숙신산은 산화, FAD·FADH₂는 환원', '<b>푸마르산은 환원, FADH₂는 산화</b>', '모두 표준 농도라 반응 없음', '숙신산은 산화, FAD는 환원', '숙신산은 산화, FADH₂는 보조인자라 변화 없음']),
    answer=ans('B', 'Fumarate would become reduced; FADH₂ would become oxidized.', '푸마르산이 환원되고(→ 숙신산), FADH₂가 산화된다(→ FAD)'),
    explain=key('전자는 E′°가 <b>낮은 쪽 → 높은 쪽</b>으로 흐른다 (물이 높은 데서 낮은 데로 흐르듯, 전자는 “−”에서 “+”로).') +
    align([('FADH₂ (−0.219)', '→ 전자 줌 (산화)', ''), ('푸마르산 (+0.031)', '← 전자 받음 (환원)', ''), ('ΔE′°', '0.031 − (−0.219) = +0.25 V → ΔG′° &lt; 0', '')]) +
    warn('세포 속 TCA에서는 반대(숙신산 → 푸마르산)로 간다 — 효소에 붙은 FAD의 실제 전위와 농도가 다르기 때문. 이 문제는 “표준 조건, 1 M”이라 B.', '함정'))

add(n=29, sec=10, diff=3, title='모두 10⁻⁵ M일 때의 자발적 방향',
    en=mcq('E′° of NAD⁺/NADH is −0.32 V. E′° of oxaloacetate/malate is −0.175 V. When the concentrations of NAD⁺, NADH, oxaloacetate, and malate are all 10⁻⁵ M, the “spontaneous” reaction is:',
           ['malate + NAD⁺ → oxaloacetate + NADH + H⁺', 'malate + NADH + H⁺ → oxaloacetate + NAD⁺', 'NAD⁺ + NADH + H⁺ → malate + oxaloacetate', 'NAD⁺ + oxaloacetate → NADH + H⁺ + malate', 'oxaloacetate + NADH + H⁺ → malate + NAD⁺']),
    ko=mcq('NAD⁺/NADH −0.32 V, OAA/말산 −0.175 V. NAD⁺, NADH, OAA, 말산이 모두 10⁻⁵ M일 때 “자발적” 반응은?',
           ['말산 + NAD⁺ → OAA + NADH + H⁺', '말산 + NADH + H⁺ → OAA + NAD⁺', 'NAD⁺ + NADH + H⁺ → 말산 + OAA', 'NAD⁺ + OAA → NADH + H⁺ + 말산', '<b>OAA + NADH + H⁺ → 말산 + NAD⁺</b>']),
    answer=ans('E', 'oxaloacetate + NADH + H⁺ → malate + NAD⁺', 'OAA + NADH → 말산 + NAD⁺ (NADH가 OAA를 환원)'),
    explain=key('농도가 모두 같으면 농도비 = 1 → ln 항 = 0 → 표준 전위만으로 판단.') +
    steps('NADH(−0.32)가 더 낮다 → 전자를 준다(산화).', 'OAA(−0.175)가 더 높다 → 전자를 받아 말산이 된다(환원).', 'ΔE′° = −0.175 − (−0.32) = +0.145 V &gt; 0 → ΔG′° = −2(96.5)(0.145) ≈ −28 kJ/mol.') +
    tip('그래서 말산 → OAA (TCA 8단계)는 표준 조건에선 불리(+29.7) — TB 13-8과 같은 이야기!', '연결'))

# ================================================================ S12 ΔG = −nFΔE (idx 11)
add(n=50, sec=11, diff=2, kind='SA', title='ΔE′°가 양수면 ΔG′°의 부호는?',
    en='<p>If ΔE′° for an oxidation-reduction reaction is positive, will ΔG′° be positive or negative? What is the equation that relates ΔG′° and ΔE′°?</p>',
    ko='<p>산화-환원 반응의 ΔE′°가 양수이면 ΔG′°는 양수인가 음수인가? 둘을 잇는 식은?</p>',
    answer=sa('Negative. ΔG′° = −nFΔE′°', '음수. ΔG′° = −nFΔE′°'),
    explain=eq('ΔG′° = −n F ΔE′°') + table(['기호', '뜻'], [['n', '이동하는 전자 수 (NADH = 2)'], ['F', '패러데이 상수 96.5 kJ/V·mol'], ['ΔE′°', 'E′°(전자 받는 쪽) − E′°(주는 쪽)']]) +
    key('앞에 마이너스가 있으니 ΔE′° 양수 ↔ ΔG′° 음수 (자발적).'))

add(n=49, sec=11, diff=3, kind='SA', title='NADH → O₂의 ΔG′°',
    en='<p>During transfer of two electrons through the mitochondrial respiratory chain, the overall reaction is NADH + ½O₂ + H⁺ → NAD⁺ + H₂O. ΔE′° = +1.14 V. Show how you would calculate ΔG′°. (F = 96.48 kJ/V·mol)</p>',
    ko='<p>미토콘드리아 호흡 사슬에서 전자 2개가 이동하는 전체 반응: NADH + ½O₂ + H⁺ → NAD⁺ + H₂O, ΔE′° = +1.14 V. ΔG′°를 계산하라. (F = 96.48 kJ/V·mol)</p>',
    answer=sa('ΔG′° = −nFΔE′° = −(2)(96.48)(1.14) = −220 kJ/mol', 'ΔG′° = −2 × 96.48 × 1.14 = <b>−220 kJ/mol</b>'),
    explain=fig(redox_ladder_big(), '') + align([('n', '2 (NADH는 전자 2개)', ''), ('ΔE′°', '+0.816 − (−0.320) = +1.14 V', ''), ('ΔG′°', '−(2)(96.48)(1.14) = <b>−220 kJ/mol</b>', '')]) +
    tip('이 220 kJ로 ATP 약 2.5개를 만든다 (19장).', '연결'))

add(n=51, sec=11, diff=2, kind='SA', title='글리세롤 3-인산 탈수소효소의 ΔG′°',
    en='<p>Glycerol 3-phosphate + NAD⁺ → NADH + H⁺ + dihydroxyacetone phosphate. Given DHAP + 2e⁻ + 2H⁺ → glycerol 3-phosphate, E′° = −0.29 V and NAD⁺ + H⁺ + 2e⁻ → NADH, E′° = −0.32 V, calculate ΔG′° (left to right). (F = 96.48 kJ/V·mol)</p>',
    ko='<p>글리세롤 3-인산 + NAD⁺ → NADH + H⁺ + DHAP. DHAP/글리세롤 3-인산 E′° = −0.29 V, NAD⁺/NADH E′° = −0.32 V. 왼쪽 → 오른쪽의 ΔG′°를 구하라.</p>',
    answer=sa('ΔE′° = E′°(acceptor NAD⁺) − E′°(donor) = −0.32 − (−0.29) = −0.03 V; ΔG′° = −(2)(96.48)(−0.03) = +5.8 kJ/mol',
              'ΔE′° = −0.32 − (−0.29) = −0.03 V → ΔG′° = <b>+5.8 kJ/mol</b> (약간 불리)'),
    explain=steps('<b>전자를 받는 쪽</b>을 먼저 찾기: 반응식에서 NAD⁺ → NADH로 바뀌니 NAD⁺가 받는 쪽.', '주는 쪽 = 글리세롤 3-인산(→ DHAP).',
                  'ΔE′° = E′°(받는 쪽) − E′°(주는 쪽) = −0.32 − (−0.29) = −0.03 V', 'ΔG′° = −(2)(96.48)(−0.03) = +5.8 kJ/mol') +
    warn('“받는 쪽 − 주는 쪽” 순서를 바꾸면 부호가 뒤집힌다. 반응식에서 누가 환원되는지 먼저 보자!', '함정'))

add(n=53, sec=11, diff=3, kind='SA', title='젖산 탈수소효소의 방향과 ΔG′°',
    en='<p>Lactate dehydrogenase: Pyruvate + NADH + H⁺ → Lactate + NAD⁺. (a) In which direction will the reaction tend to go if all are mixed at 1 M at pH 7? (b) Calculate ΔG′°. NAD⁺/NADH E′° = −0.32 V; pyruvate/lactate E′° = −0.19 V; F = 96.48 kJ/V·mol.</p>',
    ko='<p>젖산 탈수소효소: 피루브산 + NADH + H⁺ → 젖산 + NAD⁺. (a) 모두 1 M, pH 7로 섞으면 어느 방향으로 가나? (b) ΔG′°를 구하라. (NAD⁺/NADH −0.32 V, 피루브산/젖산 −0.19 V)</p>',
    answer=sa('(a) Toward lactate (as written). (b) ΔE′° = −0.19 − (−0.32) = +0.13 V; ΔG′° = −(2)(96.48)(0.13) = −25.1 kJ/mol',
              '(a) 쓰여진 방향(젖산 쪽). (b) ΔE′° = +0.13 V → ΔG′° = <b>−25.1 kJ/mol</b>'),
    explain=steps('받는 쪽 = 피루브산(→ 젖산, −0.19), 주는 쪽 = NADH(−0.32).', 'ΔE′° = −0.19 − (−0.32) = +0.13 V (양수 → 자발적)', 'ΔG′° = −2 × 96.48 × 0.13 = −25.1 kJ/mol') +
    key('전자는 낮은 E′°(NADH)에서 높은 E′°(피루브산)로 → 젖산 생성. 운동 중 근육의 젖산 발효(14장).') +
    warn('테스트뱅크 해설에 “ΔG′° = E′°(acceptor) − …”라고 오타가 있어. 첫 줄은 ΔE′°야.', '자료 오타'))

add(n=54, sec=11, diff=3, kind='SA', title='알코올 탈수소효소 — 정방향·역방향',
    en='<p>Alcohol dehydrogenase: Acetaldehyde + NADH + H⁺ → Ethanol + NAD⁺. Acetaldehyde/ethanol E′° = −0.20 V; NAD⁺/NADH E′° = −0.32 V; F = 96.48 kJ/V·mol. (a) Calculate ΔG′° as written. (b) What is ΔG′° for the reverse? (c) Which direction is spontaneous under standard conditions? (d) In the cell, the reaction actually proceeds in the direction with a positive ΔG′°. Explain.</p>',
    ko='<p>알코올 탈수소효소: 아세트알데하이드 + NADH + H⁺ → 에탄올 + NAD⁺. (아세트알데하이드/에탄올 −0.20 V, NAD⁺/NADH −0.32 V) (a) 쓰여진 방향의 ΔG′° (b) 역방향의 ΔG′° (c) 표준 조건에서 자발적인 방향 (d) 세포에서는 ΔG′°가 양수인 방향으로 진행하기도 한다. 어떻게 가능한가?</p>',
    answer=sa('(a) ΔE′° = +0.12 V; ΔG′° = −23.2 kJ/mol (b) +23.2 kJ/mol (c) forward (d) ΔG can be negative if the product concentration is kept very low: ΔG = ΔG′° + RT ln([products]/[reactants]).',
              '(a) −23.2 kJ/mol (b) +23.2 kJ/mol (c) 정방향 (d) 생성물을 계속 치워 농도를 낮게 유지하면 ln 항이 음수가 되어 ΔG &lt; 0'),
    explain=align([('ΔE′°', '−0.20 − (−0.32) = +0.12 V', ''), ('ΔG′° (정)', '−(2)(96.48)(0.12) = <b>−23.2 kJ/mol</b>', ''), ('ΔG′° (역)', '<b>+23.2 kJ/mol</b>', '')]) +
    steps('(d) 간에서는 에탄올 → 아세트알데하이드(역방향, +23.2)로 술을 분해한다.', '아세트알데하이드가 다음 효소(알데하이드 탈수소효소)로 바로 치워지고, NADH도 재산화되어 ln Q가 크게 음수 → ΔG &lt; 0.') +
    key('ΔG′°는 “정가”, 실제 방향은 농도가 정한다 — 13장 최대의 교훈.'))

# ================================================================ S13 carriers (idx 12)
add(n=30, sec=12, diff=2, title='NAD⁺ 구조에 없는 것',
    en=mcq('The structure of NAD⁺ does not include:', ['a flavin nucleotide.', 'a pyrophosphate bond.', 'an adenine nucleotide.', 'nicotinamide.', 'two ribose residues.']),
    ko=mcq('NAD⁺ 구조에 포함되지 <b>않는</b> 것은?', ['<b>플라빈 뉴클레오타이드</b>', '피로인산 결합', '아데닌 뉴클레오타이드', '니코틴아마이드', '리보스 2개']),
    answer=ans('A', 'a flavin nucleotide', '플라빈 뉴클레오타이드 (그건 FAD·FMN의 부품)'),
    explain=fig(flow(['니코틴아마이드–리보스–P', 'P–리보스–아데닌'], arrow_labels=['피로인산 결합 (P–P)'], colors=[C['orange'], C['blue']], box_h=38, width=520), 'NAD⁺ = 뉴클레오타이드 2개가 인산끼리 연결') +
    table(['조효소', '구성'], [['NAD⁺', '니코틴아마이드 뉴클레오타이드 + 아데닌 뉴클레오타이드 (나이아신 B₃)'], ['FAD', '<b>플라빈</b> 뉴클레오타이드 + 아데닌 뉴클레오타이드 (리보플래빈 B₂)']], cls='left') +
    key('Nicotinamide Adenine Dinucleotide — 이름에 답이 있다: 니코틴아마이드 + 아데닌 + 뉴클레오타이드 2개.'))

add(n=31, sec=12, diff=2, title='니코틴아마이드 조효소에 대해 틀린 것',
    en=mcq('Which of the following is not true for the nicotinamide cofactors?', ['The oxidized form is positively charged.', 'The reduced form has a large extinction coefficient at 340 nm.', 'The oxidized form provides reducing equivalents to other molecules.', 'Oxidation-reduction reactions with nicotinamides usually involve hydride transfer.', 'Enzymes transfer hydrides stereospecifically to one or the other side of the nicotinamide ring.']),
    ko=mcq('니코틴아마이드 조효소(NAD⁺·NADP⁺)에 대해 <b>틀린</b> 것은?', ['산화형은 양전하를 띤다', '환원형은 340 nm에서 흡광 계수가 크다', '<b>산화형이 다른 분자에 환원력(전자)을 준다</b>', '산화-환원은 보통 하이드라이드 전달로 일어난다', '효소는 니코틴아마이드 고리의 한쪽 면에만 하이드라이드를 입체특이적으로 전달한다']),
    answer=ans('C', 'The oxidized form provides reducing equivalents to other molecules.', '“산화형이 환원력을 준다” — 틀림. 전자를 주는 건 환원형(NADH·NADPH)'),
    explain=fig(nad_svg(), '') +
    steps('NAD⁺ = 빈 트럭 → 전자를 <b>받는</b> 쪽. NADH = 짐 실은 트럭 → 전자를 <b>주는</b> 쪽.', 'B: NADH만 340 nm 빛을 흡수 → 효소 활성 측정에 쓴다 (18장 ALT 측정).', 'A: NAD<b>⁺</b> — 이름에 양전하 표시.') +
    key('환원력(reducing equivalents)을 주는 건 늘 <b>환원형</b>.'))

# ================================================================ 보충: 13.2 화학 반응의 논리 (유기화학) — S8 묶음 뒤, 보충 페이지 다음
def nu_el():
    W, H = 540, 120
    b = arrowdef('ne', C['red'])
    b += f'<rect x="20" y="40" width="130" height="44" rx="12" fill="#eff6ff" stroke="{C["blue"]}" stroke-width="2"/>' + T(85, 60, '친핵체 Nu:⁻', 13, C['blue'], weight=900) + T(85, 77, '전자쌍이 남는다', 10, C['gray'])
    b += f'<rect x="390" y="40" width="130" height="44" rx="12" fill="#fef2f2" stroke="{C["red"]}" stroke-width="2"/>' + T(455, 60, '친전자체 E⁺ (δ+)', 13, C['red'], weight=900) + T(455, 77, '전자가 모자란다', 10, C['gray'])
    b += f'<path d="M150 50 Q 270 0 386 50" fill="none" stroke="{C["red"]}" stroke-width="2.6" marker-end="url(#ne)"/>' + T(270, 22, '굽은 화살표 = 전자쌍 2개의 이동', 11, C['red'], weight=900)
    b += T(270, 110, '화살표는 항상 “전자가 많은 곳 → 적은 곳” (Nu → E)', 11, C['navy'], weight=900)
    return svg(W, H, b)


add(n=15, sec=7, diff=1, supp=True, title='친핵체가 아닌 것',
    en=mcq('Which of the following is <b>not</b> nucleophilic?', ['A proton', 'A carbanion', 'An imidazole', 'A hydroxide', 'A carboxylic acid']),
    ko=mcq('다음 중 친핵성이 <b>없는</b> 것은?', ['<b>양성자 (H⁺)</b>', '카바니온 (탄소 음이온)', '이미다졸', '수산화 이온 (OH⁻)', '카복실산']),
    answer=ans('A', 'A proton', '양성자 (H⁺) — 전자가 하나도 없어 줄 전자쌍이 없다'),
    explain=fig(nu_el(), '') +
    table(['보기', '전자쌍?', '판정'], [['H⁺', '없음 (전자 0개)', '<b>친전자체</b>'], ['카바니온 C⁻', '음전하 전자쌍', '친핵체'], ['이미다졸 (His)', 'N의 비공유 전자쌍', '친핵체'], ['OH⁻', '음전하 산소', '친핵체'], ['카복실산 (–COO⁻)', '산소의 비공유 전자쌍', '친핵체 (약함)']], cls='left') +
    key('<b>친핵체</b>(nucleophile) = “핵(+)을 좋아한다” = 전자쌍을 <b>주는</b> 쪽. 음전하나 비공유 전자쌍이 있다.') +
    tip('H⁺는 전자를 받는 대표 친전자체 — 다음 문제(TB 13-16)에서 짝으로 나온다.', '연결'))

add(n=16, sec=7, diff=1, supp=True, title='친전자체가 아닌 것',
    en=mcq('Which of the following is <b>not</b> electrophilic?', ['A proton', 'A sulfhydryl', 'A protonated imine', 'A carbonyl group', 'A phosphoryl group']),
    ko=mcq('다음 중 친전자성이 <b>없는</b> 것은?', ['양성자 (H⁺)', '<b>설프하이드릴 (–SH)</b>', '양성자화된 이민 (C=N⁺H)', '카보닐기 (C=O)', '포스포릴기 (인산기)']),
    answer=ans('B', 'A sulfhydryl', '설프하이드릴(–SH) — 황의 비공유 전자쌍을 주는 친핵체'),
    explain=table(['보기', '전자가 모자란 곳', '판정'], [['H⁺', '전자 0개', '친전자체'], ['<b>–SH</b>', '황에 비공유 전자쌍 2쌍 (전자 풍부)', '<b>친핵체</b>'], ['C=N⁺H', '이민 탄소 (δ+, N⁺가 전자를 당김)', '친전자체'], ['C=O', '카보닐 탄소 (δ+)', '친전자체'], ['–PO₃²⁻', '인 원자 (산소 4개가 전자를 당김)', '친전자체']], cls='left') +
    key('<b>친전자체</b>(electrophile) = “전자를 좋아한다” = 전자쌍을 <b>받는</b> 쪽. 양전하 또는 δ+ 원자.') +
    steps('산소·질소처럼 전기음성도가 큰 원자와 이중결합한 탄소(C=O, C=N)는 전자를 빼앗겨 δ+ → 친전자체.', '–SH(시스테인)·–OH(세린)·이미다졸(히스티딘)은 효소 활성 부위의 대표 친핵체.') +
    tip('ATP의 인(P)도 친전자체 → 친핵체가 α·β·γ 인 원자를 공격 (슬라이드 34).', '연결'))

add(n=17, sec=7, diff=2, supp=True, title='카바니온·카보닐에 대해 틀린 것',
    en=mcq('Which of the following is <b>not</b> true?', ['The carbon adjacent to a carbonyl can be resonance stabilized to form a carbanion.', 'A carbonyl carbon can be made more electrophilic by a nearby metal ion.', 'The carbon adjacent to an imine can be resonance stabilized to form a carbanion.', 'Decarboxylation of a β-keto acid goes through a carbocation intermediate.', 'A Claisen ester condensation reaction goes through a carbanion intermediate.']),
    ko=mcq('다음 중 <b>틀린</b> 것은?', ['카보닐 옆 탄소는 공명으로 안정화되어 카바니온이 될 수 있다', '가까운 금속 이온이 카보닐 탄소를 더 친전자적으로 만들 수 있다', '이민 옆 탄소도 공명으로 안정화되어 카바니온이 될 수 있다', '<b>β-케토산의 탈카복실화는 탄소 양이온(카보양이온) 중간체를 거친다</b>', 'Claisen 에스터 축합은 카바니온 중간체를 거친다']),
    answer=ans('D', 'Decarboxylation of a β-keto acid goes through a carbocation intermediate.', '틀림 — 실제로는 카바니온(엔올레이트) 중간체를 거친다'),
    explain=key('CO₂가 떨어질 때 <b>전자쌍은 남은 탄소에 남는다</b> → 탄소 <b>음</b>이온(카바니온). 양이온이 아니다.') +
    fig(flow(['β-케토산 (–CO–CH₂–COO⁻)', '카바니온 = 엔올레이트', '케톤 + CO₂'], arrow_labels=['CO₂ 떨어짐 (전자쌍 남음)', '+ H⁺'], colors=[C['navy'], C['orange'], C['green']], box_h=38, width=540, font=10.5), '') +
    steps('A·C: 옆의 C=O(또는 C=N)가 음전하를 산소(질소)로 나눠 가져(공명) 카바니온을 안정화.', 'B: 금속 이온(Mg²⁺, Zn²⁺)이 카보닐 산소를 잡아당기면 탄소가 더 δ+ → 더 친전자적.', 'E: Claisen 축합(예: 시트르산 생성효소, 16장)은 아세틸-CoA의 카바니온이 카보닐을 공격.') +
    warn('탈카복실화 = CO₂(전자 부족한 쪽)가 떠나고 전자는 남는다 → 카바<b>니온</b>. 이름 함정: carbo<b>cation</b>(양이온) vs carb<b>anion</b>(음이온).', '함정'))

add(n=43, sec=7, diff=2, kind='SA', supp=True, title='별표(*) 원자: 친전자체? 친핵체?',
    en=f'<p>Classify each of the *ed atoms as an electrophile or a nucleophile:</p>{img("tb13_q43.png", "96%")}',
    ko='<p>별표(*)가 붙은 원자를 친전자체와 친핵체로 분류하라.<br>(a) 수산화 이온의 O⁻ (b) 케톤(아세톤)의 카보닐 탄소 (c) 양성자화된 이민(C=N⁺)의 탄소 (d) 카바니온의 탄소 (e) 트라이메틸아민의 N</p>',
    answer=sa('(a) nucleophile (b) electrophile (c) electrophile (d) nucleophile (e) nucleophile', '(a) 친핵체 (b) 친전자체 (c) 친전자체 (d) 친핵체 (e) 친핵체'),
    explain=table(['', '별표 원자', '전자 상태', '답'], [['(a)', 'HO⁻의 O', '음전하 + 비공유 전자쌍', '<b>친핵체</b>'], ['(b)', 'C=O의 C', 'O가 전자를 당겨 δ+', '<b>친전자체</b>'], ['(c)', 'C=N⁺의 C', 'N⁺가 전자를 강하게 당겨 δ+', '<b>친전자체</b>'], ['(d)', 'C⁻ (카바니온)', '음전하 전자쌍', '<b>친핵체</b>'], ['(e)', '(CH₃)₃N의 N', '비공유 전자쌍 1쌍', '<b>친핵체</b>']], cls='left') +
    key('판별 요령: <b>음전하·비공유 전자쌍 → 친핵체</b> / <b>양전하·δ+ (전기음성 원자와 이중결합한 탄소) → 친전자체</b>.') +
    tip('(b)·(c)의 탄소는 둘 다 “이중결합 상대가 전자를 빼앗는” 같은 원리. 이민 탄소는 PLP 반응(18장)의 핵심.', '연결'))
