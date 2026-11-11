# intro.pdf(새 페이지) + overlay를 얹은 6주차 요약정리 쪽을 order.json 순서대로 합침
import os, json
from pypdf import PdfReader, PdfWriter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
SRC = os.path.join(ROOT, "신약개발개론_6주차_후보물질 탐색 및 발굴1_요약정리.pdf")
OUT = os.path.join(ROOT, "신약개발개론_10주차_후보물질 탐색 및 발굴2 & 약물대사_요약정리.pdf")

new = iter(PdfReader(os.path.join(HERE, "intro.pdf")).pages)
ov = iter(PdfReader(os.path.join(HERE, "overlay.pdf")).pages)
old = PdfReader(SRC)
w = PdfWriter()
for kind, *k in json.load(open(os.path.join(HERE, "order.json"))):
    if kind == "new":
        w.add_page(next(new))
    else:
        pg = old.pages[k[0] - 1]
        pg.merge_page(next(ov))
        w.add_page(pg)
w.write(OUT)
print(OUT, len(w.pages))
