# -*- coding: utf-8 -*-
"""시험 직전 막판 29제 — ① 실전 모의고사형  ② 압축판(문제+치트키+해설 한 페이지).
교수님포인트판(final_v3.pdf)의 완성 페이지를 재사용한다."""
import json, os, subprocess, sys
import pymupdf as fitz

HERE = os.path.dirname(os.path.abspath(__file__))
SCR = os.path.join(HERE, '..')
SRC = fitz.open(os.path.join(SCR, 'final_v3.pdf'))
PLAN = {x['key']: x for x in json.load(open(os.path.join(HERE, 'plan_final.json')))}
GRID = json.load(open(os.path.join(SCR, 'grid.json')))
FONT = os.path.expanduser('~/.fonts/Pretendard-SemiBold.otf')
FONTB = os.path.expanduser('~/.fonts/Pretendard-ExtraBold.otf')
PW, PH = 1134.0, 708.96

NAMES = {17: '알코올과 페놀', 18: '에터와 에폭사이드', 19: '알데하이드와 케톤', 20: '카복실산과 나이트릴', 21: '카복실산 유도체'}
COL = {17: '#2a6f97', 18: '#2a9d8f', 19: '#7b5cd6', 20: '#e76f51', 21: '#d1495b'}

# (key, 왜 나올 만한가)
Q = [
    ('17-11', '페놀 + 치환기 → pKa 순서 (교수님 지목)'),
    ('17-14', '산화·환원 시약 고르기'),
    ('17-22', '그리냐르 + 카보닐 → 알코올'),
    ('17-31', '시약 a~f 빈칸 — 산화·환원·그리냐르·탈수 종합'),
    ('18-11', '에터 만드는 법 고르기'),
    ('18-14', 'HBr 에터 절단 생성물'),
    ('18-24', '조건(염기·산·그리냐르)별 개환 위치'),
    ('18-25', '그리냐르 개환 — 위치·입체'),
    ('19-7', '알데하이드 만들기 = 산화·환원 관계'),
    ('19-14', '1차 vs 2차 아민 → 이민 / 엔아민'),
    ('19-36', '1,4-첨가(길만)로 β 자리에 가지'),
    ('19-37', '1,2 vs 1,4 — 교수님 지목 ①'),
    ('19-38', '1,2 vs 1,4 — 교수님 지목 ②'),
    ('20-12', 'pKa 비교 + 이유 (교수님 지목)'),
    ('20-15', '표 없이 산성도 순서'),
    ('20-17', 'R–X → 카복실산: CN 길 vs 그리냐르 길'),
    ('20-27', '빠진 시약 채우기'),
    ('21-7', '간단한 메커니즘 1문제 1순위'),
    ('21-9', '유도체 반응성 순서 + 이유'),
    ('21-10', '친핵체·이탈기 찾아 생성물'),
    ('21-16', '산 조건 가수분해 (수업 강조)'),
    ('21-18', 'DCC 커플링 (수업에서 HOBt까지)'),
    ('21-26', '산 염화물 + 시약 7가지'),
    ('21-32', 'LAH vs DIBAL-H (수업 강조)'),
    ('21-36', '락톤 + 그리냐르 2당량'),
    ('21-38', '아마이드 가수분해 / LAH → 아민'),
    ('21-40', '21장 종합 생성물 ①'),
    ('21-41', '21장 종합 생성물 ②'),
    ('21-44', 'SOCl₂ 활성화 → 아마이드 (DEET)'),
]
FIX = {'20-17': ('20-10', '3차 할로젠화물 vs 1차 할로젠화물 → 카복실산')}


def info(k):
    p = PLAN[k]
    no, title = FIX.get(k, (p['no'], p['title']))
    return dict(key=k, ch=p['ch'], no=no, title=title, kind=p['kind'], src=p['final'])


ITEMS = [dict(info(k), why=w, q=i + 1) for i, (k, w) in enumerate(Q)]
N = len(ITEMS)

BASE_CSS = """
@page { size: 1134pt 708.96pt; margin: 0 }
* { box-sizing: border-box; margin: 0; padding: 0 }
body { font-family: 'Pretendard', 'Noto Color Emoji', sans-serif; color: #1f2633; background: #fff }
.pg { width: 1134pt; height: 708.96pt; page-break-after: always; position: relative; overflow: hidden }
.pg:last-child { page-break-after: auto }
sub { font-size: 70%; vertical-align: -.25em; line-height: 0 }
.foot { position: absolute; right: 30pt; bottom: 14pt; font-size: 8.6pt; color: #6b7686 }
.cv { display: grid; grid-template-columns: 360pt 1fr; height: 100% }
.cv-l { background: linear-gradient(160deg, #3b0d1c, #9c1f45 60%, #d1335b); color: #fff; padding: 40pt 32pt; position: relative }
.cv-l .k { font-size: 10.5pt; letter-spacing: 2pt; font-weight: 700; opacity: .85 }
.cv-l h1 { font-size: 36pt; font-weight: 900; line-height: 1.18; margin: 12pt 0 12pt }
.cv-l h1 em { font-style: normal; color: #ffd166 }
.cv-l .sub { font-size: 12.5pt; line-height: 1.6; opacity: .95 }
.rule { margin-top: 16pt; background: rgba(0,0,0,.2); border-radius: 8pt; padding: 10pt 12pt; font-size: 11pt; line-height: 1.7 }
.rule b { color: #ffd166 }
.cv-l .bot { position: absolute; left: 32pt; right: 32pt; bottom: 30pt; font-size: 9.5pt; opacity: .8; line-height: 1.6 }
.cv-r { padding: 26pt 28pt 26pt 26pt }
.cv-r h2 { font-size: 12.5pt; font-weight: 800; color: #1d3557; margin-bottom: 8pt; display: flex; gap: 8pt; align-items: center }
.cv-r h2:after { content: ''; flex: 1; height: 1pt; background: #dde3ee }
.tb { display: grid; grid-template-columns: 1fr 1fr; gap: 0 18pt }
.r { display: grid; align-items: center; gap: 6pt; padding: 4.1pt 2pt; border-bottom: .7pt dotted #d5dbe6; font-size: 10pt }
.r .q { font-weight: 900; color: #fff; border-radius: 5pt; text-align: center; font-size: 9.6pt; padding: 1pt 0 }
.r .no { font-weight: 800; color: #1d3557; white-space: nowrap }
.r .w { overflow: hidden; white-space: nowrap; text-overflow: ellipsis; color: #3a4556 }
.r .pp { color: #6b7686; font-weight: 700; text-align: right; white-space: nowrap; font-size: 9.2pt }
.ck { display: inline-block; width: 13pt; height: 13pt; border: 1.2pt solid #9aa5b5; border-radius: 3pt }
.chs { display: flex; gap: 6pt; margin-bottom: 10pt; flex-wrap: wrap }
.chp { color: #fff; font-weight: 800; font-size: 10pt; border-radius: 10pt; padding: 3pt 10pt }
"""


def table(mode):
    cols = '24pt 54pt 1fr 52pt' + (' 34pt 34pt' if mode == 'exam' else '')
    head = (f'<div class="r" style="grid-template-columns:{cols};font-size:8.6pt;color:#8a95a5;font-weight:700">'
            f'<span>번호</span><span>출처</span><span>왜 나올 만한가</span><span style="text-align:right">'
            f'{"문제 · 해설" if mode == "exam" else "쪽"}</span>' + ('<span>○</span><span>✗</span>' if mode == 'exam' else '') + '</div>')
    rows = []
    for it in ITEMS:
        pp = f'p.{it["qp"]} · {it["ap"]}' if mode == 'exam' else f'p.{it["ap"]}'
        extra = '<span class="ck"></span><span class="ck"></span>' if mode == 'exam' else ''
        rows.append(f'<div class="r" style="grid-template-columns:{cols}"><span class="q" style="background:{COL[it["ch"]]}">{it["q"]}</span>'
                    f'<span class="no">{it["no"]}</span><span class="w">{it["why"]}</span><span class="pp">{pp}</span>{extra}</div>')
    half = (N + 1) // 2
    return f'<div class="tb"><div>{head}{"".join(rows[:half])}</div><div>{head}{"".join(rows[half:])}</div></div>'


def chips():
    cnt = {c: sum(1 for i in ITEMS if i['ch'] == c) for c in NAMES}
    return '<div class="chs">' + ''.join(f'<span class="chp" style="background:{COL[c]}">{c}장 {NAMES[c]} · {cnt[c]}</span>' for c in NAMES) + '</div>'


RULES = """<div class="rule">📌 교수님 안내 — <b>약 12문제</b>, 단원마다 1~2문제, <b>21장 비중 ↑</b><br>
답이 딱 떨어지는 문제 · 간단한 메커니즘은 <b>한 군데</b> 정도<br>산화·환원 메커니즘, 너무 어려운 문제는 <b>안 냄</b></div>"""


def cover(mode, total):
    if mode == 'exam':
        h1 = '시험 직전<br><em>막판 모의고사</em><br>29제'
        sub = '앞: 문제만 (풀이 칸 포함)<br>뒤: 정답 · 해설 · 치트키 · 🎯 교수님 강조'
        how = ('<b>풀이법</b> — ① 앞쪽 시험지를 시간 재고 푼다 ② 오른쪽 표 ○/✗에 채점 ③ ✗ 문항만 뒤쪽 해설 쪽으로 가서 치트키까지 확인'
               '<br>⏱ 실제 12문제 기준으로 한 문제 4~5분 감각으로')
        bot = '문제 쪽 머리말의 힌트 문구(제목·태그)는 가렸다. 해설 쪽은 교수님포인트판 페이지 그대로.'
    else:
        h1 = '시험 직전<br><em>막판 29제</em><br>압축판'
        sub = '한 페이지 = 문제 + 🎯 교수님 강조 + ⚡ 치트키 + 해설<br>시험장 들어가기 직전 훑어보기용'
        how = '<b>보는 법</b> — 문제 → 분홍 띠(교수님 강조) → 치트키 → 해설 순서로. 메모 칸은 S펜용.'
        bot = '교수님포인트판(102문항)에서 실제 시험에 나올 만한 유형만 골랐다.'
    return f'''<div class="pg"><div class="cv"><div class="cv-l"><div class="k">약품유기화학 2 · 중간고사 17–21장</div>
<h1>{h1}</h1><div class="sub">{sub}</div>{RULES}<div class="bot">{bot}</div></div>
<div class="cv-r"><h2>문항 지도 · 29문제 = 실제 12문제의 약 2.5배</h2>{chips()}{table(mode)}
<div style="margin-top:10pt;font-size:10.2pt;line-height:1.6;color:#3a4556">{how}</div></div></div>
<div class="foot">1 / {total}</div></div>'''


EXAM_CSS = """
.hd { position: absolute; left: 27pt; right: 27pt; top: 14pt; height: 46pt; display: flex; align-items: center; gap: 12pt; border-bottom: 2.4pt solid #1d3557 }
.hd .qb { color: #fff; font-weight: 900; font-size: 22pt; border-radius: 9pt; padding: 2pt 14pt; line-height: 1.25 }
.hd .t { font-size: 15pt; font-weight: 800; color: #1d3557 }
.hd .s { font-size: 10pt; color: #6b7686; margin-top: 1pt }
.hd .rt { margin-left: auto; font-size: 10pt; color: #6b7686; text-align: right; line-height: 1.4 }
.ans { position: absolute; left: 27pt; right: 27pt; border: 1pt dashed #c3cad6; border-radius: 8pt;
  background-color: #fff; background-image: linear-gradient(#eef1f6 .7pt, transparent .7pt), linear-gradient(90deg, #eef1f6 .7pt, transparent .7pt); background-size: 14pt 14pt }
.ans .l { position: absolute; left: 10pt; top: 6pt; font-size: 9.5pt; color: #8a97ab; background: #fff; padding: 0 4pt }
.fin { position: absolute; left: 27pt; right: 27pt; height: 40pt; border: 1.6pt solid #1d3557; border-radius: 8pt; display: flex; align-items: center; gap: 12pt; padding: 0 14pt; background: #fff }
.fin b { font-size: 12pt; color: #1d3557; white-space: nowrap }
.fin .ln { flex: 1; border-bottom: 1pt solid #c3cad6; height: 18pt }
.fin .self { font-size: 10pt; color: #6b7686; white-space: nowrap }
.dv { height: 100%; display: flex; flex-direction: column; justify-content: center; align-items: center; background: linear-gradient(160deg,#1d3557,#2b4c7e); color: #fff }
.dv h1 { font-size: 46pt; font-weight: 900 } .dv p { font-size: 14pt; opacity: .9; margin-top: 10pt; text-align: center; line-height: 1.7 }
"""

TOP = 66.0   # 원본 페이지에서 문제 상자가 시작하는 높이
DST = 70.0   # 시험지에서 문제 상자를 놓을 높이


def exam_page(it, pageno, total):
    g = GRID[it['key']]['grid'][1]
    h = g - 6 - TOP
    ay = DST + h + 8
    fin_y = PH - 30 - 40
    return f'''<div class="pg"><div class="hd"><span class="qb" style="background:{COL[it["ch"]]}">Q{it["q"]}</span>
<div><div class="t">{it["ch"]}장 · {NAMES[it["ch"]]}</div><div class="s">출처 {it["no"]} ({it["kind"]})</div></div>
<div class="rt">막판 모의고사 {it["q"]} / {N}<br>해설 → p.{it["ap"]}</div></div>
<div class="ans" style="top:{ay:.1f}pt;height:{fin_y - 8 - ay:.1f}pt"><span class="l">✍ 풀이</span></div>
<div class="fin" style="top:{fin_y:.1f}pt"><b>최종 답</b><span class="ln"></span><span class="self">채점 ○ / ✗ &nbsp; 걸린 시간 ____ 분</span></div>
<div class="foot">{pageno} / {total}</div></div>'''


def render(html, out):
    p = os.path.join(HERE, out.replace('.pdf', '.html'))
    open(p, 'w').write(html)
    subprocess.run(['node', os.path.join(HERE, 'render.js'), p, os.path.join(HERE, out), '-', '1134', '708.96'], check=True)
    return fitz.open(os.path.join(HERE, out))


_STRIPS = {}


def footer_strip(it, label):
    key = (it['q'], label)
    if key not in _STRIPS:
        html = ('<!doctype html><html><head><meta charset="utf-8"><style>@page{size:440pt 20pt;margin:0}*{margin:0;padding:0}'
                "body{font-family:'Pretendard',sans-serif;width:440pt;height:20pt;display:flex;align-items:center;gap:6pt;padding-left:7pt;font-size:8.6pt;color:#6b7686;background:#fff}"
                f"b{{color:{COL[it['ch']]};font-size:10pt;font-weight:900}}</style></head><body><b>Q{it['q']}</b><span>{label} · 출처 {it['no']} · {it['why']}</span></body></html>")
        p = os.path.join(HERE, 'strip.html')
        open(p, 'w').write(html)
        subprocess.run(['node', os.path.join(HERE, 'render.js'), p, os.path.join(HERE, 'strip.pdf'), '-', '440', '20'], check=True)
        d = fitz.open(os.path.join(HERE, 'strip.pdf'))
        _STRIPS[key] = fitz.open('pdf', d.tobytes())
    return _STRIPS[key]


def stamp_answer_page(pg, it, pageno, total, label):
    """해설 쪽 꼬리말: 왼쪽 출처 문구 → 'Qn · 정답과 해설', 오른쪽 쪽번호 교체."""
    ph = pg.rect.height
    for r in pg.search_for('맥머리'):
        if r.y0 > ph - 40:
            pg.draw_rect(fitz.Rect(20, r.y0 - 2, 520, r.y1 + 2), color=None, fill=(1, 1, 1))
    old = f'{it["src"]} / 110'
    for r in pg.search_for(old):
        if r.y0 > ph - 40:
            pg.draw_rect(fitz.Rect(r.x0 - 4, r.y0 - 1, r.x1 + 3, r.y1 + 1), color=None, fill=(1, 1, 1))
    strip = footer_strip(it, label)
    pg.show_pdf_page(fitz.Rect(20, ph - 28, 460, ph - 8), strip, 0)
    txt = f'{pageno} / {total}'
    tw = fitz.get_text_length(txt, fontname='helv', fontsize=8.6)
    pg.insert_text((1107 - tw, ph - 15.6), txt, fontsize=8.6, fontname='helv', color=(0.42, 0.46, 0.53))


def build_compact(path):
    total = 1 + N
    for i, it in enumerate(ITEMS):
        it['ap'] = 2 + i
    covdoc = render(f'<!doctype html><html><head><meta charset="utf-8"><style>{BASE_CSS}</style></head><body>{cover("compact", total)}</body></html>', 'c29_cover.pdf')
    out = fitz.open()
    out.insert_pdf(covdoc)
    toc = [[1, '표지 · 문항 지도', 1]]
    for it in ITEMS:
        out.insert_pdf(SRC, from_page=it['src'] - 1, to_page=it['src'] - 1)
        stamp_answer_page(out[-1], it, it['ap'], total, '막판 29제 압축판')
        toc.append([1, f'Q{it["q"]}  {it["no"]}  {it["title"]}', it['ap']])
    out.set_toc(toc)
    out.set_metadata({'title': '약품유기화학2 중간고사 막판 29제 (압축판)', 'author': 'hwangzze'})
    out.save(path, garbage=4, deflate=True, use_objstms=1)
    print('compact', len(out))


def build_exam(path):
    total = 1 + N + 1 + N
    for i, it in enumerate(ITEMS):
        it['qp'] = 2 + i
        it['ap'] = 2 + N + 1 + i
    pages = [cover('exam', total)] + [exam_page(it, it['qp'], total) for it in ITEMS]
    pages.append(f'''<div class="pg"><div class="dv"><h1>정답 · 해설</h1><p>채점하고 ✗ 문항부터 보기<br>각 페이지 = 해설 + 🎯 교수님 강조 + ⚡ 치트키 (+ 📝 내 필기)</p></div>
<div class="foot" style="color:#c9d3ea">{2 + N} / {total}</div></div>''')
    shell = render(f'<!doctype html><html><head><meta charset="utf-8"><style>{BASE_CSS}{EXAM_CSS}</style></head><body>{"".join(pages)}</body></html>', 'e29_shell.pdf')
    out = fitz.open()
    out.insert_pdf(shell)
    for i, it in enumerate(ITEMS):
        pg = out[1 + i]
        g = GRID[it['key']]['grid'][1]
        h = g - 6 - TOP
        pg.show_pdf_page(fitz.Rect(0, DST, PW, DST + h), SRC, it['src'] - 1, clip=fitz.Rect(0, TOP, PW, g - 6))
    toc = [[1, '표지 · 채점표', 1], [1, '시험지', 2]]
    toc += [[2, f'Q{it["q"]}  {it["no"]}', it['qp']] for it in ITEMS]
    toc.append([1, '정답 · 해설', 2 + N])
    for it in ITEMS:
        out.insert_pdf(SRC, from_page=it['src'] - 1, to_page=it['src'] - 1)
        stamp_answer_page(out[-1], it, it['ap'], total, '정답과 해설')
        toc.append([2, f'Q{it["q"]}  {it["no"]}  {it["title"]}', it['ap']])
    out.set_toc(toc)
    out.set_metadata({'title': '약품유기화학2 중간고사 막판 모의고사 29제', 'author': 'hwangzze'})
    out.save(path, garbage=4, deflate=True, use_objstms=1)
    print('exam', len(out))




# ───────── 2문제/쪽 버전 (풀이 칸 줄 없음, 칸 밑에 정답만) ─────────
from ans29 import ANS

EX2_CSS = """
.slot { position: absolute; left: 27pt; right: 27pt }
.sl-h { display: flex; align-items: center; gap: 9pt; height: 22pt }
.sl-h .qb { color: #fff; font-weight: 900; font-size: 13pt; border-radius: 7pt; padding: 0 10pt; line-height: 20pt }
.sl-h .t { font-size: 11pt; font-weight: 800; color: #1d3557 }
.sl-h .s { font-size: 9.5pt; color: #6b7686 }
.blank { position: absolute; left: 0; right: 0; border: .8pt solid #dfe4ec; border-radius: 7pt; background: #fff }
.blank span { position: absolute; left: 9pt; top: 5pt; font-size: 8.8pt; color: #a5afbd }
.an { position: absolute; left: 0; right: 0; display: flex; gap: 8pt; align-items: flex-start; font-size: 10.4pt; line-height: 1.4; color: #1f2633 }
.an b { flex: none; background: #1d3557; color: #fff; font-size: 9.4pt; font-weight: 800; border-radius: 5pt; padding: 1pt 8pt; margin-top: 1pt }
.sep { position: absolute; left: 27pt; right: 27pt; border-top: 1.4pt dashed #c3cad6 }
.ph { position: absolute; left: 27pt; right: 27pt; top: 8pt; font-size: 8.6pt; color: #8a95a5; display: flex; justify-content: space-between }
"""
Y0, Y1, GAP = 24.0, 692.0, 14.0
SLOT_H = (Y1 - Y0 - GAP) / 2
ANS_H = 30.0
LABEL_H = 24.0


def scale_for(it):
    h = GRID[it['key']]['grid'][1] - 6 - TOP
    return min(0.8, 135.0 / h), h


def slot_html(it, y):
    s, h = scale_for(it)
    bt = y + LABEL_H + h * s + 6
    ab = y + SLOT_H - ANS_H
    return f'''<div class="slot" style="top:{y:.1f}pt;height:{SLOT_H:.1f}pt">
<div class="sl-h"><span class="qb" style="background:{COL[it["ch"]]}">Q{it["q"]}</span><span class="t">{it["ch"]}장 · {NAMES[it["ch"]]}</span><span class="s">출처 {it["no"]} ({it["kind"]}) · 해설 p.{it["ap"]}</span></div>
<div class="blank" style="top:{bt - y:.1f}pt;height:{ab - bt - 4:.1f}pt"><span>✍ 풀이</span></div>
<div class="an" style="top:{ab - y + 2:.1f}pt"><b>정답</b><span>{ANS[it["key"]]}</span></div></div>'''


def build_exam2(path):
    npg = (N + 1) // 2
    total = 1 + npg + 1 + N
    for i, it in enumerate(ITEMS):
        it['qp'] = 2 + i // 2
        it['ap'] = 2 + npg + 1 + i
    pages = [cover('exam', total).replace('앞: 문제만 (풀이 칸 포함)', '앞: 한 쪽에 2문제 · 풀이 칸 밑에 정답')]
    for p in range(npg):
        pair = ITEMS[2 * p:2 * p + 2]
        body = ''.join(slot_html(it, Y0 + j * (SLOT_H + GAP)) for j, it in enumerate(pair))
        sep = f'<div class="sep" style="top:{Y0 + SLOT_H + GAP / 2:.1f}pt"></div>' if len(pair) == 2 else ''
        pages.append(f'<div class="pg"><div class="ph"><span>약품유기화학 2 · 막판 모의고사</span><span></span></div>{body}{sep}<div class="foot">{2 + p} / {total}</div></div>')
    pages.append(f'''<div class="pg"><div class="dv"><h1>정답 · 해설</h1><p>정답은 문제 쪽에 있고, 여기는 왜 그런지(해설) + 🎯 교수님 강조 + ⚡ 치트키<br>틀린 문항만 골라서 보기</p></div>
<div class="foot" style="color:#c9d3ea">{2 + npg} / {total}</div></div>''')
    shell = render(f'<!doctype html><html><head><meta charset="utf-8"><style>{BASE_CSS}{EXAM_CSS}{EX2_CSS}</style></head><body>{"".join(pages)}</body></html>', 'e29b_shell.pdf')
    out = fitz.open()
    out.insert_pdf(shell)
    for i, it in enumerate(ITEMS):
        pg = out[1 + i // 2]
        y = Y0 + (i % 2) * (SLOT_H + GAP)
        s, h = scale_for(it)
        g = GRID[it['key']]['grid'][1]
        x0 = 27.0
        pg.show_pdf_page(fitz.Rect(x0, y + LABEL_H, x0 + 1080 * s, y + LABEL_H + h * s), SRC, it['src'] - 1,
                         clip=fitz.Rect(27, TOP, 1107, g - 6))
    toc = [[1, '표지 · 채점표', 1], [1, '시험지 (2문제/쪽)', 2]]
    toc += [[2, f'Q{it["q"]}  {it["no"]}', it['qp']] for it in ITEMS]
    toc.append([1, '정답 · 해설', 2 + npg])
    for it in ITEMS:
        out.insert_pdf(SRC, from_page=it['src'] - 1, to_page=it['src'] - 1)
        stamp_answer_page(out[-1], it, it['ap'], total, '정답과 해설')
        toc.append([2, f'Q{it["q"]}  {it["no"]}  {it["title"]}', it['ap']])
    out.set_toc(toc)
    out.set_metadata({'title': '약품유기화학2 중간고사 막판 모의고사 29제 (2문제/쪽)', 'author': 'hwangzze'})
    out.save(path, garbage=4, deflate=True, use_objstms=1)
    print('exam2', len(out))


if __name__ == '__main__':
    if 'exam2' in sys.argv:
        build_exam2(os.path.join(SCR, 'exam29b.pdf'))
    else:
        build_exam(os.path.join(SCR, 'exam29.pdf'))
        build_compact(os.path.join(SCR, 'compact29.pdf'))
