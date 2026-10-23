const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const fs = require('fs'), path = require('path');
(async () => {
  const [inp, outPdf, outJson, w, h] = process.argv.slice(2);
  const b = await chromium.launch();
  const p = await b.newPage();
  await p.goto('file://' + path.resolve(inp));
  await p.evaluate(() => document.fonts.ready);
  await p.waitForTimeout(300);
  const hs = await p.evaluate(() => {
    const r = [];
    document.querySelectorAll('.slot').forEach(s => {
      const m = s.querySelector('.memo');
      if (m && m.getBoundingClientRect().height < 34) m.remove();
      r.push([s.dataset.key, s.getBoundingClientRect().height * 0.75]);
    });
    return r;
  });
  if (outJson !== '-') fs.writeFileSync(outJson, JSON.stringify(hs));
  await p.pdf({ path: outPdf, width: ((+w)||1080)/72+'in', height: ((+h)||1100)/72+'in', printBackground: true, preferCSSPageSize: true });
  await b.close();
})();
