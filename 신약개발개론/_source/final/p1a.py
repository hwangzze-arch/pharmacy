# 01 요약 ① Hit 도출 스크리닝
from lib import page, ph

ST = '--pc:var(--blue);--pcs:var(--blue-s)'


def add():
    page(ph('9주차', 'PART 01', 'Hit 도출 — 어떻게 거르나 (가상 스크리닝 · 세 방법)', '6주차 슬라이드 34~39') + '''
<div class="body row">
  <div class="col" style="flex:1.05">
    <div class="lead"><span class="k">한 줄 요약</span>Hit 단계의 목표는 <span class="y">일단 타겟에 붙는가</span>. 기준 <b>10 μM ~ 수십 μM</b>, 구조가 다른 <b>Hit 3~5종 이상</b>을 확보해 Lead로 넘긴다.</div>
    <div class="fig"><img src="img/w6_34.jpg" style="height:43mm;object-fit:cover;object-position:top"><div class="figcap">가상 스크리닝 깔때기: 라이브러리 → 3가지 기반 → 도킹 → 유사성 → 필터 → Hit</div></div>
    <div class="callout memo"><div class="t">📚 라이브러리 · 필터</div><div class="small"><b>실물</b> WuXi HTS 30만·Mcule 650만 / <b>가상</b> Enamine 13.6억·GalaXi 34억<br>마지막 필터 = <span class="y">Rule of 5 · PAINS · Reactive groups</span></div></div>
  </div>
  <div class="col" style="flex:1">
    <table class="t">
      <tr><th></th><th>HTS</th><th>FBDD</th><th>동적 주형</th></tr>
      <tr><td>넣는 것</td><td>완성 화합물<br>수십만~수백만</td><td>작은 조각<br>(fragment)</td><td>연결기 단<br>조각</td></tr>
      <tr><td>표적 구조</td><td class="c">없어도 됨</td><td class="c">필요</td><td class="c">필요</td></tr>
      <tr><td>위치</td><td class="c">표준·범용</td><td class="c">증가</td><td class="c">연구</td></tr>
    </table>
    <div class="callout tip"><div class="t">💡 교수님 비유 (Q&amp;A)</div><div class="small">화학 신약 = <b>레고 조립</b>(작은 조각 → 수십만 모양), 바이오 신약 = <b>완제품</b>(항체가 이미 표적을 앎 → 개수 적음)</div></div>
    <div class="callout trap"><div class="t">⚠ 함정</div><div class="small">가장 많이 쓰는 방법 = <b>HTS</b>는 맞지만, <span class="p">“모든 표적에서 가장 효율적”은 ✗</span>. 탐색 효율은 FBDD가 강점.</div></div>
  </div>
</div>''', style=ST)
