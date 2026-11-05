// 사용: node render.js out.pdf  (같은 폴더의 index.html → A4 PDF)
const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const path = require('path');
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('file://' + path.join(__dirname, 'index.html'));
  await page.evaluate(() => document.fonts.ready);
  await page.pdf({ path: process.argv[2], format: 'A4', printBackground: true, preferCSSPageSize: true,
    displayHeaderFooter: true, headerTemplate: '<span></span>',
    footerTemplate: '<div style="width:100%;font-size:8px;color:#888;text-align:center;font-family:sans-serif">약품유기화학2 · 22장 강의 녹취록 · <span class="pageNumber"></span> / <span class="totalPages"></span></div>' });
  await browser.close();
})();
