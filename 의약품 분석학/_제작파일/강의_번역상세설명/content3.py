PAGES = [
# 37
dict(img=37, slide=52, title="ESI ③ — 충돌 활성화 해리(CAD/CID)", sub="ESI: Collisionally activated dissociation (CAD) or Collision-induced dissociation (CID)",
kw=["CAD = CID", "인소스 해리", "N₂와 충돌", "아세트아미노펜", "케텐 손실 42"],
sum="ESI는 소프트해서 조각이 거의 없지만, 모세관과 스키머 사이에서 이온을 가속해 N₂와 충돌시키면 일부러 깨뜨릴 수 있다(CAD). 아세트아미노펜 [M+H]⁺ 152 → 110 (케텐 42 손실).",
tr="""<p><b>충돌 활성화 해리(CAD)</b> 또는 <b>충돌 유도 해리(CID)</b></p>
<p>그림(좌): ESI 장치 — 빨간 점선 부분 = <b>모세관과 스키머 사이</b>에서 충돌 활성화 해리 발생. <b>분석물 이온과 N<sub>2</sub> 기체의 충돌</b></p>
<p>그림(우): <b>아세트아미노펜</b></p>
<ul><li>양이온: [M+H]<sup>+</sup> m/z = 152 —충돌 활성화 해리→ m/z = 110 + CH<sub>2</sub>=C=O (케텐)</li>
<li>음이온: [M−H]<sup>−</sup> m/z = 150 —충돌 활성화 해리→ m/z = 107 + [CH<sub>3</sub>CO]•</li></ul>""",
ex="""<p><b>원리</b>: 모세관 출구와 스키머 사이는 아직 기체가 꽤 있는 구간(수 mbar)이야. 여기 걸린 전압차(그림의 +40 V, −20 V 등)를 키우면 이온이 가속돼 N<sub>2</sub>와 세게 부딪히고 → <y>운동에너지가 내부에너지로 바뀌어 결합이 끊어짐</y>.</p>
<p>이온원 안에서 일어나서 <b>인소스(in-source) CID</b>라고도 해. 단점: 이온원에서 나온 모든 이온이 같이 깨져서, 섞인 시료면 어느 조각이 누구 건지 몰라 → 그래서 질량으로 먼저 고르고 깨는 <g>탠덤 MS(60번)</g>가 필요해.</p>
<div class="box"><b>아세트아미노펜 풀이</b> (C<sub>8</sub>H<sub>9</sub>NO<sub>2</sub>, M = 151)<br>
· 양이온: 152 − 110 = <b>42 = CH<sub>2</sub>=C=O (케텐, 중성 분자)</b> → 아세틸기가 떨어지고 4-아미노페놀 양이온(110) 남음. 짝전자 → 짝전자.<br>
· 음이온: 150 − 107 = <b>43 = CH<sub>3</sub>CO• (아세틸 라디칼)</b> → 남은 107은 <pk>라디칼 음이온(홀전자)</pk>. ESI에서 드문 라디칼 손실 예시.</div>
<p><b>질소 규칙 검산</b> (N 1개, 홀수): 짝전자 이온 152, 150, 110 → 짝수 ✓ / 홀전자 이온 107 → 홀수 ✓. 질소 규칙만으로도 107이 라디칼 이온임을 알 수 있어!</p>
<p class="note">CAD와 CID는 같은 말(원문 60번에도 “CAD = CID”).</p>"""),

# 38
dict(img=38, slide=53, title="APCI (대기압 화학 이온화)", sub="APCI (Atmospheric Pressure Chemical Ionization)",
kw=["가열 기화 ~500 °C", "코로나 방전 바늘", "N₂⁺ → H₃O⁺", "기체상 양성자 전달", "MH⁺"],
sum="APCI는 LC 용출액을 열과 N₂로 완전히 기화시킨 뒤, 코로나 방전으로 만든 시약 이온(H₃O⁺(H₂O)ₙ)이 분석물에 H⁺를 건네 MH⁺를 만든다. ‘대기압에서 하는 CI’.",
tr="""<ul><li>크로마토그래피 용출액이 <b>열</b>과 <b>동축 N<sub>2</sub> 기류</b>에 의해 미세한 안개로 바뀐다</li>
<li>용매와 분석물이 안개로부터 <b>증발</b>한다</li>
<li>고전압 <b>코로나 바늘</b>의 전기 방전이 분석물로부터 기체 이온을 만든다</li></ul>
<p>N<sub>2</sub> + e<sup>−</sup> → N<sub>2</sub><sup>+•</sup> + 2e<sup>−</sup><br>N<sub>2</sub><sup>+•</sup> + 2N<sub>2</sub> → N<sub>4</sub><sup>+•</sup> + N<sub>2</sub><br>N<sub>4</sub><sup>+•</sup> + H<sub>2</sub>O → H<sub>2</sub>O<sup>+•</sup> + 2N<sub>2</sub><br>H<sub>2</sub>O<sup>+•</sup> + H<sub>2</sub>O → H<sub>3</sub>O<sup>+</sup> + •OH<br>H<sub>3</sub>O<sup>+</sup> + nH<sub>2</sub>O → H<sub>3</sub>O<sup>+</sup>(H<sub>2</sub>O)<sub>n</sub><br><b>H<sub>3</sub>O<sup>+</sup>(H<sub>2</sub>O)<sub>n</sub> + M → MH<sup>+</sup> + (n+1)H<sub>2</sub>O</b></p>
<p class="note">그림 라벨: 보조 기체 · 분무 기체(N<sub>2</sub>) · 가열기(~500 °C) · 미세 안개는 ~125 °C까지 가열 · 코로나 바늘 +6 000 V · 대기압 → 고진공(0.01 Pa) · 스키머 콘(−100 V, −140 V) · 사중극자</p>""",
ex="""<p><b>8번 CI와 비교하면 쉬워</b>: CI는 진공 속에서 메테인을 전자로 이온화해 CH<sub>5</sub><sup>+</sup>를 시약 이온으로 썼지? APCI는 <y>대기압에서 코로나 방전</y>으로 N<sub>2</sub>를 이온화하고, 결국 <g>H<sub>3</sub>O<sup>+</sup>(물 클러스터)가 시약 이온</g>이 돼서 분석물에 H<sup>+</sup>를 건네.</p>
<p><b>반응식 흐름</b>: N<sub>2</sub><sup>+•</sup> → N<sub>4</sub><sup>+•</sup> → (물에 전하 전달) H<sub>2</sub>O<sup>+•</sup> → H<sub>3</sub>O<sup>+</sup> → H<sub>3</sub>O<sup>+</sup>(H<sub>2</sub>O)<sub>n</sub> → M에 양성자 전달 → <b>MH<sup>+</sup></b>. 분석물 M의 양성자 친화도가 물보다 커야 H<sup>+</sup>를 받아.</p>
<table class="t"><tr><th></th><th>ESI</th><th>APCI</th></tr>
<tr><td>이온이 생기는 곳</td><td><y>용액(액적)</y></td><td><y>기체상</y></td></tr>
<tr><td>에너지원</td><td>고전압 분무</td><td>열(~500 °C) + 코로나 방전</td></tr>
<tr><td>분석물 조건</td><td>극성·이온성</td><td>어느 정도 휘발성·열안정</td></tr></table>
<p><b>왜 가열?</b> APCI는 기체상 반응이라 분석물이 먼저 <b>기화</b>돼야 해 → 휘발성이 있고 열에 견디는 저·중극성 분자에 적합. 대신 용액 상태가 아니라서 <pk>이온 억제(매트릭스 효과)가 ESI보다 덜해</pk>.</p>
<p class="note">사진: 실제 APCI 프로브(코로나 바늘, 분무 출구). 가열기는 ~500 °C지만 실제 안개 온도는 ~125 °C 정도로, 증발 냉각 때문에 분석물이 덜 분해돼.</p>"""),

# 39
dict(img=39, slide=54, title="ESI vs APCI 비교", sub="Comparison between ESI and APCI",
kw=["이온화 상: 용액 vs 기체", "유속 0.4 vs 2 mL/min", "다전하 이온", "거대분자", "휘발성"],
sum="ESI는 용액에서 이온화 → 다전하 이온·거대분자 OK, 휘발성 불필요, 유속은 낮게. APCI는 기체상 이온화 → 단전하만, 거대분자 X, 휘발성 필요, 높은 유속 OK.",
tr="""<table class="t"><tr><th></th><th>ESI</th><th>APCI</th></tr>
<tr><td>이온화 상</td><td>용액</td><td>기체</td></tr>
<tr><td>허용 유속</td><td>최대 0.4 mL/min</td><td>최대 2 mL/min</td></tr>
<tr><td>CAD 가능 여부</td><td>예</td><td>예</td></tr>
<tr><td>단일 전하 이온 형성</td><td>예</td><td>예</td></tr>
<tr><td>다중 전하 이온 형성</td><td>예</td><td>아니오</td></tr>
<tr><td>거대분자 적합성</td><td>예</td><td>아니오</td></tr>
<tr><td>분석물 휘발성 필요</td><td>아니오</td><td>예</td></tr></table>""",
ex="""<p><span class="tag">시험 포인트</span>표 그대로 객관식이 나오기 딱 좋아. <b>이유</b>와 함께 외우면 안 헷갈려.</p>
<ul><li><b>이온화 상</b>: ESI는 액적 속 이온이 그대로 나옴 → <g>용액</g> / APCI는 기화 후 코로나 방전 → <g>기체</g></li>
<li><b>유속</b>: ESI는 미세 액적을 만들어야 해서 유속이 크면 분무가 거칠어짐 → 낮은 유속 / APCI는 가열로 다 기화시키니 <y>2 mL/min</y>까지 OK (일반 HPLC 유속 그대로)</li>
<li><b>다전하·거대분자</b>: 용액 속 단백질엔 H<sup>+</sup>가 여러 개 붙어 있어 ESI로 [M+nH]<sup>n+</sup> 그대로 날아감 / APCI는 기체상에서 H<sup>+</sup> 하나 주고받는 반응이라 1가만 생기고, 거대분자는 기화 자체가 안 됨</li>
<li><b>휘발성</b>: ESI는 기화가 필요 없음 / APCI는 분석물이 기화돼야 하니 필요</li>
<li><b>CAD</b>: 둘 다 이온원 출구에서 충돌 해리 가능</li></ul>
<div class="boxg"><b>선택 가이드</b> 극성·이온성·열에 약함·큰 분자(펩타이드, 단백질, 대사체 포합체) → <b>ESI</b> / 저·중극성·작은 분자(스테로이드, 지용성 약물)·높은 유속 → <b>APCI</b></div>
<p class="note">요즘 장비의 ESI(가열 ESI)는 1 mL/min 가까이도 쓰지만, 시험은 원문 표 값(0.4 vs 2)으로 답해.</p>"""),

# 40
dict(img=40, slide=55, title="분자량·극성에 따른 이온화법 선택", sub="Molecular weight vs polarity: ESI · APCI · APPI",
kw=["ESI: 극성·고분자량", "APCI: 중간 극성", "APPI: 비극성", "적용 범위 지도"],
sum="가로축 극성, 세로축 분자량으로 그린 이온화법 적용 지도. ESI는 극성 + 분자량 100,000까지, APCI는 중간 극성의 작은 분자, APPI는 가장 비극성 쪽을 담당한다.",
tr="""<p>그림: 가로축 <b>극성(Polarity)</b>: 비극성(Nonpolar) → 매우 극성(Very Polar) / 세로축 <b>분자량(Molecular Weight)</b>: 10 – 100,000 (로그 눈금)</p>
<ul><li><b>Electrospray Ionization (ESI)</b>: 중간~매우 극성, 분자량 약 100 – 100,000</li>
<li><b>APCI</b>: 비극성~극성 중간 영역, 분자량 약 10 – 1,000대</li>
<li><b>APPI</b>: 가장 비극성 쪽, 분자량 약 100 – 1,000대</li></ul>""",
ex="""<p>앞 표(54번)를 그림 한 장으로 정리한 거야. 시료가 지도 어디에 있느냐로 이온화법을 골라.</p>
<table class="t"><tr><th>이온화법</th><th>잘하는 영역</th><th>예</th></tr>
<tr><td><b>ESI</b> (파랑)</td><td><y>극성 + 작은~매우 큰 분자</y></td><td>펩타이드, 단백질, 핵산, 대부분의 염기성 약물</td></tr>
<tr><td><b>APCI</b> (초록)</td><td>중간 극성, 분자량 ~1,500 이하</td><td>스테로이드, 지용성 비타민, 농약</td></tr>
<tr><td><b>APPI</b> (분홍)</td><td><y>가장 비극성</y></td><td>다환방향족탄화수소(PAH), 지질 일부</td></tr></table>
<p><b>왜 이런 모양?</b></p>
<ul><li>ESI: 용액에서 이미 이온(H<sup>+</sup>가 붙은 상태)이어야 유리 → 극성 쪽. 다전하가 가능해 분자량 상한이 매우 높음.</li>
<li>APCI·APPI: 기화가 필요 → 분자량 상한이 낮음. APPI는 빛(광자)으로 전자를 직접 떼어내서 양성자를 잘 못 받는 <pk>비극성 물질도 이온화</pk> 가능.</li></ul>
<p>영역이 겹치는 곳(중간 극성, 분자량 수백)은 어느 것을 써도 되고, 실제로는 두 가지를 다 시험해 감도가 좋은 쪽을 골라.</p>
<p class="note">원본에 제목이 없는 슬라이드야(Agilent 자료 그림).</p>"""),

# 41
dict(img=41, slide=56, title="LC-UV vs LC-MS — 총이온 크로마토그램(TIC)", sub="River water spiked with herbicides (1–6) at ~1 ppb",
kw=["LC-UV (240 nm)", "TIC", "풀 스캔 질량 스펙트럼", "3차원 데이터", "~1 ppb"],
sum="UV 검출은 시간마다 흡광도 숫자 하나뿐이지만, LC-MS는 시간마다 전체 질량 스펙트럼을 얻는다. 그 스펙트럼의 모든 이온 세기를 더해 시간에 대해 그린 게 TIC.",
tr="""<p><b>제초제(1–6)를 ~1 ppb로 첨가한 강물</b></p>
<ul><li><b>LC-UV</b>: 자외선 검출 (240 nm 흡광도 vs 시간) — 표: 시간 1분 → 3, 2분 → 25, 3분 → 15 … 30분 → 51</li>
<li><b>LC-MS</b>: <b>TIC (총이온 크로마토그램)</b>, 재구성된 총이온 크로마토그램 — 삽입: 질량 스펙트럼</li>
<li>표: 시간(분)별 세기(이온 전류) — m/z 50, 51, 52, 53, 54, 55 … 499, 500, <b>Total</b>. 예: 1분 → 1, 3, 2, 4, 5, 1, …, 4, 10, 2, 합계 32 / 2분 → 합계 44 … (<b>풀 스캔 질량 스펙트럼</b>)</li></ul>""",
ex="""<p><b>표가 핵심이야</b>. 두 검출기가 만드는 데이터 모양이 달라.</p>
<ul><li><b>UV</b>: (시간, 흡광도) — 시간당 숫자 <b>하나</b> → 2차원</li>
<li><b>MS 풀 스캔</b>: (시간, m/z, 세기) — 시간당 <y>스펙트럼 하나 통째로</y> (m/z 50–500 전부) → 3차원 (다음 슬라이드 그림)</li></ul>
<div class="boxg"><b>정의</b> <b>TIC</b> = 각 시간의 풀 스캔 스펙트럼에서 <b>모든 m/z 세기를 더한 값(Total 열)</b>을 시간에 대해 그린 크로마토그램</div>
<p><b>그림 비교</b>: UV(240 nm)에선 강물의 다른 성분(유기물 등) 때문에 큰 언덕 같은 바탕선이 생겨 1–6 피크가 묻혀. TIC도 배경이 있지만, 각 피크 시점의 <pk>질량 스펙트럼으로 “이게 어떤 화합물인지” 확인</pk>할 수 있어(삽입 그림).</p>
<p>~1 ppb = 1 μg/L 수준의 미량. TIC는 모든 이온을 더하니까 배경 이온까지 다 합쳐져서 감도가 아주 좋진 않아 → 특정 이온만 보는 <g>SIM / EIC</g>로 개선 (58–59번).</p>
<p class="note">“재구성된(reconstructed)” TIC = 저장된 스펙트럼들을 컴퓨터가 합산해 다시 그린 것이라는 뜻.</p>"""),

# 42
dict(img=42, slide=57, title="LC-MS 데이터의 3차원 구조", sub="Chromatogram × mass spectra",
kw=["머무름 시간 축", "m/z 축", "세기 축", "분리된 피크의 스펙트럼"],
sum="LC-MS 데이터는 머무름 시간 × m/z × 세기의 3차원. 시간 방향으로 자르면 크로마토그램, m/z 방향으로 자르면 그 시점의 질량 스펙트럼이 된다.",
tr="""<p>그림: 3차원 LC-MS 데이터</p>
<ul><li>세로축: <b>세기(Intensity)</b></li>
<li>앞쪽 축: <b>머무름 시간(Retention time)</b> t1, t2, t3, t4 — 분리를 위한 액체 크로마토그래피</li>
<li>오른쪽 축: <b>m/z</b> 질량 대 전하비 — 질량 분석을 위한 질량분석법</li>
<li>뒤쪽 벽: <b>크로마토그램(Chromatogram)</b> / 각 피크 시점마다: <b>분리된 피크의 질량 스펙트럼</b>(Mass spectra of resolved peaks)</li></ul>""",
ex="""<p>앞 슬라이드의 표를 그림으로 그린 버전이야. 데이터 “덩어리”를 어느 방향으로 보느냐에 따라 이름이 달라져.</p>
<table class="t"><tr><th>보는 방향</th><th>얻는 것</th></tr>
<tr><td>모든 m/z를 합쳐 시간 축으로</td><td><g>TIC</g> (뒤쪽 벽의 크로마토그램)</td></tr>
<tr><td>한 시간 t에서 m/z 축으로 자르기</td><td>그 피크의 <g>질량 스펙트럼</g> (색깔별 선)</td></tr>
<tr><td>한 m/z만 골라 시간 축으로</td><td><g>EIC/XIC</g> (59번)</td></tr></table>
<p><b>그림 해석</b>: t1–t4에 각각 크로마토그래피 피크가 있고, 그 시점에서 m/z 방향으로 펼친 스펙트럼(분홍·초록·파랑·노랑)이 서로 달라 → <y>LC가 시간으로 1차 분리, MS가 질량으로 2차 분리</y>하는 2차원 분리 기술이라 강력한 거야.</p>
<div class="box"><span class="tag">포인트</span>크로마토그래피에서 두 성분이 같은 시간에 겹쳐 나와도(co-elution), m/z가 다르면 MS로 구별 가능 → UV로는 불가능한 일.</div>
<p class="note">원본에 제목이 없는 슬라이드야.</p>"""),

# 43
dict(img=43, slide=58, title="선택 이온 모니터링(SIM)", sub="Selected ion monitoring (SIM) and extracted ion chromatogram (EIC)",
kw=["SIM", "몇 개의 m/z만 측정", "이마자퀸 MH⁺ 312", "감도·선택성 향상"],
sum="SIM은 질량분석기가 처음부터 정해진 몇 개의 m/z만 측정하도록 설정하는 모드. 그 m/z에 시간을 몰아 쓰니 감도가 좋아지고, 다른 이온은 아예 안 보여 크로마토그램이 깨끗해진다.",
tr="""<p><b>SIM: 질량분석기가 몇 개의 m/z 값만 모니터링하도록 설정한다</b></p>
<p>LC-ESI(+)-MS · <b>선택 이온 모니터링 m/z 312</b></p>
<p>구조: 이마자퀸H<sup>+</sup> (ImazaquinH<sup>+</sup>), m/z = 312</p>
<p>표: 시간(분)별 세기(이온 전류, m/z 312) — 1분 → 3, 2분 → 5, 3분 → 25, … 30분 → 12</p>
<p>그림: 선택 이온 전류(m/z = 312) vs 시간(분) — 약 26분에 <b>MH<sup>+</sup></b> 피크(6번 성분) 하나</p>""",
ex="""<p>56번의 같은 강물 시료야. TIC에선 배경에 묻혀 있던 6번 제초제(이마자퀸)가 <y>SIM m/z 312</y>에선 26분에 깔끔한 피크 하나로 나와.</p>
<p><b>표 비교</b>: TIC 표는 m/z 50–500 전부 + Total 열이었지? SIM 표는 <g>m/z 312 열 하나뿐</g>. 아예 그것만 측정한 거야.</p>
<div class="box"><b>왜 감도가 좋아져?</b> 사중극자는 한순간에 한 m/z만 통과시켜. 풀 스캔(50–500)이면 m/z 312를 보는 시간은 전체의 ~1/450에 불과해. SIM이면 그 시간을 전부 312에 써서 <b>신호를 훨씬 많이 모음</b>(dwell time↑) → S/N↑ → 검출한계↓.</div>
<p><b>선택성</b>: 312가 아닌 이온(배경, 다른 성분)은 기록 자체가 안 돼 → 크로마토그램이 깨끗.</p>
<p><b>단점</b>: 정한 m/z 외 정보는 <pk>버려짐</pk> → 나중에 다른 물질을 찾고 싶어도 데이터가 없어. 또 같은 m/z 312를 갖는 다른 물질(간섭)은 구별 못 해 → SRM으로 해결(65번).</p>
<p class="note">이마자퀸 MH<sup>+</sup> 312 → M = 311 (홀수) → N 홀수 개(실제 3개) ✓ 질소 규칙.</p>"""),

# 44
dict(img=44, slide=59, title="추출 이온 크로마토그램(EIC/XIC) vs SIM", sub="Selected ion monitoring (SIM) and extracted ion chromatogram (EIC)",
kw=["TIC", "EIC = XIC", "풀 스캔 데이터에서 추출", "티아벤다졸 m/z 202.0433"],
sum="EIC는 이미 측정한 풀 스캔 데이터에서 원하는 m/z만 ‘뽑아서’ 그린 크로마토그램(측정 후 데이터 처리). SIM은 측정할 때부터 그 m/z만 재는 ‘측정 모드’. 둘을 구별하는 게 핵심!",
tr="""<p>(a) <b>총이온 크로마토그램(TIC)</b>: 이온 전류 vs 시간(분) — 피크가 매우 많음</p>
<p>표: 시간(분)별 세기 — m/z 50 … <b>202</b> … 500, Total (<b>풀 스캔 질량 스펙트럼</b>, 202 열을 강조)</p>
<p>(b) <b>추출 이온 크로마토그램(EIC 또는 XIC)</b>: 약 9분에 피크 하나 — 구조: <b>티아벤다졸</b>, MH<sup>+</sup> = C<sub>10</sub>H<sub>8</sub>N<sub>3</sub>S, m/z = 202.043 34 / 삽입 스펙트럼: 측정 m/z 202.043 1</p>""",
ex="""<p><span class="tag">시험 포인트</span>SIM과 EIC는 결과 그림이 비슷하게 생겨서 헷갈려. <b>“언제 고르나”</b>가 차이야.</p>
<table class="t"><tr><th></th><th>SIM</th><th>EIC (XIC)</th></tr>
<tr><td>정체</td><td><y>측정 모드</y> (장비 설정)</td><td><y>데이터 처리</y> (측정 후 소프트웨어)</td></tr>
<tr><td>측정 데이터</td><td>지정 m/z만 저장</td><td>풀 스캔 전체 저장 → 그중 한 열만 꺼냄</td></tr>
<tr><td>감도</td><td>높음 (시간 집중)</td><td>풀 스캔과 같음</td></tr>
<tr><td>나중에 다른 물질 찾기</td><td>불가</td><td><g>가능</g> (데이터가 다 있음)</td></tr></table>
<p><b>그림 해석</b>: (a) TIC는 피크가 너무 많아 티아벤다졸이 어디 있는지 모름. (b) 같은 데이터에서 m/z 202.0433만 꺼내니 9분에 피크 하나 → <g>표에서 202 열만 읽어 그린 것</g>.</p>
<p><b>고분해능이면 더 좋아</b>: 측정값 202.0431 vs 이론값 202.04334 → 오차 0.0002 (약 1 ppm). EIC 창을 202.04 ± 0.005처럼 아주 좁게 잡으면 명목질량이 같은 다른 이온은 걸러져 → 선택성↑ (TOF·Orbitrap 같은 HRMS의 장점).</p>
<p class="note">질소 규칙: MH<sup>+</sup> 202(짝수) → N 홀수(3개) ✓. EIC = Extracted Ion Chromatogram, XIC = eXtracted Ion Chromatogram, 같은 말.</p>"""),

# 45
dict(img=45, slide=60, title="탠덤 질량분석법 (MS/MS) — 삼중 사중극자", sub="Tandem mass spectrometry (MS/MS or MSⁿ)",
kw=["Q1 – q2 – Q3", "전구 이온 선택", "충돌 셀(CAD)", "공간 탠덤 vs 시간 탠덤"],
sum="삼중 사중극자 = Q1(전구 이온 고르기) → q2(N₂/Ar와 충돌시켜 깨기) → Q3(조각 이온 고르기). 질량분석기 둘을 공간적으로 이어 붙인 ‘공간 탠덤’이다.",
tr="""<p><b>삼중 사중극자 질량분석기 (Triple quadrupole mass spectrometer)</b></p>
<p>시료 → 이온원 → <b>Q1</b>: 전구 이온 선택용 사중극자 (비공명 이온 제거, 공명 이온만 통과) → <b>Q2</b>: 이온을 조각내는 충돌 셀 (중성 분자와의 충돌) → <b>Q3</b>: 조각 이온 선택용 사중극자 (비공명 조각 이온 제거, 공명 조각 이온만) → 이온 검출기</p>
<p>그림(중): 충돌 기체(N<sub>2</sub> 또는 Ar) 유입 → <b>CAD</b>. 크로마토그래피 컬럼에서 온 이온 혼합물 → Q1 사중극자 질량 분리기 → 전구 이온(부모 이온) → Q2 충돌 셀 → 생성 이온(딸 이온) → Q3 → 모니터링할 선택 이온 → 검출기</p>
<p>그림(하): 옥타폴 이온 가이드 · 사중극자 질량 필터 Q1 · 입구 렌즈 · Q2 육중극자(hexapole) 충돌 셀 · 출구 렌즈 · Q3 · 검출기</p>
<p>Q2에서의 과정을 충돌 활성화 해리라 한다. <b>CAD (충돌 활성화 해리) = CID (충돌 유도 해리)</b></p>
<p><b>공간 탠덤</b> (Tandem in space) cf. <b>시간 탠덤</b> (Tandem in time)</p>""",
ex="""<p>37번의 인소스 CID 문제(“모든 이온이 같이 깨져서 누구 조각인지 모름”)를 해결한 장비야.</p>
<ol><li><b>Q1</b>: 전구 이온 하나만 통과 (예: 니페디핀 [M+H]<sup>+</sup> 347) — <y>1차 질량 선택</y></li>
<li><b>q2</b>: RF only(질량 선택 안 함) + 충돌 기체 → 347만 깨져서 315 등 생성</li>
<li><b>Q3</b>: 조각 이온 고르기(315) 또는 스캔 — <y>2차 질량 선택</y></li></ol>
<p>그래서 MS를 두 번 = <g>MS/MS</g>. 이온트랩처럼 반복하면 MS<sup>n</sup>.</p>
<p><b>자전거 그림</b> = 두 사람이 한 줄로 앉아 타는 “탠덤 자전거”. 질량분석기 두 개를 한 줄로 이었다는 비유야.</p>
<table class="t"><tr><th>공간 탠덤 (in space)</th><th>시간 탠덤 (in time)</th></tr>
<tr><td>서로 다른 장소의 분석기를 차례로 통과 (QqQ, Q-TOF)</td><td>한 장소(이온트랩)에서 가두기 → 고르기 → 깨기 → 스캔을 <b>시간 순서로</b> 반복</td></tr></table>
<p class="note">충돌 셀은 사중극자가 아니라 육중극자·팔중극자일 수도 있어서 소문자 q2로 쓰기도 해. 충돌 기체는 N<sub>2</sub>나 Ar(무겁고 반응 안 하는 기체).</p>"""),

# 46
dict(img=46, slide=61, title="삼중 사중극자 LC-MS 시스템 (실제 장비)", sub="Agilent 6460 triple quadrupole (QQQ) LC-MS system",
kw=["QQQ", "HPLC + MS/MS", "Q1 · Q2 · Q3", "정량 표준 장비"],
sum="실제 LC-MS/MS 장비 구성: 왼쪽 HPLC(펌프·오토샘플러·컬럼) + 오른쪽 삼중 사중극자 질량분석기 + 제어 컴퓨터. 혈중 약물 정량 등에서 가장 많이 쓰는 표준 장비다.",
tr="""<p>그림(위): 시료 → 이온원 → <b>Q1</b> 전구 이온 선택용 사중극자 (공명 이온) → <b>Q2</b> 이온 조각화용 충돌 셀 (중성 분자와 충돌) → <b>Q3</b> 조각 이온 선택용 사중극자 (공명 조각 이온) → 이온 검출기. 비공명 이온·비공명 조각 이온은 제거됨</p>
<p>사진: <b>HPLC</b> + <b>삼중 사중극자 질량분석기</b> (+ 컴퓨터)</p>
<p><b>Agilent 6460 삼중 사중극자(QQQ) LC-MS 시스템</b></p>""",
ex="""<p>앞 슬라이드의 원리가 실제로는 이렇게 생겼어.</p>
<ul><li><b>HPLC 쪽</b>: 이동상 병 · 펌프 · 오토샘플러 · 컬럼 오븐 → 분리</li>
<li><b>MS 쪽</b>: 앞면에 ESI/APCI 이온원 → 내부에 Q1–q2–Q3 → 뒤쪽 진공 펌프</li>
<li><b>컴퓨터</b>: 측정 조건(전구/조각 이온, 충돌 에너지) 설정, 데이터 처리</li></ul>
<p><b>QQQ가 정량 표준인 이유</b></p>
<ul><li><y>SRM(MRM) 모드</y>로 선택성·감도가 매우 높음(65번) → pg/mL(ppt) 수준</li>
<li>사중극자라 튼튼하고, 정량 범위(직선성)가 넓고, 재현성이 좋아</li>
<li>약동학·생물학적 동등성 시험, 도핑, 잔류농약, 환경 분석에 표준으로 쓰여</li></ul>
<div class="box"><span class="tag">비교</span>QQQ = 단위 분해능 → <b>정량</b> 최강 / Q-TOF·Orbitrap = 고분해능 → <b>정성(미지물질 동정)</b> 최강. 26번 시장 설명의 “Quadrupole LC/MS 매출 24%”가 이 장비 계열이야.</div>
<p class="note">원본 62–63번 슬라이드는 빠져 있어.</p>"""),

# 47
dict(img=47, slide=64, title="삼중 사중극자의 스캔 모드", sub="Triple quadrupole scan modes",
kw=["Full scan", "SIM", "Product ion scan", "SRM", "Precursor ion scan", "Neutral loss scan"],
sum="Q1·Q3를 ‘스캔/SIM/RF only’, q2를 ‘충돌 기체 on/off’로 조합해 여러 모드를 만든다. 정량은 SRM(SIM–on–SIM), 구조 확인은 생성 이온 스캔(SIM–on–Scan).",
tr="""<ul><li>Q1 &amp; Q3: RF only (질량 필터링 없음), 스캔 또는 SIM</li><li>Q2: 충돌 기체 켬 또는 끔</li><li>⇒ 3(Q1) × 2(Q2) × 3(Q3) = 18가지 모드?</li></ul>
<table class="t"><tr><th>스캔 모드</th><th>Q1</th><th>Q2</th><th>Q3</th></tr>
<tr><td>풀 스캔 (Full scan)</td><td>Scan</td><td>Off</td><td>RF only</td></tr>
<tr><td>선택 이온 모니터링 (SIM)</td><td>SIM</td><td>Off</td><td>RF only</td></tr>
<tr><td>생성 이온 스캔 (Product ion scan)</td><td>SIM</td><td>On</td><td>Scan</td></tr>
<tr><td>선택 반응 모니터링 (SRM)</td><td>SIM</td><td>On</td><td>SIM</td></tr>
<tr><td>전구 이온 스캔 (Precursor ion scan)</td><td>Scan</td><td>On</td><td>SIM</td></tr>
<tr><td>중성 손실 스캔 (Neutral loss scan)</td><td>Scan</td><td>On</td><td>Scan</td></tr></table>
<p class="note">그림: 이온원 – Q1 – Q2(충돌 유도 해리 영역) – Q3 – 검출기. 모드별 이온 경로(Full Scan MS, SIM, MS/MS Product Ion Mode, MS/MS SRM, CID gas). “삼중 사중극자 장비는 다양한 방식으로 쓰일 수 있으며, 처음 두 실험은 사실상 삼중 사중극자를 단일 사중극자 모드로 쓰는 것이다.”</p>""",
ex="""<p><b>18가지?</b> 이론상 조합은 18개지만 의미 있는 건 표의 <y>6개</y>야. 나머지는 쓸모없거나 중복(예: 충돌 기체 off인데 Q3 스캔 → 그냥 풀 스캔).</p>
<table class="t"><tr><th>모드</th><th>질문</th><th>쓰임</th></tr>
<tr><td>Full scan</td><td>뭐가 들어 있지?</td><td>미지 성분 탐색</td></tr>
<tr><td>SIM</td><td>이 m/z가 얼마나?</td><td>단일 MS 정량</td></tr>
<tr><td><b>Product ion</b></td><td>이 전구 이온은 뭘로 깨지지?</td><td><g>구조 확인</g>, SRM 전이 찾기</td></tr>
<tr><td><b>SRM</b></td><td>이 전구→이 조각이 얼마나?</td><td><g>정량 끝판왕</g></td></tr>
<tr><td>Precursor ion</td><td>이 조각을 내는 부모는 누구?</td><td>같은 골격(계열) 화합물 찾기</td></tr>
<tr><td>Neutral loss</td><td>이 중성 조각을 잃는 이온은?</td><td>같은 작용기 가진 화합물 찾기</td></tr></table>
<p><b>헷갈리는 두 개</b>: 전구 이온 스캔은 Q3를 특정 조각(예: m/z 184, 포스파티딜콜린 머리)에 고정하고 Q1을 훑어 → “184를 내는 모든 부모”. 중성 손실 스캔은 Q1·Q3를 <b>일정한 질량차</b>(예: 80, 황산 포합체의 SO<sub>3</sub>)를 유지하며 함께 훑어 → “80을 잃는 모든 이온”.</p>
<div class="box"><span class="tag">시험 포인트</span>표에서 Q2가 <b>Off</b>면 MS/MS가 아님(단일 MS 모드). <b>SRM = SIM–On–SIM</b>, <b>Product = SIM–On–Scan</b>.</div>"""),

# 48
dict(img=48, slide=65, title="선택 반응 모니터링(SRM) / 다중 반응 모니터링(MRM)", sub="SRM or MRM (One of the most powerful quantitative analytical methods currently available)",
kw=["Q1 전구 이온 선택", "q2 조각화", "Q3 조각 이온 선택", "간섭 제거", "S/N 비"],
sum="SRM은 ‘전구 이온 m/z’와 ‘조각 이온 m/z’를 둘 다 맞아야 통과시키는 이중 필터. 같은 m/z의 간섭 이온은 대부분 다른 조각을 내므로 걸러져 노이즈가 크게 줄고 S/N이 높아진다.",
tr="""<p><b>SRM 또는 MRM — 현재 가능한 가장 강력한 정량 분석법 중 하나</b></p>
<p>MRM/SRM: 삼중 사중극자 질량분석기 → <b>Q1 전구 이온 선택</b> → <b>q2 조각화</b> → <b>Q3 조각 이온 선택</b> → 검출 (조각 1, 2, 3)</p>
<p>그림: 목표 화합물(Target compound)과 간섭 이온(interference ion) — <b>SIM 크로마토그램</b>(간섭이 겹친 넓은 신호 위 작은 피크) vs <b>MRM 크로마토그램</b>(목표 화합물 피크만)</p>
<p>SIM (m/z 154): 7.70분 근처 피크 + 옆에 간섭 피크 / <b>SRM/MRM</b>: 154 → 152, 154 → 102 (깨끗한 단일 피크)</p>
<p><b>신호 대 잡음비 (S/N ratio, SNR) = Signal/Noise</b></p>""",
ex="""<p><span class="tag">족보</span><b>“SIM보다 SRM의 signal-to-noise가 큰 이유?”</b> — 기말 주관식 그대로야. 답안 틀을 만들어 두자.</p>
<div class="box"><b>모범 답안</b><br>① SIM은 Q1에서 <b>전구 이온의 m/z 하나만</b> 보기 때문에, 같은(또는 비슷한) m/z를 가진 매트릭스 유래 간섭 이온·화학적 배경 이온도 함께 검출된다 → 노이즈(배경)가 크다.<br>② SRM은 Q1에서 전구 이온을 고르고, q2에서 충돌 해리시킨 뒤, Q3에서 <b>그 화합물에 특이적인 조각 이온</b>만 한 번 더 고른다(<b>이중 질량 선택</b>).<br>③ 간섭 이온은 전구 m/z가 같더라도 <b>같은 조각 이온을 낼 확률이 매우 낮아</b> Q3에서 제거된다 → 배경 노이즈가 크게 감소.<br>④ 신호는 약간 줄어도 노이즈가 훨씬 더 많이 줄어 <b>S/N이 증가</b> → 선택성·검출한계 향상.</div>
<p><b>그림 해석</b>: 회색 넓은 언덕 = 간섭 이온(SIM에선 목표 피크가 그 위에 얹혀 구별 어려움). MRM 크로마토그램(파랑)은 목표 화합물만 뾰족하게.</p>
<p><b>SRM vs MRM</b>: 전이(precursor→product) 하나만 보면 SRM, 여러 전이(여러 화합물, 또는 한 화합물의 정량·확인용 2개)를 번갈아 보면 MRM. 예: 154→152(정량), 154→102(확인).</p>
<p class="note">S/N = 피크 높이 ÷ 바탕선 잡음 폭. 보통 S/N ≥ 3이 검출한계, ≥ 10이 정량한계 기준.</p>"""),

# 49
dict(img=49, slide=66, title="SRM 실제 예 — 에티닐에스트라디올(EE₂) ppt 정량", sub="SRM: 17α-ethinylestradiol in water",
kw=["EE₂ [M−H]⁻ 295", "조각 159·145", "SRM 295 → 159 + 145", "3.6 ng/L (ppt)"],
sum="경구피임약 성분 EE₂를 음이온 [M−H]⁻ 295로 Q1에서 고르고, 생성 이온 스펙트럼에서 고른 특이 조각 159·145만 Q3로 보면 3.6 ng/L(ppt) 수준까지 검출된다.",
tr="""<p>Q1: SIM ⇓ Q2: 기체 켬 ⇓ Q3: SIM</p>
<p><b>생성 이온 스펙트럼</b>: 17α-에티닐에스트라디올(EE<sub>2</sub>) (경구 피임약) — [M−H]<sup>−</sup> 295.2, 조각: 269.2, 247.0, 225.1, 213.1, 199.1, 183.0, 170.9, <b>159.0</b>, <b>145.0</b>(기준 피크)</p>
<p><b>SRM 크로마토그램</b> (m/z 295 → 159 + 145) — Q1: SIM (m/z 295), Q3: SIM (m/z 159 &amp; 145). EE<sub>2</sub> 3.6 ng/L (ppt) 피크 (약 21분)</p>
<p>표: 시간별 세기 — 145, 159 열과 Total만 (나머지 m/z는 비어 있음)</p>
<p class="note">세로축: Q3에서 나온 m/z = 159 + 145 신호</p>""",
ex="""<p><b>SRM 방법 만드는 순서</b> (실무 그대로)</p>
<ol><li><b>전구 이온 정하기</b>: EE<sub>2</sub>(C<sub>20</sub>H<sub>24</sub>O<sub>2</sub>, M 296)는 페놀 OH가 있어 음이온 모드 → <g>[M−H]<sup>−</sup> 295</g></li>
<li><b>생성 이온 스캔</b>(Q1 SIM 295 – q2 On – Q3 Scan)으로 조각 확인 → 가장 센 <y>145, 159</y> 선택</li>
<li><b>SRM 설정</b>: Q1 = 295 고정, Q3 = 145와 159 고정 → 두 전이 신호를 더해서 크로마토그램</li></ol>
<p><b>표의 의미</b>: 풀 스캔 표는 모든 m/z 칸이 있었지만, SRM 표는 <g>145, 159 칸만</g> 있어. 그 둘만 측정했다는 뜻.</p>
<p><b>그림 해석</b>: 15분 근처의 큰 피크는 다른 물질(같은 전이를 일부 내는 간섭 or 다른 성분), 21분이 EE<sub>2</sub>. 바탕선이 깨끗해서 <pk>3.6 ng/L = 3.6 ppt</pk>도 S/N 충분히 확인 가능.</p>
<div class="box"><span class="tag">스케일 감각</span>1 ppb = 1 μg/L, 1 ppt = 1 ng/L. 3.6 ng/L는 수영장(2,500 m³)에 약 9 mg 녹인 농도 수준! 환경수 중 호르몬 분석에 SRM이 필수인 이유.</div>
<p class="note">질소 규칙: N 0개, [M−H]<sup>−</sup> 295 (짝전자, 홀수) ✓.</p>"""),

# 50
dict(img=50, slide=67, title="사중극자-비행시간형(Q-TOF) LC/MS 시스템", sub="Quadrupole Time-of-Flight (Q-TOF) LC/MS system",
kw=["Q1 + 충돌 셀 + TOF", "직교 가속", "고분해능 MS/MS", "정밀질량 조각"],
sum="Q-TOF = 삼중 사중극자의 Q3 자리에 TOF를 단 하이브리드. Q1로 전구 이온을 고르고 충돌 셀에서 깬 뒤, 조각 이온 전체를 TOF로 고분해능·정밀질량 측정한다.",
tr="""<p><b>사중극자 비행시간형 (Q-TOF) LC/MS 시스템</b></p>
<p>그림(위): 사진 — LC + Q-TOF 장비(세로로 긴 비행관). 도식 — 이온원 → 옥타폴 1 → 사중극자 질량 필터(Q1) → 옥타폴 2 · 충돌 셀 → DC 사중극자 → 이온 펄서 → 이온 미러(리플렉트론) → 검출기. 펌프: 로터리 펌프 · 3단 터보 펌프 · 터보 2</p>
<p>그림(아래): (b) <b>Q-TOF-MS/MS 동정</b> — 이온원 ESI(+/−) → Q1 전구 이온 → Q2 생성 이온 → 추출기 → TOF (v = √(2zeV<sub>s</sub>/m)) → 리플렉트론 → 검출기</p>""",
ex="""<p><b>하이브리드의 아이디어</b>: 사중극자(고르기 잘함) + TOF(고분해능·빠름)를 합침.</p>
<table class="t"><tr><th></th><th>QQQ</th><th>Q-TOF</th></tr>
<tr><td>마지막 분석기</td><td>Q3 (사중극자)</td><td><y>TOF</y></td></tr>
<tr><td>분해능</td><td>단위</td><td>고분해능 (정밀질량)</td></tr>
<tr><td>조각 이온 측정</td><td>스캔 or SIM</td><td>모든 조각을 한 번에</td></tr>
<tr><td>강점</td><td>정량(SRM)</td><td><g>미지물질 구조 동정</g></td></tr></table>
<p><b>구조 읽기</b>: 이온이 Q1을 수평으로 지나 충돌 셀을 거친 뒤, <b>이온 펄서</b>가 수직 방향으로 펄스를 줘서 TOF로 쏘아 올려(직교 가속, orthogonal acceleration). 위쪽 이온 미러(리플렉트론)에서 반사돼 내려와 검출기에 도착. 그래서 사진의 장비가 세로로 긴 탑 모양이야.</p>
<p><b>쓰임</b>: 대사체 구조 확인, 불순물·분해산물 동정, 미지 화합물 스크리닝 — 전구 이온과 조각 이온 모두 정밀질량이라 <pk>조각의 분자식까지</pk> 계산 가능.</p>
<p class="note">Q1을 RF only로 두면 그냥 고분해능 TOF-MS(풀 스캔)로도 쓸 수 있어.</p>"""),

# 51
dict(img=51, slide=68, title="사중극자-오비트랩(Q-Orbitrap) 질량분석기", sub="Quadrupole-Orbitrap mass spectrometer",
kw=["Q Exactive HF", "Orbitrap", "HCD 충돌 셀", "초고분해능", "고진공"],
sum="Q-Orbitrap = 사중극자(전구 이온 선택) + 충돌 셀(HCD) + Orbitrap(초고분해능 분석기). Orbitrap은 이온이 중심 전극 주위를 돌며 진동하는 주파수로 m/z를 재서 분해능이 매우 높다.",
tr="""<p><b>Thermo Scientific™ Q Exactive™ HF 하이브리드 사중극자-Orbitrap 질량분석기</b></p>
<p>그림: 이온원(Ion source) → RF 렌즈 → 첨단 활성 빔 가이드(AABG) → <b>사중극자</b> (첨단 사중극자 기술(AQT)을 적용한 사중극자 질량 필터) → <b>Orbitrap</b> (초고자장(HF) Orbitrap 질량분석관) / <b>충돌 셀</b> (HCD 셀)</p>""",
ex="""<p><b>Orbitrap 원리 (간단히)</b>: 방추형 중심 전극과 바깥 전극 사이에 이온을 가두면 이온이 중심축을 빙빙 돌면서 <y>축 방향으로 앞뒤로 진동</y>해. 이 진동 주파수가 <g>√(z/m)에 비례</g>해서, 전극에 유도되는 신호를 푸리에 변환(FT)하면 m/z별 주파수 → 스펙트럼. (NMR에서 FT 배운 것과 같은 아이디어!)</p>
<p><b>특징</b></p>
<ul><li>분해능이 매우 높아(수십만 수준) → 정밀질량, 동위원소 미세구조까지 구별</li>
<li>이온이 오래 진동해야 해서 <pk>가장 높은 진공 필요</pk> (47번 표: ~10<sup>−10</sup> torr)</li>
<li>측정 시간을 길게 할수록 분해능↑, 대신 스캔 속도↓ (TOF와의 트레이드오프)</li></ul>
<p><b>HCD 셀</b>(Higher-energy Collisional Dissociation): 충돌 셀에서 깬 조각을 다시 Orbitrap으로 보내 고분해능 MS/MS.</p>
<table class="t"><tr><th>고분해능 하이브리드</th><th>마지막 분석기 원리</th></tr>
<tr><td>Q-TOF</td><td>비행 시간 (t ∝ √(m/z))</td></tr>
<tr><td>Q-Orbitrap</td><td>진동 주파수 (f ∝ √(z/m)) + FT</td></tr></table>
<p class="note">그림의 C-trap(충돌 셀 앞에서 이온을 모아 Orbitrap에 주입하는 곡선형 트랩)은 라벨엔 없지만 실제 장비의 핵심 부품이야.</p>"""),

# 52
dict(img=52, slide=69, title="사중극자-선형 이온트랩(Q-Trap) 질량분석기", sub="Quadrupole-Linear ion trap (Q-Trap) mass spectrometer",
kw=["Q0 이온 가이드", "Q1 사중극자", "Q2 곡선형 충돌 셀", "Q3 선형 트랩", "MRM + 트랩 스캔"],
sum="QTRAP은 삼중 사중극자와 같은 구조인데 Q3가 일반 사중극자로도, 이온을 모아 두는 선형 이온트랩으로도 작동한다. MRM 정량과 고감도 MS/MS(구조 확인)를 한 장비로 한다.",
tr="""<p><b>사중극자-선형 이온트랩 (Q-Trap) 질량분석기</b></p>
<p>그림: 이온 가이드(Ion guide) → <b>충돌 집속 및 이온 포집 (Q<sub>0</sub>)</b> → <b>사중극자 (Q<sub>1</sub>)</b> → <b>곡선형 충돌 셀 (Q<sub>2</sub>)</b> → <b>선형 트랩 (Q<sub>3</sub>)</b></p>""",
ex="""<p><b>구조</b>: 기본 뼈대는 삼중 사중극자(Q1–q2–Q3)와 같아. 다른 점은 <y>Q3가 “두 가지 모드”</y>로 작동한다는 것.</p>
<table class="t"><tr><th>Q3 모드</th><th>동작</th><th>쓰임</th></tr>
<tr><td>일반 사중극자</td><td>m/z 필터 (투과형)</td><td><g>SRM/MRM 정량</g> (QQQ와 동일)</td></tr>
<tr><td>선형 이온트랩</td><td>이온을 가뒀다가 m/z 순서로 내보내 스캔</td><td>고감도 생성 이온 스캔 (구조 확인)</td></tr></table>
<p><b>왜 트랩이 감도에 좋아?</b> 투과형 사중극자 스캔은 한순간에 한 m/z만 통과시키고 나머지는 버려. 트랩은 <y>이온을 일단 모아 두었다가</y> 순서대로 꺼내니까 버리는 이온이 적어 → 풀 스캔 감도↑. 45번에서 말한 “시간 탠덤(tandem in time)”의 개념도 여기 들어 있어.</p>
<p><b>부품</b>: Q0 = 이온원에서 들어온 이온을 기체 충돌로 식혀 모아 줌(collisional focusing). Q2 = 곡선형 충돌 셀(장비를 짧게 만들고, 중성 입자는 곧게 날아가 제거됨).</p>
<div class="boxg"><b>하이브리드 장비 총정리</b> QQQ: 정량 / Q-TOF: 고분해능 정성 / Q-Orbitrap: 초고분해능 정성(+정량) / QTRAP: 정량 + 고감도 MS/MS</div>
<p class="note">이 슬라이드가 Lecture 5의 마지막이야. 시험 직전엔 표지 페이지의 로드맵 표와 각 페이지의 분홍(시험 포인트) 박스만 다시 훑어봐.</p>"""),
]
