# 중간고사 총정리 + 통합 모의고사 HTML 생성
FOOT = '신약개발개론 · 중간고사 총정리'
pages = []
def page(inner, cls='page', style='', pn=None):
    pages.append((cls, style, inner))

def ph(wk, part, ttl, src=''):
    return f'<div class="ph"><span class="wk">{wk}</span><span class="part">{part}</span><span class="ttl">{ttl}</span><span class="sp"></span>' + (f'<span class="src">{src}</span>' if src else '') + '</div>'

WK = {1:'1주 오리엔테이션',2:'2주 역사',3:'3주 분류',4:'4주 분류2·mRNA',5:'5주 노벨2',6:'6주 후보물질'}
def wtag(w): return f'<span class="src2024" style="background:#e9ecf5;color:#22305a">{WK[w]}</span>'

def mc(no, w, stem, opts, ans, why, src=False, h=8):
    o = ''.join(f'<li>{x}</li>' for x in opts)
    s = '<span class="src2024">2024 기출변형</span>' if src else wtag(w)
    return f'''<div class="q"><div class="q-h"><span class="q-no">{no}</span><span class="tag mc">객관식</span>{s}</div>
      <div class="q-b"><div class="stem">{stem}</div><ol class="opt">{o}</ol></div>
      <div class="blank" style="height:{h}mm"></div>
      <div class="ans"><div class="a"><span class="pill">정답</span><span class="v">{ans}</span></div><div class="why small">{why}</div></div></div>'''

def sa(no, w, stem, ans, src=False, h=10):
    s = '<span class="src2024">2024 기출</span>' if src else wtag(w)
    return f'''<div class="q"><div class="q-h"><span class="q-no">{no}</span><span class="tag sa">단답</span>{s}</div>
      <div class="q-b"><div class="stem">{stem}</div></div>
      <div class="blank" style="height:{h}mm"></div>
      <div class="ans"><div class="small">{ans}</div></div></div>'''

def es(no, stem, ans, tag, h=30):
    return f'''<div class="q"><div class="q-h"><span class="q-no">{no}</span><span class="tag es">서술</span>{tag}</div>
      <div class="q-b"><div class="stem">{stem}</div></div>
      <div class="blank" style="height:{h}mm"></div>
      <div class="ans"><div class="a"><span class="pill">모범답안</span></div>{ans}</div></div>'''

# ---------------- COVER ----------------
page('''<div class="in">
  <div class="sub">PHAR278 · 신약개발개론 · 시험대비 노트</div>
  <h1>중간고사<br>총정리 +<br>통합 모의고사<small>1~6주차 (6주차는 p.33 HTS까지)</small></h1>
  <div class="pills"><span>시험 전략</span><span>2024 기출 지도</span><span>주차별 1장 요약</span><span>함정 비교 · 연표 · 숫자</span><span>모의고사 41문항</span></div>
  <div style="margin-top:7mm;max-width:132mm;font-size:10.5pt;line-height:1.75;opacity:.92">
    주차별 노트를 다 본 뒤 <b style="color:#ffd76a">시험 전 2~3일</b>에 쓰는 마무리용이야.<br>
    앞은 <b>“한 번에 훑기”</b>, 뒤는 <b>실제 시험처럼 섞어 낸 모의고사</b>. 틀린 문제엔 주차 표시가 있으니 그 주차 노트로 돌아가면 돼.
  </div>
  <div class="toc"><h4>CONTENTS</h4><ol>
    <li><span>00</span>시험 전략 · 출제 패턴<em>2</em></li>
    <li><span>01</span>2024 기출 전 문항 지도<em>3</em></li>
    <li><span>02</span>주차별 1장 요약 (1~6주)<em>4</em></li>
    <li><span>03</span>헷갈리는 쌍 TOP 20<em>10</em></li>
    <li><span>04</span>통합 연표 · 숫자 총정리<em>11</em></li>
    <li><span>★</span>통합 모의고사 41문항<em>13</em></li>
    <li><span>✓</span>정답표 · D-day 1장<em>24</em></li>
  </ol></div>
  <div class="foot">김한준 교수님 1~6주차 강의 슬라이드 + 2024 중간고사 리뷰 녹취 + 주차별 상세요약 노트를 바탕으로 정리</div>
</div>''', cls='page cover')

# ---------------- 00 전략 ----------------
page(ph('총정리','00','시험 전략 — 형식 · 출제 패턴 · 공부 순서','2024 리뷰 녹취') + '''
  <div class="body col">
    <div class="card" style="padding:2mm 3mm"><div data-d="flow"></div></div>
    <div class="row">
      <div class="col" style="flex:1">
        <table class="t">
          <tr><th>항목</th><th>내용</th></tr>
          <tr><td><b>형식</b></td><td>단답식 · 객관식 · O/X · 서술형 혼합</td></tr>
          <tr><td><b>배점</b></td><td>중간 <b>40%</b> (2024: 40점 만점) · 기말 45%</td></tr>
          <tr><td><b>범위</b></td><td>1~6주차 강의자료 · 6주차는 <span class="p">p.33 (HTS)까지</span></td></tr>
          <tr><td><b>2024 구성</b></td><td>객관식 약 17 + 약어·단답 + 서술(서방정/장용정, “5개 쓰기”)</td></tr>
        </table>
        <div class="callout memo"><div class="t">📅 시험 전 공부 순서</div><div class="small"><b>D-3</b> 주차별 1장 요약 + 2024 기출 지도 → <b>D-2</b> 모의고사 풀기 → 틀린 주차 노트 복습 → <b>D-1</b> 헷갈리는 쌍 · 숫자 · D-day 1장</div></div>
      </div>
      <div class="card" style="flex:1.25;border-color:#f6c7bb"><h3 style="color:var(--coral)">🎯 교수님 출제 패턴 5가지 (2024)</h3>
        <table class="t" style="--pcs:var(--coral-s)">
          <tr><th>패턴</th><th>실제 사례</th></tr>
          <tr><td><b>① PPT 문장 + 한 단어 뒤집기</b></td><td>허들 실패 비율 “감소” → <b>증가</b> · 엘릭서 “간독성” → <b>신장독성</b> · mRNA “백신에서 더 호의적” → <b>종양학계</b></td></tr>
          <tr><td><b>② 비슷한 용어 바꿔치기</b></td><td>전임상 후 “NDA” → <b>IND</b> · 헬싱키 ↔ 벨몬트 · 화학상 ↔ 물리학상</td></tr>
          <tr><td><b>③ 약어 풀네임</b></td><td>IMD · API (철자 조금 틀려도 인정)</td></tr>
          <tr><td><b>④ 구체적 이름</b></td><td>조인스 vs 프로스판 · 켈시 · 설파닐아마이드</td></tr>
          <tr><td><b>⑤ 서술 = 기준 명시</b></td><td>서방정 = <b>천천히</b> / 장용정 = <b>장에서</b> (“제형 차이” ✗) · “5개” 1개 부족 −1점</td></tr>
        </table></div>
    </div>
  </div>''', style='--pc:var(--navy);--pcs:#e9ecf5')

# ---------------- 01 기출 지도 ----------------
rows = [
 ('1','허들(신약개발의 어려움)','2','통과 못하는 비율·환자 모집 비용 = <b>증가</b> 추세'),
 ('2','IND vs NDA','1·2·6','전임상 후 임상 진입 = <b>IND</b> · 3상 후 = <b>NDA</b> · 라벨링 후 시설 실사 · 4상'),
 ('3','헬싱키 선언','2','치료적·비치료적 연구 원칙 · “존중·이익·정의”는 <b>벨몬트</b>'),
 ('4','바이오 세대','3','1세대 단백질 → 2세대 <b>항체</b> → 3세대 <b>세포·유전자</b> (출제 실수로 전원 정답)'),
 ('5','천연물신약','3','위령선·괄루근·하고초 골관절염 = <b>조인스정</b> (프로스판 ✗) · 스티렌 = 애엽 위염'),
 ('6','천연물 임상','3','합성신약과 <b>동일하게 엄격</b>한 임상'),
 ('7','개량신약 예','3','용도변경·API 변경·용량·복합요법·새 인구집단 = 모두 신약 · 임상 면제는 <b>제네릭뿐</b>'),
 ('8','mRNA 역사','4','“백신에서 더 호의적” ✗ → <b>종양학계</b> 쪽이 더 호의적'),
 ('9','Ψ mRNA','4','단백질 생성량 “차이 없음” ✗ → <b>10~11배</b>'),
 ('10','2024 노벨상 · AlphaFold','5','구조 예측 = <b>화학상</b> · 신경망 = <b>물리학상</b> · 부착 사이트 예측 ✗'),
 ('11','microRNA','5','<b>헤어핀</b> → mRNA에 붙어 기능 억제 = 맞는 설명'),
 ('12','벨몬트 보고서','2','터스키기 · Acres of Skin(피부) · 유대인 병원(암세포) → 벨몬트'),
 ('14·15','탈리도마이드','2','<b>지금도 사용</b>(골수종) · 임부 금기 · 심사관 <b>켈시</b>'),
 ('16','mRNA 서열 설계','4','<b>아직 해결할 문제</b> (코돈 조합 다양) = 맞는 설명'),
 ('17','엘릭서 설파닐아마이드','2','DEG → <b>신장독성</b> (간독성 ✗)'),
 ('18','약어','1·3','<b>IMD</b> Incrementally Modified Drug · <b>API</b> Active Pharmaceutical Ingredient'),
 ('19','제네릭 요건','3','<b>생물학적 동등성 시험</b>'),
 ('20','A·B 약물','2·6','페니실린과 헷갈리게 → 정답 <b>설파닐아마이드</b> (도마크·프론토실)'),
 ('21','바이오 핵심기술','3','<b>유전자재조합</b> · <b>하이브리도마</b>'),
 ('30','서방정 vs 장용정','3','서방 = <b>천천히</b> 용출 / 장용 = <b>장에서</b> 용출'),
]
tr = ''.join(f'<tr><td class="c"><b>{a}</b></td><td><b>{b}</b></td><td class="c">{c}주</td><td>{d}</td></tr>' for a,b,c,d in rows)
page(ph('총정리','01','2024 중간고사 — 전 문항 지도','녹취 정리본 문항별 핵심') + f'''
  <div class="body row">
    <div class="col" style="flex:2.4">
      <table class="t" style="font-size:8.2pt;line-height:1.3;--pcs:var(--coral-s)"><tr><th class="c">#</th><th>주제</th><th class="c">주차</th><th>정답 포인트 (교수님 해설)</th></tr>{tr}</table>
    </div>
    <div class="col" style="flex:1">
      <div class="callout trap"><div class="t">📊 주차별로 세면</div><div class="small"><b>2주(역사)</b> 7문항 — 최다<br><b>3주(분류)</b> 7문항<br><b>4주(mRNA)</b> 3문항<br><b>5주(노벨2)</b> 2문항<br><b>1주</b>는 IND·약어로 연결<br>6주(후보물질)는 <b>새로 추가</b>된 범위</div></div>
      <div class="callout tip"><div class="t">💡 읽는 법</div><div class="small">번호는 녹취 해설 순서 (30번만 실제 번호). 13번(투여 경로)은 “거의 다 맞힘”이라 생략.<br>녹음이 첫 문항 중간부터라 앞 문항 일부는 빠져 있어.</div></div>
      <div class="callout memo"><div class="t">✍ 2026 예상</div><div class="small">같은 문장 뒤집기 + <b>6주차</b> 순서·정의(Target → Hit, Forward/Reverse, TPP)와 <b>2025·2026 노벨상</b>이 새로 들어올 가능성 ↑</div></div>
    </div>
  </div>''', style='--pc:var(--coral);--pcs:var(--coral-s)')

# ---------------- 02 주차별 1장 ----------------
def wpage(w, ttl, color, cols, trap):
    cards = ''
    for col in cols:
        cards += '<div class="col">' + ''.join(f'<div class="card" style="border-top:4px solid var(--{c})"><h3>{h}</h3><div class="small">{b}</div></div>' for h,c,b in col) + '</div>'
    page(ph(f'{w}주차','02',ttl,f'{w}주차 노트 요약') + f'''
  <div class="body col"><div class="grid3" style="flex:1">{cards}</div>
  <div class="callout trap"><div class="t">⚠ {w}주차 함정</div><div class="small">{trap}</div></div></div>''', cls='page big xl wsum', style=f'--pc:var(--{color});--pcs:var(--{color}-s)' if color!='navy' else '--pc:var(--navy);--pcs:#e9ecf5')

wpage(1,'1주차 오리엔테이션 — 정의 · 깔때기 · 임상 · 약어','navy',[
 [('📜 약사법 2조','navy','<b>4호 의약품</b>: 약전 / 진단·치료·예방 / 약리 영향 (기구·장치 ✗)<br><b>8호 신약</b>: 전혀 새로운 신물질 + 신물질 복합제 (식약처장 지정)'),
  ('🔻 깔때기','blue','FDA: <b>5,000~10,000 → 250 → 5 → 1</b><br>3~6 + 6~7 + 0.5~2 = <b>10~15년</b><br>한국: 10,000 → 50 → 5 → 1')],
 [('🚪 관문 순서','teal','전임상 → <span class="y">IND</span> → 임상 1·2·3 → <span class="y">NDA</span> → 라벨링 → 시설 실사 → 승인 → 4상<br>식약처 관장 = 임상시험 신청 ~ 시판 후 조사'),
  ('🧪 임상 한 단어','violet','0상 미량·PK · <b>1상 안전성</b>(건강인 20~100) · <b>2상 용량·유효성</b>(100~500) · <b>3상 대규모 확증</b>(1,000~5,000) · <b>4상 시판 후</b>')],
 [('🔤 약어','amber','IND Investigational New Drug · NDA New Drug Application<br><b>IMD</b> Incrementally Modified Drug · <b>API</b> Active Pharmaceutical Ingredient<br>GLP 비임상 · GCP 임상 · GMP 제조 · CRO · CDMO · ADC'),
  ('🇰🇷 국산 신약 · AI','coral','1호 <b>선플라주</b>(SK·위암·1999) · 첫 FDA <b>팩티브</b>(LG·2003) · 36호 엔블로(2022)<br>AI: 기존 ~10.5~18년 → 6~9년 (앞단 크게 ↓, 허가 그대로)')],
],'전임상 다음은 <b>IND</b> (NDA ✗) · 복제 3형제: Generic(합성·동일·생동성) / Biosimilar(바이오·유사) / Biobetter(바이오·개량) · 임상 의무 없는 건 <b>제네릭뿐</b>')

wpage(2,'2주차 약물개발의 역사 — 최초 · 실패 · 법 · 윤리','coral',[
 [('🏆 최초들','coral','백신 제너 1796 · 항생제 플레밍 1928<br>합성 항균제 <b>도마크 1935</b>(프론토실) · 화학 항암제 1943<br>인간 인슐린 1978 · 표적 항암제 1999 · CAR-T 2017'),
  ('🚧 허들 4개 · 숫자','blue','안전성 · 유효성 · 품질 · 비용효과성(급여)<br>허들 탈락 5.7 → 26.4% (<span class="p">증가</span>)<br>1상 → 승인 9.6% · 최저 2상 30.7% · 2·3상 실패 1위 = 효능 부족')],
 [('💥 실패 · 비극','violet','<b>엘릭서</b>: DEG → <span class="p">신장독성</span> · 105명 → <b>1938 FD&amp;C</b>(안전성)<br><b>탈리도마이드</b>: 1만+ 기형 · <b>켈시</b> 거부 → <b>1962 케파우버-해리스</b>(유효성·사전승인)<br>지금도 사용(골수종) · 임부 금기 · 바이옥스 = 승인 취소'),
  ('⚖ 법 연표','teal','1906 순정식품의약법(와일리) · 1938 FD&amp;C · 1962 K-H · 1992 PDUFA · 1997 FDAMA · 2022 현대화법 2.0(동물실험 의무 폐지)')],
 [('🤝 윤리 3문서','amber','<b>1947 뉘른베르크</b> 자발적 동의<br><b>1964 헬싱키</b> 치료적·비치료적 · IRB<br><b>1979 벨몬트</b> 인간 존중 · 이익 · 정의'),
  ('🚫 남용 사례 → 벨몬트','navy','터스키기(흑인 매독, 페니실린 있어도 치료 ✗)<br><b>Acres of Skin</b> = 감옥 피부 화학물질<br><b>유대인 병원</b> = 노인에 암세포')],
],'존중·이익·정의 = <b>벨몬트</b> (헬싱키 ✗) · 엘릭서 = <b>신장</b> · 탈리도마이드 = <b>지금도 사용</b> · 허들·환자 모집 비용 = <b>증가</b> · 플레밍 콧물 = 라이소자임')

wpage(3,'3주차 신약의 분류 — 합성 · 바이오 · 천연물 · 개량 · 제네릭','teal',[
 [('🗂 5분류','teal','합성(NME) 글리벡 · 바이오 엔브렐 · 천연물 스티렌 · 개량 아모잘탄 · 제네릭 노코틴<br>한국 신약 = 신물질만 / FDA = 범위 넓음'),
  ('🧪 합성 · 아스피린','blue','1763 버드나무 → 1853 아세틸화 → 1876 <b>최초 엄격한 임상</b> → 1899 바이엘<br>추출·정제 = 천연물 / 변형·합성 = 합성')],
 [('🧬 바이오','violet','핵심기술: <span class="y">유전자재조합 · 하이브리도마</span><br>세대: 단백질 → <b>항체</b> → <b>세포·유전자</b><br>휴물린 1982 최초 재조합 · 면역원성·주사·비쌈'),
  ('🌿 천연물','amber','<b>조인스</b> = 위령선·괄루근·하고초 · 골관절염 · 2001 1호<br><b>스티렌</b> = 애엽 · 위염 · 초록색 약<br>프로스판 = 아이비엽 진해거담 · 임상은 <b>합성과 동일</b>')],
 [('🔧 개량신약 (IMD)','coral','복합제(최다 60%) · 신규염 · 제형변경 · 흡수증가 · 제어방출<br>용도변경·API 변경·용량·복합요법·새 인구집단 → 모두 신약 · <b>임상 필요</b>'),
  ('📋 제네릭 · 제형','navy','제네릭 = <b>생동성</b> (AUC·Cmax 80~125%) · 독점 없음<br><b>서방정</b> = 천천히(속도), 쪼개기 ✗<br><b>장용정</b> = 장에서(장소), 제산제·우유 ✗')],
],'조인스 ↔ 프로스판 · IMD/API 풀네임 · 서술 “제형 차이”만 쓰면 오답 · 천연물도 임상 동일하게 엄격')

wpage(4,'4주차 분류2 · 노벨상1 — mRNA 백신 = 기술 4개','blue',[
 [('❓ 분류 Q&A','amber','저가 ≠ 허가 용이 · 저함량 ≠ 무위험 · 천연 ≠ 안전<br>시밀러 = 복잡한 제품의 일관된 재현<br>임상 = 효과? / 생동성 = 흡수 같나? · 용출시험 37°C'),
  ('🏅 2023 노벨상','coral','<b>카리코 · 와이스먼</b> — 뉴클레오사이드 <b>염기 변형</b><br>(mRNA·LNP 발명 ✗)<br>DNA → mRNA(cap·UTR·ORF·polyA) → 단백질')],
 [('📜 역사','blue','1984 <b>Krieg·Melton</b> IVT 합성 · 1989 리포솜 전달<br>1997 CureVac · Gilboa(암)<br>백신보다 <span class="p">종양학계</span>에서 호의적<br>특허 Cellscript · BioNTech · Moderna'),
  ('🔬 핵심 발견','violet','TLR3/7/8 · PKR → 염증·번역↓<br>U → <b>Ψ (m1Ψ)</b> = 면역↓ 번역↑ 안정↑<br>단백질 <b>10~11배</b> · 2005 Immunity')],
 [('🧴 LNP','teal','이온화 지질(자석) · 헬퍼(벽돌) · 콜레스테롤(시멘트) · PEG(코팅)<br>혈액 중성 / 엔도솜 양전하 → 탈출<br>2018 온파트로 = LNP 첫 약'),
  ('🧩 남은 숙제','navy','<b>서열 설계</b>는 아직 미해결 (코돈 조합 다양)<br>→ 5주차 LinearDesign(AI)로 연결')],
],'“백신에서 더 호의적” ✗(종양학계) · Ψ 단백질 차이 없음 ✗(10~11배) · 서열 설계 = <b>아직 미해결</b>이 맞는 설명')

wpage(5,'5주차 노벨상2 — 카리코 · miRNA · AlphaFold · 면역관용','violet',[
 [('❓ Q&amp;A','amber','전통 한약 = 가설, 검증 면제 ✗<br>시밀러 = <b>유사성</b> 단계적 입증<br>복합제 = 주장한 개선점의 근거<br>Ψ = 선천 경보↓ → 항원↑ → 적응면역 OK'),
  ('👩‍🔬 카리코','coral','1985 미국(테디베어) · 1995 강등 · 1997 와이스먼<br>쥐가 아팠다 → <b>tRNA</b> 단서 → Ψ<br>Nature·Science 거절 → Immunity 2005')],
 [('🏅 2024','teal','생리의학 = <b>microRNA</b> (Ambros·Ruvkun)<br><span class="p">화학</span> = Baker · Hassabis·Jumper<br><span class="p">물리</span> = Hopfield·Hinton<br>miRNA: Drosha → Exportin-5 → Dicer → RISC · ~22nt · seed'),
  ('💊 mRNA 치료제 · AI','blue','저분자(경구) · 항체(세포 밖) · 핵산(undruggable, 전달 필수)<br>LinearDesign MFE↓ CAI↑ · CDK20: PandaOmics → AlphaFold → Chemistry42')],
 [('🛡 2025','violet','Brunkow · Ramsdell · Sakaguchi — <b>말초 면역관용</b><br>Treg · <b>FOXP3</b> · IL-2 + TGF-β<br>관용↑ = 자가면역·이식 / 관용↓ = 면역항암'),
  ('🔮 2026 예측 → 결과','navy','예측: GLP-1(Drucker·Holst·Mojsov), Springer<br>실제: <b>광유전학</b> (→ 6주차)')],
],'화학상 ↔ 물리학상 바꿔치기 · AlphaFold = <b>구조</b> 예측 (부착 사이트 ✗) · miRNA = <b>헤어핀</b>·억제(OFF) · 2023 노벨상 = 염기 변형')

wpage(6,'6주차 후보물질 탐색1 — Target → TPP → Hit (p.33까지)','amber',[
 [('❓ Q&amp;A · 2026','amber','맞춤 암백신 = HLA 제시 · 이질성 · 빠른 생산<br>mRNA = <b>필요한 만큼</b> · LNP = 소화 ✗<br><b>2026 광유전학</b>: 헤게만·나겔·다이서로스<br>ChR2 청색 → 양이온 → ON / NpHR → Cl⁻ → OFF'),
  ('🧭 순서 · 숫자','teal','Target 선정 → 검증 → <b>Hit</b> → <b>Lead</b> → 최적화 → 후보<br>Hit = 유효물질 · Lead = 선도물질<br>프론토실(도마크) · Krogh → Novo Nordisk')],
 [('🎯 Target 선정','blue','Target ≠ Disease · off-target = 부작용<br>Have → deconvolution / Want → discovery<br><b>Forward</b> = 표현형 → 타겟 / <b>Reverse</b> = 타겟 → 화합물<br>APP → BACE1 → γ → Aβ'),
  ('✅ Target 검증','violet','“타겟을 바꾸면 병이 바뀌나?” (인과)<br><b>safety window</b> 안의 치료 이점 · 도구 8개<br>타겟 3대장 = 효소·수용체·이온채널 · siRNA<br>승인 PD-1·PD-L1·CTLA-4 / 신규 TIGIT·TIM-3')],
 [('📋 TPP','coral','FDA <b>2007.3</b> · Labeling 기반 · <b>개발자</b> 작성 · 제출 <b>의무 ✗</b><br>Living document · 9요소<br>Essential(최소) / Ideal(이상)'),
  ('🤖 Hit · HTS','navy','검증 + TPP 후 → 선택성 높은 screening<br>HTS 수십만~수백만 · 1536-well<br>Hit <b>10~수십 μM</b> · Lead 수백 nM · 후보 &lt;100 nM')],
],'Forward ↔ Reverse 방향 · TPP 제출 의무 ✗ / 작성자 = 개발자 · Hit 기준 μM (nM ✗) · 2026 = 광유전학 (GLP-1 ✗)')

# ---------------- 03 헷갈리는 쌍 ----------------
pairs = [
 ('IND','전임상 후 → 임상 진입','NDA','3상 후 → 시판허가'),
 ('헬싱키 1964','치료적·비치료적 연구 · IRB','벨몬트 1979','존중 · 이익 · 정의'),
 ('Acres of Skin','감옥 · 피부 화학물질','유대인 병원','노인 · 암세포 주입'),
 ('엘릭서 → 1938','안전성 (DEG 신장독성)','탈리도마이드 → 1962','유효성 + 사전승인'),
 ('플레밍','라이소자임 → 페니실린','도마크','프론토실 → 설파닐아마이드'),
 ('조인스정','위령선·괄루근·하고초 · 골관절염','프로스판정','아이비엽 · 진해거담'),
 ('스티렌정','애엽(쑥) · 위염','베러겐','녹차 · 사마귀 (미국 1호)'),
 ('제네릭','합성·동일 · 생동성','개량신약 (IMD)','변형 · 임상 필요'),
 ('바이오시밀러','바이오 · 유사','바이오베터','바이오 · 개량'),
 ('서방정','천천히 (속도)','장용정','장에서 (장소)'),
 ('유전자재조합','단백질 (휴물린)','하이브리도마','항체'),
 ('mRNA 초기','종양학계가 더 호의적','“백신에서 호의적”','✗ (2024 함정)'),
 ('2024 화학상','Baker · Hassabis · Jumper (단백질)','2024 물리학상','Hopfield · Hinton (신경망)'),
 ('AlphaFold','단백질 구조 예측','부착 사이트 예측','다른 AI 기술'),
 ('mRNA 백신','단백질 ON','miRNA · siRNA','단백질 OFF'),
 ('2023 · 2025','면역 켜기(백신) / 끄기(관용)','관용↑ / 관용↓','자가면역·이식 / 면역항암'),
 ('Forward','표현형 → 타겟 (deconvolution)','Reverse','타겟 → 화합물 (discovery)'),
 ('Target 동정','관련 있다 (상관)','Target 검증','바꾸면 병이 바뀐다 (인과)'),
 ('Essential','최소 기준 (go/no-go)','Ideal','이상적 목표 (경쟁 우위)'),
 ('Hit','유효물질 · μM','Lead','선도물질 · 수백 nM'),
]
half = len(pairs)//2
def ptab(ps):
    return '<table class="t" style="font-size:9pt"><tr><th>A</th><th>설명</th><th>B</th><th>설명</th></tr>' + ''.join(f'<tr><td><b class="c-blue">{a}</b></td><td>{b}</td><td><b class="c-coral">{c}</b></td><td>{d}</td></tr>' for a,b,c,d in ps) + '</table>'
page(ph('총정리','03','헷갈리는 쌍 TOP 20 — 바꿔치기 함정 방어','1~6주차') + f'''
  <div class="body row"><div class="col" style="flex:1">{ptab(pairs[:half])}</div><div class="col" style="flex:1">{ptab(pairs[half:])}</div></div>''', style='--pc:var(--violet);--pcs:var(--violet-s)')

# ---------------- 04 연표 + 숫자 ----------------
page(ph('총정리','04','통합 연표 — 순서만 확실히','2·3·4·5·6주차') + '''
  <div class="body col">
    <div class="card" style="padding:2mm 3mm"><h3>⚖ 비극 → 법 · 윤리 (2주차 중심)</h3><div data-d="tlOld"></div></div>
    <div class="card" style="padding:2mm 3mm"><h3>🧬 바이오 · mRNA · 노벨상 (3~6주차)</h3><div data-d="tlNew"></div></div>
    <div class="callout tip"><div class="t">💡 짝꿍 공식</div><div class="small">엘릭서(1937) → <b>1938</b> FD&amp;C · 탈리도마이드 → <b>1962</b> 케파우버-해리스 · 나치 → <b>1947</b> 뉘른베르크 · 터스키기 → 1974 국가연구법 → <b>1979</b> 벨몬트</div></div>
  </div>''', style='--pc:var(--teal);--pcs:var(--teal-s)')

page(ph('총정리','04','숫자 총정리 — 나오면 무조건 맞히기','1~6주차') + '''
  <div class="body grid3">
    <div class="card" style="border-top:4px solid var(--navy)"><h3>🔻 개발 과정</h3><div class="small">
      FDA <b>5,000~10,000 → 250 → 5 → 1</b><br>탐색·전임상 <b>3~6년</b> · 임상 <b>6~7년</b> · 심사 <b>0.5~2년</b> = 10~15년<br>
      임상 인원 1상 20~100 · 2상 100~500 · 3상 1,000~5,000<br>한국 10,000 → 50 → 5 → 1<br>AI 시대 ~6~9년</div></div>
    <div class="card" style="border-top:4px solid var(--coral)"><h3>📉 성공률 · 비용</h3><div class="small">
      1상 → 승인 <b>9.6%</b> · 최저 통과 2상 30.7%<br>허들 탈락 5.7 → <b>26.4%</b> (증가)<br>
      임상 효능 실패 ~90% · 개발비 평균 48억$ ≈ 6.4조<br>FDA 승인 연 36 → 22개<br>IND 30일 · NDA 접수 60일</div></div>
    <div class="card" style="border-top:4px solid var(--teal)"><h3>💊 분류 · 제네릭</h3><div class="small">
      개발기간 신약 10~15 / 개량 3~5 / 제네릭 2~3년<br>독점 6 / 4 / 없음<br>생동성 <b>AUC·Cmax 80~125%</b><br>개량신약 최다 = 복합제 60%<br>제네릭 사용량 49.7%</div></div>
    <div class="card" style="border-top:4px solid var(--violet)"><h3>🧬 mRNA · 노벨</h3><div class="small">
      Ψ mRNA 단백질 <b>10~11배</b> (2024 기출)<br>비변형 mRNA IFN-β ~120배↑<br>miRNA ~22 nt · seed 2~8번<br>노벨상 최대 3명 · 1901년 시작<br>엘릭서 105명 사망 · 탈리도마이드 1만+</div></div>
    <div class="card" style="border-top:4px solid var(--amber)"><h3>🎯 후보물질 (6주)</h3><div class="small">
      Hit <b>10~수십 μM</b> · Lead <b>수백 nM</b> · 후보 <b>&lt;100 nM</b><br>HTS 수십만~수백만 개 · 1536-well<br>초기 10⁵~10⁶ → 10³ → 10¹~10² → &lt;10 → 1<br>TPP <b>2007년 3월</b> · Optopatch <b>320개</b></div></div>
    <div class="card" style="border-top:4px solid var(--blue)"><h3>🇰🇷 국산 · 연도</h3><div class="small">
      1호 선플라주 <b>1999</b> · 팩티브 FDA <b>2003</b><br>36호 엔블로정 2022<br>조인스 2001 · 스티렌 2002<br>휴물린 1982 · IVT 1984 · Ψ 2005<br>노벨: 2023 mRNA · 2024 miRNA · 2025 관용 · 2026 광유전학</div></div>
  </div>''', cls='page big xl', style='--pc:var(--amber);--pcs:var(--amber-s)')

# ---------------- 모의고사 intro ----------------
page('''<div class="body" style="display:flex;flex-direction:column;justify-content:center;padding:0 8mm">
    <div style="font-size:10pt;font-weight:900;letter-spacing:.2em;color:var(--coral)">MOCK MIDTERM</div>
    <div style="font-size:30pt;font-weight:900;letter-spacing:-.03em;line-height:1.2;margin:2mm 0 4mm">통합 모의고사<br><span style="font-size:15pt;font-weight:500;color:var(--sub)">1~6주차 섞어서 · 객관식 15 · O/X 12 · 단답 9 · 서술 5 = 41문항 · 권장 60분</span></div>
    <div class="row" style="max-width:255mm">
      <div class="callout trap" style="flex:1"><div class="t">실전처럼</div><div class="small">타이머 60분 → 정답 칸은 종이로 가리고 → 끝까지 푼 뒤 채점 (p.24 정답표)</div></div>
      <div class="callout tip" style="flex:1"><div class="t">주차 태그</div><div class="small">각 문제 오른쪽 위 회색 태그 = 출처 주차. 틀리면 그 주차 노트로!</div></div>
      <div class="callout memo" style="flex:1"><div class="t">비중</div><div class="small">2024 기출변형(분홍 태그)이 절반 — 교수님이 <b>같은 포인트를 다시 낼</b> 가능성 대비</div></div>
    </div>
  </div>''', style='background:linear-gradient(135deg,#fff6f2,#fff)')

MC = [
 mc('모의 1',1,'약사법상 “신약”에 대한 설명으로 옳은 것은?',['화학구조·본질 조성이 전혀 새로운 신물질만 해당한다.','신물질을 유효성분으로 하는 복합제도 신약이다.','기구·장치도 의약품에 포함된다.','제네릭은 신약으로 분류된다.','신약 지정은 FDA가 한다.'],'②','신물질 + 신물질 복합제 · 식약처장 지정 · 기구·장치는 의약품 ✗'),
 mc('모의 2',1,'신약개발 과정에 대한 설명으로 옳지 <u>않은</u> 것은?',['전임상에서 검증된 결과로 NDA를 신청해 임상 1상을 시작한다.','임상 3상이 끝나면 NDA를 제출한다.','라벨링 결정 후 FDA가 생산시설을 실사한다.','시판 후 조사는 임상 4상이다.','IND는 Investigational New Drug의 약자다.'],'①','임상 진입 = <b>IND</b> (2024 최다 오답)',src=True),
 mc('모의 3',2,'신약개발의 어려움에 대한 설명으로 옳지 <u>않은</u> 것은?',['쉬운 표적은 이미 많이 소진됐다.','허들을 통과하지 못하는 비율은 감소 추세다.','협조적인 환자를 모으는 시간·비용이 증가하고 있다.','2·3상 실패의 1위 원인은 효능 부족이다.','허들 4개는 안전성·유효성·품질·비용효과성이다.'],'②','실패 비율 = <b>증가</b> (5.7 → 26.4%)',src=True),
 mc('모의 4',2,'엘릭서 설파닐아마이드 사건에 대한 설명으로 옳은 것은?',['용매 DEG가 영유아 간독성을 일으켰다.','용매 DEG(부동액 성분)가 신장독성을 일으켰다.','이 사건으로 1962년 유효성 입증이 의무화됐다.','켈시 박사가 허가를 거부해 피해를 막았다.','설파닐아마이드 자체의 독성이 원인이었다.'],'②','→ <b>1938 FD&amp;C</b>(안전성). ③④는 탈리도마이드',src=True),
 mc('모의 5',2,'의학 연구 윤리에 대한 설명으로 옳지 <u>않은</u> 것은?',['뉘른베르크 강령은 자발적 동의를 강조했다.','헬싱키 선언은 치료적·비치료적 연구의 원칙을 정리했다.','헬싱키 선언은 인간 존중·이익·정의의 3원칙을 제시했다.','터스키기 연구는 벨몬트 보고서로 이어졌다.','감옥 피부 화학물질 실험은 Acres of Skin이다.'],'③','3원칙 = <b>벨몬트</b>(1979)',src=True),
 mc('모의 6',2,'탈리도마이드에 대한 설명으로 옳지 <u>않은</u> 것은?',['임신부 입덧약으로 쓰여 기형아가 태어났다.','미국 FDA 켈시 박사가 허가를 거부했다.','1962년 케파우버-해리스 수정안의 계기가 됐다.','현재는 연구만 될 뿐 치료에 사용되지 않는다.','임신부에게 금기다.'],'④','지금도 <b>다발성 골수종</b> 등에 사용',src=True),
 mc('모의 7',3,'위령선·괄루근·하고초로 만든 골관절염 치료 천연물신약은?',['스티렌정','프로스판정','조인스정','기넥신','베러겐'],'③','프로스판 = 아이비엽 진해거담 · 스티렌 = 애엽 위염',src=True),
 mc('모의 8',3,'다음 중 개량신약(신약)에 해당하지 <u>않는</u> 것은?',['아스피린을 항혈전 용도로 개발','유효성분(API)을 바꾼 대체 소염제','처방용 고용량 제제','두 약을 합친 복합요법','특허 만료 후 동일 성분 복제약'],'⑤','그건 <b>제네릭</b> — 임상 대신 생동성',src=True),
 mc('모의 9',3,'바이오의약품의 세대 구분으로 옳은 것은?',['1세대 항체 → 2세대 단백질 → 3세대 세포·유전자','1세대 단순 단백질 → 2세대 항체 → 3세대 세포·유전자','1세대 세포 → 2세대 항체 → 3세대 단백질','1세대 백신 → 2세대 항생제 → 3세대 항체','1세대 유전자 → 2세대 세포 → 3세대 단백질'],'②','2024 원래 출제 의도',src=True),
 mc('모의 10',4,'mRNA 기술의 역사로 옳지 <u>않은</u> 것은?',['1984년 Krieg·Melton이 시험관 합성(IVT)을 보고했다.','1997년 Hoerr가 CureVac을 세웠다.','초기 mRNA 기술은 종양학계보다 백신 개발에서 더 호의적이었다.','Gilboa는 mRNA로 암 치료를 시도했다.','카리코·와이스먼은 2005년 Ψ 효과를 발표했다.'],'③','방향 반대 — <b>종양학계</b>가 더 호의적',src=True),
 mc('모의 11',4,'슈도우리딘(Ψ) mRNA에 대한 설명으로 옳지 <u>않은</u> 것은?',['우리딘(U)을 Ψ로 바꿨다.','선천면역 반응(염증)이 줄었다.','비변형 mRNA와 단백질 생성량 차이는 없었다.','2023 노벨생리의학상의 근거가 됐다.','tRNA에서 단서를 얻었다.'],'③','보통 <b>10~11배</b> 더 많음',src=True),
 mc('모의 12',5,'2024 노벨상에 대한 설명으로 옳지 <u>않은</u> 것은?',['Ambros·Ruvkun은 microRNA로 생리의학상을 받았다.','Hassabis·Jumper는 단백질 구조 예측으로 화학상을 받았다.','Hopfield·Hinton은 인공신경망으로 물리학상을 받았다.','AlphaFold의 주목적은 합성신약과 단백질의 부착 사이트 예측이다.','microRNA는 헤어핀 구조의 전구체에서 만들어진다.'],'④','AlphaFold = <b>단백질 자체 구조</b>',src=True),
 mc('모의 13',5,'2025 노벨생리의학상(말초 면역관용)과 관련 없는 것은?',['조절 T세포(Treg)','FOXP3','IL-2 + TGF-β','CTLA-4-Ig로 anergy 유도','슈도우리딘으로 선천면역 회피'],'⑤','⑤는 2023 (mRNA 백신)'),
 mc('모의 14',6,'신약 후보물질 탐색 순서로 옳은 것은?',['Hit → Target 선정 → Lead → 검증 → 최적화','Target 선정 → Target 검증 → Hit → Lead → Lead 최적화','Target 검증 → Target 선정 → Lead → Hit → 최적화','Lead → Hit → Target 선정 → 검증 → 최적화','Target 선정 → Hit → Target 검증 → Lead → 최적화'],'②','→ 후보물질 도출 · TPP는 검증 후'),
 mc('모의 15',6,'다음 중 옳은 것은?',['Forward chemical genetics는 타겟에서 화합물로 간다.','TPP는 FDA가 작성하며 제출이 의무다.','합성신약의 Hit은 보통 10 μM~수십 μM 이하에서 반응한다.','TIGIT은 이미 FDA 승인된 면역관문 타겟이다.','2026 노벨생리의학상은 GLP-1 발견에 수여됐다.'],'③','① 표현형 → 타겟 ② 개발자·의무 ✗ ④ 신규 ⑤ 광유전학'),
]
for i in range(0,15,3):
    page(ph('모의','객관식',f'모의 {i+1}~{i+3}') + '<div class="body grid3">' + ''.join(MC[i:i+3]) + '</div>', style='--pc:var(--coral)')

ox = [
 ('제네릭은 생물학적 동등성 시험으로 허가받는다.','O','2024 단답 19번',3),
 ('개량신약은 임상시험이 필요 없다.','X','제네릭만 면제',3),
 ('스티렌정은 애엽 추출 위염 치료제다.','O','초록색 약',3),
 ('서방정은 장에서 녹도록 만든 제형이다.','X','그건 장용정 · 서방 = 천천히',3),
 ('Acres of Skin은 노인에게 암세포를 주입한 연구다.','X','그건 유대인 병원',2),
 ('켈시 박사는 탈리도마이드 허가를 거부했다.','O','1962 법 계기',2),
 ('mRNA 서열 설계는 이미 완전히 해결됐다.','X','아직 해결할 문제',4),
 ('홉필드·힌턴은 2024 노벨 화학상 수상자다.','X','물리학상',5),
 ('microRNA는 mRNA에 붙어 기능을 억제한다.','O','헤어핀 → OFF',5),
 ('TPP 제출은 의무사항이다.','X','의무 아님 · 개발자 작성',6),
 ('Phenotype-based 접근은 forward chemical genetics다.','O','표현형 → 타겟',6),
 ('Target 검증은 상관관계만 확인하면 충분하다.','X','인과 + safety window',6),
]
li = ''.join(f'<li>{s}<span class="bx">O / X</span></li>' for s,_,_,_ in ox)
trs = ''.join(f'<tr><td class="c">{i+1}</td><td class="c"><b>{a}</b></td><td>{e}</td><td class="c">{w}주</td></tr>' for i,(_,a,e,w) in enumerate(ox))
page(ph('모의','O/X','모의 16 — O/X 12문항') + f'''
  <div class="body row">
    <div class="q" style="flex:1.2"><div class="q-h"><span class="q-no">모의 16</span><span class="tag ox">O/X</span><span class="src2024">기출 포인트 포함</span></div>
      <div class="q-b"><ol class="ox">{li}</ol></div><div class="blank" style="height:12mm"></div></div>
    <div class="ans" style="flex:1;border:1.5px solid #bfe6cf;border-radius:11px">
      <div class="a"><span class="pill">정답</span><span class="v">{' '.join(a for _,a,_,_ in ox)}</span></div>
      <table class="t" style="--pcs:#dff3e7;font-size:8.8pt;background:#fff"><tr><th class="c">#</th><th class="c">답</th><th>한 줄 해설</th><th class="c">주차</th></tr>{trs}</table></div>
  </div>''', style='--pc:var(--teal)')

SA = [
 sa('모의 17',3,'IMD와 API의 풀네임을 쓰시오.','<b class="c-teal">Incrementally Modified Drug</b> · <b class="c-teal">Active Pharmaceutical Ingredient</b>',src=True),
 sa('모의 18',3,'제네릭 의약품 허가에 필요한 시험은?','<b class="c-teal">생물학적 동등성 시험</b> (생동성) — AUC·Cmax 80~125%',src=True),
 sa('모의 19',3,'바이오의약품 생산의 핵심 기술 2가지는?','<b class="c-teal">유전자재조합 기술</b> · <b class="c-teal">하이브리도마 기술</b>',src=True),
 sa('모의 20',2,'도마크가 발견한 프론토실이 몸속에서 바뀌어 작용하는 최초 설파제 성분은?','<b class="c-teal">설파닐아마이드</b> (페니실린 ✗)',src=True),
 sa('모의 21',2,'탈리도마이드의 미국 허가를 막은 FDA 심사관은?','<b class="c-teal">프랜시스 올덤 켈시</b> (Frances Oldham Kelsey)',src=True),
 sa('모의 22',5,'2025 · 2026 노벨생리의학상의 주제는?','2025 <b class="c-teal">말초 면역관용</b>(Treg) · 2026 <b class="c-teal">광유전학</b>'),
]
page(ph('모의','단답','모의 17~22 — 단답형') + '<div class="body grid3" style="grid-template-rows:1fr 1fr">' + ''.join(SA) + '</div>', style='--pc:var(--violet)')

SA2 = [
 sa('모의 23',1,'국산 신약 1호의 이름·회사·적응증은?','<b class="c-teal">선플라주</b> · SK케미칼 · 위암 (1999)',h=14),
 sa('모의 24',6,'Target 검증의 핵심 질문을 한 문장으로 쓰시오.','“<b class="c-teal">Target의 변화는 목표한 질병을 변화시키는가?</b>”',h=14),
 sa('모의 25',4,'LNP의 4가지 지질 성분은?','<b class="c-teal">이온화 지질 · 헬퍼 지질(인지질) · 콜레스테롤 · PEG-지질</b>',h=14),
]
ES1 = [
 es('모의 26','서방정과 장용정의 <b>차이</b>를 서술하시오.','<div class="small"><b>서방정</b>은 약물이 <b>천천히(서서히) 용출</b>되도록 만들어 효과를 오래 유지하는 제형이다(쪼개거나 씹으면 안 됨). <b>장용정</b>은 위산에 녹지 않고 <b>장에서 용출</b>되도록 코팅한 제형이다(제산제·우유와 함께 복용 ✗). 즉 서방정은 <b>용출 속도</b>, 장용정은 <b>용출 장소</b>를 조절한다. <span class="p">“제형의 차이”만 쓰면 오답</span></div>','<span class="src2024">2024 30번</span>',h=22),
]
page(ph('모의','단답 · 서술','모의 23~26') + '<div class="body grid2"><div class="col">' + ''.join(SA2) + '</div><div class="col">' + ''.join(ES1) + '</div></div>', style='--pc:var(--violet)')

ES = [
 es('모의 27','신약개발이 점점 어려워지는 이유를 <b>5가지</b> 쓰시오. (1개 부족 시 −1점)','<ol class="small" style="padding-left:16px"><li>쉬운 표적은 이미 소진됨 (남은 질병이 복잡)</li><li>허들(안전성·유효성·품질·비용효과성) 기준이 높아짐 → 탈락 비율 증가</li><li>협조적인 환자 모집 시간·비용 증가</li><li>표준요법보다 나아야 해서 2·3상 효능 실패 多</li><li>개발 비용(평균 ~48억$)·기간(10~15년) 증가</li><li>규제·윤리 요건 강화 (IRB, 동의 등)</li></ol>','<span class="src2024">2024 스타일(“5개”)</span>'),
 es('모의 28','헬싱키 선언과 벨몬트 보고서를 <b>연도 · 계기 · 핵심 내용</b>으로 비교하시오.','<div class="small"><b>헬싱키 선언(1964)</b>은 뉘른베르크 강령(1947, 나치 인체실험)을 이어 세계의사회가 정리한 의학연구 윤리로, <b>치료적·비치료적 연구</b>의 원칙, 보호자·서면 동의, <b>IRB 사전 승인</b>을 담았다. <b>벨몬트 보고서(1979)</b>는 <b>터스키기 매독 연구</b>·유대인 만성질환 병원·Acres of Skin 같은 남용 사례 → 1974 국가연구법을 계기로 나왔으며, <b>인간 존중 · 이익(선행) · 정의</b>의 3원칙을 제시했다.</div>','<span class="src2024">2024 연결</span>'),
]
page(ph('모의','서술','모의 27~28 — 서술형') + '<div class="body grid2">' + ''.join(ES) + '</div>', style='--pc:var(--coral)')

ES2 = [
 es('모의 29','mRNA 백신 상용화를 가능하게 한 기술을 <b>3가지</b> 들고 각각이 해결한 문제를 서술하시오.','<div class="small">① <b>시험관 합성(IVT, 1984 Krieg·Melton)</b> — 원하는 mRNA를 실험실에서 대량으로 만들 수 있게 함. ② <b>뉴클레오사이드 변형(U → Ψ, 2005 카리코·와이스먼)</b> — 외부 RNA로 인식돼 생기던 <b>염증을 줄이고 단백질 생산을 10~11배</b> 늘림(2023 노벨상). ③ <b>LNP 전달(Cullis)</b> — 불안정하고 음전하인 mRNA를 보호해 <b>세포 안까지 전달</b>, 엔도솜에서 탈출. (+ BioNTech·Moderna의 산업화·투자)</div>','<span class="src2024">2024 연결</span>'),
 es('모의 30','표현형 기반(forward)과 타겟 기반(reverse) 접근을 <b>출발점 · 장단점</b>으로 비교하시오.','<div class="small"><b>표현형 기반</b>은 질병 모델에서 <b>효과 있는 화합물을 먼저</b> 찾고 타겟을 나중에 <b>역추적(deconvolution)</b>한다. 생체 내 실제 효과를 봐 first-in-class 발견에 강하지만 <b>타겟 규명이 어렵다</b>. <b>타겟 기반</b>은 <b>검증된 분자 타겟</b>에서 출발해 생화학 분석으로 화합물을 찾는다. 기전이 명확하고 HTS에 유리하지만 <b>세포·동물에서 효과가 없을 수</b> 있다.</div>',wtag(6)),
]
page(ph('모의','서술','모의 29~30 — 서술형') + '<div class="body grid2">' + ''.join(ES2) + '</div>', style='--pc:var(--coral)')

# ---------------- 정답표 ----------------
key = [('1','②',1),('2','①',1),('3','②',2),('4','②',2),('5','③',2),('6','④',2),('7','③',3),('8','⑤',3),('9','②',3),('10','③',4),('11','③',4),('12','④',5),('13','⑤',5),('14','②',6),('15','③',6)]
kt = ''.join(f'<tr><td class="c"><b>{n}</b></td><td class="c"><b class="c-coral">{a}</b></td><td class="c">{w}주</td></tr>' for n,a,w in key)
page(ph('모의','정답표','빠른 채점표 — 틀린 주차로 돌아가기') + f'''
  <div class="body row">
    <div class="col" style="flex:.8"><table class="t" style="font-size:9.2pt"><tr><th class="c">객관식</th><th class="c">답</th><th class="c">복습</th></tr>{kt}</table></div>
    <div class="col" style="flex:1.2">
      <div class="card"><h3>✅ O/X (모의 16)</h3><div class="small" style="font-size:12pt;font-weight:900;letter-spacing:.08em">{' '.join(a for _,a,_,_ in ox)}</div></div>
      <div class="card"><h3>✏ 단답 (17~25)</h3><div class="small">17 Incrementally Modified Drug · Active Pharmaceutical Ingredient<br>18 생물학적 동등성 시험 · 19 유전자재조합 · 하이브리도마<br>20 설파닐아마이드 · 21 켈시 · 22 면역관용 · 광유전학<br>23 선플라주 · 24 Target의 변화는 질병을 변화시키는가 · 25 이온화·헬퍼·콜레스테롤·PEG</div></div>
      <div class="card"><h3>📊 점수 → 할 일</h3><table class="t" style="font-size:9.2pt">
        <tr><th>맞힌 수 (41)</th><th>다음 할 일</th></tr>
        <tr><td><b>37+</b></td><td>D-day 1장 + 헷갈리는 쌍만</td></tr>
        <tr><td><b>29~36</b></td><td>틀린 주차의 <b>암기카드</b> + 실전 O/X 다시</td></tr>
        <tr><td><b>~28</b></td><td>틀린 주차 노트의 <b>요약 페이지</b>부터 다시</td></tr></table></div>
    </div>
  </div>''', style='--pc:var(--teal);--pcs:var(--teal-s)')

# ---------------- D-day ----------------
page(ph('총정리','FINAL','D-day 1장 — 시험장 들어가기 전') + '''
  <div class="body grid3 cram" style="font-size:10.6pt;line-height:1.7">
    <div class="col">
      <div class="card" style="border-top:4px solid var(--navy)"><h3>🚪 1주</h3>신물질 + 신물질 복합제 = 신약<br>5,000~10,000 → 250 → 5 → 1<br>전임상 → <b>IND</b> → 1·2·3상 → <b>NDA</b> → 4상<br>IMD · API 풀네임</div>
      <div class="card" style="border-top:4px solid var(--coral)"><h3>⚖ 2주</h3>허들·환자 모집 비용 <b>증가</b><br>엘릭서 = <b>신장</b> → 1938 / 탈리도마이드 = 켈시 → 1962, <b>지금도 사용</b><br>헬싱키 = 치료적·비치료적 / 벨몬트 = 존중·이익·정의<br>피부 = Acres of Skin · 암세포 = 유대인 병원</div>
    </div>
    <div class="col">
      <div class="card" style="border-top:4px solid var(--teal)"><h3>🗂 3주</h3><b>조인스</b>(위령선·괄루근·하고초, 골관절염) ≠ 프로스판<br>천연물 임상 = 합성과 동일<br>개량신약도 임상 · 제네릭 = <b>생동성</b><br>재조합 · 하이브리도마 · 단백질 → 항체 → 세포·유전자<br>서방 = <b>천천히</b> / 장용 = <b>장에서</b></div>
      <div class="card" style="border-top:4px solid var(--blue)"><h3>🧬 4주</h3>mRNA 초기 = <b>종양학계</b>가 호의적<br>Ψ 단백질 <b>10~11배</b><br>서열 설계 = <b>아직 미해결</b><br>2023 = 염기 변형 (카리코·와이스먼)</div>
    </div>
    <div class="col">
      <div class="card" style="border-top:4px solid var(--violet)"><h3>🏅 5주</h3>AlphaFold = <b>화학상</b>, 구조 예측 (부착 사이트 ✗)<br>신경망 = <b>물리학상</b><br>miRNA = 헤어핀 → 억제<br>2025 = 말초 면역관용 · Treg · FOXP3</div>
      <div class="card" style="border-top:4px solid var(--amber)"><h3>🎯 6주</h3>2026 = <b>광유전학</b><br>Target → 검증 → Hit → Lead → 최적화<br>Forward = 표현형 → 타겟<br>TPP 2007.3 · 개발자 · 의무 ✗<br>Hit μM · Lead 수백 nM · 후보 &lt;100 nM</div>
    </div>
  </div>''', cls='page dday', style='--pc:var(--navy);--pcs:#e9ecf5')

# ---------------- render ----------------
out = ['<!doctype html>\n<html lang="ko"><head><meta charset="utf-8"><title>신약개발개론 중간고사 총정리</title>\n<link rel="stylesheet" href="style.css"></head><body>']
for i,(cls,style,inner) in enumerate(pages):
    st = f' style="{style}"' if style else ''
    if 'cover' in cls:
        out.append(f'<section class="{cls}">{inner}</section>')
    else:
        out.append(f'<section class="{cls}"{st}>\n  {inner}\n  <div class="pf"><span>{FOOT}</span><span>{i+1}</span></div>\n</section>')
out.append('<script src="diagramsM.js"></script>\n</body></html>')
open('mid.html','w').write('\n'.join(out))
print(len(pages),'pages')
