"""9·10장 그림 자르기 + 그림 각주 문제용 라벨. crop8.py와 같은 방식.
사용: 슬라이드를 220dpi PNG(c9-NN.png, c10-NN.png)로 렌더한 폴더를 주고 python3 crop9.py 폴더"""
import os, sys
from PIL import Image, ImageDraw, ImageFont
HI = sys.argv[1] if len(sys.argv) > 1 else 'hi'
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fig')
FONT = ImageFont.truetype(os.path.expanduser('~/.fonts/Pretendard-ExtraBold.ttf'), 40)
# 요약 페이지용: 이름 -> 비율 (x0, y0, x1, y1) 또는 픽셀 박스
B = {'c9-08': (1355, 385, 2150, 1230), 'c9-20': (0, 500, 2200, 1250), 'c9-17': (.1, .55, .6, .98), 'c9-26': (.25, .12, .75, .98),
     'c9-27': (.6, .12, 1, .98), 'c9-29': (0, .12, .55, .98), 'c9-33': (0, .12, .45, .98), 'c9-39': (0, .12, 1, .68),
     'c9-41': (0, .15, .6, .98), 'c9-45': (0, .12, 1, 1),
     'c10-07': (.1, .3, .95, .95), 'c10-11': (.05, .12, .95, .98), 'c10-13': (.05, .47, .75, .98), 'c10-16': (.55, .2, 1, .98),
     'c10-21': (.25, .13, .75, .98), 'c10-24': (0, .12, 1, .98), 'c10-25': (0, .47, 1, .98), 'c10-28': (0, .15, 1, .98),
     'c10-30': (.6, .6, 1, .98), 'c10-32': (0, .45, 1, .98), 'c10-36': (0, .12, 1, .98)}
# 그림 각주: 이름 -> (원본 슬라이드, 픽셀 crop, 가릴 상자 [x0,y0,x1,y1(,'in')], 라벨 (x, y, 글자))
# 'in' = 상자 안쪽 모서리 색으로 칠함(색 있는 상자 속 글자 지우기), 없으면 상자 바깥 네 모서리 평균색
Q = {
 'c9-20-q': ('c9-20', (0, 500, 1110, 1240),
   [(33, 530, 182, 602), (33, 630, 190, 703), (33, 816, 193, 890), (856, 622, 1098, 696), (856, 813, 1034, 927), (856, 1061, 985, 1132), (33, 1062, 237, 1174)],
   [(110, 667, 'A'), (975, 659, 'B'), (945, 870, 'C'), (920, 1096, 'D'), (113, 853, 'E'), (107, 566, 'F'), (135, 1118, 'G')]),
 'c9-34-q': ('c9-34', (100, 400, 1010, 1400),
   [(407, 437, 589, 510), (625, 851, 732, 926), (880, 1278, 1003, 1390)],
   [(498, 474, 'A'), (678, 888, 'B'), (941, 1334, 'C')]),
 'c10-34-q': ('c10-34', (0, 330, 2200, 1440),
   [(913, 395, 1150, 517, 'in'), (829, 840, 1065, 994, 'in'), (869, 1071, 1188, 1196, 'in'), (1375, 1071, 1694, 1196, 'in'), (834, 1272, 1069, 1396, 'in')],
   [(1031, 456, 'A'), (947, 917, 'B'), (1028, 1133, 'C'), (1534, 1133, 'D'), (951, 1334, 'E')]),
}

def badge(d, x, y, t, r=30):
    d.ellipse((x - r, y - r, x + r, y + r), fill='#1d2747', outline='white', width=5)
    d.text((x, y), t, fill='white', font=FONT, anchor='mm')

for k, b in B.items():
    im = Image.open(os.path.join(HI, k + '.png')).convert('RGB'); W, H = im.size
    if b[2] <= 1:
        b = (int(b[0] * W), int(b[1] * H), int(b[2] * W), int(b[3] * H))
    im.crop(b).save(os.path.join(OUT, k + '.jpg'), quality=84)
for k, (src, box, masks, labels) in Q.items():
    im = Image.open(os.path.join(HI, src + '.png')).convert('RGB'); d = ImageDraw.Draw(im)
    for m in masks:
        if len(m) == 5:
            c = im.getpixel((m[0] + 6, m[1] + 6))
        else:
            cs = [im.getpixel((x, y)) for x, y in ((m[0] - 4, m[1] - 4), (m[2] + 4, m[1] - 4), (m[0] - 4, m[3] + 4), (m[2] + 4, m[3] + 4))]
            c = tuple(sum(v[i] for v in cs) // 4 for i in range(3))
        d.rectangle(m[:4], fill=c)
    for x, y, t in labels:
        badge(d, x, y, t)
    im.crop(box).save(os.path.join(OUT, k + '.jpg'), quality=86)
print('ok')
