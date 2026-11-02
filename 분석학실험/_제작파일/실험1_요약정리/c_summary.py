# -*- coding: utf-8 -*-
"""실험1_뷰렛의 검정_요약정리 — 내용은 그대로, 마스터요약 양식(A4 가로 카드 레이아웃)으로"""
from svgs import STYLE, FLOW, PARALLAX, curve, our_table, OUR, HAND


def card(kind, title, body):
    return f'<div class="card {kind}"><div class="ct">{title}</div>{body}</div>'


def prof(body):
    return card("prof", "🎙 교수님 말씀", body)


def pg(pid, bd, title, sub, part, main, side="", core=""):
    core = f'<div class="core"><span class="lb">💡 핵심</span>{core}</div>' if core else ""
    body = f'<div class="main{"" if side else " full"}">{main}</div>' + (f'<div class="side">{side}</div>' if side else "")
    return dict(t="r", id=pid, html=f'''<div class="hd"><span class="bd">{bd}</span><div class="tt"><h1>{title}</h1><div class="sb">{sub}</div></div><span class="pt">{part}</span></div>
{core}<div class="body">{body}</div>''')


K0, K1, K2, K3, K4 = "한눈에 보기", "안전 · 실험노트", "원리 · 측용기", "뷰렛 사용법", "방법 · 결과"

cover = dict(t="r", cls="cover2", html=STYLE + """
<style>
.cover2{background:radial-gradient(ellipse at 0% 0%,#ffd9e8 0%,rgba(255,217,232,0) 45%),radial-gradient(ellipse at 100% 0%,#dcd6ff 0%,rgba(220,214,255,0) 50%),radial-gradient(ellipse at 100% 100%,#d4f5e6 0%,rgba(212,245,230,0) 50%),radial-gradient(ellipse at 40% 60%,#dfe6ff 0%,rgba(223,230,255,0) 60%),#f4f1fb !important;}
.cv-k{letter-spacing:.32em;font-size:11px;font-weight:700;color:#7d74c9;margin-top:6mm;}
.cv-h{font-size:40px;line-height:1.18;font-weight:800;margin:10px 0 12px 0;background:linear-gradient(120deg,#5b3fd6,#3f57d8);-webkit-background-clip:text;background-clip:text;color:transparent;}
.cv-flow{font-size:15.5px;color:#2c3038;margin-bottom:12px;}
.cv-txt{font-size:12.6px;line-height:1.75;color:#3a3f4b;}
.cv-eq{display:inline-block;margin-top:10px;background:#fff;border:1px solid #e3def3;border-radius:12px;padding:8px 16px;font-weight:700;font-size:14px;color:#3d2a73;box-shadow:0 1px 3px rgba(80,60,160,.08);}
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
<div class="cv-left"><div class="cv-k">의약품분석학 실험 · 실험 1 (실험 기초지식) · 첫 수업 정리</div>
<div class="cv-h">실험 1.<br>뷰렛의 검정<br>(Buret Calibration)</div>
<div class="cv-flow">자료: 실험1 유인물 1–5쪽 + 첫 수업 녹취록(약 104분) 요약 · 정리일 2026-10-29</div>
<div class="cv-txt"><b>한 줄 요약</b> — 앞으로 4주간 적정에 쓸 <b>뷰렛이 제조사가 말한 만큼(±0.1 mL) 정확한지</b>를,
뷰렛에서 흘려보낸 물의 <b>무게를 재서 밀도로 나눠 "진짜 부피"</b>를 구한 뒤 눈금과 비교해 확인한 실험.</div>
<div class="cv-eq">보정치 = (물 무게 ÷ 물의 밀도) − 뷰렛 눈금 = 실제 부피 − 읽은 부피</div></div>
<div class="cv-toc"><div class="t">CONTENTS</div>
<div class="row"><span class="n">0</span><span class="nm">한눈에 보기 · 공지사항</span><span class="pg">{PAGE:p-over}</span></div>
<div class="row"><span class="n">1</span><span class="nm">실험실 안전 수칙</span><span class="pg">{PAGE:p-safe}</span></div>
<div class="row"><span class="n">2</span><span class="nm">실험노트 작성 요령</span><span class="pg">{PAGE:p-note}</span></div>
<div class="row"><span class="n">3</span><span class="nm">왜 뷰렛을 "검정"하나? — 목적과 원리</span><span class="pg">{PAGE:p-prin}</span></div>
<div class="row"><span class="n">4</span><span class="nm">측용기의 종류 — TC vs TD</span><span class="pg">{PAGE:p-tctd}</span></div>
<div class="row"><span class="n">5</span><span class="nm">뷰렛 사용법 — 오늘의 핵심 실기</span><span class="pg">{PAGE:p-use1}</span></div>
<div class="row"><span class="n">6</span><span class="nm">실험 방법</span><span class="pg">{PAGE:p-meth}</span></div>
<div class="row"><span class="n">7</span><span class="nm">오늘 우리 조 결과</span><span class="pg">{PAGE:p-res}</span></div>
<div class="row"><span class="n">8</span><span class="nm">검정곡선은 다음 주부터 이렇게 쓴다</span><span class="pg">{PAGE:p-curve}</span></div>
<div class="row"><span class="n">9</span><span class="nm">기말 대비 핵심 체크 (Q&amp;A) · 노트 체크리스트</span><span class="pg">{PAGE:p-qa1}</span></div></div>
<div class="cv-src">의약품분석학 실험 「실험 1: 실험 기초지식」 유인물 1–5쪽 · 첫 수업 녹취록</div>
""")

NOTICE = card("trap", "📌 공지사항 · 감점 포인트", """<ul style="margin:0">
<li><b>실험노트 제출</b>: 목요일 실험 → <b>다음 주 월요일 저녁 6시까지</b>, 401호(교수님 실험실) 앞 박스. 늦으면 감점. 채점 후 다음 실험 때 돌려줌.</li>
<li><b>기말고사 있음</b>: 실험한 내용에서만 출제. 실험에 성실히 참여하면 풀 수 있는 시험.</li>
<li><b>복장</b>: 실험복 필수, <b>단추 끝까지</b> 잠글 것. <b>슬리퍼·반바지 절대 불가</b> (조교 체크 → 감점/퇴실 가능).</li>
<li><b>휴대폰 사용 금지</b> (감점).</li>
<li><b>적정 시 용액이 "주르륵" 흐르면 감점</b> — 반드시 똑, 똑, 똑 떨어지게.</li>
<li>실험실은 냉방만 되고 <b>난방이 안 됨</b> → 따뜻하게 입고 올 것. 에어컨 켜도 찬 바람만 나옴.</li></ul>""")

over = pg("p-over", "한눈에", "오늘 한 일 · 실험 일정 · 공지사항", "Overview & notice", K0,
core="앞으로 4주간 적정에 쓸 <b>뷰렛이 제조사가 말한 만큼(±0.1 mL) 정확한지</b>를, 흘려보낸 물의 <b>무게 ÷ 밀도 = \"진짜 부피\"</b>로 확인한 실험.",
main="""<div class="sec">🧪 오늘 한 일 (순서)</div>
<ol><li>뷰렛 준비: 세척·린싱, 스톱콕 조임 조절, 누출 확인</li>
<li>탈이온수 채우고 <b>기포 제거</b> → 0.00 mL에 맞춤</li>
<li>빈 삼각플라스크 무게 측정</li>
<li>약 10 mL씩 <b>한 방울씩</b> 받아 눈금(0.01까지) + 무게 기록 → 50 mL까지</li>
<li>실제 부피·보정치 계산 → <b>검정곡선</b> (x: 눈금, y: 보정치)</li>
<li>뒷정리: 수돗물 → 탈이온수 헹굼 → 스톱콕 열고 거꾸로 걸어 자연건조</li></ol>
<div class="fbox"><div class="sec f">📐 오늘의 식</div><span class="fx">보정치 = (물 무게 ÷ 물의 밀도) − 뷰렛 눈금 = 실제 부피 − 읽은 부피</span></div>""",
side=card("", "📅 이번 학기 실험 일정 (총 7회)", """<table class="t" style="margin:0"><tr><th>회차</th><th>내용</th></tr>
<tr><td>1</td><td><b>뷰렛의 검정</b> (오늘)</td></tr>
<tr><td>2–5</td><td>적정 4종: 중화 · 침전 · 킬레이트(EDTA) · 산화환원<br><span class="ko">자동적정기 없이 뷰렛으로 직접</span></td></tr>
<tr><td>6</td><td>기기분석 ① 분광 분석</td></tr>
<tr><td>7</td><td>기기분석 ② 분리 분석</td></tr></table>
<p style="margin:4px 0 0">→ 오늘이 앞으로 한 달간 쓸 뷰렛의 "기초 체력 검사"인 셈.</p>""") + NOTICE)

safe = pg("p-safe", "1", "실험실 안전 수칙", "유인물 1쪽", K1,
main="""<table class="t"><tr><th style="width:17%">항목</th><th>핵심 내용</th></tr>
<tr><td>보안경</td><td>원칙은 "항상" 착용. 이 실험실은 특별히 위험한 시약이 없어 원하면 제공.</td></tr>
<tr><td>고무장갑</td><td>시약·용매를 다룰 때 반드시. 독성물질은 2겹. <span class="ko">(오늘은 물이라 불필요)</span></td></tr>
<tr><td>복장</td><td>손·다리·발·몸통을 덮는 옷과 신발. 실험복 정확히 착용(단추 안 잠그면 걸려 넘어짐). 긴 머리는 묶기.</td></tr>
<tr><td>화학물질</td><td>피펫을 입으로 빨지 말 것(Filler/Pipette aid 사용). 흡입·맛보기·피부접촉 금지. 눈에 들어가면 흐르는 물로 먼저 세척 후 알림. 실험실 내 취식·흡연 금지. 시약 정보는 Merck Index, 안전정보는 MSDS.</td></tr>
<tr><td>유리용기</td><td>뜨거운지 찬지 눈으로 구분 안 됨 → 주의. 유리관을 고무마개에 끼울 땐 윤활제 + 타월로 손 보호. 베이면 깨끗한 타월로 압박 지혈 후 즉시 알림.</td></tr>
<tr><td>화재</td><td>휘발성·가연성 용매(ether, acetone, methanol 등) 주의 — 열린 계에서 가열·휘산 금지, 감압농축기 사용. 소화기·안전샤워·화재경보기·비상구 위치 숙지 (화재 시 승강기 금지).</td></tr>
<tr><td>실험 준비</td><td>검증되지 않은 실험 금지. 미심쩍으면 반드시 질문. 교수/조교 없이 혼자 실험 금지.</td></tr></table>""",
side=prof("이 실험 아무리 열심히 해도 노벨상 못 받는다. 그러니 제일 중요한 건 안전. 유리 초자를 써서 실제로 여러 번 깨졌다.")
 + card("", "⚠️ 이 실험실의 위험 요인 정리 <span class=\"ko\">(교수님 설명)</span>", """<ul style="margin:0">
<li><span class="tag j">Chemical</span>있음 — 시약 사용 시 주의</li>
<li><span class="tag s">Bio</span>없음 — 생물 물질 안 씀</li>
<li><span class="tag j">Physical</span>많음 — 특히 <b>유리 초자</b> 파손</li>
<li><span class="tag h">Fire</span>전기 장비 누전 가능성. 학기 마지막에 알코올류 가연성 용매 사용 예정.</li></ul>"""))

note = pg("p-note", "2", "실험노트 작성 요령", "유인물 2쪽", K1,
main="""<div class="sec">📝 들어가야 할 항목</div>
<ol><li><b>실험일자</b> — 노트 쓴 날이 아니라 <b>실험한 날</b></li>
<li><b>실험자 서명</b> — <b>매 페이지</b> (페이지가 떨어져 나갈 수 있으므로)</li>
<li>증인 서명 — 원칙상 필요하지만 이 수업에선 생략</li>
<li><b>제목</b></li>
<li><b>목적</b> — 간단하게</li>
<li><b>절차</b> — 자기 말로 간단히, 실제 한 대로 과거형</li>
<li><b>실험결과</b> — 가장 중요. 표(Table I…)·그림(Figure 1…)에 번호·제목, 색·온도·무게 변화 등 관찰 모두</li>
<li><b>고찰 및 결론</b> — 결과를 해석·비교, 논리적 판단. 감상문 X</li></ol>""",
side=prof("좋은 실험노트란 \"그 분야의 통상적 지식을 가진 사람이 <b>내 노트만 보고 내 실험을 재현</b>할 수 있는 노트\"다. 나라에 따라 실험노트 날짜가 발명일(특허)이 되기도 한다.")
 + card("trap", "✍️ 형식 규칙 (어기면 감점)", """<ul style="margin:0">
<li><b>볼펜</b>으로만 (연필·지우개·수정액·화이트 금지)</li>
<li>틀리면 <b>두 줄 긋고 서명</b>, 지우지 말 것</li>
<li>페이지에 남는 여백 → <b>사선 + "여백"</b> 표시 (조작 방지)</li>
<li>출력물(표·그래프) 부착 → <b>4면 모두</b> 풀/테이프, 노트와 종이에 걸쳐 <b>간인(서명)</b></li>
<li>노트 번호 부여 (예: 분석학실험 No.1) + <b>일련 페이지 번호</b></li>
<li>노트는 아무 노트나 OK (문방구 노트)</li>
<li>서론은 핸드아웃 정리로 충분, 참고문헌 불필요</li></ul>"""))

prin = pg("p-prin", "3", "왜 뷰렛을 \"검정\"하나? — 목적과 원리", "Purpose & principle · 유인물 3쪽, 5쪽", K2,
core="<b>목적</b> (유인물): 부피측정용 유리기구에 대해 <b>제작자의 허용오차 범위 내에서</b> 실제로 정확한 부피 측정이 이루어지는지 검정한다.",
main="""<p><b>원리</b>: 증류수를 담은 뷰렛에서 일정 눈금만큼 물을 흘려보내 그 <b>질량</b>을 저울로 재고, 그 온도에서의 <b>밀도</b>로 나눠 실제 용량을 계산한다.</p>
<div class="sec">왜 무게로 부피를 알 수 있나?</div>
<div class="fbox"><span class="fx">밀도 ρ = 질량 m / 부피 V &nbsp;⟹&nbsp; V<sub>실제</sub> = m<sub>물</sub> / ρ<sub>물(수온)</sub></span></div>
<p>저울은 뷰렛 눈금보다 훨씬 정밀하다(0.001 g 단위). 물은 밀도가 온도별로 정확히 알려져 있으므로(유인물 5쪽 <b>Table 1.2</b>, 19.0–26.0 °C) "무게 → 부피"로 바꾸면 <b>진짜 나간 부피</b>를 알 수 있다. 오늘 수온은 약 <b>19 °C → ρ = 0.99842 g/mL</b> (교수님은 "약 0.998"로 설명).</p>
<table class="t"><tr><th>T (°C)</th><th>19.0</th><th>20.0</th><th>21.0</th><th>22.0</th><th>23.0</th><th>25.0</th></tr>
<tr><td>ρ (g/mL)</td><td><b>0.99842</b></td><td>0.99821</td><td>0.99800</td><td>0.99778</td><td>0.99755</td><td>0.99705</td></tr></table>
<p class="ko">→ 온도가 오를수록 밀도가 작아진다. 그래서 수온을 꼭 재서 기록해야 한다(노트에 "수온 __ °C, ρ = ____ g/mL" 명시).</p>""",
side=prof("뷰렛 윗부분에 제조사가 보증하는 정확도가 적혀 있다 — <b>20 °C 기준 ±0.1 mL</b> (또는 ±0.08). 즉 20.35를 정확히 읽어도 참값은 20.35 ± 0.1. \"제조사가 진짜 이렇게 정확하다고?\" — 그걸 의심하고 확인하는 것이 검정(calibration)이다. 적정은 간단하지만 엄청나게 정확한 정량법인데, 뷰렛이 틀리면 완전히 헛고생.")
 + card("ana", "📐 보정치(Correction)의 정의 — 부호 주의!", """<span class="fx">보정치 = 실제 부피(계산값) − 뷰렛 눈금(읽은 값)</span>
<ul style="margin:0"><li>보정치 <b>+</b> : 눈금보다 실제로 <b>더 많이</b> 나갔다 → 눈금에 더해 줘야 함</li>
<li>보정치 <b>−</b> : 눈금보다 실제로 <b>덜</b> 나갔다</li>
<li>쓰는 법: <b>보정된 부피 = 읽은 눈금 + 보정치</b> (양수·음수 모두 그대로 더함)</li></ul>"""))

tctd = pg("p-tctd", "4", "측용기(부피 측정 기구)의 종류 — TC vs TD", "To contain vs To deliver · 유인물 3쪽", K2,
main="""<table class="t"><tr><th style="width:14%"></th><th>수용(受用) 측용기 · <b>TC</b> (To Contain)</th><th>출용(出用) 측용기 · <b>TD</b> (To Deliver)</th></tr>
<tr><td>보증하는 것</td><td>표선까지 채웠을 때 <b>용기 안에 담긴</b> 부피</td><td>표선까지 채운 액체를 <b>다른 용기로 옮겼을 때</b> 나간 부피</td></tr>
<tr><td>대표 기구</td><td><b>부피플라스크</b>(volumetric flask), 수용 메스실린더</td><td><b>뷰렛</b>, <b>피펫</b>, 출용 메스실린더</td></tr>
<tr><td>예시</td><td>500 mL 부피플라스크: <b>500 ± 0.3 mL</b></td><td>50 mL 뷰렛: 눈금마다 <b>±0.1 mL</b></td></tr>
<tr><td>잘못된 사용</td><td>부피플라스크로 재서 따라 옮기기</td><td>뷰렛에 부어 담긴 양을 재기, 거꾸로 흘리기</td></tr></table>
<p><b>측용기 취급 주의점</b> (유인물): ① 세척·헹굼 철저 ② 피펫을 입으로 사용 금지(Filler 사용), 유해 기체는 후드 안에서 ③ 수용/출용 구분 사용 ④ <b>측용기는 발열성 물질 사용·가열·가열건조 금지</b> (열로 유리가 팽창 → 부피가 변함).</p>""",
side=card("tip", "💡 이해 포인트: 뷰렛 속 실제 액체 양 vs 나간 양", "벽에 액체가 조금 남기 때문에 <b>뷰렛 안에 담겨 있던 양 &gt; 실제로 나간 양</b>. 제조사는 이걸 감안해 \"나간 양\"에 맞춰 눈금을 그렸다(TD). 그래서 뷰렛은 반드시 <b>위에서 아래로 흘려보내는 용도로만</b> 써야 눈금이 맞는다.")
 + card("trap", "⚠️ 비커·삼각플라스크 눈금은 믿지 말 것", "라면 냄비 눈금처럼 <b>참고용</b>일 뿐 정확하지 않다. 비커 눈금으로 재서 옮기는 건 TC도 TD도 아님 → 정량에 쓰지 말 것. \"눈금이 있다고 다 믿으면 안 된다.\""))

use1 = pg("p-use1", "5", "뷰렛 사용법 — 오늘의 핵심 실기 ①–③", "세척·린싱 · 스톱콕 · 기포", K3,
main="""<div class="sec">① 세척과 린싱(rinsing)</div>
<ul><li>선배들이 깨끗이 씻어 놨을 거라고 <b>믿으면 안 된다</b> — 기본.</li>
<li>정석 세척: 시약은 <b>폐액통</b>에 먼저 버림 → 소량의 물로 헹굼 → <b>수돗물로 충분히</b> → 마지막에 <b>탈이온수(세척병)로 2–3회</b> 헹굼 → 실온 <b>자연건조</b>. <span class="ko">(수돗물엔 전해질이 있어 마지막만 비싼 탈이온수로 헹구면 충분)</span></li>
<li>말릴 시간이 없으면 → <b>사용할 용액으로 린싱</b> (소량 넣어 내벽을 적시고 버리기를 반복). 오늘은 용액이 탈이온수라 탈이온수로 헹구면 끝. 다음 주부터는 <b>표준액</b>으로 여러 번 린싱.</li>
<li><b>절대 열로 말리지 말 것</b>(오븐·드라이어 X).</li></ul>
<div class="sec">② 스톱콕 조임 조절 · 누출 확인</div>
<ul><li>스톱콕 뒤쪽은 나사(스크류) → 완전히 분해해 세척 가능, 조임 조절 가능. <b>그냥 쓰지 말고 풀었다가 적당히 다시 조이기.</b></li>
<li>너무 느슨 → <b>샌다</b>. 너무 꽉 → 잘 안 돌아가고 깨지거나 손을 다침.</li>
<li>왜 중요? 종말점에서는 <b>한 방울</b>로 성질이 급변 → 스톱콕을 빨리 잠그지 못하면 종말점을 넘겨 <b>실험을 다시</b> 해야 한다.</li>
<li>누출 확인: 물을 채워 0.00 근처에 두고 잠시 놔뒀을 때 눈금이 내려가는지, 스톱콕에서 맺히는지 본다.</li></ul>""",
side=prof("오늘 중요한 건 뷰렛을 사용하고 눈금을 읽는 것. 그걸 못 하면 오늘 실험은 의미가 없다.")
 + card("trap", "③ 기포 제거 ★ 제일 중요", "액체가 지나는 관(특히 스톱콕 아래 끝부분)에 <b>기포가 하나도 없어야</b> 한다. 기포가 나중에 빠지면 그 부피만큼 눈금이 틀어진다. → 처음부터 끝까지 눈으로 확인, 기포가 있으면 <b>밸브를 확 열어</b> 밀어낸 뒤 다시 채운다. <span class=\"ko\">(유인물: 공기 방울은 반드시 제거한 후 사용)</span>"))

use2 = pg("p-use2", "5", "뷰렛 사용법 — 오늘의 핵심 실기 ④–⑥", "눈금 읽기 · 유출 속도 · 저울", K3,
main="""<div class="sec">④ 눈금 읽기 — 메니스커스 &amp; 시차오차</div>
<ul><li>물의 경계면은 아래로 오목한 반달 = <b>메니스커스</b> → <b>맨 아랫부분</b>을 읽는다.</li>
<li><b>시차오차(parallax error)</b>: 눈높이를 메니스커스에 맞춰야 함. 아래에서 보면 <b>과대</b>, 위에서 보면 <b>과소</b> 평가.</li>
<li>내 키를 맞추거나, 뷰렛을 스탠드에서 위아래로 옮겨 수평을 맞춘다.</li>
<li>눈금 간격은 0.1 mL → 그 사이를 눈으로 10등분해서 <b>소수 둘째 자리(0.01)까지 반드시</b> 기록. (10.0 ✗ → 10.00 ✓)</li>
<li>눈금선 두께(약 0.02 mL), 한 방울(약 0.05 mL)은 따로 고려하지 말고 정확히 읽기만.</li></ul>
<div class="sec">⑤ 유출 속도</div>
<ul><li>적정한 유출 속도는 <b>20 mL/min 이하</b> (50 mL 뷰렛에서 절반 내려가는 데 약 1분).</li>
<li>시간 잴 필요 없이 <b>"똑, 똑, 똑" 끊어서 떨어지게</b>만 하면 자동으로 이 속도. 연속으로 주르륵 흐르면 → <b>감점</b>. <span class="ko">(빨리 흘리면 벽에 액체가 많이 남아 나간 양이 적어지고, 적정에선 종말점을 넘기기 쉬움)</span></li>
<li>남은 액체를 뿌리지(털어내지) 않는다.</li></ul>
<div class="sec">⑥ 저울 사용 <span class="ko">(유인물 3쪽 요약)</span></div>
<ul><li>진동·바람·습기·직사광선·난방기 피하기, <b>수평</b> 유지(기포 수평계).</li>
<li>시료를 넣고 뺄 땐 저울을 정지 상태로, 접시 가운데에 놓기. Tare 기능 활용. 최대 칭량치 초과 금지.</li>
<li>가열한 시료는 데시케이터에서 식힌 뒤. 청소할 때 물 사용 금지.</li>
<li><b>교수님 팁</b>: 여러 번 재야 하므로 <b>처음 쓴 저울을 끝까지 같은 걸로</b> 사용 (저울 간 차이 제거). 주변에 물 흘리면 닦기 → 오차 커짐.</li></ul>""",
side=f'<div class="fig">{PARALLAX}<div class="cap">눈높이 = 메니스커스 바닥일 때만 정확</div></div>')

meth = pg("p-meth", "6", "실험 방법", "유인물 4쪽", K4,
main="""<p><b>시약 및 기구</b>: buret (50 mL) &amp; stand, buret holder, Erlenmeyer flask (100 mL), beaker (100 mL), washing bottle, chemical balance, 탈이온수</p>
<ol><li>뷰렛을 준비한다 (세척 및 헹굼, 누출 점검).</li>
<li>뷰렛에 탈이온수를 채워 스탠드에 세우고 <b>0 mL 표선</b>에 눈금을 맞춘다. <span class="ko">(꼭 0.00일 필요는 없지만 0.00에서 시작하면 "눈금 차" 계산이 필요 없어 편함)</span></li>
<li>탈이온수 <b>10, 20, 30, 40, 50 mL</b>를 삼각플라스크에 받아 각각 질량을 측정한다 (눈금·무게 모두 <b>누적</b>).</li>
<li>3번을 <b>2회 반복</b>하여, 측정 질량에서 추정된 부피와 실제 뷰렛 눈금의 편차(보정치)를 구해 눈금에 대해 도시 → <b>검정곡선</b>.</li>
<li>실제 적정 때 검정곡선으로 측정치를 보정한다. 이때 <b>시작 눈금과 최종 눈금 모두</b> 보정.</li></ol>""" + FLOW,
side=prof("10 mL를 정확히 맞추려고 애쓰지 마라. 10 언저리에서 멈추고 <b>그 눈금을 정확히 읽는 것</b>이 중요하다. 9.98도 좋고 10.04도 좋다. 결과가 이상하면 옆 빈칸에 그 10 mL 구간만 다시 측정해 봐라."))

res = pg("p-res", "7", "오늘 우리 조 결과 (녹취록 기준)", "수온 19 °C, ρ = 0.99842 g/mL(Table 1.2)로 다시 계산 · 빈 삼각플라스크 = 45.32 g", K4,
main=our_table() + card("tip", "✅ 해석 (고찰에 쓸 내용)", """<ul style="margin:0">
<li>모든 보정치가 <b>−0.04 ~ +0.03 mL</b> → 제조사 허용오차 <b>±0.1 mL 안</b>에 들어옴 → 우리 뷰렛은 보증 정확도를 만족.</li>
<li>보정치가 구간마다 +/−로 달라짐 → 뷰렛 관의 안지름이 완전히 균일하지 않기 때문(제조 공차) + 읽기·칭량의 우연오차.</li>
<li>±0.1을 벗어나면? → 실험을 잘못했거나(기포, 시차, 흘림, 너무 빠른 유출) 뷰렛이 불량. 보통은 잘 나온다.</li></ul>"""),
side=f'<div class="fig">{curve(OUR, "우리 조 뷰렛 검정곡선 (녹취록 데이터, 19 °C)", w=520, h=280)}</div>'
 + card("trap", "⚠️ 노트 쓰기 전에 확인할 것", """<ul style="margin:0">
<li>녹취록에서 친구들은 ρ를 0.998로 계산해 30 mL 구간 29.98(+0.03), 50 mL 구간 49.97(−0.03)이라 했는데, 0.998로도 정확히는 29.99(+0.04)·49.98(−0.02), <b>표의 0.99842로는 위 표 값</b>이 맞다. 노트에는 표에서 찾은 밀도와 그 값으로 계산한 결과를 쓰자.</li>
<li>위 숫자는 <b>녹취록(AI 전사)에 나온 값</b>이라 전사 오류가 있을 수 있다. 실제 기록지/단톡방 사진의 값으로 교체할 것.</li>
<li>유인물은 <b>2회 반복</b>을 요구한다. 오늘 1회만 했다면 고찰에 그 사실을 적고, 2회 했다면 두 번의 보정치를 평균해 그린다.</li>
<li>저울이 0.001 g까지 표시됐다면 무게도 소수 셋째 자리까지 기록(유인물 예시처럼).</li></ul>"""))

crv = pg("p-curve", "8", "검정곡선은 다음 주부터 이렇게 쓴다", "유인물 4쪽 예시", K4,
core="적정할 때마다 <b>시작 눈금과 최종 눈금을 각각</b> 검정곡선에서 보정치를 읽어 보정한 뒤 뺀다 (두 점 사이 값은 선으로 이은 그래프에서 읽기 = 직선 보간).",
main="""<table class="t"><tr><th></th><th>시작</th><th>최종</th></tr>
<tr><td>뷰렛 눈금 (mL)</td><td>8.25</td><td>29.43</td></tr>
<tr><td>보정치 (mL, 곡선에서 읽음)</td><td>+0.03</td><td>−0.03</td></tr>
<tr><td>보정된 부피 (mL)</td><td>8.28</td><td>29.40</td></tr>
<tr><td colspan="3"><b>실제 용출된 부피 = 29.40 − 8.28 = 21.12 mL</b> <span class="ko">(보정 안 하면 21.18 mL → 0.06 mL 차이)</span></td></tr></table>
<p class="ko">↑ 유인물 4쪽 예시 (Harris 교재의 50 mL 뷰렛 검정곡선 사용 예).</p>
<div class="sec">참고: 유인물 예시 데이터 (5. 실험결과)</div>
<table class="t"><tr><th>뷰렛 눈금</th><th>플라스크 총무게 (g)</th><th>물 무게 (g)</th><th>눈금 차 (mL)</th><th>실제 부피 (mL)</th><th>보정치 (mL)</th></tr>
<tr><td>0.04</td><td>50.554</td><td>0.000</td><td>0.00</td><td>0.00</td><td>0.00</td></tr>
<tr><td>10.04</td><td>60.530</td><td>9.976</td><td>10.00</td><td>9.99</td><td>−0.01</td></tr>
<tr><td>20.06</td><td>70.469</td><td>19.915</td><td>20.02</td><td>19.95</td><td>−0.07</td></tr>
<tr><td>29.95</td><td>80.364</td><td>29.810</td><td>29.91</td><td>29.86</td><td>−0.05</td></tr>
<tr><td>40.05</td><td>90.379</td><td>39.825</td><td>40.01</td><td>39.90</td><td>−0.11</td></tr>
<tr><td>50.04</td><td>100.372</td><td>49.818</td><td>50.00</td><td>49.91</td><td>−0.09</td></tr></table>""",
side=f'<div class="fig">{curve(HAND, "유인물 예시 데이터로 그려 본 검정곡선", ymax=0.14, w=520, h=260)}</div>'
 + card("tip", "📌 예시에서 볼 것", """<ul style="margin:0"><li>시작이 0.04라서 <b>"눈금 차 = 눈금 − 시작 눈금"</b> 칸이 필요하다. 0.00에서 시작하면 이 칸이 없어진다(교수님 말씀).</li>
<li>예시는 40 mL 구간이 −0.11로 ±0.1을 살짝 넘는다 → 이런 경우 그 구간을 재측정하거나 고찰에서 원인을 논의.</li></ul>"""))

QA = [
("Q1. 뷰렛 검정의 목적은?", "제조사 허용오차(±0.1 mL) 범위 안에서 실제로 정확한 부피가 측정되는지 확인하고, 보정치(검정곡선)를 얻어 이후 적정값을 보정하기 위해."),
("Q2. 실제 부피는 어떻게 구하나?", "흘려보낸 물의 질량을 저울로 재고, 측정 수온에서의 물의 밀도로 나눈다. V = m / ρ."),
("Q3. 보정치의 정의와 부호의 의미는?", "보정치 = 실제 부피 − 눈금. +면 눈금보다 많이 나감, −면 적게 나감. 보정 부피 = 눈금 + 보정치."),
("Q4. 검정곡선의 x축, y축은?", "x축 = 뷰렛 눈금(mL), y축 = 보정치(mL)."),
("Q5. TC와 TD의 차이와 예는?", "TC(수용): 용기 안에 담긴 부피 보증 — 부피플라스크. TD(출용): 옮겼을 때 나간 부피 보증 — 뷰렛, 피펫, 출용 메스실린더."),
("Q6. 뷰렛에 담긴 액체의 부피와 실제 나간 부피 중 어느 것이 큰가?", "담긴 부피가 더 크다(벽에 남는 액체). 눈금은 나간 부피 기준으로 그려져 있다."),
("Q7. 뷰렛 눈금은 어디까지 읽나? 메니스커스는 어디를 읽나?", "소수 둘째 자리(0.01 mL)까지. 메니스커스의 맨 아랫부분을 눈높이를 맞춰 읽는다."),
("Q8. 시차오차: 아래에서 보면? 위에서 보면?", "아래에서 보면 과대평가, 위에서 보면 과소평가."),
("Q9. 적절한 유출 속도는?", "20 mL/min 이하 — 한 방울씩 끊어서 떨어지게."),
("Q10. 한 방울의 부피와 눈금선의 두께는 대략?", "한 방울 ≈ 0.05 mL, 눈금선 두께 ≈ 0.02 mL."),
("Q11. 측용기를 가열 건조하면 안 되는 이유는?", "열로 유리가 팽창·변형되어 부피(눈금)가 달라질 수 있기 때문. 실온 자연건조."),
("Q12. 시간이 없어 뷰렛을 말릴 수 없을 때는?", "사용할 용액(표준액)으로 여러 번 린싱해 내벽의 물을 대체한다."),
("Q13. 왜 기포를 꼭 빼야 하나?", "관 속 기포가 적정 중 빠져나가면 그 부피만큼 눈금이 실제 유출량과 달라지기 때문."),
("Q14. 적정 후 실제 용출 부피 계산 시 보정은 어디에?", "시작 눈금과 최종 눈금 모두 각각 보정한 뒤 뺀다. (예: 29.40 − 8.28 = 21.12 mL)"),
("Q15. 물의 밀도는 온도가 오르면?", "작아진다 (19 °C 0.99842 → 25 °C 0.99705 g/mL). 그래서 수온 측정이 필요."),
("Q16. 이번 학기 적정 4종은?", "중화 적정, 침전 적정, 킬레이트(EDTA) 적정, 산화환원 적정."),
]


def qa(items):
    return "".join(f'<div class="qa"><div class="q">{q}</div><div class="a">{a}</div></div>' for q, a in items)


qa1 = pg("p-qa1", "9", "기말 대비 핵심 체크 (Q&amp;A) ①", "Q1–Q8", K4, main=qa(QA[:4]), side=qa(QA[4:8]))
check = card("tip", "📝 실험노트 No.1 쓰기 체크리스트", """<ul style="list-style:none;padding-left:0;margin:0">
<li>□ 노트 번호, 페이지 번호, 매 페이지 서명, <b>실험일자 = 실험한 날(목)</b></li>
<li>□ 제목: 뷰렛의 검정 / 목적 / 원리(TC·TD, V = m/ρ, 보정치 정의) / 시약 및 기구</li>
<li>□ 방법: 실제로 한 순서대로(과거형) — 누출 확인, 기포 제거, 0.00 맞춤, 10 mL 간격, 같은 저울</li>
<li>□ 결과: 수온과 사용한 밀도값, Table I(측정 데이터), Figure 1(검정곡선, x = 눈금 · y = 보정치)</li>
<li>□ 고찰: ±0.1 mL 이내인지 판정, 오차 원인(시차·기포·유출 속도·온도·칭량), 반복 측정 여부</li>
<li>□ 출력물: 4면 부착 + 간인 / 여백엔 사선 + "여백" / 볼펜 / 틀리면 두 줄 + 서명</li>
<li>□ <b>월요일 18:00까지 401호 앞 박스</b></li></ul>""")

qa2 = pg("p-qa2", "9", "기말 대비 핵심 체크 (Q&amp;A) ② · 노트 체크리스트", "Q9–Q16", K4, main=qa(QA[8:]), side=check)

E = [cover, over, safe, note, prin, tctd, use1, use2, meth, res, crv, qa1, qa2]
