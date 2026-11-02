from lib import *

TOC = [(1, 'Physiology & Homeostasis', '생리학 개론과 항상성'), (2, 'Cell Physiology', '세포 생리학'),
       (3, 'Plasma Membrane & Membrane Potential', '세포막과 막전위'), (4, 'Neural & Hormonal Communication', '신경·호르몬 소통'),
       (5, 'Central Nervous System', '중추신경계'), (6, 'PNS: Afferent & Special Senses', '구심성 분과·특수감각'),
       (7, 'PNS: Efferent Division', '원심성 분과')]

def cover(starts):
    rows = '<div class="r"><span>00</span><span>한 장 지도 · 시험 형식</span><span>2</span></div>'
    rows += ''.join(f'<div class="r"><span>{n:02d}</span><span>{ko} <small style="color:#9fabd2">{en}</small></span><span>{starts.get(n, "")}</span></div>' for n, en, ko in TOC)
    rows += f'<div class="r"><span>✓</span><span>혼동 쌍 총정리 · 숫자 · 서술형 공식</span><span>{starts.get(99, "")}</span></div>'
    return f'''<section class="pg cover"><div class="leaves"><svg viewBox="0 0 100 100" style="width:34mm;left:150mm;top:118mm;transform:rotate(18deg);opacity:0.35"><path d="M50 4 L58 28 L80 20 L71 44 L96 50 L73 60 L81 81 L56 71 L53 96 L47 96 L44 71 L19 81 L27 60 L4 50 L29 44 L20 20 L42 28 Z" fill="#f4a582"/></svg><svg viewBox="0 0 100 100" style="width:22mm;left:120mm;top:150mm;transform:rotate(-25deg);opacity:0.3"><path d="M50 4 L58 28 L80 20 L71 44 L96 50 L73 60 L81 81 L56 71 L53 96 L47 96 L44 71 L19 81 L27 60 L4 50 L29 44 L20 20 L42 28 Z" fill="#f9c784"/></svg><svg viewBox="0 0 100 100" style="width:18mm;left:262mm;top:128mm;transform:rotate(40deg);opacity:0.32"><path d="M50 4 L58 28 L80 20 L71 44 L96 50 L73 60 L81 81 L56 71 L53 96 L47 96 L44 71 L19 81 L27 60 L4 50 L29 44 L20 20 L42 28 Z" fill="#ef8f6b"/></svg><svg viewBox="0 0 100 100" style="width:26mm;left:232mm;top:150mm;transform:rotate(-10deg);opacity:0.28"><path d="M50 4 L58 28 L80 20 L71 44 L96 50 L73 60 L81 81 L56 71 L53 96 L47 96 L44 71 L19 81 L27 60 L4 50 L29 44 L20 20 L42 28 Z" fill="#f7b27a"/></svg><svg viewBox="0 0 100 100" style="width:14mm;left:96mm;top:8mm;transform:rotate(30deg);opacity:0.3"><path d="M50 4 L58 28 L80 20 L71 44 L96 50 L73 60 L81 81 L56 71 L53 96 L47 96 L44 71 L19 81 L27 60 L4 50 L29 44 L20 20 L42 28 Z" fill="#f4a582"/></svg><svg viewBox="0 0 100 100" style="width:12mm;left:185mm;top:40mm;transform:rotate(-35deg);opacity:0.25"><path d="M50 4 L58 28 L80 20 L71 44 L96 50 L73 60 L81 81 L56 71 L53 96 L47 96 L44 71 L19 81 L27 60 L4 50 L29 44 L20 20 L42 28 Z" fill="#f9c784"/></svg></div><div class="k1">PHAR272 · HUMAN PHYSIOLOGY · 시험대비 노트</div>
<h1>인체생리학<br>1–7장 통합<br><em>마스터 노트</em></h1>
<div class="sub">Homeostasis → Cell → Membrane → Neuron → CNS → PNS</div>
<div class="pills"><span>상세요약</span><span>개념문제 104 · T/F 110문장</span><span>영어 문제 + 한글 번역</span><span>장별 암기카드</span></div>
<div class="note"><span class="y">중간고사 범위 = Chapter 1–7.</span> 문제는 <b>영어</b>, 답은 <b>한글</b>로 정리, 90분.<br>
형식: <b>T/F · 객관식(5지선다 중 1개 또는 2개) · 단답형 · 서술형</b>.<br>
각 장은 <b>요약 페이지 → 개념문제 페이지</b>가 번갈아 나오고, 장 끝에 <b>암기카드</b>.<br>
교수님 예시문제 10개는 <b>그대로</b> 넣고 「교수님 예시」로 표시, Ch 2 "Points to think" 3문항은 서술형으로 반영했어.</div>
<div class="toc"><div class="h">CONTENTS</div>{rows}</div>
<div class="strip"><div style="border-color:#0b8f84"><b>1장</b>항상성</div><div style="border-color:#2b8a3e"><b>2장</b>세포</div><div style="border-color:#1971c2"><b>3장</b>막·막전위</div><div style="border-color:#5f3dc4"><b>4장</b>신경·호르몬 신호</div><div style="border-color:#c2255c"><b>5장</b>중추신경계</div><div style="border-color:#e8590c"><b>6장</b>감각·구심</div><div style="border-color:#9c36b5"><b>7장</b>자율·체성·NMJ</div></div>
<div class="src">Sherwood, Human Physiology: From Cells to Systems · 강의 슬라이드 Ch 1–7 · 교재 연습문제 · 교수님 예시문제(Ch 2·5·6·7)를 바탕으로 정리 · 그림 © Cengage Learning</div></section>'''

def build():
    CH.update(no=0, name='', color='#1d2747')
    body = chev([('1 항상성', '왜 지키나', '#0b8f84'), ('2 세포', '누가 일하나', '#2b8a3e'), ('3 막·막전위', '경계와 전기', '#1971c2'),
                 ('4 신호', '어떻게 말하나', '#5f3dc4'), ('5 CNS', '통합 본부', '#c2255c'), ('6 PNS 구심', '감각 입력', '#e8590c'), ('7 PNS 원심', '명령 출력', '#9c36b5')])
    body += grid('1.05fr 1fr',
        col(card('한 줄 요약', '몸은 <b>세포가 사는 바닷물(ECF)</b>을 일정하게 지킨다(1). 그 일은 <b>세포</b>가 하고(2), 세포는 <b>막</b>으로 안팎을 나누고 이온 불균형으로 <b>막전위</b>를 만든다(3). 뉴런은 막전위를 흔들어 <b>활동전위</b>로, 내분비세포는 <b>호르몬</b>으로 말한다(4). 정보는 <b>CNS</b>에서 통합되고(5), <b>감각 → 구심</b>으로 들어와(6) <b>원심 → 효과기</b>로 나간다(7).', 'sum big'),
            card('이 문서 사용법', '<ol><li>요약 페이지를 한 번 정독 → 바로 다음 <b>개념문제</b>로 확인</li><li>문제는 <b>영어 → 한글 번역 → ✎ 내 풀이 → 정답·해설</b> 순서. 정답 줄을 손으로 가리고 풀기</li><li><b>✍ 서술형 핵심 문장</b> 카드는 그대로 외워 두면 서술형 뼈대가 되는 문장</li><li>장 끝 <b>암기카드</b> + 마지막 <b>혼동 쌍 총정리</b>는 시험 직전 10분용</li></ol>', 'tip', '💡')),
        col(card('🎯 시험 형식 → 이 노트의 문제 유형', tbl(['시험 형식', '노트 표시', '공략법'], [
                ['True / False', '<span class="qt" style="background:#0b8f84">T / F</span>', '거짓이면 <b>왜 틀렸는지</b>(어느 단어가 틀렸는지) 해설로 확인'],
                ['객관식 (1개 고르기)', '<span class="qt" style="background:#1971c2">객관식</span>', '교수님 예시 = 테스트뱅크형 빈칸 "____." 완성'],
                ['객관식 (2개 고르기)', '<span class="qt" style="background:#5f3dc4">객관식 · 2개</span>', '두 개 모두 맞아야 점수 → 소거법'],
                ['단답형', '<span class="qt" style="background:#e8590c">단답</span>', '🔑 <b>핵심어</b>를 빠짐없이'],
                ['서술형', '<span class="qt" style="background:#c92a2a">서술</span>', '정의 → 기전(순서) → 예 → 의미 4단 + 🔑 핵심어']]), 'warn'),
            card('⚠ 슬라이드 자체의 오류 — 교재 기준으로 외우기', '<ul><li><b>5장 슬라이드 10</b>: Interneuron과 Efferent neuron 설명이 <b>뒤바뀌어</b> 있음</li><li><b>7장 슬라이드 37</b>: "Skeletal muscle is innervated by PNS" → 정확히는 <b>somatic nervous system</b></li><li><b>7장 슬라이드 50</b>: "acetylcholinerase" → <b>acetylcholinesterase (AChE)</b></li></ul>', 'mint')))
    page('MAP', '한 장 지도 — 1~7장은 하나의 이야기', body, 'Chapter 1–7 overview')
