# -*- coding: utf-8 -*-
"""풀이 칸 밑 '그림 정답' — 구조식(RDKit) + 시약 화살표 + 직관적 한 줄 설명.
토큰: ('m', smiles, 라벨) 구조 / ('t', 글자) 기호 / ('r', 시약) 시약 화살표 / ('br',) 줄바꿈 / ('h', 라벨) 소제목
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chemdraw import svg

CSS = """
.av { margin-top: 6pt; border: 1.4pt solid #2456c9; border-radius: 8pt; background: #f5f8ff; padding: 5pt 9pt 6pt; position: relative }
.av .tag { position: absolute; left: 8pt; top: -8pt; background: #2456c9; color: #fff; font-size: 8.8pt; font-weight: 800; border-radius: 5pt; padding: 0 7pt; line-height: 14pt }
.av .ln { display: flex; align-items: center; flex-wrap: wrap; gap: 0 3pt; margin-top: 2pt }
.av .m { display: inline-flex; flex-direction: column; align-items: center }
.av .m svg { display: block }
.av .m i { font-style: normal; font-size: 8pt; color: #2456c9; font-weight: 700; margin-top: -3pt; white-space: nowrap }
.av .op { font-size: 13pt; font-weight: 800; color: #1d3557; padding: 0 2pt }
.av .h { font-size: 9pt; font-weight: 800; color: #fff; background: #1d3557; border-radius: 4pt; padding: 0 5pt; margin-right: 2pt }
.av .rg { display: inline-flex; flex-direction: column; align-items: center; padding: 0 2pt }
.av .rg span { font-size: 8.4pt; color: #1d3557; font-weight: 700; white-space: nowrap }
.av .rg b { display: block; width: 44pt; height: 0; border-top: 1.2pt solid #1d3557; position: relative; margin-top: 1pt }
.av .rg b:after { content: ''; position: absolute; right: -1pt; top: -4.1pt; border-left: 6pt solid #1d3557; border-top: 3.2pt solid transparent; border-bottom: 3.2pt solid transparent }
.av .say { font-size: 9.8pt; line-height: 1.45; color: #1f2633; margin-top: 3pt; padding-top: 3pt; border-top: .8pt dashed #b9c8ea }
.av .say b { color: #d1335b }
"""


def render(spec, size=1.0):
    toks, say = spec
    W, H, SC = int(132 * size), int(80 * size), 20 * size
    lines, cur = [], []
    for t in toks:
        if t[0] == 'br':
            lines.append(cur); cur = []
            continue
        if t[0] == 'm':
            w = int(W * (t[3] if len(t) > 3 else 1))
            lab = f'<i>{t[2]}</i>' if t[2] else ''
            cur.append(f'<span class="m">{svg(t[1], w, H, SC)}{lab}</span>')
        elif t[0] == 't':
            cur.append(f'<span class="op">{t[1]}</span>')
        elif t[0] == 'r':
            cur.append(f'<span class="rg"><span>{t[1]}</span><b></b></span>')
        elif t[0] == 'h':
            cur.append(f'<span class="h">{t[1]}</span>')
    lines.append(cur)
    body = ''.join(f'<div class="ln">{"".join(l)}</div>' for l in lines if l)
    s = f'<div class="say">{say}</div>' if say else ''
    return f'<div class="av"><span class="tag">정답</span>{body}{s}</div>'


m = lambda s, l='', k=1: ('m', s, l, k)
t = lambda x: ('t', x)
r = lambda x: ('r', x)
h = lambda x: ('h', x)
BR = ('br',)

# ───────── 막판 29제 (key = 장-원본쪽) ─────────
V29 = {
'17-11': ([m('COc1ccc(O)cc1', 'p-OCH₃'), t('&lt;'), m('Oc1ccccc1', '페놀'), t('&lt;'), m('Oc1ccc(F)cc1', 'p-F'), t('&lt;'), m('N#Cc1ccc(O)cc1', 'p-CN', 1.15)],
          '밀어줌(OCH₃) → O⁻ 불안정 = 약산 · 당김(F &lt; CN) → O⁻ 음전하 분산 = <b>강산</b>'),
'17-14': ([h('a'), r('NaBH₄'), m('CC(O)CCC(=O)OC', '', 1.2), h('b'), r('LiAlH₄'), m('CC(O)CCCO', '', 1.05), BR, h('c'), r('LiAlH₄'), m('CC1=CCC(C(C)=C)CC1O', '', 1.0)],
          '케톤만 → <b>NaBH₄</b>(순한 칼) · 에스터까지 → <b>LiAlH₄</b>(센 칼) · 둘 다 C=C는 그대로'),
'17-22': ([h('a'), m('CC=O', '', .55), t('+'), m('CC[Mg]Br', '', .8), t('or'), m('CCC=O', '', .7), t('+'), m('C[Mg]Br', '', .7), BR,
           h('b'), m('CCC=O', '', .7), t('+'), m('CC[Mg]Br', '', .8), h('c'), m('C=O', '', .45), t('+'), m('C=C(C)[Mg]Br', '', .9)],
          'OH 탄소의 가지 하나를 <b>싹둑</b> → 자른 가지 = RMgBr, 남은 몸통 = C=O'),
'17-31': ([h('a'), t('NaBH₄'), h('b'), t('PBr₃'), h('c'), t('Mg → HCHO'), BR, h('d'), t('DMP'), h('e'), t('PhCH₂MgBr'), h('f'), t('POCl₃, py')],
          '환원(C=O→OH) → 치환(OH→Br) → 그리냐르+HCHO(탄소+1) → <b>순한 산화</b>(CHO) → 그리냐르 → 탈수(C=C)'),
'18-11': ([h('a'), m('[O-]C1CCCCC1', '', .75), t('+'), m('CCCCBr', '', .8), t('(둘 다 OK)'), BR, h('b'), m('[O-]Cc1ccccc1', '', .9), t('+'), m('CCBr', '', .5),
           h('c'), m('C=C(C)C', '', .55), t('+'), m('CCC(C)O', '', .65), r('Hg²⁺→NaBH₄'), BR, h('d'), m('OCCCCBr', '', .85), r('NaH'), m('C1CCOC1', '', .55)],
          'O 한쪽이 <b>1차</b> → 윌리엄슨(1차–Br + RO⁻) · 양쪽 다 붐빔 → <b>알콕시수은화</b>'),
'18-14': ([h('a'), m('CC(C)(Br)c1ccccc1', '', 1.0), t('+'), m('CO', '', .4), h('b'), m('CCC(C)O', '', .7), t('+'), m('CCCBr', '', .65)],
          '(a) 3차·벤질 쪽 끊어져 Br (S<sub>N</sub>1) · (b) 1차 vs 2차 → <b>덜 붐비는 1차</b>에 Br (S<sub>N</sub>2)'),
'18-24': ([h('a'), m('CCC(C)(O)C[18OH]', '염기: ¹⁸O → CH₂', 1.0), h('b'), m('CCC(C)([18OH])CO', '산: ¹⁸O → 3차', 1.0), h('c'), m('CCC(C)(O)C(C)c1ccccc1', 'Ph → 덜 붐비는 C', 1.1)],
          '<b>염기·그리냐르</b> = 가벼운 C 공격 / <b>산</b> = 3차 C 공격 (생성물 모양은 같고 ¹⁸O 자리만 다름)'),
'18-25': ([m('CC12CCCCC1O2', '', .8), r('1. CH₃MgBr 2. H₃O⁺'), m('CC1CCCCC1(C)O', '', .85)],
          'CH₃⁻가 <b>H 달린(덜 붐비는) C</b>를 뒤에서 공격 → OH는 3차 C에, 두 CH₃(새 것)와 OH는 <b>trans</b>'),
'19-7': ([h('a'), m('CCCCCO', '', .75), r('DMP'), h('b'), m('C=CCCCC', '', .75), r('O₃ → Zn'), BR, h('c'), m('CCCCC(=O)OC', '', .9), r('DIBAH −78°C'),
          h('d'), m('C=CCCC', '', .65), r('BH₃ → DMP'), BR, t('모두 →'), m('CCCCC=O', '펜탄알', .8)],
         '탄소 수 같으면 산화·환원(DMP, DIBAH) · 많으면 자르기(O₃) · 끝 C에 OH 필요하면 BH₃'),
'19-14': ([m('CCC(=O)CC', '', .7), r('CH₃NH₂'), m('CCC(=NC)CC', '이민', .75), t(' '), r('(CH₃)₂NH'), m('CC=C(CC)N(C)C', '엔아민', .85)],
          'N에 H 2개(1차) → H₂O로 빠지고 <b>C=N</b> · H 1개(2차) → 옆 C의 H를 빼서 <b>C=C–N</b>'),
'19-36': ([h('a'), m('C=CC(C)=O', '', .6), t('+ Pr₂CuLi'), h('b'), m('CC1=CC(=O)CCC1', '', .65), t('+ Me₂CuLi'), BR,
           h('c'), m('CC(C)(C)C1CCC(=O)C=C1', '', .8), t('+ Et₂CuLi'), h('d'), m('O=C1CCC2CCCCC2=C1', '', .75), t('+ (vinyl)₂CuLi')],
          'β 자리에 붙일 가지 = <b>길만 시약의 R</b> · 나머지 = α,β-불포화 케톤'),
'19-37': ([h('a'), m('CC1C(=O)CC(C(C)=C)CC1C', '1,4', 1.0), h('b'), m('CC1=CCC(C(C)=C)CC1O', '1,2', .95), h('c'), m('CNC1CC(C(C)=C)CC(=O)C1C', '1,4', 1.05)],
          '부드러운 길만·아민 → <b>β 탄소(1,4)</b>, C=O 남음 · 센 LiAlH₄ → <b>C=O(1,2)</b>, C=C 남음'),
'19-38': ([h('d'), m('CC1=CCC(C(C)=C)CC1(O)c1ccccc1', '1,2', 1.1), h('e'), m('CC1CCC(C(C)C)CC1=O', 'C=C 둘 다 환원', .95), BR,
           h('f'), m('CC1=CCC(C(C)=C)CC12OCCO2', '케탈', 1.05), h('g'), m('CC=C1C(C)=CCC(C(C)=C)C1', '위티그', 1.05)],
          '그리냐르 = 1,2 · H₂/Pd = C=C만 · 다이올+H⁺ = C=O 금고(케탈) · 위티그 = O 자리에 =CHCH₃'),
'20-12': ([m('CC(O)C(=O)O', '젖산 3.86', .75), t('&gt;'), m('CC(=O)O', '아세트산 4.76', .6)],
          'α-OH가 전자를 <b>당김</b> → COO⁻ 음전하가 퍼져 안정 → H⁺를 더 잘 내놓음 = <b>강산</b>'),
'20-15': ([h('a'), m('Cc1ccc(C(=O)O)cc1', '', .8), t('&lt;'), m('O=C(O)c1ccccc1', '', .7), t('&lt;'), m('O=C(O)c1ccc(Cl)cc1', '', .8), BR,
           h('b'), m('CC(=O)O', '', .45), t('&lt;'), m('O=C(O)c1ccccc1', '', .7), t('&lt;'), m('O=C(O)c1ccc([N+](=O)[O-])cc1', '', 1.0)],
          'CH₃(밀어줌) → 약해짐 · Cl, NO₂(당김) → 강해짐 · 아세트산 4.76 &gt; 벤조산 4.19'),
'20-17': ([h('a'), m('CC(C)(C)Cl', '', .55), r('1. Mg 2. CO₂ 3. H₃O⁺'), m('CC(C)(C)C(=O)O', '', .7), BR,
           h('b'), m('CCCBr', '', .55), r('1. NaCN 2. H₃O⁺'), m('CCCC(=O)O', '', .65), t('(Mg/CO₂도 OK)')],
          '3차는 CN⁻가 뒤로 못 들어가 E2(알켄) → <b>그리냐르만</b> · 1차는 둘 다 가능'),
'20-27': ([m('C=CC(C)C', '', .55), r('a BH₃ → H₂O₂'), m('OCCC(C)C', '', .65), r('b PBr₃'), m('BrCCC(C)C', '', .65), r('c Mg → CO₂'), m('OC(=O)CCC(C)C', '', .75)],
          'a: 끝 C에 OH = <b>반마르코프니코프 BH₃</b> · b: OH → Br · c: 탄소 +1 (CN⁻ → H₃O⁺도 OK)'),
'21-7': ([m('O=C(Cl)c1ccccc1', '', .75), r('① CH₃O⁻ 공격'), m('CO[C-0](Cl)c1ccccc1'.replace('[C-0]', 'C([O-])'), '사면체 중간체', .9), r('② Cl⁻ 이탈'), m('COC(=O)c1ccccc1', '', .8)],
         '① 친핵체가 C=O 탄소 공격 → O⁻ (첨가) ② O⁻가 C=O 복구하며 <b>Cl⁻를 밀어냄</b> (제거)'),
'21-9': ([h('a'), m('CC(=O)Cl', '', .45), t('&gt;'), m('COC(C)=O', '', .5), t('&gt;'), m('CC(N)=O', '', .45), BR,
          h('b'), m('CC(=O)OC(C(F)(F)F)C(F)(F)F', '', .9), t('&gt;'), m('CC(=O)OCC(Cl)(Cl)Cl', '', .8), t('&gt;'), m('CCOC(C)=O', '', .55)],
         '이탈기가 좋을수록(약한 염기, EWG 많을수록) 반응성 ↑ · 아마이드 = N 공명으로 <b>꼴찌</b>'),
'21-10': ([h('a'), m('CC(=O)[O-].[Na+]', '', .7), h('b'), m('CC(N)=O', '', .45), h('c'), m('COC(C)=O', '', .5), t('+'), m('CC(=O)[O-]', '', .5), h('d'), m('CNC(C)=O', '', .5)],
          '이탈기 떼고 친핵체(H 하나 뗀 것) 붙이기 · (a)는 NaOH 때문에 <b>카복실레이트</b>로 끝남'),
'21-16': ([m('CCOC(=O)CC(C)C', '', .8), r('H₂O, HCl'), m('CC(C)CC(=O)O', '', .7), t('+'), m('CCO', '', .4)],
          '산 촉매: O 양성자화 → 물 공격 → EtOH 이탈 · <b>물 과량 = 가수분해 쪽</b>'),
'21-18': ([m('CC(=O)O', '', .45), t('+'), m('CN', '', .3), r('그냥 섞으면'), m('CC(=O)[O-].C[NH3+]', '염 ✗', .8), BR,
           m('CC(=O)O', '', .45), t('+'), m('CN', '', .3), r('DCC'), m('CNC(C)=O', '아마이드 ✓', .5), t('+ DCU')],
          '(a) 산-염기 반응 → 염 (b) DCC·EDC / SOCl₂ → 아민 (c) O-acylisourea · DCU (d) HOBt = <b>부반응 억제</b>'),
'21-26': ([h('a'), m('CCC(=O)c1ccccc1', '', .75), h('b'), m('CCCO', '', .4), h('c'), m('CCC(C)(C)O', '', .5), h('d'), m('CCC(=O)O', '', .45), BR,
           h('e'), m('CCC(=O)OC1CCCCC1', '', .8), h('f'), m('CCC(=O)Nc1ccccc1', '', .85), h('g'), m('CCC(=O)OC(C)=O', '', .65)],
          '산 염화물 = 사다리 꼭대기 → <b>Cl 자리에 친핵체</b>만 바꿔 끼우면 끝 (LiAlH₄·RMgBr은 2번)'),
'21-32': ([m('O=C1CCCO1', '', .5), r('LiAlH₄'), m('OCCCCO', '다이올', .6), t(' '), r('DIBAH −78°C'), m('O=CCCCO', '하이드록시 알데하이드', .7)],
          '고리가 열리며 양 끝에 O · LiAlH₄ = <b>끝까지</b> / DIBAH = <b>알데하이드에서 멈춤</b>'),
'21-36': ([m('O=C1CCO1', '', .45), r('2 EtMgBr → H₃O⁺'), m('CCC(O)(CC)CCO', '다이올', .75)],
          '락톤 + 그리냐르 2번 → 고리 열림 → 한쪽 끝 OH, 반대쪽은 <b>Et 2개 달린 3차 OH</b>'),
'21-38': ([m('CCNC(=O)c1ccccc1', '', .8), h('a'), r('NaOH, 가열'), m('O=C(O)c1ccccc1', '', .65), BR,
           h('b'), r('가수분해 → LiAlH₄'), m('OCc1ccccc1', '', .6), h('c'), r('LiAlH₄'), m('CCNCc1ccccc1', '', .75)],
          'N을 <b>버리려면 먼저 가수분해</b> · N을 <b>남기려면 바로 LiAlH₄</b> (C=O → CH₂, 아민)'),
'21-40': ([h('a'), m('CCC(O)(CC)C1CCCCC1', '', .8), h('b'), m('CC(C)CCC=O', '', .6), BR, h('c'), m('CNC(=O)C1CCCC1', '', .7), h('d'), m('COC(=O)C1CCCCC1C', 'trans 유지', .75)],
          '(a) 그리냐르 2번 (b) DIBAH 멈춤 (c) 산 염화물 + 아민 (d) C=O에서만 반응 → 고리 입체 그대로'),
'21-41': ([h('e'), m('C=CC(C)CCO', '', .65), h('f'), m('CC(=O)OC1CCCCC1', '', .7), BR, h('g'), m('Cc1ccccc1CN', '', .65), h('h'), m('O=C(Cl)Cc1ccccc1Br', '', .75)],
          'LiAlH₄: 에스터 → 알코올(C=C 그대로), <b>아마이드 → 아민</b> · SOCl₂: COOH → COCl'),
'21-44': ([m('Cc1cccc(Br)c1', '', .6), r('Mg'), r('CO₂, H₃O⁺'), m('Cc1cccc(C(=O)O)c1', '', .7), r('SOCl₂'), m('Cc1cccc(C(=O)Cl)c1', '', .7), r('Et₂NH'), m('CCN(CC)C(=O)c1cccc(C)c1', 'DEET', .85)],
          'Ar–Br → 그리냐르 → CO₂(탄소 +1) → <b>SOCl₂로 사다리 올리기</b> → 아민 = 아마이드'),
}

# ───────── 예상문제 14제 (번호 = E1..E14) ─────────
V14 = {
1: ([m('Cc1ccc(O)cc1', 'B', .7), t('&lt;'), m('Oc1ccccc1', 'A', .65), t('&lt;'), m('Oc1ccc(Cl)cc1', 'C', .75), t('&lt;'), m('O=[N+]([O-])c1ccc(O)cc1', 'D', .95)],
    'CH₃ 밀어줌 → 약산 · Cl 당김 → 조금 강 · <b>NO₂ 당김 + 공명</b>으로 O⁻ 분산 → 가장 강'),
2: ([h('a'), m('CC(O)CCC(=O)OC', '', 1.0), h('b'), m('CC(O)CCCO', '', .85), h('c'), m('CCCCC=O', '', .7), BR,
     h('d'), m('CCCCC(=O)O', '', .75), h('e'), m('CC1(O)CCCCC1', '', .6)],
    'NaBH₄ 케톤만 · LiAlH₄ 에스터까지 · DMP 알데하이드 멈춤 · CrO₃ 산까지 · 케톤+RMgBr = 3차 알코올'),
3: ([h('a'), t('① ✓'), t('② ✗ →'), m('C=C(C)C', 'E2 알켄', .55), h('b'), m('Oc1ccccc1', '', .55), t('+ CH₃Br'), BR,
     h('c'), m('CC(C)(C)I', '', .55), t('+'), m('CCO', '', .4)],
    '윌리엄슨은 <b>메틸·1차 쪽이 R–X</b> · 벤젠–O는 안 끊김 → 페놀 · 3차 쪽이 끊어져 할로젠'),
4: ([h('a'), m('COCC(C)(C)O', 'CH₂ 공격', .75), h('b'), m('COC(C)(C)CO', '3차 C 공격', .75), h('c'), m('CCC(C)(C)O', 'CH₂ 공격', .65)],
    '<b>염기·그리냐르</b> → 덜 붐비는 CH₂ / <b>산</b> → 3차 C ((a)(b)는 OCH₃ 자리만 반대!)'),
5: ([h('a'), m('OC1CCCCC1', '', .5), r('PCC·DMP'), m('O=C1CCCCC1', '', .5), h('b'), r('N₂H₄, KOH'), m('C1CCCCC1', '', .45), BR,
     h('c'), m('CCCCCC(=O)OC', '', .75), r('DIBAH −78°C'), m('CCCCCC=O', '', .65), BR,
     h('d'), r('NaBH₄'), m('CCCCCCO', '', .65), h('e'), r('CrO₃, H₃O⁺'), m('CCCCCC(=O)O', '', .7)],
    '⬆ 산화 = O 넣는 시약(PCC·DMP·CrO₃) · ⬇ 환원 = H 넣는 시약(NaBH₄·LiAlH₄·DIBAH) · C=O 삭제 = 볼프-키슈너'),
6: ([h('a'), m('CC1(O)C=CCCC1', '1,2', .6), h('b'), m('CC1CCCC(=O)C1', '1,4', .6), h('c'), m('OC1C=CCCC1', '1,2', .55), BR,
     h('d'), m('CN(C)C1CCCC(=O)C1', '1,4', .75), h('e'), m('N#CC1CCCC(=O)C1', '1,4', .7)],
    '센 놈(RMgBr, LiAlH₄) → C=O 직격 = <b>1,2</b> · 부드러운 놈(Cu, 아민, CN⁻) → β = <b>1,4</b>'),
7: ([h('a'), t('CH₃COOH &lt; ClCH₂COOH &lt; Cl₂CHCOOH &lt; CF₃COOH'), BR, h('b'), m('CCC(Cl)C(=O)O', '2-Cl 더 강', .75), t('&gt;'), m('OC(=O)CCCCl', '', .75), h('c'), t('EtOH &lt; 페놀 &lt; 아세트산')],
    '당기는 원자 <b>많을수록 · 가까울수록</b> 강산 · 음전하를 퍼뜨릴 곳 많을수록(COO⁻ &gt; 페녹사이드 &gt; RO⁻) 강산'),
8: ([h('a'), m('CC(C)(C)Cl', '', .5), r('Mg → CO₂ → H₃O⁺'), m('CC(C)(C)C(=O)O', '', .65), BR,
     h('b'), m('CCCCBr', '', .55), r('NaCN → H₃O⁺'), m('CCCCC(=O)O', '', .7), h('c'), m('N#Cc1ccccc1', '', .6), r('EtMgBr → H₃O⁺'), m('CCC(=O)c1ccccc1', '', .75)],
    '3차는 CN⁻ 불가 → 그리냐르 · 그리냐르는 나이트릴에 <b>딱 1번</b> → 케톤'),
9: ([h('a'), m('CC(=O)Cl', 'C', .45), t('&gt;'), m('CC(=O)OC(C)=O', 'D', .65), t('&gt;'), m('COC(C)=O', 'A', .5), t('&gt;'), m('CC(N)=O', 'B', .45)],
    '(b) N 비공유쌍 → C=O 공명 → C의 δ+ ↓ + NH₂⁻ 나쁜 이탈기 = <b>아마이드 꼴찌</b>'),
10: ([m('CC(=O)Cl', '', .45), r('① EtOH 공격'), m('CCOC(C)([O-])Cl', '사면체', .7), r('② Cl⁻ 이탈'), m('CCOC(C)=O', '', .6), t('+ py·HCl')],
     '① O의 전자쌍 → C=O 탄소 (π는 O로) ② O⁻가 C=O 복구, <b>Cl⁻ 밀어냄</b> ③ 피리딘이 H⁺ 제거'),
11: ([h('a'), m('O=C(O)c1ccccc1', '', .65), h('b'), m('OCc1ccccc1', '', .6), h('c'), m('O=Cc1ccccc1', '', .6), h('d'), m('CC(C)(O)c1ccccc1', '', .65)],
     'NaOH → 카복실레이트(→산) · LiAlH₄ → 알코올 · <b>DIBAH → 알데하이드에서 멈춤</b> · RMgBr 2번 → 3차 알코올'),
12: ([h('a'), m('CN(C)Cc1ccccc1', '', .7), h('b'), m('O=C(O)c1ccccc1', '', .6), h('c'), m('O=C([O-])c1ccccc1', '', .6), BR,
      h('d'), m('C1CCNC1', '고리 유지', .45), h('e'), m('OCCCCO', '고리 열림', .55)],
     '아마이드 + LiAlH₄ = <b>C=O → CH₂, 아민</b> · 락탐은 고리 그대로, 락톤은 고리가 열림'),
13: ([h('a'), r('CH₃OH, H₂SO₄'), h('b'), r('NaOH → CH₃I'), m('COC(=O)c1ccccc1', '', .65), BR,
      h('c'), r('SOCl₂ → EtNH₂'), t('또는'), r('EtNH₂ + DCC'), m('CCNC(=O)c1ccccc1', '', .75)],
     '산 = 카보닐 활성화(피셔) · 염기 = COO⁻가 <b>친핵체</b>(S<sub>N</sub>2) · 아마이드는 OH를 먼저 <b>활성화</b>'),
14: ([m('Brc1ccccc1', '', .5), r('Mg'), r('CO₂, H₃O⁺'), m('O=C(O)c1ccccc1', '', .6), r('SOCl₂'), m('O=C(Cl)c1ccccc1', '', .6), r('Et₂NH'), m('CCN(CC)C(=O)c1ccccc1', '', .8)],
     'Ar–Br → 그리냐르 → CO₂ → <b>SOCl₂(사다리 꼭대기)</b> → 2차 아민 = 아마이드'),
}


def check():
    from rdkit import Chem
    bad = []
    for d in (V29, V14):
        for k, (toks, _) in d.items():
            for tk in toks:
                if tk[0] == 'm' and Chem.MolFromSmiles(tk[1]) is None:
                    bad.append((k, tk[1]))
    return bad


if __name__ == '__main__':
    print('bad:', check(), len(V29), len(V14))


# ───────── 21장 추가 22문항 ─────────
V29.update({
'21-8': ([m('O=C(Cl)c1ccccc1', '', .7), t('+'), m('CC(C)O', '', .4), r('pyridine'), m('CC(C)OC(=O)c1ccccc1', '아이소프로필 벤조에이트', .85), t('+ HCl')],
         '이탈기(Cl) 떼고 → 친핵체(2-프로판올의 O, H 하나 뗌) 끼우기 = <b>레고 블록 교체</b>'),
'21-11': ([m('COC(=O)CC1CCCC1', '출발: 메틸 사이클로펜틸아세테이트', .9), r('OH⁻'), m('[O-]C(=O)CC1CCCC1', '생성: 카복실레이트', .8), t('+ CH₃O⁻')],
          '친핵체 = <b>OH⁻</b> · 이탈기 = <b>CH₃O⁻</b> · 염기 조건이라 최종은 <b>카복실레이트</b>(비누화 중간 단계)'),
'21-12': ([m('OC(=O)c1ccccc1Br', '', .7), t('+'), m('CCCO', '', .45), r('H⁺ (HCl)'), m('CCCOC(=O)c1ccccc1Br', '프로필 o-브로모벤조에이트', .9), t('+ H₂O')],
          '에스터를 <b>C(=O)–O에서 싹둑</b> → C=O 쪽 + OH = 산, O 쪽 + H = 알코올 (피셔 에스터화)'),
'21-13': ([h('a'), m('CC(=O)O', '', .45), t('+'), m('CCCCO', '', .55), h('b'), m('CCCC(=O)O', '', .55), t('+ CH₃OH'), BR,
           h('c'), m('OC(=O)C1CCCC1', '', .6), t('+'), m('CC(C)O', '', .4), t('(모두 H⁺ 촉매)')],
          'C(=O)–O 사이를 가르면 바로 짝이 나온다 · 평형 → <b>알코올 과량</b> 또는 물 제거'),
'21-14': ([m('OCCCCC(=O)O', '5-하이드록시펜탄산', .8), r('H⁺, −H₂O'), m('O=C1CCCCO1', 'δ-발레로락톤 (6각)', .55)],
          '한 분자 안의 OH가 몸을 구부려 C=O 탄소 공격 → 물 빠지며 <b>고리 에스터 = 락톤</b>'),
'21-15': ([h('a'), m('OC(=O)C1CCCC1', '', .55), r('SOCl₂'), m('O=C(Cl)C1CCCC1', '', .55), h('b'), m('CC=CC(=O)O', '', .5), r('SOCl₂'), m('CC=CC(=O)Cl', '', .5)],
          'OH → <b>Cl</b> (사다리 꼭대기로) · 부산물 SO₂·HCl <b>기체</b>로 날아가 비가역 · C=C는 그대로'),
'21-17': ([m('CC=CC(=O)O', '', .5), t('+ CH₃OH'), r('HCl 촉매'), m('CC=CC(=O)OC', '메틸 2-뷰테노에이트', .6), t('+ H₂O')],
          '(a)의 정확한 역반응 · 이탈기 = <b>–OH₂⁺</b>(양성자화된 물) · C=C는 그대로'),
'21-20': ([h('a'), m('CCC(=O)Cl', '', .45), t('+ CH₃OH'), h('b'), m('CC(=O)Cl', '', .4), t('+ CH₃CH₂OH'), BR,
           h('c'), m('O=C(Cl)c1ccccc1', '', .6), t('+ CH₃CH₂OH'), t('(피리딘)')],
          '에스터를 C(=O)–O에서 자르고 C=O 쪽에 <b>Cl</b> → 산 염화물 + 알코올. 피리딘 = HCl 청소부'),
'21-21': ([m('O=C(Cl)c1ccccc1', '', .6), t('+'), m('OC1CCCCC1', '', .5), r('pyridine'), m('O=C(OC1CCCCC1)c1ccccc1', '사이클로헥실 벤조에이트', .8)],
          '<b>산 염화물 방법</b>이 낫다 — 빠르고 비가역. 피셔는 평형이라 알코올을 과량 써야 하는데 사이클로헥산올은 비싸고 2차'),
'21-22': ([m('CCC(=O)Cl', '', .45), t('+ 2 CH₃NH₂'), r(' '), m('CCC(=O)NC', 'N-메틸프로판아마이드', .55), t('+ CH₃NH₃⁺Cl⁻')],
          '아민 <b>2당량</b> = 1당량 공격수 + 1당량 HCl 청소부 · 3차 아민(N–H 없음)은 아마이드 불가'),
'21-23': ([m('COc1cc(C(=O)Cl)cc(OC)c1OC', '', .8), t('+'), m('C1COCCN1', '모르폴린', .45), r('NaOH'), m('COc1cc(C(=O)N2CCOCC2)cc(OC)c1OC', '트라이메토진', 1.0)],
          '① N이 C=O 공격(첨가) → ② C=O 복구, <b>Cl⁻ 이탈</b>(제거) → ③ OH⁻가 N⁺–H의 H⁺ 제거'),
'21-24': ([h('a'), m('CCC(=O)Cl', '', .45), t('+ 2 CH₃NH₂'), h('b'), m('O=C(Cl)c1ccccc1', '', .6), t('+ 2 (CH₃CH₂)₂NH'), BR,
           h('c'), m('CCC(=O)Cl', '', .45), t('+ 2 NH₃')],
          '<b>N 위의 가지 = 아민에서 온 것</b>, C=O 쪽 = 산 염화물 · 아민은 항상 2당량'),
'21-25': ([h('a'), m('O=C(Cl)c1ccccc1', '', .55), t('+ [(CH₃)₂CH]₂CuLi'), r(''), m('CC(C)C(=O)c1ccccc1', '', .6), BR,
           h('b'), m('C=CC(=O)Cl', '', .45), t('+ (CH₃CH₂CH₂)₂CuLi'), r(''), m('C=CC(=O)CCCC', '', .6)],
          '<b>길만(R₂CuLi)</b>은 산 염화물을 딱 1번 → <b>케톤에서 멈춤</b> (그리냐르면 3차 알코올까지)'),
'21-28': ([m('O=C1OC(=O)c2ccccc12', '프탈산 무수물', .6), r('CH₃OH 1당량'), m('COC(=O)c1ccccc1C(=O)O', '모노메틸 에스터', .7)],
          '한쪽 –COOCH₃ · 반대쪽 반쪽은 고리로 묶여 있어서 같은 분자에 <b>–COOH</b>로 남는다'),
'21-29': ([m('O=C1CCC(=O)O1', '숙신산 무수물', .5), r('CH₃O⁻ Na⁺'), m('COC(=O)CCC(=O)[O-]', '한쪽 에스터, 한쪽 COO⁻', .75)],
          '고리형 이탈기는 분자 밖으로 못 나가고 <b>분자 안에 남는다</b> (21-15와 같은 원리)'),
'21-30': ([m('CCOC(C)=O', '', .45), r('OH⁻'), m('CC(=O)O', '', .4), t('+ ⁻OEt'), r('빠른 산-염기'), m('CC(=O)[O-]', '카복실레이트', .45), t('+ EtOH')],
          '생긴 RCOOH의 H⁺를 RO⁻(강염기)가 즉시 뺏음 → <b>RCOO⁻</b>의 (−) 전하가 친핵체를 막아 <b>비가역</b>'),
'21-31': ([m('CCC(=O)OCC', '', .55), t('+'), m('CCN', '', .35), r('pyridine'), m('CCC(=O)NCC', 'N-에틸프로판아마이드', .55), t('+ CH₃CH₂OH')],
          '에스터 → 아마이드 = 사다리 <b>내려가기</b>라 가능 (단 느려서 실전엔 산 염화물)'),
'21-33': ([h('a'), m('CCCC(C)C(=O)OC', '', .6), r('LiAlH₄'), m('CCCC(C)CO', '', .55), t('+ CH₃OH'), BR,
           h('b'), m('O=C(Oc1ccccc1)c1ccccc1', '', .7), r('LiAlH₄'), m('OCc1ccccc1', '벤질 알코올', .5), t('+'), m('Oc1ccccc1', '페놀', .45)],
          '에스터 + LiAlH₄ = <b>알코올 2개</b>로 쪼개짐 · C=O 쪽 → 1차 알코올, O 쪽 → 그대로 알코올(페놀)'),
'21-34': ([h('a'), m('CCOC(=O)c1ccccc1', '', .6), t('+ 2 CH₃MgBr'), h('b'), m('CCOC(C)=O', '', .45), t('+ 2 PhMgBr'), BR,
           h('c'), m('CCCCC(=O)OCC', '', .6), t('+ 2 CH₃CH₂MgBr')],
          '3차 알코올에서 <b>똑같은 가지 2개</b> = 그리냐르 2당량 · 나머지 가지 1개 + C=O = 에스터'),
'21-35': ([m('CCOC(=O)CC(C)C', '', .6), t('+ 2 PhMgBr'), r('→ H₃O⁺'), m('CC(C)CC(O)(c1ccccc1)c1ccccc1', '3-메틸-1,1-다이페닐-1-뷰탄올', .85), t('+ EtOH')],
          '1번째 Ph⁻: 치환(–OEt 이탈) → 케톤 · 2번째 Ph⁻: 첨가 → <b>Ph 2개 달린 3차 알코올</b>'),
'21-37': ([m('CC(=O)Nc1ccccc1', 'N-페닐아세트아마이드', .65), r('1. LiAlH₄ 2. H₂O'), m('CCNc1ccccc1', 'N-에틸아닐린', .6)],
          '아마이드 + LiAlH₄ = <b>C=O → CH₂</b>, 아민 (O만 빠짐) · 거꾸로: N 옆 CH₂를 C=O로'),
'21-43': ([m('O=C(O)c1ccc([N+](=O)[O-])cc1O', '', .8), r('SOCl₂'), r('PhOH'), r('Fe, H₃O⁺'), m('Nc1ccc(C(=O)Oc2ccccc2)c(O)c1', '페닐 4-아미노살리실레이트', 1.0)],
          '① SOCl₂로 활성화 → ② 페놀 = 에스터 → ③ <b>환원은 마지막</b> (NH₂가 먼저 생기면 산 염화물을 공격해 아마이드)'),
})
