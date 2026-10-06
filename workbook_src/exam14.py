# -*- coding: utf-8 -*-
"""14장 시험대비 요약노트.  python3 exam14.py → exam_ch14.pdf"""
import os, sys
os.environ['CH'] = '14'
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from helpers import *
import examlib
import ch14
from ch14 import fbp_split, atp_ledger, lactate_cori, GLY
from exam13 import hill

CH = 14
CH_TITLE = '해당과정 · 당신생 · 오탄당 인산 경로'
FOOT = 'Lehninger 8e · Ch.14 해당과정·당신생·PPP — 시험대비 요약노트'

_items = [i for i in ch14.ALL_ITEMS if i['level'] < 3]
WB = {i['id']: 6 + k for k, i in enumerate(_items)}
link = examlib.make_link(WB, CH)
page = examlib.make_page(link)


# ------------------------------------------------------------------ drawings
def gly_map():
    """10 steps: prep (left) / payoff (right)"""
    W, H = 600, 330
    b = arrowdef('gm', C['gray'])
    prep = [('포도당', ''), ('G6P', '① HK  −ATP'), ('F6P', '② PGI'), ('F1,6BP', '③ PFK-1  −ATP'), ('DHAP + G3P', '④ 알돌라아제'), ('G3P × 2', '⑤ TPI')]
    pay = [('G3P (×2)', ''), ('1,3-BPG', '⑥ GAPDH  +NADH'), ('3PG', '⑦ PGK  +ATP'), ('2PG', '⑧ PGM'), ('PEP', '⑨ 에놀레이스  −H₂O'), ('피루브산', '⑩ PK  +ATP')]
    for col, (items, x, title, tc) in enumerate([(prep, 20, '준비 단계 (투자)', C['red']), (pay, 320, '수익 단계 (×2, 회수)', C['green'])]):
        b += T(x + 120, 16, title, 12, tc, weight=900)
        for i, (n, lab) in enumerate(items):
            y = 26 + i * 50
            hot = lab.startswith(('①', '③', '⑩'))
            b += f'<rect x="{x}" y="{y}" width="120" height="28" rx="7" fill="white" stroke="{C["navy"]}" stroke-width="1.6"/>' + T(x + 60, y + 19, n, 11.5, C['navy'], weight=700)
            if i < len(items) - 1:
                b += f'<line x1="{x+60}" y1="{y+29}" x2="{x+60}" y2="{y+47}" stroke="{C["gray"]}" stroke-width="1.6" marker-end="url(#gm)"/>'
            if lab:
                col_ = C['red'] if hot else C['ink']
                b += T(x + 70, y - 6, lab, 10.5, col_, 'start', 900 if hot else 400)
    b += f'<path d="M142,290 C220,320 260,320 318,40" fill="none" stroke="{C["orange"]}" stroke-width="1.6" stroke-dasharray="5 4" marker-end="url(#gm)"/>'
    b += T(300, 322, '빨간 번호 = 비가역 3단계 (조절·당신생 우회 지점)', 10.5, C['red'], weight=700)
    return svg(W, H, b)


def three_stage():
    return flow(['포도당 (C6)', '피루브산 ×2 (C3)', '아세틸-CoA', 'CO₂ + H₂O|(O₂ 사용)'],
                arrow_labels=['① 해당과정 (세포질)', '② PDH (미토콘드리아)', '③ TCA·산화적 인산화'],
                colors=[C['navy'], C['orange'], C['blue'], C['green']], box_h=44, width=600)


def pyruvate_fates():
    W, H = 560, 210
    b = arrowdef('pf', C['gray'])
    b += f'<rect x="210" y="10" width="140" height="34" rx="9" fill="#fff7ed" stroke="{C["orange"]}" stroke-width="2"/>' + T(280, 32, '포도당 → 2 피루브산', 11.5, C['orange'], weight=900)
    outs = [(70, '유산소', '아세틸-CoA → TCA', 'CO₂ + H₂O (대부분 ATP)', C['blue']), (280, '무산소 (근육·적혈구)', '젖산 발효 (LDH)', '2 젖산 + NAD⁺ 재생', C['red']),
            (490, '무산소 (효모)', '에탄올 발효', '2 에탄올 + 2CO₂', C['purple'])]
    for x, t1, t2, t3, col in outs:
        b += f'<line x1="280" y1="46" x2="{x}" y2="88" stroke="{C["gray"]}" stroke-width="1.6" marker-end="url(#pf)"/>'
        b += f'<rect x="{x-90}" y="92" width="180" height="96" rx="10" fill="white" stroke="{col}" stroke-width="2"/>'
        b += T(x, 114, t1, 11.5, col, weight=900) + T(x, 138, t2, 11, C['ink'], weight=700) + T(x, 160, t3, 10.5, C['gray'])
    return svg(W, H, b)


def gng_bypass():
    W, H = 600, 300
    b = arrowdef('gb1', C['red']) + arrowdef('gb2', C['blue'])
    nodes = [('포도당', 20), ('G6P', 70), ('F6P', 120), ('F1,6BP', 170), ('(7개 가역 단계 공유)', 215), ('PEP', 250), ('피루브산', 290)]
    for n, y in nodes:
        b += f'<rect x="230" y="{y-16}" width="140" height="26" rx="7" fill="white" stroke="{C["navy"]}" stroke-width="1.5"/>' + T(300, y + 2, n, 11, C['navy'], weight=700)
    pairs = [(20, 70, '① 헥소키나아제 (ATP)', 'G6Pase (소포체, 간·신장)'), (120, 170, '③ PFK-1 (ATP)', 'FBPase-1'), (250, 290, '⑩ 피루브산 키나아제', 'PC + PEPCK (ATP·GTP)')]
    for top, bot, gly, gng in pairs:
        b += f'<path d="M228,{top} C190,{top+5} 190,{bot-5} 228,{bot-8}" fill="none" stroke="{C["red"]}" stroke-width="2.2" marker-end="url(#gb1)"/>'
        b += T(182, (top + bot) / 2 + 4, gly, 10.5, C['red'], 'end', 700)
        b += f'<path d="M372,{bot-8} C410,{bot-5} 410,{top+5} 372,{top}" fill="none" stroke="{C["blue"]}" stroke-width="2.2" marker-end="url(#gb2)"/>'
        b += T(418, (top + bot) / 2 + 4, gng, 10.5, C['blue'], 'start', 700)
    b += T(110, 14, '해당과정 ↓ (빨강)', 11, C['red'], weight=900) + T(490, 14, '당신생 ↑ (파랑)', 11, C['blue'], weight=900)
    return svg(W, H + 8, b)


def ppp_svg():
    W, H = 600, 220
    b = arrowdef('pp', C['gray'])
    b += f'<rect x="10" y="80" width="90" height="34" rx="8" fill="white" stroke="{C["navy"]}" stroke-width="2"/>' + T(55, 102, 'G6P', 12, C['navy'], weight=900)
    b += f'<rect x="170" y="80" width="150" height="34" rx="8" fill="#fff7ed" stroke="{C["orange"]}" stroke-width="2"/>' + T(245, 102, '리불로스 5-인산', 11.5, C['orange'], weight=900)
    b += f'<line x1="102" y1="97" x2="166" y2="97" stroke="{C["orange"]}" stroke-width="2.2" marker-end="url(#pp)"/>'
    b += T(134, 74, '산화 단계', 10.5, C['orange'], weight=900) + T(134, 132, '2NADPH + CO₂', 10.5, C['orange'], weight=700) + T(134, 146, '(G6PD가 첫 효소)', 9.5, C['gray'])
    b += f'<rect x="400" y="20" width="190" height="40" rx="8" fill="#eff6ff" stroke="{C["blue"]}" stroke-width="2"/>' + T(495, 38, '리보스 5-인산', 11.5, C['blue'], weight=900) + T(495, 53, '→ 뉴클레오타이드·DNA·RNA', 9.5, C['gray'])
    b += f'<rect x="400" y="140" width="190" height="40" rx="8" fill="#f0fdf4" stroke="{C["green"]}" stroke-width="2"/>' + T(495, 158, 'F6P · G3P', 11.5, C['green'], weight=900) + T(495, 173, '→ 해당과정으로 재활용', 9.5, C['gray'])
    b += f'<line x1="322" y1="90" x2="396" y2="45" stroke="{C["blue"]}" stroke-width="2" marker-end="url(#pp)"/>' + f'<line x1="322" y1="104" x2="396" y2="158" stroke="{C["green"]}" stroke-width="2" marker-end="url(#pp)"/>'
    b += T(360, 132, '비산화 단계', 10.5, C['green'], weight=900) + T(360, 200, '트랜스케톨레이스(TPP) · 트랜스알돌레이스', 10, C['gray'])
    b += f'<path d="M495,182 C495,215 55,215 55,118" fill="none" stroke="{C["gray"]}" stroke-dasharray="4 3" stroke-width="1.5" marker-end="url(#pp)"/>'
    b += T(270, 212, 'NADPH만 필요할 때: 6탄당으로 되돌려 다시 산화 단계로', 10, C['gray'])
    return svg(W, H + 6, b)


def favism():
    return vflow(['잠두콩 디비신 · 산화성 약물', 'ROS · H₂O₂ 증가', 'G6PD 결핍 → NADPH ↓ → GSH 재생 ↓', 'H₂O₂ 해독 실패 → 막 지질 과산화', '적혈구 파괴 = 용혈성 빈혈'],
                 colors=[C['orange'], C['red'], C['navy'], C['red'], C['red']], box_h=24, gap=16, width=330, font=10.5)


def phospho_why():
    return flow(['포도당 (막 통과 가능)', 'G6P (음전하 → 갇힘)'], arrow_labels=['헥소키나아제 + ATP'], width=420, colors=[C['blue'], C['orange']], box_h=40)


# ------------------------------------------------------------------ summary pages
SUMMARY = []

SUMMARY.append(page('S1', '세포 호흡의 큰 그림 & 해당과정 개요', 'Cellular respiration · Slides 2–6',
  '포도당을 태워 에너지를 얻는 길은 3단계. 그 첫 단계가 <b>해당과정(glycolysis)</b>: 세포질에서 포도당(C6) 1개 → <b>피루브산(C3) 2개</b>. 산소가 없어도 일어난다.',
  f'''<div class="card"><figure class="fig">{three_stage()}</figure></div>
<div class="grid2" style="margin-top:3mm"><div class="card"><h4>📌 해당과정 = 투자 + 회수</h4>{table(['', '준비 단계 ①–⑤', '수익 단계 ⑥–⑩'], [['하는 일', '포도당에 인산 2개 붙여 C3 두 개로 쪼갬', 'G3P 2개 → 피루브산 2개'], ['ATP', '<b>2개 소비</b> (①, ③)', '<b>4개 생산</b> (⑦, ⑩ × 2)'], ['NADH', '—', '<b>2개 생산</b> (⑥ × 2)']])}
 {key('순수확 = <b>ATP 2개 + NADH 2개</b> (포도당 1개당). 해당과정 중간체 10개는 모두 <b>인산이 붙은</b> 형태.')}</div>
<div class="card"><h4>탄소 수 따라가기</h4><p>C6 (포도당) → C6 (G6P·F6P·F1,6BP) → <b>C3 + C3</b> (DHAP·G3P) → C3 × 2 → … → <b>피루브산 C3 × 2</b>. 탄소는 하나도 버려지지 않는다 (CO<sub>2</sub>는 해당과정에서 안 나옴).</p>
 <p>해당(解糖) = 당을 “분해”한다는 뜻. 그리스어 <i>glykys</i>(달다) + <i>lysis</i>(분해).</p>
 {tip('모든 생물이 가진 가장 오래된 에너지 경로. 적혈구(미토콘드리아 없음)는 오직 해당과정으로만 ATP를 얻는다.', '포인트')}</div></div>''',
  ('P2', 'P3')))

SUMMARY.append(page('S2', '준비 단계 ①–⑤ — ATP 2개를 투자', 'Preparatory phase · Slides 7, 10–15',
  '포도당에 인산을 두 번 붙여(①, ③) “잘 쪼개지는 모양”으로 만든 뒤 반으로 자른다(④). 마지막에 DHAP까지 G3P로 바꿔(⑤) G3P 2개가 된다.',
  f'''<div class="grid2"><div class="card">{table(['단계', '반응', '효소', '포인트'], [
  ['<b style="color:#dc2626">①</b>', '포도당 + ATP → G6P', '헥소키나아제 (HK)', '비가역 · Mg²⁺'],
  ['②', 'G6P ⇌ F6P', '포스포헥소스 이성질화효소', '알도스 → 케토스'],
  ['<b style="color:#dc2626">③</b>', 'F6P + ATP → F1,6BP', '<b>PFK-1</b>', '비가역 · <b>첫 확정 단계</b> · 핵심 조절'],
  ['④', 'F1,6BP ⇌ DHAP + G3P', '알돌라아제', 'C6 → C3 + C3 (ΔG′° +23.8)'],
  ['⑤', 'DHAP ⇌ G3P', '삼탄당 인산 이성질화효소 (TPI)', '이제 G3P 2개']], cls='left')}
 <div class="formula">포도당 + 2ATP → 2 G3P + 2ADP &nbsp; (ΔG′° ≈ +2.1)</div></div>
<div><div class="card"><h4>📌 왜 중간체에 인산을 붙일까? (슬라이드 11)</h4><figure class="fig">{phospho_why()}</figure>
 <ol style="margin:.2em 0;padding-left:1.3em"><li><b>세포 밖으로 못 나가게</b> 가둔다 (음전하 + 수송체 없음)</li><li>효소와 강하게 결합 → <b>활성화 에너지 ↓, 특이성 ↑</b></li><li>나중에 ATP로 회수할 <b>에너지 보존</b> (⑦, ⑩)</li></ol></div>
 <div class="card" style="margin-top:3mm"><h4>왜 ②에서 과당으로 바꿀까?</h4><p>포도당(C1 알데하이드) 그대로면 ④의 알돌 절단이 C2–C3에서 일어나 C2 + C4로 짝이 안 맞는다. 케토스(F6P, C2 카보닐)로 바꾸면 C3–C4 사이가 잘려 <b>C3 + C3</b> 대칭이 된다.</p>
 {warn('④ 알돌라아제는 ΔG′° = +23.8(오르막)이지만 세포 속 농도에서는 ΔG ≈ −6 ~ 0 → 진행한다. ΔG′°만 보고 “불가능”이라 하면 틀림!', '함정')}</div></div></div>''',
  ('P1', 'P2', 'P4', 'P5', 'P13', 'P20')))

SUMMARY.append(page('S3', '수익 단계 ⑥–⑩ — ATP 4개와 NADH 2개를 회수', 'Payoff phase · Slides 8, 16–20',
  'G3P 하나당 ATP 2개, NADH 1개 → ×2 하면 <b>ATP 4개 + NADH 2개</b>. ATP는 기질에서 ADP로 인산을 직접 넘기는 <b>기질 수준 인산화</b>(⑦, ⑩)로 만든다.',
  f'''<div class="grid2"><div class="card">{table(['단계', '반응', '효소', '포인트'], [
  ['⑥', 'G3P + Pᵢ + NAD⁺ → 1,3-BPG + NADH', 'G3P 탈수소효소 (GAPDH)', '<b>산화</b> + 고에너지 아실인산'],
  ['⑦', '1,3-BPG + ADP → 3PG + <b>ATP</b>', '포스포글리세르산 키나아제 (PGK)', '첫 ATP (기질 수준)'],
  ['⑧', '3PG ⇌ 2PG', '포스포글리세르산 뮤테이스', '인산 위치 이동'],
  ['⑨', '2PG → PEP + H₂O', '에놀레이스', '탈수 → 고에너지 PEP'],
  ['<b style="color:#dc2626">⑩</b>', 'PEP + ADP → 피루브산 + <b>ATP</b>', '피루브산 키나아제 (PK)', '비가역 · 둘째 ATP']], cls='left')}
 {key('⑥은 해당과정의 <b>유일한 산화 단계</b>. 여기서 NAD⁺가 NADH로 바뀐다 → NAD⁺가 다시 공급되지 않으면 해당과정이 멈춘다 (→ 발효).')}</div>
<div><div class="card"><h4>📌 고에너지 화합물 두 개 (13장과 연결)</h4>{table(['화합물', '가수분해 ΔG′°', '왜 높나'], [['1,3-BPG', '−49.3', '아실인산(산무수물)'], ['PEP', '−61.9', '엔올 → 케토 호변이성화']])}
 <p>둘 다 ATP(−30.5)보다 “위”에 있어 ADP에 인산을 줄 수 있다 → ATP 생성.</p></div>
 <div class="card" style="margin-top:3mm"><h4>기질 수준 인산화 vs 산화적 인산화</h4>{table(['', '기질 수준', '산화적'], [['어디서', '해당 ⑦⑩ · TCA(숙시닐-CoA)', '미토콘드리아 내막'], ['어떻게', '고에너지 기질 → ADP 직접', '전자전달 → H⁺ 기울기 → ATP 합성효소'], ['O₂', '필요 없음', '필요']])}
 {warn('비산염(arsenate)은 ⑥에서 Pᵢ 대신 붙어 곧 분해 → ⑦ ATP가 사라짐 (풀이노트 문제 10).', '함정')}</div></div></div>''',
  ('P3', 'P6', 'P9', 'P10', 'P12')))

SUMMARY.append(page('S4', '해당과정 전체 반응식 · 에너지 · 비가역 단계', 'Overall equation · Slide 9 · Table 14-2',
  '전체: 포도당 + 2NAD⁺ + 2ADP + 2Pᵢ → 2 피루브산 + 2NADH + 2H⁺ + 2ATP + 2H₂O. 산화(−146)에서 나온 에너지로 ATP 합성(+61)을 하고도 <b>−85 kJ/mol</b>이 남는다.',
  f'''<div class="grid2"><div><div class="card"><h4>📌 에너지 장부 (슬라이드 9)</h4>
 {align([('A', '포도당 + 2NAD⁺ → 2 피루브산 + 2NADH + 2H⁺', '−146'), ('B', '2ADP + 2Pᵢ → 2ATP + 2H₂O', '+61'), ('합', '해당과정 전체', '<span class="hl">−85</span>')], cls='sum')}
 <p>남은 −85는 열로 방출 → 해당과정 전체를 한 방향으로 밀어 준다.</p></div>
 <div class="card" style="margin-top:3mm"><h4>표 14-2 · 세포 속 ΔG (적혈구)</h4>{table(['단계', 'ΔG′°', '세포 속 ΔG'], [[n, g, gg] for n, r, e, g, gg, no in GLY])}</div></div>
<div><div class="card"><h4>📌 비가역 3단계 = 조절 지점</h4><p>세포 속 ΔG가 크게 음수인 <b>①(−33) ③(−22) ⑩(−17)</b>만 일방통행. 나머지 7개는 ΔG ≈ 0 (평형 근처, 양방향) → 당신생이 그대로 거꾸로 쓴다.</p>
 <figure class="fig">{img('c14_p19.png', '62%', 'PFK-1 활성 vs [ATP] — ATP는 기질이자 억제제')}</figure>
 <p class="small">PFK-1: <b>ATP·시트르산이 억제</b>(에너지 넉넉), <b>AMP·ADP·과당 2,6-이인산이 활성화</b>(에너지 부족).</p></div>
 {tip('평형 근처 반응은 효소량을 바꿔도 흐름이 거의 안 변한다. 일방통행 반응(①③⑩)의 효소를 조절해야 교통이 바뀐다.', '비유')}</div></div>''',
  ('P1', 'P4', 'P18', 'P19')))

SUMMARY.append(page('S5', '피루브산의 세 가지 운명 · 파스퇴르 & 바르부르크 효과', 'Slides 21, 27–28',
  '산소가 있으면 피루브산은 미토콘드리아에서 완전 산화(ATP 약 30개). 없으면 <b>발효</b>로 NAD⁺만 되돌리고 ATP는 2개뿐.',
  f'''<div class="card"><figure class="fig">{pyruvate_fates()}</figure></div>
<div class="grid2" style="margin-top:3mm"><div class="card"><h4>📌 두 가지 효과 (슬라이드 21)</h4>{table(['효과', '조건', '이유'], [
 ['<b>파스퇴르 효과</b>', '무산소', '포도당당 ATP가 2개뿐 → 포도당을 훨씬 많이 소비. 산소를 넣으면 소비 급감'],
 ['<b>바르부르크 효과</b>', '종양 (산소 있어도)', '해당과정을 빠르게 → ATP + 생합성 재료 확보']], cls='left')}</div>
<div class="card"><h4>💊 약학 포인트</h4><p><b>FDG-PET</b>: 포도당 유사체(¹⁸F-플루오로데옥시포도당)를 주면 해당이 활발한 종양이 밝게 보인다. FDG는 헥소키나아제로 인산화된 뒤 더 진행하지 못하고 세포 안에 갇힘.</p>
 {key('어느 운명이든 공통 목적: 해당과정 ⑥에서 쓴 <b>NAD⁺를 되돌려</b> 해당과정을 계속 돌리는 것.')}</div></div>''',
  ('P7', 'P8', 'P18')))

SUMMARY.append(page('S6', '공급 경로 — 글리코겐 · 이당류 · 갈락토스', 'Feeder pathways · Slides 22–26',
  '포도당 말고도 글리코겐·녹말·이당류·다른 단당류가 <b>해당과정 준비 단계로 합류</b>한다. 핵심은 ① 인산분해(ATP 절약) ② 이당류 가수분해 ③ 갈락토스의 UDP 경로.',
  f'''<div class="grid2"><div><div class="card"><h4>📌 글리코겐 인산분해 (글리코겐 인산화효소)</h4>
 <div class="formula">글리코겐ₙ + Pᵢ → 글리코겐ₙ₋₁ + <b>G1P</b> → (뮤테이스) → G6P</div>
 <p><b>물 대신 Pᵢ로 자른다</b> → 처음부터 인산이 붙어 있어 헥소키나아제(ATP 1개)를 건너뜀 → 순수확 <b>2 → 3 ATP</b> (예제 14-1). 비타민 B₆(PLP) 조효소. (α1→6) 가지는 가지제거 효소가 처리.</p></div>
 <div class="card" style="margin-top:3mm"><h4>이당류는 먼저 가수분해 (소장 융모막)</h4>{table(['이당류', '효소', '산물'], [['엿당 (말토스)', '말테이스', '포도당 + 포도당'], ['젖당 (락토스)', '<b>락테이스</b>', '포도당 + 갈락토스'], ['설탕 (수크로스)', '수크레이스', '포도당 + 과당'], ['트레할로스', '트레할레이스', '포도당 + 포도당']])}
 <p class="small">단당류만 흡수된다. 락테이스 부족 = <b>젖당불내증</b> (대장 세균이 발효 → 가스·설사).</p></div></div>
<div><div class="card"><h4>📌 갈락토스 → G1P (슬라이드 26)</h4>{vflow(['갈락토스', '갈락토스 1-인산', 'UDP-갈락토스 + G1P', 'UDP-포도당 (재사용)'], notes=['갈락토키나아제 (ATP)', 'GALT (UDP-포도당과 교환)', 'UDP-포도당 4-에피머화효소 (NAD⁺)'], colors=[C['orange'], C['red'], C['navy'], C['green']], box_h=24, gap=20, width=520, font=10.5)}
 <p><b>UDP</b> = 육탄당을 실어 나르는 운반체. 이 경로 결함 = <b>갈락토스혈증</b> (신생아 선별검사, 치료는 젖당 제한).</p></div>
 {warn('GALT 결핍(갈락토스 1-인산 축적)이 갈락토키나아제 결핍보다 훨씬 심각 → 갈락토스 1-인산이 더 독하다 (풀이노트 문제 14).', '함정')}</div></div>''',
  ('WE14-1', 'P14')))

SUMMARY.append(page('S7', '발효 — 젖산 · 에탄올, 그리고 코리 회로', 'Fermentation · Slides 27–31',
  '발효의 진짜 목적은 <b>NAD⁺ 재생</b>. 피루브산(또는 아세트알데하이드)에 NADH의 전자를 넘겨 NAD⁺를 되돌린다. 알짜 산화는 없고 ATP는 해당과정의 2개뿐.',
  f'''<div class="grid2"><div><div class="card"><h4>📌 젖산 발효 (근육·적혈구·젖산균)</h4><div class="formula">피루브산 + NADH + H⁺ → 젖산 + NAD⁺ &nbsp; (LDH, ΔG′° −25.1)</div>
 <div class="formula" style="font-size:10pt">포도당 + 2ADP + 2Pᵢ → 2 젖산 + 2ATP + 2H₂O</div></div>
 <div class="card" style="margin-top:3mm"><h4>📌 에탄올 발효 (효모)</h4>{flow(['피루브산', '아세트알데하이드', '에탄올'], arrow_labels=['피루브산 탈카복실화효소 (TPP) −CO₂', '알코올 탈수소효소 (NADH → NAD⁺)'], colors=[C['navy'], C['orange'], C['purple']], box_h=36, width=520)}
 <p class="small">TPP = 티아민(B₁)의 조효소형. 빵이 부푸는 CO₂, 술의 에탄올이 여기서 나온다. 사람은 피루브산 탈카복실화효소가 없다.</p></div></div>
<div><div class="card"><h4>📌 코리 회로 (슬라이드 31)</h4><figure class="fig">{lactate_cori()}</figure>
 {table(['장소', '반응', 'ATP'], [['근육', '포도당 → 2 젖산', '+2'], ['간', '2 젖산 → 포도당 (당신생)', '−6'], ['한 바퀴', '', '<b>−4</b>']])}
 <p class="small">간이 에너지(지방산 산화)를 써서 근육의 “젖산 빚”을 갚아 준다.</p></div>
 {tip('“젖산이 근육 피로의 원인”은 단순화. 발효는 산소 부족 상황에서 ATP를 <b>빨리</b> 얻는 비상 수단이고, 젖산은 간·심장에서 다시 연료로 쓰인다.', '참고')}</div></div>''',
  ('P7', 'P15', 'P16', 'P21', 'P23', 'P24')))

SUMMARY.append(page('S8', '당신생 — 피루브산에서 포도당 만들기', 'Gluconeogenesis · Slides 33–36',
  '굶을 때 뇌·적혈구에 포도당을 대려고 <b>간(일부 신장)</b>이 피루브산·젖산·아미노산·글리세롤로 포도당을 만든다. 해당과정 10단계 중 <b>7개는 거꾸로 공유</b>, 비가역 3곳은 <b>다른 효소로 우회</b>.',
  f'''<div class="grid2"><div class="card"><figure class="fig">{gng_bypass()}</figure></div>
<div><div class="card"><h4>📌 우회 효소 4개</h4>{table(['해당과정 (비가역)', '당신생 우회', '반응'], [
 ['⑩ 피루브산 키나아제', '<b>피루브산 카복실화효소 (PC)</b>', '피루브산 + HCO₃⁻ + ATP → OAA (미토콘드리아, 비오틴, 아세틸-CoA가 활성화)'],
 ['', '<b>PEP 카복시키나아제 (PEPCK)</b>', 'OAA + GTP → PEP + CO₂'],
 ['③ PFK-1', '<b>FBPase-1</b>', 'F1,6BP + H₂O → F6P + Pᵢ'],
 ['① 헥소키나아제', '<b>G6Pase</b>', 'G6P + H₂O → 포도당 + Pᵢ (소포체, 간·신장만)']], cls='left')}</div>
 <div class="card" style="margin-top:3mm"><h4>왜 정확한 역반응이 아닐까?</h4><ol style="margin:.2em 0;padding-left:1.3em"><li><b>열역학</b>: ①③⑩은 ΔG가 크게 음수 → 그대로 거꾸로 못 감</li><li><b>조절</b>: 다른 효소라 두 경로를 <b>반대로(상반)</b> 조절 → 헛된 회로 방지</li></ol>
 {warn('OAA는 미토콘드리아 막을 못 지나간다 → <b>말산</b>으로 바꿔 나온 뒤 세포질에서 다시 OAA (말산 셔틀, 세포질 NADH도 함께 운반).', '함정')}</div></div></div>''',
  ('P17', 'P28', 'P29')))

SUMMARY.append(page('S9', '당신생의 비용과 원료', 'Slides 37–40 · Table 14-3, 14-4',
  '피루브산 2개 → 포도당 1개에 <b>ATP 4 + GTP 2 + NADH 2</b>. 해당과정이 버는 ATP 2개의 3배를 쓴다. 대신 두 경로 모두 세포 속에서 확실히 한 방향(비가역)이 된다.',
  f'''<div class="grid2"><div><div class="card"><h4>📌 비용 계산 (표 14-3)</h4>{table(['단계', 'ATP', 'GTP', 'NADH'], [['PC (×2)', '2', '', ''], ['PEPCK (×2)', '', '2', ''], ['PGK 역반응 (×2)', '2', '', ''], ['GAPDH 역반응 (×2)', '', '', '2'], ['<b>합계</b>', '<b>4</b>', '<b>2</b>', '<b>2</b>']])}
 <div class="formula" style="font-size:9.6pt">2 피루브산 + 4ATP + 2GTP + 2NADH + 2H⁺ + 4H₂O → 포도당 + 4ADP + 2GDP + 6Pᵢ + 2NAD⁺</div>
 <figure class="fig">{atp_ledger([('해당과정 수익', 2, C['green']), ('당신생 비용', -6, C['red']), ('한 바퀴 (헛된 회로)', -4, C['orange'])])}</figure></div></div>
<div><div class="card"><h4>📌 무엇으로 포도당을 만들 수 있나? (당원성)</h4>{table(['원료', '들어가는 곳', '포도당?'], [
 ['젖산', 'LDH → 피루브산', '○ (코리 회로)'], ['알라닌 등 당원성 아미노산', '피루브산·TCA 중간체 → OAA', '○ (포도당-알라닌 회로)'],
 ['글리세롤 (지방의 뼈대)', '→ 글리세롤 3-인산 → DHAP', '○'], ['TCA 중간체 (숙신산 등)', '→ 말산 → OAA', '○'],
 ['짝수 지방산 · 아세틸-CoA', 'PDH가 비가역, TCA에서 C2 들어가 CO₂ 2개 나감', '<b>✕</b>'], ['류신 · 라이신', '아세틸-CoA·아세토아세트산만 생성', '<b>✕</b> (케톤생성성만)']], cls='left')}</div>
 {tip('식물·미생물은 <b>글리옥실산 회로</b>로 아세틸-CoA에서 포도당을 만들 수 있다 (발아 종자, 16장). 동물은 지방산 → 포도당 불가.', '연결')}</div></div>''',
  ('P25', 'P27', 'P30', 'P31', 'P32')))

SUMMARY.append(page('S10', '오탄당 인산 경로(PPP) — NADPH와 리보스 공장', 'Pentose phosphate pathway · Slides 41–45',
  'G6P의 또 다른 길. 에너지(ATP)가 아니라 <b>NADPH</b>(생합성·항산화용 전자)와 <b>리보스 5-인산</b>(핵산 재료)을 만든다. 세포질에서 일어난다.',
  f'''<div class="card"><figure class="fig">{ppp_svg()}</figure></div>
<div class="grid2" style="margin-top:3mm"><div class="card"><h4>📌 산화 단계 (비가역)</h4><div class="formula" style="font-size:10.5pt">G6P + 2NADP⁺ + H₂O → 리불로스 5-인산 + CO₂ + 2NADPH + 2H⁺</div>
 <p>① <b>G6P 탈수소효소 (G6PD)</b>: NADPH 1 (속도 조절 효소) → 락토네이스 → ② 6-포스포글루콘산 탈수소효소: NADPH 1 + CO₂</p></div>
<div class="card"><h4>📌 NADPH는 어디에 쓰나?</h4><ul><li><b>생합성</b>: 지방산·콜레스테롤·스테로이드 (간·지방조직·부신)</li><li><b>항산화</b>: 산화형 글루타싸이온(GSSG) → 환원형 GSH → H₂O₂ 제거 (적혈구)</li></ul>
 <p class="small">페롭토시스(슬라이드 44): NADPH → GSH → GPX4가 지질 과산화물을 없앤다. GPX4를 막으면 철 의존 세포 죽음 → 항암 전략.</p></div></div>''',
  ('P33',)))

SUMMARY.append(page('S11', 'PPP 비산화 단계와 “해당과정이냐 PPP냐”', 'Slides 46–47',
  '비산화 단계는 <b>탄소 레고 재조립</b>: 오탄당 6개 → 육탄당 5개. 그리고 G6P가 어느 길로 갈지는 <b>NADPH/NADP⁺ 비율</b>이 정한다.',
  f'''<div class="grid2"><div><div class="card"><h4>📌 비산화 단계 (가역)</h4>{table(['효소', '옮기는 것', '조효소'], [['<b>트랜스케톨레이스</b>', '탄소 2개 조각', '<b>TPP</b> (B₁)'], ['<b>트랜스알돌레이스</b>', '탄소 3개 조각', '—']], cls='left')}
 <p>리불로스 5-인산 → 리보스 5-인산 / 자일룰로스 5-인산 → (재배열) → <b>F6P·G3P</b> → 해당과정·당신생으로.</p>
 <div class="formula" style="font-size:10.5pt">6 오탄당 (C5 × 6 = 30) → 5 육탄당 (C6 × 5 = 30)</div></div>
 <div class="card" style="margin-top:3mm"><h4>세포의 필요에 따른 4가지 모드</h4>{table(['필요', 'PPP가 하는 일'], [['리보스 ≫ NADPH', '비산화 단계를 거꾸로: F6P·G3P → 리보스 5-인산'], ['NADPH ≫ 리보스', '오탄당 → G6P로 되돌려 다시 산화 (계속 순환)'], ['둘 다', '산화 단계만'], ['NADPH + ATP', '오탄당 → 해당과정으로 → 피루브산']], cls='left')}</div></div>
<div><div class="card"><h4>📌 G6P 갈림길 (슬라이드 47)</h4>{table(['세포 상태', 'G6PD', 'G6P의 행선지'], [['NADPH 많음', '<b>억제</b>', '해당과정'], ['NADP⁺ 많음 (NADPH 소비 ↑)', '활성', 'PPP']])}
 <p>산물(NADPH)이 첫 효소(G6PD)를 억제하는 되먹임 조절. 해당과정·PPP·당신생 모두 세포질 → 효소·중간체 공유.</p></div>
 {key('G6P는 포도당의 세 갈래 길목: <b>해당과정</b>(ATP) · <b>PPP</b>(NADPH·리보스) · <b>글리코겐</b>(저장).')}</div></div>''',
  ('P33',)))

SUMMARY.append(page('S12', 'G6PD 결핍 · 파비즘 · 말라리아 · 베르니케-코르사코프', 'Slides 48–53 · 약학 포인트',
  '<b>G6PD 결핍</b> = PPP의 문지기 효소가 약해 NADPH가 부족한 유전 질환(X 연관, 남성에 흔함). 평소엔 괜찮다가 <b>산화 스트레스</b>가 오면 적혈구가 터진다.',
  f'''<div class="grid2"><div><div class="card"><h4>📌 파비즘의 기전 (슬라이드 51)</h4><figure class="fig">{favism()}</figure>
 <p class="small">적혈구는 미토콘드리아가 없어 NADPH를 <b>PPP에서만</b> 얻는다 → 가장 취약. 피타고라스가 제자들에게 잠두콩을 금했다는 이야기(슬라이드 49).</p></div></div>
<div><div class="card"><h4>📌 왜 이 유전자가 남았을까? (슬라이드 52)</h4><p>G6PD 결핍 적혈구는 산화 손상에 약한 <b>말라리아 원충</b>(<i>P. falciparum</i>)도 살기 어렵다 → <b>말라리아 저항성</b> (열대 아프리카인의 약 25%). 겸상적혈구와 같은 자연선택 논리.</p>
 {warn('<b>프리마퀸</b>(항말라리아제)·설폰아마이드·다프손 등 산화성 약물은 G6PD 결핍자에게 용혈 → 투약 전 G6PD 검사!', '약학')}</div>
 <div class="card" style="margin-top:3mm"><h4>📌 베르니케-코르사코프 증후군 (슬라이드 53)</h4><p><b>티아민(B₁) 결핍</b>(과음 → 흡수 ↓) + <b>트랜스케톨레이스 변이</b>(TPP 친화도 ↓) → TPP 부족 → PPP 비산화 단계 ↓ → 기억 상실·혼란·부분 마비.</p>
 <p class="small">알코올 중독 환자에게는 포도당보다 <b>티아민을 먼저</b> 투여. TPP는 PDH·α-KG 탈수소효소에도 필요(16장).</p></div></div></div>''',
  ()))

SUMMARY.append(page('S13', '14장 한 장 요약 + 시험 직전 체크리스트', 'Summary · Slides 32, 54',
  '교수님 요약 슬라이드(해당과정·PPP)와 체크리스트를 숫자·효소 이름과 함께 정리했다.',
  f'''<div class="grid3">
 <div class="card"><h4>① 해당과정</h4><ul style="font-size:.95em"><li>포도당 → 2 피루브산, 세포질, O₂ 불필요</li><li>준비 −2 ATP / 수익 +4 ATP, +2 NADH → <b>순 2 ATP + 2 NADH</b></li><li>비가역 <b>①HK ③PFK-1 ⑩PK</b> = 조절 지점</li><li>기질 수준 인산화 ⑦⑩ (1,3-BPG, PEP)</li><li>ΔG′° 전체 −85 kJ/mol</li><li>중간체 10개 모두 인산화</li></ul></div>
 <div class="card"><h4>② 발효 · 당신생</h4><ul style="font-size:.95em"><li>발효 목적 = <b>NAD⁺ 재생</b> (LDH / PDC(TPP)+ADH)</li><li>코리 회로: 근육 +2, 간 −6 → −4</li><li>우회 효소: <b>PC · PEPCK · FBPase-1 · G6Pase</b></li><li>비용: 4 ATP + 2 GTP + 2 NADH</li><li>당원성 ○: 젖산·알라닌·글리세롤 / ✕: 짝수 지방산, 류신·라이신</li></ul></div>
 <div class="card"><h4>③ 오탄당 인산 경로</h4><ul style="font-size:.95em"><li>산화: G6P → Ru5P + CO₂ + <b>2NADPH</b> (G6PD)</li><li>비산화: 오탄당 6 ⇄ 육탄당 5 (TK·TPP, TA)</li><li>조절: <b>NADPH/NADP⁺</b> (NADPH가 G6PD 억제)</li><li>G6PD 결핍 → 파비즘·용혈, 말라리아 저항</li><li>티아민 결핍 → 베르니케-코르사코프</li></ul></div>
</div>
<div class="grid2" style="margin-top:3mm"><div class="card"><h4>🔢 꼭 외울 숫자</h4><div class="tiles" style="grid-template-columns:repeat(3,1fr)">
 <div><b>해당 순수확</b><span>2 ATP</span><small>+ 2 NADH</small></div><div><b>해당 ΔG′°</b><span>−85</span><small>kJ/mol</small></div><div><b>당신생 비용</b><span>6 ~P</span><small>4 ATP + 2 GTP</small></div>
 <div><b>코리 회로</b><span>−4 ATP</span><small>한 바퀴</small></div><div><b>글리코겐 인산분해</b><span>3 ATP</span><small>포도당 1개당</small></div><div><b>PPP</b><span>2 NADPH</span><small>G6P 1개당</small></div></div></div>
 <div class="card"><h4>⚠️ 단골 함정</h4><ol style="margin:.2em 0;padding-left:1.3em;font-size:.95em"><li>알돌라아제 ΔG′° +23.8이어도 세포 속에선 진행</li><li>⑥은 산화(NAD⁺), ⑦⑩이 ATP</li><li>당신생 ≠ 해당과정 역반응 (우회 4개)</li><li>OAA는 막 통과 ✕ → 말산 셔틀</li><li>G6Pase는 간·신장만 (근육 ✕)</li><li>NADH(이화) vs NADPH(동화·항산화)</li></ol></div></div>''',
  ()))

MAPROWS = [['S1–S4 해당과정', '문제 1–6·9·10·12·13·18·19·20'], ['S5, S7 발효', '문제 7·8·15·16·21·23·24'], ['S6 공급 경로', '예제 14-1, 문제 14'],
           ['S8–S9 당신생', '문제 17·25·27–32'], ['S10–S12 PPP', '문제 33']]

# ------------------------------------------------------------------ glossary
GLOSS = [
 ('ATP · ADP', 'Adenosine Tri- / Diphosphate', '아데노신 삼인산 · 이인산', '에너지 화폐와 그 사용 후 형태'),
 ('GTP · GDP', 'Guanosine Tri- / Diphosphate', '구아노신 삼인산 · 이인산', 'PEPCK가 쓰는 에너지 화폐'),
 ('UTP · UDP', 'Uridine Tri- / Diphosphate', '유리딘 삼인산 · 이인산', '당을 실어 나르는 운반체(UDP-당)'),
 ('Pᵢ', 'inorganic Phosphate', '무기 인산', 'HPO₄²⁻'),
 ('NAD⁺ / NADH', 'Nicotinamide Adenine Dinucleotide', '니코틴아마이드 아데닌 다이뉴클레오타이드', '해당 ⑥에서 전자를 받는 이화용 운반체'),
 ('NADP⁺ / NADPH', 'NAD Phosphate', 'NAD 인산', 'PPP가 만드는 생합성·항산화용 전자'),
 ('G1P · G6P', 'Glucose 1- / 6-Phosphate', '포도당 1-·6-인산', 'G6P = 해당·PPP·글리코겐의 갈림길'),
 ('F6P', 'Fructose 6-Phosphate', '과당 6-인산', '해당 ② 산물'),
 ('F1,6BP (FBP)', 'Fructose 1,6-Bisphosphate', '과당 1,6-이인산', '해당 ③ 산물, 알돌라아제 기질'),
 ('F2,6BP', 'Fructose 2,6-Bisphosphate', '과당 2,6-이인산', 'PFK-1의 가장 강한 활성화제 (15장)'),
 ('DHAP', 'Dihydroxyacetone Phosphate', '다이하이드록시아세톤 인산', '④ 산물, TPI로 G3P가 됨'),
 ('G3P (GAP)', 'Glyceraldehyde 3-Phosphate', '글리세르알데하이드 3-인산', '수익 단계의 출발 물질'),
 ('1,3-BPG', '1,3-Bisphosphoglycerate', '1,3-이인산글리세르산', '고에너지 아실인산 (−49.3)'),
 ('3PG · 2PG', '3- / 2-Phosphoglycerate', '3-·2-포스포글리세르산', '해당 ⑦⑧ 산물'),
 ('PEP', 'Phosphoenolpyruvate', '포스포엔올피루브산', '가장 높은 인산 전달 전위 (−61.9)'),
 ('HK', 'Hexokinase', '헥소키나아제', '① 포도당 → G6P (비가역)'),
 ('PGI', 'Phosphoglucose(hexose) Isomerase', '포스포헥소스 이성질화효소', '② G6P ⇌ F6P'),
 ('PFK-1', 'Phosphofructokinase-1', '포스포프룩토키나아제-1', '③ 첫 확정 단계, 핵심 조절 효소'),
 ('TPI', 'Triose Phosphate Isomerase', '삼탄당 인산 이성질화효소', '⑤ DHAP ⇌ G3P'),
 ('GAPDH', 'Glyceraldehyde 3-Phosphate Dehydrogenase', 'G3P 탈수소효소', '⑥ 유일한 산화 단계 (NADH)'),
 ('PGK', 'Phosphoglycerate Kinase', '포스포글리세르산 키나아제', '⑦ 첫 ATP 생성'),
 ('PK', 'Pyruvate Kinase', '피루브산 키나아제', '⑩ PEP → 피루브산 + ATP (비가역)'),
 ('LDH', 'Lactate Dehydrogenase', '젖산 탈수소효소', '피루브산 ⇌ 젖산, NAD⁺ 재생'),
 ('PDC', 'Pyruvate Decarboxylase', '피루브산 탈카복실화효소', '효모: 피루브산 → 아세트알데하이드 + CO₂'),
 ('ADH', 'Alcohol Dehydrogenase', '알코올 탈수소효소', '아세트알데하이드 → 에탄올'),
 ('TPP', 'Thiamine Pyrophosphate', '티아민 피로인산', 'B₁ 조효소 (PDC·트랜스케톨레이스·PDH)'),
 ('PLP', 'Pyridoxal Phosphate', '피리독살 인산', 'B₆ 조효소, 글리코겐 인산화효소에 결합'),
 ('GALT', 'Galactose 1-Phosphate Uridylyltransferase', '갈락토스 1-인산 유리딜전이효소', '결핍 → 고전적 갈락토스혈증'),
 ('PC', 'Pyruvate Carboxylase', '피루브산 카복실화효소', '당신생 첫 우회: 피루브산 → OAA (비오틴)'),
 ('PEPCK', 'PEP Carboxykinase', 'PEP 카복시키나아제', 'OAA + GTP → PEP + CO₂'),
 ('OAA', 'Oxaloacetate', '옥살로아세트산', '막 통과 ✕ → 말산 형태로 이동'),
 ('FBPase-1', 'Fructose 1,6-Bisphosphatase 1', '과당 1,6-이인산가수분해효소', 'PFK-1 우회 (당신생)'),
 ('G6Pase', 'Glucose 6-Phosphatase', '포도당 6-인산가수분해효소', '마지막 우회, 간·신장 소포체에만'),
 ('ER', 'Endoplasmic Reticulum', '소포체', 'G6Pase가 있는 곳'),
 ('Acetyl-CoA', 'Acetyl Coenzyme A', '아세틸 조효소 A', '포도당이 될 수 없는 C2 조각'),
 ('TCA', 'Tricarboxylic Acid cycle', '시트르산 회로 (크렙스 회로)', '아세틸-CoA를 CO₂로 (16장)'),
 ('PDH', 'Pyruvate Dehydrogenase', '피루브산 탈수소효소', '피루브산 → 아세틸-CoA (비가역)'),
 ('PPP', 'Pentose Phosphate Pathway', '오탄당 인산 경로', 'NADPH + 리보스 5-인산 생산'),
 ('G6PD', 'Glucose 6-Phosphate Dehydrogenase', 'G6P 탈수소효소', 'PPP 첫 효소, NADPH가 억제'),
 ('R5P · Ru5P · Xu5P', 'Ribose / Ribulose / Xylulose 5-Phosphate', '리보스·리불로스·자일룰로스 5-인산', 'PPP의 오탄당 인산들'),
 ('TK · TA', 'Transketolase · Transaldolase', '트랜스케톨레이스 · 트랜스알돌레이스', 'C2 · C3 조각을 옮기는 재배열 효소'),
 ('GSH · GSSG', 'reduced / oxidized Glutathione', '환원형 · 산화형 글루타싸이온', 'NADPH로 재생, H₂O₂ 제거'),
 ('ROS', 'Reactive Oxygen Species', '활성산소종', 'H₂O₂ 등, 적혈구막 손상'),
 ('GPX4', 'Glutathione Peroxidase 4', '글루타싸이온 과산화효소 4', '지질 과산화물 제거, 막으면 페롭토시스'),
 ('FDG-PET', 'Fluorodeoxyglucose Positron Emission Tomography', '플루오로데옥시포도당 양전자 단층촬영', '해당이 활발한 종양을 찾는 검사'),
 ('ΔG′° · ΔG', '(standard) free-energy change', '(표준) 자유에너지 변화', '방향 판단 (13장)'),
]
ABBR_KEYS = {
 'ATP · ADP': r'\b(ATP|ADP)\b', 'GTP · GDP': r'\b(GTP|GDP)\b', 'UTP · UDP': r'\b(UTP|UDP)', 'Pᵢ': r'(?<!P)P[iᵢ](?![a-zA-Z])',
 'NAD⁺ / NADH': r'NAD(?!P)', 'NADP⁺ / NADPH': r'NADP', 'G1P · G6P': r'\bG[16]P\b', 'F6P': r'\bF6P\b', 'F1,6BP (FBP)': r'F1,6BP',
 'F2,6BP': r'F2,6BP|과당 2,6', 'DHAP': r'DHAP', 'G3P (GAP)': r'\bG3P\b', '1,3-BPG': r'BPG', '3PG · 2PG': r'\b[23]PG\b', 'PEP': r'\bPEP\b',
 'HK': r'\bHK\b|헥소키나아제', 'PGI': r'PGI|이성질화효소', 'PFK-1': r'PFK', 'TPI': r'\bTPI\b', 'GAPDH': r'GAPDH', 'PGK': r'\bPGK\b',
 'PK': r'\bPK\b|피루브산 키나아제', 'LDH': r'\bLDH\b', 'PDC': r'\bPDC\b|피루브산 탈카복실화효소', 'ADH': r'\bADH\b|알코올 탈수소효소', 'TPP': r'\bTPP\b',
 'PLP': r'\bPLP\b', 'GALT': r'GALT', 'PC': r'\bPC\b|피루브산 카복실화효소', 'PEPCK': r'PEPCK', 'OAA': r'\bOAA\b', 'FBPase-1': r'FBPase',
 'G6Pase': r'G6Pase', 'ER': r'소포체', 'Acetyl-CoA': r'아세틸-CoA', 'TCA': r'\bTCA\b', 'PDH': r'\bPDH\b', 'PPP': r'\bPPP\b|오탄당 인산 경로',
 'G6PD': r'G6PD', 'R5P · Ru5P · Xu5P': r'Ru5P|리보스 5-인산|리불로스|자일룰로스', 'TK · TA': r'트랜스케톨레이스|트랜스알돌레이스|\bTK\b',
 'GSH · GSSG': r'GSH|GSSG|글루타싸이온', 'ROS': r'\bROS\b', 'GPX4': r'GPX4', 'FDG-PET': r'FDG', 'ΔG′° · ΔG': r'ΔG',
}

# ------------------------------------------------------------------ concept checks
CHECKS = [
 dict(id='C1', num='1', title='해당과정 준비 단계', sec='S1–S2', level=1,
  q='''<p><b>1.</b> (O/X) 해당과정은 미토콘드리아에서 일어나며 산소가 꼭 필요하다.</p>
<p><b>2.</b> (빈칸) 해당과정의 비가역 3단계 효소는 ( &nbsp;&nbsp; ), ( &nbsp;&nbsp; ), ( &nbsp;&nbsp; )이다.</p>
<p><b>3.</b> (서술) 해당과정 중간체에 인산을 붙이는 이유 3가지를 써라.</p>
<p><b>4.</b> (서술) ② 단계에서 G6P를 F6P(케토스)로 바꾸는 이유는?</p>''',
  answer=chips('1. <b>X</b> (세포질, O₂ 불필요)', '2. <b>헥소키나아제 · PFK-1 · 피루브산 키나아제</b>', '3. 세포 안에 가둠 · 효소 결합(Eₐ ↓·특이성 ↑) · 에너지 보존', '4. ④에서 <b>C3 + C3</b>로 대칭 절단하려고'),
  explain=fig(gly_map(), '①③⑩ = 비가역') + steps('1. 해당과정은 세포질, 무산소에서도 진행 (그래서 발효가 가능).',
   '2. 세포 속 ΔG가 크게 음수인 ①(−33) ③(−22) ⑩(−17).', '3. 음전하 인산은 막을 못 지나가고(수송체 없음), 효소 활성 부위에 강하게 결합하며, 나중에 ⑦⑩에서 ATP로 회수된다.',
   '4. 알도스(C1 알데하이드) 상태로 알돌 절단하면 C2 + C4가 된다. 케토스(C2 카보닐)로 바꾸면 C3–C4가 잘려 C3 두 개.') +
   tip('“HK–PFK–PK” 세 개의 K(kinase)가 비가역이라고 기억!', '암기')),
 dict(id='C2', num='2', title='수익 단계와 에너지 수지', sec='S3–S4', level=1,
  q='''<p><b>1.</b> (계산) 포도당 1개가 해당과정을 지날 때 생산 ATP, 소비 ATP, 순 ATP, NADH 수는?</p>
<p><b>2.</b> (빈칸) 기질 수준 인산화가 일어나는 해당 단계는 ( &nbsp; )와 ( &nbsp; )이고, 인산을 주는 고에너지 화합물은 ( &nbsp;&nbsp; )와 ( &nbsp;&nbsp; )이다.</p>
<p><b>3.</b> (계산) A: 포도당 + 2NAD⁺ → 2 피루브산 + 2NADH (−146), B: 2ADP + 2Pᵢ → 2ATP + 2H₂O (+61). 전체 ΔG′°는?</p>
<p><b>4.</b> (O/X) 알돌라아제 반응은 ΔG′°가 +23.8 kJ/mol이므로 세포에서 정방향으로 진행할 수 없다.</p>''',
  answer=chips('1. 생산 <b>4</b> · 소비 <b>2</b> · 순 <b>2</b> · NADH <b>2</b>', '2. <b>⑦, ⑩</b> / <b>1,3-BPG, PEP</b>', '3. <b>−85 kJ/mol</b>', '4. <b>X</b> (세포 속 ΔG ≈ −6 ~ 0)'),
  explain=fig(atp_ledger([('준비 단계', -2, C['red']), ('수익 단계 (×2)', 4, C['green']), ('순수확', 2, C['orange'])]), '') +
   steps('1. ①③에서 −2, ⑦⑩ × 2에서 +4 → 순 +2. ⑥ × 2에서 NADH 2.', '3. −146 + 61 = −85 (13장 가산성).',
         '4. 생성물 2개(DHAP, G3P)의 농도가 매우 낮아 Q가 아주 작다 → RT ln Q가 크게 음수 → 실제 ΔG ≤ 0. 자발성은 ΔG′°가 아니라 ΔG로!') +
   key('⑥ 산화(NADH) → ⑦ ATP, ⑨ 탈수 → ⑩ ATP: “고에너지 화합물을 만든 직후 ATP로 바꾼다”는 패턴.')),
 dict(id='C3', num='3', title='공급 경로', sec='S6', level=1,
  q='''<p><b>1.</b> (계산) 글리코겐의 포도당 단위 1개가 인산분해로 해당과정에 들어가면 순 ATP는 몇 개인가? 유리 포도당과 비교하면?</p>
<p><b>2.</b> (빈칸) 갈락토스 → G1P 경로의 효소 3개: ( &nbsp;&nbsp; ) → ( &nbsp;&nbsp; ) → ( &nbsp;&nbsp; )</p>
<p><b>3.</b> (O/X) 설탕(수크로스)은 그대로 소장에서 흡수되어 혈액으로 들어간다.</p>
<p><b>4.</b> (단답) 젖당불내증에서 부족한 효소는? 증상이 생기는 이유는?</p>''',
  answer=chips('1. <b>3 ATP</b> (유리 포도당 2 → 1개 절약)', '2. <b>갈락토키나아제 → GALT → UDP-포도당 4-에피머화효소</b>', '3. <b>X</b> (단당류만 흡수)', '4. <b>락테이스</b> / 소화 안 된 젖당을 대장 세균이 발효 → 가스·설사'),
  explain=steps('1. 인산분해는 처음부터 G1P(인산 붙음) → G6P: 헥소키나아제 ATP 1개를 안 써서 4 − 1 = 3.',
   '2. 갈락토스 + ATP → 갈락토스 1-인산 → (UDP-포도당과 교환) UDP-갈락토스 + G1P → UDP-갈락토스는 에피머화효소로 UDP-포도당이 되어 재사용.',
   '3. 수크레이스가 포도당 + 과당으로 분해한 뒤 흡수.', '4. 락테이스는 젖을 떼면서 줄어드는 사람이 많다 (성인 젖당불내증).') +
   fig(flow(['글리코겐', 'G1P', 'G6P'], arrow_labels=['+ Pᵢ (ATP 0)', '뮤테이스'], width=420), '') +
   tip('갈락토스혈증 신생아는 모유·분유의 젖당을 끊어야 한다.', '임상')),
 dict(id='C4', num='4', title='발효와 코리 회로', sec='S5, S7', level=1,
  q='''<p><b>1.</b> (서술) 발효의 진짜 목적은 무엇인가?</p>
<p><b>2.</b> (빈칸) 효모의 에탄올 발효: 피루브산 —( &nbsp;&nbsp; , 조효소 &nbsp; )→ 아세트알데하이드 + CO₂ —( &nbsp;&nbsp; , NADH 사용)→ 에탄올</p>
<p><b>3.</b> (계산) 코리 회로 한 바퀴(포도당 → 2 젖산 → 포도당)의 ATP 수지는?</p>
<p><b>4.</b> (O/X) 젖산 발효에서도 CO₂가 생긴다. / 파스퇴르 효과란 산소가 있을 때 포도당 소비가 늘어나는 현상이다.</p>''',
  answer=chips('1. <b>NAD⁺ 재생</b> → 해당 ⑥이 계속 돌게', '2. <b>피루브산 탈카복실화효소, TPP</b> / <b>알코올 탈수소효소</b>', '3. +2 − 6 = <b>−4 ATP</b>', '4. <b>X</b> / <b>X</b> (무산소일 때 소비 ↑)'),
  explain=fig(lactate_cori(), '') + steps('1. NAD⁺는 양이 적어서 재생하지 않으면 해당과정이 곧 멈춘다. 발효는 ATP를 더 만들지 않는다.',
   '3. 근육: 해당 +2 / 간: 당신생 −6 (ATP 4 + GTP 2) → −4. 간이 지방산 산화로 비용을 낸다.',
   '4. 젖산 발효: 피루브산 → 젖산 (CO₂ 없음). CO₂는 에탄올 발효에서. 파스퇴르 효과: 산소가 <b>없으면</b> 포도당 소비가 크게 늘어난다.')),
 dict(id='C5', num='5', title='당신생', sec='S8–S9', level=2,
  q='''<p><b>1.</b> (짝짓기) 해당 효소 — 당신생 우회 효소를 짝지어라: 헥소키나아제 / PFK-1 / 피루브산 키나아제</p>
<p><b>2.</b> (계산) 피루브산 2개로 포도당 1개를 만들 때 고에너지 인산(ATP+GTP) 몇 개, NADH 몇 개가 필요한가?</p>
<p><b>3.</b> (O/X) 사람은 팔미트산(짝수 지방산)으로 포도당을 알짜로 만들 수 있다. / 류신과 라이신은 케톤생성성 아미노산이다.</p>
<p><b>4.</b> (서술) 근육에는 G6Pase가 없다. 이것이 의미하는 것은?</p>''',
  answer=chips('1. HK → <b>G6Pase</b> / PFK-1 → <b>FBPase-1</b> / PK → <b>PC + PEPCK</b>', '2. <b>6개</b> (ATP 4 + GTP 2), NADH <b>2개</b>', '3. <b>X</b> / <b>O</b>', '4. 근육 글리코겐은 <b>혈당을 올릴 수 없다</b> (자기 ATP용)'),
  explain=fig(gng_bypass(), '') + steps('2. PC 2 + PEPCK 2(GTP) + PGK 역 2 = 6, GAPDH 역 2 NADH.',
   '3. 아세틸-CoA는 PDH가 비가역이라 피루브산이 못 되고, TCA에서는 C2가 들어가 CO₂ 2개가 나가서 알짜 0.',
   '4. G6P는 막을 못 나가므로 근육은 포도당을 혈액으로 내보내지 못한다. 혈당 유지는 간(과 신장)의 일.') +
   warn('PC는 미토콘드리아, PEPCK는 세포질·미토콘드리아 둘 다. OAA는 말산으로 바뀌어 막을 넘는다.', '함정')),
 dict(id='C6', num='6', title='오탄당 인산 경로', sec='S10–S11', level=2,
  q='''<p><b>1.</b> (빈칸) 산화 단계: G6P + 2( &nbsp; ) + H₂O → ( &nbsp;&nbsp; ) + CO₂ + 2( &nbsp;&nbsp; ) + 2H⁺</p>
<p><b>2.</b> (서술) NADPH가 많을 때와 NADP⁺가 많을 때 G6P는 각각 어디로 가는가? 그 이유는?</p>
<p><b>3.</b> (상황) 지방산을 활발히 합성하는 지방세포는 NADPH는 많이, 리보스는 거의 필요 없다. PPP는 어떻게 작동하나?</p>
<p><b>4.</b> (빈칸) 트랜스케톨레이스는 탄소 ( &nbsp; )개를, 트랜스알돌레이스는 ( &nbsp; )개를 옮기며, 트랜스케톨레이스의 조효소는 ( &nbsp;&nbsp; )이다.</p>''',
  answer=chips('1. <b>NADP⁺</b> / <b>리불로스 5-인산</b> / <b>NADPH</b>', '2. NADPH 많음 → <b>해당과정</b> / NADP⁺ 많음 → <b>PPP</b> (NADPH가 G6PD 억제)', '3. 오탄당 → 비산화 단계로 <b>F6P → G6P</b>로 되돌려 다시 산화 (순환)', '4. <b>2</b> / <b>3</b> / <b>TPP</b>'),
  explain=fig(ppp_svg(), '') + steps('2. 산물(NADPH)이 첫 효소를 억제하는 되먹임. NADPH를 쓰면 NADP⁺가 늘어 G6PD가 다시 켜진다.',
   '3. 6 G6P → 6 Ru5P + 12 NADPH + 6 CO₂ → 비산화 단계로 5 G6P 재생 → 알짜로 G6P 1개를 CO₂ 6개로 태우며 NADPH 12개.') +
   tip('G6P의 세 갈래: 해당(ATP) · PPP(NADPH·리보스) · 글리코겐(저장).', '정리')),
 dict(id='C7', num='7', title='임상 연결 — G6PD 결핍 · WKS · 종양', sec='S5, S12', level=1,
  q='''<p><b>1.</b> (순서) 파비즘이 일어나는 순서로 나열하라: (가) NADPH ↓ (나) 디비신이 ROS 생성 (다) 적혈구막 지질 과산화 (라) GSH 재생 ↓ (마) 용혈</p>
<p><b>2.</b> (서술) G6PD 결핍 유전자가 열대 아프리카에 흔하게 남은 이유는?</p>
<p><b>3.</b> (단답) 베르니케-코르사코프 증후군의 원인 두 가지와, 알코올 중독 환자에게 포도당보다 먼저 줘야 하는 것은?</p>
<p><b>4.</b> (서술) FDG-PET으로 종양이 밝게 보이는 이유를 바르부르크 효과로 설명하라.</p>''',
  answer=chips('1. <b>(나) → (가) → (라) → (다) → (마)</b>', '2. <b>말라리아 저항성</b> (원충이 산화 손상에 약함)', '3. 티아민(B₁) 결핍 + 트랜스케톨레이스 변이(TPP 친화도 ↓) / <b>티아민</b>', '4. 종양은 산소가 있어도 해당과정이 빠름 → FDG를 많이 흡수·인산화해 갇힘'),
  explain=fig(favism(), '') + steps('1. 디비신 → ROS·H₂O₂ ↑ → (G6PD 결핍이라) NADPH ↓ → GSH ↓ → H₂O₂ 해독 실패 → 막 지질 과산화 → 용혈.',
   '2. 결핍 적혈구 안에서는 말라리아 원충(<i>P. falciparum</i>)이 산화 스트레스로 잘 못 자란다 → 말라리아 유행 지역에서 생존 이득 → 자연선택.',
   '4. FDG는 헥소키나아제로 FDG-6-인산이 된 뒤 다음 효소가 못 써서 세포에 갇힌다 → 포도당을 많이 먹는 세포일수록 신호가 강함.') +
   warn('프리마퀸·설폰아마이드·다프손 → G6PD 결핍자 용혈 위험.', '약학')),
]
CHECK_AFTER = {1: 'C1', 3: 'C2', 5: 'C3', 6: 'C4', 8: 'C5', 10: 'C6', 11: 'C7'}

def __getattr__(name):  # 교수님 테스트뱅크 (순환 import 방지: 지연 로드)
    if name == 'TB':
        from tb14 import TB
        return TB
    raise AttributeError(name)

if __name__ == '__main__':
    import exam14 as M
    examlib.render(M)
