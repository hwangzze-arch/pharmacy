PAGES = [
# 34
dict(img=34, slide=34, title="체순환 모세혈관에서의 O₂·CO₂ 교환", sub="O₂ and CO₂ exchange across systemic capillaries",
kw=["조직 P_O2 < 40", "조직 P_CO2 > 46", "동맥혈 100/40"],
sum="조직세포는 O₂를 계속 쓰고 CO₂를 계속 만들어서 P<sub>O2</sub> &lt; 40, P<sub>CO2</sub> &gt; 46이다. 100/40의 동맥혈이 도착하면 O₂는 조직으로, CO₂는 혈액으로 확산하고, 혈액은 40/46의 정맥혈이 되어 떠난다.",
tr="""<ul><li>❺ O₂를 소비하고 CO₂를 만드는 조직세포에서는 P<sub>O2</sub>가 비교적 낮고 P<sub>CO2</sub>가 비교적 높다</li><li>❻ 그 결과 체순환 모세혈관에서 분압 기울기가 생겨 O₂는 혈액 → 세포로, CO₂는 세포 → 혈액으로 수동 확산된다. 세포의 대사 요구를 받쳐주면서 동시에 CO₂를 혈액으로 옮긴다</li><li>❼ 조직세포와 평형을 이룬 뒤 조직을 떠나는 혈액은 O₂가 비교적 낮고 CO₂가 높다</li><li>❽ 이 혈액은 폐로 돌아가 다시 O₂를 채우고 CO₂를 버린다</li><li>조직세포: Food + O₂ → CO₂ + H₂O + ATP</li></ul>""",
ex="""<table class="t"><tr><th></th><th>P<sub>O2</sub></th><th>P<sub>CO2</sub></th></tr><tr><td>도착하는 동맥혈</td><td>100</td><td>40</td></tr><tr><td>조직세포</td><td><y>&lt; 40</y></td><td><y>&gt; 46</y></td></tr><tr><td>떠나는 정맥혈</td><td>40</td><td>46</td></tr></table>
<div class="boxg">폐 vs 조직: 방향만 반대. <g>폐: O₂ → 혈액, CO₂ → 공기</g> / <g>조직: O₂ → 세포, CO₂ → 혈액</g></div>"""),
# 35
dict(img=35, slide=35, title="폐·체순환 모세혈관 가스 교환 전체 그림", sub="O₂ and CO₂ exchange across pulmonary and systemic capillaries",
kw=["❶–❽ 순서", "폐순환", "체순환"],
sum="슬라이드 33(폐)과 34(조직)를 하나로 합친 그림이다. ❶–❽의 순서로 한 바퀴 돌며 O₂와 CO₂의 분압이 어떻게 바뀌는지 따라가면 된다.",
tr="""<ul><li>❶–❹ 폐모세혈관 교환(슬라이드 33과 같음)</li><li>❺–❽ 체순환 모세혈관 교환(슬라이드 34와 같음)</li><li>숫자는 mmHg 분압</li></ul>""",
ex="""<table class="t"><tr><th>위치</th><th>P<sub>O2</sub></th><th>P<sub>CO2</sub></th></tr><tr><td>대기</td><td>160</td><td>0.23</td></tr><tr><td>폐포</td><td>100</td><td>40</td></tr><tr><td>폐정맥 → 체동맥</td><td>100</td><td>40</td></tr><tr><td>조직</td><td>&lt;40</td><td>&gt;46</td></tr><tr><td>체정맥 → 폐동맥</td><td>40</td><td>46</td></tr></table>
<div class="box"><span class="tag">시험 포인트</span>그림 빈칸(A/B/C)에 숫자를 넣는 문제로 나오기 가장 좋은 그림.</div>"""),
# 36
dict(img=36, slide=36, title="분압 기울기 이외의 요인", sub="Factors other than partial pressure gradient (Table 13-5)",
kw=["표면적 ↑", "두께 ↑ → 속도 ↓", "확산상수 CO₂ = O₂의 20배", "폐기종", "폐부종·섬유증"],
sum="폐포–모세혈관 막을 지나는 가스 이동 속도는 분압 기울기(가장 중요), 표면적, 막 두께, 확산상수에 달려 있다. 표면적·기울기·확산상수는 클수록, 두께는 얇을수록 빠르다.",
tr="""<ul><li><b>표 13-5 폐포–모세혈관 막을 지나는 가스 이동 속도에 영향을 주는 요인</b></li><li><b>O₂·CO₂ 분압 기울기</b>: 기울기 ↑ → 속도 ↑ / 이동 속도의 주된 결정 요인</li><li><b>폐포–모세혈관 막의 표면적</b>: 면적 ↑ → 속도 ↑ / 휴식 시 일정, 운동 중 증가, <b>폐기종·폐허탈</b> 같은 병적 상태에서 감소</li><li><b>폐포–모세혈관 막의 두께</b>: 두께 ↑ → 속도 ↓ / 보통 일정, <b>폐부종·폐섬유증·폐렴</b>에서 증가</li><li><b>확산상수</b>: 상수 ↑ → 속도 ↑ / <b>CO₂의 확산상수는 O₂의 20배</b>라 CO₂의 작은 분압 기울기를 상쇄 → O₂와 CO₂가 거의 같은 양으로 교환된다</li></ul>""",
ex="""<div class="boxg">픽의 확산 법칙: <g>이동 속도 ∝ (분압 차 × 표면적 × 확산상수) / 두께</g></div>
<table class="t"><tr><th>질환</th><th>바뀌는 요인</th></tr><tr><td>폐기종</td><td>표면적 ↓ (폐포 벽 파괴)</td></tr><tr><td>폐부종·섬유증·폐렴</td><td>두께 ↑</td></tr></table>
<div class="box"><span class="tag">시험 포인트</span>"두께가 증가하면 이동 속도가 증가한다" → <b>X</b>. "CO₂ 확산상수 20배" 숫자 기억.</div>"""),
# 37
dict(img=37, slide=37, title="13.4 가스 운반 (섹션 표지)", sub="13.4 Gas Transport",
kw=["가스 운반"],
sum="네 번째 절: 혈액이 O₂와 CO₂를 어떤 형태로 실어 나르는가.",
tr="""<ul><li><b>13.4 가스 운반</b></li></ul>""",
ex="""<table class="t"><tr><th>가스</th><th>운반 형태</th></tr><tr><td>O₂</td><td>용해 1.5% / <y>Hb 결합 98.5%</y></td></tr><tr><td>CO₂</td><td>용해 10% / Hb 결합 30% / <y>HCO₃⁻ 60%</y></td></tr></table>"""),
# 38
dict(img=38, slide=38, title="가스 운반 — O₂의 두 가지 형태", sub="Gas transport",
kw=["용해 O₂ 1.5%", "헤모글로빈 결합", "가역적 결합"],
sum="혈액 속 O₂는 대부분 <b>헤모글로빈(Hb)</b>에 붙어 운반된다. O₂는 물에 잘 녹지 않아 혈장에 녹아 있는 것은 1.5%뿐이다.",
tr="""<ul><li>폐에서 혈액이 받은 산소와 세포가 만든 이산화탄소는 운반되어야 한다</li><li>혈액 속 산소는 대부분 <b>헤모글로빈에 결합</b>해 운반된다</li><li>혈액 속 산소의 두 가지 형태<ul><li><b>물리적으로 용해된 O₂</b>: O₂는 잘 녹지 않아 혈장에 조금만 녹는다(<b>1.5%</b>)</li><li><b>헤모글로빈에 결합한 O₂</b>: Hb는 적혈구 안의 철 함유 단백질로, 산소와 쉽게 되돌릴 수 있는(가역적) 결합을 한다</li></ul></li><li>그림: 헤모글로빈 분자(α·β 사슬 4개), 헴(heme) 그룹, 철 원자</li></ul>""",
ex="""<div class="boxg"><g>Hb + O₂ ⇌ HbO₂</g> (가역) — 폐에서는 오른쪽, 조직에서는 왼쪽으로.</div>
<p>용해된 O₂는 양은 적지만 <y>P<sub>O2</sub>를 결정</y>하는 것은 바로 이 용해된 O₂다. Hb는 P<sub>O2</sub>에 반응해 O₂를 붙잡거나 놓는다.</p>
<p class="note">11장 연결: 적혈구 1개당 Hb 약 2억 5천만 개, Hb 1개 = 글로빈 4사슬 + 헴 4개.</p>"""),
# 39
dict(img=39, slide=39, title="P_O2와 Hb 포화도 — O₂–Hb 해리곡선", sub="Gas transport",
kw=["Hb 1개 = O₂ 4개", "% 포화도", "S자 곡선", "평탄부(폐)", "급경사부(조직)"],
sum="Hb 하나는 헴 4개의 철마다 O₂ 하나씩, 최대 4개를 싣는다. Hb가 얼마나 차 있는지(% 포화도)를 정하는 주된 요인은 P<sub>O2</sub>다. 곡선은 S자 모양으로, 위쪽 <b>평탄부</b>는 폐에서 싣기에, 가운데 <b>급경사부</b>는 조직에서 내려놓기에 유리하다.",
tr="""<ul><li><b>P<sub>O2</sub>는 Hb 포화도를 결정하는 주된 요인</b>이다<ul><li>한 Hb에 있는 헴 4개의 철 원자 각각이 O₂ 하나와 결합할 수 있다</li><li>Hb 하나는 O₂를 최대 4개 운반한다</li><li>Hb 포화도(%): Hb가 O₂와 결합한 정도(3/4 = 75%)</li><li>P<sub>O2</sub>(혈액 속 O₂의 존재)가 % Hb 포화도를 정하는 주 요인</li></ul></li><li><b>O₂–Hb 해리곡선은 두 구간</b>을 가진다<ul><li><b>평탄부</b>: 폐에서 O₂ 싣기에 유리 — 폐포 P<sub>O2</sub>가 어느 정도 떨어져도 Hb가 높은 포화도를 유지</li><li><b>급경사부</b>: 조직에서 O₂ 내려놓기에 유리 — 조직 P<sub>O2</sub>가 조금만 떨어져도 Hb가 많은 O₂를 내놓음</li></ul></li><li>그래프: 체순환 모세혈관 평균 휴식 P<sub>O2</sub>(40) / 폐모세혈관 정상 P<sub>O2</sub>(100)</li></ul>""",
ex="""<table class="t"><tr><th>P<sub>O2</sub> (mmHg)</th><th>Hb 포화도</th><th>위치</th></tr><tr><td>100</td><td><y>~97.5%</y></td><td>폐(평탄부)</td></tr><tr><td>60</td><td>~90%</td><td>아직 평탄 — 안전 여유</td></tr><tr><td>40</td><td><y>~75%</y></td><td>휴식 조직(급경사부)</td></tr></table>
<div class="boxg">휴식 시 조직에서 Hb는 O₂의 약 1/4만 내려놓는다 → 나머지 75%는 <g>예비 저장분</g>(운동 시 사용).</div>
<div class="box"><span class="tag">시험 포인트</span>평탄부 = <b>loading(폐)</b>, 급경사부 = <b>unloading(조직)</b>. 그래프 A/B 라벨 문제 단골.</div>"""),
# 40
dict(img=40, slide=40, title="헤모글로빈은 O₂ 전달을 돕는다", sub="Hemoglobin facilitates oxygen transfer",
kw=["저장고(depot)", "분압 기울기 유지", "빠른 방출"],
sum="Hb가 녹아 있는 O₂를 계속 빨아들여 혈장 P<sub>O2</sub>를 낮게 유지하기 때문에, 폐포 → 혈액의 분압 기울기가 오래 유지되어 훨씬 많은 O₂가 넘어온다. 조직에서는 반대로 Hb가 O₂를 빠르게 풀어준다.",
tr="""<ul><li>(a) 폐포 P<sub>O2</sub> = 혈액 P<sub>O2</sub> (Hb 없을 때 — 금방 평형)</li><li>(b) 폐포 P<sub>O2</sub> &gt; 혈액 P<sub>O2</sub> (Hb가 녹은 O₂를 붙잡아 기울기 유지)</li><li>(c) 폐포 P<sub>O2</sub> = 혈액 P<sub>O2</sub> (Hb가 모두 포화된 뒤에야 평형)</li><li>범례: O₂ 분자 / 부분 포화 Hb / 완전 포화 Hb</li><li>폐포 수준의 Hb: <b>O₂의 저장고</b></li><li>조직 수준의 Hb: <b>빠른 O₂ 방출</b></li></ul>""",
ex="""<div class="boxg">Hb = <g>O₂ 스펀지</g>. 녹은 O₂를 흡수 → 혈장 P<sub>O2</sub>가 바로 오르지 않음 → 기울기 유지 → 더 많은 O₂ 유입.</div>
<p class="note">Hb가 없다면 혈액 1 L가 운반하는 O₂는 약 3 mL, Hb가 있으면 약 200 mL — 약 65배.</p>"""),
# 41
dict(img=41, slide=41, title="조직에서 O₂ 방출을 촉진하는 요인 — 오른쪽 이동", sub="Factors at the tissue level promoting O₂ unloading",
kw=["CO₂ ↑", "pH ↓(H⁺ ↑)", "보어 효과", "온도 ↑", "2,3-BPG", "오른쪽 이동"],
sum="조직의 CO₂ ↑, 산성(pH ↓), 온도 ↑, 2,3-BPG ↑는 O₂–Hb 곡선을 <b>오른쪽으로</b> 옮긴다. 같은 P<sub>O2</sub>에서 Hb의 O₂ 친화력이 떨어져 조직에 O₂를 더 많이 내려놓는다. CO₂·pH에 의한 이동을 <b>보어 효과</b>라 한다.",
tr="""<ul><li>조직의 다음 요인들은 O₂–Hb 해리곡선을 <b>오른쪽으로</b> 이동시킨다<ul><li><b>Hb의 O₂ 친화력을 낮추고 조직으로의 O₂ 방출을 촉진</b></li></ul></li><li><b>CO₂ 증가</b></li><li><b>pH 감소</b>(산성 환경)</li><li><b>보어 효과</b><ul><li>CO₂ 농도나 환경 pH의 변화로 일어나는 산소 해리곡선의 이동</li></ul></li><li><b>온도 상승</b></li><li>적혈구가 만드는 <b>2,3-비스포스포글리세르산(2,3-BPG)</b></li><li>조직 vs 폐 수준(그래프: 폐 수준의 동맥 P<sub>CO2</sub>·산도·정상 체온 곡선 vs 조직 수준의 P<sub>CO2</sub> ↑, 산(H⁺) ↑, 온도 ↑, 2,3-BPG ↑ 곡선)</li></ul>""",
ex="""<table class="t"><tr><th>오른쪽 이동(방출 ↑)</th><th>왼쪽 이동(결합 ↑)</th></tr><tr><td>CO₂ ↑, H⁺ ↑(pH ↓), 온도 ↑, 2,3-BPG ↑</td><td>CO₂ ↓, H⁺ ↓(pH ↑), 온도 ↓, 2,3-BPG ↓ (+ 태아 Hb, CO)</td></tr><tr><td>운동하는 근육, 조직</td><td>폐</td></tr></table>
<div class="boxg">암기: 운동하는 근육은 <g>뜨겁고(온도), 시고(H⁺), CO₂ 많고</g> → 오른쪽 이동 → 그 근육에 O₂를 더 많이.</div>
<div class="box"><span class="tag">시험 포인트</span>"보어 효과 = CO₂/pH에 의한 곡선 이동". 오른쪽 = 친화력 <b>감소</b>(헷갈리기 쉬움).</div>"""),
# 42
dict(img=42, slide=42, title="CO₂는 혈액에서 세 가지 방법으로 운반된다", sub="CO₂ is transported in the blood in three ways",
kw=["용해 10%", "카바미노Hb 30%", "HCO₃⁻ 60%", "탄산탈수효소"],
sum="CO₂는 ① 혈장에 녹아서(10%, O₂보다 잘 녹음) ② Hb에 붙어서(카바미노헤모글로빈, 30%) ③ <b>중탄산 이온(HCO₃⁻)</b>으로 바뀌어서(60%) 운반된다. ③은 적혈구 안의 <b>탄산탈수효소</b>가 빠르게 만든다.",
tr="""<ul><li><b>물리적 용해</b>(10%, O₂보다 많음)</li><li><b>헤모글로빈 결합</b>(30%): HbCO₂(카바미노헤모글로빈), 조직 모세혈관에서 O₂를 내준 뒤 CO₂를 받는다</li><li><b>중탄산 이온</b>(HCO₃⁻; 60%): 적혈구에 많이 들어 있는 효소 <b>탄산탈수효소</b></li><li>반응식: CO₂ + H₂O ⇌(탄산탈수효소) H₂CO₃ ⇌ H⁺ + HCO₃⁻</li><li>그림: 조직 → 적혈구 안에서 CO₂ → HCO₃⁻ + H⁺(H⁺는 Hb가 받음, HbH), HCO₃⁻는 혈장으로 나가고 Cl⁻가 들어옴(염소 이동); 폐에서는 반대</li></ul>""",
ex="""<table class="t"><tr><th>형태</th><th>비율</th><th>메모</th></tr><tr><td>용해</td><td>10%</td><td>O₂(1.5%)보다 잘 녹음</td></tr><tr><td>카바미노Hb</td><td>30%</td><td>Hb의 <b>글로빈 부분</b>(헴 아님)에 결합</td></tr><tr><td><y>HCO₃⁻</y></td><td><y>60%</y></td><td>탄산탈수효소(적혈구 안)</td></tr></table>
<div class="boxg"><g>CO₂ + H₂O ⇌ H₂CO₃ ⇌ H⁺ + HCO₃⁻</g> — 조직에서는 오른쪽, 폐에서는 왼쪽. 생긴 H⁺는 Hb가 받아 완충(HbH).</div>
<div class="box"><span class="tag">시험 포인트</span>세 숫자(10/30/60)와 효소 이름. 11장 적혈구의 탄산탈수효소와 연결.</div>"""),
# 43
dict(img=43, slide=43, title="염소 이동 (햄버거 효과)", sub="Chloride effect or Hamburger effect",
kw=["HCO₃⁻/Cl⁻ 교환", "전기적 중성", "Band 3(AE1)", "조직: H⁺ 흡수", "폐: H⁺ 방출"],
sum="적혈구 안에서 만들어진 HCO₃⁻가 혈장으로 나갈 때, 전기적 균형을 맞추려고 Cl⁻가 대신 들어온다. 이것이 <b>염소 이동(햄버거 효과)</b>이다. 폐에서는 정반대로 HCO₃⁻가 들어오고 Cl⁻가 나간다.",
tr="""<ul><li>CO₂ 운반 중 전기적 중성을 유지하기 위해 적혈구 막을 가로질러 <b>중탄산(HCO₃⁻)과 염소(Cl⁻) 이온을 교환</b>하는 것</li><li>탄산탈수효소 덕분에 CO₂가 중탄산 형태로 운반될 수 있다</li><li>적혈구 안에서 탄산탈수효소는 가역 반응 CO₂ + H₂O ⇌ HCO₃⁻ + H⁺ 를 빠르게 한다</li><li>혈액의 CO₂ 운반은 역수송체(antiporter)에 의해 이루어지며 세포질 pH를 조절한다</li><li>(a) <b>체순환 모세혈관</b>(CO₂ 높음, O₂ 낮음): + 양성자 흡수 — Hb의 히스티딘 잔기가 H⁺를 받고 O₂를 놓음, HCO₃⁻는 AE1 단백질을 통해 Cl⁻와 교환되어 나감</li><li>(b) <b>폐모세혈관</b>(CO₂ 낮음, O₂ 높음): + 양성자 방출 — Hb가 O₂를 받고 H⁺를 내놓음, HCO₃⁻가 Cl⁻와 교환되어 들어와 CO₂로 되돌아감</li></ul>""",
ex="""<table class="t"><tr><th></th><th>조직</th><th>폐</th></tr><tr><td>반응 방향</td><td>CO₂ → HCO₃⁻ + H⁺</td><td>HCO₃⁻ + H⁺ → CO₂</td></tr><tr><td>HCO₃⁻</td><td>적혈구 → 혈장</td><td>혈장 → 적혈구</td></tr><tr><td>Cl⁻</td><td><y>혈장 → 적혈구</y></td><td>적혈구 → 혈장</td></tr><tr><td>Hb</td><td>H⁺ 받고 O₂ 놓음</td><td>O₂ 받고 H⁺ 놓음</td></tr></table>
<div class="boxg">교환 통로 = <g>AE1(Band 3) 음이온 교환체</g>. 조직에서 Hb가 H⁺를 받는 것 = 보어 효과와 같은 현상(H⁺ ↑ → O₂ 방출).</div>
<div class="box"><span class="tag">시험 포인트</span>"염소 이동의 목적은?" → <b>전기적 중성 유지</b>. 정맥혈 적혈구는 Cl⁻가 더 많다.</div>"""),
# 44
dict(img=44, slide=44, title="호흡기 질환 용어 — 임상 호흡 상태 미니 용어집", sub="Respiratory diseases (Table 13-7)",
kw=["무호흡", "질식", "청색증", "호흡곤란", "과탄산혈증", "과다호흡 vs 과호흡", "저산소증 4종"],
sum="임상에서 쓰는 호흡 상태 용어 정리표. 특히 <b>hyperpnea(운동처럼 필요에 맞춘 환기 증가)</b>와 <b>hyperventilation(필요 이상 환기 → CO₂ ↓, 호흡성 알칼리증)</b>을 구분하자.",
tr="""<ul><li><b>Apnea(무호흡)</b>: 일시적 호흡 정지</li><li><b>Asphyxia(질식)</b>: 대기 O₂ 부족, 호흡 장애, 또는 조직의 O₂ 이용 불능으로 인한 조직의 O₂ 결핍</li><li><b>Cyanosis(청색증)</b>: 동맥혈 산소화 부족으로 피부가 푸르게 보임</li><li><b>Dyspnea(호흡곤란)</b>: 힘들거나 어려운 호흡</li><li><b>Eupnea(정상호흡)</b>: 정상 호흡</li><li><b>Hypercapnia(과탄산혈증)</b>: 동맥혈 CO₂ 과다</li><li><b>Hyperpnea(호흡항진)</b>: 운동처럼 대사 요구 증가에 맞춘 폐환기 증가</li><li><b>Hyperventilation(과환기)</b>: 대사 요구를 넘는 폐환기 증가 → P<sub>CO2</sub> 감소, 호흡성 알칼리증</li><li><b>Hypocapnia(저탄산혈증)</b>: 동맥혈 CO₂ 정상 이하</li><li><b>Hypoventilation(저환기)</b>: 대사 요구에 비해 부족한 환기 → P<sub>CO2</sub> 증가, 호흡성 산증</li><li><b>Hypoxia(저산소증)</b>: 세포 수준의 O₂ 부족<ul><li><b>빈혈성</b>: 혈액의 O₂ 운반 능력 감소</li><li><b>순환성</b>: 산소화된 혈액이 조직에 너무 적게 전달됨(정체성 저산소증)</li><li><b>조직독성</b>: 세포가 가용 O₂를 사용하지 못함</li><li><b>저산소혈성</b>: 동맥혈 P<sub>O2</sub>가 낮고 Hb 포화도 부족</li></ul></li><li><b>Respiratory arrest(호흡정지)</b>: 영구적 호흡 정지(교정하지 않으면)</li><li><b>Suffocation(질식)</b>: 숨을 쉬지 못해 생기는 O₂ 결핍</li></ul>""",
ex="""<table class="t"><tr><th></th><th>환기</th><th>P<sub>CO2</sub></th><th>pH</th></tr><tr><td>Hyperpnea</td><td>↑ (필요만큼)</td><td>정상</td><td>정상</td></tr><tr><td><y>Hyperventilation</y></td><td>↑↑ (필요 이상)</td><td>↓</td><td>↑ 호흡성 알칼리증</td></tr><tr><td><y>Hypoventilation</y></td><td>↓</td><td>↑</td><td>↓ 호흡성 산증</td></tr></table>
<p class="note">조직독성 저산소증의 예: 시안화물(사이토크롬 산화효소 억제).</p>"""),
# 45
dict(img=45, slide=45, title="13.5 호흡 조절 (섹션 표지)", sub="13.5 Control of Respiration",
kw=["호흡 조절"],
sum="마지막 절: 뇌간이 호흡 리듬을 만들고, 화학수용기가 P<sub>O2</sub>·P<sub>CO2</sub>·H⁺를 감지해 환기량을 조절한다.",
tr="""<ul><li><b>13.5 호흡 조절</b></li></ul>""",
ex="""<p>핵심 세 가지: ① 리듬 = <y>연수</y>(프리뵈트징거 복합체) ② 미세조정 = <y>교뇌</y> ③ 크기 조절 = <y>화학수용기</y>(가장 중요한 입력은 P<sub>CO2</sub>).</p>"""),
# 46
dict(img=46, slide=46, title="호흡 조절 — 리듬은 뇌간에서", sub="Control of respiration",
kw=["뇌간 호흡중추", "신경 지배 필수", "수의적 조절"],
sum="심장처럼 호흡도 끊임없이 반복되지만, 심장과 달리 호흡근은 스스로 박동하지 못한다. <b>뇌간의 호흡중추</b>가 신경 신호를 리듬 있게 보내야 숨을 쉰다. 말할 때처럼 의지로 바꿀 수도 있다.",
tr="""<ul><li>심장 박동처럼 호흡도 생명 유지를 위해 연속적·주기적으로 일어난다</li><li>심장근처럼 들숨근도 리듬 있게 수축·이완하여 폐를 채우고 비운다</li><li><b>뇌간의 호흡중추</b>가 리듬 있는 호흡 패턴을 만든다<ul><li>심장의 박동조율 활동과 달리, 호흡근의 리듬 수축에는 <b>주기적 신경 활동</b>이 필요하다</li><li>호흡계로 가는 신경 공급은 호흡을 유지하고 O₂·CO₂ 요구 변화에 맞춰 유연하게 조절하는 데 필수다</li><li>말하거나 의도할 때처럼 호흡 활동은 <b>수의적으로 바꿀 수 있다</b></li></ul></li></ul>""",
ex="""<table class="t"><tr><th></th><th>심장</th><th>호흡근</th></tr><tr><td>근육 종류</td><td>심장근</td><td><y>골격근</y></td></tr><tr><td>리듬의 근원</td><td>자체 박동조율(SA 결절)</td><td><y>뇌간 신경</y>(프리뵈트징거)</td></tr><tr><td>신경 끊으면</td><td>계속 뜀</td><td><y>호흡 정지</y></td></tr></table>
<div class="box"><span class="tag">시험 포인트</span>"호흡근은 심장근처럼 자체 박동조율 능력이 있다" → <b>X</b>.</div>"""),
# 47
dict(img=47, slide=47, title="호흡의 신경 조절 구성요소", sub="Components of neural control of respiration",
kw=["연수 호흡중추", "DRG(등쪽호흡군)", "VRG(배쪽호흡군)", "프리뵈트징거 복합체", "호흡조절중추(pneumotaxic)", "지속흡식중추(apneustic)"],
sum="연수의 <b>등쪽호흡군(DRG)</b>은 들숨 뉴런, <b>배쪽호흡군(VRG)</b>은 들숨+날숨 뉴런을 가진다. VRG 안의 <b>프리뵈트징거 복합체</b>가 박동조율기처럼 리듬을 만든다. 교뇌의 두 중추가 이를 미세조정한다.",
tr="""<ul><li>연수의 <b>중추 화학수용기 뉴런</b>이 P<sub>O2</sub>, P<sub>CO2</sub>, H⁺를 감지한다</li><li>주 들숨근의 수축·이완은 연수의 <b>연수 호흡중추</b>가 명령한다<ul><li><b>등쪽호흡군(DRG)</b>: 들숨근을 지배하는 들숨 뉴런</li><li><b>배쪽호흡군(VRG)</b>: 들숨 + 날숨 뉴런</li><li>VRG 안의 <b>프리뵈트징거 복합체</b>가 호흡 리듬을 만든다(이 뉴런들은 박동조율 활동을 보인다)</li></ul></li><li><b>교뇌</b>의 호흡중추가 연수 중추를 "미세조정"한다<ul><li><b>호흡조절중추(pneumotaxic)</b>: 들숨 뉴런을 꺼서 들숨 시간을 제한한다</li><li><b>지속흡식중추(apneustic)</b>: 들숨 뉴런이 꺼지지 않도록 한다</li></ul></li><li>그림 라벨: 교뇌 호흡중추(호흡조절중추, 지속흡식중추), 연수 호흡중추(프리뵈트징거 복합체, 등쪽호흡군, 배쪽호흡군)</li></ul>""",
ex="""<table class="t"><tr><th>위치</th><th>구조</th><th>역할</th></tr>
<tr><td rowspan="3">연수</td><td>DRG</td><td>들숨 뉴런 → 횡격막·외늑간근</td></tr><tr><td>VRG</td><td>들숨 + 날숨 뉴런(강제 호흡 시)</td></tr><tr><td><y>프리뵈트징거</y></td><td><y>리듬 생성(박동조율)</y></td></tr>
<tr><td rowspan="2">교뇌</td><td>호흡조절중추</td><td>들숨 <b>끄기</b> → 들숨 짧게</td></tr><tr><td>지속흡식중추</td><td>들숨 <b>안 꺼지게</b> → 들숨 길게</td></tr></table>
<div class="box"><span class="tag">시험 포인트</span>pneumotaxic(끄기) vs apneustic(유지) 바꿔치기, "리듬 생성 = 프리뵈트징거(VRG 안)". 그림 라벨 문제.</div>"""),
# 48
dict(img=48, slide=48, title="환기량의 조절 ① P_O2 감소 ② P_CO2 증가", sub="Regulation of ventilation magnitude",
kw=["말초 화학수용기", "대동맥체", "경동맥체", "중추 화학수용기", "P_CO2가 가장 중요"],
sum="조직 대사가 활발해 O₂를 더 쓰고 CO₂를 더 내놓으면 환기도 따라 늘어난다. 연수는 P<sub>O2</sub>, P<sub>CO2</sub>, H⁺를 감지해 이를 안다. P<sub>O2</sub> 감소는 <b>비상시에만</b> 자극하고, <b>P<sub>CO2</sub> 증가가 가장 중요한 입력</b>이다.",
tr="""<ul><li>조직이 더 활발히 대사해서 혈액이 폐포에서 O₂를 더 가져가고 CO₂를 더 버리면, 환기도 그에 맞게 증가한다</li><li>연수 호흡중추는 P<sub>O2</sub>, P<sub>CO2</sub>, H⁺를 감지하여 몸의 가스 교환 요구에 대한 정보를 받는다</li><li>1) <b>동맥 P<sub>O2</sub> 감소</b><ul><li>동맥 P<sub>O2</sub>, P<sub>CO2</sub>, H⁺는 <b>말초 화학수용기</b>가 감지한다(P<sub>O2</sub>는 주로 대동맥체)</li><li><b>비상 기전으로서만</b> 환기를 자극한다</li></ul></li><li>2) <b>동맥 P<sub>CO2</sub> 증가</b><ul><li>환기량을 조절하는 <b>가장 중요한 입력</b></li><li>P<sub>CO2</sub>는 크게 변할 수 있어, <b>경동맥체의 말초 화학수용기</b>와 <b>연수의 중추 화학수용기</b>를 통해 호흡중추를 강하게 자극한다</li></ul></li></ul>""",
ex="""<table class="t"><tr><th>자극</th><th>감지</th><th>중요도</th></tr><tr><td>P<sub>O2</sub> ↓</td><td>말초(주로 대동맥체 — 슬라이드 표기)</td><td>&lt;60 mmHg일 때만, <y>비상용</y></td></tr><tr><td><y>P<sub>CO2</sub> ↑</y></td><td>말초(경동맥체) + <y>중추(연수)</y></td><td><y>가장 중요</y></td></tr></table>
<p class="note">교과서(Sherwood)는 말초 화학수용기를 "경동맥체·대동맥체"로 함께 다루며 경동맥체를 더 중요하게 보기도 한다. 시험은 슬라이드 표기(P<sub>O2</sub> = 주로 대동맥체) 기준.</p>
<div class="box"><span class="tag">시험 포인트</span>"정상 상태에서 환기를 주로 조절하는 것은 P<sub>O2</sub>다" → <b>X</b>(P<sub>CO2</sub>).</div>"""),
# 49
dict(img=49, slide=49, title="환기량의 조절 ③ H⁺ 증가 · 화학 요인 정리", sub="Regulation of ventilation magnitude (Table 13-8)",
kw=["동맥 H⁺ ↑", "혈뇌장벽", "뇌 ECF H⁺", "1회 호흡량 ↑", "70–80 mmHg 억제"],
sum="동맥 H⁺ 증가(pH ↓)는 말초 화학수용기를 자극한다. 하지만 H⁺는 혈뇌장벽을 못 지나므로 중추 화학수용기는 <b>CO₂가 뇌로 들어가 만든 H⁺</b>에 반응한다. 들숨 뉴런이 더 발화하면 횡격막·외늑간근이 더 세게 수축해 1회 호흡량이 늘어난다.",
tr="""<ul><li>3) <b>동맥 H⁺ 증가(낮은 pH)</b><ul><li>말초 화학수용기(경동맥체; 동맥 H⁺)와 중추 화학수용기(연수; 뇌척수액 H⁺)가 감지</li><li>들숨 뉴런의 발화를 자극</li></ul></li><li>횡격막과 외늑간근이 더 강하게 수축 → 더 깊은 들숨(1회 호흡량 ↑)</li><li><b>표 13-8 호흡에 대한 화학 요인의 영향</b><ul><li><b>동맥혈 P<sub>O2</sub> ↓</b>: 말초 — 동맥 P<sub>O2</sub>가 생명이 위험할 정도(&lt; 60 mmHg)로 떨어졌을 때만 자극, 비상 기전 / 중추 — &lt; 60 mmHg이면 중추 화학수용기와 호흡중추 자체를 <b>직접 억제</b></li><li><b>동맥혈 P<sub>CO2</sub> ↑(뇌 ECF H⁺ ↑)</b>: 말초 — 약하게 자극 / 중추 — <b>강하게 자극, 환기 조절의 주된 요인</b>(&gt; 70–80 mmHg이면 호흡중추와 중추 화학수용기를 직접 억제)</li><li><b>동맥혈 H⁺ ↑</b>: 말초 — 자극, 산–염기 균형에 중요 / 중추 — 영향 없음, <b>혈뇌장벽을 통과하지 못함</b></li></ul></li><li>그림: 동맥 P<sub>CO2</sub> ↑ → 뇌 ECF P<sub>CO2</sub> ↑ → (탄산탈수효소) CO₂ + H₂O → H⁺ + HCO₃⁻ → 뇌 ECF H⁺ ↑ → 중추 화학수용기(+) → 연수 호흡중추 → 환기 ↑ → 동맥 P<sub>CO2</sub> ↓ (음성 되먹임). 말초 화학수용기는 약하게(+)</li></ul>""",
ex="""<table class="t"><tr><th>화학 요인</th><th>말초 화학수용기</th><th>중추 화학수용기</th></tr><tr><td>P<sub>O2</sub> ↓</td><td>&lt;60에서만 자극(비상)</td><td>오히려 <y>억제</y></td></tr><tr><td>P<sub>CO2</sub> ↑</td><td>약하게 자극</td><td><y>강하게 자극(주 조절)</y></td></tr><tr><td>H⁺ ↑ (동맥)</td><td><y>자극</y></td><td>영향 없음(BBB)</td></tr></table>
<div class="boxg">핵심 고리: <g>CO₂는 BBB 통과 O → 뇌에서 H⁺로 변함 → 중추 화학수용기 자극</g>. 동맥 H⁺ 자체는 BBB 통과 X.</div>
<div class="box"><span class="tag">시험 포인트</span>표 13-8 전체가 서술형·O/X 소재. "동맥 H⁺는 중추 화학수용기를 직접 자극한다" → <b>X</b>.</div>"""),
]
