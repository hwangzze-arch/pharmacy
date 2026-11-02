"""8장 그림 자르기 + 그림 각주 문제용 라벨(A, B, C…) 붙이기.
사용: hi/ 에 슬라이드를 220dpi PNG(c8-NN.png)로 렌더한 뒤 python3 crop8.py"""
import os, sys
from PIL import Image, ImageDraw, ImageFont
HI = sys.argv[1] if len(sys.argv) > 1 else 'hi'
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fig')
# 요약 페이지용 그림: 슬라이드 비율 좌표 (x0, y0, x1, y1)
B = {'c8-07': (.2, .12, .8, .98), 'c8-08': (0, .6, 1, .98), 'c8-13': (0, .12, 1, .98),
     'c8-17': (.17, .14, .91, .98), 'c8-18': (.555, .25, 1, .87), 'c8-23': (.17, .15, .83, .95),
     'c8-25': (0, .12, .75, .98), 'c8-26': (.25, .12, .8, .98), 'c8-29': (0, .12, 1, .85), 'c8-31': (0, .12, 1, .98),
     'c8-34': (0, .12, .6, .98), 'c8-37': (.15, .12, .8, .98),
     'c8-43': (0, .62, 1, .98), 'c8-44': (0, .12, 1, .98)}
FONT = ImageFont.truetype(os.path.expanduser('~/.fonts/Pretendard-ExtraBold.ttf'), 40)

def badge(d, x, y, t, r=30):
    d.ellipse((x - r, y - r, x + r, y + r), fill='#1d2747', outline='white', width=5)
    d.text((x, y), t, fill='white', font=FONT, anchor='mm')

# 그림 각주 문제: 출력 이름 -> (원본 crop 픽셀 박스, 가릴 상자들, 라벨 (x, y, 글자[, 지시선 끝 x, y]))
# 가릴 상자는 주변 배경색으로 칠한다(다섯 번째 값을 주면 그 색으로)
T41 = (790, 1000, 1500, 1460, 'white')  # 슬라이드 41 오른쪽 아래 설명 글(답이 적혀 있음)
Q = {
 'c8-41': ((60, 290, 1500, 1570), [T41], []),
 'c8-17-q': ((380, 240, 1990, 790),
           [(380, 560, 458, 720), (735, 283, 944, 333), (429, 398, 539, 449), (773, 398, 910, 449), (1127, 398, 1249, 449), (1468, 398, 1606, 449), (1815, 398, 1922, 449)],
           [(840, 308, 'A'), (484, 423, 'B'), (842, 423, 'C'), (1188, 423, 'D'), (1537, 423, 'E'), (1660, 500, 'F', 1542, 566), (1430, 639, 'G'), (1749, 670, 'H')]),
 'c8-31-q': ((110, 270, 2090, 1092),
           [(535, 568, 648, 656), (1106, 522, 1302, 608), (1628, 292, 1770, 338), (1852, 500, 2040, 664)],
           [(590, 612, 'A'), (1204, 565, 'B'), (1699, 315, 'C'), (1946, 582, 'D')]),
 'c8-41-q': ((60, 290, 1500, 1570),
           [T41, (500, 916, 712, 952), (70, 1524, 330, 1560), (1274, 414, 1468, 472), (580, 1188, 775, 1222), (503, 836, 730, 896), (503, 548, 665, 606), (578, 1293, 665, 1326)],
           [(1370, 443, 'A'), (678, 1205, 'B'), (612, 866, 'C'), (585, 577, 'D'), (622, 1310, 'E'), (606, 934, 'F')]),
}

for k, (a, b, c, d) in B.items():
    im = Image.open(os.path.join(HI, k + '.png')).convert('RGB'); W, H = im.size
    im.crop((int(a * W), int(b * H), int(c * W), int(d * H))).save(os.path.join(OUT, k + '.jpg'), quality=84)
for k, (box, masks, labels) in Q.items():
    im = Image.open(os.path.join(HI, k[:5] + '.png')).convert('RGB'); d = ImageDraw.Draw(im)
    for m in masks:  # 주변 배경색으로 칠해 라벨을 지운다
        if len(m) == 5:
            d.rectangle(m[:4], fill=m[4]); continue
        cs = [im.getpixel((x, y)) for x, y in ((m[0] - 4, m[1] - 4), (m[2] + 4, m[1] - 4), (m[0] - 4, m[3] + 4), (m[2] + 4, m[3] + 4))]
        d.rectangle(m, fill=tuple(sum(c[i] for c in cs) // 4 for i in range(3)))
    for x, y, t, *to in labels:  # to = 지시선 끝점 (선택)
        if to:
            d.line((x, y, to[0], to[1]), fill='#1d2747', width=5)
        badge(d, x, y, t)
    im.crop(box).save(os.path.join(OUT, k + '.jpg'), quality=86)
print('ok')
