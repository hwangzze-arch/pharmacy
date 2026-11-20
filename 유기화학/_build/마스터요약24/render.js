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
      const bad = [...pg.querySelectorAll('.main,.side,.acol')].some(c => c.scrollHeight > c.clientHeight + 1) || (pg.querySelector('.ft') && [...pg.querySelectorAll('.one,.mband,.nr')].some(x => x.getBoundingClientRect().bottom > pg.querySelector('.ft').getBoundingClientRect().top + 1));
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
      if (pg.classList.contains('qp')) {  // 한 쪽 2문제: 칸마다 문제 → 정답·해설
        const C = [...pg.querySelectorAll('.qa')];
        // 아래쪽 정렬이라 위로 넘친 것은 scrollHeight에 안 잡힘 → 자식 높이 합으로
        const ov = (c) => { const k = [...c.children]; return k.reduce((s, x) => s + x.getBoundingClientRect().height, 0) + 6 * Math.max(0, k.length - 1) > c.clientHeight + 1; };
        pg.querySelectorAll('.mz').forEach(z => { z.style.zoom = 1; const w = z.parentElement.clientWidth - 24; z.style.zoom = Math.min(1, w / z.getBoundingClientRect().width); });
        let fs = 13; pg.style.setProperty('--fs', fs + 'px');
        while (C.some(ov) && fs > 11.6) { fs -= 0.2; pg.style.setProperty('--fs', fs + 'px'); }
        let ik = 1;  // 그림을 줄여서라도 2문제가 한 쪽에 들어가면 그렇게 (최소 70 %)
        while (C.some(ov) && ik > 0.7) { ik -= 0.05; pg.style.setProperty('--ik', ik.toFixed(2)); pg.querySelectorAll('.mz').forEach(z => { const p = z.parentElement; z.style.zoom = 1; z.style.zoom = Math.min(1, (p.clientWidth - 24) / z.getBoundingClientRect().width) * ik; }); }
        res.push({ i: i + 1, ik: +ik.toFixed(2), qp: C.map(c => c.dataset.qid), over: C.map(ov), fs: Math.round(fs * 10) / 10, overflow: C.some(ov) });
        return;
      }
      if (pg.classList.contains('q1')) {  // 1문제 쪽: 위 문제, 아래 정답·해설(두 단). 넘치면 글자 → 그림 순으로 줄여 한 쪽에
        const B = pg.querySelector('.q1b') || pg.querySelector('.q1f');
        const ov = () => B.scrollHeight > B.clientHeight + 2 || B.scrollWidth > B.clientWidth + 2;
        const fitz = (ik) => pg.querySelectorAll('.mz').forEach(z => { const p = z.parentElement; z.style.zoom = 1; z.style.zoom = Math.min(1, (p.clientWidth - 24) / z.getBoundingClientRect().width) * ik; });
        let fs = 13.2, ik = 1; pg.style.setProperty('--fs', fs + 'px'); fitz(1);
        while (ov() && fs > 11.6) { fs -= 0.2; pg.style.setProperty('--fs', fs + 'px'); }
        while (ov() && ik > 0.35) { ik -= 0.05; pg.style.setProperty('--ik', ik.toFixed(2)); fitz(ik); }
        res.push({ i: i + 1, q1: pg.dataset.qid, ik: +ik.toFixed(2), fs: Math.round(fs * 10) / 10, overflow: ov() });
        return;
      }
      if (pg.classList.contains('q2')) {  // 왼쪽 문제 / 오른쪽 정답·해설: 그림은 그대로, 글자만 조금
        const L = pg.querySelector('.lcol'), R = pg.querySelector('.rcol');
        const ov = (c) => c.scrollHeight > c.clientHeight + 1;
        pg.querySelectorAll('.mz').forEach(z => { z.style.zoom = 1; const w = z.parentElement.clientWidth - 24; z.style.zoom = Math.min(1, w / z.getBoundingClientRect().width); });
        let fs = 13.2; pg.style.setProperty('--fs', fs + 'px');
        while ((ov(L) || ov(R)) && fs > 11.6) { fs -= 0.2; pg.style.setProperty('--fs', fs + 'px'); }
        let ik = 1;  // 그래도 넘치면 그림을 같이 줄여 한 쪽에 (계속 쪽 없음)
        while ((ov(L) || ov(R)) && ik > 0.4) { ik -= 0.05; pg.style.setProperty('--ik', ik.toFixed(2)); pg.querySelectorAll('.mz').forEach(z => { const p = z.parentElement; z.style.zoom = 1; z.style.zoom = Math.min(1, (p.clientWidth - 24) / z.getBoundingClientRect().width) * ik; }); }
        res.push({ i: i + 1, q2: pg.dataset.qid, part: pg.dataset.part, ik: +(pg.style.getPropertyValue('--ik') || 1), fs: Math.round(fs * 10) / 10, overL: ov(L), overR: ov(R), overflow: ov(L) || ov(R) });
        return;
      }
      let fs = 12.8, imgh = 240, guard = 0;
      const bands = [...pg.querySelectorAll('.mband .mz, .afig .mz')];
      pg.style.setProperty('--fs', fs + 'px');
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
        pg.classList.add('side'); fs = 12.8; imgh = 240; guard = 0;
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
  // 삼성노트 필기 칸: 넘치면 그 칸 글자만 줄이기 (쪽 배치는 그대로)
  await page.evaluate(() => document.querySelectorAll('.mnote').forEach(m => { let f = m.classList.contains('big') ? 1.45 : 1; m.style.setProperty('--nfs', f + 'em');
    while (m.scrollHeight > m.clientHeight + 1 && f > 0.55) { f -= 0.03; m.style.setProperty('--nfs', f + 'em'); } }));
  const nt = await page.evaluate(() => [...document.querySelectorAll('.mnote')].map(m => [m.closest('.page') && [...document.querySelectorAll('.page')].indexOf(m.closest('.page')) + 1, (m.style.getPropertyValue('--nfs') || '1em'), m.scrollHeight > m.clientHeight + 1]));
  console.log('notes', JSON.stringify(nt));
  report.filter(r => r.fs < 11 || r.overflow).forEach(r => console.log(JSON.stringify(r)));
  require('fs').writeFileSync(path.join(dir, '_report.json'), JSON.stringify(report));
  await page.pdf({ path: process.argv[2], width: '297mm', height: '210mm', printBackground: true, preferCSSPageSize: true });
  if (process.argv[3]) {
    const els = await page.$$('.page');
    for (const n of process.argv[3].split(',')) {
      await els[parseInt(n) - 1].screenshot({ path: path.join(dir, `shot-${n}.png`) });
    }
  }
  await browser.close();
})();
