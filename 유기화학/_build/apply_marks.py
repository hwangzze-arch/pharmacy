# -*- coding: utf-8 -*-
"""final_v4raw.pdf(21장 필기 반영) 위에 사용자의 동그라미 표시를 다시 얹고, 빨간 네모 문제에 '제외' 표시 → final_v4.pdf"""
import json, os, io, sys
import numpy as np
import pymupdf as fitz
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from marks21 import F, overlays, comps

SCR = os.path.join(HERE, '..')
GRID = json.load(open(os.path.join(SCR, 'grid.json')))
H3 = dict(json.load(open(os.path.join(HERE, 'heights_v3.json'))))
H4 = dict(json.load(open(os.path.join(HERE, 'heights.json'))))
PLAN = {x['key']: x['page'] for x in json.load(open(os.path.join(HERE, 'plan_v4.json')))}
USER_PAGE = {}   # key -> 사용자 파일 쪽 (3쪽부터 21-7…)
KEYS21 = [k for k in sorted(PLAN, key=lambda k: PLAN[k]) if k.startswith('21-')]
for i, k in enumerate(KEYS21):
    USER_PAGE[k] = i + 3

# 쪽별 처리: 'all' = 오버레이 전체 유지, 'circles' = 밝은 빨강/청록 동그라미만, ('xref', n) = 그 레이어만
RULE = {'21-12': 'circles', '21-14': ('xref', 4308), '21-17': 'all', '21-28': 'noteal', '21-40': 'circles', '21-41': 'circles'}
EXCLUDED = ['21-18', '21-27', '21-39']
STAMP = fitz.open(os.path.join(HERE, 'stamp.pdf'))


def delta(H, k):
    g = GRID[k]['grid']
    return max(0.0, H[k] - (g[3] - g[1]))


def keep_mask(a, mode):
    al = a[..., 3]
    if mode == 'all':
        return al > 0
    if mode == 'noteal':  # 청록 손글씨(문제 그림 위 –OCH₃/–H)만 빼고 나머지 유지
        r, g, b = a[..., 0].astype(int), a[..., 1].astype(int), a[..., 2].astype(int)
        ys = np.arange(a.shape[0])[:, None] * (708.96 / a.shape[0])
        return (al > 0) & (ys > 250)  # 문제 칸(위쪽) 손글씨는 전부 제거, 메모 칸 그림만 유지
    m = al[::2, ::2] > 40
    keep = np.zeros(al.shape, bool)
    for x0, y0, x1, y1, n in comps(m):
        if (x1 - x0) < 5 or (y1 - y0) < 5:
            continue
        sl = (slice(y0 * 2, (y1 + 1) * 2), slice(x0 * 2, (x1 + 1) * 2))
        px = a[sl][al[sl] > 40][:, :3].astype(int)
        if not len(px):
            continue
        r, g, b = px.mean(0)
        bright_red = r > 175 and g < 80
        teal = g > 150 and b > 140 and r < 120
        if bright_red or teal:
            keep[sl] |= al[sl] > 0
    return keep


def main(src, dst):
    user = fitz.open(F)
    d = fitz.open(src)
    for k, mode in RULE.items():
        up = USER_PAGE[k] - 1
        shift = delta(H4, k) - delta(H3, k)
        pg = d[PLAN[k] - 1]
        for x, b, a in overlays(user, up):
            if isinstance(mode, tuple):
                if x != mode[1]:
                    continue
                m = 'all'
            else:
                m = mode
            km = keep_mask(a, m)
            if not km.any():
                continue
            out = a.copy()
            out[..., 3] = np.where(km, a[..., 3], 0)
            bio = io.BytesIO()
            Image.fromarray(out, 'RGBA').save(bio, 'PNG')
            pg.insert_image(fitz.Rect(b[0], b[1] + shift, b[2], b[3] + shift), stream=bio.getvalue())
        print(k, 'page', PLAN[k], 'shift', round(shift, 1))
    for k in EXCLUDED:
        pg = d[PLAN[k] - 1]
        pg.show_pdf_page(fitz.Rect(867, 60, 1107, 84), STAMP, 0)
    d.save(dst, garbage=4, deflate=True, use_objstms=1)
    print('saved', len(d))


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
