// node build.js → intro.pdf, overlay.pdf (투명 배경)
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const b = await chromium.launch();
  for (const name of ['intro', 'overlay']) {
    const p = await b.newPage({ viewport: { width: 1123, height: 794 } });
    await p.goto('file://' + path.join(__dirname, name + '.html'));
    await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(500);
    if (name === 'intro') {
      const issues = await p.evaluate(() => { const out = [];
        document.querySelectorAll('.page').forEach((pg, i) => { const bot = pg.querySelector('footer').getBoundingClientRect().top - 2;
          pg.querySelectorAll('.bottom *').forEach(el => { const r = el.getBoundingClientRect(); if (r.height > 0 && r.bottom > bot) out.push(`p${i + 1}: ${el.tagName}.${el.className} over ${(r.bottom - bot).toFixed(0)}px`); }); });
        return out.slice(0, 20); });
      console.log(issues.join('\n') || 'no overflow');
    }
    await p.pdf({ path: path.join(__dirname, name + '.pdf'), preferCSSPageSize: true, printBackground: true, omitBackground: name === 'overlay' });
    await p.close();
  }
  await b.close();
})();
