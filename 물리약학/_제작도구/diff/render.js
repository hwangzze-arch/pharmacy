const { chromium } = require('/opt/node-tools/node_modules/playwright');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage();
  await p.goto('file://' + process.argv[2] + '/' + process.argv[3]);
  await p.evaluate(() => document.fonts.ready);
  const over = await p.evaluate(() => [...document.querySelectorAll('.page')].map((pg, i) => {
    const ft = pg.querySelector('.foot').getBoundingClientRect().top;
    let m = 0;
    pg.querySelectorAll('.two > div > *, .sol > *, .qcard, .pl > *, .brain, .cs').forEach(e => { m = Math.max(m, e.getBoundingClientRect().bottom); });
    let inner = 0;
    pg.querySelectorAll('.sol, .two').forEach(e => { inner = Math.max(inner, e.scrollHeight - e.clientHeight); });
    return [i + 1, Math.round(ft - m), inner];
  }).filter(x => x[1] < 4 || x[2] > 2));
  console.log('overflow:', JSON.stringify(over));
  await p.pdf({ path: process.argv[4], width: '297mm', height: '210mm', printBackground: true, preferCSSPageSize: true });
  await b.close();
})();
