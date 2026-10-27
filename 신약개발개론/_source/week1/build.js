const { chromium } = require('playwright');
(async()=>{
  const [,,html,pdf,pngdir]=process.argv;
  const b=await chromium.launch(); const p=await b.newPage({viewport:{width:1123,height:703}});
  await p.goto('file://'+html); await p.evaluate(()=>document.fonts.ready); await p.waitForTimeout(500);
  const issues=await p.evaluate(()=>{const out=[];document.querySelectorAll('.page').forEach((pg,i)=>{const pr=pg.getBoundingClientRect();const bot=pr.bottom-12;pg.querySelectorAll('.body *').forEach(el=>{const r=el.getBoundingClientRect();if(r.height>0&&r.bottom>bot+1)out.push(`p${i+1}: ${el.className||el.tagName} over ${(r.bottom-bot).toFixed(0)}px`);});
    pg.querySelectorAll('.q').forEach(q=>{if(q.scrollHeight>q.clientHeight+1)out.push(`p${i+1}: q clipped ${q.scrollHeight-q.clientHeight}`)});});return out.slice(0,60);});
  console.log(issues.join('\n')||'no overflow');
  await p.pdf({path:pdf,width:'297mm',height:'186mm',printBackground:true,preferCSSPageSize:true});
  await b.close();
})();
