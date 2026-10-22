const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({viewport:{width:794,height:1123}});
  await p.goto('file://' + __dirname + '/mock.html'); await p.evaluate(() => document.fonts.ready);
  await p.emulateMedia({ media: 'print' });
  const o = await p.evaluate(() => [...document.querySelectorAll('.pg')].map((g,i)=>{const c=g.querySelector('.cols');const ov=g.scrollHeight>g.clientHeight+1||(c&&c.scrollWidth>c.clientWidth+1);return ov?i+1:0}).filter(x=>x));
  console.log('overflow', o);
  await p.pdf({ path: __dirname + '/mock.pdf', width: '210mm', height: '297mm', printBackground: true, preferCSSPageSize: true });
  await b.close();
})();
