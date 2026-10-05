# -*- coding: utf-8 -*-
"""13장 생체에너지론 — 요약 + 문제 통합 에디션 데이터"""
from helpers import *
import content_a, content_b
from content_a import phos_ladder, egg_svg
from content_b import ladder, R, REDOX, e_line, atp_cycle

FOOT = '생화학 13장 · 생체에너지론 — 쉽게 정리 + 문제 완전 해설'
ALL_ITEMS = [i for i in content_a.ITEMS + content_b.ITEMS if i['level'] < 3]

G0 = '<span class="m">ΔG′°</span>'


# ---------------------------------------------------------------- drawings
def hill(ea=True, w=470, h=210, title_l='ATP + H₂O', title_r='ADP + Pᵢ', dg='ΔG′° = −30.5'):
    b = arrowdef('hl1', C['green']) + arrowdef('hl2', C['red'])
    b += f'<line x1="40" y1="20" x2="40" y2="{h-25}" stroke="{C["gray"]}" stroke-width="1.2"/>'
    b += f'<text x="22" y="{h/2}" font-size="10" fill="{C["gray"]}" text-anchor="middle" transform="rotate(-90 22 {h/2})" font-weight="700">자유에너지 G</text>'
    b += f'<line x1="40" y1="{h-25}" x2="{w-10}" y2="{h-25}" stroke="{C["gray"]}" stroke-width="1.2"/>'
    b += T(w / 2, h - 8, '반응 진행 →', 10, C['gray'])
    y1, y2, top = 80, 160, 30
    path = f'M50,{y1} L130,{y1} C190,{y1} 200,{top} 240,{top} C280,{top} 290,{y2} 350,{y2} L{w-20},{y2}' if ea else f'M50,{y1} L130,{y1} C220,{y1} 260,{y2} 350,{y2} L{w-20},{y2}'
    b += f'<path d="{path}" fill="none" stroke="{C["navy"]}" stroke-width="3"/>'
    b += T(90, y1 - 8, title_l, 11, C['navy'], weight=700) + T(w - 70, y2 - 8, title_r, 11, C['navy'], weight=700)
    b += f'<line x1="{w-50}" y1="{y1}" x2="{w-50}" y2="{y2-3}" stroke="{C["green"]}" stroke-width="2" marker-end="url(#hl1)" stroke-dasharray="4 3"/>'
    b += f'<line x1="130" y1="{y1}" x2="{w-50}" y2="{y1}" stroke="{C["gray"]}" stroke-dasharray="3 3"/>'
    b += T(w - 56, (y1 + y2) / 2 + 4, dg, 11, C['green'], 'end', 700)
    if ea:
        b += f'<line x1="240" y1="{y1}" x2="240" y2="{top+3}" stroke="{C["red"]}" stroke-width="2" marker-end="url(#hl2)"/>'
        b += T(246, 62, '활성화 에너지 Eₐ', 10.5, C['red'], 'start', 700) + T(246, 76, '(효소가 낮춰 줌)', 9.5, C['red'], 'start')
    return svg(w, h, b)


def atp_struct():
    W, H = 480, 150
    b = f'<rect x="10" y="50" width="120" height="44" rx="10" fill="#e0e7ff" stroke="#6366f1"/>' + T(70, 70, '아데노신', 12, C['navy'], weight=900) + T(70, 86, '(아데닌 + 리보스)', 9, C['gray'])
    b += f'<line x1="130" y1="72" x2="410" y2="72" stroke="{C["ink"]}" stroke-width="2"/>'
    for i, (x, g) in enumerate([(180, 'α'), (270, 'β'), (360, 'γ')]):
        b += f'<circle cx="{x}" cy="72" r="24" fill="white" stroke="{C["red"] if i == 2 else C["blue"]}" stroke-width="3"/>' + T(x, 78, 'P', 15, C['red'] if i == 2 else C['blue'], weight=900)
        b += T(x - 30, 46, g, 13, C['gray'], weight=900, family='Noto Serif')
        b += T(x + 18, 108, '−', 18, C['red'], weight=900) + T(x - 14, 112, '−', 18, C['red'], weight=900)
    b += T(225, 135, '고에너지 인산무수물 결합 ×2 (β–γ, α–β)', 10.5, C['orange'], weight=700)
    b += T(440, 16, '음전하끼리 밀어냄 = 꽉 찬 스프링', 10.5, C['red'], 'end', 700)
    return svg(W, H, b)


def carbon_ox():
    rows = [('CH₄ 메테인', 8), ('–CH₂– 지방(알케인)', 7), ('–CH₂OH 알코올', 5), ('–CHO 알데하이드', 3), ('–COOH 카복실산', 1), ('CO₂', 0)]
    b = ''
    for i, (n, e) in enumerate(rows):
        y = 6 + i * 26
        col = [C['blue'], C['blue'], '#0891b2', C['amber'], C['orange'], C['red']][i]
        b += T(10, y + 15, n, 11, C['ink'], 'start', 700)
        b += f'<rect x="170" y="{y+2}" width="{e*30+2}" height="18" rx="4" fill="{col}"/>' + T(176 + e * 30, y + 15, f'전자 {e}', 10.5, col, 'start', 700)
    b += T(10, 6 * 26 + 18, '위 = 가장 환원(연료) → 아래 = 가장 산화(다 탄 재)', 10.5, C['gray'], 'start', 700)
    return svg(480, 6 * 26 + 26, b)


def nad_svg():
    W, H = 480, 128
    b = arrowdef('nd', C['orange'])
    b += f'<rect x="10" y="30" width="170" height="56" rx="12" fill="#eff6ff" stroke="{C["blue"]}" stroke-width="2"/>' + T(95, 54, 'NAD⁺ (산화형)', 12, C['blue'], weight=900) + T(95, 72, '니코틴아마이드 고리 +', 10, C['gray'])
    b += f'<rect x="300" y="30" width="170" height="56" rx="12" fill="#fff7ed" stroke="{C["orange"]}" stroke-width="2"/>' + T(385, 54, 'NADH (환원형)', 12, C['orange'], weight=900) + T(385, 72, '전자 2개를 실은 트럭', 10, C['gray'])
    b += f'<line x1="185" y1="50" x2="295" y2="50" stroke="{C["orange"]}" stroke-width="2.4" marker-end="url(#nd)"/>' + T(240, 24, '+ H⁻ (= H⁺ + 2e⁻)', 10, C['orange'], weight=700)
    b += f'<line x1="295" y1="70" x2="185" y2="70" stroke="{C["blue"]}" stroke-width="2.4" marker-end="url(#nd)"/>' + T(240, 100, '전자를 내려놓으면 다시 NAD⁺', 10, C['blue'], weight=700)
    b += T(240, 120, '연료(포도당·지방)의 전자 → NADH → 전자전달계 → O₂', 10.5, C['ink'], weight=700)
    return svg(W, H, b)


# ---------------------------------------------------------------- cover / basics
def cover():
    n = len(ALL_ITEMS)
    return f'''<div class="eyebrow">LEHNINGER BIOCHEMISTRY 8E · CHAPTER 13</div>
<h1>생체에너지론<br>쉽게 정리 + 문제 {n}개 완전 해설</h1>
<div class="sub">생화학을 처음 보는 사람을 위한 버전 — 고등학교 화학만 알면 따라올 수 있어요</div>
<div class="flow">이렇게 보세요 → <span>① 개념 요약</span><span>② 원문 문제</span><span>③ 쉬운 말 번역</span><span>④ 직접 풀기 ✏️</span><span>⑤ 정답·해설</span></div>
<div class="parts" style="grid-template-columns: repeat(5, 1fr)">
 <div><b>0 · 기초 준비</b>에너지 내리막 · 평형 · ln 계산 · 산화환원</div>
 <div><b>PART 1 · 열역학</b>ΔG · ΔG′°와 K′<sub>eq</sub> ★ · 실제 ΔG ★★ · 짝지은 반응<br>→ 문제 01–08</div>
 <div><b>PART 2 · ATP</b>가수분해 에너지 · 세포 속 ΔG<sub>p</sub> ★★ · 고에너지 화합물 · 작용기 전달<br>→ 문제 09–23</div>
 <div><b>PART 3 · 산화-환원</b>탄소의 산화 상태 · 환원 전위 ★★ · ΔG = −nFΔE · NAD·FAD<br>→ 문제 24–31</div>
 <div><b>마지막 · 한 장 정리</b>시험 직전에 보는 공식 &amp; 함정 + 교과서 표</div>
</div>'''


BASICS = [f'''<div class="hd"><span class="pill">시작 전에</span><h1>이것만 알면 13장이 다 풀린다 — 기초 4가지</h1><span class="rt">Basics</span></div>
<div class="body"><div class="cols2"><div class="stack">
 <div class="cc blue"><h4>① 에너지는 “내리막”으로 저절로 흐른다</h4>
  <p>공은 언덕 위(높은 에너지)에서 아래(낮은 에너지)로 저절로 굴러가. 화학 반응도 똑같이 <b>자유에너지 G가 낮아지는 쪽</b>으로 저절로 간다.</p>
  <p>내려간 높이 = <b>ΔG</b>. <span class="mk">ΔG &lt; 0 = 내리막 = 저절로</span>, ΔG &gt; 0 = 오르막 = 에너지를 넣어야 함.</p>
  <figure class="fig">{hill(ea=False, h=170, title_l='반응물', title_r='생성물', dg='ΔG < 0')}</figure></div>
 <div class="cc green"><h4>② 평형과 르샤틀리에 (고등학교 화학 그대로)</h4>
  <p>평형 = 정반응 속도 = 역반응 속도, 겉보기로 멈춘 상태. 평형상수 <b>K = [생성물]/[반응물]</b> (평형일 때).</p>
  <p>생성물을 <b>빼면</b> → 다시 채우려고 <b>정반응</b> → / 생성물을 <b>넣으면</b> → ← 역반응. 세포는 이 원리로 반응 방향을 조절해.</p></div>
</div><div class="stack">
 <div class="cc orange"><h4>③ ln과 e<sup>x</sup> — 계산기 사용법</h4>
  <p>13장 공식은 자연로그 <b>ln</b>을 쓴다. ln x = 2.303 × log x.</p>
  <ul><li>ln 1 = 0 → K = 1이면 ΔG′° = 0</li><li>x = e<sup>y</sup> ⇔ y = ln x (계산기 <b>e<sup>x</sup></b> 버튼, 10<sup>x</sup> 아님!)</li>
  <li>25 °C에서 RT = <b>2.478 kJ/mol</b>, 37 °C에서 <b>2.578 kJ/mol</b></li>
  <li><b>10배 규칙</b>: RT·ln10 = 5.7 → K가 10배 ⇔ ΔG′° 5.7 kJ/mol 차이</li>
  <li>mM → M은 ×10<sup>−3</sup>, J → kJ는 ÷1000</li></ul></div>
 <div class="cc red"><h4>④ 산화 = 전자를 잃음, 환원 = 전자를 얻음</h4>
  <p>“OIL RIG”: Oxidation Is Loss, Reduction Is Gain. 생물에서는 전자가 보통 <b>H 원자(H⁺ + e⁻)와 함께</b> 움직인다 → H를 잃으면 산화(탈수소), 얻으면 환원.</p>
  <p>전자를 주는 쪽 = 환원제(자기는 산화됨), 받는 쪽 = 산화제(자기는 환원됨).</p></div>
 <div class="cc gray fill"><h4>🔢 자주 쓰는 숫자</h4><div class="tiles">
  <div><b>R</b><span>8.315</span><small>J/mol·K</small></div><div><b>F</b><span>96.48</span><small>kJ/V·mol</small></div><div><b>ATP → ADP+Pᵢ</b><span>−30.5</span><small>kJ/mol</small></div></div></div>
</div></div></div>''']


def divider(part):
    toc = ''.join(f'<div><b>{c["id"]}</b>{c["title"]}{" ★" * c.get("star", 0)}</div>' for c in part['concepts'])
    first, last = part['range']
    toc += f'<div><b>문제</b>{first:02d} – {last:02d} ({part["probdesc"]})</div>'
    return f'<div class="big">{part["tag"]}</div><h2>{part["title"]}</h2><div class="q">{part["q"]}</div><div class="toc">{toc}</div>'


# ---------------------------------------------------------------- PART 1
P1 = dict(tag='PART 1', title='생체에너지론과 열역학 (13.1)', q='“반응은 왜, 어느 방향으로 가나?” — ΔG 하나로 모두 판단한다', range=(1, 8), probdesc='예제 1 + 원서 7')
P1['concepts'] = [
 dict(id='1-1', title='생명과 열역학 법칙', en='Bioenergetics & thermodynamics', banner='생물도 물리 법칙을 따른다: 에너지는 없어지지 않고(1법칙), 우주 전체의 무질서는 늘기만 한다(2법칙). 그 둘을 합친 잣대가 <b>ΔG</b>.',
      html=f'''<div class="cols2"><div class="stack">
 <div class="cc blue"><h4>계(system)와 주변(surroundings)</h4><p><b>계</b> = 우리가 관심 있는 것(세포, 달걀, 반응 물질) / <b>주변</b> = 나머지 전부. 계 + 주변 = 우주.</p>
  <p><b>제1법칙</b>: 에너지는 형태만 바뀌고 총량은 일정 (화학 → 열·운동·빛).</p><p><b>제2법칙</b>: 저절로 일어나는 과정은 우주 전체의 <b>엔트로피(무질서, S)</b>를 늘린다.</p></div>
 <div class="cc green"><h4>생명은 2법칙을 어기는 것 같지만…</h4><p>세포는 작은 분자로 단백질·DNA 같은 <b>질서</b>를 만든다(계의 S ↓). 대신 음식을 태워 <b>열과 CO<sub>2</sub>·H<sub>2</sub>O</b>를 주변에 쏟아내 주변의 S를 훨씬 크게 늘린다 → 우주 전체 S ↑ ✔</p>
  <figure class="fig">{egg_svg()}</figure></div>
</div><div class="stack">
 <div class="cc purple"><h4>깁스 자유에너지 G — “일에 쓸 수 있는 에너지”</h4>
  <div class="fbox">ΔG = ΔH − TΔS<small>ΔH: 열(엔탈피) 변화 · ΔS: 무질서 변화 · T: 절대온도</small></div>
  <p>ΔH가 음수(열을 내놓음)이고 ΔS가 양수(무질서 ↑)일수록 ΔG는 더 음수 = 더 잘 일어난다.</p>
  {table(['ΔG', '뜻', '이름'], [['&lt; 0', '저절로 진행 (에너지 방출)', '발에르곤 (exergonic)'], ['= 0', '평형', '—'], ['&gt; 0', '저절로 안 됨 (에너지 필요)', '흡에르곤 (endergonic)']])}</div>
 <div class="hs"><b class="t">고등학교 화학으로 보면</b> : ΔH = 반응열(발열/흡열). 그런데 발열이어도 무질서가 크게 줄면 안 일어날 수 있어 → 그래서 열과 무질서를 함께 보는 ΔG가 필요.</div>
 <div class="trap"><b class="t">헷갈림 주의</b> : ΔG는 “방향”만 알려 주고 “속도”는 모른다. ΔG가 음수여도 활성화 에너지가 크면 느리다 → 그걸 빨리 하게 하는 게 <b>효소</b>.</div>
</div></div>'''),
 dict(id='1-2', star=1, title='표준 자유에너지 ΔG′°와 평형상수 K′eq', en='ΔG′° = −RT ln K′eq', banner='ΔG′°는 “모두 1 M에서 출발했을 때의 기본 성향”이고, 사실상 <b>평형상수 K′<sub>eq</sub>를 에너지로 바꿔 쓴 것</b>일 뿐이다.',
      html=f'''<div class="cols2"><div class="stack">
 <div class="cc blue"><h4>“표준 상태”의 약속 (′ 표시의 의미)</h4>
  <p>화학의 ΔG°: 25 °C, 1 atm, 모든 물질 1 M (H⁺도 1 M → pH 0)</p>
  <p>생화학의 <b>ΔG′°</b>: 위와 같되 <b>pH 7</b>, [H<sub>2</sub>O] = 55.5 M(식에서 생략), [Mg<sup>2+</sup>] = 1 mM. 세포에 맞춘 표준.</p>
  <p class="small">′(프라임) = “생화학 표준”. K′<sub>eq</sub>, E′°도 같은 뜻.</p></div>
 <div class="cc purple"><h4>핵심 공식</h4>
  <div class="fbox">ΔG′° = −RT ln K′<sub>eq</sub><small>거꾸로: K′<sub>eq</sub> = e<sup>−ΔG′°/RT</sup></small></div>
  <p>평형에서 ΔG = 0이 된다는 사실에서 나온 식(다음 페이지 1-3). 그래서 ΔG′°는 반응마다 정해진 <b>상수</b>.</p>
  {table(['K′<sub>eq</sub>', 'ΔG′°', '1 M에서 출발하면'], [['&gt; 1', '음수', '정반응 (생성물 쪽)'], ['= 1', '0', '이미 평형'], ['&lt; 1', '양수', '역반응 (반응물 쪽)']])}</div>
</div><div class="stack">
 <div class="cc green"><h4>시소로 이해하기</h4><p>평형 = 시소가 멈춘 위치. 생성물 쪽으로 19배 기울어 멈췄다면(K = 19), 생성물 쪽이 더 “편한”(G가 낮은) 자리라는 뜻 → ΔG′° &lt; 0.</p>
  <figure class="fig">{logaxis([(0.0475, 'K=0.05 → +7.6', C['blue']), (19, 'K=19 → −7.3', C['green']), (254, 'K=254 → −13.7', C['orange'])], -2, 3, center=1, center_lab='K = 1 ⇔ ΔG′° = 0', height=125)}<figcaption>K가 오른쪽(&gt;1)일수록 ΔG′°는 더 음수</figcaption></figure></div>
 <div class="hs"><b class="t">10배 규칙 (25 °C)</b> : K가 10배 커질 때마다 ΔG′°는 <b>−5.7 kJ/mol</b>씩. ATP 가수분해(−30.5)는 K ≈ 10<sup>5.3</sup> ≈ 2×10<sup>5</sup> → 평형에서 ATP가 거의 남지 않는다.</div>
 <div class="trap"><b class="t">헷갈림 주의</b> : R은 J 단위(8.315 J/mol·K) → 답이 J로 나오면 ÷1000. 물·H⁺(pH 7)는 K 식에 넣지 않는다.</div>
</div></div>'''),
 dict(id='1-3', star=2, title='실제 ΔG — 지금 농도가 방향을 정한다', en='ΔG = ΔG′° + RT ln Q', banner='ΔG′°는 “기후”(평균 성향), ΔG는 “오늘 날씨”(지금 농도에서의 실제 성향). 반응이 실제로 갈지 말지는 <b>ΔG</b>가 결정한다.',
      html=f'''<div class="cols2"><div class="stack">
 <div class="cc purple"><h4>실제 자유에너지 공식</h4>
  <div class="fbox">ΔG = ΔG′° + RT ln Q<small>Q = 질량작용비 = 지금의 [생성물]/[반응물] (M 단위, 물 제외)</small></div>
  <p>평형에서는 Q = K′<sub>eq</sub>이고 ΔG = 0 → 0 = ΔG′° + RT ln K′<sub>eq</sub> → 1-2의 식이 나온다.</p></div>
 <div class="cc blue"><h4>Q와 K를 비교하면 방향이 보인다</h4>
  {table(['비교', 'ΔG', '반응'], [['Q &lt; K', '음수', '정반응 → (생성물이 덜 쌓임)'], ['Q = K', '0', '평형'], ['Q &gt; K', '양수', '← 역반응']])}
  <figure class="fig">{logaxis([(0.333, '지금 Q = 0.33', C['orange']), (1.97, '평형 K = 1.97', C['navy'])], -1, 1, height=105, label='Q가 K를 향해 → 정반응')}</figure></div>
</div><div class="stack">
 <div class="cc green"><h4>세포는 생성물을 치워서 반응을 민다</h4><p>ΔG′°가 +(오르막)인 반응도, 다음 효소가 생성물을 계속 가져가 Q를 아주 작게 만들면 RT ln Q가 크게 음수 → <b>ΔG &lt; 0</b>으로 진행.</p>
  <p>예: 알돌라아제 ΔG′° = +23.8인데 간세포 속 ΔG ≈ −8.6 kJ/mol (14장).</p></div>
 <div class="cc orange"><h4>평형에서 먼 반응 = 조절 지점</h4><p>Q ≈ K인 반응은 양방향으로 왔다 갔다 → 조절 효과가 작다. Q ≪ K(ΔG가 크게 음수)인 반응은 <b>일방통행</b> → 효소 속도가 곧 흐름 → 세포가 여기를 조절한다.</p>
  <p class="small">살아 있는 세포는 평형이 아니라 <b>동적 정상 상태</b>. 평형(ΔG = 0)에 도달 = 일을 할 수 없음 = 죽음.</p></div>
 <div class="trap"><b class="t">헷갈림 주의</b> : 생성물·반응물 개수가 같으면 단위(mM)가 상쇄되어 그대로 써도 되지만, 개수가 다르면 꼭 <b>M로</b> 바꿔서 Q를 계산!</div>
</div></div>'''),
 dict(id='1-4', star=1, title='짝지은(공역) 반응 — ΔG′°는 더하고, K는 곱한다', en='Coupled reactions', banner='오르막 반응은 혼자 못 간다. 더 큰 내리막 반응(주로 ATP)과 <b>공통 중간체</b>로 묶으면, 전체가 내리막이 되어 진행한다.',
      html=f'''<div class="cols2"><div class="stack">
 <div class="cc purple"><h4>가산성 (additivity)</h4>
  <div class="fbox">반응 (1) + (2) = (3) &nbsp;→&nbsp; ΔG′°<sub>3</sub> = ΔG′°<sub>1</sub> + ΔG′°<sub>2</sub><small>K′<sub>3</sub> = K′<sub>1</sub> × K′<sub>2</sub> (ln의 성질)</small></div>
  <ul><li>반응을 <b>뒤집으면</b> ΔG′° 부호가 반대, K는 역수.</li><li>양쪽에 똑같이 나오는 물질(공통 중간체)은 지워진다.</li></ul></div>
 <div class="cc blue"><h4>대표 예: 포도당의 인산화</h4>
  {align([('(1)', '포도당 + P<sub>i</sub> → G6P + H<sub>2</sub>O', '+13.8'), ('(2)', 'ATP + H<sub>2</sub>O → ADP + P<sub>i</sub>', '−30.5'), ('합', '포도당 + ATP → G6P + ADP', '<span class="hl">−16.7</span>')], cls='sum')}
  <p>오르막 +13.8을 −30.5짜리 내리막이 끌어내려 전체 −16.7. K로 보면 10<sup>−2.4</sup> × 10<sup>5.3</sup> ≈ 10<sup>2.9</sup>배.</p></div>
</div><div class="stack">
 <div class="cc green"><h4>그림으로 보기</h4><figure class="fig">{energy_steps([('포도당 + Pᵢ', 0, C['navy']), ('G6P (혼자)', 13.8, C['red']), ('ATP와 짝지으면', -16.7, C['green'])], height=200)}</figure></div>
 <div class="hs"><b class="t">비유</b> : 무거운 짐(+13.8)을 혼자 못 들 때 도르래 반대편에 더 무거운 추(ATP, −30.5)를 단다. 단, 짐과 추가 <b>같은 줄(효소 위의 공통 중간체)</b>에 묶여 있어야 한다.</div>
 <div class="trap"><b class="t">헷갈림 주의</b> : 표에 적힌 방향과 문제의 방향이 반대면 부호부터 뒤집고 더하기! (문제 08)</div>
</div></div'''+'>'),
]
P1['problems'] = [('WE1', '1-2'), ('P1', '1-1'), ('P2', '1-2'), ('P3', '1-2'), ('P4', '1-2'), ('P6', '1-3'), ('P5', '1-4'), ('P9', '1-4')]

# ---------------------------------------------------------------- PART 2
P2 = dict(tag='PART 2', title='인산기 전달과 ATP (13.3)', q='“ATP는 왜 에너지가 많고, 그 에너지를 어떻게 건네줄까?”', range=(9, 23), probdesc='예제 1 + 원서 14')
P2['concepts'] = [
 dict(id='2-1', star=1, title='ATP 가수분해는 왜 에너지가 클까?', en='Why ATP hydrolysis is so exergonic', banner='ATP는 음전하 인산 3개가 꽉 붙은 “눌린 스프링”. 끝 인산 하나가 떨어지면 스프링이 풀리고 생성물이 훨씬 안정해져서 <b>−30.5 kJ/mol</b>이 나온다.',
      html=f'''<div class="cols2"><div class="stack">
 <div class="cc blue"><h4>ATP의 생김새</h4><figure class="fig">{atp_struct()}</figure>
  <div class="fbox">ATP<sup>4−</sup> + H<sub>2</sub>O → ADP<sup>3−</sup> + HPO<sub>4</sub><sup>2−</sup> + H<sup>+</sup><small>ΔG′° = −30.5 kJ/mol</small></div></div>
 <div class="cc green"><h4>네 가지 이유 (그림 13-11)</h4><ol style="margin:.2em 0;padding-left:1.3em">
  <li><b>전하 반발 해소</b> — 음전하끼리 밀어내던 긴장이 풀림 (만원 지하철에서 한 명 내림)</li>
  <li><b>P<sub>i</sub>의 공명 안정화</b> — 떨어진 인산의 전자가 O 4개에 고르게 퍼짐</li>
  <li><b>이온화</b> — ADP가 H⁺를 내놓아 더 안정 (pH 7에서)</li>
  <li><b>수화</b> — 생성물이 물에 더 잘 둘러싸임</li></ol></div>
</div><div class="stack">
 <div class="cc purple"><h4>그런데 ATP는 물속에서 왜 저절로 안 깨질까?</h4><figure class="fig">{hill(h=190)}</figure>
  <p><b>열역학적으로는 불안정</b>(내리막)하지만 <b>속도론적으로는 안정</b>(활성화 에너지 200–400 kJ/mol가 큼). → 효소가 있을 때만 깨진다 = 세포가 어디서 쓸지 고를 수 있다.</p></div>
 <div class="hs"><b class="t">Mg<sup>2+</sup></b> : 세포 속 ATP는 대부분 Mg<sup>2+</sup>와 붙은 MgATP<sup>2−</sup>. 음전하를 일부 가려 주고 효소가 알아보는 모양을 만든다.</div>
 <div class="trap"><b class="t">헷갈림 주의</b> : “고에너지 결합에 에너지가 들어 있다”는 말은 틀린 표현. 결합을 끊는 데는 에너지가 든다. 에너지 차이는 <b>반응물과 생성물의 안정성 차이</b>에서 온다.</div>
</div></div>'''),
 dict(id='2-2', star=2, title='세포 속 실제 ΔG<sub>p</sub> — 표준값보다 훨씬 크다', en='Phosphorylation potential', banner='세포는 ATP를 많이, ADP·P<sub>i</sub>를 적게 유지한다. 그래서 세포 속 ATP 가수분해는 −30.5가 아니라 약 <b>−50 ~ −60 kJ/mol</b>.',
      html=f'''<div class="cols2"><div class="stack">
 <div class="cc purple"><h4>인산화 전위 ΔG<sub>p</sub></h4>
  <div class="fbox">ΔG<sub>p</sub> = ΔG′° + RT ln {F('[ADP][P<sub>i</sub>]', '[ATP]')}</div>
  <p>사람 적혈구: ATP 2.25, ADP 0.25, P<sub>i</sub> 1.65 mM → Q = 1.8×10<sup>−4</sup> → RT ln Q ≈ −22 → <b>ΔG<sub>p</sub> ≈ −52 kJ/mol</b> (예제 13-2)</p>
  <figure class="fig">{bars([('표준 (모두 1 M)', 30.5, '#93c5fd', '−30.5'), ('적혈구 속', 52, C['orange'], '−52 kJ/mol')], height=85)}</figure></div>
 <div class="cc blue"><h4>표 13-5 · 세포 속 농도 (mM)</h4>{table(['세포', 'ATP', 'ADP', 'P<sub>i</sub>', 'PCr'], [['쥐 간', '3.38', '1.32', '4.8', '0'], ['쥐 근육', '8.05', '0.93', '8.05', '28'], ['쥐 뉴런', '2.59', '0.73', '2.72', '4.7'], ['사람 적혈구', '2.25', '0.25', '1.65', '0']])}</div>
</div><div class="stack">
 <div class="cc green"><h4>[ATP]/[ADP]가 높을수록 ATP 한 개가 세다</h4><p>Q가 작을수록(ATP 많고 ADP 적을수록) ΔG가 더 음수 → 오르막 반응을 더 세게 밀 수 있다. 그래서 세포는 ATP를 쓰는 즉시 다시 채운다.</p>
  <p class="small">배터리 비유: [ATP]/[ADP] = 충전량. 완충일수록 한 번 쓸 때 전압(에너지)이 크다.</p></div>
 <div class="cc orange"><h4>거꾸로: ATP를 만드는 데 드는 에너지</h4><p>합성 = 가수분해의 반대 → 세포에서 ATP 1개 만들려면 <b>+46 ~ +52 kJ/mol</b> 필요 (간세포 약 47, 적혈구 약 52).</p>
  <p>ATP는 저장 창고가 아니라 <b>빠르게 도는 현금</b>: 사람은 하루에 몸무게의 절반 이상(수십 kg)의 ATP를 만들고 쓴다.</p></div>
 <div class="trap"><b class="t">헷갈림 주의</b> : “생리적·체온”이라는 말이 나오면 37 °C → RT = <b>2.578</b> kJ/mol.</div>
</div></div>'''),
 dict(id='2-3', star=1, title='고에너지 인산 화합물 — ATP는 “중간”이다', en='Phosphoryl group transfer potential', banner='인산기는 물처럼 <b>높은 곳 → 낮은 곳</b>으로만 저절로 흐른다. ATP는 사다리의 딱 중간이라, 위에서 받아 아래로 건네주는 “중계자”.',
      html=f'''<div class="cols2"><div class="stack">
 <div class="cc blue"><h4>인산 화합물 사다리 (표 13-6, 그림 13-19)</h4><figure class="fig">{phos_ladder(hl=('PEP', 'PCr', 'ATP', 'G6P'), height=270)}</figure></div>
</div><div class="stack">
 <div class="cc green"><h4>왜 ATP보다 위에 있을까?</h4><ul>
  <li><b>PEP (−61.9)</b>: 인산이 떨어지면 엔올 → 케토 피루브산으로 변신(호변이성화) → 생성물이 훨씬 안정</li>
  <li><b>1,3-BPG (−49.3)</b>: 아실인산(산무수물) → 생성물 3-포스포글리세르산의 이온화·공명</li>
  <li><b>포스포크레아틴 (−43.0)</b>: 크레아틴의 구아니디노기 공명 → 근육의 “비상 배터리”</li>
  <li><b>아세틸-CoA (−31.4)</b>: 싸이오에스터 — S는 O보다 공명 안정화가 약해 반응물이 불안정</li></ul></div>
 <div class="cc purple"><h4>인산기 전달 계산 = 떼기 + 붙이기</h4>
  {align([('', 'PCr + H<sub>2</sub>O → Cr + P<sub>i</sub>', '−43.0'), ('', 'ADP + P<sub>i</sub> → ATP + H<sub>2</sub>O', '+30.5'), ('합', 'PCr + ADP → Cr + ATP', '<span class="hl">−12.5</span>')], cls='sum')}</div>
 <div class="hs"><b class="t">한 줄 요약</b> : 위(PEP·1,3-BPG·PCr) → ADP에 인산을 줘서 ATP 생성 / ATP → 아래(포도당·글리세롤)에 인산을 줘서 활성화.</div>
</div></div>'''),
 dict(id='2-4', star=1, title='ATP는 “작용기 전달”로 일을 시킨다', en='ATP provides energy by group transfers', banner='ATP는 대부분 그냥 물에 깨지지 않는다. 기질에 <b>인산(또는 AMP)을 먼저 붙여 활성화</b>하고, 그다음 단계에서 그 꼬리표가 떨어지며 일이 된다.',
      html=f'''<div class="cols2"><div class="stack">
 <div class="cc blue"><h4>2단계 작전 — 글루타민 합성효소</h4>
  <div class="twostep"><div><span>1단계</span>글루탐산 + ATP → 글루타밀-인산 + ADP<small>인산 꼬리표 붙이기 (활성화)</small></div><div><span>2단계</span>글루타밀-인산 + NH<sub>3</sub> → 글루타민 + P<sub>i</sub><small>좋은 이탈기 P<sub>i</sub>가 떨어짐</small></div></div>
  <p>합치면 “글루탐산 + NH<sub>3</sub> + ATP → 글루타민 + ADP + P<sub>i</sub>”. 겉보기엔 ATP 가수분해와 짝지은 것 같지만 실제로는 <b>공통 중간체(글루타밀-인산)</b>를 통한 전달.</p></div>
 <div class="cc orange"><h4>ATP → AMP + PP<sub>i</sub> (α 위치 공격)</h4><p>지방산 활성화, 아세틸-CoA 합성, DNA·RNA 합성: ATP의 <b>AMP 부분</b>을 통째로 붙이고 PP<sub>i</sub>를 내보냄.</p>
  <p>PP<sub>i</sub>는 피로인산가수분해효소가 즉시 분해(−19.2) → 반응이 한 방향으로 <b>강하게 당겨짐</b>. 인산무수물 결합 2개를 쓰는 셈.</p></div>
</div><div class="stack">
 <div class="cc green"><h4>공격 위치에 따라 산물이 다르다 (그림 13-20)</h4>
  {table(['공격 위치', '산물', '예'], [['γ (끝)', 'ADP + 기질–P', '헥소키나아제, 대부분의 키나아제'], ['β', 'AMP + 기질–PP', '드묾'], ['α', 'PP<sub>i</sub> + 기질–AMP (아데닐화)', '지방산 활성화, DNA 합성']], cls='left')}</div>
 <div class="cc purple"><h4>ATP가 하는 일 모음</h4><ul>
  <li><b>능동수송</b>: Na⁺/K⁺ ATPase — 인산화 → 모양 변화 → 3Na⁺ 밖, 2K⁺ 안</li>
  <li><b>근육 수축</b>: 마이오신이 ATP 가수분해로 모양을 바꿔 액틴을 당김</li>
  <li><b>빛</b>: 반딧불이 루시페레이스 (ATP → AMP + PP<sub>i</sub>)</li>
  <li><b>거대분자 합성</b>: 단백질·핵산·다당류 조립</li></ul></div>
 <div class="hs"><b class="t">세포 속 ATP 교체</b> : 끝(γ) 인산은 몇 초~분 단위로 계속 떨어졌다 붙는다 → ATP 농도는 일정해도 γ-인산은 계속 “새 것”.</div>
</div></div>'''),
]
P2['problems'] = [('WE2', '2-2'), ('P7', '2-1'), ('P8', '2-1'), ('P10', '2-2'), ('P15', '2-2'), ('P22', '2-2'), ('P12', '2-3'), ('P14', '2-3'), ('P20', '2-3'), ('P21', '2-3'),
                  ('P13', '2-4'), ('P23', '2-4'), ('P24', '2-4'), ('P25', '2-4'), ('P26', '2-4')]

# ---------------------------------------------------------------- PART 3
P3 = dict(tag='PART 3', title='생물학적 산화-환원 (13.4)', q='“전자가 흐르면 왜 에너지가 나올까?” — 전자의 폭포', range=(24, 31), probdesc='예제 1 + 원서 7')
P3['concepts'] = [
 dict(id='3-1', title='산화·환원과 탄소의 산화 상태', en='Oxidation states of carbon', banner='생물의 산화 = 대부분 <b>탈수소(H를 떼기)</b>. 탄소에 H가 많을수록 환원된(덜 탄) 연료이고, 산화되며 전자를 내놓을수록 에너지가 나온다.',
      html=f'''<div class="cols2"><div class="stack">
 <div class="cc blue"><h4>전자가 옮겨 가는 4가지 방식</h4><ol style="margin:.2em 0;padding-left:1.3em">
  <li><b>전자 직접</b>: Fe<sup>2+</sup> + Cu<sup>2+</sup> → Fe<sup>3+</sup> + Cu<sup>+</sup></li>
  <li><b>수소 원자</b>(H⁺ + e⁻)로: AH<sub>2</sub> + B → A + BH<sub>2</sub></li>
  <li><b>하이드라이드 이온</b>(H⁻ = H⁺ + 2e⁻)으로: NAD 탈수소효소</li>
  <li><b>산소와 직접 결합</b>: R–CH<sub>3</sub> + ½O<sub>2</sub> → R–CH<sub>2</sub>OH</li></ol>
  <p class="small">어떤 방식이든 “전자를 잃으면 산화, 얻으면 환원”. 산화와 환원은 항상 짝으로 일어난다.</p></div>
 <div class="cc green"><h4>포도당의 산화 = 전자 24개를 내놓기</h4><div class="fbox">C<sub>6</sub>H<sub>12</sub>O<sub>6</sub> + 6O<sub>2</sub> → 6CO<sub>2</sub> + 6H<sub>2</sub>O<small>ΔG′° = −2,840 kJ/mol · 전자는 NAD⁺·FAD를 거쳐 O<sub>2</sub>로</small></div></div>
</div><div class="stack">
 <div class="cc purple"><h4>탄소의 산화 상태 (그림 13-22)</h4><figure class="fig">{carbon_ox()}</figure>
  <p class="small">세는 법: 전기음성도 H &lt; C &lt; O. C–H 결합 전자는 C 것(2개), C–C는 반반(1개), C–O는 O 것(0개).</p></div>
 <div class="hs"><b class="t">그래서</b> : –CH<sub>2</sub>–가 가득한 지방은 g당 9 kcal, 이미 –CHOH–인 탄수화물은 g당 4 kcal. 더 환원된 연료일수록 태울 거리가 많다.</div>
</div></div>'''),
 dict(id='3-2', star=2, title='환원 전위 E′° — 전자를 끌어당기는 힘', en='Standard reduction potential', banner='E′°는 “전자 욕심”. <b>전자는 E′°가 낮은(더 −) 쪽에서 높은(더 +) 쪽으로 흐른다</b>. 받는 쪽 − 주는 쪽 = ΔE′° 가 양수면 저절로 간다.',
      html=f'''<div class="cols2"><div class="stack">
 <div class="cc blue"><h4>어떻게 재나? (그림 13-23)</h4><figure class="fig" style="width:58%">{img('fig13_23.png', '100%')}</figure>
  <p>기준 = 수소 전극(0.00 V). 시험할 짝을 1 M씩 넣고 전압을 잰다. 생화학 표준은 <b>pH 7</b>이라 E′° (2H⁺/H<sub>2</sub>는 pH 7에서 −0.414 V).</p></div>
 <div class="cc orange"><h4>용어 정리</h4><ul>
  <li>표의 반쪽 반응은 모두 “산화형 + e⁻ → 환원형”(환원 방향)으로 적는다.</li>
  <li>E′°가 <b>높다(+)</b> = 전자를 잘 받는다 = 산화형이 <b>강한 산화제</b> (예: O<sub>2</sub>)</li>
  <li>E′°가 <b>낮다(−)</b> = 전자를 잘 준다 = 환원형이 <b>강한 환원제</b> (예: NADH)</li></ul></div>
</div><div class="stack">
 <div class="cc purple"><h4>전자 사다리 (표 13-7 주요 값)</h4><figure class="fig">{ladder(R('½O₂/H₂O', '시토크롬 c', '푸마르산/숙신산', '피루브산/젖산', '아세트알데하이드/에탄올', 'NAD⁺/NADH', 'α-케토글루타르산+CO₂/아이소시트르산'), -0.42, 0.86, hl=('NAD⁺/NADH', '½O₂/H₂O'), flows=[('NAD⁺/NADH', '½O₂/H₂O', 'e⁻')], height=255)}</figure></div>
 <div class="trap"><b class="t">헷갈림 주의</b> : 한쪽 반쪽 반응이 실제로는 거꾸로(산화) 가도 E′°의 부호를 바꾸지 않는다. 그냥 <b>받는 쪽 − 주는 쪽</b>.</div>
</div></div>'''),
 dict(id='3-3', star=1, title='전위차 → 자유에너지, 그리고 농도 보정', en='ΔG′° = −nFΔE′°', banner='전자가 떨어지는 “높이”(ΔE)가 클수록 나오는 에너지가 크다: <b>ΔG′° = −nFΔE′°</b>. 농도가 표준과 다르면 E도 ΔG처럼 보정한다.',
      html=f'''<div class="cols2"><div class="stack">
 <div class="cc purple"><h4>공식 두 개</h4>
  <div class="fbox">ΔE′° = E′°<sub>받는 쪽</sub> − E′°<sub>주는 쪽</sub></div>
  <div class="fbox">ΔG′° = −nF ΔE′°<small>n = 옮겨 간 전자 수 (NADH·FAD는 2) · F = 96.48 kJ/V·mol</small></div>
  <p>ΔE′° &gt; 0 → ΔG′° &lt; 0 → 저절로 진행.</p></div>
 <div class="cc blue"><h4>예: NADH → O<sub>2</sub> (호흡 사슬 전체)</h4>
  <p>ΔE′° = 0.816 − (−0.320) = 1.136 V → ΔG′° = −2 × 96.48 × 1.136 ≈ <b>−219 kJ/mol</b></p>
  <p>ATP 1개 ≈ 50 kJ → 이론상 4개 이상. 실제로는 NADH 1개당 약 <b>2.5 ATP</b> (나머지는 열 → 체온).</p></div>
</div><div class="stack">
 <div class="cc green"><h4>농도 보정 — 네른스트 식</h4>
  <div class="fbox">E = E′° + {F('RT', 'nF')} ln {F('[산화형]', '[환원형]')}<small>25 °C, n = 2이면 RT/nF = 0.0128 V → 10배마다 약 30 mV</small></div>
  <figure class="fig">{e_line()}</figure>
  <p>산화형(전자 받을 놈)이 많을수록 E가 올라간다(+). ΔG = ΔG′° + RT ln Q와 같은 구조!</p></div>
 <div class="hs"><b class="t">두 식은 쌍둥이</b> : ΔG′° = −RT ln K′<sub>eq</sub> ↔ ΔG′° = −nFΔE′° / ΔG = ΔG′° + RT ln Q ↔ E = E′° + (RT/nF) ln(산화형/환원형)</div>
</div></div>'''),
 dict(id='3-4', title='전자 운반체 NAD·FAD', en='Universal electron carriers', banner='포도당·지방에서 뺀 전자는 바로 O<sub>2</sub>로 가지 않고, <b>NAD⁺·FAD라는 “전자 트럭”</b>에 실려 미토콘드리아로 간다.',
      html=f'''<div class="cols2"><div class="stack">
 <div class="cc blue"><h4>NAD⁺ / NADH (니코틴아마이드)</h4><figure class="fig">{nad_svg()}</figure>
  <div class="fbox">NAD<sup>+</sup> + 2e⁻ + 2H<sup>+</sup> → NADH + H<sup>+</sup> &nbsp; (E′° = −0.320 V)</div>
  <p>탈수소효소가 기질의 H⁻(하이드라이드)를 NAD⁺의 고리에 옮긴다. 세포 속에서 NAD⁺/NADH 비는 높게(산화형 많이) 유지 → 산화 반응에 유리.</p></div>
</div><div class="stack">
 <div class="cc orange"><h4>NAD vs NADP — 쓰임새가 다르다</h4>{table(['', 'NAD⁺/NADH', 'NADP⁺/NADPH'], [['주 용도', '<b>이화</b>(분해) → ATP 생산', '<b>동화</b>(합성)·항산화'], ['세포 속 비율', '[NAD⁺] ≫ [NADH]', '[NADPH] ≫ [NADP⁺]'], ['대표 경로', '해당·TCA·β-산화', '지방산·콜레스테롤 합성, 오탄당 인산 경로']])}</div>
 <div class="cc green"><h4>FAD · FMN (플래빈, 리보플래빈 B<sub>2</sub>)</h4><p>효소에 단단히 붙은 <b>보결분자단</b>. 전자 1개 또는 2개를 받을 수 있다(세미퀴논 중간체). FADH<sub>2</sub>는 NADH보다 ATP를 조금 덜(약 1.5) 만든다.</p></div>
 <div class="hs"><b class="t">비타민과 연결</b> : 나이아신(B<sub>3</sub>) → NAD, 리보플래빈(B<sub>2</sub>) → FAD. 나이아신 결핍 = <b>펠라그라</b>(피부염·설사·치매). 트립토판으로도 일부 만든다.</div>
</div></div>'''),
]
P3['problems'] = [('WE3', '3-3'), ('P27', '3-1'), ('P28', '3-2'), ('P29', '3-2'), ('P32', '3-2'), ('P33', '3-2'), ('P30', '3-3'), ('P31', '3-3')]

PARTS = [P1, P2, P3]

# ---------------------------------------------------------------- ending
ENDING = [f'''<div class="hd"><span class="pill">한 장 정리</span><h1>시험 직전에 보는 13장 공식 &amp; 함정</h1><span class="rt">Cheat sheet</span></div>
<div class="body"><div class="cols3">
 <div class="stack">
  <div class="cc purple"><h4>열역학 공식</h4><div class="fbox">ΔG = ΔH − TΔS</div><div class="fbox">ΔG′° = −RT ln K′<sub>eq</sub></div><div class="fbox">ΔG = ΔG′° + RT ln Q</div>
   <p>RT = 2.478 (25 °C) / 2.578 (37 °C) kJ/mol · 10배 = 5.7 kJ/mol</p></div>
  <div class="cc blue"><h4>짝지은 반응</h4><p>ΔG′°는 더하고 K는 곱한다. 뒤집으면 부호 반대.</p></div>
 </div>
 <div class="stack">
  <div class="cc orange"><h4>ATP 숫자</h4><ul><li>ATP → ADP + P<sub>i</sub>: <b>−30.5</b></li><li>ATP → AMP + PP<sub>i</sub>: −45.6 · PP<sub>i</sub> → 2P<sub>i</sub>: −19.2</li>
   <li>세포 속 ΔG<sub>p</sub>: <b>−50 ~ −60</b> (적혈구 −52)</li><li>순위: PEP −61.9 &gt; 1,3-BPG −49.3 &gt; PCr −43.0 &gt; <b>ATP −30.5</b> &gt; G6P −13.8</li></ul></div>
  <div class="cc green"><h4>산화-환원</h4><div class="fbox">ΔE′° = E′°<sub>받는</sub> − E′°<sub>주는</sub></div><div class="fbox">ΔG′° = −nFΔE′°</div>
   <p>NADH −0.320 → O<sub>2</sub> +0.816 : ΔE′° 1.136 V, ΔG′° −219</p></div>
 </div>
 <div class="stack">
  <div class="trap"><b class="t">함정 1</b> : ln ≠ log, e<sup>x</sup> ≠ 10<sup>x</sup></div>
  <div class="trap"><b class="t">함정 2</b> : R은 J 단위 → kJ로 바꾸기, mM → M</div>
  <div class="trap"><b class="t">함정 3</b> : 물·H⁺(pH 7)는 K·Q 식에서 빼기</div>
  <div class="trap"><b class="t">함정 4</b> : 자발성은 ΔG′°가 아니라 <b>ΔG</b>로 판단. 효소는 평형(K)을 못 바꾸고 속도만 높인다</div>
  <div class="trap"><b class="t">함정 5</b> : E′° 부호는 뒤집지 않는다, n = 2 빼먹지 않기</div>
  <div class="trap"><b class="t">함정 6</b> : 37 °C(생리적)면 RT = 2.578</div>
 </div>
</div></div>''',
f'''<div class="hd"><span class="pill">부록</span><h1>문제에 나오는 교과서 표</h1><span class="rt">Tables 13-4 · 13-6 · 13-7</span></div>
<div class="body"><div class="cols3">
 <div class="cc blue"><h4>표 13-4 · ΔG′° (kJ/mol)</h4>{table(['반응', 'ΔG′°'], [['ATP → ADP + P<sub>i</sub>', '−30.5'], ['ATP → AMP + PP<sub>i</sub>', '−45.6'], ['PP<sub>i</sub> → 2P<sub>i</sub>', '−19.2'], ['G6P → 포도당 + P<sub>i</sub>', '−13.8'], ['젖당 → 포도당 + 갈락토스', '−15.9'], ['G1P → G6P', '−7.3'], ['F6P → G6P', '−1.7'], ['말산 → 푸마르산 + H<sub>2</sub>O', '+3.1']], cls='left')}</div>
 <div class="cc orange"><h4>표 13-6 · 가수분해 ΔG′°</h4>{table(['화합물', 'ΔG′°'], [['PEP', '−61.9'], ['1,3-BPG', '−49.3'], ['포스포크레아틴', '−43.0'], ['ADP → AMP', '−32.8'], ['ATP → ADP', '−30.5'], ['아세틸-CoA', '−31.4'], ['F6P', '−15.9'], ['G6P', '−13.8'], ['글리세롤 3-P', '−9.2']], cls='left')}</div>
 <div class="cc purple"><h4>표 13-7 · E′° (V)</h4>{table(['짝 (산화형/환원형)', 'E′°'], [['½O<sub>2</sub>/H<sub>2</sub>O', '+0.816'], ['시토크롬 c', '+0.254'], ['푸마르산/숙신산', '+0.031'], ['옥살로아세트산/말산', '−0.166'], ['피루브산/젖산', '−0.185'], ['아세트알데하이드/에탄올', '−0.197'], ['FAD/FADH<sub>2</sub>', '−0.219'], ['NAD⁺/NADH', '−0.320'], ['NADP⁺/NADPH', '−0.324'], ['아세토아세트산/β-HB', '−0.346'], ['α-KG+CO<sub>2</sub>/아이소시트르산', '−0.38'], ['2H⁺/H<sub>2</sub> (pH 7)', '−0.414']], cls='left')}</div>
</div></div>''']
