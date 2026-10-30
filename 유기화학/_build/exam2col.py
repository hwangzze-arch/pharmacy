# -*- coding: utf-8 -*-
"""막판 모의고사 — 한 쪽에 2문제(왼쪽·오른쪽). 문제 글은 칼럼 폭에 맞춰 다시 조판, 그림은 원본에서 오려 넣기.
풀이 칸은 줄 없음, 칸 밑에 정답만."""
import json, os, subprocess, sys, html as H
import pymupdf as fitz
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import make_final29 as M
from ans29 import ANS
import ansvis
ANS = dict(ANS)
ANS['21-18'] = '(a) 산-염기 반응 → 카복실레이트 염(RCOO⁻ ⁺H₃NR′) &nbsp; (b) DCC · EDC / SOCl₂ → 산 염화물 → 아민 &nbsp; (c) O-acylisourea (좋은 이탈기) · DCU &nbsp; (d) 부반응 억제 → 아민만 선택적으로 반응'

SRC, GRID, ITEMS, N, COL, NAMES = M.SRC, M.GRID, M.ITEMS, M.N, M.COL, M.NAMES
MAIN_EN, MAIN_KO = 0x141a24, 0x1d5fc4

# 출처 표기를 동그라미 기호 대신 실제 범위로 (작은 ①ⓐ 글리프가 표지에서 깨져 보임)
DISP = {'17-22': '17-42 (a)~(c)', '18-25': '18-27 (a)', '19-37': '19-63 (a)~(c)', '19-38': '19-63 (d)~(g)',
        '20-27': '20-65 (a)~(c)', '21-16': '21-33 (a)', '21-18': '21-38 개념형', '21-36': '21-34 (b)',
        '21-40': '21-53 (a)~(d)', '21-41': '21-53 (e)~(h)'}
WHY = {'17-11': '페놀 + 치환기 → pKa 순서 (교수님 지목)', '17-31': '시약 a~f 빈칸 — 산화·환원·그리냐르·탈수 종합',
       '18-24': '조건(염기·산·그리냐르)별 에폭사이드 개환 위치', '19-7': '알데하이드 만들기 = 산화·환원 관계',
       '19-14': '1차 vs 2차 아민 → 이민 / 엔아민', '19-36': '1,4-첨가(길만)로 β 자리에 가지 붙이기',
       '19-37': '1,2 vs 1,4 첨가 (교수님 지목)', '19-38': '1,2 vs 1,4 첨가 (교수님 지목)',
       '20-12': 'pKa 비교 + 이유 (교수님 지목)', '20-17': 'R–X → 카복실산: CN 길 vs 그리냐르 길',
       '21-18': 'DCC 커플링 개념 — 수업에서 HOBt까지 설명', '21-38': '아마이드 가수분해 / LAH → 아민',
       '21-40': '21장 종합 생성물 (a)~(d)', '21-41': '21장 종합 생성물 (e)~(h)', '21-44': 'SOCl₂ 활성화 → 아마이드 (DEET)'}
for _it in ITEMS:
    _it['no'] = DISP.get(_it['key'], _it['no'])
    _it['why'] = WHY.get(_it['key'], _it['why'])
    if _it['key'] == '21-18':
        _it['title'] = 'DCC 커플링 — 산 + 아민 → 아마이드 (개념형)'

# ── 21장 추가 (삼성노트 21장 파일의 모든 문제, 빨간 네모 3개 제외) ──
SRC = fitz.open(os.path.join(M.SCR, 'final_v4.pdf'))
M.SRC = SRC
RAW = fitz.open(os.path.join(M.SCR, 'final_v4raw.pdf'))  # 시험지 그림은 필기 없는 판에서
NEW21 = [('21-8', '친핵성 아실 치환 생성물 (★★★★★ 3대 원칙)'), ('21-11', '사면체 중간체 읽기 — Nu·이탈기·출발물'),
         ('21-12', '피셔 에스터화 — 산 + 알코올'), ('21-13', '에스터 → 산 + 알코올 짝 찾기'), ('21-14', '분자 내 에스터화 → 락톤'),
         ('21-15', 'SOCl₂로 산 염화물 (사다리 올리기)'), ('21-17', '피셔 에스터화 (가수분해의 역반응)'),
         ('21-20', '산 염화물 + 알코올 → 에스터'), ('21-21', '피셔 vs 산 염화물 — 어느 방법?'), ('21-22', '산 염화물 + 아민 2당량'),
         ('21-23', '산 염화물 + 2차 아민 메커니즘'), ('21-24', '아마이드 세 개 — N 위 가지 = 아민'), ('21-25', '길만 시약 → 케톤에서 멈춤 (2당량 비교)'),
         ('21-28', '고리형 무수물 + 메탄올 1당량'), ('21-29', '숙신산 무수물 + CH₃O⁻'), ('21-30', '비누화가 비가역인 이유'),
         ('21-31', '에스터 → 아마이드 (아미노분해)'), ('21-33', '에스터 + LiAlH₄ → 알코올 2개'), ('21-34', '에스터 + 그리냐르 2당량 역합성'),
         ('21-35', '에스터 + 그리냐르 2당량 (사슬형)'), ('21-37', '아마이드 + LiAlH₄ → 아민 (O 날아감)'), ('21-43', '페닐 4-아미노살리실레이트 합성 순서')]
for _k, _w in NEW21:
    ITEMS.append(dict(M.info(_k), why=_w))
ITEMS.sort(key=lambda i: (i['ch'], int(i['key'].split('-')[1])))
for _i, _it in enumerate(ITEMS):
    _it['q'] = _i + 1
N = len(ITEMS)
DISP.update({'21-17': '21-33 (b)', '21-29': '21-31 (b)', '21-31': '21-31 (a)', '21-35': '21-34 (a)', '21-43': '21-72'})
for _it in ITEMS:
    _it['no'] = DISP.get(_it['key'], _it['no'])

# 꼭 봐야 할 문제 (교수님이 직접 짚은 포인트마다 대표 1~2문항)
MUST = {'21-8', '21-25', '21-37', '21-30', '17-11', '17-14', '17-31', '18-11', '18-24', '19-37', '20-12', '20-17', '21-7', '21-9', '21-18', '21-32', '21-38', '21-44'}
for _it in ITEMS:
    _it['must'] = _it['key'] in MUST

Q22_EN = ''
Q22_KO = ('''<div style="color:#1f2633;font-size:10.8pt;line-height:1.55">
<div style="margin-bottom:4pt">카복실산과 아민으로 아마이드를 만들려고 한다. &nbsp;R–COOH + R′–NH₂ → R–CO–NH–R′</div>
<b>(a)</b> 카복실산과 아민을 <b>그냥 섞으면</b> 아마이드가 잘 생기지 않는다. 그 이유는?<br>
<b>(b)</b> 이때 쓰는 <b>커플링 시약</b> 2가지를 쓰고, 커플링 시약 없이 쓸 수 있는 <b>다른 2단계 방법</b>을 쓰시오.<br>
<b>(c)</b> DCC를 쓰면 카복실산의 –OH는 무엇으로 바뀌는가? 반응이 끝나고 나오는 <b>부산물</b>은?<br>
<b>(d)</b> DCC와 함께 <b>HOBt</b>를 넣는 이유는?</div>''')


ORIG = {c: fitz.open(os.path.join('/home/user/pharmacy/유기화학', f)) for c, f in {
    17: 'CH17_알코올과페놀_통합풀이.pdf', 18: 'CH18_에터와에폭사이드_통합풀이.pdf', 19: 'CH19_알데하이드와케톤_통합풀이.pdf',
    20: 'CH20_카복실산과나이트릴_통합풀이.pdf', 21: 'CH21_카복실산유도체_통합풀이.pdf'}.items()}


def extract(it):
    ch, pn = map(int, it['key'].split('-'))
    pg = ORIG[ch][pn - 1]
    gy = GRID[it['key']]['grid'][1]
    box = fitz.Rect(30, 79, 1105, gy - 6)
    fb = None
    for dr in pg.get_drawings():
        r, f, c = dr['rect'], dr.get('fill'), dr.get('color')
        if f and c and min(f) > 0.99 and abs(c[0] - 0.87) < 0.03 and box.contains(r.tl) and r.width > 60:
            fb = r if fb is None else fb | r
    en, ko = [], []
    for b in pg.get_text('dict', clip=box)['blocks']:
        for l in b.get('lines', []):
            ls = l['spans']
            if not ls or ls[0]['color'] not in (MAIN_EN, MAIN_KO):
                continue
            lb = fitz.Rect(l['bbox'])
            if fb is not None and fb.intersects(lb):
                continue
            base = max(s['size'] for s in ls)
            out = ''
            for s in ls:
                t = H.escape(s['text'])
                if s['size'] < base * 0.9:
                    t = f'<sub>{t}</sub>' if s['origin'][1] >= ls[0]['origin'][1] else f'<sup>{t}</sup>'
                out += t
            (en if ls[0]['color'] == MAIN_EN else ko).append(out)
    if fb is not None:
        fb = fitz.Rect(fb.x0 + 1, fb.y0 + 1, fb.x1 - 1, fb.y1 - 1)
    return ' '.join(en), ' '.join(ko), fb


CSS = """
.col { position: absolute; top: 30pt; bottom: 30pt; width: 530pt; display: flex; flex-direction: column }
.col.cl { left: 24pt } .col.cr { right: 24pt }
.vs { position: absolute; left: 566pt; top: 30pt; bottom: 30pt; border-left: 1.4pt dashed #c3cad6 }
.ch { display: flex; align-items: center; gap: 8pt; padding-bottom: 5pt; border-bottom: 2pt solid #1d3557 }
.ch .qb { color: #fff; font-weight: 900; font-size: 14pt; border-radius: 7pt; padding: 0 10pt; line-height: 22pt }
.ch .t { font-size: 11pt; font-weight: 800; color: #1d3557 } .ch .s { font-size: 9pt; color: #6b7686; margin-left: auto }
.pb { margin-top: 7pt; background: #f4f6fb; border-left: 4pt solid #1d3557; border-radius: 6pt; padding: 7pt 10pt 8pt }
.pb .en { font-size: 11pt; line-height: 1.45; color: #141a24; font-family: 'Liberation Serif', serif }
.pb .ko { font-size: 10.4pt; line-height: 1.45; color: #1d5fc4; margin-top: 3pt }
.must { background: #ffd166; color: #7a4b00; font-weight: 900; font-size: 9.6pt; border-radius: 6pt; padding: 1pt 8pt; border: 1pt solid #e8a800 }
.pt { display: inline-block; background: #d1335b; color: #fff; font-size: 9pt; font-weight: 800; border-radius: 5pt; padding: 1pt 7pt; margin-bottom: 4pt }
.fig { margin: 6pt auto 0; background: #fff; border-radius: 5pt }
.bl { flex: 1; margin-top: 8pt; margin-bottom: 4pt; border: .8pt solid #dfe4ec; border-radius: 7pt; position: relative; min-height: 60pt }
.bl span { position: absolute; left: 9pt; top: 5pt; font-size: 8.8pt; color: #a5afbd }
.an { margin-top: 6pt; display: flex; gap: 8pt; align-items: flex-start; font-size: 10.2pt; line-height: 1.4 }
.an b { flex: none; background: #1d3557; color: #fff; font-size: 9.2pt; font-weight: 800; border-radius: 5pt; padding: 1pt 8pt; margin-top: 1pt }
"""
COLW = 530 - 20 - 4
PART = {'21-17': '(b)만', '21-29': '(b)만', '21-31': '(a)만', '21-35': '(a)만', '17-22': '(a)~(c)만', '18-25': '(a)만', '19-37': '(a)~(c)만', '19-38': '(d)~(g)만', '21-16': '(a)만',
        '21-36': '(b)만', '21-40': '(a)~(d)만', '21-41': '(e)~(h)만'}


def col_html(it, side, figinfo):
    en, ko, fb = figinfo
    if it['key'] == '21-18':
        en, ko, fb = Q22_EN, Q22_KO, None
    fig = ''
    if fb is not None:
        sc = min(1.3, COLW / fb.width, 190 / fb.height)
        fig = f'<div class="fig" data-fig="{it["key"]}" style="width:{fb.width * sc:.1f}pt;height:{fb.height * sc:.1f}pt"></div>'
    return f'''<div class="col {side}"><div class="ch"><span class="qb" style="background:{COL[it["ch"]]}">Q{it["q"]}</span>
<span class="t">{it["ch"]}장 · {NAMES[it["ch"]]}</span>{'<span class="must">★ 꼭 볼 문제</span>' if it.get('must') else ''}<span class="s">출처 {it["no"]} · 해설 p.{it["ap"]}</span></div>
<div class="pb">{f'<div class="pt">이 문항은 {PART[it["key"]]} 푼다</div>' if it['key'] in PART else ''}<div class="en">{en}</div><div class="ko">{ko}</div>{fig}</div>
<div class="bl"><span>✍ 풀이</span></div>
{ansvis.render(ansvis.V29[it["key"]], 1.25)}</div>'''


COV_CSS = """
.cv2 { display: grid; grid-template-columns: 286pt 1fr; height: 100% }
.cv2 .L { background: linear-gradient(160deg, #3b0d1c, #9c1f45 60%, #d1335b); color: #fff; padding: 34pt 26pt; display: flex; flex-direction: column; gap: 14pt }
.cv2 .k { font-size: 10pt; letter-spacing: 1.5pt; font-weight: 700; opacity: .85 }
.cv2 h1 { font-size: 33pt; font-weight: 900; line-height: 1.15 }
.cv2 h1 em { font-style: normal; color: #ffd166 }
.cv2 .box { background: rgba(0,0,0,.2); border-radius: 8pt; padding: 10pt 12pt; font-size: 10.6pt; line-height: 1.65 }
.cv2 .box b { color: #ffd166 }
.cv2 .box .h { font-weight: 800; font-size: 11pt; margin-bottom: 3pt; color: #fff }
.cv2 .R { padding: 24pt 24pt 20pt 22pt; display: flex; flex-direction: column }
.cv2 h2 { font-size: 12.5pt; font-weight: 800; color: #1d3557; display: flex; gap: 8pt; align-items: center; margin-bottom: 7pt }
.cv2 h2:after { content: ''; flex: 1; height: 1pt; background: #dde3ee }
.cv2 .tb2 { display: grid; grid-template-columns: 1fr 1fr; gap: 0 14pt }
.cv2 .rw { display: grid; grid-template-columns: 24pt 88pt 1fr 30pt 32pt 15pt 15pt; gap: 5pt; align-items: center; padding: 1.4pt 0; border-bottom: .7pt dotted #d5dbe6; font-size: 8.6pt; line-height: 1.2 }
.cv2 .rw.th2 { font-size: 8pt; color: #8a95a5; font-weight: 700; border-bottom: 1pt solid #c9d3ea; padding: 2pt 0 }
.cv2 .rw.th2 span { text-align: center } .cv2 .rw.th2 span:nth-child(3) { text-align: left }
.cv2 .qn { color: #fff; font-weight: 900; border-radius: 4pt; text-align: center; font-size: 8.4pt; line-height: 12pt }
.cv2 .no { font-weight: 800; color: #1d3557; white-space: nowrap; font-size: 8.4pt }
.cv2 .wy { color: #3a4556 }
.cv2 .pp { text-align: center; color: #6b7686; font-weight: 700; font-size: 9pt }
.cv2 .rw.mu { background: #fff6d6 } .cv2 .rw.mu .no { color: #a06800 }
.cv2 .bx { width: 10pt; height: 10pt; border: 1.2pt solid #9aa5b5; border-radius: 3pt; justify-self: center }
"""


def cover2(total, npg):
    cnt = {c: sum(1 for i in ITEMS if i['ch'] == c) for c in NAMES}
    chips = ''.join(f'<span style="background:{COL[c]};color:#fff;font-weight:800;font-size:9.6pt;border-radius:10pt;padding:2pt 9pt">{c}장 · {cnt[c]}문제</span>' for c in NAMES)
    hd = '<div class="rw th2"><span>번호</span><span style="text-align:left">출처</span><span>왜 나올 만한가</span><span>문제</span><span>해설</span><span>○</span><span>✗</span></div>'
    rows = [f'<div class="rw{" mu" if it.get("must") else ""}"><span class="qn" style="background:{COL[it["ch"]]}">{it["q"]}</span><span class="no">{"★ " if it.get("must") else ""}{it["no"]}</span>'
            f'<span class="wy">{it["why"]}</span><span class="pp">p.{it["qp"]}</span><span class="pp">p.{it["ap"]}</span>'
            f'<span class="bx"></span><span class="bx"></span></div>' for it in ITEMS]
    h = (N + 1) // 2
    return f"""<div class="pg"><div class="cv2"><div class="L">
<div class="k">약품유기화학 2 · 중간고사 17–21장</div>
<h1>시험 직전<br><em>막판 모의고사</em><br>{N}제</h1>
<div class="box"><div class="h">📌 교수님 출제 안내</div>약 <b>12문제</b> · 단원마다 1~2문제 · <b>21장 비중 ↑</b><br>답이 딱 떨어지는 문제<br>간단한 메커니즘은 <b>한 군데</b> 정도<br>산화·환원 메커니즘, 너무 어려운 문제는 <b>안 냄</b></div>
<div class="box"><div class="h">📖 이 파일 구성</div>p.2–{1 + npg} &nbsp;시험지 — 한 쪽에 2문제(왼쪽·오른쪽), 풀이 칸 밑에 <b>정답</b><br>p.{3 + npg}–{total} &nbsp;해설 — 해설 · 🎯 교수님 강조 · ⚡ 치트키 · 📝 내 필기</div>
<div class="box"><div class="h">✍ 푸는 법</div>① 정답을 손으로 가리고 시간 재며 풀기 (한 문제 4~5분)<br>② 오른쪽 표 ○ / ✗ 에 체크<br>③ ✗ 문항만 해설 쪽에서 치트키까지 확인</div>
</div><div class="R"><h2>문항 지도 · {N}문제 (21장 {cnt[21]}문제 = 21장 필기본 전 문제, 빨간 네모 제외)</h2>
<div style="font-size:10pt;color:#7a4b00;background:#fff6d6;border:1pt solid #f3d27a;border-radius:6pt;padding:4pt 9pt;margin-bottom:7pt">★ 노란 줄 = <b>꼭 볼 문제 {sum(1 for i in ITEMS if i.get("must"))}개</b> — 교수님이 짚은 포인트마다 대표 문항. 시간 없으면 이것만! &nbsp;· 변형 예상문제는 별도 파일 「예상문제 14제」</div>
<div style="display:flex;gap:6pt;flex-wrap:wrap;margin-bottom:9pt">{chips}</div>
<div class="tb2"><div>{hd}{"".join(rows[:h])}</div><div>{hd}{"".join(rows[h:])}</div></div></div></div>
<div class="foot">1 / {total}</div></div>"""


def q22_page(it, total):
    html = f"""<!doctype html><html><head><meta charset="utf-8"><style>{M.BASE_CSS}
.w {{ padding: 20pt 27pt 0 }}
.qh {{ display: flex; align-items: center; gap: 12pt; padding-bottom: 8pt; border-bottom: 2.4pt solid #1d3557 }}
.qh .b {{ background: #d1495b; color: #fff; border-radius: 9pt; padding: 3pt 12pt; text-align: center; line-height: 1.15 }}
.qh .b small {{ display: block; font-size: 8.5pt; font-weight: 700 }} .qh .b span {{ font-size: 19pt; font-weight: 900 }}
.qh h1 {{ font-size: 18pt; font-weight: 900; color: #1d3557 }} .qh .s {{ font-size: 9.5pt; color: #6b7686 }}
.ans {{ margin-top: 10pt; background: #dbe7fb; border-left: 4pt solid #2456c9; border-radius: 6pt; padding: 9pt 13pt; font-size: 12pt; line-height: 1.7; color: #1d3557 }}
.ans b {{ color: #2456c9 }}
.gg {{ display: grid; grid-template-columns: 1.15fr 1fr; gap: 14pt; margin-top: 12pt }}
.cd {{ border: 1pt solid #e1e6f0; border-radius: 7pt; padding: 10pt 13pt; font-size: 11.8pt; line-height: 1.7; background: #fbfcfe; margin-bottom: 12pt }}
.cd .t {{ font-weight: 800; color: #b3530c; font-size: 12.6pt; margin-bottom: 3pt }}
.flow {{ display: flex; align-items: center; gap: 6pt; flex-wrap: wrap; font-size: 11.2pt; margin: 4pt 0 }}
.flow span {{ background: #fff; border: 1pt solid #c9d3ea; border-radius: 5pt; padding: 2pt 7pt; font-weight: 700; color: #1d3557 }}
.flow i {{ font-style: normal; color: #8a95a5 }}
.hl {{ background: #fff1a8; padding: 0 2pt; border-radius: 2pt }}
.prof {{ display: flex; gap: 9pt; align-items: flex-start; background: #fff0f3; border: 1.3pt solid #f3a6b8; border-radius: 7pt; padding: 9pt 12pt; font-size: 11.6pt; line-height: 1.65; margin-bottom: 12pt }}
.prof .pt {{ background: #d1335b; color: #fff; font-weight: 800; font-size: 9.6pt; padding: 2pt 9pt; border-radius: 10pt; white-space: nowrap }}

.ckx {{ border-radius: 7pt; border: 1.2pt solid #c9d3ea; background: #f6f8fd; padding: 7pt 10pt }}
.ckx .tt {{ background: linear-gradient(90deg,#1d3557,#3a5a99); color: #fff; font-weight: 800; font-size: 10pt; padding: 2pt 10pt; border-radius: 10pt; display: inline-block; margin-bottom: 5pt }}
.ckx .it {{ background: #fff; border-left: 3.5pt solid #2a9d8f; border-radius: 5pt; padding: 7pt 10pt; font-size: 11.2pt; line-height: 1.6; margin-top: 7pt }}
.ckx .it.g {{ border-left-color: #7b5cd6 }}
.tg {{ font-size: 7.5pt; font-weight: 800; padding: .5pt 5pt; border-radius: 6pt; color: #fff; background: #2a9d8f; margin-right: 4pt }} .it.g .tg {{ background: #7b5cd6 }}
.ft {{ position: absolute; left: 27pt; bottom: 13pt; font-size: 8.6pt; color: #6b7686 }} .ft b {{ color: #d1495b; font-size: 10pt }}
</style></head><body><div class="pg"><div class="w">
<div class="qh"><div class="b"><small>개념형</small><span>Q22</span></div><div><h1>DCC 커플링 — 산 + 아민 → 아마이드</h1><div class="s">21-38 (DCC 메커니즘 문제)을 수업 내용 중심의 답 딱 떨어지는 형태로 바꿈 · §21.3</div></div></div>
<div class="ans"><b>정답</b> &nbsp;(a) 산-염기 반응이 먼저 일어나 <b>카복실레이트 염</b>(RCOO⁻ ⁺H₃NR′)이 된다 &nbsp;(b) <b>DCC · EDC</b> / <b>SOCl₂</b>로 산 염화물 → 아민<br>
(c) –OH → <b>O-acylisourea</b>(활성 중간체, 좋은 이탈기) · 부산물 <b>DCU</b>(다이사이클로헥실유레아) &nbsp;(d) 활성 중간체의 <b>부반응 억제</b> → 넣어 준 아민만 선택적으로 반응</div>
<div class="gg"><div>
<div class="cd"><div class="t">(a) 왜 그냥 섞으면 안 되나</div>아민은 <b>염기</b>이기도 하다 → 카복실산의 산성 H⁺(pKa ≈ 4–5)를 먼저 떼어 감 → <span class="hl">카복실레이트 음이온</span>.<br>
카복실레이트는 O⁻의 음전하가 카보닐과 공명 → C의 δ+가 약해져 친핵체(아민)의 공격을 <b>안 받는다</b>. 게다가 –OH(O⁻)는 원래 나쁜 이탈기.</div>
<div class="cd"><div class="t">(b)(c) 해결 = OH를 좋은 이탈기로 바꾸기 (활성화)</div>
<div class="flow"><span>R–COOH</span><i>→ DCC</i><span>O-acylisourea</span><i>→ R′NH₂ 공격</i><span>사면체 중간체</span><i>→</i><span>R–CO–NHR′ + DCU</span></div>
다른 길: <div class="flow"><span>R–COOH</span><i>→ SOCl₂</i><span>R–COCl</span><i>→ R′NH₂ (2당량 또는 + 염기)</i><span>R–CO–NHR′</span></div>
두 방법 모두 생각은 같다 — <b>사다리 맨 아래(산)를 위로 끌어올린 뒤 아민으로 내려오기</b>.</div>
<div class="cd"><div class="t">(d) HOBt</div>O-acylisourea에도 친전자성 자리가 있어 원치 않는 부반응이 생길 수 있다 → HOBt를 같이 넣으면 <b>선택적으로 넣어 준 친핵체(아민)만 반응</b>.</div>
</div><div>
<div class="prof"><span class="pt">🎯 교수님 강조</span><span>“카복실산 + 아민은 그냥 섞으면 반응성이 낮다 (카복실레이트가 되어 버림). 그래서 <b>DCC, EDC</b> 같은 커플링 시약이 <b>OH를 활성화</b>해 좋은 이탈기로 바꿔 준다. 단점은 부반응 → <b>HOBt</b> 보조제. OH를 <b>Cl로 바꾼 뒤 아민</b>을 넣는 방법도 많이 쓴다.” <span style="color:#8a6a3a">(21장 수업 녹취)</span></span></div>
<div class="ckx"><span class="tt">⚡ 1초 컷 치트키</span>
<div class="it g"><span class="tg">제미나이 치트키</span><b>반응성 사다리</b> — 산 염화물 &gt; 무수물 &gt; 에스터 &gt; 아마이드. 사다리를 강제로 올리려면 <b>SOCl₂</b> (약물 합성 문제의 핵심)</div>
<div class="it"><span class="tg">추가 꿀팁</span><b>DCC = 순한 SOCl₂</b>. 산 + 아민 → 염만 → DCC(EDC)로 OH 활성화 → 아마이드 + DCU. HOBt = 부반응 억제</div>
<div class="it"><span class="tg">추가 꿀팁</span>에스터 + 아민 → 아마이드는 이론상 가능하지만 느려서 거의 안 씀 (교수님) → 아마이드는 <b>산 염화물</b> 또는 <b>DCC</b>로</div>
<div class="it"><span class="tg">추가 꿀팁</span>원래 문제(21-38: 아미노산 2개 → 다이케토피페라진 메커니즘 그리기)는 단계가 많아 시험엔 안 나올 가능성이 큼 — 메커니즘 연습은 Q18(21-3)로</div>
</div></div></div></div>
<div class="ft"><b>Q22</b> &nbsp;정답과 해설 · 출처 21-38 개념형 · DCC 커플링 개념</div><div class="foot">{it["ap"]} / {total}</div></div></body></html>"""
    p = os.path.join(HERE, 'q22.html')
    open(p, 'w').write(html)
    subprocess.run(['node', os.path.join(HERE, 'render.js'), p, os.path.join(HERE, 'q22.pdf'), '-', '1134', '708.96'], check=True)
    return fitz.open(os.path.join(HERE, 'q22.pdf'))


def build(path):
    npg = (N + 1) // 2
    total = 1 + npg + 1 + N
    for i, it in enumerate(ITEMS):
        it['qp'] = 2 + i // 2
        it['ap'] = 2 + npg + 1 + i
    info = {it['key']: extract(it) for it in ITEMS}
    info['21-18'] = (Q22_EN, Q22_KO, None)
    pages = [cover2(total, npg)]
    for p in range(npg):
        pair = ITEMS[2 * p:2 * p + 2]
        body = ''.join(col_html(it, ('cl', 'cr')[j], info[it['key']]) for j, it in enumerate(pair))
        vs = '<div class="vs"></div>' if len(pair) == 2 else ''
        pages.append(f'<div class="pg">{body}{vs}<div class="foot">{2 + p} / {total}</div></div>')
    pages.append(f'''<div class="pg"><div class="dv"><h1>정답 · 해설</h1><p>정답은 문제 쪽에 있고, 여기는 해설 + 🎯 교수님 강조 + ⚡ 치트키<br>틀린 문항만 골라서 보기</p></div>
<div class="foot" style="color:#c9d3ea">{2 + npg} / {total}</div></div>''')
    hp = os.path.join(HERE, 'e2col.html')
    open(hp, 'w').write(f'<!doctype html><html><head><meta charset="utf-8"><style>{M.BASE_CSS}{M.EXAM_CSS}{CSS}{COV_CSS}{ansvis.CSS}</style></head><body>{"".join(pages)}</body></html>')
    subprocess.run(['node', os.path.join(HERE, 'render2.js'), hp, os.path.join(HERE, 'e2col.pdf'), os.path.join(HERE, 'e2col.json')], check=True)
    shell = fitz.open(os.path.join(HERE, 'e2col.pdf'))
    figs = json.load(open(os.path.join(HERE, 'e2col.json')))
    out = fitz.open()
    out.insert_pdf(shell)
    by = {it['key']: it for it in ITEMS}
    for f in figs:
        it = by[f['key']]
        fb = info[f['key']][2]
        out[f['page']].show_pdf_page(fitz.Rect(f['x'], f['y'], f['x'] + f['w'], f['y'] + f['h']), RAW, it['src'] - 1, clip=fb)
    toc = [[1, '표지 · 채점표', 1], [1, '시험지 (2문제/쪽)', 2]]
    toc += [[2, f'{"★ " if it.get("must") else ""}Q{it["q"]}  {it["no"]}', it['qp']] for it in ITEMS]
    toc.append([1, '정답 · 해설', 2 + npg])
    for it in ITEMS:
        if it['key'] == '21-18':
            out.insert_pdf(q22_page(it, total))
        else:
            out.insert_pdf(SRC, from_page=it['src'] - 1, to_page=it['src'] - 1)
            M.stamp_answer_page(out[-1], it, it['ap'], total, '정답과 해설')
        toc.append([2, f'Q{it["q"]}  {it["no"]}  {it["title"]}', it['ap']])
    out.set_toc(toc)
    out.set_metadata({'title': f'약품유기화학2 중간고사 막판 모의고사 {N}제 (2문제/쪽)', 'author': 'hwangzze'})
    out.save(path, garbage=4, deflate=True, use_objstms=1)
    print('exam2col', len(out))


if __name__ == '__main__':
    if 'dump' in sys.argv:
        for it in ITEMS:
            en, ko, fb = extract(it)
            print(it['key'], fb, '\n  EN:', en[:160], '\n  KO:', ko[:120])
    else:
        build(os.path.join(HERE, '..', 'exam29c.pdf'))
