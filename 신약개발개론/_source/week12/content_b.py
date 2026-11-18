# 12주차 (2) 11주차 PK 복습 재사용 + Chapter 5 전임상 도입 (슬라이드 14~41)
PAGES = [
# 슬라이드 14~35 = 11주차 자료 44~65 = 11주차 요약정리 32~37쪽 (PK 묶음 페이지)
dict(reuse=(32, "14~17·20·21", "44~47·50·51")),   # PK 흡수·생체이용률
dict(reuse=(33, "18·19", "48·49")),               # 전신순환
dict(reuse=(34, "22~26", "52~56")),      # PK 분포
dict(reuse=(35, "27~30", "57~60")),         # PK 대사 Phase I/II
dict(reuse=(36, "31·32", "61·62")),               # PK 배설
dict(reuse=(37, "33~35", "63~65")),            # ADME 개인차·PK/PD 모델링

dict(title="Chapter 5. 전임상연구 · 전임상 동물연구", slide="36·37", img=["s36.jpg", "s37.jpg"],
     sub="Preclinical study: toxicity &amp; efficacy",
     kw=["Chapter 5 시작", "동물독성 실험", "ADME 체내동태", "설치류·포유류"],
     sum="새 단원 <b>Chapter 5. 전임상연구(독성연구 &amp; 유효성평가)</b>. 후보물질의 <b>유효성·안전성(독성)</b>을 동물에서 검증하는 단계로, ADME 체내동태와 약효/약리 연구를 포함해. 쥐·토끼·개 등 설치류·포유류를 주로 써.",
     lab="슬라이드 내용",
     tr="""<p><b>36</b> Chapter 5. 전임상연구: 독성연구 &amp; 유효성평가 (표지)</p>
<p><b>37 전임상 동물연구 — 동물독성 실험</b></p>
<ul><li>후보물질의 <g>유효성·안전성(독성)을 검증</g>하는 단계 — 약물의 흡수·분포·배설(ADME) 체내동태와 약효/약리 연구 포함</li>
<li>약동학·약역학 외에도 기능적·형태적 효과(제형·장소·target 작용·용량 연관성·<b>성별 차이·잠복기·가역성(reversibility)</b>) 포함</li>
<li>실험동물: 쥐·토끼·기니픽·돼지·페렛·햄스터·개 등 설치류·포유류</li></ul>""",
     ex="""<p><b>전임상연구가 보는 두 축</b>:</p>
<ul><li><b>독성(안전성)</b>: 얼마나 투여하면 해로운가 → 임상 시작 용량의 근거</li>
<li><b>유효성</b>: 동물 질환 모델에서 실제로 약효가 있는가</li></ul>
<p>둘 다 몸속 거동(ADME)을 알아야 해석돼 — 그래서 앞의 PK 복습(14~35)이 이 단원의 전제야.</p>
<p class="box"><span class="tag">기말</span>전임상 = <pk>유효성 + 안전성(독성) 검증</pk>. 포함 항목에 가역성(reversibility)·성별 차이가 들어가는 것 주의.</p>"""),

dict(title="동물종과 전임상시험 — 쥐를 쓰는 이유", slide="38", img="s38.jpg",
     sub="Why rodents dominate preclinical testing",
     kw=["침팬지 99% · 쥐 81%", "비용 저렴", "관리 용이·빠른 번식", "유전자 조작 쉬움"],
     sum="사람과의 유전적 유사성은 <b>침팬지 99% &gt; 쥐 81%</b>라 침팬지 단백질이 더 비슷해. 그런데도 <b>쥐를 주로 쓰는 이유</b>는 비용이 싸고, 작아서 관리가 쉽고, 번식이 빠르고, 유전자 조작이 상대적으로 쉽기 때문이야.",
     lab="슬라이드 내용",
     tr="""<ul><li>동물실험에서 여러 동물 중 <b>침팬지와 쥐</b>를 많이 사용</li>
<li>유전적 유사성: <b>침팬지 99%, 쥐 81%</b></li>
<li>침팬지가 단백질이 사람과 더 유사하지만, <g>쥐를 주로 쓰는 이유</g> = 비용 저렴·작아서 관리 용이·번식력 빠름·유전자 조작 상대적으로 쉬움</li></ul>""",
     ex="""<p>슬라이드 그림의 동물별 특징:</p>
<table class="t"><tr><th>동물</th><th>특징</th></tr>
<tr><td>쥐</td><td>결과 확인 빠름·가장 많이 쓰임</td></tr>
<tr><td>개</td><td>사람과 삶 공유·비슷한 질병</td></tr>
<tr><td>돼지</td><td>장기 크기·구조가 사람과 비슷</td></tr>
<tr><td>영장류</td><td>사람과 가장 비슷·그러나 높은 비용</td></tr></table>
<p class="box"><span class="tag">기말</span><pk>침팬지 99% &gt; 쥐 81%</pk>인데도 쥐를 쓰는 건 비용·크기·번식·유전자 조작 때문. “쥐가 사람과 더 유사해서”는 틀린 보기.</p>"""),

dict(title="전임상연구 — 탐색적 vs 규제적", slide="39·40·41", img="s39.jpg",
     sub="Exploratory vs regulatory preclinical study",
     kw=["Candidate 기준으로 구분", "약물발굴 = 탐색적", "약물개발 = 규제적", "Drug Discovery/Development"],
     sum="전임상연구는 <b>Drug Candidate를 기준</b>으로 둘로 나뉘어. 후보물질 <b>이전(약물발굴, Drug Discovery)</b>은 <b>탐색적 전임상</b>, 후보물질 <b>이후(약물개발, Drug Development)</b>는 <b>규제적 전임상</b>이야.",
     lab="슬라이드 내용",
     tr="""<p><b>신약 후보물질 발굴 과정</b>: Hit 발견 → Hit to Lead → Lead Optimization → Drug Candidate</p>
<ul><li><b>Drug Candidate 까지</b> = 약물발굴(Drug <b>Discovery</b>)
  <ul><li>이 단계의 전임상 = <g>탐색적 전임상연구</g></li></ul></li>
<li><b>Drug Candidate 이후</b> = 약물개발(Drug <b>Development</b>)
  <ul><li>이 단계의 전임상 = <g>규제적 전임상연구</g></li></ul></li></ul>
<p class="note">39 그림: Drug Discovery→Pharmacology→Toxicology→임상 흐름. 40: 줄기세포 파킨슨 치료제 전임상 예시(쥐 50~100마리/군 → 영장류 10~20마리/군). 41: 평가 → PoC → 예비 안전성(GLP) → 확정 안전성(GLP/GMP) → IND.</p>""",
     ex="""<p>경계선은 <b>Drug Candidate가 정해지는 순간</b>이야. 그 전은 “어떤 후보가 될까” 탐색이라 자유롭고, 그 후는 “이 후보를 허가받자”라 규칙(GLP)을 따라야 해.</p>
<table class="t"><tr><th>구분</th><th>탐색적</th><th>규제적</th></tr>
<tr><td>시점</td><td>후보물질 이전(발굴)</td><td>후보물질 이후(개발)</td></tr>
<tr><td>목적</td><td>후보 탐색·방향 결정</td><td>허가용 독성 용량 규명</td></tr></table>
<p class="box"><span class="tag">기말</span><pk>탐색적 = Drug Discovery(후보 전), 규제적 = Drug Development(후보 후).</pk> 경계 = Drug Candidate 선정.</p>"""),
]
