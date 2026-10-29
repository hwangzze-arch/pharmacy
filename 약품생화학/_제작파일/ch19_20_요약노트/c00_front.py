from parts import *

cover = dict(t="r", cls="cover2", html=f"""
<style>
.cover2{{background:radial-gradient(ellipse at 0% 0%,#ffe1cf 0%,rgba(255,225,207,0) 45%),radial-gradient(ellipse at 100% 0%,#d9f0e4 0%,rgba(217,240,228,0) 50%),radial-gradient(ellipse at 100% 100%,#dfe6ff 0%,rgba(223,230,255,0) 50%),radial-gradient(ellipse at 40% 60%,#f3ecff 0%,rgba(243,236,255,0) 60%),#f6f3ee !important;}}
.cv-k{{letter-spacing:.3em;font-size:11px;font-weight:700;color:#b0603a;margin-top:6mm;}}
.cv-h{{font-size:38px;line-height:1.2;font-weight:800;margin:10px 0 12px 0;background:linear-gradient(120deg,#c2410c,#127a64);-webkit-background-clip:text;background-clip:text;color:transparent;}}
.cv-flow{{font-size:15px;color:#2c3038;margin-bottom:12px;}}
.cv-chips{{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:12px;}}
.cv-chip{{background:#fff;border:1px solid #eadfd3;border-radius:16px;padding:4px 13px;font-size:11.5px;font-weight:700;color:#2c3038;box-shadow:0 1px 3px rgba(120,80,40,.08);}}
.cv-txt{{font-size:12.2px;line-height:1.75;color:#3a3f4b;}}
.cv-txt .r{{color:#c2410c;font-weight:700;}}
.cv-toc{{position:absolute;right:13mm;top:12mm;width:108mm;background:rgba(255,255,255,.85);border:1px solid #ece4da;border-radius:14px;padding:12px 18px 8px 18px;box-shadow:0 4px 18px rgba(120,80,40,.12);}}
.cv-toc .t{{letter-spacing:.25em;font-size:10px;font-weight:700;color:#b0603a;margin-bottom:4px;}}
.cv-toc .row{{display:flex;align-items:baseline;gap:12px;border-bottom:1px solid #f1ebe3;padding:5px 0;font-size:11.6px;}}
.cv-toc .row:last-child{{border-bottom:none;}}
.cv-toc .n{{width:20px;color:#c08a6a;font-weight:700;}}
.cv-toc .nm{{flex:1;font-weight:700;color:#2c3038;}} .cv-toc .nm span{{font-weight:400;color:#8b8fa0;font-size:.9em;margin-left:4px;}}
.cv-toc .pg{{color:#8b8fa0;}}
.cv-left{{width:160mm;}}
.cv-stats{{display:flex;gap:9px;margin-top:20px;}}
.cv-st{{background:rgba(255,255,255,.78);border:1px solid #ece4da;border-radius:14px;padding:10px 14px;display:flex;align-items:center;gap:10px;flex:1;box-shadow:0 2px 8px rgba(120,80,40,.07);}}
.cv-st b{{font-size:24px;font-weight:800;color:#c2410c;border-top:1px solid #e3b79c;padding-top:2px;line-height:1.2;}}
.cv-st span{{font-size:10.5px;color:#5c6170;line-height:1.45;}}
.cv-parts{{position:absolute;left:13mm;right:13mm;bottom:14mm;display:grid;grid-template-columns:repeat(4,1fr);gap:10px;}}
.cv-p{{background:rgba(255,255,255,.88);border-radius:12px;border-top:4px solid #4651c8;padding:8px 12px;box-shadow:0 2px 8px rgba(120,80,40,.08);}}
.cv-p .a{{font-weight:800;font-size:13px;color:#23263a;}} .cv-p .b{{font-size:10.5px;color:#5c6170;margin-top:2px;line-height:1.5;}}
.cv-src{{position:absolute;left:13mm;right:13mm;bottom:7mm;font-size:9.5px;color:#9a9486;}}
.cover2 .ft{{display:none;}}
</style>
<div class="cv-left"><div class="cv-k">LEHNINGER · PHARMACEUTICAL BIOCHEMISTRY · 기말 대비 노트</div>
<div class="cv-h">약품생화학<br>Chap 19–20 시험대비<br>요약노트 (TB추가)</div>
<div class="cv-flow">전자전달 → ATP 합성 → 조절·ROS → 미토콘드리아의 다른 얼굴 → 광합성 명반응 → 캘빈 회로</div>
<div class="cv-chips"><span class="cv-chip">개념 요약 {{NC}}</span><span class="cv-chip">교수님 테스트뱅크 {{NTB}}문제</span><span class="cv-chip">개념확인 {{NMY}}</span><span class="cv-chip">다답형 · 빈칸 · O/X 연습</span><span class="cv-chip">📍 몸속 위치 표시</span><span class="cv-chip">약어 총정리</span></div>
<div class="cv-txt"><span class="r">범위 = 강의자료 Chap19_20_note (134쪽)</span> · Lehninger 19장(산화적 인산화·광인산화) + 20.1(광합성 탄수화물 합성).<br>
2026 중간고사 형식: <b>객관식 50</b>(하나 고르기 + <b>맞는 것 모두 고르기</b>) + <b>빈칸 3</b> → 보기 하나하나 O/X로 따지는 연습이 핵심.<br>
각 개념은 <b>💡 핵심 → 📖 설명 → 📐 공식 → ✍️ 예제 → 🧠 한 줄</b>, 바로 뒤에 그 개념의 문제(왼쪽 문제·풀이칸, 오른쪽 정답·해설).<br>
개념마다 <b>📍 몸속 어디?</b>(13–18장 스토리 마인드맵에 이어서)를 달았어. PART마다 <b>개념 요약 → 개념확인 → 교수님 기출(테스트뱅크)</b> 순서. 테스트뱅크 정답이 의심스러운 곳은 ⚠️로 표시했어.</div>
<div class="cv-stats">
<div class="cv-st"><b>134</b><span>강의 슬라이드<br>Chap 19–20</span></div>
<div class="cv-st"><b>{{NTB}}</b><span>테스트뱅크<br>ch19 76 · ch20 21</span></div>
<div class="cv-st"><b>{{NQ}}</b><span>전체 문제<br>1문제 = 1쪽</span></div>
<div class="cv-st"><b>30/32</b><span>포도당 1개의<br>ATP (꼭 기억!)</span></div></div></div>
<div class="cv-toc"><div class="t">CONTENTS</div>
<div class="row"><span class="n">00</span><span class="nm">시험 형식 · 이 노트 쓰는 법<span>Guide</span></span><span class="pg">{{PAGE:f-guide}}</span></div>
<div class="row"><span class="n">00</span><span class="nm">스토리 — 숨 쉬는 순간부터 샐러드까지<span>Story map</span></span><span class="pg">{{PAGE:f-story}}</span></div>
<div class="row"><span class="n">00</span><span class="nm">한 장으로 보는 큰 그림<span>Big map</span></span><span class="pg">{{PAGE:f-map}}</span></div>
<div class="row"><span class="n">00</span><span class="nm">확대 그림 — 세포 → 미토·엽록체 → 막<span>Zoom in</span></span><span class="pg">{{PAGE:f-zoom1}}</span></div>
<div class="row"><span class="n">00</span><span class="nm">백지 복습 — 빈칸 그림 2장<span>Draw it yourself</span></span><span class="pg">{{PAGE:f-blank1}}</span></div>
<div class="row"><span class="n">01</span><span class="nm">19.1 전자전달 사슬<span>Respiratory chain</span></span><span class="pg">{{S:{P1}}}</span></div>
<div class="row"><span class="n">02</span><span class="nm">19.2 ATP 합성<span>ATP synthase</span></span><span class="pg">{{S:{P2}}}</span></div>
<div class="row"><span class="n">03</span><span class="nm">19.3 조절 · 활성산소<span>Regulation · ROS</span></span><span class="pg">{{S:{P3}}}</span></div>
<div class="row"><span class="n">04</span><span class="nm">19.4–19.5 미토콘드리아의 다른 얼굴<span>Heat · P-450 · apoptosis · mtDNA</span></span><span class="pg">{{S:{P4}}}</span></div>
<div class="row"><span class="n">05</span><span class="nm">광합성 명반응<span>Photophosphorylation</span></span><span class="pg">{{S:{P5}}}</span></div>
<div class="row"><span class="n">06</span><span class="nm">20.1 캘빈 회로<span>Carbon assimilation</span></span><span class="pg">{{S:{P6}}}</span></div>
<div class="row"><span class="n">✓</span><span class="nm">혼동 쌍 · 숫자 카드 · 약어 총정리<span>Final review</span></span><span class="pg">{{PAGE:f-pairs}}</span></div></div>
<div class="cv-parts">
<div class="cv-p" style="border-top-color:#4651c8"><div class="a">PART 1–2 호흡사슬 · ATP 합성</div><div class="b">Complex I–IV · Q 회로 · 양성자 구동력 · F₀F₁ 회전 촉매 · P/O</div></div>
<div class="cv-p" style="border-top-color:#12937a"><div class="a">PART 3–4 조절 · 미토콘드리아</div><div class="b">수용체 조절 · IF₁ · ROS · 갈색지방 · P-450 · 세포자멸사 · mtDNA</div></div>
<div class="cv-p" style="border-top-color:#c2410c"><div class="a">PART 5–6 광합성</div><div class="b">엽록소 · PSII/PSI · Z 도식 · 광인산화 · 캘빈 회로 · 루비스코</div></div>
<div class="cv-p" style="border-top-color:#f0a020"><div class="a">FINAL</div><div class="b">혼동 쌍 · 숫자 카드 · 약어 총정리</div></div></div>
<div class="cv-src">Chap19_20_note 강의자료 · 쉬운 설명 · 교수님 테스트뱅크(lehninger6e_tb_ch19·20) · 생화학_13-18장_스토리_마인드맵 · 레닌저 원서 · 생화학 시험 기록(2026 중간 형식)을 바탕으로 정리</div>
""")

guide = dict(t="r", id="f-guide", html=f"""
<div class="hd"><span class="bd">읽기 전에 ①</span><div class="tt"><h1>시험 형식 · 출제 스타일 · 이 노트 쓰는 법</h1><div class="sb">Exam format · how this note is built</div></div><span class="pt">{P0}</span></div>
<div class="body"><div class="main">
<div class="sec">📅 지난 시험에서 배운 것 (생화학 시험 기록)</div>
<table class="t"><tr><th>2026 중간고사</th><td>13–18장, 총 <b>53문제</b> = 객관식 50(하나 고르기 + <b>다답형</b>: 맞는 것 모두 고르기) + <b>빈칸 채우기 3</b>. 서술형 없음.</td></tr>
<tr><th>2025 중간고사</th><td>주관식 3문제 (예: “근육에는 (글루카곤) 수용체가 없고 (당신생) 효소가 없다”)</td></tr>
<tr><th>기말 범위(이 노트)</th><td>Chap19_20_note = 19.1–19.5 산화적 인산화 + 광합성 명반응 + 20.1 캘빈 회로</td></tr></table>
<div class="sec">🎯 그래서 이렇게 공부한다</div>
<ul><li><b>다답형 대비</b>: 테스트뱅크의 “틀린 것 고르기(not / except / false)”와 이 노트의 「다답형」 문제에서 <y>보기 다섯 개를 전부 O/X로 판정</y>. 해설의 ⭕/❌ 줄을 꼭 읽기.</li>
<li><b>빈칸 대비</b>: 효소·물질 이름과 숫자를 정확히 — <pk>H<sup>+</sup> 4·4·2 = 10, P/O 2.5/1.5, 30/32 ATP, −220 kJ, 광자 4/8, H<sup>+</sup> 12개 · ΔpH 3, 캘빈 3·6·6·1·5·3, ATP 9 · NADPH 6</pk>.</li>
<li><b>억제제 지도</b>: 로테논(I) · 안티마이신 A(III) · CN<sup>−</sup>/CO(IV) · 올리고마이신(F<sub>o</sub>) · DNP/FCCP(짝풀림) · 아트락틸로사이드(ANT) · DCMU(PSII Q<sub>B</sub>) — 기출 단골.</li>
<li>교수님 테스트뱅크는 <b>문제 하나 = 한 쪽</b>: 영어 원문 → 번역 → 풀이칸 / 정답(영어 + 한글) → 쉬운 풀이. 강의에 없는 단원(광호흡·C4/CAM·녹말·수크로스 합성·셀룰로스·펩티도글리칸, 작용 스펙트럼, 광합성의 진화)은 뺐어.</li></ul>
</div><div class="side">
<div class="card tip"><div class="ct">📌 이 노트 사용법</div><ol style="margin:0"><li>개념 페이지 정독 (💡→📖→📐→✍️→🧠)</li><li>바로 뒤 문제에서 <b>오른쪽을 가리고</b> 왼쪽 풀이칸에 직접 풀기</li><li>틀린 문제는 “👉 왜?” 줄과 🧠 한 줄만 다시</li><li>시험 직전: 맨 끝 「혼동 쌍」 「숫자 카드」 「약어 총정리」</li></ol></div>
<div class="card"><div class="ct">🖍 표시 약속</div><y>노랑 = 핵심 개념</y> · <g>초록 = 공식·결론</g> · <pk>분홍 = 시험 포인트·함정</pk><br>
<span class="qk tb">교수님 기출 · TB</span> 교수님 테스트뱅크 · <span class="qk chk">개념확인</span> 직접 만든 연습<br>
<span class="term" style="display:inline-block;margin-top:4px">＊[용어: …] = 어려운 말이 나오면 바로 아래에서 쉬운 말로 풀어 줌</span></div>
<div class="card trap"><div class="ct">⚠️ 테스트뱅크 정답 주의 (⚠️ 상자로 표시)</div>19-29(명반응 결과) · 19-30(틀린 것: 실제는 C) · 19-62(인산 운반 = 공동수송) · 19-64(38 ATP → 강의는 30/32).</div>
</div></div>""")

story = dict(t="r", id="f-story", html=f"""
<style>
.st-grid{{display:grid;grid-template-columns:1fr 1fr 1fr;gap:9px;margin-top:9px;flex:1;}}
.sc-b{{background:#fff;border:1px solid var(--line);border-top:4px solid var(--c);border-radius:11px;padding:10px 14px;font-size:1.13em;line-height:1.75;}}
.sc-b .t{{font-weight:800;color:var(--c);font-size:1.05em;}} .sc-b .w{{display:inline-block;background:var(--c);color:#fff;border-radius:6px;font-size:.78em;font-weight:700;padding:0 7px;margin:2px 0 3px 0;}}
.sc-b .p{{font-size:.85em;color:#6c7280;}}
</style>
<div class="hd"><span class="bd">읽기 전에 ②</span><div class="tt"><h1>19–20장 스토리 — 숨 쉬는 순간부터 샐러드 한 입까지</h1><div class="sb">13–18장 마인드맵의 “5단계 전자전달계(내막)”를 확대한 이야기 · 개념마다 📍 몸속 어디?로 다시 나와</div></div><span class="pt">{P0}</span></div>
<div class="core"><span class="lb">🧭 줄거리</span>밥 → 포도당 → 세포질(해당) → 미토 기질(TCA) → <b>미토 내막(전자전달·ATP 합성) ← 19장</b> → 숨 쉰 O₂가 물로 … 그 밥의 탄소는 원래 <b>식물 잎의 엽록체(광합성) ← 19장 후반·20장</b>에서 왔다!</div>
<div class="st-grid">
<div class="sc-b" style="--c:#4651c8"><div class="t">① 트럭 하역 — 호흡사슬</div><span class="w">미토콘드리아 내막</span><br>TCA 맷돌이 채운 NADH·FADH₂ 트럭이 내막 레일(I → Q → III → cyt c → IV)에 전자를 쏟는다. 레일 끝 청소부 O₂(코 → 폐 → 혈액 → 세포)가 받아 물. 지나가며 H⁺를 막사이공간으로 퍼 올림.<div class="p">PART 1 · 개념 01–11</div></div>
<div class="sc-b" style="--c:#127a64"><div class="t">② 물레방아 — ATP 합성</div><span class="w">내막 → 기질</span><br>막사이공간 댐에 고인 H⁺가 ATP 합성효소(F₀ 터빈 → γ축 → F₁)를 돌리며 기질로 → ATP 목돈. ANT가 ATP를 세포질로 출하(근육 수축에 사용).<div class="p">PART 2 · 개념 12–17</div></div>
<div class="sc-b" style="--c:#9a4a12"><div class="t">③ 공장장 — 조절·불똥</div><span class="w">세포질 ↔ 기질</span><br>운동해서 ADP가 쌓여야 보일러가 빨리 돈다. 숨이 차면(저산소) IF₁이 역주행 방지, 새는 전자는 ROS 불똥 → SOD·GPx가 청소, HIF-1(핵)이 보일러 감속.<div class="p">PART 3 · 개념 18–20</div></div>
<div class="sc-b" style="--c:#c2410c"><div class="t">④ 보일러실의 부업</div><span class="w">갈색지방 · 간 · 부신 · 췌장</span><br>아기 등 갈색지방의 난로(UCP1), 간 소포체·부신 미토의 P-450(해독·스테로이드), cyt c 자폭 버튼(세포자멸사), 엄마에게서 온 mtDNA(LHON 눈, MERRF 근육), 췌장 β세포 혈당 센서.<div class="p">PART 4 · 개념 21–25</div></div>
<div class="sc-b" style="--c:#2f7d32"><div class="t">⑤ 밥의 고향 — 식물 잎의 태양광 발전</div><span class="w">엽록체 틸라코이드 막</span><br>햇빛 → 엽록소 안테나 → PSII가 물을 쪼개 O₂(우리가 마실 산소!) → PQ → b₆f → PC → PSI → NADPH. 내강에 쌓인 H⁺로 ATP. 미토와 똑같은 엔진, 연료만 빛.<div class="p">PART 5 · 개념 26–33</div></div>
<div class="sc-b" style="--c:#7c2d92"><div class="t">⑥ 설탕 공장 — 캘빈 회로</div><span class="w">엽록체 스트로마 → 세포질 → 체관</span><br>기공으로 들어온 CO₂ + ATP·NADPH → 루비스코 → G3P → 수크로스로 포장해 체관 배송 → 감자 녹말·쌀·채소 → 우리가 먹으면 다시 13장 1단계로. 이야기가 원을 그린다.<div class="p">PART 6 · 개념 34–38</div></div>
</div>""")

bigmap = dict(t="r", id="f-map", html=f"""
<style>
.mp{{display:flex;flex-direction:column;justify-content:space-around;gap:10px;margin-top:9px;flex:1;font-size:1.2em;line-height:1.7;}}
.lane{{background:#fff;border:1px solid var(--line);border-radius:12px;padding:8px 12px;}}
.lane .lt{{font-weight:800;font-size:1.05em;margin-bottom:5px;}}
.chain{{display:flex;flex-wrap:wrap;align-items:center;gap:5px;}}
.nd{{border-radius:8px;padding:3px 9px;font-weight:700;font-size:.93em;border:1.5px solid;background:#fff;white-space:nowrap;}}
.nd small{{display:block;font-weight:500;font-size:.8em;color:#6c7280;}}
.ar{{color:#9aa0ac;font-weight:700;}}
.pump{{color:#c2410c;font-weight:800;font-size:.85em;}}
</style>
<div class="hd"><span class="bd">읽기 전에 ③</span><div class="tt"><h1>한 장으로 보는 큰 그림 — 미토콘드리아와 엽록체는 같은 엔진</h1><div class="sb">Big map: respiratory chain · ATP synthase · Z scheme · Calvin cycle</div></div><span class="pt">{P0}</span></div>
<div class="mp">
<div class="lane"><div class="lt" style="color:#4651c8">⚡ 미토콘드리아 호흡사슬 (전자: NADH → O<sub>2</sub>, 내리막)</div>
<div class="chain"><span class="nd" style="border-color:#4651c8">NADH<small>−0.32 V</small></span><span class="ar">→</span>
<span class="nd" style="border-color:#4651c8">Complex I<small>FMN · Fe-S</small></span><span class="pump">4H⁺↑</span><span class="ar">→</span>
<span class="nd" style="border-color:#127a64">Q 풀<small>← II(숙신산·FAD, 0H⁺) ← ETF ← 글리세롤 3-P</small></span><span class="ar">→</span>
<span class="nd" style="border-color:#4651c8">Complex III<small>Q 회로 · b · c₁ · Rieske</small></span><span class="pump">4H⁺↑</span><span class="ar">→</span>
<span class="nd" style="border-color:#4651c8">cyt c<small>수용성 · 1e⁻</small></span><span class="ar">→</span>
<span class="nd" style="border-color:#4651c8">Complex IV<small>Cu_A · a · a₃–Cu_B</small></span><span class="pump">2H⁺↑</span><span class="ar">→</span>
<span class="nd" style="border-color:#4651c8">O₂ → H₂O<small>+0.82 V</small></span></div>
<div style="margin-top:5px">합: H⁺ <b>10</b>(NADH) / <b>6</b>(숙신산) · ΔG′° = −nℱΔE′° ≈ <b>−220 kJ/mol</b> · 억제: <pk>로테논(I) · 안티마이신 A(III) · CN⁻/CO(IV)</pk></div></div>
<div class="lane"><div class="lt" style="color:#127a64">🌀 ATP 합성효소 (같은 엔진, 두 발전소 공용)</div>
H<sup>+</sup>(P쪽) → <b>F<sub>o</sub></b>(a · b₂ · c 고리, 올리고마이신) → c 고리·<b>γ 회전</b> → <b>F<sub>1</sub></b>(α₃β₃γδε) β: 빈 → 느슨 → 꽉 → <b>ATP 방출</b>(에너지는 여기!) · 한 바퀴 = ATP 3 · ATP 1개 ≈ H<sup>+</sup> 4(수송 1 포함) → P/O <b>2.5 / 1.5</b> · 짝풀림: DNP·FCCP·UCP1</div>
<div class="lane"><div class="lt" style="color:#c2410c">🌞 엽록체 명반응 = Z 도식 (전자: H<sub>2</sub>O → NADP<sup>+</sup>, 빛으로 오르막 두 번)</div>
<div class="chain"><span class="nd" style="border-color:#c2410c">H₂O → O₂<small>Mn₄ · Tyr_Z (광자 4 / O₂)</small></span><span class="ar">→</span>
<span class="nd" style="border-color:#c2410c">PSII · P680<small>Pheo → PQ_A → PQ_B</small></span><span class="ar">→</span>
<span class="nd" style="border-color:#127a64">PQ 풀</span><span class="ar">→</span>
<span class="nd" style="border-color:#c2410c">cyt b₆f<small>Q 회로 (H⁺ → 내강)</small></span><span class="ar">→</span>
<span class="nd" style="border-color:#c2410c">PC<small>Cu · 1e⁻</small></span><span class="ar">→</span>
<span class="nd" style="border-color:#c2410c">PSI · P700<small>A₀ → A₁ → Fe-S</small></span><span class="ar">→</span>
<span class="nd" style="border-color:#c2410c">Fd → FNR → NADPH</span></div>
<div style="margin-top:5px">2H₂O + 2NADP⁺ + <b>8 광자</b> → O₂ + 2NADPH · H⁺ <b>12</b>(OEC 4 + b₆f 8) → ΔpH <b>3</b> → ATP <b>~3</b> · 순환(PSI만) = <b>ATP only</b> · 억제: <pk>DCMU(Q_B)</pk></div></div>
<div class="lane"><div class="lt" style="color:#7c2d92">🍬 캘빈 회로 (스트로마)</div>
3 RuBP + 3 CO₂ <b>(루비스코)</b> → 6 3-PG → (6 ATP · 6 NADPH) → 6 G3P → <b>1 G3P 출하</b>(DHAP ⇄ Pᵢ 역수송체 → 수크로스) + 5 G3P → (트랜스케톨레이스·TPP, 3 ATP) → 3 RuBP · G3P 1개 = ATP 9 + NADPH 6 · 포도당 = ATP 18 + NADPH 12</div>
</div>""")

E = [cover, guide, story, bigmap]
