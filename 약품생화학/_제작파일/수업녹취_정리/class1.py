"""기말고사 대비 수업1 녹취록 정리 → index.html (A4 세로)
python3 class1.py && NODE_PATH=$(npm root -g) node render.js "$PWD/out.pdf"
"""
import os

D = os.path.dirname(os.path.abspath(__file__))


POINTS = [
    ("14:39–15:22", "NADH vs FADH₂ — 출발점이 다르면 효율이 다르다",
     "NADH는 Complex I에서 들어와 H⁺ <b>4 + 4 + 2 = 10개</b>, FADH₂는 Complex II에서 들어와 <b>4 + 2 = 6개</b>(약 5분의 3). 그래서 <b>NADH ≈ 2.5 ATP, FADH₂ ≈ 1.5 ATP</b>.",
     "개념 08 (p.16)"),
    ("18:58–19:50", "영상 숫자는 틀렸다 — “4 + 4 + 2, 전자 2개당”으로 외워라",
     "수업 영상의 양성자 개수는 틀렸다고 직접 짚으심. Complex IV는 전자 4개 + H⁺ 8개가 들어가 <b>4개는 밖으로 펌프, 4개는 물 만드는 데</b> 쓰인다(이건 맞음). 기준은 <b>NADH 1개 = 전자 2개</b>.",
     "개념 07 (p.15) · 기출 19-7 (p.31)"),
    ("35:11–35:31", "Complex IV는 전자 1개당 H⁺ 1개",
     "전자 4개가 들어올 때 4개 펌프 → 전자 2개(NADH 1개)로 환산하면 <b>2개</b>. 그래서 4, 4, 2.",
     "개념 07 (p.15)"),
    ("46:23–47:38", "순서 정하는 방법 세 가지 중 <b>3번(억제제)이 중요</b>",
     "① 환원전위(마이너스로 클수록 전자를 잘 준다 = 높은 에너지) ② 산화 속도 ③ <b>억제제</b>: 막은 곳 앞에 물질이 쌓인다(환원). 사이안화물·일산화탄소 = Complex IV(시토크롬 산화효소) 억제, 치명적 독.",
     "개념 10 (p.18) · 기출 19-4 (p.28)"),
    ("26:09–27:30", "유비퀴논 = 기름에 녹는 작은 보트",
     "머리(퀴논) + 꼬리(아이소프렌 단위 약 10개, 불포화 탄화수소) → <b>지용성</b>. 전자를 받으면 C=O가 OH가 되며 H⁺ 2개를 함께 집어 듦(유비퀴놀, “알코올이 됐다”). 막 속을 자유롭게 떠다니며 큰 배(복합체)에서 큰 배로 옮겨 주는 보트.",
     "개념 03 (p.11)"),
    ("38:38–39:26", "P쪽 · N쪽과 양성자 구동력",
     "<b>N쪽 = 기질(matrix)</b>, <b>P쪽 = 막사이공간(외막과 내막 사이)</b>. ΔG는 농도 차뿐 아니라 <b>전하 차</b>로도 생긴다 → 합쳐서 양성자 구동력. ATP 합성효소 = 물레방아.",
     "개념 09 (p.17)"),
    ("23:22–25:58", "Complex I의 양성자 펌프 원리는 <b>가설</b>",
     "알려진 사실은 3D 구조(나선 구조, 철-황 클러스터가 전자 경로, 유비퀴논 환원 자리). 유비퀴논 환원 자리에서 시작된 구조 변화가 옆 나선으로 전달되고, 막 가운데 줄지은 산성 잔기(글루탐산·아스파르트산)와 염기성 잔기(히스티딘 등)가 H⁺를 주고받는다는 <b>설명은 가설</b>.",
     "개념 04 (p.12)"),
]

TIMELINE = [
    ("00:00–06:23", "서두 · 경계인 이야기",
     "AI 시대에는 여러 분야의 경계에서 판단하는 ‘경계인’이 중요하다. 약학은 생물·화학·물리·물리화학이 융합된 학문이라 사고가 유연하다(교수님 경력: 제약회사·정부출연연구소·대학). 필요한 것: 자기 탐구, 메타인지 적응력, 리스크 테이킹, 생성적 혁신(Generative Innovation).", ""),
    ("06:43", "📢 공지", "<b>중간고사 결과는 아직 채점을 받지 못해 다음 주쯤</b> 알려 주실 예정.", ""),
    ("07:10–09:42", "전자전달계 = 배터리",
     "배터리 음극에서 전자가 나가 일을 하고 양극으로 들어가는 것과 비슷. 전자를 내놓는 물질 = <b>NADH, FADH₂</b>, 최종 전자 수용체 = <b>O₂</b> → 전자를 받아 <b>물</b>. 숨 쉴 때 산소가 필요한 이유. 중간 운반체는 중간 에너지 상태 → 에너지 차이로 H⁺ 펌프.", "p.9"),
    ("10:07–11:27", "어디서? 미토콘드리아 <b>내막</b>",
     "꼬불꼬불한 내막(크리스타)에 전자전달 분자들이 박혀 있다. Complex 1·2·3·4를 지나며 생긴 에너지 차로 H⁺를 펌프 → 양성자 기울기.", "p.5 확대 그림"),
    ("11:27–13:54", "네 복합체 이름과 펌프 수",
     "I = NADH 탈수소효소, II = 숙신산 탈수소효소, III = 시토크롬 bc₁, IV = 시토크롬 산화효소. <b>I에서 4개, III에서 4개, IV에서 2개</b>를 P쪽으로. 막사이공간의 H⁺ 농도가 훨씬 높아진다.", "p.16"),
    ("14:14–15:22", "NADH vs FADH₂", "위 강조 포인트 ① 참고 (10개 vs 6개 → 2.5 vs 1.5 ATP).", "p.16"),
    ("15:43–18:29", "영상 시청 (전자전달·ATP 합성 애니메이션)", "영어 영상 소리라 인식이 대부분 깨짐.", ""),
    ("18:58–19:50", "영상 숫자 정정", "위 강조 포인트 ② 참고.", "p.15"),
    ("19:50–21:28", "Complex I = NADH:유비퀴논 산화환원효소",
     "유비퀴논이 전자와 수소를 받아 유비퀴놀(카보닐기 C=O → 알코올기 OH). 철-황 중심들이 전깃줄처럼 줄지어 전자를 흘려보냄.", "p.12"),
    ("21:53–25:58", "Complex I 3D 구조와 펌프 가설",
     "그림의 막 부분은 앞 그림을 뒤집어 놓은 것(한쪽이 기질, 한쪽이 막사이공간). 위 강조 포인트 ⑦ 참고.", "p.12"),
    ("26:09–27:30", "유비퀴논 구조", "위 강조 포인트 ⑤ 참고.", "p.11"),
    ("28:00–29:35", "Complex II와 Q로 들어오는 다른 입구",
     "숙신산 탈수소효소 → FAD → 코엔자임 Q. 전자를 넘겨 줘 <b>ROS가 생기는 것을 막아 준다</b>. Q로 전자를 주는 것: Complex I·II + <b>글리세롤 3-인산 탈수소효소</b>(해당과정 쪽 물질) + <b>ETF-Q 산화환원효소</b>(지방산 쪽).", "p.13"),
    ("29:35–31:51", "Complex III와 Q 회로",
     "철-황 + 헴(포르피린 가운데 철) 여러 개. 유비퀴놀의 전자 2개 중 <b>하나는 시토크롬 c로</b>, <b>하나는 유비퀴논을 다시 만드는 데</b>. 결과적으로 H⁺ <b>4개를 밖으로</b>, 기질에서 <b>2개를 받아들임</b>.", "p.14"),
    ("32:14–33:32", "시토크롬",
     "포르피린 고리 가운데 철, 헴과 아주 비슷. 식물에선 엽록체에 시토크롬이 많다. 시토크롬 c는 산화형(전자를 잃은 상태)·환원형(받은 상태)에 따라 흡수 스펙트럼이 다르다.", "p.11"),
    ("33:56–35:31", "Complex IV",
     "<b>철뿐 아니라 구리도 먹어야 한다</b>(구리가 필요한 효소). 헴 a·a₃와 구리 중심을 거쳐 O₂ → 물. 위 강조 포인트 ③ 참고.", "p.15"),
    ("35:55–37:22", "짝 설명 시간", "옆 사람에게 여기까지 설명해 보기 (잡담 구간).", ""),
    ("37:22–38:14", "호흡초복합체 (respirasome)",
     "Complex III와 IV가 막에서 같이 묶여 있다: 가운데 bc₁, 양옆에 시토크롬 산화효소 → 시토크롬 c를 넘겨주기 쉬움(“우주선처럼 생겼다”).", "p.16"),
    ("38:14–40:17", "양성자 구동력 · 화학삼투 모델", "위 강조 포인트 ⑥ 참고. 화학삼투 모델(chemiosmotic model) — “우리말이 더 어렵다”.", "p.17"),
    ("40:17–41:06", "미토콘드리아 구조",
     "내막에 Complex I–IV, ATP 합성효소 등 단백질 복합체가 박혀 있다(그림의 점들). 기질에는 <b>해당과정을 제외한</b>(TCA 회로부터 전자전달까지) 연료 산화가 다 있다.", "p.17"),
    ("41:06–45:13", "어떻게 연구했나 — 미토콘드리아 분리",
     "세포 파쇄(초음파 sonication, 압력 차) → 원심분리(고속 원심분리기 ~15,000 rpm으로 세포 잔해와 상층액 분리) → <b>수크로스 농도 기울기</b>로 가라앉는 속도 차이 이용, 중간층의 미토콘드리아만 빼냄(어려운 기술) → <b>디지토닌</b>(세제)으로 막을 깸 → <b>이온교환 크로마토그래피</b>(전하 차)로 복합체 분리. 같이 붙은 단백질(예: III의 cyt b·c₁)은 같이 나옴. 분리한 분획에 NADH를 넣으면 Q가 나오는 게 Complex I, 숙신산을 넣으면 Q가 나오는 게 Complex II.", "p.18"),
    ("45:20–48:14", "운반체 순서 정하기", "위 강조 포인트 ④ 참고. 끝부분(47:38~)은 문장이 끊겨 원본 확인 필요.", "p.18"),
]

FIX = [
    ("LADH", "NADH"), ("비토콘 / 뇌막", "미토콘드리아 / 내막"), ("이너맨 브레인", "inner membrane (내막)"),
    ("플렉스 1, 2, 3, 4 / 콤플렉스", "Complex I–IV"), ("포톤을 펌핑", "프로톤(H⁺)을 펌핑"),
    ("프라톤 그래넌트", "proton gradient (양성자 기울기)"), ("NADHT Hydrogenase", "NADH dehydrogenase"),
    ("세 번째는 석진화idrogenase", "세 번째는 cytochrome bc₁ (오인식)"), ("석진화id… / 수신화에드 데이도로전ase", "succinate dehydrogenase (숙신산 탈수소효소)"),
    ("유비 키논 / 유비킨온 / 유퀴논", "ubiquinone (유비퀴논)"), ("아이온 설펄 / 아이언설퍼", "iron-sulfur (철-황)"),
    ("SSD / SED / SDP 레지듀", "acidic residue (산성 잔기)"), ("블루타메이트, 아스플라테이트 히스트", "glutamate, aspartate (+ histidine)"),
    ("아이소프렛 유닛", "isoprene unit (아이소프렌 단위)"), ("liquid soluble", "lipid soluble (지용성)"),
    ("글리세롤 3-phphate", "glycerol 3-phosphate"), ("ETF-Q, Oxidal Resultated", "ETF:Q oxidoreductase"),
    ("Cytochloropisum Complex", "cytochrome bc₁ complex"), ("Hym group / 힘 AA3", "heme group / 헴 a·a₃"),
    ("폴피린 / 포필인", "porphyrin (포르피린)"), ("커프 / 커플 센터", "Cu (구리) 센터"),
    ("사이토크롬 옥시저 잇새 / 옥시대이지", "cytochrome oxidase"), ("프로토모티브로스 / 프로톤 모티폴스", "proton-motive force"),
    ("ITP 신세이즈 / ATP 센세사이저", "ATP synthase"), ("키미 아스모틱 모델 / 화학, 산투학", "chemiosmotic model / 화학삼투"),
    ("섭셀렐라 오가 / 섭셀류러 오바너", "subcellular organelle (세포소기관)"), ("울트라 세트리프지 / 하이스피드 세트리프지", "ultracentrifuge / high-speed centrifuge"),
    ("셀 데구리 / 셀 데브리, 슈퍼네이턴트", "cell debris (세포 잔해), supernatant (상층액)"), ("스크로스", "sucrose (수크로스)"),
    ("디지토닌을 디터젼트", "digitonin (세제, detergent)"), ("아이온 익스체인지 크로마토그래피", "ion-exchange chromatography"),
    ("콤플렉스 마리", "Complex I"), ("Subtinate", "succinate"), ("리덥션 / 이덕션 포텐셜", "reduction potential (환원전위)"),
    ("이니비터", "inhibitor (억제제)"), ("사이아나이드", "cyanide (사이안화물)"), ("카본 모녹사이드", "carbon monoxide (일산화탄소)"),
]

CHECK = [
    ("00:02, 16:07, 17:23, 18:11", "음량이 낮아 인식 실패 (16–18분대는 영상 소리)."),
    ("12:19–13:01", "영어·한국어가 섞여 문장이 반복됨 — 내용은 “I에서 4개, III에서 4개, IV에서 2개 → P쪽 H⁺ 농도 ↑”."),
    ("36:15–36:57", "학생 잡담이 녹음됨 (“리뷰만 하겠지?” 등) — 수업 내용 아님."),
    ("47:38–48:14", "“옛날 일본 지하철 사린가스 …” 대목에서 문장이 끊김. <b>사린은 아세틸콜린에스테레이스 억제제(신경가스)</b>라 전자전달계 억제제가 아니다. 교수님이 무엇과 비교하신 건지 원본 음성으로 확인 필요."),
]


def esc_table(rows, head):
    th = "".join(f"<th>{h}</th>" for h in head)
    return f'<table><tr>{th}</tr>' + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows) + "</table>"


CSS = """
@page { size: A4; margin: 14mm 13mm 14mm 13mm; }
body { font-family: 'Noto Sans KR', sans-serif; color: #2c3038; font-size: 10.6pt; line-height: 1.65; margin: 0; word-break: keep-all; }
h1 { font-size: 21pt; margin: 0 0 2px 0; color: #23263a; }
.sub { color: #6c7280; font-size: 10pt; margin-bottom: 10px; }
.meta { display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 12px; }
.chip { background: #eef0fd; color: #4651c8; border-radius: 12px; padding: 2px 10px; font-weight: 700; font-size: 9.5pt; }
.chip.r { background: #fde9ef; color: #a3264f; }
h2 { font-size: 13.5pt; color: #fff; background: #4651c8; border-radius: 8px; padding: 4px 12px; margin: 16px 0 8px 0; break-after: avoid; }
h2.g { background: #127a64; } h2.o { background: #c2410c; } h2.p { background: #6a3d9a; }
.box { border: 1px solid #e4dfd3; border-radius: 10px; padding: 8px 12px; margin: 6px 0; break-inside: avoid; background: #fff; }
.pt { border-left: 5px solid #e03131; background: #fff6f6; }
.pt .t { font-weight: 800; color: #a3264f; } .pt .tm { color: #6c7280; font-size: 9pt; margin-right: 6px; }
.pt .ref { color: #127a64; font-size: 9pt; font-weight: 700; }
table { border-collapse: collapse; width: 100%; font-size: 9.6pt; margin: 4px 0; }
th { background: #eef0f8; color: #2f3a8f; text-align: left; }
th, td { border: 1px solid #dcdfe8; padding: 4px 7px; vertical-align: top; }
tr { break-inside: avoid; }
td.tm { white-space: nowrap; color: #6c7280; font-size: 9pt; }
.notice { background: #fff4cc; border: 1px solid #efd27a; border-radius: 10px; padding: 8px 12px; font-weight: 700; }
.small { color: #6c7280; font-size: 9pt; }
"""


def build():
    pts = "".join(f'<div class="box pt"><div><span class="tm">⏱ {tm}</span><span class="t">{i + 1}. {t}</span></div><div>{b}</div><div class="ref">📘 {r}</div></div>'
                  for i, (tm, t, b, r) in enumerate(POINTS))
    tl = "".join(f'<tr><td class="tm">{a}</td><td><b>{b}</b><br>{c}</td><td class="tm">{d}</td></tr>' for a, b, c, d in TIMELINE)
    html = f"""<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>기말고사 대비 수업1 정리</title><style>{CSS}</style></head><body>
<h1>약품생화학 기말고사 대비 수업 ① 정리</h1>
<div class="sub">원본: 기말고사 대비 수업1 음성 녹취록.pdf (자동 녹취, 48분 25초) · 2026-10-27 수업 · 오인식을 바로잡아 다시 정리</div>
<div class="meta"><span class="chip">범위: 19.1 전자전달 사슬 (슬라이드 약 4–35)</span><span class="chip">노트: Chap19_20 시험대비 요약노트(TB추가) p.9–18</span><span class="chip r">다음 진도: 셔틀(슬라이드 37~)부터</span></div>
<div class="notice">📢 공지 (06:43) — 중간고사 결과는 아직 채점을 받지 못해 <u>다음 주쯤</u> 알려 주신다고 함.</div>

<h2>🎯 교수님이 콕 집은 포인트 (시험 직결)</h2>
{pts}

<h2 class="g">⏱ 시간대별 정리</h2>
<table><tr><th style="width:15%">시각</th><th>내용 (오인식 교정)</th><th style="width:12%">노트</th></tr>{tl}</table>

<h2 class="o">🔧 음성 인식 오류 교정표</h2>
<div class="small">녹취록에서 이상하게 적힌 말 → 실제로 하신 말. 녹취록을 읽을 때 옆에 두고 보면 돼.</div>
{esc_table(FIX, ["녹취록에 적힌 말", "실제 용어"])}

<h2 class="p">🎧 원본 음성으로 확인할 곳</h2>
{esc_table(CHECK, ["시각", "이유"])}
</body></html>"""
    open(os.path.join(D, "index.html"), "w").write(html)


if __name__ == "__main__":
    build()
