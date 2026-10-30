const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const path = require('path');
(async () => {
  const dir = __dirname;
  const out = process.argv[2];
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1123, height: 794 } });
  await page.goto('file://' + path.join(dir, 'index.html'));
  await page.evaluate(() => document.fonts.ready);
  await page.emulateMedia({ media: 'print' });
  const report = await page.evaluate(() => {
    const res = [];
    const over = (pg) => [...pg.querySelectorAll('.col')].some(c => c.scrollHeight > c.clientHeight + 1);
    // 메커니즘 쪽: 그림이 가로·세로로 넘치지 않는 한 가장 크게 (zoom)
    const wide = (f) => [...f.querySelectorAll('.mrow')].some(r => r.scrollWidth > r.clientWidth + 1);
    document.querySelectorAll('.page.mech').forEach(pg => {
      const f = pg.querySelector('.mfig');
      let z = 1.8;
      f.style.zoom = z;
      while ((over(pg) || wide(f)) && z > 0.7) { z -= 0.05; f.style.zoom = z; }
      pg.dataset.zoom = z.toFixed(2);
    });
    document.querySelectorAll('.page').forEach((pg, i) => {
      let fs = 12.5;
      let toph = parseFloat(getComputedStyle(pg).getPropertyValue('--toph')) || 292;
      pg.style.setProperty('--fs', fs + 'px');
      let guard = 0;
      while (over(pg) && guard++ < 60) {
        if (fs > 11.5) fs -= 0.25;
        else if (toph > 215) toph -= 10;
        else if (fs > 9.5) fs -= 0.25;
        else break;
        pg.style.setProperty('--fs', fs + 'px');
        pg.style.setProperty('--toph', toph + 'px');
      }
      res.push({ i: i + 1, fs, toph, overflow: over(pg) });
    });
    return res;
  });
  report.filter(r => r.fs < 12.5 || r.overflow).forEach(r => console.log(JSON.stringify(r)));
  await page.pdf({ path: out, width: '297mm', height: '210mm', printBackground: true, preferCSSPageSize: true });
  if (process.argv[3]) {
    for (const n of process.argv[3].split(',')) {
      const el = (await page.$$('.page'))[parseInt(n) - 1];
      await el.screenshot({ path: path.join(dir, `shot-${n}.png`) });
    }
  }
  await browser.close();
})();
