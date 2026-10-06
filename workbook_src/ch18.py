# -*- coding: utf-8 -*-
"""Chapter 18 — Amino Acid Oxidation and the Production of Urea"""
from helpers import *

CHAPTER = '18'
CH_TITLE = '아미노산 산화와 요소 생성'
CH_EN = 'Amino Acid Oxidation and the Production of Urea'
STAT = ('5', '요소 회로 효소 (지도 수록)')
SCOPE = ('교수님 18장 강의(슬라이드 1–72) 범위 = <b>18.1 아미노기의 대사적 운명</b>(소화, 아미노기 전이·PLP, 글루타민·알라닌 수송, 산화적 탈아미노화), '
         '<b>18.2 질소 배설과 요소 회로</b>(5단계, 조절, 유전 결함, ALT·AST), <b>18.3 아미노산 분해 경로</b>(7개 진입점, 보조인자, 유전 질환) — 18장 전체. 18장에는 본문 예제가 없어.')
INCLUDE = ['<b>아미노기 전이·PLP·ALT/AST</b> — 문제 1, 2, 5, 9',
           '<b>암모니아 수송·독성·탈아미노화</b> — 문제 3, 4',
           '<b>요소 회로·에너지 비용</b> — 문제 6, 7, 8',
           '<b>필수·케톤생성 아미노산</b> — 문제 10, 11',
           '<b>유전 질환·B<sub>12</sub></b> — 문제 12, 13, 14, 15, 21']
EXCLUDE = ['<b>문제 22</b> — DATA ANALYSIS PROBLEM']

ALL_ITEMS = []


def add(**kw):
    kw.setdefault('section', '연습문제')
    kw.setdefault('kind', 'PROBLEM')
    ALL_ITEMS.append(kw)


# ------------------------------------------------------------------ drawings
def urea_cycle():
    W, H = 560, 300
    b = arrowdef('uc', C['gray']) + arrowdef('uc2', C['orange'])
    b += f'<rect x="8" y="8" width="210" height="284" rx="14" fill="#eff6ff" stroke="#93c5fd"/>' + T(113, 284, '미토콘드리아 기질', 11, C['blue'], weight=900)
    b += f'<rect x="232" y="8" width="320" height="284" rx="14" fill="#f0fdf4" stroke="#86efac"/>' + T(392, 284, '세포질', 11, C['green'], weight=900)

    def node(x, y, s, col=C['navy'], w=112):
        return f'<rect x="{x-w/2}" y="{y-14}" width="{w}" height="28" rx="14" fill="white" stroke="{col}" stroke-width="2"/>' + T(x, y + 4, s, 11, col, weight=700)

    def ar(x1, y1, x2, y2, col=C['gray'], m='uc'):
        return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{col}" stroke-width="2" marker-end="url(#{m})"/>'
    b += T(113, 30, 'NH₄⁺ + HCO₃⁻ + 2ATP', 10.5, C['orange'], weight=700) + ar(113, 36, 113, 58, C['orange'], 'uc2') + T(160, 52, '① CPS I', 10, C['red'], weight=900)
    b += node(113, 74, '카르바모일 인산')
    b += node(60, 170, '오르니틴', w=90) + node(165, 170, '시트룰린', C['purple'], w=90)
    b += ar(130, 90, 158, 152) + T(170, 124, '② OTC', 10, C['red'], weight=900)
    b += ar(106, 170, 117, 170)
    b += ar(212, 170, 262, 170) + node(305, 170, '시트룰린', C['purple'], w=86)
    b += node(392, 70, '아르기니노숙신산', C['blue'], w=130)
    b += ar(320, 154, 360, 88) + T(244, 100, '③ ASS', 10, C['red'], 'start', 900) + T(244, 114, '+ 아스파르트산', 9.5, C['orange'], 'start', 700) + T(244, 128, 'ATP → AMP + PPᵢ', 9.5, C['gray'], 'start')
    b += node(495, 170, '아르기닌', C['navy'], w=86)
    b += ar(430, 86, 482, 152) + T(500, 106, '④ ASL', 10, C['red'], weight=900) + T(500, 120, '→ 푸마르산', 9.5, C['green'], weight=700)
    b += node(392, 248, '오르니틴', w=86)
    b += ar(480, 186, 420, 234) + T(500, 222, '⑤ 아르기네이스', 10, C['red'], weight=900) + T(500, 238, '+ H₂O → 요소', 10, C['orange'], weight=900)
    b += f'<path d="M348 248 L 200 248 Q 70 248 60 188" fill="none" stroke="{C["gray"]}" stroke-width="2" marker-end="url(#uc)"/>'
    b += T(280, 240, '오르니틴 → 미토콘드리아로', 9.5, C['gray'])
    return svg(W, H, b)


def n_flow():
    return vflow(['아미노산 + α-KG → α-케토산 + 글루탐산 (아미노전이효소, PLP)', '글루탐산 + NAD(P)⁺ → α-KG + NH₄⁺ (GDH, 간 미토콘드리아)',
                  'NH₄⁺ + HCO₃⁻ → 카르바모일 인산 → 요소 회로', '요소 → 혈액 → 신장 → 소변'],
                 colors=[C['blue'], C['orange'], C['red'], C['green']], box_h=26, gap=16, width=540, font=10.5, bw=500)


def gaa_cycle():
    W, H = 560, 200
    b = arrowdef('ga', C['gray'])
    b += f'<rect x="8" y="8" width="230" height="184" rx="14" fill="#fef2f2" stroke="#fca5a5"/>' + T(123, 28, '근육', 12, C['red'], weight=900)
    b += f'<rect x="322" y="8" width="230" height="184" rx="14" fill="#fff7ed" stroke="#fdba74"/>' + T(437, 28, '간', 12, C['orange'], weight=900)
    b += T(123, 60, '포도당 → (해당) → 피루브산', 10.5, C['ink'], weight=700) + T(123, 90, '+ NH₂ (글루탐산에서, ALT)', 10, C['blue'])
    b += T(123, 124, '→ 알라닌', 12, C['navy'], weight=900)
    b += T(437, 60, '알라닌 → 피루브산 (ALT)', 10.5, C['ink'], weight=700) + T(437, 90, 'NH₂ → 글루탐산 → 요소', 10, C['red'])
    b += T(437, 124, '피루브산 → (당신생) → 포도당', 10.5, C['green'], weight=900)
    b += f'<line x1="200" y1="140" x2="360" y2="140" stroke="{C["navy"]}" stroke-width="2.2" marker-end="url(#ga)"/>' + T(280, 132, '혈중 알라닌', 10, C['navy'], weight=700)
    b += f'<line x1="360" y1="172" x2="200" y2="172" stroke="{C["green"]}" stroke-width="2.2" marker-end="url(#ga)"/>' + T(280, 166, '혈당(포도당)', 10, C['green'], weight=700)
    return svg(W, H, b)


def pku_path():
    return flow(['페닐알라닌', '티로신', '멜라닌 · 도파민…'], arrow_labels=['✕ 페닐알라닌 수산화효소 (PKU)', '티로시네이스'],
                colors=[C['red'], C['gray'], C['gray']], box_h=38, width=540, font=11)


# ------------------------------------------------------------------ front pages
def front_pages():
    p1 = f'''<h2 class="pt"><span class="n">MAP</span> 질소가 요소가 되기까지 &amp; 요소 회로 5단계</h2>
<p class="lead">아미노산 = <b>질소(아미노기)</b> + <b>탄소 골격</b>. 질소는 글루탐산으로 모여 NH<sub>4</sub><sup>+</sup>가 되고, 간의 <b>요소 회로</b>에서 요소로 바뀌어 버려진다.</p>
<div class="grid2">
 <div class="card"><h4>🧭 질소의 길</h4><figure class="fig">{n_flow()}</figure>
  {table(['운반체', '어디서 → 어디로', '핵심 효소'], [['<b>글루타민</b>', '대부분의 조직 → 간·신장', '글루타민 합성효소 / 글루타미네이스'], ['<b>알라닌</b>', '근육 → 간 (포도당-알라닌 회로)', 'ALT']], cls='left')}</div>
 <div class="card"><h4>🔄 요소 회로 (간)</h4><figure class="fig">{urea_cycle()}</figure>
  <p class="small">요소의 질소 2개: 하나는 <b>NH<sub>4</sub><sup>+</sup></b>(카르바모일 인산), 하나는 <b>아스파르트산</b>. 탄소는 HCO<sub>3</sub><sup>−</sup>. 비용: ATP 3개 = 고에너지 결합 4개.</p></div>
</div>'''
    p2 = f'''<h2 class="pt"><span class="n">KIT</span> 탄소 골격 · 보조인자 · 유전 질환</h2>
<div class="grid2">
 <div>
  <div class="card"><h4><span class="no">1</span> 탄소 골격의 7개 진입점</h4>
   {table(['진입점', '아미노산', '성질'], [
    ['피루브산', 'A C W G S T (알라닌, 시스테인, 트립토판, 글리신, 세린, 트레오닌)', '포도당'],
    ['α-케토글루타르산', 'P R H E Q (프롤린, 아르기닌, 히스티딘, 글루탐산, 글루타민)', '포도당'],
    ['숙시닐-CoA', 'I M T V (아이소류신, 메티오닌, 트레오닌, 발린)', '포도당'],
    ['푸마르산', 'F Y (페닐알라닌, 티로신)', '포도당'],
    ['옥살로아세트산', 'N D (아스파라긴, 아스파르트산)', '포도당'],
    ['아세틸-CoA · 아세토아세틸-CoA', 'L K F W Y I T', '케톤']], cls='left')}
   {key('<b>오직 케톤생성</b> = <b>류신(L)·라이신(K)</b>. F·Y·W·I·T는 둘 다.')}</div>
 </div>
 <div>
  <div class="card"><h4><span class="no">2</span> 보조인자</h4>
   {table(['보조인자', '비타민', '하는 일'], [['PLP', 'B<sub>6</sub>', '아미노기 전이 (+ 탈카복실화, 라세미화)'], ['비오틴', 'B<sub>7</sub>', 'CO<sub>2</sub> 운반'], ['THF', '엽산 (B<sub>9</sub>)', '1탄소기 (메틸·메틸렌·포르밀)'], ['adoMet', '(메티오닌)', '메틸기 (가장 강력)'], ['THBP', '—', '페닐알라닌 수산화'], ['조효소 B<sub>12</sub>', 'B<sub>12</sub>', '메틸말로닐-CoA → 숙시닐-CoA, 메티오닌 합성']], cls='left')}</div>
  <div class="card" style="margin-top:3mm"><h4><span class="no">3</span> 유전 질환 한 줄씩</h4>
   {table(['질환', '결핍 효소', '쌓이는 것'], [['PKU', '페닐알라닌 수산화효소', 'Phe, 페닐피루브산'], ['알캅톤뇨증', '호모젠티스산 이산소화효소', '호모젠티스산 (검은 소변)'], ['백색증', '티로시네이스', '멜라닌 없음'], ['단풍당뇨증', '가지사슬 α-케토산 탈수소효소', 'Val·Ile·Leu의 α-케토산'], ['메틸말론산혈증', '메틸말로닐-CoA 뮤테이스 / B<sub>12</sub>', '메틸말론산']], cls='left')}</div>
 </div>
</div>'''
    return [p1, p2]


# ------------------------------------------------------------------ items
add(id='P1', num='1', en_title='Products of Amino Acid Transamination', ko_title='아미노기 전이반응의 산물',
    slides='강의 슬라이드 14–15, 22', level=1,
    en='<p>Name and draw the structure of the α-keto acid resulting when each of the four amino acids listed undergoes transamination with α-ketoglutarate: (a) aspartate, (b) glutamate, (c) alanine, (d) phenylalanine.</p>',
    ko='<p>다음 네 아미노산이 α-케토글루타르산과 아미노기 전이반응을 할 때 생기는 α-케토산의 이름과 구조를 써라: (a) 아스파르트산, (b) 글루탐산, (c) 알라닌, (d) 페닐알라닌.</p>',
    answer=chips('(a) <b>옥살로아세트산</b>', '(b) <b>α-케토글루타르산</b>', '(c) <b>피루브산</b>', '(d) <b>페닐피루브산</b>'),
    explain=key('아미노기 전이 = α 탄소의 <b>–NH<sub>3</sub><sup>+</sup></b>를 떼고 그 자리에 <b>=O</b>를 붙인다. 나머지 골격(R)은 그대로.') +
    eq('아미노산 + α-케토글루타르산 ⇌ α-케토산 + 글루탐산 &nbsp;(아미노전이효소, PLP)') +
    table(['아미노산', 'α 탄소 부분', 'α-케토산', '구조 (R–CO–COO⁻)'], [
        ['(a) 아스파르트산', '⁻OOC–CH<sub>2</sub>–<b>CH(NH<sub>3</sub><sup>+</sup>)</b>–COO⁻', '<b>옥살로아세트산</b>', '⁻OOC–CH<sub>2</sub>–<b>C(=O)</b>–COO⁻'],
        ['(b) 글루탐산', '⁻OOC–CH<sub>2</sub>CH<sub>2</sub>–<b>CH(NH<sub>3</sub><sup>+</sup>)</b>–COO⁻', '<b>α-케토글루타르산</b>', '⁻OOC–CH<sub>2</sub>CH<sub>2</sub>–<b>C(=O)</b>–COO⁻'],
        ['(c) 알라닌', 'CH<sub>3</sub>–<b>CH(NH<sub>3</sub><sup>+</sup>)</b>–COO⁻', '<b>피루브산</b>', 'CH<sub>3</sub>–<b>C(=O)</b>–COO⁻'],
        ['(d) 페닐알라닌', 'C<sub>6</sub>H<sub>5</sub>–CH<sub>2</sub>–<b>CH(NH<sub>3</sub><sup>+</sup>)</b>–COO⁻', '<b>페닐피루브산</b>', 'C<sub>6</sub>H<sub>5</sub>–CH<sub>2</sub>–<b>C(=O)</b>–COO⁻']], cls='left') +
    steps('(b)는 글루탐산 + α-KG ⇌ α-KG + 글루탐산 — 받는 쪽과 주는 쪽이 같아서 알짜 변화가 없다.',
          '(a) AST(GOT), (c) ALT(GPT)가 촉매하는 대표 반응.',
          '(d) 페닐피루브산은 PKU 환자 소변에 쌓이는 “페닐케톤”(문제 12).') +
    tip('이름 짝꿍: 알라닌 ↔ 피루브산, 아스파르트산 ↔ 옥살로아세트산, 글루탐산 ↔ α-케토글루타르산. 18장 내내 나온다.', '외우기'))

add(id='P2', num='2', en_title='Measurement of Alanine Aminotransferase Activity', ko_title='알라닌 아미노전이효소(ALT) 활성 측정',
    slides='강의 슬라이드 22, 35–36', level=1,
    en='<p>The measurement of alanine aminotransferase activity (reaction rate) usually includes an excess of pure lactate dehydrogenase and NADH in the reaction system. The rate of alanine disappearance is equal to the rate of NADH disappearance measured spectrophotometrically. Explain how this assay works.</p>',
    ko='<p>알라닌 아미노전이효소(ALT)의 활성(반응 속도)을 잴 때는 보통 순수한 젖산 탈수소효소(LDH)와 NADH를 과량 넣는다. 알라닌이 사라지는 속도는 분광광도계로 잰 NADH가 사라지는 속도와 같다. 이 측정법의 원리를 설명하라.</p>',
    answer=chips('ALT가 만든 <b>피루브산</b>을 LDH가 바로 젖산으로 바꾸며 <b>NADH 1개</b>를 소모', '알라닌 1개 = 피루브산 1개 = NADH 1개 → <b>340 nm 흡광도 감소 속도 = ALT 속도</b>'),
    explain=key('<b>짝지은(coupled) 측정법</b>: 눈에 안 보이는 반응을, 눈에 보이는 반응(NADH 소모)에 이어 붙여 잰다.') +
    eq('① 알라닌 + α-KG → 피루브산 + 글루탐산 &nbsp;(ALT — 측정하고 싶은 반응)',
       '② 피루브산 + NADH + H⁺ → 젖산 + NAD⁺ &nbsp;(LDH, 과량)') +
    steps('NADH는 340 nm 빛을 흡수하고 NAD⁺는 흡수하지 않는다 → NADH가 줄면 흡광도가 줄어든다.',
          'LDH와 NADH를 <b>과량</b> 넣었으므로 ②는 즉시 일어난다 → 피루브산이 생기는 순간 바로 소모 → 전체 속도는 ①(ALT)이 결정.',
          '따라서 A<sub>340</sub>이 줄어드는 속도 = NADH 소모 속도 = 피루브산 생성 속도 = <b>ALT 활성</b>.') +
    tip('혈중 ALT(SGPT) 검사가 바로 이 방법. ALT가 높다 = 간세포가 깨져 효소가 새어 나왔다(슬라이드 35–36).', '임상') +
    warn('LDH가 부족하면 ②가 느려져 ALT가 아니라 LDH 속도를 재게 된다. 그래서 “과량”이 핵심.', '함정'))

add(id='P3', num='3', en_title='Alanine and Glutamine in the Blood', ko_title='혈액 속의 알라닌과 글루타민',
    slides='강의 슬라이드 17–19', level=1,
    en='<p>Normal human blood plasma contains all the amino acids required for the synthesis of body proteins, but not in equal concentrations. Alanine and glutamine are present in much higher concentrations than any other amino acids. Suggest why.</p>',
    ko='<p>정상인의 혈장에는 체단백질 합성에 필요한 모든 아미노산이 있지만 농도는 같지 않다. 알라닌과 글루타민이 다른 어떤 아미노산보다 훨씬 많다. 그 이유를 제시하라.</p>',
    answer=chips('둘 다 말초 조직의 <b>암모니아(질소)를 간으로 나르는 운반체</b>', '<b>글루타민</b>: 대부분의 조직 → 간·신장 (질소 2개, 무독성)', '<b>알라닌</b>: 근육 → 간 (포도당-알라닌 회로)'),
    explain=key('NH<sub>4</sub><sup>+</sup>는 독성이 있어 혈액에 그대로 실을 수 없다 → 무해한 아미노산에 “포장”해서 보낸다.') +
    fig(gaa_cycle(), '포도당-알라닌 회로') +
    steps('<b>글루타민</b>: 글루탐산 + NH<sub>4</sub><sup>+</sup> + ATP → 글루타민 (글루타민 합성효소). 간에서 글루타미네이스가 NH<sub>4</sub><sup>+</sup>를 다시 풀어 요소 회로로.',
          '<b>알라닌</b>: 근육은 해당과정으로 피루브산이 많다 → 아미노기를 붙여 알라닌으로 내보냄 → 간에서 피루브산은 포도당신생, 질소는 요소로.',
          '이 두 아미노산은 늘 운반 중이라 혈중 농도가 높다.') +
    tip('글루타민 = 전국 택배, 알라닌 = 근육 전용 택배. 짐(질소)은 모두 간이라는 물류센터로 간다.', '비유'))

add(id='P4', num='4', en_title='Glutamate Dehydrogenase Function', ko_title='글루탐산 탈수소효소의 기능',
    slides='강의 슬라이드 21', level=2,
    en='<p>Increases in ATP levels in blood trigger insulin release by the pancreas, which in turn stimulates the uptake of blood glucose. Knowing this, suggest why a mutation that prevents inhibition of glutamate dehydrogenase by GTP results in insulin release and hypoglycemia.</p>',
    ko='<p>[이자 β세포 안의] ATP가 늘면 이자가 인슐린을 분비하고, 인슐린은 혈당 흡수를 촉진한다. 이를 바탕으로, 글루탐산 탈수소효소(GDH)가 GTP에 의해 억제되지 않게 만드는 돌연변이가 왜 인슐린 분비와 저혈당을 일으키는지 설명하라.</p>',
    answer=chips('GDH가 브레이크(GTP) 없이 계속 작동 → 글루탐산 → <b>α-KG + NADH</b> 과다', '→ α-KG는 TCA, NADH는 전자전달 → <b>ATP ↑</b> → 인슐린 분비 → <b>저혈당</b>', '(덤) NH<sub>4</sub><sup>+</sup>도 과다 → <b>고암모니아혈증</b>'),
    explain=key('GDH 조절: <b>ADP·GDP ▲ / ATP·GTP ⊗</b>. 에너지가 넘치면 아미노산을 태우지 말라는 브레이크.') +
    fig(vflow(['GTP 억제가 사라진 GDH', '글루탐산 → α-KG + NH₄⁺ + NADH (계속)', 'α-KG → TCA, NADH → 전자전달 → ATP ↑', 'β세포 ATP ↑ → 인슐린 분비 ↑', '혈당이 낮아도 인슐린 → 저혈당'],
              colors=[C['red'], C['orange'], C['orange'], C['blue'], C['red']], box_h=24, gap=14, width=520, font=10.5, bw=420), '') +
    steps('정상: ATP·GTP가 많으면 GDH가 꺼져 에너지 과잉 생산을 막는다.',
          '돌연변이: 에너지가 충분해도 GDH가 계속 돌아 β세포가 “ATP가 많다 = 혈당이 높다”로 착각 → 인슐린 과다.',
          '인슐린이 혈당을 계속 끌어내려 저혈당. 단백질(류신 등 GDH 활성화)을 먹은 뒤 더 심해진다.') +
    tip('실제 질환: <b>고인슐린증-고암모니아혈증 증후군(HI/HA)</b>.', '임상'))

add(id='P5', num='5', en_title='Distribution of Amino Nitrogen', ko_title='아미노 질소의 분배',
    slides='강의 슬라이드 14–15, 22', level=1,
    en='<p>If your diet is rich in alanine but deficient in aspartate, will you show signs of aspartate deficiency? Explain.</p>',
    ko='<p>식단에 알라닌은 많은데 아스파르트산이 부족하다면 아스파르트산 결핍 증상이 나타날까? 설명하라.</p>',
    answer=chips('<b>아니다</b> (나타나지 않는다)', '아스파르트산은 <b>비필수</b> 아미노산: OAA + 아미노기 → 아스파르트산 (AST)', '알라닌의 아미노기가 <b>글루탐산</b>을 거쳐 OAA로 옮겨진다'),
    explain=key('아미노기 전이반응은 <b>가역</b> → 질소는 아미노전이효소들을 통해 서로 돌려 쓸 수 있다.') +
    eq('알라닌 + α-KG ⇌ 피루브산 + 글루탐산 &nbsp;(ALT)', '글루탐산 + 옥살로아세트산 ⇌ α-KG + <b>아스파르트산</b> &nbsp;(AST)',
       '알짜: 알라닌 + OAA ⇌ 피루브산 + 아스파르트산') +
    steps('탄소 골격(OAA)은 시트르산 회로에 늘 있다.', '아미노기는 알라닌 → 글루탐산 → 아스파르트산으로 넘어간다 (글루탐산이 중간 집합소).') +
    warn('필수 아미노산(HILKMFTWV)은 이렇게 만들 수 없다 — 탄소 골격 자체를 못 만들기 때문.', '비교'))

add(id='P6', num='6', en_title='Lactate versus Alanine as Metabolic Fuel: The Cost of Nitrogen Removal', ko_title='젖산 vs 알라닌 — 질소 제거의 비용',
    slides='강의 슬라이드 17, 27–30', level=2,
    en='<p>The three carbons in lactate and alanine have identical oxidation states, and animals can use either carbon source as a metabolic fuel. Compare the net ATP yield (moles of ATP per mole of substrate) for the complete oxidation (to CO<sub>2</sub> and H<sub>2</sub>O) of lactate versus alanine when the cost of nitrogen excretion as urea is included.</p>',
    ko='<p>젖산과 알라닌의 탄소 3개는 산화 상태가 같고, 동물은 둘 다 연료로 쓸 수 있다. 요소로 질소를 배설하는 비용까지 포함해, 젖산과 알라닌을 CO<sub>2</sub>와 H<sub>2</sub>O로 완전 산화할 때의 알짜 ATP 수율(기질 1 mol당 ATP mol)을 비교하라.</p>',
    answer=chips('젖산: <b>15 ATP</b>', '알라닌: 15 − 2 (요소 비용) ≈ <b>13 ATP</b>', '차이 = 질소 1개를 요소로 버리는 비용 (요소 1개 = ATP 4당량, N 2개)'),
    explain=key('탄소 부분은 둘 다 “피루브산 + NADH 1개”로 똑같다. 다른 건 알라닌의 <b>질소 처리비</b>뿐.') +
    table(['단계', '젖산', '알라닌'], [
        ['→ 피루브산', 'LDH: NADH 1 (2.5)', '아미노기 전이 → 글루탐산 → GDH: NADH 1 (2.5)'],
        ['피루브산 → 아세틸-CoA', 'NADH 1 (2.5)', 'NADH 1 (2.5)'],
        ['아세틸-CoA → CO<sub>2</sub> (TCA)', '10', '10'],
        ['소계', '15', '15'],
        ['요소 합성 비용', '—', 'ATP 4당량 ÷ N 2개 = <b>−2</b>'],
        ['<b>알짜</b>', '<b>15 ATP</b>', '<b>≈ 13 ATP</b>']], cls='left') +
    steps('요소 1개: CPS I에 ATP 2개 + 아르기니노숙신산 합성효소에 ATP 1개(→ AMP + PP<sub>i</sub>, 고에너지 결합 2개) = 고에너지 결합 4개.',
          '요소 1개가 질소 2개를 내보내므로 질소 1개당 2 ATP. 알라닌은 질소 1개 → −2.') +
    tip('푸마르산 → 말산 → OAA에서 NADH가 생겨 실제 비용은 조금 줄어든다(아스파르트산 션트, 슬라이드 30). 그래서 교과서는 “요소 합성의 에너지 비용이 줄어든다”고 말한다.', '심화'))

add(id='P7', num='7', en_title='Ammonia Toxicity Resulting from an Arginine-Deficient Diet', ko_title='아르기닌 결핍 식이에 의한 암모니아 독성',
    slides='강의 슬라이드 20, 27, 31', level=2,
    en='<p>In a study, cats were fasted overnight then given a single meal complete in all amino acids except arginine. Within 2 hours, blood ammonia levels increased from a normal level of 18 μg/L to 140 μg/L, and the cats showed the clinical symptoms of ammonia toxicity. A control group fed a complete amino acid diet or an amino acid diet in which arginine was replaced by ornithine showed no unusual clinical symptoms.</p><p>(a) What was the role of fasting in the experiment? (b) What caused the ammonia levels to rise in the experimental group? Why did the absence of arginine lead to ammonia toxicity? Is arginine an essential amino acid in cats? Why or why not? (c) Why can ornithine be substituted for arginine?</p>',
    ko='<p>고양이를 하룻밤 굶긴 뒤, 아르기닌만 빠지고 나머지 아미노산은 모두 든 식사를 한 번 주었다. 2시간 만에 혈중 암모니아가 정상 18 μg/L에서 140 μg/L로 올랐고 암모니아 독성 증상이 나타났다. 완전한 아미노산 식이나, 아르기닌 대신 오르니틴을 넣은 식이를 먹은 대조군은 이상이 없었다.</p><p>(a) 실험에서 굶긴 이유는? (b) 실험군의 암모니아가 오른 이유는? 아르기닌이 없으면 왜 암모니아 독성이 생기나? 고양이에게 아르기닌은 필수 아미노산인가? (c) 오르니틴이 아르기닌을 대신할 수 있는 이유는?</p>',
    answer=chips('(a) 굶겨서 몸속 아미노산(특히 아르기닌·오르니틴) 저장을 바닥내고, 요소 회로 효소를 늘려 둠', '(b) 아미노산이 한꺼번에 분해 → NH<sub>4</sub><sup>+</sup> 폭증, 그런데 <b>오르니틴이 부족</b>해 요소 회로가 못 돎 → 고양이에겐 <b>필수</b>', '(c) 오르니틴은 요소 회로 <b>중간체</b> → 회로를 다시 돌릴 수 있음'),
    explain=key('요소 회로는 <b>오르니틴이라는 “회전목마 좌석”</b>이 있어야 돈다. 좌석이 없으면 NH<sub>4</sub><sup>+</sup>가 탈 수 없다.') +
    fig(urea_cycle(), '') +
    steps('(a) 공복 후 고단백 식사 → 아미노산이 몰려 분해되어 NH<sub>4</sub><sup>+</sup>가 많이 생기는 상황을 만든다. 저장된 회로 중간체도 줄어 있다.',
          '(b) 아르기닌 → 아르기네이스 → 요소 + <b>오르니틴</b>. 아르기닌을 안 주면 오르니틴 공급이 끊겨 카르바모일 인산을 받을 좌석이 없다 → NH<sub>4</sub><sup>+</sup> 축적.',
          '고양이는 오르니틴·아르기닌을 스스로 충분히 만들지 못한다 → 고양이에게 아르기닌은 <b>필수 아미노산</b>.',
          '(c) 오르니틴 + 카르바모일 인산 → 시트룰린 → … → 아르기닌. 오르니틴만 있으면 회로가 다시 돈다.') +
    tip('사람도 성장기에는 아르기닌이 “준필수”(슬라이드 34).', '연결'))

add(id='P8', num='8', en_title='Oxidation of Glutamate', ko_title='글루탐산의 산화',
    slides='강의 슬라이드 21–22, 27–30', level=2,
    en='<p>Write a series of balanced equations and an overall equation for the net reaction describing the oxidation of 2 mol of glutamate to 2 mol of α-ketoglutarate and 1 mol of urea.</p>',
    ko='<p>글루탐산 2 mol이 α-케토글루타르산 2 mol과 요소 1 mol로 산화되는 과정을 균형 맞춘 반응식들로 쓰고, 알짜 반응식을 써라.</p>',
    answer=chips('2 글루탐산 + HCO<sub>3</sub><sup>−</sup> + 3ATP + 2NAD⁺ + 4H<sub>2</sub>O', '→ 2 α-KG + <b>요소</b> + 2ADP + AMP + 4P<sub>i</sub> + 2NADH (+ H⁺)'),
    explain=key('질소 2개의 입구: ① 글루탐산 → <b>NH<sub>4</sub><sup>+</sup></b> (GDH) ② 글루탐산 → <b>아스파르트산</b> (AST).') +
    align([('글루탐산 + NAD⁺ + H<sub>2</sub>O', '', '→ α-KG + NH<sub>4</sub><sup>+</sup> + NADH &nbsp;(GDH)'),
           ('글루탐산 + OAA', '', '→ α-KG + 아스파르트산 &nbsp;(AST)'),
           ('NH<sub>4</sub><sup>+</sup> + HCO<sub>3</sub><sup>−</sup> + 2ATP', '', '→ 카르바모일 인산 + 2ADP + P<sub>i</sub> &nbsp;(CPS I)'),
           ('카르바모일 인산 + 오르니틴', '', '→ 시트룰린 + P<sub>i</sub> &nbsp;(OTC)'),
           ('시트룰린 + 아스파르트산 + ATP', '', '→ 아르기니노숙신산 + AMP + PP<sub>i</sub> &nbsp;(ASS)'),
           ('PP<sub>i</sub> + H<sub>2</sub>O', '', '→ 2P<sub>i</sub>'),
           ('아르기니노숙신산', '', '→ 아르기닌 + 푸마르산 &nbsp;(ASL)'),
           ('아르기닌 + H<sub>2</sub>O', '', '→ 요소 + 오르니틴 &nbsp;(아르기네이스)'),
           ('푸마르산 + H<sub>2</sub>O → 말산; 말산 + NAD⁺', '', '→ OAA + NADH')]) +
    steps('오르니틴, OAA, 카르바모일 인산, 시트룰린, 아스파르트산, 아르기니노숙신산, 아르기닌, 푸마르산, 말산, PP<sub>i</sub>는 양변에서 지워진다.',
          'H<sub>2</sub>O: GDH 1 + PP<sub>i</sub> 1 + 아르기네이스 1 + 푸마레이스 1 = 4. P<sub>i</sub>: CPS 1 + OTC 1 + PP<sub>i</sub> 2 = 4.') +
    warn('NADH가 2개 생긴다(GDH, 말산 탈수소효소) → 산화적 인산화로 약 5 ATP를 돌려받아 요소 비용(ATP 4당량)을 메운다.', '포인트'))

add(id='P9', num='9', en_title='Transamination and the Urea Cycle', ko_title='아미노기 전이와 요소 회로',
    slides='강의 슬라이드 22, 29–30', level=1,
    en='<p>Aspartate aminotransferase has the highest activity of all the mammalian liver aminotransferases. Why?</p>',
    ko='<p>포유류 간의 아미노전이효소 가운데 아스파르트산 아미노전이효소(AST)의 활성이 가장 높다. 왜 그런가?</p>',
    answer=chips('요소 회로의 <b>두 번째 질소</b>는 <b>아스파르트산</b>이 공급', 'AST가 글루탐산의 아미노기를 OAA에 넘겨 아스파르트산을 <b>대량</b>으로 만들어야 함'),
    explain=key('요소 1개 = NH<sub>4</sub><sup>+</sup> 1개 + <b>아스파르트산 1개</b>. 질소의 절반이 AST를 지나간다.') +
    eq('글루탐산 + OAA ⇌ α-KG + 아스파르트산 &nbsp;(AST = GOT)', '시트룰린 + <b>아스파르트산</b> + ATP → 아르기니노숙신산 (요소 회로 ③)') +
    steps('모든 아미노산의 질소는 먼저 글루탐산으로 모인다.', '글루탐산의 질소는 두 길로: GDH로 NH<sub>4</sub><sup>+</sup>, AST로 아스파르트산 → 요소에 반반씩.',
          '푸마르산 → 말산 → OAA로 돌아와 다시 AST의 기질이 된다(아스파르트산-아르기니노숙신산 션트).') +
    tip('AST는 간·심장·근육에 많아 혈중 AST(SGOT)가 조직 손상 지표로 쓰인다.', '임상'))

add(id='P10', num='10', en_title='The Case against the Liquid Protein Diet', ko_title='“액상 단백질” 다이어트의 문제점',
    slides='강의 슬라이드 4, 34', level=2,
    en='<p>A weight-reducing diet heavily promoted some years ago required the daily intake of a “liquid protein” soup made of hydrolyzed gelatin (derived from collagen), water, and an assortment of vitamins. All other food and drink were to be avoided. People on this diet typically lost 10 to 14 lb in the first week. (a) Opponents argued that the weight loss was almost entirely due to water loss and would be regained very soon after a normal diet was resumed. What is the biochemical basis for this argument? (b) A few people on this diet died. What are some of the dangers inherent in the diet, and how can they lead to death?</p>',
    ko='<p>몇 년 전 크게 유행한 다이어트는 가수분해한 젤라틴(콜라겐 유래)·물·비타민으로 만든 “액상 단백질” 수프만 먹고 다른 음식과 음료는 모두 끊는 방식이었다. 첫 주에 보통 4.5–6.4 kg이 빠졌다. (a) 반대자들은 빠진 무게가 거의 물이며 정상 식사로 돌아가면 곧 다시 찐다고 주장했다. 그 생화학적 근거는? (b) 몇 명은 사망했다. 이 식단의 위험은 무엇이며 어떻게 죽음에 이르나?</p>',
    answer=chips('(a) 탄수화물이 없어 <b>글리코겐</b>이 바닥남 → 글리코겐에 붙어 있던 <b>물</b>이 빠짐 + 케톤체·요소 배설로 소변량 ↑', '(b) 젤라틴은 <b>필수 아미노산 부족</b>(특히 Trp 없음) → 체단백질(심장 근육 포함) 분해 → 부정맥·심부전, 케톤산증, 전해질 이상'),
    explain=key('젤라틴(콜라겐) = Gly·Pro·하이드록시프롤린 투성이, <b>트립토판 0</b> → “불완전 단백질”.') +
    steps('(a) 글리코겐 1 g은 물 약 2 g과 함께 저장된다. 탄수화물이 없으면 하루 이틀 만에 간·근육 글리코겐을 다 쓰고 그 물이 빠진다. 다시 먹으면 글리코겐과 물이 돌아온다.',
          '(a) 아미노산이 연료로 쓰이며 요소가 많이 생기고, 공복으로 케톤체도 늘어 소변으로 물이 더 빠진다(삼투성 이뇨).',
          '(b) 필수 아미노산 하나라도 없으면 단백질 합성이 멈춘다 → 몸은 근육 단백질을 분해해 필요한 아미노산을 얻는다.',
          '(b) 심장 근육이 손상되고 칼륨 등 전해질이 빠져 <b>부정맥</b> → 사망. 케톤산증·탈수도 위험.') +
    tip('필수 아미노산 9개 HILKMFTWV — 하나만 빠져도 “최소량의 법칙”처럼 전체 단백질 합성이 멈춘다(슬라이드 34).', '연결'))

add(id='P11', num='11', en_title='Ketogenic Amino Acids', ko_title='케톤생성 아미노산',
    slides='강의 슬라이드 40, 46, 48', level=1,
    en='<p>Which amino acids are exclusively ketogenic?</p>',
    ko='<p>오직 케톤생성만 하는 아미노산은 무엇인가?</p>',
    answer=chips('<b>류신(Leu, L)</b>과 <b>라이신(Lys, K)</b>'),
    explain=key('탄소 골격이 <b>아세틸-CoA·아세토아세틸-CoA로만</b> 가면 포도당이 될 수 없다 (동물은 아세틸-CoA → 포도당 불가, 16장).') +
    table(['구분', '아미노산', '이유'], [
        ['오직 케톤', '<b>류신, 라이신</b>', '아세틸-CoA·아세토아세트산으로만 분해'],
        ['케톤 + 포도당', '페닐알라닌, 티로신, 트립토판, 아이소류신, 트레오닌', '골격이 쪼개져 일부는 푸마르산·숙시닐-CoA·피루브산으로'],
        ['오직 포도당', '나머지 13개', '피루브산·TCA 중간체로만']], cls='left') +
    steps('케톤생성 묶음 LWFYK(I·T): 그중 W·F·Y·I·T는 포도당 쪽 경로도 있다.', '그래서 “오직” 케톤생성은 L과 K 두 개.') +
    tip('외우기: “<b>L</b>ys와 <b>L</b>eu — 둘 다 L로 시작하는 Lonely ketogenic”.', '외우기'))

add(id='P12', num='12', en_title='A Genetic Defect in Amino Acid Metabolism: A Case History', ko_title='아미노산 대사의 유전 결함 — 증례',
    slides='강의 슬라이드 58, 64–66', level=1,
    en=f'''<p>A two-year-old child was taken to the hospital. His mother said that he vomited frequently, especially after feedings. The child’s weight and physical development were below normal. His hair, although dark, contained patches of white. A urine sample treated with ferric chloride (FeCl<sub>3</sub>) gave a green color characteristic of the presence of phenylpyruvate. Quantitative analysis of urine samples gave the results shown in the table.</p>
{table(['Substance', "Patient's urine (mM)", 'Normal urine (mM)'], [['Phenylalanine', '7.0', '0.01'], ['Phenylpyruvate', '4.8', '0'], ['Phenyllactate', '10.3', '0']])}
<p>(a) Suggest which enzyme might be deficient in this child. Propose a treatment. (b) Why does phenylalanine appear in the urine in large amounts? (c) What is the source of phenylpyruvate and phenyllactate? Why does this pathway (normally not functional) come into play when the concentration of phenylalanine rises? (d) Why does the boy’s hair contain patches of white?</p>''',
    ko='<p>두 살 아이가 병원에 왔다. 자주, 특히 먹은 뒤에 토했다. 체중과 발육이 정상보다 낮았고, 검은 머리에 흰 반점이 있었다. 소변에 염화철(FeCl<sub>3</sub>)을 넣으니 페닐피루브산을 뜻하는 초록색이 나왔고, 정량 결과는 위 표와 같았다(페닐알라닌 7.0 vs 0.01, 페닐피루브산 4.8 vs 0, 페닐젖산 10.3 vs 0 mM).</p><p>(a) 어떤 효소가 결핍됐을까? 치료법은? (b) 페닐알라닌이 소변에 많은 이유는? (c) 페닐피루브산과 페닐젖산은 어디서 오나? 평소 쓰이지 않던 이 경로가 왜 작동하나? (d) 머리에 흰 반점이 있는 이유는?</p>',
    answer=chips('(a) <b>페닐알라닌 수산화효소</b> 결핍 = <b>PKU</b> → 저페닐알라닌 식이 (+ 티로신 보충)', '(b) Phe를 티로신으로 못 바꿔 혈중 Phe ↑ → 신장 재흡수 한계 초과', '(c) Phe → (아미노기 전이) <b>페닐피루브산</b> → (환원) <b>페닐젖산</b>: 농도가 높아지자 평소엔 미미한 아미노전이효소 반응이 커짐', '(d) 티로신 부족 + Phe가 티로시네이스 방해 → <b>멜라닌</b> ↓'),
    explain=key('막힌 곳 <b>앞</b>(Phe)은 쌓이고, <b>뒤</b>(티로신 → 멜라닌)는 모자란다. 쌓인 Phe는 옆길로 넘친다.') +
    fig(pku_path(), '') +
    fig(flow(['페닐알라닌 ↑', '페닐피루브산', '페닐젖산 / 페닐아세트산'], arrow_labels=['아미노전이효소 (PLP)', '환원 / 탈카복실화'], colors=[C['red'], C['orange'], C['orange']], box_h=36, width=520, font=10.5), 'PKU의 넘침 경로 (슬라이드 66)') +
    steps('(a) 페닐알라닌 수산화효소(보조인자 THBP)가 없으면 Phe → 티로신이 막힌다. 치료: 아기 때부터 Phe를 줄인 특수 식이, 티로신은 이제 필수가 되므로 보충.',
          '(b) 혈중 Phe가 정상의 수십 배 → 신장이 다 재흡수 못 해 소변으로.',
          '(c) 아미노전이효소의 Km이 높아 평소엔 거의 안 일어나지만, Phe가 쌓이면 반응이 빨라진다(질량 작용).',
          '(d) 멜라닌은 티로신에서 티로시네이스로 만들어진다. 티로신 부족 + 많은 Phe가 티로시네이스를 경쟁적으로 억제 → 색소 감소.') +
    warn('PKU 신생아 선별검사로 일찍 찾아 식이 조절을 하면 뇌 발달 장애를 막을 수 있다. 아스파탐(Phe 포함) 주의 표시도 이 때문.', '약학'))

add(id='P13', num='13', en_title='Role of Cobalamin in Amino Acid Catabolism', ko_title='아미노산 이화에서 코발라민(B12)의 역할',
    slides='강의 슬라이드 42, 57, 59–60, 68–69', level=2,
    en='<p>Pernicious anemia is caused by impaired absorption of vitamin B<sub>12</sub>. What is the effect of this impairment on the catabolism of amino acids? Are all amino acids equally affected? (Hint: See Box 17-2.)</p>',
    ko='<p>악성빈혈은 비타민 B<sub>12</sub> 흡수 장애로 생긴다. 이 장애는 아미노산 이화에 어떤 영향을 주나? 모든 아미노산이 똑같이 영향을 받나? (힌트: 글상자 17-2)</p>',
    answer=chips('<b>메틸말로닐-CoA 뮤테이스</b>(B<sub>12</sub>) 정지 → 프로피오닐-CoA를 거치는 <b>Ile·Met·Thr·Val</b> 분해 막힘 → 메틸말론산 ↑', '<b>메티오닌 합성효소</b>(B<sub>12</sub>) 정지 → 호모시스테인 ↑, N<sup>5</sup>-메틸-THF에 갇힘', '→ 모든 아미노산이 같지 않음: 주로 IMTV(+ 메티오닌 재생)'),
    explain=key('사람에서 B<sub>12</sub>가 필요한 효소는 딱 둘: <b>메틸말로닐-CoA 뮤테이스</b>와 <b>메티오닌 합성효소</b>.') +
    fig(flow(['Ile · Met · Thr · Val', '프로피오닐-CoA', '메틸말로닐-CoA', '숙시닐-CoA'], arrow_labels=['', '비오틴', '✕ 뮤테이스 (B₁₂)'], colors=[C['navy'], C['navy'], C['red'], C['gray']], box_h=36, width=540, font=10.5), '') +
    steps('IMTV의 탄소는 숙시닐-CoA로 못 들어가고 메틸말로닐-CoA → <b>메틸말론산</b>으로 쌓인다(메틸말론산혈증, 슬라이드 68).',
          '호모시스테인 + N<sup>5</sup>-메틸-THF → 메티오닌 + THF (메티오닌 합성효소, B<sub>12</sub>)이 막혀 <b>호모시스테인</b>이 쌓이고, 엽산이 메틸-THF 형태에 갇힌다(“메틸 함정”).',
          '메틸렌-THF가 부족 → DNA(티미딘) 합성 ↓ → 거대적혈모구성 빈혈(슬라이드 69).',
          '다른 아미노산(예: 알라닌, 글루탐산)의 분해는 거의 영향이 없다.') +
    tip('17장 홀수 지방산의 마지막 단계와 같은 효소(메틸말로닐-CoA 뮤테이스).', '연결'))

add(id='P14', num='14', en_title='Vegetarian Diets', ko_title='채식 식단',
    slides='강의 슬라이드 57, 68–69', level=1,
    en='<p>Vegetarian diets can provide high levels of antioxidants and a lipid profile that can help prevent coronary disease. However, there can be some associated problems. Blood samples were taken from a large group of volunteer subjects who were vegans (strict vegetarians: no animal products), lactovegetarians (vegetarians who eat dairy products), or omnivores (individuals with a varied diet, including meat). In each case, the volunteers had followed the diet for several years. The blood levels of both homocysteine and methylmalonate were elevated in the vegan group, somewhat lower in the lactovegetarian group, and much lower in the omnivore group. Explain.</p>',
    ko='<p>채식은 항산화 물질이 많고 관상동맥 질환 예방에 좋은 지질 조성을 줄 수 있지만 문제도 있다. 비건(동물성 식품 전혀 안 먹음), 락토 채식주의자(유제품은 먹음), 잡식자(고기 포함)에게서 혈액을 뽑았다. 모두 수년간 그 식단을 지켰다. 호모시스테인과 메틸말론산 농도가 비건에서 높았고, 락토 채식주의자에서 조금 낮았고, 잡식자에서 훨씬 낮았다. 설명하라.</p>',
    answer=chips('<b>비타민 B<sub>12</sub></b>는 <b>동물성 식품</b>(고기 > 유제품)에만 있다', 'B<sub>12</sub> ↓ → 메티오닌 합성효소 ↓ → <b>호모시스테인 ↑</b>', 'B<sub>12</sub> ↓ → 메틸말로닐-CoA 뮤테이스 ↓ → <b>메틸말론산 ↑</b>', '섭취량: 비건 &lt; 락토 &lt; 잡식 → 농도 순서 반대'),
    explain=key('두 지표가 동시에 오른다 = B<sub>12</sub>가 필요한 <b>두 효소가 모두</b> 느려졌다 = B<sub>12</sub> 결핍의 지문.') +
    fig(bars([('비건', 3, C['red'], '가장 높음'), ('락토 채식', 2, C['orange'], '중간 (유제품의 B₁₂)'), ('잡식', 1, C['green'], '낮음')], height=110, vmax=4, width=540), '') +
    steps('B<sub>12</sub>는 미생물만 만들고, 동물 조직에 쌓인다 → 식물에는 거의 없다.',
          '메티오닌 합성효소: 호모시스테인 + N<sup>5</sup>-메틸-THF → 메티오닌. B<sub>12</sub> 없으면 호모시스테인 축적.',
          '메틸말로닐-CoA 뮤테이스: 메틸말로닐-CoA → 숙시닐-CoA. 없으면 메틸말론산 축적.') +
    tip('호모시스테인 ↑ = 심혈관 질환 위험 요인. 비건은 B<sub>12</sub> 보충제가 권장된다.', '임상'))

add(id='P15', num='15', en_title='Pernicious Anemia', ko_title='악성빈혈',
    slides='강의 슬라이드 69', level=1,
    en='<p>Vitamin B<sub>12</sub> deficiency can arise from a few rare genetic diseases that lead to low B<sub>12</sub> levels despite a normal diet that includes B<sub>12</sub>-rich meat and dairy sources. These conditions cannot be treated with dietary B<sub>12</sub> supplements. Explain.</p>',
    ko='<p>B<sub>12</sub>가 풍부한 고기·유제품을 정상적으로 먹어도 B<sub>12</sub>가 낮아지는 드문 유전 질환들이 있다. 이런 경우는 먹는 B<sub>12</sub> 보충제로 치료할 수 없다. 설명하라.</p>',
    answer=chips('문제는 섭취가 아니라 <b>흡수</b>(내인자·수용체·운반 단백질 결함)', '먹는 B<sub>12</sub>도 똑같이 흡수가 안 됨 → <b>근육 주사</b>로 혈액에 직접 공급해야 함'),
    explain=key('B<sub>12</sub>는 위의 <b>내인자(intrinsic factor)</b>와 결합해야 회장에서 흡수된다.') +
    fig(vflow(['음식의 B₁₂', '위: 내인자(IF)와 결합', '회장: IF 수용체로 흡수', '혈액: 트랜스코발라민이 운반'], notes=['', '✕ 내인자 결핍', '✕ 수용체 결함'],
              colors=[C['green'], C['orange'], C['orange'], C['blue']], box_h=24, gap=22, width=520, font=10.5), '') +
    steps('유전적으로 내인자, 회장 수용체, 운반 단백질 중 하나가 고장 나면 장에서 B<sub>12</sub>를 아무리 많이 먹어도 들어오지 못한다.',
          '그래서 장을 건너뛰는 <b>주사</b>(근육 내)로 B<sub>12</sub>를 준다.') +
    tip('고전적 악성빈혈은 내인자를 만드는 위 벽세포에 대한 자가면역 질환. 위 절제 환자도 같은 이유로 주사가 필요.', '임상'))

add(id='P21', num='21', en_title='Treatments for a Genetic Disease', ko_title='유전 질환의 치료 — 단풍당뇨증',
    slides='강의 슬라이드 67, 71', level=2,
    en='<p>The strict dietary controls required to stem the progress of maple syrup urine disease are difficult to follow for a lifetime, and patients may experience poor metabolic control that leads to neurological symptoms. In these cases, treatment can involve an organ transplant from a suitable donor. Organ transplantation involves considerable risk, but success can greatly alleviate this metabolic disorder and reduce the need for dietary restrictions. Which organ could be transplanted to gain this effect, and why?</p>',
    ko='<p>단풍당뇨증의 진행을 막는 엄격한 식이 조절은 평생 지키기 어렵고, 대사 조절이 나빠지면 신경 증상이 생긴다. 이런 경우 적합한 공여자로부터 장기 이식을 할 수 있다. 위험은 크지만 성공하면 질환이 크게 좋아지고 식이 제한도 줄어든다. 어떤 장기를 이식하면 되며, 그 이유는?</p>',
    answer=chips('<b>간</b> 이식', '간에는 결핍된 <b>가지사슬 α-케토산 탈수소효소</b>(BCKDH)가 많아, 정상 간이 들어오면 몸 전체의 가지사슬 α-케토산을 처리해 줌'),
    explain=key('단풍당뇨증 = Val·Ile·Leu 분해 2단계 효소 <b>BCKDH</b> 결핍 → α-케토산이 쌓여 소변에서 단풍시럽 냄새.') +
    fig(flow(['Val · Ile · Leu', 'α-케토산', '아실-CoA 유도체'], arrow_labels=['가지사슬 아미노전이효소 (주로 근육)', '✕ BCKDH (간에 많음)'], colors=[C['navy'], C['red'], C['gray']], box_h=38, width=540, font=10.5), '') +
    steps('가지사슬 아미노산은 다른 아미노산과 달리 <b>간 밖</b>(근육)에서 먼저 아미노기 전이가 일어난다(슬라이드 71).',
          '생긴 α-케토산은 혈액으로 나와 BCKDH 활성이 높은 <b>간</b>에서 많이 처리된다.',
          '정상 간을 이식하면 그 간이 BCKDH를 공급해 α-케토산을 산화 → 혈중 농도 정상화 → 식이 제한 완화.') +
    tip('실제로 단풍당뇨증 환자의 간을 다른 환자에게 이식하는 “도미노 간 이식”도 한다 — 그 간은 다른 사람 몸에서는 근육 등의 BCKDH 덕분에 문제가 적다.', '재미'))

for _n in ('16', '17', '18', '19', '20'):
    ALL_ITEMS.append(dict(id='P' + _n, num=_n, level=3, kind='PROBLEM'))
ALL_ITEMS.sort(key=lambda i: int(i['num']))
