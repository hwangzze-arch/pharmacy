"""11주차(2-1) 빈칸정답및해설 HTML 생성: python3 build.py <강의 PDF> → out.html (공통 함수·CSS는 ../w9_blank)"""
import os, sys, subprocess
here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, here)
sys.path.insert(1, os.path.join(here, '..', 'w9_blank'))
os.makedirs(f'{here}/img', exist_ok=True)
if len(sys.argv) > 1 and not os.path.exists(f'{here}/img/s-01.png'):
    subprocess.run(['pdftoppm', '-r', '110', '-png', sys.argv[1], f'{here}/img/s'], check=True)
from content import PAGES
foot = '물리약학 각론 · 화학반응속도론 및 안정성 2-1 (11주차) — Recap 빈칸 정답·기출 풀이'
n = len(PAGES)
body = '\n'.join(p.replace('{FOOT}', foot).replace('{PG}', f'{i+1} / {n}') for i, p in enumerate(PAGES))
open(f'{here}/out.html', 'w').write(f'<!doctype html><html lang="ko"><head><meta charset="utf-8"><link rel="stylesheet" href="../w9_blank/style.css"></head><body>{body}</body></html>')
print('pages', n)
