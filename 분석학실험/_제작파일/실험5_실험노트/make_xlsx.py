# -*- coding: utf-8 -*-
"""실험5 요오드 적정 결과 엑셀 (I₂ f · Na₂S₂O₃ 표정 f′ · 포비돈요오드액 · 아스코르브산), 측정값 = 파란 글자, 나머지 수식"""
import sys
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, Border, Side, PatternFill

F = "Arial"
thin = Side(style="thin", color="999999")
box = Border(left=thin, right=thin, top=thin, bottom=thin)
hdr = PatternFill("solid", fgColor="EEF0F8")
inp, blk, bold = Font(name=F, color="0000FF"), Font(name=F), Font(name=F, bold=True)
mid = Alignment(horizontal="center", vertical="center", wrap_text=True)

wb = Workbook()
ws = wb.active
ws.title = "실험5 결과"
for col, w in zip("ABCD", (36, 16, 12, 56)):
    ws.column_dimensions[col].width = w


def title(r, t):
    ws.cell(row=r, column=1, value=t).font = Font(name=F, bold=True, size=12)


def head(r):
    for j, h in enumerate(("항목", "값", "단위", "계산 / 출처"), 1):
        c = ws.cell(row=r, column=j, value=h); c.font = bold; c.fill = hdr; c.alignment = mid; c.border = box


def row(r, name, val, unit, note, fmt, is_input=False):
    if note.startswith("="):
        note = "식: " + note[1:].strip()
    for j, v in enumerate((name, val, unit, note), 1):
        c = ws.cell(row=r, column=j, value=v); c.border = box
        c.alignment = Alignment(horizontal="left" if j in (1, 4) else "center", vertical="center", wrap_text=True)
        c.font = inp if (j == 2 and is_input) else blk
    ws.cell(row=r, column=2).number_format = fmt


ws["A1"] = "실험 5. 요오드 적정 — 1조, 각 1회 측정"; ws["A1"].font = Font(name=F, bold=True, size=13)
ws["A2"] = "파란 글자 = 측정값·상수(입력), 검은 글자 = 수식. 판정 기준값(B42–B44)은 대한약전 원문으로 확인 후 수정"; ws["A2"].font = Font(name=F, italic=True, color="666666")

title(4, "Table I. [표준액] 0.05 M I₂ 표준액 (구매품, 표정 안 함)")
head(5)
row(6, "규정도계수 f", 1.003, "", "병 라벨", "0.000", True)

title(8, "Table II. [표정] 0.1 M Na₂S₂O₃액 — 간접법")
head(9)
row(10, "분취한 I₂ 표준액", 10.00, "mL", "pipet", "0.00", True)
row(11, "뷰렛 시작 눈금", 25.55, "mL", "실험자 기록", "0.00", True)
row(12, "뷰렛 최종 눈금", 35.00, "mL", "실험자 기록", "0.00", True)
row(13, "Na₂S₂O₃ 소비량", "=B12-B11", "mL", "= 최종 − 시작", "0.00")
row(14, "규정도계수 f′", "=ROUND(B6*B10/B13,3)", "", "= f × V(I₂) ÷ V(Na₂S₂O₃)", "0.000")

title(16, "Table III. [적정 1] 포비돈요오드액 중 요오드 (아이오도메트리)")
head(17)
row(18, "분취량 (요오드로서 100 mg 상당)", 10.00, "mL", "transfer pipet, 10 w/v% (유효 요오드 1 w/v%)", "0.00", True)
row(19, "표시 요오드량", "=B18*10", "mg", "= 분취량 × 10 mg/mL", "0.0")
row(20, "뷰렛 시작 눈금", 35.00, "mL", "실험자 기록", "0.00", True)
row(21, "뷰렛 최종 눈금", 42.42, "mL", "실험자 기록", "0.00", True)
row(22, "Na₂S₂O₃ 소비량", "=B21-B20", "mL", "= 최종 − 시작", "0.00")
row(23, "대응량", 12.691, "mg I₂/mL", "0.1 M Na₂S₂O₃ 1 mL ≡ 0.05 mmol I₂ (유인물)", "0.000", True)
row(24, "요오드 양", "=B22*B14*B23", "mg", "= V × f′ × 12.691", "0.00")
row(25, "표시량 대비", "=ROUND(B24/B19*100,1)", "%", "= 요오드 ÷ 표시량 × 100", "0.0")

title(27, "Table IV. [적정 2] 아스코르브산 (아이오디메트리)")
head(28)
row(29, "아스코르브산 칭량값", 0.1997, "g", "실험자 기록 (조에서 건조 안 함)", "0.0000", True)
row(30, "1차: 뷰렛 시작 눈금", 29.75, "mL", "실험자 기록", "0.00", True)
row(31, "1차: 뷰렛 최종 눈금", 50.00, "mL", "적정액 부족 → 재충전", "0.00", True)
row(32, "1차 소비량", "=B31-B30", "mL", "= 최종 − 시작", "0.00")
row(33, "2차: 뷰렛 시작 눈금", 39.10, "mL", "재충전 후", "0.00", True)
row(34, "2차: 뷰렛 최종 눈금", 41.18, "mL", "실험자 기록", "0.00", True)
row(35, "I₂ 소비량 합계", "=B32+(B34-B33)", "mL", "= 1차 + 2차", "0.00")
row(36, "대응량", 8.806, "mg/mL", "0.05 M I₂ 1 mL ≡ 아스코르브산 8.806 mg (유인물)", "0.000", True)
row(37, "아스코르브산 양", "=B35*B6*B36", "mg", "= V × f × 8.806", "0.00")
row(38, "함량", "=ROUND(B37/(B29*1000)*100,1)", "%", "= 아스코르브산 mg ÷ 칭량값 mg × 100", "0.0")

title(40, "Table V. 대한약전 기준 판정 (기준값은 원문 확인)")
head(41)
row(42, "포비돈요오드액 기준 하한", 85.0, "%", "참고값 — 대한약전 원문 확인", "0.0", True)
row(43, "포비돈요오드액 기준 상한", 120.0, "%", "참고값 — 대한약전 원문 확인", "0.0", True)
row(44, "아스코르브산 기준 하한", 99.0, "%", "참고값 — 대한약전 원문 확인", "0.0", True)
row(45, "포비돈요오드액 판정", '=IF(AND(B25>=B42,B25<=B43),"만족","불만족")', "", "", "@")
row(46, "아스코르브산 판정", '=IF(B38>=B44,"만족","불만족")', "", "", "@")
wb.save(sys.argv[1])
