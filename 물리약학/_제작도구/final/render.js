const { chromium } = require('/opt/node-tools/node_modules/playwright');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage();
  await p.goto('file://' + process.argv[2] + '/out.html');
  await p.evaluate(() => document.fonts.ready);
  const over = await p.evaluate(() => [...document.querySelectorAll('.page')].map((pg, i) => {
    const r = pg.getBoundingClientRect(); const ft = pg.querySelector('.foot').getBoundingClientRect().top;
    let m = 0, mr = 0;
    pg.querySelectorAll('.card,.formula,.box,table,.fig,.ans,.prow,.cs,.chs,.step,p,li,.traps').forEach(e => { const q = e.getBoundingClientRect(); m = Math.max(m, q.bottom); mr = Math.max(mr, q.right); });
    return [i + 1, Math.round(ft - m), Math.round(r.right - mr)];
  }).filter(x => x[1] < 6 || x[2] < 0));
  console.log('tight/overflow:', JSON.stringify(over));
  await p.pdf({ path: process.argv[3], width: '320mm', height: '200mm', printBackground: true, preferCSSPageSize: true });
  await b.close();
})();
