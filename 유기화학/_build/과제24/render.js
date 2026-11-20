const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const path = require('path');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1123, height: 794 } });
  await p.goto('file://' + path.join(__dirname, 'index.html')); await p.evaluate(() => document.fonts.ready);
  const r = await p.evaluate(() => [...document.querySelectorAll('.page')].map((pg, i) => {
    let z = 1.6; pg.querySelectorAll('.ans .rx,.mz .mrow').forEach(x => x.style.zoom = z); const f = () => pg.scrollHeight > pg.clientHeight + 1 || [...pg.querySelectorAll('.rx,.mrow')].some(x => x.scrollWidth > x.clientWidth + 1);
    while (f() && z > 0.6) { z -= 0.05; pg.querySelectorAll('.ans .rx,.mz .mrow').forEach(x => x.style.zoom = z); }
    return { i: i + 1, z: +z.toFixed(2), over: f() }; }));
  console.log(JSON.stringify(r));
  await p.pdf({ path: process.argv[2], width: '297mm', height: '210mm', printBackground: true }); await b.close();
})();
