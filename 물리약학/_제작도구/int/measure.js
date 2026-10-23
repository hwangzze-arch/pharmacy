const { chromium } = require('/opt/node-tools/node_modules/playwright');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1200, height: 900 } });
  await p.goto('file://' + process.argv[2] + '/measure.html');
  await p.waitForLoadState('networkidle'); await p.evaluate(() => Promise.all([document.fonts.ready, ...[...document.images].map(i => i.complete ? 1 : new Promise(r => { i.onload = i.onerror = r; }))]));
  await p.waitForTimeout(300);
  const r = await p.evaluate(() => { const o = {}; document.querySelectorAll('.m').forEach(e => { o[e.dataset.i + ':' + (e.dataset.w||'r')] = Math.ceil(e.firstElementChild.getBoundingClientRect().height); }); return o; });
  console.log(JSON.stringify(r));
  await b.close();
})();
