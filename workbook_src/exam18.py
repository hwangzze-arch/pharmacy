# -*- coding: utf-8 -*-
"""18장 시험대비 요약노트.  python3 exam18.py → exam_ch18.pdf"""
import os, sys
os.environ['CH'] = '18'
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from helpers import *
import examlib
import ch18
from ch18 import urea_cycle, n_flow, gaa_cycle, pku_path

CH = 18
CH_TITLE = '아미노산 산화와 요소 생성'
FOOT = 'Lehninger 8e · Ch.18 아미노산 산화와 요소 생성 — 시험대비 요약노트'

_items = [i for i in ch18.ALL_ITEMS if i['level'] < 3]
WB = {i['id']: 6 + k for k, i in enumerate(_items)}
link = examlib.make_link(WB, CH)
page = examlib.make_page(link)


# ------------------------------------------------------------------ drawings
def overview():
    W, H = 560, 220
    b = arrowdef('ov', C['gray'])
    def box(x, y, w, s, col, sub=''):
        r = f'<rect x="{x-w/2}" y="{y-16}" width="{w}" height="32" rx="10" fill="white" stroke="{col}" stroke-width="2"/>' + T(x, y + 4 if not sub else y - 1, s, 11, col, weight=900)
        if sub:
            r += T(x, y + 11, sub, 9, C['gray'])
        return r
    def ar(x1, y1, x2, y2):
        return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{C["gray"]}" stroke-width="2" marker-end="url(#ov)"/>'
    b += box(100, 30, 160, '식이 · 세포 단백질', C['navy']) + ar(100, 46, 100, 76) + box(100, 94, 120, '아미노산', C['navy'])
    b += ar(150, 86, 250, 50) + box(330, 40, 150, 'NH₄⁺ (아미노기)', C['red'], '18.1 · 18.2')
    b += ar(150, 104, 250, 150) + box(330, 160, 150, '탄소 골격 (α-케토산)', C['green'], '18.3')
    b += ar(405, 40, 455, 40) + box(500, 40, 90, '요소', C['red'], '요소 회로')
    b += ar(405, 160, 450, 130) + box(500, 120, 100, 'TCA → CO₂', C['green'])
    b += ar(405, 160, 450, 190) + box(500, 196, 100, '포도당 · 케톤체', C['green'])
    b += f'<line x1="330" y1="58" x2="330" y2="140" stroke="{C["orange"]}" stroke-width="1.6" stroke-dasharray="4 3"/>' + T(338, 100, '아스파르트산 션트', 9.5, C['orange'], 'start', 700)
    return svg(W, H, b)


def zymogen():
    return vflow(['위: 가스트린 → 벽세포 HCl + 으뜸세포 펩시노겐', '낮은 pH: 펩시노겐 → 펩신 (단백질 → 큰 펩타이드)', '십이지장: 세크레틴 → 췌장 HCO₃⁻ (pH 7) · CCK → 효소원 분비',
                  '엔테로펩티데이스: 트립시노겐 → 트립신', '트립신 → 키모트립신 · 카복시펩티데이스 · 엘라스테이스 (+ 트립신 자신)', '융모: 아미노·카복시펩티데이스 → 아미노산 → 흡수'],
                 colors=[C['red'], C['red'], C['blue'], C['orange'], C['orange'], C['green']], box_h=24, gap=12, width=540, font=10.5, bw=510)


def gdh():
    return flow(['글루탐산', 'α-KG + NH₄⁺'], arrow_labels=['GDH · NAD(P)⁺ → NAD(P)H (▲ADP ⊗GTP)'], colors=[C['navy'], C['red']], box_h=40, width=520, font=11)


def gln_carry():
    return flow(['글루탐산 + NH₄⁺', '글루타민 (혈액)', '글루탐산 + NH₄⁺ (간)'], arrow_labels=['글루타민 합성효소 (ATP)', '글루타미네이스'],
                colors=[C['blue'], C['navy'], C['red']], box_h=40, width=540, font=10.5)


def entry_map():
    W, H = 560, 290
    b = arrowdef('em', C['gray'])
    b += f'<circle cx="300" cy="185" r="70" fill="none" stroke="{C["light"]}" stroke-width="12"/>' + T(300, 189, 'TCA 회로', 12, C['gray'], weight=900)
    def node(x, y, s, col):
        return f'<rect x="{x-56}" y="{y-14}" width="112" height="28" rx="14" fill="white" stroke="{col}" stroke-width="2"/>' + T(x, y + 4, s, 10.5, col, weight=900)
    pink, blue = C['red'], C['blue']
    b += node(300, 70, '아세틸-CoA', blue) + node(110, 70, '피루브산', pink) + node(490, 70, '아세토아세틸-CoA', blue)
    b += f'<line x1="168" y1="70" x2="240" y2="70" stroke="{C["gray"]}" stroke-width="2" marker-end="url(#em)"/><line x1="432" y1="70" x2="360" y2="70" stroke="{C["gray"]}" stroke-width="2" marker-end="url(#em)"/>'
    b += f'<line x1="300" y1="86" x2="300" y2="112" stroke="{C["gray"]}" stroke-width="2" marker-end="url(#em)"/>'
    b += T(110, 40, 'A · C · G · S · T · W', 11, pink, weight=900) + T(300, 40, 'I · L · T · W', 11, blue, weight=900) + T(490, 40, 'L · K · F · Y · W', 11, blue, weight=900)
    b += node(215, 140, 'OAA', pink) + node(385, 140, 'α-KG', pink) + node(385, 235, '숙시닐-CoA', pink) + node(215, 235, '푸마르산', pink)
    b += T(150, 144, 'N · D', 11, pink, 'end', 900) + T(450, 144, 'R · H · P · E · Q', 11, pink, 'start', 900)
    b += T(450, 239, 'I · M · T · V', 11, pink, 'start', 900) + T(150, 239, 'F · Y', 11, pink, 'end', 900)
    b += T(280, 280, '빨강 = 포도당생성 진입점 / 파랑 = 케톤생성 진입점', 10, C['gray'])
    return svg(W, H, b)


def thf_states():
    return bars([('N⁵-메틸-THF (–CH₃)', 1, C['blue'], '가장 환원'), ('N⁵,N¹⁰-메틸렌-THF (–CH₂–)', 2, C['purple'], '중간'),
                 ('N¹⁰-포밀 · 메테닐 · 포미미노 (–CHO 수준)', 3, C['red'], '가장 산화')], height=120, vmax=4, width=560)


def met_cycle():
    return vflow(['메티오닌 + ATP → adoMet (PPᵢ + Pᵢ 방출)', 'adoMet → 메틸전이효소 → R–CH₃ + S-아데노실호모시스테인', '→ 호모시스테인 (+ 아데노신)',
                  '호모시스테인 + N⁵-메틸-THF → 메티오닌 (메티오닌 합성효소, B₁₂)'],
                 colors=[C['navy'], C['orange'], C['gray'], C['green']], box_h=24, gap=14, width=540, font=10.5, bw=500)


def phe_tyr():
    return vflow(['페닐알라닌', '티로신', 'p-하이드록시페닐피루브산', '호모젠티스산', '말레일아세토아세트산 → 푸마릴아세토아세트산', '푸마르산 + 아세토아세트산'],
                 notes=['✕ PKU (페닐알라닌 수산화효소, THBP)', '✕ 티로신혈증 II (티로신 아미노전이효소)', '✕ 티로신혈증 III (p-HPP 이산소화효소)', '✕ 알캅톤뇨증 (호모젠티스산 이산소화효소)', '✕ 티로신혈증 I (푸마릴아세토아세테이스)'],
                 colors=[C['navy'], C['navy'], C['navy'], C['navy'], C['navy'], C['green']], box_h=24, gap=20, width=560, font=10.5, bw=250)


def b12_trap():
    return vflow(['B₁₂ 결핍', 'N⁵-메틸-THF 축적 (메틸 함정)', 'N⁵,N¹⁰-메틸렌-THF 고갈', '티미딘 → DNA 합성 ↓', '거대적혈모구 · 큰적혈구 (악성빈혈)'],
                 colors=[C['red'], C['orange'], C['orange'], C['orange'], C['red']], box_h=24, gap=12, width=520, font=10.5, bw=330)


# ------------------------------------------------------------------ summary pages
SUMMARY = []

SUMMARY.append(page('S1', '18장 큰 그림 — 질소는 버리고 탄소는 태운다', 'Overview · Slides 1–5, 13',
  '아미노산 = <b>아미노기(질소)</b> + <b>탄소 골격</b>. 질소는 독성이 있어 <b>요소</b>로 만들어 버리고(18.1–18.2), 탄소 골격은 TCA로 태우거나 포도당·케톤체로 바꾼다(18.3).',
  f'''<div class="grid2"><div class="card"><h4>📌 아미노산 이화 개요 (슬라이드 5)</h4><figure class="fig">{overview()}</figure>
 <p class="small">두 회로(요소 회로·TCA)는 <b>아스파르트산-아르기니노숙신산 션트</b>로 이어져 있다 (S8).</p></div>
<div><div class="card"><h4>📌 아미노산을 연료로 쓰는 3가지 상황 (슬라이드 4)</h4>{table(['상황', '왜?'], [['① 단백질 교체', '세포 단백질은 계속 분해·재합성. 남는 아미노산은 저장 못 해 태움'], ['② 고단백 식사', '필요 이상 먹은 아미노산은 연료로'], ['③ 기아 · 당뇨', '탄수화물을 못 쓰니 체단백질을 분해해 연료·포도당신생에']], cls='left')}
 <p class="small">육식동물은 에너지의 90%, 사람은 10–15%를 아미노산 산화에서 얻는다.</p></div>
 <div class="card" style="margin-top:3mm"><h4>📌 질소를 버리는 3가지 형태 (슬라이드 13)</h4>{table(['형태', '동물', '이유'], [['암모니아 (NH₄⁺) — <b>암모니아 배설형</b>', '수생 척추동물(물고기)', '물에 녹여 바로 희석'], ['<b>요소</b> — <b>요소 배설형</b>', '육상 척추동물(사람)', '독성 낮고 물에 잘 녹음'], ['<b>요산</b> — <b>요산 배설형</b>', '새 · 파충류', '물을 아끼려고 고체로']], cls='left')}</div></div></div>''',
  ('P3',)))

SUMMARY.append(page('S2', '18.1 식이 단백질의 소화', 'Digestion · Slides 6–12',
  '단백질은 <b>위(펩신) → 췌장 효소(트립신 등) → 소장 융모(펩티데이스)</b> 순서로 잘려 아미노산이 되어 흡수된다. 소화효소는 자기 몸을 먹지 않도록 <b>효소원(zymogen)</b>으로 만들어져 있다가 장 안에서 켜진다.',
  f'''<div class="grid2"><div class="card"><h4>📌 소화 흐름 (슬라이드 7–12)</h4><figure class="fig">{zymogen()}</figure></div>
<div><div class="card"><h4>📌 호르몬 3총사</h4>{table(['호르몬', '어디서 → 무엇을', '결과'], [['<b>가스트린</b>', '위 점막 → 벽세포·으뜸세포', 'HCl + 펩시노겐'], ['<b>세크레틴</b>', '십이지장 → 췌장', 'HCO₃⁻로 위산 중화 (pH 7)'], ['<b>CCK</b>', '십이지장 → 췌장 · 담낭', '효소원 분비 + 담즙 분비']], cls='left')}</div>
 <div class="card" style="margin-top:3mm"><h4>📌 효소원 → 활성 효소</h4>{table(['효소원', '활성형', '자르는 곳'], [['펩시노겐', '펩신 (낮은 pH)', '사슬 안쪽'], ['트립시노겐', '<b>트립신</b> (엔테로펩티데이스)', '사슬 안쪽'], ['키모트립시노겐', '키모트립신 (트립신)', '사슬 안쪽'], ['프로카복시펩티데이스', '카복시펩티데이스 (트립신)', 'C-말단에서 하나씩']], cls='left')}</div>
 {key('<b>트립신이 열쇠</b>: 엔테로펩티데이스가 첫 트립신을 만들면, 트립신이 나머지 효소원과 트립시노겐까지 연쇄로 켠다(자가촉매).')}
 {warn('-ogen, pro- = 아직 꺼진 효소원. 췌장 안에서 미리 켜지면 췌장이 스스로 녹는다(급성 췌장염).', '포인트')}</div></div>''',
  ()))

SUMMARY.append(page('S3', '아미노기 전이 — 모든 질소는 글루탐산으로', 'Transamination · PLP · Slides 14–16, 22–24, 52',
  '<b>아미노전이효소</b>는 아미노산의 –NH₃⁺를 <b>α-케토글루타르산</b>에 넘겨 <b>글루탐산</b>을 만든다. 20종의 질소가 일단 글루탐산 한 곳으로 모인다. 조효소는 <b>PLP</b>(비타민 B₆).',
  f'''<div class="formula">L-아미노산 + α-케토글루타르산 ⇌ α-케토산 + L-글루탐산 &nbsp;(아미노전이효소, PLP)</div>
<div class="grid2" style="margin-top:3mm"><div><div class="card"><h4>📌 대표 짝꿍 (슬라이드 22)</h4>{table(['효소', '다른 이름', '반응'], [['<b>ALT</b>', 'GPT', '알라닌 + α-KG ⇌ <b>피루브산</b> + 글루탐산'], ['<b>AST</b>', 'GOT', '아스파르트산 + α-KG ⇌ <b>OAA</b> + 글루탐산']], cls='left')}
 {table(['아미노산', '↔ α-케토산'], [['알라닌', '피루브산'], ['아스파르트산', '옥살로아세트산'], ['글루탐산', 'α-케토글루타르산'], ['페닐알라닌', '페닐피루브산']])}</div>
 {key('아미노기 전이는 <b>가역</b>이고 질소가 사라지지 않는다 — 질소를 “모으는” 단계일 뿐. 버리는 건 GDH(S5).')}</div>
<div><div class="card"><h4>📌 PLP — 핑퐁 운반체 (슬라이드 23–24)</h4>{table(['상태', '모양'], [['대기 (내부 알디민)', 'PLP 알데하이드 + 효소 <b>Lys</b> = 쉬프 염기'], ['반응 중 (외부 알디민)', 'PLP + 기질 아미노산'], ['아미노기를 받은 상태', '<b>피리독사민 인산</b> (PMP)']], cls='left')}
 <p>PLP는 α 탄소의 카바니온을 안정화(전자 싱크) → <b>아미노기 전이 · 라세미화 · 탈카복실화</b> 세 반응을 모두 돕는다.</p></div>
 {tip('PLP는 왕복 택배: 아미노산에서 아미노기를 받아(PMP) α-KG에 내려놓고(PLP) 다시 돌아온다 = 핑퐁 기전.', '비유')}</div></div>''',
  ('P1', 'P5', 'P9')))

SUMMARY.append(page('S4', '암모니아 운반 — 글루타민과 알라닌', 'Slides 17–19',
  'NH₄⁺는 독성이 있어 혈액에 그대로 못 싣는다. 대부분의 조직은 <b>글루타민</b>에, 근육은 <b>알라닌</b>에 실어 간으로 보낸다. 그래서 혈중 아미노산 중 이 둘이 가장 많다.',
  f'''<div class="grid2"><div><div class="card"><h4>📌 글루타민 — 범용 운반체 (슬라이드 19)</h4><figure class="fig">{gln_carry()}</figure>
 <p class="small">글루타민 합성효소: 글루탐산 + ATP → γ-글루타밀 인산 → + NH₄⁺ → 글루타민. 글루타민은 질소 <b>2개</b>를 나르고, 일부는 생합성(퓨린 등)에 쓰인다. 신장에서는 NH₄⁺를 소변으로 내보내 산을 배출한다.</p></div></div>
<div><div class="card"><h4>📌 알라닌 — 포도당-알라닌 회로 (슬라이드 17)</h4><figure class="fig">{gaa_cycle()}</figure></div>
 {key('근육은 일석이조: 질소도 버리고, 피루브산 탄소를 간에 보내 <b>포도당</b>으로 돌려받는다 (코리 회로의 질소 버전).')}</div></div>''',
  ('P3',)))

SUMMARY.append(page('S5', '암모니아의 독성과 산화적 탈아미노화', 'Slides 20–21',
  '간 미토콘드리아의 <b>글루탐산 탈수소효소(GDH)</b>가 글루탐산에서 NH₄⁺를 떼어 요소 회로로 보낸다. 이 NH₄⁺가 뇌에 쌓이면 <b>뇌부종 · 혼수</b>.',
  f'''<div class="grid2"><div class="card"><h4>📌 산화적 탈아미노화 (슬라이드 21)</h4><figure class="fig">{gdh()}</figure>
 {table(['특징', '내용'], [['장소', '<b>간</b> 미토콘드리아 기질'], ['조효소', 'NAD⁺ 또는 NADP⁺ (둘 다 쓰는 드문 효소)'], ['조절', '<b>ADP ▲</b> (에너지 부족) / <b>GTP ⊗</b> (에너지 충분)'], ['산물의 행방', 'NH₄⁺ → 요소 회로 / α-KG → TCA · 당신생']], cls='left')}
 {warn('GTP 억제가 사라진 GDH 돌연변이 → ATP ↑ → 인슐린 과다 + NH₄⁺ ↑ = 고인슐린증-고암모니아혈증 (풀이노트 문제 4).', '임상')}</div>
<div><div class="card"><h4>📌 암모니아는 왜 독인가? (슬라이드 20)</h4>{table(['기전', '결과'], [['NH₄⁺ ↑ → 별아교세포에서 글루탐산 + NH₄⁺ → <b>글루타민</b> 축적', '삼투압 ↑ → 물 유입 → <b>뇌부종</b> → 혼수'], ['<b>글루탐산</b> 고갈', '신경전달물질 글루탐산 · <b>GABA</b> 고갈']], cls='left')}</div>
 {key('뇌에는 요소 회로가 없다 → 암모니아를 글루타민으로 가두는 것 말고는 방법이 없다.')}
 {tip('간경변 환자의 간성 혼수 = 간이 요소를 못 만들어 암모니아가 뇌로.', '연결')}</div></div>''',
  ('P4',)))

SUMMARY.append(page('S6', 'ALT · AST — 조직 손상 지표', 'Slides 22, 35–36',
  'ALT·AST는 원래 <b>세포 안</b>에 있는 효소. 혈액에서 많이 나온다 = 세포막이 깨져 새어 나왔다 = <b>조직 손상</b>.',
  f'''<div class="grid2"><div class="card"><h4>📌 두 효소 비교</h4>{table(['', 'ALT (= GPT)', 'AST (= GOT)'], [['반응', '알라닌 ⇌ 피루브산', '아스파르트산 ⇌ OAA'], ['주로 있는 곳', '<b>간</b> (간 특이성 높음)', '간 · 심장 · 근육'], ['혈액 검사 이름', 'SGPT', 'SGOT']])}
 <p class="small">S = serum(혈청). SCK = 혈청 크레아틴 키네이스(근육·심근 손상).</p>
 {tip('ALT 측정법: ALT가 만든 피루브산을 과량의 LDH가 NADH로 젖산으로 바꾸게 하고, NADH(340 nm) 감소 속도를 잰다 = 짝지은 측정법 (풀이노트 문제 2).', '실험')}</div>
<div><div class="card"><h4>📌 언제 올라가나? (슬라이드 36)</h4>{table(['상황', '새어 나오는 효소'], [['<b>심근경색</b>', 'SCK, SGOT, SGPT (심장 세포)'], ['<b>간 손상</b> (CCl₄, CHCl₃, 간염, 알코올)', 'SGOT, SGPT (간세포)']], cls='left')}</div>
 {key('AST는 간 활성이 가장 높은 아미노전이효소 — 요소 회로 두 번째 질소인 아스파르트산을 대량 공급해야 하니까 (풀이노트 문제 9).')}</div></div>''',
  ('P2', 'P9')))

SUMMARY.append(page('S7', '18.2 요소 회로 5단계', 'Urea cycle · Slides 26–29',
  '간에서 NH₄⁺ + HCO₃⁻ + 아스파르트산으로 <b>요소</b>를 만든다. 앞 2단계는 <b>미토콘드리아</b>, 뒤 3단계는 <b>세포질</b>. 요소의 질소 하나는 NH₄⁺, 하나는 아스파르트산에서.',
  f'''<div class="grid2"><div class="card"><h4>📌 요소 회로 (슬라이드 27)</h4><figure class="fig">{urea_cycle()}</figure></div>
<div><div class="card"><h4>📌 5단계 효소</h4>{table(['#', '효소', '장소', '반응'], [
  ['①', '<b>CPS I</b> (카르바모일 인산 합성효소 I)', '미토', 'NH₄⁺ + HCO₃⁻ + <b>2ATP</b> → 카르바모일 인산 (첫 번째 N)'],
  ['②', 'OTC (오르니틴 트랜스카르바모일레이스)', '미토', '카르바모일 인산 + 오르니틴 → 시트룰린'],
  ['③', 'ASS (아르기니노숙신산 합성효소)', '세포질', '시트룰린 + <b>아스파르트산</b> + ATP → 아르기니노숙신산 + AMP + PPᵢ (두 번째 N)'],
  ['④', 'ASL (아르기니노숙시네이스)', '세포질', '→ 아르기닌 + <b>푸마르산</b>'],
  ['⑤', '아르기네이스', '세포질', '아르기닌 + H₂O → <b>요소</b> + 오르니틴']], cls='left')}</div>
 {tip('③의 기전: 시트룰린이 ATP로 활성화된 <b>시트룰릴-AMP</b>가 되고, 아스파르트산이 AMP를 밀어내며 붙는다 (슬라이드 29).', '기전')}
 {key('오르니틴은 회전목마 좌석 — 소모되지 않고 계속 재사용. 오르니틴(아르기닌)이 모자라면 회로가 멈춘다 (풀이노트 문제 7).')}</div></div>''',
  ('P7', 'P8')))

SUMMARY.append(page('S8', '두 회로의 연결 · 에너지 비용 · 조절', 'Slides 30–31, 37',
  '요소 회로의 <b>푸마르산</b>은 TCA로 들어가 말산 → OAA → (AST) → <b>아스파르트산</b>이 되어 다시 요소 회로에 질소를 공급한다 = <b>아스파르트산-아르기니노숙신산 션트</b>. 요소 회로는 <b>효소량</b>과 <b>N-아세틸글루탐산</b>으로 조절된다.',
  f'''<div class="grid2"><div><div class="card"><h4>📌 아스파르트산 션트 (슬라이드 30)</h4>{flow(['푸마르산', '말산', 'OAA', '아스파르트산'], arrow_labels=['푸마레이스', 'NAD⁺ → NADH', 'AST (글루탐산)'], colors=[C['green'], C['green'], C['blue'], C['orange']], box_h=36, width=520, font=10.5)}
 <p class="small">말산 탈수소효소에서 NADH 1개 → 약 2.5 ATP를 돌려받는다.</p></div>
 <div class="card" style="margin-top:3mm"><h4>📌 에너지 비용</h4>{table(['항목', 'ATP'], [['CPS I', '2 ATP → 2 ADP'], ['ASS', '1 ATP → AMP + PPᵢ (고에너지 결합 2개)'], ['<b>합계</b>', '<b>ATP 3개 = 고에너지 결합 4개</b>'], ['돌려받기', '션트의 NADH (+ GDH의 NADH)']], cls='left')}
 <p class="small">질소 1개당 ≈ ATP 2개 → 젖산(15 ATP) vs 알라닌(≈ 13 ATP) (풀이노트 문제 6).</p></div></div>
<div><div class="card"><h4>📌 조절 2단계 (슬라이드 31)</h4>{table(['수준', '내용'], [['① 장기 (효소 양)', '5개 효소 모두 <b>기아 · 초고단백 식사</b> 때 합성 ↑'], ['② 단기 (알로스테릭)', '<b>N-아세틸글루탐산(NAG)</b>이 <b>CPS I</b>을 활성화']], cls='left')}
 {flow(['아세틸-CoA + 글루탐산', 'N-아세틸글루탐산', 'CPS I ON'], arrow_labels=['NAG 합성효소 (▲ 아르기닌)', '알로스테릭 활성'], colors=[C['gray'], C['orange'], C['red']], box_h=36, width=520, font=10.5)}
 <p class="small">아미노산 분해 ↑ → 글루탐산 ↑ → NAG ↑ → 요소 회로 ↑. 아르기닌은 NAG 합성효소를 켠다.</p></div>
 {warn('CPS <b>I</b>(미토콘드리아, 요소 회로, NAG 필요) ≠ CPS <b>II</b>(세포질, 피리미딘 합성, 글루타민 사용).', '함정')}</div></div>''',
  ('P6', 'P8')))

SUMMARY.append(page('S9', '요소 회로 결함 · 치료 · 필수 아미노산', 'Slides 32–34',
  '요소 회로 효소 하나라도 망가지면 <b>고암모니아혈증</b>. 치료는 단백질 제한 + 질소를 <b>다른 길로 버리게</b> 하는 약. 반대로 단백질을 안 먹으면 <b>필수 아미노산</b> 결핍.',
  f'''<div class="grid2"><div><div class="card"><h4>📌 결핍 효소 → 질환 (슬라이드 32)</h4>{table(['결핍 효소', '질환'], [['CPS I', 'CPS I 결핍증'], ['OTC', 'OTC 결핍증 (가장 흔함, X-연관)'], ['ASS', '시트룰린혈증'], ['ASL', '아르기니노숙신산뇨증'], ['아르기네이스', '아르기닌혈증']])}
 <p class="small">증상 = 암모니아 독성: 기면, 구토, 경련, 뇌부종, 혼수. 신생아기에 치명적.</p></div></div>
<div><div class="card"><h4>📌 고암모니아혈증 치료 (슬라이드 33)</h4>{table(['약', '결합 상대', '배설 형태', '버리는 N'], [['<b>벤조산</b>', '글리신', '히푸르산', '1개'], ['<b>페닐뷰티르산</b> (β-산화 → 페닐아세트산)', '<b>글루타민</b>', '페닐아세틸글루타민', '<b>2개</b>']], cls='left')}
 <p class="small">+ 단백질 제한, 아르기닌 보충(오르니틴 공급), 카르바모일 글루탐산(NAG 유사체 → CPS I 활성).</p></div>
 <div class="card" style="margin-top:3mm"><h4>📌 필수 아미노산 9개 (슬라이드 34)</h4><div class="formula">H I L K M F T W V</div>
 <p class="small">히스티딘 · 아이소류신 · 류신 · 라이신 · 메티오닌 · 페닐알라닌 · 트레오닌 · 트립토판 · 발린. 성장기엔 아르기닌도 준필수.</p>
 {warn('젤라틴(콜라겐) “액상 단백질” 다이어트 = <b>트립토판 0</b> → 필수 아미노산 결핍 → 체단백 분해 → 사망 사례 (풀이노트 문제 10).', '시험')}</div></div></div>''',
  ('P7', 'P10')))

SUMMARY.append(page('S10', '18.3 탄소 골격의 7개 진입점', 'Ketogenic & glucogenic · Slides 39–40, 48 · ’22 약사국시',
  '20개 아미노산의 탄소 골격은 결국 <b>7가지 중간체</b>로 들어간다. 피루브산·TCA 중간체로 가면 <b>포도당생성</b>, 아세틸-CoA·아세토아세틸-CoA로 가면 <b>케톤생성</b>.',
  f'''<div class="grid2"><div class="card"><h4>📌 진입점 지도 (슬라이드 40)</h4><figure class="fig">{entry_map()}</figure></div>
<div><div class="card"><h4>📌 묶음으로 외우기</h4>{table(['진입점', '아미노산', '개수'], [
  ['피루브산', '<b>A C G S T W</b>', '6'], ['α-케토글루타르산', '<b>P R H E Q</b>', '5'], ['숙시닐-CoA', '<b>I M T V</b>', '4'], ['푸마르산', '<b>F Y</b>', '2'], ['옥살로아세트산', '<b>N D</b>', '2'],
  ['아세틸-CoA', '<b>I L T W</b>', '4'], ['아세토아세틸-CoA', '<b>L K F Y W</b>', '5']], cls='left')}</div>
 {key('<b>오직 케톤생성 = 류신(L) · 라이신(K)</b>. 둘 다(케톤 + 포도당) = F · Y · W · I · T. 나머지 13개는 오직 포도당생성.')}
 {warn('한 아미노산이 여러 진입점에 나오는 건 골격이 <b>쪼개져</b> 여러 곳으로 가기 때문 (예: 티로신 → 푸마르산 + 아세토아세트산).', '함정')}</div></div>''',
  ('P11',)))

SUMMARY.append(page('S11', '진입점별 경로 상세', 'Slides 41–47, 49',
  '각 진입점으로 가는 길의 <b>핵심 효소·보조인자</b>만 골라 정리. 특히 B₁₂(숙시닐-CoA 길)와 THBP(페닐알라닌 길), PLP(세린·트레오닌 길)를 기억.',
  f'''<div class="grid2"><div class="card">{table(['진입점', '경로 요점', '보조인자'], [
  ['α-KG (PRHEQ)', '아르기닌 → (아르기네이스) 오르니틴 → 글루탐산 세미알데하이드 → <b>글루탐산</b>; 프롤린도 같은 곳으로; 히스티딘 → (THF) → 글루탐산', 'THF (His)'],
  ['숙시닐-CoA (IMTV)', 'Met → 호모시스테인 → α-케토뷰티르산; Thr → (탈수화효소) α-케토뷰티르산 → <b>프로피오닐-CoA</b> → 메틸말로닐-CoA → 숙시닐-CoA', 'PLP, 비오틴, <b>B₁₂</b>'],
  ['푸마르산 (FY)', 'Phe → (수산화효소) Tyr → … → <b>푸마르산 + 아세토아세트산</b>', '<b>THBP</b>'],
  ['OAA (ND)', '아스파라긴 → (아스파라지네이스) 아스파르트산 → (AST) OAA', 'PLP'],
  ['피루브산 (ACGSTW)', '세린 → (세린 탈수화효소) 피루브산; 글리신 ⇌ 세린 (SHMT); 트레오닌 → 글리신 + 아세틸-CoA', 'PLP, THF'],
  ['아세틸-CoA (LWFYKI)', '류신 → 아세토아세트산 + 아세틸-CoA; 라이신·트립토판 → α-케토아디프산 → 아세토아세틸-CoA', '—']], cls='left')}</div>
<div><div class="card"><h4>📌 트립토판은 재료 창고 (슬라이드 49)</h4>{table(['산물', '역할'], [['나이아신(B₃) → NAD⁺·NADP⁺', '결핍 시 <b>펠라그라</b> (피부염·설사·치매)'], ['세로토닌 → 멜라토닌', '신경전달물질 · 수면 (SSRI 표적)'], ['인돌아세트산 (옥신)', '식물 생장 호르몬']], cls='left')}</div>
 {tip('<b>L-아스파라지네이스</b> = 급성 림프모구 백혈병(ALL) 치료제. 백혈병 세포는 아스파라긴을 못 만들어 혈중 아스파라긴에 의존 → 혈중 아스파라긴을 없애 굶긴다.', '약학')}
 {key('트레오닌은 세 갈래(→ 숙시닐-CoA / 글리신 + 아세틸-CoA / 피루브산)라 케톤·포도당 둘 다.')}</div></div>''',
  ('P11',)))

SUMMARY.append(page('S12', '아미노산 이화의 보조인자', 'Enzyme cofactors · Slides 50–58',
  '네 종류: <b>PLP</b>(아미노기 전이), <b>1탄소 운반체</b>(비오틴 · THF · adoMet), <b>THBP</b>(산화), <b>B₁₂</b>(기 전달). 1탄소 운반체는 옮기는 탄소의 <b>산화 상태</b>로 구분한다.',
  f'''<div class="grid2"><div><div class="card"><h4>📌 1탄소 운반체 3총사 (슬라이드 53)</h4>{table(['보조인자', '옮기는 것', '산화 상태'], [['<b>비오틴</b>', 'CO₂', '가장 산화'], ['<b>THF</b> (엽산 B₉)', '메틸 · 메틸렌 · 포밀 · 메테닐 · 포미미노', '여러 단계'], ['<b>adoMet</b>', '메틸 (–CH₃)', '가장 환원, 가장 강력']], cls='left')}
 <figure class="fig">{thf_states()}</figure><p class="small">THF 위의 1탄소는 서로 산화·환원되며 바뀐다. 단, N⁵-메틸-THF → 메틸렌-THF는 거의 안 되돌아간다(메틸 함정, S13).</p></div>
 {tip('세린 ⇌ 글리신 (SHMT): PLP가 세린의 Cα를 붙잡고, THF가 하이드록시메틸을 받아 N⁵,N¹⁰-메틸렌-THF. 글리신 절단효소도 메틸렌-THF를 만든다 (슬라이드 55).', 'PLP+THF')}</div>
<div><div class="card"><h4>📌 활성 메틸 회로 — adoMet (슬라이드 57)</h4><figure class="fig">{met_cycle()}</figure>
 <p class="small">adoMet의 황은 양전하(설포늄) → 메틸기를 쉽게 내준다. ATP의 인산 3개를 모두 떼어 내며 만든다.</p></div>
 <div class="card" style="margin-top:3mm"><h4>📌 THBP — 페닐알라닌 수산화 (슬라이드 58)</h4><p class="small">Phe + O₂ + <b>테트라하이드로비오프테린</b> → Tyr + H₂O + 다이하이드로비오프테린 → (NADH, 환원효소) 재생. O₂ 원자 하나는 –OH, 하나는 물 = <b>혼합기능 산화효소</b>.</p></div></div></div>''',
  ('P12',)))

SUMMARY.append(page('S13', '조효소 B₁₂ — 자리바꿈과 메틸 함정', 'Slides 59–60, 69, 72',
  'B₁₂는 코린 고리 중심의 <b>코발트</b>에 5′-데옥시아데노신이 붙은 분자. <b>Co–C 결합</b>이 끊어져 라디칼을 만들고, 이웃한 두 탄소의 <b>H와 X를 맞바꾼다</b>. 사람에서 B₁₂ 효소는 단 둘.',
  f'''<div class="grid2"><div><div class="card"><h4>📌 B₁₂가 필요한 두 효소</h4>{table(['효소', '반응', '막히면'], [['<b>메틸말로닐-CoA 뮤테이스</b>', 'L-메틸말로닐-CoA → 숙시닐-CoA', '<b>메틸말론산</b> ↑ (IMTV · 홀수 지방산)'], ['<b>메티오닌 합성효소</b>', '호모시스테인 + N⁵-메틸-THF → 메티오닌 + THF', '<b>호모시스테인</b> ↑ + 메틸 함정']], cls='left')}
 <div class="formula" style="margin-top:2mm">–C(H)–C(X)– ⇌ –C(X)–C(H)– &nbsp;(B₁₂ 자리바꿈)</div>
 <p class="small">라디칼 기전 (슬라이드 72): Co–C 균일 분해 → 5′-데옥시아데노실 라디칼이 기질 H를 뽑음 → 기질 라디칼 재배열 → H 반환.</p></div>
 {tip('Co–C 결합 = 자연에서 유일하게 알려진 금속–탄소 결합.', '덤')}</div>
<div><div class="card"><h4>📌 악성빈혈 (슬라이드 69)</h4><figure class="fig">{b12_trap()}</figure></div>
 {table(['원인', '해결'], [['비건 식단 (B₁₂는 동물성 식품에만)', '보충제'], ['내인자·수용체 결함 (흡수 불가)', '<b>근육 주사</b> (먹어도 소용없음)']], cls='left')}
 {key('호모시스테인 ↑ + 메틸말론산 ↑ 동시 = B₁₂ 결핍의 지문 (풀이노트 문제 14).')}</div></div>''',
  ('P13', 'P14', 'P15')))

SUMMARY.append(page('S14', '아미노산 이화의 유전 질환', 'Slides 61–68, 70 · ’22 약사국시',
  '원리 하나: <b>막힌 곳 앞은 쌓이고, 뒤는 모자란다</b>. 증상은 대부분 쌓인 물질의 독성. 대부분 <b>식이 조절</b>로 치료한다.',
  f'''<div class="grid2"><div class="card"><h4>📌 페닐알라닌 · 티로신 길의 막힌 곳 (슬라이드 64)</h4><figure class="fig">{phe_tyr()}</figure>
 <p class="small">PKU에서는 Phe가 옆길로 넘쳐 <b>페닐피루브산 · 페닐젖산 · 페닐아세트산</b>이 소변에 (슬라이드 66). 치료: 저Phe 식이, 티로신 보충.</p></div>
<div><div class="card"><h4>📌 질환 표 (표 18-2)</h4>{table(['질환', '결핍 효소', '특징'], [
  ['<b>PKU</b>', '페닐알라닌 수산화효소', '뇌 발달 장애, 흰 피부·머리'], ['<b>알캅톤뇨증</b>', '호모젠티스산 이산소화효소', '검은 소변, 관절염'],
  ['<b>백색증</b> (’22 약시)', '<b>티로시네이스</b>', '멜라닌 없음'], ['<b>단풍당뇨증</b> (MSUD)', '가지사슬 α-케토산 탈수소효소', 'Val·Ile·Leu α-케토산, 단풍시럽 냄새'],
  ['<b>메틸말론산혈증</b>', '메틸말로닐-CoA 뮤테이스 / B₁₂', '메틸말론산 축적'], ['<b>비케톤성 고글리신혈증</b>', '글리신 절단효소', '중증 지적장애']], cls='left')}</div>
 {tip('가지사슬 아미노산(V·I·L)은 다른 아미노산과 달리 <b>간 밖(근육)</b>에서 먼저 분해된다. MSUD는 간 이식으로 치료하기도 (풀이노트 문제 21).', '연결')}
 {warn('고글리신혈증(hyperglycinemia) ≠ 고혈당(hyperglycemia). 이름만 비슷.', '함정')}</div></div>''',
  ('P12', 'P21')))

SUMMARY.append(page('S15', '18장 한 장 요약 + 시험 직전 체크리스트', 'Summary · Slides 25, 37, 71',
  '세 개의 요약 슬라이드를 숫자·효소 이름과 함께 한 장으로. (약어는 바로 뒤 총정리 참고)',
  f'''<div class="grid3">
 <div class="card"><h4>① 아미노기의 운명 (18.1)</h4><ul style="font-size:.95em"><li>소화: 펩신 → 트립신(엔테로펩티데이스가 켬) → 펩티데이스</li><li>아미노기 전이: PLP, 질소 → 글루탐산</li><li>ALT(GPT)·AST(GOT) = 조직 손상 지표</li><li>운반: 글루타민(범용), 알라닌(근육)</li><li>GDH: 간 미토, NAD(P)⁺, ADP ▲ GTP ⊗</li><li>NH₄⁺ 독성: 뇌부종, 글루탐산·GABA ↓</li></ul></div>
 <div class="card"><h4>② 요소 회로 (18.2)</h4><ul style="font-size:.95em"><li>미토: CPS I → OTC / 세포질: ASS → ASL → 아르기네이스</li><li>N: NH₄⁺ + 아스파르트산, C: HCO₃⁻</li><li>비용: 3 ATP = 고에너지 결합 4개</li><li>아스파르트산 션트로 TCA와 연결</li><li>조절: 효소 양 + NAG → CPS I</li><li>결함 → 고암모니아혈증 → 벤조산·페닐뷰티르산</li></ul></div>
 <div class="card"><h4>③ 탄소 골격 (18.3)</h4><ul style="font-size:.95em"><li>7개 진입점, 오직 케톤 = L · K</li><li>PLP · 비오틴 · THF · adoMet · THBP · B₁₂</li><li>B₁₂ 효소 2개: 뮤테이스, 메티오닌 합성효소</li><li>PKU · 알캅톤뇨증 · 백색증 · MSUD</li><li>V·I·L은 간 밖에서 분해</li><li>Trp → 나이아신 · 세로토닌</li></ul></div>
</div>
<div class="grid2" style="margin-top:3mm"><div class="card"><h4>🔢 꼭 외울 묶음</h4><div class="tiles" style="grid-template-columns:repeat(3,1fr)">
 <div><b>필수 AA</b><span>HILKMFTWV</span><small>9개</small></div><div><b>오직 케톤</b><span>L · K</span><small>류신 · 라이신</small></div><div><b>요소 비용</b><span>3 ATP</span><small>고에너지 결합 4</small></div>
 <div><b>피루브산</b><span>ACGSTW</span><small>6개</small></div><div><b>α-KG</b><span>PRHEQ</span><small>5개</small></div><div><b>숙시닐-CoA</b><span>IMTV</span><small>4개</small></div></div></div>
 <div class="card"><h4>⚠️ 단골 함정</h4><ol style="margin:.2em 0;padding-left:1.3em;font-size:.95em"><li>아미노기 전이는 질소를 모을 뿐, 버리는 건 GDH</li><li>CPS I(요소, 미토, NAG) ≠ CPS II(피리미딘)</li><li>요소 회로 앞 2단계만 미토콘드리아</li><li>뇌에는 요소 회로가 없다</li><li>B₁₂ 결핍: 호모시스테인 + 메틸말론산 둘 다 ↑</li><li>고글리신혈증 ≠ 고혈당</li></ol></div></div>''',
  ()))

MAPROWS = [['S1–S6 아미노기의 운명', '문제 1·2·3·4·5·9'], ['S7–S9 요소 회로', '문제 6·7·8·10'], ['S10–S11 탄소 골격', '문제 11'], ['S12–S14 보조인자 · 유전 질환', '문제 12·13·14·15·21']]

# ------------------------------------------------------------------ glossary
GLOSS = [
 ('AA', 'Amino Acid', '아미노산', '아미노기 + 탄소 골격'),
 ('NH₄⁺', 'ammonium ion', '암모늄 이온', '독성 질소, 요소로 바꿔 배설'),
 ('α-KG', 'α-Ketoglutarate', 'α-케토글루타르산', '아미노기를 받아 글루탐산이 됨'),
 ('OAA', 'Oxaloacetate', '옥살로아세트산', '아스파르트산의 짝 α-케토산'),
 ('PLP', 'Pyridoxal Phosphate', '피리독살 인산', 'B₆ 유래, 아미노기 전이 조효소'),
 ('PMP', 'Pyridoxamine Phosphate', '피리독사민 인산', '아미노기를 받은 PLP'),
 ('B₆ · B₉ · B₁₂', 'Vitamin B6 · B9 (folate) · B12 (cobalamin)', '피리독신 · 엽산 · 코발라민', 'PLP · THF · 조효소 B₁₂의 재료'),
 ('ALT (GPT)', 'Alanine Aminotransferase (Glutamate-Pyruvate Transaminase)', '알라닌 아미노전이효소', '알라닌 ⇌ 피루브산, 간 손상 지표'),
 ('AST (GOT)', 'Aspartate Aminotransferase (Glutamate-Oxaloacetate Transaminase)', '아스파르트산 아미노전이효소', '아스파르트산 ⇌ OAA, 간·심장 지표'),
 ('SGOT · SGPT · SCK', 'Serum GOT · GPT · Creatine Kinase', '혈청 GOT · GPT · 크레아틴 키네이스', '혈액으로 샌 세포 효소 = 손상'),
 ('LDH', 'Lactate Dehydrogenase', '젖산 탈수소효소', 'ALT 짝지은 측정법에 사용'),
 ('GDH', 'Glutamate Dehydrogenase', '글루탐산 탈수소효소', '글루탐산 → α-KG + NH₄⁺, ADP ▲ GTP ⊗'),
 ('NAD(P)⁺ · NAD(P)H', 'Nicotinamide Adenine Dinucleotide (Phosphate)', '니코틴아마이드 아데닌 다이뉴클레오타이드(인산)', 'GDH는 둘 다 사용'),
 ('ATP · ADP · AMP · GTP', 'Adenosine/Guanosine phosphates', '아데노신·구아노신 인산', 'GDH 조절, 요소 회로 에너지'),
 ('PPᵢ · Pᵢ', '(inorganic) Pyrophosphate · Phosphate', '피로인산 · 무기 인산', 'ASS에서 PPᵢ 방출'),
 ('GABA', 'γ-Aminobutyric acid', 'γ-아미노뷰티르산', '억제성 신경전달물질, 고암모니아 시 고갈'),
 ('CCK', 'Cholecystokinin', '콜레시스토키닌', '췌장 효소원 + 담즙 분비'),
 ('HCl', 'hydrochloric acid', '염산', '벽세포 분비, 단백질 변성'),
 ('CPS I · II', 'Carbamoyl Phosphate Synthetase I · II', '카르바모일 인산 합성효소', 'I = 요소 회로(미토, NAG) / II = 피리미딘'),
 ('OTC', 'Ornithine Transcarbamoylase', '오르니틴 트랜스카르바모일레이스', '② 시트룰린 생성, 결핍 가장 흔함'),
 ('ASS', 'Argininosuccinate Synthetase', '아르기니노숙신산 합성효소', '③ 아스파르트산 결합 (ATP → AMP)'),
 ('ASL', 'Argininosuccinate Lyase (argininosuccinase)', '아르기니노숙시네이스', '④ 아르기닌 + 푸마르산'),
 ('NAG', 'N-Acetylglutamate', 'N-아세틸글루탐산', 'CPS I 알로스테릭 활성화제'),
 ('HCO₃⁻', 'bicarbonate', '중탄산 이온', '요소의 탄소, 위산 중화'),
 ('TCA', 'Tricarboxylic Acid cycle', '시트르산 회로', '푸마르산 → OAA로 요소 회로와 연결'),
 ('CoA', 'Coenzyme A', '조효소 A', '아세틸·숙시닐·프로피오닐-CoA'),
 ('THF (H₄folate)', 'Tetrahydrofolate', '테트라하이드로엽산', '1탄소기(메틸·메틸렌·포밀) 운반'),
 ('adoMet (SAM)', 'S-Adenosylmethionine', 'S-아데노실메티오닌', '가장 강력한 메틸 공여체'),
 ('THBP (BH₄)', 'Tetrahydrobiopterin', '테트라하이드로비오프테린', '페닐알라닌 수산화효소 보조인자'),
 ('SHMT', 'Serine Hydroxymethyltransferase', '세린 하이드록시메틸전이효소', '세린 ⇌ 글리신 (PLP + THF)'),
 ('PKU', 'Phenylketonuria', '페닐케톤뇨증', '페닐알라닌 수산화효소 결핍'),
 ('MSUD', 'Maple Syrup Urine Disease', '단풍당뇨증', '가지사슬 α-케토산 탈수소효소 결핍'),
 ('BCAA · BCKDH', 'Branched-Chain Amino Acid · α-Keto acid Dehydrogenase', '가지사슬 아미노산 · α-케토산 탈수소효소', 'V·I·L, 간 밖에서 먼저 분해'),
 ('NKH', 'Nonketotic Hyperglycinemia', '비케톤성 고글리신혈증', '글리신 절단효소 결함'),
 ('IF', 'Intrinsic Factor', '내인자', 'B₁₂ 흡수에 필수 (위 벽세포)'),
 ('ALL', 'Acute Lymphoblastic Leukemia', '급성 림프모구 백혈병', 'L-아스파라지네이스로 치료'),
 ('SSRI', 'Selective Serotonin Reuptake Inhibitor', '선택적 세로토닌 재흡수 억제제', '세로토닌(Trp 유래) 표적 항우울제'),
 ('HILKMFTWV', 'essential amino acids', '필수 아미노산 9개', 'His Ile Leu Lys Met Phe Thr Trp Val'),
]
ABBR_KEYS = {
 'AA': r'\bAA\b', 'NH₄⁺': r'NH₄', 'α-KG': r'α-KG', 'OAA': r'\bOAA\b', 'PLP': r'\bPLP\b', 'PMP': r'\bPMP\b|피리독사민', 'B₆ · B₉ · B₁₂': r'B₆|B₉|B₁₂',
 'ALT (GPT)': r'\bALT\b|\bGPT\b', 'AST (GOT)': r'\bAST\b|\bGOT\b', 'SGOT · SGPT · SCK': r'SGOT|SGPT|SCK', 'LDH': r'\bLDH\b', 'GDH': r'\bGDH\b',
 'NAD(P)⁺ · NAD(P)H': r'\bNAD', 'ATP · ADP · AMP · GTP': r'\b(ATP|ADP|AMP|GTP)\b', 'PPᵢ · Pᵢ': r'PPᵢ|Pᵢ', 'GABA': r'GABA', 'CCK': r'\bCCK\b', 'HCl': r'\bHCl\b',
 'CPS I · II': r'\bCPS\b', 'OTC': r'\bOTC\b', 'ASS': r'\bASS\b', 'ASL': r'\bASL\b', 'NAG': r'\bNAG\b|N-아세틸글루탐산', 'HCO₃⁻': r'HCO₃', 'TCA': r'\bTCA\b',
 'CoA': r'CoA', 'THF (H₄folate)': r'\bTHF\b', 'adoMet (SAM)': r'adoMet', 'THBP (BH₄)': r'THBP|비오프테린', 'SHMT': r'SHMT', 'PKU': r'\bPKU\b', 'MSUD': r'MSUD|단풍당뇨',
 'BCAA · BCKDH': r'BCAA|BCKDH|가지사슬', 'NKH': r'고글리신혈증', 'IF': r'내인자', 'ALL': r'\bALL\b', 'SSRI': r'SSRI', 'HILKMFTWV': r'HILKMFTWV|필수 아미노산',
}

# ------------------------------------------------------------------ concept checks
CHECKS = [
 dict(id='C1', num='1', title='소화와 아미노기 전이', sec='S1–S3', level=1,
  q='''<p><b>1.</b> (짝짓기) 가스트린 · 세크레틴 · CCK ↔ 췌장 HCO₃⁻ 분비, 위산·펩시노겐 분비, 췌장 효소원·담즙 분비</p>
<p><b>2.</b> (빈칸) 트립시노겐을 처음 트립신으로 바꾸는 효소는 ( &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; )이고, 그 뒤엔 ( &nbsp;&nbsp; )이 나머지 효소원을 활성화한다.</p>
<p><b>3.</b> (빈칸) 아미노기 전이의 질소 수용체는 ( &nbsp;&nbsp;&nbsp; )이고 산물은 ( &nbsp;&nbsp; ), 조효소는 ( &nbsp; , 비타민 &nbsp; )이다.</p>
<p><b>4.</b> (쓰기) 알라닌, 아스파르트산, 페닐알라닌이 아미노기 전이 후 되는 α-케토산은?</p>
<p><b>5.</b> (짝짓기) 물고기 · 사람 · 새 ↔ 요소 배설형, 요산 배설형, 암모니아 배설형</p>''',
  answer=chips('1. 가스트린 → 위산·펩시노겐 · 세크레틴 → HCO₃⁻ · CCK → 효소원·담즙', '2. <b>엔테로펩티데이스</b> / <b>트립신</b>', '3. <b>α-KG</b> / <b>글루탐산</b> / <b>PLP, B₆</b>', '4. <b>피루브산 · OAA · 페닐피루브산</b>', '5. 물고기 = 암모니아 · 사람 = 요소 · 새 = 요산'),
  explain=fig(zymogen(), '') + steps('2. 트립신은 자기 효소원까지 켜는 자가촉매 → 연쇄 증폭.', '3. 20종의 질소가 먼저 글루탐산으로 모인다. 아미노기 전이는 가역.',
   '5. 물이 풍부할수록 독한 암모니아를 그대로, 물이 귀할수록 고체 요산으로.') + key('아미노산 ↔ α-케토산 짝: 알라닌–피루브산, 아스파르트산–OAA, 글루탐산–α-KG.')),
 dict(id='C2', num='2', title='암모니아 운반 · 독성 · GDH', sec='S4–S6', level=2,
  q='''<p><b>1.</b> (서술) 혈장 아미노산 중 알라닌과 글루타민이 특히 많은 이유는?</p>
<p><b>2.</b> (순서) 근육 단백질의 질소 → 글루탐산 → ( &nbsp;&nbsp; , 효소 &nbsp;&nbsp; ) → 혈액 → 간 → 피루브산은 ( &nbsp;&nbsp;&nbsp; ), 질소는 ( &nbsp;&nbsp; )</p>
<p><b>3.</b> (빈칸) GDH는 간 ( &nbsp;&nbsp;&nbsp;&nbsp; )에 있고, ( &nbsp; )로 활성화, ( &nbsp; )로 억제된다.</p>
<p><b>4.</b> (서술) 암모니아가 뇌에 독인 이유 2가지는?</p>
<p><b>5.</b> (O/X) 혈중 ALT가 높다면 간세포 손상을 의심할 수 있다.</p>''',
  answer=chips('1. 말초 조직의 질소를 간으로 나르는 <b>운반체</b>', '2. <b>알라닌 (ALT)</b> / <b>포도당신생</b> / <b>요소</b>', '3. <b>미토콘드리아</b> / <b>ADP</b> / <b>GTP</b>', '4. ① 글루타민 축적 → 뇌부종 ② 글루탐산·GABA 고갈', '5. <b>O</b>'),
  explain=fig(gaa_cycle(), '') + steps('1. 글루타민 = 범용(질소 2개), 알라닌 = 근육 전용(포도당-알라닌 회로).', '4. 뇌는 요소 회로가 없어 NH₄⁺를 글루타민에 가둘 수밖에 없다.',
   '5. ALT는 세포 안 효소 → 혈액에 나왔다 = 세포가 깨졌다. 간 특이성이 AST보다 높다.') + warn('GDH의 GTP 억제가 사라지면 ATP ↑ → 인슐린 과다 → 저혈당 (+ 고암모니아혈증).', '임상')),
 dict(id='C3', num='3', title='요소 회로', sec='S7–S8', level=2,
  q='''<p><b>1.</b> (순서) 요소 회로 5단계 효소를 순서대로 쓰고, 미토콘드리아/세포질을 구분하라.</p>
<p><b>2.</b> (빈칸) 요소의 질소 2개는 ( &nbsp;&nbsp; )와 ( &nbsp;&nbsp;&nbsp;&nbsp; )에서, 탄소는 ( &nbsp;&nbsp; )에서 온다.</p>
<p><b>3.</b> (계산) 요소 1개 합성에 드는 ATP 수와 고에너지 인산 결합 수는?</p>
<p><b>4.</b> (빈칸) CPS I의 알로스테릭 활성화제는 ( &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; )이며, 이를 만드는 효소는 ( &nbsp;&nbsp;&nbsp; )이 활성화한다.</p>
<p><b>5.</b> (서술) 아스파르트산-아르기니노숙신산 션트란?</p>''',
  answer=chips('1. 미토: <b>CPS I → OTC</b> / 세포질: <b>ASS → ASL → 아르기네이스</b>', '2. <b>NH₄⁺ · 아스파르트산</b> / <b>HCO₃⁻</b>', '3. ATP <b>3</b>개 = 고에너지 결합 <b>4</b>개', '4. <b>N-아세틸글루탐산</b> / <b>아르기닌</b>', '5. 푸마르산 → 말산 → OAA → (AST) 아스파르트산 → 다시 요소 회로'),
  explain=fig(urea_cycle(), '') + steps('3. CPS I: 2 ATP → 2 ADP. ASS: ATP → AMP + PPᵢ(→ 2Pᵢ) = 결합 2개. 합계 4.',
   '5. 션트의 말산 → OAA에서 NADH가 생겨 비용 일부를 돌려받는다.') + warn('CPS I(미토, 요소) ≠ CPS II(세포질, 피리미딘).', '함정')),
 dict(id='C4', num='4', title='요소 회로 결함과 필수 아미노산', sec='S9', level=1,
  q='''<p><b>1.</b> (O/X) 요소 회로 결핍증 중 가장 흔한 것은 X-연관 OTC 결핍증이다.</p>
<p><b>2.</b> (짝짓기) 벤조산 · 페닐뷰티르산 ↔ 글루타민과 결합(질소 2개), 글리신과 결합(히푸르산)</p>
<p><b>3.</b> (서술) 아르기닌이 빠진 식사를 한 고양이에게 고암모니아혈증이 생긴 이유는? 오르니틴을 주면 왜 괜찮아지나?</p>
<p><b>4.</b> (쓰기) 필수 아미노산 9개를 한 글자 기호로 써라.</p>''',
  answer=chips('1. <b>O</b>', '2. 벤조산 → <b>글리신</b>(히푸르산) · 페닐뷰티르산 → <b>글루타민</b>(페닐아세틸글루타민)', '3. 오르니틴 공급 ✕ → 회로가 못 돎 / 오르니틴 = 회로 중간체', '4. <b>H I L K M F T W V</b>'),
  explain=steps('2. 질소를 요소 대신 다른 분자에 묶어 소변으로. 글루타민에는 질소가 2개라 페닐뷰티르산이 더 효율적.',
   '3. 아르기네이스: 아르기닌 → 요소 + 오르니틴. 아르기닌이 없으면 좌석(오르니틴)이 없어 NH₄⁺가 쌓인다. 고양이에게 아르기닌은 필수.') +
   key('필수 = 탄소 골격을 못 만드는 것. 하나만 빠져도 단백질 합성이 멈춘다.')),
 dict(id='C5', num='5', title='탄소 골격의 진입점', sec='S10–S11', level=2,
  q='''<p><b>1.</b> (빈칸) 피루브산으로 가는 아미노산 6개: ( &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ), α-KG로 가는 5개: ( &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ), 숙시닐-CoA로 가는 4개: ( &nbsp;&nbsp;&nbsp; )</p>
<p><b>2.</b> (O/X) 류신과 라이신은 포도당과 케톤체를 모두 만들 수 있다.</p>
<p><b>3.</b> (서술) 페닐알라닌·티로신이 포도당생성이면서 케톤생성인 이유는?</p>
<p><b>4.</b> (짝짓기) 트립토판에서 만들어지는 것: 나이아신 · 세로토닌 ↔ 신경전달물질, NAD⁺의 재료</p>
<p><b>5.</b> (빈칸) 급성 림프모구 백혈병 치료제로 쓰이는 효소는 ( &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; )이다.</p>''',
  answer=chips('1. <b>ACGSTW · PRHEQ · IMTV</b>', '2. <b>X</b> (오직 케톤)', '3. 골격이 쪼개져 <b>푸마르산</b>(포도당) + <b>아세토아세트산</b>(케톤)', '4. 나이아신 → NAD⁺ · 세로토닌 → 신경전달물질', '5. <b>L-아스파라지네이스</b>'),
  explain=fig(entry_map(), '') + steps('2. 류신·라이신은 아세틸-CoA·아세토아세틸-CoA로만 → 동물은 이걸로 포도당을 못 만든다.',
   '5. 백혈병 세포는 아스파라긴을 못 만들어 혈중 아스파라긴에 의존.') + key('케톤 진입점: 아세틸-CoA (ILTW), 아세토아세틸-CoA (LKFYW).')),
 dict(id='C6', num='6', title='보조인자와 B₁₂', sec='S12–S13', level=2,
  q='''<p><b>1.</b> (짝짓기) 비오틴 · THF · adoMet ↔ 메틸기(가장 강력), CO₂, 여러 산화 상태의 1탄소기</p>
<p><b>2.</b> (순서) THF 위 1탄소를 환원된 순서로: 메틸렌, 포밀, 메틸</p>
<p><b>3.</b> (빈칸) 사람에서 B₁₂가 필요한 효소 2개는 ( &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; )와 ( &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; )이다.</p>
<p><b>4.</b> (서술) B₁₂ 결핍이 왜 빈혈(DNA 합성 장애)을 일으키나? (“메틸 함정”)</p>
<p><b>5.</b> (O/X) 내인자가 없는 악성빈혈 환자는 B₁₂를 많이 먹으면 치료된다.</p>''',
  answer=chips('1. 비오틴 = <b>CO₂</b> · THF = <b>여러 1탄소</b> · adoMet = <b>메틸</b>', '2. <b>메틸 &gt; 메틸렌 &gt; 포밀</b> (환원 → 산화)', '3. <b>메틸말로닐-CoA 뮤테이스</b> / <b>메티오닌 합성효소</b>', '4. 메티오닌 합성효소 정지 → N⁵-메틸-THF에 엽산이 갇힘 → 메틸렌-THF ↓ → 티미딘 ↓', '5. <b>X</b> (주사 필요)'),
  explain=fig(b12_trap(), '') + steps('1. CO₂(가장 산화)는 비오틴, 메틸(가장 환원)은 adoMet, 중간은 THF.',
   '3. 뮤테이스 정지 → 메틸말론산 ↑, 메티오닌 합성효소 정지 → 호모시스테인 ↑.') + tip('adoMet은 설포늄(S⁺) 때문에 메틸을 쉽게 내준다.', '덤')),
 dict(id='C7', num='7', title='아미노산 대사의 유전 질환', sec='S14', level=1,
  q='''<p><b>1.</b> (짝짓기) PKU · 알캅톤뇨증 · 백색증 · 단풍당뇨증 ↔ 티로시네이스, 페닐알라닌 수산화효소, 가지사슬 α-케토산 탈수소효소, 호모젠티스산 이산소화효소</p>
<p><b>2.</b> (서술) PKU 환자 소변에 페닐피루브산·페닐젖산이 나오는 이유는?</p>
<p><b>3.</b> (O/X) PKU 환자에게 티로신은 필수 아미노산이 된다.</p>
<p><b>4.</b> (빈칸) 비케톤성 고글리신혈증은 ( &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ) 결함이며, 메틸말론산혈증은 ( &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ) 또는 B₁₂ 대사 결함이다.</p>
<p><b>5.</b> (서술) 가지사슬 아미노산 분해가 다른 아미노산과 다른 점은?</p>''',
  answer=chips('1. PKU = 페닐알라닌 수산화효소 · 알캅톤뇨증 = 호모젠티스산 이산소화효소 · 백색증 = 티로시네이스 · MSUD = BCKDH', '2. 쌓인 Phe가 아미노기 전이로 옆길(페닐피루브산 → 페닐젖산)로 넘침', '3. <b>O</b>', '4. <b>글리신 절단효소</b> / <b>메틸말로닐-CoA 뮤테이스</b>', '5. 간이 아니라 <b>간 밖(근육)</b>에서 먼저 분해'),
  explain=fig(phe_tyr(), '') + steps('2. 막힌 곳 앞(Phe)이 쌓이고, 농도가 높아지면 평소 미미하던 아미노전이효소 반응이 커진다.',
   '3. Phe → Tyr 길이 막혀 Tyr을 음식으로 받아야 한다.') + key('막힌 곳 앞은 쌓이고, 뒤는 모자란다. 치료 = 쌓이는 아미노산을 식이에서 줄이기.')),
]
NO_STRIP = ('S15',)
CHECK_AFTER = {2: 'C1', 5: 'C2', 7: 'C3', 8: 'C4', 10: 'C5', 12: 'C6', 13: 'C7'}

def __getattr__(name):  # 교수님 테스트뱅크 (지연 로드)
    if name == 'TB':
        from tb18 import TB
        return TB
    raise AttributeError(name)


if __name__ == '__main__':
    import exam18 as M
    examlib.render(M)
