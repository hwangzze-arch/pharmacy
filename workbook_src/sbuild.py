# -*- coding: utf-8 -*-
"""'요약 + 문제 통합' 에디션 빌더 (물리약학 최종요약 스타일).
사용: CH=13 python3 sbuild.py  →  summary_ch13.pdf
장별 데이터: sNN.py (TITLE, PARTS, BASICS, CHEAT, ITEMS 매핑)"""
import os, re, sys, importlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from helpers import *

HERE = os.path.dirname(os.path.abspath(__file__))
CHNUM = os.environ.get('CH', '13')
S = importlib.import_module('s' + CHNUM)

CSS = r'''
@page { size: 320mm 200mm; margin: 0; }
* { box-sizing: border-box; }
html { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
body { font-family: 'Noto Sans KR', sans-serif; color: #1f2937; margin: 0; word-break: keep-all; }
b { font-weight: 700; }
sub, sup { font-size: 0.72em; line-height: 0; }
.m { font-family: 'Noto Serif', serif; font-style: italic; white-space: nowrap; }
.sc { font-variant: small-caps; font-size: .95em; }
.small { font-size: .9em; color: #475569; }
.c { text-align: center; }
.hl { background: linear-gradient(transparent 60%, #fde68a 60%); font-weight: 700; padding: 0 2px; }
.mk { background: #fef08a; padding: 0 3px; border-radius: 3px; font-weight: 700; }
.note { font-size: .92em; color: #475569; background: #f8fafc; border-radius: 6px; padding: .35em .8em; margin: .4em 0; }

.pg { --s: 1; width: 320mm; height: 200mm; position: relative; overflow: hidden; page-break-after: always; padding: 7mm 10mm 9mm; display: flex; flex-direction: column; background: #fff; }
.pg .foot { position: absolute; left: 10mm; right: 10mm; bottom: 3mm; font-size: 7.3pt; color: #94a3b8; display: flex; justify-content: space-between; }

/* ---------- header ---------- */
.hd { display: flex; align-items: center; gap: 4mm; border-bottom: 2.5px solid #4f46e5; padding-bottom: 2mm; margin-bottom: 3mm; flex: none; }
.hd .pill { background: #4f46e5; color: white; font-weight: 900; font-size: 9pt; padding: 1.2mm 4mm; border-radius: 999px; white-space: nowrap; }
.hd .num { background: #4f46e5; color: white; font-weight: 900; font-size: 15pt; width: 12mm; height: 10mm; border-radius: 6px; display: flex; align-items: center; justify-content: center; }
.hd .num.we { background: #0f766e; }
.hd h1 { font-size: 16.5pt; margin: 0; font-weight: 900; color: #111827; line-height: 1.2; }
.hd .src { font-size: 8.2pt; border: 1.5px solid #4f46e5; color: #4f46e5; border-radius: 999px; padding: .5mm 3mm; font-weight: 700; white-space: nowrap; }
.hd .src.we { border-color: #0f766e; color: #0f766e; }
.hd .rt { margin-left: auto; text-align: right; font-size: 8.5pt; color: #64748b; white-space: nowrap; }
.hd .rt b { color: #4f46e5; }
.stars { color: #f59e0b; letter-spacing: 1px; font-size: 9pt; }
.stars i { color: #e5e7eb; font-style: normal; }

/* ---------- concept page ---------- */
.body { flex: 1; min-height: 0; overflow: hidden; font-size: calc(10pt * var(--s)); line-height: 1.6; display: flex; flex-direction: column; gap: 2.6mm; }
.banner { background: #eef2ff; border-left: 5px solid #4f46e5; border-radius: 8px; padding: .55em 1em; font-weight: 700; color: #1e1b4b; font-size: 1.04em; flex: none; }
.cols2 { display: grid; grid-template-columns: 1fr 1fr; gap: 3.2mm; align-items: start; }
.cols3 { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 3mm; align-items: start; }
.stack { display: flex; flex-direction: column; gap: 3mm; }
.cc { border: 1px solid #e2e8f0; border-left: 4px solid var(--c, #4f46e5); border-radius: 9px; padding: .5em .9em .6em; background: #fff; }
.cc h4 { margin: 0 0 .3em; font-size: 1.05em; color: var(--c, #4f46e5); font-weight: 900; }
.cc p { margin: .25em 0; }
.cc ul { margin: .2em 0; padding-left: 1.2em; }
.cc li { margin: .15em 0; }
.cc.blue { --c: #2563eb; } .cc.green { --c: #16a34a; } .cc.red { --c: #dc2626; } .cc.orange { --c: #ea580c; } .cc.purple { --c: #7c3aed; } .cc.teal { --c: #0d9488; } .cc.gray { --c: #64748b; }
.cc.fill { background: #f8fafc; }
.fbox { border: 1.5px solid #4f46e5; border-radius: 8px; background: #fff; text-align: center; font-family: 'Noto Serif', serif; font-size: 1.15em; padding: .35em .6em; margin: .35em 0; color: #1e1b4b; }
.fbox small { display: block; font-family: 'Noto Sans KR'; font-size: .72em; color: #64748b; }
.hs { background: #fff7ed; border: 1px solid #fed7aa; border-radius: 8px; padding: .4em .9em; font-size: .95em; }
.hs b.t { color: #c2410c; }
.trap { background: #fef2f2; border: 1px solid #fecaca; border-radius: 8px; padding: .4em .9em; font-size: .95em; }
.trap b.t { color: #dc2626; }
.ok { color: #16a34a; font-weight: 900; } .no { color: #dc2626; font-weight: 900; }

/* ---------- divider / cover ---------- */
.divider { background: linear-gradient(135deg, #eef2ff, #f8fafc); justify-content: center; padding-left: 22mm; }
.divider .big { font-size: 54pt; font-weight: 900; color: #4f46e5; line-height: 1; }
.divider h2 { font-size: 26pt; margin: 4mm 0 2mm; color: #111827; }
.divider .q { color: #64748b; font-size: 12pt; margin-bottom: 8mm; }
.divider .toc { display: grid; grid-template-columns: 1fr 1fr; gap: 3mm; width: 250mm; }
.divider .toc div { background: white; border-radius: 10px; padding: 3mm 5mm; font-size: 10.5pt; box-shadow: 0 1px 2px rgba(0,0,0,.05); }
.divider .toc b { color: #4f46e5; margin-right: 3mm; }
.cover { background: linear-gradient(140deg, #1e1b4b 0%, #3730a3 45%, #4f46e5 70%, #0d9488 100%); color: white; padding: 18mm 22mm; }
.cover .eyebrow { font-size: 9.5pt; letter-spacing: 3px; color: #c7d2fe; font-weight: 700; }
.cover h1 { font-size: 34pt; line-height: 1.25; margin: 5mm 0 3mm; font-weight: 900; }
.cover .sub { font-size: 12pt; color: #e0e7ff; }
.cover .flow { margin-top: 7mm; display: flex; gap: 2.5mm; align-items: center; font-size: 9pt; color: #c7d2fe; }
.cover .flow span { background: white; color: #1e1b4b; border-radius: 999px; padding: 1.2mm 4mm; font-weight: 700; }
.cover .parts { position: absolute; left: 22mm; right: 22mm; bottom: 16mm; display: grid; gap: 3.5mm; }
.cover .parts div { background: rgba(255,255,255,.1); border: 1px solid rgba(255,255,255,.25); border-radius: 10px; padding: 3.5mm 4mm; font-size: 8.8pt; color: #e0e7ff; line-height: 1.5; }
.cover .parts b { display: block; color: white; font-size: 10.5pt; margin-bottom: 1mm; }

/* ---------- problem page ---------- */
.pbody { flex: 1; min-height: 0; overflow: hidden; font-size: calc(10pt * var(--s)); line-height: 1.55; display: flex; flex-direction: column; gap: 2.2mm; }
.row1 { display: grid; grid-template-columns: 1.08fr 1fr; gap: 3.5mm; flex: none; align-items: stretch; }
.box1 { border-radius: 9px; padding: .45em .9em .6em; }
.box1 > .lab { display: inline-block; font-size: .74em; font-weight: 900; letter-spacing: 1px; padding: 0 .7em; border-radius: 999px; margin-bottom: .2em; }
.orig { border: 1px solid #cbd5e1; background: #fff; font-family: 'Noto Serif', serif; color: #0f172a; line-height: 1.48; }
.orig > .lab { background: #334155; color: white; font-family: 'Noto Sans KR'; }
.trans { background: #eef2ff; border: 1px solid #c7d2fe; }
.trans > .lab { background: #4f46e5; color: white; }
.box1 p { margin: .25em 0; }
.blank { flex: 1 1 auto; min-height: 30mm; border: 1.3px dashed #cbd5e1; border-radius: 9px; position: relative;
         background-image: radial-gradient(#cbd5e1 0.9px, transparent 1px); background-size: 5mm 5mm; background-position: 2.5mm 2.5mm; }
.blank .lab { position: absolute; left: 3mm; top: 2mm; background: white; border: 1px solid #cbd5e1; font-size: 7.5pt; font-weight: 700; padding: 0 2.5mm; border-radius: 999px; color: #475569; }
.row3 { display: grid; grid-template-columns: 1.15fr 1fr; gap: 4mm; flex: none; border-top: 2px solid #16a34a; padding-top: 2mm; }
.ansh { display: flex; align-items: center; gap: 2mm; margin-bottom: .3em; }
.ansh .t { background: #16a34a; color: white; font-weight: 900; font-size: .8em; padding: .05em .8em; border-radius: 5px; }
.chips { display: flex; flex-wrap: wrap; gap: .3em; margin: .1em 0 .35em; }
.chip { background: #f0fdf4; border: 1px solid #86efac; border-radius: 7px; padding: .05em .65em; }
.colR { display: flex; flex-direction: column; gap: .3em; }

/* ---------- shared bits (from v1) ---------- */
.rx { display: flex; align-items: center; justify-content: center; gap: 6px; margin: .15em 0; flex-wrap: wrap; font-family: 'Noto Serif'; }
.rx .rxx { margin-left: 10px; }
.rxarr { vertical-align: middle; height: calc(var(--s) * 28px); width: auto; }
.rxlist .rx { justify-content: flex-start; }
.rxlist > div { display: flex; align-items: center; gap: 4px; }
.eq { text-align: center; font-family: 'Noto Serif', serif; font-size: 1.04em; margin: .2em 0; }
.eql { margin: .1em 0; }
.frac { display: inline-flex; flex-direction: column; vertical-align: middle; text-align: center; margin: 0 3px; }
.frac > span { line-height: 1.3; padding: 0 3px; }
.frac > span:first-child { border-bottom: 1px solid currentColor; }
table.al { margin: .2em auto; border-collapse: collapse; font-family: 'Noto Serif', serif; }
table.al td { padding: .03em .4em; vertical-align: middle; }
table.al td.l { text-align: right; white-space: nowrap; }
table.al td.n { color: #64748b; font-size: .92em; padding-left: 1em; }
table.al.sum td.l { font-family: 'Noto Sans KR'; font-weight: 700; color: #4f46e5; }
table.al.sum td.e { display: none; }
table.al.sum td.n { color: #1f2937; font-family: 'JetBrains Mono'; font-size: .95em; text-align: right; }
table.al.sum tr:last-child td { border-top: 1.5px solid #4f46e5; }
ol.steps { counter-reset: s; list-style: none; padding: 0; margin: .2em 0; }
ol.steps > li { counter-increment: s; position: relative; padding-left: 1.9em; margin: .25em 0; }
ol.steps > li::before { content: counter(s); position: absolute; left: 0; top: .15em; width: 1.4em; height: 1.4em; border-radius: 50%; background: #16a34a; color: white; font-size: .8em; font-weight: 900; display: flex; align-items: center; justify-content: center; }
.box { border-radius: 8px; padding: .3em .8em; margin: .25em 0; font-size: .95em; }
.box .bt { font-weight: 900; font-size: .78em; border-radius: 4px; padding: 0 .5em; margin-right: .5em; color: white; }
.box.key { background: #eff6ff; border-left: 4px solid #2563eb; } .box.key .bt { background: #2563eb; }
.box.tip { background: #fefce8; border-left: 4px solid #eab308; } .box.tip .bt { background: #ca8a04; }
.box.warn { background: #fef2f2; border-left: 4px solid #ef4444; } .box.warn .bt { background: #dc2626; }
figure.fig { margin: .2em auto; text-align: center; }
figure.fig img { max-width: 100%; max-height: calc(var(--s) * 55mm); }
figure.fig figcaption { font-size: .8em; color: #64748b; line-height: 1.35; }
table.tb { border-collapse: collapse; margin: .25em auto; font-size: .92em; }
table.tb th { background: #4f46e5; color: white; padding: .1em .7em; font-weight: 700; }
table.tb td { border-bottom: 1px solid #e2e8f0; padding: .04em .7em; text-align: center; }
table.tb tr:nth-child(even) td { background: #f8fafc; }
table.tb.mini { font-family: 'Noto Serif'; } table.tb.mini th { background: #475569; }
table.tb.left td { text-align: left; }
.twostep { display: flex; gap: .6em; margin: .3em 0; }
.twostep > div { flex: 1; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: .3em .6em; font-family: 'Noto Serif'; }
.twostep span { display: inline-block; background: #0f766e; color: white; font-family: 'Noto Sans KR'; font-weight: 900; font-size: .78em; border-radius: 4px; padding: 0 6px; margin-right: 6px; }
.twostep small { display: block; font-family: 'Noto Sans KR'; color: #64748b; font-size: .8em; }
.tiles { display: grid; grid-template-columns: repeat(3, 1fr); gap: 2mm; }
.tiles > div { background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: .3em .7em; line-height: 1.35; }
.tiles b { display: block; font-size: .82em; color: #475569; }
.tiles span { display: block; font-family: 'JetBrains Mono'; font-weight: 700; font-size: 1.05em; color: #4f46e5; }
.tiles small { font-size: .74em; color: #94a3b8; }
'''

FIT = r'''<script>
window.FIT = [];
for (const pg of document.querySelectorAll('.pg')) {
  const b = pg.querySelector('.body, .pbody'); if (!b) continue;
  let s = 1.0; pg.style.setProperty('--s', s);
  const over = () => b.scrollHeight > b.clientHeight + 1;
  if (b.classList.contains('body')) {
    while (!over() && s < 1.3) { s += 0.02; pg.style.setProperty('--s', s.toFixed(2)); }
  }
  while (over() && s > 0.55) { s -= 0.02; pg.style.setProperty('--s', s.toFixed(2)); }
  window.FIT.push([pg.dataset.id || '', +s.toFixed(2), b.scrollHeight > b.clientHeight + 1]);
}
</script>'''


def stars_html(n):
    return '<span class="stars">' + '★' * n + '<i>' + '★' * (3 - n) + '</i></span>'


def split_explain(html):
    """figures / tip / warn boxes → right column, the rest → left column"""
    right = []
    def grab(m):
        right.append(m.group(0)); return ''
    left = re.sub(r'<figure class="fig".*?</figure>', grab, html, flags=re.S)
    left = re.sub(r'<div class="box (?:tip|warn)">.*?</div>', grab, left, flags=re.S)
    return left, ''.join(right)


def concept_page(c, part):
    return (f'<div class="hd"><span class="pill">{part["tag"]} · {c["id"]}{" " + "★" * c.get("star", 0) if c.get("star") else ""}</span>'
            f'<h1>{c["title"]}</h1><span class="rt">{c.get("en", "")}</span></div>'
            f'<div class="body"><div class="banner">{c["banner"]}</div>{c["html"]}</div>')


def problem_page(no, it, cid, ctitle):
    we = it['kind'] != 'PROBLEM'
    src = f'예제 {it["num"]}' if we else f'원서 문제 {it["num"]}'
    left, right = split_explain(it['explain'])
    return (f'<div class="hd"><span class="num {"we" if we else ""}">{no:02d}</span><h1>{it["ko_title"]}</h1>'
            f'<span class="src {"we" if we else ""}">{src}</span>'
            f'<span class="rt">관련 개념 ▸ <b>{cid}</b> {ctitle} &nbsp;{stars_html(it["level"])}</span></div>'
            f'<div class="pbody">'
            f'<div class="row1"><div class="box1 orig"><span class="lab">원문</span>{it["en"]}</div>'
            f'<div class="box1 trans"><span class="lab">쉬운 말 번역</span>{it["ko"]}</div></div>'
            f'<div class="blank"><span class="lab">✏️ 내 풀이</span></div>'
            f'<div class="row3"><div><div class="ansh"><span class="t">정답</span></div>{it["answer"]}{left}</div>'
            f'<div class="colR">{right}</div></div>'
            f'</div>')


def build():
    pages = []  # (cls, html, id)
    pages.append(('cover', S.cover(), ''))
    for b in S.BASICS:
        pages.append(('', b, ''))
    items = {i['id']: i for i in S.ALL_ITEMS}
    no = 0
    for part in S.PARTS:
        pages.append(('divider', S.divider(part), ''))
        ctitles = {c['id']: c['title'] for c in part['concepts']}
        for c in part['concepts']:
            pages.append(('', concept_page(c, part), c['id']))
        for pid, cid in part['problems']:
            no += 1
            pages.append(('', problem_page(no, items[pid], cid, ctitles[cid]), pid))
    for e in S.ENDING:
        pages.append(('', e, ''))
    n = len(pages)
    out = []
    for k, (cls, html, pid) in enumerate(pages):
        foot = f'<div class="foot"><span>{S.FOOT}</span><span>{k + 1} / {n}</span></div>'
        out.append(f'<div class="pg {cls}" data-id="{pid}">{html}{foot}</div>')
    doc = (f'<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>{S.FOOT}</title><style>{CSS}</style></head>'
           f'<body>{"".join(out)}{FIT}</body></html>')
    open(os.path.join(HERE, f'summary_ch{CHNUM}.html'), 'w').write(doc)
    return n


def render():
    from playwright.sync_api import sync_playwright
    import pymupdf
    n = build()
    tmp = os.path.join(HERE, f'summary_ch{CHNUM}_tmp.pdf')
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome')
        pg = b.new_page()
        pg.goto('file://' + os.path.join(HERE, f'summary_ch{CHNUM}.html'))
        pg.wait_for_timeout(900)
        fit = pg.evaluate('window.FIT')
        pg.pdf(path=tmp, width='320mm', height='200mm', print_background=True, prefer_css_page_size=True)
        b.close()
    for i, f in enumerate(fit):
        if f[1] < 0.85 or f[2]:
            print(f'page {i+1:3d} {f[0]:6s} scale {f[1]}{"  <-- OVERFLOW" if f[2] else ""}')
    d = pymupdf.open(tmp)
    d.set_metadata({'title': S.FOOT, 'author': 'Claude'})
    d.save(os.path.join(HERE, f'summary_ch{CHNUM}.pdf'), garbage=3, deflate=True)
    print('pages', len(d), 'expected', n)


if __name__ == '__main__':
    render()
