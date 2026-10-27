# 물리약학 「문제 풀이」·「모의고사」 디자인을 따르는 공용 레이아웃 (A4 가로, JS 자동 페이지 나눔)
import html as H, re

TOPIC = {  # 단원 → (이름, 색)
    "basic": ("분광학 기초", "#0b7f86"),
    "uv": ("자외가시부", "#2f6fc0"),
    "fl": ("형광", "#7048b8"),
    "or": ("선광도", "#b83d78"),
    "at": ("원자분광", "#c4571b"),
    "nmr": ("NMR", "#4a52c4"),
}
FLOW = {  # 라벨 → (아이콘, 칩 배경, 칩 글자색)
    "단서": ("👀", "#e3efff", "#2a5ea8"),
    "질문": ("🤔", "#fff1c9", "#8a6400"),
    "연결": ("💡", "#fff1c9", "#8a6400"),
    "계산": ("🧮", "#eee6ff", "#6a3db8"),
    "함정 체크": ("🔍", "#ffe1e4", "#c0263d"),
    "결론": ("✅", "#dcf3e2", "#1d7a3c"),
    "보기": ("🔎", "#ffe1e4", "#c0263d"),
}
CIRC = "①②③④⑤"

CSS = r"""
@page{size:297mm 210mm;margin:0}
*{box-sizing:border-box}
html,body{margin:0;padding:0;background:#fff}
body{font-family:'Noto Sans KR',sans-serif;color:#23262e;-webkit-print-color-adjust:exact;print-color-adjust:exact}
#stage{position:absolute;left:-9999px;top:0;width:297mm}
.page{width:297mm;height:210mm;padding:9mm 11mm 12mm 11mm;position:relative;overflow:hidden;page-break-after:always;display:flex;flex-direction:column;font-size:var(--fs,12px);line-height:1.55}
.hd{display:flex;align-items:center;gap:10px;border-bottom:1.5px solid #3b3f4a;padding-bottom:6px;flex:none}
.hd .bd{background:#127a76;color:#fff;font-weight:700;font-size:12px;border-radius:7px;padding:3px 10px}
.hd .bd.ans{background:#1f6fb8}
.hd .tt{flex:1;font-weight:700;font-size:15px;color:#164e63}
.hd .mt{font-size:11px;color:#5b6070}
.ft{position:absolute;left:11mm;right:11mm;bottom:5mm;display:flex;justify-content:space-between;font-size:9.5px;color:#8a8f99}
.body{flex:1;min-height:0;display:flex;flex-direction:column;gap:9px;margin-top:9px}
/* --- problem rows --- */
.row{display:grid;grid-template-columns:1fr 1.07fr;gap:12px;flex:1 1 auto;min-height:0}
.lc{display:flex;flex-direction:column;gap:7px;min-height:0}
.pc{border:1px solid #c9ccd4;border-radius:10px;padding:8px 12px;background:#fff;flex:none}
.pc .ph{display:flex;align-items:center;gap:6px;margin-bottom:4px;flex-wrap:wrap}
.num{display:inline-block;background:#127a76;color:#fff;font-weight:700;font-size:.92em;border-radius:6px;padding:1px 9px}
.chip{display:inline-block;border:1.4px solid;border-radius:11px;font-size:.78em;font-weight:700;padding:0 8px;line-height:1.55}
.pc .pt{font-weight:700}
.opts{display:grid;grid-template-columns:1fr 1fr;gap:1px 18px;margin-top:4px}
.opts.long{grid-template-columns:1fr}
.blank{display:inline-block;min-width:3.6em;border-bottom:1.5px solid #6a3db8;text-align:center;color:#6a3db8;font-weight:700;margin:0 2px}
.work{flex:1;min-height:52px;border:1.6px dashed #c8cbd2;border-radius:10px;background-image:radial-gradient(#d3d6dd 1px,transparent 1px);background-size:13px 13px;position:relative}
.work span{position:absolute;top:6px;left:9px;background:#fff;border:1px solid #d6d9e0;border-radius:7px;font-size:.8em;font-weight:700;padding:0 7px;color:#4b505c}
.ac{border:1px solid #cfe2d6;border-radius:10px;background:#f2f8f4;padding:8px 12px;display:flex;flex-direction:column;min-height:0}
.ah{display:flex;align-items:baseline;gap:7px}
.ah .bd{background:#1d7a3c;color:#fff;font-size:.78em;font-weight:700;border-radius:6px;padding:1px 8px;flex:none}
.ah .a{font-weight:700;color:#14653a;font-size:1.06em}
.fh{font-weight:700;color:#164e63;margin:4px 0 2px 0}
.fl{display:flex;gap:6px;align-items:baseline;margin:1px 0}
.fl .ic{flex:none;width:1.25em}
.fl .lb{flex:none;border-radius:5px;font-size:.76em;font-weight:700;padding:0 6px}
.fl .tx{flex:1;min-width:0}
.fl .tx .w{display:block;color:#6b7080;font-size:.9em}
.one{margin-top:auto;background:#1d7a3c;color:#fff;border-radius:9px;padding:5px 12px;font-weight:700}
.one .lb{background:rgba(255,255,255,.2);border-radius:5px;font-size:.82em;padding:0 7px;margin-right:6px}
.ac .sp{flex:1;min-height:4px}
/* --- question sheet --- */
.qs{flex:1;min-height:0;display:grid;grid-template-columns:1fr 1fr;gap:0 0}
.qs .col{min-height:0;overflow:hidden;padding:0 12px;display:flex;flex-direction:column}
.qs .col+.col{border-left:1px solid #d5d8de}
.sec{background:#e9f1fb;border-left:4px solid #1f6fb8;border-radius:6px;padding:5px 12px;margin:0 0 8px 0;color:#164e8a;font-weight:700;font-size:1.08em}
.sec span{font-weight:400;font-size:.8em;color:#556;margin-left:8px}
.qi{padding:6px 0 12px 0;border-bottom:1px dashed #d2d5dc;margin-bottom:6px;break-inside:avoid}
.qi .ph{display:flex;gap:7px;align-items:center;margin-bottom:3px}
.oxe{padding:3px 0 7px 0;margin-bottom:4px}
.ox{display:flex;gap:9px;align-items:center;padding:9px 0;border-bottom:1px dashed #d2d5dc}
.ox .tx{flex:1}
.ox .pill{flex:none;border:1.3px solid #9aa0ab;border-radius:11px;font-size:.8em;font-weight:700;padding:0 9px;color:#555}
.saw{height:var(--h,90px);border:1px dashed #c8cbd2;border-radius:6px;margin-top:5px;background-image:linear-gradient(#ececec 1px,transparent 1px);background-size:100% 20px}
/* --- answer sheet --- */
.agrid{display:grid;grid-template-columns:repeat(7,1fr);gap:6px;margin:4px 0 8px 0}
.agrid.ox{grid-template-columns:repeat(5,1fr)}
.acard{border:1px solid #cdd1d8;border-left:4px solid;border-radius:8px;padding:4px 9px;min-height:44px}
.acard b{font-size:1.05em}.acard .k{color:#c0263d;font-weight:700;margin-left:4px}
.acard div{font-size:.8em;color:#4d5260;line-height:1.35}
.bar{border-radius:9px;color:#fff;padding:7px 13px;font-weight:700;margin-top:6px}
.bar .lb{background:rgba(255,255,255,.22);border-radius:5px;padding:0 7px;margin-right:6px;font-size:.85em}
/* --- one-page summary --- */
.sum{display:grid;grid-template-columns:repeat(3,1fr);grid-auto-rows:1fr;gap:6px;flex:1;min-height:0}
.sc{border:1px solid #d3d6dd;border-top:4px solid;border-radius:8px;padding:5px 9px;font-size:.92em;line-height:1.5}
.sc b{display:block;color:#20242c}
.sc .f{font-weight:700;color:#3d2a73}
.legend{display:flex;gap:14px;font-size:.85em;font-weight:700;margin:6px 0 2px 0}
.legend span::before{content:'■ ';}
"""

def topic_chip(t):
    n, c = TOPIC[t]
    return f'<span class="chip" style="color:{c};border-color:{c}">{n}</span>'

def opts_html(opts):
    if not opts: return ""
    long = any(len(H.unescape(o)) > 22 for o in opts)
    return f'<div class="opts{" long" if long else ""}">' + "".join(f"<div>{o if re.match(r'^[ㄱ-ㅎ]\.', o) else CIRC[i] + ' ' + o}</div>" for i, o in enumerate(opts)) + "</div>"

def flow_html(flow):
    out = []
    for lab, tx, *w in flow:
        ic, bg, fg = FLOW[lab]
        why = f'<span class="w">{w[0]}</span>' if w and w[0] else ""
        out.append(f'<div class="fl"><span class="ic">{ic}</span><span class="lb" style="background:{bg};color:{fg}">{lab}</span><span class="tx">{tx}{why}</span></div>')
    return "".join(out)

def prob_row(p, numlab, srcchip):
    """p: dict(num, t(topic), title, q, opts, a, flow, one)"""
    c = TOPIC[p["t"]][1]
    return f'''<div class="row" data-part="{H.escape(p.get("part",""))}" data-num="{p["num"]}">
<div class="lc"><div class="pc"><div class="ph"><span class="num" style="background:{c}">{numlab} {p["num"]:02d}</span>{srcchip}<span class="pt">{p["title"]}</span></div>{p["q"]}{opts_html(p.get("opts"))}</div>
<div class="work"><span>✏️ 내 풀이</span></div></div>
<div class="ac"><div class="ah"><span class="bd">정답</span><span class="a">{p["a"]}</span></div><div class="fh">🧭 사고의 흐름</div>{flow_html(p["flow"])}<div class="sp"></div>
<div class="one"><span class="lb">🧠 한 줄</span>{p["one"]}</div></div></div>'''

PAGINATE_JS = r"""
() => {
 const stage = document.getElementById('stage');
 const out = document.getElementById('out');
 const mk = (kind, title, meta) => {
   const p = document.createElement('section'); p.className = 'page';
   p.innerHTML = `<div class="hd"><span class="bd ${kind==='정답'?'ans':''}">${kind}</span><div class="tt">${title}</div><div class="mt">${meta||''}</div></div><div class="body"></div><div class="ft"><span>${window.DOCNAME}</span><span class="pn"></span></div>`;
   out.appendChild(p); return p;
 };
 const fits = (p) => { const b = p.querySelector('.body'); return b.scrollHeight <= b.clientHeight + 1 && [...p.querySelectorAll('.qs .col')].every(c => c.scrollHeight <= c.clientHeight + 1); };
 for (const grp of stage.children) {
   const kind = grp.dataset.kind, title = grp.dataset.title || '', meta = grp.dataset.meta || '';
   if (grp.dataset.mode === 'raw') { const p = mk(kind, title, meta); p.querySelector('.body').innerHTML = grp.innerHTML; continue; }
   if (grp.dataset.mode === 'rows') {
     const per = +(grp.dataset.per || 3);
     let p = null, n = 0;
     const items = [...grp.children];
     for (const it of items) {
       if (!p || n >= per) { p = mk(kind, title, meta); n = 0; }
       const b = p.querySelector('.body'); b.appendChild(it); n++;
       if (!fits(p) && n > 1) { b.removeChild(it); p = mk(kind, title, meta); p.querySelector('.body').appendChild(it); n = 1; }
       if (!fits(p)) { let fs = 12; while (!fits(p) && fs > 9.2) { fs -= .2; p.style.setProperty('--fs', fs + 'px'); } }
     }
     continue;
   }
   if (grp.dataset.mode === 'cols') {
     const items = [...grp.children];
     let p = null, col = null, ci = 0;
     const newPage = () => { p = mk(kind, title, meta); const b = p.querySelector('.body'); b.innerHTML = (grp.dataset.sec && !grp._secdone ? grp.dataset.sec : '') + '<div class="qs"><div class="col"></div><div class="col"></div></div>'; grp._secdone = true; ci = 0; col = p.querySelectorAll('.qs .col')[0]; };
     newPage();
     for (const it of items) {
       col.appendChild(it);
       if (col.scrollHeight > col.clientHeight + 1 && col.children.length > 1) {
         col.removeChild(it);
         if (ci === 0) { ci = 1; col = p.querySelectorAll('.qs .col')[1]; } else newPage();
         col.appendChild(it);
       }
     }
   }
 }
 // header ranges for rows pages
 const pages = [...out.querySelectorAll('.page')];
 pages.forEach((p, i) => {
   p.querySelector('.pn').textContent = `${i + 1} / ${pages.length}`;
   const rows = [...p.querySelectorAll('.row')];
   if (rows.length) {
     const ns = rows.map(r => +r.dataset.num); const parts = [...new Set(rows.map(r => r.dataset.part).filter(x => x))];
     const pad = n => String(n).padStart(2, '0');
     if (parts.length) p.querySelector('.tt').textContent = parts.join(' / ');
     p.querySelector('.mt').textContent = (window.RANGEWORD || '문제') + ' ' + pad(Math.min(...ns)) + (ns.length > 1 ? '–' + pad(Math.max(...ns)) : '');
   }
 });
 stage.remove();
 return pages.map((p, i) => { const b = p.querySelector('.body'); return (b.scrollHeight > b.clientHeight + 1) ? i + 1 : 0; }).filter(x => x);
}
"""

def document(docname, stage_html, rangeword="문제"):
    return f'''<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>{docname}</title><style>{CSS}</style>
<script>window.DOCNAME={docname!r};window.RANGEWORD={rangeword!r};</script></head><body><div id="out"></div><div id="stage">{stage_html}</div></body></html>'''

RENDER_JS = r"""
const { chromium } = require('playwright');
const fs = require('fs');
(async () => {
  const [,, html, pdf, js] = process.argv;
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1123, height: 794 } });
  await p.goto('file://' + html); await p.evaluate(() => document.fonts.ready); await p.emulateMedia({ media: 'print' });
  const over = await p.evaluate(fs.readFileSync(js, 'utf8'));
  console.log('pages', await p.evaluate(() => document.querySelectorAll('.page').length), 'overflow', JSON.stringify(over));
  await p.pdf({ path: pdf, width: '297mm', height: '210mm', printBackground: true, preferCSSPageSize: true });
  await b.close();
})();
"""
