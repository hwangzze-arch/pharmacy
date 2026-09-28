import sys, os, json, re, subprocess
from playwright.sync_api import sync_playwright
import pymupdf
HERE = os.path.dirname(os.path.abspath(__file__))
FOOT = '''<div style="width:100%;font-family:'Noto Sans KR';font-size:7.5pt;color:#94a3b8;padding:0 14mm;display:flex;justify-content:space-between;">
<span>Lehninger 8e · Ch.13 생체에너지론 — 예제 &amp; 연습문제 풀이 노트</span><span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>'''
def pdf(out):
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome')
        pg = b.new_page()
        pg.goto('file://' + os.path.join(HERE, 'ch13.html'))
        pg.wait_for_timeout(500)
        pg.pdf(path=out, format='A4', print_background=True, display_header_footer=True,
               header_template='<div></div>', footer_template=FOOT, prefer_css_page_size=True)
        b.close()
def pages(path):
    d = pymupdf.open(path); res = {}
    for i, p in enumerate(d):
        for m in re.findall(r'@@(\w+)@@', p.get_text()):
            res.setdefault(m, i + 1)
    return res
if __name__ == '__main__':
    out = os.path.join(HERE, 'ch13.pdf')
    subprocess.run([sys.executable, os.path.join(HERE, 'build.py')], check=True)
    pdf(out)
    pg = pages(out)
    json.dump(pg, open(os.path.join(HERE, 'pages.json'), 'w'))
    subprocess.run([sys.executable, os.path.join(HERE, 'build.py')], check=True)
    pdf(out)
    assert pages(out) == pg, 'page drift'
    # replace cover (page 1) with a footer-less render
    nf = os.path.join(HERE, 'nofoot.pdf')
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome')
        pgx = b.new_page(); pgx.goto('file://' + os.path.join(HERE, 'ch13.html')); pgx.wait_for_timeout(500)
        pgx.pdf(path=nf, format='A4', print_background=True, page_ranges='1', prefer_css_page_size=True); b.close()
    d = pymupdf.open(out); c = pymupdf.open(nf)
    d.delete_page(0); d.insert_pdf(c, from_page=0, to_page=0, start_at=0)
    toc = [[1, '표지', 1], [1, '가이드 · 생존 키트 · 표', 2]]
    names = {}
    import importlib.util
    sys.path.insert(0, HERE)
    import build as B
    for it in B.ITEMS:
        lab = ('예제 ' if it['kind'] != 'PROBLEM' else '문제 ') + it['num'] + ' · ' + re.sub('<[^>]+>', '', it['ko_title'])
        toc.append([1, lab, pg[it['id']]])
    d.set_toc(toc)
    d.set_metadata({'title': 'Lehninger 8e Ch.13 생체에너지론 — 예제 & 연습문제 풀이 노트', 'author': 'Claude', 'subject': 'Bioenergetics worked examples and problems'})
    final = os.path.join(HERE, 'final.pdf')
    d.save(final, garbage=3, deflate=True)
    print('pages', len(pymupdf.open(out)), pg)
