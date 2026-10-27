from parts import *

cover = dict(t="r", cls="cover2", html=f"""
<style>
.cover2{{background:radial-gradient(ellipse at 0% 0%,#ffd9e8 0%,rgba(255,217,232,0) 45%),radial-gradient(ellipse at 100% 0%,#dcd6ff 0%,rgba(220,214,255,0) 50%),radial-gradient(ellipse at 100% 100%,#d4f5e6 0%,rgba(212,245,230,0) 50%),radial-gradient(ellipse at 40% 60%,#dfe6ff 0%,rgba(223,230,255,0) 60%),#f4f1fb !important;}}
.cv-k{{letter-spacing:.32em;font-size:11px;font-weight:700;color:#7d74c9;margin-top:6mm;}}
.cv-h{{font-size:40px;line-height:1.18;font-weight:800;margin:10px 0 12px 0;background:linear-gradient(120deg,#5b3fd6,#3f57d8);-webkit-background-clip:text;background-clip:text;color:transparent;}}
.cv-flow{{font-size:15.5px;color:#2c3038;margin-bottom:12px;}}
.cv-chips{{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:12px;}}
.cv-chip{{background:#fff;border:1px solid #e3def3;border-radius:16px;padding:4px 13px;font-size:11.5px;font-weight:700;color:#2c3038;box-shadow:0 1px 3px rgba(80,60,160,.08);}}
.cv-txt{{font-size:12.2px;line-height:1.75;color:#3a3f4b;}}
.cv-txt .r{{color:#d6336c;font-weight:700;}}
.cv-toc{{position:absolute;right:13mm;top:12mm;width:105mm;background:rgba(255,255,255,.82);border:1px solid #e6e1f5;border-radius:14px;padding:12px 18px 8px 18px;box-shadow:0 4px 18px rgba(90,70,170,.12);}}
.cv-toc .t{{letter-spacing:.25em;font-size:10px;font-weight:700;color:#5b4fc0;margin-bottom:4px;}}
.cv-toc .row{{display:flex;align-items:baseline;gap:12px;border-bottom:1px solid #ece8f6;padding:5px 0;font-size:11.8px;}}
.cv-toc .row:last-child{{border-bottom:none;}}
.cv-toc .n{{width:20px;color:#8a83c9;font-weight:700;}}
.cv-toc .nm{{flex:1;font-weight:700;color:#2c3038;}} .cv-toc .nm span{{font-weight:400;color:#8b8fa0;font-size:.9em;margin-left:4px;}}
.cv-toc .pg{{color:#8b8fa0;}}
.cv-left{{width:163mm;}}
.cv-stats{{display:flex;gap:9px;margin-top:22px;}}
.cv-st{{background:rgba(255,255,255,.75);border:1px solid #e6e1f5;border-radius:14px;padding:10px 14px;display:flex;align-items:center;gap:10px;flex:1;box-shadow:0 2px 8px rgba(90,70,170,.07);}}
.cv-st b{{font-size:24px;font-weight:800;color:#3f57d8;border-top:1px solid #9aa3d8;padding-top:2px;line-height:1.2;}}
.cv-st span{{font-size:10.5px;color:#5c6170;line-height:1.45;}}
.cv-parts{{position:absolute;left:13mm;right:13mm;bottom:14mm;display:grid;grid-template-columns:repeat(4,1fr);gap:10px;}}
.cv-p{{background:rgba(255,255,255,.85);border-radius:12px;border-top:4px solid #4651c8;padding:8px 12px;box-shadow:0 2px 8px rgba(90,70,170,.08);}}
.cv-p .a{{font-weight:800;font-size:13px;color:#23263a;}} .cv-p .b{{font-size:10.5px;color:#5c6170;margin-top:2px;line-height:1.5;}}
.cv-src{{position:absolute;left:13mm;right:13mm;bottom:7mm;font-size:9.5px;color:#9a9486;}}
.cover2 .ft{{display:none;}}
</style>
<div class="cv-left"><div class="cv-k">PHAR · PHARMACEUTICAL ANALYSIS II · 중간고사 대비 노트</div>
<div class="cv-h">의약품분석학 II<br>중간고사 통합<br>마스터 노트</div>
<div class="cv-flow">빛의 성질 → UV-Vis → 형광 → 선광도 → 원자분광법 → NMR</div>
<div class="cv-chips"><span class="cv-chip">상세요약 · 개념 {{NC}}</span><span class="cv-chip">문제 {{NQ}} (객관·서술·계산·빈칸·O/X)</span><span class="cv-chip">과제 1·2 전 문항</span><span class="cv-chip">족보·녹취록 반영</span><span class="cv-chip">혼동 쌍·숫자 카드</span></div>
<div class="cv-txt"><span class="r">중간고사 범위 = Lecture 2–4</span> · 10/26(월) 13:00–14:30 (90분), 과학기술2관 217호, 성적의 40%.<br>
형식: <b>객관식 + 주관식</b>(서술형 · 계산 · 빈칸 채우기). <b>계산기 사용 불가</b> · OMR(Optical Mark Recognition, 광학 마크 판독) 카드용 수성펜 지참.<br>
각 개념은 <b>💡 핵심 → 📖 설명 → 📐 공식 → ✍️ 예제 → 🧠 한 줄</b>, 바로 뒤에 그 개념의 문제(왼쪽 문제·풀이칸, 오른쪽 정답·해설).<br>
작년 기출은 「족보」, 과제는 「과제」, 마지막 수업 녹음에서 강조한 건 「🎯 녹음」으로 표시했어.</div>
<div class="cv-stats">
<div class="cv-st"><b>111</b><span>슬라이드<br>Lecture 2–4</span></div>
<div class="cv-st"><b>18</b><span>족보 주제<br>전부 문항화</span></div>
<div class="cv-st"><b>11</b><span>과제 1·2<br>빈칸형 재구성</span></div>
<div class="cv-st"><b>10/26</b><span>시험일(월)<br>성적 40%</span></div></div></div>
<div class="cv-toc"><div class="t">CONTENTS</div>
<div class="row"><span class="n">00</span><span class="nm">시험 정보 · 출제 스타일<span>Exam info</span></span><span class="pg">{{PAGE:f-guide}}</span></div>
<div class="row"><span class="n">00</span><span class="nm">족보 · 과제 체크리스트<span>What seniors saw</span></span><span class="pg">{{PAGE:f-jokbo}}</span></div>
<div class="row"><span class="n">00</span><span class="nm">계산기 없이 푸는 수학<span>Math</span></span><span class="pg">{{PAGE:f-math}}</span></div>
<div class="row"><span class="n">01</span><span class="nm">분광학 기초<span>Basics of spectroscopy</span></span><span class="pg">{{S:{P1}}}</span></div>
<div class="row"><span class="n">02</span><span class="nm">자외가시부흡광도측정법<span>UV-Vis</span></span><span class="pg">{{S:{P2}}}</span></div>
<div class="row"><span class="n">03</span><span class="nm">형광광도법<span>Fluorimetry</span></span><span class="pg">{{S:{P3}}}</span></div>
<div class="row"><span class="n">04</span><span class="nm">선광도<span>Optical rotation</span></span><span class="pg">{{S:{P4}}}</span></div>
<div class="row"><span class="n">05</span><span class="nm">원자분광법<span>Atomic spectroscopy</span></span><span class="pg">{{S:{P5}}}</span></div>
<div class="row"><span class="n">06</span><span class="nm">핵자기공명(NMR)<span>NMR</span></span><span class="pg">{{S:{P6}}}</span></div>
<div class="row"><span class="n">✓</span><span class="nm">혼동 쌍 총정리 · 숫자 · 공식<span>Final review</span></span><span class="pg">{{PAGE:f-pairs}}</span></div></div>
<div class="cv-parts">
<div class="cv-p" style="border-top-color:#4651c8"><div class="a">1–2장 분광학 · UV-Vis</div><div class="b">빛 · 람베르트-비어 · 장치 · 발색단 · 정량법 4종 · 과제 1</div></div>
<div class="cv-p" style="border-top-color:#12937a"><div class="a">3–4장 형광 · 선광도</div><div class="b">야블론스키 · 여기/방출 · 비선광도 · ee · 과제 2</div></div>
<div class="cv-p" style="border-top-color:#d6336c"><div class="a">5–6장 원자분광 · NMR</div><div class="b">AAS·AES·ICP · 화학적 이동 · 짝지음 · FT · ¹³C</div></div>
<div class="cv-p" style="border-top-color:#f0a020"><div class="a">FINAL</div><div class="b">혼동 쌍 · 숫자 카드 · 족보 체크리스트</div></div></div>
<div class="cv-src">의약품분석학II Lecture 2–4 강의자료 · 번역·상세설명 3종 · 과제 1·2 · 족보(중간·기말 복기) · 중간고사 전 2주 수업 녹음 · 교재 예제·연습문제를 바탕으로 정리</div>
""")

guide = dict(t="r", id="f-guide", html=f"""
<div class="hd"><span class="bd">읽기 전에 ①</span><div class="tt"><h1>시험 정보 · 출제 스타일 · 이 노트 쓰는 법</h1><div class="sb">Exam info · how this note is built</div></div><span class="pt">{P0}</span></div>
<div class="body"><div class="main">
<div class="sec">📅 교수님 공지</div>
<table class="t"><tr><th>일시</th><td>2026년 10월 26일 13:00–14:30 (90분)</td><th>장소</th><td>과학기술2관 217호</td></tr>
<tr><th>범위</th><td colspan="3">중간고사 이전 강의 전체 = Lecture 2(분광학 기초·자외가시부) · Lecture 3(형광·선광도·원자분광법) · Lecture 4(NMR, ¹³C-NMR까지 — 녹음에서 “시험 범위는 여기까지”)</td></tr>
<tr><th>형식</th><td colspan="3">객관식 + 주관식 (서술형 · 계산 · 빈칸 채우기 혼합)</td></tr>
<tr><th>유의</th><td colspan="3"><pk>계산기 포함 전자기기 사용 불가</pk> → 숫자가 손으로 풀리게 나온다(과제·예제 숫자 그대로 나올 가능성 큼). OMR(Optical Mark Recognition, 광학 마크 판독) 카드용 수성펜 지참</td></tr></table>
<div class="sec">🎯 교수님 출제 스타일 (족보 · 과제 · 녹음에서 읽어낸 것)</div>
<ul><li><b>강의자료를 제대로 들었는지</b> 확인하는 문제가 대부분 → 슬라이드의 정의·숫자·Q(질문)가 그대로 나온다.</li>
<li><b>과제 1·2와 비슷한 계산</b>: 비흡광도, 표준물첨가법, 검량선, 형광 정량, 비선광도·몰선광도, ee(Enantiomeric excess, 거울상이성질체 과잉률).</li>
<li><b>서술형 계산에 빈칸 넣기</b> — 식의 한 부분을 비워 두고 채우게 한다 (이 노트의 「빈칸 채우기」 문제).</li>
<li>녹음에서 교수님이 콕 집은 것: NMR 분석 가능한 핵종 5개 외우기, δ 공식의 단위(교재 오류 정정), 이웃자리 짝지음(³J)만 해석, FT-NMR 3단계, ¹³C-NMR 특징.</li></ul>
</div><div class="side">
<div class="card tip"><div class="ct">📌 이 노트 사용법</div><ol style="margin:0"><li>개념 페이지를 한 번 정독 (💡→📖→📐→✍️→🧠)</li><li>바로 뒤 문제 페이지에서 <b>오른쪽을 가리고</b> 왼쪽 빈칸에 직접 풀기</li><li>틀린 문제는 해설의 “👉 왜?” 줄만 다시 읽기</li><li>시험 직전: 맨 끝 「혼동 쌍 총정리」와 「숫자·공식 카드」</li></ol></div>
<div class="card"><div class="ct">🖍 표시 약속</div><y>노랑 = 핵심 개념</y> · <g>초록 = 공식·결론</g> · <pk>분홍 = 시험 포인트·함정</pk><br><span class="tag j">족보</span>작년 기출 · <span class="tag h">과제</span>과제 1·2 · <span class="tag s">슬라이드 Q</span>강의자료 속 질문<br><span class="term" style="display:inline-block;margin-top:4px">＊[용어: …] = 어려운 말이 나오면 바로 아래에서 쉬운 말로 풀어 줌</span></div>
<div class="card trap"><div class="ct">⚠️ 범위 주의</div>작년 중간 족보의 IR(Infrared, 적외선)·Raman(라만) 문제는 <b>올해 Lecture 2–4에 없는 단원</b>이라 이 노트에서 뺐어. 질량분석법(Lecture 5)도 녹음상 중간 범위 밖.</div>
</div></div>""")

jokbo = dict(t="r", id="f-jokbo", html=f"""
<div class="hd"><span class="bd">읽기 전에 ②</span><div class="tt"><h1>족보·과제 체크리스트 — 어디서 다시 보나</h1><div class="sb">Past-exam & assignment map</div></div><span class="pt">{P0}</span></div>
<div class="body"><div class="main">
<table class="t"><tr><th>작년 중간고사 기출(복기)</th><th>유형</th><th>이 노트에서</th></tr>
<tr><td>UV-Vis 광원의 특징과 파장</td><td>객관·서술</td><td>{{REF:c-lamp}} · {{REF:q-lamp}}</td></tr>
<tr><td>광다이오드 배열(PDA) 설명</td><td>주관식</td><td>{{REF:c-pda}} · {{REF:q-pda}}</td></tr>
<tr><td>투광도·흡광도 계산</td><td>계산</td><td>{{REF:c-ta}} · {{REF:q-ta}}</td></tr>
<tr><td>비흡광도 계산</td><td>계산</td><td>{{REF:c-e1}} · {{REF:q-hw11}}</td></tr>
<tr><td>조색단 특징</td><td>객관식</td><td>{{REF:c-auxo}} · {{REF:q-auxo}}</td></tr>
<tr><td>Emission / Excitation spectrum</td><td>객관·빈칸</td><td>{{REF:c-exem}} · {{REF:q-exem}}</td></tr>
<tr><td>비선광도 설명·계산</td><td>객관식</td><td>{{REF:c-sr}} · {{REF:q-nap}}</td></tr>
<tr><td>Enantiomeric excess 계산</td><td>계산</td><td>{{REF:c-ee}} · {{REF:q-hw25}}</td></tr>
<tr><td>분자분광 = 연속, 원자분광 = 선 스펙트럼</td><td>주관식</td><td>{{REF:c-line}} · {{REF:q-line}}</td></tr>
<tr><td>AAS 중공음극램프 파장범위·원리</td><td>객관식</td><td>{{REF:c-hcl}} · {{REF:q-hcl}}</td></tr>
<tr><td>ICP 과정</td><td>서술</td><td>{{REF:c-icp}} · {{REF:q-icp}}</td></tr>
<tr><td>NMR 분석 가능한 원소</td><td>객관식</td><td>{{REF:c-spin}} · {{REF:q-spin}}</td></tr>
<tr><td>B 변화에 따른 진동수 변화 계산</td><td>계산</td><td>{{REF:c-larmor}} · {{REF:q-larmor}}</td></tr>
<tr><td>Chemical shift 계산</td><td>계산</td><td>{{REF:c-delta}} · {{REF:q-delta}}</td></tr>
<tr><td>자기이방성 보기</td><td>객관식</td><td>{{REF:c-aniso}} · {{REF:q-aniso}}</td></tr>
<tr><td>spin-spin coupling · 대응 수소 찾기 · 짝지음 상수 계산</td><td>객관·계산</td><td>{{REF:c-n1}} · {{REF:q-split}} · {{REF:q-j}}</td></tr>
<tr><td>FT-NMR 분석 순서</td><td>주관식</td><td>{{REF:c-ft}} · {{REF:q-ft}}</td></tr>
<tr><td>형광분석에 레이저를 쓰는 이유</td><td>주관식</td><td>{{REF:c-fint}} · {{REF:q-laser}}</td></tr></table>
</div><div class="side">
<table class="t"><tr><th>과제</th><th>이 노트에서</th></tr>
<tr><td>과제 1-1 비흡광도로 적합 판정</td><td>{{REF:q-hw11}}</td></tr>
<tr><td>과제 1-2 비흡광도로 함량</td><td>{{REF:q-hw12}}</td></tr>
<tr><td>과제 1-3 표준물첨가(1점)</td><td>{{REF:q-hw13}}</td></tr>
<tr><td>과제 1-4 표준물첨가(다점·X절편)</td><td>{{REF:q-hw14}}</td></tr>
<tr><td>과제 1-5 검량선법</td><td>{{REF:q-hw15}}</td></tr>
<tr><td>과제 1-6 표준품 비교·공시험</td><td>{{REF:q-hw16}}</td></tr>
<tr><td>과제 2-1 형광으로 정제 함량</td><td>{{REF:q-hw21}}</td></tr>
<tr><td>과제 2-2 선광도로 포도당</td><td>{{REF:q-hw22}}</td></tr>
<tr><td>과제 2-3 포도당 주사액</td><td>{{REF:q-hw23}}</td></tr>
<tr><td>과제 2-4 비선광도·몰선광도</td><td>{{REF:q-hw24}}</td></tr>
<tr><td>과제 2-5 광학순도·ee</td><td>{{REF:q-hw25}}</td></tr></table>
<div class="card tip"><div class="ct">📌 PART별 위치</div>
PART 1 분광학 기초: {{R:{P1}}}<br>PART 2 자외가시부: {{R:{P2}}}<br>PART 3 형광: {{R:{P3}}}<br>PART 4 선광도: {{R:{P4}}}<br>PART 5 원자분광법: {{R:{P5}}}<br>PART 6 NMR: {{R:{P6}}}</div>
</div></div>""")

math1 = dict(t="r", id="f-math", html=f"""
<div class="hd"><span class="bd">읽기 전에 ③</span><div class="tt"><h1>계산기 없이 푸는 수학 — 이 과목에 필요한 건 딱 6개</h1><div class="sb">Math you actually need (no calculator!)</div></div><span class="pt">{P0}</span></div>
<div class="body"><div class="main">
<p><b>❶ 10의 거듭제곱</b> — 10<sup>−1</sup> = 0.1, 10<sup>−2</sup> = 0.01, 10<sup>−3</sup> = 0.001. “10<sup>−A</sup>”는 “소수점을 A칸 왼쪽으로”. 그래서 흡광도 A = 2면 투광도 T = 10<sup>−2</sup> = 1 %.</p>
<p><b>❷ 로그(log)</b> — log x = “10을 몇 번 곱하면 x?” → log 10 = 1, log 100 = 2, log 1 = 0, log 0.1 = −1.</p>
<div class="term">＊[용어: 로그 = 큰 수를 “0이 몇 개냐”로 줄여 쓰는 자. 곱셈을 덧셈으로 바꿔 줌: log(a×b) = log a + log b]</div>
<p>외워 둘 값 3개: <g>log 2 ≈ 0.30</g>, <g>log 3 ≈ 0.48</g>, <g>log 5 ≈ 0.70</g> → 그러면 log 20 = 1.30, log 0.5 = −0.30, log 0.9 ≈ −0.046 (= log 9 − 1 = 2×0.477 − 1).</p>
<p><b>❸ 비례식</b> — “a : b = c : d → a × d = b × c”. 흡광도·형광세기·선광도는 모두 <y>양(농도)에 비례</y>하니까 거의 모든 정량 계산이 비례식 하나로 끝나.</p>
<p><b>❹ 단위 바꾸기</b> — 1 g = 1000 mg, 1 mg = 1000 μg. <y>w/v% = g/100 mL</y>. 2 mg/100 mL = 0.002 g/100 mL = 0.002 %. 1 g/mL는 100 g/100 mL. ppm(parts per million, 백만분율) = μg/g ≈ μg/mL, ppb(parts per billion, 십억분율) = ng/g, ppt(parts per trillion, 조분율) = pg/g.</p>
<p><b>❺ 나눗셈 요령</b> — 0.925 ÷ 0.002 → 위아래에 1000을 곱해 925 ÷ 2 = 462.5. <b>소수점은 위아래 같이 옮기면 값이 안 변해.</b></p>
<p><b>❻ 파스칼(Pascal) 삼각형</b> — 1 / 1 1 / 1 2 1 / 1 3 3 1 / 1 4 6 4 1 … 바로 위 두 수를 더하면 아래 수. NMR(Nuclear Magnetic Resonance, 핵자기공명) 피크 갈라짐의 높이 비가 이것.</p>
</div><div class="side">
<div class="card"><div class="ct">📋 투광도 ↔ 흡광도 즉답표 (외우기)</div>
<table class="t" style="margin:0"><tr><th>T (투광도)</th><th>A = −log T</th></tr>
<tr><td>100 %</td><td>0</td></tr><tr><td>50 %</td><td>0.30</td></tr><tr><td>10 %</td><td>1</td></tr><tr><td>1 %</td><td>2</td></tr><tr><td>0.1 %</td><td>3</td></tr><tr><td>90 %</td><td>≈ 0.046</td></tr><tr><td>31.6 %</td><td>0.5</td></tr></table></div>
<div class="card ana"><div class="ct">🎈 비유</div>로그는 <b>“계단 층수”</b>야. 1층 = 10, 2층 = 100, 3층 = 1000. 흡광도 A가 1 오르면 통과하는 빛은 1/10로 줄어 — 선글라스를 한 겹 더 쓸 때마다 밝기가 1/10씩!</div>
<div class="card trap"><div class="ct">⚠️ 함정</div>비흡광도는 c를 <b>g/100 mL(%)</b>로, 비선광도는 c를 <b>g/mL</b>로, 층장 l을 <b>mm</b>로 넣는다. 단위가 공식마다 달라서 여기서 제일 많이 틀려.</div>
</div></div>""")

E = [cover, guide, jokbo, math1]
