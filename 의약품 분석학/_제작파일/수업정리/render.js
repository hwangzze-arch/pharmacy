// node render.js in.html out.pdf "꼬리말"
const { chromium } = require('playwright');
(async () => {
  const [inp, out, foot] = process.argv.slice(2);
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('file://' + inp, { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);
  await page.pdf({ path: out, format: 'A4', printBackground: true, preferCSSPageSize: true,
    displayHeaderFooter: true, headerTemplate: '<span></span>',
    footerTemplate: `<div style="font-size:8px;color:#5f6b78;width:100%;padding:0 14mm;display:flex;font-family:sans-serif"><span style="flex:1">${foot || ''}</span><span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>` });
  await browser.close();
})();
