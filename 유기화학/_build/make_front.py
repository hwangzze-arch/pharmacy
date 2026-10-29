# -*- coding: utf-8 -*-
"""표지 + 교수님 시험 안내 + 장 표지 5장(문항 목차) + 21장 수업 핵심 HTML."""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import make_slots as MS
from front_css import CSS
from selection import PROF, A_18, A_20SYN
STAR = {k for k, v in PROF.items() if v not in (A_18, A_20SYN)}

plan = json.load(open(os.path.join(HERE, 'plan.json')))
NAMES = {17: '알코올과 페놀', 18: '에터와 에폭사이드', 19: '알데하이드와 케톤', 20: '카복실산과 나이트릴', 21: '카복실산 유도체'}
EN = {17: 'Alcohols and Phenols', 18: 'Ethers and Epoxides', 19: 'Aldehydes and Ketones', 20: 'Carboxylic Acids and Nitriles', 21: 'Carboxylic Acid Derivatives'}
COL = {17: '#2a6f97', 18: '#2a9d8f', 19: '#7b5cd6', 20: '#e76f51', 21: '#d1495b'}
CHS = [17, 18, 19, 20, 21]
LEAD, AFTER = 2, {21: 1}

# 최종 쪽 번호 계산
cnt = {c: sum(1 for i in plan if i['ch'] == c) for c in CHS}
divp, pos = {}, LEAD
for c in CHS:
    divp[c] = pos + 1
    pos += 1 + AFTER.get(c, 0) + cnt[c]
TOTAL = pos
seq = {c: 0 for c in CHS}
for it in plan:
    c = it['ch']; seq[c] += 1
    it['final'] = divp[c] + AFTER.get(c, 0) + seq[c]
first = {c: divp[c] + AFTER.get(c, 0) + 1 for c in CHS}
last = {c: max(i['final'] for i in plan if i['ch'] == c) for c in CHS}
BYKEY = {i['key']: i for i in plan}
json.dump(plan, open(os.path.join(HERE, 'plan_final.json'), 'w'), ensure_ascii=False)


def chips(keys):
    return ' '.join(f'<span class="qc">{BYKEY[k]["no"]}<i>p.{BYKEY[k]["final"]}</i></span>' for k in keys if k in BYKEY)


EXTRA = """
.qc { display: inline-block; border: 1pt solid #d5dbe6; border-radius: 5pt; padding: 0 5pt; margin: 1.5pt 2pt 1.5pt 0; font-size: 10pt; font-weight: 700; color: #1d3557; background: #fff; white-space: nowrap }
.qc i { font-style: normal; font-weight: 500; color: #8a95a5; margin-left: 3pt }
.gd { display: grid; grid-template-columns: 330pt 1fr; height: 100% }
.gd-l { background: linear-gradient(165deg, #d1335b, #7a1f3d 120%); color: #fff; padding: 34pt 28pt; position: relative }
.gd-l .k { font-size: 10.5pt; letter-spacing: 2pt; font-weight: 700; opacity: .85 }
.gd-l h1 { font-size: 27pt; font-weight: 900; margin: 8pt 0 14pt; line-height: 1.2 }
.fact { display: flex; gap: 10pt; align-items: baseline; padding: 11pt 0; border-bottom: .8pt solid rgba(255,255,255,.22); font-size: 11.5pt; line-height: 1.4 }
.fact b.n { font-size: 20pt; font-weight: 900; min-width: 64pt; color: #ffd166 }
.no-box { margin-top: 18pt; background: rgba(0,0,0,.18); border-radius: 8pt; padding: 11pt 12pt; font-size: 11.5pt; line-height: 1.55 }
.no-box b { color: #ffd166 }
.gd-r { padding: 26pt 30pt 30pt 26pt; display: flex; flex-direction: column; gap: 9pt }
.gd-r h2 { font-size: 12.5pt; color: #1d3557; font-weight: 800; display: flex; gap: 8pt; align-items: center }
.gd-r h2:after { content: ''; flex: 1; height: 1pt; background: #dde3ee }
.ct { display: grid; grid-template-columns: 84pt 1fr; border: 1pt solid #e1e6f0; border-radius: 7pt; overflow: hidden; font-size: 12pt; line-height: 1.5 }
.ct .h { color: #fff; font-weight: 900; font-size: 15pt; display: flex; flex-direction: column; justify-content: center; align-items: center; line-height: 1.1 }
.ct .h small { font-size: 8.4pt; font-weight: 700; opacity: .9; margin-top: 2pt; text-align: center }
.ct .b { padding: 8pt 12pt; background: #fbfcfe }
.ct .say { font-weight: 700; color: #b0254a }
.ct .say:before { content: '🎯 ' }
.drop { font-size: 10.4pt; color: #4a5568; border: 1pt dashed #c3cad6; border-radius: 7pt; padding: 6pt 10pt; line-height: 1.5 }
.drop b { color: #1d3557 }
.star { color: #d1335b; font-weight: 900; margin-right: 2pt }

.lc { padding: 26pt 30pt 22pt; height: 100% }
.lc h1 { font-size: 22pt; font-weight: 900; color: #1d3557; display: flex; align-items: baseline; gap: 10pt }
.lc h1 small { font-size: 10.5pt; font-weight: 600; color: #6b7686 }
.lc .grid { display: grid; grid-template-columns: 1.35fr 1fr; gap: 12pt; margin-top: 10pt }
.lt { border-collapse: collapse; width: 100%; font-size: 11.2pt; line-height: 1.4 }
.lt th { background: #1d3557; color: #fff; font-weight: 700; padding: 4pt 6pt; text-align: left }
.lt td { border-bottom: .7pt solid #e1e6f0; padding: 5.4pt 6pt; vertical-align: top }
.lt td:first-child { font-weight: 700; white-space: nowrap }
.lt tr:nth-child(even) td { background: #f7f9fc }
.lt .hot td { background: #fff0f3 !important }
.card { border: 1pt solid #e1e6f0; border-radius: 7pt; padding: 8pt 11pt; font-size: 11.2pt; line-height: 1.55; margin-bottom: 10pt; background: #fbfcfe }
.card .t { font-weight: 800; color: #b0254a; font-size: 12pt; margin-bottom: 2pt }
.card .row { display: grid; grid-template-columns: 38pt 1fr; gap: 4pt; margin: 2pt 0 }
.card .tag { font-size: 8.4pt; font-weight: 800; color: #fff; border-radius: 4pt; text-align: center; padding: 1pt 0; height: fit-content }
.acid { background: #e76f51 } .base { background: #2a7ab0 }
"""


def cover():
    tiles = ''.join(f'''<div class="chc" style="background:{COL[c]}"><div class="n">{c}<small>장</small></div>
<div class="t">{NAMES[c]}</div><div class="e">{EN[c]}</div><div class="p">{cnt[c]}문항 · p.{divp[c]}–{last[c]}</div></div>''' for c in CHS)
    return f'''<div class="pg"><div class="cv">
<div class="cv-l"><div class="k">MIDTERM · CH 17–21 · 교수님 출제 포인트판</div>
<h1>약품유기화학 2<br><em>문제 + 해설</em><br>+ 1초 컷 치트키</h1>
<div class="sub">맥머리 유기화학 10판 17–21장<br>교수님이 말씀하신 범위 · 유형만 골라 {len(plan)}문항</div>
<span class="pill">🎯 교수님 강조</span><span class="pill">📝 내 필기 반영</span><span class="pill">⚡ 문항별 치트키</span>
<div class="bot">21장 수업 녹취록의 중간고사 안내를 기준으로<br>이름 붙이기·어려운 메커니즘·긴 합성·생화학 문항은 뺐다. 삼성노트 가로 보기용.</div></div>
<div class="cv-r">
<h2>CHAPTERS</h2><div class="chs">{tiles}</div>
<h2>한 페이지 읽는 법</h2>
<div class="how">
<div class="hw"><b class="t">① 문제</b>원문(영어) + 번역. 그림이 잘렸던 문항은 원서에서 다시 오려 넣었다.</div>
<div class="hw"><b class="t">② 📝 내 필기 · 🎯 교수님 강조</b>삼성노트 필기를 다시 편집하고, 이 문항에 해당하는 교수님 말씀을 분홍 띠로 붙였다.</div>
<div class="hw"><b class="t">③ ⚡ 1초 컷 치트키</b><span class="chip" style="background:#7b5cd6">제미나이 치트키</span> + <span class="chip" style="background:#2a9d8f">추가 꿀팁</span>. 남는 칸은 ✍ 메모.</div>
<div class="hw"><b class="t">④ 정답과 해설</b>통합풀이의 해설 그대로. 산화·환원 문항엔 🔄 일방통행 티켓 박스.</div>
</div>
<h2>시험장 단골 — 산화 · 환원 (생성물만! 메커니즘은 안 냄)</h2>{MS.REDOX}
</div></div><div class="foot">1 / {TOTAL}</div></div>'''


def k(ch, *pages):
    return [f'{ch}-{p}' for p in pages]


def guide():
    rows = [
        (17, '알코올·페놀', '방향족 고리에 치환기가 붙었을 때 → <b>산성도(pKa)</b> 차이', '페놀 산성도',
         k(17, 7, 9, 10, 11),
         '알코올을 만드는 법 = <b>산화(O 넣기) / 환원(O 빼기)</b> — 시약으로 생성물을 만들 수 있어야', '산화·환원·그리냐르',
         k(17, 13, 14, 15, 29, 30, 31, 16, 17, 22)),
        (18, '에터·에폭사이드', '따로 언급 없음 → 단원별 1~2문제 대비, <b>생성물 예측</b>만', '핵심 3종',
         k(18, 11, 13, 24, 25, 26, 31), '', '', []),
        (19, '알데하이드·케톤', '카보닐 화합물의 <b>산화·환원 관계</b>에 익숙해지기', '산화·환원',
         k(19, 7, 8, 18),
         '<b>1,2-첨가 vs 1,4-첨가</b> 중 어느 쪽이 유리한지', '1,2 vs 1,4', k(19, 34, 35, 36, 37, 38)),
        (20, '카복실산·나이트릴', '카복실산은 산 → <b>pKa 관점</b>으로 공부', 'pKa',
         k(20, 8, 9, 11, 12, 13, 14, 15), '', '', []),
        (21, '카복실산 유도체', '카복실산과 <b>다양한 친핵체</b>의 반응 — 21장 수업 복습 (새 단원이라 <b>비중 큼</b>)', '수업 핵심',
         k(21, 9, 12, 15, 18, 27, 32, 37, 38),
         '', '', []),
    ]
    html = ''
    for ch, nm, s1, l1, q1, s2, l2, q2 in rows:
        b = f'<div class="say">{s1}</div><div>{chips(q1)}</div>'
        if s2:
            b += f'<div class="say" style="margin-top:3pt">{s2}</div><div>{chips(q2)}</div>'
        if ch == 21:
            b += f'<div style="font-size:9.2pt;color:#4a5568;margin-top:2pt">→ 21장 표지 뒤 <b>“21장 수업 핵심”</b> 한 장 (p.{divp[21] + 1}) 에 녹취록 반응표·조건별 정리를 모아 둠</div>'
        html += f'<div class="ct"><div class="h" style="background:{COL[ch]}">{ch}장<small>{nm}</small></div><div class="b">{b}</div></div>'
    return f'''<div class="pg"><div class="gd">
<div class="gd-l"><div class="k">교수님 중간고사 안내 · 21장 수업 녹취</div><h1>이렇게 나온다</h1>
<div class="fact"><b class="n">17–21장</b><span>시험 범위</span></div>
<div class="fact"><b class="n">약 12문제</b><span>각 단원에서 <b>1~2문제</b>씩</span></div>
<div class="fact"><b class="n">21장 ↑</b><span>새로 배운 단원이라 비중이 큼</span></div>
<div class="fact"><b class="n">답 딱!</b><span>답이 딱 떨어지는 문제. 기본은 확실히</span></div>
<div class="fact"><b class="n">메커니즘</b><span><b>간단한 것 한 군데</b> 정도만</span></div>
<div class="no-box">❌ <b>산화·환원 메커니즘</b>처럼 그리기 까다로운 건 안 냄<br>❌ <b>너무 어려운 문제</b>는 안 냄<br>❌ 21장 별도 자료·문제 없음</div>
</div>
<div class="gd-r"><h2>단원별 교수님 포인트 → 이 책에서 볼 문항</h2>{html}
<div class="drop"><b>이번 판에서 뺀 것 (150 → {len(plan)}문항)</b> — 이름 붙이기·구조 그리기 · 그리기 까다로운 메커니즘(POCl₃ 탈수, 알콕시수은화, BBr₃, 이민 가수분해, 아세탈, 칸니차로) · 생화학 입체(NADH, 아이소시트르산) · 긴 다단계 합성(타목시펜, 이부프로펜, 펜클로락, 부타세틴, 19-62 ⓐ②ⓑⓒ) · 분자 모형 · 끓는점 · 싸이올 · 헨더슨–하셀바흐(원래 강의 제외)<br>
<span style="color:#8a95a5">※ 녹취 요약의 단원 추정(17=방향족, 18=알코올)은 교재 목차와 달라서 <b>내용 기준</b>으로 맞췄다: 페놀 산성도·알코올 산화/환원 = 교재 17장, 카보닐 = 19장.</span></div>
</div></div><div class="foot">2 / {TOTAL}</div></div>'''


def lecture21():
    tbl = [
        ('카복실산', '<b>염기</b>: 카복실레이트 + R–X (S<sub>N</sub>2)', '에스터', '카복실레이트가 친핵체, I⁻ 등이 이탈', False),
        ('카복실산', '<b>산</b>: 알코올 + 산 촉매 (피셔)', '에스터', '카보닐 O 양성자화 → C 친전자성 ↑', True),
        ('카복실산 + 아민', 'DCC · EDC (+ HOBt)', '아마이드', '그냥 섞으면 염만 생김 → OH 활성화', True),
        ('카복실산', 'OH → Cl (SOCl₂)', '아실 클로라이드', '가장 반응성 큰 유도체 = 활성화', True),
        ('에스터 · 아실 클로라이드', '그리냐르 (과량)', '3차 알코올', '케톤에서 못 멈추고 한 번 더', False),
        ('카복실산 · 에스터', 'LiAlH₄ → 후처리', '1차 알코올', 'H⁻ 4개, 알데하이드에서 못 멈춤', False),
        ('에스터', 'DIBAL-H, −78 °C', '알데하이드', '부피 큰 Al 사면체 중간체가 버팀', True),
        ('락톤', 'LiAlH₄', '고리 열린 다이올', 'C–O가 끊어짐', False),
        ('아마이드 · 락탐', 'LiAlH₄', '아민 (락탐은 고리형 아민)', 'C–N 유지, O만 빠짐', True),
        ('아마이드', '산: H₂O / 염기: OH⁻', '카복실산', '염기는 카복실레이트 → 중화', True),
    ]
    rows = ''.join(f'<tr class="{"hot" if h else ""}"><td>{a}</td><td>{b}</td><td><b>{c}</b></td><td>{d}</td></tr>' for a, b, c, d, h in tbl)
    return f'''<div class="pg"><div class="lc">
<h1>21장 수업 핵심 — 교수님 강의 그대로 <small>녹취록 정리 · 분홍 줄 = 교수님이 시간 들여 설명한 것</small></h1>
<div class="grid"><div>
<table class="lt"><tr><th>출발</th><th>시약 · 조건</th><th>생성물</th><th>핵심</th></tr>{rows}</table>
<div class="card" style="margin-top:9pt"><div class="t">반응성 순서 — 이유까지</div>
<b>아실 클로라이드 &gt; 무수물 &gt; 에스터·카복실산 &gt; 아마이드</b><br>
Cl: 전자를 끌어 C가 더 δ+ · 좋은 이탈기 / 아마이드: <b>N 비공유쌍이 카보닐로 공명</b> → 꼴찌 <span style="color:#b0254a">(전기음성도만 보고 착각 금지)</span><br>
EDG(알킬) 붙으면 반응성 ↓, EWG(Cl) 붙으면 ↑ · “OH를 좋은 이탈기로 = <b>활성화</b>”</div>
</div><div>
<div class="card"><div class="t">조건이 바뀌면 특징이 바뀐다 (교수님 강조)</div>
<div class="row"><span class="tag base">염기</span><span>카복실산 → 카복실레이트: 공명으로 C의 δ+ ↓ → 공격 <b>안 받음</b>. 대신 <b>자기가 친핵체</b>(R–X와 S<sub>N</sub>2 → 에스터)</span></div>
<div class="row"><span class="tag acid">산</span><span>카보닐 O 양성자화 → C 전자 부족 → 친핵체 첨가 → 사면체 → H⁺ 이동 → 물 이탈</span></div></div>
<div class="card"><div class="t">아마이드 가수분해</div>
<div class="row"><span class="tag acid">산</span><span>O 양성자화 → H₂O 공격 → 사면체 → NH₂가 <b>NH₃⁺</b> 되어 이탈 → 카복실산</span></div>
<div class="row"><span class="tag base">염기</span><span>OH⁻ 직접 공격 → 사면체 → <b>NH₂⁻</b> 이탈 → 산의 H 뺏어 <b>카복실레이트</b>(안정) → 중화하면 카복실산</span></div></div>
<div class="card"><div class="t">환원 3종 한 줄</div>
에스터·산 + <b>LAH</b> → 알코올 (O 남음, C–O 끊김)<br>아마이드 + <b>LAH</b> → 아민 (O 사라짐, C–N 유지, 이미늄 경유)<br>
에스터 + <b>DIBAL-H(−78 °C)</b> → 알데하이드 · 에스터 + <b>그리냐르</b> → 3차 알코올</div>
<div class="card"><div class="t">pKa와 선택성</div>
벤조산 ≈ 4 · 페놀 ≈ 10 · 아닐린 N–H ≫ (강한 산의 짝염기 = 약한 친핵체)<br>
<b>살리실산</b>: NaOH 충분하면 두 곳 다 O⁻ → 선택성은 친전자체 <b>1당량</b>으로<br>
<b>OH + NH₂</b> 방향족: NaOH면 페놀 OH만 O⁻ → O쪽 선택 / NH₂까지는 <b>NaH</b>급<br>
<b>1차 vs 2차 알코올</b>: 1차가 덜 붐벼 더 잘 반응 → 1차만 선택 가능</div>
</div></div>
<div style="font-size:8.6pt;color:#8a95a5;margin-top:4pt">녹취에서 시약명이 변형된 곳(“달달 H” = DIBAL-H, 염소화 시약 = SOCl₂로 추정, NaH 추정)은 슬라이드 기준으로 적었다.</div>
</div><div class="foot">{divp[21] + 1} / {TOTAL}</div></div>'''


def divider(c):
    items = [i for i in plan if i['ch'] == c]
    kinds = {kk: sum(1 for i in items if i['kind'] == kk) for kk in ['예제', '본문', '과제', '참고']}
    rows = ''.join(f'<div class="tr"><span class="kd {i["kind"]}">{i["kind"]}</span><span class="no">{i["no"]}</span><span class="tt">{"<span class=star>🎯</span>" if i["key"] in STAR else ""}{i["title"]}</span><span class="pp">{i["final"]}</span></div>' for i in items)
    dense = ' dense' if len(items) > 32 else ''
    st = ' · '.join(f'{kk} <b>{v}</b>' for kk, v in kinds.items() if v)
    return f'''<div class="pg"><div class="dv"><div class="dv-l" style="background:linear-gradient(165deg,{COL[c]},#1d3557 140%)">
<div class="k">CHAPTER</div><div class="n">{c}<small>장</small></div><h1>{NAMES[c]}</h1><div class="e">{EN[c]}</div>
<div class="st">총 <b>{len(items)}</b>문항<br>{st}<br>p.{first[c]}–{last[c]}</div></div>
<div class="dv-r"><h2>문항 목차 <span style="font-size:9pt;font-weight:600;color:#6b7686">🎯 = 교수님 말씀과 직결</span></h2><div class="toc{dense}">{rows}</div></div></div>
<div class="foot">{divp[c]} / {TOTAL}</div></div>'''


RX = MS.CSS[MS.CSS.index(".redox"):MS.CSS.index("/* 남는 칸")]
pages = [cover(), guide()]
for c in CHS:
    pages.append(divider(c))
    if c == 21:
        pages.append(lecture21())
html = (f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}{EXTRA}{RX}.cv-r .redox{{font-size:10.6pt}} '
        f'.cv-r .rx-t{{font-size:12pt}} .cv-r .rx-row{{grid-template-columns:120pt 1fr 1fr}}</style></head><body>{"".join(pages)}</body></html>')
open(os.path.join(HERE, 'front.html'), 'w').write(html)
print('total', TOTAL, divp, last)
