# -*- coding: utf-8 -*-
"""각 문제 페이지의 '내 풀이' 칸 자리에 들어갈 [내 필기 + 치트키] 블록을 HTML로 만든다."""
import json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from content_notes import NOTES
from content_cheat import CHEAT

HERE = os.path.dirname(os.path.abspath(__file__))
GRID = json.load(open(os.path.join(HERE, '..', 'grid.json')))
from selection import KEEP, PROF
W = 1080  # pt

REDOX = """
<div class="redox">
 <div class="rx-t">🔄 산화 · 환원 일방통행 티켓</div>
 <div class="rx-row up"><div class="rx-lab">⬆ 산화<small>알코올 → C=O</small><em>O 들어간 시약</em></div>
  <div class="rx-c"><b>순한 맛</b> DMP · PCC<br><span>1차 → <u>알데하이드</u>에서 딱 멈춤</span></div>
  <div class="rx-c hot"><b>매운 맛</b> CrO₃ · KMnO₄<br><span>1차 → <u>카복실산</u>까지 / 2차 → 케톤</span></div></div>
 <div class="rx-row dn"><div class="rx-lab">⬇ 환원<small>C=O → 알코올</small><em>H 들어간 시약</em></div>
  <div class="rx-c"><b>순한 맛</b> NaBH₄<br><span>케톤 · 알데하이드만</span></div>
  <div class="rx-c hot"><b>매운 맛</b> LiAlH₄<br><span>에스터 · 카복실산까지 싹 다</span></div></div>
 <div class="rx-f">갔던 길을 되돌아올 땐 <b>반대 역할 시약</b>으로 바꿔 쓴다!</div>
</div>"""

CSS = """
@page { size: 1080pt 1100pt; margin: 0 }
* { box-sizing: border-box; margin: 0; padding: 0 }
html, body { background: #fff; font-family: 'Pretendard', 'Noto Color Emoji', sans-serif; color: #1f2633; }
.slot { width: 1080pt; page-break-after: always; display: flex; flex-direction: column; gap: 5pt; padding: 0 1pt; }
.slot:last-child { page-break-after: auto }
sub { font-size: 70%; vertical-align: -0.25em; line-height: 0 }
b { font-weight: 700 }
.r { color: #d63a3a } .bl { color: #2456c9 }
.hl { background: #fff1a8; padding: 0 2pt; border-radius: 2pt }

/* 내 필기 */
.notes { border: 1.2pt solid #f2c76b; background: #fffaf0; border-radius: 7pt; padding: 7pt 11pt 8pt; font-size: 10.6pt; line-height: 1.5; position: relative }
.notes .tag { display: inline-block; background: #f0a020; color: #fff; font-weight: 800; font-size: 9.5pt; padding: 1.5pt 8pt; border-radius: 10pt; margin-bottom: 4pt; letter-spacing: .3pt }
.nt-h { font-weight: 800; color: #b3530c; margin: 1pt 0 3pt; font-size: 11pt }
.nt-h.bl { color: #2456c9 }
.nt-ol, .nt-ul { padding-left: 15pt } .nt-ol li, .nt-ul li { margin: 1.5pt 0 }
.nt-cols2 { columns: 2; column-gap: 22pt } .nt-cols2 li { break-inside: avoid }
.nt-box { background: #fff; border: 1pt dashed #e6b35a; border-radius: 5pt; padding: 5pt 8pt; margin-top: 4pt }
.nt-two { display: grid; grid-template-columns: 1fr 1fr; gap: 12pt; align-items: start }
img { max-width: 100%; max-height: 235pt; display:block }
.side { display: grid; grid-template-columns: var(--l, 1fr) var(--r, 1fr); gap: 6pt; align-items: start }
.nt-cap { font-size: 8.5pt; color: #8a7a5a; margin-bottom: 2pt }
.nt-chem { font-size: 11.5pt; font-weight: 600; color: #c33; margin: 2pt 0 4pt; letter-spacing: .2pt }
.ring { border: 1.6pt solid #2ec4b6; border-radius: 50%; padding: 1pt 6pt }
.nt-small { font-size: 8.8pt; color: #8a6a3a; margin-top: 3pt }
.nt-tb { border-collapse: collapse; margin-top: 6pt; width: 100%; font-size: 10pt }
.nt-tb th, .nt-tb td { border: 1pt solid #f0d9a8; padding: 3pt 6pt; text-align: left }
.nt-tb th { background: #fdebc4 }
.nt-ice { border-collapse: collapse; font-size: 12pt; font-weight: 600; color: #c33 }
.nt-ice td { padding: 1pt 7pt; text-align: center } .nt-ice td:first-child { font-size: 9pt; color: #8a6a3a }
.nt-ice tr.ln td { border-top: 1.2pt dashed #c33 }

/* 교수님 강조 */
.prof { display: flex; gap: 9pt; align-items: center; background: #fff0f3; border: 1.3pt solid #f3a6b8; border-radius: 7pt; padding: 5pt 10pt; font-size: 10.8pt; line-height: 1.45 }
.prof .pt { background: #d1335b; color: #fff; font-weight: 800; font-size: 10pt; padding: 2pt 9pt; border-radius: 10pt; white-space: nowrap }
/* 치트키 */
.cheat { border-radius: 7pt; border: 1.2pt solid #c9d3ea; background: #f6f8fd; padding: 6pt 9pt 8pt; }
.ch-head { display: flex; align-items: center; gap: 8pt; margin-bottom: 5pt }
.ch-head .t { background: linear-gradient(90deg,#1d3557,#3a5a99); color: #fff; font-weight: 800; font-size: 10.5pt; padding: 2pt 10pt; border-radius: 10pt; letter-spacing: .3pt }
.ch-head .lg { font-size: 8pt; color: #6b7686 } .ch-head .lg i { font-style: normal; padding: 0 5pt; border-radius: 6pt; margin: 0 2pt; font-weight: 700 }
.items { display: grid; gap: 6pt }
.it { background: #fff; border-radius: 5pt; padding: 5pt 8pt 6pt; border-left: 3.5pt solid #2a9d8f; font-size: 10.3pt; line-height: 1.45; box-shadow: 0 0 0 .6pt #e1e6f0 }
.it.g { border-left-color: #7b5cd6 }
.it .h { font-weight: 800; font-size: 10.6pt; color: #1d3557; margin-bottom: 1.5pt; display: flex; gap: 5pt; align-items: baseline }
.it .tg { font-size: 7.5pt; font-weight: 800; padding: .5pt 5pt; border-radius: 6pt; color: #fff; background: #2a9d8f; white-space: nowrap }
.it.g .tg { background: #7b5cd6 }
.tgg { background: #ece6fb; color: #5b3fc0 } .tgc { background: #dff3f0; color: #1f7a6f }

.redox { background: #fff; border-radius: 5pt; box-shadow: 0 0 0 .6pt #e1e6f0; border-left: 3.5pt solid #e76f51; padding: 5pt 8pt 6pt; font-size: 9.6pt; line-height: 1.35 }
.rx-t { font-weight: 800; color: #b23a1e; font-size: 10.6pt; margin-bottom: 3pt }
.rx-row { display: grid; grid-template-columns: 96pt 1fr 1fr; gap: 5pt; margin: 3pt 0 }
.rx-lab { font-weight: 800; font-size: 10.5pt; border-radius: 4pt; padding: 2pt 6pt; color: #fff; line-height: 1.2 }
.rx-lab small { display: block; font-size: 8pt; font-weight: 600; opacity: .95 } .rx-lab em { display:block; font-style: normal; font-size: 7.6pt; font-weight: 600; opacity: .9 }
.up .rx-lab { background: #e76f51 } .dn .rx-lab { background: #2a7ab0 }
.rx-c { border: 1pt solid #eee; border-radius: 4pt; padding: 2pt 6pt; background: #fbfbfb }
.rx-c span { color: #555 } .rx-c.hot { background: #fff4ef; border-color: #f6c9b9 }
.dn .rx-c.hot { background: #eef6fd; border-color: #bcd9f0 }
.rx-f { font-size: 9pt; color: #b23a1e; margin-top: 2pt }

/* 남는 칸 = 메모 */
.memo { flex: 1 1 auto; border: 1pt dashed #c3cad6; border-radius: 7pt; min-height: 0;
  background-color: #fff;
  background-image: linear-gradient(#eef1f6 .7pt, transparent .7pt), linear-gradient(90deg, #eef1f6 .7pt, transparent .7pt);
  background-size: 14pt 14pt; position: relative }
.memo span { position: absolute; left: 9pt; top: 4pt; font-size: 8.5pt; color: #8a97ab; background: #fff; padding: 0 3pt }
"""

def item_html(it):
    if it == "REDOX":
        return REDOX
    kind, t, b = it
    tag = {'g': '제미나이 치트키', 'c': '추가 꿀팁'}[kind]
    return f'<div class="it {kind}"><div class="h"><span class="tg">{tag}</span>{t}</div><div>{b}</div></div>'

def cols_for(items):
    n = len(items)
    if n == 1: return "1fr"
    if n == 2: return "1fr 1fr"
    return "1fr 1fr 1fr"

SIDE = {"18-11": ("1.45fr", "1fr"), "18-23": ("1.15fr", "1fr"), "18-28": ("1.2fr", "1fr"), "21-15": ("1.3fr", "1fr"),
        "21-23": ("1.5fr", "1fr"), "21-26": ("0.75fr", "1fr"), "21-34": ("1.5fr", "1fr"), "18-24": ("1fr", "1.3fr"),
        "18-12": ("1fr", "1.2fr"), "20-24": ("1fr", "1.3fr"), "21-10": ("1fr","0.0001fr")}

def slot_html(key, hg):
    parts = []
    if key in NOTES:
        parts.append(f'<div class="notes"><span class="tag">📝 내 필기 정리</span>{NOTES[key]}</div>')
    items = CHEAT[key]
    if key in PROF:
        parts.append(f'<div class="prof"><span class="pt">🎯 교수님 강조</span><span>{PROF[key]}</span></div>')
    # REDOX 박스는 넓게: 다른 아이템과 2열로
    if "REDOX" in items:
        others = [i for i in items if i != "REDOX"]
        cols = "1fr 1.25fr" if len(others) <= 1 else "1fr 1fr 1.3fr"
    else:
        cols = cols_for(items)
    if key in SIDE and key != "21-10":
        cols = "1fr"
    inner = ''.join(item_html(i) for i in items)
    parts.append(f'''<div class="cheat"><div class="ch-head"><span class="t">⚡ 1초 컷 치트키</span>
<span class="lg"><i class="tgg">제미나이 치트키</i><i class="tgc">추가 꿀팁</i></span></div>
<div class="items" style="grid-template-columns:{cols}">{inner}</div></div>''')
    if key in SIDE and key != "21-10":
        l, r = SIDE[key]
        parts = [f'<div class="side" style="--l:{l};--r:{r}">{parts[0]}<div class="sidecol" style="display:flex;flex-direction:column;gap:5pt">{"".join(parts[1:])}</div></div>']
    parts.append('<div class="memo"><span>✍ 메모</span></div>')
    return f'<div class="slot" data-key="{key}" style="min-height:{hg:.1f}pt">{"".join(parts)}</div>'

def main():
    out = []
    keys = []
    for ch, rg in KEEP.items():
        for pn in rg:
            k = f'{ch}-{pn}'
            g = GRID[k]['grid']
            hg = g[3] - g[1]
            out.append(slot_html(k, hg))
            keys.append(k)
    html = f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{"".join(out)}</body></html>'
    open(os.path.join(HERE, 'slots.html'), 'w').write(html)
    json.dump(keys, open(os.path.join(HERE, 'slot_keys.json'), 'w'))
    print(len(keys), 'slots')

if __name__ == '__main__':
    main()
