PAGES = [
# 9 (17)
dict(img=9, slide=17, title="친화 크로마토그래피", sub="Affinity chromatography",
kw=["특이적 상호작용", "고정화된 분자", "가장 선택적", "항원-항체 · 효소-기질 · 수용체-리간드"],
sum="고정상에 공유결합(고정화)한 분자와 특이적으로 결합하는 한 가지 분자만 붙잡고, 나머지는 전부 씻겨 나간다. 가장 선택적인 크로마토그래피.",
tr="""<p><b>친화 크로마토그래피 (Affinity chromatography)</b></p>
<ul><li>용질 분자와, 고정상에 <b>공유결합(고정화, immobilized)</b>된 분자 사이의 <b>특이적 상호작용</b>에 기반한다</li>
<li>복잡한 혼합물에서 <b>단일 화합물</b>을 분리하는 데 쓰는 <b>가장 선택적인</b> 크로마토그래피. 예: 항원(고정화된 분자)과 항체(용질), 효소와 기질, 수용체와 리간드 사이의 상호작용</li></ul>
<p>그림: 복잡한 혼합물 속 한 종류의 분자가 고정상에 공유결합된 분자에 붙음 / 다른 모든 분자는 그냥 씻겨 나감</p>""",
ex="""<p>“열쇠와 자물쇠”야. 자물쇠(리간드)를 칼럼에 박아두면 <y>맞는 열쇠(목표 분자)만</y> 걸리고 나머지는 전부 통과해.</p>
<table class="t"><tr><th>고정화한 것</th><th>붙잡히는 것</th></tr>
<tr><td>항원</td><td>그 항원에 대한 <b>항체</b></td></tr>
<tr><td>기질(유사체)</td><td><b>효소</b></td></tr>
<tr><td>리간드</td><td><b>수용체</b></td></tr>
<tr><td>Protein A</td><td>IgG 항체 (항체 의약품 정제)</td></tr></table>
<p><b>순서</b>: ① 시료 흘림 → 목표만 결합 ② 세척 → 나머지 제거 ③ 용리 조건(pH 변화, 고농도 경쟁 리간드)으로 목표를 떼어냄</p>
<div class="boxg"><b>다섯 가지 기전 한 줄 정리</b><br>흡착 = 표면에 붙음 · 분배 = 액체막에 녹음 · 이온교환 = 반대 전하 인력 · 크기배제 = 구멍 출입(큰 것 먼저) · <b>친화 = 생물학적 특이 결합 (선택성 최고)</b></div>"""),

# 10 (18)
dict(img=10, slide=18, title="배관공의 시각 — 부피유속과 길이유속", sub="A plumber’s view: volume flow rate u_v vs linear flow rate u_x",
kw=["부피유속 u_v (mL/min)", "길이유속 u_x (cm/min)", "u_x = u_v / πr²", "개관 칼럼"],
sum="칼럼 = 관(pipe). 1분에 몇 mL 흐르나가 부피유속 u_v, 1분에 몇 cm 나아가나가 길이유속 u_x. 개관 칼럼은 u_x = u_v / (πr²).",
tr="""<p><b>배관공의 시각으로 본 크로마토그래피</b></p>
<p>관을 통과하는 액체나 기체의 흐름! ≈ 칼럼을 통과하는 이동상의 흐름!</p>
<p><b>부피유속 (volume flow rate), u<sub>v</sub> (mL/min)</b><br>- 단위 시간당 칼럼을 지나가는 용매의 부피</p>
<p><b>길이유속 (linear flow rate), u<sub>x</sub> (cm/min)</b><br>- 단위 시간당 용매가 이동한 거리</p>
<p class="eq">u<sub>x</sub> (cm/min) = u<sub>v</sub> (mL/min) / 칼럼 단위 길이당 부피 (mL/cm)</p>
<p class="eq">= u<sub>v</sub> / (πr<sup>2</sup> × 1) (mL/cm) &nbsp;(개관 칼럼)</p>
<p>(r: 칼럼 안쪽 반지름)</p>""",
ex="""<p>수도꼭지 비유: 같은 양의 물(u<sub>v</sub>)이라도 <y>호스가 가늘면 물이 더 빨리 나아가(u<sub>x</sub>↑)</y>지?</p>
<p>단위로 확인: (mL/min) ÷ (mL/cm) = <g>cm/min</g> ✓. 단위 길이당 부피 = 단면적 × 1 cm = πr<sup>2</sup>.</p>
<p><b>예제</b>: 안지름 0.25 mm 모세관 GC 칼럼(r = 0.0125 cm), u<sub>v</sub> = 1.0 mL/min</p>
<p class="eq">πr<sup>2</sup> = 3.14 × (0.0125)<sup>2</sup> = 4.9 × 10<sup>−4</sup> mL/cm<br>u<sub>x</sub> = 1.0 / 4.9 × 10<sup>−4</sup> ≈ <b>2.0 × 10<sup>3</sup> cm/min ≈ 34 cm/s</b></p>
<ul><li><b>충전 칼럼</b>은 관 안에 입자가 차 있어서 이동상이 지나갈 공간이 단면적의 일부(공극률)뿐 → 같은 u<sub>v</sub>라도 u<sub>x</sub>가 πr<sup>2</sup>로 계산한 것보다 큼. 그래서 식에 “(개관 칼럼)”이라는 조건이 붙어.</li>
<li><pk>van Deemter 식(슬라이드 39–)의 u<sub>x</sub>는 길이유속</pk>이야. 띠 넓어짐은 용질이 “얼마나 빨리 나아가나”에 달려 있거든.</li></ul>"""),

# 11 (19)
dict(img=11, slide=19, title="크로마토그램 — t_r, t_m, t′_r", sub="The chromatogram: retention time, dead time, adjusted retention time",
kw=["크로마토그램", "머무름시간 t_r", "불감시간 t_m (t₀)", "보정 머무름시간 t′_r = t_r − t_m"],
sum="크로마토그램은 시간에 따른 검출기 신호 그래프. t_r = 주입부터 검출까지, t_m = 안 붙잡히는 물질(CH₄)이 나오는 시간(이동상에 있는 시간), t′_r = t_r − t_m = 고정상에 머문 시간.",
tr="""<p><b>크로마토그램</b>: 용리 시간에 따른 검출기 응답을 나타낸 그래프</p>
<p>그림: 주입 시각 → CH<sub>4</sub> 피크 → 옥테인, 미지 물질, 노네인 피크. 위 화살표: 보정 머무름시간 t′<sub>r</sub>, 머무름시간 t<sub>r</sub>, t<sub>m</sub></p>
<ul><li><b>t<sub>r</sub></b>: 머무름시간(retention time), 유지시간 또는 머무름시간 (주입 후 분석물이 검출기에 도달하는 데 걸리는 시간)</li>
<li><b>t<sub>m</sub></b> (t<sub>0</sub>, 불감시간 dead time 또는 공극시간 void time): 머무르지 않는 이동상이 주입 후 검출기에 도달하는 데 걸리는 시간; <b>용질이 이동상에 머문 시간</b></li>
<li><b>t′<sub>r</sub></b>: 보정 머무름시간(adjusted retention time), t′<sub>r</sub> = t<sub>r</sub> − t<sub>m</sub>; <b>용질이 고정상에 머문 시간</b></li></ul>""",
ex="""<p><b>핵심 아이디어</b>: 모든 용질은 칼럼 길이만큼 이동상을 타고 가야 하니까 <y>최소 t<sub>m</sub>은 무조건 걸려</y>. 여기에 고정상에 붙잡혀 있던 시간 t′<sub>r</sub>이 더해진 게 t<sub>r</sub>이야.</p>
<p class="eq">t<sub>r</sub> = t<sub>m</sub> (이동상에 있던 시간) + t′<sub>r</sub> (고정상에 있던 시간)</p>
<ul><li><b>왜 CH<sub>4</sub>?</b> GC에서 메테인은 고정상과 거의 상호작용 안 해서 운반 기체와 같은 속도로 나와 → <g>t<sub>m</sub> 측정용 표지</g>. HPLC에선 우라실 같은 극성 물질을 써 (슬라이드 32 성적서 첫 피크가 우라실!).</li>
<li>옥테인(C8) → 미지 → 노네인(C9) 순서: 탄소 수가 많을수록 끓는점이 높고 고정상에 오래 머물러. 미지 물질은 둘 사이니까 GC에선 이렇게 표준 알케인 사이 위치로 정체를 추정하기도 해.</li></ul>
<p><b>예제</b>: t<sub>m</sub> = 1.0 min, t<sub>r</sub> = 6.0 min → t′<sub>r</sub> = <b>5.0 min</b> (고정상에서 5분, 이동상에서 1분)</p>
<div class="box"><span class="tag">헷갈림</span>t<sub>m</sub>은 “용질이 이동상에 머문 시간”이기도 해. <b>머무르지 않는</b> 물질이든 오래 머무는 물질이든 이동상에서 보내는 총 시간은 똑같이 t<sub>m</sub>이야.</div>"""),

# 12 (20)
dict(img=12, slide=20, title="분리인자 α · γ · 용량인자 k′", sub="Relative retention (α), unadjusted relative retention (γ), retention (capacity) factor (k′)",
kw=["α = t′r2 / t′r1 > 1", "γ = tr2 / tr1", "k′ = (tr − tm)/tm = t′r/tm", "유속과 거의 무관"],
sum="α = 두 피크의 보정 머무름시간 비(>1, 유속에 거의 무관). γ = 보정 안 한 머무름시간 비. k′ = 고정상에 머문 시간이 이동상에 머문 시간의 몇 배인가.",
tr="""<p><b>상대 머무름 (분리인자, separation factor), α:</b></p>
<p class="eq">α = t′<sub>r2</sub> / t′<sub>r1</sub> &nbsp; (t′<sub>r2</sub> > t′<sub>r1</sub>, α > 1)</p>
<p>상대 머무름은 <b>유속과 거의 무관</b>하다.</p>
<p><b>보정하지 않은 상대 머무름 (unadjusted relative retention), γ:</b></p>
<p class="eq">γ = t<sub>r2</sub> / t<sub>r1</sub></p>
<p><b>머무름(또는 용량) 인자 (retention / capacity factor), k′:</b></p>
<p class="eq">k′ = (t<sub>r</sub> − t<sub>m</sub>) / t<sub>m</sub> = t′<sub>r</sub> / t<sub>m</sub></p>
<ul><li>보정 머무름시간을 t<sub>m</sub>의 배수로 나타낸 것 (용질이 고정상에 머무는 시간(t′<sub>r</sub>)을 이동상에 머무는 시간(t<sub>m</sub>)의 배수로 표현한 것)</li>
<li>성분이 칼럼에 오래 붙잡힐수록 머무름 인자가 크다</li></ul>""",
ex="""<p><b>예제</b> (t<sub>m</sub> = 1.0 min, 피크1 t<sub>r1</sub> = 5.0 min, 피크2 t<sub>r2</sub> = 6.0 min)</p>
<table class="t"><tr><th>값</th><th>계산</th><th>답</th></tr>
<tr><td>t′<sub>r1</sub>, t′<sub>r2</sub></td><td>5.0 − 1.0, 6.0 − 1.0</td><td>4.0, 5.0 min</td></tr>
<tr><td><b>α</b></td><td>5.0 / 4.0</td><td><b>1.25</b></td></tr>
<tr><td><b>γ</b></td><td>6.0 / 5.0</td><td><b>1.20</b></td></tr>
<tr><td>k′<sub>1</sub>, k′<sub>2</sub></td><td>4.0/1.0, 5.0/1.0</td><td><b>4.0, 5.0</b></td></tr></table>
<ul><li><pk>α는 항상 “늦게 나온 것 / 먼저 나온 것”</pk>이라 1보다 커. α = 1이면 두 피크가 겹쳐서 분리 불가.</li>
<li><b>왜 α는 유속에 무관?</b> 유속을 2배로 하면 t′<sub>r1</sub>, t′<sub>r2</sub>가 둘 다 절반 → 비율은 그대로. 그래서 α는 <g>칼럼과 이동상 조성(화학)</g>에 의해 정해지는 값이야.</li>
<li>γ는 t<sub>m</sub>을 안 빼서 α보다 항상 1에 가까워(γ < α). 슬라이드 34의 분리도 식에 γ가 쓰여.</li>
<li>k′ = α의 재료: <g>α = k′<sub>2</sub>/k′<sub>1</sub></g> (5.0/4.0 = 1.25 ✓)</li></ul>"""),

# 13 (21)
dict(img=13, slide=21, title="머무름시간과 분배계수의 관계 · 머무름부피", sub="Relation between retention time and the partition coefficient",
kw=["k′ = K·V_s/V_m", "k′ ∝ K ∝ t′r", "α = k′2/k′1 = K2/K1", "V_r = t_r·u_v"],
sum="k′ = (고정상에 머문 시간/이동상에 머문 시간) = (고정상 속 몰수/이동상 속 몰수) = K·V_s/V_m. 그래서 분리인자 α는 결국 두 성분의 분배계수 비. 머무름부피 V_r = t_r·u_v는 유속에 무관.",
tr="""<p><b>머무름시간과 분배계수의 관계</b></p>
<p class="eq">k′ = t′<sub>r</sub>/t<sub>m</sub> = (용질이 고정상에 머문 시간)/(용질이 이동상에 머문 시간) = (고정상 속 용질 몰수)/(이동상 속 용질 몰수)</p>
<p class="eq">k′ = c<sub>s</sub>V<sub>s</sub> / c<sub>m</sub>V<sub>m</sub> = K·V<sub>s</sub>/V<sub>m</sub> = (t<sub>r</sub> − t<sub>m</sub>)/t<sub>m</sub> = t′<sub>r</sub>/t<sub>m</sub></p>
<p class="eq">k′ ∝ K ∝ t′<sub>r</sub></p>
<p class="eq">상대 머무름 α = t′<sub>r2</sub>/t′<sub>r1</sub> = k′<sub>2</sub>/k′<sub>1</sub> = K<sub>2</sub>/K<sub>1</sub></p>
<p><b>머무름부피 (retention volume), V<sub>r</sub></b>: 특정 용질을 칼럼에서 용리하는 데 필요한 이동상의 부피<br>V<sub>r</sub> = t<sub>r</sub>·u<sub>v</sub> (u<sub>v</sub>: 부피유속). 특정 용질의 V<sub>r</sub>은 일정 범위의 유속에서 <b>일정</b>하다.</p>
<p>Q: 다음 각각의 경우 용질이 고정상에 머무는 시간은 이동상에 머무는 시간의 몇 배인가? k′ = 0 / k′ = 1 / k′ = 5</p>""",
ex="""<p><b>왜 시간 비 = 몰수 비?</b> 용질 분자 하나하나는 고정상과 이동상을 계속 오가. 어느 순간 전체 분자의 몇 %가 고정상에 있냐 = 한 분자가 전체 시간 중 몇 %를 고정상에서 보내냐. 그래서 <y>시간 비 = 몰수 비</y>야.</p>
<p>몰수 = 농도 × 부피 → c<sub>s</sub>V<sub>s</sub>/c<sub>m</sub>V<sub>m</sub>, 그리고 c<sub>s</sub>/c<sub>m</sub> = <b>K</b> (분배계수!) → <g>k′ = K·(V<sub>s</sub>/V<sub>m</sub>)</g></p>
<ul><li>같은 칼럼이면 V<sub>s</sub>/V<sub>m</sub>은 상수 → <b>k′ ∝ K</b>. 분배계수가 큰 성분일수록 늦게 나와.</li>
<li>그래서 <pk>α = K<sub>2</sub>/K<sub>1</sub></pk>: 분리되려면 두 성분의 K가 달라야 해 (슬라이드 1의 “왜 분리되나?”의 답).</li></ul>
<div class="boxg"><b>Q 정답</b> (k′ = 고정상 시간 / 이동상 시간)<br>• k′ = 0 → <b>0배</b>: 고정상에 전혀 안 머묾, t<sub>r</sub> = t<sub>m</sub> (CH<sub>4</sub> 같은 비머무름 물질)<br>• k′ = 1 → <b>1배</b>: 두 상에서 같은 시간, t<sub>r</sub> = 2t<sub>m</sub><br>• k′ = 5 → <b>5배</b>: t<sub>r</sub> = 6t<sub>m</sub></div>
<p><b>V<sub>r</sub>이 유속에 무관한 이유</b>: 유속을 2배로 하면 t<sub>r</sub>은 절반 → t<sub>r</sub>·u<sub>v</sub>는 그대로. 용질을 씻어내는 데 필요한 이동상 “양”은 같다는 뜻이야.</p>"""),

# 14 (24)
dict(img=14, slide=24, title="분리 효율 — 분리도 R과 가우스 피크", sub="Efficiency of separation: resolution, w = 4σ, w½ = 2.35σ",
kw=["분리도 R = Δt_r / w_av", "w = 4σ", "w½ = 2.35σ", "R = 0.589Δt_r / w½av", "가우스 피크"],
sum="분리가 잘 됐는지는 ① 두 피크 사이 거리(Δt_r)와 ② 피크 폭(w)이 결정. R = Δt_r / 평균 바닥폭. 가우스 피크에서 바닥폭 w = 4σ, 반높이 폭 w½ = 2.35σ = 1.70배 관계.",
tr="""<p><b>분리 효율</b> — 크로마토그래피로 화합물이 얼마나 잘 분리되는지에 기여하는 요인:</p>
<ul><li>피크 사이의 머무름시간 차이</li><li>피크 폭</li></ul>
<p class="eq">분리도 (Resolution), R = Δt<sub>r</sub>/w<sub>av</sub> = ΔV<sub>r</sub>/w<sub>av</sub> = Δt<sub>r</sub>/1.70w<sub>1/2av</sub> = 0.589Δt<sub>r</sub>/w<sub>1/2av</sub></p>
<p class="eq">w = 4σ, &nbsp; w<sub>1/2</sub> = 2.35σ, &nbsp; σ = w<sub>1/2</sub>/2.35<br>w = 4 × w<sub>1/2</sub>/2.35 = 1.70w<sub>1/2</sub></p>
<p>그림: 가우스 피크(대칭). 변곡점(곡선이 가장 가파른 부분)에 그은 접선이 바탕선과 만나는 두 점 사이가 w = 4σ, 높이의 1/2에서의 폭 w<sub>1/2</sub> = 2.35σ, 피크 꼭대기 위치가 t<sub>r</sub> 또는 V<sub>r</sub></p>
<p>Q: 왜 피크의 모양이 정규분포곡선일까?</p>""",
ex="""<p><b>R의 의미</b>: 두 피크 중심 간 거리를 “피크 폭 몇 개만큼 떨어졌나”로 잰 것. w<sub>av</sub>는 두 피크 폭의 평균.</p>
<p><b>상수 유도</b> (시험에 계산 많이 나옴)</p>
<ul><li>바닥폭 <b>w = 4σ</b> (변곡점 접선이 바탕선과 만나는 폭, 평균 ± 2σ)</li>
<li>반높이 폭 <b>w<sub>1/2</sub> = 2√(2ln2)σ = 2.35σ</b></li>
<li>w = 4σ = 4 × (w<sub>1/2</sub>/2.35) = <g>1.70w<sub>1/2</sub></g> → R = Δt<sub>r</sub>/1.70w<sub>1/2</sub> = <g>0.589Δt<sub>r</sub>/w<sub>1/2</sub></g> (1/1.70 = 0.589)</li></ul>
<p><b>예제</b>: Δt<sub>r</sub> = 0.60 min, 두 피크의 w<sub>1/2</sub> = 0.18, 0.22 min → w<sub>1/2av</sub> = 0.20<br>R = 0.589 × 0.60 / 0.20 = <b>1.77</b> (바탕선 분리 ✓)</p>
<div class="boxg"><b>Q: 왜 정규분포일까?</b> 용질 분자 하나하나가 칼럼을 지나며 <y>무작위로</y> 고정상에 붙었다 떨어지고, 확산으로 앞뒤로 흩어지는 일을 수없이 반복해. 서로 독립인 작은 무작위 변화가 아주 많이 더해지면 <b>중심극한정리</b>에 따라 결과 분포가 정규(가우스) 분포가 돼. (슬라이드 26 브라운 운동 히스토그램과 29의 확산식이 그 증거)</div>"""),

# 15 (25)
dict(img=15, slide=25, title="분리도에 따른 피크 겹침", sub="Resolution = 0.50, 0.75, 1.00, 1.50",
kw=["R = 0.5 (2σ)", "R = 0.75 (3σ)", "R = 1.0 (4σ)", "R = 1.5 (6σ) 바람직"],
sum="두 피크 중심 사이가 2σ, 3σ, 4σ, 6σ일 때 R = 0.5, 0.75, 1.0, 1.5. R = 1.5면 바탕선까지 거의 완전 분리 → 바람직.",
tr="""<p><b>분리 효율</b></p>
<p class="eq">분리도 = Δt<sub>r</sub>/w<sub>av</sub> = 2σ/4σ = 0.5</p>
<ul><li>중심 간 거리 <b>2σ</b> → 분리도 <b>0.50</b></li>
<li>중심 간 거리 <b>3σ</b> → 분리도 <b>0.75</b></li>
<li>중심 간 거리 <b>4σ</b> → 분리도 <b>1.00</b></li>
<li>중심 간 거리 <b>6σ</b> → 분리도 <b>1.50</b> — <b>바람직하다!</b></li></ul>
<p>그림: 점선은 각각의 피크, 실선은 검출기가 실제로 보는 합쳐진 신호(Signal vs Time). 회색으로 칠한 부분이 서로 겹친 면적</p>""",
ex="""<p>w = 4σ이니까 <g>R = Δt<sub>r</sub>/4σ</g> → 중심 간 거리를 σ로 나타내면 R이 바로 나와.</p>
<table class="t"><tr><th>R</th><th>Δt<sub>r</sub></th><th>모양</th><th>각 피크가 상대 쪽으로 넘어간 양 (대략)</th></tr>
<tr><td>0.50</td><td>2σ</td><td>봉우리 하나처럼 보임</td><td>~16%</td></tr>
<tr><td>0.75</td><td>3σ</td><td>두 봉우리, 골이 깊지 않음</td><td>~7%</td></tr>
<tr><td>1.00</td><td>4σ</td><td>골이 꽤 내려감</td><td>~2.3%</td></tr>
<tr><td><b>1.50</b></td><td><b>6σ</b></td><td><b>바탕선 분리</b></td><td><b>~0.13%</b></td></tr></table>
<p class="note">겹침 %는 같은 크기의 두 가우스 피크에서 중간 지점 너머로 넘어간 꼬리 면적이야 (표준정규분포 표에서 z = R × 2일 때의 꼬리).</p>
<ul><li><pk>정량분석에서 목표는 R ≥ 1.5</pk>. R = 1이면 겉보기엔 두 피크인데 실제론 2% 넘게 섞여 있어.</li>
<li>피크 크기가 많이 다르면(큰 피크 옆 작은 불순물) R = 1.5로도 부족할 수 있어.</li></ul>
<div class="box"><span class="tag">족보</span>“Resolution, 크로마토그래피 공식 암기하고 계산문제 꽤 나옴”. Δσ ↔ R 변환은 바로 나와야 해.</div>"""),

# 16 (26)
dict(img=16, slide=26, title="확산 — 띠 넓어짐의 주원인", sub="Diffusion: main cause of peak (or band) broadening",
kw=["띠 넓어짐", "확산(diffusion)", "고농도 → 저농도", "브라운 운동", "정규분포"],
sum="용질 띠는 칼럼을 지나갈수록 넓어진다. 주된 원인은 확산: 분자의 무작위 운동으로 고농도에서 저농도로 퍼지는 것. 무작위 걸음 히스토그램이 정규분포 모양이다.",
tr="""<p><b>확산: 피크(또는 띠) 넓어짐의 주원인</b></p>
<ul><li>용질 띠는 크로마토그래피 칼럼을 이동하면서 넓어진다</li>
<li>띠 넓어짐의 주원인 중 하나는 <b>확산(diffusion)</b>, 즉 분자의 <b>무작위 운동</b>에 의해 용질이 <b>고농도 영역에서 저농도 영역으로</b> 알짜 이동하는 것이다</li></ul>
<p>그림 (a): 칼럼 시작점의 좁은 띠가 이동하며 점점 넓고 낮아짐(농도 분포) (b) 2.0 min의 날카로운 피크, 26 min의 넓은 피크 (c) 넓은 피크 폭 약 3 s</p>
<p>오른쪽: <b>분자의 무작위 운동</b> — 지름 20 μm 물방울 속 지름 290 nm 형광 비드의 브라운 운동. 아래는 x, y 방향 걸음 길이의 확률 히스토그램 (정규분포)</p>""",
ex="""<p>잉크 한 방울을 물에 떨어뜨리면 가만히 둬도 점점 퍼지지? 칼럼 속 용질 띠도 똑같아. 이동하는 동안 <y>시간이 흐를수록 퍼져서 넓고 낮은 피크</y>가 돼.</p>
<ul><li>(b) 일찍 나온 피크(2 min)는 좁고 높고, 늦게 나온 피크(26 min)는 넓고 낮아. <g>칼럼 속에 오래 있을수록 더 많이 확산</g>했기 때문이야. 면적(양)은 같아.</li>
<li>오른쪽 그림: 비드 하나의 경로가 지그재그(브라운 운동). 한 걸음의 x, y 방향 길이를 모으면 0을 중심으로 한 <b>종 모양(정규분포)</b> → 앞 슬라이드 Q “왜 피크가 정규분포인가?”의 실험적 근거야.</li></ul>
<div class="boxg"><b>정리</b>: 무작위 걸음이 많이 쌓이면 → 가우스 분포 → 그래서 크로마토그래피 피크가 가우스 모양. 그리고 그 폭(σ)은 시간이 지날수록 커져 (σ ∝ √t, 슬라이드 29).</div>
<div class="box"><span class="tag">족보</span>기말 복기 키워드 “<b>Diffusion</b>”. 확산이 왜 띠를 넓히는지, 그리고 van Deemter의 B항(세로 확산)과 연결해서 설명할 수 있어야 해.</div>"""),
]
