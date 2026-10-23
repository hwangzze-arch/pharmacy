const { chromium } = require('/opt/node-tools/node_modules/playwright');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage();
  await p.goto('file://' + process.argv[2] + '/' + process.argv[3]);
  await p.waitForLoadState('networkidle'); await p.evaluate(() => Promise.all([document.fonts.ready, ...[...document.images].map(i => i.complete ? 1 : new Promise(r => { i.onload = i.onerror = r; }))]));
  await p.waitForTimeout(300);
  const over = await p.evaluate(() => [...document.querySelectorAll('.page')].map((pg, i) => {
    const ft = pg.querySelector('.foot').getBoundingClientRect().top; let m = 0, inner = 0;
    pg.querySelectorAll('.cc, .prow, .grid2, .cs, .pbox > *').forEach(e => { m = Math.max(m, e.getBoundingClientRect().bottom); });
    pg.querySelectorAll('.sol, .qcard, .cc').forEach(e => { inner = Math.max(inner, e.scrollHeight - e.clientHeight); });
    return [i + 1, Math.round(ft - m), inner];
  }).filter(x => x[1] < 2 || x[2] > 2));
  console.log('overflow:', JSON.stringify(over));
  await p.pdf({ path: process.argv[4], width: '297mm', height: '210mm', printBackground: true, preferCSSPageSize: true });
  await b.close();
})();
