# -*- coding: utf-8 -*-
"""실험5 요오드 적정법 (산화환원 적정) — 실험1~4 요약정리와 같은 양식 (유인물 3쪽 + 녹취록 2026-11-26)"""
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
<g class="bt"><text x="79" y="36">I₂ 표준액 0.05 M</text><text x="79" y="56">f = 병 라벨 (표정 X)</text>
<text x="265" y="36">I₂ 10 mL + 물 40 mL</text><text x="265" y="56">← Na₂S₂O₃ 적정</text>
<text x="446" y="36">미황색 → 전분</text><text x="446" y="56">청색 → 무색</text>
<text x="614" y="36">Na₂S₂O₃의 f′</text><text x="614" y="56">(간접법 표정)</text>
<text x="265" y="138">포비돈요오드액</text><text x="265" y="158">I 100 mg 상당 (10 mL)</text>
<text x="446" y="138">← Na₂S₂O₃ 적정</text><text x="446" y="158">미황색 → 전분 → 무색</text>
<text x="614" y="138">요오드 함량</text><text x="614" y="158">표시량 대비 %</text></g>
<g class="ar"><path d="M156 41 h30"/><path d="M342 41 h30"/><path d="M518 41 h30"/>
<path d="M342 143 h30"/><path d="M518 143 h30"/><path d="M614 74 v34"/></g>
<text x="626" y="96" class="sm">f′ 사용</text>
<text x="4" y="104" class="sm okt">① 아이오도메트리 (Na₂S₂O₃가 뷰렛)</text>
<text x="4" y="192" class="sm okt">② 뷰렛 교체 → 아이오디메트리: I₂ 표준액으로 아스코르브산 적정 (전분 처음부터, 무색 → 청색)</text>
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
<div class="cv-left"><div class="cv-k">의약품분석학 실험 · 실험 5 · 산화환원 적정 (마지막 적정)</div>
<div class="cv-h">실험 5.<br>요오드 적정법 —<br>포비돈요오드액 · 아스코르브산</div>
<div class="cv-flow">자료: 실험5 유인물 1–3쪽 + 수업 녹취록(2026-11-26, 약 63분) 요약</div>
<div class="cv-txt"><b>한 줄 요약</b> — 제조사 f가 있는 <b>I₂ 표준액</b>으로 Na₂S₂O₃를 <b>표정(간접법, f′)</b>하고,
<b>아이오도메트리</b>로 포비돈요오드액(완제 의약품)의 요오드를, <b>아이오디메트리</b>로 아스코르브산(원료 의약품)을 정량해
<b>대한약전 기준을 만족하는지</b> 판정한 실험.</div>
<div class="cv-eq">I₂ + 2S₂O₃²⁻ → 2I⁻ + S₄O₆²⁻ &nbsp;·&nbsp; C₆H₈O₆ + I₂ → C₆H₆O₆ + 2HI<br>
0.05 M I₂ (= 0.1 N) ↔ 0.1 M Na₂S₂O₃ : 부피 1 : 1로 대응</div></div>
<div class="cv-toc"><div class="t">CONTENTS</div>
<div class="row"><span class="n">0</span><span class="nm">공지 · 지난주 리뷰 · 결론 쓰는 법</span><span class="pg">{PAGE:p-notice}</span></div>
<div class="row"><span class="n">0</span><span class="nm">오늘 한 일 한눈에</span><span class="pg">{PAGE:p-over}</span></div>
<div class="row"><span class="n">1</span><span class="nm">요오드 적정 2종 — 아이오디 vs 아이오도</span><span class="pg">{PAGE:p-two}</span></div>
<div class="row"><span class="n">2</span><span class="nm">원리 ① 표준액 2개 · f와 f′ · 농도 1 : 2</span><span class="pg">{PAGE:p-std}</span></div>
<div class="row"><span class="n">2</span><span class="nm">원리 ② 전분 지시약 · 넣는 시점</span><span class="pg">{PAGE:p-starch}</span></div>
<div class="row"><span class="n">2</span><span class="nm">원리 ③ 계산식 · 대응량 · 예상 종말점</span><span class="pg">{PAGE:p-calcf}</span></div>
<div class="row"><span class="n">3</span><span class="nm">실험방법 — 표준액 / 표정 / 적정 구분</span><span class="pg">{PAGE:p-meth}</span></div>
<div class="row"><span class="n">4</span><span class="nm">조작 요령 · 뷰렛 교체</span><span class="pg">{PAGE:p-tips}</span></div>
<div class="row"><span class="n">5</span><span class="nm">고찰 · 결론 포인트</span><span class="pg">{PAGE:p-disc}</span></div>
<div class="row"><span class="n">6</span><span class="nm">기말 대비 Q&amp;A · 노트 체크리스트</span><span class="pg">{PAGE:p-qa}</span></div></div>
<div class="cv-src">의약품분석학 실험 「실험 5: 요오드 적정법」 유인물 1–3쪽 · 수업 녹취록</div>
""")

notice = pg("p-notice", "공지", "지난주(실험 4) 리뷰 · 결론 쓰는 법", "수업 시작 전 교수님 말씀", K0,
main=card("tip", "📊 지난주 경도 결과", """<ul style="margin:0">
<li>시료는 3종류: <b>생수 2종 + 수돗물</b>. 대부분 <b>100 ppm 이하</b>.</li>
<li>수돗물 총경도는 <b>약 60–70 ppm</b>. <b>동원샘물</b>이 높게 나왔음 — 잘못된 게 아님.</li>
<li>같은 생수라도 <b>수원지</b>에 따라 차이가 큼. 수돗물은 빗물이라 경도가 높을 이유가 없고, 생수는 <b>지하수</b>를 쓰기도 해서 전해질이 더 녹아 있을 수 있다.</li>
<li>중요한 건 <b>모든 물이 총경도 기준(300 ppm 이하)을 만족</b>한다는 것 → 음용수로 문제없음.</li></ul>""")
 + card("trap", "✍️ 결론 쓰는 법 (이번 코멘트)", """고찰은 대부분 잘 썼다. 그런데 <b>결론</b>은 실험의 최종 목적에 대한 답을 <b>한 줄로 딱</b> 쓰면 더 좋다 (감점은 안 함).<br>
예) 실험 4: <b>"조치원 수돗물은 음용수 총경도 기준(300 ppm 이하)을 만족한다."</b> ("엄청 만족한다"는 X)<br>
→ 오늘 실험의 결론: <b>"시료 아스코르브산(원료)은 대한약전 기준을 만족한다/만족하지 않는다"</b>, <b>"포비돈요오드액(완제)은 대한약전 기준을 만족한다/만족하지 않는다"</b>."""),
side=card("trap", "⚠️ 팩터는 셋째 자리까지", "\"넷째 자리까지 적고 있는 사람 있던데… <b>계속 감점합니다</b>. 여러 번 얘기했기 때문에.\"")
 + prof("그 아스코르브산 원료 의약품이 대한약전 기준을 만족하는지, 그거를 써야 돼요. 그게 결론이에요.")
 + card("", "🧤 오늘", "고무장갑 라지가 떨어져서 미디엄으로. 오늘이 <b>마지막 적정</b> 실험."))

over = pg("p-over", "한눈에", "오늘 한 일 — 표준액 2개, 의약품 2개", "Overview", K0,
core="표준액 2개(<b>I₂: f는 라벨</b>, <b>Na₂S₂O₃: f′를 표정</b>)로 의약품 2개(<b>포비돈요오드액</b> = 완제, <b>아스코르브산</b> = 원료)를 정량하고 대한약전 기준과 비교.",
main=FLOW + """<ul><li><b>순서대로</b> 할 것: ① Na₂S₂O₃ 표정 → ② 포비돈요오드액(아이오도메트리) → 뷰렛 교체 → ③ 아스코르브산(아이오디메트리). 왔다 갔다 하면 더 오래 걸림.</li>
<li>유인물 <b>2.1 = KIO₃를 이용한 직접법 표정 → 하지 않음</b> (4.1의 "[표정(직접법)](생략)"). <b>2.2 간접법</b>부터 시작.</li>
<li>전분 지시약, Na₂S₂O₃액, 메타인산 용액은 <b>모두 만들어져 있음</b> → 노트에 "제공된 …".</li></ul>""",
side=card("", "🧪 시료 2개", "<b>포비돈요오드액</b>(\"빨간약\", 완제 의약품) — 전용 파이펫으로 필요한 양만 가져가기, 쓰고 나면 꽂아 두기.<br><b>아스코르브산</b>(비타민 C, 원료 의약품) — 약 0.2 g, 라벨상 순도 거의 100%.")
 + prof("오늘 좀 우리 실험에선 드물게 의약품 두 개를 적정을 하게 되는 거예요. 하나는 원료고 하나는 완제고."))

two = pg("p-two", "1", "요오드 적정 2종 — 아이오디메트리 vs 아이오도메트리", "iodimetry vs iodometry", K1,
core="<b>아이오디메트리</b> = I₂ 표준액<b>으로(with)</b> 적정 (I₂가 뷰렛). <b>아이오도메트리</b> = I₂<b>를</b> Na₂S₂O₃로 적정 (I₂가 플라스크, Na₂S₂O₃가 뷰렛).",
main="""<table class="t"><tr><th></th><th>아이오디메트리 (iodimetry)</th><th>아이오도메트리 (iodometry)</th></tr>
<tr><td>암기</td><td>아이오<b>디</b> — I가 <b>with</b>: 요오드<b>로</b> 적정</td><td>요오드<b>를</b> 적정</td></tr>
<tr><td>뷰렛</td><td><b>I₂ 표준액</b> (0.05 M)</td><td><b>Na₂S₂O₃ 표준액</b> (0.1 M)</td></tr>
<tr><td>플라스크</td><td>환원성 의약품 (아스코르브산)</td><td>I₂ (I₂ 표준액 / 포비돈요오드액)</td></tr>
<tr><td>전분 투입</td><td><b>처음부터</b></td><td><b>종말점 직전</b> (미황색일 때)</td></tr>
<tr><td>종말점 색</td><td>무색 → <b>청색이 나타남</b></td><td>청색 → <b>청색이 사라짐(무색)</b></td></tr>
<tr><td>오늘 쓴 곳</td><td>③ 아스코르브산</td><td>① Na₂S₂O₃ 표정, ② 포비돈요오드액</td></tr></table>
<div class="sec">반응식</div>
<div class="fbox"><span class="fx">I₂ + 2S₂O₃²⁻ → 2I⁻ + S₄O₆²⁻</span> (요오드 : 티오황산 = 1 : 2 몰)<br>
<span class="fx">C₆H₈O₆ (아스코르브산) + I₂ → C₆H₆O₆ (데히드로아스코르브산) + 2HI</span> (1 : 1 몰, 둘 다 2당량)</div>
<p>산화환원 적정은 종류가 매우 많아 1학기에 일부만 다뤘다. 오늘은 그중 요오드 적정.</p>""",
side=fig("ascorbic", "유인물 2.4 — 아스코르브산 + I₂ → 데히드로아스코르브산 + 2HI", 130)
 + prof("요오드 적정은 크게 두 종류가 있어요. 아이오디메트리하고 아이오도메트리. 아이오디메트리는 아이가 위드에서 따온 것처럼 기억하면 된다 그랬죠.")
 + card("trap", "⚠️ 헷갈리는 포인트", "\"뷰렛에 무엇이 들어 있나\"로 구분하면 쉽다: <b>I₂면 아이오디</b>, <b>Na₂S₂O₃면 아이오도</b>."))

std = pg("p-std", "2-①", "표준액 2개 — f(I₂)와 f′(Na₂S₂O₃)", "직접법 vs 간접법 · 노르말 농도", K1,
core="I₂ 표준액은 <b>구매한 표준액 → 라벨의 f를 그대로 사용(표정 X)</b>. Na₂S₂O₃는 실험실에서 만든 것 → I₂ 표준액(<b>2차 표준물질</b>)으로 <b>간접법 표정</b>해 <b>f′</b>.",
main="""<div class="sec">직접법 vs 간접법 (표정)</div>
<ul><li><b>직접법</b> = 1차 표준물질을 사용한 표정 → 유인물 <b>2.1</b>: 요오드산칼륨(KIO₃, FM 214.00)<br>
<span class="ko">KIO₃ + 6Na₂S₂O₃ + 5KI + 3H₂SO₄ → 6NaI + 3Na₂S₄O₆ + 3K₂SO₄ + 3H₂O, 0.1 M Na₂S₂O₃ 1 mL ≡ 1/60 mmol KIO₃ ≡ 3.567 mg KIO₃</span> → <b>오늘 안 함</b> (조작이 길다).</li>
<li><b>간접법</b> = 이미 표정되어 f를 가진 다른 표준액(<b>2차 표준물질</b>)을 사용한 표정 → 유인물 <b>2.2부터</b> 시작.</li></ul>
<div class="sec">0.05 M I₂ = 0.1 N — 같은 용액</div>
<ul><li>병에는 <b>0.1 N</b>으로 적혀 있음. I₂는 1 mol이 <b>2당량</b>이므로 노르말 농도 = 몰 농도 × 2. \"농도가 두 배네\" 하고 다시 계산하면 안 됨.</li>
<li>Na₂S₂O₃는 1 mol = 1당량 → 0.1 M = 0.1 N.</li>
<li>I₂ : S₂O₃²⁻ = <b>1 : 2 몰</b>로 반응하는데 농도를 <b>0.05 M : 0.1 M</b>으로 맞춰 놨으니 → <b>부피 1 : 1로 대응</b>. 계산이 편하라고 일부러 그렇게 만든 것.</li></ul>
<div class="fbox"><div class="sec f">📐 f′ 구하기 (1 : 1 대응)</div>
유인물: 0.1 mol/L Na₂S₂O₃ 1 mL ≡ 0.05 mol/L I₂ 1 mL &nbsp; <span class="fx">f′ = f × V(0.05 M I₂) / V(0.1 M Na₂S₂O₃)</span><br>
1조) I₂ 10.00 mL, f = 1.003(라벨), Na₂S₂O₃ 9.45 mL → f′ = 1.003 × 10.00 / 9.45 = 1.061</div>""",
side=fig("fprime", "유인물 2.2 — 간접법 표정과 f′ 식", 120)
 + prof("요오드 표준액은 표정하지 않습니다. 그대로 사용합니다. 우리가 제조사를 믿어야죠. 대신에 팩터를 반드시 사용하셔야 돼요. 표준액이기 때문에.")
 + prof("티오황산나트륨 용액은 우리도 팩터를 몰라. 우리가 잘 만들고 여러분이 실험을 잘 했으면 팩터가 1에 가까이 나올 거예요.")
 + card("tip", "📌 f와 f′ 이름", "I₂ 표준액의 팩터 = <b>f</b>, Na₂S₂O₃액의 팩터 = <b>f′</b>로 구분. 계산할 때 <b>두 개 다</b> 알맞게 사용."))

starch = pg("p-starch", "2-②", "전분 지시약 — 언제 넣고 무슨 색이 되나", "starch indicator · 수용성 전분", K1,
core="I₂가 전분에 끼어 들어가면 <b>아주 짙은 파란색</b>. 아이오도메트리는 <b>종말점 직전(미황색)</b>에 넣고 <b>청색이 사라지면</b> 끝, 아이오디메트리는 <b>처음부터</b> 넣고 <b>청색이 나타나면</b> 끝.",
main="""<div class="sec">아이오도메트리 (Na₂S₂O₃ 표정 · 포비돈요오드액)</div>
<ol><li>I₂ 자체가 <b>짙은 적갈색</b> → 지시약 없이 Na₂S₂O₃를 넣으면 점점 옅어진다.</li>
<li><b>미황색</b>이 되면 그때 전분 1 mL → 아직 종말점 전이면 <b>짙은 청색</b>으로 확 변한다. (넣었는데 색이 안 변하면 종말점을 넘긴 것)</li>
<li>그때부터 한 방울씩 → 종말점에서 \"깜짝 놀라울 정도로\" <b>색이 싹 사라짐</b>(무색).</li></ol>
<div class="ebox"><div class="sec e">왜 처음부터 넣으면 안 되나</div>I₂가 많을 때 전분을 넣으면 많은 양의 I₂가 전분에 끼어 들어가 강하게 붙잡혀, 종말점이 돼도 색이 빨리 안 변한다 → 종말점이 늦어진다. <b>"처음부터 넣으면 절대로 안 돼요."</b></div>
<div class="sec">아이오디메트리 (아스코르브산)</div>
<ul><li>아스코르브산 용액에 전분을 <b>처음부터</b> 넣는다 → <b>아무 색도 없어야</b> 정상 (색이 나타나면 뭔가 들어 있는 것).</li>
<li>I₂가 아스코르브산을 다 산화시키고 남기 시작하면 <b>짙은 파란색</b> → 바로 멈춤.</li>
<li>색이 조금 연해지며 사라지면 아스코르브산이 남아 있던 것 → 기다렸다 한 방울 더. 색이 안 사라지면 종말점 (\"더 가면 안 되지\").</li></ul>""",
side=card("", "🧪 전분 지시약", "물을 끓여야 해서 조제는 생략, <b>제공됨</b>. 요리용 전분이 아니라 <b>수용성 전분(soluble starch)</b>, 맑은 용액. 비치된 마이크로피펫으로 <b>1 mL</b>씩, <b>팁은 버리지 말고 재사용</b>(환경), 플라스크 입구에 닿지 않게(오염 방지).")
 + prof("여러분이 아이오디메트리를 하느냐, 아이오도메트리를 하느냐에 따라 종말점이 달라요. 잘 기억을 하시고 해야 되고요."))

calcf = pg("p-calcf", "2-③", "계산식 · 대응량 · 예상 종말점", "유인물 2.2–2.4 대응량", K1,
core="<b>0.1 M Na₂S₂O₃ 1 mL ≡ 0.05 mmol I₂ ≡ 12.691 mg I₂</b>, <b>0.05 M I₂ 1 mL ≡ 아스코르브산 8.806 mg</b>. 시료를 100%로 가정해 <b>종말점을 미리 계산</b>하고 적정.",
main="""<div class="fbox"><div class="sec f">① 포비돈요오드액 (아이오도메트리)</div>
농도: 포비돈요오드 <b>10 w/v%</b>, 그중 유효 요오드가 <b>10%</b> → 요오드로서 <b>1 w/v%</b> (= 10 mg/mL)<br>
요오드로서 100 mg에 해당하는 양 = <b>10 mL</b> (포비돈은 신경 쓰지 말고 요오드 농도만)<br>
<span class="fx">요오드(mg) = V<sub>S₂O₃</sub> × f′ × 12.691</span> &nbsp; <span class="fx">표시량 대비(%) = I(mg) / 100 mg × 100</span><br>
예상 종말점 = 100 / 12.691 ≈ <b>7.88 mL</b> (f′ = 1)</div>
<div class="fbox"><div class="sec f">② 아스코르브산 (아이오디메트리)</div>
<span class="fx">아스코르브산(mg) = V<sub>I₂</sub> × f × 8.806</span> (176.12 × 0.05) &nbsp; <span class="fx">함량(%) = 아스코르브산(mg) / 칭량값(mg) × 100</span><br>
예상 종말점 (0.2 g, 100% 가정) = 200 / 8.806 ≈ <b>22.7 mL</b> (f = 1)</div>
<div class="ebox"><div class="sec e">✍️ 대응량이 나오는 이유</div>
Na₂S₂O₃ 0.1 mmol ↔ I₂ 0.05 mmol = 0.05 × 253.81 = <b>12.691 mg</b> (= I 원자 0.1 mmol)<br>
I₂ 0.05 mmol ↔ 아스코르브산 0.05 mmol = 0.05 × 176.12 = <b>8.806 mg</b></div>""",
side=prof("우리가 사용한 요오드 양이 100 mg이니까 100을 대응량으로 나눠주면 바로 나오지. 100 나누기 12.69. 그게 바로 이론적인 당량점이 되는 거야. 그럼 그걸 알고 들어가면 훨씬 마음이 편해.")
 + card("trap", "⚠️ 수업 중 혼동", "아스코르브산 예상량을 \"0.1이니까 11.35 mL\"로 계산한 대화가 있었지만, 뷰렛의 I₂는 <b>0.05 M</b>(= 0.1 N)이라 0.2 g이면 약 <b>22.7 mL</b>가 맞다.")
 + card("tip", "📌 판정 — 대한약전 기준", "포비돈요오드액 유효요오드 <b>표시량의 85.0~120.0%</b>, 아스코르브산 <b>99.0~101.0%</b>. 두 결과를 기준과 비교해 <b>만족 여부를 결론 한 줄</b>로."))

meth = pg("p-meth", "3", "실험방법 — 유인물 4.1 · 4.2 (표준액 / 표정 / 적정 구분)", "유인물 2–3쪽 · 생략 단계 표시", K2,
main="""<div class="sec">4.1 Iodometry — 티오황산나트륨 표준액으로 요오드 적정</div>
<p class="ko">[전분 지시약(1 w/v%) 제조] · [0.1 M Na₂S₂O₃액 제조(Na₂S₂O₃·5H₂O 25 g + Na₂CO₃ 0.2 g → 1000 mL)] · [표정(직접법, KIO₃)] → <b>모두 생략</b> (제공됨 / 안 함)</p>
<p><b>[표준액]</b> 0.05 M I₂ 표준액: 구매품, <b>라벨 f</b> 사용 (표정 안 함)</p>
<p><b>[표정] 0.1 M Na₂S₂O₃액 (간접법)</b></p>
<ol><li>0.05 M I₂ 표준액(f) <b>10 mL</b>를 100 mL 삼각플라스크에, 메스실린더로 탈이온수 <b>40 mL</b>를 가해 섞는다.</li>
<li>0.1 M Na₂S₂O₃액을 적가하다 <b>종말점 직전 전분 1 mL</b> → 진한 청색이 <b>완전히 사라질 때까지</b>.</li>
<li>f′ 계산.</li></ol>
<p><b>[적정 1] 포비돈요오드액(10 w/v%, 유효요오드로서 1 w/v%) 중 요오드 정량</b></p>
<ol><li>요오드(I)로서 <b>100 mg</b>에 해당하는 양(10 mL)을 <b>transfer pipet</b>으로 100 mL 삼각플라스크에, 전체량이 약 <b>50 mL</b>가 되도록 메스실린더로 탈이온수.</li>
<li>0.1 M Na₂S₂O₃(f′) 적가 → 종말점 직전 전분 1 mL → 청색이 완전히 사라질 때까지.</li>
<li>요오드 함량 계산, <b>대한약전 기준 만족 여부</b>.</li></ol>
<div class="sec">4.2 Iodimetry — 요오드 표준액으로 아스코르브산 적정</div>
<p class="ko">[메타인산용액(1→50) 제조: 메타인산 2 g → 100 mL] → 제공됨</p>
<ol><li><b>[적정 2]</b> 건조된 아스코르브산 <b>약 0.2 g을 정밀하게</b> 달아 200 mL 삼각플라스크, 메타인산용액 <b>50 mL</b>로 녹임 (실제 칭량값 기록).</li>
<li>전분 1 mL → 0.05 M I₂ 표준액(f)을 <b>갈색 뷰렛</b>에 넣어 <b>지속적인 청색</b>이 나타날 때까지.</li>
<li>함량 계산, <b>대한약전 기준 만족 여부</b>.</li></ol>""",
side=card("trap", "✍️ 노트에 쓸 때", """<ul style="margin:0"><li><b>[표준액] / [표정] / [적정 1] / [적정 2]</b> 단락을 나눠서 (실험 3 코멘트)</li>
<li>생략: 전분·Na₂S₂O₃·메타인산 제조, 직접법 표정 → "제공된 …", "하지 않았다"</li>
<li>아스코르브산은 \"건조된\" — 조에서 건조했는지 실제대로</li>
<li>실제 칭량값·분취량·눈금, 각 1회</li></ul>""")
 + card("", "🧾 시약 및 기구 (유인물)", "분석저울, magnetic stirrer, beaker(100, 250 mL), Erlenmeyer flask(100, 200, 250 mL), volumetric flask(100, 250, 1000 mL), buret(50 mL), <b>amber buret(50 mL)</b>, mass cylinder(100 mL), transfer pipet(10 mL), stand, clamp, 세척병, weighing boat, amber bottle(50 mL), ascorbic acid(FM 176.12), metaphosphoric acid, 포비돈요오드액, iodine standard solution(0.05 M), Na₂S₂O₃·5H₂O(FM 248.19), KIO₃(FM 214.00), Na₂CO₃, NaHCO₃, KI(FM 166.00), As₂O₃(FM 197.84), 10% H₂SO₄, 1 N NaOH, 10% HCl, 0.1% methyl orange, soluble starch")
 + prof("물은 어차피 적정이 안 돼. 적정에서 농도를 재는 게 아니고 양을 재는 거기 때문에 부피는 약간 틀려져도 돼. 대신에 요오드 용액을 정확히 넣어야지."))

tips = pg("p-tips", "4", "조작 요령 · 뷰렛 교체", "교수님 순회 지도", K2,
main="""<div class="sec">① 시약 취하기</div>
<ul><li>I₂ 표준액 10 mL는 <b>무게가 아니라 부피</b>로 (\"10 g이 아니고 10 mL. 무게 재면 안 돼\").</li>
<li>플라스크 입구를 막아 두기 — I₂는 반응성·휘발성이 있다 <span class="ko">(녹취 일부)</span>.</li>
<li>포비돈요오드액은 공용 전용 파이펫으로, 쓰고 나서 <b>꽂아 두기</b> (벤치가 빨갛게 엉망이 됨).</li>
<li>공통 시약(전분, 포비돈)은 <b>플라스크를 들고 가서</b> 필요한 만큼.</li></ul>
<div class="sec">② 적정</div>
<ul><li>뷰렛 위 <b>깔때기는 빼고</b> 적정 (한 방울 톡 떨어지면 오차).</li>
<li>f′ ≈ 1이면 Na₂S₂O₃도 I₂와 <b>거의 같은 부피</b>(약 10 mL)가 들어가야 함 — 7.5 mL쯤에서 \"아직 안 됐어, 요오드 많이 남았어\".</li>
<li>색 변화가 잘 안 일어나는 시점에서 <b>눈금을 읽어 기록</b> → 더 안 변하면 그 값, 계속 변하면 다음 값.</li>
<li>아스코르브산: 청색이 30초쯤 뒤 연해지면 한 방울 더, 안 사라지면 종말점.</li></ul>
<div class="sec">③ 뷰렛 교체 (Na₂S₂O₃ → I₂)</div>
<p>뷰렛이 하나뿐 → Na₂S₂O₃를 다 버리고 <b>수돗물로 충분히</b> → <b>탈이온수</b>로 헹굼 → 말릴 수 없으니(뿌리거나 흔들어 말리지 말 것) <b>I₂ 표준액 소량으로 2–3회</b> 안쪽을 헹군 뒤 채움.</p>""",
side=card("", "🧽 마지막 정리", "오늘이 마지막 적정 → 기구를 물로 잘 씻고 <b>반드시 탈이온수로 헹군 뒤</b> 3조·4조 테이블로. 5조 빼고 퇴실.")
 + card("tip", "📌 예상값을 알고 적정", "포비돈 ≈ 7.9 mL, 아스코르브산(0.2 g) ≈ 22.7 mL, Na₂S₂O₃ 표정 ≈ 10 mL (f, f′ ≈ 1)"))

disc = pg("p-disc", "5", "고찰 · 결론 포인트", "결론 = 대한약전 기준 만족 여부 한 줄", K3,
main="""<table class="t"><tr><th style="width:22%">원인</th><th>결과에 미치는 영향</th><th style="width:28%">대책 · 개선</th></tr>
<tr><td>아이오도메트리에서 전분을 너무 일찍 넣음</td><td>I₂가 전분에 붙잡혀 청색이 늦게 사라짐 → V↑ → f′ 과소(표정) / 요오드 함량 과대(포비돈)</td><td>미황색에서 투입</td></tr>
<tr><td>종말점 초과 (빠른 적정)</td><td>V↑</td><td>예상 종말점 근처 한 방울씩</td></tr>
<tr><td>I₂의 휘발 · 공기 중 I⁻ 산화</td><td>플라스크의 I₂ 양 변화</td><td>마개, 신속한 적정</td></tr>
<tr><td>아스코르브산 공기 산화</td><td>소비 I₂↓ → 함량 과소</td><td>메타인산 용액, 녹인 즉시 적정</td></tr>
<tr><td>뷰렛 교체 시 물·Na₂S₂O₃ 잔류</td><td>I₂ 표준액이 묽어지거나 소비 → V 오차</td><td>I₂ 표준액으로 충분히 린싱</td></tr>
<tr><td>I₂ 라벨 f 신뢰</td><td>f가 틀리면 f′와 아스코르브산 결과 모두 영향</td><td>1차 표준물질(2.1 직접법)로 확인</td></tr>
<tr><td>포비돈요오드액 10 mL 분취 오차</td><td>표시량 대비 % 오차</td><td>점성 있는 액체 → 피펫 천천히, 잔류액 주의</td></tr>
<tr><td>1회 측정</td><td>재현성 확인 불가</td><td>3회 반복</td></tr></table>
<div class="ebox"><div class="sec e">✍️ 결론 문장 예</div>
"시료 아스코르브산의 함량은 __._%로 대한약전 기준(99.0~101.0%)을 <b>만족한다 / 만족하지 않는다</b>."<br>
"포비돈요오드액의 유효 요오드는 표시량의 __._%로 대한약전 기준(85.0~120.0%)을 <b>만족한다</b>."</div>""",
side=prof("이 회사 포비돈요오드액을 여러분이 적정을 했는데 대한약전 기준을 만족하지 않으면 좀 이상하겠죠. 이게 어떻게 허가를 받았지? 생각할 수가 있겠죠.")
 + card("trap", "⚠️ 대한약전 기준", "포비돈요오드액 유효요오드: <b>표시량의 85.0~120.0%</b><br>아스코르브산: <b>99.0~101.0%</b> (상한도 있음)"))

QA = [
("Q1. 아이오디메트리와 아이오도메트리의 차이는?", "아이오디: I₂ 표준액으로(with) 적정, I₂가 뷰렛. 아이오도: I₂를 Na₂S₂O₃로 적정, Na₂S₂O₃가 뷰렛."),
("Q2. I₂와 Na₂S₂O₃의 반응과 몰비는?", "I₂ + 2S₂O₃²⁻ → 2I⁻ + S₄O₆²⁻, 1 : 2."),
("Q3. 0.05 M I₂가 0.1 N인 이유는?", "I₂ 1 mol이 2당량이라 노르말 농도 = 몰 농도 × 2."),
("Q4. 0.05 M I₂와 0.1 M Na₂S₂O₃의 부피 대응은?", "1 : 2 몰비 × 1 : 2 농도 → 부피 1 : 1."),
("Q5. 직접법과 간접법(표정)의 차이는?", "직접법: 1차 표준물질 사용. 간접법: f를 가진 다른 표준액(2차 표준물질) 사용."),
("Q6. 오늘 Na₂S₂O₃의 표정법과 사용한 2차 표준물질은?", "간접법, 0.05 M I₂ 표준액(라벨 f 사용)."),
("Q7. 아이오도메트리에서 전분을 언제 넣고 왜?", "종말점 직전(미황색). 처음부터 넣으면 I₂가 전분에 많이 붙잡혀 종말점이 늦어짐."),
("Q8. 아이오도메트리의 종말점 색 변화는?", "청색 → 무색 (청색이 사라짐)."),
("Q9. 아이오디메트리에서 전분은? 종말점은?", "처음부터 넣고(무색), 청색이 나타나 사라지지 않을 때."),
("Q10. 아스코르브산과 I₂의 반응 몰비는?", "1 : 1 (C₆H₈O₆ + I₂ → C₆H₆O₆ + 2HI), 둘 다 2당량."),
("Q11. 0.1 M Na₂S₂O₃ 1 mL의 요오드 대응량은?", "0.05 mmol I₂ = 12.691 mg I₂."),
("Q12. 0.05 M I₂ 1 mL의 아스코르브산 대응량은?", "8.806 mg (0.05 × 176.12)."),
("Q13. 포비돈요오드액(10%)에서 요오드로서 100 mg에 해당하는 양은?", "요오드 1 w/v% → 10 mL."),
("Q14. 포비돈요오드 적정의 이론 종말점은?", "100 / 12.691 ≈ 7.88 mL (f′ = 1)."),
("Q15. 아스코르브산을 메타인산 용액에 녹이는 이유는?", "산성으로 유지해 공기 중 산화를 막기 위해."),
("Q16. 이 실험의 결론으로 써야 할 것은?", "아스코르브산(원료)과 포비돈요오드액(완제)이 대한약전 기준을 만족하는지 여부."),
]


def qa(items):
    return "".join(f'<div class="qa"><div class="q">{q}</div><div class="a">{a}</div></div>' for q, a in items)


check = card("tip", "📝 실험노트 체크리스트 (실험 5)", """<ul style="list-style:none;padding-left:0;margin:0">
<li>□ 페이지 번호 실험 4에서 이어서, 1권, 서명은 머리말/꼬리말</li>
<li>□ 원리 최소 반 페이지 (두 요오드 적정, 반응식, 당량·농도, 전분, 대응량)</li>
<li>□ <b>[표준액] / [표정] / [적정 1] / [적정 2]</b> 구분</li>
<li>□ I₂ 라벨 f, Na₂S₂O₃ f′ — <b>둘 다 셋째 자리까지</b> (넷째 자리 감점)</li>
<li>□ 실제 값: 아스코르브산 칭량값, 포비돈 분취량, 모든 눈금(둘째 자리)</li>
<li>□ <b>결론 한 줄</b>: 두 의약품의 대한약전 기준 만족 여부</li>
<li>□ 부착물: 노트 번호 + 부착 페이지, 겹치게 간인</li></ul>""")

qa1 = pg("p-qa", "6", "기말 대비 핵심 체크 (Q&amp;A) ①", "Q1–Q8", K3, main=qa(QA[:4]), side=qa(QA[4:8]))
qa2 = pg("p-qa2", "6", "기말 대비 핵심 체크 (Q&amp;A) ② · 노트 체크리스트", "Q9–Q16", K3, main=qa(QA[8:]), side=check)

E = [cover, notice, over, two, std, starch, calcf, meth, tips, disc, qa1, qa2]
