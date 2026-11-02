# -*- coding: utf-8 -*-
"""예상문제 14제 PDF — 표지 + 시험지(한 쪽 2문제, 풀이 칸 밑 정답) + 문항별 해설."""
import os, sys, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from predict_content import P, S
import make_final29 as M
import ansvis

COL = {17: '#2a6f97', 18: '#2a9d8f', 19: '#7b5cd6', 20: '#e76f51', 21: '#d1495b'}
NAMES = {17: '알코올과 페놀', 18: '에터와 에폭사이드', 19: '알데하이드와 케톤', 20: '카복실산과 나이트릴', 21: '카복실산 유도체'}
N = len(P)
NPG = (N + 1) // 2
TOTAL = 1 + NPG + N
for i, p in enumerate(P):
    p['q'] = i + 1
    p['qp'] = 2 + i // 2
    p['ap'] = 2 + NPG + i

CSS = M.BASE_CSS + ansvis.CSS + """
.mol { display: inline-flex; flex-direction: column; align-items: center; margin: 0 4pt }
.mol svg { display: block } .mc { font-size: 8.6pt; color: #4a5568; margin-top: -2pt; text-align: center; max-width: 150pt; line-height: 1.25 }
.row { display: flex; align-items: flex-end; flex-wrap: wrap; gap: 2pt 6pt; margin-top: 4pt }
.pl { font-size: 10.6pt; line-height: 1.65; margin-top: 4pt; color: #1f2633 }
.rx { display: flex; align-items: center; gap: 6pt; margin-top: 4pt; flex-wrap: wrap }
.rg { display: flex; flex-direction: column; align-items: center; min-width: 70pt } .rg span { font-size: 9pt; color: #1f2633 }
.rg .ln { width: 70pt; height: 0; border-top: 1.2pt solid #1f2633; position: relative }
.rg .ln:after { content: ''; position: absolute; right: -1pt; top: -4.4pt; border-left: 7pt solid #1f2633; border-top: 3.6pt solid transparent; border-bottom: 3.6pt solid transparent }
.q { font-size: 20pt; font-weight: 900; color: #d1335b } .pls { font-size: 14pt; color: #4a5568 } .arr { font-size: 18pt; color: #4a5568; align-self: center }
.col { position: absolute; top: 28pt; bottom: 30pt; width: 530pt; display: flex; flex-direction: column }
.col.cl { left: 24pt } .col.cr { right: 24pt }
.vs { position: absolute; left: 566pt; top: 28pt; bottom: 30pt; border-left: 1.4pt dashed #c3cad6 }
.chd { display: flex; align-items: center; gap: 8pt; padding-bottom: 5pt; border-bottom: 2pt solid #1d3557 }
.chd .qb { color: #fff; font-weight: 900; font-size: 14pt; border-radius: 7pt; padding: 0 10pt; line-height: 22pt }
.chd .t { font-size: 11pt; font-weight: 800; color: #1d3557 } .chd .s { font-size: 8.8pt; color: #6b7686; margin-left: auto; text-align: right }
.pb { margin-top: 7pt; background: #f4f6fb; border-left: 4pt solid #1d3557; border-radius: 6pt; padding: 8pt 11pt 8pt; font-size: 10.8pt; line-height: 1.55 }
.bl { flex: 1; margin-top: 8pt; border: .8pt solid #dfe4ec; border-radius: 7pt; position: relative; min-height: 50pt }
.bl span { position: absolute; left: 9pt; top: 5pt; font-size: 8.8pt; color: #a5afbd }
.an { margin-top: 6pt; display: flex; gap: 8pt; align-items: flex-start; font-size: 10pt; line-height: 1.42 }
.an b { flex: none; background: #1d3557; color: #fff; font-size: 9.2pt; font-weight: 800; border-radius: 5pt; padding: 1pt 8pt; margin-top: 1pt }
/* 해설 쪽 */
.w { padding: 20pt 27pt 0; position: absolute; inset: 0 0 34pt 0; display: flex; flex-direction: column }
.memo { flex: 1; margin-top: 12pt; border: 1pt dashed #c3cad6; border-radius: 7pt; position: relative; min-height: 30pt }
.memo span { position: absolute; left: 9pt; top: 5pt; font-size: 8.8pt; color: #a5afbd }
.qh { display: flex; align-items: center; gap: 12pt; padding-bottom: 7pt; border-bottom: 2.4pt solid #1d3557 }
.qh .b { color: #fff; border-radius: 9pt; padding: 3pt 12pt; text-align: center; line-height: 1.15 }
.qh .b small { display: block; font-size: 8.5pt; font-weight: 700 } .qh .b span { font-size: 19pt; font-weight: 900 }
.qh h1 { font-size: 19pt; font-weight: 900; color: #1d3557 } .qh .s { font-size: 9.5pt; color: #6b7686 }
.ans { margin-top: 9pt; background: #dbe7fb; border-left: 4pt solid #2456c9; border-radius: 6pt; padding: 10pt 14pt; font-size: 13pt; line-height: 1.65; color: #1d3557 }
.ans > b { color: #2456c9 }
.am { display: flex; flex-wrap: wrap; gap: 2pt 10pt; margin-top: 3pt; align-items: flex-end }
.gg { display: grid; grid-template-columns: 1.1fr 1fr; gap: 14pt; margin-top: 10pt }
.cd { border: 1pt solid #e1e6f0; border-radius: 7pt; padding: 11pt 15pt; font-size: 12.6pt; line-height: 1.7; background: #fbfcfe }
.cd .t { font-weight: 800; color: #b3530c; font-size: 13.4pt; margin-bottom: 3pt }
.cd ul { padding-left: 15pt } .cd li { margin: 5pt 0 }
.prof { display: flex; gap: 9pt; align-items: flex-start; background: #fff0f3; border: 1.3pt solid #f3a6b8; border-radius: 7pt; padding: 10pt 13pt; font-size: 12.4pt; line-height: 1.65; margin-bottom: 12pt }
.prof .pt { background: #d1335b; color: #fff; font-weight: 800; font-size: 9.6pt; padding: 2pt 9pt; border-radius: 10pt; white-space: nowrap }
.ckx { border-radius: 7pt; border: 1.2pt solid #c9d3ea; background: #f6f8fd; padding: 7pt 10pt }
.ckx .tt { background: linear-gradient(90deg,#1d3557,#3a5a99); color: #fff; font-weight: 800; font-size: 10pt; padding: 2pt 10pt; border-radius: 10pt; display: inline-block; margin-bottom: 3pt }
.ckx .it { background: #fff; border-left: 3.5pt solid #2a9d8f; border-radius: 5pt; padding: 8pt 11pt; font-size: 12pt; line-height: 1.6; margin-top: 7pt }
.ckx .it.gm { border-left-color: #7b5cd6 }
.tg { font-size: 7.5pt; font-weight: 800; padding: .5pt 5pt; border-radius: 6pt; color: #fff; background: #2a9d8f; margin-right: 4pt } .it.gm .tg { background: #7b5cd6 }
.lk { margin-top: 10pt; font-size: 10pt; color: #4a5568; border: 1pt dashed #c3cad6; border-radius: 7pt; padding: 6pt 10pt }
.ft { position: absolute; left: 27pt; bottom: 13pt; font-size: 8.6pt; color: #6b7686 }
/* 표지 */
.cv2 { display: grid; grid-template-columns: 300pt 1fr; height: 100% }
.cv2 .L { background: linear-gradient(160deg, #10243f, #1d3557 55%, #6d4bc4); color: #fff; padding: 34pt 26pt; display: flex; flex-direction: column; gap: 14pt }
.cv2 .k { font-size: 10pt; letter-spacing: 1.5pt; font-weight: 700; opacity: .85 }
.cv2 h1 { font-size: 33pt; font-weight: 900; line-height: 1.15 } .cv2 h1 em { font-style: normal; color: #ffd166 }
.cv2 .box { background: rgba(0,0,0,.22); border-radius: 8pt; padding: 10pt 12pt; font-size: 10.6pt; line-height: 1.65 } .cv2 .box b { color: #ffd166 }
.cv2 .box .h { font-weight: 800; font-size: 11pt; margin-bottom: 3pt }
.cv2 .R { padding: 26pt 26pt 20pt 24pt; display: flex; flex-direction: column }
.cv2 h2 { font-size: 12.5pt; font-weight: 800; color: #1d3557; display: flex; gap: 8pt; align-items: center; margin-bottom: 8pt }
.cv2 h2:after { content: ''; flex: 1; height: 1pt; background: #dde3ee }
.rw { display: grid; grid-template-columns: 26pt 46pt 1fr 150pt 30pt 30pt 15pt 15pt; gap: 6pt; align-items: center; padding: 8.6pt 0; border-bottom: .7pt dotted #d5dbe6; font-size: 10.6pt; line-height: 1.3 }
.rw.th2 { font-size: 8.2pt; color: #8a95a5; font-weight: 700; border-bottom: 1pt solid #c9d3ea; padding: 3pt 0 }
.rw.th2 span { text-align: center } .rw.th2 span:nth-child(3), .rw.th2 span:nth-child(4) { text-align: left }
.qn { color: #fff; font-weight: 900; border-radius: 5pt; text-align: center; font-size: 10pt; line-height: 16pt }
.cht { font-weight: 800; font-size: 9.6pt } .lkc { font-size: 9pt; color: #6b7686 } .pp { text-align: center; color: #6b7686; font-weight: 700; font-size: 9.4pt }
.bx { width: 13pt; height: 13pt; border: 1.2pt solid #9aa5b5; border-radius: 3pt; justify-self: center }
"""


def cover():
    rows = ''.join(f'<div class="rw"><span class="qn" style="background:{COL[p["ch"]]}">E{p["q"]}</span><span class="cht" style="color:{COL[p["ch"]]}">{p["ch"]}장</span>'
                   f'<span>{p["title"]}</span><span class="lkc">{p["link"]}</span><span class="pp">p.{p["qp"]}</span><span class="pp">p.{p["ap"]}</span>'
                   f'<span class="bx"></span><span class="bx"></span></div>' for p in P)
    hd = '<div class="rw th2"><span>번호</span><span>단원</span><span>무엇을 묻나</span><span>원래 문제 (막판 29제)</span><span>문제</span><span>해설</span><span>○</span><span>✗</span></div>'
    return f'''<div class="pg"><div class="cv2"><div class="L"><div class="k">약품유기화학 2 · 중간고사 17–21장</div>
<h1>진짜 시험<br><em>예상문제</em><br>14제</h1>
<div class="box"><div class="h">📌 교수님 출제 안내대로 구성</div>약 12문제 · 단원마다 1~2문제 → <b>17·18·19·20장 2문제씩, 21장 6문제</b><br>답이 딱 떨어지는 형태 · 메커니즘은 <b>E10 한 문제</b>만<br>산화·환원은 <b>생성물·시약만</b> (메커니즘 X)</div>
<div class="box"><div class="h">🔁 변형 방법</div>막판 29제 · 교과서 문제의 <b>핵심 원리는 그대로</b> 두고 화합물·조건만 바꿨다 → 외운 답이 아니라 원리로 풀 수 있는지 확인용<br>구조식은 모두 다시 그림</div>
<div class="box"><div class="h">✍ 푸는 법</div>정답 줄을 가리고 풀기 → ○ / ✗ → ✗ 문항은 해설 + 원래 문제(29제)까지</div>
</div><div class="R"><h2>문항 지도</h2>{hd}{rows}</div></div><div class="foot">1 / {TOTAL}</div></div>'''


def col(p, side):
    return f'''<div class="col {side}"><div class="chd"><span class="qb" style="background:{COL[p["ch"]]}">E{p["q"]}</span>
<span class="t">{p["ch"]}장 · {NAMES[p["ch"]]}</span><span class="s">변형: {p["link"]}<br>해설 p.{p["ap"]}</span></div>
<div class="pb">{p["stem"]}{p["fig"]}</div>
<div class="bl"><span>✍ 풀이</span></div>
{ansvis.render(ansvis.V14[p["q"]], 1.3)}</div>'''


def answer_page(p):
    am = ''
    if p.get('amol'):
        am = '<div class="am">' + ''.join(S(s, w=160, h=95, scale=23, lab=l) for l, s in p['amol']) + '</div>'
    expl = ''.join(f'<li>{e}</li>' for e in p['expl'])
    ck = ''.join(f'<div class="it {"gm" if k == "g" else ""}"><span class="tg">{"제미나이 치트키" if k == "g" else "추가 꿀팁"}</span><b>{t}</b> — {b}</div>' for k, t, b in p['cheat'])
    return f'''<div class="pg"><div class="w">
<div class="qh"><div class="b" style="background:{COL[p["ch"]]}"><small>{p["ch"]}장 예상</small><span>E{p["q"]}</span></div><div><h1>{p["title"]}</h1><div class="s">변형 출처: {p["link"]}</div></div></div>
<div class="ans"><b>정답</b> &nbsp;{p["ans"]}{am}</div>
<div class="gg"><div class="cd"><div class="t">해설</div><ul>{expl}</ul></div>
<div><div class="prof"><span class="pt">🎯 교수님 근거</span><span>{p["prof"]}</span></div>
<div class="ckx"><span class="tt">⚡ 1초 컷 치트키</span>{ck}</div></div></div><div class="memo"><span>✍ 메모 · 틀린 이유</span></div></div>
<div class="ft"><b style="color:{COL[p["ch"]]}">E{p["q"]}</b> &nbsp;예상문제 정답과 해설 · {p["title"]}</div><div class="foot">{p["ap"]} / {TOTAL}</div></div>'''


def build(out):
    pages = [cover()]
    for k in range(NPG):
        pair = P[2 * k:2 * k + 2]
        body = ''.join(col(p, ('cl', 'cr')[j]) for j, p in enumerate(pair))
        pages.append(f'<div class="pg">{body}{"<div class=vs></div>" if len(pair) == 2 else ""}<div class="foot">{2 + k} / {TOTAL}</div></div>')
    pages += [answer_page(p) for p in P]
    hp = os.path.join(HERE, 'predict14.html')
    open(hp, 'w').write(f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{"".join(pages)}</body></html>')
    subprocess.run(['node', os.path.join(HERE, 'render.js'), hp, out, '-', '1134', '708.96'], check=True)
    import pymupdf as fitz
    d = fitz.open(out)
    toc = [[1, '표지 · 문항 지도', 1], [1, '시험지', 2]] + [[2, f'E{p["q"]}  {p["ch"]}장 {p["title"]}', p['qp']] for p in P]
    toc += [[1, '정답 · 해설', 2 + NPG]] + [[2, f'E{p["q"]}  {p["title"]}', p['ap']] for p in P]
    d.set_toc(toc)
    d.set_metadata({'title': '약품유기화학2 중간고사 예상문제 14제', 'author': 'hwangzze'})
    d.saveIncr() if False else d.save(out + '.tmp', garbage=3, deflate=True)
    os.replace(out + '.tmp', out)
    print('pages', len(d))


if __name__ == '__main__':
    build(os.path.join(HERE, '..', 'predict14.pdf'))
