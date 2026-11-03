from lib import *

PAGES = []
def add(*a, **k): PAGES.append(page(len(PAGES) + 1, *a, **k))

def choices(items, ans):
    """보기 목록, 정답 번호(1부터)는 파란 박스"""
    nums = '①②③④⑤'
    return '<p>' + '<br>'.join((A(f'{nums[i]} {c}') if i + 1 == ans else f'{nums[i]} {c}') for i, c in enumerate(items)) + '</p>'

def flow(rows):
    icon = {'see': '👀 단서', 'ask': '🤔 질문', 'link': '💡 연결', 'calc': '🧮 계산', 'chk': '🔍 함정체크', 'done': '✅ 결론'}
    return tbl(['🧭 사고의 흐름', ''], [[icon[k], v] for k, v in rows])

# ---------------- 01 표지 ----------------
add('표지 · 이번 강의 로드맵', '물리약학 각론 — 화학반응속도론 및 안정성 1-1, 이재우 교수, 고려대학교 약학대학 (Ch.14)', 1,
    ['9주차 복습 (Recap 1~4)', 'k 단위 · 초기속도법', '계수와 속도의 관계', '효소-기질: 혈전 형성', '기출 Quiz 7문제'],
    '9주차 내용을 Recapitulation 1~4로 다시 정리하고, k 단위·초기속도법 예제와 N<sub>2</sub>O<sub>5</sub> 분해 예제를 푼 뒤, 효소-기질 반응의 예(혈전 형성)와 2017~2026 기출 Quiz 7문제를 다룬다.',
    h4('오늘 강의 흐름') + tbl(['순서', '내용', '슬라이드'], [
        ['1', 'Recapitulation 1 — 안정성 · 반응 속도 · k와 반응 차수', '2'],
        ['2', 'Recapitulation 2 — 0/1/2차 적분식 · 반감기 · k 단위', '3'],
        ['3', 'Recapitulation 3 — 가역 반응 · 평행 반응', '4'],
        ['4', 'Recapitulation 4 — 정류 상태 근사법 · Michaelis-Menten', '5'],
        ['5', '기초 수학 (정답판)', '6'],
        ['6', 'k 단위 + 초기속도법 예제 · N<sub>2</sub>O<sub>5</sub> 계수 예제', '7~8'],
        ['7', '효소-기질 반응의 예: Thrombus(혈전)의 형성', '9'],
        ['8', '기출 Quiz (2026 · 2025 · 2024 ×2 · 2021 · 2020 · 2017)', '10~16'],
    ]),
    h4('읽는 법') + ul(
        '이번 자료는 <b>본수업 게시용</b>이라 대부분의 정답이 슬라이드에 빨간 글씨로 들어 있어. 그 정답을 파란 박스로 옮겼어.',
        '슬라이드에 답이 없는 <b>예제 2개(슬라이드 7, 8)와 기출 Quiz 7문제</b>는 직접 풀어서 정답과 🧭 사고의 흐름을 붙였어.',
        '9주차 빈칸정답및해설과 내용이 이어지니까 같이 보면 좋아.') +
    box('tip', '빈칸 정답 표시법', f'빈칸·선택형 괄호·기출 정답은 이렇게 {A("파란 박스")}로 표시했어.') +
    box('exam', '시험 포인트', '기출 7문제 중 5문제가 <b>1차 반응 계산(ln, 반감기)</b>과 <b>차수 판단</b>이야. 공식 t<sub>1/2</sub> = 0.693/k, ln(C<sub>0</sub>/C) = kt는 무조건 손에 익혀 둬.'),
    left_title='원문 정리')

# ---------------- 02 Recap 1 ----------------
add('Recapitulation 1 — 안정성 · 반응 속도 · 속도 상수 (정답)', 'Recap 1: stability, reaction rate, rate constant & order', 2,
    ['배합 시 pH', '반응물 소비 = 생성물 생성', 'k: 농도 무관', '차수: 실험적으로만'],
    '9주차 Summary 1과 같은 내용. 배합 시 pH, 반응 속도 = 반응물이 소비되는 속도 = 생성물이 생성되는 속도(−d[A]/dt = +d[B]/dt), k는 농도와 무관, 반응 차수는 실험적으로만 구한다.',
    h4('안정성 시험에서의 필요성') + ul(
        '온도, 습도, 빛, pH 등의 다양한 요인에 의해서 약물이 분해될 수 있음.',
        '약물의 분해 속도를 화학 반응 속도로 예측할 수 있음.',
        f'약물을 배합할 경우 (온도/{A("pH")})에 따른 약물의 분해 속도를 알고 있어야 함.') +
    h4('반응 속도') + ul(
        f'반응 속도 = (생성물 / {A("반응물")})이 소비되는 속도 = ({A("생성물")} / 반응물)이 생성되는 속도',
        f'= ({A("−")}/+) d[A]/dt = (−/{A("+")}) d[B]/dt') +
    eq('aA + bB → cC + dD, &nbsp; −' + F('1', 'a') + F('d[A]', 'dt') + ' = −' + F('1', 'b') + F('d[B]', 'dt') + ' = ' + F('1', 'c') + F('d[C]', 'dt') + ' = ' + F('1', 'd') + F('d[D]', 'dt') + ' = k[A]<sup>x</sup>[B]<sup>y</sup>') +
    h4('속도 상수와 반응 차수') + ul(
        f'k = 속도 상수 : 반응물의 농도에 ({A("무관하며")} / 영향을 받으며) 반응물 종류, 온도에 영향을 받는다.',
        f'x + y = 전체 반응 차수, x, y 값은 (이론적으로 계산 가능 / {A("실험적으로만")}) 구해야 함!'),
    tbl(['선택형', '정답', '틀린 보기의 함정'], [
        ['(온도 / pH)', A('pH'), '온도도 분해 요인이지만 “배합” 문장은 pH'],
        ['(생성물 / 반응물)이 소비', A('반응물'), '생성물은 생성됨'],
        ['(−/+) d[A]/dt', A('−'), 'A는 감소 → d[A]/dt < 0 → −를 붙여 양수로'],
        ['(−/+) d[B]/dt', A('+'), 'B는 증가'],
        ['(무관하며 / 영향을 받으며)', A('무관하며'), '농도가 바뀌면 속도는 변해도 k는 그대로'],
        ['(이론적 / 실험적으로만)', A('실험적으로만'), '계수 ≠ 차수 (슬라이드 7 예제 참고)'],
    ]) +
    box('warn', '혼동 주의', '“속도”와 “속도 <b>상수</b>”를 구별해. 농도 ↑ → 속도 ↑ (0차 제외), 하지만 k는 그대로. 온도 ↑ → k 자체가 ↑.') +
    box('exam', 'OX 연습', '① 속도 상수는 반응물 농도에 영향을 받는다 (X) ② 반응 차수는 반응식 계수로 이론적으로 정한다 (X) ③ 반응 속도 = 생성물이 생성되는 속도 (O)'))

# ---------------- 03 Recap 2 ----------------
add('Recapitulation 2 — 0 · 1 · 2차 반응 (정답)', 'Recap 2: integrated rate laws, half-lives, units', 3,
    ['0차: 직선 · 비례', '1차: 지수적 · 무관', '2차: 반비례 · 반비례', 'k 단위'],
    '0차는 직선으로 감소·속도가 농도와 무관·반감기가 초기 농도에 비례, 1차는 지수적 감소·농도의 1제곱에 비례·반감기 무관, 2차는 반비례 곡선으로 감소·농도의 2제곱에 비례·반감기 반비례.',
    tbl(['차수', '속도식', '적분식', '반감기', 'k 단위'], [
        ['0차', '−d[A]/dt = k', A('[A]<sub>t</sub> = −kt + [A]<sub>0</sub>'), '[A]<sub>0</sub>/2k', 'mol/L·sec'],
        ['1차', '−d[A]/dt = k[A]<sup>1</sup>', 'ln[A]<sub>t</sub> = −kt + ln[A]<sub>0</sub>', A('0.693/k'), 'sec<sup>−1</sup>'],
        ['2차', '−d[A]/dt = k[A]<sup>2</sup>', A('1/[A]<sub>t</sub> = kt + 1/[A]<sub>0</sub>'), '1/k[A]<sub>0</sub>', 'L/sec·mol'],
    ]) + ul(
        f'<b>0차 반응</b> : 시간에 따른 ({A("반응물")} / 생성물)이 ({A("직선")} / 지수적)으로 감소하며 반응 속도가 반응물의 농도에 따라 ({A("변하지 않음")} / 비례함). 반감기는 초기 반응물 농도에 ({A("비례")} / 반비례 / 무관) 함.',
        f'<b>1차 반응</b> : 시간에 따른 ({A("반응물")} / 생성물)이 (직선 / {A("지수적")})으로 감소하며 반응 속도가 반응물의 농도의 ({A("1")}/2)제곱에 (반비례함 / {A("비례함")}). 반감기는 초기 반응물 농도에 (비례 / 반비례 / {A("무관")}) 함.',
        f'<b>2차 반응</b> : 시간에 따른 ({A("반응물")} / 생성물)이 (직선 / {A("반비례")})(으)로 감소하며 반응 속도가 반응물의 농도의 (1/{A("2")})제곱에 (반비례함 / {A("비례함")}). 반감기는 초기 반응물 농도에 (비례 / {A("반비례")} / 무관) 함.'),
    tbl(['항목', '0차', '1차', '2차'], [
        ['직선이 되는 그래프', '[A] vs t (기울기 −k)', 'ln[A] vs t (기울기 −k)', '1/[A] vs t (기울기 +k)'],
        ['반감기 vs [A]<sub>0</sub>', P('비례'), P('무관'), P('반비례')],
        ['[A]<sub>0</sub> 2배 → t<sub>1/2</sub>', '2배', '그대로', '1/2배'],
        ['k 단위', 'mol/L·s', 's<sup>−1</sup>', 'L/mol·s'],
        ['이번 기출', '2017 Q13', '2026 · 2025 · 2024 · 2021', '2020 Q13'],
    ]) +
    box('tip', '외우기', '반감기 식에서 [A]<sub>0</sub>의 위치: 0차 <b>분자</b>(비례) · 1차 <b>없음</b>(무관) · 2차 <b>분모</b>(반비례).') +
    box('exam', 'OX 연습', '① 1차 반응의 반감기는 초기 농도에 무관하다 (O) ② 2차 반응은 반응물이 직선으로 감소한다 (X, 반비례) ③ 0차 반응 속도는 농도에 비례한다 (X)'))

# ---------------- 04 Recap 3 ----------------
add('Recapitulation 3 — 가역 반응 · 평행 반응 (정답)', 'Recap 3: reversible & parallel reactions', 4,
    ['가역: 일부 B → A', '(k<sub>f</sub>+k<sub>r</sub>)/2.303', 'K = k<sub>f</sub>/k<sub>r</sub> = B<sub>eq</sub>/A<sub>eq</sub>', '평행: 동시에'],
    '가역 반응은 A가 B가 되면서 일부 B가 다시 A로 돌아가는 반응이고, 그래프 기울기 (k<sub>f</sub>+k<sub>r</sub>)/2.303과 K = k<sub>f</sub>/k<sub>r</sub>을 연립해 k<sub>f</sub>, k<sub>r</sub>을 구한다. 평행 반응은 한 물질에서 동시에 두 가지 이상이 생기며, A vs (1 − e<sup>−kt</sup>) 기울기로 k<sub>1</sub>을 구한다.',
    h4('가역 반응 (Reversible reaction)') + ul(
        f'A가 B를 형성하면서 일부 (A/{A("B")})는 다시 ({A("A")}/B)로 되돌아가는 현상') +
    eq('ln' + F('A<sub>0</sub> − A<sub>eq</sub>', 'A − A<sub>eq</sub>') + ' = (k<sub>f</sub>+k<sub>r</sub>)t, &nbsp; log' + F('A<sub>0</sub> − A<sub>eq</sub>', 'A − A<sub>eq</sub>') + ' = ' + F('(k<sub>f</sub>+k<sub>r</sub>)t', '2.303'),
       F('k<sub>f</sub>', 'k<sub>r</sub>') + ' = ' + F('B<sub>eq</sub>', 'A<sub>eq</sub>') + ' — 두 식을 연립방정식으로 하면 k<sub>f</sub>, k<sub>r</sub>를 구할 수 있음.') +
    h4('평행반응 (Parallel reaction)') + ul(
        f'한 가지 물질에서 (연속으로/{A("동시")})에 두 가지 이상의 물질이 생성되는 반응으로 약학에서 흔히 일어나는 반응 중 하나임.') +
    eq('A = ' + F('k<sub>1</sub>', 'k') + 'P<sub>0</sub>(1 − e<sup>−kt</sup>), &nbsp; N = ' + F('k<sub>2</sub>', 'k') + 'P<sub>0</sub>(1 − e<sup>−kt</sup>)',
       '기울기 = ' + F('k<sub>1</sub>', 'k') + 'P<sub>0</sub> → k<sub>1</sub> = 기울기 × ' + F('k', 'P<sub>0</sub>') + ', &nbsp; k<sub>2</sub> = k − k<sub>1</sub>') +
    '<p>실험적으로 k<sub>1</sub>, k<sub>2</sub> 구하기 : 생성된 A 또는 N 물질의 농도를 Y축으로 하고 1 − e<sup>−kt</sup>를 x축으로 하는 그래프를 그린 뒤 기울기를 구한다.</p>',
    tbl(['선택형', '정답', '함정'], [
        ['일부 (A/B)는', A('B'), '되돌아가는 건 생성물 B'],
        ['다시 (A/B)로', A('A'), '방향 뒤집기 주의'],
        ['(연속으로/동시)', A('동시'), '“연속” = 연속 반응 (A → C → D)'],
    ]) +
    tbl(['', '가역 반응', '평행 반응'], [
        ['구하는 것', 'k<sub>f</sub>, k<sub>r</sub>', 'k<sub>1</sub>, k<sub>2</sub>'],
        ['그래프', 'log[(A<sub>0</sub>−A<sub>eq</sub>)/(A−A<sub>eq</sub>)] vs t', 'A, N vs (1 − e<sup>−kt</sup>)'],
        ['기울기', '(k<sub>f</sub>+k<sub>r</sub>)/2.303', '(k<sub>1</sub>/k)P<sub>0</sub>'],
        ['두 번째 식', 'K = k<sub>f</sub>/k<sub>r</sub> = B<sub>eq</sub>/A<sub>eq</sub>', 'k<sub>2</sub> = k − k<sub>1</sub> (k = k<sub>1</sub> + k<sub>2</sub>)'],
    ]) +
    box('warn', '혼동 주의', '가역 반응 그래프 기울기는 k<sub>f</sub> 하나가 아니라 <b>(k<sub>f</sub> + k<sub>r</sub>)/2.303</b>. 평행 반응에서 P의 감소 속도 상수는 k<sub>1</sub>이 아니라 <b>k = k<sub>1</sub> + k<sub>2</sub></b>.') +
    box('exam', 'OX 연습', '① 평행 반응은 연속으로 두 물질이 생긴다 (X) ② K = k<sub>f</sub>/k<sub>r</sub> (O)'))

# ---------------- 05 Recap 4 ----------------
add('Recapitulation 4 — 정류 상태 근사법 · Michaelis-Menten (정답)', 'Recap 4: steady-state, Michaelis-Menten, Lineweaver-Burk', 5,
    ['중간 생성물 일정', 'C = k<sub>1</sub>AB/(k<sub>2</sub>+k<sub>3</sub>)', '다단계 · 중간 산물', 'y절편 → V<sub>m</sub>, 기울기 → K<sub>m</sub>'],
    '정류 상태 근사법은 중간 생성물 농도가 일정하다고 보는 방법(C = k<sub>1</sub>AB/(k<sub>2</sub>+k<sub>3</sub>)). Michaelis-Menten 식은 다단계 효소 반응에서 중간 산물 E·S를 정류 상태로 가정한 식이고, Lineweaver-Burk 그래프의 y절편에서 V<sub>m</sub>, 기울기에서 K<sub>m</sub>을 구한다.',
    h4('정류 상태 근사법 (Steady-state approximation)') + ul(
        f'여러 단계로 이루어진 반응에서 중간 단계 생성물이 반응에 있어서 (증가/{A("일정")})하다고 가정할 수 있을 때 이를 정류 상태 근사법이라고 함.') +
    eq('A + B ⇄ C → D, &nbsp; ' + F('dC', 'dt') + ' = k<sub>1</sub>AB − k<sub>2</sub>C − k<sub>3</sub>C = 0 (정류상태라면) → C = ' + F('k<sub>1</sub>', 'k<sub>2</sub> + k<sub>3</sub>') + 'AB') +
    h4('Michaelis-Menten / Lineweaver-Burk 식') + ul(
        f'기질 S(substrate)와 효소 E(Enzyme)의 반응을 통해 최종적으로 생성물 P(Product)를 만드는 (단일/{A("다단계")}) 반응에서 (최종/{A("중간")}) 산물을 정류 상태로 가정할 때 반응 속도를 구하는 식.') +
    eq('(E·S) = ' + F('k<sub>1</sub>', 'k<sub>2</sub> + k<sub>3</sub>') + 'ES, &nbsp; ' + F('dP', 'dt') + ' = V, &nbsp; (' + F('dP', 'dt') + ')<sub>maximum</sub> = V<sub>m</sub>',
       F('1', 'V') + ' = ' + F('K<sub>m</sub> + S', 'V<sub>m</sub>S') + ' = ' + F('K<sub>m</sub>', 'V<sub>m</sub>') + F('1', 'S') + ' + ' + F('1', 'V<sub>m</sub>')) +
    f'<p>(1/V) vs (1/S) 그래프를 그린 뒤 y절편에서 ({A("V<sub>m</sub>")}/K<sub>m</sub>)을 구할 수 있고 기울기에서 (V<sub>m</sub>/{A("K<sub>m</sub>")}) (Michaelis-Menten 상수)를 구할 수 있다.</p>',
    tbl(['선택형', '정답', '함정'], [
        ['(증가/일정)', A('일정'), '정류 상태 = 중간체 농도 일정'],
        ['(단일/다단계)', A('다단계'), 'E + S ⇄ E·S → P'],
        ['(최종/중간) 산물', A('중간'), '정류 상태로 두는 건 E·S'],
        ['y절편에서 (V<sub>m</sub>/K<sub>m</sub>)', A('V<sub>m</sub>'), 'y절편 = 1/V<sub>m</sub>'],
        ['기울기에서 (V<sub>m</sub>/K<sub>m</sub>)', A('K<sub>m</sub>'), '기울기 = K<sub>m</sub>/V<sub>m</sub>'],
    ]) +
    tbl(['그래프 위치', '값'], [['y절편', G('1/V<sub>m</sub>')], ['기울기', G('K<sub>m</sub>/V<sub>m</sub>')], ['x절편', G('−1/K<sub>m</sub>')]]) +
    box('warn', '혼동 주의', '“(V<sub>m</sub>/K<sub>m</sub>)”는 분수가 아니라 V<sub>m</sub>과 K<sub>m</sub> 중 고르기야. 정류 상태(중간체 일정, 반응은 진행 중) ≠ 평형(정·역반응 속도 같음).'))

# ---------------- 06 기초 수학 ----------------
add('이번 시간에 쓰이는 기초 수학 (정답)', 'Basic math for kinetics', 6,
    ['log 빼기 = 나누기', '∫1/x dx = ln x', '∫1/x² dx = −1/x', '∫e<sup>−kt</sup>dt'],
    '9주차의 빈칸이었던 기초 수학 6개가 이번 슬라이드에는 정답(빨간 글씨)으로 들어 있다. 1차는 ∫1/x, 2차는 ∫1/x², 가역은 ∫1/(ax+b), 평행은 ∫e<sup>−kt</sup>dt를 쓴다.',
    tbl(['식', '정답'], [
        ['log A − log B =', A('log (A/B)')],
        ['∫ 1/x dx =', A('ln x + C')],
        ['∫ 1/x² dx =', A('−1/x + C')],
        ['∫ 1/(ax+b) dx =', A('(1/a) ln(ax+b) + C')],
        ['ln e<sup>−kt</sup> =', A('−kt')],
        ['∫<sub>0</sub><sup>t</sup> e<sup>−kt</sup> dt =', A('−(1/k)(e<sup>−kt</sup> − 1)')],
    ]) +
    h4('기출 계산에 쓰는 로그 값') + tbl(['값', '쓰임'], [
        ['ln 2 = 0.693', '1차 반감기 t<sub>1/2</sub> = 0.693/k'],
        ['ln 10 = 2.303 (≈ 2.3)', 'ln x = 2.303 log x, 농도가 1/10이 될 때'],
        ['ln 100 = 4.6', '2026 기출: 초기 농도 100'],
    ]),
    tbl(['공식', '어디에 쓰나'], [
        ['∫1/x dx = ln x', '1차 적분 → ' + G('ln[A]<sub>t</sub> = −kt + ln[A]<sub>0</sub>')],
        ['∫1/x² dx = −1/x', '2차 적분 → ' + G('1/[A]<sub>t</sub> = kt + 1/[A]<sub>0</sub>')],
        ['∫1/(ax+b) dx', '가역 반응 (a = k<sub>f</sub> + k<sub>r</sub>)'],
        ['ln e<sup>−kt</sup> = −kt', '[A]<sub>t</sub> = [A]<sub>0</sub>e<sup>−kt</sup>'],
        ['∫e<sup>−kt</sup>dt', '평행 반응 A, N'],
        ['log(A/B) = log A − log B', 'ln(C<sub>0</sub>/C) 꼴 계산'],
    ]) +
    box('warn', '혼동 주의', '∫1/x² dx = <b>−</b>1/x. ∫1/(ax+b) dx 앞에 <b>1/a</b>가 붙는 것 잊지 말기.') +
    box('tip', '체크', '1차 계산 기출은 거의 다 <b>ln(C<sub>0</sub>/C) = kt</b> 한 줄로 끝나. log를 쓰면 log(C<sub>0</sub>/C) = kt/2.303.'))

# ---------------- 07 k 단위 + 예제 ----------------
add('속도 상수와 0차 반응 — 속도 상수의 단위 · 초기속도법 예제 (정답)', 'Units of k · initial-rate example', 7,
    ['0차: mol/L·sec', '1차: sec<sup>−1</sup>', '2차: L/mol·sec', 'rate = k[A]²[B]'],
    'k 단위는 0차 mol/L·sec, 1차 sec<sup>−1</sup>, 2차 L/sec·mol(정답판 빨간 글씨). 예제: [B] 2배 → 속도 2배(y = 1), [A] 2배 → 속도 4배(x = 2) → rate = k[A]²[B], k = 20 L²/mol²·s.',
    '<p style="text-align:center">A → B, &nbsp; −' + F('d[A]', 'dt') + ' = k[A]<sup>x</sup> → k = −' + F('d[A]', 'dt') + F('1', '[A]<sup>x</sup>') + '</p>' +
    tbl(['차수', 'k 계산', '단위 (정답)'], [
        ['x = 0 (0차)', 'k = (mol/L)/sec', A('mol/L·sec')],
        ['x = 1 (1차)', 'k = (mol/L)/(sec·mol/L)', A('sec<sup>−1</sup>')],
        ['x = 2 (2차)', 'k = (mol/L)/(sec·(mol/L)<sup>2</sup>)', A('L/sec·mol')],
    ]) +
    h4('예제') + '<p>A + 2B → C 반응에서 농도에 따른 초기반응속도의 측정결과가 표와 같을 때, 반응 속도식과 k값과 단위를 구하시오.</p>' +
    tbl(['실험', '[A] (mol/L)', '[B] (mol/L)', 'C 생성속도 (mol/L·s)'], [
        ['1', '0.1', '0.1', '0.02'], ['2', '0.1', '0.2', '0.04'], ['3', '0.2', '0.1', '0.08']]) +
    '<p>정답: ' + A('rate = k[A]<sup>2</sup>[B]') + ', ' + A('k = 20 L<sup>2</sup>/mol<sup>2</sup>·s') + '</p>',
    flow([
        ('see', '한 번에 한 물질 농도만 바뀐 실험 쌍을 찾는다'),
        ('calc', '실험 1 → 2: [A] 그대로, [B] ×2 → 속도 ×2 → 2<sup>y</sup> = 2 → ' + G('y = 1')),
        ('calc', '실험 1 → 3: [B] 그대로, [A] ×2 → 속도 ×4 → 2<sup>x</sup> = 4 → ' + G('x = 2')),
        ('link', 'C의 계수가 1 → C 생성속도 = 반응 속도 = k[A]<sup>2</sup>[B] (전체 3차)'),
        ('calc', 'k = 0.02 / (0.1<sup>2</sup> × 0.1) = 0.02 / 0.001 = ' + G('20')),
        ('chk', '단위: (mol/L·s) ÷ (mol/L)<sup>3</sup> = L<sup>2</sup>/(mol<sup>2</sup>·s)'),
        ('done', 'rate = k[A]<sup>2</sup>[B], k = 20 L<sup>2</sup>/mol<sup>2</sup>·s'),
    ]) +
    box('warn', '함정 체크', 'B의 계수는 2인데 차수 y = 1, A의 계수는 1인데 차수 x = 2. <b>계수 ≠ 차수</b> → 차수는 실험적으로만!') +
    box('tip', '단위 공식', 'k 단위 = (mol/L)<sup>1−n</sup>·s<sup>−1</sup> (n = 전체 차수). 3차면 L<sup>2</sup>/mol<sup>2</sup>·s.'))

# ---------------- 08 N2O5 ----------------
add('화학 반응 속도 — 계수와 속도의 관계 예제 (정답)', 'Example: 2N<sub>2</sub>O<sub>5</sub> → 4NO<sub>2</sub> + O<sub>2</sub>', 8,
    ['계수로 나누기', '소멸속도 0.2/t', 'NO<sub>2</sub> 생성 0.4/t', 'O<sub>2</sub> 생성 0.1/t'],
    'N<sub>2</sub>O<sub>5</sub>가 t 동안 0.4 M → 0.2 M이면 소멸속도는 0.2/t M. 계수 비 2 : 4 : 1에 따라 NO<sub>2</sub> 생성속도는 2배(0.4/t), O<sub>2</sub>는 1/2배(0.1/t). 반응이 끝나면 N<sub>2</sub>O<sub>5</sub> 0.4 M이 모두 분해되어 NO<sub>2</sub>는 0.8 M.',
    '<p>아래 반응에서 반응 초기부터 t시간 동안 N<sub>2</sub>O<sub>5</sub> 농도가 0.4 M에서 0.2 M이 되었을 때, 다음 물음에 답하시오.</p>' +
    eq('2N<sub>2</sub>O<sub>5</sub>(g) → 4NO<sub>2</sub>(g) + O<sub>2</sub>(g)') +
    tbl(['물음', '정답'], [
        ['반응이 종료되었을 때 NO<sub>2</sub>의 농도', A('0.8 M')],
        ['N<sub>2</sub>O<sub>5</sub>의 소멸속도', A('0.2/t M')],
        ['NO<sub>2</sub>의 생성속도', A('0.4/t M')],
        ['O<sub>2</sub>의 생성속도', A('0.1/t M')],
    ]) +
    '<p>(처음에 NO<sub>2</sub>, O<sub>2</sub>는 없었다고 가정. 속도 단위는 M/시간)</p>' +
    eq('반응 속도 = −' + F('1', '2') + F('d[N<sub>2</sub>O<sub>5</sub>]', 'dt') + ' = ' + F('1', '4') + F('d[NO<sub>2</sub>]', 'dt') + ' = ' + F('d[O<sub>2</sub>]', 'dt') + ' = ' + F('0.1', 't') + ' M'),
    flow([
        ('see', '계수 2 : 4 : 1 → 같은 시간 동안 변하는 몰 수의 비'),
        ('calc', 'N<sub>2</sub>O<sub>5</sub> 감소량 = 0.4 − 0.2 = 0.2 M → 소멸속도 = ' + G('0.2/t')),
        ('calc', 'NO<sub>2</sub>: N<sub>2</sub>O<sub>5</sub>의 4/2 = 2배 → ' + G('0.4/t')),
        ('calc', 'O<sub>2</sub>: N<sub>2</sub>O<sub>5</sub>의 1/2배 → ' + G('0.1/t')),
        ('calc', '반응 종료: N<sub>2</sub>O<sub>5</sub> 0.4 M 전부 분해 → NO<sub>2</sub> = 0.4 × 2 = ' + G('0.8 M') + ' (O<sub>2</sub>는 0.2 M)'),
        ('chk', '“반응 속도” 하나로는 0.1/t — 각 물질 속도를 계수로 나누면 모두 0.1/t로 같아짐'),
    ]) +
    box('warn', '혼동 주의', '“반응 종료” = 반응물이 <b>처음 양(0.4 M)</b> 기준으로 다 사라진 상태. t시간 동안 줄어든 0.2 M으로 계산하면(0.4 M) 틀려.') +
    box('exam', '시험 포인트', '“N<sub>2</sub>O<sub>5</sub>의 소멸속도와 NO<sub>2</sub>의 생성속도는 같다” → <b>X</b> (NO<sub>2</sub>가 2배). 같은 건 계수로 나눈 값.'))

# ---------------- 09 Thrombus ----------------
add('기질(Substrate) – 효소(Enzyme) 반응의 예 : Thrombus의 형성', 'Coagulation cascade as enzyme–substrate reactions (Budnick et al., 2018)', 9,
    ['혈액 응고 연쇄 반응', 'Prothrombin → Thrombin', 'Fibrinogen → Fibrin', '항응고제의 작용점'],
    '혈전(thrombus) 형성은 응고 인자들이 차례로 다음 인자를 활성화하는 효소-기질 반응의 연쇄다. FXa가 prothrombin(기질)을 thrombin(효소)으로 바꾸고, thrombin이 fibrinogen(기질)을 fibrin으로 바꿔 crosslinked clot을 만든다. 항응고제는 이 효소 단계를 막는다.',
    h4('그림 읽기 (Budnick et al., 2018, Trends in Immunology)') + ul(
        '<b>Intrinsic pathway(내인성 경로)</b>: 표면(Surface)·혈소판(Platelet, PolyP) → FXII → FXIIa → FXI → FXIa → FIX → FIXa (+FVIIIa)',
        '<b>Extrinsic pathway(외인성 경로)</b>: 활성화된 내피세포·조직·단핵구의 TF(조직인자) → FVII → FVIIa',
        '두 경로가 <b>FX → FXa</b>(+FVa)에서 만남 → <b>Prothrombin → Thrombin</b>',
        '<b>Thrombin</b>: Fibrinogen → <b>Fibrin</b> → (FXIIIa) → <b>Crosslinked clot</b> (혈전)') +
    tbl(['약물', '작용 지점 (그림의 ⊣)'], [
        ['Warfarin', 'FIX, FX, FVII, Prothrombin (비타민 K 의존 인자 생성 억제)'],
        ['Rivaroxaban', 'FXa (직접 억제)'],
        ['Dabigatran (direct)', 'Thrombin 직접 억제'],
        ['Heparin (indirect)', 'Thrombin 간접 억제 (antithrombin을 통해)'],
    ]),
    '<p>(이 슬라이드에는 빈칸이 없어.)</p>' +
    h4('Michaelis-Menten과 연결') + tbl(['단계', '효소 (E)', '기질 (S)', '생성물 (P)'], [
        ['1', 'FXa (+FVa)', 'Prothrombin', 'Thrombin'],
        ['2', 'Thrombin', 'Fibrinogen', 'Fibrin'],
        ['3', 'FXIIIa', 'Fibrin', 'Crosslinked clot'],
    ]) +
    '<p>각 단계가 E + S ⇄ E·S → P 꼴이야. 앞 단계의 생성물(P)이 다음 단계의 <b>효소(E)</b>가 되는 게 연쇄 반응(cascade)의 핵심 — 그래서 작은 신호가 크게 증폭돼.</p>' +
    box('tip', '비유', '도미노: 앞 도미노(활성 효소)가 다음 도미노(기질)를 넘어뜨려 활성 효소로 만들고, 마지막에 fibrin 그물(혈전)이 생겨.') +
    box('exam', '시험 포인트', '물리약학 시험에서는 “효소-기질 반응(Michaelis-Menten)의 예”로 기억하면 충분할 가능성이 높아. 약물 작용점은 약리학과 연결되는 보너스 정보야.'))

# ---------------- 10~16 Quiz ----------------
def quiz(year, slide, title, kw, summ, q, items, ans, fl, extra=''):
    add(f'Quiz — {year} 기출: {title} (정답 {"①②③④⑤"[ans-1]})', f'Past exam {year}', slide, kw, summ,
        f'<p><b>{year} 기출</b> {q}</p>' + choices(items, ans) + extra,
        flow(fl[0]) + fl[1], left_title='문제 (정답 표시)')

quiz('2026', 10, '1차 반응 농도 계산', ['t<sub>1/2</sub> → k', 'ln C = ln C<sub>0</sub> − kt', 'k = 0.1 day<sup>−1</sup>'],
     't<sub>1/2</sub> = 6.93일 → k = 0.693/6.93 = 0.1 day<sup>−1</sup>. ln C = ln 100 − kt = 4.6 − 0.1 × 20 = 2.6 → ③.',
     '13. 25 ℃에서 반감기가 6.93일인 약물 A의 분해는 1차 반응을 따른다. 초기농도가 100 mg/mL일 때, 20일 후 약물 농도가 C mg/mL이다. lnC는? (단, ln2 = 0.693, ln100 = 4.6이다.)',
     ['1.3', '2.3', '2.6', '3.9', '4.6'], 3,
     ([('see', '1차 반응 + 반감기 주어짐 → k부터'),
       ('calc', 'k = 0.693 / t<sub>1/2</sub> = 0.693 / 6.93 = ' + G('0.1 day<sup>−1</sup>')),
       ('link', '1차 적분식: ln C = −kt + ln C<sub>0</sub>'),
       ('calc', 'ln C = 4.6 − 0.1 × 20 = 4.6 − 2 = ' + G('2.6')),
       ('chk', '20일 ≈ 2.9 반감기 → C ≈ 100 × (1/2)<sup>2.9</sup> ≈ 13.5, ln 13.5 ≈ 2.6 ✔'),
       ('done', '③ 2.6')],
      box('warn', '함정', '① 1.3은 kt = 3.3으로 잘못 계산, ⑤ 4.6은 ln C<sub>0</sub> 그대로. 단위(일)를 k와 t에서 맞추기.')))

quiz('2025', 11, '차수 판단 (그래프)', ['초기 농도 2개', '같은 비율로 감소', '반감기 일정 → 1차'],
     '초기 농도 600과 400에서 시작한 두 곡선이 같은 시간 동안 같은 <b>비율</b>로 줄어든다(곡선형 감소). 반감기가 초기 농도와 무관 → 1차 반응 ②.',
     '13. 다음은 25 ℃, 서로 다른 초기농도에서 시간에 따른 약물 A의 농도 변화이다. 약물 A의 분해반응 차수는? (원본 그래프는 비공개, 아래는 슬라이드에 실린 손그림 그래프)',
     ['0차', '1차', '2차', '3차', '유사 0차'], 2,
     ([('see', '같은 약에 초기 농도 2개(● 약 600, ○ 약 400) → 반감기법으로 판단하라는 신호'),
       ('calc', '● 600 → 약 480 (10시간): ×0.8, ○ 400 → 약 330: ×0.8 정도 → 같은 비율로 감소'),
       ('calc', '● 600 → 300: 약 30~35시간, ○ 400 → 200: 약 30시간 → 반감기 거의 같음'),
       ('link', '반감기가 초기 농도와 무관 = ' + G('1차')),
       ('chk', '0차라면 직선 감소 + 농도가 높을수록 반감기 김. 그래프는 곡선(감소폭이 점점 줄어듦) → 0차 아님'),
       ('done', '② 1차')],
      box('warn', '주의', '원본 그래프가 비공개라 손그림 수치로 판단했어. 수업에서 교수님이 다른 정답을 말씀하셨으면 그걸 따르세요.') +
      box('tip', '반감기법', '[A]<sub>0</sub>를 바꿨을 때 t<sub>1/2</sub>가 비례 → 0차, 그대로 → 1차, 반비례 → 2차.')),
     extra='<img src="img/q2025_graph.png" style="height:52mm;border:1px solid #ccc;border-radius:4px;margin-top:4px">')

quiz('2024', 12, '1차 속도상수와 반감기 비교', ['t<sub>1/2</sub> ∝ 1/k', 'k<sub>A</sub> = k<sub>B</sub>/10', '반감기 10배'],
     '1차 반감기는 t<sub>1/2</sub> = 0.693/k로 k에 반비례. k<sub>A</sub> = 0.1×10<sup>−5</sup> = 1×10<sup>−6</sup> h<sup>−1</sup>는 k<sub>B</sub> = 1×10<sup>−5</sup>의 1/10 → A의 반감기는 B의 10배 ⑤.',
     '13. 25 ℃에서 약물 A와 약물 B는 각각 1차 반응에 의해 분해된다. 약물 A의 1차 반응속도상수가 0.1×10<sup>−5</sup> h<sup>−1</sup>이고, 약물 B의 1차 반응속도상수는 1×10<sup>−5</sup> h<sup>−1</sup>일 때, 약물 A의 반감기는?',
     ['약물 B의 반감기×0.693', '약물 B의 반감기×2', '약물 B의 반감기×2.303', '약물 B의 반감기×5', '약물 B의 반감기×10'], 5,
     ([('see', '둘 다 1차 → t<sub>1/2</sub> = 0.693/k'),
       ('calc', 'k<sub>A</sub> = 0.1×10<sup>−5</sup> = ' + G('1×10<sup>−6</sup> h<sup>−1</sup>') + ', k<sub>B</sub> = 1×10<sup>−5</sup> h<sup>−1</sup>'),
       ('calc', 't<sub>1/2,A</sub>/t<sub>1/2,B</sub> = k<sub>B</sub>/k<sub>A</sub> = 10<sup>−5</sup>/10<sup>−6</sup> = ' + G('10')),
       ('chk', '0.693과 2.303은 공식 속 숫자를 보기로 넣은 함정 — 비율에서는 약분돼 사라짐'),
       ('done', '⑤ 약물 B의 반감기 × 10')],
      box('tip', '직관', 'k가 작다 = 느리게 분해 = 반감기가 길다. k가 1/10이면 반감기는 10배.')))

quiz('2024', 13, '1차 반응 시간 계산', ['t = ln(C<sub>0</sub>/C)/k', '0.105 / 1.05×10<sup>−5</sup>', '10,000 h'],
     '1차: ln(C<sub>0</sub>/C) = kt → t = ln(200/180)/k = 0.105 / (1.05×10<sup>−5</sup> h<sup>−1</sup>) = 1×10<sup>4</sup> h = 10,000 h ③.',
     '14. 25 ℃에서 1차 반응에 따라 분해되는 약물의 분해 반응속도상수는 1.05×10<sup>−5</sup> h<sup>−1</sup>이다. 이 약물의 초기농도가 200 unit/mL일 때 약물의 농도가 180 unit/mL가 될 때까지 걸리는 시간(h)은? (단, ln(200/180) = 0.105이다.)',
     ['100', '1,000', '10,000', '100,000', '1,000,000'], 3,
     ([('see', '1차 + k + 처음·나중 농도 → 시간'),
       ('link', 'ln[A]<sub>t</sub> = −kt + ln[A]<sub>0</sub> → ' + G('ln(C<sub>0</sub>/C) = kt')),
       ('calc', 't = 0.105 / (1.05×10<sup>−5</sup>) = 0.1×10<sup>5</sup> = ' + G('1.0×10<sup>4</sup> h')),
       ('chk', '10% 분해 시간(t<sub>90</sub>, 유효기간) 문제야. 0.105/1.05 = 0.1 → 10<sup>5</sup>×0.1 = 10<sup>4</sup>. 자릿수 실수 주의'),
       ('done', '③ 10,000')],
      box('tip', '유효기간 t<sub>90</sub>', '1차 반응에서 90%가 남을 때까지의 시간 t<sub>90</sub> = 0.105/k. 다음 시간(안정성) 단원에서 다시 나올 공식이야.')))

quiz('2021', 14, '1차 반응 시간 계산 (농도 1/10)', ['ln 10 = 2.3', 't = 2.3/k', '1.0×10<sup>3</sup> h'],
     '5 → 0.5 mg/mL는 1/10로 감소. ln(C<sub>0</sub>/C) = ln 10 = 2.3 log 10 = 2.3 → t = 2.3/(2.3×10<sup>−3</sup> h<sup>−1</sup>) = 1.0×10<sup>3</sup> h ④.',
     '14. 25 ℃에서 어떤 주사제의 분해반응 비반응속도상수 k는 2.3×10<sup>−3</sup> h<sup>−1</sup>이다. 이 주사제의 초기농도가 5 mg/mL일 때, 농도가 0.5 mg/mL로 되는 데 걸리는 시간(h)은? (단, 온도는 일정하고, lnA = 2.3 logA이다.)',
     ['1.0×10<sup>2</sup>', '2.0×10<sup>2</sup>', '6.9×10<sup>2</sup>', '1.0×10<sup>3</sup>', '1.0×10<sup>4</sup>'], 4,
     ([('see', 'k 단위 h<sup>−1</sup> → 1차 반응'),
       ('calc', 'C<sub>0</sub>/C = 5/0.5 = 10 → ln 10 = 2.3 × log 10 = ' + G('2.3')),
       ('calc', 't = ln(C<sub>0</sub>/C)/k = 2.3 / (2.3×10<sup>−3</sup>) = ' + G('1.0×10<sup>3</sup> h')),
       ('chk', '반감기(0.693/k ≈ 301 h)는 농도가 절반일 때. 1/10까지는 반감기 약 3.3번(2.3/0.693) → 301 × 3.3 ≈ 1000 h ✔'),
       ('done', '④ 1.0×10<sup>3</sup>')],
      box('tip', '“비반응속도상수”', '= specific rate constant = 속도 상수 k. 이름에 겁먹지 말기. 단위가 h<sup>−1</sup>이면 1차.')))

quiz('2020', 15, '2차 반응 반감기와 초기 농도', ['비누화 = 2차', '초기 농도 같음 = a', 't<sub>1/2</sub> = 1/ka'],
     '에틸아세테이트 + NaOH 비누화는 2차 반응(각각 1차). 두 반응물의 초기 농도가 a로 같으면 t<sub>1/2</sub> = 1/(ka) → a에 반비례 ③.',
     '13. 다음은 에틸아세테이트의 비누화 반응이다. 에틸아세테이트와 수산화나트륨의 초기농도가 각각 a로 같을 때, 반감기(t<sub>1/2</sub>)와 a와의 관계로 옳은 것은?<br><span style="display:inline-block;border:1px solid #888;padding:2px 8px;margin:4px 0">CH<sub>3</sub>COOC<sub>2</sub>H<sub>5</sub> + NaOH → CH<sub>3</sub>COONa + C<sub>2</sub>H<sub>5</sub>OH</span>',
     ['t<sub>1/2</sub>은 a와 관계없다.', 't<sub>1/2</sub>은 a에 비례한다.', 't<sub>1/2</sub>은 a에 반비례한다.', 't<sub>1/2</sub>은 a<sup>2</sup>에 비례한다.', 't<sub>1/2</sub>은 a<sup>2</sup>에 반비례한다.'], 3,
     ([('see', '반응물 두 개가 1 : 1로 만나는 비누화 → rate = k[에스터][OH<sup>−</sup>] (2차)'),
       ('link', '초기 농도가 같으면 계속 같음 → rate = k[A]<sup>2</sup>와 같은 꼴'),
       ('calc', '2차 반감기 t<sub>1/2</sub> = ' + G('1/(k[A]<sub>0</sub>) = 1/(ka)')),
       ('chk', '⑤ a<sup>2</sup>에 반비례는 3차 반응의 반감기(1/a<sup>2</sup>)와 헷갈리게 한 함정'),
       ('done', '③ a에 반비례')],
      box('tip', '비누화(saponification)', '에스터가 염기(NaOH)에 의해 가수분해되는 반응. 물리약학에서 대표적인 2차 반응 예시야.')))

quiz('2017', 16, '0차 반응 판단', ['일정한 기울기로 감소', '농도 vs 시간 직선', '0차'],
     '일정한 온도에서 약물 함량이 시간에 따라 일정한 기울기로(직선으로) 감소 → [A] vs t가 직선 → 0차 반응 ①.',
     '13. 어떤 과포화된 약물의 유효기간을 결정하려고 한다. 일정한 온도에서 시간에 따른 약물의 함량이 일정한 기울기로 감소하였다. 이 약물의 분해과정은 몇 차 반응인가?',
     ['0차 반응', '1차 반응', '2차 반응', '유사 1차 반응', '유사 2차 반응'], 1,
     ([('see', '“함량이 일정한 기울기로 감소” = 농도 vs 시간 그래프가 직선'),
       ('link', '[A]<sub>t</sub> = −kt + [A]<sub>0</sub> → 직선 + 기울기 −k = ' + G('0차')),
       ('chk', '1차는 ln[A] vs t가 직선, 농도 자체는 곡선. “일정한 기울기”가 농도에 대한 말이면 0차'),
       ('chk', '“유사(pseudo)” 차수는 한 반응물이 아주 많아 농도가 사실상 일정할 때 쓰는 말 — 문제에 그런 조건 없음'),
       ('done', '① 0차 반응')],
      box('tip', '왜 과포화·현탁 약물이 0차?', '녹아 있는 약이 분해되면 고체(또는 과량의 약)가 계속 녹아 보충돼서 용액 농도가 일정 → 분해 속도도 일정 → 겉보기 0차. (교재 내용, 다음 단원과 연결)')))
