# -*- coding: utf-8 -*-
"""Chapter 16 — The Citric Acid Cycle"""
import math
from helpers import *

CHAPTER = '16'
CH_TITLE = '시트르산 회로'
CH_EN = 'The Citric Acid Cycle'
STAT = ('8', '회로 단계 (지도 수록)')
SCOPE = ('교수님 16장 강의(슬라이드 1–54) 범위 = <b>16.1 아세틸-CoA 생성(PDH)</b>, <b>16.2 시트르산 회로의 반응</b>, '
         '<b>16.3 조절</b>, <b>16.4 글리옥실산 회로</b> — 16장 전체. 16장에는 본문 예제가 없어.')
INCLUDE = ['<b>회로 전체·에너지</b> — 문제 2, 4, 14',
           '<b>PDH 복합체·조효소·비타민</b> — 문제 6, 7, 11, 12, 18, 32',
           '<b>개별 반응·계산</b> — 문제 8, 10, 15, 31',
           '<b>중간체 보충(보충 반응)·양방향성</b> — 문제 9, 13, 19, 20, 22–24',
           '<b>조절·산소</b> — 문제 25, 27–30, 33, 34']
EXCLUDE = ['<b>문제 35</b> — DATA ANALYSIS PROBLEM']

ALL_ITEMS = []


def add(**kw):
    kw.setdefault('section', '연습문제')
    kw.setdefault('kind', 'PROBLEM')
    ALL_ITEMS.append(kw)


def tca_wheel(hl=(), block=None, width=520, height=330):
    """circular TCA cycle diagram. hl: node names to highlight; block: index of arrow to mark ✕"""
    R = min(150, (height - 130) / 2)
    cx, cy = 260, height / 2 + 7
    nodes = ['옥살로아세트산', '시트르산', '아이소시트르산', 'α-케토글루타르산', '숙시닐-CoA', '숙신산', '푸마르산', '말산']
    outs = ['NADH', '', '', 'NADH + CO₂', 'NADH + CO₂', 'GTP(ATP)', 'FADH₂', '']
    b = arrowdef('tw', C['gray']) + arrowdef('tw2', C['orange'])
    pts = []
    for i in range(8):
        a = -math.pi / 2 + i * 2 * math.pi / 8
        pts.append((cx + R * math.cos(a), cy + R * math.sin(a)))
    for i in range(8):
        x1, y1 = pts[i]
        x2, y2 = pts[(i + 1) % 8]
        # shorten
        dx, dy = x2 - x1, y2 - y1
        L = math.hypot(dx, dy)
        sx, sy = x1 + dx * 0.24, y1 + dy * 0.24
        ex, ey = x1 + dx * 0.76, y1 + dy * 0.76
        col = C['red'] if block == i else C['gray']
        b += f'<line x1="{sx:.1f}" y1="{sy:.1f}" x2="{ex:.1f}" y2="{ey:.1f}" stroke="{col}" stroke-width="2" marker-end="url(#tw)"/>'
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        ox, oy = (mx - cx) / R * 44, (my - cy) / R * 44
        lab = outs[(i + 1) % 8]
        if block == i:
            b += T(mx, my + 5, '✕', 20, C['red'], weight=900)
        if lab:
            b += T(mx + ox, my + oy + 4, lab, 10.5, C['orange'], weight=700)
    for i, (x, y) in enumerate(pts):
        h = nodes[i] in hl
        w = 108
        b += f'<rect x="{x-w/2:.1f}" y="{y-13:.1f}" width="{w}" height="26" rx="13" fill="{"#fff7ed" if h else "white"}" stroke="{C["orange"] if h else C["navy"]}" stroke-width="{2.4 if h else 1.6}"/>'
        b += T(x, y + 4, nodes[i], 10.5, C['orange'] if h else C['navy'], weight=700)
    b += T(cx, cy - 6, '시트르산 회로', 13, C['navy'], weight=900)
    b += T(cx, cy + 12, '(미토콘드리아 기질)', 10, C['gray'])
    b += T(cx, cy - R - 42, '아세틸-CoA (C2)', 11, C['orange'], weight=900)
    b += f'<line x1="{cx}" y1="{cy-R-36}" x2="{cx+30}" y2="{pts[0][1]+22}" stroke="{C["orange"]}" stroke-width="2" marker-end="url(#tw2)"/>'
    return svg(width, height, b)


TCA = [('1', '아세틸-CoA + OAA + H<sub>2</sub>O → 시트르산 + CoA', '시트르산 생성효소', '−32.2', '축합 (C–C 결합), <b>조절</b>'),
       ('2', '시트르산 ⇌ 아이소시트르산', '아코니테이스 (Fe–S)', '+13.3', '이성질화 (탈수 → 수화)'),
       ('3', '아이소시트르산 + NAD<sup>+</sup> → α-KG + CO<sub>2</sub> + NADH', '아이소시트르산 탈수소효소', '−20.9', '산화적 탈카복실화, <b>조절</b>'),
       ('4', 'α-KG + CoA + NAD<sup>+</sup> → 숙시닐-CoA + CO<sub>2</sub> + NADH', 'α-KG 탈수소효소 복합체', '−33.5', '산화적 탈카복실화 (PDH와 같은 방식), <b>조절</b>'),
       ('5', '숙시닐-CoA + GDP + P<sub>i</sub> ⇌ 숙신산 + CoA + GTP', '숙시닐-CoA 합성효소', '−2.9', '기질 수준 인산화'),
       ('6', '숙신산 + FAD ⇌ 푸마르산 + FADH<sub>2</sub>', '숙신산 탈수소효소 (막에 박힘)', '0', '산화 (FAD) — 말론산이 경쟁적 억제'),
       ('7', '푸마르산 + H<sub>2</sub>O ⇌ L-말산', '푸마레이스', '−3.8', '수화'),
       ('8', 'L-말산 + NAD<sup>+</sup> ⇌ OAA + NADH + H<sup>+</sup>', '말산 탈수소효소', '+29.7', '산화 (OAA가 낮아 진행)')]


def front_pages():
    t = table(['단계', '반응', '효소', 'ΔG′°', '반응 유형 · 포인트'], TCA, cls='left')
    p1 = f'''<h2 class="pt"><span class="n">MAP</span> 시트르산 회로 8단계 한눈에</h2>
<p class="lead">아세틸-CoA(C2) 1개가 들어가면 CO<sub>2</sub> 2개가 나가고, <b>NADH 3 · FADH<sub>2</sub> 1 · GTP(ATP) 1</b>이 생긴다. 옥살로아세트산(OAA)은 소모되지 않고 다시 만들어진다(촉매처럼).</p>
<div class="card">{t}</div>
<div class="grid2" style="margin-top:3mm">
 <div class="card"><h4>➡️ 입구: 피루브산 탈수소효소(PDH) 복합체</h4>
  <div class="formula" style="font-size:10.5pt">피루브산 + CoA + NAD<sup>+</sup> → 아세틸-CoA + CO<sub>2</sub> + NADH &nbsp; (ΔG′° = −33.4)</div>
  <p>E1(TPP) → E2(리포산, CoA) → E3(FAD, NAD<sup>+</sup>) · 조효소 5개: <b>TPP·리포산·CoA·FAD·NAD<sup>+</sup></b> (비타민 B<sub>1</sub>·판토텐산·B<sub>2</sub>·나이아신)</p></div>
 <div class="card"><h4>🧮 알짜 반응식 (아세틸-CoA 1개)</h4>
  <div class="formula" style="font-size:10pt">아세틸-CoA + 3NAD<sup>+</sup> + FAD + GDP + P<sub>i</sub> + 2H<sub>2</sub>O → 2CO<sub>2</sub> + CoA + 3NADH + FADH<sub>2</sub> + GTP + 2H<sup>+</sup></div>
  <p class="small">포도당 1개 = 아세틸-CoA 2개 → 회로 2바퀴. NADH ≈ 2.5 ATP, FADH<sub>2</sub> ≈ 1.5 ATP → 포도당당 약 30–32 ATP</p></div>
</div>'''
    p2 = f'''<h2 class="pt"><span class="n">KIT</span> 회로 그림 · 조절 · 보충 반응</h2>
<div class="grid2">
 <div class="card"><figure class="fig">{tca_wheel()}</figure></div>
 <div>
  <div class="card"><h4><span class="no">1</span> 조절 지점 4곳 (모두 평형에서 먼 반응)</h4>
   <p><b>PDH</b>: − 아세틸-CoA, NADH, ATP (+ PDH 키나아제 인산화 → 불활성) / + AMP, CoA, NAD<sup>+</sup>, Ca<sup>2+</sup></p>
   <p><b>시트르산 생성효소</b>: − NADH, 숙시닐-CoA, 시트르산, ATP / + ADP</p>
   <p><b>아이소시트르산 DH</b>: − ATP / + ADP, Ca<sup>2+</sup> &nbsp; <b>α-KG DH</b>: − 숙시닐-CoA, NADH / + Ca<sup>2+</sup></p>
   {key('신호는 두 가지: <b>에너지 충분(ATP·NADH ↑) → 느리게</b>, 에너지 부족(ADP·NAD<sup>+</sup>·Ca<sup>2+</sup> ↑) → 빠르게.')}</div>
  <div class="card" style="margin-top:3mm"><h4><span class="no">2</span> 양방향성(amphibolic) &amp; 보충(anaplerotic) 반응</h4>
   <p>중간체가 생합성으로 빠져나감: α-KG → 글루탐산, OAA → 아스파르트산·당신생, 숙시닐-CoA → 헴, 시트르산 → 지방산</p>
   <p>빠진 만큼 채움: <b>피루브산 카복실화효소</b> (피루브산 + HCO<sub>3</sub><sup>−</sup> + ATP → OAA, 아세틸-CoA가 활성화) 가 가장 중요</p></div>
  <div class="card" style="margin-top:3mm"><h4><span class="no">3</span> 글리옥실산 회로 (식물·미생물)</h4>
   <p>아이소시트르산 분해효소 + 말산 생성효소로 CO<sub>2</sub> 2개가 나가는 단계를 건너뜀 → 아세틸-CoA 2개 → 숙신산 1개 → <b>지방으로 포도당 합성 가능</b>. 척추동물은 불가.</p></div>
 </div>
</div>'''
    return [p1, p2]


# ------------------------------------------------------------------ items
add(id='P2', num='2', en_title='Net Equation for Glycolysis and the Citric Acid Cycle', ko_title='해당과정 + 시트르산 회로의 알짜 반응식',
    slides='강의 슬라이드 4–5, 15', level=2,
    en='<p>Write the net biochemical equation for the metabolism of a molecule of glucose by glycolysis and the citric acid cycle, including all cofactors.</p>',
    ko='<p>포도당 한 분자가 해당과정과 시트르산 회로로 대사되는 알짜 생화학 반응식을 모든 조효소를 포함해 써라.</p>',
    answer=chips('포도당 + 2H<sub>2</sub>O + 10NAD<sup>+</sup> + 2FAD + 4ADP + 4P<sub>i</sub> → 6CO<sub>2</sub> + 10NADH + 2FADH<sub>2</sub> + 4ATP (+ H<sup>+</sup>)'),
    explain=key('세 구간(해당과정 · PDH ×2 · 회로 ×2)을 각각 쓰고 <b>더한다</b>. 피루브산·아세틸-CoA·CoA 같은 중간체는 지워진다.') +
    align([('해당과정', '포도당 + 2NAD<sup>+</sup> + 2ADP + 2P<sub>i</sub> → 2 피루브산 + 2NADH + 2ATP + 2H<sub>2</sub>O', ''),
           ('PDH ×2', '2 피루브산 + 2CoA + 2NAD<sup>+</sup> → 2 아세틸-CoA + 2CO<sub>2</sub> + 2NADH', ''),
           ('회로 ×2', '2 아세틸-CoA + 6NAD<sup>+</sup> + 2FAD + 2GDP + 2P<sub>i</sub> + 4H<sub>2</sub>O → 4CO<sub>2</sub> + 6NADH + 2FADH<sub>2</sub> + 2GTP + 2CoA', ''),
           ('합', '포도당 + 2H<sub>2</sub>O + 10NAD<sup>+</sup> + 2FAD + 4ADP + 4P<sub>i</sub> → 6CO<sub>2</sub> + 10NADH + 2FADH<sub>2</sub> + 4ATP', '')], cls='sum') +
    fig(bars([('NADH', 10, C['blue'], '10개 (해당 2 + PDH 2 + 회로 6)'), ('FADH₂', 2, C['green'], '2개'), ('ATP(+GTP)', 4, C['orange'], '4개'), ('CO₂', 6, C['gray'], '6개 = 포도당의 탄소 6개 전부')],
             height=150), '') +
    tip('ATP는 직접 4개뿐이지만, NADH 10개·FADH<sub>2</sub> 2개가 전자전달계(19장)에서 약 26–28 ATP를 더 만든다 → 총 30–32 ATP. 회로의 진짜 산물은 “전자(NADH)”!', '큰 그림') +
    warn('GTP는 ATP로 셌어(문제 14). H<sup>+</sup>는 생화학 반응식 관례상 정확히 맞추지 않아도 돼.', '참고'))

add(id='P4', num='4', en_title='Relationship between Energy Release and the Oxidation State of Carbon', ko_title='에너지 방출과 탄소 산화 상태의 관계',
    slides='13장 슬라이드 38 · 16장 슬라이드 4', level=1,
    en='<p>A eukaryotic cell can use glucose (C<sub>6</sub>H<sub>12</sub>O<sub>6</sub>) and hexanoate (C<sub>6</sub>H<sub>11</sub>O<sub>2</sub><sup>−</sup>) as fuels for cellular respiration. On the basis of their structural formulas, which substance releases more energy per gram on complete combustion to CO<sub>2</sub> and H<sub>2</sub>O?</p>',
    ko='<p>진핵세포는 포도당(C<sub>6</sub>H<sub>12</sub>O<sub>6</sub>)과 헥산산염(C<sub>6</sub>H<sub>11</sub>O<sub>2</sub><sup>−</sup>)을 세포 호흡의 연료로 쓸 수 있다. 구조식을 바탕으로 판단할 때, CO<sub>2</sub>와 H<sub>2</sub>O로 완전 연소될 때 그램당 에너지를 더 많이 내는 것은?</p>',
    answer=chips('<b>헥산산염</b>이 그램당 에너지를 더 많이 낸다', '탄소가 더 <b>환원</b>되어 있음 (O가 적고 H가 많음)'),
    explain=key('연소 = 탄소가 CO<sub>2</sub>까지 산화되는 것. 처음에 <b>덜 산화된(환원된) 탄소</b>일수록 갈 길이 멀어 에너지가 많이 나온다(13장 문제 27).') +
    table(['', '포도당', '헥산산염'], [['구조', 'C 6개 중 5개에 –OH, 1개는 C=O', '–CH<sub>3</sub>, –CH<sub>2</sub>– ×4, –COO<sup>−</sup>'],
                                  ['O 원자 수', '6개 (탄소 1개당 1개)', '2개 (끝 탄소 하나에만)'],
                                  ['탄소 상태', '이미 반쯤 산화', '대부분 환원 (지방산과 같음)'],
                                  ['그램당 에너지', '적음', '<b>많음 (약 2배)</b>']]) +
    steps('포도당의 탄소는 이미 산소와 결합(–CHOH–)해 있어 “반쯤 탄 연료”.',
          '헥산산염은 탄소 6개 중 5개가 C–H로 둘러싸인 탄화수소 사슬 → 태울 거리가 훨씬 많다.',
          '게다가 포도당은 산소 원자 무게(16 × 6)가 분자량의 절반을 차지 → 그램당 에너지가 더 낮아진다.') +
    tip('지방(약 9 kcal/g)이 탄수화물(약 4 kcal/g)보다 두 배 이상 에너지가 많은 이유와 똑같아.', '생활 속'))

add(id='P6', num='6', en_title='Pyruvate Dehydrogenase Cofactors and Mechanism', ko_title='피루브산 탈수소효소의 조효소와 기전',
    slides='강의 슬라이드 6–12', level=2,
    en='<p>Describe the role of each cofactor involved in the reaction catalyzed by the pyruvate dehydrogenase complex.</p>',
    ko='<p>피루브산 탈수소효소(PDH) 복합체가 촉매하는 반응에 관여하는 각 조효소의 역할을 설명하라.</p>',
    answer=chips('<b>TPP</b>(E1): 탈카복실화, 하이드록시에틸기 운반', '<b>리포산</b>(E2): 아세틸기·전자를 받아 옮기는 “흔들팔”', '<b>CoA</b>(E2): 아세틸기 최종 수용 → 아세틸-CoA', '<b>FAD</b>(E3): 환원된 리포산 재산화', '<b>NAD<sup>+</sup></b>(E3): 최종 전자 수용 → NADH'),
    explain=key('다섯 조효소가 <b>릴레이</b>처럼 차례로 넘긴다: 탄소는 TPP → 리포산 → CoA로, 전자는 리포산 → FAD → NAD<sup>+</sup>로.') +
    table(['효소', '조효소 (비타민)', '하는 일'], [
        ['E1 피루브산 탈수소효소', 'TPP (B<sub>1</sub> 티아민)', '피루브산의 COO<sup>−</sup>를 CO<sub>2</sub>로 떼고, 남은 C2(하이드록시에틸)를 붙잡음'],
        ['E2 다이하이드로리포일 아세틸전달효소', '리포산 (Lys에 결합)', 'C2를 산화해 아세틸기로 받아 옮김 (자기는 환원됨) — 긴 흔들팔'],
        ['E2', 'CoA (판토텐산 B<sub>5</sub>)', '아세틸기를 받아 <b>아세틸-CoA</b>로 내보냄'],
        ['E3 다이하이드로리포일 탈수소효소', 'FAD (B<sub>2</sub> 리보플래빈)', '환원된 리포산에서 전자 2개를 받아 리포산을 원래대로'],
        ['E3', 'NAD<sup>+</sup> (나이아신)', 'FADH<sub>2</sub>의 전자를 받아 <b>NADH</b>로 → 전자전달계로']], cls='left') +
    fig(flow(['피루브산', 'TPP-C2', '아세틸-리포산', '아세틸-CoA'], arrow_labels=['E1: −CO₂', 'E2: 산화', 'E2: CoA로'], colors=[C['navy'], C['orange'], C['orange'], C['green']]), '탄소의 길 (전자는 리포산 → FAD → NAD⁺)') +
    tip('비타민 B군 4가지(B<sub>1</sub>·B<sub>2</sub>·B<sub>3</sub>·B<sub>5</sub>)가 한 반응에 다 모여 있어 → 시험 단골! α-KG 탈수소효소(4단계)도 똑같은 5조효소를 쓴다.', '시험 포인트'))

add(id='P7', num='7', en_title='Thiamine Deficiency', ko_title='티아민 결핍',
    slides='강의 슬라이드 10', level=1,
    en='<p>Individuals with a thiamine-deficient diet have relatively high levels of pyruvate in their blood. Explain this in biochemical terms.</p>',
    ko='<p>티아민이 부족한 식사를 하는 사람은 혈중 피루브산 농도가 비교적 높다. 생화학적으로 설명하라.</p>',
    answer=chips('티아민(B<sub>1</sub>) → <b>TPP</b> 부족', '→ PDH의 E1(TPP 필요)이 제대로 작동 못 함 → 피루브산 → 아세틸-CoA 전환 ↓ → 피루브산이 <b>쌓여</b> 혈액으로'),
    explain=key('효소가 막히면 그 <b>기질</b>이 쌓인다. PDH의 기질 = 피루브산.') +
    fig(flow(['포도당', '피루브산 ↑↑', '아세틸-CoA'], arrow_labels=['해당과정 (정상)', '✕ PDH (TPP 부족)'], colors=[C['navy'], C['red'], C['gray']]), '') +
    steps('티아민은 몸에서 TPP(티아민 피로인산)로 바뀌어 PDH E1의 조효소가 된다.',
          'TPP가 없으면 피루브산의 탈카복실화가 안 됨 → 해당과정은 계속 피루브산을 만드는데 치워지지 않음.',
          '쌓인 피루브산(일부는 젖산으로)이 혈액으로 나온다. α-KG 탈수소효소도 TPP가 필요해 α-KG도 쌓인다(문제 18).') +
    tip('포도당을 주 연료로 쓰는 뇌·신경이 특히 타격 → 각기병, 베르니케-코르사코프 증후군(알코올 중독자에서 흔함, 14장 슬라이드 53).', '임상'))

add(id='P8', num='8', en_title='Isocitrate Dehydrogenase Reaction', ko_title='아이소시트르산 탈수소효소 반응',
    slides='강의 슬라이드 25', level=1,
    en='<p>What type of chemical reaction is involved in the conversion of isocitrate to α-ketoglutarate? Name and describe the role of any cofactors. What other reaction(s) of the citric acid cycle are of this same type?</p>',
    ko='<p>아이소시트르산 → α-케토글루타르산 전환에는 어떤 종류의 화학 반응이 관여하는가? 관여하는 조효소의 이름과 역할을 설명하라. 시트르산 회로의 다른 어떤 반응이 같은 종류인가?</p>',
    answer=chips('<b>산화적 탈카복실화</b> (산화 + CO<sub>2</sub> 제거)', '조효소: <b>NAD<sup>+</sup></b>(미토콘드리아형; 세포질형은 NADP<sup>+</sup>) — 하이드라이드를 받음 / Mn<sup>2+</sup>(Mg<sup>2+</sup>) — 중간체 안정화', '같은 유형: <b>α-KG 탈수소효소</b> (그리고 회로 밖 PDH)'),
    explain=key('두 단계: ① –OH를 C=O로 <b>산화</b>(NAD<sup>+</sup>가 전자를 가져감) → 옥살로숙신산 ② β-케토산이라 CO<sub>2</sub>가 쉽게 <b>빠짐</b>.') +
    fig(flow(['아이소시트르산', '옥살로숙신산|(효소에 붙은 중간체)', 'α-케토글루타르산'], arrow_labels=['NAD⁺ → NADH', '−CO₂ (Mn²⁺)'], colors=[C['navy'], C['orange'], C['green']], box_h=46), '') +
    steps('NAD<sup>+</sup>: 아이소시트르산 C2의 H<sup>−</sup>(하이드라이드)를 받아 NADH가 된다 → 전자전달계로.',
          'Mn<sup>2+</sup>/Mg<sup>2+</sup>: 옥살로숙신산의 카보닐 O와 결합해, CO<sub>2</sub>가 빠질 때 생기는 음전하(에놀레이트)를 안정화.',
          'α-KG 탈수소효소: α-KG → 숙시닐-CoA + CO<sub>2</sub> + NADH. 역시 산화 + 탈카복실화 (단, PDH 방식의 5조효소 복합체).') +
    tip('회로에서 CO<sub>2</sub>가 나오는 곳은 딱 두 군데(3·4단계), 둘 다 산화적 탈카복실화야.', '포인트'))

add(id='P9', num='9', en_title='Stimulation of Oxygen Consumption by Oxaloacetate and Malate', ko_title='옥살로아세트산과 말산에 의한 산소 소비 촉진',
    slides='강의 슬라이드 14, 30', level=2,
    en='<p>In the early 1930s, Albert Szent-Györgyi reported the interesting observation that the addition of small amounts of oxaloacetate or malate to suspensions of minced pigeon breast muscle stimulated the oxygen consumption of the preparation. Surprisingly, the amount of oxygen consumed was about seven times more than the amount necessary for complete oxidation (to CO<sub>2</sub> and H<sub>2</sub>O) of the added oxaloacetate or malate. Why did the addition of oxaloacetate or malate stimulate oxygen consumption? Why was the amount of oxygen consumed so much greater than the amount necessary to completely oxidize the added oxaloacetate or malate?</p>',
    ko='<p>1930년대 초 센트죄르지는 잘게 다진 비둘기 가슴 근육 현탁액에 옥살로아세트산이나 말산을 소량 넣으면 산소 소비가 촉진된다는 흥미로운 관찰을 보고했다. 놀랍게도 소비된 산소는 넣어 준 옥살로아세트산·말산을 CO<sub>2</sub>와 H<sub>2</sub>O로 완전 산화하는 데 필요한 양의 약 7배였다. 왜 옥살로아세트산·말산이 산소 소비를 촉진했는가? 왜 소비된 산소가 그렇게 많았는가?</p>',
    answer=chips('OAA·말산은 회로의 <b>“촉매”</b> — 한 바퀴 돌 때마다 다시 만들어짐', '근육에 있던 연료(피루브산 → 아세틸-CoA)를 여러 바퀴 산화시켜 NADH → O<sub>2</sub> 소비', '→ 넣은 양보다 훨씬 많은 산소 소비'),
    explain=key('회로의 중간체는 <b>소모되지 않고 재생</b>된다. 적은 양이 많은 아세틸-CoA를 태우게 “돕는” 촉매 역할.') +
    fig(tca_wheel(hl=('옥살로아세트산', '말산'), height=330), 'OAA 1개가 한 바퀴 돌면 아세틸-CoA 1개를 태우고 다시 OAA로 돌아온다') +
    steps('다진 근육에는 아세틸-CoA를 만들 연료(글리코겐 → 피루브산)는 있는데, 회로 중간체(OAA)가 부족해 회로가 느리게 돌고 있었다.',
          '말산 → OAA가 공급되면 아세틸-CoA가 들어갈 “자리”가 생겨 회로가 빨리 돈다 → NADH·FADH<sub>2</sub> ↑ → 전자전달계 → O<sub>2</sub> 소비 ↑.',
          'OAA는 한 바퀴마다 재생되어 여러 번 쓰이므로, 태운 것은 “근육의 원래 연료”이고 산소 소비는 넣은 양의 몇 배가 된다.') +
    tip('회전문(OAA)을 하나 더 설치하면 건물(회로)에 드나드는 사람(아세틸-CoA)이 훨씬 늘어나지. 회전문 자체는 닳지 않아.', '비유') +
    warn('이 관찰이 크렙스가 “회로(cycle)” 개념을 떠올리는 결정적 단서가 됐어.', '역사'))

add(id='P10', num='10', en_title='Formation of Oxaloacetate in a Mitochondrion', ko_title='미토콘드리아에서 옥살로아세트산 생성',
    slides='강의 슬라이드 30', level=2,
    en=f'''<p>In the last reaction of the citric acid cycle, malate is dehydrogenated to regenerate the oxaloacetate necessary for the entry of acetyl-CoA into the cycle:</p>
<p class="c"><span class="sc">L</span>-Malate + NAD<sup>+</sup> → oxaloacetate + NADH + H<sup>+</sup> &nbsp;&nbsp; ΔG′° = 30.0 kJ/mol</p>
<p><b>a.</b> Calculate the equilibrium constant for this reaction at 25 °C.<br><b>b.</b> Because ΔG′° assumes a standard pH of 7, the equilibrium constant calculated in (a) corresponds to</p>
{eq(f"K′<sub>eq</sub> = {F('[oxaloacetate][NADH]', '[<span class=sc>L</span>-malate][NAD<sup>+</sup>]')}")}
<p>The measured concentration of <span class="sc">L</span>-malate in rat liver mitochondria is about 0.20 m<span class="sc">M</span> when [NAD<sup>+</sup>]/[NADH] is 10. Calculate the concentration of oxaloacetate at pH 7 in these mitochondria.<br><b>c.</b> To appreciate the magnitude of the mitochondrial oxaloacetate concentration, calculate the number of oxaloacetate molecules in a single rat liver mitochondrion. Assume the mitochondrion is a sphere of diameter 2.0 μm.</p>''',
    ko='<p>시트르산 회로의 마지막 반응에서 말산이 탈수소화되어, 아세틸-CoA가 회로에 들어오는 데 필요한 옥살로아세트산을 재생한다(L-말산 + NAD<sup>+</sup> → OAA + NADH + H<sup>+</sup>, ΔG′° = +30.0 kJ/mol).<br><b>a.</b> 25 °C에서 평형상수를 계산하라.<br><b>b.</b> ΔG′°는 pH 7 기준이므로 (a)의 평형상수는 위 식에 해당한다. 쥐 간 미토콘드리아에서 L-말산 농도는 약 0.20 mM이고 [NAD<sup>+</sup>]/[NADH] = 10이다. 이 미토콘드리아에서 pH 7일 때 옥살로아세트산 농도를 계산하라.<br><b>c.</b> 이 농도가 얼마나 작은지 실감하기 위해, 쥐 간 미토콘드리아 하나에 들어 있는 옥살로아세트산 분자 수를 계산하라. 미토콘드리아는 지름 2.0 μm의 구라고 가정한다.</p>',
    answer=chips('a. K′<sub>eq</sub> ≈ <b>5.5 × 10<sup>−6</sup></b>', 'b. [OAA] ≈ <b>1.1 × 10<sup>−8</sup> M</b> (0.011 μM)', 'c. 미토콘드리아 하나에 약 <b>28개</b>'),
    explain=steps('<b>a.</b> K = e<sup>−30.0/2.478</sup> = e<sup>−12.1</sup> = <span class="hl">5.5 × 10<sup>−6</sup></span> → 평형은 말산 쪽으로 크게 치우침.',
                  '<b>b.</b> 식을 [OAA]에 대해 정리:' + eq(f"[OAA] = K × [말산] × {F('[NAD<sup>+</sup>]', '[NADH]')} = (5.5×10<sup>−6</sup>)(2.0×10<sup>−4</sup> M)(10) = <span class='hl'>1.1×10<sup>−8</sup> M</span>"),
                  '<b>c.</b> 반지름 r = 1.0 μm = 1.0×10<sup>−5</sup> dm → 부피 V = (4/3)πr<sup>3</sup> = 4.2×10<sup>−15</sup> L<br>분자 수 = (1.1×10<sup>−8</sup> mol/L)(4.2×10<sup>−15</sup> L)(6.02×10<sup>23</sup>/mol) ≈ <span class="hl">28개</span>') +
    tip('미토콘드리아 하나에 OAA가 고작 수십 개! 그래서 OAA는 생기는 즉시 시트르산 생성효소(ΔG′° = −32.2)가 가져가고, 이 강한 “당김” 덕분에 +30짜리 불리한 8단계가 굴러간다.', '포인트') +
    warn('단위 주의: 부피는 L(= dm<sup>3</sup>)로! 1 μm = 10<sup>−5</sup> dm.', '함정 주의'))

add(id='P11', num='11', en_title='Cofactors for the Citric Acid Cycle', ko_title='시트르산 회로의 조효소',
    slides='강의 슬라이드 9–12, 15', level=1,
    en='<p>Suppose you have prepared a mitochondrial extract that contains all the soluble enzymes of the matrix but has lost (by dialysis) all the low molecular weight cofactors. What must you add to the extract so that the preparation will oxidize acetyl-CoA to CO<sub>2</sub>?</p>',
    ko='<p>미토콘드리아 기질의 모든 수용성 효소는 들어 있지만, 투석으로 저분자 조효소를 모두 잃은 미토콘드리아 추출물을 만들었다고 하자. 이 표본이 아세틸-CoA를 CO<sub>2</sub>로 산화하게 하려면 무엇을 넣어야 하는가?</p>',
    answer=chips('<b>NAD<sup>+</sup>, FAD, CoA, TPP, 리포산</b>', '<b>GDP(또는 ADP), P<sub>i</sub>, Mg<sup>2+</sup>(Mn<sup>2+</sup>)</b>', '회로를 시작할 <b>옥살로아세트산</b>(소량)'),
    explain=key('회로 8단계를 하나씩 보며 “효소 말고 필요한 작은 분자”를 모으면 된다.') +
    table(['필요한 것', '쓰이는 곳'], [['NAD<sup>+</sup>', '3·4·8단계 (전자 수용)'], ['FAD', '6단계 숙신산 탈수소효소, α-KG DH의 E3'],
                                ['CoA', '1단계에서 방출·4단계에서 재사용'], ['TPP, 리포산', '4단계 α-KG 탈수소효소 복합체'],
                                ['GDP(ADP) + P<sub>i</sub>', '5단계 숙시닐-CoA 합성효소'], ['Mg<sup>2+</sup>/Mn<sup>2+</sup>', '3단계 아이소시트르산 DH 등'],
                                ['옥살로아세트산', '아세틸-CoA가 들어갈 첫 짝꿍 (촉매량)']], cls='left') +
    steps('FAD·리포산·TPP는 원래 효소에 단단히 붙어 있어 투석에도 일부 남을 수 있지만, 안전하게 모두 넣는다.',
          '추출물에는 전자전달계(막)가 없으므로 NADH를 NAD<sup>+</sup>로 되돌릴 수 없다 → NAD<sup>+</sup>는 <b>충분히 많이</b>(소모량만큼) 넣어야 한다.') +
    tip('효소 = 공장 기계, 조효소 = 기계에 넣는 소모품·공구. 기계만 있으면 아무것도 못 만든다.', '비유'))

add(id='P12', num='12', en_title='Riboflavin Deficiency', ko_title='리보플래빈 결핍',
    slides='강의 슬라이드 7, 28', level=1,
    en='<p>How would a riboflavin deficiency affect the functioning of the citric acid cycle? Explain your answer.</p>',
    ko='<p>리보플래빈 결핍은 시트르산 회로의 작동에 어떤 영향을 주는가? 설명하라.</p>',
    answer=chips('리보플래빈(B<sub>2</sub>) → <b>FAD</b>(FMN) 부족', '→ <b>숙신산 탈수소효소</b>(6단계)와 <b>α-KG DH·PDH의 E3</b>가 약해짐 → 회로 전체가 느려짐'),
    explain=key('리보플래빈은 FAD의 재료. FAD를 쓰는 효소를 찾으면 끝.') +
    fig(tca_wheel(hl=('숙신산', 'α-케토글루타르산'), height=330), 'FAD가 필요한 곳: 숙신산 → 푸마르산, α-KG → 숙시닐-CoA(E3)') +
    steps('숙신산 → 푸마르산(숙신산 탈수소효소)은 FAD가 전자를 받는 반응 → FAD 부족 시 숙신산이 쌓인다.',
          'α-KG 탈수소효소와 PDH의 E3(다이하이드로리포일 탈수소효소)도 FAD가 필요 → 회로 입구(PDH)와 4단계도 느려진다.',
          '결과: 아세틸-CoA 산화 ↓ → NADH·FADH<sub>2</sub> ↓ → ATP 생산 ↓.') +
    tip('회로는 원형 도로라서 한 곳만 막혀도 전체 교통이 멈춘다.', '비유'))

add(id='P13', num='13', en_title='Oxaloacetate Pool', ko_title='옥살로아세트산 풀(pool)',
    slides='강의 슬라이드 31–32, 53', level=1,
    en='<p>What factors might decrease the pool of oxaloacetate available for the activity of the citric acid cycle? How can the pool of oxaloacetate be replenished?</p>',
    ko='<p>시트르산 회로가 쓸 수 있는 옥살로아세트산 풀을 줄이는 요인은 무엇인가? 옥살로아세트산 풀은 어떻게 다시 채워지는가?</p>',
    answer=chips('줄이는 요인: 중간체가 <b>생합성으로 빠져나감</b> — 당신생(OAA → PEP), 아스파르트산 합성, α-KG → 글루탐산, 숙시닐-CoA → 헴, 시트르산 → 지방산', '채우는 법: <b>보충(anaplerotic) 반응</b> — 피루브산 카복실화효소(가장 중요), PEP 카복시키나아제/카복실화효소, 말산 효소, 아미노산 분해'),
    explain=key('회로의 어느 중간체든 빠져나가면 결국 OAA가 줄어든다(원형이니까). 빠진 만큼 <b>밖에서 채워 넣는</b> 반응 = 보충 반응.') +
    eq('피루브산 + HCO<sub>3</sub><sup>−</sup> + ATP → 옥살로아세트산 + ADP + P<sub>i</sub> &nbsp; (피루브산 카복실화효소, 비오틴, 아세틸-CoA가 활성화)') +
    steps('<b>빠져나가는 길</b>: 공복 시 간의 당신생(OAA 대량 사용), 아미노산·헴·지방산 합성.',
          '<b>채우는 길</b>: 피루브산 카복실화효소 — 아세틸-CoA가 쌓이면(= OAA 부족 신호) 자동으로 켜진다. 그 밖에 아스파르트산 아미노기전달 → OAA, 글루탐산 → α-KG 등.') +
    tip('양동이(회로)에 구멍(생합성)이 있으면, 수도꼭지(보충 반응)로 물을 채워 줘야 수위가 유지된다.', '비유'))

add(id='P14', num='14', en_title='Energy Yield from the Citric Acid Cycle', ko_title='시트르산 회로의 에너지 수확',
    slides='강의 슬라이드 17, 27', level=1,
    en='<p>The reaction catalyzed by succinyl-CoA synthetase produces the high-energy compound GTP. How is the free energy contained in GTP incorporated into the cellular ATP pool?</p>',
    ko='<p>숙시닐-CoA 합성효소가 촉매하는 반응은 고에너지 화합물 GTP를 만든다. GTP에 담긴 자유에너지는 어떻게 세포의 ATP 풀로 들어가는가?</p>',
    answer=chips('<b>뉴클레오사이드 이인산 키나아제</b>: GTP + ADP ⇌ GDP + ATP (ΔG′° ≈ 0)'),
    explain=key('GTP와 ATP는 인산 꼬리가 똑같다(13장 문제 7). 인산 하나를 “옮기기”만 하면 된다.') +
    fig(flow(['GTP + ADP', 'GDP + ATP'], arrow_labels=['뉴클레오사이드 이인산 키나아제'], width=380, colors=[C['green'], C['orange']]), '') +
    steps('숙시닐-CoA의 싸이오에스터 에너지 → GTP (기질 수준 인산화).',
          'ΔG′° ≈ 0이라 양방향 반응이지만, 세포가 ATP를 계속 쓰니 ATP 쪽으로 흐른다.',
          '(동물 조직에 따라 ATP를 직접 만드는 숙시닐-CoA 합성효소 동종효소도 있다.)') +
    tip('GTP와 ATP는 “다른 은행의 같은 금액 지폐”. 수수료 없는 환전(ΔG ≈ 0)으로 바꿔 쓴다.', '비유'))

add(id='P15', num='15', en_title='Respiration Studies in Isolated Mitochondria', ko_title='분리한 미토콘드리아의 호흡 연구',
    slides='강의 슬라이드 28', level=2,
    en='<p>Cellular respiration can be studied in isolated mitochondria by measuring oxygen consumption under different conditions. If 0.01 <span class="sc">M</span> sodium malonate is added to actively respiring mitochondria that are using pyruvate as fuel, respiration soon stops and a metabolic intermediate accumulates.<br><b>a.</b> What is the structure of this intermediate?<br><b>b.</b> Explain why it accumulates.<br><b>c.</b> Explain why oxygen consumption stops.<br><b>d.</b> Aside from removal of the malonate, what can overcome this inhibition of respiration? Explain.</p>',
    ko='<p>분리한 미토콘드리아에서 조건을 바꿔 가며 산소 소비를 재면 세포 호흡을 연구할 수 있다. 피루브산을 연료로 활발히 호흡하는 미토콘드리아에 0.01 M 말론산 나트륨을 넣으면 곧 호흡이 멈추고 한 대사 중간체가 쌓인다.<br><b>a.</b> 이 중간체의 구조는?<br><b>b.</b> 왜 쌓이는가?<br><b>c.</b> 왜 산소 소비가 멈추는가?<br><b>d.</b> 말론산을 제거하는 것 외에, 호흡 억제를 극복할 방법은? 설명하라.</p>',
    answer=chips('a. <b>숙신산</b> (<sup>−</sup>OOC–CH<sub>2</sub>–CH<sub>2</sub>–COO<sup>−</sup>)', 'b. 말론산이 <b>숙신산 탈수소효소를 경쟁적으로 억제</b>', 'c. 회로가 멈춰 NADH·FADH<sub>2</sub> 공급 중단 → 전자전달계에 전자가 없음 → O<sub>2</sub> 불필요', 'd. <b>숙신산 농도를 크게 높이면</b> (경쟁적 억제는 기질로 이김)'),
    explain=key('말론산(<sup>−</sup>OOC–CH<sub>2</sub>–COO<sup>−</sup>)은 숙신산과 <b>꼭 닮은</b> 가짜 기질 → 효소 자리를 차지하지만 반응은 못 함.') +
    table(['', '구조', '역할'], [['숙신산 (진짜)', '<sup>−</sup>OOC–CH<sub>2</sub>–CH<sub>2</sub>–COO<sup>−</sup>', '기질 → 푸마르산'],
                               ['말론산 (가짜)', '<sup>−</sup>OOC–CH<sub>2</sub>–COO<sup>−</sup>', '활성 자리만 차지 (CH<sub>2</sub>–CH<sub>2</sub>가 없어 산화 불가)']]) +
    fig(tca_wheel(hl=('숙신산',), block=5, height=330), '6단계(숙신산 → 푸마르산)가 막혀 숙신산이 쌓인다') +
    steps('<b>c.</b> 6단계가 막히면 푸마르산·말산·OAA가 만들어지지 않음 → 아세틸-CoA가 회로에 못 들어감 → NADH·FADH<sub>2</sub> 생산 중단 → O<sub>2</sub>를 쓸 전자가 없어 호흡 정지.',
          '<b>d.</b> 경쟁적 억제는 기질 농도를 높이면 억제제를 밀어낼 수 있다 → 숙신산을 많이 넣어 준다. (또는 푸마르산·말산·OAA를 넣으면 막힌 뒤쪽부터 회로를 우회해 일부 산화를 다시 돌릴 수 있다.)') +
    tip('의자(활성 자리) 뺏기 게임: 진짜 손님(숙신산)이 훨씬 많아지면 가짜 손님(말론산)이 앉을 확률이 줄어든다.', '비유'))

add(id='P18', num='18', en_title='Role of the Vitamin Thiamine', ko_title='비타민 티아민의 역할',
    slides='강의 슬라이드 10, 26', level=1,
    en='<p>People with beriberi, a disease caused by thiamine deficiency, have elevated levels of blood pyruvate and α-ketoglutarate, especially after consuming a meal rich in glucose. How are these effects related to a deficiency of thiamine?</p>',
    ko='<p>티아민 결핍으로 생기는 각기병 환자는 특히 포도당이 많은 식사 후 혈중 피루브산과 α-케토글루타르산 농도가 높다. 이 현상은 티아민 결핍과 어떻게 관련되는가?</p>',
    answer=chips('TPP가 필요한 두 효소: <b>PDH</b>(피루브산 → 아세틸-CoA) · <b>α-KG 탈수소효소</b>(α-KG → 숙시닐-CoA)', '두 효소가 느려짐 → 각 기질인 <b>피루브산·α-KG가 쌓임</b>', '포도당 식사 → 피루브산이 더 많이 생겨 증상 악화'),
    explain=key('문제 7의 확장판: TPP를 쓰는 효소는 <b>두 개</b>이고, 두 기질이 모두 쌓인다.') +
    fig(tca_wheel(hl=('α-케토글루타르산',), block=3, height=330), '4단계(α-KG DH)도 TPP가 필요 → α-KG 축적') +
    steps('티아민 → TPP. PDH의 E1과 α-KG DH의 E1은 둘 다 TPP로 탈카복실화를 한다.',
          '포도당을 많이 먹으면 해당과정이 피루브산을 더 많이 만들어 → PDH 병목에서 피루브산이 더 쌓인다.',
          '회로가 α-KG에서도 막혀 에너지 생산이 줄고, 포도당 의존도가 큰 신경·심장이 먼저 망가진다(각기병: 말초신경염, 심부전).') +
    tip('(참고: 오탄당 인산 경로의 트랜스케톨레이스도 TPP를 쓴다 — 14장.)', '연결'))

add(id='P19', num='19', en_title='Synthesis of Oxaloacetate by the Citric Acid Cycle', ko_title='시트르산 회로로 옥살로아세트산을 합성할 수 있을까?',
    slides='강의 슬라이드 18, 31–32', level=2,
    en='<p>In the last step of the citric acid cycle, NAD<sup>+</sup>-dependent oxidation of <span class="sc">L</span>-malate forms oxaloacetate. Can a net synthesis of oxaloacetate from acetyl-CoA occur using only the enzymes and cofactors of the citric acid cycle, without depleting the intermediates of the cycle? Explain. How do cells replenish the oxaloacetate that is lost from the cycle to biosynthetic reactions?</p>',
    ko='<p>시트르산 회로의 마지막 단계에서 NAD<sup>+</sup> 의존적 L-말산 산화로 옥살로아세트산이 생긴다. 회로의 효소와 조효소만으로, 회로 중간체를 고갈시키지 않고 아세틸-CoA로부터 옥살로아세트산을 <b>알짜로</b> 합성할 수 있는가? 설명하라. 세포는 생합성으로 빠져나간 옥살로아세트산을 어떻게 보충하는가?</p>',
    answer=chips('<b>불가능</b> — 아세틸-CoA의 C2가 들어오면 CO<sub>2</sub> 2개가 나감 → 알짜 탄소 증가 0', '보충: <b>피루브산 카복실화효소</b> 등 보충(anaplerotic) 반응'),
    explain=key('탄소 장부: 들어오는 탄소 2개(아세틸) = 나가는 탄소 2개(CO<sub>2</sub> ×2). OAA는 “제자리”로 돌아올 뿐 늘지 않는다.') +
    fig(bars([('들어오는 탄소 (아세틸기)', 2, C['green'], '+2 C'), ('나가는 탄소 (3·4단계 CO₂)', 2, C['red'], '−2 C'), ('OAA 알짜 변화', 0.05, C['gray'], '0')], height=120), '') +
    steps('OAA(C4) + 아세틸(C2) → 시트르산(C6) → … 3단계 −CO<sub>2</sub>(C5) → 4단계 −CO<sub>2</sub>(C4) → … → OAA(C4). 한 바퀴 후 OAA 1개 = 처음과 같음.',
          '따라서 회로만으로는 OAA를 늘릴 수 없고, 생합성으로 뺀 만큼 외부에서 채워야 한다.',
          '보충 반응: 피루브산 + HCO<sub>3</sub><sup>−</sup> + ATP → OAA (피루브산 카복실화효소, 아세틸-CoA가 활성화), PEP 카복시키나아제, 말산 효소, 아미노산 분해 등.') +
    tip('그래서 동물은 지방산(→ 아세틸-CoA)으로 포도당을 알짜로 만들 수 없다(14장 문제 25). 식물은 글리옥실산 회로로 CO<sub>2</sub> 방출 단계를 건너뛰어 가능!', '연결'))

add(id='P20', num='20', en_title='Oxaloacetate Depletion', ko_title='옥살로아세트산 고갈',
    slides='강의 슬라이드 31–32', level=1,
    en='<p>Mammalian liver can carry out gluconeogenesis using oxaloacetate as the starting material (Chapter 14). Would the extensive use of oxaloacetate for gluconeogenesis affect the operation of the citric acid cycle? Explain your answer.</p>',
    ko='<p>포유류 간은 옥살로아세트산을 출발 물질로 당신생을 할 수 있다(14장). 옥살로아세트산을 당신생에 대량으로 쓰면 시트르산 회로 작동에 영향이 있을까? 설명하라.</p>',
    answer=chips('<b>영향이 있다</b> — OAA가 부족하면 아세틸-CoA가 회로에 들어갈 짝이 없어 회로가 <b>느려진다</b>', '보충 반응(피루브산 카복실화효소)으로 채우지 못하면 아세틸-CoA는 <b>케톤체</b>로 빠진다'),
    explain=key('OAA는 회로의 “입장권”. 당신생이 입장권을 가져가 버리면 아세틸-CoA가 입장하지 못한다.') +
    fig(flow(['OAA', '당신생 → 포도당', '아세틸-CoA', '케톤체'], arrow_labels=['대량 사용', '', 'OAA 없으면'], colors=[C['orange'], C['green'], C['navy'], C['red']]), '공복·당뇨 시 간의 상황') +
    steps('시트르산 생성효소는 OAA + 아세틸-CoA가 모두 있어야 작동. OAA 농도가 떨어지면 회로 속도 ↓.',
          '피루브산 카복실화효소가 아세틸-CoA로 활성화되어 OAA를 보충하려 하지만, 공복·당뇨처럼 당신생이 아주 활발하면 따라잡지 못한다.',
          '남는 아세틸-CoA는 간에서 케톤체(아세토아세트산·β-하이드록시뷰티르산)로 바뀌어 다른 조직의 연료가 된다.') +
    tip('15장 문제 9(인슐린 부족 → 케톤체 ↑)와 같은 이야기야.', '연결'))

add(id='P22', num='22', en_title='Synthesis of L-Malate in Wine Making', ko_title='와인 제조에서 L-말산의 합성',
    slides='강의 슬라이드 32, 53 · 14장 발효', level=2,
    en='<p>The tartness of some wines is due to high concentrations of <span class="sc">L</span>-malate. Write a sequence of reactions showing how yeast cells synthesize <span class="sc">L</span>-malate from glucose under anaerobic conditions in the presence of dissolved CO<sub>2</sub> (HCO<sub>3</sub><sup>−</sup>). Note that the overall reaction for this fermentation cannot involve the consumption of nicotinamide coenzymes or citric acid cycle intermediates.</p>',
    ko='<p>일부 와인의 신맛은 높은 L-말산 농도 때문이다. 용존 CO<sub>2</sub>(HCO<sub>3</sub><sup>−</sup>)가 있는 무산소 조건에서 효모가 포도당으로부터 L-말산을 합성하는 반응 순서를 써라. 이 발효의 전체 반응은 니코틴아마이드 조효소나 시트르산 회로 중간체를 알짜로 소비해서는 안 된다.</p>',
    answer=chips('포도당 → 2 피루브산 (해당과정: 2NADH, 2ATP)', '2 피루브산 + 2HCO<sub>3</sub><sup>−</sup> + 2ATP → 2 OAA (피루브산 카복실화효소)', '2 OAA + 2NADH → 2 L-말산 (말산 탈수소효소)', '알짜: <b>포도당 + 2HCO<sub>3</sub><sup>−</sup> → 2 L-말산</b>'),
    explain=key('조건 두 개: ① NADH가 알짜로 남거나 모자라면 안 됨 ② 회로 중간체를 빼 쓰면 안 됨. → 해당과정이 만든 NADH 2개를 OAA → 말산 환원에 <b>딱 맞게</b> 쓴다.') +
    align([('①', '포도당 + 2NAD<sup>+</sup> + 2ADP + 2P<sub>i</sub> → 2 피루브산 + 2NADH + 2ATP', ''),
           ('②', '2 피루브산 + 2HCO<sub>3</sub><sup>−</sup> + 2ATP → 2 OAA + 2ADP + 2P<sub>i</sub>', ''),
           ('③', '2 OAA + 2NADH + 2H<sup>+</sup> → 2 L-말산 + 2NAD<sup>+</sup>', ''),
           ('합', '포도당 + 2HCO<sub>3</sub><sup>−</sup> → 2 L-말산 (+ 2H<sup>+</sup> 정도)', '')], cls='sum') +
    steps('NAD<sup>+</sup>/NADH: ①에서 2개 환원, ③에서 2개 산화 → 균형 ✔ (그래서 무산소에서도 계속 가능 = 발효).',
          'ATP: ①에서 +2, ②에서 −2 → 알짜 0. 효모는 에너지를 얻진 못하지만 NAD<sup>+</sup> 균형은 맞는다.',
          'OAA는 새로 만들어졌다가 곧바로 말산으로 → 회로 중간체를 가져다 쓰지 않음 ✔.') +
    tip('젖산 발효가 “피루브산 → 젖산”으로 NAD<sup>+</sup>를 되돌리듯, 여기서는 “OAA → 말산”이 그 역할을 한다.', '연결'))

add(id='P23', num='23', en_title='Net Synthesis of α-Ketoglutarate', ko_title='α-케토글루타르산의 알짜 합성',
    slides='강의 슬라이드 31–32', level=2,
    en='<p>α-Ketoglutarate plays a central role in the biosynthesis of several amino acids. Write a sequence of enzymatic reactions that could result in the net synthesis of α-ketoglutarate from pyruvate. Your proposed sequence must not involve the net consumption of other citric acid cycle intermediates. Write an equation for the overall reaction.</p>',
    ko='<p>α-케토글루타르산은 여러 아미노산 생합성의 중심이다. 피루브산으로부터 α-케토글루타르산을 알짜로 합성하는 효소 반응 순서를 써라. 다른 시트르산 회로 중간체를 알짜로 소비해서는 안 된다. 전체 반응식을 써라.</p>',
    answer=chips('피루브산 ① → <b>OAA</b> (피루브산 카복실화효소) / 피루브산 ② → <b>아세틸-CoA</b> (PDH)', 'OAA + 아세틸-CoA → 시트르산 → 아이소시트르산 → <b>α-KG</b>', '알짜: <b>2 피루브산 + ATP + 2NAD<sup>+</sup> + H<sub>2</sub>O → α-KG + CO<sub>2</sub> + ADP + P<sub>i</sub> + 2NADH (+ H<sup>+</sup>)</b>'),
    explain=key('피루브산 2개를 <b>둘로 나눠</b> 쓴다: 하나는 OAA(보충 반응으로 새로 만듦), 하나는 아세틸-CoA. 둘이 합쳐 회로 앞쪽 세 단계를 따라가면 α-KG.') +
    fig(flow(['피루브산 ×2', 'OAA + 아세틸-CoA', '시트르산', 'α-KG'], arrow_labels=['PC(+HCO₃⁻, ATP) / PDH(−CO₂)', '시트르산 생성효소', '아코니테이스·IDH(−CO₂)'], box_h=44), '') +
    align([('', '피루브산 + HCO<sub>3</sub><sup>−</sup> + ATP → OAA + ADP + P<sub>i</sub>', ''),
           ('', '피루브산 + CoA + NAD<sup>+</sup> → 아세틸-CoA + CO<sub>2</sub> + NADH', ''),
           ('', 'OAA + 아세틸-CoA + H<sub>2</sub>O → 시트르산 + CoA', ''),
           ('', '시트르산 → 아이소시트르산', ''),
           ('', '아이소시트르산 + NAD<sup>+</sup> → α-KG + CO<sub>2</sub> + NADH', ''),
           ('합', '2 피루브산 + ATP + 2NAD<sup>+</sup> + H<sub>2</sub>O → α-KG + CO<sub>2</sub> + ADP + P<sub>i</sub> + 2NADH', '')], cls='sum') +
    tip('HCO<sub>3</sub><sup>−</sup> 1개가 들어가고 CO<sub>2</sub> 2개가 나가서 알짜 CO<sub>2</sub>는 1개. 탄소 수 확인: 3 + 3 + 1 − 2 = 5 = α-KG(C5) ✔', '검산'))

add(id='P24', num='24', en_title='Amphibolic Pathways', ko_title='양방향성(amphibolic) 경로',
    slides='강의 슬라이드 31–32', level=1,
    en='<p>Explain, giving examples, what is meant by the statement that the citric acid cycle is amphibolic.</p>',
    ko='<p>시트르산 회로가 양방향성(amphibolic)이라는 말의 뜻을 예를 들어 설명하라.</p>',
    answer=chips('<b>이화(분해)</b>와 <b>동화(합성)</b> 모두에 쓰인다', '이화: 아세틸-CoA → CO<sub>2</sub> + NADH·FADH<sub>2</sub> (에너지)', '동화: 중간체 → 아미노산·포도당·헴·지방산의 <b>원료</b>'),
    explain=key('amphi = “양쪽”. 회로는 연료를 태우는 <b>용광로</b>이자 부품을 내주는 <b>부품 창고</b>.') +
    table(['중간체', '만들어지는 것 (동화)'], [['시트르산', '→ 세포질로 나가 아세틸-CoA → <b>지방산·콜레스테롤</b>'],
                                         ['α-케토글루타르산', '→ <b>글루탐산</b> → 글루타민·프롤린·아르지닌'],
                                         ['숙시닐-CoA', '→ <b>헴</b>(포르피린)'],
                                         ['옥살로아세트산', '→ <b>아스파르트산</b>(→ 아스파라진, 뉴클레오타이드) / → PEP → <b>포도당</b>(당신생)']], cls='left') +
    steps('이화 방향: 탄수화물·지방·아미노산 → 아세틸-CoA → 회로 → CO<sub>2</sub> + 환원된 조효소 → ATP.',
          '동화 방향: 위 표처럼 중간체를 빼서 생합성. 빠진 만큼 보충 반응(피루브산 카복실화효소 등)으로 채운다(문제 13, 19).') +
    tip('14장 해당과정도 DHAP → 글리세롤 3-인산처럼 부품을 내준다. 중심 대사 경로는 거의 다 양방향성이야.', '연결'))

add(id='P25', num='25', en_title='Regulation of the Pyruvate Dehydrogenase Complex', ko_title='피루브산 탈수소효소 복합체의 조절',
    slides='강의 슬라이드 37, 39–40', level=1,
    en='<p>In animal tissues, the ratio of active, unphosphorylated to inactive, phosphorylated PDH complex regulates the rate of conversion of pyruvate to acetyl-CoA. Determine what happens to the rate of this reaction when a preparation of rabbit muscle mitochondria containing the PDH complex is treated with (a) pyruvate dehydrogenase kinase, ATP, and NADH; (b) pyruvate dehydrogenase phosphatase and Ca<sup>2+</sup>; (c) malonate.</p>',
    ko='<p>동물 조직에서는 활성(탈인산화) PDH와 불활성(인산화) PDH의 비율이 피루브산 → 아세틸-CoA 전환 속도를 조절한다. PDH 복합체가 든 토끼 근육 미토콘드리아 표본을 다음으로 처리하면 반응 속도는 어떻게 되는가? (a) PDH 키나아제, ATP, NADH (b) PDH 인산가수분해효소와 Ca<sup>2+</sup> (c) 말론산</p>',
    answer=chips('(a) <b>감소</b> — 인산화 → 불활성 (NADH도 키나아제 활성화·PDH 억제)', '(b) <b>증가</b> — 탈인산화 → 활성 (Ca<sup>2+</sup>가 인산가수분해효소 활성화)', '(c) <b>감소</b> — 숙신산 탈수소효소 억제 → 회로 정체 → 아세틸-CoA·NADH 쌓여 PDH 억제'),
    explain=key('PDH는 글리코겐 인산화효소와 <b>반대</b>: <b>인산이 붙으면 꺼진다</b>.') +
    fig(flow(['PDH (활성)', 'PDH–P (불활성)'], arrow_labels=['키나아제 + ATP → / ← 인산가수분해효소'], width=420, colors=[C['green'], C['gray']]), '') +
    steps('<b>(a)</b> PDH 키나아제가 E1을 인산화 → 불활성. ATP·NADH·아세틸-CoA는 “에너지 충분” 신호로 키나아제를 더 활성화한다 → 속도 ↓.',
          '<b>(b)</b> 근육 수축 시 늘어나는 Ca<sup>2+</sup>가 PDH 인산가수분해효소를 활성화 → 인산 제거 → 활성 PDH ↑ → 속도 ↑ (운동 = 에너지 필요).',
          '<b>(c)</b> 말론산은 PDH를 직접 건드리지 않지만, 회로 6단계를 막아(문제 15) 아세틸-CoA와 NADH가 쌓인다 → 생성물 억제 + 키나아제 활성화 → 속도 ↓.') +
    tip('Ca<sup>2+</sup> = “근육이 일하는 중”이라는 신호. 에너지가 필요할 때 연료 입구를 여는 거야.', '포인트'))

add(id='P27', num='27', en_title='Regulation of Citrate Synthase', ko_title='시트르산 생성효소의 조절',
    slides='강의 슬라이드 38–41', level=2,
    en=f'''<p>In the presence of saturating amounts of oxaloacetate, the activity of citrate synthase from pig heart tissue shows a sigmoid dependence on the concentration of acetyl-CoA, as shown in the graph. Adding succinyl-CoA shifts the curve to the right and makes the sigmoid dependence more pronounced.</p>{img('c16_p27.png', '32%')}
<p>On the basis of these observations, suggest how succinyl-CoA regulates the activity of citrate synthase. (Hint: See Fig. 6-37.) Why is succinyl-CoA an appropriate signal for regulation of the citric acid cycle? How does the regulation of citrate synthase control the rate of cellular respiration in pig heart tissue?</p>''',
    ko='<p>옥살로아세트산이 충분할 때, 돼지 심장의 시트르산 생성효소 활성은 그래프처럼 아세틸-CoA 농도에 대해 S자(시그모이드) 곡선을 보인다. 숙시닐-CoA를 넣으면 곡선이 오른쪽으로 이동하고 S자 모양이 더 뚜렷해진다. 이 관찰로부터 숙시닐-CoA가 시트르산 생성효소를 어떻게 조절하는지 제안하라(힌트: 그림 6-37). 숙시닐-CoA는 왜 시트르산 회로 조절에 적절한 신호인가? 시트르산 생성효소의 조절은 돼지 심장의 세포 호흡 속도를 어떻게 조절하는가?</p>',
    answer=chips('숙시닐-CoA = <b>알로스테릭 억제제</b> (아세틸-CoA에 대한 친화도 ↓, K<sub>0.5</sub> ↑)', '적절한 이유: 회로 <b>뒤쪽 산물</b> → 쌓이면 “회로가 밀려 있다/에너지 충분” 신호 (되먹임 억제)', '시트르산 생성효소 = 아세틸-CoA의 <b>입구</b> → 입구 속도가 NADH 생산 → 호흡(O<sub>2</sub> 소비) 속도를 결정'),
    explain=key('S자 곡선 = 알로스테릭 효소. 곡선이 <b>오른쪽으로 밀림</b> = 같은 활성을 내려면 기질이 더 필요 = 억제.') +
    steps('숙시닐-CoA는 아세틸-CoA와 비슷한 아실-CoA 구조라 효소의 조절 자리(또는 아세틸-CoA 자리 근처)에 결합해, 효소를 T(덜 활성) 상태로 기울게 한다 → 협동성(S자) ↑, 기질 친화도 ↓.',
          '숙시닐-CoA는 4단계(α-KG DH)의 산물. 뒤에서 쌓이면 회로가 NADH·GTP를 충분히 만들고 있다는 뜻 → 앞문(1단계)을 좁혀 과잉 생산을 막는 <b>되먹임</b>.',
          '1단계가 느려지면 → 시트르산·NADH 생산 ↓ → 전자전달계로 가는 전자 ↓ → O<sub>2</sub> 소비(호흡) ↓. 반대로 에너지가 필요하면 억제가 풀려 호흡 ↑.') +
    tip('고속도로 진입로 신호등(시트르산 생성효소)이 도로 끝의 정체(숙시닐-CoA)를 보고 빨간불을 켜는 것과 같아.', '비유'))

add(id='P28', num='28', en_title='Regulation of Pyruvate Carboxylase', ko_title='피루브산 카복실화효소의 조절',
    slides='강의 슬라이드 32, 53', level=2,
    en='<p>The carboxylation of pyruvate by pyruvate carboxylase occurs at a very low rate unless acetyl-CoA, a positive allosteric modulator, is present. If you have just eaten a meal rich in fatty acids (triacylglycerols) but low in carbohydrates (glucose), how does this regulatory property shut down the oxidation of glucose to CO<sub>2</sub> and H<sub>2</sub>O but increase the oxidation of acetyl-CoA derived from fatty acids?</p>',
    ko='<p>피루브산 카복실화효소에 의한 피루브산 카복실화는 양성 알로스테릭 조절자인 아세틸-CoA가 없으면 매우 느리다. 지방산(트라이아실글리세롤)은 많고 탄수화물(포도당)은 적은 식사를 막 했다면, 이 조절 성질이 어떻게 포도당의 CO<sub>2</sub>·H<sub>2</sub>O로의 산화는 멈추고 지방산 유래 아세틸-CoA의 산화는 늘리는가?</p>',
    answer=chips('지방산 β-산화 → <b>아세틸-CoA ↑</b>', '① 아세틸-CoA가 <b>PDH 억제</b>(+ PDH 키나아제 활성) → 피루브산(포도당 유래)이 아세틸-CoA로 안 감 → 포도당 산화 ↓', '② 아세틸-CoA가 <b>피루브산 카복실화효소 활성</b> → 피루브산 → OAA ↑ → 지방산 유래 아세틸-CoA를 받아 줄 OAA 공급 → 지방 산화 ↑'),
    explain=key('아세틸-CoA가 많다 = “지방 연료가 충분”. 피루브산의 운명을 <b>태우기(PDH)</b>에서 <b>OAA 만들기(PC)</b>로 전환한다.') +
    fig(flow(['피루브산', 'OAA', '+ 지방산 유래|아세틸-CoA → 회로'], arrow_labels=['PC ↑ (아세틸-CoA가 켬)', ''], colors=[C['navy'], C['green'], C['orange']], box_h=46), '피루브산 → 아세틸-CoA (PDH)는 꺼지고, 피루브산 → OAA (PC)는 켜진다') +
    steps('지방이 많으면 β-산화로 아세틸-CoA가 대량 생산.',
          'PDH: 생성물(아세틸-CoA·NADH)이 억제 → 포도당 → 피루브산 → CO<sub>2</sub> 경로가 막힌다(포도당 절약).',
          'PC: 아세틸-CoA가 활성화 → OAA ↑ → 시트르산 생성효소가 지방산 유래 아세틸-CoA를 회로로 받아들임 → 지방 산화 ↑. (남는 OAA는 간에서 당신생으로도 간다.)') +
    tip('같은 신호(아세틸-CoA)가 한 효소는 끄고 다른 효소는 켜서 연료 선택을 바꿔. 15장의 상반 조절과 같은 논리야.', '연결'))

add(id='P29', num='29', en_title='Relationship between Respiration and the Citric Acid Cycle', ko_title='호흡과 시트르산 회로의 관계',
    slides='강의 슬라이드 4, 15', level=1,
    en='<p>Although oxygen does not participate directly in the citric acid cycle, the cycle operates only when O<sub>2</sub> is present. Why?</p>',
    ko='<p>산소는 시트르산 회로에 직접 참여하지 않지만, 회로는 O<sub>2</sub>가 있을 때만 작동한다. 왜 그런가?</p>',
    answer=chips('회로는 <b>NAD<sup>+</sup>·FAD</b>가 계속 있어야 돈다', '이 산화형 조효소는 <b>전자전달계</b>에서 NADH·FADH<sub>2</sub>의 전자를 <b>O<sub>2</sub></b>에 넘겨야 재생된다', 'O<sub>2</sub> 없음 → NADH 쌓임, NAD<sup>+</sup> 고갈 → 탈수소효소 정지'),
    explain=key('회로의 탈수소효소 4개는 “빈 접시”(NAD<sup>+</sup>, FAD)가 필요. 접시를 씻는 곳 = 전자전달계, 마지막 세제 = O<sub>2</sub>.') +
    fig(flow(['시트르산 회로', 'NADH · FADH₂', '전자전달계', 'O₂ → H₂O'], arrow_labels=['NAD⁺·FAD 사용', '전자 전달', '최종 수용체'], colors=[C['navy'], C['orange'], C['navy'], C['blue']]), 'NAD⁺·FAD는 전자전달계를 거쳐야 재생된다') +
    steps('회로 한 바퀴에 NAD<sup>+</sup> 3개, FAD 1개가 환원된다.', '미토콘드리아 속 NAD<sup>+</sup> 양은 적어서 재생이 없으면 곧 바닥.',
          '산소가 없으면 전자전달계가 멈춤 → NADH/NAD<sup>+</sup> ↑ → 3·4·8단계 멈춤 → 회로 정지 (근육은 해당과정 + 젖산 발효로 버팀).') +
    tip('14장 문제 7(LDH)과 같은 원리: 산화형 조효소를 되살리는 곳이 없으면 대사가 멈춘다.', '연결'))

add(id='P30', num='30', en_title='Effect of [NADH]/[NAD⁺] on the Citric Acid Cycle', ko_title='[NADH]/[NAD⁺] 비가 시트르산 회로에 미치는 영향',
    slides='강의 슬라이드 39, 43', level=1,
    en='<p>How would you expect the operation of the citric acid cycle to respond to a rapid increase in the [NADH]/[NAD<sup>+</sup>] ratio in the mitochondrial matrix? Why?</p>',
    ko='<p>미토콘드리아 기질에서 [NADH]/[NAD<sup>+</sup>] 비가 빠르게 증가하면 시트르산 회로의 작동은 어떻게 반응할 것으로 예상되는가? 왜 그런가?</p>',
    answer=chips('회로가 <b>느려진다</b>', '① NAD<sup>+</sup>(기질) 부족 → 3·4·8단계 탈수소효소 속도 ↓', '② NADH가 시트르산 생성효소·IDH·α-KG DH·PDH를 <b>억제</b>', '③ 말산 → OAA 평형이 말산 쪽 → OAA ↓ → 1단계 ↓'),
    explain=key('NADH가 많다 = “전자(에너지)가 넘친다” → 더 만들 필요 없음 → 회로 브레이크.') +
    fig(tca_wheel(hl=('아이소시트르산', 'α-케토글루타르산', '말산'), height=330), 'NAD⁺를 쓰는 세 단계(3·4·8)가 모두 느려진다') +
    steps('질량 작용: 탈수소효소 반응의 생성물(NADH)이 많고 반응물(NAD<sup>+</sup>)이 적어 정반응이 불리해진다.',
          '알로스테릭 억제: NADH는 시트르산 생성효소, 아이소시트르산·α-KG 탈수소효소, PDH를 직접 억제.',
          '특히 8단계(ΔG′° = +29.7)는 NADH/NAD<sup>+</sup>에 매우 민감 → OAA 농도가 더 떨어져 1단계도 느려진다(문제 10).') +
    tip('반대로 운동으로 ATP를 쓰면 전자전달계가 빨라져 NADH → NAD<sup>+</sup>가 늘고, 회로도 다시 빨라진다.', '연결'))

add(id='P31', num='31', en_title='Thermodynamics of Citrate Synthase Reaction in Cells', ko_title='세포 속 시트르산 생성효소 반응의 열역학',
    slides='강의 슬라이드 20 · 13장 ΔG', level=2,
    en='''<p>Citrate is formed by the condensation of acetyl-CoA with oxaloacetate, catalyzed by citrate synthase:</p>
<p class="c">Oxaloacetate + acetyl-CoA + H<sub>2</sub>O ⇌ citrate + CoA + H<sup>+</sup></p>
<p>In rat heart mitochondria at pH 7.0 and 25 °C, the concentrations of reactants and products are oxaloacetate, 1 μ<span class="sc">M</span>; acetyl-CoA, 1 μ<span class="sc">M</span>; citrate, 220 μ<span class="sc">M</span>; and CoA, 65 μ<span class="sc">M</span>. The standard free-energy change for the citrate synthase reaction is −32.2 kJ/mol. What is the direction of metabolite flow through the citrate synthase reaction in rat heart cells? Explain.</p>''',
    ko='<p>시트르산은 시트르산 생성효소가 촉매하는 아세틸-CoA와 옥살로아세트산의 축합으로 생긴다(위 반응식). pH 7.0, 25 °C의 쥐 심장 미토콘드리아에서 농도는 옥살로아세트산 1 μM, 아세틸-CoA 1 μM, 시트르산 220 μM, CoA 65 μM이다. 이 반응의 표준 자유에너지 변화는 −32.2 kJ/mol이다. 쥐 심장 세포에서 시트르산 생성효소 반응을 통한 대사물의 흐름 방향은? 설명하라.</p>',
    answer=chips(f'Q ≈ 1.4 × 10<sup>4</sup>', f'{DG} ≈ <b>−8.5 kJ/mol</b> (&lt; 0)', '→ <b>시트르산 생성 방향(정반응)</b>으로 흐른다'),
    explain=key('13장 공식: ΔG = ΔG′° + RT ln Q. 물과 H<sup>+</sup>(pH 7 = 표준)는 Q에 넣지 않는다.') +
    steps(eq(f"Q = {F('[시트르산][CoA]', '[OAA][아세틸-CoA]')} = {F('(220×10<sup>−6</sup>)(65×10<sup>−6</sup>)', '(1×10<sup>−6</sup>)(1×10<sup>−6</sup>)')} = 1.43 × 10<sup>4</sup>"),
          'RT ln Q = 2.478 × ln(1.43×10<sup>4</sup>) = 2.478 × 9.57 = +23.7 kJ/mol',
          align([(DG, '−32.2 + 23.7'), ('', '<span class="hl">−8.5 kJ/mol</span> → 음수 → 정반응')])) +
    fig(bars([('표준 ΔG′°', 32.2, C['blue'], '−32.2'), ('농도 보정 RT ln Q', 23.7, C['red'], '+23.7'), ('실제 ΔG', 8.5, C['green'], '−8.5 → 여전히 내리막')], height=120), '') +
    tip('생성물(시트르산)이 기질보다 수백 배 많아 표준값보다 덜 유리하지만, 여전히 음수라 한 방향으로 흐른다 → 조절 지점이 될 수 있는 반응.', '포인트'))

add(id='P32', num='32', en_title='Reactions of the Pyruvate Dehydrogenase Complex', ko_title='피루브산 탈수소효소 복합체의 반응',
    slides='강의 슬라이드 6–8, 12', level=2,
    en='<p>Two of the steps in the oxidative decarboxylation of pyruvate (steps ④ and ⑤ in Fig. 16-6) do not involve any of the three carbons of pyruvate, yet are essential to the operation of the PDH complex. Explain.</p>',
    ko='<p>피루브산의 산화적 탈카복실화 단계 중 두 단계(그림 16-6의 ④와 ⑤)는 피루브산의 탄소 세 개 중 어느 것과도 관련이 없는데도 PDH 복합체 작동에 필수적이다. 설명하라.</p>',
    answer=chips('④·⑤ = E3가 <b>환원된 리포아마이드를 다시 산화</b>하는 단계 (④ 리포산 → FAD, ⑤ FADH<sub>2</sub> → NAD<sup>+</sup>)', '이게 없으면 리포산이 환원된 채 남아 <b>다음 피루브산을 받을 수 없음</b> → 한 번 돌고 멈춤'),
    explain=key('효소도 “원래 상태로 돌아와야” 다음 손님을 받는다. ④·⑤는 <b>리셋 단계</b>.') +
    table(['단계', '일어나는 일', '탄소?'], [['① E1', '피루브산 → CO<sub>2</sub> + TPP-하이드록시에틸', '○'],
                                         ['② E1→E2', '하이드록시에틸 산화 → 아세틸-리포아마이드 (리포산 환원)', '○'],
                                         ['③ E2', '아세틸기 → CoA → 아세틸-CoA', '○'],
                                         ['④ E3', '환원된 리포아마이드(–SH HS–) → 산화형(S–S), FAD → FADH<sub>2</sub>', '✕'],
                                         ['⑤ E3', 'FADH<sub>2</sub> + NAD<sup>+</sup> → FAD + NADH + H<sup>+</sup>', '✕']], cls='left') +
    steps('③이 끝나면 E2의 리포산 팔은 환원형(다이하이드로리포아마이드)으로 남는다.',
          '④ E3의 FAD가 전자를 가져가 리포산을 산화형으로 되돌리고, ⑤ NAD<sup>+</sup>가 FADH<sub>2</sub>의 전자를 받아 FAD도 되돌린다.',
          '이 두 단계가 없으면 모든 조효소가 환원형으로 “갇혀” 한 번 반응한 뒤 복합체가 멈춘다. 또 ⑤는 반응의 산화 에너지를 NADH로 거둬들이는 단계.') +
    tip('식당에서 요리(①–③)만 하고 설거지(④·⑤)를 안 하면, 접시가 다 떨어져 두 번째 손님부터는 못 받는다.', '비유'))

add(id='P33', num='33', en_title='Pyruvate Transport into Mitochondria', ko_title='피루브산의 미토콘드리아 수송',
    slides='강의 슬라이드 36', level=2,
    en='<p>The mitochondrial pyruvate carrier (MPC) is a heterodimer of the proteins MPC1 and MPC2. In a high proportion (80%) of certain cancers, including gliomas (tumors of the glial cells of the brain), the gene for one of these proteins is mutated such that pyruvate cannot enter the mitochondrial matrix. Name three metabolic effects that you would expect to see if cytosolic pyruvate could not gain access to the machinery of the citric acid cycle. (Hint: Box 14-1 may be helpful.)</p>',
    ko='<p>미토콘드리아 피루브산 운반체(MPC)는 MPC1과 MPC2 단백질의 이형이량체다. 신경교종(뇌 교세포 종양) 등 일부 암의 높은 비율(80%)에서 이 중 한 단백질의 유전자가 돌연변이되어 피루브산이 미토콘드리아 기질로 들어가지 못한다. 세포질의 피루브산이 시트르산 회로에 접근하지 못할 때 예상되는 대사 효과 세 가지를 말하라. (힌트: Box 14-1)</p>',
    answer=chips('① <b>젖산 생성·분비 ↑</b> (피루브산 → 젖산, 바르부르크 효과)', '② ATP를 채우려고 <b>포도당 흡수·해당과정 ↑</b>', '③ 포도당 유래 <b>아세틸-CoA·회로·산화적 인산화 ↓</b> → 회로는 글루타민·지방산으로 채움 (포도당 → 지방 합성도 ↓)'),
    explain=key('피루브산이 “미토콘드리아 문 앞에서 막힌다” → 세포질에서 처리할 수밖에 없다 = 젖산.') +
    fig(flow(['포도당', '피루브산 (세포질)', '젖산 ↑ (분비)'], arrow_labels=['해당과정 ↑', 'LDH'], colors=[C['navy'], C['orange'], C['red']]), 'MPC ✕ → 미토콘드리아(PDH·회로)로 가는 길이 막힘') +
    steps('<b>젖산 ↑</b>: NAD<sup>+</sup> 재생을 위해 피루브산을 LDH로 젖산으로 → 세포 밖으로 분비 (산소가 있어도 발효 = 바르부르크 효과).',
          '<b>해당과정 ↑</b>: 포도당당 ATP가 2개뿐이라 ATP를 맞추려면 포도당을 훨씬 많이 써야 함 (PET 검사에서 암이 밝게 보이는 이유).',
          '<b>포도당 산화 ↓</b>: 포도당 탄소가 아세틸-CoA로 못 가 회로·산화적 인산화 기여 ↓. 회로 중간체는 글루타민(→ α-KG)·지방산으로 보충. 포도당 → 시트르산 → 지방산 합성도 줄어든다.') +
    tip('암세포는 오히려 이 상태에서 해당과정 중간체를 핵산·아미노산 합성 재료로 빼 쓰며 빨리 자란다는 해석도 있어.', '연결'))

add(id='P34', num='34', en_title='Citric Acid Cycle Mutants', ko_title='시트르산 회로 효소 돌연변이',
    slides='강의 슬라이드 4, 31', level=1,
    en='<p>There are many cases of human disease in which one or another enzyme activity is lacking due to genetic mutation. Why are cases in which individuals lack one of the enzymes of the citric acid cycle extremely rare?</p>',
    ko='<p>유전적 돌연변이로 어떤 효소 활성이 없는 인간 질병은 많다. 그런데 시트르산 회로 효소 중 하나가 없는 사례는 왜 극히 드문가?</p>',
    answer=chips('회로는 거의 모든 세포의 <b>에너지 생산 중심</b>이자 생합성 원료 공급원', '→ 효소 하나가 완전히 없으면 <b>배아 단계에서 살아남지 못함</b>(치명적) → 태어난 환자로 관찰되기 어려움'),
    explain=key('너무 중요한 효소의 결함은 “병”이 되기 전에 “생존 불가”가 된다.') +
    steps('회로는 탄수화물·지방·아미노산 산화의 공통 종착역 → 세포 ATP의 대부분(NADH·FADH<sub>2</sub> 공급)이 여기에 의존.',
          '또 α-KG·OAA·숙시닐-CoA 등 생합성 전구체를 공급(문제 24) → 효소 하나만 빠져도 에너지와 합성이 동시에 무너진다.',
          '그래서 완전 결손은 발생 초기에 치명적이고, 관찰되는 사례는 활성이 일부 남은 경우(예: 푸마레이스 결핍증, 숙신산 탈수소효소 변이 종양)에 한정된다.') +
    tip('자동차 엔진 핵심 부품이 없으면 “고장 난 차”가 아니라 아예 “출고가 안 되는 차”인 것과 같아.', '비유'))

for _n in ('1', '3', '5', '16', '17', '21', '26'):
    ALL_ITEMS.append(dict(id='P' + _n, num=_n, level=3, kind='PROBLEM'))
ALL_ITEMS.sort(key=lambda i: int(i['num']))
