from lib import *

TOC = [(8, 'Muscle Physiology', '근육 생리학'), (9, 'Cardiac Physiology', '심장 생리학'), (10, 'Blood Vessels & Blood Pressure', '혈관과 혈압'), (11, 'The Blood', '혈액'), (13, 'The Respiratory System', '호흡계'), (14, 'The Urinary System', '비뇨계')]

def cover(starts):
    rows = ''.join(f'<div class="row"><span class="n">{n:02d}</span><span class="nm">{ko}<span>{en}</span></span><span class="pgn">{starts.get(n, "")}</span></div>' for n, en, ko in TOC)
    rows += '<div class="row"><span class="n">+</span><span class="nm">소화계<span>강의가 끝나면 이어서 추가 · 기말 범위 끝</span></span><span class="pgn">–</span></div>'
    return f'''<section class="pg cover4">
<div class="cv-left"><div class="cv-k">PHAR272 · HUMAN PHYSIOLOGY · 기말고사 대비 노트</div>
<div class="cv-h"><span class="t1">인체생리학</span><svg class="t2" width="560" height="104" viewBox="0 0 560 104"><defs><linearGradient id="cvg" x1="0" y1="0" x2="1" y2=".35"><stop offset="0" stop-color="#c2410c"/><stop offset="1" stop-color="#5b3fd6"/></linearGradient></defs><text x="0" y="88" fill="url(#cvg)" font-size="100" font-weight="900" letter-spacing="-4">기말 8–14장</text></svg><span class="t3">근육 · 심장 · 혈관 · 혈액 · 호흡 · 비뇨 마스터 노트</span></div>
<div class="cv-flow">근육 수축 → 심장 펌프 → 혈관과 혈압 → 혈액 → 호흡 → 비뇨</div>
<div class="cv-chips"><span class="cv-chip">장별 상세 요약</span><span class="cv-chip">개념문제 72 · T/F 80문장</span><span class="cv-chip">2개 고르기 · 그림 각주 · 단어 박스</span><span class="cv-chip">녹취록 10개 반영</span><span class="cv-chip">장별 암기카드</span></div>
<div class="cv-txt"><span class="r">기말 범위 = 8장 ~ 소화계</span> · 12장 강의 없음 · 마지막 주 내분비계는 범위 아님 · 소화계는 강의 후 추가.<br>
형식: <b>O/X · 2개 고르기(보기 전부 긴 문장) · 그림 각주(A, B, C…) · 단어 박스 빈칸 · 서술형 2</b>.<br>
문제는 <b>영어</b>, 답은 <b>한글</b> · 장마다 <b>요약 → 개념문제 → 암기카드</b>.<br>
교수님 녹취에서 강조한 건 🎯로 표시했어.</div>
<div class="cv-stats">
<div class="cv-st"><b>6</b><span>장<br>근육 ~ 비뇨</span></div>
<div class="cv-st"><b>72</b><span>개념문제<br>정답·오답 이유</span></div>
<div class="cv-st"><b>10</b><span>녹취록<br>10/29 ~ 11/30</span></div>
<div class="cv-st"><b>9</b><span>그림 각주<br>슬라이드 그림</span></div></div></div>
<div class="cv-toc"><div class="t">CONTENTS</div>{rows}</div>
<div class="cv-parts">
<div class="cv-p" style="border-top-color:#c92a2a"><div class="a">8장 근육</div><div class="b">근절 · 교차다리 · E-C 연결 · 대사 · 평활근</div></div>
<div class="cv-p" style="border-top-color:#d6336c"><div class="a">9장 심장</div><div class="b">박동조율 전위 · 전도 · ECG · 주기 · CO</div></div>
<div class="cv-p" style="border-top-color:#0c8599"><div class="a">10장 혈관·혈압</div><div class="b">R ∝ ηL/r⁴ · 세동맥 · 모세혈관 · 정맥 환류</div></div>
<div class="cv-p" style="border-top-color:#e8590c"><div class="a">11장 혈액</div><div class="b">혈장 단백질 · 적혈구·EPO · 백혈구 · 지혈</div></div>
<div class="cv-p" style="border-top-color:#1c7ed6"><div class="a">13장 호흡</div><div class="b">경벽압 · 해리곡선 · CO₂ 운반 · 경동맥체</div></div>
<div class="cv-p" style="border-top-color:#7048e8"><div class="a">14장 비뇨</div><div class="b">GFR · RAAS · 역류 증폭 · 바소프레신</div></div>
<div class="cv-p" style="border-top-color:#9aa0b0"><div class="a">소화계</div><div class="b">강의 후 추가</div></div></div>
<div class="cv-src">Sherwood, Human Physiology: From Cells to Systems · 강의 슬라이드 Ch 8–14 · 강의 녹취록(2026-10-29 ~ 11-30)을 바탕으로 정리 · 그림 © Cengage Learning</div>
</section>'''
