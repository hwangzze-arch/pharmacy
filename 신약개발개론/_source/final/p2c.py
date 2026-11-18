# 02 요약 ③ Efficacy vs Potency · 내성 (교수님 출제 힌트)
from lib import page, ph

ST = '--pc:var(--teal);--pcs:var(--teal-s)'


def add():
    page(ph('11·12주차', 'PART 02', 'Efficacy vs Potency · 약물 내성', '11주차 38~41 · 12주차 Q&A') + '''
<div class="body col">
  <div class="row">
    <div class="col" style="flex:1">
      <div class="lead"><span class="k">한 줄 요약</span>잘 붙는 정도(affinity)와 최대 반응(Emax)은 <span class="y">독립적</span>. <b>효능 = Y축(천장), 역가 = X축(왼쪽일수록 ↑)</b>.</div>
      <table class="t small">
        <tr><th></th><th>역가(potency)</th><th>효능(efficacy)</th></tr>
        <tr><td>Fentanyl</td><td class="c">가장 높음</td><td class="c">높음</td></tr>
        <tr><td>Morphine</td><td class="c">중간</td><td class="c">펜타닐과 비슷</td></tr>
        <tr><td>Aspirin</td><td class="c">낮음</td><td class="c">낮음</td></tr>
      </table>
      <div class="callout memo"><div class="t">🧷 그래프 읽기</div><div class="small"><b>가장 왼쪽 곡선 = 역가 최고</b> · <b>가장 높은 천장 = 효능 최고</b> · Emax가 다르면 <span class="y">같은 반응값에서</span> 농도 비교</div></div>
    </div>
    <div class="col" style="flex:1">
      <div class="fig"><img src="img/w12_s10.jpg" style="height:36mm;object-fit:cover;object-position:top"><div class="figcap">내성 시 곡선이 오른쪽 이동 — EC50 수치↑(역가↓)</div></div>
      <div class="callout trap"><div class="t">⚠ 내성 시 변화</div><div class="small">같은 효과에 더 많은 양 → <b>Potency 감소 = EC50 수치 증가</b>(곡선 오른쪽). Emax는 유지 또는 감소. <span class="p">“EC50 감소” ✗</span></div></div>
    </div>
  </div>
  <div class="callout trap" style="border-color:#f5b6cb;background:#fff1f5"><div class="t" style="color:#c2185b">📣 교수님 출제 힌트 (12주차)</div><div class="small">“요런 그래프들 … 약물 내성, 항암제 … <b>예시 문제로 내기 좋은 주제</b>” — 항체 기반 2·3차 항암제를 일찍 안 쓰는 이유 = 종양 내성(역가↓·독성 농도 접근·효과↓). 11주차: <b>A·B·C·D 그래프에서 “포텐시 최고”, “포텐시 높고 에피커시 낮은 약 고르기”</b> 식 출제 예고.</div></div>
</div>''', style=ST)
