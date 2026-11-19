# -*- coding: utf-8 -*-
"""실험4 EDTA를 이용한 물의 세기(경도) 측정 — 실험1~3 요약정리와 같은 양식 (유인물 2쪽 + 녹취록)"""
from svgs import STYLE


def card(kind, title, body):
    return f'<div class="card {kind}"><div class="ct">{title}</div>{body}</div>'


def prof(body):
    return card("prof", "🎙 교수님 말씀", body)


def fig(name, cap, h=150):
    return f'<div class="fig" style="--imgh:{h}px"><img src="img/{name}.jpg"><div class="cap">{cap}</div></div>'


def pg(pid, bd, title, sub, part, main, side="", core=""):
    core = f'<div class="core"><span class="lb">💡 핵심</span>{core}</div>' if core else ""
    body = f'<div class="main{"" if side else " full"}">{main}</div>' + (f'<div class="side">{side}</div>' if side else "")
    return dict(t="r", id=pid, html=f'''<div class="hd"><span class="bd">{bd}</span><div class="tt"><h1>{title}</h1><div class="sb">{sub}</div></div><span class="pt">{part}</span></div>
{core}<div class="body">{body}</div>''')


K0, K1, K2, K3 = "공지 · 한눈에", "목적 · 원리", "방법 · 조작", "계산 · 고찰"

FLOW = """<svg viewBox="0 0 680 200" class="svgf">
<g class="box"><rect x="4" y="10" width="150" height="62" rx="8" class="hl"/><rect x="190" y="10" width="150" height="62" rx="8"/>
<rect x="376" y="10" width="140" height="62" rx="8"/><rect x="552" y="10" width="124" height="62" rx="8" class="hl"/>
<rect x="190" y="112" width="150" height="62" rx="8"/><rect x="376" y="112" width="140" height="62" rx="8"/>
<rect x="552" y="112" width="124" height="62" rx="8" class="hl"/></g>
<g class="bt"><text x="79" y="36">EDTA 표준액 조제</text><text x="79" y="56">≈ 0.931 g → 250 mL, f</text>
<text x="265" y="36">시료 100 mL + KCN</text><text x="265" y="56">+ MgCl₂ 1.0 mL + pH 10</text>
<text x="446" y="36">EBT, EDTA 적정</text><text x="446" y="56">적색 → 청색 (a mL)</text>
<text x="614" y="36">총경도</text><text x="614" y="56">(a·f − 1) × 10</text>
<text x="265" y="138">시료 100 mL + NaOH</text><text x="265" y="158">pH 12, Mg(OH)₂↓ 5분</text>
<text x="446" y="138">HNB, EDTA 적정</text><text x="446" y="158">적색 → 청색 (b mL)</text>
<text x="614" y="138">Ca 경도</text><text x="614" y="158">b · f × 10</text></g>
<g class="ar"><path d="M156 41 h30"/><path d="M342 41 h30"/><path d="M518 41 h30"/>
<path d="M342 143 h30"/><path d="M518 143 h30"/><path d="M79 74 v69 h107"/></g>
<text x="4" y="104" class="sm okt">① 표준액 (1차 표준물질 → 표정 생략)</text>
<text x="190" y="192" class="sm okt">② 적정 2번 → Mg 경도 = 총경도 − Ca 경도</text>
</svg>"""

cover = dict(t="r", cls="cover2", html=STYLE + """
<style>
.cover2{background:radial-gradient(ellipse at 0% 0%,#ffd9e8 0%,rgba(255,217,232,0) 45%),radial-gradient(ellipse at 100% 0%,#dcd6ff 0%,rgba(220,214,255,0) 50%),radial-gradient(ellipse at 100% 100%,#d4f5e6 0%,rgba(212,245,230,0) 50%),radial-gradient(ellipse at 40% 60%,#dfe6ff 0%,rgba(223,230,255,0) 60%),#f4f1fb !important;}
.cv-k{letter-spacing:.32em;font-size:11px;font-weight:700;color:#7d74c9;margin-top:6mm;}
.cv-h{font-size:34px;line-height:1.2;font-weight:800;margin:10px 0 12px 0;background:linear-gradient(120deg,#5b3fd6,#3f57d8);-webkit-background-clip:text;background-clip:text;color:transparent;}
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
<div class="cv-left"><div class="cv-k">의약품분석학 실험 · 실험 4 · 킬레이트 적정법</div>
<div class="cv-h">실험 4.<br>EDTA를 이용한<br>물의 세기(경도) 측정</div>
<div class="cv-flow">자료: 실험4 유인물 1–2쪽 + 수업 녹취록(2026-11-19, 약 72분) 요약</div>
<div class="cv-txt"><b>한 줄 요약</b> — 1차 표준물질 <b>EDTA</b>로 표준액을 만들고(f), 가리움제로 다른 금속을 막은 뒤
pH 10(EBT)에서 <b>Ca²⁺ + Mg²⁺</b>, pH 12(HNB)에서 <b>Ca²⁺만</b> 적정해 모두 <b>CaCO₃ ppm</b>으로 나타낸 실험.</div>
<div class="cv-eq">0.01 M EDTA 1 mL ≡ 1.000 mg CaCO₃ · 시료 100 mL<br>
총경도 = (a × f − 1) × 10 &nbsp;·&nbsp; Ca 경도 = b × f × 10 &nbsp;·&nbsp; Mg 경도 = 총경도 − Ca 경도</div></div>
<div class="cv-toc"><div class="t">CONTENTS</div>
<div class="row"><span class="n">0</span><span class="nm">공지 · 지난주 리뷰 · 노트 코멘트</span><span class="pg">{PAGE:p-notice}</span></div>
<div class="row"><span class="n">0</span><span class="nm">오늘 한 일 한눈에</span><span class="pg">{PAGE:p-over}</span></div>
<div class="row"><span class="n">1</span><span class="nm">물의 경도 — 정의 · ppm · 기준</span><span class="pg">{PAGE:p-hard}</span></div>
<div class="row"><span class="n">2</span><span class="nm">원리 ① EDTA 킬레이트 · 지시약 색 변화</span><span class="pg">{PAGE:p-edta}</span></div>
<div class="row"><span class="n">2</span><span class="nm">원리 ② 가리움제 · MgCl₂ · pH 10 vs 12</span><span class="pg">{PAGE:p-mask}</span></div>
<div class="row"><span class="n">2</span><span class="nm">원리 ③ 계산식 · 암산 · EDTA의 f</span><span class="pg">{PAGE:p-calcf}</span></div>
<div class="row"><span class="n">3</span><span class="nm">시약 및 기구 — 만들 것은 1개</span><span class="pg">{PAGE:p-reag}</span></div>
<div class="row"><span class="n">4</span><span class="nm">실험방법 — 표준액 조제 / 적정 구분</span><span class="pg">{PAGE:p-meth}</span></div>
<div class="row"><span class="n">5</span><span class="nm">조작 요령 · 종말점 · 안전</span><span class="pg">{PAGE:p-tips}</span></div>
<div class="row"><span class="n">6</span><span class="nm">고찰 포인트 — 원인 · 대책 · 개선</span><span class="pg">{PAGE:p-disc}</span></div>
<div class="row"><span class="n">7</span><span class="nm">기말 대비 Q&amp;A · 노트 체크리스트</span><span class="pg">{PAGE:p-qa}</span></div></div>
<div class="cv-src">의약품분석학 실험 「실험 4: EDTA를 이용한 물의 세기(경도) 측정(킬레이트 적정법)」 유인물 1–2쪽 · 수업 녹취록</div>
""")

notice = pg("p-notice", "공지", "지난주(실험 3) 리뷰 · 노트 코멘트 · 오늘의 시료", "수업 시작 전 교수님 말씀", K0,
main=card("tip", "📊 지난주 NaCl 함량 리뷰", """<ul style="margin:0">
<li>시판 소금의 NaCl 함량은 <b>아무도 정답(참값)을 모른다</b> → "오차가 있다"고 단정할 수 없다.</li>
<li>그런데 두 조쯤이 <b>100%를 넘게(103% 등)</b> 나왔다 → 참값은 몰라도 <b>분명히 오차</b>가 있는 것.</li>
<li>결국 <b>V가 과대하게 측정</b>된 것 — 당량점을 넘겼거나 교반이 잘 안 돼서 늦게 변색됐을 수도. 원인은 아무도 모르지만 <b>디스커션을 잘 썼더라</b>.</li>
<li>"실험이니까 오차는 항상 존재할 수 있다. 전혀 이상한 게 아니다."</li></ul>""")
 + card("trap", "✍️ 실험노트 코멘트 (이번 채점)", """지금까지 리포트는 만점. 다만 <b>"표정과 적정을 구분하여 기재하면 더 좋겠다"</b>.<br>
→ 결과·방법을 <b>[표준액 조제/표정]</b>과 <b>[시료 적정]</b> 단락(또는 표)으로 나눠 쓰기. 이번 실험은
<b>[EDTA 표준액 조제 — 1차 표준물질이라 표정 생략, f 계산]</b> / <b>[총경도 적정]</b> / <b>[Ca 경도 적정]</b> / <b>[Mg 경도 계산]</b>."""),
side=card("", "💧 오늘의 시료", "가져온 물: <b>에비앙, 백산수, 삼다수</b> (세 조). 나머지 조는 <b>실험실 수돗물</b>.<br>교수님: \"오른쪽 수돗물하고 왼쪽 수돗물이 경도가 같을까요?\" — 다르게 나오면 배관 문제일 수도.")
 + prof("참값을 우리가 모르지만 분명히 오차가 있는 거지. 그래서 디스커션에 잘해 놨더라고. 그게 실험입니다."))

over = pg("p-over", "한눈에", "오늘 한 일 — 표준액 조제 → 적정 2번", "Overview", K0,
core="만들 용액은 <b>EDTA 표준액 1개</b>뿐. 적정은 <b>총경도(pH 10, EBT)</b>와 <b>Ca 경도(pH 12, HNB)</b> 2번, Mg 경도는 <b>계산</b>.",
main=FLOW + """<ul><li>EDTA(disodium EDTA dihydrate, 순도 99.5%)는 <b>1차 표준물질</b> → 표정 없이 칭량값으로 f를 구한다 (실험 3의 NaCl 표준액 f′와 같은 방식).</li>
<li>나머지 시약(완충액, 지시약, KCN, MgCl₂, NaOH, hydroxylamine)은 <b>모두 만들어져 있음</b> → 노트에는 "제공된 …을 사용하였다".</li>
<li>공통 시약은 오른쪽에 모아 둠. <b>삼각플라스크를 들고 가서</b> 시약을 넣고 오기 ("요리하듯 양념을 치고").</li></ul>""",
side=card("tip", "🧮 미리 알고 하는 적정 (f ≈ 1)", """<table class="t" style="margin:0"><tr><th>총경도</th><th>a (mL)</th></tr>
<tr><td>100 ppm</td><td><b>11</b> (10 아님!)</td></tr><tr><td>300 ppm (음용수 상한)</td><td><b>31</b></td></tr></table>
→ 11쯤에서 끝나면 평범한 물, 30이 넘어가면 문제 (물이 기준 초과 또는 실험 오류).""")
 + prof("여러분이 답을 미리 알고 적정을 해야 실험을 잘할 수 있어. 답을 모르고 적정을 하면 종말점을 지나가는지 안 지나가는지 알 수가 없거든."))

hard = pg("p-hard", "1", "물의 경도 — 정의 · ppm · 기준", "유인물 1쪽 1. 원리", K1,
core="경도 = <b>Ca²⁺와 Mg²⁺</b>의 양을 <b>모두 CaCO₃의 양으로 환산</b>해 <b>ppm</b>으로 나타낸 것 (Mg도 CaCO₃로 간주).",
main="""<p><b>원리 (유인물)</b>: 천연수에 가장 많이 함유된 양이온은 Ca²⁺와 Mg²⁺이다. 물에 함유되어 있는 철, 구리, 망간 등의 금속이온을 가리움제(masking agent)를 써서 반응에 참여하지 못하게 한 후 EDTA 표준액을 사용하여 Ca²⁺와 Mg²⁺의 킬레이트를 생성시켜 전체 금속이온 농도를 구한다. 물의 세기는 킬레이트 적정법에 의하여 정량되는 칼슘과 마그네슘에 의해 결정되며 이 양을 모두 CaCO₃의 양으로 환산하여 ppm 단위로 표시한다.</p>
<div class="fbox"><div class="sec f">📐 1 ppm은 얼마나 작은가</div>
<span class="fx">1 ppm = 1 g / 10⁶ mL = 1 μg/mL</span> (밀도 1 가정)<br>
10⁶ mL = 10⁶ g = 1,000 kg = <b>물 1톤</b>에 CaCO₃ <b>1 g</b>이 녹아 있으면 1 ppm.</div>
<p>총산도(실험 2: 모든 유기산 → 초산), NaCl 정량(실험 3: 모든 Cl⁻ → NaCl)과 같은 논리 — 이번엔 Ca²⁺·Mg²⁺ → CaCO₃.</p>""",
side=fig("table", "유인물 1쪽 — 경도 기준 (ppm as CaCO₃)", 150)
 + card("tip", "📌 기준 (시험 포인트)", "<b>우리나라 음용수 기준: 총경도 300 ppm 이하</b> (실제로는 100 ppm 이하가 좋다고 봄). 기준은 법으로 딱 정해진 게 아니라 자료마다 조금씩 다를 수 있음.")
 + prof("음용수는 300 ppm이 넘으면 안 됩니다. 만일 우리 수돗물이 300 ppm이 넘으면 수돗물이 잘못됐는지 배관 시스템에 문제가 있는지 확인을 해봐야 돼."))

edta = pg("p-edta", "2-①", "EDTA 킬레이트와 지시약 색 변화", "유인물 1쪽 2. 반응식 · 목시 적정", K1,
core="지시약은 <b>유리형(HIn²⁻) = 청색</b>, <b>금속 결합형(MIn⁻) = 적색</b>. 시료에 지시약을 넣으면 <b>적색</b>, 종말점에서 EDTA가 금속을 뺏어 <b>청색</b>.",
main="""<ul><li>EDTA는 매우 다양한 금속과 아주 안정한 착물(킬레이트)을 만든다 → <b>형성상수 K<sub>f</sub>가 매우 커서</b> 적정이 가능. 대신 <b>선택성이 별로 없다</b> → 가리움제가 필요.</li>
<li>EDTA와 금속은 <b>1 : 1</b>로 결합: Ca²⁺ + Y⁴⁻ → CaY²⁻ (log K<sub>f</sub> = 10.65), Mg²⁺ + Y⁴⁻ → MgY²⁻ (log K<sub>f</sub> = 8.79)</li></ul>
<div class="sec">적정 중 일어나는 순서 (순차 반응)</div>
<ol><li>시료(수돗물) + 지시약 → 지시약이 금속 일부와 결합 → <b>적색</b> (M²⁺ + HIn²⁻ → MIn⁻ + H⁺)</li>
<li>EDTA를 넣어도 처음엔 <b>적색 그대로</b> — 지시약은 아주 조금만 넣었으니 남아 있는 자유 Ca²⁺·Mg²⁺가 먼저 EDTA와 반응</li>
<li>자유 Ca²⁺·Mg²⁺가 다 소모되면 EDTA가 <b>지시약에 붙은 금속을 빼앗음</b> → 지시약이 유리형으로 → <b>청색</b> = 종말점<br>
<span class="fx">MIn⁻(red) + Y⁴⁻ + H⁺ → MY²⁻ + HIn²⁻(blue)</span></li></ol>
<div class="ebox"><div class="sec e">✔ 확인 실험</div>탈이온수에 지시약을 넣으면 금속이 없으니 <b>청색</b>이어야 정상. 적색이면 탈이온수가 오염된 것.</div>""",
side=fig("rxn", "유인물 1쪽 — 반응식 (지시약 결합/유리, CaY²⁻·MgY²⁻의 log K<sub>f</sub>)", 150)
 + prof("유리형, 프리 폼일 때의 색깔이 무슨 색깔이죠? 파란색이에요. 잘 기억해야 돼요. 금속과 결합하면 빨간색으로 바뀌어요.")
 + card("trap", "⚠️ 수업 중 함정 문답", "\"지시약을 넣으면 무슨 색?\" → 학생들 \"파란색\" → 교수님 \"파란색이라고요?\" → 정답은 <b>빨간색</b> (수돗물엔 금속 이온이 있으니까)."))

mask = pg("p-mask", "2-②", "가리움제 · MgCl₂를 넣는 이유 · pH 10 vs 12", "masking agent · 지시약 2종", K1,
core="<b>KCN</b>(가리움제)으로 Fe·Cu·Mn 등을 먼저 막고, pH 10에서는 <b>Ca + Mg</b>(EBT), NaOH로 <b>pH 12</b>를 만들면 <b>Mg(OH)₂가 침전</b>되어 <b>Ca만</b>(HNB) 적정.",
main="""<div class="sec">가리움제 (masking agent)</div>
<ul><li>수돗물에는 Ca·Mg 말고도 철(배관), 구리, 망간 등이 있을 수 있고, EDTA는 이들과도 킬레이트를 만든다 → 어느 금속이 반응했는지 구분 불가.</li>
<li>→ 가리움제를 <b>먼저</b> 넣어 다른 금속이 EDTA와 반응하지 못하게 한 다음 Ca·Mg만 적정.</li>
<li><b>10% KCN(청산가리)</b>: 다른 금속을 시안화 착물로 만들어 가린다. <b>10% hydroxylamine HCl</b>(Ca 경도): 환원제로 Fe³⁺·Mn 등을 낮은 산화 상태로 바꿔 지시약 방해를 줄인다 <span class="ko">(일반 이론)</span>.</li></ul>
<div class="sec">MgCl₂ 0.01 M 1.0 mL를 넣는 이유 (총경도)</div>
<ul><li>EBT는 Mg와의 색 변화가 선명 → <b>종말점 색 변화를 선명하게</b> 하려고 일부러 넣는다.</li>
<li>넣은 Mg도 경도로 측정되므로 <b>빼 줘야</b> 과대평가가 안 됨 → 식의 "<b>− 1</b>". MgCl₂와 EDTA가 같은 0.01 M이고 1 : 1이라 부피(1 mL)를 그대로 뺀다.</li></ul>
<div class="sec">pH와 지시약</div>
<table class="t"><tr><th></th><th>총경도</th><th>Ca 경도</th></tr>
<tr><td>pH 조절</td><td>암모니아 완충액 2 mL → <b>pH 10</b></td><td>20% NaOH 1 mL → <b>pH ≈ 12</b></td></tr>
<tr><td>적정 대상</td><td>Ca²⁺ + Mg²⁺</td><td>Ca²⁺만 (Mg는 <b>Mg(OH)₂ 흰 침전</b>, 5분 방치)</td></tr>
<tr><td>지시약</td><td><b>EBT</b> 용액 3방울</td><td><b>HNB</b> 희석 분말 (스패출러로 소량)</td></tr>
<tr><td>색 변화</td><td>적색 → 청색</td><td>적색 → 청색</td></tr></table>""",
side=prof("pH 조건에 따라서 변색 범위가 달라져요, 지시약이. 그래서 지시약이 다릅니다.")
 + card("tip", "📌 Mg(OH)₂ 관찰", "NaOH를 넣고 흔들며 흰 부유물이 생기는지 보기. 많이 생기면 Mg가 많은 것, 거의 안 생기면 <b>실험을 잘못한 게 아니라 Mg가 거의 없는 것</b> → Mg 경도 ≈ 0, Ca 경도 ≈ 총경도.")
 + card("trap", "⚠️ 지시약 이름", "유인물: <b>HNB</b>(hydroxynaphthol blue disodium salt). 녹취에서는 \"NNB\"로 들림. 노트에는 유인물대로 <b>HNB</b>."))

calcf = pg("p-calcf", "2-③", "계산식 · 암산 · EDTA 표준액의 f", "유인물 2쪽", K1,
core="0.01 M EDTA <b>1 mL ≡ 1.000 mg CaCO₃</b>. 시료 100 mL면 1000/100이 약분돼 <b>× 10</b>만 하면 ppm.",
main="""<div class="fbox"><div class="sec f">① EDTA 표준액의 f (1차 표준물질 → 표정 생략)</div>
이론량 = 0.01 mol/L × 0.2500 L × 372.25 g/mol = <b>0.9306 g</b> (≈ 0.931 g)<br>
<span class="fx">f = 실제 칭량량 / 이론량</span> &nbsp; <span class="ko">0.931 g을 정확히 맞추려 하지 말고, 근처를 달아 정확한 값만 기록</span><br>
<span class="ko">(유인물은 "정확한 농도를 계산하여 f 표기". 순도 99.5%는 실험 3처럼 100%로 가정하는지 확인 — 고찰 거리)</span></div>
<div class="fbox"><div class="sec f">② 경도 계산 (유인물)</div>
1 mol/L EDTA 1 mL ≡ 100.0869 mg CaCO₃ → 0.01 mol/L EDTA 1 mL ≡ 1.000 mg CaCO₃<br>
<span class="fx">총경도 (CaCO₃ ppm) = (a × f − 1) × 1000 / 시료 mL</span><br>
<span class="fx">Ca 경도 (CaCO₃ ppm) = b × f × 1000 / 시료 mL</span><br>
<span class="fx">Mg 경도 (CaCO₃ ppm) = 총경도 − Ca 경도</span></div>
<div class="ebox"><div class="sec e">✍️ 암산 예 (시료 100 mL, f = 1)</div>
a = 11 mL → (11 − 1) × 10 = <b>100 ppm</b> · a = 31 mL → <b>300 ppm</b> · b = 10 mL → <b>Ca 100 ppm</b><br>
수업 중 한 조: a ≈ 6.8 mL → (6.8 − 1) × 10 ≈ <b>58 ppm</b> → "단물" (조치원 수돗물)</div>""",
side=fig("eq_total", "유인물 2쪽 — 대응량과 총경도 식", 120)
 + prof("팩터가 없는 표준액은 그냥 용액이고요, 팩터가 있어야지 표준액이 됩니다. 표정 과정이 생략되는 거지, 1차 표준 물질이기 때문에.")
 + card("trap", "⚠️ 식의 −1 위치", "유인물 식은 <b>(a × f − 1)</b>: EDTA 소비량에 f를 곱해 실제 0.01 M 상당 부피로 바꾼 뒤, 정확히 0.01 M인 MgCl₂ 1 mL를 뺀다. 수업 중엔 \"V − 1에 f를 곱한다\"처럼 말씀하셨지만 노트에는 <b>유인물 식</b>대로."))

reag = pg("p-reag", "3", "시약 및 기구 — 만들 용액은 EDTA 표준액 1개", "유인물 1쪽 3. 시약 및 기구 · 4. 시약 조제", K2,
main="""<p><b>시약 및 기구 (유인물)</b>: 분석저울, magnetic stirrer, Erlenmeyer flask (250 mL), mess cylinder (100 mL), volumetric flask (100, 250, 500 mL), buret (50 mL), transfer pipet (2, 20 mL), stand, clamp, 세척병, disodium EDTA dihydrate (FM 372.25), 탈이온수, 암모니아수 (28%), NH₄Cl, 20% NaOH 수용액, KCN, hydroxylamine HCl, triethanolamine, MgCl₂, KNO₃, Eriochrome Black T (EBT), hydroxynaphthol blue disodium salt (HNB)</p>
<p class="ko">교수님: 기구 목록에 잘못 적힌 것이 있어 조교가 맞게 준비함 (실제로는 200 mL 삼각플라스크, 1 mL 마이크로피펫 사용).</p>
<table class="t"><tr><th>용액 (유인물 조제법)</th><th>오늘</th></tr>
<tr><td><b>0.01 mol/L EDTA 표준액</b>: 80 °C 1시간 건조·데시케이터 → 약 0.931 g을 정확히 → 250 mL 용량플라스크, 탈이온수 약 200 mL로 진탕해 녹인 후 표선 → f 표기</td><td><b>직접 조제</b> (건조는 실제 여부 기록)</td></tr>
<tr><td>암모니아 완충용액 (pH 10): NH₄Cl 17.4 g + 28% 암모니아수 142 mL → 250 mL</td><td>제공됨</td></tr>
<tr><td>EBT 지시약 (0.1 w/v%): EBT 10 mg + triethanolamine 5 mL + 무수 에탄올 5 mL</td><td>제공됨</td></tr>
<tr><td>HNB 지시약: 질산칼륨 1 g + HNB 10 mg 희석분쇄</td><td>제공됨 (분말)</td></tr>
<tr><td>10% KCN: KCN 10.00 g → 100 mL</td><td>제공됨</td></tr>
<tr><td>0.01 mol/L MgCl₂: MgCl₂ 95.21 mg → 100 mL</td><td>제공됨</td></tr>
<tr><td>20% NaOH: NaOH 20.00 g → 100 mL (plastic 용량플라스크)</td><td>제공됨</td></tr>
<tr><td>10% hydroxylamine HCl: 10.00 g → 100 mL</td><td>제공됨</td></tr></table>""",
side=prof("여러분이 만들어야 되는 용액은 한 개밖에 없습니다. 나머지는 다 만들어져 있어요.")
 + card("trap", "⚠️ 유인물 내 표기 차이", "<ul style=\"margin:0\"><li>HNB 희석제: 1쪽은 <b>질산칼륨(KNO₃)</b>, 2쪽은 \"질산나트륨으로 희석한 HNB\" → 시약 목록은 KNO₃.</li><li>삼각플라스크: 목록 250 mL, 방법 200 mL.</li></ul>")
 + card("tip", "📌 EDTA 녹이기", "\"200 mL를 먼저 넣으라는 게 아니고 <b>녹여서 완전히 녹은 상태에서</b> 표선까지 맞추라.\" (36:35)"))

meth = pg("p-meth", "4", "실험방법 — 표준액 조제 / 적정을 구분해서", "유인물 2쪽 · 노트 코멘트 반영", K2,
main="""<div class="sec">[A. 0.01 M EDTA 표준액 조제] — 표정 생략 (1차 표준물질)</div>
<p>disodium EDTA dihydrate 약 0.931 g을 정확히 칭량(실제 값 기록) → 250 mL 용량플라스크 → 탈이온수로 완전히 녹인 뒤 표선 → f = 실제/이론(0.9306 g).</p>
<div class="sec">[B. 총경도 적정] — pH 10, EBT</div>
<ol><li>시료 100 mL를 <b>메스실린더</b>로 정확히 취해 200 mL 삼각플라스크에.</li>
<li>10% KCN <b>5방울</b>, 0.01 M MgCl₂ <b>1.0 mL</b>(마이크로피펫), 암모니아 완충액(pH 10) <b>2 mL</b>, EBT 지시약 <b>3방울</b> → 적색.</li>
<li>0.01 M EDTA로 적색이 <b>전부 청색</b>이 될 때까지 적정 (a mL).</li></ol>
<div class="sec">[C. Ca 경도 적정] — pH 12, HNB</div>
<ol><li>시료 100 mL(메스실린더) → 200 mL 삼각플라스크.</li>
<li>20% NaOH <b>1 mL</b>(pH ≈ 12), 10% KCN <b>5방울</b>, 10% hydroxylamine HCl <b>5방울</b> → 잘 저은 뒤 <b>5분 방치</b> (Mg(OH)₂ 석출).</li>
<li>스패출러로 HNB 희석 분말을 소량 → 적색. 0.01 M EDTA로 <b>전부 청색</b>이 될 때까지 적정 (b mL).</li></ol>
<div class="sec">[D. Mg 경도] — 계산: 총경도 − Ca 경도</div>""",
side=card("trap", "✍️ 노트에 쓸 때", """<ul style="margin:0"><li><b>표준액 조제(f)</b>와 <b>적정 B·C</b>를 <b>단락·표를 나눠서</b> (교수님 코멘트)</li>
<li>실제로 한 대로: 시료 종류(수돗물·생수), 건조 여부, 실제 칭량값, 마이크로피펫, 제공된 시약</li>
<li>1회 측정이면 1회라고</li></ul>""")
 + prof("100 mL는 양이 많으니까 아주 정밀한 파이펫으로 옮기려고 하지 말고요. 메스실린더를 사용하도록 하세요. 메니스커스를 정확히 읽어가지고."))

tips = pg("p-tips", "5", "조작 요령 · 종말점 · 안전", "교수님 순회 지도", K2,
main="""<div class="sec">① 종말점 — 오늘은 변색이 느리다</div>
<ul><li>온도가 낮아서인지 종말점 변색이 <b>천천히</b> 일어남 → 색이 변하기 시작하면 적정 속도를 <b>확 떨어뜨리기</b>: 한 방울 넣고 한참 지켜보기.</li>
<li>\"<b>빨간색이 사라지는 순간</b>이 있어. 그때부터 조심.\" 색이 옅어지면 기다리면 점점 파래짐 → 완전히 청색이 되면 닫기.</li>
<li>멀리서 보면 색 차이가 잘 보임 (적색 플라스크와 나란히 비교).</li>
<li><b>줄줄 흘리지 말 것</b> — 너무 빨리 넣어 종말점을 확 넘긴 건 \"고찰거리인 <b>오차</b>가 아니라 명백한 <b>오류</b>\".</li>
<li>지시약이 너무 적으면 색이 금방 최대치가 되어 얼마나 넘었는지 알 수 없음. HNB는 너무 진해도 색 구분이 안 되니 <b>조금씩 넣어 보며</b> 적당히.</li></ul>
<div class="sec">② 기구</div>
<ul><li>시료 100 mL = 메스실린더, MgCl₂·NaOH 1 mL = <b>마이크로피펫</b> (1 mL 세팅; 2 mL는 두 번).</li>
<li>공통 시약은 오른쪽 → 용액 병을 들고 다니다 깨지 않도록 <b>플라스크를 들고 가서</b> 넣기.</li></ul>
<div class="sec">③ 뒷정리</div>
<p>기구는 잘 씻어 바구니를 3조 자리에 반납, 마그네틱 스터러는 후드 안. 벤치 위에 아무것도 남기지 않기.</p>""",
side=card("trap", "☠ 안전: KCN(청산가리)", "<b>맹독</b>. 장갑 착용, 피부·입 접촉 금지. <b>산과 섞으면 HCN 가스</b>가 나오므로 산성 폐액과 섞지 말고 지정 폐액통에. <span class=\"ko\">(일반 안전 지식)</span>")
 + card("", "📌 공시험", "정리 중 질문: 보정계수 칸 — \"공시험을 했는데 공시험에 사용된 물 부피를 안 적어놔서\". 공시험을 했다면 <b>사용한 물 부피와 소비량</b>을 꼭 기록."))

disc = pg("p-disc", "6", "고찰 포인트 — 오차 원인 · 대책 · 개선 방안", "참값을 모르는 시료 → 범위·경향으로 판단", K3,
main="""<table class="t"><tr><th style="width:22%">원인</th><th>결과에 미치는 영향</th><th style="width:28%">대책 · 개선</th></tr>
<tr><td>종말점 지연 (낮은 온도, 느린 변색)</td><td>청색을 기다리다 과량 → a·b↑ → 경도 과대</td><td>종말점 근처 한 방울씩, 충분히 기다림, 적색 대조 플라스크</td></tr>
<tr><td>너무 빠른 적정</td><td>종말점 초과 (오차가 아니라 <b>오류</b>)</td><td>재측정</td></tr>
<tr><td>메스실린더로 100 mL 측정</td><td>±1 mL면 경도 ±1%</td><td>100 mL transfer pipet 사용</td></tr>
<tr><td>MgCl₂ 1.0 mL 부정확 · f 미적용</td><td>"−1" 보정 오차 → 총경도 오차</td><td>마이크로피펫 검정, 식 (a × f − 1)</td></tr>
<tr><td>EDTA 순도 99.5%·건조 여부</td><td>실제 EDTA↓ → f 과대 → 경도 과대</td><td>80 °C 1시간 건조, 순도 보정</td></tr>
<tr><td>Mg(OH)₂ 침전 불완전 / Ca 공침</td><td>Ca 경도 오차 → Mg 경도(차이값) 오차</td><td>5분 방치, pH 12 확인</td></tr>
<tr><td>가리움 불충분 (Fe, Cu, Mn)</td><td>EDTA 소비↑ 또는 지시약 방해</td><td>KCN·hydroxylamine 충분히</td></tr>
<tr><td>지시약 양</td><td>너무 적음 → 색 최대 빨리, 너무 많음 → 구분 어려움</td><td>적당량, 일정하게</td></tr>
<tr><td>1회 측정</td><td>재현성 확인 불가</td><td>3회 반복</td></tr></table>
<p class="ko">결과 해석: 음용수 기준(300 ppm) 이내인지, 표의 연수/경수 구분, Mg 경도가 0에 가까우면 그 의미(Mg(OH)₂ 침전 관찰과 연결), 다른 조의 물(에비앙·백산수·삼다수·수돗물)과 비교.</p>""",
side=prof("이거는 고찰이 아니라 명백한 실험적 오차가 아니고 오류야, 오류.")
 + card("tip", "📌 참값을 모르는 시료", "지난주 교수님 말씀처럼 경도의 참값은 모름 → \"오차\"를 단정하지 말고, 기준·예상 범위(수돗물 ≈ 60 ppm 등)와 비교해 <b>타당성</b>을 논의."))

QA = [
("Q1. 물의 경도란?", "Ca²⁺와 Mg²⁺의 양을 모두 CaCO₃의 양으로 환산해 ppm으로 나타낸 것."),
("Q2. 1 ppm의 의미는?", "1 g / 10⁶ mL = 1 μg/mL. 물 1톤에 CaCO₃ 1 g."),
("Q3. 우리나라 음용수 총경도 기준은?", "300 ppm 이하 (실제로는 100 ppm 이하가 좋다고 봄)."),
("Q4. 연수(단물)의 기준은?", "0–75 ppm (75–150 비교적 약한 경수, 150–300 경수, >300 아주 강한 경수)."),
("Q5. 지시약의 유리형·결합형 색은?", "유리형(HIn²⁻) 청색, 금속 결합형(MIn⁻) 적색. 종말점 = 적색 → 청색."),
("Q6. 수돗물에 지시약을 넣으면? 탈이온수면?", "수돗물은 적색(금속 있음), 탈이온수는 청색."),
("Q7. CaY²⁻와 MgY²⁻의 log K<sub>f</sub>는?", "10.65와 8.79. EDTA와 금속은 1 : 1."),
("Q8. 가리움제를 쓰는 이유와 예는?", "EDTA는 선택성이 없어 Fe·Cu·Mn 등과도 반응 → KCN 등으로 먼저 가림."),
("Q9. 총경도 측정에 MgCl₂ 1 mL를 넣는 이유는?", "EBT 종말점 색 변화를 선명하게 하려고. 넣은 만큼 식에서 1을 뺀다."),
("Q10. Ca 경도 측정에서 NaOH를 넣는 이유는?", "pH ≈ 12로 만들어 Mg를 Mg(OH)₂로 침전시켜 Ca만 적정."),
("Q11. 총경도·Ca 경도의 지시약과 pH는?", "총경도 EBT, pH 10(암모니아 완충액) / Ca 경도 HNB, pH 12."),
("Q12. 0.01 M EDTA 1 mL는 CaCO₃ 몇 mg?", "1.000 mg (100.0869 × 0.01)."),
("Q13. 총경도·Ca·Mg 경도 식은?", "(a × f − 1) × 1000/시료 mL, b × f × 1000/시료 mL, 총경도 − Ca 경도."),
("Q14. 시료 100 mL, f = 1, 총경도 100 ppm이면 a는?", "11 mL (10 아님). 300 ppm이면 31 mL."),
("Q15. EDTA 표준액을 표정하지 않는 이유는?", "disodium EDTA dihydrate(99.5%)가 1차 표준물질 → 칭량값으로 f = 실제/이론."),
("Q16. 0.01 M EDTA 250 mL에 필요한 이론량은?", "0.01 × 0.250 × 372.25 = 0.9306 g (≈ 0.931 g)."),
]


def qa(items):
    return "".join(f'<div class="qa"><div class="q">{q}</div><div class="a">{a}</div></div>' for q, a in items)


check = card("tip", "📝 실험노트 체크리스트 (실험 4)", """<ul style="list-style:none;padding-left:0;margin:0">
<li>□ 페이지 번호 실험 3에서 이어서, 1권, 서명은 머리말/꼬리말</li>
<li>□ 원리 최소 반 페이지 (경도 정의·ppm, 반응식·K<sub>f</sub>, 지시약 색, 가리움제, MgCl₂, pH 10/12)</li>
<li>□ <b>[표준액 조제(f)]와 [적정]을 구분</b>해서 방법·결과 기재 (교수님 코멘트)</li>
<li>□ 실제 한 대로: 시료 종류, 건조 여부, 실제 칭량값, 메스실린더·마이크로피펫, 제공된 시약</li>
<li>□ 결과: EDTA 칭량값·f(셋째 자리), a·b의 시작·최종 눈금(둘째 자리), 총·Ca·Mg 경도 계산 과정</li>
<li>□ 고찰: 기준 300 ppm·연수/경수 판정, Mg(OH)₂ 관찰, 원인 · 대책 · 개선</li>
<li>□ 부착물: 노트 번호 + 부착 페이지, 겹치게 간인</li></ul>""")

qa1 = pg("p-qa", "7", "기말 대비 핵심 체크 (Q&amp;A) ①", "Q1–Q8", K3, main=qa(QA[:4]), side=qa(QA[4:8]))
qa2 = pg("p-qa2", "7", "기말 대비 핵심 체크 (Q&amp;A) ② · 노트 체크리스트", "Q9–Q16", K3, main=qa(QA[8:]), side=check)

E = [cover, notice, over, hard, edta, mask, calcf, reag, meth, tips, disc, qa1, qa2]
