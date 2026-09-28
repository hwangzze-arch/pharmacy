# -*- coding: utf-8 -*-
"""Landscape workbook: one problem per page (16:10, Samsung Notes friendly)."""
import sys, os, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from helpers import *
import content_a, content_b

HERE = os.path.dirname(os.path.abspath(__file__))
CHAPTER = '13'
CH_TITLE = '생체에너지론'
CH_EN = 'Bioenergetics and Biochemical Reaction Types'
# 난이도 ★★★ 문제는 제외 (사용자 요청 — 생화학 전 장 공통 규칙)
ITEMS = [i for i in content_a.ITEMS + content_b.ITEMS if i['level'] < 3]
EXCLUDED_HARD = [i['num'] for i in content_a.ITEMS + content_b.ITEMS if i['level'] >= 3]

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
.cover h1 { font-size: 36pt; line-height: 1.2; margin: 5mm 0 3mm; font-weight: 900; }
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


def stars(n):
    return '<span class="stars">' + '★' * n + '<i>' + '★' * (3 - n) + '</i></span>'


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
            if cls == 'item':
                foot = foot.replace('<span>' + str(i + 1), '<span><a class="back" href="#toc">↩ 차례로</a> &nbsp; ' + str(i + 1))
            if cls == 'front':
                inner = f'<div class="fw">{inner}</div>'
            out.append(f'<div class="pg {cls}">{inner}{foot}</div>')
        return '\n'.join(out)


def cover():
    nwe = sum(1 for i in ITEMS if i['kind'] != 'PROBLEM')
    npb = sum(1 for i in ITEMS if i['kind'] == 'PROBLEM')
    return f'''
<div class="eyebrow">LEHNINGER PRINCIPLES OF BIOCHEMISTRY · 8TH EDITION</div>
<h1>Chapter {CHAPTER}<br><span>{CH_TITLE}</span><br>예제 &amp; 문제 풀이 노트</h1>
<div class="sub">한 문제 = 한 페이지 · 원문 → 번역 → 직접 풀기 → 정답과 쉬운 해설</div>
<div class="en">{CH_EN}</div>
<div class="stats">
 <div class="stat"><b>{nwe}</b><span>본문 예제</span></div>
 <div class="stat"><b>{npb}</b><span>장말 연습문제<br>(강의 관련 · ★★★ 제외)</span></div>
 <div class="stat"><b>6</b><span>꼭 외울 공식</span></div>
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
    inc = [i['num'] for i in ITEMS if i['kind'] == 'PROBLEM']
    return f'''
<h2 class="pt"><span class="n">GUIDE</span> 이 노트에 담긴 것</h2>
<p class="lead">교수님 13장 강의(슬라이드 1–54) 범위 = <b>13.1 생체에너지론과 열역학</b>, <b>13.3 인산기 전달과 ATP</b>, <b>13.4 생물학적 산화-환원</b>. 이 범위와 연결된 예제·문제만 골랐어.</p>
<div class="grid3">
 <div class="card"><h4>✅ 포함 (예제 3 + 문제 {len(inc)})</h4>
  <p><b>본문 예제</b> 13-1, 13-2, 13-3</p>
  <p><b>ΔG′°·K′<sub>eq</sub>·ΔG 계산</b> — 문제 1–6, 9, 10, 13–15</p>
  <p><b>ATP·인산기 전달·공역</b> — 문제 7, 8, 12, 20–25</p>
  <p><b>능동수송 에너지</b> — 문제 26</p>
  <p><b>산화-환원 · 환원 전위</b> — 문제 27–33</p>
 </div>
 <div class="card"><h4>⛔ 제외</h4>
  <p><b>문제 {", ".join(EXCLUDED_HARD)}</b> — 난이도 ★★★ (여러 파트 종합형)</p>
  <p><b>문제 16–19</b> — 13.2절 반응 메커니즘 (강의 범위 밖)</p>
  <p><b>문제 36</b> — K<sub>m</sub>·V<sub>max</sub> (6장 내용)</p>
  <p><b>문제 37</b> — DATA ANALYSIS PROBLEM</p>
  <p class="small">난이도: {stars(1)} 공식 한 번 대입 · {stars(2)} 두세 단계</p>
 </div>
 <div class="card"><h4>📌 해설 박스 읽는 법</h4>
  {key('이 문제를 푸는 한 줄 아이디어')}{tip('일상 비유로 직관 잡기')}{warn('시험에서 자주 틀리는 포인트')}
 </div>
</div>
<div class="card" style="margin-top:4mm"><h4>🔢 자주 쓰는 숫자 (표 13-1)</h4>
<div class="tiles">
 <div><b>R</b><span>8.315 J/mol·K</span><small>kJ면 8.315×10<sup>−3</sup></small></div>
 <div><b>RT (25 °C)</b><span>2.478 kJ/mol</span><small>“표준 조건”</small></div>
 <div><b>RT (37 °C)</b><span>2.578 kJ/mol</span><small>“체온·생리적”</small></div>
 <div><b>F</b><span>96.48 kJ/V·mol</span><small>n = 전자 수 (NADH 2)</small></div>
 <div><b>RT/F (25 °C)</b><span>0.0257 V</span><small>E 농도 보정</small></div>
 <div><b>ATP → ADP + P<sub>i</sub></b><span>−30.5 kJ/mol</span><small>13장 기준값</small></div>
</div>
{warn('계산기의 <b>ln</b>(자연로그)과 <b>log</b>(상용로그)를 헷갈리지 말 것! ln x = 2.303 × log x.  그리고 mM → M은 ×10<sup>−3</sup>.')}
</div>'''


def cheat_page():
    down = svg(250, 110,
               '<path d="M10,30 C80,30 90,95 240,95" fill="none" stroke="#1e3a8a" stroke-width="3"/>'
               '<circle cx="36" cy="22" r="9" fill="#ea580c"/>' +
               T(30, 58, '반응물', 10.5, '#1e3a8a', weight=700) + T(215, 85, '생성물', 10.5, '#1e3a8a', weight=700) +
               arrowdef('cd', '#16a34a') +
               '<line x1="150" y1="34" x2="150" y2="86" stroke="#16a34a" stroke-width="2" marker-end="url(#cd)"/>' +
               T(158, 58, 'ΔG &lt; 0', 11, '#16a34a', 'start', 700) + T(158, 72, '내리막 = 저절로', 9.5, '#16a34a', 'start'))
    return f'''
<h2 class="pt"><span class="n">KIT</span> 먼저 이것만! 13장 계산 문제 생존 키트</h2>
<p class="lead">13장 계산 문제는 거의 전부 아래 6개 중 하나(또는 조합)야. 막히면 이 페이지로 돌아와.</p>
<div class="grid3">
 <div class="card"><h4><span class="no">1</span> ΔG의 부호 = 반응 방향</h4>
  <figure class="fig" style="margin:0">{down}</figure>
  <p><b>ΔG &lt; 0</b> 저절로 진행 · <b>ΔG = 0</b> 평형 · <b>ΔG &gt; 0</b> 역방향이 저절로. 공이 언덕을 굴러 내려가듯 G가 낮아지는 쪽으로.</p>
 </div>
 <div class="card"><h4><span class="no">2</span> ΔG′° ↔ K′<sub>eq</sub></h4>
  <div class="formula"><i>ΔG′°</i> = −<i>RT</i> ln <i>K′</i><sub>eq</sub></div>
  <div class="formula"><i>K′</i><sub>eq</sub> = e<sup>−ΔG′°/RT</sup></div>
  <p>K &gt; 1 ⇔ ΔG′° &lt; 0 · K &lt; 1 ⇔ ΔG′° &gt; 0</p>
  <p><b>10배 규칙</b>: 25 °C에서 K ×10 ⇔ ΔG′° −5.7 kJ/mol</p>
 </div>
 <div class="card"><h4><span class="no">3</span> 실제 ΔG = 표준값 + 농도 보정</h4>
  <div class="formula"><i>ΔG</i> = <i>ΔG′°</i> + <i>RT</i> ln <i>Q</i></div>
  <p>Q = {F('[생성물]', '[반응물]')} (지금 농도, <b>M 단위</b>, 물은 빼기)</p>
  <p>Q &lt; K → ΔG &lt; 0 → 정반응 / Q = K → 평형</p>
 </div>
 <div class="card"><h4><span class="no">4</span> 짝지은(공역) 반응</h4>
  <div class="formula"><i>ΔG′°</i><sub>합</sub> = <i>ΔG′°</i><sub>1</sub> + <i>ΔG′°</i><sub>2</sub> &nbsp;·&nbsp; <i>K′</i><sub>합</sub> = <i>K′</i><sub>1</sub> × <i>K′</i><sub>2</sub></div>
  <p>반응을 <b>뒤집으면 ΔG′° 부호 반대</b>, K는 역수(1/K).</p>
 </div>
 <div class="card"><h4><span class="no">5</span> 산화-환원: 전위차 → 자유에너지</h4>
  <div class="formula"><i>ΔE′°</i> = <i>E′°</i><sub>받는 쪽</sub> − <i>E′°</i><sub>주는 쪽</sub></div>
  <div class="formula"><i>ΔG′°</i> = −<i>nF ΔE′°</i></div>
  <p>전자는 E′°가 <b>낮은(−) 쪽 → 높은(+) 쪽</b>으로.</p>
 </div>
 <div class="card"><h4><span class="no">6</span> 실제 환원 전위</h4>
  <div class="formula"><i>E</i> = <i>E′°</i> + {F('<i>RT</i>', '<i>nF</i>')} ln {F('[산화형]', '[환원형]')}</div>
  <p>산화형(전자 받을 놈)이 많을수록 E가 커진다(+).</p>
 </div>
</div>'''


def tables_pages():
    t4 = table(['반응', 'ΔG′° (kJ/mol)'], [
        ['ATP + H<sub>2</sub>O → ADP + P<sub>i</sub>', '−30.5'], ['ATP + H<sub>2</sub>O → AMP + PP<sub>i</sub>', '−45.6'],
        ['PP<sub>i</sub> + H<sub>2</sub>O → 2P<sub>i</sub>', '−19.2'], ['포도당 6-인산 + H<sub>2</sub>O → 포도당 + P<sub>i</sub>', '−13.8'],
        ['젖당 + H<sub>2</sub>O → 포도당 + 갈락토스', '−15.9'], ['포도당 1-인산 → 포도당 6-인산', '−7.3'],
        ['과당 6-인산 → 포도당 6-인산', '−1.7'], ['말산 → 푸마르산 + H<sub>2</sub>O', '+3.1']], cls='left')
    t6 = table(['화합물 (가수분해)', 'ΔG′° (kJ/mol)'], [
        ['포스포엔올피루브산 (PEP)', '−61.9'], ['1,3-이인산글리세르산', '−49.3'], ['포스포크레아틴 (PCr)', '−43.0'],
        ['ADP (→ AMP + P<sub>i</sub>)', '−32.8'], ['ATP (→ ADP + P<sub>i</sub>)', '−30.5'], ['ATP (→ AMP + PP<sub>i</sub>)', '−45.6'],
        ['아세틸-CoA (티오에스터)', '−31.4'], ['과당 6-인산', '−15.9'], ['포도당 6-인산', '−13.8'], ['글리세롤 3-인산', '−9.2']], cls='left')
    t5 = table(['세포', 'ATP', 'ADP', 'AMP', 'P<sub>i</sub>', 'PCr'], [
        ['쥐 간세포', '3.38', '1.32', '0.29', '4.8', '0'], ['쥐 근육세포', '8.05', '0.93', '0.04', '8.05', '28'],
        ['쥐 뉴런', '2.59', '0.73', '0.06', '2.72', '4.7'], ['사람 적혈구', '2.25', '0.25', '0.02', '1.65', '0'], ['대장균', '7.90', '1.04', '0.82', '7.9', '0']])
    rows7 = [
        ['½O<sub>2</sub> + 2H<sup>+</sup> + 2e<sup>−</sup> → H<sub>2</sub>O', '<b>+0.816</b>'], ['Fe<sup>3+</sup> + e<sup>−</sup> → Fe<sup>2+</sup>', '+0.771'],
        ['시토크롬 c (Fe<sup>3+</sup>) + e<sup>−</sup> → (Fe<sup>2+</sup>)', '+0.254'], ['유비퀴논 + 2H<sup>+</sup> + 2e<sup>−</sup> → 유비퀴놀', '+0.045'],
        ['푸마르산 + 2H<sup>+</sup> + 2e<sup>−</sup> → 숙신산', '+0.031'], ['2H<sup>+</sup> + 2e<sup>−</sup> → H<sub>2</sub> (표준, pH 0)', '0.000'],
        ['옥살로아세트산 + 2H<sup>+</sup> + 2e<sup>−</sup> → 말산', '−0.166'], ['피루브산 + 2H<sup>+</sup> + 2e<sup>−</sup> → 젖산', '−0.185'],
        ['아세트알데하이드 + 2H<sup>+</sup> + 2e<sup>−</sup> → 에탄올', '−0.197'], ['FAD + 2H<sup>+</sup> + 2e<sup>−</sup> → FADH<sub>2</sub>', '−0.219'],
        ['리포산 + 2H<sup>+</sup> + 2e<sup>−</sup> → 다이하이드로리포산', '−0.29'],
        ['NAD<sup>+</sup> + H<sup>+</sup> + 2e<sup>−</sup> → NADH', '<b>−0.320</b>'], ['NADP<sup>+</sup> + H<sup>+</sup> + 2e<sup>−</sup> → NADPH', '−0.324'],
        ['아세토아세트산 + 2H<sup>+</sup> + 2e<sup>−</sup> → β-하이드록시뷰티르산', '−0.346'],
        ['α-케토글루타르산 + CO<sub>2</sub> + 2H<sup>+</sup> + 2e<sup>−</sup> → 아이소시트르산', '−0.38'],
        ['2H<sup>+</sup> + 2e<sup>−</sup> → H<sub>2</sub> (pH 7)', '−0.414'], ['페레독신 (Fe<sup>3+</sup>) + e<sup>−</sup> → (Fe<sup>2+</sup>)', '−0.432']]
    head7 = ['반쪽 반응 (산화형 + e<sup>−</sup> → 환원형)', 'E′° (V)']
    p1 = f'''<h2 class="pt"><span class="n">DATA</span> 문제에 나오는 교과서 표 모음</h2>
<p class="lead">문제에서 “Table 13-4 / 13-5 / 13-6을 이용하라”고 하면 여기서 찾으면 돼.</p>
<div class="grid3">
 <div class="card"><h4>표 13-4 · 표준 자유에너지 변화 (일부)</h4>{t4}</div>
 <div class="card"><h4>표 13-6 · 인산 화합물 가수분해 ΔG′°</h4>{t6}</div>
 <div class="card"><h4>표 13-5 · 세포 속 농도 (mM)</h4>{t5}</div>
</div>'''
    p2 = f'''<h2 class="pt"><span class="n">DATA</span> 표 13-7 · 표준 환원 전위 E′°</h2>
<p class="lead">위로 갈수록(+) 전자를 <b>받으려는</b> 힘이 세고, 아래로 갈수록(−) 전자를 <b>주려는</b> 힘이 세다. 전자는 <b>아래 → 위</b>로 흐른다.</p>
<div class="grid2">
 <div class="card">{table(head7, rows7[:9], cls='left')}</div>
 <div class="card">{table(head7, rows7[9:], cls='left')}</div>
</div>'''
    return p1, p2


def toc_page(first):
    rows = []
    for k, it in enumerate(ITEMS):
        lab = f"예제 {it['num']}" if it['kind'] != 'PROBLEM' else f"문제 {it['num']}"
        a = f'<a href="#{it["id"]}">'
        rows.append(f'<tr><td class="no">{a}{lab}</a></td><td>{a}{it["ko_title"]}</a></td><td>{a}{stars(it["level"])}</a></td>'
                    f'<td class="pgn">{a}{first + k} ›</a></td></tr>')
    half = (len(rows) + 1) // 2
    return f'''<h2 class="pt" id="toc"><span class="n">INDEX</span> 차례 <span style="font-size:9pt;color:#94a3b8;font-weight:500">— 항목을 누르면 해당 문제로 이동</span></h2>
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
    P.add(cheat_page(), 'front')
    for t in tables_pages():
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
    open(os.path.join(HERE, 'ch13.html'), 'w').write(doc)
    return first


if __name__ == '__main__':
    print('first item page', build(), 'items', len(ITEMS))
