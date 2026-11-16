# -*- coding: utf-8 -*-
"""편별 퀴즈 HTML 생성: 바이러스 퀴즈를 틀(CSS·JS)로 쓰고 내용은 PDF 소스 모듈에서 생성
사용: python3 make_quiz.py <모듈(f_abx1)> <틀 html> <출력 html>
내용(요약·셀프테스트·세트·암기·종합표)은 전부 모듈에서 가져오므로 PDF와 어긋나지 않음."""
import re, sys, os, base64, importlib
mod, tpl, out = sys.argv[1], sys.argv[2], sys.argv[3]
here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, here); sys.argv = ["x"]
F = importlib.import_module(mod)
M = F.QUIZ_META

LAB = {"KEY": "핵심", "TIP": "암기 팁", "참고": "참고", "NOTE": "교재 정답 확인"}


def datauri(rel):
    b = open(os.path.join(here, rel), "rb").read()
    return "data:image/png;base64," + base64.b64encode(b).decode()


def imgs(h):
    return re.sub(r'src="(img/[^"]+\.png)"', lambda m: f'src="{datauri(m.group(1))}"', h)


def conv(h):
    """PDF 요약 HTML → 퀴즈 HTML 클래스"""
    h = h.replace("<span class='mt'>🎯</span>", ' <i class="tg rec">녹취</i>')
    h = h.replace("<span class='ms'>★</span>", '<i class="tg ex">출제</i> ')
    h = re.sub(r'<div class="card2[^"]*">', '<div class="card">', h)
    h = h.replace("<h4>", "<h3>").replace("</h4>", "</h3>")
    h = re.sub(r'<div class="row c2">', '<div class="g2">', h)
    h = re.sub(r'<table class="t[^"]*">', '<div class="tw"><table>', h).replace("</table>", "</table></div>")
    h = re.sub(r'<div class="one-line">(.*?)</div>', r'<p class="band">\1</p>', h, flags=re.S)
    h = re.sub(r'style="height:calc\((\d+)mm \* var\(--s,1\)\)"', lambda m: f'style="height:{int(m.group(1)) * 4.2:.0f}px"', h)
    return imgs(h)


def js(t):
    assert "`" not in t and "${" not in t
    return "`" + t + "`"


def opt(t):
    if t.startswith("img:"):
        return f'<img class="sopt" src="{datauri(os.path.join("img", F.K.imgdir, t[4:] + ".png"))}" alt="구조">'
    return t


# ---------------- 세트 데이터
sets = []
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
    sets.append(f"{{t:{js(title)},o:[{','.join(js(opt(o)) for o in S['box'])}],q:[\n" + ",\n".join(qs) + "]}")
SETS_JS = "const SETS=[\n" + ",\n".join(sets) + "\n];"
nq = sum(len(S["qs"]) for S in F.SETS)

# ---------------- 본문
sec = []
nav = ['<a href="#how"><span>00</span>공부법</a>']
summ = [x for x in F.K.SUMMARY if x[0] not in ("암기", "종합")]
for i, (kicker, title, body) in enumerate(summ, 1):
    sid = f"s{i}"
    nav.append(f'<a href="#{sid}"><span>{i:02d}</span>{re.sub(r"<[^>]+>", "", title).split(" — ")[0].split(" (")[0].split(" + ")[0].replace(" ★", "")}</a>')
    qa = F.SELFTEST_ANS.get(title, [])
    qs = F.K.SELFTEST.get(title, [])
    selfh = ""
    if qs:
        selfh = '<div class="self"><h4>가리고 답하기</h4>' + "".join(
            f'<details><summary>{q}</summary><p>{qa[j] if j < len(qa) else ""}</p></details>' for j, q in enumerate(qs)) + '</div>'
    sec.append(f'<section id="{sid}">\n  <div class="sh"><p class="eyebrow">{i:02d} · {kicker}</p><h2>{title}</h2></div>\n  {conv(body)}\n  {selfh}\n</section>')
nav += ['<a href="#sets"><span>▶</span>실전 세트</a>', '<a href="#formulas"><span>✓</span>암기 공식</a>', '<a href="#final"><span>✓</span>종합 비교표</a>']

formulas = "".join(f'<div><strong>{re.sub(r"<[^>]+>", "", a)}</strong>{conv(b)}</div>' for a, b in F.CHEAT1 + F.CHEAT2)
final_tbl = conv(F.table(F.FINAL_HEAD, F.FINAL_ROWS))

main = f'''<header class="top">
  <p class="eyebrow">PHAR · Medical Microbiology · 기말고사 대비 노트</p>
  <h1>{M["h1"]}</h1>
  <p class="lede">{M["lede"]}</p>
  <dl class="facts">
    <div><dt>범위</dt><dd>{M["scope"]}</dd></div>
    <div><dt>시험</dt><dd>12/14(월)~18(금)</dd></div>
    <div><dt>형식</dt><dd>보기 ①~⑪ 세트 → 문항별 지정 개수 고르기</dd></div>
    <div><dt>세트</dt><dd>{len(F.SETS)}세트 · {nq}문항</dd></div>
  </dl>
  <p class="legend"><span><i class="tg rec">녹취</i> 교수님이 녹취에서 강조</span><span><i class="tg ex">출제</i> 출제 유력</span><span>요약 뒤 셀프테스트는 안 보고 답하기 → 눌러서 확인</span></p>
</header>

<section id="how">
  <div class="sh"><p class="eyebrow">필독 · 인출 연습(retrieval practice)</p><h2>이 자료 공부법: 읽지 말고 풀어라</h2></div>
  <div class="g2">
    <div class="card"><h3>읽기만 하면 왜 안 되나</h3><ul>
      <li>여러 번 읽으면 글자가 <b>익숙</b>해져서 '아는 것 같은 착각'이 든다</li>
      <li>시험은 <b>보기 ①~⑪를 주고 떠올려 고르는</b> 형식. 읽기로는 이 능력이 안 길러짐</li>
      <li>항생제는 <b>이름이 비슷</b>해서 특히 헷갈림 → 이름 유래(구조)로 묶어 외우기</li></ul></div>
    <div class="card"><h3>그래서 이렇게: 인출 연습 3단계</h3><ul>
      <li><b>손으로 푼다.</b> 해설은 가리고, 보기에서 지정 개수만큼 직접 고른다.</li>
      <li><b>바로 채점.</b> 틀린 건 <b>왜 틀렸는지</b> 해설을 한 줄로 읽는다.</li>
      <li><b>틀린 것만 다시.</b> 3번 연속 맞으면 졸업.</li></ul></div>
  </div>
  <p class="band">{M["band"]}</p>
</section>

<div class="note" style="display:contents">
{chr(10).join(sec)}
</div>

<section id="sets">
  <div class="sh"><p class="eyebrow">실전 세트 {len(F.SETS)} · {nq}문항</p><h2>실전 세트: 보기에서 지정 개수만큼 고르기</h2></div>
  <div class="tabs" id="tabs" role="tablist" aria-label="세트 선택"></div>
  <div id="setpanel" style="display:flex;flex-direction:column;gap:14px"></div>
</section>

<section id="formulas">
  <div class="sh"><p class="eyebrow">한 줄 공식 모음</p><h2>암기 공식: 시험 직전에 이것만</h2></div>
  <div class="formulas note">{formulas}</div>
</section>

<section id="final">
  <div class="sh"><p class="eyebrow">종합</p><h2>{M["final_title"]}</h2></div>
  <div class="note">{final_tbl}</div>
  <p class="band">{F.FINAL_NOTE}</p>
  <footer>{M["footer"]} 풀이 기록은 이 브라우저에만 저장돼요.</footer>
</section>
'''

s = open(tpl, encoding="utf-8").read()
s = re.sub(r"<title>.*?</title>", f"<title>{M['title']}</title>", s, count=1)
s = re.sub(r'<nav aria-label="목차">.*?</nav>', '<nav aria-label="목차">\n    ' + "\n    ".join(nav) + "\n  </nav>", s, count=1, flags=re.S)
i = s.index('<header class="top">'); j = s.index("</main>")
s = s[:i] + main + s[j:]
i = s.index("const SETS=["); j = s.index("\n];", i) + 3
s = s[:i] + SETS_JS + s[j:]
s = re.sub(r"const KEY='[^']+'", f"const KEY='{M['key']}'", s, count=1)
extra = ("\n.sfigs{display:flex;flex-wrap:wrap;gap:10px;justify-content:space-around;align-items:flex-end}"
         ".sfig{margin:0;display:flex;flex-direction:column;align-items:center;background:#fff;border:1px solid var(--line);border-radius:8px;padding:6px 8px}"
         ".sfig img{max-width:100%;height:auto!important;max-height:120px}.sfig figcaption{font-size:12.5px;font-weight:700;color:var(--accent)}"
         ".opt .sopt{height:118px;width:100%;object-fit:contain;background:#fff;border-radius:4px;display:block}"
         ".opt:has(.sopt){flex-direction:column;align-items:stretch;width:172px}\n</style>")
s = s.replace("</style>", extra, 1)
open(out, "w", encoding="utf-8").write(s)
print("sets", len(F.SETS), "questions", nq, "bytes", len(s))
