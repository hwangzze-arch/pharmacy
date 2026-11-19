# 01 요약 ③ Lead 최적화 · UCL 로드맵 · AI
from lib import page, ph

ST = '--pc:var(--blue);--pcs:var(--blue-s)'


def add():
    page(ph('9주차', 'PART 01', 'Lead 최적화 → 후보물질 · UCL 로드맵 · AI', '6주차 슬라이드 44~58') + '''
<div class="body col">
  <div class="row">
    <div class="col" style="flex:1">
      <div class="lead" style="font-size:11pt"><span class="k">한 줄 요약</span><b>Lead 최적화 = 화학 구조를 바꿀 수 있는 마지막 단계.</b> 후보물질(Candidate) 선정 후에는 용량만 조절 → Drug Discovery에서 <span class="y">가장 오래 걸리는 단계</span>.</div>
      <div class="card"><h3>Candidate 조건 (슬라이드 46)</h3>
      <ul class="dot small">
        <li><b>EC50 / IC50 ≤ 100 nM</b></li>
        <li>유사 타겟과 <b>~1,000배</b> 선택성</li>
        <li>적절한 용해도 · in vivo PK</li>
        <li>주요 <b>CYP450</b> 저해/유도 확인</li>
        <li>동물 약효 · 단회~2주 독성 안전성</li>
        <li>in vitro 변이원성(Ames·소핵) · 특허 출원</li>
      </ul></div>
    </div>
    <div class="col" style="flex:1.1">
      <div class="fig"><img src="img/w6_47.jpg" style="height:40mm;object-fit:cover;object-position:top"><div class="figcap">Lead 최적화 사례: 글리벡(Glivec) — 세포 활성↑ · 티로신 키나아제 선택성 · PKC 결합 제거 · 용해도·경구 흡수↑</div></div>
      <div class="callout memo"><div class="t">🤖 AI 기반 Hit to Lead</div><div class="small">DB → 정제·필터링 → AI → <b>평가(MW·LogP·SA·QED·NP)</b> → 결과 평가<br>GENTRL: 전통 2~3년 → <b>&lt;2개월</b> (DDR1 저해제)</div></div>
    </div>
  </div>
  <div class="callout tip"><div class="t">💡 로드맵 공통 출발 = IDEA·IP·PPI</div><div class="small">저분자·바이오·세포유전자 로드맵 모두 <b>미충족 의료수요(TPP) · 지식재산권(IP) · 환자참여(PPI)</b>로 시작. 바이오는 중간 개발 단계부터 <b>규제</b>가 들어오고, 세포·유전자 치료제는 <b>더 까다로운 규제 자문</b>이 필요하다.</div></div>
</div>''', style=ST)
