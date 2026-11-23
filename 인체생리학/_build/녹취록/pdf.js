// 사용법: node pdf.js 본문.html 출력.pdf  (head.html + 본문을 합쳐 PDF로, 넘침 검사)
const fs = require('fs'), path = require('path');
const { chromium } = require('/opt/node22/lib/node_modules/playwright');
(async () => {
  const [, , body, out] = process.argv;
  const head = fs.readFileSync(path.join(__dirname, 'head.html'), 'utf8');
  const tmp = path.join(require('os').tmpdir(), 'lec_' + process.pid + '.html');
  fs.writeFileSync(tmp, head + fs.readFileSync(body, 'utf8'));
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1123, height: 703 } });
  await p.goto('file://' + tmp, { waitUntil: 'networkidle' });
  await p.emulateMedia({ media: 'print' });
  const bad = await p.evaluate(() => {
    const r = [];
    document.querySelectorAll('.pg').forEach((pg, i) => {
      const pb = pg.querySelector('.pb');
      if (pb && pb.scrollHeight > pb.clientHeight + 2) r.push(`p${i + 1} BODY +${pb.scrollHeight - pb.clientHeight}px`);
    });
    return r;
  });
  console.log(bad.length ? bad.join('\n') : 'NO OVERFLOW');
  if (out) await p.pdf({ path: out, width: '297mm', height: '186mm', printBackground: true, preferCSSPageSize: true });
  await b.close();
  fs.unlinkSync(tmp);
})();
