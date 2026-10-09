// 5주차 도식
const F = 'font-family="NSKR"';
const T=(x,y,s,o='')=>`<text x="${x}" y="${y}" ${F} ${o}>${s}</text>`;
const AR=`<defs><marker id="a5" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10z" fill="#22305a"/></marker></defs>`;

function tl(ev, W=760, H=150){
  const n=ev.length, x0=46, step=(W-2*x0)/(n-1), mid=H/2;
  let o=`<line x1="20" y1="${mid}" x2="${W-20}" y2="${mid}" stroke="#22305a" stroke-width="2.4"/>`;
  ev.forEach(([y,t,s,side,c],i)=>{
    const x=x0+i*step, up=side<0, ty=up?16:H-28;
    o+=`<line x1="${x}" y1="${mid}" x2="${x}" y2="${up?ty+30:ty-14}" stroke="${c}" stroke-width="1.4"/>`;
    o+=`<circle cx="${x}" cy="${mid}" r="6" fill="#fff" stroke="${c}" stroke-width="2.6"/>`;
    o+=T(x,mid+(up?20:-12),y,`font-size="9.3" font-weight="900" fill="${c}" text-anchor="middle"`);
    o+=T(x,ty,t,`font-size="10" font-weight="900" fill="${c}" text-anchor="middle"`);
    o+=T(x,ty+13,s,`font-size="8.4" fill="#5b6478" text-anchor="middle"`);
  });
  return `<svg viewBox="0 0 ${W} ${H}" width="100%">${o}</svg>`;
}
function life(){
  return tl([
    ['1955','헝가리 출생','솔노크',-1,'#5b6478'],
    ['1982 (27)','생화학 박사','세게드 대학교',1,'#5b6478'],
    ['1985 (30)','미국행','테디베어 속 900파운드',-1,'#e2553a'],
    ['1989 (34)','UPenn','바나단과 mRNA',1,'#3b6fd8'],
    ['1995 (40)','강등','연구비 계속 탈락',-1,'#e2553a'],
    ['1997 (42)','와이스먼 만남','복사기 앞 우연',1,'#0e8a83'],
    ['2005 (50)','Immunity 논문','Nature·Science 거절',-1,'#7457d6'],
    ['2006~13','RNARx CEO','특허 → Cellscript',1,'#5b6478'],
    ['2013~22','BioNTech','부사장 → 수석부사장',-1,'#3b6fd8'],
    ['2023 (68)','노벨상','와이스먼과 공동',1,'#e39a12'],
  ],860,150);
}
function nobels(){
  return tl([
    ['2023 생리의학','mRNA 백신','카리코·와이스먼 · Ψ',-1,'#e2553a'],
    ['2024 생리의학','microRNA','Ambros·Ruvkun',1,'#0e8a83'],
    ['2024 화학','단백질 설계·구조','Baker / Hassabis·Jumper',-1,'#3b6fd8'],
    ['2024 물리','인공신경망','Hopfield·Hinton',1,'#7457d6'],
    ['2025 생리의학','말초 면역관용','Brunkow·Ramsdell·Sakaguchi',-1,'#e39a12'],
    ['2026 ?','후보: GLP-1 · 부착 수용체','발표 10.5~12',1,'#5b6478'],
  ],820,150);
}
function mirna(){
  const b=(x,y,w,t,s,c,f='#fff')=>`<rect x="${x}" y="${y}" width="${w}" height="40" rx="7" fill="${f}" stroke="${c}" stroke-width="1.8"/>${T(x+w/2,y+17,t,`font-size="10.5" font-weight="900" fill="${c}" text-anchor="middle"`)}${T(x+w/2,y+32,s,'font-size="8.5" fill="#5b6478" text-anchor="middle"')}`;
  const a=(x1,y1,x2,y2,t,tx,ty)=>`<line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" stroke="#22305a" stroke-width="1.8" marker-end="url(#a5)"/>`+(t?T(tx,ty,t,'font-size="9.2" font-weight="900" fill="#e2553a" text-anchor="middle"'):'');
  return `<svg viewBox="0 0 660 170" width="100%">${AR}
  <rect x="0" y="18" width="260" height="70" rx="10" fill="#f3f4f7"/>${T(8,13,'핵','font-size="9.5" font-weight="700" fill="#5b6478"')}${T(280,13,'세포질','font-size="9.5" font-weight="700" fill="#5b6478"')}
  ${b(8,32,100,'pri-miRNA','머리핀 구조','#22305a')}${a(108,52,146,52,'Drosha',127,27)}
  ${b(150,32,100,'pre-miRNA','짧아진 머리핀','#22305a')}${a(250,52,290,52,'Exportin-5',272,27)}
  ${b(294,32,108,'Dicer 절단','→ 이중가닥 ~22 nt','#3b6fd8')}
  ${T(272,74,'(핵 밖으로)','font-size="8" fill="#5b6478" text-anchor="middle"')}
  ${a(402,52,438,52,'풀림',420,27)}
  ${b(442,32,110,'RISC','Argonaute + 한 가닥','#7457d6','#efeaff')}
  ${T(497,88,'동승 가닥(passenger)은 버림','font-size="8.5" fill="#5b6478" text-anchor="middle"')}
  ${a(497,94,400,120,'')}${a(497,94,600,120,'')}
  ${b(290,122,200,'불완전 결합 (seed 2~8번)','동물 → 번역 억제 + 탈아데닐화','#0e8a83','#e2f5f2')}
  ${b(500,122,156,'완전 결합','식물 → mRNA 절단·분해','#e39a12','#fff4dc')}
  ${T(8,130,'결과: 단백질 OFF','font-size="11" font-weight="900" fill="#e2553a"')}${T(8,146,'= 전사 “후” 유전자 조절','font-size="9.5" fill="#1d2433"')}${T(8,162,'(mRNA 백신 = 단백질 ON)','font-size="9" fill="#5b6478"')}
  </svg>`;
}
function ai(){
  const s=[['① 표적 발굴','PandaOmics','CDK20 (dark target)','#3b6fd8'],['② 구조 예측','AlphaFold','구조 모르던 표적','#0e8a83'],['③ 분자 생성','Chemistry42','생성형 AI · 2라운드','#7457d6'],['④ 검증','in vitro','세포 증식 억제','#e39a12']];
  let o=AR;
  s.forEach(([a,b,c,col],i)=>{const x=6+i*162;o+=`<rect x="${x}" y="8" width="140" height="66" rx="9" fill="#fff" stroke="${col}" stroke-width="2"/>`+T(x+70,28,a,`font-size="10.5" font-weight="900" fill="${col}" text-anchor="middle"`)+T(x+70,46,b,'font-size="11" font-weight="900" fill="#1d2433" text-anchor="middle"')+T(x+70,63,c,'font-size="8.6" fill="#5b6478" text-anchor="middle"');
    if(i<3)o+=`<line x1="${x+142}" y1="41" x2="${x+160}" y2="41" stroke="#22305a" stroke-width="2" marker-end="url(#a5)"/>`;});
  o+=`<rect x="330" y="84" width="300" height="26" rx="13" fill="#fdece7"/>`+T(480,101,'KD 7300 nM → 180 nM (약 40배↑, 작을수록 강하게 결합)','font-size="9.5" font-weight="900" fill="#b8341c" text-anchor="middle"');
  return `<svg viewBox="0 0 650 116" width="100%">${o}</svg>`;
}
function twosig(){
  return `<svg viewBox="0 0 460 170" width="100%">
  <circle cx="90" cy="85" r="62" fill="#efeaff" stroke="#7457d6" stroke-width="2"/>${T(90,40,'APC (수지상세포)','font-size="10" font-weight="900" fill="#7457d6" text-anchor="middle"')}
  <circle cx="370" cy="85" r="62" fill="#e8f0ff" stroke="#3b6fd8" stroke-width="2"/>${T(370,40,'T세포','font-size="10.5" font-weight="900" fill="#3b6fd8" text-anchor="middle"')}
  <rect x="145" y="58" width="40" height="18" rx="4" fill="#7457d6"/>${T(165,71,'MHC','font-size="8.5" font-weight="700" fill="#fff" text-anchor="middle"')}
  <rect x="275" y="58" width="40" height="18" rx="4" fill="#3b6fd8"/>${T(295,71,'TCR','font-size="8.5" font-weight="700" fill="#fff" text-anchor="middle"')}
  <line x1="185" y1="67" x2="275" y2="67" stroke="#1f9a5c" stroke-width="3"/>${T(230,60,'신호 ① 항원','font-size="9.5" font-weight="900" fill="#1f9a5c" text-anchor="middle"')}
  <rect x="145" y="100" width="40" height="18" rx="4" fill="#7457d6"/>${T(165,113,'B7','font-size="8.5" font-weight="700" fill="#fff" text-anchor="middle"')}
  <rect x="275" y="100" width="40" height="18" rx="4" fill="#3b6fd8"/>${T(295,113,'CD28','font-size="8.5" font-weight="700" fill="#fff" text-anchor="middle"')}
  <line x1="185" y1="109" x2="275" y2="109" stroke="#e39a12" stroke-width="3" stroke-dasharray="6 3"/>${T(230,102,'신호 ② 공동자극','font-size="9.5" font-weight="900" fill="#b97900" text-anchor="middle"')}
  <rect x="200" y="114" width="60" height="16" rx="8" fill="#e2553a"/>${T(230,126,'CTLA-4-Ig','font-size="8.5" font-weight="900" fill="#fff" text-anchor="middle"')}
  ${T(230,152,'①만 오고 ②가 없으면 → Anergy(무반응) · 제거','font-size="10" font-weight="900" fill="#1d2433" text-anchor="middle"')}
  ${T(230,166,'CTLA-4-Ig가 B7을 가려 ② 차단 (아바타셉트)','font-size="9" fill="#e2553a" text-anchor="middle"')}
  </svg>`;
}
document.querySelectorAll('[data-d]').forEach(el=>{el.innerHTML=window[el.dataset.d]();});
