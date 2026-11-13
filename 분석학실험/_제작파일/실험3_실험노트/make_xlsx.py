# -*- coding: utf-8 -*-
"""실험3 모어법 NaCl 정량 결과 엑셀 (NaCl 표준액 f′ · AgNO₃ 표정 f · 시판 소금 함량), 측정값 = 파란 글자, 나머지 수식"""
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
ws.title = "실험3 결과"
for col, w in zip("ABCD", (34, 16, 12, 54)):
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


ws["A1"] = "실험 3. 모어법에 의한 NaCl 정량 — 1조, 1회 측정"; ws["A1"].font = Font(name=F, bold=True, size=13)
ws["A2"] = "파란 글자 = 측정값·상수(입력), 검은 글자 = 수식. AgNO₃ 규정 농도는 0.2 M (수업 중 정정)"; ws["A2"].font = Font(name=F, italic=True, color="666666")

title(4, "Table I. 0.1 M NaCl 표준액")
head(5)
row(6, "NaCl 화학식량", 58.44, "g/mol", "유인물", "0.00", True)
row(7, "NaCl 규정 농도", 0.1, "M", "유인물", "0.0", True)
row(8, "용량플라스크 부피", 100.0, "mL", "", "0.0", True)
row(9, "이론량 (함량 100% 가정)", "=B7*B8/1000*B6", "g", "= 0.1 M × 0.1000 L × 58.44", "0.0000")
row(10, "NaCl 표준품 칭량값", 0.583, "g", "실험자 기록 (건조 생략)", "0.000", True)
row(11, "규정도계수 f′", "=ROUND(B10/B9,3)", "", "= 실제 칭량량 ÷ 이론량", "0.000")

title(13, "Table II. AgNO₃ 표준액의 표정")
head(14)
row(15, "AgNO₃ 규정 농도", 0.2, "M", "수업 중 정정 (유인물 0.1 M)", "0.0", True)
row(16, "분취한 NaCl 표준액", 20.0, "mL", "pipet", "0.0", True)
row(17, "NaCl 몰수", "=B7*B11*B16", "mmol", "= 0.1 × f′ × 20.0", "0.0000")
row(18, "뷰렛 시작 눈금", 19.87, "mL", "실험자 기록", "0.00", True)
row(19, "뷰렛 최종 눈금", 29.73, "mL", "실험자 기록", "0.00", True)
row(20, "AgNO₃ 소비량 V", "=B19-B18", "mL", "= 최종 − 시작", "0.00")
row(21, "공시험 b", 0.03, "mL", "실험자 기록", "0.00", True)
row(22, "보정 소비량 V − b", "=B20-B21", "mL", "", "0.00")
row(23, "규정도계수 f", "=ROUND(B17/(B15*B22),3)", "", "= NaCl mmol ÷ (0.2 × (V − b))", "0.000")

title(25, "Table III. 시판 소금 중 NaCl 함량")
head(26)
row(27, "시판 소금 칭량값", 0.099, "g", "실험자 기록 (건조 생략)", "0.000", True)
row(28, "뷰렛 시작 눈금", 32.60, "mL", "실험자 기록", "0.00", True)
row(29, "뷰렛 최종 눈금", 41.18, "mL", "실험자 기록", "0.00", True)
row(30, "AgNO₃ 소비량 V", "=B29-B28", "mL", "= 최종 − 시작", "0.00")
row(31, "공시험 b", 0.02, "mL", "녹취록 41.18 → 41.20 (확인 필요)", "0.00", True)
row(32, "보정 소비량 V − b", "=B30-B31", "mL", "", "0.00")
row(33, "대응량 E (0.2 M 1 mL)", "=B15*B6", "mg NaCl/mL", "= 0.2 × 58.44", "0.000")
row(34, "NaCl 양", "=B32*B23*B33/1000", "g", "= (V − b) × f × E × 10⁻³", "0.0000")
row(35, "NaCl 함량", "=ROUND(B34/B27*100,1)", "%", "= NaCl(g) ÷ 시료(g) × 100", "0.0")
row(36, "(참고) 표준품 순도 99% 반영 시 함량", "=ROUND(B32*ROUND(B7*ROUND(B10*0.99/B9,3)*B16/(B15*B22),3)*B33/1000/B27*100,1)", "%", "f′ = 0.583 × 0.99 ÷ 0.5844 — 노트 계산에는 쓰지 않음", "0.0")
wb.save(sys.argv[1])
