# -*- coding: utf-8 -*-
"""Chapter 15 — Principles of Metabolic Regulation (glycolysis/gluconeogenesis, glycogen)"""
from helpers import *

CHAPTER = '15'
CH_TITLE = '대사 조절의 원리'
CH_EN = 'Principles of Metabolic Regulation'
STAT = ('3', '핵심 호르몬 (인슐린·글루카곤·에피네프린)')
SCOPE = ('교수님 15장 강의(슬라이드 1–77) 범위 = <b>15.1 대사 경로의 조절</b>, <b>15.2 대사 조절의 분석</b>, <b>15.3 해당과정·당신생의 조절</b>, '
         '<b>15.4 글리코겐 대사</b>, <b>15.5 글리코겐 합성·분해의 조절</b> — 15장 전체. 15장에는 본문 예제가 없어.')
INCLUDE = ['<b>글리코겐 분해·에너지</b> — 문제 1, 2, 3',
           '<b>글리코겐 인산화효소 조절</b> — 문제 4, 10',
           '<b>근육 대사 조절 비교</b> — 문제 6',
           '<b>호르몬(인슐린·글루카곤) 조절</b> — 문제 9, 11']
EXCLUDE = ['<b>문제 13</b> — DATA ANALYSIS PROBLEM']

ALL_ITEMS = []


def add(**kw):
    kw.setdefault('section', '연습문제')
    kw.setdefault('kind', 'PROBLEM')
    ALL_ITEMS.append(kw)


def cascade():
    W, H = 520, 270
    items = [('에피네프린 / 글루카곤', C['red']), ('수용체 → G 단백질 → 아데닐산 고리화효소', C['ink']), ('cAMP ↑', C['orange']),
             ('PKA 활성화', C['orange']), ('인산화효소 b 키나아제 (인산화 → 활성)', C['orange']), ('글리코겐 인산화효소 b → a (활성)', C['green']),
             ('글리코겐 → 포도당 1-인산', C['green'])]
    b = arrowdef('ca', C['gray'])
    for i, (t, col) in enumerate(items):
        y = 6 + i * 38
        w = 330
        b += f'<rect x="{(W-w)/2}" y="{y}" width="{w}" height="26" rx="7" fill="white" stroke="{col}" stroke-width="2"/>' + T(W / 2, y + 17, t, 11, col, weight=700)
        if i < len(items) - 1:
            b += f'<line x1="{W/2}" y1="{y+27}" x2="{W/2}" y2="{y+36}" stroke="{C["gray"]}" stroke-width="1.6" marker-end="url(#ca)"/>'
    b += T(W / 2 + 175, 90, '단계마다', 10.5, C['red'], 'start', 700) + T(W / 2 + 175, 104, '신호 증폭 ×10~100', 10.5, C['red'], 'start', 700)
    return svg(W, H, b)


def front_pages():
    t1 = table(['단계', '해당과정 효소 (+ 활성 / − 억제)', '당신생 효소 (+ 활성 / − 억제)'], [
        ['1', '<b>헥소키나아제</b>: − G6P (근육형) / 간 HK IV: 조절 단백질이 핵에 붙잡음', '<b>G6Pase</b>: 전사 조절 (FOXO1 ↑)'],
        ['3', '<b>PFK-1</b>: + AMP, ADP, <b>과당 2,6-이인산</b> / − ATP, 시트르산', '<b>FBPase-1</b>: − AMP, <b>과당 2,6-이인산</b>'],
        ['10', '<b>피루브산 키나아제</b>: + F1,6BP / − ATP, 아세틸-CoA, 알라닌, 긴사슬 지방산, (간형) 글루카곤 → 인산화로 불활성',
         '<b>피루브산 카복실화효소</b>: + 아세틸-CoA<br><b>PEPCK</b>: 전사 조절 (글루카곤 ↑, 인슐린 ↓)']], cls='left')
    p1 = f'''<h2 class="pt"><span class="n">MAP</span> 해당과정 ⇄ 당신생: 상반(reciprocal) 조절 한눈에</h2>
<p class="lead">같은 신호가 한쪽은 켜고 다른 쪽은 끈다 → 두 경로가 동시에 돌아 ATP만 버리는 <b>헛된 회로</b>를 막는다.</p>
<div class="card">{t1}</div>
<div class="grid3" style="margin-top:3mm">
 <div class="card"><h4><span class="no">1</span> 과당 2,6-이인산 (F2,6BP)</h4><p>PFK-1 ↑ · FBPase-1 ↓ 의 “스위치”. PFK-2/FBPase-2(한 단백질, 두 활성)가 만들고 없앤다.</p>
  <p><b>인슐린</b> → PFK-2 활성 → F2,6BP ↑ → 해당과정 ↑<br><b>글루카곤</b> → cAMP → PKA → FBPase-2 활성 → F2,6BP ↓ → 당신생 ↑</p></div>
 <div class="card"><h4><span class="no">2</span> 에너지 신호</h4><p><b>ATP ↑, 시트르산 ↑</b> = 에너지 넉넉 → 해당과정 ↓</p><p><b>AMP ↑</b> = 에너지 부족 → 해당과정 ↑, 당신생 ↓ (AMPK도 활성)</p>
  <p class="small">아데닐산 키나아제: 2ADP ⇌ ATP + AMP → ATP가 조금만 줄어도 AMP는 크게 늘어 민감한 신호가 된다.</p></div>
 <div class="card"><h4><span class="no">3</span> 조절 지점의 조건</h4><p>세포 속에서 <b>평형에서 먼 반응</b>(ΔG ≪ 0)이 조절 지점: HK·PFK-1·PK.</p>
  <p>평형 근처 반응은 효소량을 바꿔도 흐름이 거의 안 바뀐다(양방향).</p>
  <p class="small">15.2: 플럭스 조절 계수 C, 탄력성 ε, 반응 계수 R = C·ε</p></div>
</div>'''
    t2 = table(['', '인슐린 (혈당 ↑)', '글루카곤 (혈당 ↓, 간)', '에피네프린 (위기, 근육·간)'], [
        ['신호', '인슐린 수용체 → PKB(Akt)', 'cAMP → PKA', 'cAMP → PKA (+ 간: Ca<sup>2+</sup>)'],
        ['글리코겐 인산화효소', '↓ (PP1 활성 → b형)', '↑ (a형)', '↑ (a형)'],
        ['글리코겐 합성효소', '↑ (GSK3 억제, PP1 → a형)', '↓ (인산화 → b형)', '↓'],
        ['해당과정 (간)', '↑ (F2,6BP ↑)', '↓ (F2,6BP ↓, PK-L 인산화)', '근육: ↑'],
        ['당신생 (간)', '↓', '↑', '↑'],
        ['포도당 흡수', 'GLUT4 → 근육·지방 ↑', '—', '—']], cls='left')
    p2 = f'''<h2 class="pt"><span class="n">KIT</span> 글리코겐 대사와 호르몬 조절 핵심 정리</h2>
<div class="grid2">
 <div>
  <div class="card"><h4>🔁 글리코겐 분해 vs 합성</h4>
   <p><b>분해</b>: 글리코겐<sub>n</sub> + P<sub>i</sub> → 글리코겐<sub>n−1</sub> + <b>포도당 1-인산</b> (글리코겐 인산화효소, PLP) → 가지제거 효소 → G6P (뮤테이스) → 간: G6Pase로 포도당 방출 / 근육: 해당과정</p>
   <p><b>합성</b>: G1P + UTP → <b>UDP-포도당</b> → 글리코겐 합성효소(α1→4) + 가지형성 효소(α1→6), 시작은 글리코게닌</p>
   {key('인산화효소: <b>인산화 = 활성(a)</b> / 합성효소: <b>인산화 = 불활성(b)</b> — 같은 인산화가 반대로 작용한다!')}
  </div>
  <div class="card" style="margin-top:3mm"><h4>🧪 근육 vs 간</h4>
   <p><b>근육</b>: 자기 쓸 ATP용. AMP·Ca<sup>2+</sup>로 인산화효소 b도 활성 → 수축하면 즉시 분해. G6Pase 없음 → 포도당을 혈액에 못 내보냄.</p>
   <p><b>간</b>: 혈당 유지용. 포도당이 인산화효소 a의 억제제(혈당 높으면 분해 멈춤). 글루카곤에 반응.</p></div>
 </div>
 <div class="card"><h4>💉 세 호르몬의 효과</h4>{t2}
  <figure class="fig">{cascade()}</figure></div>
</div>'''
    return [p1, p2]


add(id='P1', num='1', en_title='Glycogen as Energy Storage: How Long Can a Game Bird Fly?', ko_title='에너지 저장소 글리코겐: 사냥새는 얼마나 오래 날 수 있을까?',
    slides='강의 슬라이드 30–32', level=2,
    en='''<p>Since ancient times, people have observed that certain game birds, such as grouse, quail, and pheasants, fatigue easily. The Greek historian Xenophon wrote: “The bustards … can be caught if one is quick in starting them up, for they will fly only a short distance, like partridges, and soon tire; and their flesh is delicious.” The flight muscles of game birds rely almost entirely on the use of glucose 1-phosphate to drive ATP synthesis (Chapter 14). The glucose 1-phosphate derives from the breakdown of stored muscle glycogen, catalyzed by the enzyme glycogen phosphorylase. The rate of ATP production is limited by the rate at which glycogen can be broken down. During a “panic flight,” the game bird’s rate of glycogen breakdown is quite high, approximately 120 μmol/min of glucose 1-phosphate produced per gram of fresh tissue. Given that the flight muscles usually contain about 0.35% glycogen by weight, calculate how long a game bird can fly. (Assume the average molecular weight of a glucose residue in glycogen is 162 g/mol.)</p>''',
    ko='<p>예로부터 사람들은 뇌조·메추라기·꿩 같은 사냥새가 쉽게 지친다는 것을 관찰했다. (크세노폰: “느시는 재빨리 날려 보내면 잡을 수 있다. 자고새처럼 짧은 거리만 날고 곧 지치기 때문이다. 그리고 고기가 맛있다.”) 사냥새의 비행 근육은 ATP 합성을 거의 전적으로 포도당 1-인산에 의존한다. 포도당 1-인산은 글리코겐 인산화효소가 저장 글리코겐을 분해해 만든다. ATP 생산 속도는 글리코겐 분해 속도에 의해 제한된다. “공황 비행” 중 글리코겐 분해 속도는 조직 1 g당 포도당 1-인산 약 120 μmol/min이다. 비행 근육의 글리코겐 함량이 무게의 약 0.35%라면, 사냥새는 얼마나 오래 날 수 있는가? (글리코겐 속 포도당 단위의 평균 분자량 = 162 g/mol)</p>',
    answer=chips('약 <b>0.18분 ≈ 11초</b>'),
    explain=key('“조직 1 g” 기준으로 ① 글리코겐 속 포도당이 몇 μmol인지 ② 그걸 1분에 120 μmol씩 쓰면 몇 분인지. 나눗셈 한 번!') +
    steps('조직 1 g 속 글리코겐 = 1 g × 0.0035 = <b>3.5 mg</b> = 3.5×10<sup>−3</sup> g',
          '포도당 단위 몰수 = 3.5×10<sup>−3</sup> g ÷ 162 g/mol = 2.16×10<sup>−5</sup> mol = <b>21.6 μmol</b>',
          '비행 시간 = 21.6 μmol ÷ 120 μmol/min = <span class="hl">0.18 min ≈ 11초</span>') +
    fig(bars([('저장량 (1 g당)', 21.6, C['blue'], '21.6 μmol'), ('1분 사용량', 120, C['red'], '120 μmol/min')], height=90), '1분에 쓰는 양이 저장량의 5배 이상 → 몇 초 만에 바닥') +
    tip('그래서 사냥새는 짧게 “푸드득” 날고 곧 지쳐 버린다. 반면 오래 나는 철새는 지방을 산화하는 유산소 근육(문제 6)을 쓴다.', '연결'))

add(id='P2', num='2', en_title='Enzyme Activity and Physiological Function', ko_title='효소 활성과 생리적 기능',
    slides='강의 슬라이드 32, 56', level=1,
    en='<p>The V<sub>max</sub> of the glycogen phosphorylase from skeletal muscle is much greater than the V<sub>max</sub> of the same enzyme from liver tissue.<br><b>a.</b> What is the physiological function of glycogen phosphorylase in skeletal muscle? In liver tissue?<br><b>b.</b> Why does the V<sub>max</sub> of the muscle enzyme need to be greater than that of the liver enzyme?</p>',
    ko='<p>골격근의 글리코겐 인산화효소 V<sub>max</sub>는 간의 같은 효소보다 훨씬 크다.<br><b>a.</b> 골격근과 간에서 글리코겐 인산화효소의 생리적 기능은 각각 무엇인가?<br><b>b.</b> 왜 근육 효소의 V<sub>max</sub>가 간 효소보다 커야 하는가?</p>',
    answer=chips('a. 근육: <b>자기 수축용 ATP</b>를 위해 G1P 공급 / 간: <b>혈당 유지</b>용 포도당 공급', 'b. 근육은 순간적으로 ATP 수요가 수십~수백 배 폭증 → 매우 빠른 분해 필요 / 간은 천천히 꾸준히'),
    explain=key('같은 효소라도 “누구를 위해 일하느냐”가 다르다. 근육 = 나 자신, 간 = 몸 전체(혈액).') +
    table(['', '근육', '간'], [['글리코겐의 용도', '근육 자신의 해당과정 → ATP', 'G6Pase → 포도당 → 혈액 (뇌·적혈구용)'],
                              ['필요한 속도', '<b>폭발적</b> (전력 질주·도망)', '<b>느리고 꾸준히</b> (식사 사이 몇 시간)'],
                              ['주 신호', '에피네프린, AMP, Ca<sup>2+</sup>', '글루카곤 (포도당이 억제)']]) +
    steps('<b>a.</b> 근육은 G6Pase가 없어 포도당을 내보낼 수 없다 → 분해한 글리코겐은 전부 자기 ATP용. 간은 G6Pase로 포도당을 혈액에 내보내 혈당을 유지한다.',
          '<b>b.</b> 근육은 휴식 → 최대 운동 시 ATP 사용이 수십 배 이상 늘어난다. 이 속도를 따라가려면 효소의 최대 속도가 커야 한다. 간은 혈당을 몇 시간에 걸쳐 조금씩 보충하면 되므로 V<sub>max</sub>가 작아도 충분.') +
    tip('근육 효소 = 스포츠카 엔진(순간 가속), 간 효소 = 트럭 엔진(오래 꾸준히).', '비유'))

add(id='P3', num='3', en_title='Glycogen Phosphorylase Equilibrium', ko_title='글리코겐 인산화효소의 평형',
    slides='강의 슬라이드 32 · 13장 ΔG', level=2,
    en='<p>Glycogen phosphorylase catalyzes the removal of glucose from glycogen. The ΔG′° for this reaction is 3.1 kJ/mol.<br><b>a.</b> Calculate the ratio of [P<sub>i</sub>] to [glucose 1-phosphate] when the reaction is at equilibrium. (Hint: The removal of glucose units from glycogen does not change the glycogen concentration.)<br><b>b.</b> The measured ratio [P<sub>i</sub>]/[glucose 1-phosphate] in myocytes under physiological conditions is more than 100:1. What does this indicate about the direction of metabolite flow through the glycogen phosphorylase reaction in muscle?<br><b>c.</b> Why are the equilibrium and physiological ratios different? What is the possible significance of this difference?</p>',
    ko='<p>글리코겐 인산화효소는 글리코겐에서 포도당을 떼어 낸다. 이 반응의 ΔG′°는 +3.1 kJ/mol이다.<br><b>a.</b> 반응이 평형일 때 [P<sub>i</sub>] : [포도당 1-인산] 비를 계산하라. (힌트: 글리코겐에서 포도당 단위를 떼어도 글리코겐 농도는 변하지 않는다.)<br><b>b.</b> 생리적 조건의 근육세포에서 측정한 [P<sub>i</sub>]/[G1P]는 100 : 1이 넘는다. 이것은 근육에서 이 반응의 대사물 흐름 방향에 대해 무엇을 말해 주는가?<br><b>c.</b> 평형 비와 생리적 비가 왜 다른가? 이 차이의 의미는?</p>',
    answer=chips('a. 평형에서 [P<sub>i</sub>]/[G1P] ≈ <b>3.5</b>', 'b. 실제 비(&gt;100)가 평형보다 훨씬 큼 → <b>글리코겐 분해 방향</b>(G1P 생성)으로 흐른다',
                 'c. G1P가 즉시 소비되어 낮게 유지 → 평형에서 먼 <b>조절 지점</b> (합성은 다른 경로: UDP-포도당)'),
    explain=key('글리코겐 농도는 변하지 않으니 K에는 [G1P]/[P<sub>i</sub>]만 남는다.') +
    eq('글리코겐<sub>n</sub> + P<sub>i</sub> ⇌ 글리코겐<sub>n−1</sub> + G1P &nbsp;&nbsp; K = [G1P] / [P<sub>i</sub>]') +
    steps('<b>a.</b> K = e<sup>−3.1/2.478</sup> = e<sup>−1.25</sup> = 0.29 → [P<sub>i</sub>]/[G1P] = 1/0.29 ≈ <span class="hl">3.5</span>',
          '<b>b.</b> 실제 [G1P]/[P<sub>i</sub>] = Q &lt; 0.01 ≪ K(0.29) → ΔG = 3.1 + 2.478 × ln(0.01) ≈ 3.1 − 11.4 = <b>−8.3 kJ/mol</b> → 분해(G1P 만드는) 방향으로 진행.',
          '<b>c.</b> 생긴 G1P가 포스포글루코뮤테이스 → G6P → 해당과정으로 곧바로 빠져나가 [G1P]가 낮게 유지된다. 평형에서 멀리 있으므로 ① 흐름이 한 방향이고 ② 효소 활성(인산화·AMP 등)으로 흐름을 조절할 수 있다. 반대로 합성은 이 반응의 역반응이 아니라 UDP-포도당을 쓰는 별도 경로로 한다.') +
    fig(logaxis([(0.01, '세포 속 Q < 0.01', C['orange']), (0.29, '평형 K = 0.29', C['navy'])], -3, 1, label='Q ≪ K → 정반응(분해)'), '') +
    tip('표준값은 약간 불리(+3.1)해도, 세포는 P<sub>i</sub>를 많이·G1P를 적게 유지해 분해 쪽으로 밀어준다. 13장 공식 그대로!', '연결'))

add(id='P4', num='4', en_title='Regulation of Glycogen Phosphorylase', ko_title='글리코겐 인산화효소의 조절',
    slides='강의 슬라이드 48–49', level=1,
    en='<p>In muscle tissue, the rate of conversion of glycogen to glucose 6-phosphate is determined by the ratio of phosphorylase <i>a</i> (active) to phosphorylase <i>b</i> (less active). Determine what happens to the rate of glycogen breakdown if a broken cell extract of muscle containing glycogen phosphorylase is treated with (a) phosphorylase kinase and ATP (b) PP1 (c) epinephrine.</p>',
    ko='<p>근육에서 글리코겐 → G6P 전환 속도는 인산화효소 <i>a</i>(활성)와 <i>b</i>(덜 활성)의 비율로 결정된다. 글리코겐 인산화효소가 들어 있는 근육의 <b>깨진 세포 추출물</b>을 다음으로 처리하면 글리코겐 분해 속도는 어떻게 되는가? (a) 인산화효소 키나아제와 ATP (b) PP1(인단백질 인산가수분해효소 1) (c) 에피네프린</p>',
    answer=chips('(a) <b>증가</b> (b → a, 인산화)', '(b) <b>감소</b> (a → b, 탈인산화)', '(c) <b>거의 변화 없음</b> (세포가 깨져 수용체–cAMP 신호 체계가 작동 안 함)'),
    explain=key('인산화효소는 <b>인산이 붙으면 켜진다(a)</b>. 붙이는 효소 = 인산화효소 키나아제, 떼는 효소 = PP1.') +
    fig(flow(['인산화효소 b|(덜 활성)', '인산화효소 a|(활성, Ser-P)'], arrow_labels=['키나아제 + ATP → / ← PP1'], width=420, box_h=46, colors=[C['gray'], C['green']]), '') +
    steps('<b>(a)</b> 인산화효소 키나아제가 ATP의 인산을 b형의 Ser14에 붙여 a형으로 → 분해 속도 ↑.',
          '<b>(b)</b> PP1이 인산을 떼어 a형 → b형 → 분해 속도 ↓.',
          '<b>(c)</b> 에피네프린은 세포막 <b>수용체</b>에 붙어 G 단백질 → 아데닐산 고리화효소 → cAMP → PKA → 인산화효소 키나아제로 신호를 전달한다. 깨진 추출물에선 막 구조와 신호 연결이 망가져 에피네프린을 넣어도 효과가 (거의) 없다.') +
    tip('에피네프린은 “초인종”이고, 인산화효소 키나아제는 “문을 여는 손”이야. 집(세포)이 부서지면 초인종을 눌러도 아무도 문을 안 연다.', '비유'))

add(id='P6', num='6', en_title='Glycogen Breakdown in Migrating Birds', ko_title='철새의 글리코겐 분해',
    slides='강의 슬라이드 15, 21–22, 66', level=2,
    en='<p>Unlike a rabbit, running all-out for a few moments to escape a predator, migratory birds require energy for extended periods of time. For example, ducks generally fly several thousand miles during their annual migration. The flight muscles of migratory birds have a high oxidative capacity and obtain the necessary ATP through the oxidation of acetyl-CoA (obtained from fats) via the citric acid cycle. Compare the regulation of muscle glycolysis during short-term intense activity, as in a fleeing rabbit, and during extended activity, as in a migrating duck. Why must the regulation in these two settings be different?</p>',
    ko='<p>포식자를 피해 잠깐 전력으로 달리는 토끼와 달리, 철새는 오랜 시간 에너지가 필요하다. 예를 들어 오리는 해마다 수천 마일을 이동한다. 철새의 비행 근육은 산화 능력이 높아 지방에서 얻은 아세틸-CoA를 시트르산 회로로 산화해 ATP를 얻는다. 도망치는 토끼 같은 짧고 격렬한 활동과, 이동하는 오리 같은 긴 활동에서 근육 해당과정의 조절을 비교하라. 왜 두 상황의 조절이 달라야 하는가?</p>',
    answer=chips('토끼: 무산소 해당과정 <b>최대 가동</b> — AMP ↑, 에피네프린 → 글리코겐 분해·PFK-1 ↑, 젖산 생성', '오리: 지방산 산화가 주 연료 — 시트르산·아세틸-CoA·ATP ↑ → PFK-1·PDH <b>억제</b> → 해당과정 ↓, 글리코겐 절약',
                 '이유: 글리코겐은 몇 분 분량뿐 / 지방은 오래 가는 연료'),
    explain=table(['', '도망치는 토끼 (짧고 격렬)', '이동하는 오리 (길고 꾸준)'],
                  [['연료', '근육 글리코겐 → 해당과정 → <b>젖산</b>', '<b>지방산</b> → 아세틸-CoA → TCA → 산화적 인산화'],
                   ['신호', '에피네프린, [AMP] ↑, Ca<sup>2+</sup> ↑', '[시트르산] ↑, [아세틸-CoA] ↑, [ATP] 충분'],
                   ['글리코겐 인산화효소', '↑↑ (a형 + AMP)', '낮게 유지'],
                   ['PFK-1', '↑ (AMP)', '↓ (시트르산·ATP)'],
                   ['PDH', '—', '↓ (아세틸-CoA·NADH)']], cls='left') +
    steps('토끼는 몇 초 안에 최대 ATP가 필요 → 산소를 기다릴 수 없으니 해당과정을 풀가동. 짧게 쓰고 끝나니 효율보다 <b>속도</b>.',
          '오리는 몇 시간~며칠을 날아야 함 → 글리코겐은 금방 바닥나니(문제 1) 에너지가 훨씬 많은 지방을 태워야 한다. 지방 산화가 만든 시트르산·아세틸-CoA가 “연료 충분” 신호가 되어 포도당 사용을 억제(<b>포도당 절약</b>).',
          '연료와 산소 조건이 다르므로 같은 효소(PFK-1 등)를 반대 신호로 조절해야 한다.') +
    tip('단거리 선수는 “니트로 부스터”(해당과정), 마라토너는 “연비 운전”(지방 산화). 엔진 제어 프로그램이 다를 수밖에 없어.', '비유'))

add(id='P9', num='9', en_title='Blood Metabolites in Insulin Insufficiency', ko_title='인슐린이 부족할 때 혈중 대사물질',
    slides='강의 슬라이드 13, 46–47, 54–55', level=1,
    en='<p>For the patient described in Problem 8 (a man with insulin-dependent diabetes who has not taken any insulin for two days), predict the levels of each listed metabolite in his blood before treatment in the emergency room, relative to levels maintained during adequate insulin treatment: (a) glucose (b) ketone bodies (c) free fatty acids.</p>',
    ko='<p>문제 8의 환자(인슐린 의존성 당뇨병 환자가 이틀 동안 인슐린을 맞지 못함)에 대해, 응급실 치료 전 혈중 다음 대사물질의 농도를 인슐린을 적절히 맞을 때와 비교해 예측하라: (a) 포도당 (b) 케톤체 (c) 유리 지방산</p>',
    answer=chips('(a) 포도당 <b>↑↑</b> (고혈당)', '(b) 케톤체 <b>↑↑</b> (케톤산증)', '(c) 유리 지방산 <b>↑</b>'),
    explain=key('인슐린이 없으면 몸은 “굶고 있다”고 착각한다: 포도당은 넘치는데 세포가 못 쓰고, 지방을 태운다.') +
    steps('<b>(a) 포도당 ↑</b>: GLUT4가 막에 안 올라가 근육·지방이 포도당을 못 가져감 + 간은 글루카곤 우세로 당신생·글리코겐 분해 ↑ → 혈당 급상승.',
          '<b>(c) 유리 지방산 ↑</b>: 인슐린은 지방 분해(호르몬 민감성 지방분해효소)를 억제하는데, 그게 풀려 지방세포가 지방산을 대량 방출.',
          '<b>(b) 케톤체 ↑</b>: 간이 넘치는 지방산을 β-산화 → 아세틸-CoA가 TCA 처리량을 넘음(OAA는 당신생으로 빠짐) → 케톤체(아세토아세트산·β-하이드록시뷰티르산)로 → 혈액 산성화(당뇨성 케톤산증) → 혼수.') +
    fig(flow(['인슐린 ✕', '지방 분해 ↑|유리 지방산 ↑', '간 β-산화|아세틸-CoA 과잉', '케톤체 ↑|(케톤산증)'], box_h=46, colors=[C['red'], C['orange'], C['orange'], C['red']]), '') +
    tip('환자가 혼수 상태로 온 이유 = 고혈당 + 케톤산증(산성 혈액) + 소변으로 물이 빠진 탈수. 치료: 인슐린 + 수액.', '임상'))

add(id='P10', num='10', en_title='Metabolic Effects of Mutant Enzymes', ko_title='돌연변이 효소의 대사 효과',
    slides='강의 슬라이드 48–53', level=2,
    en='<p>Predict and explain the effect on glycogen metabolism of each of the listed defects caused by mutation: (a) Loss of the cAMP-binding site on the regulatory subunit of protein kinase A (PKA) (b) Loss of the protein phosphatase inhibitor (inhibitor 1 in Fig. 15-16) (c) Overexpression of phosphorylase <i>b</i> kinase in liver (d) Defective glucagon receptors in liver.</p>',
    ko='<p>돌연변이로 생긴 다음 결함이 글리코겐 대사에 미치는 효과를 예측하고 설명하라: (a) PKA 조절 소단위의 cAMP 결합 자리 소실 (b) 인단백질 인산가수분해효소 억제제(억제제 1) 소실 (c) 간에서 인산화효소 <i>b</i> 키나아제 과발현 (d) 간의 글루카곤 수용체 결함</p>',
    answer=chips('(a) PKA가 안 켜짐 → 분해 신호 차단, 합성효소 활성 유지 → 글리코겐 <b>↑(축적)</b>', '(b) PP1 항상 활성 → 인산화효소 끔·합성효소 켬 → 글리코겐 <b>↑</b>',
                 '(c) 인산화효소 a 과다 → 분해 <b>↑</b> → 간 글리코겐 ↓, 혈당 ↑', '(d) 글루카곤에 반응 못 함 → 공복에 분해 ✕ → 글리코겐 <b>↑</b>, 저혈당'),
    explain=key('규칙 두 개: <b>PKA 경로가 켜지면 → 분해 ↑·합성 ↓</b> / <b>PP1이 켜지면 → 분해 ↓·합성 ↑</b>.') +
    fig(cascade(), '글루카곤·에피네프린 → cAMP → PKA → 인산화효소 키나아제 → 인산화효소 a') +
    steps('<b>(a)</b> cAMP가 조절 소단위에 붙어야 촉매 소단위가 풀려나 활성. 결합 자리가 없으면 PKA는 영원히 꺼짐 → 인산화효소 키나아제·인산화효소 활성화 불가, 글리코겐 합성효소도 인산화(억제)되지 않음 → 글리코겐이 쌓인다.',
          '<b>(b)</b> 억제제 1은 PKA에 의해 인산화되면 PP1을 억제한다. 없으면 PP1이 항상 일함 → 인산화효소 탈인산화(끔) + 합성효소 탈인산화(켬) → 글리코겐 ↑, 분해 신호에 둔감.',
          '<b>(c)</b> 키나아제가 너무 많으면 인산화효소 a가 늘어 → 간 글리코겐 분해 ↑ → 간 글리코겐 적고 혈당은 높은 쪽.',
          '<b>(d)</b> 간은 글루카곤으로 공복을 알아채는데 수용체가 망가지면 cAMP가 안 생김 → 분해·당신생이 안 켜짐 → 간 글리코겐은 쌓이고 공복 시 <b>저혈당</b>.') +
    tip('신호 전달은 “도미노”. 어느 도미노가 빠졌는지만 보면, 그 뒤로 무엇이 안 넘어지는지 알 수 있다.', '요령'))

add(id='P11', num='11', en_title='Hormonal Control of Metabolic Fuel', ko_title='대사 연료의 호르몬 조절',
    slides='강의 슬라이드 18, 46–49, 55', level=2,
    en='<p>Between your evening meal and breakfast, your blood glucose drops and your liver becomes a net producer rather than consumer of glucose. Describe the hormonal basis for this switch, and explain how the hormonal change triggers glucose production by the liver.</p>',
    ko='<p>저녁 식사와 아침 식사 사이에 혈당이 떨어지고, 간은 포도당을 “소비하는 쪽”에서 “생산하는 쪽”으로 바뀐다. 이 전환의 호르몬적 기초를 설명하고, 호르몬 변화가 어떻게 간의 포도당 생산을 일으키는지 설명하라.</p>',
    answer=chips('혈당 ↓ → <b>인슐린 ↓, 글루카곤 ↑</b>', '간: 글루카곤 → cAMP → <b>PKA</b>', 'PKA → ① 글리코겐 분해 ↑·합성 ↓ ② F2,6BP ↓ → 해당과정 ↓·당신생 ↑ ③ 간 피루브산 키나아제 억제', '→ G6Pase로 포도당 방출'),
    explain=key('글루카곤 한 방에 PKA가 켜지고, PKA가 <b>세 군데</b>를 동시에 스위칭한다.') +
    fig(vflow(['혈당 ↓ (밤새 공복)', '이자 α세포: 글루카곤 ↑ (β세포 인슐린 ↓)', '간: 수용체 → cAMP → PKA', 'G6P → (G6Pase) → 혈액 포도당 ↑'],
              notes=['', '', '글리코겐 분해 + 당신생'], colors=[C['red'], C['orange'], C['orange'], C['green']], box_h=26, gap=20, width=420), '') +
    steps('<b>글리코겐 분해 ↑</b>: PKA → 인산화효소 키나아제 → 인산화효소 a. 동시에 글리코겐 합성효소는 인산화돼 꺼짐.',
          '<b>해당과정 ↓·당신생 ↑</b>: PKA가 PFK-2/FBPase-2를 인산화 → FBPase-2 활성 → 과당 2,6-이인산 ↓ → PFK-1 ↓, FBPase-1 ↑. 간형 피루브산 키나아제도 인산화돼 꺼짐 → PEP가 포도당 쪽으로.',
          '<b>장기적</b>: PEPCK·G6Pase 유전자 전사 ↑ (CREB, FOXO1).',
          '결과: 간이 만든 G6P를 G6Pase가 포도당으로 바꿔 혈액으로 내보냄 → 혈당 유지(특히 뇌).') +
    tip('인슐린 = “배부름” 모드(저장), 글루카곤 = “배고픔” 모드(방출). 간은 이 두 호르몬 비율을 보고 모드를 바꾼다.', '비유'))

for _n in ('5', '7', '8', '12'):
    ALL_ITEMS.append(dict(id='P' + _n, num=_n, level=3, kind='PROBLEM'))
ALL_ITEMS.sort(key=lambda i: int(i['num']))
