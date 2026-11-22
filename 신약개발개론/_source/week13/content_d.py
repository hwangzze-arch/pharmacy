# (D) 동물실험 대체법 · Organ-on-a-chip · 간 칩 연구 (슬라이드 33~52)
PAGES = [
dict(title="FDA 현대화법 2.0 (FDA Modernization Act 2.0)", slide="33", img="s33.jpg",
     sub="New medicines need not be tested in animals",
     kw=["2022년 12월 서명", "1938년 동물시험 규정 대체", "동물 또는 비동물 시험", "의무 폐지 ✗ · 허용"],
     sum="2022년 12월 말 서명된 법으로, 신약이 FDA 승인을 받기 위해 <b>반드시 동물실험을 할 필요는 없게</b> 됐어. 1938년부터의 “동물에서 안전성·효능 시험” 규정 대신, <b>동물 또는 비동물 시험</b> 뒤 임상으로 갈 수 있어. 다만 허용일 뿐 <b>요구는 아니고</b>, FDA 독성학자들은 여전히 동물시험을 선호해.",
     lab="슬라이드 내용",
     tr="""<ul><li>신약은 FDA 승인을 받기 위해 <b>동물에서 시험할 필요가 없다</b> — 2022년 12월 말 바이든 대통령이 서명한 법</li>
<li><b>1938년</b>부터의 “잠재적 약은 동물에서 안전성·효능을 시험해야 한다”는 규정 대신, FDA가 <b>동물 또는 비동물 시험</b> 후 약물·바이오의약품을 임상시험으로 넘길 수 있게 함</li>
<li>동물실험 없이 임상을 허가하는 것을 <b>허용(allows)</b>하지만, 그렇게 하라고 <b>요구(require)하지는 않음</b></li>
<li>FDA 독성학자들은 보수적이라 동물시험을 선호 — 안락사 후 <b>모든 장기</b>에서 독성을 볼 수 있기 때문</li></ul>""",
     ex="""<p>1938년 = 2주차에 본 <b>FD&amp;C법</b>(엘릭서 설파닐아마이드 사건 → 안전성 입증 의무)과 같은 해야. 그때부터 이어진 동물시험 규정을 바꾼 거야.</p>
<table class="t"><tr><th>맞는 것</th><th>틀린 보기</th></tr>
<tr><td>동물 <b>또는</b> 비동물 시험 허용</td><td>동물실험 <b>금지</b> ✗</td></tr>
<tr><td>허용(allow) · 요구 아님</td><td>비동물 시험 <b>의무화</b> ✗</td></tr></table>
<p class="box"><span class="tag">시험 포인트</span><pk>FDA 현대화법 2.0 = 동물실험 “의무”를 없앤 것, 금지가 아님</pk>. 2022년 12월.</p>"""),

dict(title="현재 질환 모델의 한계", slide="34·35", img=["s34.jpg", "s35.jpg"],
     sub="Limitations of current disease modeling",
     kw=["생쥐 ≠ 사람", "인간화 생쥐 모델", "Human-on-a-chip", "개인 맞춤 질환 모델"],
     sum="동물 모델은 기전 연구에 유용하지만 <b>생쥐 ≠ 사람</b>이라 결과가 사람에게 그대로 옮겨지지 않아. 인간화 면역 생쥐도 한계가 있어서, 사람 세포로 만든 <b>개인 맞춤 질환 모델 = Organ-on-a-chip</b>이 대안으로 떠올라.",
     lab="슬라이드 내용",
     tr="""<p><b>34</b></p>
<ul><li>전임상 모델로 기전·경로를 찾고 치료 효과·시간 경과를 보지만, 사람 결과와 연결이 불확실 (Translational Stroke Research 2018)</li>
<li><b>생쥐 ≠ 사람</b> · 인간화 면역계 생쥐 모델(Nature Immunology 2019)도 한계</li>
<li>→ <b>Human-on-a-chip</b></li></ul>
<p><b>35</b> 사람 세포 → <b>Personalized disease model = Organ-on-a-chip</b></p>
<ul><li>미세생리 시스템(MPS): 기계적 자극·ECM, 영양 기울기·전단 응력</li>
<li>고처리량 분석·재현성: 칩 플랫폼, 기전 평가 시스템</li>
<li>→ 사람 시험(Human Testing?)에 더 가까운 예측</li></ul>""",
     ex="""<p>11·12주차 “60 kg 서양 남성 기준 → 개인차”와 같은 문제의식이야. 동물은 더 다르니, <g>사람 세포 + 생리적 환경</g>을 칩에 재현하려는 거야.</p>
<p class="box"><span class="tag">흐름</span>동물 모델의 한계 → <b>사람 세포 기반 대체법(오가노이드·Organ-on-a-chip)</b>.</p>"""),

dict(title="오가노이드 vs Organ-on-a-chip", slide="36·37", img=["s36.jpg", "s37.jpg"],
     sub="Organoid vs organ-on-a-chip · organoid technology",
     kw=["오가노이드 = 줄기세포 유래 3D", "스스로 조직화", "OoC = 미세유체 칩", "고처리량 분화"],
     sum="<b>오가노이드</b> = 줄기세포에서 유래해 스스로 조직화한 작은 3차원 조직 배양체. <b>Organ-on-a-chip(OoC)</b> = 공학적으로 만든 또는 천연의 작은 조직을 <b>미세유체(microfluidic) 칩 안에서</b> 키운 시스템이야.",
     lab="슬라이드 내용",
     tr="""<p><b>36</b></p>
<ul><li><b>Organoids</b>: tiny, self-organized three-dimensional tissue cultures that are derived from <b>stem cells</b> — 줄기세포 유래, 스스로 조직화한 작은 3D 조직 배양체</li>
<li><b>Organs-on-chips (OoCs)</b>: systems containing engineered or natural miniature tissues grown inside <b>microfluidic chips</b> — 미세유체 칩 안에서 키운 작은 조직을 담은 시스템</li></ul>
<p><b>37 Organoid technology: Precise biological Response</b> — 내이·갑상선·간·장·뇌·폐·위·신장·종양 오가노이드 / 자동화 고처리량 분화(신장 오가노이드) → 분화 개선·독성 예측·다낭성 신장질환 이해·치료</p>""",
     ex="""<table class="t"><tr><th></th><th>오가노이드</th><th>Organ-on-a-chip</th></tr>
<tr><td>출발</td><td><b>줄기세포</b></td><td>공학적/천연 작은 조직</td></tr>
<tr><td>특징</td><td>스스로 조직화한 3D</td><td><b>미세유체 칩</b>에서 배양</td></tr>
<tr><td>강점</td><td>정밀한 생물학적 반응</td><td>미세생리 자극(흐름·압력)</td></tr></table>
<p class="box"><span class="tag">시험 포인트</span>정의 짝을 바꾼 보기 주의: <pk>줄기세포 → 오가노이드 / 미세유체 칩 → OoC</pk>.</p>"""),

dict(title="Organ-on-a-chip 기술 · 활용 가능성", slide="38·39", img=["s38.jpg", "s39.jpg"],
     sub="Microphysiological stimulus · potential applications",
     kw=["미세생리 자극", "Human-on-a-chip", "약물 스크리닝", "항암 3대 치료"],
     sum="Organ-on-a-chip은 혈관처럼 흐르는 채널·늘어나는 막 등으로 <b>미세생리 자극</b>을 줘서, 장기 여러 개를 연결한 Human-on-a-chip까지 만들어. 환자 유래 세포로 약물 반응·독성을 평가해 <b>화학요법·표적치료·면역치료</b> 선택에 활용할 수 있어.",
     lab="슬라이드 내용",
     tr="""<p><b>38 Organ-on-a-chip technology: Provide Microphysiological stimulus</b></p>
<ul><li>Human-on-a-chip 개념도: 혈관 내피가 깔린 채널, 늘어났다 줄어드는 막(폐 호흡 모사), 심장 근육 박동 등</li>
<li>환자 유래 세포·세포주 + 약물·배지 → 펌프 → 관류형/액적형 플랫폼 → 영상·세포 분석·바이오마커·센서</li></ul>
<p><b>39 Potential of Organoid/Organ-on-a-chip technology</b> — 오가노이드·OoC로 <b>화학요법</b>(카페시타빈·5-FU 등), <b>표적치료</b>(세툭시맙·베바시주맙 등), <b>면역치료</b>(니볼루맙·펨브롤리주맙·이필리무맙 등) 반응 예측</p>""",
     ex="""<p><b>미세생리 자극(microphysiological stimulus)</b> = 그냥 접시 배양과 달리, 몸속처럼 액체가 흐르고(전단 응력) 조직이 늘어나는 환경을 주는 것. 그래서 사람 반응을 더 잘 흉내 내.</p>
<p>39번 그림의 약 이름들은 4주차 항암제 세대(화학 → 표적 → 면역)와 연결돼.</p>"""),

dict(title="오가노이드-온-칩 · 뇌", slide="40·41", img=["s40.jpg", "s41.jpg"],
     sub="Organoid and organoid-on-a-chip · brain",
     kw=["정적 배양 한계", "동물 모델 한계", "오가노이드 장단점", "Retina-/Brain-on-a-chip"],
     sum="정적 세포 배양·동물 모델·체외 조직(ex vivo)은 각각 한계가 있고, 오가노이드도 <b>성숙 불완전·관류 없음</b> 같은 한계가 있어. 오가노이드를 칩에 넣어 관류(흐름)를 주면 생리적 구조·영양 공급이 좋아져 — 망막·뇌 오가노이드-온-칩이 예시야.",
     lab="슬라이드 내용",
     tr="""<p><b>40 Organoid and Organoid-on-a-chip</b></p>
<ul><li>정적 세포 배양 ✗: 비생리적 세포/배지 비율 · ECM 없음 · 단일 세포 종류</li>
<li><b>동물 모델 ✗</b>: 다른 (병태)생리 · 비용·수급(영장류·대형동물) · <b>윤리 문제</b></li>
<li>체외 조직 ✗: 짧은 수명 · 수급 제한 · 공여자 차이</li>
<li>오가노이드 ＋ 복잡한 조직·장기 배양·윤리 문제 없음 / ✗ <b>성숙 불완전 · 관류 없음</b></li>
<li><b>Retina-on-a-chip</b> ＋ ECM 포함 생리 구조 · 혈관 유사 관류 · 지속적 배지 공급 · 기계적 안정성</li></ul>
<p><b>41 Organoid-on-a-chip: Brain</b> — 사람 iPSC → 배아체(EB) → 신경상피 → 뇌 오가노이드, 관류 채널이 있는 칩에서 키움(D3~D33)</p>""",
     ex="""<table class="t"><tr><th>모델</th><th>주요 한계</th></tr>
<tr><td>정적 배양</td><td>ECM 없음 · 단일 세포</td></tr>
<tr><td>동물 모델</td><td>사람과 다른 생리 · 비용 · <b>윤리</b></td></tr>
<tr><td>오가노이드</td><td>성숙 불완전 · <b>관류 없음</b></td></tr>
<tr><td>오가노이드-온-칩</td><td>→ 관류·영양 공급으로 보완</td></tr></table>
<p class="box"><span class="tag">시험 포인트</span>오가노이드의 한계 = <pk>관류(perfusion) 없음</pk> → 칩으로 보완.</p>"""),

dict(title="Organ-on-a-chip의 조직 출처 · 구조", slide="42·43", img=["s42.jpg", "s43.jpg"],
     sub="Tissue sources and chip structures",
     kw=["ESC · ASC · iPSC", "일차세포 · 세포주", "단일·이중·다중 채널", "다공성 막"],
     sum="칩에 넣는 세포는 <b>배아줄기세포(ESC)·성체줄기세포(ASC)·유도만능줄기세포(iPSC)·일차세포(조직 생검)·세포주</b>가 있고 각각 장단점이 있어. 칩 구조는 단일 채널부터 다공성 막으로 나눈 이중(평행·샌드위치)·다중 채널까지 있어.",
     lab="슬라이드 내용",
     tr="""<p><b>42 Tissue sources for OOAC devices</b></p>
<ul><li><b>ESC</b>(배반포 유래) · <b>ASC</b>(성체 줄기세포) · <b>iPSC</b>(유도만능줄기세포) · <b>Primary cells</b>(조직 생검) · <b>Cell lines</b>(종양 유래 등)</li>
<li>각각 장단점(얻기 쉬움·성숙도·재현성·윤리 등)이 겹치는 벤 다이어그램 · 2D vs 3D 배양</li></ul>
<p><b>43 Organ-on-a-chip and structure</b></p>
<ul><li>Single Channel · Double Channel(Parallel / Sandwich, 다공성 막) · Multi Channel</li>
<li>혈관 기능(영양·산소 운반, 온도 조절)과 칩(3D 세포 배양, 미세유체, 장기 기능 모사)의 공통점</li></ul>""",
     ex="""<p>줄기세포 약어를 정리해 둬:</p>
<table class="t"><tr><th>약어</th><th>뜻</th></tr>
<tr><td>ESC</td><td>Embryonic stem cell, 배아줄기세포</td></tr>
<tr><td>ASC</td><td>Adult stem cell, 성체줄기세포</td></tr>
<tr><td>iPSC</td><td>induced Pluripotent Stem Cell, 유도만능줄기세포</td></tr></table>
<p>이중 채널(샌드위치)은 <b>다공성 막</b>으로 두 세포층을 나눠, 장벽(예: 혈관-조직)을 흉내 내.</p>"""),

dict(title="간 미세생리 · 연구 접근", slide="44·45·46", img=["s44.jpg", "s46.jpg"],
     sub="Liver microphysiology · research approach (Small, 2021)",
     kw=["실질 + 비실질 세포", "간 주요 4세포", "GelMA 10~20 kPa", "FFA → NAFLD 단계"],
     sum="간에서 일어나는 일을 연구하려면 <b>실질세포(간세포)와 비실질세포</b>를 함께 봐야 해. 그래서 <b>간의 주요 4세포(간세포·HUVEC·쿠퍼세포·성상세포)</b>로 3D 구형체를 만들어 GelMA(10~20 kPa)에 넣고, 유리지방산(FFA)으로 지방간 → 지방간염 → 섬유화를 단계적으로 유도해. 관류형 칩(유속 200 μl/시간)에서 배양해.",
     lab="슬라이드 내용",
     tr="""<p><b>44 Liver microphysiology</b> — 손상된 간세포 → DAMPs → 성상세포(HSC) 활성화·ECM 침착, 쿠퍼세포·단핵구·T세포·혈관 내피세포 상호작용<br>“간의 생물학적 현상을 연구하려면 <b>실질세포와 비실질세포를 모두</b> 분석해야 한다.” (Cells 2020)</p>
<p><b>45·46 Research approach</b> (HJ Cho &amp; H-J Kim et al., Small 2021)</p>
<ul><li>간의 <b>주요 4세포</b>로 만든 3D 구형체: 간세포 · HUVEC(혈관 내피) · 쿠퍼세포 · 성상세포</li>
<li>GelMA(10~20 kPa) 속 간 미세조직</li>
<li>FFA → 지방증(Steatosis) → 지방간염 → 섬유화 동반 지방간염 → 섬유화 간 미세조직</li>
<li>관류형 생물반응기 칩 · 유속 200 μl/hour</li></ul>""",
     ex="""<table class="t"><tr><th>세포</th><th>역할</th></tr>
<tr><td>간세포(HepaRG)</td><td>실질세포 · 알부민 분비 등 간 기능</td></tr>
<tr><td>HUVEC</td><td>혈관 내피</td></tr>
<tr><td>쿠퍼세포</td><td>간의 대식세포 · 염증</td></tr>
<tr><td>성상세포(HSC)</td><td>활성화되면 섬유화(ECM 침착)</td></tr></table>
<p>교수님 연구실 논문이야. 12주차 녹취에서 말한 “대사질환·간 칩” 연구가 이거야.</p>
<p class="box"><span class="tag">시험 포인트</span>간 칩 = <pk>실질 + 비실질 세포를 함께</pk> 넣어야 하는 이유.</p>"""),

dict(title="다세포 간 칩 · HUVEC/쿠퍼세포의 영향", slide="47·48·49", img=["s47.jpg", "s49.jpg"],
     sub="Multicellular liver-on-a-chip · effects of HUVEC and Kupffer cells",
     kw=["세포별 색 표지", "HUVEC → 알부민↑ · 가역성", "쿠퍼세포 → 지질↑ · ROS↑", "NAFLD 진행"],
     sum="세포마다 다른 색으로 표지해 다세포 간 미세조직을 만들었어. <b>HUVEC</b>은 간세포의 <b>알부민 분비를 늘리고 지질 축적을 되돌리는(가역성)</b> 데 기여했고, <b>쿠퍼세포</b>는 간세포 기능엔 유의한 영향이 없었지만 <b>지질 축적과 ROS(염증)를 늘렸어</b>.",
     lab="슬라이드 내용",
     tr="""<p><b>47 Multicellular Liver-on-a-chip</b> — HepaRG·HUVEC·쿠퍼세포·성상세포를 비율별(100% → 61:13:13:13)로 섞어 구형체 형성(Day 1~4) → 간 병태생리 연구용 다세포 미세조직</p>
<p><b>48·49 Effect of HUVEC/Kupffer cells</b></p>
<ul><li><b>HUVEC</b> → 간세포 <b>알부민 분비↑</b> · 지질 축적의 <b>가역성↑</b><br>“HUVEC은 NAFLD 진행 중 간세포 기능과 지질 축적 가역성에 영향을 준다”</li>
<li><b>쿠퍼세포</b> → 간세포 기능엔 <b>유의차 없음(n.s.)</b> · <b>지질 축적↑ · ROS 발현↑</b><br>“쿠퍼세포는 NAFLD 진행 중 지질 축적과 염증에 영향을 준다”</li></ul>""",
     ex="""<table class="t"><tr><th>세포</th><th>간세포 기능</th><th>지질 축적</th><th>염증(ROS)</th></tr>
<tr><td>HUVEC</td><td>알부민↑</td><td>가역성↑</td><td>—</td></tr>
<tr><td>쿠퍼세포</td><td>n.s.</td><td>↑</td><td>↑</td></tr></table>
<p>NAFLD = 비알코올성 지방간 질환. 세포 하나만 넣으면 이런 상호작용을 볼 수 없어서 <b>다세포 칩</b>이 필요해.</p>"""),

dict(title="성상세포의 영향 · 약물 시험 · 요약", slide="50·51·52", img=["s51.jpg", "s52.jpg"],
     sub="Stellate cells · drug testing · personalized disease model",
     kw=["성상세포 → 지질·염증·섬유화", "농도 기울기 칩", "피르페니돈(항섬유화)", "개인 맞춤 질환 모델"],
     sum="<b>성상세포</b>는 지질 축적·염증(IL-6)·<b>섬유화(TGF-β)</b>에 모두 영향을 줬어. 농도 기울기 칩으로 항섬유화제 <b>피르페니돈</b>을 시험하니, FFA로 유도한 모델이 생체와 비슷한 약물 반응을 보였어 → 이 다세포 간 칩은 <b>후보물질 평가에 더 적합</b>해. 결론: 사람 세포 + 3D 구조 + 미세유체 = 개인 맞춤 질환 모델.",
     lab="슬라이드 내용",
     tr="""<p><b>50 Effects of Stellate Cells (HSCs)</b> — 성상세포 → 지질 축적 · 염증(IL-6 분비) · <b>섬유화</b>(TGF-β)<br>“성상세포는 NAFLD 진행 중 지질 축적, 염증, 섬유화에 영향을 준다”</p>
<p><b>51 Drug testing and Mechanism evaluation</b></p>
<ul><li>농도 기울기 생성 미세유체 장치 · 약물: <b>Pirfenidone</b>(항섬유화제) → αSMA 발현</li>
<li>FFA로 유도한 NAFLD → <b>생체와 비슷한 약물 반응</b> 및 질환 진행(지질 축적 + 염증 + 섬유화) 재현</li>
<li>→ “이 다세포 간 칩 모델은 <b>약물 후보 평가에 더 적합</b>할 수 있다”</li></ul>
<p><b>52 Summary: Personalized Disease Model</b> — 사람 세포 → 3D 세포 구조 → 미세유체 → 약물 처리에 따른 기전 → Organ-on-a-chip</p>""",
     ex="""<p>세 세포 정리 (48~50쪽):</p>
<table class="t"><tr><th>세포</th><th>NAFLD에서 영향</th></tr>
<tr><td>HUVEC</td><td>간세포 기능 · 지질 가역성</td></tr>
<tr><td>쿠퍼세포</td><td>지질 축적 · 염증</td></tr>
<tr><td>성상세포</td><td>지질 축적 · 염증 · <b>섬유화</b></td></tr></table>
<p class="box"><span class="tag">결론</span>Organ-on-a-chip = <pk>사람 세포 + 3D 구조 + 미세유체</pk>로 만든 <b>개인 맞춤 질환 모델</b> → 동물실험 대체·보완(FDA 현대화법 2.0과 연결).</p>"""),
]
