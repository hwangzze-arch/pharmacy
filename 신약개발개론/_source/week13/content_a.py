# (A) 표지 · 전임상 개요 · 실험동물 (슬라이드 1~14)
PAGES = [
dict(title="강의 표지 · 이번 강의 로드맵", src="표지", img="s01.jpg",
     sub="신약개발개론 — Non-GLP 전임상 연구와 동물실험 대체법 (10·13주차 보강 녹화 강의)",
     kw=["Chapter 5 전임상", "탐색적 vs 규제적", "실험동물", "안전성 → 유효성", "FDA 현대화법 2.0", "Organ-on-a-chip"],
     sum="휴강 보강 녹화 강의. 앞부분은 <b>Non-GLP(탐색적) 전임상연구</b> — 실험동물, 안전성 평가, 유효성 평가 사례. 뒷부분은 <b>동물실험 대체법</b> — FDA 현대화법 2.0, 오가노이드, Organ-on-a-chip(간 칩 연구)이야.",
     lab="표지 내용",
     tr="""<h3>신약개발개론</h3><ul>
<li>Non-GLP 전임상 연구와 동물실험대체법</li>
<li>Han-Jun Kim (김한준), D.V.M., Ph.D. — College of Pharmacy, Korea University</li>
<li class="note">표지 날짜(2023.11.26)와 직함(Assistant Professor)은 예전 녹화본 그대로야.</li></ul>
<p class="note">마지막 “Questions?”(53)는 내용이 없어 뺐어.</p>""",
     ex="""<table class="t"><tr><th>파트</th><th>슬라이드</th><th>이 노트</th></tr>
<tr><td>전임상 개요 · 탐색적 vs 규제적</td><td>2~8</td><td>2~4쪽</td></tr>
<tr><td>실험동물 · 비교생물학</td><td>9~14</td><td>5~8쪽</td></tr>
<tr><td>1단계 안전성 (생체적합성·독성)</td><td>15~21</td><td>9~12쪽</td></tr>
<tr><td>2단계 유효성 · 질환모델 사례</td><td>22~32</td><td>13~18쪽</td></tr>
<tr><td>동물실험 대체법 · FDA 현대화법 2.0</td><td>33~43</td><td>19~24쪽</td></tr>
<tr><td>간 칩(Liver-on-a-chip) 연구</td><td>44~52</td><td>25~27쪽</td></tr></table>
<p><b>12주차와 연결</b>: 12주차에 본 <g>탐색적(Non-GLP) vs 규제적(GLP) 전임상</g> 중 <b>탐색적</b> 쪽을 교수님 연구 사례로 자세히 보는 강의야.</p>
<p class="box"><span class="tag">기말</span>탐색적 vs 규제적, <b>FDA 현대화법 2.0</b>(동물실험 의무 폐지가 아니라 <b>선택</b>), <b>오가노이드 vs Organ-on-a-chip</b> 정의가 1순위.</p>"""),

dict(title="Chapter 5 · 전임상연구 — 탐색적 vs 규제적", slide="2·3·6", img=["s03.jpg", "s06.jpg"],
     sub="Preclinical study: exploratory vs regulatory",
     kw=["Drug Candidate가 경계", "탐색적 = 약물발굴", "규제적 = 약물개발", "GLP 적용 여부"],
     sum="전임상연구는 <b>Drug Candidate 선정을 경계</b>로 나뉘어. 그 전(약물발굴)은 <b>탐색적 전임상</b>으로 GLP가 필수가 아니고, 그 후(약물개발)는 <b>규제적 전임상</b>으로 GLP를 따르며 독성 용량을 찾아.",
     lab="슬라이드 내용",
     tr="""<p><b>2</b> Chapter 5. 전임상연구: 독성연구 &amp; 유효성평가</p>
<p><b>3 신약 후보물질 발굴 과정</b>: Hit 발견 → Hit to Lead → Lead Optimization → Drug Candidate</p>
<ul><li>Drug candidate <b>까지</b> = 약물발굴(Drug discovery) → <g>탐색적 전임상연구</g></li>
<li>Drug candidate <b>이후</b> = 약물개발(Drug Development) → <g>규제적 전임상연구</g></li></ul>
<p><b>6</b> 탐색적 전임상: GLP 규정을 반드시 적용할 필요 없음 · 유연 · 선도물질 선정 이전에도 수행 · 약물발굴에 중요<br>
규제적 전임상: GLP 규정 준수 · 실험방법 정형화 · 독성에 관여하는 용량을 찾는 것이 목표</p>""",
     ex="""<table class="t"><tr><th></th><th>탐색적 (Non-GLP)</th><th>규제적 (GLP)</th></tr>
<tr><td>시점</td><td>후보물질 이전</td><td>후보물질 이후</td></tr>
<tr><td>단계</td><td>약물발굴</td><td>약물개발</td></tr>
<tr><td>GLP</td><td>필수 아님</td><td>필수</td></tr>
<tr><td>방법</td><td>유연</td><td>정형화</td></tr>
<tr><td>목표</td><td>후보 탐색</td><td>독성 용량 규명</td></tr></table>
<p>이번 강의 제목의 <b>“Non-GLP 전임상”</b> = 탐색적 전임상이야.</p>
<p class="box"><span class="tag">시험 포인트</span>12주차와 같은 내용이 또 나왔어. <pk>탐색적↔규제적, GLP 적용 여부를 바꾼 보기</pk>를 조심해.</p>"""),

dict(title="신약개발 흐름 속 전임상 (Drug development · Preclinical testing)", slide="4·5", img=["s04.jpg", "s05.jpg"],
     sub="Where preclinical research sits",
     kw=["Target → Hit → Lead", "Drug candidate", "PoC → 예비 안전성", "확정 안전성 → IND"],
     sum="신약개발 순환(Target → Hits → Leads → 최적화 → Drug candidate) 중 <b>후보물질 이후 임상으로 가는 구간</b>이 전임상이야. 전임상은 평가 → 개념증명(PoC) → 예비 안전성 → 확정 안전성/효능 순으로 진행돼 IND로 이어져.",
     lab="슬라이드 내용",
     tr="""<p><b>4 Drug development</b>: Drug target search → Screening → Hits → 구조생물학·분자모델링 → 의약화학 → Leads → Optimisation → <b>Selection of drug candidate</b> → Pharmacology · PK/대사 → To clinical studies (빨간 점선 = 이번 범위)</p>
<p><b>5 Preclinical testing</b> 단계</p>
<ul><li><b>Evaluation</b>: in vitro testing · animal model · in vivo testing</li>
<li><b>Proof-of-concept(efficacy)</b>: Compliance R&amp;D · Material R&amp;D · 예비 효능</li>
<li><b>Preliminary safety</b>: Compliance <b>GLP</b> · Material <b>GMP</b> · IND enabling</li>
<li><b>Definitive safety/efficacy</b>: Compliance <b>GLP/GMP</b> · Material clinical-grade · IND enabling</li></ul>""",
     ex="""<p>5번 그림 읽기 — 왼쪽(노란 점선)은 <b>R&amp;D 수준</b>(탐색적), 오른쪽(파란 점선)은 <b>GLP/GMP 수준</b>(규제적)이야. 뒤로 갈수록 규제 수준과 재료 등급이 올라가.</p>
<ul><li>탐색적 쪽: 연구실 수준(R&amp;D) 재료·기준</li>
<li>규제적 쪽: GLP(시험) + GMP(제조) + clinical-grade 재료 → <b>IND 신청 가능</b></li></ul>
<p class="box"><span class="tag">연결</span>GLP = 시험 관리기준, GMP = 제조 관리기준. 전임상 후반은 둘 다 요구돼.</p>"""),

dict(title="신약개발과정 · 전임상연구 지도", slide="7·8", img=["s07.jpg", "s08.jpg"],
     sub="Drug development stages and preclinical research map",
     kw=["기초연구 2~3년", "비임상 3~5년", "임상 3~7년", "NIH NCATS 지도"],
     sum="신약개발 6단계 중 <b>비임상(전임상)은 3~5년</b>. 신약 후보의 효능·안전성 연구, 약리·약동·독성 연구, 제형·생산(CMC)이 이 단계에서 이뤄져. 전임상은 이익(질병 경과·영상·치료 기회)과 위험(단기·장기 안전성·임신 등)을 저울질하는 단계야.",
     lab="슬라이드 내용",
     tr="""<p><b>7 신약개발과정</b> (6단계)</p>
<ol><li>기초연구 2~3년 — 발견·신물질 합성·타겟 탐색·스크리닝</li>
<li><b>비임상(non-clinical) 3~5년</b> — 신물질 효능·안전성: 약리 효능, 약동학, 독성 / CMC: 제형 설계·생산</li>
<li>임상 3~7년 — 1상(건강인 안전성) · 2상(소수 환자 효능·용량) · 3상(대규모 비교)</li>
<li>신약 허가 신청·심사 약 1년</li><li>승인·출시</li><li>시판 후 조사(4상)</li></ol>
<p><b>8 Preclinical Research</b>: R&amp;D → Preclinical research(안전성·효능 시험) → Clinical studies. 아래는 이익 vs 위험 저울과 NIH NCATS 신약개발 지도(2017).</p>""",
     ex="""<p>빨간 점선(2단계)이 이번 강의 범위야. 기간 숫자를 기억해 둬.</p>
<table class="t"><tr><th>단계</th><th>기간</th></tr>
<tr><td>기초연구</td><td>2~3년</td></tr><tr><td><b>비임상(전임상)</b></td><td><b>3~5년</b></td></tr>
<tr><td>임상</td><td>3~7년</td></tr><tr><td>허가 신청·심사</td><td>약 1년</td></tr></table>
<p class="box"><span class="tag">시험 포인트</span>비임상에서 하는 것 = <pk>약리(효능) · 약동학 · 독성 + CMC(제형·생산)</pk>.</p>"""),

dict(title="흔히 쓰는 실험동물 모델의 장점과 용도", slide="9", img="s09.jpg",
     sub="Advantages and applications of common animal models",
     kw=["설치류 = 가장 많이", "토끼", "제브라피시", "초파리 · 제노푸스"],
     sum="실험동물마다 장점이 달라. <b>설치류</b>는 가장 많이 쓰이고 유전자 조작이 쉬우며 사람과 매우 비슷해 모든 질병 연구에 써. 토끼는 다루기 쉽고, 제브라피시·초파리는 싸고 세대가 짧아 발생·유전 연구에 좋아.",
     lab="슬라이드 내용",
     tr="""<table class="t"><tr><th>동물</th><th>장점 · 용도</th></tr>
<tr><td><b>설치류(Rodents)</b></td><td>가장 많이 쓰임 · 구하기 쉬움 · 유전자 조작 가능 · 사람과 매우 비슷 · 모든 질병 연구</td></tr>
<tr><td><b>토끼(Rabbit)</b></td><td>짧은 수명 주기 · 온순해 다루기 쉬움 · 계통적으로 가까움 · 모든 질병 연구</td></tr>
<tr><td><b>제노푸스(Xenopus)</b></td><td>알 조작 쉬움 · 체외수정 · 배아 발생 연구</td></tr>
<tr><td><b>제브라피시</b></td><td>저렴 · 세대 짧음 · 배아 투명 · 유전자 조작 쉬움 · 발생 질환 연구</td></tr>
<tr><td><b>초파리(Drosophila)</b></td><td>저렴 · 세대 짧음 · 작은 게놈 · 유전자 기능·돌연변이 연구</td></tr></table>""",
     ex="""<p>12주차 “쥐를 주로 쓰는 이유(비용·관리·번식·유전자 조작)”와 같은 흐름이야.</p>
<p><b>질병 모델로는 설치류·토끼</b>, <b>발생·유전 연구로는 제브라피시·제노푸스·초파리</b>로 나눠 기억하면 쉬워.</p>
<p class="box"><span class="tag">시험 포인트</span>“가장 많이 쓰이는 실험동물 = <pk>설치류</pk>”. 투명한 배아 = 제브라피시.</p>"""),

dict(title="실험용 생쥐 · 비교생물학", slide="10·11", img=["s10.jpg", "s11.jpg"],
     sub="Laboratory mice and comparative biology",
     kw=["연구의 ~75%", "단백질 코딩 85% 동일", "99% ~ 60%", "치료제 효과 검증"],
     sum="생쥐는 전체 연구의 약 75%에 쓰이는 “생명의 은인”이야. NIH에 따르면 생쥐와 사람 게놈의 <b>단백질 코딩 영역은 평균 85% 동일</b>(유전자에 따라 99%~60%)해서, 치료제 후보의 효과를 시험하기 좋아.",
     lab="슬라이드 내용",
     tr="""<p><b>10 Laboratory Mice — “CV of a Lifesaver”</b></p>
<ul><li>연구의 약 <b>75%</b>에 쓰임 · 짧은 수명과 빠른 번식 → 일생 전체 연구 가능</li>
<li>유전자의 90%가 사람과 비슷 · 생식·신경계가 비슷해 같은 질병을 앓음</li>
<li>유전자 조작으로 사람 질병 모델을 만들 수 있음 · 노벨상 연구에 다수 기여</li></ul>
<p><b>11 Comparative biology</b> (NIH NHGRI, 2010)</p>
<p>“평균적으로 생쥐와 사람 게놈의 <b>단백질 코딩 영역은 85% 동일</b>하다. 어떤 유전자는 99%, 어떤 것은 60%만 같다. 생쥐 모델은 치료제 후보를 시험하고 효과를 평가할 기회를 준다.”</p>""",
     ex="""<p>숫자 정리 — 헷갈리지 않게 출처별로 기억해:</p>
<table class="t"><tr><th>숫자</th><th>뜻</th></tr>
<tr><td><b>85%</b></td><td>생쥐-사람 단백질 코딩 영역 평균 동일성(NIH)</td></tr>
<tr><td>99% / 60%</td><td>유전자에 따라 최고 / 최저</td></tr>
<tr><td>~75%</td><td>생쥐가 쓰이는 연구 비율</td></tr>
<tr><td>99% / 81%</td><td>(12주차) 침팬지 / 쥐 유전적 유사성</td></tr></table>
<p class="box"><span class="tag">주의</span>12주차 “쥐 81%”와 이번 “생쥐 85%”는 출처·기준이 달라. 문제에 나온 기준을 그대로 따라가.</p>"""),

dict(title="수의사·생명공학 배경의 약학 연구자 · 바이오의약품과 전임상", slide="12·13", img=["s12.jpg", "s13.jpg"],
     sub="DVM/bioengineering scientists · biopharmaceutics and preclinical research",
     kw=["비교의학", "제약사 병리 책임자", "COVID-19 백신", "전임상 → 빠른 승인"],
     sum="MIT·피츠버그대 등에서 수의사·생명공학 연구자가 비교의학·재생의학을 이끌고, 모더나·화이자·암젠 등 제약사의 <b>병리(전임상) 책임자</b>도 맡고 있어. 바이오의약품 매출이 급성장했고, COVID-19 백신은 전임상 데이터로 빠르게 개발됐어.",
     lab="슬라이드 내용",
     tr="""<p><b>12</b> 수의사(DVM)·생명공학 배경 연구자 예시</p>
<ul><li>MIT 비교의학 부서 창립 소장 · 생명공학·안과·의학 교수진</li>
<li>피츠버그대 McGowan 재생의학연구소 — DARPA 2,200만 달러(약 266억 원) 근육 재생 장치 과제</li>
<li>모더나·아스트라제네카·화이자·암젠·리제네론의 <b>병리(Pathology) 책임자</b></li></ul>
<p><b>13</b> 2020년 매출 상위 10개 의약품(60억 달러 이상) 중 바이오의약품 급증 · COVID-19 이전 백신 개발은 10~15년 · 화이자·바이오엔텍 mRNA 백신 전임상 결과 발표</p>""",
     ex="""<p>교수님(수의사, D.V.M.)이 이 슬라이드를 넣은 이유: <g>전임상(동물실험·병리 평가)은 수의학·생명공학 전문성이 필요한 분야</g>이고, 글로벌 제약사도 이 인력을 핵심으로 둔다는 거야.</p>
<p>COVID-19 이전에는 백신 개발에 보통 <b>10~15년</b>이 걸렸어(13번 그림). COVID-19 백신은 전임상 결과를 빠르게 발표하며 이 기간을 크게 줄였어.</p>
<p class="box"><span class="tag">참고</span>사례 슬라이드라 세부 이름·금액보다 <b>“전임상 = 동물 병리 평가가 핵심”</b> 흐름을 기억해.</p>"""),

dict(title="다양한 신기술 바이오 소재 (Various Novel Biotechnology)", slide="14", img="s14.jpg",
     sub="Novel biotechnology platforms",
     kw=["마이크로니들", "줄기세포 시트", "주사형 소재", "전자 패치 · 의료기기"],
     sum="요즘 전임상 대상은 약물만이 아니야. <b>마이크로니들, 줄기세포 시트, 생리활성 소재, 주사형 소재, 전자 패치, 의료기기</b> 같은 신기술도 같은 전임상 평가(안전성 → 유효성)를 거쳐.",
     lab="슬라이드 내용",
     tr="""<ul><li><b>Microneedle</b> — 피부에 붙이는 미세바늘 패치</li>
<li><b>Stem-cell loaded sheet</b> — 줄기세포(MSC)를 실은 나노섬유 시트(SF+GelMA 공동 전기방사)</li>
<li><b>Bioactive Materials</b> — 생리활성 성분을 담은 소재(예: 커큐민 나노입자)</li>
<li><b>Injectable Materials</b> — 주사로 넣는 하이드로겔 등</li>
<li><b>Electronic Patch</b> — 전기장을 주는 유연 패치</li>
<li><b>Biomedical Device</b> — 체내 삽입형 장치(신경 전극 등)</li></ul>""",
     ex="""<p>이 여섯 가지가 뒤의 <b>유효성 사례(24~31)</b>에 하나씩 다시 나와. 예: 전자 패치 → 상처 치유, 신경 전극 → 신경병증 통증, 마이크로니들 → 지혈, 줄기세포 시트 → 힘줄 재생.</p>
<p class="box"><span class="tag">흐름</span>신기술도 약과 똑같이 <pk>1단계 안전성 → 2단계 유효성</pk> 순서로 전임상을 거쳐.</p>"""),
]
