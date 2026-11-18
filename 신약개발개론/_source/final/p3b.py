# 03 요약 ② GLP · QAU · 흐름
from lib import page, ph

ST = '--pc:var(--violet);--pcs:var(--violet-s)'


def add():
    page(ph('12주차', 'PART 03', 'GLP — 정의 · 필요성 · QAU · 흐름', '12주차 슬라이드 44~48') + '''
<div class="body col">
  <div class="row">
    <div class="col" style="flex:1">
      <div class="lead" style="font-size:11pt"><span class="k">한 줄 요약</span><b>GLP = 비임상시험 관리기준.</b> 허가 신청용 비임상 시험의 <span class="y">계획·실시·점검·기록·보고·보관</span> 절차를 정한 규정.</div>
      <div class="card"><h3 style="font-size:10.5pt">필요성 · 역사</h3>
      <div class="small">· 목적 = 안전성시험자료의 <b>신뢰성</b> 확보<br>· 계기 = <b>탈리도마이드</b> 기형유발(동물시험 신뢰성 문제)<br>· 1970년대 미국 FDA → <b>1981 OECD</b> 국제 통합<br>· 현재 허가용 모든 안전성시험은 GLP 준수</div></div>
    </div>
    <div class="col" style="flex:1">
      <div class="card" style="border-color:#c9bdf3"><h3 style="font-size:10.5pt;color:#5b3fd1">QAU — 핵심 장치</h3>
      <div class="small"><b>QAU = Quality Assurance Unit (품질보증부서)</b><br>· 시험팀과 <b>독립된 제3자</b>가 관리·감독·점검<br>· 시험하는 사람이 스스로 “잘했다” → 못 믿음<br>→ 분리된 부서가 계획·실시·보고를 따로 점검해 신뢰성 보증</div></div>
      <div class="callout memo"><div class="t">🔁 GLP 시험 흐름</div><div class="small"><b>개시 → 준비 → 실시 → Data 처리 → 종료 → 검체·자료 보관</b><br>각 단계에 <b>QA 점검</b>이 병행 · SOP·시험책임자·운영책임자·QAU 분리</div></div>
    </div>
  </div>
  <div class="callout trap"><div class="t">⚠ 단답 주의</div><div class="small"><b>QAU</b> = Quality Assurance Unit · <b>GLP</b> = Good Laboratory Practice · <b>SOP</b> = Standard Operating Procedure — 풀네임 철자까지. 계기 = <b>탈리도마이드</b>, 국제 통합 = <b>1981 OECD</b>.</div></div>
</div>''', style=ST)
