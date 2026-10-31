# -*- coding: utf-8 -*-
from parts import *

cover = dict(t="r", cls="cover2", html=f"""
<style>
.cover2{{background:radial-gradient(ellipse at 0% 0%,#ffd8d8 0%,rgba(255,216,216,0) 45%),radial-gradient(ellipse at 100% 0%,#ffe0ec 0%,rgba(255,224,236,0) 50%),radial-gradient(ellipse at 100% 100%,#ffe8cc 0%,rgba(255,232,204,0) 50%),#fff5f5 !important;}}
.cv-k{{letter-spacing:.32em;font-size:11px;font-weight:700;color:#c92a2a;margin-top:6mm;}}
.cv-h{{font-size:38px;line-height:1.2;font-weight:800;margin:10px 0 12px 0;color:#8a1c1c;}}
.cv-flow{{font-size:15px;color:#2c3038;margin-bottom:12px;}}
.cv-chips{{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:12px;}}
.cv-chip{{background:#fff;border:1px solid #f5c2c2;border-radius:16px;padding:4px 13px;font-size:11.5px;font-weight:700;color:#2c3038;}}
.cv-txt{{font-size:12.2px;line-height:1.75;color:#3a3f4b;}}
.cv-txt .r{{color:#d6336c;font-weight:700;}}
.cv-toc{{position:absolute;right:13mm;top:12mm;width:108mm;background:rgba(255,255,255,.88);border:1px solid #f3c7c7;border-radius:14px;padding:12px 18px 8px 18px;box-shadow:0 4px 18px rgba(160,30,30,.12);}}
.cv-toc .t{{letter-spacing:.25em;font-size:10px;font-weight:700;color:#c92a2a;margin-bottom:4px;}}
.cv-toc .row{{display:flex;align-items:baseline;gap:12px;border-bottom:1px solid #fbe3e3;padding:5px 0;font-size:11.8px;}}
.cv-toc .row:last-child{{border-bottom:none;}}
.cv-toc .n{{width:20px;color:#c92a2a;font-weight:700;}}
.cv-toc .nm{{flex:1;font-weight:700;color:#2c3038;}} .cv-toc .nm span{{font-weight:400;color:#8b8fa0;font-size:.9em;margin-left:4px;}}
.cv-toc .pg{{color:#8b8fa0;}}
.cv-left{{width:160mm;}}
.cv-stats{{display:flex;gap:9px;margin-top:20px;}}
.cv-st{{background:rgba(255,255,255,.8);border:1px solid #f3c7c7;border-radius:14px;padding:10px 14px;display:flex;align-items:center;gap:10px;flex:1;}}
.cv-st b{{font-size:24px;font-weight:800;color:#c92a2a;border-top:1px solid #f0a0a0;padding-top:2px;line-height:1.2;}}
.cv-st span{{font-size:10.5px;color:#5c6170;line-height:1.45;}}
.cv-parts{{position:absolute;left:13mm;right:13mm;bottom:14mm;display:grid;grid-template-columns:repeat(4,1fr);gap:10px;}}
.cv-p{{background:rgba(255,255,255,.88);border-radius:12px;border-top:4px solid #c92a2a;padding:8px 12px;}}
.cv-p .a{{font-weight:800;font-size:13px;color:#23263a;}} .cv-p .b{{font-size:10.5px;color:#5c6170;margin-top:2px;line-height:1.5;}}
.cv-src{{position:absolute;left:13mm;right:13mm;bottom:7mm;font-size:9.5px;color:#9a9486;}}
.cover2 .ft{{display:none;}}
</style>
<div class="cv-left"><div class="cv-k">PHARMACEUTICAL ORGANIC CHEMISTRY II · 기말 대비 노트 · CH 22</div>
<div class="cv-h">제22장<br>카르보닐 알파 치환 반응<br>마스터 노트</div>
<div class="cv-flow">엔올 → 산성 α-할로젠화 · HVZ → α-H 산성도 · 엔올레이트 → 알킬화 (말론산 · 아세토아세트산 · LDA)</div>
<div class="cv-chips"><span class="cv-chip">개념 {{NC}}</span><span class="cv-chip">문제 {{NQ}} (그리기·시약·순서·메커니즘·생성물·중간체)</span><span class="cv-chip">과제 22-37·38·42·54</span><span class="cv-chip">원서 예제 4 · 문제 22-1~22-16 (그대로)</span><span class="cv-chip">🎯 녹취 · ✍️ 단권화 노트 반영</span></div>
<div class="cv-txt">각 개념은 <b>💡 핵심 → 📖 설명 → 🖼 슬라이드 → ⚗️ 메커니즘 → 🧠 한 줄</b>, 파트 끝에 문제(왼쪽 문제·풀이 칸, 오른쪽 정답·해설).<br>
수업 녹음에서 교수님이 강조한 것은 「🎯 녹취」, 내가 번역본을 공부하며 정리한 Q&amp;A는 「✍️ 내 정리」로 표시했어.<br>
<span class="r">중간고사처럼 전부 주관식</span>: 구조식 그리기 · 시약 쓰기 · 산 세기 순서 · 반응 사다리 · <b>시약+출발물질만 주는 메커니즘</b> · 생성물/중간체 예측 — 이 노트의 문제도 그 형식이야.</div>
<div class="cv-stats">
<div class="cv-st"><b>36</b><span>강의 슬라이드<br>+ 연습문제 4</span></div>
<div class="cv-st"><b>20</b><span>원서 예제 4<br>+ 문제 16 (그대로)</span></div>
<div class="cv-st"><b>2</b><span>의약품 합성<br>부프로피온·페노바르비탈</span></div>
<div class="cv-st"><b>9→36</b><span>꼭 외울 pKa<br>다이케톤 → LDA</span></div></div></div>
<div class="cv-toc"><div class="t">CONTENTS</div>
<div class="row"><span class="n">00</span><span class="nm">이 노트 쓰는 법 · 출제 스타일<span>Guide</span></span><span class="pg">{{PAGE:f-guide}}</span></div>
<div class="row"><span class="n">00</span><span class="nm">자료 체크리스트<span>Checklist</span></span><span class="pg">{{PAGE:f-check}}</span></div>
<div class="row"><span class="n">00</span><span class="nm">22장 반응 지도 · 4대 직관 공식<span>Map</span></span><span class="pg">{{PAGE:f-map}}</span></div>
<div class="row"><span class="n">01</span><span class="nm">엔올과 산성 α-치환<span>Enols · HVZ · bupropion</span></span><span class="pg">{{S:{P1}}}</span></div>
<div class="row"><span class="n">02</span><span class="nm">α-H 산성도와 엔올레이트<span>pKa · LDA · haloform</span></span><span class="pg">{{S:{P2}}}</span></div>
<div class="row"><span class="n">03</span><span class="nm">엔올레이트 알킬화<span>Malonic · acetoacetic · LDA</span></span><span class="pg">{{S:{P3}}}</span></div>
<div class="row"><span class="n">✓</span><span class="nm">시약 치트시트 · 혼동 쌍 · 직전 10줄<span>Final</span></span><span class="pg">{{PAGE:f-reag}}</span></div></div>
<div class="cv-parts">
<div class="cv-p"><div class="a">PART 1 엔올 · 산성 α-치환</div><div class="b">토토머화 · 엔올 반응 · α-할로젠화 · 속도론 · E2 · HVZ · 부프로피온</div></div>
<div class="cv-p"><div class="a">PART 2 산성도 · 엔올레이트</div><div class="b">NaH·LDA · pKa 표 · 1,3-다이카르보닐 · 할로폼</div></div>
<div class="cv-p"><div class="a">PART 3 알킬화</div><div class="b">S<sub>N</sub>2 제약 · 말론산 · 탈카르복실화 · 아세토아세트산 · 페노바르비탈 · LDA</div></div>
<div class="cv-p"><div class="a">FINAL</div><div class="b">시약 치트시트 · 혼동 쌍 · 시험 직전 10줄</div></div></div>
<div class="cv-src">CH22 강의자료 · 번역본(슬라이드 옆 메커니즘) · 10/30 강의 녹취록 · 단권화 노트 · OpenStax Organic Chemistry 10e 해설집(SSM Ch22) · 중간고사 시험 후기를 바탕으로 정리</div>
""")

guide = dict(t="r", id="f-guide", html=f"""
<div class="hd"><span class="bd">읽기 전에 ①</span><div class="tt"><h1>출제 스타일 · 이 노트 쓰는 법</h1><div class="sb">How the exam looks · how this note is built</div></div><span class="pt">{P0}</span></div>
<div class="body"><div class="main">
<div class="sec">📝 중간고사에서 확인된 출제 형식 (시험 후기)</div>
<table class="t"><tr><th>형식</th><td>총 13문제, 한 문제에 소문항 2–4개, <b>전부 주관식</b></td></tr>
<tr><th>유형</th><td>구조식 그리기 · 시약 쓰기 · 산 세기 순서 · 반응성 사다리 순서 · 메커니즘 그리기 · 생성물 예측 · 중간체 예측</td></tr>
<tr><th>메커니즘</th><td><pk>시약과 출발물질만</pk> 주고 처음부터 끝까지 (중간체·화살표 힌트 없음)</td></tr>
<tr><th>난이도</th><td>모의고사와 결은 같지만 <b>더 어렵게</b> — 여러 단계, 낯선 기질에 같은 반응, 헷갈리는 순서 보기</td></tr>
<tr><th>기말 범위</th><td>22장 + 이후 장 (범위 공지 확인). 22장은 10/30 강의로 마무리.</td></tr></table>
<div class="sec">🎯 22장 강의에서 교수님이 강조한 것 (녹취)</div>
<ul><li>“엔올은 극미량인데 왜 만드나? → <b>반응하기 위해서</b>.” — 개념 01</li>
<li>“α 위치에 Br을 넣는 건 <b>다음 반응(S<sub>N</sub>2·E2)을 위해서</b>.” — 개념 05·06</li>
<li>“문제를 많이 풀어봐야 한다. 요령: <b>거꾸로(역반응)</b> 가 보라.” — 부프로피온, 개념 07</li>
<li>“엔올레이트는 아무 염기나 안 되고 <b>강한 염기(NaH, LDA)</b>.” — 개념 08</li>
<li>“<b>왜 NaOH가 아니라 NaOEt?</b> 가수분해되니까 같은 알콕사이드.” — 개념 12</li>
<li>“탈카르복실화는 <b>β 위치에 카보닐</b>이 있어야.” — 개념 13</li>
<li>“3차는 S<sub>N</sub>2보다 <b>E2</b>, 벤질·알릴은 S<sub>N</sub>2 아주 잘.” — 개념 11</li></ul>
</div><div class="side">
<div class="card tip"><div class="ct">📌 이 노트 사용법</div><ol style="margin:0"><li>개념 쪽 정독: 💡 → 📖 → 슬라이드 → ⚗️ 메커니즘 → 🧠</li><li>메커니즘 띠는 <b>손으로 따라 그리기</b> (화살표는 전자쌍에서 출발)</li><li>문제 쪽은 <b>오른쪽을 가리고</b> 왼쪽 칸에 직접 풀기</li><li>틀린 문제는 “👉 왜?” 줄과 연결된 개념 쪽으로</li><li>시험 직전: 맨 뒤 시약 치트시트 · 혼동 쌍 · 10줄</li></ol></div>
<div class="card"><div class="ct">🖍 표시 약속</div><y>노랑 = 핵심 개념</y> · <g>초록 = 결론·공식</g> · <pk>분홍 = 시험 포인트·함정</pk><br>
<span class="tag j">🎯 녹취</span>교수님 강조 · <span class="tag h">✍️ 내 정리</span>단권화 노트 Q&amp;A · <span class="tag s">본문/과제</span>문제 출처</div>
<div class="card"><div class="ct">🧪 문제 유형 표시</div><span class="qk draw">구조식 그리기</span> <span class="qk reag">시약 쓰기</span> <span class="qk ord">순서 배열</span> <span class="qk mech">메커니즘</span> <span class="qk prod">생성물 예측</span> <span class="qk int">중간체 예측</span> <span class="qk bl">빈칸 채우기</span> <span class="qk sa">서술형</span></div>
<div class="card trap"><div class="ct">⚠️ 녹취 vs 슬라이드가 다른 곳</div>페노바르비탈 “1972년” → 슬라이드 <b>1912년</b>. 두 번째 알킬기 “페닐” → ✗(S<sub>N</sub>2 불가). 케톤 브로민화를 “HVZ”라 부른 부분 → HVZ는 <b>카복실산 + Br₂/PBr₃</b>.</div>
</div></div>""")

check = dict(t="r", id="f-check", html=f"""
<div class="hd"><span class="bd">읽기 전에 ②</span><div class="tt"><h1>자료 체크리스트 — 무엇이 어디에 들어 있나</h1><div class="sb">Homework · in-chapter problems · lecture coverage</div></div><span class="pt">{P0}</span></div>
<div class="body"><div class="main">
<div class="sec">📮 과제 (강의자료 마지막 슬라이드 — 다음 시간 제출)</div>
<table class="t"><tr><th>과제</th><th>내용</th><th>이 노트</th></tr>
<tr><td>22-37</td><td>산성 수소(pKa &lt; 25) 찾기 — (c) 알킨 끝 CH₃ 함정</td><td>PART 2</td></tr>
<tr><td>22-38</td><td>산성도 증가 순서 — 알코올 &gt; 케톤 함정</td><td>PART 2</td></tr>
<tr><td>22-42</td><td>생성물 예측 4종 (탈카르복실화·다이온 알킬화·HVZ·할로폼)</td><td>PART 3</td></tr>
<tr><td>22-54</td><td>시약 a–c (β-케토 에스터 → 가수분해·탈카르복실화 → LDA)</td><td>PART 3</td></tr></table>
<div class="sec">📗 본문 예제·문제 — 원서 그대로 (문제 그림 = 원서, 정답 = 원서 Answer Key + 해설집 SSM)</div>
<table class="t"><tr><th>PART</th><th>원서 예제 · 문제</th></tr>
<tr><td>1 엔올 · 산성 α-치환</td><td>Problem 22-1 · 22-2 · 22-3 · 22-4 · 22-5 · 22-6</td></tr>
<tr><td>2 산성도 · 엔올레이트</td><td>Worked Example 22.1 · Problem 22-7 · 22-8 · 22-9</td></tr>
<tr><td>3 알킬화</td><td>Worked Example 22.2 · Problem 22-10 · 22-11 · 22-12 · Worked Example 22.3 · Problem 22-13 · 22-14 · 22-15 · Worked Example 22.4 · Problem 22-16</td></tr></table>
<div class="sec">🔮 예상 변형 (중간고사보다 한 단계 어렵게)</div>
<p>부프로피온 빈칸 · 염기 고르기 · S<sub>N</sub>2 되는 할라이드 · 페노바르비탈 · 시약+출발물질만 메커니즘 · β vs γ 탈카르복실화 · 합성 설계</p>
</div><div class="side">
<div class="card"><div class="ct">🗂 슬라이드 → 개념</div>
<table class="t"><tr><th>슬라이드</th><th>개념</th></tr><tr><td>2–5</td><td>01 토토머화</td></tr><tr><td>6–7</td><td>02 엔올 반응</td></tr><tr><td>8–9</td><td>03 산성 할로젠화</td></tr><tr><td>10</td><td>04 속도론·D 교환</td></tr><tr><td>11</td><td>05 E2</td></tr><tr><td>12–13</td><td>06 HVZ</td></tr><tr><td>14</td><td>07 부프로피온</td></tr><tr><td>15–16</td><td>08 엔올레이트·LDA</td></tr><tr><td>17–18</td><td>09 pKa</td></tr><tr><td>19–21</td><td>10 할로폼</td></tr><tr><td>22–23</td><td>11 알킬화·S<sub>N</sub>2</td></tr><tr><td>24–26, 29–30</td><td>12 말론산 ①</td></tr><tr><td>27–28</td><td>13 탈카르복실화</td></tr><tr><td>31–32</td><td>14 아세토아세트산</td></tr><tr><td>33</td><td>15 페노바르비탈</td></tr><tr><td>34–35</td><td>16 LDA 직접</td></tr><tr><td>36</td><td>17 생합성</td></tr></table></div>
<div class="card tip"><div class="ct">📌 함께 볼 파일</div><b>CH22_번역본</b>: 슬라이드마다 번역 + 그림 옆 메커니즘 · <b>강의녹취록</b> · <b>단권화노트</b>(내 Q&amp;A)</div>
</div></div>""")

MAP = (RX(('m', 'CC(=O)C', 70, 55), ('a', 'H⁺', '엔올화'), ('m', 'CC(O)=C', 70, 55), ('a', 'X₂', '1번, 붐비는 쪽'), ('m', 'CC(=O)CBr', 80, 55), ('a', '피리딘, Δ', 'E2'), ('t', 'α,β-불포화 케톤'))
       + RX(('m', 'CCC(=O)O', 70, 55), ('a', '1. Br₂, PBr₃', '2. H₂O (HVZ)'), ('m', 'CC(Br)C(=O)O', 80, 60), ('a', 'NH₃ 등', 'S<sub>N</sub>2'), ('t', 'α-아미노산 등'))
       + RX(('m', 'CCOC(=O)CC(=O)OCC', 100, 55), ('a', '1. NaOEt', '2. R–X'), ('m', 'CCOC(=O)C([*])C(=O)OCC', 100, 70), ('a', 'H₃O⁺, Δ', '−CO₂'), ('m', '[*]CC(=O)O', 70, 55), ('t', '말론산 → 산'))
       + RX(('m', 'CCOC(=O)CC(C)=O', 90, 55), ('a', '1. NaOEt', '2. R–X'), ('m', 'CCOC(=O)C([*])C(C)=O', 90, 70), ('a', 'H₃O⁺, Δ', '−CO₂'), ('m', '[*]CC(C)=O', 70, 55), ('t', '아세토아세트산 → 메틸 케톤'))
       + RX(('m', 'CC1CCCCC1=O', 80, 65), ('a', '1. LDA, THF', '2. CH₃I'), ('m', 'CC1CCCC(C)C1=O', 85, 65), ('t', '덜 붐비는 쪽'), ('a', 'X₂, NaOH 과량', '메틸 케톤'), ('t', 'RCOO⁻ + CHX₃ (할로폼)')))

mp = dict(t="r", id="f-map", html=f"""
<div class="hd"><span class="bd">읽기 전에 ③</span><div class="tt"><h1>22장 한 장 지도 · 4대 직관 공식</h1><div class="sb">Reaction map · the four rules (단권화 노트)</div></div><span class="pt">{P0}</span></div>
<div class="body"><div class="main">
<div class="sec">🗺 반응 지도 — α 탄소를 친핵체로 만들어 E를 붙인다</div>
<div class="mz">{MAP}</div>
<table class="t"><tr><th></th><th>엔올 (산성)</th><th>엔올레이트 (염기)</th></tr>
<tr><td>만드는 법</td><td>H⁺ 촉매, 극미량 계속 생성</td><td>NaOEt(1,3-다이카르보닐) · NaH·LDA(단일 카르보닐)</td></tr>
<tr><td>친핵성</td><td>중성 — X₂, D₃O⁺ 정도</td><td>음이온 — R–X(S<sub>N</sub>2)까지</td></tr>
<tr><td>위치</td><td>더 치환된 쪽</td><td>LDA: 덜 치환된 쪽</td></tr></table>
</div><div class="side">
<div class="card my"><div class="ct">✍️ 내가 만든 4대 만능 직관 공식</div>
<ol style="margin:0;padding-left:1.2em"><li><b>엔올의 반응성</b>: –OH가 공명으로 전자를 밀어 α 탄소로 와르르 → 알켄보다 반응성 큼, α 탄소가 공격수.</li>
<li><b>산성도</b>: 전자 밀어주는 방해꾼(N ＞ O ＞ CH₃)이 없을수록 → 카르보닐 전자 끌기↑ → α-H 쉽게 떨어짐 → 작은 pKa.</li>
<li><b>가열(Δ)</b>: 결합을 끊어 기체(CO₂, CO)로 날리거나(탈카르복실화) 작은 분자(HBr)를 뜯어낼 때(E2, 엔트로피↑) 쓰는 필살기.</li>
<li><b>위치 선택성</b>: 산성(Br₂+AcOH) = 튼튼한 이중결합(자이체프) → 더 치환된 쪽 / LDA = 뚱보라 한산한 쪽.</li></ol></div>
<div class="card tip"><div class="ct">📌 문제 읽는 법</div>조건을 보고 경로를 먼저 정한다: <b>H⁺·AcOH</b> → 엔올 / <b>NaOH·NaOEt·LDA</b> → 엔올레이트 / <b>R–X</b> → S<sub>N</sub>2 / <b>H₃O⁺, Δ</b> → 가수분해 + 탈카르복실화.</div>
</div></div>""")

E = [cover, guide, check, mp]
