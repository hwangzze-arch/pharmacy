const { chromium } = require('/opt/node22/lib/node_modules/playwright');
(async () => {
  const [, , inp, out] = process.argv;
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1123, height: 703 } });
  await p.goto('file://' + inp, { waitUntil: 'networkidle' });
  await p.emulateMedia({ media: 'print' });
  const bad = await p.evaluate(() => {
    const r = [];
    document.querySelectorAll('.pg').forEach((pg, i) => {
      const pb = pg.querySelector('.pb');
      if (pb && pb.scrollHeight > pb.clientHeight + 2) r.push(`BODY ${i + 1} p${i + 1} BODY +${pb.scrollHeight - pb.clientHeight}px ${pg.dataset.t}`);
      pg.querySelectorAll('.q').forEach((q, j) => {
        const w = q.querySelector('.work');
        if (q.scrollHeight > q.clientHeight + 1) r.push(`p${i + 1} Q${j + 1} overflow +${q.scrollHeight - q.clientHeight}px ${pg.dataset.t}`);
        else if (w && w.clientHeight < 40) r.push(`p${i + 1} Q${j + 1} small work ${w.clientHeight}px ${pg.dataset.t}`);
      });
    });
    return r;
  });
  console.log(bad.length ? bad.join('\n') : 'NO OVERFLOW');
  if (out) await p.pdf({ path: out, width: '297mm', height: '186mm', printBackground: true, preferCSSPageSize: true });
  await b.close();
})();
