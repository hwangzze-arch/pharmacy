# -*- coding: utf-8 -*-
"""14장 테스트뱅크 (lehninger6e_tb_ch14). 강의 범위 밖 제외: 11·12(공유결합 효소 중간체), 47(해당 효소 유전병), 56(알돌 절단 기전)."""
from helpers import *
from tblib import mcq, ans, sa
from exam14 import gly_map, pyruvate_fates, gng_bypass, ppp_svg, phospho_why
from exam13 import hill

DG = 'ΔG′°'
TB = []


def add(**kw):
    kw.setdefault('kind', 'MC')
    TB.append(kw)


def carbon_map():
    return table(['포도당 탄소', '알돌라아제 후', 'TPI 후 G3P의 위치', '피루브산', '젖산', '에탄올'], [
        ['C-1 · C-6', 'C-1 → DHAP / C-6 → G3P', '<b>C-3</b> (–CH₂OP)', '<b>C-3 메틸</b>', 'C-3 메틸', '<b>C-2 메틸</b>'],
        ['C-2 · C-5', 'C-2 → DHAP / C-5 → G3P', '<b>C-2</b> (–CHOH)', '<b>C-2 카보닐</b>', 'C-2 (–OH 달린 탄소)', 'C-1 (–CH₂OH)'],
        ['C-3 · C-4', 'C-3 → DHAP / C-4 → G3P', '<b>C-1</b> (–CHO)', '<b>C-1 카복실</b>', 'C-1 카복실', 'CO₂로 빠짐']], cls='left')


def carbon_flow():
    W, H = 560, 170
    b = arrowdef('cfm', C['gray'])
    cols = ['#dc2626', '#2563eb', '#16a34a', '#16a34a', '#2563eb', '#dc2626']
    for i in range(6):
        x = 40 + i * 40
        b += f'<circle cx="{x}" cy="40" r="14" fill="{cols[i]}"/>' + T(x, 45, f'C{i+1}', 10, 'white', weight=900)
    b += T(140, 14, '포도당 (F1,6BP)', 11, C['navy'], weight=900)
    b += f'<line x1="140" y1="58" x2="140" y2="78" stroke="{C["gray"]}" stroke-width="2" marker-end="url(#cfm)"/>' + T(150, 72, '알돌라아제 → 3C + 3C, TPI로 DHAP → G3P', 9.5, C['orange'], 'start', 700)
    for j, (lab, c) in enumerate([('C-1 (CHO)', '#16a34a'), ('C-2', '#2563eb'), ('C-3 (CH₂OP)', '#dc2626')]):
        x = 60 + j * 90
        b += f'<rect x="{x-38}" y="96" width="76" height="26" rx="8" fill="white" stroke="{c}" stroke-width="2"/>' + T(x, 113, lab, 9.5, c, weight=900)
    b += T(150, 142, 'G3P 2개 (두 분자가 똑같아진다)', 10.5, C['navy'], weight=900)
    b += T(430, 30, '같은 색끼리 같은 자리로', 11, C['gray'], weight=900)
    b += T(430, 60, '빨강 C1·C6 → 피루브산 메틸', 10.5, '#dc2626', weight=700) + T(430, 82, '파랑 C2·C5 → 피루브산 카보닐', 10.5, '#2563eb', weight=700) + T(430, 104, '초록 C3·C4 → 피루브산 카복실', 10.5, '#16a34a', weight=700)
    b += T(430, 132, '→ 에탄올 발효면 초록은 CO₂', 10.5, C['orange'], weight=700)
    return svg(W, H, b)


def bpg_svg():
    W, H = 420, 170
    b = arrowdef('bp', C['red'])
    rows = [('C1', 'O=C–O–PO₃²⁻', C['red'], '아실 인산 (고에너지, −49.3)'), ('C2', 'H–C–OH', C['ink'], ''), ('C3', 'H₂C–O–PO₃²⁻', C['blue'], '인산 에스터 (저에너지)')]
    for i, (c, s, col, note) in enumerate(rows):
        y = 34 + i * 48
        b += T(30, y + 4, c, 11, C['gray'], weight=900) + T(130, y + 5, s, 14, col, weight=900, family='Noto Serif')
        if note:
            b += T(250, y + 5, '← ' + note, 10.5, col, 'start', 700)
    b += f'<ellipse cx="160" cy="38" rx="56" ry="18" fill="none" stroke="{C["red"]}" stroke-width="2.4"/>'
    b += f'<line x1="70" y1="10" x2="70" y2="150" stroke="{C["light"]}" stroke-width="2"/>'
    return svg(W, H, b)


def ppp_c1_graph():
    W, H = 520, 210
    L, R, Tp, B = 50, 490, 40, 170
    b = f'<line x1="{L}" y1="{B}" x2="{R}" y2="{B}" stroke="{C["gray"]}"/><line x1="{L}" y1="{Tp}" x2="{L}" y2="{B}" stroke="{C["gray"]}"/>'
    import math
    def curve(k, col, lab, ly):
        pts = ' '.join(f'{L + t*(R-L)/60:.1f},{B - (B-Tp)*0.9*(1-math.exp(-k*t)):.1f}' for t in range(0, 61, 2))
        return f'<polyline points="{pts}" fill="none" stroke="{col}" stroke-width="3"/>' + T(R - 10, ly, lab, 11, col, 'end', 900)
    b += curve(0.12, C['red'], '[1-¹⁴C]포도당 → 빨리, 많이', 22)
    b += curve(0.025, C['blue'], '[6-¹⁴C]포도당 → 늦게, 적게', 112)
    b += T((L + R) / 2, B + 22, '시간 →', 10.5, C['gray']) + f'<text x="20" y="{(Tp+B)/2}" font-size="10" fill="{C["gray"]}" text-anchor="middle" transform="rotate(-90 20 {(Tp+B)/2})" font-weight="700">¹⁴CO₂ 방출량</text>'
    return svg(W, H, b)


# ================================================================ S1 (0)
add(n=1, sec=0, diff=2, title='포도당 → 젖산 11단계는 무엇의 예?',
    en=mcq('Glycolysis is the name given to a metabolic pathway occurring in many different cell types. It consists of 11 enzymatic steps that convert glucose to lactic acid. Glycolysis is an example of:', ['aerobic metabolism.', 'anabolic metabolism.', 'a net reductive process.', 'fermentation.', 'oxidative phosphorylation.']),
    ko=mcq('해당과정은 여러 세포에서 일어나는 대사 경로로, 포도당을 젖산으로 바꾸는 11개의 효소 단계로 이루어진다. 이것은 무엇의 예인가?', ['유산소 대사', '동화 대사', '알짜 환원 과정', '<b>발효</b>', '산화적 인산화']),
    answer=ans('D', 'fermentation', '발효 (산소 없이 포도당 → 젖산)'),
    explain=key('해당 10단계 + 젖산 탈수소효소(피루브산 → 젖산) 1단계 = <b>11단계</b> = 젖산 발효.') +
    steps('산소를 쓰지 않는다 → A·E 틀림.', '큰 분자를 쪼갠다(이화) → B 틀림.', '포도당 → 젖산은 전체적으로 산화도 환원도 아님(NADH를 만들고 다시 씀) → C 틀림.') +
    tip('발효 = 산소 없이 유기물이 전자를 주고받으며 ATP를 얻는 것.', '정의'))

# ================================================================ S2 (1) 준비 단계
add(n=7, sec=1, diff=2, title='ATP를 기질로 쓰는 반응',
    en=mcq('Which of the following reactions in glycolysis requires ATP as a substrate?', ['Hexokinase', 'Glyceraldehyde-3-phosphate dehydrogenase', 'Pyruvate kinase', 'Aldolase', 'Phosphoglycerate kinase']),
    ko=mcq('해당과정에서 ATP를 기질로 쓰는 반응은?', ['<b>헥소키나아제</b>', 'GAPDH', '피루브산 키나아제', '알돌라아제', 'PGK']),
    answer=ans('A', 'Hexokinase', '헥소키나아제 (포도당 + ATP → G6P + ADP)'),
    explain=fig(gly_map(), '') + key('ATP를 <b>쓰는</b> 곳 = ① 헥소키나아제, ③ PFK-1 (준비 단계). ATP를 <b>만드는</b> 곳 = ⑦ PGK, ⑩ PK.') +
    warn('PGK·PK도 “키나아제”지만 ATP를 만드는 쪽. 이름에 속지 말자.', '함정'))

add(n=9, sec=1, diff=2, title='알도스 → 케토스 이성질화',
    en=mcq('Which of the following reactions in glycolysis is an aldose to ketose isomerization?', ['Enolase', 'Phosphoglycerate mutase', 'Phosphohexose isomerase', 'Aldolase', 'Glyceraldehyde-3-phosphate dehydrogenase']),
    ko=mcq('해당과정에서 알도스 → 케토스 이성질화 반응은?', ['에놀레이스', 'PGM', '<b>포스포헥소스 이성질화효소</b>', '알돌라아제', 'GAPDH']),
    answer=ans('C', 'Phosphohexose isomerase', '포스포헥소스 이성질화효소: G6P(알도스) → F6P(케토스)'),
    explain=table(['반응', '방향', '효소'], [['② G6P → F6P', '<b>알도스 → 케토스</b>', '포스포헥소스 이성질화효소'], ['⑤ DHAP → G3P', '<b>케토스 → 알도스</b>', 'TPI']]) +
    key('알도스 = –CHO(알데하이드), 케토스 = C=O(케톤). G6P는 C1이 알데하이드, F6P는 C2가 케톤.') + tip('바로 다음 문제(TB 14-10)가 반대 방향을 묻는다.', '연결'))

add(n=10, sec=1, diff=2, title='케토스 → 알도스 이성질화',
    en=mcq('Which of the following reactions in glycolysis is a ketose to aldose isomerization?', ['Hexokinase', 'Phosphoglycerate mutase', 'Enolase', 'Aldolase', 'Triose phosphate isomerase']),
    ko=mcq('해당과정에서 케토스 → 알도스 이성질화 반응은?', ['헥소키나아제', 'PGM', '에놀레이스', '알돌라아제', '<b>삼탄당 인산 이성질화효소(TPI)</b>']),
    answer=ans('E', 'Triose phosphate isomerase', 'TPI: DHAP(케토스) → G3P(알도스)'),
    explain=key('DHAP는 가운데 C=O(케톤), G3P는 끝에 –CHO(알데하이드). 수익 단계로 가는 건 G3P뿐이라 DHAP를 바꿔 줘야 한다.') +
    steps('B(뮤테이스)는 인산 위치만 옮김 (3PG → 2PG).', 'D(알돌라아제)는 6C를 3C 두 개로 자르는 반응.') + tip('“이성질화효소(isomerase)” 이름이 붙은 두 효소가 답 — ② 알도스→케토스, ⑤ 케토스→알도스.', '외우기'))

add(n=3, sec=1, diff=2, title='G6P ⇌ F6P, G6P가 2배',
    en=mcq(f'When a mixture of glucose 6-phosphate and fructose 6-phosphate is incubated with phosphohexose isomerase, the final mixture contains twice as much glucose 6-phosphate as fructose 6-phosphate. Which statement is most nearly correct for Glucose 6-phosphate ↔ fructose 6-phosphate? (R = 8.315 J/mol·K, T = 298 K)', [f'{DG} is +1.7 kJ/mol.', f'{DG} is –1.7 kJ/mol.', f'{DG} is incalculably large and negative.', f'{DG} is incalculably large and positive.', f'{DG} is zero.']),
    ko=mcq('G6P와 F6P를 포스포헥소스 이성질화효소와 평형까지 두었더니 G6P가 F6P의 2배. G6P ⇌ F6P에 대해 가장 맞는 것은?', [f'{DG} = +1.7 kJ/mol', f'{DG} = −1.7 kJ/mol', '계산 불가할 만큼 크고 음수', '계산 불가할 만큼 크고 양수', '0']),
    answer=ans('A', f'{DG} is +1.7 kJ/mol', f'{DG} = +1.7 kJ/mol'),
    explain=align([('K′eq', '[F6P]/[G6P] = 1/2', ''), ('ΔG′°', '−(2.48)(ln 0.5) = <b>+1.7 kJ/mol</b>', '')]) +
    tip('13장 기출 13-4와 같은 문제. 해당 ②단계의 교과서 값도 +1.7.', '연결'))

add(n=4, sec=1, diff=2, title='알돌라아제 (ΔG′° +23.8) 진행 조건',
    en=mcq(f'In glycolysis, fructose 1,6-bisphosphate is converted to two products with {DG} of 23.8 kJ/mol. Under what conditions (encountered in a normal cell) will ΔG be negative, enabling the reaction to proceed to the right?', ['If the concentrations of the two products are high relative to that of fructose 1,6-bisphosphate.', f'The reaction will not go to the right spontaneously under any conditions because the {DG} is positive.', 'Under standard conditions, enough energy is released to drive the reaction to the right.', 'When there is a high concentration of fructose 1,6-bisphosphate relative to the concentration of products.', 'When there is a high concentration of products relative to the concentration of fructose 1,6-bisphosphate.']),
    ko=mcq('F1,6BP가 두 산물로 쪼개지는 반응의 ΔG′° = +23.8. 정상 세포에서 ΔG가 음수가 되는 조건은?', ['두 산물의 농도가 F1,6BP보다 높을 때', '어떤 조건에서도 진행하지 않는다', '표준 조건에서 충분한 에너지가 나온다', '<b>F1,6BP 농도가 산물보다 높을 때</b>', '산물 농도가 F1,6BP보다 높을 때']),
    answer=ans('D', 'When [fructose 1,6-bisphosphate] is high relative to [products].', 'F1,6BP가 산물보다 훨씬 많을 때'),
    explain=eq('ΔG = +23.8 + RT ln ([DHAP][G3P] / [F1,6BP])') +
    steps('분모(F1,6BP) ↑, 분자(산물) ↓ → ln 항이 크게 음수 → ΔG &lt; 0.', '세포에서 G3P는 ⑥단계로 바로 끌려가 낮게 유지 → 실제 ΔG ≈ −6 ~ 0.') +
    tip('13장 기출 13-11과 같은 문제 — 13장 테스트뱅크는 답을 A로 잘못 적었고, 여기 14장은 D로 바르게 되어 있어.', '연결'))

add(n=55, sec=1, diff=2, kind='SA', title='ΔG′°가 양수인 두 이성질화 반응',
    en=f'<p>What are the two reactions in glycolysis in which aldose–ketose isomerization is catalyzed by an enzyme? For both reactions the {DG} is positive. Briefly explain how the reactions are able to proceed without the input of additional energy.</p>',
    ko=f'<p>해당과정에서 알도스–케토스 이성질화를 효소가 촉매하는 두 반응은? 둘 다 {DG}가 양수다. 추가 에너지 없이 어떻게 진행되는지 간단히 설명하라.</p>',
    answer=sa('Phosphohexose isomerase (G6P → F6P) and triose phosphate isomerase (DHAP → G3P). Their products are immediately removed by the next step, so product concentrations stay low and ΔG = ΔG′° + RT ln([P]/[S]) becomes negative.',
              '포스포헥소스 이성질화효소(G6P → F6P)와 TPI(DHAP → G3P). 산물이 다음 단계로 바로 쓰여 농도가 낮게 유지되므로 ln 항이 음수 → 실제 ΔG &lt; 0.'),
    explain=table(['단계', '반응', 'ΔG′°'], [['②', 'G6P → F6P (알도스→케토스)', '+1.7'], ['⑤', 'DHAP → G3P (케토스→알도스)', '+7.5']]) + eq('ΔG = ΔG′° + RT ln([산물]/[기질])') +
    key('“뒤에서 계속 끌어당긴다” — 다음 효소가 산물을 치워 버린다.'))

add(n=61, sec=1, diff=3, kind='SA', title='TPI의 K′eq 계산',
    en=f'<p>The conversion of glyceraldehyde 3-phosphate to dihydroxyacetone phosphate is catalyzed by triose phosphate isomerase. {DG} for this reaction is –7.5 kJ/mol. Draw the two structures. Define the equilibrium constant and calculate it using only the data given. (R = 8.315 J/mol·K; T = 298 K)</p>',
    ko=f'<p>G3P → DHAP 전환(TPI)의 {DG} = −7.5 kJ/mol. 두 구조를 그리고, 평형상수를 정의해 계산하라.</p>',
    answer=sa(f'K′eq = [DHAP]/[G3P]; ln K′eq = 7,500/(8.315 × 298) = 3.03 → K′eq ≈ 20.6', 'K′eq = [DHAP]/[G3P] ≈ <b>20.6</b> (평형에서 DHAP가 G3P의 약 20배)'),
    explain=table(['', 'G3P (알도스)', 'DHAP (케토스)'], [['C1', 'H–C=O (알데하이드)', 'CH₂OH'], ['C2', 'H–C–OH', 'C=O (케톤)'], ['C3', 'CH₂–OPO₃²⁻', 'CH₂–OPO₃²⁻']]) +
    align([('ln K′eq', '−ΔG′°/RT = 7,500 / 2,478 = 3.03', ''), ('K′eq', 'e<sup>3.03</sup> ≈ <b>20.6</b>', '')]) +
    warn('테스트뱅크 해설은 K′eq = [G3P]/[DHAP]로 적었지만, 반응이 G3P → DHAP이니 <b>[DHAP]/[G3P]</b>가 맞아(값 20.6은 같음).', '자료 오타') +
    tip('평형은 DHAP 쪽인데 해당과정은 DHAP → G3P로 간다 — G3P가 계속 소모되니까 (TB 14-55).', '연결'))

add(n=59, sec=1, diff=3, kind='SA', title='C-3과 C-4가 같아지는 순간',
    en='<p>At which point in glycolysis do C-3 and C-4 of glucose become chemically equivalent?</p>',
    ko='<p>해당과정의 어느 시점에서 포도당의 C-3과 C-4가 화학적으로 같아지는가?</p>',
    answer=sa('When triose phosphate isomerase converts DHAP to G3P: both become C-1 (aldehyde carbon) of glyceraldehyde 3-phosphate.', 'TPI가 DHAP → G3P로 바꿀 때. 둘 다 G3P의 C-1(알데하이드 탄소)이 된다.'),
    explain=fig(carbon_flow(), '') + steps('알돌라아제: C1–C3 → DHAP, C4–C6 → G3P. 아직 C3(DHAP의 C=O)과 C4(G3P의 CHO)는 다른 분자.', 'TPI: DHAP → G3P가 되면 C3도 G3P의 CHO 탄소 = C4와 같은 자리.') +
    key('TPI 이후 “두 개의 똑같은 G3P” → 탄소 짝: (1,6) (2,5) (3,4).'))

add(n=63, sec=1, diff=3, kind='SA', title='[1-¹⁴C]포도당 → G3P의 어느 탄소?',
    en='<p>When glucose labeled with ¹⁴C at C-1 (the aldehyde carbon) passes through glycolysis, the glyceraldehyde 3-phosphate produced still contains the radioactive carbon. Draw the structure of glyceraldehyde 3-phosphate, and circle the atom(s) that would be radioactive.</p>',
    ko='<p>C-1(알데하이드 탄소)에 ¹⁴C가 표지된 포도당이 해당과정을 지나면 G3P에도 방사성 탄소가 있다. G3P 구조를 그리고 방사성 원자에 동그라미 하라.</p>',
    answer=sa('C-3 of G3P (the –CH₂–OPO₃²⁻ carbon) is labeled.', 'G3P의 <b>C-3</b> (인산이 붙은 –CH₂–O–P 탄소)'),
    explain=fig(carbon_flow(), '') + table(['G3P', '구조', '포도당 유래'], [['C1', 'H–C=O', 'C3 · C4'], ['C2', 'H–C–OH', 'C2 · C5'], ['<b>C3 ★</b>', '<b>CH₂–O–PO₃²⁻</b>', '<b>C1 · C6</b>']]) +
    steps('포도당 C1 → F1,6BP의 C1 (인산 붙음) → DHAP의 C1(CH₂OP) → TPI 후 G3P의 C3(CH₂OP).') + key('인산이 붙은 끝 탄소는 끝까지 인산을 달고 간다.'))

add(n=52, sec=1, diff=2, kind='SA', title='해당 중간체가 모두 인산화된 이유',
    en='<p>All of the intermediates in the glycolytic pathway are phosphorylated. Give two plausible reasons why this might be advantageous to the cell.</p>',
    ko='<p>해당과정의 중간체는 모두 인산화되어 있다. 세포에 유리한 이유 두 가지를 들라.</p>',
    answer=sa('(1) Charged phosphates cannot cross the plasma membrane, so intermediates are trapped in the cell; (2) phosphoryl groups conserve energy and can be transferred to ADP to make ATP; (3) phosphate binding to enzymes lowers activation energy and increases specificity.',
              '① 음전하라 막을 못 지나 세포 안에 갇힌다 ② 인산기에 에너지를 보존했다가 ADP에 넘겨 ATP를 만든다 ③ 효소 결합 에너지로 활성화 에너지 ↓, 특이성 ↑'),
    explain=fig(phospho_why(), '') + key('슬라이드 11의 세 가지 이유 그대로: 에너지 보존 · 효소 결합/특이성 · 세포 안에 가두기.'))

add(n=58, sec=1, diff=2, kind='SA', title='포도당 → G6P (흡에르곤)를 어떻게 진행시키나',
    en='<p>The conversion of glucose into glucose 6-phosphate, which must occur in the breakdown of glucose, is thermodynamically unfavorable (endergonic). How do cells overcome this problem?</p>',
    ko='<p>포도당 → G6P 전환은 열역학적으로 불리(흡에르곤)하다. 세포는 이 문제를 어떻게 해결하나?</p>',
    answer=sa('By coupling it to ATP hydrolysis: the phosphoryl group is transferred from ATP to glucose (hexokinase). Glucose + Pᵢ → G6P (+13.8) plus ATP → ADP + Pᵢ (−30.5) gives −16.7 kJ/mol overall.',
              'ATP와 짝지음: 헥소키나아제가 ATP의 인산을 포도당에 직접 전달. +13.8 + (−30.5) = <b>−16.7 kJ/mol</b>'),
    explain=align([('포도당 + Pᵢ → G6P + H₂O', '+13.8', ''), ('ATP + H₂O → ADP + Pᵢ', '−30.5', ''), ('포도당 + ATP → G6P + ADP', '<b>−16.7</b>', '')]) +
    key('13장의 “짝지음(coupling)”이 해당 ①단계에서 실제로 쓰인다.'))

add(n=53, sec=1, diff=3, kind='SA', title='포도당 → G3P 경로 설명',
    en='<p>Describe the glycolytic pathway from glucose to glyceraldehyde 3-phosphate. Show structures of intermediates, enzyme names, and indicate where any cofactors participate.</p>',
    ko='<p>포도당에서 G3P까지의 해당 경로를 설명하라. 중간체, 효소 이름, 보조인자가 관여하는 곳을 표시하라.</p>',
    answer=sa('Hexokinase (ATP, Mg²⁺) → G6P → phosphohexose isomerase → F6P → PFK-1 (ATP, Mg²⁺) → F1,6BP → aldolase → DHAP + G3P → triose phosphate isomerase → 2 G3P.',
              '헥소키나아제(ATP) → G6P → 이성질화효소 → F6P → PFK-1(ATP) → F1,6BP → 알돌라아제 → DHAP + G3P → TPI → G3P 2개'),
    explain=table(['#', '효소', '반응', '보조인자', 'ΔG′°'], [['①', '헥소키나아제', '포도당 → G6P', '<b>ATP, Mg²⁺</b>', '−16.7'], ['②', '포스포헥소스 이성질화효소', 'G6P → F6P', '', '+1.7'], ['③', 'PFK-1', 'F6P → F1,6BP', '<b>ATP, Mg²⁺</b>', '−14.2'], ['④', '알돌라아제', 'F1,6BP → DHAP + G3P', '', '+23.8'], ['⑤', 'TPI', 'DHAP → G3P', '', '+7.5']], cls='left') +
    key('준비 단계 = ATP 2개 투자해 G3P 2개 만들기.'))

# ================================================================ S3 (2) 수익 단계
add(n=2, sec=2, diff=2, title='F1,6BP 1 mol → 피루브산 2 mol의 수확',
    en=mcq('The conversion of 1 mol of fructose 1,6-bisphosphate to 2 mol of pyruvate by the glycolytic pathway results in a net formation of:', ['1 mol of NAD⁺ and 2 mol of ATP.', '1 mol of NADH and 1 mol of ATP.', '2 mol of NAD⁺ and 4 mol of ATP.', '2 mol of NADH and 2 mol of ATP.', '2 mol of NADH and 4 mol of ATP.']),
    ko=mcq('F1,6BP 1 mol이 해당과정으로 피루브산 2 mol이 될 때 알짜로 생기는 것은?', ['NAD⁺ 1, ATP 2', 'NADH 1, ATP 1', 'NAD⁺ 2, ATP 4', 'NADH 2, ATP 2', '<b>NADH 2, ATP 4</b>']),
    answer=ans('E', '2 mol of NADH and 4 mol of ATP', 'NADH 2 mol + ATP 4 mol'),
    explain=key('F1,6BP부터 시작 = ATP 투자(①③)는 이미 끝났다 → 수익만 계산.') +
    steps('G3P 2개 × (⑥ NADH 1 + ⑦ ATP 1 + ⑩ ATP 1) = NADH 2 + ATP 4.') + warn('포도당부터면 ATP 4 − 2 = 2 (D). 출발점이 어디인지 꼭 확인!', '함정'))

add(n=8, sec=2, diff=2, title='ATP를 산물로 만드는 반응',
    en=mcq('Which of the following reactions in glycolysis produces ATP as a product?', ['Hexokinase', 'Glyceraldehyde-3-phosphate dehydrogenase', 'Pyruvate kinase', 'Aldolase', 'Phosphofructokinase-1']),
    ko=mcq('해당과정에서 ATP를 산물로 만드는 반응은?', ['헥소키나아제', 'GAPDH', '<b>피루브산 키나아제</b>', '알돌라아제', 'PFK-1']),
    answer=ans('C', 'Pyruvate kinase', '피루브산 키나아제 (PEP + ADP → 피루브산 + ATP)'),
    explain=key('ATP 생성 = ⑦ PGK, ⑩ PK (기질수준 인산화). 보기에 PGK가 없으니 PK.') + fig(gly_map(), ''))

add(n=14, sec=2, diff=2, title='G3P → 3PG 구간에 없는 것',
    en=mcq('The steps of glycolysis between glyceraldehyde 3-phosphate and 3-phosphoglycerate involve all of the following <b>except</b>:', ['ATP synthesis.', 'catalysis by phosphoglycerate kinase.', 'oxidation of NADH to NAD⁺.', 'the formation of 1,3-bisphosphoglycerate.', 'utilization of Pᵢ.']),
    ko=mcq('G3P → 3PG 구간(⑥⑦)에 포함되지 <b>않는</b> 것은?', ['ATP 합성', 'PGK의 촉매', '<b>NADH → NAD⁺ 산화</b>', '1,3-BPG 생성', 'Pᵢ 사용']),
    answer=ans('C', 'oxidation of NADH to NAD⁺', 'NADH의 산화 — 실제로는 반대로 NAD⁺가 NADH로 환원된다'),
    explain=align([('⑥ G3P + Pᵢ + NAD⁺', '→ 1,3-BPG + NADH + H⁺', '(GAPDH)'), ('⑦ 1,3-BPG + ADP', '→ 3PG + ATP', '(PGK)')]) +
    steps('A(ATP 합성) ⑦ ✔, B(PGK) ✔, D(1,3-BPG) ✔, E(Pᵢ 사용) ⑥ ✔.', 'C: 여기서는 NAD⁺ → NADH (환원). NADH를 다시 NAD⁺로 돌리는 건 젖산 발효(LDH)나 산소.') + warn('방향을 거꾸로 써 놓은 함정 보기.', '함정'))

add(n=15, sec=2, diff=2, title='처음으로 고에너지 화합물을 만드는 효소',
    en=mcq('The first reaction in glycolysis that results in the formation of an energy-rich compound is catalyzed by:', ['glyceraldehyde 3-phosphate dehydrogenase.', 'hexokinase.', 'phosphofructokinase-1.', 'phosphoglycerate kinase.', 'triose phosphate isomerase.']),
    ko=mcq('해당과정에서 처음으로 고에너지 화합물을 만드는 반응의 효소는?', ['<b>GAPDH</b>', '헥소키나아제', 'PFK-1', 'PGK', 'TPI']),
    answer=ans('A', 'glyceraldehyde 3-phosphate dehydrogenase', 'GAPDH → 1,3-BPG (아실 인산, −49.3 kJ/mol)'),
    explain=fig(bpg_svg(), '1,3-BPG: C1의 아실 인산이 고에너지') +
    steps('G6P·F1,6BP의 인산은 저에너지 에스터(−13.8 정도).', '⑥에서 산화 에너지를 이용해 Pᵢ를 붙여 <b>아실 인산</b>(−49.3) = ATP보다 센 고에너지 결합.', '⑦ PGK가 이 인산을 ADP에 넘겨 첫 ATP.') +
    key('산화(전자 빼기)의 에너지를 인산 결합에 저장하는 곳 = GAPDH.'))

add(n=16, sec=2, diff=1, title='GAPDH의 보조인자',
    en=mcq('Which of the following is a cofactor in the reaction catalyzed by glyceraldehyde 3-phosphate dehydrogenase?', ['ATP', 'Cu²⁺', 'heme', 'NAD⁺', 'NADP⁺']),
    ko=mcq('GAPDH 반응의 보조인자는?', ['ATP', 'Cu²⁺', '헴', '<b>NAD⁺</b>', 'NADP⁺']),
    answer=ans('D', 'NAD⁺', 'NAD⁺ (→ NADH)'),
    explain=eq('G3P + Pᵢ + <b>NAD⁺</b> ⇌ 1,3-BPG + <b>NADH</b> + H⁺') +
    key('이화(분해) = NAD⁺, 동화(합성)·PPP = NADP⁺.') + tip('NAD⁺의 양은 한정 → 계속 재생해야 해당이 돈다(발효의 이유, S7).', '연결'))

add(n=17, sec=2, diff=3, title='PGM에서 잠깐 인산화되는 아미노산',
    en=mcq('In the phosphoglycerate mutase reaction, the side chain of which amino acid in the enzyme is transiently phosphorylated as part of the reaction?', ['Serine', 'Threonine', 'Tyrosine', 'Histidine', 'Arginine']),
    ko=mcq('포스포글리세르산 뮤테이스 반응에서 효소의 어떤 아미노산 곁사슬이 잠깐 인산화되나?', ['세린', '트레오닌', '티로신', '<b>히스티딘</b>', '아르지닌']),
    answer=ans('D', 'Histidine', '히스티딘 (포스포히스티딘)'),
    explain=steps('효소의 인산화된 His가 3PG의 C2에 인산을 줌 → 2,3-BPG 중간체.', '2,3-BPG의 C3 인산이 효소 His로 돌아감 → 2PG + 다시 인산화된 효소.') +
    key('슬라이드 18: “중간체로 2,3-BPG를 거쳐 (효소의 인산화된 His 이용)”.') + tip('16장 숙시닐-CoA 합성효소도 포스포히스티딘을 쓴다.', '연결'))

add(n=18, sec=2, diff=2, title='불소(F⁻)로 에놀레이스를 막으면',
    en=mcq('Inorganic fluoride inhibits enolase. In an anaerobic system that is metabolizing glucose, which compound would you expect to increase in concentration following the addition of fluoride?', ['2-Phosphoglycerate', 'Glucose', 'Glyoxylate', 'Phosphoenolpyruvate', 'Pyruvate']),
    ko=mcq('플루오린화 이온은 에놀레이스를 억제한다. 포도당을 대사하는 무산소 계에 넣으면 농도가 늘어날 물질은?', ['<b>2-포스포글리세르산</b>', '포도당', '글리옥실산', 'PEP', '피루브산']),
    answer=ans('A', '2-Phosphoglycerate', '2PG (에놀레이스의 기질)'),
    explain=fig(flow(['3PG', '2PG ↑', 'PEP ↓', '피루브산 ↓'], arrow_labels=['PGM', '✕ 에놀레이스 (F⁻)', 'PK'], colors=[C['navy'], C['red'], C['gray'], C['gray']], box_h=36, width=520), '') +
    key('효소가 막히면 <b>앞(기질)은 쌓이고 뒤(산물)는 줄어든다</b>.') + tip('혈당 검사 채혈관(회색 뚜껑)에 NaF를 넣는 이유: 적혈구의 해당을 막아 포도당이 소모되지 않게.', '실생활'))

add(n=60, sec=2, diff=2, kind='SA', title='Pᵢ가 꼭 필요한 이유',
    en='<p>Explain why Pᵢ (inorganic phosphate) is absolutely required for glycolysis to proceed.</p>',
    ko='<p>해당과정이 진행하려면 무기 인산(Pᵢ)이 반드시 필요한 이유는?</p>',
    answer=sa('Pᵢ is an essential substrate of glyceraldehyde 3-phosphate dehydrogenase (G3P + Pᵢ + NAD⁺ → 1,3-BPG + NADH).', 'Pᵢ는 GAPDH 반응의 <b>기질</b>이다 (G3P + Pᵢ + NAD⁺ → 1,3-BPG + NADH).'),
    explain=eq('G3P + <b>Pᵢ</b> + NAD⁺ → 1,3-BPG + NADH + H⁺') + key('ATP에서 온 인산이 아니라 <b>무기 인산</b>이 직접 붙는 유일한 해당 단계.'))

add(n=64, sec=2, diff=2, kind='SA', title='인산 없이 효모 + 포도당 = 에탄올 0',
    en='<p>If brewer’s yeast is mixed with pure sugar (glucose) in the absence of phosphate (Pᵢ), no ethanol is produced. With the addition of a little Pᵢ, ethanol production soon begins. Explain this observation in 25 words or less.</p>',
    ko='<p>맥주 효모를 인산 없이 순수 포도당과 섞으면 에탄올이 생기지 않는다. Pᵢ를 조금 넣으면 곧 생긴다. 25단어 이내로 설명하라.</p>',
    answer=sa('Glyceraldehyde 3-phosphate dehydrogenase requires Pᵢ as a substrate; without Pᵢ, glycolysis stops at G3P and no ethanol forms.', 'GAPDH가 Pᵢ를 기질로 쓴다. Pᵢ가 없으면 해당이 G3P에서 멈춰 에탄올이 안 생긴다.'),
    explain=key('바로 앞 기출(TB 14-60)의 실험 버전.') + steps('포도당 → G3P까지는 ATP의 인산으로 진행.', 'G3P → 1,3-BPG에서 무기 인산이 필요 → 없으면 멈춤 → 피루브산 → 아세트알데하이드 → 에탄올 불가.') + tip('“25 words or less” — 영어 답안은 짧게! 위 EN 답이 20단어.', '시험'))

add(n=65, sec=2, diff=2, kind='SA', title='1,3-BPG 구조 — 고에너지 인산은 어디?',
    en='<p>Draw the structure of 1,3-bisphosphoglycerate. Indicate with an arrow the phosphate ester, and circle the phosphate group for which the free energy of hydrolysis is very high.</p>',
    ko='<p>1,3-BPG 구조를 그리고, 인산 에스터에 화살표, 가수분해 자유에너지가 매우 큰 인산기에 동그라미를 하라.</p>',
    answer=sa('Circle: the acyl phosphate on C-1 (–C(=O)–O–PO₃²⁻). Arrow: the phosphate ester on C-3 (–CH₂–O–PO₃²⁻).', '동그라미 = C-1의 <b>아실 인산</b>(고에너지) / 화살표 = C-3의 <b>인산 에스터</b>(저에너지)'),
    explain=fig(bpg_svg(), '') + steps('C1: 카복실산 + 인산 = 산 무수물(아실 인산) → 가수분해 −49.3 kJ/mol.', 'C3: 알코올 + 인산 = 에스터 → 저에너지. 이건 3PG까지 그대로 남는다.') +
    key('⑦ PGK는 C1의 고에너지 인산만 ADP에 넘긴다.'))

add(n=66, sec=2, diff=2, kind='SA', title='ATP를 만드는 두 반응',
    en='<p>Two reactions in glycolysis produce ATP. For each of these, show the name and structure of reactant and product, indicate which cofactors participate and where, and name the enzymes.</p>',
    ko='<p>해당과정에서 ATP를 만드는 두 반응의 반응물·산물 이름(구조), 보조인자, 효소를 써라.</p>',
    answer=sa('(1) Phosphoglycerate kinase: 1,3-BPG + ADP → 3PG + ATP (Mg²⁺). (2) Pyruvate kinase: PEP + ADP → pyruvate + ATP (Mg²⁺, K⁺).', '① PGK: 1,3-BPG + ADP → 3PG + ATP (Mg²⁺) ② PK: PEP + ADP → 피루브산 + ATP (Mg²⁺, K⁺)'),
    explain=table(['', '⑦ PGK', '⑩ 피루브산 키나아제'], [['반응물', '1,3-BPG (C1 아실 인산)', 'PEP (엔올 인산)'], ['산물', '3PG + ATP', '피루브산 + ATP'], ['보조인자', 'Mg²⁺', 'Mg²⁺, K⁺'], ['ΔG′°', '−18.5', '−31.4'], ['종류', '기질수준 인산화', '기질수준 인산화 (+ 토토머화)']]) +
    key('두 반응 모두 3탄소 단계 → 포도당 1개당 ×2 = ATP 4개.'))

add(n=54, sec=2, diff=3, kind='SA', title='G3P → 피루브산 경로 설명',
    en='<p>Describe the glycolytic pathway from glyceraldehyde 3-phosphate to pyruvate, showing structures of intermediates and names of enzymes. Indicate where any cofactors participate.</p>',
    ko='<p>G3P에서 피루브산까지의 해당 경로를 중간체, 효소, 보조인자와 함께 설명하라.</p>',
    answer=sa('GAPDH (NAD⁺, Pᵢ) → 1,3-BPG → phosphoglycerate kinase (ADP→ATP, Mg²⁺) → 3PG → phosphoglycerate mutase → 2PG → enolase (−H₂O, Mg²⁺) → PEP → pyruvate kinase (ADP→ATP, Mg²⁺, K⁺) → pyruvate.',
              'GAPDH(NAD⁺, Pᵢ) → 1,3-BPG → PGK(ATP 생성) → 3PG → PGM → 2PG → 에놀레이스(−H₂O) → PEP → PK(ATP 생성) → 피루브산'),
    explain=table(['#', '효소', '반응', '보조인자/산물', 'ΔG′°'], [['⑥', 'GAPDH', 'G3P → 1,3-BPG', '<b>NAD⁺ → NADH, Pᵢ</b>', '+6.3'], ['⑦', 'PGK', '1,3-BPG → 3PG', '<b>ADP → ATP</b>, Mg²⁺', '−18.5'], ['⑧', 'PGM', '3PG → 2PG', 'Mg²⁺ (His-P)', '+4.4'], ['⑨', '에놀레이스', '2PG → PEP', '−H₂O, Mg²⁺', '+7.5'], ['⑩', 'PK', 'PEP → 피루브산', '<b>ADP → ATP</b>, Mg²⁺·K⁺', '−31.4']], cls='left') +
    key('수익 단계 ×2 = NADH 2 + ATP 4.'))

add(n=5, sec=2, diff=3, title='[1,6-¹⁴C]포도당 → 피루브산 표지 위치',
    en=mcq('Glucose labeled with ¹⁴C in C-1 and C-6 gives rise in glycolysis to pyruvate labeled in:', ['A and C.', 'all three carbons.', 'its carbonyl carbon.', 'its carboxyl carbon.', 'its methyl carbon.']),
    ko=mcq('C-1과 C-6에 ¹⁴C가 표지된 포도당이 해당과정을 거치면 피루브산의 어디가 표지되나?', ['A와 C', '세 탄소 모두', '카보닐 탄소', '카복실 탄소', '<b>메틸 탄소</b>']),
    answer=ans('E', 'its methyl carbon', '메틸 탄소 (C-3)'),
    explain=fig(carbon_flow(), '') + carbon_map() + key('C1·C6 → G3P의 CH₂OP(C3) → 인산이 떨어진 뒤 피루브산의 <b>CH₃</b>.'))

add(n=6, sec=2, diff=2, title='[2-¹⁴C]포도당 → 피루브산 표지 위치',
    en=mcq('If glucose labeled with ¹⁴C at C-2 were metabolized in the liver, the first radioactive pyruvate formed would be labeled in:', ['all three carbons.', 'both A and C.', 'its carbonyl carbon.', 'its carboxyl carbon.', 'its methyl carbon.']),
    ko=mcq('C-2에 ¹⁴C가 표지된 포도당이 간에서 대사되면, 처음 생기는 방사성 피루브산은 어디가 표지되나?', ['세 탄소 모두', 'A와 C', '<b>카보닐 탄소</b>', '카복실 탄소', '메틸 탄소']),
    answer=ans('C', 'its carbonyl carbon', '카보닐 탄소 (C-2, C=O)'),
    explain=carbon_map() + key('가운데 탄소(C2·C5)는 언제나 가운데 → 피루브산의 C=O.'))

add(n=62, sec=2, diff=3, kind='SA', title='3PG의 인산 탄소 = 포도당 C-1 또는 C-6',
    en='<p>When glucose is oxidized via glycolysis, the carbon atom that bears the phosphate in the 3-phosphoglycerate formed may have originally been either C-1 or C-6 of the original glucose. Describe this pathway in just enough detail to explain this fact.</p>',
    ko='<p>해당과정으로 생긴 3-포스포글리세르산에서 인산이 붙은 탄소는 원래 포도당의 C-1 또는 C-6이었을 수 있다. 이유를 경로로 설명하라.</p>',
    answer=sa('Aldolase splits F1,6BP into DHAP (C-1–C-3) and G3P (C-4–C-6). Triose phosphate isomerase converts DHAP to G3P, so C-3 of G3P (phosphate-bearing) comes from C-1 or C-6; it becomes C-3 of 3PG.',
              '알돌라아제: DHAP(C1–3) + G3P(C4–6). TPI가 DHAP → G3P로 바꾸면 인산이 붙은 G3P의 C-3은 포도당의 C-1 또는 C-6. 이것이 3PG의 C-3.'),
    explain=fig(carbon_flow(), '') + key('포도당 양 끝(C1, C6)은 처음부터 인산이 붙는 자리(①③) → 끝까지 인산 탄소.'))

# ================================================================ S4 (3) 전체·비가역
add(n=49, sec=3, diff=1, kind='SA', title='ATP 2개 쓰고 2개 만드는데 왜 알짜 +2?',
    en='<p>In glycolysis there are two reactions that require one ATP each and two reactions that produce one ATP each. How can fermentation of glucose to lactate lead to the net production of two ATP molecules per glucose?</p>',
    ko='<p>해당과정에는 ATP를 하나씩 쓰는 반응 2개와 하나씩 만드는 반응 2개가 있다. 그런데 어떻게 포도당 → 젖산 발효에서 알짜 ATP가 2개인가?</p>',
    answer=sa('ATP-consuming steps act on hexoses (once per glucose), but ATP-producing steps act on trioses, which occur twice per glucose: 4 made − 2 used = 2 net.', 'ATP를 쓰는 반응은 6탄당 단계(1번씩), 만드는 반응은 3탄당 단계(2번씩). 4 − 2 = <b>2</b>.'),
    explain=table(['', '단계', '포도당당 횟수', 'ATP'], [['투자', '① HK, ③ PFK-1 (6C)', '×1', '−2'], ['회수', '⑦ PGK, ⑩ PK (3C)', '<b>×2</b>', '+4'], ['알짜', '', '', '<b>+2</b>']]) + key('반으로 자른 뒤(④) 모든 것이 두 배.'))

add(n=57, sec=3, diff=2, kind='SA', title='해당 효소 순서 맞추기',
    en='<p>Number the enzymes in the order they function in glucose → pyruvate: hexokinase (1), triose phosphate isomerase, phosphohexose isomerase, enolase, glyceraldehyde 3-phosphate dehydrogenase, pyruvate kinase, phosphofructokinase-1. Which is a major regulation point? Which produces ATP? Which produces NADH?</p>',
    ko='<p>포도당 → 피루브산에서 효소가 일하는 순서를 번호로: 헥소키나아제(1), TPI, 포스포헥소스 이성질화효소, 에놀레이스, GAPDH, 피루브산 키나아제, PFK-1. 주요 조절 지점은? ATP를 만드는 것은? NADH를 만드는 것은?</p>',
    answer=sa('Hexokinase 1; TPI 4; phosphohexose isomerase 2; enolase 6; GAPDH 5; pyruvate kinase 7; PFK-1 3. Regulation: PFK-1. ATP: pyruvate kinase. NADH: GAPDH.',
              '헥소키나아제 1 · TPI 4 · 이성질화효소 2 · 에놀레이스 6 · GAPDH 5 · PK 7 · PFK-1 3. 조절 = PFK-1, ATP = PK, NADH = GAPDH'),
    explain=fig(gly_map(), '') + key('PFK-1 = 첫 전념(committed) 단계 → 핵심 조절 지점 (15장).'))

# ================================================================ S5 (4) 피루브산 운명·바르부르크
add(n=13, sec=4, diff=2, title='[¹⁸F]2-플루오로-2-데옥시포도당(FDG)',
    en=mcq('The compound [¹⁸F]2-fluoro-2-deoxyglucose is:', ['an intermediate in glycolysis', 'a positive regulator of glycolysis', 'a potent anti-cancer agent', 'an antibiotic', 'an imaging agent used to detect tumors']),
    ko=mcq('[¹⁸F]2-플루오로-2-데옥시포도당은?', ['해당 중간체', '해당 양성 조절자', '강력한 항암제', '항생제', '<b>종양을 찾는 영상 진단제</b>']),
    answer=ans('E', 'an imaging agent used to detect tumors', '종양 탐지용 영상제 (FDG-PET)'),
    explain=steps('종양은 바르부르크 효과로 포도당을 많이 흡수 → FDG도 많이 들어감.', '헥소키나아제가 FDG-6-인산으로 만들지만 다음 단계로 못 가 → 세포 안에 갇혀 쌓임.', '¹⁸F 방사선을 PET으로 찍으면 종양이 밝게 보인다.') +
    key('“인산화되면 갇힌다”(S2) + “종양은 포도당을 많이 먹는다”(바르부르크) = FDG-PET.'))

add(n=50, sec=4, diff=2, kind='SA', title='사람에서 피루브산의 운명',
    en='<p>Briefly describe the possible metabolic fates of pyruvate produced by glycolysis in humans, and explain the circumstances that favor each.</p>',
    ko='<p>사람에서 해당과정으로 생긴 피루브산의 운명과 각각이 일어나는 조건을 설명하라.</p>',
    answer=sa('Aerobic: oxidized to acetyl-CoA and through the citric acid cycle. Anaerobic: reduced to lactate to regenerate NAD⁺ for glycolysis.', '유산소: 아세틸-CoA → TCA. 무산소: 젖산으로 환원되어 NAD⁺를 재생.'),
    explain=fig(pyruvate_fates(), '') + key('산소 있음 → 태운다(아세틸-CoA), 산소 없음 → NAD⁺만 되찾는다(젖산).'))

add(n=51, sec=4, diff=2, kind='SA', title='NADH → NAD⁺ 재생 (유산소 / 무산소)',
    en='<p>Show how NADH is recycled to NAD⁺ under aerobic conditions and under anaerobic conditions. Why is it important to recycle NADH produced during glycolysis to NAD⁺?</p>',
    ko='<p>유산소·무산소에서 NADH가 NAD⁺로 재생되는 방법을 보이고, 왜 재생이 중요한지 설명하라.</p>',
    answer=sa('Aerobic: NADH passes electrons to O₂ (respiratory chain). Anaerobic: NADH reduces pyruvate to lactate. NAD⁺ is limited; without recycling, the GAPDH step stops for lack of electron acceptor.',
              '유산소: 전자전달계로 O₂에 전자 전달. 무산소: 피루브산 → 젖산. NAD⁺는 양이 한정 → 재생 안 하면 GAPDH가 멈춘다.'),
    explain=table(['조건', 'NADH의 전자 → ', '결과'], [['유산소', 'O₂ (전자전달계)', 'H₂O + ATP 많이'], ['무산소 (근육)', '피루브산 → <b>젖산</b> (LDH)', 'NAD⁺ 재생만'], ['무산소 (효모)', '아세트알데하이드 → <b>에탄올</b>', 'NAD⁺ 재생만']]) +
    key('세포 속 NAD⁺ + NADH 총량은 일정 → 빈 트럭(NAD⁺)을 계속 돌려받아야 한다.'))

add(n=29, sec=4, diff=2, title='유산소 수축 때 젖산이 덜 생기는 이유',
    en=mcq('When a muscle is stimulated to contract aerobically, less lactic acid is formed than when it contracts anaerobically because:', ['glycolysis does not occur to significant extent under aerobic conditions.', 'muscle is metabolically less active under aerobic than anaerobic conditions.', 'the lactic acid generated is rapidly incorporated into lipids under aerobic conditions.', 'under aerobic conditions in muscle, the major energy-yielding pathway is the pentose phosphate pathway, which does not produce lactate.', 'under aerobic conditions most of the pyruvate generated as a result of glycolysis is oxidized by the citric acid cycle rather than reduced to lactate.']),
    ko=mcq('근육이 유산소로 수축할 때 무산소일 때보다 젖산이 덜 생기는 이유는?', ['유산소에서는 해당이 거의 안 일어나서', '유산소에서 근육 대사가 덜 활발해서', '젖산이 빠르게 지질로 바뀌어서', '유산소 근육의 주 에너지 경로가 PPP라서', '<b>유산소에서는 피루브산 대부분이 젖산 대신 TCA로 산화되어서</b>']),
    answer=ans('E', 'most pyruvate is oxidized by the citric acid cycle rather than reduced to lactate', '피루브산이 젖산 대신 TCA에서 산화되기 때문'),
    explain=fig(pyruvate_fates(), '') + warn('A는 함정: 유산소에서도 해당은 똑같이 일어난다. 달라지는 건 피루브산의 운명.', '함정'))

add(n=30, sec=4, diff=2, title='틀린 문장 고르기 — 피루브산',
    en=mcq('Which of the following statements is incorrect?', ['Aerobically, oxidative decarboxylation of pyruvate forms acetate that enters the citric acid cycle.', 'In anaerobic muscle, pyruvate is converted to lactate.', 'In yeast growing anaerobically, pyruvate is converted to ethanol.', 'Reduction of pyruvate to lactate regenerates a cofactor essential for glycolysis.', 'Under anaerobic conditions pyruvate does not form because glycolysis does not occur.']),
    ko=mcq('틀린 것은?', ['유산소에서 피루브산의 산화적 탈카복실화로 생긴 아세트산(아세틸기)이 TCA로 들어간다', '무산소 근육에서 피루브산은 젖산이 된다', '무산소로 자라는 효모에서 피루브산은 에탄올이 된다', '피루브산 → 젖산 환원이 해당에 필수인 보조인자를 재생한다', '<b>무산소에서는 해당이 안 일어나 피루브산이 안 생긴다</b>']),
    answer=ans('E', 'Under anaerobic conditions pyruvate does not form because glycolysis does not occur.', '틀림 — 해당은 산소와 무관하게 일어난다'),
    explain=key('해당과정 = 산소가 필요 없는 경로. 무산소에서 오히려 더 빨리 돈다(파스퇴르 효과).') + tip('A의 “acetate”는 엄밀히는 아세틸-CoA의 아세틸기.', '참고'))

# ================================================================ S6 (5) 공급 경로
add(n=19, sec=5, diff=1, title='글리코겐 → 단당류 효소',
    en=mcq('Glycogen is converted to monosaccharide units by:', ['glucokinase.', 'glucose-6-phosphatase.', 'glycogen phosphorylase.', 'glycogen synthase.', 'glycogenase.']),
    ko=mcq('글리코겐을 단당 단위로 바꾸는 효소는?', ['글루코키나아제', 'G6Pase', '<b>글리코겐 인산화효소</b>', '글리코겐 합성효소', '글리코게네이스']),
    answer=ans('C', 'glycogen phosphorylase', '글리코겐 인산화효소 → 포도당 1-인산'),
    explain=eq('글리코겐(n) + Pᵢ → 글리코겐(n−1) + <b>포도당 1-인산</b>') + key('가수분해가 아니라 <b>인산분해</b> → 바로 인산이 붙은 G1P (ATP 절약).') + warn('E(“글리코게네이스”)는 존재하지 않는 이름.', '함정'))

add(n=68, sec=5, diff=3, kind='SA', title='인산분해가 가수분해보다 효율적인 이유',
    en='<p>Explain why the phosphorolysis of glycogen is more efficient than the hydrolysis of glycogen in mobilizing glucose for the glycolytic pathway.</p>',
    ko='<p>글리코겐을 해당과정에 쓰려 할 때 인산분해가 가수분해보다 효율적인 이유는?</p>',
    answer=sa('Phosphorolysis yields glucose 1-phosphate, which becomes G6P without ATP; hydrolysis yields free glucose, which must be phosphorylated by hexokinase at the cost of ATP.', '인산분해 → G1P → G6P (ATP 불필요). 가수분해 → 포도당 → 헥소키나아제로 ATP 1개 소비.'),
    explain=table(['', '인산분해 (Pᵢ)', '가수분해 (H₂O)'], [['산물', '포도당 1-인산', '포도당'], ['G6P까지', '뮤테이스 (ATP 0)', '헥소키나아제 (ATP 1)'], ['포도당당 알짜 ATP (젖산까지)', '<b>3</b>', '2']]) + key('글리코겐에서 시작한 해당은 ATP를 하나 덜 투자한다.'))

add(n=69, sec=5, diff=3, kind='SA', title='근육 글리코겐 분해 과정',
    en='<p>Describe the process of glycogen breakdown in muscle. Include the structure of glycogen, the nature of the breakdown reaction and product, and the required enzyme(s).</p>',
    ko='<p>근육의 글리코겐 분해 과정을 설명하라 (글리코겐 구조, 분해 반응의 성질, 산물, 효소).</p>',
    answer=sa('Glycogen: (α1→4)-linked glucose chains with (α1→6) branches. Glycogen phosphorylase removes terminal residues from nonreducing ends by phosphorolysis → glucose 1-phosphate. Near branch points, debranching enzyme transfers residues and removes the branch, so phosphorylase can continue.',
              '글리코겐 = (α1→4) 사슬 + (α1→6) 가지. 인산화효소가 비환원 말단에서 인산분해로 G1P를 떼어 냄. 가지점 근처에서는 가지제거 효소가 남은 조각을 옮기고 가지를 잘라 다시 진행.'),
    explain=table(['단계', '효소', '산물'], [['① 사슬 끝 자르기', '글리코겐 인산화효소 (PLP)', 'G1P'], ['② 가지 처리', '가지제거 효소', '(α1→4)로 옮김 + 포도당 1개'], ['③ G1P → G6P', '포스포글루코뮤테이스', 'G6P → 해당']], cls='left') +
    tip('근육엔 G6Pase가 없어 G6P는 자기 해당에만 쓴다 (15장).', '연결'))

add(n=20, sec=5, diff=3, title='갈락토스혈증의 원인',
    en=mcq('Galactosemia is a genetic error of metabolism associated with:', ['deficiency of galactokinase.', 'deficiency of UDP-glucose.', 'deficiency of UDP-glucose: galactose 1-phosphate uridylyltransferase.', 'excessive ingestion of galactose.', 'inability to digest lactose.']),
    ko=mcq('갈락토스혈증과 관련된 유전 결함은?', ['갈락토키나아제 결핍', 'UDP-포도당 결핍', '<b>UDP-포도당:갈락토스 1-인산 유리딜전이효소 결핍</b>', '갈락토스 과다 섭취', '락토스 소화 불능']),
    answer=ans('C', 'deficiency of UDP-glucose:galactose 1-phosphate uridylyltransferase', '유리딜전이효소 결핍 (고전적 갈락토스혈증)'),
    explain=fig(flow(['갈락토스', '갈락토스 1-인산', 'UDP-갈락토스 + G1P'], arrow_labels=['갈락토키나아제', '✕ 유리딜전이효소'], colors=[C['navy'], C['red'], C['gray']], box_h=36, width=520), '') +
    steps('전이효소가 없으면 갈락토스 1-인산과 갈락토스가 쌓인다 → 간·뇌·수정체 손상(백내장).', '치료: 젖(락토스 = 포도당 + 갈락토스)을 끊는다.') +
    warn('E(락토스 소화 불능)는 <b>락테이스</b> 결핍 = 젖당 불내증. 다른 병!', '함정'))

add(n=70, sec=5, diff=2, kind='SA', title='젖당 불내증의 생화학적 원인',
    en='<p>Explain the biochemical basis of the human metabolic disorder called lactose intolerance.</p>',
    ko='<p>젖당 불내증의 생화학적 원인을 설명하라.</p>',
    answer=sa('Intestinal lactase is lost in adulthood, so lactose is not hydrolyzed and absorbed in the small intestine; it passes to the large intestine, where bacteria ferment it, causing gas and diarrhea.', '어른이 되며 소장의 <b>락테이스</b>가 줄어 락토스를 못 쪼갬 → 대장으로 넘어가 세균이 발효 → 가스·설사·복통.'),
    explain=eq('락토스 + H₂O → 갈락토스 + 포도당 &nbsp;(락테이스)') + key('이당류는 단당류로 쪼개져야만 흡수된다 (슬라이드 25).') + tip('락테이스 보충제나 락토스 없는 우유로 해결.', '약학'))

add(n=67, sec=5, diff=3, kind='SA', title='효모의 만노스 → 에탄올',
    en='<p>Yeast can metabolize D-mannose to ethanol and CO₂. Besides the glycolytic enzymes, the only other enzyme needed is phosphomannose isomerase (mannose 6-phosphate → fructose 6-phosphate). By the most direct pathway, which are involved? A. Lactate B. Acetaldehyde C. Acetyl-CoA D. FAD E. Glucose 6-phosphate F. Fructose 1-phosphate G. Pyruvate H. Lipoic acid I. Thiamine pyrophosphate J. Dihydroxyacetone phosphate</p>',
    ko='<p>효모는 만노스를 에탄올 + CO₂로 바꾼다. 해당 효소 외에 필요한 건 포스포만노스 이성질화효소(만노스 6-인산 → 과당 6-인산)뿐이다. 가장 직접적인 경로에 관여하는 것은? A 젖산 B 아세트알데하이드 C 아세틸-CoA D FAD E G6P F 과당 1-인산 G 피루브산 H 리포산 I TPP J DHAP</p>',
    answer=sa('B, G, I, J', 'B (아세트알데하이드), G (피루브산), I (TPP), J (DHAP)'),
    explain=fig(flow(['만노스 → M6P', 'F6P → … DHAP·G3P', '피루브산', '아세트알데하이드 → 에탄올'], arrow_labels=['이성질화효소', '해당', '탈카복실화효소 (TPP)'], colors=[C['purple'], C['navy'], C['navy'], C['green']], box_h=36, width=560, font=10), '') +
    steps('E(G6P) ✕: 만노스 6-인산이 바로 F6P가 되어 G6P를 거치지 않는다.', 'C·H ✕: 아세틸-CoA·리포산은 PDH(유산소) 경로. D(FAD)도 무관.', 'A(젖산) ✕: 효모는 에탄올 발효. F(과당 1-인산)은 간의 과당 대사.'))

# ================================================================ S7 (6) 발효
add(n=21, sec=6, diff=1, title='격렬한 운동 중 NADH 재산화',
    en=mcq('During strenuous exercise, the NADH formed in the glyceraldehyde 3-phosphate dehydrogenase reaction in skeletal muscle must be reoxidized to NAD⁺ if glycolysis is to continue. The most important reaction involved is:', ['dihydroxyacetone phosphate → glycerol 3-phosphate.', 'glucose 6-phosphate → fructose 6-phosphate.', 'isocitrate → α-ketoglutarate.', 'oxaloacetate → malate.', 'pyruvate → lactate.']),
    ko=mcq('격렬한 운동 중 골격근에서 GAPDH가 만든 NADH를 NAD⁺로 되돌리는 가장 중요한 반응은?', ['DHAP → 글리세롤 3-인산', 'G6P → F6P', '아이소시트르산 → α-KG', 'OAA → 말산', '<b>피루브산 → 젖산</b>']),
    answer=ans('E', 'pyruvate → lactate', '피루브산 → 젖산 (LDH)'),
    explain=fig(flow(['피루브산 + NADH', '젖산 + NAD⁺'], arrow_labels=['젖산 탈수소효소 (LDH)'], colors=[C['navy'], C['green']], box_h=36, width=480), '') + key('산소가 모자라면 NADH의 전자를 피루브산에 버려 NAD⁺를 되찾는다.'))

add(n=23, sec=6, diff=1, title='포도당 → 젖산 2개의 알짜 수확',
    en=mcq('The anaerobic conversion of 1 mol of glucose to 2 mol of lactate by fermentation is accompanied by a net gain of:', ['1 mol of ATP.', '1 mol of NADH.', '2 mol of ATP.', '2 mol of NADH.', 'None of the above']),
    ko=mcq('포도당 1 mol → 젖산 2 mol 발효의 알짜 수확은?', ['ATP 1 mol', 'NADH 1 mol', '<b>ATP 2 mol</b>', 'NADH 2 mol', '정답 없음']),
    answer=ans('C', '2 mol of ATP', 'ATP 2 mol (NADH는 젖산 만들 때 다 써서 0)'),
    explain=eq('포도당 + 2ADP + 2Pᵢ → 2 젖산 + 2ATP + 2H₂O') + warn('NADH 2개는 GAPDH에서 생기지만 LDH에서 다시 써 버려 알짜 0 → D 틀림.', '함정'))

add(n=26, sec=6, diff=2, title='젖산 발효의 산화-환원 보조인자',
    en=mcq('Which of these cofactors participates directly in most of the oxidation-reduction reactions in the fermentation of glucose to lactate?', ['ADP', 'ATP', 'FAD/FADH₂', 'Glyceraldehyde 3-phosphate', 'NAD⁺/NADH']),
    ko=mcq('포도당 → 젖산 발효의 산화-환원에 직접 참여하는 보조인자는?', ['ADP', 'ATP', 'FAD/FADH₂', 'G3P', '<b>NAD⁺/NADH</b>']),
    answer=ans('E', 'NAD⁺/NADH', 'NAD⁺/NADH'),
    explain=table(['반응', '산화-환원'], [['⑥ GAPDH', 'G3P 산화, NAD⁺ → NADH'], ['LDH', '피루브산 환원, NADH → NAD⁺']]) + key('젖산 발효의 산화-환원은 딱 두 번, 둘 다 NAD.'))

add(n=27, sec=6, diff=1, title='수축 중인 근육 vs 쉬는 근육',
    en=mcq('In comparison with the resting state, actively contracting human muscle tissue has a:', ['higher concentration of ATP.', 'higher rate of lactate formation.', 'lower consumption of glucose.', 'lower rate of consumption of oxygen', 'lower ratio of NADH to NAD⁺.']),
    ko=mcq('쉬는 상태와 비교해 활발히 수축하는 근육은?', ['ATP 농도가 높다', '<b>젖산 생성 속도가 높다</b>', '포도당 소비가 적다', '산소 소비가 적다', 'NADH/NAD⁺ 비율이 낮다']),
    answer=ans('B', 'higher rate of lactate formation', '젖산 생성 속도가 더 높다'),
    explain=steps('ATP를 빨리 써서 [ATP]는 오히려 ↓ (A ✕).', '포도당·산소 소비 모두 ↑ (C·D ✕).', 'NADH가 쌓여 NADH/NAD⁺ ↑ (E ✕) → 젖산으로 NAD⁺ 재생 ↑.') + key('산소 공급이 수요를 못 따라가면 젖산 ↑.'))

add(n=28, sec=6, diff=2, title='무산소 근육의 해당에 대해 틀린 것',
    en=mcq('Which of the following statements is not true concerning glycolysis in anaerobic muscle?', ['Fructose 1,6-bisphosphatase is one of the enzymes of the pathway.', 'It is an endergonic process.', 'It results in net synthesis of ATP.', 'It results in synthesis of NADH.', 'Its rate is slowed by a high [ATP]/[ADP] ratio.']),
    ko=mcq('무산소 근육의 해당과정에 대해 틀린 것은?', ['FBPase-1이 경로의 효소이다', '<b>흡에르곤 과정이다</b>', '알짜 ATP를 만든다', 'NADH를 만든다', '[ATP]/[ADP]가 높으면 느려진다']),
    answer=ans('B', 'It is an endergonic process.', '흡에르곤이다 — 틀림. 해당은 전체적으로 발에르곤(ΔG′° ≈ −196 kJ/mol 젖산까지)',
               note='⚠️ 엄밀히는 A도 틀린 문장이야. FBPase-1은 <b>당신생</b> 효소이고, 해당과정은 PFK-1을 쓴다. 테스트뱅크 정답은 B — 시험에서는 B를 고르되, A도 틀렸다는 걸 알아 두자.'),
    explain=steps('B: ATP를 만들며 진행하는 발에르곤 과정.', 'C·D: ATP 알짜 2, NADH는 GAPDH에서 생성(LDH에서 다시 소비).', 'E: ATP가 많으면 PFK-1 억제 → 느려짐 (15장).') + key('해당 = 에너지를 <b>내놓는</b> 경로.'))

add(n=31, sec=6, diff=2, title='에탄올 발효의 최종 전자 수용체',
    en=mcq('The ultimate electron acceptor in the fermentation of glucose to ethanol is:', ['acetaldehyde.', 'acetate.', 'ethanol.', 'NAD⁺.', 'pyruvate.']),
    ko=mcq('포도당 → 에탄올 발효의 최종 전자 수용체는?', ['<b>아세트알데하이드</b>', '아세트산', '에탄올', 'NAD⁺', '피루브산']),
    answer=ans('A', 'acetaldehyde', '아세트알데하이드 (NADH의 전자를 받아 에탄올이 됨)'),
    explain=fig(flow(['피루브산', '아세트알데하이드', '에탄올'], arrow_labels=['탈카복실화효소 (TPP), −CO₂', 'ADH: NADH → NAD⁺'], colors=[C['navy'], C['orange'], C['green']], box_h=36, width=520), '') +
    steps('NAD⁺는 중간 운반자(트럭)일 뿐, 최종 수용체가 아니다.', '에탄올은 전자를 받은 <b>결과물</b>.') + key('젖산 발효의 최종 전자 수용체는 피루브산, 에탄올 발효는 아세트알데하이드.'))

add(n=32, sec=6, diff=2, title='알코올 발효에서 TPP가 필요한 효소',
    en=mcq('In the alcoholic fermentation of glucose by yeast, thiamine pyrophosphate is a coenzyme required by:', ['aldolase.', 'hexokinase.', 'lactate dehydrogenase.', 'pyruvate decarboxylase.', 'transaldolase.']),
    ko=mcq('효모의 알코올 발효에서 티아민 피로인산(TPP)이 필요한 효소는?', ['알돌라아제', '헥소키나아제', 'LDH', '<b>피루브산 탈카복실화효소</b>', '트랜스알돌레이스']),
    answer=ans('D', 'pyruvate decarboxylase', '피루브산 탈카복실화효소 (TPP, Mg²⁺)'),
    explain=key('TPP(비타민 B₁) = 탈카복실화 전문가. PDH, α-KG DH, 트랜스케톨레이스도 TPP (16장).') + warn('E: PPP의 트랜스<b>케톨</b>레이스는 TPP를 쓰지만 트랜스<b>알돌</b>레이스는 안 쓴다.', '함정'))

add(n=22, sec=6, diff=3, title='[3,4-¹⁴C]포도당 → 젖산 표지',
    en=mcq('In an anaerobic muscle preparation, lactate formed from glucose labeled in C-3 and C-4 would be labeled in:', ['all three carbon atoms.', 'only the carbon atom carrying the OH.', 'only the carboxyl carbon atom.', 'only the methyl carbon atom.', 'the methyl and carboxyl carbon atoms.']),
    ko=mcq('C-3, C-4가 표지된 포도당에서 무산소 근육이 만든 젖산은 어디가 표지되나?', ['세 탄소 모두', '–OH가 붙은 탄소만', '<b>카복실 탄소만</b>', '메틸 탄소만', '메틸과 카복실']),
    answer=ans('C', 'only the carboxyl carbon atom', '카복실 탄소(–COO⁻)만'),
    explain=carbon_map() + key('C3·C4 → G3P의 CHO(C1) → 산화되어 카복실 → 피루브산·젖산의 COO⁻.'))

add(n=25, sec=6, diff=2, title='[2-¹⁴C]포도당 → 젖산 표지',
    en=mcq('In an anaerobic muscle preparation, lactate formed from glucose labeled in C-2 would be labeled in:', ['all three carbon atoms.', 'only the carbon atom carrying the OH.', 'only the carboxyl carbon atom.', 'only the methyl carbon atom.', 'the methyl and carboxyl carbon atoms.']),
    ko=mcq('C-2가 표지된 포도당에서 생긴 젖산은 어디가 표지되나?', ['세 탄소 모두', '<b>–OH가 붙은 탄소만</b>', '카복실 탄소만', '메틸 탄소만', '메틸과 카복실']),
    answer=ans('B', 'only the carbon atom carrying the OH', '–OH가 붙은 가운데 탄소(C-2)'),
    explain=carbon_map() + key('C2 → 피루브산의 C=O(C2) → LDH가 환원 → 젖산의 CH–OH.'))

add(n=24, sec=6, diff=2, title='[1-¹⁴C]포도당 → 에탄올 발효',
    en=mcq('If glucose labeled with ¹⁴C in C-1 were fed to yeast carrying out the ethanol fermentation, where would the ¹⁴C label be in the products?', ['In C-1 of ethanol and CO₂', 'In C-1 of ethanol only', 'In C-2 (methyl group) of ethanol only', 'In C-2 of ethanol and CO₂', 'In CO₂ only']),
    ko=mcq('C-1이 표지된 포도당을 에탄올 발효 효모에 주면 표지는 어디에?', ['에탄올 C-1과 CO₂', '에탄올 C-1만', '<b>에탄올 C-2(메틸)만</b>', '에탄올 C-2와 CO₂', 'CO₂만']),
    answer=ans('C', 'In C-2 (methyl group) of ethanol only', '에탄올의 메틸 탄소(C-2)만'),
    explain=carbon_map() + steps('C1 → 피루브산 메틸(C3).', '탈카복실화로 떨어지는 CO₂는 피루브산의 카복실(C1 ← 포도당 C3·C4).', '메틸은 그대로 → 아세트알데하이드의 CH₃ → 에탄올의 CH₃(C-2).') + key('에탄올 발효의 CO₂ = 포도당의 C3·C4.'))

add(n=48, sec=6, diff=2, kind='SA', title='발효의 정의와 NADH의 역할',
    en='<p>Define “fermentation” and explain, by describing relevant reactions, how it differs from glycolysis. Include a discussion of the role of NADH.</p>',
    ko='<p>“발효”를 정의하고, 관련 반응으로 해당과정과의 차이를 설명하라. NADH의 역할을 포함하라.</p>',
    answer=sa('Fermentation is glycolysis operating anaerobically. Without O₂, NADH from the GAPDH step cannot pass electrons to O₂, so it reduces pyruvate (→ lactate) or acetaldehyde (→ ethanol), regenerating NAD⁺ so glycolysis can continue.',
              '발효 = 산소 없이 돌아가는 해당. GAPDH가 만든 NADH가 O₂에 전자를 못 주니, 피루브산(→ 젖산)이나 아세트알데하이드(→ 에탄올)를 환원해 NAD⁺를 재생한다.'),
    explain=table(['', '해당 + 유산소', '발효'], [['피루브산', '→ 아세틸-CoA → TCA', '→ 젖산 / 에탄올'], ['NADH 재산화', 'O₂ (전자전달계)', '피루브산·아세트알데하이드'], ['ATP / 포도당', '≈ 30–32', '2']]) + key('발효의 목적은 에너지가 아니라 <b>NAD⁺ 되찾기</b>.'))

add(n=71, sec=6, diff=1, kind='SA', title='맥주를 무산소로 양조하는 이유',
    en='<p>The yeast used in brewing beer can break down glucose either aerobically or anaerobically. Explain why beer is brewed under anaerobic conditions.</p>',
    ko='<p>맥주 효모는 유산소·무산소 모두 포도당을 분해한다. 맥주를 무산소로 양조하는 이유는?</p>',
    answer=sa('With O₂, yeast oxidizes glucose aerobically (more energy) and makes no ethanol. Anaerobically, it ferments glucose to ethanol and CO₂, the key ingredients of beer.', '산소가 있으면 유산소 대사(에너지 많음)를 해서 알코올이 안 생긴다. 무산소일 때만 에탄올 + CO₂(맥주 거품)가 생긴다.'),
    explain=key('효모도 산소가 있으면 굳이 발효를 안 한다 (파스퇴르 효과의 반대 방향).') + tip('빵이 부푸는 것도 에탄올 발효의 CO₂ (슬라이드 29).', '연결'))

add(n=72, sec=6, diff=2, kind='SA', title='100 m 달리기 후 혈중 젖산 ↑',
    en='<p>Explain with words, diagrams, or structures why lactate accumulates in the blood during bursts of very vigorous exercise (such as a 100-meter dash).</p>',
    ko='<p>100 m 달리기 같은 격렬한 운동 중 혈중 젖산이 쌓이는 이유를 설명하라.</p>',
    answer=sa('O₂ cannot be delivered fast enough, so muscle works anaerobically. NADH from GAPDH cannot be reoxidized by O₂; it is reoxidized by reducing pyruvate to lactate, which accumulates and enters the blood.', '산소 공급이 수요를 못 따라감 → 무산소 → NADH를 O₂로 못 돌림 → 피루브산을 젖산으로 환원해 NAD⁺ 재생 → 젖산이 쌓여 혈액으로.'),
    explain=fig(flow(['포도당', '피루브산 + NADH', '젖산 + NAD⁺ → 혈액 → 간 (코리 회로)'], arrow_labels=['해당 (빠르게)', 'LDH'], colors=[C['navy'], C['orange'], C['red']], box_h=38, width=560, font=10.5), '') + key('운동 후 숨이 찬 것 = 쌓인 젖산을 간에서 처리할 산소 빚.'))

add(n=73, sec=6, diff=2, kind='SA', title='휴식 vs 전력 질주 — 피루브산의 운명',
    en='<p>Describe the fate of pyruvate formed by glycolysis in animal skeletal muscle (a) at rest and (b) during an all-out sprint. Explain why pyruvate metabolism differs.</p>',
    ko='<p>골격근에서 해당으로 생긴 피루브산의 운명을 (a) 휴식 (b) 전력 질주 때로 나누어 설명하라.</p>',
    answer=sa('(a) At rest, O₂ is plentiful: pyruvate → acetyl-CoA (PDH) → citric acid cycle → CO₂. (b) In a sprint, O₂ is insufficient: pyruvate is reduced to lactate to regenerate NAD⁺ so glycolysis continues.', '(a) 휴식: 산소 충분 → PDH → 아세틸-CoA → TCA → CO₂ (b) 전력 질주: 산소 부족 → 젖산으로 환원해 NAD⁺ 재생'),
    explain=fig(pyruvate_fates(), '') + key('같은 피루브산, 산소 공급이 갈림길을 정한다.'))

add(n=74, sec=6, diff=2, kind='SA', title='백색근에 LDH가 없다면',
    en='<p>In white skeletal muscle, ATP is produced almost exclusively by fermentation of glucose to lactate. If a person had white muscle tissue devoid of lactate dehydrogenase, how would this affect metabolism at rest and during strenuous exercise?</p>',
    ko='<p>백색 골격근은 거의 젖산 발효로만 ATP를 만든다. 백색근에 LDH가 없는 사람은 휴식 때와 격렬한 운동 때 어떻게 될까?</p>',
    answer=sa('At rest: little effect (aerobic red muscle suffices). During strenuous exercise: NAD⁺ cannot be regenerated anaerobically, so glycolysis stops and anaerobic performance is severely reduced (fatigue, cramps).', '휴식: 거의 문제없음(적색근의 유산소 대사로 충분). 격렬한 운동: NAD⁺를 재생 못 해 해당이 멈춤 → 무산소 운동 능력 크게 ↓'),
    explain=table(['', '적색근 (지구력)', '백색근 (순발력)'], [['미토콘드리아', '많음', '적음'], ['ATP', '유산소', '젖산 발효'], ['LDH 없으면', '영향 적음', '<b>해당 정지</b>']]) + key('LDH = 무산소 때 NAD⁺를 돌려주는 유일한 출구.'))

# ================================================================ S8 (7) 당신생
add(n=34, sec=7, diff=2, title='해당·당신생 둘 다 쓰는 효소',
    en=mcq('An enzyme used in both glycolysis and gluconeogenesis is:', ['3-phosphoglycerate kinase.', 'glucose 6-phosphatase.', 'hexokinase.', 'phosphofructokinase-1.', 'pyruvate kinase.']),
    ko=mcq('해당과정과 당신생에 모두 쓰이는 효소는?', ['<b>3-포스포글리세르산 키나아제(PGK)</b>', 'G6Pase', '헥소키나아제', 'PFK-1', '피루브산 키나아제']),
    answer=ans('A', '3-phosphoglycerate kinase', 'PGK (가역 반응)'),
    explain=fig(gng_bypass(), '') + key('비가역 3곳(헥소키나아제·PFK-1·PK)만 우회, 나머지 7개는 공유.') + steps('B(G6Pase)는 당신생 전용.', 'C·D·E는 해당 전용(비가역).'))

add(n=36, sec=7, diff=2, title='당신생에 쓰이지 않는 해당 효소',
    en=mcq('All of the following enzymes involved in glycolysis are also involved in gluconeogenesis <b>except</b>:', ['3-phosphoglycerate kinase.', 'aldolase.', 'enolase.', 'phosphofructokinase-1.', 'phosphoglucoisomerase.']),
    ko=mcq('해당 효소 중 당신생에 쓰이지 <b>않는</b> 것은?', ['PGK', '알돌라아제', '에놀레이스', '<b>PFK-1</b>', '포스포글루코이성질화효소']),
    answer=ans('D', 'phosphofructokinase-1', 'PFK-1 (당신생은 FBPase-1로 우회)'),
    explain=table(['해당 (비가역)', '당신생 우회'], [['헥소키나아제', 'G6Pase'], ['<b>PFK-1</b>', '<b>FBPase-1</b>'], ['피루브산 키나아제', 'PC + PEPCK']]))

add(n=35, sec=7, diff=2, title='당신생에 대해 틀린 것',
    en=mcq('Which one of the following statements about gluconeogenesis is false?', ['For starting materials, it can use carbon skeletons derived from certain amino acids.', 'It consists entirely of the reactions of glycolysis, operating in the reverse direction.', 'It employs the enzyme glucose 6-phosphatase.', 'It is one of the ways that mammals maintain normal blood glucose levels between meals.', 'It requires metabolic energy (ATP or GTP).']),
    ko=mcq('당신생에 대해 틀린 것은?', ['일부 아미노산의 탄소 골격을 원료로 쓸 수 있다', '<b>해당과정 반응을 그대로 거꾸로 돌린 것이다</b>', 'G6Pase를 쓴다', '식사 사이 혈당 유지 방법 중 하나다', 'ATP·GTP가 필요하다']),
    answer=ans('B', 'It consists entirely of the reactions of glycolysis, operating in the reverse direction.', '틀림 — 비가역 3단계는 다른 효소로 우회한다'),
    explain=fig(gng_bypass(), '') + key('7개는 공유, 3개는 우회(G6Pase, FBPase-1, PC+PEPCK).'))

add(n=37, sec=7, diff=2, title='사람의 당신생',
    en=mcq('In humans, gluconeogenesis:', ['can result in the conversion of protein into blood glucose.', 'helps to reduce blood glucose after a carbohydrate-rich meal.', 'is activated by the hormone insulin', 'is essential in the conversion of fatty acids to glucose.', 'requires the enzyme hexokinase.']),
    ko=mcq('사람에서 당신생은?', ['<b>단백질을 혈당으로 바꿀 수 있다</b>', '탄수화물 식사 후 혈당을 낮춘다', '인슐린이 활성화한다', '지방산 → 포도당 전환에 필수다', '헥소키나아제가 필요하다']),
    answer=ans('A', 'can result in the conversion of protein into blood glucose', '단백질(당원성 아미노산)을 혈당으로 바꿀 수 있다'),
    explain=steps('B·C: 당신생은 혈당을 <b>올리고</b>, 글루카곤이 켠다(인슐린은 끈다).', 'D: 동물은 지방산 → 포도당 불가 (16·17장).', 'E: 헥소키나아제는 해당 전용.') + key('기아 시 근육 단백질 → 알라닌 → 간 → 포도당 (포도당-알라닌 회로).'))

add(n=75, sec=7, diff=1, kind='SA', title='당신생이란? 왜 필요한가?',
    en='<p>What is gluconeogenesis, and what useful purposes does it serve in people?</p>',
    ko='<p>당신생이란 무엇이며, 사람에게 어떤 쓸모가 있나?</p>',
    answer=sa('Synthesis of glucose from noncarbohydrate precursors (lactate, pyruvate, glycerol, glucogenic amino acids). During fasting, when glycogen is exhausted, it supplies glucose to tissues that depend on it (brain, red blood cells).', '비탄수화물 전구체(젖산·피루브산·글리세롤·당원성 아미노산)로 포도당을 만드는 것. 공복으로 글리코겐이 바닥나면 뇌·적혈구에 포도당을 공급.'),
    explain=key('뇌는 하루 포도당 약 120 g. 적혈구는 미토콘드리아가 없어 포도당만 쓴다.') + table(['원료', '출처'], [['젖산', '근육·적혈구 (코리 회로)'], ['알라닌 등 아미노산', '근육 단백질'], ['글리세롤', '지방 분해']]))

add(n=76, sec=7, diff=2, kind='SA', title='¹⁴CO₂는 당신생 후 어디에?',
    en='<p>If you incubate ¹⁴C-CO₂ with liver extracts capable of performing gluconeogenesis, where does the radioactive label end up?</p>',
    ko='<p>당신생이 가능한 간 추출물에 ¹⁴CO₂를 넣으면 방사성 표지는 어디로 가나?</p>',
    answer=sa('Back in CO₂. It is added to pyruvate to form OAA (pyruvate carboxylase), then released as CO₂ when PEPCK forms PEP.', '다시 <b>CO₂</b>로. PC가 피루브산에 붙여 OAA를 만들지만, PEPCK가 PEP를 만들 때 같은 탄소를 CO₂로 떼어 낸다.'),
    explain=fig(flow(['피루브산 + ¹⁴CO₂', 'OAA (¹⁴C)', 'PEP + ¹⁴CO₂'], arrow_labels=['PC (비오틴, ATP)', 'PEPCK (GTP)'], colors=[C['navy'], C['orange'], C['green']], box_h=36, width=520), '') +
    key('CO₂는 “잠깐 빌려 썼다가 돌려주는” 활성화 손잡이 — 포도당에는 안 들어간다.'))

add(n=77, sec=7, diff=3, kind='SA', title='피루브산 → PEP (당신생)',
    en='<p>In gluconeogenesis, how do animals convert pyruvate to phosphoenolpyruvate? Show structures, enzymes, and cofactors.</p>',
    ko='<p>당신생에서 동물은 피루브산을 어떻게 PEP로 바꾸나? 구조, 효소, 보조인자를 보여라.</p>',
    answer=sa('(1) Pyruvate + HCO₃⁻ + ATP → oxaloacetate + ADP + Pᵢ (pyruvate carboxylase, biotin). (2) Oxaloacetate + GTP → PEP + CO₂ + GDP (PEP carboxykinase).', '① 피루브산 + HCO₃⁻ + ATP → OAA (피루브산 카복실화효소, <b>비오틴</b>) ② OAA + GTP → PEP + CO₂ (PEPCK)'),
    explain=fig(gng_bypass(), '') + table(['단계', '효소', '장소', '에너지'], [['① 카복실화', 'PC (비오틴)', '미토콘드리아', 'ATP'], ['② 탈카복실화 + 인산화', 'PEPCK', '미토 또는 세포질', 'GTP']]) +
    key('PK 한 단계를 거꾸로 하는 데 고에너지 2개(ATP + GTP).'))

# ================================================================ S9 (8) 비용·원료
add(n=33, sec=8, diff=2, title='당신생 원료가 될 수 없는 것',
    en=mcq('Which of the following compounds cannot serve as the starting material for the synthesis of glucose via gluconeogenesis?', ['acetate', 'glycerol', 'lactate', 'oxaloacetate', 'α-ketoglutarate']),
    ko=mcq('당신생의 출발 물질이 될 수 <b>없는</b> 것은?', ['<b>아세트산</b>', '글리세롤', '젖산', '옥살로아세트산', 'α-케토글루타르산']),
    answer=ans('A', 'acetate', '아세트산 (아세틸-CoA)'),
    explain=key('아세틸 2C가 TCA에 들어가면 CO₂ 2개로 나가 OAA가 순증가하지 않는다 → 포도당 불가 (16장).') +
    steps('글리세롤 → DHAP, 젖산 → 피루브산, OAA·α-KG → TCA → OAA → PEP: 모두 가능.'))

add(n=38, sec=8, diff=2, title='간에서 알짜 당신생에 기여 못 하는 것',
    en=mcq('Which of the following substrates cannot contribute to net gluconeogenesis in mammalian liver?', ['Alanine', 'Glutamate', 'Palmitate', 'Pyruvate', 'α-ketoglutarate']),
    ko=mcq('포유류 간에서 알짜 당신생에 기여할 수 <b>없는</b> 것은?', ['알라닌', '글루탐산', '<b>팔미트산</b>', '피루브산', 'α-KG']),
    answer=ans('C', 'Palmitate', '팔미트산 (짝수 지방산 → 아세틸-CoA만)'),
    explain=key('짝수 지방산 → 아세틸-CoA → CO₂. 글리옥실산 회로가 없는 동물은 포도당을 못 만든다.') + table(['원료', '진입', '포도당?'], [['알라닌', '피루브산', '○'], ['글루탐산', 'α-KG', '○'], ['<b>팔미트산</b>', '아세틸-CoA', '<b>✕</b>']]))

# ================================================================ S10 (9) PPP
add(n=39, sec=9, diff=2, title='PPP에 대해 옳은 것',
    en=mcq('Which of the following statements about the pentose phosphate pathway is correct?', ['It generates 36 mol of ATP per mole of glucose consumed.', 'It generates 6 moles of CO₂ for each mole of glucose consumed', 'It is a reductive pathway; it consumes NADH.', 'It is present in plants, but not in animals.', 'It provides precursors for the synthesis of nucleotides.']),
    ko=mcq('오탄당 인산 경로(PPP)에 대해 옳은 것은?', ['포도당당 ATP 36 mol', '포도당당 CO₂ 6 mol', '환원 경로로 NADH를 소비한다', '식물에만 있다', '<b>뉴클레오타이드 합성 재료를 공급한다</b>']),
    answer=ans('E', 'It provides precursors for the synthesis of nucleotides.', '뉴클레오타이드의 재료(리보스 5-인산)를 공급'),
    explain=fig(ppp_svg(), '') + steps('A: PPP는 ATP를 만들지 않는다.', 'B: 산화 단계에서 CO₂는 포도당당 1개.', 'C: NADP⁺를 <b>환원</b>해 NADPH를 <b>만든다</b>.', 'D: 동물에도 있다(간·지방·적혈구).'))

add(n=40, sec=9, diff=2, title='PPP의 대사적 기능',
    en=mcq('The metabolic function of the pentose phosphate pathway is to:', ['act as a source of ADP biosynthesis.', 'generate NADPH and pentoses for the biosynthesis of fatty acids and nucleic acids.', 'participate in oxidation-reduction reactions during the formation of H₂O.', 'provide intermediates for the citric acid cycle.', 'synthesize phosphorus pentoxide.']),
    ko=mcq('PPP의 대사적 기능은?', ['ADP 합성의 원료', '<b>지방산·핵산 합성을 위한 NADPH와 오탄당 생성</b>', '물 생성 산화-환원에 참여', 'TCA 중간체 공급', '오산화인 합성']),
    answer=ans('B', 'generate NADPH and pentoses for the biosynthesis of fatty acids and nucleic acids', 'NADPH(지방산 합성 등)와 오탄당(핵산)을 만든다'),
    explain=fig(ppp_svg(), '') + key('PPP의 두 산물 = <b>NADPH</b>(환원력·항산화) + <b>리보스 5-인산</b>(뉴클레오타이드).'))

add(n=80, sec=9, diff=1, kind='SA', title='PPP의 생물학적 기능',
    en='<p>What are the biological functions of the pentose phosphate pathway?</p>',
    ko='<p>PPP의 생물학적 기능은?</p>',
    answer=sa('It produces pentose phosphates (for nucleotide synthesis) and NADPH (reducing agent for biosynthesis and protection against oxidative damage).', '오탄당 인산(뉴클레오타이드 합성)과 NADPH(환원적 생합성·항산화)를 만든다.'),
    explain=table(['산물', '쓰임'], [['리보스 5-인산', 'DNA·RNA·ATP·NAD⁺·CoA'], ['NADPH', '지방산·스테로이드 합성, GSH 재생(적혈구 보호)']]) + tip('G6PD 결핍 → NADPH ↓ → 적혈구 용혈 (파비즘, S12).', '연결'))

add(n=41, sec=9, diff=2, title='PPP에 대해 틀린 것',
    en=mcq('Which of the following statements about the pentose phosphate pathway is incorrect?', ['It generates CO₂ from C-1 of glucose.', 'It involves the conversion of an aldohexose to an aldopentose.', 'It is prominent in lactating mammary gland.', 'It is principally directed toward the generation of NADPH.', 'It requires the participation of molecular oxygen.']),
    ko=mcq('PPP에 대해 틀린 것은?', ['포도당 C-1에서 CO₂를 만든다', '알도헥소스를 알도펜토스로 바꾼다', '수유 중인 젖샘에서 활발하다', '주로 NADPH 생성을 향한다', '<b>산소 분자(O₂)가 필요하다</b>']),
    answer=ans('E', 'It requires the participation of molecular oxygen.', '산소가 필요하다 — 틀림. 전자는 NADP⁺가 받는다'),
    explain=key('PPP의 “산화”는 NADP⁺가 전자를 받는 탈수소 반응 — O₂와 무관.') + steps('C: 젖샘은 젖 지방(지방산) 합성으로 NADPH가 많이 필요 → PPP 활발.', 'A: 6-포스포글루콘산 탈수소효소가 C-1을 CO₂로.'))

add(n=42, sec=9, diff=2, title='6-포스포글루콘산의 다음 운명',
    en=mcq('Glucose breakdown in certain cells can occur by mechanisms other than classic glycolysis. In most of these, glucose 6-phosphate is oxidized to 6-phosphogluconate, which is then further metabolized by:', ['an aldolase-type split to form glyceric acid and glyceraldehyde 3-phosphate.', 'an aldolase-type split to form glycolic acid and erythrose 4-phosphate.', 'conversion to 1,6-bisphosphogluconate.', 'decarboxylation to produce keto- and aldopentoses.', 'oxidation to a six-carbon dicarboxylic acid.']),
    ko=mcq('G6P가 6-포스포글루콘산으로 산화된 뒤 어떻게 대사되나?', ['알돌라아제식 절단 → 글리세르산 + G3P', '알돌라아제식 절단 → 글리콜산 + 에리트로스 4-인산', '1,6-비스포스포글루콘산으로', '<b>탈카복실화되어 케토·알도 오탄당이 된다</b>', '6탄소 다이카복실산으로 산화']),
    answer=ans('D', 'decarboxylation to produce keto- and aldopentoses', '산화적 탈카복실화 → 리불로스 5-인산(케토) → 리보스 5-인산(알도)'),
    explain=fig(flow(['G6P', '6-포스포글루콘산', '리불로스 5-인산', '리보스 5-인산'], arrow_labels=['G6PD (NADPH)', '탈수소·탈카복실화 (NADPH, CO₂)', '이성질화'], colors=[C['navy'], C['navy'], C['orange'], C['green']], box_h=36, width=560, font=10), '') + key('6C → 5C: CO₂ 하나가 빠진다.'))

add(n=43, sec=9, diff=2, title='PPP에서 일하는 효소',
    en=mcq('Which of the following enzymes acts in the pentose phosphate pathway?', ['6-Phosphogluconate dehydrogenase', 'Aldolase', 'Glycogen phosphorylase', 'Phosphofructokinase-1', 'Pyruvate kinase']),
    ko=mcq('PPP에서 일하는 효소는?', ['<b>6-포스포글루콘산 탈수소효소</b>', '알돌라아제', '글리코겐 인산화효소', 'PFK-1', '피루브산 키나아제']),
    answer=ans('A', '6-Phosphogluconate dehydrogenase', '6-포스포글루콘산 탈수소효소 (NADPH + CO₂ 생성)'),
    explain=table(['PPP 효소', '단계'], [['G6PD', '산화 ① (NADPH)'], ['락토네이스', '산화 ②'], ['<b>6-포스포글루콘산 탈수소효소</b>', '산화 ③ (NADPH, CO₂)'], ['트랜스케톨레이스 (TPP) · 트랜스알돌레이스', '비산화']], cls='left'))

add(n=44, sec=9, diff=3, title='포도당 3 mol을 PPP로 산화하면',
    en=mcq('The oxidation of 3 mol of glucose by the pentose phosphate pathway may result in the production of:', ['2 mol of pentose, 4 mol of NADPH, and 8 mol of CO₂.', '3 mol of pentose, 4 mol of NADPH, and 3 mol of CO₂.', '3 mol of pentose, 6 mol of NADPH, and 3 mol of CO₂.', '4 mol of pentose, 3 mol of NADPH, and 3 mol of CO₂.', '4 mol of pentose, 6 mol of NADPH, and 6 mol of CO₂.']),
    ko=mcq('포도당 3 mol을 PPP로 산화하면 생기는 것은?', ['오탄당 2, NADPH 4, CO₂ 8', '오탄당 3, NADPH 4, CO₂ 3', '<b>오탄당 3, NADPH 6, CO₂ 3</b>', '오탄당 4, NADPH 3, CO₂ 3', '오탄당 4, NADPH 6, CO₂ 6']),
    answer=ans('C', '3 mol of pentose, 6 mol of NADPH, and 3 mol of CO₂', '오탄당 3 + NADPH 6 + CO₂ 3'),
    explain=eq('포도당 6-인산 + 2NADP⁺ + H₂O → 리보스 5-인산 + <b>2NADPH</b> + 2H⁺ + <b>CO₂</b>') + steps('포도당 1개당: 오탄당 1, NADPH 2, CO₂ 1.', '× 3 → 3, 6, 3.') + key('“1 · 2 · 1” 비율만 기억하면 된다.'))

add(n=45, sec=9, diff=2, title='¹⁴CO₂가 가장 빨리 나오는 표지 위치',
    en=mcq('Glucose labeled with ¹⁴C in different carbon atoms is added to a crude extract of a tissue rich in pentose phosphate pathway enzymes. The most rapid production of ¹⁴CO₂ will occur when the glucose is labeled in:', ['C-1.', 'C-3.', 'C-4.', 'C-5.', 'C-6.']),
    ko=mcq('PPP 효소가 풍부한 조직 추출물에서 ¹⁴CO₂가 가장 빨리 나오는 포도당 표지 위치는?', ['<b>C-1</b>', 'C-3', 'C-4', 'C-5', 'C-6']),
    answer=ans('A', 'C-1', 'C-1'),
    explain=key('6-포스포글루콘산 탈수소효소가 떼어 내는 CO₂ = 포도당의 <b>C-1</b> (산화된 C1의 카복실기).') + fig(ppp_c1_graph(), '') + tip('해당 + TCA로는 C-1·C-6이 같이, 훨씬 늦게 나온다 (TB 14-81).', '연결'))

add(n=46, sec=9, diff=2, title='PPP에서 포도당 C-1의 행방',
    en=mcq('In a tissue that metabolizes glucose via the pentose phosphate pathway, C-1 of glucose would be expected to end up principally in:', ['carbon dioxide.', 'glycogen.', 'phosphoglycerate.', 'pyruvate.', 'ribulose 5-phosphate.']),
    ko=mcq('PPP로 포도당을 대사하는 조직에서 포도당 C-1은 주로 어디로?', ['<b>이산화탄소</b>', '글리코겐', '포스포글리세르산', '피루브산', '리불로스 5-인산']),
    answer=ans('A', 'carbon dioxide', 'CO₂'),
    explain=key('C1 → (G6PD 산화) 락톤 → 6-포스포글루콘산의 –COO⁻ → (탈카복실화) <b>CO₂</b>. 리불로스 5-인산은 C2–C6.') + tip('바로 앞 기출(TB 14-45)과 같은 원리.', '연결'))

add(n=78, sec=9, diff=2, kind='SA', title='해당(G) · PPP(P) · 둘 다 · 둘 다 아님',
    en='<p>Rat liver metabolizes glucose by both glycolysis and the pentose phosphate pathway. Indicate glycolytic (G), pentose phosphate (P), both (G + P), or neither (0): NAD⁺ is involved; CO₂ is liberated; phosphate esters are intermediates; glyceraldehyde 3-phosphate is an intermediate; fructose 6-phosphate is an intermediate.</p>',
    ko='<p>쥐 간은 해당과 PPP 모두로 포도당을 대사한다. 각 항목이 해당(G), PPP(P), 둘 다(G+P), 둘 다 아님(0) 중 무엇인지: NAD⁺ 관여 / CO₂ 방출 / 인산 에스터 중간체 / G3P 중간체 / F6P 중간체</p>',
    answer=sa('G; P; G + P; G; G (test bank key)', 'NAD⁺ = G · CO₂ = P · 인산 에스터 = G+P · G3P = G · F6P = G (테스트뱅크 정답)'),
    explain=table(['항목', '정답', '이유'], [['NAD⁺', 'G', 'PPP는 NADP⁺를 쓴다'], ['CO₂ 방출', 'P', '해당은 CO₂를 안 낸다'], ['인산 에스터', 'G + P', '둘 다 인산화된 당'], ['G3P', 'G', '(해당의 핵심 중간체)'], ['F6P', 'G', '(해당의 핵심 중간체)']], cls='left') +
    warn('PPP의 <b>비산화 단계</b>(트랜스케톨레이스·트랜스알돌레이스)에서도 G3P와 F6P가 생기므로 “G + P”도 맞다고 볼 수 있어. 교수님 채점 기준을 확인하자. 테스트뱅크는 산화 단계만 보고 G로 적은 것.', '주의'))

add(n=79, sec=9, diff=3, kind='SA', title='대장균은 리보스 5-인산을 어디서?',
    en='<p>E. coli can grow with glucose as its only carbon source. How does it obtain ribose 5-phosphate (for ATP synthesis)? Show structures and indicate where cofactors participate.</p>',
    ko='<p>대장균은 포도당만으로 자랄 수 있다. ATP 합성에 필요한 리보스 5-인산은 어떻게 얻나? 보조인자가 관여하는 곳을 표시하라.</p>',
    answer=sa('From the oxidative pentose phosphate pathway: glucose → G6P (ATP) → 6-phosphogluconolactone (G6PD, NADP⁺) → 6-phosphogluconate (lactonase) → ribulose 5-phosphate + CO₂ (6-phosphogluconate dehydrogenase, NADP⁺) → ribose 5-phosphate (isomerase).',
              'PPP 산화 단계: 포도당 → G6P → (G6PD, NADP⁺) 락톤 → (락토네이스) 6-포스포글루콘산 → (탈수소효소, NADP⁺, −CO₂) 리불로스 5-인산 → (이성질화효소) 리보스 5-인산'),
    explain=fig(ppp_svg(), '') + key('NADPH가 두 번(G6PD, 6PG 탈수소효소), CO₂가 한 번.'))

add(n=81, sec=9, diff=3, kind='SA', title='지방조직 추출물: C-1 vs C-6 표지',
    en='<p>An extract of adipose tissue can metabolize glucose to CO₂. When glucose labeled with ¹⁴C in either C-1 or C-6 was added, ¹⁴CO₂ was released with the time courses shown (C-1 label released much faster than C-6). What is the major path of glucose oxidation? Explain.</p>',
    ko='<p>지방조직 추출물이 포도당을 CO₂로 대사한다. C-1 또는 C-6 표지 포도당을 넣었더니 C-1 표지에서 ¹⁴CO₂가 훨씬 빨리 나왔다(그래프). 주 산화 경로는? 이유는?</p>',
    answer=sa('Mainly the pentose phosphate pathway: it releases C-1 as CO₂ early (6-phosphogluconate dehydrogenase). In glycolysis, C-1 and C-6 become equivalent in G3P and would be released together, later, via the citric acid cycle.',
              '주로 <b>PPP</b>. PPP는 C-1을 먼저 CO₂로 떼어 낸다. 해당이라면 C-1과 C-6이 G3P에서 같아져 TCA에서 함께, 늦게 나와야 한다.'),
    explain=fig(ppp_c1_graph(), '테스트뱅크 그래프를 단순화해 다시 그림') + steps('두 곡선이 겹치면 → 해당 + TCA (C1 = C6).', 'C-1이 훨씬 빠르면 → PPP가 C-1만 먼저 떼어 냄.') +
    key('지방조직은 지방산 합성에 NADPH가 많이 필요 → PPP가 활발.'))
