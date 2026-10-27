#!/bin/sh
# 강의 PDF에서 슬라이드 그림(img/L2-01.jpg …)을 다시 만든다. 이 폴더에서 실행.
SRC="../.."
mkdir -p img
pdftoppm -r 100 -jpeg -jpegopt quality=82 "$SRC/의약품분석학II-Lecture2_분광학기초, 자외가시부.pdf" img/L2
pdftoppm -r 100 -jpeg -jpegopt quality=82 "$SRC/의약품분석학II-Lecture3_형광 선광도 원자분광법.pdf" img/L3
pdftoppm -r 100 -jpeg -jpegopt quality=82 "$SRC/의약품분석학II-Lecture4_NMR.pdf" img/L4
