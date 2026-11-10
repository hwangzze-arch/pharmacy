PAGES = [
dict(img=73, slide=73, title="③ 스쿠알렌 형성 — 아이소프렌 6개", sub="(3) Formation of squalene",
kw=["프레닐 전달효소 (머리-꼬리)", "제라닐 PP C10", "파네실 PP C15", "스쿠알렌 합성효소 (머리-머리)", "NADPH"],
sum="DMAPP + IPP → 제라닐 파이로인산(C10) → + IPP → 파네실 파이로인산(C15). 파네실 PP 2개를 스쿠알렌 합성효소가 머리-머리로 붙여(NADPH) C30 스쿠알렌.",
tr="""<p><b>(3) 스쿠알렌의 형성</b></p>
<p>다이메틸알릴 PP + Δ³-아이소펜텐일 PP —(<b>프레닐 전달효소, 머리-꼬리 축합</b>, PPᵢ)→ <b>제라닐 파이로인산</b> —(프레닐 전달효소, + IPP, PPᵢ)→ <b>파네실 파이로인산</b><br>
파네실 PP × 2 —(<b>스쿠알렌 합성효소, 머리-머리</b>, NADPH, 2PPᵢ)→ <b>스쿠알렌</b></p>
<p class="note">(강의 중 영상: biosynthesis_squalene.mov)</p>""",
ex="""<table class="t"><tr><th>산물</th><th>탄소</th><th>계산</th></tr>
<tr><td>제라닐 PP</td><td>C10</td><td>5 + 5</td></tr><tr><td>파네실 PP</td><td>C15</td><td>10 + 5</td></tr>
<tr><td>스쿠알렌</td><td>C30</td><td>15 + 15 (머리-머리)</td></tr></table>
<p>각 축합에서 <g>파이로인산(PPᵢ)</g>이 떨어지며 생긴 탄소 양이온이 다음 이중결합을 공격해. 마지막 머리-머리 연결에선 NADPH가 환원에 쓰여.</p>
<div class="box"><span class="tag">연결</span>파네실 PP는 갈림길: 단백질 프레닐화(Ras), 돌리콜, 유비퀴논 쪽으로도 감.</div>"""),

dict(img=74, slide=74, title="④ 스쿠알렌 → 스테로이드 핵 → 콜레스테롤", sub="(4) squalene to the condensed steroid nucleus",
kw=["스쿠알렌 일산소화효소 (O₂, NADPH)", "2,3-에폭사이드", "고리화효소", "라노스테롤", "식물 스티그마스테롤 · 곰팡이 에르고스테롤"],
sum="스쿠알렌 일산소화효소가 2,3-에폭사이드를 만들고(O₂, NADPH), 고리화효소가 4개 고리를 한 번에 닫아 라노스테롤. 이후 여러 단계로 콜레스테롤. 식물은 스티그마스테롤, 곰팡이는 에르고스테롤로 간다.",
tr="""<p><b>(4) 스쿠알렌에서 축합된 스테로이드 핵으로</b></p>
<p>스쿠알렌 —(<b>스쿠알렌 일산소화효소</b>, NADPH + H⁺ + O₂ → H₂O + NADP⁺)→ <b>스쿠알렌 2,3-에폭사이드</b> —(<b>고리화효소</b>, 동물)→ <b>라노스테롤</b> → (여러 단계) → <b>콜레스테롤</b><br>
에폭사이드 → (여러 단계, 식물) <b>스티그마스테롤</b> / (여러 단계, 곰팡이) <b>에르고스테롤</b></p>
<p class="note">(강의 중 영상: squalene_to_cholesterol.mov)</p>""",
ex="""<p>긴 사슬이 <y>지퍼 잠기듯</y> 한 번에 4개 고리(A·B·C·D)로 접히는 놀라운 반응이야. 라노스테롤(C30) → 메틸기 3개 떼고 → 콜레스테롤(<b>C27</b>).</p>
<div class="box"><span class="tag">약학</span><b>스쿠알렌 일산소화효소(에폭시데이스)</b>의 곰팡이 버전 억제 = 테르비나핀(무좀약). <b>에르고스테롤</b>은 곰팡이 막 성분 → 아졸계 항진균제(라노스테롤 14α-탈메틸화효소 억제), 암포테리신 B(에르고스테롤 결합)의 표적.</div>"""),

dict(img=75, slide=75, title="콜레스테롤 에스터 — 저장·운반용", sub="Synthesis of cholesteryl esters (more hydrophobic form for storage and transport)",
kw=["ACAT", "지방아실-CoA", "C3–OH 에스터화", "더 소수성"],
sum="ACAT(아실-CoA:콜레스테롤 아실전달효소)가 콜레스테롤 C3–OH에 지방산을 붙여 콜레스테릴 에스터를 만든다. 완전히 소수성이라 세포 안 지질 방울이나 지질단백질 속에 저장·운반된다. 콜레스테롤의 운명: 세포막, 담즙 콜레스테롤, 담즙산.",
tr="""<p><b>콜레스테릴 에스터의 합성</b> (저장·운반을 위한 더 소수성인 형태)</p>
<p>콜레스테롤 + 지방아실-CoA —(<b>아실-CoA–콜레스테롤 아실전달효소, ACAT</b>, CoA-SH)→ <b>콜레스테릴 에스터</b></p>
<p>콜레스테롤 → 세포막 / 담즙 콜레스테롤 / 담즙산</p>""",
ex="""<p>콜레스테롤의 유일한 친수성 부분인 <b>–OH</b>를 지방산으로 덮어 버리니까 <y>완전한 기름 덩어리</y>가 돼서 막에 끼지 못하고 지질 방울·지질단백질 핵 속으로 들어가.</p>
<table class="t"><tr><th>효소</th><th>어디서</th><th>지방산 공여체</th></tr>
<tr><td><b>ACAT</b></td><td>세포 안 (간, 장)</td><td>지방아실-CoA</td></tr>
<tr><td><b>LCAT</b></td><td>혈액 속 HDL</td><td>레시틴(PC)의 C2 지방산 (다음 슬라이드)</td></tr></table>"""),

dict(img=76, slide=76, title="LCAT — HDL에서 콜레스테롤 에스터화", sub="Reaction catalyzed by lecithin-cholesterol acyl transferase (LCAT) in HDL",
kw=["LCAT", "레시틴(PC)", "리소레시틴", "HDL 성숙"],
sum="HDL의 LCAT가 레시틴(포스파티딜콜린) C2의 지방산을 콜레스테롤에 옮겨 콜레스테릴 에스터와 리소레시틴을 만든다. 에스터는 HDL 속으로 들어가 HDL이 둥글게 성숙한다.",
tr="""<p><b>HDL에서 레시틴-콜레스테롤 아실전달효소(LCAT)가 촉매하는 반응</b></p>
<p>포스파티딜콜린(레시틴) + 콜레스테롤 —(<b>LCAT</b>)→ <b>콜레스테릴 에스터</b> + <b>리소레시틴</b></p>""",
ex="""<p>HDL은 말초 조직에서 여분의 콜레스테롤을 주워 오는 청소차야. 주운 콜레스테롤을 LCAT로 에스터화해 <y>속으로 집어넣어야</y> 표면이 비어 더 주워 올 수 있어 → 역콜레스테롤 수송(슬라이드 92)의 핵심 단계.</p>
<div class="boxg">LCAT의 활성화 인자 = <g>ApoA-I</g> (HDL의 주 단백질).</div>"""),

dict(img=77, slide=77, title="콜레스테롤 합성의 조절 — 합성과 섭취의 균형", sub="Regulation of cholesterol formation balances synthesis with dietary uptake",
kw=["HMG-CoA 환원효소", "인슐린 ⊕ (탈인산화)", "글루카곤 ⊖ (인산화)", "스타틴 ⊣", "콜레스테롤 ⊣ (단백질 분해 촉진)", "ACAT ⊕"],
sum="조절 지점은 HMG-CoA 환원효소. 인슐린은 탈인산화로 켜고, 글루카곤은 인산화로 끈다. 세포 안 콜레스테롤이 많으면 효소 분해를 촉진하고, LDL 수용체 세포내이입을 줄이며, ACAT로 저장한다. 스타틴은 이 효소를 직접 억제.",
tr="""<p><b>콜레스테롤 형성의 조절은 합성과 식이 섭취의 균형을 맞춘다</b></p>
<p>아세틸-CoA → HMG-CoA —(<b>HMG-CoA 환원효소</b>)→ 메발론산 → 콜레스테롤(세포 내)</p>
<ul><li><b>인슐린</b> ⊕ (탈인산화, de(P)) / <b>글루카곤</b> ⊗ (인산화, (P))</li><li><b>스타틴</b> ⊣ HMG-CoA 환원효소</li>
<li>콜레스테롤 → X → <b>HMG-CoA 환원효소의 단백질 분해 촉진</b> ⊗ (X = 아직 밝혀지지 않은 콜레스테롤 대사물)</li>
<li>콜레스테롤 → <b>수용체 매개 세포내이입</b> ⊗ (LDL-콜레스테롤 유입 감소)</li><li>콜레스테롤 → ACAT ⊕ → 콜레스테릴 에스터</li></ul>""",
ex="""<table class="t"><tr><th>조절</th><th>방법</th><th>속도</th></tr>
<tr><td>호르몬</td><td>인슐린 ON / 글루카곤 OFF (인산화 — AMPK)</td><td>빠름</td></tr>
<tr><td>콜레스테롤 많음</td><td>효소 분해 ↑ (Insig 결합 → 유비퀴틴화)</td><td>중간</td></tr>
<tr><td>콜레스테롤 적음</td><td><b>SREBP</b> → 효소·LDL 수용체 유전자 ↑ (슬라이드 79)</td><td>느림(전사)</td></tr>
<tr><td>약</td><td><b>스타틴</b> 경쟁 억제</td><td>—</td></tr></table>
<div class="boxg">ACC(지방산)와 똑같은 패턴: <g>인슐린 = 탈인산화 = ON, 글루카곤 = 인산화 = OFF</g>.</div>"""),

dict(img=78, slide=78, title="스타틴 — HMG-CoA 환원효소 억제제", sub="Statins as inhibitors of HMG-CoA reductase",
kw=["메발론산 닮은꼴", "경쟁적 억제", "컴팩틴·심바스타틴·프라바스타틴·로바스타틴", "아토르바스타틴(리피토)"],
sum="스타틴은 메발론산(HMG-CoA 환원효소의 산물)과 닮은 부분을 가져 효소에 경쟁적으로 붙는다. 컴팩틴, 심바스타틴(조코), 프라바스타틴(프라바콜), 로바스타틴(메바코), 아토르바스타틴(리피토, 연 120억 달러 매출).",
tr="""<p><b>HMG-CoA 환원효소 억제제로서의 스타틴</b></p>
<p>메발론산 구조와 비교 — 스타틴의 분홍색 부분(HO–CH–CH₂–CH(OH)–CH₂–COO⁻)이 닮음</p>
<table class="t"><tr><th>R₁</th><th>R₂</th><th>이름</th></tr>
<tr><td>H</td><td>H</td><td>컴팩틴</td></tr><tr><td>CH₃</td><td>CH₃</td><td>심바스타틴 (조코)</td></tr>
<tr><td>H</td><td>OH</td><td>프라바스타틴 (프라바콜)</td></tr><tr><td>H</td><td>CH₃</td><td>로바스타틴 (메바코)</td></tr></table>
<p><b>아토르바스타틴: 리피토</b> — 연 120억 달러 매출</p>""",
ex="""<p>스타틴의 다이하이드록시산 부분이 <y>HMG-CoA → 메발론산 반응의 중간 상태</y>를 흉내 내서 활성 부위를 차지해 (경쟁적 억제, Kᵢ ≈ nM).</p>
<div class="boxg"><b>LDL을 낮추는 진짜 이유</b>: 간세포 콜레스테롤 ↓ → <g>SREBP 활성 → LDL 수용체 ↑</g> → 혈중 LDL을 간이 더 많이 빨아들임.</div>
<div class="box"><span class="tag">약학</span>부작용: 근육통·횡문근융해(CoQ10 ↓ 등), 간효소 ↑. 밤에 복용 권장(콜레스테롤 합성은 밤에 활발, 반감기 짧은 심바스타틴 등). 임부 금기.</div>"""),

dict(img=79, slide=79, title="콜레스테롤이 부족하면 — SREBP 활성화", sub="When cholesterol is scarce… SREBP activation",
kw=["SREBP", "SCAP", "Insig", "골지 단백질 분해효소 2개", "HMG-CoA 환원효소 ↑"],
sum="콜레스테롤이 많으면 SCAP-SREBP가 Insig에 묶여 소포체에 머문다. 부족하면 Insig가 분해되고 SCAP가 SREBP를 골지로 데려가, 단백질 분해효소 2개가 조절 도메인을 잘라 핵으로 보낸다 → 지질 합성 효소(HMG-CoA 환원효소, LDL 수용체) 전사 ↑.",
tr="""<p><b>콜레스테롤이 부족할 때… SREBP 활성화</b></p>
<p>(a) 소포체 [스테롤] 높음: <b>SCAP/SREBP</b>가 소포체에 남아 <b>Insig</b>에 결합</p>
<p>(b) 소포체 [스테롤] 낮음: ① 유비퀴틴이 Insig를 분해로 표시 ② 분비 단백질(Sec)이 SCAP/SREBP를 골지로 호위 ③ 골지에서 <b>두 단백질 분해효소</b>가 SREBP의 조절 도메인을 풀어줌 ④ 조절 도메인이 <b>핵으로</b> 들어감 ⑤ 지질 합성 효소의 <b>전사 촉진</b></p>
<p>(c) 소포체에서 콜레스테롤 합성 증가 → <b>HMG-CoA 환원효소 ↑</b></p>""",
ex="""<p>SREBP = Sterol Regulatory Element-Binding Protein (스테롤 조절 요소 결합 단백질). 평소엔 <y>소포체 막에 묶인 전사인자</y>야.</p>
<table class="t"><tr><th>등장인물</th><th>역할</th></tr>
<tr><td>SCAP</td><td>스테롤 감지기 + SREBP 호위</td></tr><tr><td>Insig</td><td>스테롤이 많을 때 SCAP를 붙잡는 닻</td></tr>
<tr><td>골지 단백질 분해효소 (S1P, S2P)</td><td>SREBP를 잘라 핵으로 보냄</td></tr></table>
<div class="boxg">표적 유전자: <g>HMG-CoA 환원효소, LDL 수용체</g> → 스타틴이 LDL 수용체를 늘리는 원리.</div>"""),

dict(img=80, slide=80, title="스테로이드 호르몬", sub="steroid hormones",
kw=["콜레스테롤 → 프레그네놀론", "부신 · 생식샘"],
sum="소제목 슬라이드. 콜레스테롤에서 곁사슬을 자르고 산화해 스테로이드 호르몬을 만든다.",
tr="""<p><b>스테로이드 호르몬</b></p>""",
ex="""<p>Summary 4: “Steroid hormones are formed by <b>side-chain cleavage and oxidation</b> of cholesterol.”</p>
<p>장소: <y>부신 피질</y>(코르티솔, 알도스테론), <y>생식샘</y>(테스토스테론, 에스트라디올), 태반(프로제스테론).</p>"""),

dict(img=81, slide=81, title="콜레스테롤에서 나오는 스테로이드 호르몬", sub="Some steroid hormones derived from cholesterol",
kw=["프레그네놀론", "프로제스테론", "코르티솔(당질)", "알도스테론(무기질)", "테스토스테론 → 에스트라디올"],
sum="콜레스테롤 → 프레그네놀론 → 프로제스테론 → ① 코르티솔(당질코르티코이드) ② 코르티코스테론 → 알도스테론(무기질코르티코이드) ③ 테스토스테론 → 에스트라디올.",
tr="""<p><b>콜레스테롤에서 유래한 스테로이드 호르몬</b></p>
<p>콜레스테롤 → <b>프레그네놀론</b> → <b>프로제스테론</b> →</p>
<ul><li><b>코르티솔</b>(당질코르티코이드): 단백질·탄수화물 대사에 영향, 면역 반응·염증·알레르기 반응 억제</li>
<li><b>코르티코스테론</b>(무기질코르티코이드) → <b>알도스테론</b>: 신장에서 Na⁺, Cl⁻, HCO₃⁻ 재흡수 조절</li>
<li><b>테스토스테론</b> → <b>에스트라디올</b>: 남녀 성호르몬, 2차 성징, 여성 생식 주기 조절</li></ul>""",
ex="""<table class="t"><tr><th>계열</th><th>탄소</th><th>대표</th><th>작용</th></tr>
<tr><td>프로제스틴</td><td>C21</td><td>프로제스테론</td><td>임신 유지</td></tr>
<tr><td>당질코르티코이드</td><td>C21</td><td>코르티솔</td><td>혈당 ↑, 항염 (슬라이드 47–48)</td></tr>
<tr><td>무기질코르티코이드</td><td>C21</td><td>알도스테론</td><td>Na⁺ 재흡수, 혈압</td></tr>
<tr><td>안드로젠</td><td>C19</td><td>테스토스테론</td><td>남성 호르몬</td></tr>
<tr><td>에스트로젠</td><td>C18</td><td>에스트라디올</td><td>A 고리 방향족화(아로마테이스)</td></tr></table>"""),

dict(img=82, slide=82, title="곁사슬 절단 — 콜레스테롤 → 프레그네놀론", sub="Side-chain cleavage in the synthesis of steroid hormones",
kw=["시토크롬 P-450", "아드레노독신 / 환원효소", "혼합기능 산화효소", "20,22-다이하이드록시콜레스테롤", "데스몰레이스", "아이소카프로알데하이드"],
sum="P-450 곁사슬 절단 효소가 NADPH 2개, O₂ 2개로 C20·C22에 –OH를 붙이고(혼합기능 산화효소), 데스몰레이스가 C20–C22 사이를 잘라 프레그네놀론(C21) + 아이소카프로알데하이드(C6).",
tr="""<p><b>스테로이드 호르몬 합성에서 곁사슬 절단</b></p>
<p>콜레스테롤 —(<b>혼합기능 산화효소</b>: cyt P-450, 아드레노독신(Fe-S), 아드레노독신 환원효소(플래보단백질); 2O₂ → 2H₂O, 2NADPH + 2H⁺ → 2NADP⁺)→ <b>20,22-다이하이드록시콜레스테롤</b> —(<b>데스몰레이스</b>, NADPH + H⁺ + O₂ → NADP⁺ + H₂O)→ <b>아이소카프로알데하이드</b> + <b>프레그네놀론</b></p>""",
ex="""<p>19장 P-450 단원(부신 미토콘드리아)과 같은 장면이야: <g>NADPH → 아드레노독신 환원효소(FAD) → 아드레노독신(Fe-S) → P-450 → O₂</g>.</p>
<ul><li>C27 콜레스테롤 − C6 곁사슬 = <b>C21 프레그네놀론</b></li>
<li>이 단계가 <pk>스테로이드 호르몬 합성의 속도 결정 단계</pk> (ACTH가 조절, 장소 = 미토콘드리아)</li></ul>"""),

dict(img=83, slide=83, title="부신 미토콘드리아의 P-450 — 스테로이드 수산화", sub="Mitochondrial P-450 oxygenases catalyze steroid hydroxylations",
kw=["미토콘드리아 vs 활면소포체", "21-하이드록실레이스", "11β-하이드록실레이스", "알도스테론 합성효소", "아로마테이스"],
sum="스테로이드 합성 효소는 미토콘드리아(곁사슬 절단, 11β-하이드록실레이스, 알도스테론 합성효소)와 활면소포체(17α-하이드록실레이스, 21-하이드록실레이스, 아로마테이스 등)를 오가며 작동한다. 부신 미토콘드리아는 스테로이드 합성에 특화돼 있다.",
tr="""<p><b>미토콘드리아 P-450 산소화효소가 스테로이드 수산화를 촉매한다</b></p>
<p>그림: 프로제스틴(C21) · 무기질코르티코이드(C21) · 당질코르티코이드(C21) · 안드로젠(C19) · 에스트로젠(C18) 합성 지도. 효소 위치: <b>미토콘드리아</b>(빨강) / <b>활면소포체</b>(초록)</p>
<p><b>스테로이드 합성에 특화된 부신의 미토콘드리아</b> (전자현미경 사진)</p>""",
ex="""<table class="t"><tr><th>효소</th><th>위치</th><th>결핍 시</th></tr>
<tr><td>곁사슬 절단(CYP11A1)</td><td>미토</td><td>모든 스테로이드 ↓</td></tr>
<tr><td>21-하이드록실레이스</td><td>소포체</td><td><b>선천성 부신 과형성</b>(가장 흔함): 코르티솔·알도스테론 ↓, 안드로젠 ↑</td></tr>
<tr><td>11β-하이드록실레이스</td><td>미토</td><td>코르티솔 ↓</td></tr>
<tr><td>아로마테이스</td><td>소포체</td><td>에스트로젠 ↓ (억제제 = 유방암 치료)</td></tr></table>
<p class="note">19장 개념 22(P-450)와 같은 그림. 부신 미토콘드리아는 관 모양 크리스타가 특징.</p>"""),

dict(img=84, slide=84, title="지질 운반", sub="Lipid transport",
kw=["지질단백질", "택배 트럭"],
sum="소제목 슬라이드. 물에 녹지 않는 지질(TAG, 콜레스테롤)을 혈액으로 나르려면 단백질 껍데기를 씌운 택배 상자(지질단백질)에 담아야 한다.",
tr="""<p><b>지질 운반</b></p>
<p>그림: 상자를 나르는 택배 트럭</p>""",
ex="""<p>기름은 물(혈장)에 안 녹으니까 <y>바깥은 친수성(인지질 머리, 단백질), 속은 소수성(TAG, 콜레스테릴 에스터)</y>인 공 모양 입자에 담아 날라. 이게 지질단백질이고, 겉의 단백질(아포지질단백질)이 <b>주소 라벨</b> 역할(수용체 결합).</p>"""),

dict(img=85, slide=85, title="기름진 식사 후 혈장이 우윳빛", sub="Blood plasma after a fast vs after a high-fat meal",
kw=["킬로미크론", "식후 혈장 탁함"],
sum="공복 혈장(왼쪽)은 맑고, 기름진 식사 후 혈장(오른쪽)은 킬로미크론 때문에 우윳빛으로 뿌옇다.",
tr="""<p>공복 후(왼쪽)와 고지방 식사 후(오른쪽)에 채취한 혈장. 기름진 식사 후 만들어진 <b>킬로미크론</b>이 혈장을 <b>우윳빛</b>으로 만든다.</p>""",
ex="""<p>킬로미크론은 지질단백질 중 <y>가장 크고(지름 최대 ~500 nm) 가장 가벼워서</y> 빛을 산란시켜 혈장이 탁해져.</p>
<div class="box"><span class="tag">임상</span>지질 검사(중성지방)를 <b>12시간 공복</b> 후 하는 이유. 식후엔 킬로미크론 때문에 TAG가 크게 올라가.</div>"""),

dict(img=86, slide=86, title="지질단백질의 구조 — LDL과 킬로미크론", sub="Cholesterol and other lipids are carried on plasma lipoproteins",
kw=["인지질 단일층", "유리 콜레스테롤", "핵: TAG + 콜레스테릴 에스터", "ApoB-100 (LDL)", "ApoB-48 · C-II · C-III (킬로미크론)"],
sum="지질단백질은 인지질 단일층 + 유리 콜레스테롤 + 아포지질단백질 껍질 속에 TAG와 콜레스테릴 에스터를 담는다. LDL엔 ApoB-100 하나, 킬로미크론엔 ApoB-48과 C-II·C-III 등.",
tr="""<p><b>콜레스테롤과 다른 지질은 혈장 지질단백질에 실려 운반된다</b></p>
<p><b>저밀도 지질단백질(LDL)의 구조</b>: 인지질 단일층, <b>ApoB-100</b>, 중성지방, 유리(비에스터화) 콜레스테롤, 콜레스테릴 에스터</p>
<p><b>킬로미크론</b>: 아포지질단백질(B-48, C-III, C-II), 콜레스테롤, 인지질, 중성지방과 콜레스테릴 에스터</p>""",
ex="""<p>세포막(이중층)과 달리 지질단백질은 <b>단일층</b>이야 — 꼬리는 속(기름 핵), 머리는 밖(혈장)을 향해.</p>
<table class="t"><tr><th>아포단백질</th><th>어디</th><th>역할</th></tr>
<tr><td>B-48</td><td>킬로미크론</td><td>장에서 만든 표지</td></tr>
<tr><td><b>B-100</b></td><td>VLDL, LDL</td><td><b>LDL 수용체</b>에 결합</td></tr>
<tr><td>C-II</td><td>킬로미크론, VLDL</td><td>지단백질 지질분해효소(LPL) 활성화</td></tr>
<tr><td>A-I</td><td>HDL</td><td>LCAT 활성화, ABCA1과 결합</td></tr>
<tr><td>E</td><td>여러 종</td><td>간 수용체 결합 (슬라이드 94 ApoE4)</td></tr></table>"""),

dict(img=87, slide=87, title="지질단백질 4종 비교 (표 21-1)", sub="Major classes of human plasma lipoproteins",
kw=["밀도 ↑ = 단백질 ↑", "킬로미크론 TAG 85%", "VLDL TAG 50%", "LDL 콜레스테릴 에스터 37%", "HDL 단백질 55%"],
sum="밀도는 킬로미크론 < VLDL < LDL < HDL. 단백질 비율이 높을수록 무겁다. 킬로미크론·VLDL은 TAG 운반, LDL은 콜레스테롤 운반(에스터 37%), HDL은 단백질이 절반 이상.",
tr="""<table class="t"><tr><th>지질단백질</th><th>밀도(g/mL)</th><th>단백질</th><th>인지질</th><th>유리 콜</th><th>콜 에스터</th><th>TAG</th></tr>
<tr><td>킬로미크론</td><td>&lt;1.006</td><td>2</td><td>9</td><td>1</td><td>3</td><td><b>85</b></td></tr>
<tr><td>VLDL</td><td>0.95–1.006</td><td>10</td><td>18</td><td>7</td><td>12</td><td><b>50</b></td></tr>
<tr><td>LDL</td><td>1.006–1.063</td><td>23</td><td>20</td><td>8</td><td><b>37</b></td><td>10</td></tr>
<tr><td>HDL</td><td>1.063–1.210</td><td><b>55</b></td><td>24</td><td>2</td><td>15</td><td>4</td></tr></table>
<p>(조성: 무게 %) 전자현미경 사진: 킬로미크론(×60,000), VLDL·LDL·HDL(×180,000)</p>""",
ex="""<p>기름은 물보다 가볍고 단백질은 무거워. 그래서 <y>지질 많을수록 가볍고 크고, 단백질 많을수록 무겁고 작아</y>.</p>
<div class="boxg">한 줄: <g>킬로미크론(장 → 식이 TAG) · VLDL(간 → TAG) · LDL(콜레스테롤 배달, ‘나쁜’) · HDL(콜레스테롤 회수, ‘좋은’)</g></div>
<p class="note">크기 순서는 정반대: 킬로미크론 &gt; VLDL &gt; LDL &gt; HDL.</p>"""),

dict(img=88, slide=88, title="이상지질혈증 보험급여 기준 (2014)", sub="바뀐 보험급여 기준 알아두자 (2014.05.13)",
kw=["LDL 기준으로 변경", "위험요인 5가지", "TG 500 mg/dL", "생활습관"],
sum="이상지질혈증 약 급여 기준이 총콜레스테롤에서 LDL 기준으로 바뀌고(위험요인 수·질환에 따라 160/130/100/70 mg/dL), 위험요인이 명시되었으며, 고중성지방은 500(위험요인 있으면 200) mg/dL로 단순화되고, 생활습관 병행이 강조되었다.",
tr="""<p><b>change 1</b> ‘총콜레스테롤 → LDL’ 기준 변경: LDL <b>160 mg/dL 이상</b>(위험요인 1개 이하), <b>130</b> 이상(위험요인 2개 이상), <b>100</b> 이상(관상동맥질환 위험자), <b>70</b> 이상(급성관동맥증후군). (건강검진 기준치 70–130, &lt;100 정상)</p>
<p><b>change 2</b> 위험요인 명시 (NCEP ATP III): 흡연, 고혈압(약 복용 또는 140/90 mmHg 이상), 낮은 HDL(&lt;40 mg/dL), 관상동맥질환 조기 발병 가족력(남 55세 미만, 여 65세 미만), 나이(남 45세 이상, 여 55세 이상)</p>
<p><b>change 3</b> 고중성지방: ‘두 번 연속’ 조항 삭제 → <b>500 mg/dL</b> 이상이면 급여, 위험요인 있으면 <b>200</b> 이상</p>
<p><b>change 4</b> 생활습관 변화 중요성 강조: “치료제를 처방할 때는 생활습관 변화를 병행해 치료 효과를 극대화해야 한다”</p>""",
ex="""<table class="t"><tr><th>대상</th><th>LDL 투약 기준 (mg/dL)</th></tr>
<tr><td>위험요인 0–1개</td><td>≥ 160</td></tr><tr><td>위험요인 2개 이상</td><td>≥ 130</td></tr>
<tr><td>관상동맥질환 위험자(당뇨 등)</td><td>≥ 100</td></tr><tr><td>급성관동맥증후군</td><td>≥ 70</td></tr></table>
<div class="box"><span class="tag">약학</span>위험이 클수록 LDL 목표가 낮아져. HDL ≥ 60 mg/dL은 위험요인 1개를 빼 주는 ‘보호 인자’. (현재 지침은 이후 개정됐을 수 있어 — 강의 슬라이드 기준으로 공부.)</div>"""),

dict(img=89, slide=89, title="지질단백질과 지질 운반 — 전체 지도", sub="Lipoproteins and lipid transport",
kw=["외인성 경로(식이)", "내인성 경로(간)", "역콜레스테롤 수송", "장간 순환"],
sum="① 외인성: 장 → 킬로미크론(림프) → LPL로 TAG 내림 → 잔여물은 간으로. ② 내인성: 간 → VLDL → IDL → LDL → LDL 수용체로 조직·간에 콜레스테롤 배달. ③ 역수송: HDL이 조직·대식세포의 콜레스테롤을 간으로. ④ 담즙산은 장간 순환.",
tr="""<p><b>지질단백질과 지질 운반</b></p>
<p><b>외인성 경로</b>: 식이 지방 → ① 장세포에서 킬로미크론 → 림프계 → ② 모세혈관에서 FFA (근육·지방·유선) → ③ 킬로미크론 잔여물 → ④ 간</p>
<p><b>내인성 경로</b>: ⑤ 간: C → CE → VLDL → ⑥ 모세혈관 FFA → IDL → LDL → ⑦ 부신·생식샘, 근육, 지방 → ⑧ LDL → ⑨ LDL 수용체(간)</p>
<p><b>역콜레스테롤 수송</b>: ⑩ HDL → ⑪ 대식세포·거품세포의 C → ⑫ SR-BI 수용체(간) → ⑬</p>
<p><b>장간 순환</b>: ⑭ 담즙산 → 담낭 → 장 → 간</p>""",
ex="""<table class="t"><tr><th>경로</th><th>출발</th><th>운반체</th><th>도착</th></tr>
<tr><td>외인성</td><td>장(식이)</td><td>킬로미크론</td><td>근육·지방(TAG) → 간(잔여물)</td></tr>
<tr><td>내인성</td><td>간</td><td>VLDL → IDL → <b>LDL</b></td><td>말초 조직 (LDL 수용체)</td></tr>
<tr><td>역수송</td><td>말초·대식세포</td><td><b>HDL</b></td><td>간 (SR-BI)</td></tr></table>
<div class="boxg">공통 열쇠: <g>지단백질 지질분해효소(LPL)</g>가 모세혈관 벽에서 TAG를 지방산으로 잘라 조직에 넘겨 줘(ApoC-II가 활성화).</div>"""),

dict(img=90, slide=90, title="HDL 성숙과 ABCA1 — 탄지어병", sub="ABCA1 defective in Tangier disease, familial HDL deficiency",
kw=["ApoA-I", "ABCA1", "ABCG1", "성숙 HDL", "SR-B 수용체", "탄지어병"],
sum="빈 ApoA-I가 ABCA1을 통해 거품세포의 유리 콜레스테롤을 받고, ABCG1로 더 받아 성숙 HDL이 된다. HDL은 콜레스테릴 에스터를 VLDL/LDL에 넘기거나 간 SR-B 수용체로 직접 전달. ABCA1이 고장 나면 탄지어병(가족성 HDL 결핍).",
tr="""<p><b>ABCA1 결함 = 탄지어병, 가족성 HDL 결핍</b></p>
<p>ApoA-I → (<b>ABCA1</b>, 거품세포의 유리 콜레스테롤) → ApoA-I → (<b>ABCG1</b>) → <b>성숙 HDL</b>(CE, TAG) → (CE ⇄ TAG 교환) → VLDL/LDL(ApoB) → 간 LDL 수용체 / 성숙 HDL → 간 <b>SR-B 수용체</b></p>
<p><b>ABCA1</b>(ATP 결합 카세트 아과 A 구성원 1): <b>콜레스테롤 유출 조절 단백질(CERP)</b>로도 알려짐<br><b>ABCG1</b>(ATP 결합 카세트 아과 G 구성원 1): 콜레스테롤과 인지질 수송</p>""",
ex="""<ol><li>간·장이 만든 <b>지질이 거의 없는 ApoA-I</b> (원반 모양)</li>
<li>대식세포의 <b>ABCA1</b>(ATP로 펌프)이 유리 콜레스테롤·인지질을 ApoA-I로 내보냄</li>
<li>LCAT가 에스터화 → 속으로 → 둥근 <b>성숙 HDL</b>, ABCG1로 더 받음</li>
<li>간으로: SR-B1이 콜레스테릴 에스터만 선택적으로 흡수, 또는 CETP로 LDL에 넘김</li></ol>
<div class="box"><span class="tag">임상</span><b>탄지어병</b>: ABCA1 결함 → HDL 거의 0, 주황색 편도, 대식세포에 콜레스테롤 축적.</div>"""),

dict(img=91, slide=91, title="수용체 매개 세포내이입 — LDL 흡수", sub="Uptake of cholesterol by receptor-mediated endocytosis",
kw=["LDL 수용체", "ApoB-100", "엔도솜", "수용체 재활용", "리소좀 분해"],
sum="① LDL 수용체가 소포체·골지를 거쳐 세포막으로 ② ApoB-100에 결합 → 세포내이입 시작 ③ 엔도솜으로 들어감 ④ 수용체는 분리돼 세포막으로 재활용 ⑤ 엔도솜이 리소좀과 융합 ⑥ 분해 → 아미노산, 지방산, 콜레스테롤 (→ 지질 방울).",
tr="""<p><b>수용체 매개 세포내이입에 의한 콜레스테롤 흡수</b></p>
<ol><li><b>LDL 수용체</b>가 조면소포체에서 합성되어 골지를 거쳐 세포막으로 이동</li>
<li>LDL 수용체가 LDL의 <b>ApoB-100</b>에 결합해 세포내이입 시작</li>
<li>LDL이 <b>엔도솜</b> 안으로 들어감</li>
<li>LDL 수용체는 소포로 분리되어 <b>세포 표면으로 재활용</b></li>
<li>LDL을 담은 엔도솜이 <b>리소좀</b>과 융합</li>
<li>리소좀 효소가 ApoB-100과 콜레스테릴 에스터를 분해 → 아미노산, 지방산, 콜레스테롤 방출</li></ol>""",
ex="""<p>Michael Brown(마이클 브라운)·Joseph Goldstein(조지프 골드스타인), 1985 노벨상.</p>
<div class="boxg">들어온 콜레스테롤의 효과 (슬라이드 77과 연결): <g>HMG-CoA 환원효소 ↓ · LDL 수용체 합성 ↓ · ACAT ↑</g></div>
<div class="box"><span class="tag">임상</span><b>가족성 고콜레스테롤혈증</b>: LDL 수용체 결함 → LDL이 혈액에 남아 매우 높음 → 젊은 나이 심근경색. Summary 3: “Cholesteryl esters enter cells by <b>receptor-mediated endocytosis</b>.”</div>"""),

dict(img=92, slide=92, title="LDL은 죽상경화, HDL은 역콜레스테롤 수송", sub="High levels of LDL cause atherosclerosis · HDL clears cholesterol by reverse cholesterol transport",
kw=["‘나쁜’ LDL", "‘좋은’ HDL", "역콜레스테롤 수송"],
sum="혈중 LDL 콜레스테롤이 높으면 혈관 벽에 쌓여 죽상경화를 일으키고(그림의 악당), HDL은 쌓인 콜레스테롤을 쓸어 간으로 가져가 치운다(청소부).",
tr="""<p><b>LDL에 결합한 콜레스테롤이 높으면 죽상경화가 생긴다</b></p>
<p><b>HDL은 역콜레스테롤 수송으로 콜레스테롤을 치운다</b></p>
<p>그림: 혈관 속에서 콜레스테롤을 뿌리는 LDL 악당, 빗자루로 쓸어 내는 HDL</p>""",
ex="""<table class="t"><tr><th></th><th>LDL</th><th>HDL</th></tr>
<tr><td>방향</td><td>간 → 말초 (배달)</td><td>말초 → 간 (회수)</td></tr>
<tr><td>많으면</td><td>죽상경화 위험 ↑</td><td>위험 ↓</td></tr>
<tr><td>별명</td><td>나쁜 콜레스테롤</td><td>좋은 콜레스테롤</td></tr></table>
<p class="note">사실 콜레스테롤 분자 자체는 같고, <b>어느 차에 타서 어디로 가느냐</b>가 다를 뿐이야.</p>"""),

dict(img=93, slide=93, title="죽상경화반이 생기는 과정 (그림 21-46)", sub="Atherosclerosis: oxidized LDL → macrophage → foam cell → plaque",
kw=["산화 LDL", "단핵구 → 대식세포", "거품세포", "세포자멸·괴사", "콜레스테롤이 많은 반"],
sum="① 산화된 지질단백질이 동맥벽 기질에 쌓임 ② 단핵구가 끌려옴 ③ 대식세포로 분화 ④ 지질단백질을 먹어 거품세포 ⑤ 유리 콜레스테롤이 막·방울에 쌓임 ⑥ 세포자멸·괴사, 조직 손상 ⑦ 콜레스테롤이 많은 반(플라크) 형성.",
tr="""<ol><li><b>산화된 지질단백질</b>이 뭉쳐 세포외 기질에 달라붙음</li>
<li>산화 지질단백질 부위로 <b>단핵구</b>가 끌려옴</li><li>단핵구가 <b>대식세포</b>로 분화</li>
<li>거품세포(대식세포)가 지질단백질을 삼킴</li><li>유리 콜레스테롤이 막과 방울에 쌓임</li>
<li>세포자멸·괴사, 조직 손상</li><li><b>콜레스테롤이 많은 반(plaque)</b> 형성</li></ol>""",
ex="""<p>핵심은 <y>산화</y>: 정상 LDL이 아니라 ROS로 산화된 LDL을 대식세포의 청소 수용체(scavenger receptor)가 <b>조절 없이</b> 마구 먹어서 콜레스테롤로 가득 찬 <b>거품세포(foam cell)</b>가 돼.</p>
<div class="boxg">HDL의 ABCA1 경로(슬라이드 90)가 바로 이 거품세포에서 콜레스테롤을 빼내는 길 → 그래서 HDL이 보호적.</div>
<p class="note">반이 터지면 혈전 → 심근경색·뇌졸중. 스타틴은 LDL ↓ + 반 안정화.</p>"""),

dict(img=94, slide=94, title="아포지질단백질 E4와 알츠하이머", sub="apolipoprotein E4",
kw=["APOE4", "지질 배달 부족", "β-아밀로이드 응집", "신경세포 내 절단 → 미토콘드리아 방해"],
sum="APOE4 대립유전자는 알츠하이머병의 가장 강한 유전 위험인자. 작은 E4가 정상 APOE와 경쟁해 신경세포로 지질을 덜 배달하고 β-아밀로이드 응집을 늘리며, 신경세포 안의 E4는 잘려 조각이 미토콘드리아를 방해해 신경 퇴행을 일으킨다.",
tr="""<p><b>아포지질단백질 E4</b></p>
<p>(1a) 크기가 작은 E4가 정상 크기의 다른 APOE 변이체와 <b>경쟁</b>해 → <b>지질 배달이 불충분</b>해지고 → <b>β-아밀로이드(Aβ) 응집</b> 증가 → (2) 병든 신경세포 → (3) 알츠하이머병</p>
<p>(1b) 신경세포 안에서 만들어진 E4는 <b>단백질 분해로 잘려</b> 조각이 되고, 이 조각이 <b>미토콘드리아 활동을 방해</b>해 신경 퇴행과 알츠하이머병으로 이어진다.</p>""",
ex="""<p>APOE는 뇌에서 콜레스테롤·지질을 나르는 주 운반 단백질이야 (뇌는 혈뇌장벽 때문에 LDL을 못 받고 자체 운반).</p>
<table class="t"><tr><th>대립유전자</th><th>알츠하이머 위험</th></tr>
<tr><td>E2</td><td>낮음(보호)</td></tr><tr><td>E3</td><td>보통(가장 흔함)</td></tr><tr><td><b>E4</b></td><td><b>높음</b> (1개 ~3배, 2개 ~10배 이상)</td></tr></table>
<p class="note">19장 미토콘드리아 기능 장애와 연결되는 내용. 앞의 플라스말로겐 감소도 알츠하이머와 관련.</p>"""),

dict(img=95, slide=95, title="(빈 슬라이드)", sub="—",
kw=["—"],
sum="원본 강의자료의 빈 슬라이드야.",
tr="""<p class="note">내용 없음</p>""",
ex="""<p class="note">원본 PDF 95쪽이 비어 있어서 번역·설명도 비워 뒀어.</p>"""),

dict(img=96, slide=96, title="21.4 · 지질 운반 요약", sub="Summary",
kw=["4단계 콜레스테롤 합성", "지질단백질 운반", "수용체 매개 세포내이입", "곁사슬 절단 · 산화"],
sum="① 콜레스테롤은 아세틸-CoA에서 4단계로 ② 콜레스테롤과 지질은 혈장 지질단백질로 운반 ③ 콜레스테릴 에스터는 수용체 매개 세포내이입으로 세포에 들어감 ④ 스테로이드 호르몬은 콜레스테롤의 곁사슬 절단과 산화로 만들어진다.",
tr="""<ol><li>콜레스테롤은 아세틸-CoA로부터 <b>4단계</b>로 만들어진다.</li>
<li>콜레스테롤과 다른 지질은 <b>혈장 지질단백질</b>에 실려 운반된다.</li>
<li>콜레스테릴 에스터는 <b>수용체 매개 세포내이입</b>으로 세포에 들어간다.</li>
<li>스테로이드 호르몬은 콜레스테롤의 <b>곁사슬 절단과 산화</b>로 만들어진다.</li></ol>""",
ex="""<div class="boxg">숫자 카드: <g>C2 → C6 메발론산 → C5 IPP → C10 → C15 → C30 스쿠알렌 → C27 콜레스테롤 → C21 프레그네놀론 → C19 안드로젠 → C18 에스트로젠</g></div>
<div class="box"><span class="tag">약물 표적 총정리</span><b>스타틴</b> HMG-CoA 환원효소 · <b>NSAID</b> COX · <b>스테로이드</b> PLA₂ · <b>TZD</b> PPARγ · <b>몬테루카스트</b> LTD₄ 수용체 · <b>아졸·테르비나핀</b> 에르고스테롤 합성 · <b>아로마테이스 억제제</b> 에스트로젠 합성</div>"""),
]
