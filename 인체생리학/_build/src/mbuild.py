import sys, os, json
D = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, D)
import annotate
from mdata import Q
from lib import COLORS

ACC = '#d9622b'
NUM = '①②③④⑤'
TAG = {'tf': ('T / F', '#0b8f84'), 'mc': ('객관식', '#1971c2'), 'mc2': ('객관식 · 2개', '#5f3dc4'), 'sa': ('단답', '#e8590c'), 'es': ('서술', '#c92a2a')}
PART = {'tf': ('PART I', 'True / False', '각 1점'), 'mc': ('PART II', '객관식 — 1개 고르기', '각 2점'), 'mc2': ('PART III', '객관식 — 2개 고르기', '각 3점'),
        'sa': ('PART IV', '단답형', '각 2점'), 'es': ('PART V', '서술형', '각 3.5점')}
for i, q in enumerate(Q):
    q['no'] = i + 1

def chcolor(ch):
    return COLORS[int(ch[0])]

def chtag(ch):
    return f'<span class="mch" style="border-color:{chcolor(ch)};color:{chcolor(ch)}">{ch}장</span>'

PAGES = []
def page(part, title, body, note='', cls=''):
    p = f'<span class="part">{part}</span>' if part else ''
    PAGES.append(dict(title=title, html=f'<div class="ph"><span class="chip">모의고사</span>{p}<span class="pt">{title}</span><span class="pl"></span><span class="pn">{note}</span></div><div class="pb {cls}">{body}</div>'))

def qhead(q):
    lab, c = TAG[q['kind']]
    return f'<div class="qh"><b>{q["no"]}</b><span class="qt" style="background:{c}">{lab}</span>{chtag(q["ch"])}<span class="st">{q["pts"]:g}점</span></div>'

def choices(q):
    return '<ol class="chs">' + ''.join(f'<li><span class="n">{NUM[i]}</span><div><span class="e">{e}</span></div></li>' for i, (e, k) in enumerate(q['choices'])) + '</ol>'

def qcard(q, work):
    body = f'<div class="e">{q["en"]}</div>' + (choices(q) if 'choices' in q else '')
    return f'<div class="q mq">{qhead(q)}<div class="qb">{body}</div><div class="work" style="min-height:{work}mm"><span>✎ 내 풀이</span></div><div class="ansbox">답 <span></span></div></div>'

def by(kind):
    return [q for q in Q if q['kind'] == kind]

# ---------------- 문제지 ----------------
tfs = by('tf')
rows = ''.join(f'<div class="tfrow"><b>{q["no"]}</b>{chtag(q["ch"])}<div class="tfx"><div class="e">{q["en"]}</div></div><div class="tfbox">T &nbsp;/&nbsp; F</div></div>' for q in tfs)
page('PART I', 'True / False — 1~14번 (각 1점)', f'<div class="tfgrid">{rows}</div>', '맞으면 T, 틀리면 F에 동그라미')
for kind, per, work in [('mc', 4, 14), ('mc2', 4, 14), ('sa', 4, 30), ('es', 2, 70)]:
    qs = by(kind); pt = PART[kind]
    for s in range(0, len(qs), per):
        grp = qs[s:s + per]
        cols = 2
        page(pt[0], f'{pt[1]} — {grp[0]["no"]}~{grp[-1]["no"]}번 ({pt[2]})',
             f'<div class="qg mg" style="grid-template-columns:repeat({cols},1fr)">' + ''.join(qcard(q, work) for q in grp) + '</div>', cls='qp')

# ---------------- 정답표 ----------------
cells = ''.join(f'<div class="ak"><span class="akn">{q["no"]}</span><span class="aka">{q["ans"] if q["kind"] in ("tf", "mc", "mc2") else ("서술" if q["kind"] == "es" else "단답")}</span><span class="akp" style="color:{chcolor(q["ch"])}">{q["ch"]}장 · {q["pts"]:g}</span></div>' for q in Q)
chs = {}
for q in Q:
    for c in q['ch'].split('·'):
        chs.setdefault(int(c), []).append(q['no'])
diag = ''.join(f'<tr><td style="color:{COLORS[c]}"><b>{c}장</b></td><td>{", ".join(map(str, sorted(set(v))))}</td><td>{len(set(v))}</td><td class="blank"></td></tr>' for c, v in sorted(chs.items()))
page('ANSWER KEY', '정답표 · 채점 · 약점 진단', f'''<div class="grid" style="grid-template-columns:1.55fr 1fr">
<div class="card"><div class="ct">✅ 빠른 정답표 (단답·서술은 해설 페이지에서 채점)</div><div class="akg">{cells}</div></div>
<div class="col"><div class="card tip"><div class="ct">🧮 배점 (총 100점)</div><table><tr><th>영역</th><th>번호</th><th>배점</th><th>내 점수</th></tr>
<tr><td>True / False</td><td>1–14</td><td>14 × 1 = 14</td><td class="blank"></td></tr><tr><td>객관식 1개</td><td>15–30</td><td>16 × 2 = 32</td><td class="blank"></td></tr>
<tr><td>객관식 2개</td><td>31–38</td><td>8 × 3 = 24</td><td class="blank"></td></tr><tr><td>단답형</td><td>39–46</td><td>8 × 2 = 16</td><td class="blank"></td></tr>
<tr><td>서술형</td><td>47–50</td><td>4 × 3.5 = 14</td><td class="blank"></td></tr><tr><td><b>합계</b></td><td></td><td><b>100</b></td><td class="blank"></td></tr></table>
<p class="sm" style="margin-top:1mm">2개 고르기는 두 개 모두 맞아야 점수. 서술형은 🔑 핵심어 하나당 부분점수로 채점해 보기.</p></div>
<div class="card"><div class="ct">🩺 장별 약점 진단 — 틀린 개수를 적고 마스터 노트의 해당 장으로</div><table><tr><th>장</th><th>문항 번호</th><th>문항 수</th><th>틀린 수</th></tr>{diag}</table></div></div></div>''')

# ---------------- 해설 ----------------
def xcard(q):
    lab, c = TAG[q['kind']]
    if q['kind'] in ('sa', 'es'):
        a = f'<div class="ab2">모범답안</div><div class="model">{q["ans"]}</div>'
    else:
        a = f'<div><span class="ab">정답</span> <b class="big">{q["ans"]}</b></div>'
    why = ''.join(f'<div>{w}</div>' for w in q['why'])
    keys = ('<div class="keys">🔑 핵심어 ' + ''.join(f'<span>{k}</span>' for k in q['keys']) + '</div>') if q['keys'] else ''
    return f'<div class="xq"><div class="qh"><b>{q["no"]}</b><span class="qt" style="background:{c}">{lab}</span>{chtag(q["ch"])}<span class="st">{q["pts"]:g}점</span></div><div class="xk">{q["ko"]}</div>{a}<div class="why">{why}</div>{keys}</div>'

def xpages(part, title, qs, per, cols):
    for s in range(0, len(qs), per):
        grp = qs[s:s + per]
        page(part, f'{title} — {grp[0]["no"]}~{grp[-1]["no"]}번', f'<div class="xg" style="column-count:{cols}">' + ''.join(xcard(q) for q in grp) + '</div>')

xpages('해설 I', '정답·해설 True / False', by('tf'), 7, 3)
xpages('해설 II', '정답·해설 객관식 1개', by('mc'), 6, 3)
xpages('해설 III', '정답·해설 객관식 2개', by('mc2'), 4, 2)
xpages('해설 IV', '정답·해설 단답형', by('sa'), 4, 2)
xpages('해설 V', '정답·해설 서술형', by('es'), 2, 2)

# ---------------- 규칙 적용 + 조립 ----------------
ai = [i for i, p in enumerate(PAGES) if 'ANSWER KEY' in p['html'] or '해설' in p['html'].split('class="pt"')[0]]
new = annotate.annotate_chapter([PAGES[i]['html'] for i in ai], 0)
for i, h in zip(ai, new):
    PAGES[i]['html'] = h

LVF = os.path.join(D, 'mlevels.json')
LV = json.load(open(LVF)) if os.path.exists(LVF) else {}
leaf = "M50 4 L58 28 L80 20 L71 44 L96 50 L73 60 L81 81 L56 71 L53 96 L47 96 L44 71 L19 81 L27 60 L4 50 L29 44 L20 20 L42 28 Z"
leaves = ''.join(f'<svg viewBox="0 0 100 100" style="width:{w}mm;left:{x}mm;top:{y}mm;transform:rotate({r}deg);opacity:{o}"><path d="{leaf}" fill="{c}"/></svg>'
  for w, x, y, r, o, c in [(34, 150, 118, 18, .35, '#f4a582'), (22, 120, 150, -25, .3, '#f9c784'), (18, 262, 128, 40, .32, '#ef8f6b'), (26, 232, 150, -10, .28, '#f7b27a'), (14, 96, 8, 30, .3, '#f4a582'), (12, 185, 40, -35, .25, '#f9c784')])
cnt = {}
for q in Q:
    for c in q['ch'].split('·'):
        cnt[int(c)] = cnt.get(int(c), 0) + 1
strip = ''.join(f'<div style="border-color:{COLORS[c]}"><b>{c}장</b>{cnt.get(c, 0)}문항</div>' for c in range(1, 8))
first = {}
for i, p in enumerate(PAGES):
    k = p['html'].split('class="part">')[1].split('<')[0]
    first.setdefault(k, i + 2)
toc = ''.join(f'<div class="r"><span>{a}</span><span>{b} <small>{c}</small></span><span>{first.get(a, "")}</span></div>' for a, b, c in [
    ('PART I', 'True / False 1–14', '각 1점'), ('PART II', '객관식 1개 15–30', '각 2점'), ('PART III', '객관식 2개 31–38', '각 3점'),
    ('PART IV', '단답형 39–46', '각 2점'), ('PART V', '서술형 47–50', '각 3.5점'), ('ANSWER KEY', '정답표 · 배점 · 약점 진단', ''), ('해설 I', '정답·해설 (보기별 오답 이유)', '')])
cover = f'''<section class="pg cover"><div class="leaves">{leaves}</div><div class="k1">PHAR272 · HUMAN PHYSIOLOGY · MOCK EXAM</div>
<h1>인체생리학<br>1–7장<br><em>통합모의고사</em></h1>
<div class="sub">50문항 · 100점 · 90분</div>
<div class="pills"><span>T/F 14</span><span>객관식 1개 16</span><span>객관식 2개 8</span><span>단답 8</span><span>서술 4</span></div>
<div class="note"><span class="y">실제 시험처럼 90분 타이머를 켜고 풀기.</span><br>
문제는 실제 시험처럼 <b>영어로만</b>, 답은 <b>한글</b>로 쓰기. (한글 번역은 해설 페이지에)<br>
문제지를 다 푼 뒤 <b>정답표</b>로 채점 → <b>해설</b>에서 틀린 보기의 이유 확인 → <b>약점 진단표</b>로 마스터 노트 복습.</div>
<div class="toc toc2"><div class="h">CONTENTS</div>{toc}</div>
<div class="strip">{strip}</div>
<div class="src">인체생리학 1–7장 통합 마스터 노트와 짝을 이루는 실전 모의고사 · 교재 테스트뱅크 유형 + 교수님 예시문제 형식</div></section>'''
css = open(os.path.join(D, 'style.css'), encoding='utf-8').read() + open(os.path.join(D, 'mstyle.css'), encoding='utf-8').read()
secs = [cover]
for i, p in enumerate(PAGES):
    h = p['html']
    if '<div class="pb ">' in h:
        h = h.replace('<div class="pb ">', f'<div class="pb L{LV.get(str(i + 2), -1)}">', 1)
    secs.append(f'<section class="pg" style="--c:{ACC}" data-t="{p["title"]}">{h}<div class="foot"><span>인체생리학 · 1–7장 통합모의고사</span><span>{i + 2}</span></div></section>')
open(os.path.join(D, 'mout.html'), 'w', encoding='utf-8').write(
    f'<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>인체생리학 1–7장 통합모의고사</title><style>{css}</style></head><body>{"".join(secs)}</body></html>')
print('pages', len(secs))
