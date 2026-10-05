# -*- coding: utf-8 -*-
"""16장 시험대비 요약노트.  python3 exam16.py → exam_ch16.pdf"""
import os, sys
os.environ['CH'] = '16'
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from helpers import *
import examlib
import ch16
from ch16 import tca_wheel, TCA

CH = 16
CH_TITLE = '시트르산 회로'
FOOT = 'Lehninger 8e · Ch.16 시트르산 회로 — 시험대비 요약노트'

_items = [i for i in ch16.ALL_ITEMS if i['level'] < 3]
WB = {i['id']: 6 + k for k, i in enumerate(_items)}
link = examlib.make_link(WB, CH)
page = examlib.make_page(link)


# ------------------------------------------------------------------ drawings
def carbon_flow():
    W, H = 560, 150
    b = arrowdef('cf', C['gray']) + arrowdef('cf2', C['red'])
    def dots(x, n, col, lab, sub, y=40):
        s = ''.join(f'<circle cx="{x + k*13:.1f}" cy="{y}" r="5.5" fill="{col}"/>' for k in range(n))
        c = x + (n - 1) * 6.5
        return s + T(c, y + 24, lab, 10.5, C['ink'], weight=700) + T(c, y + 38, sub, 9.5, C['gray'])
    def ar(x1, x2, lab):
        return f'<line x1="{x1}" y1="40" x2="{x2}" y2="40" stroke="{C["gray"]}" stroke-width="2" marker-end="url(#cf)"/>' + T((x1 + x2) / 2, 30, lab, 9.5, C['orange'], weight=700)
    def co2(x, lab):
        return f'<line x1="{x}" y1="80" x2="{x}" y2="116" stroke="{C["red"]}" stroke-width="1.6" marker-end="url(#cf2)" stroke-dasharray="3 2"/>' + T(x, 132, lab, 10, C['red'], weight=700)
    b += dots(10, 6, C['navy'], '포도당', '6C') + ar(84, 128, '해당')
    b += dots(140, 3, C['blue'], '피루브산 ×2', '3C') + ar(178, 228, 'PDH')
    b += dots(240, 2, C['orange'], '아세틸-CoA ×2', '2C') + ar(264, 322, '+ OAA(4C)')
    b += dots(334, 6, C['green'], '시트르산', '6C') + ar(408, 456, '회로')
    b += dots(468, 4, C['purple'], 'OAA 재생', '4C')
    b += co2(203, 'CO₂ 1개 ×2') + co2(432, 'CO₂ 2개 ×2')
    return svg(W, H, b)


def pdh_arm():
    W, H = 540, 210
    b = arrowdef('pa', C['gray'])
    for x, col, nm, en, co in [(80, '#eab308', 'E1', '피루브산 탈수소효소', 'TPP'), (270, C['green'], 'E2', '다이하이드로리포일 아세틸전달효소', '리포산 · CoA'), (460, C['red'], 'E3', '다이하이드로리포일 탈수소효소', 'FAD · NAD⁺')]:
        b += f'<circle cx="{x}" cy="70" r="46" fill="white" stroke="{col}" stroke-width="3"/>' + T(x, 66, nm, 20, col, weight=900) + T(x, 86, co, 10.5, C['ink'], weight=700)
        b += T(x, 136, en, 9.5, C['gray'])
    b += f'<path d="M120 40 Q 195 0 232 44" fill="none" stroke="{C["orange"]}" stroke-width="2.4" marker-end="url(#pa)"/>' + T(176, 14, '히드록시에틸 → 아세틸', 10, C['orange'], weight=700)
    b += f'<path d="M308 44 Q 360 0 420 40" fill="none" stroke="{C["orange"]}" stroke-width="2.4" marker-end="url(#pa)"/>' + T(364, 14, '리포일 팔이 전자 전달', 10, C['orange'], weight=700)
    b += T(80, 162, '① 피루브산 → CO₂ 방출', 10.5, C['ink'], weight=700)
    b += T(270, 162, '②③ 아세틸 → CoA = 아세틸-CoA', 10.5, C['ink'], weight=700)
    b += T(460, 162, '④⑤ FADH₂ → NADH', 10.5, C['ink'], weight=700)
    b += T(270, 194, '리포일라이신 “긴 팔”이 E1 → E2 → E3를 돌며 중간체를 직접 넘김 = 기질 채널링', 11, C['navy'], weight=900)
    return svg(W, H, b)


def yield_bars():
    return bars([('NADH 3개 × 2.5', 7.5, C['blue'], '7.5 ATP'), ('FADH₂ 1개 × 1.5', 1.5, C['purple'], '1.5 ATP'), ('GTP 1개', 1.0, C['green'], '1 ATP'), ('합계 / 아세틸-CoA', 10, C['orange'], '≈ 10 ATP')],
                height=140, vmax=12, width=540)


def pdh_switch():
    W, H = 540, 150
    b = arrowdef('ps1', C['red']) + arrowdef('ps2', C['green'])
    b += f'<rect x="20" y="45" width="150" height="52" rx="12" fill="#f0fdf4" stroke="{C["green"]}" stroke-width="2"/>' + T(95, 67, 'PDH (E1–Ser–OH)', 11.5, C['green'], weight=900) + T(95, 85, '활성', 10.5, C['ink'])
    b += f'<rect x="370" y="45" width="150" height="52" rx="12" fill="#fef2f2" stroke="{C["red"]}" stroke-width="2"/>' + T(445, 67, 'PDH (E1–Ser–P)', 11.5, C['red'], weight=900) + T(445, 85, '불활성', 10.5, C['ink'])
    b += f'<path d="M172 55 Q 270 10 368 55" fill="none" stroke="{C["red"]}" stroke-width="2.2" marker-end="url(#ps1)"/>' + T(270, 22, 'PDH 키나아제 (ATP·아세틸-CoA·NADH ↑ 일 때)', 10.5, C['red'], weight=700)
    b += f'<path d="M368 88 Q 270 134 172 88" fill="none" stroke="{C["green"]}" stroke-width="2.2" marker-end="url(#ps2)"/>' + T(270, 140, 'PDH 포스파타아제 (Ca²⁺·인슐린, ATP ↓ 일 때)', 10.5, C['green'], weight=700)
    return svg(W, H, b)


def glyox():
    W, H = 560, 260
    b = arrowdef('gx', C['gray']) + arrowdef('gx2', C['red'])
    P = {'OAA': (280, 30), '시트르산': (460, 95), '아이소시트르산': (460, 185), '글리옥실산': (100, 185), '말산': (100, 95)}
    for k, (x, y) in P.items():
        b += f'<rect x="{x-56}" y="{y-14}" width="112" height="28" rx="14" fill="white" stroke="{C["navy"]}" stroke-width="1.8"/>' + T(x, y + 4, k, 11, C['navy'], weight=700)
    def ln(x1, y1, x2, y2, col=C['gray'], m='gx'):
        return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{col}" stroke-width="2.2" marker-end="url(#{m})"/>'
    b += ln(338, 38, 420, 78) + T(400, 48, '+ 아세틸-CoA ①', 10, C['orange'], 'start', 700)
    b += ln(460, 111, 460, 167) + T(468, 143, '아코니테이스', 10, C['orange'], 'start', 700)
    b += ln(402, 185, 160, 185, C['red'], 'gx2') + T(280, 176, '아이소시트르산 분해효소', 11, C['red'], weight=900)
    b += ln(280, 190, 280, 226, C['red'], 'gx2') + T(280, 246, '숙신산 (4C) → 미토콘드리아 → 포도당신생', 11, C['green'], weight=900)
    b += ln(100, 169, 100, 113, C['red'], 'gx2') + T(108, 138, '말산 생성효소', 11, C['red'], 'start', 900) + T(108, 153, '(+ 아세틸-CoA)', 10, C['orange'], 'start', 700)
    b += ln(158, 86, 222, 40) + T(176, 52, 'NADH', 10, C['orange'], 'end', 700)
    b += T(300, 120, '글리옥시솜', 13, C['gray'], weight=900)
    return svg(W, H, b)


def amphibolic():
    W, H = 580, 240
    b = arrowdef('am', C['blue']) + arrowdef('am2', C['red'])
    b += f'<circle cx="240" cy="125" r="78" fill="none" stroke="{C["light"]}" stroke-width="10"/>' + T(240, 129, '시트르산 회로', 11, C['gray'], weight=900)
    nodes = [('OAA', 240, 47, '아스파르트산 · 피리미딘 · 포도당', 40), ('시트르산', 312, 95, '지방산 · 스테롤', 92), ('α-KG', 312, 160, '글루탐산 · 퓨린', 162), ('숙시닐-CoA', 240, 203, '포르피린 · 헴', 214)]
    for k, x, y, lab, ty in nodes:
        b += f'<rect x="{x-46}" y="{y-13}" width="92" height="26" rx="13" fill="white" stroke="{C["navy"]}" stroke-width="1.8"/>' + T(x, y + 4, k, 10.5, C['navy'], weight=700)
        b += f'<line x1="{x+48}" y1="{y}" x2="{392}" y2="{ty}" stroke="{C["blue"]}" stroke-width="1.8" marker-end="url(#am)"/>'
        b += T(398, ty + 4, lab, 10.5, C['blue'], 'start', 700)
    b += f'<rect x="122" y="112" width="70" height="26" rx="13" fill="white" stroke="{C["navy"]}" stroke-width="1.8"/>' + T(157, 129, '말산', 10.5, C['navy'], weight=700)
    b += f'<line x1="14" y1="47" x2="190" y2="47" stroke="{C["red"]}" stroke-width="2.4" marker-end="url(#am2)"/>'
    b += T(96, 37, '피루브산 + CO₂ → OAA', 10.5, C['red'], weight=900) + T(96, 66, '(PC · 비오틴) = 보충 반응', 10, C['red'], weight=700)
    b += T(470, 236, '파랑 = 빠져나가는 생합성 / 빨강 = 채우는 보충 반응', 9.5, C['gray'])
    return svg(W, H, b)


# ------------------------------------------------------------------ summary pages
SUMMARY = []

SUMMARY.append(page('S1', '세포호흡 3단계와 탄소 추적', 'Stages of cellular respiration · Slides 3–5',
  '세포호흡 = ① 아세틸-CoA 만들기 → ② <b>시트르산 회로</b>에서 아세틸기를 CO₂로 태우며 전자를 NADH·FADH₂에 모으기 → ③ 전자전달·산화적 인산화로 ATP. 시트르산 회로 = 구연산 회로 = TCA 회로 = 크렙스 회로 (모두 같은 말).',
  f'''<div class="grid2"><div class="card"><h4>📌 탄소가 어디로 가나? (슬라이드 5)</h4><figure class="fig">{carbon_flow()}</figure>
 <p>포도당 1개 → 피루브산 2개 → 아세틸-CoA 2개 → 회로 <b>2바퀴</b>. 탄소 6개가 결국 CO₂ 6개(PDH 2 + 회로 4)로 나간다.</p></div>
<div><div class="card"><h4>📌 포도당 1분자 기준 수확 (슬라이드 5)</h4>{table(['구간', 'ATP(GTP)', 'NADH', 'FADH₂', 'CO₂'], [
  ['해당과정 (세포질)', '2', '2', '–', '–'], ['피루브산 → 아세틸-CoA (PDH)', '–', '2', '–', '2'], ['시트르산 회로 ×2', '2', '6', '2', '4'], ['<b>합계</b>', '<b>4</b>', '<b>10</b>', '<b>2</b>', '<b>6</b>']])}</div>
 {key('회로 자체는 ATP를 거의 안 만든다(1바퀴 GTP 1개). 진짜 일은 <b>전자를 NADH·FADH₂에 모으는 것</b> → 3단계에서 ATP로.')}
 {tip('2단계 회로와 3단계 전자전달 모두 <b>미토콘드리아</b>. 해당과정만 세포질.', '위치')}</div></div>''',
  ('P2', 'P29', 'P34')))

SUMMARY.append(page('S2', '16.1 피루브산 → 아세틸-CoA (PDH 복합체)', 'Pyruvate dehydrogenase complex · Slides 6–7, 12',
  '피루브산 탈수소효소(PDH) 복합체가 피루브산(3C)의 카복실기를 CO₂로 떼고, 남은 아세틸기(2C)를 CoA에 붙인다. 전자는 NAD⁺로 → NADH. 이것이 <b>산화적 탈카복실화</b>, 그리고 <b>비가역</b>.',
  f'''<div class="formula">피루브산 + CoA-SH + NAD⁺ → 아세틸-CoA + CO₂ + NADH &nbsp; (ΔG′° = −33.4 kJ/mol)</div>
<div class="grid2" style="margin-top:3mm"><div class="card"><h4>📌 세 효소가 한 몸 (슬라이드 7, 12)</h4><figure class="fig">{pdh_arm()}</figure></div>
<div><div class="card"><h4>📌 5단계 반응 (슬라이드 12)</h4>{table(['단계', '효소', '하는 일'], [
  ['①', 'E1 (TPP)', '피루브산 탈카복실화 → 히드록시에틸-TPP + CO₂'],
  ['②', 'E2 (리포산)', '히드록시에틸이 산화되어 아세틸기로 리포일 팔에 붙음'],
  ['③', 'E2 (CoA)', '아세틸기 → CoA-SH = <b>아세틸-CoA</b> 방출, 팔은 환원형(–SH HS–)'],
  ['④', 'E3 (FAD)', '환원된 리포일 팔을 다시 산화 → FADH₂'],
  ['⑤', 'E3 (NAD⁺)', 'FADH₂ → FAD, NAD⁺ → <b>NADH</b>']], cls='left')}</div>
 {warn('비가역 → 동물은 아세틸-CoA를 피루브산(→ 포도당)으로 되돌릴 수 없다. 그래서 <b>지방산 → 포도당 불가</b> (S14와 연결).', '중요')}
 {tip('리포일 도메인 수: 대장균 3, 포유류 2, 효모 1. E3는 α-KG 탈수소효소 복합체와 <b>같은 효소</b>.', '참고')}</div></div>''',
  ('P6', 'P32')))

SUMMARY.append(page('S3', 'PDH의 조효소 5개와 비타민', 'Coenzymes · Slides 8–11, 54',
  'PDH에는 조효소가 <b>5개</b> 필요하다: TPP · 리포산 · CoA · FAD · NAD⁺. 이 중 4개가 비타민 B에서 온다 → 비타민이 모자라면 회로가 막힌다.',
  f'''<div class="grid2"><div><div class="card"><h4>📌 조효소 · 비타민 · 운반물 (슬라이드 8)</h4>{table(['조효소', '비타민', '운반하는 것', '어디서'], [
  ['<b>TPP</b>', '티아민 (B₁)', '히드록시에틸기 (2C)', 'E1'], ['<b>리포산</b>', '(비타민 아님)', '아세틸기 + 전자', 'E2'], ['<b>CoA</b>', '판토텐산 (B₅)', '아세틸기(아실기)', 'E2'],
  ['<b>FAD</b>', '리보플래빈 (B₂)', '전자', 'E3'], ['<b>NAD⁺</b>', '나이아신 (B₃)', '전자 (하이드라이드)', 'E3']], cls='left')}
 <p class="small">외우기: “<b>T</b>hank <b>L</b>ovely <b>C</b>oenzymes <b>F</b>or <b>N</b>othing” = TPP · Lipoate · CoA · FAD · NAD.</p></div>
 {warn('티아민(B₁) 결핍 = <b>각기병</b>: PDH·α-KG DH가 멈춰 피루브산이 쌓인다. 포도당만 쓰는 뇌·신경이 먼저 망가진다 (풀이노트 문제 7·18).', '임상')}</div>
<div><div class="card"><h4>📌 CoA, TPP, 리포산의 핵심 부위 (슬라이드 9–11)</h4>{table(['조효소', '반응하는 곳', '포인트'], [
  ['CoA', '끝의 –SH (티올기)', '아세틸기와 <b>티오에스터</b>(고에너지)'], ['TPP', '티아졸 고리의 C2', '탈카복실화를 도움 (PDH, α-KG DH, 트랜스케톨레이스 등)'], ['리포산', 'S–S ↔ SH HS', 'E2의 <b>Lys</b>에 아미드 결합 = 리포일라이신 “긴 팔”']], cls='left')}</div>
 <div class="card" style="margin-top:3mm"><h4>긴 팔 3총사 (슬라이드 54)</h4>{table(['팔', '붙는 곳', '나르는 것'], [['리포산', 'E2의 Lys', '아세틸기'], ['비오틴', '피루브산 카복실화효소의 Lys', 'CO₂'], ['판토텐산(포스포판테테인)', 'ACP의 Ser', '아실기 (지방산 합성)']])}</div></div></div>''',
  ('P7', 'P11', 'P12', 'P18')))

SUMMARY.append(page('S4', '16.2 시트르산 회로 8단계 한눈에', 'Reactions of the cycle · Slides 13–19',
  '아세틸-CoA(2C) + 옥살로아세트산(OAA, 4C) → 시트르산(6C)으로 시작해서, CO₂ 2개를 내보내고 OAA로 돌아온다. 모든 반응은 <b>미토콘드리아 기질</b> (숙신산 탈수소효소만 내막).',
  f'''<div class="grid2"><div class="card"><figure class="fig">{tca_wheel(width=520, height=400)}</figure>
 <p class="small">외우기 (중간체 순서): <b>오 시 아 알 숙 숙 푸 말</b> — 옥살로아세트산 · 시트르산 · 아이소시트르산 · α-KG · 숙시닐-CoA · 숙신산 · 푸마르산 · 말산.</p></div>
<div><div class="card"><h4>📌 8단계 표</h4>{table(['#', '효소', 'ΔG′°', '반응 종류'], [[n, e, g, k] for n, _, e, g, k in TCA], cls='left')}</div>
 {key('탈수소효소 4개(③④⑥⑧) → NADH 3 + FADH₂ 1. CO₂는 ③④에서. GTP는 ⑤에서 딱 한 번.')}</div></div>''',
  ('P9',)))

SUMMARY.append(page('S5', '단계 ①② — 시트르산 생성효소와 아코니테이스', 'Slides 19–24',
  '① 아세틸-CoA의 메틸기가 OAA의 카보닐 탄소를 공격 (Claisen 축합). 티오에스터가 끊어지는 에너지 덕분에 ΔG′° = <b>−32.2</b>. ② 아코니테이스가 –OH 위치를 옮겨 산화될 수 있는 아이소시트르산으로.',
  f'''<div class="grid2"><div><div class="card"><h4>📌 ① 시트르산 생성효소 (슬라이드 20–21)</h4>{table(['단계', '일어나는 일'], [['1', 'Asp375가 아세틸-CoA의 메틸 H⁺를 떼어 <b>에놀레이트</b> (His274가 안정화)'], ['2', '에놀레이트가 OAA 카보닐 탄소 공격 → <b>시트로일-CoA</b> (His320 = 일반 산)'], ['3', '티오에스터 가수분해 → 시트르산 + CoA-SH (큰 에너지 방출)']], cls='left')}
 <p class="small">OAA가 먼저 결합해야 효소 모양이 바뀌어 아세틸-CoA 자리가 생긴다 (<b>유도 적합</b>) → 아세틸-CoA가 쓸데없이 가수분해되지 않음.</p></div>
 <div class="card" style="margin-top:3mm"><h4>📌 ② 아코니테이스 (슬라이드 22)</h4><p>시트르산 →(−H₂O)→ <i>cis</i>-아코니트산 →(+H₂O)→ 아이소시트르산. <b>Fe–S 중심</b>이 기질을 잡고 물을 뗐다 붙인다.</p>
 <p class="small">왜? 시트르산의 –OH는 3차 알코올이라 산화가 안 됨 → 2차 알코올(아이소시트르산)로 옮겨야 ③에서 산화 가능. ΔG′° = +13.3이지만 아이소시트르산이 바로 쓰여 진행.</p></div></div>
<div><div class="card"><h4>📌 아코니테이스는 “투잡” 효소 (슬라이드 23–24)</h4>{table(['', '철 많음', '철 부족'], [['세포질 아코니테이스', '아코니테이스 (Fe–S 있음)', '<b>IRP1</b>으로 변신 → mRNA의 IRE에 결합'], ['페리틴 (철 저장)', '합성 ↑', '번역 억제 ↓'], ['TfR (철 흡수 수용체)', '분해 ↑', 'mRNA 안정화 ↑'], ['결과', '철 저장', '철 흡수 ↑']])}
 <p class="small">몸의 철: 적혈구 65%, 간 20%(페리틴). 하루 흡수·손실은 1–2 mg뿐 → <b>재활용</b>이 핵심.</p></div>
 {tip('moonlighting = 본업 끝나고 밤에 하는 부업. 하나의 단백질이 두 가지 일을 한다.', '비유')}</div></div>''',
  ('P31',)))

SUMMARY.append(page('S6', '단계 ③④⑤ — 탈카복실화 두 번과 GTP', 'Slides 25–27',
  '③④에서 CO₂가 하나씩 빠져 6C → 5C → 4C. 둘 다 NADH를 만든다. ⑤에서 숙시닐-CoA의 티오에스터 에너지로 GTP를 직접 만든다 (<b>기질 수준 인산화</b>).',
  f'''<div class="grid3"><div class="card"><h4>③ 아이소시트르산 탈수소효소 (IDH)</h4><p>아이소시트르산 + NAD⁺ → 옥살로석신산(중간체) → <b>α-KG + CO₂ + NADH</b>. Mn²⁺가 탈카복실화를 도움.</p>
 <p class="small">동종효소: 미토콘드리아 = NAD⁺, 세포질·미토콘드리아 일부 = NADP⁺.</p>
 {warn('IDH 돌연변이(신경교종·AML) → α-KG를 <b>D-2-하이드록시글루타르산</b>(종양대사체)으로 바꿈.', '암')}</div>
<div class="card"><h4>④ α-KG 탈수소효소 복합체</h4><p>α-KG + CoA + NAD⁺ → <b>숙시닐-CoA + CO₂ + NADH</b> (ΔG′° = −33.5)</p>{table(['', 'PDH', 'α-KG DH'], [['기질', '피루브산 3C', 'α-KG 5C'], ['산물', '아세틸-CoA', '숙시닐-CoA'], ['조효소', 'TPP·리포산·CoA·FAD·NAD⁺', '같음'], ['E3', '같은 효소', '같은 효소']])}</div>
<div class="card"><h4>⑤ 숙시닐-CoA 합성효소</h4><p>숙시닐-CoA + GDP + Pᵢ ⇌ 숙신산 + CoA + <b>GTP</b> (ΔG′° = −2.9)</p>
 <p class="small">기전: Pᵢ가 공격 → 숙시닐 인산 → 효소의 <b>His</b>로 인산 이동(포스포히스티딘) → GDP에 전달.</p>
 <p class="small">GTP + ADP ⇌ GDP + ATP (뉴클레오사이드 이인산 키나아제) → ATP와 같은 가치.</p>
 {key('회로에서 ATP(GTP)가 직접 나오는 곳은 ⑤ 하나뿐.')}</div></div>
{tip('“synthetase” 이름은 역반응(NTP를 써서 숙시닐-CoA 합성)에서 붙었다. 함정 주의: 정방향은 GTP를 <b>만든다</b>.', '이름')}
{warn('이번 바퀴에 나간 CO₂ 2개의 탄소는 방금 들어온 아세틸기 탄소가 <b>아니라</b> OAA 유래 탄소. 양만 같다.', '함정')}''',
  ('P8', 'P14')))

SUMMARY.append(page('S7', '단계 ⑥⑦⑧ — OAA 재생', 'Slides 28–30',
  '숙신산 → 푸마르산 → 말산 → OAA. 탈수소(FAD) → 수화 → 탈수소(NAD⁺)의 3단계로 다시 OAA를 만든다. ⑧은 ΔG′° <b>+29.7</b>로 불리하지만 OAA가 즉시 ①에서 쓰여 계속 진행된다.',
  f'''<div class="grid3"><div class="card"><h4>⑥ 숙신산 탈수소효소 (SDH)</h4><p>숙신산 + FAD → 푸마르산 + <b>FADH₂</b> (ΔG′° ≈ 0)</p>
 <p class="small">미토콘드리아 <b>내막</b>에 박혀 있음 = 전자전달계 복합체 II. 회로 효소 중 유일하게 막에 있음.</p>
 <p class="small">왜 FAD? C–C → C=C 산화는 에너지가 작아 NAD⁺를 환원하기 부족.</p>
 {warn('<b>말론산</b>(⁻OOC–CH₂–COO⁻)은 숙신산과 닮은 <b>경쟁적 억제제</b>: Km ↑, Vmax 그대로. 숙신산을 많이 넣으면 극복.', '시험')}</div>
<div class="card"><h4>⑦ 푸마레이스</h4><p>푸마르산 + H₂O → <b>L-말산</b> (ΔG′° = −3.8)</p>{table(['', '푸마레이스가?'], [['푸마르산 (trans)', '○'], ['말레산 (cis)', '✕'], ['L-말산', '○ (역반응)'], ['D-말산', '✕']])}
 <p class="small">입체특이성이 매우 높다.</p></div>
<div class="card"><h4>⑧ 말산 탈수소효소</h4><p>L-말산 + NAD⁺ ⇌ OAA + <b>NADH</b> + H⁺ (ΔG′° = <b>+29.7</b>)</p>
 <p class="small">세포 속 [OAA]가 아주 낮고(&lt; 1 μM), ①(−32.2)이 OAA를 바로 끌어가서 실제 ΔG는 0 근처 → 진행.</p>
 {key('⑧ + ① 짝꿍: 불리한 반응을 뒤의 유리한 반응이 끌어당긴다.')}</div></div>
<div class="card" style="margin-top:3mm"><h4>ΔG′° 한 줄 정리 (kJ/mol)</h4>{table(['①', '②', '③', '④', '⑤', '⑥', '⑦', '⑧'], [['−32.2', '+13.3', '−20.9', '−33.5', '−2.9', '0', '−3.8', '+29.7']])}
 <p class="small">크게 음수인 ①③④ = 조절되는 3개의 발에르곤 반응 (S11–S12).</p></div>''',
  ('P9', 'P10', 'P15')))

SUMMARY.append(page('S8', '한 바퀴의 수확 — 아세틸-CoA 1개 ≈ 10 ATP', 'Overall outcome · Slide 18',
  '회로 1바퀴: 아세틸기 2C가 들어와 CO₂ 2개가 나가고, <b>NADH 3 + FADH₂ 1 + GTP 1</b>이 생긴다. 산화적 인산화까지 가면 약 <b>10 ATP</b>.',
  f'''<div class="formula">아세틸-CoA + 3NAD⁺ + FAD + GDP + Pᵢ + 2H₂O → 2CO₂ + 3NADH + FADH₂ + GTP + 2H⁺ + CoA</div>
<div class="grid2" style="margin-top:3mm"><div class="card"><h4>📌 ATP 환산 (슬라이드 18)</h4><figure class="fig">{yield_bars()}</figure>
 <p class="small">NADH 1 ≈ 2.5 ATP, FADH₂ 1 ≈ 1.5 ATP (19장 산화적 인산화).</p></div>
<div><div class="card"><h4>📌 포도당 1분자 전체 계산</h4>{table(['구간', '직접', 'NADH', 'FADH₂', 'ATP 환산'], [
  ['해당과정', '2 ATP', '2', '', '2 + 5 = 7 *'], ['PDH ×2', '', '2', '', '5'], ['회로 ×2', '2 GTP', '6', '2', '2 + 15 + 3 = 20'], ['<b>합계</b>', '', '', '', '<b>≈ 32</b>']])}
 <p class="small">* 세포질 NADH는 셔틀 종류에 따라 1.5 또는 2.5 → 총 30–32 ATP.</p></div>
 {key('회로 = 산소를 직접 쓰지 않지만, NADH·FADH₂를 다시 산화하려면 O₂가 필요 → <b>산소 없으면 회로도 멈춘다</b> (풀이노트 문제 29).')}</div></div>''',
  ('P14', 'P2', 'P29')))

SUMMARY.append(page('S9', '양방향성 경로와 보충 반응', 'Amphibolic · anaplerotic · Slides 31–32, 53',
  '회로는 분해(이화)뿐 아니라 합성(동화) 재료도 내준다 = <b>양방향성(amphibolic)</b>. 중간체가 빠져나가면 OAA가 모자라 회로가 멈추므로, 다시 채워 넣는 <b>보충 반응(anaplerotic)</b>이 필요하다.',
  f'''<div class="grid2"><div class="card"><h4>📌 빠져나가는 곳 · 채우는 곳 (슬라이드 32)</h4><figure class="fig">{amphibolic()}</figure></div>
<div><div class="card"><h4>📌 보충 반응 (빨간 화살표)</h4>{table(['반응', '효소', '어디'], [
  ['피루브산 + HCO₃⁻ + ATP → <b>OAA</b>', '<b>피루브산 카복실화효소</b> (비오틴)', '동물 간·신장 (가장 중요)'],
  ['PEP + CO₂ ⇌ OAA', 'PEP 카복시키나아제 / PEP 카복실화효소', '심장·근육 / 식물·세균'],
  ['피루브산 + HCO₃⁻ + NAD(P)H → 말산', '말산 효소', '여러 조직']], cls='left')}
 <p class="small">피루브산 카복실화효소는 <b>아세틸-CoA</b>가 알로스테릭 활성화 → 아세틸-CoA가 쌓이면(OAA 부족) 자동으로 OAA를 채운다.</p></div>
 <div class="card" style="margin-top:3mm"><h4>비오틴이 CO₂를 나른다 (슬라이드 53)</h4><p class="small">HCO₃⁻ + ATP → 카복시인산 → CO₂ → <b>카복시비오틴</b> → 비오틴 팔이 다른 활성 자리로 이동 → 피루브산 에놀레이트에 CO₂ 전달 → OAA.</p></div>
 {warn('회로만으로는 OAA가 <b>순증가하지 않는다</b> (아세틸 2C 들어오면 CO₂ 2개 나감). 그래서 보충 반응이 꼭 필요 (풀이노트 문제 19·20).', '시험')}</div></div>''',
  ('P13', 'P19', 'P20', 'P23', 'P24', 'P28')))

SUMMARY.append(page('S10', '16.3 조절 — 어디서, 어느 지점에서?', 'Where & control points · Slides 35–38',
  '회로는 미토콘드리아 기질에서. 조절 지점은 <b>PDH 단계 + 크게 발에르곤인 3단계(①③④)</b>. 공통 원리: <b>연료·산물이 넘치면 끄고, 수요 신호가 오면 켠다</b>.',
  f'''<div class="grid2"><div class="card"><h4>📌 미토콘드리아의 문 (슬라이드 36)</h4>{table(['구성', '하는 일'], [['<b>MPC</b> (MPC1/2)', '세포질 피루브산 → 기질로 들여옴'], ['PDH → TCA', '아세틸-CoA → NADH·FADH₂'], ['OXPHOS 복합체 I–IV + ATP 합성효소', 'H⁺ 기울기로 ATP 생성'], ['<b>ANT</b>', 'ATP를 세포질로 내보내고 ADP를 들여옴']], cls='left')}
 <p class="small">미토콘드리아 리보솜이 OXPHOS 단백질 일부를 직접 합성한다.</p></div>
<div><div class="card"><h4>📌 조절 지점 4곳 (슬라이드 37–38)</h4><figure class="fig">{tca_wheel(hl=('시트르산', 'α-케토글루타르산', '숙시닐-CoA'), width=520, height=300)}</figure>
 <p class="small">주황 = 조절되는 단계(①③④)의 산물.</p>{table(['#', '조절 지점', '왜?'], [['0', 'PDH 복합체', '비가역 · 회로 입구'], ['①', '시트르산 생성효소', 'ΔG′° −32.2'], ['③', 'IDH', 'ΔG′° −20.9'], ['④', 'α-KG DH', 'ΔG′° −33.5']])}</div></div></div>''',
  ('P33', 'P25')))

SUMMARY.append(page('S11', 'PDH의 조절 — 알로스테릭 + 인산화', 'Slides 39–40',
  'PDH는 <b>산물·에너지(ATP, 아세틸-CoA, NADH, 지방산)</b>로 억제, <b>수요 신호(AMP, CoA, NAD⁺, Ca²⁺)</b>로 활성화. 또 E1이 <b>인산화되면 꺼진다</b>.',
  f'''<div class="grid2"><div class="card"><h4>📌 알로스테릭 조절 (슬라이드 39)</h4>{table(['', '물질', '의미'], [['⊗ 억제', 'ATP, 아세틸-CoA, NADH, 지방산', '“연료(fuels)” 충분'], ['▲ 활성', 'AMP, CoA, NAD⁺, Ca²⁺', '“수요(demands)” 큼']])}
 {key('산물(아세틸-CoA·NADH)이 쌓이면 억제, 기질(CoA·NAD⁺)이 많으면 활성 → 질량작용과 같은 논리.')}
 {tip('지방산이 PDH를 억제 → 지방을 태우는 공복 때는 피루브산을 아껴 포도당신생으로 (15장 S5와 연결).', '연결')}</div>
<div><div class="card"><h4>📌 공유결합 조절: E1의 Ser 인산화 (슬라이드 40)</h4><figure class="fig">{pdh_switch()}</figure>
 <p>[ATP] 높음 → <b>키나아제</b>가 E1 Ser 인산화 → PDH <b>OFF</b> / [ATP] 낮음 → <b>포스파타아제</b>가 인산 제거 → PDH <b>ON</b>.</p></div>
 {warn('글리코겐 인산화효소(인산화 = ON)와 반대. PDH는 <b>인산화 = OFF</b>.', '함정')}</div></div>''',
  ('P25', 'P30')))

SUMMARY.append(page('S12', '세 효소의 조절과 Ca²⁺', 'Slides 41–43 · ’22 약사국시',
  '시트르산 생성효소 · IDH · α-KG DH 모두 <b>고에너지(ATP, NADH)와 산물</b>로 억제, <b>ADP · Ca²⁺</b>로 활성화된다.',
  f'''<div class="grid2"><div><div class="card"><h4>📌 조절 물질 표 (’22 약시 출제)</h4>{table(['효소', '⊗ 억제', '▲ 활성'], [
  ['<b>시트르산 생성효소</b> ①', 'NADH, 숙시닐-CoA, 시트르산, ATP', 'ADP'], ['<b>IDH</b> ③', 'ATP', 'Ca²⁺, ADP'], ['<b>α-KG DH</b> ④', '숙시닐-CoA, NADH', 'Ca²⁺']], cls='left')}
 <p class="small">시트르산 생성효소는 기질(아세틸-CoA, OAA)이 얼마나 있느냐에 따라서도 속도가 제한된다.</p></div>
 <div class="card" style="margin-top:3mm"><h4>📌 회로를 움직이는 4가지 비율 (슬라이드 43)</h4>{table(['비율', '높으면'], [['[ADP]/[ATP]', '회로 ↑'], ['[NAD⁺]/[NADH]', '회로 ↑'], ['[기질]/[산물]', '회로 ↑'], ['[수요]/[연료]', '회로 ↑']])}</div></div>
<div><div class="card"><h4>숙시닐-CoA = 시트르산 생성효소의 알로스테릭 억제제 (풀이노트 문제 27)</h4><figure class="fig">{img('c16_p27.png', '62%')}</figure>
 <p class="small">S자 곡선 = 알로스테릭 효소. 숙시닐-CoA를 넣으면 곡선이 오른쪽으로(K<sub>0.5</sub> ↑) → 같은 속도에 아세틸-CoA가 더 필요 = 되먹임 억제.</p></div>
 <div class="card" style="margin-top:3mm"><h4>왜 Ca²⁺? (슬라이드 43)</h4><p>근육 수축·호르몬 자극 → 세포질 Ca²⁺ ↑ = “곧 ATP가 많이 필요하다”는 신호 → <b>PDH(포스파타아제 경유) · IDH · α-KG DH</b> 활성 → NADH 공급 ↑.</p></div></div></div>''',
  ('P27', 'P30')))

SUMMARY.append(page('S13', '기질 채널링 — 효소들이 손을 잡는다', 'Substrate channeling · Slides 44–45',
  '회로 효소들은 물에 녹는 단백질이지만, 미토콘드리아 안에서는 <b>다효소 복합체</b>로 모여 중간체를 바로 옆 효소에 넘긴다 = <b>기질 채널링</b>.',
  f'''<div class="grid2"><div class="card"><h4>📌 채널링의 장점 (슬라이드 44)</h4><ul><li>경로가 <b>빠르고 효율적</b> (중간체가 멀리 퍼지지 않음)</li><li><b>불안정한 중간체</b>가 새어 나가지 않음</li><li>중간체를 다른 경로와 덜 다툼</li></ul>
 {flow(['시트르산 생성효소', '아코니테이스', 'IDH'], arrow_labels=['시트르산 직접 전달', '아이소시트르산 직접'], width=500, colors=[C['blue'], C['green'], C['orange']], box_h=40)}
 <p class="small">PDH의 리포일 팔(S2)도 같은 아이디어를 한 단백질 안에서 구현한 것.</p></div>
<div><div class="card"><h4>📌 빽빽해야 붙어 있다 (슬라이드 45)</h4>{table(['', '세포 속 (특히 미토콘드리아)', '세포를 깨면'], [['단백질 농도', '아주 높음 (crowding)', '수십~수백 배 희석'], ['효소 복합체', '유지 (높은 농도 = 결합 유리)', '흩어짐'], ['채널링', '○', '✕']])}</div>
 {warn('시험관(희석된 추출액)에서 잰 효소 성질이 세포 속과 다를 수 있다 — 약한 복합체는 정제 중에 깨진다.', '포인트')}</div></div>''',
  ()))

SUMMARY.append(page('S14', '16.4 글리옥실산 회로 — 지방으로 포도당 만들기', 'Glyoxylate cycle · Slides 46–51',
  '식물 종자·일부 미생물은 회로에서 CO₂를 잃는 두 단계(③④)를 <b>건너뛰어</b> 아세틸-CoA 2개로 숙신산(4C) 1개를 순수하게 만든다 → 포도당신생 가능. 핵심 효소: <b>아이소시트르산 분해효소</b> + <b>말산 생성효소</b>.',
  f'''<div class="grid2"><div class="card"><h4>📌 회로 그림 (슬라이드 47–48)</h4><figure class="fig">{glyox()}</figure></div>
<div><div class="card"><h4>📌 Input · Outcome · TCA와 차이 (슬라이드 47)</h4>{table(['질문', '답'], [['입력', '아세틸-CoA <b>2개</b> (①과 말산 생성효소에서 하나씩)'], ['결과', '<b>숙신산 1개</b> (+ NADH 1), CO₂ 방출 없음'], ['TCA와 차이', '③④(탈카복실화 2번)를 건너뜀 → 탄소 손실 없음']], cls='left')}</div>
 <div class="card" style="margin-top:3mm"><h4>📌 세포 속 경로 (슬라이드 49)</h4>{flow(['지방체|TAG → 지방산', '글리옥시솜|아세틸-CoA → 숙신산', '미토콘드리아|숙신산 → 말산', '세포질|말산 → 포도당'], width=520, box_h=42, gap=18, font=9.5, colors=[C['gray'], C['green'], C['blue'], C['orange']])}</div>
 <div class="card" style="margin-top:3mm"><h4>📌 분기점 = 아이소시트르산 (슬라이드 51)</h4><p class="small">IDH가 <b>인산화되면 OFF</b> → 아이소시트르산이 글리옥실산 회로로 / 탈인산화되면 ON → TCA로. 중간체 낮으면 글리옥실산 회로, 높으면 TCA.</p></div>
 {warn('<b>척추동물은 지방산 → 포도당 불가</b>: 글리옥실산 회로 효소가 없고 PDH가 비가역이라 아세틸-CoA 2C는 CO₂ 2개로 다 나간다. (단, 글리세롤 부분은 포도당이 될 수 있다.)', '시험')}</div></div>''',
  ()))

SUMMARY.append(page('S15', '16장 한 장 요약 + 시험 직전 체크리스트', 'Summary · Slides 33, 52',
  '두 개의 요약 슬라이드를 숫자·효소 이름과 함께 한 장으로. (약어는 바로 뒤 총정리 참고)',
  f'''<div class="grid3">
 <div class="card"><h4>① PDH (16.1)</h4><ul style="font-size:.95em"><li>피루브산 → 아세틸-CoA + CO₂ + NADH, 비가역</li><li>E1(TPP) · E2(리포산, CoA) · E3(FAD, NAD⁺)</li><li>조효소 5개: B₁ · 리포산 · B₅ · B₂ · B₃</li><li>리포일 팔 = 기질 채널링</li><li>B₁ 결핍 = 각기병</li></ul></div>
 <div class="card"><h4>② 회로 (16.2)</h4><ul style="font-size:.95em"><li>오 시 아 알 숙 숙 푸 말</li><li>③④ 산화적 탈카복실화 → CO₂ 2</li><li>⑤ 기질 수준 인산화 → GTP</li><li>⑥ SDH = 복합체 II, FADH₂, 말론산 경쟁적 억제</li><li>⑧ +29.7이지만 ①이 끌어감</li><li>1바퀴 ≈ 10 ATP</li><li>양방향성 → 보충 반응 (PC, 비오틴, 아세틸-CoA가 활성화)</li></ul></div>
 <div class="card"><h4>③ 조절 · 글리옥실산 (16.3–4)</h4><ul style="font-size:.95em"><li>조절: PDH + ①③④</li><li>억제: ATP, NADH, 아세틸-CoA, 숙시닐-CoA, 시트르산</li><li>활성: ADP, AMP, NAD⁺, CoA, Ca²⁺</li><li>PDH: E1 인산화 = OFF</li><li>Ca²⁺ → PDH · IDH · α-KG DH</li><li>글리옥실산 회로: 아이소시트르산 분해효소 + 말산 생성효소</li><li>동물: 지방산 → 포도당 ✕</li></ul></div>
</div>
<div class="grid2" style="margin-top:3mm"><div class="card"><h4>🔢 꼭 외울 숫자</h4><div class="tiles" style="grid-template-columns:repeat(3,1fr)">
 <div><b>1바퀴</b><span>3 · 1 · 1</span><small>NADH · FADH₂ · GTP</small></div><div><b>CO₂</b><span>2</span><small>③ · ④에서</small></div><div><b>ATP 환산</b><span>≈ 10</span><small>아세틸-CoA 1개</small></div>
 <div><b>① ΔG′°</b><span>−32.2</span><small>kJ/mol</small></div><div><b>⑧ ΔG′°</b><span>+29.7</span><small>kJ/mol</small></div><div><b>조효소</b><span>5</span><small>PDH · α-KG DH</small></div></div></div>
 <div class="card"><h4>⚠️ 단골 함정</h4><ol style="margin:.2em 0;padding-left:1.3em;font-size:.95em"><li>CO₂로 나가는 탄소 ≠ 방금 들어온 아세틸 탄소</li><li>회로만으로 OAA 순증가 ✕</li><li>PDH 인산화 = OFF (글리코겐 인산화효소와 반대)</li><li>SDH만 내막 (복합체 II)</li><li>숙시닐-CoA “합성효소”인데 정방향은 GTP 생성</li><li>회로는 O₂를 직접 안 쓰지만 O₂ 없으면 멈춤</li></ol></div></div>''',
  ()))

MAPROWS = [['S1–S3 PDH · 조효소', '문제 2·6·7·11·12·18·29·32·34'], ['S4–S8 회로 반응 · 수확', '문제 8·9·10·14·15·31'], ['S9 양방향성 · 보충 반응', '문제 13·19·20·22·23·24·28'], ['S10–S12 조절', '문제 25·27·30·33']]

# ------------------------------------------------------------------ glossary
GLOSS = [
 ('TCA', 'TriCarboxylic Acid cycle', '시트르산 회로 (구연산·크렙스 회로)', '아세틸-CoA를 CO₂로 태우는 회로'),
 ('CoA (CoA-SH)', 'Coenzyme A', '조효소 A', 'B₅ 유래, –SH로 아실기를 티오에스터로 운반'),
 ('Acetyl-CoA', 'Acetyl Coenzyme A', '아세틸-CoA', '회로의 연료 (2C)'),
 ('PDH', 'Pyruvate Dehydrogenase (complex)', '피루브산 탈수소효소 (복합체)', '피루브산 → 아세틸-CoA, 비가역'),
 ('E1 · E2 · E3', 'Enzymes 1 · 2 · 3 of the PDH complex', '탈수소효소 · 아세틸전달효소 · 다이하이드로리포일 탈수소효소', 'TPP / 리포산·CoA / FAD·NAD⁺'),
 ('TPP', 'Thiamine Pyrophosphate', '티아민 피로인산', 'B₁ 유래, 탈카복실화 조효소'),
 ('Lipoate', 'lipoic acid', '리포산', 'E2의 Lys에 붙은 긴 팔, 아세틸기·전자 운반'),
 ('FAD · FADH₂', 'Flavin Adenine Dinucleotide', '플라빈 아데닌 다이뉴클레오타이드', 'B₂ 유래 전자 운반체 (1 FADH₂ ≈ 1.5 ATP)'),
 ('NAD⁺ · NADH', 'Nicotinamide Adenine Dinucleotide', '니코틴아마이드 아데닌 다이뉴클레오타이드', 'B₃ 유래 전자 운반체 (1 NADH ≈ 2.5 ATP)'),
 ('NADP⁺', 'NAD Phosphate', 'NAD 인산', '일부 IDH 동종효소의 전자 수용체'),
 ('B₁ · B₂ · B₃ · B₅', 'Vitamin B1 · B2 · B3 · B5', '티아민 · 리보플래빈 · 나이아신 · 판토텐산', 'TPP · FAD · NAD · CoA의 재료'),
 ('OAA', 'Oxaloacetate', '옥살로아세트산', '회로의 시작·끝 (4C)'),
 ('α-KG', 'α-Ketoglutarate', 'α-케토글루타르산', '5C, 글루탐산의 재료'),
 ('IDH', 'Isocitrate Dehydrogenase', '아이소시트르산 탈수소효소', '③ CO₂ + NADH, 조절 효소'),
 ('α-KG DH (KDH)', 'α-Ketoglutarate Dehydrogenase complex', 'α-KG 탈수소효소 복합체', '④ PDH와 같은 방식, 조절 효소'),
 ('SDH', 'Succinate Dehydrogenase', '숙신산 탈수소효소', '⑥ FADH₂, 내막 = 복합체 II'),
 ('MDH', 'Malate Dehydrogenase', '말산 탈수소효소', '⑧ ΔG′° +29.7'),
 ('GTP · GDP', 'Guanosine Tri-/Diphosphate', '구아노신 삼·이인산', '⑤에서 생성, ATP와 같은 가치'),
 ('ATP · ADP · AMP', 'Adenosine Tri-/Di-/Monophosphate', '아데노신 삼·이·일인산', 'ADP·AMP ↑ = 회로 켜라'),
 ('Pᵢ', 'inorganic phosphate', '무기 인산', '⑤ 기질 수준 인산화에 사용'),
 ('ΔG′°', 'standard free-energy change', '표준 자유 에너지 변화', '음수 클수록 한 방향 (조절 지점)'),
 ('Fe–S', 'iron–sulfur center', '철–황 중심', '아코니테이스가 기질을 잡는 곳'),
 ('IRP1 · IRE', 'Iron Regulatory Protein 1 · Iron Response Element', '철 조절 단백질 · 철 반응 요소', '철 부족 시 아코니테이스가 변신해 mRNA 결합'),
 ('TfR', 'Transferrin Receptor', '트랜스페린 수용체', '철 흡수 통로, 철 부족 시 ↑'),
 ('D-2HG', 'D-2-Hydroxyglutarate', 'D-2-하이드록시글루타르산', '돌연변이 IDH가 만드는 종양대사체'),
 ('AML', 'Acute Myeloid Leukemia', '급성 골수성 백혈병', 'IDH 돌연변이가 흔한 암'),
 ('PC', 'Pyruvate Carboxylase', '피루브산 카복실화효소', '피루브산 → OAA, 비오틴, 아세틸-CoA가 켬'),
 ('PEP · PEPCK', 'Phosphoenolpyruvate · PEP Carboxykinase', 'PEP · PEP 카복시키나아제', 'PEP ⇌ OAA 보충 반응'),
 ('HCO₃⁻', 'bicarbonate', '중탄산 이온', 'PC가 쓰는 CO₂의 형태'),
 ('MPC', 'Mitochondrial Pyruvate Carrier', '미토콘드리아 피루브산 수송체', '피루브산을 기질로 들여옴'),
 ('ANT', 'Adenine Nucleotide Translocase', '아데닌 뉴클레오타이드 전위효소', 'ATP 내보내고 ADP 들여옴'),
 ('OXPHOS', 'Oxidative Phosphorylation', '산화적 인산화', 'NADH·FADH₂의 전자로 ATP 생성'),
 ('ACP', 'Acyl Carrier Protein', '아실 운반 단백질', '판토텐산 팔로 지방산 합성 중간체 운반'),
 ('Km · Vmax', 'Michaelis constant · maximum velocity', '미카엘리스 상수 · 최대 속도', '경쟁적 억제: Km ↑, Vmax 그대로'),
 ('TAG', 'Triacylglycerol', '트라이아실글리세롤', '저장 지방 → 지방산'),
]
ABBR_KEYS = {
 'TCA': r'\bTCA\b', 'CoA (CoA-SH)': r'CoA', 'Acetyl-CoA': r'아세틸-CoA', 'PDH': r'\bPDH\b', 'E1 · E2 · E3': r'\bE[123]\b', 'TPP': r'\bTPP\b', 'Lipoate': r'리포산|리포일',
 'FAD · FADH₂': r'\bFAD', 'NAD⁺ · NADH': r'\bNAD(?!P)', 'NADP⁺': r'NADP', 'B₁ · B₂ · B₃ · B₅': r'B[₁₂₃₅]', 'OAA': r'\bOAA\b', 'α-KG': r'α-KG', 'IDH': r'\bIDH\b',
 'α-KG DH (KDH)': r'α-KG DH|KDH', 'SDH': r'\bSDH\b', 'MDH': r'\bMDH\b', 'GTP · GDP': r'\bG[TD]P\b', 'ATP · ADP · AMP': r'\b(ATP|ADP|AMP)\b', 'Pᵢ': r'P[ᵢi]\b|Pᵢ',
 'ΔG′°': r'ΔG', 'Fe–S': r'Fe–S', 'IRP1 · IRE': r'IRP|IRE\b', 'TfR': r'TfR', 'D-2HG': r'하이드록시글루타르산', 'AML': r'\bAML\b', 'PC': r'\bPC\b|피루브산 카복실화효소',
 'PEP · PEPCK': r'\bPEP', 'HCO₃⁻': r'HCO', 'MPC': r'\bMPC\b', 'ANT': r'\bANT\b', 'OXPHOS': r'OXPHOS', 'ACP': r'\bACP\b', 'Km · Vmax': r'\bKm\b|Vmax', 'TAG': r'\bTAG\b',
}

# ------------------------------------------------------------------ concept checks
CHECKS = [
 dict(id='C1', num='1', title='PDH 복합체와 조효소', sec='S1–S3', level=1,
  q='''<p><b>1.</b> (빈칸) 피루브산 + CoA + NAD⁺ → ( &nbsp;&nbsp;&nbsp; ) + ( &nbsp; ) + ( &nbsp;&nbsp; ). 이 반응을 ( &nbsp;&nbsp;&nbsp;&nbsp; ) 탈카복실화라 하며 ( 가역 / 비가역 )이다.</p>
<p><b>2.</b> (짝짓기) TPP · 리포산 · CoA · FAD · NAD⁺ 를 E1 / E2 / E3에 배정하고, 비타민이 무엇인지 써라.</p>
<p><b>3.</b> (O/X) α-KG 탈수소효소 복합체는 PDH와 같은 조효소 5개를 쓰고, E3는 같은 효소이다.</p>
<p><b>4.</b> (서술) 티아민(B₁)이 부족하면 혈중 피루브산은 어떻게 되며, 왜 신경계가 먼저 손상되는가?</p>''',
  answer=chips('1. <b>아세틸-CoA · CO₂ · NADH</b> / <b>산화적</b> / <b>비가역</b>', '2. E1 = TPP(B₁) · E2 = 리포산, CoA(B₅) · E3 = FAD(B₂), NAD⁺(B₃)', '3. <b>O</b>', '4. 피루브산 <b>↑</b> — 뇌는 포도당 산화에 의존'),
  explain=fig(pdh_arm(), '') + steps('1. 카복실기가 CO₂로 빠지고(탈카복실화) 전자는 NAD⁺로(산화). ΔG′° −33.4로 비가역.',
   '2. 순서대로 “TPP → 리포산 → CoA → FAD → NAD⁺”가 E1 → E2 → E3를 따라 흐른다.',
   '4. TPP가 없으면 PDH(와 α-KG DH)가 멈춤 → 피루브산이 쌓이고 ATP 생산 ↓ → 포도당 의존도가 높은 뇌·신경이 먼저 타격 (각기병, 베르니케 뇌병증).') +
   tip('“T-L-C-F-N” 순서 = 반응이 일어나는 순서.', '요령')),
 dict(id='C2', num='2', title='회로 8단계 순서와 탄소', sec='S4', level=1,
  q='''<p><b>1.</b> (순서) 옥살로아세트산 → ( &nbsp; ) → 아이소시트르산 → ( &nbsp; ) → 숙시닐-CoA → ( &nbsp; ) → 푸마르산 → ( &nbsp; ) → 옥살로아세트산</p>
<p><b>2.</b> (빈칸) NADH를 만드는 단계: ( &nbsp; ), ( &nbsp; ), ( &nbsp; ) / FADH₂: ( &nbsp; ) / GTP: ( &nbsp; ) / CO₂: ( &nbsp; ), ( &nbsp; ) (단계 번호로)</p>
<p><b>3.</b> (O/X) 회로 효소는 모두 미토콘드리아 기질에 녹아 있다.</p>
<p><b>4.</b> (계산) 회로 중간체의 탄소 수: 시트르산 ( ), α-KG ( ), 숙시닐-CoA ( ), OAA ( )</p>''',
  answer=chips('1. <b>시트르산 · α-KG · 숙신산 · 말산</b>', '2. NADH ③④⑧ · FADH₂ ⑥ · GTP ⑤ · CO₂ ③④', '3. <b>X</b> (SDH는 내막)', '4. 6 · 5 · 4 · 4'),
  explain=fig(tca_wheel(width=520, height=300), '') + steps('2. 탈수소효소 4개 = ③ IDH, ④ α-KG DH, ⑥ SDH, ⑧ MDH. 이 중 ⑥만 FAD.',
   '3. SDH는 전자전달계 복합체 II로 내막에 박혀 있다.', '4. 6C → (CO₂) → 5C → (CO₂) → 4C 그대로 OAA까지.') +
   key('“오 시 아 알 숙 숙 푸 말”')),
 dict(id='C3', num='3', title='개별 단계의 특징', sec='S5–S7', level=2,
  q='''<p><b>1.</b> (O/X) 아코니테이스가 시트르산을 아이소시트르산으로 바꾸는 이유는 3차 알코올을 산화 가능한 2차 알코올로 바꾸기 위해서다.</p>
<p><b>2.</b> (빈칸) 말론산은 ( &nbsp;&nbsp;&nbsp; )의 ( 경쟁적 / 비경쟁적 ) 억제제로, Km은 ( ↑/↓/그대로 ), Vmax는 ( ↑/↓/그대로 )이다.</p>
<p><b>3.</b> (O/X) 푸마레이스는 말레산(cis)과 D-말산에도 작용한다.</p>
<p><b>4.</b> (서술) 말산 탈수소효소 반응은 ΔG′° = +29.7 kJ/mol인데 세포에서 어떻게 정방향으로 진행되나?</p>
<p><b>5.</b> (빈칸) 철이 부족하면 세포질 아코니테이스는 ( &nbsp;&nbsp; )이 되어 페리틴 합성은 ( ↑/↓ ), TfR은 ( ↑/↓ ).</p>''',
  answer=chips('1. <b>O</b>', '2. <b>숙신산 탈수소효소</b> / 경쟁적 / Km ↑ / Vmax 그대로', '3. <b>X</b> (trans·L형만)', '4. [OAA]가 매우 낮고 ①이 즉시 소모 → 실제 ΔG ≈ 0 이하', '5. <b>IRP1</b> / ↓ / ↑'),
  explain=steps('2. 말론산은 숙신산과 닮아 활성 자리에 붙지만 CH₂–CH₂가 없어 반응 못 함. 숙신산을 늘리면 극복 → 경쟁적.',
   '4. ΔG = ΔG′° + RT ln Q. 산물(OAA)이 거의 없으면 Q가 아주 작아 ΔG가 음수로 내려간다.',
   '5. 철 부족 → 철 저장(페리틴) 줄이고 흡수(TfR) 늘림.') +
   warn('숙시닐-CoA “합성효소”지만 회로 방향에서는 GTP를 만든다.', '함정')),
 dict(id='C4', num='4', title='에너지 수확 계산', sec='S8', level=2,
  q='''<p><b>1.</b> (계산) 아세틸-CoA 1개가 회로를 돌고 산화적 인산화까지 가면 ATP 몇 개? (NADH 2.5, FADH₂ 1.5)</p>
<p><b>2.</b> (계산) 피루브산 1개가 CO₂로 완전히 산화되면 ATP 몇 개?</p>
<p><b>3.</b> (계산) 포도당 1개에서 시트르산 회로(2바퀴)만으로 만들어지는 NADH · FADH₂ · GTP · CO₂ 수는?</p>
<p><b>4.</b> (O/X) 시트르산 회로는 O₂를 직접 반응물로 쓰지 않으므로, 산소가 없어도 계속 돈다.</p>''',
  answer=chips('1. 3×2.5 + 1.5 + 1 = <b>10</b>', '2. PDH NADH 2.5 + 10 = <b>12.5</b>', '3. NADH 6 · FADH₂ 2 · GTP 2 · CO₂ 4', '4. <b>X</b>'),
  explain=fig(yield_bars(), '') + steps('2. 피루브산 → 아세틸-CoA에서 NADH 1개(2.5) 추가.',
   '4. 산소가 없으면 NADH·FADH₂가 재산화되지 못해 NAD⁺·FAD가 바닥 → 탈수소 단계가 멈춘다.') +
   key('회로의 진짜 산물 = 환원된 전자 운반체.')),
 dict(id='C5', num='5', title='양방향성과 보충 반응', sec='S9', level=2,
  q='''<p><b>1.</b> (짝짓기) 회로 중간체 → 생합성 산물: α-KG · 숙시닐-CoA · OAA · 시트르산 ↔ 헴, 글루탐산, 지방산, 아스파르트산</p>
<p><b>2.</b> (빈칸) 동물에서 가장 중요한 보충 반응은 피루브산 + HCO₃⁻ + ATP → ( &nbsp; )이며, 효소는 ( &nbsp;&nbsp;&nbsp;&nbsp; ), 조효소는 ( &nbsp;&nbsp; ), 알로스테릭 활성화제는 ( &nbsp;&nbsp;&nbsp; )이다.</p>
<p><b>3.</b> (O/X) 아세틸-CoA만 충분히 공급하면 회로가 OAA를 순수하게 늘릴 수 있다.</p>
<p><b>4.</b> (서술) 왜 OAA 부족을 아세틸-CoA가 “알려 주는” 구조가 합리적인가?</p>''',
  answer=chips('1. α-KG → 글루탐산 · 숙시닐-CoA → 헴 · OAA → 아스파르트산 · 시트르산 → 지방산', '2. <b>OAA</b> / <b>피루브산 카복실화효소</b> / <b>비오틴</b> / <b>아세틸-CoA</b>', '3. <b>X</b>', '4. OAA가 모자라면 아세틸-CoA가 회로에 못 들어가 쌓임 → 그 신호로 PC를 켜 OAA 보충'),
  explain=fig(amphibolic(), '') + steps('3. 아세틸 2C가 들어오면 CO₂ 2개가 나가 OAA 수는 그대로. OAA를 늘리려면 PC 같은 보충 반응이 필요.',
   '4. 아세틸-CoA = “연료는 있는데 받아 줄 OAA가 없다”는 신호. 동시에 PDH는 억제해 피루브산을 OAA 쪽으로.') +
   tip('MSG(글루탐산 나트륨)도 α-KG에서 만든다.', '연결')),
 dict(id='C6', num='6', title='회로의 조절', sec='S10–S12', level=2,
  q='''<p><b>1.</b> (분류) 다음이 PDH를 억제(⊗)하는지 활성화(▲)하는지: ATP, AMP, 아세틸-CoA, NAD⁺, NADH, CoA, 지방산, Ca²⁺</p>
<p><b>2.</b> (O/X) PDH는 E1의 Ser가 인산화되면 활성화된다.</p>
<p><b>3.</b> (빈칸, ’22 약시) 시트르산 생성효소의 억제제는 ( &nbsp; ), ( &nbsp; ), ( &nbsp; ), ( &nbsp; )이고 활성화제는 ( &nbsp; )이다.</p>
<p><b>4.</b> (서술) 근육이 수축할 때 회로가 빨라지는 이유를 Ca²⁺로 설명하라.</p>''',
  answer=chips('1. ⊗ ATP · 아세틸-CoA · NADH · 지방산 / ▲ AMP · NAD⁺ · CoA · Ca²⁺', '2. <b>X</b> (인산화 = OFF)', '3. <b>NADH · 숙시닐-CoA · 시트르산 · ATP</b> / <b>ADP</b>', '4. Ca²⁺ → PDH(포스파타아제) · IDH · α-KG DH 활성 → NADH ↑ → ATP ↑'),
  explain=fig(pdh_switch(), '') + steps('1. 연료·산물 = 억제, 수요·기질 = 활성.', '4. Ca²⁺는 수축(ATP 소비)의 신호이므로 ATP가 떨어지기 전에 미리 공급을 늘린다 (피드포워드 성격).') +
   warn('PDH(인산화 = OFF) vs 글리코겐 인산화효소(인산화 = ON). 짝으로 외우자.', '함정')),
 dict(id='C7', num='7', title='기질 채널링과 글리옥실산 회로', sec='S13–S14', level=1,
  q='''<p><b>1.</b> (O/X) 세포를 깨서 희석하면 약하게 붙어 있던 회로 효소 복합체가 흩어질 수 있다.</p>
<p><b>2.</b> (빈칸) 글리옥실산 회로의 고유 효소 2개는 ( &nbsp;&nbsp;&nbsp;&nbsp; )와 ( &nbsp;&nbsp;&nbsp;&nbsp; )이며, 아세틸-CoA ( ) 분자로 숙신산 ( ) 분자를 만든다.</p>
<p><b>3.</b> (O/X) 글리옥실산 회로에서는 CO₂가 2개 방출된다.</p>
<p><b>4.</b> (서술) 사람은 지방산으로 포도당을 만들 수 없다. 이유 2가지는?</p>''',
  answer=chips('1. <b>O</b>', '2. <b>아이소시트르산 분해효소 · 말산 생성효소</b> / 2 → 1', '3. <b>X</b> (③④를 건너뜀)', '4. ① PDH 비가역 ② 글리옥실산 회로 효소 없음 → 아세틸 2C는 CO₂로 다 나감'),
  explain=fig(glyox(), '') + steps('1. 높은 농도가 결합을 유리하게 함 → 희석하면 해리 → 채널링 소실.',
   '4. 지방산 → 아세틸-CoA는 회로에서 CO₂ 2개로 나갈 뿐 OAA 순증가가 없어 포도당신생 재료가 안 된다. 단 TAG의 글리세롤은 포도당 가능.') +
   key('식물 종자: 지방체 → 글리옥시솜 → 미토콘드리아 → 세포질 순으로 지방이 포도당이 된다.')),
]
NO_STRIP = ('S15',)
CHECK_AFTER = {2: 'C1', 3: 'C2', 6: 'C3', 7: 'C4', 8: 'C5', 11: 'C6', 13: 'C7'}

if __name__ == '__main__':
    import exam16 as M
    examlib.render(M)
