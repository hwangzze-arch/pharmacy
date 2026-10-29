from parts import *
from svgs import STYLE, FLOW

cover = dict(t="r", cls="cover2", html=f"""
{STYLE}
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
.cv-parts{{position:absolute;left:13mm;right:13mm;bottom:14mm;display:grid;grid-template-columns:repeat(5,1fr);gap:10px;}}
.cv-p{{background:rgba(255,255,255,.85);border-radius:12px;border-top:4px solid #4651c8;padding:8px 12px;box-shadow:0 2px 8px rgba(90,70,170,.08);}}
.cv-p .a{{font-weight:800;font-size:13px;color:#23263a;}} .cv-p .b{{font-size:10.5px;color:#5c6170;margin-top:2px;line-height:1.5;}}
.cv-src{{position:absolute;left:13mm;right:13mm;bottom:7mm;font-size:9.5px;color:#9a9486;}}
.cover2 .ft{{display:none;}}
</style>
<div class="cv-left"><div class="cv-k">PHAR · PHARMACEUTICAL ANALYSIS LAB · 실험 1 · 실험 기초지식</div>
<div class="cv-h">의약품분석학 실험<br>실험 1 뷰렛의 검정<br>마스터 노트</div>
<div class="cv-flow">안전 · 실험노트 → TC/TD · V = m/ρ → 뷰렛 사용법 → 보정치 · 검정곡선</div>
<div class="cv-chips"><span class="cv-chip">상세요약 · 개념 {{NC}}</span><span class="cv-chip">문제 {{NQ}} (객관·서술·계산·빈칸·O/X)</span><span class="cv-chip">유인물 1–5쪽 전부</span><span class="cv-chip">첫 수업 녹취록 반영</span><span class="cv-chip">혼동 쌍·숫자 카드</span></div>
<div class="cv-txt"><span class="r">실험노트 제출 = 다음 주 월요일 18:00</span> · 401호(교수님 실험실) 앞 박스, 늦으면 감점.<br>
<b>기말고사</b>는 실험한 내용에서만 출제 → 이 노트의 문제는 그 대비용.<br>
각 개념은 <b>💡 핵심 → 📖 설명 → 📐 공식 → ✍️ 예제 → 🧠 한 줄</b>, 바로 뒤에 그 개념의 문제(왼쪽 문제·풀이칸, 오른쪽 정답·해설).<br>
교수님이 수업에서 강조한 건 「🎯 녹음」, 유인물 내용은 「유인물」로 표시했어.</div>
<div class="cv-stats">
<div class="cv-st"><b>±0.1</b><span>뷰렛 허용오차<br>(mL, 20 °C)</span></div>
<div class="cv-st"><b>0.01</b><span>눈금 읽는 자리<br>(mL)</span></div>
<div class="cv-st"><b>20</b><span>유출 속도 상한<br>(mL/min)</span></div>
<div class="cv-st"><b>월 18시</b><span>실험노트 제출<br>401호 앞</span></div></div></div>
<div class="cv-toc"><div class="t">CONTENTS</div>
<div class="row"><span class="n">00</span><span class="nm">공지 · 감점 · 이 노트 쓰는 법<span>Notice</span></span><span class="pg">{{PAGE:f-guide}}</span></div>
<div class="row"><span class="n">00</span><span class="nm">오늘 실험 한 장 요약<span>Overview</span></span><span class="pg">{{PAGE:f-over}}</span></div>
<div class="row"><span class="n">01</span><span class="nm">안전 · 실험노트<span>Safety & notebook</span></span><span class="pg">{{S:{P1}}}</span></div>
<div class="row"><span class="n">02</span><span class="nm">검정의 원리 · 측용기<span>Principle · TC/TD</span></span><span class="pg">{{S:{P2}}}</span></div>
<div class="row"><span class="n">03</span><span class="nm">뷰렛 · 저울 사용법<span>Technique</span></span><span class="pg">{{S:{P3}}}</span></div>
<div class="row"><span class="n">04</span><span class="nm">결과 · 검정곡선<span>Data & curve</span></span><span class="pg">{{S:{P4}}}</span></div>
<div class="row"><span class="n">✓</span><span class="nm">혼동 쌍 · 숫자 · 노트 체크리스트<span>Final review</span></span><span class="pg">{{PAGE:f-pairs}}</span></div></div>
<div class="cv-parts">
<div class="cv-p" style="border-top-color:#4651c8"><div class="a">PART 1 안전 · 노트</div><div class="b">안전 수칙 · 위험 요인 · 노트 항목 · 볼펜·간인·여백</div></div>
<div class="cv-p" style="border-top-color:#12937a"><div class="a">PART 2 원리 · 측용기</div><div class="b">검정 목적 · V = m/ρ · 밀도표 · TC/TD · 보정치 부호</div></div>
<div class="cv-p" style="border-top-color:#d6336c"><div class="a">PART 3 사용법</div><div class="b">세척·린싱 · 스톱콕 · 기포 · 메니스커스·시차 · 유출 속도 · 저울</div></div>
<div class="cv-p" style="border-top-color:#9a4a12"><div class="a">PART 4 결과</div><div class="b">우리 조 데이터 · 검정곡선 · 시작·최종 보정</div></div>
<div class="cv-p" style="border-top-color:#f0a020"><div class="a">FINAL</div><div class="b">혼동 쌍 · 숫자 카드 · 노트 No.1 체크리스트</div></div></div>
<div class="cv-src">의약품분석학 실험 「실험 1: 실험 기초지식」 유인물 1–5쪽(안전 수칙 · 실험노트 작성 요령 · 뷰렛의 검정 · 물의 밀도표) · 첫 수업 녹취록(약 104분)을 바탕으로 정리</div>
""")

guide = dict(t="r", id="f-guide", html=f"""
<div class="hd"><span class="bd">읽기 전에 ①</span><div class="tt"><h1>공지 · 감점 포인트 · 이 노트 쓰는 법</h1><div class="sb">Notice · grading · how this note is built</div></div><span class="pt">{P0}</span></div>
<div class="body"><div class="main">
<div class="sec">📅 교수님 공지</div>
<table class="t"><tr><th>노트 제출</th><td>목요일 실험 → <pk>다음 주 월요일 저녁 6시까지</pk>, 401호(교수님 실험실) 앞 박스. 늦으면 감점. 채점해서 다음 실험 시간에 돌려줌.</td></tr>
<tr><th>기말고사</th><td>학기 말, <b>실험한 내용으로만</b> 출제. “열심히 실험하면 다 풀 수 있는 시험.”</td></tr>
<tr><th>학기 일정</th><td>총 7회: ① 뷰렛의 검정(오늘) → ②–⑤ 적정 4종(<b>중화 · 침전 · 킬레이트(EDTA) · 산화환원</b>) → ⑥ 분광 분석 → ⑦ 분리 분석. 적정은 자동적정기 없이 <b>뷰렛으로</b> → 앞으로 한 달간 뷰렛을 계속 씀.</td></tr>
<tr><th>실험실 환경</th><td>냉방만 되고 <b>난방 안 됨</b> → 따뜻하게 입고 오기. 에어컨을 켜도 찬 바람만 나옴.</td></tr>
<tr><th>조교</th><td>한 학기 동안 지도. 복장·태도 체크해서 점수에 반영.</td></tr></table>
<div class="sec">🚫 감점 · 퇴실 포인트 (🎯 녹음)</div>
<ul><li><b>실험복</b> 필수, <b>단추 끝까지</b> 잠그기 (안 잠그면 걸려 넘어짐).</li>
<li><pk>슬리퍼 · 반바지 절대 불가</pk> → 감점 및 퇴실 가능.</li>
<li>실험 중 <b>휴대폰 사용 금지</b>.</li>
<li>적정할 때 용액이 <b>“주르륵” 연속으로 흐르면 감점</b> → 반드시 똑, 똑, 똑.</li>
<li>노트 지각 제출 감점. 노트 형식 규칙 위반(연필·화이트 등) → {{REF:c-format}}.</li></ul>
</div><div class="side">
<div class="card tip"><div class="ct">📌 이 노트 사용법</div><ol style="margin:0"><li>개념 페이지를 한 번 정독 (💡→📖→📐→✍️→🧠)</li><li>바로 뒤 문제 페이지에서 <b>오른쪽을 가리고</b> 왼쪽 빈칸에 직접 풀기</li><li>틀린 문제는 해설의 “👉 왜?” 줄만 다시 읽기</li><li>실험노트 쓰기 직전: 맨 끝 「노트 No.1 체크리스트」</li></ol></div>
<div class="card"><div class="ct">🖍 표시 약속</div><y>노랑 = 핵심 개념</y> · <g>초록 = 공식·결론</g> · <pk>분홍 = 시험 포인트·함정</pk><br><span class="tag j">🎯 녹음</span>교수님이 수업에서 강조 · <span class="tag h">유인물</span>유인물 원문 · <span class="tag s">우리 조</span>오늘 우리 조 데이터<br><span class="term" style="display:inline-block;margin-top:4px">＊[용어: …] = 처음 보는 말 풀이</span></div>
<div class="card trap"><div class="ct">⚠️ 데이터 주의</div>「우리 조」 숫자는 <b>녹취록(AI 전사)</b>에서 가져온 값이야. 전사 오류가 있을 수 있으니 실험노트에는 단톡방에 올라온 <b>실제 기록지 사진</b>의 값을 써.</div>
</div></div>""")

over = dict(t="r", id="f-over", html=f"""
<div class="hd"><span class="bd">읽기 전에 ②</span><div class="tt"><h1>오늘 실험 한 장 요약 — 뷰렛, 정말 ±0.1 mL만큼 정확해?</h1><div class="sb">Experiment 1 at a glance</div></div><span class="pt">{P0}</span></div>
<div class="core"><span class="lb">💡 한 줄 요약</span>뷰렛에서 흘려보낸 물의 <b>무게</b>를 재서 <b>밀도로 나눠 “진짜 부피”</b>를 구하고, 읽은 눈금과의 차이(<b>보정치</b>)를 그래프로 그려 뷰렛이 제조사 보증(±0.1 mL) 안에 드는지 확인한다.</div>
<div class="body"><div class="main">
<div class="sec">🔁 실험 흐름</div>
{FLOW}
<div class="fbox"><div class="sec f">📐 오늘의 공식 2개</div>
<span class="fx">실제 부피 V = 물 무게 m ÷ 물의 밀도 ρ(수온)</span><br>
<span class="fx">보정치 = 실제 부피 − 뷰렛 눈금</span> &nbsp;→ 검정곡선: <g>x축 = 눈금, y축 = 보정치</g></div>
<div class="sec">🧪 오늘 한 일 (순서)</div>
<ol><li>뷰렛 준비: 세척·린싱, 스톱콕 조임 조절, 누출 확인</li>
<li>탈이온수 채우고 <b>기포 제거</b> → 0.00 mL에 맞춤</li>
<li>빈 삼각플라스크 무게 측정 (같은 저울을 끝까지)</li>
<li>약 10 mL씩 <b>한 방울씩</b> 받아 눈금(0.01까지)과 무게 기록 → 50 mL까지 누적</li>
<li>실제 부피·보정치 계산 → 검정곡선</li>
<li>뒷정리: 폐액 → 수돗물 → 탈이온수 헹굼 → 스톱콕 열고 <b>거꾸로 걸어</b> 자연건조</li></ol>
</div><div class="side">
<div class="card ana"><div class="ct">🎈 비유</div>뷰렛 검정 = <b>새 자(ruler)를 믿기 전에 표준 자와 대 보는 것</b>. 저울(아주 정확한 표준)로 뷰렛(자)의 눈금이 맞는지 구간마다 확인하고, 틀린 만큼을 “보정표”로 만들어 두는 거야.</div>
<div class="card tip"><div class="ct">📌 시험 포인트</div>① 검정 목적 ② V = m/ρ ③ 보정치 = 실제 − 눈금 (부호!) ④ 검정곡선 축 ⑤ TC vs TD ⑥ 0.01 mL까지 읽기 ⑦ 시차오차 방향 ⑧ 20 mL/min ⑨ 기포 ⑩ 시작·최종 둘 다 보정</div>
<div class="card"><div class="ct">🧾 시약 및 기구 <span class="tag h">유인물</span></div>buret (50 mL) &amp; stand, buret holder, Erlenmeyer flask (100 mL), beaker (100 mL), washing bottle, chemical balance, 탈이온수(시약 = 물이라 오늘은 장갑 불필요)</div>
</div></div>""")

E = [cover, guide, over]
