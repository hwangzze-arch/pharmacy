# -*- coding: utf-8 -*-
# 압축판 v3: 한 장 정리 + 문제·풀이, 페이지 꽉 채우기, 13px, 속도론 제외
import os, json, subprocess, lib
import p1, p2, p3, p4, p5, p6  # noqa
from lib import HERE

W_IN = 1039      # 297mm − 2×11mm
H_IN = 676       # 본문 높이(헤더·푸터 제외)
GAP = 9

CSS = open(os.path.join(HERE, 'style4.css'), encoding='utf-8').read() + '''
body { font-size: 13px; line-height: 1.52; }
.page { padding: 8mm 11mm 0; display: flex; flex-direction: column; }
.ptop { margin-bottom: 8px; padding-bottom: 5px; border-bottom-width: 1.5px; }
.ptop .pl { font-size: 11px; padding: 2px 9px; } .ptop .pt { font-size: 14px; } .ptop .pr { font-size: 11px; }
.pbox { display: flex; flex-direction: column; gap: 9px; height: 676px; }
.prow { flex: 1 1 auto; display: grid; grid-template-columns: 0.9fr 1.1fr; gap: 10px; margin: 0 !important; padding: 0 !important; border: 0 !important; }
.pq { display: flex; flex-direction: column; }
.qcard { border: 1px solid #d6dbe4; border-radius: 9px; padding: 7px 11px; background: #fff; }
.qh { margin-bottom: 4px; gap: 6px; } .qh .n { font-size: 11.5px; padding: 0 8px; border-radius: 5px; }
.qh .s { font-size: 10px; padding: 0 7px; border-width: 1px; } .qh .t { font-size: 13.4px; }
.qq { font-size: 13.2px; margin-bottom: 3px; } .chs { font-size: 12.8px; gap: 0 12px; }
.mine { flex: 1 1 auto; min-height: 34px; height: auto; margin-top: 6px; border: 1.2px dashed #cfd5df; border-radius: 9px; background-size: 13px 13px; }
.mine span { font-size: 10.5px; top: 4px; left: 8px; padding: 0 6px; }
.sol { border: 1px solid #cfe5d6; background: #f6faf7; border-radius: 9px; padding: 7px 11px; display: flex; flex-direction: column; }
.sol .ans { font-size: 14px; margin-bottom: 2px; } .sol .ans .lb { font-size: 10px; }
.sol .sh { font-size: 12px; margin: 3px 0 2px; }
.sol .brain { margin-top: auto; font-size: 12.2px; padding: 5px 10px; }
.fl { padding-bottom: 2px; gap: 7px; } .fl .ic { width: 21px; height: 21px; font-size: 11px; }
.fl:not(:last-child)::before { left: 10px; top: 21px; }
.fl .tx { font-size: 12.6px; padding-top: 1px; } .fl .tg { font-size: 10px; }
.warn, .fixnote, .mynote { font-size: 12px; padding: 4px 10px; margin: 3px 0; }
table { font-size: 12px; } .img img { max-height: 95px !important; }
.cs { grid-template-columns: repeat(4, 1fr); gap: 7px; }
.cs > div { padding: 6px 10px; border-width: 1px; }
.cs .f { font-size: 13.2px; line-height: 1.38; } .cs .d { font-size: 11.6px; line-height: 1.4; } .cs .h { font-size: 11px; }
.brain { font-size: 12.8px; padding: 6px 11px; }
.title { display: flex; align-items: baseline; gap: 12px; border-bottom: 2.5px solid #1d6db1; padding-bottom: 5px; margin-bottom: 8px; }
.title h1 { margin: 0; font-size: 21px; } .title span { color: #555; font-size: 12.5px; }
.legend { font-size: 12px; color: #444; margin: 0 0 7px; }
.foot { bottom: 4.5mm; font-size: 9.5px; left: 11mm; right: 11mm; }
'''

# ---------- 문제 모으기 (속도론 PART 6 제외)
probs = [it for it in lib.ITEMS if it['kind'] == 'pr' and it['part'] != 6]
probs.sort(key=lambda it: it['part'])
PARTNAME = {1: 'PART 1 · 용해도 · 분배 (2주차)', 2: 'PART 2 · 착물 · 단백질 결합 (3주차)', 3: 'PART 3 · 확산 (4–6주차)', 4: 'PART 4 · 붕해 · 용출 · 약물 방출 (7주차)'}

# ---------- 높이 측정
blocks = ''.join(f'<div class="m" data-i="{i}" style="width:{W_IN}px;margin-bottom:30px">{lib.pr_html(it, 0)}</div>' for i, it in enumerate(probs))
open(os.path.join(HERE, 'measure.html'), 'w', encoding='utf-8').write(
    f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS} .m .prow{{flex:none}} .m .mine{{flex:none;height:34px}}</style></head><body>{blocks}</body></html>')
res = subprocess.run(['node', os.path.join(HERE, 'measure.js'), HERE], capture_output=True, text=True)
hs = {int(k.split(':')[0]): v for k, v in json.loads(res.stdout.replace('"undefined"', '"x"')).items()}

# ---------- 페이지 채우기 (순서 유지 + 같은 PART 안에서 앞쪽 8개까지 끌어오기)
pages = []
pool = list(range(len(probs)))
while pool:
    cur, used = [], 0
    while pool:
        pick = None
        for k, i in enumerate(pool[:8]):
            need = hs[i] + (GAP if cur else 0)
            if used + need <= H_IN:
                pick = k; break
        if pick is None:
            break
        i = pool.pop(pick); used += hs[i] + (GAP if cur else 0); cur.append(i)
    if not cur:
        cur = [pool.pop(0)]; print('WARN tall', probs[cur[0]]['title'], hs[cur[0]])
    cur.sort()
    pages.append((probs[cur[0]]['part'], cur, used))

# ---------- 한 장 정리 (속도론 제외)
cells = ''.join(f'<div><div class="h {w}">{a}</div><div class="f">{b}</div><div class="d">{c}</div></div>' for w, a, b, c in p5.CS)
total_q = len(probs)
out = [f'''<section class="page p5"><div class="title"><h1>물리약학 중간고사 — 시험 직전 5분 한 장 정리</h1><span>2–7주차 · 뒤에 문제 {total_q}개 + 사고의 흐름 풀이</span></div>
<div class="legend"><b style="color:#0e7c86">■ 2주차 용해도·분배</b> · <b style="color:#7b3fb5">■ 3주차 착물</b> · <b style="color:#4954d1">■ 4–6주차 확산</b> · <b style="color:#c4501f">■ 7주차 방출</b></div>
<div class="cs">{cells}</div>
<div class="brain" style="margin-top:8px"><span class="lab">🧠 전 범위 한 문장</span>녹아야(Cs) → 나뉘고(K) → 퍼져서(J = DKΔC/h) → 나온다(√t · 0차) — 착물은 이 흐름을 조절하는 도구!</div>
<div class="brain" style="background:#b42318"><span class="lab">⚠️ 함정 TOP 6</span>① pKa ≠ 침전 pH ② 진분배계수는 pH와 무관 ③ 두께 무관은 D, P ∝ 1/h ④ 다층은 저항 더하고 뒤집기 ⑤ 막의 K = C₃/C₂ ⑥ 누적 방출량은 항상 증가, 줄어드는 건 속도</div>{{FOOT}}</section>''']
no = 0
for part, idxs, used in pages:
    rows = ''
    first = no + 1
    for i in idxs:
        no += 1
        rows += lib.pr_html(probs[i], no)
    rng = f'문제 {first:02d}' + (f'–{no:02d}' if no > first else '')
    parts = sorted({probs[i]['part'] for i in idxs})
    pt = ' / '.join(PARTNAME[q] for q in parts)
    out.append(f'<section class="page p{part}"><div class="ptop"><span class="pl">문제</span><span class="pt">{pt}</span><span class="pr">{rng}</span></div><div class="pbox">{rows}</div>{{FOOT}}</section>')
foot = '<div class="foot"><span>물리약학 중간고사 · 한 장 정리 + 문제·풀이</span><span>{PN}</span></div>'
N = len(out)
html = ''.join(p.replace('{FOOT}', foot.replace('{PN}', f'{k} / {N}')) for k, p in enumerate(out, 1))
open(os.path.join(HERE, 'out3.html'), 'w', encoding='utf-8').write(
    f'<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>물리약학 중간고사 한 장 정리 + 문제풀이</title><style>{CSS}</style></head><body>{html}</body></html>')
fill = [round(u / H_IN * 100) for _, _, u in pages]
print(N, 'pages,', total_q, 'problems, fill% min', min(fill), 'avg', sum(fill) // len(fill))
