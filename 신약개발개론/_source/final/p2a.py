# 02 요약 ① 후보물질 선정 — 활성 + 속성
from lib import page, ph

ST = '--pc:var(--teal);--pcs:var(--teal-s)'


def add():
    page(ph('11주차', 'PART 02', '후보물질 선정 — 활성 + 속성 동시 최적화', '11주차 슬라이드 31~33') + '''
<div class="body row">
  <div class="col" style="flex:1">
    <div class="lead"><span class="k">한 줄 요약</span>후보물질은 <span class="y">활성(activity)뿐 아니라 속성(property)</span>까지 갖춘 <b>Drug-like</b> 물질. 개발공정에선 <b>PD·PK·독성</b>을 집중 분석한다.</div>
    <div class="fig"><img src="img/w11_s29.jpg" style="height:38mm;object-fit:cover;object-position:top"><div class="figcap">후보물질 선정과정 — Lead 최적화 · Candidate Selection 반복 평가</div></div>
    <div class="callout trap"><div class="t">⚠ 함정</div><div class="small"><span class="p">“in vitro 효능만 좋으면 된다” ✗</span> — 동물에서 혈중농도 유지 못하면 신약 가치 상실. PD·PK·독성 = <b>임상 용량·IND의 근거</b>.</div></div>
  </div>
  <div class="col" style="flex:1">
    <div class="card"><h3>왜 속성(property)이 중요한가</h3>
    <ul class="dot small">
      <li>이상적 약물 = 표적엔 강하게, 다른 경로엔 <b>최소 효과</b></li>
      <li>전임상 독성 데이터 = <b>안전성 신뢰</b> 제공</li>
      <li>PD·PK·독성 = 임상 투약용량 결정 → <b>IND 필수</b></li>
      <li>용해도·안정성·물리화학적 속성 데이터 필요</li>
    </ul></div>
    <div class="callout memo"><div class="t">🔑 PK vs PD</div><div class="small"><b>PK</b> = 몸이 약에게 (ADME, 시간 vs 농도) &nbsp;/&nbsp; <b>PD</b> = 약이 몸에게 (용량 vs 반응, 시간 축 없음)<br>“PK 먼저, 그다음 PD”</div></div>
  </div>
</div>''', style=ST)
