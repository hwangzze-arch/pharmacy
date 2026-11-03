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
import answers as _ans
from notes22 import NOTE as _NOTE
from parts import RX as _RX, MSR as _MSR


def _split(extra):
    """원서 정답 / 해설집 부분 나누기."""
    k = extra.find('📗 원서 정답'); ss = extra.find('📘 해설집')
    cut = lambda i: extra.rfind('<div class="sec"', 0, i)
    key = extra[cut(k):cut(ss) if ss > 0 else len(extra)] if k > 0 else ""
    sol = extra[cut(ss):] if ss > 0 else ""
    return key, sol


if os.environ.get("ED") != "core":
    import extra22 as _x
    _by = {e.get("id"): e for e in ENTRIES if e.get("id")}
    # 얇은 쪽 합치기: 속도론 → 산성 할로젠화, 생합성 → LDA
    _by["c-acidbr"]["detail"] = '<ul><li>아세토페논 + Br₂(아세트산) → α-브로모아세토페논(72 %). 4단계: 양성자화 → α-H 제거(엔올) → Br₂ 공격 → O–H 탈양성자 (자세한 설명은 아래 노트).</li><li><b>1번만</b>, <y>더 치환된 쪽</y> (산성 = 더 안정한 엔올). HBr이 생겨 <b>자기 촉매</b>.</li></ul>'
    _by["c-acidbr"]["detail"] += '<p><b>속도론</b>(슬 10): 속도 = k[케톤][H⁺], <y>[X₂] 없음</y> · D₃O⁺ 교환 속도 = 할로젠화 속도 → 느린 단계 = <g>엔올 형성</g>(공통 중간체). 엔올화는 가역이라 D₂O/D⁺에 오래 두면 모든 α-H → D.</p>'
    _by["c-acidbr"]["title"] = "산성 α-할로젠화 + 속도론 — 엔올 중간체의 증거"; _by["c-acidbr"]["sub"] = "Acid-catalyzed α-halogenation · rate law · 슬라이드 8–10"
    _by["c-lda"]["detail"] += '<p><b>생체 내 α-알킬화</b>(슬 36, 인돌마이신): 효소의 염기·산이 엔올을 만들고 엔올이 <b>SAM</b>(S⁺–CH₃)의 메틸을 S<sub>N</sub>2로 받음 = 생체판 “LDA + CH₃I”.</p>'
    _by["c-lda"]["title"] = "LDA 직접 알킬화 · 위치 선택성 · 생체 내 알킬화"
    ENTRIES = [e for e in ENTRIES if e.get("id") not in ("c-rate", "c-bio")]
    for e in ENTRIES:
        if e["t"] == "c" and e.get("id") in _x.NOTE:
            e["my"] = _x.NOTE[e["id"]]; e["rec"] = _x.REC.get(e["id"], "")
            e["side"] = [x for x in e.get("side", []) if x[0] in ("img", "trap")]
            if e["id"] == "c-acidbr":
                e["side"] = [(x[0], x[1], x[2], 105) if x[0] == "img" else x for x in e["side"]]
    _n = 0
    for e in ENTRIES:
        if e["t"] != "q":
            continue
        _n += 1
        e["n"] = _n
        if _n in _ans.A:
            e["a"], e["exp"] = _ans.A[_n]
            e["steps"] = []; e["one"] = None
        keep = _ans.KEEP.get(_n, "")
        key, sol = _split(e.get("extra", ""))
        we = e.get("extra", "") if "we" in keep else ""
        e["extra"] = (key if "key" in keep else "") + (sol if "ss" in keep else "") + we
        if "img" in keep:
            e["extra"] += (e.get("afig", "") if e.get("afig", "").startswith("<img") else e.get("afig", "").split("<div class=\"mrow")[0])
        if "afig" not in keep or _n in (12, 20):
            e["afig"] = "" if "afig" not in keep else e.get("afig", "")
        if _n == 27:
            e["afig"] = _MSR('a54', 0, 1, 2)
            e["extra"] = '<img src="../강의번역/img/a54.jpg" style="width:100%">'
        if _n == 28:
            e["afig"] = (_RX(('m', 'CCOC(=O)Cc1ccccc1', 110, 60), ('t', '①'), ('m', 'CCOC(=O)C(=O)C(c1ccccc1)C(=O)OCC', 140, 85), ('t', '②'),
                             ('m', 'CCOC(=O)C(CC)(c1ccccc1)C(=O)OCC', 130, 85), ('t', '③')) + _MSR(33, 2))
        e["pair"] = _n in _ans.PAIR
        e["split"] = _n in _ans.SPLIT
    # 문제 29–31 삭제 (사용자 요청)
    ENTRIES = [e for e in ENTRIES if not (e["t"] == "q" and e.get("n", 0) > 28)]

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
    prob = f'<div class="pbx{" top g" + str(_tr[1]) if _tr else ""}"><span class="plb">PROBLEM {n:02d}</span>{tb(e.get("n"), True)}{kinds}{src}<div class="qtext">{e["q"]}</div></div>'
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

# 시험 직전 TOP 10 — 출제 확률 순서 (문제 번호 → 순위, 등급)
TOPR = {27: (1, 1), 20: (2, 1), 13: (3, 1), 12: (4, 1), 7: (5, 2), 28: (6, 2), 23: (7, 2), 14: (8, 3), 6: (9, 3), 26: (10, 3), 24: (10, 3)}
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


def notepage(i, e):
    n = e["n"]
    return f'''<section class="page v21 npage n{n}">
{_hd21(f"{n:02d}", e["title"] + " — 문제 + 내 필기", "문제를 보면서 삼성노트 텍스트상자 필기 읽기", [e["part"]], top=tb(e.get("n")))}
{_qv(e, n)[0]}
<div class="nbox"><div class="mnote big"><div class="mnt">✍ 내 필기 (삼성노트)</div>{_NOTE[n][1]}</div></div>
{foot(i)}</section>'''


TOP10 = """
<div class="h21"><div class="b21"><span>최종</span><b>③</b></div><div class="tt"><h1>시험 직전 TOP 10 — 출제 확률 순서</h1><div class="sb">문제 01–28 중 이 10개만 순서대로 풀면 나머지 18개는 자동으로 풀린다 (구글 아르곤4 추천)</div></div><div class="pills"><span class="pill">시험 직전</span></div></div>
<div class="tgrid">
<div class="tc t1"><div class="tct">🥇 1등급 — 무조건 100% 출제! 자다가도 풀어야 할 4문제 (과제 4인방)</div>
<p class="tsub">교수님이 수업 마지막에 직접 “풀어서 제출하라”고 찍어주신 과제 4문제. 그대로 나오거나 숫자/작용기만 살짝 바뀌어서 무조건 나온다!</p>
<div class="tr"><span class="rk">1위</span><div><b>문제 27</b> (과제 22-54, p.{QP:27}) — <b>[22장 최종 보스]</b><br>a(β-케토 에스터 위치 지정 알킬화) → b(가열 탈카르복실화) → c(LDA 한산한 쪽 알킬화) 3단 콤보를 한 문제로 물어보는 최고의 명품 문제.</div></div>
<div class="tr"><span class="rk">2위</span><div><b>문제 20</b> (과제 22-42, p.{QP:20}) — <b>[생성물 예측 4종 세트]</b><br>탈카르복실화(a), 다이케톤 알킬화(b), HVZ 물 넣기 전(–COBr)/후(–COOH) 구분(c), 할로폼 반응 CHI₃(d)까지 22장 핵심 반응 4개를 한 판에.</div></div>
<div class="tr"><span class="rk">3위</span><div><b>문제 13</b> (과제 22-38, p.{QP:13} 왼쪽) — <b>[산성도 줄 세우기]</b><br>에탄올(16) &gt; 아세톤(19) 순서 역전 함정 서술형과 염소 3개 유발 효과(CCl₃COOH)까지 산 세기 문제의 정석.</div></div>
<div class="tr"><span class="rk">4위</span><div><b>문제 12</b> (과제 22-37, p.{QP:12}) — <b>[산성 수소 모두 찾기]</b><br>(c)번의 알코올 –OH와 삼중결합 건너편 끝 –CH₃ 공명 함정 때문에 출제율 99%. (이거 하나만 풀면 문제 01, 02, 08, 09는 안 봐도 된다!)</div></div>
</div>
<div class="tcol">
<div class="tc t2"><div class="tct">🥈 2등급 — 약대 전공 특화 &amp; 서술형/빈칸 1순위 (3문제)</div>
<div class="tr"><span class="rk">5위</span><div><b>문제 07</b> (부프로피온 합성, p.{QP:7}) — <b>[의약품 빈칸 1호]</b> 교수님이 “문제를 많이 풀어봐야 한다, 거꾸로 가보라”며 직접 칠판에 풀어주신 문제! 빈칸 3개와 S<sub>N</sub>2 화살표는 필수 암기.</div></div>
<div class="tr"><span class="rk">6위</span><div><b>문제 28</b> (페노바르비탈 합성, p.{QP:28}) — <b>[의약품 빈칸 2호]</b> 왜 Ph–Br을 못 써서 우회하는지(서술형) + 빈칸 3개 + 요소가 에스터 치고 들어가 고리 닫는 메커니즘 화살표.</div></div>
<div class="tr"><span class="rk">7위</span><div><b>문제 23</b> (본문 22-14, p.{QP:23}) — <b>[합성 불가능한 이유 3대장]</b> 알킬화의 3대 제약 조건(① 아릴 할라이드 S<sub>N</sub>2 불가 ② 탄소 3개 골격 유지 ③ 산성 수소 2개 제한)을 한 번에. (이거 하나면 문제 15, 18이 자동 해결!)</div></div>
</div>
<div class="tc t3"><div class="tct">🥉 3등급 — 실전 응용력을 완성해 주는 알짜배기 (3문제)</div>
<div class="tr"><span class="rk">8위</span><div><b>문제 14</b> (염기 고르기, p.{QP:14} 오른쪽) — 짝산 pK<sub>a</sub> 시소 법칙! 언제 NaOEt를 쓰고 언제 LDA를 쓰는지 확실하게.</div></div>
<div class="tr"><span class="rk">9위</span><div><b>문제 06</b> (본문 22-6, p.{QP:6}) — <b>[HVZ + 메탄올 변형]</b> HVZ 마지막에 물 대신 메탄올(CH₃OH)을 넣어 에스터로 끝내는 변형. 메커니즘 그리기 시험으로 내기 아주 좋다.</div></div>
<div class="tr"><span class="rk">10위</span><div><b>문제 26</b> (본문 22-16, p.{QP:26}) 또는 <b>문제 24</b> (고리 만들기, p.{QP:24}) — LDA 직접 알킬화 ‘가지치기’(26)와 Br(CH₂)₄Br로 5각형 고리 만드는 법(24)만 눈에 익혀두면 역합성 설계는 끝!</div></div>
</div>
</div>
</div>
<div class="one"><span class="lb">💡 한 줄 요약 (이 번호만 접어두기)</span><span>1순위(과제): 27 → 20 → 13 → 12 · 2순위(의약품·함정): 07 → 28 → 23 · 3순위(응용): 14 → 06 → 26 (또는 24)</span></div>
"""

def raw(i, e):
    return f'<section class="page {e.get("cls","")}">{e["html"]}{foot(i)}</section>'

pages = []
PID = {}
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
            nxt = ENTRIES[ENTRIES.index(e) + 1] if e.get("pair") else None
            if nxt is not None and nxt["t"] == "q":
                qn += 1; pages.append(question2(i, qn, e, nxt)); qn += 1; nxt["_skip"] = True; nxt_used = nxt
            else:
                qn += 1; _r = question1(i, qn, e); pages.extend(_r if isinstance(_r, list) else [_r])
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
    if e["t"] == "q" and e.get("pair") and nxt_used is not None and nxt_used.get("id"):
        PID[nxt_used["id"]] = (len(pages), qn, "q")
    pk = e.get("part")
    if pk and e["t"] in "cq":
        r = rng.setdefault(pk, {"p": [i, i], "c": [], "q": []})
        r["p"][1] = i
        r["c" if e["t"] == "c" else "q"].append(cn if e["t"] == "c" else qn)
import re
if os.environ.get("ED") != "core":
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
from themes import THEMES as _TH
CSS = CSS + _TH[os.environ.get('THEME', 'mid21')]
html = f'<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>{TITLE}</title><style>{CSS}</style></head><body>{html}</body></html>'
open(os.path.join(D, "index.html"), "w").write(html)
print("pages", len(pages), "concepts", cn, "questions", qn)
