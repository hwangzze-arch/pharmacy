# 01 요약 ② Hit → Lead (SAR) · Lead 조건
from lib import page, ph

ST = '--pc:var(--blue);--pcs:var(--blue-s)'


def add():
    page(ph('9주차', 'PART 01', 'Hit → Lead (SAR) · Lead의 조건', '6주차 슬라이드 40~43') + '''
<div class="body row">
  <div class="col" style="flex:1">
    <div class="lead"><span class="k">한 줄 요약</span>Hit을 <b>SAR 연구</b>로 개량해 Lead를 만든다. 핵심 골격을 나눠 R₁·R₂ 등을 바꿔가며 <span class="y">구조-활성 관계</span>를 규명한다.</div>
    <div class="fig"><img src="img/w6_41.jpg" style="height:40mm;object-fit:cover"><div class="figcap">구조 단순화 SAR 사례 — 치환기 변경에 따른 활성(pKi) 차이</div></div>
    <div class="callout memo"><div class="t">📈 농도 사다리</div><div class="small"><b>Hit μM → Lead 수백 nM → Candidate ≤100 nM</b><br>뒤로 갈수록 화학(구조)만이 아니라 <span class="g">생물(ADME·독성)</span>이 들어온다</div></div>
  </div>
  <div class="col" style="flex:1.05">
    <div class="card"><h3>Lead의 조건 (정확한 정의는 없으나)</h3>
    <ul class="dot small">
      <li><b>수백 nM</b> 수준 효과 (Hit은 μM)</li>
      <li>타겟 유효성 어느 정도 확인</li>
      <li><b>작용 기전(MOA)</b> 확립 (reversible/irreversible·kinetics)</li>
      <li>다른 분자 타겟에 대한 <b>선택성</b> 확인</li>
      <li>경쟁력·신규성 포함한 <b>특허성</b> 확인</li>
      <li>예비 PK (설치류 in vivo)</li>
    </ul></div>
    <div class="callout trap"><div class="t">⚠ Hit vs Lead vs Candidate</div><div class="small">효력 <b>μM → 수백 nM → ≤100 nM</b> · 선택성은 Candidate에서 <b>~1,000배</b><br>“Lead가 수백 nM”를 μM/100 nM로 바꾸면 ✗</div></div>
  </div>
</div>''', style=ST)
