
const { chromium } = require('playwright');
const fs = require('fs');
(async () => {
  const [,, html, pdf, js] = process.argv;
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1123, height: 794 } });
  await p.goto('file://' + html); await p.evaluate(() => document.fonts.ready); await p.emulateMedia({ media: 'print' });
  const over = await p.evaluate(fs.readFileSync(js, 'utf8'));
  console.log('pages', await p.evaluate(() => document.querySelectorAll('.page').length), 'overflow', JSON.stringify(over));
  await p.pdf({ path: pdf, width: '297mm', height: '210mm', printBackground: true, preferCSSPageSize: true });
  await b.close();
})();
