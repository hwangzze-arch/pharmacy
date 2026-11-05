# -*- coding: utf-8 -*-
"""직접 그린 그림(SVG)"""

GP = "#0e8a6a"
VR = "#5847d6"
INK = "#1d2330"
MU = "#5d6678"

# 1. 그람양성 vs 그람음성 vs 마이코플라스마 세포벽
CELLWALL = f'''<svg viewBox="0 0 520 230" xmlns="http://www.w3.org/2000/svg">
<g font-size="13">
 <text x="85" y="18" text-anchor="middle" font-weight="800" fill="{GP}">그람양성균</text>
 <text x="260" y="18" text-anchor="middle" font-weight="800" fill="#c0392b">그람음성균</text>
 <text x="435" y="18" text-anchor="middle" font-weight="800" fill="#a66300">마이코플라스마</text>
 <!-- G+ -->
 <rect x="20" y="40" width="130" height="58" rx="4" fill="#8e5cc7"/>
 <text x="85" y="74" text-anchor="middle" fill="#fff" font-weight="700">두꺼운 펩티도글리칸</text>
 <rect x="20" y="100" width="130" height="16" rx="3" fill="#f2c94c"/>
 <text x="85" y="112" text-anchor="middle" font-size="11">세포막</text>
 <!-- G- -->
 <rect x="195" y="40" width="130" height="18" rx="3" fill="#f28c8c"/>
 <text x="260" y="53" text-anchor="middle" font-size="11">외막(LPS)</text>
 <rect x="195" y="62" width="130" height="12" rx="3" fill="#e7a4c9"/>
 <text x="260" y="72" text-anchor="middle" font-size="10">얇은 펩티도글리칸</text>
 <rect x="195" y="100" width="130" height="16" rx="3" fill="#f2c94c"/>
 <text x="260" y="112" text-anchor="middle" font-size="11">세포막</text>
 <!-- Myco -->
 <rect x="370" y="100" width="130" height="16" rx="3" fill="#f2c94c"/>
 <text x="435" y="112" text-anchor="middle" font-size="11">세포막만!</text>
 <text x="435" y="70" text-anchor="middle" font-size="12" fill="#a66300">세포벽 없음</text>
</g>
<g font-size="12.5" fill="{INK}">
 <circle cx="85" cy="160" r="22" fill="#8e5cc7"/><text x="85" y="196" text-anchor="middle">보라색으로 염색</text>
 <circle cx="260" cy="160" r="22" fill="#f28c8c"/><text x="260" y="196" text-anchor="middle">분홍색으로 염색</text>
 <path d="M415 150 q20 -25 40 0 q15 25 -10 30 q-30 8 -30 -30z" fill="#f6d27a"/><text x="435" y="196" text-anchor="middle">모양이 제멋대로(다형성)</text>
 <text x="435" y="214" text-anchor="middle" font-size="11.5" fill="#c0392b">페니실린(β-락탐) 안 들음</text>
 <text x="85" y="214" text-anchor="middle" font-size="11.5" fill="{MU}">벽 두께가 염료를 붙잡음</text>
 <text x="260" y="214" text-anchor="middle" font-size="11.5" fill="{MU}">알코올에 염료가 씻겨나감</text>
</g></svg>'''

# 2. 그람양성균 분류 지도
GP_TREE = f'''<svg viewBox="0 0 900 300" xmlns="http://www.w3.org/2000/svg" font-size="13">
<defs><style>.bx{{fill:#fff;stroke:{GP};stroke-width:1.6}} .h{{font-weight:800}} .s{{font-size:11.5px;fill:{MU}}}</style></defs>
<rect x="340" y="6" width="220" height="34" rx="8" fill="{GP}"/>
<text x="450" y="28" text-anchor="middle" fill="#fff" font-weight="800" font-size="15">그람양성균</text>
<path d="M450 40 V58 M150 58 H750 M150 58 V72 M450 58 V72 M750 58 V72" stroke="{GP}" stroke-width="1.6" fill="none"/>
<rect class="bx" x="40" y="72" width="220" height="44" rx="8"/>
<text x="150" y="91" text-anchor="middle" class="h">문 Bacillota</text><text x="150" y="108" text-anchor="middle" class="s">(옛 이름 Firmicutes · 저 G+C)</text>
<rect class="bx" x="340" y="72" width="220" height="44" rx="8"/>
<text x="450" y="91" text-anchor="middle" class="h">문 Mycoplasmatota</text><text x="450" y="108" text-anchor="middle" class="s">(세포벽 없는 강 Mollicutes)</text>
<rect class="bx" x="640" y="72" width="220" height="44" rx="8"/>
<text x="750" y="91" text-anchor="middle" class="h">문 Actinomycetota</text><text x="750" y="108" text-anchor="middle" class="s">(옛 Actinobacteria · 고 G+C)</text>
<path d="M150 116 V130 M85 130 H215 M85 130 V140 M215 130 V140" stroke="{GP}" stroke-width="1.4" fill="none"/>
<path d="M450 116 V140" stroke="{GP}" stroke-width="1.4"/>
<path d="M750 116 V140" stroke="{GP}" stroke-width="1.4"/>
<rect x="20" y="140" width="130" height="150" rx="8" fill="#e7f5f0"/>
<text x="85" y="158" text-anchor="middle" class="h">강 Clostridia</text>
<text x="85" y="176" text-anchor="middle" font-style="italic">Clostridium</text>
<text x="85" y="196" text-anchor="middle" class="s">botulinum</text><text x="85" y="212" text-anchor="middle" class="s">tetani</text>
<text x="85" y="228" text-anchor="middle" class="s">difficile</text><text x="85" y="244" text-anchor="middle" class="s">perfringens</text>
<text x="85" y="260" text-anchor="middle" class="s">sordellii</text>
<text x="85" y="280" text-anchor="middle" font-size="11" fill="#c0392b">절대혐기 · 내생포자</text>
<rect x="160" y="140" width="120" height="150" rx="8" fill="#e7f5f0"/>
<text x="220" y="158" text-anchor="middle" class="h">강 Negativicutes</text>
<text x="220" y="180" text-anchor="middle" font-style="italic">Veillonella</text>
<text x="220" y="200" text-anchor="middle" class="s">입 안 정상균</text>
<text x="220" y="216" text-anchor="middle" class="s">젖산 → 프로피온산</text>
<text x="220" y="232" text-anchor="middle" class="s">충치 · 치석 · 치주염</text>
<rect x="340" y="140" width="220" height="150" rx="8" fill="#e7f5f0"/>
<text x="450" y="158" text-anchor="middle" class="h">목 Mycoplasmatales</text>
<text x="450" y="182" text-anchor="middle" font-style="italic">Mycoplasma</text>
<text x="450" y="200" text-anchor="middle" class="s">pneumoniae → 이형(걷는) 폐렴</text>
<text x="450" y="216" text-anchor="middle" class="s">genitalium · hominis → 성병/생식기</text>
<text x="450" y="242" text-anchor="middle" font-style="italic">Ureaplasma</text>
<text x="450" y="260" text-anchor="middle" class="s">urealyticum → 비임균성 요도염</text>
<text x="450" y="280" text-anchor="middle" font-size="11" fill="#c0392b">세포벽 X · 가장 작은 세균</text>
<rect x="590" y="140" width="300" height="150" rx="8" fill="#e7f5f0"/>
<text x="740" y="158" text-anchor="middle" class="h">강 Actinomycetia</text>
<g class="s" font-size="11.5">
<text x="600" y="180"><tspan font-style="italic" fill="{INK}">Actinomyces</tspan> 방선균증</text>
<text x="600" y="198"><tspan font-style="italic" fill="{INK}">Corynebacterium</tspan> 디프테리아</text>
<text x="600" y="216"><tspan font-style="italic" fill="{INK}">Mycobacterium</tspan> 결핵·한센병</text>
<text x="600" y="234"><tspan font-style="italic" fill="{INK}">Nocardia</tspan> 노카르디아증</text>
<text x="752" y="180"><tspan font-style="italic" fill="{INK}">Propionibacterium</tspan> 여드름</text>
<text x="752" y="198"><tspan font-style="italic" fill="{INK}">Micromonospora</tspan> 겐타마이신</text>
<text x="752" y="216"><tspan font-style="italic" fill="{INK}">Streptomyces</tspan> 스트렙토마이신</text>
<text x="752" y="234"><tspan font-style="italic" fill="{INK}">Bifidobacterium</tspan> 유산균</text>
</g>
<text x="740" y="270" text-anchor="middle" font-size="11" fill="#c0392b">곰팡이처럼 실(균사) · 무성포자 · 항생제 공장</text>
</svg>'''

# 3. 보툴리눔 vs 파상풍 신경독소
NEUROTOX = f'''<svg viewBox="0 0 560 250" xmlns="http://www.w3.org/2000/svg" font-size="12.5">
<rect x="5" y="5" width="265" height="240" rx="10" fill="#eef6ff"/>
<rect x="290" y="5" width="265" height="240" rx="10" fill="#fff1ef"/>
<text x="137" y="28" text-anchor="middle" font-weight="800" fill="#1f5fa8">보툴리눔 독소 (C. botulinum)</text>
<text x="422" y="28" text-anchor="middle" font-weight="800" fill="#c0392b">파상풍 독소 (C. tetani)</text>
<!-- botulinum -->
<circle cx="60" cy="90" r="20" fill="#8fb8e8"/><text x="60" y="94" text-anchor="middle" font-size="11">운동신경</text>
<path d="M80 90 H170" stroke="#4a7fc1" stroke-width="5"/>
<rect x="175" y="65" width="70" height="50" rx="10" fill="#f6c1c1"/><text x="210" y="94" text-anchor="middle">근육</text>
<text x="128" y="78" text-anchor="middle" font-size="11">아세틸콜린 ✕</text>
<path d="M118 100 l20 -20 M118 80 l20 20" stroke="#c0392b" stroke-width="3"/>
<text x="137" y="145" text-anchor="middle">"움직여!" 신호가 근육에 못 감</text>
<text x="137" y="175" text-anchor="middle" font-weight="800" font-size="15" fill="#1f5fa8">축 늘어지는 마비</text>
<text x="137" y="198" text-anchor="middle" fill="{MU}" font-size="11.5">눈→얼굴→목→팔→호흡근 (위→아래)</text>
<text x="137" y="218" text-anchor="middle" fill="{MU}" font-size="11.5">통조림·꿀(영아)·상처</text>
<!-- tetanus -->
<circle cx="345" cy="70" r="18" fill="#f2b8a8"/><text x="345" y="74" text-anchor="middle" font-size="10">억제신경</text>
<circle cx="345" cy="120" r="18" fill="#e8a090"/><text x="345" y="124" text-anchor="middle" font-size="10">운동신경</text>
<path d="M345 88 V102" stroke="#999" stroke-width="3"/>
<text x="400" y="80" font-size="11">GABA·글리신 ✕</text>
<path d="M363 120 H460" stroke="#d35d4a" stroke-width="5"/>
<rect x="465" y="95" width="70" height="50" rx="10" fill="#f6c1c1"/><text x="500" y="124" text-anchor="middle">근육</text>
<text x="422" y="160" text-anchor="middle">"그만!" 브레이크가 고장 → 계속 수축</text>
<text x="422" y="187" text-anchor="middle" font-weight="800" font-size="15" fill="#c0392b">뻣뻣한 경련(강직)</text>
<text x="422" y="210" text-anchor="middle" fill="{MU}" font-size="11.5">입이 안 벌어짐 · 활처럼 휜 등</text>
<text x="422" y="230" text-anchor="middle" fill="{MU}" font-size="11.5">녹슨 못 등 깊은 상처</text>
</svg>'''

# 4. 위막성 대장염 기전
CDIFF = f'''<svg viewBox="0 0 560 150" xmlns="http://www.w3.org/2000/svg" font-size="12">
<g>
<rect x="5" y="20" width="150" height="90" rx="12" fill="#e7f5f0"/>
<text x="80" y="14" text-anchor="middle" font-weight="800">① 평소 장</text>
<g fill="#38a169">{''.join(f'<circle cx="{25+ (i%6)*22}" cy="{40+(i//6)*22}" r="7"/>' for i in range(18))}</g>
<circle cx="135" cy="95" r="6" fill="#d35d4a"/>
<text x="80" y="128" text-anchor="middle" fill="{MU}" font-size="11">정상균이 C.diff(빨강)를 눌러 둠</text>
<path d="M162 65 H200" stroke="{INK}" stroke-width="2" marker-end="url(#a)"/>
<text x="181" y="55" text-anchor="middle" font-size="11">항생제</text><text x="181" y="85" text-anchor="middle" font-size="10" fill="{MU}">clindamycin</text>
<rect x="205" y="20" width="150" height="90" rx="12" fill="#f4f4f4"/>
<text x="280" y="14" text-anchor="middle" font-weight="800">② 정상균 전멸</text>
<g fill="#bbb">{''.join(f'<circle cx="{225+(i%6)*22}" cy="{40+(i//6)*22}" r="4"/>' for i in range(18))}</g>
<circle cx="335" cy="95" r="6" fill="#d35d4a"/>
<text x="280" y="128" text-anchor="middle" fill="{MU}" font-size="11">C.diff는 내성 → 살아남음</text>
<path d="M362 65 H400" stroke="{INK}" stroke-width="2" marker-end="url(#a)"/>
<rect x="405" y="20" width="150" height="90" rx="12" fill="#fdecea"/>
<text x="480" y="14" text-anchor="middle" font-weight="800">③ C.diff 폭증</text>
<g fill="#d35d4a">{''.join(f'<circle cx="{425+(i%6)*22}" cy="{40+(i//6)*22}" r="7"/>' for i in range(18))}</g>
<text x="480" y="128" text-anchor="middle" fill="#c0392b" font-size="11">독소 A·B → 위막성 대장염</text>
</g>
<defs><marker id="a" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8z" fill="{INK}"/></marker></defs>
</svg>'''

# 5. 바이러스 구조
VSTRUCT = f'''<svg viewBox="0 0 560 230" xmlns="http://www.w3.org/2000/svg" font-size="12.5">
<!-- naked -->
<text x="120" y="18" text-anchor="middle" font-weight="800">외피 없는 바이러스 (naked)</text>
<polygon points="120,40 175,72 175,136 120,168 65,136 65,72" fill="#d9d4fb" stroke="{VR}" stroke-width="2"/>
<g fill="#8f82ea">{''.join(f'<circle cx="{120+ 48*__import__("math").cos(i*0.5236)}" cy="{104+48*__import__("math").sin(i*0.5236)}" r="7"/>' for i in range(12))}</g>
<path d="M95 100 q12 -20 25 0 t25 0" stroke="#d35d4a" stroke-width="3" fill="none"/>
<text x="120" y="190" text-anchor="middle" fill="{MU}" font-size="11.5">핵산 + 캡시드 = 뉴클레오캡시드</text>
<text x="120" y="208" text-anchor="middle" fill="#1b7f47" font-size="11.5" font-weight="700">튼튼함: 알코올·산·담즙에 강함</text>
<!-- enveloped -->
<text x="420" y="18" text-anchor="middle" font-weight="800">외피 있는 바이러스 (enveloped)</text>
<circle cx="420" cy="104" r="70" fill="#fff4d6" stroke="#e0a526" stroke-width="5"/>
<g stroke="#e0a526" stroke-width="3">{''.join(f'<line x1="{420+72*__import__("math").cos(i*0.4488)}" y1="{104+72*__import__("math").sin(i*0.4488)}" x2="{420+84*__import__("math").cos(i*0.4488)}" y2="{104+84*__import__("math").sin(i*0.4488)}"/>' for i in range(14))}</g>
<polygon points="420,62 456,83 456,125 420,146 384,125 384,83" fill="#d9d4fb" stroke="{VR}" stroke-width="2"/>
<path d="M398 100 q11 -18 22 0 t22 0" stroke="#d35d4a" stroke-width="3" fill="none"/>
<text x="420" y="208" text-anchor="middle" fill="#c0392b" font-size="11.5" font-weight="700">약함: 에테르·세제·건조·열에 쉽게 파괴</text>
<text x="420" y="226" text-anchor="middle" fill="{MU}" font-size="11">외피 = 숙주 세포막을 빌려 입은 옷</text>
<!-- labels -->
<g font-size="11.5">
<line x1="160" y1="150" x2="230" y2="178" stroke="{MU}"/><text x="232" y="182">캡시드(단백질 껍질)</text>
<line x1="127" y1="57" x2="230" y2="40" stroke="{MU}"/><text x="232" y="44">캡소미어(벽돌)</text>
<line x1="140" y1="100" x2="230" y2="100" stroke="{MU}"/><text x="232" y="104">핵산(DNA or RNA)</text>
<line x1="495" y1="40" x2="520" y2="34" stroke="{MU}"/><text x="500" y="30">당단백 돌기</text>
</g>
</svg>'''

# 6. 생활사 5단계
LIFECYCLE = f'''<svg viewBox="0 0 600 120" xmlns="http://www.w3.org/2000/svg" font-size="12.5">
<defs><marker id="b" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8z" fill="{VR}"/></marker></defs>
{''.join(f"""<g><circle cx="{60+i*120}" cy="45" r="32" fill="{['#efedfd','#e3dffc','#d6d0fa','#c8c0f7','#b9aff4'][i]}" stroke="{VR}" stroke-width="1.5"/>
<text x="{60+i*120}" y="40" text-anchor="middle" font-weight="900" fill="{VR}" font-size="16">{i+1}</text>
<text x="{60+i*120}" y="58" text-anchor="middle" font-weight="700" font-size="11.5">{n}</text>
<text x="{60+i*120}" y="98" text-anchor="middle" font-size="11" fill="{MU}">{d}</text>
<text x="{60+i*120}" y="112" text-anchor="middle" font-size="11" fill="{MU}">{d2}</text></g>""" for i,(n,d,d2) in enumerate([('부착','수용체에 착 달라붙기','(열쇠-자물쇠)'),('침입·탈각','세포 안으로 들어가','껍질 벗기'),('복제·합성','숙주 공장으로','핵산·단백질 복사'),('조립·성숙','부품 끼워','새 바이러스 완성'),('방출','세포 밖으로','다음 세포 감염')]))}
{''.join(f'<path d="M{94+i*120} 45 H{124+i*120}" stroke="{VR}" stroke-width="2" marker-end="url(#b)"/>' for i in range(4))}
</svg>'''

# 7. 볼티모어 분류
BALTIMORE = f'''<svg viewBox="0 0 640 270" xmlns="http://www.w3.org/2000/svg" font-size="12.5">
<defs><marker id="c" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8z" fill="{INK}"/></marker></defs>
<rect x="250" y="112" width="140" height="44" rx="22" fill="{VR}"/>
<text x="320" y="132" text-anchor="middle" fill="#fff" font-weight="800" font-size="15">(+) mRNA</text>
<text x="320" y="149" text-anchor="middle" fill="#e9e5ff" font-size="11">→ 단백질 (모두 여기로!)</text>
{''.join(f"""<g><rect x="{x}" y="{y}" width="170" height="54" rx="9" fill="#fff" stroke="{c}" stroke-width="2"/>
<text x="{x+10}" y="{y+20}" font-weight="900" fill="{c}">{g}</text>
<text x="{x+38}" y="{y+20}" font-weight="700">{t}</text>
<text x="{x+10}" y="{y+40}" font-size="11" fill="{MU}">{ex}</text>
<path d="M{ax1} {ay1} L{ax2} {ay2}" stroke="{INK}" stroke-width="1.5" marker-end="url(#c)"/></g>""" for (x,y,g,t,ex,c,ax1,ay1,ax2,ay2) in [
 (10,8,'I','dsDNA','폭스·헤르페스·아데노·파포바','#3b6fd8',180,40,265,112),
 (235,8,'II','ssDNA','파보','#3b6fd8',320,62,320,110),
 (460,8,'III','dsRNA','레오(로타)','#d4762c',460,40,375,112),
 (10,206,'IV','(+)ssRNA','코로나·피코르나·플라비·토가','#1b9e5a',180,226,265,156),
 (235,206,'V','(−)ssRNA','파라믹소·랍도·번야·오르토믹소','#d4762c',320,206,320,158),
 (460,206,'VI','ssRNA-RT','레트로(HIV·HTLV)','#c0392b',460,226,375,156),
])}
<rect x="10" y="100" width="170" height="54" rx="9" fill="#fff" stroke="#c0392b" stroke-width="2"/>
<text x="20" y="120" font-weight="900" fill="#c0392b">VII</text><text x="52" y="120" font-weight="700">dsDNA-RT</text>
<text x="20" y="140" font-size="11" fill="{MU}">헤파드나(B형 간염)</text>
<path d="M180 128 L248 132" stroke="{INK}" stroke-width="1.5" marker-end="url(#c)"/>
<text x="560" y="128" text-anchor="middle" font-size="11" fill="{MU}">RT = 역전사</text>
<text x="560" y="144" text-anchor="middle" font-size="11" fill="{MU}">(RNA→DNA)</text>
</svg>'''

# 8. 레트로바이러스 복제 + 약물 표적
RETRO = f'''<svg viewBox="0 0 640 200" xmlns="http://www.w3.org/2000/svg" font-size="12">
<defs><marker id="d" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8z" fill="{INK}"/></marker></defs>
{''.join(f"""<g><rect x="{x}" y="60" width="{w}" height="44" rx="8" fill="{f}" stroke="{s}" stroke-width="1.5"/>
<text x="{x+w/2}" y="80" text-anchor="middle" font-weight="800">{t}</text>
<text x="{x+w/2}" y="96" text-anchor="middle" font-size="10.5" fill="{MU}">{sub}</text></g>""" for (x,w,t,sub,f,s) in [
 (5,95,'① 부착·융합','CD4 + CCR5/CXCR4','#efedfd',VR),
 (122,95,'② 역전사','RNA → DNA','#fff1d6','#d4762c'),
 (239,95,'③ 통합','숙주 DNA에 끼움','#fde3e1','#c0392b'),
 (356,95,'④ 전사·번역','= provirus 상태','#e7f5f0',GP),
 (473,75,'⑤ 절단','gag·pol 자르기','#efedfd',VR),
 (566,70,'⑥ 출아','새 HIV','#efedfd',VR)])}
{''.join(f'<path d="M{a} 82 H{b}" stroke="{INK}" stroke-width="1.5" marker-end="url(#d)"/>' for a,b in [(100,120),(217,237),(334,354),(451,471),(548,564)])}
<g font-size="11" font-weight="700">
<rect x="5" y="128" width="95" height="40" rx="6" fill="#f3f0ff"/><text x="52" y="144" text-anchor="middle" fill="{VR}">융합·진입 억제제</text><text x="52" y="160" text-anchor="middle" font-weight="400">enfuvirtide 등</text>
<rect x="122" y="128" width="95" height="56" rx="6" fill="#fff4e0"/><text x="169" y="144" text-anchor="middle" fill="#b05f00">NRTI</text><text x="169" y="158" text-anchor="middle" font-weight="400">AZT(zidovudine)</text><text x="169" y="174" text-anchor="middle" fill="#b05f00">NNRTI: nevirapine…</text>
<rect x="239" y="128" width="95" height="40" rx="6" fill="#fdeceb"/><text x="286" y="144" text-anchor="middle" fill="#c0392b">통합효소 억제제</text><text x="286" y="160" text-anchor="middle" font-weight="400">raltegravir</text>
<rect x="473" y="128" width="75" height="40" rx="6" fill="#f3f0ff"/><text x="510" y="144" text-anchor="middle" fill="{VR}">PI(-navir)</text><text x="510" y="160" text-anchor="middle" font-weight="400">saquinavir…</text>
</g>
<text x="320" y="24" text-anchor="middle" font-weight="800" font-size="14">레트로바이러스(HIV) 한 바퀴 + 약이 막는 곳</text>
<text x="320" y="44" text-anchor="middle" fill="{MU}" font-size="11">"retro = 거꾸로": 보통은 DNA→RNA인데, 이들은 RNA→DNA (역전사효소 = RNA 의존 DNA 중합효소)</text>
</svg>'''

# 9. 헤르페스 잠복 장소
HERPES = f'''<svg viewBox="0 0 330 250" xmlns="http://www.w3.org/2000/svg" font-size="12">
<circle cx="110" cy="40" r="26" fill="#f6e3d3" stroke="#c9a68a"/>
<rect x="88" y="66" width="44" height="90" rx="18" fill="#f6e3d3" stroke="#c9a68a"/>
<rect x="88" y="150" width="18" height="80" rx="8" fill="#f6e3d3" stroke="#c9a68a"/>
<rect x="114" y="150" width="18" height="80" rx="8" fill="#f6e3d3" stroke="#c9a68a"/>
<circle cx="128" cy="42" r="7" fill="#d35d4a"/>
<path d="M135 42 H175" stroke="#d35d4a" stroke-width="1.5"/>
<text x="178" y="38" font-weight="800" fill="#c0392b">HSV-1 → 3차 신경절</text><text x="178" y="54" fill="{MU}" font-size="11">입술 물집(구순포진)</text>
<circle cx="110" cy="105" r="6" fill="#d4762c"/><circle cx="110" cy="120" r="6" fill="#d4762c"/>
<path d="M117 112 H175" stroke="#d4762c" stroke-width="1.5"/>
<text x="178" y="108" font-weight="800" fill="#b05f00">VZV → 척수 후근 신경절</text><text x="178" y="124" fill="{MU}" font-size="11">수두 → 나중에 대상포진</text>
<circle cx="110" cy="150" r="7" fill="{VR}"/>
<path d="M117 150 H175 V172" stroke="{VR}" stroke-width="1.5" fill="none"/>
<text x="178" y="168" font-weight="800" fill="{VR}">HSV-2 → 엉치(천골) 신경절</text><text x="178" y="184" fill="{MU}" font-size="11">생식기 포진</text>
<text x="165" y="222" text-anchor="middle" font-size="11.5" font-weight="700">신경 속에 "숨어 자다가"(잠복) 면역↓ 때 깨어남(재활성화)</text>
<text x="165" y="240" text-anchor="middle" font-size="11" fill="{MU}">CMV·EBV는 백혈구(단핵구·림프구)에 잠복</text>
</svg>'''

# 10. 아시클로버 활성화
ACV = f'''<svg viewBox="0 0 600 120" xmlns="http://www.w3.org/2000/svg" font-size="12">
<defs><marker id="e" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8z" fill="{INK}"/></marker></defs>
<rect x="5" y="30" width="110" height="44" rx="8" fill="#f4f4f4" stroke="#999"/><text x="60" y="50" text-anchor="middle" font-weight="800">Acyclovir</text><text x="60" y="66" text-anchor="middle" font-size="10.5" fill="{MU}">구아노신 짝퉁(비활성)</text>
<path d="M115 52 H185" stroke="{INK}" stroke-width="1.6" marker-end="url(#e)"/>
<text x="150" y="40" text-anchor="middle" font-weight="800" fill="#c0392b" font-size="11">바이러스 TK</text><text x="150" y="70" text-anchor="middle" font-size="10" fill="{MU}">(감염세포에만!)</text>
<rect x="188" y="30" width="100" height="44" rx="8" fill="#fff4e0" stroke="#d4762c"/><text x="238" y="57" text-anchor="middle" font-weight="800">ACV-인산1</text>
<path d="M288 52 H350" stroke="{INK}" stroke-width="1.6" marker-end="url(#e)"/>
<text x="319" y="40" text-anchor="middle" font-size="10.5">숙주 효소</text>
<rect x="353" y="30" width="100" height="44" rx="8" fill="#fde3e1" stroke="#c0392b"/><text x="403" y="57" text-anchor="middle" font-weight="800">ACV-인산3</text>
<path d="M453 52 H500" stroke="{INK}" stroke-width="1.6" marker-end="url(#e)"/>
<rect x="503" y="22" width="92" height="60" rx="8" fill="#efedfd" stroke="{VR}"/><text x="549" y="44" text-anchor="middle" font-weight="800" fill="{VR}">바이러스</text><text x="549" y="60" text-anchor="middle" font-weight="800" fill="{VR}">DNA 중합효소</text><text x="549" y="76" text-anchor="middle" font-size="10.5">✕ 사슬 끊김</text>
<text x="300" y="108" text-anchor="middle" font-size="11.5" fill="{MU}">→ 감염 안 된 정상세포에선 거의 활성화 안 됨 = 부작용 적음 (헤르페스 계열에 잘 듦)</text>
</svg>'''

# 11. 인플루엔자: 입자 + 약물 + 변이
FLU = f'''<svg viewBox="0 0 600 220" xmlns="http://www.w3.org/2000/svg" font-size="12">
<circle cx="100" cy="100" r="62" fill="#fff4d6" stroke="#e0a526" stroke-width="4"/>
{''.join(f'<rect x="{100+64*__import__("math").cos(a)-3}" y="{100+64*__import__("math").sin(a)-3}" width="7" height="7" fill="#3b6fd8" transform="rotate(0)"/>' for a in [i*0.785 for i in range(0,8)])}
{''.join(f'<circle cx="{100+68*__import__("math").cos(a)}" cy="{100+68*__import__("math").sin(a)}" r="5" fill="#d35d4a"/>' for a in [i*0.785+0.39 for i in range(0,8)])}
{''.join(f'<path d="M{70+i*9} {85+ (i%2)*10} q4 -8 8 0" stroke="{VR}" stroke-width="2.5" fill="none"/>' for i in range(8))}
<text x="100" y="135" text-anchor="middle" font-size="10.5" fill="{MU}">(−)RNA 8조각</text>
<rect x="96" y="96" width="8" height="8" fill="#2ca58d"/>
<g font-size="11.5">
<rect x="185" y="20" width="12" height="12" fill="#3b6fd8"/><text x="202" y="31"><tspan font-weight="800">HA</tspan> 헤마글루티닌: 세포에 달라붙는 손</text>
<rect x="185" y="44" width="12" height="12" rx="6" fill="#d35d4a"/><text x="202" y="55"><tspan font-weight="800">NA</tspan> 뉴라미니다아제: 다 만든 뒤 떨어져 나가는 가위</text>
<text x="202" y="72" fill="#c0392b" font-weight="700">  ↳ oseltamivir(타미플루)·zanamivir가 막음</text>
<rect x="185" y="86" width="12" height="12" fill="#2ca58d"/><text x="202" y="97"><tspan font-weight="800">M2</tspan> 이온 통로: 껍질 벗기기(탈각)</text>
<text x="202" y="114" fill="#c0392b" font-weight="700">  ↳ amantadine·rimantadine이 막음</text>
</g>
<rect x="185" y="128" width="200" height="84" rx="8" fill="#efedfd"/>
<text x="285" y="146" text-anchor="middle" font-weight="800" fill="{VR}">항원 소변이 (drift)</text>
<text x="285" y="164" text-anchor="middle" font-size="11">점돌연변이가 조금씩 쌓임</text>
<text x="285" y="180" text-anchor="middle" font-size="11">→ 매년 독감(계절 유행)</text>
<text x="285" y="198" text-anchor="middle" font-size="11" fill="{MU}">그래서 백신을 매년 맞음</text>
<rect x="395" y="128" width="200" height="84" rx="8" fill="#fdeceb"/>
<text x="495" y="146" text-anchor="middle" font-weight="800" fill="#c0392b">항원 대변이 (shift)</text>
<text x="495" y="164" text-anchor="middle" font-size="11">두 바이러스의 RNA 조각이 섞임</text>
<text x="495" y="180" text-anchor="middle" font-size="11">(돼지 몸속에서 사람+조류형)</text>
<text x="495" y="198" text-anchor="middle" font-size="11" font-weight="700" fill="#c0392b">→ 완전 신종 → 대유행(팬데믹)</text>
<text x="100" y="196" text-anchor="middle" font-size="11" fill="{MU}">A형: H18 × N11 조합</text>
<text x="100" y="212" text-anchor="middle" font-size="11" fill="{MU}">예) H1N1, H3N2, H5N1</text>
</svg>'''

# 12. 크기 비교
SIZE = f'''<svg viewBox="0 0 560 120" xmlns="http://www.w3.org/2000/svg" font-size="11.5">
<line x1="20" y1="80" x2="540" y2="80" stroke="#ccc"/>
<circle cx="60" cy="80" r="3" fill="{VR}"/><text x="60" y="104" text-anchor="middle">폴리오·파보</text><text x="60" y="117" text-anchor="middle" fill="{MU}">20~30 nm</text>
<circle cx="150" cy="80" r="6" fill="{VR}"/><text x="150" y="104" text-anchor="middle">아데노</text><text x="150" y="117" text-anchor="middle" fill="{MU}">90~100 nm</text>
<circle cx="240" cy="80" r="9" fill="{VR}"/><text x="240" y="104" text-anchor="middle">HIV·헤르페스</text><text x="240" y="117" text-anchor="middle" fill="{MU}">~100 nm</text>
<rect x="315" y="66" width="34" height="26" rx="8" fill="{VR}"/><text x="332" y="104" text-anchor="middle">천연두(폭스)</text><text x="332" y="117" text-anchor="middle" fill="{MU}">200~400 nm</text>
<rect x="400" y="40" width="130" height="58" rx="28" fill="{GP}" opacity=".85"/><text x="465" y="74" text-anchor="middle" fill="#fff" font-weight="700">세균 1,000~5,000 nm</text>
<text x="280" y="20" text-anchor="middle" font-weight="800">광학현미경 한계 ≈ 200 nm → 바이러스는 대부분 전자현미경으로만 보임</text>
</svg>'''

# 13. 간염 바이러스 비교 그림(입/피)
HEP = f'''<svg viewBox="0 0 520 110" xmlns="http://www.w3.org/2000/svg" font-size="13">
<rect x="5" y="10" width="250" height="90" rx="12" fill="#e7f5f0"/>
<text x="130" y="36" text-anchor="middle" font-weight="900" fill="{GP}">입으로 (분변-경구)</text>
<text x="130" y="66" text-anchor="middle" font-size="24" font-weight="900" fill="{GP}">A · E</text>
<text x="130" y="90" text-anchor="middle" font-size="11.5" fill="{MU}">모음(A, E) = 입 · 급성만, 만성 X</text>
<rect x="265" y="10" width="250" height="90" rx="12" fill="#fdeceb"/>
<text x="390" y="36" text-anchor="middle" font-weight="900" fill="#c0392b">피로 (혈액·성접촉)</text>
<text x="390" y="66" text-anchor="middle" font-size="24" font-weight="900" fill="#c0392b">B · C · D</text>
<text x="390" y="90" text-anchor="middle" font-size="11.5" fill="{MU}">자음 = 피 · 만성 → 간경변 → 간암</text>
</svg>'''
