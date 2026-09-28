# -*- coding: utf-8 -*-
"""HTML/SVG helper functions for the Ch.13 workbook."""
import math, base64, os

HERE = os.path.dirname(os.path.abspath(__file__))

# ---------- symbols ----------
G0 = '<span class="m">ΔG′°</span>'
DG = '<span class="m">ΔG</span>'
K = '<span class="m">K′<sub>eq</sub></span>'
E0 = '<span class="m">E′°</span>'
DE0 = '<span class="m">ΔE′°</span>'
Pi = 'P<sub>i</sub>'


def F(n, d):
    """inline fraction"""
    return f'<span class="frac"><span>{n}</span><span>{d}</span></span>'


def eq(*lines, cls=''):
    """centered block equation(s)"""
    inner = ''.join(f'<div class="eql">{l}</div>' for l in lines)
    return f'<div class="eq {cls}">{inner}</div>'


def align(rows, cls=''):
    """aligned equation rows: list of (lhs, rhs) or (lhs, rhs, note)"""
    h = f'<table class="al {cls}">'
    for r in rows:
        lhs, rhs = r[0], r[1]
        note = r[2] if len(r) > 2 else ''
        h += (f'<tr><td class="l">{lhs}</td><td class="e">{"=" if rhs else ""}</td>'
              f'<td class="r">{rhs}</td><td class="n">{note}</td></tr>')
    return h + '</table>'


def arrow_svg(label='', rev=True, w=92):
    """reaction arrow (⇌ or →) with optional enzyme label on top"""
    if rev:
        body = (f'<line x1="2" y1="17" x2="{w-4}" y2="17" stroke="#334155" stroke-width="1.3"/>'
                f'<path d="M{w-11},12 L{w-3},17" stroke="#334155" stroke-width="1.3" fill="none"/>'
                f'<line x1="4" y1="22" x2="{w-2}" y2="22" stroke="#334155" stroke-width="1.3"/>'
                f'<path d="M11,27 L3,22" stroke="#334155" stroke-width="1.3" fill="none"/>')
    else:
        body = (f'<line x1="2" y1="20" x2="{w-4}" y2="20" stroke="#334155" stroke-width="1.3"/>'
                f'<path d="M{w-11},15 L{w-2},20 L{w-11},25" stroke="#334155" stroke-width="1.3" fill="none"/>')
    lab = f'<text x="{w/2}" y="9" text-anchor="middle" font-size="8.5" fill="#2563eb" font-style="italic">{label}</text>' if label else ''
    return f'<svg class="rxarr" viewBox="0 0 {w} 30" width="{w}" height="30">{lab}{body}</svg>'


def rx(left, right, label='', rev=True, extra='', w=None):
    if w is None:
        w = max(70, int(len(label) * 5.2) + 16)
    ex = f'<span class="rxx">{extra}</span>' if extra else ''
    return f'<div class="rx"><span>{left}</span>{arrow_svg(label, rev, w)}<span>{right}</span>{ex}</div>'


def img(name, width='60%', cap=''):
    p = os.path.join(HERE, 'img', name)
    b64 = base64.b64encode(open(p, 'rb').read()).decode()
    c = f'<figcaption>{cap}</figcaption>' if cap else ''
    return f'<figure class="fig" style="width:{width}"><img src="data:image/png;base64,{b64}"/>{c}</figure>'


def fig(svg, cap='', width=None):
    st = f' style="width:{width}"' if width else ''
    c = f'<figcaption>{cap}</figcaption>' if cap else ''
    return f'<figure class="fig"{st}>{svg}{c}</figure>'


def steps(*items):
    return '<ol class="steps">' + ''.join(f'<li>{i}</li>' for i in items) + '</ol>'


def box(kind, title, body):
    return f'<div class="box {kind}"><span class="bt">{title}</span>{body}</div>'


def key(body):
    return box('key', '핵심', body)


def tip(body, title='비유'):
    return box('tip', title, body)


def warn(body, title='함정 주의'):
    return box('warn', title, body)


def chips(*items):
    return '<div class="chips">' + ''.join(f'<span class="chip">{i}</span>' for i in items) + '</div>'


def table(head, rows, cls=''):
    h = f'<table class="tb {cls}"><thead><tr>' + ''.join(f'<th>{x}</th>' for x in head) + '</tr></thead><tbody>'
    for r in rows:
        h += '<tr>' + ''.join(f'<td>{x}</td>' for x in r) + '</tr>'
    return h + '</tbody></table>'


# ---------- SVG drawings ----------
C = dict(navy='#1e3a8a', blue='#2563eb', sky='#dbeafe', orange='#ea580c', amber='#f59e0b',
         red='#dc2626', green='#16a34a', mint='#dcfce7', gray='#64748b', light='#f1f5f9',
         ink='#1f2937', purple='#7c3aed', pink='#fce7f3', yellow='#fef3c7')


def svg(w, h, body, maxw=None):
    return (f'<svg viewBox="0 0 {w} {h}" style="height:calc(var(--s,1) * var(--fz,0.24mm) * {h});width:auto;max-width:100%" xmlns="http://www.w3.org/2000/svg" '
            f'font-family="Noto Sans KR" font-size="12">{body}</svg>')


def T(x, y, s, size=12, color='#1f2937', anchor='middle', weight=400, italic=False, family=None):
    st = ' font-style="italic"' if italic else ''
    fam = f' font-family="{family}"' if family else ''
    return (f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" text-anchor="{anchor}" '
            f'font-weight="{weight}"{st}{fam}>{s}</text>')


def arrowdef(idn, color):
    return (f'<defs><marker id="{idn}" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" '
            f'orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{color}"/></marker></defs>')


def ladder(entries, lo, hi, hl=(), flows=(), width=520, height=300, title='E′° (V)'):
    """redox ladder. entries: list of (label, value). hl: labels to highlight.
    flows: list of (from_label, to_label, text) electrons from→to"""
    top, bot = 26, height - 22
    def Y(v):
        return bot - (v - lo) / (hi - lo) * (bot - top)
    x0 = 70
    b = arrowdef('ea', C['orange'])
    # gradient axis
    b += (f'<defs><linearGradient id="lg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fca5a5"/>'
          f'<stop offset="1" stop-color="#93c5fd"/></linearGradient></defs>')
    b += f'<rect x="{x0-7}" y="{top}" width="14" height="{bot-top}" rx="7" fill="url(#lg)"/>'
    b += T(x0, top - 10, title, 11, C['gray'], weight=700)
    b += T(x0 - 14, top + 10, '+', 15, C['red'], 'end', 700)
    b += T(x0 - 14, bot, '−', 15, C['blue'], 'end', 700)
    b += T(18, (top + bot) / 2 - 8, '전자를', 10, C['gray'], 'middle')
    b += T(18, (top + bot) / 2 + 6, '받고 싶은', 10, C['gray'], 'middle')
    b += T(18, (top + bot) / 2 + 20, '정도 ↑', 10, C['gray'], 'middle')
    pos = {}
    ys_used = []
    for lab, v in sorted(entries, key=lambda e: -e[1]):
        y = Y(v)
        ty = y
        for u in ys_used:
            if abs(ty - u) < 15:
                ty = u + 15
        ys_used.append(ty)
        pos[lab] = y
        h = lab in hl
        col = C['orange'] if h else C['ink']
        b += f'<line x1="{x0-9}" y1="{y}" x2="{x0+30}" y2="{y}" stroke="{col}" stroke-width="{2.2 if h else 1.2}"/>'
        b += f'<line x1="{x0+30}" y1="{y}" x2="{x0+40}" y2="{ty}" stroke="{col}" stroke-width="0.8"/>'
        b += T(x0 + 44, ty + 4, f'{v:+.3f}'.replace('+0.000', '0.000').replace('-', '−'), 11, col, 'start', 700 if h else 400, family='JetBrains Mono')
        b += T(x0 + 100, ty + 4, lab, 11.5, col, 'start', 700 if h else 400)
    fx = width - 40
    for i, (a, c, t) in enumerate(flows):
        xx = fx - i * 34
        b +=(f'<path d="M{xx-14},{pos[a]} L{xx},{pos[a]} L{xx},{pos[c]} L{xx-14},{pos[c]}" fill="none" '
              f'stroke="{C["orange"]}" stroke-width="2.2" marker-end="url(#ea)"/>')
        b += T(xx + 6, (pos[a] + pos[c]) / 2 + 4, t, 11, C['orange'], 'start', 700)
    return svg(width, height, b)


def logaxis(points, lo, hi, width=520, height=120, label='', marks=None, center=None, center_lab=''):
    """points: list of (value, label, color). log10 axis"""
    L, R = 30, width - 20
    y = 64
    def X(v):
        return L + (math.log10(v) - lo) / (hi - lo) * (R - L)
    b = arrowdef('la', C['gray'])
    b += f'<line x1="{L}" y1="{y}" x2="{R}" y2="{y}" stroke="{C["gray"]}" stroke-width="1.5" marker-end="url(#la)"/>'
    for e in range(lo, hi + 1):
        x = X(10 ** e)
        b += f'<line x1="{x}" y1="{y-4}" x2="{x}" y2="{y+4}" stroke="{C["gray"]}"/>'
        b += T(x, y + 18, f'10<tspan dy="-5" font-size="8">{e}</tspan>', 10, C['gray'], family='Noto Serif')
    if center is not None:
        x = X(center)
        b += f'<line x1="{x}" y1="{y-40}" x2="{x}" y2="{y+26}" stroke="{C["red"]}" stroke-dasharray="4 3"/>'
        b += T(x, y + 38, center_lab, 10.5, C['red'], weight=700)
    for i, (v, lab, col) in enumerate(points):
        x = X(v)
        dy = -24 if i % 2 == 0 else -40
        b += f'<circle cx="{x}" cy="{y}" r="6" fill="{col}" stroke="white" stroke-width="1.5"/>'
        b += f'<line x1="{x}" y1="{y-7}" x2="{x}" y2="{y+dy+4}" stroke="{col}" stroke-width="1"/>'
        b += T(x, y + dy, lab, 11, col, weight=700)
    if label:
        b += T(R, y + 38, label, 10.5, C['gray'], 'end')
    return svg(width, height, b)


def energy_steps(levels, width=520, height=220, unit='kJ/mol', title=''):
    """levels: list of (x_label, G_value, color). draws horizontal platforms with arrows between successive."""
    vals = [v for _, v, _ in levels]
    vmax, vmin = max(vals + [0]), min(vals + [0])
    top, bot = 44, height - 30
    def Y(v):
        return top + (vmax - v) / (vmax - vmin + 1e-9) * (bot - top)
    n = len(levels)
    seg = (width - 80) / n
    b = arrowdef('es', C['ink'])
    b += f'<line x1="50" y1="{top-30}" x2="50" y2="{bot+8}" stroke="{C["gray"]}" stroke-width="1.2" marker-start="url(#es)"/>'
    b += f'<text x="34" y="{(top+bot)/2}" font-size="10" font-weight="700" fill="{C["gray"]}" text-anchor="middle" transform="rotate(-90 34 {(top+bot)/2})">G (자유에너지)</text>'
    for i, (lab, v, col) in enumerate(levels):
        x1 = 60 + i * seg + 8
        x2 = x1 + seg - 16
        y = Y(v)
        b += f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="{col}" stroke-width="5" stroke-linecap="round"/>'
        b += T((x1 + x2) / 2, y - 9, lab, 11.5, col, weight=700)
        if i > 0:
            pv = levels[i - 1][1]
            py = Y(pv)
            xm = x1 - 8
            d = v - pv
            c2 = C['red'] if d > 0 else C['green']
            b += f'<line x1="{xm}" y1="{py}" x2="{xm}" y2="{y + (4 if d < 0 else -4)}" stroke="{c2}" stroke-width="2" marker-end="url(#es)"/>'
            s = f'{d:+.1f}'.replace('-', '−')
            b += T(xm - 6, (py + y) / 2 + 4, s, 11, c2, 'end', 700, family='JetBrains Mono')
    if title:
        b += T(width / 2, height - 8, title, 11, C['gray'])
    return svg(width, height, b)


def bars(items, width=520, height=180, vmax=None, unit='', title='', neg=False):
    """horizontal bars. items: (label, value, color, text)"""
    vm = vmax or max(abs(v) for _, v, _, _ in items)
    L = 150
    bh = 26
    gap = (height - 20) / len(items)
    b = ''
    for i, (lab, v, col, txt) in enumerate(items):
        y = 12 + i * gap
        w = abs(v) / vm * (width - L - 90)
        b += T(L - 10, y + bh / 2 + 4, lab, 11.5, C['ink'], 'end', 700)
        b += f'<rect x="{L}" y="{y}" width="{w}" height="{bh}" rx="5" fill="{col}"/>'
        b += T(L + w + 8, y + bh / 2 + 4, txt, 11.5, col, 'start', 700)
    return svg(width, height, b)


def bubble(text, x, y, w, h, fill='#fff7ed', stroke='#fdba74'):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{fill}" stroke="{stroke}"/>'
            f'{T(x + w / 2, y + h / 2 + 4, text, 11)}')
