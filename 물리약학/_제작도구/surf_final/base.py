def foot():
    return f'<div class="foot"><span>{FOOT}</span><span>{{PN}}</span></div>'


def J(t):
    return f'<span class="jk">[즉, {t}]</span>'


def sec(emoji, label, html):
    return f'<div class="sec"><div class="sh"><span class="e">{emoji}</span>{label}</div>{html}</div>'


def EXPL(html):
    return sec('📖', '상세 설명', html)


def FORM(html):
    return sec('📐', '중요 공식', html)


def EXAM(html):
    return sec('✍️', '예제 및 풀이', html)


def ana(t, label='🍬 비유'):
    return f'<div class="ana"><span class="t">{label}</span>{t}</div>'


def fbox(f, s=''):
    return f'<div class="fbox"><div class="f">{f}</div>' + (f'<div class="s">{s}</div>' if s else '') + '</div>'


def tbl(head, rows, cls=''):
    h = ''.join(f'<th>{c}</th>' for c in head)
    b = ''.join('<tr>' + ''.join(f'<td>{c}</td>' for c in r) + '</tr>' for r in rows)
    return f'<table class="{cls}"><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table>'


def steps(items):
    out = ''
    for i, it in enumerate(items, 1):
        t, why = (it if isinstance(it, tuple) else (it, ''))
        w = f'<span class="why">👉 왜? {why}</span>' if why else ''
        out += f'<div class="st"><i>Step {i}</i><div>{t}{w}</div></div>'
    return out


def ex(q, st):
    return f'<div class="ex"><div class="q">Q. {q}</div>{steps(st)}</div>'


def warn(t, label='⚠️ 함정'):
    return f'<div class="warn"><b>{label}</b>{t}</div>'


def ul(items):
    return '<ul>' + ''.join(f'<li>{x}</li>' for x in items) + '</ul>'


def fig(svg, cap=''):
    return f'<div class="fig">{svg}' + (f'<div class="cap">{cap}</div>' if cap else '') + '</div>'


def hdr(badge, title, en, part):
    return f'<div class="hdr"><span class="badge">{badge}</span><div><h1>{title}</h1><div class="en">{en}</div></div><span class="part">{part}</span></div>'


PARTS = {0: '읽기 전에', 1: 'PART 1 · 반응 속도 기초', 2: 'PART 2 · 0 · 1 · 2차 반응', 3: 'PART 3 · 복합 반응', 4: 'PART 4 · 온도와 속도',
         5: 'PART 5 · 촉매 · pH · 안정성'}


def concept(part, num, title, en, core, left, right, brain=None, cols='1fr 1fr', dense=False):
    c = f'<div class="core"><span class="lab">💡 핵심 개념</span><span>{core}</span></div>'
    b = f'<div class="brain"><span class="lab">🧠 뇌리에 박히는 한 줄</span><span>{brain}</span></div>' if brain else ''
    pages.append(f'''<section class="page p{part}{' dense' if dense else ''}">{hdr(f'개념 {num:02d}', title, en, PARTS[part])}{c}
<div class="two" style="grid-template-columns:{cols}"><div>{left}</div><div>{right}</div></div>{b}<div style="height:13mm;flex:none"></div>{foot()}</section>''')


def problem(part, n, title, src, q, chs, ans, st, rows=None, brain='', extra=''):
    ch = ''.join(f'<div class="ch">{"①②③④⑤"[i]} {c}</div>' for i, c in enumerate(chs)) if chs else ''
    ct = ''
    if rows:
        ct = '<div class="sh">🔍 보기별 해설</div><table class="ctab"><tbody>' + ''.join(
            f'<tr{" class=ok" if ok else ""}><td class="m">{m}</td><td>{t}</td></tr>' for ok, m, t in rows) + '</tbody></table>'
    b = f'<div class="brain"><span class="lab">🧠 한 줄</span><span>{brain}</span></div>' if brain else ''
    pages.append(f'''<section class="page p{part}">{hdr(f'문제 {n:02d}', title, src, PARTS[part])}
<div class="prob"><div class="pl"><div class="qcard"><span class="lb">문제</span><div class="qq">{q}</div>{ch}</div><div class="mine"><span>✏️ 내 풀이 — 먼저 풀고 오른쪽을 보세요</span></div></div>
<div class="sol"><span class="lb">정답 및 해설</span><div class="ans">정답 : {ans}</div><div class="sh">🪜 Step-by-Step 풀이</div>{steps(st)}{ct}{extra}{b}</div></div>{foot()}</section>''')


def _axes(w, h, x0, y0, x1, y1, xl, yl):
    return (f'<line x1="{x0}" y1="{y1}" x2="{x1}" y2="{y1}" stroke="#333" stroke-width="1.3"/>'
            f'<line x1="{x0}" y1="{y0}" x2="{x0}" y2="{y1}" stroke="#333" stroke-width="1.3"/>'
            f'<text x="{x1}" y="{y1 + 15}" font-size="12" text-anchor="end">{xl}</text>'
            f'<text x="{x0 - 5}" y="{y0 + 10}" font-size="12" text-anchor="end">{yl}</text>')


def _curve(f, x0, x1, y0, y1, n=40):
    pts = []
    for i in range(n + 1):
        t = i / n
        pts.append(f'{x0 + (x1 - x0) * t:.1f},{y1 - (y1 - y0) * f(t):.1f}')
    return 'M' + ' L'.join(pts)

