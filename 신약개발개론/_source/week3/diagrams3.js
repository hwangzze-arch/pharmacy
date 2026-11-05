// 3주차 도식
const F = 'font-family="NSKR"';
const T=(x,y,s,o='')=>`<text x="${x}" y="${y}" ${F} ${o}>${s}</text>`;

function tl(ev, W=760, H=150){
  const n=ev.length, x0=50, step=(W-2*x0)/(n-1), mid=H/2;
  let o=`<line x1="20" y1="${mid}" x2="${W-20}" y2="${mid}" stroke="#22305a" stroke-width="2.4"/>`;
  ev.forEach(([y,t,s,side,c],i)=>{
    const x=x0+i*step, up=side<0, ty=up?16:H-28;
    o+=`<line x1="${x}" y1="${mid}" x2="${x}" y2="${up?ty+30:ty-14}" stroke="${c}" stroke-width="1.4"/>`;
    o+=`<circle cx="${x}" cy="${mid}" r="6" fill="#fff" stroke="${c}" stroke-width="2.6"/>`;
    o+=T(x,mid+(up?18:-10),y,`font-size="9.5" font-weight="900" fill="${c}" text-anchor="middle"`);
    o+=T(x,ty,t,`font-size="10.5" font-weight="900" fill="${c}" text-anchor="middle"`);
    o+=T(x,ty+13,s,`font-size="8.6" fill="#5b6478" text-anchor="middle"`);
  });
  return `<svg viewBox="0 0 ${W} ${H}" width="100%">${o}</svg>`;
}
function aspirin(){
  return tl([
    ['1763','버드나무 껍질','에드워드 스톤 · 열병 효과',-1,'#0e8a83'],
    ['1828','살리실산 추출','부흐너 · 결정 생성',1,'#0e8a83'],
    ['1853','아세틸살리실산 합성','게르하르트',-1,'#3b6fd8'],
    ['1876','최초의 엄격한 임상시험','류머티즘 발열·염증 완화',1,'#e2553a'],
    ['1899','바이엘 아스피린','합성 · 판매',-1,'#3b6fd8'],
    ['1971','작용기전(COX)','존 베인 → 1982 노벨상',1,'#7457d6'],
  ],720,150);
}
// 항암제 세대별 1년 비용 (대략, 백만원) — 로그 눈금
function cost(){
  const d=[['1세대 세포독성','1회 10~50만원','≈ 연 500만',5,'#8d96aa'],['2세대 표적 (타그리소)','월 500~1000만','≈ 연 0.6~1.2억',90,'#3b6fd8'],['3세대 면역 (옵디보·여보이)','월 600~1000만','≈ 연 0.7~1.2억',95,'#0e8a83'],['4세대 CAR-T (킴리아)','1회 3~5억','≈ 1회 4억',400,'#e2553a']];
  const x0=150,W=300,lg=v=>Math.log10(v)/Math.log10(500)*W;
  let o='';
  d.forEach(([n,a,b,v,c],i)=>{const y=12+i*38,w=Math.max(lg(v),18);
    o+=T(x0-8,y+14,n,`font-size="10" font-weight="700" fill="#1d2433" text-anchor="end"`);
    o+=T(x0-8,y+27,a,`font-size="8.6" fill="#5b6478" text-anchor="end"`);
    o+=`<rect x="${x0}" y="${y}" width="${w}" height="24" rx="5" fill="${c}"/>`;
    o+=T(x0+w+6,y+16,b,`font-size="10" font-weight="900" fill="${c}"`);});
  return `<svg viewBox="0 0 560 165" width="100%">${o}${T(x0,162,'※ 막대는 로그 눈금 (1년 기준 대략값)','font-size="8" fill="#8d96aa"')}</svg>`;
}
// 아스피린 vs 항체 크기
function size(){
  return `<svg viewBox="0 0 300 132" width="100%">
  <circle cx="40" cy="70" r="5" fill="#e39a12"/>${T(40,98,'아스피린','font-size="10" font-weight="900" fill="#b97900" text-anchor="middle"')}${T(40,111,'180 Da','font-size="9" fill="#5b6478" text-anchor="middle"')}
  <circle cx="200" cy="58" r="52" fill="#dbe6ff" stroke="#3b6fd8" stroke-width="2"/>
  <path d="M200,90 L200,62 L178,36 M200,62 L222,36" stroke="#3b6fd8" stroke-width="7" stroke-linecap="round" fill="none"/>
  ${T(200,126,'단일클론항체 150,000 Da','font-size="10" font-weight="900" fill="#22305a" text-anchor="middle"')}
  ${T(105,60,'≈ 830배 →','font-size="11" font-weight="900" fill="#e2553a" text-anchor="middle"')}</svg>`;
}
// 신약 vs 개량신약 vs 제네릭
function ladder(){
  const d=[['신약 (혁신)','10~15년','1000억↑','6년','#22305a',15],['개량신약','3~5년','10~40억','4년','#3b6fd8',5],['제네릭','2~3년','2~3억','없음','#8d96aa',3]];
  let o='';
  d.forEach(([n,y,c,e,col,v],i)=>{const yy=14+i*44,w=v*22;
    o+=T(0,yy+17,n,`font-size="11" font-weight="900" fill="${col}"`);
    o+=`<rect x="90" y="${yy}" width="${w}" height="26" rx="6" fill="${col}"/>`;
    o+=T(96,yy+17,y,`font-size="10" font-weight="900" fill="#fff"`);
    o+=T(90+w+8,yy+11,'비용 '+c,`font-size="9" fill="#1d2433"`);
    o+=T(90+w+8,yy+24,'독점 '+e,`font-size="9" font-weight="700" fill="${col}"`);});
  return `<svg viewBox="0 0 520 145" width="100%">${o}</svg>`;
}
// 혈중농도 곡선 공통
function curve(fn,x0,y0,w,h,n=80){let p='';for(let i=0;i<=n;i++){const t=i/n;p+=(i?'L':'M')+(x0+t*w).toFixed(1)+','+(y0-fn(t)*h).toFixed(1)+' ';}return p;}
function be(){
  const x0=40,y0=150,w=400,h=120;
  const f=t=>{const k=t*10;return 1.6*(Math.exp(-0.45*k)-Math.exp(-1.8*k));};
  const g=t=>{const k=t*10;return 1.55*(Math.exp(-0.45*k)-Math.exp(-1.7*k));};
  return `<svg viewBox="0 0 470 185" width="100%">
  <path d="${curve(f,x0,y0,w,h)} L${x0+w},${y0} L${x0},${y0} Z" fill="#3b6fd8" opacity=".12"/>
  <line x1="${x0}" y1="${y0}" x2="${x0+w}" y2="${y0}" stroke="#8d96aa"/><line x1="${x0}" y1="${y0}" x2="${x0}" y2="20" stroke="#8d96aa"/>
  <path d="${curve(f,x0,y0,w,h)}" fill="none" stroke="#3b6fd8" stroke-width="2.6"/>
  <path d="${curve(g,x0,y0,w,h)}" fill="none" stroke="#e2553a" stroke-width="2.4" stroke-dasharray="6 4"/>
  <line x1="${x0+41}" y1="${y0-1.6*0.58*h}" x2="${x0+41}" y2="${y0}" stroke="#22305a" stroke-dasharray="3 3"/>
  ${T(x0+46,y0-1.6*0.58*h-4,'Cmax (최고농도)','font-size="10" font-weight="900" fill="#22305a"')}
  ${T(x0+41,y0+14,'Tmax','font-size="9.5" font-weight="700" fill="#22305a" text-anchor="middle"')}
  ${T(x0+170,y0-10,'AUC = 면적 = 흡수된 총량','font-size="10" font-weight="900" fill="#3b6fd8" stroke="#fff" stroke-width="3" paint-order="stroke"')}
  ${T(x0+w-4,y0+14,'시간 →','font-size="9" fill="#5b6478" text-anchor="end"')}
  ${T(x0-4,16,'혈중농도','font-size="9" fill="#5b6478"')}
  <line x1="300" y1="34" x2="330" y2="34" stroke="#3b6fd8" stroke-width="2.6"/>${T(336,38,'오리지널','font-size="10" font-weight="700" fill="#3b6fd8"')}
  <line x1="300" y1="52" x2="330" y2="52" stroke="#e2553a" stroke-width="2.4" stroke-dasharray="6 4"/>${T(336,56,'제네릭','font-size="10" font-weight="700" fill="#e2553a"')}
  ${T(235,180,'AUC·Cmax 비의 90% 신뢰구간이 80~125% → “동등”','font-size="10" font-weight="900" fill="#13693f" text-anchor="middle"')}
  </svg>`;
}
// 일반정 vs 서방정 vs 장용정
function release(){
  const x0=40,y0=140,w=420,h=110;
  const ir=t=>{const k=t*10;return 1.5*(Math.exp(-0.7*k)-Math.exp(-3*k));};
  const sr=t=>{const k=t*10;return 0.62*(Math.exp(-0.18*k)-Math.exp(-1.2*k));};
  const ec=t=>{const k=t*10-2.2;return k<0?0:1.4*(Math.exp(-0.7*k)-Math.exp(-3*k));};
  return `<svg viewBox="0 0 480 175" width="100%">
  <rect x="${x0}" y="20" width="${0.22*w}" height="${y0-20}" fill="#fff4dc"/>${T(x0+0.11*w,34,'위 (산성)','font-size="9.5" font-weight="700" fill="#b97900" text-anchor="middle"')}
  <rect x="${x0+0.22*w}" y="20" width="${0.78*w}" height="${y0-20}" fill="#e2f5f2" opacity=".6"/>${T(x0+0.5*w,34,'장 (중성) →','font-size="9.5" font-weight="700" fill="#0e8a83" text-anchor="middle"')}
  <line x1="${x0}" y1="${y0}" x2="${x0+w}" y2="${y0}" stroke="#8d96aa"/><line x1="${x0}" y1="${y0}" x2="${x0}" y2="20" stroke="#8d96aa"/>
  <path d="${curve(ir,x0,y0,w,h)}" fill="none" stroke="#8d96aa" stroke-width="2.2"/>
  <path d="${curve(sr,x0,y0,w,h)}" fill="none" stroke="#3b6fd8" stroke-width="2.8"/>
  <path d="${curve(ec,x0,y0,w,h)}" fill="none" stroke="#e2553a" stroke-width="2.8"/>
  ${T(x0+52,52,'일반정: 빨리 올라 빨리 떨어짐','font-size="9.5" font-weight="700" fill="#5b6478"')}
  ${T(x0+300,y0-40,'서방정: 천천히·오래 (시간 조절)','font-size="10" font-weight="900" fill="#3b6fd8"')}
  ${T(x0+218,62,'장용정: 위에선 0 → 장에서 녹음 (장소 조절)','font-size="10" font-weight="900" fill="#e2553a"')}
  ${T(x0+w-4,y0+14,'시간 →','font-size="9" fill="#5b6478" text-anchor="end"')}${T(x0-4,16,'혈중농도','font-size="9" fill="#5b6478"')}
  </svg>`;
}
function imdPie(){
  const parts=[[60,'#3b6fd8','새로운 조성(복합제) 60%'],[27.2,'#0e8a83','제제개선(동일 경로) 27.2%'],[5.6,'#e39a12','새로운 염·이성체 5.6%'],[4.0,'#7457d6','새로운 투여경로 4.0%'],[3.2,'#e2553a','새로운 효능·효과 3.2%']];
  let a=0,out='';const R=52,r=30,cx=60,cy=62;
  parts.forEach(([v,c])=>{const a1=a/100*2*Math.PI-Math.PI/2,a2=(a+v)/100*2*Math.PI-Math.PI/2;const L=v>50?1:0;
    const p=(ang,rad)=>`${cx+rad*Math.cos(ang)},${cy+rad*Math.sin(ang)}`;
    out+=`<path d="M${p(a1,R)} A${R},${R} 0 ${L} 1 ${p(a2,R)} L${p(a2,r)} A${r},${r} 0 ${L} 0 ${p(a1,r)} Z" fill="${c}" stroke="#fff" stroke-width="1.6"/>`;a+=v;});
  const leg=parts.map(([v,c,n],i)=>`<rect x="128" y="${16+i*20}" width="11" height="11" rx="3" fill="${c}"/>${T(145,25+i*20,n,`font-size="10" font-weight="${i==0?900:500}" fill="#1d2433"`)}`).join('');
  return `<svg viewBox="0 0 300 124" width="100%">${out}${T(60,66,'개량신약','font-size="9" font-weight="900" fill="#22305a" text-anchor="middle"')}${leg}</svg>`;
}
document.querySelectorAll('[data-d]').forEach(el=>{el.innerHTML=window[el.dataset.d]();});
