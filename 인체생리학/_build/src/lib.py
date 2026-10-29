import base64, os
FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'fig')
PAGES = []          # list of (kind, chapter, title, html_fn)
CH = {'no': 0, 'name': '', 'color': '#1c3d7a'}
COLORS = {1: '#0b8f84', 2: '#2b8a3e', 3: '#1971c2', 4: '#5f3dc4', 5: '#c2255c', 6: '#e8590c', 7: '#9c36b5'}
_q = [0]

def img(name, cap='', h='60mm'):
    with open(os.path.join(FIG, name + '.jpg'), 'rb') as f:
        b = base64.b64encode(f.read()).decode()
    c = f'<div class="cap">{cap}</div>' if cap else ''
    return f'<div class="fig"><img style="max-height:{h}" src="data:image/jpeg;base64,{b}">{c}</div>'

def chapter(no, name):
    CH.update(no=no, name=name, color=COLORS[no]); _q[0] = 0

def _head(part, title, note=''):
    p = f'<span class="part">{part}</span>' if part else ''
    return (f'<div class="ph"><span class="chip">{str(CH["no"]) + "장" if CH["no"] else "총정리"}</span>{p}<span class="pt">{title}</span>'
            f'<span class="pl"></span><span class="pn">{note}</span></div>')

def page(part, title, body, note='', cls=''):
    PAGES.append(dict(ch=CH['no'], color=CH['color'], name=CH['name'], title=title,
        html=f'{_head(part, title, note)}<div class="pb {cls}">{body}</div>'))

def raw(html, cls='', title=''):
    PAGES.append(dict(ch=CH['no'], color=CH['color'], name=CH['name'], title=title, html=html, cls=cls))

# ---- building blocks ----
def card(title, body, kind='', icon='', style=''):
    t = f'<div class="ct">{icon + " " if icon else ""}{title}</div>' if title else ''
    return f'<div class="card {kind}" style="{style}">{t}{body}</div>'

def grid(cols, *items, style=''):
    return f'<div class="grid" style="grid-template-columns:{cols};{style}">{"".join(items)}</div>'

def col(*items):
    return f'<div class="col">{"".join(items)}</div>'

def tbl(head, rows, cls=''):
    h = ''.join(f'<th>{x}</th>' for x in head)
    r = ''.join('<tr>' + ''.join(f'<td>{c}</td>' for c in row) + '</tr>' for row in rows)
    return f'<table class="{cls}"><tr>{h}</tr>{r}</table>'

def flow(*steps, small=False):
    s = '<i>→</i>'.join(f'<span>{x}</span>' for x in steps)
    return f'<div class="flow{" sm" if small else ""}">{s}</div>'

def chev(items):
    # items: (title, sub, color)
    s = ''.join(f'<div class="chev" style="background:{c}"><b>{t}</b><small>{u}</small></div>' for t, u, c in items)
    return f'<div class="chevs">{s}</div>'

def eng(lines):
    lines = MEMO_KO.get(CH['no'], lines)
    return card('서술형 핵심 문장 — 이 문장 그대로 외우기', '<ul class="en">' + ''.join(f'<li>{x}</li>' for x in lines) + '</ul>', 'engc', '✍')

# ---- questions ----
TAGS = {'tf': ('T / F', '#0b8f84'), 'mc': ('객관식', '#1971c2'), 'mc2': ('객관식 · 2개', '#5f3dc4'),
        'sa': ('단답', '#e8590c'), 'es': ('서술', '#c92a2a')}

def _qcard(kind, body, ans, exp, stars, extra='', prof=False):
    _q[0] += 1
    lab, colr = TAGS[kind]
    st = '★' * stars + '☆' * (3 - stars)
    pf = '<span class="prof">교수님 예시</span>' if prof else ''
    return (f'<div class="q"><div class="qh"><b>Q{_q[0]}</b><span class="qt" style="background:{colr}">{lab}</span>{pf}{extra}'
            f'<span class="st">{st}</span></div><div class="qb">{body}</div>'
            f'<div class="work"><span>✎ 내 풀이</span></div>'
            f'<div class="ans"><div><span class="ab">정답</span> <b>{ans}</b></div><div class="ex">{exp}</div></div></div>')

def TF(items, ans, exp, stars=2):
    """items: list of (en, ko)"""
    li = ''.join(f'<li><div class="tfr"><div><div class="e">{e}</div><div class="k">{k}</div></div><span class="ox">T / F</span></div></li>' for e, k in items)
    body = f'<div class="e">Mark each statement True (T) or False (F).</div><div class="k">각 문장이 참이면 T, 거짓이면 F.</div><ol class="tfl">{li}</ol>'
    return _qcard('tf', body, ans, exp, stars)

def MC(en, ko, ch, ans, exp, pick=1, stars=2, prof=False):
    nums = '①②③④⑤'
    c = ''.join(f'<li><span class="n">{nums[i]}</span><div><div class="e">{e}</div><div class="k">{k}</div></div></li>' for i, (e, k) in enumerate(ch))
    body = f'<div class="e">{en}</div><div class="k">{ko}</div><ol class="chs">{c}</ol>'
    return _qcard('mc' if pick == 1 else 'mc2', body, ans, exp, stars, prof=prof)

def SA(en, ko, ans, exp, stars=1):
    return _qcard('sa', f'<div class="e">{en}</div><div class="k">{ko}</div>', ans, exp, stars)

def ES(en, ko, model, exp, stars=3):
    _q[0] += 1
    lab, colr = TAGS['es']
    return (f'<div class="q"><div class="qh"><b>Q{_q[0]}</b><span class="qt" style="background:{colr}">{lab}</span>'
            f'<span class="st">{"★" * stars + "☆" * (3 - stars)}</span></div><div class="qb"><div class="e">{en}</div><div class="k">{ko}</div></div>'
            f'<div class="work"><span>✎ 내 풀이</span></div>'
            f'<div class="ans"><div><span class="ab">모범답안</span></div><div class="model">{model}</div><div class="ex">{exp}</div></div></div>')

def load_bank():
    import importlib
    for n in range(1, 8):
        try:
            m = importlib.import_module(f'q{n}')
        except ModuleNotFoundError:
            continue
        BANK[n] = m.PAGES
        if hasattr(m, 'MEMO'):
            MEMO_KO[n] = m.MEMO

BANK = {}; MEMO_KO = {}; _bi = {}

def qpage(part, title, *qs, cols=3):
    ch = CH['no']
    if ch in BANK:
        k = _bi.get(ch, 0); _bi[ch] = k + 1
        pages = BANK[ch][k]
    else:
        pages = [(cols, list(qs))]
    for n, (cl, cards) in enumerate(pages):
        t = f'개념문제 — {title}' + (f' ({n + 1})' if len(pages) > 1 else '')
        page(part, t, f'<div class="qg" style="grid-template-columns:repeat({cl},1fr)">{"".join(cards)}</div>', cls='qp')

def K(*words):
    return '<div class="keys">🔑 핵심어 ' + ''.join(f'<span>{w}</span>' for w in words) + '</div>'

def W(*lines):
    return '<div class="why">' + ''.join(f'<div>{x}</div>' for x in lines) + '</div>'

def memo(cards, warn=None, en=None):
    html = ''.join(f'<div class="mc"><div class="ct">{t}</div>{b}</div>' for t, b in cards)
    body = f'<div class="grid" style="grid-template-columns:repeat({min(len(cards),4)},1fr)">{html}</div>'
    low = []
    if warn: low.append(card('⚠ 함정 TOP 3', warn, 'warn'))
    if en: low.append(eng(en))
    if low: body += grid('1fr 2fr' if len(low) == 2 else '1fr', *low, style='margin-top:3.2mm')
    page('FINAL', f'{CH["no"]}장 암기카드 — 시험 직전 5분', body)
