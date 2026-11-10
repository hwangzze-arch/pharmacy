from parts import *

cover = dict(t="r", id="f-cover", cls="cvx", html="""
<style>
.page.cvx{padding:0;flex-direction:row;background:#fbf9f4;}
.cvx .lp{width:92mm;flex:none;height:100%;background:linear-gradient(170deg,#f08c3c 0%,#d9531e 34%,#a8381a 66%,#5e2a1c 100%);color:#fff;padding:14mm 8mm 12mm 10mm;display:flex;flex-direction:column;}
.cvx .lp .s{font-size:12px;font-weight:700;opacity:.9;letter-spacing:.06em;}
.cvx .lp .k{letter-spacing:.32em;font-size:12px;font-weight:700;opacity:.92;margin-top:5mm;}
.cvx .lp .big{display:flex;align-items:flex-end;gap:3px;margin-top:3mm;line-height:.9;white-space:nowrap;}
.cvx .lp .big b{font-size:94px;font-weight:800;letter-spacing:-4px;}
.cvx .lp .big span{font-size:34px;font-weight:800;margin-bottom:9px;}
.cvx .lp h1{font-size:26px;line-height:1.3;margin:7mm 0 3px 0;font-weight:800;}
.cvx .lp .en{font-size:11.5px;opacity:.85;line-height:1.45;}
.cvx .lp .pill{display:inline-block;margin-top:4mm;background:#fff;color:#a8381a;border-radius:14px;padding:3px 12px;font-size:12px;font-weight:800;align-self:flex-start;}
.cvx .lp .chips{margin-top:5mm;display:flex;flex-direction:column;gap:5px;font-size:11px;}
.cvx .lp .chips span{background:rgba(255,255,255,.16);border:1px solid rgba(255,255,255,.3);border-radius:8px;padding:3px 9px;}
.cvx .lp .stt{margin-top:auto;font-size:12.5px;line-height:1.75;}
.cvx .lp .stt b{font-size:19px;font-weight:800;}
.cvx .rp{flex:1;min-width:0;padding:10mm 11mm 11mm 9mm;display:flex;flex-direction:column;}
.cvx .rh{display:flex;align-items:baseline;gap:10px;border-bottom:1px solid #dfe5ee;padding-bottom:5px;}
.cvx .rh h2{margin:0;font-size:15px;color:#5e2a1c;}
.cvx .rh span{font-size:10.5px;color:#6b7686;}
.cvx .toc{flex:1;min-height:0;display:grid;grid-template-columns:1fr 1fr;column-gap:16px;margin-top:5px;grid-auto-flow:column;grid-template-rows:repeat(var(--rows),1fr);}
.cvx .tr{display:flex;align-items:center;gap:7px;border-bottom:1px solid #eef1f5;font-size:11px;min-width:0;line-height:1.3;}
.cvx .tr .bg{flex:none;width:30px;text-align:center;border-radius:8px;font-size:9.5px;font-weight:700;color:#fff;padding:1px 0;}
.cvx .bg.g{background:#8b8fa0;} .cvx .bg.c{background:#d9531e;} .cvx .bg.q{background:#127a64;} .cvx .bg.f{background:#7a4a2a;}
.cvx .tr .nm{flex:none;width:40px;font-weight:700;color:#5e2a1c;}
.cvx .tr .ti{flex:1;min-width:0;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;color:#2c3038;}
.cvx .tr .pg{flex:none;font-weight:700;color:#6b7686;width:26px;text-align:right;}
.cvx .tr.part{border-bottom:none;font-weight:700;color:#c2410c;font-size:10.5px;letter-spacing:.03em;}
.cvx .ft{left:auto;right:11mm;width:auto;border-top:none !important;}
.cvx .ft span:not(:last-child){display:none;}
</style>
<div class="lp"><div class="s">약품생화학 · 기말 대비 노트</div><div class="k">CHAPTER</div>
<div class="big"><b>19–20</b><span>장</span></div>
<h1>산화적 인산화<br>· 광인산화<br>· 탄소 고정</h1><div class="en">Oxidative Phosphorylation · Photophosphorylation · Carbon Assimilation (Lehninger)</div>
<div class="pill">시험대비 요약노트 (TB추가)</div>
<div class="chips"><span>호흡사슬 Complex I–IV · ATP 합성효소</span><span>조절 · 활성산소 · 갈색지방 · 세포자멸사</span><span>명반응 PSII/PSI · Z 도식 · 캘빈 회로</span></div>
<div class="stt">개념 <b>{NC}</b> · 문제 <b>{NQ}</b><br>교수님 TB {NTB} · 🎤 수업 1–5 반영<br>p.1–{TOTAL}</div></div>
<div class="rp"><div class="rh"><h2>목차</h2><span>개념 = 개념 쪽 · 문제 = 그 파트 문제 묶음(개념확인 + 교수님 TB)</span></div>
<div class="toc">{TOC}</div></div>""")
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

from lecture import LEC, CLASS
_KEY = {
    1: [("“<b>4+4+2, 전자 2개당</b>으로 기억” — 영상 숫자는 틀렸다", "c-sum"), ("순서 정하는 방법 중 <b>3번(억제제)이 중요</b>", "c-order"), ("Complex I 펌프 원리는 <b>가설</b>", "c-c1")],
    2: [("에너지가 드는 건 ATP <b>방출</b> (K′eq 2.4, ΔG ≈ 0)", "c-f1cat"), ("<b>한 바퀴 = ATP 3</b>, 실제 NADH 2.5 (ANT 비용)", "c-po"), ("숙신산 → CN⁻ → DNP 그래프", "c-coupling")],
    3: [("수용체 조절비 &gt; 10, 질량작용비", "c-regul"), ("IF₁ 이량체(저산소, pH ↓)", "c-if1"), ("소단원 요약 6줄: 열발생 · P450 · 세포자멸사 · mtDNA · 질환 · 당뇨", "c-mtdna")],
    4: [("★ “<b>핵심</b>”: 미토 vs 엽록체 — H⁺ 방향 · O₂/H₂O 역할 · 에너지원", "c-photophos"), ("PSII: P680 → Pheo → PQ / Tyr ← Mn ← 물", "c-psii"), ("cyt b₆f ≈ III, 플라스토시아닌(Cu) ≈ cyt c", "c-psi")],
    5: [("순환 = ATP만, “<b>기억해 두면 되겠습니다</b>”", "c-zscheme"), ("탄소 15 + 3 = 18, 인산 1개는 ATP가", "c-calvin"), ("루비스코 라이신 카바모일화 + Mg²⁺", "c-rubisco")],
}
_WHAT = {1: "19.1 전자전달 사슬", 2: "셔틀 · 19.2 ATP 합성", 3: "19.3 조절 · 19.4–19.5 미토콘드리아", 4: "광합성 명반응", 5: "광계 II 영상 · 캘빈 회로"}
_rows = ""
for n in CLASS:
    ids = [k for k, v in LEC.items() if any(x[0] == n for x in v)]
    key = "".join(f"<li>{t} — {{{{REF:{i}}}}}</li>" for t, i in _KEY[n])
    _rows += f'<tr><td><b>수업{n}</b><br>{CLASS[n]}<br><span class="ko">{_WHAT[n]}</span></td><td><ul style="margin:0">{key}</ul></td><td style="font-size:.86em">' + " · ".join(f"{{{{REF:{i}}}}}" for i in ids) + "</td></tr>"
_rows = _rows.replace("{{", "{").replace("}}", "}")
lecpage = dict(t="r", id="f-lec", html=f"""
<div class="hd"><span class="bd">읽기 전에 ①-2</span><div class="tt"><h1>🎤 교수님 강조 체크리스트 — 기말 대비 수업 1–5</h1><div class="sb">녹취록에서 교수님이 직접 짚은 것 · 해당 개념 페이지 오른쪽의 파란 「🎤 수업 강조」 상자에 시각과 함께 있어</div></div><span class="pt">{P0}</span></div>
<div class="body"><div class="main full">
<table class="t"><tr><th style="width:13%">수업</th><th style="width:52%">교수님이 직접 강조·정정한 것</th><th>🎤 상자가 있는 개념</th></tr>{_rows}</table>
<div class="card trap" style="margin-top:6px"><div class="ct">⚠️ 강의 말과 교재가 다른 곳 (해당 🎤 상자에 ⚠️로 표시)</div>질량작용비 정의 [ATP]/([ADP][Pᵢ]) · IF₁ 역주행 조건 · 해독 P450은 주로 소포체 · 아드레노독신 환원효소(FAD) · 회전 관측은 형광현미경 · 영상의 H⁺ 3개/ATP · 광자 4개 vs 8개 · 루비스코 산물은 3PG · F₁ 방향(틸라코이드 안팎)</div>
<div class="small" style="margin-top:6px">원본: 약품생화학 폴더의 「기말고사 대비 수업1–5 정리.pdf」 (수업3은 동영상 강의). 기말고사 범위는 <b>23장까지</b> (수업5 공지).</div>
</div></div>""")

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

E = [cover, guide, lecpage, story, bigmap]
