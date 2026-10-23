# -*- coding: utf-8 -*-
# 2–7주차 통합 마스터 요약본 — 공통 헬퍼 + 자동 배치(측정 → 2개씩 묶기)
import os, json, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
FOOT = '물리약학 2–7주차 통합 마스터 요약본 · 중간고사 범위'
ITEMS = []          # 순서대로 쌓이는 항목
PARTNAME = {0: '시작', 1: 'PART 1 · 용해도 · 분배 (2주차)', 2: 'PART 2 · 착물 · 단백질 결합 (3주차)',
            3: 'PART 3 · 확산 (4–6주차)', 4: 'PART 4 · 붕해 · 용출 · 방출 (7주차)', 5: '마무리'}


def J(t): return f'<span class="jk">[즉, {t}]</span>'
def ul(xs): return '<ul>' + ''.join(f'<li>{x}</li>' for x in xs) + '</ul>'
def sh(t): return f'<div class="sh">{t}</div>'
def ana(t, label='🍬 비유'): return f'<div class="ana"><span class="t">{label}</span>{t}</div>'
def warn(t, label='⚠️ 함정'): return f'<div class="warn"><b>{label}</b>{t}</div>'
def mynote(h, label='📝 내 필기'): return f'<div class="mynote"><span class="nl">{label}</span>{h}</div>'
def fixnote(t): return f'<div class="fixnote"><b>🔧 바로잡기</b>{t}</div>'


def fbox(f, s=''):
    return f'<div class="fbox"><div class="f">{f}</div>' + (f'<div class="s">{s}</div>' if s else '') + '</div>'


def tbl(head, rows):
    h = ''.join(f'<th>{c}</th>' for c in head)
    b = ''.join('<tr>' + ''.join(f'<td>{c}</td>' for c in r) + '</tr>' for r in rows)
    return f'<table><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table>'


def img(name, cap='', h=None):
    st = f' style="max-height:{h}px"' if h else ''
    return f'<div class="img"><img src="img/{name}"{st}>' + (f'<div class="cap">{cap}</div>' if cap else '') + '</div>'


def fig(svg, cap=''):
    return f'<div class="fig">{svg}' + (f'<div class="cap">{cap}</div>' if cap else '') + '</div>'


KIND = {'see': ('👀', '단서'), 'ask': ('🤔', '질문'), 'link': ('💡', '연결'), 'calc': ('🧮', '계산'), 'chk': ('🔍', '함정 체크'), 'done': ('✅', '결론')}


def flow(items):
    out = ''
    for k, t in items:
        ic, tg = KIND[k]
        out += f'<div class="fl k-{k}"><span class="ic">{ic}</span><div class="tx"><span class="tg">{tg}</span>{t}</div></div>'
    return out


def ex(q, items):
    return f'<div class="ex"><div class="q">Q. {q}</div>{flow(items)}</div>'


# ------------------------------------------------------------ 항목 생성
def page(part, html):
    ITEMS.append({'kind': 'page', 'part': part, 'html': html})


def concept(part, title, en, core, body, brain, force_wide=False):
    ITEMS.append({'kind': 'cc', 'part': part, 'title': title, 'en': en, 'core': core, 'body': body, 'brain': brain, 'wide': force_wide})


def prob(part, title, src, q, chs, ans, fl, brain='', sg=False, one=False, extra='', qimg=''):
    ITEMS.append({'kind': 'pr', 'part': part, 'title': title, 'src': src, 'q': q, 'chs': chs, 'ans': ans, 'fl': fl,
                  'brain': brain, 'sg': sg, 'one': one, 'extra': extra, 'qimg': qimg})


def divider(part, title, q, items):
    li = ''.join(f'<div><span>{a}</span>{b}</div>' for a, b in items)
    page(part, f'<section class="page div p{part}"><div class="big">PART {part}</div><h2>{title}</h2><div class="q">{q}</div><div class="list">{li}</div>{{FOOT}}</section>')


# ------------------------------------------------------------ 렌더
def cc_html(it, no, wide=False):
    return (f'<div class="cc p{it["part"]}{" wide" if wide else ""}"><div class="ch"><span class="no">개념 {no:02d}</span><div><div class="tt">{it["title"]}</div>'
            f'<div class="en">{it["en"]}</div></div></div><div class="core"><span class="lab">💡 핵심</span>{it["core"]}</div>'
            f'<div class="body">{it["body"]}</div><div class="brain"><span class="lab">🧠 한 줄</span>{it["brain"]}</div></div>')


def pr_html(it, no):
    ch = ''
    if it['chs']:
        one = ' one' if (it['one'] or max(len(c) for c in it['chs']) > 22) else ''
        ch = f'<div class="chs{one}">' + ''.join(f'<div>{"①②③④⑤"[i]} {c}</div>' for i, c in enumerate(it['chs'])) + '</div>'
    sgc = ' sg' if it['sg'] else ''
    b = f'<div class="brain"><span class="lab">🧠 한 줄</span>{it["brain"]}</div>' if it['brain'] else ''
    return (f'<div class="prow p{it["part"]}"><div class="pq"><div class="qcard"><div class="qh"><span class="n">문제 {no:02d}</span><span class="s{sgc}">{it["src"]}</span>'
            f'<span class="t">{it["title"]}</span></div><div class="qq">{it["q"]}</div>{ch}{it["qimg"]}</div><div class="mine"><span>✏️ 내 풀이</span></div></div>'
            f'<div class="sol"><div class="ans"><span class="lb">정답</span>{it["ans"]}</div><div class="sh">🧭 사고의 흐름</div>{flow(it["fl"])}{it["extra"]}{b}</div></div>')


def ptop(part, label, right):
    return f'<div class="ptop"><span class="pl">{label}</span><span class="pt">{PARTNAME[part]}</span><span class="pr">{right}</span></div>'


def foot():
    return f'<div class="foot"><span>{FOOT}</span><span>{{PN}}</span></div>'


def build(out_name='out'):
    css = open(os.path.join(HERE, 'style4.css'), encoding='utf-8').read()
    # 번호 매기기
    cn = pn = 0
    for it in ITEMS:
        if it['kind'] == 'cc':
            cn += 1; it['no'] = cn
        elif it['kind'] == 'pr':
            pn += 1; it['no'] = pn
    # 1) 측정
    blocks = []
    for i, it in enumerate(ITEMS):
        if it['kind'] == 'cc':
            blocks.append(f'<div class="m" data-i="{i}" data-w="n" style="width:{COLW}px">{cc_html(it, it["no"])}</div>')
            blocks.append(f'<div class="m" data-i="{i}" data-w="w" style="width:{FULLW}px">{cc_html(it, it["no"], True)}</div>')
        elif it['kind'] == 'pr':
            blocks.append(f'<div class="m" data-i="{i}" data-w="r" style="width:{FULLW}px">{pr_html(it, it["no"])}</div>')
    mhtml = f'<!doctype html><html><head><meta charset="utf-8"><style>{css} .m{{margin:0 0 40px; --c:#333}}</style></head><body style="padding:10px">{"".join(blocks)}</body></html>'
    open(os.path.join(HERE, 'measure.html'), 'w', encoding='utf-8').write(mhtml)
    res = subprocess.run(['node', os.path.join(HERE, 'measure.js'), HERE], capture_output=True, text=True)
    hs = json.loads(res.stdout)
    H = {}
    for k, v in hs.items():
        i, w = k.split(':'); H[(int(i), w)] = v
    # 2) 배치
    pages = []
    i = 0
    n = len(ITEMS)
    while i < n:
        it = ITEMS[i]
        if it['kind'] == 'page':
            pages.append(it['html']); i += 1; continue
        if it['kind'] == 'cc':
            h1 = H[(i, 'n')]
            nxt = ITEMS[i + 1] if i + 1 < n else None
            if not it['wide'] and h1 <= AVAIL and nxt and nxt['kind'] == 'cc' and not nxt['wide'] and H[(i + 1, 'n')] <= AVAIL and nxt['part'] == it['part']:
                body = f'<div class="grid2">{cc_html(it, it["no"])}{cc_html(nxt, nxt["no"])}</div>'
                pages.append(f'<section class="page p{it["part"]}">{ptop(it["part"], "개념", f"개념 {it["no"]:02d}–{nxt["no"]:02d}")}{body}{foot()}</section>')
                i += 2
            else:
                # 전체 폭 카드를 세로로 쌓기 (같은 PART에서 들어가는 만큼)
                group = [i]; tot = H[(i, 'w')]
                j = i + 1
                while j < n and ITEMS[j]['kind'] == 'cc' and ITEMS[j]['part'] == it['part'] and tot + 12 + H[(j, 'w')] <= AVAIL:
                    # 다음 둘이 나란히 들어가는 편이 낫다면 멈춤
                    if j + 1 < n and ITEMS[j + 1]['kind'] == 'cc' and ITEMS[j + 1]['part'] == it['part'] and max(H[(j, 'n')], H[(j + 1, 'n')]) <= AVAIL and len(group) >= 1 and H[(j, 'w')] > 330:
                        break
                    group.append(j); tot += 12 + H[(j, 'w')]; j += 1
                body = '<div style="display:flex;flex-direction:column;gap:12px">' + ''.join(cc_html(ITEMS[k], ITEMS[k]['no'], True) for k in group) + '</div>'
                rng = f"개념 {ITEMS[group[0]]['no']:02d}" + (f"–{ITEMS[group[-1]]['no']:02d}" if len(group) > 1 else '')
                pages.append(f'<section class="page p{it["part"]}">{ptop(it["part"], "개념", rng)}{body}{foot()}</section>')
                if H[(i, 'w')] > AVAIL:
                    print('WARN wide overflow', it['title'], H[(i, 'w')])
                i = j
            continue
        if it['kind'] == 'pr':
            h1 = H[(i, 'r')]
            nxt = ITEMS[i + 1] if i + 1 < n else None
            if nxt and nxt['kind'] == 'pr' and nxt['part'] == it['part'] and h1 + H[(i + 1, 'r')] + 22 <= AVAIL:
                body = pr_html(it, it['no']) + pr_html(nxt, nxt['no'])
                rng = f'문제 {it["no"]:02d}–{nxt["no"]:02d}'
                i += 2
            else:
                body = pr_html(it, it['no'])
                rng = f'문제 {it["no"]:02d}'
                if h1 > AVAIL:
                    print('WARN problem overflow', it['title'], h1)
                i += 1
            pages.append(f'<section class="page p{it["part"]}">{ptop(it["part"], "문제", rng)}<div class="pbox" style="height:{AVAIL}px;display:flex;flex-direction:column">{body}</div>{foot()}</section>')
    total = len(pages)
    html = ''.join(p.replace('{FOOT}', foot()).replace('{PN}', f'{k} / {total}') for k, p in enumerate(pages, 1))
    html = html.replace('{PN}', '')
    open(os.path.join(HERE, out_name + '.html'), 'w', encoding='utf-8').write(
        f'<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>물리약학 2–7주차 통합 마스터 요약본</title><style>{css}'
        f'.pbox .prow{{flex:1}} .pbox .prow .pq{{min-height:100%}}</style></head><body>{html}</body></html>')
    print(total, 'pages,', cn, 'concepts,', pn, 'problems')


COLW = 507
FULLW = 1031
AVAIL = 660     # 본문 높이
