# -*- coding: utf-8 -*-
"""13장 시험대비 요약노트 (풀이노트와 같은 디자인).  python3 exam13.py → exam_ch13.pdf"""
import os, sys, math
os.environ.setdefault('CH', '13')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from helpers import *
import build as B
import ch13
from content_a import phos_ladder, egg_svg
from content_b import R, e_line, atp_cycle, pump_svg

HERE = os.path.dirname(os.path.abspath(__file__))
FOOT = 'Lehninger 8e · Ch.13 생체에너지론 — 시험대비 요약노트'

# 풀이노트 쪽번호 (레닌저 13장 예제·문제 풀이노트.pdf)
_items = [i for i in ch13.ALL_ITEMS if i['level'] < 3]
WB = {i['id']: 7 + k for k, i in enumerate(_items)}


def link(*ids):
    parts = []
    for i in ids:
        lab = '예제 13-' + i[2:] if i.startswith('WE') else '문제 ' + i[1:]
        parts.append(f'<span class="wl">{lab} <i>p.{WB[i]}</i></span>')
    return f'<div class="wlink"><b>📒 풀이노트로 이어서 풀기</b>{"".join(parts)}</div>'


# ------------------------------------------------------------------ drawings
def hill(ea=True, w=470, h=200, l='ATP + H₂O', r='ADP + Pᵢ', dg='ΔG′° = −30.5'):
    b = arrowdef('h1', C['green']) + arrowdef('h2', C['red'])
    b += f'<line x1="40" y1="16" x2="40" y2="{h-25}" stroke="{C["gray"]}"/><line x1="40" y1="{h-25}" x2="{w-10}" y2="{h-25}" stroke="{C["gray"]}"/>'
    b += f'<text x="22" y="{h/2}" font-size="10" fill="{C["gray"]}" text-anchor="middle" transform="rotate(-90 22 {h/2})" font-weight="700">자유에너지 G</text>'
    b += T(w / 2, h - 8, '반응 진행 →', 10, C['gray'])
    y1, y2, top = 80, 150, 28
    path = (f'M50,{y1} L130,{y1} C190,{y1} 200,{top} 240,{top} C280,{top} 290,{y2} 350,{y2} L{w-20},{y2}' if ea
            else f'M50,{y1} L130,{y1} C220,{y1} 260,{y2} 350,{y2} L{w-20},{y2}')
    b += f'<path d="{path}" fill="none" stroke="{C["navy"]}" stroke-width="3"/>'
    b += T(90, y1 - 8, l, 11, C['navy'], weight=700) + T(w - 60, y2 - 8, r, 11, C['navy'], weight=700)
    b += f'<line x1="130" y1="{y1}" x2="{w-40}" y2="{y1}" stroke="{C["gray"]}" stroke-dasharray="3 3"/>'
    b += f'<line x1="{w-40}" y1="{y1}" x2="{w-40}" y2="{y2-3}" stroke="{C["green"]}" stroke-width="2" marker-end="url(#h1)"/>'
    b += T(w - 46, (y1 + y2) / 2 + 4, dg, 11, C['green'], 'end', 700)
    if ea:
        b += f'<line x1="240" y1="{y1}" x2="240" y2="{top+3}" stroke="{C["red"]}" stroke-width="2" marker-end="url(#h2)"/>'
        b += T(250, 50, 'Eₐ (활성화 에너지)', 10.5, C['red'], 'start', 700) + T(250, 64, '효소가 낮춘다', 9.5, C['red'], 'start')
    return svg(w, h, b)


def metab_map():
    W, H = 560, 230
    b = arrowdef('mm1', C['orange']) + arrowdef('mm2', C['blue'])
    b += f'<rect x="10" y="20" width="160" height="70" rx="12" fill="#fff7ed" stroke="#fdba74"/>' + T(90, 46, '음식 분자', 12, C['orange'], weight=900) + T(90, 66, '포도당·지방산·아미노산', 10, C['ink'])
    b += f'<rect x="200" y="20" width="160" height="70" rx="12" fill="#fef2f2" stroke="#fca5a5"/>' + T(280, 46, '이화 (분해)', 12, C['red'], weight=900) + T(280, 66, '해당·TCA·산화적 인산화', 10, C['ink'])
    b += f'<rect x="390" y="20" width="160" height="70" rx="12" fill="#fefce8" stroke="#facc15"/>' + T(470, 46, '쓸 수 있는 에너지', 12, '#a16207', weight=900) + T(470, 66, 'ATP · NADH · NADPH', 10.5, C['ink'], weight=700)
    b += f'<rect x="390" y="140" width="160" height="70" rx="12" fill="#eff6ff" stroke="#93c5fd"/>' + T(470, 166, '동화 (합성)', 12, C['blue'], weight=900) + T(470, 186, '단백질·DNA·지방·글리코겐', 10, C['ink'])
    b += f'<rect x="200" y="140" width="160" height="70" rx="12" fill="#f8fafc" stroke="#cbd5e1"/>' + T(280, 166, '열 (손실)', 12, C['gray'], weight=900) + T(280, 186, '2법칙: 일부는 꼭 열로', 10, C['ink'])
    b += f'<line x1="172" y1="55" x2="196" y2="55" stroke="{C["orange"]}" stroke-width="2.5" marker-end="url(#mm1)"/>'
    b += f'<line x1="362" y1="55" x2="386" y2="55" stroke="{C["orange"]}" stroke-width="2.5" marker-end="url(#mm1)"/>'
    b += f'<line x1="470" y1="92" x2="470" y2="136" stroke="{C["blue"]}" stroke-width="2.5" marker-end="url(#mm2)"/>' + T(478, 118, '에너지 사용', 10, C['blue'], 'start', 700)
    b += f'<line x1="280" y1="92" x2="280" y2="136" stroke="{C["gray"]}" stroke-width="2" marker-end="url(#mm2)" stroke-dasharray="4 3"/>'
    b += T(90, 130, '이화: 큰 → 작은, 에너지 방출', 10.5, C['red'], weight=700) + T(90, 150, '동화: 작은 → 큰, 에너지 소비', 10.5, C['blue'], weight=700)
    b += T(90, 172, '이화의 중간체는 동화의', 10, C['gray']) + T(90, 186, '재료(building block)도 된다', 10, C['gray'])
    return svg(W, H, b)


def atp_struct():
    W, H = 480, 150
    b = f'<rect x="10" y="50" width="120" height="44" rx="10" fill="#e0e7ff" stroke="#6366f1"/>' + T(70, 70, '아데노신', 12, C['navy'], weight=900) + T(70, 86, '(아데닌 + 리보스)', 9, C['gray'])
    b += f'<line x1="130" y1="72" x2="410" y2="72" stroke="{C["ink"]}" stroke-width="2"/>'
    for i, (x, g) in enumerate([(180, 'α'), (270, 'β'), (360, 'γ')]):
        col = C['red'] if i == 2 else C['blue']
        b += f'<circle cx="{x}" cy="72" r="24" fill="white" stroke="{col}" stroke-width="3"/>' + T(x, 78, 'P', 15, col, weight=900)
        b += T(x - 30, 46, g, 13, C['gray'], weight=900, family='Noto Serif')
        b += T(x + 18, 108, '−', 18, C['red'], weight=900) + T(x - 14, 112, '−', 18, C['red'], weight=900)
    b += T(225, 138, '인산무수물 결합 ×2 (α–β, β–γ)', 10.5, C['orange'], weight=700)
    b += T(470, 16, '음전하끼리 밀어냄 = 꽉 눌린 스프링', 10.5, C['red'], 'end', 700)
    return svg(W, H, b)


def carbon_ox():
    rows = [('CH₄ 메테인', 8), ('CH₃–CH₃ 에테인(알케인)', 7), ('CH₃CH₂OH 에탄올', 5), ('CH₃CHO 아세트알데하이드', 3), ('CH₃COOH 아세트산', 1), ('CO₂', 0)]
    b = ''
    cols = [C['blue'], C['blue'], '#0891b2', C['amber'], C['orange'], C['red']]
    for i, (n, e) in enumerate(rows):
        y = 6 + i * 26
        b += T(10, y + 15, n, 11, C['ink'], 'start', 700)
        b += f'<rect x="200" y="{y+2}" width="{e*28+2}" height="18" rx="4" fill="{cols[i]}"/>' + T(206 + e * 28, y + 15, f'전자 {e}개', 10.5, cols[i], 'start', 700)
    b += T(10, 6 * 26 + 18, '빨간 탄소가 “소유한” 전자 수 · 위 = 가장 환원 → 아래 = 가장 산화', 10.5, C['gray'], 'start', 700)
    return svg(500, 6 * 26 + 26, b)


def nad_svg():
    W, H = 480, 128
    b = arrowdef('nd', C['orange'])
    b += f'<rect x="10" y="30" width="170" height="56" rx="12" fill="#eff6ff" stroke="{C["blue"]}" stroke-width="2"/>' + T(95, 54, 'NAD⁺ (산화형)', 12, C['blue'], weight=900) + T(95, 72, '빈 트럭', 10, C['gray'])
    b += f'<rect x="300" y="30" width="170" height="56" rx="12" fill="#fff7ed" stroke="{C["orange"]}" stroke-width="2"/>' + T(385, 54, 'NADH (환원형)', 12, C['orange'], weight=900) + T(385, 72, '전자 2개를 실은 트럭', 10, C['gray'])
    b += f'<line x1="185" y1="50" x2="295" y2="50" stroke="{C["orange"]}" stroke-width="2.4" marker-end="url(#nd)"/>' + T(240, 24, '+ H⁻ (= H⁺ + 2e⁻)', 10, C['orange'], weight=700)
    b += f'<line x1="295" y1="70" x2="185" y2="70" stroke="{C["blue"]}" stroke-width="2.4" marker-end="url(#nd)"/>' + T(240, 100, '전자를 내려놓으면 다시 NAD⁺', 10, C['blue'], weight=700)
    b += T(240, 120, '연료의 전자 → NADH → 전자전달계 → O₂', 10.5, C['ink'], weight=700)
    return svg(W, H, b)


def std_state():
    rows = [('ΔG', '실제 농도 (지금 이 순간)', '변수', C['orange']), ('ΔG°', '25 °C · 1 atm · 모든 물질 1 M (H⁺ 1 M = pH 0)', '상수', C['gray']),
            ('ΔG′°', '위 + pH 7 · [H₂O] 55.5 M · [Mg²⁺] 1 mM', '상수', C['blue'])]
    b = ''
    for i, (s, d, k, col) in enumerate(rows):
        y = 8 + i * 44
        b += f'<rect x="8" y="{y}" width="70" height="34" rx="8" fill="{col}"/>' + T(43, y + 23, s, 15, 'white', weight=900, family='Noto Serif')
        b += T(92, y + 22, d, 11.5, C['ink'], 'start', 700) + f'<rect x="440" y="{y+6}" width="52" height="22" rx="11" fill="none" stroke="{col}"/>' + T(466, y + 21, k, 11, col, weight=900)
    return svg(500, 140, b)


def two_step():
    return flow(['글루탐산 + ATP', 'γ-글루타밀 인산|(효소에 붙은 중간체)', '글루타민 + Pᵢ'], arrow_labels=['① 인산 전달 (−ADP)', '② + NH₃'],
                colors=[C['navy'], C['orange'], C['green']], box_h=44)


def redox_ladder_big():
    return ladder(R('½O₂/H₂O', '시토크롬 c', '유비퀴논/유비퀴놀', '푸마르산/숙신산', '피루브산/젖산', '아세트알데하이드/에탄올', 'NAD⁺/NADH', 'α-케토글루타르산+CO₂/아이소시트르산'),
                  -0.42, 0.86, hl=('NAD⁺/NADH', '½O₂/H₂O'), flows=[('NAD⁺/NADH', '½O₂/H₂O', 'e⁻ 폭포')], height=270)


def ksign():
    return logaxis([(0.01, 'K=0.01 → +11.4', C['red']), (1, 'K=1 → 0', C['gray']), (100, 'K=100 → −11.4', C['green'])], -3, 3,
                   center=1, center_lab='', height=110, label='K′eq (로그 눈금)')


# ------------------------------------------------------------------ pages
def page(no, title, en, lead, body, links=()):
    lk = link(*links) if links else ''
    return (f'<h2 class="pt"><span class="n">{no}</span> {title} <span class="en2">{en}</span></h2>'
            f'<p class="lead">{lead}</p>{body}{lk}')


SUMMARY = []

SUMMARY.append(page('S1', '대사의 큰 그림 — 이화와 동화', 'Metabolism · Slides 3–7',
  '<b>대사</b> = 세포 안 모든 화학 변화의 총합. 효소 반응이 줄지어 이어진 <b>대사 경로</b>로 일어난다. 목적은 ① 에너지 얻기 ② 영양분을 내 분자로 바꾸기 ③ 작은 단위를 큰 분자로 중합.',
  f'''<div class="grid2"><div class="card"><figure class="fig">{metab_map()}</figure></div>
<div><div class="card"><h4>📌 시험 포인트</h4>{table(['', '이화 (catabolism)', '동화 (anabolism)'], [['방향', '큰 분자 → 작은 분자', '작은 분자 → 큰 분자'], ['에너지', '<b>방출</b> (ATP·NADH 생성)', '<b>소비</b> (ATP·NADPH 사용)'], ['예', '해당·TCA·산화적 인산화', '단백질·핵산·지방 합성, 광합성 탄소 고정']])}
 {key('이화로 얻은 <b>ATP·NADPH</b>가 동화를 돌린다. 에너지의 일부는 항상 <b>열</b>로 손실 (열역학 제2법칙).')}</div>
<div class="card" style="margin-top:3mm"><h4>🧩 13장은 “대사의 문법”</h4><p>14장(해당과정)부터 나오는 모든 경로를 읽으려면 세 가지가 필요: <b>ΔG</b>(방향), <b>ATP</b>(에너지 화폐), <b>산화-환원</b>(전자 흐름). 이 셋이 13장의 전부.</p></div></div></div>'''))

SUMMARY.append(page('S2', 'ATP — 세포의 에너지 화폐', 'ATP · Slides 9–13',
  'ATP = 아데노신 + 인산 3개. 끝 인산이 떨어지는 가수분해(ATP + H<sub>2</sub>O → ADP + P<sub>i</sub>)가 <b>ΔG′° = −30.5 kJ/mol</b>로 크다. 이유 4가지는 단골 문제!',
  f'''<div class="grid2"><div><div class="card"><h4>ATP의 구조</h4><figure class="fig">{atp_struct()}</figure>
 <div class="formula">ATP<sup>4−</sup> + H<sub>2</sub>O → ADP<sup>3−</sup> + HPO<sub>4</sub><sup>2−</sup> + H<sup>+</sup> &nbsp; ΔG′° = −30.5</div></div>
 <div class="card" style="margin-top:3mm"><h4>⚡ 왜 저절로 안 깨질까? — 열역학 vs 속도론</h4><figure class="fig">{hill(h=180)}</figure>
 <p><b>열역학적으로 불안정</b>(내리막)이지만 <b>속도론적으로 안정</b>(Eₐ 200–400 kJ/mol). 효소가 있어야만 깨짐 → 세포가 쓰는 곳을 고를 수 있다.</p></div></div>
<div><div class="card"><h4>📌 가수분해 ΔG가 큰 이유 4가지 (그림 13-11)</h4>
 <figure class="fig" style="width:42%;float:right;margin:0 0 0 3mm">{img('fig13_11.png', '100%')}</figure>
 <ol style="margin:.2em 0;padding-left:1.3em"><li><b>전하 반발 해소</b>: 음전하 인산끼리 밀어내던 긴장이 풀림 (만원 지하철에서 한 명 내림)</li>
 <li><b>P<sub>i</sub>의 공명 안정화</b>: 떨어진 인산의 전자가 O 4개에 고르게 퍼짐</li>
 <li><b>이온화</b>: ADP<sup>2−</sup> → ADP<sup>3−</sup> + H<sup>+</sup> (pH 7에서 H⁺를 내놓아 안정)</li>
 <li><b>수화(용매화)</b>: 생성물이 물에 더 잘 둘러싸임</li></ol><div style="clear:both"></div></div>
 {tip('“고에너지 결합에 에너지가 저장돼 있다”는 엄밀히 틀린 말. 결합을 끊는 데는 에너지가 든다. 차이는 <b>반응물과 생성물의 안정성 차이</b>에서 온다.', '함정')}
 {key('ATP는 오래 보관하는 창고가 아니라 <b>빨리 도는 현금</b>. 사람은 하루에 몸무게만큼 가까운 ATP를 만들고 쓴다.')}</div></div>''',
  ('P7', 'P8', 'P22')))

SUMMARY.append(page('S3', '세포 속 실제 ATP 에너지 — ΔGp', 'Phosphorylation potential · Slides 14, 54',
  '세포는 ATP를 <b>많이</b>, ADP·P<sub>i</sub>를 <b>적게</b> 유지한다 → 생성물이 적으니 반응이 더 “가고 싶어” 함(르샤틀리에) → 실제 ΔG<sub>p</sub>는 −30.5보다 훨씬 큰 약 <b>−50 ~ −60 kJ/mol</b>.',
  f'''<div class="grid2"><div class="card"><h4>계산법</h4><div class="formula">ΔG<sub>p</sub> = ΔG′° + RT ln {F('[ADP][P<sub>i</sub>]', '[ATP]')}</div>
 {table(['세포', 'ATP', 'ADP', 'P<sub>i</sub>', 'PCr'], [['쥐 간세포', '3.38', '1.32', '4.8', '0'], ['쥐 근육세포', '8.05', '0.93', '8.05', '28'], ['쥐 뉴런', '2.59', '0.73', '2.72', '4.7'], ['사람 적혈구', '2.25', '0.25', '1.65', '0']])}
 <p class="small">표 13-5 (mM). 적혈구: Q = (0.25×10<sup>−3</sup>)(1.65×10<sup>−3</sup>)/(2.25×10<sup>−3</sup>) = 1.8×10<sup>−4</sup> → RT ln Q = 2.58 × (−8.6) = −22 → <b>−52 kJ/mol</b></p>
 <figure class="fig">{bars([('표준 (모두 1 M)', 30.5, '#93c5fd', '−30.5'), ('적혈구 속', 52, C['orange'], '−52 kJ/mol')], height=85)}</figure></div>
<div><div class="card"><h4>📌 실제 ΔG<sub>p</sub>에 영향을 주는 요인 (슬라이드 54)</h4><ul>
 <li><b>농도</b>: ADP·P<sub>i</sub>가 낮을수록 더 음수</li><li><b>pH·온도·[Mg<sup>2+</sup>]</b>: Mg<sup>2+</sup>가 ATP 음전하를 가려 줌 (세포 속 ATP는 대부분 MgATP<sup>2−</sup>)</li>
 <li><b>단백질 결합</b>: 계산에 쓸 “자유” 농도는 총 농도보다 낮다 (자유 ADP로 계산하면 약 −58)</li></ul>
 {key('세포는 [ATP]/[ADP]를 평형보다 <b>훨씬 높게</b> 유지 = 평형에서 멀리 = 일을 할 수 있는 상태. 평형(ΔG = 0)에 도달 = 죽음.')}</div>
 <div class="card" style="margin-top:3mm"><h4>🔁 ATP를 “만들 때”는?</h4><p>합성은 가수분해의 정반대 → 세포에서 ATP 1개 만드는 데 약 <b>+50 kJ/mol</b> (적혈구 +52, 간 +47).</p>
 {warn('“체온·생리적 조건” → 37 °C → RT = <b>2.578</b> kJ/mol. 25 °C면 2.478.', '함정')}</div></div></div>''',
  ('WE2', 'P10', 'P15', 'P22')))

SUMMARY.append(page('S4', '깁스 자유에너지 G — 반응 방향의 잣대', 'Gibbs free energy · Slide 15',
  '<b>G = 일을 할 수 있는 에너지</b>. 반응은 G가 낮아지는 쪽(<b>ΔG &lt; 0</b>)으로 저절로 간다. 열(ΔH)과 무질서(ΔS)를 한 식에 묶은 것.',
  f'''<div class="grid2"><div><div class="card"><h4>핵심 공식</h4><div class="formula">ΔG = ΔH − TΔS</div>
 {table(['기호', '이름', '뜻'], [['G', '깁스 자유에너지', '일할 수 있는 에너지 (kJ/mol)'], ['H', '엔탈피', '반응계의 열 함량 · ΔH &lt; 0 = 발열'], ['S', '엔트로피', '무작위성·무질서도 · ΔS &gt; 0 = 무질서 ↑'], ['T', '절대온도', 'K (25 °C = 298 K)']], cls='left')}</div>
 <div class="card" style="margin-top:3mm"><h4>📌 ΔG 부호 = 방향</h4>{table(['ΔG', '반응', '용어'], [['&lt; 0', '자발적 (정반응)', '발에르곤 exergonic'], ['= 0', '평형', '—'], ['&gt; 0', '비자발적 (역방향이 자발)', '흡에르곤 endergonic']])}</div></div>
<div><div class="card"><h4>열역학 법칙과 생명</h4><p><b>제1법칙</b>: 에너지 총량 일정 (형태만 변함). <b>제2법칙</b>: 우주 전체 엔트로피는 늘어난다.</p>
 <p>생물은 질서를 만들지만(계 S ↓), 열·CO<sub>2</sub>·H<sub>2</sub>O를 주변에 쏟아 주변 S를 더 크게 늘린다 → 우주 S ↑ ✔</p><figure class="fig">{egg_svg()}</figure></div>
 {warn('ΔG는 “방향”만 알려 준다. <b>속도</b>는 활성화 에너지가 결정 → 효소의 몫.', '함정')}</div></div>''',
  ('P1',)))

SUMMARY.append(page('S5', 'ΔG · ΔG° · ΔG′° — 표준 상태의 차이', 'Standard states · Slide 16',
  '세 기호를 헷갈리면 13장 문제를 못 푼다. <b>ΔG′°</b>(생화학 표준)와 <b>ΔG°</b>는 반응마다 정해진 <b>상수</b>, <b>ΔG</b>는 농도에 따라 바뀌는 <b>변수</b>.',
  f'''<div class="grid2"><div class="card"><h4>세 가지 비교</h4><figure class="fig">{std_state()}</figure>
 <p>′(프라임) = “생화학 표준 (pH 7)”. K′<sub>eq</sub>, E′°도 같은 약속.</p>
 {key('ΔG′° = “모두 1 M에서 출발했다면”의 기본 성향 (기후) / ΔG = “지금 이 농도에서”의 실제 성향 (오늘 날씨).')}</div>
<div><div class="card"><h4>📌 왜 pH 7로 바꿨을까?</h4><p>화학 표준은 [H⁺] = 1 M (pH 0)인데, 세포는 pH 7. H⁺가 참여하는 반응은 pH에 따라 ΔG가 크게 달라지므로 생화학자들은 pH 7을 표준으로 잡았다.</p>
 <p>물(55.5 M)과 H⁺(pH 7)는 상수 취급 → <b>K, Q 식에 넣지 않는다</b>.</p></div>
 <div class="card" style="margin-top:3mm"><h4>✏️ 시험에서 이렇게 묻는다</h4><ul><li>“ΔG′°는 농도에 따라 변한다” → <b>✕</b> (상수)</li><li>“자발성은 ΔG′°의 부호로 판단한다” → <b>✕</b> (ΔG로)</li><li>“ΔG′°가 양수인 반응도 세포에서 진행될 수 있다” → <b>○</b> (Q를 작게)</li></ul></div></div></div>''',
  ('P6',)))

SUMMARY.append(page('S6', 'ΔG′°와 평형상수 K′eq, 그리고 실제 ΔG', 'Slides 17–19 · Table 13-3',
  '두 공식이 13장 계산의 80%. <b>ΔG′° = −RT ln K′<sub>eq</sub></b> (평형상수 ↔ 표준 에너지), <b>ΔG = ΔG′° + RT ln Q</b> (지금 농도 보정).',
  f'''<div class="grid2"><div><div class="card"><h4>유도 — 평형에서 ΔG = 0</h4>
 <div class="formula">ΔG = ΔG′° + RT ln Q</div><p>평형이면 Q = K′<sub>eq</sub>, ΔG = 0 →</p><div class="formula">ΔG′° = −RT ln K′<sub>eq</sub> &nbsp;⇔&nbsp; K′<sub>eq</sub> = e<sup>−ΔG′°/RT</sup></div>
 <p class="small">Q(질량작용비) = [C]<sup>c</sup>[D]<sup>d</sup>/[A]<sup>a</sup>[B]<sup>b</sup> (지금 농도, M 단위, 물 제외)</p></div>
 <div class="card" style="margin-top:3mm"><h4>📌 표 13-3 · K와 ΔG′°</h4>{table(['K′<sub>eq</sub>', 'ΔG′°', '모두 1 M에서 출발하면'], [['&gt; 1', '음수', '정반응'], ['= 1', '0', '평형'], ['&lt; 1', '양수', '역반응']])}
 <figure class="fig">{ksign()}</figure></div></div>
<div><div class="card"><h4>Q와 K 비교 = 지금 방향</h4>{table(['', 'ΔG', '진행'], [['Q &lt; K', '음수', '정반응 →'], ['Q = K', '0', '평형'], ['Q &gt; K', '양수', '← 역반응']])}
 <figure class="fig">{logaxis([(0.333, '지금 Q', C['orange']), (1.97, '평형 K', C['navy'])], -1, 1, height=100, label='Q → K 쪽으로 이동')}</figure></div>
 <div class="card" style="margin-top:3mm"><h4>🔢 계산 꿀팁</h4><ul><li>RT = <b>2.478</b> (25 °C) / <b>2.578</b> (37 °C) kJ/mol</li><li><b>10배 규칙</b>: K ×10 ⇔ ΔG′° −5.7 kJ/mol (25 °C)</li><li>ln ≠ log! ln x = 2.303 log x</li></ul>
 {warn('R = 8.315 <b>J</b>/mol·K → 답이 J이면 ÷1000. 생성물·반응물 개수가 다르면 꼭 M로 바꿔 Q 계산.', '함정')}</div></div></div>''',
  ('WE1', 'P2', 'P3', 'P4', 'P6')))

SUMMARY.append(page('S7', 'ΔG에 관한 6가지 정리 (Note)', 'Slide 20',
  '교수님이 따로 정리한 슬라이드 = <b>OX 문제의 원천</b>. 여섯 줄을 그대로 외워 두자.',
  f'''<div class="grid3">
 <div class="card"><h4><span class="no">1</span> 자발성은 ΔG′°가 아니라 ΔG</h4><p>생성물을 치우면(Q ↓) RT ln Q가 크게 음수 → ΔG′° &gt; 0이어도 ΔG &lt; 0 → 진행.</p></div>
 <div class="card"><h4><span class="no">2</span> ΔG′°는 상수, ΔG는 변수</h4><p>ΔG는 ΔG′°와 반응물·생성물 농도에 따라 달라진다.</p></div>
 <div class="card"><h4><span class="no">3</span> ΔG = 최대로 얻을 수 있는 일</h4><p>실제로는 일부가 엔트로피(열)로 손실 → 쓸 수 있는 일은 ΔG보다 적다.</p></div>
 <div class="card"><h4><span class="no">4</span> 유리한 반응도 활성화 에너지 필요</h4><figure class="fig">{hill(h=150, l='반응물', r='생성물', dg='ΔG < 0')}</figure></div>
 <div class="card"><h4><span class="no">5</span> 효소는 평형상수를 못 바꾼다</h4><p>효소 = Eₐ ↓ → <b>속도 ↑</b>. 정반응·역반응을 똑같이 빠르게 → K′<sub>eq</sub>, ΔG′° 그대로.</p></div>
 <div class="card"><h4><span class="no">6</span> ΔG′°는 더하고, K′<sub>eq</sub>는 곱한다</h4>
  {align([('', '포도당 + P<sub>i</sub> → G6P', '+13.8'), ('', 'ATP → ADP + P<sub>i</sub>', '−30.5'), ('합', '포도당 + ATP → G6P + ADP', '<span class="hl">−16.7</span>')], cls='sum')}
  <p class="small">헥소키나아제 반응. 뒤집으면 부호 반대, K는 역수.</p></div>
</div>''',
  ('P5', 'P9', 'P12', 'P13')))

SUMMARY.append(page('S8', 'ATP는 어떻게 일을 시키나? — 작용기 전달', 'Role of ATP · Slides 21–26',
  'ATP는 대부분 그냥 가수분해되지 않는다. <b>기질에 인산(또는 AMP)을 먼저 붙여 활성화</b>하고, 다음 단계에서 그 꼬리표가 떨어지며 반응이 진행된다 (2단계 반응).',
  f'''<div class="grid2"><div><div class="card"><h4>📌 2단계 반응 — 글루타민 합성 (슬라이드 22)</h4><figure class="fig">{two_step()}</figure>
 <p>겉보기 “글루탐산 + NH<sub>3</sub> + ATP → 글루타민 + ADP + P<sub>i</sub>”이지만, 실제로는 <b>공통 중간체(γ-글루타밀 인산)</b>를 통한 인산기 전달. 효소 안 양전하가 인산을 안정화해 Eₐ를 낮춘다.</p></div>
 <div class="card" style="margin-top:3mm"><h4>ATP의 공격 위치</h4>{table(['위치', '산물', '예'], [['γ (끝)', 'ADP + 기질–P', '대부분의 키나아제'], ['α', 'PP<sub>i</sub> + 기질–AMP', '지방산 활성화, DNA·RNA 합성, 루시페레이스']], cls='left')}
 <p class="small">ATP → AMP + PP<sub>i</sub> 후 PP<sub>i</sub> → 2P<sub>i</sub>(−19.2)까지 → 반응을 강하게 당긴다.</p></div></div>
<div><div class="card"><h4>ATP가 하는 일 (슬라이드 23–26)</h4>{table(['일', '어떻게'], [
  ['<b>빛</b> (반딧불이)', '루시페린 + ATP → 루시페릴-AMP + PP<sub>i</sub> → 빛 (루시페레이스)'],
  ['<b>능동수송</b>', 'Na⁺/K⁺ ATPase: 인산화 → 모양 변화 → 3Na⁺ 밖, 2K⁺ 안 (P형 ATPase)'],
  ['<b>근육 수축</b>', '마이오신이 ATP를 직접 가수분해 → 모양 변화로 액틴을 당김'],
  ['<b>거대분자 합성</b>', '단백질·핵산·다당류 조립에 ATP/GTP/UTP 사용']], cls='left')}
 <figure class="fig">{pump_svg()}</figure></div>
 {tip('디곡신(심장약)은 Na⁺/K⁺ ATPase를 억제해 심근 수축력을 높인다 — 약대 포인트!', '약학')}</div></div>''',
  ('P13', 'P23', 'P24', 'P25', 'P26')))

SUMMARY.append(page('S9', 'ATP보다 센 놈들 — 고에너지 화합물', 'Other energy sources · Slides 27–33',
  '인산기는 <b>높은 곳 → 낮은 곳</b>으로만 저절로 흐른다. ATP는 순위표의 <b>중간</b>이라, 위(PEP·1,3-BPG·PCr)에서 받아 아래(포도당 등)에 건네는 중계자.',
  f'''<div class="grid2"><div class="card"><h4>📌 순위 (표 13-6 · 그림 13-19)</h4><figure class="fig">{phos_ladder(hl=('PEP', '1,3-BPG', 'PCr', 'ATP', 'G6P'), height=280)}</figure>
 <p class="small">순서 외우기: <b>PEP &gt; 1,3-BPG &gt; PCr &gt; ATP &gt; G6P</b> (−61.9 &gt; −49.3 &gt; −43.0 &gt; −30.5 &gt; −13.8)</p></div>
<div><div class="card"><h4>왜 큰가? — 생성물이 특별히 안정해서</h4>{table(['화합물', '이유', '어디서'], [
  ['PEP', '엔올 → <b>케토</b> 피루브산으로 호변이성화 + P<sub>i</sub> 공명', '해당과정 10단계'],
  ['1,3-BPG', '아실인산(산무수물) → 생성물 이온화·공명', '해당과정 7단계'],
  ['포스포크레아틴', '크레아틴의 구아니디노기 공명 안정화', '근육의 <b>비상 배터리</b>'],
  ['아세틸-CoA (−31.4)', '<b>싸이오에스터</b>: S는 O보다 공명이 약해 반응물이 덜 안정', 'TCA 입구']], cls='left')}</div>
 <div class="card" style="margin-top:3mm"><h4>인산기 전달 계산 = 떼기 + 붙이기</h4>{align([('', 'PCr + H<sub>2</sub>O → Cr + P<sub>i</sub>', '−43.0'), ('', 'ADP + P<sub>i</sub> → ATP + H<sub>2</sub>O', '+30.5'), ('합', 'PCr + ADP → Cr + ATP', '<span class="hl">−12.5</span>')], cls='sum')}
 <p class="small">크레아틴 키나아제(CK). 혈중 CK ↑ = 근육·심근 손상 지표.</p></div></div></div>''',
  ('P12', 'P14', 'P20', 'P21')))

SUMMARY.append(page('S10', '생물학적 산화-환원 — 탄소의 산화 상태', 'Biological redox · Slides 35–38',
  '산화 = 전자(와 H)를 <b>잃음</b>, 환원 = <b>얻음</b>. 생물에서 연료의 산화는 대부분 <b>탈수소</b>. 탄소에 H가 많을수록 더 환원된(덜 탄) 연료 → 산화될 때 에너지가 많다.',
  f'''<div class="grid2"><div class="card"><h4>📌 탄소의 산화 상태 (그림 13-22)</h4><figure class="fig">{carbon_ox()}</figure>
 <p class="small">세는 법: 전기음성도 H &lt; C &lt; S &lt; N &lt; O. C–H 전자는 C 것(2), C–C는 반반(1), C–O는 O 것(0).</p></div>
<div><div class="card"><h4>포도당의 완전 산화</h4><div class="formula">C<sub>6</sub>H<sub>12</sub>O<sub>6</sub> + 6O<sub>2</sub> → 6CO<sub>2</sub> + 6H<sub>2</sub>O &nbsp; ΔG′° = −2,840</div>
 <p>포도당은 전자를 잃고(산화) O<sub>2</sub>는 전자를 얻는다(환원). 전자는 한 번에 가지 않고 NAD⁺·FAD 같은 운반체를 거쳐 단계적으로 O<sub>2</sub>까지 → 에너지를 조금씩 ATP로 저장.</p></div>
 <div class="card" style="margin-top:3mm"><h4>용어 정리</h4>{table(['용어', '뜻'], [['산화 (oxidation)', '전자를 잃음 · 탈수소 · O와 결합'], ['환원 (reduction)', '전자를 얻음 · 수소 첨가'], ['환원제 (전자 공여체)', '전자를 <b>주고</b> 자기는 산화됨 (예: NADH)'], ['산화제 (전자 수용체)', '전자를 <b>받고</b> 자기는 환원됨 (예: O<sub>2</sub>)'], ['짝 (conjugate redox pair)', '산화형 + 환원형 (예: NAD⁺/NADH)']], cls='left')}
 {key('지방(–CH<sub>2</sub>–)이 탄수화물(–CHOH–)보다 g당 에너지가 2배 이상 많은 이유 = 더 환원되어 있어서.')}</div></div></div>''',
  ('P27',)))

SUMMARY.append(page('S11', '전자의 흐름과 환원 전위 E′°', 'Slides 39–43 · Fig 13-23 · Table 13-7',
  '전자는 <b>E′°가 낮은(−) 쪽 → 높은(+) 쪽</b>으로 흐른다(물이 위에서 아래로 떨어지듯). 흐르는 전자는 일을 할 수 있다 (배터리처럼).',
  f'''<div class="grid2"><div><div class="card"><h4>전자가 옮겨 가는 4가지 방식 (슬라이드 41)</h4><ol style="margin:.2em 0;padding-left:1.3em">
 <li><b>전자 직접</b>: Fe<sup>2+</sup> + Cu<sup>2+</sup> → Fe<sup>3+</sup> + Cu<sup>+</sup></li><li><b>수소 원자</b>(H⁺ + e⁻): AH<sub>2</sub> + B → A + BH<sub>2</sub></li>
 <li><b>하이드라이드</b>(H⁻ = H⁺ + 2e⁻): NAD 탈수소효소</li><li><b>산소와 직접 결합</b>: R–CH<sub>3</sub> + ½O<sub>2</sub> → R–CH<sub>2</sub>OH</li></ol></div>
 <div class="card" style="margin-top:3mm"><h4>E′° 측정 (그림 13-23)</h4><figure class="fig" style="width:42%;float:left;margin:0 3mm 0 0">{img('fig13_23.png', '100%')}</figure>
 <p>기준 = <b>수소 전극 0.00 V</b>. 시험 짝(산화형·환원형 1 M)과 연결해 전압(기전력)을 잰다. 생화학 표준 E′°는 <b>pH 7</b> (2H⁺/H<sub>2</sub>는 −0.414 V).</p>
 <p>E′° 큼(+) = 전자를 잘 <b>받음</b> = 강한 산화제 (O<sub>2</sub>)<br>E′° 작음(−) = 전자를 잘 <b>줌</b> = 강한 환원제 (NADH)</p><div style="clear:both"></div></div></div>
<div class="card"><h4>📌 전자 사다리 (표 13-7)</h4><figure class="fig">{redox_ladder_big()}</figure>
 {warn('표의 반쪽 반응은 모두 “환원 방향”으로 적혀 있다. 실제로 산화되는 쪽도 <b>E′° 부호를 뒤집지 않는다</b>.', '함정')}</div></div>''',
  ('P28', 'P29', 'P32', 'P33')))

SUMMARY.append(page('S12', '전위차 → 자유에너지, 그리고 네른스트 식', 'Slides 44–46 · Worked Example 13-3',
  '전자가 떨어지는 높이(ΔE)가 클수록 나오는 에너지가 크다: <b>ΔG′° = −nFΔE′°</b>. 농도가 표준과 다르면 E도 ΔG처럼 보정한다.',
  f'''<div class="grid2"><div><div class="card"><h4>📌 공식</h4><div class="formula">ΔE′° = E′°<sub>전자 수용체</sub> − E′°<sub>전자 공여체</sub></div><div class="formula">ΔG′° = −nF ΔE′°</div>
 <p class="small">n = 이동 전자 수 (NADH·FAD는 2) · F = 96.48 kJ/V·mol · ΔE′° &gt; 0 → ΔG′° &lt; 0 → 자발</p></div>
 <div class="card" style="margin-top:3mm"><h4>예제 13-3 한 줄 풀이</h4><p>아세트알데하이드 + NADH + H⁺ → 에탄올 + NAD⁺</p>
 <p>ΔE′° = −0.197 − (−0.320) = +0.123 V → ΔG′° = −2 × 96.48 × 0.123 = <b>−23.7</b> → Q = 0.01이면 ΔG = −23.7 + 2.48 ln 0.01 = <b>−35.1 kJ/mol</b></p></div>
 <div class="card" style="margin-top:3mm"><h4>호흡 사슬 전체 (NADH → O<sub>2</sub>)</h4><p>ΔE′° = 0.816 − (−0.320) = 1.136 V → ΔG′° ≈ <b>−219 kJ/mol</b> → 실제로는 NADH 1개당 약 2.5 ATP</p></div></div>
<div><div class="card"><h4>실제 환원 전위 — 네른스트 식</h4><div class="formula">E = E′° + {F('RT', 'nF')} ln {F('[전자 수용체]', '[전자 공여체]')}</div>
 <p class="small">25 °C에서 RT/F = 0.0257 V. n = 2이면 0.0128 V → 농도비 10배마다 약 <b>30 mV</b>. (슬라이드의 0.0026 V는 0.026 V의 오기로 보임)</p>
 <figure class="fig">{e_line()}</figure></div>
 <div class="card" style="margin-top:3mm"><h4>🧠 두 식은 쌍둥이</h4>{table(['자유에너지', '환원 전위'], [['ΔG = ΔG′° + RT ln Q', 'E = E′° + (RT/nF) ln([수용체]/[공여체])'], ['ΔG′° = −RT ln K′<sub>eq</sub>', 'ΔG′° = −nFΔE′°']])}</div></div></div>''',
  ('WE3', 'P30', 'P31')))

SUMMARY.append(page('S13', '전자 운반체 — NAD · NADP · FAD · FMN', 'Slides 47–52',
  'ATP가 “에너지 운반체”라면, 이들은 “<b>전자 운반체</b>”. 연료에서 뺀 전자를 실어 나른다. 모두 <b>비타민</b>에서 만들어진다.',
  f'''<div class="grid2"><div><div class="card"><h4>NAD⁺ / NADH (니코틴아마이드)</h4><figure class="fig">{nad_svg()}</figure>
 <div class="formula">NAD<sup>+</sup> + 2e⁻ + 2H<sup>+</sup> → NADH + H<sup>+</sup> &nbsp; (E′° = −0.320 V)</div>
 <p class="small">탈수소효소가 기질의 H⁻(하이드라이드)를 니코틴아마이드 고리에 넘긴다. 환원되면 340 nm에서 빛을 흡수 → 효소 활성 측정에 이용.</p></div>
 <div class="card" style="margin-top:3mm"><h4>FAD · FMN (플래빈)</h4><p>리보플래빈(B<sub>2</sub>)에서. 효소에 단단히 붙은 <b>보결분자단</b>. 전자 <b>1개 또는 2개</b>를 받을 수 있다(세미퀴논 중간체). FADH<sub>2</sub> ≈ 1.5 ATP (NADH ≈ 2.5).</p></div></div>
<div><div class="card"><h4>📌 NAD vs NADP — 쓰임새 (슬라이드 51)</h4>{table(['', 'NAD⁺ / NADH', 'NADP⁺ / NADPH'], [['주 용도', '<b>이화</b> → ATP 생산', '<b>동화</b>(생합성)·항산화'], ['세포 속 비율', '[NAD⁺] ≫ [NADH] (산화에 유리)', '[NADPH] ≫ [NADP⁺] (환원에 유리)'], ['대표 경로', '해당과정·TCA·β-산화', '지방산·콜레스테롤 합성, 오탄당 인산 경로']])}</div>
 <div class="card" style="margin-top:3mm"><h4>비타민과 질병 (슬라이드 52)</h4>{table(['비타민', '조효소', '결핍'], [['나이아신 (B<sub>3</sub>, 니코틴산)', 'NAD⁺, NADP⁺', '<b>펠라그라</b>: 피부염·설사·치매 (3D)'], ['리보플래빈 (B<sub>2</sub>)', 'FAD, FMN', '구각염 등']], cls='left')}
 <p class="small">트립토판 → 나이아신 → NAD(P)의 니코틴아마이드. 옥수수 위주 식단(트립토판·나이아신 부족)에서 펠라그라 유행.</p></div></div></div>''',
  ()))

SUMMARY.append(page('S14', '13장 한 장 요약 + 시험 직전 체크리스트', 'Summary · Slide 53',
  '교수님 요약 슬라이드의 10줄을 시험에 나오는 숫자·공식과 함께 정리했다.',
  f'''<div class="grid3">
 <div class="card"><h4>① ATP와 자유에너지</h4><ol style="margin:.2em 0;padding-left:1.3em;font-size:.95em"><li>세포는 자유에너지원(ATP)이 필요</li><li>ΔG′°는 평형상수와 직접 관련: ΔG′° = −RT ln K′<sub>eq</sub></li><li>실제 ΔG는 농도에 따라: ΔG = ΔG′° + RT ln Q</li><li>흔한 생화학 반응 5가지 (C–C 형성·절단, 재배열·이성질화·제거, 자유 라디칼, 작용기 전달, 산화-환원)</li><li>ATP는 가수분해가 아니라 <b>작용기 전달</b>로 에너지 제공</li><li>거대분자 조립·능동수송·근육 수축에 ATP</li></ol></div>
 <div class="card"><h4>② 전자 흐름과 산화-환원</h4><ol start="7" style="margin:.2em 0;padding-left:1.3em;font-size:.95em"><li>전자의 흐름은 생물학적 일을 할 수 있다</li><li>산화 = e⁻·H를 잃음, 환원 = 얻음</li><li>E′°로 ΔG 계산: ΔG′° = −nFΔE′°</li><li>포도당 → CO<sub>2</sub>에는 전자 운반체(NAD⁺·FAD·FMN)가 필요</li></ol></div>
 <div class="card"><h4>✅ 시험 직전 체크리스트</h4><ul style="font-size:.95em"><li>☐ ΔG′° = −RT ln K′<sub>eq</sub>, ΔG = ΔG′° + RT ln Q</li><li>☐ ATP 가수분해 −30.5, 적혈구 ΔG<sub>p</sub> ≈ −52</li><li>☐ 가수분해 큰 이유 4가지</li><li>☐ PEP &gt; 1,3-BPG &gt; PCr &gt; ATP &gt; G6P</li><li>☐ ΔE′° = 받는 쪽 − 주는 쪽, ΔG′° = −nFΔE′°</li><li>☐ 효소는 평형 불변, 자발성 = ΔG</li><li>☐ NAD⁺ 이화 / NADPH 동화 · NADH 2.5 · FADH<sub>2</sub> 1.5 ATP</li><li>☐ RT: 25 °C 2.478 / 37 °C 2.578</li></ul></div>
</div>
<div class="grid2" style="margin-top:3mm"><div class="card"><h4>🔢 꼭 외울 숫자</h4><div class="tiles" style="grid-template-columns:repeat(3,1fr)">
 <div><b>ATP → ADP+Pᵢ</b><span>−30.5</span><small>kJ/mol</small></div><div><b>ATP → AMP+PPᵢ</b><span>−45.6</span><small>kJ/mol</small></div><div><b>PPᵢ → 2Pᵢ</b><span>−19.2</span><small>kJ/mol</small></div>
 <div><b>NAD⁺/NADH</b><span>−0.320</span><small>V</small></div><div><b>½O₂/H₂O</b><span>+0.816</span><small>V</small></div><div><b>F</b><span>96.48</span><small>kJ/V·mol</small></div></div></div>
 <div class="card"><h4>⚠️ 단골 함정 6가지</h4><ol style="margin:.2em 0;padding-left:1.3em;font-size:.95em"><li>ln ≠ log, e<sup>x</sup> ≠ 10<sup>x</sup></li><li>R은 J 단위, mM → M</li><li>물·H⁺(pH 7)는 K·Q에서 빼기</li><li>표 방향과 반대면 ΔG′° 부호 뒤집기</li><li>E′° 부호는 뒤집지 않기, n = 2</li><li>“체온”이면 37 °C (RT 2.578)</li></ol></div></div>''',
  ()))

# ------------------------------------------------------------------ glossary
GLOSS = [
 ('ATP', 'Adenosine Triphosphate', '아데노신 삼인산', '세포의 에너지 화폐. 인산 3개'),
 ('ADP', 'Adenosine Diphosphate', '아데노신 이인산', 'ATP가 인산 1개를 잃은 것'),
 ('AMP', 'Adenosine Monophosphate', '아데노신 일인산', '인산 1개. 에너지 부족 신호'),
 ('Pᵢ', 'inorganic Phosphate', '무기 인산', 'HPO₄²⁻ (가수분해로 떨어진 인산)'),
 ('PPᵢ', 'inorganic Pyrophosphate', '무기 피로인산', '인산 2개 덩어리. 곧 2Pᵢ로 분해'),
 ('GTP · CTP · UTP', 'Guanosine / Cytidine / Uridine Triphosphate', '구아노신·사이티딘·유리딘 삼인산', 'ATP와 같은 인산 꼬리를 가진 친척들'),
 ('NAD⁺ / NADH', 'Nicotinamide Adenine Dinucleotide (산화형 / 환원형)', '니코틴아마이드 아데닌 다이뉴클레오타이드', '이화용 전자 운반체 (나이아신)'),
 ('NADP⁺ / NADPH', 'NAD Phosphate', 'NAD 인산', '동화(생합성)·항산화용 전자 운반체'),
 ('FAD / FADH₂', 'Flavin Adenine Dinucleotide', '플래빈 아데닌 다이뉴클레오타이드', '효소에 붙은 전자 운반체 (리보플래빈)'),
 ('FMN', 'Flavin Mononucleotide', '플래빈 모노뉴클레오타이드', 'FAD의 작은 버전'),
 ('CoA (CoA-SH)', 'Coenzyme A', '조효소 A', '아실기를 싸이오에스터로 운반 (판토텐산)'),
 ('Acetyl-CoA', 'Acetyl Coenzyme A', '아세틸 조효소 A', '고에너지 싸이오에스터 (−31.4)'),
 ('PEP', 'Phosphoenolpyruvate', '포스포엔올피루브산', '가장 높은 인산 전달 전위 (−61.9)'),
 ('1,3-BPG', '1,3-Bisphosphoglycerate', '1,3-이인산글리세르산', '아실인산 (−49.3), 해당과정 중간체'),
 ('3PG · 2PG', '3- / 2-Phosphoglycerate', '3-·2-포스포글리세르산', '해당과정 중간체'),
 ('PCr · Cr', 'Phosphocreatine · Creatine', '포스포크레아틴 · 크레아틴', '근육의 비상 배터리 (−43.0)'),
 ('CK', 'Creatine Kinase', '크레아틴 키나아제', 'PCr + ADP ⇌ Cr + ATP. 근육 손상 지표'),
 ('G1P · G6P', 'Glucose 1- / 6-Phosphate', '포도당 1-·6-인산', 'G6P 가수분해 −13.8 (저에너지)'),
 ('F6P · F1,6BP', 'Fructose 6-Phosphate · Fructose 1,6-Bisphosphate', '과당 6-인산 · 과당 1,6-이인산', '해당과정 중간체'),
 ('DHAP · G3P(GAP)', 'Dihydroxyacetone Phosphate · Glyceraldehyde 3-Phosphate', '다이하이드록시아세톤 인산 · 글리세르알데하이드 3-인산', '3탄당 인산'),
 ('OAA', 'Oxaloacetate', '옥살로아세트산', 'TCA 회로 중간체'),
 ('α-KG', 'α-Ketoglutarate', 'α-케토글루타르산', 'TCA 회로 중간체'),
 ('β-HB', 'β-Hydroxybutyrate', 'β-하이드록시뷰티르산', '케톤체'),
 ('TPP', 'Thiamine Pyrophosphate', '티아민 피로인산', '탈카복실화 조효소 (B₁)'),
 ('UDP-glucose', 'Uridine Diphosphate Glucose', 'UDP-포도당', '활성화된 포도당 (−43.0)'),
 ('ΔG', 'Gibbs free-energy change', '(실제) 자유에너지 변화', '지금 농도에서 반응 방향'),
 ('ΔG°', 'standard free-energy change', '표준 자유에너지 변화', '1 M, 25 °C, pH 0 기준 상수'),
 ('ΔG′°', 'biochemical standard free-energy change', '생화학 표준 자유에너지 변화', 'pH 7 기준 상수'),
 ('ΔG<sub>p</sub>', 'phosphorylation potential', '인산화 전위', '세포 속 실제 ATP 가수분해 ΔG'),
 ('ΔH · ΔS', 'enthalpy · entropy change', '엔탈피 · 엔트로피 변화', '열 · 무질서도의 변화'),
 ('K′<sub>eq</sub>', 'equilibrium constant (pH 7)', '(생화학) 평형상수', '평형에서 [생성물]/[반응물]'),
 ('Q', 'mass-action ratio', '질량작용비', '지금의 [생성물]/[반응물]'),
 ('R · T', 'gas constant · absolute temperature', '기체 상수 · 절대온도', '8.315 J/mol·K · K 단위'),
 ('F', 'Faraday constant', '패러데이 상수', '96.48 kJ/V·mol'),
 ('n', 'number of electrons', '이동 전자 수', 'NADH·FAD는 2'),
 ('E · E° · E′°', 'reduction potential', '(실제·표준·생화학 표준) 환원 전위', '전자를 끌어당기는 힘 (V)'),
 ('ΔE′°', 'difference in standard reduction potential', '표준 환원 전위차', '수용체 − 공여체'),
 ('emf', 'electromotive force', '기전력', '두 반쪽 전지 사이 전압'),
 ('Eₐ', 'activation energy', '활성화 에너지', '반응 언덕의 높이. 효소가 낮춤'),
 ('LDH · ADH', 'Lactate / Alcohol Dehydrogenase', '젖산 / 알코올 탈수소효소', 'NADH를 쓰는 대표 탈수소효소'),
 ('Na⁺/K⁺ ATPase', 'sodium-potassium pump', '나트륨-칼륨 펌프', 'ATP 1개로 3Na⁺ 밖, 2K⁺ 안'),
 ('KEGG', 'Kyoto Encyclopedia of Genes and Genomes', '교토 유전자·유전체 백과사전', '대사 경로 데이터베이스'),
 ('mM · μM', 'millimolar · micromolar', '밀리몰농도 · 마이크로몰농도', '10⁻³ M · 10⁻⁶ M'),
]


def glossary_pages():
    half = (len(GLOSS) + 1) // 2
    out = []
    for k, chunk in enumerate([GLOSS[:half], GLOSS[half:]]):
        rows = [[f'<b>{a}</b>', f'<span class="en3">{e}</span>', h, m] for a, e, h, m in chunk]
        out.append(f'''<h2 class="pt"><span class="n">ABC</span> 13장 영어 약어·기호 총정리 ({k+1}/2) <span class="en2">Abbreviations</span></h2>
<p class="lead">문제·표에 나오는 약어를 모두 모았어. 뜻을 모르는 약어가 나오면 여기서 찾자.</p>
<div class="card" style="width:100%">{table(['약어·기호', '영어 원래 이름', '한글', '한 줄 뜻'], rows, cls='left gl')}</div>''')
    return out



# ------------------------------------------------------------------ per-page abbreviation strip
import re as _re
ABBR_KEYS = {
 'ATP': r'\bATP\b', 'ADP': r'\bADP\b', 'AMP': r'\bAMP\b', 'Pᵢ': r'(?<!P)P[iᵢ](?![a-zA-Z])', 'PPᵢ': r'PP[iᵢ]',
 'GTP · CTP · UTP': r'\b(GTP|CTP|UTP)\b', 'NAD⁺ / NADH': r'NAD(?!P)', 'NADP⁺ / NADPH': r'NADP', 'FAD / FADH₂': r'FAD',
 'FMN': r'FMN', 'CoA (CoA-SH)': r'CoA', 'Acetyl-CoA': r'아세틸-CoA|[Aa]cetyl-CoA', 'PEP': r'\bPEP\b', '1,3-BPG': r'BPG',
 '3PG · 2PG': r'\b[23]PG\b', 'PCr · Cr': r'PCr', 'CK': r'\bCK\b', 'G1P · G6P': r'\bG[16]P\b', 'F6P · F1,6BP': r'F6P|F1,6BP',
 'DHAP · G3P(GAP)': r'DHAP|\bG3P\b', 'OAA': r'\bOAA\b', 'α-KG': r'α-KG', 'β-HB': r'β-HB', 'TPP': r'\bTPP\b',
 'UDP-glucose': r'UDP', 'ΔG′°': r'ΔG′\s*°', 'ΔG°': r'ΔG°', 'ΔG': r'ΔG(?![′°p\s]*[′°p])', 'ΔG<sub>p</sub>': r'ΔG\s*p',
 'ΔH · ΔS': r'ΔH|ΔS', 'K′<sub>eq</sub>': r'K′\s*eq', 'Q': r'\bQ\b', 'R · T': r'\bRT\b|\bR\s*=', 'F': r'nF|\bF\s*=',
 'n': r'\bn\s*=', 'E · E° · E′°': r'\bE′\s*°|\bE\s*=', 'ΔE′°': r'ΔE', 'emf': r'emf|기전력', 'Eₐ': r'Eₐ',
 'LDH · ADH': r'\b(LDH|ADH)\b', 'Na⁺/K⁺ ATPase': r'ATPase', 'KEGG': r'KEGG', 'mM · μM': r'\b(mM|μM)\b',
}


def _plain(html):
    t = _re.sub(r'<(sub|sup)>', '', html)
    t = _re.sub(r'</(sub|sup)>', '', t)
    t = _re.sub(r'<[^>]+>', ' ', t)
    return t.replace('&nbsp;', ' ')


def abbr_strip(html, compact=False):
    t = _plain(html)
    found = [g for g in GLOSS if g[0] in ABBR_KEYS and _re.search(ABBR_KEYS[g[0]], t)]
    if not found:
        return ''
    chips = ''.join(f'<span class="ab"><b>{a}</b> <i>{e}</i> <em>{h}</em> <u>— {m}</u></span>' for a, e, h, m in found)
    return f'<div class="abbr{" cmp" if compact else ""}"><b class="h">🔤 이 페이지의 약어</b>{chips}</div>'

# ------------------------------------------------------------------ concept checks
CHECKS = [
 dict(id='C1', num='1', title='대사·ATP 기초', sec='S1–S3', level=1,
  q='''<p><b>1.</b> (O/X) 이화 경로는 큰 분자를 작은 분자로 분해하며 ATP·NADH를 만든다.</p>
<p><b>2.</b> (O/X) ATP는 열역학적으로도, 속도론적으로도 불안정해서 물속에서 금방 분해된다.</p>
<p><b>3.</b> (빈칸) ATP 가수분해의 ΔG′°는 ( &nbsp;&nbsp; ) kJ/mol이고, 큰 이유 4가지는 ① 전하 ( &nbsp;&nbsp; ) 해소 ② P<sub>i</sub>의 ( &nbsp;&nbsp; ) 안정화 ③ ( &nbsp;&nbsp; ) ④ ( &nbsp;&nbsp; ) 이다.</p>
<p><b>4.</b> (계산) 쥐 근육세포의 [ATP] = 8.05 mM, [ADP] = 0.93 mM, [P<sub>i</sub>] = 8.05 mM이다. 37 °C에서 ΔG<sub>p</sub>는?</p>''',
  answer=chips('1. <b>O</b>', '2. <b>X</b> (속도론적으로는 안정)', '3. <b>−30.5</b> / 반발 · 공명 · 이온화 · 수화', '4. ΔG<sub>p</sub> ≈ <b>−48.5 kJ/mol</b>'),
  explain=key('2번 함정: “열역학적으로 불안정(내리막) + 속도론적으로 안정(높은 Eₐ)” = 효소가 있을 때만 깨진다.') +
   steps('4번: Q = [ADP][P<sub>i</sub>]/[ATP] = (0.93×10<sup>−3</sup>)(8.05×10<sup>−3</sup>)/(8.05×10<sup>−3</sup>) = 9.3×10<sup>−4</sup>',
         'RT(37 °C) = 2.578 kJ/mol, ln(9.3×10<sup>−4</sup>) = −6.98 → RT ln Q = −18.0',
         'ΔG<sub>p</sub> = −30.5 − 18.0 = <span class="hl">−48.5 kJ/mol</span> (근육은 ATP가 많아 적혈구 −52와 비슷하게 큼)') +
   fig(hill(h=150), '열역학: 내리막 / 속도론: 언덕(Eₐ)이 높다') + tip('P<sub>i</sub>가 분자·분모에 같이 있어 지워지는 걸 눈치채면 계산이 쉬워진다.', '요령')),
 dict(id='C2', num='2', title='깁스 자유에너지와 표준 상태', sec='S4–S5', level=1,
  q='''<p><b>1.</b> (계산) 어떤 반응의 ΔH = −20 kJ/mol, ΔS = −0.050 kJ/mol·K이다. 25 °C(298 K)에서 ΔG는? 자발적인가? 온도를 400 K로 올리면?</p>
<p><b>2.</b> (O/X) ΔG′°는 반응물과 생성물의 농도에 따라 값이 달라진다.</p>
<p><b>3.</b> (O/X) ΔG°와 ΔG′°의 가장 큰 차이는 표준 pH (0 vs 7)이다.</p>
<p><b>4.</b> (빈칸) ΔG &lt; 0인 반응을 ( &nbsp;&nbsp; )에르곤 반응, ΔG &gt; 0인 반응을 ( &nbsp;&nbsp; )에르곤 반응이라 한다.</p>''',
  answer=chips('1. 298 K: <b>−5.1 kJ/mol</b> (자발) / 400 K: <b>0</b> (평형, 더 높으면 비자발)', '2. <b>X</b> (상수)', '3. <b>O</b>', '4. <b>발</b>에르곤 / <b>흡</b>에르곤'),
  explain=key('ΔG = ΔH − TΔS. ΔS가 음수(질서 ↑)면 온도가 높을수록 −TΔS가 커져 불리해진다.') +
   steps('298 K: ΔG = −20 − (298)(−0.050) = −20 + 14.9 = <span class="hl">−5.1 kJ/mol</span> → 자발',
         '400 K: ΔG = −20 − (400)(−0.050) = −20 + 20 = <span class="hl">0</span> → 평형. 400 K보다 높으면 ΔG &gt; 0 → 비자발',
         '발열(ΔH &lt; 0)이라도 무질서가 줄면(ΔS &lt; 0) 고온에선 안 일어날 수 있다 → 그래서 ΔG로 판단.') +
   fig(bars([('ΔH', 20, C['blue'], '−20 (유리)'), ('−TΔS (298 K)', 14.9, C['red'], '+14.9 (불리)'), ('−TΔS (400 K)', 20, C['red'], '+20 (불리)')], height=110), '') +
   tip('단위 통일: ΔS가 J/mol·K로 주어지면 ÷1000 해서 kJ로 바꿔야 ΔH와 더할 수 있다.', '함정')),
 dict(id='C3', num='3', title='평형상수 K′eq · Q · 효소', sec='S6–S7', level=1,
  q='''<p><b>1.</b> (계산) 25 °C에서 K′<sub>eq</sub> = 100인 반응의 ΔG′°는?</p>
<p><b>2.</b> (계산, 10배 규칙) ΔG′° = +5.7 kJ/mol인 반응의 K′<sub>eq</sub>는 대략?</p>
<p><b>3.</b> (판단) K′<sub>eq</sub> = 10인 반응에서 지금 Q = 1000이다. ΔG의 부호와 반응 방향은?</p>
<p><b>4.</b> (O/X) 효소는 K′<sub>eq</sub>를 크게 만들어 반응을 정방향으로 민다.</p>''',
  answer=chips('1. <b>−11.4 kJ/mol</b>', '2. K′<sub>eq</sub> ≈ <b>0.1</b>', '3. Q &gt; K → ΔG <b>&gt; 0</b> → <b>역반응</b>', '4. <b>X</b> (속도만 ↑, 평형 불변)'),
  explain=steps('1. ΔG′° = −2.478 × ln 100 = −2.478 × 4.61 = <span class="hl">−11.4 kJ/mol</span> (= 10배 두 번 → −5.7 × 2)',
                '2. +5.7 = “10배 한 번 반대 방향” → K = 10<sup>−1</sup> = <span class="hl">0.1</span>',
                '3. ΔG = RT ln(Q/K) = 2.478 × ln 100 = +11.4 → 양수 → 생성물이 너무 많다 → 역반응으로 평형을 향해 감',
                '4. 효소는 언덕(Eₐ)만 낮춘다. 정·역반응을 똑같이 빠르게 → 평형 위치(K) 그대로.') +
   fig(logaxis([(10, '평형 K = 10', C['navy']), (1000, '지금 Q = 1000', C['red'])], -1, 4, height=105, label='Q > K → 왼쪽(역반응)으로'), '') +
   key('Q와 K 비교 = 13장 방향 문제의 만능 열쇠.')),
 dict(id='C4', num='4', title='짝지은 반응과 ATP의 작용기 전달', sec='S7–S8', level=2,
  q='''<p><b>1.</b> (계산) A → B: ΔG′° = +12 kJ/mol, B → C: ΔG′° = −20 kJ/mol. A → C의 ΔG′°와 25 °C에서의 K′<sub>eq</sub>는?</p>
<p><b>2.</b> (빈칸) 글루타민 합성효소 반응에서 ATP의 인산이 먼저 붙은 공통 중간체는 ( &nbsp;&nbsp;&nbsp; )이다.</p>
<p><b>3.</b> (서술) ATP → AMP + PP<sub>i</sub>로 쪼개는 반응이 “거의 비가역”이 되는 이유는?</p>
<p><b>4.</b> (O/X) Na⁺/K⁺ ATPase는 ATP 1개로 Na⁺ 2개를 밖으로, K⁺ 3개를 안으로 옮긴다.</p>''',
  answer=chips('1. ΔG′° = <b>−8 kJ/mol</b>, K′<sub>eq</sub> ≈ <b>25</b>', '2. <b>γ-글루타밀 인산</b> (글루타밀-인산)', '3. PP<sub>i</sub>가 <b>피로인산가수분해효소</b>로 즉시 2P<sub>i</sub> (−19.2) → 생성물 제거', '4. <b>X</b> (Na⁺ 3개 밖, K⁺ 2개 안)'),
  explain=steps('1. 더하기: +12 + (−20) = <span class="hl">−8 kJ/mol</span> → K = e<sup>8/2.478</sup> = e<sup>3.23</sup> ≈ <span class="hl">25</span> (곱하기로도: K<sub>1</sub> × K<sub>2</sub>)',
                '2. ① 글루탐산 + ATP → γ-글루타밀 인산 + ADP ② + NH<sub>3</sub> → 글루타민 + P<sub>i</sub>. 공통 중간체가 있어야 짝지어진다.',
                '3. 르샤틀리에: 생성물 PP<sub>i</sub>가 계속 사라짐 + 인산무수물 결합 2개(ATP 2개 당량)를 쓰는 셈 → 역반응 불가.',
                '4. 3Na⁺ 밖 / 2K⁺ 안 → 알짜 양전하 1개가 밖으로 → 막전위 형성에 기여.') +
   fig(energy_steps([('A', 0, C['navy']), ('B', 12, C['red']), ('C', -8, C['green'])], height=180), '오르막 +12를 내리막 −20이 끌어내림') +
   tip('“3 나가고 2 들어온다” — 나트륨(Na)은 나가고(Out), 칼륨(K)은 들어온다(In).', '암기')),
 dict(id='C5', num='5', title='고에너지 인산 화합물', sec='S9', level=1,
  q='''<p><b>1.</b> (순서) 가수분해 ΔG′°가 더 음수인 순으로 나열하라: 포스포크레아틴, 포도당 6-인산, PEP, ATP(→ADP), 1,3-BPG</p>
<p><b>2.</b> (계산) PEP + ADP → 피루브산 + ATP의 ΔG′°는?</p>
<p><b>3.</b> (서술) PEP 가수분해의 ΔG′°가 특히 큰 가장 중요한 이유는?</p>
<p><b>4.</b> (O/X) 싸이오에스터(아세틸-CoA)의 가수분해는 같은 산소 에스터보다 ΔG′°가 덜 음수다.</p>''',
  answer=chips('1. <b>PEP &gt; 1,3-BPG &gt; PCr &gt; ATP &gt; G6P</b>', '2. −61.9 + 30.5 = <b>−31.4 kJ/mol</b>', '3. 생성물 엔올 피루브산이 <b>케토형으로 호변이성화</b>하며 크게 안정', '4. <b>X</b> (더 음수)'),
  explain=fig(phos_ladder(hl=('PEP', 'ATP'), flows=[('PEP', 'ATP', '−31.4')], height=250), '위에서 아래로 = 인산이 저절로 흐르는 방향') +
   steps('2. 떼기(PEP → 피루브산 + P<sub>i</sub>, −61.9) + 붙이기(ADP + P<sub>i</sub> → ATP, +30.5) = −31.4 → 해당과정 10단계(피루브산 키나아제)가 비가역인 이유.',
         '3. 반응물 PEP는 엔올 한 가지뿐, 생성물은 엔올 ⇌ 케토 → 케토형이 훨씬 안정(+ 엔트로피 이득) + P<sub>i</sub> 공명.',
         '4. S는 O보다 C=O와의 공명이 약해 싸이오에스터(반응물)가 덜 안정 → 깨질 때 더 많이 내려간다 (아세틸-CoA −31.4).')),
 dict(id='C6', num='6', title='산화-환원과 환원 전위', sec='S10–S11', level=2,
  q='''<p><b>1.</b> (순서) 가장 환원된 것부터: CH<sub>3</sub>COOH, CH<sub>3</sub>CH<sub>3</sub>, CO<sub>2</sub>, CH<sub>3</sub>CHO, CH<sub>3</sub>CH<sub>2</sub>OH</p>
<p><b>2.</b> (O/X) E′°가 더 음수인 짝의 산화형이 더 강한 산화제다.</p>
<p><b>3.</b> (계산) 푸마르산/숙신산 E′° = +0.031 V, NAD⁺/NADH E′° = −0.320 V. NADH가 푸마르산을 숙신산으로 환원하는 반응은 표준 조건에서 진행하는가? ΔG′°는?</p>
<p><b>4.</b> (빈칸) E′° 측정의 기준 전극은 ( &nbsp;&nbsp; ) 전극(0.00 V)이고, pH 7에서 2H⁺/H<sub>2</sub>의 E′°는 ( &nbsp;&nbsp; ) V이다.</p>''',
  answer=chips('1. <b>CH<sub>3</sub>CH<sub>3</sub> &gt; CH<sub>3</sub>CH<sub>2</sub>OH &gt; CH<sub>3</sub>CHO &gt; CH<sub>3</sub>COOH &gt; CO<sub>2</sub></b>', '2. <b>X</b> (더 양수가 강한 산화제)', '3. <b>진행</b>, ΔE′° = +0.351 V, ΔG′° ≈ <b>−67.7 kJ/mol</b>', '4. <b>수소</b> / <b>−0.414</b>'),
  explain=fig(ladder([('푸마르산/숙신산', 0.031), ('NAD⁺/NADH', -0.320)], -0.36, 0.08, hl=('푸마르산/숙신산', 'NAD⁺/NADH'), flows=[('NAD⁺/NADH', '푸마르산/숙신산', '2e⁻')], height=160), '아래(−) → 위(+)로 전자가 흐른다') +
   steps('1. H가 많을수록 환원, O가 붙을수록 산화 (빨간 탄소 전자 7 → 5 → 3 → 1 → 0).',
         '2. 산화제 = 전자를 빼앗는 놈 = 전자 욕심이 큰 놈 = E′°가 <b>더 양수</b>.',
         '3. 받는 쪽 푸마르산(+0.031) − 주는 쪽 NADH(−0.320) = +0.351 V &gt; 0 → 진행. ΔG′° = −2 × 96.48 × 0.351 = <span class="hl">−67.7 kJ/mol</span>') +
   tip('전자는 “물처럼 아래로” 가 아니라 “E′° 숫자가 커지는 쪽”으로 간다고 기억하면 헷갈리지 않아.', '요령')),
 dict(id='C7', num='7', title='네른스트 식 · ΔG = −nFΔE · 전자 운반체', sec='S12–S13', level=2,
  q='''<p><b>1.</b> (계산) 25 °C에서 [NAD⁺] : [NADH] = 100 : 1인 용액의 실제 환원 전위 E는? (E′° = −0.320 V, n = 2)</p>
<p><b>2.</b> (계산) ΔE′° = +0.20 V, n = 2인 산화-환원 반응의 ΔG′°는?</p>
<p><b>3.</b> (빈칸) NADH는 주로 ( &nbsp;&nbsp; ) 반응(ATP 생산)에, NADPH는 주로 ( &nbsp;&nbsp; ) 반응에 쓰인다. 나이아신이 부족하면 ( &nbsp;&nbsp; )이 생긴다.</p>
<p><b>4.</b> (O/X) FAD는 전자를 한 번에 1개씩도 받을 수 있지만 NAD⁺는 하이드라이드(전자 2개)로만 받는다.</p>''',
  answer=chips('1. E ≈ <b>−0.261 V</b>', '2. ΔG′° ≈ <b>−38.6 kJ/mol</b>', '3. <b>이화</b> / <b>동화(생합성)</b> / <b>펠라그라</b>', '4. <b>O</b>'),
  explain=steps('1. E = E′° + (RT/2F) ln([NAD⁺]/[NADH]) = −0.320 + 0.0128 × ln 100 = −0.320 + 0.0128 × 4.61 = <span class="hl">−0.261 V</span> (100배 = 30 mV × 2 ≈ 59 mV 상승)',
                '2. ΔG′° = −nFΔE′° = −2 × 96.48 × 0.20 = <span class="hl">−38.6 kJ/mol</span>',
                '3. NAD⁺/NADH 비는 높게(산화에 유리), NADPH/NADP⁺ 비는 높게(환원·합성에 유리) 유지된다.',
                '4. 플래빈은 세미퀴논(전자 1개) 중간체가 있어 1개·2개 모두 가능.') +
   fig(e_line(), '산화형(NAD⁺)이 많을수록 E가 + 쪽으로') +
   key('ΔG ↔ E 쌍둥이 식: ΔG = ΔG′° + RT ln Q ↔ E = E′° + (RT/nF) ln(수용체/공여체)')),
]

# where to insert each check (after which summary page index, 0-based)
CHECK_AFTER = {2: 'C1', 4: 'C2', 6: 'C3', 7: 'C4', 8: 'C5', 10: 'C6', 12: 'C7'}


def render_check(it):
    return f'''
<div class="ph"><div class="badge" style="background:#7c3aed"><small>개념 확인</small><b>{it['num']}</b></div>
 <div class="ttl"><span class="ko">{it['title']}</span><span class="en">관련 요약 ▸ {it['sec']}</span></div>
 <div class="meta"><span class="tag">스스로 점검</span>{stars(it['level'])}</div></div>
<div class="cols">
 <div class="col">
  <div class="blk trans"><span class="lab" style="background:#7c3aed">문제</span>{it['q']}</div>
  <div class="blk blank"><span class="lab">풀이 · 직접 풀어 보기</span><span class="hint">오른쪽을 가리고 풀어 보세요</span></div>
  {abbr_strip(it['q'] + it['answer'] + it['explain'], True)}
 </div>
 <div class="col">
  <div class="blk ans"><span class="lab">정답</span>{it['answer']}</div>
  <div class="blk exp"><span class="lab">해설</span>{it['explain']}</div>
 </div>
</div>'''


def cover():
    return f'''
<div class="eyebrow">LEHNINGER PRINCIPLES OF BIOCHEMISTRY · 8TH EDITION</div>
<h1>Chapter 13<br><span>생체에너지론</span><br>시험대비 요약노트</h1>
<div class="sub">개념 요약 14쪽 + 개념확인 문제 7세트 + 영어 약어 총정리</div>
<div class="en">“풀이노트의 문제를 풀기 전에 이 노트로 개념부터”</div>
<div class="stats">
 <div class="stat"><b>14</b><span>개념 요약 페이지<br>(강의 슬라이드 순서)</span></div>
 <div class="stat"><b>{len(CHECKS)}</b><span>개념확인 문제 세트<br>(OX·빈칸·계산)</span></div>
 <div class="stat"><b>{len(GLOSS)}</b><span>영어 약어·기호<br>총정리</span></div>
</div>
<div class="how"><h3>HOW TO USE · 이렇게 보세요</h3>
 <div style="background:#1e3a8a"><b>① 요약 읽기</b>그림과 한 줄 요약으로 개념 잡기</div>
 <div style="background:#7c3aed"><b>② 개념확인</b>OX·빈칸·짧은 계산으로 점검</div>
 <div style="background:#ea580c"><b>③ 풀이노트로</b>각 페이지 아래 “📒”에 적힌 문제·쪽수로 이동</div>
 <div style="background:#0f766e"><b>④ 약어 찾기</b>모르는 약어는 맨 뒤 약어 총정리</div>
 <p style="font-size:8.5pt;color:#cbd5e1;margin-top:3mm">함께 볼 파일: <b>레닌저 13장 예제·문제 풀이노트.pdf</b><br>📒 옆의 p.번호 = 풀이노트의 쪽번호</p>
</div>'''


def toc():
    rows = []
    for k, pg in enumerate(SUMMARY):
        t = pg.split('</span> ', 1)[1].split(' <span class="en2">')[0]
        rows.append(f'<tr><td class="no">S{k+1}</td><td>{t}</td></tr>')
    rows2 = [f'<tr><td class="no">개념확인 {c["num"]}</td><td>{c["title"]} <span class="en">({c["sec"]})</span></td></tr>' for c in CHECKS]
    rows2.append('<tr><td class="no">ABC</td><td>영어 약어·기호 총정리</td></tr>')
    return f'''<h2 class="pt"><span class="n">INDEX</span> 차례와 풀이노트 연결표</h2>
<div class="grid2"><div class="card"><h4>📘 개념 요약</h4><table class="toc">{''.join(rows)}</table></div>
<div><div class="card"><h4>✏️ 개념확인 · 부록</h4><table class="toc">{''.join(rows2)}</table></div>
<div class="card" style="margin-top:3mm"><h4>📒 풀이노트 문제는 어디서 배우나?</h4>{table(['요약', '풀이노트 문제'], [
 ['S2–S3 ATP', '예제 13-2, 문제 7·8·10·15·22'], ['S4–S7 ΔG·K·Q', '예제 13-1, 문제 1–6·9'], ['S7–S8 짝지음·작용기 전달', '문제 5·9·12·13·23–26'],
 ['S9 고에너지 화합물', '문제 12·14·20·21'], ['S10–S11 산화환원·E′°', '문제 27·28·29·32·33'], ['S12 ΔG = −nFΔE', '예제 13-3, 문제 30·31']], cls='left')}</div></div></div>'''


EXTRA_CSS = r'''
.abbr { margin-top: 2.5mm; background: #f5f3ff; border: 1px solid #ddd6fe; border-radius: 8px; padding: 1.4mm 3mm; font-size: 8.4pt; line-height: 1.5; display: flex; flex-wrap: wrap; gap: 1.2mm 2mm; align-items: center; flex: none; }
.abbr .h { color: #6d28d9; margin-right: 1mm; }
.abbr .ab { background: white; border: 1px solid #e9d5ff; border-radius: 6px; padding: 0 2mm; white-space: nowrap; }
.abbr .ab b { color: #5b21b6; }
.abbr .ab i { font-family: 'Noto Serif'; color: #475569; }
.abbr .ab em { font-style: normal; color: #1f2937; }
.abbr .ab u { text-decoration: none; color: #7c3aed; }
.abbr.cmp .ab { white-space: normal; }
.abbr.cmp { font-size: calc(7.6pt * var(--s)); margin-top: 0; }

.wlink { margin-top: 2.5mm; background: #fff7ed; border: 1px dashed #fb923c; border-radius: 8px; padding: 1.4mm 4mm; font-size: 9pt; display: flex; flex-wrap: wrap; gap: 2mm; align-items: center; }
.wlink b { color: #c2410c; margin-right: 2mm; }
.wl { background: white; border: 1px solid #fdba74; border-radius: 999px; padding: 0 3mm; }
.wl i { color: #ea580c; font-style: normal; font-weight: 700; font-family: 'JetBrains Mono'; font-size: 8.5pt; }
h2.pt .en2 { font-size: 9pt; color: #94a3b8; font-weight: 500; margin-left: auto; font-family: 'Noto Serif'; font-style: italic; }
.card ol li, .card ul li { margin: .5mm 0; }
.card ul { padding-left: 1.2em; margin: 1mm 0; }
.en3 { font-family: 'Noto Serif'; font-style: italic; color: #475569; font-size: .92em; }
table.gl { width: 100%; } table.gl td { padding: .6mm 2.5mm; }
.front .formula { font-size: 11pt; }
.front table.tb { margin: 1.5mm auto; }
'''

FIT = r'''<script>
for (const pg of document.querySelectorAll('.pg.front')) {
  const fw = pg.querySelector('.fw');
  const avail = pg.clientHeight - 19 * 3.78;
  let z = 1.0; fw.style.zoom = z;
  const h = () => fw.getBoundingClientRect().height;
  if (h() > avail) { while (h() > avail && z > 0.6) { z -= 0.02; fw.style.zoom = z.toFixed(2); } }
  else { while (z < 1.45) { fw.style.zoom = (z + 0.02).toFixed(2); if (h() > avail) { fw.style.zoom = z.toFixed(2); break; } z += 0.02; } }
  pg.dataset.z = fw.style.zoom;
}
window.FIT = [];
for (const pg of document.querySelectorAll('.pg.item')) {
  const r = [pg.dataset.id];
  for (const c of pg.querySelectorAll('.col')) {
    let s = 1.0; c.style.setProperty('--s', s);
    const ov = () => c.scrollHeight > c.clientHeight + 1;
    while (ov() && s > 0.55) { s -= 0.02; c.style.setProperty('--s', s.toFixed(2)); }
    r.push(+s.toFixed(2), ov());
  }
  window.FIT.push(r);
}
window.ZOOM = [...document.querySelectorAll('.pg.front')].map(p => p.dataset.z);
</script>'''


def build():
    P = B.Pager()
    P.add(cover(), 'cover')
    P.add(toc(), 'front')
    for k, pg in enumerate(SUMMARY):
        strip = abbr_strip(pg)
        if '<div class="wlink">' in pg:
            pg = pg.replace('<div class="wlink">', strip + '<div class="wlink">', 1)
        else:
            pg = pg + strip
        P.add(pg, 'front')
        if k in CHECK_AFTER:
            c = [x for x in CHECKS if x['id'] == CHECK_AFTER[k]][0]
            P.add(render_check(c), 'item')
    for g in glossary_pages():
        P.add(g, 'front')
    html = P.html().replace('Lehninger 8e · Ch.13 생체에너지론 — 예제 &amp; 연습문제 풀이 노트', FOOT)
    doc = f'''<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>{FOOT}</title>
<style>{B.CSS}{EXTRA_CSS}</style></head><body>{html}{FIT}</body></html>'''
    open(os.path.join(HERE, 'exam_ch13.html'), 'w').write(doc)
    return len(P.pages)


def render():
    from playwright.sync_api import sync_playwright
    import pymupdf
    n = build()
    tmp = os.path.join(HERE, 'exam_ch13_tmp.pdf')
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome')
        pg = b.new_page()
        pg.goto('file://' + os.path.join(HERE, 'exam_ch13.html'))
        pg.wait_for_timeout(900)
        print('fit', pg.evaluate('window.FIT'))
        print('zoom', pg.evaluate('window.ZOOM'))
        pg.pdf(path=tmp, width='320mm', height='200mm', print_background=True, prefer_css_page_size=True)
        b.close()
    d = pymupdf.open(tmp)
    d.set_metadata({'title': FOOT, 'author': 'Claude'})
    d.save(os.path.join(HERE, 'exam_ch13.pdf'), garbage=3, deflate=True)
    print('pages', len(d), 'expected', n)


if __name__ == '__main__':
    render()
