# -*- coding: utf-8 -*-
"""CH22 기말대비 TOP 10판 — 출제 확률 순서대로 10문제(+1)만.
문제마다: ① 문제 + 메모 + 이 문제에 필요한 개념(핵심·메커니즘)  ② 정답과 해설(풀이·원서 해설 그림)  ③ 삼성노트 내 필기
앞: TOP 10 한눈에 + 기초 1쪽 / 뒤: 시약 치트시트 · 혼동 쌍.
ED=top10 python3 build.py && node render.js ../../CH22_기말대비_TOP10판.pdf"""
import re

# (순위, 문제 번호, 등급, 왜 나오나, 필요한 개념 id, 메커니즘을 보여 줄 개념 id)
RANK = [
    ("1위", 27, 1, "a(β-케토 에스터 위치 지정 알킬화) → b(가열 탈카르복실화) → c(LDA 한산한 쪽 알킬화) 3단 콤보 — 22장 최종 보스", ["c-aae", "c-decarb", "c-lda"], "c-lda"),
    ("2위", 20, 1, "탈카르복실화 · 다이케톤 알킬화 · HVZ 물 전/후 · 할로폼 CHI₃ — 핵심 반응 4개를 한 판에", ["c-decarb", "c-alk", "c-hvz", "c-haloform"], "c-haloform"),
    ("3위", 13, 1, "에탄올(16) > 아세톤(19) 순서 역전 함정 + CCl₃COOH 유발 효과 — 산 세기 문제의 정석", ["c-pka"], "c-pka"),
    ("4위", 12, 1, "(c) 알코올 –OH와 삼중결합 건너편 –CH₃ 공명 함정 — 출제율 99% (01·02·08·09가 같이 풀림)", ["c-pka", "c-acid"], "c-pka"),
    ("5위", 7, 2, "교수님이 “거꾸로 가보라”며 칠판에 직접 푼 의약품 빈칸 1호 — 빈칸 3개 + S<sub>N</sub>2 화살표", ["c-bup", "c-acidbr"], "c-bup"),
    ("6위", 28, 2, "왜 Ph–Br을 못 쓰나(서술형) + 빈칸 3개 + 요소 고리 닫기 화살표 — 의약품 빈칸 2호", ["c-phb", "c-alk"], "c-phb"),
    ("7위", 23, 2, "알킬화 3대 제약(아릴 할라이드 ×, 탄소 3개 골격, 산성 H 2개) — 15·18이 같이 풀림", ["c-aae", "c-alk"], "c-aae"),
    ("8위", 14, 3, "짝산 pK<sub>a</sub> 시소 법칙 — 언제 NaOEt, 언제 LDA", ["c-acid", "c-pka"], "c-acid"),
    ("9위", 6, 3, "HVZ 마지막에 물 대신 메탄올 → 에스터 — 메커니즘 그리기로 내기 좋음", ["c-hvz"], "c-hvz"),
    ("10위", 26, 3, "LDA 직접 알킬화 ‘가지치기’ — 역합성 설계", ["c-lda"], "c-lda"),
    ("10위", 24, 3, "Br(CH₂)₄Br로 5각형 고리 — N각형 = 염기 2배 + (N−1)개 양끝 브로민화물", ["c-mal", "c-aae"], "c-mal"),
]
BASIC = ["c-taut", "c-enolrx", "c-acidbr", "c-e2"]
GRADE = {1: ("🥇 1등급", "#e89b1c"), 2: ("🥈 2등급", "#1d5fc4"), 3: ("🥉 3등급", "#2b8a3e")}


def build(G):
    E = G["ENTRIES"]; _hd21 = G["_hd21"]; foot = G["foot"]; _qv = G["_qv"]; NOTE = G["_NOTE"]
    C = {e["id"]: e for e in E if e["t"] == "c" and e.get("id")}
    Q = {e["n"]: e for e in E if e["t"] == "q" and e.get("n")}
    pages, QP = [], {}

    def ccard(cid, mech=False):
        c = C[cid]
        m = ""
        if mech and c.get("mech"):
            m = f'<div class="afig cm"><div class="mz">{c["mech"]}</div></div>'
        elif mech:  # 메커니즘이 없는 개념은 강의 슬라이드
            im = next((x for x in c.get("side", []) if x[0] == "img"), None)
            if im: m = f'<div class="cimg"><img src="{G["IMG"]}{im[1]}.jpg"><div class="cap">{im[2]}</div></div>'

        return f'<div class="ccd"><div class="cct">📚 {c["title"]}</div><div class="ccr">💡 {c["core"]}</div><div class="cco">🧠 {c["one"]}</div>{m}</div>'

    # 1쪽 — TOP 10 한눈에 (마스터요약 최종 ③과 같은 내용, 쪽 번호만 이 판 기준)
    top = G["TOP10"].replace(" 왼쪽)", ")").replace(" 오른쪽)", ")").replace("최종</span><b>③", "TOP</span><b>10")
    pages.append(None)  # 쪽 번호가 정해진 뒤에 채움

    # 2쪽 — 기초 1쪽
    cards = "".join(ccard(c, True) for c in BASIC)
    pages.append(f'''<section class="page v21 t10b">
{_hd21("기초", "기초 1쪽 — TOP 10에 직접 안 나오지만 바탕이 되는 개념", "토토머화 · 엔올 반응 일반 틀 · 산성 할로젠화 · E2 탈브로민화수소", ["22장 기초"], "TOP 10")}
<div class="bgrid">{cards}</div>
{foot(len(pages) + 1)}</section>''')

    for rk, n, gd, why, cids, mid in RANK:
        e = Q[n]; g, col = GRADE[gd]
        prob, memo, _ = _qv(dict(e, n=-1), n, mini=True)
        _, _, ans = _qv(dict(e, n=-1), n, mini=True)
        concepts = "".join(ccard(c, c == mid) for c in cids)
        i = len(pages) + 1; QP[n] = i
        pages.append(f'''<section class="page v21 t10a">
{_hd21(rk, f"문제 {n:02d} · {e['title']}", why, [g, e["part"]], "TOP")}
{prob}{memo}
<div class="cbx"><div class="cbl">이 문제에 필요한 개념 (개념 쪽 핵심 + 메커니즘)</div><div class="cgrid n{len(cids)}">{concepts}</div></div>
<div class="nextp">정답과 해설은 다음 쪽 →</div>
{foot(i)}</section>''')
        pages.append(f'''<section class="page v21 aonly">
{_hd21(rk, f"문제 {n:02d} · {e['title']} — 정답과 해설", e.get("src", ""), [g, e["part"]], "TOP")}
{ans}
{'<div class="nextp">✍ 내 필기(삼성노트)는 다음 쪽 →</div>' if n in NOTE else ""}
{foot(len(pages) + 1)}</section>''')
        if n in NOTE:
            pages.append(G["notepage"](len(pages) + 1, e).replace(f'<b>{n:02d}</b>', f'<b>{rk}</b>').replace('<span>문제</span>', '<span>TOP</span>'))

    # 뒤 — 시약 치트시트 · 혼동 쌍 (개념 번호 대신 TOP 순위로 안내)
    first = {}
    for rk, n, gd, why, cids, mid in RANK:
        for c in cids:
            first.setdefault(c, rk)
    first.update({c: "기초" for c in BASIC if c not in first})
    for fid in ("f-reag", "f-pairs"):
        f = next(x for x in E if x.get("id") == fid)
        h = re.sub(r"\{CN:([a-z0-9-]+)\}", lambda m: first.get(m.group(1), "기초"), f["html"])
        h = h.replace("{QN:q-2254}", "27").replace("<th>개념</th>", "<th>어디서</th>")
        pages.append(f'<section class="page {f.get("cls", "")}">{h}{foot(len(pages) + 1)}</section>')

    top = re.sub(r"\{QP:(\d+)\}", lambda m: str(QP[int(m.group(1))]), top)
    pages[0] = f'<section class="page top10">{top}{foot(1)}</section>'
    return pages
