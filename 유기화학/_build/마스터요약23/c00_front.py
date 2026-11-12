# -*- coding: utf-8 -*-
from parts import *

# 21장 정리본 표지 스타일: 왼쪽 그라데이션 판(큰 '23장') + 오른쪽 문항 목차 — 삼성노트 썸네일에서 장 번호가 크게 보이게
cover = dict(t="r", cls="cv21", html="""
<style>
.page.cv21{padding:0;flex-direction:row;}
.cv21 .lp{width:78mm;flex:none;height:100%;background:#f76707;color:#fff;padding:15mm 9mm 12mm 10mm;display:flex;flex-direction:column;}
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
<div class="big"><b>23</b><span>장</span></div>
<h1>카르보닐<br>축합 반응</h1><div class="en">Carbonyl Condensation Reactions</div>
<div class="chips"><span>알돌 · E1cB 탈수 · 혼합/분자 내 알돌</span><span>클라이젠 · 디크만</span><span>마이클 · 스토크 엔아민 · 로빈슨</span></div>
<div class="stt">개념 <b>{NC}</b> · 문제 <b>{NQ}</b><br>{TOCSTAT}<br>p.1–{TOTAL}</div></div>
<div class="rp"><div class="rh"><h2>목차</h2><span>🎯 = 교수님 녹취 강조 · 🔥 = 출제 예상 TOP</span></div>
<div class="toc">{TOC}</div></div>""")

MAPR = [
 RX(('m', 'CC=O', 45, 40), ('a', 'NaOH (촉매)', '알돌'), ('m', 'CC(O)CC=O', 75, 50), ('a', 'Δ, −H₂O', 'E1cB'), ('m', 'C/C=C/C=O', 70, 45), ('t', '알돌 축합 · '),
    ('m', 'CC(=O)CCC(C)=O', 90, 45), ('a', 'NaOH', '분자 내'), ('m', 'CC1=CC(=O)CC1', 60, 55), ('t', '5원 엔온')),
 RX(('m', 'O=Cc1ccccc1', 65, 50), ('t', '+'), ('m', 'CC(C)=O', 45, 40), ('a', 'NaOH', '혼합 알돌'), ('m', 'CC(=O)/C=C/c1ccccc1', 100, 50), ('t', 'α-H 없는 받개 · '),
    ('m', 'CCOC(C)=O', 55, 40), ('a', '1. NaOEt', '2. H₃O⁺'), ('m', 'CCOC(=O)CC(C)=O', 90, 45), ('t', '클라이젠')),
 RX(('m', 'CCOC(=O)CCCCC(=O)OCC', 120, 40), ('a', '1. NaOEt', '2. H₃O⁺'), ('m', 'CCOC(=O)C1CCCC1=O', 75, 55), ('t', '디크만 (1,6 → 5원) · '),
    ('m', 'CCOC(=O)CC(C)=O', 80, 45), ('t', '+'), ('m', 'C=CC(C)=O', 50, 40), ('a', 'NaOEt', '마이클'), ('m', 'CCOC(=O)C(CCC(C)=O)C(C)=O', 100, 60), ('t', '1,5')),
 RX(('m', 'O=C1CCCCC1', 50, 45), ('a', '피롤리딘', ''), ('m', 'C1=C(N2CCCC2)CCCC1', 75, 55), ('a', '1. MVK', '2. H₃O⁺'), ('m', 'CC(=O)CCC1CCCCC1=O', 90, 55), ('t', '스토크 · '),
    ('m', 'CC1C(=O)CCC1=O', 60, 50), ('a', '1. MVK, 염기', '2. 알돌·Δ'), ('m', 'CC12CCC(=O)C=C1CCC2=O', 80, 60), ('t', '로빈슨')),
]
MAP = ''.join(MAPR)

mp = dict(t="r", id="f-map", html=f"""
<div class="hd"><span class="bd">23장</span><div class="tt"><h1>23장 한 장 지도 — 엔올레이트가 무엇을 치느냐</h1><div class="sb">Reaction map · 알돌 / 클라이젠 / 마이클 한 줄 요약</div></div><span class="pt">{P0}</span></div>
<div class="main full" style="flex:none;margin-top:8px">
<div class="sec">🗺 반응 지도 — 친핵체(엔올레이트·엔아민) + 친전자체(카르보닐 C=O 또는 β 탄소)</div>
<div class="mz">{MAP}</div></div>
<div class="body"><div class="main">
<table class="t"><tr><th>반응</th><th>친핵체 → 친전자체</th><th>생성물 패턴</th><th>개념</th></tr>
<tr><td>알돌 / 축합</td><td>알데하이드·케톤 엔올레이트 → C=O</td><td>β-하이드록시 카르보닐 → 엔온</td><td>{{CN:c-aldol}}–{{CN:c-intra}}</td></tr>
<tr><td>클라이젠 / 디크만</td><td>에스터 엔올레이트 → 에스터 C=O (–OEt 이탈)</td><td>β-케토 에스터 (1,3)</td><td>{{CN:c-claisen}}–{{CN:c-dieck}}</td></tr>
<tr><td>마이클 / 스토크</td><td>안정한 엔올레이트·엔아민 → <b>β 탄소</b></td><td>1,5-다이카르보닐</td><td>{{CN:c-michael}}·{{CN:c-stork}}</td></tr>
<tr><td>로빈슨</td><td>마이클 + 분자 내 알돌</td><td>2-사이클로헥센온 (새 6원 고리)</td><td>{{CN:c-robinson}}</td></tr></table>
</div><div class="side">
<div class="card tip"><div class="ct">📌 문제 읽는 법 — 산소 위치로 반응 찾기</div>
<ul style="margin:0;padding-left:1.2em"><li><b>O가 1,3</b> (C=O와 β-OH) → 알돌 / C=O와 C=O → 클라이젠</li>
<li><b>C=C–C=O</b> (엔온) → 알돌 축합 (Cα=Cβ 끊기)</li>
<li><b>C=O가 1,5</b> → 마이클 · 스토크</li>
<li><b>고리 엔온</b> → 분자 내 알돌 / 로빈슨</li>
<li><b>고리 β-케토 에스터</b> → 디크만</li></ul></div>
<div class="card rec"><div class="ct">🎯 녹취 — 교수님 말씀</div>“23장은 꽤 어려운 챕터라 2주에 걸쳐” · “클라이젠은 <b>이름만 새로 나왔을 뿐 원리는 알돌과 똑같습니다</b>” · “디크만은 클라이젠과 완전히 똑같고” · “로빈슨은 새 반응이 아니라 <b>마이클 + 분자 내 알돌</b>” · “과제는 다음 시간에 내도록 하겠습니다.”</div>
<div class="card"><div class="ct">🔢 꼭 쓰는 pKa</div>1,3-다이케톤 9 · β-케토 에스터 11 · 말론산 다이에틸 13 · 물·EtOH 16 · 케톤 19 · 에스터 25</div>
</div></div>""")

E = [cover, mp]
