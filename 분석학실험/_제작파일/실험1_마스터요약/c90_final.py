from parts import *
F = "실험노트 쓰기 전 10분"

pairs = dict(t="r", id="f-pairs", html=f"""
<div class="hd"><span class="bd">최종 정리 ①</span><div class="tt"><h1>혼동 쌍 총정리 · 숫자 카드</h1><div class="sb">Confusing pairs · numbers to remember</div></div><span class="pt">{F}</span></div>
<div class="body"><div class="main"><table class="t">
<tr><th>헷갈리는 쌍</th><th>맞는 쪽</th><th>틀린 쪽(오답 보기)</th></tr>
<tr><td>보정치 부호</td><td><b>실제 부피 − 눈금</b></td><td>눈금 − 실제 부피</td></tr>
<tr><td>실제 부피 계산</td><td>무게 <b>÷</b> 밀도</td><td>무게 × 밀도</td></tr>
<tr><td>검정곡선 축</td><td>x = <b>눈금</b>, y = <b>보정치</b></td><td>x = 보정치, y = 눈금 / y = 무게</td></tr>
<tr><td>TC vs TD</td><td>TC = 부피플라스크(담긴 양) / TD = 뷰렛·피펫(나간 양)</td><td>뷰렛 = TC</td></tr>
<tr><td>뷰렛 속 양 vs 나간 양</td><td>속 양 <b>&gt;</b> 나간 양</td><td>같다 / 나간 양이 더 크다</td></tr>
<tr><td>시차: 아래에서 봄</td><td><b>과대</b>평가</td><td>과소평가</td></tr>
<tr><td>시차: 위에서 봄</td><td><b>과소</b>평가</td><td>과대평가</td></tr>
<tr><td>메니스커스</td><td>오목한 <b>맨 아랫부분</b></td><td>윗가장자리</td></tr>
<tr><td>읽는 자리</td><td><b>0.01 mL</b> (10.00)</td><td>0.1 mL (10.0)</td></tr>
<tr><td>유출 속도</td><td>20 mL/min <b>이하</b>, 똑똑</td><td>이상 / 주르륵</td></tr>
<tr><td>건조</td><td>실온 <b>자연건조</b>, 거꾸로 매달기</td><td>오븐·드라이어 가열 건조</td></tr>
<tr><td>급할 때</td><td>쓸 용액으로 <b>린싱</b></td><td>젖은 채로 사용</td></tr>
<tr><td>세척 순서</td><td>폐액 → 수돗물 → <b>탈이온수 마무리</b></td><td>처음부터 탈이온수만</td></tr>
<tr><td>스톱콕</td><td><b>적당히</b> 조임</td><td>최대한 꽉</td></tr>
<tr><td>적정값 보정</td><td>시작 · 최종 <b>둘 다</b></td><td>최종만</td></tr>
<tr><td>온도와 밀도</td><td>온도 ↑ → 밀도 <b>↓</b> → 부피 ↑</td><td>온도 ↑ → 밀도 ↑</td></tr>
<tr><td>실험일자</td><td><b>실험한 날</b></td><td>노트 쓴 날</td></tr>
</table></div><div class="side">
<div class="card"><div class="ct">🔢 숫자 카드</div><table class="t" style="margin:0">
<tr><td>뷰렛 허용오차</td><td><b>±0.1 mL</b> (20 °C, 또는 ±0.08)</td></tr>
<tr><td>500 mL 부피플라스크</td><td><b>±0.3 mL</b></td></tr>
<tr><td>뷰렛 용량 · 눈금 간격</td><td>50 mL · 0.1 mL</td></tr>
<tr><td>읽는 자리</td><td><b>0.01 mL</b></td></tr>
<tr><td>한 방울</td><td><b>≈ 0.05 mL</b></td></tr>
<tr><td>눈금선 두께</td><td><b>≈ 0.02 mL</b></td></tr>
<tr><td>유출 속도</td><td><b>≤ 20 mL/min</b></td></tr>
<tr><td>측정 간격</td><td>10 mL씩 → 50 mL, <b>2회</b> 반복</td></tr>
<tr><td>물 밀도 19 °C</td><td><b>0.99842</b> g/mL</td></tr>
<tr><td>물 밀도 20 / 25 °C</td><td>0.99821 / 0.99705 g/mL</td></tr>
<tr><td>독성물질 장갑</td><td>2겹</td></tr>
<tr><td>노트 제출</td><td><b>월 18:00</b>, 401호 앞 박스</td></tr>
<tr><td>학기 실험</td><td>7회 = 검정 1 + 적정 4 + 분광 1 + 분리 1</td></tr></table></div>
<div class="card tip"><div class="ct">📌 적정 4종</div>중화 · 침전 · 킬레이트(EDTA) · 산화환원 — 모두 뷰렛, 모두 오늘 검정곡선으로 보정.</div>
</div></div>""")

check = dict(t="r", id="f-check", html=f"""
<div class="hd"><span class="bd">최종 정리 ②</span><div class="tt"><h1>실험노트 No.1 쓰기 체크리스트</h1><div class="sb">Notebook checklist for Experiment 1</div></div><span class="pt">{F}</span></div>
<div class="body"><div class="main">
<div class="sec">📒 내용 (이 순서대로)</div>
<table class="t"><tr><th style="width:24%">항목</th><th>쓸 내용 (이 노트에서)</th></tr>
<tr><td>표지 · 번호</td><td>분석학실험 No.1, 페이지 일련번호, <b>매 페이지 서명</b>, 실험일자 = 실험한 날(목)</td></tr>
<tr><td>제목</td><td>실험 1. 뷰렛의 검정</td></tr>
<tr><td>목적</td><td>제작자의 허용오차 범위 내에서 실제 정확한 부피 측정이 이루어지는지 검정 ({{REF:c-purpose}})</td></tr>
<tr><td>원리</td><td>V = m/ρ, TC/TD, 보정치 = 실제 − 눈금 ({{REF:c-principle}} · {{REF:c-tctd}} · {{REF:c-corr}})</td></tr>
<tr><td>시약 및 기구</td><td>buret 50 mL &amp; stand, buret holder, Erlenmeyer flask 100 mL, beaker 100 mL, washing bottle, chemical balance, 탈이온수</td></tr>
<tr><td>방법 (과거형)</td><td>누출 확인 → 기포 제거 → 0.00 맞춤 → 빈 플라스크 무게 → 10 mL씩 누적, 같은 저울 → 50 mL ({{REF:c-proc}})</td></tr>
<tr><td>결과</td><td><b>수온 __ °C, ρ = ____ g/mL</b> 명시 · Table I(눈금, 총무게, 물 무게, 실제 부피, 보정치) · Figure 1 검정곡선 (x = 눈금, y = 보정치)</td></tr>
<tr><td>고찰 · 결론</td><td>±0.1 mL 이내 판정 · 보정치 부호 해석 · 오차 원인(시차·기포·유출 속도·온도·칭량) · 반복 횟수 · 다음 적정에서 보정 방법 ({{REF:c-curve}} · {{REF:c-use}})</td></tr></table>
</div><div class="side">
<div class="card trap"><div class="ct">✍️ 형식 (감점 방지)</div><ul style="margin:0">
<li>□ <b>볼펜</b>만 (연필·지우개·화이트 X)</li><li>□ 틀리면 <b>두 줄 + 서명</b></li><li>□ 남는 공간 <b>사선 + “여백”</b></li>
<li>□ 출력물 <b>4면 부착 + 간인</b></li><li>□ 표 = Table I, 그림 = Figure 1 번호·제목</li><li>□ 서론은 핸드아웃 정리, 참고문헌 X</li></ul></div>
<div class="card tip"><div class="ct">📬 제출</div><b>다음 주 월요일 18:00까지</b><br>401호(교수님 실험실) 앞 박스</div>
<div class="card"><div class="ct">🔎 데이터 확인</div>녹취록 숫자 대신 <b>단톡방 기록지 사진</b> 값으로. 1회만 측정했다면 그 사실을 고찰에.</div>
</div></div>""")

E = [pairs, check]
