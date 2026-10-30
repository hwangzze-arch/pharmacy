// node render.js <dir> <html> <pdf> — PDF 출력 + 넘침 검사
const { chromium } = require('/opt/node-tools/node_modules/playwright');
(async () => {
  const [dir, html, pdf] = process.argv.slice(2);
  const b = await chromium.launch();
  const p = await b.newPage();
  await p.goto('file://' + dir + '/' + html);
  await p.evaluate(() => document.fonts.ready);
  const over = await p.evaluate(() => [...document.querySelectorAll('.page')].map((pg, i) => {
    const lim = pg.querySelector('footer').getBoundingClientRect().top - 2;
    const cols = [...pg.querySelectorAll('.col, .kw, .sum')];
    const worst = Math.max(...cols.map(c => Math.max(...[...c.children].map(e => e.getBoundingClientRect().bottom))));
    return worst > lim ? `${i + 1}:+${Math.round(worst - lim)}px` : null;
  }).filter(Boolean));
  console.log('overflow:', JSON.stringify(over));
  await p.pdf({ path: pdf, width: '297mm', height: '210mm', printBackground: true });
  await b.close();
})();
