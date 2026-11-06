// 사용: node render.js out.pdf [index.html] [장]  (예: node render.js out.pdf index23.html 23)
const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const path = require('path');
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('file://' + path.join(__dirname, process.argv[3] || 'index.html'));
  await page.evaluate(() => document.fonts.ready);
  await page.pdf({ path: process.argv[2], format: 'A4', printBackground: true, preferCSSPageSize: true,
    displayHeaderFooter: true, headerTemplate: '<span></span>',
    footerTemplate: '<div style="width:100%;font-size:8px;color:#888;text-align:center;font-family:sans-serif">약품유기화학2 · ' + (process.argv[4] || '22') + '장 강의 녹취록 · <span class="pageNumber"></span> / <span class="totalPages"></span></div>' });
  await browser.close();
})();
