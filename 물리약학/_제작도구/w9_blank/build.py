"""9주차 빈칸정답및해설 HTML 생성: python3 build.py <강의 PDF> → out.html (img/ 에 슬라이드 PNG)"""
import os, sys, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
here = os.path.dirname(os.path.abspath(__file__))
os.makedirs(f'{here}/img', exist_ok=True)
if len(sys.argv) > 1 and not os.path.exists(f'{here}/img/s-01.png'):
    subprocess.run(['pdftoppm', '-r', '110', '-png', sys.argv[1], f'{here}/img/s'], check=True)
from content import PAGES
foot = '물리약학 · 화학반응속도론 및 안정성 (1) (9주차) — 슬라이드별 원문 정리·설명·빈칸 정답'
n = len(PAGES)
body = '\n'.join(p.replace('{FOOT}', foot).replace('{PG}', f'{i+1} / {n}') for i, p in enumerate(PAGES))
open(f'{here}/out.html', 'w').write(f'<!doctype html><html lang="ko"><head><meta charset="utf-8"><link rel="stylesheet" href="style.css"></head><body>{body}</body></html>')
print('pages', n)
