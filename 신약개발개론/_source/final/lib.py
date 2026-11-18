# 기말 통합 상세요약+문제 — 공통 도우미
FOOT = '신약개발개론 · 기말 통합 상세요약 + 문제'
pages = []   # (cls, style, inner)


def page(inner, cls='page', style=''):
    pages.append((cls, style, inner))


def ph(wk, part, ttl, src=''):
    return (f'<div class="ph"><span class="wk">{wk}</span><span class="part">{part}</span>'
            f'<span class="ttl">{ttl}</span><span class="sp"></span>'
            + (f'<span class="src">{src}</span>' if src else '') + '</div>')


def wt(w):
    return f'<span class="wtag">{w}</span>'


def hint():
    return '<span class="hint">교수님 출제 힌트</span>'


def _ans(ans, why, one):
    a = f'<div class="a"><span class="pill">정답</span><span class="v">{ans}</span></div>' if ans else ''
    w = f'<div class="why small">{why}</div>' if why else ''
    o = f'<div class="one">{one}</div>' if one else ''
    return f'<div class="ans">{a}{w}{o}</div>'


def mc(no, w, stem, opts, ans, why='', one='', h=None, extra=''):
    o = ''.join(f'<li>{x}</li>' for x in opts)
    bh = f' style="height:{h}mm;flex:0 0 auto"' if h else ''
    return (f'<div class="q"><div class="q-h"><span class="q-no">{no}</span><span class="tag mc">객관식</span>{wt(w)}{extra}</div>'
            f'<div class="q-b"><div class="stem">{stem}</div><ol class="opt">{o}</ol></div>'
            f'<div class="blank"{bh}></div>{_ans(ans, why, one)}</div>')


def ox(no, w, items, ans, why='', h=None, extra=''):
    li = ''.join(f'<li>{t}<span class="bx">O / X</span></li>' for t in items)
    bh = f' style="height:{h}mm;flex:0 0 auto"' if h else ''
    return (f'<div class="q"><div class="q-h"><span class="q-no">{no}</span><span class="tag ox">O/X</span>{wt(w)}{extra}</div>'
            f'<div class="q-b"><ol class="ox">{li}</ol></div>'
            f'<div class="blank"{bh}></div>{_ans(ans, why, "")}</div>')


def sa(no, w, stem, ans, why='', h=None, extra=''):
    bh = f' style="height:{h}mm;flex:0 0 auto"' if h else ''
    return (f'<div class="q"><div class="q-h"><span class="q-no">{no}</span><span class="tag sa">단답</span>{wt(w)}{extra}</div>'
            f'<div class="q-b"><div class="stem">{stem}</div></div>'
            f'<div class="blank"{bh}></div>{_ans(ans, why, "")}</div>')


def es(no, w, stem, model, h=None, extra=''):
    bh = f' style="height:{h}mm;flex:0 0 auto"' if h else ''
    return (f'<div class="q"><div class="q-h"><span class="q-no">{no}</span><span class="tag es">서술</span>{wt(w)}{extra}</div>'
            f'<div class="q-b"><div class="stem">{stem}</div></div>'
            f'<div class="blank"{bh}></div>'
            f'<div class="ans"><div class="a"><span class="pill">모범답안</span></div><div class="small">{model}</div></div></div>')


def qpage(wk, part, ttl, qs, style='', cols=3):
    grid = 'grid3' if cols == 3 else 'grid2'
    per = cols
    chunks = [qs[i:i + per] for i in range(0, len(qs), per)]
    for ci, ch in enumerate(chunks):
        t = ttl if len(chunks) == 1 else f'{ttl} ({ci + 1}/{len(chunks)})'
        body = ''.join(ch)
        page(ph(wk, part, t) + f'<div class="body {grid}" style="align-content:start">' + body + '</div>', style=style)


def render(path, title):
    out = ['<!doctype html>\n<html lang="ko"><head><meta charset="utf-8">'
           f'<title>{title}</title>'
           '<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700;900&family=Nanum+Pen+Script&display=swap" rel="stylesheet">'
           '<link rel="stylesheet" href="style.css"></head><body>']
    for i, (cls, style, inner) in enumerate(pages):
        st = f' style="{style}"' if style else ''
        if 'lcover' in cls:
            out.append(f'<section class="{cls}">{inner}</section>')
        else:
            out.append(f'<section class="{cls}"{st}>\n{inner}\n<div class="pf"><span>{FOOT}</span><span>{i + 1}</span></div>\n</section>')
    out.append('</body></html>')
    open(path, 'w').write('\n'.join(out))
    return len(pages)
