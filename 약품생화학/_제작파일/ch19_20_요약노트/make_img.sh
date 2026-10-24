#!/bin/sh
# 강의 PDF에서 슬라이드 그림(img/S-001.jpg …)을 만든다. 이 폴더에서 실행.
mkdir -p img
pdftoppm -r 100 -jpeg -jpegopt quality=80 "../../Chap19_20_note.pdf" img/S
# 슬라이드 가장자리 흰 여백을 잘라 그림을 크게 보이게
mogrify -fuzz 4% -trim +repage img/S-*.jpg
mogrify -resize "760x760>" -quality 76 img/S-*.jpg
