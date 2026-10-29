const { chromium } = require('/opt/node22/lib/node_modules/playwright');
(async () => {
  const path = require('path');
  const dir = __dirname;
  const out = process.argv[2] || path.join(dir, 'out.pdf');
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1200, height: 800 } });
  await page.goto('file://' + path.join(dir, 'out.html'));
  await page.evaluate(() => document.fonts.ready);
  const report = await page.evaluate(() => {
    const res = [];
    document.querySelectorAll('.page').forEach((p) => {
      let s = p.classList.contains('spage') ? 1.3 : (p.classList.contains('qpage') ? 1.06 : 1.0);
      p.style.setProperty('--s', s);
      const over = () => p.scrollHeight > p.clientHeight + 1 || [...p.querySelectorAll('.qrow .card, .card2, .ans')].some(e => e.scrollWidth > e.clientWidth + 2);
      while (over() && s > 0.66) { s -= 0.02; p.style.setProperty('--s', s.toFixed(2)); }
      const blank = p.querySelector('.blank');
      res.push({ pn: p.dataset.pn, s: +s.toFixed(2), over: over(), blank: blank ? Math.round(blank.getBoundingClientRect().height / 3.78) : null });
    });
    return res;
  });
  const bad = report.filter(r => r.s < 0.84 || r.over || (r.blank !== null && r.blank < 24));
  console.log('pages', report.length, 'flagged', bad.length);
  bad.forEach(r => console.log(JSON.stringify(r)));
  await page.pdf({ path: out, width: '297mm', height: '186mm', printBackground: true, preferCSSPageSize: true });
  await browser.close();
})();
