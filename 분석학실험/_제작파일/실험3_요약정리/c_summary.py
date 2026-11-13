# -*- coding: utf-8 -*-
"""실험3 모어법(Mohr method)에 의한 NaCl 정량 — 실험1·2 요약정리와 같은 양식 (유인물 1쪽 + 녹취록)"""
from svgs import STYLE


def card(kind, title, body):
    return f'<div class="card {kind}"><div class="ct">{title}</div>{body}</div>'


def prof(body):
    return card("prof", "🎙 교수님 말씀", body)


def pg(pid, bd, title, sub, part, main, side="", core=""):
    core = f'<div class="core"><span class="lb">💡 핵심</span>{core}</div>' if core else ""
    body = f'<div class="main{"" if side else " full"}">{main}</div>' + (f'<div class="side">{side}</div>' if side else "")
    return dict(t="r", id=pid, html=f'''<div class="hd"><span class="bd">{bd}</span><div class="tt"><h1>{title}</h1><div class="sb">{sub}</div></div><span class="pt">{part}</span></div>
{core}<div class="body">{body}</div>''')


K0, K1, K2, K3 = "공지 · 한눈에", "목적 · 원리", "방법 · 조작", "계산 · 고찰"

FLOW = """<svg viewBox="0 0 680 190" class="svgf">
<g class="box"><rect x="4" y="10" width="150" height="62" rx="8"/><rect x="190" y="10" width="150" height="62" rx="8"/>
<rect x="376" y="10" width="140" height="62" rx="8"/><rect x="552" y="10" width="124" height="62" rx="8" class="hl"/>
<rect x="4" y="112" width="150" height="62" rx="8"/><rect x="190" y="112" width="150" height="62" rx="8"/>
<rect x="376" y="112" width="140" height="62" rx="8"/><rect x="552" y="112" width="124" height="62" rx="8" class="hl"/></g>
<g class="bt"><text x="79" y="36">NaCl 표준품 ≈ 0.584 g</text><text x="79" y="56">→ 100 mL (f′ 계산)</text>
<text x="265" y="36">20.00 mL 분취</text><text x="265" y="56">+ 물 약 40 mL + K₂CrO₄</text>
<text x="446" y="36">AgNO₃ 적정 ①</text><text x="446" y="56">+ 공시험 ②</text>
<text x="614" y="36">AgNO₃의 f</text><text x="614" y="56">(셋째 자리)</text>
<text x="79" y="138">시판 소금 ≈ 0.1 g</text><text x="79" y="158">정밀 칭량</text>
<text x="265" y="138">탈이온수 50 mL</text><text x="265" y="158">+ K₂CrO₄ 지시약</text>
<text x="446" y="138">AgNO₃ 적정 ③</text><text x="446" y="158">+ 공시험 ④</text>
<text x="614" y="138">NaCl 함량</text><text x="614" y="158">(%)</text></g>
<g class="ar"><path d="M156 41 h30"/><path d="M342 41 h30"/><path d="M518 41 h30"/>
<path d="M156 143 h30"/><path d="M342 143 h30"/><path d="M518 143 h30"/><path d="M614 74 v34"/></g>
<text x="626" y="96" class="sm">f 사용</text>
<text x="4" y="104" class="sm okt">① 표정 (AgNO₃의 진짜 농도)</text>
<text x="4" y="188" class="sm okt">② 시판 소금 중 NaCl 정량</text>
</svg>"""

cover = dict(t="r", cls="cover2", html=STYLE + """
<style>
.cover2{background:radial-gradient(ellipse at 0% 0%,#ffd9e8 0%,rgba(255,217,232,0) 45%),radial-gradient(ellipse at 100% 0%,#dcd6ff 0%,rgba(220,214,255,0) 50%),radial-gradient(ellipse at 100% 100%,#d4f5e6 0%,rgba(212,245,230,0) 50%),radial-gradient(ellipse at 40% 60%,#dfe6ff 0%,rgba(223,230,255,0) 60%),#f4f1fb !important;}
.cv-k{letter-spacing:.32em;font-size:11px;font-weight:700;color:#7d74c9;margin-top:6mm;}
.cv-h{font-size:36px;line-height:1.2;font-weight:800;margin:10px 0 12px 0;background:linear-gradient(120deg,#5b3fd6,#3f57d8);-webkit-background-clip:text;background-clip:text;color:transparent;}
.cv-flow{font-size:14.5px;color:#2c3038;margin-bottom:12px;}
.cv-txt{font-size:12.6px;line-height:1.75;color:#3a3f4b;}
.cv-eq{display:inline-block;margin-top:10px;background:#fff;border:1px solid #e3def3;border-radius:12px;padding:8px 16px;font-weight:700;font-size:13.5px;color:#3d2a73;box-shadow:0 1px 3px rgba(80,60,160,.08);line-height:1.7;}
.cv-toc{position:absolute;right:13mm;top:12mm;width:105mm;background:rgba(255,255,255,.82);border:1px solid #e6e1f5;border-radius:14px;padding:12px 18px 8px 18px;box-shadow:0 4px 18px rgba(90,70,170,.12);}
.cv-toc .t{letter-spacing:.25em;font-size:10px;font-weight:700;color:#5b4fc0;margin-bottom:4px;}
.cv-toc .row{display:flex;align-items:baseline;gap:12px;border-bottom:1px solid #ece8f6;padding:4px 0;font-size:11.8px;}
.cv-toc .row:last-child{border-bottom:none;}
.cv-toc .n{width:20px;color:#8a83c9;font-weight:700;}
.cv-toc .nm{flex:1;font-weight:700;color:#2c3038;}
.cv-toc .pg{color:#8b8fa0;}
.cv-left{width:163mm;}
.cv-src{position:absolute;left:13mm;right:13mm;bottom:7mm;font-size:9.5px;color:#9a9486;}
.cover2 .ft{display:none;}
</style>
<div class="cv-left"><div class="cv-k">의약품분석학 실험 · 실험 3 · 침전 적정 (은적정)</div>
<div class="cv-h">실험 3.<br>모어법에 의한<br>염화나트륨(NaCl) 정량</div>
<div class="cv-flow">자료: 실험3 유인물 1쪽 + 수업 녹취록(약 86분) 요약</div>
<div class="cv-txt"><b>한 줄 요약</b> — NaCl 표준품으로 만든 표준액(f′)으로 <b>AgNO₃ 용액을 표정</b>해 f를 구하고,
그 AgNO₃로 <b>시판 소금</b>을 적정해 들어 있는 <b>Cl⁻을 NaCl로 환산한 함량(%)</b>을 구한 실험. 지시약은 <b>K₂CrO₄</b>(모어법).</div>
<div class="cv-eq">Ag⁺ + Cl⁻ → AgCl↓ (흰색) &nbsp;·&nbsp; 종말점: 2Ag⁺ + CrO₄²⁻ → Ag₂CrO₄↓ (적갈색)<br>
⚠ AgNO₃ 규정 농도는 0.1 M이 아니라 <b>0.2 M</b> (수업 중 정정)</div></div>
<div class="cv-toc"><div class="t">CONTENTS</div>
<div class="row"><span class="n">0</span><span class="nm">공지 · 노트 피드백 · 지난 결과</span><span class="pg">{PAGE:p-notice}</span></div>
<div class="row"><span class="n">0</span><span class="nm">오늘 한 일 한눈에 (적정 4번)</span><span class="pg">{PAGE:p-over}</span></div>
<div class="row"><span class="n">1</span><span class="nm">목적 · 은적정은 Cl⁻ 정량</span><span class="pg">{PAGE:p-purpose}</span></div>
<div class="row"><span class="n">2</span><span class="nm">원리 ① 모어법 · K₂CrO₄ 지시약 · 종말점</span><span class="pg">{PAGE:p-mohr}</span></div>
<div class="row"><span class="n">2</span><span class="nm">원리 ② 공시험(blank test)</span><span class="pg">{PAGE:p-blank}</span></div>
<div class="row"><span class="n">2</span><span class="nm">원리 ③ 계산식 — f′, f, 대응량, 함량</span><span class="pg">{PAGE:p-calcf}</span></div>
<div class="row"><span class="n">3</span><span class="nm">실험방법 — 실제로 한 대로</span><span class="pg">{PAGE:p-meth}</span></div>
<div class="row"><span class="n">4</span><span class="nm">조작 요령 · 교수님 시연</span><span class="pg">{PAGE:p-tips}</span></div>
<div class="row"><span class="n">5</span><span class="nm">1조 결과 (실험노트 값)</span><span class="pg">{PAGE:p-calc}</span></div>
<div class="row"><span class="n">6</span><span class="nm">고찰 포인트 — 원인 · 대책 · 개선</span><span class="pg">{PAGE:p-disc}</span></div>
<div class="row"><span class="n">7</span><span class="nm">기말 대비 Q&amp;A · 노트 체크리스트</span><span class="pg">{PAGE:p-qa}</span></div></div>
<div class="cv-src">의약품분석학 실험 「실험 3: 모어법에 의한 NaCl 정량」 유인물 1쪽 · 수업 녹취록</div>
""")

notice = pg("p-notice", "공지", "실험노트 피드백 · 지난 결과 · 다음 주 안내", "실험 2 노트 채점 후 교수님 피드백", K0,
main=card("trap", "✍️ 실험노트 피드백 (이번부터 감점)", """<ul style="margin:0">
<li><b>실험 원리를 최소 반 페이지</b>. 유인물을 주저리주저리 다 옮기지 말고, <b>제목과 정확히 맞는 핵심</b>만. 원리를 알아야 재현할 수 있다. (더 많이 쓰는 건 OK)</li>
<li>재현할 수 없는 노트는 <b>이미 감점</b>했다. 노트의 가장 큰 목적 = 다른 사람이 재현.</li>
<li><b>페이지 번호는 책처럼 계속 이어서</b>. 실험이 바뀌어도 1페이지부터 다시 시작하지 말 것 (같은 페이지가 여러 개 나오면 안 됨).</li>
<li>실험방법은 <b>유인물이 아니라 실제로 한 대로</b>. CO₂ 제거 안 했는데 "CO₂ 제거된 물"이라고 쓰면 <b>감점</b>. 칭량량이 달랐으면 <b>실제 칭량값</b>.</li>
<li>물은 <b>"증류수"가 아니라 "탈이온수"</b> (끓여서 식힌 물도 아님). 이미 만들어 준 지시약·AgNO₃는 <b>"제공된 …을 사용했다"</b>고 쓸 것 (직접 만들었다고 쓰면 틀림).</li>
<li>규정도계수는 <b>소수점 이하 셋째 자리까지만</b> (넘게 쓴 사람 있었음).</li></ul>"""),
side=card("tip", "📊 지난주(실험 2) 정답", """식초는 <b>6 v/v%</b>(빙초산 희석), 밀도 <b>1.05</b> → <b>6 × 1.05 = 6.3 w/v%</b>.<br>
조별 결과 6.2–6.45 w/v% → "적정이 이렇게 정확하다." <span class="ko">(1조 6.44 w/v% → 정답 대비 +2.2%)</span>""")
 + card("", "💧 다음 주: 물의 경도 측정", "궁금한 물(정수기·수돗물·생수·기숙사 물)을 <b>생수병에 약 500 mL</b> 가져오면 그 물로 실험. 안 가져오면 실험실(조치원) 수돗물. 작년 선배는 에비앙을 측정 — \"비싼 물이 경도가 낮지는 않더라.\"")
 + prof("실험 노트를 쓰는 가장 큰 목적은 그 실험 노트를 가지고 다른 사람들이 여러분의 실험 결과를 재현하기 위한 거예요."))

over = pg("p-over", "한눈에", "오늘 한 일 — 표정 → 시판 소금 정량 (적정 4번)", "Overview", K0,
core="침전 적정(은적정) 중 <b>모어법</b>. ① NaCl 표준액으로 AgNO₃의 <b>f</b>를 구하고 ② 시판 소금의 NaCl 함량을 구한다. 각각 <b>공시험</b>을 해서 적정은 총 <b>4번</b>.",
main=FLOW + """<div class="sec">🧂 표준품과 시료</div>
<ul><li><b>NaCl 표준품</b>: 순도 99% 시약 → <b>100%(일차표준물질)로 가정</b>하고 계산. 99%로 계산하지 말 것.</li>
<li><b>시료</b>: 가정에서 쓰는 <b>시판 테이블 솔트</b>. 수분·다른 염이 있으니 100%보다 낮게 나와야 정상.</li>
<li><b>AgNO₃</b>: 조교가 그날 아침 만든 용액(갈색 병, 조별 약 100 mL) → <b>표준액이 아님</b>(표정 안 됨) → 직접 f를 구해야 함.</li></ul>""",
side=card("trap", "⚠️ AgNO₃ 농도 정정 (수업 중 공지)", "규정 농도가 <b>0.1 M이 아니라 0.2 M</b> (조교가 잘못 만듦). → 적정량이 예상의 절반(약 10 mL)이어도 놀라지 말 것. <b>모든 계산을 0.2 M으로</b>. 고찰에 언급.")
 + card("trap", "⚠️ 생략·변경된 것 (= 고찰거리)", """<ul style="margin:0">
<li>NaCl 표준품 100–120 °C 2시간 건조 → <b>생략</b></li>
<li>NaCl 표준품 순도 99% → 100%로 가정</li>
<li>5% K₂CrO₄ 지시액 · AgNO₃ 용액 조제 → <b>제공됨</b></li>
<li>표정 · 시료 적정 3회 반복 → <b>1회만</b></li></ul>"""))

purpose = pg("p-purpose", "1", "목적 · 은적정은 사실 Cl⁻ 정량", "침전 적정 · Argentometry", K1,
core="AgNO₃ 표준액으로 <b>Cl⁻</b>을 적정하고, 그 양을 <b>NaCl로 환산</b>한다. \"NaCl 정량\"은 엄밀히는 틀린 말 — 물에 녹아 Cl⁻을 내는 <b>모든 물질</b>(예: KCl)이 함께 정량된다.",
main="""<div class="sec">원리 (유인물)</div>
<p>pH 6.5~10.5 사이에서 Cl⁻ ion을 AgNO₃ 표준액으로 적정하면 AgCl이 침전되며, 지시약으로 넣은 K₂CrO₄는 Cl⁻이 모두 AgCl로 침전한 후 과량의 Ag⁺와 반응하여 Ag₂CrO₄의 적갈색 침전을 형성하는데, 이 적갈색 침전이 형성되는 때를 반응 종말점으로 한다.</p>
<p class="ko"><b>시약 및 기구</b>: 분석저울, magnetic stirrer, Erlenmeyer flask (200 mL), volumetric flask (100 mL), buret (50 mL), transfer pipet (10 mL), mess cylinder (100 mL), stand, clamp, 세척병, NaCl, AgNO₃, K₂CrO₄</p>
<div class="sec">적정 반응</div>
<div class="fbox"><span class="fx">NaCl + AgNO₃ → AgCl↓ (흰색) + NaNO₃</span> &nbsp; (Ag⁺ + Cl⁻ → AgCl)<br>
<ul style="margin:4px 0 0"><li><b>1 : 1 몰비</b> → 계산이 편하다.</li>
<li>AgCl의 용해도곱 K<sub>sp</sub> ≈ <b>10⁻¹⁰</b> (1.8 × 10⁻¹⁰) → 물에 거의 안 녹음 → 평형상수가 매우 커서 종말점에서 반응이 완결된다.</li>
<li>한 방울 들어가자마자 <b>우유 빛깔의 흰색 침전</b>이 계속 생긴다.</li></ul></div>
<div class="sec">총산도와 같은 논리</div>
<p>실험 2에서 모든 유기산을 초산으로 간주했듯이, 여기서는 모든 Cl⁻을 NaCl에서 온 것으로 간주한다. 소금의 Cl⁻은 거의 대부분 NaCl에서 나오므로 그렇게 쓰는 것뿐.</p>""",
side=prof("실제로는 NaCl을 정량하는 게 아니고 클로라이드를 정량하는 거예요. 클로라이드를 제공할 수 있는 모든 화합물은 다 정량이 되는 거죠. 소금 중에 뭐가 있을까요? — KCl 같은 거.")
 + card("ana", "🎈 비유", "출석부의 <b>\"김\"씨를 다 세고</b> \"김철수 반 학생 수\"라고 부르는 것. 실제로는 김영희도 섞여 있지만, 대부분이 김철수 반이라면 그렇게 불러도 크게 틀리지 않는다."))

mohr = pg("p-mohr", "2-①", "모어법 — K₂CrO₄ 지시약과 종말점", "Mohr method · 목시 적정", K1,
core="Cl⁻이 다 소모되면 다음 Ag⁺이 <b>CrO₄²⁻</b>와 반응해 <b>적갈색 Ag₂CrO₄</b> 침전 → 흰 침전 속에 <b>옅은 적갈색이 생겨 사라지지 않는 순간</b>이 종말점.",
main="""<ul><li>지시약 <b>K₂CrO₄</b>(크롬산칼륨, 5% 시액) — 자체가 약간 <b>노란색</b>.</li>
<li>종말점 전: Ag⁺는 Cl⁻하고만 반응 → 흰색 AgCl.</li>
<li>당량점 부근: Cl⁻이 없어지면 <span class="fx">2Ag⁺ + CrO₄²⁻ → Ag₂CrO₄↓ (적갈색)</span></li>
<li>적갈색 침전이 생겨 <b>교반해도 안 녹으면 바로 멈춤</b>. 전체가 <b>옅은 적갈색</b>(연갈색)이 된다. 시커멓게 될 때까지 기다리면 넘어간 것.</li>
<li>침전이 생기면 용액 → <b>현탁액</b> → 잘 안 섞임 → <b>교반을 세게</b>. 생겼다 없어지는 걸 반복하므로 교반이 종말점 판단의 핵심.</li></ul>
<div class="ebox"><div class="sec e">왜 AgCl이 먼저 침전되나? (K<sub>sp</sub>는 유인물 값)</div>
몰 용해도: AgCl s = √K<sub>sp</sub> ≈ 1.3 × 10⁻⁵ M &lt; Ag₂CrO₄ s = (K<sub>sp</sub>/4)<sup>1/3</sup> ≈ 6.7 × 10⁻⁵ M (K<sub>sp</sub> = 1.2 × 10⁻¹², 유인물)<br>
→ 덜 녹는 AgCl이 먼저 생기고, Cl⁻이 거의 다 없어진 뒤에야 Ag₂CrO₄가 생긴다. 당량점의 [Ag⁺] ≈ 1.3 × 10⁻⁵ M에서 Ag₂CrO₄가 생기려면 [CrO₄²⁻] = 1.2 × 10⁻¹² / 1.8 × 10⁻¹⁰ ≈ 7 × 10⁻³ M이 필요.</div>
<div class="ebox"><div class="sec e">모어법의 pH 조건 — 유인물: pH 6.5~10.5</div>
유인물: <b>pH 6.5~10.5</b> 사이에서 적정. 산성이면 CrO₄²⁻ → HCrO₄⁻/Cr₂O₇²⁻로 바뀌어 종말점이 늦어지고, 강알칼리면 Ag⁺가 AgOH/Ag₂O로 침전된다. 소금물·탈이온수는 대체로 중성이라 그대로 적정.</div>""",
side='<div class="fig" style="--imgh:150px"><img src="img/flasks.jpg"><div class="cap">유인물 1쪽 사진 — 흰 AgCl 현탁액 → 종말점의 옅은 적갈색</div></div>'
 + prof("하얀색 침전이 막 생기다가 갑자기 적갈색 침전이 생겨서 안 없어지잖아요? 그럼 바로 멈춰야 되는 거예요. 시커멓게 변할 때까지 기다리지 말고.")
 + card("tip", "📌 표정과 시료의 색 맞추기", "실험 2처럼 두 적정의 종말점 색(옅은 적갈색)을 같게 맞추면 지시약 오차가 줄어든다. 학생들도 \"아까 그거에 비해서 약간 연해\"라며 비교함."))

blank = pg("p-blank", "2-②", "공시험(blank test) — 물과 지시약의 몫 빼기", "표정 공시험 ② · 시료 공시험 ④", K1,
core="시료 없이 <b>종말점과 같은 부피의 탈이온수 + 지시약</b>만 적정 → 그 소비량(b)을 본 적정값에서 <b>빼 준다</b>. 좋은 탈이온수면 <b>한 방울</b>에 바로 적갈색.",
main="""<ul><li>목적: 물에 Ag⁺와 반응하는 Cl⁻ 등이 있거나, 지시약 색이 보이기까지 Ag⁺가 조금 더 필요한 만큼(지시약 오차)을 구해 보정.</li>
<li><b>"종말점에서와 같은 부피"</b> = 적정 플라스크에 <b>들어간 모든 용액의 부피 합</b>.<br>
&nbsp;&nbsp;표정: NaCl 표준액 20 mL + 물 약 40 mL + V(약 10 mL) ≈ <b>70 mL</b><br>
&nbsp;&nbsp;시료: 탈이온수 50 mL + V(약 8.6 mL) ≈ <b>59 mL</b></li>
<li>정확할 필요 없음 → <b>메스실린더</b>로 대충 재서 부음 (피펫 X, <b>뷰렛으로 물 옮기기 X</b> — 그 뷰렛은 못 쓰게 됨).</li>
<li>지시약 같은 양(4방울) 넣고 교반하며 적정. 한 방울에 끝나야 정상. 계속 들어가면 물이 오염된 것 → 물을 바꿀 것.</li>
<li>유인물은 "증류수"라고 되어 있지만 <b>노트에는 "탈이온수"</b>.</li></ul>
<div class="fbox"><span class="fx">보정 적정량 = V(본 적정) − b(공시험)</span></div>""",
side=prof("여러분이 적정을 잘하고 있다면 탈이온수를 적정했을 때는 질산은 한 방울 들어가자마자 바로 색깔이 쫙 변하면서 적갈색 침전이 생겨야 돼요. 그러면 우리 탈이온수가 아주 좋은 탈이온수라는 걸 확인할 수 있는 거죠.")
 + card("ana", "📎 지난주 5조의 공시험", "CO₂ 제거 안 한 탈이온수를 NaOH로 공시험 → <b>한 방울에 변색</b> → 녹아 있는 탄산이 거의 없다는 뜻. 실험 2 고찰에 쓸 수 있는 근거."))

calcf = pg("p-calcf", "2-③", "계산식 — f′, f, 대응량, NaCl 함량", "AgNO₃ 규정 농도 0.2 M 기준", K1,
core="두 개의 팩터를 쓴다: NaCl 표준액의 <b>f′ = 실제 칭량량 / 이론량</b>, AgNO₃의 <b>f</b> = 표정으로 구함. 둘 다 <b>소수 셋째 자리</b>.",
main="""<div class="fbox"><div class="sec f">① NaCl 표준액의 f′ (다시 표정하지 않음)</div>
이론량 = 0.1 mol/L × 0.1000 L × 58.44 g/mol = <b>0.5844 g</b> (함량 100% 가정)<br>
<span class="fx">f′ = 실제 칭량량 / 이론량</span> &nbsp; 예) 0.583 / 0.5844 = <b>0.998</b><br>
<span class="ko">0.584 g을 정확히 맞추려 애쓰지 말 것 — 시간 낭비. 더 쓰면 f′ &gt; 1, 덜 쓰면 &lt; 1, 상관없음.</span></div>
<div class="fbox"><div class="sec f">② AgNO₃의 f (표정)</div>
NaCl mmol = 0.1 × f′ × 20.00 = AgNO₃ mmol = 0.2 × f × (V − b)<br>
<span class="fx">f = (0.1 × f′ × 20.00) / [0.2 × (V − b)]</span></div>
<div class="fbox"><div class="sec f">③ 대응량 E와 NaCl 양</div>
E = AgNO₃ 1 mL에 대응하는 NaCl 양: 0.1 M → <b>5.844 mg</b>, <b>0.2 M → 11.69 mg</b><br>
<span class="fx">NaCl(mg) = (V − b) × f × E = (V − b) × f × 0.2 × 58.44</span><br>
<span class="fx">NaCl 함량(%) = NaCl(g) / 시료 칭량값(g) × 100</span></div>""",
side=prof("V × E 하면 NaCl의 양이 바로 나오죠. 하나 빼먹었잖아 — 팩터. 규정도 계수를 곱해줘야 돼요. 팩터 까먹지 말고요.")
 + card("trap", "⚠️ 흔한 실수", """<ul style="margin:0"><li>AgNO₃를 0.1 M로 계산 (정정 전 값)</li><li>NaCl 표준품을 99%로 계산 (100%로 가정)</li><li>f′ 또는 f를 빠뜨림 / 공시험 b를 안 뺌</li><li>f를 넷째 자리 이상으로 표기</li></ul>"""))

meth = pg("p-meth", "3", "실험방법 — 실제로 한 대로 쓰기", "유인물 1쪽 4. 실험방법 — 생략·제공된 것 표시", K2,
main="""<div class="sec">[0.1 M NaCl 표준액 조제] <span class="tag j">건조 생략</span></div>
<p>NaCl 표준품(99%, 100%로 가정)을 건조하지 않고 이론량 약 0.584 g 부근을 정밀하게 칭량(1조: 0.583 g) → 100 mL 용량플라스크, 탈이온수로 녹이고 표선까지 → 섞기. f′ 계산.</p>
<div class="sec">[5% K₂CrO₄ 지시액] <span class="tag j">제공됨</span> · [0.1 M AgNO₃ 조제] <span class="tag j">제공됨 · 실제 0.2 M</span></div>
<p>노트에는 "제공된 5% K₂CrO₄ 지시약", "제공된 AgNO₃ 용액(규정 농도 0.2 M, 갈색 병)을 사용하였다"고 쓴다. 유인물의 AgNO₃ 3.397 g 칭량 단계는 하지 않음.</p>
<div class="sec">[AgNO₃ 표정]</div>
<ol><li>NaCl 표준액 <b>20.00 mL</b>를 피펫으로 취해 삼각플라스크에 넣고 탈이온수(약 40 mL, 메스실린더)와 5% K₂CrO₄ 지시약 4방울을 넣는다 (200 mL 삼각플라스크).</li>
<li>교반하며 AgNO₃로 적정 → 옅은 적갈색 침전이 사라지지 않는 점. <span class="tag j">3회 반복 생략</span></li>
<li><b>공시험</b>: 들어간 부피 합(약 70 mL)만큼의 탈이온수 + 지시약을 적정.</li>
<li>f′와 공시험값으로 AgNO₃의 f(셋째 자리)를 계산.</li></ol>
<div class="sec">[시판 소금 중 NaCl 정량]</div>
<ol><li>시판 소금 약 0.1 g을 정밀 칭량해 삼각플라스크에 넣고 탈이온수 <b>50 mL</b>로 녹인 뒤 지시약 4방울(약 0.2 mL). <span class="tag j">시료 건조 생략</span></li>
<li>교반하며 AgNO₃로 적정. <span class="tag j">3회 반복 생략</span></li>
<li><b>공시험</b>: 50 mL + V(약 59 mL) 탈이온수 + 지시약을 적정.</li>
<li>f와 공시험값으로 NaCl 함량(%) 계산.</li></ol>""",
side=prof("실험 노트에다가 이걸 만들었다고 쓰면 틀리는 거죠. 그냥 '제공된 5% 포타슘 크로메이트 지시약을 사용했다', 이렇게 쓰면 돼요.")
 + card("tip", "🧪 적정 횟수", "오늘 적정 = <b>4번</b>: 표정 ① + 표정 공시험 ② + 시료 ③ + 시료 공시험 ④")
 + card("", "📌 녹취록 속 1조 진행", "피펫 필러가 잘 안 끼워져 20 mL 취하는 데 애먹음 → 끝까지 밀착해서 끼우니 해결. 탈이온수 40 mL, 지시약 4방울."))

tips = pg("p-tips", "4", "조작 요령 · 교수님 시연", "순회 지도 + 녹취록", K2,
main="""<div class="sec">① 뷰렛 · 용액</div>
<ul><li>뷰렛은 물이 아니라 <b>AgNO₃로 린싱</b>한 뒤 채움. 기포 없이 꽉 채우기 (\"잘했네\").</li>
<li>AgNO₃는 빛에 의해 조금씩 분해될 수 있어 <b>갈색 병</b>에 보관. 실험 중에 급격히 변하지는 않으니 걱정할 필요는 없음.</li>
<li>Ag⁺는 피부·옷에 묻으면 검게 변함 → <b>장갑</b>.</li>
<li>적정 전 뷰렛 위 <b>깔때기 빼기</b>.</li></ul>
<div class="sec">② 적정</div>
<ul><li>예상 소비량(표정 약 10 mL, 0.2 M 기준) 근처까지는 비교적 빠르게, 그 뒤 <b>한 방울씩</b>.</li>
<li>침전이 생기면 현탁액 → <b>교반 세게</b>. 적갈색이 생겼다 사라지면 계속, <b>약 15초간 흔들어도 탈색되지 않는 옅은 적갈색</b>이면 끝 (유인물).</li>
<li>물은 <b>메스실린더</b>로. 뷰렛으로 물을 옮기면 그 뷰렛은 못 쓰게 됨.</li></ul>
<div class="sec">③ 교수님 시연 — 과량 적정</div>
<p>공시험 끝난 플라스크(AgCl 없음)에 AgNO₃를 1 mL 이상 왕창 넣자 <b>핏빛·포도주 색</b>으로 변함 = Ag₂CrO₄가 엄청 생긴 것. \"침전 적정이 극도로 실패하면 이렇게 된다. 이런 색이 나올 때까지 하면 안 된다.\" AgCl과 섞이면 옅은 적갈색으로 보인다.</p>""",
side=card("trap", "🗑 뒷정리", "뷰렛은 원래 자리, 마그네틱 교반자·스터러는 <b>후드 안 원래 자리</b>. 테이블 위에 아무것도 남기지 말 것. 은·크롬산 폐액은 폐수통.")
 + card("tip", "⏱ 시간 절약", "저울이 붐비면 시료 소금(약 0.1 g)을 미리 칭량해 두기 (1조가 그렇게 함)."))

calc = pg("p-calc", "5", "1조 결과 — 실험노트 값", "1조, 각 1회 측정 (자세한 표·초안은 실험3_실험노트_부착용표_초안.pdf)", K3,
core="f′ = 0.583/0.5844 = <b>0.998</b> · 표정 V = 29.73 − 19.87 = <b>9.86 mL</b>, b = 0.03 → <b>f = 1.015</b> · 시료 V = 41.18 − 32.60 = <b>8.58 mL</b>, b = 0.03 → <b>함량 102.5%</b>",
main="""<div class="sec">① AgNO₃의 f</div>
<ol><li>NaCl mmol (20.0 mL) = 0.1 × 0.998 × 20.0 = <b>1.9960 mmol</b> → 0.2 M면 예상 V ≈ 9.98 mL</li>
<li>f = 1.9960 / [0.2 × (9.86 − 0.03)] = 1.9960 / 1.966 = <b>1.015</b></li></ol>
<div class="sec">② 시판 소금 중 NaCl (f = 1.015)</div>
<ol><li>V − b = 8.58 − 0.03 = <b>8.55 mL</b></li>
<li>NaCl = 8.55 × 1.015 × 11.688 × 10⁻³ = <b>0.10143 g</b></li>
<li>함량 = 0.10143 / 0.099 × 100 = <b>102.5%</b></li></ol>
<table class="t"><tr><th>적정</th><th>시작</th><th>최종</th><th>소비량</th></tr>
<tr><td>① 표정 (NaCl 표준액 20.0 mL)</td><td>19.87</td><td>29.73</td><td>9.86 mL</td></tr>
<tr><td>② 표정 공시험 (약 70 mL)</td><td colspan="2">—</td><td>0.03 mL</td></tr>
<tr><td>③ 시판 소금 (0.099 g)</td><td>32.60</td><td>41.18</td><td>8.58 mL</td></tr>
<tr><td>④ 시료 공시험 (약 59 mL)</td><td colspan="2">—</td><td>0.03 mL</td></tr></table>""",
side=card("trap", "⚠️ 함량이 100%를 넘음 → 고찰 핵심", """<ul style="margin:0"><li>표준품 순도 99%를 100%로 가정 → f 과대. 99% 반영 시 f′ = 0.988, f = 1.005, 함량 101.4%</li>
<li>표준품 건조 생략 → 같은 방향</li>
<li>시료 0.099 g(셋째 자리) 칭량 → ±0.5%</li>
<li>KCl 등 다른 염화물, 종말점 판단</li></ul>""")
 + card("tip", "📌 자료", "실험노트 초안·부착용 표: <b>실험3_실험노트_부착용표_초안.pdf</b><br>수식 포함 결과표: <b>실험3_모어법 NaCl 정량_결과.xlsx</b>"))

disc = pg("p-disc", "6", "고찰 포인트 — 오차 원인 · 대책 · 개선 방안", "교수님: 디스커션 할 게 많아지도록 일부러 생략", K3,
main="""<table class="t"><tr><th style="width:22%">원인</th><th>결과에 미치는 영향</th><th style="width:28%">대책 · 개선</th></tr>
<tr><td><b>표준품 순도 99%</b>를 100%로 가정</td><td>실제 NaCl이 칭량값보다 1% 적음 → 표정 V↓ → <b>f 과대</b> → 시료 함량 과대</td><td>고순도(일차표준) NaCl 사용 또는 순도 보정</td></tr>
<tr><td>표준품 <b>건조 생략</b></td><td>수분만큼 실제 NaCl↓ → f 과대 → 함량 과대</td><td>100–120 °C 2시간 건조, 데시케이터 냉각</td></tr>
<tr><td>시료 소금 <b>건조 안 함</b></td><td>수분 포함 → 함량(%)은 그만큼 낮게 나와야 정상</td><td>건조 감량 측정 후 건조물 기준으로 환산</td></tr>
<tr><td>Cl⁻ 공급원이 NaCl만이 아님 (KCl 등)</td><td>모든 Cl⁻이 NaCl로 환산 → 함량 과대 가능</td><td>Na⁺를 따로 정량(원자분광 등)해 비교</td></tr>
<tr><td>종말점 판단 (적갈색)</td><td>흰 침전 속 색 구분 어려움, 교반 부족 → 늦게 멈춤 → V↑</td><td>교반 세게, 표정·시료 색 맞추기, 반 방울씩</td></tr>
<tr><td>지시약 오차</td><td>Ag₂CrO₄ 색이 보이려면 Ag⁺ 조금 더 필요 → V↑</td><td>공시험으로 보정 (오늘 한 것)</td></tr>
<tr><td>AgNO₃ 농도 정정 (0.1 → 0.2 M)</td><td>V가 약 10 mL로 작아져 눈금 읽기 오차의 비율↑</td><td>적정량이 20 mL 이상 되도록 시료량 조절</td></tr>
<tr><td>1회 측정</td><td>평균·표준편차 없음, 재현성 확인 불가</td><td>3회 반복</td></tr>
<tr><td>AgNO₃ 광분해</td><td>실험 시간 동안은 영향 거의 없음 (교수님)</td><td>갈색 병, 빛 차단</td></tr></table>""",
side=prof("99%짜리를 100% 표준품이라 생각하고... 약간의 오차가 들어가겠죠? 얼마나 좋아요, 디스커션에 쓸 게 생겼잖아.")
 + prof("100%가 안 돼야지 맞겠죠. 물도 약간 묻어 있을 거고 수분도 좀 들어 있을 거고. 우리가 말리지 않았거든요."))

QA = [
("Q1. 모어법은 어떤 적정이고 무엇을 정량하나?", "AgNO₃를 적정제로 하는 침전 적정(은적정). 실제로는 Cl⁻을 정량해 NaCl로 환산."),
("Q2. 적정 반응과 몰비는?", "Ag⁺ + Cl⁻ → AgCl↓(흰색), 1 : 1."),
("Q3. AgCl의 K<sub>sp</sub>는 대략?", "약 10⁻¹⁰ (1.8 × 10⁻¹⁰)."),
("Q4. 모어법의 지시약과 종말점 색은?", "K₂CrO₄(노란색). 종말점에서 Ag₂CrO₄ 적갈색 침전."),
("Q5. AgCl이 Ag₂CrO₄보다 먼저 침전되는 이유는?", "몰 용해도가 더 작기 때문 (AgCl ≈ 1.3 × 10⁻⁵ M &lt; Ag₂CrO₄ ≈ 6.7 × 10⁻⁵ M)."),
("Q6. 침전 적정에서 교반이 특히 중요한 이유는?", "침전이 생기면 현탁액이 되어 잘 안 섞이고, 적갈색이 생겼다 사라지기를 반복하므로."),
("Q7. 공시험이란?", "시료 없이 종말점과 같은 부피의 물 + 지시약을 적정해 그 값을 본 적정값에서 빼는 것."),
("Q8. \"종말점에서와 같은 부피\"는?", "플라스크에 들어간 모든 용액 부피의 합 (표정: 20 + 40 + V)."),
("Q9. NaCl 표준액의 f′는?", "실제 칭량량 / 이론량 (0.1 M 100 mL → 이론량 0.5844 g)."),
("Q10. AgNO₃의 f 식은?", "f = (0.1 × f′ × 20.00) / [0.2 × (V − b)] (오늘은 규정 농도 0.2 M)."),
("Q11. 0.2 M AgNO₃ 1 mL의 NaCl 대응량은?", "0.2 × 58.44 = 11.69 mg (0.1 M면 5.844 mg)."),
("Q12. AgNO₃를 갈색 병에 보관하는 이유는?", "빛에 의해 조금씩 분해될 수 있어서."),
("Q13. 모어법의 적정 pH와 이유는?", "pH 6.5~10.5 (유인물). 산성이면 크롬산이 바뀌어 종말점 지연, 강알칼리면 AgOH/Ag₂O 침전."),
("Q14. 시판 소금의 함량이 100%보다 낮게 나와야 하는 이유는?", "수분과 다른 성분이 들어 있고 건조하지 않았기 때문."),
("Q15. 과량의 AgNO₃를 넣으면?", "Ag₂CrO₄가 많이 생겨 핏빛·포도주 색이 된다 (교수님 시연)."),
("Q16. 표준품 99%를 100%로 가정하면 f는?", "실제 NaCl이 적어 V가 작아지므로 f가 과대평가된다."),
]


def qa(items):
    return "".join(f'<div class="qa"><div class="q">{q}</div><div class="a">{a}</div></div>' for q, a in items)


check = card("tip", "📝 실험노트 체크리스트 (실험 3)", """<ul style="list-style:none;padding-left:0;margin:0">
<li>□ 페이지 번호 <b>실험 2에서 이어서</b>, 1권, 서명은 머리말/꼬리말</li>
<li>□ <b>원리 최소 반 페이지</b> (반응식, 지시약, K<sub>sp</sub>, 공시험, f′·f 식)</li>
<li>□ 방법은 <b>실제 한 대로</b>: 건조 생략, 탈이온수, 제공된 지시약·AgNO₃(0.2 M), 실제 칭량값, 1회</li>
<li>□ 결과: 칭량값 2개, 적정 4번의 시작·최종 눈금(둘째 자리), f′·f(셋째 자리), 함량(%) 계산 과정</li>
<li>□ 고찰: 원인 · 대책 · 개선 (99% 표준품, 건조 생략, 0.2 M 정정, 종말점, 1회 측정)</li>
<li>□ 부착물: 노트 번호 + 부착 페이지, 겹치게 간인</li>
<li>□ 큰 빈 공간만 빗금 한 줄</li></ul>""")

qa1 = pg("p-qa", "7", "기말 대비 핵심 체크 (Q&amp;A) ①", "Q1–Q8", K3, main=qa(QA[:4]), side=qa(QA[4:8]))
qa2 = pg("p-qa2", "7", "기말 대비 핵심 체크 (Q&amp;A) ② · 노트 체크리스트", "Q9–Q16", K3, main=qa(QA[8:]), side=check)

E = [cover, notice, over, purpose, mohr, blank, calcf, meth, tips, calc, disc, qa1, qa2]
