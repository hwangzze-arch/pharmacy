# -*- coding: utf-8 -*-
"""반응 메커니즘 그림: RDKit 구조식 + 곡선 화살표(전자 이동).

SMILES의 원자 번호(:n)로 원자를 가리킨다. 번호는 그림에서 지워진다.
  arrows: [(src, dst, bend), ...]
    src = n (원자 n의 비공유전자쌍, 점 두 개 표시) | (n, m) (n–m 결합)
    dst = n (원자 n 쪽으로)                         | (n, m) (n–m 사이에 새 결합)
    bend = 곡률(+ 왼쪽, − 오른쪽, 기본 0.35)
"""
import math
from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem.Draw import rdMolDraw2D

ARC = "#d6247a"
# [n*] 원자의 표시 글자
DUMMY = {0: "R", 1: "R'", 2: "Ar", 3: "Bu", 4: "Ph", 5: "Et", 6: "t-Bu", 7: "X"}


def _mol(smiles):
    p = Chem.SmilesParserParams()
    p.removeHs = False
    m = Chem.MolFromSmiles(smiles, p)
    assert m is not None, smiles
    idx = {}
    for a in m.GetAtoms():
        if a.GetAtomicNum() == 0:  # * = R, [1*] = R′, [2*] = Ar
            a.SetProp("_displayLabel", DUMMY.get(a.GetIsotope(), "R"))
            a.SetIsotope(0)
        if a.GetAtomMapNum():
            idx[a.GetAtomMapNum()] = a.GetIdx()
            a.SetAtomMapNum(0)
    return m, idx


def _pt(d, i):
    p = d.GetDrawCoords(i)
    return (p.x, p.y)


def _sub(a, b):
    return (a[0] - b[0], a[1] - b[1])


def _unit(v):
    l = math.hypot(*v) or 1.0
    return (v[0] / l, v[1] / l)


def _layout(m, idx, rot, flip, pos, frot, ori, tmpl=None):
    """조각(. 로 나뉜 분자)마다 따로 좌표를 잡는다.
    ori = {조각: (a, b, 각도[, 뒤집기])}: 원자 a→b 방향을 각도(0=오른쪽, 90=위)로 돌리고, 뒤집기면 그 축으로 대칭.
    pos[k-1] = (dx, dy) 첫 조각 중심 기준 | (기준원자, 내원자, dx, dy) 내 원자를 기준 원자 + (dx,dy)Å 에."""
    AllChem.Compute2DCoords(m)
    conf = m.GetConformer()
    if tmpl:  # 고리 모양 등 원하는 배치: 원자 번호가 같은 템플릿 분자의 좌표를 그대로 씀
        tm, tidx = _mol(tmpl)
        AllChem.Compute2DCoords(tm)
        tc = tm.GetConformer()
        for n, i in tidx.items():
            if n in idx:
                conf.SetAtomPosition(idx[n], tc.GetAtomPosition(i))
    frags = Chem.GetMolFrags(m)
    P = lambda i: (conf.GetAtomPosition(i).x, conf.GetAtomPosition(i).y)
    cent0 = None
    for k, fr in enumerate(frags):
        xs, ys = zip(*[P(i) for i in fr])
        cx, cy = sum(xs) / len(xs), sum(ys) / len(ys)
        o = (ori or {}).get(k)
        if o:
            (ax, ay), (bx, by) = P(idx[o[0]]), P(idx[o[1]])
            r = o[2] - math.degrees(math.atan2(by - ay, bx - ax))
        else:
            r = rot + (frot or {}).get(k, 0)
        c, s_ = math.cos(math.radians(r)), math.sin(math.radians(r))
        for i in fr:
            x, y = P(i)
            x, y = x - cx, y - cy
            if flip and not o:
                x = -x
            x, y = x * c - y * s_, x * s_ + y * c
            if o and len(o) > 3 and o[3]:
                t = math.radians(o[2])
                ux, uy = math.cos(t), math.sin(t)
                d = x * ux + y * uy
                x, y = 2 * d * ux - x, 2 * d * uy - y
            conf.SetAtomPosition(i, (x, y, 0))
        if k == 0:
            continue
        sp = pos[k - 1] if pos and k - 1 < len(pos) else (2.2 * k, 0)
        if len(sp) == 4:
            (ax, ay), (bx, by) = P(idx[sp[0]]), P(idx[sp[1]])
            dx, dy = ax + sp[2] - bx, ay + sp[3] - by
        else:
            dx, dy = sp
        for i in fr:
            x, y = P(i)
            conf.SetAtomPosition(i, (x + dx, y + dy, 0))


def panel(smiles, arrows=(), w=180, h=120, scale=26, rot=0, flip=False, hl=(), note="", pos=None, frot=None, ori=None, tmpl=None, hb=(), labels=None):
    """구조식 1칸 SVG. rot: 회전(도), flip: 좌우 반전, hl: 강조할 원자 번호,
    pos·ori: _layout 참고 (y는 위가 +, 1Å ≈ 결합 길이의 2/3)."""
    m, idx = _mol(smiles)
    for n, t in (labels or {}).items():  # 원자 하나를 글자로 (예: EtO⁻, (i-Pr)₂N⁻)
        m.GetAtomWithIdx(idx[n]).SetProp("_displayLabel", t)
    _layout(m, idx, rot, flip, pos, frot, ori, tmpl)
    d = rdMolDraw2D.MolDraw2DSVG(w, h)
    o = d.drawOptions()
    o.clearBackground = False
    o.bondLineWidth = 1.5
    o.fixedBondLength = scale
    o.padding = 0.16
    o.minFontSize = 11
    o.maxFontSize = 13
    o.additionalAtomLabelPadding = 0.1
    kw = {}
    if hl:
        ids = [idx[n] for n in hl]
        kw = dict(highlightAtoms=ids, highlightAtomColors={i: (1, .94, .5) for i in ids}, highlightBonds=[])
    d.DrawMolecule(m, **kw)
    d.FinishDrawing()
    svg = d.GetDrawingText()
    svg = svg[svg.index('<svg'):]

    def pos(x):
        if isinstance(x, tuple):
            a, b = _pt(d, idx[x[0]]), _pt(d, idx[x[1]])
            return ((a[0] + b[0]) / 2, (a[1] + b[1]) / 2), False
        return _pt(d, idx[x]), True

    extra = []
    for a_, b_ in hb:  # 수소결합(점선)
        pa, pb = _pt(d, idx[a_]), _pt(d, idx[b_])
        v = _unit(_sub(pb, pa))
        pa, pb = (pa[0] + v[0] * 7, pa[1] + v[1] * 7), (pb[0] - v[0] * 7, pb[1] - v[1] * 7)
        extra.append(f'<line x1="{pa[0]:.1f}" y1="{pa[1]:.1f}" x2="{pb[0]:.1f}" y2="{pb[1]:.1f}" stroke="#777" stroke-width="1.3" stroke-dasharray="3,2.5"/>')
    for ar in arrows:
        src, dst = ar[0], ar[1]
        bend = ar[2] if len(ar) > 2 else 0.35
        p0, s_atom = pos(src)
        p3, d_atom = pos(dst)
        v = _unit(_sub(p3, p0))
        nrm = (-v[1], v[0])
        if s_atom:  # 비공유전자쌍: 원자에서 곡선이 휘는 쪽으로 살짝 띄운 점 두 개
            side = 1 if bend >= 0 else -1
            lp = _unit((v[0] + nrm[0] * side * 0.9, v[1] + nrm[1] * side * 0.9))
            c = (p0[0] + lp[0] * 10, p0[1] + lp[1] * 10)
            t = (-lp[1], lp[0])
            for k in (-2.4, 2.4):
                extra.append(f'<circle cx="{c[0]+t[0]*k:.1f}" cy="{c[1]+t[1]*k:.1f}" r="1.4" fill="#222"/>')
            p0 = (c[0] + lp[0] * 3, c[1] + lp[1] * 3)
        dist = math.hypot(*_sub(p3, p0))
        if d_atom:  # 원자 글자에 닿기 전에 멈춤
            p3 = (p3[0] - v[0] * 8, p3[1] - v[1] * 8)
            dist = math.hypot(*_sub(p3, p0))
        v = _unit(_sub(p3, p0))
        nrm = (-v[1], v[0])
        off = bend * max(dist, 16)
        c1 = (p0[0] + (p3[0] - p0[0]) * .2 + nrm[0] * off, p0[1] + (p3[1] - p0[1]) * .2 + nrm[1] * off)
        c2 = (p0[0] + (p3[0] - p0[0]) * .8 + nrm[0] * off, p0[1] + (p3[1] - p0[1]) * .8 + nrm[1] * off)
        tg = _unit(_sub(p3, c2))
        L, W = 7.5, 3.6
        base = (p3[0] - tg[0] * L, p3[1] - tg[1] * L)
        q1 = (base[0] - tg[1] * W, base[1] + tg[0] * W)
        q2 = (base[0] + tg[1] * W, base[1] - tg[0] * W)
        extra.append(
            f'<path d="M{p0[0]:.1f},{p0[1]:.1f} C{c1[0]:.1f},{c1[1]:.1f} {c2[0]:.1f},{c2[1]:.1f} {base[0]:.1f},{base[1]:.1f}" '
            f'fill="none" stroke="{ARC}" stroke-width="1.5"/>'
            f'<polygon points="{p3[0]:.1f},{p3[1]:.1f} {q1[0]:.1f},{q1[1]:.1f} {q2[0]:.1f},{q2[1]:.1f}" fill="{ARC}"/>')
    svg = svg.replace('</svg>', "".join(extra) + '</svg>')
    cap = f'<span class="pn">{note}</span>' if note else ''
    return f'<span class="pnl">{svg}{cap}</span>'


def step(top="", bot="", rev=False):
    """반응 화살표(가역이면 rev=True)."""
    cls = "stp rev" if rev else "stp"
    return f'<span class="{cls}"><span class="at">{top}</span><span class="al"></span><span class="ab">{bot}</span></span>'


def mrow(*items, label=""):
    lab = f'<span class="ml">{label}</span>' if label else ''
    return f'<div class="mrow">{lab}{"".join(items)}</div>'


MECH_CSS = """
.mrow{display:flex;align-items:center;gap:0;margin:0 0 2px 0;flex-wrap:nowrap;overflow:hidden;}
.mrow .ml{flex:none;font-size:10.5px;font-weight:700;color:#fff;background:#2a9d8f;border-radius:4px;padding:1px 6px;margin-right:4px;}
.pnl{display:inline-flex;flex-direction:column;align-items:center;flex:none;}
.pnl svg{display:block;}
.pnl .pn{font-size:9.5px;color:#555;margin-top:-6px;white-space:nowrap;}
.stp{display:inline-flex;flex-direction:column;align-items:center;min-width:46px;font-size:9.5px;line-height:1.15;color:#1f3f66;flex:none;text-align:center;}
.stp .al{display:block;width:100%;height:0;border-top:1.4px solid #333;position:relative;margin:2px 0;}
.stp .al::after{content:'';position:absolute;right:-1px;top:-4.6px;border-left:7px solid #333;border-top:4px solid transparent;border-bottom:4px solid transparent;}
.stp.rev .al::before{content:'';position:absolute;left:-1px;top:-4.6px;border-right:7px solid #333;border-top:4px solid transparent;border-bottom:4px solid transparent;}
"""
