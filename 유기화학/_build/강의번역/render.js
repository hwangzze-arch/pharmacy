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
    // 슬라이드+메커니즘 쪽: 글자 크기를 조금씩 줄여 가며 메커니즘 그림을 가장 크게 (zoom)
    const wide = (f) => [...f.querySelectorAll('.mrow')].some(r => r.scrollWidth > r.clientWidth + 1);
    const low = (pg) => { const f = pg.querySelector('.msrow'), ft = pg.querySelector('footer');
      return f.getBoundingClientRect().bottom > ft.getBoundingClientRect().top - 4; };
    const fits = (pg, f) => !over(pg) && !wide(f) && !low(pg);
    document.querySelectorAll('.page.ms').forEach(pg => {
      const f = pg.querySelector('.mfig');
      let best = null;
      for (const fs of [12.5, 12, 11.5, 11, 10.5, 10]) {
        pg.style.setProperty('--fs', fs + 'px');
        for (let z = 1.6; z >= 0.8; z -= 0.05) {
          f.style.zoom = z;
          if (fits(pg, f)) { best = { fs, z }; break; }
        }
        if (best) break;
      }
      if (!best) { let z = 0.8; while (!fits(pg, f) && z > 0.4) { z -= 0.05; f.style.zoom = z; } best = { fs: 10, z }; }
      pg.style.setProperty('--fs', best.fs + 'px'); f.style.zoom = best.z;
      pg.dataset.fs = best.fs; pg.dataset.zoom = best.z.toFixed(2);
    });
    document.querySelectorAll('.page').forEach((pg, i) => {
      if (pg.classList.contains('ms')) { res.push({ i: i + 1, ms: true, fs: +pg.dataset.fs, zoom: +pg.dataset.zoom, overflow: over(pg) }); return; }
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
  report.filter(r => r.ms || r.fs < 12.5 || r.overflow).forEach(r => console.log(JSON.stringify(r)));
  await page.pdf({ path: out, width: '297mm', height: '210mm', printBackground: true, preferCSSPageSize: true });
  if (process.argv[3]) {
    for (const n of process.argv[3].split(',')) {
      const el = (await page.$$('.page'))[parseInt(n) - 1];
      await el.screenshot({ path: path.join(dir, `shot-${n}.png`) });
    }
  }
  await browser.close();
})();
