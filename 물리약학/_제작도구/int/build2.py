# -*- coding: utf-8 -*-
# 압축판: 한 장 정리(맨 앞) + 문제·풀이만 (흐름 배치, 원래 글자 크기)
import os, lib
import p1, p2, p3, p4, p5, p6  # noqa
from lib import flow, HERE

CSS = open(os.path.join(HERE, 'style4.css'), encoding='utf-8').read() + '''
@page { size: 297mm 210mm; margin: 9mm 12mm 11mm; }
body { font-size: 15.4px; line-height: 1.62; }
.page { height: auto; overflow: visible; padding: 0; break-after: auto; page-break-after: auto; }
.flowdoc .prow { break-inside: avoid; page-break-inside: avoid; margin: 0 0 12px; padding: 0 0 12px; border-bottom: 2px dashed #d7dde8; border-top: 0; }
.flowdoc .prow + .prow { margin-top: 0; padding-top: 0; border-top: 0; }
.qq { font-size: 15.4px; } .chs { font-size: 14.8px; } .fl .tx { font-size: 14.8px; }
.qh .t { font-size: 15.6px; } .sol .ans { font-size: 17px; } table { font-size: 14px; }
.mine { flex: none; height: 46px; min-height: 0; margin-top: 7px; }
.sec-h { break-after: avoid; display: flex; align-items: center; gap: 12px; margin: 4px 0 10px; padding: 7px 14px; border-radius: 10px; background: var(--cl); border-left: 6px solid var(--c); }
.sec-h b { font-size: 19px; color: var(--cd); } .sec-h span { font-size: 13px; color: #555; }
.newpart { break-before: page; }
.cs { grid-template-columns: repeat(4, 1fr); gap: 7px; } .cs > div { padding: 5px 10px; }
.cs .f { font-size: 14.4px; line-height: 1.4; } .cs .d { font-size: 12.4px; line-height: 1.4; } .cs .h { font-size: 12px; }
.title + .legend + .cs + .brain { margin-top: 8px; } .brain { padding: 6px 12px; font-size: 14.2px; }
.title { display: flex; align-items: baseline; gap: 14px; border-bottom: 3px solid #1d6db1; padding-bottom: 6px; margin-bottom: 10px; }
.title h1 { margin: 0; font-size: 24px; } .title span { color: #555; font-size: 13.5px; }
.legend { font-size: 13px; color: #444; margin: 0 0 8px; }
.cs .w5 { color: #b42318; }
.p6 { --c: #b42318; --cl: #fdeeee; --cd: #8a1c1c; }

.flowdoc .prow { grid-template-columns: 0.82fr 1.18fr; gap: 12px; }
.fl { padding-bottom: 3px; } .fl:not(:last-child)::before { top: 23px; }
.sol { padding: 7px 12px; } .qcard { padding: 7px 12px; }
'''

# ---------- 한 장 정리 (맨 앞) + 속도론 칸 추가
CS = list(p5.CS) + [
    ('w5', '반응 차수', '−d[A]/dt = k[A]ⁿ', 'n은 실험으로 결정 · 계수 ≠ 차수'),
    ('w5', '0차', '[A]ₜ = −kt + [A]₀ · t½ = [A]₀/2k', 'k: mol/L·s · [A]–t 직선 · Pt 표면 N₂O'),
    ('w5', '1차', 'ln[A]ₜ = −kt + ln[A]₀ · t½ = 0.693/k', 'k: s⁻¹ · ln[A]–t 직선(−k) · t½ 농도 무관'),
    ('w5', '2차', '1/[A]ₜ = kt + 1/[A]₀ · t½ = 1/k[A]₀', 'k: L/mol·s · 1/[A]–t 직선(+k)'),
]
cells = ''.join(f'<div><div class="h {w}">{a}</div><div class="f">{b}</div><div class="d">{c}</div></div>' for w, a, b, c in CS)
head = f'''<section class="page p5"><div class="title"><h1>물리약학 중간고사 — 시험 직전 5분 한 장 정리</h1><span>2–7주차 + 화학반응 속도론 · 뒤에 문제 {{N}}개 + 사고의 흐름 풀이</span></div>
<div class="legend"><b style="color:#0e7c86">■ 2주차 용해도·분배</b> · <b style="color:#7b3fb5">■ 3주차 착물</b> · <b style="color:#4954d1">■ 4–6주차 확산</b> · <b style="color:#c4501f">■ 7주차 방출</b> · <b style="color:#b42318">■ 속도론</b></div>
<div class="cs">{cells}</div>
<div class="brain"><span class="lab">🧠 전 범위 한 문장</span>녹아야(Cs) → 나뉘고(K) → 퍼져서(J = DKΔC/h) → 나온다(√t · 0차) — 착물은 이 흐름을 조절하는 도구, 속도론은 "얼마나 빨리 사라지나"!</div>
<div class="brain" style="background:#b42318"><span class="lab">⚠️ 함정 TOP 6</span>① pKa ≠ 침전 pH ② 진분배계수는 pH와 무관 ③ 두께 무관은 D, P ∝ 1/h ④ 다층은 저항 더하고 뒤집기 ⑤ 누적 방출량은 항상 증가, 줄어드는 건 속도 ⑥ 1차 반감기는 농도와 무관</div></section>'''

# ---------- 문제 (PART 순으로 안정 정렬)
probs = [it for it in lib.ITEMS if it['kind'] == 'pr']
probs.sort(key=lambda it: it['part'])
SECT = {1: ('PART 1 · 용해도 · 분배 (2주차)', '침전 pH · 보용매 · 입자 크기 · 분배계수 · 추출'),
        2: ('PART 2 · 착물 · 단백질 결합 (3주차)', '배위수 · 킬레이트 · 카페인 · 내포화합물 · CD · 투석'),
        3: ('PART 3 · 확산 (4–6주차)', 'Fick · 정상상태 · P = DK/h · 다층 · 막/수층 제어 · pH 분배 · 패치'),
        4: ('PART 4 · 붕해 · 용출 · 약물 방출 (7주차)', '0차 · OROS · Noyes-Whitney · Higuchi · Bottari · K-P · BCS'),
        6: ('PART 5 · 화학반응 속도론', '0·1·2차 속도식 · 적분식 · 반감기 · k 단위 — 2024 중간 리뷰 재구성')}
body = ''
cur = None
for no, it in enumerate(probs, 1):
    if it['part'] != cur:
        cur = it['part']
        t, s = SECT[cur]
        body += f'<div class="sec-h p{cur} newpart"><b>{t}</b><span>{s}</span></div>'
    body += lib.pr_html(it, no)
html = head.replace('{N}', str(len(probs))) + f'<section class="flowdoc">{body}</section>'
open(os.path.join(HERE, 'out2.html'), 'w', encoding='utf-8').write(
    f'<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>물리약학 중간고사 문제 · 풀이 압축판</title><style>{CSS}</style></head><body>{html}</body></html>')
print(len(probs), 'problems')
