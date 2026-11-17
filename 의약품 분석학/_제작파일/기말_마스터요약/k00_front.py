from parts import *

cover = dict(t="r", cls="cover2", html=f"""
<style>
.cover2{{background:radial-gradient(ellipse at 0% 0%,#ffe1cc 0%,rgba(255,225,204,0) 45%),radial-gradient(ellipse at 100% 0%,#dcd6ff 0%,rgba(220,214,255,0) 50%),radial-gradient(ellipse at 100% 100%,#d4f5e6 0%,rgba(212,245,230,0) 50%),#f6f2fb !important;}}
.cv-k{{letter-spacing:.32em;font-size:11px;font-weight:700;color:#7d74c9;margin-top:6mm;}}
.cv-h{{display:block;margin:6px 0 8px 0;overflow:visible;}}
.cv-flow{{font-size:15px;color:#2c3038;margin-bottom:12px;}}
.cv-chips{{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:12px;}}
.cv-chip{{background:#fff;border:1px solid #e3def3;border-radius:16px;padding:4px 13px;font-size:11.5px;font-weight:700;color:#2c3038;}}
.cv-txt{{font-size:12.2px;line-height:1.75;color:#3a3f4b;}}
.cv-txt .r{{color:#d6336c;font-weight:700;}}
.cv-left{{width:165mm;}}
.cv-toc{{position:absolute;right:13mm;top:12mm;width:103mm;background:rgba(255,255,255,.85);border:1px solid #e6e1f5;border-radius:14px;padding:12px 18px 8px 18px;box-shadow:0 4px 18px rgba(90,70,170,.12);}}
.cv-toc .t{{letter-spacing:.25em;font-size:10px;font-weight:700;color:#5b4fc0;margin-bottom:4px;}}
.cv-toc .row{{display:flex;align-items:baseline;gap:12px;border-bottom:1px solid #ece8f6;padding:5px 0;font-size:11.8px;}}
.cv-toc .row:last-child{{border-bottom:none;}}
.cv-toc .n{{width:20px;color:#8a83c9;font-weight:700;}}
.cv-toc .nm{{flex:1;font-weight:700;color:#2c3038;}} .cv-toc .nm span{{font-weight:400;color:#8b8fa0;font-size:.9em;margin-left:4px;}}
.cv-toc .pg{{color:#8b8fa0;}}
.cv-stats{{display:flex;gap:9px;margin-top:20px;}}
.cv-st{{background:rgba(255,255,255,.78);border:1px solid #e6e1f5;border-radius:14px;padding:10px 14px;display:flex;align-items:center;gap:10px;flex:1;}}
.cv-st b{{font-size:24px;font-weight:800;color:#c2410c;line-height:1.2;}}
.cv-st span{{font-size:10.5px;color:#5c6170;line-height:1.45;}}
.cv-parts{{position:absolute;left:13mm;right:13mm;bottom:14mm;display:grid;grid-template-columns:repeat(5,1fr);gap:10px;}}
.cv-p{{background:rgba(255,255,255,.88);border-radius:12px;border-top:4px solid #4651c8;padding:8px 12px;}}
.cv-p .a{{font-weight:800;font-size:12.5px;color:#23263a;}} .cv-p .b{{font-size:10.5px;color:#5c6170;margin-top:2px;line-height:1.5;}}
.cv-src{{position:absolute;left:13mm;right:13mm;bottom:7mm;font-size:9.5px;color:#9a9486;}}
.cover2 .ft{{display:none;}}
</style>
<div class="cv-left"><div class="cv-k">PHAR · PHARMACEUTICAL ANALYSIS II · 기말고사 대비 노트</div>
<svg class="cv-h" width="420" height="150" viewBox="0 0 420 150"><defs><linearGradient id="cvg" x1="0" y1="0" x2="1" y2=".6"><stop offset="0" stop-color="#c2410c"/><stop offset="1" stop-color="#5b3fd6"/></linearGradient></defs><text fill="url(#cvg)" font-size="40" font-weight="800" font-family="Pretendard"><tspan x="0" y="38">의약품분석학 II</tspan><tspan x="0" y="85">기말고사 통합</tspan><tspan x="0" y="132">마스터 노트</tspan></text></svg>
<div class="cv-flow">PART 1–4 질량분석법 (Lecture 5) → 크로마토그래피 (Lecture 6~, 추가 예정)</div>
<div class="cv-chips"><span class="cv-chip">상세요약 · 개념 {{NC}}</span><span class="cv-chip">문제 {{NQ}} (다답형·서술·계산·빈칸)</span><span class="cv-chip">족보 7주제 문항화</span><span class="cv-chip">수업 녹음 3회 반영</span><span class="cv-chip">혼동 쌍·숫자 카드</span></div>
<div class="cv-txt"><span class="r">중간고사 실제 출제 = 모의고사와 결은 같고 한 단계 더 어렵게</span> → 이 노트의 객관식은 대부분 <b>다답형(모두 고르기)</b>.<br>
각 개념은 <b>💡 핵심 → 📖 설명 → 📐 공식 → ✍️ 예제 → 🧠 한 줄</b>, 바로 뒤에 그 개념의 문제(왼쪽 문제·풀이칸, 오른쪽 정답·해설).<br>
🗣️ = 수업 녹음에서 교수님이 한 말, <span class="tag j">족보</span> = 작년 기말 복기에 나온 주제.</div>
<div class="cv-stats">
<div class="cv-st"><b>52</b><span>슬라이드<br>Lecture 5</span></div>
<div class="cv-st"><b>7</b><span>족보 주제<br>전부 문항화</span></div>
<div class="cv-st"><b>3</b><span>수업 녹음<br>강조점 반영</span></div>
<div class="cv-st"><b>39</b><span>중간 실제 문항<br>33 · 4 · 2</span></div></div></div>
<div class="cv-toc"><div class="t">CONTENTS</div>
<div class="row"><span class="n">00</span><span class="nm">시험 정보 · 출제 스타일<span>Exam info</span></span><span class="pg">{{PAGE:f-guide}}</span></div>
<div class="row"><span class="n">00</span><span class="nm">족보 · 녹음 체크리스트<span>Checklist</span></span><span class="pg">{{PAGE:f-jokbo}}</span></div>
<div class="row"><span class="n">01</span><span class="nm">질량분석 원리 · 이온화<span>EI · CI · RP</span></span><span class="pg">{{S:{P1}}}</span></div>
<div class="row"><span class="n">02</span><span class="nm">질량 스펙트럼 해석<span>N rule · DBE · isotope</span></span><span class="pg">{{S:{P2}}}</span></div>
<div class="row"><span class="n">03</span><span class="nm">질량분석관<span>Quadrupole · TOF</span></span><span class="pg">{{S:{P3}}}</span></div>
<div class="row"><span class="n">04</span><span class="nm">LC-MS · 탠덤 MS<span>ESI · APCI · SRM</span></span><span class="pg">{{S:{P4}}}</span></div>
<div class="row"><span class="n">✓</span><span class="nm">혼동 쌍 · 숫자 · 공식<span>Final review</span></span><span class="pg">{{PAGE:f-pairs}}</span></div></div>
<div class="cv-parts">
<div class="cv-p" style="border-top-color:#4651c8"><div class="a">PART 1 원리·이온화</div><div class="b">m/z · 질량 3종 · EI · CI · 분해능 · HRMS</div></div>
<div class="cv-p" style="border-top-color:#12937a"><div class="a">PART 2 스펙트럼 해석</div><div class="b">질소 규칙 · DBE · 동위원소 · 조각화</div></div>
<div class="cv-p" style="border-top-color:#d6336c"><div class="a">PART 3 질량분석관</div><div class="b">사중극자 · 안정성 도표 · TOF · 리플렉트론</div></div>
<div class="cv-p" style="border-top-color:#c2410c"><div class="a">PART 4 LC-MS·탠덤</div><div class="b">ESI · APCI · TIC/SIM/EIC · QQQ · SRM</div></div>
<div class="cv-p" style="border-top-color:#9aa0b0"><div class="a">PART 5~ 크로마토그래피</div><div class="b">강의가 끝나면 이어서 추가</div></div></div>
<div class="cv-src">의약품분석학II Lecture 5 강의자료 · Lecture 5 번역·상세설명 · 족보(중간·기말 복기, 2025-2 기말 주관식 복기) · 기말 대비 수업 녹음 3회 · 2026-2 중간고사 실제 출제 형식을 바탕으로 정리</div>
""")

guide = dict(t="r", id="f-guide", html=f"""
<div class="hd"><span class="bd">읽기 전에 ①</span><div class="tt"><h1>시험 정보 · 출제 스타일 · 이 노트 쓰는 법</h1><div class="sb">Exam info · how this note is built</div></div><span class="pt">{P0}</span></div>
<div class="body"><div class="main">
<div class="sec">📅 기말고사</div>
<table class="t"><tr><th>범위</th><td>Lecture 5 질량분석법 전체 + Lecture 6 크로마토그래피 ~ (마지막 수업까지). <b>일시·장소는 공지 후 이 표에 갱신</b></td></tr>
<tr><th>예상 형식</th><td>중간고사와 같은 틀: <b>객관식(단답형 + 다답형 혼합)</b> · 주관식 단답 · <b>서술형</b></td></tr></table>
<div class="sec">🎯 중간고사에서 확인된 출제 스타일 (2026-2 실제 시험)</div>
<ul><li>총 39문제 = <b>객관식 33</b> + 주관식 단답 4 + <b>서술형 2</b></li>
<li>객관식은 답이 하나인 문제와 <pk>여러 개인 다답형을 섞어서</pk> → 몇 개를 골라야 하는지 헷갈리게</li>
<li>모의고사와 결은 비슷하지만 <b>한 단계 더 어렵고 헷갈리게</b> (함정 보기: 단어 하나 바꿔치기, 정의 뒤집기)</li>
<li>서술형은 <b>“차이점”, “이유”</b>를 묻는 형식 (원자 vs 분자 스펙트럼 차이, 형광이 농도에 비례하지 않는 이유)</li></ul>
<div class="sec">✏️ 이 노트의 구성</div>
<ul><li>개념 → 그 개념의 문제 순서. 문제는 <b>왼쪽에서 먼저 풀고</b> 오른쪽 해설 확인</li>
<li>객관식은 대부분 <b>다답형</b>(실전처럼), 서술형은 족보·녹음 강조점으로 <b>모범 답안</b>까지</li>
<li>보기 해설에 “왜 틀렸나”를 한 줄씩 → 함정 패턴을 몸에 익히기</li></ul></div>
<div class="side">
<div class="card tip"><div class="ct">🗣️ 교수님이 직접 강조한 것 (녹음)</div>
• 사중극자: “DC와 RF를 <b>동시에</b>, <b>비율을 유지하면서</b> 바꾼다 — 왜 자꾸 이 얘기를 하겠어요? <b>시험에 내려고</b>” → {{REF:c-stab}}<br>
• 동위원소: “시험 기간에 <b>동위원소 확률 계산표를 제공</b>할 테니 M+1, M+2를 계산할 수 있어야” → {{REF:q-iso}}<br>
• ESI vs APCI: “이온화 매질, 휘발성 필요 여부 기본 차이는 잘 알아 두기를” → {{REF:c-apci}}<br>
• “SIM 모드와 EIC를 <b>구분할 줄 알아야</b>” → {{REF:c-sim}}<br>
• SRM: “이 <b>선택</b>이란 단어가 중요해요”, “중요한 건 <b>S/N</b>” → {{REF:c-srm}}<br>
• 탠덤: “적어도 탠덤 질량분석기가 뭔지, <b>왜 하는지</b> 기본 이유는 알아야”</div>
<div class="card trap"><div class="ct">⚠️ 다답형 푸는 법</div>보기마다 O/X를 <b>따로</b> 판단하고, 하나라도 애매하면 해당 개념 페이지의 ‘함정’ 카드로 돌아가기. “항상/직접/모든” 같은 단어가 들어간 보기는 의심부터.</div>
</div></div>""")

jokbo = dict(t="r", id="f-jokbo", html=f"""
<div class="hd"><span class="bd">읽기 전에 ②</span><div class="tt"><h1>족보 · 녹음 체크리스트 — 어디서 다시 보나</h1><div class="sb">Past-exam map</div></div><span class="pt">{P0}</span></div>
<div class="body"><div class="main">
<table class="t"><tr><th>작년 기말 기출(복기) — 질량분석</th><th>유형</th><th>이 노트에서</th></tr>
<tr><td>Resolving power · Resolution</td><td>객관·계산</td><td>{{REF:c-rp}} · {{REF:q-rp}}</td></tr>
<tr><td>Nitrogen rule</td><td>객관·빈칸</td><td>{{REF:c-nrule}} · {{REF:q-nrule}}</td></tr>
<tr><td>Isotope pattern</td><td>계산</td><td>{{REF:c-iso1}} · {{REF:c-iso2}} · {{REF:q-iso}}</td></tr>
<tr><td>Degree of unsaturation (DBE)</td><td>계산</td><td>{{REF:c-dbe}} · {{REF:q-nrule}}</td></tr>
<tr><td>High resolution (같은 명목질량 구별)</td><td>계산</td><td>{{REF:c-hrms}} · {{REF:q-rp}}</td></tr>
<tr><td>TOF</td><td>객관·계산</td><td>{{REF:c-tof}} · {{REF:q-tof}}</td></tr>
<tr><td><b>SIM보다 SRM의 S/N이 큰 이유</b> (2025-2 주관식)</td><td>서술형</td><td>{{REF:c-srm}} · {{REF:q-srm}}</td></tr></table>
<p class="why" style="margin-top:6px">기말 복기의 나머지(Diffusion, van Deemter, open tubular, tailing, 검출기, Resolution 계산)는 크로마토그래피 PART에서 다룰 예정.</p>
</div><div class="side">
<table class="t"><tr><th>녹음 강조</th><th>이 노트에서</th></tr>
<tr><td>정전기력 · 기체 이온 · m/z</td><td>{{REF:c-ms}}</td></tr>
<tr><td>CI 100–200 eV, 준분자 이온</td><td>{{REF:c-ci}}</td></tr>
<tr><td>Resolution = RP로 씀</td><td>{{REF:c-rp}}</td></tr>
<tr><td>동위원소 표 제공 계산</td><td>{{REF:q-iso}}</td></tr>
<tr><td>아세트아미노펜 152 → 110</td><td>{{REF:c-frag}} · {{REF:q-final}}</td></tr>
<tr><td>DC/RF 비율, 기울기</td><td>{{REF:c-stab}} · {{REF:q-quad}}</td></tr>
<tr><td>리플렉트론</td><td>{{REF:c-tof}}</td></tr>
<tr><td>ESI vs APCI</td><td>{{REF:c-apci}} · {{REF:q-esi-sa}}</td></tr>
<tr><td>SIM vs EIC</td><td>{{REF:c-sim}} · {{REF:q-sim}}</td></tr>
<tr><td>QQQ 모드 18 → 6</td><td>{{REF:c-tandem}} · {{REF:q-mode}}</td></tr>
<tr><td>SRM · EE2 3.6 ppt</td><td>{{REF:c-srm}}</td></tr></table>
<div class="card tip"><div class="ct">📌 PART별 위치</div>
PART 1 원리·이온화: {{R:{P1}}}<br>PART 2 스펙트럼 해석: {{R:{P2}}}<br>PART 3 질량분석관: {{R:{P3}}}<br>PART 4 LC-MS·탠덤: {{R:{P4}}}</div>
</div></div>""")

E = [cover, guide, jokbo]
