# -*- coding: utf-8 -*-
from parts import *

F = "시험 직전"

cheat = dict(t="r", id="f-cheat", html=f"""
<div class="hd"><span class="bd">최종 정리 ①</span><div class="tt"><h1>시약 → 반응 → 생성물 치트키</h1><div class="sb">Reagent → reaction (24장)</div></div><span class="pt">{F}</span></div>
<div class="body"><div class="main full"><table class="t">
<tr><th>시약 / 조건</th><th>출발물</th><th>반응</th><th>생성물</th><th>개념</th></tr>
<tr><td>1. NaCN 2. LiAlH₄</td><td>R–X</td><td>S<sub>N</sub>2 → 니트릴 환원</td><td>R–CH₂NH₂ (+1 C)</td><td>{{CN:c-redsyn}}</td></tr>
<tr><td>1. SOCl₂ 2. NH₃ 3. LiAlH₄</td><td>RCOOH</td><td>아마이드 → 환원</td><td>RCH₂NH₂ (C 그대로)</td><td>{{CN:c-redsyn}}</td></tr>
<tr><td>HNO₃/H₂SO₄ → H₂/Pt 또는 SnCl₂, H₃O⁺; NaOH</td><td>벤젠</td><td>나이트로화 → 환원</td><td>ArNH₂</td><td>{{CN:c-redsyn}}</td></tr>
<tr><td>NH₃ + R–X</td><td>R–X</td><td>S<sub>N</sub>2 과알킬화</td><td>1·2·3·4차 혼합</td><td>{{CN:c-sn2}}</td></tr>
<tr><td>1. NaN₃ 2. LiAlH₄</td><td>1·2차 R–X</td><td>아자이드 → 환원 (−N₂)</td><td>1차 아민</td><td>{{CN:c-sn2}}</td></tr>
<tr><td>프탈이미드, KOH → R–X → NaOH, H₂O</td><td>1차 R–X</td><td>가브리엘</td><td>1차 아민 + 프탈산염</td><td>{{CN:c-sn2}}</td></tr>
<tr><td>NH₃ / RNH₂ / R₂NH + NaBH₄ (H₂/Ni)</td><td>알데하이드·케톤</td><td>환원성 아미노화 (이민)</td><td>1 / 2 / 3차 아민</td><td>{{CN:c-redam}}</td></tr>
<tr><td>Br₂, NaOH, H₂O</td><td>1차 아마이드</td><td>호프만 자리옮김</td><td>RNH₂ (−1 C, −CO₂)</td><td>{{CN:c-rearr}}</td></tr>
<tr><td>1. NaN₃ 2. H₂O, Δ</td><td>산 염화물</td><td>커티어스 자리옮김</td><td>RNH₂ (−1 C, −N₂, −CO₂)</td><td>{{CN:c-rearr}}</td></tr>
<tr><td>RCOCl, 피리딘</td><td>1·2차 아민</td><td>아실화</td><td>아마이드</td><td>{{CN:c-acyl}}</td></tr>
<tr><td>1. CH₃I 과량 2. Ag₂O, H₂O, Δ</td><td>아민</td><td>호프만 제거 (E2)</td><td>덜 치환된 알켄 + 3차 아민</td><td>{{CN:c-acyl}}</td></tr>
<tr><td>Ac₂O → EAS → NaOH</td><td>아닐린</td><td>보호 → 파라 치환 → 탈보호</td><td>p-치환 아닐린</td><td>{{CN:c-ear}}</td></tr>
<tr><td>NaNO₂(HNO₂), H₂SO₄, 0–5 °C</td><td>ArNH₂</td><td>다이아조화</td><td>ArN₂⁺</td><td>{{CN:c-diaz}}</td></tr>
<tr><td>CuCl / CuBr / CuCN / NaI / Cu₂O / H₃PO₂</td><td>ArN₂⁺</td><td>산드마이어 등</td><td>ArCl / ArBr / ArCN / ArI / ArOH / ArH</td><td>{{CN:c-diaz}}</td></tr>
<tr><td>페놀 · N,N-다이메틸아닐린</td><td>ArN₂⁺</td><td>아조 커플링 (파라)</td><td>Ar–N=N–Ar′</td><td>{{CN:c-azo}}</td></tr>
</table></div></div>""")

pairs = dict(t="r", id="f-pairs", html=f"""
<div class="hd"><span class="bd">최종 정리 ②</span><div class="tt"><h1>혼동 쌍 총정리 · 시험 직전 10줄</h1><div class="sb">Confusing pairs · last 10 lines</div></div><span class="pt">{F}</span></div>
<div class="body"><div class="main"><table class="t">
<tr><th>헷갈리는 쌍</th><th>왼쪽</th><th>오른쪽</th></tr>
<tr><td>짝산 pKa vs 염기 세기</td><td>pKa 큼</td><td>= 강한 염기</td></tr>
<tr><td>알킬아민 vs 아닐린</td><td>≈ 10.6 (강)</td><td>4.63 (공명으로 약)</td></tr>
<tr><td>피롤 vs 피리딘</td><td>N 전자쌍 방향족에 → 비염기, EAS C2</td><td>sp² 전자쌍 → 약염기, EAS C3</td></tr>
<tr><td>피리딘 vs Et₃N</td><td>sp² (약)</td><td>sp³ (강)</td></tr>
<tr><td>아자이드 합성 vs 커티어스</td><td>R–X + N₃⁻ → 환원, C 그대로</td><td>RCOCl + N₃⁻ → Δ, C 1개 ↓</td></tr>
<tr><td>니트릴 환원 vs 호프만</td><td>+1 C</td><td>−1 C</td></tr>
<tr><td>가브리엘 vs 환원성 아미노화</td><td>1차 아민만</td><td>1·2·3차 모두</td></tr>
<tr><td>호프만 자리옮김 vs 호프만 제거</td><td>아마이드 → 아민</td><td>아민 → 알켄</td></tr>
<tr><td>호프만 제거 vs 일반 E2</td><td>덜 치환된 알켄</td><td>더 치환된 (자이체프)</td></tr>
<tr><td>산드마이어 vs 아조 커플링</td><td>N₂ 잃고 치환</td><td>N₂ 유지 (N=N)</td></tr>
<tr><td>NaNO₂ vs NaNO₃</td><td>아질산염 — 다이아조화 ○</td><td>질산염 — ✗</td></tr>
<tr><td>파라 아닐린 vs 메타 아닐린</td><td>아세틸 보호 상태에서 치환</td><td>NO₂ 상태에서 치환 → 환원</td></tr>
</table></div><div class="side">
<div class="card tip"><div class="ct">🧠 시험 직전 10줄</div><ol style="margin:0;padding-left:1.2em">
<li>질소 전자쌍 = 염기·친핵체. 짝산 pKa 클수록 강한 염기.</li>
<li>아마이드·피롤·인돌 N은 비염기 (전자쌍을 공명에).</li>
<li>아닐린은 끄는 기 붙으면 더 약한 염기.</li>
<li>1차 아민 깨끗이 = 아자이드 또는 가브리엘.</li>
<li>C=O + 아민 + NaBH₄ = 환원성 아미노화.</li>
<li>호프만·커티어스 = R 이동 + CO₂ → C 1개 ↓.</li>
<li>호프만 제거 = CH₃I 과량 → Ag₂O, Δ → 말단 알켄.</li>
<li>ArNH₂ → NaNO₂ → ArN₂⁺ → Cu 시약으로 무엇이든.</li>
<li>아조 커플링은 파라, 색이 난다.</li>
<li>피롤 C2, 피리딘 C3, 인돌 C3.</li></ol></div>
<div class="card rec"><div class="ct">🎯 일정</div>기말 <b>12월 18일</b> · 25·26장까지 · 12월 첫째·둘째 주 문제 풀이 · 24장 과제 4문제 숙제.</div>
</div></div>""")

E = [cheat, pairs]
