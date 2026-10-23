# -*- coding: utf-8 -*-
"""RDKit로 구조식 SVG 만들기 (흰 배경 없음, 굵기 통일)."""
from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem.Draw import rdMolDraw2D


def svg(smiles, w=150, h=90, scale=22):
    m = Chem.MolFromSmiles(smiles)
    assert m is not None, smiles
    AllChem.Compute2DCoords(m)
    d = rdMolDraw2D.MolDraw2DSVG(w, h)
    o = d.drawOptions()
    o.clearBackground = False
    o.bondLineWidth = 1.6
    o.fixedBondLength = scale
    o.padding = 0.06
    o.minFontSize = 11
    o.maxFontSize = 13
    o.additionalAtomLabelPadding = 0.08
    d.DrawMolecule(m)
    d.FinishDrawing()
    s = d.GetDrawingText()
    s = s[s.index('<svg'):]
    return s
