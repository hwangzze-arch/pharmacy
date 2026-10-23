# -*- coding: utf-8 -*-
from lib import *
P = 5

PAIRS = [
    ('분배계수 K', '2주차: 물/기름 <b>추출·용해도</b> 비 (K 방향 주의, 진 vs 겉보기)', '5주차: 막 입구 <b>농도 점프</b> C₁ = K·C<sub>d</sub>, P = DK/h', 'BCS 투과도 · pH 분배(비해리형 ↑ = K ↑)'),
    ('Cs (포화 농도)', '2주차: 용해도 그 자체 · 입자 ↓ · 보용매 ↑', '7주차 Noyes-Whitney (Cs − C) · Higuchi A ≫ Cs', 'Class II = Cs가 작아 용출 율속'),
    ('정적 확산층 h', '7주차 Noyes-Whitney: 고체 표면의 물막 (젓기 → h ↓ → 용출 ↑)', '5주차: 막 양쪽 2겹 2h<sub>a</sub>/D<sub>a</sub> (수층 제어 = P<sub>a</sub>C₁/2)', '7주차 캡슐: 바깥 1겹 h<sub>a</sub>'),
    ('0차 방출', '6주차 Reservoir 패치 (막 제어, P<sub>m</sub> &lt; P<sub>skin</sub>)', '7주차 OROS (삼투압 = 압력)', '7주차 실리콘 캡슐 Q = PC<sub>p</sub>t · 공통: 포화 저장소 → ΔC 일정'),
    ('√t 방출', 'Higuchi 1 (균질) · Higuchi 2 (ε, τ)', 'Bottari (R 무시) · K-P n = 0.45', '6주차 Matrix 패치 · 지연시간 tL = h²/6D는 h² (√ 아님)'),
    ('투석 · 한외여과', '4주차 응용: 투석 = 압력 X·크기별 속도 차 / 한외여과 = 압력 O', '3주차: 단백질 결합 측정 (평형투석 · 한외여과 · 동적투석)', '"수압·원심" = 한외여과 · "속도" = 동적투석'),
    ('입자 크기', '2주차: 용해도 S ↑ (0.1 μm 이하에서 의미, Ostwald-Freundlich)', '7주차: 용출 속도 ↑ (Noyes-Whitney의 S ↑)', 'K(분배계수)는 안 바뀜 (5주차 기출 11번)'),
    ('pH 효과', '2주차: 약산은 pH ↑ → 용해도 ↑ (A⁻)', '5주차: 약산은 pH ↓ → 비해리 ↑ → 투과 ↑', '같은 HA ⇌ A⁻ 평형의 양면 — 용해도와 흡수는 반대!'),
    ('저항 R', '5주차 얇은 막 R = h/D (K = 1) · 다층 ΣR', '6주차 패치 1/P = R<sub>m</sub> + R<sub>skin</sub>', '7주차 캡슐 R = hm/Dm + ha/DaKr · 큰 저항 = 율속'),
    ('"1차"라는 말', '7주차 강의: 속도가 감소하는 방출 (Noyes-Whitney, Higuchi)', '수학: 1차 <b>반응</b> = 지수함수 (Noyes-Whitney는 해당)', 'Higuchi는 √t 법칙 → 보기 "1차반응" ✕, "√t 비례" ✓'),
]
rows = ''.join(f'<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td></tr>' for a, b, c, d in PAIRS)
page(P, f'''<section class="page p5" style="font-size:13.4px;line-height:1.48"><div class="ptop"><span class="pl">마무리 ①</span><span class="pt">주차를 넘나드는 "헷갈리는 짝" 10쌍</span><span class="pr">Cross-week traps</span></div>
<table><thead><tr><th style="width:12%">개념</th><th>여기서는…</th><th>저기서는…</th><th>연결 · 함정</th></tr></thead><tbody>{rows}</tbody></table>
<div class="brain"><span class="lab">🧠 한 줄</span>같은 기호(K, Cs, h, R)가 주차마다 다른 자리에서 일한다 — "지금 어느 식의 어느 자리인가?"부터 묻기!</div>{{FOOT}}</section>''')

TOP = [
    ('19', '1차 반응 (화학반응 속도론)', '36.8%', '※ 시험 범위 확인 필요 — 이 책 범위 밖', ''),
    ('22', '약물의 방출과 용출', '39.5%', 'Higuchi 두번째 식 = 일반식 (ε = τ = 1이면 첫번째 식)', 'PART 4 · Higuchi 2'),
    ('4', '해리형 분자의 소장 점막 흡수 (pH 분배가설의 예외)', '44.7%', '해리형도 이온수송체·세포간 경로로 일부 흡수', 'PART 3 · pH 분배 가설'),
    ('11', 'Higuchi 약물방출 모델', '55.3%', '누적 √t 증가 · 속도 1/√t 감소 · 확산거리 증가', 'PART 4 문제 · 2024 중간 11번'),
    ('18 · 23', '화학반응 속도론', '57.9%', '※ 시험 범위 확인 필요', ''),
    ('25', 'BCS 체계', '57.9%', '4칸 위치: 세로 용해도, 가로 투과도 · II = 용출 율속', 'PART 4 · BCS'),
    ('1', '정상상태에 대한 설명', '68.4%', 'dC/dx 일정, dC/dt = 0, 평형(기울기 0)과 구분', 'PART 3 · 정상상태'),
]
trows = ''.join(f'<tr><td>{a}</td><td>{b}</td><td style="color:#c62828;font-weight:800">{c}</td><td>{d}</td><td>{e}</td></tr>' for a, b, c, d, e in TOP)
page(P, f'''<section class="page p5"><div class="ptop"><span class="pl">마무리 ②</span><span class="pt">2024 중간고사 오답률 TOP — 정답률 낮은 순</span><span class="pr">2024 Midterm review</span></div>
<table><thead><tr><th>번호</th><th>주제</th><th>정답률</th><th>꼭 기억할 한 줄</th><th>이 책 위치</th></tr></thead><tbody>{trows}</tbody></table>
<div class="grid2" style="margin-top:8px">
<div>{sh('🎯 시험 직전 우선순위')}{ul(['<b>1순위</b>: Higuchi(√t·가정·Higuchi 2), pH 분배 가설의 예외, BCS 4칸 — 오답률 상위가 모두 7주차·5주차', '<b>2순위</b>: 정상상태 vs 평형, Fick 1·2법칙, 다층 저항, 막/수층 제어', '<b>3순위</b>: 2주차 계산(침전 pH·추출 양의 비), 3주차 키워드 짝(CD 6·7·8, 투석 3종)'])}</div>
<div>{warn('19·18·23번 "화학반응 속도론"은 2024년 범위였지만 올해 2–7주차 자료에는 없어요. 올해 범위에 포함되는지 공지를 꼭 확인!', '⚠️ 범위 확인')}
{sh('📝 2024 리뷰 건의사항 → 이 책의 대응')}{ul(['"예제·연습문제를 더" → 강의 문제 + 소그룹 32문제 전부 수록', '"빈칸이 있는지 헷갈림" → 모든 빈칸 정답을 문제·개념에 명시'])}</div></div>{{FOOT}}</section>''')

CS = [
    ('w1', '침전 pH (약산)', 'pH = pKa + log((S − S₀)/S₀)', 'pKa ≠ 침전 pH · S는 g/L ÷ MW'),
    ('w1', '보용매 (알코올)', '극성 ↓ → S₀ ↑ · Ka ↓ (pKa ↑)', '침전 pH ↓ · pH 자체는 안 바뀜'),
    ('w1', '입자 크기', 'log(S/S₀) = 2γV/(2.303RTr)', 'r ↓ → S ↑ · R = 8.314×10⁷ erg'),
    ('w1', '분배 · 추출', '진 = HA끼리 · 겉보기 = 총량', '양의 비 = K·V추출 : V원래 · 나눠서 여러 번'),
    ('w2', '루이스 · 배위수', '염기 = 전자쌍 줌 · 배위수 = 받은 전자쌍', 'en ×2 · EDTA ×6 · 6배위 = 팔면체'),
    ('w2', '착물 3종', '금속(배위결합) · 유기분자(약함, 3 Å↑)', '내포 = 결합 X, 크기·자리 · 카페인 2번 N = 산'),
    ('w2', '시클로덱스트린', 'α β γ = 6 7 8 · 겉 친수 속 소수', '단분자 · 1:1 · 메틸화 → 수용성 ↑'),
    ('w2', '단백질 결합', '평형투석 안 &gt; 밖 · 한외여과 수압·원심', '동적투석 = 소실 속도 ∝ 유리 약물'),
    ('w3', 'Fick 1 · 2법칙', 'J = −D ∂C/∂x · ∂C/∂t = D ∂²C/∂x²', '1 = 정상 · 2 = 비정상+정상 모두'),
    ('w3', '정상상태 · 싱크', 'dC/dx 일정 · dC/dt = 0 · C<sub>r</sub> 5~10% 이하', '평형(기울기 0)과 구분 · M은 계속 증가'),
    ('w3', '투과도 P', 'P = DK/h (cm/s) · dM/dt = PSC<sub>d</sub>', '두께 무관은 D · K는 단위 없음'),
    ('w3', '투과 실험', '기울기 = dM/dt · x절편 = tL = h²/6D', 'y축 M/S면 기울기 = J'),
    ('w3', '다층 · 정적층', 'R = ΣR · P = 1/R · R = 2h<sub>a</sub>/D<sub>a</sub> + h<sub>m</sub>/D<sub>m</sub>K', '막의 K = C₃/C₂ · 물층 K 없음'),
    ('w3', '막 / 수층 제어', 'J = P<sub>m</sub>C₁ / J = P<sub>a</sub>C₁/2', '율속 = 저항 큰 쪽 · 교반 ↑ → 수층 제어만 J ↑'),
    ('w3', 'pH 분배 · 패치', '비해리형만 기름벽 통과', 'Reservoir = 막 제어(P<sub>m</sub> &lt; P<sub>skin</sub>)'),
    ('w4', '0차 · OROS', 'Q = Q₀ + K₀t · 구동력 = 삼투압(압력)', 'Δπ ↑ → 방출 ↑ · 장용제 = 지연(DR)'),
    ('w4', 'Noyes-Whitney', 'dM/dt = (DS/h)(Cs − C)', '1차 · K 없음 · 세제곱근은 Hixson-Crowell'),
    ('w4', 'Higuchi', 'Q = √(D(2A − Cs)Cs t) ∝ √t', 'dQ/dt ∝ 1/√t · 가정 4개 · 모양 불변'),
    ('w4', 'Higuchi 2 · Bottari · K-P', 'ε ↑ 방출 ↑ · τ ↑ 방출 ↓', 'Bottari = 연고·정제 · K-P n 0.45 = Fick'),
    ('w4', 'BCS', 'II = 용해도 ↓ → 용출 율속', '친수성 ↑ → 용해 ↑ 투과 ↓ · IV 상용화 어려움'),
]
cells = ''.join(f'<div><div class="h {w}">{a}</div><div class="f">{b}</div><div class="d">{c}</div></div>' for w, a, b, c in CS)
page(P, f'''<section class="page p5"><div class="ptop"><span class="pl">마무리 ③</span><span class="pt">시험 직전 5분 — 2–7주차 한 장 정리</span><span class="pr"><span style="color:#0e7c86">■ 2주차</span> · <span style="color:#7b3fb5">■ 3주차</span> · <span style="color:#4954d1">■ 4–6주차</span> · <span style="color:#c4501f">■ 7주차</span></span></div>
<div class="cs">{cells}</div>
<div class="brain"><span class="lab">🧠 전 범위 한 문장</span>녹아야(Cs) → 나뉘고(K) → 퍼져서(J = DKΔC/h) → 나온다(√t · 0차) — 착물은 이 흐름을 조절하는 도구!</div>{{FOOT}}</section>''')
