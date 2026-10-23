const { chromium } = require('/opt/node-tools/node_modules/playwright');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage();
  await p.goto('file://' + process.argv[2] + '/' + process.argv[3]); await p.waitForLoadState('networkidle');
  await p.evaluate(() => document.fonts.ready);
  await p.pdf({ path: process.argv[4], preferCSSPageSize: true, printBackground: true, displayHeaderFooter: true,
    headerTemplate: '<div></div>',
    footerTemplate: '<div style="font-size:8px;color:#9aa1ad;width:100%;padding:0 12mm;display:flex;justify-content:space-between;font-family:sans-serif"><span>물리약학 중간고사 · 한 장 정리 + 문제·풀이</span><span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>' });
  await b.close();
})();
