# -*- coding: utf-8 -*-
from helpers import *
import content_a, content_b

CHAPTER = '13'
CH_TITLE = '생체에너지론'
CH_EN = 'Bioenergetics and Biochemical Reaction Types'
ALL_ITEMS = content_a.ITEMS + content_b.ITEMS
STAT = ('6', '꼭 외울 공식')
SCOPE = '교수님 13장 강의(슬라이드 1–54) 범위 = <b>13.1 생체에너지론과 열역학</b>, <b>13.3 인산기 전달과 ATP</b>, <b>13.4 생물학적 산화-환원</b>. 이 범위와 연결된 예제·문제만 골랐어.'
INCLUDE = ['<b>본문 예제</b> 13-1, 13-2, 13-3',
           '<b>ΔG′°·K′<sub>eq</sub>·ΔG 계산</b> — 문제 1–6, 9, 10, 13–15',
           '<b>ATP·인산기 전달·공역</b> — 문제 7, 8, 12, 20–25',
           '<b>능동수송 에너지</b> — 문제 26',
           '<b>산화-환원 · 환원 전위</b> — 문제 27–33']
EXCLUDE = ['<b>문제 16–19</b> — 13.2절 반응 메커니즘 (강의 범위 밖)',
           '<b>문제 36</b> — K<sub>m</sub>·V<sub>max</sub> (6장 내용)',
           '<b>문제 37</b> — DATA ANALYSIS PROBLEM']
GUIDE_EXTRA = f'''<div class="card" style="margin-top:4mm"><h4>🔢 자주 쓰는 숫자 (표 13-1)</h4>
<div class="tiles">
 <div><b>R</b><span>8.315 J/mol·K</span><small>kJ면 8.315×10<sup>−3</sup></small></div>
 <div><b>RT (25 °C)</b><span>2.478 kJ/mol</span><small>“표준 조건”</small></div>
 <div><b>RT (37 °C)</b><span>2.578 kJ/mol</span><small>“체온·생리적”</small></div>
 <div><b>F</b><span>96.48 kJ/V·mol</span><small>n = 전자 수 (NADH 2)</small></div>
 <div><b>RT/F (25 °C)</b><span>0.0257 V</span><small>E 농도 보정</small></div>
 <div><b>ATP → ADP + P<sub>i</sub></b><span>−30.5 kJ/mol</span><small>13장 기준값</small></div>
</div>
{warn('계산기의 <b>ln</b>(자연로그)과 <b>log</b>(상용로그)를 헷갈리지 말 것! ln x = 2.303 × log x.  그리고 mM → M은 ×10<sup>−3</sup>.')}
</div>'''


def cheat_page():
    down = svg(250, 110,
               '<path d="M10,30 C80,30 90,95 240,95" fill="none" stroke="#1e3a8a" stroke-width="3"/>'
               '<circle cx="36" cy="22" r="9" fill="#ea580c"/>' +
               T(30, 58, '반응물', 10.5, '#1e3a8a', weight=700) + T(215, 85, '생성물', 10.5, '#1e3a8a', weight=700) +
               arrowdef('cd', '#16a34a') +
               '<line x1="150" y1="34" x2="150" y2="86" stroke="#16a34a" stroke-width="2" marker-end="url(#cd)"/>' +
               T(158, 58, 'ΔG &lt; 0', 11, '#16a34a', 'start', 700) + T(158, 72, '내리막 = 저절로', 9.5, '#16a34a', 'start'))
    return f'''
<h2 class="pt"><span class="n">KIT</span> 먼저 이것만! 13장 계산 문제 생존 키트</h2>
<p class="lead">13장 계산 문제는 거의 전부 아래 6개 중 하나(또는 조합)야. 막히면 이 페이지로 돌아와.</p>
<div class="grid3">
 <div class="card"><h4><span class="no">1</span> ΔG의 부호 = 반응 방향</h4>
  <figure class="fig" style="margin:0">{down}</figure>
  <p><b>ΔG &lt; 0</b> 저절로 진행 · <b>ΔG = 0</b> 평형 · <b>ΔG &gt; 0</b> 역방향이 저절로. 공이 언덕을 굴러 내려가듯 G가 낮아지는 쪽으로.</p>
 </div>
 <div class="card"><h4><span class="no">2</span> ΔG′° ↔ K′<sub>eq</sub></h4>
  <div class="formula"><i>ΔG′°</i> = −<i>RT</i> ln <i>K′</i><sub>eq</sub></div>
  <div class="formula"><i>K′</i><sub>eq</sub> = e<sup>−ΔG′°/RT</sup></div>
  <p>K &gt; 1 ⇔ ΔG′° &lt; 0 · K &lt; 1 ⇔ ΔG′° &gt; 0</p>
  <p><b>10배 규칙</b>: 25 °C에서 K ×10 ⇔ ΔG′° −5.7 kJ/mol</p>
 </div>
 <div class="card"><h4><span class="no">3</span> 실제 ΔG = 표준값 + 농도 보정</h4>
  <div class="formula"><i>ΔG</i> = <i>ΔG′°</i> + <i>RT</i> ln <i>Q</i></div>
  <p>Q = {F('[생성물]', '[반응물]')} (지금 농도, <b>M 단위</b>, 물은 빼기)</p>
  <p>Q &lt; K → ΔG &lt; 0 → 정반응 / Q = K → 평형</p>
 </div>
 <div class="card"><h4><span class="no">4</span> 짝지은(공역) 반응</h4>
  <div class="formula"><i>ΔG′°</i><sub>합</sub> = <i>ΔG′°</i><sub>1</sub> + <i>ΔG′°</i><sub>2</sub> &nbsp;·&nbsp; <i>K′</i><sub>합</sub> = <i>K′</i><sub>1</sub> × <i>K′</i><sub>2</sub></div>
  <p>반응을 <b>뒤집으면 ΔG′° 부호 반대</b>, K는 역수(1/K).</p>
 </div>
 <div class="card"><h4><span class="no">5</span> 산화-환원: 전위차 → 자유에너지</h4>
  <div class="formula"><i>ΔE′°</i> = <i>E′°</i><sub>받는 쪽</sub> − <i>E′°</i><sub>주는 쪽</sub></div>
  <div class="formula"><i>ΔG′°</i> = −<i>nF ΔE′°</i></div>
  <p>전자는 E′°가 <b>낮은(−) 쪽 → 높은(+) 쪽</b>으로.</p>
 </div>
 <div class="card"><h4><span class="no">6</span> 실제 환원 전위</h4>
  <div class="formula"><i>E</i> = <i>E′°</i> + {F('<i>RT</i>', '<i>nF</i>')} ln {F('[산화형]', '[환원형]')}</div>
  <p>산화형(전자 받을 놈)이 많을수록 E가 커진다(+).</p>
 </div>
</div>'''



def tables_pages():
    t4 = table(['반응', 'ΔG′° (kJ/mol)'], [
        ['ATP + H<sub>2</sub>O → ADP + P<sub>i</sub>', '−30.5'], ['ATP + H<sub>2</sub>O → AMP + PP<sub>i</sub>', '−45.6'],
        ['PP<sub>i</sub> + H<sub>2</sub>O → 2P<sub>i</sub>', '−19.2'], ['포도당 6-인산 + H<sub>2</sub>O → 포도당 + P<sub>i</sub>', '−13.8'],
        ['젖당 + H<sub>2</sub>O → 포도당 + 갈락토스', '−15.9'], ['포도당 1-인산 → 포도당 6-인산', '−7.3'],
        ['과당 6-인산 → 포도당 6-인산', '−1.7'], ['말산 → 푸마르산 + H<sub>2</sub>O', '+3.1']], cls='left')
    t6 = table(['화합물 (가수분해)', 'ΔG′° (kJ/mol)'], [
        ['포스포엔올피루브산 (PEP)', '−61.9'], ['1,3-이인산글리세르산', '−49.3'], ['포스포크레아틴 (PCr)', '−43.0'],
        ['ADP (→ AMP + P<sub>i</sub>)', '−32.8'], ['ATP (→ ADP + P<sub>i</sub>)', '−30.5'], ['ATP (→ AMP + PP<sub>i</sub>)', '−45.6'],
        ['아세틸-CoA (티오에스터)', '−31.4'], ['과당 6-인산', '−15.9'], ['포도당 6-인산', '−13.8'], ['글리세롤 3-인산', '−9.2']], cls='left')
    t5 = table(['세포', 'ATP', 'ADP', 'AMP', 'P<sub>i</sub>', 'PCr'], [
        ['쥐 간세포', '3.38', '1.32', '0.29', '4.8', '0'], ['쥐 근육세포', '8.05', '0.93', '0.04', '8.05', '28'],
        ['쥐 뉴런', '2.59', '0.73', '0.06', '2.72', '4.7'], ['사람 적혈구', '2.25', '0.25', '0.02', '1.65', '0'], ['대장균', '7.90', '1.04', '0.82', '7.9', '0']])
    rows7 = [
        ['½O<sub>2</sub> + 2H<sup>+</sup> + 2e<sup>−</sup> → H<sub>2</sub>O', '<b>+0.816</b>'], ['Fe<sup>3+</sup> + e<sup>−</sup> → Fe<sup>2+</sup>', '+0.771'],
        ['시토크롬 c (Fe<sup>3+</sup>) + e<sup>−</sup> → (Fe<sup>2+</sup>)', '+0.254'], ['유비퀴논 + 2H<sup>+</sup> + 2e<sup>−</sup> → 유비퀴놀', '+0.045'],
        ['푸마르산 + 2H<sup>+</sup> + 2e<sup>−</sup> → 숙신산', '+0.031'], ['2H<sup>+</sup> + 2e<sup>−</sup> → H<sub>2</sub> (표준, pH 0)', '0.000'],
        ['옥살로아세트산 + 2H<sup>+</sup> + 2e<sup>−</sup> → 말산', '−0.166'], ['피루브산 + 2H<sup>+</sup> + 2e<sup>−</sup> → 젖산', '−0.185'],
        ['아세트알데하이드 + 2H<sup>+</sup> + 2e<sup>−</sup> → 에탄올', '−0.197'], ['FAD + 2H<sup>+</sup> + 2e<sup>−</sup> → FADH<sub>2</sub>', '−0.219'],
        ['리포산 + 2H<sup>+</sup> + 2e<sup>−</sup> → 다이하이드로리포산', '−0.29'],
        ['NAD<sup>+</sup> + H<sup>+</sup> + 2e<sup>−</sup> → NADH', '<b>−0.320</b>'], ['NADP<sup>+</sup> + H<sup>+</sup> + 2e<sup>−</sup> → NADPH', '−0.324'],
        ['아세토아세트산 + 2H<sup>+</sup> + 2e<sup>−</sup> → β-하이드록시뷰티르산', '−0.346'],
        ['α-케토글루타르산 + CO<sub>2</sub> + 2H<sup>+</sup> + 2e<sup>−</sup> → 아이소시트르산', '−0.38'],
        ['2H<sup>+</sup> + 2e<sup>−</sup> → H<sub>2</sub> (pH 7)', '−0.414'], ['페레독신 (Fe<sup>3+</sup>) + e<sup>−</sup> → (Fe<sup>2+</sup>)', '−0.432']]
    head7 = ['반쪽 반응 (산화형 + e<sup>−</sup> → 환원형)', 'E′° (V)']
    p1 = f'''<h2 class="pt"><span class="n">DATA</span> 문제에 나오는 교과서 표 모음</h2>
<p class="lead">문제에서 “Table 13-4 / 13-5 / 13-6을 이용하라”고 하면 여기서 찾으면 돼.</p>
<div class="grid3">
 <div class="card"><h4>표 13-4 · 표준 자유에너지 변화 (일부)</h4>{t4}</div>
 <div class="card"><h4>표 13-6 · 인산 화합물 가수분해 ΔG′°</h4>{t6}</div>
 <div class="card"><h4>표 13-5 · 세포 속 농도 (mM)</h4>{t5}</div>
</div>'''
    p2 = f'''<h2 class="pt"><span class="n">DATA</span> 표 13-7 · 표준 환원 전위 E′°</h2>
<p class="lead">위로 갈수록(+) 전자를 <b>받으려는</b> 힘이 세고, 아래로 갈수록(−) 전자를 <b>주려는</b> 힘이 세다. 전자는 <b>아래 → 위</b>로 흐른다.</p>
<div class="grid2">
 <div class="card">{table(head7, rows7[:9], cls='left')}</div>
 <div class="card">{table(head7, rows7[9:], cls='left')}</div>
</div>'''
    return p1, p2



def front_pages():
    return [cheat_page(), *tables_pages()]
