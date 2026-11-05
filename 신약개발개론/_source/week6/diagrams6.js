// 6주차 도식
const F = 'font-family="NSKR"';
const T=(x,y,s,o='')=>`<text x="${x}" y="${y}" ${F} ${o}>${s}</text>`;
const AR=`<defs><marker id="a6" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10z" fill="#22305a"/></marker></defs>`;
const L=(x1,y1,x2,y2,c='#22305a',w=1.8,d='')=>`<line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" stroke="${c}" stroke-width="${w}" ${d?`stroke-dasharray="${d}"`:''} marker-end="url(#a6)"/>`;

// 6단계 파이프라인 + 화합물 수 + 효력 기준
function pipe(){
  const s=[['① Target 선정','무엇을 겨냥?','#3b6fd8'],['② Target 검증','바꾸면 병이 바뀌나?','#0e8a83'],['③ Hit 도출','일단 붙는 물질','#e39a12'],['④ Lead 도출','쓸 만한 소수','#e2553a'],['⑤ Lead 최적화','약이 되게 다듬기','#7457d6'],['⑥ 후보물질','전임상으로!','#22305a']];
  let o=AR;const w=128,g=8;
  s.forEach(([a,b,c],i)=>{const x=4+i*(w+g);
    o+=`<path d="M${x},14 L${x+w-12},14 L${x+w},37 L${x+w-12},60 L${x},60 ${i?`L${x+12},37`:''} Z" fill="${c}"/>`;
    o+=T(x+w/2+3,34,a,'font-size="11.5" font-weight="900" fill="#fff" text-anchor="middle"')+T(x+w/2+3,50,b,'font-size="8.8" fill="#fff" text-anchor="middle"');});
  // TPP 표시
  o+=`<rect x="140" y="66" width="120" height="20" rx="10" fill="#e2f5f2" stroke="#0e8a83"/>`+T(200,80,'+ TPP (목표 제품 설계도)','font-size="9" font-weight="900" fill="#0e8a83" text-anchor="middle"');
  // 화합물 수
  const n=[[2,'10⁵~10⁶ 스크리닝'],[3,'10³'],[4,'10¹~10²'],[5,'1']];
  n.forEach(([i,t])=>{const x=4+i*(w+g)+w/2;o+=T(x,80,t,'font-size="9.5" font-weight="900" fill="#5b6478" text-anchor="middle"');});
  // 효력 막대
  const p=[[2,'μM (10~수십 μM)','#e39a12'],[3,'수백 nM','#e2553a'],[5,'< 100 nM','#22305a']];
  o+=T(4,104,'결합 세기 기준','font-size="9.5" font-weight="900" fill="#1d2433"')+T(4,117,'(숫자 ↓ = 강함)','font-size="8.5" fill="#5b6478"');
  p.forEach(([i,t,c])=>{const x=4+i*(w+g)+w/2;o+=`<rect x="${x-56}" y="95" width="112" height="22" rx="11" fill="#fff" stroke="${c}" stroke-width="1.8"/>`+T(x,110,t,`font-size="10" font-weight="900" fill="${c}" text-anchor="middle"`);});
  o+=L(370,123,700,123,'#e2553a',2);o+=T(535,136,'갈수록 개수 ↓ · 결합 세기 ↑ · 검증 in vitro → in vivo','font-size="9" font-weight="700" fill="#e2553a" text-anchor="middle"');
  return `<svg viewBox="0 0 820 140" width="100%">${o}</svg>`;
}

// 광유전학: 켜기(ChR2) vs 끄기(NpHR)
function opto(){
  const cell=(x,title,col,light,lc,ion,dir,res)=>{
    let o=`<rect x="${x}" y="44" width="200" height="16" fill="#f0e6d6" stroke="#c9b48f"/>`+T(x+4,40,'세포 밖','font-size="8.5" fill="#5b6478"')+T(x+4,76,'세포 안','font-size="8.5" fill="#5b6478"');
    o+=`<rect x="${x+82}" y="38" width="36" height="28" rx="6" fill="${col}"/>`+T(x+100,56,title,'font-size="9" font-weight="900" fill="#fff" text-anchor="middle"');
    o+=`<path d="M${x+20},6 l12,8 l-8,3 l12,8" stroke="${lc}" stroke-width="2.5" fill="none"/>`+T(x+40,16,light,`font-size="9.5" font-weight="900" fill="${lc}"`);
    o+=L(x+150,dir>0?20:84,x+150,dir>0?84:22,'#22305a',2)+T(x+160,dir>0?32:30,ion,'font-size="10" font-weight="900" fill="#1d2433"');
    o+=`<rect x="${x}" y="92" width="200" height="24" rx="12" fill="${col}" opacity=".15"/>`+T(x+100,108,res,`font-size="10" font-weight="900" fill="${col}" text-anchor="middle"`);
    return o;};
  return `<svg viewBox="0 0 450 122" width="100%">${AR}
  ${cell(4,'ChR2','#3b6fd8','청색 ~470 nm','#3b6fd8','Na⁺ 등 양이온',1,'탈분극 → 활동전위 = ON')}
  ${cell(244,'NpHR','#b97900','황록 ~580 nm','#c9a400','Cl⁻ (펌프)',1,'과분극 → 발화 억제 = OFF')}
  </svg>`;
}

// Have/Want a compound → one target → validation
function deconv(){
  const b=(x,y,w,t,c,f='#fff')=>`<rect x="${x}" y="${y}" width="${w}" height="30" rx="15" fill="${f}" stroke="${c}" stroke-width="2"/>`+T(x+w/2,y+19,t,`font-size="10" font-weight="900" fill="${c}" text-anchor="middle"`);
  return `<svg viewBox="0 0 604 150" width="100%">${AR}
  ${b(200,4,204,'TARGET IDENTIFICATION','#22305a','#e9ecf5')}
  ${b(2,52,124,'Have a compound','#1f9a5c','#e3f6ec')}${L(126,67,158,67)}${b(162,52,138,'Target deconvolution','#1f9a5c')}
  ${b(478,52,124,'Want a compound','#7457d6','#efeaff')}${L(478,67,446,67)}${b(304,52,138,'Target discovery','#7457d6')}
  ${T(64,98,'효과 먼저 → “뭐에 붙지?”','font-size="9" fill="#13693f" text-anchor="middle"')}${T(540,98,'타겟 먼저 → “뭘로 막지?”','font-size="9" fill="#5a3fb8" text-anchor="middle"')}
  ${L(240,83,276,104)}${L(366,83,330,104)}
  ${b(252,106,100,'ONE TARGET','#e2553a','#fdece7')}
  ${L(352,121,420,121)}${b(424,106,170,'TARGET VALIDATION','#0e8a83','#e2f5f2')}
  ${T(64,122,'= 표현형 기반 (forward)','font-size="9" font-weight="700" fill="#1f9a5c" text-anchor="middle"')}${T(64,138,'예) 아스피린 → COX','font-size="8.5" fill="#5b6478" text-anchor="middle"')}
  ${T(540,146,'= 타겟 기반 (reverse)','font-size="9" font-weight="700" fill="#7457d6" text-anchor="middle"')}
  </svg>`;
}

// Forward vs Reverse chemical genetics
function fr(){
  const col=(x,c,f,h,steps)=>{let o=`<rect x="${x}" y="2" width="262" height="24" rx="8" fill="${c}"/>`+T(x+131,19,h,'font-size="10.5" font-weight="900" fill="#fff" text-anchor="middle"');
    steps.forEach((s,i)=>{const y=34+i*27;o+=`<rect x="${x+16}" y="${y}" width="230" height="21" rx="6" fill="${f}" stroke="${c}" stroke-width="1.3"/>`+T(x+131,y+15,s,'font-size="9.6" font-weight="700" fill="#1d2433" text-anchor="middle"');
      if(i<steps.length-1)o+=`<line x1="${x+131}" y1="${y+21}" x2="${x+131}" y2="${y+27}" stroke="${c}" stroke-width="1.6"/>`;});return o;};
  return `<svg viewBox="0 0 540 166" width="100%">
  ${col(2,'#1f9a5c','#e3f6ec','Phenotype-based = FORWARD',['① 질병 모델 (세포·초파리)','② 표현형 분석 (phenotypic assay)','③ 후보 저분자','④ 타겟 동정 (나중에!)','⑤ 작용기전 연구'])}
  ${col(276,'#b97900','#fff4dc','Target-based = REVERSE',['① 타겟 검증 (단백질 먼저)','② 생화학 분석 (biochemical assay)','③ 후보 저분자 (단백질 결합)','④ 세포·동물 모델에서 확인','⑤ (효과 없을 수도…)'])}
  </svg>`;
}

// APP 절단 경로
function app(){
  const b=(x,y,w,t,c,f='#fff')=>`<rect x="${x}" y="${y}" width="${w}" height="28" rx="7" fill="${f}" stroke="${c}" stroke-width="1.8"/>`+T(x+w/2,y+18,t,`font-size="10" font-weight="900" fill="${c}" text-anchor="middle"`);
  return `<svg viewBox="0 0 560 128" width="100%">${AR}
  ${b(2,46,60,'APP','#22305a','#e9ecf5')}
  ${L(62,52,126,24)}${T(64,12,'β-세크레타제','font-size="9" font-weight="900" fill="#e2553a"')}${T(64,24,'(BACE1)','font-size="8.5" fill="#e2553a"')}
  ${b(130,10,70,'C99','#e2553a')}${L(200,24,262,24)}${T(231,16,'γ-세크레타제','font-size="9" font-weight="900" fill="#e2553a" text-anchor="middle"')}
  ${b(266,10,54,'Aβ','#e2553a','#fdece7')}${L(320,24,370,24)}${b(374,10,182,'올리고머 → 플라크 (세포 밖)','#e2553a','#fdece7')}
  ${L(62,74,126,96,'#1f9a5c')}${T(64,122,'α-세크레타제','font-size="9" font-weight="900" fill="#1f9a5c"')}
  ${b(130,86,70,'C83','#1f9a5c')}${L(200,100,262,100,'#1f9a5c')}${b(266,86,54,'P3','#1f9a5c','#e3f6ec')}${T(330,104,'비아밀로이드 경로 (Aβ ✗)','font-size="9.5" font-weight="700" fill="#13693f"')}
  ${T(374,58,'약물 공략 지점','font-size="9.5" font-weight="900" fill="#1d2433"')}
  ${T(374,73,'BACE1 저해제 → 임상 실패','font-size="9" fill="#5b6478"')}
  ${T(374,86,'γ 저해제 → Notch 부작용 실패','font-size="9" fill="#5b6478"')}
  </svg>`;
}

// TPP: Essential vs Ideal
function tpp(){
  const r=[['효능 (반응률)',40,70,'%','↑'],['안전성 (이상반응)',20,5,'%','↓'],['투여 간격',1,30,'일','↑']];
  let o='';
  r.forEach(([n,e,i,u,d],k)=>{const y=8+k*34;
    o+=T(0,y+16,n,'font-size="10" font-weight="900" fill="#1d2433"');
    o+=`<rect x="118" y="${y+3}" width="150" height="20" rx="10" fill="#fff4dc" stroke="#e39a12" stroke-width="1.6"/>`+T(193,y+17,`Essential ${k==2?'매일':(k==1?'≤ ':'≥ ')+e+u}`,'font-size="9.5" font-weight="900" fill="#b97900" text-anchor="middle"');
    o+=`<line x1="270" y1="${y+13}" x2="296" y2="${y+13}" stroke="#22305a" stroke-width="1.8" marker-end="url(#a6)"/>`;
    o+=`<rect x="300" y="${y+3}" width="150" height="20" rx="10" fill="#e2f5f2" stroke="#0e8a83" stroke-width="1.6"/>`+T(375,y+17,`Ideal ${k==2?'매월':(k==1?'≤ ':'≥ ')+i+u}`,'font-size="9.5" font-weight="900" fill="#0e8a83" text-anchor="middle"');});
  o+=T(193,112,'최소 기준 = go / no-go','font-size="9" fill="#b97900" text-anchor="middle"')+T(375,112,'경쟁 우위 = 시장 최고','font-size="9" fill="#0e8a83" text-anchor="middle"');
  return `<svg viewBox="0 0 456 118" width="100%">${AR}${o}</svg>`;
}

document.querySelectorAll('[data-d]').forEach(el=>{el.innerHTML=window[el.dataset.d]();});
