// 중간고사 총정리 도식
const F = 'font-family="NSKR"';
const T=(x,y,s,o='')=>`<text x="${x}" y="${y}" ${F} ${o}>${s}</text>`;

function tl(ev, W=900, H=150){
  const n=ev.length, x0=46, step=(W-2*x0)/(n-1), mid=H/2;
  let o=`<line x1="20" y1="${mid}" x2="${W-20}" y2="${mid}" stroke="#22305a" stroke-width="2.4"/>`;
  ev.forEach(([y,t,s,side,c],i)=>{
    const x=x0+i*step, up=side<0, ty=up?16:H-28;
    o+=`<line x1="${x}" y1="${mid}" x2="${x}" y2="${up?ty+30:ty-14}" stroke="${c}" stroke-width="1.4"/>`;
    o+=`<circle cx="${x}" cy="${mid}" r="6" fill="#fff" stroke="${c}" stroke-width="2.6"/>`;
    o+=T(x,mid+(up?20:-12),y,`font-size="9.6" font-weight="900" fill="${c}" text-anchor="middle"`);
    o+=T(x,ty,t,`font-size="10" font-weight="900" fill="${c}" text-anchor="middle"`);
    o+=T(x,ty+13,s,`font-size="8.4" fill="#5b6478" text-anchor="middle"`);
  });
  return `<svg viewBox="0 0 ${W} ${H}" width="100%">${o}</svg>`;
}
const R='#e2553a',B='#3b6fd8',G='#0e8a83',V='#7457d6',A='#e39a12',N='#5b6478';
function tlOld(){
  return tl([
    ['1796','제너 우두','최초 백신',-1,N],
    ['1906','순정식품의약법','와일리',1,B],
    ['1928','플레밍','페니실린',-1,N],
    ['1935','도마크','프론토실 → 설파',1,R],
    ['1937→38','엘릭서 → FD&C','DEG 신장독성 · 안전성',-1,R],
    ['1947','뉘른베르크','자발적 동의',1,V],
    ['1962','케파우버-해리스','탈리도마이드 · 유효성',-1,R],
    ['1964','헬싱키','치료적·비치료적',1,V],
    ['1979','벨몬트','존중·이익·정의',-1,V],
    ['1992','PDUFA','심사 수수료',1,B],
  ]);
}
function tlNew(){
  return tl([
    ['1982','휴물린','최초 재조합',-1,G],
    ['1984','IVT 합성','Krieg·Melton',1,G],
    ['1999','선플라주','국산 신약 1호',-1,N],
    ['2001·02','조인스·스티렌','천연물신약',1,A],
    ['2005','Ψ 발견','카리코·와이스먼',-1,R],
    ['2020','mRNA 백신','코로나',1,R],
    ['2022','FDA 현대화법 2.0','동물실험 의무 폐지',-1,B],
    ['2023','노벨상 mRNA','염기 변형',1,R],
    ['2024','miRNA · AlphaFold','생리의학 · 화학',-1,V],
    ['2025·26','면역관용 · 광유전학','노벨생리의학상',1,V],
  ]);
}
function flow(){
  const w=[['1주','오리엔테이션','정의 · 깔때기 · 임상','#22305a'],['2주','약물개발의 역사','실패 · 법 · 윤리','#e2553a'],['3주','신약의 분류','합성·바이오·천연물·개량','#0e8a83'],['4주','분류2 · 노벨1','mRNA · Ψ · LNP','#3b6fd8'],['5주','노벨2','miRNA · AlphaFold · 관용','#7457d6'],['6주','후보물질 탐색1','Target → TPP → Hit','#e39a12']];
  let o='';w.forEach(([a,b,c,col],i)=>{const x=4+i*150;
    o+=`<path d="M${x},6 L${x+134},6 L${x+146},34 L${x+134},62 L${x},62 ${i?`L${x+12},34`:''} Z" fill="${col}"/>`;
    o+=T(x+74,24,a+' · '+b,'font-size="10.5" font-weight="900" fill="#fff" text-anchor="middle"')+T(x+74,42,c,'font-size="8.6" fill="#fff" text-anchor="middle"');});
  return `<svg viewBox="0 0 906 66" width="100%">${o}</svg>`;
}
document.querySelectorAll('[data-d]').forEach(el=>{el.innerHTML=window[el.dataset.d]();});
