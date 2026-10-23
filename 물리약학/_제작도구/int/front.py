# -*- coding: utf-8 -*-
from lib import *

page(0, '''<section class="page cover">
<div class="k">PHYSICAL PHARMACY · WEEK 2–7 · MIDTERM MASTER</div>
<h1>물리약학 중간고사 통합 마스터 요약본<br>용해도 → 착물 → 확산 → 방출, 한 권으로 끝내기</h1>
<div class="sub">2·3·4–6·7주차 강의 + 기출·예제 + 소그룹 활동 32문제 + 삼성노트 필기 — 모든 문제는 🧭 사고의 흐름으로 풀이</div>
<div class="how">각 개념 카드 → <span class="p">💡 핵심</span><span class="p">📖 설명 · 비유</span><span class="p">📐 공식</span><span class="p">✍️ 사고의 흐름</span><span class="p">🧠 한 줄</span><span class="p">📝 내 필기</span></div>
<div class="parts">
<div><b>시작</b>사용법 · 2–7주차 가계도 · 약어 사전 · 수학 겁먹지 않기</div>
<div><b>PART 1 · 2주차</b>용해도 · pH와 침전 · 보용매 · 입자 크기 · 분배계수 · 추출</div>
<div><b>PART 2 · 3주차</b>배위수 · 킬레이트 · 카페인 착물 · 내포화합물 · 시클로덱스트린 · 단백질 결합</div>
<div><b>PART 3 · 4–6주차</b>Fick 법칙 · 정상상태 · P = DK/h · 다층 · 막/수층 제어 · pH 분배 · 패치</div>
<div><b>PART 4 · 7주차 + 마무리</b>Noyes-Whitney · Higuchi · Bottari · K-P · 캡슐 · BCS · 헷갈리는 짝 · 오답 TOP · 한 장 정리</div>
</div>{FOOT}</section>''')

FAM = '''<svg viewBox="0 0 1040 300" width="1040" height="300">
<defs><marker id="ar" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L9,4.5 L0,9 z" fill="#555"/></marker></defs>
<g font-family="Pretendard" font-size="13">
<rect x="10" y="20" width="190" height="110" rx="12" fill="#e6f4f5" stroke="#0e7c86" stroke-width="2"/>
<text x="105" y="44" text-anchor="middle" font-weight="800" fill="#0a5960" font-size="15">① 용해도 (2주차)</text>
<text x="105" y="66" text-anchor="middle">최대로 녹는 양 Cs · S₀</text><text x="105" y="86" text-anchor="middle">pH = pKa + log((S−S₀)/S₀)</text><text x="105" y="106" text-anchor="middle">보용매 · 입자 크기</text>
<rect x="10" y="160" width="190" height="110" rx="12" fill="#e6f4f5" stroke="#0e7c86" stroke-width="2"/>
<text x="105" y="184" text-anchor="middle" font-weight="800" fill="#0a5960" font-size="15">② 분배 (2주차)</text>
<text x="105" y="206" text-anchor="middle">K = C기름 / C물</text><text x="105" y="226" text-anchor="middle">진 vs 겉보기 · 추출</text><text x="105" y="246" text-anchor="middle">→ 지용성의 숫자</text>
<rect x="245" y="90" width="190" height="110" rx="12" fill="#f3ecfb" stroke="#7b3fb5" stroke-width="2"/>
<text x="340" y="114" text-anchor="middle" font-weight="800" fill="#5a2690" font-size="15">③ 착물 (3주차)</text>
<text x="340" y="136" text-anchor="middle">용해도·분배를 바꾸는 도구</text><text x="340" y="156" text-anchor="middle">CD 가용화 · 카페인 · EDTA</text><text x="340" y="176" text-anchor="middle">단백질 결합 = 투석·한외여과</text>
<rect x="480" y="90" width="200" height="110" rx="12" fill="#eef0fd" stroke="#4954d1" stroke-width="2"/>
<text x="580" y="114" text-anchor="middle" font-weight="800" fill="#2c35a0" font-size="15">④ 확산 (4–6주차)</text>
<text x="580" y="136" text-anchor="middle">J = D·K·ΔC / h</text><text x="580" y="156" text-anchor="middle">P = DK/h · R = ΣR</text><text x="580" y="176" text-anchor="middle">정상상태 · 싱크 · pH 분배</text>
<rect x="725" y="90" width="200" height="110" rx="12" fill="#fdf0e9" stroke="#c4501f" stroke-width="2"/>
<text x="825" y="114" text-anchor="middle" font-weight="800" fill="#933610" font-size="15">⑤ 방출·용출 (7주차)</text>
<text x="825" y="136" text-anchor="middle">Noyes-Whitney (ΔC = Cs−C)</text><text x="825" y="156" text-anchor="middle">Higuchi (h ∝ √t) · 0차</text><text x="825" y="176" text-anchor="middle">Bottari · K-P · 캡슐</text>
<rect x="955" y="90" width="80" height="110" rx="12" fill="#e8f1fb" stroke="#1d6db1" stroke-width="2"/>
<text x="995" y="125" text-anchor="middle" font-weight="800" fill="#134e83" font-size="15">흡수</text><text x="995" y="147" text-anchor="middle">BCS</text><text x="995" y="167" text-anchor="middle" font-size="11">용해도×투과도</text>
<line x1="200" y1="90" x2="476" y2="128" stroke="#555" stroke-width="2" marker-end="url(#ar)"/>
<line x1="200" y1="215" x2="476" y2="165" stroke="#555" stroke-width="2" marker-end="url(#ar)"/>
<line x1="200" y1="75" x2="243" y2="110" stroke="#7b3fb5" stroke-width="2" stroke-dasharray="5 4" marker-end="url(#ar)"/>
<line x1="200" y1="230" x2="243" y2="185" stroke="#7b3fb5" stroke-width="2" stroke-dasharray="5 4" marker-end="url(#ar)"/>
<line x1="680" y1="145" x2="721" y2="145" stroke="#555" stroke-width="2" marker-end="url(#ar)"/>
<line x1="925" y1="145" x2="951" y2="145" stroke="#555" stroke-width="2" marker-end="url(#ar)"/>
<text x="330" y="70" font-size="12" fill="#555" font-weight="700">Cs가 ΔC가 된다</text>
<text x="330" y="240" font-size="12" fill="#555" font-weight="700">K가 막 입구 점프가 된다</text>
<text x="660" y="235" font-size="12" fill="#933610" font-weight="700">Cs (2주차) → Noyes-Whitney · Higuchi의 Cs (7주차)</text>
<text x="660" y="255" font-size="12" fill="#2c35a0" font-weight="700">P = DK/h (5주차) → BCS의 "투과도" (7주차)</text>
<text x="660" y="275" font-size="12" fill="#5a2690" font-weight="700">투석 · 한외여과 (4주차 응용) → 단백질 결합 측정 (3주차)</text>
</g></svg>'''

page(0, f'''<section class="page p0"><div class="ptop"><span class="pl">시작</span><span class="pt">이 책 사용법 · 2–7주차 가계도</span><span class="pr">Read me first</span></div>
<div class="sh" style="font-size:16px">🌳 2–7주차는 "공식 하나의 가계도" — 따로 외울 게 아니라 이어져 있어요</div>
<div class="fig">{FAM}</div>
<div class="grid2" style="margin-top:6px">
<div>{sh('📚 이렇게 보세요')}{ul(['<b>개념 카드</b>: 💡 핵심 → 📖 설명·비유 → 📐 공식 → ✍️ 사고의 흐름 예제 → 🧠 한 줄. 분홍 점선 📝 = 내가 삼성노트에 썼던 필기.',
   '<b>문제</b>: 왼쪽 = 문제 + ✏️ 내 풀이 칸, 오른쪽 = 정답 + 🧭 사고의 흐름. <b>오른쪽을 가리고 먼저 풀기!</b>',
   '<b>출처 표시</b>: 주황 테두리 = 강의 예제·기출, <span style="color:#134e83;font-weight:800">파란 테두리 = 소그룹 활동(조별 출제)</span>.',
   '<b>마무리</b>: 주차를 넘나드는 헷갈리는 짝 → 2024 중간 오답 TOP → 한 장 정리.'])}</div>
<div>{sh('🧭 사고의 흐름 아이콘')}{flow([('see', '문제에서 눈에 띄는 단어·숫자'), ('ask', '"이게 뭐였지?" 떠올리는 질문'), ('link', '알고 있는 개념·공식과 연결'), ('calc', '숫자 계산'), ('chk', '함정·오답 보기 점검'), ('done', '결론')])}</div>
</div>{{FOOT}}</section>''')

page(0, f'''<section class="page p0" style="font-size:13.3px;line-height:1.48"><div class="ptop"><span class="pl">시작</span><span class="pt">약어 · 기호 · 이름 사전 — 이 책의 모든 약어</span><span class="pr">Abbreviations</span></div>
<div class="grid2">
<div>{tbl(['약어 / 기호', 'Full name → 뜻'], [
    ['S · S₀ · Cs', 'Solubility(총 용해도) · 고유(분자형) 용해도 · Saturation(포화) 농도'],
    ['pH · pKa · Ka', 'power of Hydrogen(산성도) · −log Ka · acid dissociation constant(산 해리 상수)'],
    ['MW', 'Molecular Weight — 분자량 (g/mol)'],
    ['USP · KP', 'United States Pharmacopeia(미국약전) · Korean Pharmacopoeia(대한민국약전)'],
    ['K · log P', 'Partition coefficient(분배계수) · 옥탄올/물 분배계수의 log'],
    ['SLS', 'Sodium Lauryl Sulfate — 라우릴황산나트륨(계면활성제)'],
    ['EDTA', 'EthyleneDiamineTetraAcetic acid — 6자리 킬레이트제'],
    ['en (EDA)', 'ethylenediamine — 에틸렌다이아민, 2자리 리간드'],
    ['CD (α·β·γ)', 'CycloDextrin — 시클로덱스트린 (포도당 6·7·8개)'],
    ['J · D · P · R', 'Flux(확산류) · Diffusion coefficient · Permeability(투과도) · Resistance(저항)'],
    ['d · r · a · m', 'Donor(공여체) · Receptor(수용체) · Aqueous(물층) · Membrane(막)'],
    ['tL', 'lag time — 지연시간'],
    ['ATP', 'Adenosine TriPhosphate — 세포 에너지 화폐'],
    ['MDR · P-gp', 'Multi-Drug Resistance · P-glycoprotein(약을 퍼내는 펌프)'],
])}</div>
<div>{tbl(['약어 / 이름', 'Full name → 뜻'], [
    ['TDDS · TTS', 'Transdermal Drug Delivery / Therapeutic System — 경피 패치'],
    ['BBB', 'Blood-Brain Barrier — 혈액-뇌 장벽'],
    ['IR · DR · ER · CR', 'Immediate · Delayed · Extended · Controlled Release (속방·지연·서방·조절 방출)'],
    ['OROS', 'Osmotic-controlled Release Oral delivery System — 삼투압 펌프 알약'],
    ['API · ADME', 'Active Pharmaceutical Ingredient · 흡수·분포·대사·배설'],
    ['BCS', 'Biopharmaceutics Classification System — 생물약제학적 분류체계'],
    ['K-P', 'Korsmeyer-Peppas (코르스마이어-페파스) 모델'],
    ['PABA · PEG', 'para-AminoBenzoic Acid · PolyEthylene Glycol'],
    ['Henderson–Hasselbalch', '헨더슨-하셀바흐 — pH와 해리 비율 식'],
    ['Yalkowsky', '얄코프스키 — 용해도-분배계수 관계식'],
    ['Fick · Higuchi · Noyes-Whitney', '픽 · 히구치 · 노예스-휘트니'],
    ['Bottari · Hixson-Crowell', '보타리 · 힉슨-크로웰(세제곱근 법칙)'],
    ['Karth · Wurster · Sweetana/Grass', '카르트 · 부르스터 · 스위타나/그래스 확산셀'],
    ['Clathrate · Lewis', '클라드레트(새장 격자 착물) · 루이스(전자쌍 산·염기)'],
])}
<div class="ana"><span class="t">📌 읽는 요령</span>본문 속 어려운 말 옆 <span class="jk">[즉, ~라는 뜻]</span>만 이어 읽어도 흐름이 보이게 썼어요.</div></div>
</div>{{FOOT}}</section>''')

page(0, f'''<section class="page p0"><div class="ptop"><span class="pl">시작</span><span class="pt">수학 겁먹지 않기 — 이 범위에 필요한 수학은 딱 6개</span><span class="pr">Math</span></div>
<div class="grid2">
<div>
{sh('➊ log — "10을 몇 번 곱했나"')}<p>log 10 = 1, log 100 = 2, log 1 = 0. <mark>log(a/b) = log a − log b</mark>, <mark>log(aⁿ) = n·log a</mark>. pH가 pKa보다 1 크면 A⁻ : HA = 10 : 1, 2 크면 100 : 1, 3 크면 1000 : 1.</p>
<p>음수 log 되돌리기: −4.64 = −5 + 0.36 → 10<sup>0.36</sup> × 10⁻⁵.</p>
{sh('➋ 지수 계산 (10ⁿ)')}<p>곱하기는 지수 <b>더하기</b>, 나누기는 지수 <b>빼기</b>: 0.01 ÷ 10⁻⁶ = 10⁻² ÷ 10⁻⁶ = <b>10⁴</b>. 더하기는 지수부터 맞추기: 5×10⁵ = 0.5×10⁶.</p>
{sh('➌ 비례 · 루트')}<p>A ∝ B: B 2배 → A 2배. A ∝ 1/B: B 2배 → A 절반. <mark>Q ∝ √t</mark>: 양 2배가 되려면 시간 <b>4배</b>.</p>
</div>
<div>
{sh('➍ 미분 = 기울기 = 순간 속도')}<p>dC/dx = 거리 1 갈 때 농도 변화(비탈길), dQ/dt = 지금 이 순간 나오는 속도(속도계). √t를 미분하면 1/(2√t).</p>
{mynote('<p><b>편미분 ∂</b>: 변수가 2개 이상(위치 x, 시간 t)일 때 <em>하나만 콕 집어서</em> 미분. "시간은 잠깐 멈추고(고정), 위치에 따라 얼마나 달라지나?"만 발라낼 때 꼬부라진 ∂를 써요.</p><p><b>2번 미분</b>: y = x² → 한 번 2x, 두 번 2. 한 번 = 기울기, 두 번 = 기울기가 변하는 정도(<em>휘어진 정도</em>). = 0 직선, &gt; 0 오목(∪), &lt; 0 볼록(∩).</p>')}
{sh('➎ 적분 = 쌓기')}<p>속도를 시간 동안 쌓으면 누적량: 매시간 2 mg × 3시간 = 6 mg.</p>
{sh('➏ 단위 감각')}<p>g/100 mL → g/L은 ×10 · g/L ÷ MW = mol/L · cm → μm는 ×10⁴ · 1시간 = 3600초.</p>
</div></div>{{FOOT}}</section>''')
