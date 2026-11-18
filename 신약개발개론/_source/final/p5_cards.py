# ✓ 헷갈리는 쌍 + 암기카드
from lib import page, ph


def add():
    page(ph('기말', '✓ 헷갈리는 쌍', '맞바꾸기 주의 — TOP 10', '') + '''
<div class="body">
  <table class="t" style="--pcs:#efeaff">
    <tr><th style="width:26%">쌍</th><th>맞는 것</th><th>뒤집으면 오답</th></tr>
    <tr><td><b>Efficacy ↔ Potency</b></td><td>효능=Emax(Y축) / 역가=EC50(X축)</td><td>“EC50 높을수록 역가↑” ✗</td></tr>
    <tr><td><b>내성 시 EC50</b></td><td>수치 <b>증가</b>(역가↓, 곡선 오른쪽)</td><td>“EC50 감소” ✗</td></tr>
    <tr><td><b>생체이용률 F</b></td><td>IV=1, 경구<1</td><td>“경구=1, IV<1” ✗</td></tr>
    <tr><td><b>경구 ↔ 주사 ADME</b></td><td>경구 A-M-D-E / 주사 A-D-M-E</td><td>순서 바꾸기 ✗</td></tr>
    <tr><td><b>Phase I ↔ II</b></td><td>I=산화·환원·가수분해(CYP) / II=포합</td><td>“I=포합” ✗</td></tr>
    <tr><td><b>탐색적 ↔ 규제적</b></td><td>탐색적=후보 전(GLP 불필요) / 규제적=후보 후(GLP 필수)</td><td>GLP 적용 뒤집기 ✗</td></tr>
    <tr><td><b>처방 농도</b></td><td>효과 80~90% 목표</td><td>“Emax로 처방” ✗</td></tr>
    <tr><td><b>이눌린</b></td><td>재흡수·재분비 없음 → 순수 여과율</td><td>“배설률 높음” ✗</td></tr>
    <tr><td><b>쥐 vs 침팬지</b></td><td>유사성 침팬지 99%>쥐 81%(쥐는 실용성)</td><td>“쥐가 더 유사” ✗</td></tr>
    <tr><td><b>QAU</b></td><td>시험팀과 독립된 제3자 점검</td><td>“시험팀이 겸함” ✗</td></tr>
  </table>
</div>''', style='--pc:#5b3fd1;--pcs:#efeaff')

    page(ph('기말', '✓ 암기카드', '시험 직전 5분', '') + '''
<div class="body grid3">
  <div class="card"><h3 style="font-size:11pt">🎯 Hit → Lead → 후보</h3>
  <div class="small">농도 <b>μM → 수백 nM → ≤100 nM</b><br>선택성 후보 <b>~1,000배</b><br>Lead 최적화 = 구조 바꾸는 마지막 단계<br>HTS=범용 / FBDD=효율<br>바이오: 과정 동일, 기술만 다름</div></div>
  <div class="card"><h3 style="font-size:11pt">💊 PD</h3>
  <div class="small"><b>Emax</b>=효능(Y) / <b>EC50</b>=역가(X, 낮을수록↑)<br>TD50=독성 / LD50=사망 / <b>TI=TD50/ED50</b><br>역가 F>M>A, 효능 F=M>A<br>처방 80~90% · 내성 → EC50↑</div></div>
  <div class="card"><h3 style="font-size:11pt">🧪 PK (ADME)</h3>
  <div class="small"><b>F</b>: IV=1, 경구<1 · AUC=흡수량<br>경구 A-M-D-E / 주사 A-D-M-E<br>대사=간 · Phase I(CYP) / II(포합)<br>배설=신장 · BUN·Cr · 이눌린=여과율<br>장벽 3곳: 뇌·눈·정소/난소</div></div>
  <div class="card"><h3 style="font-size:11pt">🐭 전임상</h3>
  <div class="small">유효성+안전성(독성) 검증<br>침팬지 99%>쥐 81%(쥐=실용성)<br>탐색적(후보 전)=Discovery<br>규제적(후보 후)=Development·GLP</div></div>
  <div class="card"><h3 style="font-size:11pt">📋 GLP</h3>
  <div class="small">= 비임상시험 관리기준<br>계기 <b>탈리도마이드</b>, 통합 <b>1981 OECD</b><br>흐름: 개시→준비→실시→Data→종료→보관<br><b>QAU</b> = 독립 제3자 점검</div></div>
  <div class="card" style="border-color:#f5b6cb;background:#fff6f9"><h3 style="font-size:11pt;color:#c2185b">⚠ 출제 1순위</h3>
  <div class="small">potency/efficacy <b>그래프 해석</b><br>A·B·C·D 중 “역가 최고/효능 낮은 약”<br>약물 내성 시 EC50·Emax 변화<br>(교수님: “예시 문제로 내기 좋은 주제”)</div></div>
</div>''', style='--pc:#5b3fd1;--pcs:#efeaff')
