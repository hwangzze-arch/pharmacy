import os, sys, glob, importlib
D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, D)

from parts import CH, MODS, FOOT, TITLE, CSS_EXTRA, IMG
ENTRIES = []
for m in MODS:
    ENTRIES += importlib.import_module(m).E
for e in ENTRIES:
    e["_flags"] = set(e.get("flags", []))
    if e.get("note"): e["_note"] = e["note"]
_NOTE = {}  # 삼성노트 필기 — 올려주면 notes23.py로
from parts import RX as _RX, MSR as _MSR


def _split(extra):
    """원서 정답 / 해설집 부분 나누기."""
    k = extra.find('📗 원서 정답'); ss = extra.find('📘 해설집')
    cut = lambda i: extra.rfind('<div class="sec"', 0, i)
    key = extra[cut(k):cut(ss) if ss > 0 else len(extra)] if k > 0 else ""
    sol = extra[cut(ss):] if ss > 0 else ""
    return key, sol


import extra23 as _x
for e in ENTRIES:
    if e["t"] == "c" and e.get("id") in _x.REC:
        e["rec"] = _x.REC[e["id"]]
_n = 0
for e in ENTRIES:
    if e["t"] != "q":
        continue
    _n += 1
    e["n"] = _n
    e["pair"] = bool(e.get("pair"))
    e["split"] = bool(e.get("split"))

NOTE_HD = '<div class="mynote"><div class="nt">✍️ 내 필기</div>'


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
body{font-family:'NotoKR','WenQuanYi Zen Hei',sans-serif;color:var(--ink);-webkit-print-color-adjust:exact;print-color-adjust:exact;}
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
.fx{font-family:'Noto Sans KR',sans-serif;font-weight:700;font-size:1.08em;color:#3d2a73;background:#fff;border-radius:6px;padding:2px 9px;display:inline-block;margin:1px 0 3px 0;border:1px solid #e0d6f3;}
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
.nr{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-top:6px;flex:none;}
.nr.one1{grid-template-columns:1fr;}
.nr .card{font-size:.92em;line-height:1.55;padding:6px 9px;}
.nr .card p{margin:0 0 3px 0;}
.nq{font-weight:700;color:#a4185f;margin:4px 0 1px 0 !important;} .na{margin:0 0 3px 0;}
.key2{background:#fff3bf;border-left:4px solid #f2c200;padding:3px 7px;border-radius:4px;font-weight:500;}
.work.sm{flex:none;height:var(--wh,120px);min-height:0;}
.qcol{flex:.9;}
.exp p{margin:0 0 4px 0;} .acol ul,.acol ol{margin:0 0 4px 0;}
.ans{font-size:1em;color:#0f4f3d;font-weight:500;background:#fff;border:1px solid #cfe5d8;border-radius:8px;padding:5px 9px;}
.ans p{margin:0 0 3px 0;}

.page.pair .qhalf + .qhalf{border-top:2px dashed #cfe5d8;padding-top:6px;}
.page.pair .qh{font-weight:700;color:#23263a;font-size:1.02em;}
.page.pair .bd2{background:#127a64;color:#fff;border-radius:6px;font-size:.82em;padding:1px 8px;margin-right:4px;}
.page.pair .qbody{margin-top:4px;}
.page.pair .work.sm{height:var(--wh,60px);}
.gls{flex:none;margin-top:6px;background:#f3f8ff;border:1px dashed #a5c3e8;border-radius:8px;padding:4px 10px 3px 10px;font-size:.82em;line-height:1.45;}
.gls .gt{display:inline-block;background:#1c5fa8;color:#fff;border-radius:6px;font-weight:700;font-size:.92em;padding:0 8px;margin-bottom:2px;}
.gls .gg{display:grid;grid-template-columns:repeat(3,1fr);column-gap:14px;row-gap:1px;}
.pbx .gls .gg{grid-template-columns:repeat(2,1fr);} .pair2 .pbx .gls .gg{grid-template-columns:1fr;}
.gls .gi{border-left:2px solid #c5d8f0;padding-left:6px;} .gls b{color:#0f3f8c;margin-right:3px;}
.pbx .gls{background:#fff;}
.qpb{flex:1;min-height:0;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:auto auto minmax(0,1fr);column-gap:14px;row-gap:6px;margin-top:8px;}
.qpb .qa{min-height:0;overflow:hidden;display:flex;flex-direction:column;justify-content:flex-end;gap:6px;}
.qc{min-height:0;overflow:hidden;display:flex;flex-direction:column;gap:6px;}
.qch{display:flex;align-items:center;gap:7px;border-bottom:2px solid #e5dbff;padding-bottom:3px;}
.qch .qn{flex:none;background:#7048e8;color:#fff;font-weight:700;border-radius:6px;font-size:.85em;padding:1px 9px;}
.qch .qt{flex:1;min-width:0;font-weight:700;color:#3b2a8a;font-size:1.02em;}
.qc .lbox .qsrc{font-size:.78em;}
.q1b{flex:1;min-height:0;margin-top:9px;column-count:2;column-gap:16px;column-fill:auto;overflow:hidden;}
.q1b>div{break-inside:avoid;margin-bottom:8px;}
.q1b .rblk img{break-inside:avoid;}
.q2b{flex:1;min-height:0;display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-top:9px;}
.q2b .lcol,.q2b .rcol{min-height:0;overflow:hidden;display:flex;flex-direction:column;gap:8px;}
.lbox{background:#eef3fa;border-radius:10px;border-left:5px solid var(--navy);padding:8px 12px;}
.lbox.top.g1{border-left-color:#e8590c;background:#fff4e6;} .lbox.top.g2{border-left-color:#1c7ed6;background:#e7f5ff;} .lbox.top.g3{border-left-color:#2b8a3e;background:#ebfbee;}
.lbox .lt{display:flex;align-items:center;gap:5px;flex-wrap:wrap;margin-bottom:4px;}
.lbox .qtext img{display:block;margin:3px 0;}
.lbox .term{background:#fff;border-left:3px solid #2f9e44;color:#2b4a2f;margin-top:7px !important;}
.rans{background:#fff4e6;border:1.5px solid #f59f00;border-radius:10px;padding:6px 12px;}
.rans .rlb{display:inline-block;background:#e8590c;color:#fff;font-weight:700;border-radius:6px;font-size:.85em;padding:0 9px;margin-bottom:3px;}
.rans .rav{font-weight:700;color:#7a2e00;line-height:1.55;}
.rblk{background:#fff;border:1px solid #dfe5ee;border-radius:10px;padding:6px 12px;}
.rblk .afig{border:none;padding:0;margin-top:4px;}
.rcont{font-size:.85em;color:#8b95a5;}
.lcol .gls .gg{grid-template-columns:1fr 1fr;}
.q2 .mz{width:max-content;}
.rx .tx,.rx .arw{white-space:nowrap;}
.ssp .sscols{flex:1;min-height:0;display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-top:8px;}
.ssp .sscols img{width:100%;height:100%;object-fit:contain;object-position:top center;border:1px solid #dfe5ee;border-radius:8px;background:#fff;}
""" + CSS_EXTRA

def foot(i):
    return f'<div class="ft"><span>{FOOT}</span><span class="lg">형광펜 <i class="y"></i>핵심 개념 <i class="g"></i>규칙·결론 <i class="p"></i>주의·시험 포인트 <i class="b"></i>정답</span><span>{i} / {{TOTAL}}</span></div>'

def side_html(items, flags=()):
    out = []
    for it in items:
        k = it[0]
        if k == "img":
            cap = it[2] if len(it) > 2 else ""
            h = f' style="--imgh:{it[3]}px"' if len(it) > 3 else ""
            out.append(f'<div class="fig"{h}><img src="{IMG}{it[1]}.jpg"><div class="cap">{cap}</div></div>')
        elif k == "mech":
            cap = it[2] if len(it) > 2 else ""
            out.append(f'<div class="fig mfig"><div class="mz">{it[1]}</div><div class="cap">{cap}</div></div>')
        elif k in ("ana", "trap", "tip", "card", "rec", "my"):
            title = {"ana": "🎈 비유", "trap": "⚠️ 함정", "tip": "📌 시험 포인트", "card": "", "rec": "🎯 녹취 — 교수님 강조", "my": "✍️ 내 정리 (단권화 노트 Q&amp;A)"}[k]
            if len(it) > 2:
                title = it[2]
            imp = " imp" if k in flags else ""
            out.append(f'<div class="card {k}{imp}"><div class="ct">{title}</div>{it[1]}</div>')
        elif k == "html":
            out.append(it[1])
    return "".join(out)


# 📚 용어 풀이 — 쪽 글에 나오는 용어를 나온 순서대로 (gloss23.py)
import re as _re
from gloss23 import G as _G
_SEEN = set()
def gl(html, n):
    txt = _re.sub(r"<img[^>]*>", " ", html)
    txt = _re.sub(r"<(?!sub|/sub)[^>]+>", " ", txt)
    hits = []
    for name, d, pat in _G:
        m = _re.search(pat, txt)
        if m:
            hits.append((m.start(), name, d))
    hits = [h for h in hits if h[1] not in _SEEN]  # 앞쪽에서 이미 풀이한 용어는 빼기
    hits.sort()
    hits = hits[:n]
    _SEEN.update(h[1] for h in hits)
    if not hits:
        return ""
    items = "".join(f'<span class="gi"><b>{nm}</b> {d}</span>' for _, nm, d in hits[:n])
    return f'<div class="gls"><span class="gt">📚 용어 풀이</span><div class="gg">{items}</div></div>'

def concept(i, n, e):
    main = []
    if e.get("detail"):
        main.append(f'<div class="sec">📖 상세 설명</div>{e["detail"]}')
    if e.get("formula"):
        main.append(f'<div class="fbox"><div class="sec f">📐 중요 공식</div>{e["formula"]}</div>')
    if e.get("example"):
        imp = " imp" if "ex" in e["_flags"] else ""
        main.append(f'<div class="ebox{imp}"><div class="sec e">✍️ 예제 및 풀이</div>{e["example"]}</div>')
    nr = ""
    if e.get("rec") or e.get("my"):
        nr = ('<div class="nr' + ('' if (e.get("rec") and e.get("my")) else ' one1') + '">' + (f'<div class="card rec"><div class="ct">🎯 녹취 — 교수님 설명</div>{e["rec"]}</div>' if e.get("rec") else "")
                    + (f'<div class="card my"><div class="ct">✍️ 내 정리 (단권화 노트)</div>{e["my"]}</div>' if e.get("my") else "") + '</div>')
    side = side_html(e.get("side", []), e["_flags"])
    nt = e.get("_note")
    if nt and nt[0] == "main": main.append(NOTE_HD + nt[1] + '</div>')
    if nt and nt[0] == "side": side += NOTE_HD + nt[1] + '</div>'
    core = f'<mk>{e["core"]}</mk>' if "core" in e["_flags"] else e["core"]
    oneimp = " imp" if "one" in e["_flags"] else ""
    body = f'<div class="main{" full" if not side else ""}">{"".join(main)}</div>' + (f'<div class="side">{side}</div>' if side else "")
    return f'''<section class="page">
{_hd21(f"{n:02d}", e["title"], e.get("sub",""), [e["part"]], "개념")}
<div class="core"><span class="lb">💡 핵심 개념</span>{core}</div>
{gl(e["title"] + e["core"] + e.get("detail", "") + e.get("example", "") + "".join(str(x[1]) for x in e.get("side", []) if x[0] != "img") + e.get("rec", "") + e["one"], e.get("gln", 9))}
<div class="body">{body}</div>
{nr}
{f'<div class="mband"><span class="mbl">⚗️ 메커니즘 (곡선 화살표)</span><div class="mz">{e["mech"]}</div></div>' if e.get("mech") else ""}
<div class="one{oneimp}"><span class="lb">🧠 뇌리에 박히는 한 줄</span><span>{e["one"]}</span></div>
{foot(i)}</section>'''

KIND = {"ex": "원서 예제", "draw": "구조식 그리기", "reag": "시약 쓰기", "ord": "순서 배열", "mech": "메커니즘", "prod": "생성물 예측", "int": "중간체 예측", "sa": "서술형", "bl": "빈칸 채우기"}

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
<div class="acol"><span class="al">정답 및 해설</span><div class="ans">정답 : {e["a"]}</div>{stitle}{steps}{opx}{extra}{f'<div class="afig"><div class="mz">{e["afig"]}</div></div>' if e.get("afig") else ""}
{f'<div class="qone{qimp}"><span class="lb">🧠 한 줄</span>{e["one"]}</div>' if e.get("one") else ""}</div></div>
{foot(i)}</section>'''

def _qparts(e):
    kinds = "".join(f'<span class="qk {k}">{KIND[k]}</span>' for k in e["kind"])
    src = f'<span class="qsrc">{e["src"]}</span>' if e.get("src") else ""
    exp = f'<div class="sec" style="color:#0f6b52;margin-top:4px">📝 풀이</div><div class="exp">{e["exp"]}</div>' if e.get("exp") else ""
    fig = f'<div class="afig"><div class="mz">{e["afig"]}</div></div>' if e.get("afig") else ""
    left = f'<div class="qcol"><div class="qcard">{kinds}{src}<div class="qtext">{e["q"]}</div></div><div class="work sm"><span class="wl">✏️ 내 풀이</span></div></div>'
    right = f'<div class="acol"><span class="al">정답 및 해설</span><div class="ans">{e["a"]}</div>{exp}{fig}{e.get("extra","")}</div>'
    return left, right


def question1(i, n, e):
    left, right = _qparts(e)
    return f'''<section class="page">
<div class="hd q"><span class="bd">문제 {n:02d}</span><div class="tt"><h1>{e["title"]}</h1></div><span class="pt">{e["part"]}</span></div>
<div class="qbody">{left}{right}</div>
{foot(i)}</section>'''


def question2(i, n, e1, e2):
    rows = ""
    for k, e in ((n, e1), (n + 1, e2)):
        left, right = _qparts(e)
        rows += f'<div class="qhalf"><div class="qh"><span class="bd2">문제 {k:02d}</span> {e["title"]} {tb(e.get("n"), True)}</div><div class="qbody">{left}{right}</div></div>'
    return f'''<section class="page pair">
<div class="hd q"><span class="bd">문제 {n:02d}–{n+1:02d}</span><div class="tt"><h1>{e1["part"]}</h1></div><span class="pt">짧은 문제 2개</span></div>
{rows}
{foot(i)}</section>'''


# ── 21장 정리본 스타일: 위 문제 → 메모(줄 없음) → 아래 정답과 해설 ──
def _qv(e, n, mini=False):
    kinds = "".join(f'<span class="qk {k}">{KIND[k]}</span>' for k in e["kind"])
    src = f'<span class="qsrc">{e["src"]}</span>' if e.get("src") else ""
    exp = f'<div class="xsec">📝 풀이</div><div class="exp">{e["exp"]}</div>' if e.get("exp") else ""
    fig = (f'<div class="afig"><div class="mz">{e["afig"]}</div></div>' if e.get("afig") else "") + e.get("extra", "")
    _tr = TOPR.get(e.get("n"))
    prob = f'<div class="pbx{" top g" + str(_tr[1]) if _tr else ""}"><span class="plb">PROBLEM {n:02d}</span>{tb(e.get("n"), True)}{kinds}{src}<div class="qtext">{e["q"]}</div>{gl(e["title"] + e["q"] + e["a"] + e.get("exp", ""), 4 if mini else 6)}</div>'
    _nt = _NOTE.get(e.get("n"))
    if _nt and _nt[0] == "memo":
        memo = f'<div class="memo hasn"><div class="mnote"><div class="mnt">✍ 내 필기 (삼성노트)</div>{_nt[1]}</div></div>'
    elif _nt:
        memo = '<div class="memo"><span class="ml2">✍ 메모</span><span class="mgo">✍ 내 필기는 다음 쪽 →</span></div>'
    else:
        memo = '<div class="memo"><span class="ml2">✍ 메모</span></div>'
    if mini or not fig:
        grid = f'<div class="agrid one1"><div class="xc">{exp}{fig}</div></div>'
    else:
        grid = f'<div class="agrid"><div class="xc">{exp}</div><div class="xc fc">{fig}</div></div>'
    ans = f'<div class="abx"><div class="ah"><span class="alb">정답과 해설</span><div class="abar">{e["a"]}</div></div>{grid}</div>'
    return prob, memo, ans

from top23 import TOPR_ID, TOP10  # 녹취 강조 기준 출제 예상 순위
TOPR = {e["n"]: TOPR_ID[e["id"]] for e in ENTRIES if e["t"] == "q" and e.get("id") in TOPR_ID}
_GR = {1: ("🥇 1등급", "g1"), 2: ("🥈 2등급", "g2"), 3: ("🥉 3등급", "g3")}

def tb(n, small=False):
    if n not in TOPR:
        return ""
    r, g = TOPR[n]; nm, c = _GR[g]
    return f'<span class="topb {c}{" sm" if small else ""}"><i>🔥 TOP</i><b>{r}위</b><em>{nm}</em></span>'

def _hd21(n, title, sub, tags, kind="문제", top=""):
    pills = "".join(f'<span class="pill">{t}</span>' for t in tags if t)
    return f'<div class="h21{" istop" if top else ""}"><div class="b21"><span>{kind}</span><b>{n}</b></div><div class="tt"><h1>{title}</h1><div class="sb">{sub}</div></div>{top}<div class="pills">{pills}</div></div>'

def question1(i, n, e):
    if e.get("split"):
        prob, memo, ans = _qv(e, n, mini=True)
        return [f'''<section class="page v21">
{_hd21(f"{n:02d}", e["title"], e.get("src",""), [e["part"]], top=tb(e.get("n")))}
{prob}{memo}<div class="nextp">정답과 해설은 다음 쪽 →</div>
{foot(i)}</section>''', f'''<section class="page v21 aonly">
{_hd21(f"{n:02d}", e["title"] + " — 정답과 해설", e.get("src",""), [e["part"]], top=tb(e.get("n")))}
{ans}
{foot(i + 1)}</section>''']
    prob, memo, ans = _qv(e, n)
    return f'''<section class="page v21">
{_hd21(f"{n:02d}", e["title"], e.get("src",""), [e["part"]], top=tb(e.get("n")))}
{prob}{memo}{ans}
{foot(i)}</section>'''

def question2(i, n, e1, e2):
    cols = ""
    for k, e in ((n, e1), (n + 1, e2)):
        prob, memo, ans = _qv(e, k, mini=True)
        cols += f'<div class="pc"><div class="qh"><span class="bd2">문제 {k:02d}</span> {e["title"]} {tb(e.get("n"), True)}</div>{prob}{memo}{ans}</div>'
    return f'''<section class="page v21 pair2">
{_hd21(f"{n:02d}–{n+1:02d}", e1["part"], "짧은 문제 2개", [])}
<div class="pcols">{cols}</div>
{foot(i)}</section>'''



# ── 생화학 「예제 및 문제 풀이 노트」 형식: 왼쪽 문제(원문·번역·용어) / 오른쪽 정답 → 해설. 메모 칸 없음.
#    그림은 줄이지 않고(모두 같은 배율) 넘치면 뒤 블록을 '정답과 해설 (계속)' 쪽으로 넘긴다 (_qsplit.json, make.sh가 채움)
import json as _json
try:
    QSPLIT = _json.load(open(os.path.join(D, "_qsplit.json")))
except Exception:
    QSPLIT = {}

def _blocks(e):
    """오른쪽 칸 블록: 정답 / 풀이(+afig) / 원서·해설집 그림들 (xsec 머리마다 한 블록)."""
    b = [f'<div class="rans"><span class="rlb">정답</span><div class="rav">{e["a"]}</div></div>']
    exp = f'<div class="xsec">📝 해설</div><div class="exp">{e["exp"]}</div>' if e.get("exp") else ""
    if e.get("afig"):
        exp += f'<div class="afig"><div class="mz">{e["afig"]}</div></div>'
    if exp:
        b.append(f'<div class="rblk">{exp}</div>')
    ex = e.get("extra", "")
    parts = ex.split('<div class="xsec">')
    if parts[0].strip():
        b.append(f'<div class="rblk">{parts[0]}</div>')
    for p in parts[1:]:
        h, _, body = p.partition('</div>')
        if '<div class="rx"' in body and '<div class="mz">' not in body:
            body = f'<div class="mz">{body}</div>'  # 반응식 줄은 칸 폭에 맞춤
        b.append(f'<div class="rblk"><div class="xsec">{h}</div>{body}</div>')
    return b

def qpage(i, n, e):
    """한 쪽 1문제: 왼쪽 위 문제 → 정답 → 해설 → 그림이 왼쪽 단 아래로, 이어서 오른쪽 단으로. 넘치면 render.js가 그림·글자를 줄임."""
    kinds = "".join(f'<span class="qk {k}">{KIND[k]}</span>' for k in e["kind"])
    _tr = TOPR.get(e.get("n"))
    q = e["q"]
    kk = q.find('<div class="term"')
    orig, trans = (q[:kk], q[kk:]) if kk >= 0 else (q, "")
    box = (f'<div class="lbox o{" top g" + str(_tr[1]) if _tr else ""}"><div class="lt"><span class="plb">PROBLEM {n:02d}</span>{tb(e.get("n"), True)}{kinds}</div>'
           f'<div class="qtext">{orig}</div>{trans}</div>')
    g = gl(e["title"] + e["q"] + e["a"] + e.get("exp", ""), 6)
    hd = _hd21(f"{n:02d}", e["title"], e.get("src", ""), [e["part"]], top=tb(e.get("n")))
    body = box + g + "".join(_blocks(e))
    return [f'''<section class="page v21 q1" data-qid="{e.get("id","")}">{hd}<div class="q1b">{body}</div>{foot(i)}</section>''']

try:
    QSOLO = set(_json.load(open(os.path.join(D, "_qsolo.json"))))
except Exception:
    QSOLO = set()

def qcol(n, e):
    """한 문제 = (머리, 문제 상자, 정답·해설 칸) — 두 문제의 정답·해설이 같은 높이에서 시작하도록 격자로."""
    kinds = "".join(f'<span class="qk {k}">{KIND[k]}</span>' for k in e["kind"])
    _tr = TOPR.get(e.get("n"))
    q = e["q"]
    kk = q.find('<div class="term"')
    orig, trans = (q[:kk], q[kk:]) if kk >= 0 else (q, "")
    head = f'<div class="qch"><span class="qn">문제 {n:02d}</span><span class="qt">{e["title"]}</span>{tb(e.get("n"), True)}</div>'
    box = (f'<div class="lbox o{" top g" + str(_tr[1]) if _tr else ""}"><div class="lt">{kinds}<span class="qsrc">{e.get("src","")}</span></div>'
           f'<div class="qtext">{orig}</div>{trans}</div>')
    g = gl(e["title"] + e["q"] + e["a"] + e.get("exp", ""), 4)
    ans = f'<div class="qa" data-qid="{e.get("id","")}">{"".join(_blocks(e))}{g}</div>'
    return head, box, ans

def qpair(i, n, e1, e2):
    h1, b1, a1 = qcol(n, e1); h2, b2, a2 = qcol(n + 1, e2)
    return f'''<section class="page v21 qp" data-q1="{e1.get("id","")}" data-q2="{e2.get("id","")}">{_hd21(f"{n:02d}–{n+1:02d}", e1["part"].split(" · ", 1)[-1], "문제 → 정답과 해설", [e1["part"]])}<div class="qpb">{h1}{h2}{b1}{b2}{a1}{a2}</div>{foot(i)}</section>'''

def notepage(i, e):
    n = e["n"]
    return f'''<section class="page v21 npage n{n}">
{_hd21(f"{n:02d}", e["title"] + " — 문제 + 내 필기", "문제를 보면서 삼성노트 텍스트상자 필기 읽기", [e["part"]], top=tb(e.get("n")))}
{_qv(e, n)[0]}
<div class="nbox"><div class="mnote big"><div class="mnt">✍ 내 필기 (삼성노트)</div>{_NOTE[n][1]}</div></div>
{foot(i)}</section>'''


def raw(i, e):
    return f'<section class="page {e.get("cls","")}">{e["html"]}{foot(i)}</section>'

pages = []
PID = {}
START = {}
ORIG = []
QPG = {}
cn = qn = 0
rng = {}
for e in ENTRIES:
    i = len(pages) + 1
    nxt_used = None
    if e["t"] == "c":
        cn += 1; pages.append(concept(i, cn, e))
    elif e["t"] == "q":
        if e.get("_skip"):
            continue
        if "exp" in e or e.get("n"):
            k = ENTRIES.index(e)
            nxt = ENTRIES[k + 1] if k + 1 < len(ENTRIES) else None
            if (e.get("id") not in QSOLO and nxt is not None and nxt["t"] == "q" and nxt.get("part") == e.get("part")
                    and nxt.get("id") not in QSOLO):
                qn += 1; pages.append(qpair(i, qn, e, nxt)); qn += 1; nxt["_skip"] = True; nxt_used = nxt
            else:
                qn += 1; pages.extend(qpage(i, qn, e))
        else:
            qn += 1; pages.append(question(i, qn, e))
    else:
        pages.append(raw(i, e))
    if not str(e.get("id", "")).startswith("f-mapx"):  # 새로 끼운 해설 쪽은 삼성노트 원래 쪽 번호에서 제외
        ORIG.extend(range(i, len(pages) + 1))
    if e["t"] == "q":
        for _q in ([e] + ([nxt_used] if nxt_used is not None else [])):
            QPG[_q.get("n")] = i
        for _q in ([e] + ([nxt_used] if nxt_used is not None else [])):
            _nt = _NOTE.get(_q.get("n"))
            if _nt and _nt[0] == "page":
                pages.append(notepage(len(pages) + 1, _q))
    if e.get("id"):
        PID[e["id"]] = (len(pages), cn if e["t"] == "c" else qn, e["t"])
        START[e["id"]] = i
        if nxt_used is not None and nxt_used.get("id"):
            START[nxt_used["id"]] = i
    if e["t"] == "q" and e.get("pair") and nxt_used is not None and nxt_used.get("id"):
        PID[nxt_used["id"]] = (len(pages), qn, "q")
    pk = e.get("part")
    if pk and e["t"] in "cq":
        r = rng.setdefault(pk, {"p": [i, i], "c": [], "q": []})
        r["p"][1] = i
        r["c" if e["t"] == "c" else "q"].append(cn if e["t"] == "c" else qn)
import re
if True:
    pages.append(f'<section class="page top10">{TOP10}{foot(len(pages) + 1)}</section>')
    # 삼성노트 표시(동그라미·형광·화살표) — 원래 쪽 번호 j 의 표시를 같은 쪽 위에 그대로
    for j, idx in enumerate(ORIG, 1):
        if os.path.exists(os.path.join(D, "ov", f"{j:02d}.png")):
            pg = pages[idx - 1]; cut = pg.rfind("</section>")
            pages[idx - 1] = pg[:cut] + f'<img class="ovl" src="ov/{j:02d}.png">' + pg[cut:]
html = "".join(pages).replace("{TOTAL}", str(len(pages)))
html = re.sub(r"\{QP:(\d+)\}", lambda m: str(QPG[int(m.group(1))]), html)
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
    v = PID.get(m.group(1)) or ids.get(m.group(1))
    if not v:
        print("MISSING REF", m.group(1)); return "?"
    return f'{"개념" if v[2] == "c" else "문제"} {v[1]:02d}(p.{v[0]})'
html = re.sub(r"\{REF:([^}]+)\}", ref, html)
html = re.sub(r"\{PAGE:([^}]+)\}", lambda m: str(PID[m.group(1)][0]) if m.group(1) in PID else str(ids[m.group(1)][0]), html)
html = re.sub(r"\{QN:([^}]+)\}", lambda m: f"{PID[m.group(1)][1]:02d}", html)
html = re.sub(r"\{CN:([^}]+)\}", lambda m: f"{PID[m.group(1)][1]:02d}", html)
html = re.sub(r"\{PR:([^}]+)\}", lambda m: f"{PID[m.group(1)][0]}" + (f"–{PID[m.group(1)+'2'][0]}" if m.group(1)+'2' in PID else ""), html)
html = html.replace("{NC}", str(cn)).replace("{NQ}", str(qn))
# 표지 목차 (21장 정리본 스타일)
_rows = []; _lastp = None; _c = 0
_BG = {"예제": "w", "본문": "p", "과제": "h", "강의": "l", "변형": "v"}
for e in ENTRIES:
    if e["t"] not in "cq" or e.get("t") == "r":
        continue
    if e.get("part") != _lastp:
        _lastp = e.get("part"); _rows.append(f'<div class="tr part">{_lastp}</div>')
    if e["t"] == "c":
        _c += 1
        _rows.append(f'<div class="tr"><span class="bg c">개념</span><span class="nm">{_c:02d}</span><span class="ti">{e.get("toc", e["title"])}</span><span class="pg">{START[e["id"]]}</span></div>')
    else:
        mk = ("🔥" if e.get("n") in TOPR else "") + ("🎯" if e.get("rec") else "")
        nm = e["num"] if e["badge"] != "변형" else f'Q{e["n"]:02d}'
        _rows.append(f'<div class="tr"><span class="bg {_BG[e["badge"]]}">{e["badge"]}</span><span class="nm">{nm}</span><span class="ti">{mk}{e["toc"]}</span><span class="pg">{START[e["id"]]}</span></div>')
_cnt = {k: sum(1 for e in ENTRIES if e["t"] == "q" and e.get("badge") == k) for k in _BG}
html = html.replace("{TOC}", "".join(_rows)).replace('class="toc"', f'class="toc" style="--rows:{(len(_rows) + 1) // 2}"', 1)
html = html.replace("{TOCSTAT}", " · ".join(f'<span style="white-space:nowrap">{k} {v}</span>' for k, v in _cnt.items() if v))
_IDN = {e["id"]: e["n"] for e in ENTRIES if e["t"] == "q" and e.get("id")}
html = re.sub(r"\{QNI:([^}]+)\}", lambda m: f"{_IDN[m.group(1)]:02d}", html)
html = re.sub(r"\{QPI:([^}]+)\}", lambda m: str(START[m.group(1)]), html)
from themes import THEMES as _TH
PALETTE = '''
/* ── 색감: 주황 · 보라 · 연두 · 분홍 */
:root{--navy:#6741d9;--nblue:#5f3dc4;--indigo:#6741d9;--indigo-soft:#f3f0ff;}
.h21{border-bottom-color:#7048e8 !important;} .b21{background:linear-gradient(160deg,#845ef7,#6741d9) !important;}
.h21 h1{color:#4c2f9e !important;}
.pill{border-color:#d0bfff !important;background:#f3f0ff !important;color:#5f3dc4 !important;}
.core{background:#fff4e6 !important;border-color:#ffd8a8 !important;border-left-color:#fd7e14 !important;} .core .lb{background:#fd7e14 !important;}
.one{background:linear-gradient(90deg,#7048e8,#d6336c) !important;}
.card.tip,.card.ana{background:#f4fce3 !important;border-color:#c0eb75 !important;} .card.tip .ct,.card.ana .ct{color:#5c940d !important;}
.card.rec,.card.trap{background:#fff0f6 !important;border-color:#faa2c1 !important;} .card.rec .ct,.card.trap .ct{color:#c2255c !important;}
table.t th{background:#f3f0ff !important;color:#5f3dc4 !important;}
.mband .mbl{color:#5f3dc4 !important;background:#f3f0ff !important;} .mband,.fig{border-color:#e5dbff !important;}
.sec{color:#6741d9 !important;}
.lbox{background:#f8f6ff !important;border-left-color:#7048e8 !important;}
.plb{background:#7048e8 !important;}
.lbox .term,.term{background:#f4fce3 !important;border-left:3px solid #82c91e !important;color:#2b5a0a !important;}
.gls{background:#fff0f6 !important;border-color:#faa2c1 !important;} .gls .gt{background:#e64980 !important;} .gls b{color:#a61e4d !important;} .gls .gi{border-left-color:#fcc2d7 !important;}
.rans{background:#fff4e6 !important;border-color:#fd7e14 !important;} .rans .rlb{background:#f76707 !important;} .rans .rav{color:#a33d00 !important;}
.rblk{border-color:#e5dbff !important;} .xsec{color:#7048e8 !important;}
.ft{border-top-color:#e5dbff !important;}
'''
CSS = CSS + _TH[os.environ.get('THEME', 'mid21')] + PALETTE
html = f'<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>{TITLE}</title><style>{CSS}</style></head><body>{html}</body></html>'
open(os.path.join(D, "index.html"), "w").write(html)
print("pages", len(pages), "concepts", cn, "questions", qn)
