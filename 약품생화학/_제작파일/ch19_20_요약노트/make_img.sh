#!/bin/sh
# 강의 PDF에서 슬라이드 그림(img/S-001.jpg …)을 만든다. 이 폴더에서 실행.
mkdir -p img
pdftoppm -r 100 -jpeg -jpegopt quality=80 "../../Chap19_20_note.pdf" img/S
# 슬라이드 가장자리 흰 여백을 잘라 그림을 크게 보이게
mogrify -fuzz 4% -trim +repage img/S-*.jpg
mogrify -resize "760x760>" -quality 76 img/S-*.jpg
# 백지 복습용 실제 세포소기관 그림 (확대 부위에 빨간 원)
convert img/S-028.jpg -crop 370x641+0+0 +repage -fill none -stroke "#e03131" -strokewidth 5 -draw "ellipse 88,310 58,22 0,360" img/real_mito.jpg
convert img/S-097.jpg -crop 300x290+460+135 +repage -fill none -stroke "#e03131" -strokewidth 5 -draw "ellipse 168,166 32,15 0,360" img/real_chl.jpg
