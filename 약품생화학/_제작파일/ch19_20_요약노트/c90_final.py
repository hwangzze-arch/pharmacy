from parts import *

pairs = dict(t="r", id="f-pairs", html=f"""
<div class="hd"><span class="bd">FINAL ①</span><div class="tt"><h1>헷갈리는 짝 총정리 — 시험 직전 10분</h1><div class="sb">Confusing pairs · 다답형 O/X의 함정은 대부분 여기서 나온다</div></div><span class="pt">{PF}</span></div>
<div class="body"><div class="main full">
<table class="t"><tr><th style="width:22%">헷갈리는 짝</th><th>A</th><th>B</th></tr>
<tr><td>억제제 vs 짝풀림제</td><td>억제제(로테논·안티마이신·CN⁻): 전자 흐름 <b>정지</b> → O₂ ✕, ATP ✕, NADH ↑</td><td>짝풀림제(DNP·FCCP·발리노마이신·UCP1): 흐름 <b>↑</b> → O₂ ↑, ATP ✕, 열 ↑, P/O ↓</td></tr>
<tr><td>올리고마이신 vs DNP</td><td>F<sub>o</sub> 차단 → ATP ✕ → (짝지음) O₂도 ✕</td><td>H⁺ 누출 → O₂ 다시 ↑, ATP는 여전히 ✕</td></tr>
<tr><td>Complex I vs II</td><td>NADH, FMN·Fe-S, <b>H⁺ 4</b>, 로테논</td><td>숙신산, FAD·Fe-S·헴 b, <b>H⁺ 0</b>, 시트르산 회로 효소</td></tr>
<tr><td>Q vs cyt c</td><td>지용성·막 속, <b>2e⁻ + 2H⁺</b>, I/II → III</td><td>수용성·막사이공간, <b>1e⁻</b>, III → IV (+ 세포자멸 신호)</td></tr>
<tr><td>Complex IV의 8H⁺</td><td>4개 = 물의 재료(substrate)</td><td>4개 = P쪽으로 펌프</td></tr>
<tr><td>F<sub>o</sub> vs F<sub>1</sub></td><td>막 속 H⁺ 통로, ab₂c<sub>n</sub>, 올리고마이신 감수성</td><td>기질 쪽 촉매, α₃β₃γδε, 떼어 내면 ATPase</td></tr>
<tr><td>회전자 vs 고정자</td><td>c 고리 + γ + ε (돈다)</td><td>a + b₂ + δ + α₃β₃ (붙잡힘)</td></tr>
<tr><td>F₁ 위 vs 용액</td><td>ATP ⇌ ADP + Pᵢ, ΔG′° ≈ <b>0</b> (K′eq 2.4)</td><td>ΔG′° = <b>−30.5</b> kJ/mol</td></tr>
<tr><td>ANT vs 인산 전위효소</td><td>역수송: ATP⁴⁻ out / ADP³⁻ in (Δψ 소비), 아트락틸로사이드</td><td>공동수송: H₂PO₄⁻ + H⁺ in (ΔpH 소비)</td></tr>
<tr><td>말산-아스파르트산 vs 글리세롤 3-P 셔틀</td><td>간·심장·신장, NADH → I, <b>2.5</b></td><td>골격근·뇌, FAD → Q, <b>1.5</b></td></tr>
<tr><td>IF₁ vs UCP1</td><td>IF₁: 저산소(pH &lt; 6.5) 이량체 → ATP <b>가수분해</b> 차단</td><td>UCP1(thermogenin): H⁺ 통로 → 짝풀림 → 열</td></tr>
<tr><td>LHON vs MERRF</td><td>ND4(I)·cyt b 염기 하나 → <b>실명</b></td><td>tRNA<sup>Lys</sup> → 근육 경련·근력 약화</td></tr>
<tr><td>미토 vs 엽록체</td><td>NADH → O₂, H⁺ 기질 → <b>막사이공간</b>, Δψ + ΔpH</td><td>H₂O → NADP⁺, H⁺ 스트로마 → <b>내강</b>, 주로 ΔpH(3)</td></tr>
<tr><td>PSII vs PSI</td><td>P680, 페오피틴-퀴논형, 물 분해(O₂), DCMU</td><td>P700, Fe-S형, A₀ → 필로퀴논 → Fe-S → Fd → NADPH</td></tr>
<tr><td>비순환 vs 순환</td><td>PSII + PSI → O₂ + NADPH + ATP</td><td>PSI만(Fd → b₆f → PC) → <b>ATP만</b></td></tr>
<tr><td>엑시톤 전달 vs 전자 전달</td><td>안테나: <b>에너지</b>만 이웃으로</td><td>반응 중심: <b>전자</b>가 수용체로(전하 분리)</td></tr>
<tr><td>루비스코 활성화</td><td>activase = <b>ATP</b>로 RuBP 치우기</td><td>카바모일화는 <b>CO₂</b>가 Lys²⁰¹에(비효소적) → Mg²⁺</td></tr>
<tr><td>캘빈 FBPase vs 해당 PFK-1</td><td>FBP → F6P + Pᵢ (캘빈·당신생)</td><td>F6P + ATP → FBP (해당) — 캘빈 효소 아님</td></tr></table>
</div></div>""")

nums = dict(t="r", id="f-nums", html=f"""
<div class="hd"><span class="bd">FINAL ②</span><div class="tt"><h1>숫자 · 공식 카드 — 빈칸 문제는 여기서 나온다</h1><div class="sb">Numbers & formulas to memorize</div></div><span class="pt">{PF}</span></div>
<div class="body"><div class="main">
<table class="t"><tr><th>항목</th><th>숫자</th></tr>
<tr><td>H⁺ 펌프 (전자 2개당) I · II · III · IV</td><td><b>4 · 0 · 4 · 2</b> → NADH 10, 숙신산 6</td></tr>
<tr><td>ATP 1개당 H⁺</td><td><b>4</b> (합성 ~3 + 수송 1)</td></tr>
<tr><td>P/O (NADH / 숙신산)</td><td><b>2.5 / 1.5</b> (옛 값 3 / 2)</td></tr>
<tr><td>포도당 1개 ATP</td><td><b>30 또는 32</b> (NADH 10 · FADH₂ 2 · 기질수준 4)</td></tr>
<tr><td>ΔE′° NADH → O₂ / ΔG′°</td><td><b>1.14 V / −220 kJ/mol</b></td></tr>
<tr><td>E′° NAD⁺ · Q · cyt c · O₂</td><td><b>−0.32 · +0.045 · +0.254 · +0.816 V</b></td></tr>
<tr><td>F₁ 위 K′eq / Kd(ATP) / Kd(ADP)</td><td><b>2.4 / ≤ 10⁻¹² M / ≈ 10⁻⁵ M</b></td></tr>
<tr><td>γ 1회전</td><td>ATP <b>3</b>개 (120°마다 1)</td></tr>
<tr><td>Complex IV 소단위체 / I</td><td><b>13 / 43</b>(세균 14)</td></tr>
<tr><td>수용체 조절비</td><td><b>≥ 10</b></td></tr>
<tr><td>IF₁ 작동 pH</td><td><b>&lt; 6.5</b> (이량체)</td></tr>
<tr><td>ROS가 되는 O₂ 비율</td><td><b>0.1–4 %</b></td></tr>
<tr><td>mtDNA</td><td>16,569 bp · 유전자 37 (단백질 <b>13</b> · tRNA 22 · rRNA 2) · 핵 유래 미토 단백질 ~900</td></tr>
<tr><td>LHCII 단량체</td><td>엽록소 a <b>7</b> · b <b>5</b> · 루테인 <b>2</b>, 삼량체</td></tr>
<tr><td>O₂ 1개 / 포도당 1개</td><td>광자 4(PSII만) · <b>8</b>(Z 도식) / <b>48</b></td></tr>
<tr><td>O₂ 1개당 H⁺ · ATP</td><td><b>12</b>(OEC 4 + b₆f 8) · ΔpH 3 · ATP <b>~3</b></td></tr>
<tr><td>1 einstein · 700 nm</td><td>6.022 × 10²³ 광자 · ≈ <b>170 kJ</b></td></tr>
<tr><td>캘빈 (CO₂ 3개)</td><td><b>3 · 6 · 6 · 1 · 5 · 3</b>, ATP 9 · NADPH 6 (CO₂ 1개당 3 : 2)</td></tr>
<tr><td>포도당 1개 (캘빈)</td><td>ATP <b>18</b> · NADPH <b>12</b></td></tr>
<tr><td>트랜스케톨레이스</td><td><b>6+3 = 4+5</b> · <b>7+3 = 5+5</b> (TPP)</td></tr>
<tr><td>루비스코</td><td>Form I <b>L₈S₈</b> / Form II <b>L₂</b> · Lys<b>²⁰¹</b> · Mg²⁺</td></tr></table>
</div><div class="side">
<div class="fbox"><div class="sec f">📐 공식 4개</div>
<span class="fx">ΔG′° = −nℱΔE′°</span><br>ΔE′° = E′°(받개) − E′°(주개), ℱ = 96.5 kJ/V·mol<br>
<span class="fx">ΔG = 2.3RT ΔpH + ℱΔψ</span><br>양성자 1몰을 퍼내는 데 드는 에너지 (화학 + 전기)<br>
<span class="fx">E = hν = hc/λ</span><br>× 6.022 × 10²³ → kJ/einstein, λ는 m 단위!<br>
<span class="fx">P/O = (펌프된 H⁺) ÷ 4</span></div>
<div class="card tip"><div class="ct">📌 계산 요령 (계산기 없이)</div>96.5 × 2 ≈ 193 → 193 × 1.14 ≈ 220 · 193 × 0.77 ≈ 149 · 193 × 0.264 ≈ 51<br>최대 ATP = |ΔG′°| ÷ 30.5 → 소수점 버림</div>
<div class="card ana"><div class="ct">🎈 한 문장 요약</div>전자는 <b>낮은 전위 → 높은 전위</b>로 굴러 내려가며 H⁺를 퍼 올리고, H⁺는 ATP 합성효소의 물레방아를 돌리며 내려온다. 엽록체는 빛으로 전자를 두 번 퍼 올려 같은 일을 한다.</div>
</div></div>""")

ABBR = [
("ADP / ATP", "Adenosine Di/TriPhosphate", "아데노신 이인산/삼인산 — 세포의 충전 전 / 충전된 배터리"),
("ANT", "Adenine Nucleotide Translocase", "아데닌 뉴클레오타이드 전위효소 — ATP 내보내고 ADP 들이는 역수송체"),
("Apaf-1", "Apoptosis Protease Activating Factor-1", "세포자멸 프로테이스 활성 인자 — cyt c와 apoptosome 형성"),
("BAT", "Brown Adipose Tissue", "갈색지방조직 — 미토가 많아 열을 내는 지방"),
("1,3-BPG", "1,3-BisPhosphoGlycerate", "1,3-이인산글리세르산 — 3-PG가 ATP로 인산화된 것"),
("CF₀CF₁", "Chloroplast F₀F₁", "엽록체 ATP 합성효소"),
("CN⁻ / CO", "Cyanide / Carbon monoxide", "사이안화물 / 일산화탄소 — Complex IV 억제"),
("CoQ (Q)", "Coenzyme Q = Ubiquinone", "코엔자임 Q, 유비퀴논 — 막 속 2전자 운반체 (QH₂ = 유비퀴놀)"),
("COX", "Cytochrome c OXidase", "시토크롬 c 산화효소 = Complex IV"),
("CYP2E1", "CYtochrome P450 2E1", "시토크롬 P450 2E1 — 타이레놀을 NAPQI로"),
("cyt", "cytochrome", "시토크롬 — 헴 철로 전자 1개씩 나르는 단백질"),
("DCMU", "3-(3,4-DiChlorophenyl)-1,1-DiMethylUrea", "다이클로로페닐 다이메틸요소(디우론) — PSII Q_B 자리 억제 제초제"),
("DCCD", "DiCycloHexylCarbodiimide", "다이사이클로헥실카보다이이미드 — F₀·CF₀ 양성자 통로 차단"),
("DHAP", "DiHydroxyAcetone Phosphate", "다이하이드록시아세톤 인산 — 삼탄당 인산"),
("DNP", "2,4-DiNitroPhenol", "2,4-다이나이트로페놀 — 짝풀림제"),
("E4P / Xu5P / R5P / Ru5P / S7P", "Erythrose 4-P / Xylulose 5-P / Ribose 5-P / Ribulose 5-P / Sedoheptulose 7-P", "에리트로스 4-인산 / 자일룰로스 / 리보스 / 리불로스 5-인산 / 세도헵툴로스 7-인산"),
("ETF", "Electron-Transferring Flavoprotein", "전자전달 플래빈단백질 — 지방산 산화의 전자를 Q로"),
("FAD / FADH₂", "Flavin Adenine Dinucleotide", "플래빈 아데닌 다이뉴클레오타이드 — 1·2전자 운반"),
("FBP / FBPase", "Fructose 1,6-BisPhosphate / -phosphatase", "과당 1,6-이인산 / 그 인산을 떼는 효소"),
("FCCP", "Carbonylcyanide-p-trifluoromethoxyphenylhydrazone", "카보닐사이아나이드 트라이플루오로메톡시페닐하이드라존 — 짝풀림제"),
("Fd / FNR", "Ferredoxin / Ferredoxin:NADP⁺ oxidoreductase", "페레독신 / 페레독신-NADP⁺ 산화환원효소 — NADPH 생성"),
("FMN", "Flavin MonoNucleotide", "플래빈 모노뉴클레오타이드 — Complex I의 첫 수용체"),
("Fe-S", "Iron-Sulfur center", "철-황 중심 — 전자 1개씩 (Rieske = Complex III·b₆f의 Fe-S)"),
("G3P (PGAL)", "Glyceraldehyde 3-Phosphate", "글리세르알데하이드 3-인산 — 캘빈 회로 산물"),
("GPx / GSH / GSSG", "Glutathione Peroxidase / reduced / oxidized Glutathione", "글루타티온 과산화효소(Se) / 환원형 / 산화형 글루타티온"),
("HIF-1", "Hypoxia-Inducible Factor 1", "저산소 유도 인자 1 — 해당 ↑, PDH ↓, ROS ↓"),
("IF₁", "Inhibitory Factor 1", "억제 인자 1 — 저산소 때 ATP 가수분해 차단"),
("Kd / K′eq", "dissociation constant / equilibrium constant", "해리상수(작을수록 꽉 붙음) / 평형상수"),
("LHC(II)", "Light-Harvesting Complex (II)", "집광 복합체 — 빛을 모아 반응 중심에 전달"),
("LHON", "Leber's Hereditary Optic Neuropathy", "레버 유전성 시신경병증 — ND4·cyt b 돌연변이, 실명"),
("MERRF", "Myoclonic Epilepsy and Ragged-Red Fiber disease", "근간대성 간질 및 누더기 적색 섬유병 — tRNA^Lys"),
("MODY", "Maturity-Onset Diabetes of the Young", "젊은이의 성인형 당뇨 — 글루코키나아제 한쪽 결함(MODY2)"),
("MPC", "Mitochondrial Pyruvate Carrier", "미토콘드리아 피루브산 운반체"),
("mtDNA", "mitochondrial DNA", "미토콘드리아 DNA — 모계 유전"),
("NAD⁺ / NADH", "Nicotinamide Adenine Dinucleotide", "니코틴아마이드 아데닌 다이뉴클레오타이드 — ATP 생산용 2전자 운반체"),
("NADP⁺ / NADPH", "NAD Phosphate", "NAD 인산 — 생합성·해독용 환원력 (광합성 최종 산물)"),
("NAPQI", "N-Acetyl-p-BenzoQuinone Imine", "N-아세틸-p-벤조퀴논이민 — 타이레놀의 독성 대사체"),
("ND4", "NADH Dehydrogenase subunit 4", "Complex I 소단위체 4 (mtDNA 유전자)"),
("OEC", "Oxygen-Evolving Complex", "산소 발생 복합체 — Mn₄ 클러스터, 물 분해"),
("P680 / P700", "Pigment absorbing at 680 / 700 nm", "PSII / PSI 반응 중심 엽록소"),
("PC", "PlastoCyanin", "플라스토시아닌 — Cu, b₆f → PSI"),
("PDH", "Pyruvate DeHydrogenase", "피루브산 탈수소효소"),
("3-PG", "3-PhosphoGlycerate", "3-인산글리세르산 — CO₂ 고정의 첫 산물"),
("Pheo", "Pheophytin", "페오피틴 — Mg 없는 엽록소, PSII 첫 수용체"),
("Pᵢ", "inorganic Phosphate", "무기인산"),
("pmf", "proton-motive force", "양성자 구동력 = ΔpH + Δψ"),
("P/O", "Phosphate/Oxygen ratio", "산소 원자 1개당 만든 ATP 수"),
("PQ (PQ_A, PQ_B)", "PlastoQuinone", "플라스토퀴논 — 엽록체판 Q"),
("PSI / PSII", "PhotoSystem I / II", "광계 I(Fe-S형) / 광계 II(페오피틴-퀴논형)"),
("ROS", "Reactive Oxygen Species", "활성산소종 — ·O₂⁻, H₂O₂, ·OH"),
("Rubisco", "RibUlose 1,5-BISphosphate Carboxylase/Oxygenase", "리불로스 1,5-이인산 카복실화/산소화효소"),
("RuBP", "Ribulose 1,5-BisPhosphate", "리불로스 1,5-이인산 — CO₂ 수용체"),
("SBP / SBPase", "Sedoheptulose 1,7-BisPhosphate / -phosphatase", "세도헵툴로스 1,7-이인산 / 그 가수분해효소"),
("SOD", "SuperOxide Dismutase", "초과산화물 불균등화효소 — ·O₂⁻ → H₂O₂"),
("TPP", "Thiamine PyroPhosphate", "티아민 피로인산(비타민 B₁) — 트랜스케톨레이스 보조효소"),
("UCP1", "UnCoupling Protein 1 = thermogenin", "짝풀림 단백질 1 — 갈색지방 열 생산"),
("ΔE′° / ΔG′° / Δψ / ΔpH", "standard reduction potential difference / standard free-energy change / membrane potential / pH gradient", "표준환원전위 차 / 표준 자유에너지 변화 / 막전위 / pH 차"),
]


def abbr_page(i, rows, pid):
    trs = "".join(f"<tr><td><b>{a}</b></td><td>{b}</td><td>{c}</td></tr>" for a, b, c in rows)
    return dict(t="r", id=pid, html=f"""
<div class="hd"><span class="bd">FINAL ③</span><div class="tt"><h1>약어 총정리 {i} — 영어 전체 이름 · 한글 뜻</h1><div class="sb">Abbreviations (alphabetical)</div></div><span class="pt">{PF}</span></div>
<div class="body"><div class="main full"><table class="t" style="font-size:.9em"><tr><th style="width:17%">약어</th><th style="width:36%">Full name</th><th>한글 · 한 줄 뜻</th></tr>{trs}</table></div></div>""")


h = (len(ABBR) + 1) // 2
E = [pairs, nums, abbr_page(1, ABBR[:h], "f-abbr1"), abbr_page(2, ABBR[h:], "f-abbr2")]
