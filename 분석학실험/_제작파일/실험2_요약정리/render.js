const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const dir = __dirname;
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1123, height: 794 } });
  await page.goto('file://' + path.join(dir, 'index.html'));
  await page.evaluate(() => document.fonts.ready);
  await page.emulateMedia({ media: 'print' });
  const report = await page.evaluate(() => {
    const res = [];
    const sel = '.main,.side,.acol,.qcard,.page';
    const over = (pg) => {
      const bad = [...pg.querySelectorAll('.main,.side,.acol')].some(c => c.scrollHeight > c.clientHeight + 1);
      const work = pg.querySelector('.work');
      const wsmall = work ? (work.classList.contains('hasnote') ? work.scrollHeight > work.clientHeight + 1 : work.clientHeight < 90) : false;
      return bad || wsmall;
    };
    document.querySelectorAll('.page').forEach((pg, i) => {
      if (pg.classList.contains('cover') || pg.classList.contains('cover2')) return;
      let fs = 18, imgh = 240, guard = 0;
      pg.style.setProperty('--fs', fs + 'px');
      while (over(pg) && guard++ < 80) {
        if (fs > 11.6) fs -= 0.2;
        else if (imgh > 150) imgh -= 15;
        else if (fs > 9.4) fs -= 0.2;
        else break;
        pg.style.setProperty('--fs', fs + 'px');
        pg.style.setProperty('--imgh', imgh + 'px');
      }
      res.push({ i: i + 1, fs: Math.round(fs * 10) / 10, imgh, overflow: over(pg) });
    });
    return res;
  });
  report.filter(r => process.env.FITLOG || r.fs < 11 || r.overflow).forEach(r => console.log(JSON.stringify(r)));
  await page.pdf({ path: process.argv[2], width: '297mm', height: '210mm', printBackground: true, preferCSSPageSize: true });
  if (process.argv[3]) {
    const els = await page.$$('.page');
    for (const n of process.argv[3].split(',')) {
      await els[parseInt(n) - 1].screenshot({ path: path.join(dir, `shot-${n}.png`) });
    }
  }
  await browser.close();
})();
