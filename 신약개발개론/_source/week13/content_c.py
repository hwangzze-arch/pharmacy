# (C) 2단계 유효성 · 질환모델 사례 (슬라이드 22~32)
PAGES = [
dict(title="전임상 2단계: 유효성 (Therapeutic Efficacy)", slide="22·23", img=["s22.jpg", "s23.jpg"],
     sub="Preclinical research 2nd step: efficacy",
     kw=["안전성 다음 = 효능", "세포주 · 일차세포", "생쥐 · 랫드 · 토끼", "질환 모델"],
     sum="안전성이 확인되면 <b>2단계 치료 효능</b>을 봐. 표적 장기(뇌·폐·간·피부·뼈 등)에 맞는 <b>세포(in vitro)</b>와 <b>동물 질환 모델(in vivo)</b>로 평가해. 생쥐는 종양·상처·골다공증, 랫드는 뼈·상처·힘줄, 토끼는 골관절염 모델에 써.",
     lab="슬라이드 내용",
     tr="""<p><b>22</b> 전임상 안전성 다음 단계 = <b>Therapeutic Efficacy</b>(뇌·두개골·식도·폐·위·간·신장·심장·림프·혈관·장·근육·뼈·신경·방광 등)</p>
<p><b>23</b> 효능 평가에 쓰는 모델</p>
<ul><li><b>세포</b>: 상피세포(HaCaT) · 중간엽세포(HDF·3T3-L1·C2C12) · 종양 세포주(RENCA·PANC02·Huh7·MCF7 등) · 일차 분리 세포(ADSC·PBMC 등)</li>
<li><b>생쥐</b>: 생체적합성(피하 이식) · 종양 모델(피하·동소이식) · 상처 모델(피부·근육·말초신경) · 내분비(골다공증)</li>
<li><b>랫드</b>: 생체적합성 · 뼈(두개골 결손·경골 미세골절) · 상처(피부·근육·신경·힘줄)</li>
<li><b>토끼</b>: 골관절염 모델(미세골절)</li></ul>""",
     ex="""<p>동물 크기에 따라 모델이 달라: 작은 생쥐는 종양·피부, 조금 큰 랫드는 뼈·힘줄, 관절이 큰 <b>토끼는 골관절염</b>.</p>
<p>이어지는 사례(24~31)는 모두 이 구조야: <g>질환 → 신기술 → in vitro 시험 → in vivo 동물 모델 → 조직병리 평가</g>.</p>
<p class="box"><span class="tag">시험 포인트</span>골관절염 모델 = <pk>토끼</pk>, 종양 모델 = 생쥐. 동물-모델 짝을 물을 수 있어.</p>"""),

dict(title="유효성 사례 ① 상처 치유 전자 패치 · 신경병증 통증 전극", slide="24·25", img=["s24.jpg", "s25.jpg"],
     sub="Case: ePatch for infected wounds · drug-coated neural electrode",
     kw=["ePatch (전기장)", "감염 상처 · 생쥐", "CsA 코팅 전극", "신경병증 · 랫드"],
     sum="<b>전기장을 내는 유연 패치(ePatch)</b>는 in vitro 상처 긁기 시험과 생쥐 상처·감염 상처 모델로 상처 치유·항균 효과를 검증했어. <b>사이클로스포린A(CsA) 전도성 코팅 신경 전극</b>은 랫드 말초신경병증 모델에서 전기 자극·기록과 조직병리로 검증했어.",
     lab="슬라이드 내용",
     tr="""<p><b>24 Skin: Flexible electrical patch for wound healing</b> (생쥐 모델, Biomaterials 2022)</p>
<ul><li>전기장을 만드는 유연 다기능 ePatch</li>
<li>in vitro 상처 긁기(scratch) 시험 → in vivo 상처 치유 · <b>감염 상처</b> 치유 시험</li>
<li>→ 감염 상처에 대한 <b>상처 치유 촉진·항균</b> 솔루션으로 검증</li></ul>
<p><b>25 Neuropathic pain: Drug-coated Neural electrode</b> (랫드 모델)</p>
<ul><li>말초신경병증 · 사이클로스포린A(CsA) 전도성 코팅 전극</li>
<li>신경 전극 이식 → 신경전도검사 · 전기 자극 · 조직병리 평가</li>
<li>→ 전기 자극/기록 솔루션으로 검증</li></ul>""",
     ex="""<p>두 사례 모두 <b>의료기기형 신기술</b>이야(14쪽 전자 패치·의료기기).</p>
<table class="t"><tr><th>신기술</th><th>질환</th><th>동물</th></tr>
<tr><td>ePatch</td><td>(감염) 상처</td><td>생쥐</td></tr>
<tr><td>CsA 코팅 전극</td><td>신경병증 통증</td><td>랫드</td></tr></table>
<p class="box"><span class="tag">흐름</span>in vitro로 기전 확인 → 동물 모델로 효과 → 조직병리로 확인.</p>"""),

dict(title="유효성 사례 ② 탈모 플라즈마 · 비만 발아콩배아 추출물", slide="26·27", img=["s26.jpg", "s27.jpg"],
     sub="Case: non-thermal plasma for hair loss · germinated soy germ extract for obesity",
     kw=["비열 플라즈마(NTP)", "모발 재생 · 생쥐", "GSGE · 소야사포닌", "고지방식이 비만 · 생쥐"],
     sum="<b>비열 플라즈마(NTP) 장치</b>는 혈관신생 시험과 생쥐 모발 재생·조직병리로 탈모 치료 가능성을 검증했어. <b>발아콩배아 추출물(GSGE)</b>은 지방 생성 억제 시험과 생쥐 비만 모델(체중·μ-CT 지방 영상)로 항비만 효과를 검증했어.",
     lab="슬라이드 내용",
     tr="""<p><b>26 Hair loss: Non-Thermal Plasma (NTP)</b> (생쥐, RSC Advances 2021)</p>
<ul><li>탈모(alopecia) · 모발 성장을 돕는 NTP 발생 장치</li>
<li>in vitro 혈관신생 시험 → in vivo 모발 재생 시험(Day 0·7·14) → 조직병리(β-catenin·IGF-1·CD31)</li></ul>
<p><b>27 Obesity: Germinated Soy Germ Extract</b> (생쥐)</p>
<ul><li>발아콩배아 추출물(GSGE)의 생리활성 성분(소야사포닌 Ab)</li>
<li>in vitro 지방 생성(lipogenesis) 시험 → in vivo 비만 모델(대조·고지방식이·GSGE) → 체중 · μ-CT(노랑 = 지방)</li>
<li>→ 항비만 치료 성분으로 검증</li></ul>""",
     ex="""<p>장치(NTP)와 천연물(GSGE)도 같은 전임상 틀로 평가해. 천연물은 3주차 <b>천연물신약</b>과 연결돼.</p>
<table class="t"><tr><th>신기술</th><th>질환</th><th>동물 · 핵심 지표</th></tr>
<tr><td>NTP 장치</td><td>탈모</td><td>생쥐 · 모발 재생</td></tr>
<tr><td>GSGE</td><td>비만</td><td>생쥐 · 체중·지방(μ-CT)</td></tr></table>"""),

dict(title="유효성 사례 ③ 지혈 마이크로니들 · 힘줄 재생 나노섬유", slide="28·29", img=["s28.jpg", "s29.jpg"],
     sub="Case: hemostatic microneedle array · MSC-loaded nanofiber for tendon",
     kw=["지혈 마이크로니들", "간 출혈 모델 · 랫드", "MSC 탑재 나노섬유", "아킬레스건 · 랫드"],
     sum="<b>지혈 마이크로니들 배열</b>은 혈액 응고 시험과 랫드 간 출혈 모델로 출혈 조절 효과를 검증했어. <b>줄기세포(MSC)를 실은 실크/GelMA 나노섬유</b>는 유전자 발현 분석과 랫드 아킬레스건 재생 모델로 힘줄 파열 재생 솔루션을 최적화했어.",
     lab="슬라이드 내용",
     tr="""<p><b>28 Bleeding: Hemostatic microneedle array</b> (랫드)</p>
<ul><li>출혈 부위에 붙이면 혈전 형성</li>
<li>혈액 응고 시험(시간별) → in vivo <b>간 출혈 모델</b> → 효과적인 출혈 조절로 검증</li></ul>
<p><b>29 Tendon: MSC-loaded Electrospun nanofiber</b> (랫드, Small 2022)</p>
<ul><li>아킬레스건 손상 · MSC를 실은 실크 피브로인/GelMA 공동 전기방사 나노섬유</li>
<li>in vitro 유전자 발현 분석(MSC) → in vivo 힘줄 재생 시험(2·4주) → 힘줄 파열 재생 솔루션 최적화</li></ul>""",
     ex="""<table class="t"><tr><th>신기술</th><th>질환</th><th>동물</th></tr>
<tr><td>지혈 마이크로니들</td><td>출혈</td><td>랫드(간 출혈)</td></tr>
<tr><td>MSC 나노섬유</td><td>힘줄 파열</td><td>랫드(아킬레스건)</td></tr></table>
<p>23쪽 표와 맞춰 봐: 힘줄·상처는 <b>랫드</b> 모델이야.</p>"""),

dict(title="유효성 사례 ④ 연골 3D 프린팅 지지체 · 흑색종 pH 반응 항암제", slide="30·31", img=["s30.jpg", "s31.jpg"],
     sub="Case: 3D printed scaffold for cartilage · pH-responsive chemotherapy for melanoma",
     kw=["하이브리드 바이오잉크", "골관절염 · 토끼", "DOX-STB 하이드로겔", "B16F10 흑색종 · 생쥐"],
     sum="<b>세포를 담은 3D 프린팅 지지체(PCL·콜라겐)</b>는 토끼 골관절염 모델과 조직병리로 연골 재생을 최적화했어. <b>독소루비신을 담은 젤라틴/실리케이트 하이드로겔(DOX-STB)</b>은 산성(종양) 환경에서 약을 더 내보내는 pH 반응형으로, 생쥐 흑색종 모델에서 효과를 확인했어.",
     lab="슬라이드 내용",
     tr="""<p><b>30 Cartilage: 3D printed cell-laden scaffold</b> (토끼)</p>
<ul><li>관절 연골 · 3D 프린팅 세포 담지 지지체(PCL:콜라겐) 세 종류 비교</li>
<li><b>토끼 골관절염 모델</b> → 조직병리(H&amp;E·Safranin-O) → 골관절염 재생 솔루션 최적화</li></ul>
<p><b>31 Melanoma: pH-responsive chemotherapy</b> (생쥐)</p>
<ul><li>악성 흑색종 · 독소루비신 탑재 젤라틴/실리케이트 복합 하이드로겔(DOX-STB)</li>
<li><b>pH 반응 DOX 방출</b>(산성에서 방출↑) → B16F10 흑색종 모델 → 생존율·조직병리</li></ul>""",
     ex="""<p><b>pH 반응형</b>이 핵심: 종양 주변은 산성이라, 산성에서 약을 더 내놓으면 종양에 집중되고 정상 조직 노출은 줄어(약물전달 설계 = 분포(D)와 연결).</p>
<table class="t"><tr><th>신기술</th><th>질환</th><th>동물</th></tr>
<tr><td>3D 지지체</td><td>골관절염</td><td>토끼</td></tr>
<tr><td>DOX-STB</td><td>흑색종</td><td>생쥐(B16F10)</td></tr></table>
<p class="box"><span class="tag">시험 포인트</span>골관절염 = <pk>토끼</pk> 모델이 23쪽·30쪽 두 번 나왔어.</p>"""),

dict(title="연구 접근 요약 (Summary of Research approach)", slide="32", img="s32.jpg",
     sub="From animal disease model to mechanism",
     kw=["동물 질환 모델", "기능 분석", "미세구조 평가", "기전 평가"],
     sum="전임상 유효성 연구는 <b>동물 질환 모델 → 기능 분석 → 미세구조 평가 → 병태생리 기전 평가</b>로 이어지고, 이 결과를 다시 신기술(바이오융합 솔루션)로 되돌려 개선해. 그 과정 내내 이익과 위험을 저울질해.",
     lab="슬라이드 내용",
     tr="""<ol><li><b>Animal Disease Model</b> for Human Diseases</li>
<li><b>Functional Analysis</b> (기능 분석)</li>
<li><b>Micro-structural Assessment</b> (조직 등 미세구조 평가)</li>
<li><b>Underlying Pathophysiological Mechanism Evaluation</b> (기전 평가)</li></ol>
<p>→ “Translating Scientific Findings into Bioconvergent Solutions!” (과학적 발견을 바이오융합 솔루션으로)<br>아래: 이익(질병 경과·영상·치료 기회·편의) vs 위험(단기·장기 안전성·약물감시·시판 후·임신)</p>""",
     ex="""<p>24~31쪽 사례가 모두 이 4단계를 따랐어. 예: ePatch → 상처 모델(1) → 치유 속도(2) → 조직 염색(3) → 기전(4).</p>
<p class="box"><span class="tag">흐름</span>여기까지가 <b>Non-GLP 전임상</b>. 다음부터는 동물실험의 한계와 <b>대체법</b>이야.</p>"""),
]
