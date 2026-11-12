from lib import *

TOC = [(8, 'Muscle Physiology', '근육 생리학'), (9, 'Cardiac Physiology', '심장 생리학'), (10, 'Blood Vessels & Blood Pressure', '혈관과 혈압')]

def cover(starts):
    rows = ''.join(f'<div class="r"><span>{n:02d}</span><span>{ko} <small style="color:#9fabd2">{en}</small></span><span>{starts.get(n, "")}</span></div>' for n, en, ko in TOC)
    rows += '<div class="r"><span>+</span><span>다음 장은 강의가 끝나는 대로 이어서 추가</span><span></span></div>'
    return f'''<section class="pg cover"><div class="k1">PHAR272 · HUMAN PHYSIOLOGY · 기말고사 대비 노트</div>
<h1>인체생리학<br>기말 8–10장<br><em>마스터 노트</em></h1>
<div class="sub">Muscle → Heart → Blood Vessels &amp; Blood Pressure</div>
<div class="pills"><span>상세요약</span><span>개념문제 44 · T/F 45문장</span><span>2개 고르기 · 그림 각주 · 단어 박스 · 서술</span><span>암기카드</span></div>
<div class="note"><span class="y">기말 범위 = Chapter 8~.</span> 11장 혈액은 강의가 끝나면 이어서 추가.<br>
문제는 <b>영어</b>(긴 문장), 답은 <b>한글</b>. 객관식은 실제 시험처럼 <b>모두 2개 고르기</b>, 보기는 <b>완전한 문장</b>.<br>
시험 유형 그대로: <b>O/X · 2개 고르기 · 그림 각주(A, B, C…) · 단어 박스 빈칸 · 서술형</b>.<br>
10/29 · 11/2 · 11/9 · 11/12 <b>강의 녹취록</b>에서 교수님이 강조한 내용과 마무리 퀴즈를 반영했어.</div>
<div class="toc"><div class="h">CONTENTS</div>{rows}</div>
<div class="strip"><div style="border-color:#c92a2a"><b>8장</b>근육: 근절·교차다리·E-C 연결·대사</div><div style="border-color:#d6336c"><b>9장</b>심장: 박동조율·ECG·주기·CO</div><div style="border-color:#0c8599"><b>10장</b>혈관: 저항·세동맥·모세혈관·MAP</div></div>
<div class="src">Sherwood, Human Physiology: From Cells to Systems · 강의 슬라이드 Ch 8–10 · 강의 녹취록(2026-10-29 ~ 11-12)을 바탕으로 정리 · 그림 © Cengage Learning</div></section>'''
