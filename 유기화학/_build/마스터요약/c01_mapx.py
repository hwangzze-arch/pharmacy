# -*- coding: utf-8 -*-
"""1쪽 반응 지도 5줄 — 그림별 해설 (2쪽). 그림은 c00_front.MAPR 그대로."""
from c00_front import MAPR

CSS = """<style>
.mxp .mxlead{flex:none;margin-top:8px;background:#fff4e6;border:1px solid #ffd8a8;border-left:6px solid #e8590c;border-radius:9px;padding:5px 12px;font-weight:700;color:#7a2e00;}
.mxp .mxl{flex:1;min-height:0;display:flex;flex-direction:column;gap:7px;margin-top:7px;}
.mxp .mxr{display:grid;grid-template-columns:var(--mxw,40%) 1fr;gap:12px;border:1px solid #dfe5ee;border-radius:11px;padding:6px 10px;background:#fff;align-items:start;}
.mxp .mxf{border-right:1px dashed #d3deee;padding-right:8px;overflow:hidden;align-self:center;}
.mxp .mxf .tx,.mxp .mxf .arw{white-space:nowrap;}
.mxp .mxn{display:inline-block;background:#1d3557;color:#fff;font-weight:700;border-radius:6px;padding:0 8px;margin-bottom:3px;font-size:.92em;}
.mxp .mxh{font-weight:700;color:#0f3f8c;font-size:1.04em;margin-bottom:2px;}
.mxp .mxflow{font-size:.9em;color:#495057;background:#f6f8fc;border-radius:6px;padding:1px 7px;margin-bottom:3px;}
.mxp .mxt ol{margin:0;padding-left:1.25em;} .mxp .mxt li{margin:0 0 2px 0;} .mxp .mxt p{margin:0 0 2px 0;}
.mxp .mxsum{flex:none;display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-top:7px;}
.mxp .mxs{border-radius:10px;padding:6px 11px;font-size:.95em;}
.mxp .mxs.a{background:#fff9db;border:1px solid #ffe066;} .mxp .mxs.b{background:#e7f5ff;border:1px solid #a5d8ff;}
.mxp .mxs b.t{display:block;margin-bottom:2px;}
</style>"""

ROWS = [
 ("1️⃣ 첫째 줄", "산성 α-할로젠화 → E2 제거로 ‘α,β-불포화 케톤’ 만들기", "개념 03·04",
  "케톤 →(H⁺) 엔올 →(X₂) α-할로 케톤 (1번, 붐비는 쪽) →(피리딘, Δ) α,β-불포화 케톤",
  "<ol><li><b>엔올화 (H⁺)</b>: 케톤에 산을 넣으면 카르보닐 산소가 H⁺를 받아먹고, 옆의 α-H가 빠져 <b>C=C 이중결합을 가진 공격수 ‘엔올(C=C–OH)’</b>로 변신. 산성 조건에서는 천천히 가장 튼튼한 이중결합(자이체프 규칙)을 만들므로 <y>더 치환된(붐비는) 쪽</y>으로 엔올이 만들어진다.</li>"
  "<li><b>할로젠화 (X₂)</b>: 엔올의 α 탄소가 Br₂를 공격해 붐비는 쪽 α 자리에 Br을 <y>딱 1개만</y> 붙인다. (Br이 전자를 끌어당겨 두 번째 양성자화를 방해하므로 1번만 반응하고 멈춤!)</li>"
  "<li><b>E2 제거 (피리딘, Δ)</b>: 이 Br은 다음 반응을 위한 발판! 약하고 덩치 있는 염기인 피리딘을 넣고 <b>가열(Δ)</b>하면, 이웃한 β 탄소의 H와 α 탄소의 Br이 동시에 빠져나가면서(E2), 카르보닐(C=O) 바로 옆에 콘쥬게이션된 안정한 <b>C=C 이중결합(α,β-불포화 케톤)</b>이 완성된다!</li></ol>"),
 ("2️⃣ 둘째 줄", "카복실산의 α-브로민화 (HVZ 반응) → S<sub>N</sub>2 응용", "개념 05·06",
  "카복실산 →(1. Br₂, PBr₃ / 2. H₂O) α-브로모 카복실산 →(NH₃ 등, S<sub>N</sub>2) α-아미노산 등",
  "<ol><li><b>문제 상황</b>: 카복실산(–COOH)은 옆의 –OH 산소가 카르보닐에 전자를 퍼줘서 배가 부르기 때문에, 그냥 Br₂를 넣어선 죽어도 엔올로 변신하지 않는다.</li>"
  "<li><b>HVZ 꼼수 (1. Br₂, PBr₃ / 2. H₂O)</b>: 해결사 <b>PBr₃</b>를 넣어 –COOH를 엔올 변신이 아주 잘 되는 <y>‘산 브로마이드(–COBr)’</y>로 잠깐 위장 → 그 상태에서 엔올이 되어 α 자리에 Br을 하나 붙인 뒤(물 넣기 전 중간체: α-브로모 산 브로마이드) → 마지막에 <b>물(H₂O)</b>을 부어 끝자리만 다시 원래의 카복실산(–COOH)으로 복구!</li>"
  "<li><b>S<sub>N</sub>2 응용 (NH₃ 등)</b>: α 자리에 좋은 이탈기인 Br을 심어놓으면, 아민(NH₃나 t-BuNH₂)을 넣어 등 뒤를 찌르는 S<sub>N</sub>2 반응으로 Br을 쫓아내고 <y>아미노산이나 부프로피온(항우울제)</y> 같은 의약품을 손쉽게 만들 수 있다!</li></ol>"),
 ("3️⃣ 셋째 줄", "말론산 에스터 합성 → 탄소 2개 늘어난 ‘카복실산’ 만들기", "개념 11·12",
  "말론산 에스터 →(1. NaOEt / 2. R–X) 알킬화 말론산 에스터 →(H₃O⁺, Δ, −CO₂) 치환된 카복실산 (R–CH₂COOH)",
  "<ol><li><b>왜 말론산 에스터인가?</b> 일반 에스터(pK<sub>a</sub> 25)는 수소가 안 빠지지만, 양쪽에 에스터 2개가 달린 <b>말론산 에스터(pK<sub>a</sub> 13)</b>는 양쪽에서 전자를 끌어당겨 주므로(샌드위치 효과) 값싼 <y>NaOEt</y>(에스터 교환 막으려고 같은 –OEt 염기 사용!)만 넣어도 가운데 수소가 100% 빠져 강력한 공격수(엔올레이트, C⁻)가 된다.</li>"
  "<li><b>S<sub>N</sub>2 알킬화 (2. R–X)</b>: 이 C⁻가 날렵한 알킬 할라이드(R–X, <y>메틸·1차·알릴·벤질만 가능!</y>)의 등 뒤를 S<sub>N</sub>2 공격해 가운데 탄소에 새로운 탄소 사슬(R)을 붙인다. (가운데 수소가 2개이므로 최대 2번까지 알킬화 가능!)</li>"
  "<li><b>가수분해 및 탈카르복실화 (H₃O⁺, Δ)</b>: 산성 물에 넣고 <b>가열(Δ)</b>하면, 양쪽 에스터가 –COOH 2개로 가수분해된 뒤 <b>6원 고리 전이상태</b>를 거쳐 여분의 –COOH 한 짝이 CO₂ 기체로 뽀글뽀글 날아가 버리고, 수소는 그 자리에 남아 <y>탄소 2개가 늘어난 카복실산(R–CH₂COOH)</y>이 탄생!</li></ol>"),
 ("4️⃣ 넷째 줄", "아세토아세트산 에스터 합성 → 탄소 3개 늘어난 ‘메틸 케톤’ 만들기", "개념 13",
  "아세토아세트산 에스터 →(1. NaOEt / 2. R–X) 알킬화 →(H₃O⁺, Δ, −CO₂) 치환된 메틸 케톤 (R–CH₂COCH₃)",
  "<ol><li><b>셋째 줄(말론산)과의 유일한 차이점</b>: 출발 물질의 왼쪽이 에스터가 아니라 <b>메틸 케톤(CH₃CO–)</b>이고 오른쪽만 에스터(–CO₂Et)인 일란성 쌍둥이(pK<sub>a</sub> 11)!</li>"
  "<li><b>과정과 결과</b>: 똑같이 1. NaOEt로 가운데 수소를 뽑고 2. R–X로 S<sub>N</sub>2 알킬화를 한 뒤, 마지막에 H₃O⁺, 가열(Δ)을 하면 오른쪽의 에스터(–CO₂Et) 한 짝만 CO₂ 기체로 날아가고, 왼쪽에 있던 메틸 케톤 골격이 그대로 남아서 <y>메틸 케톤(R–CH₂COCH₃)</y>이 된다!</li>"
  "<li><b>핵심 역할</b>: 오른쪽 에스터(–CO₂Et)는 <b>“무조건 두 카르보닐 사이(가운데 탄소)의 수소만 뽑아서 여기에만 알킬화해!”</b>라고 위치를 지정해 준 뒤, 볼일 끝나면 CO₂로 사라져 주는 <y>‘길 안내 도우미’</y>! (문제 27번의 a → b 단계!)</li></ol>"),
 ("5️⃣ 다섯째 줄", "뚱보 염기 LDA 직접 알킬화 & 염기 과량 ‘할로폼 반응’", "개념 07·09·15",
  "비대칭 케톤(2-메틸사이클로헥사논) →(1. LDA, THF / 2. CH₃I) 덜 붐비는 쪽 메틸화 · 메틸 케톤 →(X₂, NaOH 과량) RCOO⁻ + CHX₃",
  "<p><b>전반부 — LDA 직접 알킬화 (1. LDA, THF / 2. CH₃I)</b></p><ol>"
  "<li>에스터 도우미 없이 평범한 케톤(pK<sub>a</sub> 19)이나 에스터(25), 니트릴(25)의 수소를 한 방에 100% 뽑으려면 초강력 염기 <b>LDA(짝산 pK<sub>a</sub> 36)</b>를 써야 한다.</li>"
  "<li>특히 <b>LDA는 양옆에 거대한 아이소프로필기 날개를 단 ‘엄청난 뚱보 염기’</b>라서, 메틸기가 가로막고 있는 비좁은 쪽(C2)을 싫어하고 입구가 뻥 뚫려 한산한(덜 붐비는) 반대쪽(C6)의 수소를 빠르게 낚아채어(속도론적 엔올레이트) <y>그 한산한 자리에 메틸기(–CH₃)</y>를 붙인다! (※ 첫째 줄 산성 조건이 ‘붐비는 쪽’이었던 것과 정반대!)</li></ol>"
  "<p><b>후반부 화살표 — 메틸 케톤의 할로폼 반응 (X₂, NaOH 과량)</b></p><ol>"
  "<li>한쪽에 메틸기(–CH₃)가 달린 메틸 케톤에 산 대신 염기(NaOH)와 할로젠(X₂)을 과량으로 넣으면?</li>"
  "<li>첫 번째 X가 붙으면 X의 강력한 전자 끌기 때문에 같은 탄소에 남은 수소들의 산성도가 훨씬 강해져서, 멈추지 않고 <y>3번 연속 폭주하여 –CH₃가 –CX₃</y>가 된다!</li>"
  "<li>그다음 OH⁻가 카르보닐 탄소(C=O)를 공격해 올라갔다가 내려오면서, 할로젠 3개 덕분에 안정해진 <b>⁻CX₃ 음이온</b>을 통째로 끊어내어 쫓아낸다!</li>"
  "<li>결국 메틸기가 잘려 나간 <b>할로폼(CHX₃, I₂를 쓰면 노란 침전 아이오도폼 CHI₃)</b>과 탄소 1개가 줄어든 <b>카복실산염(RCOO⁻)</b>으로 쪼개진다!</li></ol>"),
]


def _row(k):
    a, h, c, flow, body = ROWS[k]
    return (f'<div class="mxr"><div class="mxf"><div class="mz">{MAPR[k]}</div></div>'
            f'<div class="mxt"><span class="mxn">{a} · {c}</span><div class="mxh">{h}</div><div class="mxflow">흐름: {flow}</div>{body}</div></div>')


def _page(title, sub, idx, extra=""):
    return f'''{CSS}
<div class="hd"><span class="bd">22장</span><div class="tt"><h1>{title}</h1><div class="sb">{sub}</div></div><span class="pt">반응 지도 해설</span></div>
<div class="mxlead">22장 대주제: 원래 얌전하던 α 탄소를 공격수(친핵체: 엔올 또는 엔올레이트)로 변신시켜서, 원하는 부품(Br이나 탄소 사슬 R)을 낚아채 붙인다!</div>
<div class="mxl">{"".join(_row(k) for k in idx)}</div>{extra}'''


SUM = ('<div class="mxsum"><div class="mxs a"><b class="t">💡 산성 경로 (첫째·둘째 줄 = 엔올)</b>산(H⁺)이 촉매 → 중성이라 공격력이 약해 할로젠(X₂) 정도만 붙임 → <b>더 치환된(붐비는) 쪽 공격, 딱 1번만!</b></div>'
       '<div class="mxs b"><b class="t">💡 염기 경로 (셋째·넷째·다섯째 줄 = 엔올레이트)</b>염기(NaOEt 또는 LDA) 사용 → 진짜 음이온(C⁻)이라 공격력이 막강해 알킬 할라이드(R–X)와 S<sub>N</sub>2로 탄소 사슬을 붙임 → <b>LDA는 덜 치환된(한산한) 쪽, 염기성 할로젠화는 끝까지 폭주(할로폼)!</b></div></div>')

mx1 = dict(t="r", id="f-mapx1", cls="mxp", html=_page("🗺 반응 지도 5줄 해설 ① — 산성 경로 (엔올)", "앞 쪽 반응 지도의 첫째·둘째 줄 · 그림 옆에 원리", [0, 1]))
mx2 = dict(t="r", id="f-mapx2", cls="mxp", html=_page("🗺 반응 지도 5줄 해설 ② — 말론산 · 아세토아세트산", "앞 쪽 반응 지도의 셋째·넷째 줄", [2, 3]))
mx3 = dict(t="r", id="f-mapx3", cls="mxp", html=_page("🗺 반응 지도 5줄 해설 ③ — LDA · 할로폼 + 한 줄 요약", "앞 쪽 반응 지도의 다섯째 줄 + 아래 표(엔올 vs 엔올레이트) 한 줄 요약", [4], SUM))
