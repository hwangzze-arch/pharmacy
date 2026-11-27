const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('file://' + path.join(__dirname, 'note.html'));
  await page.evaluate(() => document.fonts.ready);
  await page.pdf({ path: process.argv[2], format: 'A4', printBackground: true, preferCSSPageSize: true });
  await browser.close();
})();
