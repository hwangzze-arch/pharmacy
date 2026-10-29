from lib import *

def build():
    chapter(7, 'PNS: Efferent Division')
    c = CH['color']
    page('CHAPTER 7', 'The PNS: Efferent Division — 한 장 지도',
        chev([('7.1 ANS 경로', '2-뉴런 사슬', '#7b2a93'), ('교감 vs 부교감', 'NE vs ACh', c), ('수용체·약물', 'N·M·α·β', '#ae3ec9'), ('7.2 체성', '최종 공통 경로', '#862e9c'), ('7.3 NMJ', 'ACh → EPP → AP', '#5f1f73')]) +
        grid('1fr 1fr',
            col(card('한 줄 요약', 'CNS의 명령은 두 길로 나간다: <span class="hy">자율신경(2-뉴런, 신경절 경유) → 심장근·평활근·샘</span>, <span class="hy">체성신경(1-뉴런) → 골격근</span>. 교감 = <span class="hp">투쟁-도피·NE</span>, 부교감 = <span class="hg">휴식-소화·ACh</span>. 골격근은 <b>NMJ</b>에서 ACh → 종판전위 → AP.', 'sum big'),
                card('💡 숫자', '교감 기원 <b>T1–L2</b> · 부신수질 <b>E 80% / NE 20%</b> · 근섬유당 NMJ <b>1개</b> · NMJ <b>9단계</b>', 'tip')),
            card('🎯 교수님 예시문제(Ch 7) 3개 → 정답', tbl(['문제', '정답'], [
                ['The motor-end plate ____.', '<b>contains acetylcholine receptors</b>'],
                ['Innervation by both branches of the ANS ____.', '<b>is dual innervation</b>'],
                ['Which is a function of the sympathetic nervous system?', '<b>Pupil dilation</b>']]) +
                '<p style="margin-top:1.5mm">오답 보기: 심박↓·소화↑·혈압↓·호흡↓ = 모두 <b>부교감 방향</b> / lateral inhibition = 감각계 용어 / Ca<sup>2+</sup> 원천 = <b>SR</b> / NT 방출 = <b>terminal button</b></p>', 'warn')), 'Slides 37–51')

    page('PART 01', '자율신경 경로 — 교감 vs 부교감',
        grid('1fr 1.1fr 1fr',
            col(card('정의', '<b>Efferent division</b> = CNS가 효과기(근육·샘)를 조절하는 고리<br><b>ANS</b> = <span class="hy">불수의</span>: 심장근, 평활근, 대부분 외분비샘, 일부 내분비샘, 지방조직<br><b>Somatic</b> = <span class="hy">수의</span>: 골격근', 'def'),
                card('🔗 2-뉴런 사슬', flow('CNS', '<b>Preganglionic</b>', '자율신경절 (ACh → nicotinic)', '<b>Postganglionic</b>', '효과기', small=True) + '<b>Ganglion</b> = CNS 밖 뉴런 세포체 모임'),
                card('🏃 Adrenal medulla', '<b>변형된 교감신경절</b> — 신경절전 교감 섬유(ACh → nicotinic)가 직접 지배 → 축삭 대신 <b>E(~80%) + NE(~20%)를 혈액으로</b> → 교감 효과 강화·연장', 'tip')),
            card('🆚 교감 vs 부교감', tbl(['', 'Sympathetic', 'Parasympathetic'], [
                    ['기원', '<b>흉·요수 T1–L2</b> (thoracolumbar)', '<b>뇌간 + 천수</b> (craniosacral, 미주신경 X)'],
                    ['신경절', '척수 옆 <b>교감신경절 사슬</b>', '효과기 <b>안·근처</b>(terminal)'],
                    ['신경절전', '<b>짧다</b>', '<b>길다</b>'], ['신경절후', '<b>길다</b>', '<b>짧다</b>'],
                    ['신경절 NT', '<b>ACh → nicotinic</b>', '<b>ACh → nicotinic</b>'],
                    ['신경절후 NT', '<b>Norepinephrine</b> (adrenergic)', '<b>Acetylcholine</b> (cholinergic)'],
                    ['효과기 수용체', '<b>Adrenergic</b> α, β', '<b>Muscarinic</b>'],
                    ['우세 시', '<span class="hp">Fight-or-flight</span>', '<span class="hg">Rest-and-digest</span>']]) +
                '<p style="margin-top:2mm">🧠 교감 = "<b>짧게</b> 출발해 <b>멀리</b>" · 부교감 = "<b>멀리</b> 가서 <b>짧게</b>"<br>⚠ 예외: 교감 → <b>땀샘</b>은 <b>ACh</b>(muscarinic)</p>'),
            img('c6-39', '교감(T1–L2) vs 부교감(뇌간·천수) · 부신수질', '128mm')), 'Slides 37–39')

    page('PART 02', '효과 · 이중 신배 · 수용체 · 약물',
        grid('1.05fr 1fr 1fr',
            card('🐻 vs 🍚 기관별 효과', tbl(['기관', '교감 (곰!)', '부교감 (식후 휴식)'], [
                    ['심장', '심박·수축력 <b>↑</b>', '심박 <b>↓</b>'], ['혈관(대부분)', '수축 → 혈압 ↑ <small>(교감만)</small>', '—'],
                    ['기관지', '<b>확장</b>', '수축'], ['동공', '<b>확대</b>(방사근)', '축소(환상근)'], ['수정체', '먼 곳', '가까운 곳'],
                    ['소화관', '운동·분비 <b>↓</b>', '<b>↑</b>'], ['침', '소량·진함', '다량·묽음'], ['간', '포도당 방출 ↑', '글리코겐 합성'],
                    ['지방', '지방 분해 ↑', '—'], ['방광', '이완(참기)', '수축(배뇨)'], ['땀샘', '분비 ↑ <small>(교감만, ACh)</small>', '—']])),
            col(card('정의', '<b>Dual innervation</b> = 한 기관을 교감·부교감 <b>둘 다</b> 지배 → 대개 <b>반대 효과</b> = <span class="hg">상반 조절(reciprocal control)</span>, 가속페달 + 브레이크. 우세한 쪽이 상태 결정. 예외(교감만): 대부분 혈관, 땀샘, 부신수질', 'def'),
                card('🔑 수용체', tbl(['수용체', '결합', '위치'], [['<b>Nicotinic</b>', 'ACh', '<b>모든 자율신경절</b>, <b>부신수질</b>, <b>NMJ</b>'], ['<b>Muscarinic</b>', 'ACh', '부교감 <b>효과기</b> (+ 땀샘)'], ['α<sub>1</sub>', 'NE &gt; E', '혈관 수축'], ['β<sub>1</sub>', 'NE = E', '<b>심장</b> ↑'], ['β<sub>2</sub>', '주로 E', '<b>기관지</b>·일부 혈관 <b>이완</b>']]))),
            col(card('💊 Agonist vs Antagonist', '<b>Agonist</b> = 같은 반응 — <b>salbutamol(β<sub>2</sub>)</b> → 기관지 확장<br><b>Antagonist</b> = 결합 방해 — <b>atropine</b>(muscarinic 차단 → 동공 확대·침↓), <b>β<sub>1</sub> blocker</b>(심박·혈압↓)', 'why'),
                card('🧠 자율 조절 CNS', '<ul><li><b>척수</b>: 일부 자율 반사(배뇨·배변)</li><li><b>연수</b>: 자율 출력 <b>직접</b></li><li><b>시상하부</b>: 자율·체성·내분비 <b>통합</b></li><li><b>전전두엽</b>: 감정 → 자율 (긴장하면 얼굴 붉음)</li></ul>', 'mint'))), 'Slides 40–43')

    qpage('PART 01–02', '자율신경계 ①',
        MC('Innervation by both branches of the autonomic nervous system ____.', 'ANS 두 분지 모두에 의한 신경 지배는 ____.',
           [('is lateral inhibition', '측방 억제이다'), ('is dual innervation', '이중 신배이다'), ('never occurs in humans', '인간에선 없다'), ('occurs at random because both have the same effect', '같은 효과라 무작위로 일어난다'), ('occurs only in the gastrointestinal system', '위장관에서만 일어난다')], '②',
           '대부분 내장기관, 대개 반대 효과(상반 조절).', stars=1, prof=True),
        MC('Which of these is a function of the sympathetic nervous system?', '교감신경계의 기능은?',
           [('Decreased heart rate', '심박수 감소'), ('Increased digestion', '소화 증가'), ('Decreased blood pressure', '혈압 감소'), ('Pupil dilation', '동공 확대'), ('Decreased breathing', '호흡 감소')], '④',
           '"곰을 만났다" — 나머지는 전부 반대 방향.', stars=1, prof=True),
        TF([('All preganglionic fibers of both divisions release acetylcholine.', '두 분지 모든 신경절전 섬유는 ACh를 방출한다.'),
            ('Sympathetic preganglionic fibers are long; parasympathetic ones are short.', '교감 신경절전은 길고 부교감은 짧다.'),
            ('The adrenal medulla is a modified sympathetic ganglion that secretes E and NE into the blood.', '부신수질은 E·NE를 혈액으로 분비하는 변형된 교감신경절이다.'),
            ('Sympathetic postganglionic fibers to sweat glands release acetylcholine.', '땀샘으로 가는 교감 신경절후 섬유는 ACh를 방출한다.'),
            ('Parasympathetic preganglionic fibers originate from T1–L2.', '부교감 신경절전 섬유는 T1–L2에서 기원한다.')],
           'T F T T F', '(2) 반대: sympathetic pre = <b>short</b>, parasympathetic pre = <b>long</b> (5) → <b>brain stem and sacral</b> cord; T1–L2 = sympathetic.'))

    qpage('PART 02', '자율신경계 ② — 수용체 · 약물',
        MC('Nicotinic receptors are found at which TWO locations? <b>(Choose two.)</b>', '니코틴 수용체가 있는 곳 두 군데는?',
           [('Autonomic ganglia', '자율신경절'), ('Parasympathetic effector organs', '부교감 효과기'), ('Motor end plates of skeletal muscle', '골격근 운동종판'), ('Cardiac muscle (sympathetic)', '심장근(교감)'), ('Bronchiolar smooth muscle', '기관지 평활근')], '①, ③',
           'Nicotinic = 신경절·부신수질·NMJ. ② muscarinic ④ β<sub>1</sub> ⑤ β<sub>2</sub>.', pick=2, stars=3),
        MC('Which TWO effects result from parasympathetic stimulation? <b>(Choose two.)</b>', '부교감 자극의 결과 두 개는?',
           [('Increased digestive motility and secretion', '소화관 운동·분비 증가'), ('Bronchodilation', '기관지 확장'), ('Pupil constriction', '동공 축소'), ('Glucose release from the liver', '간 포도당 방출'), ('Increased heart rate', '심박 증가')], '①, ③', 'Rest-and-digest. 나머지는 교감.', pick=2),
        MC('Atropine blocks ACh at muscarinic receptors. Atropine is therefore ____ and would cause ____.', '아트로핀은 무스카린 수용체에서 ACh를 차단한다. 아트로핀은 ____이며 ____을 일으킨다.',
           [('an agonist; pupil constriction', '작용제; 동공 축소'), ('an antagonist; pupil dilation and decreased salivation', '길항제; 동공 확대·침 감소'), ('an agonist; increased digestion', '작용제; 소화 증가'),
            ('an antagonist; skeletal muscle paralysis', '길항제; 골격근 마비'), ('an antagonist; decreased heart rate', '길항제; 심박 감소')], '②', '부교감 차단 → 교감처럼 보임. 골격근은 <b>nicotinic</b>이라 무관.', stars=3))

    page('PART 03', '체성신경계 · 신경근 접합부(NMJ)',
        grid('1fr 1.05fr 1fr',
            col(card('💪 Somatic nervous system', '<ul><li>운동뉴런 세포체 = <b>척수 전각</b>(또는 뇌간) → <b>하나의 긴 유수 축삭</b> → 골격근</li><li>말단에서 <b>ACh</b> → 수축</li><li><span class="hp">흥분만 가능</span> — 골격근 억제는 <b>CNS 안에서</b> 운동뉴런을 억제해야만</li><li><b>Final common pathway</b> = 다른 신경계가 골격근에 영향 주는 <b>유일한 길</b></li></ul>', 'def'),
                card('🆚 ANS vs Somatic', tbl(['', 'Autonomic', 'Somatic'], [['효과기', '심장·평활근·샘', '골격근'], ['뉴런 수', '<b>2</b>', '<b>1</b>'], ['NT', 'ACh / NE', '<b>ACh만</b>'], ['수용체', 'muscarinic / adrenergic', '<b>nicotinic</b>'], ['효과', '흥분·억제', '<b>흥분만</b>'], ['조절', '불수의', '수의']]))),
            card('⚡ NMJ 9단계', '각 근섬유 <b>NMJ 1개</b> · 말단 = <b>terminal button</b>(ACh 소포) · <b>Motor end plate</b> = 근세포막의 얕은 홈, <b>ACh 수용체</b>' + tbl(['#', '사건'], [
                    ['1', 'AP가 terminal button 도달'], ['2', '전압개폐 <b>Ca<sup>2+</sup></b> 통로 열림'], ['3', 'Ca<sup>2+</sup> 유입 → <b>ACh 세포외유출</b>'],
                    ['4', 'ACh → 종판의 <b>화학개폐 수용체-통로</b>'], ['5', '<b>비특이 양이온</b> 통로 → Na<sup>+</sup> 유입'], ['6', '<b>End-plate potential (EPP)</b> = 등급전위'],
                    ['7', '국소 전류 → <b>인접 막</b> 전압개폐 Na<sup>+</sup> 열림'], ['8', '역치 → <b>근섬유 전체 AP</b>'], ['9', '<b>AChE</b>가 ACh 분해 → 종료']]), 'tip'),
            col(img('c6-51', 'NMJ: Ca²⁺ → ACh → EPP → 근육 AP → AChE', '62mm'),
                card('EPP 포인트', 'EPP는 등급전위지만 매우 커서 <b>항상 역치</b> → 운동뉴런 AP 1회 = 근섬유 AP 1회 (<b>1:1</b>) — CNS 시냅스(가중 필요)와 다름', 'mint'))), 'Slides 45–51')

    page('PART 04', 'NMJ를 건드리는 물질 · 교수님 예시 해부',
        grid('1.2fr 1fr',
            card('☠ 독소 · 약물 · 질환', tbl(['물질·질환', '작용', '결과'], [
                    ['Black widow venom', 'ACh <b>폭발적 방출</b>', '지속 탈분극 → 호흡근 마비'],
                    ['<b>Botulinum toxin</b>', 'ACh <b>방출 차단</b>', '이완성 마비 (보톡스)'],
                    ['<b>Curare</b>', 'nicotinic 수용체 <b>차단</b>(길항제)', '마비 (수술 근이완제 원형)'],
                    ['<b>Organophosphates</b>', '<b>AChE 억제</b>', 'ACh 축적 → 지속 탈분극 → 호흡 마비'],
                    ['<b>Myasthenia gravis</b>', 'ACh 수용체 <b>자가항체</b>', '근력 약화 → AChE 억제제(neostigmine)']]) +
                '<p style="margin-top:2mm">🧠 <b>"방출(보툴) · 수용체(큐라레) · 분해효소(유기인)"</b> — 단계별로 하나씩</p>'),
            col(card('⚠ 교수님 예시: The motor-end plate ____.', '① <b>contains acetylcholine receptors ✔</b><br>② adrenergic ✗ — 골격근 = nicotinic<br>③ 수축용 Ca<sup>2+</sup> 원천 ✗ — <b>근소포체(SR)</b>(8장)<br>④ NT 방출 부위 ✗ — <b>terminal button</b>(종판은 <u>근육</u> 쪽)<br>⑤ 축삭이 세포질로 들어감 ✗ — 틈을 두고 접할 뿐', 'warn'),
                card('정의', '<b>Terminal button</b> = 신경 쪽, ACh 방출 / <b>Motor end plate</b> = 근육 쪽, ACh 수용체 / <b>Synaptic cleft</b> = 사이 틈', 'def'))), 'Slides 48–51')

    qpage('PART 03–04', '체성신경 · NMJ',
        MC('The motor-end plate ____.', '운동종판은 ____.',
           [('contains acetylcholine receptors', 'ACh 수용체를 가진다'), ('contains adrenergic receptors', '아드레날린성 수용체를 가진다'), ('is the source of calcium for muscle contraction', '근수축 칼슘의 원천이다'),
            ('is the region of the motor neuron that releases the neurotransmitter', 'NT를 방출하는 운동뉴런 부위이다'), ('is where axon terminals enter the muscle cell cytoplasm', '축삭 말단이 근세포질로 들어가는 곳이다')], '①',
           '종판 = <b>근육 쪽</b>, nicotinic 수용체.', stars=1, prof=True),
        MC('Which substance causes paralysis by blocking ACh receptors at the motor end plate?', '운동종판의 ACh 수용체를 차단해 마비를 일으키는 물질은?',
           [('black widow venom', '검은과부거미 독'), ('organophosphates', '유기인제'), ('curare', '큐라레'), ('neostigmine', '네오스티그민'), ('botulinum toxin', '보툴리눔 독소')], '③', '보툴리눔은 <b>방출</b> 차단(결과는 같아도 기전 다름).'),
        TF([('Somatic motor neurons can either excite or inhibit skeletal muscle.', '체성 운동뉴런은 골격근을 흥분 또는 억제할 수 있다.'),
            ('The end-plate potential is an action potential that propagates along the end plate.', '종판전위는 종판을 따라 전파되는 AP이다.'),
            ('Each skeletal muscle fiber has only one neuromuscular junction.', '각 골격근 섬유는 NMJ가 하나뿐이다.'),
            ('Acetylcholinesterase is located on the motor end-plate membrane.', 'AChE는 운동종판 막에 있다.'),
            ('Ca<sup>2+</sup> entry into the terminal button triggers ACh release by exocytosis.', '말단으로의 Ca<sup>2+</sup> 유입이 ACh의 세포외유출을 일으킨다.')],
           'F F T T T', '(1) → can only <b>stimulate</b>; inhibition only within the CNS (2) → a <b>graded</b> potential triggering an AP in the <b>adjacent</b> membrane.'))

    qpage('PART 01–04', '단답',
        SA('What enzyme terminates ACh action at the NMJ, and where is it located?', 'NMJ에서 ACh 작용을 끝내는 효소와 위치는?', 'Acetylcholinesterase (AChE), on the motor end-plate membrane', '억제되면(유기인) ACh 축적 → 지속 탈분극.'),
        SA('Why are motor neurons called the "final common pathway"?', '운동뉴런을 왜 "최종 공통 경로"라 부르나?', 'Because the only way other parts of the nervous system can influence skeletal muscle is by acting on these motor neurons.', '피질·소뇌·기저핵·반사 모두 운동뉴런을 거쳐야 함.', stars=2),
        SA('From which CNS regions do (a) sympathetic and (b) parasympathetic preganglionic fibers originate?', '(a) 교감 (b) 부교감 신경절전 섬유의 기원은?', '(a) thoracic and lumbar spinal cord (T1–L2) (b) brain stem and sacral spinal cord', 'thoracolumbar vs craniosacral.'))

    qpage('PART 01 · 03', '서술형',
        ES('Compare the sympathetic and parasympathetic nervous systems: origin, ganglion location, fiber length, neurotransmitters, effector receptors, and overall function.', '교감·부교감을 기원, 신경절 위치, 섬유 길이, NT, 효과기 수용체, 기능 측면에서 비교하시오.',
           'Sympathetic preganglionic fibers originate in the thoracic and lumbar spinal cord (T1–L2), are short, and synapse in the sympathetic ganglion chain; postganglionic fibers are long. Parasympathetic preganglionic fibers originate in the brain stem and sacral cord, are long, and synapse in terminal ganglia in or near the organs; postganglionic fibers are short. In both, preganglionic fibers release ACh onto nicotinic receptors. Most sympathetic postganglionic fibers release norepinephrine onto α/β adrenergic receptors; parasympathetic postganglionic fibers release ACh onto muscarinic receptors. The sympathetic system dominates in "fight-or-flight" (heart rate ↑, bronchodilation, pupil dilation, digestion ↓); the parasympathetic in "rest-and-digest". Most organs receive dual innervation with opposing effects.',
           '6항목 표로 그려도 만점. 부신수질 한 줄 추가 시 가산점.'),
        ES('Describe the sequence of events at the neuromuscular junction from the arrival of an action potential to the termination of ACh activity.', 'AP 도착부터 ACh 작용 종료까지 NMJ의 사건을 순서대로 서술하시오.',
           '(1) An AP reaches the terminal button of the motor neuron. (2) Voltage-gated Ca<sup>2+</sup> channels open. (3) Ca<sup>2+</sup> entry triggers ACh release by exocytosis. (4) ACh binds to chemically gated receptor-channels (nicotinic) on the motor end plate. (5) These nonspecific cation channels open, allowing net Na<sup>+</sup> entry. (6) An end-plate potential (graded) is produced. (7) Local current opens voltage-gated Na<sup>+</sup> channels in the adjacent membrane. (8) The membrane reaches threshold and an AP propagates throughout the muscle fiber. (9) Acetylcholinesterase on the end plate degrades ACh, ending the response.',
           '슬라이드 49–50의 9단계 번호 그대로.'), cols=2)

    memo([('🔗 경로', 'ANS = 2-뉴런(신경절) / Somatic = 1-뉴런<br>교감 T1–L2, 짧은 전·긴 후<br>부교감 뇌간+천수, 긴 전·짧은 후<br>부신수질 = E 80% + NE 20%'),
          ('🔑 NT·수용체', '신경절 = ACh → <b>nicotinic</b> (둘 다)<br>교감 후 = NE → α·β / 부교감 후 = ACh → <b>muscarinic</b><br>땀샘 = 교감인데 ACh<br>β<sub>1</sub> 심장 / β<sub>2</sub> 기관지 이완'),
          ('🐻 효과', '교감: 심박↑ 기관지 확장 동공 확대 소화↓ 포도당↑<br>부교감: 그 반대 + 배뇨<br>Dual innervation = 상반 조절<br>Atropine = muscarinic 길항'),
          ('⚡ NMJ', 'AP → Ca<sup>2+</sup> → ACh → nicotinic → Na<sup>+</sup> → <b>EPP</b> → 인접 막 AP → AChE<br>종판 = 근육 쪽 수용체<br>보툴(방출) · 큐라레(수용체) · 유기인(AChE)')],
         '<ol><li>교감 = <b>동공 확대</b>, 심박↑</li><li>운동종판 = <b>ACh 수용체</b> (방출 ✗)</li><li>체성 운동뉴런 = <b>흥분만</b></li></ol>',
         ['All preganglionic fibers release acetylcholine onto nicotinic receptors; most sympathetic postganglionic fibers release norepinephrine, whereas parasympathetic postganglionic fibers release acetylcholine onto muscarinic receptors.',
          'Dual innervation is the innervation of an organ by both ANS branches, which usually exert opposing effects.',
          'At the NMJ, ACh binds to receptors on the motor end plate, producing an end-plate potential that triggers a muscle action potential; AChE then degrades ACh.'])
