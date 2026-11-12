// HTML 한 장 → PDF 한 장.  node render.js in.html out.pdf <폭pt> <높이pt>
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const [inp, out, w, h] = process.argv.slice(2);
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: Math.round(+w * 4 / 3), height: Math.round(+h * 4 / 3) } });
  await page.goto('file://' + path.resolve(inp), { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);
  const missing = await page.evaluate(() => ['Noto Sans KR', 'Inter Tight'].filter(f => !document.fonts.check(`800 20px "${f}"`)));
  if (missing.length) { console.error('글꼴을 못 불러옴:', missing.join(', ')); process.exit(1); }
  await page.pdf({ path: out, width: `${(+w / 72).toFixed(4)}in`, height: `${(+h / 72).toFixed(4)}in`, printBackground: true, pageRanges: '1' });
  await browser.close();
})();
