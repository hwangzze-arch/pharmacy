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


# 작은 전하 작용기는 글자로 (전하 기호가 결합선에 겹쳐 안 보이는 문제): NO₂ · N₃ · N₂⁺
from rdkit.Chem import rdAbbreviations
_ABBR = rdAbbreviations.ParseAbbreviations("NO2\t*[N+](=O)[O-]\tO2N\nN3\t*N=[N+]=[N-]\tN3\nN2p\t*[N+]#N\tN2p")
_LAB = {"NO2": ("NO<sub>2</sub>", "O<sub>2</sub>N"), "N3": ("N<sub>3</sub>", "N<sub>3</sub>"), "N2p": ("N<sub>2</sub><sup>+</sup>", "<sup>+</sup>N<sub>2</sub>")}


def _abbr(m):
    m2 = rdAbbreviations.CondenseMolAbbreviations(m, _ABBR, maxCoverage=0.95)
    for a in m2.GetAtoms():
        if a.HasProp("atomLabel") and a.GetProp("atomLabel") in _LAB:
            e, w = _LAB[a.GetProp("atomLabel")]
            a.SetProp("_displayLabel", e); a.SetProp("_displayLabelW", w)
    return m2


def _stretch(m, f=0.6):
    """글자 원자끼리 붙은 결합(N=N 등)은 글자가 선을 먹어 짧아 보임 → 한쪽 조각을 밀어 결합을 늘림."""
    from rdkit.Geometry import Point3D
    c = m.GetConformer()
    for b in m.GetBonds():
        a1, a2 = b.GetBeginAtom(), b.GetEndAtom()
        if b.IsInRing() or a1.GetAtomicNum() == 6 or a2.GetAtomicNum() == 6 or 0 in (a1.GetAtomicNum(), a2.GetAtomicNum()):
            continue
        if a1.HasProp("atomLabel") or a2.HasProp("atomLabel"):
            continue
        em = Chem.RWMol(m); em.RemoveBond(a1.GetIdx(), a2.GetIdx())
        frags = Chem.GetMolFrags(em, asMols=False)
        side = next(fr for fr in frags if a2.GetIdx() in fr)
        if a1.GetIdx() in side:
            continue
        p1, p2 = c.GetAtomPosition(a1.GetIdx()), c.GetAtomPosition(a2.GetIdx())
        dx, dy = (p2.x - p1.x) * f, (p2.y - p1.y) * f
        for i in side:
            p = c.GetAtomPosition(i); c.SetAtomPosition(i, Point3D(p.x + dx, p.y + dy, 0))


def svg(smiles, w=150, h=95, scale=22):
    m, hl = mol(smiles)
    if not hl:
        m = _abbr(m)
    for a in m.GetAtoms():  # 빈 자리(*) = 치환기 R
        if a.GetAtomicNum() == 0 and not a.HasProp("atomLabel"):
            a.SetProp("_displayLabel", "R"); a.SetProp("_displayLabelW", "R")
    AllChem.Compute2DCoords(m)
    _stretch(m)
    d = rdMolDraw2D.MolDraw2DSVG(w, h)
    o = d.drawOptions()
    o.clearBackground = False
    o.bondLineWidth = 1.0
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
