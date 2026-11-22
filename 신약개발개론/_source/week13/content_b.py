# (B) 1단계 안전성 (슬라이드 15~21)
PAGES = [
dict(title="전임상 1단계: 안전성 — 생체적합성 (숙주 반응)", slide="15·16·17", img=["s15.jpg", "s16.jpg"],
     sub="Preclinical research 1st step: safety · biocompatibility",
     kw=["안전성 먼저 → 유효성", "생체적합성", "ISO 10993-1", "분해·멸균·열안정성"],
     sum="전임상은 <b>1단계 안전성 → 2단계 유효성</b> 순서야. 신기술은 먼저 몸이 받아들이는지(<b>생체적합성, 숙주 반응</b>)를 봐야 하고, 이를 위해 대상 질환·적용 방법·분해성·멸균법·열안정성·생존 기간 등을 따져. 평가 항목은 ISO 10993-1 표로 정해져 있어.",
     lab="슬라이드 내용",
     tr="""<p><b>15</b> Preclinical Research – 1st Step: <b>Safety</b> — 전임상 안전성(약물대사·세포독성·in vitro ADME-Tox·기능 평가·독성/중개·심장/신경독성) 다음에 치료 효능</p>
<p><b>16 Biologically Safe: Host response – Biocompatibility</b> (신기술에 대한 질문)</p>
<ul><li>대상 질환은? · 어떻게 적용하나? · <b>분해되나?</b></li>
<li><b>멸균 방법은?</b> · <b>열안정성은?</b> · 살아 있나? 얼마나 오래? · +α</li></ul>
<p><b>17</b> ISO 10993-1 부록 A — 의료기기 분류(접촉 부위·접촉 기간)별 생물학적 평가 항목(세포독성·감작·자극·급성/아급성/만성 독성·이식·혈액적합성·유전독성·발암성·생식독성·분해 등)</p>""",
     ex="""<p><b>순서가 핵심</b>: 안전하지 않으면 효능을 볼 의미가 없어서 <g>안전성이 먼저</g>야.</p>
<p><b>생체적합성(biocompatibility)</b> = 몸에 넣었을 때 해로운 숙주 반응(염증·면역 반응 등) 없이 받아들여지는 성질.</p>
<p>ISO 10993-1 표는 “얼마나 오래, 어디에 닿느냐”에 따라 필요한 시험이 늘어나는 구조야. 오래·깊이 닿을수록 시험 항목이 많아져.</p>
<p class="box"><span class="tag">시험 포인트</span>전임상 순서 = <pk>안전성(1st) → 유효성(2nd)</pk>. 생체적합성 = 숙주 반응.</p>"""),

dict(title="세포적합성 (Cytocompatibility)", slide="18", img="s18.jpg",
     sub="In vitro cytocompatibility tests",
     kw=["Live/Dead 염색", "세포 생존율", "증식 = 대사 활성", "Day 1·4·7"],
     sum="동물에 넣기 전에 <b>세포 수준(in vitro)</b>에서 먼저 안전한지 봐. <b>Live/Dead 염색</b>으로 살아 있는 세포(초록)를 보고, <b>세포 생존율</b>과 <b>대사 활성 기반 증식</b>을 1·4·7일에 측정해.",
     lab="슬라이드 내용",
     tr="""<ul><li><b>Live/Dead Assay</b> — 여러 소재(TCP·SF·SG15~SG3·GelMA) 위 세포를 Day 1·4·7에 염색(초록 = 살아 있는 세포)</li>
<li><b>Cell viability</b> — 죽은/산 세포 비율로 생존율(%) 계산</li>
<li><b>Proliferation</b> — 대사 활성(metabolic activity)으로 세포 증식 측정</li></ul>""",
     ex="""<p>세포적합성 시험 세 가지:</p>
<table class="t"><tr><th>시험</th><th>보는 것</th></tr>
<tr><td>Live/Dead</td><td>살아 있는/죽은 세포를 눈으로</td></tr>
<tr><td>Viability</td><td>생존 비율(%)</td></tr>
<tr><td>Proliferation</td><td>대사 활성 → 잘 자라는지</td></tr></table>
<p>TCP(세포배양 플라스틱)를 대조군으로 두고 새 소재가 비슷하거나 더 나은지 봐.</p>
<p class="box"><span class="tag">흐름</span>in vitro(세포적합성) → in vivo(동물 생체적합성) 순으로 안전성을 확인해.</p>"""),

dict(title="전임상 안전성 — 투여 경로", slide="19", img="s19.jpg",
     sub="Preclinical safety: route of administration",
     kw=["피하 이식", "국소 적용", "위관 투여", "흡입"],
     sum="안전성 시험은 <b>실제 쓰일 경로</b>로 투여해. 피하 이식(subcutaneous implantation), 피부 국소 적용(topical), 위관 투여(intragastric gavage, 경구), 흡입(inhalation)이 대표적이야.",
     lab="슬라이드 내용",
     tr="""<ul><li><b>Subcutaneous implantation</b> — 등 피부 밑에 소재 이식</li>
<li><b>Topical Application</b> — 피부에 붙이고 Day 0·3 관찰</li>
<li><b>Intragastric gavage</b> — 관으로 위에 직접 투여(경구 투여 모델)</li>
<li><b>Inhalation</b> — 흡입 챔버로 투여</li></ul>""",
     ex="""<p>11주차 ADME의 <b>흡수(A)</b>와 연결돼. 투여 경로에 따라 몸에 들어가는 방식과 노출이 달라서, 안전성도 그 경로로 봐야 해.</p>
<table class="t"><tr><th>경로</th><th>사람에서 대응</th></tr>
<tr><td>위관 투여</td><td>경구약</td></tr><tr><td>흡입</td><td>흡입제</td></tr>
<tr><td>국소 적용</td><td>피부 패치·연고</td></tr><tr><td>피하 이식</td><td>이식형 소재·기기</td></tr></table>
<p class="box"><span class="tag">시험 포인트</span><pk>intragastric gavage = 위관(경구) 투여</pk>. 용어 뜻을 물을 수 있어.</p>"""),

dict(title="전임상 안전성 — 생체적합성·생분해성 · 전신·흡입 독성", slide="20·21", img=["s20.jpg", "s21.jpg"],
     sub="Biocompatibility, biodegradability, systemic and inhalational toxicity",
     kw=["CD68 · CD3 염색", "잔존 면적 = 분해", "주요 장기 H&E", "혈액·혈청 화학"],
     sum="동물에서는 <b>생체적합성</b>(이식 부위 염증세포 CD68·CD3), <b>생분해성</b>(시간에 따라 남은 면적), <b>전신 독성</b>(심장·폐·간·신장·비장 조직), <b>흡입 독성</b>(폐 조직), <b>혈액·혈청 화학 검사</b>로 안전성을 확인해.",
     lab="슬라이드 내용",
     tr="""<p><b>20</b></p>
<ul><li><b>Biocompatibility</b> — 피하 이식 후 조직 염색(H&amp;E), 대식세포 <b>CD68</b>·T세포 <b>CD3</b> 염색으로 염증 반응 확인</li>
<li><b>Biodegradability</b> — GelMA vs GelMA+β-CD: Day 7·14에 남은 면적(%)으로 분해 정도 비교</li></ul>
<p><b>21</b></p>
<ul><li><b>Systemic Toxicity</b> — 심장·폐·간·신장·비장 H&amp;E 조직 비교(손상군·대조군·시험군)</li>
<li><b>Inhalational Toxicity</b> — 폐·세기관지 조직(OVA20 vs Albuterol)</li>
<li><b>Blood Exam &amp; Serum chemistry</b> — 혈당·인슐린·렙틴·총콜레스테롤 등</li></ul>""",
     ex="""<table class="t"><tr><th>평가</th><th>무엇으로 보나</th></tr>
<tr><td>생체적합성</td><td>이식 부위 염증세포(CD68 대식세포, CD3 T세포)</td></tr>
<tr><td>생분해성</td><td>시간에 따라 남은 소재 면적</td></tr>
<tr><td>전신 독성</td><td>주요 장기 조직검사(H&amp;E)</td></tr>
<tr><td>흡입 독성</td><td>폐 조직</td></tr>
<tr><td>혈액·혈청</td><td>혈액 수치 변화</td></tr></table>
<p>12주차 GLP 흐름의 “부검 및 혈액검사”가 바로 이런 평가야.</p>
<p class="box"><span class="tag">시험 포인트</span>안전성 = <pk>생체적합성·생분해성·전신 독성·(흡입 독성)·혈액 검사</pk>.</p>"""),
]
