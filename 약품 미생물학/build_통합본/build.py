# -*- coding: utf-8 -*-
import os, sys, importlib
sys.path.insert(0, os.path.dirname(__file__))
import core
from core import PAGES, TOC

MODULES = ["c00_intro", "c10_gp", "c20_v_basic", "c30_v_dna", "c40_v_rna", "c50_v_rt"]
only = sys.argv[1:] or MODULES
for m in MODULES:
    if m in only and os.path.exists(os.path.join(os.path.dirname(__file__), m + ".py")):
        importlib.import_module(m)

css = open(os.path.join(os.path.dirname(__file__), "style.css"), encoding="utf-8").read()
out = []
for i, (kind, html) in enumerate(PAGES):
    html = html.replace('<section class="page', f'<section data-pn="{i+1}" class="page', 1)
    out.append(html)
body = "\n".join(out)
# TOC 치환
toc_html = ""
last = None
for grp, title, idx in TOC:
    if grp != last:
        cls = "gpc" if grp.startswith("PART 1") else ("vrc" if grp.startswith("PART 2") else "")
        toc_html += f'<div class="grp {cls}">{grp}</div>'
        last = grp
    toc_html += f'<div class="it"><span>{title}</span><span>{idx+1}</span></div>'
body = body.replace("<!--TOC-->", toc_html)
doc = f'''<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>약품미생물학 통합본</title>
<style>{css}</style></head><body>{body}</body></html>'''
open(os.path.join(os.path.dirname(__file__), "out.html"), "w", encoding="utf-8").write(doc)
print("pages:", len(PAGES), "questions:", core.COUNTER["q"])
