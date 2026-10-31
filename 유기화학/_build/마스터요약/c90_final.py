# -*- coding: utf-8 -*-
from parts import *

F = "시험 직전"

reag = dict(t="r", id="f-reag", html=f"""
<div class="hd"><span class="bd">최종 정리 ①</span><div class="tt"><h1>시약 치트시트 — 시약을 보면 반응이 떠오르게</h1><div class="sb">Reagent → reaction</div></div><span class="pt">{F}</span></div>
<div class="body"><div class="main"><table class="t">
<tr><th>시약 / 조건</th><th>하는 일</th><th>결과</th><th>개념</th></tr>
<tr><td>Br₂ (Cl₂, I₂), CH₃COOH</td><td>산 촉매 엔올 → α-할로젠화</td><td>α-X 1개, 더 치환된 쪽</td><td>03</td></tr>
<tr><td>D₃O⁺ (D₂O, H⁺)</td><td>엔올 → α-D 교환</td><td>모든 α-H → D</td><td>04</td></tr>
<tr><td>피리딘, 가열</td><td>α-브로모 케톤의 E2</td><td>α,β-불포화 케톤</td><td>05</td></tr>
<tr><td>1. Br₂, PBr₃ 2. H₂O</td><td>HVZ</td><td>α-브로모 카복실산 (물 전: –COBr)</td><td>06</td></tr>
<tr><td>1. RMgX 2. H₃O⁺ (니트릴)</td><td>Grignard 첨가 + 이민 가수분해</td><td>케톤</td><td>07</td></tr>
<tr><td>아민 (t-BuNH₂ 등)</td><td>α-할로 케톤에 S<sub>N</sub>2</td><td>α-아미노 케톤</td><td>07</td></tr>
<tr><td>NaH / LDA, THF, −78 °C</td><td>완전한 엔올레이트</td><td>LDA: 덜 치환된 쪽</td><td>08·16</td></tr>
<tr><td>X₂, NaOH (과량)</td><td>염기 할로젠화 폭주 → 할로폼</td><td>RCOO⁻ + CHX₃ (I₂: 노란 침전)</td><td>10</td></tr>
<tr><td>1. NaOEt 2. R–X</td><td>1,3-다이카르보닐 알킬화 (S<sub>N</sub>2)</td><td>α-R (최대 2번)</td><td>11·12</td></tr>
<tr><td>2 NaOEt + Br(CH₂)ₙBr</td><td>분자 간 + 분자 내 알킬화</td><td>(n+1)원 고리</td><td>12</td></tr>
<tr><td>H₃O⁺, 가열</td><td>에스터 가수분해 + 탈카르복실화</td><td>말론산 → 산 / 아세토아세트산 → 메틸 케톤</td><td>13·14</td></tr>
<tr><td>NaOCH₃ (메틸 에스터)</td><td>에스터 교환 없이 엔올레이트</td><td>같은 알콕사이드 원칙</td><td>12 · 문제 18</td></tr>
<tr><td>옥살산 다이에틸, NaOEt → Δ</td><td>Claisen → −CO</td><td>페닐말론산 다이에틸</td><td>15</td></tr>
<tr><td>요소 H₂NCONH₂</td><td>다이에스터와 아실 치환 ×2</td><td>바르비튜르산 고리</td><td>15</td></tr>
<tr><td>1. LDA 2. CH₃I</td><td>단일 카르보닐 직접 알킬화</td><td>α-CH₃ (케톤·에스터·락톤·니트릴)</td><td>16</td></tr>
<tr><td>SAM (생체)</td><td>엔올이 S⁺–CH₃에 S<sub>N</sub>2</td><td>생체 α-메틸화</td><td>17</td></tr>
</table></div><div class="side">
<div class="card"><div class="ct">🔢 꼭 외울 pKa 사다리</div><table class="t">
<tr><td>CCl₃COOH</td><td>0.7</td></tr><tr><td>카복실산</td><td>5</td></tr><tr><td>1,3-다이케톤</td><td>9</td></tr><tr><td>페놀</td><td>10</td></tr><tr><td>β-케토 에스터</td><td>11</td></tr><tr><td>말론산 에스터</td><td>13</td></tr><tr><td>물 / 알코올</td><td>15.7 / 16</td></tr><tr><td>산염화물 α-H</td><td>16</td></tr><tr><td>알데하이드 α-H</td><td>17</td></tr><tr><td>케톤 α-H</td><td>19</td></tr><tr><td>싸이오에스터</td><td>21</td></tr><tr><td>에스터 · 니트릴</td><td>25</td></tr><tr><td>다이알킬아마이드</td><td>30</td></tr><tr><td>H₂ (NaH)</td><td>35</td></tr><tr><td>다이아이소프로필아민 (LDA)</td><td>36</td></tr></table></div>
</div></div>""")

pairs = dict(t="r", id="f-pairs", html=f"""
<div class="hd"><span class="bd">최종 정리 ②</span><div class="tt"><h1>혼동 쌍 총정리 · 시험 직전 10줄</h1><div class="sb">Confusing pairs · last 10 lines</div></div><span class="pt">{F}</span></div>
<div class="body"><div class="main"><table class="t">
<tr><th>헷갈리는 쌍</th><th>왼쪽</th><th>오른쪽</th></tr>
<tr><td>토토머 vs 공명</td><td>H가 이동 (⇌), 다른 화합물</td><td>전자만 이동 (↔)</td></tr>
<tr><td>산 vs 염기 엔올화</td><td>O 양성자화 → α-H 제거</td><td>α-H 제거 → O 양성자화</td></tr>
<tr><td>산 vs 염기 할로젠화</td><td>촉매, <b>1번</b>, 더 치환된 쪽</td><td>촉진, <b>여러 번</b> → 할로폼</td></tr>
<tr><td>산성 Br₂ vs LDA 알킬화</td><td>더 치환된 쪽 (열역학)</td><td>덜 치환된 쪽 (속도론)</td></tr>
<tr><td>HVZ 중간체 vs 최종</td><td>α-Br–<b>COBr</b> (물 전)</td><td>α-Br–<b>COOH</b> (물 후)</td></tr>
<tr><td>NaOEt vs NaOH</td><td>에스터에 안전 (같은 OR)</td><td>에스터 가수분해 ✗</td></tr>
<tr><td>NaOEt vs LDA</td><td>pKa ≤ 13 기질 (1,3-다이카르보닐)</td><td>단일 카르보닐(19–25) 완전 전환</td></tr>
<tr><td>말론산 vs 아세토아세트산</td><td>→ 카복실산</td><td>→ 메틸 케톤</td></tr>
<tr><td>β-케토산 vs γ-케토산</td><td>가열 → −CO₂</td><td>안 빠짐 (6원 고리 불가)</td></tr>
<tr><td>1° / 3° 할라이드</td><td>S<sub>N</sub>2 알킬화 ○</td><td>E2 알켄 ✗</td></tr>
<tr><td>알코올 vs 케톤 산성</td><td>에탄올 16 (더 산성)</td><td>아세톤 19</td></tr>
<tr><td>케톤 vs 니트릴 α-H</td><td>19 (O⁻가 음전하)</td><td>25 (N⁻, C=C=N⁻ 불편)</td></tr>
</table></div><div class="side">
<div class="card tip"><div class="ct">🧠 시험 직전 10줄</div><ol style="margin:0;padding-left:1.2em">
<li>엔올은 반응하려고 만든다 — α 탄소가 공격수.</li>
<li>산성 할로젠화 4단계, 한 번만, 붐비는 쪽.</li>
<li>속도식에 X₂ 없음 = 엔올화가 느린 단계.</li>
<li>케톤 → Br₂/AcOH → 피리딘/Δ = α,β-불포화 케톤.</li>
<li>HVZ = PBr₃로 –COBr → 엔올 → Br₂ → H₂O.</li>
<li>엔올레이트 100 % = NaH·LDA. 1,3-다이카르보닐은 NaOEt.</li>
<li>염기·X₂ 과량 + 메틸 케톤 = 할로폼(⁻CX₃ 이탈).</li>
<li>알킬화 = S<sub>N</sub>2: CH₃·1°·알릴·벤질만.</li>
<li>H₃O⁺, Δ = 가수분해 + 6원 고리 −CO₂ (β 필수).</li>
<li>LDA는 한산한 쪽, 막히면 거꾸로 풀기!</li></ol></div>
</div></div>""")

E = [reag, pairs]
