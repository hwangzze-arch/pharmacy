#!/bin/sh
# 강의 PDF에서 슬라이드 그림(img/L5-01.jpg …)을 만든다. 이 폴더에서 실행.
SRC="../.."
mkdir -p img
pdftoppm -r 100 -jpeg -jpegopt quality=82 "$SRC/의약품분석학II-Lecture5_질량분석법.pdf" img/L5
pdftoppm -r 100 -jpeg -jpegopt quality=82 "$SRC/의약품분석학II-Lecture6_Chromatography.pdf" img/L6
