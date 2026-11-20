# -*- coding: utf-8 -*-
from parts import *

# 21장 정리본 표지 스타일: 왼쪽 그라데이션 판(큰 '23장') + 오른쪽 문항 목차 — 삼성노트 썸네일에서 장 번호가 크게 보이게
cover = dict(t="r", cls="cv21", html="""
<style>
.page.cv21{padding:0;flex-direction:row;}
.cv21 .lp{width:78mm;flex:none;height:100%;background:linear-gradient(170deg,#e64980 0%,#c2255c 38%,#862e5c 72%,#4a2347 100%);color:#fff;padding:15mm 9mm 12mm 10mm;display:flex;flex-direction:column;}
.cv21 .lp .k{letter-spacing:.32em;font-size:12px;font-weight:700;opacity:.92;}
.cv21 .lp .big{display:flex;align-items:flex-end;gap:4px;margin-top:4mm;line-height:.9;}
.cv21 .lp .big b{font-size:118px;font-weight:800;letter-spacing:-4px;}
.cv21 .lp .big span{font-size:36px;font-weight:800;margin-bottom:12px;}
.cv21 .lp h1{font-size:27px;line-height:1.3;margin:7mm 0 2px 0;font-weight:800;}
.cv21 .lp .en{font-size:12px;opacity:.85;}
.cv21 .lp .chips{margin-top:6mm;display:flex;flex-direction:column;gap:5px;font-size:11.5px;}
.cv21 .lp .chips span{background:rgba(255,255,255,.16);border:1px solid rgba(255,255,255,.3);border-radius:8px;padding:3px 9px;}
.cv21 .lp .stt{margin-top:auto;font-size:13px;line-height:1.75;}
.cv21 .lp .stt b{font-size:20px;font-weight:800;}
.cv21 .rp{flex:1;min-width:0;padding:11mm 11mm 12mm 9mm;display:flex;flex-direction:column;}
.cv21 .rh{display:flex;align-items:baseline;gap:10px;border-bottom:1px solid #dfe5ee;padding-bottom:5px;}
.cv21 .rh h2{margin:0;font-size:15px;color:#5f3dc4;}
.cv21 .rh span{font-size:10.5px;color:#6b7686;}
.cv21 .toc{flex:1;min-height:0;display:grid;grid-template-columns:1fr 1fr;column-gap:16px;margin-top:5px;grid-auto-flow:column;grid-template-rows:repeat(var(--rows),1fr);}
.cv21 .tr{display:flex;align-items:center;gap:7px;border-bottom:1px solid #eef1f5;font-size:11.3px;min-width:0;}
.cv21 .tr .bg{flex:none;width:30px;text-align:center;border-radius:8px;font-size:9.5px;font-weight:700;color:#fff;padding:1px 0;}
.cv21 .bg.c{background:#7048e8;} .cv21 .bg.w{background:#e64980;} .cv21 .bg.p{background:#74b816;} .cv21 .bg.v{background:#fab005;} .cv21 .bg.h{background:#f76707;} .cv21 .bg.l{background:#ae3ec9;}
.cv21 .tr .nm{flex:none;width:44px;font-weight:700;color:#5f3dc4;}
.cv21 .tr .ti{flex:1;min-width:0;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;color:#2c3038;}
.cv21 .tr .pg{flex:none;font-weight:700;color:#6b7686;width:24px;text-align:right;}
.cv21 .tr.part{border-bottom:none;font-weight:700;color:#e8590c;font-size:10.5px;letter-spacing:.04em;}
.cv21 .ft{left:auto;right:11mm;width:auto;border-top:none !important;}
.cv21 .ft span:not(:last-child){display:none;}
</style>
<div class="lp"><div class="k">CHAPTER</div>
<div class="big"><b>24</b><span>장</span></div>
<h1>아민과<br>헤테로고리</h1><div class="en">Amines and Heterocycles</div>
<div class="chips"><span>염기성 · 아릴아민 · 치환기 효과</span><span>아민 합성 · 가브리엘 · 호프만/커티어스</span><span>호프만 제거 · 다이아조늄 · 헤테로고리</span></div>
<div class="stt">개념 <b>{NC}</b> · 문제 <b>{NQ}</b><br>{TOCSTAT}<br>p.1–{TOTAL}</div></div>
<div class="rp"><div class="rh"><h2>목차</h2><span>🎯 = 교수님 녹취 강조 · 🔥 = 출제 예상 TOP</span></div>
<div class="toc">{TOC}</div></div>""")

MAPR = [
 RX(('m', 'CCCCBr', 55, 35), ('a', 'NaN₃', '또는 프탈이미드⁻'), ('m', 'CCCCN=[N+]=[N-]', 80, 35), ('a', 'LiAlH₄', '(가브리엘: NaOH)'), ('m', 'CCCCN', 55, 35), ('t', '1차 아민 · '),
    ('m', 'CC(=O)Cc1ccccc1', 75, 45), ('a', 'NH₃, NaBH₄', '환원성 아미노화'), ('m', 'CC(N)Cc1ccccc1', 75, 45)),
 RX(('m', 'NC(=O)c1ccccc1', 65, 45), ('a', 'Br₂, NaOH', '호프만 (−CO₂)'), ('m', 'Nc1ccccc1', 50, 40), ('t', '탄소 1개 ↓ · '),
    ('m', 'O=C(Cl)c1ccccc1', 65, 45), ('a', 'NaN₃; Δ, H₂O', '커티어스 (−N₂, −CO₂)'), ('m', 'Nc1ccccc1', 50, 40)),
 RX(('m', 'CCCCC(C)N', 70, 40), ('a', '1. CH₃I 과량', '2. Ag₂O, Δ'), ('m', 'C=CCCCC', 65, 35), ('t', '호프만 제거 (덜 치환된 알켄) · '),
    ('m', 'Cc1ccc(N)cc1', 55, 40), ('a', 'NaNO₂, H₂SO₄', '0–5 °C'), ('m', 'Cc1ccc([N+]#N)cc1', 70, 40), ('a', 'CuBr · CuCN · NaI', 'Cu₂O · H₃PO₂'), ('t', 'Ar–Br · CN · I · OH · H')),
 RX(('m', '[N+](#N)c1ccccc1', 60, 40), ('t', '+'), ('m', 'Oc1ccccc1', 50, 40), ('a', '아조 커플링', '파라'), ('m', 'Oc1ccc(/N=N/c2ccccc2)cc1', 110, 45), ('t', ' · 피롤 C2 · 피리딘 C3 · '),
    ('m', 'c1cc[nH]c1', 40, 35), ('m', 'c1ccncc1', 40, 35)),
]
MAP = ''.join(MAPR)

mp = dict(t="r", id="f-map", html=f"""
<div class="hd"><span class="bd">24장</span><div class="tt"><h1>24장 한 장 지도 — 질소의 전자쌍이 모든 것</h1><div class="sb">Reaction map · 염기성 / 합성 / 반응 / 헤테로고리</div></div><span class="pt">{P0}</span></div>
<div class="main full" style="flex:none;margin-top:8px">
<div class="sec">🗺 반응 지도 — 아민 만들기 → 아민 바꾸기 → 고리 속 질소</div>
<div class="mz">{MAP}</div></div>
<div class="body"><div class="main">
<table class="t"><tr><th>주제</th><th>핵심</th><th>개념</th></tr>
<tr><td>염기성</td><td>짝산 pKa 큼 = 강한 염기 · 알킬아민 ≈ 11 &gt; NH₃ 9 &gt; 피리딘·아닐린 5 &gt; 피롤 0.4 · 아마이드 비염기</td><td>{{CN:c-base}}–{{CN:c-aryl}}</td></tr>
<tr><td>합성</td><td>환원(니트릴·아마이드·NO₂) · S<sub>N</sub>2(과알킬화) · 아자이드 · 가브리엘 · 환원성 아미노화 · 호프만/커티어스</td><td>{{CN:c-redsyn}}–{{CN:c-rearr}}</td></tr>
<tr><td>반응</td><td>아실화 · 호프만 제거 · 아릴아민 EAS(보호) · 다이아조늄(산드마이어·커플링)</td><td>{{CN:c-acyl}}–{{CN:c-azo}}</td></tr>
<tr><td>헤테로고리</td><td>피롤(N 전자쌍 방향족, C2) · 이미다졸 · 피리딘(sp² N, C3) · 융합 고리</td><td>{{CN:c-pyrrole}}–{{CN:c-fused}}</td></tr></table>
</div><div class="side">
<div class="card tip"><div class="ct">📌 문제 읽는 법 — 시약으로 반응 찾기</div>
<ul style="margin:0;padding-left:1.2em"><li><b>NaN₃ → LiAlH₄</b> / <b>프탈이미드 → NaOH</b> = 1차 아민 (탄소 그대로)</li>
<li><b>Br₂, NaOH</b> (아마이드) / <b>NaN₃, Δ</b> (산 염화물) = 아민, <b>탄소 1개 ↓</b></li>
<li><b>C=O + 아민 + NaBH₄</b> = 환원성 아미노화</li>
<li><b>CH₃I 과량 → Ag₂O, Δ</b> = 호프만 제거</li>
<li><b>NaNO₂(HNO₂), H₂SO₄</b> → 다이아조늄 → Cu 시약</li></ul></div>
<div class="card rec"><div class="ct">🎯 녹취 — 교수님 말씀</div>“가브리엘의 목적은 <b>질소 도입</b>” · “호프만·커티어스 공통점 = <b>자리바꿈 + CO₂</b>” · “호프만 제거는 결국 <b>E2</b>” · “피롤은 <b>C2</b>, 피리딘은 <b>C3</b> — 요 정도만” · <b>기말 12월 18일</b>.</div>
</div></div>""")

E = [cover, mp]
