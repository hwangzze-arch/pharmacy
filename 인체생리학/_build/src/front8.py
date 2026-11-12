from lib import *

TOC = [(8, 'Muscle Physiology', '근육 생리학'), (9, 'Cardiac Physiology', '심장 생리학'), (10, 'Blood Vessels & Blood Pressure', '혈관과 혈압')]

def cover(starts):
    rows = ''.join(f'<div class="row"><span class="n">{n:02d}</span><span class="nm">{ko}<span>{en}</span></span><span class="pgn">{starts.get(n, "")}</span></div>' for n, en, ko in TOC)
    rows += '<div class="row"><span class="n">11</span><span class="nm">혈액<span>The Blood — 강의 후 추가</span></span><span class="pgn">–</span></div>'
    return f'''<section class="pg cover2v">
<div class="cv-left"><div class="cv-k">PHAR272 · HUMAN PHYSIOLOGY · 기말고사 대비 노트</div>
<div class="cv-h"><span class="t1">근육 · 심장 · 혈관</span><span class="t2">인체생리학</span><span class="t3"><span class="t3b">기말 8–10장</span> 마스터 노트</span></div>
<div class="cv-flow">근육 수축 → 심장 펌프 → 혈관과 혈압 (MAP = CO × TPR)</div>
<div class="cv-chips"><span class="cv-chip">장별 상세 요약</span><span class="cv-chip">개념문제 44 · T/F 45문장</span><span class="cv-chip">2개 고르기 · 그림 각주 · 단어 박스</span><span class="cv-chip">녹취록 5개 반영</span><span class="cv-chip">장별 암기카드</span></div>
<div class="cv-txt"><span class="r">기말 범위 = Chapter 8~</span> · 11장 혈액은 강의가 끝나면 이어서 추가.<br>
형식: <b>O/X · 2개 고르기(보기 전부 긴 문장) · 그림 각주(A, B, C…) · 단어 박스 빈칸 · 서술형 2</b>.<br>
문제는 <b>영어</b>, 답은 <b>한글</b> · 장마다 <b>요약 → 개념문제 → 암기카드</b>.<br>
교수님 녹취에서 강조한 건 🎯로 표시했어.</div>
<div class="cv-stats">
<div class="cv-st"><b>3</b><span>장<br>근육·심장·혈관</span></div>
<div class="cv-st"><b>44</b><span>개념문제<br>정답·오답 이유</span></div>
<div class="cv-st"><b>5</b><span>녹취록<br>10/29 ~ 11/12</span></div>
<div class="cv-st"><b>6</b><span>그림 각주<br>슬라이드 그림</span></div></div></div>
<div class="cv-toc"><div class="t">CONTENTS</div>{rows}</div>
<div class="cv-parts">
<div class="cv-p" style="border-top-color:#7a1fb0"><div class="a">8장 근육</div><div class="b">근절 · 교차다리 · E-C 연결 · 대사 · 평활근</div></div>
<div class="cv-p" style="border-top-color:#d61f7a"><div class="a">9장 심장</div><div class="b">박동조율 전위 · 전도 · ECG · 주기 · CO</div></div>
<div class="cv-p" style="border-top-color:#a62ac8"><div class="a">10장 혈관·혈압</div><div class="b">R ∝ ηL/r⁴ · 세동맥 · 모세혈관 · 정맥 환류</div></div>
<div class="cv-p" style="border-top-color:#c2185b"><div class="a">시험 형식</div><div class="b">O/X · 2개 고르기 · 그림 각주 · 단어 박스 · 서술 2</div></div></div>
<div class="cv-src">Sherwood, Human Physiology: From Cells to Systems · 강의 슬라이드 Ch 8–10 · 강의 녹취록(2026-10-29 ~ 11-12)을 바탕으로 정리 · 그림 © Cengage Learning</div>
</section>'''
