import sys, os, importlib
D = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, D)
import lib, json, annotate, allen
lib.load_bank()
LV = json.load(open(os.path.join(D,'levels.json'))) if os.path.exists(os.path.join(D,'levels.json')) else {}
mods = sys.argv[1:] or ['front', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'back']
for m in mods:
    importlib.import_module(m).build()
# chapter start pages for TOC (cover = page 1, so offset 2)
starts = {}
for i, p in enumerate(lib.PAGES):
    starts.setdefault(p['ch'] if p['ch'] else (99 if i > 2 else 0), i + 2)
import front
cover = front.cover(starts)
css = open(os.path.join(D, 'style.css'), encoding='utf-8').read()
secs = [cover]
# Q 번호를 장마다 1부터 다시 매기기 + 장별 용어 풀이 자동 적용
import re as _r
cnt = {}
for p in lib.PAGES:
    def _rn(m, ch=p['ch']):
        cnt[ch] = cnt.get(ch, 0) + 1
        return f'<b>Q{cnt[ch]}</b>'
    p['html'] = _r.sub(r'<b>Q\d+</b>', _rn, p['html'])
for ch in sorted(set(p['ch'] for p in lib.PAGES)):
    idx = [i for i, p in enumerate(lib.PAGES) if p['ch'] == ch and (ch or i < 3)]
    new = annotate.annotate_chapter([lib.PAGES[i]['html'] for i in idx], ch if ch else 0)
    for i, h in zip(idx, new):
        lib.PAGES[i]['html'] = h
for p in lib.PAGES:
    if 'class="pb qp"' not in p['html']:
        p['html'] = allen.annotate_all(p['html'])
import re as _re
for i, p in enumerate(lib.PAGES):
    if p['ch'] and 'class="part">CHAPTER' in p['html']:
        rows = []
        for j, q in enumerate(lib.PAGES):
            if q['ch'] == p['ch'] and j != i:
                m = _re.search(r'class="part">([^<]*)</span><span class="pt">([^<]*)</span>', q['html'])
                part, title = (m.group(1), m.group(2)) if m else ('', q['title'])
                isq = '개념문제' in title
                rows.append(f'<div class="tr{" tq" if isq else ""}"><span class="tp">{j + 2}</span><span class="tpart">{part}</span><span>{title}</span></div>')
        toc = '<div class="card ctoc" style="margin-top:3.2mm"><div class="ct">📑 이 장의 페이지 — 요약 → 개념문제 순서로</div><div class="tgrid"' + (' style="grid-template-columns:1fr 1fr 1fr"' if len(rows) > 10 else '') + '>' + ''.join(rows) + '</div></div>'
        h = p['html']; k = h.rfind('</div>')
        p['html'] = h[:k] + toc + h[k:]
for i, p in enumerate(lib.PAGES):
    foot = f'<div class="foot"><span>인체생리학 · {p["ch"]}장 {p["name"]}</span><span>{i + 2}</span></div>' if p['ch'] else f'<div class="foot"><span>인체생리학 · 1–7장 통합 마스터 노트</span><span>{i + 2}</span></div>'
    h = p['html']
    if '<div class="pb ">' in h:
        h = h.replace('<div class="pb ">', f'<div class="pb L{LV.get(str(i + 2), -1)}">', 1)
    secs.append(f'<section class="pg {p.get("cls", "")}" style="--c:{p["color"]}" data-i="{i + 2}" data-t="{p["title"]}">{h}{foot}</section>')
open(os.path.join(D, 'out.html'), 'w', encoding='utf-8').write(
    f'<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>인체생리학 1–7장 통합 마스터 노트</title><style>{css}</style></head><body>{"".join(secs)}</body></html>')
print('pages', len(secs))
