# -*- coding: utf-8 -*-
from helpers import *
import math

ITEMS = []


def add(**kw):
    ITEMS.append(kw)


# =====================================================================
# 공용 그림
# =====================================================================
def phos_ladder(hl=(), flows=(), width=520, height=300, extra=()):
    """인산 화합물 가수분해 ΔG′° 사다리 (그림 13-19 스타일)"""
    data = [('PEP (포스포엔올피루브산)', -61.9), ('1,3-BPG (1,3-이인산글리세르산)', -49.3),
            ('PCr (포스포크레아틴)', -43.0), ('ATP → ADP + Pᵢ', -30.5),
            ('PPᵢ → 2Pᵢ', -19.2), ('F6P (과당 6-인산)', -15.9), ('G6P (포도당 6-인산)', -13.8),
            ('글리세롤 3-인산', -9.2)] + list(extra)
    top, bot = 28, height - 20
    lo, hi = -66, -5
    def Y(v):
        return top + (v - lo) / (hi - lo) * (bot - top)
    x0 = 92
    b = arrowdef('pl', C['orange'])
    b += (f'<defs><linearGradient id="pg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fde68a"/>'
          f'<stop offset="1" stop-color="#bfdbfe"/></linearGradient></defs>')
    b += f'<rect x="{x0-8}" y="{top}" width="16" height="{bot-top}" rx="8" fill="url(#pg)"/>'
    b += T(x0, top - 12, 'ΔG′° of hydrolysis (kJ/mol)', 10, C['gray'], weight=700)
    b += T(40, top + 20, '고에너지', 11, C['orange'], weight=700)
    b += T(40, top + 34, '(인산 잘 줌)', 9.5, C['orange'])
    b += T(40, bot - 18, '저에너지', 11, C['blue'], weight=700)
    b += T(40, bot - 4, '(인산 받음)', 9.5, C['blue'])
    yat = Y(-25)
    b += f'<line x1="{x0-14}" y1="{yat}" x2="{width-10}" y2="{yat}" stroke="{C["gray"]}" stroke-dasharray="4 4" stroke-width="0.8"/>'
    pos = {}
    used = []
    for lab, v in sorted(data, key=lambda e: e[1]):
        y = Y(v)
        ty = y
        for u in used:
            if abs(ty - u) < 16:
                ty = u + 16
        used.append(ty)
        pos[lab] = y
        h = any(lab.startswith(x) for x in hl)
        col = C['orange'] if h else C['ink']
        b += f'<circle cx="{x0}" cy="{y}" r="{5 if h else 3.5}" fill="{col}"/>'
        b += f'<line x1="{x0+5}" y1="{y}" x2="{x0+12}" y2="{ty}" stroke="{col}" stroke-width="0.8"/>'
        b += T(x0 + 14, ty + 4, f'{v:.1f}'.replace('-', '−'), 11, col, 'start', 700 if h else 400, family='JetBrains Mono')
        b += T(x0 + 62, ty + 4, lab, 11.5, col, 'start', 700 if h else 400)
    for i, (a, c, t) in enumerate(flows):
        ya = [pos[k] for k in pos if k.startswith(a)][0]
        yc = [pos[k] for k in pos if k.startswith(c)][0]
        xx = width - 30 - i * 36
        b += (f'<path d="M{xx-12},{ya} L{xx},{ya} L{xx},{yc} L{xx-12},{yc}" fill="none" '
              f'stroke="{C["orange"]}" stroke-width="2.2" marker-end="url(#pl)"/>')
        b += T(xx - 6, (ya + yc) / 2 + 4, t, 10.5, C['orange'], 'end', 700)
    return svg(width, height, b)


def plot_p10():
    W, H = 520, 300
    L, R, Tp, B = 62, 490, 20, 250
    xlo, xhi, ylo, yhi = -8.5, 0.5, -52, -28
    def X(v): return L + (v - xlo) / (xhi - xlo) * (R - L)
    def Y(v): return Tp + (yhi - v) / (yhi - ylo) * (B - Tp)
    b = ''
    for gy in range(-50, -27, 5):
        b += f'<line x1="{L}" y1="{Y(gy)}" x2="{R}" y2="{Y(gy)}" stroke="#e5e7eb"/>'
        b += T(L - 8, Y(gy) + 4, str(gy).replace('-', '−'), 10, C['gray'], 'end', family='JetBrains Mono')
    for gx in range(-8, 1, 2):
        b += f'<line x1="{X(gx)}" y1="{Tp}" x2="{X(gx)}" y2="{B}" stroke="#f1f5f9"/>'
        b += T(X(gx), B + 16, str(gx).replace('-', '−'), 10, C['gray'], family='JetBrains Mono')
    b += f'<line x1="{L}" y1="{B}" x2="{R}" y2="{B}" stroke="{C["gray"]}"/>'
    b += f'<line x1="{L}" y1="{Tp}" x2="{L}" y2="{B}" stroke="{C["gray"]}"/>'
    b += T((L + R) / 2, B + 34, 'ln Q   ( Q = [ADP][Pᵢ] / [ATP] )', 11, C['ink'], weight=700)
    b += f'<text x="16" y="{(Tp+B)/2}" font-size="11" font-weight="700" fill="{C["ink"]}" transform="rotate(-90 16 {(Tp+B)/2})" text-anchor="middle">ΔG (kJ/mol)</text>'
    b += f'<line x1="{X(-8.5)}" y1="{Y(-30.5+2.478*-8.5)}" x2="{X(0.5)}" y2="{Y(-30.5+2.478*0.5)}" stroke="{C["blue"]}" stroke-width="2.2"/>'
    pts = [(-7.82, -49.9, '① 25', 'end', -8, -6), (-4.72, -42.2, '② 1.4', 'end', -8, -6), (-3.00, -37.9, '⑤ 0.2', 'start', 8, 16),
           (-2.83, -37.5, '③ 0.24', 'end', -8, -6), (-0.99, -32.9, '④ 0.04', 'start', 8, 16)]
    for x, y, r, anc, dx, dy in pts:
        b += f'<circle cx="{X(x)}" cy="{Y(y)}" r="5.5" fill="{C["orange"]}" stroke="white" stroke-width="1.5"/>'
        b += T(X(x) + dx, Y(y) + dy, f'{r}', 10.5, C['orange'], anc, 700)
    b += T(R - 4, B - 8, '주황 숫자 = [ATP]/[ADP] 비', 10, C['orange'], 'end')
    b += T(X(-7.6), Y(-31.5), '기울기 = RT = 2.48 kJ/mol', 11, C['blue'], 'start', 700)
    b += T(X(-7.6), Y(-33.5), 'ln Q = 0 일 때 ΔG = ΔG′° = −30.5', 11, C['blue'], 'start')
    b += arrowdef('p10', C['red'])
    b += f'<line x1="{X(-1.4)}" y1="{Y(-45)}" x2="{X(-6.6)}" y2="{Y(-45)}" stroke="{C["red"]}" stroke-width="2" marker-end="url(#p10)"/>'
    b += T(X(-4), Y(-46.8) + 16, 'ATP/ADP ↑ → ΔG 더 음수 = ATP 1개의 “힘”↑', 11, C['red'], weight=700)
    return svg(W, H, b)


def egg_svg():
    W, H = 520, 220
    b = arrowdef('eg', C['orange']) + arrowdef('eg2', C['blue'])
    b += f'<rect x="20" y="16" width="480" height="190" rx="18" fill="#eff6ff" stroke="#93c5fd" stroke-dasharray="6 4"/>'
    b += T(40, 38, '주변 (surroundings) = 인큐베이터 속 공기·열', 11.5, C['blue'], 'start', 700)
    b += '<ellipse cx="170" cy="122" rx="62" ry="78" fill="#fffbeb" stroke="#f59e0b" stroke-width="2"/>'
    b += T(170, 104, '계 (system)', 12, C['orange'], weight=700)
    b += T(170, 122, '= 달걀', 12, C['orange'], weight=700)
    b += T(170, 146, '영양분 → 병아리', 10.5, C['ink'])
    b += T(170, 162, '(무질서 → 질서)', 10.5, C['ink'])
    b += f'<line x1="236" y1="92" x2="330" y2="72" stroke="{C["orange"]}" stroke-width="2.2" marker-end="url(#eg)"/>'
    b += f'<line x1="238" y1="122" x2="330" y2="122" stroke="{C["orange"]}" stroke-width="2.2" marker-end="url(#eg)"/>'
    b += f'<line x1="236" y1="152" x2="330" y2="172" stroke="{C["orange"]}" stroke-width="2.2" marker-end="url(#eg)"/>'
    b += T(340, 76, '열 (heat) 방출', 11.5, C['orange'], 'start', 700)
    b += T(340, 126, 'CO₂ · H₂O 방출', 11.5, C['orange'], 'start', 700)
    b += T(340, 176, '(작은 분자 여러 개 = 무질서↑)', 10.5, C['orange'], 'start')
    b += f'<line x1="330" y1="102" x2="240" y2="108" stroke="{C["blue"]}" stroke-width="1.8" marker-end="url(#eg2)"/>'
    b += T(340, 100, 'O₂ 흡수', 11, C['blue'], 'start', 700)
    return svg(W, H, b)


# =====================================================================
# WORKED EXAMPLES
# =====================================================================
add(id='WE1', kind='WORKED EXAMPLE', num='13-1', section='본문 예제',
    en_title='Calculation of ΔG′°', ko_title='ΔG′° 계산하기', slides='강의 슬라이드 17–18', level=1,
    en=f'''<p>Calculate the standard free-energy change of the reaction catalyzed by the enzyme phosphoglucomutase,</p>
{rx('Glucose 1-phosphate', 'glucose 6-phosphate')}
<p>given that, starting with 20 m<span class="sc">M</span> glucose 1-phosphate and no glucose 6-phosphate, the final equilibrium mixture at 25 °C and pH 7.0 contains 1.0 m<span class="sc">M</span> glucose 1-phosphate and 19 m<span class="sc">M</span> glucose 6-phosphate. Does the reaction in the direction of glucose 6-phosphate formation proceed with a loss or a gain of free energy?</p>''',
    ko=f'''<p>포스포글루코뮤테이스(phosphoglucomutase) 효소가 촉매하는 아래 반응의 <b>표준 자유에너지 변화</b>를 계산하라.</p>
{rx('포도당 1-인산', '포도당 6-인산')}
<p>포도당 1-인산 20 mM, 포도당 6-인산 0에서 시작했더니, 25 °C·pH 7.0에서 최종 평형 혼합물에 포도당 1-인산 1.0 mM, 포도당 6-인산 19 mM이 들어 있었다. 포도당 6-인산이 만들어지는 방향의 반응은 자유에너지를 <b>잃는가(방출)</b>, <b>얻는가(흡수)</b>?</p>''',
    blank=45,
    answer=chips(f'{K} = 19', f'{G0} ≈ −7.3 kJ/mol', '자유에너지를 <b>잃는다</b>(방출) → 정반응 쪽이 유리'),
    explain=key(f'평형 농도를 알면 → {K}를 구하고 → {G0} = −RT ln {K}에 넣는다. <b>딱 두 단계.</b>') +
    steps(
        f'<b>{K} 구하기</b> — 평형에서의 (생성물 ÷ 반응물):' +
        eq(f'{K} = {F("[포도당 6-인산]<sub>eq</sub>", "[포도당 1-인산]<sub>eq</sub>")} = {F("19 mM", "1.0 mM")} = 19'),
        f'<b>{G0} 계산</b> — R = 8.315 J/mol·K, T = 298 K:' +
        align([(G0, '−RT ln ' + K),
               ('', '−(8.315 J/mol·K)(298 K)(ln 19)'),
               ('', '−(2478 J/mol)(2.94) = −7290 J/mol ≈ <span class="hl">−7.3 kJ/mol</span>')]),
        f'<b>해석</b> — {G0} &lt; 0 → 포도당 6-인산 쪽으로 가면서 자유에너지를 <b>잃는다(방출)</b>. 거꾸로(6-인산 → 1-인산)는 크기는 같고 부호만 반대인 +7.3 kJ/mol.'
    ) +
    fig(bars([('포도당 1-인산', 1.0, '#93c5fd', '1.0 mM'), ('포도당 6-인산', 19, C['orange'], '19 mM  ← 19배 많음')],
             height=90), '평형에서 생성물(6-인산)이 19배 많다 = 생성물 쪽이 “더 편안한(낮은 에너지)” 상태') +
    tip('평형은 “시소가 멈춘 위치”야. 시소가 생성물 쪽으로 19배 기울어서 멈췄다면, 생성물 쪽이 더 낮은(편한) 자리라는 뜻 → K′<sub>eq</sub> &gt; 1 ⇔ ΔG′° &lt; 0.') +
    warn('R은 <b>J</b> 단위(8.315 J/mol·K)라 답이 J/mol로 나온다. 마지막에 ÷1000 해서 kJ/mol로 바꾸는 걸 잊지 말자.'))

add(id='WE2', kind='WORKED EXAMPLE', num='13-2', section='본문 예제',
    en_title='Calculation of ΔG<sub>p</sub>', ko_title='세포 속 ATP 가수분해의 실제 자유에너지 ΔG<sub>p</sub>', slides='강의 슬라이드 14', level=2,
    en=f'''<p>Calculate the actual free energy of hydrolysis of ATP, ΔG<sub>p</sub>, in human erythrocytes. The standard free energy of hydrolysis of ATP is −30.5 kJ/mol, and the concentrations of ATP, ADP, and P<sub>i</sub> in erythrocytes are as shown in Table 13-5. Assume that the pH is 7.0 and the temperature is 37 °C (human body temperature). What does this reveal about the amount of energy required to synthesize ATP under the same cellular conditions?</p>
<p class="small">Table 13-5 (human erythrocyte): [ATP] = 2.25 m<span class="sc">M</span>, [ADP] = 0.25 m<span class="sc">M</span>, [P<sub>i</sub>] = 1.65 m<span class="sc">M</span></p>''',
    ko=f'''<p>사람 적혈구에서 ATP 가수분해의 <b>실제</b> 자유에너지 ΔG<sub>p</sub>를 계산하라. ATP 가수분해의 표준 자유에너지는 −30.5 kJ/mol이고, 적혈구의 ATP·ADP·P<sub>i</sub> 농도는 표 13-5와 같다. pH는 7.0, 온도는 37 °C(사람 체온)로 가정한다. 이 결과는 같은 세포 조건에서 ATP를 <b>합성</b>하는 데 필요한 에너지에 대해 무엇을 알려 주는가?</p>
<p class="small">표 13-5 (사람 적혈구): [ATP] = 2.25 mM, [ADP] = 0.25 mM, [P<sub>i</sub>] = 1.65 mM</p>''',
    blank=55,
    answer=chips('ΔG<sub>p</sub> ≈ <b>−52 kJ/mol</b> (표준값 −30.5보다 훨씬 큼)', '같은 조건에서 ATP 합성엔 <b>+52 kJ/mol</b>이 필요'),
    explain=key(f'실제 {DG} = {G0} + RT ln Q.  Q = “지금” 농도비 = {F("[ADP][P<sub>i</sub>]", "[ATP]")}  (물은 용매라 식에 넣지 않는다)') +
    steps(
        '<b>농도를 M(mol/L)로</b> 바꾼다: ATP 2.25×10<sup>−3</sup>, ADP 0.25×10<sup>−3</sup>, P<sub>i</sub> 1.65×10<sup>−3</sup> M',
        '<b>Q 계산</b>' + eq(f'Q = {F("(0.25×10<sup>−3</sup>)(1.65×10<sup>−3</sup>)", "2.25×10<sup>−3</sup>")} = 1.8×10<sup>−4</sup>'),
        '<b>RT (37 °C = 310 K)</b> = 8.315 × 310 = 2578 J/mol = 2.58 kJ/mol,  ln(1.8×10<sup>−4</sup>) = −8.6',
        '<b>대입</b>' + align([('ΔG<sub>p</sub>', '−30.5 + (2.58)(−8.6)'), ('', '−30.5 − 22 = <span class="hl">−52 kJ/mol</span>')]),
        '<b>합성은 가수분해의 정반대</b> → 부호만 바꿔 <b>+52 kJ/mol</b>이 들어가야 ATP 1몰을 만든다.'
    ) +
    fig(bars([('표준 조건 (1 M)', 30.5, '#93c5fd', '−30.5 kJ/mol'), ('적혈구 속 (실제)', 52, C['orange'], '−52 kJ/mol')],
             height=90), 'ATP 1개를 깼을 때 나오는 에너지: 세포 속이 약 1.7배 더 크다') +
    tip('세포는 ADP·P<sub>i</sub>(생성물)를 아주 적게, ATP를 많게 유지해. 생성물 자리가 텅 비어 있으니 반응이 “더 가고 싶어” 한다 — 르샤틀리에 원리. 그래서 Q가 작을수록(ln Q가 음수) ΔG가 더 음수가 된다.'))

add(id='WE3', kind='WORKED EXAMPLE', num='13-3', section='본문 예제',
    en_title='Calculation of ΔG′° and ΔG of a Redox Reaction', ko_title='산화-환원 반응의 ΔG′°와 ΔG 계산', slides='강의 슬라이드 44–46', level=2,
    en=f'''<p>Calculate the standard free-energy change, ΔG′°, for the reaction in which acetaldehyde is reduced by the biological electron carrier NADH:</p>
{rx('Acetaldehyde + NADH + H<sup>+</sup>', 'ethanol + NAD<sup>+</sup>', rev=False)}
<p>Then calculate the actual free-energy change, ΔG, when [acetaldehyde] and [NADH] are 1.00 <span class="sc">M</span>, and [ethanol] and [NAD<sup>+</sup>] are 0.100 <span class="sc">M</span>. The relevant half-reactions and their E′° values are</p>
<p class="c">1. Acetaldehyde + 2H<sup>+</sup> + 2e<sup>−</sup> → ethanol &nbsp;&nbsp; E′° = −0.197 V<br>2. NAD<sup>+</sup> + 2H<sup>+</sup> + 2e<sup>−</sup> → NADH + H<sup>+</sup> &nbsp;&nbsp; E′° = −0.320 V</p>
<p>Remember that, by convention, ΔE′° is E′° of the electron acceptor minus E′° of the electron donor.</p>''',
    ko=f'''<p>생물학적 전자 운반체인 NADH가 아세트알데하이드를 <b>환원</b>시키는 아래 반응의 표준 자유에너지 변화 ΔG′°를 계산하라.</p>
{rx('아세트알데하이드 + NADH + H<sup>+</sup>', '에탄올 + NAD<sup>+</sup>', rev=False)}
<p>이어서 [아세트알데하이드]와 [NADH]가 1.00 M, [에탄올]과 [NAD<sup>+</sup>]가 0.100 M일 때의 <b>실제</b> 자유에너지 변화 ΔG를 계산하라. 관련 반쪽 반응과 E′° 값은 위와 같다(① 아세트알데하이드/에탄올 −0.197 V, ② NAD<sup>+</sup>/NADH −0.320 V). 관례상 ΔE′° = (전자 <b>받는</b> 쪽의 E′°) − (전자 <b>주는</b> 쪽의 E′°)임을 기억하라.</p>''',
    blank=55,
    answer=chips(f'{DE0} = +0.123 V', f'{G0} ≈ <b>−23.7 kJ/mol</b>', f'{DG} ≈ <b>−35.1 kJ/mol</b>'),
    explain=key(f'산화-환원 문제의 3종 세트: ① 누가 전자를 받고 주나? ② {DE0} = E′°<sub>받는 쪽</sub> − E′°<sub>주는 쪽</sub> ③ {G0} = −nF{DE0}') +
    fig(ladder([('NAD⁺/NADH', -0.320), ('아세트알데하이드/에탄올', -0.197)], -0.36, -0.16,
               hl=('NAD⁺/NADH', '아세트알데하이드/에탄올'), flows=[('NAD⁺/NADH', '아세트알데하이드/에탄올', '2e⁻')], height=170),
        '전자는 E′°가 낮은(더 음수) 쪽 → 높은 쪽으로 흐른다: NADH → 아세트알데하이드') +
    steps(
        '<b>역할 정하기</b> — 아세트알데하이드는 에탄올이 되며 전자를 <b>받는다</b>(수용체, −0.197 V). NADH는 NAD<sup>+</sup>가 되며 전자를 <b>준다</b>(공여체, −0.320 V). 전자 수 n = 2.',
        f'<b>{DE0}</b> = −0.197 − (−0.320) = <b>+0.123 V</b>  (양수 → 자발적)',
        f'<b>{G0}</b> = −nF{DE0} = −2 × (96.5 kJ/V·mol) × 0.123 V = <span class="hl">−23.7 kJ/mol</span>',
        '<b>실제 ΔG</b>' + eq(f'Q = {F("[에탄올][NAD<sup>+</sup>]", "[아세트알데하이드][NADH]")} = {F("(0.100)(0.100)", "(1.00)(1.00)")} = 0.0100') +
        align([(DG, f'{G0} + RT ln Q = −23.7 + (2.48)(ln 0.0100)'), ('', '−23.7 + (2.48)(−4.61) = −23.7 − 11.4 = <span class="hl">−35.1 kJ/mol</span>')])
    ) +
    warn('표에서는 모든 반쪽 반응이 “환원” 방향으로 적혀 있어. 실제로는 한쪽이 거꾸로(산화) 가지만, <b>E′°의 부호를 바꾸지 않는다</b>. 그냥 “받는 쪽 − 주는 쪽”으로 빼면 끝.') +
    tip('E′°는 “전자 욕심”이야. 욕심이 더 큰 쪽(더 +)이 전자를 뺏어 간다. 욕심 차이(ΔE′°)가 클수록 방출되는 에너지(−ΔG′°)가 크다.', '직관'))

# =====================================================================
# PROBLEMS 1 – 15
# =====================================================================
add(id='P1', kind='PROBLEM', num='1', section='연습문제',
    en_title='Entropy Changes during Egg Development', ko_title='달걀이 발생할 때의 엔트로피 변화', slides='강의 슬라이드 15', level=1,
    en='<p>Consider a system consisting of an egg in an incubator. The white and yolk of the egg contain proteins, carbohydrates, and lipids. If fertilized, the egg transforms from a single cell to a complex organism. Discuss this irreversible process in terms of the entropy changes in the system and surroundings. Be sure that you first clearly define the system and surroundings.</p>',
    ko='<p>인큐베이터 속 달걀로 이루어진 계를 생각해 보자. 달걀의 흰자와 노른자에는 단백질, 탄수화물, 지질이 들어 있다. 수정된 달걀은 단 하나의 세포에서 복잡한 생물체로 변한다. 이 <b>비가역</b> 과정을 계와 주변의 <b>엔트로피 변화</b> 관점에서 논하라. 먼저 무엇이 계이고 무엇이 주변인지 분명히 정의하라.</p>',
    blank=45,
    answer=chips('계 = 달걀 / 주변 = 인큐베이터(공기·열)', '계의 엔트로피 <b>감소</b> (질서↑)', '주변의 엔트로피 <b>크게 증가</b>', '전체(우주) 엔트로피 <b>증가</b> → 제2법칙 OK'),
    explain=key('생명체가 스스로 질서를 만들 때는, 그 대가로 <b>주변을 더 크게 어지럽힌다</b>. 그래서 전체 엔트로피는 항상 늘어난다.') +
    fig(egg_svg(), '계(달걀)는 정돈되지만, 주변으로 열과 작은 분자들이 쏟아져 나간다') +
    steps(
        '<b>계 정의</b>: 달걀(껍데기 안 전부). <b>주변</b>: 달걀을 둘러싼 인큐베이터 속 공기와 열. 둘을 합치면 “우주”.',
        '<b>계의 엔트로피 ↓</b>: 흰자·노른자 속 영양분(단백질·지방·탄수화물)이 뼈·근육·깃털 같은 <b>고도로 조직된 구조</b>로 바뀐다 → 무질서도 감소.',
        '<b>주변의 엔트로피 ↑↑</b>: 이 일을 하려고 달걀은 영양분 일부를 O<sub>2</sub>로 산화(태워)해 <b>CO<sub>2</sub>·H<sub>2</sub>O</b>(큰 분자 1개 → 작은 분자 여러 개)와 <b>열</b>을 내보낸다. 흩어진 기체 분자와 열은 주변의 무질서를 크게 늘린다.',
        '<b>결론</b>: ΔS<sub>계</sub> &lt; 0 이지만 ΔS<sub>주변</sub>이 훨씬 커서 ΔS<sub>우주</sub> = ΔS<sub>계</sub> + ΔS<sub>주변</sub> &gt; 0. 그래서 이 과정은 저절로 한 방향으로만 일어나는 <b>비가역</b> 과정이다(병아리가 다시 달걀로 돌아가지 않는다).'
    ) +
    tip('방 청소를 떠올려 봐. 방(계)은 깨끗해지지만, 너는 땀을 흘리고 열을 내고 밥(영양분)을 태웠어. 방 + 너 + 공기 전체로 보면 무질서는 오히려 늘었다.'))

add(id='P2', kind='PROBLEM', num='2', section='연습문제',
    en_title='Calculation of ΔG′° from an Equilibrium Constant', ko_title='평형상수로부터 ΔG′° 계산하기', slides='강의 슬라이드 17–18', level=1,
    en=f'''<p>Calculate the standard free-energy change for each of the three metabolically important enzyme-catalyzed reactions, using the equilibrium constants given for the reactions at 25 °C and pH 7.0.</p>
<div class="rxlist">
<div><b>a.</b> {rx('Glutamate + oxaloacetate', 'aspartate + α-ketoglutarate', 'aspartate aminotransferase', extra=f'{K} = 6.8')}</div>
<div><b>b.</b> {rx('Dihydroxyacetone phosphate', 'glyceraldehyde 3-phosphate', 'triose phosphate isomerase', extra=f'{K} = 0.0475')}</div>
<div><b>c.</b> {rx('Fructose 6-phosphate + ATP', 'fructose 1,6-bisphosphate + ADP', 'phosphofructokinase', extra=f'{K} = 254')}</div></div>''',
    ko=f'''<p>대사에서 중요한 세 가지 효소 촉매 반응에 대해, 25 °C·pH 7.0에서 주어진 평형상수를 이용하여 각각의 <b>표준 자유에너지 변화</b>를 계산하라.</p>
<p class="small">a. 글루탐산 + 옥살로아세트산 ⇌ 아스파르트산 + α-케토글루타르산 (아스파르트산 아미노기전달효소), {K} = 6.8<br>
b. 다이하이드록시아세톤 인산 ⇌ 글리세르알데하이드 3-인산 (삼탄당 인산 이성질화효소), {K} = 0.0475<br>
c. 과당 6-인산 + ATP ⇌ 과당 1,6-이인산 + ADP (포스포프룩토키나아제), {K} = 254</p>''',
    blank=45,
    answer=chips('a. <b>−4.7 kJ/mol</b>', 'b. <b>+7.6 kJ/mol</b>', 'c. <b>−13.7 kJ/mol</b>'),
    explain=key(f'{G0} = −RT ln {K},  25 °C에서 RT = 2.478 kJ/mol.  K &gt; 1이면 음수, K &lt; 1이면 양수.') +
    table(['', K, f'ln {K}', f'{G0} = −2.478 × ln K'],
          [['a', '6.8', '1.92', '<b>−4.7 kJ/mol</b>'], ['b', '0.0475', '−3.05', '<b>+7.6 kJ/mol</b>'], ['c', '254', '5.54', '<b>−13.7 kJ/mol</b>']]) +
    fig(logaxis([(0.0475, 'b (0.0475)', C['blue']), (6.8, 'a (6.8)', C['green']), (254, 'c (254)', C['orange'])], -2, 3,
                center=1, center_lab='K = 1 ⇔ ΔG′° = 0', height=125),
        '왼쪽(K&lt;1): ΔG′° &gt; 0, 역방향 우세  |  오른쪽(K&gt;1): ΔG′° &lt; 0, 정방향 우세') +
    tip('<b>10배 규칙</b>: 25 °C에서 K가 10배 커질 때마다 ΔG′°는 약 <b>−5.7 kJ/mol</b>씩 변한다 (2.478 × ln10 = 5.7). 예: c는 K ≈ 10<sup>2.4</sup> → −5.7 × 2.4 ≈ −13.7 ✔. 검산할 때 아주 유용해!', '꿀팁'))

add(id='P3', kind='PROBLEM', num='3', section='연습문제',
    en_title='Calculation of the Equilibrium Constant from ΔG′°', ko_title='ΔG′°로부터 평형상수 계산하기', slides='강의 슬라이드 17–19', level=1,
    en=f'''<p>Calculate the equilibrium constant {K} for each of the three reactions at pH 7.0 and 25 °C, using the ΔG′° values in Table 13-4.</p>
<div class="rxlist">
<div><b>a.</b> {rx('Glucose 6-phosphate + H<sub>2</sub>O', 'glucose + P<sub>i</sub>', 'glucose 6-phosphatase')}</div>
<div><b>b.</b> {rx('Lactose + H<sub>2</sub>O', 'glucose + galactose', 'β-galactosidase')}</div>
<div><b>c.</b> {rx('Malate', 'fumarate + H<sub>2</sub>O', 'fumarase')}</div></div>''',
    ko=f'''<p>표 13-4의 ΔG′° 값을 이용하여, pH 7.0·25 °C에서 다음 세 반응의 평형상수 {K}를 각각 계산하라.</p>
<p class="small">a. 포도당 6-인산 + H<sub>2</sub>O ⇌ 포도당 + P<sub>i</sub> (포도당 6-인산가수분해효소) — 표 13-4: ΔG′° = −13.8 kJ/mol<br>
b. 젖당 + H<sub>2</sub>O ⇌ 포도당 + 갈락토스 (β-갈락토시데이스) — 표 13-4: ΔG′° = −15.9 kJ/mol<br>
c. 말산 ⇌ 푸마르산 + H<sub>2</sub>O (푸마레이스) — 표 13-4: ΔG′° = +3.1 kJ/mol</p>''',
    blank=45,
    answer=chips('a. <b>≈ 2.6 × 10²</b> (262)', 'b. <b>≈ 6.1 × 10²</b> (612)', 'c. <b>≈ 0.29</b>'),
    explain=key(f'앞 문제의 식을 거꾸로: {K} = e<sup>−ΔG′°/RT</sup>  (RT = 2.478 kJ/mol)') +
    table([f'', f'{G0} (kJ/mol)', '−ΔG′°/RT', K],
          [['a', '−13.8', '+5.57', '<b>262</b>'], ['b', '−15.9', '+6.42', '<b>612</b>'], ['c', '+3.1', '−1.25', '<b>0.29</b>']]) +
    steps('a 예시: −(−13.8) ÷ 2.478 = 5.57 → e<sup>5.57</sup> = 262. (계산기: <b>e<sup>x</sup></b> 버튼, 10<sup>x</sup> 아님!)',
          '가수분해 반응의 H<sub>2</sub>O는 K 식에 넣지 않는다 (물은 용매라 농도가 사실상 일정; ΔG′° 안에 이미 포함).',
          'c는 ΔG′°가 +라서 K &lt; 1 → 1 M에서 시작하면 말산 쪽(역방향)이 우세. 하지만 세포에서 푸마르산을 계속 치워 주면 정방향으로도 잘 간다(구연산 회로).') +
    tip('<b>검산</b>: 10배 규칙(5.7 kJ/mol = 10배)으로 a는 13.8 ÷ 5.7 ≈ 2.4 → 10<sup>2.4</sup> ≈ 250. 비슷하면 정답!', '꿀팁'))

add(id='P4', kind='PROBLEM', num='4', section='연습문제',
    en_title='Experimental Determination of K′<sub>eq</sub> and ΔG′°', ko_title='실험으로 K′<sub>eq</sub>와 ΔG′° 구하기', slides='강의 슬라이드 17–18', level=1,
    en=f'''<p>Incubating a 0.1 <span class="sc">M</span> solution of glucose 1-phosphate at 25 °C with a catalytic amount of phosphoglucomutase transforms some of the glucose 1-phosphate to glucose 6-phosphate. At equilibrium, the concentrations of the reaction components are</p>
<p class="c">Glucose 1-phosphate ⇌ glucose 6-phosphate<br>4.5 × 10<sup>−3</sup> <span class="sc">M</span> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 9.6 × 10<sup>−2</sup> <span class="sc">M</span></p>
<p>Calculate {K} and ΔG′° for this reaction.</p>''',
    ko=f'''<p>0.1 M 포도당 1-인산 용액을 25 °C에서 소량(촉매량)의 포스포글루코뮤테이스와 함께 두면, 포도당 1-인산의 일부가 포도당 6-인산으로 바뀐다. 평형에서의 농도는 포도당 1-인산 4.5×10<sup>−3</sup> M, 포도당 6-인산 9.6×10<sup>−2</sup> M이다. 이 반응의 {K}와 ΔG′°를 계산하라.</p>''',
    blank=40,
    answer=chips(f'{K} ≈ <b>21</b>', f'{G0} ≈ <b>−7.6 kJ/mol</b>'),
    explain=key('예제 13-1과 똑같은 구조의 문제! 평형 농도 → K → ΔG′°') +
    steps(eq(f'{K} = {F("9.6×10<sup>−2</sup> M", "4.5×10<sup>−3</sup> M")} = 21.3'),
          align([(G0, '−(2.478 kJ/mol)(ln 21.3)'), ('', '−(2.478)(3.06) = <span class="hl">−7.6 kJ/mol</span>')]),
          '<b>검산</b>: 4.5×10<sup>−3</sup> + 9.6×10<sup>−2</sup> = 0.1005 M ≈ 처음 0.1 M ✔ (물질이 사라지지 않았다).') +
    tip('예제 13-1은 K = 19 → −7.3, 여기선 K = 21 → −7.6. 실험마다 조금씩 차이가 나지만 거의 같은 값이 나온다. ΔG′°는 반응마다 정해진 <b>상수</b>라는 뜻!', '포인트'))

add(id='P5', kind='PROBLEM', num='5', section='연습문제',
    en_title='Experimental Determination of ΔG′° for ATP Hydrolysis', ko_title='ATP 가수분해의 ΔG′°를 간접적으로 구하기', slides='강의 슬라이드 20 (가산성)', level=2,
    en=f'''<p>A direct measurement of the standard free-energy change associated with the hydrolysis of ATP is technically demanding because the minute amount of ATP remaining at equilibrium is difficult to measure accurately. The value of ΔG′° can be calculated indirectly, however, from the equilibrium constants of two other enzymatic reactions having less favorable equilibrium constants:</p>
<p class="c">Glucose 6-phosphate + H<sub>2</sub>O → glucose + P<sub>i</sub> &nbsp;&nbsp;&nbsp; {K} = 270<br>ATP + glucose → ADP + glucose 6-phosphate &nbsp;&nbsp;&nbsp; {K} = 890</p>
<p>Using this information for equilibrium constants determined at 25 °C, calculate the standard free energy of hydrolysis of ATP.</p>''',
    ko=f'''<p>ATP 가수분해의 표준 자유에너지 변화를 직접 측정하기는 기술적으로 어렵다. 평형에서 남아 있는 ATP가 극히 적어 정확히 재기 힘들기 때문이다. 그러나 평형상수가 덜 치우친 다른 두 효소 반응의 평형상수로부터 ΔG′°를 <b>간접적으로</b> 계산할 수 있다. (포도당 6-인산 + H<sub>2</sub>O → 포도당 + P<sub>i</sub>, {K} = 270 / ATP + 포도당 → ADP + 포도당 6-인산, {K} = 890) 25 °C에서 구한 이 평형상수들을 이용해 ATP 가수분해의 표준 자유에너지를 계산하라.</p>''',
    blank=50,
    answer=chips(f'{G0}<sub>ATP 가수분해</sub> ≈ <b>−30.7 kJ/mol</b> (교과서 값 −30.5와 거의 같음)'),
    explain=key('두 반응식을 <b>더하면</b> ATP 가수분해 식이 된다 → ΔG′°는 <b>더하고</b>, K는 <b>곱한다</b>.') +
    align([('(1)', 'G6P + H<sub>2</sub>O → 포도당 + P<sub>i</sub>', f'{G0}<sub>1</sub> = −2.478 ln 270 = −13.9'),
           ('(2)', 'ATP + 포도당 → ADP + G6P', f'{G0}<sub>2</sub> = −2.478 ln 890 = −16.8'),
           ('합', 'ATP + H<sub>2</sub>O → ADP + P<sub>i</sub>', f'{G0} = −13.9 + (−16.8) = <span class="hl">−30.7 kJ/mol</span>')], cls='sum') +
    '<p class="note">포도당과 G6P는 양쪽에 한 번씩 나와서 지워진다(공통 중간체).  또는 K = 270 × 890 = 2.4×10<sup>5</sup> → −2.478 × ln(2.4×10<sup>5</sup>) = −30.7 kJ/mol. 결과 동일!</p>' +
    fig(energy_steps([('ATP + H₂O + 포도당', 0, C['navy']), ('ADP + G6P + H₂O', -16.8, C['blue']), ('ADP + Pᵢ + 포도당', -30.7, C['orange'])], height=200),
        '계단 두 칸을 내려가면 총 −30.7: ATP 가수분해 한 번과 같은 높이 차') +
    tip('ln(a × b) = ln a + ln b 이므로 “K를 곱하는 것”과 “ΔG′°를 더하는 것”은 같은 말이야. 계단을 두 번 내려간 높이 = 한 번에 내려간 높이.', '왜 되나?'))

add(id='P6', kind='PROBLEM', num='6', section='연습문제',
    en_title='Difference between ΔG′° and ΔG', ko_title='ΔG′°와 ΔG의 차이', slides='강의 슬라이드 16–17, 20', level=1,
    en=f'''<p>Consider the interconversion shown, which occurs in glycolysis (Chapter 14):</p>
{rx('Fructose 6-phosphate', 'glucose 6-phosphate', extra=f'{K} = 1.97')}
<p>a. What is ΔG′° for the reaction ({K} measured at 25 °C)?<br>
b. If the concentration of fructose 6-phosphate is adjusted to 1.5 <span class="sc">M</span> and that of glucose 6-phosphate is adjusted to 0.50 <span class="sc">M</span>, what is ΔG?<br>
c. Why are ΔG′° and ΔG different?</p>''',
    ko=f'''<p>해당과정(14장)에서 일어나는 다음 상호 전환을 생각하자: 과당 6-인산 ⇌ 포도당 6-인산, {K} = 1.97</p>
<p>a. 이 반응의 ΔG′°는? ({K}는 25 °C에서 측정)<br>
b. 과당 6-인산 농도를 1.5 M, 포도당 6-인산 농도를 0.50 M로 맞추면 ΔG는?<br>
c. ΔG′°와 ΔG는 왜 다른가?</p>''',
    blank=50,
    answer=chips('a. <b>−1.7 kJ/mol</b>', 'b. <b>−4.4 kJ/mol</b>', 'c. ΔG′°는 “모두 1 M” 기준 상수, ΔG는 “지금 농도”를 반영한 변수'),
    explain=steps(
        f'<b>a.</b> {G0} = −2.478 × ln 1.97 = −2.478 × 0.678 = <span class="hl">−1.7 kJ/mol</span>',
        '<b>b.</b> Q = [생성물]/[반응물] = [G6P]/[F6P] = 0.50/1.5 = 0.333' +
        align([(DG, f'{G0} + RT ln Q = −1.7 + 2.478 × ln 0.333'), ('', '−1.7 + 2.478 × (−1.10) = −1.7 − 2.7 = <span class="hl">−4.4 kJ/mol</span>')]),
        '<b>c.</b> ΔG′°는 모든 물질이 1 M일 때(표준 상태)의 값으로 반응마다 정해진 <b>상수</b>. ΔG는 실제 농도(Q)가 들어가는 <b>변수</b>. 여기선 생성물이 반응물보다 적어서(Q = 0.33 &lt; K = 1.97) 반응이 표준 상태보다 더 “가고 싶어” 한다 → ΔG가 더 음수.'
    ) +
    fig(logaxis([(0.333, '지금 Q = 0.33', C['orange']), (1.97, '평형 K = 1.97', C['navy'])], -1, 1, height=110,
                label='Q가 K를 향해 → 정반응 진행'),
        'Q &lt; K 이면 ΔG &lt; 0 → 평형(K)을 향해 오른쪽(정반응)으로 간다') +
    tip('ΔG′°는 그 지역의 “평균 기후”, ΔG는 “오늘 날씨”. 평균적으로 따뜻한 지역도 오늘은 추울 수 있듯, ΔG′°가 양수인 반응도 농도 조건에 따라 ΔG는 음수가 될 수 있다.'))

add(id='P7', kind='PROBLEM', num='7', section='연습문제',
    en_title='Free Energy of Hydrolysis of CTP', ko_title='CTP 가수분해의 자유에너지', slides='강의 슬라이드 12–13', level=1,
    en=f'''<p>Compare the structure of the nucleoside triphosphate CTP with the structure of ATP.</p>
{img('ctp_atp.png', '62%')}
<p>Now predict the {K} and ΔG′° for the reaction:</p>
{rx('ATP + CDP', 'ADP + CTP', rev=False)}''',
    ko=f'''<p>뉴클레오사이드 삼인산인 CTP의 구조와 ATP의 구조를 비교하라(위 그림: 위 CTP, 아래 ATP). 그런 다음 다음 반응의 {K}와 ΔG′°를 예측하라: ATP + CDP → ADP + CTP</p>''',
    blank=35,
    answer=chips(f'{K} ≈ <b>1</b>', f'{G0} ≈ <b>0 kJ/mol</b>'),
    explain=key('ATP의 에너지는 <b>꼬리(인산 3개 사이의 무수물 결합)</b>에서 나온다. CTP와 ATP는 꼬리가 <b>완전히 똑같고</b>, 머리(염기: 사이토신 vs 아데닌)만 다르다.') +
    steps('ATP → ADP + P<sub>i</sub> : −30.5 kJ/mol (꼬리 끝 인산 하나 떼기)',
          'CDP + P<sub>i</sub> → CTP : +30.5 kJ/mol (똑같은 꼬리에 인산 하나 붙이기)',
          f'합: ATP + CDP → ADP + CTP : −30.5 + 30.5 ≈ <span class="hl">0 kJ/mol</span> → {K} = e<sup>0</sup> ≈ <b>1</b>') +
    tip('같은 물건(인산기)을 A 지갑에서 B 지갑으로 옮기는 것뿐이라 득실이 0이야. 실제로 세포에는 이 반응을 하는 <b>뉴클레오사이드 이인산 키나아제</b>가 있고, 교과서에도 “ATP + NDP ⇌ ADP + NTP, ΔG′° ≈ 0”으로 나온다.', '직관'))

add(id='P8', kind='PROBLEM', num='8', section='연습문제',
    en_title='Dependence of ΔG on pH', ko_title='ΔG의 pH 의존성', slides='강의 슬라이드 13, 54', level=2,
    en='<p>The free energy released by the hydrolysis of ATP under standard conditions is −30.5 kJ/mol. If ATP is hydrolyzed under standard conditions except at pH 5.0, is more or less free energy released? Explain.</p>',
    ko='<p>표준 조건에서 ATP 가수분해로 방출되는 자유에너지는 −30.5 kJ/mol이다. pH만 5.0이고 나머지는 표준 조건에서 ATP를 가수분해한다면, 방출되는 자유에너지는 더 많은가, 더 적은가? 설명하라.</p>',
    blank=35,
    answer=chips('<b>더 적게</b> 방출된다 (ΔG가 덜 음수가 됨)'),
    explain=key('pH 7에서 ATP 가수분해는 <b>H<sup>+</sup>를 생성물로 내놓는다</b>. pH 5 = H<sup>+</sup>가 이미 100배 많은 환경 → 생성물이 쌓여 있는 셈.') +
    eq('ATP<sup>4−</sup> + H<sub>2</sub>O → ADP<sup>3−</sup> + HPO<sub>4</sub><sup>2−</sup> + <span class="hl">H<sup>+</sup></span>') +
    steps('<b>르샤틀리에</b>: pH 5의 [H<sup>+</sup>] = 10<sup>−5</sup> M로 pH 7(10<sup>−7</sup> M)보다 100배 많다. 생성물(H<sup>+</sup>)이 많으면 반응은 덜 앞으로 가려 한다 → ΔG가 덜 음수.',
          '<b>전하 반발 감소</b>: 산성에서는 ATP의 인산기 일부에 H<sup>+</sup>가 붙어(양성자화) 음전하가 줄어든다. ATP를 불안정하게 만들던 “음전하끼리 밀어내기”가 약해지니, 깨질 때 풀려나는 에너지도 줄어든다.',
          '(대략적인 크기: H<sup>+</sup>가 1개 나온다고 치면 RT ln100 ≈ 2.48 × 4.6 ≈ 11 kJ/mol만큼 덜 유리해진다. 실제로는 pH 7에서 H<sup>+</sup>가 1개 미만으로 나오므로 이보다 작다.)') +
    tip('만원 지하철(ATP)에서 한 명이 내리면(가수분해) 모두 편해지지. 그런데 이미 사람들이 서로 덜 밀치고 있다면(양성자화로 음전하↓) 한 명이 내려도 “편해지는 정도”가 작아.'))

add(id='P9', kind='PROBLEM', num='9', section='연습문제',
    en_title='The ΔG′° for Coupled Reactions', ko_title='연결된 반응의 ΔG′°', slides='강의 슬라이드 20 (가산성)', level=1,
    en=f'''<p>Glucose 1-phosphate is converted into fructose 6-phosphate in two successive reactions:</p>
<p class="c">Glucose 1-phosphate → glucose 6-phosphate<br>Glucose 6-phosphate → fructose 6-phosphate</p>
<p>Using the ΔG′° values in Table 13-4, calculate the equilibrium constant, {K}, for the sum of the two reactions:</p>
<p class="c">Glucose 1-phosphate → fructose 6-phosphate</p>''',
    ko=f'''<p>포도당 1-인산은 두 단계의 연속 반응(포도당 1-인산 → 포도당 6-인산, 포도당 6-인산 → 과당 6-인산)을 거쳐 과당 6-인산으로 바뀐다. 표 13-4의 ΔG′° 값을 이용하여, 두 반응을 합한 반응(포도당 1-인산 → 과당 6-인산)의 평형상수 {K}를 계산하라.</p>
<p class="small">표 13-4: 포도당 1-인산 → 포도당 6-인산 −7.3 kJ/mol / 과당 6-인산 → 포도당 6-인산 −1.7 kJ/mol</p>''',
    blank=45,
    answer=chips(f'{G0}<sub>합</sub> = <b>−5.6 kJ/mol</b>', f'{K} ≈ <b>9.6</b> (약 10)'),
    explain=key('표에 있는 방향과 <b>반대</b>로 쓰인 반응은 ΔG′°의 <b>부호를 뒤집는다</b>. 그다음 더한다.') +
    steps('① G1P → G6P : <b>−7.3</b> kJ/mol (표 그대로)',
          '② G6P → F6P : 표에는 F6P → G6P가 −1.7로 나와 있으니, 반대 방향은 <b>+1.7</b> kJ/mol',
          f'합: −7.3 + 1.7 = <b>−5.6 kJ/mol</b> → {K} = e<sup>5.6/2.478</sup> = e<sup>2.26</sup> ≈ <span class="hl">9.6</span>',
          '<b>검산(K 곱하기)</b>: K<sub>1</sub> ≈ 19, K<sub>2</sub> = 1/1.97 ≈ 0.51 → 19 × 0.51 ≈ 9.6 ✔') +
    fig(energy_steps([('포도당 1-인산', 0, C['navy']), ('포도당 6-인산', -7.3, C['blue']), ('과당 6-인산', -5.6, C['orange'])], height=190),
        '크게 내려갔다가(−7.3) 살짝 올라가도(+1.7) 전체로는 내리막(−5.6)') +
    warn('표의 방향을 꼭 확인! “F6P → G6P = −1.7”을 그대로 더하면 −9.0이 나와서 틀린다.'))

add(id='P10', kind='PROBLEM', num='10', section='연습문제',
    en_title='Effect of [ATP]/[ADP] Ratio on Free Energy of Hydrolysis of ATP', ko_title='[ATP]/[ADP] 비가 ATP 가수분해 자유에너지에 미치는 영향', slides='강의 슬라이드 14, 54', level=2,
    en='''<p>Using Equation 13-4, plot ΔG against ln Q (mass-action ratio) at 25 °C for the concentrations of ATP, ADP, and P<sub>i</sub> in the table shown. ΔG′° for the reaction is −30.5 kJ/mol. Use the resulting plot to explain why metabolism is regulated to keep the ratio [ATP]/[ADP] high.</p>''' +
    table(['Concentration (mM)', '①', '②', '③', '④', '⑤'],
          [['ATP', '5', '3', '1', '0.2', '5'], ['ADP', '0.2', '2.2', '4.2', '5.0', '25'], ['P<sub>i</sub>', '10', '12.1', '14.1', '14.9', '10']], cls='mini'),
    ko='<p>식 13-4(ΔG = ΔG′° + RT ln Q)를 이용하여, 표에 주어진 ATP·ADP·P<sub>i</sub> 농도에 대해 25 °C에서 ΔG를 ln Q(질량작용비)에 대해 그래프로 그려라. 이 반응의 ΔG′°는 −30.5 kJ/mol이다. 그 그래프를 이용하여, 왜 대사가 [ATP]/[ADP] 비를 <b>높게</b> 유지하도록 조절되는지 설명하라.</p>',
    blank=70,
    answer=chips('그래프: 기울기 RT(2.48), y절편 −30.5인 <b>직선</b>', '[ATP]/[ADP]가 높을수록 ΔG가 더 음수(최대 약 −50 kJ/mol)', '→ ATP 1개가 낼 수 있는 에너지를 <b>최대로</b> 유지하려고'),
    explain=key('Q = [ADP][P<sub>i</sub>]/[ATP]. ATP가 많고 ADP가 적을수록 Q가 작아지고 → ln Q가 더 음수 → ΔG가 더 음수(더 강력).') +
    table(['', '[ATP]/[ADP]', 'Q (M)', 'ln Q', 'ΔG (kJ/mol)'],
          [['①', '25', '4.0×10<sup>−4</sup>', '−7.82', '<b>−49.9</b>'], ['②', '1.4', '8.9×10<sup>−3</sup>', '−4.72', '<b>−42.2</b>'],
           ['③', '0.24', '5.9×10<sup>−2</sup>', '−2.83', '<b>−37.5</b>'], ['④', '0.04', '0.37', '−0.99', '<b>−32.9</b>'],
           ['⑤', '0.2', '5.0×10<sup>−2</sup>', '−3.00', '<b>−37.9</b>']]) +
    '<p class="note">예: ① Q = (0.2×10<sup>−3</sup>)(10×10<sup>−3</sup>)/(5×10<sup>−3</sup>) = 4.0×10<sup>−4</sup> → ΔG = −30.5 + 2.478×(−7.82) = −49.9 kJ/mol. (단위를 꼭 M로 바꿔서 계산!)</p>' +
    fig(plot_p10(), 'ΔG vs ln Q: 직선. 왼쪽(ATP 많고 ADP 적음)으로 갈수록 ATP 한 개의 힘이 세진다') +
    tip('[ATP]/[ADP] 비는 “배터리 충전량”이야. 완충일수록 한 번 쓸 때 전압(에너지)이 커. 세포는 ATP를 쓰는 즉시 다시 충전해서 비를 높게 유지해야, ATP 1개로 오르막 반응을 충분히 끌어올릴 수 있다.'))

add(id='P11', kind='PROBLEM', num='11', section='연습문제',
    en_title='Strategy for Overcoming an Unfavorable Reaction: ATP-Dependent Chemical Coupling', ko_title='불리한 반응 극복 전략: ATP 의존성 화학적 공역(짝짓기)', slides='강의 슬라이드 20, 22', level=3,
    en=f'''<p>The phosphorylation of glucose to glucose 6-phosphate is the initial step in the catabolism of glucose. The direct phosphorylation of glucose by P<sub>i</sub> is described by the equation</p>
<p class="c">Glucose + P<sub>i</sub> → glucose 6-phosphate + H<sub>2</sub>O &nbsp;&nbsp; ΔG′° = 13.8 kJ/mol</p>
<p><b>a.</b> Calculate the equilibrium constant for this reaction at 37 °C. In the rat hepatocyte, the physiological concentrations of glucose and P<sub>i</sub> are maintained at approximately 4.8 m<span class="sc">M</span>. What is the equilibrium concentration of glucose 6-phosphate obtained by the direct phosphorylation of glucose by P<sub>i</sub>? Does this reaction represent a reasonable metabolic step for the catabolism of glucose? Explain.</p>
<p><b>b.</b> In principle at least, one way to increase the concentration of glucose 6-phosphate is to drive the equilibrium reaction to the right by increasing the intracellular concentrations of glucose and P<sub>i</sub>. Assuming a fixed concentration of P<sub>i</sub> at 4.8 m<span class="sc">M</span>, how high would the intracellular concentration of glucose have to be to give an equilibrium concentration of glucose 6-phosphate of 250 μ<span class="sc">M</span> (the normal physiological concentration)? Would this route be physiologically reasonable, given that the maximum solubility of glucose is less than 1 <span class="sc">M</span>?</p>
<p><b>c.</b> The phosphorylation of glucose in the cell is coupled to the hydrolysis of ATP; that is, part of the free energy of ATP hydrolysis is used to phosphorylate glucose:</p>
<p class="c">(1) Glucose + P<sub>i</sub> → glucose 6-phosphate + H<sub>2</sub>O &nbsp; ΔG′° = 13.8 kJ/mol<br>(2) ATP + H<sub>2</sub>O → ADP + P<sub>i</sub> &nbsp; ΔG′° = −30.5 kJ/mol<br>Sum: Glucose + ATP → glucose 6-phosphate + ADP</p>
<p>Calculate {K} at 37 °C for the overall reaction. For the ATP-dependent phosphorylation of glucose, what concentration of glucose is needed to achieve a 250 μ<span class="sc">M</span> intracellular concentration of glucose 6-phosphate when the concentrations of ATP and ADP are 3.38 m<span class="sc">M</span> and 1.32 m<span class="sc">M</span>, respectively? Does this coupling process provide a feasible route, at least in principle, for the phosphorylation of glucose in the cell? Explain.</p>
<p><b>d.</b> Although coupling ATP hydrolysis to glucose phosphorylation makes thermodynamic sense, we have not yet specified how this coupling is to take place. Given that coupling requires a common intermediate, one conceivable route is to use ATP hydrolysis to raise the intracellular concentration of P<sub>i</sub> and thus drive the unfavorable phosphorylation of glucose by P<sub>i</sub>. Is this a reasonable route? (Think about the solubility product, K<sub>sp</sub>, of metabolic intermediates.)</p>
<p><b>e.</b> The ATP-coupled phosphorylation of glucose is catalyzed in hepatocytes by the enzyme glucokinase. This enzyme binds ATP and glucose to form a glucose-ATP-enzyme complex, and the phosphoryl group is transferred directly from ATP to glucose. Explain the advantages of this route.</p>''',
    ko='''<p>포도당 → 포도당 6-인산(인산화)은 포도당 분해의 첫 단계다. P<sub>i</sub>로 포도당을 직접 인산화하는 반응은 다음과 같다: 포도당 + P<sub>i</sub> → 포도당 6-인산 + H<sub>2</sub>O, ΔG′° = 13.8 kJ/mol</p>
<p><b>a.</b> 37 °C에서 이 반응의 평형상수를 계산하라. 쥐 간세포에서 포도당과 P<sub>i</sub>의 생리적 농도는 약 4.8 mM로 유지된다. P<sub>i</sub>로 직접 인산화할 때 얻어지는 포도당 6-인산의 평형 농도는? 이 반응은 포도당 분해의 합리적인 대사 단계인가? 설명하라.</p>
<p><b>b.</b> 원리적으로는 세포 속 포도당과 P<sub>i</sub>의 농도를 높여 평형을 오른쪽으로 밀면 포도당 6-인산 농도를 높일 수 있다. P<sub>i</sub>를 4.8 mM로 고정할 때, 포도당 6-인산 평형 농도가 250 μM(정상 생리 농도)이 되려면 세포 속 포도당 농도가 얼마나 높아야 하는가? 포도당의 최대 용해도가 1 M 미만임을 고려할 때 이 방법은 생리적으로 타당한가?</p>
<p><b>c.</b> 세포에서 포도당 인산화는 ATP 가수분해와 짝지어진다(공역). 즉 ATP 가수분해의 자유에너지 일부가 포도당 인산화에 쓰인다[(1)+(2) → 포도당 + ATP → 포도당 6-인산 + ADP]. 37 °C에서 전체 반응의 K′<sub>eq</sub>를 계산하라. ATP와 ADP가 각각 3.38 mM, 1.32 mM일 때 포도당 6-인산 250 μM를 얻으려면 포도당이 얼마나 필요한가? 이 공역 과정은 (적어도 원리적으로) 세포에서 포도당을 인산화하는 실현 가능한 경로인가?</p>
<p><b>d.</b> ATP 가수분해와 포도당 인산화를 짝짓는 것이 열역학적으로 타당하더라도, 어떻게 짝지어지는지는 아직 정하지 않았다. 짝짓기에는 공통 중간체가 필요하므로, ATP 가수분해로 세포 속 P<sub>i</sub> 농도를 높여 불리한 포도당 인산화를 밀어붙이는 경로를 생각할 수 있다. 이것은 합리적인가? (대사 중간체의 용해도곱 K<sub>sp</sub>를 생각해 보라.)</p>
<p><b>e.</b> 간세포에서 ATP와 짝지어진 포도당 인산화는 글루코키나아제가 촉매한다. 이 효소는 ATP와 포도당에 결합해 포도당-ATP-효소 복합체를 만들고, 인산기를 ATP에서 포도당으로 <b>직접</b> 옮긴다. 이 경로의 장점을 설명하라.</p>''',
    blank=80,
    answer=chips('a. K′<sub>eq</sub> ≈ 4.7×10<sup>−3</sup> M<sup>−1</sup>, [G6P] ≈ 1.1×10<sup>−7</sup> M → <b>불합리</b>',
                 'b. 포도당 ≈ <b>11 M</b> 필요 → 용해도 초과, <b>불가능</b>',
                 'c. K′<sub>eq</sub> ≈ 6.5×10<sup>2</sup>, 포도당 ≈ <b>1.5×10<sup>−7</sup> M</b>이면 충분 → <b>가능</b>',
                 'd. P<sub>i</sub>를 ~11 M로 올려야 → 침전(K<sub>sp</sub> 초과), <b>불합리</b>',
                 'e. 효소 위 <b>직접 전달</b>: 중간체 불필요, 에너지 낭비 없음, 특이성·조절'),
    explain=key('오르막 반응(+13.8)은 혼자서는 거의 안 일어난다. 더 큰 내리막(ATP, −30.5)과 <b>한 효소 위에서 짝지으면</b> 전체가 내리막(−16.7)이 된다.') +
    fig(energy_steps([('포도당 + Pᵢ', 0, C['navy']), ('G6P (+H₂O)', 13.8, C['red']), ('ATP 가수분해로 보충 → 전체', -16.7, C['green'])], height=210),
        '오르막 +13.8을 −30.5짜리 내리막이 끌어내려, 전체는 −16.7 kJ/mol') +
    steps(
        '<b>a.</b> RT(37 °C) = 8.315×310 = 2.578 kJ/mol → K = e<sup>−13.8/2.578</sup> = e<sup>−5.35</sup> = <b>4.7×10<sup>−3</sup> M<sup>−1</sup></b>' +
        eq(f'K = {F("[G6P]", "[포도당][P<sub>i</sub>]")} → [G6P] = (4.7×10<sup>−3</sup>)(4.8×10<sup>−3</sup>)(4.8×10<sup>−3</sup>) = <span class="hl">1.1×10<sup>−7</sup> M</span>') +
        '필요한 250 μM(2.5×10<sup>−4</sup> M)의 약 <b>1/2300</b>밖에 안 된다 → 대사 단계로 쓸 수 없다.',
        '<b>b.</b> [포도당] = [G6P] / (K[P<sub>i</sub>]) = 2.5×10<sup>−4</sup> / (4.7×10<sup>−3</sup> × 4.8×10<sup>−3</sup>) = <span class="hl">11 M</span> → 최대 용해도(1 M 미만)의 10배 이상. 불가능.',
        '<b>c.</b> 전체 ΔG′° = 13.8 + (−30.5) = −16.7 kJ/mol → K = e<sup>16.7/2.578</sup> = e<sup>6.48</sup> ≈ <b>6.5×10<sup>2</sup></b>' +
        eq(f'[포도당] = {F("[G6P][ADP]", "K[ATP]")} = {F("(2.5×10<sup>−4</sup>)(1.32×10<sup>−3</sup>)", "(650)(3.38×10<sup>−3</sup>)")} = <span class="hl">1.5×10<sup>−7</sup> M</span>') +
        '실제 포도당 농도(4.8 mM)보다 훨씬 낮은 농도로도 충분 → 충분히 가능한 경로!',
        '<b>d.</b> b와 같은 계산으로, 포도당 4.8 mM에서 P<sub>i</sub>가 약 <b>11 M</b>이어야 한다. 그 전에 인산은 Ca<sup>2+</sup>·Mg<sup>2+</sup>와 결합해 <b>침전</b>한다(용해도곱 K<sub>sp</sub> 초과). 게다가 자유 P<sub>i</sub>는 세포 안 모든 인산 관련 반응에 영향을 준다 → 불합리.',
        '<b>e.</b> 효소가 ATP와 포도당을 한 자리에 붙잡고 인산기를 <b>직접</b> 넘긴다. ① 자유 P<sub>i</sub>를 거치지 않아 농도를 높일 필요가 없음 ② ATP의 에너지가 열로 새지 않음(헛된 가수분해 방지) ③ 포도당에만 인산이 붙는 <b>특이성</b> ④ 효소 활성으로 속도를 <b>조절</b> 가능.'
    ) +
    fig(logaxis([(1.5e-7, 'c: ATP 짝지음 1.5×10⁻⁷ M', C['green']), (11, 'b: Pᵢ만 11 M', C['red'])], -8, 2,
                center=1, center_lab='포도당 용해도 한계 ~1 M', height=125),
        '필요한 포도당 농도 비교 (로그 눈금): ATP와 짝지으면 약 7천만 배 적어도 된다') +
    tip('무거운 짐(+13.8)을 혼자 들 수 없을 때, 도르래 반대편에 더 무거운 추(−30.5)를 달면 짐이 올라간다. 단, 짐과 추가 <b>같은 줄(효소)</b>에 묶여 있어야 한다 — 이게 e의 “직접 전달”이야.'))

add(id='P12', kind='PROBLEM', num='12', section='연습문제',
    en_title='Calculations of ΔG′° for ATP-Coupled Reactions', ko_title='ATP와 짝지어진 반응의 ΔG′° 계산', slides='강의 슬라이드 30–31', level=1,
    en='<p>From data in Table 13-6, calculate the ΔG′° value for each reaction:</p><p class="c">a. Phosphocreatine + ADP → creatine + ATP<br>b. ATP + fructose → ADP + fructose 6-phosphate</p>',
    ko='<p>표 13-6의 자료를 이용하여 각 반응의 ΔG′°를 계산하라: a. 포스포크레아틴 + ADP → 크레아틴 + ATP / b. ATP + 과당 → ADP + 과당 6-인산</p><p class="small">표 13-6: 포스포크레아틴 −43.0, ATP(→ADP+P<sub>i</sub>) −30.5, 과당 6-인산 −15.9 kJ/mol (모두 가수분해 ΔG′°)</p>',
    blank=40,
    answer=chips('a. <b>−12.5 kJ/mol</b>', 'b. <b>−14.6 kJ/mol</b>'),
    explain=key('인산기 전달 = “A의 인산 떼기(가수분해)” + “B에 인산 붙이기(가수분해의 역반응)”. 떼는 쪽은 표 값 그대로, 붙이는 쪽은 부호를 뒤집어 더한다.') +
    align([('a.', 'PCr + H<sub>2</sub>O → Cr + P<sub>i</sub>', '−43.0'), ('', 'ADP + P<sub>i</sub> → ATP + H<sub>2</sub>O', '+30.5'),
           ('합', 'PCr + ADP → Cr + ATP', '<span class="hl">−12.5 kJ/mol</span>')], cls='sum') +
    align([('b.', 'ATP + H<sub>2</sub>O → ADP + P<sub>i</sub>', '−30.5'), ('', '과당 + P<sub>i</sub> → F6P + H<sub>2</sub>O', '+15.9'),
           ('합', 'ATP + 과당 → ADP + F6P', '<span class="hl">−14.6 kJ/mol</span>')], cls='sum') +
    fig(phos_ladder(hl=('PCr', 'ATP', 'F6P'), flows=[('PCr', 'ATP', 'a'), ('ATP', 'F6P', 'b')], height=290),
        '인산기는 사다리 위(고에너지)에서 아래(저에너지)로만 저절로 흐른다. ATP는 딱 중간 = 중계자') +
    tip('인산기는 물처럼 “높은 곳 → 낮은 곳”으로 흘러. PCr(−43)는 ATP(−30.5)보다 위에 있으니 ADP에 인산을 줄 수 있고(근육의 비상 배터리), ATP는 과당(−15.9)보다 위에 있으니 과당에 인산을 줄 수 있다.', '직관'))

add(id='P13', kind='PROBLEM', num='13', section='연습문제',
    en_title='Coupling ATP Cleavage to an Unfavorable Reaction', ko_title='ATP 분해를 불리한 반응과 짝짓기', slides='강의 슬라이드 14, 20', level=2,
    en='''<p>To explore the consequences of coupling ATP hydrolysis under physiological conditions to a thermodynamically unfavorable biochemical reaction, consider the hypothetical transformation X → Y, for which ΔG′° = 20.0 kJ/mol.</p>
<p><b>a.</b> What is the ratio [Y]/[X] at equilibrium?<br>
<b>b.</b> Suppose X and Y participate in a sequence of reactions during which ATP is hydrolyzed to ADP and P<sub>i</sub>. The overall reaction is X + ATP + H<sub>2</sub>O → Y + ADP + P<sub>i</sub>. Calculate [Y]/[X] for this reaction at equilibrium. Assume that the temperature is 25.0 °C and the equilibrium concentrations of ATP, ADP, and P<sub>i</sub> are 1 <span class="sc">M</span>.<br>
<b>c.</b> We know that [ATP], [ADP], and [P<sub>i</sub>] are not 1 <span class="sc">M</span> under physiological conditions. Calculate [Y]/[X] for the ATP-coupled reaction when the values of [ATP], [ADP], and [P<sub>i</sub>] are those found in rat myocytes (Table 13-5).</p>''',
    ko='''<p>생리적 조건에서 ATP 가수분해를 열역학적으로 불리한 생화학 반응과 짝지었을 때의 결과를 알아보기 위해, ΔG′° = 20.0 kJ/mol인 가상의 변환 X → Y를 생각하자.</p>
<p><b>a.</b> 평형에서 [Y]/[X] 비는?<br><b>b.</b> X와 Y가 ATP가 ADP와 P<sub>i</sub>로 가수분해되는 일련의 반응에 참여하여, 전체 반응이 X + ATP + H<sub>2</sub>O → Y + ADP + P<sub>i</sub>라고 하자. 25.0 °C이고 ATP·ADP·P<sub>i</sub>의 평형 농도가 모두 1 M일 때, 평형에서 [Y]/[X]를 계산하라.<br><b>c.</b> 실제 생리적 조건에서 [ATP], [ADP], [P<sub>i</sub>]는 1 M이 아니다. 쥐 근육세포(표 13-5: ATP 8.05, ADP 0.93, P<sub>i</sub> 8.05 mM)의 값을 쓸 때 ATP와 짝지어진 반응의 [Y]/[X]를 계산하라.</p>''',
    blank=55,
    answer=chips('a. [Y]/[X] ≈ <b>3.1×10<sup>−4</sup></b>', 'b. ≈ <b>69</b>', 'c. ≈ <b>7.4×10<sup>4</sup></b>'),
    explain=steps(
        '<b>a.</b> K = e<sup>−20.0/2.478</sup> = e<sup>−8.07</sup> = <span class="hl">3.1×10<sup>−4</sup></span> → Y가 X의 약 1/3000. 거의 안 일어남.',
        '<b>b.</b> 전체 ΔG′° = 20.0 + (−30.5) = −10.5 kJ/mol → K = e<sup>10.5/2.478</sup> = e<sup>4.24</sup> ≈ 69.' +
        eq(f'K = {F("[Y][ADP][P<sub>i</sub>]", "[X][ATP]")}, ATP·ADP·P<sub>i</sub> = 1 M 이면 [Y]/[X] = K = <span class="hl">69</span>'),
        '<b>c.</b> 같은 K 식을 [Y]/[X]에 대해 풀면:' +
        eq(f'{F("[Y]", "[X]")} = K × {F("[ATP]", "[ADP][P<sub>i</sub>]")} = 69 × {F("8.05×10<sup>−3</sup>", "(0.93×10<sup>−3</sup>)(8.05×10<sup>−3</sup>)")} = 69 × 1075 ≈ <span class="hl">7.4×10<sup>4</sup></span>')
    ) +
    fig(logaxis([(3.1e-4, 'a: ATP 없이', C['red']), (69, 'b: ATP (1 M)', C['blue']), (7.4e4, 'c: 세포 속 ATP', C['green'])], -5, 6,
                center=1, center_lab='[Y]=[X]', height=125),
        'ATP 하나를 짝지었을 뿐인데 [Y]/[X]가 약 <b>2억 배(10<sup>8</sup>)</b> 바뀐다') +
    tip('세포 속에선 ATP는 많고 ADP·P<sub>i</sub>는 적어서, ATP가 “표준 조건”일 때보다 훨씬 센 힘으로 반응을 밀어준다. 그래서 오르막 반응도 세포 안에서는 거뜬히 일어난다.', '포인트'))

add(id='P14', kind='PROBLEM', num='14', section='연습문제',
    en_title='Calculations of ΔG at Physiological Concentrations', ko_title='생리적 농도에서의 ΔG 계산', slides='강의 슬라이드 14, 30', level=2,
    en='<p>Calculate the actual, physiological ΔG for the reaction</p><p class="c">Phosphocreatine + ADP → creatine + ATP</p><p>at 37 °C, as it occurs in the cytosol of neurons, with phosphocreatine at 4.7 m<span class="sc">M</span>, creatine at 1.0 m<span class="sc">M</span>, ADP at 0.73 m<span class="sc">M</span>, and ATP at 2.6 m<span class="sc">M</span>.</p>',
    ko='<p>뉴런의 세포질에서 37 °C로 일어나는 반응 포스포크레아틴 + ADP → 크레아틴 + ATP의 실제(생리적) ΔG를 계산하라. 농도는 포스포크레아틴 4.7 mM, 크레아틴 1.0 mM, ADP 0.73 mM, ATP 2.6 mM이다.</p>',
    blank=45,
    answer=chips(f'{DG} ≈ <b>−13.2 kJ/mol</b>'),
    explain=key(f'{G0}는 문제 12a에서 구한 <b>−12.5 kJ/mol</b>. 여기에 RT ln Q로 “지금 농도” 보정만 하면 된다.') +
    steps(eq(f'Q = {F("[크레아틴][ATP]", "[포스포크레아틴][ADP]")} = {F("(1.0)(2.6)", "(4.7)(0.73)")} = 0.76'),
          '분자·분모 모두 농도가 2개씩이라 mM 단위가 서로 지워진다 → mM 그대로 계산해도 OK.',
          align([(DG, '−12.5 + (2.578)(ln 0.76)'), ('', '−12.5 + (2.578)(−0.28) = −12.5 − 0.7 = <span class="hl">−13.2 kJ/mol</span>')])) +
    tip('이 반응(크레아틴 키나아제)은 근육·뇌에서 ATP가 갑자기 부족할 때 PCr의 인산을 ADP에 넘겨 ATP를 즉시 채워 주는 <b>비상 발전기</b>야. ΔG가 음수이니 실제 세포 안에서도 ATP를 만드는 방향으로 간다.'))

add(id='P15', kind='PROBLEM', num='15', section='연습문제',
    en_title='Free Energy Required for ATP Synthesis under Physiological Conditions', ko_title='생리적 조건에서 ATP 합성에 필요한 자유에너지', slides='강의 슬라이드 14', level=1,
    en=f'<p>In the cytosol of rat hepatocytes, the temperature is 37 °C and the mass-action ratio, Q, is</p>{eq(F("[ATP]", "[ADP][P<sub>i</sub>]") + " = 5.33 × 10<sup>2</sup> M<sup>−1</sup>")}<p>Calculate the free energy required to synthesize ATP in a rat hepatocyte.</p>',
    ko='<p>쥐 간세포의 세포질에서 온도는 37 °C이고, 질량작용비 Q = [ATP]/([ADP][P<sub>i</sub>]) = 5.33×10<sup>2</sup> M<sup>−1</sup>이다. 쥐 간세포에서 ATP를 합성하는 데 필요한 자유에너지를 계산하라.</p>',
    blank=35,
    answer=chips(f'{DG}<sub>합성</sub> ≈ <b>+46.7 kJ/mol</b> (약 47 kJ/mol 필요)'),
    explain=key('ATP <b>합성</b>(ADP + P<sub>i</sub> → ATP + H<sub>2</sub>O)은 가수분해의 반대 → ΔG′° = <b>+30.5</b>. 주어진 Q가 이미 “합성 방향”으로 쓰여 있다.') +
    align([(DG, '+30.5 + RT ln Q = 30.5 + (2.578)(ln 533)'), ('', '30.5 + (2.578)(6.28) = 30.5 + 16.2 = <span class="hl">+46.7 kJ/mol</span>')]) +
    '<p class="note">비교: 사람 적혈구에서는 약 52 kJ/mol(예제 13-2). 세포마다 농도가 달라서 필요한 에너지도 조금씩 다르다.</p>' +
    tip('세포는 ATP를 “많이 채워 둔” 상태라서(Q 큼), 거기에 하나 더 채워 넣으려면 표준 조건(30.5)보다 더 많은 힘(46.7)이 든다. 이미 빵빵한 풍선에 바람 넣기가 더 힘든 것과 같아.'))
