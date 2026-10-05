# -*- coding: utf-8 -*-
"""15장 시험대비 요약노트.  python3 exam15.py → exam_ch15.pdf"""
import os, sys
os.environ['CH'] = '15'
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from helpers import *
import examlib
import ch15
from ch15 import cascade

CH = 15
CH_TITLE = '대사 조절의 원리'
FOOT = 'Lehninger 8e · Ch.15 대사 조절의 원리 — 시험대비 요약노트'

_items = [i for i in ch15.ALL_ITEMS if i['level'] < 3]
WB = {i['id']: 6 + k for k, i in enumerate(_items)}
link = examlib.make_link(WB, CH)
page = examlib.make_page(link)


# ------------------------------------------------------------------ drawings
def mm_curve():
    W, H = 520, 230
    L, R, Tp, B = 50, 500, 18, 190
    xmax = 20.0
    def X(v): return L + v / xmax * (R - L)
    def Y(f): return B - f * (B - Tp)
    b = f'<line x1="{L}" y1="{B}" x2="{R}" y2="{B}" stroke="{C["gray"]}"/><line x1="{L}" y1="{Tp}" x2="{L}" y2="{B}" stroke="{C["gray"]}"/>'
    b += f'<rect x="{X(4)}" y="{Tp}" width="{X(8)-X(4)}" height="{B-Tp}" fill="#fef3c7" opacity=".7"/>' + T(X(6), Tp + 14, '혈당 범위 4–8 mM', 10, '#a16207', weight=700)
    for km, col, lab in [(0.1, C['blue'], 'HK I·II (근육) Km 0.1 mM'), (10, C['orange'], 'HK IV (간) Km ≈ 10 mM')]:
        pts = ' '.join(f'{X(s):.1f},{Y(s/(s+km)):.1f}' for s in [i * 0.1 for i in range(0, 201)])
        b += f'<polyline points="{pts}" fill="none" stroke="{col}" stroke-width="3"/>'
    b += T(X(14), Y(0.99) + 16, 'HK I·II: 이미 포화 (혈당 변화에 둔감)', 10.5, C['blue'], weight=700)
    b += T(X(15), Y(0.42) + 16, 'HK IV: 혈당에 비례 = 혈당 센서', 10.5, C['orange'], weight=700)
    for v in [0, 5, 10, 15, 20]:
        b += T(X(v), B + 16, str(v), 10, C['gray'])
    b += T((L + R) / 2, B + 34, '[포도당] (mM)', 10.5, C['ink'], weight=700)
    b += f'<text x="16" y="{(Tp+B)/2}" font-size="10" fill="{C["ink"]}" font-weight="700" text-anchor="middle" transform="rotate(-90 16 {(Tp+B)/2})">v / Vmax</text>'
    return svg(W, H + 14, b)


def glut_bars():
    return bars([('GLUT3 (뇌)', 1.0, C['purple'], 'Kt 매우 낮음 → 저혈당에도 확보'), ('GLUT1 (적혈구)', 1.5, C['blue'], 'Kt 1.5 mM → 늘 포화'),
                 ('GLUT4 (근육·지방)', 5, C['green'], 'Kt 5 mM · 인슐린 의존'), ('GLUT2 (간·이자)', 66, C['orange'], 'Kt ~66 mM → 혈당 비례')],
                height=150, vmax=110, width=560)


def f26bp_switch():
    W, H = 560, 200
    b = arrowdef('fs1', C['green']) + arrowdef('fs2', C['red'])
    b += f'<rect x="200" y="70" width="160" height="56" rx="12" fill="#fefce8" stroke="#eab308" stroke-width="2"/>' + T(280, 94, 'PFK-2 / FBPase-2', 12, '#a16207', weight=900) + T(280, 112, '한 단백질 · 두 활성', 10, C['gray'])
    b += f'<rect x="10" y="20" width="160" height="50" rx="10" fill="#f0fdf4" stroke="{C["green"]}" stroke-width="2"/>' + T(90, 40, '인슐린 · Xu5P', 11.5, C['green'], weight=900) + T(90, 58, '→ 탈인산화 (PP2A)', 10, C['ink'])
    b += f'<rect x="10" y="126" width="160" height="50" rx="10" fill="#fef2f2" stroke="{C["red"]}" stroke-width="2"/>' + T(90, 146, '글루카곤', 11.5, C['red'], weight=900) + T(90, 164, '→ cAMP → PKA 인산화', 10, C['ink'])
    b += f'<line x1="172" y1="50" x2="198" y2="82" stroke="{C["green"]}" stroke-width="2" marker-end="url(#fs1)"/><line x1="172" y1="150" x2="198" y2="116" stroke="{C["red"]}" stroke-width="2" marker-end="url(#fs2)"/>'
    b += f'<rect x="390" y="20" width="160" height="50" rx="10" fill="#f0fdf4" stroke="{C["green"]}"/>' + T(470, 40, 'PFK-2 ON → F2,6BP ↑', 11, C['green'], weight=900) + T(470, 58, 'PFK-1 ↑ · FBPase-1 ↓ = 해당', 10, C['ink'])
    b += f'<rect x="390" y="126" width="160" height="50" rx="10" fill="#fef2f2" stroke="{C["red"]}"/>' + T(470, 146, 'FBPase-2 ON → F2,6BP ↓', 11, C['red'], weight=900) + T(470, 164, 'PFK-1 ↓ · FBPase-1 ↑ = 당신생', 10, C['ink'])
    b += f'<line x1="362" y1="86" x2="388" y2="50" stroke="{C["green"]}" stroke-width="2" marker-end="url(#fs1)"/><line x1="362" y1="110" x2="388" y2="150" stroke="{C["red"]}" stroke-width="2" marker-end="url(#fs2)"/>'
    return svg(W, H, b)


def glycogen_tree():
    W, H = 300, 240
    b = f'<circle cx="150" cy="105" r="14" fill="{C["orange"]}"/>' + T(150, 109, 'G', 11, 'white', weight=900)
    import math
    def branch(x, y, ang, depth):
        nonlocal b
        if depth == 0:
            return
        x2, y2 = x + 27 * math.cos(ang), y + 27 * math.sin(ang)
        for k in range(4):
            px, py = x + (x2 - x) * k / 3, y + (y2 - y) * k / 3
            b += f'<circle cx="{px:.1f}" cy="{py:.1f}" r="3.2" fill="{C["blue"]}"/>'
        b += f'<line x1="{x:.1f}" y1="{y:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{C["blue"]}" stroke-width="1.5"/>'
        branch(x2, y2, ang - 0.45, depth - 1)
        branch(x2, y2, ang + 0.45, depth - 1)
    for a in [0, 2.1, 4.2]:
        branch(150, 105, a, 3)
    b += T(150, 232, 'G = 글리코게닌 (중심) · 파란 점 = 포도당 · 갈래 = (α1→6) 가지', 9.5, C['gray'])
    return svg(W, H, b)


def steady_state():
    return flow(['A (공급)', 'S (예: 혈당 5 mM)', 'P (소비)'], arrow_labels=['V₁ (식사·간)', 'V₂ (뇌·근육)'], width=460, box_h=40,
                colors=[C['navy'], C['orange'], C['navy']])


def amp_bars():
    return bars([('[ATP] 5.0 → 4.5 mM', 10, C['blue'], '−10%'), ('[AMP] 0.1 → 0.6 mM', 500, C['red'], '+500% (6배)')], height=90, vmax=520)


def mca_bars():
    return bars([('헥소키나아제 IV', 0.79, C['orange'], 'C = 0.79'), ('PFK-1', 0.21, C['blue'], 'C = 0.21'), ('포스포헥소스 이성질화효소', 0.005, C['gray'], 'C ≈ 0')], height=120, vmax=1.0)


# ------------------------------------------------------------------ summary pages
SUMMARY = []

SUMMARY.append(page('S1', '해당과정 ⇄ 당신생 — 왜 조절이 필요한가', 'Slides 4–6',
  '같은 세포질에 정반대 경로가 같이 있다. 둘이 동시에 돌면 ATP만 버리는 <b>헛된 회로(futile cycle)</b>. 그래서 비가역 3곳(①③⑩)에 서로 다른 효소를 두고 <b>반대로(상반, reciprocal)</b> 조절한다.',
  f'''<div class="grid2"><div class="card"><h4>📌 우회 지점 3곳 = 조절 지점</h4>{table(['단계', '해당과정', '당신생'], [
  ['Step 1', '헥소키나아제', 'G6Pase'], ['Step 3', '<b>PFK-1</b>', '<b>FBPase-1</b>'], ['Step 10', '피루브산 키나아제', 'PC → PEPCK']])}
 {key('같은 신호가 한쪽은 <b>켜고</b> 다른 쪽은 <b>끈다</b>. 예: AMP → PFK-1 ↑, FBPase-1 ↓.')}
 <p>F6P + ATP → F1,6BP + ADP 와 F1,6BP + H₂O → F6P + Pᵢ 가 동시에 돌면, 알짜 = <b>ATP + H₂O → ADP + Pᵢ</b> (열만 남음).</p></div>
<div class="card"><h4>조절 방법은 시간 규모가 다르다</h4>{table(['방법', '시간', '예 (15장)'], [
  ['알로스테릭', '밀리초~초', 'ATP·AMP·시트르산·F2,6BP → PFK-1'], ['인산화 (호르몬)', '초~분', 'PKA → 간 PK, PFK-2/FBPase-2'], ['전사·분해 (효소 양)', '시간~일', 'ChREBP, FOXO1 → HK IV·G6Pase·PEPCK']], cls='left')}
 {tip('헛된 회로가 완전히 쓸모없지는 않다: 약간 돌게 두면 신호에 아주 민감하게 반응하고, 열을 내기도 한다 (벌의 비행근).', '참고')}</div></div>''',
  ('P11',)))

SUMMARY.append(page('S2', 'Step 1 — 헥소키나아제 동종효소와 GLUT', 'Slides 7–11',
  '근육의 헥소키나아제(HK I·II)는 <b>Km이 아주 낮아</b> 늘 포화(자기가 쓸 포도당 확보). 간의 <b>HK IV(글루코키나아제)</b>는 Km이 높아 혈당에 <b>비례</b>해 일하는 혈당 센서.',
  f'''<div class="grid2"><div class="card"><figure class="fig">{mm_curve()}</figure>
 {table(['', 'HK I·II (근육)', 'HK IV (간)'], [['Km', '0.1 mM', '~10 mM'], ['혈당 5 mM에서', '거의 포화', '절반쯤'], ['G6P 억제', '○ (산물 억제)', '✕ → <b>조절 단백질</b>이 조절']])}</div>
<div><div class="card"><h4>📌 간 HK IV — 핵에 숨었다 나온다 (슬라이드 10)</h4>{table(['상태', 'HK IV 위치', '활성'], [['공복 (F6P ↑)', '조절 단백질과 함께 <b>핵</b>', '꺼짐'], ['식후 (고혈당)', '포도당이 풀어 줌 → <b>세포질</b>', '켜짐']])}</div>
 <div class="card" style="margin-top:3mm"><h4>📌 포도당 수송체 GLUT (Kt = 수송체의 Km)</h4>{glut_bars()}
 <p class="small">Kt가 낮을수록 적은 포도당도 잘 붙잡음. 간은 GLUT2(높은 Kt) + HK IV(높은 Km) 조합으로 혈당을 비례 감지.</p></div></div></div>''',
  ('P2',)))

SUMMARY.append(page('S3', 'GLUT4와 인슐린 · 1형 당뇨', 'Slides 12–13',
  '근육·지방의 GLUT4는 평소 세포 안 <b>소포에 숨어</b> 있다가 인슐린이 오면 세포막으로 올라온다. 조절되는 건 GLUT4의 총량이 아니라 <b>막에 나와 있는 수</b>.',
  f'''<div class="grid2"><div class="card"><h4>📌 GLUT4 소포 순환</h4>{vflow(['인슐린이 수용체에 결합', 'GLUT4 소포 → 세포막과 융합', '포도당 유입 ↑ (근육·지방)', '인슐린 떨어지면 → 다시 소포로 (세포내이입)'], colors=[C['green'], C['blue'], C['orange'], C['gray']], box_h=26, gap=20, width=520, font=11, bw=440)}
 {table(['', '인슐린 있음 (식후)', '없음 (공복)'], [['GLUT4 위치', '세포막', '세포 안 소포'], ['포도당 흡수', '↑↑', '↓']])}</div>
<div><div class="card"><h4>📌 1형 당뇨 — “혈당은 높은데 세포는 굶는다”</h4><ol style="margin:.2em 0;padding-left:1.3em"><li>인슐린 없음 → GLUT4가 막으로 못 감</li><li>혈당 ↑↑, 세포 안은 포도당 기아</li><li>지방 분해 ↑ → 지방산 산화 → 아세틸-CoA 과잉</li><li>간에서 <b>케톤체</b> 과다 → 혈액 산성화 = <b>케톤산증</b></li></ol>
 <p class="small">케톤체 = 아세토아세트산, β-하이드록시뷰티르산, 아세톤 (17장).</p></div>
 {warn('GLUT1·2·3은 인슐린과 무관. <b>GLUT4만</b> 인슐린으로 막 위치가 바뀐다.', '함정')}
 {tip('근육 운동도(AMPK·Ca²⁺) GLUT4를 막으로 올린다 → 운동이 혈당을 낮추는 이유.', '연결')}</div></div>''',
  ('P9',)))

SUMMARY.append(page('S4', 'Step 3 — PFK-1 / FBPase-1과 과당 2,6-이인산', 'Slides 14–19',
  'PFK-1은 해당과정의 핵심 조절 효소. <b>ATP·시트르산</b>(에너지 넉넉)은 끄고, <b>AMP·ADP·과당 2,6-이인산(F2,6BP)</b>은 켠다. FBPase-1은 정반대.',
  f'''<div class="grid2"><div><div class="card"><h4>📌 상반 조절 표 (슬라이드 16–17)</h4>{table(['조절자', 'PFK-1 (해당)', 'FBPase-1 (당신생)', '의미'], [
  ['ATP', '⊗', '', '에너지 충분'], ['시트르산', '⊗', '', 'TCA 재료 충분'], ['ADP', '▲', '', '에너지 부족'], ['AMP', '▲', '⊗', '에너지 크게 부족'], ['<b>F2,6BP</b>', '<b>▲▲</b>', '<b>⊗</b>', '“해당 돌려라” (호르몬 신호)']])}</div>
 <div class="card" style="margin-top:3mm"><h4>ATP는 기질이자 억제제</h4><figure class="fig">{img('c14_p19.png', '58%')}</figure>
 <p class="small">활성 부위(친화도 높음) = 기질 / 알로스테릭 부위(친화도 낮음) = ATP 많을 때만 채워져 억제.</p></div></div>
<div><div class="card"><h4>📌 F2,6BP는 누가 만드나? (슬라이드 18)</h4><figure class="fig">{f26bp_switch()}</figure>
 <p><b>인산화 = FBPase-2 활성 = F2,6BP ↓ = 당신생</b>. 거꾸로 외우지 않게 주의!</p></div>
 <div class="card" style="margin-top:3mm"><h4>자일룰로스 5-인산(Xu5P) — 음식 신호 (슬라이드 19)</h4><p>탄수화물을 많이 먹으면 PPP의 Xu5P ↑ → <b>PP2A</b> 활성 → PFK-2 탈인산화 → F2,6BP ↑ → 해당·지방산 합성 ↑ (남는 포도당 → 지방).</p></div>
 {warn('<b>F1,6BP</b> = 해당 중간체(PFK-1 산물) / <b>F2,6BP</b> = 조절 전용 신호. 이름만 비슷하다.', '함정')}</div></div>''',
  ('P6',)))

SUMMARY.append(page('S5', 'Step 10 — 피루브산 키나아제 · PC · PDH', 'Slides 20–22',
  '간에서는 공복 때 <b>PKA가 피루브산 키나아제(L형)를 인산화해 꺼서</b> PEP를 당신생으로 보낸다. <b>아세틸-CoA</b>가 많으면 PDH는 끄고 PC는 켜서 피루브산도 당신생 쪽으로.',
  f'''<div class="grid2"><div class="card"><h4>📌 피루브산 키나아제 조절</h4>{table(['신호', '효과', '설명'], [
  ['글루카곤 → PKA (간 L형만)', 'PK <b>OFF</b>', '공복: 포도당 아끼기'], ['F1,6BP', 'PK <b>ON</b>', '<b>피드포워드</b>: 앞에서 쌓이면 뒤를 미리 열어 줌'],
  ['ATP · 아세틸-CoA · 긴사슬 지방산 · 알라닌', 'PK <b>OFF</b>', '에너지·연료 충분']], cls='left')}
 <p class="small">근육형(M)은 PKA로 인산화되지 않는다 → 근육은 에피네프린 때 해당과정을 계속 돌린다.</p></div>
<div class="card"><h4>📌 아세틸-CoA = 피루브산의 교통정리 (슬라이드 22)</h4>{flow(['피루브산', 'OAA → 당신생'], arrow_labels=['PC ▲ (아세틸-CoA가 켬)'], width=440, colors=[C['navy'], C['green']], box_h=36)}
 {flow(['피루브산', '아세틸-CoA → TCA'], arrow_labels=['PDH ⊗ (아세틸-CoA가 끔)'], width=440, colors=[C['navy'], C['red']], box_h=36)}
 {key('아세틸-CoA가 넘친다 = 지방산 산화 중(주로 공복) → 피루브산은 태우지 말고 포도당 만드는 데 써라.')}</div></div>''',
  ('P6', 'P11')))

SUMMARY.append(page('S6', '전사 조절 — ChREBP와 FOXO1', 'Slides 23–27',
  '오래 지속되는 상황엔 효소의 <b>양</b>을 바꾼다. 포도당이 많으면 <b>ChREBP</b>가 해당·지방 합성 유전자를 켜고, 공복엔 <b>FOXO1</b>이 당신생 유전자(PEPCK·G6Pase)를 켠다.',
  f'''<div class="grid2"><div class="card"><h4>📌 ChREBP — 해당 ON (슬라이드 24)</h4>{vflow(['포도당 ↑ → G6P → PPP → Xu5P ↑', 'PP2A 활성 → ChREBP 탈인산화', 'ChREBP 핵으로 이동 + Mlx와 짝', 'ChoRE에 결합 → 해당·지방산 합성 효소 전사 ↑'], colors=[C['orange'], C['green'], C['blue'], C['green']], box_h=24, gap=16, width=520, font=10.5, bw=470)}
 <p class="small">같은 Xu5P 신호가 즉각(F2,6BP ↑)과 장기(ChREBP) 두 층으로 해당과정을 켠다.</p></div>
<div><div class="card"><h4>📌 FOXO1 — 당신생 ON (슬라이드 25)</h4>{table(['', '인슐린 있음 (식후)', '없음 (공복)'], [['FOXO1', 'PKB가 인산화 → <b>분해</b>', '탈인산화 → 핵에 존재'], ['PEPCK·G6Pase 전사', '↓', '↑'], ['결과', '당신생 ↓', '당신생 ↑']])}
 {key('짝으로 외우기: <b>ChREBP (해당 ON) ↔ FOXO1 (당신생 ON)</b>. 인슐린 하나가 두 경로를 반대로 움직인다.')}</div>
 <div class="card" style="margin-top:3mm"><h4>PEPCK 프로모터 — 신호의 통합 (슬라이드 26)</h4>{table(['신호', '전사인자'], [['글루카곤 (cAMP)', 'CREB'], ['코르티솔', 'GR'], ['갑상선 호르몬', 'T3R'], ['인슐린', 'FOXO1 제거']], cls='left')}
 <p class="small">표를 다 외우기보다 “유전자 하나가 여러 신호를 통합한다”가 핵심.</p></div></div></div>''',
  ()))

SUMMARY.append(page('S7', '글리코겐의 구조와 분해', 'Glycogenolysis · Slides 29–35',
  '글리코겐 = 포도당이 (α1→4)로 이어지고 8–12개마다 (α1→6)로 가지 친 큰 저장 분자. 분해는 <b>인산분해</b>: 글리코겐 인산화효소가 끝에서 하나씩 <b>포도당 1-인산(G1P)</b>으로 떼어 낸다.',
  f'''<div class="grid2"><div><div class="card"><h4>글리코겐 입자</h4><figure class="fig">{glycogen_tree()}</figure>
 <p class="small">β입자(~21 nm, 포도당 ~55,000개, 근육) → 20–40개가 모여 α입자(로제트, ~100 nm, 간). 가지가 많을수록 끝(비환원 말단)이 많아 빨리 분해·합성할 수 있다.</p></div></div>
<div><div class="card"><h4>📌 분해 4단계</h4>{table(['단계', '효소', '하는 일'], [
  ['①', '<b>글리코겐 인산화효소</b> (PLP)', '(α1→4) 끝을 Pᵢ로 잘라 G1P. 가지점 4개 앞에서 멈춤'],
  ['②', '<b>가지제거 효소</b>', '3개를 옆 사슬로 옮기고(전이효소), 남은 (α1→6) 1개를 가수분해 → 유리 포도당'],
  ['③', '포스포글루코뮤테이스', 'G1P → G6P'],
  ['④', '<b>G6Pase</b> (간·신장 소포체)', 'G6P → 포도당 → 혈액 (근육에는 없음!)']], cls='left')}</div>
 <div class="card" style="margin-top:3mm"><h4>근육 vs 간 — 같은 G6P, 다른 운명</h4>{table(['', '근육', '간'], [['G6P의 행선지', '해당과정 → 자기 ATP', 'G6Pase → 포도당 → 혈당 유지'], ['분해 신호', '에피네프린, AMP, Ca²⁺', '글루카곤, 에피네프린']])}</div>
 {tip('인산분해 덕분에 ATP 1개 절약 (14장 예제 14-1). 세포 속 [Pᵢ]/[G1P] &gt; 100이라 표준값(+3.1)과 상관없이 분해 방향으로 간다.', '연결')}</div></div>''',
  ('P1', 'P2', 'P3')))

SUMMARY.append(page('S8', '글리코겐 합성', 'Glycogenesis · Slides 36–41',
  '합성은 분해의 역반응이 아니다. 포도당을 먼저 <b>UDP-포도당</b>으로 활성화하고, <b>글리코겐 합성효소</b>가 (α1→4)로 늘리고, <b>가지형성 효소</b>가 (α1→6) 가지를 만든다. 시작은 <b>글리코게닌</b>.',
  f'''<div class="grid2"><div class="card"><h4>📌 합성 단계</h4>{table(['단계', '효소', '반응'], [
  ['①', 'UDP-포도당 피로포스포릴레이스', 'G1P + UTP → <b>UDP-포도당</b> + PPᵢ (PPᵢ → 2Pᵢ로 당김)'],
  ['②', '<b>글리코겐 합성효소 (GS)</b>', 'UDP-포도당의 포도당을 비환원 말단에 (α1→4)로 붙임'],
  ['③', '<b>가지형성 효소</b>', '6–7개 조각을 떼어 (α1→6)로 옆에 붙임 (4개 이상 떨어진 곳)'],
  ['④', '<b>글리코게닌</b>', '자기 Tyr에 포도당을 붙여 첫 사슬(프라이머) 시작 — GS는 맨손으로 시작 못 함']], cls='left')}</div>
<div><div class="card"><h4>분해 vs 합성 한눈에</h4>{table(['', '분해', '합성'], [['핵심 효소', '글리코겐 인산화효소', '글리코겐 합성효소'], ['포도당 형태', 'G1P (Pᵢ로 자름)', 'UDP-포도당 (UTP로 활성화)'], ['가지', '가지제거 효소', '가지형성 효소'], ['에너지', 'ATP 절약', '포도당당 UTP 1개 소비']])}</div>
 {key('왜 따로? → 두 경로를 <b>따로 조절</b>하려고. 그리고 합성 쪽은 UTP·PPᵢ 분해로 확실히 한 방향.')}
 {warn('“가지가 왜 필요?” → ① 물에 잘 녹고 ② 끝이 많아 한꺼번에 빨리 꺼내고 붙일 수 있다.', '시험')}</div></div>''',
  ()))

SUMMARY.append(page('S9', '세 호르몬 — 인슐린 · 글루카곤 · 에피네프린', 'Slides 45–47',
  '<b>인슐린 = “저장하라”</b>(혈당 ↑일 때 이자 β세포), <b>글루카곤 = “꺼내라”</b>(혈당 ↓일 때 α세포, 주로 간), <b>에피네프린 = “위기! 당장 써라”</b>(부신수질, 간·근육).',
  f'''<div class="card"><h4>📌 호르몬 효과 표 (슬라이드 47)</h4>{table(['경로', '인슐린 · 간', '인슐린 · 근육', '글루카곤 · 간', '글루카곤 · 근육', '에피 · 간', '에피 · 근육'], [
 ['해당과정', '↑', '↑', '↓', '–', '↓', '<b>↑</b>'], ['당신생', '↓', '–', '↑', '–', '↑', '–'], ['글리코겐 합성', '↑', '↑', '↓', '–', '↓', '↓'], ['글리코겐 분해', '↓', '↓', '↑', '–', '↑', '↑']])}
 <p class="small">“–” = 수용체나 효소가 없어 영향 없음. 근육에는 <b>글루카곤 수용체가 없다</b>.</p></div>
<div class="grid2" style="margin-top:3mm"><div class="card"><h4>신호 경로</h4>{table(['호르몬', '경로'], [['인슐린', '수용체 티로신 키나아제 → PKB(Akt) → GSK3 ⊗, PP1 ▲, GLUT4 ↑'], ['글루카곤·에피네프린', 'G 단백질 → 아데닐산 고리화효소 → <b>cAMP → PKA</b>'], ['(근육) 수축', 'Ca²⁺ → 인산화효소 b 키나아제 ▲']], cls='left')}</div>
 <div class="card">{tip('에피네프린 때 <b>간은 해당 ↓</b>(포도당을 내보내야 하니까), <b>근육은 해당 ↑</b>(자기가 태워서 도망가야 하니까). 시험 단골!', '포인트')}
 {key('PKA = 글루카곤·에피네프린의 실행자. PKA가 인산화하면 → 분해 ON, 합성 OFF, 당신생 ON.')}</div></div>''',
  ('P11',)))

SUMMARY.append(page('S10', '글리코겐 분해의 조절 — 인산화 연쇄와 포도당 센서', 'Slides 48–50',
  '글리코겐 인산화효소는 <b>인산이 붙으면 활성(a형)</b>, 떨어지면 덜 활성(b형). 호르몬 신호가 여러 단계를 거치며 <b>증폭</b>되어 극소량 호르몬으로 G1P가 만 배 이상 나온다.',
  f'''<div class="grid2"><div class="card"><h4>📌 증폭 연쇄 (슬라이드 49)</h4><figure class="fig">{cascade()}</figure></div>
<div><div class="card"><h4>📌 활성화 스위치 정리</h4>{table(['조절', '효과', '어디서'], [['PKA → 인산화효소 b 키나아제 → Ser14-P', 'b → <b>a (ON)</b>', '간·근육'], ['AMP (알로스테릭)', 'b형도 활성', '근육 (에너지 부족)'], ['Ca²⁺ (근수축)', '인산화효소 b 키나아제 ON', '근육'], ['<b>포도당</b> (알로스테릭)', 'a → b (OFF)', '<b>간</b>'], ['PP1 (인슐린)', '탈인산화 → OFF', '간·근육']], cls='left')}</div>
 <div class="card" style="margin-top:3mm"><h4>간의 인산화효소 = 혈당 센서 (슬라이드 50)</h4><p>혈당 ↑ → 간세포 포도당 ↑ → 포도당이 인산화효소 a에 결합 → Ser14-P가 드러남 → <b>PP1이 인산 제거</b> → b형 → 분해 정지. “혈당 충분하니 그만 꺼내.”</p></div></div></div>''',
  ('P4', 'P10')))

SUMMARY.append(page('S11', '글리코겐 합성의 조절 — GSK3 · CKII · PP1', 'Slides 51–53',
  '글리코겐 합성효소(GS)는 인산화효소와 <b>정반대</b>: <b>인산이 붙으면 꺼진다(b형)</b>. 인슐린은 GSK3를 막고 PP1을 켜서 GS를 탈인산화(활성) 상태로 만든다.',
  f'''<div class="grid2"><div><div class="card"><h4>📌 같은 인산화, 반대 결과</h4>{table(['효소', '인산화되면', '탈인산화되면'], [['글리코겐 인산화효소', '<b>a = ON</b>', 'b = OFF'], ['글리코겐 합성효소', 'b = OFF', '<b>a = ON</b>']])}
 {key('PKA가 인산화 → 분해 ON + 합성 OFF / PP1이 탈인산화 → 분해 OFF + 합성 ON. 하나의 스위치로 두 효소를 반대로!')}</div>
 <div class="card" style="margin-top:3mm"><h4>GSK3와 프라이밍 (슬라이드 51–52)</h4>{vflow(['CKII가 GS를 먼저 인산화 (프라이밍)', 'GSK3가 그 옆 Ser들을 인산화 → GS OFF', '인슐린 → PKB → GSK3 인산화 → GSK3 OFF', 'PP1이 GS 탈인산화 → GS ON → 합성 ↑'], colors=[C['gray'], C['red'], C['green'], C['green']], box_h=24, gap=16, width=520, font=10.5, bw=470)}
 <p class="small">G6P는 GS b를 알로스테릭으로 활성화하기도 한다 (포도당이 넘치면 저장).</p></div></div>
<div class="card"><h4>📌 GM — PP1을 붙잡는 닻 (슬라이드 53)</h4>{table(['', '인슐린', '에피네프린'], [['GM 인산화 자리', '자리 1', '자리 2 (PKA)'], ['PP1', '글리코겐에 붙어 활성', '떨어져 나감 + 억제제 1이 억제'], ['인산화효소', '탈인산 → OFF', '인산 유지 → ON'], ['GS', '탈인산 → ON', '인산 유지 → OFF'], ['결과', '<b>합성</b>', '<b>분해</b>']])}
 {warn('억제제 1(inhibitor 1)은 PKA에 인산화되면 PP1을 막는다. 억제제 1이 없으면 PP1이 계속 일해 분해 신호에 둔감 (풀이노트 문제 10b).', '함정')}</div></div>''',
  ('P10',)))

SUMMARY.append(page('S12', '간 vs 근육 — 고혈당 · 저혈당에서의 조절', 'Slides 54–57',
  '간은 몸 전체를 위해 혈당을 맞추는 <b>“너그러운” 장기</b>, 근육은 자기 ATP만 챙기는 <b>“이기적인” 조직</b>.',
  f'''<div class="grid2"><div class="card"><h4>📌 고혈당 (인슐린) vs 저혈당 (글루카곤) — 간</h4>{table(['', '고혈당 · 인슐린', '저혈당 · 글루카곤'], [
  ['신호', 'PKB · PP1 ▲, GSK3 ⊗', 'cAMP → PKA'], ['글리코겐', '합성 ↑ · 분해 ↓', '분해 ↑ · 합성 ↓'], ['F2,6BP', '↑ → 해당 ↑', '↓ → 당신생 ↑'], ['간 PK', '활성', '인산화 → OFF'], ['전사', 'HK IV·해당 효소 ↑ (ChREBP)', 'PEPCK·G6Pase ↑ (CREB·FOXO1)'], ['결과', '포도당 흡수·저장', '포도당 생산·방출']], cls='left')}</div>
<div><div class="card"><h4>📌 간 vs 근육 (슬라이드 56)</h4>{table(['', '간', '근육'], [['글루카곤 수용체', '있음', '<b>없음</b>'], ['G6Pase · 당신생 효소', '있음', '<b>없음</b>'], ['글리코겐 용도', '혈당으로 내보냄', '자기 해당 연료'], ['에피네프린 시 해당', '↓', '↑']])}</div>
 {tip('투쟁-도피 반응(슬라이드 57): 에피네프린 → 간은 포도당을 쏟아내고, 근육은 글리코겐을 태워 ATP를 만든다.', '연결')}
 {warn('근육 글리코겐은 혈당 유지에 못 쓴다 — G6Pase가 없어서.', '함정')}</div></div>''',
  ('P2', 'P6', 'P11')))

SUMMARY.append(page('S13', '15.1 대사 조절의 기본 — 동적 정상 상태와 조절 지점', 'Slides 59–65',
  '세포는 평형이 아니라 <b>동적 정상 상태</b>: 물질이 계속 흐르지만 들어오는 속도 = 나가는 속도라 농도는 일정. 조절 지점은 <b>평형에서 먼 반응</b>(Q ≪ K′eq).',
  f'''<div class="grid2"><div><div class="card"><h4>📌 동적 정상 상태 (슬라이드 61)</h4><figure class="fig">{steady_state()}</figure>
 <p>V₁ = V₂이면 [S] 일정. 혈당 5 mM이 대표 예. <b>평형(알짜 흐름 0) ≠ 정상 상태(흐름 있어도 농도 일정)</b>.</p></div>
 <div class="card" style="margin-top:3mm"><h4>📌 평형에서 먼 반응 (슬라이드 62–63, 표 15-3)</h4>{table(['', '정반응 : 역반응', '상태', '조절'], [['①', '10.01 : 0.01', '평형에서 멂', '<b>조절 지점</b>'], ['②③', '200 : 190', '평형 근처', '농도에 따라 저절로']])}
 <p class="small">Q/K′eq가 아주 작은 효소: HK, PFK-1, PK, PC+PEPCK. ΔG′°가 아니라 세포 속 실제 ΔG로 판단 (알돌라아제는 ΔG′° +24지만 세포 속 −6).</p></div></div>
<div class="card"><h4>📌 효소 활성을 바꾸는 10가지 요인 (슬라이드 64–65)</h4>{table(['종류', '방법', '15장의 예'], [
  ['효소 <b>양</b> (느림)', '전사 · mRNA 안정성 · 번역 · 분해 · 격리', 'ChREBP·FOXO1 전사, FOXO1 분해, HK IV 핵 격리'],
  ['효소 <b>활성</b> (빠름)', '기질 농도', '혈당 → HK IV'], ['', '알로스테릭 조절자', 'ATP·AMP·F2,6BP·시트르산'], ['', '공유결합 변형 (인산화)', '인산화효소, GS, PFK-2/FBPase-2'], ['', '조절 단백질 결합', 'HK IV–조절 단백질, PP1–GM']], cls='left')}
 {key('빠른 조절 = 이미 있는 효소의 <b>활성</b> / 느린 조절 = 효소의 <b>양</b>.')}</div></div>''',
  ()))

SUMMARY.append(page('S14', 'ATP · AMP와 AMPK — 세포의 에너지 센서', 'Slides 66–68',
  '<b>[ATP]가 10%만 줄어도 [AMP]는 6배</b>로 뛴다 → AMP가 훨씬 예민한 에너지 경보. 그 경보를 듣고 움직이는 소방관이 <b>AMPK</b>.',
  f'''<div class="grid2"><div><div class="card"><h4>📌 왜 AMP가 크게 변할까? (슬라이드 66)</h4><div class="formula">2ADP ⇌ ATP + AMP<br><small>아데닐산 키나아제 · 거의 평형</small></div>
 <figure class="fig">{amp_bars()}</figure><p>AMP는 원래 아주 적어서(0.1 mM), ATP에서 빠진 0.5 mM이 AMP로 가면 비율로는 몇 배. 큰 저수지(ATP)가 조금 빠져도 옆 작은 컵(AMP)은 크게 출렁인다.</p></div></div>
<div><div class="card"><h4>📌 AMPK가 하는 일 (슬라이드 67–68)</h4>{table(['방향', '경로'], [['<b>켬</b> (ATP 생성)', '포도당 흡수(GLUT4), 해당과정, 지방산 산화, 미토콘드리아 생합성'], ['<b>끔</b> (ATP 소비)', '지방산 합성(ACC 인산화), 콜레스테롤 합성, 단백질 합성, 인슐린 분비']], cls='left')}
 {key('에너지 부족 → <b>만드는 건 켜고, 쓰는 건 꺼라</b>.')}</div>
 {tip('당뇨병 약 <b>메트포르민</b>은 AMPK 쪽을 활성화해 간의 포도당 생성을 줄인다. 운동도 AMPK를 켠다.', '약학')}</div></div>''',
  ()))

SUMMARY.append(page('S15', '15.2 대사 조절의 분석 — C · ε · R', 'Metabolic control analysis · Slides 70–76',
  '모든 효소가 필요하지만 흐름(flux, J)을 “결정”하는 정도는 다르다. 그걸 숫자로 나타낸 것이 <b>플럭스 조절 계수 C</b>. 해당과정 앞부분에서는 PFK-1이 아니라 <b>헥소키나아제가 주인공</b>.',
  f'''<div class="grid2"><div><div class="card"><h4>📌 세 계수</h4>{table(['계수', '뜻', '포인트'], [
  ['<b>C</b> (플럭스 조절 계수)', '효소 양이 변할 때 flux가 변하는 정도', '한 경로의 C 합 = <b>1</b>. 옆길로 빼면 음수 가능'],
  ['<b>ε</b> (탄력성 계수)', '[기질·조절자] 변화에 효소 속도가 반응하는 정도', '[S] ≪ Km → ε ≈ 1, 포화 → ε ≈ 0'],
  ['<b>R</b> (반응 계수)', '외부 신호(인슐린 등)가 flux를 바꾸는 정도', '<b>R = C × ε</b>']], cls='left')}
 <figure class="fig">{mca_bars()}</figure><p class="small">0.79 + 0.21 + 0.0 = 1.0. PFK-1을 5배 늘려도 해당 flux는 10%도 안 늘었다.</p></div></div>
<div><div class="card"><h4>📌 통제(Control) vs 조절(Regulation) (슬라이드 76)</h4>{table(['', 'Control (통제)', 'Regulation (조절)'], [['하는 일', 'flux 양을 결정', '중간체 농도의 요동 방지'], ['대표 효소', '헥소키나아제 (C 0.79)', 'PFK-1 (C 0.21)'], ['비유', '자동차 <b>액셀</b>', '자동차 <b>서스펜션</b>']])}</div>
 {warn('“첫 확정 단계(committed step) = flux 결정 효소”는 <b>아니다</b>. 알로스테릭 조절자가 가장 많은 PFK-1의 C는 작다.', '함정')}
 {tip('R = C·ε → 둘 중 하나라도 작으면 신호 효과가 작다. “신호에 민감하다”와 “flux를 좌우한다”는 다른 문제.', '포인트')}</div></div>''',
  ()))

SUMMARY.append(page('S16', '15장 한 장 요약 + 시험 직전 체크리스트', 'Summaries · Slides 27, 42, 58, 69, 77',
  '다섯 개의 요약 슬라이드를 숫자·효소 이름과 함께 한 장으로. (약어는 바로 뒤 총정리 참고)',
  f'''<div class="grid3">
 <div class="card"><h4>① 해당 ⇄ 당신생 조절</h4><ul style="font-size:.95em"><li>우회 3곳 상반 조절 → 헛된 회로 방지</li><li>HK I·II Km 0.1 (포화) / HK IV Km 10 (혈당 센서, 핵 격리)</li><li>GLUT4만 인슐린 의존</li><li>PFK-1: ATP·시트르산 ⊗, AMP·F2,6BP ▲</li><li>PKA 인산화 → FBPase-2 ON → F2,6BP ↓ → 당신생</li><li>간 PK: PKA로 OFF, F1,6BP 피드포워드 ON</li><li>아세틸-CoA: PC ▲, PDH ⊗</li><li>ChREBP(해당) ↔ FOXO1(당신생)</li></ul></div>
 <div class="card"><h4>② 글리코겐</h4><ul style="font-size:.95em"><li>분해: 인산화효소(PLP) → G1P, 가지제거, 뮤테이스, G6Pase(간만)</li><li>합성: UDP-포도당 → GS (α1→4) → 가지형성 (α1→6), 시작 = 글리코게닌</li><li>인산화효소: 인산화 = ON / GS: 인산화 = OFF</li><li>PKA → 분해 ON / 인슐린 → PKB → GSK3 ⊗ + PP1 ▲ → 합성 ON</li><li>간 인산화효소 = 포도당 센서</li><li>근육: 글루카곤 수용체 ✕, G6Pase ✕</li></ul></div>
 <div class="card"><h4>③ 조절의 원리 · 분석</h4><ul style="font-size:.95em"><li>동적 정상 상태 ≠ 평형</li><li>조절 지점 = 평형에서 먼 반응 (Q ≪ K′eq)</li><li>효소 활성 10요인: 양(느림) / 활성(빠름)</li><li>ATP 10% ↓ → AMP 6배 ↑</li><li>AMPK: 만드는 건 ON, 쓰는 건 OFF (메트포르민)</li><li>C 합 = 1, R = C·ε</li><li>HK = control (C 0.79), PFK-1 = regulation (0.21)</li></ul></div>
</div>
<div class="grid2" style="margin-top:3mm"><div class="card"><h4>🔢 꼭 외울 숫자</h4><div class="tiles" style="grid-template-columns:repeat(3,1fr)">
 <div><b>HK I · II Km</b><span>0.1 mM</span><small>근육, 늘 포화</small></div><div><b>HK IV Km</b><span>~10 mM</span><small>간, 혈당 센서</small></div><div><b>GLUT2 Kt</b><span>~66 mM</span><small>간</small></div>
 <div><b>AMP 증폭</b><span>×6</span><small>ATP 10% ↓일 때</small></div><div><b>C (HK IV)</b><span>0.79</span><small>PFK-1 0.21</small></div><div><b>C 합</b><span>1.0</span><small>한 경로</small></div></div></div>
 <div class="card"><h4>⚠️ 단골 함정</h4><ol style="margin:.2em 0;padding-left:1.3em;font-size:.95em"><li>F1,6BP(중간체) ≠ F2,6BP(조절자)</li><li>PKA 인산화 → PFK-2 OFF·FBPase-2 ON</li><li>인산화효소 인산화 = ON, GS 인산화 = OFF</li><li>에피네프린: 간 해당 ↓, 근육 해당 ↑</li><li>committed step ≠ flux 결정 효소</li><li>정상 상태 ≠ 평형</li></ol></div></div>''',
  ()))

MAPROWS = [['S1–S6 해당·당신생 조절', '문제 6·9·11'], ['S7–S8 글리코겐 대사', '문제 1·2·3'], ['S9–S12 호르몬 조절', '문제 2·4·6·10·11'], ['S13–S15 조절의 원리·분석', '(개념확인 6·7)']]

# ------------------------------------------------------------------ glossary
GLOSS = [
 ('HK (I·II·IV)', 'Hexokinase', '헥소키나아제', '포도당 → G6P. I·II 근육, IV 간'),
 ('GK', 'Glucokinase (= HK IV)', '글루코키나아제', '간의 혈당 센서 (Km 높음)'),
 ('Km · Kt', 'Michaelis constant · transport constant', '미카엘리스 상수 · 수송 상수', '절반 속도일 때 [S]. 작을수록 친화도 ↑'),
 ('Vmax', 'maximum velocity', '최대 속도', '효소가 포화될 때의 속도'),
 ('GLUT1–4', 'Glucose Transporter 1–4', '포도당 수송체', '촉진 확산. GLUT4만 인슐린 의존'),
 ('G1P · G6P', 'Glucose 1- / 6-Phosphate', '포도당 1-·6-인산', '글리코겐 분해 산물 / 갈림길'),
 ('F6P', 'Fructose 6-Phosphate', '과당 6-인산', 'PFK-1 기질, HK IV 조절 단백질에 결합'),
 ('F1,6BP', 'Fructose 1,6-Bisphosphate', '과당 1,6-이인산', '해당 중간체, PK 피드포워드 활성'),
 ('F2,6BP', 'Fructose 2,6-Bisphosphate', '과당 2,6-이인산', '조절 전용 신호: PFK-1 ▲, FBPase-1 ⊗'),
 ('PFK-1', 'Phosphofructokinase-1', '포스포프룩토키나아제-1', '해당 핵심 조절 효소 (F6P → F1,6BP)'),
 ('PFK-2 / FBPase-2', 'Phosphofructokinase-2 / Fructose 2,6-Bisphosphatase', '이중기능 효소', 'F2,6BP를 만들고 없앰'),
 ('FBPase-1', 'Fructose 1,6-Bisphosphatase 1', '과당 1,6-이인산가수분해효소', 'PFK-1의 당신생 짝'),
 ('PK (L · M)', 'Pyruvate Kinase (Liver · Muscle)', '피루브산 키나아제 (간형·근육형)', 'L형만 PKA로 꺼짐'),
 ('PC', 'Pyruvate Carboxylase', '피루브산 카복실화효소', '아세틸-CoA가 활성화'),
 ('PEPCK', 'PEP Carboxykinase', 'PEP 카복시키나아제', '당신생, 전사 조절 대표 유전자'),
 ('PDH', 'Pyruvate Dehydrogenase', '피루브산 탈수소효소', '아세틸-CoA가 억제'),
 ('G6Pase', 'Glucose 6-Phosphatase', '포도당 6-인산가수분해효소', '간·신장만, 근육 ✕'),
 ('OAA', 'Oxaloacetate', '옥살로아세트산', 'PC 산물 → 당신생'),
 ('Acetyl-CoA', 'Acetyl Coenzyme A', '아세틸 조효소 A', '연료 충분 신호'),
 ('Xu5P', 'Xylulose 5-Phosphate', '자일룰로스 5-인산', 'PPP 중간체, 탄수화물 과잉 신호'),
 ('PP2A', 'Protein Phosphatase 2A', '단백질 인산가수분해효소 2A', 'Xu5P가 켬 → PFK-2·ChREBP 탈인산화'),
 ('ChREBP · ChoRE · Mlx', 'Carbohydrate Response Element-Binding Protein', '탄수화물 반응 요소 결합 단백질', '해당·지방 합성 유전자 전사 ON'),
 ('FOXO1', 'Forkhead box O1', '포크헤드 전사인자 O1', '당신생 유전자 전사 ON, 인슐린이 분해'),
 ('CREB', 'cAMP Response Element-Binding protein', 'cAMP 반응 요소 결합 단백질', '글루카곤 → PEPCK 전사'),
 ('PKA', 'Protein Kinase A', '단백질 키나아제 A', 'cAMP가 켬. 글루카곤·에피네프린 실행자'),
 ('PKB (Akt)', 'Protein Kinase B', '단백질 키나아제 B', '인슐린 신호. GSK3 ⊗, FOXO1 분해'),
 ('cAMP', 'cyclic AMP', '고리형 AMP', '2차 전달자'),
 ('AC', 'Adenylyl Cyclase', '아데닐산 고리화효소', 'ATP → cAMP'),
 ('UTP · UDP-포도당', 'Uridine Triphosphate · UDP-glucose', '유리딘 삼인산 · UDP-포도당', '글리코겐 합성용 활성 포도당'),
 ('PPᵢ', 'inorganic Pyrophosphate', '무기 피로인산', '즉시 2Pᵢ로 분해 → 합성 당김'),
 ('PLP', 'Pyridoxal Phosphate', '피리독살 인산', 'B₆, 글리코겐 인산화효소 조효소'),
 ('GS', 'Glycogen Synthase', '글리코겐 합성효소', '인산화 = OFF'),
 ('GSK3', 'Glycogen Synthase Kinase 3', '글리코겐 합성효소 키나아제 3', 'GS를 인산화해 끔. 인슐린이 억제'),
 ('CKII', 'Casein Kinase II', '카제인 키나아제 II', 'GS 프라이밍 인산화'),
 ('PP1', 'Phosphoprotein Phosphatase 1', '인단백질 인산가수분해효소 1', '인산화효소 OFF + GS ON'),
 ('GM', 'Glycogen-targeting subunit (muscle)', '글리코겐 표적 소단위', 'PP1을 글리코겐에 붙잡는 닻'),
 ('a형 · b형', 'phosphorylase / synthase a · b', '활성형 · 덜 활성형', '인산화효소 a = 인산화, GS a = 탈인산'),
 ('Ser-P', 'phosphoserine', '포스포세린', '인산화된 세린 잔기 (예: Ser14)'),
 ('AMP · ADP · ATP', 'Adenosine Mono-/Di-/Triphosphate', '아데노신 일·이·삼인산', 'AMP = 예민한 에너지 경보'),
 ('AMPK', 'AMP-activated Protein Kinase', 'AMP 활성화 단백질 키나아제', '에너지 센서: 생성 ON, 소비 OFF'),
 ('ACC', 'Acetyl-CoA Carboxylase', '아세틸-CoA 카복실화효소', '지방산 합성 첫 효소, AMPK가 끔'),
 ('Q · K′eq', 'mass-action ratio · equilibrium constant', '질량작용비 · 평형상수', 'Q ≪ K′eq = 평형에서 먼 반응'),
 ('J', 'flux', '흐름(플럭스)', '경로를 지나가는 물질의 속도'),
 ('C', 'flux control coefficient', '플럭스 조절 계수', '효소 양 → flux 영향력, 합 = 1'),
 ('ε', 'elasticity coefficient', '탄력성 계수', '[S]·조절자 변화에 대한 민감도'),
 ('R', 'response coefficient', '반응 계수', 'R = C × ε'),
]
ABBR_KEYS = {
 'HK (I·II·IV)': r'\bHK\b|헥소키나아제', 'GK': r'글루코키나아제|\bGK\b', 'Km · Kt': r'\bK[mt]\b', 'Vmax': r'V\s*max', 'GLUT1–4': r'GLUT',
 'G1P · G6P': r'\bG[16]P\b', 'F6P': r'\bF6P\b', 'F1,6BP': r'F1,6BP', 'F2,6BP': r'F2,6BP', 'PFK-1': r'PFK-1', 'PFK-2 / FBPase-2': r'PFK-2|FBPase-2',
 'FBPase-1': r'FBPase-1', 'PK (L · M)': r'\bPK\b|피루브산 키나아제', 'PC': r'\bPC\b', 'PEPCK': r'PEPCK', 'PDH': r'\bPDH\b', 'G6Pase': r'G6Pase', 'OAA': r'\bOAA\b',
 'Acetyl-CoA': r'아세틸-CoA', 'Xu5P': r'Xu5P', 'PP2A': r'PP2A', 'ChREBP · ChoRE · Mlx': r'ChREBP|ChoRE', 'FOXO1': r'FOXO1', 'CREB': r'CREB',
 'PKA': r'\bPKA\b', 'PKB (Akt)': r'\bPKB\b|Akt', 'cAMP': r'cAMP', 'AC': r'아데닐산 고리화효소', 'UTP · UDP-포도당': r'UTP|UDP', 'PPᵢ': r'PP[iᵢ]',
 'PLP': r'\bPLP\b', 'GS': r'\bGS\b|글리코겐 합성효소', 'GSK3': r'GSK', 'CKII': r'CKII', 'PP1': r'\bPP1\b', 'GM': r'\bGM\b', 'a형 · b형': r'[ab]형',
 'Ser-P': r'Ser\d*-P|Ser14', 'AMP · ADP · ATP': r'\b(AMP|ADP|ATP)\b', 'AMPK': r'AMPK', 'ACC': r'\bACC\b', 'Q · K′eq': r'K′\s*eq|\bQ\b',
 'J': r'flux', 'C': r'\bC\s*[=값(]|조절 계수|\bC\s*0\.', 'ε': r'ε', 'R': r'\bR\s*=|반응 계수',
}

# ------------------------------------------------------------------ concept checks
CHECKS = [
 dict(id='C1', num='1', title='헥소키나아제와 GLUT', sec='S1–S3', level=2,
  q='''<p><b>1.</b> (계산, 미카엘리스-멘텐 근사 v/Vmax = [S]/(Km+[S])) 혈당이 5 mM → 10 mM로 오를 때 근육 HK I(Km 0.1 mM)과 간 HK IV(Km 10 mM)의 상대 속도는 각각 어떻게 변하나?</p>
<p><b>2.</b> (O/X) 간의 HK IV는 G6P에 의해 강하게 산물 억제된다.</p>
<p><b>3.</b> (빈칸) 인슐린에 의해 세포막 위치가 조절되는 수송체는 ( &nbsp;&nbsp; )이고, 주로 ( &nbsp; )과 ( &nbsp; ) 조직에 있다.</p>
<p><b>4.</b> (서술) 헛된 회로(futile cycle)란? 왜 막아야 하나?</p>''',
  answer=chips('1. HK I: 0.980 → 0.990 (거의 그대로) / HK IV: 0.33 → 0.50 (<b>1.5배</b>)', '2. <b>X</b> (조절 단백질로 핵 격리)', '3. <b>GLUT4</b> / 근육 · 지방', '4. 반대 경로가 동시에 돌아 <b>ATP만 가수분해</b>되는 회로 → 에너지 낭비'),
  explain=fig(mm_curve(), '') + steps('1. HK I: 5/5.1 = 0.980, 10/10.1 = 0.990 → 혈당에 둔감. HK IV: 5/15 = 0.33, 10/20 = 0.50 → 혈당에 비례 (실제 HK IV는 S자 곡선이지만 결론은 같다).',
   '2. HK IV는 G6P로 억제되지 않는다. 대신 F6P가 붙은 조절 단백질이 HK IV를 핵에 가둔다.',
   '4. 예: PFK-1 + FBPase-1이 동시에 → 알짜 ATP + H₂O → ADP + Pᵢ. 그래서 상반 조절.') +
   tip('Km이 작다 = 조금만 있어도 꽉 찬다 = 농도 변화에 둔감.', '요령')),
 dict(id='C2', num='2', title='PFK-1 · FBPase-1 · F2,6BP', sec='S4', level=2,
  q='''<p><b>1.</b> (분류) 다음이 PFK-1을 켜는지(▲) 끄는지(⊗) 써라: ATP, AMP, 시트르산, F2,6BP</p>
<p><b>2.</b> (빈칸) 글루카곤 → cAMP → ( &nbsp; )가 PFK-2/FBPase-2를 인산화 → ( &nbsp;&nbsp; ) 활성 ON → F2,6BP ( ↑/↓ ) → ( 해당 / 당신생 ) 증가</p>
<p><b>3.</b> (O/X) F1,6BP와 F2,6BP는 모두 해당과정의 중간체이다.</p>
<p><b>4.</b> (서술) 흰쌀밥을 많이 먹으면 Xu5P가 어떻게 지방 합성을 늘리나?</p>''',
  answer=chips('1. ATP <b>⊗</b> · AMP <b>▲</b> · 시트르산 <b>⊗</b> · F2,6BP <b>▲</b>', '2. <b>PKA</b> / <b>FBPase-2</b> / <b>↓</b> / <b>당신생</b>', '3. <b>X</b> (F2,6BP는 조절자)', '4. Xu5P → PP2A → PFK-2 탈인산화(F2,6BP ↑) + ChREBP 핵 이동 → 해당·지방산 합성 ↑'),
  explain=fig(f26bp_switch(), '') + steps('1. 에너지 넉넉(ATP·시트르산) → 해당 브레이크 / 에너지 부족(AMP) 또는 “해당 돌려라” 신호(F2,6BP) → 가속.',
   '2. 인산화되면 키나아제(PFK-2)는 꺼지고 포스파타아제(FBPase-2)가 켜진다 → F2,6BP 분해.',
   '4. 즉각(F2,6BP)과 장기(ChREBP 전사) 두 층으로 남는 포도당을 지방으로 보낸다.') +
   warn('AMP는 PFK-1 ▲ 이면서 FBPase-1 ⊗ → 상반 조절의 대표 예.', '함정')),
 dict(id='C3', num='3', title='Step 10 조절과 전사 조절', sec='S5–S6', level=1,
  q='''<p><b>1.</b> (O/X) 공복 시 간에서는 PKA가 피루브산 키나아제를 인산화해 활성화한다.</p>
<p><b>2.</b> (빈칸) F1,6BP가 피루브산 키나아제를 활성화하는 것을 ( &nbsp;&nbsp;&nbsp; ) 활성화라 한다.</p>
<p><b>3.</b> (짝짓기) 아세틸-CoA가 많을 때: PDH ( ▲/⊗ ), 피루브산 카복실화효소 ( ▲/⊗ )</p>
<p><b>4.</b> (빈칸) 해당 유전자 전사를 켜는 전사인자는 ( &nbsp;&nbsp; ), 당신생 유전자(PEPCK·G6Pase)를 켜는 것은 ( &nbsp;&nbsp; )이며, 인슐린은 ( &nbsp; )를 통해 후자를 인산화·분해시킨다.</p>''',
  answer=chips('1. <b>X</b> (인산화 → <b>비활성</b>)', '2. <b>피드포워드</b>', '3. PDH <b>⊗</b> / PC <b>▲</b>', '4. <b>ChREBP</b> / <b>FOXO1</b> / <b>PKB(Akt)</b>'),
  explain=steps('1. 공복 → 글루카곤 → PKA → 간 PK(L형) 인산화 → OFF → PEP를 당신생으로 보냄. 근육 M형은 인산화 안 됨.',
   '2. 앞 단계 산물이 쌓이면 뒤 단계를 미리 열어 병목을 막는다.',
   '3. 아세틸-CoA 많음 = 지방산 산화 활발 → 피루브산을 태우지 말고(PDH ⊗) 포도당 재료로(PC ▲).',
   '4. 인슐린 → PKB → FOXO1 인산화 → 핵에서 빠져 분해 → 당신생 유전자 전사 ↓.') +
   key('빠른 조절(알로스테릭·인산화) + 느린 조절(전사) 두 층이 함께 작동한다.')),
 dict(id='C4', num='4', title='글리코겐의 분해와 합성', sec='S7–S8', level=1,
  q='''<p><b>1.</b> (빈칸) 글리코겐 인산화효소는 (α1→ &nbsp; ) 결합을 ( &nbsp;&nbsp; )으로 잘라 ( &nbsp;&nbsp; )을 만들며, 조효소는 ( &nbsp; )이다.</p>
<p><b>2.</b> (O/X) 근육 글리코겐은 G6Pase를 통해 혈당 유지에 쓰인다.</p>
<p><b>3.</b> (짝짓기) UDP-포도당 · 글리코게닌 · 가지형성 효소 · 가지제거 효소 — 각각 합성/분해 중 어디에 쓰이고 무슨 일을 하나?</p>
<p><b>4.</b> (서술) 글리코겐이 가지를 많이 치는 이점 2가지는?</p>''',
  answer=chips('1. <b>4</b> / <b>Pᵢ (인산분해)</b> / <b>G1P</b> / <b>PLP (B₆)</b>', '2. <b>X</b> (근육엔 G6Pase 없음)', '3. UDP-포도당·글리코게닌·가지형성 = <b>합성</b> / 가지제거 = <b>분해</b>', '4. ① 물에 잘 녹음 ② 말단이 많아 빠른 분해·합성'),
  explain=fig(glycogen_tree(), '') + steps('3. UDP-포도당 = 활성화된 포도당 공급원 / 글리코게닌 = 첫 사슬 프라이머 / 가지형성 = (α1→6) 가지 생성 / 가지제거 = 가지점 처리(전이 + α1→6 가수분해).',
   '4. 인산화효소·합성효소는 모두 비환원 말단에서만 일하므로, 말단 수 = 동시에 일하는 효소 수.') +
   tip('사냥새는 근육 글리코겐 분해 속도가 매우 빨라 ~11초 만에 바닥 (풀이노트 문제 1).', '연결')),
 dict(id='C5', num='5', title='호르몬과 인산화 스위치', sec='S9–S12', level=2,
  q='''<p><b>1.</b> (표 채우기) 인산화되면 ON/OFF? 글리코겐 인산화효소 ( &nbsp; ), 글리코겐 합성효소 ( &nbsp; ), 간 피루브산 키나아제 ( &nbsp; ), FBPase-2 ( &nbsp; )</p>
<p><b>2.</b> (O/X) 에피네프린은 간과 근육 모두에서 해당과정을 촉진한다.</p>
<p><b>3.</b> (순서) 에피네프린 → ( ) → cAMP → ( ) → 인산화효소 b 키나아제 → 인산화효소 ( b→a ) → G1P</p>
<p><b>4.</b> (서술) 혈당이 올라가면 간의 글리코겐 분해가 왜 멈추는가? (두 가지)</p>''',
  answer=chips('1. 인산화효소 <b>ON</b> · GS <b>OFF</b> · 간 PK <b>OFF</b> · FBPase-2 <b>ON</b>', '2. <b>X</b> (간 ↓, 근육 ↑)', '3. <b>G 단백질·아데닐산 고리화효소</b> → <b>PKA</b>', '4. ① 포도당이 인산화효소 a에 붙어 PP1이 탈인산화 ② 인슐린 → PP1 ↑'),
  explain=fig(cascade(), '') + steps('1. PKA가 인산화하면 → 분해·당신생 쪽 ON, 저장·해당 쪽 OFF. 한 번의 인산화가 대사 전체를 “공복 모드”로 바꾼다.',
   '2. 간은 포도당을 내보내야 해서 해당 ↓, 근육은 자기가 태워야 해서 해당 ↑.',
   '4. 간의 인산화효소 = 혈당 센서. 인슐린은 PKB → GSK3 ⊗, PP1 ▲로 합성도 켠다.') +
   warn('글루카곤은 근육에 영향 없음 (수용체 없음).', '함정')),
 dict(id='C6', num='6', title='정상 상태 · 조절 지점 · AMP', sec='S13–S14', level=1,
  q='''<p><b>1.</b> (O/X) 동적 정상 상태에서는 알짜 흐름이 0이다.</p>
<p><b>2.</b> (판단) 반응 X는 정반응 속도 : 역반응 속도 = 1000 : 1, 반응 Y는 500 : 490이다. 어느 쪽이 조절 지점으로 알맞나? 이유는?</p>
<p><b>3.</b> (계산) [ATP] 5.0 mM, [AMP] 0.1 mM인 세포에서 ATP가 0.5 mM 줄고 그만큼 AMP가 늘면 [AMP]는 몇 배가 되나?</p>
<p><b>4.</b> (빈칸) AMPK는 ATP를 ( 만드는 / 쓰는 ) 경로는 켜고, ( 만드는 / 쓰는 ) 경로는 끈다. AMPK 쪽을 활성화하는 당뇨약은 ( &nbsp;&nbsp;&nbsp; )이다.</p>''',
  answer=chips('1. <b>X</b> (흐름 있음, 농도만 일정)', '2. <b>X</b> — 평형에서 멀어 효소 활성이 곧 flux', '3. 0.1 → 0.6 mM = <b>6배</b>', '4. <b>만드는</b> / <b>쓰는</b> / <b>메트포르민</b>'),
  explain=fig(steady_state(), '') + fig(amp_bars(), '') + steps('2. Y는 평형 근처라 효소를 바꿔도 정·역반응이 함께 변해 흐름이 거의 그대로. X는 거의 일방통행이라 효소 속도 = 흐름.',
   '3. 0.1 + 0.5 = 0.6 mM → 6배 (+500%). ATP는 10%만 줄었는데!') + key('평형 = 알짜 흐름 0, 정상 상태 = V₁ = V₂.')),
 dict(id='C7', num='7', title='대사 조절 분석 (MCA)', sec='S15', level=2,
  q='''<p><b>1.</b> (계산) 어떤 경로의 세 효소 중 둘의 C가 0.55, 0.30이다. 나머지 효소의 C는?</p>
<p><b>2.</b> (판단) [S] = 0.1 Km일 때와 [S] = 10 Km일 때 탄력성 ε는 각각 대략?</p>
<p><b>3.</b> (계산) C = 0.21, ε = 0.5인 효소에 신호가 작용할 때 반응 계수 R은?</p>
<p><b>4.</b> (O/X) PFK-1은 해당과정의 첫 확정 단계이므로 해당 flux를 가장 크게 결정한다.</p>''',
  answer=chips('1. 1 − 0.55 − 0.30 = <b>0.15</b>', '2. 0.1 Km → <b>ε ≈ 1</b> / 10 Km → <b>ε ≈ 0</b>', '3. R = 0.21 × 0.5 = <b>0.105</b>', '4. <b>X</b> (HK IV가 C 0.79로 가장 큼)'),
  explain=fig(mca_bars(), '') + steps('1. 한 경로의 C 합 = 1.', '2. Km보다 훨씬 적으면 속도가 [S]에 비례(직선 구간) → ε ≈ 1. 포화되면 [S]를 바꿔도 속도 그대로 → ε ≈ 0.',
   '4. PFK-1은 flux “결정(control)”보다 중간체 농도 “조절(regulation)” 담당. 액셀은 헥소키나아제, PFK-1은 서스펜션.') +
   tip('R = C × ε: 신호에 아무리 민감해도(ε 큼) C가 작으면 flux는 별로 안 바뀐다.', '포인트')),
]
NO_STRIP = ('S16',)  # 총정리 페이지: 약어는 맨 뒤 총정리로
CHECK_AFTER = {1: 'C1', 3: 'C2', 5: 'C3', 7: 'C4', 11: 'C5', 13: 'C6', 14: 'C7'}

if __name__ == '__main__':
    import exam15 as M
    examlib.render(M)
