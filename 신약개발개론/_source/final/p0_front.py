# 표지 + 00 기말 시험 전략
from lib import page, ph

# 기말 범위 주차 진행: (번호, 라벨, 상태) 상태 = on(완료) / off(휴강·시험) / next(예정)
WEEKS = [(9, '11/4', 'on'), (10, '휴강', 'off'), (11, '11/11', 'on'), (12, '11/18', 'on'),
         (13, '휴강·녹화', 'next'), (14, '', 'next'), (15, '', 'next')]


def add_cover():
    wk = ''.join(f'<div class="w"><div class="d {s}">{n}</div>{l or "주"}</div>' for n, l, s in WEEKS)
    page(f'''<div class="in">
  <div class="kicker">PHAR278 · 신약개발개론 · 시험대비 노트</div>
  <h1>기말고사<br>통합 상세요약<br><span class="v">+ 문제</span></h1>
  <div class="rng">9 · 11 · 12주차 (10주차 휴강) — 매주 이어 붙이는 통합본</div>
  <div class="chips"><span>시험 전략</span><span>Hit → Lead → 후보</span><span>PD · PK(ADME)</span><span>전임상 · GLP</span><span>개념문제</span><span>실전문제</span><span>헷갈리는 쌍</span></div>
  <div class="desc">요약정리·녹취록으로 공부한 뒤 <span class="hl">개념 확인 → 실전</span> 순서로 쓰는 노트야.<br>
  중간고사처럼 <b>“두 개념을 맞바꾼 보기”</b>를 잡는 데 집중했고, 수업에서 교수님이 <b>“예시 문제로 내기 좋다”</b>고 한 부분엔 분홍 태그를 달았어.</div>
  <div class="toc"><h4>CONTENTS</h4><ol>
    <li><span class="b">00</span>기말 시험 전략 · 출제 힌트<em>{{00}}</em></li>
    <li><span class="b">01</span>Ch 3-2 후반: Hit → Lead → AI<em>{{01}}</em></li>
    <li><span class="b">02</span>Ch 4 후보물질 선정 · PD · PK<em>{{02}}</em></li>
    <li><span class="b">03</span>Ch 5 전임상연구 · GLP<em>{{03}}</em></li>
    <li><span class="b o">★</span>기말 대비 실전문제<em>{{ex}}</em></li>
    <li><span class="b o">✓</span>헷갈리는 쌍 · 암기카드<em>{{ck}}</em></li>
  </ol></div>
  <div class="wk"><div class="lb">기말 범위 진행 (회색 = 휴강 · 점선 = 예정)</div><div class="tr">{wk}</div></div>
  <div class="foot">김한준 교수님 9·11·12주차 강의 슬라이드 + 수업 녹취록 + 주차별 요약정리를 바탕으로 정리</div>
</div>''', cls='page lcover')


def add_strategy():
    page(ph('기말', '00', '기말 시험 전략 — 형식 · 출제 패턴 · 교수님 힌트', '시험기록 · 9·11·12주차 녹취') + '''
<div class="body col">
  <div class="row">
    <div class="col" style="flex:1">
      <table class="t">
        <tr><th>항목</th><th>내용</th></tr>
        <tr><td><b>비중</b></td><td>기말 <b>45%</b> (중간 40%)</td></tr>
        <tr><td><b>중간 형식</b></td><td>객관식 26 + 단답 14 = 40문항, <b>서술 없음</b></td></tr>
        <tr><td><b>중간 결과</b></td><td>평균 27.3/40 · 최고 38 · <b>B컷 ≈ 25</b></td></tr>
        <tr><td><b>기말 난이도</b></td><td>교수님: 중간보다 <b>조금 쉽게</b> (F 안 나오게)</td></tr>
        <tr><td><b>범위</b></td><td>9주차(Virtual screening~)부터 · 13주차 휴강은 <b>전임상 녹화 강의</b>로 보강 · 대면 약 2번 남음</td></tr>
      </table>
      <div class="callout memo"><div class="t">📅 이 노트 쓰는 법</div><div class="small">요약정리·녹취록으로 먼저 공부 → 각 PART <b>상세요약</b>으로 정리 → <b>개념문제</b>로 확인 → 마지막 <b>실전문제</b>는 정답 칸 가리고 시간 재서</div></div>
    </div>
    <div class="card" style="flex:1.3;border-color:#f6c7bb"><h3 style="color:var(--coral)">🎯 중간고사 출제 패턴 → 기말에도</h3>
      <table class="t" style="--pcs:var(--coral-s)">
        <tr><th>패턴</th><th>중간 실제 사례 → 기말 예상</th></tr>
        <tr><td><b>① 두 개념 맞바꾸기</b></td><td>엔브렐↔스티렌 · 서방정↔장용정 · 화학상↔물리학상<br>→ <b>Efficacy↔Potency</b> · <b>Phase I↔II</b> · <b>탐색적↔규제적</b></td></tr>
        <tr><td><b>② 한 단어 뒤집기</b></td><td>광유전학 “억제” → <b>흥분</b><br>→ 내성 시 EC50 “감소” → <b>증가</b> · F “IV&lt;1” → <b>IV=1</b></td></tr>
        <tr><td><b>③ 단답 = 정확한 단어</b></td><td>NDA = <b>Application</b>(Approval ✗) · ‘녹차’ ✗ 시네카테킨<br>→ <b>QAU · GLP · BUN · CYP450</b> 풀네임</td></tr>
        <tr><td><b>④ 순서·숫자</b></td><td>생동성: 채혈 → 통계 → <b>판정</b><br>→ Hit μM → Lead 수백 nM → 후보 ≤100 nM · 경구 <b>A-M-D-E</b></td></tr>
      </table></div>
  </div>
  <div class="callout trap" style="border-color:#f5b6cb;background:#fff1f5"><div class="t" style="color:#c2185b">📣 교수님이 직접 짚은 출제 후보</div><div class="small">
    <b>12주차</b> “요런 그래프들 제가 굉장히 좋아한다 … 약물 내성, 항암제 … <b>예시 문제로 내기에 굉장히 좋은 주제</b>” → <span class="p">potency/efficacy 그래프 해석 · 내성 시 EC50·Emax</span><br>
    <b>11주차</b> “그래프에 A, B, C, D … ‘포텐시가 가장 높은 약물’, ‘포텐시 높고 에피커시 낮은 약물을 고르시오’ 이런 식으로 시험 문제가 나갈 수 있다”
  </div></div>
</div>''', style='--pc:var(--navy);--pcs:#efeaff')
