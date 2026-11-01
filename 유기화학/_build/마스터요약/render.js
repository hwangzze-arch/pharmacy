const { chromium } = require('/opt/node22/lib/node_modules/playwright');
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
      const bad = [...pg.querySelectorAll('.main,.side,.acol')].some(c => c.scrollHeight > c.clientHeight + 1) || (pg.querySelector('.ft') && [...pg.querySelectorAll('.one,.mband,.nr,.nr .card')].some(x => x.getBoundingClientRect().bottom > pg.querySelector('.ft').getBoundingClientRect().top + 1));
      const work = pg.querySelector('.work');
      const wsmall = work && !work.classList.contains('sm') ? (work.classList.contains('hasnote') ? work.scrollHeight > work.clientHeight + 1 : work.clientHeight < 90) : false;
      const ft = pg.querySelector('.ft');
      const vbad = [...pg.querySelectorAll('.abx')].some(x => x.scrollHeight > x.clientHeight + 1) || ft && [...pg.querySelectorAll('.abx,.pbx')].some(x => x.getBoundingClientRect().bottom > ft.getBoundingClientRect().top - 2);
      const msmall = [...pg.querySelectorAll('.memo')].some(m => m.clientHeight < 55);
      return bad || wsmall || vbad || msmall;
    };
    // 메커니즘·구조식 그림(.mz): 들어갈 칸 너비에 맞춰 축소 (최대 1배)
    const fitw = (z) => { z.style.zoom = 1; const w = z.parentElement.clientWidth - 4; const r = w / z.scrollWidth; z.style.zoom = Math.min(1, r); return Math.min(1, r); };
    document.querySelectorAll('.mz').forEach(fitw);
    // 전체 메커니즘 쪽: 칸 높이·너비에 맞게 최대한 크게
    document.querySelectorAll('.mfull .mband.big .mz').forEach(z => { const p = z.parentElement; z.style.zoom = 1;
      const r = Math.min((p.clientWidth - 20) / z.scrollWidth, (p.clientHeight - 44) / z.scrollHeight); z.style.zoom = Math.min(1.6, r); });
    document.querySelectorAll('.page').forEach((pg, i) => {
      if (pg.classList.contains('cover') || pg.classList.contains('cover2')) return;
      let fs = 12.8, imgh = 320, guard = 0;
      const bands = [...pg.querySelectorAll('.mband .mz, .afig .mz')];
      pg.style.setProperty('--fs', fs + 'px'); pg.style.setProperty('--imgh', imgh + 'px');
      while (over(pg) && guard++ < 120) {
        if (fs > 11.6) fs -= 0.2;
        else if (imgh > 150) imgh -= 15;
        else if ([...pg.querySelectorAll('.fcol .fz')].some(z => (parseFloat(z.style.zoom) || 1) > 0.45)) pg.querySelectorAll('.fcol .fz').forEach(z => z.style.zoom = Math.max(0.45, (parseFloat(z.style.zoom) || 1) - 0.05));
        else if (pg.querySelector('.pbx img') && (parseFloat(pg.style.getPropertyValue('--pimgh')) || 230) > 90) pg.style.setProperty('--pimgh', ((parseFloat(pg.style.getPropertyValue('--pimgh')) || 230) - 10) + 'px');
        else if (pg.querySelector('.acol .tbimg, .abx .tbimg') && (parseFloat(pg.style.getPropertyValue('--aimg')) || 1) > 0.5) pg.style.setProperty('--aimg', ((parseFloat(pg.style.getPropertyValue('--aimg')) || 1) - 0.05).toFixed(2));
        else if (bands.length && bands.some(z => parseFloat(z.style.zoom) > 0.55)) bands.forEach(z => z.style.zoom = Math.max(0.55, parseFloat(z.style.zoom) - 0.05));
        else if (fs > 9.4) fs -= 0.2;
        else break;
        pg.style.setProperty('--fs', fs + 'px');
        pg.style.setProperty('--imgh', imgh + 'px');
      }
      if (over(pg) && pg.classList.contains('v21') && !pg.classList.contains('pair2') && !pg.classList.contains('side')) {
        pg.classList.add('side'); fs = 12.8; imgh = 320; guard = 0;
        pg.style.removeProperty('--aimg'); pg.style.removeProperty('--pimgh');
        pg.querySelectorAll('.mz').forEach(fitw); bands.forEach(z => fitw(z));
        pg.style.setProperty('--fs', fs + 'px'); pg.style.setProperty('--imgh', imgh + 'px');
        while (over(pg) && guard++ < 120) {
          if (fs > 11.6) fs -= 0.2;
          else if (pg.querySelector('.abx .tbimg') && (parseFloat(pg.style.getPropertyValue('--aimg')) || 1) > 0.5) pg.style.setProperty('--aimg', ((parseFloat(pg.style.getPropertyValue('--aimg')) || 1) - 0.05).toFixed(2));
          else if (bands.length && bands.some(z => parseFloat(z.style.zoom) > 0.55)) bands.forEach(z => z.style.zoom = Math.max(0.55, parseFloat(z.style.zoom) - 0.05));
          else if (fs > 9.4) fs -= 0.2;
          else break;
          pg.style.setProperty('--fs', fs + 'px');
        }
      }
      res.push({ side: pg.classList.contains('side'), i: i + 1, fs: Math.round(fs * 10) / 10, imgh, overflow: over(pg) });
    });
    return res;
  });
  if (process.env.AUDIT) {
    const au = await page.evaluate(() => [...document.querySelectorAll('.page')].map((pg, i) => ({
      i: i + 1,
      img: [...pg.querySelectorAll('img')].map(m => [m.getAttribute('src').split('/').pop(), Math.round(m.getBoundingClientRect().width), m.naturalWidth, +(m.getBoundingClientRect().width / m.naturalWidth).toFixed(2), Math.round(m.getBoundingClientRect().height)]),
      mz: [...pg.querySelectorAll('.mz')].map(z => [+(parseFloat(z.style.zoom) || 1).toFixed(2), z.closest('.afig') ? 'afig' : z.closest('.mband') ? 'band' : z.closest('.fig') ? 'fig' : 'other']),
      fs: pg.style.getPropertyValue('--fs') })));
    require('fs').writeFileSync('/tmp/audit.json', JSON.stringify(au));
    const need = await page.evaluate(() => [...document.querySelectorAll('.page')].map((pg, i) => {
      const small = [];
      pg.querySelectorAll('img').forEach(m => {
        const n = m.getAttribute('src').split('/').pop(), w = m.getBoundingClientRect().width, sc = w / m.naturalWidth;
        if (/^(tp|ta|ss|we)/.test(n) ? sc < 0.4 : /^s-\d/.test(n) ? w < 380 : (m.naturalWidth >= 2000 && w < 520)) small.push(n + ':' + sc.toFixed(2));
      });
      pg.querySelectorAll('.mz').forEach(z => { const r = parseFloat(z.style.zoom) || 1; if (r < 0.78 && z.closest('.mband,.afig,.fig') && !pg.classList.contains('mfull')) small.push('mz:' + r.toFixed(2)); });
      const fs = parseFloat(pg.style.getPropertyValue('--fs')) || 12.8;
      if (fs < 10.4 && !pg.classList.contains('mfull')) small.push('fs:' + fs.toFixed(1));
      const ftp = pg.querySelector('.ft'); const nrb = pg.querySelector('.nr');
      if (ftp && nrb && (nrb.getBoundingClientRect().bottom > ftp.getBoundingClientRect().top + 1 || [...nrb.querySelectorAll('.card')].some(c => c.scrollHeight > c.clientHeight + 1 || c.getBoundingClientRect().bottom > ftp.getBoundingClientRect().top + 1))) small.push('overflow');
      if (!small.length) return null;
      const t = pg.classList.contains('pair2') ? 'unpair' : pg.classList.contains('aonly') ? 'none' : pg.classList.contains('cnext') ? 'csplit2' : pg.classList.contains('v21') ? 'qsplit' : pg.dataset.k ? 'csplit' : 'none';
      return { i: i + 1, t, k: pg.dataset.k, k2: pg.dataset.k2, small };
    }).filter(Boolean));
    require('fs').writeFileSync('/tmp/need.json', JSON.stringify(need));
  }
  report.filter(r => r.fs < 11 || r.overflow).forEach(r => console.log(JSON.stringify(r)));
  await page.pdf({ path: process.argv[2], width: '297mm', height: '210mm', printBackground: true, preferCSSPageSize: true });
  if (process.argv[3]) {
    const els = await page.$$('.page');
    for (const n of process.argv[3].split(',')) {
      await els[parseInt(n) - 1].screenshot({ path: path.join(dir, `shot-${n}.png`) });
    }
  }
  await browser.close();
})();
