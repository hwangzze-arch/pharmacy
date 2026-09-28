# -*- coding: utf-8 -*-
from helpers import *
from content_a import phos_ladder

ITEMS = []


def add(**kw):
    kw.setdefault('section', '연습문제')
    ITEMS.append(kw)


REDOX = [('½O₂/H₂O', 0.816), ('시토크롬 c', 0.254), ('유비퀴논/유비퀴놀', 0.045), ('푸마르산/숙신산', 0.031),
         ('옥살로아세트산/말산', -0.166), ('피루브산/젖산', -0.185), ('아세트알데하이드/에탄올', -0.197),
         ('NAD⁺/NADH', -0.320), ('NADP⁺/NADPH', -0.324), ('아세토아세트산/β-하이드록시뷰티르산', -0.346),
         ('α-케토글루타르산+CO₂/아이소시트르산', -0.38)]


def R(*names):
    return [e for e in REDOX if e[0] in names]


# ---------------- drawings ----------------
def atp_chain():
    W, H = 520, 150
    b = ''
    b += f'<rect x="20" y="52" width="120" height="40" rx="8" fill="#e0e7ff" stroke="#6366f1"/>' + T(80, 77, '아데노신', 12, C['navy'], weight=700)
    xs = [190, 290, 390]
    labs = [('α', '#94a3b8'), ('β', C['blue']), ('γ', C['red'])]
    b += f'<line x1="140" y1="72" x2="{xs[-1]}" y2="72" stroke="{C["ink"]}" stroke-width="2"/>'
    for x, (g, col) in zip(xs, labs):
        b += f'<circle cx="{x}" cy="72" r="22" fill="white" stroke="{col}" stroke-width="3"/>' + T(x, 77, 'P', 14, col, weight=900)
        b += T(x, 38, g, 15, col, weight=900, family='Noto Serif')
    b += T(390, 118, '끝 인산: 가장 자주 떨어지고', 10.5, C['red'], weight=700)
    b += T(390, 133, '다시 붙음 → 교체 빠름', 10.5, C['red'], weight=700)
    b += T(290, 118, 'ADP가 되어도', 10.5, C['blue'], weight=700)
    b += T(290, 133, '그대로 남음', 10.5, C['blue'], weight=700)
    b += arrowdef('ac', C['red'])
    b += f'<path d="M412,60 C450,30 480,40 495,70" fill="none" stroke="{C["red"]}" stroke-width="2" marker-end="url(#ac)"/>'
    b += T(478, 94, 'Pᵢ', 13, C['red'], weight=700)
    return svg(W, H, b)


def atp_cycle():
    W, H = 520, 200
    b = arrowdef('cy1', C['orange']) + arrowdef('cy2', C['blue'])
    b += f'<rect x="200" y="20" width="120" height="44" rx="12" fill="#fff7ed" stroke="{C["orange"]}" stroke-width="2"/>' + T(260, 48, 'ATP', 16, C['orange'], weight=900)
    b += f'<rect x="185" y="140" width="150" height="44" rx="12" fill="#eff6ff" stroke="{C["blue"]}" stroke-width="2"/>' + T(260, 168, 'ADP + Pᵢ', 16, C['blue'], weight=900)
    b += f'<path d="M330,44 C420,50 420,150 340,160" fill="none" stroke="{C["orange"]}" stroke-width="3" marker-end="url(#cy1)"/>'
    b += f'<path d="M180,160 C100,150 100,50 190,44" fill="none" stroke="{C["blue"]}" stroke-width="3" marker-end="url(#cy2)"/>'
    b += T(430, 92, '에너지 사용', 11.5, C['orange'], 'start', 700) + T(430, 108, '근육 수축·합성·수송', 10.5, C['orange'], 'start')
    b += T(90, 92, '에너지 충전', 11.5, C['blue'], 'end', 700) + T(90, 108, '음식(연료) 산화', 10.5, C['blue'], 'end')
    b += T(260, 108, '하루 수백 번 이상 회전', 11, C['gray'], weight=700)
    return svg(W, H, b)


def pump_svg():
    W, H = 520, 190
    b = arrowdef('pu', C['red'])
    b += '<rect x="20" y="20" width="200" height="150" rx="14" fill="#f0fdf4" stroke="#86efac"/>'
    b += '<rect x="300" y="20" width="200" height="150" rx="14" fill="#fef2f2" stroke="#fca5a5"/>'
    b += '<rect x="236" y="14" width="48" height="162" rx="10" fill="#fde68a" stroke="#f59e0b"/>'
    b += T(120, 46, '세포질 (pH 7)', 12.5, C['green'], weight=900) + T(120, 66, '[H⁺] = 10⁻⁷ M', 11, C['green'], family='JetBrains Mono')
    b += T(400, 46, '위 속 (pH 1)', 12.5, C['red'], weight=900) + T(400, 66, '[H⁺] = 10⁻¹ M', 11, C['red'], family='JetBrains Mono')
    b += T(260, 100, '펌프', 11, '#92400e', weight=900)
    for i, y in enumerate([110, 140]):
        b += T(80 + i * 60, y, 'H⁺', 11, C['green'], weight=700)
    for i in range(6):
        b += T(330 + (i % 3) * 55, 110 + (i // 3) * 30, 'H⁺', 11, C['red'], weight=700)
    b += f'<path d="M150,125 C220,125 300,95 330,85" fill="none" stroke="{C["red"]}" stroke-width="2.5" marker-end="url(#pu)"/>'
    b += T(260, 160, 'ATP → ADP + Pᵢ', 10.5, '#92400e', weight=700)
    b += T(260, 188, '농도가 100만 배 높은 쪽으로 밀어 올리기 = 오르막', 11, C['red'], weight=700)
    return svg(W, H + 6, b)


def carbon_ladder():
    W, H = 520, 210
    rows = [('d', 'R–CH₂–CH₃', '메틸 (알케인)', 7, C['blue']), ('a', 'R–CH₂–CH₂–OH', '알코올', 5, '#0891b2'),
            ('c', 'R–CH₂–CHO', '알데하이드', 3, C['amber']), ('b', 'R–CH₂–COO⁻', '카복실산', 1, C['red'])]
    b = ''
    for i, (k, f, n, e, col) in enumerate(rows):
        y = 18 + i * 46
        b += f'<rect x="10" y="{y}" width="30" height="32" rx="8" fill="{col}"/>' + T(25, y + 22, k, 14, 'white', weight=900)
        b += T(52, y + 21, f, 13, C['ink'], 'start', 700, family='Noto Serif')
        b += T(200, y + 21, n, 11, C['gray'], 'start')
        b += f'<rect x="290" y="{y+6}" width="{e*26}" height="20" rx="5" fill="{col}" opacity=".85"/>'
        b += T(290 + e * 26 + 8, y + 21, f'끝 탄소가 가진 전자 {e}개', 10.5, col, 'start', 700)
    b += T(10, H - 2, '위 = 가장 환원(H 많음, 에너지 많음)  →  아래 = 가장 산화(O 많음)', 10.5, C['gray'], 'start', 700)
    return svg(W, H + 6, b)


def battery_svg():
    W, H = 520, 200
    b = arrowdef('bt', C['orange'])
    for x, top, bot, col, fill in [(40, '피루브산 / 젖산', 'E′° = −0.185 V', C['blue'], '#eff6ff'), (320, '푸마르산 / 숙신산', 'E′° = +0.031 V', C['red'], '#fef2f2')]:
        b += f'<path d="M{x},70 L{x},170 Q{x},185 {x+15},185 L{x+145},185 Q{x+160},185 {x+160},170 L{x+160},70" fill="{fill}" stroke="{top and col}" stroke-width="2"/>'
        b += T(x + 80, 132, top, 11.5, col, weight=900) + T(x + 80, 150, bot, 10.5, col, family='JetBrains Mono')
        b += f'<rect x="{x+74}" y="60" width="12" height="60" fill="#475569"/>'
    b += f'<path d="M120,60 L120,25 L400,25 L400,60" fill="none" stroke="#475569" stroke-width="2"/>'
    b += f'<line x1="170" y1="25" x2="350" y2="25" stroke="{C["orange"]}" stroke-width="3" marker-end="url(#bt)"/>'
    b += T(260, 17, 'e⁻ 흐름 →', 12, C['orange'], weight=900)
    b += T(120, 205, '젖산 → 피루브산 (전자 내놓음)', 10.5, C['blue'], weight=700)
    b += T(400, 205, '푸마르산 → 숙신산 (전자 받음)', 10.5, C['red'], weight=700)
    return svg(W, H + 12, b)


def e_line():
    W, H = 520, 110
    L, Rr = 40, 480
    lo, hi = -0.36, -0.28
    def X(v): return L + (v - lo) / (hi - lo) * (Rr - L)
    b = arrowdef('el', C['gray'])
    b += f'<line x1="{L}" y1="60" x2="{Rr}" y2="60" stroke="{C["gray"]}" stroke-width="1.5" marker-end="url(#el)"/>'
    for v in [-0.36, -0.34, -0.32, -0.30, -0.28]:
        b += f'<line x1="{X(v)}" y1="56" x2="{X(v)}" y2="64" stroke="{C["gray"]}"/>' + T(X(v), 80, f'{v:.2f}'.replace('-', '−'), 10, C['gray'], family='JetBrains Mono')
    for v, lab, col in [(-0.350, 'a  NAD⁺:NADH = 1:10', C['blue']), (-0.320, 'b  1:1 (= E′°)', C['ink']), (-0.290, 'c  10:1', C['red'])]:
        b += f'<circle cx="{X(v)}" cy="60" r="7" fill="{col}" stroke="white" stroke-width="2"/>' + T(X(v), 40, lab, 11, col, weight=700)
    b += T(Rr, 100, 'E (V) — 산화형(NAD⁺)이 많을수록 오른쪽(+)', 10.5, C['gray'], 'end')
    return svg(W, H, b)


# =====================================================================
add(id='P20', kind='PROBLEM', num='20',
    en_title='Effect of Structure on Group Transfer Potential', ko_title='구조가 작용기 전달 전위에 미치는 영향', slides='강의 슬라이드 30–31', level=1,
    en='<p>Some invertebrates contain phosphoarginine. Is the standard free energy of hydrolysis of this molecule more similar to that of glucose 6-phosphate or of ATP? Explain your answer.</p>',
    ko='<p>일부 무척추동물은 포스포아르지닌(phosphoarginine)을 가지고 있다. 이 분자의 가수분해 표준 자유에너지는 포도당 6-인산과 ATP 중 어느 쪽과 더 비슷한가? 이유를 설명하라.</p>',
    blank=35,
    answer=chips('<b>ATP와 비슷</b>하다 (포스포크레아틴과 같은 고에너지 인산 화합물)'),
    explain=key('포스포아르지닌은 척추동물 근육의 <b>포스포크레아틴</b>과 쌍둥이 구조야. 둘 다 인산이 <b>구아니디노기의 N</b>에 붙어 있다(P–N 결합).') +
    steps('<b>포도당 6-인산</b>: 인산이 당의 O에 붙은 평범한 <b>에스터</b>(P–O–C). 떼어내도 생성물(포도당)이 특별히 안정해지지 않음 → −13.8 kJ/mol (저에너지).',
          '<b>포스포아르지닌</b>: 인산을 떼면 아르지닌의 구아니디늄기(–NH–C(=NH<sub>2</sub><sup>+</sup>)–NH<sub>2</sub>)가 생기는데, 양전하가 N 세 개에 골고루 퍼지는 <b>공명 안정화</b>가 크게 일어난다 → 생성물이 훨씬 편해짐 → 가수분해 ΔG′°가 크게 음수.',
          '그래서 포스포크레아틴처럼 <b>고에너지 인산 화합물</b>에 속한다(문헌값 약 −32 kJ/mol로 ATP의 −30.5와 거의 같다). 무척추동물에서는 근육의 “ATP 비상 저장소(포스파젠)” 역할을 한다.') +
    fig(phos_ladder(hl=('PCr', 'ATP', 'G6P'), height=280), '포스포아르지닌은 PCr과 같은 “고에너지 구역(점선 위)”에 들어간다') +
    tip('ATP를 “에너지 화폐”라고 하면, 포스포크레아틴·포스포아르지닌은 “비상금 통장”. 둘 다 ATP보다 살짝 위에 있어서 ADP에 인산을 줘 ATP를 바로 다시 만들 수 있어.', '직관'))

add(id='P21', kind='PROBLEM', num='21',
    en_title='Polyphosphate as a Possible Energy Source', ko_title='폴리인산은 에너지원이 될 수 있을까?', slides='강의 슬라이드 14, 31', level=2,
    en='<p>The standard free energy of hydrolysis of inorganic polyphosphate (polyP) is about −20 kJ/mol for each P<sub>i</sub> released. We calculated in Worked Example 13-2 that, in a cell, it takes about 50 kJ/mol of energy to synthesize ATP from ADP and P<sub>i</sub>. Is it feasible for a cell to use polyphosphate to synthesize ATP from ADP? Explain your answer.</p>',
    ko='<p>무기 폴리인산(polyP)의 가수분해 표준 자유에너지는 P<sub>i</sub> 하나가 떨어질 때마다 약 −20 kJ/mol이다. 예제 13-2에서 세포 속에서 ADP와 P<sub>i</sub>로 ATP를 합성하려면 약 50 kJ/mol이 필요하다고 계산했다. 세포가 폴리인산을 이용해 ADP로부터 ATP를 합성하는 것이 가능한가? 설명하라.</p>',
    blank=40,
    answer=chips('인산 1개(−20)로 ATP 1개(+50)를 만들기엔 <b>에너지가 모자란다</b> → 단순 계산으로는 <b>어렵다</b>', '단, 농도 조건(polyP 매우 많음, ATP/ADP 낮음)이 받쳐 주면 가능 — 실제로 일부 세균은 이렇게 한다'),
    explain=key('에너지 장부: 들어오는 돈(−20) &lt; 나가는 돈(+50). 한 번의 인산 전달로는 적자!') +
    align([('', 'polyP<sub>n</sub> + H<sub>2</sub>O → polyP<sub>n−1</sub> + P<sub>i</sub>', '−20'),
           ('', 'ADP + P<sub>i</sub> → ATP + H<sub>2</sub>O (세포 속)', '+50'),
           ('합', 'polyP<sub>n</sub> + ADP → polyP<sub>n−1</sub> + ATP', '≈ +30 kJ/mol')], cls='sum') +
    steps('합이 양수(+) → 세포의 보통 조건에서는 저절로 ATP 쪽으로 가지 않는다. 표준 조건에서 비교해도 −20 + 30.5 = <b>+10.5 kJ/mol</b>로 여전히 불리.',
          '하지만 ΔG는 농도에 따라 바뀐다(ΔG = ΔG′° + RT ln Q). polyP가 아주 많고 ADP가 많고 ATP가 적은 상황(예: 에너지 부족 시)에는 Q가 작아져 진행할 수 있다.',
          '실제로 일부 세균은 <b>폴리인산 키나아제</b>로 polyP의 인산을 ADP(또는 GDP)에 넘겨 ATP를 만든다. 즉 “항상 쓰는 주 에너지원”은 못 되지만 “보조 저장소”는 될 수 있다.') +
    tip('인산기는 사다리 “위 → 아래”로만 저절로 흘러. polyP(−20)는 ATP(−30.5)보다 <b>아래</b>에 있어서, 위로 인산을 올려 주려면 농도로 억지로 밀어 줘야 해.', '직관'))

add(id='P22', kind='PROBLEM', num='22',
    en_title='Daily ATP Utilization by Human Adults', ko_title='성인이 하루에 쓰는 ATP의 양', slides='강의 슬라이드 9, 14', level=2,
    en='''<p><b>a.</b> The synthesis of ATP from ADP and P<sub>i</sub> requires a total of 30.5 kJ/mol of free energy when the reactants and products are at 1 <span class="sc">M</span> concentrations and the temperature is 25 °C (standard state). However, the actual physiological concentrations of ATP, ADP, and P<sub>i</sub> are not 1 <span class="sc">M</span>, and the physiological temperature is 37 °C. Thus, the free energy required to synthesize ATP under physiological conditions is different from ΔG′°. Calculate the free energy required to synthesize ATP in the human hepatocyte when the physiological concentrations of ATP, ADP, and P<sub>i</sub> are 3.5, 1.50, and 5.0 m<span class="sc">M</span>, respectively.</p>
<p><b>b.</b> A 68 kg (150 lb) adult requires a caloric intake of 2,000 kcal (8,360 kJ) of food per day (24 hours). The body metabolizes the food and uses the free energy to synthesize ATP, which then provides energy for the body’s daily chemical and mechanical work. Assuming that the efficiency of converting food energy into ATP is 50%, calculate the weight of ATP used by a human adult in 24 hours. What percentage of the body weight does this represent?</p>
<p><b>c.</b> Although adults synthesize large amounts of ATP daily, their body weight, structure, and composition do not change significantly during this period. Explain this apparent contradiction.</p>''',
    ko='''<p><b>a.</b> 반응물과 생성물이 모두 1 M이고 25 °C(표준 상태)일 때 ADP와 P<sub>i</sub>로 ATP를 합성하려면 총 30.5 kJ/mol의 자유에너지가 필요하다. 그러나 실제 생리적 농도는 1 M이 아니고 체온은 37 °C이므로, 생리적 조건에서 필요한 자유에너지는 ΔG′°와 다르다. ATP·ADP·P<sub>i</sub>의 생리적 농도가 각각 3.5, 1.50, 5.0 mM인 사람 간세포에서 ATP 합성에 필요한 자유에너지를 계산하라.</p>
<p><b>b.</b> 68 kg 성인은 하루(24시간)에 2,000 kcal(8,360 kJ)의 음식을 섭취해야 한다. 몸은 음식을 대사해 그 자유에너지로 ATP를 합성하고, ATP가 하루의 화학적·기계적 일에 에너지를 공급한다. 음식 에너지를 ATP로 바꾸는 효율이 50%라고 할 때, 성인이 24시간 동안 사용하는 ATP의 무게를 계산하라. 이는 체중의 몇 %인가?</p>
<p><b>c.</b> 성인은 매일 엄청난 양의 ATP를 합성하지만, 그동안 체중·구조·조성은 거의 변하지 않는다. 이 모순처럼 보이는 현상을 설명하라.</p>''',
    blank=65,
    answer=chips('a. ≈ <b>+46 kJ/mol</b>', 'b. 약 90 mol ≈ <b>46 kg</b> ≈ 체중의 <b>67%</b>', 'c. ATP는 쌓이지 않고 <b>계속 재활용</b>(ATP ⇄ ADP + P<sub>i</sub>)'),
    explain=steps(
        '<b>a.</b> 합성 방향: ADP + P<sub>i</sub> → ATP, ΔG′° = +30.5' +
        eq(f'Q = {F("[ATP]", "[ADP][P<sub>i</sub>]")} = {F("3.5×10<sup>−3</sup>", "(1.50×10<sup>−3</sup>)(5.0×10<sup>−3</sup>)")} = 467 M<sup>−1</sup>') +
        align([(DG, '30.5 + (2.578)(ln 467) = 30.5 + (2.578)(6.15)'), ('', '30.5 + 15.8 = <span class="hl">+46.3 kJ/mol</span>')]),
        '<b>b.</b> ATP로 저장되는 에너지 = 8,360 kJ × 0.50 = 4,180 kJ<br>ATP 몰수 = 4,180 ÷ 46.3 ≈ <b>90 mol</b><br>무게 = 90 mol × 507 g/mol (ATP 분자량) ≈ 45,700 g ≈ <span class="hl">46 kg</span><br>체중 비율 = 46 ÷ 68 ≈ <span class="hl">67%</span>',
        '<b>c.</b> ATP는 만들어 두고 쌓아 두는 물질이 아니다. 쓰이면 ADP + P<sub>i</sub>가 되고, 곧바로 다시 ATP로 <b>재충전</b>된다. 몸속 ATP의 총량은 적지만, 같은 분자들이 하루에 수백 번 이상 돌고 돌아서 “누적 사용량”이 46 kg이 되는 것. 합성 속도 = 분해 속도 → <b>동적 정상 상태</b>.'
    ) +
    fig(atp_cycle(), 'ATP-ADP 사이클: 같은 분자가 충전(파랑) ↔ 방전(주황)을 끝없이 반복') +
    tip('충전식 배터리 하나를 하루에 수백 번 충전해서 쓰는 것과 같아. “하루 사용한 배터리 무게”를 합산하면 엄청나지만, 실제로 가진 배터리는 몇 개뿐이야.'))

add(id='P23', kind='PROBLEM', num='23',
    en_title='Rates of Turnover of γ and β Phosphates of ATP', ko_title='ATP의 γ-인산과 β-인산의 교체 속도', slides='강의 슬라이드 22', level=2,
    en='<p>After adding a small amount of ATP labeled with radioactive phosphorus in the terminal position, [γ-<sup>32</sup>P]ATP, to a yeast extract, a researcher finds about half of the <sup>32</sup>P activity in P<sub>i</sub> within a few minutes, but the concentration of ATP remains unchanged. Explain. She then carries out the same experiment using ATP labeled with <sup>32</sup>P in the central position, [β-<sup>32</sup>P]ATP, but the <sup>32</sup>P does not appear in P<sub>i</sub> within such a short time. Why?</p>',
    ko='<p>말단 위치의 인이 방사성 동위원소로 표지된 ATP([γ-<sup>32</sup>P]ATP)를 효모 추출물에 소량 넣었더니, 몇 분 안에 <sup>32</sup>P 방사능의 약 절반이 P<sub>i</sub>에서 발견되었지만 ATP 농도는 변하지 않았다. 설명하라. 이어서 가운데 위치가 표지된 ATP([β-<sup>32</sup>P]ATP)로 같은 실험을 했더니, 그 짧은 시간 안에는 <sup>32</sup>P가 P<sub>i</sub>에 나타나지 않았다. 왜 그런가?</p>',
    blank=40,
    answer=chips('γ: 끝 인산은 <b>계속 떨어졌다 다시 붙는다</b>(빠른 교체) → 표지가 P<sub>i</sub>로 퍼짐, ATP 총량은 <b>합성 = 분해</b>라 일정',
                 'β: ATP → ADP가 돼도 β-인산은 <b>ADP에 남아</b> 있다가 다시 ATP가 됨 → P<sub>i</sub>로 잘 안 나옴'),
    explain=fig(atp_chain(), 'ATP의 세 인산: α(리보스 쪽) – β(가운데) – γ(끝)') +
    steps('<b>γ-표지</b>: 세포에서 ATP는 대부분 γ-인산(끝)을 주고 ADP가 된다 → 표지된 <sup>32</sup>P가 P<sub>i</sub>(또는 다른 분자 → 결국 P<sub>i</sub>)로 나간다.',
          '곧바로 ADP + (표지 안 된 대부분의) P<sub>i</sub> → ATP로 재합성된다. 만드는 속도 = 쓰는 속도라서 <b>[ATP]는 일정</b>하지만, 끝자리 인산은 계속 “새 것으로 교체” → 표지가 P<sub>i</sub> 풀(pool)로 희석된다.',
          '<b>β-표지</b>: ATP → ADP + P<sub>i</sub>에서 β-인산은 ADP의 끝 인산이 되어 <b>그대로 남는다</b>. 다시 인산화되면 또 ATP의 β-자리. β가 P<sub>i</sub>로 나오려면 ATP → AMP + PP<sub>i</sub> → 2P<sub>i</sub> 같은 드문 경로가 필요해서 몇 분 안엔 거의 안 보인다.') +
    tip('기차(ATP)의 맨 끝 칸(γ)만 역마다 떼었다 붙였다 한다고 생각해 봐. 끝 칸에 붙은 스티커(표지)는 금방 플랫폼(P<sub>i</sub>)으로 흩어지지만, 가운데 칸(β)의 스티커는 기차에 계속 남아 있어.'))

add(id='P24', kind='PROBLEM', num='24',
    en_title='Cleavage of ATP to AMP and PP<sub>i</sub> during Metabolism', ko_title='대사 중 ATP가 AMP와 PP<sub>i</sub>로 쪼개질 때', slides='강의 슬라이드 22, 31', level=2,
    en='''<p>Synthesis of the activated form of acetate (acetyl-CoA) is carried out in an ATP-dependent process:</p>
<p class="c">Acetate + CoA + ATP → acetyl-CoA + AMP + PP<sub>i</sub></p>
<p><b>a.</b> The ΔG′° for hydrolysis of acetyl-CoA to acetate and CoA is −32.2 kJ/mol. The ΔG′° for hydrolysis of ATP to AMP and PP<sub>i</sub> is −30.5 kJ/mol. Calculate ΔG′° for the ATP-dependent synthesis of acetyl-CoA.<br>
<b>b.</b> Almost all cells contain the enzyme inorganic pyrophosphatase, which catalyzes the hydrolysis of PP<sub>i</sub> to P<sub>i</sub>. What effect does the presence of this enzyme have on the synthesis of acetyl-CoA? Explain.</p>''',
    ko='''<p>아세트산의 활성화된 형태(아세틸-CoA)는 ATP 의존적 과정으로 합성된다: 아세트산 + CoA + ATP → 아세틸-CoA + AMP + PP<sub>i</sub></p>
<p><b>a.</b> 아세틸-CoA가 아세트산과 CoA로 가수분해되는 ΔG′°는 −32.2 kJ/mol, ATP가 AMP와 PP<sub>i</sub>로 가수분해되는 ΔG′°는 −30.5 kJ/mol이다. ATP 의존적 아세틸-CoA 합성의 ΔG′°를 계산하라.<br>
<b>b.</b> 거의 모든 세포에는 PP<sub>i</sub>를 P<sub>i</sub>로 가수분해하는 무기 피로인산가수분해효소(pyrophosphatase)가 있다. 이 효소가 있으면 아세틸-CoA 합성에 어떤 영향을 주는가? 설명하라.</p>''',
    blank=45,
    answer=chips('a. ΔG′° = +32.2 + (−30.5) = <b>+1.7 kJ/mol</b> (약간 불리)', 'b. PP<sub>i</sub> 분해(−19.2)가 더해져 합이 <b>−17.5 kJ/mol</b> → 합성이 <b>강하게 정방향</b>(사실상 비가역)'),
    explain=key('ATP를 <b>AMP + PP<sub>i</sub></b>로 자르고, 이어서 PP<sub>i</sub>까지 잘라 버리면 인산 무수물 결합 <b>두 개</b>의 에너지를 쓰는 셈이다.') +
    align([('a.', '아세트산 + CoA → 아세틸-CoA (+H<sub>2</sub>O)', '+32.2'), ('', 'ATP + H<sub>2</sub>O → AMP + PP<sub>i</sub>', '−30.5'),
           ('합', '아세트산 + CoA + ATP → 아세틸-CoA + AMP + PP<sub>i</sub>', '<span class="hl">+1.7</span>')], cls='sum') +
    align([('b.', '위 반응', '+1.7'), ('', 'PP<sub>i</sub> + H<sub>2</sub>O → 2P<sub>i</sub>', '−19.2'),
           ('합', '전체 (PP<sub>i</sub>까지 분해)', '<span class="hl">−17.5</span>')], cls='sum') +
    steps('<b>b 해석 ①</b> 에너지: PP<sub>i</sub> 가수분해의 −19.2가 더해져 전체가 크게 음수 → K가 약 10<sup>3</sup>배 이상 커진다.',
          '<b>b 해석 ②</b> 르샤틀리에: 생성물 PP<sub>i</sub>가 즉시 치워지니 역반응이 불가능 → 아세틸-CoA 합성이 한 방향으로 쭉 “당겨진다”.') +
    fig(energy_steps([('아세트산 + CoA + ATP', 0, C['navy']), ('아세틸-CoA + AMP + PPᵢ', 1.7, C['red']), ('… + 2Pᵢ', -17.5, C['green'])], height=190),
        '살짝 오르막(+1.7)이지만, PPᵢ를 부수는 내리막(−19.2)이 뒤에서 확 끌어당긴다') +
    warn('표 13-6에는 ATP → AMP + PP<sub>i</sub>가 −45.6 kJ/mol로 나와 있어. 이 값을 쓰면 a는 −13.4 kJ/mol이 된다. 문제에서 −30.5라고 <b>주어졌으니 주어진 값</b>으로 계산하는 게 원칙!', '참고'))

add(id='P25', kind='PROBLEM', num='25',
    en_title='Activation of a Fatty Acid by Reaction with Coenzyme A', ko_title='조효소 A와의 반응으로 지방산 활성화하기', slides='강의 슬라이드 22', level=2,
    en='''<p>In the reaction sequence for fatty acid breakdown, coenzyme A (CoA), with its thiol (—SH) group, joins to the fatty acid as a thiol ester, as ATP is converted into AMP and PP<sub>i</sub>:</p>
<p class="c">R—COO<sup>−</sup> + ATP + CoA—SH → AMP + PP<sub>i</sub> + R—CO—S—CoA</p>
<p>The oxidation of fatty acids as fuels requires two steps. The first step transfers an activating group from ATP to the carboxyl group of the fatty acid. In the second step, CoA—SH displaces the activating group to form fatty acyl-S—CoA. Given the known products of the reaction, what is the activating group?</p>''',
    ko='<p>지방산 분해 과정에서, 싸이올(—SH)기를 가진 조효소 A(CoA)는 ATP가 AMP와 PP<sub>i</sub>로 바뀌는 동안 지방산과 <b>싸이오에스터</b>로 결합한다(위 반응식). 연료로서 지방산을 산화하려면 두 단계가 필요하다. 1단계에서는 ATP의 <b>활성화기</b>가 지방산의 카복실기로 옮겨진다. 2단계에서는 CoA—SH가 그 활성화기를 밀어내고 지방산아실-S—CoA를 만든다. 알려진 생성물로 판단할 때, 활성화기는 무엇인가?</p>',
    blank=35,
    answer=chips('활성화기 = <b>AMP (아데닐기, adenylyl group)</b> — 중간체는 지방산아실-AMP(아실 아데닐산)'),
    explain=key('생성물에 <b>PP<sub>i</sub></b>와 <b>AMP</b>가 “따로따로” 나온다 = 1단계에서 PP<sub>i</sub>가 먼저 떨어지고, AMP는 지방산에 붙었다가 2단계에서 떨어진다.') +
    '<div class="twostep"><div><span>1단계</span>R—COO<sup>−</sup> + ATP → R—CO—<b>AMP</b> + <b>PP<sub>i</sub></b><small>카복실산의 O가 ATP의 α-인산을 공격 → 아데닐기가 지방산으로</small></div>'
    '<div><span>2단계</span>R—CO—AMP + CoA—SH → R—CO—S—CoA + <b>AMP</b><small>CoA의 —SH가 AMP를 밀어내고 자리를 차지</small></div></div>' +
    steps('ATP가 γ-인산을 주면 생성물은 ADP + P<sub>i</sub>가 나왔을 것. 그런데 실제로는 <b>AMP + PP<sub>i</sub></b> → 공격 지점은 γ가 아니라 <b>α-인산</b>(AMP 부분이 통째로 전달).',
          '지방산아실-AMP는 카복실산과 인산이 붙은 <b>혼합 산무수물</b>이라 매우 반응성이 크다(좋은 이탈기 AMP) → CoA가 쉽게 치환.',
          '문제 24처럼 PP<sub>i</sub>는 피로인산가수분해효소로 곧바로 분해 → 전체 반응이 강하게 앞으로 당겨진다.') +
    tip('슬라이드 22의 글루타민 합성(글루탐산 → 글루타밀 <b>인산</b> → 글루타민)과 같은 “2단계 작전”이야. 다른 점은 붙는 꼬리표가 인산이 아니라 <b>AMP</b>라는 것뿐.', '연결'))

add(id='P26', kind='PROBLEM', num='26',
    en_title='Energy for H<sup>+</sup> Pumping', ko_title='H<sup>+</sup> 펌프에 필요한 에너지', slides='강의 슬라이드 24 (능동수송)', level=2,
    en='<p>The parietal cells of the stomach lining contain membrane “pumps” that transport hydrogen ions from the cytosol (pH 7.0) into the stomach, contributing to the acidity of gastric juice (pH 1.0). Calculate the free energy required to transport 1 mol of hydrogen ions through these pumps. (Hint: See Chapter 11.) Assume a temperature of 37 °C.</p>',
    ko='<p>위 점막의 벽세포(parietal cell)에는 세포질(pH 7.0)에서 위 속(pH 1.0)으로 수소 이온을 운반하는 막 “펌프”가 있어 위액의 산성에 기여한다. 이 펌프로 수소 이온 1 mol을 운반하는 데 필요한 자유에너지를 계산하라. (힌트: 11장 참고) 온도는 37 °C로 가정한다.</p>',
    blank=40,
    answer=chips(f'{DG} ≈ <b>+35.6 kJ/mol</b> (H<sup>+</sup> 1 mol당)'),
    explain=key('막을 사이에 둔 농도 차를 거슬러 옮길 때: ΔG = RT ln(C<sub>도착</sub> / C<sub>출발</sub>). 도착지가 더 진하면 양수(오르막).') +
    fig(pump_svg(), '묽은 곳(pH 7) → 진한 곳(pH 1)으로 H⁺를 퍼 올리는 오르막 수송') +
    steps('C<sub>출발</sub> = 세포질 [H<sup>+</sup>] = 10<sup>−7</sup> M,  C<sub>도착</sub> = 위 속 [H<sup>+</sup>] = 10<sup>−1</sup> M → 비 = 10<sup>6</sup>',
          align([(DG, 'RT ln(10<sup>6</sup>) = (2.578 kJ/mol)(13.8)'), ('', '<span class="hl">+35.6 kJ/mol</span>')]),
          '(이 펌프는 H<sup>+</sup> 1개를 내보내며 K<sup>+</sup> 1개를 들여오는 H<sup>+</sup>/K<sup>+</sup> ATPase라 전하가 상쇄 → 막전위 항은 무시해도 된다.)') +
    tip('<b>pH 1 차이 = 농도 10배</b> ↔ 37 °C에서 약 5.9 kJ/mol. pH 차이 6 × 5.9 ≈ 35.6 kJ/mol. ATP 1개(세포 속 약 50 kJ/mol)로 H<sup>+</sup> 1개를 옮길 수 있는 수준이야.', '꿀팁'))

add(id='P27', kind='PROBLEM', num='27',
    en_title='Most-Reduced Carbon Compounds', ko_title='가장 환원된 탄소 화합물', slides='강의 슬라이드 36–38', level=1,
    en='<p>Arrange the four structures in order from most reduced to most oxidized.</p><p class="c">a. R—CH<sub>2</sub>—CH<sub>2</sub>—OH &nbsp;&nbsp; b. R—CH<sub>2</sub>—COO<sup>−</sup> &nbsp;&nbsp; c. R—CH<sub>2</sub>—CHO &nbsp;&nbsp; d. R—CH<sub>2</sub>—CH<sub>3</sub></p>',
    ko='<p>네 구조를 가장 환원된 것부터 가장 산화된 것 순서로 나열하라.</p>',
    blank=30,
    answer=chips('<b>d &gt; a &gt; c &gt; b</b>', '(알케인 &gt; 알코올 &gt; 알데하이드 &gt; 카복실산)'),
    explain=key('<b>H가 많이 붙을수록 환원</b>, <b>O가 많이 붙을수록 산화</b>. 오른쪽 끝 탄소만 비교하면 된다.') +
    fig(carbon_ladder(), '그림 13-22 방식: 전기음성도 H &lt; C &lt; O → C–H 전자는 C가, C–O 전자는 O가 “소유”') +
    steps('끝 탄소의 전자 세기: C–C 결합은 1개씩 나눠 갖고, C–H는 2개 모두 C 것, C–O는 0개.',
          'd –CH<sub>3</sub>: 1 + 2×3 = <b>7</b> / a –CH<sub>2</sub>OH: 1 + 2×2 = <b>5</b> / c –CHO: 1 + 2 = <b>3</b> / b –COO<sup>−</sup>: <b>1</b>',
          '전자가 많을수록 환원된 상태 → d(7) &gt; a(5) &gt; c(3) &gt; b(1).') +
    tip('환원된 탄소 = 아직 “타지 않은 연료”. 그래서 –CH<sub>2</sub>–가 가득한 지방이 –CHOH–인 탄수화물보다 1 g당 에너지가 더 많다(태울 거리가 더 많음).', '연결'))

add(id='P28', kind='PROBLEM', num='28',
    en_title='Standard Reduction Potentials', ko_title='표준 환원 전위', slides='강의 슬라이드 42–45', level=2,
    en='''<p>The standard reduction potential, E′°, of any redox pair is defined for the half-cell reaction</p>
<p class="c">Oxidizing agent + <i>n</i> electrons → reducing agent</p>
<p>The E′° values for the NAD<sup>+</sup>/NADH and pyruvate/lactate conjugate redox pairs are −0.32 V and −0.19 V, respectively.</p>
<p><b>a.</b> Which redox pair has the greater tendency to lose electrons? Explain.<br>
<b>b.</b> Which pair is the stronger oxidizing agent? Explain.<br>
<b>c.</b> Beginning with 1 <span class="sc">M</span> concentrations of each reactant and product at pH 7 and 25 °C, in which direction will the following reaction proceed?<br>
<span class="c" style="display:block">Pyruvate + NADH + H<sup>+</sup> ⇌ lactate + NAD<sup>+</sup></span>
<b>d.</b> What is the standard free-energy change (ΔG′°) for the conversion of pyruvate to lactate?<br>
<b>e.</b> What is the equilibrium constant ({K}) for this reaction?</p>'''.replace('{K}', 'K′<sub>eq</sub>'),
    ko='''<p>어떤 산화환원 짝의 표준 환원 전위 E′°는 반쪽 반응 “산화제 + n 전자 → 환원제”에 대해 정의된다. NAD<sup>+</sup>/NADH 짝과 피루브산/젖산 짝의 E′°는 각각 −0.32 V, −0.19 V이다.</p>
<p><b>a.</b> 전자를 잃으려는 경향이 더 큰 짝은? 설명하라.<br><b>b.</b> 더 강한 산화제인 짝은? 설명하라.<br>
<b>c.</b> pH 7, 25 °C에서 모든 반응물과 생성물이 1 M로 시작할 때, 반응(피루브산 + NADH + H<sup>+</sup> ⇌ 젖산 + NAD<sup>+</sup>)은 어느 방향으로 진행하는가?<br>
<b>d.</b> 피루브산 → 젖산 전환의 표준 자유에너지 변화(ΔG′°)는?<br><b>e.</b> 이 반응의 평형상수(K′<sub>eq</sub>)는?</p>''',
    blank=55,
    answer=chips('a. <b>NAD<sup>+</sup>/NADH</b> (E′° 더 음수)', 'b. <b>피루브산/젖산</b> (E′° 더 양수)', 'c. <b>오른쪽</b> (젖산 + NAD<sup>+</sup> 생성)',
                 'd. <b>−25 kJ/mol</b>', 'e. <b>≈ 2.5×10<sup>4</sup></b>'),
    explain=fig(ladder([('NAD⁺/NADH', -0.32), ('피루브산/젖산', -0.19)], -0.35, -0.16, hl=('NAD⁺/NADH', '피루브산/젖산'),
                       flows=[('NAD⁺/NADH', '피루브산/젖산', '2e⁻')], height=160),
                '전자는 더 음수(NADH) → 더 양수(피루브산)로 흐른다') +
    steps('<b>a.</b> E′°가 <b>더 음수</b>일수록 전자를 붙잡는 힘이 약하다 = 잘 내준다 → NAD<sup>+</sup>/NADH(−0.32). (환원형 NADH가 좋은 환원제)',
          '<b>b.</b> 산화제 = 전자를 <b>빼앗는</b> 물질. E′°가 더 양수인 피루브산/젖산(−0.19)의 피루브산이 더 강한 산화제.',
          '<b>c.</b> 전자는 NADH → 피루브산으로 흐른다 → 피루브산이 젖산으로 환원, NADH는 NAD<sup>+</sup>로 산화 → <b>오른쪽</b>.',
          f'<b>d.</b> {DE0} = −0.19 − (−0.32) = +0.13 V → {G0} = −2 × 96.48 × 0.13 = <span class="hl">−25 kJ/mol</span>',
          f'<b>e.</b> {K} = e<sup>25.1/2.478</sup> = e<sup>10.1</sup> ≈ <span class="hl">2.5×10<sup>4</sup></span>') +
    tip('산화제/환원제 용어가 헷갈리면: “산화제는 남을 산화시키고 <b>자기는 환원</b>된다(전자를 받는다)”. 전자를 받는 쪽 = E′°가 높은 쪽 = 산화제.', '용어 정리') +
    '<p class="note">표 13-7의 더 정확한 값(−0.185 V)을 쓰면 ΔE′° = 0.135 V, ΔG′° = −26 kJ/mol, K ≈ 3.6×10<sup>4</sup>. 문제에 주어진 −0.19 V로 계산하는 게 원칙.</p>')

add(id='P29', kind='PROBLEM', num='29',
    en_title='Simple Biobattery', ko_title='간단한 바이오 배터리', slides='강의 슬라이드 42–43', level=2,
    en=f'''<p>Suppose you set up a simple battery using half-reactions as pictured in Figure 13-23. One electrode contains pyruvate and lactate at 1 m<span class="sc">M</span>, and the other electrode contains fumarate and succinate at 1 m<span class="sc">M</span> (see Table 13-7).</p>
{img('fig13_23.png', '30%', 'FIGURE 13-23 Measurement of the standard reduction potential (E′°) of a redox pair.')}
<p><b>a.</b> In which direction will electrons initially flow?<br>
<b>b.</b> Calculate the standard reduction potential and standard free-energy change for your biological battery.<br>
<b>c.</b> When a flashlight battery “runs out,” net electron movement has essentially ended. What is the equivalent situation for your biobattery?</p>''',
    ko='''<p>그림 13-23과 같은 반쪽 전지를 이용해 간단한 전지를 만든다고 하자. 한쪽 전극에는 피루브산과 젖산이 각 1 mM, 다른 쪽 전극에는 푸마르산과 숙신산이 각 1 mM 들어 있다(표 13-7 참고).</p>
<p><b>a.</b> 전자는 처음에 어느 방향으로 흐르는가?<br><b>b.</b> 이 생물 전지의 표준 (환원) 전위차와 표준 자유에너지 변화를 계산하라.<br>
<b>c.</b> 손전등 건전지가 “다 닳으면” 알짜 전자 이동이 사실상 멈춘다. 이 바이오 배터리에서 이에 해당하는 상황은 무엇인가?</p>''',
    blank=45,
    answer=chips('a. <b>피루브산/젖산 전극 → 푸마르산/숙신산 전극</b>', f'b. {DE0} = <b>+0.216 V</b>, {G0} ≈ <b>−41.7 kJ/mol</b>', 'c. 반응이 <b>평형</b>에 도달 (ΔE = 0, ΔG = 0)'),
    explain=fig(battery_svg(), '전자는 E′°가 낮은(−0.185) 쪽에서 높은(+0.031) 쪽으로 도선을 따라 흐른다') +
    steps('<b>a.</b> 두 전극 모두 산화형:환원형 = 1:1이라 실제 전위 = E′°. 피루브산/젖산(−0.185) &lt; 푸마르산/숙신산(+0.031) → 젖산이 전자를 내놓고(→ 피루브산), 푸마르산이 받는다(→ 숙신산).',
          f'<b>b.</b> {DE0} = E′°<sub>받는 쪽</sub> − E′°<sub>주는 쪽</sub> = 0.031 − (−0.185) = <span class="hl">+0.216 V</span><br>{G0} = −nF{DE0} = −2 × 96.48 × 0.216 = <span class="hl">−41.7 kJ/mol</span>',
          '<b>c.</b> 반응이 진행할수록 젖산·푸마르산은 줄고 피루브산·숙신산은 늘어 두 전극의 실제 전위 E가 점점 가까워진다. E가 같아지면(ΔE = 0) ΔG = 0 = <b>평형</b> → 전자 흐름이 멈춘 “방전된 배터리”.') +
    tip('배터리가 “살아 있다” = 평형에서 멀다. 세포가 살아 있는 것도 마찬가지로 반응들을 평형에서 멀리 유지하기 때문이야(평형 = 죽음).', '연결'))

add(id='P30', kind='PROBLEM', num='30',
    en_title='Energy Span of the Respiratory Chain', ko_title='호흡 사슬의 에너지 폭', slides='강의 슬라이드 43, 45', level=2,
    en=f'''<p>Electron transfer in the mitochondrial respiratory chain may be represented by the net reaction equation</p>
<p class="c">NADH + H<sup>+</sup> + ½O<sub>2</sub> ⇌ H<sub>2</sub>O + NAD<sup>+</sup></p>
<p><b>a.</b> Calculate ΔE′° for the net reaction of mitochondrial electron transfer. Use E′° values in Table 13-7.<br>
<b>b.</b> Calculate ΔG′° for this reaction.<br>
<b>c.</b> How many ATP molecules can <i>theoretically</i> be generated by this reaction if the free energy of ATP synthesis under cellular conditions is 52 kJ/mol?</p>''',
    ko='''<p>미토콘드리아 호흡 사슬의 전자 전달은 알짜 반응식 NADH + H<sup>+</sup> + ½O<sub>2</sub> ⇌ H<sub>2</sub>O + NAD<sup>+</sup>로 나타낼 수 있다.</p>
<p><b>a.</b> 표 13-7의 E′° 값으로 미토콘드리아 전자 전달 알짜 반응의 ΔE′°를 계산하라.<br><b>b.</b> 이 반응의 ΔG′°를 계산하라.<br>
<b>c.</b> 세포 조건에서 ATP 합성의 자유에너지가 52 kJ/mol이라면, 이 반응으로 <i>이론적으로</i> 몇 개의 ATP를 만들 수 있는가?</p>''',
    blank=40,
    answer=chips(f'a. {DE0} = <b>1.136 V</b>', f'b. {G0} ≈ <b>−219 kJ/mol</b>', 'c. 219 ÷ 52 ≈ 4.2 → 최대 <b>4개</b>'),
    explain=fig(ladder(R('½O₂/H₂O', '시토크롬 c', '유비퀴논/유비퀴놀', 'NAD⁺/NADH'), -0.36, 0.86, hl=('½O₂/H₂O', 'NAD⁺/NADH'),
                       flows=[('NAD⁺/NADH', '½O₂/H₂O', '2e⁻')], height=260),
                '표 13-7의 맨 아래 근처(NADH)에서 맨 위(O₂)까지 — 가장 큰 폭의 전자 “폭포”') +
    steps(f'<b>a.</b> 받는 쪽 O<sub>2</sub>(+0.816), 주는 쪽 NADH(−0.320): {DE0} = 0.816 − (−0.320) = <span class="hl">1.136 V</span>',
          f'<b>b.</b> {G0} = −2 × 96.48 × 1.136 = <span class="hl">−219 kJ/mol</span>',
          '<b>c.</b> 219 ÷ 52 = 4.2 → ATP는 정수 개만 만들 수 있으니 이론상 최대 <b>4개</b>.') +
    tip('실제로 NADH 1개당 만들어지는 ATP는 약 <b>2.5개</b>(슬라이드 53). 나머지 에너지는 열로 나가 체온 유지에 쓰인다. 전자가 한 번에 떨어지지 않고 유비퀴논·시토크롬 같은 “계단”을 타고 내려가는 덕분에 에너지를 조금씩 나눠 담을 수 있어.', '연결'))

add(id='P31', kind='PROBLEM', num='31',
    en_title='Dependence of Electromotive Force on Concentrations', ko_title='기전력의 농도 의존성', slides='강의 슬라이드 44', level=2,
    en='''<p>Suppose that you place an electrode into solutions of various concentrations of NAD<sup>+</sup> and NADH at pH 7.0 and 25 °C. Calculate the electromotive force (in volts) registered by the electrode when immersed in each solution, with reference to a half-cell of E′° 0.00 V.</p>
<p class="c">a. 1.0 m<span class="sc">M</span> NAD<sup>+</sup> and 10 m<span class="sc">M</span> NADH<br>b. 1.0 m<span class="sc">M</span> NAD<sup>+</sup> and 1.0 m<span class="sc">M</span> NADH<br>c. 10 m<span class="sc">M</span> NAD<sup>+</sup> and 1.0 m<span class="sc">M</span> NADH</p>''',
    ko='<p>pH 7.0, 25 °C에서 NAD<sup>+</sup>와 NADH 농도가 다양한 용액에 전극을 넣었다고 하자. E′° = 0.00 V인 반쪽 전지를 기준으로, 각 용액에 전극을 담갔을 때 측정되는 기전력(V)을 계산하라. (a. NAD<sup>+</sup> 1.0 mM, NADH 10 mM / b. 둘 다 1.0 mM / c. NAD<sup>+</sup> 10 mM, NADH 1.0 mM)</p>',
    blank=40,
    answer=chips('a. <b>−0.350 V</b>', 'b. <b>−0.320 V</b>', 'c. <b>−0.290 V</b>'),
    explain=key(f'E = {E0} + {F("RT", "nF")} ln {F("[산화형]", "[환원형]")},  n = 2,  25 °C에서 RT/2F = 0.0128 V') +
    table(['', '[NAD<sup>+</sup>]/[NADH]', 'ln(비)', '0.0128 × ln', 'E (V)'],
          [['a', '0.1', '−2.30', '−0.030', '<b>−0.350</b>'], ['b', '1', '0', '0', '<b>−0.320</b>'], ['c', '10', '+2.30', '+0.030', '<b>−0.290</b>']]) +
    fig(e_line(), '농도비가 10배 바뀔 때마다 E는 약 30 mV(0.03 V)씩 이동') +
    tip('E는 “전자를 받고 싶은 정도”. 전자를 받을 NAD<sup>+</sup>가 많으면 받고 싶은 마음이 커져 E가 올라가고(+ 방향), 이미 전자를 받은 NADH가 많으면 E가 내려간다. 비가 1:1이면 딱 E′°.', '직관'))

add(id='P32', kind='PROBLEM', num='32',
    en_title='Electron Affinity of Compounds', ko_title='화합물의 전자 친화도', slides='강의 슬라이드 43', level=1,
    en='<p>List the four compounds or reactions in order of increasing tendency to accept electrons:</p><p class="c">a. α-ketoglutarate + CO<sub>2</sub> (yielding isocitrate) &nbsp; b. oxaloacetate &nbsp; c. O<sub>2</sub> &nbsp; d. NADP<sup>+</sup></p>',
    ko='<p>다음 네 화합물(또는 반응)을 전자를 받으려는 경향이 <b>증가하는</b> 순서로 나열하라: a. α-케토글루타르산 + CO<sub>2</sub>(아이소시트르산 생성) / b. 옥살로아세트산 / c. O<sub>2</sub> / d. NADP<sup>+</sup></p>',
    blank=30,
    answer=chips('<b>a &lt; d &lt; b &lt; c</b>', '(−0.38 &lt; −0.324 &lt; −0.166 &lt; +0.816 V)'),
    explain=key('“전자를 받으려는 경향” = 환원 전위 E′°. 표 13-7에서 값을 찾아 <b>작은 것 → 큰 것</b> 순으로 줄 세우면 끝.') +
    fig(ladder(R('½O₂/H₂O', '옥살로아세트산/말산', 'NADP⁺/NADPH', 'α-케토글루타르산+CO₂/아이소시트르산'), -0.42, 0.86,
               hl=('½O₂/H₂O', '옥살로아세트산/말산', 'NADP⁺/NADPH', 'α-케토글루타르산+CO₂/아이소시트르산'), height=240),
        '위로 갈수록 전자를 더 좋아한다: O₂가 압도적 1위') +
    tip('O<sub>2</sub>가 호흡 사슬의 마지막 전자 수용체인 이유가 바로 이것. 전자를 가장 “탐내는” 분자라서 모든 전자가 결국 O<sub>2</sub>로 흘러간다.', '연결'))

add(id='P33', kind='PROBLEM', num='33',
    en_title='Direction of Oxidation-Reduction Reactions', ko_title='산화-환원 반응의 방향', slides='강의 슬라이드 43', level=2,
    en='''<p>Which of the reactions listed would you expect to proceed in the direction shown, under standard conditions, in the presence of the appropriate enzymes?</p>
<p class="c">a. Malate + NAD<sup>+</sup> → oxaloacetate + NADH + H<sup>+</sup><br>b. Acetoacetate + NADH + H<sup>+</sup> → β-hydroxybutyrate + NAD<sup>+</sup><br>c. Pyruvate + NADH + H<sup>+</sup> → lactate + NAD<sup>+</sup><br>d. Pyruvate + β-hydroxybutyrate → lactate + acetoacetate<br>e. Malate + pyruvate → oxaloacetate + lactate<br>f. Acetaldehyde + succinate → ethanol + fumarate</p>''',
    ko='<p>적절한 효소가 있을 때, 표준 조건에서 다음 반응 중 표시된 방향으로 진행할 것이라 예상되는 것은? (a. 말산 + NAD<sup>+</sup> → 옥살로아세트산 + NADH + H<sup>+</sup> / b. 아세토아세트산 + NADH + H<sup>+</sup> → β-하이드록시뷰티르산 + NAD<sup>+</sup> / c. 피루브산 + NADH + H<sup>+</sup> → 젖산 + NAD<sup>+</sup> / d. 피루브산 + β-하이드록시뷰티르산 → 젖산 + 아세토아세트산 / e. 말산 + 피루브산 → 옥살로아세트산 + 젖산 / f. 아세트알데하이드 + 숙신산 → 에탄올 + 푸마르산)</p>',
    blank=40,
    answer=chips('진행 ○ : <b>c, d</b>', '진행 ✕ : a, b, e, f'),
    explain=key(f'각 반응에서 ① 전자를 <b>받는</b> 쪽(환원되는 물질)과 ② <b>주는</b> 쪽을 찾고 → {DE0} = E′°<sub>받는</sub> − E′°<sub>주는</sub>. 양수면 ○.') +
    table(['', '받는 쪽 (E′°)', '주는 쪽 (E′°)', 'ΔE′° (V)', '진행?'],
          [['a', 'NAD<sup>+</sup> (−0.320)', '말산 (−0.166)', '−0.154', '✕'],
           ['b', '아세토아세트산 (−0.346)', 'NADH (−0.320)', '−0.026', '✕'],
           ['c', '피루브산 (−0.185)', 'NADH (−0.320)', '<b>+0.135</b>', '<b>○</b>'],
           ['d', '피루브산 (−0.185)', 'β-하이드록시뷰티르산 (−0.346)', '<b>+0.161</b>', '<b>○</b>'],
           ['e', '피루브산 (−0.185)', '말산 (−0.166)', '−0.019', '✕'],
           ['f', '아세트알데하이드 (−0.197)', '숙신산 (+0.031)', '−0.228', '✕']]) +
    fig(ladder(R('푸마르산/숙신산', '옥살로아세트산/말산', '피루브산/젖산', '아세트알데하이드/에탄올', 'NAD⁺/NADH', '아세토아세트산/β-하이드록시뷰티르산'),
               -0.37, 0.05, hl=('피루브산/젖산',), flows=[('NAD⁺/NADH', '피루브산/젖산', 'c'), ('아세토아세트산/β-하이드록시뷰티르산', '피루브산/젖산', 'd')], height=270),
        '규칙: 아래쪽 짝의 환원형이 위쪽 짝의 산화형에게 전자를 준다 (c, d만 “아래 → 위”)') +
    tip('받는 쪽 찾는 법: 화살표 뒤에서 H가 늘어난(또는 O가 줄어든) 물질이 환원된 것 = 전자를 받은 쪽. 예) 피루브산 → 젖산(H 2개 추가).', '요령'))

add(id='P34', kind='PROBLEM', num='34',
    en_title='Measurement of Intracellular Metabolite Concentrations', ko_title='세포 속 대사물질 농도 측정', slides='강의 슬라이드 20, 54', level=3,
    en='''<p>Measuring the concentrations of metabolic intermediates in a living cell presents great experimental difficulties — usually, a cell must be destroyed before metabolite concentrations can be measured. Yet enzymes catalyze metabolic interconversions very rapidly, so a common problem associated with these types of measurements is that the findings reflect not the physiological concentrations of metabolites but the equilibrium concentrations. To prevent changes in metabolite concentrations during sample preparation, cells were quick-frozen in liquid nitrogen, then extracted under conditions that prevented enzymatic activity. The table gives the intracellular concentrations of the substrates and products of the phosphofructokinase-1 reaction in isolated rat heart tissue.</p>''' +
    table(['Metabolite', 'Concentration (μM)'], [['Fructose 6-phosphate', '87.0'], ['Fructose 1,6-bisphosphate', '22.0'], ['ATP', '11,400'], ['ADP', '1,320']], cls='mini') +
    '''<p class="small c">Data from J. R. Williamson, J. Biol. Chem. 240:2308, 1965. Calculated as μmol/mL of intracellular water.</p>
<p><b>a.</b> Calculate Q, [fructose 1,6-bisphosphate][ADP]/[fructose 6-phosphate][ATP], for the PFK-1 reaction under physiological conditions.<br>
<b>b.</b> Given a ΔG′° for the PFK-1 reaction of −14.2 kJ/mol, calculate the equilibrium constant for this reaction.<br>
<b>c.</b> Compare the values of Q and K′<sub>eq</sub>. Is the physiological reaction near or far from equilibrium? Explain. What does this experiment suggest about the role of PFK-1 as a regulatory enzyme?</p>''',
    ko='''<p>살아 있는 세포 속 대사 중간체의 농도를 재기는 매우 어렵다. 보통 세포를 부순 뒤에야 측정할 수 있는데, 효소는 대사 전환을 매우 빠르게 촉매하므로 측정값이 실제 생리적 농도가 아니라 <b>평형 농도</b>를 반영해 버리는 문제가 흔하다. 시료 준비 중 농도 변화를 막으려고 세포를 액체 질소로 급속 냉동한 뒤 효소가 작동하지 못하는 조건에서 추출했다. 표는 분리한 쥐 심장 조직에서 포스포프룩토키나아제-1(PFK-1) 반응의 기질과 생성물의 세포 내 농도이다.</p>
<p><b>a.</b> 생리적 조건에서 PFK-1 반응의 Q = [과당 1,6-이인산][ADP]/[과당 6-인산][ATP]를 계산하라.<br><b>b.</b> PFK-1 반응의 ΔG′°가 −14.2 kJ/mol일 때 평형상수를 계산하라.<br>
<b>c.</b> Q와 K′<sub>eq</sub>를 비교하라. 생리적 반응은 평형에 가까운가, 먼가? 설명하라. 이 실험은 조절 효소로서 PFK-1의 역할에 대해 무엇을 시사하는가?</p>''',
    blank=50,
    answer=chips('a. Q ≈ <b>0.029</b> (2.9×10<sup>−2</sup>)', 'b. K′<sub>eq</sub> ≈ <b>3.1×10<sup>2</sup></b>', 'c. Q ≪ K (약 1만 배 차이) → 평형에서 <b>매우 멀다</b> → PFK-1은 <b>조절 지점</b>'),
    explain=steps(
        '<b>a.</b>' + eq(f'Q = {F("(22.0)(1320)", "(87.0)(11400)")} = {F("29,040", "991,800")} = <span class="hl">0.029</span>') + '(분자·분모 농도 2개씩 → μM 단위 상쇄)',
        f'<b>b.</b> {K} = e<sup>14.2/2.478</sup> = e<sup>5.73</sup> ≈ <span class="hl">308</span>',
        '<b>c.</b> K/Q ≈ 308 / 0.029 ≈ 10<sup>4</sup>. 실제 ΔG = −14.2 + 2.478 × ln 0.029 = −14.2 − 8.8 ≈ <b>−23 kJ/mol</b> → 평형(ΔG = 0)과 거리가 멀다 → 사실상 한 방향(비가역).',
        '평형 근처 반응은 효소가 양쪽으로 왔다 갔다 해서 조절해도 효과가 작다. 반면 평형에서 먼 반응은 효소 활성(속도)이 곧 경로 전체의 흐름을 결정 → PFK-1은 해당과정의 <b>핵심 조절 효소</b>(“병목의 밸브”)가 될 수 있다.'
    ) +
    fig(logaxis([(0.029, '실제 Q = 0.029', C['orange']), (308, '평형 K = 308', C['navy'])], -3, 4, height=110, label='약 1만 배 차이 → 강하게 정반응'),
        'Q와 K 사이가 멀수록 ΔG가 더 음수 = 평형에서 먼 “일방통행” 반응') +
    tip('평형 근처 반응 = 양방향 도로, 평형에서 먼 반응 = 일방통행 도로. 교통을 통제(조절)하려면 일방통행 도로의 신호등(PFK-1)을 조작하는 게 효과적이야.'))

add(id='P35', kind='PROBLEM', num='35',
    en_title='Are All Metabolic Reactions at Equilibrium?', ko_title='모든 대사 반응은 평형 상태일까?', slides='강의 슬라이드 28, 54', level=3,
    en='''<p><b>a.</b> Phosphoenolpyruvate (PEP) is one of the two phosphoryl group donors in the synthesis of ATP during glycolysis. In human erythrocytes, the steady-state concentration of ATP is 2.24 m<span class="sc">M</span>, that of ADP is 0.25 m<span class="sc">M</span>, and that of pyruvate is 0.051 m<span class="sc">M</span>. Calculate the concentration of PEP at 25 °C, assuming that the pyruvate kinase reaction (see Fig. 13-13) is at equilibrium in the cell.<br>
<b>b.</b> The physiological concentration of PEP in human erythrocytes is 0.023 m<span class="sc">M</span>. Compare this with the value obtained in (a). Explain the significance of this difference.</p>''',
    ko='''<p><b>a.</b> 포스포엔올피루브산(PEP)은 해당과정에서 ATP 합성에 인산기를 주는 두 공여체 중 하나다. 사람 적혈구에서 정상 상태 농도는 ATP 2.24 mM, ADP 0.25 mM, 피루브산 0.051 mM이다. 피루브산 키나아제 반응(그림 13-13 참고)이 세포 안에서 평형에 있다고 가정하고, 25 °C에서 PEP의 농도를 계산하라.<br>
<b>b.</b> 사람 적혈구의 실제 PEP 농도는 0.023 mM이다. (a)에서 구한 값과 비교하고, 이 차이의 의미를 설명하라.</p>''',
    blank=50,
    answer=chips('a. 평형이라면 [PEP] ≈ <b>1.4×10<sup>−9</sup> M</b> (1.4 nM)', 'b. 실제(2.3×10<sup>−5</sup> M)는 약 <b>1.6×10<sup>4</sup>배</b> 많다 → 평형이 <b>아니다</b> (평형에서 먼 비가역·조절 단계)'),
    explain=key('피루브산 키나아제: PEP + ADP → 피루브산 + ATP. ΔG′°는 “PEP 인산 떼기(−61.9) + ADP에 붙이기(+30.5)”.') +
    steps(f'{G0} = −61.9 + 30.5 = −31.4 kJ/mol → {K} = e<sup>31.4/2.478</sup> = e<sup>12.7</sup> ≈ <b>3.2×10<sup>5</sup></b>',
          eq(f'{K} = {F("[피루브산][ATP]", "[PEP][ADP]")} → [PEP] = {F("[피루브산][ATP]", f"{K}[ADP]")} = {F("(0.051)(2.24)", "(3.2×10<sup>5</sup>)(0.25)")} mM') +
          '= 1.4×10<sup>−6</sup> mM = <span class="hl">1.4×10<sup>−9</sup> M</span>',
          '<b>b.</b> 실제 0.023 mM ÷ 평형값 1.4×10<sup>−6</sup> mM ≈ <b>1.6×10<sup>4</sup></b>. PEP가 평형보다 훨씬 많다 = 반응이 평형에서 멀다 → 실제 ΔG가 크게 음수 → 사실상 <b>비가역</b>. 이런 반응이 대사 경로의 방향을 정하고 조절 지점이 된다.') +
    fig(logaxis([(1.4e-9, '평형이라면 1.4 nM', C['blue']), (2.3e-5, '실제 23 μM', C['orange'])], -10, -3, height=110, label='[PEP] (M)'),
        '실제 농도와 평형 농도의 거리 = 반응이 평형에서 얼마나 먼가') +
    fig(phos_ladder(hl=('PEP', 'ATP'), flows=[('PEP', 'ATP', 'PK')], height=250), 'PEP는 사다리 꼭대기(−61.9): ADP에 인산을 줘 ATP를 만들기 충분') +
    tip('세포는 평형 상태가 아니라 “<b>동적 정상 상태</b>”야. 물이 계속 들어오고 나가서 수위가 일정한 욕조처럼, 농도는 일정하지만 평형은 아니야. 평형에 도달한다는 건 흐름이 멈춘다는 뜻 = 죽음.', '큰 그림'))
