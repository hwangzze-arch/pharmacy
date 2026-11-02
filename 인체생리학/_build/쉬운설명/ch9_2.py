PAGES = [
# 16
dict(img=16, slide=16, title="심장의 전기 활동 — 자동능과 두 종류의 세포", sub="Electrical activity of the heart",
kw=["자동능", "수축세포 99%", "자동능 세포", "AP 전달"],
sum="심장은 스스로 AP를 만들어 리듬 있게 뛴다(<b>자동능</b>). 심장근 세포의 <b>99%</b>는 펌프 일을 하는 <b>수축세포</b>(AP를 시작하지 못하고 전달만), 나머지가 AP를 시작·전도하는 <b>자동능 세포</b>(수축하지 않음).",
tr="""<ul><li>심장근 세포의 수축은 세포막을 휩쓰는 AP가 일으킨다.</li>
<li><b>자동능(autorhythmicity, automaticity)</b>: 스스로 만든 AP의 결과로 심장이 리듬 있게 수축하는 것</li>
<li>두 종류의 특수 심장근 세포
<ul><li><b>1) 수축세포(contractile cells)</b>: 심장근 세포의 99%, 펌프질이라는 기계적 일을 한다. AP를 <b>시작하지 않고 전달만</b> 한다.</li>
<li><b>2) 자동능 세포(autorhythmic cells)</b>: 수축세포를 수축시키는 AP를 <b>시작하고 전도</b>한다. <b>수축하지 않는다</b>.</li></ul></li></ul>""",
ex="""<table class="t"><tr><th></th><th>수축세포</th><th>자동능 세포</th></tr>
<tr><td>비율</td><td><b>99%</b></td><td>약 1%</td></tr>
<tr><td>AP 시작</td><td>✗ (전달만)</td><td><b>✔ 스스로</b></td></tr>
<tr><td>수축</td><td><b>✔</b></td><td>✗</td></tr>
<tr><td>휴지막전위</td><td>안정 (−90 mV)</td><td><b>없음</b> (계속 천천히 탈분극)</td></tr>
<tr><td>위치</td><td>심방·심실 벽 대부분</td><td>SA결절, AV결절, 히스다발, 푸르키네 섬유</td></tr></table>
<div class="boxg">골격근과의 차이: 골격근 AP는 <b>운동뉴런</b>(ACh)이 시작한다. 심장은 <g>신경 없이도</g> 뛴다 → 심장 이식으로 신경이 끊겨도 뛴다.</div>
<div class="box"><span class="tag">시험 포인트</span>"자동능 세포는 수축도 한다" → <b>✗</b>. "수축세포가 AP를 시작한다" → <b>✗</b>.</div>"""),
# 17
dict(img=17, slide=17, title="자동능 세포 — 박동조율 전위", sub="Cardiac autorhythmic cells",
kw=["박동조율 활동", "휴지막전위 없음", "느린 탈분극", "역치", "박동조율 전위"],
sum="자동능 세포에는 <b>휴지막전위가 없다</b>. AP와 AP 사이에 막전위가 <b>천천히 역치까지 올라가는데</b>(박동조율 전위), 이 느린 상승 덕분에 신경 없이도 주기적으로 AP가 생긴다.",
tr="""<ul><li>심장 자동능 세포는 <b>박동조율 활동(pacemaker activity)</b>을 보인다.
<ul><li>쉬고 있는 신경·골격근 세포와 달리 <b>휴지막전위가 없다</b>.</li>
<li>AP 사이에 막전위가 역치에 도달할 때까지 <b>천천히 탈분극</b>한다.</li></ul></li>
<li><b>박동조율 전위(pacemaker potential)</b>
<ul><li>자동능 세포 막이 역치 쪽으로 천천히 이동해 주기적으로 AP를 시작하는 것</li>
<li>AP가 퍼져 신경 지배 없이도 리듬 있는 박동을 일으킨다.</li></ul></li>
<li>(그림) 느린 탈분극(박동조율 전위) → 역치 → 스스로 생긴 AP. KEY: I<sub>f</sub> = funny 채널, T = 일시적 T형 Ca²⁺ 채널, L = 오래 열리는 L형 Ca²⁺ 채널</li></ul>""",
ex="""<p>그림을 단계로 읽으면:</p>
<table class="t"><tr><th>구간</th><th>막전위 변화</th><th>주인공</th></tr>
<tr><td>① 느린 탈분극 (전반)</td><td>약 −60 mV에서 천천히 ↑</td><td><y>funny 채널(Na⁺ 유입)</y> + K⁺ 유출 ↓</td></tr>
<tr><td>② 느린 탈분극 (후반)</td><td>역치(약 −40 mV) 직전</td><td><y>T형 Ca²⁺ 채널</y></td></tr>
<tr><td>③ 상승기</td><td>역치 넘어 빠르게 ↑</td><td><y>L형 Ca²⁺ 채널</y> (Na⁺ 아님!)</td></tr>
<tr><td>④ 하강기</td><td>다시 ↓</td><td>K⁺ 채널 열림 (K⁺ 유출)</td></tr></table>
<div class="boxg"><b>박동조율 전위 = 역치까지 천천히 올라가는 탈분극</b>. 기울기가 가파를수록 역치에 빨리 닿아 <g>심박수 ↑</g>.</div>
<div class="box"><span class="tag">시험 포인트</span>"자동능 세포는 −90 mV의 안정된 휴지막전위를 가진다" → <b>✗</b> (그건 수축세포). 그림 각주로 박동조율 전위 구간을 표시하게 할 수 있다.</div>"""),
# 18
dict(img=18, slide=18, title="자동능 세포의 AP (1): 막 시계 — funny 채널과 T형 Ca²⁺", sub="Cardiac autorhythmic cells – action potential",
kw=["Na⁺ 유입 ↑", "K⁺ 유출 ↓", "funny 채널(I_f)", "과분극에 열림", "T형 Ca²⁺ 채널"],
sum="박동조율 전위는 세 가지 이온 흐름이 만든다: <b>Na⁺ 유입 ↑</b>(funny 채널), <b>K⁺ 유출 ↓</b>(K⁺ 채널이 서서히 닫힘), <b>Ca²⁺ 유입 ↑</b>(T형 Ca²⁺ 채널이 마지막에 역치까지 밀어 올림).",
tr="""<ul><li><b>박동조율 전위</b>: Na⁺ 내향 전류 증가 · K⁺ 외향 전류 감소 · Ca²⁺ 내향 전류 증가</li>
<li><b>막 시계(membrane clock) 기전</b></li>
<li>① <b>Funny 채널(I<sub>f</sub> 채널)</b>
<ul><li><b>과분극(더 음성)</b>일 때 열리는 전압개폐 Na⁺ 채널</li><li><b>심장 박동조율 세포에만</b> 있다.</li></ul></li>
<li>① <b>K⁺ 채널의 지연된 닫힘</b>
<ul><li>탈분극 전위에서 열렸던 전압개폐 K⁺ 채널이 과분극 동안 서서히 닫힌다.</li>
<li>K⁺ 유출이 줄어 느린 탈분극을 돕고 막전위를 역치 쪽으로 되돌린다.</li></ul></li>
<li>② <b>일시적(T형) Ca²⁺ 채널 열림</b>
<ul><li>funny 채널이 닫힐 무렵, 역치 도달 전에 열린다.</li><li>짧은 Ca²⁺ 유입이 막전위를 역치까지 올린다.</li><li>그 후 T형 Ca²⁺ 채널은 닫힌다.</li></ul></li></ul>""",
ex="""<table class="t"><tr><th>그림 번호</th><th>채널</th><th>이온 흐름</th><th>결과</th></tr>
<tr><td>①</td><td><b>Funny (I<sub>f</sub>)</b></td><td>Na⁺ 유입 ↑</td><td>느린 탈분극 시작</td></tr>
<tr><td>①</td><td>K⁺ 채널 서서히 닫힘</td><td>K⁺ 유출 ↓</td><td>탈분극 도움</td></tr>
<tr><td>②</td><td><b>T형 Ca²⁺</b> (Transient)</td><td>Ca²⁺ 짧게 유입</td><td><y>역치 도달</y></td></tr>
<tr><td>③</td><td><b>L형 Ca²⁺</b> (Long-lasting)</td><td>Ca²⁺ 크게 유입</td><td>AP 상승기</td></tr>
<tr><td>④</td><td>전압개폐 K⁺</td><td>K⁺ 유출</td><td>재분극</td></tr></table>
<p><b>"Funny"인 이유</b>: 보통 Na⁺ 채널은 <b>탈분극</b>에 열리는데, 이건 반대로 <y>과분극(재분극 끝)에 열려서</y> "이상한(funny)" 채널이라 불렀다.</p>
<div class="boxg">기억법: <g>T = Transient(잠깐, 역치까지)</g>, <g>L = Long-lasting(오래, 상승기)</g>.</div>
<div class="box"><span class="tag">시험 포인트</span>"funny 채널은 탈분극에 열리는 K⁺ 채널" → <b>✗</b> (과분극에 열리는 Na⁺ 채널). 단어 박스 빈칸으로 ①~④ 순서를 묻기 좋다.</div>"""),
# 19
dict(img=19, slide=19, title="자동능 세포의 AP (2): Ca²⁺ 시계 · L형 Ca²⁺ · 재분극", sub="Cardiac autorhythmic cells – action potential",
kw=["Ca²⁺ 시계", "결합 시계", "L형 Ca²⁺ 채널", "K⁺ 유출", "SERCA", "NCX"],
sum="역치를 넘으면 <b>L형 Ca²⁺ 채널</b>이 열려 Na⁺가 아닌 <b>Ca²⁺가 크게 유입</b>되어 상승기를 만들고, 이어 K⁺ 채널이 열려 재분극한다. Ca²⁺는 SERCA·NCX로 치우고, 과분극이 다시 funny 채널을 열어 다음 주기가 시작된다.",
tr="""<ul><li>막 시계 기전을 넘어서
<ul><li>박동조율 활동은 막 전류만으로 움직이지 않는다.</li><li>세포 안 Ca²⁺ 순환(<b>Ca²⁺ 시계</b> 기전)도 기여한다.</li><li>현대의 관점: 두 기전을 통합한 <b>결합 시계(coupled-clock)</b> 시스템</li></ul></li>
<li>자동능 세포에서 박동조율 전위 다음의 AP
<ul><li>③ <b>L형 Ca²⁺ 채널</b>: 역치에 도달하면 AP가 오래 열리는 전압개폐 Ca²⁺ 채널을 연다 → Na⁺가 아니라 <b>Ca²⁺가 크게 유입</b></li>
<li>④ <b>전압개폐 K⁺ 채널</b>: L형 Ca²⁺ 채널이 닫히면서 함께 열려 K⁺ 유출을 일으킨다.</li></ul></li>
<li>AP의 종료와 재순환
<ul><li>Ca²⁺ 제거 기전: 1) <b>SERCA 펌프</b>(세포질 → SR) 2) <b>Na⁺/Ca²⁺ 교환체(NCX)</b>(Ca²⁺ 밖으로 / Na⁺ 안으로)</li>
<li>Na⁺/K⁺ ATPase가 이온 기울기를 되돌린다.</li>
<li>과분극이 I<sub>f</sub> 채널을 활성화 → 다음 주기 시작</li></ul></li></ul>""",
ex="""<div class="boxg"><b>한 바퀴</b>: <g>funny(Na⁺) → T형 Ca²⁺ → 역치 → L형 Ca²⁺ 상승 → K⁺ 재분극 → 과분극 → 다시 funny</g></div>
<table class="t"><tr><th>Ca²⁺ 치우는 장치</th><th>방향</th><th>에너지</th></tr>
<tr><td>SERCA</td><td>세포질 → SR 안</td><td>ATP 직접</td></tr>
<tr><td>NCX (Na⁺/Ca²⁺ 교환체)</td><td>Ca²⁺ 밖으로, Na⁺ 안으로</td><td>Na⁺ 기울기(2차 능동)</td></tr>
<tr><td>Na⁺/K⁺ ATPase</td><td>Na⁺ 밖, K⁺ 안</td><td>ATP — 기울기 복구</td></tr></table>
<p><b>신경 AP와 다른 점</b>: 뉴런 AP 상승기는 <b>Na⁺</b> 유입, 박동조율 세포 상승기는 <y>Ca²⁺(L형)</y> 유입 → 상승이 느리고 완만하다.</p>
<div class="box"><span class="tag">시험 포인트</span>"SA결절 AP의 상승기는 빠른 Na⁺ 유입 때문" → <b>✗</b> (L형 Ca²⁺). 빠른 Na⁺ 상승은 <b>수축세포</b>(슬라이드 25).</div>"""),
# 20
dict(img=20, slide=20, title="심장의 박동조율 세포 (그림): 특수 전도계", sub="Pacemaker cells in the heart",
kw=["SA결절", "심방간 경로", "결절간 경로", "AV결절", "히스다발", "푸르키네 섬유"],
sum="(a) 심장의 특수 전도계: 우심방의 <b>SA결절</b> → 심방간·결절간 경로 → <b>AV결절</b> → <b>히스다발</b>(좌·우 가지) → <b>푸르키네 섬유</b>. (b) 흥분이 퍼지는 순서. 심방과 심실 사이는 전기가 통하지 않는 섬유조직이 막고 있다.",
tr="""<ul><li>(a) 심장의 특수 전도계: 동방결절(SA node), 심방간 경로, 결절간 경로, 방실결절(AV node), 히스다발, 히스다발의 우각·좌각, 푸르키네 섬유</li>
<li>(b) 심장 흥분의 확산: 심방(우·좌) → AV결절 → 히스다발 → 푸르키네 섬유 → 심실</li>
<li>표시: 전기가 통하지 않는 섬유조직(electrically nonconductive fibrous tissue)</li></ul>""",
ex="""<table class="t"><tr><th>#</th><th>구조</th><th>위치</th></tr>
<tr><td>1</td><td><b>SA node 동방결절</b></td><td>우심방 벽, 상대정맥 입구 근처</td></tr>
<tr><td>2</td><td>Interatrial pathway 심방간 경로</td><td>우심방 → 좌심방</td></tr>
<tr><td>3</td><td>Internodal pathway 결절간 경로</td><td>SA결절 → AV결절</td></tr>
<tr><td>4</td><td><b>AV node 방실결절</b></td><td>우심방 바닥, 중격 근처</td></tr>
<tr><td>5</td><td><b>Bundle of His 히스다발</b> (좌·우 가지)</td><td>심실 중격 속</td></tr>
<tr><td>6</td><td><b>Purkinje fibers 푸르키네 섬유</b></td><td>심실 근육 전체</td></tr></table>
<div class="boxg">순서 외우기: <g>"SA → 심방 → AV(잠깐 멈춤) → His → 좌·우 가지 → Purkinje → 심실"</g></div>
<div class="box"><span class="tag">시험 포인트</span>이 그림은 <b>그림 각주 문제</b>로 나오기 딱 좋다(SA결절, AV결절, 히스다발, 푸르키네 섬유 위치). 단어 박스 빈칸으로 전도 순서를 묻기도 좋다.</div>"""),
# 21
dict(img=21, slide=21, title="심장의 박동조율 세포 (글): 네 곳의 자동능 부위", sub="Pacemaker cells in the heart",
kw=["SA결절 = 정상 박동조율기", "AV결절", "히스다발", "푸르키네 섬유"],
sum="자동능이 있는 곳은 SA결절, AV결절, 히스다발, 푸르키네 섬유의 네 곳이다. 그중 <b>SA결절이 정상 박동조율기</b>다.",
tr="""<ul><li>자동능이 있는 특수 부위: SA결절, AV결절, 히스다발(AV다발), 푸르키네 섬유</li>
<li><b>SA결절</b>은 심장의 <i>정상</i> 박동조율기다.
<ul><li>상대정맥 입구 근처 우심방 벽의 작은 부위</li></ul></li>
<li><b>방실결절(AV node)</b>
<ul><li>우심방 바닥 중격 근처, 심방과 심실 경계 바로 위에 있는 작은 심장근 섬유 다발</li></ul></li>
<li><b>히스다발</b>
<ul><li>AV결절에서 시작해 중격으로 들어가는 세포 다발</li><li>심실 끝(심첨)을 돌아 다시 심방 쪽으로 올라간다.</li></ul></li>
<li><b>푸르키네 섬유</b>
<ul><li>히스다발에서 뻗어 나와 심실 심근층 전체로 퍼지는 작은 말단 섬유</li></ul></li></ul>""",
ex="""<table class="t"><tr><th>부위</th><th>위치 한 줄</th><th>역할</th></tr>
<tr><td><b>SA결절</b></td><td><y>우심방</y> 벽, 상대정맥 입구</td><td><b>정상 박동조율기</b></td></tr>
<tr><td><b>AV결절</b></td><td>우심방 바닥, 중격 근처</td><td>심방 → 심실 <y>유일한 통로</y> + 지연</td></tr>
<tr><td>히스다발</td><td>중격 속</td><td>심실로 빠르게 전달</td></tr>
<tr><td>푸르키네 섬유</td><td>심실 벽 전체</td><td>심실 근육 구석구석</td></tr></table>
<div class="boxg">히스다발이 심첨을 돌아 위로 올라가는 이유: 심실이 <g>아래(심첨)부터 위로</g> 수축해야 치약 짜듯 피를 위쪽 동맥으로 밀어낸다.</div>
<div class="box"><span class="tag">시험 포인트</span>"SA결절은 좌심방에 있다" → <b>✗</b> (우심방). 위치 함정 자주 나옴.</div>"""),
# 22
dict(img=22, slide=22, title="박동조율 활동 — 누가 리듬을 정하나", sub="Pacemaker activity",
kw=["SA 70–80/분", "AV 40–60/분", "히스·푸르키네 20–40/분", "가장 빠른 곳이 주도", "인공 박동조율기"],
sum="자동능 세포마다 발화 속도가 다르다: <b>SA결절 70–80</b>, <b>AV결절 40–60</b>, <b>히스·푸르키네 20–40</b>회/분. 가장 빠른 SA결절의 AP가 먼저 온 심장에 퍼지므로 SA결절이 박동조율기가 된다. SA결절이 고장 나면 AV결절이 이어받는다.",
tr="""<ul><li>자동능 세포마다 역치까지 느리게 탈분극하는 속도가 다르다.</li>
<li>또 세포 종류마다 1분에 만들 수 있는 AP 수(속도)가 다르다.
<ul><li>SA결절: <b>70–80</b> AP/분</li><li>AV결절: <b>40–60</b> AP/분</li><li>히스다발과 푸르키네 섬유: <b>20–40</b> AP/분</li></ul></li>
<li>어느 심장근 세포에서든 AP가 생기면 심장 전체로 전파된다 → <b>SA결절이 심장의 박동조율기</b></li>
<li>SA결절이 고장 나면 <b>AV결절</b>이 박동조율을 이어받는다.</li>
<li>심박수가 비정상적으로 느리면 <b>인공 박동조율기</b>를 쓴다.</li></ul>""",
ex="""<table class="t"><tr><th>부위</th><th>속도(회/분)</th><th>순위</th></tr>
<tr><td><b>SA결절</b></td><td><b>70–80</b></td><td>1등 → 정상 리듬(동리듬)</td></tr>
<tr><td>AV결절</td><td>40–60</td><td>2등 → SA 고장 시 대신</td></tr>
<tr><td>히스·푸르키네</td><td>20–40</td><td>3등 → 너무 느림</td></tr></table>
<p><b>왜 SA결절이 이기나?</b> SA결절이 가장 먼저 역치에 도달해 AP를 쏘면, 그 AP가 다른 자동능 세포까지 퍼져 그들이 <y>스스로 역치에 닿기 전에 미리 흥분시켜</y> 버린다(리셋). 그래서 다른 부위의 리듬은 숨어 있다.</p>
<div class="boxg">비유: 줄 서서 박수 치기 — 가장 빠른 사람이 박수를 시작하면 모두 따라 친다.</div>
<div class="box"><span class="tag">시험 포인트</span>숫자 3세트(<b>70–80 / 40–60 / 20–40</b>)와 "SA 고장 → AV가 대신"이 그대로 나온다. 정상 휴식 심박수 약 70회/분(슬라이드 36)과 연결.</div>"""),
# 23
dict(img=23, slide=23, title="심장의 흥분 전파 (1): 심방 흥분", sub="Cardiac excitation and muscle contraction",
kw=["조화된 전파", "심방 먼저", "간극연접", "심방간 경로", "결절간 경로", "AV결절 = 유일한 접점"],
sum="효율적인 펌프가 되려면 ① 심방 수축이 심실보다 먼저 끝나고 ② 각 방이 한 덩어리로 ③ 양쪽 심방·양쪽 심실이 동시에 수축해야 한다. SA결절의 AP는 간극연접 + <b>심방간 경로</b>(→좌심방)로 두 심방에 퍼지고, <b>결절간 경로</b>로 AV결절에 간다.",
tr="""<ul><li>심장 흥분의 전파는 효율적 펌프가 되도록 조화롭게 이루어진다.
<ul><li>심방의 흥분·수축이 심실 수축 시작 전에 끝나야 한다.</li><li>각 방이 한 덩어리로 수축해 효율적으로 펌프질하도록 섬유 흥분이 조화되어야 한다.</li><li>두 심방, 두 심실은 각각 동시에 수축하도록 조화된다.</li></ul></li>
<li>SA결절에서 시작된 AP는 심장 나머지로 퍼진다.</li>
<li><b>1) 심방 흥분</b>
<ul><li>SA결절의 AP는 먼저 <b>간극연접</b>을 통해 세포에서 세포로 두 심방 전체로 퍼진다.</li><li>추가로 특수 전도 경로가 전도를 빠르게 한다.</li>
<li><b>심방간 경로</b>: 좌심방으로 → 두 심방이 동시에 수축</li>
<li><b>결절간 경로</b>: AV결절로
<ul><li>AV결절은 심방과 심실 사이의 <b>유일한 전기적 접점</b>이다.</li><li>심방 수축 뒤에 심실이 순서대로 수축하게 한다.</li></ul></li></ul></li></ul>""",
ex="""<table class="t"><tr><th>경로</th><th>어디로</th><th>목적</th></tr>
<tr><td>간극연접 (세포→세포)</td><td>심방 전체</td><td>심방이 한 덩어리로</td></tr>
<tr><td><b>Interatrial 심방간</b></td><td>우심방 → <b>좌심방</b></td><td>두 심방 <y>동시</y> 수축</td></tr>
<tr><td><b>Internodal 결절간</b></td><td>SA → <b>AV결절</b></td><td>심실로 넘길 준비</td></tr></table>
<div class="boxg">펌프 효율의 3조건: <g>① 심방 → 심실 순서 ② 각 방은 한 덩어리 ③ 좌우는 동시</g></div>
<p>왜 심방이 먼저? 심방이 수축해 마지막 피를 심실에 채워 준 뒤에 심실이 짜야 한 번에 많이 내보낸다.</p>
<div class="box"><span class="tag">시험 포인트</span>"심방간 경로는 AV결절로 간다" → <b>✗</b> (좌심방으로). 결절간 = 결절(SA)과 결절(AV) 사이라고 외우기.</div>"""),
# 24
dict(img=24, slide=24, title="심장의 흥분 전파 (2): AV결절 지연 · 심실 흥분", sub="Cardiac excitation and muscle contraction",
kw=["AV결절 지연 ~100 ms", "심실 충만 보장", "히스다발", "푸르키네", "30 ms"],
sum="AV결절에서는 전도가 일부러 느려진다(<b>AV결절 지연, 약 100 ms</b>) → 심방이 수축을 끝내고 심실이 다 찰 시간을 준다. 그다음 히스다발·푸르키네 섬유가 <b>30 ms 안에</b> 심실 전체로 AP를 퍼뜨려 심실이 한 덩어리로 수축한다.",
tr="""<ul><li>SA결절에서 시작된 AP는 심장 나머지로 퍼진다.</li>
<li><b>2) 심방–심실 사이 전도</b>
<ul><li><b>AV결절 지연</b>: AP가 AV결절을 비교적 느리게 지나간다.</li><li>심방과 심실 사이 전도가 느려진다(약 <b>100 ms</b>).</li><li>심방 수축이 끝난 뒤 심실 충만이 이루어지도록 보장한다.</li></ul></li>
<li><b>3) 심실 흥분</b>
<ul><li>히스다발과 푸르키네 섬유(심실 전도계)가 중격을 따라 내려가 심실 심근층 전체로 퍼진다.</li>
<li>이 섬유망은 AP를 <b>30 ms 안에</b> 빠르게 전달해 심실이 한 덩어리로 수축하게 한다.</li></ul></li></ul>""",
ex="""<table class="t"><tr><th>단계</th><th>속도</th><th>의미</th></tr>
<tr><td>심방 전파</td><td>빠름</td><td>두 심방 동시 수축</td></tr>
<tr><td><b>AV결절</b></td><td><b>느림 (~100 ms 지연)</b></td><td><y>심실이 다 찰 때까지 기다림</y></td></tr>
<tr><td>히스·푸르키네</td><td><b>아주 빠름 (30 ms)</b></td><td>심실 전체 동시 흥분</td></tr></table>
<div class="boxg">AV결절 지연은 <g>심전도의 PR 분절</g>로 보인다(슬라이드 28).</div>
<p>비유: AV결절 = 톨게이트. 심방에서 온 신호를 잠깐 세워 두고(심실 채우기), 통과하면 고속도로(푸르키네)로 순식간에 심실 전체로.</p>
<div class="box"><span class="tag">시험 포인트</span>"AV결절은 전도가 가장 빠른 곳" → <b>✗</b> (가장 느림, 의도된 지연). 지연의 목적 = <b>심방 수축 완료 후 심실 충만</b>.</div>"""),
# 25
dict(img=25, slide=25, title="수축세포의 AP (글): 고원기", sub="The action potential of cardiac contractile cells",
kw=["휴지막전위 −90 mV", "빠른 Na⁺", "+30 mV", "고원기", "L형 Ca²⁺", "K⁺ 투과도 ↓", "긴 불응기"],
sum="수축세포는 −90 mV의 안정된 휴지막전위를 가진다. 간극연접으로 역치에 닿으면 <b>빠른 Na⁺ 유입</b>으로 +30 mV까지 오르고, 잠깐 내려온 뒤 <b>수백 ms 동안 고원기</b>(L형 Ca²⁺ 유입 + K⁺ 유출 감소)를 유지한다. 그래서 <b>불응기가 길어 강축이 없다</b>.",
tr="""<ul><li>SA결절 자동능 세포와 수축세포의 AP는 매우 다르다.</li>
<li>SA결절과 달리 수축세포는 약 <b>−90 mV</b>의 휴지막전위를 가진다 — 매우 새는 K⁺ 채널 → K⁺ 유출</li>
<li>간극연접을 통한 전류가 막을 역치까지 탈분극시키면 다음과 같이 AP가 생긴다.
<ul><li><b>전압개폐 Na⁺ 채널</b> 활성화: 막전위가 <b>+30 mV</b>까지 빠르게 상승</li>
<li>일시적·누출 K⁺ 채널 일부가 열림: K⁺ 유출로 짧은 재분극(덜 양성)</li>
<li>독특하게, 막전위가 <b>수백 ms 동안 유지</b>된다(AP의 <b>고원기</b>). 두 기전으로 유지:
<ul><li><b>느린 L형 Ca²⁺ 채널</b> 활성화: 느리고 오래가는 Ca²⁺ 유입</li><li><b>K⁺ 투과도의 뚜렷한 감소</b>: 채널이 닫혀 K⁺ 유출이 줄어 탈분극 유지</li></ul></li>
<li>L형 Ca²⁺ 채널의 비활성화(닫힘)와 전압개폐 K⁺ 채널 활성화 → 재분극</li></ul></li>
<li><b>긴 불응기가 강축을 막는다.</b></li></ul>""",
ex="""<table class="t"><tr><th>단계</th><th>이온</th><th>막전위</th></tr>
<tr><td>휴지</td><td>K⁺ 누출</td><td><b>−90 mV</b> (안정)</td></tr>
<tr><td>상승기</td><td><y>Na⁺ 빠른 유입</y></td><td>→ +30 mV</td></tr>
<tr><td>초기 재분극</td><td>일시적 K⁺ 유출</td><td>살짝 ↓</td></tr>
<tr><td><b>고원기</b></td><td><y>Ca²⁺ 유입(L형) + K⁺ 유출 ↓</y></td><td>약 0 mV 근처 <b>수백 ms 유지</b></td></tr>
<tr><td>재분극</td><td>Ca²⁺ 채널 닫힘 + K⁺ 유출 ↑</td><td>→ −90 mV</td></tr></table>
<div class="boxg"><b>왜 강축이 없나</b>: 고원기 때문에 AP(≈250 ms)가 수축만큼 길다 → <g>불응기가 수축이 거의 끝날 때까지 지속</g> → 다음 AP가 수축 중간에 끼어들 수 없어 가중·강축 불가. 덕분에 심장은 반드시 이완해서 다시 피를 채운다.</div>
<div class="box"><span class="tag">시험 포인트</span>박동조율 세포 vs 수축세포 비교가 핵심: 상승기 이온(<b>Ca²⁺ vs Na⁺</b>), 휴지막전위(<b>없음 vs −90 mV</b>), 고원기(<b>없음 vs 있음</b>).</div>"""),
# 26
dict(img=26, slide=26, title="수축세포의 AP (그림): 이온별 투과도 변화", sub="The action potential of cardiac contractile cells",
kw=["↑P_Na", "↓P_K (일시적)", "↑P_Ca 느림", "고원기", "~250 ms"],
sum="그래프로 보는 수축세포 AP: −90에서 <b>Na⁺ 빠른 유입</b>으로 +30 → 일시적 K⁺ 유출로 살짝 하강 → <b>Ca²⁺ 느린 유입 + K⁺ 유출 감소</b>로 고원기 → K⁺ 빠른 유출로 −90 복귀. 전체가 약 250 ms.",
tr="""<ul><li>그래프: 막전위(mV) vs 시간(ms)</li>
<li>상승: ↑P<sub>Na</sub> (Na⁺ 빠르게 들어옴) — 동시에 ↓P<sub>K</sub>(일시적·누출 K⁺)</li>
<li>살짝 하강: ↑P<sub>K</sub>(일시적) — K⁺ 빠르게 나감</li>
<li>고원기: ↑P<sub>Ca</sub>(L형), ↓P<sub>K</sub> — Ca²⁺ 천천히 들어옴</li>
<li>하강: ↓P<sub>Ca</sub>, ↑P<sub>K</sub>(일반 전압개폐) — K⁺ 빠르게 나감</li>
<li>바닥: ↓P<sub>K</sub>(일반 전압개폐), ↑P<sub>K</sub>(누출) — 휴지 −90 mV, 역치 약 −70 mV, 길이 약 250 ms</li></ul>""",
ex="""<p>P = permeability(투과도). ↑P<sub>X</sub> = X 이온 채널이 열려 그 이온이 잘 지나감.</p>
<table class="t"><tr><th>구간</th><th>열림(↑)</th><th>닫힘(↓)</th></tr>
<tr><td>빠른 상승</td><td><b>Na⁺</b></td><td>K⁺ (일시적·누출)</td></tr>
<tr><td>작은 하강</td><td>K⁺ (일시적)</td><td>—</td></tr>
<tr><td><b>고원기</b></td><td><b>Ca²⁺ (L형)</b></td><td><b>K⁺</b></td></tr>
<tr><td>재분극</td><td>K⁺ (일반 전압개폐)</td><td>Ca²⁺</td></tr></table>
<div class="boxg">골격근 AP는 1–2 ms(8장), 심장 수축세포 AP는 <g>약 250 ms</g> — 100배 이상 길다.</div>
<div class="box"><span class="tag">시험 포인트</span>그림 각주: 고원기 구간을 가리키고 "이 구간을 유지하는 두 이온 변화"를 쓰게 할 수 있다 → <b>Ca²⁺ 유입 ↑, K⁺ 유출 ↓</b>.</div>"""),
# 27
dict(img=27, slide=27, title="Ca²⁺ 유발 Ca²⁺ 방출 (CICR)", sub="Calcium entry from ECF induces Ca²⁺ release from SR",
kw=["T세관의 L형 Ca²⁺ 채널", "세포외액 Ca²⁺", "라이아노딘 수용체", "CICR", "트로포닌"],
sum="심장근에서는 AP 동안 T세관의 L형 Ca²⁺ 채널로 <b>세포외액의 Ca²⁺가 조금</b> 들어오고, 이 Ca²⁺가 SR의 <b>라이아노딘 수용체</b>를 열어 <b>훨씬 많은 Ca²⁺를 방출</b>시킨다(Ca²⁺ 유발 Ca²⁺ 방출). 그 Ca²⁺가 트로포닌에 붙어 교차다리가 시작된다.",
tr="""<ul><li>L형 Ca²⁺ 채널은 대부분 <b>T세관</b>에 있다.</li>
<li>골격근과 달리, AP 동안 Ca²⁺가 T세관을 가로질러 <b>세포외액(ECF)</b>에서 세포질로 확산해 들어온다.</li>
<li>이 들어온 Ca²⁺가 SR 측면 주머니의 <b>라이아노딘 Ca²⁺ 방출 채널</b>을 연다.</li>
<li><b>Ca²⁺ 유발 Ca²⁺ 방출(CICR)</b>: ECF에서 세포질로 들어온 Ca²⁺가 세포 안 SR에서 훨씬 많은 Ca²⁺를 방출시킨다.</li>
<li>Ca²⁺는 트로포닌-트로포마이오신 복합체에 붙어 그것을 옆으로 끌어내 교차다리를 가능하게 한다.</li>
<li>Ca²⁺ 양이 골격근보다 더 세밀하게 조절된다.</li>
<li>(흐름도) 심장 수축세포의 AP → T세관 따라 내려감 → L형 Ca²⁺ 채널로 소량 Ca²⁺ 유입 → SR에서 대량 Ca²⁺ 방출 → 세포질 Ca²⁺ ↑ → 트로포닌-트로포마이오신 이동 → 교차다리 순환 → 가는 필라멘트가 미끄러짐 → 수축</li></ul>""",
ex="""<table class="t"><tr><th></th><th>골격근 (8장)</th><th>심장근</th></tr>
<tr><td>Ca²⁺ 출처</td><td><b>SR만</b></td><td><b>ECF(소량) + SR(대량)</b></td></tr>
<tr><td>SR 방출 방아쇠</td><td>T세관 전압 변화가 직접</td><td><y>들어온 Ca²⁺</y>가 라이아노딘 수용체를 엶</td></tr>
<tr><td>Ca²⁺ 결합</td><td>트로포닌</td><td>트로포닌</td></tr>
<tr><td>조절</td><td>보통 최대한 방출</td><td>방출량을 <b>조절</b> → 수축력 조절 가능</td></tr></table>
<div class="boxg"><g>CICR = 작은 불씨(ECF Ca²⁺)가 큰 불(SR Ca²⁺)을 붙인다</g></div>
<p>교감신경(NE·E)이 L형 Ca²⁺ 유입을 늘리면 SR 방출도 커져 <y>수축력 ↑</y> — 슬라이드 40의 "수축성"과 연결.</p>
<div class="box"><span class="tag">시험 포인트</span>"심장근 수축의 Ca²⁺는 모두 세포외액에서 온다" → <b>✗</b> (대부분은 SR). "골격근처럼 SR에서만" → <b>✗</b>. 정답은 <b>둘 다, 그리고 ECF가 SR을 촉발</b>.</div>"""),
# 28
dict(img=28, slide=28, title="심전도 (ECG)", sub="ECG (electrocardiogram)",
kw=["P파", "QRS군", "T파", "PR 분절", "ST 분절", "TP 분절"],
sum="심전도는 심장 전기 활동이 체액을 타고 <b>몸 표면</b>에 닿은 것을 기록한 것이다. <b>P파 = 심방 탈분극</b>, <b>QRS = 심실 탈분극</b>(심방 재분극은 가려짐), <b>T파 = 심실 재분극</b>. PR 분절 = AV결절 지연, ST 분절 = 고원기, TP 분절 = 쉬는 기준선.",
tr="""<ul><li>ECG는 심장 전체의 전기 활동 확산을 기록한 것이다.</li>
<li>ECG는 몸 표면에 도달한 심장 자극이 체액에 만든 전기 활동의 기록이지, 심장 실제 전기 활동의 직접 기록이 아니다.</li>
<li>ECG의 세 파형
<ul><li><b>P파</b>: 심방 탈분극</li><li><b>QRS군</b>: 심실 탈분극 (심방 재분극은 가려짐)</li><li><b>T파</b>: 심실 재분극</li></ul></li>
<li>심장근에 알짜 전류가 없는 세 구간
<ul><li><b>PR 분절</b>: P 끝 ~ QRS 시작 — <b>AV결절 지연</b>(AV결절 통과 전도)을 반영</li>
<li><b>ST 분절</b>: QRS ~ T — 심실이 완전히 탈분극된 시기(<b>고원기</b>)</li>
<li><b>TP 분절</b>: T 끝 ~ 다음 P — 박동 사이 전기적으로 조용한 시기(<b>진짜 기준선</b>)</li></ul></li></ul>""",
ex="""<table class="t"><tr><th>파형/구간</th><th>심장에서 일어나는 일</th></tr>
<tr><td><b>P</b></td><td>심방 <y>탈분극</y> (→ 곧 심방 수축)</td></tr>
<tr><td>PR 분절</td><td><y>AV결절 지연</y></td></tr>
<tr><td><b>QRS</b></td><td>심실 <y>탈분극</y> (+ 심방 재분극이 묻힘)</td></tr>
<tr><td>ST 분절</td><td>심실 <y>고원기</y> (전체가 탈분극 상태라 전류 0)</td></tr>
<tr><td><b>T</b></td><td>심실 <y>재분극</y></td></tr>
<tr><td>TP 분절</td><td>휴식, 기준선</td></tr></table>
<div class="boxg">중요한 오해: ECG의 파형 = <g>전기</g> 사건, 수축(기계) 자체가 아니다. 수축은 탈분극 <b>직후</b>에 따라온다.</div>
<p>왜 심방 재분극 파가 안 보이나? QRS와 같은 때 일어나는데 심실이 훨씬 커서 신호가 덮인다.</p>
<div class="box"><span class="tag">시험 포인트</span>① P·QRS·T 짝짓기 ② "T파 = 심방 재분극" → <b>✗</b> ③ PR = AV 지연, ST = 고원기. 그림 각주·빈칸 단골.</div>"""),
# 29
dict(img=29, slide=29, title="심전도와 심장 주기 · 심전도로 알 수 있는 것", sub="ECG (electrocardiogram) and cardiac cycle",
kw=["흥분 순서와 파형", "심박수 이상", "리듬 이상", "심근병증·손상"],
sum="그림은 SA결절 발화 → P파(심방 탈분극) → PR(AV 지연) → QRS(심실 탈분극) → ST(심실 수축·박출) → T파(심실 재분극) → TP(이완·충만)를 심장 그림과 함께 한 바퀴로 보여 준다. 심전도로 <b>심박수·리듬 이상과 심근 손상</b>을 찾는다.",
tr="""<ul><li>(그림) 한 번의 정상 심박 동안 심전도의 각 구간과 심장의 전기 흥분 부위를 대응</li>
<li>ECG는 비정상적인 심박수와 리듬, 그리고 심장근 손상을 찾아낸다.
<ul><li>심박수 이상</li><li>리듬 이상</li><li>심근병증(cardiac myopathies)</li></ul></li></ul>""",
ex="""<table class="t"><tr><th>순서</th><th>심전도</th><th>심장 (색칠된 부위)</th></tr>
<tr><td>1</td><td>—</td><td>SA결절 발화</td></tr>
<tr><td>2</td><td>P파</td><td>심방 탈분극</td></tr>
<tr><td>3</td><td>PR 분절</td><td>AV결절 지연 (심방 수축, 심실 마지막 충만)</td></tr>
<tr><td>4</td><td>QRS</td><td>심실 탈분극</td></tr>
<tr><td>5</td><td>ST 분절</td><td>심실 수축·박출</td></tr>
<tr><td>6</td><td>T파</td><td>심실 재분극</td></tr>
<tr><td>7</td><td>TP 분절</td><td>심실 이완·충만</td></tr></table>
<table class="t"><tr><th>찾을 수 있는 것</th><th>예</th></tr>
<tr><td>심박수 이상</td><td>빈맥(너무 빠름), 서맥(너무 느림)</td></tr>
<tr><td>리듬 이상</td><td>부정맥, 심방세동, 방실 차단(P 뒤에 QRS가 빠짐)</td></tr>
<tr><td>심근 손상</td><td>심근경색 시 ST 분절 변화</td></tr></table>
<div class="box"><span class="tag">시험 포인트</span>심전도 구간 ↔ 심장 사건 짝짓기를 "순서대로 빈칸 채우기"로 낼 수 있다. 다음 절(9.3) 심장 주기 그림과 같이 묶어 외우기.</div>"""),
# 30
dict(img=30, slide=30, title="9.3 심장 주기의 기계적 사건 (섹션 표지)", sub="9.3 Mechanical Events of the Cardiac Cycle",
kw=["수축기", "이완기", "등용적", "판막 개폐", "심음"],
sum="9.3절은 전기 신호가 만든 <b>수축과 이완</b>이 심실 압력·용적·판막·심음을 어떻게 바꾸는지, 즉 심장 주기의 네 단계를 다룬다.",
tr="""<ul><li><b>9.3 심장 주기의 기계적 사건(Mechanical Events of the Cardiac Cycle)</b></li></ul>""",
ex="""<table class="t"><tr><th>슬라이드</th><th>내용</th></tr>
<tr><td>31</td><td>심장 주기 영상</td></tr>
<tr><td>32</td><td>수축기·이완기, <y>네 단계 정의</y></td></tr>
<tr><td>33</td><td>단계별 판막·ECG·심음 (Wiggers 도표)</td></tr>
<tr><td>34</td><td><y>압력-용적 고리</y>: EDV 135 mL, ESV 65 mL, SV 70 mL</td></tr></table>
<div class="boxg">한 줄로: 판막이 <b>둘 다 닫힌</b> 짧은 두 시기(등용적 수축·이완)와, <b>하나만 열린</b> 긴 두 시기(충만·박출)가 번갈아 온다.</div>"""),
]
