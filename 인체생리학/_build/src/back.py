from lib import *

def build():
    CH.update(no=0, name='', color='#1d2747')
    pairs = [
        ('Cytoplasm vs Cytosol', '핵 뺀 세포 내부 전부 vs 세포기관을 둘러싼 액체만'),
        ('Lysosome vs Peroxisome', '가수분해효소(분해·자가포식) vs 산화효소+catalase(H<sub>2</sub>O<sub>2</sub>, 해독)'),
        ('Pinocytosis vs RME vs Phagocytosis', 'ECF 비선택 vs 특정 분자 선택(수용체) vs 큰 입자'),
        ('Microtubule vs Microfilament vs IF', '모양·이동(축삭수송·방추사) vs 수축(actin) vs 기계적 스트레스(keratin)'),
        ('Tight vs Desmosome vs Gap', '봉인 vs 리벳(고정) vs 터널(소통)'),
        ('Hypotonic vs Hypertonic', '세포 부풂(용혈) vs 세포 쪼그라듦'),
        ('Channel vs Carrier', '빠름·수동·이온 vs 느림·모양 변화·수동/능동·포화'),
        ('Facilitated vs Primary vs Secondary', 'ATP 없음 vs ATP 직접(Na<sup>+</sup>–K<sup>+</sup> 펌프) vs Na<sup>+</sup> 기울기(SGLT)'),
        ('Symport vs Antiport', '같은 방향 vs 반대 방향'),
        ('E<sub>K</sub> vs E<sub>Na</sub> vs RMP', '−90 vs +60 vs −70 (K<sup>+</sup> 투과도↑ → E<sub>K</sub>에 가까움)'),
        ('Graded vs Action potential', '국소·가변·감쇠·가중 O vs 실무율·재생·불응기·가중 X'),
        ('Absolute vs Relative refractory', '어떤 자극도 X(Na<sup>+</sup> 불활성) vs 강한 자극이면 O'),
        ('Contiguous vs Saltatory', '무수·느림 vs 유수·결절에서 점프·50배 빠름·에너지 절약'),
        ('EPSP vs IPSP', 'Na<sup>+</sup> 유입·탈분극 vs K<sup>+</sup> 유출/Cl<sup>−</sup> 유입·과분극'),
        ('Temporal vs Spatial summation', '같은 입력·빠른 반복 vs 여러 입력·동시'),
        ('Convergence vs Divergence', '많은 → 하나 vs 하나 → 많은'),
        ('Hydrophilic vs Lipophilic hormone', '막 수용체·2차 전령·기존 단백질 vs 세포 내 수용체·유전자·새 단백질'),
        ('Nervous vs Endocrine', 'wired·근접성·빠름·짧음 vs wireless·수용체·느림·김'),
        ('Gray vs White matter', '세포체·시냅스(처리) vs 유수 축삭(전선) · 척수는 배치가 뇌와 반대'),
        ('Oligodendrocyte vs Schwann cell', 'CNS 수초 vs PNS 수초'),
        ('Precentral vs Postcentral gyrus', '1차 운동피질(전두엽) vs 체성감각피질(두정엽)'),
        ("Broca vs Wernicke", '말하기(전두엽) vs 이해(두정·측두·후두 교차)'),
        ('Thalamus vs Hypothalamus', '감각 중계소 vs 항상성 통합·ANS–내분비 연결'),
        ('Hippocampus vs Amygdala', '장기기억 형성 vs 공포·불안'),
        ('Habituation vs Sensitization', 'Ca<sup>2+</sup>↓·NT↓·반응↓ vs 세로토닌·Ca<sup>2+</sup>↑·NT↑·반응↑'),
        ('AMPA vs NMDA', 'Na<sup>+</sup>·EPSP vs Ca<sup>2+</sup>·글루탐산+탈분극 둘 다 필요'),
        ('STM vs LTM', '기존 시냅스 일시 변화 vs 단백질 합성·새 시냅스'),
        ('Dorsal vs Ventral root', '구심(감각) 진입·후근신경절 vs 원심(운동) 출구'),
        ('Ganglion vs Nucleus', 'CNS 밖 세포체 모임 vs CNS 안'),
        ('Nerve vs Tract', 'PNS 축삭 다발 vs CNS 축삭 다발'),
        ('Monosynaptic vs Polysynaptic', '슬개건 반사 vs 사이신경 ≥1(회피반사)'),
        ('Tonic vs Phasic receptor', '느린 적응(근방추·통증) vs 빠른 적응(Pacinian)'),
        ('A-delta vs C fiber', '유수·날카로운 통증 vs 무수·둔한 통증(polymodal)'),
        ('Rods vs Cones', '희미한 빛·흑백·저해상 vs 밝은 빛·색·고해상(중심와)'),
        ('Near vs Far vision', '섬모체근 수축·인대 느슨·렌즈 둥글 vs 이완·팽팽·납작'),
        ('Semicircular canals vs Otolith organs', '회전 가속 vs 직선 가속·중력'),
        ('Inner vs Outer hair cells', '신호를 뇌로 vs 증폭기'),
        ('Taste vs Olfactory receptor', '별도 상피세포(NT 방출) vs 뉴런 자체(2개월 재생)'),
        ('Sympathetic vs Parasympathetic', 'T1–L2·짧은 전/긴 후·NE vs 뇌간+천수·긴 전/짧은 후·ACh'),
        ('Nicotinic vs Muscarinic', '신경절·부신수질·NMJ vs 부교감 효과기'),
        ('Agonist vs Antagonist', '같은 반응 vs 결합 방해'),
        ('Terminal button vs Motor end plate', '신경 쪽(ACh 방출) vs 근육 쪽(ACh 수용체)'),
        ('Botulinum vs Curare vs Organophosphate', 'ACh 방출 차단 vs 수용체 차단 vs AChE 억제'),
    ]
    def ptab(ps):
        return tbl(['쌍', '한 줄 구분'], [[a, b] for a, b in ps])
    n = len(pairs); k = (n + 3) // 4
    page('FINAL', '혼동 쌍 총정리 ① — 1~4장', grid('1fr 1fr', card('', ptab(pairs[:k])), card('', ptab(pairs[k:2 * k]))), 'Confusing pairs')
    page('FINAL', '혼동 쌍 총정리 ② — 4~7장', grid('1fr 1fr', card('', ptab(pairs[2 * k:3 * k])), card('', ptab(pairs[3 * k:]))), 'Confusing pairs')
    nums = [('−70 mV', '뉴런 RMP'), ('−90 / +60 mV', 'E<sub>K</sub> / E<sub>Na</sub>'), ('−50~−55 mV', '역치'), ('+30 mV', 'AP 정점'),
            ('3 Na⁺ : 2 K⁺', '펌프 / ATP 1'), ('300 mOsm', '등장액'), ('200 · 4 · 11', '세포 종류 · 조직 · 계통'), ('80% / 20%', '간질액 / 혈장 (ECF)'),
            ('90%', '교세포 비율'), ('20% / 50%', '뇌 O₂ / 포도당'), ('3억 · 6층', '뇌량 축삭 · 피질'), ('50–70%', '소뇌 뉴런'),
            ('31 / 12쌍', '척수신경 / 뇌신경'), ('8·12·5·5·1', 'C·T·L·S·Co'), ('L1–L2 / L3–L5', '척수 끝 / 요추천자'), ('T1–L2', '교감 기원'),
            ('~50 · 5', '미뢰 세포 · 기본 맛'), ('2개월', '후각 수용기 교체'), ('1개 · 9단계', '근섬유당 NMJ · NMJ 사건')]
    page('FINAL', '꼭 외울 숫자 · 서술형 공식 · 마지막 한 장',
        grid('1fr 1.1fr 1fr',
            card('🔢 숫자 19', tbl(['숫자', '의미'], [[f'<b>{a}</b>', b] for a, b in nums], 'nb')),
            col(card('✍ 서술형 4단 공식', '<ol><li><b>정의</b> — "○○은 ~이다" (요약 카드의 정의 문장 그대로)</li><li><b>기전</b> — 먼저 → 그다음 → 그 결과 (순서대로)</li><li><b>예</b> — "예를 들어 ~" 교재 예 하나</li><li><b>의미</b> — "그래서 ~를 가능하게 한다"</li></ol>', 'engc'),
                card('🔑 핵심어 쓰는 요령', '<ul><li>모범답안 아래 <b>🔑 핵심어</b>가 곧 채점 기준 — 빠지면 감점</li><li>비교 문제는 "A는 ~인 반면, B는 ~이다" 한 문장으로</li><li>방향 단어를 정확히: 증가/감소, 탈분극/과분극, 기울기 아래로/거슬러</li><li>T/F 거짓은 <b>틀린 단어</b>만 찾아 바르게 바꾸기</li><li>"2개 고르기" = 두 개 다 맞아야 점수</li></ul>', 'tip')),
            card('🔥 1~7장을 반사 하나로', '뜨거운 냄비를 만진다 → 피부 <b>침해수용기</b>의 <b>수용기전위</b>(6) → 구심 뉴런 <b>AP</b>(Na<sup>+</sup>/K<sup>+</sup> 통로, 4; 막전위 3) → <b>후근</b>으로 척수 진입 → <b>사이신경</b>에서 EPSP 가중(4·5) → <b>전각 운동뉴런</b> = 최종 공통 경로(7) → <b>NMJ</b>에서 ACh → EPP → 근수축 → 손을 뗀다. 동시에 <b>시상</b> → <b>두정엽 체성감각피질</b>이 "뜨겁다"를 지각(5), 놀라서 <b>교감신경</b>이 심박↑(7). 손의 세포는 다시 안정된 <b>ECF</b> 속에서 산다 — <b>항상성</b>(1).', 'why')), 'Numbers & writing')
