"""강의 PDF 슬라이드를 img<장>/s-01.jpg … 로 만든다. 사용: python3 make_img.py 9 "../../Chapter 9_Cardiac Physiology.pdf" """
import os, sys, subprocess, glob, tempfile
from PIL import Image
ch, pdf = sys.argv[1], sys.argv[2]
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), f'img{ch}'); os.makedirs(out, exist_ok=True)
with tempfile.TemporaryDirectory() as t:
    subprocess.run(['pdftoppm', '-r', '150', '-png', pdf, os.path.join(t, 's')], check=True)
    for f in sorted(glob.glob(os.path.join(t, 's-*.png'))):
        n = int(f.rsplit('-', 1)[1][:-4])
        im = Image.open(f).convert('RGB'); im.thumbnail((1200, 1200))
        im.save(os.path.join(out, f's-{n:02d}.jpg'), quality=85)
print('ok')
