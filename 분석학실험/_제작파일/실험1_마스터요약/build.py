import os, sys, glob, importlib
D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, D)

MODS = ["c00_front", "c10_part1", "c20_part2", "c30_part3", "c40_part4", "c90_final"]
ENTRIES = []
for m in MODS:
    ENTRIES += importlib.import_module(m).E
# 필기 반영(annot.py)은 아직 없음 — 나중에 필기를 받으면 의약품 분석학 마스터요약처럼 추가
for e in ENTRIES:
    e["_flags"] = set(e.get("flags", []))
NOTE_HD = '<div class="mynote"><div class="nt">✍️ 내 필기</div>'

FOOT = "의약품분석학 실험 · 실험 1 뷰렛의 검정 마스터 노트"

CSS = r"""
@page { size: 297mm 210mm; margin: 0; }
:root{
 --paper:#fbf9f4; --ink:#2c3038; --muted:#6c7280; --line:#e4dfd3;
 --indigo:#4651c8; --indigo-soft:#eef0fd; --teal:#127a64; --teal-soft:#eef7f2;
 --yel:#fff4cc; --yel-b:#efd27a; --pink:#fde9ef; --pink-b:#f2a7bd; --mint:#e7f6ec; --mint-b:#9fd5b1;
 --blue-soft:#eaf2fb; --blue-b:#a9c6e8;
}
*{box-sizing:border-box;}
html,body{margin:0;padding:0;background:var(--paper);}
body{font-family:'Noto Sans KR','Pretendard',sans-serif;color:var(--ink);-webkit-print-color-adjust:exact;print-color-adjust:exact;}
.page{width:297mm;height:210mm;padding:8mm 12mm 14mm 12mm;position:relative;overflow:hidden;page-break-after:always;display:flex;flex-direction:column;background:var(--paper);font-size:var(--fs,12.4px);line-height:1.62;}
.hd{display:flex;align-items:center;gap:12px;border-bottom:2px solid var(--indigo);padding-bottom:6px;flex:none;}
.hd .bd{background:var(--indigo);color:#fff;font-weight:700;font-size:12.5px;border-radius:7px;padding:4px 11px;white-space:nowrap;}
.hd.q{border-bottom-color:var(--teal);} .hd.q .bd{background:var(--teal);}
.hd .tt{flex:1;min-width:0;}
.hd h1{margin:0;font-size:19.5px;line-height:1.3;font-weight:700;color:#23263a;}
.hd .sb{font-size:11px;color:var(--muted);}
.hd .pt{background:var(--indigo-soft);color:var(--indigo);font-weight:700;font-size:11px;border-radius:12px;padding:3px 11px;white-space:nowrap;}
.hd.q .pt{background:var(--teal-soft);color:var(--teal);}
.core{margin-top:8px;background:var(--yel);border:1px solid var(--yel-b);border-radius:9px;padding:6px 13px;font-weight:700;flex:none;font-size:1.04em;}
.core .lb{display:inline-block;background:#fff;border:1px solid var(--yel-b);color:#7a5c00;border-radius:6px;font-size:.82em;padding:0 7px;margin-right:8px;}
.body{display:flex;gap:16px;margin-top:9px;flex:1;min-height:0;}
.main{flex:1.35;min-width:0;overflow:hidden;}
.side{flex:1;min-width:0;overflow:hidden;display:flex;flex-direction:column;gap:7px;}
.main.full{flex:1;}
.sec{font-weight:700;color:#2f3a8f;margin:2px 0 3px 0;font-size:1.02em;}
.sec.f{color:#6a3d9a;} .sec.e{color:#9a4a12;}
p{margin:0 0 4px 0;}
ul,ol{margin:0 0 5px 0;padding-left:1.25em;}
li{margin:0 0 2px 0;}
.term{font-size:.84em;color:#6b5a33;background:#fbf3df;border-left:3px solid #e2c98a;border-radius:3px;padding:1px 7px;margin:1px 0 5px 0;}
.fbox{background:#f4f0fb;border:1px solid #d6c9ef;border-radius:8px;padding:6px 11px;margin:4px 0 6px 0;}
.fx{font-family:'Noto Sans KR','Pretendard',sans-serif;font-weight:700;font-size:1.08em;color:#3d2a73;background:#fff;border-radius:6px;padding:2px 9px;display:inline-block;margin:1px 0 3px 0;border:1px solid #e0d6f3;}
.ebox{background:#fff6ee;border:1px solid #f0c9a4;border-radius:8px;padding:6px 11px;margin:4px 0 6px 0;}
.card{background:#fff;border:1px solid var(--line);border-radius:9px;padding:7px 11px;}
.card.ana{background:#eef6fd;border-color:var(--blue-b);}
.card.trap{background:var(--pink);border-color:var(--pink-b);}
.card.tip{background:var(--mint);border-color:var(--mint-b);}
.card .ct{font-weight:700;margin-bottom:2px;}
.card.ana .ct{color:#1d5a95;} .card.trap .ct{color:#a3264f;} .card.tip .ct{color:#1f7a3f;}
.fig{background:#fff;border:1px solid var(--line);border-radius:9px;padding:5px;text-align:center;}
.fig img{max-width:100%;max-height:var(--imgh,240px);border-radius:5px;}
.fig .cap{font-size:.8em;color:var(--muted);margin-top:2px;}
.one{margin-top:8px;background:var(--indigo);color:#fff;border-radius:10px;padding:7px 14px;font-weight:700;flex:none;display:flex;gap:10px;align-items:center;font-size:1.05em;}
.one .lb{background:rgba(255,255,255,.18);border-radius:6px;font-size:.8em;padding:1px 8px;white-space:nowrap;}
table.t{border-collapse:collapse;width:100%;margin:3px 0 6px 0;font-size:.93em;background:#fff;}
table.t th{background:#eef0f8;color:#2f3a8f;font-weight:700;text-align:left;}
table.t th,table.t td{border:1px solid #dcdfe8;padding:2px 6px;vertical-align:top;}
y{background:#ffe98a;padding:0 2px;border-radius:2px;}
g{background:#bff0c8;padding:0 2px;border-radius:2px;}
pk{background:#ffd3e0;padding:0 2px;border-radius:2px;}
b{font-weight:700;}
.ko{color:var(--muted);font-weight:400;}
.tag{display:inline-block;font-size:.8em;font-weight:700;border-radius:5px;padding:0 6px;margin-right:4px;vertical-align:1px;}
.tag.j{background:#ffd3e0;color:#9a1d48;} .tag.h{background:#d9ecff;color:#1d5a95;} .tag.s{background:#e3f6e1;color:#2a6b22;}
/* question page */
.qbody{display:flex;gap:16px;margin-top:9px;flex:1;min-height:0;}
.qcol{flex:1;display:flex;flex-direction:column;gap:9px;min-width:0;min-height:0;}
.acol{flex:1.08;min-width:0;background:#f3f8f5;border:1px solid #cfe5d8;border-radius:11px;padding:9px 13px;overflow:hidden;}
.qcard{background:#fff;border:1px solid var(--line);border-radius:11px;padding:9px 13px;flex:none;overflow:hidden;}
.qk{display:inline-block;background:#3a3f4b;color:#fff;border-radius:6px;font-size:.8em;font-weight:700;padding:1px 8px;margin-right:6px;}
.qk.mc{background:#4651c8;} .qk.sa{background:#a3264f;} .qk.calc{background:#9a4a12;} .qk.tf{background:#127a64;} .qk.bl{background:#6a3d9a;}
.qsrc{font-size:.8em;color:var(--muted);}
.qtext{margin-top:4px;font-weight:500;}
.opts{margin:4px 0 0 0;padding:0;list-style:none;}
.opts li{margin:1px 0;}
.blank{display:inline-block;min-width:4.2em;border-bottom:1.6px solid #6a3d9a;text-align:center;color:#6a3d9a;font-weight:700;margin:0 2px;}
.work{flex:1;min-height:70px;border:2px dashed #c9c3b4;border-radius:11px;background-color:#fffdf8;background-image:radial-gradient(#d8d2c3 1px,transparent 1px);background-size:16px 16px;position:relative;}
.work .wl{position:absolute;top:8px;left:10px;background:#fff;border:1px solid #e3ddcd;border-radius:7px;font-size:.82em;font-weight:700;color:#6c7280;padding:1px 8px;}
.al{display:inline-block;background:var(--teal);color:#fff;border-radius:6px;font-size:.8em;font-weight:700;padding:1px 9px;}
.ans{color:#0f6b52;font-weight:700;font-size:1.1em;margin:5px 0 6px 0;}
.st{display:flex;gap:8px;margin:3px 0 4px 0;}
.st .n{flex:none;background:var(--indigo);color:#fff;border-radius:11px;font-size:.78em;font-weight:700;padding:1px 8px;height:1.6em;margin-top:.12em;}
.st .c{flex:1;min-width:0;}
.why{color:#5b6070;font-size:.92em;}
.why::before{content:'👉 왜? ';}
.opx{margin:2px 0 4px 0;font-size:.95em;}
.opx div{margin:1px 0;}
.qone{margin-top:7px;background:#127a64;color:#fff;border-radius:9px;padding:5px 12px;font-weight:700;}
.qone .lb{background:rgba(255,255,255,.2);border-radius:5px;font-size:.8em;padding:0 7px;margin-right:6px;}
.ft{position:absolute;left:12mm;right:12mm;bottom:5mm;display:flex;justify-content:space-between;font-size:9.5px;color:#9a9486;border-top:1px solid var(--line);padding-top:4px;}
/* cover */
.cover{background:linear-gradient(135deg,#2c3a8c 0%,#4651c8 55%,#1b8a75 100%);color:#fff;}
.cover .k{letter-spacing:.18em;font-size:12px;font-weight:700;opacity:.85;margin-top:16mm;}
.cover h1{font-size:34px;line-height:1.3;margin:10px 0 8px 0;}
.cover .s{font-size:14px;opacity:.92;}
.cover .pills{display:flex;gap:9px;margin-top:16px;flex-wrap:wrap;align-items:center;}
.cover .pill{background:#fff;color:#2c3a8c;border-radius:16px;padding:4px 12px;font-weight:700;font-size:12px;}
.cover .grid{position:absolute;left:12mm;right:12mm;bottom:16mm;display:grid;grid-template-columns:repeat(7,1fr);gap:8px;}
.cover .gc{background:rgba(255,255,255,.13);border:1px solid rgba(255,255,255,.3);border-radius:10px;padding:8px 9px;font-size:10.5px;line-height:1.5;}
.cover .gc b{display:block;font-size:11.5px;margin-bottom:2px;}
.cover .ft{color:rgba(255,255,255,.75);border-top-color:rgba(255,255,255,.25);}
mk{box-shadow:0 0 0 2px #e03131;border-radius:3px;padding:0 2px;-webkit-box-decoration-break:clone;box-decoration-break:clone;}
mk::after{content:'★';color:#e03131;font-size:.8em;margin-left:2px;vertical-align:.25em;}
.one mk{box-shadow:0 0 0 2px #ff8787;} .one mk::after{color:#ffc9c9;}
.imp{box-shadow:0 0 0 2.5px #e03131 !important;position:relative;}
.imp:not(table)::after{content:'★ 중요';position:absolute;top:-9px;right:12px;background:#e03131;color:#fff;font-size:10px;font-weight:700;border-radius:8px;padding:0 8px;line-height:16px;}
table.t.imp{box-shadow:none !important;outline:2.5px solid #e03131;outline-offset:1px;}
tr.hl td{background:#ffe3e3;}
.mynote{background:#fff5f5;border:1.5px dashed #f08c8c;border-radius:9px;padding:6px 11px;margin:6px 0 4px 0;font-size:.95em;line-height:1.6;}
.mynote .nt{font-weight:700;color:#c92a2a;margin-bottom:2px;}
.mynote p{margin:0 0 4px 0;} .mynote .q{font-weight:700;color:#c92a2a;}
.mynote .rd{color:#d6336c;font-weight:700;}
.work.hasnote{background-image:none;padding:30px 10px 8px 10px;overflow:hidden;}
.work.hasnote .mynote{margin:0;font-size:.9em;}
.cols{display:grid;grid-template-columns:1fr 1fr;gap:12px;}
.cols3{display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px;}
"""

def foot(i):
    return f'<div class="ft"><span>{FOOT}</span><span>{i} / {{TOTAL}}</span></div>'

def side_html(items, flags=()):
    out = []
    for it in items:
        k = it[0]
        if k == "img":
            cap = it[2] if len(it) > 2 else ""
            h = f' style="--imgh:{it[3]}px"' if len(it) > 3 else ""
            out.append(f'<div class="fig"{h}><img src="img/{it[1]}.jpg"><div class="cap">{cap}</div></div>')
        elif k in ("ana", "trap", "tip", "card"):
            title = {"ana": "🎈 비유", "trap": "⚠️ 함정", "tip": "📌 시험·노트 포인트", "card": ""}[k]
            if len(it) > 2:
                title = it[2]
            imp = " imp" if k in flags else ""
            out.append(f'<div class="card {k}{imp}"><div class="ct">{title}</div>{it[1]}</div>')
        elif k == "html":
            out.append(it[1])
    return "".join(out)

def concept(i, n, e):
    main = []
    if e.get("detail"):
        main.append(f'<div class="sec">📖 상세 설명</div>{e["detail"]}')
    if e.get("formula"):
        main.append(f'<div class="fbox"><div class="sec f">📐 중요 공식</div>{e["formula"]}</div>')
    if e.get("example"):
        imp = " imp" if "ex" in e["_flags"] else ""
        main.append(f'<div class="ebox{imp}"><div class="sec e">✍️ 예제 및 풀이</div>{e["example"]}</div>')
    side = side_html(e.get("side", []), e["_flags"])
    nt = e.get("_note")
    if nt and nt[0] == "main": main.append(NOTE_HD + nt[1] + '</div>')
    if nt and nt[0] == "side": side += NOTE_HD + nt[1] + '</div>'
    core = f'<mk>{e["core"]}</mk>' if "core" in e["_flags"] else e["core"]
    oneimp = " imp" if "one" in e["_flags"] else ""
    body = f'<div class="main{" full" if not side else ""}">{"".join(main)}</div>' + (f'<div class="side">{side}</div>' if side else "")
    return f'''<section class="page">
<div class="hd"><span class="bd">개념 {n:02d}</span><div class="tt"><h1>{e["title"]}</h1><div class="sb">{e.get("sub","")}</div></div><span class="pt">{e["part"]}</span></div>
<div class="core"><span class="lb">💡 핵심 개념</span>{core}</div>
<div class="body">{body}</div>
<div class="one{oneimp}"><span class="lb">🧠 뇌리에 박히는 한 줄</span><span>{e["one"]}</span></div>
{foot(i)}</section>'''

KIND = {"mc": "객관식", "sa": "주관식·서술형", "calc": "계산", "tf": "O / X", "bl": "빈칸 채우기"}

def question(i, n, e):
    kinds = "".join(f'<span class="qk {k}">{KIND[k]}</span>' for k in e["kind"])
    src = f'<span class="qsrc">{e["src"]}</span>' if e.get("src") else ""
    steps = "".join(f'<div class="st"><span class="n">Step {j+1}</span><div class="c">{s[0]}' + (f'<div class="why">{s[1]}</div>' if len(s) > 1 and s[1] else "") + '</div></div>' for j, s in enumerate(e.get("steps", [])))
    opx = f'<div class="sec" style="color:#0f6b52;margin-top:4px">🔍 보기별 해설</div><div class="opx">{e["opx"]}</div>' if e.get("opx") else ""
    extra = e.get("extra", "")
    stitle = '<div class="sec" style="color:#0f6b52">🪜 Step-by-Step 풀이</div>' if steps else ""
    qimp = " imp" if "qone" in e["_flags"] else ""
    nt = e.get("_note")
    wnote = NOTE_HD + nt[1] + '</div>' if nt else ""
    return f'''<section class="page">
<div class="hd q"><span class="bd">문제 {n:02d}</span><div class="tt"><h1>{e["title"]}</h1><div class="sb">{e.get("sub","")}</div></div><span class="pt">{e["part"]}</span></div>
<div class="qbody"><div class="qcol"><div class="qcard">{kinds}{src}<div class="qtext">{e["q"]}</div></div>
<div class="work{' hasnote' if wnote else ''}"><span class="wl">✏️ 내 풀이 — 먼저 풀고 오른쪽을 보세요</span>{wnote}</div></div>
<div class="acol"><span class="al">정답 및 해설</span><div class="ans">정답 : {e["a"]}</div>{stitle}{steps}{opx}{extra}
<div class="qone{qimp}"><span class="lb">🧠 한 줄</span>{e["one"]}</div></div></div>
{foot(i)}</section>'''

def raw(i, e):
    return f'<section class="page {e.get("cls","")}">{e["html"]}{foot(i)}</section>'

pages = []
cn = qn = 0
rng = {}
for e in ENTRIES:
    i = len(pages) + 1
    if e["t"] == "c":
        cn += 1; pages.append(concept(i, cn, e))
    elif e["t"] == "q":
        qn += 1; pages.append(question(i, qn, e))
    else:
        pages.append(raw(i, e))
    pk = e.get("part")
    if pk and e["t"] in "cq":
        r = rng.setdefault(pk, {"p": [i, i], "c": [], "q": []})
        r["p"][1] = i
        r["c" if e["t"] == "c" else "q"].append(cn if e["t"] == "c" else qn)
html = "".join(pages).replace("{TOTAL}", str(len(pages)))
for pk, r in rng.items():
    s = f'p.{r["p"][0]}–{r["p"][1]} · 개념 {min(r["c"]):02d}–{max(r["c"]):02d} · 문제 {min(r["q"]):02d}–{max(r["q"]):02d}' if r["c"] and r["q"] else f'p.{r["p"][0]}–{r["p"][1]}'
    html = html.replace("{R:" + pk + "}", s)
    html = html.replace("{S:" + pk + "}", str(r["p"][0]))
import re
ids = {}
c2 = q2 = 0
for k, e in enumerate(ENTRIES):
    if e["t"] == "c": c2 += 1
    if e["t"] == "q": q2 += 1
    if e.get("id"):
        ids[e["id"]] = (k + 1, c2 if e["t"] == "c" else q2, e["t"])
def ref(m):
    v = ids.get(m.group(1))
    if not v:
        print("MISSING REF", m.group(1)); return "?"
    return f'{"개념" if v[2] == "c" else "문제"} {v[1]:02d}(p.{v[0]})'
html = re.sub(r"\{REF:([^}]+)\}", ref, html)
html = re.sub(r"\{PAGE:([^}]+)\}", lambda m: str(ids[m.group(1)][0]), html)
html = html.replace("{NC}", str(cn)).replace("{NQ}", str(qn))
FONTS = "".join(f'<link rel="stylesheet" href="file://{p}">' for p in (os.path.expanduser(f'~/.fonts/nskr/package/{w}.css') for w in (400, 500, 700, 800)) if os.path.exists(p))
html = f'<!doctype html><html lang="ko"><head><meta charset="utf-8">{FONTS}<title>분석학실험 실험1 뷰렛의 검정 마스터 노트</title><style>{CSS}</style></head><body>{html}</body></html>'
open(os.path.join(D, "index.html"), "w", encoding="utf-8").write(html)
print("pages", len(pages), "concepts", cn, "questions", qn)
