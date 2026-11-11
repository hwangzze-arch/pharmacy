# 사용법: python3 sync_quiz.py <build_통합본 폴더> <퀴즈 html 경로>
# -*- coding: utf-8 -*-
"""PDF 세트 데이터(f_virus.SETS) → 퀴즈 HTML의 SETS 배열로 생성해 교체"""
import re, sys, json
build, html = sys.argv[1], sys.argv[2]
sys.path.insert(0, build); sys.argv = ["x"]
import core, f_virus as F

LAB = {"KEY": "핵심", "TIP": "암기 팁", "참고": "참고", "NOTE": "교재 정답 확인"}


def js(t):
    assert "`" not in t and "${" not in t
    return "`" + t + "`"


out = []
for S in F.SETS:
    title = re.sub(r"^세트 \d+ · ", "", S["title"])
    qs = []
    for q in S["qs"]:
        e, k, w = [], None, False
        for ln in q["exp"]:
            kind, body = ln.split("|", 1) if "|" in ln else ("", ln)
            if kind in ("O", "X", "?"):
                lab, txt = body.split("::", 1) if "::" in body else ("", body)
                e.append(f"[{1 if kind == 'O' else 0},{js((lab + ' ' + txt).strip())}]")
            elif kind in LAB:
                if k is None:
                    k = [LAB[kind], body]; w = kind == "NOTE"
                else:
                    k[1] += " · " + body
            else:
                e.append(f"[0,{js(ln)}]")
        item = f"{{q:{js(q['q'])},a:[{','.join(str(a + 1) for a in q['ans'])}],e:[{','.join(e)}]"
        if k: item += f",k:[{js(k[0])},{js(k[1])}]"
        if w: item += ",w:1"
        qs.append(" " + item + "}")
    out.append(f"{{t:{js(title)},o:[{','.join(js(o) for o in S['box'])}],q:[\n" + ",\n".join(qs) + "]}")
new = "const SETS=[\n" + ",\n".join(out) + "\n];"

s = open(html, encoding="utf-8").read()
i = s.index("const SETS=[")
j = s.index("\n];", i) + len("\n];")
s = s[:i] + new + s[j:]
s = re.sub(r"const KEY='virus-final-v\d+'", "const KEY='virus-final-v4'", s)
a = "<div><strong>간염 전파</strong>모음(A·E)=<b>입</b>, 자음(B·C·D)=<b>피</b></div>"
s = s.replace(a, "<div><strong>HBV 만성화</strong>성인 5~10% &lt; 소아 30~50% &lt; <b>영아 80~90%</b> — 어릴수록 만성화</div>")
open(html, "w", encoding="utf-8").write(s)
print("sets", len(F.SETS), "questions", sum(len(S["qs"]) for S in F.SETS))
