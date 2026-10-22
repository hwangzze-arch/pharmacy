import os, re, sys, runpy, html as H
D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, D)
from xd import *

B = os.path.join(D, "..", "중간고사_마스터요약")
cwd = os.getcwd(); os.chdir(B); g = runpy.run_path("build.py"); os.chdir(cwd)
ENTRIES = g["ENTRIES"]

PT = {"PART 1 · 분광학 기초": "basic", "PART 2 · 자외가시부흡광도측정법": "uv", "PART 3 · 형광광도법": "fl",
      "PART 4 · 선광도": "or", "PART 5 · 원자분광법": "at", "PART 6 · 핵자기공명(NMR)": "nmr"}
PNAME = {"PART 1 · 분광학 기초": "PART 1 · 분광학 기초 (Lecture 2)", "PART 2 · 자외가시부흡광도측정법": "PART 2 · 자외가시부흡광도측정법 (Lecture 2)",
         "PART 3 · 형광광도법": "PART 3 · 형광광도법 (Lecture 3)", "PART 4 · 선광도": "PART 4 · 선광도 (Lecture 3)",
         "PART 5 · 원자분광법": "PART 5 · 원자분광법 (Lecture 3)", "PART 6 · 핵자기공명(NMR)": "PART 6 · 핵자기공명 NMR (Lecture 4)"}

# ---- 개념 페이지의 ✍️ 예제 (사고의 흐름 형식으로 새로 정리) ----
EX = {
 "c-wave": [dict(src="교재 연습문제 02", title="굴절률과 파장 · 파수 환산",
   q="(1) 진공에서 파장 600 nm인 가시광선이 굴절률 1.2인 용액을 통과할 때 용액 속 파장은?<br>(2) 파수 1000 cm⁻¹의 빛은 파장으로 몇 μm인가?",
   a="(1) 500 nm (2) 10 μm",
   flow=[("단서", "매질 속에서 변하지 않는 것 = 진동수 ν(색). 변하는 것 = 속도(c/n)와 파장"),
         ("계산", "λ = λ<sub>진공</sub>/n = 600/1.2 = 500 nm"),
         ("계산", "λ = 1/ν̃ = 1/1000 cm = 0.001 cm = 10 μm", "1 cm = 10⁴ μm"),
         ("함정 체크", "“진동수가 n배” 같은 보기는 X — ν는 광원이 정한다")],
   one="매질에선 ν 고정, λ만 ÷n. 파수 ↔ 파장은 역수")],
 "c-beer": [dict(src="교재 예제 1-1", title="층장을 바꿀 때의 투광도",
   q="어떤 용액을 층장 1 cm 셀로 측정하였더니 투과율이 90 %였다. 층장 2 cm, 5 cm 셀로 측정하면 투과율은?",
   a="2 cm 81 %, 5 cm 59 %",
   flow=[("단서", "람베르트 법칙: A ∝ b → 두께가 2배면 A도 2배"),
         ("계산", "A₁ = −log 0.9 ≈ 0.046 → 2 cm 0.092, 5 cm 0.23"),
         ("연결", "계산기 없이: 1 cm마다 90 %씩 남으니 0.9를 b번 곱한다"),
         ("결론", "0.9² = 0.81 → 81 % / 0.9⁵ ≈ 0.59 → 59 %")],
   one="T는 곱해지고, A는 더해진다(비례)")],
 "c-quant1": [dict(src="교재 연습문제 12", title="비흡광도 + 희석으로 제제 중 양",
   q="아세트산 히드로코르티손 제제를 메탄올로 정확히 100 mL로 하였다. 이 액 5 mL를 메탄올로 정확히 50 mL로 하여 242 nm에서 흡광도 0.395를 얻었다. E¹%₁cm(242 nm) = 395일 때 제제 중 양(mg)은?",
   a="10 mg",
   flow=[("계산", "측정액 c = A/E = 0.395/395 = 0.001 % = 1 mg/100 mL = 0.01 mg/mL"),
         ("계산", "측정액 50 mL 속 = 0.5 mg", "희석은 양을 바꾸지 않는다 → 이건 분취한 5 mL 속 양"),
         ("계산", "처음 100 mL 전체 = 0.5 × (100/5) = 10 mg"),
         ("함정 체크", "희석 문제는 “측정액 → 분취액 → 원액”으로 거꾸로 올라가기")],
   one="측정액 양 = 분취액 양 → 전체/분취 배수 곱")],
 "c-sr": [dict(src="교재 예제 1-4 · 1-5", title="약전의 비선광도 표기 읽기",
   q="(1) d-장뇌의 비선광도는 [α]²⁰<sub>D</sub> = +41.0 ~ +43.0° (5 g, 에탄올, 50 mL, 100 mm)이다. 이 문장의 의미와 실제로 측정되어야 할 선광도 α의 범위는?<br>(2) dl-장뇌의 비선광도가 −1.5 ~ +1.5°인 이유는?",
   a="(1) 5 g → 에탄올 50 mL, 20 °C, 100 mm 관, Na D선으로 잰 비선광도가 +41.0~+43.0° → α = +4.1 ~ +4.3° (2) d:l = 1:1 라세미라 이론상 0",
   flow=[("단서", "괄호 안 = 측정 조건(시료량, 용매, 부피, 관 길이), 위첨자 20 = 20 °C, 아래첨자 D = Na D선 589 nm"),
         ("계산", "c = 5 g/50 mL = 0.1 g/mL → α = [α] × l × c / 100 = 41 × 100 × 0.1 / 100 = 4.1 (43 → 4.3)"),
         ("연결", "dl = 라세미 → 두 거울상의 회전이 상쇄 → 0, ±1.5°는 측정 오차 허용")],
   one="α = [α]·l·c/100 · 라세미 = 0")],
 "c-mr": [dict(src="교재 예제 1-3 · 슬라이드 22", title="비선광도와 몰선광도 (나프록센)",
   q="(S)-나프록센 250 mg을 클로로포름에 녹여 20 mL로 하고 200 mm 관, Na D선, 20 °C에서 α = +1.65°를 얻었다. 비선광도와 몰선광도는? (MW 230.17)",
   a="[α] = +66.0°, [M] = +15.2°",
   flow=[("계산", "c = 0.250 g/20 mL = 0.0125 g/mL"),
         ("계산", "[α] = 100 × 1.65 / (200 × 0.0125) = 165/2.5 = +66.0°"),
         ("계산", "[M] = [α] × MW/1000 = 66.0 × 230.17/1000 ≈ +15.2°"),
         ("함정 체크", "몰선광도는 ÷1000 (÷100 아님). 교재의 0.00125·152.0°는 오타")],
   one="[α] = 100α/(l·c) → [M] = [α]·MW/1000")],
 "c-glu": [dict(src="슬라이드 23·24 Q", title="포도당 정량의 1895.4",
   q="(1) 포도당 정량법(약 10 g → 100 mL, 100 mm)에서 함량 100 %인 시료 10 g이면 측정될 α는?<br>(2) 포도당 주사액 정량에 포도당 약 4 g이 필요할 때 5 % 포도당 주사액 몇 mL를 취하나?<br>(3) (2)의 주사액이 표시량 100 %라면 α는?",
   a="(1) +5.28° (2) 80 mL (3) +2.11°",
   flow=[("단서", "포도당(mg) = α × 1895.4 (100 mL, 100 mm, [α] 중간값 52.75°)"),
         ("계산", "α = 10000/1895.4 ≈ 5.28°"),
         ("계산", "5 % = 0.05 g/mL → 4/0.05 = 80 mL"),
         ("계산", "α = 4000/1895.4 ≈ 2.11°")],
   one="1° 돌면 100 mL 속 포도당 약 1.9 g")],
 "c-ee": [dict(src="마스터 요약 예제", title="광학순도 → 거울상이성질체 비",
   q="(1) 시료의 [α] = +30°, 순수한 (R)의 [α] = +50°일 때 (R) : (S)는?<br>(2) 순수한 (S)-나프록센의 [α] = +66.0°, 어떤 시료가 +33.0°였다면 (S) : (R)는?",
   a="(1) 80 : 20 (4 : 1) (2) 75 : 25 (3 : 1)",
   flow=[("단서", "광학순도 = [α]비 × 100 = ee = 많은 % − 적은 %"),
         ("계산", "(1) 30/50 = 60 % → (R) = (100 + 60)/2 = 80 %, (S) = 20 %"),
         ("계산", "(2) 33/66 = 50 % → (S) = 75 %, (R) = 25 %")],
   one="많은 쪽 = (100 + ee)/2")],
 "c-larmor": [dict(src="마스터 요약 예제", title="고유진동수 계산 (ν₀ ∝ B₀, ν₀ ∝ γ)",
   q="¹H의 γ = 267.53 × 10⁶ rad·s⁻¹·T⁻¹이다. (1) 2.35 T에서 ¹H의 고유진동수는? (2) 14.1 T와 1.41 T에서는? (3) 14.1 T에서 ¹³C(γ ≈ ¹H의 1/4)는?",
   a="(1) 100 MHz (2) 600 MHz, 60 MHz (3) 150 MHz",
   flow=[("계산", "ν₀ = γB₀/2π = 42.58 × 10⁶ × 2.35 ≈ 100.0 MHz"),
         ("연결", "계산기 없이 비례로: 14.1/2.35 = 6배 → 600 MHz, 1.41 = 0.6배 → 60 MHz"),
         ("계산", "¹³C = 600 × 1/4 = 150 MHz")],
   one="ν₀ = 42.6 × B₀(T) MHz, ¹³C는 1/4")],
 "c-delta": [dict(src="슬라이드 8 · 마스터 요약 예제", title="히드록시아세톤의 화학적 이동",
   q="히드록시아세톤 CH₃의 차폐상수 σ = 0.0000178, σ<sub>TMS</sub> = 0.00002이다. 100 MHz와 600 MHz 기기에서 Δν(Hz)와 δ(ppm)는?",
   a="100 MHz: 220 Hz, 2.2 ppm / 600 MHz: 1320 Hz, 2.2 ppm",
   flow=[("계산", "σ 차이 = 0.00002 − 0.0000178 = 0.0000022"),
         ("계산", "Δν = 100 × 10⁶ × 0.0000022 = 220 Hz → δ = 220/100 = 2.2 ppm"),
         ("계산", "600 MHz: Δν = 1320 Hz → δ = 1320/600 = 2.2 ppm"),
         ("결론", "Hz는 자석에 비례해 바뀌고 δ는 그대로 (지름길: δ = σ차이 × 10⁶)")],
   one="δ = Δν(Hz)/ν₀(Hz) × 10⁶")],
 "c-integ": [dict(src="마스터 요약 예제", title="적분비로 수소 개수 정하기",
   q="분자식 C₄H₈O₂인 화합물의 ¹H-NMR에서 신호 3개의 적분 높이가 6 mm : 4 mm : 6 mm였다. 각 신호의 수소 개수는?",
   a="3H : 2H : 3H",
   flow=[("계산", "가장 작은 값으로 나누기 → 1.5 : 1 : 1.5 → ×2 → 3 : 2 : 3"),
         ("계산", "합 8 = 분자식 H 수 8 ✓"),
         ("연결", "예: 에틸 아세테이트 CH₃CO– (3H) · –OCH₂– (2H) · –CH₃ (3H)")],
   one="적분비 → 정수비 → 총 H 수로 맞추기")],
 "c-j": [dict(src="슬라이드 15", title="갈라진 간격으로 J 구하기",
   q="프로필 아세테이트의 270 MHz ¹H-NMR에서 –OCH₂– 삼중선의 바깥 두 피크가 4.06 ppm과 4.02 ppm에 있다. 짝지음 상수 J(Hz)는?",
   a="J = 5.4 Hz",
   flow=[("단서", "삼중선의 바깥 간격 = 2J (이웃한 두 줄 간격이 J)"),
         ("계산", "4.06 − 4.02 = 0.04 ppm = 2J → J = 0.02 ppm"),
         ("계산", "J(Hz) = 0.02 × 270 = 5.4 Hz")],
   one="J(Hz) = 간격(ppm) × MHz")],
}

def kind_src(e):
    s = re.sub("<[^>]+>", "", e.get("src", "")).strip()
    return s

LBL_CALC = re.compile(r"(=\s*[−\d(]|[\d)]\s*[×÷/]\s*[\d(]|\d\s*[−+]\s*\d)")
TRAP = ("✗", "함정", "잊", "빼먹", "주의", "반대", "아니", "X ", "→ X", "바꿔치기", "틀림")

def conv_steps(steps, kinds):
    fl = []
    n = len(steps)
    for i, s in enumerate(steps):
        main = s[0]; why = s[1] if len(s) > 1 else ""
        t = re.sub("<[^>]+>", "", main)
        if any(k in t for k in TRAP): lab = "함정 체크"
        elif LBL_CALC.search(t): lab = "계산"
        elif i == 0: lab = "단서"
        elif "?" in t: lab = "질문"
        else: lab = "연결"
        fl.append((lab, main, why))
    return fl

def conv_opx(opx):
    rows = re.findall(r"<div>(.*?)</div>", opx, re.S)
    return [("보기", r) for r in rows]

def split_opts(q):
    m = re.search(r'<ol class="opts">(.*?)</ol>', q, re.S)
    if not m: return q, None
    opts = [re.sub(r"^\s*[①②③④⑤]\s*", "", x).strip() for x in re.findall(r"<li>(.*?)</li>", m.group(1), re.S)]
    return q[:m.start()] + q[m.end():], opts

items = []
for e in ENTRIES:
    if e["t"] == "c" and e.get("id") in EX:
        for x in EX[e["id"]]:
            items.append(dict(part=PNAME[e["part"]], t=PT[e["part"]], src=x["src"], title=x["title"], q=x["q"], opts=None,
                              a=x["a"], flow=x["flow"], one=x["one"], ex=True))
    if e["t"] == "q":
        q, opts = split_opts(e["q"])
        fl = conv_steps(e.get("steps", []), e["kind"])
        if e.get("opx"): fl += conv_opx(e["opx"])
        if e.get("extra"):
            ex = re.sub(r'<div class="ct">(.*?)</div>', r"<b>\1</b> ", e["extra"])
            ex = re.sub(r"</?div[^>]*>", " ", ex)
            fl.append(("연결", ex.strip()))
        items.append(dict(part=PNAME[e["part"]], t=PT[e["part"]], src=kind_src(e), title=e["title"], q=q, opts=opts,
                          a=e["a"], flow=fl, one=e["one"], ex=False))

def chip_src(it):
    s = it["src"]
    col = "#c4571b" if ("족보" in s or "기출" in s) else "#1f6fb8" if "과제" in s else "#7048b8" if it["ex"] else "#127a76"
    tag = "예제" if it["ex"] else "문제"
    return f'<span class="chip" style="color:{col};border-color:{col}">{H.escape(s.split("·")[0].strip()) if s else tag}</span>'

rows = []
for i, it in enumerate(items, 1):
    it["num"] = i
    rows.append(prob_row(it, "문제", chip_src(it)))

# ---- 1쪽: 시험 직전 5분 한 장 정리 ----
S = [
 ("basic", "빛의 기본", "c = λν · E = hν = hc/λ", "매질: ν 고정, λ·속도 ÷n<br>E ∝ ν ∝ 1/λ"),
 ("basic", "영역 ↔ 일", "X선 속전자 · UV/Vis 바깥 전자", "IR 진동 · 마이크로파 회전 · 라디오파 핵 스핀"),
 ("basic", "에너지 3층", "전자 ≫ 진동 ≫ 회전", "분자 = 띠(10–100 nm) · 원자 = 선(0.001 nm)"),
 ("basic", "S vs T", "T₁ 에너지 < S₁", "흡수는 S→S가 압도적(스핀 그대로)"),
 ("uv", "흡광도", "A = −log T = εbc", "T 10 % → A 1 · log 2 = 0.30 · 측정 A 0.3–1.5"),
 ("uv", "비흡광도", "E¹%₁cm = A/(b·c)", "c = g/100 mL! · ε = E × MW/10"),
 ("uv", "장치", "D₂ 110–400 · W 320–2500 · HCL 선", "UV = 석영 셀 · PMT 90 V 10⁶배 · PDA 동시·S/N↑·튼튼"),
 ("uv", "발색·이동", "K = π→π* 강 · R = n→π* 약", "batho 빨강 · hypso 파랑 · hyper ↑ · hypo ↓ · 공액 +30 nm ε×2"),
 ("uv", "정량 4종", "x = A/E × f · x = s·Aₓ/(A_T−Aₓ)", "다점 |X절편| = b/a · 검량선 (A−b)/a · T = S·A_T/A_S"),
 ("fl", "형광 vs 인광", "S₁→S₀ 10⁻⁸ s · T₁→S₀ 느림", "파장: 흡수 < 형광 < 인광 · 감도 형광 ≫ 흡광"),
 ("fl", "여기/방출", "여기 = λex 스캔 · 방출 = λem 스캔", "단색화장치 2개 · 검출기 90° · I = kP₀c → 레이저"),
 ("or", "선광도", "[α] = 100α/(l·c)", "l = mm, c = g/mL · [M] = [α]·MW/1000"),
 ("or", "포도당 · ee", "포도당 mg = α × 1895.4", "광학순도 = ee · 많은 쪽 = (100+ee)/2"),
 ("at", "원자분광", "AES 열→발광 · AAS 흡수 · AFS 90°", "HCL 선 193–852 nm · Ne/Ar 500 V"),
 ("at", "원자화", "화염 2400–2700 K · 흑연로 Ar·μL·감도↑", "ICP 스파크→RF→6000–10000 K · 할로젠 X"),
 ("nmr", "NMR 핵·진동수", "¹H ¹³C ¹⁵N ¹⁹F ³¹P · ν₀ = γB₀/2π", "2.35 T = 100 MHz · ¹³C = 1/4"),
 ("nmr", "화학적 이동", "δ = Δν(Hz)/ν₀(Hz) × 10⁶", "전자↑ = 차폐 = 오른쪽 · 벤젠 7.27 · 알카인 2–3"),
 ("nmr", "짝지음 · FT", "n+1 · 파스칼 · J(Hz) 고정", "펄스 → FID → FT · ¹³C 1.1 %·0–220 ppm·단일선"),
]
cards = "".join(f'<div class="sc" style="border-top-color:{TOPIC[t][1]}"><b>{n}</b><span class="f">{f}</span><br>{d}</div>' for t, n, f, d in S)
legend = "".join(f'<span style="color:{c}">{n}</span>' for n, c in TOPIC.values())
summary = f'''<div data-kind="정리" data-title="의약품분석학 II 중간고사 — 시험 직전 5분 한 장 정리" data-meta="Lecture 2–4 · 뒤에 예제·문제 {len(items)}개 + 사고의 흐름 풀이" data-mode="raw">
<div class="legend">{legend}</div><div class="sum">{cards}</div>
<div class="bar" style="background:#1f6fb8"><span class="lb">🧠 전 범위 한 문장</span>빛을 먹으면(흡수 A = εbc) → 다시 내고(형광 I = kP₀c) → 돌리고(선광 [α]) → 원자로 쪼개 재고(AAS·ICP) → 핵을 뒤집어 구조를 읽는다(NMR δ·n+1)</div>
<div class="bar" style="background:#b42318"><span class="lb">⚠️ 함정 TOP 6</span>① mg→g, c = g/100 mL(E) vs g/mL([α]) ② 분취 배수 ×10 ③ [M]은 ÷1000 ④ HCL = 선 광원 ⑤ 전자↑ = 차폐 = δ↓ ⑥ J(Hz)·δ는 자석과 무관</div></div>'''

stage = summary + f'<div data-kind="문제" data-mode="rows" data-per="3">{"".join(rows)}</div>'
DOC = "의약품분석학 II 중간고사 · 한 장 정리 + 예제·문제 풀이"
open(os.path.join(D, "book.html"), "w").write(document(DOC, stage))
open(os.path.join(D, "paginate.js"), "w").write("(" + PAGINATE_JS + ")()")
open(os.path.join(D, "render.js"), "w").write(RENDER_JS)
print("items", len(items), "examples", sum(1 for i in items if i["ex"]))
