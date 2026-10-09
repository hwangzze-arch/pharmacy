// 2주차 도식
const F = 'font-family="NSKR"';
const T=(x,y,s,o='')=>`<text x="${x}" y="${y}" ${F} ${o}>${s}</text>`;

// 균등 간격 타임라인: ev = [연도, 제목, 부제, 위(-1)/아래(1), 색]
function tl(ev, W=760, H=150){
  const n=ev.length, x0=46, step=(W-2*x0)/(n-1), mid=H/2;
  let o=`<line x1="20" y1="${mid}" x2="${W-20}" y2="${mid}" stroke="#22305a" stroke-width="2.4"/>`;
  ev.forEach(([y,t,s,side,c],i)=>{
    const x=x0+i*step, up=side<0, ly=up?mid-50:mid+50, ty=up?16:H-28;
    o+=`<line x1="${x}" y1="${mid}" x2="${x}" y2="${up?ty+30:ty-14}" stroke="${c}" stroke-width="1.4"/>`;
    o+=`<circle cx="${x}" cy="${mid}" r="6" fill="#fff" stroke="${c}" stroke-width="2.6"/>`;
    o+=T(x,mid+(up?18:-10),y,`font-size="9.5" font-weight="900" fill="${c}" text-anchor="middle"`);
    o+=T(x,ty,t,`font-size="10.5" font-weight="900" fill="${c}" text-anchor="middle"`);
    o+=T(x,ty+13,s,`font-size="8.6" fill="#5b6478" text-anchor="middle"`);
  });
  return `<svg viewBox="0 0 ${W} ${H}" width="100%">${o}</svg>`;
}
function chron(){
  return tl([
    ['1796','천연두 백신','제너 · 최초 백신',-1,'#3b6fd8'],
    ['1928','페니실린','플레밍 · 최초 항생제',1,'#0e8a83'],
    ['1935','프론토실(설파제)','도마크 · 최초 합성 항균제',-1,'#0e8a83'],
    ['1943','1세대 화학 항암제','머스타드 가스 → 항암',1,'#e2553a'],
    ['1953','DNA 이중나선','왓슨·크릭',-1,'#7457d6'],
    ['1978','인간 인슐린','DNA 재조합',1,'#7457d6'],
    ['1999','2세대 표적 항암제','글리벡 · CML',-1,'#e2553a'],
    ['2017','CAR-T','FDA 승인 · 맞춤형',1,'#e2553a'],
  ],760,150);
}
function lawA(){
  return tl([
    ['1848','의약품 수입법','최초 규제(수입만)',-1,'#3b6fd8'],
    ['1902','생물제제관리법','혈청·백신 순도',1,'#3b6fd8'],
    ['1906','순정식품의약법','불량·부정표시 금지',-1,'#3b6fd8'],
    ['1930','FDA 명칭','화학국 → FDA',1,'#5b6478'],
    ['1937','엘릭서 비극','DEG · 105명 사망',-1,'#e2553a'],
    ['1938','FD&C Act','안전성 사전 제출',1,'#3b6fd8'],
    ['1941·45','인슐린·페니실린','수정안(배치 검정)',-1,'#3b6fd8'],
    ['1947','뉘른베르크 강령','자발적 동의',1,'#0e8a83'],
    ['1961','탈리도마이드','기형아 1만 명+',-1,'#e2553a'],
    ['1962','케파우버-해리스','유효성 + 사전승인',1,'#3b6fd8'],
  ],820,150);
}
function lawB(){
  return tl([
    ['1964','헬싱키 선언','IRB 사전 승인',-1,'#0e8a83'],
    ['1972','터스키기 폭로','40년 비치료 실험',1,'#e2553a'],
    ['1974','국가연구법','국가위원회 · IRB',-1,'#3b6fd8'],
    ['1979','벨몬트 보고서','존중·선행·정의',1,'#0e8a83'],
    ['1987','IND 정정 규정','피험자 보호 강화',-1,'#3b6fd8'],
    ['1992','PDUFA','수수료 → 심사 단축',1,'#7457d6'],
    ['1997','FDAMA','PDUFA 연장 · 소아',-1,'#7457d6'],
    ['2022','현대화법 2.0','동물실험 의무 폐지',1,'#7457d6'],
  ],820,150);
}
function passRate(){
  const d=[['1상→2상',63.2,'9.6'],['2상→3상',30.7,'15.2'],['3상→신청',58.1,'49.6'],['신청→승인',85.3,'85.3']];
  const bw=70,gap=38,x0=40,base=150,sc=1.25;
  let o=`<line x1="30" y1="${base}" x2="${x0+4*(bw+gap)}" y2="${base}" stroke="#aab1c2"/>`;
  d.forEach(([n,v,c],i)=>{const x=x0+i*(bw+gap),h=v*sc,low=i==1;
    o+=`<rect x="${x}" y="${base-h}" width="${bw}" height="${h}" rx="6" fill="${low?'#e2553a':'#9fb6ea'}"/>`;
    o+=T(x+bw/2,base-h-6,v+'%',`font-size="13" font-weight="900" fill="${low?'#e2553a':'#22305a'}" text-anchor="middle"`);
    o+=T(x+bw/2,base+15,n,`font-size="10.5" font-weight="700" fill="#1d2433" text-anchor="middle"`);
    o+=T(x+bw/2,base+30,`(승인까지 ${c}%)`,`font-size="9" fill="#5b6478" text-anchor="middle"`);});
  o+=T(x0+1*(bw+gap)+bw/2,base-30.7*sc-24,'가장 큰 벽!',`font-size="10" font-weight="900" fill="#e2553a" text-anchor="middle"`);
  return `<svg viewBox="0 0 470 190" width="100%">${o}</svg>`;
}
function hurdle(){
  const d=[[1997,5.7],[1998,13.2],[1999,18.9],[2000,24.5],[2001,26.4]];
  const bw=52,gap=26,x0=24,base=120,sc=3.4;
  let o=`<line x1="14" y1="${base}" x2="${x0+5*(bw+gap)}" y2="${base}" stroke="#aab1c2"/>`;
  d.forEach(([y,v],i)=>{const x=x0+i*(bw+gap),h=v*sc;
    o+=`<rect x="${x}" y="${base-h}" width="${bw}" height="${h}" rx="5" fill="${i==4?'#e2553a':'#f2a08f'}"/>`;
    o+=T(x+bw/2,base-h-5,v+'%',`font-size="12" font-weight="900" fill="#b8341c" text-anchor="middle"`);
    o+=T(x+bw/2,base+14,y,`font-size="10" fill="#5b6478" text-anchor="middle"`);});
  o+=`<path d="M${x0+bw/2},${base-5.7*sc-22} L${x0+4*(bw+gap)+bw/2},${base-26.4*sc-22}" stroke="#e2553a" stroke-width="2" marker-end="url(#ar)" fill="none" stroke-dasharray="4 3"/>`;
  return `<svg viewBox="0 0 410 140" width="100%"><defs><marker id="ar" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#e2553a"/></marker></defs>${o}</svg>`;
}
document.querySelectorAll('[data-d]').forEach(el=>{el.innerHTML=window[el.dataset.d]();});
