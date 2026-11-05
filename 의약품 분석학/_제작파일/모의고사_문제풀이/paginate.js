(
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
)()