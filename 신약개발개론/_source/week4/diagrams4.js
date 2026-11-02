// 4주차 도식
const F = 'font-family="NSKR"';
const T=(x,y,s,o='')=>`<text x="${x}" y="${y}" ${F} ${o}>${s}</text>`;

function tl(ev, W=760, H=150){
  const n=ev.length, x0=50, step=(W-2*x0)/(n-1), mid=H/2;
  let o=`<line x1="20" y1="${mid}" x2="${W-20}" y2="${mid}" stroke="#22305a" stroke-width="2.4"/>`;
  ev.forEach(([y,t,s,side,c],i)=>{
    const x=x0+i*step, up=side<0, ty=up?16:H-28;
    o+=`<line x1="${x}" y1="${mid}" x2="${x}" y2="${up?ty+30:ty-14}" stroke="${c}" stroke-width="1.4"/>`;
    o+=`<circle cx="${x}" cy="${mid}" r="${c=='#e2553a'&&y=='2005'?8:6}" fill="${c=='#e2553a'&&y=='2005'?'#e2553a':'#fff'}" stroke="${c}" stroke-width="2.6"/>`;
    o+=T(x,mid+(up?20:-12),y,`font-size="9.5" font-weight="900" fill="${c}" text-anchor="middle"`);
    o+=T(x,ty,t,`font-size="10.2" font-weight="900" fill="${c}" text-anchor="middle"`);
    o+=T(x,ty+13,s,`font-size="8.5" fill="#5b6478" text-anchor="middle"`);
  });
  return `<svg viewBox="0 0 ${W} ${H}" width="100%">${o}</svg>`;
}
function history(){
  return tl([
    ['1961','mRNA 발견','기능 규명',-1,'#3b6fd8'],
    ['1965','리포솜','최초 지질 기포',1,'#0e8a83'],
    ['1984','mRNA 합성(IVT)','Krieg·Melton (하버드)',-1,'#3b6fd8'],
    ['1989','리포솜 전달','Felgner·Malone',1,'#0e8a83'],
    ['1993','쥐 면역 유도','Transgene → DNA로 전환',-1,'#8d96aa'],
    ['1997','CureVac','Hoerr · Gilboa(암)',1,'#8d96aa'],
    ['2005','변형 RNA (Ψ)','카리코·와이스먼 ★',-1,'#e2553a'],
    ['2008·10','BioNTech·Moderna','산업화',1,'#7457d6'],
    ['2018','LNP 첫 약','파티시란(온파트로)',-1,'#0e8a83'],
    ['2020','코로나 mRNA 백신','긴급사용승인',1,'#e2553a'],
  ],860,150);
}
function dogma(){
  const box=(x,w,t,s,c,f='#fff')=>`<rect x="${x}" y="40" width="${w}" height="46" rx="8" fill="${f}" stroke="${c}" stroke-width="2"/>${T(x+w/2,60,t,`font-size="11.5" font-weight="900" fill="${c}" text-anchor="middle"`)}${T(x+w/2,77,s,'font-size="8.8" fill="#5b6478" text-anchor="middle"')}`;
  const ar=(x1,x2,t)=>`<line x1="${x1}" y1="63" x2="${x2-4}" y2="63" stroke="#22305a" stroke-width="2" marker-end="url(#a4)"/>${T((x1+x2)/2,34,t,'font-size="9" font-weight="700" fill="#22305a" text-anchor="middle"')}`;
  return `<svg viewBox="0 0 640 118" width="100%"><defs><marker id="a4" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10z" fill="#22305a"/></marker></defs>
  <rect x="0" y="22" width="300" height="78" rx="10" fill="#f3f4f7"/>${T(10,16,'핵 (nucleus)','font-size="9.5" font-weight="700" fill="#5b6478"')}
  ${T(330,16,'세포질 (cytoplasm)','font-size="9.5" font-weight="700" fill="#5b6478"')}
  ${box(8,80,'DNA','이중가닥 · A T G C','#22305a')}${ar(88,118,'전사')}
  ${box(118,90,'pre-mRNA','엑손 + 인트론','#5b6478')}${ar(208,232,'스플라이싱')}
  ${box(232,62,'mRNA','성숙','#3b6fd8')}${ar(294,350,'핵 밖으로')}
  ${box(350,110,'리보솜','번역 (코돈 3개 = aa 1)','#0e8a83','#e2f5f2')}${ar(460,488,'')}
  ${box(488,140,'단백질 (항원)','스파이크 단백질','#e39a12','#fff4dc')}
  <path d="M410,102 L410,90" stroke="#e2553a" stroke-width="2.2" marker-end="url(#a4)"/>${T(410,116,'mRNA 백신은 여기로 바로 투입 → 핵·DNA 안 거침','font-size="10" font-weight="900" fill="#e2553a" text-anchor="middle"')}
  </svg>`;
}
function struct(){
  const seg=[['5′ cap','#22305a',48],['5′ UTR','#8d96aa',62],['ORF (스파이크 단백질 정보)','#3b6fd8',250],['3′ UTR','#8d96aa',62],['poly(A) 꼬리','#e39a12',96]];
  let x=10,o='';
  seg.forEach(([n,c,w])=>{o+=`<rect x="${x}" y="22" width="${w-3}" height="34" rx="6" fill="${c}"/>`+T(x+w/2-1,44,n,`font-size="10" font-weight="900" fill="#fff" text-anchor="middle"`);x+=w;});
  for(let i=0;i<9;i++){const xx=150+i*24;o+=`<circle cx="${xx}" cy="72" r="7" fill="#fdece7" stroke="#e2553a" stroke-width="1.6"/>`+T(xx,76,'Ψ','font-size="9" font-weight="900" fill="#e2553a" text-anchor="middle"');}
  o+=T(380,76,'← U를 전부 m1Ψ로 (염증↓ 번역↑)','font-size="9.5" font-weight="700" fill="#e2553a"');
  o+=T(10,14,'5′','font-size="9" fill="#5b6478"')+T(530,14,'3′','font-size="9" fill="#5b6478"');
  return `<svg viewBox="0 0 540 88" width="100%">${o}</svg>`;
}
function psi(){
  const d=[['변형 없음',200],['m5C',180],['m6A',210],['Ψ (슈도우리딘)',0],['m5U',0],['s2U',0],['m6A/Ψ',0]];
  let o='';const x0=110,sc=1.5;
  d.forEach(([n,v],i)=>{const y=8+i*22,good=v==0;
    o+=T(x0-6,y+13,n,`font-size="10" font-weight="${good?900:500}" fill="${good?'#13693f':'#1d2433'}" text-anchor="end"`);
    o+=v?`<rect x="${x0}" y="${y}" width="${v*sc}" height="15" rx="4" fill="#e2553a"/>`+T(x0+v*sc+5,y+12,'염증 ↑','font-size="9" fill="#b8341c"'):T(x0+4,y+12,'N.D. (거의 0) ✔','font-size="9.5" font-weight="900" fill="#1f9a5c"');});
  o+=`<rect x="2" y="${8+3*22-3}" width="440" height="${4*22}" rx="6" fill="none" stroke="#1f9a5c" stroke-width="1.6" stroke-dasharray="5 3"/>`;
  return `<svg viewBox="0 0 450 170" width="100%">${o}${T(x0,166,'수지상세포(DC1) TNF-α 분비 — Karikó 2005 Immunity','font-size="8.6" fill="#5b6478"')}</svg>`;
}
function labjab(){
  const d=[['장티푸스',1884,1989],['수막염',1889,1981],['백일해',1906,1948],['소아마비',1908,1955],['수두',1953,1995],['홍역',1953,1963],['B형간염',1965,1981],['에볼라',1976,2019],['HPV',1981,2006],['COVID-19',2020,2020]];
  const x=y=>60+(y-1880)*2.6;let o='';
  [1880,1920,1960,2000,2020].forEach(y=>o+=`<line x1="${x(y)}" y1="6" x2="${x(y)}" y2="216" stroke="#e6e9f1"/>`+T(x(y),228,y,'font-size="8.5" fill="#8d96aa" text-anchor="middle"'));
  d.forEach(([n,a,b],i)=>{const yy=14+i*20,c=n=='COVID-19';
    o+=T(54,yy+4,n,`font-size="9.5" font-weight="${c?900:500}" fill="${c?'#e2553a':'#1d2433'}" text-anchor="end"`);
    o+=`<line x1="${x(a)}" y1="${yy}" x2="${x(b)}" y2="${yy}" stroke="${c?'#e2553a':'#aab1c2'}" stroke-width="3"/><circle cx="${x(a)}" cy="${yy}" r="4" fill="${c?'#e2553a':'#5b6478'}"/><circle cx="${x(b)}" cy="${yy}" r="4.5" fill="#fff" stroke="${c?'#e2553a':'#5b6478'}" stroke-width="2"/>`;
    o+=T(x(b)+8,yy+4,c?'같은 해!':(b-a)+'년',`font-size="9" font-weight="700" fill="${c?'#e2553a':'#5b6478'}"`);});
  return `<svg viewBox="0 0 450 234" width="100%">${o}</svg>`;
}
document.querySelectorAll('[data-d]').forEach(el=>{el.innerHTML=window[el.dataset.d]();});
