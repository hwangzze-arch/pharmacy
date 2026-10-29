const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const fs = require('fs'), path = require('path');
(async () => {
  const [inp, outPdf, outJson] = process.argv.slice(2);
  const b = await chromium.launch(); const p = await b.newPage();
  await p.goto('file://' + path.resolve(inp));
  await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(300);
  const r = await p.evaluate(() => [...document.querySelectorAll('[data-fig]')].map(e => {
    const pg = e.closest('.pg'), pr = pg.getBoundingClientRect(), q = e.getBoundingClientRect();
    return { key: e.dataset.fig, page: [...document.querySelectorAll('.pg')].indexOf(pg),
      x: (q.left - pr.left) * .75, y: (q.top - pr.top) * .75, w: q.width * .75, h: q.height * .75 };
  }));
  fs.writeFileSync(outJson, JSON.stringify(r));
  await p.pdf({ path: outPdf, width: 1134/72 + 'in', height: 708.96/72 + 'in', printBackground: true, preferCSSPageSize: true });
  await b.close();
})();
