# -*- coding: utf-8 -*-
"""Chapter 17 — Fatty Acid Catabolism"""
from helpers import *

CHAPTER = '17'
CH_TITLE = '지방산 분해'
CH_EN = 'Fatty Acid Catabolism'
STAT = ('4', 'β-산화 단계 (지도 수록)')
SCOPE = ('교수님 17장 강의(슬라이드 1–46) 범위 = <b>17.1 지방의 소화·동원·수송</b>, <b>17.2 지방산 산화</b>(β-산화, 불포화·홀수 지방산, 조절, 퍼옥시좀·ω-산화), '
         '<b>17.3 케톤체</b> — 17장 전체. 17장에는 본문 예제가 없어.')
INCLUDE = ['<b>지방 저장·동원</b> — 문제 1, 2, 6, 27',
           '<b>활성화·카르니틴 셔틀</b> — 문제 3, 4, 5, 9',
           '<b>β-산화 반응·횟수</b> — 문제 7, 8, 10, 11, 21, 22, 25',
           '<b>홀수 지방산·B<sub>12</sub></b> — 문제 17, 18, 26',
           '<b>조절·독성·케톤체</b> — 문제 14, 16, 19, 20']
EXCLUDE = ['<b>문제 28</b> — DATA ANALYSIS PROBLEM']

ALL_ITEMS = []


def add(**kw):
    kw.setdefault('section', '연습문제')
    kw.setdefault('kind', 'PROBLEM')
    ALL_ITEMS.append(kw)


def beta_cycle():
    """4 steps of beta-oxidation vs TCA analog"""
    return vflow(['아실-CoA (Cₙ)', 'trans-Δ²-엔오일-CoA', 'L-3-하이드록시아실-CoA', '3-케토아실-CoA', '아실-CoA (Cₙ₋₂) + 아세틸-CoA'],
                 notes=['① 아실-CoA 탈수소효소: FAD → FADH₂', '② 엔오일-CoA 수화효소: + H₂O', '③ 하이드록시아실-CoA 탈수소효소: NAD⁺ → NADH', '④ 티올레이스: + CoA'],
                 colors=[C['navy'], C['blue'], C['blue'], C['blue'], C['green']], box_h=26, gap=24, width=560)


def carnitine():
    W, H = 520, 200
    b = arrowdef('cn', C['gray'])
    b += f'<rect x="10" y="20" width="150" height="160" rx="12" fill="#f0fdf4" stroke="#86efac"/>' + T(85, 40, '세포질', 12, C['green'], weight=900)
    b += f'<rect x="200" y="12" width="36" height="176" rx="6" fill="#fde68a"/>' + f'<rect x="270" y="12" width="36" height="176" rx="6" fill="#fde68a"/>'
    b += T(218, 200, '외막', 9.5, C['gray']) + T(288, 200, '내막', 9.5, C['gray'])
    b += f'<rect x="340" y="20" width="170" height="160" rx="12" fill="#eff6ff" stroke="#93c5fd"/>' + T(425, 40, '기질 (β-산화)', 12, C['blue'], weight=900)
    b += T(85, 80, '지방산 + CoA + ATP', 10.5) + T(85, 96, '→ 아실-CoA', 10.5, C['ink'], weight=700) + T(85, 112, '(CoA 풀 ①)', 9.5, C['gray'])
    b += T(253, 70, 'CAT I', 10.5, C['red'], weight=900) + T(253, 84, '말로닐-CoA', 9, C['red']) + T(253, 96, '억제!', 9, C['red'], weight=700)
    b += T(253, 130, '아실-카르니틴', 10, C['orange'], weight=700) + T(253, 144, '수송체', 9.5, C['gray'])
    b += T(425, 80, 'CAT II', 10.5, C['blue'], weight=900) + T(425, 98, '아실-카르니틴 + CoA', 10.5) + T(425, 114, '→ 아실-CoA', 10.5, C['ink'], weight=700) + T(425, 130, '(CoA 풀 ②)', 9.5, C['gray'])
    b += f'<line x1="150" y1="104" x2="330" y2="104" stroke="{C["orange"]}" stroke-width="2.2" marker-end="url(#cn)"/>'
    b += T(260, 172, '아실기만 카르니틴에 실려 건너감 · CoA는 건너가지 않는다', 10.5, C['ink'], weight=700)
    return svg(W, H + 10, b)


def odd_chain():
    return flow(['프로피오닐-CoA (C3)', 'D-메틸말로닐-CoA', 'L-메틸말로닐-CoA', '숙시닐-CoA → TCA'],
                arrow_labels=['카복실화 (비오틴·ATP)', '에피머화', '뮤테이스 (B₁₂)'], colors=[C['orange'], C['navy'], C['navy'], C['green']], box_h=44)


def front_pages():
    t = table(['단계', '반응', '효소', '산물', 'TCA에서 닮은 반응'], [
        ['①', '아실-CoA → trans-Δ<sup>2</sup>-엔오일-CoA', '아실-CoA 탈수소효소 (길이별 동위효소)', '<b>FADH<sub>2</sub></b>', '숙신산 → 푸마르산 (FAD)'],
        ['②', '엔오일-CoA + H<sub>2</sub>O → L-3-하이드록시아실-CoA', '엔오일-CoA 수화효소', '—', '푸마르산 → 말산 (수화)'],
        ['③', 'L-3-하이드록시아실-CoA → 3-케토아실-CoA', '3-하이드록시아실-CoA 탈수소효소', '<b>NADH</b>', '말산 → OAA (NAD<sup>+</sup>)'],
        ['④', '3-케토아실-CoA + CoA → 아실-CoA(C<sub>n−2</sub>) + <b>아세틸-CoA</b>', '티올레이스', '<b>아세틸-CoA</b>', '—']], cls='left')
    p1 = f'''<h2 class="pt"><span class="n">MAP</span> β-산화 4단계 &amp; 팔미트산 수지 계산</h2>
<p class="lead">한 바퀴 = 탄소 2개(아세틸-CoA)를 떼고 <b>FADH<sub>2</sub> 1 + NADH 1</b>. 탄소 n개 짝수 지방산 → <b>(n/2 − 1)바퀴</b>, 아세틸-CoA n/2개.</p>
<div class="card">{t}</div>
<div class="grid2" style="margin-top:3mm">
 <div class="card"><h4>🔥 팔미토일-CoA (16:0) 완전 산화</h4>
  {table(['출처', '개수', '× ATP', '= ATP'], [['FADH<sub>2</sub> (β-산화)', '7', '1.5', '10.5'], ['NADH (β-산화)', '7', '2.5', '17.5'], ['아세틸-CoA (TCA+전자전달)', '8', '10', '80'], ['<b>합계</b>', '', '', '<b>108</b>']])}
  <p class="small">유리 팔미트산 기준: 활성화(ATP → AMP + PP<sub>i</sub> = ATP 2개 당량)를 빼서 <b>106 ATP</b>. O<sub>2</sub> 소비 23개.</p></div>
 <div class="card"><h4>🧮 바퀴 수 빠른 계산</h4>
  <p>16:0 팔미트산 → 7바퀴 → 아세틸-CoA 8</p><p>18:0 스테아르산 → 8바퀴 → 아세틸-CoA 9</p><p>20:0 아라키드산 → 9바퀴 → 아세틸-CoA 10</p>
  <p>홀수 (예: 11:0) → 4바퀴 → 아세틸-CoA 4 + <b>프로피오닐-CoA 1</b></p>
  {warn('마지막 바퀴는 C4 → 아세틸-CoA 2개가 한꺼번에 나와서, 바퀴 수 = 아세틸-CoA 수 − 1.', '함정')}</div>
</div>'''
    p2 = f'''<h2 class="pt"><span class="n">KIT</span> 운반 · 조절 · 특수 지방산 · 케톤체</h2>
<div class="grid2">
 <div>
  <div class="card"><h4><span class="no">1</span> 지방 동원과 카르니틴 셔틀</h4>
   <p>에피네프린·글루카곤 → cAMP → PKA → 페릴리핀·호르몬 민감성 리파아제 인산화 → TG 분해 → 지방산은 알부민에 실려 혈액으로, 글리세롤은 간 → 당신생</p>
   <figure class="fig">{carnitine()}</figure></div>
  <div class="card" style="margin-top:3mm"><h4><span class="no">2</span> 조절</h4>
   <p><b>말로닐-CoA</b>(지방산 합성 첫 중간체, ACC가 만듦) → <b>CAT I 억제</b> → 합성 중엔 분해 입구를 닫는다.</p>
   <p>AMPK(에너지 부족) → ACC 인산화(억제) → 말로닐-CoA ↓ → 지방산 산화 ↑. NADH ↑ → ③ 억제, 아세틸-CoA ↑ → ④ 억제.</p></div>
 </div>
 <div>
  <div class="card"><h4><span class="no">3</span> 특수한 지방산</h4>
   <p><b>불포화</b>: cis 이중결합 → <b>엔오일-CoA 이성질화효소</b>(cis-Δ<sup>3</sup> → trans-Δ<sup>2</sup>), 다중불포화는 + 2,4-다이엔오일-CoA 환원효소(NADPH)</p>
   <p><b>홀수</b>: 마지막에 프로피오닐-CoA → 숙시닐-CoA (비오틴, <b>B<sub>12</sub></b>) → <b>포도당이 될 수 있다</b></p>
   <figure class="fig">{odd_chain()}</figure>
   <p><b>퍼옥시좀</b>: 매우 긴 사슬, 첫 단계에서 FADH<sub>2</sub> 대신 H<sub>2</sub>O<sub>2</sub> · <b>α-산화</b>: 피탄산(가지) · <b>ω-산화</b>: 소포체, 끝 탄소부터</p></div>
  <div class="card" style="margin-top:3mm"><h4><span class="no">4</span> 케톤체 (간 미토콘드리아)</h4>
   <p>2 아세틸-CoA → 아세토아세틸-CoA → HMG-CoA → <b>아세토아세트산</b> → D-β-하이드록시뷰티르산 / 아세톤</p>
   <p>공복·당뇨: OAA가 당신생으로 빠짐 → 아세틸-CoA가 TCA에 못 들어감 → 케톤체 ↑. 간은 만들기만 하고(전이효소 없음) 심장·근육·뇌가 쓴다.</p></div>
 </div>
</div>'''
    return [p1, p2]


# ------------------------------------------------------------------ items
add(id='P1', num='1', en_title='Energy in Triacylglycerols', ko_title='트라이아실글리세롤 속의 에너지',
    slides='강의 슬라이드 4–5', level=1,
    en='<p>On a per-carbon basis, where does the largest amount of biologically available energy in triacylglycerols reside: in the fatty acid portions or in the glycerol portion? Indicate how knowledge of the chemical structure of triacylglycerols provides the answer.</p>',
    ko='<p>탄소 1개당으로 따질 때, 트라이아실글리세롤에서 생물학적으로 쓸 수 있는 에너지가 가장 많은 곳은 지방산 부분인가, 글리세롤 부분인가? 트라이아실글리세롤의 화학 구조로 어떻게 답을 알 수 있는지 설명하라.</p>',
    answer=chips('<b>지방산 부분</b>', '지방산 탄소는 대부분 –CH<sub>2</sub>–(가장 환원됨) / 글리세롤 탄소는 모두 O와 결합(이미 부분 산화)'),
    explain=key('탄소가 <b>환원</b>되어 있을수록(H가 많고 O가 적을수록) 산화될 때 에너지가 많이 나온다(13장 문제 27, 16장 문제 4).') +
    table(['부분', '탄소의 모습', '산화 상태'], [['지방산 (예: 팔미트산)', '–CH<sub>2</sub>–CH<sub>2</sub>–…–CH<sub>3</sub> (탄소 16개 중 15개가 C–H만)', '<b>매우 환원</b> → 에너지 많음'],
                                         ['글리세롤', '–CH<sub>2</sub>–O– / –CH–O– / –CH<sub>2</sub>–O– (세 탄소 모두 O와 결합)', '이미 탄수화물 수준으로 산화 → 에너지 적음']], cls='left') +
    steps('트라이아실글리세롤 = 글리세롤(C3) + 지방산 3개(각 C16~C18). 탄소 수로도 지방산이 95% 이상.',
          '지방산의 –CH<sub>2</sub>–는 CO<sub>2</sub>까지 가는 동안 전자를 많이 내준다(β-산화 한 바퀴마다 FADH<sub>2</sub> + NADH).',
          '글리세롤의 탄소는 이미 –OH/–O–에 붙어 있어 탄수화물과 비슷한 수준.') +
    tip('지방이 g당 약 9 kcal, 탄수화물이 약 4 kcal인 이유. 지방은 물도 거의 안 머금어서 저장 효율이 훨씬 좋아(슬라이드 5).', '연결'))

add(id='P2', num='2', en_title='Effect of PDE Inhibitor on Adipocytes', ko_title='PDE 억제제가 지방세포에 미치는 영향',
    slides='강의 슬라이드 15–16', level=1,
    en='<p>How would the addition of a cAMP phosphodiesterase (PDE) inhibitor affect the response of an adipocyte to epinephrine? (Hint: See Fig. 12-4.)</p>',
    ko='<p>cAMP 포스포다이에스터레이스(PDE) 억제제를 넣으면 에피네프린에 대한 지방세포의 반응은 어떻게 달라지는가? (힌트: 그림 12-4)</p>',
    answer=chips('cAMP가 분해되지 않아 <b>더 오래·더 많이</b> 남음', '→ PKA 계속 활성 → 지방 분해(TG → 지방산 + 글리세롤) <b>증가·연장</b>'),
    explain=key('PDE = cAMP를 끄는 “지우개”. 지우개를 빼앗으면 신호가 꺼지지 않는다.') +
    fig(vflow(['에피네프린 → β-아드레날린 수용체', 'G 단백질 → 아데닐산 고리화효소 → cAMP ↑', 'PKA → 페릴리핀·호르몬 민감성 리파아제 인산화', '저장 TG 분해 → 지방산 방출 ↑'],
              notes=['', '✕ PDE (cAMP → AMP)가 억제됨', ''], colors=[C['red'], C['orange'], C['orange'], C['green']], box_h=26, gap=22, width=520), '') +
    steps('보통은 에피네프린 신호가 끝나면 PDE가 cAMP → AMP로 바꿔 PKA를 끈다.',
          'PDE 억제제가 있으면 cAMP가 쌓여 PKA가 계속 켜짐 → 지방 분해가 더 강하고 길게 지속.',
          '카페인·테오필린(PDE 억제제)이 지방 분해를 약간 촉진한다고 알려진 이유.') +
    tip('음악(신호)을 끄는 버튼(PDE)이 고장 나면, 한 번 튼 음악이 계속 크게 나온다.', '비유'))

add(id='P3', num='3', en_title='Compartmentation in β Oxidation', ko_title='β-산화의 구획화',
    slides='강의 슬라이드 18–21', level=2,
    en='<p>The activation of free palmitate to its coenzyme A derivative (palmitoyl-CoA) in the cytosol occurs before it can be oxidized in the mitochondrion. After adding palmitate and [<sup>14</sup>C]coenzyme A to a liver homogenate, you find palmitoyl-CoA isolated from the cytosolic fraction is radioactive, but that isolated from the mitochondrial fraction is not. Explain.</p>',
    ko='<p>유리 팔미트산은 미토콘드리아에서 산화되기 전에 세포질에서 CoA 유도체(팔미토일-CoA)로 활성화된다. 간 균질액에 팔미트산과 [<sup>14</sup>C]CoA를 넣었더니, 세포질 분획의 팔미토일-CoA는 방사성이지만 미토콘드리아 분획의 팔미토일-CoA는 방사성이 아니었다. 설명하라.</p>',
    answer=chips('세포질과 미토콘드리아의 <b>CoA 풀은 따로</b>', '팔미토일기는 <b>카르니틴</b>에 실려 들어가고, CoA는 막을 건너지 않음', '→ 기질에서 <b>미토콘드리아 자신의(표지 안 된) CoA</b>와 다시 결합'),
    explain=key('막을 건너는 건 “아실기 + 카르니틴”뿐. 표지된 CoA는 세포질에 남는다.') +
    fig(carnitine(), '카르니틴 셔틀: CAT I (외막) → 수송체 → CAT II (기질 쪽)') +
    steps('세포질: 팔미트산 + [<sup>14</sup>C]CoA + ATP → [<sup>14</sup>C]팔미토일-CoA (방사성) ✔.',
          'CAT I: 팔미토일기가 카르니틴으로 옮겨져 팔미토일-카르니틴이 되고, [<sup>14</sup>C]CoA는 세포질에 풀려남.',
          '팔미토일-카르니틴이 내막을 통과 → CAT II가 기질의 CoA(표지 없음)에 다시 옮김 → 미토콘드리아 팔미토일-CoA는 방사성 ✕.') +
    tip('짐(아실기)만 다른 차(카르니틴)로 옮겨 실어 국경을 넘고, 국경 너머에서 그 나라 차(미토콘드리아 CoA)에 다시 싣는 거야.', '비유'))

add(id='P4', num='4', en_title='Mutant Carnitine Acyltransferase', ko_title='돌연변이 카르니틴 아실전이효소',
    slides='강의 슬라이드 20, 32–33', level=2,
    en='<p>What changes in metabolic pattern would result from a mutation in the muscle carnitine acyltransferase 1 in which the mutant protein has lost its affinity for malonyl-CoA but not its catalytic activity?</p>',
    ko='<p>근육의 카르니틴 아실전이효소 I(CAT I)이 촉매 활성은 그대로인데 말로닐-CoA에 대한 친화도만 잃는 돌연변이가 생기면, 대사 양상은 어떻게 바뀌는가?</p>',
    answer=chips('CAT I이 말로닐-CoA로 <b>억제되지 않음</b>', '→ 영양이 충분할 때(말로닐-CoA ↑)도 지방산이 계속 미토콘드리아로 들어가 <b>β-산화가 멈추지 않음</b>', '→ 지방산 합성·저장과 산화가 동시에 → <b>헛된 회로</b>, 포도당 사용 조절도 흐트러짐'),
    explain=key('말로닐-CoA = “지금은 지방을 저장할 때니 태우지 마” 신호. 그 신호를 못 들으면 브레이크가 없다.') +
    fig(carnitine(), '정상: 말로닐-CoA가 CAT I을 막아 분해 입구를 닫음') +
    steps('정상: 식후(인슐린 ↑) ACC가 말로닐-CoA를 만들고, 말로닐-CoA가 CAT I을 억제 → 지방산은 산화되지 않고 저장으로.',
          '돌연변이: 말로닐-CoA가 많아도 CAT I이 계속 작동 → 지방산이 항상 β-산화로 → 에너지가 남아도 지방을 태움.',
          '결과: 근육은 지방산을 더 쓰고 포도당은 덜 쓰는 쪽으로 기울고, 합성된 지방산이 바로 분해되는 헛된 회로로 ATP 낭비.') +
    tip('ACC2 억제제가 비만 치료 후보인 이유(슬라이드 34)와 같은 논리: 말로닐-CoA를 줄이면 지방 연소가 늘어난다.', '연결'))

add(id='P5', num='5', en_title='Effect of Carnitine Deficiency', ko_title='카르니틴 결핍의 영향',
    slides='강의 슬라이드 18–21', level=2,
    en='''<p>An individual developed a condition characterized by progressive muscular weakness and aching muscle cramps. The symptoms were aggravated by fasting, exercise, and a high-fat diet. An homogenate of a skeletal muscle specimen from the patient oxidized added oleate more slowly than did control homogenates consisting of muscle specimens from healthy individuals. When the pathologist added carnitine to the patient’s muscle homogenate, the rate of oleate oxidation equaled that in the control homogenates. Based on these results, the attending physician diagnosed the patient as having a carnitine deficiency.<br><b>a.</b> Why did added carnitine increase the rate of oleate oxidation in the patient’s muscle homogenate?<br><b>b.</b> Why did fasting, exercise, and a high-fat diet aggravate the patient’s symptoms?<br><b>c.</b> Suggest two possible reasons for the deficiency of muscle carnitine in this individual.</p>''',
    ko='<p>어떤 사람에게 점점 심해지는 근력 약화와 아픈 근육 경련이 생겼다. 증상은 공복, 운동, 고지방 식사로 악화됐다. 환자의 골격근 균질액은 건강한 사람의 것보다 올레산을 더 느리게 산화했다. 병리학자가 환자의 근육 균질액에 카르니틴을 넣자 올레산 산화 속도가 정상과 같아졌다. 의사는 카르니틴 결핍으로 진단했다.<br><b>a.</b> 카르니틴을 넣으면 왜 올레산 산화가 빨라졌는가?<br><b>b.</b> 공복·운동·고지방 식사는 왜 증상을 악화시켰는가?<br><b>c.</b> 이 사람의 근육 카르니틴이 부족한 이유 두 가지를 제안하라.</p>',
    answer=chips('a. 카르니틴 = 지방산을 미토콘드리아로 나르는 <b>운반체</b> → 보충하면 β-산화 정상화', 'b. 셋 다 근육이 <b>지방산 연료에 더 의존</b>하게 만드는 상황', 'c. ① 카르니틴 <b>합성</b> 결함(간·신장, Lys·Met에서) ② 근육으로의 <b>수송체</b> 결함 (또는 신장 손실·식이 부족)'),
    explain=key('지방산은 카르니틴 없이는 미토콘드리아 안(β-산화 장소)으로 못 들어간다.') +
    steps('<b>a.</b> 긴 사슬 지방산(올레산 C18)은 아실-CoA → 아실-카르니틴 형태로만 내막을 통과. 카르니틴이 부족하면 입구에서 병목 → 넣어 주면 해소.',
          '<b>b.</b> 공복(포도당·글리코겐 ↓), 오래 하는 운동, 고지방 식사 모두 근육이 지방산을 주 연료로 쓰는 상황 → 연료를 못 써서 에너지 부족·경련, 근육에 지방 축적.',
          '<b>c.</b> 카르니틴은 주로 간·신장에서 라이신과 메싸이오닌으로 만들어져 혈액으로 근육에 전달된다 → ① 합성 효소 결함 ② 근육 세포막의 카르니틴 수송체(OCTN2) 결함 ③ 신장에서 과도하게 배출 ④ 식이 부족(채식·영양실조) 등.') +
    fig(carnitine(), '카르니틴이 없으면 가운데 다리(셔틀)가 끊긴다') +
    tip('치료: 카르니틴 보충 + 지방 대신 탄수화물 위주 식사, 공복 피하기.', '임상'))

add(id='P6', num='6', en_title='Fuel Reserves in Adipose Tissue', ko_title='지방 조직의 연료 저장량',
    slides='강의 슬라이드 4–5', level=2,
    en='<p>Triacylglycerols, with their hydrocarbon-like fatty acids, have the highest energy content of the major nutrients.<br><b>a.</b> If 15% of the body mass of a 70.0 kg adult consists of triacylglycerols, what is the total available fuel reserve, in both kilojoules and kilocalories, in the form of triacylglycerols? Recall that 1.00 kcal = 4.18 kJ.<br><b>b.</b> If the basal energy requirement is approximately 8,400 kJ/day (2,000 kcal/day), how long could this person survive if the oxidation of fatty acids stored as triacylglycerols were the only source of energy?<br><b>c.</b> What would be the weight loss in pounds per day under such starvation conditions (1 lb = 0.454 kg)?</p>',
    ko='<p>탄화수소 같은 지방산을 가진 트라이아실글리세롤은 주요 영양소 중 에너지 함량이 가장 높다.<br><b>a.</b> 체중 70.0 kg 성인의 15%가 트라이아실글리세롤이라면, 트라이아실글리세롤 형태의 총 연료 저장량은 몇 kJ, 몇 kcal인가? (1.00 kcal = 4.18 kJ)<br><b>b.</b> 기초 에너지 필요량이 하루 약 8,400 kJ(2,000 kcal)이고 저장 지방의 산화가 유일한 에너지원이라면, 이 사람은 얼마나 오래 살 수 있는가?<br><b>c.</b> 이런 굶주림 상태에서 하루 체중 감소는 몇 파운드인가? (1 lb = 0.454 kg)</p>',
    answer=chips('a. ≈ <b>4.0 × 10<sup>5</sup> kJ</b> ≈ <b>9.5 × 10<sup>4</sup> kcal</b>', 'b. 약 <b>48일</b>', 'c. 하루 약 0.22 kg ≈ <b>0.49 lb</b>'),
    explain=key('지방 1 g ≈ <b>38 kJ</b>(약 9 kcal)를 쓰면 나머지는 곱셈·나눗셈. (문제 27에서 주는 값과 같은 기준)') +
    steps('<b>a.</b> 지방량 = 70.0 kg × 0.15 = 10.5 kg = 10,500 g<br>에너지 = 10,500 g × 38 kJ/g = <span class="hl">4.0 × 10<sup>5</sup> kJ</span> ÷ 4.18 = <span class="hl">9.5 × 10<sup>4</sup> kcal</span>',
          '<b>b.</b> 4.0 × 10<sup>5</sup> kJ ÷ 8,400 kJ/day ≈ <span class="hl">48일</span>',
          '<b>c.</b> 하루 태우는 지방 = 8,400 kJ ÷ 38 kJ/g ≈ 221 g = 0.221 kg → ÷ 0.454 = <span class="hl">0.49 lb/day</span>') +
    fig(bars([('지방 저장 (10.5 kg)', 400, C['orange'], '≈ 400,000 kJ'), ('하루 필요량', 8.4, C['blue'], '8,400 kJ')], height=90), '저장량이 하루 필요량의 약 48배') +
    warn('실제로는 뇌가 포도당을 필요로 해 단백질도 분해되고, 지방을 100% 다 쓸 수도 없어서 이 계산은 “이론적 최대”야.', '참고'))

add(id='P7', num='7', en_title='Common Reaction Steps in the Fatty Acid Oxidation Cycle and Citric Acid Cycle', ko_title='β-산화와 시트르산 회로의 공통 반응 단계',
    slides='강의 슬라이드 24 · 16장', level=2,
    en='<p>Cells often use the same enzyme reaction pattern for analogous metabolic conversions. For example, the steps in the oxidation of pyruvate to acetyl-CoA and of α-ketoglutarate to succinyl-CoA, although catalyzed by different enzymes, are very similar. The first stage of fatty acid oxidation follows a reaction sequence closely resembling a sequence in the citric acid cycle. Use equations to show the analogous reaction sequences in the two pathways.</p>',
    ko='<p>세포는 비슷한 대사 전환에 같은 효소 반응 패턴을 자주 쓴다. 예를 들어 피루브산 → 아세틸-CoA와 α-KG → 숙시닐-CoA 산화는 효소는 다르지만 단계가 매우 비슷하다. 지방산 산화의 첫 단계는 시트르산 회로의 한 반응 순서와 매우 닮았다. 두 경로의 닮은 반응 순서를 반응식으로 보여라.</p>',
    answer=chips('β-산화 ①–③ = 회로 6–8단계: <b>FAD 산화 → 수화 → NAD<sup>+</sup> 산화</b>', '–CH<sub>2</sub>–CH<sub>2</sub>– → –CH=CH– → –CHOH–CH<sub>2</sub>– → –CO–CH<sub>2</sub>–'),
    explain=key('“단일결합 → 이중결합(FAD) → 물 붙이기 → 케톤(NAD<sup>+</sup>)”의 3단 콤보가 두 경로에 똑같이 나온다.') +
    table(['', 'β-산화', '시트르산 회로'], [
        ['① 탈수소 (FAD)', '아실-CoA → trans-Δ<sup>2</sup>-엔오일-CoA + FADH<sub>2</sub>', '숙신산 → 푸마르산 (trans 이중결합) + FADH<sub>2</sub>'],
        ['② 수화 (+H<sub>2</sub>O)', 'trans-Δ<sup>2</sup>-엔오일-CoA → L-3-하이드록시아실-CoA', '푸마르산 → L-말산'],
        ['③ 탈수소 (NAD<sup>+</sup>)', 'L-3-하이드록시아실-CoA → 3-케토아실-CoA + NADH', 'L-말산 → 옥살로아세트산 + NADH']], cls='left') +
    fig(beta_cycle(), 'β-산화 한 바퀴의 4단계 (①–③이 TCA 6–8단계와 같은 패턴)') +
    tip('C–C 단일결합은 NAD<sup>+</sup>로 산화하기엔 에너지가 부족해서 FAD를 쓰고(문제 21), C–OH → C=O는 NAD<sup>+</sup>로 충분해서 NAD<sup>+</sup>를 쓴다. 두 경로가 같은 “화학 논리”를 따르는 것.', '왜 같을까'))

add(id='P8', num='8', en_title='β Oxidation: How Many Cycles?', ko_title='β-산화: 몇 바퀴?',
    slides='강의 슬라이드 23–24, 28', level=1,
    en='<p>How many cycles of β oxidation are required for the complete oxidation of activated oleic acid, 18:1(Δ<sup>9</sup>)?</p>',
    ko='<p>활성화된 올레산 18:1(Δ<sup>9</sup>)을 완전히 산화하려면 β-산화가 몇 바퀴 필요한가?</p>',
    answer=chips('<b>8바퀴</b> → 아세틸-CoA 9개'),
    explain=key('탄소 18개 = 아세틸(C2) 9개. 마지막 바퀴에 C4가 아세틸 2개로 갈라지니 바퀴 수 = 9 − 1 = <b>8</b>.') +
    steps('18 ÷ 2 = 아세틸-CoA 9개.', '바퀴 수 = 9 − 1 = 8.',
          '이중결합(Δ<sup>9</sup>)은 바퀴 수를 바꾸지 않는다. 다만 4번째 바퀴 근처에서 이성질화효소 한 단계가 더 끼어들고, 그 바퀴에서는 ①단계(FAD)를 건너뛰어 FADH<sub>2</sub>가 1개 적다.') +
    fig(bars([('스테아르산 18:0', 8, C['blue'], '8바퀴, FADH₂ 8'), ('올레산 18:1', 8, C['orange'], '8바퀴, FADH₂ 7 (이성질화효소)')], height=90), '') +
    tip('그래서 불포화 지방산은 같은 길이 포화 지방산보다 ATP가 약간(1.5개) 적게 나와.', '포인트'))

add(id='P9', num='9', en_title='Chemistry of the Acyl-CoA Synthetase Reaction', ko_title='아실-CoA 합성효소 반응의 화학',
    slides='강의 슬라이드 19', level=2,
    en=f'''<p>Fatty acids are converted to their coenzyme A esters in a reversible reaction catalyzed by acyl-CoA synthetase:</p>{img('c17_p9a.png', '46%')}
<p><b>a.</b> The enzyme-bound intermediate in this reaction has been identified as the mixed anhydride of the fatty acid and adenosine monophosphate (AMP), acyl-AMP:</p>{img('c17_p9b.png', '26%')}
<p>Write two equations corresponding to the two steps of the reaction catalyzed by acyl-CoA synthetase.<br><b>b.</b> The acyl-CoA synthetase reaction is readily reversible, with an equilibrium constant near 1. How can this reaction be made to favor formation of fatty acyl–CoA?</p>''',
    ko='<p>지방산은 아실-CoA 합성효소가 촉매하는 가역 반응(R–COO<sup>−</sup> + ATP + CoA ⇌ R–CO–CoA + AMP + PP<sub>i</sub>)으로 CoA 에스터가 된다.<br><b>a.</b> 이 반응의 효소 결합 중간체는 지방산과 AMP의 혼합 산무수물인 아실-AMP로 밝혀졌다. 아실-CoA 합성효소가 촉매하는 두 단계 반응식을 써라.<br><b>b.</b> 이 반응은 평형상수가 1에 가까워 쉽게 역반응한다. 지방산아실-CoA 생성 쪽으로 반응을 치우치게 하려면 어떻게 하는가?</p>',
    answer=chips('① R–COO<sup>−</sup> + ATP → <b>아실-AMP</b> + PP<sub>i</sub>', '② 아실-AMP + CoA–SH → <b>아실-CoA</b> + AMP', 'b. <b>무기 피로인산가수분해효소</b>가 PP<sub>i</sub> → 2P<sub>i</sub> (ΔG′° −19.2) → 생성물 제거 → 정반응'),
    explain=key('13장 문제 24·25와 똑같은 반응! 첫 단계에서 ATP의 α-인산을 공격해 AMP가 붙고 PP<sub>i</sub>가 떨어진다.') +
    '<div class="twostep"><div><span>1단계</span>R–COO<sup>−</sup> + ATP → R–CO–AMP + PP<sub>i</sub><small>지방산 카복실산이 ATP의 α-인산 공격</small></div><div><span>2단계</span>R–CO–AMP + CoA–SH → R–CO–S–CoA + AMP<small>CoA의 –SH가 AMP를 밀어냄</small></div></div>' +
    align([('', 'R–COO<sup>−</sup> + ATP + CoA → 아실-CoA + AMP + PP<sub>i</sub>', '≈ 0'), ('', 'PP<sub>i</sub> + H<sub>2</sub>O → 2P<sub>i</sub>', '−19.2'),
           ('합', 'R–COO<sup>−</sup> + ATP + CoA + H<sub>2</sub>O → 아실-CoA + AMP + 2P<sub>i</sub>', '<span class="hl">≈ −19</span>')], cls='sum') +
    steps('PP<sub>i</sub>가 즉시 분해되어 사라지므로(르샤틀리에) 역반응이 불가능 → 활성화가 사실상 비가역.',
          'ATP → AMP는 고에너지 인산 결합 <b>2개</b>를 쓴 셈 → ATP 수지 계산에서 “활성화 = ATP 2개”로 센다(108 → 106).') +
    tip('스위치를 켠 뒤 다시 못 끄도록 스위치 손잡이(PP<sub>i</sub>)를 부러뜨리는 것.', '비유'))

add(id='P10', num='10', en_title='Intermediates in Oleic Acid Oxidation', ko_title='올레산 산화의 중간체',
    slides='강의 슬라이드 28', level=2,
    en='<p>What is the structure of the partially oxidized fatty acyl group that is formed when oleic acid, 18:1(Δ<sup>9</sup>), has undergone three cycles of β oxidation? What are the next two steps in the continued oxidation of this intermediate?</p>',
    ko='<p>올레산 18:1(Δ<sup>9</sup>)이 β-산화를 세 바퀴 돈 뒤 생기는 부분 산화된 지방산아실기의 구조는? 이 중간체를 계속 산화하는 다음 두 단계는?</p>',
    answer=chips('3바퀴 후: <b>cis-Δ<sup>3</sup>-도데센오일-CoA</b> (C12, 3번 탄소에 cis 이중결합)', '다음 ① <b>엔오일-CoA 이성질화효소</b>: cis-Δ<sup>3</sup> → trans-Δ<sup>2</sup>', '다음 ② <b>엔오일-CoA 수화효소</b>: → L-3-하이드록시도데칸오일-CoA'),
    explain=key('한 바퀴에 앞(카복실 쪽)에서 탄소 2개씩 떨어지므로 이중결합 번호가 바퀴마다 <b>2씩 줄어든다</b>: Δ<sup>9</sup> → Δ<sup>7</sup> → Δ<sup>5</sup> → Δ<sup>3</sup>.') +
    fig(flow(['18:1 cis-Δ⁹', '16:1 cis-Δ⁷', '14:1 cis-Δ⁵', '12:1 cis-Δ³'], arrow_labels=['1바퀴', '2바퀴', '3바퀴'], colors=[C['navy'], C['navy'], C['navy'], C['orange']]), '') +
    steps('3바퀴 후 C12, 이중결합이 C3–C4 사이(cis) = cis-Δ<sup>3</sup>-도데센오일-CoA. 구조: CH<sub>3</sub>(CH<sub>2</sub>)<sub>7</sub>–CH=CH–CH<sub>2</sub>–CO–S-CoA (cis).',
          '문제: β-산화 ①단계(아실-CoA 탈수소효소)는 C2=C3(trans) 이중결합을 만드는데, 이미 C3=C4 cis 이중결합이 있어 수화효소가 쓸 수 없다.',
          '<b>이성질화효소</b>가 이중결합을 C2=C3 trans로 옮김 → <b>수화효소</b>가 물을 붙여 L-3-하이드록시아실-CoA → 이후 정상 β-산화로 계속.') +
    tip('이 바퀴는 ①단계(FAD)를 건너뛰니 FADH<sub>2</sub> 하나를 못 얻는다(문제 8).', '연결'))

add(id='P11', num='11', en_title='β Oxidation of an Odd-Number Fatty Acid', ko_title='홀수 탄소 지방산의 β-산화',
    slides='강의 슬라이드 30', level=1,
    en='<p>What are the direct products of β oxidation of a fully saturated, straight-chain fatty acid of 11 carbons?</p>',
    ko='<p>탄소 11개의 완전 포화 직쇄 지방산을 β-산화하면 직접 생기는 산물은 무엇인가?</p>',
    answer=chips('<b>아세틸-CoA 4개 + 프로피오닐-CoA 1개</b>', '(4바퀴 동안 FADH<sub>2</sub> 4개, NADH 4개도 생김)'),
    explain=key('C2씩 떼다 보면 마지막에 <b>C3</b>(프로피오닐-CoA)가 남는다: 11 = 2+2+2+2+3.') +
    steps('11 − 2×4 = 3 → 4바퀴 후 프로피오닐-CoA(C3) 남음.', '산물: 아세틸-CoA 4, 프로피오닐-CoA 1, FADH<sub>2</sub> 4, NADH 4.',
          '프로피오닐-CoA → (비오틴) → 메틸말로닐-CoA → (B<sub>12</sub>) → 숙시닐-CoA → 시트르산 회로.') +
    fig(odd_chain(), '프로피오닐-CoA의 운명: 숙시닐-CoA로 들어가 포도당도 될 수 있다') +
    tip('홀수 지방산은 소·양 같은 반추동물의 지방이나 일부 식물에 있어. 사람 식사에서는 드물어.', '참고'))

add(id='P14', num='14', en_title='Fatty Acids as a Source of Water', ko_title='물의 공급원으로서의 지방산',
    slides='강의 슬라이드 4–5, 27', level=2,
    en='<p>Contrary to legend, camels do not store water in their humps, which actually consist of large fat deposits. How can these fat deposits serve as a source of water? Calculate the amount of water (in liters) that a camel can produce from 1.0 kg of fat. Assume for simplicity that the fat consists entirely of tripalmitoylglycerol.</p>',
    ko='<p>전설과 달리 낙타는 혹에 물을 저장하지 않는다. 혹은 사실 커다란 지방 덩어리다. 이 지방이 어떻게 물의 공급원이 될 수 있는가? 낙타가 지방 1.0 kg으로 만들 수 있는 물의 양(L)을 계산하라. 단순화를 위해 지방은 모두 트라이팔미토일글리세롤이라고 가정한다.</p>',
    answer=chips('지방이 산화되면 H 원자가 O<sub>2</sub>와 만나 <b>대사수(H<sub>2</sub>O)</b>가 생긴다', '1.0 kg → 약 <b>1.1 L</b>의 물'),
    explain=key('연소 반응식만 맞추면 끝. 탄소는 CO<sub>2</sub>, 수소는 H<sub>2</sub>O로.') +
    steps('트라이팔미토일글리세롤 = C<sub>51</sub>H<sub>98</sub>O<sub>6</sub>, 분자량 ≈ 807 g/mol',
          eq('C<sub>51</sub>H<sub>98</sub>O<sub>6</sub> + 72.5 O<sub>2</sub> → 51 CO<sub>2</sub> + <b>49 H<sub>2</sub>O</b>'),
          '1.0 kg ÷ 807 g/mol = 1.24 mol → 물 1.24 × 49 = 60.7 mol × 18 g/mol ≈ 1,090 g ≈ <span class="hl">1.1 L</span>') +
    tip('지방 무게보다 물이 더 많이 나온다! (산소의 무게가 보태지기 때문). 단, 숨 쉴 때 날아가는 수분도 있어서 실제 “이득”은 이보다 작아.', '재미'))

add(id='P16', num='16', en_title='Fatty Acid Oxidation in Uncontrolled Diabetes', ko_title='조절되지 않는 당뇨에서의 지방산 산화',
    slides='강의 슬라이드 41–44', level=1,
    en='<p>When the acetyl-CoA produced during β oxidation in the liver exceeds the capacity of the citric acid cycle, the excess acetyl-CoA forms ketone bodies — acetone, acetoacetate, and <span class="sc">D</span>-β-hydroxybutyrate. This occurs in people with severe, uncontrolled diabetes; because their tissues cannot use glucose, they oxidize large amounts of fatty acids instead. Although acetyl-CoA is not toxic, the mitochondrion must divert the acetyl-CoA to ketone bodies. What problem would arise if acetyl-CoA were not converted to ketone bodies? How does the diversion to ketone bodies solve the problem?</p>',
    ko='<p>간의 β-산화로 생긴 아세틸-CoA가 시트르산 회로의 처리 능력을 넘으면, 남는 아세틸-CoA는 케톤체(아세톤, 아세토아세트산, D-β-하이드록시뷰티르산)가 된다. 심한 비조절 당뇨에서 이런 일이 생긴다(조직이 포도당을 못 써서 지방산을 대량 산화). 아세틸-CoA 자체는 독성이 없지만 미토콘드리아는 이를 케톤체로 돌려야 한다. 아세틸-CoA가 케톤체로 바뀌지 않으면 어떤 문제가 생기는가? 케톤체로 돌리는 것이 어떻게 문제를 해결하는가?</p>',
    answer=chips('문제: CoA가 전부 <b>아세틸-CoA로 묶여</b> 자유 CoA 고갈 → β-산화(티올레이스·활성화)가 멈춤', '해결: 케톤체 합성이 <b>CoA를 풀어 줌</b> → β-산화 계속 + 케톤체는 다른 조직의 연료로 수출'),
    explain=key('CoA는 양이 한정된 “바구니”. 바구니가 전부 아세틸기로 차 있으면 새 짐(β-산화)을 담을 수 없다.') +
    fig(flow(['2 아세틸-CoA', '아세토아세틸-CoA', 'HMG-CoA', '아세토아세트산 + CoA 해방'], arrow_labels=['티올레이스 (−CoA)', '+아세틸-CoA (−CoA)', 'HMG-CoA 분해효소'], colors=[C['navy'], C['navy'], C['navy'], C['green']]), '케톤체가 만들어지는 동안 CoA가 풀려난다') +
    steps('당뇨·공복 간: OAA가 당신생으로 빠져 아세틸-CoA가 회로에 못 들어감 → 아세틸-CoA가 쌓인다.',
          'CoA가 계속 아세틸-CoA에 묶이면 자유 CoA ↓ → β-산화 ④(티올레이스)와 지방산 활성화가 멈춤 → 간이 에너지(ATP)도 못 얻는다.',
          '케톤체로 바꾸면 CoA가 풀려 β-산화가 계속되고, 케톤체는 혈액으로 나가 심장·근육·뇌의 연료가 된다. 단, 너무 많으면 산성 → 케톤산증.') +
    tip('16장 문제 20(OAA 고갈), 15장 문제 9(인슐린 부족 → 케톤체 ↑)와 같은 이야기의 마지막 퍼즐.', '연결'))

add(id='P17', num='17', en_title='Consequences of a High-Fat Diet with No Carbohydrates', ko_title='탄수화물 없는 고지방 식사의 결과',
    slides='강의 슬라이드 30, 44–45', level=2,
    en='<p>Suppose you had to subsist on a diet of whale blubber and seal blubber, with little or no carbohydrate.<br><b>a.</b> What would be the effect of carbohydrate deprivation on the utilization of fats for energy?<br><b>b.</b> If your diet were totally devoid of carbohydrate, would it be better to consume odd- or even-number fatty acids? Explain.</p>',
    ko='<p>고래·물범 지방만 먹고 탄수화물은 거의 없이 살아야 한다고 하자.<br><b>a.</b> 탄수화물 결핍은 지방을 에너지로 쓰는 데 어떤 영향을 주는가?<br><b>b.</b> 식단에 탄수화물이 전혀 없다면, 홀수와 짝수 지방산 중 어느 쪽을 먹는 게 나은가? 설명하라.</p>',
    answer=chips('a. OAA가 부족해(당신생에 쓰임) 아세틸-CoA가 회로에 다 못 들어감 → <b>케톤체 ↑(케톤증)</b>, 지방이 완전히 산화되지 못함', 'b. <b>홀수</b> 지방산 — 프로피오닐-CoA → 숙시닐-CoA → OAA → <b>포도당</b>을 만들 수 있다'),
    explain=key('“지방은 탄수화물의 불꽃 속에서 탄다.” 아세틸-CoA를 태우려면 OAA가 필요한데, OAA는 탄수화물(피루브산)에서 보충된다.') +
    steps('<b>a.</b> 탄수화물이 없으면 혈당 유지를 위해 간이 OAA를 당신생으로 쓴다 → 회로의 OAA ↓ → 아세틸-CoA가 시트르산이 되지 못하고 케톤체로. 뇌는 케톤체에 적응하지만, 포도당이 꼭 필요한 조직(적혈구 등)을 위해 근육 단백질도 분해된다.',
          '<b>b.</b> 짝수 지방산 → 아세틸-CoA만 → 알짜 포도당 0. 홀수 지방산 → 마지막 프로피오닐-CoA → 숙시닐-CoA → OAA: 회로를 보충하고 당신생 원료가 된다 → 케톤증 ↓, 근육 단백질 보존.') +
    fig(odd_chain(), '홀수 지방산의 끝 3탄소 = 포도당이 될 수 있는 유일한 지방산 조각') +
    tip('이누이트 전통 식단이 고지방인데도 큰 문제가 없었던 데엔 단백질(아미노산 → 당신생)이 충분했던 영향이 커.', '참고'))

add(id='P18', num='18', en_title='Even- and Odd-Number Fatty Acids in the Diet', ko_title='식단 속 짝수·홀수 지방산',
    slides='강의 슬라이드 30', level=2,
    en='<p>In a laboratory experiment, investigators feed two groups of rats two different fatty acids as their sole source of carbon for a month. The first group gets heptanoic acid (7:0), and the second gets octanoic acid (8:0). After the experiment, those in the first group are healthy and have gained weight, whereas those in the second group are weak and have lost weight as a result of losing muscle mass. What is the biochemical basis for this difference?</p>',
    ko='<p>실험에서 두 무리의 쥐에게 한 달 동안 서로 다른 지방산을 유일한 탄소원으로 먹였다. 첫 무리는 헵탄산(7:0), 둘째 무리는 옥탄산(8:0)을 먹었다. 실험 후 첫 무리는 건강하고 체중이 늘었지만, 둘째 무리는 근육이 빠져 약해지고 체중이 줄었다. 이 차이의 생화학적 기초는?</p>',
    answer=chips('헵탄산(7:0) → 아세틸-CoA 2 + <b>프로피오닐-CoA 1</b> → 숙시닐-CoA → <b>포도당 합성 가능</b>', '옥탄산(8:0) → 아세틸-CoA 4뿐 → 포도당 <b>못 만듦</b> → 근육 단백질을 분해해 당신생'),
    explain=key('탄소원이 오직 지방산뿐일 때, <b>포도당을 만들 수 있느냐</b>가 생사를 가른다.') +
    table(['', '헵탄산 7:0 (홀수)', '옥탄산 8:0 (짝수)'], [['β-산화 산물', '아세틸-CoA 2 + 프로피오닐-CoA 1', '아세틸-CoA 4'],
                                                        ['포도당 원료?', '○ 프로피오닐 → 숙시닐-CoA → OAA', '✕ (14장 문제 25)'],
                                                        ['뇌·적혈구용 포도당', '지방산에서 공급', '<b>근육 단백질</b> 분해로 공급'],
                                                        ['결과', '건강, 체중 증가', '근육 소실, 쇠약']], cls='left') +
    fig(odd_chain(), '') +
    tip('16장 문제 19: 아세틸-CoA는 회로에서 C2 들어가고 CO<sub>2</sub> 2개 나가서 OAA를 알짜로 늘리지 못한다. 홀수 지방산만 예외.', '연결'))

add(id='P19', num='19', en_title='Metabolic Consequences of Ingesting ω-Fluorooleate', ko_title='ω-플루오로올레산을 먹었을 때의 대사 결과',
    slides='강의 슬라이드 24 · 16장 아코니테이스', level=2,
    en=f'''<p>The shrub <i>Dichapetalum toxicarium</i>, native to Sierra Leone, produces ω-fluorooleate, which is highly toxic to warm-blooded animals.</p>{img('c17_p19.png', '40%')}
<p>This substance has been used as an arrow poison, and powdered fruit from the plant is sometimes used as a rat poison (hence the plant’s common name, ratsbane). Why is this substance so toxic? (Hint: Review Chapter 16, Problem 21.)</p>''',
    ko='<p>시에라리온 자생 관목 <i>Dichapetalum toxicarium</i>은 온혈동물에게 매우 독한 ω-플루오로올레산(F–CH<sub>2</sub>–(CH<sub>2</sub>)<sub>7</sub>–CH=CH–(CH<sub>2</sub>)<sub>7</sub>–COO<sup>−</sup>)을 만든다. 화살 독으로 쓰였고, 열매 가루는 쥐약으로도 쓰인다. 이 물질은 왜 이렇게 독한가? (힌트: 16장 문제 21)</p>',
    answer=chips('β-산화가 카복실 끝부터 C2씩 떼다가 <b>마지막에 플루오로아세틸-CoA</b>가 나옴', '→ 시트르산 생성효소가 <b>플루오로시트르산</b>을 만듦 → <b>아코니테이스 억제</b>', '→ 시트르산 회로 정지 → ATP 생산 붕괴 → 치명적'),
    explain=key('“치명적 합성(lethal synthesis)”: 독 자체가 아니라 몸이 그걸 대사해 만든 산물이 효소를 막는다.') +
    fig(flow(['ω-플루오로올레산 (C18)', '플루오로아세틸-CoA', '플루오로시트르산', '✕ 아코니테이스'], arrow_labels=['β-산화 8바퀴', '시트르산 생성효소', '억제'], colors=[C['navy'], C['orange'], C['red'], C['red']]), '') +
    steps('C18 짝수 지방산 → β-산화로 아세틸-CoA 단위로 잘림. F가 붙은 맨 끝(ω) 탄소 2개는 마지막에 <b>플루오로아세틸-CoA</b>로 나온다.',
          '플루오로아세틸-CoA는 아세틸-CoA와 비슷해 시트르산 생성효소가 OAA와 붙여 플루오로시트르산을 만든다.',
          '플루오로시트르산은 아코니테이스를 강하게 억제 → 시트르산이 쌓이고 회로 정지 → 심장·뇌처럼 에너지를 많이 쓰는 기관부터 멈춘다.') +
    tip('쥐약 “1080”(플루오로아세트산 나트륨)과 같은 원리야. 지방산 형태라 지방 대사를 따라 몸속 깊이 퍼진다.', '연결'))

add(id='P20', num='20', en_title='Mutant Acetyl-CoA Carboxylase', ko_title='돌연변이 아세틸-CoA 카복실화효소',
    slides='강의 슬라이드 32–34', level=2,
    en='<p>What would be the consequences for fat metabolism of a mutation in acetyl-CoA carboxylase that replaced the Ser residue normally phosphorylated by AMPK with an Ala residue? What might happen if the same Ser were replaced by Asp? (Hint: Compare the structures of phosphoserine, alanine, aspartate; see Fig. 17-13.)</p>',
    ko='<p>AMPK가 보통 인산화하는 아세틸-CoA 카복실화효소(ACC)의 Ser 잔기가 Ala로 바뀐 돌연변이는 지방 대사에 어떤 결과를 낳는가? 같은 Ser이 Asp로 바뀌면 어떻게 될까? (힌트: 포스포세린, 알라닌, 아스파르트산의 구조 비교, 그림 17-13)</p>',
    answer=chips('<b>Ser → Ala</b>: 인산화 불가 → ACC <b>항상 활성</b> → 말로닐-CoA ↑ → CAT I 억제 → 지방산 산화 ↓ (에너지 부족해도), 합성 ↑', '<b>Ser → Asp</b>: Asp의 음전하가 포스포세린 흉내 → ACC <b>항상 억제</b> → 말로닐-CoA ↓ → 지방산 산화 ↑, 합성 ↓'),
    explain=key('AMPK가 Ser에 인산(음전하)을 붙이면 ACC가 <b>꺼진다</b>. Ala = 인산을 못 받음(항상 켜짐), Asp = 이미 음전하(항상 꺼진 척).') +
    table(['잔기', '곁사슬', 'ACC 상태'], [['Ser–P (정상, 인산화)', '–CH<sub>2</sub>–O–PO<sub>3</sub><sup>2−</sup> (음전하)', '불활성'],
                                       ['Ala', '–CH<sub>3</sub> (–OH 없음 → 인산화 불가)', '<b>항상 활성</b>'],
                                       ['Asp', '–CH<sub>2</sub>–COO<sup>−</sup> (음전하 → 인산 흉내)', '<b>항상 불활성</b>']], cls='left') +
    fig(flow(['AMPK (에너지 부족)', 'ACC–P (꺼짐)', '말로닐-CoA ↓', 'CAT I 열림 → β-산화 ↑'], colors=[C['orange'], C['gray'], C['navy'], C['green']], box_h=44), '정상 조절 경로') +
    tip('실험실에서 인산화 효과를 흉내 낼 때 Ser → Asp/Glu(“인산 모방”), 막을 때 Ser → Ala 돌연변이를 실제로 많이 써.', '연구 팁'))

add(id='P21', num='21', en_title='Role of FAD as Electron Acceptor', ko_title='전자 수용체로서 FAD의 역할',
    slides='강의 슬라이드 24 · 13장 환원 전위', level=2,
    en='<p>Acyl-CoA dehydrogenase uses enzyme-bound FAD as a prosthetic group to dehydrogenate the α and β carbons of fatty acyl–CoA. What is the advantage of using FAD as an electron acceptor rather than NAD<sup>+</sup>? Explain in terms of the standard reduction potentials for the Enz-FAD/FADH<sub>2</sub> (E′° = −0.219 V) and NAD<sup>+</sup>/NADH (E′° = −0.320 V) half-reactions.</p>',
    ko='<p>아실-CoA 탈수소효소는 효소에 결합한 FAD를 보결분자단으로 써서 지방산아실-CoA의 α·β 탄소를 탈수소화한다. 전자 수용체로 NAD<sup>+</sup> 대신 FAD를 쓰는 장점은? Enz-FAD/FADH<sub>2</sub>(E′° = −0.219 V)와 NAD<sup>+</sup>/NADH(E′° = −0.320 V)의 표준 환원 전위로 설명하라.</p>',
    answer=chips('FAD의 E′°가 <b>더 양수</b>(−0.219 &gt; −0.320) = 전자를 더 잘 받는 <b>강한 산화제</b>', 'ΔE′°가 0.101 V 더 커져 ΔG′°가 약 <b>−19.5 kJ/mol 더 유리</b>', '→ C–C 단일결합을 C=C로 만드는 “어려운” 산화를 진행시킬 수 있다'),
    explain=key('13장 공식: ΔG′° = −nFΔE′°. 받는 쪽 E′°가 높을수록 ΔE′°가 커지고 ΔG′°가 더 음수.') +
    fig(ladder([('FAD/FADH₂ (효소 결합)', -0.219), ('NAD⁺/NADH', -0.320)], -0.35, -0.19, hl=('FAD/FADH₂ (효소 결합)',), height=150), 'FAD가 NAD⁺보다 위(더 +) → 전자를 더 세게 끌어당긴다') +
    steps('아실-CoA → 엔오일-CoA (–CH<sub>2</sub>–CH<sub>2</sub>– → –CH=CH–)는 알코올 → 케톤보다 전자를 떼기 어려운 반응(기질 짝의 E′°가 상대적으로 높다).',
          '받는 쪽을 NAD<sup>+</sup>로 하면 ΔE′°가 너무 작거나 음수가 되어 진행이 불리.',
          'FAD로 바꾸면 ΔE′°가 0.320 − 0.219 = 0.101 V 커짐 → ΔG′° 차이 = −2 × 96.48 × 0.101 ≈ <span class="hl">−19.5 kJ/mol</span> 더 유리.') +
    tip('대가: FADH<sub>2</sub>는 NADH보다 ATP를 적게(1.5 vs 2.5) 만든다. “더 확실히 진행”과 “ATP 조금 덜”을 맞바꾼 것. 숙신산 탈수소효소(16장)도 같은 이유로 FAD를 쓴다.', '연결'))

add(id='P22', num='22', en_title='β Oxidation of Arachidic Acid', ko_title='아라키드산의 β-산화',
    slides='강의 슬라이드 23–24', level=1,
    en='<p>How many turns of the fatty acid oxidation cycle are required for complete oxidation of arachidic acid (20:0) to acetyl-CoA?</p>',
    ko='<p>아라키드산(20:0)을 아세틸-CoA로 완전히 산화하려면 지방산 산화 회로를 몇 바퀴 돌아야 하는가?</p>',
    answer=chips('<b>9바퀴</b> → 아세틸-CoA 10개'),
    explain=key('짝수 지방산 C<sub>n</sub> → 바퀴 수 = n/2 − 1.') +
    steps('20 ÷ 2 = 아세틸-CoA 10개.', '마지막 바퀴(C4 → 아세틸-CoA 2개) 때문에 바퀴 수 = 10 − 1 = <span class="hl">9</span>.',
          '덤: FADH<sub>2</sub> 9 + NADH 9 + 아세틸-CoA 10 → 9×1.5 + 9×2.5 + 10×10 = <b>136 ATP</b> (아라키도일-CoA 기준).') +
    fig(beta_cycle(), '한 바퀴 = 4단계, 탄소 2개 제거') +
    tip('C20 이상의 아주 긴 사슬은 먼저 <b>퍼옥시좀</b>에서 짧게 줄인 뒤 미토콘드리아로 넘어가기도 해(슬라이드 37).', '연결'))

add(id='P25', num='25', en_title='Sources of H₂O Produced in β Oxidation', ko_title='β-산화에서 생기는 물의 출처',
    slides='강의 슬라이드 27', level=2,
    en='''<p>The complete oxidation of palmitoyl-CoA to carbon dioxide and water is represented by the overall equation</p>
<p class="c">Palmitoyl-CoA + 23O<sub>2</sub> + 108P<sub>i</sub> + 108ADP → CoA + 16CO<sub>2</sub> + 108ATP + 23H<sub>2</sub>O</p>
<p>Water also forms in the reaction ADP + P<sub>i</sub> → ATP + H<sub>2</sub>O but is not included as a product in the overall equation. Why?</p>''',
    ko='<p>팔미토일-CoA가 CO<sub>2</sub>와 물로 완전히 산화되는 전체 반응식은 위와 같다. ADP + P<sub>i</sub> → ATP + H<sub>2</sub>O 반응에서도 물이 생기지만 전체 반응식의 생성물에는 포함되지 않았다. 왜 그런가?</p>',
    answer=chips('ATP 합성으로 생긴 물(108개)은 그 ATP가 <b>쓰일 때(가수분해) 다시 소비</b>된다 → 순환하므로 알짜 0', '23 H<sub>2</sub>O만이 연료의 H가 <b>O<sub>2</sub>로 산화</b>되어 생긴 진짜 “대사수”', '(또 생화학 반응식에서 물은 용매라 보통 생략)'),
    explain=key('ATP ⇄ ADP + P<sub>i</sub>는 계속 도는 <b>순환</b>. 만들 때 물 1개 나오고, 쓸 때 물 1개 들어간다.') +
    fig(flow(['ADP + Pᵢ', 'ATP + H₂O', '일(근육·합성) 후 ADP + Pᵢ'], arrow_labels=['ATP 합성 (+H₂O)', 'ATP 가수분해 (−H₂O)'], colors=[C['navy'], C['orange'], C['navy']], box_h=44), '물이 나왔다가 다시 들어가 알짜 0') +
    steps('전자전달계: NADH·FADH<sub>2</sub>의 전자 + O<sub>2</sub> → H<sub>2</sub>O. 23 O<sub>2</sub> → 23 H<sub>2</sub>O (β-산화 7 + TCA 16). 이것이 연료에서 나온 진짜 물.',
          'ATP 합성의 물 108개는 그 ATP를 세포가 써서 ADP + P<sub>i</sub>로 되돌릴 때 정확히 소비된다 → 정상 상태에서 알짜 생성 없음.',
          '그래서 낙타(문제 14)의 “대사수” 계산에도 ATP 합성의 물은 넣지 않는다.') +
    tip('돈(물)을 은행에 넣었다(ATP 합성) 바로 꺼내 쓰면(ATP 사용) 잔고는 그대로야.', '비유'))

add(id='P26', num='26', en_title='Biological Importance of Cobalt', ko_title='코발트의 생물학적 중요성',
    slides='강의 슬라이드 30', level=2,
    en='<p>Cattle, deer, sheep, and other ruminant animals produce large amounts of propionate in the rumen through the bacterial fermentation of ingested plant matter. Propionate is the principal source of glucose for these animals, via the route propionate → oxaloacetate → glucose. In some areas of the world, notably Australia, ruminant animals sometimes show symptoms of anemia with concomitant loss of appetite and retarded growth, resulting from an inability to transform propionate to oxaloacetate. This condition is due to a cobalt deficiency caused by very low cobalt levels in the soil and thus in plant matter. Explain.</p>',
    ko='<p>소·사슴·양 같은 반추동물은 먹은 식물을 반추위의 세균이 발효시켜 프로피온산을 대량으로 만든다. 프로피온산 → 옥살로아세트산 → 포도당 경로로, 프로피온산은 이 동물들의 주된 포도당 원료다. 호주 등 일부 지역에서는 반추동물이 프로피온산을 옥살로아세트산으로 바꾸지 못해 빈혈, 식욕 부진, 성장 지연을 보인다. 이는 토양과 식물의 코발트가 매우 적어 생기는 코발트 결핍 때문이다. 설명하라.</p>',
    answer=chips('코발트 = <b>비타민 B<sub>12</sub>(코발라민)</b>의 중심 금속', 'B<sub>12</sub>는 <b>메틸말로닐-CoA 뮤테이스</b>의 조효소 → 결핍 시 프로피오닐-CoA → 숙시닐-CoA가 막힘 → 포도당 부족(식욕↓·성장 지연)', 'B<sub>12</sub>는 DNA 합성(엽산 대사)에도 필요 → 적혈구 생성 장애 → <b>빈혈</b>'),
    explain=key('코발트 → B<sub>12</sub> → 메틸말로닐-CoA 뮤테이스. 사슬 하나만 끊겨도 반추동물의 포도당 공급로 전체가 멈춘다.') +
    fig(odd_chain(), '세 번째 화살표(뮤테이스, B₁₂)가 코발트 결핍으로 막힌다') +
    steps('반추위 세균은 B<sub>12</sub>를 만들 수 있지만, 그 재료인 코발트가 흙·풀에 없으면 B<sub>12</sub>도 못 만든다.',
          '메틸말로닐-CoA 뮤테이스(B<sub>12</sub> 필요)가 멈추면 L-메틸말로닐-CoA가 쌓이고 숙시닐-CoA → OAA → 포도당이 안 됨 → 에너지 부족, 식욕 부진, 성장 지연.',
          'B<sub>12</sub>는 메싸이오닌 합성효소에도 필요해, 부족하면 DNA 합성이 느려져 적혈구를 못 만든다(거대적아구성 빈혈).') +
    tip('사람도 B<sub>12</sub>가 부족하면 소변에 메틸말로닐산이 나온다 → B<sub>12</sub> 결핍 진단 지표(슬라이드 30).', '임상'))

add(id='P27', num='27', en_title='Fat Loss during Hibernation', ko_title='겨울잠 동안의 지방 감소',
    slides='강의 슬라이드 1, 44', level=2,
    en='<p>Bears expend about 25 × 10<sup>6</sup> J/day during periods of hibernation, which may last as long as seven months. The energy required to sustain life is obtained from fatty acid oxidation. How much weight (in kilograms) do bears lose after 7 months of hibernation? How could a bear’s body minimize ketosis during hibernation? (Assume the oxidation of fat yields 38 kJ/g.)</p>',
    ko='<p>곰은 겨울잠 동안 하루 약 25 × 10<sup>6</sup> J을 쓰고, 겨울잠은 7개월까지 이어질 수 있다. 생명 유지에 필요한 에너지는 지방산 산화로 얻는다. 7개월 겨울잠 후 곰의 체중은 몇 kg 줄어드는가? 겨울잠 동안 곰의 몸은 어떻게 케톤증을 최소화할 수 있는가? (지방 산화 = 38 kJ/g)</p>',
    answer=chips('약 <b>140 kg</b> 감소 (7개월 ≈ 210일 기준 138 kg)', '케톤증 최소화: 지방의 <b>글리세롤</b>을 당신생에 써서 포도당·OAA 공급 → 아세틸-CoA가 회로에서 완전 산화되도록'),
    explain=steps('하루: 25 × 10<sup>6</sup> J = 25,000 kJ → 지방 25,000 ÷ 38 ≈ 658 g/day',
                  '7개월 ≈ 210일: 658 g × 210 ≈ 138,000 g ≈ <span class="hl">138 kg</span>',
                  '<b>케톤증 줄이기</b>: TG 분해로 나오는 글리세롤 → DHAP → 당신생 → 포도당(뇌 연료) + OAA 보충 → 아세틸-CoA가 케톤체 대신 시트르산 회로로. 또 곰은 요소를 재활용해 단백질 분해를 최소화하고 대사율을 크게 낮춘다.') +
    fig(bars([('하루 지방 소비', 0.658, C['orange'], '≈ 0.66 kg/day'), ('7개월 합계', 138, C['red'], '≈ 138 kg')], height=90, vmax=140), '') +
    key('지방 1 g = 38 kJ. 하루 에너지 ÷ 38 = 하루 지방 소비량. 그다음 날수를 곱한다.') +
    tip('곰은 겨울잠 전에 하루 2만 kcal 이상 먹어서 지방을 잔뜩 저장해 둔다(슬라이드 1).', '재미'))

for _n in ('12', '13', '15', '23', '24'):
    ALL_ITEMS.append(dict(id='P' + _n, num=_n, level=3, kind='PROBLEM'))
ALL_ITEMS.sort(key=lambda i: int(i['num']))
