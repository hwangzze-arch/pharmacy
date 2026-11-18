# 03 요약 ① 전임상 동물연구 · 탐색적 vs 규제적
from lib import page, ph

ST = '--pc:var(--violet);--pcs:var(--violet-s)'


def add():
    page(ph('12주차', 'PART 03', '전임상연구 — 동물연구 · 탐색적 vs 규제적', '12주차 슬라이드 37~42') + '''
<div class="body row">
  <div class="col" style="flex:1">
    <div class="lead"><span class="k">한 줄 요약</span>후보물질의 <span class="y">유효성 + 안전성(독성)</span>을 동물에서 검증. <b>Drug Candidate를 기준</b>으로 탐색적/규제적 전임상이 갈린다.</div>
    <div class="card"><h3 style="font-size:10.5pt">동물종 — 왜 쥐를 쓰나</h3>
    <div class="small">유전적 유사성 <b>침팬지 99% &gt; 쥐 81%</b>인데도 쥐 사용 →<br>비용 저렴 · 작아서 관리 용이 · 번식 빠름 · 유전자 조작 쉬움<br><span class="p">“쥐가 사람과 더 유사해서” ✗</span></div></div>
    <div class="callout memo"><div class="t">🧷 포함 항목</div><div class="small">ADME 체내동태 + 약효/약리 + <b>가역성(reversibility)·성별 차이·잠복기·용량 연관성</b></div></div>
  </div>
  <div class="col" style="flex:1">
    <table class="t">
      <tr><th></th><th>탐색적</th><th>규제적</th></tr>
      <tr><td>시점</td><td>후보물질 <b>이전</b></td><td>후보물질 <b>이후</b></td></tr>
      <tr><td>단계</td><td>약물발굴<br>(Discovery)</td><td>약물개발<br>(Development)</td></tr>
      <tr><td><b>GLP</b></td><td class="c">불필요</td><td class="c">필수</td></tr>
      <tr><td>목적</td><td>후보 탐색<br>방향 결정</td><td>독성 용량<br>규명</td></tr>
    </table>
    <div class="callout trap"><div class="t">⚠ 함정</div><div class="small">경계선 = <b>Drug Candidate 선정</b>. <span class="p">탐색적↔규제적을 바꾸거나 GLP 적용을 뒤집는 보기 주의</span>.</div></div>
  </div>
</div>''', style=ST)
