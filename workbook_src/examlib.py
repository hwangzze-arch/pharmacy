# -*- coding: utf-8 -*-
"""시험대비 요약노트 공통 엔진 (13장 exam13.py와 같은 디자인).
장별 파일(examNN.py)이 CH, CH_TITLE, FOOT, WB, SUMMARY, CHECKS, CHECK_AFTER, GLOSS, ABBR_KEYS, MAPROWS 를 정의하고
examlib.render(module) 을 호출한다."""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from helpers import *

HERE = os.path.dirname(os.path.abspath(__file__))


def make_link(WB, ch):
    def link(*ids):
        parts = []
        for i in ids:
            lab = '예제 ' + i[2:] if i.startswith('WE') else '문제 ' + i[1:]
            parts.append(f'<span class="wl">{lab} <i>p.{WB[i]}</i></span>')
        return f'<div class="wlink"><b>📒 풀이노트로 이어서 풀기</b>{"".join(parts)}</div>'
    return link


def make_page(link):
    def page(no, title, en, lead, body, links=()):
        lk = link(*links) if links else ''
        return (f'<h2 class="pt"><span class="n">{no}</span> {title} <span class="en2">{en}</span></h2>'
                f'<p class="lead">{lead}</p>{body}{lk}')
    return page


def _plain(html):
    t = re.sub(r'</?(sub|sup)>', '', html)
    t = re.sub(r'<[^>]+>', ' ', t)
    return t.replace('&nbsp;', ' ')


def abbr_strip(M, html, compact=False):
    t = _plain(html)
    found = [g for g in M.GLOSS if g[0] in M.ABBR_KEYS and re.search(M.ABBR_KEYS[g[0]], t)]
    if not found:
        return ''
    chips = ''.join(f'<span class="ab"><b>{a}</b> <i>{e}</i> <em>{h}</em> <u>— {m}</u></span>' for a, e, h, m in found)
    return f'<div class="abbr{" cmp" if compact else ""}"><b class="h">🔤 이 페이지의 약어</b>{chips}</div>'


def render_check(M, it):
    return f'''
<div class="ph"><div class="badge" style="background:#7c3aed"><small>개념 확인</small><b>{it['num']}</b></div>
 <div class="ttl"><span class="ko">{it['title']}</span><span class="en">관련 요약 ▸ {it['sec']}</span></div>
 <div class="meta"><span class="tag">스스로 점검</span>{stars(it['level'])}</div></div>
<div class="cols">
 <div class="col">
  <div class="blk trans"><span class="lab" style="background:#7c3aed">문제</span>{it['q']}</div>
  <div class="blk blank"><span class="lab">풀이 · 직접 풀어 보기</span><span class="hint">오른쪽을 가리고 풀어 보세요</span></div>
  {abbr_strip(M, it['q'] + it['answer'], True)}
 </div>
 <div class="col">
  <div class="blk ans"><span class="lab">정답</span>{it['answer']}</div>
  <div class="blk exp"><span class="lab">해설</span>{it['explain']}</div>
 </div>
</div>'''


def cover(M):
    return f'''
<div class="eyebrow">LEHNINGER PRINCIPLES OF BIOCHEMISTRY · 8TH EDITION</div>
<h1>Chapter {M.CH}<br><span style="font-size:{'36pt' if len(M.CH_TITLE) <= 10 else '27pt'}">{M.CH_TITLE}</span><br>시험대비 요약노트</h1>
<div class="sub">개념 요약 {len(M.SUMMARY)}쪽 + 개념확인 문제 {len(M.CHECKS)}세트 + 영어 약어 총정리</div>
<div class="en">“풀이노트의 문제를 풀기 전에 이 노트로 개념부터”</div>
<div class="stats">
 <div class="stat"><b>{len(M.SUMMARY)}</b><span>개념 요약 페이지<br>(강의 슬라이드 순서)</span></div>
 <div class="stat"><b>{len(M.CHECKS)}</b><span>개념확인 문제 세트<br>(OX·빈칸·계산)</span></div>
 <div class="stat"><b>{len(M.GLOSS)}</b><span>영어 약어·기호<br>총정리</span></div>
</div>
<div class="how"><h3>HOW TO USE · 이렇게 보세요</h3>
 <div style="background:#1e3a8a"><b>① 요약 읽기</b>그림과 한 줄 요약으로 개념 잡기</div>
 <div style="background:#7c3aed"><b>② 개념확인</b>OX·빈칸·짧은 계산으로 점검</div>
 <div style="background:#ea580c"><b>③ 풀이노트로</b>각 페이지 아래 “📒”에 적힌 문제·쪽수로 이동</div>
 <div style="background:#0f766e"><b>④ 약어 찾기</b>페이지마다 “🔤 이 페이지의 약어” + 맨 뒤 총정리</div>
 <p style="font-size:8.5pt;color:#cbd5e1;margin-top:3mm">함께 볼 파일: <b>레닌저 {M.CH}장 예제·문제 풀이노트.pdf</b><br>📒 옆의 p.번호 = 풀이노트의 쪽번호</p>
</div>'''


def toc(M):
    rows = []
    for k, pg in enumerate(M.SUMMARY):
        t = pg.split('</span> ', 1)[1].split(' <span class="en2">')[0]
        rows.append(f'<tr><td class="no">S{k+1}</td><td>{t}</td></tr>')
    rows2 = [f'<tr><td class="no">개념확인 {c["num"]}</td><td>{c["title"]} <span class="en">({c["sec"]})</span></td></tr>' for c in M.CHECKS]
    rows2.append('<tr><td class="no">ABC</td><td>영어 약어·기호 총정리</td></tr>')
    return f'''<h2 class="pt"><span class="n">INDEX</span> 차례와 풀이노트 연결표</h2>
<div class="grid2"><div class="card"><h4>📘 개념 요약</h4><table class="toc">{''.join(rows)}</table></div>
<div><div class="card"><h4>✏️ 개념확인 · 부록</h4><table class="toc">{''.join(rows2)}</table></div>
<div class="card" style="margin-top:3mm"><h4>📒 풀이노트 문제는 어디서 배우나?</h4>{table(['요약', '풀이노트 문제'], M.MAPROWS, cls='left')}</div></div></div>'''


def glossary_pages(M):
    half = (len(M.GLOSS) + 1) // 2
    out = []
    for k, chunk in enumerate([M.GLOSS[:half], M.GLOSS[half:]]):
        rows = [[f'<b>{a}</b>', f'<span class="en3">{e}</span>', h, m] for a, e, h, m in chunk]
        out.append(f'''<h2 class="pt"><span class="n">ABC</span> {M.CH}장 영어 약어·기호 총정리 ({k+1}/2) <span class="en2">Abbreviations</span></h2>
<p class="lead">요약·문제에 나오는 약어를 모두 모았어. 뜻을 모르는 약어가 나오면 여기서 찾자.</p>
<div class="card" style="width:100%">{table(['약어·기호', '영어 원래 이름', '한글', '한 줄 뜻'], rows, cls='left gl')}</div>''')
    return out


def build(M):
    os.environ['CH'] = str(M.CH)
    import build as B
    from exam13 import EXTRA_CSS, FIT
    P = B.Pager()
    P.add(cover(M), 'cover')
    P.add(toc(M), 'front')
    for k, pg in enumerate(M.SUMMARY):
        strip = abbr_strip(M, pg)
        pg = pg.replace('<div class="wlink">', strip + '<div class="wlink">', 1) if '<div class="wlink">' in pg else pg + strip
        P.add(pg, 'front')
        if k in M.CHECK_AFTER:
            c = [x for x in M.CHECKS if x['id'] == M.CHECK_AFTER[k]][0]
            P.add(render_check(M, c), 'item')
    for g in glossary_pages(M):
        P.add(g, 'front')
    html = re.sub(r'<span>Lehninger 8e · Ch\.\d+ [^<]*</span>', f'<span>{M.FOOT}</span>', P.html())
    doc = f'''<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>{M.FOOT}</title>
<style>{B.CSS}{EXTRA_CSS}</style></head><body>{html}{FIT}</body></html>'''
    open(os.path.join(HERE, f'exam_ch{M.CH}.html'), 'w').write(doc)
    return len(P.pages)


def render(M):
    from playwright.sync_api import sync_playwright
    import pymupdf
    n = build(M)
    tmp = os.path.join(HERE, f'exam_ch{M.CH}_tmp.pdf')
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome')
        pg = b.new_page()
        pg.goto('file://' + os.path.join(HERE, f'exam_ch{M.CH}.html'))
        pg.wait_for_timeout(900)
        print('fit', pg.evaluate('window.FIT'))
        print('zoom', pg.evaluate('window.ZOOM'))
        pg.pdf(path=tmp, width='320mm', height='200mm', print_background=True, prefer_css_page_size=True)
        b.close()
    d = pymupdf.open(tmp)
    d.set_metadata({'title': M.FOOT, 'author': 'Claude'})
    d.save(os.path.join(HERE, f'exam_ch{M.CH}.pdf'), garbage=3, deflate=True)
    print('pages', len(d), 'expected', n)
