# 03 요약 ④ 동물실험 대체법 — FDA 현대화법 2.0 · 오가노이드 · Organ-on-a-chip (13주차 보강)
from lib import page, ph

ST = '--pc:var(--violet);--pcs:var(--violet-s)'


def add():
    page(ph('13주차 보강', 'PART 03', '동물실험 대체법 — FDA 현대화법 2.0 · 오가노이드 vs Organ-on-a-chip', '13주차 보강 슬라이드 33~52') + '''
<div class="body col">
  <div class="row">
    <div class="col" style="flex:1">
      <div class="card" style="border-color:#c9bdf3"><h3 style="font-size:10.5pt;color:#5b3fd1">FDA 현대화법 2.0 (2022년 12월)</h3>
      <div class="small"><b>1938~2022</b>: 신약 승인에 동물실험 <b>필수</b><br>→ 이제 <b>동물 또는 비동물</b> 시험 후 임상 가능 = <b>허용</b>(요구·금지 ✗)<br>FDA 독성학자는 <b>보수적</b> · 비동물은 장기 하나씩은 보지만 <b>장기 통합성</b>은 보기 어려움<br>→ 동물실험이 <b>아예 없어지진 않을 것</b> · 비동물 평가를 조금씩 받아들이는 추세</div></div>
      <div class="card"><h3 style="font-size:10.5pt">동물 → 사람에 가깝게</h3>
      <div class="small"><b>휴머나이즈드 마우스</b> = 방사선으로 골수 파괴 → <b>사람 골수 이식</b> → 사람 면역세포를 가진 쥐(면역항암제 연구)<br>그래도 생쥐 ≠ 사람 → <b>Human-on-a-chip</b>(장기 칩 연결) · 환자 세포로 <b>개인 맞춤 질병 모델</b></div></div>
    </div>
    <div class="col" style="flex:1.15">
      <table class="t">
        <tr><th></th><th>오가노이드</th><th>Organ-on-a-chip</th></tr>
        <tr><td>출발</td><td><b>iPSC</b>(야마나카, 4유전자) 등 줄기세포</td><td>세포를 <b>3D로 재구성</b></td></tr>
        <tr><td>핵심</td><td>어떻게 <b>분화</b>됐나</td><td><b>영양 공급</b>(혈관·미세유체 흐름)</td></tr>
        <tr><td>강점</td><td>장기 특징을 가장 잘 대변</td><td>영양 공급 · 3D 노출</td></tr>
        <tr><td>약점</td><td>흐름(관류) 없음</td><td>생물학적 특징 덜함</td></tr>
      </table>
      <div class="small" style="margin-top:1.5mm">→ 둘을 합친 <b>오가노이드-온-칩</b>(예: 뇌) · 세포 출처 ESC(요즘 거의 안 씀)·<b>iPSC·성체줄기세포</b>·일차세포·세포주 · 채널 single / dual / multi</div>
      <div class="callout memo"><div class="t">🔬 교수님 간 칩</div><div class="small"><b>간세포 + 혈관(HUVEC) + 염증(쿠퍼) + 성상세포</b> 4종 3D 구체 + ECM → <b>유리지방산</b>으로 지방간 → 지방간염 → 섬유화 · 간 기능 = <b>알부민</b> 분비 · 피르페니돈 농도 기울기 시험<br><span class="p">세부 데이터는 “그렇게 기억하지 않으셔도 좋다”</span></div></div>
    </div>
  </div>
  <div class="callout trap"><div class="t">⚠ 한계 · 함정</div><div class="small">2D(바닥 배양)는 <b>아직 FDA 승인 불가</b> · 칩 한계 = <b>비용</b>(동물 1마리 ≈ 3만 원 vs 칩 1개 ≈ 100만 원) + <b>장기 통합성</b>(칩 5~6개를 묶어야) · <span class="p">“현대화법 2.0 = 동물실험 금지/비동물 의무화” ✗ · 오가노이드↔칩 정의 맞바꾸기 ✗</span></div></div>
</div>''', style=ST)
