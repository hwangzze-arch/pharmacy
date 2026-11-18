# 표지 + 00 기말 시험 전략
from lib import page, ph

TOC = [('00', '기말 시험 전략 · 출제 힌트', 'Exam strategy', '00'),
       ('01', 'Hit → Lead → 후보물질 · AI', 'Hit to Lead', '01'),
       ('02', '후보물질 선정 · PD · PK', 'Pharmacodynamics · ADME', '02'),
       ('03', '전임상연구 · GLP', 'Preclinical study', '03'),
       ('★', '기말 대비 실전문제', 'Practice exam', 'ex'),
       ('✓', '헷갈리는 쌍 · 암기카드', 'Final review', 'ck')]


def grad(text, c0=(0xc2, 0x41, 0x0c), c1=(0x5b, 0x3f, 0xd6)):
    """그라데이션 제목 — PDF 뷰어(삼성노트 등)에서 깨지지 않게 글자마다 단색으로 보간"""
    vis = [i for i, ch in enumerate(text) if ch != ' ']
    out = []
    for i, ch in enumerate(text):
        if ch == ' ':
            out.append(' ')
            continue
        t = vis.index(i) / max(1, len(vis) - 1)
        col = '#%02x%02x%02x' % tuple(round(c0[k] + (c1[k] - c0[k]) * t) for k in range(3))
        out.append(f'<span style="color:{col}">{ch}</span>')
    return '<span class="t2g">' + ''.join(out) + '</span>'


def add_cover():
    rows = ''.join(f'<div class="row"><span class="n">{n}</span><span class="nm">{ko}<span>{en}</span></span><span class="pgn">{{{k}}}</span></div>' for n, ko, en, k in TOC)
    rows += '<div class="row"><span class="n">+</span><span class="nm">다음 단원<span>강의가 끝나면 이어서 추가</span></span><span class="pgn">–</span></div>'
    page(f'''<div class="cv-left"><div class="cv-k">PHAR278 · NEW DRUG DEVELOPMENT · 기말고사 대비 노트</div>
<div class="cv-h"><span class="t1">신약개발개론</span>{grad("기말 9–12주")}<span class="t3">후보물질 · PD/PK · 전임상 통합 노트</span></div>
<div class="cv-flow">Hit → Lead → 후보물질 → PD · PK(ADME) → 전임상 · GLP</div>
<div class="cv-chips"><span class="cv-chip">단원별 상세요약</span><span class="cv-chip">개념문제 24</span><span class="cv-chip">실전문제 21 (객관식 · O/X · 단답 · 서술)</span><span class="cv-chip">녹취록 3개 반영</span><span class="cv-chip">헷갈리는 쌍 · 암기카드</span></div>
<div class="cv-txt"><span class="r">기말 범위 = 9주차(Virtual screening)~</span> · 10주차 휴강, 13주차 휴강은 전임상 녹화 강의로 보강 → 이어서 추가.<br>
중간 형식: <b>객관식 26 · 단답 14 · 서술 0</b> → 보기는 <b>두 개념 맞바꾸기 · 한 단어 뒤집기</b> 중심.<br>
단원마다 <b>상세요약 → 개념문제</b>, 마지막에 <b>실전문제 → 헷갈리는 쌍 · 암기카드</b>.<br>
교수님이 “예시 문제로 내기 좋다”고 한 건 <b>분홍 태그</b>로 표시했어.</div>
<div class="cv-stats">
<div class="cv-st"><b>3</b><span>주차 반영<br>9 · 11 · 12주차</span></div>
<div class="cv-st"><b>45</b><span>문제<br>개념 24 · 실전 21</span></div>
<div class="cv-st"><b>3</b><span>녹취록<br>11/4 ~ 11/18</span></div>
<div class="cv-st"><b>2</b><span>출제 힌트<br>그래프 · 약물 내성</span></div></div></div>
<div class="cv-toc"><div class="t">CONTENTS</div>{rows}</div>
<div class="cv-parts">
<div class="cv-p" style="border-top-color:#3b6fd8"><div class="a">PART 01 Hit → Lead</div><div class="b">스크리닝 · SAR · Lead 조건 · 후보 조건 · AI</div></div>
<div class="cv-p" style="border-top-color:#0e8a83"><div class="a">PART 02 PD · PK</div><div class="b">Emax · EC50 · 역가/효능 · 내성 · ADME</div></div>
<div class="cv-p" style="border-top-color:#6a4ae0"><div class="a">PART 03 전임상 · GLP</div><div class="b">동물연구 · 탐색적 vs 규제적 · QAU</div></div>
<div class="cv-p" style="border-top-color:#e2553a"><div class="a">★ 실전 · ✓ 암기</div><div class="b">실전 21문항 · 헷갈리는 쌍 TOP 10</div></div>
<div class="cv-p" style="border-top-color:#9aa0b0"><div class="a">다음 단원</div><div class="b">전임상 녹화 강의 · 임상시험 — 이어서 추가</div></div></div>
<div class="cv-src">김한준 교수님 9·11·12주차 강의 슬라이드 · 수업 녹취록(2026-11-04 ~ 11-18) · 주차별 요약정리를 바탕으로 정리</div>''', cls='page cover4')


def add_strategy():
    page(ph('기말', '00', '기말 시험 전략 — 형식 · 출제 패턴 · 교수님 힌트', '시험기록 · 9·11·12주차 녹취') + '''
<div class="body col">
  <div class="row">
    <div class="col" style="flex:1">
      <table class="t">
        <tr><th>항목</th><th>내용</th></tr>
        <tr><td><b>비중</b></td><td>기말 <b>45%</b> (중간 40%)</td></tr>
        <tr><td><b>중간 형식</b></td><td>객관식 26 + 단답 14 = 40문항, <b>서술 없음</b></td></tr>
        <tr><td><b>중간 결과</b></td><td>평균 27.3/40 · 최고 38 · <b>B컷 ≈ 25</b></td></tr>
        <tr><td><b>기말 난이도</b></td><td>교수님: 중간보다 <b>조금 쉽게</b> (F 안 나오게)</td></tr>
        <tr><td><b>범위</b></td><td>9주차(Virtual screening~)부터 · 13주차 휴강은 <b>전임상 녹화 강의</b>로 보강 · 대면 약 2번 남음</td></tr>
      </table>
      <div class="callout memo"><div class="t">📅 이 노트 쓰는 법</div><div class="small">요약정리·녹취록으로 먼저 공부 → 각 PART <b>상세요약</b>으로 정리 → <b>개념문제</b>로 확인 → 마지막 <b>실전문제</b>는 정답 칸 가리고 시간 재서</div></div>
    </div>
    <div class="card" style="flex:1.3;border-color:#f6c7bb"><h3 style="color:var(--coral)">🎯 중간고사 출제 패턴 → 기말에도</h3>
      <table class="t" style="--pcs:var(--coral-s)">
        <tr><th>패턴</th><th>중간 실제 사례 → 기말 예상</th></tr>
        <tr><td><b>① 두 개념 맞바꾸기</b></td><td>엔브렐↔스티렌 · 서방정↔장용정 · 화학상↔물리학상<br>→ <b>Efficacy↔Potency</b> · <b>Phase I↔II</b> · <b>탐색적↔규제적</b></td></tr>
        <tr><td><b>② 한 단어 뒤집기</b></td><td>광유전학 “억제” → <b>흥분</b><br>→ 내성 시 EC50 “감소” → <b>증가</b> · F “IV&lt;1” → <b>IV=1</b></td></tr>
        <tr><td><b>③ 단답 = 정확한 단어</b></td><td>NDA = <b>Application</b>(Approval ✗) · ‘녹차’ ✗ 시네카테킨<br>→ <b>QAU · GLP · BUN · CYP450</b> 풀네임</td></tr>
        <tr><td><b>④ 순서·숫자</b></td><td>생동성: 채혈 → 통계 → <b>판정</b><br>→ Hit μM → Lead 수백 nM → 후보 ≤100 nM · 경구 <b>A-M-D-E</b></td></tr>
      </table></div>
  </div>
  <div class="callout trap" style="border-color:#f5b6cb;background:#fff1f5"><div class="t" style="color:#c2185b">📣 교수님이 직접 짚은 출제 후보</div><div class="small">
    <b>12주차</b> “요런 그래프들 제가 굉장히 좋아한다 … 약물 내성, 항암제 … <b>예시 문제로 내기에 굉장히 좋은 주제</b>” → <span class="p">potency/efficacy 그래프 해석 · 내성 시 EC50·Emax</span><br>
    <b>11주차</b> “그래프에 A, B, C, D … ‘포텐시가 가장 높은 약물’, ‘포텐시 높고 에피커시 낮은 약물을 고르시오’ 이런 식으로 시험 문제가 나갈 수 있다”
  </div></div>
</div>''', style='--pc:var(--navy);--pcs:#efeaff')
