#!/bin/sh
# 강의 PDF 슬라이드를 img/s-01.jpg … 로 만든다. 사용: sh make_img.sh "../../CH22_약품유기화학2.pdf"
mkdir -p img tmp
pdftoppm -r 150 -png "$1" tmp/s
for f in tmp/s-*.png; do b=$(basename "$f" .png); convert "$f" -resize 1200x -quality 85 "img/$b.jpg"; done
rm -rf tmp
