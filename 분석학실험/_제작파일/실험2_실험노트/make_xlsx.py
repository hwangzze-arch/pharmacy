# -*- coding: utf-8 -*-
"""실험2 식초 총산도 결과 엑셀 (KHP 용액 · NaOH 표정 · 식초 총산도), 측정값 = 파란 글자, 나머지 수식"""
import sys
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, Border, Side, PatternFill
from openpyxl.comments import Comment

F = "Arial"
thin = Side(style="thin", color="999999")
box = Border(left=thin, right=thin, top=thin, bottom=thin)
hdr = PatternFill("solid", fgColor="EEF0F8")
inp, blk, bold = Font(name=F, color="0000FF"), Font(name=F), Font(name=F, bold=True)
mid = Alignment(horizontal="center", vertical="center", wrap_text=True)

wb = Workbook()
ws = wb.active
ws.title = "실험2 결과"
ws.column_dimensions["A"].width = 34
ws.column_dimensions["B"].width = 16
ws.column_dimensions["C"].width = 12
ws.column_dimensions["D"].width = 52


def title(r, t):
    ws.cell(row=r, column=1, value=t).font = Font(name=F, bold=True, size=12)


def head(r):
    for j, h in enumerate(("항목", "값", "단위", "계산 / 출처"), 1):
        c = ws.cell(row=r, column=j, value=h); c.font = bold; c.fill = hdr; c.alignment = mid; c.border = box


def row(r, name, val, unit, note, fmt, is_input=False):
    if note.startswith("="):
        note = "식: " + note[1:].strip()
    vals = (name, val, unit, note)
    for j, v in enumerate(vals, 1):
        c = ws.cell(row=r, column=j, value=v); c.border = box
        c.alignment = Alignment(horizontal="left" if j in (1, 4) else "center", vertical="center", wrap_text=True)
        c.font = inp if (j == 2 and is_input) else blk
    ws.cell(row=r, column=2).number_format = fmt


ws["A1"] = "실험 2. 지시약을 이용한 식초 중의 총 산도 측정 — 1조, 1회 측정"; ws["A1"].font = Font(name=F, bold=True, size=13)
ws["A2"] = "파란 글자 = 측정값·상수(입력), 검은 글자 = 수식"; ws["A2"].font = Font(name=F, italic=True, color="666666")

title(4, "Table I. KHP 일차표준용액 (1조 제조)")
head(5)
row(6, "KHP 칭량값 A₀", 2.042, "g", "실험자 기록 (1조 칭량)", "0.000", True)
row(7, "KHP 화학식량", 204.221, "g/mol", "유인물", "0.000", True)
row(8, "용량플라스크 부피", 100.0, "mL", "", "0.0", True)
row(9, "KHP 몰농도 C", "=B6/B7/(B8/1000)", "M", "= A₀ ÷ 204.221 ÷ 0.1000 L", "0.0000")
row(10, "pK₁", 2.9, "", "유인물", "0.0", True)
row(11, "pK₂", 5.5, "", "유인물", "0.0", True)
row(12, "이론 pH (중간형, 정확식)", "=-LOG10(SQRT((10^-B10*10^-B11*B9+10^-B10*1E-14)/(10^-B10+B9)))", "", "[H⁺] = √[(K₁K₂C + K₁K_w)/(K₁ + C)]", "0.00")
row(13, "이론 pH (근사식)", "=(B10+B11)/2", "", "(pK₁ + pK₂)/2", "0.00")

title(15, "Table II. 0.1 M NaOH 표준액의 표정")
head(16)
row(17, "분취한 KHP 용액", 20.00, "mL", "pipet", "0.00", True)
row(18, "적정한 KHP 양 A", "=B6*B17/B8", "g", "= A₀ × 20.00/100.0", "0.0000")
row(19, "KHP 몰수", "=B18*1000/B7", "mmol", "= A × 10³ / 204.221", "0.0000")
row(20, "뷰렛 시작 눈금", 15.00, "mL", "실험자 기록", "0.00", True)
row(21, "뷰렛 최종 눈금", 34.50, "mL", "실험자 기록", "0.00", True)
row(22, "NaOH 소비량 V_b", "=B21-B20", "mL", "= 최종 − 시작", "0.00")
row(23, "NaOH 농도 B", "=B19/B22", "mmol/mL", "= KHP mmol ÷ V_b", "0.00000")
row(24, "규정도계수 f", "=ROUND(B23/0.1,3)", "", "= B / 0.100 (소수 셋째 자리)", "0.000")

title(26, "Table III. 식초의 총 산도")
head(27)
row(28, "식초 원액 분취량", 10.00, "mL", "pipet → 100 mL로 희석", "0.00", True)
row(29, "희석액 분취량", 20.00, "mL", "pipet", "0.00", True)
row(30, "실제 적정한 식초 원액", "=B28*B29/B8", "mL", "= 10.00 × 20.00/100.0", "0.000")
row(31, "NaOH 소비량 V_b", 20.92, "mL", "실험자 기록 (시작·최종 눈금 미기록)", "0.00", True)
row(32, "초산 화학식량", 60.05, "g/mol", "유인물", "0.00", True)
row(33, "초산 (환산량)", "=0.1*B24*B31*B32/1000", "g", "= 0.1 × f × V_b × 60.05 × 10⁻³", "0.0000")
row(34, "총산도", "=ROUND(B33/B30*100,2)", "w/v%", "= 초산(g) ÷ 식초(mL) × 100", "0.00")
row(35, "(비교) f = 1.000으로 계산 시", "=ROUND(0.1*1*B31*B32/1000/B30*100,2)", "w/v%", "제조사 팩터 — 노트 계산에는 쓰지 않음", "0.00")

wb.save(sys.argv[1])
