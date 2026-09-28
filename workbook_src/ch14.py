# -*- coding: utf-8 -*-
"""Chapter 14 — Glycolysis, Gluconeogenesis, and the Pentose Phosphate Pathway"""
from helpers import *

CHAPTER = '14'
CH_TITLE = '해당과정 · 당신생 · 오탄당 인산 경로'
CH_EN = 'Glycolysis, Gluconeogenesis, and the Pentose Phosphate Pathway'
STAT = ('10', '해당과정 단계 (지도 수록)')
SCOPE = ('교수님 14장 강의(슬라이드 1–54) 범위 = <b>14.1 해당과정</b>, <b>14.2 공급 경로</b>, <b>14.3 발효</b>, '
         '<b>14.4 당신생</b>, <b>14.5 오탄당 인산 경로</b> — 14장 전체. 그래서 ★★★와 DATA ANALYSIS를 뺀 나머지를 모두 담았어.')
INCLUDE = ['<b>본문 예제</b> 14-1 (글리코겐 인산분해의 ATP 절약)',
           '<b>해당과정 반응·에너지</b> — 문제 1–10, 12, 13, 18–21',
           '<b>공급 경로·갈락토스</b> — 문제 14',
           '<b>발효·젖산</b> — 문제 7, 8, 15–17, 23, 24',
           '<b>당신생</b> — 문제 25, 27–32',
           '<b>오탄당 인산 경로</b> — 문제 33']
EXCLUDE = ['<b>문제 34</b> — DATA ANALYSIS PROBLEM']

ALL_ITEMS = []


def add(**kw):
    kw.setdefault('section', '연습문제')
    kw.setdefault('kind', 'PROBLEM')
    ALL_ITEMS.append(kw)


RT25, RT37 = '2.478', '2.578'

# ---------------------------------------------------------------- drawings
def fbp_split():
    """F1,6BP carbons → DHAP + G3P (aldolase) and TPI"""
    W, H = 520, 250
    b = arrowdef('fs', C['gray']) + arrowdef('fs2', C['orange'])
    xs = 40
    labs = ['C1 (CH₂OP)', 'C2 (C=O)', 'C3 (CHOH)', 'C4 (CHOH)', 'C5 (CHOH)', 'C6 (CH₂OP)']
    b += T(95, 16, '과당 1,6-이인산', 12, C['navy'], weight=900)
    for i, l in enumerate(labs):
        y = 26 + i * 32
        hot = i in (2, 3)
        b += f'<rect x="{xs}" y="{y}" width="110" height="26" rx="6" fill="{"#fff7ed" if hot else "white"}" stroke="{C["orange"] if hot else C["navy"]}" stroke-width="{2 if hot else 1.2}"/>'
        b += T(xs + 55, y + 17, l, 10.5, C['orange'] if hot else C['navy'], weight=700 if hot else 400)
    b += f'<line x1="{xs-12}" y1="{26+3*32-3}" x2="{xs+124}" y2="{26+3*32-3}" stroke="{C["red"]}" stroke-width="2" stroke-dasharray="5 3"/>'
    b += T(xs + 130, 26 + 3 * 32, '알돌라아제가 자름', 10, C['red'], 'start', 700)
    # DHAP
    b += T(330, 44, 'DHAP (C1–C3 유래)', 11.5, C['blue'], weight=900)
    b += T(330, 62, 'C3 → CH₂OH 탄소 ★', 10.5, C['orange'], weight=700)
    b += T(330, 150, 'G3P (C4–C6 유래)', 11.5, C['green'], weight=900)
    b += T(330, 168, 'C4 → 알데하이드 C-1 ★', 10.5, C['orange'], weight=700)
    b += f'<line x1="160" y1="70" x2="250" y2="56" stroke="{C["gray"]}" stroke-width="1.6" marker-end="url(#fs)"/>'
    b += f'<line x1="160" y1="170" x2="250" y2="160" stroke="{C["gray"]}" stroke-width="1.6" marker-end="url(#fs)"/>'
    b += f'<path d="M430,70 C470,90 470,130 430,145" fill="none" stroke="{C["orange"]}" stroke-width="2" marker-start="url(#fs2)" marker-end="url(#fs2)"/>'
    b += T(478, 112, 'TPI', 11, C['orange'], 'start', 900)
    b += T(260, 225, '★ 표지된 G3P의 C-1은 알돌라아제 역반응으로 FBP의 C-4가 되고,', 10.5, C['ink'])
    b += T(260, 242, 'TPI로 DHAP이 된 표지 G3P는 C-1(→DHAP의 CH₂OH)이 FBP의 C-3이 된다', 10.5, C['ink'])
    return svg(W, H, b)


def atp_ledger(rows, width=520):
    """rows: (label, value int, color)"""
    b = ''
    y = 8
    for lab, v, col in rows:
        b += T(10, y + 16, lab, 11.5, C['ink'], 'start', 700)
        s = f'{v:+d}'.replace('-', '−')
        b += f'<rect x="300" y="{y}" width="{abs(v)*24}" height="22" rx="5" fill="{col}"/>'
        b += T(300 + abs(v) * 24 + 8, y + 16, s + ' ATP', 11.5, col, 'start', 700)
        y += 32
    return svg(width, y + 4, b)


def lactate_cori():
    W, H = 520, 170
    b = arrowdef('co', C['blue']) + arrowdef('co2', C['red'])
    b += f'<rect x="20" y="30" width="170" height="110" rx="14" fill="#fef2f2" stroke="#fca5a5"/>' + T(105, 52, '근육 (전력 질주)', 12, C['red'], weight=900)
    b += T(105, 82, '포도당 → 피루브산', 10.5, C['ink']) + T(105, 100, '→ 젖산 (LDH)', 10.5, C['ink']) + T(105, 122, '빠른 ATP 2개', 10.5, C['red'], weight=700)
    b += f'<rect x="330" y="30" width="170" height="110" rx="14" fill="#eff6ff" stroke="#93c5fd"/>' + T(415, 52, '간 (휴식 중)', 12, C['blue'], weight=900)
    b += T(415, 82, '젖산 → 피루브산', 10.5, C['ink']) + T(415, 100, '→ 당신생 → 포도당', 10.5, C['ink']) + T(415, 122, 'ATP 6개 소비 (느림)', 10.5, C['blue'], weight=700)
    b += f'<path d="M190,60 C250,40 280,40 328,60" fill="none" stroke="{C["red"]}" stroke-width="2.2" marker-end="url(#co2)"/>' + T(260, 36, '혈액 속 젖산', 10.5, C['red'], weight=700)
    b += f'<path d="M328,115 C280,135 250,135 192,115" fill="none" stroke="{C["blue"]}" stroke-width="2.2" marker-end="url(#co)"/>' + T(260, 150, '혈액 속 포도당', 10.5, C['blue'], weight=700)
    b += T(260, 166, '코리 회로 (Cori cycle)', 11, C['gray'], weight=700)
    return svg(W, H + 6, b)


# ---------------------------------------------------------------- front pages
GLY = [
    ('1', '포도당 + ATP → G6P + ADP', '헥소키나아제', '−16.7', '−33.4', 'ATP −1 · 비가역'),
    ('2', 'G6P ⇌ F6P', '포스포헥소스 이성질화효소', '+1.7', '0 ~ 25', '이성질화'),
    ('3', 'F6P + ATP → F1,6BP + ADP', 'PFK-1', '−14.2', '−22.2', 'ATP −1 · 비가역 · <b>핵심 조절</b>'),
    ('4', 'F1,6BP ⇌ DHAP + G3P', '알돌라아제', '+23.8', '−6 ~ 0', 'C6 → C3 × 2'),
    ('5', 'DHAP ⇌ G3P', '삼탄당 인산 이성질화효소 (TPI)', '+7.5', '0 ~ 4', '이제 G3P 2개'),
    ('6', 'G3P + P<sub>i</sub> + NAD<sup>+</sup> ⇌ 1,3-BPG + NADH + H<sup>+</sup>', 'G3P 탈수소효소', '+6.3', '−2 ~ 2', 'NADH +1 (×2)'),
    ('7', '1,3-BPG + ADP ⇌ 3PG + ATP', '포스포글리세르산 키나아제', '−18.8', '0 ~ 2', 'ATP +1 (×2)'),
    ('8', '3PG ⇌ 2PG', '포스포글리세르산 뮤테이스', '+4.4', '0 ~ 0.8', '인산 위치 이동'),
    ('9', '2PG ⇌ PEP + H<sub>2</sub>O', '에놀레이스', '+7.5', '0 ~ 3.3', '탈수 → 고에너지 PEP'),
    ('10', 'PEP + ADP → 피루브산 + ATP', '피루브산 키나아제', '−31.4', '−16.7', 'ATP +1 (×2) · 비가역'),
]


def front_pages():
    rows = [[n, r, e, g, gg, note] for n, r, e, g, gg, note in GLY]
    for r in rows:
        if r[0] in ('1', '3', '10'):
            r[0] = f'<b style="color:#dc2626">{r[0]}</b>'
    t = table(['단계', '반응', '효소', 'ΔG′° (kJ/mol)', '세포 속 ΔG', '포인트'], rows, cls='left')
    p1 = f'''<h2 class="pt"><span class="n">MAP</span> 해당과정 10단계 한눈에 (표 14-2)</h2>
<p class="lead">빨간 번호(1·3·10) = 세포 속 ΔG가 크게 음수인 <b>비가역 단계</b> → 당신생에서 우회하는 곳이자 조절 지점. 나머지는 ΔG ≈ 0 (평형 근처, 양방향).</p>
<div class="card">{t}</div>
<div class="grid2" style="margin-top:3mm">
 <div class="card"><h4>📦 준비 단계 (1–5): 투자</h4><p>포도당(C6) 1개 → G3P(C3) 2개, <b>ATP 2개 소비</b></p>
  <div class="formula">포도당 + 2ATP → 2 G3P + 2ADP</div></div>
 <div class="card"><h4>💰 수익 단계 (6–10): 회수 (×2)</h4><p>G3P 2개 → 피루브산 2개, <b>ATP 4개 · NADH 2개 생산</b> → 순수익 ATP 2개</p>
  <div class="formula">포도당 + 2NAD<sup>+</sup> + 2ADP + 2P<sub>i</sub> → 2 피루브산 + 2NADH + 2H<sup>+</sup> + 2ATP + 2H<sub>2</sub>O</div></div>
</div>'''
    p2 = f'''<h2 class="pt"><span class="n">KIT</span> 발효 · 당신생 · 오탄당 인산 경로 핵심 정리</h2>
<p class="lead">14장 문제의 대부분은 아래 세 카드 중 하나에서 답이 나와.</p>
<div class="grid3">
 <div class="card"><h4><span class="no">1</span> 피루브산의 운명 (산소 없을 때 = 발효)</h4>
  <p><b>젖산 발효</b> (근육·적혈구·젖산균)</p>
  <div class="formula">피루브산 + NADH + H<sup>+</sup> → 젖산 + NAD<sup>+</sup></div>
  <p class="small">젖산 탈수소효소(LDH), ΔG′° = −25.1 kJ/mol</p>
  <p><b>에탄올 발효</b> (효모)</p>
  <div class="formula">피루브산 → 아세트알데하이드 + CO<sub>2</sub> → 에탄올</div>
  <p class="small">피루브산 탈카복실화효소(TPP 필요) → 알코올 탈수소효소(NADH 사용)</p>
  {key('발효의 진짜 목적 = <b>NAD<sup>+</sup> 재생</b>. 그래야 6단계(G3P 탈수소효소)가 계속 돌아 ATP를 만든다.')}
 </div>
 <div class="card"><h4><span class="no">2</span> 당신생 = 피루브산 → 포도당</h4>
  <p>해당과정의 비가역 3단계를 <b>다른 효소로 우회</b>:</p>
  <p>① 피루브산 → OAA → PEP: <b>피루브산 카복실화효소</b>(ATP, 비오틴) + <b>PEPCK</b>(GTP)</p>
  <p>② F1,6BP → F6P: <b>FBPase-1</b> (가수분해)</p>
  <p>③ G6P → 포도당: <b>G6Pase</b> (간·신장의 소포체에만)</p>
  <div class="formula" style="font-size:10pt">2 피루브산 + 4ATP + 2GTP + 2NADH → 포도당 (+…)</div>
  {warn('해당과정은 ATP 2개를 벌지만, 당신생은 ATP 4 + GTP 2 = <b>6개</b>를 쓴다.', '숫자')}
 </div>
 <div class="card"><h4><span class="no">3</span> 오탄당 인산 경로 (PPP)</h4>
  <p><b>산화 단계</b>: G6P → 리불로스 5-인산 + CO<sub>2</sub>, <b>NADPH 2개</b></p>
  <div class="formula" style="font-size:10pt">G6P + 2NADP<sup>+</sup> + H<sub>2</sub>O → 리보스 5-P + CO<sub>2</sub> + 2NADPH</div>
  <p class="small">첫 효소 = <b>G6P 탈수소효소(G6PD)</b> — 결핍 시 파비즘·용혈</p>
  <p><b>비산화 단계</b>: 트랜스케톨레이스(TPP)·트랜스알돌레이스가 5탄당 ↔ 6탄당·3탄당 재배열 → 남는 리보스를 해당과정 중간체로 되돌림</p>
  {tip('NADPH = 생합성·항산화(글루타싸이온 환원)용 전자, NADH = ATP 만들기용 전자. 쓰임새가 다르다.', '구분')}
 </div>
</div>'''
    return [p1, p2]


# ---------------------------------------------------------------- items
add(id='WE14-1', kind='WORKED EXAMPLE', num='14-1', section='본문 예제',
    en_title='Energy Savings for Glycogen Breakdown by Phosphorolysis', ko_title='인산분해로 글리코겐을 분해할 때의 에너지 절약',
    slides='강의 슬라이드 23–24', level=1,
    en='<p>Calculate the energy savings (in ATP molecules per glucose monomer) achieved by breaking down glycogen by phosphorolysis rather than hydrolysis to begin the process of glycolysis.</p>',
    ko='<p>해당과정을 시작할 때 글리코겐을 <b>가수분해</b>(물로 자르기) 대신 <b>인산분해</b>(P<sub>i</sub>로 자르기)로 분해하면, 포도당 단위 하나당 ATP 몇 개를 절약하는지 계산하라.</p>',
    answer=chips('포도당 1개당 <b>ATP 1개 절약</b>', '순수익 ATP: 2개 → <b>3개</b>'),
    explain=key('인산분해는 처음부터 <b>인산이 붙은 포도당(G1P)</b>을 내준다 → 헥소키나아제로 ATP를 써서 인산을 붙일 필요가 없다.') +
    fig(flow(['글리코겐', '포도당 1-인산', '포도당 6-인산', '해당과정'], arrow_labels=['+ Pᵢ (ATP 0)', '뮤테이스', '']), '인산분해 경로: ATP를 쓰지 않고 G6P에 도착') +
    steps('<b>유리 포도당에서 시작</b>: 준비 단계에서 ATP 2개(1단계 헥소키나아제 + 3단계 PFK-1) 소비, 수익 단계에서 4개 생산 → 순수익 <b>2 ATP</b>.',
          '<b>글리코겐 인산분해에서 시작</b>: G1P → G6P(포스포글루코뮤테이스)는 ATP가 필요 없음 → 준비 단계에서 ATP 1개(PFK-1)만 소비 → 4 − 1 = <b>3 ATP</b>.',
          '차이 = 3 − 2 = <span class="hl">포도당 1개당 ATP 1개 절약</span>.') +
    tip('가수분해로 자르면 “인산 없는 포도당”이 나와서 다시 ATP로 인산을 붙여야 해. 인산분해는 자르는 순간 P<sub>i</sub>를 붙여 주니 공짜로 한 단계를 건너뛰는 셈.'))

add(id='P1', num='1', en_title='Is the Hexokinase Reaction at Equilibrium in Cells?', ko_title='세포 속 헥소키나아제 반응은 평형 상태일까?',
    slides='강의 슬라이드 10, 35', level=1,
    en=f'''<p>For the reaction catalyzed by the enzyme hexokinase</p>{rx('Glucose + ATP', 'glucose 6-phosphate + ADP')}
<p>the equilibrium constant, K<sub>eq</sub>, is 7.8 × 10<sup>2</sup>. In living <i>E. coli</i> cells, [ATP] = 5 m<span class="sc">M</span>, [ADP] = 0.5 m<span class="sc">M</span>, [glucose] = 2 m<span class="sc">M</span>, and [glucose 6-phosphate] = 1 m<span class="sc">M</span>. Is the reaction at equilibrium in <i>E. coli</i>?</p>''',
    ko='<p>헥소키나아제가 촉매하는 반응(포도당 + ATP ⇌ 포도당 6-인산 + ADP)의 평형상수 K<sub>eq</sub>는 7.8 × 10<sup>2</sup>이다. 살아 있는 대장균 세포에서 [ATP] = 5 mM, [ADP] = 0.5 mM, [포도당] = 2 mM, [포도당 6-인산] = 1 mM이다. 대장균 속에서 이 반응은 평형 상태인가?</p>',
    answer=chips('Q = <b>0.05</b> ≪ K = 780', '→ 평형이 <b>아니다</b> (평형보다 훨씬 왼쪽, 정반응이 강하게 진행: ΔG ≈ −24 kJ/mol)'),
    explain=key('평형인지 보려면 “지금 비율” Q를 계산해서 K와 비교! Q = K면 평형, Q &lt; K면 앞으로 더 간다.') +
    steps(eq(f'Q = {F("[G6P][ADP]", "[포도당][ATP]")} = {F("(1)(0.5)", "(2)(5)")} = 0.05'),
          '분자·분모 농도가 2개씩이라 mM 단위가 지워져 그대로 계산해도 OK.',
          'Q(0.05)는 K(780)의 약 <b>1/16,000</b> → 평형과 거리가 아주 멀다.',
          f'ΔG = RT ln(Q/K) = {RT25} × ln(6.4×10<sup>−5</sup>) ≈ <span class="hl">−24 kJ/mol</span> → 크게 음수 = 사실상 <b>비가역</b>.') +
    fig(logaxis([(0.05, '세포 속 Q = 0.05', C['orange']), (780, '평형 K = 780', C['navy'])], -2, 4, label='약 16,000배 차이'), 'Q와 K가 멀리 떨어짐 = 평형에서 먼 반응') +
    tip('그래서 헥소키나아제는 해당과정의 <b>비가역 3단계</b>(1·3·10단계) 중 하나이고, 당신생에서는 G6Pase라는 다른 효소로 우회한다.', '연결'))

add(id='P2', num='2', en_title='Equation for the Preparatory Phase of Glycolysis', ko_title='해당과정 준비 단계의 반응식',
    slides='강의 슬라이드 6–7, 10–15', level=2,
    en='<p>Write balanced biochemical equations for all the reactions in the catabolism of glucose to two molecules of glyceraldehyde 3-phosphate (the preparatory phase of glycolysis), including the standard free-energy change for each reaction. Then write the overall or net equation for the preparatory phase of glycolysis, with the net standard free-energy change.</p>',
    ko='<p>포도당이 글리세르알데하이드 3-인산 2분자로 분해되는 모든 반응(해당과정의 준비 단계)의 균형 잡힌 생화학 반응식을 각 반응의 표준 자유에너지 변화와 함께 써라. 그다음 준비 단계 전체(알짜) 반응식과 알짜 표준 자유에너지 변화를 써라.</p>',
    answer=chips('알짜: 포도당 + 2ATP → 2 G3P + 2ADP + 2H<sup>+</sup>', f'{G0}<sub>알짜</sub> = <b>+2.1 kJ/mol</b>'),
    explain=key('5개 반응을 순서대로 쓰고 ΔG′°를 그냥 <b>더한다</b>(13장 가산성). 5단계(TPI)로 DHAP이 G3P가 되어 G3P가 2개.') +
    align([('①', '포도당 + ATP → G6P + ADP', '−16.7'), ('②', 'G6P ⇌ F6P', '+1.7'), ('③', 'F6P + ATP → F1,6BP + ADP', '−14.2'),
           ('④', 'F1,6BP ⇌ DHAP + G3P', '+23.8'), ('⑤', 'DHAP ⇌ G3P', '+7.5'),
           ('합', '포도당 + 2ATP → 2 G3P + 2ADP + 2H<sup>+</sup>', '<span class="hl">+2.1</span>')], cls='sum') +
    fig(energy_steps([('포도당', 0, C['navy']), ('G6P', -16.7, C['blue']), ('F6P', -15.0, C['blue']), ('F1,6BP', -29.2, C['blue']),
                      ('DHAP+G3P', -5.4, C['orange']), ('2 G3P', 2.1, C['orange'])], height=210), 'ATP 2개를 “투자”해 인산을 붙인 뒤, C6를 C3 두 개로 쪼갠다') +
    tip('준비 단계는 에너지를 얻는 단계가 아니라 <b>투자</b> 단계. ATP 2개를 써서 포도당을 “잘 쪼개지는” 모양(인산 2개)으로 만든다. 표준값이 +2.1이어도 세포 속에선 농도 덕분에 잘 진행돼.', '비유'))

add(id='P3', num='3', en_title='Payoff Phase of Glycolysis: Fate of Pyruvate in Active Skeletal Muscle', ko_title='해당과정 수익 단계: 활동하는 골격근에서 피루브산의 운명',
    slides='강의 슬라이드 8, 16–20, 30', level=2,
    en='<p>In working skeletal muscle under anaerobic conditions, glyceraldehyde 3-phosphate is converted to pyruvate (the payoff phase of glycolysis), and the pyruvate is reduced to lactate. Write balanced biochemical equations for all the reactions in this process, with the standard free-energy change for each reaction. Then write the overall or net equation for the payoff phase of glycolysis with fermentation to lactate, including the net standard free-energy change.</p>',
    ko='<p>무산소 조건에서 일하는 골격근에서는 글리세르알데하이드 3-인산이 피루브산으로 바뀌고(해당과정의 수익 단계), 피루브산은 젖산으로 환원된다. 이 과정의 모든 반응을 각 반응의 표준 자유에너지 변화와 함께 균형 잡힌 반응식으로 써라. 그다음 젖산 발효를 포함한 수익 단계의 알짜 반응식과 알짜 표준 자유에너지 변화를 써라.</p>',
    answer=chips('알짜: 2 G3P + 2P<sub>i</sub> + 4ADP → 2 젖산 + 4ATP + 2H<sub>2</sub>O', f'{G0}<sub>알짜</sub> ≈ <b>−114 kJ/mol</b>'),
    explain=key('G3P 1개 기준으로 6개 반응을 더한 뒤 <b>×2</b>. NAD<sup>+</sup>는 6단계에서 쓰이고 LDH에서 다시 만들어져 알짜식에서 지워진다.') +
    align([('⑥', 'G3P + P<sub>i</sub> + NAD<sup>+</sup> ⇌ 1,3-BPG + NADH + H<sup>+</sup>', '+6.3'), ('⑦', '1,3-BPG + ADP ⇌ 3PG + ATP', '−18.8'),
           ('⑧', '3PG ⇌ 2PG', '+4.4'), ('⑨', '2PG ⇌ PEP + H<sub>2</sub>O', '+7.5'), ('⑩', 'PEP + ADP → 피루브산 + ATP', '−31.4'),
           ('LDH', '피루브산 + NADH + H<sup>+</sup> → 젖산 + NAD<sup>+</sup>', '−25.1'),
           ('G3P 1개', 'G3P + P<sub>i</sub> + 2ADP → 젖산 + 2ATP + H<sub>2</sub>O', '−57.1'),
           ('×2', '2 G3P + 2P<sub>i</sub> + 4ADP → 2 젖산 + 4ATP + 2H<sub>2</sub>O', '<span class="hl">−114.2</span>')], cls='sum') +
    tip('준비 단계(+2.1, 문제 2)와 합치면 포도당 → 2 젖산 + 2ATP 전체가 약 −112 kJ/mol. ATP는 4개 벌지만 준비 단계에서 2개 썼으니 <b>순수익 2개</b>.', '연결') +
    warn('⑦ 값은 교과서 본문에서 −18.5로도 나와(표 14-2는 −18.8). 어느 값을 써도 결론은 같다.', '참고'))

add(id='P4', num='4', en_title='Energetics of the Aldolase Reaction', ko_title='알돌라아제 반응의 에너지',
    slides='강의 슬라이드 14', level=1,
    en=f'''<p>Aldolase catalyzes the glycolytic reaction</p>{rx('Fructose 1,6-bisphosphate', 'glyceraldehyde 3-phosphate + dihydroxyacetone phosphate', rev=False)}
<p>The standard free-energy change for this reaction in the direction written is +23.8 kJ/mol. The concentrations of the three intermediates in the hepatocyte of a mammal are fructose 1,6-bisphosphate, 1.4 × 10<sup>−5</sup> <span class="sc">M</span>; glyceraldehyde 3-phosphate, 3 × 10<sup>−6</sup> <span class="sc">M</span>; and dihydroxyacetone phosphate, 1.6 × 10<sup>−5</sup> <span class="sc">M</span>. At body temperature (37 °C), what is the actual free-energy change for the reaction?</p>''',
    ko='<p>알돌라아제는 해당과정 반응(과당 1,6-이인산 → 글리세르알데하이드 3-인산 + 다이하이드록시아세톤 인산)을 촉매한다. 쓰인 방향의 표준 자유에너지 변화는 +23.8 kJ/mol이다. 포유류 간세포 속 세 중간체의 농도는 과당 1,6-이인산 1.4×10<sup>−5</sup> M, G3P 3×10<sup>−6</sup> M, DHAP 1.6×10<sup>−5</sup> M이다. 체온(37 °C)에서 이 반응의 실제 자유에너지 변화는?</p>',
    answer=chips(f'{DG} ≈ <b>−8.6 kJ/mol</b> (표준값은 +23.8이지만 세포 속에서는 음수 → 진행)'),
    explain=key('13장 공식 그대로: ΔG = ΔG′° + RT ln Q. 반응물 1개 → 생성물 2개라 Q가 <b>아주 작아진다</b>.') +
    steps(eq(f'Q = {F("[G3P][DHAP]", "[F1,6BP]")} = {F("(3×10<sup>−6</sup>)(1.6×10<sup>−5</sup>)", "1.4×10<sup>−5</sup>")} = 3.4×10<sup>−6</sup>'),
          f'RT (37 °C) = {RT37} kJ/mol,  ln(3.4×10<sup>−6</sup>) = −12.6',
          align([(DG, f'23.8 + ({RT37})(−12.6)'), ('', '23.8 − 32.4 = <span class="hl">−8.6 kJ/mol</span>')])) +
    fig(bars([('표준 ΔG′°', 23.8, C['red'], '+23.8 (오르막)'), ('세포 속 ΔG', 8.6, C['green'], '−8.6 (내리막)')], height=90), '같은 반응도 농도에 따라 방향이 바뀐다') +
    tip('생성물이 2개인 반응은 농도가 작을수록(μM 수준) Q가 “제곱”처럼 작아져서 유리해져. 거기에 뒤 단계들이 G3P를 계속 가져가니 알돌라아제는 세포에서 잘 굴러간다.', '포인트'))

add(id='P5', num='5', en_title='Equivalence of Triose Phosphates', ko_title='두 삼탄당 인산은 서로 같은 운명',
    slides='강의 슬라이드 14–15', level=2,
    en='<p>A researcher adds <sup>14</sup>C-labeled glyceraldehyde 3-phosphate to a yeast extract. After a short time, she isolates fructose 1,6-bisphosphate labeled with <sup>14</sup>C at C-3 and C-4. What was the location of the <sup>14</sup>C label in the starting glyceraldehyde 3-phosphate? Where did the second <sup>14</sup>C label in fructose 1,6-bisphosphate come from? Explain.</p>',
    ko='<p>연구자가 <sup>14</sup>C로 표지된 글리세르알데하이드 3-인산(G3P)을 효모 추출물에 넣었다. 잠시 후 C-3과 C-4가 <sup>14</sup>C로 표지된 과당 1,6-이인산을 분리했다. 처음 G3P에서 <sup>14</sup>C는 어디에 있었는가? 과당 1,6-이인산의 두 번째 <sup>14</sup>C 표지는 어디서 왔는가? 설명하라.</p>',
    answer=chips('처음 표지 위치: G3P의 <b>C-1</b> (알데하이드 탄소)', '두 번째 표지: 표지 G3P가 <b>TPI</b>로 DHAP이 된 뒤, <b>알돌라아제 역반응</b>으로 다른 표지 G3P와 결합'),
    explain=key('알돌라아제와 TPI는 둘 다 <b>가역</b>(ΔG ≈ 0). 그래서 G3P → DHAP, G3P + DHAP → F1,6BP 방향으로도 반응이 일어난다.') +
    fig(fbp_split(), 'F1,6BP의 탄소 번호와 DHAP·G3P의 대응') +
    steps('F1,6BP의 C4–C6은 G3P에서 온다: <b>G3P C-1(알데하이드) = FBP C-4</b>. → 표지는 G3P의 C-1에 있었다.',
          '표지 G3P 일부가 TPI로 DHAP이 된다. 이때 G3P의 C-1은 DHAP의 CH<sub>2</sub>OH 탄소(C-3)가 된다.',
          '표지 DHAP(C1–C3 부분)가 알돌라아제 역반응으로 표지 G3P와 합쳐지면, DHAP의 그 탄소가 <b>FBP의 C-3</b>이 된다 → C-3과 C-4 둘 다 표지.') +
    tip('자르는 칼(알돌라아제)이 붙이는 풀 역할도 할 수 있어. 세포 속에서 평형 근처인 반응은 앞뒤로 계속 왔다 갔다 하니까 표지가 “섞인다”.', '직관'))

add(id='P6', num='6', en_title='Glycolysis Shortcut', ko_title='해당과정 지름길',
    slides='강의 슬라이드 16–17', level=1,
    en=f'''<p>Suppose you discovered a mutant yeast whose glycolytic pathway was shorter because of the presence of a new enzyme catalyzing the reaction</p>{img('c14_p6.png', '78%')}<p>Would shortening the glycolytic pathway in this way benefit the cell? Explain.</p>''',
    ko='<p>새로운 효소 때문에 해당과정이 짧아진 돌연변이 효모를 발견했다고 하자. 이 효소는 G3P + H<sub>2</sub>O + NAD<sup>+</sup> → 3-포스포글리세르산 + NADH + H<sup>+</sup> 반응을 촉매한다(1,3-BPG를 거치지 않음). 해당과정을 이렇게 줄이는 것이 세포에 이로울까? 설명하라.</p>',
    answer=chips('<b>이롭지 않다</b> — 7단계(PGK)의 ATP 생성을 건너뛰어 해당과정의 순수익 ATP가 <b>2 → 0</b>'),
    explain=key('1,3-BPG의 “고에너지 아실인산 결합”이 7단계에서 ATP로 바뀐다. 이 중간체를 건너뛰면 그 ATP가 사라진다.') +
    fig(flow(['G3P', '1,3-BPG', '3PG'], arrow_labels=['6단계 (+Pᵢ)', '7단계: ATP 생성!'], colors=[C['navy'], C['orange'], C['navy']]), '정상 경로: G3P → 1,3-BPG → 3PG 사이에서 ATP 1개(×2)') +
    fig(atp_ledger([('정상 해당과정 (포도당 1개)', 2, C['green']), ('지름길 효모', 0, C['red'])]), '') +
    steps('정상: 준비 단계 −2 ATP, 7단계 +2, 10단계 +2 → 순수익 <b>+2</b>.',
          '지름길: G3P의 산화 에너지가 ATP로 저장되지 않고 <b>열</b>로 버려짐 → 7단계 +2가 없어져 −2 + 2 = <b>0</b>.',
          '무산소에서 효모는 해당과정만으로 ATP를 얻으니 → 살 수 없거나 크게 불리.') +
    tip('월급(산화 에너지)을 통장(ATP)에 넣지 않고 길바닥에 버리는 셈. 길이 짧아졌다고 좋은 게 아니야.'))

add(id='P7', num='7', en_title='Role of Lactate Dehydrogenase', ko_title='젖산 탈수소효소의 역할',
    slides='강의 슬라이드 27–30', level=1,
    en='<p>During strenuous activity, the demand for ATP in muscle tissue vastly increases. In rabbit leg muscle or turkey flight muscle, ATP production is almost exclusively a product of lactic acid fermentation. Phosphoglycerate kinase and pyruvate kinase catalyze the two reactions that form ATP in the payoff phase of glycolysis. Suppose skeletal muscle were devoid of lactate dehydrogenase. Could it carry out strenuous physical activity; that is, could it generate ATP at a high rate by glycolysis? Explain.</p>',
    ko='<p>격렬한 활동 중에는 근육의 ATP 수요가 크게 늘어난다. 토끼 다리 근육이나 칠면조 비행 근육에서 ATP는 거의 전부 젖산 발효로 만들어진다. 해당과정 수익 단계에서 ATP를 만드는 두 반응은 포스포글리세르산 키나아제와 피루브산 키나아제가 촉매한다. 골격근에 젖산 탈수소효소(LDH)가 없다고 가정하자. 이 근육이 격렬한 활동을 할 수 있을까? 즉 해당과정으로 ATP를 빠르게 만들 수 있을까? 설명하라.</p>',
    answer=chips('<b>할 수 없다</b> — LDH가 없으면 NADH → NAD<sup>+</sup> 재생이 안 됨 → 6단계(G3P 탈수소효소)가 멈춤 → 해당과정 전체 정지'),
    explain=key('LDH는 ATP를 직접 만들지 않지만, <b>NAD<sup>+</sup>를 되돌려 주는</b> 역할로 해당과정을 계속 돌게 한다.') +
    fig(flow(['G3P', '1,3-BPG', '피루브산', '젖산'], arrow_labels=['NAD⁺ → NADH', '…ATP 생성…', 'NADH → NAD⁺ (LDH)'],
             colors=[C['navy'], C['navy'], C['navy'], C['green']]), 'NAD⁺는 6단계에서 쓰이고 LDH에서 돌려받는다 = 재활용 순환') +
    steps('세포 속 NAD<sup>+</sup>는 양이 아주 적다. 6단계에서 G3P 1개를 산화할 때마다 NAD<sup>+</sup> 1개가 NADH가 된다.',
          '산소가 부족한 격렬한 운동 중엔 미토콘드리아가 NADH를 충분히 산화하지 못한다 → LDH가 유일한 NAD<sup>+</sup> 재생 통로.',
          'LDH가 없으면 NAD<sup>+</sup>가 곧 바닥 → 6단계 정지 → 7·10단계(ATP 생성)도 멈춤 → 빠른 ATP 공급 불가.') +
    tip('NAD<sup>+</sup>는 식당의 “빈 접시”야. 접시(NAD<sup>+</sup>)를 씻어서(LDH) 다시 내놓지 않으면, 음식(G3P)이 아무리 많아도 손님을 받을 수 없다.'))

add(id='P8', num='8', en_title='Efficiency of ATP Production in Muscle', ko_title='근육의 ATP 생산 효율',
    slides='강의 슬라이드 30–31', level=1,
    en='<p>The transformation of glucose to lactate in myocytes releases only about 7% of the free energy released when glucose is completely oxidized to CO<sub>2</sub> and H<sub>2</sub>O. Does this mean that glycolysis with lactate fermentation under anaerobic conditions in muscle is a wasteful use of glucose? Explain.</p>',
    ko='<p>근육세포에서 포도당 → 젖산 전환은 포도당을 CO<sub>2</sub>와 H<sub>2</sub>O로 완전히 산화할 때 방출되는 자유에너지의 약 7%만 방출한다. 그렇다면 근육의 무산소 해당과정 + 젖산 발효는 포도당을 낭비하는 것인가? 설명하라.</p>',
    answer=chips('<b>낭비가 아니다</b> — 나머지 에너지는 <b>젖산 속에 그대로 남아</b> 있고, 간(코리 회로)이나 심장 등에서 다시 쓰인다', '대신 산소 없이 <b>빠르게</b> ATP를 얻는 장점'),
    explain=key('에너지가 “버려진” 게 아니라 젖산이라는 형태로 <b>보관</b>된 것. 젖산은 혈액을 타고 다른 조직으로 간다.') +
    fig(lactate_cori(), '코리 회로: 근육이 만든 젖산을 간이 포도당으로 되돌려 보낸다') +
    steps('격렬한 운동 = 산소 공급이 수요를 못 따라감 → 빠른 ATP가 필요 → 해당과정은 산화적 인산화보다 훨씬 빠르다.',
          '젖산은 혈액으로 나가 ① 간에서 당신생으로 포도당이 되거나(코리 회로) ② 심장·휴식 근육에서 피루브산으로 되돌려 완전히 산화된다.',
          '결국 포도당의 에너지는 대부분 나중에 회수된다 → 전체적으로 보면 낭비가 아님.') +
    tip('급할 때 현금(ATP)을 빨리 뽑아 쓰고, 남은 돈(젖산)은 저축 통장(간)에 넣어 두는 것과 같아.'))

add(id='P9', num='9', en_title='Free-Energy Change for Triose Phosphate Oxidation', ko_title='삼탄당 인산 산화의 자유에너지 변화',
    slides='강의 슬라이드 16–17', level=1,
    en="<p>The oxidation of glyceraldehyde 3-phosphate to 1,3-bisphosphoglycerate, catalyzed by glyceraldehyde 3-phosphate dehydrogenase, proceeds with an unfavorable equilibrium constant (K′<sub>eq</sub> = 0.08; ΔG′° = 6.3 kJ/mol), yet the flow through this point in the glycolytic pathway proceeds smoothly. How does the cell overcome the unfavorable equilibrium?</p>",
    ko='<p>G3P 탈수소효소가 촉매하는 G3P → 1,3-이인산글리세르산 산화는 평형상수가 불리하다(K′<sub>eq</sub> = 0.08, ΔG′° = +6.3 kJ/mol). 그런데도 해당과정의 이 지점은 원활하게 흘러간다. 세포는 이 불리한 평형을 어떻게 극복하는가?</p>',
    answer=chips('다음 단계(7단계, PGK, ΔG′° = −18.8)가 <b>1,3-BPG를 즉시 소비</b>', '→ 생성물 농도가 낮게 유지되어 Q ≪ K → 실제 ΔG ≈ 0 이하 → 계속 진행'),
    explain=key('불리한 반응 + 뒤따르는 유리한 반응 = <b>공통 중간체로 짝지어진 반응</b>(13장 공역). 합치면 내리막.') +
    align([('⑥', 'G3P + P<sub>i</sub> + NAD<sup>+</sup> → 1,3-BPG + NADH', '+6.3'), ('⑦', '1,3-BPG + ADP → 3PG + ATP', '−18.8'),
           ('합', 'G3P + P<sub>i</sub> + NAD<sup>+</sup> + ADP → 3PG + NADH + ATP', '<span class="hl">−12.5</span>')], cls='sum') +
    steps('ΔG = ΔG′° + RT ln Q. 1,3-BPG가 생기자마자 7단계가 가져가니 [1,3-BPG]가 아주 낮다 → Q가 작다 → ΔG가 음수 쪽으로.',
          '실제로 적혈구 속 6단계의 ΔG는 −2 ~ +2 kJ/mol로 거의 0(평형 근처). 흐름은 뒤 단계가 “당겨서” 만든다.',
          '또 LDH·미토콘드리아가 NADH를 NAD<sup>+</sup>로 되돌려 NAD<sup>+</sup>/NADH를 높게 유지하는 것도 도움.') +
    tip('물을 위로 퍼 올리는 펌프(6단계) 바로 뒤에 폭포(7단계)가 있어서, 퍼 올린 물이 곧바로 떨어져 나가는 구조야.'))

add(id='P10', num='10', en_title='Arsenate Poisoning', ko_title='비산염 중독',
    slides='강의 슬라이드 16–17', level=2,
    en=f'''<p>Arsenate is structurally and chemically similar to inorganic phosphate (P<sub>i</sub>), and many enzymes that require phosphate will also use arsenate. Organic compounds of arsenate are less stable than analogous phosphate compounds, however. For example, acyl <i>arsenates</i> decompose rapidly by hydrolysis, as shown.</p>{img('c14_p10.png', '50%')}
<p>On the other hand, acyl <i>phosphates</i>, such as 1,3-bisphosphoglycerate, are more stable and undergo further enzyme-catalyzed transformation in cells.<br><b>a.</b> Predict the effect on the net reaction catalyzed by glyceraldehyde 3-phosphate dehydrogenase if phosphate were replaced by arsenate.<br><b>b.</b> What would be the consequence to an organism if arsenate were substituted for phosphate? Arsenate is very toxic to most organisms. Explain why.</p>''',
    ko='<p>비산염(arsenate)은 무기 인산(P<sub>i</sub>)과 구조·화학적으로 비슷해서, 인산을 쓰는 많은 효소가 비산염도 쓴다. 하지만 비산염 유기 화합물은 인산 화합물보다 불안정하다. 예를 들어 아실 비산염은 위 그림처럼 빠르게 가수분해된다. 반면 1,3-BPG 같은 아실 인산은 더 안정해서 세포 속에서 다음 효소 반응으로 넘어간다.<br><b>a.</b> 인산 대신 비산염이 쓰이면 G3P 탈수소효소가 촉매하는 알짜 반응은 어떻게 되는가?<br><b>b.</b> 생물에서 비산염이 인산을 대신하면 어떤 결과가 생기는가? 비산염은 대부분의 생물에 매우 독하다. 이유를 설명하라.</p>',
    answer=chips('a. 1-아세노-3-포스포글리세르산이 생기자마자 저절로 분해 → 알짜: <b>G3P + NAD<sup>+</sup> + H<sub>2</sub>O → 3PG + NADH</b> (1,3-BPG·ATP 생성 건너뜀)',
                 'b. 7단계 ATP를 잃어 해당과정 순수익 ATP <b>0</b> → ATP 고갈 → 독성'),
    explain=key('문제 6의 “지름길”이 비산염 때문에 실제로 일어나는 것! 7단계 기질(1,3-BPG)이 만들어지지 않는다.') +
    fig(flow(['G3P', '1-아세노-3-PG', '3PG'], arrow_labels=['+ 비산염 (6단계)', '저절로 가수분해 (ATP 없음)'], colors=[C['navy'], C['red'], C['navy']]), '비산염이 있으면 PGK 단계가 사라진다') +
    steps('<b>a.</b> G3P 탈수소효소는 P<sub>i</sub> 대신 비산염을 붙여 1-아세노-3-포스포글리세르산을 만든다. 이 아실 비산염은 효소를 만나기 전에 물과 반응해 3PG + 비산염으로 분해된다. 비산염은 다시 쓰이므로(촉매처럼) 알짜로는 G3P가 바로 3PG로 산화되는 셈.',
          '<b>b.</b> 7단계(PGK)에서 만들어질 ATP 2개가 없어져 해당과정의 순수익이 0. 세포가 ATP를 만들지 못해 에너지 고갈 → 치명적. (비산염은 ATP 합성효소에서도 ADP-비산염을 만들어 산화적 인산화도 방해한다.)') +
    tip('겉모습만 비슷한 “가짜 부품”이 조립 라인에 들어가, 완성품(ATP)이 나오기 직전에 부서져 버리는 것과 같아.', '비유'))

add(id='P12', num='12', en_title='Role of the Vitamin Niacin', ko_title='비타민 나이아신의 역할',
    slides='강의 슬라이드 16 (NAD⁺)', level=1,
    en='<p>Adults engaged in strenuous physical activity require an intake of about 160 g of carbohydrate daily but only about 20 mg of niacin for optimal nutrition. Given the role of niacin in glycolysis, how do you explain the observation?</p>',
    ko='<p>격렬한 신체 활동을 하는 성인은 최적의 영양을 위해 하루 약 160 g의 탄수화물이 필요하지만, 나이아신은 약 20 mg만 필요하다. 해당과정에서 나이아신의 역할을 생각할 때 이 관찰을 어떻게 설명하는가?</p>',
    answer=chips('나이아신 → <b>NAD<sup>+</sup></b>(조효소)', 'NAD<sup>+</sup>는 반응에서 소모되지 않고 NAD<sup>+</sup> ⇄ NADH로 <b>계속 재활용</b> → 조금만 있어도 충분'),
    explain=key('기질(포도당)은 반응할 때마다 <b>없어지지만</b>, 조효소(NAD<sup>+</sup>)는 <b>되돌아온다</b>.') +
    steps('나이아신(비타민 B<sub>3</sub>)은 NAD<sup>+</sup>의 니코틴아마이드 부분의 원료.',
          'NAD<sup>+</sup>는 6단계에서 NADH가 됐다가 LDH나 미토콘드리아 전자전달계에서 다시 NAD<sup>+</sup>가 된다 → 하루에 수천 번 재사용.',
          '160 g 포도당 ≈ 0.9 mol인데 NAD<sup>+</sup>는 촉매량만 있으면 된다. 식이로는 조금씩 분해·손실되는 몫만 보충하면 됨.') +
    tip('포도당은 “연료”, NAD<sup>+</sup>는 연료를 나르는 “트럭”. 연료는 매일 많이 사야 하지만, 트럭은 몇 대만 있으면 계속 왕복한다.'))

add(id='P13', num='13', en_title='Synthesis of Glycerol Phosphate', ko_title='글리세롤 인산의 합성',
    slides='강의 슬라이드 14–15', level=1,
    en='<p>The glycerol 3-phosphate required for the synthesis of glycerophospholipids can be synthesized from a glycolytic intermediate. Propose a reaction sequence for this conversion.</p>',
    ko='<p>글리세로인지질 합성에 필요한 글리세롤 3-인산은 해당과정 중간체로부터 합성할 수 있다. 이 전환의 반응 순서를 제안하라.</p>',
    answer=chips('<b>DHAP + NADH + H<sup>+</sup> → 글리세롤 3-인산 + NAD<sup>+</sup></b>', '효소: 글리세롤 3-인산 탈수소효소 (한 단계 환원)'),
    explain=key('DHAP의 케톤(C=O)을 알코올(CH–OH)로 <b>환원</b>하면 바로 글리세롤 3-인산. 탄소 3개·인산 1개 위치가 딱 맞다.') +
    fig(flow(['DHAP|CH₂OH–C(=O)–CH₂OP', '글리세롤 3-인산|CH₂OH–CHOH–CH₂OP'], arrow_labels=['NADH → NAD⁺'], width=460, box_h=46, colors=[C['navy'], C['green']]), '4단계에서 나온 DHAP의 C=O를 환원') +
    steps('해당과정 4단계(알돌라아제)에서 DHAP이 생긴다.', 'NADH가 수소(전자 2개 + H<sup>+</sup>)를 C=O에 넘겨 C–OH로 만든다.', '이 반응은 지방세포·간에서 지방(트라이아실글리세롤)과 인지질의 “뼈대”를 만드는 출발점.') +
    tip('해당과정은 에너지 공장이면서 동시에 <b>부품 공급처</b>야. DHAP은 지방의 뼈대로, 3PG는 세린 같은 아미노산으로 빠져나간다.', '연결'))

add(id='P14', num='14', en_title='Severity of Clinical Symptoms Due to Enzyme Deficiency', ko_title='효소 결핍에 따른 임상 증상의 심각도',
    slides='강의 슬라이드 26', level=2,
    en='<p>The clinical symptoms of two forms of galactosemia — galactokinase-deficiency galactosemia and transferase-deficiency galactosemia — show radically different severity. Although both types produce gastric discomfort after milk ingestion, deficiency of the transferase also leads to liver, kidney, spleen, and brain dysfunction and eventual death. What products accumulate in the blood and tissues with each type of enzyme deficiency? Estimate the relative toxicities of these products from the above information.</p>',
    ko='<p>갈락토스혈증의 두 형태 — 갈락토키나아제 결핍형과 전이효소(transferase) 결핍형 — 은 증상의 심각도가 크게 다르다. 둘 다 우유를 마신 뒤 위장 불편감을 일으키지만, 전이효소 결핍은 간·신장·비장·뇌 기능 장애와 결국 사망까지 일으킨다. 각 효소 결핍에서 혈액과 조직에 무엇이 쌓이는가? 위 정보로부터 이 물질들의 상대적 독성을 추정하라.</p>',
    answer=chips('갈락토키나아제 결핍: <b>갈락토스</b>(+ 갈락티톨) 축적', '전이효소 결핍: <b>갈락토스 + 갈락토스 1-인산</b> 축적', '→ <b>갈락토스 1-인산이 훨씬 독성이 크다</b>'),
    explain=key('효소가 막히면 <b>그 효소의 기질</b>(과 그 앞 물질)이 쌓인다. 어느 단계가 막혔는지만 찾으면 끝.') +
    fig(flow(['갈락토스', '갈락토스 1-인산', 'UDP-갈락토스|→ 포도당 1-인산'], arrow_labels=['갈락토키나아제 (ATP)', '전이효소 (UDP-포도당)'], colors=[C['orange'], C['red'], C['navy']], width=520, box_h=44), '갈락토스 → 해당과정으로 들어가는 길') +
    steps('<b>갈락토키나아제 결핍</b>: 첫 단계가 막힘 → 갈락토스가 쌓이고 일부는 갈락티톨로 환원(수정체에 쌓여 백내장).',
          '<b>전이효소 결핍</b>: 두 번째 단계가 막힘 → 갈락토스 1-인산이 세포 안에 갇혀 쌓이고, 갈락토스도 쌓인다.',
          '두 경우의 차이는 “갈락토스 1-인산이 쌓이느냐”뿐인데 전이효소 결핍만 치명적 → <b>갈락토스 1-인산이 갈락토스보다 훨씬 독하다</b>고 추정할 수 있다. (인산이 붙어 세포 밖으로 못 나가고, 인산을 붙잡아 두어 ATP·P<sub>i</sub>가 부족해지는 것도 원인.)') +
    tip('치료는 둘 다 같다: 우유(젖당 = 포도당 + 갈락토스)를 끊는 것.', '임상'))

add(id='P15', num='15', en_title='Ethanol Affects Blood Glucose Levels', ko_title='에탄올은 혈당에 영향을 준다',
    slides='강의 슬라이드 29–31, 34', level=2,
    en=f'''<p>The consumption of alcohol (ethanol), especially after periods of strenuous activity or after not eating for several hours, results in a deficiency of glucose in the blood, a condition known as hypoglycemia. The first step in the metabolism of ethanol by the liver is oxidation to acetaldehyde, catalyzed by liver alcohol dehydrogenase:</p>
<p class="c">CH<sub>3</sub>CH<sub>2</sub>OH + NAD<sup>+</sup> → CH<sub>3</sub>CHO + NADH + H<sup>+</sup></p>
<p>Explain how this reaction inhibits the transformation of lactate to pyruvate. Why does this lead to hypoglycemia?</p>''',
    ko='<p>알코올(에탄올)을 마시면, 특히 격렬한 활동 후나 몇 시간 굶은 뒤에는 혈중 포도당이 부족해지는 저혈당이 생긴다. 간에서 에탄올 대사의 첫 단계는 간 알코올 탈수소효소가 촉매하는 아세트알데하이드로의 산화이다(위 반응식). 이 반응이 어떻게 젖산 → 피루브산 전환을 억제하는지 설명하라. 왜 이것이 저혈당으로 이어지는가?</p>',
    answer=chips('에탄올 산화로 간 세포질의 <b>NADH ↑, NAD<sup>+</sup> ↓</b>', '→ LDH의 젖산 → 피루브산(NAD<sup>+</sup> 필요)이 막힘', '→ 당신생 원료 부족 → 포도당 못 만듦 → <b>저혈당</b>'),
    explain=key('젖산 → 피루브산은 <b>NAD<sup>+</sup>가 있어야</b> 일어나는 산화 반응. 에탄올이 NAD<sup>+</sup>를 다 NADH로 바꿔 버린다.') +
    eq('젖산 + NAD<sup>+</sup> ⇌ 피루브산 + NADH + H<sup>+</sup> &nbsp;&nbsp; (LDH)') +
    steps('에탄올 분해가 NAD<sup>+</sup> → NADH를 대량으로 만든다 → [NADH]/[NAD<sup>+</sup>] ↑.',
          '르샤틀리에: 생성물(NADH)이 많고 반응물(NAD<sup>+</sup>)이 적으니 LDH 반응이 왼쪽(피루브산 → 젖산)으로 밀린다 → 젖산에서 피루브산이 안 만들어짐. (같은 이유로 말산 → 옥살로아세트산도 막힌다.)',
          '공복·운동 후엔 간 글리코겐이 바닥이라 혈당을 <b>당신생</b>에 의존하는데, 그 원료인 피루브산이 부족 → 포도당 생산 ↓ → 저혈당.') +
    tip('술 마신 다음 날 식사를 거르면 특히 위험한 이유. 뇌는 포도당을 주 연료로 쓰기 때문에 저혈당은 어지러움·의식 저하로 이어질 수 있어.', '임상'))

add(id='P16', num='16', en_title='Blood Lactate Levels during Vigorous Exercise', ko_title='격렬한 운동 중 혈중 젖산 농도',
    slides='강의 슬라이드 30–31', level=2,
    en=f'''<p>The graph shows the concentrations of lactate in blood plasma before, during, and after a 400 m sprint.</p>{img('c14_p16.png', '34%')}
<p><b>a.</b> What causes the rapid rise in lactate concentration?<br><b>b.</b> What causes the decline in lactate concentration after completion of the sprint? Why does the decline occur more slowly than the increase?<br><b>c.</b> Why is the concentration of lactate not zero during the resting state?</p>''',
    ko='<p>그래프는 400 m 전력 질주 전·중·후 혈장의 젖산 농도를 보여 준다.<br><b>a.</b> 젖산 농도가 빠르게 올라가는 원인은?<br><b>b.</b> 질주가 끝난 뒤 젖산 농도가 내려가는 원인은? 왜 감소가 증가보다 느린가?<br><b>c.</b> 휴식 상태에서 젖산 농도가 0이 아닌 이유는?</p>',
    answer=chips('a. 산소 부족 → 근육의 <b>젖산 발효</b>가 폭발적으로 증가', 'b. 간(<b>코리 회로</b>·당신생)과 심장 등이 젖산을 가져가 처리 — 이 과정은 발효보다 <b>느리다</b>',
                 'c. <b>적혈구</b>(미토콘드리아 없음) 등은 항상 젖산을 만든다'),
    explain=steps('<b>a.</b> 전력 질주: ATP 수요 ≫ 산소 공급 → 해당과정이 최고 속도로 돌고, NAD<sup>+</sup> 재생을 위해 피루브산 → 젖산. 젖산이 혈액으로 쏟아진다.',
                  '<b>b.</b> 운동 후 젖산은 ① 간에서 피루브산 → 당신생 → 포도당(코리 회로) ② 심장·휴식 근육에서 피루브산 → 완전 산화. 당신생은 ATP 6개가 드는 여러 단계 과정이고 산소 공급·효소 속도에 제한이 있어 발효(빠른 해당과정)보다 느리다.',
                  '<b>c.</b> 적혈구는 미토콘드리아가 없어 오직 해당과정 + 젖산 발효로만 ATP를 얻는다. 망막·신장 수질 등도 젖산을 만든다 → 항상 기본 농도가 있다.') +
    fig(lactate_cori(), '올라갈 때 = 근육의 발효(빠름) / 내려갈 때 = 간의 당신생(느림)') +
    tip('그래프의 가파른 오르막 = “빚을 빨리 짐”, 완만한 내리막 = “빚을 천천히 갚음”. 운동 후에도 숨이 찬 이유(초과 산소 소비) 중 하나야.', '비유'))

add(id='P17', num='17', en_title='Relationship between Fructose 1,6-Bisphosphatase and Blood Lactate Levels', ko_title='FBPase-1과 혈중 젖산 농도의 관계',
    slides='강의 슬라이드 35–36', level=1,
    en='<p>A congenital defect in the liver enzyme fructose 1,6-bisphosphatase results in abnormally high levels of lactate in the blood plasma. Explain.</p>',
    ko='<p>간 효소인 과당 1,6-이인산가수분해효소(FBPase-1)의 선천적 결함은 혈장 젖산 농도를 비정상적으로 높인다. 설명하라.</p>',
    answer=chips('FBPase-1 = <b>당신생의 우회 효소</b>', '결함 → 간이 젖산 → 포도당(당신생)을 못 함 → 젖산이 혈액에 <b>쌓인다</b>'),
    explain=key('간은 혈중 젖산의 “처리장”. 처리 공정(당신생)의 한 단계가 막히면 원료(젖산)가 쌓인다.') +
    fig(vflow(['젖산', '피루브산', '… PEP … F1,6BP', 'F6P', '포도당'], notes=['LDH', '', '✕ FBPase-1 결함', ''],
              colors=[C['red'], C['navy'], C['navy'], C['gray'], C['gray']], box_h=26, gap=18), '당신생의 두 번째 우회 지점에서 길이 끊김') +
    steps('해당과정 3단계(PFK-1)는 비가역이라 당신생은 FBPase-1로 F1,6BP → F6P를 우회한다.',
          'FBPase-1이 없으면 피루브산·젖산 → 포도당 경로가 중간에서 막힌다.',
          '근육·적혈구가 계속 만드는 젖산을 간이 처리하지 못함 → 혈중 젖산 ↑ (젖산산증), 공복 시 저혈당도 함께 생긴다.') +
    tip('해당과정은 멀쩡하니 젖산은 계속 만들어지는데, 되돌리는 길만 막힌 상황이야.', '핵심 그림'))

add(id='P18', num='18', en_title='Effect of O₂ Supply on Glycolytic Rates', ko_title='산소 공급이 해당과정 속도에 미치는 영향',
    slides='강의 슬라이드 21', level=2,
    en='<p>The regulated steps of glycolysis in intact cells can be identified by studying the catabolism of glucose in whole tissues or organs. For example, the glucose consumption by heart muscle can be measured by artificially circulating blood through an isolated intact heart and measuring the concentration of glucose before and after the blood passes through the heart. If the circulating blood is deoxygenated, heart muscle consumes glucose at a steady rate. When oxygen is added to the blood, the rate of glucose consumption drops dramatically, then is maintained at the new, lower rate. Explain.</p>',
    ko='<p>세포 속 해당과정의 조절 단계는 조직·기관 전체에서 포도당 분해를 연구해 찾을 수 있다. 예를 들어 분리한 심장에 혈액을 인공적으로 순환시키고, 심장을 지나기 전후의 포도당 농도를 재면 심장근의 포도당 소비를 측정할 수 있다. 산소가 없는 혈액을 순환시키면 심장근은 일정한 속도로 포도당을 소비한다. 혈액에 산소를 넣으면 포도당 소비 속도가 급격히 떨어진 뒤 새로운 낮은 속도로 유지된다. 설명하라.</p>',
    answer=chips('<b>파스퇴르 효과</b>', '산소 있음 → 포도당 1개당 ATP가 약 <b>2개 → 30개 이상</b> → 같은 ATP에 필요한 포도당이 훨씬 적음',
                 '늘어난 <b>ATP·시트르산</b>이 PFK-1을 억제 → 해당과정 속도 ↓'),
    explain=key('세포는 “필요한 ATP만큼만” 포도당을 쓴다. 산소가 있으면 포도당 1개에서 뽑는 ATP가 15배 이상 많아진다.') +
    fig(atp_ledger([('무산소: 포도당 → 젖산', 2, C['red']), ('유산소: 포도당 → CO₂ (약 30 ATP)', 8, C['green'])]), '막대 길이는 비율만 표시 (유산소 ≈ 30 ATP)') +
    steps('산소 없음: 해당과정 + 발효만 → 포도당당 2 ATP → ATP 수요를 채우려면 포도당을 빨리 많이 써야 한다.',
          '산소 있음: 피루브산 → 시트르산 회로 → 산화적 인산화 → 포도당당 약 30–32 ATP.',
          '[ATP] ↑·[AMP] ↓·[시트르산] ↑ → <b>PFK-1(와 헥소키나아제) 억제</b> → 포도당 소비가 새 낮은 수준에서 안정.') +
    tip('연비 나쁜 차(무산소)에서 연비 좋은 차(유산소)로 갈아타면, 같은 거리를 가는 데 기름(포도당)이 훨씬 덜 든다.'))

add(id='P19', num='19', en_title='Regulation of PFK-1', ko_title='PFK-1의 조절',
    slides='강의 슬라이드 13 · 15장 슬라이드 15', level=2,
    en=f'''<p>The graph shows the effect of ATP on the allosteric enzyme PFK-1. For a given concentration of fructose 6-phosphate, the PFK-1 activity increases with increasing concentrations of ATP, but there is a point beyond which increasing the concentration of ATP inhibits the enzyme.</p>{img('c14_p19.png', '40%')}
<p><b>a.</b> Explain how ATP can be both a substrate and an inhibitor of PFK-1. How is the enzyme regulated by ATP?<br><b>b.</b> How do ATP levels regulate glycolysis?<br><b>c.</b> The inhibition of PFK-1 by ATP diminishes when the ADP concentration is high, as shown in the graph. What explains this observation?</p>''',
    ko='<p>그래프는 알로스테릭 효소 PFK-1에 대한 ATP의 효과를 보여 준다. 과당 6-인산 농도가 일정할 때, ATP 농도가 늘면 PFK-1 활성이 증가하다가 어느 지점을 넘으면 ATP가 오히려 효소를 억제한다.<br><b>a.</b> ATP가 어떻게 PFK-1의 기질이면서 동시에 억제제일 수 있는가? ATP는 효소를 어떻게 조절하는가?<br><b>b.</b> ATP 농도는 해당과정을 어떻게 조절하는가?<br><b>c.</b> 그래프처럼 ADP 농도가 높으면 ATP의 억제가 약해진다. 이유는?</p>',
    answer=chips('a. ATP 결합 자리가 <b>2곳</b>: 활성 자리(기질, 친화도 높음) + 조절 자리(억제, 친화도 낮음)', 'b. ATP 많음 → PFK-1 억제 → 해당과정 ↓ / ATP 적음 → ↑',
                 'c. ADP(·AMP)는 <b>활성화제</b> → ATP 억제를 풀어 줌'),
    explain=steps('<b>a.</b> ATP 농도가 낮을 땐 친화도가 높은 <b>활성 자리</b>만 채워져 기질로 쓰인다(그래프 왼쪽 상승). 농도가 높아지면 친화도가 낮은 <b>알로스테릭(조절) 자리</b>까지 채워져, 효소 모양이 바뀌고 F6P에 대한 친화도가 떨어진다(오른쪽 하강).',
                  '<b>b.</b> ATP가 충분 = 에너지 넉넉 → PFK-1 속도 ↓ → 해당과정 흐름 ↓ (포도당 절약, 글리코겐으로 저장). ATP가 부족하면 억제가 풀려 해당과정 ↑.',
                  '<b>c.</b> ADP·AMP는 조절 자리에 결합해 ATP의 억제 효과와 반대로 작용(활성화). ADP가 많다 = ATP가 소비되고 있다 = 에너지가 필요하다는 신호 → 억제 해제.') +
    tip('ATP는 PFK-1에게 “재료”이자 “이제 그만!” 신호야. 창고(ATP)가 꽉 차면 공장 라인(해당과정)을 늦추는 자동 센서.', '비유') +
    warn('포유류에서는 ADP보다 <b>AMP</b>가 더 강력한 활성화제이고, <b>과당 2,6-이인산</b>이 가장 강한 활성화제야(15장).', '연결'))

add(id='P20', num='20', en_title='Cellular Glucose Concentration', ko_title='세포 속 포도당 농도',
    slides='강의 슬라이드 10–11', level=2,
    en='<p>Homeostatic mechanisms maintain the concentration of glucose in human blood at about 5 m<span class="sc">M</span>. The concentration of free glucose inside a myocyte is much lower. Why is the concentration so low in the cell? What happens to glucose after entry into the cell? Physicians administer glucose intravenously as a food source in certain clinical situations. Given that the transformation of glucose to glucose 6-phosphate consumes ATP, why not administer intravenous glucose 6-phosphate instead?</p>',
    ko='<p>항상성 기전은 사람 혈중 포도당을 약 5 mM로 유지한다. 근육세포 안의 유리 포도당 농도는 훨씬 낮다. 세포 안 농도가 왜 이렇게 낮은가? 포도당이 세포에 들어간 뒤 어떻게 되는가? 의사는 특정 상황에서 포도당을 정맥 주사로 영양 공급한다. 포도당 → G6P 전환에 ATP가 드는데, 왜 G6P를 대신 주사하지 않는가?</p>',
    answer=chips('들어오자마자 <b>헥소키나아제가 인산화</b>(→ G6P) → 유리 포도당이 거의 없음 → 농도 차 유지로 계속 유입',
                 'G6P는 음전하 인산 때문에 <b>세포막을 통과 못 함</b>(수송체도 없음) → 주사해도 세포가 흡수 불가'),
    explain=key('인산이 붙으면 포도당은 <b>세포 안에 갇힌다</b>. 들어오는 문(GLUT)은 “인산 없는 포도당”만 통과시킨다.') +
    fig(flow(['혈액 포도당 5 mM', '세포 안 포도당 (아주 낮음)', 'G6P (갇힘)'], arrow_labels=['GLUT (촉진 확산)', '헥소키나아제 + ATP'], colors=[C['blue'], C['navy'], C['orange']], box_h=44), '') +
    steps('GLUT는 농도가 높은 곳 → 낮은 곳으로만 운반(촉진 확산). 세포 안 포도당이 계속 G6P로 바뀌어 낮게 유지되니 유입이 멈추지 않는다.',
          'G6P는 해당과정·글리코겐 합성·PPP로 간다. 인산의 음전하 때문에 막을 통과하지 못하고, 그 수송체도 없어 밖으로 새지 않는다.',
          '같은 이유로 혈액에 G6P를 넣으면 세포가 가져갈 방법이 없다 → 영양 공급원이 못 된다. ATP 1개 투자가 “입장료”인 셈.') +
    tip('슬라이드 11 “중간체를 인산화하는 이유”: ① 세포 밖으로 못 나가게 가두기 ② 효소 결합 에너지 제공 ③ 고에너지 인산 화합물 만들기.', '연결'))

add(id='P21', num='21', en_title='Ethanol Production in Yeast', ko_title='효모의 에탄올 생산',
    slides='강의 슬라이드 29 · 13장 표 13-7', level=2,
    en='<p>When grown anaerobically on glucose, yeast (<i>S. cerevisiae</i>) converts pyruvate to acetaldehyde, then reduces acetaldehyde to ethanol using electrons from NADH. Write the equation for the second reaction, and calculate its equilibrium constant at 25 °C, given the standard reduction potentials in Table 13-7.</p>',
    ko='<p>포도당에서 무산소로 자랄 때 효모는 피루브산을 아세트알데하이드로 바꾼 뒤, NADH의 전자로 아세트알데하이드를 에탄올로 환원한다. 두 번째 반응의 반응식을 쓰고, 표 13-7의 표준 환원 전위를 이용해 25 °C에서 평형상수를 계산하라.</p>',
    answer=chips('아세트알데하이드 + NADH + H<sup>+</sup> → 에탄올 + NAD<sup>+</sup>', f'{DE0} = +0.123 V, {G0} = −23.7 kJ/mol', f'{K} ≈ <b>1.4 × 10<sup>4</sup></b>'),
    explain=key('13장 예제 13-3과 똑같은 반응! ΔE′° → ΔG′° → K 순서로 두 번만 변환.') +
    fig(ladder([('NAD⁺/NADH', -0.320), ('아세트알데하이드/에탄올', -0.197)], -0.36, -0.16, hl=('NAD⁺/NADH', '아세트알데하이드/에탄올'),
               flows=[('NAD⁺/NADH', '아세트알데하이드/에탄올', '2e⁻')], height=150), '') +
    steps(f'{DE0} = E′°<sub>받는 쪽</sub> − E′°<sub>주는 쪽</sub> = −0.197 − (−0.320) = <b>+0.123 V</b>',
          f'{G0} = −nF{DE0} = −2 × 96.48 × 0.123 = <b>−23.7 kJ/mol</b>',
          f'{K} = e<sup>23.7/{RT25}</sup> = e<sup>9.57</sup> ≈ <span class="hl">1.4 × 10<sup>4</sup></span> → 에탄올 쪽으로 크게 치우침') +
    tip('효모가 이 반응을 하는 목적도 젖산 발효와 같아: <b>NAD<sup>+</sup> 재생</b>. 에탄올은 그 “부산물”이고 우리가 술로 마시는 것.', '연결'))

add(id='P23', num='23', en_title='Heat from Fermentations', ko_title='발효에서 나오는 열',
    slides='강의 슬라이드 27–29', level=1,
    en='<p>Large-scale industrial fermenters generally require constant, vigorous cooling. Why?</p>',
    ko='<p>대규모 산업용 발효조는 보통 계속해서 강하게 냉각해 주어야 한다. 왜 그런가?</p>',
    answer=chips('발효는 <b>발열(exergonic)</b> 과정 — 방출된 자유에너지 중 ATP로 저장되는 건 일부뿐, <b>나머지는 열</b>', '식히지 않으면 온도가 올라 미생물·효소가 죽거나 변성'),
    explain=key('에너지는 사라지지 않는다(열역학 제1법칙). ATP로 못 잡은 에너지는 <b>열</b>이 된다.') +
    steps('포도당 → 2 에탄올 + 2CO<sub>2</sub>(또는 2 젖산)은 큰 음의 ΔG를 가진 반응.',
          '그중 ATP 2개(각 약 30.5 kJ/mol)로 저장되는 건 일부이고, 나머지는 열로 방출된다.',
          '수천 리터의 발효조에서 수많은 미생물이 동시에 이렇게 하면 열이 계속 쌓임 → 적정 온도 유지를 위해 냉각 필수.') +
    tip('퇴비 더미 속이 뜨끈한 것, 막걸리 발효 항아리가 따뜻해지는 것도 같은 원리야.', '생활 속'))

add(id='P24', num='24', en_title='Fermentation to Produce Soy Sauce', ko_title='간장을 만드는 발효',
    slides='강의 슬라이드 28–30', level=1,
    en='<p>Soy sauce preparation involves fermenting a salted mixture of soybeans and wheat with several microorganisms, including yeast, over a period of 8 to 12 months. The resulting sauce (after solids are removed) is rich in lactate and ethanol. How are these two compounds produced? To prevent the soy sauce from having a strong vinegary taste (vinegar is dilute acetic acid), oxygen must be kept out of the fermentation tank. Why?</p>',
    ko='<p>간장은 소금을 넣은 콩과 밀 혼합물을 효모를 포함한 여러 미생물로 8–12개월 동안 발효해 만든다. 완성된 간장(고형물 제거 후)에는 젖산과 에탄올이 풍부하다. 이 두 물질은 어떻게 만들어지는가? 간장이 강한 식초 맛(식초 = 묽은 아세트산)을 내지 않게 하려면 발효조에 산소가 들어가지 않게 해야 한다. 왜 그런가?</p>',
    answer=chips('밀의 녹말 → 포도당 → 해당과정 → 피루브산', '젖산균: 피루브산 → <b>젖산</b> / 효모: 피루브산 → <b>에탄올 + CO<sub>2</sub></b>',
                 '산소가 있으면 <b>호기성 세균(아세트산균)</b>이 에탄올을 아세트산으로 산화 → 식초 맛'),
    explain=fig(flow(['포도당', '피루브산', '젖산 (젖산균)|에탄올 (효모)'], arrow_labels=['해당과정', '발효 (NAD⁺ 재생)'], box_h=46), '두 종류의 미생물이 두 가지 발효를 한다') +
    steps('콩·밀의 녹말·당이 분해되어 포도당이 되고, 미생물이 해당과정으로 피루브산을 만든다.',
          '산소가 없으니 NAD<sup>+</sup>를 재생해야 한다: 젖산균은 LDH로 젖산, 효모는 탈카복실화 + ADH로 에탄올.',
          '산소가 있으면 아세트산균(<i>Acetobacter</i>)이 에탄올 → 아세트알데하이드 → <b>아세트산</b>으로 산화한다(산소가 전자를 받아야 가능) → 식초.') +
    tip('막걸리를 뚜껑 열어 오래 두면 시큼해지는 것 = 공기 중 산소 + 아세트산균이 알코올을 식초로 바꾼 것.', '생활 속'))

add(id='P25', num='25', en_title='Glucogenic Substrates', ko_title='포도당을 만들 수 있는(당원성) 물질',
    slides='강의 슬라이드 34, 39–40', level=2,
    en='''<p>A common procedure for determining the effectiveness of compounds as precursors of glucose in mammals is to starve the animal until the liver glycogen stores are depleted and then administer the compound in question. A substrate that leads to a <i>net</i> increase in liver glycogen is termed glucogenic, because it must first be converted to glucose 6-phosphate. Show by means of known enzymatic reactions which of these substances are glucogenic:</p>
<p class="c">(a) succinate &nbsp; (b) glycerol &nbsp; (c) acetyl-CoA &nbsp; (d) pyruvate &nbsp; (e) butyrate</p>
<p class="small">※ 이 PDF에는 물질 목록 그림이 빠져 있어, 교과서의 목록(a–e)으로 보충했어.</p>''',
    ko='<p>포유류에서 어떤 화합물이 포도당의 전구체로 얼마나 효과적인지 알아보는 흔한 방법은, 간 글리코겐이 고갈될 때까지 동물을 굶긴 뒤 그 화합물을 투여하는 것이다. 간 글리코겐을 <i>알짜로</i> 증가시키는 물질은 먼저 G6P로 바뀌어야 하므로 당원성(glucogenic)이라 한다. 알려진 효소 반응으로 다음 중 어느 것이 당원성인지 보여라: (a) 숙신산 (b) 글리세롤 (c) 아세틸-CoA (d) 피루브산 (e) 뷰티르산</p>',
    answer=chips('당원성 ○: <b>(a) 숙신산, (b) 글리세롤, (d) 피루브산</b>', '당원성 ✕: <b>(c) 아세틸-CoA, (e) 뷰티르산</b>'),
    explain=key('포도당이 되려면 <b>옥살로아세트산(OAA)이나 DHAP·피루브산</b>에 “알짜로 탄소를 보탤” 수 있어야 한다. 아세틸-CoA(C2)는 못 한다.') +
    table(['물질', '경로', '결론'],
          [['(a) 숙신산', '→ 푸마르산 → 말산 → <b>OAA</b> → PEP(PEPCK) → … 포도당', '○'],
           ['(b) 글리세롤', '글리세롤 키나아제 → 글리세롤 3-인산 → <b>DHAP</b> → 당신생', '○'],
           ['(c) 아세틸-CoA', 'PDH는 비가역 → 피루브산 불가. TCA에 들어가도 C2 들어가고 CO<sub>2</sub> 2개 나감 → 알짜 0', '✕'],
           ['(d) 피루브산', '피루브산 카복실화효소 → <b>OAA</b> → PEP → … 포도당', '○'],
           ['(e) 뷰티르산', 'β-산화 → 아세틸-CoA 2개 → (c)와 같은 이유', '✕']], cls='left') +
    tip('그래서 동물은 <b>지방산으로 포도당을 만들 수 없다</b>(식물은 글리옥실산 회로로 가능 — 16장). 지방의 글리세롤 부분만 포도당이 될 수 있어.', '연결'))

add(id='P27', num='27', en_title='Energy Cost of a Cycle of Glycolysis and Gluconeogenesis', ko_title='해당과정–당신생 한 바퀴의 에너지 비용',
    slides='강의 슬라이드 37', level=1,
    en='<p>What is the cost (in ATP equivalents) of transforming glucose to pyruvate via glycolysis and back again to glucose via gluconeogenesis?</p>',
    ko='<p>포도당을 해당과정으로 피루브산으로 바꾼 뒤, 당신생으로 다시 포도당으로 되돌리는 데 드는 비용은 (ATP 당량으로) 얼마인가?</p>',
    answer=chips('한 바퀴 비용 = <b>ATP 4개</b> 당량 (6 소비 − 2 생산)'),
    explain=fig(atp_ledger([('해당과정: 포도당 → 2 피루브산', 2, C['green']), ('당신생: 2 피루브산 → 포도당 (4ATP + 2GTP)', -6, C['red']), ('한 바퀴 합계', -4, C['orange'])]), '') +
    steps('해당과정 순수익: <b>+2 ATP</b> (NADH 2개 생성).',
          '당신생: 피루브산 카복실화효소 2 ATP + PEPCK 2 GTP + PGK 역반응 2 ATP = <b>6</b> (NADH 2개 소비).',
          'NADH는 서로 상쇄. 합계 −6 + 2 = <span class="hl">−4 ATP 당량</span>(GTP = ATP 1개로 계산).') +
    tip('이렇게 비싼 “역주행”을 두 경로가 동시에 돌면 에너지만 버리는 <b>헛된 회로</b>(futile cycle)가 돼. 그래서 두 경로는 서로 반대로(상반) 조절된다(15장).', '연결'))

add(id='P28', num='28', en_title='Relationship between Gluconeogenesis and Glycolysis', ko_title='당신생과 해당과정의 관계',
    slides='강의 슬라이드 35–37', level=1,
    en='<p>Why is it important that gluconeogenesis is not the exact reversal of glycolysis?</p>',
    ko='<p>당신생이 해당과정의 정확한 역반응이 아니라는 것이 왜 중요한가?</p>',
    answer=chips('① <b>열역학</b>: 해당과정의 3단계는 크게 음수 ΔG(비가역) → 그대로 거꾸로는 못 감', '② <b>조절</b>: 다른 효소를 쓰면 두 경로를 <b>따로(상반) 조절</b> 가능 → 헛된 회로 방지'),
    explain=key('같은 도로를 양방향으로 쓰면 신호등을 따로 달 수 없다. 비가역 구간 3곳에 <b>전용 우회로</b>를 만든 것.') +
    table(['해당과정 (비가역)', '당신생 우회 효소'],
          [['① 헥소키나아제 (ΔG −33)', 'G6Pase'], ['③ PFK-1 (ΔG −22)', 'FBPase-1'], ['⑩ 피루브산 키나아제 (ΔG −17)', '피루브산 카복실화효소 + PEPCK']]) +
    steps('세포 속 ΔG가 크게 음수인 반응을 거꾸로 돌리려면 엄청난 에너지·농도 차가 필요 → 불가능. 다른 반응(가수분해, ATP+GTP 사용)으로 우회하면 당신생도 전체가 음수 ΔG(약 −16 kJ/mol)가 된다.',
          '우회 효소들은 각각 다른 신호(ATP·AMP·과당 2,6-이인산·아세틸-CoA·호르몬)로 반대로 조절된다 → 포도당이 필요할 땐 당신생만, 에너지가 필요할 땐 해당과정만.') +
    tip('해당과정 ΔG ≈ −63, 당신생 ΔG ≈ −16 kJ/mol(세포 속): <b>둘 다 내리막</b>이라 각자 한 방향으로 확실히 흐른다.', '숫자'))

add(id='P29', num='29', en_title='Energetics of the Pyruvate Kinase Reaction', ko_title='피루브산 키나아제 반응의 에너지',
    slides='강의 슬라이드 36–38', level=2,
    en='<p>Explain in bioenergetic terms how the conversion of pyruvate to phosphoenolpyruvate in gluconeogenesis overcomes the large, negative, standard free-energy change of the pyruvate kinase reaction in glycolysis.</p>',
    ko='<p>당신생에서 피루브산 → PEP 전환이, 해당과정 피루브산 키나아제 반응의 크고 음수인 표준 자유에너지 변화를 어떻게 극복하는지 생체에너지론 관점에서 설명하라.</p>',
    answer=chips('두 단계로 우회하며 <b>고에너지 인산 2개(ATP + GTP)</b>를 쓴다', '피루브산 카복실화효소(ATP) → OAA → PEPCK(GTP) → PEP', f'전체 {G0} ≈ +0.9, 세포 속 ΔG ≈ <b>−25 kJ/mol</b>'),
    explain=key('PEP 1개(아주 높은 에너지, −61.9)를 만들려면 ATP 1개로는 부족 → <b>ATP + GTP 두 개</b>를 “지불”한다.') +
    fig(flow(['피루브산', '옥살로아세트산', 'PEP'], arrow_labels=['+HCO₃⁻, ATP (비오틴)', 'GTP, −CO₂'], colors=[C['navy'], C['orange'], C['green']]), '카복실화 → 탈카복실화: CO₂는 붙었다가 다시 떨어진다') +
    steps('해당과정: PEP + ADP → 피루브산 + ATP, ΔG′° = −31.4 → 거꾸로는 +31.4 (ATP 1개로 불가능).',
          '당신생: ① 피루브산 + HCO<sub>3</sub><sup>−</sup> + ATP → OAA ② OAA + GTP → PEP + CO<sub>2</sub> + GDP. 합계 ΔG′° = <b>+0.9 kJ/mol</b>.',
          '세포 속에서는 PEP가 다음 반응으로 곧 소비되어 농도가 낮으므로 ΔG ≈ <b>−25 kJ/mol</b> → 사실상 비가역으로 진행.') +
    tip('붙였다 떼는 CO<sub>2</sub>는 “지렛대”야. 탈카복실화가 전자를 재배열시켜 GTP의 인산을 받기 쉽게 만든다. 지방산 합성(21장)에서도 같은 트릭이 나와.', '포인트'))

add(id='P30', num='30', en_title='Muscle Wasting in Starvation', ko_title='굶을 때 근육이 줄어드는 이유',
    slides='강의 슬라이드 34, 39', level=1,
    en='<p>One consequence of starvation is a reduction in muscle mass. What happens to the muscle proteins?</p>',
    ko='<p>굶주림의 결과 중 하나는 근육량 감소다. 근육 단백질은 어떻게 되는가?</p>',
    answer=chips('근육 단백질 → <b>아미노산</b>으로 분해', '당원성 아미노산(알라닌·글루타민 등) → 간 → <b>당신생</b> → 뇌·적혈구용 포도당'),
    explain=key('굶으면 간 글리코겐은 하루 안에 바닥. 그 뒤 뇌에 줄 포도당의 원료로 <b>근육 단백질</b>을 헐어 쓴다.') +
    fig(flow(['근육 단백질', '아미노산 (알라닌 등)', '피루브산·OAA', '포도당 (간)'], arrow_labels=['분해', '아미노기 제거', '당신생']), '') +
    steps('뇌와 적혈구는 포도당이 꼭 필요(적혈구는 포도당만 사용).',
          '지방산은 포도당으로 바꿀 수 없으므로(문제 25), 탄소 공급원은 글리세롤·젖산·<b>아미노산</b>뿐.',
          '근육 단백질이 아미노산으로 분해 → 혈액으로 → 간에서 아미노기는 요소로, 탄소 뼈대는 피루브산·TCA 중간체 → 포도당.') +
    tip('단식이 길어지면 간이 케톤체를 만들어 뇌가 그걸 연료로 쓰기 시작하면서 근육 분해 속도가 줄어든다(17장).', '연결'))

add(id='P31', num='31', en_title='Effect of Phloridzin on Carbohydrate Metabolism', ko_title='플로리진이 탄수화물 대사에 미치는 영향',
    slides='강의 슬라이드 38–39', level=2,
    en='<p>Phloridzin, a toxic glycoside from the bark of the pear tree, blocks the normal reabsorption of glucose from the kidney tubule, thus causing blood glucose to be almost completely excreted in the urine. In an experiment, rats fed phloridzin and sodium succinate excreted about 0.5 mol of glucose (made by gluconeogenesis) for every 1 mol of sodium succinate ingested. How do rats transform the succinate to glucose? Explain the stoichiometry.</p>',
    ko='<p>배나무 껍질의 독성 배당체인 플로리진은 신세관의 포도당 재흡수를 막아 혈중 포도당을 거의 전부 소변으로 배출시킨다. 실험에서 플로리진과 숙신산 나트륨을 먹인 쥐는 섭취한 숙신산 1 mol당 약 0.5 mol의 포도당(당신생으로 만든 것)을 배출했다. 쥐는 숙신산을 어떻게 포도당으로 바꾸는가? 화학량론(0.5 : 1)을 설명하라.</p>',
    answer=chips('숙신산 → 푸마르산 → 말산 → <b>OAA</b> → (PEPCK, −CO<sub>2</sub>) → <b>PEP</b> → … → 포도당', '포도당 1개 = PEP 2개 = 숙신산 2개 → <b>0.5 mol 포도당 / 1 mol 숙신산</b>'),
    explain=key('숙신산 1개는 <b>PEP 1개</b>(C3)가 된다. 포도당(C6)은 PEP 2개가 필요.') +
    fig(vflow(['숙신산 (C4)', '푸마르산 → 말산', '옥살로아세트산 (C4)', 'PEP (C3) + CO₂', '½ 포도당 (C6 ÷ 2)'], notes=['숙신산 탈수소효소', 'TCA 회로 효소', 'PEPCK (GTP)', '당신생 × (PEP 2개 → 포도당 1개)'],
              colors=[C['orange'], C['navy'], C['navy'], C['green'], C['green']], box_h=26, gap=18), '') +
    steps('숙신산은 시트르산 회로의 뒤쪽 반응(숙신산 탈수소효소 → 푸마레이스 → 말산 탈수소효소)으로 OAA가 된다.',
          'OAA → PEP(PEPCK)에서 탄소 1개가 CO<sub>2</sub>로 빠진다: C4 → C3.',
          'PEP 2개 → 당신생 → 포도당 1개. 따라서 숙신산 2 mol → 포도당 1 mol = <span class="hl">0.5 : 1</span>.') +
    tip('플로리진 덕분에 만들어진 포도당이 모두 소변으로 나오니까, 소변 포도당을 재면 당신생 양을 바로 측정할 수 있는 영리한 실험이야. (SGLT2 억제제 당뇨약의 원조!)', '재미'))

add(id='P32', num='32', en_title='Excess O₂ Uptake during Gluconeogenesis', ko_title='당신생 중의 초과 산소 소비',
    slides='강의 슬라이드 37', level=2,
    en='<p>The conversion of lactate to glucose in the liver requires the input of 6 mol of ATP for every mol of glucose produced. Investigators can monitor the extent of this process in a rat liver preparation by administering [<sup>14</sup>C]lactate and measuring the amount of [<sup>14</sup>C]glucose produced. Because the stoichiometry of O<sub>2</sub> consumption and ATP production is known (about 5 ATP per O<sub>2</sub>), investigators can predict the extra O<sub>2</sub> consumption above the normal rate after administering a given amount of lactate. However, when they actually measure extra O<sub>2</sub> used in the synthesis of glucose from lactate, it is always higher than what the stoichiometric relationships predict. Suggest a possible explanation for this observation.</p>',
    ko='<p>간에서 젖산 → 포도당 전환에는 포도당 1 mol당 ATP 6 mol이 필요하다. 쥐 간 표본에 [<sup>14</sup>C]젖산을 주고 [<sup>14</sup>C]포도당 양을 재면 이 과정을 추적할 수 있다. O<sub>2</sub> 소비와 ATP 생산의 비(O<sub>2</sub> 1개당 ATP 약 5개)를 알기 때문에, 젖산 투여 후 늘어날 O<sub>2</sub> 소비를 예측할 수 있다. 그런데 실제로 잰 초과 O<sub>2</sub> 소비는 항상 예측보다 많다. 가능한 설명을 제안하라.</p>',
    answer=chips('계산에 안 들어간 ATP 소비가 있다:', '① 해당과정과 당신생이 동시에 돌아 생기는 <b>헛된 회로</b>(기질 회로)', '② 수송 비용(피루브산·말산·P<sub>i</sub> 미토콘드리아 출입) 등', '③ 실제 ATP/O 비가 5보다 낮음(양성자 누출)'),
    explain=key('“포도당 1개 = ATP 6개”는 <b>이상적인 최소값</b>. 실제 세포에선 새는 곳이 있다.') +
    steps('<b>헛된 회로</b>: 간에서 PFK-1/FBPase-1, 피루브산 키나아제/(PC + PEPCK)가 완전히 꺼지지 않아 일부가 되돌아간다 → 포도당은 안 늘고 ATP만 소모.',
          '<b>운반 비용</b>: 피루브산을 미토콘드리아로 넣고 말산/PEP를 내보내는 수송도 양성자 기울기(에너지)를 쓴다.',
          '<b>효율</b>: 산화적 인산화의 실제 ATP/O 비는 이론값보다 낮을 수 있다(양성자 누출).',
          '그 외 새 포도당을 저장·내보내는 과정 등도 에너지를 쓴다 → 측정 O<sub>2</sub> &gt; 예측 O<sub>2</sub>.') +
    tip('가계부 예산(6 ATP)보다 실제 지출이 늘 많은 이유: 수수료·배송비(수송)와 새는 돈(헛된 회로) 때문.', '비유'))

add(id='P33', num='33', en_title='Role of the Pentose Phosphate Pathway', ko_title='오탄당 인산 경로의 역할',
    slides='강의 슬라이드 41–47', level=2,
    en='<p>If the oxidation of glucose 6-phosphate via the pentose phosphate pathway were being used primarily to generate NADPH for biosynthesis, the other product, ribose 5-phosphate, would accumulate. What problems might this cause?</p>',
    ko='<p>G6P를 오탄당 인산 경로로 산화하는 목적이 주로 생합성용 NADPH를 만드는 것이라면, 다른 생성물인 리보스 5-인산이 쌓일 것이다. 이것은 어떤 문제를 일으킬 수 있는가?</p>',
    answer=chips('리보스 5-인산이 쌓이면 <b>인산·탄소가 묶여</b> 버리고 G6P가 고갈 → 대사 불균형', '실제로는 <b>비산화 단계</b>(트랜스케톨레이스·트랜스알돌레이스)가 남는 리보스 5-P를 <b>F6P·G3P로 재활용</b>해 문제를 막는다'),
    explain=key('NADPH만 필요하고 리보스는 필요 없을 때: 5탄당 6개 → 6탄당 5개로 “재조립”해서 다시 G6P로 돌린다.') +
    fig(flow(['G6P', '리보스 5-P + NADPH', 'F6P · G3P', 'G6P (재사용)'], arrow_labels=['산화 단계', '비산화 단계', '당신생 반응'], colors=[C['navy'], C['orange'], C['green'], C['navy']], box_h=44), 'NADPH를 계속 뽑아 쓰는 순환') +
    steps('<b>문제</b>: 리보스 5-인산만 쌓이면 ① 세포 속 인산(P<sub>i</sub>)과 탄소가 쓸모없는 형태로 묶이고 ② G6P(해당과정·글리코겐 원료)가 줄며 ③ 뉴클레오타이드 합성 균형도 깨질 수 있다.',
          '<b>해결</b>: 비산화 단계가 5C × 6 → 6C × 5로 탄소를 재배열 → F6P는 G6P로 되돌아가 다시 산화 단계로 → 결국 G6P를 CO<sub>2</sub>로 태우며 NADPH만 대량 생산할 수 있다.',
          '지방 합성이 활발한 지방세포·간, 항산화가 중요한 적혈구가 이런 방식으로 NADPH를 얻는다.') +
    tip('레고 블록(탄소)을 5칸짜리로 잘라 놓았는데 5칸이 필요 없으면, 다시 6칸짜리로 재조립해서 처음부터 또 쓰는 거야.', '비유'))

# ★★★ (제외) — 가이드 페이지의 제외 목록용
for _n in ('11', '22', '26'):
    ALL_ITEMS.append(dict(id='P' + _n, num=_n, level=3, kind='PROBLEM'))
ALL_ITEMS.sort(key=lambda i: (i['kind'] == 'PROBLEM', int(i['num'].split('-')[-1])))
