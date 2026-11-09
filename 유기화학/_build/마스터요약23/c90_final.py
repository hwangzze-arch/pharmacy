# -*- coding: utf-8 -*-
from parts import *

F = "시험 직전"

cheat = dict(t="r", id="f-cheat", html=f"""
<div class="hd"><span class="bd">최종 정리 ①</span><div class="tt"><h1>반응물 · 시약 · 생성물 연결 치트키</h1><div class="sb">Reactant → reagent → product (23장 6대 반응)</div></div><span class="pt">{F}</span></div>
<div class="body"><div class="main full"><table class="t">
<tr><th>반응</th><th>반응물 (주개 + 받개)</th><th>시약 / 조건</th><th>핵심 단계</th><th>생성물</th><th>개념</th></tr>
<tr><td><b>알돌</b></td><td>α-H 있는 알데하이드·케톤 ×2</td><td>NaOH·NaOEt <b>촉매량</b></td><td>엔올레이트 → C=O 첨가 → H⁺</td><td>β-하이드록시 카르보닐</td><td>{{CN:c-aldol}}</td></tr>
<tr><td><b>알돌 축합</b></td><td>알돌 생성물</td><td>H⁺ 또는 OH⁻, <b>가열</b></td><td>염기: <b>E1cB</b> / 산: –OH₂⁺ 이탈</td><td>α,β-불포화 카르보닐 (엔온)</td><td>{{CN:c-dehyd}}</td></tr>
<tr><td><b>혼합 알돌</b></td><td>α-H 없는 받개(PhCHO·HCHO) + 주개 / 1,3-다이카르보닐 주개</td><td>NaOH, 가열</td><td>주개만 엔올레이트</td><td>엔온 한 가지</td><td>{{CN:c-mixed}}</td></tr>
<tr><td><b>분자 내 알돌</b></td><td>1,4-다이케톤 / 1,5-다이케톤</td><td>NaOH, 가열</td><td>5·6원 고리만 (가역)</td><td>사이클로펜텐온 / 사이클로헥센온</td><td>{{CN:c-intra}}</td></tr>
<tr><td><b>클라이젠</b></td><td>α-H 2개 이상 에스터 ×2</td><td>NaOEt <b>1당량</b> → H₃O⁺</td><td>첨가 → <b>–OEt 이탈</b> → 산성 H 제거</td><td>β-케토 에스터</td><td>{{CN:c-claisen}}</td></tr>
<tr><td><b>혼합 클라이젠</b></td><td>α-H 없는 에스터(폼에이트·벤조에이트·옥살레이트) + 에스터/케톤</td><td>NaH·NaOEt → H₃O⁺</td><td>케톤이 주개 (19 &lt; 25)</td><td>β-케토 에스터 / β-다이케톤</td><td>{{CN:c-mixcl}}</td></tr>
<tr><td><b>디크만</b></td><td>1,6-다이에스터 / 1,7-다이에스터</td><td>NaOEt → H₃O⁺</td><td>분자 내 클라이젠</td><td>5원 / 6원 고리 β-케토 에스터</td><td>{{CN:c-dieck}}</td></tr>
<tr><td><b>+ 알킬화</b></td><td>고리 β-케토 에스터 + R–X</td><td>1. NaOEt 2. R–X 3. H₃O⁺, Δ</td><td>S<sub>N</sub>2 → 가수분해 → −CO₂</td><td>2-알킬 사이클로알칸온</td><td>{{CN:c-dieck}}</td></tr>
<tr><td><b>마이클</b></td><td>β-다이카르보닐 주개 + α,β-불포화 받개</td><td>NaOEt (촉매)</td><td><b>β 탄소</b>에 1,4-첨가</td><td>1,5-다이카르보닐</td><td>{{CN:c-michael}}</td></tr>
<tr><td><b>스토크</b></td><td>케톤 + <b>2차 아민</b>(피롤리딘) + 받개</td><td>① −H₂O ② 받개 ③ <b>H₃O⁺</b></td><td>엔아민 → 마이클 → 가수분해</td><td>1,5-다이카르보닐</td><td>{{CN:c-stork}}</td></tr>
<tr><td><b>로빈슨</b></td><td>β-다이케톤(β-케토 에스터·엔아민) + 메틸 바이닐 케톤</td><td>염기, 가열</td><td>마이클 → 분자 내 알돌 → 탈수</td><td>새 6원 고리 엔온</td><td>{{CN:c-robinson}}</td></tr>
</table>
<div class="cols" style="margin-top:6px"><div class="card tip"><div class="ct">🔁 거꾸로 풀기 (역합성) 공식</div>
엔온 → <b>Cα=Cβ</b> 끊고 β를 C=O로 · β-케토 에스터 → <b>Cα–C(=O)</b> 끊고 C=O에 –OEt · 1,5-다이카르보닐 → <b>Cα(주개)–Cβ(받개)</b> 끊고 받개에 C=C · 사이클로헥센온 → C=C 끊기 → 1,5-다이케톤 → 다시 끊기.</div>
<div class="card trap"><div class="ct">⚠️ 염기 고르기</div>에틸 에스터 = <b>NaOEt</b>, 메틸 에스터 = <b>NaOCH₃</b> (에스터 교환 방지) · NaOH는 에스터 비누화 · LDA 1당량은 축합이 아니라 α-알킬화(22장).</div></div>
</div></div>""")

pairs = dict(t="r", id="f-pairs", html=f"""
<div class="hd"><span class="bd">최종 정리 ②</span><div class="tt"><h1>혼동 쌍 총정리 · 시험 직전 10줄</h1><div class="sb">Confusing pairs · last 10 lines</div></div><span class="pt">{F}</span></div>
<div class="body"><div class="main"><table class="t">
<tr><th>헷갈리는 쌍</th><th>왼쪽</th><th>오른쪽</th></tr>
<tr><td>α-치환 vs 축합</td><td>LDA 1당량, −78 °C → R–X</td><td>염기 촉매량 → 남은 C=O</td></tr>
<tr><td>알돌 vs 클라이젠</td><td>–OH 남음 (β-하이드록시)</td><td>–OEt 이탈 (β-케토 에스터)</td></tr>
<tr><td>염기 촉매량 vs 1당량</td><td>알돌 (촉매)</td><td>클라이젠·디크만 (생성물이 염기 소모)</td></tr>
<tr><td>E2 vs E1cB</td><td>좋은 이탈기(–Br), 한 번에</td><td>나쁜 이탈기(–OH), 엔올레이트 먼저</td></tr>
<tr><td>산 탈수 vs 염기 탈수</td><td>–OH₂⁺로 H₂O 이탈 (엔올 경유)</td><td>E1cB (엔올레이트 경유)</td></tr>
<tr><td>1,2-첨가 vs 1,4-첨가</td><td>C=O 탄소 (알돌)</td><td>β 탄소 (마이클)</td></tr>
<tr><td>1차 vs 2차 아민</td><td>이민 (C=N)</td><td>엔아민 (C=C–N)</td></tr>
<tr><td>알돌 vs 디크만 고리</td><td>1,4-다이온 → 5원, 1,5-다이온 → 6원</td><td>1,6-다이에스터 → 5원, 1,7 → 6원</td></tr>
<tr><td>마이클 vs 로빈슨</td><td>1,5-다이카르보닐에서 멈춤</td><td>+ 분자 내 알돌 → 사이클로헥센온</td></tr>
<tr><td>혼합 알돌 ○ vs ✗</td><td>한쪽 α-H 없음 / 한쪽 훨씬 산성</td><td>둘 다 α-H → 4가지 혼합물</td></tr>
</table></div><div class="side">
<div class="card tip"><div class="ct">🧠 시험 직전 10줄</div><ol style="margin:0;padding-left:1.2em">
<li>엔올레이트(친핵체) + 카르보닐(친전자체) = 23장 전부.</li>
<li>알돌 = α 탄소 – C=O 탄소 연결, O는 –OH (β).</li>
<li>가열하면 엔온. 염기 탈수는 <b>E1cB</b>로 그린다.</li>
<li>혼합 알돌은 PhCHO·HCHO 같은 α-H 없는 받개.</li>
<li>분자 내 알돌·디크만은 5·6원 고리만 — 번호 매기기.</li>
<li>클라이젠 = 알돌 + –OEt 이탈, 염기 1당량.</li>
<li>케톤 + 에스터면 케톤이 주개 → β-다이케톤.</li>
<li>마이클 = β 탄소, 1,5-다이카르보닐.</li>
<li>스토크 = 2차 아민 → 엔아민 → 마이클 → H₃O⁺.</li>
<li>로빈슨 = 마이클 + 분자 내 알돌 → 6원 엔온.</li></ol></div>
<div class="card rec"><div class="ct">🎯 다음 시간</div>“다음 시간에 23장 문제 풀이를 같이 하면서 마무리하고 24장으로” — <b>과제가 공지되면</b> 이 노트에 추가.</div>
</div></div>""")

E = [cheat, pairs]
