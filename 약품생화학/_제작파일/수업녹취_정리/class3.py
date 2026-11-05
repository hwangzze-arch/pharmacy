"""기말고사 대비 수업3 (동영상 강의) 녹취록 정리 → index.html (A4 세로)
원문: 사용자가 채팅으로 준 영문 녹취 + 국문 해석 (2026-11-01)
python3 class3.py && NODE_PATH=$(npm root -g) node render.js "$PWD/out.pdf"
"""
import os
from class1 import CSS, D, esc_table

POINTS = [
    ("00:00–01:41", "수용체 조절 — ADP가 호흡의 액셀",
     "산화적 인산화는 <b>ADP의 가용성</b>(= 세포의 에너지 요구)으로 조절된다 = <b>acceptor control of respiration</b>. <b>수용체 조절비 &gt; 10</b>. ADP는 ATP 합성의 기질이라 ADP ↑ → ATP 합성·O₂ 소비 ↑. 또 <b>질량작용비 [ATP]/([ADP][Pᵢ])</b>도 조절: ATP를 쓰면 이 비가 ↓ → 호흡 속도 ↑.",
     "개념 18 (p.74) · 기출 19-22 · 19-23 · 19-63 (p.79, 80, 82)"),
    ("01:42–02:27", "ATP 생성 경로는 한꺼번에 조절된다",
     "ATP/ADP 비, <b>NADH/NAD⁺ 비</b>, <b>시트르산</b>이 해당과정·시트르산 회로·산화적 인산화를 함께(협동적으로) 조절.",
     "개념 18 (p.74)"),
    ("02:28–04:55", "IF₁ — 저산소에서 ATP ‘역주행’(가수분해) 방지",
     "효소 반응은 거꾸로도 가므로 ATP 합성효소가 <b>ATPase</b>로 작동해 ATP를 낭비할 수 있다. 저산소 → 전자전달·ATP 합성 ↓ → 피루브산·젖산 ↑ → <b>pH ↓</b> → <b>IF₁이 이량체(dimer)</b>가 되어 ATP 가수분해 억제(ATP 절약). 산소가 돌아오면 pH ↑ → 이량체가 풀려 ATP 합성 재개.",
     "개념 19 (p.75)"),
    ("04:56–08:52", "ROS 3종과 HIF-1",
     "ROS = <b>초과산화물 라디칼(O₂•⁻), 과산화수소(H₂O₂), 하이드록실 라디칼(•OH)</b> — O₂와 H₂O 사이의 서로 다른 산화 상태. 산화적 인산화(유비퀴놀 쪽에서 새는 전자) 외에 방사선·염증·금속·약물도 원인. 방어 = <b>글루타티온 과산화효소 + 글루타티온</b>. 저산소에선 <b>HIF-1</b>이 해당 ↑, <b>PDH ↓</b> → TCA·산화적 인산화가 느려져 <b>ROS ↓</b>, Complex IV는 낮은 O₂에 적응.",
     "개념 20 (p.76) · 기출 19-24 · 19-65 (p.81, 84)"),
    ("09:51–11:36", "열발생 — 갈색지방의 thermogenin",
     "신생아 <b>목·등</b>의 갈색지방세포는 미토콘드리아가 많고, <b>thermogenin(UCP1)</b>이 H⁺ 통로가 되어 H⁺가 ATP 합성효소 대신 그쪽으로 흐름 → <b>ATP 대신 열</b>(짝풀림) → 아기 체온 유지.",
     "개념 21 (p.85) · 기출 19-25 (p.93)"),
    ("11:37–14:43", "P450: 해독(NAPQI 주의)과 스테로이드 합성",
     "해독: 산소를 붙여(oxygenation) 약물·외인성 물질을 물에 잘 녹게 → 배설. 가끔 더 독한 물질: <b>타이레놀 과량 → NAPQI</b>(간 독성), <b>음주로 CYP2E1이 많아지면</b> 위험 ↑. 스테로이드: <b>부신 미토콘드리아</b>의 P450이 스테로이드 수산화. 전자 경로 <b>NADPH → (FAD) 아드레노독신 환원효소 → 아드레노독신 → P450</b> → O₂와 직접 반응해 R–OH.",
     "개념 22 (p.86)"),
    ("14:44–15:47", "세포자멸사 — 시토크롬 c 방출이 시작",
     "미토콘드리아 손상 → 세포질의 <b>시토크롬 c ↑</b> → <b>아폽토좀</b> 형성 → <b>카스페이스</b> 활성화 → 프로그램된 세포 죽음.",
     "개념 23 (p.87) · 기출 19-26 · 19-66 (p.94, 98)"),
    ("15:48–20:32", "미토 유전자 · LHON · MERRF · 모계 유전 · 이형세포질성",
     "mtDNA = 전자전달·ATP 합성 부품(<b>ND</b> = Complex I, <b>cyt b</b> = III, <b>cyt oxidase</b> = IV, ATP 합성효소) + tRNA + rRNA + 조절 부위. <b>LHON</b> = ND4 또는 cyt b의 염기 하나 변화 → 중추신경(시신경) → <b>실명</b>. <b>MERRF</b> = <b>tRNA<sup>Lys</sup></b> 돌연변이 → 근력 약화·통제 안 되는 근육 경련. 정자의 미토는 수정 후 난자가 파괴 → <b>모계 유전</b>. 분열 때 돌연변이 미토가 무작위로 나뉘어 세포마다 비율이 다름 = <b>heteroplasmy</b> → 질병·노화.",
     "개념 24 (p.88) · 기출 19-27 · 19-28 · 19-67 (p.95, 96, 99)"),
    ("20:33–22:01", "췌장 β세포 미토 결함 → 당뇨",
     "ATP가 <b>K⁺(ATP) 채널을 막아야</b> → (탈분극) → <b>Ca²⁺ 채널 열림</b> → 인슐린 분비. 미토 결함으로 ATP가 적으면 이 신호가 안 와서 인슐린 분비 ↓ → 당뇨.",
     "개념 25 (p.89)"),
]

SUMMARY = ["갈색지방의 짝풀림된 미토콘드리아는 열을 만든다.", "미토콘드리아 P450 산소화효소는 스테로이드 수산화(스테로이드 합성)를 촉매한다.",
           "미토콘드리아는 세포자멸사 개시의 중심이다.", "mtDNA 돌연변이는 평생 쌓여 노화·질병을 일으킨다.",
           "일부 mtDNA 돌연변이는 심각한 질병을 일으킨다(LHON, MERRF).", "췌장 β세포의 미토 결함으로 당뇨가 생길 수 있다."]

CHECK = [
    ("01:00 질량작용비", "강의에선 “ATP와 ADP의 비”라고만 했지만 정의는 <b>[ATP] / ([ADP][Pᵢ])</b> (슬라이드 63)."),
    ("02:28 “ATP가 많으면 ATPase로”", "역주행이 일어나는 진짜 조건은 <b>양성자 구동력이 사라졌을 때</b>(저산소로 전자전달이 멈춤). ATP가 많다는 것만으로 거꾸로 돌진 않는다."),
    ("04:56 “유비퀴놀이 O₂에 전자를”", "교재 기준으로는 Complex I·III의 <b>반퀴논 라디칼(•Q⁻)</b>이 O₂에 전자 1개를 줘서 O₂•⁻가 생긴다. 시험엔 “Q 부근에서 새는 전자”로."),
    ("11:37 “P450 해독은 미토콘드리아에서”", "해독(약물 대사) P450은 주로 <b>간세포 소포체(ER)</b>에 있다. 미토콘드리아 P450의 대표 기능은 <b>부신의 스테로이드 합성</b>. 강의는 미토 단원 안에서 같이 소개한 것."),
    ("13:19 “NADPH → FADH₂ → 아드레노독신”", "FADH₂ 자체가 아니라 <b>FAD를 가진 아드레노독신 환원효소</b>(플래보단백질) → 아드레노독신(Fe-S) → P450 (슬라이드 76)."),
    ("22:02 세포내 공생설", "“우리 몸에 세균이 감염”이 아니라 <b>먼 옛날 원시 진핵세포</b>에 호기성 세균이 들어가 미토콘드리아가 된 것."),
    ("17:49 MERRF 우리말", "Myoclonic Epilepsy and Ragged-Red Fiber disease = 근간대성 간질(뇌전증) 및 누더기 적색 섬유병."),
]

# (시각, 제목, 영문 원문, 국문 해석) — 사용자가 준 녹취를 그대로 옮기되 국문의 오역 몇 곳만 바로잡음
BILINGUAL = [
    ("00:00–01:41", "ADP 가용성과 질량작용비",
     "Oxidative phosphorylation is regulated by the availability of ADP, which is the cellular energy needs, and we call this the acceptor control of respiration. This acceptor control ratio is generally larger than 10. … ADP is a substrate for ATP synthesis. … In the energy-requiring process, the use of ATP energy will decrease this mass action ratio, then the rate of respiration will be increased.",
     "산화적 인산화는 세포 에너지 요구량을 나타내는 ADP의 가용성으로 조절되며, 이를 호흡의 수용체 조절이라 한다. 수용체 조절비는 보통 10보다 크다. … ADP는 ATP 합성의 기질이다. … 에너지가 필요한 과정에서 ATP를 쓰면 질량작용비가 낮아지고 호흡 속도가 빨라진다."),
    ("01:42–02:27", "경로들의 통합 조절",
     "ATP-producing pathways are coordinately regulated by ATP and ADP ratio, NADH/NAD⁺ ratio, and citrate. … Oxidative phosphorylation will be stimulated by the ADP concentrations.",
     "ATP 생성 경로들은 ATP/ADP 비, NADH/NAD⁺ 비, 시트르산에 의해 협동적으로 조절된다. … 산화적 인산화는 ADP 농도로 촉진된다."),
    ("02:28–04:55", "IF₁",
     "Inhibitory protein IF₁ prevents ATP hydrolysis by ATP synthase. … When a cell is in a hypoxic condition, electron transfer slows down, ATP synthesis slows down, and we need to prevent ATP hydrolysis. … Pyruvate and lactate increase, pH decreases, IF₁ makes a dimer, which results in ATP hydrolysis inhibition. In aerobic condition pH increases, the IF₁ dimer is destabilized, and ATP synthesis is resumed.",
     "억제 단백질 IF₁은 ATP 합성효소에 의한 ATP 가수분해를 막는다. … 저산소에서는 전자전달과 ATP 합성이 느려지므로 ATP 가수분해를 막아야 한다. … 피루브산·젖산이 늘어 pH가 낮아지면 IF₁이 이량체를 만들어 가수분해를 억제한다. 산소가 충분해 pH가 오르면 이량체가 풀리고 ATP 합성이 재개된다."),
    ("04:56–07:17", "ROS",
     "Reactive oxygen species are generated during oxidative phosphorylation: superoxide radical, which can be transformed into hydroxyl radical or hydrogen peroxide. … By glutathione peroxidase and glutathione we regulate ROS. … Radiation, inflammation, metals and some drugs can also induce ROS.",
     "산화적 인산화 중 ROS가 생긴다: 초과산화물 라디칼과 이것이 바뀐 하이드록실 라디칼·과산화수소. … 글루타티온 과산화효소와 글루타티온으로 조절한다. … 방사선·염증·금속·일부 약물도 ROS를 유발한다."),
    ("07:18–08:52", "HIF-1",
     "In hypoxic cells, imbalance between input electrons and electron transfer increases ROS. HIF-1 is increased, glycolysis is upregulated, PDH is slowed down, so ROS production is reduced, and Complex IV is adapted to lower oxygen.",
     "저산소 세포에선 들어오는 전자와 전자전달의 불균형으로 ROS가 는다. HIF-1이 늘어 해당과정 ↑, PDH ↓ → ROS 생성 ↓, Complex IV는 낮은 산소에 적응한다."),
    ("08:53–11:36", "열발생",
     "In the infant, there are brown adipose tissues near the neck and back. … Thermogenin provides a path for proton flow, so the flow of protons produces heat instead of ATP.",
     "신생아 목·등 근처에 갈색지방조직이 있다. … thermogenin이 양성자 통로를 제공해 양성자 흐름이 ATP 대신 열을 만든다."),
    ("11:37–14:43", "P450",
     "Cytochrome P450 adds oxygen (oxygenation) to solubilize drug molecules for excretion, but sometimes generates more toxic molecules such as NAPQI. … Highly expressed CYP2E1 by alcohol … Mitochondria of adrenal glands are specialized for steroid synthesis. NADPH provides electrons → (adrenodoxin reductase) → adrenodoxin → P450 hydroxylase, which interacts directly with oxygen and makes an alcohol product.",
     "P450은 산소를 붙여 약물을 물에 잘 녹게 해 배설시키지만, 가끔 NAPQI 같은 더 독한 물질을 만든다. … 음주로 늘어난 CYP2E1 … 부신 미토콘드리아는 스테로이드 합성에 특화. NADPH의 전자 → 아드레노독신 환원효소 → 아드레노독신 → P450 수산화효소 → O₂와 직접 반응해 알코올(R–OH) 생성."),
    ("14:44–15:47", "세포자멸사",
     "Programmed cell death can be initiated by the releasing of cytochrome c from mitochondria … making apoptosome, which triggers activation of caspases.",
     "프로그램된 세포 죽음은 미토콘드리아의 시토크롬 c 방출로 시작될 수 있다 … 아폽토좀이 만들어져 카스페이스를 활성화한다."),
    ("15:48–18:56", "mtDNA · LHON · MERRF",
     "ND is NADH dehydrogenase (Complex I), cytochrome b is Complex III, cytochrome oxidase is Complex IV, plus ATP synthase genes, transfer RNAs, ribosomal RNAs and a control region. … LHON is a single base change in ND4 or cytochrome b, leading to blindness. MERRF is caused by mutation in lysyl-tRNA: muscular weakness and uncontrollable muscular jerking.",
     "ND = NADH 탈수소효소(Complex I), cyt b = Complex III, cyt oxidase = Complex IV, ATP 합성효소 유전자, 운반 RNA(tRNA), 리보솜 RNA, 조절 부위. … LHON은 ND4 또는 cyt b의 염기 하나 변화로 실명에 이른다. MERRF는 라이신 tRNA 돌연변이로 근력 약화와 통제 안 되는 근육 경련."),
    ("18:57–20:32", "모계 유전 · 이형세포질성",
     "Mitochondria in the sperm are destroyed after fertilization, so mitochondria are inherited exclusively from mother. … When cells divide, daughter cells have larger or smaller numbers of mutants — heteroplasmy.",
     "정자의 미토콘드리아는 수정 후 파괴되어 미토는 어머니에게서만 온다. … 분열 때 딸세포마다 돌연변이 미토 수가 달라진다 = 이형세포질성."),
    ("20:33–22:01", "β세포 · 당뇨",
     "Low production of ATP, which should block the potassium channel, which triggers opening of the calcium channel to stimulate insulin secretion. … Defect of mitochondria results in blocking of insulin secretion.",
     "ATP가 K⁺ 채널을 막아야 Ca²⁺ 채널이 열려 인슐린이 나오는데 ATP 생산이 적으면 분비가 줄어든다. … 미토 결함은 인슐린 분비를 막아 당뇨의 원인이 된다."),
    ("22:02–22:47", "세포내 공생설",
     "There is a similarity of mitochondria and bacteria, so there is a hypothesis of endosymbiotic origin of mitochondria.",
     "미토콘드리아와 세균이 닮아서, 미토콘드리아가 세포내 공생에서 왔다는 가설이 있다."),
]


def build():
    pts = "".join(f'<div class="box pt"><div><span class="tm">⏱ {tm}</span><span class="t">{i + 1}. {t}</span></div><div>{b}</div><div class="ref">📘 {r}</div></div>'
                  for i, (tm, t, b, r) in enumerate(POINTS))
    summ = "".join(f"<li>{s}</li>" for s in SUMMARY)
    bil = "".join(f'<tr><td class="tm">{a}<br><b>{b}</b></td><td style="font-family:\'Noto Serif\',serif;font-size:9pt">{c}</td><td style="font-size:9.2pt">{d}</td></tr>' for a, b, c, d in BILINGUAL)
    html = f"""<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>기말고사 대비 수업3 정리</title><style>{CSS}</style></head><body>
<h1>약품생화학 기말고사 대비 수업 ③ 정리 (동영상 강의)</h1>
<div class="sub">원본: 동영상 강의 영문 녹취 + 국문 해석 (24분) · 2026-11-01 정리 · 강의 슬라이드·요약노트와 대조</div>
<div class="meta"><span class="chip">범위: 19.3 조절 → 19.4 미토콘드리아의 다른 기능 → 19.5 미토 유전자 (슬라이드 약 62–89)</span><span class="chip">노트: Chap19_20 시험대비 요약노트(TB추가) p.74–100</span><span class="chip r">다음 진도: 광합성(슬라이드 90~)</span></div>
<div class="notice">영어 강의 · 소리가 깨끗하게 녹음되어 인식 누락 구간 없음. 마지막에 교수님이 직접 정리한 소단원 요약 6줄이 있음(아래 ✅).</div>

<h2>🎯 핵심 포인트 (시험 직결)</h2>
{pts}

<h2 class="g">✅ 교수님 소단원 요약 (22:48–24:11) — 슬라이드 89 그대로</h2>
<div class="box"><ol style="margin:0">{summ}</ol></div>

<h2 class="p">⚠️ 강의 말과 교재가 다른 곳 · 주의할 표현</h2>
{esc_table(CHECK, ["대목", "바로잡기"])}

<h2 class="o">📜 구간별 영문 원문 · 국문 해석 (요점 발췌)</h2>
<div class="small">전체 원문은 채팅으로 받은 녹취 그대로. 여기선 시험에 나올 문장 위주로 줄였고, 국문 해석의 어색한 곳(“전령이 아닌 운반 RNA” 등)은 바로잡았어.</div>
<table><tr><th style="width:15%">시각</th><th>English</th><th style="width:40%">국문</th></tr>{bil}</table>
</body></html>"""
    open(os.path.join(D, "index.html"), "w").write(html)


if __name__ == "__main__":
    build()
