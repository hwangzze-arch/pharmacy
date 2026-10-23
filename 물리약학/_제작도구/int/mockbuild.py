# -*- coding: utf-8 -*-
# 모의고사: 문제지(2단) → 빠른 정답 → 해설(문제 | 사고의 흐름) , 13px, 페이지 꽉 채우기
import os, json, subprocess, lib
from lib import HERE, flow
from mock import MCQ, OX
import build3css
CSS = build3css.CSS + open(os.path.join(HERE, 'mock.css'), encoding='utf-8').read()
H_IN, COL, GAP = 676, 512, 8
NUM = '①②③④⑤'
PN = {1: '용해도·분배', 2: '착물·단백질 결합', 3: '확산', 4: '붕해·용출·방출'}

# ---- 정답 위치 고르게 (보기 순서가 의미 없는 문제만 회전)
items = [list(m) for m in MCQ]
cnt = [0] * 5
for m in items:
    if m[5]: cnt[m[4]] += 1
for m in items:
    if m[5]: continue
    t = min(range(5), key=lambda k: (cnt[k], k == m[4]))
    ch = m[3]; c = ch.pop(m[4]); ch.insert(t, c); m[4] = t; cnt[t] += 1
print('answer dist', cnt)

def measure(blocks):
    open(os.path.join(HERE, 'measure.html'), 'w', encoding='utf-8').write(
        f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS} .m .prow{{flex:none}} .m .mine{{flex:none;height:34px}} .m .memo{{flex:none;height:0}}</style></head><body>{blocks}</body></html>')
    r = subprocess.run(['node', os.path.join(HERE, 'measure.js'), HERE], capture_output=True, text=True)
    return {int(k.split(':')[0]): v for k, v in json.loads(r.stdout).items()}

def pack(hs, order, cap, minmemo=0):
    pages, cur, used = [], [], 0
    for i in order:
        need = hs[i] + minmemo + (GAP if cur else 0)
        if cur and used + need > cap:
            pages.append(cur); cur, used = [], 0; need = hs[i] + minmemo
        cur.append(i); used += need
    if cur: pages.append(cur)
    return pages

def chs_html(ch):
    one = ' one' if max(len(c) for c in ch) > 15 else ''
    return f'<div class="chs{one}">' + ''.join(f'<div>{NUM[i]} {c}</div>' for i, c in enumerate(ch)) + '</div>'

# ---------- 문제지 카드
cards = []   # (kind, html)
cards.append(('h', '<div class="sec p5"><b>Ⅰ. 객관식</b><span>35문항 · 5지선다 · 가장 알맞은 것 하나</span></div>'))
for n, m in enumerate(items, 1):
    part, top, q, ch = m[:4]
    cards.append(('q', f'<div class="xq p{part}"><div class="xh"><span class="n">{n}</span><span class="tp">{PN[part]}</span></div><div class="qq">{q}</div>{chs_html(ch)}<div class="memo"></div></div>'))
cards.append(('h', '<div class="sec p5"><b>Ⅱ. OX</b><span>15문항 · 옳으면 O, 틀리면 X</span></div>'))
for n, (part, s, a, w) in enumerate(OX, 36):
    cards.append(('o', f'<div class="xo p{part}"><span class="n">{n}</span><div class="st">{s}</div><span class="bub">O · X</span></div>'))
hs = measure(''.join(f'<div class="m" data-i="{i}" style="width:{COL}px;margin-bottom:30px">{h}</div>' for i, (_, h) in enumerate(cards)))
# 2단: 열 단위로 채우고 2열씩 페이지
nq = 36  # 카드 0..35 = 객관식 헤더+35문제
cols = pack(hs, range(nq), H_IN, minmemo=18)
if len(cols) % 2: print('WARN odd mcq cols', len(cols))
book = []
def bpage(pair, extra=''):
    body = ''.join('<div class="col">' + ''.join(cards[i][1] for i in c) + '</div>' for c in pair)
    return f'<section class="page p5"><div class="ptop"><span class="pl">문제지</span><span class="pt">물리약학 중간고사 모의고사</span><span class="pr">제한시간 60분 · 2–7주차</span></div>{extra}<div class="two">{body}</div>{{FOOT}}</section>'
for k in range(0, len(cols), 2):
    book.append(bpage(cols[k:k + 2]))
ox = list(range(nq + 1, len(cards)))
tot = sum(hs[i] for i in ox); acc = 0
for j, i in enumerate(ox):
    acc += hs[i]
    if acc >= tot / 2: sp = j + 1; break
book.append(bpage([ox[:sp], ox[sp:]], cards[nq][1]).replace('class="two"', 'class="two oxb"'))

# ---------- 빠른 정답 + 출제 지도
cells = ''.join(f'<div class="ak p{m[0]}"><b>{n}</b><span>{NUM[m[4]]}</span><i>{m[1]}</i></div>' for n, m in enumerate(items, 1))
oxc = ''.join(f'<div class="ak p{p}"><b>{n}</b><span>{a}</span><i>{s[:16]}…</i></div>' for n, (p, s, a, w) in enumerate(OX, 36))
dist = ' · '.join(f'{NUM[k]} {cnt[k]}개' for k in range(5))
keypage = f'''<section class="page p5"><div class="ptop"><span class="pl">정답</span><span class="pt">빠른 정답표 · 채점 후 틀린 번호만 해설로!</span><span class="pr">객관식 정답 분포 {dist}</span></div>
<div class="kp"><div class="kh">Ⅰ. 객관식 (1–35)</div><div class="akg">{cells}</div><div class="kh">Ⅱ. OX (36–50)</div><div class="akg" style="grid-template-columns:repeat(5,1fr)">{oxc}</div>
<div class="brain"><span class="lab">🎯 출제 포인트</span>교수님 정정 공지 반영 — 공극(ε)은 유효확산계수(εD/τ)와 매트릭스 내 약물 농도(εCs)를 <u>증가</u>, 곡로(τ)는 방출 속도를 <u>저하</u> (33번 · 48번). Bottari Cs ≫ Cv 부분은 "출제하지 않음" 공지대로 제외.</div>
<div class="brain" style="background:#b42318"><span class="lab">📊 점수 읽기</span>45개 이상: 실전 준비 완료 · 38–44개: 틀린 주제만 한 장 정리 다시 · 37개 이하: 통합 요약본의 해당 PART부터 복습</div></div>{{FOOT}}</section>'''

# ---------- 해설 (문제 | 사고의 흐름)
probs = []
for n, m in enumerate(items, 1):
    part, top, q, ch, a, _, fl, br = m
    probs.append({'part': part, 'title': top, 'src': PN[part], 'q': q, 'chs': ch, 'ans': f'{NUM[a]} {ch[a]}', 'fl': fl,
                  'brain': br, 'sg': False, 'one': False, 'extra': '', 'qimg': ''})
def pr(it, no):
    h = lib.pr_html(it, no)
    return h
hp = measure(''.join(f'<div class="m" data-i="{i}" style="width:1039px;margin-bottom:30px">{pr(it, i + 1)}</div>' for i, it in enumerate(probs)))
# 순서 유지, 앞 6개까지 끌어오기
pages, pool = [], list(range(len(probs)))
while pool:
    cur, used = [], 0
    while pool:
        pick = next((k for k, i in enumerate(pool[:6]) if used + hp[i] + (9 if cur else 0) <= H_IN), None)
        if pick is None: break
        i = pool.pop(pick); used += hp[i] + (9 if cur else 0); cur.append(i)
    if not cur: cur = [pool.pop(0)]; print('WARN tall', cur)
    cur.sort(); pages.append((cur, used))
sol = []
for cur, used in pages:
    rows = ''.join(pr(probs[i], i + 1) for i in cur)
    rng = f'{cur[0] + 1}' + (f'–{cur[-1] + 1}' if len(cur) > 1 else '') + '번'
    ps = ' / '.join(PN[p] for p in sorted({probs[i]['part'] for i in cur}))
    sol.append(f'<section class="page p{probs[cur[0]]["part"]}"><div class="ptop"><span class="pl">해설</span><span class="pt">객관식 {rng}</span><span class="pr">{ps}</span></div><div class="pbox">{rows}</div>{{FOOT}}</section>')
print('fill', [round(u / H_IN * 100) for _, u in pages])

# ---------- OX 해설 (2단)
oxcards = [f'<div class="xe p{p}"><div class="eh"><span class="n">{n}</span><span class="a {"o" if a == "O" else "x"}">{a}</span><span class="tp">{PN[p]}</span></div><div class="st">{s}</div><div class="why">💡 {w}</div></div>' for n, (p, s, a, w) in enumerate(OX, 36)]
ho = measure(''.join(f'<div class="m" data-i="{i}" style="width:{COL}px;margin-bottom:30px">{h}</div>' for i, h in enumerate(oxcards)))
tot = sum(ho.values()); half = tot / 2; acc = 0; split = 0
for i in range(len(oxcards)):
    acc += ho[i]
    if acc >= half: split = i + 1; break
oxp = f'<section class="page p5"><div class="ptop"><span class="pl">해설</span><span class="pt">OX 36–50번</span><span class="pr">X 문장은 "어디를 고치면 O가 되나"까지 말해 보기</span></div><div class="two ox">' + \
      '<div class="col">' + ''.join(oxcards[:split]) + '</div><div class="col">' + ''.join(oxcards[split:]) + '</div></div>{FOOT}</section>'
print('ox col h', sum(ho[i] for i in range(split)), sum(ho[i] for i in range(split, len(oxcards))))

out = book + [keypage] + sol + [oxp]
foot = '<div class="foot"><span>물리약학 중간고사 모의고사 · 객관식 35 + OX 15</span><span>{PN}</span></div>'
N = len(out)
html = ''.join(p.replace('{FOOT}', foot.replace('{PN}', f'{k} / {N}')) for k, p in enumerate(out, 1))
open(os.path.join(HERE, 'mock.html'), 'w', encoding='utf-8').write(
    f'<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>물리약학 중간고사 모의고사</title><style>{CSS}</style></head><body>{html}</body></html>')
print(N, 'pages; booklet', len(book), 'sol', len(sol))
