# -*- coding: utf-8 -*-
"""맥머리 10판(OpenStax) 22장 본문 예제·문제 — 원서 그대로 (문제 그림 = 원서 캡처).
왼쪽: 원서 문제 그림 + 번역 / 오른쪽: 원서 정답(Answer Key) + 해설집(SSM) 풀이 + 한글 단계 설명."""
from parts import P1, P2, P3

I = "img/"


import os
from PIL import Image as _Im
_FULL = {"tp": 1497, "we": 1497, "ta": 1497, "ss": 1500}  # 원서 한 줄 폭(px)


def _qimg(name):
    """왼쪽 문제 그림: 칸이 원서보다 좁아서 1.3배, 답안 쪽 축소와 무관."""
    px = _Im.open(os.path.join(os.path.dirname(__file__), "img", name + ".jpg")).width
    w = min(100, round(130 * px / _FULL[name[:2]], 1))
    return f'<img src="{I}{name}.jpg" style="width:{w}%;display:block;margin:2px 0">'


def _img(name, w=None):
    """원서 글자 크기가 일정하도록 실제 폭 비율로 (답안 칸에서는 render.js가 --aimg로 더 줄임)."""
    if w is None:
        px = _Im.open(os.path.join(os.path.dirname(__file__), "img", name + ".jpg")).width
        w = min(100, round(100 * px / _FULL[name[:2]], 1))
    return f'<img class="tbimg" src="{I}{name}.jpg" style="width:calc({w}% * var(--aimg, 1));display:block;margin:2px 0">'


def tb(n, part, title, kind, ko, a, steps, key=True, ss=None, extra=""):
    """본문 문제 22-n."""
    figs = ""
    if key:
        figs += '<div class="sec" style="color:#0f6b52;margin-top:4px">📗 원서 정답 (Answer Key)</div>' + _img(f"ta{n:02d}")
    if ss:
        figs += '<div class="sec" style="color:#0f6b52;margin-top:4px">📘 해설집 풀이 (SSM 22.' + str(n) + ')</div>' + "".join(_img(s) for s in ss)
    return dict(t="q", part=part, kind=kind, src=f"본문 Problem 22-{n} (원서 그대로)", title=f"Problem 22-{n} — {title}",
                q=_qimg(f"tp{n:02d}") + f'<div class="term" style="margin-top:6px">번역: {ko}</div>',
                a=a, steps=steps, extra=figs + extra, one=None)


def we(n, part, title, ko, a, steps, qimg, simg):
    """본문 Worked Example 22.n."""
    return dict(t="q", part=part, kind=["ex"], src=f"본문 Worked Example 22.{n} (원서 그대로)", title=f"Worked Example 22.{n} — {title}",
                q=_qimg(qimg) + f'<div class="term" style="margin-top:6px">번역: {ko}</div>',
                a=a, steps=steps,
                extra='<div class="sec" style="color:#0f6b52;margin-top:4px">📗 원서 풀이 (Strategy · Solution)</div>' + _img(simg), one=None)


# ───────── PART 1 (22.1–22.4)
T1 = [
tb(1, P1, "엔올 토토머 그리기", ["draw"],
   "다음 화합물의 엔올 토토머 구조를 그리시오: (a) 사이클로펜탄온 (b) 메틸 싸이오아세테이트 (c) 에틸 아세테이트 (d) 프로판알 (e) 아세트산 (f) 페닐아세톤",
   "α 탄소와 C=O 탄소 사이 C=C, 산소는 –OH (원서 정답 그림)",
   [("C=O 바로 옆 sp³ 탄소(α)를 찾는다.", "그 α와 C=O 탄소 사이를 C=C로, C=O의 산소를 –OH로."),
    ("(f) 페닐아세톤은 α가 양쪽(CH₃, CH₂Ph) → 엔올 두 가지.", "(d)(f)는 cis/trans 엔올도 가능.")], ss=["ss01"]),
tb(2, P1, "산성 수소 개수", ["sa"],
   "문제 22-1의 각 분자는 산성 수소를 몇 개 가지는가? 표시하시오.",
   "(a) 4 (b) 3 (c) 3 (d) 2 (e) 4 (f) 5",
   [("α 탄소의 H를 센다 (해설집 그림에서 굵게 표시된 H).", ""),
    ("(e) 아세트산: α-CH₃ 3개 + O–H 1개 = 4.", ""),
    ("(f) CH₃ 3개 + CH₂ 2개 = 5.", "")]),
tb(3, P1, "모노엔올과 안정성", ["draw", "sa"],
   "다음 분자의 모든 모노엔올 구조를 그리시오. 어느 것이 가장 안정할 것으로 예상하는가? 설명하시오.",
   "두 C=O 사이(C2)로 엔올화한 엔올 2개(서로 같음)가 더 안정 — 엔올 C=C가 C=O와 콘쥬게이션",
   [("분자 = 사이클로헥세인-1,3-다이온. α 탄소: C2, C4, C6.", ""),
    ("C2 쪽 엔올: C=C–C=O 콘쥬게이션 → 더 안정.", "해설집: “The first two monoenols are more stable because the enol double bond is conjugated with the carbonyl group.”"),
    ("C4/C6 쪽 엔올은 콘쥬게이션 없음 → 덜 안정.", "")], ss=["ss03"]),
tb(4, P1, "D₃O⁺ 중수소화 메커니즘", ["mech"],
   "아세톤을 D₃O⁺로 처리할 때 중수소화의 완전한 메커니즘을 쓰시오. (CH₃COCH₃ → CH₃COCH₂D)",
   "산 촉매 엔올 형성 → 엔올 이중결합에 D 첨가(중수소화) → 산소의 D 제거",
   [("① C=O 산소가 D₃O⁺의 D를 받음 → ② D₂O가 α-H를 뗌 → 엔올.", "슬라이드 4의 산 촉매 엔올화."),
    ("③ 엔올 C=C가 D₃O⁺의 D를 공격 → ④ D₂O가 O–D의 D⁺를 뗌 → CH₃COCH₂D.", "할로젠화와 같은 틀, E⁺ = D⁺.")], ss=["ss04"]),
tb(5, P1, "1-펜텐-3-온 만들기", ["reag"],
   "3-펜탄온으로부터 1-펜텐-3-온을 어떻게 만들 수 있는지 보이시오.",
   "1. Br₂ (CH₃CO₂H)  2. 피리딘, 가열",
   [("α-브로민화로 α 탄소에 Br.", "산성 조건 엔올 경로."),
    ("피리딘·가열로 E2 → HBr 제거 → α,β-불포화 케톤.", "슬라이드 11.")], ss=["ss05"]),
tb(6, P1, "HVZ 후 메탄올 → 에스터", ["mech", "int"],
   "Hell–Volhard–Zelinskii 반응의 마지막에 물 대신 메탄올을 넣으면 산이 아니라 에스터가 생긴다. 다음 변환을 어떻게 수행할지 보이고, 에스터 생성 단계의 메커니즘을 제시하시오.",
   "1. Br₂, PBr₃  2. CH₃OH — 중간체 α-브로모 산 브로마이드가 메탄올과 친핵성 아실 치환 → α-브로모 에스터",
   [("HVZ: –COOH → –COBr → 엔올 → Br₂ → α-브로모 산 브로마이드.", ""),
    ("CH₃OH가 C=O 첨가 → 사면체 → Br⁻ 이탈 → H⁺ 이탈 → 메틸 에스터.", "21장 친핵성 아실 치환.")], ss=["ss06"]),
]

# ───────── PART 2 (22.5–22.6)
T2 = [
we(1, P2, "화합물의 산성 수소 찾기",
   "다음 화합물에서 가장 산성인 수소를 찾고, 산성도가 증가하는 순서로 배열하시오. (a) 1-페닐-1,3-뷰테인다이온 (b) 메틸 2-메틸프로파노에이트 (c) 사이클로펜테인카브알데하이드",
   "산성도: (a) &gt; (c) &gt; (b)",
   [("<b>전략</b>: 카르보닐 옆 탄소의 H가 산성. β-다이카르보닐 &gt; 케톤·알데하이드 &gt; 카복실산 유도체(에스터).", ""),
    ("(a) 두 C=O 사이 CH₂ (pKa ≈ 9) — 가장 산성. 끝 CH₃는 덜 산성.", ""),
    ("(c) 알데하이드 α-H (≈ 17) &gt; (b) 에스터 α-H (≈ 25).", "")], "we1q", "we1s"),
tb(7, P2, "가장 산성인 수소", ["sa"],
   "다음 분자에서 가장 산성인 수소를 찾으시오: (a) CH₃CH₂CHO (b) (CH₃)₃CCOCH₃ (c) CH₃CO₂H (d) 벤즈아마이드 (e) CH₃CH₂CH₂CN (f) CH₃CON(CH₃)₂",
   "(a)(b)(e)(f) α-H (약산) · (c) O–H (가장 산성) · (d) N–H",
   [("카르보닐·니트릴 하나 옆 α-H = 약한 산.", "해설집: “Hydrogens α to one carbonyl group (or nitrile) are weakly acidic.”"),
    ("(c) 카복실산은 O–H가 압도적으로 산성.", ""),
    ("(d) 벤즈아마이드엔 α 탄소가 없어 N–H.", "")], ss=["ss07"]),
tb(8, P2, "아세토나이트릴 음이온의 공명", ["draw", "sa"],
   "아세토나이트릴 음이온 ⁻:CH₂C≡N의 공명 구조를 그리고, 니트릴이 산성인 이유를 설명하시오.",
   "⁻:CH₂–C≡N: ↔ H₂C=C=N:⁻ — 음전하가 니트릴의 π 결합을 통해 N으로 비편재화",
   [("탄소 음이온의 전자쌍이 C≡N의 π 결합으로 내려가 N에 음전하.", ""),
    ("공명 안정화된 음이온 → 니트릴 α-H는 약하게 산성 (pKa 25).", "")], ss=["ss08"]),
tb(9, P2, "산 촉매 vs 염기 촉진", ["sa"],
   "산성 매질의 케톤 할로젠화는 왜 산 ‘촉매’라 하고, 염기성 매질의 할로젠화는 염기 ‘촉진’이라 하는가? 즉, 왜 할로젠화에 염기가 1당량 이상 필요한가?",
   "산은 다시 생성되지만, 염기는 화학량론적으로 소모된다",
   [("산: R–CO–CH + X₂ —H⁺→ R–CO–CX + H⁺ + X⁻ → H⁺ 재생.", ""),
    ("염기: R–CO–CH + X₂ + B⁻ → R–CO–CX + BH + X⁻ → 염기가 BH로 소모.", "")], ss=["ss09"]),
]

# ───────── PART 3 (22.7)
T3a = [
we(2, P3, "말론산 에스터 합성으로 카복실산 만들기",
   "말론산 에스터 합성으로 헵탄산을 어떻게 만들겠는가?",
   "CH₃CH₂CH₂CH₂CH₂Br + CH₂(CO₂Et)₂ → 1. Na⁺ ⁻OEt 2. H₃O⁺, 가열 → 헵탄산",
   [("<b>전략</b>: 말론산 에스터 합성은 알킬 할라이드를 탄소 2개 긴 카복실산으로 바꾼다.", ""),
    ("헵탄산(C7) → 탄소 5개짜리 할라이드 = 1-브로모펜테인.", "")], "we2q", "we2s"),
tb(10, P3, "말론산 에스터 합성 설계", ["reag"],
   "말론산 에스터 합성으로 다음 화합물을 어떻게 만들겠는가? 모든 단계를 보이시오. (a) 3-페닐프로판산 (b) 2-메틸펜탄산 (c) 4-메틸펜탄산",
   "(a) 1. Na⁺ ⁻OEt 2. PhCH₂Br 3. H₃O⁺ · (b) 1. Na⁺ ⁻OEt 2. CH₃CH₂CH₂Br 3. Na⁺ ⁻OEt 4. CH₃Br 5. H₃O⁺ · (c) 1. Na⁺ ⁻OEt 2. (CH₃)₂CHCH₂Br 3. H₃O⁺",
   [("α 탄소 + COOH = 말론산 에스터에서, α에 붙은 가지 = R–X에서.", "해설집: “Identify the component that originates from malonic ester.”"),
    ("가지가 2개(b)면 알킬화 2번.", "")], ss=["ss10"]),
tb(11, P3, "트라이알킬 아세트산은 왜 안 되나", ["sa"],
   "모노알킬·다이알킬 아세트산은 말론산 에스터 합성으로 만들 수 있지만, 트라이알킬 아세트산(R₃C–CO₂H)은 만들 수 없다. 설명하시오.",
   "말론산 에스터에는 치환될 수 있는 산성 수소가 2개뿐",
   [("알킬화 한 번에 α-H 하나 소모 → 최대 2번.", "")], ss=["ss11"]),
tb(12, P3, "말론산 에스터 합성 (분자 모형)", ["reag"],
   "말론산 에스터 합성으로 다음 화합물(분자 모형)을 어떻게 만들겠는가?",
   "1. Na⁺ ⁻OEt 2. (CH₃)₂CHCH₂Br 3. Na⁺ ⁻OEt 4. CH₃Br 5. H₃O⁺ → 2,4-다이메틸펜탄산",
   [("모형 = 2,4-다이메틸펜탄산. α에 메틸과 아이소뷰틸.", ""),
    ("두 할라이드로 차례로 알킬화 → 가수분해·탈카르복실화.", "")], ss=["ss12"]),
]
T3b = [
we(3, P3, "아세토아세트산 에스터 합성으로 케톤 만들기",
   "아세토아세트산 에스터 합성으로 2-펜탄온을 어떻게 만들겠는가?",
   "CH₃CH₂Br + 아세토아세트산 에틸 → 1. Na⁺ ⁻OEt 2. H₃O⁺, 가열 → 2-펜탄온",
   [("<b>전략</b>: 아세토아세트산 에스터 합성은 알킬 할라이드에 탄소 3개(CH₂COCH₃)를 붙여 메틸 케톤을 만든다.", ""),
    ("2-펜탄온 = CH₃CH₂–CH₂COCH₃ → R = 에틸 → 브로모에테인.", "")], "we3q", "we3s"),
tb(13, P3, "아세토아세트산 에스터 합성의 할라이드", ["reag"],
   "아세토아세트산 에스터 합성으로 다음 케톤을 만들려면 어떤 알킬 할라이드를 쓰겠는가? (a) 5-메틸-2-헥산온 (b) 5-페닐-2-펜탄온",
   "(a) (CH₃)₂CHCH₂Br (b) PhCH₂CH₂Br",
   [("메틸 케톤 CH₃CO–CH₂– 부분 = 아세토아세트산, 나머지 = R–X.", "")], ss=["ss13"]),
tb(14, P3, "만들 수 없는 것", ["sa"],
   "다음 중 아세토아세트산 에스터 합성으로 만들 수 없는 것은? 설명하시오. (a) 페닐아세톤 (b) 아세토페논 (c) 3,3-다이메틸-2-뷰탄온",
   "셋 다 만들 수 없다",
   [("(a) 브로모벤젠이 필요 → S<sub>N</sub>2 불가.", ""),
    ("(b) RCOCH₃형 — 아세토아세트산의 3탄소가 남지 않음.", ""),
    ("(c) α 위치가 3치환 → 알킬화 최대 2번.", "")], ss=["ss14"]),
tb(15, P3, "아세토아세트산 에스터 합성 (분자 모형)", ["reag"],
   "아세토아세트산 에스터 합성으로 다음 화합물(분자 모형)을 어떻게 만들겠는가?",
   "1. 2 Na⁺ ⁻OEt 2. BrCH₂CH₂CH₂CH₂Br 3. H₃O⁺ → 사이클로펜틸 메틸 케톤",
   [("모형 = 사이클로펜틸 메틸 케톤 → 고리를 1,4-다이브로모뷰테인으로.", "염기 2당량: 분자 간 + 분자 내 S<sub>N</sub>2."),
    ("H₃O⁺, 가열로 에스터 제거 → 메틸 케톤.", "")], ss=["ss15"]),
]
T3c = [
we(4, P3, "알킬화로 치환 에스터 만들기",
   "알킬화 반응으로 에틸 1-메틸사이클로헥세인카복실레이트를 어떻게 만들겠는가?",
   "에틸 사이클로헥세인카복실레이트 → 1. LDA, THF 2. CH₃I",
   [("<b>전략</b>: 케톤·에스터·니트릴의 α 위치에 메틸/1차 알킬기를 넣는 데 알킬화(S<sub>N</sub>2)를 쓴다.", ""),
    ("목표의 α에 메틸 → 에스터 엔올레이트(LDA) + 아이오도메테인.", "")], "we4q", "we4s"),
tb(16, P3, "알킬화를 핵심 단계로", ["reag"],
   "알킬화 반응을 핵심 단계로 하여 다음 화합물을 어떻게 만들 수 있는지 보이시오.",
   "(a) 페닐아세톤 + CH₃I (b) 펜테인나이트릴 + CH₃CH₂I (c) 사이클로헥사논 + H₂C=CHCH₂Br (d) 사이클로헥사논 + 과량 CH₃I (e) C₆H₅COCH₂CH₃ + CH₃I (f) 메틸 3-메틸뷰타노에이트 + CH₃CH₂I",
   [("α의 가지 하나를 떼면 R–X, 나머지가 출발물질 (LDA 또는 NaH).", ""),
    ("(a) 페닐 옆 탄소에서 알킬화 — 페닐이 엔올레이트를 안정화.", "해설집 설명."),
    ("(d) 과량 LDA·CH₃I로 4번.", "")], ss=["ss16"]),
]
