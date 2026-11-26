# -*- coding: utf-8 -*-
"""CH25_2 강의자료(20쪽) = CH25_1 슬라이드 18장 + 새 슬라이드 19·20. 기존 번역을 그대로 가져와 번호만 새로."""
import re
from ch25_1 import PAGES as A
from ch25_2 import PAGES as B
from ch25_3 import PAGES as C

OLD = {p["slide"]: p for p in A + B + C}
# 새 번호 → CH25_1 번호
MAP = {2: 8, 3: 9, 4: 13, 5: 18, 6: 20, 7: 21, 8: 22, 9: 23, 10: 24, 11: 26, 12: 27, 13: 28, 14: 29, 15: 30, 16: 31, 17: 32, 18: 33}
INV = {o: n for n, o in MAP.items()}


def _ref(s):
    def one(m):
        o = int(m.group(1))
        return f"슬 {INV[o]}" if o in INV else f"CH25_1 슬 {o}"
    def rng(m):
        a, b = int(m.group(1)), int(m.group(2))
        if a in INV and b in INV:
            return f"슬 {INV[a]}–{INV[b]}"
        return f"CH25_1 슬 {a}–{b}"
    s = re.sub(r"슬 (\d+)–(\d+)", rng, s)
    return re.sub(r"슬 (\d+)(?![–\d])", one, s)


def _fix(p, n):
    q = dict(p, img=n, slide=n, src=f"원본 슬라이드 {n} (CH25_1 슬 {p['slide']})")
    for k in ("sum", "tr", "ex"):
        if k in q:
            q[k] = _ref(q[k])
    return q


COVER = dict(img=1, slide=1, src="표지", title="제25장 생체분자: 탄수화물 — CH25_2 강의 로드맵", sub="Chapter 25 · Biomolecules: Carbohydrates",
kw=["피셔·하스 투영", "D/L", "피라노스", "단당류 반응", "글리코사이드", "환원·산화", "사슬 늘이기·줄이기", "필수 단당류"],
sum="CH25_2는 25장에서 <b>단당류</b> 부분만 골라 정리한 강의자료(20쪽). 피셔·하스 투영 → D/L → 고리형(피라노스) → 단당류의 반응 → 필수 단당류 구조까지.",
tr="""<p><b>제25장 생체분자: 탄수화물</b></p>
<p class="note">영문 원제: Chapter 25 · Biomolecules: Carbohydrates — 표지 슬라이드라 문장은 제목뿐이야.</p>
<p><b>용어 먼저</b></p>
<ul><li><b>단당류(monosaccharide)</b>: 더 작은 당으로 가수분해되지 않는 당 (포도당·과당).</li>
<li><b>알도스 / 케토스</b>: 알데하이드(–CHO)를 가진 당 / 케톤(C=O)을 가진 당.</li>
<li><b>헤미아세탈 · 아세탈</b>: 알데하이드 + 알코올 1개 / 2개 (19장). 당의 고리 = 분자 내 헤미아세탈.</li></ul>""",
ex="""<table class="t"><tr><th>주제</th><th>슬라이드</th><th>핵심</th></tr>
<tr><td>입체화학 표현</td><td>2–4</td><td>피셔 투영 확인, 하스 투영, D/L</td></tr>
<tr><td>고리 구조</td><td>5</td><td>포도당 피라노스 (α/β 아노머)</td></tr>
<tr><td>단당류 반응</td><td>6–17</td><td>에스터·에터, 글리코사이드, 쾨니히스-크노르, 환원(알디톨), 산화(알돈산·알다르산·우론산), 환원당, 킬리아니-피셔, 볼 분해</td></tr>
<tr><td>필수 단당류</td><td>18–20</td><td>8가지 필수 단당류, 포도당 기준 차이(갈락토스 C4·만노스 C2·푸코스·자일로스), 9가지 당 기호</td></tr></table>
<p class="note">CH25_1(51쪽)에서 빠진 부분: 탄수화물 분류·명명, 피셔 R/S 예제, 아노머 비율, 퓨라노스, 이당류·다당류, 데옥시당·아미노당, 인플루엔자.</p>""")

S19 = dict(img=19, slide=19, src="원본 슬라이드 19 (새 슬라이드)", title="필수 단당류 비교 — 포도당 기준으로 어디가 다른가", sub="Glucose · Galactose · Mannose · Fucose · Xylose",
kw=["갈락토스 = C4 에피머", "만노스 = C2 에피머", "푸코스 = 6-데옥시-갈락토스 (L)", "자일로스 = C5 알도스 (CH₂OH 없음)"],
sum="포도당(D-글루코스)을 기준으로 피셔 투영에서 <b>빨간 상자</b>만 다르다: 갈락토스는 C4–OH, 만노스는 C2–OH가 반대쪽, 푸코스는 6번 탄소가 CH₃(데옥시), 자일로스는 탄소 하나 적은 5탄당. 아래 줄은 각 당의 의자형(물결선 = α·β 둘 다).",
tr="""<p class="note">그림 (위): 의자형 β-피라노스 · 가운데: 피셔 투영 · 아래: 의자형 (물결선 OH = α 또는 β)</p>
<ul><li><b>Glucose</b> 포도당</li>
<li><b>Galactose</b> 갈락토스 — 빨간 상자: C4의 HO가 왼쪽</li>
<li><b>Mannose</b> 만노스 — 빨간 상자: C2의 HO가 왼쪽</li>
<li><b>Fucose (6-deoxy-galactose)</b> 푸코스 (6-데옥시-갈락토스) — C6이 CH₃</li>
<li><b>Xylose</b> 자일로스 — 빨간 상자: CH₂OH(C6) 자리가 비어 있음 (5탄당)</li></ul>
<p class="note">피셔 투영의 분홍 O = C1 카르보닐(고리에서 아노머 OH가 됨), 초록 OH = 고리를 만드는 C5–OH.</p>""",
ex="""<table class="t"><tr><th>당</th><th>포도당과 차이</th><th>의자형에서</th></tr>
<tr><td>갈락토스</td><td>C4 에피머</td><td>C4–OH가 <b>위(액시얼)</b></td></tr>
<tr><td>만노스</td><td>C2 에피머</td><td>C2–OH가 <b>위(액시얼)</b></td></tr>
<tr><td>푸코스</td><td>6-데옥시 + <b>L</b>형 갈락토스</td><td>C5에 CH₃, 고리가 뒤집혀 그려짐</td></tr>
<tr><td>자일로스</td><td>C6 없음 (알도펜토스)</td><td>C5에 치환기 없음 (CH₂)</td></tr></table>
<p>외우는 법: 포도당 의자형은 <b>모든 치환기가 에쿼토리얼</b>(β). 다른 당은 “어느 OH 하나가 위로 섰나”만 보면 된다.</p>
<div class="box"><span class="tag">시험형</span>피셔 ↔ 의자형 변환: 피셔에서 <b>오른쪽 OH = 하스·의자형에서 아래</b>, 왼쪽 = 위.</div>""")

S20 = dict(img=20, slide=20, src="원본 슬라이드 20 (새 슬라이드)", title="자주 나오는 단당류 9가지 — 구조와 기호", sub="Structures and symbols of the nine commonly found monosaccharides (Kanie et al. 2017)",
kw=["GlcNAc ■ 파랑", "Glc ● 파랑", "Man ● 초록", "GlcU ◆", "Sia ◆ 보라", "GalNAc ■ 노랑", "Gal ● 노랑", "Xyl ★", "Fuc ▲ 빨강"],
sum="당사슬(글리칸) 그림에서 쓰는 9가지 단당류와 기호. <b>색 = 당의 종류</b>(파랑 포도당 계열, 초록 만노스, 노랑 갈락토스 계열), <b>모양 = 변형</b>(● 그냥 당, ■ N-아세틸아미노당, ◆ 산). 아래: 단당류 → 이당류 → 다당류(가지 친 사슬).",
tr="""<p>흔히 발견되는 9가지 단당류의 구조와 기호</p>
<ul><li><b>N-아세틸-D-글루코사민</b> (GlcNAc) ■ · <b>D-포도당</b> (Glc) ● · <b>D-만노스</b> (Man) ● · <b>D-글루쿠론산</b> (GlcU) ◆ · <b>N-아세틸시알산</b> (Sia) ◆</li>
<li><b>N-아세틸-D-갈락토사민</b> (GalNAc) ■ · <b>D-갈락토스</b> (Gal) ● · <b>D-자일로스</b> (Xyl) ★ · <b>L-푸코스</b> (Fuc) ▲</li>
<li>아래 그림: 단당류(Monosaccharide) · 이당류(Disaccharide) · 다당류(Polysaccharide)</li></ul>
<p class="note">출처: Kanie et al., Biochemical Compounds 2017</p>""",
ex="""<ul><li><b>NHAc</b> = –NH–C(=O)CH₃ (C2의 OH 대신) → 아미노당. GlcNAc는 키틴·당단백질의 기본 단위.</li>
<li><b>글루쿠론산</b> = 포도당 C6이 –COOH (<b>우론산</b>, 슬 15). 간에서 약물 글루쿠론산 포합(배설).</li>
<li><b>시알산</b> = 9탄당 산, 세포 표면 당사슬의 끝 → 인플루엔자 바이러스가 붙는 자리 (뉴라미니데이스가 자름, 타미플루 표적).</li>
<li><b>L-푸코스</b>: 자연에 드문 L-당. 혈액형 항원(ABO)의 끝 당.</li></ul>
<div class="box"><span class="tag">약학</span>당단백질 약(항체·EPO)의 당사슬 구조를 이 기호로 표시한다.</div>""")

PAGES = [COVER] + [_fix(OLD[o], n) for n, o in sorted(MAP.items())] + [S19, S20]
