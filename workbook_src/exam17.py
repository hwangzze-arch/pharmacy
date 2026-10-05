# -*- coding: utf-8 -*-
"""17장 시험대비 요약노트.  python3 exam17.py → exam_ch17.pdf"""
import os, sys
os.environ['CH'] = '17'
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from helpers import *
import examlib
import ch17
from ch17 import beta_cycle, carnitine, odd_chain

CH = 17
CH_TITLE = '지방산 분해'
FOOT = 'Lehninger 8e · Ch.17 지방산 분해 — 시험대비 요약노트'

_items = [i for i in ch17.ALL_ITEMS if i['level'] < 3]
WB = {i['id']: 6 + k for k, i in enumerate(_items)}
link = examlib.make_link(WB, CH)
page = examlib.make_page(link)


# ------------------------------------------------------------------ drawings
def fuel_bars():
    return bars([('탄수화물·단백질', 17, C['blue'], '≈ 17 kJ/g (4 kcal/g)'), ('지방 (TG)', 38, C['orange'], '≈ 38 kJ/g (9 kcal/g)'),
                 ('글리코겐 (물 포함)', 6, C['gray'], '물 2배를 끌고 다녀 실제론 더 낮음')], height=120, vmax=48, width=560)


def absorb():
    return vflow(['① 담즙산염이 지방을 유화 → 혼합 미셀', '② 장 리파아제: TG → 모노아실글리세롤 + FA', '③ 장 점막 세포가 흡수 → TG로 재합성',
                  '④ TG + 콜레스테롤 + 아포지단백질 = 킬로미크론', '⑤ 림프 → 혈액으로 이동', '⑥ 모세혈관 LPL(apoC-II가 켬): TG → FA + 글리세롤',
                  '⑦ FA가 세포 안으로', '⑧ 근육: 산화(ATP) / 지방조직: 다시 TG로 저장'],
                 colors=[C['green'], C['green'], C['blue'], C['blue'], C['navy'], C['orange'], C['orange'], C['purple']], box_h=24, gap=12, width=520, font=10.5, bw=470)


def mobilize():
    return vflow(['혈당 ↓ → 글루카곤 · 에피네프린', '수용체 → Gs → 아데닐산 고리화효소 → cAMP', 'PKA → 페릴리핀 · HSL 인산화',
                  '리파아제가 TG → 지방산 + 글리세롤', '지방산 + 혈청 알부민 → 혈액으로', '근육·심장: β-산화 → TCA → ATP'],
                 colors=[C['red'], C['navy'], C['orange'], C['orange'], C['blue'], C['green']], box_h=24, gap=12, width=520, font=10.5, bw=440)


def glycerol_fate():
    return flow(['글리세롤', '글리세롤 3-인산', 'DHAP', 'GAP → 해당 / 당신생'], arrow_labels=['글리세롤 키나아제 (ATP)', '탈수소효소 (NADH)', 'TPI'],
                colors=[C['navy'], C['blue'], C['blue'], C['green']], box_h=38, width=560, font=10.5)


def yield_bars():
    return bars([('7 FADH₂ × 1.5', 10.5, C['purple'], '10.5'), ('7 NADH × 2.5', 17.5, C['blue'], '17.5'), ('8 아세틸-CoA × 10', 80, C['green'], '80'),
                 ('팔미토일-CoA 합계', 108, C['orange'], '108 ATP'), ('유리 팔미트산', 106, C['red'], '106 ATP (활성화 −2)')], height=170, vmax=130, width=560)


def malonyl_switch():
    W, H = 560, 210
    b = arrowdef('ms1', C['green']) + arrowdef('ms2', C['red']) + arrowdef('ms3', C['gray'])
    b += f'<rect x="10" y="20" width="150" height="46" rx="10" fill="#f0fdf4" stroke="{C["green"]}" stroke-width="2"/>' + T(85, 39, '식후: 인슐린', 11.5, C['green'], weight=900) + T(85, 56, '→ ACC 탈인산화 = ON', 10, C['ink'])
    b += f'<rect x="10" y="140" width="150" height="46" rx="10" fill="#fef2f2" stroke="{C["red"]}" stroke-width="2"/>' + T(85, 159, '공복: 글루카곤', 11.5, C['red'], weight=900) + T(85, 176, '→ PKA → ACC 인산화 = OFF', 10, C['ink'])
    b += f'<rect x="210" y="78" width="140" height="50" rx="12" fill="#fefce8" stroke="#eab308" stroke-width="2"/>' + T(280, 98, '아세틸-CoA → 말로닐-CoA', 10.5, '#a16207', weight=900) + T(280, 116, 'ACC (비오틴)', 10, C['gray'])
    b += f'<line x1="162" y1="50" x2="208" y2="88" stroke="{C["green"]}" stroke-width="2" marker-end="url(#ms1)"/><line x1="162" y1="156" x2="208" y2="120" stroke="{C["red"]}" stroke-width="2" marker-end="url(#ms2)"/>'
    b += f'<rect x="400" y="20" width="150" height="46" rx="10" fill="white" stroke="{C["navy"]}" stroke-width="2"/>' + T(475, 39, '말로닐-CoA ↑', 11.5, C['navy'], weight=900) + T(475, 56, 'CAT I ⊗ → β-산화 OFF', 10, C['red'], weight=700)
    b += f'<rect x="400" y="140" width="150" height="46" rx="10" fill="white" stroke="{C["navy"]}" stroke-width="2"/>' + T(475, 159, '말로닐-CoA ↓', 11.5, C['navy'], weight=900) + T(475, 176, 'CAT I 열림 → β-산화 ON', 10, C['green'], weight=700)
    b += f'<line x1="352" y1="92" x2="398" y2="50" stroke="{C["gray"]}" stroke-width="2" marker-end="url(#ms3)"/><line x1="352" y1="116" x2="398" y2="158" stroke="{C["gray"]}" stroke-width="2" marker-end="url(#ms3)"/>'
    b += T(280, 200, '지방을 만드는 중엔 태우지 않는다 (헛된 회로 방지)', 11, C['navy'], weight=900)
    return svg(W, H, b)


def ketone_make():
    return flow(['2 아세틸-CoA', '아세토아세틸-CoA', 'HMG-CoA', '아세토아세트산'], arrow_labels=['티올레이스', 'HMG-CoA 합성효소 (+아세틸-CoA)', 'HMG-CoA 분해효소'],
                colors=[C['navy'], C['blue'], C['blue'], C['orange']], box_h=38, width=560, font=10.5)


def ketone_use():
    return flow(['β-하이드록시뷰티르산', '아세토아세트산', '아세토아세틸-CoA', '2 아세틸-CoA → TCA'], arrow_labels=['탈수소효소 (NADH)', '전이효소 (숙시닐-CoA)', '티올레이스'],
                colors=[C['orange'], C['orange'], C['blue'], C['green']], box_h=38, width=560, font=10.5)


def ketone_liver():
    W, H = 560, 200
    b = arrowdef('kl', C['gray']) + arrowdef('kl2', C['red'])
    b += f'<rect x="10" y="10" width="330" height="180" rx="14" fill="#fff7ed" stroke="#fdba74"/>' + T(175, 30, '간세포 (공복 · 1형 당뇨)', 12, C['orange'], weight=900)
    b += T(80, 62, '지방산', 11, C['ink'], weight=700) + f'<line x1="110" y1="58" x2="168" y2="58" stroke="{C["gray"]}" stroke-width="2" marker-end="url(#kl)"/>' + T(139, 50, 'β-산화 ↑', 9.5, C['orange'], weight=700)
    b += T(225, 62, '아세틸-CoA ↑↑', 11, C['navy'], weight=900)
    b += T(110, 120, '옥살로아세트산', 11, C['ink'], weight=700) + f'<line x1="110" y1="128" x2="110" y2="166" stroke="{C["red"]}" stroke-width="2" marker-end="url(#kl2)"/>' + T(110, 182, '포도당신생으로 빠짐', 10, C['red'], weight=700)
    b += f'<line x1="225" y1="70" x2="225" y2="104" stroke="{C["red"]}" stroke-width="2" stroke-dasharray="4 3"/>' + T(225, 120, 'TCA 못 들어감 ✕', 10.5, C['red'], weight=900)
    b += f'<line x1="282" y1="58" x2="380" y2="58" stroke="{C["gray"]}" stroke-width="2.2" marker-end="url(#kl)"/>' + T(330, 50, '케톤체 생성', 9.5, C['orange'], weight=700)
    b += T(470, 50, '케톤체 → 혈액', 11.5, C['orange'], weight=900) + T(470, 70, '심장 · 근육 · 신장 · 뇌', 10.5, C['green'], weight=700)
    b += f'<rect x="380" y="100" width="170" height="70" rx="12" fill="#fef2f2" stroke="{C["red"]}"/>' + T(465, 122, '너무 많으면', 10.5, C['ink']) + T(465, 142, '케톤산증 → 혼수', 12, C['red'], weight=900) + T(465, 160, '아세톤 = 호흡의 과일 냄새', 9.5, C['gray'])
    return svg(W, H, b)


# ------------------------------------------------------------------ summary pages
SUMMARY = []

SUMMARY.append(page('S1', '지방은 왜 최고의 저장 연료인가', 'Fats provide efficient fuel storage · Slides 1–7',
  '지방산은 탄소가 <b>더 환원</b>되어 있어(–CH₂–) 태울 때 에너지가 많고, <b>비극성</b>이라 물을 끌고 다니지 않는다. 그래서 같은 무게에 2배 이상의 에너지를 수개월 동안 저장한다.',
  f'''<div class="grid2"><div class="card"><h4>📌 g당 에너지 비교 (슬라이드 5)</h4><figure class="fig">{fuel_bars()}</figure>
 {table(['', '포도당·글리코겐', '지방 (TG)'], [['에너지', '≈ 17 kJ/g', '≈ 38 kJ/g'], ['물', '무게의 약 2배와 결합', '거의 없음'], ['용도', '단기 · 빠른 공급', '장기(수개월) · 느린 공급']])}</div>
<div><div class="card"><h4>📌 백색 지방조직 (슬라이드 4)</h4><p>지방세포 안은 거의 <b>하나의 큰 지방방울</b>(TG + 스테롤 에스터). 겉은 인지질 한 겹 + <b>페릴리핀</b> 단백질이 감싼다. 핵은 가장자리로 밀려나 있다.</p>
 <p class="small">갈색 지방조직 = 작은 방울 여러 개 + 미토콘드리아 많음 → 열 생산.</p></div>
 <div class="card" style="margin-top:3mm"><h4>📌 세포가 지방산을 얻는 3가지 경로 (슬라이드 7)</h4>{table(['공급원', '어떻게', '슬라이드'], [['① 음식', '소장 흡수 → 킬로미크론', 'S2'], ['② 저장 TG', '호르몬으로 동원 → 알부민', 'S3'], ['③ 새로 합성', '간에서 남는 탄수화물로 (21장)', '–']])}</div>
 {key('심장·간 에너지의 약 80%가 지방산 산화. 겨울잠 곰은 지방만으로 수개월을 버틴다(산화 때 대사수도 생김).')}</div></div>''',
  ('P1', 'P6', 'P14')))

SUMMARY.append(page('S2', '17.1 식이 지방의 흡수 — 8단계', 'Digestion & transport · Slides 8–14',
  '물에 안 녹는 지방은 <b>TG → FA → TG(킬로미크론) → FA → TG</b>로 모양을 바꾸며 이동한다. 막을 지날 땐 작게(FA), 운반할 땐 포장해서(킬로미크론).',
  f'''<div class="grid2"><div class="card"><h4>📌 흡수 8단계 (슬라이드 9)</h4><figure class="fig">{absorb()}</figure></div>
<div><div class="card"><h4>📌 단계별 핵심</h4>{table(['주인공', '포인트'], [
  ['<b>담즙산염</b> (콜산 등)', '간에서 콜레스테롤로 합성 → 담낭 저장. <b>효소가 아니라 세제</b>: 유화만 함'],
  ['<b>췌장(장) 리파아제</b>', 'TG의 1·3번 에스터를 끊어 2-모노아실글리세롤 + FA 2개'],
  ['<b>킬로미크론</b>', '가장 크고 밀도 낮은 지단백질. 속: TG·콜레스테릴 에스터 / 겉: 인지질·apoB-48·C-II·C-III'],
  ['<b>LPL</b> (지단백질 리파아제)', '근육·지방 모세혈관 내피에 붙어 있음. <b>apoC-II</b>가 켜는 스위치']], cls='left')}</div>
 {tip('비만약 <b>오르리스타트</b> = 췌장 리파아제 억제 → 지방 흡수 ↓ (부작용: 지방변).', '약학')}
 {warn('킬로미크론은 너무 커서 모세혈관이 아니라 <b>림프관</b>(유미관 → 흉관)으로 먼저 간다.', '함정')}</div></div>''',
  ()))

SUMMARY.append(page('S3', '저장 TG의 동원 — 호르몬 → cAMP → PKA', 'Mobilization · Slides 15–17',
  '혈당이 떨어지면 <b>글루카곤·에피네프린</b> → cAMP → <b>PKA</b>가 <b>페릴리핀</b>과 <b>호르몬 민감성 리파아제(HSL)</b>를 인산화 → TG가 지방산 + 글리세롤로. 지방산은 <b>혈청 알부민</b>에 실려 근육으로.',
  f'''<div class="grid2"><div class="card"><h4>📌 동원 경로 (슬라이드 16)</h4><figure class="fig">{mobilize()}</figure>
 <p class="small">페릴리핀이 인산화되면 지방방울 표면이 열려 리파아제가 TG에 접근할 수 있게 된다. 인슐린은 반대로 동원을 억제한다.</p></div>
<div><div class="card"><h4>📌 글리세롤의 운명 (슬라이드 17)</h4><figure class="fig">{glycerol_fate()}</figure>
 <p>TG 에너지의 약 95%는 지방산, 5%만 글리세롤. 그래도 글리세롤은 <b>포도당이 될 수 있는 유일한 부분</b>.</p></div>
 {warn('글리세롤 키나아제는 <b>간</b>에 있고 지방세포에는 거의 없다 → 글리세롤은 혈액으로 나가 간에서 처리.', '시험')}
 {tip('PDE(포스포다이에스터레이스) 억제제(예: 카페인) → cAMP 분해 ↓ → 지방 동원 ↑ (풀이노트 문제 2).', '연결')}</div></div>''',
  ('P2',)))

SUMMARY.append(page('S4', '지방산의 활성화와 카르니틴 셔틀', 'Carnitine shuttle · Slides 18–21',
  'β-산화 효소는 미토콘드리아 기질에 있다. 탄소 12개 이하 지방산은 그냥 들어가지만, <b>14개 이상</b>은 내막을 못 지나 <b>카르니틴 셔틀</b>이 필요하다: 활성화 → 카르니틴에 옮겨 싣기 → 안에서 다시 CoA로.',
  f'''<div class="grid2"><div class="card"><h4>📌 셔틀 그림 (슬라이드 18, 21)</h4><figure class="fig">{carnitine()}</figure>
 {key('세포질 CoA 풀(지방 합성용)과 미토콘드리아 CoA 풀(산화용)이 <b>분리</b>되어 있다 — 아실기만 건너간다.')}</div>
<div><div class="card"><h4>📌 세 반응 (슬라이드 18–21)</h4>{table(['#', '효소', '위치', '반응'], [
  ['①', '아실-CoA 합성효소', '외막', 'FA + CoA + ATP → 아실-CoA + <b>AMP + PPᵢ</b> (ΔG′° −34)'],
  ['②', '<b>CAT I</b> (= CPT1)', '외막', '아실-CoA + 카르니틴 → 아실-카르니틴 + CoA'],
  ['', '아실-카르니틴/카르니틴 수송체', '내막', '아실-카르니틴 들어오고 카르니틴 나감 (교환)'],
  ['③', 'CAT II (= CPT2)', '내막 안쪽', '아실-카르니틴 + CoA → 아실-CoA + 카르니틴']], cls='left')}</div>
 {warn('활성화에 ATP 1개를 쓰지만 AMP + PPᵢ(→ 2Pᵢ)로 가므로 <b>ATP 2개 분</b>의 에너지가 든다. 그래서 유리 팔미트산 = 108 − 2 = 106 ATP.', '계산')}
 {tip('중간체는 <b>아실-아데닐산</b>(아실-AMP, 효소 결합) → CoA가 공격해 아실-CoA (풀이노트 문제 9).', '기전')}
 {key('<b>CAT I = β-산화의 입구 = 조절 지점</b> (말로닐-CoA가 억제, S10).')}</div></div>''',
  ('P3', 'P5', 'P9')))

SUMMARY.append(page('S5', '17.2 β-산화 4단계', 'β-oxidation of saturated FA · Slides 22–24',
  '한 바퀴 = <b>탈수소(FAD) → 수화(H₂O) → 탈수소(NAD⁺) → 티올분해(CoA)</b>. 매 바퀴 β 탄소가 산화되어 탄소 2개가 아세틸-CoA로 떨어지고, FADH₂ 1 + NADH 1이 생긴다.',
  f'''<div class="grid2"><div class="card"><h4>📌 4단계 (슬라이드 24)</h4><figure class="fig">{beta_cycle()}</figure></div>
<div><div class="card"><h4>📌 지방산 산화의 3단계 (슬라이드 23)</h4>{table(['단계', '장소', '산물'], [['1 β-산화', '미토콘드리아 기질', '아세틸-CoA, NADH, FADH₂'], ['2 시트르산 회로', '기질', 'CO₂, NADH, FADH₂, GTP'], ['3 전자전달·산화적 인산화', '내막', 'H₂O, ATP']])}</div>
 <div class="card" style="margin-top:3mm"><h4>📌 회전 수 공식 (짝수 Cₙ)</h4><div class="formula">바퀴 수 = n/2 − 1 &nbsp;·&nbsp; 아세틸-CoA = n/2</div>
 <p>팔미트산(C16): 7바퀴 → 아세틸-CoA 8개 + FADH₂ 7 + NADH 7.</p></div>
 {key('TCA의 숙신산 → 푸마르산 → 말산 → OAA와 <b>똑같은 패턴</b> (FAD 탈수소 → 수화 → NAD 탈수소).')}
 {warn('③ 탈수소효소는 <b>L-이성질체</b>에만 작용. 마지막 바퀴(C4)는 아세틸-CoA <b>2개</b>가 나온다.', '함정')}</div></div>''',
  ('P8', 'P22', 'P7', 'P19', 'P21')))

SUMMARY.append(page('S6', '사슬 길이별 효소와 다기능 단백질', 'Isozymes · TFP · MFP · Slides 25–26',
  '1단계 아실-CoA 탈수소효소는 사슬 길이별 <b>동위효소 3종</b>. ②–④단계는 긴 사슬이면 내막의 <b>삼기능 단백질(TFP)</b>이, 짧으면 기질의 가용성 효소들이 맡는다.',
  f'''<div class="grid2"><div><div class="card"><h4>📌 아실-CoA 탈수소효소 동위효소 (슬라이드 25)</h4>{table(['효소', '사슬 길이 (탄소 수)'], [['VLCAD (very-long)', '12–18'], ['MCAD (medium)', '4–14'], ['SCAD (short)', '4–8']])}
 <p class="small">FADH₂의 전자 → <b>ETF</b>(전자전달 플라보단백질) → ETF:유비퀴논 산화환원효소 → Q → 호흡 사슬 (복합체 I을 건너뛰어 1.5 ATP).</p>
 {warn('<b>MCAD 결핍</b> = 가장 흔한 유전성 β-산화 장애. 공복 시 저혈당 + 케톤체 생성 부족.', '임상')}</div>
 <div class="card" style="margin-top:3mm"><h4>②–④단계 효소 두 세트</h4>{table(['세트', '대상', '위치'], [['TFP (삼기능 단백질)', 'C12 이상', '내막 (기질 채널링)'], ['가용성 효소 4개', 'C12 이하', '기질']])}</div></div>
<div class="card"><h4>📌 다기능 단백질(MFP)의 장단점 (슬라이드 26)</h4>{table(['', '내용'], [['장점', '<b>기질 채널링</b>: 중간체를 바로 옆 활성 부위로 → 빠르고, 희석·누출 없음'], ['단점', '단계별 따로 조절이 어렵다. 한 폴리펩타이드 돌연변이로 여러 활성이 한꺼번에 망가짐']], cls='left')}
 {table(['시스템', '효소 배치'], [['그람양성균·미토콘드리아 짧은 사슬', '4개 효소 따로 (확산)'], ['그람음성균', '4개가 한 덩어리'], ['미토콘드리아 매우 긴 사슬', '내막의 TFP'], ['식물 퍼옥시좀·글리옥시좀', 'MFP']], cls='left')}
 {tip('16장 PDH의 리포일 팔, 시트르산 회로 효소 복합체와 같은 아이디어.', '연결')}</div></div>''',
  ()))

SUMMARY.append(page('S7', '수지 계산 — 팔미트산 1개 = 106 ATP', 'Balance sheet · Slide 27',
  '팔미토일-CoA 1개: β-산화 7바퀴(FADH₂ 7 + NADH 7 = 28 ATP) + 아세틸-CoA 8개(× 10 = 80 ATP) = <b>108 ATP</b>. 유리 팔미트산이면 활성화 비용 2를 빼서 <b>106 ATP</b>.',
  f'''<div class="formula">팔미토일-CoA + 23O₂ + 108Pᵢ + 108ADP → CoA + 108ATP + 16CO₂ + 23H₂O</div>
<div class="grid2" style="margin-top:3mm"><div class="card"><h4>📌 ATP 막대 (슬라이드 27)</h4><figure class="fig">{yield_bars()}</figure></div>
<div><div class="card"><h4>📌 단계별 표</h4>{table(['출처', '개수', '× ATP', '= ATP'], [['FADH₂ (β-산화)', '7', '1.5', '10.5'], ['NADH (β-산화)', '7', '2.5', '17.5'], ['아세틸-CoA (TCA + 전자전달)', '8', '10', '80'], ['<b>팔미토일-CoA</b>', '', '', '<b>108</b>'], ['활성화 비용 (ATP → AMP)', '', '', '−2'], ['<b>유리 팔미트산</b>', '', '', '<b>106</b>']], cls='left')}</div>
 {tip('O₂: β-산화 7 + 아세틸-CoA 16 = <b>23 O₂</b>. CO₂ 16, H₂O 23 (대사수).', '덤')}
 {key('포도당(6C) ≈ 32 ATP vs 팔미트산(16C) ≈ 106 ATP. 탄소당으로도 지방이 더 많다 — 더 환원돼 있으니까.')}</div></div>''',
  ('P14', 'P25')))

SUMMARY.append(page('S8', '불포화 지방산 — 이성질화효소와 환원효소', 'Unsaturated FA · Slides 28–29',
  '천연 이중결합은 <b>cis</b>이고 위치가 β-산화와 맞지 않는다. 엔오일-CoA 수화효소는 <b>trans-Δ²</b>만 받기 때문에 이를 맞춰 주는 효소가 추가로 필요하다.',
  f'''<div class="grid2"><div class="card"><h4>📌 단일불포화: 올레산 18:1 (Δ⁹) (슬라이드 28)</h4>{vflow(['올레오일-CoA (C18, cis-Δ⁹)', '3바퀴 → 아세틸-CoA 3 + cis-Δ³-도데센오일-CoA', 'Δ³,Δ²-엔오일-CoA 이성질화효소', 'trans-Δ² → 나머지 5바퀴 → 아세틸-CoA 6'], colors=[C['navy'], C['blue'], C['red'], C['green']], box_h=24, gap=14, width=520, font=10.5, bw=460)}
 {warn('이성질화된 바퀴는 1단계(아실-CoA 탈수소효소)를 건너뛴다 → <b>FADH₂ 1개 덜</b> → 이중결합 하나당 ATP 1.5 적음.', '계산')}</div>
<div class="card"><h4>📌 다중불포화: 리놀레산 18:2 (Δ⁹,¹²) (슬라이드 29)</h4>{table(['효소', '하는 일', '언제'], [['엔오일-CoA 이성질화효소', 'cis(trans)-Δ³ → trans-Δ²', '이중결합이 <b>홀수</b> 위치'], ['<b>2,4-다이엔오일-CoA 환원효소</b>', 'trans-Δ², cis-Δ⁴ → trans-Δ³ (<b>NADPH</b> 사용)', '이중결합이 <b>짝수</b> 위치']], cls='left')}
 <p class="small">리놀레산: 3바퀴 → 이성질화 → 1바퀴 + 다음 바퀴 첫 산화 → 환원효소(NADPH) → 이성질화 → 4바퀴. 총 아세틸-CoA 9개.</p>
 {key('홀수 위치 이중결합 = 이성질화효소 하나 / 짝수 위치 = 환원효소 + 이성질화효소 둘 다.')}</div></div>''',
  ('P8', 'P10')))

SUMMARY.append(page('S9', '홀수 탄소 지방산 — 프로피오닐-CoA', 'Odd-number FA · Slide 30',
  '홀수 지방산도 똑같이 잘리다가 마지막에 <b>프로피오닐-CoA(C3)</b>가 남는다. 이것은 3단계(카복실화 → 에피머화 → 자리옮김)를 거쳐 <b>숙시닐-CoA</b>가 되어 TCA로 들어간다.',
  f'''<div class="card"><h4>📌 프로피오닐-CoA → 숙시닐-CoA</h4><figure class="fig">{odd_chain()}</figure></div>
<div class="grid2" style="margin-top:3mm"><div class="card">{table(['효소', '조효소', '하는 일'], [['프로피오닐-CoA 카복실화효소 (PCC)', '<b>비오틴</b>, ATP, HCO₃⁻', 'CO₂ 붙임 → D-메틸말로닐-CoA'], ['메틸말로닐-CoA 에피머화효소', '–', 'D → L'], ['메틸말로닐-CoA 뮤테이스', '<b>B₁₂</b> (코발라민)', '탄소 골격 재배열 → 숙시닐-CoA']], cls='left')}</div>
<div>{key('숙시닐-CoA는 TCA 중간체 → 순증가 → 말산 → OAA → <b>포도당신생 가능</b>. 그래서 홀수 지방산의 C3 부분은 포도당이 될 수 있다 (짝수 지방산은 불가).')}
 {warn('B₁₂ 결핍 → 메틸말로닐-CoA 축적 → <b>메틸말로닐산혈증</b>(소변 메틸말로닐산 ↑) (풀이노트 문제 17·18).', '임상')}
 {tip('Val·Ile·Met·Thr 분해도 프로피오닐-CoA를 거친다.', '연결')}</div></div>''',
  ('P11', 'P17', 'P18', 'P26')))

SUMMARY.append(page('S10', 'β-산화의 조절 — 말로닐-CoA가 입구를 막는다', 'Regulation · Slides 31–33',
  '가장 중요한 조절: 지방산 합성의 첫 중간체 <b>말로닐-CoA</b>가 <b>CAT I</b>을 억제 → 지방산이 미토콘드리아에 못 들어간다. 그리고 산물(NADH, 아세틸-CoA)이 쌓이면 β-산화 효소가 스스로 브레이크.',
  f'''<div class="grid2"><div class="card"><h4>📌 인슐린 vs 글루카곤 (슬라이드 33)</h4><figure class="fig">{malonyl_switch()}</figure>
 {table(['', '식후 (혈당 ↑)', '공복 (혈당 ↓)'], [['호르몬', '인슐린', '글루카곤'], ['ACC', '탈인산화 → 활성', 'PKA 인산화 → 비활성'], ['말로닐-CoA', '↑', '↓'], ['CAT I', '억제', '풀림'], ['결과', '지방산 <b>합성</b>', '<b>β-산화</b>']])}</div>
<div><div class="card"><h4>📌 산물 억제 (슬라이드 31)</h4>{table(['신호', '억제되는 효소', '단계'], [['[NADH]/[NAD⁺] ↑', 'β-하이드록시아실-CoA 탈수소효소', '③'], ['[아세틸-CoA] ↑', '티올레이스', '④']])}</div>
 {key('말로닐-CoA → CAT I ⊗ = 지방산 <b>합성과 분해를 반대로</b> 묶는 연결고리 (헛된 회로 방지).')}
 {warn('ACC는 PDH처럼 <b>인산화 = OFF</b>. (글리코겐 인산화효소는 인산화 = ON)', '함정')}</div></div>''',
  ('P4', 'P20')))

SUMMARY.append(page('S11', 'ACC2 · 비오틴 카복실화효소 4총사', 'Slides 34–35',
  '<b>ACC2</b>가 없는 쥐는 더 많이 먹어도 마르고 지방이 적다 — 말로닐-CoA 브레이크가 풀려 지방을 계속 태우기 때문. 비만 치료 약물 표적.',
  f'''<div class="grid2"><div><div class="card"><h4>📌 ACC 동위효소 (슬라이드 34)</h4>{table(['', '위치', '말로닐-CoA의 용도'], [['ACC1', '세포질 (간·지방조직)', '지방산 <b>합성</b>'], ['<b>ACC2</b>', '미토콘드리아 외막 근처 (심장·근육)', 'CAT I <b>억제</b> (β-산화 조절)']])}
 <p>Acc2<sup>−/−</sup> 쥐: 정상 수명, 지방산 산화율 ↑, 지방량 ↓ (먹는 양은 오히려 많음).</p>
 {key('ACC2 억제 → 말로닐-CoA ↓ → CAT I 열림 → 지방 연소 ↑ → 비만 치료 아이디어.')}</div></div>
<div class="card"><h4>📌 비오틴을 쓰는 카복실화효소 (슬라이드 35)</h4>{table(['효소', '반응', '의미'], [
  ['<b>PC</b>', '피루브산 → OAA', '포도당신생, TCA 보충 (16장)'], ['<b>ACC</b>', '아세틸-CoA → 말로닐-CoA', '지방산 합성, β-산화 조절'],
  ['<b>PCC</b>', '프로피오닐-CoA → 메틸말로닐-CoA', '홀수 지방산, Val·Ile·Met·Thr'], ['<b>MCC</b>', '3-메틸크로토닐-CoA 카복실화', '류신 분해']], cls='left')}
 <p class="small">공통: HCO₃⁻ + ATP + <b>비오틴</b>으로 CO₂를 붙인다. 날달걀 흰자의 아비딘이 비오틴과 결합 → 비오틴 결핍.</p></div></div>''',
  ('P20',)))

SUMMARY.append(page('S12', '퍼옥시좀 β-산화 · α-산화 · ω-산화', 'Slides 36–40',
  '미토콘드리아 말고도 지방산을 태우는 곳이 있다. <b>퍼옥시좀</b>은 아주 긴 사슬·가지 지방산을 짧게 줄이고(ATP 안 생김, H₂O₂ 생성), <b>α-산화</b>는 β 가지 때문에 막힌 지방산을, <b>ω-산화</b>(소포체)는 반대쪽 끝을 처리한다.',
  f'''<div class="grid2"><div class="card"><h4>📌 미토콘드리아 vs 퍼옥시좀 (슬라이드 37)</h4>{table(['', '미토콘드리아', '퍼옥시좀'], [
  ['1단계 효소', '아실-CoA 탈수소효소', '아실-CoA <b>산화효소</b>'], ['FADH₂의 전자', '호흡 사슬 → ATP', 'O₂로 바로 → <b>H₂O₂</b> (카탈레이스가 분해)'],
  ['ATP', '생성', '1단계에선 없음 (열)'], ['대상', '일반 지방산', '매우 긴 사슬(VLCFA) · 가지 지방산'], ['산물', 'CO₂까지', '짧아진 사슬 · 아세틸-CoA 수출']], cls='left')}
 {warn('퍼옥시좀 장애: <b>젤웨거 증후군</b>, <b>X-ALD</b>(부신백질이영양증) → VLCFA 축적.', '임상')}
 <p class="small">식물 종자의 글리옥시좀: β-산화 아세틸-CoA → 글리옥실산 회로 → 포도당 (16장 S14).</p></div>
<div><div class="card"><h4>📌 α-산화 — 피탄산 (슬라이드 39)</h4><p>피탄산(엽록소 유래)은 <b>β 탄소에 메틸 가지</b>가 있어 β-산화 불가 → 퍼옥시좀에서 <b>탄소 1개</b>를 먼저 떼어(α-산화) 프리스탄산으로 → 그 뒤 β-산화 (프로피오닐-CoA도 생김).</p>
 {warn('α-산화 결함 = <b>레프숨병</b>: 피탄산 축적 → 신경 손상.', '임상')}</div>
 <div class="card" style="margin-top:3mm"><h4>📌 ω-산화 — 소포체 (슬라이드 40)</h4><p>카복실기 반대쪽 끝 메틸(ω) 탄소를 <b>사이토크롬 P450</b>(O₂ + NADPH)이 –OH로 → 알데하이드 → –COOH. 결과: 양 끝이 –COOH인 <b>다이카복실산</b> → 양쪽에서 β-산화 → 숙신산·아디프산.</p>
 <p class="small">평소엔 보조 경로. β-산화가 막혔을 때 늘어난다.</p></div></div></div>''',
  ()))

SUMMARY.append(page('S13', '17.3 케톤체 — 만들기와 쓰기', 'Ketone bodies · Slides 41–43',
  '공복 때 간에서 넘치는 아세틸-CoA로 <b>케톤체</b>(아세토아세트산, β-하이드록시뷰티르산, 아세톤)를 만들어 다른 조직에 연료로 수출한다. <b>간은 만들기만 하고 쓰지 못한다.</b>',
  f'''<div class="grid2"><div class="card"><h4>📌 생성 — 간 미토콘드리아 (슬라이드 42)</h4><figure class="fig">{ketone_make()}</figure>
 {table(['케톤체', '어떻게', '특징'], [['아세토아세트산', 'HMG-CoA 분해효소 산물', '기본 케톤체'], ['<b>D-β-하이드록시뷰티르산</b>', '아세토아세트산 환원 (NADH)', '혈중 가장 많음'], ['아세톤', '아세토아세트산 자발적 탈카복실화', '소량, 호흡으로 배출 (과일 냄새)']], cls='left')}
 <p class="small">HMG-CoA는 콜레스테롤 합성의 중간체이기도 하다 (세포질 쪽).</p></div>
<div><div class="card"><h4>📌 사용 — 간 외 조직 (슬라이드 43)</h4><figure class="fig">{ketone_use()}</figure>
 <p>심장 · 골격근 · 신장 피질, 오래 굶으면 <b>뇌</b>까지(포도당 아끼기).</p></div>
 {warn('간에는 <b>β-케토아실-CoA 전이효소</b>(티오포레이스)가 없다 → 간은 케톤체를 못 쓴다. 생산자와 소비자가 나뉘어 있음.', '시험')}
 {tip('전이효소는 숙시닐-CoA의 CoA를 빌려 온다 → 숙시닐-CoA 합성효소의 GTP 1개를 손해 본다.', '덤')}</div></div>''',
  ('P16',)))

SUMMARY.append(page('S14', '공복 · 당뇨와 케톤산증', 'Slides 44–45',
  '공복이나 1형 당뇨에서는 간의 <b>OAA가 포도당신생으로 빠져</b> 아세틸-CoA가 TCA에 못 들어간다. 동시에 β-산화는 ↑ → 쌓인 아세틸-CoA가 케톤체로. 너무 많으면 <b>케톤산증 → 혼수 → 사망</b>.',
  f'''<div class="grid2"><div class="card"><h4>📌 간에서 일어나는 일 (슬라이드 44)</h4><figure class="fig">{ketone_liver()}</figure>
 {table(['', '변화'], [['포도당신생', '↑ (OAA 소모)'], ['시트르산 회로', '↓'], ['β-산화', '↑'], ['케톤체', '↑↑']])}</div>
<div><div class="card"><h4>📌 1형 당뇨 — 케톤산증의 흐름</h4><ol style="margin:.2em 0;padding-left:1.3em"><li>인슐린 없음 → 세포가 포도당을 못 씀 (혈당 ↑)</li><li>지방 동원 ↑ (HSL 억제 해제) → 혈중 지방산 ↑</li><li>간 β-산화 ↑ + OAA는 당신생으로 → 아세틸-CoA 과잉</li><li>케톤체 ↑↑ → 혈액 산성화 = <b>케톤산증</b></li><li>치료: 인슐린, 수액 보충, 중탄산염</li></ol></div>
 <div class="card" style="margin-top:3mm"><h4>저탄고지 식단 (슬라이드 45)</h4><p class="small">탄수화물을 10–25%로 적당히 줄이면 혈당·혈중 지질 개선. 10% 미만 극단적 제한은 6개월 이후 체지방·LDL ↑. 권장: 탄수화물 55–65%, 단백질 7–20%, 지방 15–30%.</p></div>
 {key('15장 S3(GLUT4·1형 당뇨)과 같은 이야기를 지방산 쪽에서 본 것.')}</div></div>''',
  ('P16', 'P17', 'P27')))

SUMMARY.append(page('S15', '17장 한 장 요약 + 시험 직전 체크리스트', 'Summary · Slide 46',
  '요약 슬라이드를 숫자·효소 이름과 함께 한 장으로. (약어는 바로 뒤 총정리 참고)',
  f'''<div class="grid3">
 <div class="card"><h4>① 소화 · 동원 · 수송</h4><ul style="font-size:.95em"><li>지방 38 kJ/g, 물 없이 저장</li><li>담즙산염(세제) → 리파아제 → 킬로미크론 → LPL(apoC-II)</li><li>글루카곤 → cAMP → PKA → HSL·페릴리핀</li><li>FA는 알부민, 글리세롤은 간 → GAP</li><li>C14↑: 카르니틴 셔틀, CAT I = 조절점</li><li>활성화 = ATP 2개 분</li></ul></div>
 <div class="card"><h4>② β-산화</h4><ul style="font-size:.95em"><li>탈수소(FAD) → 수화 → 탈수소(NAD⁺) → 티올분해</li><li>Cₙ: n/2 − 1바퀴, n/2 아세틸-CoA</li><li>팔미토일-CoA 108 / 팔미트산 106 ATP</li><li>불포화: 이성질화효소(+ 환원효소, NADPH)</li><li>홀수: 프로피오닐-CoA → 숙시닐-CoA (비오틴, B₁₂)</li><li>말로닐-CoA → CAT I ⊗</li></ul></div>
 <div class="card"><h4>③ 기타 산화 · 케톤체</h4><ul style="font-size:.95em"><li>퍼옥시좀: 산화효소 → H₂O₂, VLCFA</li><li>α-산화: 피탄산 (레프숨병)</li><li>ω-산화: 소포체 P450</li><li>케톤체: 간에서 생성, 간 외에서 사용</li><li>간엔 β-케토아실-CoA 전이효소 없음</li><li>공복·당뇨: OAA 고갈 → 케톤산증</li></ul></div>
</div>
<div class="grid2" style="margin-top:3mm"><div class="card"><h4>🔢 꼭 외울 숫자</h4><div class="tiles" style="grid-template-columns:repeat(3,1fr)">
 <div><b>지방 에너지</b><span>38 kJ/g</span><small>탄수화물 17</small></div><div><b>셔틀 필요</b><span>C14 ↑</span><small>C12 이하는 그냥</small></div><div><b>팔미트산</b><span>7 · 8</span><small>바퀴 · 아세틸-CoA</small></div>
 <div><b>팔미토일-CoA</b><span>108</span><small>ATP</small></div><div><b>유리 팔미트산</b><span>106</span><small>ATP</small></div><div><b>O₂</b><span>23</span><small>팔미토일-CoA 1개</small></div></div></div>
 <div class="card"><h4>⚠️ 단골 함정</h4><ol style="margin:.2em 0;padding-left:1.3em;font-size:.95em"><li>담즙산염은 효소가 아니다</li><li>활성화: ATP → AMP (2개 분)</li><li>CoA는 내막을 못 건넌다 — 아실기만</li><li>불포화 이중결합 하나당 FADH₂ 1개 덜</li><li>짝수 지방산 → 포도당 ✕ / 홀수의 C3·글리세롤 → ○</li><li>간은 케톤체를 만들지만 못 쓴다</li></ol></div></div>''',
  ()))

MAPROWS = [['S1–S4 저장 · 동원 · 셔틀', '문제 1·2·3·5·6·9·14'], ['S5–S9 β-산화 · 수지 · 변형', '문제 7·8·10·11·17·18·19·21·22·25·26'], ['S10–S11 조절', '문제 4·20'], ['S13–S14 케톤체', '문제 16·17·27']]

# ------------------------------------------------------------------ glossary
GLOSS = [
 ('TG (TAG)', 'Triacylglycerol (triglyceride)', '트라이아실글리세롤 (중성지방)', '글리세롤 + 지방산 3개, 저장 지방'),
 ('FA', 'Fatty Acid', '지방산', '긴 탄화수소 사슬 + –COOH'),
 ('MAG · DAG', 'Mono-/Diacylglycerol', '모노·다이아실글리세롤', 'TG가 부분 분해된 것'),
 ('LPL', 'Lipoprotein Lipase', '지단백질 리파아제', '모세혈관에서 킬로미크론 TG 분해'),
 ('apoB-48 · apoC-II', 'Apolipoprotein B-48 · C-II', '아포지단백질', 'B-48 = 킬로미크론 뼈대, C-II = LPL 스위치'),
 ('HSL', 'Hormone-Sensitive Lipase', '호르몬 민감성 리파아제', 'PKA가 인산화해 켬 → TG 분해'),
 ('PKA', 'Protein Kinase A', '단백질 키나아제 A', 'cAMP가 켬. HSL·페릴리핀·ACC 인산화'),
 ('cAMP', 'cyclic AMP', '고리형 AMP', '글루카곤·에피네프린의 2차 전달자'),
 ('PDE', 'Phosphodiesterase', '포스포다이에스터레이스', 'cAMP 분해 (카페인이 억제)'),
 ('Gs', 'stimulatory G protein', '자극성 G 단백질', '수용체 → 아데닐산 고리화효소 연결'),
 ('DHAP · GAP', 'Dihydroxyacetone Phosphate · Glyceraldehyde 3-Phosphate', '다이하이드록시아세톤 인산 · 글리세르알데하이드 3-인산', '글리세롤이 해당과정에 들어가는 입구'),
 ('TPI', 'Triose Phosphate Isomerase', '삼탄당 인산 이성질화효소', 'DHAP ⇌ GAP'),
 ('CoA (CoA-SH)', 'Coenzyme A', '조효소 A', '아실기를 티오에스터로 운반'),
 ('Acyl-CoA', 'fatty acyl-coenzyme A', '지방 아실-CoA', '활성화된 지방산'),
 ('CAT I · II (CPT1 · 2)', 'Carnitine Acyltransferase I · II', '카르니틴 아실전이효소 I · II', 'I = 외막·조절점 / II = 내막 안쪽'),
 ('AMP · ADP · ATP', 'Adenosine Mono-/Di-/Triphosphate', '아데노신 일·이·삼인산', '활성화에 ATP → AMP'),
 ('PPᵢ · Pᵢ', '(inorganic) Pyrophosphate · Phosphate', '피로인산 · 무기 인산', 'PPᵢ → 2Pᵢ로 반응을 당김'),
 ('FAD · FADH₂', 'Flavin Adenine Dinucleotide', '플라빈 아데닌 다이뉴클레오타이드', 'β-산화 ① 전자 수용체 (1.5 ATP)'),
 ('NAD⁺ · NADH', 'Nicotinamide Adenine Dinucleotide', '니코틴아마이드 아데닌 다이뉴클레오타이드', 'β-산화 ③ 전자 수용체 (2.5 ATP)'),
 ('NADPH', 'NAD Phosphate (reduced)', '환원형 NADP', '2,4-다이엔오일-CoA 환원효소·P450의 전자 공여체'),
 ('VLCAD · MCAD · SCAD', 'Very-long / Medium / Short-Chain Acyl-CoA Dehydrogenase', '사슬 길이별 아실-CoA 탈수소효소', 'β-산화 ①의 동위효소 3종'),
 ('ETF', 'Electron-Transferring Flavoprotein', '전자전달 플라보단백질', 'FADH₂ 전자를 유비퀴논(Q)으로'),
 ('Q', 'ubiquinone (coenzyme Q)', '유비퀴논', '호흡 사슬의 전자 운반체'),
 ('TFP', 'Trifunctional Protein', '삼기능 단백질', '긴 사슬 ②–④단계, 내막'),
 ('MFP', 'Multifunctional Protein', '다기능 단백질', '여러 활성이 한 단백질 (채널링)'),
 ('ACC (1 · 2)', 'Acetyl-CoA Carboxylase', '아세틸-CoA 카복실화효소', '말로닐-CoA 생성, 비오틴, 인산화 = OFF'),
 ('PC', 'Pyruvate Carboxylase', '피루브산 카복실화효소', '피루브산 → OAA, 비오틴'),
 ('PCC', 'Propionyl-CoA Carboxylase', '프로피오닐-CoA 카복실화효소', '홀수 지방산 C3 처리, 비오틴'),
 ('MCC', 'Methylcrotonyl-CoA Carboxylase', '메틸크로토닐-CoA 카복실화효소', '류신 분해, 비오틴'),
 ('B₁₂', 'cobalamin', '코발라민', '메틸말로닐-CoA 뮤테이스 조효소'),
 ('OAA', 'Oxaloacetate', '옥살로아세트산', '공복 땐 당신생으로 빠짐 → 케톤체 ↑'),
 ('TCA', 'Tricarboxylic Acid cycle', '시트르산 회로', '아세틸-CoA를 CO₂로'),
 ('HMG-CoA', 'β-Hydroxy-β-Methylglutaryl-CoA', 'HMG-CoA', '케톤체·콜레스테롤 합성 중간체'),
 ('VLCFA', 'Very-Long-Chain Fatty Acid', '매우 긴 사슬 지방산', '퍼옥시좀에서 먼저 짧게'),
 ('X-ALD', 'X-linked Adrenoleukodystrophy', 'X-연관 부신백질이영양증', 'VLCFA 축적 질환'),
 ('H₂O₂', 'hydrogen peroxide', '과산화수소', '퍼옥시좀 β-산화 부산물 (카탈레이스가 분해)'),
 ('P450', 'cytochrome P450', '사이토크롬 P450', 'ω-산화의 혼합기능 산화효소'),
 ('ER', 'Endoplasmic Reticulum', '소포체', 'ω-산화 장소'),
 ('LDL', 'Low-Density Lipoprotein', '저밀도 지단백질', '“나쁜” 콜레스테롤 운반체'),
 ('Δ (Δⁿ)', 'delta numbering', '이중결합 위치 표기', '카복실 탄소부터 n번째 탄소에 이중결합'),
]
ABBR_KEYS = {
 'TG (TAG)': r'\bTG\b|\bTAG\b', 'FA': r'\bFA\b', 'MAG · DAG': r'모노아실|다이아실', 'LPL': r'\bLPL\b', 'apoB-48 · apoC-II': r'apo', 'HSL': r'\bHSL\b', 'PKA': r'\bPKA\b',
 'cAMP': r'cAMP', 'PDE': r'\bPDE\b|포스포다이에스터레이스', 'Gs': r'\bGs\b', 'DHAP · GAP': r'DHAP|\bGAP\b', 'TPI': r'\bTPI\b', 'CoA (CoA-SH)': r'\bCoA\b',
 'Acyl-CoA': r'아실-CoA', 'CAT I · II (CPT1 · 2)': r'CAT|CPT', 'AMP · ADP · ATP': r'\b(ATP|ADP|AMP)\b', 'PPᵢ · Pᵢ': r'P[ᵢi]\b|Pᵢ', 'FAD · FADH₂': r'\bFAD',
 'NAD⁺ · NADH': r'\bNAD(?!P)', 'NADPH': r'NADP', 'VLCAD · MCAD · SCAD': r'[VMS]C?L?CAD|MCAD', 'ETF': r'\bETF\b', 'Q': r'\bQ\b|유비퀴논', 'TFP': r'\bTFP\b',
 'MFP': r'\bMFP\b', 'ACC (1 · 2)': r'\bACC', 'PC': r'\bPC\b', 'PCC': r'\bPCC\b', 'MCC': r'\bMCC\b', 'B₁₂': r'B₁₂|B12', 'OAA': r'\bOAA\b', 'TCA': r'\bTCA\b',
 'HMG-CoA': r'HMG', 'VLCFA': r'VLCFA', 'X-ALD': r'X-ALD', 'H₂O₂': r'H₂O₂', 'P450': r'P450', 'ER': r'\bER\b|소포체', 'LDL': r'\bLDL\b', 'Δ (Δⁿ)': r'Δ[⁰¹²³⁴⁵⁶⁷⁸⁹ⁿ]',
}

# ------------------------------------------------------------------ concept checks
CHECKS = [
 dict(id='C1', num='1', title='지방 저장 · 흡수 · 동원', sec='S1–S3', level=1,
  q='''<p><b>1.</b> (서술) 지방이 글리코겐보다 저장 연료로 유리한 이유 2가지는?</p>
<p><b>2.</b> (O/X) 담즙산염은 TG의 에스터 결합을 가수분해하는 효소이다.</p>
<p><b>3.</b> (빈칸) 모세혈관에서 킬로미크론의 TG를 분해하는 효소는 ( &nbsp;&nbsp; )이고, 이를 활성화하는 아포지단백질은 ( &nbsp;&nbsp;&nbsp; )이다.</p>
<p><b>4.</b> (순서) 글루카곤 → ( &nbsp;&nbsp; ) → ( &nbsp;&nbsp; ) → 페릴리핀·( &nbsp;&nbsp; ) 인산화 → TG 분해 → 지방산은 ( &nbsp;&nbsp; )에 실려 근육으로</p>
<p><b>5.</b> (O/X) 지방세포는 글리세롤 키나아제가 많아 글리세롤을 직접 재사용한다.</p>''',
  answer=chips('1. ① 더 환원됨(g당 에너지 ↑) ② 비극성(물 없음)', '2. <b>X</b> (유화제)', '3. <b>LPL</b> / <b>apoC-II</b>', '4. <b>cAMP · PKA · HSL · 알부민</b>', '5. <b>X</b> (간에 있음)'),
  explain=fig(fuel_bars(), '') + steps('1. 지방 38 kJ/g vs 탄수화물 17 kJ/g. 게다가 글리코겐은 무게 2배의 물을 끌고 다님.',
   '2. 담즙산염은 세제처럼 지방을 작은 미셀로 쪼개 리파아제가 일할 표면을 넓힐 뿐.',
   '5. 글리세롤은 혈액으로 나가 간에서 글리세롤 키나아제 → DHAP → GAP.') +
   key('TG → FA → TG → FA → TG: 막은 작게, 운반은 포장해서.')),
 dict(id='C2', num='2', title='활성화와 카르니틴 셔틀', sec='S4', level=2,
  q='''<p><b>1.</b> (빈칸) FA + CoA + ATP → 아실-CoA + ( &nbsp;&nbsp; ) + ( &nbsp;&nbsp; ). 이 반응 중간체는 ( &nbsp;&nbsp;&nbsp;&nbsp; )이다.</p>
<p><b>2.</b> (계산) 지방산 활성화에 드는 에너지는 ATP 몇 개 분? 이유는?</p>
<p><b>3.</b> (O/X) 아실-CoA는 미토콘드리아 내막 수송체로 직접 들어간다.</p>
<p><b>4.</b> (순서) 세포질 아실-CoA → ( &nbsp; : 외막 효소) → 아실-카르니틴 → 수송체 → ( &nbsp; : 내막 효소) → 기질 아실-CoA</p>
<p><b>5.</b> (판단) 탄소 수가 몇 개 이상이면 카르니틴 셔틀이 필요한가?</p>''',
  answer=chips('1. <b>AMP · PPᵢ</b> / <b>아실-아데닐산(아실-AMP)</b>', '2. <b>2개</b> — ATP → AMP + PPᵢ → 2Pᵢ', '3. <b>X</b>', '4. <b>CAT I → CAT II</b>', '5. <b>C14 이상</b>'),
  explain=fig(carnitine(), '') + steps('2. 인산무수물 결합 2개가 끊어짐 → AMP를 ATP로 되돌리려면 ATP 2개 분이 필요.',
   '3. CoA는 내막을 못 지남 → 아실기만 카르니틴에 실어 넘기고, 안에서 미토콘드리아 CoA에 다시 붙인다.') +
   warn('카르니틴 셔틀 결핍 → 긴 사슬 지방산을 못 태워 근육 경련·저혈당.', '임상')),
 dict(id='C3', num='3', title='β-산화 4단계', sec='S5–S6', level=1,
  q='''<p><b>1.</b> (순서) β-산화 한 바퀴의 4단계와 각 단계의 조효소(있으면)를 써라.</p>
<p><b>2.</b> (계산) 스테아르산(C18)은 몇 바퀴 돌고 아세틸-CoA 몇 개를 만드나? 라우르산(C12)은?</p>
<p><b>3.</b> (O/X) β-산화 ③단계의 탈수소효소는 D-이성질체에 특이적이다.</p>
<p><b>4.</b> (빈칸) 아실-CoA 탈수소효소의 FADH₂ 전자는 ( &nbsp;&nbsp; ) → ETF:유비퀴논 산화환원효소 → ( &nbsp; )로 넘어간다.</p>
<p><b>5.</b> (짝짓기) VLCAD · MCAD · SCAD ↔ C4–8, C4–14, C12–18</p>''',
  answer=chips('1. 탈수소(<b>FAD</b>) → 수화(H₂O) → 탈수소(<b>NAD⁺</b>) → 티올분해(<b>CoA</b>)', '2. C18: <b>8바퀴 · 9개</b> / C12: <b>5바퀴 · 6개</b>', '3. <b>X</b> (L형)', '4. <b>ETF</b> / <b>Q (유비퀴논)</b>', '5. VLCAD C12–18 · MCAD C4–14 · SCAD C4–8'),
  explain=fig(beta_cycle(), '') + steps('2. 바퀴 = n/2 − 1, 아세틸-CoA = n/2. 마지막 바퀴(C4)는 아세틸-CoA 2개.',
   '4. 복합체 I을 건너뛰므로 FADH₂는 NADH(2.5)보다 적은 1.5 ATP.') +
   tip('TCA의 숙신산 → 푸마르산 → 말산 → OAA와 같은 순서로 외우자.', '요령')),
 dict(id='C4', num='4', title='ATP 수지 계산', sec='S7', level=2,
  q='''<p><b>1.</b> (계산) 팔미토일-CoA(C16) 1개 → CO₂ + H₂O. ATP는? (FADH₂ 1.5, NADH 2.5, 아세틸-CoA 10)</p>
<p><b>2.</b> (계산) 유리 팔미트산이면 ATP는?</p>
<p><b>3.</b> (계산) 스테아로일-CoA(C18) 1개의 ATP 수율은?</p>
<p><b>4.</b> (계산) 미리스트산(C14, 유리 지방산) 1개의 ATP 수율은?</p>''',
  answer=chips('1. 7×1.5 + 7×2.5 + 8×10 = <b>108</b>', '2. 108 − 2 = <b>106</b>', '3. 8×1.5 + 8×2.5 + 9×10 = <b>122</b>', '4. 6×4 + 7×10 − 2 = <b>92</b>'),
  explain=fig(yield_bars(), '') + steps('한 바퀴 = FADH₂ 1 + NADH 1 = 1.5 + 2.5 = <b>4 ATP</b>. 아세틸-CoA 1개 = 10 ATP.',
   '3. C18: 8바퀴 × 4 = 32 + 9 × 10 = 90 → 122.', '4. C14: 6바퀴 × 4 = 24 + 7 × 10 = 70 → 94, 활성화 −2 → 92.') +
   key('공식: Cₙ 아실-CoA ATP = 4(n/2 − 1) + 10(n/2). 유리 지방산이면 −2.')),
 dict(id='C5', num='5', title='불포화 · 홀수 지방산', sec='S8–S9', level=2,
  q='''<p><b>1.</b> (O/X) 엔오일-CoA 수화효소는 cis-Δ³ 이중결합도 기질로 받는다.</p>
<p><b>2.</b> (계산) 올레오일-CoA(18:1 Δ⁹)의 ATP 수율은? (스테아로일-CoA = 122)</p>
<p><b>3.</b> (빈칸) 이중결합이 짝수 위치에 있으면 ( &nbsp;&nbsp;&nbsp;&nbsp; ) 환원효소가 추가로 필요하며, 전자 공여체는 ( &nbsp;&nbsp;&nbsp; )이다.</p>
<p><b>4.</b> (순서) 프로피오닐-CoA → ( &nbsp; , 조효소: &nbsp; ) → D-메틸말로닐-CoA → 에피머화 → L형 → ( &nbsp; , 조효소: &nbsp; ) → ( &nbsp;&nbsp; )</p>
<p><b>5.</b> (O/X) 홀수 탄소 지방산의 일부는 포도당이 될 수 있다.</p>''',
  answer=chips('1. <b>X</b> (trans-Δ²만)', '2. 122 − 1.5 = <b>120.5</b>', '3. <b>2,4-다이엔오일-CoA</b> / <b>NADPH</b>', '4. 카복실화효소(<b>비오틴</b>) → 뮤테이스(<b>B₁₂</b>) → <b>숙시닐-CoA</b>', '5. <b>O</b>'),
  explain=fig(odd_chain(), '') + steps('2. 이성질화효소가 cis-Δ³ → trans-Δ²로 바로 만들어 ①단계(FAD)를 건너뜀 → FADH₂ 1개(1.5 ATP) 손해.',
   '5. 숙시닐-CoA는 TCA 중간체를 순증가시켜 OAA → 포도당신생 가능. 짝수 지방산의 아세틸-CoA는 불가.') +
   warn('B₁₂ 결핍 → 메틸말로닐산혈증.', '임상')),
 dict(id='C6', num='6', title='β-산화의 조절', sec='S10–S11', level=2,
  q='''<p><b>1.</b> (빈칸) 지방산 산화의 핵심 조절 지점은 ( &nbsp;&nbsp;&nbsp; )이며, 이를 억제하는 물질은 ( &nbsp;&nbsp;&nbsp; )이다.</p>
<p><b>2.</b> (표 채우기) 식후: 인슐린 → ACC ( 인산화 / 탈인산화 ) → ACC ( ON / OFF ) → 말로닐-CoA ( ↑/↓ ) → β-산화 ( ↑/↓ )</p>
<p><b>3.</b> (짝짓기) [NADH]/[NAD⁺] ↑ · [아세틸-CoA] ↑ ↔ 티올레이스, β-하이드록시아실-CoA 탈수소효소</p>
<p><b>4.</b> (서술) ACC2 결손 쥐는 더 많이 먹는데도 지방이 적다. 이유는?</p>
<p><b>5.</b> (O/X) PC, ACC, PCC는 모두 비오틴을 조효소로 쓴다.</p>''',
  answer=chips('1. <b>CAT I</b> / <b>말로닐-CoA</b>', '2. <b>탈인산화 · ON · ↑ · ↓</b>', '3. NADH ↑ → <b>β-하이드록시아실-CoA 탈수소효소</b> · 아세틸-CoA ↑ → <b>티올레이스</b>', '4. 말로닐-CoA ↓ → CAT I 열림 → 지방 연소 ↑', '5. <b>O</b>'),
  explain=fig(malonyl_switch(), '') + steps('1. 지방산 합성 중(말로닐-CoA ↑)에 분해까지 하면 헛된 회로 → 입구를 닫는다.',
   '4. ACC2는 근육·심장에서 CAT I 조절용 말로닐-CoA를 만든다. 없으면 브레이크가 없다.') +
   warn('ACC: 인산화 = OFF (PKA). PDH와 같은 방향.', '함정')),
 dict(id='C7', num='7', title='퍼옥시좀 산화와 케톤체', sec='S12–S14', level=2,
  q='''<p><b>1.</b> (O/X) 퍼옥시좀 β-산화의 첫 단계에서 생긴 FADH₂의 전자는 호흡 사슬로 가서 ATP를 만든다.</p>
<p><b>2.</b> (짝짓기) 레프숨병 · 젤웨거 증후군 · MCAD 결핍 ↔ 피탄산 α-산화 결함, 퍼옥시좀 형성 결함, 중간 사슬 β-산화 결함</p>
<p><b>3.</b> (빈칸) 케톤체 3가지는 ( &nbsp;&nbsp;&nbsp; ), ( &nbsp;&nbsp;&nbsp;&nbsp; ), ( &nbsp; )이며, ( &nbsp; )에서 만들어진다.</p>
<p><b>4.</b> (서술) 간이 케톤체를 연료로 쓰지 못하는 이유는?</p>
<p><b>5.</b> (서술) 1형 당뇨 환자에게 케톤산증이 생기는 과정을 OAA를 넣어 설명하라.</p>''',
  answer=chips('1. <b>X</b> (O₂ → H₂O₂)', '2. 레프숨 = <b>α-산화</b> · 젤웨거 = <b>퍼옥시좀</b> · MCAD = <b>중간 사슬</b>', '3. <b>아세토아세트산 · β-하이드록시뷰티르산 · 아세톤</b> / <b>간 미토콘드리아</b>', '4. <b>β-케토아실-CoA 전이효소</b>가 없음', '5. 인슐린 ✕ → 지방 동원·β-산화 ↑ + OAA는 당신생으로 → 아세틸-CoA 과잉 → 케톤체 ↑↑'),
  explain=fig(ketone_liver(), '') + steps('1. 퍼옥시좀의 아실-CoA <b>산화효소</b>는 전자를 O₂에 직접 줘서 H₂O₂ (카탈레이스가 분해). 에너지는 열로.',
   '4. 간은 생산자, 심장·근육·뇌는 소비자 — 간이 자기가 만든 연료를 다 써 버리지 않게.',
   '5. 케톤체는 산(H⁺ 방출) → 혈액 pH ↓. 아세톤 때문에 날숨에서 과일 냄새.') +
   key('공복 간: OAA 부족 → 아세틸-CoA는 TCA 대신 케톤체로.')),
]
NO_STRIP = ('S15',)
CHECK_AFTER = {2: 'C1', 3: 'C2', 5: 'C3', 6: 'C4', 8: 'C5', 10: 'C6', 13: 'C7'}

if __name__ == '__main__':
    import exam17 as M
    examlib.render(M)
