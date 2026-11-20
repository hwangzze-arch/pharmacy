# -*- coding: utf-8 -*-
"""실험4 물의 경도 결과 엑셀 (EDTA 표준액 f · 총경도 적정 · Ca 경도 적정 · Mg 경도), 측정값 = 파란 글자, 나머지 수식"""
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
ws.title = "실험4 결과"
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


ws["A1"] = "실험 4. EDTA를 이용한 물의 세기(경도) 측정 — 1조, 수돗물, 1회 측정"; ws["A1"].font = Font(name=F, bold=True, size=13)
ws["A2"] = "파란 글자 = 측정값·상수(입력), 검은 글자 = 수식"; ws["A2"].font = Font(name=F, italic=True, color="666666")

title(4, "Table I. 0.01 M EDTA 표준액 조제 (1차 표준물질 → 표정 생략)")
head(5)
row(6, "EDTA 화학식량 (Na₂H₂Y·2H₂O)", 372.25, "g/mol", "유인물", "0.00", True)
row(7, "규정 농도", 0.01, "M", "유인물", "0.00", True)
row(8, "용량플라스크 부피", 250.0, "mL", "", "0.0", True)
row(9, "이론량", "=B7*B8/1000*B6", "g", "= 0.01 × 0.2500 × 372.25", "0.0000")
row(10, "EDTA 칭량값", 0.931, "g", "실험자 기록 (조에서 건조 안 함)", "0.000", True)
row(11, "규정도계수 f", "=ROUND(B10/B9,3)", "", "= 실제 칭량량 ÷ 이론량", "0.000")

title(13, "Table II. 총경도 적정 (pH 10, EBT)")
head(14)
row(15, "시료 (수돗물)", 100.0, "mL", "메스실린더", "0.0", True)
row(16, "가한 0.01 M MgCl₂", 1.0, "mL", "마이크로피펫", "0.0", True)
row(17, "뷰렛 시작 눈금", 25.35, "mL", "실험자 기록", "0.00", True)
row(18, "뷰렛 최종 눈금", 32.11, "mL", "실험자 기록", "0.00", True)
row(19, "EDTA 소비량 a", "=B18-B17", "mL", "= 최종 − 시작", "0.00")
row(20, "총경도", "=ROUND((B19*B11-B16)*1000/B15,1)", "ppm CaCO₃", "= (a × f − 1) × 1000 ÷ 시료 mL", "0.0")

title(22, "Table III. Ca 경도 적정 (pH 12, HNB)")
head(23)
row(24, "시료 (수돗물)", 100.0, "mL", "메스실린더", "0.0", True)
row(25, "뷰렛 시작 눈금", 32.11, "mL", "실험자 기록", "0.00", True)
row(26, "뷰렛 최종 눈금", 36.25, "mL", "실험자 기록", "0.00", True)
row(27, "EDTA 소비량 b", "=B26-B25", "mL", "= 최종 − 시작", "0.00")
row(28, "Ca 경도", "=ROUND(B27*B11*1000/B24,1)", "ppm CaCO₃", "= b × f × 1000 ÷ 시료 mL", "0.0")

title(30, "Table IV. 경도 결과")
head(31)
row(32, "총경도", "=B20", "ppm CaCO₃", "", "0.0")
row(33, "Ca 경도", "=B28", "ppm CaCO₃", "", "0.0")
row(34, "Mg 경도", "=ROUND(B32-B33,1)", "ppm CaCO₃", "= 총경도 − Ca 경도", "0.0")
row(35, "판정", '=IF(B32<=75,"연수(단물)",IF(B32<=150,"비교적 약한 경수",IF(B32<=300,"경수","아주 강한 경수")))&IF(B32<=300," · 음용수 기준(300 ppm 이하) 만족"," · 음용수 기준 초과")', "", "유인물 경도 기준표", "@")
wb.save(sys.argv[1])
