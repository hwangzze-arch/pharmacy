from parts import *
P = P4

E = [
dict(t="c", id="c-hyph", part=P, title="GC-MS · LC-MS — 왜 LC 연결이 어려웠나",
sub="Hyphenated techniques · ionization time line · API",
core="현대 MS는 대부분 <b>크로마토그래피와 연결</b>(분리 → 이온화 → 질량 측정)해서 쓴다. GC는 시료가 이미 <b>기체</b>라 EI·CI로 쉽게 연결됐지만, LC는 <b>용액</b>을 <b>기체 이온</b>으로 바꿔야 해서 <b>API(대기압 이온화)</b>가 나오고서야 연결됐다.",
detail="""<ul><li>🗣️ 크로마토그래피(고압)와 질량분석기(고진공)는 <b>압력 조건이 정반대</b> → 연결이 기술적으로 역설적</li>
<li>🗣️ LC의 어려움: 용액이 기체가 되면 <b>부피가 엄청나게</b> 늘어남 + 용액 속 분자를 기체 이온으로 바꾸기 어려움</li>
<li>두 기술을 하이픈으로 잇는 것 = <b>hyphenated technique</b> (GC-MS, LC-MS, LC-MS/MS)</li></ul>
<table class="t imp"><tr><th>크로마토그래피</th><th>이온화법</th><th>이유</th></tr>
<tr><td><b>GC</b></td><td><b>EI, CI</b> (진공 이온원)</td><td>이미 기체</td></tr>
<tr><td><b>LC</b></td><td><b>API = ESI, APCI, APPI</b> (대기압)</td><td>용매를 날리면서 이온을 만들어야</td></tr></table>
<p><b>연대표</b>: EI 1929 → CI 1965 → … → 열분무(TS) 1980 → <b>ESI 1984</b> → <b>MALDI 1985</b> → “Not done!”<br>
🗣️ <b>ESI는 2002년 노벨상</b> (존 펜). 같은 해 다나카 고이치(소프트 레이저 탈착, MALDI 계열)도 공동 수상. 지금 거의 모든 MS에 ESI 이온원 (약대 2대 모두).</p>""",
side=[("img","L5-34","원본 슬라이드 49 — 이온화 방법의 연대표"),
("ana","GC-MS는 <b>이미 김(기체)이 된 차</b>를 바로 마시는 것. LC-MS는 <b>찻잔(용액)째</b> 마셔야 하는데 기계(진공)가 물을 못 마셔 → 물만 날리고 찻잎 향(이온)만 뽑아내는 기술(ESI)이 노벨상."),
("trap","“APCI는 GC-MS의 이온화법이다” → <b>X</b> (LC용 API). “EI·CI는 대기압 이온화” → <b>X</b> (진공 이온원).")],
one="GC → EI·CI (이미 기체) / LC → API = ESI·APCI·APPI (대기압). ESI 1984 개발, 2002 노벨상."),

dict(t="c", id="c-esi", part=P, title="ESI(전기분무 이온화) — 용액에서 이미 이온, 쿨롱 폭발",
sub="Electrospray ionization · Taylor cone · Coulombic explosion · adduct & multiply charged ions",
core="LC 용출액을 <b>강한 전기장 속에서 뜨겁게 분무</b>한다. 용액 속에 <b>이미 있던 이온</b> 중 전기장 반대 부호 이온만 끌려 나와 액적에 담기고, 용매가 증발해 액적이 작아지다 <b>쿨롱 폭발</b>로 쪼개져 <b>기체 이온</b>이 된다.",
detail="""<ol><li>🗣️ 전기장: 수업 예 <b>−3,500 V → 양이온 분석</b> (음이온은 +3,500 V). 슬라이드 그림: 모세관 0 V, MS 입구 −4,500 V</li>
<li>뜨거운 <b>건조 기체(N₂)</b> + 분무관(nebulizer capillary)으로 열분무</li>
<li>★ <b>이온화는 용액 상태에서 이미</b> 일어나 있음 (조금만 이온화돼도 충분) → <y>약산 = 음이온 모드, 약염기 = 양이온 모드</y></li>
<li>모세관 끝 <b>테일러 콘(Taylor cone)</b>에서 한 부호 이온만 담긴 액적(~1 μm) 분무</li>
<li>용매 증발 → 액적 작아짐 → 전하끼리 반발이 표면장력을 이기면(레일리 한계) <b>펑 (쿨롱 폭발)</b> → 반복 → 기체 이온(~10 nm)</li></ol>
<table class="t"><tr><th>양이온 모드 부가 이온</th><th>m/z</th><th>음이온 모드</th><th>m/z</th></tr>
<tr><td>[M+H]⁺</td><td>M+1</td><td>[M−H]⁻</td><td>M−1</td></tr>
<tr><td>[M+NH₄]⁺</td><td>M+18</td><td>[M+HCOO]⁻</td><td>M+45</td></tr>
<tr><td>[M+Na]⁺</td><td>M+23</td><td>[M+CH₃COO]⁻</td><td>M+59</td></tr>
<tr><td>[M+K]⁺</td><td>M+39</td><td colspan="2"></td></tr></table>
<p><b>다가 이온 [M+nH]ⁿ⁺</b>: 단백질처럼 큰 분자는 H⁺가 여러 개 붙어 m/z가 작아짐 → 일반 질량 범위에서 측정 가능 (ESI만의 특징)</p>""",
side=[("img","L5-36","원본 슬라이드 51 — 테일러 콘, 액적 분열, 부가 이온 목록"),
("ana","🗣️ 양이온만 가득 담은 물방울에 뜨거운 바람을 불면 물이 날아가 방울이 작아지고, 서로 밀어내던 양이온들이 너무 가까워지면 <b>펑!</b> 하고 흩어지며 기체 이온이 돼."),
("trap","“ESI는 기체 상태 중성 분자에 전자를 쏘아 이온화한다” → <b>X</b> (그건 EI). ESI는 <b>용액에서 이미 생긴 이온</b>을 꺼내는 것. 부가 이온 [M+Na]⁺ = <b>M+23</b> (M+22 아님!).")],
one="ESI = 전기장 속 열분무 · 용액에서 이미 이온 · 쿨롱 폭발 · 약산→음이온, 약염기→양이온 · 다가 이온·부가 이온 · 휘발성 불필요."),

dict(t="c", id="c-apci", part=P, title="APCI · APPI — ESI와 무엇이 다른가 ★",
sub="APCI (corona discharge, gas-phase CI) vs ESI · ionization map by MW & polarity",
core="APCI는 <b>약 500 °C로 분무해 기화</b>시킨 <b>중성 분자</b>를 <b>코로나 니들</b>의 전자 → H₃O⁺(기체 강산) → 양성자 전달로 <b>기체 상태에서</b> 이온화한다. 그래서 <b>휘발성이 필요</b>하고 단백질은 안 된다.",
detail="""<ul><li>🗣️ 전기장에 분무하는 게 아님. 분무 끝에 <b>코로나 니들(약 6,000 V)</b> → 전자 방출 → N₂·용매와 연쇄 반응 → <b>H₃O⁺(수화된 하이드로늄)</b> → 기체 중성 분자에 H⁺ 전달</li>
<li>= 대기압에서 하는 <b>화학 이온화(CI)</b></li></ul>
<table class="t imp"><tr><th></th><th>ESI</th><th>APCI</th></tr>
<tr><td><b>이온이 생기는 곳</b></td><td><b>용액 (liquid-phase)</b></td><td><b>기체 (gas-phase)</b></td></tr>
<tr><td>원리</td><td>이미 있는 이온 + 전기장 + 쿨롱 폭발</td><td>코로나 방전 → H₃O⁺ → 양성자 전달</td></tr>
<tr><td><b>분석물 휘발성 필요?</b></td><td><b>No</b></td><td><b>Yes</b></td></tr>
<tr><td>거대분자 (단백질·DNA)</td><td><b>가능</b> (다가 이온)</td><td>불가 (가열하면 분해)</td></tr>
<tr><td>잘 맞는 시료</td><td>극성, 분자량 ~100–100,000</td><td>중간 극성, 분자량 ~1,500 이하</td></tr></table>
<p><b>APPI</b> (Atmospheric Pressure Photoionization): <b>UV 빛</b>으로 전자를 떼어냄 → 양성자를 잘 못 받는 <b>가장 비극성</b> 물질 (PAH 등)</p>
<p>🗣️ “다 외울 필요는 전혀 없고, <b>이온화 매질(용액/기체)</b>과 <b>휘발성 필요 여부(No/Yes)</b> 기본 차이는 잘 알아 둬라.”</p>""",
side=[("img","L5-40","원본 슬라이드 55 — 분자량·극성 지도: ESI(파랑), APCI(초록), APPI(분홍)"),
("img","L5-38","원본 슬라이드 53 — APCI 장치, 코로나 방전"),
("trap","“APCI는 단백질 분석에 적합하다” → <b>X</b>. “ESI는 분석물이 휘발성이어야 한다” → <b>X</b>. 지도: 비극성일수록 APCI → APPI 쪽.")],
one="ESI = 용액에서 이온·휘발성 X·단백질 O / APCI = 기체에서 이온(코로나 → H₃O⁺)·휘발성 O·단백질 X / APPI = 빛, 가장 비극성."),

dict(t="q", id="q-api", part=P, kind=["multi"], title="ESI · APCI — 다답형",
src="슬라이드 48–55 · 수업 녹음(둘째 수업)",
q="""LC-MS의 대기압 이온화(API)에 대한 설명으로 <b>옳은 것을 모두</b> 고르시오.
<ul class="opts"><li>① ESI에서 분석물의 이온은 주로 용액 상태에서 이미 만들어져 있던 것이다.</li>
<li>② 약염기성 약물을 ESI로 분석할 때는 음이온 모드가 일반적으로 유리하다.</li>
<li>③ APCI는 기체 상태의 중성 분자를 코로나 방전으로 생긴 H₃O⁺와 반응시켜 이온화한다.</li>
<li>④ 분자량 66 kDa의 단백질은 APCI보다 ESI로 분석하는 것이 적합하다.</li>
<li>⑤ GC-MS에서는 시료가 이미 기체이므로 주로 ESI를 사용한다.</li></ul>""",
a="①, ③, ④",
steps=[("① ESI의 핵심: 이온화를 따로 시킬 필요 없이 용액 속 이온을 꺼냄 ✓",""),
("② 약염기 = 용액에서 H⁺를 받아 <b>양이온</b> → 양이온 모드. ✗","약산 = 음이온 모드."),
("③ 코로나 니들 → 전자 → H₃O⁺ → 기체상 양성자 전달 = 대기압 CI ✓",""),
("④ 단백질은 기화 불가 → APCI 불가. ESI는 휘발성 불필요 + 다가 이온 ✓",""),
("⑤ GC-MS = <b>EI, CI</b>. ESI는 LC용. ✗","")],
one="ESI: 용액 이온·약염기→양이온·단백질 O. APCI: 기체상 CI·휘발성 필요. GC = EI·CI."),

dict(t="q", id="q-adduct", part=P, kind=["calc","bl"], title="부가 이온 · 다가 이온 계산",
src="슬라이드 51 · 수업 녹음(첫 수업)",
q="""분자량(명목질량) 300인 중성 약물 M을 ESI로 분석했다. 빈칸을 채우시오. (H 1, Na 23, K 39, NH₄ 18)<br>
(1) 양이온 모드: [M+H]⁺ = <span class="blank">(가)</span>, [M+NH₄]⁺ = <span class="blank">(나)</span>, [M+Na]⁺ = <span class="blank">(다)</span>, [M+K]⁺ = <span class="blank">(라)</span><br>
(2) 음이온 모드: [M−H]⁻ = <span class="blank">(마)</span>, [M+HCOO]⁻ = <span class="blank">(바)</span><br>
(3) 스펙트럼에 m/z 301과 323이 함께 보였다. 차이 22는 <span class="blank">(사)</span>에 해당하므로 두 피크는 같은 분자에서 나온 것이다.<br>
(4) 분자량 10,000인 단백질이 [M+10H]¹⁰⁺로 검출되면 m/z ≈ <span class="blank">(아)</span>이다.""",
a="(가) 301 (나) 318 (다) 323 (라) 339 (마) 299 (바) 345 (사) Na − H (23 − 1) (아) 1,001",
steps=[("양이온: 300 + 1, + 18, + 23, + 39","부가 이온 m/z = M + 붙은 이온 질량 (전하 1)."),
("음이온: 300 − 1 = 299, 300 + 45(HCOO⁻) = 345",""),
("323 − 301 = 22 = [M+Na]⁺ − [M+H]⁺ = 23 − 1","두 피크 간격으로 분자량을 교차 확인하는 요령."),
("(10,000 + 10×1) / 10 = 1,001","다가 이온: m/z = (M + n) / n → 큰 단백질도 작은 m/z로.")],
one="부가 이온 = M + 붙은 것 (H 1, NH₄ 18, Na 23, K 39 / −H, HCOO 45). 다가 이온 m/z = (M+n)/n."),

dict(t="q", id="q-esi-sa", part=P, kind=["sa"], title="서술형 — ESI는 되고 APCI는 안 되는 이유",
src="슬라이드 54–55 · 수업 녹음(둘째 수업: “노벨상을 받을 만한 게…”)",
q="""단백질과 같은 거대분자를 LC-MS로 분석할 때 ESI는 사용할 수 있지만 APCI는 사용하기 어렵다. 두 이온화법의 <b>이온화가 일어나는 상태</b>와 <b>분석물의 휘발성 요구</b>를 비교하여 그 이유를 서술하시오.""",
a="아래 모범 답안 (키워드: 용액상 vs 기체상, 휘발성 No vs Yes, 기화 시 분해, 쿨롱 폭발, 다가 이온)",
steps=[("<b>ESI</b>: 분석물이 용액 속에서 이미 이온 상태로 존재하고, 전기장 속에 열분무된 하전 액적에서 용매가 증발하다 쿨롱 폭발로 기체 이온이 방출된다. 분석물을 기화시킬 필요가 없으므로 휘발성이 필요 없고, 여러 개의 H⁺가 붙은 다가 이온으로 m/z가 작아져 거대분자도 측정할 수 있다.",""),
("<b>APCI</b>: 약 500 °C에서 분무해 분석물을 기체 상태의 중성 분자로 만든 뒤 코로나 방전으로 생긴 H₃O⁺와의 기체상 화학 반응으로 이온화한다. 따라서 분석물이 기화될 수 있어야(휘발성) 하는데, 단백질은 기화되지 않고 가열하면 분해되므로 분석할 수 없다.","")],
one="ESI = 용액에서 이온(휘발성 X, 다가 이온) / APCI = 기체에서 이온(휘발성 O) → 단백질은 ESI만."),

dict(t="c", id="c-sim", part=P, title="LC-MS 데이터 — TIC · SIM · EIC",
sub="Total ion chromatogram · selected ion monitoring · extracted ion chromatogram",
core="<b>TIC</b> = 범위 내 모든 m/z를 스캔해 <b>다 더한</b> 크로마토그램. <b>SIM</b> = 측정 <b>전에</b> 사중극자를 고정해 원하는 m/z만 검출. <b>EIC</b> = 스캔해 둔 데이터에서 측정 <b>후에</b> 원하는 m/z만 뽑아 다시 그린 것.",
detail="""<ul><li>🗣️ 기기분석의 두 데이터: <b>크로마토그램(x축 = 시간)</b>, <b>스펙트럼(x축 = 파장·화학적 이동·m/z)</b></li>
<li>예: 강물에 제초제 6종 <b>1 ppb</b> 스파이크 → LC-UV(240 nm)는 잡피크·바탕선 출렁임 → LC-MS TIC도 별 차이 없어 보임 (🗣️ “1억 더 쓸 가치? 여기서 끝이 아니라 시작”)</li>
<li>데이터는 <b>3차원</b>(시간 × m/z × 세기) → 원하는 축만 골라 그림</li></ul>
<table class="t imp"><tr><th></th><th>TIC</th><th>SIM</th><th>EIC (XIC)</th></tr>
<tr><td>측정</td><td>스캔 (모든 m/z)</td><td><b>선택한 m/z만</b> (DC/RF 고정)</td><td>스캔 (모든 m/z)</td></tr>
<tr><td>언제 고르나</td><td>—</td><td><b>측정 전</b></td><td><b>측정 후</b> (컴퓨터로 추출)</td></tr>
<tr><td>실험</td><td>—</td><td>새로 설정해 측정</td><td>새 실험 X, 다르게 플롯</td></tr>
<tr><td>선택성·감도</td><td>낮음 (잡피크 多)</td><td><b>가장 높음</b></td><td>중간 (기기 능력이 분산)</td></tr></table>
<p>🗣️ SIM: 6번 제초제 = m/z 312만 입력 → 잡피크 싹 사라지고 피크 하나. 여러 이온을 몇 ms씩 순차 모니터링(6개, 20개, 100개…)도 모두 SIM.<br>
🗣️ “<b>SIM 모드와 EIC를 구분할 줄 알아야 돼요.</b>”</p>""",
side=[("img","L5-43","원본 슬라이드 58 — SIM으로 m/z 312만 검출"),
("img","L5-44","원본 슬라이드 59 — EIC vs SIM"),
("trap","“EIC는 사중극자를 특정 m/z에 고정하고 측정한 것” → <b>X</b> (그건 SIM). “EIC가 SIM보다 감도가 높다” → <b>X</b>.")],
one="TIC = 전부 더함 · SIM = 측정 전 선택(감도 최고) · EIC = 측정 후 추출(새 실험 X). 크로마토그램은 x = 시간!"),

dict(t="q", id="q-sim", part=P, kind=["mc","bl"], title="TIC · SIM · EIC 구분",
src="슬라이드 56–59 · 수업 녹음(둘째 수업)",
q="""(1) 다음 중 <b>옳은 것</b>을 하나 고르시오.
<ul class="opts"><li>① TIC는 선택한 한 가지 m/z의 신호만 시간에 따라 나타낸 것이다.</li>
<li>② EIC를 얻으려면 사중극자의 DC/RF를 특정 값에 고정한 채 다시 측정해야 한다.</li>
<li>③ 같은 이온을 정량할 때 SIM이 EIC보다 일반적으로 선택성과 감도가 높다.</li>
<li>④ 질량 스펙트럼은 x축이 시간, y축이 세기인 그래프이다.</li></ul>
(2) 스캔으로 m/z 50–500을 모두 측정해 둔 데이터에서 m/z 202에 해당하는 열만 골라 y값으로 다시 그린 것은 <span class="blank">(가)</span>이고, 모든 m/z 신호를 단순히 합해 그린 것은 <span class="blank">(나)</span>이다.""",
a="(1) ③ (2) (가) EIC (나) TIC",
steps=[("① TIC는 모든 이온의 합. 한 m/z만은 SIM 또는 EIC. ✗",""),
("② EIC는 새로 측정하지 않고 기존 스캔 데이터를 추출. 고정해서 측정하는 건 SIM. ✗",""),
("③ SIM은 기기 능력을 원하는 이온에 집중 → 선택성·감도↑ ✓",""),
("④ x축 = 시간이면 크로마토그램. 질량 스펙트럼은 x = m/z. ✗",""),
("(2) 사후 추출 = EIC, 단순 합 = TIC","")],
one="SIM = 측정 전, EIC = 측정 후. 감도 SIM > EIC. x = 시간 → 크로마토그램."),

dict(t="c", id="c-tandem", part=P, title="탠덤 MS(MS/MS) · 삼중 사중극자의 스캔 모드",
sub="Tandem MS · QQQ (Q1 – q2 collision cell – Q3) · CID = CAD · 6 scan modes",
core="질량분석을 한 번 하고, 거기서 <b>고른 이온으로 한 번 더</b> 질량분석 = MS/MS. 삼중 사중극자(QQQ)는 <b>Q1(선택) → q2(충돌관, 조각화) → Q3(선택/스캔)</b>. q2는 질량 선택을 안 해서 MS/MS/MS가 아니라 <b>MS/MS</b>.",
detail="""<ul><li>🗣️ 요즘 MS는 거의 다 탠덤 (비싸지만 장점 압도적, 약대 2대 모두)</li>
<li>🗣️ <b>q2 = 충돌관(collision cell)</b>: N₂·Ar을 넣어 선택된 이온을 충돌시켜 조각화. 질량 선택 없이 이온 빔이 흩어지지 않게 모아주기만 → 요즘은 <b>헥사폴(전극 6개, 60°)</b>. 소문자 q로 쓰기도</li>
<li>충돌로 조각나는 것 = <b>CID (collision-induced dissociation) = CAD (collision-activated dissociation)</b> — 같은 말</li>
<li>ESI 이온원 안(모세관–스키머 사이)에서 일어나는 <b>in-source CID</b>는 모든 이온이 같이 깨져 누구 조각인지 모름 → <y>먼저 질량으로 고르고 깨는 탠덤이 필요</y></li></ul>
<p><b>모드 수</b>: Q1(Scan / SIM / RF only) 3 × q2(On / Off) 2 × Q3 3 = <b>이론상 18</b> → 실제로 쓰는 건 <b>6</b>. (🗣️ RF only = DC를 끄면 일정 범위 모든 이온 통과)</p>
<table class="t imp"><tr><th>모드</th><th>Q1</th><th>q2</th><th>Q3</th><th>알 수 있는 것</th></tr>
<tr><td>Full scan</td><td>Scan</td><td>Off</td><td>RF only</td><td>무엇이 들었나</td></tr>
<tr><td>SIM</td><td>SIM</td><td>Off</td><td>RF only</td><td>이 m/z가 얼마나</td></tr>
<tr><td><b>Product ion scan</b></td><td>SIM</td><td>On</td><td><b>Scan</b></td><td>이 선구 이온이 뭘로 깨지나 (구조, SRM 전이 찾기)</td></tr>
<tr><td><b>SRM (MRM)</b></td><td>SIM</td><td>On</td><td><b>SIM</b></td><td>선구 → 이 조각이 얼마나 (정량 끝판왕)</td></tr>
<tr><td>Precursor ion scan</td><td>Scan</td><td>On</td><td>SIM</td><td>이 조각을 내는 부모들 (같은 골격)</td></tr>
<tr><td>Neutral loss scan</td><td>Scan</td><td>On</td><td>Scan (일정 질량차)</td><td>같은 중성 손실을 보이는 이온 (같은 작용기)</td></tr></table>""",
side=[("img","L5-47","원본 슬라이드 64 — 삼중 사중극자 스캔 모드 표"),
("trap","q2가 <b>Off</b>면 MS/MS가 아님 (단일 MS 모드). “q2도 질량 선택을 한다” → <b>X</b>. 전구 이온 스캔은 <b>Q3 고정</b>, Q1 스캔 (생성 이온 스캔과 반대!).")],
one="QQQ = Q1 선택 → q2 충돌(CID = CAD, 헥사폴) → Q3. 3×2×3 = 18, 실제 6. SRM = SIM-On-SIM, Product = SIM-On-Scan."),

dict(t="q", id="q-mode", part=P, kind=["bl"], title="스캔 모드 표 채우기",
src="슬라이드 64 · 수업 녹음(둘째·셋째 수업)",
q="""삼중 사중극자의 각 모드에서 Q1, q2, Q3의 작동을 채우시오. (Q1·Q3: Scan / SIM / RF only, q2: On / Off)
<table class="t"><tr><th>모드</th><th>Q1</th><th>q2</th><th>Q3</th></tr>
<tr><td>SIM</td><td>SIM</td><td><span class="blank">(가)</span></td><td>RF only</td></tr>
<tr><td>Product ion scan</td><td><span class="blank">(나)</span></td><td>On</td><td><span class="blank">(다)</span></td></tr>
<tr><td>SRM (MRM)</td><td>SIM</td><td><span class="blank">(라)</span></td><td><span class="blank">(마)</span></td></tr>
<tr><td>Precursor ion scan</td><td><span class="blank">(바)</span></td><td>On</td><td>SIM</td></tr></table>
(2) 이론적으로 가능한 조합 수는 <span class="blank">(사)</span>가지이고, 실제로 많이 쓰는 모드는 <span class="blank">(아)</span>가지이다.<br>
(3) 충돌관에서 이온이 깨지는 과정을 CID 또는 <span class="blank">(자)</span>라고 한다.""",
a="(가) Off (나) SIM (다) Scan (라) On (마) SIM (바) Scan (사) 18 (아) 6 (자) CAD",
steps=[("SIM은 단일 MS 모드 → 충돌 Off",""),
("Product ion: 부모 하나 고르고(SIM) 깨서(On) 생기는 조각을 전부 훑음(Scan)",""),
("SRM: 부모 고르고(SIM) 깨서(On) 조각 하나 고름(SIM) → <b>선택 두 번</b>",""),
("Precursor ion: 특정 조각(Q3 SIM)을 내는 부모를 Q1이 훑음(Scan)","Product ion scan과 Q1·Q3 역할이 뒤바뀐 것."),
("3 × 2 × 3 = 18, 의미 있는 것 6",""),
("Collision-Induced Dissociation = Collision-Activated Dissociation","🗣️ “하나만 하지, 꼭 둘 다 해 가지고…”")],
one="Product = SIM-On-Scan · SRM = SIM-On-SIM · Precursor = Scan-On-SIM · 18가지 중 6가지."),

dict(t="c", id="c-srm", part=P, title="SRM = MRM — 선택을 두 번, 잡음이 사라진다",
sub="Selected / multiple reaction monitoring · S/N · EE2 3.6 ppt · Q-TOF, Q-Orbitrap",
core="SRM(= MRM): Q1에서 <b>선구 이온</b>을 고르고, q2에서 깨고, Q3에서 <b>특정 조각 이온</b>을 한 번 더 고른다. 🗣️ “<b>선택이란 단어가 중요해요.</b>” 같은 질량의 방해 물질은 구조가 달라 같은 조각을 못 만들어 걸러진다 → <b>신호는 그대로, 잡음이 사라져 S/N↑</b>.",
detail="""<ul><li>🗣️ <b>현존하는 가장 민감한 정량법 중 하나</b>. 실험실에선 다들 <b>MRM</b>이라 부름. 분석할 물질을 <b>이미 알 때</b> 사용 (의약품 분석에 흔함)</li>
<li>🗣️ 싱글 MS(SIM)와 <b>Q1까지는 똑같음</b>. q2 + Q3에서 한 번 더 고르는 게 차이</li>
<li>🗣️ SIM 크로마토그램: 원하는 질량만 골랐는데도 <b>방해 이온</b> 피크 多 (같은 질량 물질이 시료에 많고 MS가 너무 민감) → MRM: 원하는 피크 하나만</li>
<li>🗣️ “<b>시그널 자체는 커진 게 아니라요, 노이즈가 사라진 거예요.</b> 중요한 거는 S/N이거든요.”</li>
<li>🗣️ 예: SIM m/z 154 → 피크 2개 / Q3에서 152 또는 102 통과 → 뒤 피크와 앞 작은 피크들까지 사라짐</li></ul>
<table class="t"><tr><th>예</th><th>전이 (선구 → 조각)</th></tr>
<tr><td><b>17α-에티닐에스트라다이올 (EE2)</b>, 피임제, 강물 오염</td><td>[M−H]⁻ <b>295 → 159 + 145</b> (음이온 모드), <b>3.6 ppt (3.6 ng/L)</b>까지 검출</td></tr>
<tr><td>니페디핀</td><td>[M+H]⁺ 347 → 315 (−CH₃OH)</td></tr>
<tr><td>아세트아미노펜</td><td>[M+H]⁺ 152 → 110 (−케텐)</td></tr></table>
<p>📝 ppm = 10⁻⁶, ppb = 10⁻⁹, <b>ppt = 10⁻¹²</b> (교수님이 수업에서 ‘ppt = 10⁹분의 1’이라 말실수 → 슬라이드 ng/L가 맞음)</p>
<p><b>Q3 자리에 뭘 붙이나</b>: 사중극자 = QQQ (단위 분해능) / <b>TOF = Q-TOF</b> (조각 이온 정밀질량, 약대 보유) / Orbitrap = Q-Orbitrap (매우 고분해능) / linear ion trap = Q-Trap</p>""",
side=[("img","L5-48","원본 슬라이드 65 — SIM(분홍) vs MRM(파랑) 크로마토그램, 방해 이온이 사라짐"),
("img","L5-49","원본 슬라이드 66 — EE2 295 → 159 + 145, 3.6 ng/L"),
("tip","<span class=\"tag j\">족보</span> 2025-2 기말 주관식 <b>“SIM보다 SRM의 signal-to-noise가 큰 이유?”</b> → {REF:q-srm}")],
one="SRM = MRM = SIM-On-SIM · 선택 두 번 · 같은 질량 방해 물질은 같은 조각 X → 잡음↓ → S/N↑ (신호가 커진 게 아님!) · EE2 295→159/145, 3.6 ppt."),

dict(t="q", id="q-srm", part=P, kind=["sa"], title="서술형 — SIM보다 SRM의 S/N이 큰 이유 (족보)",
src="족보(2025-2 기말 주관식) · 슬라이드 65–66 · 수업 녹음(셋째 수업)",
q="""삼중 사중극자 LC-MS/MS로 혈장 속 약물을 정량할 때, 같은 시료를 SIM 모드와 SRM(MRM) 모드로 각각 측정하면 SRM의 신호 대 잡음비(S/N)가 훨씬 크다. <b>각 모드에서 Q1, q2, Q3가 하는 일</b>을 포함해 그 이유를 서술하시오.""",
a="아래 모범 답안 (키워드: 질량만으로 선택 vs 선구 이온·조각 이온 두 번 선택, 같은 m/z 방해 물질, 구조가 달라 같은 조각 X, 잡음 감소, 신호는 그대로)",
steps=[("<b>SIM</b>: Q1에서 분석물의 m/z 하나만 통과시켜 검출한다(q2 충돌 Off, Q3 RF only). 선택 기준이 <b>질량 하나뿐</b>이라 시료 속에 같은 m/z를 갖는 방해 물질도 함께 검출되어 바탕 잡음과 방해 피크가 크다.",""),
("<b>SRM</b>: Q1에서 분석물의 선구 이온을 선택하고, q2(충돌관)에서 N₂·Ar과 충돌시켜 조각화(CID)한 뒤, Q3에서 그 분석물에 특징적인 <b>조각 이온을 다시 선택</b>한다. 즉 선택이 두 번 일어난다.",""),
("<b>이유</b>: 같은 m/z의 방해 물질은 화학 구조가 달라 조각화해도 같은 조각 이온을 만들 확률이 거의 없으므로 Q3에서 걸러진다. 그 결과 분석물 신호는 그대로이지만 <b>잡음(방해 신호)이 거의 0에 가깝게 줄어</b> S/N이 크게 증가한다.","🗣️ “시그널 자체는 커진 게 아니라요, 노이즈가 사라진 거예요.”")],
one="SIM = 질량 1번 선택 → 같은 질량 방해 물질도 검출. SRM = 선구·조각 2번 선택 → 방해 물질 탈락 → 잡음↓ → S/N↑."),

dict(t="q", id="q-final", part=P, kind=["multi","calc"], title="종합 — 아세트아미노펜 LC-MS/MS 정량 시나리오",
src="수업 녹음(첫·셋째 수업: “실험에서 합성한 아세트아미노펜”) · 슬라이드 12, 26, 52, 64–65",
q="""실험에서 합성한 아세트아미노펜(C₈H₉NO₂, 명목질량 151, 단일동위원소 질량 151.0633)을 삼중 사중극자 LC-MS/MS로 정량하려 한다. <b>옳은 것을 모두</b> 고르시오.
<ul class="opts"><li>① 아세트아미노펜은 LC 용출액 속에서 이온화되므로 ESI 양이온 모드에서 [M+H]⁺ m/z 152를 선구 이온으로 쓸 수 있다.</li>
<li>② [M+H]⁺의 정밀질량은 151.0633 + 1.007825 = 152.0711로 계산한다.</li>
<li>③ SRM 채널은 Q1 152 → q2 충돌 On → Q3 110으로 설정하고, 이때 중성 손실은 케텐(42)이다.</li>
<li>④ m/z 110은 N 1개를 포함한 짝전자 이온이므로 질소 규칙에 따라 짝수인 것이 맞다.</li>
<li>⑤ 이 분석을 Q3를 Scan으로 바꿔 수행하면 SRM보다 정량 감도가 더 좋아진다.</li></ul>""",
a="①, ③, ④",
steps=[("① 질소(아마이드)·페놀이 있는 극성 약물, 학생 실험 녹음에서도 [M+H]⁺ 152 ✓",""),
("② [M+H]⁺에는 <b>양성자 1.007276</b>을 더해야 함 → 152.0706. H 원자(1.007825)를 더하면 전자 질량만큼 틀림 ✗","정밀질량 함정!"),
("③ 152 − 110 = 42 = CH₂=C=O ✓",""),
("④ N 1개(홀) + 짝전자 → 뒤집혀서 짝수 ✓",""),
("⑤ Q3 Scan = Product ion scan → 모든 조각을 훑느라 한 조각에 머무는 시간이 줄어 감도↓. 정량은 SRM이 최고 ✗","Product ion scan은 SRM 전이를 <b>찾을 때</b> 쓰는 모드.")],
one="아세트아미노펜: ESI+ [M+H]⁺ 152.0706 → SRM 152→110 (−42 케텐) · 짝전자+N홀 = 짝수 · 정량은 SRM."),
]
