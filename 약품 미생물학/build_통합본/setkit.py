# -*- coding: utf-8 -*-
"""편별 기말 학습자료 공통 부품 (항생제 1편부터 사용)
- SS(): 요약 페이지 + 페이지별 셀프테스트
- SET(): 세트 문제 등록 (보기 11개, 'img:파일명'이면 구조식 그림 보기)
- render_sets(): 세트별 문제 → 해설 페이지
- study_page(), cover_page(): 공부법·표지"""
from core import RAW, S, SEC, card, ul, PAGES, MARKS, exp_html

CIR = MARKS["circle"]


class Kit:
    def __init__(self, part, imgdir=""):
        self.P = part
        self.imgdir = imgdir
        self.SETS = []
        self.SELFTEST = {}
        self.SUMMARY = []   # (kicker, title, body) — 퀴즈 HTML 생성용

    # ---------------- 요약
    def SS(self, kicker, title, body, sub=""):
        self.SUMMARY.append((kicker, title, body))
        qs = self.SELFTEST.get(title)
        if qs:
            lis = "".join(f'<li><b class="qn">Q{i}</b> {q}</li>' for i, q in enumerate(qs, 1))
            body += (f'<div class="selftest"><span class="stlabel">✋ 위 가리고 답하기</span>'
                     f'<ul class="stq">{lis}</ul></div>')
        S(self.P, kicker, title, body, sub)

    def fig(self, name, cap, h=26):
        return (f'<figure class="sfig"><img src="img/{self.imgdir}/{name}.png" style="height:calc({h}mm * var(--s,1))">'
                f'<figcaption>{cap}</figcaption></figure>')

    def figs(self, items, h=26):
        return '<div class="sfigs">' + "".join(self.fig(n, c, h) for n, c in items) + '</div>'

    # ---------------- 세트
    def SET(self, title, box, qs, cols=2):
        assert len(box) == 11, title
        self.SETS.append(dict(title=title, box=box, qs=qs, cols=cols))

    def _boxitem(self, t):
        if t.startswith("img:"):
            return f'<img src="img/{self.imgdir}/{t[4:]}.png">'
        return t

    def render_sets(self, sec_title="실전 세트 — 문제와 해설 (보기 11개 · 개수 지정)"):
        SEC("실전 세트 (문제+해설)", sec_title)
        for si, s in enumerate(self.SETS, 1):
            isimg = s["box"][0].startswith("img:")
            boxli = "".join(f'<li><span class="mk">{CIR[k]}</span><span>{self._boxitem(t)}</span></li>'
                            for k, t in enumerate(s["box"]))
            items = ""
            for qi, q in enumerate(s["qs"], 1):
                items += (f'<div class="setitem"><div class="setq">'
                          f'<span class="num">{qi}.</span><span class="qt">{q["q"]}</span>' +
                          (f'<span class="pick">{q["n"]}개</span>' if "모두" not in q["q"] else '') +
                          '</div><div class="ansline"></div></div>')
            head = (f'<header class="shead"><div class="kicker">세트 {si}</div><h2>{s["title"]}</h2>'
                    f'<div class="ssub">{"구조를 보고 " if isimg else ""}보기에서 지정 개수만큼 고르시오</div></header>')
            if isimg:
                body = (f'<div class="sbody isbody"><div class="setbox img"><div class="bt">[보기] 구조 ①~⑪</div>'
                        f'<ul>{boxli}</ul></div><div class="setqs">{items}</div></div>')
            else:
                cols = "c3" if s["cols"] == 3 else ""
                body = (f'<div class="sbody"><div class="setbox {cols}"><div class="bt">[보기] 아래 ①~⑪ 중에서 고르시오</div>'
                        f'<ul>{boxli}</ul></div><div class="setqs">{items}</div></div>')
            RAW(f'<section class="page spage {self.P}">{head}{body}</section>')
            ans_items = ""
            for qi, q in enumerate(s["qs"], 1):
                av = " ".join(CIR[a] for a in q["ans"])
                ans_items += (f'<div class="ansitem"><div class="ansrow"><span class="num">{qi}.</span>'
                              f'<span class="av">{av}</span><span class="apick">{q["n"]}개</span></div>'
                              f'<div class="aexp">{exp_html(q["exp"])}</div></div>')
            RAW(f'''<section class="page spage {self.P}"><header class="shead"><div class="kicker">세트 {si} 해설</div>
<h2>{s["title"]}</h2><div class="ssub">앞 문제의 정답·해설</div></header>
<div class="sbody anspage"><div class="ansgrid">{ans_items}</div></div></section>''')

    # ---------------- 공부법 · 표지
    def study_page(self, tracker_names, note):
        chk = '<td class="chk">☐</td>'
        rows = "".join(f'<tr><td>{n}</td>{chk}{chk}{chk}<td class="last"></td></tr>' for n in tracker_names)
        tracker = ('<table class="track"><thead><tr><th>세트</th><th>1회독</th><th>2회독</th>'
                   '<th>3회독</th><th>다시 볼 문항 번호</th></tr></thead><tbody>' + rows + '</tbody></table>')
        steps = ('<div class="stepbox">'
                 '<div class="r"><span class="sn">1</span><span class="tx"><b>손으로 푼다</b> — 해설 페이지는 가리고, 보기에서 지정 개수만큼 직접 골라 답 줄에 쓴다.</span></div>'
                 '<div class="r"><span class="sn">2</span><span class="tx"><b>바로 채점</b> — 다음 장 해설로 표시. 틀린 건 <b>왜 틀렸는지</b> 한 줄 읽기.</span></div>'
                 '<div class="r"><span class="sn">3</span><span class="tx"><b>틀린 것만 다시</b> — 다음 회독엔 틀린 문항만. 3번 연속 맞으면 졸업.</span></div>'
                 '</div>')
        body = ('<div class="row c2">' +
                card("❌ 읽기만 하면 왜 안 되나",
                     ul(["여러 번 읽으면 글자가 <b>익숙</b>해져서 '아는 것 같은 착각'이 든다",
                         "시험은 <b>보기 ①~⑪를 주고 떠올려 고르는</b> 형식 — 읽기로는 이 능력이 안 길러짐",
                         "항생제는 <b>이름이 비슷</b>해서 특히 헷갈림 → 이름 유래(구조)로 묶어 외우기"]), "warm") +
                card("✅ 그래서 이렇게 — 인출 연습 3단계", steps, "soft") +
                '</div>' + tracker + f'<div class="one-line">{note}</div>')
        page = (f'<section class="page spage {self.P}"><header class="shead"><div class="kicker">필독</div>'
                f'<h2>이 자료 공부법 — 읽지 말고 \'풀어라\'</h2>'
                f'<div class="ssub">인출 연습(retrieval practice)</div></header>'
                f'<div class="sbody">{body}</div></section>')
        PAGES.insert(0, ("s", page))

    def cover_page(self, html):
        PAGES.insert(0, ("r", html))
