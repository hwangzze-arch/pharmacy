# 03 요약 ③ Non-GLP 전임상 — 실험동물 · 안전성 → 유효성 (13주차 보강)
from lib import page, ph

ST = '--pc:var(--violet);--pcs:var(--violet-s)'


def add():
    page(ph('13주차 보강', 'PART 03', 'Non-GLP 전임상 — 실험동물 · 1단계 안전성 → 2단계 유효성', '13주차 보강 슬라이드 2~32') + '''
<div class="body row">
  <div class="col" style="flex:1">
    <div class="lead"><span class="k">한 줄 요약</span>제목의 <b>Non-GLP 전임상 = 탐색적 전임상</b>. 신기술은 <span class="y">1단계 안전성 → 2단계 유효성</span> 순서로 검증한다.</div>
    <div class="card"><h3 style="font-size:10.5pt">탐색적(Non-GLP) — 교수님 정리</h3>
    <div class="small">GLP <b>반드시 적용할 필요 없음</b> · 방법이 유연 · <b>케이스 바이 케이스</b><br>선도물질 선정 <b>이전</b>에도 수행 · <b>약물 발굴</b> 단계에 중요<br>비임상에서 하는 것 = 약리(효능) · 약동 · 독성 + <b>CMC</b>(제형·생산)</div></div>
    <div class="card"><h3 style="font-size:10.5pt">실험동물</h3>
    <div class="small">가장 많이 쓰는 = <b>설치류</b>(유전자 조작 쉬움) · 생쥐 = 연구의 약 75%<br>제브라피시·초파리 = 싸고 세대 짧음(투명 배아 = 제브라피시)<br>동물-질환모델 짝: 생쥐 = 종양·상처·비만 · 랫드 = 뼈·힘줄·간 출혈 · <b>토끼 = 골관절염</b></div></div>
  </div>
  <div class="col" style="flex:1">
    <table class="t">
      <tr><th></th><th>1단계 안전성</th><th>2단계 유효성</th></tr>
      <tr><td>질문</td><td>몸이 받아들이나<br>(<b>생체적합성</b> = 숙주 반응)</td><td>치료 효과가 있나<br>(Therapeutic efficacy)</td></tr>
      <tr><td>세포</td><td>Live/Dead · 생존율 · 증식<br><b>미토콘드리아 활성</b></td><td>표적 장기 세포 in vitro</td></tr>
      <tr><td>동물</td><td>생분해성 · 전신·흡입 독성<br>혈액·혈청 검사</td><td>동물 <b>질환 모델</b><br>기능·현미경·유전자/단백질</td></tr>
      <tr><td>기준</td><td><b>ISO 10993-1</b> 표</td><td>→ GLP·임상의 <b>지표</b></td></tr>
    </table>
    <div class="callout memo"><div class="t">🧷 고려 항목 (Non-GLP에서 질문)</div><div class="small">대상 질환 · 적용 방법 · 분해성 · <b>멸균</b> · 열안정성(mRNA 백신 <b>콜드 체인</b>) · 생존 기간 · 투여 경로(피하 이식·국소·<b>위관 = 경구</b>·흡입)</div></div>
    <div class="callout trap"><div class="t">⚠ 함정</div><div class="small">순서 <b>안전성 → 유효성</b>(뒤집기 ✗) · 세포 수준(in vitro) → 동물(in vivo) · <span class="p">“토끼 = 종양 모델” ✗ (토끼 = 골관절염)</span></div></div>
  </div>
</div>''', style=ST)
