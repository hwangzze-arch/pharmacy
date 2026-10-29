# -*- coding: utf-8 -*-
"""RDKit 구조식 SVG + 반응식 HTML 조각 (정답·풀이 페이지용)."""
from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem.Draw import rdMolDraw2D

PINK = (0.93, 0.33, 0.61)


def mol(smiles):
    """[H:1]처럼 원자 번호 1을 단 원자는 강조 대상으로 돌려준다."""
    p = Chem.SmilesParserParams()
    p.removeHs = False
    m = Chem.MolFromSmiles(smiles, p)
    assert m is not None, smiles
    hl = []
    for a in m.GetAtoms():
        if a.GetAtomMapNum() == 1:
            hl.append(a.GetIdx())
            a.SetAtomMapNum(0)
    return m, hl


def svg(smiles, w=150, h=95, scale=22):
    m, hl = mol(smiles)
    AllChem.Compute2DCoords(m)
    d = rdMolDraw2D.MolDraw2DSVG(w, h)
    o = d.drawOptions()
    o.clearBackground = False
    o.bondLineWidth = 1.6
    o.fixedBondLength = scale
    o.padding = 0.08
    o.minFontSize = 11
    o.maxFontSize = 13
    o.additionalAtomLabelPadding = 0.08
    o.highlightRadius = 0.32
    kw = {}
    if hl:
        kw = dict(highlightAtoms=hl, highlightAtomColors={i: PINK for i in hl}, highlightBonds=[])
    d.DrawMolecule(m, **kw)
    d.FinishDrawing()
    s = d.GetDrawingText()
    return s[s.index('<svg'):]


def arrow(top="", bot=""):
    return (f'<span class="arw"><span class="at">{top}</span>'
            f'<span class="al"></span><span class="ab">{bot}</span></span>')


def row(*items, label=""):
    """items: ('m', smiles[, w, h]) 구조식 / ('a', 위, 아래) 화살표 / ('t', 글자)."""
    out = []
    for it in items:
        if it[0] == 'm':
            out.append(f'<span class="mol">{svg(*it[1:])}</span>')
        elif it[0] == 'a':
            out.append(arrow(*it[1:]))
        else:
            out.append(f'<span class="tx">{it[1]}</span>')
    lab = f'<span class="rl">{label}</span>' if label else ''
    return f'<div class="rx">{lab}{"".join(out)}</div>'


def cap(smiles, text, w=150, h=95):
    return f'<span class="cap">{svg(smiles, w, h)}<span>{text}</span></span>'


def check(*smiles):
    for s in smiles:
        mol(s)
