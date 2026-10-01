# -*- coding: utf-8 -*-
"""공통 레이아웃 헬퍼: 문제 페이지 / 요약 페이지 HTML 생성"""
import html as _h

PAGES = []          # (kind, html)
COUNTER = {"q": 0}


def esc(s):
    return _h.escape(s, quote=False)


MARKS = {
    "circle": "①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳㉑㉒㉓㉔㉕",
    "hangul": ["ㄱ", "ㄴ", "ㄷ", "ㄹ", "ㅁ", "ㅂ", "ㅅ", "ㅇ", "ㅈ", "ㅊ"],
}


def _mark(style, i):
    if style == "circle":
        return MARKS["circle"][i]
    if style == "paren":
        return f"({i+1})"
    if style == "hangul":
        return MARKS["hangul"][i] + "."
    if style == "alpha":
        return "ABCDEFGHIJ"[i] + "."
    return ""


def opts_html(opts, style="circle", cols=None):
    if not opts:
        return ""
    if cols is None:
        longest = max(len(o) for o in opts)
        cols = 1 if longest > 30 else (2 if longest > 13 else 3)
    items = "".join(
        f'<li><span class="mk">{_mark(style, i)}</span><span>{o}</span></li>' for i, o in enumerate(opts))
    return f'<ul class="opts c{cols}">{items}</ul>'


def exp_html(lines):
    """해설 줄 포맷:
    'O|텍스트' 맞는 보기   'X|텍스트' 틀린 보기   'KEY|' 핵심   'TIP|' 암기팁
    'NOTE|' 교재 정답 관련 주의   그 외: 일반 문단 (HTML 허용)"""
    out = []
    oxbuf = []

    def flush():
        if oxbuf:
            out.append('<div class="oxlist">' + "".join(oxbuf) + "</div>")
            oxbuf.clear()
    for ln in lines:
        if ln.startswith("O|") or ln.startswith("X|") or ln.startswith("?|"):
            m, t = ln[0], ln[2:]
            m = "Q" if m == "?" else m
            lab, body = (t.split("::", 1) + [""])[:2] if "::" in t else ("", t)
            lab_html = f'<b class="lab">{lab}</b>' if lab else ""
            oxbuf.append(
                f'<div class="ox {m}"><span class="ic">{ {"O": "O", "X": "X", "Q": "△"}[m] }</span>'
                f'<span class="tx">{lab_html}{body}</span></div>')
            continue
        flush()
        if ln.startswith("KEY|"):
            out.append(f'<div class="key"><span>핵심</span>{ln[4:]}</div>')
        elif ln.startswith("TIP|"):
            out.append(f'<div class="tip"><span>암기 팁</span>{ln[4:]}</div>')
        elif ln.startswith("NOTE|"):
            out.append(f'<div class="note"><span>⚠ 교재 정답 확인</span>{ln[5:]}</div>')
        else:
            out.append(f'<p>{ln}</p>')
    flush()
    return "".join(out)


def Q(part, topic, src, orig, trans, ans, exp, opts=None, topts=None, mk="circle",
      cols=None, tcols=None, fig=None, figw=34, extra_orig="", extra_trans=""):
    """문제 1페이지"""
    COUNTER["q"] += 1
    n = COUNTER["q"]
    o_html = f'<div class="stem">{orig}</div>{extra_orig}{opts_html(opts, mk, cols)}'
    t_html = f'<div class="stem">{trans}</div>{extra_trans}{opts_html(topts if topts else opts, mk, tcols if tcols else cols)}'
    figpart = ""
    if fig:
        if fig.strip().startswith("<"):
            figpart = f'<div class="afig" style="width:{figw}%">{fig}</div>'
        else:
            figpart = f'<div class="afig" style="width:{figw}%"><img src="img/{fig}"></div>'
    added = ' added' if src.startswith("추가") else ''
    page = f'''
<section class="page qpage {part}">
  <header class="qhead">
    <div class="qno">Q{n:03d}</div>
    <div class="qtopic">{topic}</div>
    <div class="qsrc{added}">{src}</div>
  </header>
  <div class="qrow">
    <div class="card orig"><div class="lbl">원문</div>{o_html}</div>
    <div class="card trans"><div class="lbl">번역 · 쉬운 말</div>{t_html}</div>
  </div>
  <div class="blank"><div class="lbl">✏ 내 풀이</div></div>
  <div class="ans">
    <div class="ahead"><span class="pill">정답</span><span class="aval">{ans}</span></div>
    <div class="abody"><div class="aexp">{exp_html(exp)}</div>{figpart}</div>
  </div>
</section>'''
    PAGES.append(("q", page))


def S(part, kicker, title, body, sub=""):
    """요약/설명 페이지 1장"""
    page = f'''
<section class="page spage {part}">
  <header class="shead">
    <div class="kicker">{kicker}</div>
    <h2>{title}</h2>
    {f'<div class="ssub">{sub}</div>' if sub else ''}
  </header>
  <div class="sbody">{body}</div>
</section>'''
    PAGES.append(("s", page))


def RAW(html):
    PAGES.append(("r", html))


def card(title, body, cls=""):
    return f'<div class="card2 {cls}"><h4>{title}</h4>{body}</div>'


def ul(items):
    return "<ul class='b'>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def table(head, rows, cls=""):
    th = "".join(f"<th>{h}</th>" for h in head)
    trs = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f'<table class="t {cls}"><thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table>'


def img(name, cap="", w=100):
    c = f'<figcaption>{cap}</figcaption>' if cap else ""
    return f'<figure class="fig" style="width:{w}%"><img src="img/{name}">{c}</figure>'


TOC = []   # (group, title, page_index)


def SEC(group, title):
    TOC.append((group, title, len(PAGES)))
