from lib import *

At = '[A]<sub>t</sub>'
A0 = '[A]<sub>0</sub>'
t12 = 't<sub>1/2</sub>'
kf, kr = 'k<sub>f</sub>', 'k<sub>r</sub>'
Aeq, Beq = 'A<sub>eq</sub>', 'B<sub>eq</sub>'
dAdt = F('d[A]', 'dt')

PAGES = []
def add(*a, **k): PAGES.append(page(len(PAGES) + 1, *a, **k))

# ---------------- 01 표지 ----------------
add('표지 · 이번 강의 로드맵', '물리약학 — 화학반응속도론 및 안정성 (1), 이재우 교수, 고려대학교 약학대학 (Ch.14)', 1,
    ['반응 속도 · 속도 법칙', '속도 상수 k · 반응 차수', '0차 · 1차 · 2차 반감기', '가역 · 평행 반응', '정류 상태 · Michaelis-Menten'],
    '새 단원(Ch.14): 약이 <b>얼마나 빨리 분해되는지</b>를 식으로 다룬다. 반응 속도·속도 법칙 → 0/1/2차 적분식·반감기·k 단위 → 차수 결정 → 복합 반응(가역·평행) → 정류 상태 근사법과 Michaelis-Menten·Lineweaver-Burk까지.',
    h4('오늘 강의 흐름') + tbl(['순서', '내용', '슬라이드'], [
        ['1', '기초 수학 (log, 적분) — 빈칸 예고편', '2'],
        ['2', '반응 속도론이 왜 필요한가 (안정성·유효기간), 분해 예시', '3~4'],
        ['3', '반응 속도 · 속도 법칙 · 속도 상수 · 반응 차수 · k 단위 · 예제', '5~8'],
        ['4', '0차 · 1차 · 2차 반응 — 그래프, 적분식, 반감기', '9~16'],
        ['5', '반응 차수의 결정 (그래프법 · 예제) · 0~2차 요약표', '17~19'],
        ['6', '복합 반응: 가역 반응 · 평행 반응', '20~26'],
        ['7', '정류 상태 근사법 · Michaelis-Menten · Lineweaver-Burk', '27~31'],
        ['8', 'Summary 1~4 (빈칸판 + 정답판) · Thank You', '32~40'],
    ]),
    h4('읽는 법') + ul(
        '강의용 PDF의 네모 칸·괄호 빈칸을 <b>슬라이드에 숨겨진 원문 텍스트</b>와 수업 내용 흐름으로 채웠어.',
        'Summary 1~4는 강의 자료에 <b>정답판 슬라이드(빨간 글씨)</b>가 같이 들어 있어서, 빈칸판과 정답판을 한 쪽에 묶었어.',
        '그래프 빈칸(슬라이드 9~11)은 축에 맞는 직선 개형을 그려 넣었어.') +
    box('tip', '빈칸 정답 표시법', f'빈칸·선택형 괄호·네모 칸의 정답은 이렇게 {A("파란 박스")}로 표시했어.') +
    box('exam', '시험 포인트', '중간고사처럼 OX가 슬라이드 문장에서 나온다면 이번 단원의 단골 함정은 <b>반감기와 초기 농도의 관계(0차 비례 · 1차 무관 · 2차 반비례)</b>, <b>k 단위</b>, <b>각 차수의 직선 그래프 축</b>이야.'),
    left_title='원문 정리')

# ---------------- 02 기초 수학 ----------------
add('이번 시간에 쓰이는 기초 수학 (빈칸 정답)', 'Basic math for kinetics', 2,
    ['log 빼기 = 나누기', '∫1/x dx = ln x', '∫1/x² dx = −1/x', 'ln e<sup>−kt</sup> = −kt'],
    '적분식 유도에 쓰는 공식 6개. 1차는 ∫1/x, 2차는 ∫1/x², 가역 반응은 ∫1/(ax+b), 평행 반응은 ∫e<sup>−kt</sup>를 쓴다.',
    tbl(['식', '정답'], [
        ['log A − log B =', A('log (A/B)')],
        ['∫ 1/x dx =', A('ln x + C')],
        ['∫ 1/x² dx =', A('−1/x + C')],
        ['∫ 1/(ax+b) dx =', A('(1/a) ln(ax+b) + C')],
        ['ln e<sup>−kt</sup> =', A('−kt')],
        ['∫<sub>0</sub><sup>t</sup> e<sup>−kt</sup> dt =', A('−(1/k)(e<sup>−kt</sup> − 1)') + ' = (1/k)(1 − e<sup>−kt</sup>)'],
    ]),
    tbl(['공식', '어디에 쓰나'], [
        ['∫1/x dx = ln x', '1차 반응 적분 → ' + G('ln[A]<sub>t</sub> = −kt + ln[A]<sub>0</sub>')],
        ['∫1/x² dx = −1/x', '2차 반응 적분 → ' + G('1/[A]<sub>t</sub> = kt + 1/[A]<sub>0</sub>')],
        ['∫1/(ax+b) dx', '가역 반응 적분 (a = k<sub>f</sub> + k<sub>r</sub>)'],
        ['ln e<sup>−kt</sup> = −kt', '1차 식을 지수형으로: [A]<sub>t</sub> = [A]<sub>0</sub>e<sup>−kt</sup>'],
        ['∫e<sup>−kt</sup>dt', '평행 반응에서 생성물 A, N 농도 구하기'],
        ['log ↔ ln', 'ln x = 2.303 log x → 그래프 기울기에 2.303이 붙는 이유'],
    ]) +
    box('warn', '혼동 주의', '∫1/x² dx = <b>−</b>1/x (부호 마이너스!). 그래서 2차 적분식에서 −kt = −1/[A]<sub>t</sub> + 1/[A]<sub>0</sub> → 정리하면 1/[A]<sub>t</sub> = <b>+</b>kt + 1/[A]<sub>0</sub>.') +
    box('tip', '체크', '∫<sub>0</sub><sup>t</sup>e<sup>−kt</sup>dt에 t = 0을 넣으면 0, t → ∞면 1/k. 결과식이 맞는지 이렇게 확인해.'))

# ---------------- 03 필요성 ----------------
add('화학 반응 속도론 이해의 필요성 (빈칸 정답)', 'Why chemical kinetics? — stability testing', 3,
    ['안정성 시험', '분해 속도 → 유효기간', '배합 시 pH', '효능 상실 · 순응도 · 독성'],
    '약은 온도·습도·빛·pH에 의해 분해된다. 분해 속도를 알아야 저장 유효기간과 저장 조건을 정할 수 있고, 배합할 때는 pH에 따른 분해 속도를 알아야 한다.',
    h4('안정성 시험에서의 필요성') + ul(
        f'온도, 습도, 빛, pH 등의 다양한 요인에 의해서 약물이 {A("분해")}될 수 있음.',
        '약물에 따라 안정한 저장 조건을 확립해야 함.',
        f'약물의 분해 속도에 따른 저장 {A("유효 기간")} 및 {A("저장 조건")} 확립에 반응 속도론 필요.',
        f'약물을 배합할 경우 {A("pH")}에 따른 약물의 분해 속도를 알고 있어야 함.') +
    h4('약물 분해 측정의 중요성') + ul(
        '약물의 분해 정도가 임상적으로 어떠한 영향을 주는가?',
        f'{Y("효능")}을 상실하는가?',
        f'제형의 외형 변형에 따라 환자의 {Y("복약 순응도")}가 떨어질 수 있는가?',
        f'{Y("독성 분해산물")}이 생성되는가?'),
    tbl(['빈칸', '정답', '구별 포인트'], [
        ['약물이 ___될 수 있음', A('분해'), '온도·습도·빛·pH = 분해 요인 4개'],
        ['저장 ___ 및 ___ 확립', A('유효 기간') + ' / ' + A('저장 조건'), '분해 속도 → 유효기간·저장 조건'],
        ['배합 시 ___에 따른 분해', A('pH'), 'Summary 1 선택형: (온도 / ' + A('pH') + ')'],
    ]) +
    h4('분해가 문제인 이유 3가지') + tbl(['문제', '예'], [
        ['효능 상실', '유효 성분 함량 ↓ → 약효 ↓'],
        ['복약 순응도 ↓', '변색·냄새·외형 변화 → 환자가 안 먹음'],
        ['독성 분해산물', '분해되며 해로운 물질 생성'],
    ]) +
    box('exam', '시험 포인트', 'Summary 1에서는 “약물을 배합할 경우 (<b>온도</b>/<b>pH</b>)에 따른 분해 속도” 선택형으로 나와. 정답은 <b>pH</b>. 분해 <b>요인</b>에는 온도도 들어가지만, <b>배합</b> 문장에서는 pH야.'))

# ---------------- 04 분해 예시 ----------------
add('화학 반응 속도론 이해의 필요성 — 약물 분해의 예시 (빈칸 정답)', 'Examples: thiamine HCl, Clavulin', 4,
    ['티아민: pH 2–3 안정', 'pH 6 이상 불안정', '클라불린: pH 6 안정', 'pH 3.5 → 약효 ↓'],
    '티아민(비타민 B1)은 산성(pH 2–3)에서 안정하고 pH 6 이상에서 불안정하다. 클라불린(아목시실린)은 pH 6에서 안정하고 pH 3.5로 섞이면 약효가 크게 줄어든다. 약사는 약마다 안정 조건과 분해 속도를 알아야 한다.',
    h4('약물 분해의 예시') +
    '<p><b>✓ Thiamine hydrochloride (티아민, 비타민 B1)</b></p>' + ul(
        f'pH 2–3에서 {Y("안정")}하며 pH 6 이상에서는 {Y("불안정")}함.',
        '만약 pH 8~9 이상인 완충 용액에 희석되었을 경우 분해될 수 있음.',
        f'이런 경우 분해 속도를 지연시키는 완충 용액의 {A("추가 희석")}을 고려할 수 있음.') +
    '<p><b>✓ Clavulin (아목시실린; 항생제)</b></p>' + ul(
        f'pH 6에서 안정하며 pH 3.5 등으로 혼합 조제되었을 경우 {Y("심각한 약효의 감소")}가 일어남.') +
    f'<p>➢ 실무 약사의 경우 약물에 따른 {Y("안정 조건")}과 {Y("분해 속도")}를 고려하여, 시판되는 약의 보관 유효기간이 조건에 따라 크게 달라질 수 있음을 알고 있어야 함.</p>',
    tbl(['약', '안정한 pH', '불안정한 조건'], [
        ['티아민 HCl (비타민 B1)', G('pH 2–3 (산성)'), 'pH 6 이상, 특히 pH 8–9 완충액'],
        ['클라불린 (아목시실린)', G('pH 6'), 'pH 3.5 등 산성으로 혼합 조제'],
    ]) +
    '<p>빈칸 정답: 완충 용액의 ' + A('추가 희석') + '</p>' +
    '<p><b>왜 희석하면 분해가 느려질까?</b> 완충 용액이 pH를 8–9로 붙잡고 있어서 분해가 빨라져. 완충 용액을 더 희석하면 완충 능력(완충 성분 농도)이 줄어 pH를 강하게 유지하지 못하고, 완충 성분이 분해를 촉매하는 효과도 줄어 분해가 느려져. [즉, 희석 = 분해 촉진 환경을 약하게 만들기]</p>' +
    box('warn', '혼동 주의', '티아민은 <b>산성에서 안정</b>, 클라불린은 <b>pH 6에서 안정·산성(3.5)에서 불안정</b>. 두 약의 방향이 반대라 OX로 바꿔치기하기 좋아.'))

# ---------------- 05 반응 속도 ----------------
add('화학 반응 속도 — 반응 속도의 정의 (빈칸 정답)', 'Chemical kinetics · Reaction rate', 5,
    ['Chemical kinetics', '반응물 소비 = 생성물 생성', '−d[A]/dt = d[B]/dt', '2A → B: −½ d[A]/dt'],
    '반응 속도 = 반응물(A)이 소비되는 속도 = 생성물(B)이 생성되는 속도. A는 줄어들어 d[A]/dt가 음수라 앞에 −를 붙이고, 계수가 2면 1/2을 곱해 맞춘다.',
    h4('화학반응속도론 (Chemical kinetics)') +
    '<p>화학 반응의 속도를 다루는 화학의 한 분야로 반응 메커니즘을 고려한 반응 속도의 계산 등이 포함된다.</p>' +
    h4('반응 속도 (Reaction rate)') +
    '<p style="text-align:center">A → B<br>반응 속도 = A(반응물)가 소비되는 속도 = B(생성물)가 생성되는 속도<br>= ' + A('−' + F('d[A]', 'dt')) + ' = ' + F('d[B]', 'dt') + '</p>' +
    '<p>만약, 반응물의 계수가 1 초과로 존재할 경우, <b>2A → B</b><br>A 2분자가 소비되는 속도 = B 1분자가 생성되는 속도</p>' +
    '<p style="text-align:center">' + A('−' + F('1', '2') + F('d[A]', 'dt')) + ' = ' + F('d[B]', 'dt') + '</p>' +
    '<p>그림: 시간이 지날수록 A(검은 점)는 감소, B(빨간 점)는 증가. 그래프에서 A 분자 수 곡선은 내려가고 B 곡선은 올라감.</p>',
    tbl(['빈칸', '정답', '이유'], [
        ['A → B', A('−d[A]/dt'), 'A는 줄어드니 d[A]/dt < 0 → −를 붙여 양수로'],
        ['2A → B', A('−½ · d[A]/dt'), 'A가 B보다 2배 빨리 줄어듦 → 1/2로 맞춤'],
    ]) +
    '<p><b>왜 −가 붙나?</b> 속도는 항상 양수로 표현해. 반응물 농도는 시간에 따라 감소 → 기울기 d[A]/dt가 음수 → −를 붙여야 양수가 돼. 생성물은 증가하니 그대로 +.</p>' +
    '<p><b>왜 1/2?</b> 2A → B에서 B 1개가 생길 때 A는 2개가 사라져. A의 감소 속도는 B 생성 속도의 2배 → 같은 “반응 속도” 하나로 맞추려면 A 쪽을 2로 나눠.</p>' +
    box('exam', '시험 포인트', 'Summary 1: “반응 속도 = (생성물 / <b>반응물</b>)이 소비되는 속도 = (<b>생성물</b> / 반응물)이 생성되는 속도”, “= (<b>−</b>/+) d[A]/dt = (−/<b>+</b>) d[B]/dt”.'))

# ---------------- 06 일반식 · 속도 법칙 ----------------
add('화학 반응 속도 — 일반식과 속도 법칙 (빈칸 정답)', 'General rate expression · Rate law', 6,
    ['aA + bB → cC + dD', '계수로 나누기', 'Rate law', 'rate = k[A]<sup>x</sup>[B]<sup>y</sup>'],
    '일반 반응 aA + bB → cC + dD의 반응 속도는 각 물질의 농도 변화를 계수로 나눈 값으로 모두 같다. 속도 법칙은 이 속도를 속도 상수 k와 반응물 농도의 지수(x, y)로 표현한 것이다.',
    '<p>일반적으로 화학 반응 속도는 다음과 같이 쓸 수 있음.</p>' +
    eq('aA + bB → cC + dD',
       'Reaction rate = −' + F('1', 'a') + F('d[A]', 'dt') + ' = −' + F('1', 'b') + F('d[B]', 'dt') + ' = ' + F('1', 'c') + F('d[C]', 'dt') + ' = ' + F('1', 'd') + F('d[D]', 'dt')) +
    h4('화학반응속도법칙 (Rate law)') +
    f'<p>화학 반응의 속도를 {A("속도 상수")}와 {A("반응물 농도")}의 지수로 표현한 것</p>' +
    eq('aA + bB → cC + dD &nbsp;→&nbsp; Reaction rate = k[A]<sup>x</sup>[B]<sup>y</sup>',
       '−' + F('1', 'a') + F('d[A]', 'dt') + ' = −' + F('1', 'b') + F('d[B]', 'dt') + ' = ' + F('1', 'c') + F('d[C]', 'dt') + ' = ' + F('1', 'd') + F('d[D]', 'dt') + ' = k[A]<sup>x</sup>[B]<sup>y</sup>'),
    tbl(['빈칸', '정답', '포인트'], [
        ['___와', A('속도 상수'), 'k (rate constant)'],
        ['___의 지수로', A('반응물 농도'), '[A]<sup>x</sup>[B]<sup>y</sup> — 생성물 농도 아님'],
    ]) +
    '<p><b>읽는 법</b>: 반응물(A, B) 쪽은 줄어드니 −, 생성물(C, D) 쪽은 +. 모두 자기 계수로 나누면 하나의 “반응 속도”가 돼.</p>' +
    box('warn', '혼동 주의', '속도 법칙의 지수 x, y는 <b>계수 a, b와 같지 않아도 돼</b>. 계수는 반응식에서 바로 보이지만, 지수는 실험으로만 구해 (다음 슬라이드).') +
    box('tip', '비유', '속도 법칙 = “반응 속도 레시피”. k는 반응 자체의 빠르기(체질), [A]<sup>x</sup>[B]<sup>y</sup>는 재료가 얼마나 있는지에 대한 민감도야.'))

# ---------------- 07 k · 반응 차수 ----------------
add('화학 반응 속도 — 속도 상수와 반응 차수 (빈칸 정답)', 'Rate constant & reaction order', 7,
    ['k: 종류·온도에 의존', 'k: 농도와 무관', 'x + y = 전체 차수', '차수는 실험적으로만'],
    '속도 상수 k는 반응물의 종류와 온도에 따라 변하지만 농도와는 무관하다. 반응 차수 x, y는 반드시 실험으로 구하며, x + y가 전체 반응 차수이다.',
    eq('−' + F('1', 'a') + F('d[A]', 'dt') + ' = −' + F('1', 'b') + F('d[B]', 'dt') + ' = ' + F('1', 'c') + F('d[C]', 'dt') + ' = ' + F('1', 'd') + F('d[D]', 'dt') + ' = k[A]<sup>x</sup>[B]<sup>y</sup>') +
    h4('속도 상수(Rate constant)와 반응 차수(reaction order)') + ul(
        f'<b>k = 속도 상수</b> : 반응물의 {Y("종류, 온도")}에 따라 변하지만 반응물의 {A("농도와는 무관")}함.',
        f'<b>반응 차수</b> : k[A]<sup>x</sup>[B]<sup>y</sup>에서, x는 A에 대한 반응 차수, y는 B에 대한 반응 차수, x + y = 전체 반응 차수, x, y 값은 반드시 {A("실험적")}으로 구해야 함!') +
    '<p style="text-align:center">F<sub>2</sub>(g) + 2ClO<sub>2</sub>(g) → 2FClO<sub>2</sub>(g)<br>−' + F('d[F<sub>2</sub>]', 'dt') + ' = −' + F('1', '2') + F('d[ClO<sub>2</sub>]', 'dt') + ' = ' + F('1', '2') + F('d[FClO<sub>2</sub>]', 'dt') + ' = k[F<sub>2</sub>]<sup>1</sup>[ClO<sub>2</sub>]<sup>1</sup></p>' +
    '<p>x = 1, y = 1, x + y = 2 : F<sub>2</sub>에 대한 차수 1, ClO<sub>2</sub>에 대한 반응 차수 = 1, 전체 반응 차수 = ' + A('2') + '</p>',
    tbl(['빈칸', '정답', '포인트'], [
        ['반응물의 ___함', A('농도와는 무관'), 'Summary 1: (<b>무관하며</b> / 영향을 받으며)'],
        ['반드시 ___으로', A('실험적'), 'Summary 1: (이론적으로 계산 가능 / <b>실험적으로만</b>)'],
        ['전체 반응 차수 =', A('2'), 'x + y = 1 + 1 (슬라이드 끝이 잘려 있음)'],
    ]) +
    '<p><b>예시 함정</b>: F<sub>2</sub> + <b>2</b>ClO<sub>2</sub>에서 ClO<sub>2</sub>의 계수는 2지만 차수는 <b>1</b>. 계수 ≠ 차수의 대표 예야.</p>' +
    tbl(['k를 바꾸는 것', 'k를 안 바꾸는 것'], [
        ['반응물의 종류, ' + Y('온도') + ' (온도 ↑ → k ↑, 다음 시간 Arrhenius)', '반응물의 ' + Y('농도')],
    ]) +
    box('exam', '시험 포인트', '“속도 상수 k는 반응물의 농도가 높을수록 커진다” → <b>X</b>. 농도가 높으면 <b>속도</b>는 커질 수 있지만 <b>k</b>는 그대로야. “반응 차수는 반응식의 계수로 정해진다” → <b>X</b> (실험적으로만).'))

# ---------------- 08 k 단위 · 예제 ----------------
add('속도 상수와 0차 반응 — 속도 상수의 단위 · 예제 (빈칸 정답)', 'Units of k · initial-rate example', 8,
    ['0차: mol/L·sec', '1차: sec<sup>−1</sup>', '2차: L/mol·sec', '초기속도법'],
    'k = 속도 ÷ [A]<sup>x</sup>이므로 차수가 올라갈수록 단위에 (mol/L)이 하나씩 더 나뉜다. 0차 mol/L·s, 1차 s<sup>−1</sup>, 2차 L/mol·s. 예제: 초기속도 표로 rate = k[A]²[B], k = 20 L²/mol²·s.',
    '<p style="text-align:center">A → B, &nbsp; −' + dAdt + ' = k[A]<sup>x</sup> &nbsp;→&nbsp; k = −' + dAdt + F('1', '[A]<sup>x</sup>') + '</p>' +
    tbl(['차수', 'k 계산', '단위 (정답)'], [
        ['x = 0 (0차)', 'k = −d[A]/dt = (mol/L)/sec', A('mol/L·sec')],
        ['x = 1 (1차)', 'k = (mol/L)/(sec·mol/L)', A('sec<sup>−1</sup>')],
        ['x = 2 (2차)', 'k = (mol/L)/(sec·(mol/L)<sup>2</sup>)', A('L/sec·mol')],
    ]) +
    h4('예제') + '<p>A + 2B → C 반응에서 농도에 따른 초기반응속도의 측정결과가 표와 같을 때, 반응 속도식과 k값과 단위를 구하시오.</p>' +
    tbl(['실험', '[A] (mol/L)', '[B] (mol/L)', 'C 생성속도 (mol/L·s)'], [
        ['1', '0.1', '0.1', '0.02'], ['2', '0.1', '0.2', '0.04'], ['3', '0.2', '0.1', '0.08']]) +
    '<p>정답: ' + A('rate = k[A]<sup>2</sup>[B]') + ', ' + A('k = 20 L<sup>2</sup>/mol<sup>2</sup>·s') + '</p>',
    h4('예제 풀이 (초기속도법)') + tbl(['단계', '내용'], [
        ['👀 단서', '한 번에 한 물질 농도만 바뀐 실험 쌍을 찾는다'],
        ['🧮 실험 1 → 2', '[A] 그대로, [B] ×2 → 속도 0.02 → 0.04 (×2) → 2<sup>y</sup> = 2 → ' + G('y = 1')],
        ['🧮 실험 1 → 3', '[B] 그대로, [A] ×2 → 속도 0.02 → 0.08 (×4) → 2<sup>x</sup> = 4 → ' + G('x = 2')],
        ['💡 속도식', 'rate = d[C]/dt = k[A]<sup>2</sup>[B]<sup>1</sup> (전체 3차). C의 계수가 1이라 C 생성속도 = 반응 속도'],
        ['🧮 k', 'k = 0.02 / (0.1<sup>2</sup> × 0.1) = 0.02 / 0.001 = ' + G('20')],
        ['🔍 단위', '(mol/L·s) ÷ (mol/L)<sup>3</sup> = ' + G('L<sup>2</sup>/(mol<sup>2</sup>·s)')],
    ]) +
    box('warn', '함정 체크', 'B의 계수는 2지만 차수 y = 1, A의 계수는 1이지만 차수 x = 2. <b>계수 ≠ 차수</b>를 숫자로 확인하는 예제야.') +
    box('tip', '단위 외우기', '<b>k 단위 = (mol/L)<sup>1−n</sup>·s<sup>−1</sup></b> (n = 전체 차수). n = 0 → mol/L·s, n = 1 → s<sup>−1</sup>, n = 2 → L/mol·s, n = 3 → L²/mol²·s.'))

# ---------------- 09~11 그래프 ----------------
def graph_page(order, slide, ylab, kind, kw, summ, ans, why, trap):
    add(f'{order}차 반응과 {order}차 반감기 — 그래프 빈칸 (빈칸 정답)', f'{["Zero", "First", "Second"][order]}-order reaction · graphs', slide, kw, summ,
        f'<p>➢ <b>{order}차 반응</b> A → B</p>' +
        '<div class="grs">' +
        f'<figure>{graph(kind, 190, 140, ylab, ans)}<br>왼쪽 빈 그래프 정답: {A(ylab + " vs t = 직선")}</figure>' +
        f'<figure>{graph({0: "line_down", 1: "exp_down", 2: "inv_down"}[order], 190, 140, "[A]")}<br>오른쪽(원본): [A] vs t</figure></div>' +
        why, trap)

graph_page(0, 9, '[A]', 'line_down',
           ['[A] vs t 직선', '기울기 = −k', '농도 일정하게 감소'],
           '0차 반응은 [A]를 그대로 t에 대해 그리면 기울기 −k인 직선이 된다. 오른쪽 원본 그래프도 [A]가 직선으로 줄어든다.',
           '기울기 −k',
           '<p>적분식 [A]<sub>t</sub> = −kt + [A]<sub>0</sub> → y = [A]<sub>t</sub>, x = t, 기울기 = ' + G('−k') + ', y절편 = [A]<sub>0</sub>.</p>',
           tbl(['차수', '직선이 되는 축', '기울기'], [
               [A('0차'), A('[A] vs t'), '−k'], ['1차', 'ln[A] vs t', '−k'], ['2차', '1/[A] vs t', '+k']]) +
           '<p>0차는 단위 시간마다 <b>같은 양</b>이 줄어. 그래서 [A]가 0에 닿는 순간이 있어(직선이 x축과 만남).</p>' +
           box('tip', '비유', '0차 = 한 시간에 정확히 10개씩 파는 가게. 재고가 많든 적든 판매 속도는 같아.') +
           box('exam', '시험 포인트', '“0차 반응에서 [A]와 시간의 그래프는 직선이고 기울기는 −k” → O.'))

graph_page(1, 10, 'ln[A]', 'line_down',
           ['ln[A] vs t 직선', '기울기 = −k', '[A] vs t는 지수 곡선'],
           '1차 반응은 [A]를 그대로 그리면 지수적으로 줄어드는 곡선(오른쪽)이지만, ln[A]를 t에 대해 그리면 기울기 −k인 직선이 된다.',
           '기울기 −k',
           '<p>적분식 ln[A]<sub>t</sub> = −kt + ln[A]<sub>0</sub> → y = ln[A]<sub>t</sub>, 기울기 = ' + G('−k') + ', y절편 = ln[A]<sub>0</sub>.</p>',
           tbl(['그래프', '모양', '이유'], [
               ['[A] vs t', '지수 감소 곡선', '[A]<sub>t</sub> = [A]<sub>0</sub>e<sup>−kt</sup>'],
               [A('ln[A] vs t'), A('직선'), 'ln을 취하면 지수가 내려와 일차식'],
           ]) +
           '<p>1차는 단위 시간마다 <b>같은 비율</b>이 줄어 (예: 매시간 10%씩). 그래서 [A]가 0에 닿지 않고 점점 천천히 줄어.</p>' +
           box('warn', '혼동 주의', 'ln[A] vs t의 기울기는 <b>−k</b>, log[A] vs t로 그리면 기울기는 <b>−k/2.303</b>.'))

graph_page(2, 11, '1/[A]', 'line_up',
           ['1/[A] vs t 직선', '기울기 = +k', '[A] vs t는 반비례 곡선'],
           '2차 반응은 1/[A]를 t에 대해 그리면 기울기 +k로 올라가는 직선이 된다. [A] 자체는 1차보다 더 완만하게 꼬리를 끄는 곡선이다.',
           '기울기 +k',
           '<p>적분식 1/[A]<sub>t</sub> = kt + 1/[A]<sub>0</sub> → y = 1/[A]<sub>t</sub>, 기울기 = ' + G('+k') + ', y절편 = 1/[A]<sub>0</sub>.</p>',
           tbl(['차수', '직선 축', '기울기 부호'], [
               ['0차', '[A] vs t', '− (내려감)'], ['1차', 'ln[A] vs t', '− (내려감)'], [A('2차'), A('1/[A] vs t'), A('+ (올라감)')]]) +
           '<p>[A]가 줄어들면 1/[A]는 커지니까 그래프가 <b>올라가</b>. 2차만 기울기가 양수야.</p>' +
           box('exam', '시험 포인트', '“2차 반응의 1/[A] vs t 그래프 기울기는 −k” → <b>X</b> (+k). 부호 바꾸기 함정 주의.'))

# ---------------- 12 0차 유도 ----------------
add('속도 상수와 0차 반응 — 0차 반응의 적분식 (빈칸 정답)', 'Zero-order reaction: integrated rate law', 12,
    ['Zero-order', '속도가 농도에 무관', '−d[A]/dt = k', '[A]<sub>t</sub> = −kt + [A]<sub>0</sub>'],
    '0차 반응은 반응 속도가 반응물 농도에 따라 변하지 않는 반응이다. −d[A]/dt = k를 0→t로 적분하면 [A]<sub>t</sub> = −kt + [A]<sub>0</sub>.',
    f'<p>• <b>0차 반응 (Zero-order reaction)</b> : 반응 속도가 반응물 농도에 따라 {A("변하지 않는")} 반응</p>' +
    '<p style="text-align:center">A → B</p>' +
    eq('−' + dAdt + ' = k[A]<sup>x</sup> → k = −' + dAdt + F('1', '[A]<sup>x</sup>') + ' → x = 0 (0차 반응) → k = −' + dAdt,
       '−k · ∫<sub>0</sub><sup>t</sup> dt = ∫<sub>[A]0</sub><sup>[A]t</sup> d[A] → −kt = [A]<sub>t</sub> − [A]<sub>0</sub> → ' + A('[A]<sub>t</sub> = −kt + [A]<sub>0</sub>')),
    tbl(['빈칸', '정답'], [
        ['반응물 농도에 따라 ___ 반응', A('변하지 않는')],
        ['빨간 박스', A('[A]<sub>t</sub> = −kt + [A]<sub>0</sub>')],
    ]) +
    h4('유도 한 줄씩') + tbl(['단계', '내용'], [
        ['1', '[A]<sup>0</sup> = 1이라 속도식이 −d[A]/dt = k'],
        ['2', '변수 분리: d[A] = −k dt'],
        ['3', '양변 적분: [A]<sub>t</sub> − [A]<sub>0</sub> = −kt'],
        ['4', '정리: ' + G('[A]<sub>t</sub> = −kt + [A]<sub>0</sub>') + ' (y = ax + b 꼴)'],
    ]) +
    box('exam', '시험 포인트', 'Summary 2: 0차 반응은 반응 속도가 반응물 농도에 따라 (<b>변하지 않음</b> / 비례함).'))

# ---------------- 13 0차 의미 ----------------
add('0차 반응의 의미 (빈칸 정답)', 'Meaning of zero-order kinetics', 13,
    ['직선으로 감소', '그래프 직선', '기울기 = −k', '|기울기| = k'],
    '시간에 따라 반응물 농도가 직선으로 줄어들면, 즉 [A]<sub>t</sub> vs t 그래프가 직선이고 기울기가 −k이면 0차 반응이다. 실험에서는 그래프 기울기의 절대값이 k다.',
    eq(G('[A]<sub>t</sub> = −kt + [A]<sub>0</sub>')) + ul(
        f'<b>0차 반응 (Zero-order reaction)</b> : 시간에 따른 반응물의 농도가 {A("직선")}으로 감소할 때 또는 시간(t)과 반응물의 농도([A]<sub>t</sub>)와의 그래프가 {A("직선")}이고 그 기울기가 {A("−k")}일 때, 0차 반응이라고 함.',
        f'<b>실험적으로 속도 상수 구하기</b> : 반응이 0차라고 할 때, 시간과 반응물 농도 감소량을 측정하여 그래프를 그린 뒤 {Y("기울기의 절대값")}을 취하면 됨.') +
    '<p>그래프: [A]<sub>t</sub> vs time(t), y절편 [A]<sub>0</sub>, 기울기 = −k</p>',
    tbl(['빈칸', '정답', '포인트'], [
        ['농도가 ___으로 감소', A('직선'), 'Summary 2: (<b>직선</b> / 지수적)'],
        ['그래프가 ___이고', A('직선'), '[A]<sub>t</sub> vs t'],
        ['기울기가 ___일 때', A('−k'), 'k = |기울기|'],
    ]) +
    '<p><b>왜 절대값?</b> 기울기는 −k라 음수로 나와. k는 양수로 쓰니까 부호만 떼면 돼.</p>' +
    '<p><b>약학 예</b>: 현탁액(suspension) — 녹아 있는 약은 계속 분해되지만 고체가 녹아 보충해서 용액 농도가 일정(포화)하게 유지 → 겉보기 0차. (교재 내용, 다음 시간 범위일 수 있음)</p>' +
    box('exam', '시험 포인트', 'Summary 2: 0차 반응은 시간에 따른 (<b>반응물</b> / 생성물)이 (<b>직선</b> / 지수적)으로 감소.'))

# ---------------- 14 0차 반감기 ----------------
add('0차 반응의 반감기 (빈칸 정답)', 'Half-life of zero-order reaction', 14,
    ['반감기 = 절반까지 시간', 't<sub>1/2</sub> = [A]<sub>0</sub>/2k', '초기 농도에 비례', '금속 표면 · 효소'],
    '반감기는 초기 농도가 절반이 되는 데 걸리는 시간. 0차에서는 t<sub>1/2</sub> = [A]<sub>0</sub>/2k로 초기 농도에 비례한다. 0차 반응은 금속 표면이나 효소가 필요한 반응에서 주로 보이며, N<sub>2</sub>O는 뜨거운 백금 표면 위에서만 분해된다.',
    f'<p>• <b>0차 반응에서의 반감기</b>: 초기 반응물의 농도가 {A("절반")}으로 감소하기까지 걸리는 시간</p>' +
    eq('[A]<sub>t</sub> = −kt + [A]<sub>0</sub> → ' + F('1', '2') + '[A]<sub>0</sub> = −kt<sub>1/2</sub> + [A]<sub>0</sub> → ' + A('t<sub>1/2</sub> = ' + F('[A]<sub>0</sub>', '2k'))) +
    f'<p style="color:#b91c1c"><b>즉, 0차 반응의 반감기는 초기 농도에 비례함!</b></p>' +
    '<p style="text-align:center">2N<sub>2</sub>O(g) → 2N<sub>2</sub>(g) + O<sub>2</sub>(g)<br>−' + F('1', '2') + F('d[N<sub>2</sub>O]', 'dt') + ' = k[N<sub>2</sub>O]<sup>0</sup> = k (constant)</p>' + ul(
        f'영차 반응(0차)은 어떤 반응을 진행시키기 위하여 {Y("금속 표면이나 효소")}와 같은 물질이 필요한 경우에 주로 발견됨.',
        f'예를 들어 N<sub>2</sub>O의 분해 반응은 {Y("뜨거운 백금 표면")} 위에서만 일어남.'),
    tbl(['빈칸', '정답'], [['농도가 ___으로', A('절반')], ['빨간 박스', A('t<sub>1/2</sub> = [A]<sub>0</sub>/2k')]]) +
    h4('왜 0차가 되나? (그림 해석)') +
    '<p>백금(Pt) 표면의 자리 수는 정해져 있어. 왼쪽(N<sub>2</sub>O 적음)이든 오른쪽(N<sub>2</sub>O 많음)이든 표면이 이미 꽉 차 있으면 반응하는 분자 수가 같아 → <b>농도와 무관하게 속도 일정</b> = 0차.</p>' +
    box('tip', '비유', '계산대가 3개뿐인 마트: 줄이 10명이든 100명이든 1분에 계산되는 사람 수는 같아. 계산대 = 금속 표면/효소 자리.') +
    tbl(['초기 농도 [A]<sub>0</sub> 2배', '0차', '1차', '2차'], [['반감기', P('2배'), '그대로', '1/2배']]) +
    box('exam', '시험 포인트', '“0차 반응의 반감기는 초기 농도에 반비례한다” → <b>X</b> (비례). Summary 2 선택형: (<b>비례</b> / 반비례 / 무관).'))

# ---------------- 15 1차 ----------------
add('1차 반응과 1차 반감기 (빈칸 정답)', 'First-order reaction · half-life', 15,
    ['농도 1제곱에 비례', 'ln[A]<sub>t</sub> = −kt + ln[A]<sub>0</sub>', '[A]<sub>t</sub> = e<sup>−kt</sup>[A]<sub>0</sub>', 't<sub>1/2</sub> = 0.693/k'],
    '1차 반응은 속도가 반응물 농도의 1제곱에 비례한다. 적분하면 ln[A]<sub>t</sub> = −kt + ln[A]<sub>0</sub>, 지수형은 [A]<sub>t</sub> = e<sup>−kt</sup>[A]<sub>0</sub>. 반감기 t<sub>1/2</sub> = 0.693/k로 초기 농도와 무관하다.',
    f'<p>• <b>1차 반응 (First-order reaction)</b> : 반응 속도가 반응물 농도 {A("1제곱")}에 비례하는 반응</p>' +
    eq('−' + dAdt + ' = k[A]<sup>1</sup> → −k∫<sub>0</sub><sup>t</sup>dt = ∫ ' + F('1', '[A]') + 'd[A] → −kt = ln[A]<sub>t</sub> − ln[A]<sub>0</sub>',
       'ln[A]<sub>t</sub> = −kt + ln[A]<sub>0</sub> → ln[A]<sub>t</sub> = ln e<sup>−kt</sup> + ln[A]<sub>0</sub> → ' + A('[A]<sub>t</sub> = e<sup>−kt</sup>[A]<sub>0</sub>'),
       F('1', '2') + '[A]<sub>0</sub> = e<sup>−kt<sub>1/2</sub></sup>[A]<sub>0</sub> → ln' + F('1', '2') + ' = −kt<sub>1/2</sub> → t<sub>1/2</sub> = ' + F('ln 2', 'k') + ' = ' + A(F('0.693', 'k'))) +
    '<p style="color:#b91c1c"><b>즉, 1차 반응의 반감기는 초기 농도에 무관함!</b></p>' +
    '<p>그래프: [A]<sub>t</sub> vs t는 지수 감소 곡선 ([A]<sub>t</sub> = [A]<sub>0</sub>e<sup>−kt</sup>), ln[A]<sub>t</sub> vs t는 기울기 −k인 직선.</p>' +
    h4('반감기가 지날 때마다') + tbl(['경과', '남은 양'], [['1 t<sub>1/2</sub>', '50%'], ['2 t<sub>1/2</sub>', '25%'], ['3 t<sub>1/2</sub>', '12.5%'], ['n t<sub>1/2</sub>', '(1/2)<sup>n</sup>']]),
    tbl(['빈칸', '정답'], [['농도 ___에 비례', A('1제곱')], ['지수형', A('[A]<sub>t</sub> = e<sup>−kt</sup>[A]<sub>0</sub>')], ['반감기', A('t<sub>1/2</sub> = 0.693/k')]]) +
    h4('왜 초기 농도와 무관할까?') +
    '<p>1차는 매 순간 <b>남은 양의 일정 비율</b>이 사라져. 100 → 50에 걸리는 시간이나 50 → 25에 걸리는 시간이 같아. 그래서 출발 농도가 얼마든 반감기는 0.693/k 하나.</p>' +
    box('tip', '0.693', 'ln 2 = 0.693. 1차 반감기 식에만 나오는 숫자야. 0.693이 보이면 1차!') +
    box('exam', '시험 포인트', 'Summary 2: 1차는 (반응물)이 (<b>지수적</b>)으로 감소, 농도의 (<b>1</b>)제곱에 (<b>비례</b>), 반감기는 초기 농도에 (<b>무관</b>).'))

# ---------------- 16 2차 ----------------
add('2차 반응과 2차 반감기 (빈칸 정답)', 'Second-order reaction · half-life', 16,
    ['농도 2제곱에 비례', '1/[A]<sub>t</sub> = kt + 1/[A]<sub>0</sub>', 't<sub>1/2</sub> = 1/k[A]<sub>0</sub>', '초기 농도에 반비례'],
    '2차 반응은 속도가 반응물 농도의 2제곱에 비례한다. 적분하면 1/[A]<sub>t</sub> = kt + 1/[A]<sub>0</sub>, 반감기 t<sub>1/2</sub> = 1/(k[A]<sub>0</sub>)로 초기 농도에 반비례한다.',
    f'<p>• <b>2차 반응 (Second-order reaction)</b> : 반응 속도가 반응물 농도 {A("2제곱")}에 비례하는 반응</p>' +
    eq('−' + dAdt + ' = k[A]<sup>2</sup> → −k∫<sub>0</sub><sup>t</sup>dt = ∫ ' + F('1', '[A]<sup>2</sup>') + 'd[A] → −kt = −' + F('1', '[A]<sub>t</sub>') + ' + ' + F('1', '[A]<sub>0</sub>'),
       A(F('1', '[A]<sub>t</sub>') + ' = kt + ' + F('1', '[A]<sub>0</sub>')) + ' &nbsp; ([A]<sub>t</sub> = ' + F('[A]<sub>0</sub>', 'kt[A]<sub>0</sub> + 1') + ')',
       F('2', '[A]<sub>0</sub>') + ' = kt<sub>1/2</sub> + ' + F('1', '[A]<sub>0</sub>') + ' → ' + A('t<sub>1/2</sub> = ' + F('1', 'k[A]<sub>0</sub>'))) +
    '<p style="color:#b91c1c"><b>즉, 2차 반응의 반감기는 초기 농도에 반비례함!</b></p>' +
    '<p>그래프: 1/[A]<sub>t</sub> vs t는 y절편 1/[A]<sub>0</sub>, 기울기 = +k인 직선.</p>',
    tbl(['빈칸', '정답'], [['농도 ___에 비례', A('2제곱')], ['적분식', A('1/[A]<sub>t</sub> = kt + 1/[A]<sub>0</sub>')], ['반감기', A('t<sub>1/2</sub> = 1/k[A]<sub>0</sub>')]]) +
    h4('반감기 유도 포인트') + '<p>[A]<sub>t</sub> = ½[A]<sub>0</sub>을 넣으면 1/[A]<sub>t</sub> = <b>2</b>/[A]<sub>0</sub>. 2/[A]<sub>0</sub> − 1/[A]<sub>0</sub> = 1/[A]<sub>0</sub> = kt<sub>1/2</sub>.</p>' +
    h4('왜 반비례?') + '<p>2차는 농도가 높을수록 분자끼리 더 자주 부딪쳐 아주 빨리 반응해. 농도가 낮으면 만날 확률이 확 줄어 반감기가 길어져. 그래서 반감기가 지날 때마다 다음 반감기는 <b>2배씩 길어져</b>.</p>' +
    box('warn', '혼동 주의', '“[A]<sub>t</sub> = [A]<sub>0</sub>/(kt[A]<sub>0</sub> + 1)”은 y = c/(ax + b) 꼴 → [A] vs t는 <b>반비례 곡선</b>. Summary 2: 2차는 (직선 / <b>반비례</b>)(으)로 감소.') +
    box('exam', '시험 포인트', '반감기와 초기 농도: 0차 <b>비례</b> · 1차 <b>무관</b> · 2차 <b>반비례</b>. 식으로 보면 [A]<sub>0</sub>가 분자 · 없음 · 분모.'))

# ---------------- 17 차수 결정 그래프 ----------------
add('반응 차수의 결정 — 그래프법 (빈칸 정답)', 'Determining reaction order', 17,
    ['실험적으로 결정', '대입법 · 그래프법 · 반감기법', '직선이 되는 축 찾기'],
    '반응 차수는 실험 데이터로 결정하며, 대입법·그래프법·반감기법을 쓴다. 그래프법은 [A], ln[A], 1/[A]를 t에 대해 그려 어느 것이 직선인지 보는 방법이다.',
    ul(f'<b>반응 차수 결정</b>: 반응 차수는 실험적으로 결정하되 데이터를 기반으로 하여 {Y("대입법, 그래프법, 반감기법")} 등으로 차수를 최종 결정할 수 있음.') +
    tbl(['그래프', '0차', '1차', '2차'], [
        ['[A]<sub>t</sub> vs t', G('직선 (기울기 −k)'), '곡선 (지수 감소)', '곡선'],
        ['ln[A]<sub>t</sub> vs t', '곡선', G('직선 (기울기 −k)'), '곡선'],
        ['1/[A]<sub>t</sub> vs t', '곡선', '곡선', G('직선 (기울기 +k)')],
    ]) +
    '<p>원본 그림: Zero-order ([A]<sub>t</sub> 직선), 1st-order (ln[A] 직선 · [A] 곡선), 2nd-order (1/[A] 직선, y절편 1/[A]<sub>0</sub>). 파란 네모로 표시된 것이 각 그래프의 축 이름이야.</p>',
    tbl(['방법', '어떻게', '판단 기준'], [
        ['대입법', '데이터를 0·1·2차 적분식에 넣어 k 계산', 'k가 일정하게 나오는 차수'],
        ['그래프법', '[A], ln[A], 1/[A] vs t를 그림', G('직선이 되는 그래프')],
        ['반감기법', '초기 농도를 바꿔 반감기 측정', '비례 → 0차, 무관 → 1차, 반비례 → 2차'],
    ]) +
    box('tip', '외우기', '0차 → 그대로 [A], 1차 → ln[A], 2차 → 1/[A]. “그대로 · 로그 · 역수”.') +
    box('exam', '시험 포인트', '“반응 차수는 반응식의 계수로부터 이론적으로 결정한다” → <b>X</b>. 실험 데이터 + 대입법/그래프법/반감기법.'))

# ---------------- 18 차수 결정 예제 ----------------
add('반응 차수의 결정 — 아조메탄 분해 예제', 'Example: CH<sub>3</sub>−N=N−CH<sub>3</sub> → N<sub>2</sub> + C<sub>2</sub>H<sub>6</sub>', 18,
    ['ln P<sub>t</sub> vs t 직선', '1차 반응!', 'k = 2.55×10<sup>−3</sup> s<sup>−1</sup>'],
    '아조메탄의 부분 압력을 ln으로 바꿔 시간에 대해 그리면 직선 → 1차 반응. 기울기에서 k = 2.55×10<sup>−3</sup> s<sup>−1</sup>, y절편 ln[A]<sub>0</sub> = 5.649.',
    '<p style="text-align:center">CH<sub>3</sub>−N=N−CH<sub>3</sub>(g) → N<sub>2</sub>(g) + C<sub>2</sub>H<sub>6</sub>(g)</p>' +
    tbl(['시간 (t)', '부분 압력 (P<sub>t</sub>)', 'ln P<sub>t</sub>'], [
        ['0', '284', '5.649'], ['100', '220', '5.394'], ['150', '193', '5.263'], ['200', '170', '5.136'], ['250', '150', '5.011'], ['300', '132', '4.883']]) +
    eq('ln[A]<sub>t</sub> = −(2.55×10<sup>−3</sup>)t + 5.649 ↔ ln[A]<sub>t</sub> = −kt + ln[A]<sub>0</sub> → <span style="color:#b91c1c">1차 반응!</span>',
       'k = 2.55×10<sup>−3</sup> sec<sup>−1</sup>, &nbsp; ln[A]<sub>0</sub> = 5.649',
       '−' + F('d[CH<sub>3</sub>−N=N−CH<sub>3</sub>]', 'dt') + ' = k[CH<sub>3</sub>−N=N−CH<sub>3</sub>]<sup>1</sup>'),
    h4('풀이 (사고의 흐름)') + tbl(['단계', '내용'], [
        ['👀 단서', '표에 ln P<sub>t</sub>가 이미 계산돼 있음 → 1차 확인용'],
        ['🧮 기울기', '(4.883 − 5.649)/(300 − 0) = −0.766/300 = ' + G('−2.55×10<sup>−3</sup>')],
        ['🔍 직선 확인', '구간마다 기울기: (5.394−5.649)/100 = −2.55×10<sup>−3</sup>, (5.263−5.394)/50 = −2.62×10<sup>−3</sup> … 거의 일정 → 직선'],
        ['💡 결론', 'ln P vs t 직선 = ' + G('1차') + ', k = |기울기| = 2.55×10<sup>−3</sup> s<sup>−1</sup>'],
        ['➕ 반감기', 't<sub>1/2</sub> = 0.693/k = 0.693/(2.55×10<sup>−3</sup>) ≈ ' + G('272 s')],
    ]) +
    '<p><b>왜 압력으로 해도 되나?</b> 기체는 PV = nRT라서 부분 압력이 농도에 비례해. ln P와 ln[A]는 상수만큼만 차이 나서 기울기(−k)가 같아.</p>' +
    box('warn', '혼동 주의', 'k 단위가 sec<sup>−1</sup>인 것도 1차라는 증거야. (0차 mol/L·s, 2차 L/mol·s)'))

# ---------------- 19 요약표 ----------------
add('화학 반응 속도 0~2차 반응 요약 (빈칸 정답)', 'Summary table of 0th, 1st, 2nd order', 19,
    ['반응물 소비 = 생성물 생성', '속도식 · 적분식', '반감기 · k 단위'],
    '반응 속도 = 반응물이 소비되는 속도 = 생성물이 생성되는 속도. 0·1·2차의 속도식, 적분식, 반감기, k 단위를 한 표로 정리한다.',
    ul(f'반응 속도 = ( {A("반응물")} )이 소비되는 속도 = ( {A("생성물")} )이 생성되는 속도') +
    '<p style="text-align:center">aA + bB → cC + dD → Reaction rate = k[A]<sup>x</sup>[B]<sup>y</sup></p>' +
    tbl(['차수', '속도식', '적분식', '반감기', 'k 단위'], [
        ['0차', '−d[A]/dt = k', '[A]<sub>t</sub> = −kt + [A]<sub>0</sub>', '[A]<sub>0</sub>/2k', 'mol/L·sec'],
        ['1차', '−d[A]/dt = k[A]<sup>1</sup>', 'ln[A]<sub>t</sub> = −kt + ln[A]<sub>0</sub>', '0.693/k', 'sec<sup>−1</sup>'],
        ['2차', '−d[A]/dt = k[A]<sup>2</sup>', '1/[A]<sub>t</sub> = kt + 1/[A]<sub>0</sub>', '1/k[A]<sub>0</sub>', 'L/sec·mol'],
    ]),
    tbl(['비교', '0차', '1차', '2차'], [
        ['[A] vs t 모양', '직선', '지수 곡선', '반비례 곡선'],
        ['직선이 되는 축', '[A]', 'ln[A]', '1/[A]'],
        ['기울기', '−k', '−k', '+k'],
        ['반감기 vs [A]<sub>0</sub>', P('비례'), P('무관'), P('반비례')],
        ['속도 vs [A]', '무관 (일정)', '[A]에 비례', '[A]²에 비례'],
        ['예', 'N<sub>2</sub>O/Pt, 현탁액', '대부분의 약물 분해', '두 분자 충돌'],
    ]) +
    box('tip', '빈칸 정답', '첫 줄 괄호 = ' + A('반응물') + ' / ' + A('생성물') + '. 소비되는 건 반응물, 생성되는 건 생성물.') +
    box('exam', '시험 포인트', '이 표는 Summary 2의 빈칸(0차 적분식, 1차 반감기, 2차 적분식)과 그대로 연결돼. 한 칸씩 가리고 써 보기.'))

# ---------------- 20 복합 반응 ----------------
add('복합 반응 — 종류와 가역 반응 (빈칸 정답)', 'Complex reactions · Reversible reaction', 20,
    ['Complex reaction', '가역 · 평행 · 연속', 'A ⇄ B', '정·역반응 모두 1차'],
    '0·1·2·3차 같은 단순 식으로 표시할 수 없는 반응이 복합 반응(가역·평행·연속)이다. 가역 반응은 A가 B가 되면서 일부 B가 다시 A로 돌아가는 반응이고, 정반응·역반응을 모두 1차로 가정해 식을 세운다.',
    h4('복합 반응 (Complex reaction)') +
    f'<p>0, 1, 2, 3차 등의 반응식으로 표시할 수 없는 경우 : {Y("가역 반응, 평행 반응, 연속 반응")}</p>' +
    h4('가역 반응 (Reversible reaction)') +
    f'<p>{Y("A가 B를 형성하면서 일부 B는 다시 A로 되돌아가는 현상")}, A와 B 사이의 평형을 나타내기까지의 과정을 표현하기 위한 목적임. 정반응과 역반응이 모두 {A("1차")}라 가정하면,</p>' +
    eq('A ⇄ B (정반응 k<sub>f</sub>, 역반응 k<sub>r</sub>)',
       F('dA', 'dt') + ' = −Ak<sub>f</sub> + Bk<sub>r</sub>, &nbsp; A<sub>0</sub> − A = B (A<sub>0</sub>: t = 0에서의 A 초기 농도)'),
    tbl(['빈칸', '정답', '이유'], [['정반응과 역반응이 모두 ___라 가정', A('1차'), '−Ak<sub>f</sub>, +Bk<sub>r</sub> 모두 농도의 1제곱']]) +
    h4('식 읽기') + tbl(['항', '의미'], [
        ['−Ak<sub>f</sub>', 'A가 B로 가며 줄어드는 속도 (정반응, forward)'],
        ['+Bk<sub>r</sub>', 'B가 A로 돌아오며 A가 늘어나는 속도 (역반응, reverse)'],
        ['A<sub>0</sub> − A = B', '처음엔 A만 있었으니, 줄어든 A만큼 B가 생김 (물질 보존)'],
    ]) +
    tbl(['복합 반응', '모양'], [['가역', 'A ⇄ B'], ['평행', 'P → A, P → N (동시에)'], ['연속', 'A → C → D (차례로)']]) +
    box('exam', '시험 포인트', 'Summary 3: A가 B를 형성하면서 일부 (A/<b>B</b>)는 다시 (<b>A</b>/B)로 되돌아가는 현상. 방향 바꾸기 함정 주의.'))

# ---------------- 21 가역 유도 ----------------
add('복합 반응 (가역 반응) — 적분식 유도 (빈칸 정답)', 'Reversible reaction: derivation (식1)', 21,
    ['B = A<sub>0</sub> − A 대입', 'f(A) = A(k<sub>f</sub>+k<sub>r</sub>) − A<sub>0</sub>k<sub>r</sub>', '∫dx/(ax+b)', '식1'],
    'B = A<sub>0</sub> − A를 대입해 A만의 식으로 만들고, ∫dx/(ax+b) 공식으로 적분하면 식1: ln[A<sub>0</sub>k<sub>f</sub> / (A(k<sub>f</sub>+k<sub>r</sub>) − A<sub>0</sub>k<sub>r</sub>)] = (k<sub>f</sub> + k<sub>r</sub>)t.',
    eq(F('dA', 'dt') + ' = −Ak<sub>f</sub> + Bk<sub>r</sub>, &nbsp; A<sub>0</sub> − A = B',
       F('dA', 'dt') + ' = −Ak<sub>f</sub> + (A<sub>0</sub> − A)k<sub>r</sub> = A<sub>0</sub>k<sub>r</sub> − A(k<sub>f</sub> + k<sub>r</sub>)',
       F('dA', 'A(k<sub>f</sub>+k<sub>r</sub>) − A<sub>0</sub>k<sub>r</sub>') + ' = −dt, &nbsp; f(A) = A(k<sub>f</sub>+k<sub>r</sub>) − A<sub>0</sub>k<sub>r</sub>',
       '∫<sub>A0</sub><sup>A</sup> ' + F('dA', 'f(A)') + ' = −∫<sub>0</sub><sup>t</sup>dt, &nbsp; ∫' + F('dx', 'ax+b') + ' = ' + F('1', 'a') + 'ln(ax+b)',
       F('1', "f′(A)") + '[ln f(A) − ln f(A<sub>0</sub>)] = −t → ln' + F('f(A<sub>0</sub>)', 'f(A)') + " = f′(A)t",
       '<b>식1</b>: ln' + F('A<sub>0</sub>k<sub>f</sub>', 'A(k<sub>f</sub>+k<sub>r</sub>) − A<sub>0</sub>k<sub>r</sub>') + ' = ( ' + A('k<sub>f</sub> + k<sub>r</sub>') + ' )t'),
    tbl(['빈칸', '정답', '이유'], [['식1 오른쪽 괄호', A('k<sub>f</sub> + k<sub>r</sub>'), "f′(A) = d/dA[A(k<sub>f</sub>+k<sub>r</sub>) − A<sub>0</sub>k<sub>r</sub>] = k<sub>f</sub> + k<sub>r</sub>"]]) +
    h4('유도 핵심 3단계') + tbl(['단계', '내용'], [
        ['💡 B 없애기', 'B = A<sub>0</sub> − A → 식에 A만 남김'],
        ['🧮 적분 공식', 'f(A)는 A에 대한 1차식(a = k<sub>f</sub>+k<sub>r</sub>, b = −A<sub>0</sub>k<sub>r</sub>) → ∫dx/(ax+b) = (1/a)ln(ax+b)'],
        ['🔍 f(A<sub>0</sub>) 계산', 'f(A<sub>0</sub>) = A<sub>0</sub>(k<sub>f</sub>+k<sub>r</sub>) − A<sub>0</sub>k<sub>r</sub> = ' + G('A<sub>0</sub>k<sub>f</sub>') + ' → 식1의 분자'],
    ]) +
    box('tip', '포인트', '가역 반응에서 측정되는 속도 상수는 k<sub>f</sub> 하나가 아니라 <b>k<sub>f</sub> + k<sub>r</sub></b>(합)이야. 평형으로 다가가는 빠르기는 정·역반응을 합친 값으로 정해져.'))

# ---------------- 22 평형 ----------------
add('복합 반응 (가역 반응) — 평형 상태 (빈칸 정답)', 'Reversible reaction at equilibrium (식2, 식3)', 22,
    ['평형: dA/dt = 0', 'A<sub>eq</sub>k<sub>f</sub> = B<sub>eq</sub>k<sub>r</sub>', 'A<sub>eq</sub> = k<sub>r</sub>A<sub>0</sub>/(k<sub>f</sub>+k<sub>r</sub>)', '식2 · 식3'],
    '평형에서는 A가 더 이상 변하지 않으므로 dA/dt = 0. 여기서 A<sub>eq</sub>k<sub>f</sub> = B<sub>eq</sub>k<sub>r</sub>, 식2 A<sub>eq</sub> = k<sub>r</sub>A<sub>0</sub>/(k<sub>f</sub>+k<sub>r</sub>), 식3 A<sub>0</sub> − A<sub>eq</sub> = (k<sub>f</sub>/k<sub>r</sub>)A<sub>eq</sub>를 얻어 식1에 넣는다.',
    f'<p>반응이 {Y("평형 상태")}에 이르렀다면,</p>' +
    eq(F('dA', 'dt') + ' = −Ak<sub>f</sub> + Bk<sub>r</sub> = ' + A('0'),
       'A<sub>eq</sub>k<sub>f</sub> = B<sub>eq</sub>k<sub>r</sub> ← A<sub>0</sub> − A<sub>eq</sub> = B<sub>eq</sub> → A<sub>eq</sub>k<sub>f</sub> = (A<sub>0</sub> − A<sub>eq</sub>)k<sub>r</sub>',
       '<b>식2</b>: A<sub>eq</sub> = ' + F('k<sub>r</sub>', 'k<sub>f</sub> + k<sub>r</sub>') + 'A<sub>0</sub>',
       'A<sub>0</sub> = ' + F('k<sub>f</sub> + k<sub>r</sub>', 'k<sub>r</sub>') + 'A<sub>eq</sub> = A<sub>eq</sub> + ' + F('k<sub>f</sub>', 'k<sub>r</sub>') + 'A<sub>eq</sub> → <b>식3</b>: A<sub>0</sub> − A<sub>eq</sub> = ' + F('k<sub>f</sub>', 'k<sub>r</sub>') + 'A<sub>eq</sub>') +
    '<p><b>식1</b> ln' + F('A<sub>0</sub>k<sub>f</sub>', 'A(k<sub>f</sub>+k<sub>r</sub>) − A<sub>0</sub>k<sub>r</sub>') + ' = (k<sub>f</sub>+k<sub>r</sub>)t → 분자·분모를 (k<sub>f</sub>+k<sub>r</sub>)로 나누면 ln' + F('A<sub>0</sub>k<sub>f</sub>/(k<sub>f</sub>+k<sub>r</sub>)', 'A − A<sub>0</sub>k<sub>r</sub>/(k<sub>f</sub>+k<sub>r</sub>)') + ' = (k<sub>f</sub>+k<sub>r</sub>)t</p>',
    tbl(['빈칸', '정답', '이유'], [['평형에서 dA/dt = ___', A('0'), '정반응 속도 = 역반응 속도 → A 변화 없음']]) +
    h4('왜 이 식들이 필요하나?') +
    '<p>식1에는 A<sub>0</sub>k<sub>r</sub>/(k<sub>f</sub>+k<sub>r</sub>) 같은 복잡한 덩어리가 있어. 식2를 보면 이게 바로 ' + G('A<sub>eq</sub>') + '! 그리고 A<sub>0</sub>k<sub>f</sub>/(k<sub>f</sub>+k<sub>r</sub>) = A<sub>0</sub> − A<sub>eq</sub>. 이렇게 바꾸면 식이 측정 가능한 농도(A<sub>0</sub>, A, A<sub>eq</sub>)만으로 깔끔해져 (다음 슬라이드).</p>' +
    box('warn', '혼동 주의', '평형 = 반응이 <b>멈춘</b> 게 아니라 정반응과 역반응 속도가 <b>같아진</b> 상태. A<sub>eq</sub>k<sub>f</sub> = B<sub>eq</sub>k<sub>r</sub>는 “속도가 같다”는 뜻이지 “농도가 같다”는 뜻이 아니야.') +
    box('tip', '식2 체크', 'k<sub>r</sub>이 크면(역반응이 강하면) A<sub>eq</sub>가 A<sub>0</sub>에 가까워짐 → 말이 됨.'))

# ---------------- 23 가역 최종 ----------------
add('복합 반응 (가역 반응) — 최종식과 k<sub>f</sub>, k<sub>r</sub> 구하기', 'Reversible reaction: final form & graph', 23,
    ['ln[(A<sub>0</sub>−A<sub>eq</sub>)/(A−A<sub>eq</sub>)]', '기울기 = (k<sub>f</sub>+k<sub>r</sub>)/2.303', 'K = B<sub>eq</sub>/A<sub>eq</sub> = k<sub>f</sub>/k<sub>r</sub>', '연립방정식'],
    '식2·식3을 식1에 넣으면 ln[(A<sub>0</sub>−A<sub>eq</sub>)/(A−A<sub>eq</sub>)] = (k<sub>f</sub>+k<sub>r</sub>)t. log로 그린 그래프의 기울기 (k<sub>f</sub>+k<sub>r</sub>)/2.303과 평형상수 K = B<sub>eq</sub>/A<sub>eq</sub> = k<sub>f</sub>/k<sub>r</sub>을 연립하면 k<sub>f</sub>, k<sub>r</sub>을 각각 구할 수 있다.',
    eq('식3: A<sub>0</sub> − A<sub>eq</sub> = ' + F('k<sub>f</sub>', 'k<sub>r</sub>') + 'A<sub>eq</sub>, &nbsp; 식2: A<sub>eq</sub> = ' + F('k<sub>r</sub>', 'k<sub>f</sub>+k<sub>r</sub>') + 'A<sub>0</sub>',
       'ln' + F('(k<sub>f</sub>/k<sub>r</sub>)A<sub>eq</sub>', 'A − A<sub>eq</sub>') + ' = (k<sub>f</sub>+k<sub>r</sub>)t → ' + G('ln' + F('A<sub>0</sub> − A<sub>eq</sub>', 'A − A<sub>eq</sub>') + ' = (k<sub>f</sub>+k<sub>r</sub>)t'),
       G('log' + F('A<sub>0</sub> − A<sub>eq</sub>', 'A − A<sub>eq</sub>') + ' = ' + F('(k<sub>f</sub>+k<sub>r</sub>)t', '2.303'))) +
    '<p style="color:#b91c1c"><b>실험적으로 구할 수 있는 값:</b></p>' +
    tbl(['값', '어디서'], [
        ['그래프의 기울기 = ' + F('k<sub>f</sub> + k<sub>r</sub>', '2.303'), 'log[(A<sub>0</sub>−A<sub>eq</sub>)/(A−A<sub>eq</sub>)] vs Time 직선'],
        ['K = ' + F('B<sub>eq</sub>', 'A<sub>eq</sub>') + ' = ' + F('k<sub>f</sub>', 'k<sub>r</sub>'), '평형 농도 측정'],
    ]) +
    '<p style="color:#b91c1c">두 식을 연립방정식으로 하면 k<sub>f</sub>, k<sub>r</sub>를 구할 수 있음.</p>',
    h4('연립 풀이 예시') + tbl(['단계', '내용'], [
        ['🧮 그래프', '기울기 × 2.303 = k<sub>f</sub> + k<sub>r</sub> (합)'],
        ['🧮 평형', 'K = k<sub>f</sub>/k<sub>r</sub> (비)'],
        ['💡 연립', 'k<sub>r</sub> = (k<sub>f</sub>+k<sub>r</sub>)/(K+1), &nbsp; k<sub>f</sub> = K·k<sub>r</sub>'],
        ['예', '합 = 0.03 min<sup>−1</sup>, K = 2 → k<sub>r</sub> = 0.01, k<sub>f</sub> = 0.02 min<sup>−1</sup>'],
    ]) +
    '<p><b>1차와 비교</b>: 1차의 ln(A<sub>0</sub>/A) = kt에서 A 대신 “평형까지 남은 거리” (A − A<sub>eq</sub>)를 쓴 꼴이야. 가역 반응은 0이 아니라 <b>A<sub>eq</sub>를 향해</b> 1차처럼 다가가.</p>' +
    box('warn', '혼동 주의', '그래프 기울기는 k<sub>f</sub> 하나가 아니라 <b>(k<sub>f</sub> + k<sub>r</sub>)/2.303</b>. ln으로 그리면 2.303 없이 k<sub>f</sub> + k<sub>r</sub>.') +
    box('exam', '시험 포인트', 'K = B<sub>eq</sub>/A<sub>eq</sub> = k<sub>f</sub>/k<sub>r</sub>. 분자·분모 뒤집기(k<sub>r</sub>/k<sub>f</sub>) 함정 주의.'))

# ---------------- 24 평행 1 ----------------
add('복합 반응 (평행 반응) — 정의', 'Parallel reaction', 24,
    ['Parallel reaction', '동시에 2가지 이상 생성', '약학에서 흔함', 'k = k<sub>1</sub> + k<sub>2</sub>'],
    '평행 반응은 한 물질(P)에서 동시에 두 가지 이상의 물질(A, N)이 생성되는 반응으로 약학에서 흔하다. P의 감소 속도는 dP/dt = −(k<sub>1</sub>+k<sub>2</sub>)P = −kP로 1차 반응과 같다.',
    h4('평행반응 (Parallel reaction)') +
    f'<p>한 가지 물질에서 {Y("동시에")} {Y("두 가지 이상의 물질이 생성")}되는 반응으로 약학에서 흔히 일어나는 반응 중 하나임.</p>' +
    eq('P →(k<sub>1</sub>) A, &nbsp; P →(k<sub>2</sub>) N',
       F('dP', 'dt') + ' = −Pk<sub>1</sub> − Pk<sub>2</sub> = −kP &nbsp; (k<sub>1</sub> + k<sub>2</sub> = k)'),
    '<p>(이 슬라이드에는 빈칸이 없어.)</p>' +
    h4('왜 k = k<sub>1</sub> + k<sub>2</sub>?') +
    '<p>P는 두 갈래 길로 동시에 빠져나가. 출구가 두 개인 수조처럼 빠지는 속도는 두 출구의 합이야. 그래서 P 입장에서는 속도 상수 k = k<sub>1</sub> + k<sub>2</sub>인 <b>1차 반응</b>.</p>' +
    tbl(['비교', '평행 반응', '연속 반응'], [
        ['모양', 'P → A, P → N (갈라짐)', 'A → C → D (이어짐)'],
        ['핵심 단어', P('동시에'), '차례로 (중간체 C)'],
    ]) +
    box('tip', '약학 예', '하나의 약이 가수분해와 산화로 동시에 분해되는 경우, 또는 한 약이 두 가지 대사체로 동시에 대사되는 경우.') +
    box('exam', '시험 포인트', 'Summary 3: 한 가지 물질에서 (연속으로/<b>동시</b>)에 두 가지 이상의 물질이 생성. “연속으로”는 함정!'))

# ---------------- 25 평행 2 ----------------
add('복합 반응 (평행 반응) — A, N 농도 유도', 'Parallel reaction: product concentrations', 25,
    ['P = P<sub>0</sub>e<sup>−kt</sup>', 'dA/dt = k<sub>1</sub>P', 'A = (k<sub>1</sub>/k)P<sub>0</sub>(1−e<sup>−kt</sup>)', 'N = (k<sub>2</sub>/k)P<sub>0</sub>(1−e<sup>−kt</sup>)'],
    'P는 1차로 줄어 P = P<sub>0</sub>e<sup>−kt</sup>. 생성물 A는 dA/dt = k<sub>1</sub>P로 생기므로 적분하면 A = (k<sub>1</sub>/k)P<sub>0</sub>(1 − e<sup>−kt</sup>), N = (k<sub>2</sub>/k)P<sub>0</sub>(1 − e<sup>−kt</sup>).',
    eq(F('dP', 'dt') + ' = −Pk<sub>1</sub> − Pk<sub>2</sub> = −kP (k<sub>1</sub>+k<sub>2</sub> = k) → ln' + F('P<sub>0</sub>', 'P') + ' = kt → P = P<sub>0</sub>e<sup>−kt</sup>',
       F('dA', 'dt') + ' = Pk<sub>1</sub> = k<sub>1</sub>P<sub>0</sub>e<sup>−kt</sup> → ∫<sub>A0</sub><sup>A</sup>dA = k<sub>1</sub>P<sub>0</sub>∫<sub>0</sub><sup>t</sup>e<sup>−kt</sup>dt → A − A<sub>0</sub> = −' + F('k<sub>1</sub>', 'k') + 'P<sub>0</sub>(e<sup>−kt</sup> − 1)',
       G('A = ' + F('k<sub>1</sub>', 'k') + 'P<sub>0</sub>(1 − e<sup>−kt</sup>)') + ' &nbsp; ' + G('N = ' + F('k<sub>2</sub>', 'k') + 'P<sub>0</sub>(1 − e<sup>−kt</sup>)')) +
    '<p>(A<sub>0</sub> = 0, 처음엔 생성물이 없다고 둠)</p>',
    h4('식 해석') + tbl(['포인트', '의미'], [
        ['(1 − e<sup>−kt</sup>)', '반응한 P의 비율. t = 0 → 0, t → ∞ → 1'],
        ['k<sub>1</sub>/k', 'P가 A 쪽으로 가는 몫 (분기 비율)'],
        ['t → ∞', 'A = (k<sub>1</sub>/k)P<sub>0</sub>, N = (k<sub>2</sub>/k)P<sub>0</sub>'],
        ['A/N', G('= k<sub>1</sub>/k<sub>2</sub> (언제나 일정!)')],
    ]) +
    '<p><b>비유</b>: 갈림길에서 사람들이 70:30으로 나뉘면, 언제 세어 봐도 A 쪽:N 쪽 = 7:3. 총 몇 명이 지나갔는지만 시간에 따라 늘어나.</p>' +
    box('warn', '혼동 주의', '∫<sub>0</sub><sup>t</sup>e<sup>−kt</sup>dt = −(1/k)(e<sup>−kt</sup> − 1) — 슬라이드 2 기초 수학이 여기서 쓰여. 결과의 k는 k<sub>1</sub>이 아니라 <b>전체 k = k<sub>1</sub>+k<sub>2</sub></b>.'))

# ---------------- 26 평행 k1 k2 ----------------
add('복합 반응 (평행 반응) — 실험적으로 k<sub>1</sub>, k<sub>2</sub> 구하기 (빈칸 정답)', 'Parallel reaction: determining k<sub>1</sub>, k<sub>2</sub>', 26,
    ['y축: A 또는 N', 'x축: 1 − e<sup>−kt</sup>', '기울기 = (k<sub>1</sub>/k)P<sub>0</sub>', 'k<sub>2</sub> = k − k<sub>1</sub>'],
    'A(또는 N) 농도를 y축, (1 − e<sup>−kt</sup>)를 x축으로 그리면 직선이고 기울기 = (k<sub>1</sub>/k)P<sub>0</sub>. k와 P<sub>0</sub>를 알면 k<sub>1</sub> = 기울기 × k/P<sub>0</sub>, k<sub>2</sub> = k − k<sub>1</sub>.',
    h4('실험적으로 k<sub>1</sub>, k<sub>2</sub> 구하기') +
    f'<p>: 생성된 {Y("A 또는 N 물질의 농도를 Y축")}으로 하고, {Y("1 − e<sup>−kt</sup>를 x축")}으로 하는 그래프를 그린 뒤 {A("기울기")}를 구한다. k 값과 P<sub>0</sub> 값을 알고 있다고 할 때,</p>' +
    eq('A = ' + F('k<sub>1</sub>', 'k') + 'P<sub>0</sub>(1 − e<sup>−kt</sup>) &nbsp; N = ' + F('k<sub>2</sub>', 'k') + 'P<sub>0</sub>(1 − e<sup>−kt</sup>)',
       '기울기 = ' + F('k<sub>1</sub>', 'k') + 'P<sub>0</sub> → k<sub>1</sub> = 기울기 × ' + F('k', 'P<sub>0</sub>') + ', &nbsp; k<sub>2</sub> = k − k<sub>1</sub>') +
    '<p>그래프: x축 (1 − e<sup>−kt</sup>), y축 A, N. 기울기 (k<sub>1</sub>/k)P<sub>0</sub>인 직선과 (k<sub>2</sub>/k)P<sub>0</sub>인 직선.</p>',
    tbl(['빈칸', '정답', '포인트'], [['그래프를 그린 뒤 ___를 구한다', A('기울기'), 'Summary 3에서도 k<sub>1</sub> = ' + A('기울기') + ' × k/P<sub>0</sub>']]) +
    h4('순서 (사고의 흐름)') + tbl(['단계', '내용'], [
        ['1', 'P의 감소를 측정 → ln P vs t 기울기로 전체 ' + G('k') + ' 구함 (1차)'],
        ['2', '각 시간의 (1 − e<sup>−kt</sup>) 계산 → x값'],
        ['3', 'A 농도 vs (1 − e<sup>−kt</sup>) 직선의 기울기 = (k<sub>1</sub>/k)P<sub>0</sub>'],
        ['4', G('k<sub>1</sub> = 기울기 × k/P<sub>0</sub>')],
        ['5', G('k<sub>2</sub> = k − k<sub>1</sub>')],
    ]) +
    box('tip', '왜 x축이 (1 − e<sup>−kt</sup>)?', 'A = (상수) × (1 − e<sup>−kt</sup>) 꼴이라 x를 (1 − e<sup>−kt</sup>)로 잡으면 y = ax 직선(원점 통과)이 돼.') +
    box('warn', '혼동 주의', 'x축은 t가 아니라 <b>1 − e<sup>−kt</sup></b>. y축은 P가 아니라 <b>생성물 A 또는 N</b>.'))

# ---------------- 27 정류 상태 ----------------
add('정류 상태 근사법 (Steady-state approximation)', 'Steady-state approximation', 27,
    ['중간 생성물 = 일정', 'dC/dt = 0', 'C = k<sub>1</sub>AB/(k<sub>2</sub>+k<sub>3</sub>)', '연속 1차 반응 가정'],
    '여러 단계 반응에서 중간 생성물 농도가 일정하다고 가정할 수 있을 때 쓰는 방법이 정류 상태 근사법이다. dC/dt = 0으로 두면 중간체 농도 C = k<sub>1</sub>AB/(k<sub>2</sub>+k<sub>3</sub>)로 간단히 표현된다.',
    h4('정류 상태 근사법 (Steady-state approximation)') +
    f'<p>여러 단계로 이루어진 반응에서 {Y("중간 단계 생성물이 반응에 있어서 일정하다고 가정")}할 수 있을 때, 이를 정류 상태 근사법이라고 함. {Y("연속 1차 반응을 가정")}하면, 중간 반응물 농도를 다음과 같이 간단히 표현 가능함.</p>' +
    eq('A + B ⇄ C → D &nbsp; (정 k<sub>1</sub>, 역 k<sub>2</sub>, 다음 단계 k<sub>3</sub>)',
       F('dC', 'dt') + ' = k<sub>1</sub>AB − k<sub>2</sub>C − k<sub>3</sub>C = 0 (정류상태라면)',
       G('C = ' + F('k<sub>1</sub>', 'k<sub>2</sub> + k<sub>3</sub>') + 'AB')),
    '<p>(이 슬라이드에는 빈칸이 없어.)</p>' +
    h4('dC/dt 식 읽기') + tbl(['항', '의미'], [
        ['+k<sub>1</sub>AB', 'A와 B가 만나 C가 생김'],
        ['−k<sub>2</sub>C', 'C가 다시 A + B로 돌아감'],
        ['−k<sub>3</sub>C', 'C가 D(최종 생성물)로 감'],
        ['= 0', '생기는 속도 = 없어지는 속도 → C 농도 일정'],
    ]) +
    box('tip', '비유', '정류 상태 = 물이 들어오는 만큼 빠져나가는 욕조. 수위(C)는 일정하지만 물은 계속 흐르고 있어.') +
    box('warn', '혼동 주의', '정류 상태(steady state) ≠ 평형(equilibrium). 정류 상태는 <b>중간체</b> 농도만 일정하고 반응은 D 쪽으로 계속 진행 중. (확산 단원의 정상상태 ↔ 평형 구별과 같은 함정)') +
    box('exam', '시험 포인트', 'Summary 4: 중간 단계 생성물이 반응에 있어서 (증가/<b>일정</b>)하다고 가정.'))

# ---------------- 28 MM 정의 ----------------
add('정류 상태 근사법 — Michaelis-Menten식', 'Michaelis-Menten: enzyme–substrate complex', 28,
    ['기질 S · 효소 E', '효소-기질 복합체 E·S', '다단계 반응', '중간 산물 = 정류 상태'],
    'Michaelis-Menten식은 기질 S와 효소 E가 효소-기질 복합체(E·S)를 거쳐 생성물 P를 만드는 다단계 반응에서, 중간 산물(E·S)을 정류 상태로 가정해 반응 속도를 구한 식이다.',
    h4('Michaelis-Menten식') +
    f'<p>기질 S(substrate)와 효소 E(Enzyme)의 반응을 통해 최종적으로 생성물 P(Product)를 만드는 {Y("다단계")} 반응에서 {Y("중간 산물을 정류 상태로 가정")}할 때 반응 속도를 구하는 식.</p>' +
    eq('E + S ⇄ (E·S) → P &nbsp; (k<sub>1</sub>, k<sub>2</sub>, k<sub>3</sub>)',
       F('d(E·S)', 'dt') + ' = k<sub>1</sub>ES − k<sub>2</sub>(E·S) − k<sub>3</sub>(E·S) = 0 (정류상태라면)',
       G('(E·S) = ' + F('k<sub>1</sub>', 'k<sub>2</sub> + k<sub>3</sub>') + 'ES')) +
    '<p>그림: 효소(E) + 기질(S) → 효소-기질 복합체(E·S) → 효소 + 생성물(P: C + D)</p>',
    '<p>(이 슬라이드에는 빈칸이 없어.)</p>' +
    tbl(['정류 상태 근사법 (27)', 'Michaelis-Menten (28)'], [
        ['A + B ⇄ C → D', 'E + S ⇄ (E·S) → P'],
        ['중간체 C', '중간체 (E·S)'],
        ['C = k<sub>1</sub>AB/(k<sub>2</sub>+k<sub>3</sub>)', '(E·S) = k<sub>1</sub>ES/(k<sub>2</sub>+k<sub>3</sub>)'],
    ]) +
    '<p>앞 슬라이드의 일반식에 A → E, B → S, C → (E·S), D → P를 넣은 것과 똑같아.</p>' +
    box('tip', '비유', '효소 = 자물쇠, 기질 = 열쇠. 열쇠가 꽂힌 상태(E·S)를 거쳐 생성물이 나오고, 효소는 다시 빈 자물쇠로 돌아가 재사용돼.') +
    box('exam', '시험 포인트', 'Summary 4: (단일/<b>다단계</b>) 반응에서 (최종/<b>중간</b>) 산물을 정류 상태로 가정. “최종 산물”은 함정!'))

# ---------------- 29 MM 유도 ----------------
add('Michaelis-Menten식과 Lineweaver-Burk식 — (E·S) 유도', 'Deriving (E·S) and K<sub>m</sub>', 29,
    ['E<sub>0</sub> = E + (E·S)', 'E = E<sub>0</sub> − (E·S)', '(E·S) = SE<sub>0</sub>/(K<sub>m</sub>+S)', 'K<sub>m</sub> = (k<sub>2</sub>+k<sub>3</sub>)/k<sub>1</sub>'],
    '자유 효소 E는 측정하기 어려우므로 총 효소 농도 E<sub>0</sub> = E + (E·S)를 써서 E를 없앤다. 정리하면 (E·S) = SE<sub>0</sub>/(K<sub>m</sub>+S), K<sub>m</sub> = (k<sub>2</sub>+k<sub>3</sub>)/k<sub>1</sub>.',
    eq('E + S ⇄ (E·S) → P, &nbsp; E<sub>0</sub>(Enzyme의 총 농도) = E + (E·S) → E = E<sub>0</sub> − (E·S)',
       '(E·S) = ' + F('k<sub>1</sub>', 'k<sub>2</sub>+k<sub>3</sub>') + 'ES = ' + F('k<sub>1</sub>S(E<sub>0</sub> − (E·S))', 'k<sub>2</sub>+k<sub>3</sub>'),
       '(k<sub>2</sub>+k<sub>3</sub>)(E·S) = k<sub>1</sub>SE<sub>0</sub> − k<sub>1</sub>S(E·S)',
       '(k<sub>2</sub>+k<sub>3</sub> + Sk<sub>1</sub>)(E·S) = k<sub>1</sub>SE<sub>0</sub>',
       '(E·S) = ' + F('k<sub>1</sub>SE<sub>0</sub>', '(k<sub>2</sub>+k<sub>3</sub>) + Sk<sub>1</sub>') + ' = ' + F('SE<sub>0</sub>', '(k<sub>2</sub>+k<sub>3</sub>)/k<sub>1</sub> + S'),
       G('(E·S) = ' + F('SE<sub>0</sub>', 'K<sub>m</sub> + S')) + ', &nbsp; ' + G('K<sub>m</sub> = ' + F('k<sub>2</sub>+k<sub>3</sub>', 'k<sub>1</sub>'))),
    '<p>(이 슬라이드에는 빈칸이 없어.)</p>' +
    h4('유도 핵심') + tbl(['단계', '내용'], [
        ['💡 E 없애기', '자유 효소 E는 모름 → E = E<sub>0</sub> − (E·S) 대입'],
        ['🧮 (E·S) 모으기', '(E·S)가 들어간 항을 왼쪽으로: (k<sub>2</sub>+k<sub>3</sub>+k<sub>1</sub>S)(E·S) = k<sub>1</sub>SE<sub>0</sub>'],
        ['🧮 k<sub>1</sub>로 나누기', '분자·분모를 k<sub>1</sub>로 나누면 K<sub>m</sub>이 등장'],
    ]) +
    h4('K<sub>m</sub>의 의미') + '<p>K<sub>m</sub> = (k<sub>2</sub>+k<sub>3</sub>)/k<sub>1</sub> = (E·S가 깨지는 속도)/(E·S가 생기는 속도). <b>K<sub>m</sub>이 작을수록</b> 효소-기질 복합체가 잘 생기고 오래 유지 → 효소와 기질의 <b>친화력이 크다</b>. 단위는 농도(mol/L).</p>' +
    box('warn', '혼동 주의', 'K<sub>m</sub> = (k<sub>2</sub>+k<sub>3</sub>)/k<sub>1</sub>. 분자·분모 위치 바꾸기(k<sub>1</sub>/(k<sub>2</sub>+k<sub>3</sub>)) 함정 주의 — 그건 (E·S) 식의 계수야.'))

# ---------------- 30 MM 속도 · LB ----------------
add('Michaelis-Menten식과 Lineweaver-Burk식 — V, V<sub>m</sub> (빈칸 정답)', 'Rate V, V<sub>max</sub>, Lineweaver-Burk', 30,
    ['V = k<sub>3</sub>(E·S)', 'V<sub>m</sub> = k<sub>3</sub>E<sub>0</sub>', 'V = V<sub>m</sub>S/(K<sub>m</sub>+S)', '1/V = (K<sub>m</sub>/V<sub>m</sub>)(1/S) + 1/V<sub>m</sub>'],
    '생성물 생성 속도 V = k<sub>3</sub>(E·S) = k<sub>3</sub>SE<sub>0</sub>/(K<sub>m</sub>+S). 기질이 아주 많으면 모든 효소가 E·S가 되어 최대 속도 V<sub>m</sub> = k<sub>3</sub>E<sub>0</sub>. 역수를 취하면 1/V vs 1/S가 기울기 K<sub>m</sub>/V<sub>m</sub>, y절편 1/V<sub>m</sub>인 직선(Lineweaver-Burk).',
    eq('(E·S) = ' + F('SE<sub>0</sub>', 'K<sub>m</sub> + S') + ', &nbsp; K<sub>m</sub> = ' + F('k<sub>2</sub>+k<sub>3</sub>', 'k<sub>1</sub>'),
       '생성물(P)의 반응 속도는, ' + F('dP', 'dt') + ' = k<sub>3</sub>(E·S) = ' + F('k<sub>3</sub>SE<sub>0</sub>', 'K<sub>m</sub> + S') + ', &nbsp; ' + F('dP', 'dt') + ' = V, &nbsp; (' + F('dP', 'dt') + ')<sub>maximum</sub> = V<sub>m</sub>') +
    f'<p>생성물의 최대 속도(V<sub>m</sub>)는 {Y("(E·S) 농도가 최대일 때")}임 : 이를 위해 기질(S)이 매우 크다고 가정하면, {Y("E는 모두 (E·S) 상태로 존재")}할 것임. 이 때, (E·S) = E<sub>0</sub>이고 속도가 V<sub>m</sub>이 된다.</p>' +
    eq('k<sub>3</sub>(E·S) = k<sub>3</sub>E<sub>0</sub> = V<sub>m</sub> → ' + F('dP', 'dt') + ' = ' + F(A('V<sub>m</sub>S'), 'K<sub>m</sub> + S') + ' = V',
       F('1', 'V') + ' = ' + F('K<sub>m</sub> + S', 'V<sub>m</sub>S') + ' = ' + F('K<sub>m</sub>', 'V<sub>m</sub>') + F('1', 'S') + ' + ' + F('1', 'V<sub>m</sub>')) +
    f'<p>x축을 1/S라 하고 y축을 1/V라고 하면, 기울기가 ( {A("K<sub>m</sub>/V<sub>m</sub>")} ), y절편이 ( {A("1/V<sub>m</sub>")} )인 직선이 되며, 이러한 직선을 <b>Lineweaver-Burk 식</b>이라고 한다.</p>',
    tbl(['빈칸', '정답', '이유'], [
        ['dP/dt = ___/(K<sub>m</sub>+S)', A('V<sub>m</sub>S'), 'k<sub>3</sub>E<sub>0</sub> = V<sub>m</sub> 대입'],
        ['기울기', A('K<sub>m</sub>/V<sub>m</sub>'), '1/S 앞의 계수'],
        ['y절편', A('1/V<sub>m</sub>'), '1/S = 0일 때 1/V'],
    ]) +
    h4('Michaelis-Menten 식 해석') + tbl(['기질 농도', 'V', '차수'], [
        ['S ≪ K<sub>m</sub>', 'V ≈ (V<sub>m</sub>/K<sub>m</sub>)S', G('S에 대해 1차')],
        ['S = K<sub>m</sub>', 'V = V<sub>m</sub>/2', P('K<sub>m</sub> = 최대 속도의 절반일 때 S')],
        ['S ≫ K<sub>m</sub>', 'V ≈ V<sub>m</sub>', G('0차 (효소 포화)')],
    ]) +
    box('tip', '연결', 'S가 매우 크면 0차 → 슬라이드 14 “0차는 효소가 필요한 반응에서 발견”과 같은 이야기야.') +
    box('warn', '혼동 주의', '역수 그래프라 <b>y절편 = 1/V<sub>m</sub></b> (V<sub>m</sub> 자체 아님), <b>x절편 = −1/K<sub>m</sub></b>.'))

# ---------------- 31 LB 그래프 ----------------
add('Michaelis-Menten식과 Lineweaver-Burk식 — 그래프 읽기 (빈칸 정답)', 'Lineweaver-Burk plot', 31,
    ['1/V vs 1/S', 'y절편 → V<sub>m</sub>', '기울기 → K<sub>m</sub>', 'x절편 = −1/K<sub>m</sub>'],
    '1/V vs 1/S 그래프(Lineweaver-Burk plot)를 그리면 y절편(1/V<sub>m</sub>)에서 V<sub>m</sub>을, 기울기(K<sub>m</sub>/V<sub>m</sub>)에서 Michaelis-Menten 상수 K<sub>m</sub>을 구할 수 있다.',
    eq(F('1', 'V') + ' = ' + F('K<sub>m</sub>', 'V<sub>m</sub>') + F('1', 'S') + ' + ' + F('1', 'V<sub>m</sub>')) +
    f'<p>1/V vs 1/S 그래프를 그린 뒤, y절편에서 ( {A("V<sub>m</sub>")} )을 구할 수 있고, 기울기에서 ( {A("K<sub>m</sub>")} )(Michaelis-Menten 상수)를 구할 수 있다.</p>' +
    eq('K<sub>m</sub> = ' + F('k<sub>2</sub>+k<sub>3</sub>', 'k<sub>1</sub>')) +
    '<p>그래프: y축 1/V, x축 1/[S], Intercept 1/V<sub>m</sub>, Slope K<sub>m</sub>/V<sub>m</sub>, x축과 만나는 점 −(1/K<sub>m</sub>).</p>' +
h4('x절편이 −1/K<sub>m</sub>인 이유') + '<p>1/V = 0으로 두면 (K<sub>m</sub>/V<sub>m</sub>)(1/S) = −1/V<sub>m</sub> → 1/S = −1/K<sub>m</sub>. 실제로는 측정할 수 없는 영역이라 점선으로 연장해서 읽어.</p>',
    tbl(['빈칸', '정답', '계산'], [
        ['y절편에서 ( )', A('V<sub>m</sub>'), 'y절편 = 1/V<sub>m</sub> → V<sub>m</sub> = 1/(y절편)'],
        ['기울기에서 ( )', A('K<sub>m</sub>'), '기울기 = K<sub>m</sub>/V<sub>m</sub> → K<sub>m</sub> = 기울기 × V<sub>m</sub>'],
    ]) +
    tbl(['그래프 위치', '값'], [['y절편', G('1/V<sub>m</sub>')], ['기울기', G('K<sub>m</sub>/V<sub>m</sub>')], ['x절편', G('−1/K<sub>m</sub>')]]) +
    box('tip', '왜 역수로 그리나?', 'Michaelis-Menten 곡선(V vs S)은 V<sub>m</sub>에 천천히 다가가는 곡선이라 V<sub>m</sub>을 정확히 읽기 어려워. 역수로 바꾸면 직선이 돼서 절편·기울기로 깔끔하게 구할 수 있어.') +
    box('exam', '시험 포인트', 'Summary 4 정답판 표기: “y절편에서 (V<sub>m</sub>/K<sub>m</sub>) 중 <b>V<sub>m</sub></b>”, “기울기에서 (V<sub>m</sub>/K<sub>m</sub>) 중 <b>K<sub>m</sub></b>”. 정확히는 y절편 = 1/V<sub>m</sub>, 기울기 = K<sub>m</sub>/V<sub>m</sub>.'))

# ---------------- 32~35 Summary ----------------
def summary(n, slides, kw, summ, left, right):
    add(f'Summary {n} (빈칸판 + 정답판)', f'원본 슬라이드 {slides[0]} (빈칸) · {slides[1]} (정답)', f'{slides[0]}·{slides[1]}', kw, summ, left, right,
        img=[f'img/s-{slides[0]:02d}.png'])

summary(1, (32, 33), ['분해 요인 4개', '배합 시 pH', '반응물 소비 = 생성물 생성', 'k: 농도 무관 · 차수: 실험'],
        '안정성 시험의 필요성, 반응 속도의 정의(부호), 속도 상수(농도 무관)와 반응 차수(실험적으로만) 정리.',
        h4('안정성 시험에서의 필요성') + ul(
            '온도, 습도, 빛, pH 등의 다양한 요인에 의해서 약물이 분해될 수 있음.',
            '약물의 분해 속도를 화학 반응 속도로 예측할 수 있음.',
            f'약물을 배합할 경우 (온도/{A("pH")})에 따른 약물의 분해 속도를 알고 있어야 함.') +
        h4('반응 속도') + ul(
            f'반응 속도 = (생성물 / {A("반응물")})이 소비되는 속도 = ({A("생성물")} / 반응물)이 생성되는 속도',
            f'= ({A("−")}/+) d[A]/dt = (−/{A("+")}) d[B]/dt') +
        '<p style="text-align:center">−' + F('1', 'a') + F('d[A]', 'dt') + ' = −' + F('1', 'b') + F('d[B]', 'dt') + ' = ' + F('1', 'c') + F('d[C]', 'dt') + ' = ' + F('1', 'd') + F('d[D]', 'dt') + ' = k[A]<sup>x</sup>[B]<sup>y</sup></p>' +
        h4('속도 상수와 반응 차수') + ul(
            f'k = 속도 상수 : 반응물의 농도에 ({A("무관하며")} / 영향을 받으며) 반응물 종류, 온도에 영향을 받는다.',
            f'x + y = 전체 반응 차수, x, y 값은 (이론적으로 계산 가능 / {A("실험적으로만")}) 구해야 함!'),
        tbl(['선택형', '정답', '틀린 보기의 함정'], [
            ['(온도 / pH)', A('pH'), '온도도 분해 요인이지만 “배합” 문장은 pH'],
            ['(생성물 / 반응물)이 소비', A('반응물'), '생성물은 생성됨'],
            ['(−/+) d[A]/dt', A('−'), 'A는 감소 → 음수 보정'],
            ['(−/+) d[B]/dt', A('+'), 'B는 증가'],
            ['(무관하며 / 영향을 받으며)', A('무관하며'), '농도 → 속도는 변해도 k는 그대로'],
            ['(이론적 / 실험적으로만)', A('실험적으로만'), '계수 ≠ 차수'],
        ]) +
        box('exam', 'OX 연습', '① 속도 상수는 온도에 영향을 받는다 (O) ② 속도 상수는 반응물 농도가 커지면 커진다 (X) ③ 반응 차수는 반응식의 계수와 항상 같다 (X) ④ 반응물의 반응 속도는 −d[A]/dt로 쓴다 (O)'))

summary(2, (34, 35), ['적분식 · 반감기 · k 단위', '0차: 직선 · 비례', '1차: 지수적 · 무관', '2차: 반비례 · 반비례'],
        '0·1·2차의 적분식·반감기·k 단위 표와, 각 차수의 감소 모양·속도와 농도의 관계·반감기와 초기 농도의 관계를 선택형으로 정리.',
        tbl(['차수', '속도식', '적분식', '반감기', 'k 단위'], [
            ['0차', '−d[A]/dt = k', A('[A]<sub>t</sub> = −kt + [A]<sub>0</sub>'), '[A]<sub>0</sub>/2k', 'mol/L·sec'],
            ['1차', '−d[A]/dt = k[A]<sup>1</sup>', 'ln[A]<sub>t</sub> = −kt + ln[A]<sub>0</sub>', A('0.693/k'), 'sec<sup>−1</sup>'],
            ['2차', '−d[A]/dt = k[A]<sup>2</sup>', A('1/[A]<sub>t</sub> = kt + 1/[A]<sub>0</sub>'), '1/k[A]<sub>0</sub>', 'L/sec·mol'],
        ]) + ul(
            f'<b>0차 반응</b> : 시간에 따른 ({A("반응물")} / 생성물)이 ({A("직선")} / 지수적)으로 감소하며 반응 속도가 반응물의 농도에 따라 ({A("변하지 않음")} / 비례함). 반감기는 초기 반응물 농도에 ({A("비례")} / 반비례 / 무관) 함.',
            f'<b>1차 반응</b> : 시간에 따른 ({A("반응물")} / 생성물)이 (직선 / {A("지수적")})으로 감소하며 반응 속도가 반응물의 농도의 ({A("1")}/2)제곱에 (반비례함 / {A("비례함")}). 반감기는 초기 반응물 농도에 (비례 / 반비례 / {A("무관")}) 함.',
            f'<b>2차 반응</b> : 시간에 따른 ({A("반응물")} / 생성물)이 (직선 / {A("반비례")})(으)로 감소하며 반응 속도가 반응물의 농도의 (1/{A("2")})제곱에 (반비례함 / {A("비례함")}). 반감기는 초기 반응물 농도에 (비례 / {A("반비례")} / 무관) 함.'),
        tbl(['항목', '0차', '1차', '2차'], [
            ['감소 모양', '직선', '지수적', '반비례'],
            ['속도와 농도', '변하지 않음', '1제곱에 비례', '2제곱에 비례'],
            ['반감기 vs [A]<sub>0</sub>', P('비례'), P('무관'), P('반비례')],
            ['반감기 식', '[A]<sub>0</sub>/2k', '0.693/k', '1/k[A]<sub>0</sub>'],
            ['k 단위', 'mol/L·s', 's<sup>−1</sup>', 'L/mol·s'],
            ['직선 그래프', '[A] vs t', 'ln[A] vs t', '1/[A] vs t'],
        ]) +
        box('warn', '혼동 주의', '“반응 속도가 농도에 비례”는 1차·2차 모두 <b>비례함</b>이 정답 (2차는 2제곱에 비례). 반비례가 나오는 건 <b>반감기</b>(2차)와 <b>감소 모양</b>(2차)뿐이야.') +
        box('exam', 'OX 연습', '① 1차 반응의 반감기는 초기 농도에 비례한다 (X, 무관) ② 0차 반응은 반응물이 직선으로 감소한다 (O) ③ 2차 반응의 반감기는 1/k[A]<sub>0</sub>이다 (O) ④ 1차 반응 k의 단위는 mol/L·sec이다 (X, sec<sup>−1</sup>)'))

summary(3, (36, 37), ['가역: B → A로 되돌아감', '(k<sub>f</sub>+k<sub>r</sub>)/2.303', 'K = k<sub>f</sub>/k<sub>r</sub>', '평행: 동시에'],
        '가역 반응(일부 B가 다시 A로, 기울기와 평형상수의 연립으로 k<sub>f</sub>·k<sub>r</sub>)과 평행 반응(동시에 두 가지 이상 생성, 기울기로 k<sub>1</sub>·k<sub>2</sub>) 정리.',
        h4('가역 반응 (Reversible reaction)') + ul(
            f'A가 B를 형성하면서 일부 (A/{A("B")})는 다시 ({A("A")}/B)로 되돌아가는 현상') +
        eq('ln' + F('A<sub>0</sub> − A<sub>eq</sub>', 'A − A<sub>eq</sub>') + ' = (k<sub>f</sub>+k<sub>r</sub>)t, &nbsp; log' + F('A<sub>0</sub> − A<sub>eq</sub>', 'A − A<sub>eq</sub>') + ' = ' + F('(k<sub>f</sub>+k<sub>r</sub>)t', '2.303'),
           F('k<sub>f</sub>', 'k<sub>r</sub>') + ' = ' + F('B<sub>eq</sub>', 'A<sub>eq</sub>') + ' — 두 식을 연립방정식으로 하면 k<sub>f</sub>, k<sub>r</sub>를 구할 수 있음.') +
        '<p>그래프 y축 빈칸: ' + A('log[(A<sub>0</sub> − A<sub>eq</sub>)/(A − A<sub>eq</sub>)]') + ' (x축 Time)</p>' +
        h4('평행반응 (Parallel reaction)') + ul(
            f'한 가지 물질에서 (연속으로/{A("동시")})에 두 가지 이상의 물질이 생성되는 반응으로 약학에서 흔히 일어나는 반응 중 하나임.') +
        eq('A = ' + F('k<sub>1</sub>', 'k') + 'P<sub>0</sub>(1 − e<sup>−kt</sup>), &nbsp; N = ' + F('k<sub>2</sub>', 'k') + 'P<sub>0</sub>(1 − e<sup>−kt</sup>)',
           '기울기 = ' + F('k<sub>1</sub>', 'k') + 'P<sub>0</sub>, &nbsp; k<sub>1</sub> = ' + A('기울기') + ' × ' + F('k', 'P<sub>0</sub>') + ', &nbsp; k<sub>2</sub> = k − k<sub>1</sub>'),
        tbl(['선택형 · 빈칸', '정답', '함정'], [
            ['일부 (A/B)는', A('B'), '되돌아가는 건 생성물 B'],
            ['다시 (A/B)로', A('A'), '방향 뒤집기 주의'],
            ['그래프 y축', A('log[(A<sub>0</sub>−A<sub>eq</sub>)/(A−A<sub>eq</sub>)]'), '기울기 = (k<sub>f</sub>+k<sub>r</sub>)/2.303'],
            ['(연속으로/동시)', A('동시'), '“연속” = 연속 반응 (A → C → D)'],
            ['k<sub>1</sub> = ___ × k/P<sub>0</sub>', A('기울기'), 'A vs (1 − e<sup>−kt</sup>) 그래프'],
        ]) +
        tbl(['', '가역 반응', '평행 반응'], [
            ['구하는 것', 'k<sub>f</sub>, k<sub>r</sub>', 'k<sub>1</sub>, k<sub>2</sub>'],
            ['그래프', 'log[(A<sub>0</sub>−A<sub>eq</sub>)/(A−A<sub>eq</sub>)] vs t', 'A, N vs (1 − e<sup>−kt</sup>)'],
            ['기울기', '(k<sub>f</sub>+k<sub>r</sub>)/2.303', '(k<sub>1</sub>/k)P<sub>0</sub>'],
            ['두 번째 식', 'K = k<sub>f</sub>/k<sub>r</sub> = B<sub>eq</sub>/A<sub>eq</sub>', 'k<sub>2</sub> = k − k<sub>1</sub>'],
        ]) +
        box('exam', 'OX 연습', '① 평행 반응은 한 물질에서 연속으로 두 가지 물질이 생성된다 (X, 동시에) ② k<sub>f</sub>/k<sub>r</sub> = B<sub>eq</sub>/A<sub>eq</sub> (O) ③ 가역 반응 그래프의 기울기는 k<sub>f</sub>/2.303이다 (X)'))

summary(4, (38, 39), ['중간 생성물 일정', 'C = k<sub>1</sub>AB/(k<sub>2</sub>+k<sub>3</sub>)', '다단계 · 중간 산물', 'y절편 → V<sub>m</sub>, 기울기 → K<sub>m</sub>'],
        '정류 상태 근사법(중간 생성물 농도 일정 → C = k<sub>1</sub>AB/(k<sub>2</sub>+k<sub>3</sub>))과 Michaelis-Menten/Lineweaver-Burk(다단계, 중간 산물 정류 상태, y절편 → V<sub>m</sub>, 기울기 → K<sub>m</sub>) 정리.',
        h4('정류 상태 근사법 (Steady-state approximation)') + ul(
            f'여러 단계로 이루어진 반응에서 중간 단계 생성물이 반응에 있어서 (증가/{A("일정")})하다고 가정할 수 있을 때 이를 정류 상태 근사법이라고 함.') +
        eq('A + B ⇄ C → D, &nbsp; ' + F('dC', 'dt') + ' = k<sub>1</sub>AB − k<sub>2</sub>C − k<sub>3</sub>C = 0 (정류상태라면) → C = ' + A(F('k<sub>1</sub>', 'k<sub>2</sub> + k<sub>3</sub>')) + 'AB') +
        h4('Michaelis-Menten / Lineweaver-Burk 식') + ul(
            f'기질 S(substrate)와 효소 E(Enzyme)의 반응을 통해 최종적으로 생성물 P(Product)를 만드는 (단일/{A("다단계")}) 반응에서 (최종/{A("중간")}) 산물을 정류 상태로 가정할 때 반응 속도를 구하는 식.') +
        eq('(E·S) = ' + F('k<sub>1</sub>', 'k<sub>2</sub> + k<sub>3</sub>') + 'ES, &nbsp; ' + F('1', 'V') + ' = ' + F('K<sub>m</sub> + S', 'V<sub>m</sub>S') + ' = ' + F('K<sub>m</sub>', 'V<sub>m</sub>') + F('1', 'S') + ' + ' + F('1', 'V<sub>m</sub>')) +
        f'<p>(1/V) vs (1/S) 그래프를 그린 뒤 y절편에서 ({A("V<sub>m</sub>")}/K<sub>m</sub>)을 구할 수 있고 기울기에서 (V<sub>m</sub>/{A("K<sub>m</sub>")}) (Michaelis-Menten 상수)를 구할 수 있다.</p>',
        tbl(['선택형 · 빈칸', '정답', '함정'], [
            ['(증가/일정)', A('일정'), '정류 상태 = 중간체 농도 일정'],
            ['C = ___AB', A('k<sub>1</sub>/(k<sub>2</sub>+k<sub>3</sub>)'), '분모 = C가 없어지는 두 길'],
            ['(단일/다단계)', A('다단계'), 'E + S ⇄ E·S → P 두 단계 이상'],
            ['(최종/중간) 산물', A('중간'), '정류 상태로 두는 건 E·S'],
            ['y절편에서 (V<sub>m</sub>/K<sub>m</sub>)', A('V<sub>m</sub>'), 'y절편 = 1/V<sub>m</sub>'],
            ['기울기에서 (V<sub>m</sub>/K<sub>m</sub>)', A('K<sub>m</sub>'), '기울기 = K<sub>m</sub>/V<sub>m</sub>'],
        ]) +
        box('warn', '혼동 주의', '정답판의 “(V<sub>m</sub>/K<sub>m</sub>)”는 분수가 아니라 <b>V<sub>m</sub>과 K<sub>m</sub> 중 고르기</b>야. 실제 값은 y절편 = <b>1/V<sub>m</sub></b>, 기울기 = <b>K<sub>m</sub>/V<sub>m</sub></b>, x절편 = <b>−1/K<sub>m</sub></b>.') +
        box('exam', 'OX 연습', '① 정류 상태 근사법은 중간 생성물 농도가 증가한다고 가정한다 (X) ② Michaelis-Menten 식은 최종 산물을 정류 상태로 가정한다 (X) ③ Lineweaver-Burk 그래프의 y절편은 1/V<sub>m</sub>이다 (O) ④ K<sub>m</sub> = (k<sub>2</sub>+k<sub>3</sub>)/k<sub>1</sub> (O)'))
