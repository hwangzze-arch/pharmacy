# -*- coding: utf-8 -*-
"""실험2 지시약을 이용한 식초 중의 총 산도 측정 — 실험1 요약정리와 같은 양식"""
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

FLOW = """<svg viewBox="0 0 680 190" class="svgf">
<g class="box"><rect x="4" y="10" width="150" height="62" rx="8"/><rect x="190" y="10" width="150" height="62" rx="8"/>
<rect x="376" y="10" width="140" height="62" rx="8"/><rect x="552" y="10" width="124" height="62" rx="8" class="hl"/>
<rect x="4" y="112" width="150" height="62" rx="8"/><rect x="190" y="112" width="150" height="62" rx="8"/>
<rect x="376" y="112" width="140" height="62" rx="8"/><rect x="552" y="112" width="124" height="62" rx="8" class="hl"/></g>
<g class="bt"><text x="79" y="36">KHP 약 2.042 g</text><text x="79" y="56">정밀하게 칭량</text>
<text x="265" y="36">100 mL 용량플라스크</text><text x="265" y="56">물 반쯤 → 녹이고 → 표선</text>
<text x="446" y="36">20.00 mL 분취</text><text x="446" y="56">+ 지시약 2방울</text>
<text x="614" y="36">NaOH 적정</text><text x="614" y="56">→ f (셋째 자리)</text>
<text x="79" y="138">식초 10.00 mL</text><text x="79" y="158">피펫으로 정확히</text>
<text x="265" y="138">100 mL 용량플라스크</text><text x="265" y="158">표선까지 희석 (10배)</text>
<text x="446" y="138">20.00 mL 분취</text><text x="446" y="158">+ 물 20 mL + 지시약</text>
<text x="614" y="138">NaOH 적정</text><text x="614" y="158">→ 총산도 (w/v%)</text></g>
<g class="ar"><path d="M156 41 h30"/><path d="M342 41 h30"/><path d="M518 41 h30"/>
<path d="M156 143 h30"/><path d="M342 143 h30"/><path d="M518 143 h30"/><path d="M614 74 v34"/></g>
<text x="626" y="96" class="sm">f 사용</text>
<text x="4" y="104" class="sm okt">① 표정 (NaOH의 진짜 농도)</text>
<text x="4" y="188" class="sm okt">② 식초 총산도 측정</text>
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
<div class="cv-left"><div class="cv-k">의약품분석학 실험 · 실험 2 · 산·염기 중화 적정</div>
<div class="cv-h">실험 2.<br>지시약을 이용한<br>식초 중의 총 산도 측정</div>
<div class="cv-flow">자료: 실험2 유인물 1–2쪽 + 수업 녹취록(약 95분) 요약</div>
<div class="cv-txt"><b>한 줄 요약</b> — 일차표준물질 <b>KHP</b>로 NaOH 표준액을 <b>표정</b>해서 진짜 농도(규정도계수 <b>f</b>)를 구하고,
그 <b>f로</b> 식초를 적정해 들어 있는 모든 유기산을 <b>초산으로 환산한 농도(총산도, w/v%)</b>를 구한 실험.</div>
<div class="cv-eq">f = B / 0.100 &nbsp;(B = KHP mmol ÷ V<sub>b</sub>)<br>총산도(w/v%) = 0.1 × f × V<sub>b</sub> × 60.05 × 10⁻³ ÷ 실제 적정한 식초(mL) × 100</div></div>
<div class="cv-toc"><div class="t">CONTENTS</div>
<div class="row"><span class="n">0</span><span class="nm">실험노트 피드백 · 오늘의 과제</span><span class="pg">{PAGE:p-notice}</span></div>
<div class="row"><span class="n">0</span><span class="nm">오늘 한 일 한눈에</span><span class="pg">{PAGE:p-over}</span></div>
<div class="row"><span class="n">1</span><span class="nm">목적 · 총산도란?</span><span class="pg">{PAGE:p-purpose}</span></div>
<div class="row"><span class="n">2</span><span class="nm">원리 ① NaOH 표준액의 표정 (KHP)</span><span class="pg">{PAGE:p-std}</span></div>
<div class="row"><span class="n">2</span><span class="nm">원리 ② 과제: KHP(중간형) 용액의 pH</span><span class="pg">{PAGE:p-ph}</span></div>
<div class="row"><span class="n">2</span><span class="nm">원리 ③ 페놀프탈레인 지시약 · 종말점</span><span class="pg">{PAGE:p-ind}</span></div>
<div class="row"><span class="n">2</span><span class="nm">원리 ④ 식초 총산도 계산식</span><span class="pg">{PAGE:p-acid}</span></div>
<div class="row"><span class="n">3·4</span><span class="nm">시약 및 기구 · 실험방법</span><span class="pg">{PAGE:p-meth}</span></div>
<div class="row"><span class="n">5</span><span class="nm">조작 요령 · 폐액</span><span class="pg">{PAGE:p-tips}</span></div>
<div class="row"><span class="n">6</span><span class="nm">계산 예시 (녹취록 값)</span><span class="pg">{PAGE:p-calc}</span></div>
<div class="row"><span class="n">7</span><span class="nm">고찰 포인트 — 오차 원인 · 대책 · 개선</span><span class="pg">{PAGE:p-disc}</span></div>
<div class="row"><span class="n">8</span><span class="nm">기말 대비 Q&amp;A · 노트 체크리스트</span><span class="pg">{PAGE:p-qa}</span></div></div>
<div class="cv-src">의약품분석학 실험 「실험 2: 식초 중의 총 산도 측정」 유인물 1–2쪽 · 수업 녹취록</div>
""")

notice = pg("p-notice", "공지", "실험노트 피드백 · 오늘의 과제", "지난주(실험 1) 노트 채점 후 교수님 피드백", K0,
main=card("trap", "✍️ 실험노트 형식 피드백", """<ul style="margin:0">
<li><b>페이지 일련번호</b>를 매 페이지에. 지금 쓰는 노트는 <b>"1권"</b> (노트 번호). 노트가 여러 권이 되면 2권, 3권…</li>
<li><b>부착물(표·그래프)</b>에도 <b>노트 번호 + 부착된 페이지 번호</b>를 적기 → 떨어져 나왔을 때 어디서 나왔는지 알 수 있게.</li>
<li><b>서명</b>은 페이지 중간이 아니라 <b>머리말이나 꼬리말</b>(위·아래 여백)에, <b>매 페이지마다</b>.</li>
<li><b>부착물 서명(간인)</b>: 부착물 안에만 하지 말고 <b>부착물과 노트 공란에 겹치도록</b>. 그래야 떨어졌을 때 맞춰 볼 수 있다.</li>
<li><b>여백 표시</b>: 글자 옆 자잘한 빈칸은 표시할 필요 없음. <b>왼쪽부터 오른쪽까지 위아래가 완전히 빈 공간</b>에만 <b>빗금 한 줄</b>. (너무 과격하게 그으면 지저분)</li>
<li><b>차트(그래프)는 엑셀로</b> 그려서 출력·부착. 손으로 그리지 말 것(부정확).</li>
<li><b>고찰</b>: 결과가 이론값(예: 보정치 ±0.1)을 크게 벗어나도 감점은 없지만, 고찰에 <b>원인 · 대책 · 개선 방안</b>을 논리적으로 유추해서 반드시 쓸 것. 결과가 명백히 잘못됐는데 고찰이 비어 있으면 안 됨.</li></ul>"""),
side=prof("일부 학생들은 실험 노트를 감동적으로 썼더라. 눈물 날 뻔했어. 특히 3조가 대단하더라고. 나중에 시간 될 때 한 번 봐요.")
 + card("tip", "📝 오늘의 과제 (노트에 기재)", """<ol style="margin:0">
<li>일차표준물질 <b>KHP(중간형) 용액의 이론적 pH</b>를 계산해서 노트에 적기 → {REF}</li>
<li>제조사 팩터(f = 1.000)를 쓰지 말고 <b>직접 표정해서 구한 f(소수 셋째 자리)</b>로 식초의 총산도 계산. 계산 과정과 결과 모두 기재. <b>안 쓰면 감점</b>.</li>
<li>계산은 만든 총량(100 mL)이 아니라 <b>실제 적정에 사용한 분취량</b> 기준 (KHP는 20%, 식초도 실제 사용한 양).</li></ol>""".replace("{REF}", "p.{PAGE:p-ph}"))
 + card("", "🧾 기타", "지난주 노트를 안 가져온 사람 한 명 있었음. 2조 대신 4조가 청소 → 다음에 4조 차례 때 2조가 하기."))

over = pg("p-over", "한눈에", "오늘 한 일 — 표정 → 총산도", "Overview", K0,
core="검정한 뷰렛으로 첫 <b>산·염기 중화 적정</b>. ① KHP로 NaOH의 <b>f</b>를 구하고 ② 그 f로 식초를 적정해 <b>총산도(w/v%)</b>를 구한다.",
main=FLOW + """<div class="sec">🧪 오늘의 분담 (시약이 부족해서)</div>
<ul><li><b>KHP 표준용액</b>: 홀수 조(1·3·5·7조)만 100 mL 제조 → 1·2조, 3·4조, 5·6조, 7·8조가 나눠 씀 (조당 20 mL만 필요).</li>
<li><b>식초 시료</b>: 50 mL씩 4병 → 두 조당 1병 (조당 10 mL 필요).</li>
<li><b>NaOH 표준액</b>(삼전순약, 0.1 M, f = 1.000 표기): 두 조당 1병.</li>
<li>표정과 식초 적정은 <b>순서 상관없음</b> (KHP 용액 기다리는 동안 식초 먼저 해도 됨). f는 계산할 때만 쓰니까.</li></ul>""",
side=card("trap", "⚠️ 이번 실험에서 생략된 것 (= 고찰거리)", """<ul style="margin:0">
<li>CO₂ 제거한 증류수(5분 끓임) → <b>생략</b>, 그냥 탈이온수 사용</li>
<li>KHP 110 °C 1시간 건조 → <b>생략</b>, 바로 칭량</li>
<li>표정 2회 반복 → <b>1회만</b></li>
<li>식초 적정 3회 반복 · 평균 · 표준편차 → <b>1회만</b></li>
<li>지시약 용액 제조 → 이미 만들어 둠 (바구니의 갈색 작은 병)</li></ul>""")
 + prof("일부러 여러분들 디스커션 할 게 많아지도록 배려를 하는 거예요. 완벽한 실험은 없습니다."))

purpose = pg("p-purpose", "1", "목적 · 총산도(total acidity)란?", "유인물 1쪽 1. 목적", K1,
core="<b>목적</b>(유인물): 표정을 통해 염기 표준액의 정확한 농도를 결정하고, 중화적정법의 예로서 이 표준액을 이용하여 식초 중의 총 산도를 측정한다.",
main="""<div class="sec">총산도의 의미</div>
<ul><li>식초에는 주로 <b>아세트산(초산, acetic acid)</b>이 들어 있지만, 특히 <b>발효 양조식초</b>는 발효 과정에서 여러 가지 <b>유기산</b>이 생긴다.</li>
<li>NaOH로 중화 적정하면 초산만 골라서 적정할 방법이 없다 → <b>적정 가능한 모든 유기산이 함께 적정</b>된다.</li>
<li>그래서 결과를 "초산의 농도"라고 부를 수 없다. 대신 <y>모든 유기산을 초산이라고 간주하고</y> 계산한다.</li>
<li>→ <b>총산도</b> = 용액 중 적정 가능한 모든 유기산의 농도를 <b>초산 농도로 환산</b>해 나타낸 것.</li></ul>
<div class="fbox"><div class="sec f">📐 단위 = w/v% (weight per volume percent)</div>
<span class="fx">총산도 5 w/v% = 식초 100 mL 중에 초산으로 환산된 유기산이 5 g</span></div>
<div class="sec">왜 NaOH(강염기)인가?</div>
<p>유기산·초산은 <b>약산</b> → 약산은 <b>강알칼리</b>로 적정해야 한다. 0.1 M(= 0.1 N) NaOH 표준액을 적정제로 사용. 약산 + 강염기 반응은 평형상수가 매우 커서(초산: K = K<sub>a</sub>/K<sub>w</sub> = 10<sup>14−4.756</sup> ≈ 1.8 × 10⁹) 빠르고 완벽하게 반응한다 (1학기 내용).</p>""",
side=prof("그 모든 유기산을 다 초산이라고 간주하고 계산하는 거예요. 그게 총산도의 의미예요. 초산의 농도라고 부르지 못하니까 그냥 총산도라고 부르는 거예요.")
 + card("ana", "🎈 비유", "여러 나라 돈이 섞인 지갑을 <b>전부 원화로 환산</b>해서 \"총 얼마\"라고 말하는 것. 실제로는 달러·엔이 섞여 있어도 원화 기준 총액으로 표시 → 총산도는 모든 산을 <b>초산 기준</b>으로 환산한 총액."))

std = pg("p-std", "2-①", "NaOH 표준액의 표정 — 일차표준물질 KHP", "유인물 1쪽 [0.1 M NaOH 표준용액의 표정]", K1,
core="제조사 f(1.000)를 <b>믿지 말고</b>, 일차표준물질 <b>KHP</b>로 직접 적정해 <b>규정도계수 f</b>를 구한다. KHP와 NaOH는 <b>1 : 1</b>로 반응.",
main="""<ul><li><b>표준액</b> = 규정도계수(factor, f)를 아는 용액. 구매한 NaOH(삼전순약)에는 f = 1.000 (0.999 ~ 1.001)이라 적혀 있다 → 0.1 M이라고 주장.</li>
<li>"우리는 의심이 많아요. 못 믿겠어." → 원래 필요 없지만 <b>표정 연습</b>을 위해 직접 확인.</li>
<li>강염기를 표정하려면 <b>일차표준물질 약산</b>이 필요 → <b>KHP</b>(potassium hydrogen phthalate, FM 204.221, pK₁ = 2.9, pK₂ = 5.5).</li>
<li>프탈산은 카복실산이 2개인 <b>이가산</b> → 산성형 · <b>중간형</b> · 염기성형. KHP는 <b>중간형</b>(–COOK, –COOH) → 남은 –COOH 하나가 NaOH와 <b>1 : 1</b>.</li></ul>
<div class="fbox"><div class="sec f">📐 규정도계수 계산 (유인물)</div>
<span class="fx">A(g) / 204.221(g/mol) × 10³ (mmol/mol) = B (mmol/mL) × V<sub>b</sub> (mL)</span><br>
<span class="fx">B (mmol/mL) = A × 10³ / (204.221 × V<sub>b</sub>)</span> &nbsp; <span class="fx">f = B / M₀ = B / 0.100</span></div>
<div class="ebox"><div class="sec e">⚠️ A = 실제로 적정한 KHP 양</div>
KHP 2.042 g → 100 mL 중 <b>20.00 mL(20%)</b>만 적정 → <b>A = 2.042 × 20/100 = 0.4084 g</b> (= 1.9998 mmol). 2.042 g을 그대로 넣으면 "황당한 팩터"가 나온다.</div>""",
side=fig("khp", "유인물 1쪽 — KHP + NaOH → KNaP + H₂O (1차 표준물질 KHP, FM 204.221)", 130)
 + prof("공장의 전문가가 훨씬 더 정확하겠죠. 그렇지만 우리는 자신감을 가지고 <b>여러분들이 구한 팩터</b>를 가지고 계산해야 됩니다. 팩터는 <b>소수점 이하 셋째 자리</b>까지.")
 + card("tip", "📌 f의 의미", "f = 실제 농도 / 표시 농도. f = 1.026이면 \"0.1 M\"이라던 NaOH가 실제로는 0.1026 M."))

ph = pg("p-ph", "2-②", "과제 — KHP(중간형) 용액의 이론적 pH", "적정 시작 전에 용액이 산성인지 알고 시작하기", K1,
core="중간형(양쪽성) 화학종의 pH ≈ <b>(pK₁ + pK₂) / 2 = (2.9 + 5.5) / 2 = 4.2</b> → KHP 용액은 <b>약산성</b>. 정확한 식으로 풀어도 <b>pH ≈ 4.20</b>.",
main="""<div class="sec">① 몰농도 (유인물: "제조된 용액의 몰농도 및 pH를 계산하여 계산식과 결과를 기재")</div>
<p><span class="fx">C = 2.042 g ÷ 204.221 g/mol ÷ 0.1000 L = 0.09999 M ≈ 0.1000 M</span> <span class="ko">(실제 칭량값으로 바꿔 계산)</span></p>
<div class="sec">② 중간형 pH 식 (1학기)</div>
<div class="fbox"><span class="fx">[H⁺] = √[(K₁K₂C + K₁K<sub>w</sub>) / (K₁ + C)]</span><br>
K₁ = 10<sup>−2.9</sup> = 1.26 × 10⁻³, K₂ = 10<sup>−5.5</sup> = 3.16 × 10⁻⁶, C = 0.1000 M</div>
<ul><li>K₁K₂C = 1.26 × 10⁻³ × 3.16 × 10⁻⁶ × 0.1000 = 3.98 × 10⁻¹⁰</li>
<li>K₁K<sub>w</sub> = 1.26 × 10⁻¹⁷ → 무시 가능 &nbsp;·&nbsp; K₁ + C = 0.1013</li>
<li>[H⁺] = √(3.98 × 10⁻¹⁰ / 0.1013) = √(3.93 × 10⁻⁹) = 6.27 × 10⁻⁵ M</li>
<li><b>pH = 4.20</b></li></ul>
<div class="ebox"><div class="sec e">근사식</div>C ≫ K₁ 이고 K₁K₂C ≫ K₁K<sub>w</sub> 이면 <span class="fx">[H⁺] ≈ √(K₁K₂) → pH ≈ (pK₁ + pK₂)/2 = 4.2</span> — 농도와 거의 무관.</div>""",
side=card("tip", "📌 그래서 무엇을 알 수 있나", "pH 4.2 = <b>산성</b> → 페놀프탈레인을 넣으면 <b>무색</b>이어야 정상. 넣자마자 분홍색이면 뭔가 잘못된 것 → 씻고 다시.")
 + card("ana", "📐 참고: 당량점 pH (지시약 선택 근거)", """<ul style="margin:0"><li>KHP 표정 당량점: 프탈레이트(P²⁻) ≈ 2.00 mmol / 39.5 mL = 0.0506 M, pK<sub>b</sub> = 14 − 5.5 = 8.5 → pOH = ½(8.5 − log 0.0506) = 4.90 → <b>pH ≈ 9.1</b></li>
<li>식초 적정 당량점: 아세트산 이온 ≈ 0.034 M, pK<sub>b</sub> = 9.244 → <b>pH ≈ 8.6</b></li>
<li>둘 다 약알칼리 → 변색 범위 pH 8.0–9.6인 <b>페놀프탈레인</b>이 적합</li></ul>""")
 + prof("일차표준물질이 중간형이다, 그러면 이걸 물에 녹였을 때 pH가 산성인지 중성인지 염기성인지 그걸 알고는 시작해야 된다."))

ind = pg("p-ind", "2-③", "페놀프탈레인 지시약 · 종말점 잡는 법", "유인물 1쪽 [Phenolphthalein 지시약] · 목시 적정", K1,
core="산을 강염기로 적정 → pH가 <b>올라가는</b> 방향. 페놀프탈레인은 <b>무색(pH &lt; 8.0) → 분홍(pH &gt; 9.6)</b>. 종말점 = <b>옅은 분홍이 사라지지 않고 지속</b>되는 순간.",
main="""<ul><li>지시약 자체도 산 또는 염기. 페놀프탈레인은 페놀(–OH) 2개 → <b>산성 지시약</b>. 산성형 = <b>무색</b>, 염기성형 = <b>분홍</b>.</li>
<li>적정 전 지시약 <b>2–3방울</b> → <b>무색 확인</b> (= pH 7 미만). 분홍이면 잘못된 것 → 씻고 다시 시작.</li>
<li>적정 중: 떨어진 자리에 분홍이 <b>나타났다 사라지기</b>를 반복 (계속 반응 중이니까) → 사라지는 속도가 점점 느려짐 = 종말점 근처.</li>
<li>처음엔 조금 빠르게(똑똑똑), 근처에서는 속도를 <b>극도로 낮춰</b> → <b>한 방울(반 방울) 넣고 한참 관찰</b> 반복.</li>
<li><b>더 이상 사라지지 않고 분홍이 지속</b>되면 바로 멈춤. 계속 가면 종말점을 넘는다.</li>
<li>사라질 수도 있으니 <b>교반을 조금 더 세게</b> 해서 확인.</li></ul>
<div class="ebox"><div class="sec e">⭐ 두 적정의 색을 똑같이 맞추기</div>
표정(KHP) 종말점의 <b>분홍 진하기를 기억</b>(사진 찍거나 플라스크를 옆에 두기) → 식초 적정도 <b>같은 색</b>에서 멈춤 → <b>지시약 오차가 서로 상쇄</b>된다.</div>""",
side=fig("php", "유인물 1쪽 — Colorless phenolphthalein (pH &lt; 8.0) ⇌ Pink phenolphthalein (pH &gt; 9.6)", 150)
 + prof("핑크색 진하기를 잘 기억했다가, 다음 식초 적정할 때도 똑같은 색깔에서 멈추면 돼요. 두 적정의 색깔을 똑같이 맞춰주면 지시약 오차가 서로 상쇄가 되거든요."))

acid = pg("p-acid", "2-④", "식초의 총산도 계산식", "유인물 1쪽 [식초의 총 산도 측정]", K1,
core="CH₃COOH + NaOH → CH₃COONa + H₂O (<b>1 : 1</b>, FM 60.05, pK<sub>a</sub> = 4.756). 계산은 <b>실제 적정한 식초 양</b> 기준.",
main="""<div class="fbox"><div class="sec f">📐 유인물 식</div>
<span class="fx">초산(g) = 0.1 (mmol/mL) × f × V<sub>b</sub> (mL) × 60.05 (mg/mmol) × 10⁻³ (g/mg)</span><br>
<span class="fx">식초의 총산도 (w/v%) = 초산(g) / 식초(mL) × 100</span></div>
<ul><li>0.1 × f = NaOH의 <b>실제 농도</b>(mmol/mL) → × V<sub>b</sub> = 반응한 NaOH mmol = 초산 mmol (1:1)</li>
<li>× 60.05 mg/mmol × 10⁻³ = 초산 g</li>
<li>f는 <b>직접 표정한 값</b> (1.000 쓰면 감점)</li></ul>
<div class="ebox"><div class="sec e">⚠️ "식초(mL)" = 실제로 적정한 식초 원액의 양</div>
식초 10.00 mL → 100 mL로 희석(10배) → 그중 20.00 mL 적정<br>
→ 적정한 식초 원액 = <b>10.00 × 20.00/100 = 2.000 mL</b> (100 mL, 10 mL를 넣으면 틀림)</div>
<p>참고: 일가산 초산의 pH = ½(pK<sub>a</sub> − log C). 총산도가 약 6%면 원액 C ≈ 1.0 M → pH ≈ 2.4 (약산성에서 시작 → 끝나면 pH &gt; 8 약알칼리 → 분홍).</p>""",
side=prof("실제로 우리가 적정에 사용한 KHP는 2.042 g의 20%인 거예요. 안 그러면 숫자가 엉망으로 나와요, 황당한 팩터가 나올 거예요. 식초도 마찬가지. 모든 적정은 실제로 사용한 양으로 계산합니다.")
 + card("trap", "⚠️ 흔한 실수", "<ul style=\"margin:0\"><li>KHP에 2.042 g 전체를 넣음 → f가 5배</li><li>식초(mL)에 10 mL나 20 mL를 넣음 → 총산도가 1/5 또는 1/10</li><li>f 대신 1.000 사용 → 감점</li></ul>"))

meth = pg("p-meth", "3·4", "시약 및 기구 · 실험방법", "유인물 1–2쪽 (생략한 단계 표시)", K2,
main="""<p><b>시약 및 기구</b>: 0.1 M NaOH standard solution, potassium hydrogen phthalate (KHP), phenolphthalein, ethanol, buret (50 mL, 1 ea) &amp; stand, buret holder, volumetric flask (100 mL, 200 mL), Erlenmeyer flask (100 mL), graduated pipet (20 mL), pipet aid, chemical balance, indicator bottle</p>
<div class="sec">[CO₂가 제거된 증류수 제조] <span class="tag j">생략</span></div>
<p>증류수를 5분간 끓인 후 폴리에틸렌병에 붓고 마개를 잘 막아서 실온에 보관한다.</p>
<div class="sec">[0.2 w/v% phenolphthalein 지시약 용액의 제조] <span class="tag j">생략 · 준비됨</span></div>
<p>Phenolphthalein 0.2 g을 100 mL 용량플라스크에 넣고 에탄올 50 mL로 녹인 후 증류수를 표선까지 가하고 섞어 준다.</p>
<div class="sec">[알칼리표준액의 표정]</div>
<ol><li>KHP를 110 °C에서 1시간 건조 후 데시케이터에서 식힌다 <span class="tag j">건조 생략</span>. KHP 약 2.042 g을 정밀하게 달아 100 mL 용량플라스크에 넣고 증류수 약 70 mL(대충 반)를 가해 녹인 후, 완전히 녹으면 표선까지 가하고 섞는다. 용액의 <b>몰농도 및 pH를 계산</b>해 계산식과 결과를 노트에 기재한다.</li>
<li>1의 용액 <b>20.00 mL</b>를 pipet으로 정확히 취해 100 mL 삼각플라스크에 넣고 지시약 <b>두 방울</b> → 0.1 M NaOH로 적정한다.</li>
<li>2를 두 번 반복해 평균 <span class="tag j">생략, 1회</span>. 규정도계수를 계산하고 식초 산도 측정에 활용한다.</li></ol>
<div class="sec">[식초의 총 산도 측정]</div>
<ol><li>식초 <b>10.00 mL</b>를 pipet으로 정확히 취해 100 mL 용량플라스크에 넣고 증류수를 표선까지 가하고 섞는다.</li>
<li>희석한 식초 <b>20.00 mL</b>를 100 mL 삼각플라스크에 넣고 (물 20 mL 추가) 지시약 두 방울 → 0.1 M NaOH로 적정한다.</li>
<li>2를 세 번 반복 <span class="tag j">생략</span>. 4. 식초 100 mL에 함유된 초산의 양(g)으로 총산도(w/v%)를 구한다. 평균·표준편차 <span class="tag j">생략</span>.</li></ol>""",
side=prof("처음부터 표선까지 꽉 채워서 녹이지 말고. 녹는 과정에서 부피가 변할 수 있고, 공간이 있어야 잘 섞이잖아요. 대충 반 정도 넣고 고체가 다 녹으면 표선까지 채우고 마지막에 섞어줘야 돼요.")
 + card("tip", "🧪 학생 팁 (녹취록)", "<ul style=\"margin:0\"><li>피펫이 용량플라스크 입구에 안 들어가면 → <b>비커에 조금 따라서</b> 빨아올리기</li><li>다 녹으면 마개 막고 <b>위아래로 뒤집어</b> 섞기</li><li>식초 묻은 피펫은 한 번 씻고 KHP에 사용</li></ul>"))

tips = pg("p-tips", "5", "조작 요령 · 안전 · 폐액", "교수님 순회 지도 + 녹취록", K2,
main="""<div class="sec">① 뷰렛 준비 (이번엔 진짜 NaOH)</div>
<ul><li>강알칼리 → <b>반드시 장갑</b>.</li>
<li>물로 먼저 씻지 말 것 (그 물을 또 없애야 함) → 처음부터 <b>NaOH를 조금씩 부어 내벽을 세척(린싱)</b>하고 버림(폐수통) → 충분히 세척되면 채움.</li>
<li>지난번처럼 액체가 지나는 <b>모든 경로에 기포 없이</b>. 0.00에 꼭 맞출 필요 없이 넉넉히 채우고 <b>시작 눈금만 정확히</b> 읽기 (한 번에 약 20 mL 사용).</li>
<li>모든 준비가 끝날 때까지는 <b>밑에 비커</b>를 받쳐 두고, 다 되면 그때 시료 플라스크로 교체 (한 방울 떨어지면 처음부터 다시).</li>
<li>적정 전 <b>뷰렛 위 깔때기는 빼기</b> → 깔때기에 묻은 액체가 흘러내리면 부피 오차.</li></ul>
<div class="sec">② 피펫 + 피펫 필러</div>
<ul><li>필러를 <b>다 밀어 넣은 상태</b>에서 피펫을 살짝 밀착해 꽂고 → <b>바퀴를 굴려</b> 압력으로 빨아올림 (먼저 쭉 당겨놓고 넣으면 안 됨).</li>
<li>20 mL 표선보다 <b>충분히 넘게</b> 올린 뒤, 눈높이 맞춰 조금씩 빼서 메니스커스를 표선에.</li></ul>
<div class="sec">③ 적정</div>
<ul><li>적정은 화학 반응 → <b>반드시 교반</b> (마그네틱 바 + 스터러).</li>
<li>약 20 mL 들어갈 것을 예상 → 그 전까지는 비교적 빠르게, 근처에서 한 방울씩.</li></ul>""",
side=card("trap", "🗑 폐액", "<ul style=\"margin:0\"><li>수돗가: <b>물, 순수한 식초</b>만 (식품이라 OK, 냄새나니 물 많이 틀고)</li><li>그 외 <b>KHP, NaOH, 지시약 섞인 용액(분홍 용액) 등은 전부 폐수통</b></li></ul>")
 + card("", "🧽 뒷정리", "뷰렛의 남은 NaOH는 폐수통 → 수돗물로 충분히 → 탈이온수로 마지막 헹굼 → 거꾸로 매달기. 초자는 헹궈서 바구니에 두고 퇴실.")
 + card("trap", "⚠️ 시약병 확인", "'MeOH'(메탄올)와 'NaOH' 병을 헷갈리지 말 것 (녹취록)."))

calc = pg("p-calc", "6", "계산 예시 — 녹취록에 나온 값으로", "실제 노트에는 우리 조의 칭량값·눈금으로 바꿔 계산", K3,
core="표정 V<sub>b</sub> = 34.50 − 15.00 = <b>19.50 mL</b> → <b>f = 1.026</b> &nbsp;·&nbsp; 식초 V<sub>b</sub> = 35.20 − 15.50 = <b>19.70 mL</b> → <b>총산도 ≈ 6.07 w/v%</b>",
main="""<div class="sec">① 규정도계수 f (KHP 2.042 g 가정)</div>
<ol><li>적정한 KHP: A = 2.042 g × 20.00/100.0 = <b>0.4084 g</b></li>
<li>KHP mmol = 0.4084 × 10³ / 204.221 = <b>1.9998 mmol</b></li>
<li>B = 1.9998 mmol / 19.50 mL = <b>0.10255 mmol/mL</b></li>
<li>f = B / 0.100 = 1.0255 → <b>f = 1.026</b> (셋째 자리)</li></ol>
<div class="sec">② 식초 총산도 (f = 1.026)</div>
<ol><li>초산(g) = 0.1 × 1.026 × 19.70 × 60.05 × 10⁻³ = <b>0.1214 g</b></li>
<li>적정한 식초 원액 = 10.00 × 20.00/100.0 = <b>2.000 mL</b></li>
<li>총산도 = 0.1214 / 2.000 × 100 = <b>6.07 w/v%</b></li></ol>
<table class="t"><tr><th></th><th>시작 눈금</th><th>최종 눈금</th><th>V<sub>b</sub></th><th>결과</th></tr>
<tr><td>표정 (KHP 20.00 mL)</td><td>15.00</td><td>34.50</td><td>19.50 mL</td><td>f = 1.026</td></tr>
<tr><td>식초 (희석액 20.00 mL)</td><td>15.50</td><td>35.20</td><td>19.70 mL</td><td>6.07 w/v%</td></tr></table>""",
side=card("trap", "⚠️ 실제 노트 쓸 때", """<ul style="margin:0"><li>위 숫자는 <b>녹취록(AI 전사)</b>의 한 조 값. 실제 <b>KHP 칭량값(소수 넷째 자리)</b>, 시작·최종 눈금을 우리 조 기록으로 바꿀 것.</li>
<li>짝수 조는 홀수 조가 만든 KHP 용액을 썼으므로 <b>그 조의 칭량값</b>을 받아 적기.</li>
<li>뷰렛 눈금은 실험 1의 <b>검정곡선으로 시작·최종 모두 보정</b>해서 쓰면 더 정확 (고찰에 언급).</li>
<li>f = 1.000 쓰면 감점. f는 셋째 자리까지.</li></ul>""")
 + card("tip", "📌 f를 안 썼다면?", "f = 1.000으로 계산하면 0.1 × 1.000 × 19.70 × 60.05 × 10⁻³ / 2.000 × 100 = 5.92 w/v% → f 차이(2.6%)만큼 결과가 달라진다."))

disc = pg("p-disc", "7", "고찰 포인트 — 오차 원인 · 대책 · 개선 방안", "교수님: 결과가 이상하면 원인·대책·개선을 유추해서 쓸 것", K3,
main="""<table class="t"><tr><th style="width:22%">원인</th><th>결과에 미치는 영향</th><th style="width:28%">대책 · 개선</th></tr>
<tr><td><b>CO₂ 미제거 물</b> 사용 (끓이기 생략)</td><td>녹은 CO₂ → 탄산 → NaOH 소비. 식초 희석수에 있으면 V<sub>b</sub>↑ → <b>총산도 과대</b>. KHP 용해수에 있으면 V<sub>b</sub>↑ → <b>f 과소</b>.</td><td>5분 끓여 식힌 물을 마개로 막아 사용</td></tr>
<tr><td><b>KHP 건조 생략</b></td><td>수분만큼 실제 KHP가 적음 → V<sub>b</sub>↓ → 계산된 <b>f 과대</b> → 총산도도 과대</td><td>110 °C 1시간 건조, 데시케이터에서 냉각</td></tr>
<tr><td><b>1회 측정</b> (반복 생략)</td><td>우연오차를 평가할 수 없음, 평균·표준편차 없음</td><td>표정 2회, 식초 3회 이상 반복</td></tr>
<tr><td>종말점 판단 (지시약)</td><td>분홍 진하기 차이 → V<sub>b</sub> 오차. 넘기면 V<sub>b</sub>↑</td><td>두 적정 색 맞추기, 종말점 근처 반 방울씩</td></tr>
<tr><td>NaOH가 공기 중 CO₂ 흡수</td><td>Na₂CO₃ 생성 → 실제 농도 변화</td><td>병 마개 닫기, 사용 직전 표정</td></tr>
<tr><td>분취·희석 오차 (피펫·용량플라스크)</td><td>표선 맞춤·피펫 잔류액 → 적정량 오차</td><td>눈높이 맞추기, 피펫 린싱</td></tr>
<tr><td>뷰렛 눈금 오차</td><td>실험 1 보정치만큼 V<sub>b</sub> 오차</td><td>검정곡선으로 시작·최종 보정</td></tr>
<tr><td>다른 조가 만든 KHP 용액 (짝수 조)</td><td>칭량·제조 오차를 확인할 수 없음</td><td>직접 제조, 칭량값 기록 공유</td></tr></table>
<p class="ko">결과 비교: 제조사 f(1.000)와 내 f의 차이, 식초 라벨 산도(있으면)와 내 총산도의 차이를 원인과 연결해서 쓰기.</p>""",
side=prof("완벽한 실험은 없습니다. 탄산은 우리 경험상 큰 차이 없어요, 그렇게 많이 안 녹아 있어요. 그렇지만 모릅니다, 여기서 오차가 발생할 수 있고.")
 + prof("2, 4, 6, 8조는 실험 결과 안 나오면 1, 3, 5, 7조를 원망하면 돼요. 여러 가지 디스커션 할 게 많아지죠."))

QA = [
("Q1. 총산도란?", "적정 가능한 모든 유기산을 초산으로 간주해 초산 농도로 환산한 값. 단위 w/v%."),
("Q2. 총산도 5 w/v%의 의미는?", "식초 100 mL 중 초산으로 환산된 유기산이 5 g."),
("Q3. 왜 \"초산 농도\"라고 하지 않나?", "중화 적정은 초산만 선택적으로 적정할 수 없고 모든 유기산이 함께 적정되기 때문."),
("Q4. NaOH 표정에 쓰는 일차표준물질과 반응비는?", "KHP(potassium hydrogen phthalate, FM 204.221), NaOH와 1 : 1."),
("Q5. KHP는 프탈산의 어떤 형태이고 pH는?", "중간형(양쪽성). pH ≈ (pK₁ + pK₂)/2 = (2.9 + 5.5)/2 = 4.2."),
("Q6. 규정도계수 f 계산식은?", "B = A × 10³ / (204.221 × V<sub>b</sub>), f = B / 0.100. A는 실제 적정한 KHP 양(g)."),
("Q7. f는 몇 자리까지?", "소수점 이하 셋째 자리."),
("Q8. 페놀프탈레인의 색 변화와 범위는?", "산성형 무색(pH &lt; 8.0) → 염기성형 분홍(pH &gt; 9.6)."),
("Q9. 적정 전 지시약을 넣었더니 분홍이면?", "잘못된 것(이미 알칼리성) → 씻고 다시 시작."),
("Q10. 종말점은?", "옅은 분홍이 사라지지 않고 지속되는 지점."),
("Q11. 지시약 오차를 줄이는 방법은?", "표정과 시료 적정의 종말점 색을 똑같이 맞춘다 → 오차 상쇄."),
("Q12. 식초 총산도 식은?", "초산(g) = 0.1 × f × V<sub>b</sub> × 60.05 × 10⁻³, 총산도 = 초산(g)/식초(mL) × 100."),
("Q13. 식초 10 mL → 100 mL 희석 → 20 mL 적정 시 식초(mL)는?", "2.000 mL."),
("Q14. CO₂를 제거하지 않은 물을 쓰면?", "탄산이 NaOH와 반응 → 소비량 증가 → 총산도 과대평가."),
("Q15. 뷰렛을 물로 먼저 씻지 않고 NaOH로 헹구는 이유는?", "남은 물이 표준액을 묽히므로 → 사용할 표준액으로 린싱."),
("Q16. 페놀프탈레인을 쓰는 이유는?", "약산–강염기 적정의 당량점이 약알칼리(pH ≈ 8.6–9.1)라 변색 범위 8.0–9.6과 맞기 때문."),
]


def qa(items):
    return "".join(f'<div class="qa"><div class="q">{q}</div><div class="a">{a}</div></div>' for q, a in items)


check = card("tip", "📝 실험노트 체크리스트 (실험 2)", """<ul style="list-style:none;padding-left:0;margin:0">
<li>□ <b>1권</b>, 페이지 일련번호, 서명은 <b>머리말/꼬리말</b>에 매 페이지</li>
<li>□ 실험일자 = 실험한 날, 제목 · 목적 · 원리(반응식, f 식, 총산도 식) · 시약 및 기구</li>
<li>□ 과제: KHP 몰농도와 <b>pH 계산식 + 결과</b></li>
<li>□ 방법: 실제 한 대로(과거형) + 생략한 단계 명시</li>
<li>□ 결과: KHP 칭량값, 시작·최종 눈금, V<sub>b</sub>, <b>f(셋째 자리)</b>, 총산도 계산 과정 + 결과</li>
<li>□ 계산은 <b>분취량</b> 기준 (KHP 20%, 식초 2.000 mL)</li>
<li>□ 고찰: 원인 · 대책 · 개선 (CO₂, 건조 생략, 1회 측정, 종말점 색)</li>
<li>□ 부착물: 노트 번호 + 부착 페이지 번호, <b>겹치게 간인</b>, 그래프는 엑셀</li>
<li>□ 큰 빈 공간만 빗금 한 줄</li></ul>""")

qa1 = pg("p-qa", "8", "기말 대비 핵심 체크 (Q&amp;A) ①", "Q1–Q8", K3, main=qa(QA[:4]), side=qa(QA[4:8]))
qa2 = pg("p-qa2", "8", "기말 대비 핵심 체크 (Q&amp;A) ② · 노트 체크리스트", "Q9–Q16", K3, main=qa(QA[8:]), side=check)

E = [cover, notice, over, purpose, std, ph, ind, acid, meth, tips, calc, disc, qa1, qa2]
