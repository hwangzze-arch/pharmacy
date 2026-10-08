# -*- coding: utf-8 -*-
"""18장 테스트뱅크 (lehninger6e_tb_ch18). 55문제 모두 강의 범위 → 전부 수록."""
from helpers import *
from tblib import mcq, ans, sa
from exam18 import overview, zymogen, gdh, gln_carry, entry_map, thf_states, met_cycle, phe_tyr
from ch18 import urea_cycle, gaa_cycle

TB = []


def add(**kw):
    kw.setdefault('kind', 'MC')
    TB.append(kw)


def entry_table():
    return table(['진입점', '아미노산'], [['피루브산', 'A C G S T W'], ['α-KG', 'P R H E Q'], ['숙시닐-CoA', 'I M T V'], ['푸마르산', 'F Y'], ['OAA', 'N D'], ['아세틸-CoA', 'I L T W'], ['아세토아세틸-CoA', 'L K F Y W']], cls='left')


def urea_steps():
    return table(['#', '효소', '장소', '반응'], [['①', 'CPS I', '미토', 'NH₄⁺ + HCO₃⁻ + 2ATP → 카르바모일 인산'], ['②', 'OTC', '미토', '+ 오르니틴 → 시트룰린'], ['③', 'ASS', '세포질', '+ 아스파르트산 + ATP → 아르기니노숙신산'], ['④', 'ASL', '세포질', '→ 아르기닌 + 푸마르산'], ['⑤', '아르기네이스', '세포질', '→ 요소 + 오르니틴']], cls='left')


def transam_fig():
    return flow(['아미노산 + α-KG', 'α-케토산 + 글루탐산'], arrow_labels=['아미노전이효소 (PLP)'], colors=[C['navy'], C['green']], box_h=40, width=520, font=11)


# ================================================================ S1 (0) 큰 그림
add(n=1, sec=0, diff=2, title='아미노산이 산화 분해되지 않는 상황',
    en=mcq('Under which circumstances are amino acids not metabolized via oxidative degradation?', ['Starvation', 'Plants growing in nutrient-rich soils', 'Normal protein turnover', 'A diet rich in proteins', 'Uncontrolled diabetes']),
    ko=mcq('아미노산이 산화 분해되지 <b>않는</b> 상황은?', ['기아', '<b>영양이 풍부한 토양에서 자라는 식물</b>', '정상 단백질 교체', '고단백 식사', '조절 안 되는 당뇨']),
    answer=ans('B', 'Plants growing in nutrient-rich soils', '영양 풍부한 토양의 식물'),
    explain=key('식물은 아미노산을 거의 태우지 않고 생합성 재료로 쓴다. 동물이 아미노산을 태우는 3가지 상황 = C·D·A/E.') + table(['상황', '왜?'], [['단백질 교체', '남는 아미노산은 저장 못 해 태움'], ['고단백 식사', '필요 이상은 연료로'], ['기아·당뇨', '탄수화물 못 써 체단백 분해']], cls='left'))

add(n=43, sec=0, diff=2, kind='SA', title='포유류가 암모니아 대신 요소를 만드는 이유',
    en='<p>Why does a mammal go to all of the trouble of making urea from ammonia rather than simply excreting ammonia as many bacteria do?</p>', ko='<p>포유류는 왜 세균처럼 암모니아를 그냥 내보내지 않고 굳이 요소로 만드는가?</p>',
    answer=sa('Bacteria release ammonia into the surrounding medium, where it is diluted to nontoxic levels. In mammals, ammonia cannot be diluted enough in tissues and blood to avoid toxic levels; urea is much less toxic.', '세균은 주변 물에 희석하면 끝. 포유류는 몸속에서 충분히 희석할 수 없어 독성 수준까지 쌓인다 → 독성이 훨씬 낮은 요소로 바꿔 버린다.'),
    explain=key('NH₄⁺ ↑ → 뇌에서 글루타민 축적 → 뇌부종 · 혼수 (S5).') + fig(overview(), ''))

add(n=44, sec=0, diff=2, kind='SA', title='질소를 버리는 세 가지 형태',
    en='<p>Describe the three different forms of nitrogen by which different organisms dispose of excess nitrogen. Give examples.</p>', ko='<p>생물이 남는 질소를 버리는 세 가지 형태와 예를 들어라.</p>',
    answer=sa('(1) Ammonotelic: NH₄⁺ (bacteria, many aquatic animals, bony fish); (2) Uricotelic: uric acid (birds, reptiles); (3) Ureotelic: urea (most terrestrial vertebrates, including humans).', '① 암모니아 배설형 NH₄⁺ (세균·물고기) ② 요산 배설형 (새·파충류) ③ 요소 배설형 (사람 등 육상 척추동물)'),
    explain=table(['형태', '동물', '이유'], [['암모니아', '물고기', '물에 바로 희석'], ['요소', '사람', '독성 낮고 잘 녹음'], ['요산', '새 · 파충류', '물을 아끼려 고체로']], cls='left'))

add(n=45, sec=0, diff=2, kind='SA', title='20가지 아미노산을 처리하는 공통 전략',
    en='<p>Amino acid catabolism involves 20 amino acids that all contain nitrogen but have different carbon skeletons. What overall strategy is used? Give two examples.</p>', ko='<p>20개 아미노산은 모두 질소가 있지만 탄소 골격은 다르다. 공통 전략은? 예 두 가지.</p>',
    answer=sa('Nitrogen is first removed by transamination to glutamate, converting each amino acid into an α-keto acid that is (or becomes) an intermediate of carbohydrate catabolism. E.g., alanine → pyruvate; aspartate → oxaloacetate.', '먼저 아미노기 전이로 질소를 글루탐산에 모으고, 남은 α-케토산은 해당·TCA 중간체가 된다. 예: 알라닌 → 피루브산, 아스파르트산 → OAA.'),
    explain=key('질소는 한 곳(글루탐산 → 요소), 탄소는 7개 진입점으로.') + fig(overview(), ''))

# ================================================================ S2 (1) 소화
add(n=2, sec=1, diff=2, title='소장에서 작용하는 단백질 분해효소가 아닌 것',
    en=mcq('Which of these is not a protease that acts in the small intestine?', ['Chymotrypsin', 'Elastase', 'Enteropeptidase', 'Secretin', 'Trypsin']),
    ko=mcq('소장에서 작용하는 단백질 분해효소가 <b>아닌</b> 것은?', ['키모트립신', '엘라스테이스', '엔테로펩티데이스', '<b>세크레틴</b>', '트립신']),
    answer=ans('D', 'Secretin', '세크레틴 — 효소가 아니라 호르몬'), explain=key('세크레틴 = 췌장에 HCO₃⁻를 내라고 시키는 호르몬.') + fig(zymogen(), ''))

add(n=3, sec=1, diff=2, title='효소원 활성화의 열쇠',
    en=mcq('In the digestion of protein that occurs in the small intestine, which enzyme is critical in the activation of zymogens?', ['Enteropeptidase', 'Hexokinase', 'Papain', 'Pepsin', 'Secretin']),
    ko=mcq('소장 단백질 소화에서 효소원 활성화에 결정적인 효소는?', ['<b>엔테로펩티데이스</b>', '헥소키나아제', '파파인', '펩신', '세크레틴']),
    answer=ans('A', 'Enteropeptidase', '엔테로펩티데이스 (트립시노겐 → 트립신)'), explain=fig(zymogen(), '') + key('첫 트립신만 만들면 트립신이 나머지를 연쇄로 켠다.'))

add(n=4, sec=1, diff=2, title='Lys·Arg 옆을 자르는 효소의 효소원',
    en=mcq('Which is a zymogen that can be converted to an endopeptidase that hydrolyzes peptide bonds adjacent to Lys and Arg residues?', ['Chymotrypsinogen', 'Pepsin', 'Pepsinogen', 'Trypsin', 'Trypsinogen']),
    ko=mcq('Lys·Arg 옆 펩타이드 결합을 자르는 효소가 되는 <b>효소원</b>은?', ['키모트립시노겐', '펩신', '펩시노겐', '트립신', '<b>트립시노겐</b>']),
    answer=ans('E', 'Trypsinogen', '트립시노겐'), explain=steps('Lys·Arg(+ 전하) 뒤를 자르는 효소 = 트립신.', '“효소원”을 물었으니 -ogen → 트립시노겐.') + warn('D 트립신은 활성 효소라 오답.', '함정'))

add(n=32, sec=1, diff=3, kind='SA', title='가스트린·펩시노겐·CCK·엔테로펩티데이스',
    en='<p>Describe briefly the role of (a) gastrin, (b) pepsinogen, (c) cholecystokinin, and (d) enteropeptidase in protein digestion.</p>', ko='<p>단백질 소화에서 (a) 가스트린 (b) 펩시노겐 (c) CCK (d) 엔테로펩티데이스의 역할은?</p>',
    answer=sa('(a) Gastrin stimulates secretion of HCl and pepsinogen; (b) pepsinogen → pepsin begins protein digestion in the stomach; (c) CCK stimulates secretion of pancreatic zymogens; (d) enteropeptidase activates trypsinogen → trypsin, which activates the other zymogens.', '(a) HCl·펩시노겐 분비 (b) 펩신이 되어 위에서 분해 시작 (c) 췌장 효소원 분비 (d) 트립시노겐 → 트립신 (→ 나머지 활성화)'),
    explain=fig(zymogen(), ''))

add(n=33, sec=1, diff=2, kind='SA', title='인슐린을 먹는 약으로 못 쓰는 이유',
    en='<p>In the treatment of diabetes, insulin is injected. Why can’t this hormone, a small protein, be taken orally?</p>', ko='<p>인슐린(작은 단백질)은 왜 먹지 못하고 주사해야 하나?</p>',
    answer=sa('Insulin would be denatured by gastric acid and digested by proteases; even if intact, the intestinal cells absorb free amino acids, not whole proteins.', '위산·단백질 분해효소에 분해되고, 장은 아미노산만 흡수하지 통째 단백질은 흡수하지 않는다.'),
    explain=key('먹은 인슐린 = 그냥 아미노산 간식.') + fig(zymogen(), ''))

add(n=34, sec=1, diff=2, kind='SA', title='헬리코박터의 우레이스가 산을 중화하는 원리',
    en='<p>Helicobacter pylori survives stomach acid in part by excreting urease, which hydrolyzes urea to bicarbonate and ammonia. Explain how these products make the environment less acidic.</p>', ko='<p>H. pylori는 요소를 HCO₃⁻와 NH₃로 분해하는 우레이스를 내놓아 위산에서 살아남는다. 왜 덜 산성이 되나?</p>',
    answer=sa('Bicarbonate is a buffer: HCO₃⁻ + H⁺ → H₂CO₃ → CO₂ + H₂O. Ammonia also takes up a proton: NH₃ + H⁺ → NH₄⁺. Both consume H⁺.', 'HCO₃⁻ + H⁺ → CO₂ + H₂O, NH₃ + H⁺ → NH₄⁺ — 둘 다 H⁺를 먹어 치운다.'),
    explain=align([('HCO₃⁻ + H⁺', '→ H₂CO₃ → CO₂ + H₂O', ''), ('NH₃ + H⁺', '→ NH₄⁺', '')]) + key('두 산물 모두 염기 → 세균 주변에 중화 방패.') + tip('요소 호기 검사(¹³C-요소)로 H. pylori를 진단하는 원리이기도 하다.', '임상'))

add(n=35, sec=1, diff=1, kind='SA', title='효소원의 정의와 예',
    en='<p>Define zymogen and describe the role of one zymogen in protein digestion.</p>', ko='<p>효소원을 정의하고 소화에서의 예를 하나 들어라.</p>',
    answer=sa('A zymogen is an inactive enzyme precursor activated by proteolytic cleavage. E.g., trypsinogen is cleaved by enteropeptidase to trypsin in the small intestine.', '잘려야 켜지는 비활성 전구체. 예: 트립시노겐 → (엔테로펩티데이스) → 트립신.',),
    explain=warn('테스트뱅크 해설은 펩시노겐을 “췌장 효소”라고 적었지만 펩시노겐은 <b>위</b>(으뜸세포)에서 나온다.', '자료 오류') + key('자기 몸(췌장)을 소화하지 않으려고 꺼진 상태로 만든다.'))

# ================================================================ S3 (2) 아미노기 전이·PLP
add(n=5, sec=2, diff=2, title='많은 아미노산 이화의 첫 반응',
    en=mcq('In amino acid catabolism, the first reaction for many amino acids is a(n):', ['decarboxylation requiring TPP.', 'hydroxylation requiring NADPH and O₂.', 'oxidative deamination requiring NAD⁺.', 'reduction requiring PLP.', 'transamination requiring PLP.']),
    ko=mcq('많은 아미노산 이화의 첫 반응은?', ['TPP 탈카복실화', 'NADPH·O₂ 수산화', 'NAD⁺ 산화적 탈아미노화', 'PLP 환원', '<b>PLP 아미노기 전이</b>']),
    answer=ans('E', 'transamination requiring PLP', 'PLP 의존 아미노기 전이'), explain=fig(transam_fig(), '') + warn('C는 글루탐산 하나에만 쓰이는 GDH 반응.', '함정'))

add(n=6, sec=2, diff=2, title='아미노기 전이 조효소의 비타민',
    en=mcq('The coenzyme required for all transaminations is derived from:', ['niacin.', 'pyridoxine (vitamin B₆).', 'riboflavin.', 'thiamin.', 'vitamin B₁₂.']),
    ko=mcq('모든 아미노기 전이의 조효소는 무엇에서 오나?', ['나이아신', '<b>피리독신 (B₆)</b>', '리보플라빈', '티아민', 'B₁₂']),
    answer=ans('B', 'pyridoxine (vitamin B₆)', '비타민 B₆ → PLP'), explain=table(['비타민', '조효소'], [['B₁ 티아민', 'TPP'], ['B₂ 리보플라빈', 'FAD'], ['B₃ 나이아신', 'NAD⁺'], ['<b>B₆ 피리독신</b>', '<b>PLP</b>']]))

add(n=7, sec=2, diff=1, title='아미노전이효소의 조효소',
    en=mcq('The coenzyme involved in a transaminase reaction is:', ['biotin phosphate.', 'lipoic acid.', 'NADP⁺.', 'pyridoxal phosphate (PLP).', 'thiamine pyrophosphate (TPP).']),
    ko=mcq('아미노전이효소의 조효소는?', ['비오틴 인산', '리포산', 'NADP⁺', '<b>PLP</b>', 'TPP']),
    answer=ans('D', 'pyridoxal phosphate (PLP)', 'PLP'), explain=fig(transam_fig(), ''))

add(n=8, sec=2, diff=1, title='알라닌 → α-KG 아미노기 전이의 조효소',
    en=mcq('Transamination from alanine to α-ketoglutarate requires the coenzyme:', ['biotin.', 'NADH.', 'No coenzyme is involved.', 'pyridoxal phosphate (PLP).', 'TPP.']),
    ko=mcq('알라닌 → α-KG 아미노기 전이(ALT)의 조효소는?', ['비오틴', 'NADH', '없음', '<b>PLP</b>', 'TPP']),
    answer=ans('D', 'pyridoxal phosphate (PLP)', 'PLP'), explain=key('ALT: 알라닌 + α-KG ⇌ 피루브산 + 글루탐산.'))

add(n=9, sec=2, diff=1, title='PLP가 촉매할 수 없는 반응',
    en=mcq('Which reaction involving an amino acid cannot be catalyzed via a PLP-dependent mechanism?', ['Hydrolysis', 'Decarboxylation', 'Racemization', 'Transamination', 'Transimination']),
    ko=mcq('PLP 기전으로 촉매할 수 <b>없는</b> 반응은?', ['<b>가수분해</b>', '탈카복실화', '라세미화', '아미노기 전이', '알디민 교환']),
    answer=ans('A', 'Hydrolysis', '가수분해'), explain=key('PLP = α 탄소의 전자 싱크 → 아미노기 전이 · 라세미화 · 탈카복실화.') + steps('E 알디민 교환: Lys–PLP(내부) → 아미노산–PLP(외부) — 모든 PLP 반응의 첫 단계.'))

add(n=36, sec=2, diff=1, kind='SA', title='아미노기 전이 빈칸',
    en='<p>Transamination reactions all require ______ as a coenzyme. In the first step, the coenzyme in the aldehyde form condenses with the ______ group of an amino acid to form a(n) ______.</p>', ko='<p>아미노기 전이는 모두 ___ 조효소가 필요하다. 첫 단계에서 알데하이드형 조효소가 아미노산의 ___기와 축합해 ___를 만든다.</p>',
    answer=sa('pyridoxal phosphate (PLP); α-amino; Schiff base (imine, aldimine)', 'PLP · α-아미노 · 쉬프 염기(알디민)'),
    explain=table(['상태', '모양'], [['대기 (내부 알디민)', 'PLP + 효소 Lys'], ['반응 중 (외부 알디민)', 'PLP + 기질 아미노산'], ['아미노기 받음', 'PMP']], cls='left'))

add(n=37, sec=2, diff=1, kind='SA', title='글루탐산 + 피루브산의 아미노기 전이',
    en='<p>Draw the reactants and products of the transamination in which glutamate and pyruvate are the starting materials. What cofactor is required?</p>', ko='<p>글루탐산과 피루브산으로 시작하는 아미노기 전이의 반응물·산물을 그려라. 보조인자는?</p>',
    answer=sa('Glutamate + pyruvate ⇌ α-ketoglutarate + alanine (alanine aminotransferase); cofactor PLP.', '글루탐산 + 피루브산 ⇌ α-KG + 알라닌 (ALT, PLP)'),
    explain=table(['', '구조'], [['글루탐산', '⁻OOC–CH₂–CH₂–CH(NH₃⁺)–COO⁻'], ['피루브산', 'CH₃–CO–COO⁻'], ['α-KG', '⁻OOC–CH₂–CH₂–CO–COO⁻'], ['알라닌', 'CH₃–CH(NH₃⁺)–COO⁻']], cls='left') + key('–NH₃⁺와 =O가 자리만 바꾼다.'))

add(n=38, sec=2, diff=1, kind='SA', title='α-KG와 아미노기 전이 후의 α-케토산',
    en='<p>Name and draw the α-keto acid formed when (a) glutamate, (b) aspartate, (c) alanine undergo transamination with α-ketoglutarate.</p>', ko='<p>(a) 글루탐산 (b) 아스파르트산 (c) 알라닌이 α-KG와 아미노기 전이하면 생기는 α-케토산은?</p>',
    answer=sa('(a) α-ketoglutarate; (b) oxaloacetate; (c) pyruvate', '(a) α-KG (b) OAA (c) 피루브산'),
    explain=table(['아미노산', '↔ α-케토산', '구조'], [['글루탐산', 'α-KG', '⁻OOC–CH₂–CH₂–CO–COO⁻'], ['아스파르트산', 'OAA', '⁻OOC–CH₂–CO–COO⁻'], ['알라닌', '피루브산', 'CH₃–CO–COO⁻']]))

add(n=39, sec=2, diff=3, kind='SA', title='PLP 아미노기 전이의 중간체',
    en='<p>Describe, by showing the chemical intermediates, the role of PLP in the transamination of an amino acid.</p>', ko='<p>PLP가 아미노기 전이에서 하는 역할을 중간체로 설명하라.</p>',
    answer=sa('Enzyme–Lys–PLP (internal aldimine) → amino acid replaces Lys (external aldimine) → tautomerization (quinonoid → ketimine) → hydrolysis releases α-keto acid, leaving PMP. PMP then transfers –NH₂ to α-ketoglutarate in the reverse sequence, regenerating PLP and forming glutamate.', '내부 알디민 → 외부 알디민 → (자리 이동) 케티민 → 가수분해: α-케토산 방출 + PMP → 역순으로 α-KG에 –NH₂ 넘김 → 글루탐산 + PLP 복귀'),
    explain=vflow(['E–Lys=PLP (내부 알디민)', '아미노산=PLP (외부 알디민)', '케티민 (이중결합 자리 이동)', '+ H₂O → α-케토산 방출 + PMP', 'PMP + α-KG → 글루탐산 + PLP'], colors=[C['gray'], C['navy'], C['purple'], C['green'], C['orange']], box_h=24, gap=12, width=520, font=10.5, bw=400) + tip('핑퐁 택배: 받고(PMP) → 내려놓고(PLP).', '비유'))

add(n=52, sec=2, diff=2, kind='SA', title='알라닌 분해의 첫 단계',
    en='<p>Some bacteria use alanine as their chief energy source. Describe the first step in alanine degradation; show any cofactors.</p>', ko='<p>알라닌을 주 에너지원으로 쓰는 세균. 알라닌 분해의 첫 단계와 보조인자는?</p>',
    answer=sa('Transamination: alanine + α-ketoglutarate ⇌ pyruvate + glutamate (PLP).', '아미노기 전이: 알라닌 + α-KG ⇌ 피루브산 + 글루탐산 (PLP)'), explain=fig(transam_fig(), ''))

# ================================================================ S4 (3) 운반
add(n=40, sec=3, diff=3, kind='SA', title='글루타민 합성효소와 글루타미네이스',
    en='<p>Describe the roles of glutamine synthetase and glutaminase in the metabolism of amino groups in mammals.</p>', ko='<p>포유류 아미노기 대사에서 글루타민 합성효소와 글루타미네이스의 역할은?</p>',
    answer=sa('In extrahepatic tissues, toxic NH₄⁺ is combined with glutamate to form glutamine (glutamine synthetase, ATP). Glutamine travels to liver/kidney, where glutaminase releases NH₄⁺ + glutamate; the NH₄⁺ goes to urea.', '조직: 글루탐산 + NH₄⁺ + ATP → 글루타민 (합성효소, 독성 없이 운반). 간·신장: 글루타민 → 글루탐산 + NH₄⁺ (글루타미네이스) → 요소.'),
    explain=fig(gln_carry(), ''))

add(n=42, sec=3, diff=2, kind='SA', title='포도당-알라닌 회로',
    en='<p>Describe the reactions and the role of the glucose-alanine cycle.</p>', ko='<p>포도당-알라닌 회로의 반응과 역할을 설명하라.</p>',
    answer=sa('In muscle, amino groups are transferred to pyruvate (from glycolysis) forming alanine, which carries nitrogen nontoxically to the liver. There alanine is transaminated back to pyruvate; the N goes to urea and pyruvate becomes glucose by gluconeogenesis, which returns to muscle.', '근육: 피루브산 + 아미노기 → 알라닌 → 간: 알라닌 → 피루브산(→ 포도당신생 → 근육) + 아미노기(→ 요소)'),
    explain=fig(gaa_cycle(), '') + key('질소 버리기 + 탄소 돌려받기 일석이조.'))

# ================================================================ S5 (4) GDH
add(n=10, sec=4, diff=2, title='GDH 반응에 대해 틀린 것',
    en=mcq('Which is not true of the reaction catalyzed by glutamate dehydrogenase?', ['It is similar to transamination in that it involves PLP.', 'NH₄⁺ is produced.', 'The enzyme can use either NAD⁺ or NADP⁺.', 'The enzyme is glutamate-specific, but the reaction is involved in oxidizing other amino acids.', 'α-Ketoglutarate is produced from an amino acid.']),
    ko=mcq('GDH 반응에 대해 <b>틀린</b> 것은?', ['<b>아미노기 전이처럼 PLP가 관여한다</b>', 'NH₄⁺ 생성', 'NAD⁺·NADP⁺ 둘 다 사용', '글루탐산 특이적이지만 다른 아미노산 산화에도 관여', 'α-KG 생성']),
    answer=ans('A', 'It involves PLP (false)', '틀림 — GDH는 PLP를 쓰지 않는다'), explain=fig(gdh(), ''))

add(n=11, sec=4, diff=2, title='글루탐산 → α-KG + NH₄⁺ 과정의 이름',
    en=mcq('Glutamate is converted to α-ketoglutarate and NH₄⁺ by a process described as:', ['deamination.', 'hydrolysis.', 'oxidative deamination.', 'reductive deamination.', 'transamination.']),
    ko=mcq('글루탐산 → α-KG + NH₄⁺ 과정은?', ['탈아미노화', '가수분해', '<b>산화적 탈아미노화</b>', '환원적 탈아미노화', '아미노기 전이']),
    answer=ans('C', 'oxidative deamination', '산화적 탈아미노화 (NAD(P)⁺ → NAD(P)H)'), explain=fig(gdh(), ''))

add(n=12, sec=4, diff=1, title='글루탐산 → α-케토산 + NH₄⁺',
    en=mcq('The conversion of glutamate to an α-keto acid and NH₄⁺:', ['does not require any cofactors.', 'is a reductive deamination.', 'is accompanied by ATP hydrolysis by the same enzyme.', 'is catalyzed by glutamate dehydrogenase.', 'requires ATP.']),
    ko=mcq('글루탐산 → α-케토산 + NH₄⁺ 반응은?', ['보조인자 불필요', '환원적', 'ATP 가수분해 동반', '<b>GDH가 촉매</b>', 'ATP 필요']),
    answer=ans('D', 'catalyzed by glutamate dehydrogenase', 'GDH'), explain=fig(gdh(), ''))

add(n=41, sec=4, diff=2, kind='SA', title='글루탐산에서 암모니아가 생기는 반응',
    en='<p>Show the reaction in which ammonia is formed from glutamate; include required cofactors and intermediates.</p>', ko='<p>글루탐산에서 암모니아가 생기는 반응을 보조인자·중간체와 함께 보여라.</p>',
    answer=sa('Glutamate dehydrogenase: glutamate + NAD(P)⁺ → (α-iminoglutarate) + H₂O → α-ketoglutarate + NH₄⁺ + NAD(P)H.', 'GDH: 글루탐산 + NAD(P)⁺ → α-이미노글루타르산 → + H₂O → α-KG + NH₄⁺ + NAD(P)H'),
    explain=fig(gdh(), '') + key('간 미토콘드리아, ADP ▲ / GTP ⊗.'))

# ================================================================ S7 (6) 요소 회로
add(n=13, sec=6, diff=1, title='요소가 주로 합성되는 곳',
    en=mcq('Urea synthesis in mammals takes place primarily in the:', ['brain.', 'kidney.', 'liver.', 'skeletal muscle.', 'small intestine.']),
    ko=mcq('요소 합성의 주 장소는?', ['뇌', '신장', '<b>간</b>', '골격근', '소장']),
    answer=ans('C', 'liver', '간'), explain=warn('B 신장은 요소를 <b>배설</b>하는 곳.', '함정'))

add(n=14, sec=6, diff=1, title='요소 회로에 관여하지 않는 것',
    en=mcq('Which substance is not involved in the production of urea from NH₄⁺ via the urea cycle?', ['Aspartate', 'ATP', 'Carbamoyl phosphate', 'Malate', 'Ornithine']),
    ko=mcq('요소 회로에 관여하지 <b>않는</b> 것은?', ['아스파르트산', 'ATP', '카르바모일 인산', '<b>말산</b>', '오르니틴']),
    answer=ans('D', 'Malate', '말산'), explain=urea_steps() + tip('말산은 회로 밖 션트(푸마르산 → 말산 → OAA)에서 나온다.', '참고'))

add(n=15, sec=6, diff=1, title='요소의 질소를 직접 주는 것',
    en=mcq('Which of these directly donates a nitrogen atom for the formation of urea?', ['Adenine', 'Aspartate', 'Creatine', 'Glutamate', 'Ornithine']),
    ko=mcq('요소의 질소를 직접 주는 것은?', ['아데닌', '<b>아스파르트산</b>', '크레아틴', '글루탐산', '오르니틴']),
    answer=ans('B', 'Aspartate', '아스파르트산 (③ ASS)'), explain=key('요소 N 두 개 = NH₄⁺(카르바모일 인산) + 아스파르트산.') + warn('E 오르니틴은 운반 좌석일 뿐, 자기 질소를 주지 않는다.', '함정'))

add(n=16, sec=6, diff=1, title='오르니틴 → 시트룰린은 무엇의 합성?',
    en=mcq('Conversion of ornithine to citrulline is a step in the synthesis of:', ['aspartate.', 'carnitine.', 'pyruvate.', 'tyrosine.', 'urea.']),
    ko=mcq('오르니틴 → 시트룰린은 무엇의 합성 단계?', ['아스파르트산', '카르니틴', '피루브산', '티로신', '<b>요소</b>']),
    answer=ans('E', 'urea', '요소 (② OTC)'), explain=fig(urea_cycle(), ''))

add(n=17, sec=6, diff=1, title='OTC가 촉매하는 반응',
    en=mcq('In the urea cycle, ornithine transcarbamoylase catalyzes:', ['cleavage of urea to ammonia.', 'formation of citrulline from ornithine and another reactant.', 'formation of ornithine from citrulline.', 'formation of urea from arginine.', 'transamination of arginine.']),
    ko=mcq('OTC가 촉매하는 것은?', ['요소 → 암모니아', '<b>오르니틴 + (카르바모일 인산) → 시트룰린</b>', '시트룰린 → 오르니틴', '아르기닌 → 요소', '아르기닌 아미노기 전이']),
    answer=ans('B', 'formation of citrulline from ornithine and another reactant', '오르니틴 + 카르바모일 인산 → 시트룰린'), explain=urea_steps())

add(n=18, sec=6, diff=1, title='요소 합성에 대해 틀린 것',
    en=mcq('Which statement is false in reference to mammalian synthesis of urea?', ['Krebs was a major contributor to elucidating the pathway.', 'Arginine is the immediate precursor to urea.', 'The carbon of urea is derived from mitochondrial HCO₃⁻.', 'The precursor to one of the nitrogens of urea is aspartate.', 'Urea production is an energy-yielding series of reactions.']),
    ko=mcq('요소 합성에 대해 <b>틀린</b> 것은?', ['크레브스가 밝혔다', '아르기닌이 바로 앞 전구체', '요소의 탄소는 미토 HCO₃⁻', '질소 하나는 아스파르트산', '<b>요소 생산은 에너지를 내는 반응</b>']),
    answer=ans('E', 'Urea production is energy-yielding (false)', '틀림 — ATP 3개(고에너지 결합 4개)를 <b>소모</b>'), explain=urea_steps())

# ================================================================ S8 (7) 연결·조절
add(n=20, sec=7, diff=2, title='소변 요소가 높은 사람의 식단',
    en=mcq('If a person’s urine contains unusually high concentrations of urea, which diet has he or she probably been eating?', ['High carbohydrate, very low protein', 'Very high carbohydrate, no protein, no fat', 'Very very high fat, high carbohydrate, no protein', 'Very high fat, very low protein', 'Very low carbohydrate, very high protein']),
    ko=mcq('소변 요소가 매우 높다면 최근 식단은?', ['고탄수 · 저단백', '초고탄수 · 무단백 · 무지방', '초고지방 · 고탄수 · 무단백', '초고지방 · 저단백', '<b>저탄수 · 초고단백</b>']),
    answer=ans('E', 'Very low carbohydrate, very high protein', '저탄수화물 · 초고단백'), explain=key('단백질 ↑ → 아미노산 분해 ↑ → 요소 ↑. 탄수화물까지 적으면 아미노산을 연료로 더 태운다.') + tip('요소 회로 효소 양도 고단백 식사 때 늘어난다 (S8 조절).', '연결'))

add(n=46, sec=7, diff=1, kind='SA', title='기아 때 요소가 늘어나는 이유',
    en='<p>During starvation, more urea production occurs. Explain.</p>', ko='<p>기아 때 요소 생산이 늘어나는 이유는?</p>',
    answer=sa('Cellular proteins are degraded and their carbon skeletons oxidized for energy (and gluconeogenesis); their amino groups are removed and excreted as urea.', '체단백질을 분해해 탄소는 연료·포도당신생에 쓰고, 떼어 낸 아미노기는 요소로 버린다.'),
    explain=key('기아 · 초고단백 식사 → 요소 회로 효소 5개 모두 합성 ↑.'))

# ================================================================ S9 (8) 결함·필수 AA
add(n=19, sec=8, diff=2, title='사람의 필수 아미노산',
    en=mcq('Which of the following amino acids is essential for humans?', ['Alanine', 'Aspartic acid', 'Asparagine', 'Serine', 'Threonine']),
    ko=mcq('사람의 필수 아미노산은?', ['알라닌', '아스파르트산', '아스파라긴', '세린', '<b>트레오닌</b>']),
    answer=ans('E', 'Threonine', '트레오닌'), explain=eq('H I L K M F <b>T</b> W V', '필수 아미노산 9개'))

add(n=47, sec=8, diff=2, kind='SA', title='요소 회로 결함 환자의 영양 문제와 치료',
    en='<p>Describe (a) the fundamental nutritional problem faced by individuals with genetic defects in urea-cycle enzymes and (b) two approaches to treatment.</p>', ko='<p>요소 회로 효소 결함 환자의 (a) 근본적인 영양 문제와 (b) 치료법 두 가지는?</p>',
    answer=sa('(a) Dietary protein raises blood ammonia, so protein must be limited — yet essential amino acids must still be eaten. (b) Give compounds (benzoate, phenylbutyrate) that bind glycine/glutamine and are excreted, so replenishing them removes ammonia; or supply compounds (arginine, carbamoyl glutamate) that bypass/stimulate the defective step.', '(a) 단백질을 줄여야 하지만 필수 아미노산은 먹어야 한다. (b) ① 벤조산·페닐뷰티르산으로 글리신·글루타민째 질소 배설 ② 아르기닌·카르바모일 글루탐산 보충'),
    explain=table(['약', '결합 상대', '버리는 N'], [['벤조산', '글리신', '1'], ['페닐뷰티르산', '글루타민', '2']]))

add(n=48, sec=8, diff=2, kind='SA', title='앞 3개 효소 결핍 환자에게 아르기닌을 주는 이유',
    en='<p>Explain why one might give high concentrations of Arg to patients deficient in one of the first three enzymes of the urea cycle.</p>', ko='<p>요소 회로 앞 3개 효소 중 하나가 결핍된 환자에게 아르기닌을 많이 주는 이유는?</p>',
    answer=sa('Arginase still works, so Arg is converted to urea and ornithine; the extra ornithine raises intermediate levels and increases flux through the remaining cycle (Arg also activates NAG synthase).', '아르기네이스는 정상 → 아르기닌 → 요소 + 오르니틴. 오르니틴(좌석)이 늘어 회로 흐름 ↑. (아르기닌은 NAG 합성효소도 켬)'),
    explain=fig(urea_cycle(), ''))

# ================================================================ S10 (9) 진입점
add(n=21, sec=9, diff=2, title='아미노기 전이 한 번으로 TCA 중간체가 되는 것',
    en=mcq('Which amino acid can be directly converted into a citric acid cycle intermediate by transamination?', ['Glutamic acid', 'Serine', 'Threonine', 'Tyrosine', 'Proline']),
    ko=mcq('아미노기 전이 한 번으로 TCA 중간체가 되는 것은?', ['<b>글루탐산</b>', '세린', '트레오닌', '티로신', '프롤린']),
    answer=ans('A', 'Glutamic acid', '글루탐산 → α-KG'), explain=key('바로 되는 셋: 글루탐산 → α-KG, 아스파르트산 → OAA, 알라닌 → 피루브산(TCA 아님).'))

add(n=22, sec=9, diff=2, title='케톤·포도당 둘 다 되는 아미노산',
    en=mcq('Which of these amino acids are both ketogenic and glucogenic? 1. Isoleucine 2. Valine 3. Histidine 4. Arginine 5. Tyrosine', ['1 and 5', '1, 3, and 5', '2 and 4', '2, 3, and 4', '2, 4, and 5']),
    ko=mcq('케톤생성 + 포도당생성 둘 다인 것은? 1 Ile 2 Val 3 His 4 Arg 5 Tyr', ['<b>1 · 5</b>', '1·3·5', '2·4', '2·3·4', '2·4·5']),
    answer=ans('A', '1 and 5', 'Ile · Tyr'), explain=key('둘 다 = F · Y · W · I · T. 오직 케톤 = L · K.') + fig(entry_map(), ''))

add(n=25, sec=9, diff=2, title='세린·알라닌·시스테인의 산물',
    en=mcq('The amino acids serine, alanine, and cysteine can be catabolized to yield:', ['fumarate.', 'pyruvate.', 'succinate.', 'α-ketoglutarate.', 'None of the above']),
    ko=mcq('세린 · 알라닌 · 시스테인은 무엇이 되나?', ['푸마르산', '<b>피루브산</b>', '숙신산', 'α-KG', '정답 없음']),
    answer=ans('B', 'pyruvate', '피루브산'), explain=entry_table())

add(n=26, sec=9, diff=2, title='세린·시스테인이 아세틸-CoA가 되기 전',
    en=mcq('Serine or cysteine may enter the citric acid cycle as acetyl-CoA after conversion to:', ['oxaloacetate.', 'propionate.', 'pyruvate.', 'succinate.', 'succinyl-CoA.']),
    ko=mcq('세린·시스테인은 무엇을 거쳐 아세틸-CoA가 되나?', ['OAA', '프로피온산', '<b>피루브산</b>', '숙신산', '숙시닐-CoA']),
    answer=ans('C', 'pyruvate', '피루브산 → (PDH) → 아세틸-CoA'), explain=entry_table())

add(n=29, sec=9, diff=2, title='α-KG가 되는 아미노산',
    en=mcq('Which of these amino acids are converted to α-ketoglutarate? 1. Glycine 2. Glutamate 3. Histidine 4. Arginine 5. Proline', ['1, 3, and 5', '2, 3, and 4', '2, 3, and 5', '2, 3, 4, and 5', '3, 4, and 5']),
    ko=mcq('α-KG가 되는 것은? 1 Gly 2 Glu 3 His 4 Arg 5 Pro', ['1·3·5', '2·3·4', '2·3·5', '<b>2·3·4·5</b>', '3·4·5']),
    answer=ans('D', '2, 3, 4, and 5', 'Glu · His · Arg · Pro'), explain=eq('α-KG = P R H E Q', '프롤린 · 아르기닌 · 히스티딘 · 글루탐산 · 글루타민'))

add(n=30, sec=9, diff=2, title='숙시닐-CoA가 되는 아미노산',
    en=mcq('Which of these amino acids are converted to succinyl-CoA? 1. Isoleucine 2. Valine 3. Methionine 4. Arginine 5. Threonine', ['2 and 4', '2, 3, and 4', '2, 4, and 5', '1 and 5', '1, 3, and 5']),
    ko=mcq('숙시닐-CoA가 되는 것은? 1 Ile 2 Val 3 Met 4 Arg 5 Thr', ['2·4', '2·3·4', '2·4·5', '1·5', '<b>1·3·5</b>']),
    answer=ans('E', '1, 3, and 5', 'Ile · Met · Thr', note='⚠️ 발린(2)도 숙시닐-CoA로 간다(I M T V). 1·2·3·5 보기가 없으니 E가 가장 맞는 답.'),
    explain=eq('숙시닐-CoA = I M T V', '아이소류신 · 메티오닌 · 트레오닌 · 발린'))

add(n=31, sec=9, diff=2, title='OAA가 되는 아미노산',
    en=mcq('Which of these amino acids are converted to oxaloacetate? 1. Asparagine 2. Glutamine 3. Serine 4. Arginine 5. Aspartate', ['2 and 4', '2, 3, and 4', '2, 4, and 5', '1 and 5', '1, 3, and 5']),
    ko=mcq('OAA가 되는 것은? 1 Asn 2 Gln 3 Ser 4 Arg 5 Asp', ['2·4', '2·3·4', '2·4·5', '<b>1 · 5</b>', '1·3·5']),
    answer=ans('D', '1 and 5', 'Asn · Asp'), explain=eq('OAA = N D', '아스파라긴 → 아스파르트산 → OAA'))

add(n=49, sec=9, diff=1, kind='SA', title='한 단계로 피루브산·TCA 중간체가 되는 4개',
    en='<p>Name four amino acids that can be converted in one step into pyruvate or a citric acid cycle intermediate, and name the intermediate.</p>', ko='<p>한 단계로 피루브산이나 TCA 중간체가 되는 아미노산 4개와 그 산물은?</p>',
    answer=sa('Aspartate → oxaloacetate; glutamate → α-ketoglutarate; alanine → pyruvate; serine → pyruvate.', '아스파르트산 → OAA · 글루탐산 → α-KG · 알라닌 → 피루브산 · 세린 → 피루브산(세린 탈수화효소)'),
    explain=key('앞 셋은 아미노기 전이, 세린은 PLP 탈수화효소.'))

add(n=50, sec=9, diff=2, kind='SA', title='중간체별 아미노산 하나씩',
    en='<p>Name one amino acid whose oxidation proceeds via (a) pyruvate; (b) oxaloacetate; (c) α-ketoglutarate; (d) succinyl-CoA; (e) fumarate.</p>', ko='<p>(a) 피루브산 (b) OAA (c) α-KG (d) 숙시닐-CoA (e) 푸마르산을 거치는 아미노산을 하나씩.</p>',
    answer=sa('(a) Ala, Trp, Gly, Ser, Cys, Thr; (b) Asp, Asn; (c) Glu, Gln, Arg, His, Pro; (d) Ile, Thr, Met, Val; (e) Phe, Tyr.', '(a) A C G S T W (b) N D (c) P R H E Q (d) I M T V (e) F Y'), explain=entry_table())

add(n=51, sec=9, diff=2, kind='SA', title='포도당생성 vs 케톤생성 아미노산',
    en='<p>Explain the distinction between glucogenic and ketogenic amino acids in terms of their metabolic fates.</p>', ko='<p>포도당생성 아미노산과 케톤생성 아미노산의 차이를 대사 운명으로 설명하라.</p>',
    answer=sa('Glucogenic amino acids yield pyruvate or 4-/5-carbon citric acid cycle intermediates, which can be substrates for gluconeogenesis. Ketogenic amino acids yield acetyl-CoA or acetoacetyl-CoA, precursors of ketone bodies.', '포도당생성 = 피루브산 · TCA 중간체(C4·C5) → 포도당신생 가능. 케톤생성 = 아세틸-CoA · 아세토아세틸-CoA → 케톤체.'),
    explain=fig(entry_map(), '') + warn('아세틸-CoA는 포도당이 될 수 없다(PDH 비가역, TCA에서 C 2개 다 CO₂로).', '왜?'))

# ================================================================ S11 (10) 경로 상세
add(n=55, sec=10, diff=3, kind='SA', title='프롤린의 분해 경로',
    en='<p>Diagram the degradative pathway from proline to an intermediate of glycolysis or the citric acid cycle. Show intermediates and cofactors.</p>', ko='<p>프롤린 → 해당·TCA 중간체 경로를 중간체와 보조인자와 함께 그려라.</p>',
    answer=sa('Proline → (proline oxidase) Δ¹-pyrroline-5-carboxylate → (spontaneous, + H₂O) glutamate γ-semialdehyde → (NAD(P)⁺) glutamate → (transamination/GDH) α-ketoglutarate.', '프롤린 → 피롤린-5-카복실산 → 글루탐산 γ-세미알데하이드 → 글루탐산 → α-KG'),
    explain=vflow(['프롤린 (고리)', 'Δ¹-피롤린-5-카복실산', '글루탐산 γ-세미알데하이드 (고리 열림, + H₂O)', '글루탐산 (NAD(P)⁺ → NAD(P)H)', 'α-케토글루타르산 (아미노기 전이 / GDH)'], colors=[C['navy'], C['navy'], C['purple'], C['orange'], C['green']], box_h=24, gap=12, width=520, font=10.5, bw=420) + tip('아르기닌도 오르니틴 → 글루탐산 세미알데하이드로 같은 길에 합류.', '연결'))

# ================================================================ S12 (11) 보조인자
add(n=23, sec=11, diff=2, title='THF가 나르는 것',
    en=mcq('Tetrahydrofolate (THF) and its derivatives shuttle ______ between different substrates.', ['electrons', 'H⁺', 'acyl groups', 'one-carbon units', 'NH₂ groups']),
    ko=mcq('THF가 기질 사이에 나르는 것은?', ['전자', 'H⁺', '아실기', '<b>1탄소 단위</b>', 'NH₂기']),
    answer=ans('D', 'one-carbon units', '1탄소 단위'), explain=fig(thf_states(), ''))

add(n=24, sec=11, diff=2, title='THF의 가장 산화된 형태가 아닌 것',
    en=mcq('Which of the following is not a form of the most oxidized state of THF?', ['N¹⁰-formyl THF', 'N⁵,N¹⁰-methenyl THF', 'N⁵,N¹⁰-methylene THF', 'N⁵-formyl THF', 'N⁵-formimino THF']),
    ko=mcq('THF의 가장 산화된 상태가 <b>아닌</b> 것은?', ['N¹⁰-포밀', 'N⁵,N¹⁰-메테닐', '<b>N⁵,N¹⁰-메틸렌</b>', 'N⁵-포밀', 'N⁵-포미미노']),
    answer=ans('C', 'N⁵,N¹⁰-methylene THF', 'N⁵,N¹⁰-메틸렌-THF (중간 산화 상태)', note='원본 보기 기호가 F–J로 잘못 인쇄되어 있어 A–E로 바꿨어.'),
    explain=fig(thf_states(), '') + key('–CH₃(메틸) &lt; –CH₂–(메틸렌) &lt; –CHO 수준(포밀·메테닐·포미미노).'))

# ================================================================ S14 (13) 유전 질환
add(n=27, sec=13, diff=1, title='페닐케톤뇨증(PKU)의 원인',
    en=mcq('The human genetic disease phenylketonuria (PKU) can result from:', ['deficiency of protein in the diet.', 'inability to catabolize ketone bodies.', 'inability to convert phenylalanine to tyrosine.', 'inability to synthesize phenylalanine.', 'production of enzymes containing no phenylalanine.']),
    ko=mcq('PKU의 원인은?', ['단백질 부족', '케톤체 분해 불가', '<b>페닐알라닌 → 티로신 전환 불가</b>', '페닐알라닌 합성 불가', '페닐알라닌 없는 효소']),
    answer=ans('C', 'inability to convert phenylalanine to tyrosine', '페닐알라닌 수산화효소 결핍'), explain=fig(phe_tyr(), '') + warn('이름의 “케톤”은 케톤체가 아니라 <b>페닐피루브산</b>(페닐케톤).', '함정'))

add(n=28, sec=13, diff=1, title='단풍당뇨증(MSUD)의 결함',
    en=mcq('In maple syrup urine disease, the metabolic defect involves:', ['a deficiency of niacin.', 'oxidative decarboxylation.', 'synthesis of branched-chain amino acids.', 'transamination of an amino acid.', 'uptake of branched-chain amino acids into liver.']),
    ko=mcq('단풍당뇨증의 결함은?', ['나이아신 결핍', '<b>산화적 탈카복실화</b>', '가지사슬 AA 합성', '아미노기 전이', '간의 흡수']),
    answer=ans('B', 'oxidative decarboxylation', '가지사슬 α-케토산 탈수소효소 (산화적 탈카복실화)'), explain=key('V·I·L → (아미노기 전이 OK) → α-케토산 → ✕ 탈수소효소 복합체 (PDH와 같은 방식).') + tip('쌓인 α-케토산 때문에 소변에서 단풍시럽 냄새.', '이름'))

add(n=53, sec=13, diff=2, kind='SA', title='소변에 페닐알라닌이 많은 환자',
    en='<p>A lab report shows high phenylalanine and its metabolites in a patient’s urine. What disease would you suspect, and what defect(s) cause it?</p>', ko='<p>소변에 페닐알라닌과 그 대사물이 많다. 어떤 질환이며 원인 결함은?</p>',
    answer=sa('Phenylketonuria — a defect in phenylalanine hydroxylase or in the enzyme that regenerates tetrahydrobiopterin (dihydrobiopterin reductase).', 'PKU — 페닐알라닌 수산화효소 또는 테트라하이드로비오프테린(THBP) 재생효소 결함'),
    explain=fig(phe_tyr(), '') + steps('Phe가 옆길로 넘쳐 페닐피루브산 · 페닐젖산 · 페닐아세트산이 소변에.'))

add(n=54, sec=13, diff=2, kind='SA', title='PKU 어린이의 식단 짜기',
    en='<p>You are formulating the diet for a 4-year-old with phenylketonuria. How do you decide what kind and amount of protein to include?</p>', ko='<p>4살 PKU 아이의 식단에서 단백질 종류와 양은 어떻게 정하나?</p>',
    answer=sa('A growing child needs some Phe (and Tyr) for protein synthesis; give just enough to meet that need but not enough for phenylketones to accumulate. Supplement Tyr (now essential). If the defect is in BH₄ regeneration, L-DOPA and 5-hydroxytryptophan must also be supplied (BH₄ itself is unstable and does not cross the blood–brain barrier).', '성장에 필요한 만큼만 Phe를 주고 넘치지 않게. 티로신은 보충(이제 필수). THBP 재생 결함이면 L-DOPA · 5-하이드록시트립토판도 보충.'),
    explain=key('PKU 환자에게 티로신은 필수 아미노산이 된다.') + warn('아스파탐(Phe 포함) 음료 주의 표시가 붙는 이유.', '생활'))
