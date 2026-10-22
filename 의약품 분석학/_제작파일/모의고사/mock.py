import json, os
D = os.path.dirname(os.path.abspath(__file__))
IDS = json.load(open(os.path.join(D, "ids.json")))
def ref(*ks):
    return " · ".join(f'개념 {IDS[k][1]:02d} (p.{IDS[k][0]})' for k in ks)

# ---------------- 객관식 (각 2점) ----------------
MC = [
dict(q="진공에서 파장이 400 nm인 빛이 굴절률 1.25인 용액으로 들어갔다. 이에 대한 설명으로 옳은 것은?",
 o=["진동수가 1.25배로 커진다", "용액 속 파장은 320 nm가 된다", "빛의 속도는 진공과 같다", "광자 1개의 에너지가 1/1.25로 줄어든다", "파수(ν̃)는 변하지 않는다"],
 a=2, ex="매질에서는 진동수(=색, 에너지)는 그대로, 속도와 파장만 1/n. λ = 400/1.25 = 320 nm. 파장이 바뀌니 파수(1/λ)도 바뀐다.", r=("c-wave",)),
dict(q="분자의 에너지와 흡수 스펙트럼에 대한 설명으로 <b>옳지 않은</b> 것은?",
 o=["전자전이의 에너지 간격은 수백 kJ/mol로 진동·회전보다 크다", "회전전이는 마이크로파를 흡수해 일어난다", "기체 원자의 흡수선 폭은 약 0.001 nm이다", "분자의 흡수가 넓은 띠인 것은 전자전이에 진동·회전 전이가 함께 일어나기 때문이다", "T₁은 S₁보다 에너지가 높으므로 S₀→T₁ 흡수가 S₀→S₁보다 우세하다"],
 a=5, ex="T₁이 S₁보다 에너지가 <b>낮다</b>(파장 397 vs 355 nm). 그리고 흡수는 스핀이 그대로인 S₀→S₁이 압도적(S→T는 금지 전이).", r=("c-etrans", "c-line")),
dict(q="어떤 시료의 투광도가 25 %일 때 흡광도는? (log 2 = 0.30)",
 o=["0.25", "0.30", "0.60", "0.75", "1.40"], a=3, ex="A = −log 0.25 = log 4 = 2 × 0.30 = 0.60.", r=("c-ta",)),
dict(q="1 cm 셀에서 흡광도 0.20인 용액을 물로 2배 묽힌 뒤 5 cm 셀로 측정하면 흡광도는?",
 o=["0.10", "0.20", "0.40", "0.50", "1.00"], a=4, ex="A = εbc → b ×5, c ×1/2 → 0.20 × 5 × 0.5 = 0.50.", r=("c-beer",)),
dict(q="분자량 200인 물질의 E¹%₁cm(250 nm)가 500이다. 이 물질의 250 nm에서 몰흡광계수 ε(M⁻¹cm⁻¹)는?",
 o=["1,000", "2,500", "10,000", "25,000", "100,000"], a=3, ex="ε = E¹%₁cm × MW / 10 = 500 × 200 / 10 = 10,000.", r=("c-e1",)),
dict(q="230 nm에서 흡광도를 측정하려 한다. 광원·셀·용매의 조합으로 가장 적절한 것은?",
 o=["텅스텐 램프 · 유리 셀 · 물", "중수소 램프 · 석영 셀 · 메탄올", "중수소 램프 · 유리 셀 · 아세토나이트릴", "텅스텐 램프 · 석영 셀 · 아세톤", "중수소 램프 · 석영 셀 · 벤젠"],
 a=2, ex="UV → 중수소 램프, UV는 유리가 먹으니 석영 셀, 용매 cutoff는 230보다 짧아야 → 메탄올(210) ○ / 아세톤(330)·벤젠(280) ×.", r=("c-lamp", "c-cell")),
dict(q="광다이오드 배열(PDA) 검출기에 대한 설명으로 <b>옳지 않은</b> 것은?",
 o=["시료를 통과한 다색광을 격자로 펼쳐 검출한다", "모든 파장을 동시에 측정해 스펙트럼을 1초 이내에 얻는다", "신호 평균화로 신호대잡음비가 높다", "회절격자를 회전시키며 한 파장씩 스캔하기 때문에 튼튼하다", "움직이는 부품이 거의 없다"],
 a=4, ex="격자를 돌리며 한 파장씩 스캔하는 건 기존 분산형. PDA는 움직이는 부품이 거의 없어서 튼튼하다.", r=("c-pda",)),
dict(q="광전자증배관(PMT)에 대한 설명으로 옳은 것만을 고른 것은?<br>ㄱ. 각 다이노드는 앞의 것보다 약 90 V 더 양(+)전위이다<br>ㄴ. 광자 1개당 10⁶개 이상의 전자가 양극에 모인다<br>ㄷ. 강한 빛에도 손상되지 않아 별도 보호가 필요 없다<br>ㄹ. 증폭 없이 빛을 전류로 바꾸는 단순한 반도체 소자이다",
 o=["ㄱ", "ㄱ, ㄴ", "ㄴ, ㄷ", "ㄱ, ㄴ, ㄹ", "ㄷ, ㄹ"], a=2, ex="ㄷ: 강한 빛에 노출되면 손상(셔터로 보호). ㄹ: 그건 광다이오드(PD) 설명.", r=("c-det",)),
dict(q="벤젠(λmax 254 nm)에 –NH₂가 치환되자 λmax가 280 nm로 이동하고 흡광도가 커졌다. 이 현상과 –NH₂의 역할을 바르게 짝지은 것은?",
 o=["hypsochromic + hyperchromic, 발색단", "bathochromic + hyperchromic, 조색단", "bathochromic + hypochromic, 조색단", "hypsochromic + hypochromic, 발색단", "bathochromic + hyperchromic, 발색단"],
 a=2, ex="긴 파장으로 = bathochromic(적색), 흡광 증가 = hyperchromic. –NH₂는 스스로 흡수 못 하고 발색단의 λ·ε를 바꾸는 조색단.", r=("c-auxo",)),
dict(q="공액 이중결합 2개인 화합물의 λmax가 222 nm, εmax가 20,000이다. 공액 이중결합이 4개로 늘어나면 대략 어떻게 되는가?",
 o=["252 nm, 40,000", "282 nm, 80,000", "282 nm, 40,000", "342 nm, 160,000", "192 nm, 10,000"],
 a=2, ex="1개당 +30 nm, ε ×2 → 2개 추가: 222 + 60 = 282 nm, 20,000 × 4 = 80,000.", r=("c-conj",)),
dict(q="어떤 착물 용액이 청록색으로 보인다. 이 용액이 주로 흡수하는 파장 영역은?",
 o=["380–420 nm", "440–470 nm", "500–520 nm", "620–680 nm", "680–780 nm"], a=4, ex="보이는 색 = 흡수된 색의 보색. 청록이 보이면 빨강(620–680 nm)을 흡수.", r=("c-color",)),
dict(q="야블론스키 도표에 대한 설명으로 옳은 것은?",
 o=["인광은 S₁ → S₀ 전이에서 나오는 빛이다", "계간전이는 S₁ → T₁으로 스핀이 뒤집히는 무복사 전이이다", "형광의 수명은 10⁻⁴–10² s로 인광보다 길다", "내부전환은 광자를 방출하는 복사 전이이다", "형광은 흡수보다 짧은 파장에서 나타난다"],
 a=2, ex="①은 형광 ③은 인광의 수명 ④ 내부전환은 열로 버림(무복사) ⑤ 형광은 흡수보다 <b>긴</b> 파장(스토크스 이동).", r=("c-jab",)),
dict(q="형광 측정 장치와 스펙트럼에 대한 설명으로 <b>옳지 않은</b> 것은?",
 o=["여기 스펙트럼은 λem을 고정하고 λex를 변화시켜 얻는다", "여기 스펙트럼의 모양은 흡수 스펙트럼과 매우 비슷하다", "형광광도계에는 단색화장치가 2개 있다", "발광광도계(luminometer)에도 Xe 램프와 여기 단색화장치가 반드시 필요하다", "형광광도계의 검출기는 여기광 진행 방향과 90°에 둔다"],
 a=4, ex="화학·생물발광은 시료가 스스로 빛나므로 발광광도계에는 광원·여기 단색화장치가 없다.", r=("c-exem",)),
dict(q="형광 세기와 형광 물질 구조에 대한 설명으로 옳은 것만을 고른 것은?<br>ㄱ. 묽은 용액에서 형광세기는 I = kP₀c로 농도와 여기광 세기에 비례한다<br>ㄴ. 고농도에서는 자기흡수로 형광세기가 오히려 줄어든다<br>ㄷ. 벤젠 고리에 무거운 할로젠이 치환될수록 형광이 증가한다<br>ㄹ. 단단하고 평평한 방향족 고리가 많을수록 형광이 세다",
 o=["ㄱ, ㄴ", "ㄱ, ㄹ", "ㄱ, ㄴ, ㄹ", "ㄴ, ㄷ, ㄹ", "ㄱ, ㄴ, ㄷ, ㄹ"], a=3, ex="ㄷ: 원자량이 클수록(F < Cl < Br < I) 형광 <b>감소</b>.", r=("c-fint", "c-dye")),
dict(q="광학활성 물질 2.00 g을 녹여 50 mL로 하고 200 mm 관에서 측정한 선광도가 +4.0°였다. 비선광도 [α]는?",
 o=["+25°", "+50°", "+100°", "+12.5°", "+200°"], a=2, ex="c = 2.00/50 = 0.04 g/mL → [α] = 100 × 4.0 / (200 × 0.04) = 400/8 = +50°.", r=("c-sr",)),
dict(q="비선광도가 +50°이고 분자량이 300인 물질의 몰선광도 [M]은?",
 o=["+1.5°", "+15°", "+150°", "+1,500°", "+0.15°"], a=2, ex="[M] = [α] × MW / 1000 = 50 × 300 / 1000 = +15°. (÷100 아니고 ÷1000!)", r=("c-mr",)),
dict(q="순수한 (R)-거울상이성질체의 비선광도는 +40°이다. 같은 조건에서 어떤 시료의 비선광도가 +30°라면 (R) : (S)는?",
 o=["75 : 25", "87.5 : 12.5", "62.5 : 37.5", "80 : 20", "70 : 30"], a=2, ex="광학순도 = 30/40 = 75 % = ee → (R) = (100 + 75)/2 = 87.5 %, (S) = 12.5 %.", r=("c-ee",)),
dict(q="중공음극램프(HCL)에 대한 설명으로 <b>옳지 않은</b> 것은?",
 o=["음극은 분석하려는 금속 원소로 만든다", "유리관 안에 1–5 Torr의 Ne 또는 Ar이 들어 있다", "검출할 원소마다 다른 램프가 필요하다", "연속 스펙트럼 광원이라서 분광기로 원하는 원소의 파장을 골라 쓴다", "램프 내부에서 빛이 나오는 원리는 원자 발광(AES)과 같다"],
 a=4, ex="HCL은 그 원소의 선만 내는 <b>선(line) 스펙트럼</b> 광원(193–852 nm).", r=("c-hcl",)),
dict(q="원자화 장치에 대한 설명으로 옳은 것은?",
 o=["흑연로는 화염보다 분석물 체류시간이 짧아 감도가 낮다", "흑연로에서는 Ar 가스를 흘려 흑연의 산화를 막는다", "ICP-AES는 스펙트럼 간섭이 매우 적다", "아세틸렌–공기 화염의 온도는 6000–10000 K이다", "ICP로 F, Cl, Br을 쉽게 직접 정량할 수 있다"],
 a=2, ex="흑연로는 체류 수 초 → 감도↑ / ICP-AES는 스펙트럼 간섭이 <b>많다</b> / 아세틸렌–공기는 2400–2700 K(6000–10000 K는 ICP) / 할로젠은 ICP로 직접 분석 불가.", r=("c-flame", "c-cmp")),
dict(q="다음 중 NMR로 분석할 수 있는 핵종의 개수는?<br>¹²C, ¹³C, ¹⁶O, ¹⁷O, ¹⁴N, ³²S, ¹⁹F, ³¹P, ²H<br><span style='font-size:.9em'>(원자번호 C 6, O 8, N 7, S 16, F 9, P 15, H 1)</span>",
 o=["4", "5", "6", "7", "8"], a=3, ex="질량수·원자번호 둘 다 짝수면 I = 0(불가): ¹²C, ¹⁶O, ³²S. 나머지 6개(¹³C, ¹⁷O, ¹⁴N, ¹⁹F, ³¹P, ²H) 가능.", r=("c-spin",)),
dict(q="2.35 T에서 ¹H의 고유진동수는 100 MHz이다. 11.75 T 자석에서 ¹³C의 공명 진동수는? (¹³C의 γ ≈ ¹H의 1/4)",
 o=["25 MHz", "100 MHz", "125 MHz", "500 MHz", "2000 MHz"], a=3, ex="ν₀ ∝ B₀ → 11.75/2.35 = 5배 → ¹H 500 MHz → ¹³C = 500/4 = 125 MHz.", r=("c-larmor",)),
dict(q="400 MHz ¹H-NMR에서 TMS로부터 1200 Hz 떨어진 곳에 피크가 나왔다. 같은 시료를 600 MHz 기기로 측정할 때 이 피크의 δ와 TMS로부터의 거리는?",
 o=["3.0 ppm, 1200 Hz", "3.0 ppm, 1800 Hz", "4.5 ppm, 1800 Hz", "2.0 ppm, 1200 Hz", "3.0 ppm, 800 Hz"],
 a=2, ex="δ = 1200/400 = 3.0 ppm(기기와 무관) → 600 MHz에서 Δν = 3.0 × 600 = 1800 Hz.", r=("c-delta",)),
dict(q="¹H-NMR 화학적 이동에 대한 설명으로 <b>옳지 않은</b> 것은?",
 o=["스펙트럼의 왼쪽(δ가 큰 쪽)을 낮은 장(downfield)이라 한다", "Si의 전기음성도가 C보다 작아 TMS의 수소는 가장 많이 차폐되어 있다", "벤젠 수소가 약 7.27 ppm에 나타나는 것은 고리전류에 의한 탈차폐 때문이다", "알카인(≡C–H) 수소는 sp 탄소에 붙어 있어 알켄 수소보다 δ가 크다", "카복실산 수소는 대략 10–12 ppm에 나타난다"],
 a=4, ex="알카인 H는 삼중결합 축 방향의 차폐(+) 영역에 있어서 2–3 ppm으로 알켄(5–7)보다 <b>작다</b>(자기이방성).", r=("c-aniso",)),
dict(q="CH₃CH₂Cl의 ¹H-NMR 스펙트럼(이웃자리 짝지음만 고려)으로 옳은 것은?",
 o=["CH₃ 사중선, CH₂ 삼중선, 적분비 3 : 2", "CH₃ 삼중선, CH₂ 사중선, 적분비 2 : 3", "CH₃ 삼중선, CH₂ 사중선, 적분비 3 : 2", "CH₃ 이중선, CH₂ 칠중선, 적분비 3 : 2", "CH₃·CH₂ 모두 단일선, 적분비 3 : 2"],
 a=3, ex="CH₃: 이웃 CH₂(2H) → 2+1 = 삼중선 / CH₂: 이웃 CH₃(3H) → 3+1 = 사중선 / 적분 = H 수 3 : 2.", r=("c-n1", "c-integ")),
]

# ---------------- 주관식 ----------------
SA = [
dict(pt=5, kind="빈칸 채우기", h=150,
 q="어떤 의약품의 대한약전 규정: E¹%₁cm(270 nm) : 380–410 (건조 후, 4 mg, 메탄올, 200 mL). 이 약을 건조하여 4.0 mg을 달아 메탄올로 200 mL로 하고 층장 1 cm, 270 nm에서 흡광도 0.79를 얻었다.<br><br>c = 4.0 mg/200 mL = ( 가 ) g/100 mL = ( 나 ) w/v%<br>E¹%₁cm = 0.79 / (( 나 ) × 1) = ( 다 ) → 대한약전 기준에 ( 라 )(적합 / 부적합)",
 a="(가) 0.002 (나) 0.002 (다) 395 (라) 적합", ex="4.0 mg/200 mL = 2.0 mg/100 mL = 0.002 g/100 mL. 0.79/0.002 = 790/2 = 395 → 380–410 안 → 적합. (함정: mg → g, 200 mL → 100 mL 환산)", r=("c-e1",)),
dict(pt=6, kind="계산", h=200,
 q="원료의약품 50.0 mg을 물에 녹여 정확히 100 mL로 하였다. 이 액 10.0 mL씩을 두 개의 50 mL 용량플라스크에 넣고, 하나는 물로, 다른 하나는 표준용액(0.2 mg/mL) 5.0 mL를 넣은 뒤 물로 표선까지 채웠다. 흡광도가 각각 0.480, 0.580이었다면 원료의약품의 함량(%)은? (풀이 과정을 쓰시오)",
 a="96.0 %", ex="① 더한 표준 = 0.2 × 5.0 = 1.0 mg ② 0.480 : x = 0.580 : (x + 1.0) → 0.100x = 0.480 → x = 4.80 mg (분취 10 mL 속) ③ 전체 100 mL = 48.0 mg ④ 48.0/50.0 × 100 = 96.0 %. (×10 분취 배수 잊지 않기)", r=("c-sa1",)),
dict(pt=6, kind="계산", h=200,
 q="원료의약품 70.0 mg을 물로 정확히 1000 mL로 하고, 이 액 10.0 mL를 물로 정확히 100 mL로 하여 검액으로 하였다. 표준액 5개로 얻은 검량선은 Y = 0.050X + 0.010 (X: μg/mL, Y: 흡광도)이고, 검액의 흡광도는 0.355였다. 원료의약품의 함량(%)은?",
 a="약 98.6 %", ex="① 검액 X = (0.355 − 0.010)/0.050 = 0.345/0.050 = 6.9 μg/mL ② 희석 전(1000 mL 용액) = 6.9 × 10 = 69 μg/mL ③ 1000 mL 속 = 69 mg ④ 69/70.0 × 100 ≈ 98.6 %.", r=("c-cal",)),
dict(pt=6, kind="빈칸 채우기", h=170,
 q="어떤 형광 정제(1정 표시량 5 mg)의 규격은 표시량의 95.0–105.0 %이다. 20정의 무게가 2.000 g이었고, 가루 0.250 g을 달아 검액을 만들었다. 표준품 12.0 mg으로 표준액을 만들고 검액과 똑같이 희석하여 형광세기 F<sub>T</sub> = 49.0, F<sub>S</sub> = 48.0을 얻었다.<br><br>1정 평균 무게 = ( 가 ) g → 가루 0.250 g = ( 나 )정 분량 → 표시량 = ( 다 ) mg<br>측정량 = 12.0 × ( 라 ) = ( 마 ) mg → 함량 = ( 바 ) % → ( 사 )(적합/부적합)",
 a="(가) 0.100 (나) 2.5 (다) 12.5 (라) 49.0/48.0 (마) 12.25 (바) 98.0 (사) 적합", ex="2.000/20 = 0.100 g → 0.250/0.100 = 2.5정 × 5 mg = 12.5 mg. 같은 희석이므로 형광세기 비 = 양 비 → 12.0 × 49/48 = 12.25 mg → 12.25/12.5 = 98.0 %.", r=("c-benz",)),
dict(pt=6, kind="계산", h=170,
 q="5 %(w/v) 포도당 주사액 80.0 mL를 정확히 취하여 암모니아 시액 0.2 mL와 물을 넣어 정확히 100 mL로 하고, 30분 방치한 뒤 20 °C, 층장 100 mm에서 선광도 +2.10°를 얻었다. 표시량 대비 함량(%)은? (포도당의 양(mg) = α<sub>D</sub> × 1895.4 를 이용)",
 a="약 99.5 %", ex="① 측정 포도당 = 2.10 × 1895.4 = 3790.8 + 189.54 = 3980.3 mg ② 표시량 = 80.0 mL × 0.05 g/mL = 4.000 g = 4000 mg ③ 3980.3/4000 × 100 ≈ 99.5 %.", r=("c-glu",)),
dict(pt=6, kind="서술형", h=170,
 q="람베르트-비어(Lambert-Beer) 법칙이 잘 성립하지 않는(흡광도가 농도에 비례하지 않는) 경우를 <b>3가지 이상</b> 쓰고 각각 이유를 간단히 설명하시오.",
 a="① 고농도: 분자끼리 가까워 상호작용 → 흡광계수가 변함 ② 단색광이 아님(다색광·미광): 법칙은 단색광 가정 ③ 화학적 변화: 해리·결합·반응으로 흡수 화학종의 농도가 실제 농도와 달라짐 ④ 산란(탁한 용액)·형광 발생: 빛이 흡수 외의 이유로 줄거나 더해짐",
 ex="교재 연습문제 01. 마스터 요약 람베르트-비어 개념의 “잘 안 맞는 경우” 그대로. 핵심어: 고농도·다색광/미광·해리/결합·산란·형광.", r=("c-beer",)),
dict(pt=6, kind="서술형", h=190,
 q="형광광도법이 자외가시부흡광도측정법보다 감도가 높은 이유를 두 방법의 <b>측정 원리와 검출기 위치</b>를 비교하여 서술하고, 형광 분석에 레이저를 광원으로 쓰는 이유를 형광세기 식과 연결하여 쓰시오.",
 a="흡광법은 시료와 일직선(180°)에서 센 입사광(P₀)과 투과광(P)의 작은 차이를 재므로 미세한 농도 차이를 구별하기 어렵다. 형광법은 여기광과 90° 방향에서 시료가 새로 내는 빛만 재므로 ‘어두운 배경 위의 신호’를 측정해 훨씬 낮은 농도(약 10⁵배)까지 검출된다. 묽은 용액에서 I = kP₀c로 형광세기가 여기광 세기 P₀에 비례하므로, 세기가 매우 큰 단색광인 레이저를 쓰면 신호가 커져 감도가 더 높아진다.",
 ex="네 필기(UV-Vis = 먹고 남은 빛 재기 · 180° / 형광 = 새로 뱉은 빛 재기 · 90°) + 족보 “레이저 쓰는 이유”. 핵심어: 180° vs 90°, 차이 측정 vs 어두운 배경, I = kP₀c, P₀↑.", r=("c-benz", "c-fint")),
dict(pt=5, kind="서술형", h=170,
 q="유도결합플라즈마(ICP)가 만들어지고 유지되는 과정과, 시료가 측정되기까지의 과정을 순서대로 쓰시오. (사용하는 기체, 주파수, 온도를 포함할 것)",
 a="① 테슬라 코일의 스파크로 Ar 일부 이온화(Ar → Ar⁺ + e⁻) ② 유도 코일의 RF(27 또는 41 MHz) 전류가 만든 진동 자기장이 전자를 가속 ③ 전자가 Ar과 충돌해 에너지 전달 → 6000–10000 K 유지 ④ 분무된 시료가 플라즈마에서 원자화·여기·이온화 ⑤ 들뜬 원자가 원소 고유 파장의 빛 방출(ICP-AES) / 이온은 질량분석(ICP-MS)",
 ex="족보 주제. 순서 키워드: 스파크 → RF 자기장 전자 가속 → 충돌 가열 6000–10000 K → 원자화·여기·이온화 → 발광.", r=("c-icp",)),
dict(pt=6, kind="빈칸 · 서술", h=200,
 q="분자식 C₃H₆O₂인 화합물의 ¹H-NMR(300 MHz, CDCl₃): δ 8.03 (s, 1H), 4.21 (q, J = 7.1 Hz, 2H), 1.29 (t, J = 7.1 Hz, 3H).<br>(1) 이 화합물에는 화학적으로 다른 수소가 ( 가 )종류 있다.<br>(2) 4.21 ppm 신호가 사중선인 이유는 이웃 탄소에 수소가 ( 나 )개 있기 때문이다.<br>(3) 4.21과 1.29 ppm 신호가 서로 이웃임을 알 수 있는 근거를 쓰시오.<br>(4) 사중선에서 이웃한 두 줄 사이 간격은 ( 다 ) Hz = 약 ( 라 ) ppm이다.<br>(5) 이 화합물은? (보기: 아세트산 메틸 CH₃COOCH₃ / 폼산 에틸 HCOOCH₂CH₃ / 프로판산 CH₃CH₂COOH)",
 a="(가) 3 (나) 3 (3) 두 신호의 짝지음 상수 J가 7.1 Hz로 같다 (다) 7.1 (라) 0.024 (5) 폼산 에틸 HCOOCH₂CH₃",
 ex="8.03(s, 1H) = H–C(=O)O 폼일 H(이웃 H 없음). 4.21(q, 2H) = O에 붙은 CH₂(탈차폐, 이웃 CH₃ 3H). 1.29(t, 3H) = CH₃(이웃 CH₂ 2H). J(ppm) = 7.1/300 ≈ 0.024. 아세트산 메틸은 단일선 2개, 프로판산은 COOH 10–12 ppm이 나와야 함.", r=("c-n1", "c-j", "c-region")),
]

TARGET = [1,5,3,4,1, 2,4,5,1,3, 4,2,5,1,3, 2,4,1,5,3, 2,4,1,3]
for m, t in zip(MC, TARGET):
    o = m["o"]; c = o.pop(m["a"] - 1); o.insert(t - 1, c); m["a"] = t
from collections import Counter; print("dist", sorted(Counter(TARGET).items()))
TOT_MC = len(MC) * 2
TOT_SA = sum(s["pt"] for s in SA)
assert TOT_MC + TOT_SA == 100, (TOT_MC, TOT_SA)
CIRC = "①②③④⑤"

CSS = r"""
@page{size:210mm 297mm;margin:0}
*{box-sizing:border-box}
body{margin:0;font-family:'Noto Sans KR',sans-serif;color:#22252c;-webkit-print-color-adjust:exact;print-color-adjust:exact;}
.pg{width:210mm;height:297mm;padding:13mm 13mm 14mm 13mm;position:relative;overflow:hidden;page-break-after:always;background:#fff;font-size:11.3px;line-height:1.62;}
.top{display:flex;justify-content:space-between;align-items:flex-end;border-bottom:2.5px solid #222;padding-bottom:5px;margin-bottom:9px}
.top b{font-size:15px}.top span{font-size:10.5px;color:#555}
.cols{column-count:2;column-gap:9mm;column-rule:1px solid #ccc;}
.mc{break-inside:avoid;margin:0 0 11px 0}
.mc .n{font-weight:700;margin-right:3px}
.mc ol{list-style:none;margin:4px 0 0 0;padding:0 0 0 2px}
.mc li{margin:1px 0}
.sa{border:1px solid #bbb;border-radius:6px;padding:8px 11px;margin:0 0 9px 0;break-inside:avoid}
.sa .h{font-weight:700;margin-bottom:3px}
.sa .k{display:inline-block;font-size:9.5px;background:#eee;border-radius:4px;padding:0 6px;margin-left:5px;color:#444;font-weight:700}
.ans{border:1px dashed #aaa;border-radius:5px;margin-top:6px;background-image:linear-gradient(#e6e6e6 1px,transparent 1px);background-size:100% 22px;}
.ft{position:absolute;left:13mm;right:13mm;bottom:6mm;text-align:center;font-size:9.5px;color:#888;border-top:1px solid #ddd;padding-top:4px}
.cover h1{font-size:25px;margin:18mm 0 4px 0;text-align:center}
.cover .s{text-align:center;color:#555;font-size:12.5px}
.box{border:1.5px solid #222;border-radius:6px;padding:10px 14px;margin:9mm 0 0 0;font-size:12px;line-height:1.85}
table.info{width:100%;border-collapse:collapse;margin-top:8mm;font-size:12px}
table.info td{border:1px solid #888;padding:6px 9px}
.omr{display:grid;grid-template-columns:repeat(2,1fr);grid-template-rows:repeat(12,auto);grid-auto-flow:column;gap:4px 16mm;margin-top:6mm}
.omr div{font-size:12px;letter-spacing:.35em}
.omr b{display:inline-block;width:22px;letter-spacing:0}
.div{display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;background:#f3f0fb}
.div h2{font-size:26px;margin:0 0 8px 0;color:#4651c8}
.ak{display:grid;grid-template-columns:repeat(6,1fr);gap:5px;margin-bottom:10px}
.ak div{border:1px solid #ccc;border-radius:5px;text-align:center;padding:3px;font-size:12px}
.ak b{color:#4651c8}
.ex{border-left:4px solid #4651c8;background:#f7f8fd;border-radius:4px;padding:5px 10px;margin:0 0 7px 0;break-inside:avoid}
.ex .t{font-weight:700}.ex .t i{font-style:normal;color:#c92a2a}
.ex .r{font-size:10px;color:#6a3d9a;margin-top:2px}
.ex.s{border-left-color:#127a64;background:#f2f8f5}
.chk{width:100%;border-collapse:collapse;font-size:11px;margin-top:6px}
.chk th,.chk td{border:1px solid #bbb;padding:4px 7px;text-align:left}
.chk th{background:#eef0f8}
"""

def foot(t): return f'<div class="ft">{t}</div>'

pages = []
# cover
pages.append(f'''<section class="pg cover"><h1>의약품분석학 II 중간고사 모의고사</h1>
<div class="s">범위: Lecture 2–4 (분광학 기초 · 자외가시부 · 형광 · 선광도 · 원자분광법 · NMR)</div>
<table class="info"><tr><td style="width:25%">시험 시간</td><td>90분 (타이머를 맞추고 한 번에 풀기)</td></tr>
<tr><td>구성</td><td>객관식 {len(MC)}문항 × 2점 = {TOT_MC}점 · 주관식 {len(SA)}문항 = {TOT_SA}점 · 총 100점</td></tr>
<tr><td>유의사항</td><td><b>계산기 사용 금지</b> (log 2 = 0.30, log 3 = 0.48만 기억) · 객관식은 맨 뒤 답안 표기란에 표시 · 주관식은 풀이 과정까지</td></tr>
<tr><td>채점</td><td>정답·해설은 <b>뒤쪽에 따로</b> 있어. 다 푼 뒤에만 넘기기. 해설마다 마스터 요약 개념·쪽수가 달려 있어</td></tr></table>
<div class="box"><b>📌 이 모의고사의 특징</b><br>
· 과제·예제와 같은 유형이지만 <b>숫자와 물질을 바꿔서</b> 외운 답으로는 못 풀게 만들었어.<br>
· 마스터 요약에 없던 유형도 섞었어: 몰흡광계수↔비흡광도 환산, 다시 계산하는 공액 길이, 람베르트-비어 이탈(교재 연습문제 01), 낯선 ¹H-NMR 구조 추정.<br>
· 틀린 문제는 해설의 <b>📍개념 번호(p.쪽)</b>로 가서 그 부분만 다시 보면 돼.</div>
<div class="box"><b>이름</b> ____________________ &nbsp;&nbsp; <b>푼 날짜</b> ________ &nbsp;&nbsp; <b>걸린 시간</b> ______분 &nbsp;&nbsp; <b>점수</b> ______ / 100</div>
{foot("의약품분석학 II · 중간고사 모의고사")}</section>''')

# MC pages
def mc_html(i, m):
    ops = "".join(f"<li>{CIRC[k]} {o}</li>" for k, o in enumerate(m["o"]))
    return f'<div class="mc"><span class="n">{i}.</span>{m["q"]}<ol>{ops}</ol></div>'
chunks = [MC[0:9], MC[9:17], MC[17:24]]
n = 1; pno = 1
for ch in chunks:
    body = "".join(mc_html(n + k, m) for k, m in enumerate(ch)); n += len(ch)
    pages.append(f'<section class="pg"><div class="top"><b>Ⅰ. 객관식</b><span>각 2점 · 가장 알맞은 것 하나</span></div><div class="cols">{body}</div>{foot(f"모의고사 {pno}")}</section>'); pno += 1

# SA pages
def sa_html(i, s):
    return f'<div class="sa"><div class="h">{i}. <span class="k">{s["kind"]} · {s["pt"]}점</span></div>{s["q"]}<div class="ans" style="height:{s["h"]}px"></div></div>'
sa_chunks = [SA[0:3], SA[3:5], SA[5:7], SA[7:9]]
k = len(MC) + 1
for ch in sa_chunks:
    body = "".join(sa_html(k + j, s) for j, s in enumerate(ch)); k += len(ch)
    pages.append(f'<section class="pg"><div class="top"><b>Ⅱ. 주관식</b><span>풀이 과정을 함께 쓰시오</span></div>{body}{foot(f"모의고사 {pno}")}</section>'); pno += 1

# OMR
omr = "".join(f'<div><b>{i}</b> ① ② ③ ④ ⑤</div>' for i in range(1, len(MC) + 1))
pages.append(f'<section class="pg"><div class="top"><b>객관식 답안 표기란</b><span>정답에 동그라미 · 시험 땐 OMR 수성펜!</span></div><div class="omr">{omr}</div>{foot(f"모의고사 {pno}")}</section>')

# divider
pages.append('<section class="pg div"><h2>✋ 여기서부터 정답·해설</h2><div style="font-size:14px;color:#444">90분 다 풀고 나서 넘기기!<br>채점 → 틀린 문제의 📍개념 쪽만 마스터 요약에서 다시 보기</div></section>')

# answers
ak = "".join(f'<div>{i+1}. <b>{CIRC[m["a"]-1]}</b></div>' for i, m in enumerate(MC))
exs = "".join(f'<div class="ex"><div class="t">{i+1}. 정답 <i>{CIRC[m["a"]-1]}</i></div>{m["ex"]}<div class="r">📍 {ref(*m["r"])}</div></div>' for i, m in enumerate(MC))
def exh(lo, hi): return "".join(f'<div class="ex"><div class="t">{i+1}. 정답 <i>{CIRC[MC[i]["a"]-1]}</i></div>{MC[i]["ex"]}<div class="r">📍 {ref(*MC[i]["r"])}</div></div>' for i in range(lo, hi))
pages.append(f'<section class="pg"><div class="top"><b>정답표 · 객관식 해설 (1)</b><span>각 2점</span></div><div class="ak">{ak}</div><div class="cols">{exh(0,10)}</div>{foot("정답·해설")}</section>')
pages.append(f'<section class="pg"><div class="top"><b>객관식 해설 (2)</b><span>각 2점</span></div><div class="cols">{exh(10,24)}</div>{foot("정답·해설")}</section>')
# split if too long -> handled by render check
sas = "".join(f'<div class="ex s"><div class="t">{len(MC)+i+1}. ({s["pt"]}점) 정답: <i>{s["a"]}</i></div>{s["ex"]}<div class="r">📍 {ref(*s["r"])}</div></div>' for i, s in enumerate(SA))
pages.append(f'<section class="pg"><div class="top"><b>주관식 정답 · 해설</b><span>부분점수: 식·단위·핵심어</span></div>{sas}{foot("정답·해설")}</section>')

# check table
rows = [("분광학 기초·람베르트-비어", "1–5", "c-wave"), ("UV-Vis 장치(광원·셀·검출기)", "6–8", "c-lamp"), ("발색단·공액·색", "9–11", "c-auxo"),
        ("UV-Vis 정량(비흡광도·표준물첨가·검량선)", "25–27, 30", "c-quant1"), ("형광", "12–14, 28, 31", "c-jab"), ("선광도", "15–17, 29", "c-sr"),
        ("원자분광법", "18–19, 32", "c-hcl"), ("NMR", "20–24, 33", "c-spin")]
tr = "".join(f'<tr><td>{a}</td><td>{b}</td><td>/</td><td>{ref(c)}부터</td></tr>' for a, b, c in rows)
pages.append(f'<section class="pg"><div class="top"><b>단원별 오답 체크표</b><span>틀린 개수를 적고, 많이 틀린 단원부터 복습</span></div>'
             f'<table class="chk"><tr><th>단원</th><th>문항</th><th>틀린 수</th><th>다시 볼 곳(마스터 요약)</th></tr>{tr}</table>'
             f'<div class="box" style="margin-top:8mm"><b>남은 기간 추천</b><br>① 틀린 단원 개념 페이지 + 그 뒤 문제 다시 풀기<br>② 시험 전날: 마스터 요약 「혼동 쌍 총정리」·「숫자·공식 카드」·★ 표시한 곳만<br>③ 계산 문제는 계산기 없이 손으로 한 번 더(특히 ÷1000, ×10 분취, mg→g)</div>'
             f'{foot("정답·해설")}</section>')

html = f'<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>의약품분석학II 중간고사 모의고사</title><style>{CSS}</style></head><body>{"".join(pages)}</body></html>'
open(os.path.join(D, "mock.html"), "w").write(html)
print("pages", len(pages))
