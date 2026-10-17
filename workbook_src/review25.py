# -*- coding: utf-8 -*-
"""2025 생화학 중간고사 복기 · 실전 서술형 연습.  python3 review25.py → review25.pdf"""
import os, re, sys
os.environ['CH'] = '13'
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from helpers import *
from tblib import sa

HERE = os.path.dirname(os.path.abspath(__file__))
FOOT = '2025 생화학 중간고사 복기 · 실전 서술형 연습 (13–18장)'


def blank_table(head, rows):
    """rows: list of lists; '' → 빈칸(밑줄)."""
    h = '<table class="tb bl"><thead><tr>' + ''.join(f'<th>{x}</th>' for x in head) + '</tr></thead><tbody>'
    for r in rows:
        h += '<tr>' + ''.join(f'<td>{x if x else "<span class=sl></span>"}</td>' for x in r) + '</tr>'
    return h + '</tbody></table>'


def B():
    return '<span class="sl s"></span>'


def glucose_bars():
    return bars([('해당과정', 7, C['blue'], '2 ATP + 2 NADH → 7 (또는 5)'), ('PDH × 2', 5, C['purple'], '2 NADH → 5'),
                 ('TCA × 2', 20, C['green'], '2 GTP + 6 NADH + 2 FADH₂ → 20'), ('합계', 32, C['orange'], '≈ 32 (30–32)')], height=150, vmax=36, width=560)


def redox_ladder():
    from exam13 import redox_ladder_big
    return redox_ladder_big()


ITEMS = []


def add(**kw):
    kw.setdefault('kind', 'SA')
    ITEMS.append(kw)


# ---------------------------------------------------------------- ① 포도당 ATP (2025 서술형 1)
add(n='1', tag='2025 서술형 1', diff=2, title='포도당 1분자의 ATP · NADH · FADH₂ 총계산', where='14장 S2–S5 · 16장 S9',
    en='<p>For one molecule of glucose completely oxidized to CO₂, how many ATP (or GTP), NADH, and FADH₂ are produced in (a) glycolysis, (b) the pyruvate dehydrogenase reaction, and (c) the citric acid cycle? Using 2.5 ATP/NADH and 1.5 ATP/FADH₂, calculate the total ATP yield.</p>',
    ko='<p>포도당 1분자를 CO₂까지 완전 산화할 때 (a) 해당과정 (b) PDH (c) TCA 회로에서 생기는 ATP(GTP)·NADH·FADH₂ 수는? NADH = 2.5, FADH₂ = 1.5 ATP로 총 ATP를 계산하라.</p>'
       + blank_table(['구간', 'ATP/GTP', 'NADH', 'FADH₂', 'ATP 환산'], [['해당과정', '', '', '', ''], ['PDH (×2)', '', '', '', ''], ['TCA (×2)', '', '', '', ''], ['<b>합계</b>', '', '', '', '']]),
    answer=sa('Glycolysis 2 ATP + 2 NADH; PDH 2 NADH; TCA 2 GTP + 6 NADH + 2 FADH₂. Total 4 ATP/GTP + 10 NADH + 2 FADH₂ = 4 + 25 + 3 = <b>32 ATP</b> (30 if cytosolic NADH uses the glycerol-3-phosphate shuttle).',
              '해당 2 ATP + 2 NADH / PDH 2 NADH / TCA 2 GTP + 6 NADH + 2 FADH₂ → 4 + 25 + 3 = <b>32 ATP</b> (셔틀에 따라 30)'),
    explain=table(['구간', 'ATP/GTP', 'NADH', 'FADH₂', 'ATP 환산'], [['해당과정', '2 (4 − 2)', '2', '', '2 + 5 = 7'], ['PDH ×2', '', '2', '', '5'], ['TCA ×2', '2 GTP', '6', '2', '2 + 15 + 3 = 20'], ['<b>합계</b>', '<b>4</b>', '<b>10</b>', '<b>2</b>', '<b>32</b>']])
    + fig(glucose_bars(), '') + key('NADH 10 × 2.5 = 25, FADH₂ 2 × 1.5 = 3, 직접 4 → 32.') + warn('해당과정은 ATP 4개를 만들지만 2개를 먼저 써서(헥소키나아제·PFK-1) <b>알짜 2</b>.', '함정'))

add(n='2', tag='2025 서술형 1 변형', diff=2, title='ATP 계산 변형 — 셔틀 · 무산소 · 기질 수준', where='14장 S3 · 16장 S9',
    en='<p>(a) Net ATP from one glucose under anaerobic conditions (to lactate)?<br>(b) Why is the total 30 in skeletal muscle but 32 in liver/heart?<br>(c) Name the three enzymes that make ATP/GTP by substrate-level phosphorylation in glycolysis and the TCA cycle.<br>(d) The TCA cycle uses no O₂ directly. Why does it stop without O₂?</p>',
    ko='<p>(a) 산소 없을 때(젖산까지) 포도당 1분자의 알짜 ATP는?<br>(b) 근육은 30, 간·심장은 32인 이유는?<br>(c) 해당·TCA에서 기질 수준 인산화로 ATP/GTP를 만드는 효소 3개는?<br>(d) TCA는 O₂를 직접 쓰지 않는데 왜 O₂가 없으면 멈추나?</p>',
    answer=sa('(a) 2 ATP. (b) Cytosolic NADH enters mitochondria by the glycerol-3-phosphate shuttle (→ FADH₂, 1.5) in muscle, but by the malate–aspartate shuttle (→ NADH, 2.5) in liver/heart: 2 × 1 = 2 ATP difference. (c) Phosphoglycerate kinase, pyruvate kinase, succinyl-CoA synthetase. (d) NADH/FADH₂ cannot be reoxidized without O₂, so NAD⁺/FAD run out.',
              '(a) 2 ATP (b) 근육 = 글리세롤-3-인산 셔틀(1.5), 간·심장 = 말산-아스파르트산 셔틀(2.5) → 2개 차이 (c) PGK · 피루브산 키나아제 · 숙시닐-CoA 합성효소 (d) NAD⁺·FAD가 재생되지 않아서'),
    explain=table(['셔틀', '조직', '세포질 NADH 1개', '포도당 총'], [['말산-아스파르트산', '간 · 심장 · 신장', '2.5', '<b>32</b>'], ['글리세롤-3-인산', '골격근 · 뇌', '1.5 (FADH₂로)', '<b>30</b>']])
    + steps('무산소: 해당 2 ATP, NADH는 LDH가 젖산 만들며 NAD⁺로 되돌림 → 추가 ATP 없음.', '산소 = 전자 최종 수용체. NADH가 줄을 못 서면 회로의 탈수소효소들이 멈춘다.'))

# ---------------------------------------------------------------- ② 세 호르몬 (2025 서술형 2)
add(n='3', tag='2025 서술형 2', diff=2, title='인슐린 · 글루카곤 · 에피네프린 효과 표 채우기', where='15장 S9 (슬라이드 47)',
    en='<p>Complete the table: effect (↑, ↓, or – no effect) of insulin, glucagon, and epinephrine on each pathway in liver and muscle.</p>',
    ko='<p>표를 채워라: 간·근육에서 각 호르몬이 각 경로에 주는 효과 (↑ · ↓ · – 영향 없음).</p>'
       + blank_table(['경로', '인슐린·간', '인슐린·근육', '글루카곤·간', '글루카곤·근육', '에피·간', '에피·근육'], [['해당과정'] + [''] * 6, ['당신생'] + [''] * 6, ['글리코겐 합성'] + [''] * 6, ['글리코겐 분해'] + [''] * 6]),
    answer=table(['경로', '인슐린·간', '인슐린·근육', '글루카곤·간', '글루카곤·근육', '에피·간', '에피·근육'], [
        ['해당과정', '↑', '↑', '↓', '–', '↓', '<b>↑</b>'], ['당신생', '↓', '–', '↑', '–', '↑', '–'], ['글리코겐 합성', '↑', '↑', '↓', '–', '↓', '↓'], ['글리코겐 분해', '↓', '↓', '↑', '–', '↑', '↑']]),
    explain=steps('글루카곤·근육 열은 전부 “–” — 근육엔 <b>글루카곤 수용체가 없다</b>.', '근육 당신생 열도 “–” — 근육엔 당신생 효소(G6Pase 등)가 없다.', '에피네프린: 간은 해당 ↓(포도당을 내보내야), 근육은 해당 ↑(자기가 태워 도망가야).')
    + key('인슐린 = 저장하라 / 글루카곤 = 꺼내라(간) / 에피네프린 = 위기! 당장 써라(간 + 근육).'))

add(n='4', tag='2025 서술형 2', diff=2, title='세 호르몬은 어떻게 작용하나 — 신호 경로', where='15장 S8–S9',
    en='<p>Describe how insulin, glucagon, and epinephrine act: the stimulus for secretion, the receptor/second messenger, the key kinase, and the effect on glycogen phosphorylase and glycogen synthase.</p>',
    ko='<p>인슐린·글루카곤·에피네프린의 작용을 설명하라: 분비 자극, 수용체·2차 전령, 핵심 키나아제, 글리코겐 인산화효소·합성효소에 대한 효과.</p>'
       + blank_table(['', '인슐린', '글루카곤', '에피네프린'], [['분비 세포 · 자극', '', '', ''], ['수용체 · 2차 전령', '', '', ''], ['핵심 키나아제', '', '', ''], ['인산화효소 / 합성효소', '', '', '']]),
    answer=table(['', '인슐린', '글루카곤', '에피네프린'], [['분비 · 자극', '이자 β · 혈당 ↑', '이자 α · 혈당 ↓', '부신수질 · 위기'], ['수용체 · 전령', '수용체 티로신 키나아제', 'GPCR → Gs → cAMP', 'GPCR(β) → cAMP'], ['키나아제', 'PKB(Akt) → GSK3 ⊗, PP1 ▲', 'PKA', 'PKA (+ Ca²⁺)'], ['인산화효소 / GS', 'OFF / <b>ON</b>', '<b>ON</b> / OFF', '<b>ON</b> / OFF']]),
    explain=vflow(['글루카곤·에피네프린 → GPCR → Gs', '아데닐산 고리화효소 → cAMP ↑', 'PKA 활성', '인산화효소 b 키나아제 → 인산화효소 a (분해 ON)', 'GS 인산화 → OFF (합성 OFF)'], colors=[C['red'], C['orange'], C['orange'], C['green'], C['gray']], box_h=24, gap=12, width=540, font=10.5, bw=420)
    + key('인산화 = 분해 ON · 합성 OFF. 인슐린은 PP1로 인산을 떼어 반대로(합성 ON).') + tip('간에선 PKA가 PFK-2를 인산화 → F2,6BP ↓ → 해당 ↓ · 당신생 ↑.', '간'))

# ---------------------------------------------------------------- ③ 간 vs 근육 (2025 서술형 3)
add(n='5', tag='2025 서술형 3', diff=1, title='간 vs 근육 괄호 채우기', where='15장 S10 (슬라이드 56)',
    en='<p>Fill in the blanks.</p>',
    ko=f'''<ol style="line-height:2.1;margin:.2em 0;padding-left:1.3em">
<li>근육에는 ( {B()} ) 수용체가 없고 ( {B()} ) 효소가 없다. <b>← 2025 기출</b></li>
<li>근육은 ( {B()} )가 없어서 글리코겐에서 나온 G6P를 혈액으로 내보내지 못하고 ( {B()} )에만 쓴다.</li>
<li>간 글리코겐의 역할은 ( {B()} ) 유지, 근육 글리코겐의 역할은 ( {B()} ) 공급이다.</li>
<li>에피네프린이 오면 간의 해당과정은 ( ↑ / ↓ ), 근육의 해당과정은 ( ↑ / ↓ ).</li>
<li>근육의 젖산은 간으로 가 포도당이 되어 돌아온다 = ( {B()} ) 회로. 알라닌으로 질소까지 나르면 ( {B()} ) 회로.</li>
<li>근육형 피루브산 키나아제는 PKA에 의해 ( 인산화된다 / 인산화되지 않는다 ).</li></ol>''',
    answer=sa('1 glucagon; gluconeogenic (G6Pase) 2 glucose-6-phosphatase; its own glycolysis 3 blood glucose; ATP for muscle 4 ↓; ↑ 5 Cori; glucose–alanine 6 is not',
              '① 글루카곤 · 당신생(G6Pase) ② G6Pase · 자기 해당과정 ③ 혈당 · 근육 자신의 ATP ④ ↓ · ↑ ⑤ 코리 · 포도당-알라닌 ⑥ 인산화되지 않는다'),
    explain=table(['', '간', '근육'], [['글루카곤 수용체', '있음', '<b>없음</b>'], ['G6Pase · 당신생 효소', '있음', '<b>없음</b>'], ['글리코겐 용도', '혈당으로 내보냄', '자기 해당 연료'], ['에피네프린 시 해당', '↓', '↑'], ['PK의 PKA 조절', '있음 (L형)', '없음 (M형)']])
    + key('근육 = 이기적인 소비자, 간 = 몸 전체의 포도당 은행.'))

# ---------------------------------------------------------------- ④ 산화환원 (복기: 생각보다 많이 등장)
add(n='6', tag='복기 · 산화환원 개념', diff=1, title='누가 산화되고 누가 환원되나', where='13장 S10–S13',
    en='<p>For each reaction, identify the species oxidized, the species reduced, the oxidizing agent, and the reducing agent.<br>(a) Pyruvate + NADH + H⁺ → lactate + NAD⁺<br>(b) Succinate + FAD → fumarate + FADH₂<br>(c) Malate + NAD⁺ → oxaloacetate + NADH + H⁺<br>(d) Rank by oxidation state of carbon: CO₂, CH₄, CH₃OH, HCOOH, HCHO.</p>',
    ko='<p>각 반응에서 산화되는 것 · 환원되는 것 · 산화제 · 환원제는?<br>(a) 피루브산 + NADH → 젖산 + NAD⁺ (b) 숙신산 + FAD → 푸마르산 + FADH₂ (c) 말산 + NAD⁺ → OAA + NADH<br>(d) 탄소 산화 상태 순서: CO₂, CH₄, CH₃OH, HCOOH, HCHO</p>'
       + blank_table(['', '산화됨', '환원됨', '산화제', '환원제'], [['(a)', '', '', '', ''], ['(b)', '', '', '', ''], ['(c)', '', '', '', '']]),
    answer=table(['', '산화됨', '환원됨', '산화제', '환원제'], [['(a)', 'NADH', '피루브산', '피루브산', 'NADH'], ['(b)', '숙신산', 'FAD', 'FAD', '숙신산'], ['(c)', '말산', 'NAD⁺', 'NAD⁺', '말산']])
    + '<p style="margin:.4em 0 0"><b>(d)</b> CH₄ &lt; CH₃OH &lt; HCHO &lt; HCOOH &lt; CO₂ (가장 환원 → 가장 산화)</p>',
    explain=key('산화 = 전자(H) 잃음, 환원 = 전자(H) 얻음. <b>산화제 = 자기가 환원되는 쪽</b>, 환원제 = 자기가 산화되는 쪽.')
    + steps('H가 붙으면 환원, 떨어지면 산화 (NAD⁺ → NADH = 환원).', '탄소에 O가 많을수록, H가 적을수록 산화 상태 ↑.')
    + warn('“산화제”는 산화<b>되는</b> 것이 아니라 남을 산화<b>시키는</b> 것.', '함정'))

add(n='7', tag='복기 · 13장 계산', diff=2, title='ΔE′° → ΔG′° 계산', where='13장 S11–S12',
    en='<p>Using E′° values (NAD⁺/NADH −0.320 V; FAD/FADH₂ −0.219 V; acetaldehyde/ethanol −0.197 V; ½O₂/H₂O +0.816 V; F = 96.48 kJ/V·mol), calculate ΔE′° and ΔG′° for:<br>(a) NADH + ½O₂ + H⁺ → NAD⁺ + H₂O<br>(b) FADH₂ + ½O₂ → FAD + H₂O<br>(c) Acetaldehyde + NADH + H⁺ → ethanol + NAD⁺</p>',
    ko='<p>표준 환원 전위로 ΔE′°와 ΔG′°를 구하라: (a) NADH → O₂ (b) FADH₂ → O₂ (c) 아세트알데하이드 + NADH → 에탄올</p>'
       + blank_table(['', '전자 공여체', '전자 수용체', 'ΔE′° (V)', 'ΔG′° (kJ/mol)'], [['(a)', '', '', '', ''], ['(b)', '', '', '', ''], ['(c)', '', '', '', '']]),
    answer=table(['', 'ΔE′° (V)', 'ΔG′° (kJ/mol)'], [['(a)', '0.816 − (−0.320) = <b>1.136</b>', '−2 × 96.48 × 1.136 = <b>−219</b>'], ['(b)', '0.816 − (−0.219) = <b>1.035</b>', '<b>−200</b>'], ['(c)', '−0.197 − (−0.320) = <b>0.123</b>', '<b>−23.7</b>']]),
    explain=eq('ΔE′° = E′°(수용체) − E′°(공여체)', 'ΔG′° = −n F ΔE′°  (n = 2)') + fig(redox_ladder(), '전자는 아래(−) → 위(+)로 떨어진다')
    + steps('수용체 = 전자를 받는 쪽 = 환원되는 쪽 (O₂, 아세트알데하이드).', 'ΔE > 0 → ΔG < 0 → 자발.')
    + tip('(a)/(b) 비율 ≈ 2.5 : 1.5 ATP와 같은 이유 — FADH₂는 더 낮은 곳에서 출발.', '연결'))

add(n='8', tag='복기 · 13장 계산', diff=3, title='네른스트 식 — 비율이 바뀌면 E도 바뀐다', where='13장 S12',
    en='<p>Calculate E for the NAD⁺/NADH couple at 25 °C when [NAD⁺]/[NADH] = 10 (E′° = −0.320 V, n = 2, RT/F = 0.0257 V). Is NADH then a better or worse electron donor than under standard conditions?</p>',
    ko='<p>[NAD⁺]/[NADH] = 10일 때 NAD⁺/NADH의 E는? 표준보다 전자를 더 잘 주나, 못 주나?</p>',
    answer=sa('E = −0.320 + (0.0257/2) ln 10 = −0.320 + 0.0296 = <b>−0.290 V</b>. E is less negative, so NADH is a slightly weaker electron donor.',
              'E = −0.290 V. 덜 음수 → NADH가 전자를 주려는 힘이 약간 약해진다.'),
    explain=eq('E = E′° + (RT / nF) ln ( [산화형] / [환원형] )', '= −0.320 + 0.01285 × 2.303 = −0.290 V')
    + key('산화형이 많을수록 E ↑ (전자를 받으려는 쪽으로). ΔG = ΔG′° + RT ln Q와 같은 모양.') + warn('ln 안은 <b>산화형/환원형</b>. 거꾸로 넣으면 부호가 반대.', '함정'))

add(n='9', tag='복기 · 13장 계산', diff=2, title='K′eq · ΔG′° · 실제 ΔG · 짝지음', where='13장 S5–S8',
    en='<p>(a) G1P ⇌ G6P has K′eq = 19 at 25 °C. Calculate ΔG′° (RT = 2.479 kJ/mol).<br>(b) FBP → DHAP + G3P has ΔG′° = +23.8 kJ/mol. Calculate ΔG when [FBP] = 1 mM and [DHAP] = [G3P] = 10 μM.<br>(c) Glucose + Pᵢ → G6P (ΔG′° = +13.8) is coupled to ATP hydrolysis (−30.5). Find the overall ΔG′° and K′eq trend.</p>',
    ko='<p>(a) G1P ⇌ G6P, K′eq = 19 → ΔG′°? (b) 알돌레이스 반응(ΔG′° +23.8), [FBP] 1 mM, [DHAP] = [G3P] = 10 μM일 때 ΔG? (c) 포도당 + Pᵢ → G6P(+13.8)를 ATP 가수분해(−30.5)와 짝지으면?</p>',
    answer=sa('(a) −RT ln 19 = −2.479 × 2.944 = <b>−7.3 kJ/mol</b>. (b) Q = (10⁻⁵)²/10⁻³ = 10⁻⁷; ΔG = 23.8 + 2.479 ln 10⁻⁷ = 23.8 − 40.0 = <b>−16.2 kJ/mol</b> (proceeds). (c) 13.8 − 30.5 = <b>−16.7 kJ/mol</b>; K′eq becomes ≫ 1.',
              '(a) −7.3 (b) −16.2 → 세포에선 진행 (c) −16.7 → 자발'),
    explain=eq('ΔG′° = −RT ln K′eq', 'ΔG = ΔG′° + RT ln Q') + key('ΔG′°가 +여도 산물이 매우 적으면(Q ≪ 1) 실제 ΔG는 −가 될 수 있다.') + steps('짝지은 반응: ΔG′°는 <b>더하고</b>, K′eq는 <b>곱한다</b>.', 'M 단위로 바꿔 넣기: 10 μM = 10⁻⁵ M.'))

add(n='10', tag='복기 · 13장 계산', diff=2, title='세포 속 ATP 가수분해의 실제 ΔG (ΔGp)', where='13장 S3',
    en='<p>In human erythrocytes [ATP] = 2.25 mM, [ADP] = 0.25 mM, [Pᵢ] = 1.65 mM. Calculate the actual ΔG for ATP hydrolysis at 37 °C (ΔG′° = −30.5 kJ/mol; RT = 2.58 kJ/mol).</p>',
    ko='<p>적혈구의 [ATP] 2.25 mM, [ADP] 0.25 mM, [Pᵢ] 1.65 mM일 때 37 °C에서 ATP 가수분해의 실제 ΔG는?</p>',
    answer=sa('Q = (0.25 × 10⁻³)(1.65 × 10⁻³)/(2.25 × 10⁻³) = 1.83 × 10⁻⁴; ΔG = −30.5 + 2.58 ln(1.83 × 10⁻⁴) = −30.5 − 22.2 = <b>−52.7 kJ/mol</b> (≈ −52).',
              'Q = 1.83 × 10⁻⁴ → ΔG ≈ <b>−52 kJ/mol</b> (표준값 −30.5보다 훨씬 크다)'),
    explain=eq('Q = [ADP][Pᵢ] / [ATP]', 'ΔGp = −30.5 + RT ln Q') + key('세포는 ATP를 ADP보다 훨씬 많이 유지 → 실제 에너지 ≈ −50~−65 kJ/mol.') + warn('mM을 M으로 바꾸는 걸 잊지 말 것 (10⁻³).', '실수'))

# ---------------------------------------------------------------- ⑤ 복기 언급: B12 · 질환
add(n='11', tag='복기 · B₁₂', diff=2, title='비타민 B₁₂ 한 장 정리', where='17장 S9 · 18장 S13',
    en='<p>What is coenzyme B₁₂? Name the two human enzymes that require it, and explain why B₁₂ deficiency raises both methylmalonic acid and homocysteine and causes pernicious anemia.</p>',
    ko='<p>조효소 B₁₂란? B₁₂가 필요한 사람의 두 효소와, 결핍 시 메틸말론산·호모시스테인이 함께 오르고 악성빈혈이 생기는 이유는?</p>'
       + blank_table(['B₁₂ 효소', '반응', '결핍 시 쌓이는 것'], [['', '', ''], ['', '', '']]),
    answer=sa('Cobalamin: Co³⁺ in a corrin ring with a Co–C bond to 5′-deoxyadenosine; homolytic cleavage makes a radical that swaps H and a group on adjacent carbons. (1) Methylmalonyl-CoA mutase (L-methylmalonyl-CoA → succinyl-CoA) → methylmalonic acid ↑. (2) Methionine synthase (homocysteine + N⁵-methyl-THF → Met + THF) → homocysteine ↑; N⁵-methyl-THF trap → less THF for thymidine → DNA synthesis ↓ → megaloblastic (pernicious) anemia.',
              '코린 고리 + 코발트 + Co–C 결합(라디칼). ① 메틸말로닐-CoA 뮤테이스 → 메틸말론산 ↑ ② 메티오닌 합성효소 → 호모시스테인 ↑ + 메틸 함정 → DNA 합성 ↓ → 악성빈혈'),
    explain=table(['효소', '어디서 쓰이나', '막히면'], [['메틸말로닐-CoA 뮤테이스', '홀수 지방산 · I M T V', '메틸말론산 ↑'], ['메티오닌 합성효소', '활성 메틸 회로', '호모시스테인 ↑ · 메틸 함정']])
    + key('호모시스테인 ↑ + 메틸말론산 ↑ 동시 = B₁₂ 결핍의 지문 (엽산 결핍은 호모시스테인만 ↑).') + tip('B₁₂는 동물성 식품에만, 흡수에 내인자 필요 → 비건 · 위절제 · 내인자 결함이 원인.', '원인'))

add(n='12', tag='복기 · 질환 원인', diff=2, title='질환은 어디가 막혀서 생기나', where='14장 PPP · 17장 · 18장 S9·S14',
    en='<p>For each disorder, name the defective enzyme (or missing factor) and what accumulates or is lacking.</p>',
    ko='<p>각 질환의 결함 효소(또는 부족한 인자)와 쌓이거나 모자라는 것을 써라.</p>'
       + blank_table(['질환', '결함 효소 · 원인', '쌓임 / 부족'], [['페닐케톤뇨증 (PKU)', '', ''], ['단풍당뇨증 (MSUD)', '', ''], ['알캅톤뇨증', '', ''], ['백색증', '', ''], ['잠두중독증 (favism)', '', ''], ['악성빈혈', '', ''], ['OTC 결핍증', '', '']]),
    answer=table(['질환', '결함', '결과'], [['PKU', '페닐알라닌 수산화효소 (또는 THBP 재생)', 'Phe · 페닐피루브산 ↑, Tyr ↓'], ['MSUD', '가지사슬 α-케토산 탈수소효소', 'V·I·L의 α-케토산 ↑ (단풍 냄새)'], ['알캅톤뇨증', '호모젠티스산 이산소화효소', '호모젠티스산 ↑ (검은 소변)'], ['백색증', '티로시네이스', '멜라닌 없음'], ['잠두중독증', '<b>G6PD</b> (PPP 첫 효소)', 'NADPH ↓ → GSH ↓ → 용혈'], ['악성빈혈', '내인자 → B₁₂ 흡수 불가', '메틸말론산 · 호모시스테인 ↑'], ['OTC 결핍', '요소 회로 ②', 'NH₄⁺ ↑ (고암모니아혈증)']]),
    explain=key('원리 하나: <b>막힌 곳 앞은 쌓이고, 뒤는 모자란다</b>.')
    + steps('잠두중독증: 잠두콩(디비신)·산화성 약물 → ROS ↑ → G6PD 결핍이면 NADPH로 글루타티온을 못 되살림 → 적혈구 막 손상 → 용혈성 빈혈.', 'MSUD는 PDH와 같은 방식의 산화적 탈카복실화 효소 결함.')
    + warn('복기: “왜 · 어디서 유발되는지” 묻는 문제가 나왔다 → 효소 이름까지 외우기.', '시험'))


def front():
    rows = ''.join(f'<tr><td class="no">{it["n"]}</td><td>{it["title"]} <span class="en">{it["tag"]} · {it["where"]}</span></td></tr>' for it in ITEMS)
    return f'''<h2 class="pt"><span class="n">2025</span> 생화학 중간고사 복기 — 무엇이 나왔나 <span class="en2">13–18장 · 선배 복기 정리</span></h2>
<p class="lead">복기 메모를 정리하고, <b>서술형 3문제</b>와 복기가 강조한 <b>산화환원 · 13장 계산 · B₁₂ · 질환 원인</b>을 실전 연습 12문제로 만들었다. 각 문제는 왼쪽에서 직접 쓰고, 오른쪽 정답으로 확인한다.</p>
<div class="grid2"><div><div class="card"><h4>📝 복기 메모 요약</h4>{table(['포인트', '대비'], [
 ['산화환원 개념이 생각보다 많이', '13장 S10–S13 + 연습 6–8'], ['13장 계산 문제 꽤 나옴', '13장 테스트뱅크 + 연습 7–10'], ['17 · 18장은 테스트뱅크에서 본 문제 많음', '17 · 18장 기출 전부 풀기'],
 ['15 · 16장: 회로 · 반응물 · 효소 외우기', '요약노트 표 암기'], ['B₁₂가 뭔지 알고 가기', '연습 11'], ['PKU · MSUD 같은 질환 원인', '연습 12'], ['Favism(잠두중독증) 원인', '연습 12 · 14장 PPP'],
 ['15장 수용체는 별로 안 나옴', '테스트뱅크 위주로 가볍게'], ['구조 · 화학 반응 기전은 거의 없음', '구조 암기보다 흐름·효소']], cls='left')}</div>
 {key('테스트뱅크에서 절반 조금 넘게 나왔다. 나머지는 PPT의 큰 줄기(표 · 회로)에서.')}</div>
<div><div class="card"><h4>✏️ 주관식 3문제 (2025)</h4><ol style="margin:.2em 0;padding-left:1.3em;line-height:1.7">
 <li>포도당 1분자 → 해당 · TCA · 전자전달 후 ATP · NADH · FADH₂ 수 → <b>총 ATP</b> <span class="en">→ 연습 1–2</span></li>
 <li>글루카곤 · 인슐린 · 에피네프린의 작용 (PPT 표) <span class="en">→ 연습 3–4</span></li>
 <li>근육에는 ( 글루카곤 ) 수용체가 없고 ( 당신생 ) 효소가 없다 <span class="en">→ 연습 5</span></li></ol></div>
 <div class="card" style="margin-top:3mm"><h4>📋 연습 문제 목록</h4><table class="toc">{rows}</table></div></div></div>'''


def render_item(it):
    return f'''
<div class="ph"><div class="badge" style="background:#b91c1c"><small>2025 복기</small><b>연습 {it['n']}</b></div>
 <div class="ttl"><span class="ko">{it['title']}</span><span class="en">{it['tag']} · 관련 ▸ {it['where']}</span></div>
 <div class="meta"><span class="tag">서술형 · 실전</span>{stars(it['diff'])}</div></div>
<div class="cols">
 <div class="col">
  <div class="blk orig"><span class="lab">ORIGINAL · 원문</span>{it['en']}</div>
  <div class="blk trans"><span class="lab">번역</span>{it['ko']}</div>
  <div class="blk blank"><span class="lab">풀이 · 직접 풀어 보기</span><span class="hint">오른쪽을 가리고 풀어 보세요</span></div>
 </div>
 <div class="col">
  <div class="blk ans"><span class="lab">정답 · ANSWER</span>{it['answer']}</div>
  <div class="blk exp"><span class="lab">풀이</span>{it['explain']}</div>
 </div>
</div>'''


CSS2 = r'''
table.bl{table-layout:fixed;width:100%}
table.bl td{height:7.5mm}
table.bl td .sl{min-width:0;width:80%}
.sl{display:inline-block;min-width:18mm;border-bottom:1.2px solid #94a3b8;height:1em}
.sl.s{min-width:22mm}
'''


def main():
    import build as Bd
    import tblib
    from exam13 import EXTRA_CSS, FIT
    from playwright.sync_api import sync_playwright
    import pymupdf
    P = Bd.Pager()
    P.add(front(), 'front')
    for it in ITEMS:
        P.add(render_item(it), 'item')
    html = re.sub(r'<span>Lehninger 8e · Ch\.\d+ [^<]*</span>', f'<span>{FOOT}</span>', P.html())
    doc = f'''<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>{FOOT}</title>
<style>{Bd.CSS}{EXTRA_CSS}{tblib.TB_CSS}{CSS2}</style></head><body>{html}{FIT}</body></html>'''
    hp = os.path.join(HERE, 'review25.html')
    open(hp, 'w').write(doc)
    tmp = os.path.join(HERE, 'review25_tmp.pdf')
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome')
        pg = b.new_page()
        pg.goto('file://' + hp)
        pg.wait_for_timeout(900)
        print('fit', pg.evaluate('window.FIT'))
        print('zoom', pg.evaluate('window.ZOOM'))
        pg.pdf(path=tmp, width='320mm', height='200mm', print_background=True, prefer_css_page_size=True)
        b.close()
    d = pymupdf.open(tmp)
    d.set_metadata({'title': FOOT, 'author': 'Claude'})
    d.save(os.path.join(HERE, 'review25.pdf'), garbage=3, deflate=True)
    print('pages', len(d), 'expected', len(P.pages))


if __name__ == '__main__':
    main()
