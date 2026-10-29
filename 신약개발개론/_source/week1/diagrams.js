// 손으로 그린 도식들 — blank=true 이면 빈칸 버전
const F = 'font-family="NSKR"';
function B(txt, blank, key){ return blank ? `(${key})` : txt; }

function funnel(blank){
  const t=(x,y,s,o='')=>`<text x="${x}" y="${y}" ${F} ${o}>${s}</text>`;
  const bl=(x,y,k)=>`<rect x="${x-26}" y="${y-13}" width="52" height="19" rx="5" fill="#fff" stroke="#e2553a" stroke-width="1.4" stroke-dasharray="3 2"/>${t(x,y+1,`(${k})`,'font-size="11" font-weight="900" fill="#e2553a" text-anchor="middle"')}`;
  return `<svg viewBox="0 0 660 250" width="100%">
  <defs><linearGradient id="fg${blank?1:0}" x1="0" x2="1"><stop offset="0" stop-color="#22305a" stop-opacity=".9"/><stop offset="1" stop-color="#3b6fd8" stop-opacity=".85"/></linearGradient></defs>
  <rect x="0" y="28" width="215" height="190" rx="8" fill="#e8f0ff"/>
  <rect x="235" y="28" width="230" height="190" rx="8" fill="#e2f5f2"/>
  <rect x="485" y="28" width="80" height="190" rx="8" fill="#fff4dc"/>
  <rect x="575" y="28" width="85" height="190" rx="8" fill="#efeaff"/>
  ${t(107,20,'① 발굴 + 전임상','font-size="12" font-weight="900" fill="#3b6fd8" text-anchor="middle"')}
  ${t(350,20,'② 임상시험 (사람)','font-size="12" font-weight="900" fill="#0e8a83" text-anchor="middle"')}
  ${t(525,20,'③ FDA 심사','font-size="12" font-weight="900" fill="#b97900" text-anchor="middle"')}
  ${t(617,20,'④ 시판 후','font-size="12" font-weight="900" fill="#7457d6" text-anchor="middle"')}
  <path d="M8,48 C120,52 330,104 560,116 L560,128 C330,140 120,192 8,198 Z" fill="url(#fg${blank?1:0})"/>
  ${blank?bl(70,128,'A'):t(70,121,'5,000~10,000','font-size="12.5" font-weight="900" fill="#fff" text-anchor="middle"')+t(70,137,'후보 화합물','font-size="9.5" fill="#dbe6ff" text-anchor="middle"')}
  ${blank?bl(178,124,'B'):t(178,128,'250','font-size="15" font-weight="900" fill="#fff" text-anchor="middle"')}
  ${blank?bl(300,123,'C'):t(300,127,'5','font-size="15" font-weight="900" fill="#fff" text-anchor="middle"')}
  <circle cx="575" cy="122" r="17" fill="#fff" stroke="#e39a12" stroke-width="3"/>
  ${t(575,127,'1','font-size="15" font-weight="900" fill="#b97900" text-anchor="middle"')}
  <line x1="225" y1="30" x2="225" y2="235" stroke="#e2553a" stroke-width="2.2" stroke-dasharray="5 3"/>
  <line x1="475" y1="30" x2="475" y2="235" stroke="#e2553a" stroke-width="2.2" stroke-dasharray="5 3"/>
  ${blank?bl(225,246,'D'):`<rect x="196" y="232" width="58" height="18" rx="9" fill="#e2553a"/>`+t(225,245,'IND 제출','font-size="10.5" font-weight="900" fill="#fff" text-anchor="middle"')}
  ${blank?bl(475,246,'E'):`<rect x="446" y="232" width="58" height="18" rx="9" fill="#e2553a"/>`+t(475,245,'NDA 제출','font-size="10.5" font-weight="900" fill="#fff" text-anchor="middle"')}
  ${[['1상',265,'20~100'],['2상',345,'100~500'],['3상',425,'1,000~5,000']].map(([p,x,n],i)=>`<rect x="${x-36}" y="160" width="72" height="50" rx="7" fill="#fff" stroke="#9fd8d1"/>${t(x,177,'임상 '+p,'font-size="10.5" font-weight="900" fill="#0e8a83" text-anchor="middle"')}${blank&&i==2?bl(x,197,'F'):t(x,198,n+'명','font-size="10" font-weight="700" fill="#1d2433" text-anchor="middle"')}`).join('')}
  ${t(107,212,'3~6년','font-size="11" font-weight="700" fill="#3b6fd8" text-anchor="middle"')}
  ${t(350,226,'6~7년','font-size="11" font-weight="700" fill="#0e8a83" text-anchor="middle"')}
  ${t(525,212,'0.5~2년','font-size="11" font-weight="700" fill="#b97900" text-anchor="middle"')}
  ${blank?bl(617,180,'G'):t(617,176,'임상 4상','font-size="11" font-weight="900" fill="#7457d6" text-anchor="middle"')+t(617,192,'시판 후 조사','font-size="9.5" fill="#7457d6" text-anchor="middle"')}
  ${t(575,152,'승인 1개!','font-size="10" font-weight="900" fill="#b97900" text-anchor="middle"')}
  </svg>`;
}

function mfds(blank){
  const t=(x,y,s,o='')=>`<text x="${x}" y="${y}" ${F} ${o}>${s}</text>`;
  const bl=(x,y,k,w=52)=>`<rect x="${x-w/2}" y="${y-13}" width="${w}" height="19" rx="5" fill="#fff" stroke="#e2553a" stroke-width="1.4" stroke-dasharray="3 2"/>${t(x,y+1,`(${k})`,'font-size="11" font-weight="900" fill="#e2553a" text-anchor="middle"')}`;
  const box=(x,w,h1,h2,c)=>`<rect x="${x}" y="8" width="${w}" height="48" rx="8" fill="${c}"/>${t(x+w/2,27,h1,'font-size="11.5" font-weight="900" fill="#fff" text-anchor="middle"')}${t(x+w/2,45,h2,'font-size="9" fill="#fff" text-anchor="middle" opacity=".9"')}`;
  return `<svg viewBox="0 0 660 230" width="100%">
  ${box(0,140,'기초·탐색연구','질병 이해 · 타겟 검증','#3b6fd8')}
  ${box(170,120,'비임상','주기안정성 · 후보 최적화','#5a7fd0')}
  ${box(320,190,'임상시험','phase 0 · 1 · 2 · 3','#0e8a83')}
  ${box(540,120,'허가 검토/승인','신약허가 · 시판 후 조사','#e39a12')}
  <circle cx="70" cy="112" r="36" fill="#e8f0ff" stroke="#3b6fd8" stroke-width="2"/>
  ${blank?bl(70,116,'A'):t(70,117,'10,000개','font-size="13" font-weight="900" fill="#22305a" text-anchor="middle"')}
  <circle cx="230" cy="112" r="22" fill="#e8f0ff" stroke="#5a7fd0" stroke-width="2"/>
  ${blank?bl(230,116,'B',44):t(230,117,'50개','font-size="12.5" font-weight="900" fill="#22305a" text-anchor="middle"')}
  <circle cx="415" cy="105" r="14" fill="#e2f5f2" stroke="#0e8a83" stroke-width="2"/>
  ${t(415,110,'5','font-size="12" font-weight="900" fill="#0e8a83" text-anchor="middle"')}
  ${t(415,140,'20~100 · 100~500 · 1,000~5,000명','font-size="9" fill="#5b6478" text-anchor="middle"')}
  <circle cx="600" cy="112" r="10" fill="#fff4dc" stroke="#e39a12" stroke-width="2"/>
  ${t(600,116,'1','font-size="11" font-weight="900" fill="#b97900" text-anchor="middle"')}
  <rect x="296" y="66" width="20" height="100" rx="5" fill="#fdece7" stroke="#e2553a" stroke-width="1.5"/>
  <rect x="516" y="66" width="20" height="100" rx="5" fill="#fdece7" stroke="#e2553a" stroke-width="1.5"/>
  ${blank? t(306,120,'C','font-size="12" font-weight="900" fill="#e2553a" text-anchor="middle"') : [...'임상시험신청'].map((c,i)=>t(306,82+i*15,c,'font-size="10.5" font-weight="900" fill="#e2553a" text-anchor="middle"')).join('')}
  ${blank? t(526,120,'D','font-size="12" font-weight="900" fill="#e2553a" text-anchor="middle"') : [...'신약허가신청'].map((c,i)=>t(526,82+i*15,c,'font-size="10.5" font-weight="900" fill="#e2553a" text-anchor="middle"')).join('')}
  <line x1="0" y1="182" x2="660" y2="182" stroke="#aab1c2" stroke-width="1.2"/>
  ${[[70,'5년'],[230,'1.5년'],[415,'6년'],[600,'2년']].map(([x,s])=>t(x,178,s,'font-size="10.5" font-weight="700" fill="#5b6478" text-anchor="middle"')).join('')}
  <path d="M306,190 L306,205 L660,205 L660,190" fill="none" stroke="#e2553a" stroke-width="1.8" stroke-dasharray="5 3"/>
  ${blank?bl(483,214,'E',70):`<rect x="433" y="198" width="100" height="22" rx="11" fill="#fff" stroke="#e2553a" stroke-width="1.5"/>`+t(483,213,'식약처 관장범위','font-size="10.5" font-weight="900" fill="#e2553a" text-anchor="middle"')}
  </svg>`;
}

function aiChart(){
  const yr=24; // px per year
  const x0=95;
  const seg=(y,arr)=>{let x=x0,out='';arr.forEach(([n,r,mid,c])=>{const w=mid*yr;out+=`<rect x="${x}" y="${y}" width="${w-2}" height="34" rx="5" fill="${c}"/><text x="${x+w/2-1}" y="${y+15}" ${F} font-size="${w<40?8.4:9.6}" font-weight="900" fill="#fff" text-anchor="middle">${n}</text><text x="${x+w/2-1}" y="${y+28}" ${F} font-size="8.6" fill="#fff" text-anchor="middle" opacity=".92">${r}</text>`;x+=w;});return out;};
  const ticks=[...Array(16).keys()].map(i=>`<line x1="${x0+i*yr}" y1="120" x2="${x0+i*yr}" y2="124" stroke="#aab1c2"/>${i%2==0?`<text x="${x0+i*yr}" y="135" ${F} font-size="8.5" fill="#8d96aa" text-anchor="middle">${i}년</text>`:''}`).join('');
  return `<svg viewBox="0 0 470 140" width="100%">
  <text x="0" y="31" ${F} font-size="10.5" font-weight="900" fill="#22305a">기존 방식</text><text x="0" y="45" ${F} font-size="9" fill="#5b6478">≈ 10.5~18년</text>
  ${seg(16,[['타겟','2~3년',2.5,'#3b6fd8'],['스크리닝','0.5~1',0.75,'#4f7fe0'],['최적화','1~3년',2,'#6a8fe3'],['독성','1~3년',2,'#8aa6e8'],['임상 1~3상','5~6년',5.5,'#0e8a83'],['허가','1~2년',1.5,'#e39a12']])}
  <text x="0" y="86" ${F} font-size="10.5" font-weight="900" fill="#e2553a">AI 활용</text><text x="0" y="100" ${F} font-size="9" fill="#5b6478">≈ 6~9년</text>
  ${seg(71,[['빅데이터','0.5~1',0.75,'#e2553a'],['타당성','0.5~1',0.75,'#ec7a62'],['임상 1~3상','4~5년',4.5,'#0e8a83'],['허가','1~2년',1.5,'#e39a12']])}
  <line x1="${x0}" y1="120" x2="${x0+15*yr}" y2="120" stroke="#aab1c2"/>${ticks}
  </svg>`;
}

function donut(){
  const parts=[[40,'#3b6fd8','중간고사 40'],[45,'#22305a','기말고사 45'],[5,'#e39a12','수시과제 5'],[10,'#0e8a83','참여도 10']];
  let a=0,out='';const R=52,r=32,cx=60,cy=60;
  parts.forEach(([v,c])=>{const a1=a/100*2*Math.PI-Math.PI/2,a2=(a+v)/100*2*Math.PI-Math.PI/2;const L=v>50?1:0;
    const p=(ang,rad)=>`${cx+rad*Math.cos(ang)},${cy+rad*Math.sin(ang)}`;
    out+=`<path d="M${p(a1,R)} A${R},${R} 0 ${L} 1 ${p(a2,R)} L${p(a2,r)} A${r},${r} 0 ${L} 0 ${p(a1,r)} Z" fill="${c}" stroke="#fff" stroke-width="2"/>`;a+=v;});
  const leg=parts.map(([v,c,n],i)=>`<rect x="132" y="${16+i*24}" width="12" height="12" rx="3" fill="${c}"/><text x="150" y="${26+i*24}" ${F} font-size="11" font-weight="${i<2?900:500}" fill="#1d2433">${n}점</text>`).join('');
  return `<svg viewBox="0 0 250 120" width="100%">${out}<text x="60" y="58" ${F} font-size="9" fill="#5b6478" text-anchor="middle">시험</text><text x="60" y="73" ${F} font-size="14" font-weight="900" fill="#22305a" text-anchor="middle">85점</text>${leg}</svg>`;
}

function semester(){
  const wx=i=>12+(i-1)*36.5, cx=i=>wx(i)+15;
  // 실제 진행된 강의 (1~6주) + 강의계획서상 이후 일정
  const wk=[[1,'OT'],[2,'역사'],[3,'분류'],[4,'분류2','노벨1'],[5,'노벨2'],[6,'후보','발굴']];
  const grp=[[9,12,'임상시험 (준비 → 1·2·3상)','#0e8a83'],[13,13,'이전','#e39a12'],[14,15,'최신 동향','#7457d6']];
  let o='';
  for(let i=1;i<=16;i++){const ex=i==8||i==16, mid=i<=6;o+=`<circle cx="${cx(i)}" cy="64" r="${ex?13:10}" fill="${ex?'#e2553a':mid?'#3b6fd8':'#fff'}" stroke="${ex?'#e2553a':mid?'#3b6fd8':'#22305a'}" stroke-width="1.6"/><text x="${cx(i)}" y="68" ${F} font-size="9.5" font-weight="900" fill="${ex||mid?'#fff':'#22305a'}" text-anchor="middle">${i}</text>`;}
  wk.forEach(([i,l1,l2])=>{o+=`<text x="${cx(i)}" y="${l2?90:95}" ${F} font-size="8.6" font-weight="700" fill="#3b6fd8" text-anchor="middle">${l1}</text>`+(l2?`<text x="${cx(i)}" y="101" ${F} font-size="8.6" font-weight="700" fill="#3b6fd8" text-anchor="middle">${l2}</text>`:'');});
  o+=`<text x="${cx(6)}" y="40" ${F} font-size="8.4" font-weight="900" fill="#e2553a" text-anchor="middle">p.33까지</text><line x1="${cx(6)+14}" y1="30" x2="${cx(6)+14}" y2="104" stroke="#e2553a" stroke-width="1.6" stroke-dasharray="4 3"/>`;
  grp.forEach(([a,b,n,c])=>{const x=wx(a)+2,w=wx(b)-wx(a)+28;o+=`<rect x="${x}" y="84" width="${w}" height="20" rx="5" fill="${c}"/><text x="${x+w/2}" y="98" ${F} font-size="${w<60?8:9}" font-weight="700" fill="#fff" text-anchor="middle">${n}</text>`;});
  o+=`<text x="${cx(8)}" y="44" ${F} font-size="10" font-weight="900" fill="#e2553a" text-anchor="middle">중간고사</text><text x="${cx(16)}" y="44" ${F} font-size="10" font-weight="900" fill="#e2553a" text-anchor="middle">기말고사</text>`;
  o+=`<rect x="${wx(1)}" y="6" width="${cx(6)+12-wx(1)}" height="20" rx="10" fill="#e8f0ff"/><text x="${(wx(1)+cx(6)+12)/2}" y="20" ${F} font-size="9.5" font-weight="900" fill="#3b6fd8" text-anchor="middle">중간 범위 = 1~6주차 (6주차 p.33 HTS까지)</text>`;
  o+=`<rect x="${cx(7)-14}" y="6" width="${wx(16)+28-cx(7)+14}" height="20" rx="10" fill="#e2f5f2"/><text x="${(cx(7)-14+wx(16)+28)/2}" y="20" ${F} font-size="9.5" font-weight="900" fill="#0e8a83" text-anchor="middle">기말 범위 = 6주차 p.34~ → 임상 → 기술이전 → 동향</text>`;
  const axis=`<line x1="${cx(1)}" y1="64" x2="${cx(16)}" y2="64" stroke="#22305a" stroke-width="1.2" opacity=".3"/>`;
  return `<svg viewBox="0 0 600 108" width="100%">${axis}${o}</svg>`;
}

function kdrugs(){
  const yr=y=>70+(y-1999)*27;
  const items=[[1999,'1호 선플라주','SK케미칼 · 위암',-1,'#3b6fd8'],[2003,'팩티브정 (5호)','국산 최초 FDA 허가 · 항생제',1,'#e2553a'],[2010,'카나브정 (15호)','보령 · 고혈압',-1,'#0e8a83'],[2012,'제미글로정 (19호)','LG · 당뇨',1,'#0e8a83'],[2016,'올리타정 (27호)','한미 · 표적항암',-1,'#7457d6'],[2018,'케이캡정 (30호)','CJ · 위식도역류',1,'#0e8a83'],[2021,'렉라자정 (31호)','유한 · 폐암',-1,'#7457d6'],[2022,'36호 엔블로정','대웅 · 제2형 당뇨',1,'#3b6fd8']];
  let o=`<line x1="40" y1="80" x2="720" y2="80" stroke="#22305a" stroke-width="2.4"/>`;
  [1999,2005,2010,2015,2020].forEach(y=>o+=`<text x="${yr(y)}" y="${y==1999?96:96}" ${F} font-size="8.5" fill="#8d96aa" text-anchor="middle">${y}</text>`);
  items.forEach(([y,n,d,s,c])=>{const x=yr(y),ty=s<0?24:120;o+=`<line x1="${x}" y1="80" x2="${x}" y2="${s<0?48:108}" stroke="${c}" stroke-width="1.4"/><circle cx="${x}" cy="80" r="5.5" fill="#fff" stroke="${c}" stroke-width="2.4"/><text x="${x}" y="${ty}" ${F} font-size="10.5" font-weight="900" fill="${c}" text-anchor="middle">${n}</text><text x="${x}" y="${ty+13}" ${F} font-size="8.6" fill="#5b6478" text-anchor="middle">${d}</text>`;});
  return `<svg viewBox="0 0 760 142" width="100%">${o}</svg>`;
}
document.querySelectorAll('[data-d]').forEach(el=>{const [fn,arg]=el.dataset.d.split(':');el.innerHTML=window[fn](arg==='blank');});
