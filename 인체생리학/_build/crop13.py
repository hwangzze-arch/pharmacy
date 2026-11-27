"""13·14장 그림 자르기 + 그림 각주 문제용 라벨. crop9.py와 같은 방식.
사용: 슬라이드를 220dpi PNG(c13-NN.png, c14-NN.png)로 렌더한 폴더를 주고 python3 crop13.py 폴더
  pdftoppm -r 220 -png "Chapter 13_The Respiratory System.pdf" 폴더/c13
  pdftoppm -r 220 -png "Chapter 14_The Urinary System.pdf" 폴더/c14"""
import os, sys
from PIL import Image, ImageDraw, ImageFont
HI = sys.argv[1] if len(sys.argv) > 1 else 'hi'
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fig')
FONT = ImageFont.truetype(os.path.expanduser('~/.fonts/Pretendard-ExtraBold.ttf'), 40)
B = {  # 요약 페이지용: 이름 -> 비율 (x0, y0, x1, y1) 또는 픽셀 박스
     'c13-06': (.58, .12, 1, .98), 'c13-10': (0, .1, 1, .9), 'c13-12': (0, .12, 1, .92), 'c13-17': (0, .15, 1, .8),
     'c13-20': (0, .1, 1, .98), 'c13-24': (.45, .235, 1, .96), 'c13-29': (0, .12, 1, .98), 'c13-35': (0, .1, 1, 1),
     'c13-39': (.62, .1, 1, .98), 'c13-41': (.58, .4, 1, .98), 'c13-42': (.28, .45, .9, 1), 'c13-47': (0, .17, .52, 1),
     'c13-49': (0, .5, 1, .98),
     'c14-06': (.27, .12, 1, .98), 'c14-11': (.5, .53, 1, .98), 'c14-16': (.25, .1, .75, 1), 'c14-18': (.2, .5, .8, 1),
     'c14-19': (.62, .1, 1, .95), 'c14-22': (.575, .12, 1, .98), 'c14-26': (.25, .12, 1, .85), 'c14-31': (.2, .14, .85, 1),
     'c14-33': (.25, .1, .75, 1), 'c14-43': (0, .12, 1, .98), 'c14-44': (0, .12, 1, .78), 'c14-45': (0, .12, .8, 1)}
# 그림 각주: 이름 -> (원본 슬라이드, 픽셀 crop, 가릴 상자 [x0,y0,x1,y1(,'in')], 라벨 (x, y, 글자))
Q = {
 'c13-47-q': ('c13-47', (0, 300, 1150, 1600),
   [(472, 1050, 770, 1150), (472, 1150, 745, 1232), (265, 1210, 672, 1308), (472, 1308, 862, 1398), (472, 1400, 862, 1492)],
   [(600, 1100, 'A'), (600, 1192, 'B'), (470, 1258, 'C'), (660, 1352, 'D'), (660, 1446, 'E')]),
 'c14-16-q': ('c14-16', (550, 210, 1650, 1290),
   [(700, 242, 808, 308), (1102, 242, 1210, 308), (648, 442, 798, 476), (648, 493, 782, 560), (1182, 774, 1322, 842), (770, 918, 890, 1080)],
   [(754, 275, 'A'), (1156, 275, 'B'), (723, 459, 'C'), (715, 526, 'D'), (1252, 808, 'E'), (830, 999, 'F')]),
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
