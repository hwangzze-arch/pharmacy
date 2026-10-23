# -*- coding: utf-8 -*-
# 7주차 붕해·용출·약물방출 최종 요약 생성기 (4-6주차 확산 최종 요약 형식)
import os
HERE = os.path.dirname(os.path.abspath(__file__))
FOOT = '물리약학 7주차 · 붕해, 용출, 약물 방출'
pages = []


def sub(x):
    return f'<sub>{x}</sub>'


Cs, Cp, Kr, Dm, Da, hm, ha, Cv = 'C' + sub('s'), 'C' + sub('p'), 'K' + sub('r'), 'D' + sub('m'), 'D' + sub('a'), 'h' + sub('m'), 'h' + sub('a'), 'C' + sub('v')


def foot():
    return f'<div class="foot"><span>{FOOT}</span><span>{{PN}}</span></div>'


def steps(items):
    return ''.join(f'<div class="step"><i>{i}</i><div>{t}</div></div>' for i, t in enumerate(items, 1))


def ul(items):
    return '<ul class="b">' + ''.join(f'<li>{t}</li>' for t in items) + '</ul>'


def table(head, rows, cls=''):
    h = ''.join(f'<th>{c}</th>' for c in head)
    body = ''
    for r in rows:
        ok = ''
        if r and r[0] == '!':
            ok, r = ' class="ok"', r[1:]
        body += f'<tr{ok}>' + ''.join(f'<td>{c}</td>' for c in r) + '</tr>'
    return f'<table class="{cls}"><thead><tr>{h}</tr></thead><tbody>{body}</tbody></table>'


def card(title, body, cls=''):
    t = f'<h3>{title}</h3>' if title else ''
    return f'<div class="card {cls}">{t}{body}</div>'


def formula(f, s=''):
    return f'<div class="formula"><div class="f">{f}</div>' + (f'<div class="s">{s}</div>' if s else '') + '</div>'


def box(kind, label, body):
    return f'<div class="box {kind}"><b>{label}</b> {body}</div>'


def concept(part, code, title, en, lead, left, right, cols='1fr 1fr'):
    pages.append(f'''<section class="page p{part}">
<div class="hd"><span class="tag">PART {part} · {code}</span><h1>{title}</h1><span class="en">{en}</span></div>
<div class="lead">{lead}</div>
<div class="grid" style="grid-template-columns:{cols}"><div>{left}</div><div>{right}</div></div>
{foot()}</section>''')


def divider(part, title, q, items):
    li = ''.join(f'<div><span>{a}</span>{b}</div>' for a, b in items)
    pages.append(f'''<section class="page div p{part}">
<div class="big">PART {part}</div><h2>{title}</h2><div class="q">{q}</div>
<div class="list">{li}</div>{foot()}</section>''')


def problem(part, n, title, src, rel, q, chs, easy, ans, ans_steps, right, one=False, mh=105):
    ch = ''
    if chs:
        ch = f'<div class="chs{" one" if one else ""}">' + ''.join(f'<div>{"①②③④⑤"[i]} {c}</div>' for i, c in enumerate(chs)) + '</div>'
    erows = ''.join(f'<tr><td>{a}</td><td>{b}</td></tr>' for a, b in easy[1])
    pages.append(f'''<section class="page p{part}">
<div class="ph"><span class="n">{n:02d}</span><h1>{title}</h1><span class="src">{src}</span><span class="rel">관련 개념 ▸ <b>{rel}</b></span></div>
<div class="prow"><div class="orig"><span class="lbl">원문</span><div class="q">{q}</div>{ch}</div>
<div class="easy"><span class="lbl e">쉬운 말 번역</span><div class="t">{easy[0]}</div><table>{erows}</table></div></div>
<div class="mine" style="--mh:{mh}px"><span>✏️ 내 풀이</span></div>
<div class="ans"><div><div class="al"><span class="x">정답</span><b>{ans}</b></div>{steps(ans_steps)}</div><div>{right}</div></div>
{foot()}</section>''')


def ctab(rows):
    """rows: (ok?, mark, text)"""
    out = ''
    for ok, m, t in rows:
        out += f'<tr{" class=ok" if ok else ""}><td class="m">{m}</td><td>{t}</td></tr>'
    return f'<table class="ctab"><tbody>{out}</tbody></table>'


# ============================== SVG figures
def svg_patterns(w=330, h=170):
    return f'''<svg viewBox="0 0 330 170" width="{w}" height="{h}">
<line x1="34" y1="140" x2="318" y2="140" stroke="#333"/><line x1="34" y1="140" x2="34" y2="10" stroke="#333"/>
<text x="300" y="156" font-size="11">t</text><text x="8" y="16" font-size="11">Q</text>
<line x1="34" y1="140" x2="300" y2="22" stroke="#12957f" stroke-width="2.6"/>
<path d="M34,140 C38,95 70,78 120,66 S240,48 300,42" fill="none" stroke="#8e3fbf" stroke-width="2.6"/>
<path d="M34,140 C64,82 105,66 160,62 S265,60 300,60" fill="none" stroke="#c9461d" stroke-width="2.6"/>
<text x="150" y="26" font-size="11" fill="#12957f" font-weight="700">0차: Q = Q₀ + K₀t (직선)</text>
<text x="196" y="102" font-size="11" fill="#8e3fbf" font-weight="700">Higuchi: Q ∝ √t</text>
<text x="196" y="118" font-size="11" fill="#c9461d" font-weight="700">Noyes-Whitney: 포화로 접근</text>
</svg>'''


def svg_rates(w=330, h=150):
    return f'''<svg viewBox="0 0 330 150" width="{w}" height="{h}">
<line x1="34" y1="125" x2="318" y2="125" stroke="#333"/><line x1="34" y1="125" x2="34" y2="10" stroke="#333"/>
<text x="300" y="141" font-size="11">t</text><text x="4" y="16" font-size="11">dQ/dt</text>
<line x1="34" y1="60" x2="300" y2="60" stroke="#12957f" stroke-width="2.6"/>
<path d="M38,14 C44,70 80,92 140,102 S250,110 300,112" fill="none" stroke="#8e3fbf" stroke-width="2.6"/>
<text x="200" y="52" font-size="11" fill="#12957f" font-weight="700">0차: 속도 일정</text>
<text x="160" y="92" font-size="11" fill="#8e3fbf" font-weight="700">Higuchi: ∝ 1/√t (감소)</text>
</svg>'''


def svg_disint():
    box = lambda x, y, w, t, c: f'<rect x="{x}" y="{y}" width="{w}" height="30" rx="7" fill="{c}" stroke="#4b55d6"/><text x="{x + w / 2}" y="{y + 19}" font-size="11.5" text-anchor="middle" font-weight="700">{t}</text>'
    arr = lambda x1, y1, x2, y2: f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#4b55d6" stroke-width="2" marker-end="url(#a1)"/>'
    return f'''<svg viewBox="0 0 360 230" width="350" height="224">
<defs><marker id="a1" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#4b55d6"/></marker>
<marker id="a2" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#c9461d"/></marker></defs>
{box(10, 8, 120, '정제 · 캡슐', '#eef0fc')}{arr(70, 38, 70, 66)}<text x="78" y="57" font-size="10.5" fill="#2f37a3" font-weight="700">붕해</text>
{box(10, 68, 120, '과립 · 뭉침', '#eef0fc')}{arr(70, 98, 70, 126)}<text x="78" y="117" font-size="10.5" fill="#2f37a3" font-weight="700">분산</text>
{box(10, 128, 120, '미세 입자', '#eef0fc')}
{box(225, 68, 125, '용액 속 약물', '#fff1a1')}
<line x1="130" y1="23" x2="222" y2="76" stroke="#c9461d" stroke-width="1.8" marker-end="url(#a2)"/>
<line x1="130" y1="83" x2="222" y2="83" stroke="#c9461d" stroke-width="1.8" marker-end="url(#a2)"/>
<line x1="130" y1="143" x2="222" y2="92" stroke="#c9461d" stroke-width="1.8" marker-end="url(#a2)"/>
<text x="160" y="72" font-size="10.5" fill="#c9461d" font-weight="700">용출</text>
{arr(287, 98, 287, 176)}<text x="295" y="140" font-size="10.5" fill="#2f37a3" font-weight="700">흡수</text>
{box(225, 178, 125, '혈중 · 조직 약물', '#e8f7ee')}
<text x="10" y="200" font-size="10" fill="#6b7280">용출은 세 단계 어디서든 일어나요 (작을수록 빠름)</text>
<text x="10" y="216" font-size="10" fill="#6b7280">붕해 + 분산 + 용출 전체 = 약물 방출</text>
</svg>'''


def svg_release_types():
    return '''<svg viewBox="0 0 340 170" width="330" height="165">
<line x1="30" y1="145" x2="330" y2="145" stroke="#333"/><line x1="30" y1="145" x2="30" y2="10" stroke="#333"/>
<text x="312" y="161" font-size="11">시간</text><text x="2" y="14" font-size="10.5">혈중 농도</text>
<rect x="30" y="70" width="300" height="34" fill="#e8f7ee"/><text x="250" y="66" font-size="9.5" fill="#15803d">치료 범위</text>
<path d="M30,145 C45,10 75,20 95,110 S130,145 160,145" fill="none" stroke="#c9461d" stroke-width="2.4"/>
<path d="M30,145 L110,145 C125,20 150,25 165,110 S200,145 230,145" fill="none" stroke="#8e3fbf" stroke-width="2.4" stroke-dasharray="5 3"/>
<path d="M30,145 C60,80 90,82 150,84 S260,90 320,118" fill="none" stroke="#12957f" stroke-width="2.6"/>
<text x="40" y="32" font-size="10.5" fill="#c9461d" font-weight="700">속방출 IR</text>
<text x="150" y="32" font-size="10.5" fill="#8e3fbf" font-weight="700">지연 방출 DR (늦게 시작)</text>
<text x="190" y="132" font-size="10.5" fill="#12957f" font-weight="700">서방출 ER (오래 유지)</text>
</svg>'''


def svg_oros():
    return '''<svg viewBox="0 0 340 190" width="330" height="184">
<defs><marker id="ab" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#1f6fb5"/></marker>
<marker id="ao" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#c9461d"/></marker></defs>
<rect x="70" y="30" width="200" height="110" rx="55" fill="#fff" stroke="#555" stroke-width="5"/>
<path d="M125,35 h-0 a50,50 0 0 0 0,100 h55 v-100 z" fill="#f6d5a8"/>
<path d="M180,35 h35 a50,50 0 0 1 0,100 h-35 z" fill="#cfe0f5"/>
<rect x="76" y="35" width="104" height="100" rx="48" fill="#f6d5a8"/>
<line x1="180" y1="35" x2="180" y2="135" stroke="#888" stroke-dasharray="4 3"/>
<text x="105" y="88" font-size="12" font-weight="700">약물층</text>
<text x="192" y="82" font-size="12" font-weight="700">push층</text><text x="188" y="97" font-size="9.5">(삼투 활성 고분자)</text>
<rect x="63" y="78" width="12" height="14" fill="#fff"/>
<line x1="64" y1="85" x2="14" y2="85" stroke="#c9461d" stroke-width="2.6" marker-end="url(#ao)"/>
<text x="4" y="72" font-size="10.5" fill="#c9461d" font-weight="700">약물 방출</text><text x="4" y="104" font-size="9.5" fill="#c9461d">(레이저 구멍)</text>
<line x1="322" y1="55" x2="284" y2="70" stroke="#1f6fb5" stroke-width="2" marker-end="url(#ab)"/>
<line x1="322" y1="118" x2="284" y2="103" stroke="#1f6fb5" stroke-width="2" marker-end="url(#ab)"/>
<text x="300" y="47" font-size="10.5" fill="#1f6fb5" font-weight="700">H₂O</text><text x="300" y="134" font-size="10.5" fill="#1f6fb5" font-weight="700">H₂O</text>
<text x="170" y="160" font-size="11" text-anchor="middle">바깥 = 반투막 (물만 통과, 약은 못 나감)</text>
<text x="170" y="178" font-size="11" text-anchor="middle" fill="#0b6b5b" font-weight="700">물 유입 속도 = 밀려나는 약 속도 = 일정 → 0차</text>
</svg>'''


def svg_nw():
    return '''<svg viewBox="0 0 340 180" width="330" height="175">
<rect x="20" y="20" width="80" height="130" fill="#d9c5ec"/><text x="60" y="90" font-size="11" text-anchor="middle" font-weight="700">고체 약</text>
<rect x="100" y="20" width="70" height="130" fill="#f5ecfb" stroke="#8e3fbf" stroke-dasharray="4 3"/>
<text x="135" y="168" font-size="10.5" text-anchor="middle">정적 확산층 h</text>
<text x="250" y="168" font-size="10.5" text-anchor="middle">bulk 용액 (부피 V)</text>
<polyline points="100,35 170,118 330,118" fill="none" stroke="#8e3fbf" stroke-width="2.8"/>
<text x="104" y="31" font-size="11" font-weight="700" fill="#6a2595">Cs (포화)</text>
<text x="250" y="110" font-size="11" font-weight="700" fill="#6a2595">C (bulk 농도)</text>
<line x1="100" y1="150" x2="170" y2="150" stroke="#333"/><text x="96" y="146" font-size="9">x=0</text><text x="163" y="146" font-size="9">x=h</text>
<text x="180" y="60" font-size="11" fill="#333">기울기 = (Cs − C)/h</text>
</svg>'''


def svg_higuchi():
    dots = ''.join(f'<circle cx="{x}" cy="{y}" r="2.6" fill="#6a2595"/>' for x in range(118, 196, 11) for y in range(38, 146, 11))
    return f'''<svg viewBox="0 0 340 185" width="330" height="180">
<rect x="20" y="28" width="180" height="125" fill="#efe4f8" stroke="#8e3fbf"/>
<rect x="20" y="28" width="88" height="125" fill="#fff" stroke="#8e3fbf" stroke-dasharray="4 3"/>{dots}
<text x="38" y="22" font-size="10.5" font-weight="700">고갈 영역 h</text><text x="125" y="22" font-size="10.5" font-weight="700">고체 약 A 남음</text>
<line x1="108" y1="20" x2="108" y2="160" stroke="#c9461d" stroke-dasharray="3 3"/><text x="94" y="174" font-size="10" fill="#c9461d">방출 경계 →</text>
<polyline points="20,150 108,60" fill="none" stroke="#c9461d" stroke-width="2.4"/>
<text x="112" y="58" font-size="10" fill="#c9461d" font-weight="700">Cs</text><text x="8" y="150" font-size="10" fill="#c9461d">0</text>
<text x="215" y="50" font-size="11" font-weight="700" fill="#6a2595">시간이 가면</text>
<text x="215" y="68" font-size="11">경계가 안쪽으로 이동</text>
<text x="215" y="86" font-size="11">→ 고갈 영역 h ↑</text>
<text x="215" y="104" font-size="11">→ 확산 거리 ↑</text>
<text x="215" y="122" font-size="11">→ 속도 ↓ (1/√t)</text>
<text x="215" y="146" font-size="11" font-weight="700" fill="#c9461d">h ∝ √t , Q ∝ √t</text>
</svg>'''


def svg_capsule():
    return '''<svg viewBox="0 0 340 185" width="330" height="180">
<rect x="20" y="25" width="85" height="125" fill="#dbe9f7"/><text x="62" y="18" font-size="10.5" text-anchor="middle" font-weight="700">캡슐 안 (Cp)</text>
<g fill="#1f6fb5">''' + ''.join(f'<circle cx="{x}" cy="{y}" r="4"/>' for x in range(34, 100, 16) for y in range(40, 145, 16)) + '''</g>
<rect x="105" y="25" width="50" height="125" fill="#f6d5a8"/><text x="130" y="18" font-size="10.5" text-anchor="middle" font-weight="700">막 hm</text>
<rect x="155" y="25" width="70" height="125" fill="#e9f2fb" stroke="#1f6fb5" stroke-dasharray="4 3"/><text x="190" y="18" font-size="10.5" text-anchor="middle" font-weight="700">물층 ha</text>
<text x="280" y="18" font-size="10.5" text-anchor="middle" font-weight="700">싱크</text>
<polyline points="20,45 105,45 155,95 155,110 225,145 330,145" fill="none" stroke="#c9461d" stroke-width="2.6"/>
<text x="110" y="70" font-size="10" fill="#c9461d">Cp→Cm</text><text x="158" y="92" font-size="10" fill="#c9461d">Cs (점프)</text>
<text x="232" y="138" font-size="10" fill="#c9461d">Cb ≈ 0</text>
<text x="170" y="170" font-size="11.5" text-anchor="middle" font-weight="700" fill="#134f86">R = hm/Dm + ha/DaKr ,  Q = P·Cp·t (0차)</text>
</svg>'''


def svg_kp():
    return '''<svg viewBox="0 0 330 180" width="320" height="175">
<line x1="40" y1="150" x2="310" y2="150" stroke="#333"/><line x1="40" y1="150" x2="40" y2="12" stroke="#333"/>
<text x="285" y="167" font-size="11">log t</text><text x="6" y="16" font-size="11">log f</text>
<line x1="40" y1="118" x2="300" y2="80" stroke="#1f6fb5" stroke-width="2.6"/>
<line x1="40" y1="128" x2="300" y2="58" stroke="#c9461d" stroke-width="2.6"/>
<line x1="40" y1="145" x2="300" y2="22" stroke="#12957f" stroke-width="2.6"/>
<text x="52" y="22" font-size="11" fill="#12957f" font-weight="700">― n &gt; 0.89 침식 동반 (가파름)</text>
<text x="52" y="38" font-size="11" fill="#c9461d" font-weight="700">― 0.45 &lt; n &lt; 0.89 변칙적</text>
<text x="52" y="54" font-size="11" fill="#1f6fb5" font-weight="700">― n = 0.45 Fick 확산 (완만)</text>
<text x="175" y="140" font-size="10.5" fill="#6b7280">기울기 = n, 절편 = log k</text>
</svg>'''


def svg_bcs():
    cell = lambda x, y, t, s, c, a: f'<rect x="{x}" y="{y}" width="120" height="62" rx="6" fill="{c}" stroke="#999"/><text x="{x + 60}" y="{y + 20}" font-size="12.5" text-anchor="middle" font-weight="800">{t}</text><text x="{x + 60}" y="{y + 37}" font-size="10" text-anchor="middle">{s}</text><text x="{x + 60}" y="{y + 52}" font-size="10" text-anchor="middle" fill="#b91c1c" font-weight="700">{a}</text>'
    return f'''<svg viewBox="0 0 300 175" width="300" height="175">
<line x1="30" y1="160" x2="290" y2="160" stroke="#333" marker-end="url(#a1)"/><line x1="30" y1="160" x2="30" y2="6" stroke="#333"/>
<text x="235" y="174" font-size="10.5" font-weight="700">투과도 →</text><text x="2" y="12" font-size="10.5" font-weight="700">용해도</text>
{cell(38, 14, 'Class III', '용해 ↑ · 투과 ↓', '#fff6d6', '율속: 막 투과')}{cell(164, 14, 'Class I', '용해 ↑ · 투과 ↑', '#e8f7ee', '90% 이상 흡수')}
{cell(38, 88, 'Class IV', '용해 ↓ · 투과 ↓', '#fdecec', '상용화 어려움')}{cell(164, 88, 'Class II', '용해 ↓ · 투과 ↑', '#fff6d6', '율속: 용출')}
</svg>'''


# ============================== 01 표지
pages.append(f'''<section class="page cover">
<div class="k">PHYSICAL PHARMACY · WEEK 7 · CH.13</div>
<h1>붕해, 용출, 약물 방출 (Drug Release)<br>쉽게 정리 + 문제 12개 완전 해설</h1>
<div class="sub">7주차 게시용 1 · 2와 본수업(수정반영)을 한 권으로 — 4~6주차 확산(Fick 법칙)만 기억하면 따라올 수 있어요</div>
<div class="how">이렇게 보세요 → <span class="p">① 개념 요약</span><span class="p">② 원문 문제</span><span class="p">③ 쉬운 말 번역</span><span class="p">④ 직접 풀기 ✏️</span><span class="p">⑤ 정답·해설</span></div>
<div class="parts">
<div><b>0 · 기초 준비</b>Q와 dQ/dt 읽기 · 그래프 3모양 · 확산 복습 · 기호</div>
<div><b>PART 1 · 용어·제형</b>붕해→분산→용출 · IR/DR/ER/CR · 방출 패턴 → 문제 01</div>
<div><b>PART 2 · 0차 방출</b>Q = Q₀ + K₀t · OROS · 패치 · 구동력 → 문제 02–03</div>
<div><b>PART 3 · 1차 방출</b>Noyes-Whitney · 싱크 · Higuchi 유도 Q ∝ √t ★★ → 문제 04–08</div>
<div><b>PART 4 · 확장 모델</b>Higuchi 2 (ε, τ) · Bottari · Korsmeyer-Peppas → 문제 09–10</div>
<div><b>PART 5 · 캡슐·BCS</b>저항의 합 · 막/확산층 제어 · BCS 4칸 · 한 장 정리 → 문제 11–12</div>
</div>{foot()}</section>''')

# ============================== 02 시작 전에
pages.append(f'''<section class="page p1">
<div class="hd"><span class="tag">시작 전에</span><h1>이것만 알면 방출 단원이 다 풀린다 — 기초 4가지</h1><span class="en">Basics</span></div>
<div class="grid" style="grid-template-columns:1fr 1fr">
<div>
{card('<b class="c">①</b> Q와 dQ/dt — "누적량"과 "속도"를 구분하기',
 '<p><b>Q</b> = 단위 면적당 <mark>지금까지 나온 약의 총량</mark> (누적량, 절대 줄지 않아요).</p>'
 '<p><b>dQ/dt</b> = 지금 이 순간 나오는 <mark>속도</mark> = Q 그래프의 기울기.</p>'
 '<p class="mut">문제에서 "방출량"이면 Q, "방출 속도·순간속도"면 dQ/dt. 여기서 틀리는 사람이 제일 많아요.</p>')}
{card('<b class="c">②</b> 그래프 세 모양만 외우기', '<div class="fig">' + svg_patterns(330, 150) + '</div>'
 '<p class="mut">직선 = 0차 · 루트 곡선 = Higuchi(√t) · 위로 평평해지는 곡선 = Noyes-Whitney(포화로 접근)</p>')}
</div>
<div>
{card('<b class="c">③</b> 출발점은 전부 확산(4~6주차)',
 '<p>모든 방출식은 <b>J = D·ΔC/h</b> (Fick 제1법칙, 얇은 막)에서 시작해요. 달라지는 건 <mark>ΔC와 h가 시간에 따라 변하느냐</mark>뿐.</p>'
 + table(['모델', 'ΔC', 'h (확산 거리)', '결과'], [
     ['0차 (막·삼투)', '일정', '일정', '속도 일정'],
     ['Noyes-Whitney', 'Cs − C ↓', '일정', '속도 감소'],
     ['Higuchi', '일정 (Cs − 0)', '커짐 ∝ √t', '속도 ∝ 1/√t'],
     ['캡슐', 'Cp 일정', '일정 (막+물층)', '0차'],
 ]), 'tint')}
{card('<b class="c">④</b> 기호 감각',
 table(['기호', '뜻', '단위'], [
     ['Q', '단위 면적당 방출된 약 양', 'mg/cm²'],
     ['A', '매트릭스 속 약 총 농도 (녹은 것 + 고체)', 'mg/cm³'],
     ['Cs', '포화 농도 (최대로 녹을 수 있는 농도)', 'mg/cm³'],
     ['h', '확산 거리 (정적 확산층·고갈 영역)', 'cm'],
     ['S · V', '표면적 · bulk 용액 부피', 'cm² · cm³'],
 ]))}
<div class="box ex"><b>전체 흐름 한 줄</b> 제형이 부서지고(붕해) → 흩어지고(분산) → 녹아야(용출) 흡수된다. 녹는 속도를 식으로 쓴 게 방출 동력학이고, 제형 구조에 따라 0차 / √t / tⁿ 로 갈린다.</div>
</div></div>{foot()}</section>''')

# ============================== PART 1
divider(1, '붕해·용출의 기초와 방출 제형', '"정제는 어떻게 녹아서 흡수되나?" — 7주차 약물 방출 1 (앞부분)',
        [('1-1', '용어 6개 — 붕해 · 분산 · 용출 · 약물 방출 ★'), ('1-2', '방출 제형 4가지 — IR · DR · ER · CR ★'),
         ('1-3', '방출 패턴 한눈에 — 0차 vs 1차 vs Higuchi'), ('문제', '01 (Summary 1 빈칸)')])

concept(1, '1-1 ★', '용어 6개 — 약품 · 약물 기질 · 붕해 · 분산 · 용출 · 약물 방출', 'Definitions',
        '정제 →(<em>붕해</em>) 과립 →(<em>분산</em>) 미세 입자 →(<em>용출</em>) 용액 →(흡수) 혈중. 이 전 과정이 <em>약물 방출</em>이에요.',
        card('정의 (강의 빈칸 그대로)', table(['용어', '정의', '영어'], [
            ['약품', '약물 기질을 함유한 <mark>최종 제형</mark> (정제·캡슐, 부형제 포함)', 'Drug product'],
            ['약물 기질', '직접적인 <mark>약리 효과</mark>를 내는 유효 물질', 'Drug substance'],
            ['붕해', '제형에서 빠져나와 <mark>과립·뭉침</mark> 형태로 나오는 것', 'Disintegration'],
            ['분산', '붕해된 덩어리가 <mark>개개의 입자</mark>가 되는 것', 'Deaggregation'],
            ['용출', '고체 입자가 물 같은 <mark>용액으로 녹아</mark> 들어가는 과정', 'Dissolution'],
            ['약물 방출', '고체상 → 액체상으로 녹아 들어가는 <mark>전 과정</mark>', 'Drug release'],
        ], 'l')) +
        box('ok', '기억법', '"붕분용" — 붕(부서짐) → 분(흩어짐) → 용(녹음). 약품 = 완제품, 약물 기질 = 그 안의 진짜 약(API).'),
        '<div class="fig">' + svg_disint() + '그림 13-2 재구성 — 붕해·분산·용출</div>' +
        box('warn', '단골 함정', '"붕해 = 약이 용액에 녹는 것" → ✕ (그건 용출). 흡수되려면 반드시 <b>용출(용액 상태)</b>을 거쳐야 해서, 난용성 약은 용출이 흡수의 율속 단계가 돼요 (→ BCS Class II).'))

concept(1, '1-2 ★', '방출 제형 4가지 — 속방출 · 지연 · 서방출 · 조절 방출', 'Types of drug release',
        '방출은 ADME와 맞물리는 과정이라 <em>방출 속도를 조절</em>하면 약효를 극대화할 수 있어요. "언제 시작하나 / 얼마나 오래 가나"로 구분!',
        card('4가지 제형 (강의 빈칸)', table(['제형', '설계 목적', '예'], [
            ['속방출 IR', '즉각 방출 → 흡수가 지연되지 않게', '일반 정제·캡슐'],
            ['지연 방출 DR', '<mark>일정 시간 후</mark>에 방출 시작', '<b>장용제</b> (위산 보호)'],
            ['서방출 ER', '방출 기간 <mark>연장</mark> → 투여 횟수 ↓', '1일 1회 서방정'],
            ['조절 방출 CR', '방출 <mark>시간·장소</mark>까지 설계', 'OROS, 경피 패치'],
        ], 'l')) +
        card('왜 이렇게 나누나?', ul(['IR은 빨리 올라가 빨리 떨어지는 뾰족한 혈중 농도 → 자주 먹어야 해요.',
                                    'ER/CR은 낮고 넓게 오래 유지 → <b>피크(부작용)↓, 트로프(효과 부족)↓</b>, 복약 순응도 ↑.',
                                    '친수성 고분자 매트릭스는 물을 먹고 <b>팽윤 → 겔층 → 바깥부터 침식</b>하며 천천히 방출 (서방).'])),
        '<div class="fig">' + svg_release_types() + '혈중 농도 모양으로 보는 IR · DR · ER</div>' +
        box('warn', '단골 함정', '장용제는 <b>지연 방출</b>이지 서방출이 아니에요. 지연 = "늦게 시작", 서방 = "오래 지속".') +
        box('ex', '연결', '0차 방출(PART 2)은 대표적인 <b>조절 방출</b> 방식이고, Higuchi·K-P 매트릭스(PART 3·4)는 대표적인 <b>서방출</b> 방식이에요.'))

concept(1, '1-3', '방출 패턴 한눈에 — 0차 vs 1차 vs Higuchi', 'Release patterns at a glance',
        '방출 패턴은 크게 <em>0차</em>(속도 일정)와 <em>1차</em>(속도가 점점 감소) 두 가지. 강의는 Higuchi(√t)도 "1차 방출 동력학"에 묶어요.',
        '<div class="fig">' + svg_patterns(340, 165) + '누적량 Q vs t</div>' + '<div class="fig" style="margin-top:8px">' + svg_rates(340, 140) + '속도 dQ/dt vs t</div>',
        table(['', '0차', '1차 (Noyes-Whitney)', 'Higuchi'], [
            ['누적량 Q', '∝ t (직선)', 'Cs로 지수적 접근', '∝ √t'],
            ['속도 dQ/dt', '<mark>일정</mark>', '(Cs − C)에 비례, 감소', '∝ 1/√t, 감소'],
            ['농도 영향', '<b>받지 않음</b>', '받음 (C ↑ → 속도 ↓)', '고갈 영역 h ↑ → 속도 ↓'],
            ['제형', 'OROS · 패치 · 캡슐', '고체 입자 용출', '평판 고분자 매트릭스'],
            ['확인 그래프', 'Q vs t 직선', 'ln(Cs − C) vs t 직선', '<b>Q vs √t 직선</b>'],
        ]) +
        card('그래프 판별 순서 (시험용)', ul(['Q vs t가 직선 → <b>0차</b>', 'Q vs √t가 직선 → <b>Higuchi</b>',
                                          'log f vs log t의 기울기 n → <b>Korsmeyer-Peppas</b>로 기전 판별 (PART 4)']), 'tint') +
        box('warn', '혼동 주의', '강의 분류상 Higuchi도 "1차 방출 동력학" 단원이지만, 수학적으로는 <b>1차 반응(지수함수)이 아니라 √t 법칙</b>이에요. 보기에 "1차반응으로 방출된다"와 "방출량 ∝ √t"가 같이 나오면 <b>√t</b>가 정답!'))

problem(1, 1, '용어 · 방출 종류 · 0차 방출 빈칸', 'Summary 1 · 본수업', '1-1 · 1-2 · 2-1',
        '다음 빈칸을 채우시오.<br>(가) ( ) : 약물 기질을 함유하고 있는 최종 제형 &nbsp;(나) ( ) : 약물이 제형으로부터 빠져나와 과립이나 뭉침 형태로 나오는 것<br>'
        '(다) ( ) : 고체상의 약물 입자들이 물과 같은 용액으로 녹아들어가는 과정 &nbsp;(라) ( ) : 일정 시간 후에 방출되도록 설계 Ex) 장용제<br>'
        '(마) 0차 방출은 시간에 따른 방출량이 (점차 감소 / 일정하게 유지)되며, (시간 / 방출 농도)에만 의존한다.', None,
        ('용어 정의를 보고 이름 맞히기 + 0차 방출의 성질 고르기', [('키워드', '최종 제형 · 과립 · 녹아들어감 · 일정 시간 후'), ('헷갈릴 것', '붕해 ↔ 용출, 지연 ↔ 서방'), ('구할 것', '용어 5개 + 0차 성질')]),
        '약품 · 붕해 · 용출 · 지연 방출 · 일정하게 유지 / 시간',
        ['(가) 완제품 = <b>약품</b> (약효 성분 자체는 약물 기질)', '(나) 덩어리로 부서짐 = <b>붕해</b> → 낱알로 흩어지면 분산',
         '(다) 녹아 들어감 = <b>용출</b>, (라) 늦게 시작 = <b>지연 방출</b>', '(마) 0차는 속도 <b>일정</b> → Q가 <b>시간</b>에만 비례, 농도와 무관'],
        table(['빈칸', '정답', '헷갈린 오답'], [
            ['(가)', '약품', '약물 기질 (= 유효 성분)'],
            ['(나)', '붕해', '분산 (개개 입자)'],
            ['(다)', '용출', '약물 방출 (전 과정)'],
            ['(라)', '지연 방출', '서방출 (투여 횟수 ↓)'],
            ['(마)', '일정 · 시간', '방출 농도 (1차의 특징)'],
        ]) + box('ex', '나머지 Summary 1 빈칸', '약물 기질 · 분산 · 약물 방출 · 속방출 · 서방출 · 조절 방출 — 1-1, 1-2 표 그대로.'), mh=95)

# ============================== PART 2
divider(2, '0차 방출 — 속도가 일정한 방출', '"매시간 똑같은 양이 나오게 할 수 있을까?" — 약물 방출 1 · 본수업',
        [('2-1', '0차 방출의 성질 — Q = Q₀ + K₀t'), ('2-2', 'OROS 삼투압 펌프 ★'),
         ('2-3', '물질수송의 구동력 4종'), ('문제', '02 – 03 (예제 + 작년 기출)')])

concept(2, '2-1', '0차 방출의 성질 — Q = Q₀ + K₀t', 'Zero-order release',
        '0차 = <em>속도가 일정</em> → 누적량은 <em>시간에 정비례</em> → 시스템 약물 농도에 <em>영향 받지 않음</em>.',
        formula('dQ/dt = K₀ (상수) &nbsp;⇒&nbsp; Q = Q₀ + K₀t', '속도를 적분하면 누적량 · K₀ = 기울기 (단위: 양/시간)') +
        card('0차 방출의 성질 4가지 (강의 빈칸)', steps(['약물 방출 속도가 <mark>일정</mark>함', '누적 약물 방출량은 시간에 <mark>비례</mark>함',
                                                  '방출 속도가 시스템 약물 농도에 <mark>영향 받지 않음</mark>',
                                                  '제형이 <mark>붕해되지 않는</mark> 경피 전달 시스템, 이식형 장치 등에 적용'])) +
        box('ex', '예시 (가정 수치)', 'K₀ = 2 mg/h, Q₀ = 0 → 3시간 6 mg, 12시간 24 mg. 속도는 언제나 2 mg/h.'),
        '<div class="fig">' + svg_patterns(330, 150) + '초록 직선이 0차</div>' +
        card('왜 농도에 영향을 안 받나?', ul(['추진력이 <b>일정하게 유지되도록 설계</b>했기 때문이에요.',
                                         '저장소가 <b>포화 상태로 유지</b> (패치·캡슐: 고체 약이 남아 있는 동안 C = Cs 고정)',
                                         '<b>삼투압</b>으로 밀어내는 속도가 일정 (OROS)',
                                         '6주차 경피 패치의 <b>Reservoir형 = 막 제어 0차 방출</b>과 같은 원리']), 'tint') +
        box('ok', '장점', '혈중 농도가 평탄하게 유지돼서 피크(부작용)와 트로프(효과 부족)를 줄여요.'))

concept(2, '2-2 ★', 'OROS 삼투압 펌프 — 물이 들어온 만큼 약이 밀려 나간다', 'Osmotic pump (OROS)',
        'OROS = 반투막 + <em>삼투 활성 폴리머(push층)</em> + 약물층 + <em>레이저 구멍</em>. 구동력은 <em>삼투압(압력)</em>, 방출은 <em>0차</em>.',
        '<div class="fig">' + svg_oros() + 'push-pull OROS 구조</div>' +
        card('작동 4단계', steps(['바깥 <b>반투막</b>: 물은 통과, 약은 못 나감', '물이 들어와 <b>push층(친수성 폴리머)이 지속적으로 팽창</b>',
                               '부푼 push층이 약물층을 밀어냄', '약은 <b>레이저 방출구 하나로만</b> 나감 → 일정한 속도'])),
        card('방출 속도 식 (보충)', formula('dM/dt = (A · k / h) · Δπ · C', 'A 막 면적 · k 막 투과성 · h 막 두께 · Δπ 삼투압 차 · C 약물 농도') +
             '<p class="mt">안쪽이 포화로 유지되는 동안 Δπ가 거의 일정 → <b>속도 일정 (0차)</b>. 위장관 pH나 운동에도 거의 영향을 안 받아요.</p>') +
        table(['바꾸면', '물 유입', '방출 속도'], [
            ['삼투압층 전해질 농도 ↑ (Δπ ↑)', '↑', '<b>↑</b>'],
            ['반투막 두께 h ↑', '↓', '↓'],
            ['반투막 표면적 A ↓', '↓', '↓'],
            ['방출 구멍 크기 ↓ (적정 범위)', '—', '거의 변화 없음'],
        ]) +
        box('warn', '단골 함정', '구멍을 작게 해도 속도는 안 빨라져요. 속도를 정하는 건 <b>물이 들어오는 속도(Δπ, A, k, h)</b>예요. → 문제 03') +
        box('ex', '예', '니페디핀 서방정(Procardia XL), 메틸페니데이트 서방정(Concerta). 경피 패치도 붕해되지 않는 0차 제형이에요.'))

concept(2, '2-3', '물질수송의 구동력 4종 — 무엇이 약을 움직이나', 'Driving forces of mass transport',
        '물질이 움직이려면 <em>차이(구배)</em>가 필요해요: <em>농도차 · 압력차 · 전위차 · 온도차</em>. 현상과 구동력을 짝짓는 문제가 단골!',
        table(['구동력', '흐름', '대표 현상'], [
            ['농도차 (화학 퍼텐셜)', '진한 곳 → 묽은 곳', '확산 (Fick 법칙), 동결건조 수증기 이동 (증기압 차)'],
            ['<mark>압력차</mark>', '높은 압력 → 낮은 압력', '<b>삼투적 약물방출(OROS)</b>, 한외여과, 대류'],
            ['전위차', '전하 ↔ 반대 극', '<b>전기영동</b>(DNA), <b>이온토포레시스</b>'],
            ['온도차', '고온 → 저온', '열전달, 증발·건조, <b>마이크로파 가열 추출</b>'],
        ], 'l') + card('외우는 법', ul(['이름에 "<b>전기</b>"가 들어가면 → 전위 (전기영동, 이온토포레시스)',
                                     '"<b>삼투</b>"는 → 압력 (삼투압도 압력이에요)',
                                     '"<b>열·마이크로파</b>"는 → 온도', '"<b>확산·증발</b>"은 → 농도(증기압)']), 'tint'),
        box('warn', '출제 패턴', '보기가 ②↔④, ③↔⑤처럼 구동력을 <b>엇갈려</b> 놓아요. "전기영동의 구동력은 압력" ✕, "이온토포레시스의 구동력은 온도" ✕.') +
        card('이온토포레시스가 뭐예요?', '<p>피부에 약한 전류를 걸어 <b>이온형 약물</b>을 피부 속으로 밀어 넣는 방법이에요. 전하를 띤 약이 같은 극에서 밀려나가니 구동력은 <b>전기 전위</b>.</p>') +
        card('동결건조에서 수증기는?', '<p>얼음이 승화해서 생긴 수증기는 <b>증기압(농도)이 높은 곳 → 낮은 곳(응축기)</b>으로 확산해요. 전기 전위와는 무관.</p>'))

problem(2, 2, '물질수송의 예와 구동력', '예제 · Quiz 2', '2-3 구동력',
        '물질수송의 예와 그 주된 구동력(driving force)에 대한 설명으로 옳은 것은?',
        ['삼투적 약물방출시스템의 구동력은 압력이다.', '전기영동에서 DNA 이동의 구동력은 압력이다.', '동결건조 시 수증기의 확산에서 구동력은 전기 전위이다.',
         '이온토포레시스를 이용한 약물전달의 구동력은 온도이다.', '마이크로파를 이용한 물질의 추출에서 구동력은 전기 전위이다.'],
        ('각 현상에서 물질을 움직이는 "원인"이 맞게 짝지어진 것은?', [('키워드', '삼투 · 전기영동 · 동결건조 · 이온토포레시스 · 마이크로파'), ('헷갈릴 보기', '②④ 전기 관련, ③⑤ 전위↔온도'), ('구할 것', '맞는 짝 1개')]),
        '① 삼투 = 압력',
        ['OROS는 반투막으로 물이 들어와 생긴 <b>삼투압</b>이 약을 밀어냄', '삼투압은 압력의 한 종류 → ① 옳음', '나머지는 구동력을 서로 바꿔 놓은 함정'],
        ctab([(True, '①', '삼투 → 압력 ✓'), (False, '②', '전기영동 DNA → <b>전기 전위</b> (음전하 DNA가 +극으로)'),
              (False, '③', '동결건조 수증기 → <b>증기압(농도) 차</b>'), (False, '④', '이온토포레시스 → <b>전기 전위</b>'),
              (False, '⑤', '마이크로파 추출 → <b>온도</b> (가열)')]) +
        box('ex', '같은 문제', '7주차 게시용 1 예제, 본수업 Quiz 2·예제 — 세 번 나온 문제예요.'), one=True, mh=80)

problem(2, 3, 'push-pull OROS 방출속도 증가', '작년 기출 11번', '2-2 OROS',
        '다음은 push-pull OROS 삼투압 펌프 제제의 설계에 관한 것이다. 제제의 정상상태 약물 방출속도를 증가시킬 수 있는 방법은?<br>'
        '<span class="mut">• 약물층과 전해질을 포함한 삼투압층으로 구성된 2층 정제 제조 • 반투막으로 정제 코팅 • 약물층의 반투막에 약물방출 구멍 형성</span>',
        ['반투막 두께 증가', '반투막 표면적 감소', '약물방출 구멍 크기 감소', '삼투압층 전해질 농도 증가', '제제 내부로 용매 유입속도 감소'],
        ('물을 더 빨리 빨아들이게 하려면 무엇을 바꿔야 하나?', [('키워드', '정상상태 방출속도 증가'), ('핵심 식', 'dM/dt = (A·k/h)·Δπ·C'), ('구할 것', '속도를 ↑시키는 설계')]),
        '④ 삼투압층 전해질 농도 증가',
        ['방출 속도 = 물이 들어오는 속도 (들어온 물 부피만큼 약이 밀려남)', '물 유입은 Δπ(삼투압 차)·면적 A에 비례, 막 두께 h에 반비례',
         '전해질 농도 ↑ → <b>Δπ ↑</b> → 물 유입 ↑ → 방출 ↑'],
        ctab([(False, '①', '두께 h ↑ → 분모 ↑ → 물 유입 ↓ → 방출 ↓'), (False, '②', '면적 A ↓ → 물 유입 ↓ → 방출 ↓'),
              (False, '③', '구멍 크기는 적정 범위에서 속도를 정하지 않음'), (True, '④', 'Δπ ↑ → 방출 ↑ ✓'),
              (False, '⑤', '용매 유입 ↓ → 밀어내는 부피 ↓ → 방출 ↓')]) +
        box('warn', '함정', '"구멍을 작게 하면 압력이 세져서 빨리 나온다"는 직관 ✕. 속도는 물 유입이 정해요.'), one=True, mh=80)

# ============================== PART 3
divider(3, '1차 방출 — Noyes-Whitney와 Higuchi', '"녹을수록, 비어갈수록 왜 느려질까?" — 약물 방출 1 (뒷부분) · 본수업',
        [('3-1', 'Noyes-Whitney 방정식 — 정적 확산층 ★★'), ('3-2', '싱크 조건 · 용출 속도 올리는 법'),
         ('3-3', 'Higuchi ① 고갈 영역과 물질수지 ★'), ('3-4', 'Higuchi ② h(t)와 Q 유도 ★★'),
         ('3-5', 'Higuchi ③ Q ∝ √t · 가정 4개 ★'), ('문제', '04 – 08 (예제 · Quiz · 2024 중간 11번)')])

concept(3, '3-1 ★★', 'Noyes-Whitney 방정식 — 고체가 녹는 속도', 'Noyes–Whitney equation',
        '고체 표면은 <em>포화 농도 Cs</em>, 정적 확산층(두께 h)을 지나 bulk 농도 C로 떨어져요. 얇은 막 확산식을 그대로 적용 → <em>dM/dt = (SD/h)(Cs − C)</em>.',
        '<div class="fig">' + svg_nw() + '고체상 Matrix로부터의 약물 방출 — 정적 확산층 모델</div>' +
        card('유도 4단계 (확산 → Noyes-Whitney)', steps([
            '얇은 막 식 J = dM/(S·dt) = (DK/h)(C₁ − C₂) 에서 막 = <b>물층</b> → K = 1',
            'C₁ = 고체 표면 = <b>포화 농도 Cs</b>, C₂ = bulk 농도 <b>C</b>',
            '양변 × S → <b>dM/dt = (SD/h)(Cs − C)</b>',
            'bulk 부피 V로 나눔 (C = M/V) → <b>dC/dt = (DS/Vh)(Cs − C)</b>'])),
        formula('dM/dt = (S·D / h) · (Cs − C)', 'D 확산계수 · S 표면적 · h 확산층 두께 · Cs 포화 농도 · C bulk 농도 — <b>K(분배계수)는 없음!</b>') +
        card('왜 "1차"인가?', '<p>k = DS/Vh로 두면 dC/dt = k(Cs − C) → <b>남은 농도차에 1차 비례</b>. 풀면 C = Cs(1 − e<sup>−kt</sup>) — 포화로 지수적으로 다가가는 곡선이에요.</p>'
             '<p>녹아 나온 약(C)이 쌓일수록 추진력(Cs − C)이 줄어 → <mark>방출 속도가 점차 감소</mark> (강의 빈칸).</p>', 'tint') +
        box('warn', '단골 함정', 'Noyes-Whitney에 들어가지 <b>않는</b> 항 = <b>K(분배계수)</b>. K는 막 투과(P = DK/h)에서 나와요. → 문제 06') +
        box('ex', '대상', '(액상 / <b>고체 제형</b>)에서 약물이 용출되는 속도를 기술 — Summary 2 빈칸.'))

concept(3, '3-2', '싱크 조건 · 용출 속도를 올리는 법', 'Sink condition · speeding up dissolution',
        '<em>싱크</em> = bulk 농도 C ≈ 0 (Cs의 10~20% 이하). 그러면 C를 무시해 <em>dM/dt = DSCs/h</em> — 표면적이 일정한 동안 일정한 속도.',
        formula('dM/dt = (SD/h)(Cs − C) &nbsp;→(싱크, C ≈ 0)→&nbsp; dM/dt = DS·Cs / h') +
        card('싱크는 왜 중요?', ul(['<b>용출 시험</b>: 용액을 충분히 크게 해서 싱크를 맞춰야 제형 자체 성질로만 비교 가능',
                                  '<b>체내</b>: 녹은 약이 장막으로 계속 흡수돼 빠져나가 → 장관 내 C가 낮게 유지 → 대체로 싱크',
                                  '싱크가 깨지면 C ↑ → (Cs − C) ↓ → 속도 ↓'])) +
        box('ex', '예시 (가정 수치)', 'D = 5×10⁻⁶ cm²/s, h = 0.005 cm, S = 1 cm², Cs = 1 mg/mL → dM/dt = (5×10⁻⁶ × 1 / 0.005) × 1 = 1×10⁻³ mg/s ≈ 3.6 mg/h. C가 Cs의 절반이 되면 속도도 절반.'),
        table(['바꾸는 것', '식의 어디', '실제 방법'], [
            ['입자를 작게', '<mark>S ↑</mark>', '미분화, 나노화'],
            ['세게 교반', '<mark>h ↓</mark>', '확산층이 얇아짐'],
            ['용해도 ↑', '<mark>Cs ↑</mark>', '염 형성, 무정형, 고체분산체'],
            ['점도 ↓, 온도 ↑', '<mark>D ↑</mark>', '확산이 빨라짐'],
            ['싱크 유지', '<mark>C ↓</mark>', '용액 교체·흡수'],
        ]) +
        card('연결: BCS Class II', '<p>용해도가 낮고 투과도가 높은 약은 <b>용출이 흡수의 율속 단계</b>예요. 그래서 위 표의 방법(S·Cs ↑)으로 Noyes-Whitney 속도를 키우는 게 제제 설계의 핵심 (PART 5).</p>', 'tint') +
        box('warn', '혼동 주의', '싱크에서 dM/dt = DSCs/h는 "속도 일정"처럼 보이지만, 실제 입자는 녹으면서 S가 줄어서 결국 느려져요.'))

concept(3, '3-3 ★', 'Higuchi ① — 고갈 영역이 "추가 확산 거리"가 된다', 'Higuchi model: depletion zone',
        '고분자 매트릭스 표면부터 약이 빠져나가 <em>약물 고갈 영역</em>(두께 h)이 생기고, 그만큼 확산 거리가 길어져요. 이걸 식에 넣은 게 <em>Higuchi 식</em>.',
        '<div class="fig">' + svg_higuchi() + '평판 매트릭스의 고갈 영역</div>' +
        card('기호 (Summary 3)', table(['기호', '뜻'], [
            ['Q', '단위 면적당 약물의 방출 총량'], ['A', '매트릭스 내 (녹았든 안 녹았든) 약물의 <b>총 농도</b>'],
            ['Cs', '매트릭스 내 약물 <b>포화 농도</b>'], ['h', '확산 거리 (= 고갈 영역 두께)'],
        ], 'l')),
        card('물질수지 — 경계가 dh 움직일 때 나온 양 dQ', formula('dQ = A·dh + ½Cs·h − ½Cs(h + dh) = (A − ½Cs)·dh') +
             table(['항', '의미'], [
                 ['A·dh', '새로 비워진 두께 dh 안에 있던 약 <b>전부</b>'],
                 ['+ ½Cs·h', '이전 고갈 영역(삼각형)에 녹아 있던 양'],
                 ['− ½Cs(h + dh)', '새 고갈 영역(더 큰 삼각형)에 <b>아직 남아 있는</b> 양'],
             ], 'l') + '<p class="mut">고갈 영역 속 농도가 Cs → 0으로 직선이라 남은 양 = 삼각형 넓이 = ½·Cs·h.</p>') +
        box('ok', '한 줄 이해', '방출량 = 새로 비운 양 − 고갈 영역에 남는 증가분 = (A − ½Cs)·dh') +
        box('ex', '고갈 영역 쉽게', '스펀지에서 물이 바깥부터 빠지면 마른 부분이 점점 두꺼워지죠. 안쪽 물은 그 마른 층을 지나야 나오니 점점 느려져요.'))

concept(3, '3-4 ★★', 'Higuchi ② — h(t)와 Q를 유도하기', 'Deriving the Higuchi equation',
        '<em>물질수지</em> dQ = (A − ½Cs)dh 와 <em>Fick 확산</em> dQ/dt = DCs/h 를 같게 놓고 적분 → <em>h ∝ √t</em> → <em>Q ∝ √t</em>.',
        card('유도 6단계', steps([
            '물질수지: dQ = (A − ½Cs)·dh',
            'Fick (싱크·단위면적, 고갈 영역 양끝 Cs → 0): dQ = (D·Cs / h)·dt',
            '같게 놓기: (A − ½Cs)dh = (DCs/h)dt → <b>(2A − Cs)/(2DCs) · h dh = dt</b>',
            '적분: ∫h dh = h²/2 → t = h²(2A − Cs)/(4DCs) + C',
            '초기조건 t = 0 → h = 0 이므로 C = 0',
            '<b>h = √(4DCs·t / (2A − Cs))</b> → 고갈 영역은 √t로 두꺼워짐'])) +
        box('ok', '핵심 두 식', '물질수지(얼마나 비었나) + Fick(얼마나 빨리 나가나) — 이 둘을 엮으면 끝.'),
        card('Q 대입', steps([
            'Q = (A − ½Cs)·h = ((2A − Cs)/2) · √(4DCst/(2A − Cs))',
            '(2A − Cs)/2를 루트 안으로: (2A − Cs)²/4 × 4DCst/(2A − Cs)',
            '약분 → <b>Q = √(D(2A − Cs)Cs·t)</b>',
            't로 미분 (√t → 1/(2√t)) → <b>dQ/dt = ½√(D(2A − Cs)Cs / t)</b>'])) +
        formula('Q = √( D(2A − Cs)Cs t ) &nbsp;·&nbsp; dQ/dt = ½√( D(2A − Cs)Cs / t )', 'Higuchi 식 (최종)') +
        box('ex', '숫자로 감 잡기', 'Q ∝ √t 이므로 1시간에 1 mg 나왔다면 4시간에 2 mg, 9시간에 3 mg. <b>2배 방출하려면 시간은 4배</b>.'))

concept(3, '3-5 ★', 'Higuchi ③ — A ≫ Cs 간단식 · Q ∝ √t · 가정 4개', 'Final form and assumptions',
        'A ≫ Cs면 2A − Cs ≈ 2A → <em>Q = √(2ADCs·t)</em>, <em>dQ/dt = √(ADCs / 2t)</em>. 누적량 ∝ <em>√t</em>(증가), 속도 ∝ <em>1/√t</em>(감소) → 1차 방출.',
        formula('Q = √(2AD·Cs·t) &nbsp;&nbsp; dQ/dt = √(AD·Cs / 2t)', 'A ≫ Cs 일 때 (Summary 3 빈칸: ≫ · 2ADCst · ADCs)') +
        table(['빈칸 (Summary 3)', '정답', '이유'], [
            ['누적 약물량 ∝', '<mark>√t</mark>', 'Q = 상수 × √t'], ['누적량은 점차', '<mark>증가</mark>', '누적량은 절대 줄지 않음'],
            ['순간 방출량 ∝', '<mark>1/√t</mark>', 'dQ/dt = 상수 × 1/√t'], ['방출 속도는', '<mark>감소</mark>', 't ↑ → 1/√t ↓'],
            ['방출 패턴', '<mark>1차</mark>', '속도가 감소하는 방출'],
        ]) + '<div class="fig" style="margin-top:8px">' + svg_rates(330, 130) + '</div>',
        card('Higuchi 식의 가정 4개 (본수업)', table(['가정', '깨지면?'], [
            ['약물 초기 농도 <b>A ≫ Cs</b>', '고체 약이 없어 경계가 안 생김 → 식 성립 X'],
            ['<b>싱크</b> 상태', '바깥 농도 ≠ 0 → 추진력 감소'],
            ['약물이 <b>평평한 면</b>', '구·원통형은 면적이 변해 식이 달라짐'],
            ['고분자 제제의 <b>모양 불변</b> (균질한 Matrix)', '팽윤·침식 → K-P / 구멍 생김 → Higuchi 2'],
        ], 'l')) +
        card('그래프로 확인', '<p><b>Q vs √t</b>를 그리면 직선, 기울기 = √(D(2A − Cs)Cs). Q vs t로 그리면 위로 볼록한 곡선이에요.</p>', 'tint') +
        box('warn', '단골 함정', '"방출 과정에서 확산거리는 감소/일정하다" ✕ → 고갈 영역이 자라서 <b>확산거리는 증가</b>해요. → 문제 05'))

problem(3, 4, 'Higuchi 모델 — Q와 dQ/dt', '예제 · Quiz 1', '3-5 Q ∝ √t',
        '제제가 히구치(Higuchi) 약물방출 모델을 따를 때, 옳은 것은?',
        ['시간 t에서 단위 면적당 방출된 약물의 양(Q)은 시간(t)에 비례한다.', 'Q는 시간의 제곱근(√t)에 반비례한다.', '약물방출 순간속도(dQ/dt)는 시간(t)에 비례한다.',
         'dQ/dt는 시간의 제곱근(√t)에 비례한다.', 'dQ/dt는 시간의 제곱근(√t)에 반비례한다.'],
        ('Higuchi에서 누적량과 속도가 시간과 어떤 관계?', [('키워드', 'Q (누적량) · dQ/dt (속도)'), ('공식', 'Q = √(2ADCst)'), ('구할 것', '맞는 비례 관계')]),
        '⑤ dQ/dt ∝ 1/√t',
        ['Q = √(2ADCs) · √t → <b>Q ∝ √t</b>', '미분하면 √t → 1/(2√t) → <b>dQ/dt ∝ 1/√t</b>', '즉 순간속도는 √t에 반비례 → ⑤'],
        ctab([(False, '①', 'Q ∝ t는 0차의 특징'), (False, '②', 'Q는 √t에 <b>비례</b>'), (False, '③', '속도는 시간이 갈수록 감소'),
              (False, '④', '속도는 √t에 <b>반비례</b>'), (True, '⑤', 'dQ/dt ∝ 1/√t ✓')]) +
        box('ex', '외우는 법', '누적 = √t, 속도 = 그걸 미분한 1/√t.'), one=True, mh=80)

problem(3, 5, '균일한 고분자 매트릭스의 Higuchi 방출', 'Quiz 4 · 국시형', '3-5 가정·확산거리',
        '균일한 고분자 매트릭스 약물전달체의 약물이 Higuchi 확산식에 따라 방출될 때 옳은 것은?',
        ['0차반응으로 방출된다', '1차반응으로 방출된다', '방출과정에서 확산거리는 감소한다', '방출과정에서 확산거리는 일정하게 유지된다', '방출량은 시간의 제곱근에 비례한다.'],
        ('Higuchi 방출의 수학적 특징은?', [('키워드', '균일한 매트릭스 · Higuchi'), ('헷갈릴 보기', '② "1차반응", ③④ 확산거리'), ('구할 것', '옳은 설명')]),
        '⑤ 방출량 ∝ √t',
        ['Higuchi: Q = √(D(2A − Cs)Cs t) → <b>방출량 ∝ √t</b>', '고갈 영역 h = √(4DCst/(2A − Cs)) → 확산거리는 <b>증가</b>', '0차(∝ t)도, 1차반응(지수함수)도 아님'],
        ctab([(False, '①', '0차는 Q ∝ t (OROS·패치)'), (False, '②', '1차반응 = 지수함수. Higuchi는 √t 법칙'),
              (False, '③', '고갈 영역이 자라 확산거리 <b>증가</b>'), (False, '④', '일정하면 0차가 됨'), (True, '⑤', 'Q ∝ √t ✓')]) +
        box('warn', '함정', '강의는 Higuchi를 "1차 방출 동력학"에 넣지만, 보기 ②의 "1차<b>반응</b>"은 다른 말이에요. 국시 정답은 ⑤.'), one=True, mh=80)

problem(3, 6, 'Noyes-Whitney 식을 구성하는 항', 'Quiz 6', '3-1 Noyes-Whitney',
        'Noyes-Whitney 식을 구성하는 항으로 옳지 않은 것은?',
        ['D (확산계수)', 'S (표면적)', 'h (확산층 두께)', 'Cs (약물 포화농도)', 'K (분배계수)'],
        ('dM/dt = (SD/h)(Cs − C)에 없는 기호는?', [('키워드', 'Noyes-Whitney · 옳지 않은 것'), ('떠올릴 식', 'dM/dt = (SD/h)(Cs − C)'), ('구할 것', '식에 없는 항')]),
        '⑤ K (분배계수)',
        ['식을 써 본다: dM/dt = (S·D/h)·(Cs − C)', 'D·S·h·Cs·C는 있음', '확산층이 <b>물층</b>이라 K = 1 → K는 식에 없음'],
        ctab([(False, '①', 'D — 분자에 있음'), (False, '②', 'S — 분자에 있음 (미분화 → S ↑)'), (False, '③', 'h — 분모에 있음 (교반 → h ↓)'),
              (False, '④', 'Cs — 추진력 (Cs − C)'), (True, '⑤', 'K — <b>없음</b> ✓ (막 투과 P = DK/h에 등장)')]) +
        box('ex', '연결', '확산 단원의 얇은 막 식 J = (DK/h)(C₁ − C₂)에서 막이 물층이면 K = 1 → Noyes-Whitney.'), mh=90)

problem(3, 7, '매트릭스 방출의 이론적 모델', 'Quiz 5', '3-3 Higuchi',
        '매트릭스에서 약물이 방출되는 현상에 대한 이론적 모델이 되는 식은?',
        ['Stokes 식', 'Higuchi 식', 'Langmuir 식', 'Scatchard 식', 'Freundlich 식'],
        ('식 이름 ↔ 쓰임 짝짓기', [('키워드', '매트릭스 · 약물 방출'), ('헷갈릴 보기', 'Langmuir·Freundlich(흡착), Scatchard(단백결합)'), ('구할 것', '방출 모델 이름')]),
        '② Higuchi 식',
        ['매트릭스(고분자 중합체) 방출 + 고갈 영역 → <b>Higuchi</b>', '나머지는 다른 단원의 식'],
        ctab([(False, '①', 'Stokes — 입자의 <b>침강 속도</b> (현탁제 안정성)'), (True, '②', 'Higuchi — 매트릭스 방출 Q ∝ √t ✓'),
              (False, '③', 'Langmuir — <b>단분자층 흡착</b> 등온식'), (False, '④', 'Scatchard — <b>단백 결합</b> 분석 (3주차)'),
              (False, '⑤', 'Freundlich — 경험적 <b>흡착</b> 등온식')]) +
        box('ex', '2~7주차 통합 대비', 'Scatchard는 3주차 단백결합, Stokes는 다음 단원(현탁제)에서 다시 나와요.'), mh=90)

problem(3, 8, 'Higuchi 식과 1차 방출 동력학 빈칸', '2024 중간 11번 · 정답률 55%', '3-4 · 3-5',
        '✓ Higuchi 식과 1차 방출 동력학 &nbsp;Q = 단위 면적당 방출 총량, A = 매트릭스 내 약물 총 농도, h = 확산거리, Cs = 포화 농도<br>'
        '• Higuchi 식에서 A ( ) Cs를 가정하면 Q = √( ㉠ ), dQ/dt = √( ㉡ / 2t )<br>'
        '• 누적 약물량은 (√t / 1/√t)에 비례함. 이는 시간이 갈수록 누적 방출량이 점차 (증가/감소)함을 의미함.<br>'
        '• 순간 방출량은 (√t / 1/√t)에 비례함. 방출 속도가 시간이 감에 따라 (증가/감소)함을 의미하는데 이러한 방출 패턴을 (0차/1차) 방출 동력학이라고 함.', None,
        ('A ≫ Cs 간단식을 쓰고, 누적량·속도의 시간 의존성 고르기', [('키워드', 'A ≫ Cs · 누적 vs 순간'), ('헷갈릴 것', '누적은 "증가", 속도가 "감소"'), ('구할 것', '빈칸 8개')]),
        '≫ · 2ADCst · ADCs · √t · 증가 · 1/√t · 감소 · 1차',
        ['A ≫ Cs → 2A − Cs ≈ 2A → Q = √(D·2A·Cs·t) = <b>√(2ADCst)</b>', '미분: dQ/dt = √(2ADCs) · 1/(2√t) = <b>√(ADCs/2t)</b>',
         '누적 Q ∝ √t → 계속 <b>증가</b> / 속도 ∝ 1/√t → <b>감소</b> → <b>1차</b>'],
        table(['빈칸', '정답'], [['A ( ) Cs', '≫'], ['㉠', '2ADCst'], ['㉡', 'ADCs'], ['누적량 ∝ · 변화', '√t · 증가'],
                               ['순간량 ∝ · 변화', '1/√t · 감소'], ['패턴', '1차']]) +
        box('warn', '오답 1순위', '"누적 방출량이 점차 (증가/감소)" → 속도가 줄어드니 감소라고 고르는 실수! 누적량은 <b>증가</b>, 줄어드는 건 <b>증가 속도</b>예요.'), mh=70)

# ============================== PART 4
divider(4, '확장 모델 — Higuchi 2 · Bottari · Korsmeyer-Peppas', '"매트릭스에 구멍이 생기거나, 연고이거나, 부풀면?" — 약물 방출 2 · 본수업(수정반영)',
        [('4-1', 'Higuchi 두번째 식 — 공극률 ε · 곡로율 τ ★★'), ('4-2', 'Bottari 이차식 — 연고·정제, 세 가지 경우 ★'),
         ('4-3', 'Korsmeyer-Peppas — 팽윤 고분자, 지수 n ★'), ('4-4', '모델 고르는 법 — 제형 ↔ 식 ↔ Q 모양'),
         ('문제', '09 – 10 (올해 기출 + Summary 4·5 빈칸)')])

concept(4, '4-1 ★★', 'Higuchi 두번째 식 — 공극률 ε · 곡로율 τ (교수님 수정본)', 'Porous (granular) matrix',
        '약이 빠져나간 자리에 <em>구멍(공극, ε)</em>이 생기고 통로가 <em>꼬불꼬불(곡로, τ)</em>해져요. D → <em>Dε/τ</em>, 2A 옆 Cs → <em>εCs</em>로 바꾼 일반식.',
        formula('Q = √( (Dε/τ)(2A − εCs)Cs t ) &nbsp;&nbsp; ε = ε₀ + A/ρ', 'ε = Porosity 공극률 (0 ≤ ε ≤ 1) · τ = Tortuosity 곡로율 (τ = 1, 2, 3)') +
        card('공극률·곡로율이 용출에 미치는 영향 (수정본 · 노란 강조)', ul([
            '<b>공극률</b>: 공극의 존재는 매트릭스의 <mark>유효확산계수(εD/τ)</mark>와 매트릭스 내 용해 약물의 농도(εCs)를 <mark>증가</mark>시킴.',
            '<b>곡로율</b>: 곡로의 존재는 약물의 확산을 방해 (유효확산계수 εD/τ 감소)하여 방출 속도를 <mark>저하</mark>시킴.']), 'hl') +
        table(['기호', '뜻', 'Q에 미치는 영향'], [
            ['ε ↑', '빈 구멍 부피 분율 ↑', 'εD/τ ↑ → <b>Q ↑</b>'], ['τ ↑', '실제 경로 / 직선 거리 ↑', 'εD/τ ↓ → <b>Q ↓</b>'],
            ['ε₀', '처음부터 있던 공극', '—'], ['A/ρ', '약이 녹아 나가며 새로 생기는 공극', '시간 따라 ε ↑'],
        ]),
        card('왜 "두번째 식이 더 일반적"인가 (2024 중간 22번 포인트)', '<p>ε = 1, τ = 1을 넣으면 εD/τ = D, 2A − εCs = 2A − Cs → <mark>첫번째 Higuchi 식과 똑같아져요</mark>. 즉 첫번째 식은 두번째 식의 <b>특수한 경우</b>(구멍·곡로 없는 균질 Matrix)이고, 두번째 식이 <b>일반적인</b> 식이에요.</p>', 'tint') +
        card('숫자로 (가정 수치)', '<p>τ = 3 고정: ε = 0.3 → εD/τ = 0.10D, ε = 0.6 → 0.20D (공극 2배 → 유효 D 2배 → Q 약 √2 ≈ 1.4배).<br>ε = 0.3에서 τ = 3 → 1.5로 줄면 0.20D → 방출 ↑.</p>') +
        table(['', '첫번째 식', '두번째 식'], [['매트릭스', '균질한 Matrix', '다공성 (과립) Matrix'], ['D 자리', 'D', 'Dε/τ'],
                                            ['2A 옆', 'Cs', 'εCs'], ['Q ∝', '√t', '√t (그대로 1차)']]) +
        box('ok', '암기', '"구멍(ε)은 길을 열고, 꼬불길(τ)은 길을 막는다." 방출을 <b>줄이는</b> 건 τ ↑ → 문제 09'))

concept(4, '4-2 ★', 'Bottari 이차식 — 연고·정제, 그리고 세 가지 경우 (수정본 추가)', "Bottari's quadratic model",
        '약물이 <em>연고(ointment)나 정제(tablet)</em>에서 큰 용해성을 가질 때 = <em>균질한 고체·반고체 기제</em>. 기제–경계면 <em>저항 R</em>까지 넣으면 2차식이 돼요.',
        formula('Q² + 2DRA*·Q − 2DA*·Cs·t = 0', 'A* = A − ½(Cs + Cv) · R = 기제와 경계면 사이 저항 · Cs = 기제 내부 약물 농도 · Cv = 경계면 약물 농도') +
        card('세 가지 경우', steps([
            '<b>R 무시</b> (Q² ≫ 2DRA*Q): Q² − 2DA*Cst = 0 → <mark>Q = √(2DA*Cs·t)</mark>',
            '+ <b>Cs ≫ Cv</b> (기제 내부 농도가 무시할 수 없을 만큼 높음): A* = A − Cs/2 → Q = √(2D(A − Cs/2)Cst) = <mark>√(D(2A − Cs)Cst)</mark> = Higuchi 식!',
            '<b>R을 무시 못 함</b>: 근의 공식 → Q = [−2DRA* + √((2DRA*)² + 8DA*Cst)] / 2'])) +
        box('ok', '결론', '방출된 약물의 양이 <b>√t에 비례</b> → <b>1차 방출</b>을 설명할 수 있음.'),
        table(['', 'Higuchi', 'Bottari'], [
            ['제형', '평판 고분자 매트릭스', '<b>연고 · 정제</b> (균질 기제)'], ['경계면 저항', '없음 (완전 싱크)', 'R 포함'],
            ['A 자리', 'A − ½Cs', 'A* = A − ½(Cs + Cv)'], ['Higuchi가 되는 조건', '—', '<b>Q² ≫ 2DRA*Q</b> (+ Cs ≫ Cv)'],
        ]) +
        card('근의 공식 확인', '<p>aQ² + bQ + c = 0 (a = 1, b = 2DRA*, c = −2DA*Cst) → Q = (−b + √(b² − 4ac))/2. Q > 0이라 + 근만 써요.</p>') +
        card('R이 클 때 모양 (보충)', '<p>초기(t 작음): Q ≈ Cs·t/R → t에 비례 (<b>경계면 저항이 율속</b>) / 후기(t 큼): Q ∝ √t (<b>기제 안 확산이 율속</b>).</p>', 'tint') +
        box('warn', 'Summary 4 빈칸', '(팽창하는 고분자 / <b>연고나 정제</b>) · (<b>Q² ≫ 2DRA*Q</b> / Q² ≪ 2DRA*Q) · (<b>√t</b> / t) · (0차 / <b>1차</b>)'))

concept(4, '4-3 ★', 'Korsmeyer-Peppas 모델 — 부푸는 고분자는 지수 n으로', 'Korsmeyer–Peppas power law',
        '약물 기제가 방출되며 <em>팽윤</em>하는 고분자 제제: <em>f = Mt/M∞ = ktⁿ</em>. 지수 <em>n</em>으로 방출 기전을 판별해요.',
        formula('f<sub>t</sub> = M<sub>t</sub> / M<sub>∞</sub> = k·tⁿ', 'f 방출 분율 · Mt t시간까지 방출량 · M∞ 총량 · k 제제 구조 상수') +
        table(['n (원통형 기준)', '기전', 'Q 모양'], [
            ['<mark>n = 0.45</mark>', '순수 확산 (<b>Fick 법칙</b> 적용 가능)', '≈ √t (Higuchi형)'],
            ['0.45 &lt; n &lt; 0.89', '<b>변칙적 확산</b> — 확산 + 고분자 변형', '√t와 t 사이'],
            ['0.89 &lt; n', '고분자 <b>침식</b>이 있는 확산 (Case II)', '≈ t (0차에 가까움)'],
        ]) +
        card('변형식', ul(['지연시간 L: f<sub>t−L</sub> = k(t − L)ⁿ — 처음 L 동안은 방출 0',
                          '초기 burst b: f = ktⁿ + b — 표면 약이 한꺼번에 나옴'])) +
        box('warn', '수정 포인트', '슬라이드 12의 "0.89 > n"은 오타 → 슬라이드 13에서 <b>0.89 &lt; n</b>으로 수정됐어요.'),
        '<div class="fig">' + svg_kp() + 'log f vs log t — 기울기가 n</div>' +
        card('n 구하는 법', '<p>양변에 log: <b>log f = log k + n·log t</b> → log f vs log t 그래프의 <b>기울기 = n</b>. 보통 방출 초기 60% 이하 구간으로 맞춰요.</p>') +
        box('ex', '예시 (가정 수치)', 'f = 0.2 (1 h) → 0.4 (4 h): n = log2/log4 = 0.5 → 거의 Fick. f = 0.2 → 0.6: n = log3/log4 = 0.79 → 변칙적 확산.') +
        box('warn', 'Summary 5 빈칸', '(<b>팽창하는 고분자</b> / 연고나 정제) · Fick = (<b>n = 0.45</b>) · 팽창·침식 포함 = (<b>n > 0.45</b>)'))

concept(4, '4-4', '모델 고르는 법 — 제형 ↔ 식 ↔ Q 모양', 'Choosing a release model',
        '문제가 <em>제형</em>을 말해주면 모델이 정해지고, 모델이 정해지면 <em>Q 모양</em>이 정해져요. 이 표 하나로 PART 2~5 연결!',
        table(['제형', '모델', '식', 'Q 모양'], [
            ['OROS · 패치 · 캡슐(포화)', '0차', 'Q = Q₀ + K₀t · Q = PCpt', '<b>∝ t</b>'],
            ['고체 입자 용출', 'Noyes-Whitney', 'dM/dt = (SD/h)(Cs − C)', '포화로 지수 접근'],
            ['평판(균질) 매트릭스', 'Higuchi 1', 'Q = √(D(2A − Cs)Cst)', '<b>∝ √t</b>'],
            ['다공성(과립) 매트릭스', 'Higuchi 2', 'Q = √((Dε/τ)(2A − εCs)Cst)', '∝ √t'],
            ['연고 · 정제 (균질 기제)', 'Bottari', 'Q² + 2DRA*Q − 2DA*Cst = 0', '∝ √t (R 무시)'],
            ['팽윤 고분자', 'Korsmeyer-Peppas', 'f = ktⁿ', '<b>∝ tⁿ</b>'],
        ], 'l'),
        card('키워드 → 모델 즉답', ul(['"과립상·다공성 매트릭스", "공극률·곡로율" → <b>Higuchi 2</b>', '"연고·정제", "경계면 저항 R" → <b>Bottari</b>',
                                       '"팽윤·팽창하는 고분자", "n값" → <b>Korsmeyer-Peppas</b>', '"고체 제형의 용출 속도", "정적 확산층" → <b>Noyes-Whitney</b>',
                                       '"반투막·삼투", "실리콘 캡슐" → <b>0차</b>']), 'tint') +
        box('warn', '자주 바뀌는 짝', 'Bottari ↔ K-P의 적용 제형을 맞바꾼 보기가 Summary 4·5 빈칸에 그대로 나와요: Bottari = <b>연고·정제</b>, K-P = <b>팽창하는 고분자</b>.') +
        box('ok', '공통점', 'Higuchi 1·2, Bottari 모두 결론은 Q ∝ √t → "1차 방출"을 설명.'))

problem(4, 9, '과립상 매트릭스의 방출을 감소시키는 것', '올해 기출 12번', '4-1 Higuchi 2',
        '과립상 매트릭스에 균일하게 분산되어 있는 약물의 방출을 감소시키는 것은? (단, 약물 방출 기전은 Higuchi 모델을 따른다.)',
        ['곡로율 증가', '공극률 증가', '방출시간 증가', '확산계수 증가', '매트릭스에 대한 약물의 용해도 증가'],
        ('구멍 난 매트릭스(Higuchi 2)에서 Q를 줄이는 변화는?', [('키워드', '과립상 = 다공성 → Higuchi 2'), ('공식', 'Q = √((Dε/τ)(2A − εCs)Cst)'), ('구할 것', 'Q ↓ 시키는 것')]),
        '① 곡로율 증가',
        ['과립상(다공성) 매트릭스 → <b>Higuchi 두번째 식</b>', '분모에 있는 건 <b>τ(곡로율)</b> 하나뿐', 'τ ↑ → εD/τ ↓ → Q ↓'],
        ctab([(True, '①', 'τ ↑ → 유효확산계수 ↓ → Q ↓ ✓'), (False, '②', 'ε ↑ → εD/τ ↑ → Q ↑'), (False, '③', 'Q ∝ √t → 누적량 ↑ (속도만 ↓)'),
              (False, '④', 'D ↑ → Q ↑'), (False, '⑤', 'Cs ↑ → Q ↑')]) +
        box('warn', '함정', '③ "방출시간 증가"는 <b>속도</b>(1/√t)는 줄이지만 <b>방출량</b>은 늘려요.'), one=True, mh=80)

problem(4, 10, 'Bottari · Korsmeyer-Peppas 빈칸', 'Summary 4 · 5', '4-2 · 4-3',
        '• Bottari의 이차식 모델: 약물이 (팽창하는 고분자 / 연고나 정제)에서 방출될 때 적용 가능하다. (Q² ≫ 2DRA*Q / Q² ≪ 2DRA*Q)일 경우 Higuchi식과 동일하게 된다. 약물 방출량은 (√t / t)에 비례하므로 (0차/1차) 방출을 설명한다.<br>'
        '• Korsmeyer-Peppas 모델: 약물이 (팽창하는 고분자 / 연고나 정제)에서 방출될 때 적용 가능하다. (n = 0.45 / n > 0.45)일 때 Fick’s law가 적용 가능한 단순 확산, (n = 0.45 / n > 0.45)일 때 고분자의 팽창이나 침식을 포함하여 기술할 수 있다.', None,
        ('두 모델의 적용 제형과 판별 조건 고르기', [('키워드', '연고·정제 vs 팽창 고분자'), ('헷갈릴 것', '두 모델의 제형을 맞바꾼 보기'), ('구할 것', '선택형 괄호 7개')]),
        '연고나 정제 · Q² ≫ 2DRA*Q · √t · 1차 / 팽창하는 고분자 · n = 0.45 · n > 0.45',
        ['Bottari = 균질 고체·반고체 기제 = <b>연고나 정제</b>', '저항 R 무시 = 2DRA*Q 항이 작음 = <b>Q² ≫ 2DRA*Q</b> → Q = √(2DA*Cst) ∝ <b>√t</b> → <b>1차</b>',
         'K-P = <b>팽창하는 고분자</b>, Fick = <b>n = 0.45</b>, 팽윤·침식 = <b>n > 0.45</b>'],
        table(['모델', '적용 제형', '조건 → 결과'], [['Bottari', '연고나 정제', 'Q² ≫ 2DRA*Q → Higuchi, √t, 1차'],
                                               ['Korsmeyer-Peppas', '팽창하는 고분자', 'n = 0.45 Fick / n > 0.45 팽윤·침식']]) +
        box('ex', 'Summary 4 앞부분', '공극률 → (εD/τ, εCs) <b>증가</b>, 곡로율 → 방출 속도 <b>저하</b> (수정본).'), mh=70)

# ============================== PART 5
divider(5, '캡슐제제 방출 · 생물약제학적 분류체계(BCS)', '"막과 물층 중 누가 속도를 정하나? 어떤 약이 잘 흡수되나?" — 약물 방출 2 · 본수업',
        [('5-1', '캡슐 방출식 — 저항의 합, Q = PCpt ★★'), ('5-2', '막 제어 vs 정적 확산층 제어 ★'),
         ('5-3', 'BCS 4칸 — 용해도 × 투과도 ★★'), ('문제', '11 – 12 (예제 + Summary 6)'), ('정리', '한 장 정리 (공식·함정)')])

concept(5, '5-1 ★★', '캡슐제제 방출식 — 실리콘막 + 정적 확산층 = 다층 확산', 'Silicone capsule: series resistances',
        '실리콘 캡슐 = <em>실리콘막(hm)</em> + 바깥 <em>정적 확산층(ha)</em>의 다층 확산. 저항을 더하고 뒤집으면 P, 그리고 <em>Q = P·Cp·t</em> (0차).',
        '<div class="fig">' + svg_capsule() + '캡슐 안 → 막 → 물층 → 싱크 농도 프로파일</div>' +
        card('유도 4단계', steps([
            '층별 저항 R = h/(DK) — K는 캡슐 안 Cp 기준. 막: K = 1 → <b>Rm = hm/Dm</b>. 물층: K = Kr → <b>Ra = ha/(DaKr)</b>',
            '직렬 합: R = hm/Dm + ha/DaKr = (hmDaKr + haDm) / (DmDaKr)',
            '뒤집기: <b>P = 1/R = DmDaKr / (hmDaKr + haDm)</b>',
            '싱크라 J = dQ/dt = P·Cp (상수) → 적분 <b>Q = P·Cp·t</b>'])),
        formula('Q = [ D<sub>m</sub>D<sub>a</sub>K<sub>r</sub> / (h<sub>m</sub>D<sub>a</sub>K<sub>r</sub> + h<sub>a</sub>D<sub>m</sub>) ] · C<sub>p</sub> · t', 'Q ∝ t → 저장소형 캡슐 방출은 0차') +
        table(['기호', '뜻'], [
            ['Cp', '캡슐 내부 약물 농도 (고체가 있어 포화 유지)'], ['Cm', '막과 수층 경계면에서 막쪽 농도'],
            ['Cs', '막과 수층 경계면에서 수층 쪽 농도'], ['Cb', '수층과 싱크 경계면 농도 (≈ 0)'],
            ['hm · ha', '캡슐 막 두께 · 정적 확산층 두께'], ['Kr = Cs/Cp', '<mark>시스템 전체에서의 유효분배계수</mark>'],
        ], 'l') +
        box('ex', '확산 단원과 연결', '5~6주차 다층 확산(R = ΣR, P = 1/R)과 똑같은 구조. 차이는 물층이 바깥 <b>한 겹</b>뿐이라 2ha가 아니라 ha.') +
        box('warn', '함정', 'Kr = Cp/Cs ✕ → <b>Kr = Cs/Cp</b>. Summary 5 빈칸: 실리콘막과 (<b>정적 확산층</b>)으로 이루어진 다층 확산.'))

concept(5, '5-2 ★', '막 제어 vs 정적 확산층 제어 — 저항이 큰 쪽이 속도를 정한다', 'Membrane vs diffusion-layer control',
        '분모 hmDaKr + haDm에서 <em>큰 항만 남기면</em> 끝. 막 저항이 크면 <em>막 제어</em>, 물층 저항이 크면 <em>정적 확산층 제어</em>.',
        table(['', '막 제어', '정적 확산층 제어'], [
            ['조건', 'Rm ≫ Ra<br><b>hmDaKr ≫ haDm</b>', 'Rm ≪ Ra<br><b>hmDaKr ≪ haDm</b>'],
            ['분모에서 남는 항', 'hmDaKr', 'haDm'],
            ['Q', '<mark>(Dm/hm)·Cp·t</mark>', '(DaKr/ha)·Cp·t = <mark>(Da/ha)·Cs·t</mark>'],
            ['속도를 정하는 것', '막 두께 · 막 확산계수', '물층 두께(교반) · 물 확산계수'],
            ['무관한 것', '물층 (ha, Da)', '막 (hm, Dm)'],
        ]) +
        card('마지막 변환', '<p>Kr·Cp = (Cs/Cp)·Cp = <b>Cs</b> → (DaKr/ha)Cp = (Da/ha)Cs</p>') +
        box('warn', 'Summary 6 빈칸', '(<b>막제어시</b> / 정적 확산층 제어시) hmDaKr ≫ haDm · (막제어시 / <b>정적 확산층 제어시</b>) hmDaKr ≪ haDm'),
        card('실험으로 방출 속도 구하기', ul(['막 제어: Q vs t 직선의 기울기 = <b>(Dm/hm)Cp</b>', '정적 확산층 제어: Q vs t 직선의 기울기 = <b>(Da/ha)Cs</b>',
                                           '둘 다 Q ∝ t → <b>0차</b>, 직선 기울기가 곧 방출 속도'])) +
        box('ex', '예시 (가정 수치)', '막 제어, Dm = 1×10⁻⁷ cm²/s, hm = 0.02 cm, Cp = 1 mg/cm³ → dQ/dt = 5×10⁻⁶ mg/(cm²·s) ≈ 0.43 mg/(cm²·day). 3 cm² 캡슐이면 하루 약 1.3 mg 일정 방출.') +
        card('직관', '<p>파이프 두 개를 이어 붙였을 때 <b>더 좁은 쪽</b>이 물 흐름을 정하죠. 저항이 압도적으로 큰 층 하나가 전체 속도를 결정해요 (율속 단계).</p>', 'tint') +
        box('ok', '확산 단원 짝', '6주차 경피 패치: 막 제어 Pm·C₁ / 피부 제어 — 같은 논리.'))

concept(5, '5-3 ★★', '경구 약물의 생물약제학적 분류체계 (BCS)', 'Biopharmaceutics Classification System',
        '경구 약물을 <em>용해도(Solubility)</em>와 <em>투과도(Permeability)</em>로 4칸 분류. 녹아야(용출) 흡수되고, 녹은 뒤엔 장관막을 빨리 지나야 해요.',
        '<div class="fig">' + svg_bcs() + 'BCS 4칸 (세로 용해도 · 가로 투과도)</div>' +
        table(['Class', '용해도', '투과도', '흡수 율속 · 전략 (보충)'], [
            ['I', '높음', '높음', '<b>90% 이상 흡수</b> · 문제 없음'],
            ['II', '<mark>낮음</mark>', '높음', '<b>약물 용출 속도</b> · 미분화·염·고체분산체'],
            ['III', '높음', '<mark>낮음</mark>', '막 투과 · 투과 촉진제·프로드럭'],
            ['IV', '낮음', '낮음', '둘 다 · <b>상용화 어려움</b>'],
        ]),
        card('강의 빈칸 (Summary 6)', ul([
            'class I: 용해도와 투과도가 모두 (<b>높아</b>) 90% 이상 흡수',
            'class II: 투과도는 (<b>높</b>)지만 용해도가 (<b>낮</b>)아 흡수율 ↓ → (<b>약물 용출 속도</b>)가 흡수 속도를 제어',
            'class III: 용해도는 (<b>높</b>)지만 투과도가 (<b>낮</b>)아 흡수율 ↓', 'class IV: 모두 (<b>낮아</b>) 상용화 어려움',
            '분자량이 클수록 투과도 (<b>낮아</b>)짐 · 친수성일수록 용해도 (<b>증가</b>), 투과도 (<b>감소</b>)'])) +
        card('친수성의 딜레마', '<p>친수성 ↑ → 물에 잘 녹아 용해도 ↑, 하지만 지질막 분배계수 K ↓ → 투과도 ↓ (5주차 pH 분배 가설과 같은 원리). 그래서 적당한 지용성이 필요해요.</p>', 'tint') +
        box('ex', '예시 약물 (보충)', 'I 메토프롤롤 · II 이부프로펜·카르바마제핀 · III 아테놀롤·메트포르민 · IV 푸로세미드') +
        box('warn', '2024 중간 25번 (정답률 58%)', '4칸 위치를 그림으로 물어요. 세로축 = 용해도, 가로축 = 투과도 → 오른쪽 위 I, 왼쪽 위 III, 오른쪽 아래 II, 왼쪽 아래 IV.'))

problem(5, 11, '저용해·고투과 약물의 속도결정단계', '예제 · Quiz 3', '5-3 BCS',
        '용해도가 낮고 막투과도가 높은 약물을 함유한 정제의 경구 투여 시 위장관 흡수 과정에서의 속도결정단계는?',
        ['분배', '분해', '삼투', '용출', '응결'],
        ('BCS Class II 약은 흡수 과정에서 어디가 제일 느린가?', [('키워드', '용해도 ↓ · 투과도 ↑ = Class II'), ('흡수 순서', '붕해 → 분산 → 용출 → 막 투과'), ('구할 것', '가장 느린 단계')]),
        '④ 용출',
        ['저용해도 + 고투과도 → <b>BCS Class II</b>', '막 투과는 빠른데 녹는 게 느림', '가장 느린 단계 = <b>용출</b> = 속도결정단계'],
        ctab([(False, '①', '분배 — 막 투과 단계, 투과도가 높으니 빠름 (Class III라면 후보)'), (False, '②', '분해 — 화학적 안정성, 흡수 단계 아님'),
              (False, '③', '삼투 — 물의 이동 (OROS 구동력)'), (True, '④', '용출 — 녹는 속도가 율속 ✓'), (False, '⑤', '응결 — 입자가 엉기는 것')]) +
        box('ex', '변형', '"용해도 높고 투과도 낮은 약(Class III)의 율속?" → <b>막 투과</b>. Class II는 Noyes-Whitney의 S·Cs를 키우는 게 해법.'), mh=95)

problem(5, 12, '캡슐 막 제어 · BCS 빈칸', 'Summary 6', '5-2 · 5-3',
        '• (막제어시 / 정적 확산층 제어시), hmDaKr ≫ haDm : Q = (Dm/hm)Cpt<br>• (막제어시 / 정적 확산층 제어시), hmDaKr ≪ haDm : Q = (Da/ha)Cst<br>'
        '• BCS class II : 투과도는 (낮/높)지만 용해도가 (높/낮)아 흡수율이 떨어짐. 이 경우 (약물 용출 속도 / 투과도)가 흡수 속도를 제어함.<br>'
        '• 분자량이 클수록 투과도가 (낮아/높아)짐. 친수성일수록 용해도는 (감소/증가)하지만 투과도는 (감소/증가)함.', None,
        ('분모의 큰 항 고르기 + BCS 성질 고르기', [('키워드', '≫ / ≪ · Class II · 분자량 · 친수성'), ('요령', '저항 큰 쪽이 제어'), ('구할 것', '선택형 괄호 7개')]),
        '막제어시 · 정적 확산층 제어시 · 높 · 낮 · 약물 용출 속도 · 낮아 · 증가 · 감소',
        ['hmDaKr ≫ haDm → 막 항이 큼 → <b>막제어</b>, ≪ → <b>정적 확산층 제어</b>', 'Class II = 투과도 <b>높</b>, 용해도 <b>낮</b> → <b>용출 속도</b>가 율속',
         '분자량 ↑ → 투과 <b>낮아</b>짐 · 친수성 ↑ → 용해 <b>증가</b>, 투과 <b>감소</b>'],
        table(['괄호', '정답', '이유'], [['≫ 일 때', '막제어시', '분모에서 hmDaKr만 남음'], ['≪ 일 때', '정적 확산층 제어시', 'haDm만 남음'],
                                       ['Class II', '높 · 낮 · 용출 속도', '녹는 게 느림'], ['분자량 ↑', '투과 낮아짐', '큰 분자는 막 통과 어려움'],
                                       ['친수성 ↑', '용해 증가 · 투과 감소', '지질막 K ↓']]) +
        box('ex', 'BCS 그림 빈칸', '좌상 Class III (High Solubility · Low Permeability), 우하 Class II (Low Solubility · High Permeability), 세로축 Solubility, 가로축 Permeability.'), mh=70)

# ============================== 한 장 정리
cs = [
    ('용어', '붕해 → 분산 → 용출', '전 과정 = 약물 방출 · 약품 = 완제품'),
    ('방출 제형', 'IR · DR · ER · CR', '장용제 = 지연(DR) · 서방 = 투여 횟수 ↓'),
    ('0차', 'Q = Q₀ + K₀t', '속도 일정 · 농도 무관 · 붕해 안 됨'),
    ('OROS', '구동력 = 삼투압(압력)', 'Δπ ↑ → 방출 ↑ · 구멍 크기 무관'),
    ('구동력', '전기 → 전위 · 열 → 온도', '확산·증발 → 농도(증기압)'),
    ('Noyes-Whitney', 'dM/dt = (SD/h)(Cs − C)', 'K 없음 · C ↑ → 속도 ↓ · 고체 제형'),
    ('싱크', 'dM/dt = DSCs/h', 'C ≈ 0 · 체내 대체로 싱크'),
    ('Higuchi', 'Q = √(D(2A − Cs)Cst)', 'A ≫ Cs → Q = √(2ADCst)'),
    ('Higuchi 결과', 'Q ∝ √t · dQ/dt ∝ 1/√t', '누적 증가 · 속도 감소 · 1차 · h ↑'),
    ('Higuchi 가정', 'A ≫ Cs · 싱크 · 평면', '모양 불변 (균질한 Matrix)'),
    ('Higuchi 2', 'D → Dε/τ, Cs → εCs', 'ε ↑ 방출 ↑ · τ ↑ 방출 ↓ · 일반식'),
    ('Bottari', 'Q² + 2DRA*Q − 2DA*Cst = 0', '연고·정제 · Q² ≫ 2DRA*Q → Higuchi'),
    ('Korsmeyer-Peppas', 'f = Mt/M∞ = ktⁿ', '팽윤 고분자 · 0.45 Fick · >0.89 침식'),
    ('캡슐', 'Q = [DmDaKr/(hmDaKr + haDm)]Cpt', '0차 · Kr = Cs/Cp (유효분배계수)'),
    ('막 / 확산층 제어', '(Dm/hm)Cpt / (Da/ha)Cst', '≫ 막 제어 · ≪ 확산층 제어'),
    ('BCS', 'I ↑↑ · II 용해 ↓ · III 투과 ↓', 'II = 용출 율속 · IV 상용화 어려움'),
    ('BCS 성질', '분자량 ↑ → 투과 ↓', '친수성 ↑ → 용해 ↑ 투과 ↓'),
    ('그래프 판별', 'Q–t 직선 0차 · Q–√t 직선 Higuchi', 'log f–log t 기울기 = n'),
    ('정답 모음 ①', '구동력 ① · OROS ④ · Higuchi ⑤', 'Noyes-Whitney K ⑤ · 매트릭스 ②'),
    ('정답 모음 ②', '과립 매트릭스 ① 곡로율', 'Class II 율속 ④ 용출'),
]
cells = ''.join(f'<div><div class="h">{a}</div><div class="f">{b}</div><div class="d">{c}</div></div>' for a, b, c in cs)
pages.append(f'''<section class="page p5">
<div class="hd"><span class="tag">한 장 정리</span><h1>시험 직전에 보는 방출 공식 &amp; 함정</h1><span class="en">Cheat sheet</span></div>
<div class="cs">{cells}</div>
<div class="traps">
<div><b>함정 ①</b> 누적 방출량은 항상 <b>증가</b>, 줄어드는 건 속도(dQ/dt) — 문제 05·08</div>
<div><b>함정 ②</b> "1차반응"(지수) ≠ Higuchi(√t). 확산거리는 <b>증가</b> — 문제 05</div>
<div><b>함정 ③</b> Bottari = 연고·정제, K-P = 팽창 고분자 (맞바꾼 보기) — 문제 10</div>
<div><b>함정 ④</b> 방출시간 ↑는 방출량 ↑. 방출 ↓는 <b>곡로율 ↑</b>뿐 — 문제 09</div>
</div>{foot()}</section>''')

total = len(pages)
html = ''.join(p.replace('{PN}', f'{i} / {total}') for i, p in enumerate(pages, 1))
css = open(os.path.join(HERE, 'style.css'), encoding='utf-8').read()
open(os.path.join(HERE, 'out.html'), 'w', encoding='utf-8').write(
    f'<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>7주차 붕해·용출·약물방출 최종 요약</title><style>{css}</style></head><body>{html}</body></html>')
print(total, 'pages')
