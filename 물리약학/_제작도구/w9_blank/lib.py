"""빈칸정답및해설 PDF 공통 함수 (슬라이드 1장 = A4 가로 1쪽)."""
import html

def A(t):
    """빈칸 정답 (파란 박스)"""
    return f'<b class="a">{t}</b>'

def Y(t):  return f'<mark class="y">{t}</mark>'   # 핵심 개념
def G(t):  return f'<mark class="g">{t}</mark>'   # 공식·정의·결론
def P(t):  return f'<mark class="p">{t}</mark>'   # 시험 포인트

def F(n, d):
    """분수"""
    return f'<span class="fr"><span>{n}</span><span>{d}</span></span>'

def eq(*lines):
    """공식 상자 (초록 띠)"""
    return '<div class="eq">' + '<br>'.join(lines) + '</div>'

def tbl(head, rows, cls=''):
    h = ''.join(f'<th>{c}</th>' for c in head)
    b = ''.join('<tr>' + ''.join(f'<td>{c}</td>' for c in r) + '</tr>' for r in rows)
    return f'<table class="t {cls}"><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table>'

def box(kind, label, text):
    """kind: warn(혼동 주의, 분홍) / exam(시험 포인트, 분홍) / tip(비유·팁, 파랑)"""
    return f'<div class="box {kind}"><b>{label}</b> {text}</div>'

def h4(t):
    return f'<h4>{t}</h4>'

def ul(*items):
    return '<ul>' + ''.join(f'<li>{i}</li>' for i in items) + '</ul>'


def graph(kind, w=150, h=105, ylab='[A]', note=''):
    """간단한 개형 그래프 SVG. kind: line_down, line_up, exp_down, inv_down"""
    x0, y0, x1, y1 = 28, 10, w - 8, h - 18
    if kind == 'line_down':
        path = f'M{x0+2},{y0+6} L{x1-14},{y1-2}'
    elif kind == 'line_up':
        path = f'M{x0+2},{y1-14} L{x1-6},{y0+6}'
    elif kind == 'exp_down':
        pts = []
        for i in range(41):
            t = i / 40
            pts.append(f'{x0+2+(x1-x0-6)*t:.1f},{y1-2-(y1-y0-10)*(2.718**(-3.2*t)):.1f}')
        path = 'M' + ' L'.join(pts)
    else:  # inv_down
        pts = []
        for i in range(41):
            t = i / 40
            pts.append(f'{x0+2+(x1-x0-6)*t:.1f},{y1-2-(y1-y0-10)/(1+6*t):.1f}')
        path = 'M' + ' L'.join(pts)
    return f'''<svg class="gr" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
<line x1="{x0}" y1="{y0}" x2="{x0}" y2="{y1}" stroke="#333" stroke-width="1.2"/>
<line x1="{x0}" y1="{y1}" x2="{x1}" y2="{y1}" stroke="#333" stroke-width="1.2"/>
<path d="{path}" fill="none" stroke="#1d4ed8" stroke-width="2"/>
<text x="{x0-4}" y="{y0+10}" font-size="10" text-anchor="end">{ylab}</text>
<text x="{x1-2}" y="{y1+13}" font-size="10" text-anchor="end">t</text>
<text x="{(x0+x1)/2+8}" y="{y0+12}" font-size="10" fill="#b91c1c">{note}</text>
</svg>'''


def page(no, title, sub, slide, kw, summary, left, right, left_title='원문 정리 (빈칸 정답 채움)', img=None):
    kws = ''.join(f'<span class="chip">{k}</span>' for k in kw)
    imgs = img if img is not None else [f'img/s-{slide:02d}.png'] if isinstance(slide, int) else []
    imghtml = ''.join(f'<img src="{s}">' for s in imgs)
    slabel = f'원본 슬라이드 {slide}' if isinstance(slide, int) else f'원본 슬라이드 {slide}'
    return f'''<section class="page">
<header><span class="no">{no:02d}</span><div class="ttl"><h1>{title}</h1><div class="sub">{sub}</div></div><div class="src">{slabel}</div></header>
<div class="top">
  <div class="kw"><div class="lbl">핵심 키워드</div>{kws}</div>
  <div class="img n{len(imgs)}">{imghtml}</div>
  <div class="sum"><div class="lbl">한 줄 요약</div><p>{summary}</p></div>
</div>
<div class="bot">
  <div class="col l"><div class="pill navy">{left_title}</div>{left}</div>
  <div class="col r"><div class="pill orange">상세 설명 · 풀이</div>{right}</div>
</div>
<footer><span class="ft">{{FOOT}}</span><span class="leg">형광펜 <i class="y"></i>핵심 개념 <i class="g"></i>공식·정의·결론 <i class="p"></i>시험 포인트 / Q&amp;A <i class="a"></i>빈칸 정답</span><span class="pg">{{PG}}</span></footer>
</section>'''
