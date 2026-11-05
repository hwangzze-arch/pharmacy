# -*- coding: utf-8 -*-
"""원본 통합풀이 페이지(벡터) + 새 [내 필기/치트키] 블록 + 교정 그림을 합쳐 최종 PDF를 만든다."""
import json, os, sys, io
import numpy as np
import pymupdf as fitz
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
SCR = os.path.join(HERE, '..')
SRC = '/home/user/pharmacy/유기화학'
sys.path.insert(0, HERE)
from content_notes import KEEP_TEAL

FILES = {17: 'CH17_알코올과페놀_통합풀이.pdf', 18: 'CH18_에터와에폭사이드_통합풀이.pdf',
         19: 'CH19_알데하이드와케톤_통합풀이.pdf', 20: 'CH20_카복실산과나이트릴_통합풀이.pdf',
         21: 'CH21_카복실산유도체_통합풀이.pdf'}
from selection import KEEP
FRONT_LEAD = 2          # 표지 + 교수님 시험 안내
AFTER_DIV = {21: 1}     # 21장 표지 뒤 '수업 핵심' 1쪽
PW, PH = 1134.0, 708.96

GRID = json.load(open(os.path.join(SCR, 'grid.json')))
SLOT_H = dict((k, v) for k, v in json.load(open(os.path.join(HERE, 'heights.json'))))
SLOT_KEYS = json.load(open(os.path.join(HERE, 'slot_keys.json')))

# 잘린 문제 그림 → 원서에서 다시 오려 같은 자리에 넣기: key: (원래 그림 bbox, (장, 원서 쪽, 원서 영역))
REPL = {
    '18-13': ((851.2, 104.3, 1082.2, 156.8), (18, 6, (230, 600, 382, 656))),
    '18-15': ((789.0, 98.3, 1082.2, 162.0), (18, 6, (158, 465, 454, 543))),
    '21-7':  ((845.2, 100.5, 1082.2, 160.5), (21, 6, (118, 240, 330, 302))),
    '21-10': ((722.2, 93.8, 1082.2, 183.8), (21, 9, (120, 58, 446, 148))),
    '21-14': ((891.0, 93.8, 1082.2, 168.8), (21, 12, (118, 518, 284, 602))),
    '21-27': ((412.5, 177.0, 726.8, 259.5), (21, 22, (124, 123, 488, 217))),
    '21-28': ((882.0, 93.8, 1082.2, 168.8), (21, 22, (118, 343, 272, 416))),
    '21-32': ((942.8, 94.5, 1082.2, 147.0), (21, 27, (118, 200, 226, 254))),
    '21-33': ((810.0, 93.8, 1082.2, 165.0), (21, 27, (120, 272, 354, 341))),
    '21-37': ((846.8, 98.3, 1082.2, 162.0), (21, 30, (224, 185, 388, 247))),
    '21-39': ((887.2, 112.5, 1082.2, 168.8), (21, 30, (118, 485, 337, 549))),
}
# 그림 가장자리에 걸린 다른 글자 조각 지우기: key: [(x0,y0,x1,y1) 흰 사각형]
TRIM = json.load(open(os.path.join(HERE, 'trim.json'))) if os.path.exists(os.path.join(HERE, 'trim.json')) else {}
# 그림 위에 글자 덧쓰기 (잘린 원자 기호 복원): key: [(x, y, text, size)]
ADDTXT = json.load(open(os.path.join(HERE, 'addtxt.json'))) if os.path.exists(os.path.join(HERE, 'addtxt.json')) else {}

TB = {c: fitz.open(os.path.join(SRC, f'맥머리 유기화학 10판 원서 {c}장.pdf')) for c in (18, 21)}


def overlay_xrefs(page):
    out = []
    for info in page.get_image_info(xrefs=True):
        b = info['bbox']
        if info['xref'] and b[2] - b[0] > 1100 and b[3] - b[1] > 700:
            out.append(info['xref'])
    return out


def teal_layer(doc, xref, y_from):
    """삼성노트 레이어에서 청록 동그라미만 뽑아 투명 PNG로."""
    pix = fitz.Pixmap(doc, xref)
    sm = doc.extract_image(xref).get('smask', 0)
    if sm:
        pix = fitz.Pixmap(pix, fitz.Pixmap(doc, sm))
    a = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.h, pix.w, pix.n).copy()
    r, g, b, al = a[..., 0].astype(int), a[..., 1].astype(int), a[..., 2].astype(int), a[..., 3]
    teal = (g > 150) & (b > 140) & (r < 140) & (al > 10)
    ys = np.arange(pix.h)[:, None] * (PH / pix.h)
    keep = teal & (ys > y_from)
    a[..., 3] = np.where(keep, al, 0)
    bio = io.BytesIO()
    Image.fromarray(a, 'RGBA').save(bio, 'PNG')
    return bio.getvalue()


def meta(page):
    no, title = '', ''
    for b in page.get_text('dict')['blocks']:
        for l in b.get('lines', []):
            for s in l['spans']:
                x0, y0 = s['bbox'][:2]
                if y0 < 60 and x0 < 140 and s['size'] > 15:
                    no += s['text']
                elif y0 < 50 and 140 <= x0 < 900 and s['size'] > 17:
                    title += s['text']
    badge = page.get_text(clip=fitz.Rect(28, 10, 140, 34)).replace('\n', '').strip()
    tags = page.get_text(clip=fitz.Rect(700, 20, 1110, 50))
    kind = '과제' if ('과제' in badge or '과제 문제' in tags) else ('예제' if '예제' in badge else ('참고' if '참고' in badge else '본문'))
    import re
    m = re.match(r'^([\d.\-]+(?:\s*[ⓐ-ⓩ①-⑳]+)*)\s*(.*)$', no.strip())
    if m:
        no, title = m.group(1).strip(), (m.group(2) + title).strip()
    return kind, no, title


KEEPALIVE = []


def build(out_path, front_pdf, plan_out=None):
    slots = fitz.open(os.path.join(HERE, 'slots.pdf'))
    out = fitz.open()
    front = fitz.open(front_pdf) if front_pdf else None
    plan = []
    fp = 0
    if front:
        out.insert_pdf(front, from_page=0, to_page=FRONT_LEAD - 1)  # 표지 + 시험 안내
        fp = FRONT_LEAD
    total_pages = None
    toc = []
    pages_meta = []
    for ch, fn in FILES.items():
        src = fitz.open(os.path.join(SRC, fn))
        KEEPALIVE.append(src)  # 문서 객체 id 재사용으로 graft 캐시가 꼬이는 것 방지
        # 원본 저장 전 overlay 정보 확보
        ovmap = {}
        for pn in KEEP[ch]:
            xs = overlay_xrefs(src[pn - 1])
            ovmap[pn] = xs
        tealimg = {}
        for pn in KEEP[ch]:
            k = f'{ch}-{pn}'
            if k in KEEP_TEAL and ovmap[pn]:
                tealimg[pn] = teal_layer(src, ovmap[pn][0], GRID[k]['grid'][3] + 2)
        for pn in KEEP[ch]:
            for x in ovmap[pn]:
                src[pn - 1].delete_image(x)
        toc.append([1, f'{ch}장', len(out) + 1])
        if front:
            extra = AFTER_DIV.get(ch, 0)
            out.insert_pdf(front, from_page=fp, to_page=fp + extra)  # 장 표지 (+ 수업 정리)
            fp += 1 + extra
        for pn in KEEP[ch]:
            k = f'{ch}-{pn}'
            sp = src[pn - 1]
            kind, no, title = meta(sp)
            g = GRID[k]['grid']
            gy0, gy1 = g[1], g[3]
            hg = gy1 - gy0
            hs = SLOT_H[k]
            delta = max(0.0, hs - hg)
            ph = PH + delta
            np_ = out.new_page(width=PW, height=ph)
            np_.show_pdf_page(fitz.Rect(0, 0, PW, gy0), src, pn - 1, clip=fitz.Rect(0, 0, PW, gy0))
            sh = max(hs, hg)
            one = fitz.open()
            one.insert_pdf(slots, from_page=SLOT_KEYS.index(k), to_page=SLOT_KEYS.index(k))
            one = fitz.open('pdf', one.tobytes(garbage=3))
            KEEPALIVE.append(one)
            np_.show_pdf_page(fitz.Rect(27, gy0, 1107, gy0 + sh), one, 0, clip=fitz.Rect(0, 0, 1080, sh))
            np_.show_pdf_page(fitz.Rect(0, gy1 + delta, PW, PH + delta), src, pn - 1,
                              clip=fitz.Rect(0, gy1, PW, PH))
            if pn in tealimg:
                np_.insert_image(fitz.Rect(0, delta, PW, PH + delta), stream=tealimg[pn])
            # 잘린 그림 교정
            if k in REPL:
                (x0, y0, x1, y1), (c, p, r) = REPL[k]
                np_.draw_rect(fitz.Rect(x0 - 1, y0 - 1, x1 + 1, y1 + 1), color=None, fill=(1, 1, 1))
                pix = TB[c][p - 1].get_pixmap(dpi=300, clip=fitz.Rect(*r))
                ar = pix.width / pix.height
                bw, bh = x1 - x0, (y1 - y0)
                if bw / bh > ar:
                    w = bh * ar; h = bh
                else:
                    w = bw; h = bw / ar
                cx = x1 - w  # 원래처럼 오른쪽 정렬
                if k == '21-27':
                    cx = x0 + (bw - w) / 2
                np_.insert_image(fitz.Rect(cx, y0, cx + w, y0 + h), stream=pix.tobytes('png'))
            for rr in TRIM.get(k, []):
                np_.draw_rect(fitz.Rect(*rr), color=None, fill=(1, 1, 1))
            for (x, y, t, s) in ADDTXT.get(k, []):
                np_.insert_text((x, y), t, fontsize=s, fontname='helv', color=(0.12, 0.12, 0.12))
            # 쪽 번호 바꾸기 (원본 "n / N" 지우기)
            hits = sp.search_for(f'{pn} / {len(src)}')
            for h_ in hits:
                if h_.y0 > 670:
                    rr = fitz.Rect(h_.x0 - 4, h_.y0 - 1 + delta, h_.x1 + 2, h_.y1 + 1 + delta)
                    np_.draw_rect(rr, color=None, fill=(1, 1, 1))
            pages_meta.append((len(out), ph))
            toc.append([2, f'{no}  {title}', len(out)])
            plan.append(dict(key=k, ch=ch, kind=kind, no=no, title=title, page=len(out)))
    n = len(out)
    for (pi, ph) in pages_meta:
        pg = out[pi - 1]
        txt = f'{pi} / {n}'
        tw = fitz.get_text_length(txt, fontname='helv', fontsize=8.6)
        pg.insert_text((1107 - tw, ph - 15.6), txt, fontsize=8.6, fontname='helv', color=(0.42, 0.46, 0.53))
    out.set_toc(toc)
    out.set_metadata({'title': '약품유기화학2 중간고사 17–21장 문제·해설 + 치트키', 'author': 'hwangzze',
                      'subject': '맥머리 유기화학 10판 17–21장 · 예제·본문 문제·과제'})
    out.save(out_path, garbage=3, deflate=True)
    if plan_out:
        json.dump(plan, open(plan_out, 'w'), ensure_ascii=False, indent=0)
    print('pages', n)


if __name__ == '__main__':
    build(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 and sys.argv[2] != '-' else None,
          sys.argv[3] if len(sys.argv) > 3 else None)
