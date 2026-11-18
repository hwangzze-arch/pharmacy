// node build.js → final.pdf (+ 넘침 검사)
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1123, height: 703 } });
  await p.goto('file://' + path.join(__dirname, 'final.html'));
  await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(800);
  const issues = await p.evaluate(() => { const out = [];
    document.querySelectorAll('.page').forEach((pg, i) => { const pr = pg.getBoundingClientRect(); const bot = pr.bottom - 10;
      pg.querySelectorAll('.body *').forEach(el => { const r = el.getBoundingClientRect(); if (r.height > 0 && r.bottom > bot + 1) out.push(`p${i + 1}: ${el.className || el.tagName} over ${(r.bottom - bot).toFixed(0)}px`); });
      pg.querySelectorAll('.q').forEach(q => { if (q.scrollHeight > q.clientHeight + 1) out.push(`p${i + 1}: q clipped ${q.scrollHeight - q.clientHeight}`); }); });
    return out.slice(0, 60); });
  console.log(issues.join('\n') || 'no overflow');
  await p.pdf({ path: path.join(__dirname, 'final.pdf'), width: '297mm', height: '186mm', printBackground: true, preferCSSPageSize: true });
  await b.close();
})();
