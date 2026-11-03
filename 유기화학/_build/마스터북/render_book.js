// 표지(쪽 번호 없음) + 본문(꼬리말·쪽 번호) 따로 뽑아 합침
const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const path = require('path');
const { execFileSync } = require('child_process');
(async () => {
  const dir = __dirname, out = process.argv[2];
  const browser = await chromium.launch();
  const page = await browser.newPage();
  const tmp = path.join(dir, '_tmp'); require('fs').mkdirSync(tmp, { recursive: true });
  await page.goto('file://' + path.join(dir, 'cover.html'));
  await page.evaluate(() => document.fonts.ready);
  await page.pdf({ path: tmp + '/cover.pdf', width: '297mm', height: '210mm', printBackground: true, margin: { top: 0, bottom: 0, left: 0, right: 0 }, pageRanges: '1' });
  await page.goto('file://' + path.join(dir, 'book.html'));
  await page.evaluate(() => document.fonts.ready);
  const foot = `<div style="font-family:'WenQuanYi Zen Hei',sans-serif;font-size:7px;color:#8b95a5;width:100%;padding:0 12mm;display:flex;justify-content:space-between;">
    <span>제22장 핵심 킬러 TOP 10 · 단번에 이해하는 최종 실전 마스터북</span><span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>`;
  await page.pdf({ path: tmp + '/body.pdf', printBackground: true, preferCSSPageSize: true,
    displayHeaderFooter: true, headerTemplate: '<div></div>', footerTemplate: foot });
  await browser.close();
  execFileSync('python3', ['-c', `import pymupdf as f,sys
d=f.open(sys.argv[1]);d.insert_pdf(f.open(sys.argv[2]));d.save(sys.argv[3],garbage=3,deflate=True)`, tmp + '/cover.pdf', tmp + '/body.pdf', out]);
  console.log('saved', out);
})();
