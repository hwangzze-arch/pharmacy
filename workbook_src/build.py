# -*- coding: utf-8 -*-
"""Landscape workbook: one problem per page (16:10, Samsung Notes friendly)."""
import sys, os, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import importlib
from helpers import *

HERE = os.path.dirname(os.path.abspath(__file__))
CHNUM = os.environ.get('CH', '13')
CH = importlib.import_module('ch' + CHNUM)
CHAPTER, CH_TITLE, CH_EN = CH.CHAPTER, CH.CH_TITLE, CH.CH_EN
# 난이도 ★★★ 문제는 제외 (사용자 요청 — 생화학 전 장 공통 규칙)
ITEMS = [i for i in CH.ALL_ITEMS if i['level'] < 3]
EXCLUDED_HARD = [i['num'] for i in CH.ALL_ITEMS if i['level'] >= 3]

W, H = 320, 200  # mm, 16:10

CSS = r'''
@page { size: 320mm 200mm; margin: 0; }
* { box-sizing: border-box; }
html { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
body { font-family: 'Noto Sans KR', sans-serif; color: #1f2937; margin: 0; word-break: keep-all; }
.pg { --s: 1; width: 320mm; height: 200mm; position: relative; overflow: hidden; page-break-after: always;
      padding: 8mm 11mm 10mm; font-size: calc(10.2pt * var(--s)); line-height: 1.62; background: #fff; display: flex; flex-direction: column; }
.pg .foot { position: absolute; left: 11mm; right: 11mm; bottom: 3.5mm; font-size: 7.5pt; color: #94a3b8; display: flex; justify-content: space-between; }
b { font-weight: 700; }
sub, sup { font-size: 0.72em; line-height: 0; }
.m { font-family: 'Noto Serif', serif; font-style: italic; white-space: nowrap; }
.sc { font-variant: small-caps; font-size: .95em; }
.small { font-size: .92em; color: #475569; }
.c { text-align: center; }
.note { font-size: .92em; color: #475569; background: #f8fafc; border-radius: 6px; padding: .4em .9em; margin: .5em 0; }
.hl { background: linear-gradient(transparent 62%, #fde68a 62%); font-weight: 700; padding: 0 2px; }

/* header */
.ph { display: flex; align-items: stretch; margin-bottom: 3.5mm; border-radius: 12px; overflow: hidden; border: 1px solid #c7d2fe; flex: none; }
.ph .badge { background: #1e3a8a; color: white; min-width: 26mm; padding: 1.6mm 3mm; display: flex; flex-direction: column; justify-content: center; align-items: center; }
.ph .badge.we { background: #0f766e; }
.ph .badge small { font-size: 6.8pt; letter-spacing: 1.5px; opacity: .85; font-weight: 700; }
.ph .badge b { font-size: 19pt; line-height: 1.1; font-weight: 900; }
.ph .ttl { flex: 1; padding: 1.6mm 5mm; background: linear-gradient(90deg, #eef2ff, #ffffff); display: flex; align-items: baseline; gap: 5mm; flex-wrap: wrap; }
.ph .ttl .ko { font-size: 14.5pt; font-weight: 900; color: #111827; }
.ph .ttl .en { font-family: 'Noto Serif'; font-weight: 700; font-size: 10pt; color: #1e3a8a; }
.ph .meta { padding: 1.6mm 5mm; display: flex; align-items: center; gap: 3mm; background: white; }
.tag { font-size: 7.8pt; background: #fff7ed; color: #c2410c; border: 1px solid #fed7aa; padding: 0 7px; border-radius: 999px; white-space: nowrap; }
.stars { color: #f59e0b; letter-spacing: 1px; font-size: 9pt; white-space: nowrap; }
.stars i { color: #e5e7eb; font-style: normal; }

/* two columns */
.cols { flex: 1; min-height: 0; display: grid; grid-template-columns: 1fr 1.12fr; gap: 6mm; }
.col { --s: 1; font-size: calc(10.2pt * var(--s)); min-height: 0; overflow: hidden; display: flex; flex-direction: column; gap: 2.6mm; }
.blk { position: relative; padding: .5em 1.1em .7em; border-radius: 10px; flex: none; }
.blk > .lab { display: inline-block; margin: 0 0 .2em -.3em; font-size: 7.4pt; font-weight: 900; letter-spacing: 1.2px; padding: 0 8px; border-radius: 999px; line-height: 1.75; }
.blk p { margin: .3em 0; }
.orig { background: #f8fafc; border: 1px solid #cbd5e1; font-family: 'Noto Serif', serif; line-height: 1.5; color: #0f172a; }
.orig > .lab { background: #334155; color: white; font-family: 'Noto Sans KR'; }
.trans { background: #f0fdf4; border: 1px solid #bbf7d0; }
.trans > .lab { background: #15803d; color: white; }
.blank { flex: 1 1 auto; min-height: 42mm; border: 1.4px dashed #94a3b8; background-color: #fff;
         background-image: repeating-linear-gradient(transparent 0, transparent 8.4mm, #e2e8f0 8.4mm, #e2e8f0 8.6mm); background-position: 0 6mm; }
.blank > .lab { background: #64748b; color: white; }
.blank .hint { position: absolute; right: 4mm; top: 1.6mm; font-size: 7.3pt; color: #94a3b8; }
.ans { background: #fff7ed; border: 2px solid #fb923c; }
.ans > .lab { background: #ea580c; color: white; }
.exp { background: #ffffff; border: 1px solid #fed7aa; border-top: 4px solid #fdba74; flex: 1 1 auto; }
.exp > .lab { background: #9a3412; color: white; }

.chips { display: flex; flex-wrap: wrap; gap: .35em; margin: .1em 0; }
.chip { background: white; border: 1px solid #fdba74; border-radius: 8px; padding: .1em .7em; }

.rx { display: flex; align-items: center; justify-content: center; gap: 6px; margin: .15em 0; flex-wrap: wrap; font-family: 'Noto Serif'; }
.rx .rxx { margin-left: 10px; }
.rxarr { vertical-align: middle; height: calc(var(--s) * 30px); width: auto; }
.rxlist .rx { justify-content: flex-start; }
.rxlist > div { display: flex; align-items: center; gap: 4px; }
.eq { text-align: center; font-family: 'Noto Serif', serif; font-size: 1.05em; margin: .25em 0; }
.eql { margin: .1em 0; }
.frac { display: inline-flex; flex-direction: column; vertical-align: middle; text-align: center; margin: 0 3px; }
.frac > span { line-height: 1.3; padding: 0 3px; }
.frac > span:first-child { border-bottom: 1px solid currentColor; }
table.al { margin: .25em auto; border-collapse: collapse; font-family: 'Noto Serif', serif; }
table.al td { padding: .05em .4em; vertical-align: middle; }
table.al td.l { text-align: right; white-space: nowrap; }
table.al td.n { color: #64748b; font-size: .92em; padding-left: 1em; }
table.al.sum td.l { font-family: 'Noto Sans KR'; font-weight: 700; color: #9a3412; }
table.al.sum td.e { display: none; }
table.al.sum td.n { color: #1f2937; font-family: 'JetBrains Mono'; font-size: .95em; text-align: right; }
table.al.sum tr:last-child td { border-top: 1.5px solid #9a3412; }

ol.steps { counter-reset: s; list-style: none; padding: 0; margin: .25em 0; }
ol.steps > li { counter-increment: s; position: relative; padding-left: 2em; margin: .3em 0; }
ol.steps > li::before { content: counter(s); position: absolute; left: 0; top: .15em; width: 1.45em; height: 1.45em; border-radius: 50%; background: #ea580c; color: white; font-size: .82em; font-weight: 900; display: flex; align-items: center; justify-content: center; }

.box { border-radius: 8px; padding: .3em .9em; margin: .35em 0; font-size: .95em; }
.box .bt { font-weight: 900; font-size: .8em; border-radius: 4px; padding: 0 .5em; margin-right: .5em; color: white; }
.box.key { background: #eff6ff; border-left: 4px solid #2563eb; }
.box.key .bt { background: #2563eb; }
.box.tip { background: #fefce8; border-left: 4px solid #eab308; }
.box.tip .bt { background: #ca8a04; }
.box.warn { background: #fef2f2; border-left: 4px solid #ef4444; }
.box.warn .bt { background: #dc2626; }

figure.fig { margin: .35em auto; text-align: center; }
figure.fig img { max-width: 100%; max-height: calc(var(--s) * 62mm); }
figure.fig figcaption { font-size: .82em; color: #64748b; margin-top: .1em; line-height: 1.35; }

table.tb { border-collapse: collapse; margin: .3em auto; font-size: .93em; min-width: 60%; }
table.tb th { background: #1e3a8a; color: white; padding: .1em .8em; font-weight: 700; }
table.tb td { border-bottom: 1px solid #e2e8f0; padding: .05em .8em; text-align: center; }
table.tb tr:nth-child(even) td { background: #f8fafc; }
table.tb.mini { font-family: 'Noto Serif'; }
table.tb.mini th { background: #475569; }
table.tb.left td { text-align: left; }
.twostep { display: flex; gap: .7em; margin: .4em 0; }
.twostep > div { flex: 1; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: .3em .7em; font-family: 'Noto Serif'; }
.twostep span { display: inline-block; background: #0f766e; color: white; font-family: 'Noto Sans KR'; font-weight: 900; font-size: .78em; border-radius: 4px; padding: 0 6px; margin-right: 6px; }
.twostep small { display: block; font-family: 'Noto Sans KR'; color: #64748b; font-size: .8em; }

/* front pages */
h2.pt { font-size: 17pt; font-weight: 900; color: #1e3a8a; margin: 0 0 1.5mm; display: flex; align-items: center; gap: 10px; }
h2.pt .n { background: #1e3a8a; color: white; border-radius: 8px; font-size: 11pt; padding: 2px 10px; }
.lead { color: #475569; margin: 0 0 3.5mm; }
.grid2 { display: grid; grid-template-columns: 1fr 1fr; gap: 4mm; }
.grid3 { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 4mm; }
.card { border: 1px solid #e2e8f0; border-radius: 10px; padding: 3mm 4mm; background: white; }
.card h4 { margin: 0 0 1.5mm; font-size: 10.5pt; color: #1e3a8a; display: flex; gap: 6px; align-items: center; }
.card h4 .no { background: #ea580c; color: white; border-radius: 50%; width: 18px; height: 18px; font-size: 9pt; display: inline-flex; align-items: center; justify-content: center; }
.card p { margin: 1mm 0; font-size: 9.3pt; }
.formula { font-family: 'Noto Serif'; font-size: 12pt; text-align: center; background: #eff6ff; border-radius: 8px; padding: 1.5mm; margin: 1.5mm 0; color: #1e3a8a; }
.tiles { display: grid; grid-template-columns: repeat(6, 1fr); gap: 2.5mm; }
.tiles > div { background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 1.8mm 3mm; line-height: 1.35; }
.tiles b { display: block; font-size: 8.4pt; color: #475569; }
.tiles span { display: block; font-family: 'JetBrains Mono'; font-weight: 700; font-size: 10.5pt; color: #1e3a8a; }
.tiles small { font-size: 7.4pt; color: #94a3b8; }
.front { font-size: 9.6pt; line-height: 1.6; }
.front figure.fig svg { --fz: .2mm; }
table.toc { width: 100%; border-collapse: collapse; font-size: 10.8pt; }
table.toc td { padding: 1.35mm 2mm; white-space: nowrap; border-bottom: 1px dashed #e2e8f0; vertical-align: middle; }
table.toc td.no { width: 21mm; font-weight: 900; color: #1e3a8a; white-space: nowrap; }
table.toc td.pgn { width: 14mm; text-align: right; color: #ea580c; font-weight: 700; font-family: 'JetBrains Mono'; }
a { color: inherit; text-decoration: none; }
.pg .foot a.back { color: #2563eb; font-weight: 700; }
table.toc td a { display: block; }
table.toc td .en { font-size: 8pt; color: #94a3b8; font-family: 'Noto Serif'; font-style: italic; margin-left: 2mm; }

/* cover */
.cover { background: radial-gradient(circle at 88% 18%, #3b82f6 0%, transparent 40%), radial-gradient(circle at 8% 95%, #f97316 0%, transparent 38%), linear-gradient(150deg, #1e3a8a, #0f1d4a); color: white; padding: 20mm 22mm; }
.cover .eyebrow { font-size: 10.5pt; letter-spacing: 3px; color: #fdba74; font-weight: 700; }
.cover h1 { max-width: 185mm; font-size: 36pt; line-height: 1.2; margin: 5mm 0 3mm; font-weight: 900; }
.cover h1 span { color: #fbbf24; }
.cover .sub { font-size: 13pt; color: #dbeafe; font-weight: 500; }
.cover .en { font-family: 'Noto Serif'; font-style: italic; color: #93c5fd; font-size: 12pt; margin-top: 2mm; }
.cover .stats { display: flex; gap: 5mm; margin-top: 10mm; width: 150mm; }
.cover .stat { flex: 1; background: rgba(255,255,255,.08); border: 1px solid rgba(255,255,255,.18); border-radius: 12px; padding: 4mm; }
.cover .stat b { display: block; font-size: 22pt; color: #fbbf24; line-height: 1.1; }
.cover .stat span { font-size: 9pt; color: #cbd5e1; }
.cover .how { position: absolute; right: 22mm; top: 22mm; width: 92mm; }
.cover .how h3 { color: #fdba74; font-size: 10.5pt; margin: 0 0 3mm; letter-spacing: 1px; }
.cover .how div { border-radius: 10px; padding: 2.6mm 4mm; font-size: 9.5pt; margin-bottom: 2.5mm; }
.cover .how div b { margin-right: 3mm; }
.cover .foot { color: #94a3b8; }
'''


class Pager:
    def __init__(self):
        self.pages = []

    def add(self, inner, cls='', label=''):
        self.pages.append((inner, cls, label))

    def html(self):
        out = []
        n = len(self.pages)
        for i, (inner, cls, label) in enumerate(self.pages):
            foot = (f'<div class="foot"><span>Lehninger 8e · Ch.{CHAPTER} {CH_TITLE} — 예제 &amp; 연습문제 풀이 노트</span>'
                    f'<span>{i + 1} / {n}</span></div>')
            if cls == 'front':
                inner = f'<div class="fw">{inner}</div>'
            out.append(f'<div class="pg {cls}">{inner}{foot}</div>')
        return '\n'.join(out)


def cover():
    nwe = sum(1 for i in ITEMS if i['kind'] != 'PROBLEM')
    npb = sum(1 for i in ITEMS if i['kind'] == 'PROBLEM')
    return f'''
<div class="eyebrow">LEHNINGER PRINCIPLES OF BIOCHEMISTRY · 8TH EDITION</div>
<h1>Chapter {CHAPTER}<br><span style="font-size:{'36pt' if len(CH_TITLE) <= 10 else '27pt'}">{CH_TITLE}</span><br>예제 &amp; 문제 풀이 노트</h1>
<div class="sub">한 문제 = 한 페이지 · 원문 → 번역 → 직접 풀기 → 정답과 쉬운 해설</div>
<div class="en">{CH_EN}</div>
<div class="stats">
 <div class="stat"><b>{nwe if nwe else "–"}</b><span>본문 예제{"" if nwe else " (이 장엔 없음)"}</span></div>
 <div class="stat"><b>{npb}</b><span>장말 연습문제<br>(강의 관련 · ★★★ 제외)</span></div>
 <div class="stat"><b>{CH.STAT[0]}</b><span>{CH.STAT[1]}</span></div>
</div>
<div class="how"><h3>HOW TO USE · 페이지 구성</h3>
 <div style="background:#334155"><b>① 원문</b>영어 원서 문장 그대로</div>
 <div style="background:#15803d"><b>② 번역</b>무슨 말인지 파악</div>
 <div style="background:#64748b"><b>③ 풀이 빈칸</b>S펜으로 직접 풀기</div>
 <div style="background:#ea580c"><b>④ 정답</b>오른쪽 위에서 결과 확인</div>
 <div style="background:#9a3412"><b>⑤ 해설</b>그림 + 쉬운 설명</div>
 <p style="font-size:8.5pt;color:#cbd5e1;margin-top:3mm">왼쪽 = 문제와 풀이 공간 · 오른쪽 = 정답과 해설.<br>먼저 풀 때는 오른쪽을 손으로 가리고 풀어 보세요.</p>
</div>'''


def guide_page():
    nwe = sum(1 for i in ITEMS if i['kind'] != 'PROBLEM')
    npb = sum(1 for i in ITEMS if i['kind'] == 'PROBLEM')
    inc = ''.join(f'<p>{x}</p>' for x in CH.INCLUDE)
    exc = ''.join(f'<p>{x}</p>' for x in CH.EXCLUDE)
    hard = f'<p><b>문제 {", ".join(EXCLUDED_HARD)}</b> — 난이도 ★★★ (여러 파트 종합형)</p>' if EXCLUDED_HARD else ''
    extra = getattr(CH, 'GUIDE_EXTRA', '')
    return f'''
<h2 class="pt"><span class="n">GUIDE</span> 이 노트에 담긴 것</h2>
<p class="lead">{CH.SCOPE}</p>
<div class="grid3">
 <div class="card"><h4>✅ 포함 (예제 {nwe} + 문제 {npb})</h4>{inc}</div>
 <div class="card"><h4>⛔ 제외</h4>{hard}{exc}
  <p class="small">난이도: {stars(1)} 한 단계 · {stars(2)} 두세 단계 (★★★는 제외)</p>
 </div>
 <div class="card"><h4>📌 해설 박스 읽는 법</h4>
  {key('이 문제를 푸는 한 줄 아이디어')}{tip('일상 비유로 직관 잡기')}{warn('시험에서 자주 틀리는 포인트')}
 </div>
</div>
{extra}'''


def toc_page(first):
    rows = []
    for k, it in enumerate(ITEMS):
        lab = f"예제 {it['num']}" if it['kind'] != 'PROBLEM' else f"문제 {it['num']}"
        rows.append(f'<tr><td class="no">{lab}</td><td>{it["ko_title"]}</td><td>{stars(it["level"])}</td>'
                    f'<td class="pgn">{first + k}</td></tr>')
    half = (len(rows) + 1) // 2
    return f'''<h2 class="pt" id="toc"><span class="n">INDEX</span> 차례</h2>
<div class="grid2"><table class="toc">{''.join(rows[:half])}</table><table class="toc">{''.join(rows[half:])}</table></div>'''


def render_item(it):
    we = it['kind'] != 'PROBLEM'
    kind = 'WORKED EXAMPLE' if we else 'PROBLEM'
    return f'''
<div class="ph"><div class="badge {'we' if we else ''}"><small>{kind}</small><b>{it['num']}</b></div>
 <div class="ttl"><span class="ko">{it['ko_title']}</span><span class="en">{it['en_title']}</span></div>
 <div class="meta"><span class="tag">{it['slides']}</span>{stars(it['level'])}</div></div>
<div class="cols">
 <div class="col">
  <div class="blk orig"><span class="lab">ORIGINAL · 원문</span>{it['en']}</div>
  <div class="blk trans"><span class="lab">번역</span>{it['ko']}</div>
  <div class="blk blank"><span class="lab">풀이 · 직접 풀어 보기</span><span class="hint">오른쪽을 가리고 풀어 보세요</span></div>
 </div>
 <div class="col">
  <div class="blk ans"><span class="lab">정답</span>{it['answer']}</div>
  <div class="blk exp"><span class="lab">해설</span>{it['explain']}</div>
 </div>
</div>'''


FIT_JS = r'''
<script>
for (const pg of document.querySelectorAll('.pg.front')) {
  const fw = pg.querySelector('.fw');
  if (pg.querySelector('#toc')) continue;
  const avail = pg.clientHeight - 20 * 3.78;
  let z = 1.0;
  while (z < 1.6) { fw.style.zoom = (z + 0.04).toFixed(2); if (fw.getBoundingClientRect().height > avail) { fw.style.zoom = z.toFixed(2); break; } z += 0.04; }
}
window.FIT = [];
for (const pg of document.querySelectorAll('.pg.item')) {
  const r = [pg.dataset.id];
  for (const c of pg.querySelectorAll('.col')) {
    let s = 1.0; c.style.setProperty('--s', s);
    const ov = () => c.scrollHeight > c.clientHeight + 1;
    while (ov() && s > 0.55) { s -= 0.02; c.style.setProperty('--s', s.toFixed(2)); }
    r.push(+s.toFixed(2), ov());
  }
  window.FIT.push(r);
}
</script>'''


def build():
    P = Pager()
    P.add(cover(), 'cover')
    P.add(guide_page(), 'front')
    for t in CH.front_pages():
        P.add(t, 'front')
    first = len(P.pages) + 2
    P.add(toc_page(first), 'front')
    for it in ITEMS:
        P.add(render_item(it), 'item')
    html = P.html()
    # tag item pages with ids (for fit report / bookmarks)
    ids = iter([it['id'] for it in ITEMS])
    html = re.sub(r'<div class="pg item">', lambda m: (lambda i: f'<div class="pg item" id="{i}" data-id="{i}">')(next(ids)), html)
    doc = f'''<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>Lehninger {CHAPTER}장 예제·문제 풀이노트</title>
<style>{CSS}</style></head><body>{html}{FIT_JS}</body></html>'''
    open(os.path.join(HERE, f'ch{CHNUM}.html'), 'w').write(doc)
    return first


if __name__ == '__main__':
    print('first item page', build(), 'items', len(ITEMS))
