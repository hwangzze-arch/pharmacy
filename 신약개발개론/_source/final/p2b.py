# 02 요약 ② PD — 용량-반응 · Emax·EC50·TD50·LD50·TI
from lib import page, ph

ST = '--pc:var(--teal);--pcs:var(--teal-s)'


def add():
    page(ph('11·12주차', 'PART 02', 'PD — 용량-반응 곡선 · 5대 지표', '11주차 34~41 · 12주차 Q&A') + '''
<div class="body col">
  <div class="row">
    <div class="col" style="flex:1.1">
      <div class="lead" style="font-size:11pt"><span class="k">한 줄 요약</span>PD = 약물 용량·농도와 효과의 관계. <span class="y">로그 스케일 S자형 용량-반응 곡선</span>으로 치료효과와 이상반응을 함께 본다.</div>
      <table class="t">
        <tr><th>기호</th><th>뜻</th><th>축</th></tr>
        <tr><td><b>Emax</b></td><td>약이 낼 수 있는 <b>최대 효과</b> = 효능(efficacy)</td><td class="c">Y축(천장)</td></tr>
        <tr><td><b>EC50</b></td><td>최대 효과의 <b>50%</b> 농도 = 역가(potency)</td><td class="c">X축(50% 지점)</td></tr>
        <tr><td><b>TD50</b></td><td>집단 절반에 <b>독성</b></td><td class="c">—</td></tr>
        <tr><td><b>LD50</b></td><td>집단 절반에 <b>사망</b>(동물실험)</td><td class="c">—</td></tr>
        <tr><td><b>TI</b></td><td>치료계수 = <b>TD50 / ED50</b> (넓을수록 안전)</td><td class="c">—</td></tr>
      </table>
    </div>
    <div class="col" style="flex:1">
      <div class="fig"><img src="img/w12_s08.jpg" style="height:36mm;object-fit:cover;object-position:top"><div class="figcap">치료 창(therapeutic window) — 치료 곡선과 독성 곡선 사이</div></div>
      <div class="callout tip"><div class="t">💡 약처방 = 80~90%</div><div class="small">Emax(100%)로 처방 ✗ → “모든 약은 독”, 고농도는 독성 농도 접근. 치료 창이 넓은 약(항히스타민제)만 드물게 Emax.</div></div>
    </div>
  </div>
  <div class="callout trap"><div class="t">⚠ EC50은 독성 시작점이 아니다</div><div class="small">EC50 = <b>효능의 절반 농도·역가 지표</b>일 뿐. 50%를 쓰는 이유 = <span class="y">S자 곡선의 가운데가 기울기가 안정적·선형에 가까워</span> 비교가 쉬움(10·20·80%는 기울기 변화가 큼). 효과와 독성은 다른 곡선.</div></div>
</div>''', style=ST)
