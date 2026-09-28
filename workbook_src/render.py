import sys, os, re
from playwright.sync_api import sync_playwright
import pymupdf
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build as B

def main():
    first = B.build()
    out = os.path.join(HERE, 'ch13_tmp.pdf')
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome')
        pg = b.new_page()
        pg.goto('file://' + os.path.join(HERE, 'ch13.html'))
        pg.wait_for_timeout(800)
        fit = pg.evaluate('window.FIT')
        pg.pdf(path=out, width='320mm', height='200mm', print_background=True, prefer_css_page_size=True)
        b.close()
    for f in fit:
        flag = '  <-- OVERFLOW' if (f[2] or f[4]) else ''
        print(f'{f[0]:5s} left {f[1]}  right {f[3]}{flag}')
    d = pymupdf.open(out)
    toc = [[1, '표지', 1], [1, '가이드 · 생존 키트 · 표 · 차례', 2]]
    for k, it in enumerate(B.ITEMS):
        lab = ('예제 ' if it['kind'] != 'PROBLEM' else '문제 ') + it['num'] + ' · ' + re.sub('<[^>]+>', '', it['ko_title'])
        toc.append([1, lab, first + k])
    d.set_metadata({'title': f'Lehninger 8e Ch.{B.CHAPTER} {B.CH_TITLE} — 예제 & 연습문제 풀이 노트', 'author': 'Claude'})
    d.save(os.path.join(HERE, 'final.pdf'), garbage=3, deflate=True)
    print('pages', len(d), 'expected', first + len(B.ITEMS) - 1)

main()
