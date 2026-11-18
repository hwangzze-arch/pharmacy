# 02 요약 ④ PK — ADME · 생체이용률 · 분포 · 대사 · 배설
from lib import page, ph

ST = '--pc:var(--teal);--pcs:var(--teal-s)'


def add():
    page(ph('11·12주차', 'PART 02', 'PK — ADME · 생체이용률 · 분포 · 대사 · 배설', '11주차 44~65 · 12주차 전체') + '''
<div class="body col">
  <div class="row">
    <div class="col" style="flex:1">
      <div class="card"><h3 style="font-size:10.5pt">A · 흡수 — 생체이용률(F)</h3>
      <div class="small"><b>F = 전신순환 도달량 / 투여량</b><br>· <b>IV = 1</b>(100%) · 근육·피하 &lt; IV, &gt; 경구 · <b>경구(PO) &lt; 1</b><br>· 손실: 용해 → 장벽 흡수 → <span class="y">간 1차 통과(first-pass)</span> → 담즙<br>· <b>AUC</b> = 혈중농도 곡선 아래 면적 = 흡수량(경구 AUC &lt; IV)<br>· 단백질·펩타이드·mRNA = 소화효소에 분해 → <b>주사</b></div></div>
      <div class="card"><h3 style="font-size:10.5pt">D · 분포 — 장벽 · 단백질 결합</h3>
      <div class="small">· 혈관 장벽 3곳 = <b>뇌(BBB)·눈·정소/난소</b><br>· <b>알부민에 붙은 약은 혈관 밖으로 못 나감</b>(유리 약물만 이동)<br>· 지용성 약물 = 지방에 저장 → 오래 작용(개인차 큼)<br>· 간질액: 하루 ~20 L 유출 → 17 L 삼투압 회수, 3 L 림프</div></div>
    </div>
    <div class="col" style="flex:1">
      <div class="card"><h3 style="font-size:10.5pt">M · 대사 — 간 · Phase I/II</h3>
      <div class="small">· 대부분 <b>간</b>(가장 큰 고형장기, 80~90% 간세포)<br>· 경구 <b>A-M-D-E</b> / 주사 <b>A-D-M-E</b>(1차 통과 없음)<br>· <b>Phase I</b> = 산화·환원·가수분해(<span class="y">CYP450</span>)<br>· <b>Phase II</b> = 포합(글루쿠론산·황산·글리신·GSH·아세틸·메틸)<br>· 핵심 효소 = <b>CYP450(cytochrome P450)</b></div></div>
      <div class="card"><h3 style="font-size:10.5pt">E · 배설 — 신장</h3>
      <div class="small">· 흡수된 약은 대부분 <b>신장(소변)</b>, 소수 담즙, 소량 호흡·땀<br>· 사구체 = 모세혈관(단백질은 안 빠짐) → 재흡수·재분비<br>· 신기능 지표 = <b>BUN · 크레아티닌</b> · <b>이눌린</b> = 순수 여과율<br>· 클리어런스(배설률) ↔ 흡수의 생체이용률</div></div>
    </div>
  </div>
  <div class="callout memo"><div class="t">🧷 ADME 한 줄</div><div class="small"><b>PK = 시간에 따른 약의 변화</b> → 안전·효율적 치료의 전제(세포 수준만으로 개발 불가). 대부분 60 kg 서양 남성 기준 개발 → 성별·나이·인종·CYP450 차이 → <b>맞춤형 치료</b>(CAR-T 등). ADME를 <b>ABCD</b>로도 표현.</div></div>
</div>''', style=ST)
