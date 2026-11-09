// node render.js <html> <pdf> — A4 세로, 쪽 번호 꼬리말
const { chromium } = require('/opt/node-tools/node_modules/playwright');
(async () => {
  const [html, pdf] = process.argv.slice(2);
  const b = await chromium.launch(); const p = await b.newPage();
  await p.goto('file://' + require('path').resolve(html));
  await p.evaluate(() => document.fonts.ready);
  await p.pdf({ path: pdf, format: 'A4', printBackground: true, displayHeaderFooter: true, headerTemplate: '<span></span>',
    footerTemplate: '<div style="font-size:8px;width:100%;text-align:center;color:#666"><span class="pageNumber"></span> / <span class="totalPages"></span></div>',
    margin: { top: '16mm', bottom: '16mm', left: '15mm', right: '15mm' } });
  await b.close();
})();
