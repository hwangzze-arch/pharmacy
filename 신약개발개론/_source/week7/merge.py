# intro.pdf + (6주차 요약정리 재사용 쪽 위에 overlay.pdf) → 7주차 요약정리
import os, json
from pypdf import PdfReader, PdfWriter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
SRC = os.path.join(ROOT, "신약개발개론_6주차_후보물질 탐색 및 발굴1_요약정리.pdf")
OUT = os.path.join(ROOT, "신약개발개론_7주차_중간고사 결과 & 후보물질 탐색 및 발굴2_요약정리.pdf")

w = PdfWriter()
for pg in PdfReader(os.path.join(HERE, "intro.pdf")).pages:
    w.add_page(pg)
old = PdfReader(SRC)
ov = PdfReader(os.path.join(HERE, "overlay.pdf")).pages
for k, o in zip(json.load(open(os.path.join(HERE, "reuse.json"))), ov):
    pg = old.pages[k - 1]
    pg.merge_page(o)
    w.add_page(pg)
w.write(OUT)
print(OUT, len(w.pages))
