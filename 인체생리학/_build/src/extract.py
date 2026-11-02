import re, sys, os, importlib, json
sys.path.insert(0, '.')
import lib
lib.load_bank()
for m in ['front','c1','c2','c3','c4','c5','c6','c7','back']:
    importlib.import_module(m).build()
TOK = re.compile(r'(<svg.*?</svg>|<img[^>]*>|<[^>]+>)', re.S)
EN = re.compile(r"[A-Za-z][A-Za-z0-9'’\-]*(?:[ \-/][A-Za-z][A-Za-z0-9'’\-]*)*")
cnt = {}
for p in lib.PAGES:
    if 'class="pb qp"' in p['html']: continue
    txt = ''.join(t for t in TOK.split(p['html']) if not t.startswith('<'))
    for m in EN.finditer(txt):
        w = m.group(0).strip()
        if len(w) < 3 or w.isupper() and len(w) <= 6: continue
        after = txt[m.end():m.end()+3]; before = txt[max(0,m.start()-2):m.start()]
        if re.match(r'\s*[(가-힣]', after) or '(' in before: continue
        cnt[w] = cnt.get(w, 0) + 1
json.dump(sorted(cnt), open('en_terms.json','w'), ensure_ascii=False)
print(len(cnt))
print(' | '.join(sorted(cnt)))
