import re
from endict import D
TOKEN = re.compile(r'(<svg.*?</svg>|<img[^>]*>|</?[a-zA-Z][^>]*>)', re.S)
SKIPC = {'pn','chip','part','foot','tp','tpart','ann','ox','kw','e','k','tfl'}
TERMS = sorted(D, key=len, reverse=True)
RX = re.compile(r'(?<![A-Za-z0-9\-])(' + '|'.join(re.escape(t) for t in TERMS) + r")(?![A-Za-z0-9\-'])")
def _cls(tag):
    m = re.search(r'class="([^"]*)"', tag); return set(m.group(1).split()) if m else set()
def annotate_all(html):
    toks = [t for t in TOKEN.split(html) if t != '']
    vis = ['' if t.startswith('<') else t for t in toks]
    stack = []; out = []
    for i, tok in enumerate(toks):
        if tok.startswith('<'):
            if tok.startswith('</'):
                n = re.match(r'</\s*([a-zA-Z0-9]+)', tok).group(1).lower()
                for k in range(len(stack)-1, -1, -1):
                    if stack[k][0] == n: del stack[k:]; break
            elif not (tok.startswith('<svg') or tok.startswith('<img') or tok.endswith('/>')):
                n = re.match(r'<\s*([a-zA-Z0-9]+)', tok).group(1).lower()
                if n != 'br': stack.append((n, _cls(tok)))
            out.append(tok); continue
        if any(c & SKIPC for _, c in stack):
            out.append(tok); continue
        nxt = ''
        for t2 in toks[i+1:i+10]:
            if t2.startswith('<'):
                if re.match(r'</?(td|th|tr|div|li|p|br|ol|ul|table)\b', t2): break
                continue
            nxt += t2
            if len(nxt) >= 4: break
        prev = ''.join(out)
        tail = re.split(r'<(?:td|th|div|li|p|br|span class="ann")\b[^>]*>', prev[-300:])[-1]
        prevvis = re.sub(r'<[^>]+>', '', tail)[-2:]
        res = []; last = 0
        for m in RX.finditer(tok):
            after = (tok[m.end():] + nxt)[:4]
            before = (prevvis + tok[:m.start()])[-2:]
            if re.match(r"\s*[(가-힣\[]", after) or after.startswith("'s") or '(' in before:
                continue
            res.append(tok[last:m.end()]); res.append(f'<span class="ann">({D[m.group(1)]})</span>'); last = m.end()
        res.append(tok[last:]); out.append(''.join(res))
    return ''.join(out)
