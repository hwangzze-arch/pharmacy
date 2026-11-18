// node build.js → final.pdf
// 1) 요약 페이지(.page.fit)는 본문이 페이지 높이를 꽉 채우도록 배율(zoom)을 페이지마다 자동으로 찾음
// 2) 넘침 검사 후 PDF 출력
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1123, height: 703 } });
  await p.goto('file://' + path.join(__dirname, 'final.html'));
  await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(800);
  const fit = await p.evaluate(() => {
    const res = [];
    const contentBottom = (body) => { let m = 0; body.querySelectorAll('*').forEach(el => { if (el.children.length && el.tagName !== 'TABLE' && !el.classList.contains('card') && !el.classList.contains('callout') && !el.classList.contains('lead') && !el.classList.contains('fig')) return; const r = el.getBoundingClientRect(); if (r.height > 0) m = Math.max(m, r.bottom); }); return m; };
    document.querySelectorAll('.page.fit').forEach((pg) => {
      const body = pg.querySelector('.body'); if (!body) return;
      const r0 = body.getBoundingClientRect(); const W = r0.width, H = r0.height, top = r0.top;
      const set = (k) => { body.style.zoom = k; body.style.flex = 'none'; body.style.width = (W / k) + 'px'; body.style.height = (H / k) + 'px'; };
      const ok = (k) => { set(k); return (contentBottom(body) - top) <= H * 0.975 && body.scrollWidth <= body.clientWidth + 1; };
      let lo = 1, hi = 1.7;
      if (!ok(lo)) { lo = 0.8; }
      for (let i = 0; i < 14; i++) { const m = (lo + hi) / 2; if (ok(m)) lo = m; else hi = m; }
      set(lo); res.push(lo.toFixed(2));
    });
    return res;
  });
  console.log('fit zoom:', fit.join(' '));
  const issues = await p.evaluate(() => { const out = [];
    document.querySelectorAll('.page').forEach((pg, i) => { const pr = pg.getBoundingClientRect(); const bot = pr.bottom - 10;
      pg.querySelectorAll('.body *').forEach(el => { const r = el.getBoundingClientRect(); if (r.height > 0 && r.bottom > bot + 1) out.push(`p${i + 1}: ${el.className || el.tagName} over ${(r.bottom - bot).toFixed(0)}px`); });
      pg.querySelectorAll('.q').forEach(q => { if (q.scrollHeight > q.clientHeight + 1) out.push(`p${i + 1}: q clipped ${q.scrollHeight - q.clientHeight}`); }); });
    return out.slice(0, 60); });
  console.log(issues.join('\n') || 'no overflow');
  await p.pdf({ path: path.join(__dirname, 'final.pdf'), width: '297mm', height: '186mm', printBackground: true, preferCSSPageSize: true });
  await b.close();
})();
