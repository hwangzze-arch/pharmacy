# -*- coding: utf-8 -*-
"""22장 단권화 노트 PDF (사용자가 번역본을 공부하며 정리한 내용). python3 ch22_note.py → index.html → node render.js out.pdf"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.relpath(os.path.join(HERE, "..", "강의번역", "fonts"), HERE)
FONT = "".join(
    f"@font-face{{font-family:'NotoKR';font-weight:{w};src:url({FONTS}/noto-sans-kr-{s}-{w}-normal.woff2) format('woff2');}}"
    for s in ("korean", "latin", "latin-ext") for w in (400, 500, 700))

CSS = FONT + """
@page{size:A4;margin:15mm 15mm 16mm 15mm;}
*{box-sizing:border-box;}
body{font-family:'NotoKR','WenQuanYi Zen Hei',sans-serif;color:#1d2530;font-size:10.4pt;line-height:1.62;margin:0;-webkit-print-color-adjust:exact;print-color-adjust:exact;}
.cover{border-bottom:3px solid #2a9d8f;padding-bottom:8px;margin-bottom:12px;}
.cover .tag{display:inline-block;background:#2a9d8f;color:#fff;font-weight:700;font-size:9.5pt;border-radius:4px;padding:1px 9px;}
h1{font-size:19pt;color:#1f3f66;margin:6px 0 2px 0;line-height:1.3;}
.sub{color:#5f6b78;font-size:10pt;}
.law{background:#eef7f5;border:1px solid #a7d8cf;border-radius:8px;padding:8px 12px;margin:10px 0 6px 0;break-inside:avoid;}
.law h2{background:none;color:#1f5f56;padding:0;margin:0 0 6px 0;font-size:12.5pt;}
.law ol>li{margin-bottom:6px;}
h2{font-size:13pt;color:#fff;background:#1f3f66;padding:5px 11px;border-radius:6px;margin:18px 0 8px 0;break-after:avoid;}
h3{font-size:11.4pt;color:#1f3f66;margin:13px 0 5px 0;border-left:5px solid #2a9d8f;padding-left:8px;break-after:avoid;}
h4{font-size:10.6pt;color:#2a6f97;margin:8px 0 3px 0;break-after:avoid;}
p{margin:0 0 5px 0;}
ul,ol{margin:0 0 6px 0;padding-left:1.35em;}
li{margin:0 0 3px 0;}
b{color:#13253f;}
.qa{background:#fdf2f8;border:1px solid #f3c1dc;border-left:5px solid #e0559c;border-radius:6px;padding:6px 11px;margin:7px 0;break-inside:avoid;}
.qa .h{font-weight:700;color:#a4185f;font-size:9.6pt;margin-bottom:3px;}
.q{font-weight:700;color:#7a1550;margin:5px 0 2px 0;}
.q::before{content:'Q. ';color:#e0559c;}
.a{margin:0 0 4px 0;}
.a::before{content:'A. ';font-weight:700;color:#2a9d8f;}
.story{background:#fff8dc;border:1px solid #f0d77a;border-left:5px solid #f2c200;border-radius:6px;padding:5px 11px;margin:6px 0;}
.key{background:#ecf9e6;border:1px solid #a9db95;border-left:5px solid #4caf2c;border-radius:6px;padding:5px 11px;margin:6px 0;break-inside:avoid;}
.top{display:inline-block;background:#ffc4e3;color:#7a1550;font-weight:700;font-size:8.8pt;border-radius:3px;padding:0 6px;margin-right:4px;}
.pg{color:#5f6b78;font-weight:400;font-size:.85em;}
.ans{background:#f3f6fa;border-radius:4px;padding:3px 9px;display:inline-block;margin:2px 0;}
y{background:#fff07a;padding:0 2px;border-radius:2px;}
"""

BODY = """
<div class="cover"><span class="tag">단권화 완결본</span>
<h1>📘 제22장 카르보닐 알파 치환 반응<br>직관적 이해 &amp; Q&amp;A 총정리 노트</h1>
<div class="sub">CH22_약품유기화학2_번역본을 공부하며 생긴 궁금증과 설명을 정리한 노트 · 쪽 번호(p.)는 번역본 기준</div></div>

<div class="law"><h2>🌟 제22장을 꿰뚫는 '나만의 4대 만능 직관 공식'</h2>
<ol>
<li><b>엔올의 반응성 원리</b>: 산소(–OH)가 옆에 붙으면 탄소끼리 파이(π) 전자를 가운데 붙잡아두는 팽팽한 균형이 깨지고(결합 차수 저하) 공명으로 전자를 밀어주어, 반대편 끝인 <y>알파(α) 탄소 쪽으로 전자가 와르르 몰린다!</y> (그래서 일반 알켄보다 반응성이 훨씬 크고 α 탄소가 공격수가 됨)</li>
<li><b>산성도(pKa) 만능 공식</b>: 옆에서 전자를 밀어주는 방해꾼(N ＞ O ＞ CH₃)이 없을수록 → 카르보닐의 '전자 끌기'가 강해지고 → α 탄소의 전자를 강하게 뺏어 수소를 쉽게 쫓아내며(빠진 뒤 음전하도 산소가 잘 받아줌) → <y>산성도가 강해진다(작은 pKa)!</y></li>
<li><b>가열(Heat, Δ)의 법칙</b>: 반응 조건에 '가열'이 보이면 뻑뻑한 결합을 끊어내어 기체(CO₂, CO)로 날려버리거나(탈카르복실화), 작은 분자(HBr)를 뜯어내어 쪼개버릴 때(E2 제거 반응, 엔트로피 증가) 쓰는 필살기다!</li>
<li><b>비대칭 케톤의 위치 선택성</b>
<ul><li><b>산성 조건 (Br₂ + 아세트산)</b>: 천천히 가장 튼튼한 이중결합(자이체프 규칙)을 만드니까 <y>더 치환된(붐비는) 쪽</y>에 붙는다!</li>
<li><b>염기(LDA) 조건</b>: 양옆에 아이소프로필 날개를 단 뚱보 염기 LDA가 좁은 곳을 싫어하니까 <y>덜 치환된(한산한) 쪽</y>의 수소를 빠르게 뽑아 그쪽에 붙는다!</li></ul></li>
</ol></div>

<h2>PART 1. 산성 조건 α-할로젠화 및 엔올(Enol)의 반응 <span class="pg">(p.1 ~ p.19)</span></h2>

<h3>1. 알데하이드·케톤의 산성 α-할로젠화 메커니즘 <span class="pg">(p.8 ~ p.9)</span></h3>
<div class="story"><b>핵심 스토리</b>: "얌전한 케톤을 산(Acid)으로 자극해 공격적인 '엔올(Enol)'로 변신시킨 다음, 브로민(Br₂)을 낚아채고 다시 케톤 모양으로 돌아온다!" (8p 아세토페논과 9p 아세톤은 출발 물질의 왼쪽 덩어리만 다를 뿐 메커니즘은 100% 동일함)</div>
<h4>[1부: 엔올화 — 공격 준비 단계]</h4>
<p class="pg">(원래 케톤의 α 탄소는 단일결합만 있어 쓸 수 있는 전자가 없으므로 엔올로 변신해야 함)</p>
<ol><li><b>산소에 H⁺ 붙이기 (양성자화)</b>: 카르보닐 산소(C=O)가 주변 산(HBr 또는 아세트산)에서 H⁺를 뺏어옴 → 산소가 플러스(C=O⁺–H)를 띠며 전자가 고파져 옆 α 탄소의 전자를 맹렬히 끌어당김 → α-H가 아주 떨어지기 쉬운 상태가 됨.</li>
<li><b>α-H 떼어내고 '엔올' 만들기</b>: 약한 염기(Br⁻ 또는 CH₃COO⁻)가 덜렁거리는 α-H를 떼어감 → 남긴 전자쌍이 내려와 C=C 이중결합을 만들고 산소는 –OH가 되어 전자가 풍부한 <b>엔올(C=C–OH)</b> 완성!</li></ol>
<h4>[2부: 치환 — 공격 및 마무리 단계]</h4>
<ol start="3"><li><b>엔올이 Br₂ 공격하기</b>: –OH 산소가 비공유 전자쌍을 다시 내려보내면서(C=O 복구 시도), 그 힘으로 C=C 이중결합 전자쌍이 튀어나가 Br–Br 중 하나를 낚아챔 → α 탄소에 Br이 붙고 반대편은 Br⁻로 떨어져 나감.</li>
<li><b>H⁺ 버리고 C=O 복구하기</b>: Br⁻가 산소에 붙어있던 H⁺를 가져가면서(–HBr), 안정한 C=O 이중결합이 복구되며 <b>α-브로모 케톤</b> 탄생!</li></ol>
<div class="qa"><div class="h">💬 핵심 Q&amp;A 체크</div>
<p class="q">처음부터 플라스크에 아세트산과 Br₂를 다 같이 때려 넣는 거지? 그럼 1번의 수소는 아세트산의 수소일 수도 있고, 2번의 염기는 아세트산 음이온일 수도 있는 거네?</p>
<p class="a"><b>정확함!</b> 원팟(One-pot) 반응이라 처음엔 HBr이 없으므로 용매인 아세트산(CH₃COOH)이 H⁺를 주고, 짝염기인 아세트산 음이온(CH₃COO⁻)이 α-H를 떼어냄. 반응이 한 번 돌고 나면 ④번에서 강산인 HBr이 계속 새로 만들어지므로, 그 뒤부터는 HBr이 산 촉매 역할을 하여 반응이 갈수록 빨라짐(<b>자기 촉매 반응</b>).</p>
<p class="q">왜 산성 조건에서는 딱 1번만 브로민화되고 멈출까?</p>
<p class="a">새로 들어간 Br이 강력한 전자 끌개라서 카르보닐 산소의 전자까지 끌어당김 → 산소의 염기성이 낮아져 두 번째로 H⁺를 받아들이기(①번 양성자화 단계)가 너무 힘들어지므로 1번만 치환되고 멈춤.</p></div>

<h3>2. 반응 속도론과 중수소(D) 교환 실험 — 엔올 중간체의 증거 <span class="pg">(p.10 ~ p.11)</span></h3>
<div class="story"><b>직관적 비유 (맛집 주방과 손님)</b>: 케톤이 주방에서 '엔올'로 요리되어 나오는 데 무조건 10분(엄청 느림, 속도결정단계)이 걸리고, 엔올이 나오기만 하면 홀에 대기하던 손님(X₂ 또는 D₃O⁺)이 낚아채는 데는 단 1초(엄청 빠름)밖에 안 걸림.</div>
<h4>실험적 결론 2가지</h4>
<ol><li><b>할로젠(X₂)의 종류(Cl₂, Br₂, I₂)를 바꾸거나 농도를 늘려도 전체 반응 속도는 그대로다</b>: 가장 느린 병목 구간이 할로젠은 참여하지도 않는 '산 촉매 엔올 형성 단계'이기 때문! (속도 = k[케톤][H⁺], 속도식에 [X₂] 없음)</li>
<li><b>할로젠 대신 중수소 산(D₃O⁺)을 넣었을 때 α-H가 D로 바뀌는 속도가 할로젠화 속도와 정확히 똑같다</b>: 엔올 메커니즘을 아는 우리 눈엔 D로 바뀌는 게 당연하지만, 옛날 과학자들에게는 <i>"Br₂가 직접 부딪혀 치환하는 게 아니라, 둘 다 똑같은 느린 단계(엔올 형성)를 거쳐 똑같은 공통 중간체(엔올)를 공유한다!"</i>는 것을 증명한 스모킹 건(결정적 증거)이었음.</li></ol>
<div class="qa"><div class="h">💬 핵심 Q&amp;A 체크</div>
<p class="q">10페이지 메커니즘에서 선 끝에 H라고 굳이 적어준 건 탄소가 아님을 알려주는 약속이야?</p>
<p class="a"><b>맞음!</b> 골격 구조식에서 글자 없는 선 끝은 무조건 메틸기(–CH₃)를 뜻함. 왼쪽 아래 H는 케톤뿐만 아니라 알데하이드(–CHO)도 포함한다는 걸 보여주려 적은 것이고, 오른쪽 아래 α-H는 물(H₂O)이 공격해서 떼어내는 메커니즘 화살표를 그리기 위해 생략하지 않고 꺼내 그려준 것임.</p></div>

<h3>3. α-브로모 케톤의 제거 반응 — α,β-불포화 케톤 만들기 <span class="pg">(p.12)</span></h3>
<h4>용어 정리 ('불포화 케톤'이란?)</h4>
<ul><li><b>포화</b>: 탄소끼리 전부 단일결합(C–C)이라 수소가 꽉 찬 상태.</li>
<li><b>불포화</b>: 수소가 빠져 C=C 이중결합이 들어있는 상태.</li>
<li><b>α,β-불포화 케톤</b>: 카르보닐기(C=O) 바로 옆(α 탄소와 β 탄소 사이)에 C=C 이중결합이 붙어있어 콘쥬게이션(O=C–C=C)으로 안정화된 케톤!</li></ul>
<h4>2단계 합성 과정 (예: 2-메틸사이클로헥사논)</h4>
<ol><li><b>1단계 (Br₂, 아세트산)</b>: 산성 조건이므로 더 안정한 사치환 엔올(자이체프 규칙)을 거쳐 더 치환된 오른쪽(C2, 메틸기 있는 쪽)에 Br이 붙음.</li>
<li><b>2단계 (피리딘(Pyridine), 가열(Heat))</b>: 약하고 덩치 있는 염기인 피리딘이 C=O는 공격하지 않고 바깥의 β-H(C3의 수소)만 떼어내면서 동시에 Br⁻가 튕겨 나가는 <b>E2 제거 반응</b>이 일어나 C=C 이중결합 생성!</li></ol>
<div class="qa"><div class="h">💬 핵심 Q&amp;A 체크</div>
<p class="q">여기서 가열(Heat)은 왜 해주는 거야?</p>
<p class="a">① 피리딘이 부반응을 막기 위해 고른 '약한 염기'라서, 뻑뻑한 β-H를 뜯어내려면 열에너지로 등짝을 밀어줘야(활성화 에너지 극복) 하고, ② 원래 모든 제거 반응(쪼개져서 조각 수가 늘어나는 반응)은 무질서도(엔트로피, ΔS)가 증가하므로 온도(T)를 높여줄수록 훨씬 잘 일어나며, ③ 고리가 비틀어져야 H와 Br이 180도(안티) 각도를 맞출 수 있기 때문!</p></div>

<h3>4. 카르복실산의 α-브로민화 — HVZ 반응 <span class="pg">(p.13 ~ p.16)</span></h3>
<h4>왜 카르복실산(과 에스터·아마이드)은 그냥 Br₂와 반응하지 않을까?</h4>
<p>카르복실산(–COOH), 에스터(–COOR), 아마이드(–CONH₂)는 C=O 바로 옆의 산소(O)나 질소(N)가 비공유 전자쌍을 C=O에 팍팍 퍼주어 이미 배가 부른 상태임 → 굳이 옆의 α 탄소를 끌어당기지 않으므로 엔올이 거의 만들어지지 않음! (게다가 카르복실산은 –COOH의 산성 수소가 먼저 반응해 버림)</p>
<h4>해결책 (1. Br₂, PBr₃ / 2. H₂O)</h4>
<ul><li><b>PBr₃ (삼브로민화 인)</b>: –OH를 만나면 무조건 –Br로 바꿔치기해 주는 전문 해결사 시약!</li></ul>
<ol><li><b>변장하기 (13~14p 메커니즘)</b>: 카르복실산의 –OH가 PBr₃의 인(P)을 공격해 달라붙으면 아주 잘 떨어지는 모래주머니(–OPBr₂, 좋은 이탈기)가 됨 → 방금 튕겨 나갔던 Br⁻가 다시 C=O 탄소를 공격해 올라갔다가(O⁻), 다시 내려오면서 –OPBr₂를 쫓아내어(친핵성 아실 치환) 엔올화가 아주 잘 되는 <b>'산 브로마이드(R–CH₂–COBr)'</b>로 변장 완료! (14p 아래쪽 그림은 이 산 브로마이드가 15~16p 과정을 거쳐 최종 생성물이 된다는 전체 요약표임)</li>
<li><b>엔올화 (15p)</b>: 산 브로마이드가 HBr 촉매 하에 산 브로마이드 엔올로 변신!</li>
<li><b>α-브로민화 (16p 왼쪽 ③)</b>: 엔올의 C=C가 Br₂를 공격해 α 자리에 Br을 붙임 (α-브로모 산 브로마이드 생성 — <span class="top">주의</span>물 넣기 전 1단계 중간 생성물을 물어보면 이걸 그려야 함!).</li>
<li><b>변장 해제 (16p 오른쪽 ④~⑤)</b>: 두 번째 시약인 물(H₂O)을 넣으면, 물이 C=O 탄소를 공격해 올라갔다가(O⁻) 다시 내려오면서 임시직이었던 Br⁻를 쫓아내고 원래의 카르복실산(<b>α-브로모 카르복실산</b>)으로 복구됨!</li></ol>

<h3>5. 의약품 실전 1: 부프로피온 염산염(항우울제·금연보조제) 합성 <span class="pg">(p.17 ~ p.19)</span></h3>
<h4>전체 4단계 흐름</h4>
<ol><li><b>니트릴 → 케톤 (1. EtMgBr / 2. H₃O⁺, 17~18p)</b>
<div class="qa"><p class="q">왜 니트릴 상태로는 바로 Br을 못 붙여? 그리고 Et가 에틸렌이야?</p>
<p class="a">출발 물질(3-클로로벤조니트릴)에는 아직 α 탄소(탄소 다리) 자체가 아예 없고 니트릴은 엔올화도 잘 안 됨! 또한 Et는 이중결합인 에틸렌이 아니라 단일결합 탄소 2개짜리 부품인 <b>'에틸기(–CH₂CH₃)'</b>임 (Me=1개, Et=2개, Pr=3개, Bu=4개, Ph=벤젠). 즉, EtMgBr을 넣어 탄소 2개짜리 다리를 붙여줌과 동시에 가수분해하여 케톤(빈칸 ①)으로 만드는 일석이조 단계임!</p></div></li>
<li><b>산성 α-브로민화 (Br₂, DCM, 19p 위)</b>: 방금 만든 케톤이 엔올로 변신해 Br₂를 공격하여 α 자리에 Br 장착 (빈칸 ②: α-브로모 케톤).</li>
<li><b>아민화 (t-BuNH₂, ACN, 19p 아래)</b>: 아민의 질소(N)가 Br이 붙은 α 탄소의 등 뒤를 S<sub>N</sub>2 공격하여 Br⁻를 밀어내고 아민 장착 (빈칸 ③: 부프로피온).</li>
<li><b>염산염 포장 (HCl, 19p 맨 끝)</b>: 물(체액)에 잘 녹고 안정한 알약으로 만들기 위해 HCl을 넣어 아민 질소에 H⁺를 붙여 이온 소금 형태(부프로피온 염산염)로 만듦.</li></ol>

<h2>PART 2. α-수소의 산성도(pKa)와 엔올레이트(Enolate)의 반응 <span class="pg">(p.20 ~ p.26)</span></h2>

<h3>1. 케톤 vs 니트릴 산성도 심층 비교 &amp; 엔올레이트 형성 <span class="pg">(p.20)</span></h3>
<div class="qa"><div class="h">💬 핵심 Q&amp;A 체크</div>
<p class="q">니트릴(–C≡N)은 삼중결합이라 전자를 더 잘 당길 텐데, 왜 이중결합인 케톤(pKa=19)이 니트릴(pKa=25)보다 산성도가 백만 배나 더 높을까?</p>
<p class="a">단순 유발 효과는 삼중결합이 세지만, 수소가 빠진 뒤 만들어지는 <b>공명 음이온의 안정성</b>에서 케톤이 압승하기 때문!</p>
<ol><li><b>음전하를 최종적으로 받아주는 원자의 전기음성도</b>: 케톤은 전자를 엄청 좋아하는 산소(O⁻)가 음전하를 떠안지만(C=C–O⁻), 니트릴은 산소보다 전기음성도가 작은 질소(N⁻)가 떠안아야 함(C=C=N⁻).</li>
<li><b>구조적 편안함</b>: 니트릴이 공명하면 가운데 탄소를 중심으로 이중결합 2개가 연속된 뻣뻣하고 불편한 구조(C=C=N⁻)가 되어 공명 안정화 효과가 케톤보다 떨어짐.</li></ol></div>
<h4>케톤을 100% 엔올레이트로 바꾸려면? (20p)</h4>
<ul><li>케톤(pKa=19)에 평범한 염기인 NaOH나 NaOEt(짝산 pKa ≈ 16)를 넣으면 역반응이 더 잘 일어나 일부(0.1%)만 엔올레이트가 됨.</li>
<li>100% 완전 전환시키려면 수소를 먹고 수소 기체로 날아가 버리는 <b>NaH</b>(짝산 H₂ pKa=35)나 초강력 염기 <b>LDA</b>(짝산 pKa=36)를 써야 함!</li></ul>

<h3>2. 초강력 뚱보 염기 LDA 집중 탐구 <span class="pg">(p.21)</span></h3>
<h4>왜 그냥 뷰틸리튬(BuLi)을 안 쓰고 LDA를 만들어 쓸까?</h4>
<ul><li>BuLi는 힘은 세지만 날렵해서 α-H를 떼는 대신 C=O 탄소를 직접 공격(친핵성 첨가)해 버림.</li>
<li>그래서 다이아이소프로필아민(pKa=36)에 BuLi를 넣어 뷰테인 가스(C₄H₁₀)를 날리고 양옆에 거대한 아이소프로필기 날개 2개가 달린 질소 음이온 염기(LDA)를 만듦!</li></ul>
<div class="key"><b>LDA의 3대 장점</b>
<ol><li><b>엄청난 강염기(짝산 pKa=36)</b>: 케톤(19)이나 에스터(25)를 100% 완전히 엔올레이트로 전환함.</li>
<li><b>엄청난 덩치(입체 장애)</b>: 뚱뚱해서 좁은 C=O 탄소는 절대 공격 못 하고 오직 바깥의 α-H만 떼어내는 순수 염기로만 작동함.</li>
<li><b>저온(−78 °C, THF) 작동 &amp; 위치 선택성</b>: 비대칭 케톤에서 덜 붐비는 한산한 쪽의 α-H를 선택적으로 빠르게 떼어냄(속도론적 엔올레이트).</li></ol></div>

<h3>3. 두 카르보닐 사이의 수소(샌드위치 효과)와 pKa 총정리 표 <span class="pg">(p.22 ~ p.23)</span></h3>
<h4>1,3-다이카르보닐의 샌드위치 효과 (22p)</h4>
<ul><li>양옆에 카르보닐기 2개가 있으면 양쪽에서 동시에 전자를 강하게 끌어당기고, 수소가 빠진 뒤 음전하도 [왼쪽 산소 + 가운데 탄소 + 오른쪽 산소] 3군데로 분산되므로 산성도가 폭발적으로 강해짐(pKa=9~13).</li>
<li><b>장점</b>: 비싼 LDA 없이 흔한 NaOEt(짝산 pKa=16)만 넣어도 100% 엔올레이트로 완전 전환됨!</li></ul>
<div class="key"><span class="top">시험 1순위</span><b>'전자 끌기 논리'로 완벽 정리하는 산성도(pKa) 순서 (22~23p)</b>
<ul><li><b>1,3-다이케톤(pKa=9) ＞ 3-케토 에스터(11) ＞ 1,3-다이에스터(말론산 에스터, 13)</b>: 에스터(–OEt)의 산소가 자기 C=O에 전자를 밀어 넣어 배부르게 만드니까, 에스터가 많을수록 가운데 탄소의 전자를 끌어당기는 힘이 약해져 산성도가 약해짐!</li>
<li><b>단일 작용기 α-H 산성도 순서</b>: 산 염화물(16, Cl이 전자를 당김) ＞ 알데하이드(17) ＞ 케톤(19, 메틸기가 전자를 살짝 밀어 방해) ＞ 싸이오에스터(21) ＞ 에스터(25) ≈ 니트릴(25) ＞ 다이알킬아마이드(30, 질소가 전자를 팍팍 밀어 방해) ＞ 다이알킬아민(36, N–H). (※ 카르복실산 5, 알코올 16은 O–H의 산성도임)</li></ul></div>

<h3>4. 엔올레이트의 반응성(O vs C) 및 염기 촉진 할로젠화·할로폼 반응 <span class="pg">(p.24 ~ p.26)</span></h3>
<h4>왜 엔올레이트는 산소(O⁻)가 아니라 알파 탄소(C⁻)로 공격할까? (24p)</h4>
<p>산소에 친전자체(E)가 붙으면 약한 C=C 이중결합만 남지만, 알파 탄소(C)에 E가 붙으면 훨씬 강력하고 튼튼한 C=O 이중결합을 되살릴 수 있어서 결과물이 훨씬 안정하기 때문!</p>
<h4>왜 염기성 조건(Br₂ + NaOH) 할로젠화는 1번에서 안 멈추고 끝까지 폭주할까? (25p → 26p)</h4>
<ul><li>첫 번째 할로젠(X)이 붙으면, X의 강력한 '전자 끌기' 때문에 같은 탄소에 남은 두 번째, 세 번째 수소의 산성도가 처음보다 훨씬 더 강해짐!</li>
<li>따라서 염기(OH⁻)는 새 케톤을 건드리는 대신 이미 X가 붙어 수소가 헐거워진 바로 그 탄소의 남은 수소를 빛의 속도로 마저 다 뽑아내어 –CH₃가 –CX₃가 될 때까지 3번 연속 폭주함!</li></ul>
<h4>할로폼(Haloform) 반응 (26p)</h4>
<ul><li>메틸 케톤(R–CO–CH₃)에 과량의 염기와 할로젠(NaOH, X₂)을 넣으면 R–CO–CX₃가 된 뒤, OH⁻가 C=O 탄소를 공격함.</li>
<li>올라갔던 O⁻가 내려오면서 옆의 –CX₃를 통째로 쫓아냄! (원래 탄소 음이온은 못 떨어지지만, 할로젠 3개가 전자를 세 방향에서 강하게 끌어당겨 음이온을 안정화해 주므로 ⁻CX₃는 예외적으로 좋은 이탈기가 됨!)</li>
<li>마지막에 ⁻CX₃가 R–COOH의 수소를 뺏어 최종적으로 <b>[탄소 1개 줄어든 카르복실산염(R–COO⁻)] + [할로폼(CHX₃)]</b> 생성! (I₂/NaOH를 쓰면 노란색 침전물인 아이오도폼 CHI₃가 생겨 메틸 케톤 확인 시험으로 쓰임)</li></ul>

<h2>PART 3. 엔올레이트의 알킬화 — 탄소 뼈대 키우기 <span class="pg">(p.27 ~ p.44)</span></h2>

<h3>1. 엔올레이트 알킬화의 기본 틀과 S<sub>N</sub>2 제약 조건 <span class="pg">(p.27 ~ p.28)</span></h3>
<ul><li><b>기본 2단계 메커니즘 (27p)</b>: ① 염기로 α-H를 떼어 엔올레이트(C⁻) 형성 → ② 엔올레이트(C⁻)가 알킬 할라이드(R–X)의 등 뒤를 S<sub>N</sub>2 공격하여 X⁻를 쫓아내고 알파 자리에 R 장착!</li>
<li><b>제약 조건 (28p — 유기1 S<sub>N</sub>2 규칙 그대로!)</b>
<ul><li>타깃인 R–X가 날렵한 메틸기, 1차 할라이드(특히 알릴, 벤질)일 때만 알킬화가 잘 됨!</li>
<li>2차 할라이드는 느리고 수율이 낮으며, 뚱뚱한 3차 할라이드(예: t-BuBr)는 S<sub>N</sub>2가 아예 불가능하여 제거 반응(E2, 알켄 생성)만 일어남! 또한 바이닐(C=C–X)이나 아릴 할라이드(벤젠 고리 Ph–X)도 S<sub>N</sub>2 절대 불가(×)!</li></ul></li></ul>

<h3>2. 말론산 에스터 합성 — 카르복실산(R–CH₂COOH) 만들기 <span class="pg">(p.29 ~ p.36)</span></h3>
<ul><li><b>말론산이란?</b> 가운데 CH₂ 양옆에 –COOH 2개가 달린 탄소 3개짜리 산(HOOC–CH₂–COOH). (※ 다이카르복실산 암기: 가운데 CH₂가 0개면 옥살산, 1개면 말론산, 2개면 숙신산 — <b>"옥-말-숙"</b>)</li>
<li><b>원리</b>: 일반 에스터는 수소가 안 빠져서 알킬화가 힘드니까, 양쪽에 에스터 2개가 달린 말론산 에스터(EtO₂C–CH₂–CO₂Et, pKa=13)를 써서 쉽게 알킬화한 뒤 마지막에 여분의 에스터 1개를 CO₂ 가스로 날려버리는 기술!</li></ul>
<h4>3단계 흐름</h4>
<ol><li><b>1차 알킬화 (30p)</b>: 1. NaOEt, EtOH (에스터 교환 부반응 막으려고 같은 –OEt 염기 사용) → 2. R–X 넣어 가운데 탄소에 R 장착!</li>
<li><b>2차 알킬화 — 다이알킬화 (31p, 선택)</b>: 가운데 탄소에 남은 수소 1개를 NaOEt → R′–X로 한 번 더 뽑아 두 번째 알킬기(R′) 장착 가능! (고리 만들기 응용(36p): Br–(CH₂)ₙ–Br처럼 양쪽 끝에 Br이 달린 시약을 쓰면 분자 간/분자 내 알킬화가 연속으로 일어나 고리형 카르복실산 생성!)</li>
<li><b>가수분해 및 탈카르복실화 (32~33p)</b>: H₃O⁺, 가열(Heat) 처리! 양쪽 에스터가 둘 다 –COOH로 가수분해된 뒤, 가열하면 두 카르보닐기가 6각형 고리(6원 고리 전이상태, 33p)를 이루며 수소를 주고받아 한쪽 –COOH가 CO₂ 기체로 날아가고 산 엔올을 거쳐 모노카르복실산(R–CH₂–COOH 또는 RR′CH–COOH) 완성!</li></ol>

<h3>3. 아세토아세트산 에스터 합성 — 메틸 케톤(R–CH₂COCH₃) 만들기 <span class="pg">(p.37 ~ p.38)</span></h3>
<h4>말론산 에스터와의 유일한 차이점 (37p)</h4>
<ul><li>출발 물질의 왼쪽이 에스터가 아니라 케톤(CH₃CO–CH₂–CO₂Et, pKa=11)임!</li>
<li>따라서 똑같이 NaOEt / R–X로 1~2회 알킬화한 뒤 H₃O⁺, 가열로 오른쪽 에스터(–CO₂Et)를 CO₂ 가스로 날려버리면, 왼쪽 케톤이 그대로 남아 <b>메틸 케톤(R–CH₂–COCH₃)</b>이 됨!</li></ul>
<h4>일반화 — 고리형 β-케토 에스터의 활용 이유 (38p)</h4>
<p>사이클로헥사논 옆에 에스터(–CO₂Et)가 붙어있으면, 그 에스터가 "무조건 두 카르보닐 사이(C2)의 수소만 뽑아서 여기에만 깔끔하게 알킬화해!"라고 위치를 지정해 주는 <b>길 안내 도우미</b> 역할을 함. 알킬화(NaOEt / PhCH₂Br)가 끝나면 H₃O⁺, 가열로 도우미 에스터를 CO₂로 날려버려 깔끔한 2-벤질사이클로헥사논을 얻음!</p>

<h3>4. 의약품 실전 2: 페노바르비탈(항경련제) 합성 <span class="pg">(p.39 ~ p.41)</span></h3>
<div class="story"><b>핵심 전략</b>: 벤젠 고리(Ph–Br)는 S<sub>N</sub>2 알킬화로 붙일 수 없으므로, 처음부터 벤젠 고리가 달린 니트릴에서 출발해 우회하여 페닐말론산 에스터를 만든다!</div>
<ol><li><b>Ph–CH₂–CN + EtOH/산</b> → 니트릴이 에스터로 바뀜 (빈칸 ①: Ph–CH₂–CO₂Et).</li>
<li><b>NaOEt + 옥살산 다이에틸((EtO₂C)₂)</b> → 엔올레이트가 옥살산 에스터를 공격해 –OEt를 쫓아내고 달라붙음 (빈칸 ②: α-케토 에스터 중간체).</li>
<li><b>Heat(가열)</b> → 열에 의해 여분의 카르보닐기가 일산화탄소(CO 기체)로 날아가 벤젠이 장착된 페닐말론산 다이에틸 완성!</li>
<li><b>1. NaOEt / 2. EtBr (40p)</b> → 남은 가운데 α-H 하나를 뽑고 S<sub>N</sub>2로 에틸기(Et) 장착 (빈칸 ③: Ph와 Et가 모두 달린 말론산 에스터).</li>
<li><b>요소(Urea, NH₂CONH₂, 41p)</b> → 요소의 양쪽 NH₂가 두 에스터를 차례로 공격(–OEt 2개 이탈)하여 6각형 고리를 닫으면 <b>페노바르비탈</b> 완성!</li></ol>

<h3>5. LDA를 이용한 직접 알킬화 &amp; 생체 내 알킬화 <span class="pg">(p.42 ~ p.44)</span></h3>
<ul><li><b>직접 알킬화 (42p)</b>: 에스터 도우미를 달았다 날리는 과정 없이, 단일 카르보닐(케톤, 에스터, 락톤, 니트릴)에 초강력 염기 1. LDA, THF를 넣어 100% 엔올레이트로 만든 뒤 2. R–X를 넣어 한 방에 α 자리에 R을 붙임! (이때 엔올레이트 쪽이 3차 탄소로 붐벼도 타깃인 CH₃I가 날렵하면 S<sub>N</sub>2 잘 됨!)</li></ul>
<div class="key"><span class="top">시험 1순위</span><b>비대칭 케톤(2-메틸사이클로헥사논)의 LDA 직접 알킬화 (43p)</b><br>
1. LDA, THF / 2. CH₃I 처리 시, 뚱보 염기 LDA는 메틸기가 있어 비좁은 오른쪽(C2)을 피하고 한산하고 덜 붐비는 왼쪽(C6)의 수소를 빠르게 뽑아내므로, 왼쪽(C6)에 메틸기가 붙은 <b>2,6-다이메틸사이클로헥사논(56%)</b>이 주생성물이 됨! (산성 조건 브로민화와 정반대 위치!)</div>
<ul><li><b>생체 내 알킬화 — 인돌마이신 생합성 (44p)</b>: 실험실의 LDA 대신 효소의 염기·산 잔기가 협동해 엔올을 만들고, 실험실의 CH₃I 대신 생체 메틸기 공여체인 SAM(S⁺–CH₃)을 엔올이 S<sub>N</sub>2 공격하여 α-메틸화를 수행함.</li></ul>

<h2>PART 4. 연습문제 4선 완벽 해설 <span class="pg">(p.45 ~ p.54)</span></h2>

<h3>1. 문제 22-37: 산성 수소(pKa ＜ 25) 모두 찾기 <span class="pg">(p.45 ~ p.46)</span></h3>
<ul><li><b>(a) CH₃CH₂CH(CH₃)COCH₃</b>: C=O 양옆의 CH(1개) + CH₃(3개) = 총 4개.</li>
<li><b>(b) 사이클로펜테인-1,3-다이온</b>: 두 C=O 사이 C2의 CH₂(2개, 가장 산성 pKa ≈ 9) + 아래쪽 C4·C5의 CH₂–CH₂(4개, pKa ≈ 19) = 고리의 수소 6개 전부!</li>
<li><b>(c) HOCH₂CH₂CO–C≡C–CH₃</b>: 알코올의 –OH(가장 산성, pKa=16) + C=O 왼쪽 옆 CH₂(2개) + 삼중결합 끝의 CH₃(3개, 수소가 빠지면 음전하가 C≡C 다리를 타고 C=O 산소까지 공명 분산되므로 산성!).</li>
<li><b>(d) 2-(사이아노메틸)벤조산 메틸</b>: 니트릴 옆 벤질 위치인 –CH₂CN의 수소 2개만 해당 (벤젠 고리 H와 에스터 –OCH₃는 아님).</li>
<li><b>(e) 사이클로펜테인카르보닐 클로라이드</b>: –COCl 바로 옆 고리 탄소의 α-H 1개.</li>
<li><b>(f) CH₃CH₂CO–C(CH₃)=CH₂</b>: 왼쪽 에틸기의 CH₂ 2개만 해당 (이중결합 쪽은 제외).</li></ul>

<h3>2. 문제 22-38: 산성도 증가 순서(약한 산 → 강한 산) 배열 <span class="pg">(p.47 ~ p.48)</span></h3>
<p><b>정답 순서</b>: <span class="ans">(c) (CH₃CH₂)₂NH (pKa ≈ 36) ＜ (d) CH₃COCH₃ (19) ＜ (b) CH₃CH₂OH (16) ＜ (e) CH₃COCH₂COCH₃ (9) ＜ (a) CH₃CH₂CO₂H (4.8) ＜ (f) CCl₃CO₂H (0.7)</span></p>
<div class="key"><b>핵심 포인트</b>: 아세톤(케톤, 19)보다 산소가 100% 음전하를 들고 있는 에탄올(알코올, 16)이 더 강한 산이며, 같은 카르복실산끼리는 전자 끌개(Cl 3개)의 유발 효과가 있는 (f)가 압도적으로 가장 강한 산임!</div>

<h3>3. 문제 22-42: 생성물 예측 4종 <span class="pg">(p.49 ~ p.51)</span></h3>
<ul><li><b>(a) 사이클로헥세인-1,1-다이카르복실산 + Heat</b>: 같은 탄소에 –COOH가 2개일 때 가열하면 탈카르복실화되어 1개가 CO₂로 날아감 → <b>사이클로헥세인카르복실산 + CO₂</b></li>
<li><b>(b) 사이클로펜테인-1,3-다이온 + 1. NaOEt / 2. CH₃I</b>: 두 C=O 사이(C2)에 메틸기가 붙음 → <b>2-메틸사이클로펜테인-1,3-다이온</b></li>
<li><b>(c) 뷰탄산(CH₃CH₂CH₂COOH) →(Br₂, PBr₃) ? →(H₂O) ?</b> (HVZ 반응)
<ul><li>첫 번째 물음표(물 넣기 전): <b>2-브로모뷰타노일 브로마이드</b> (CH₃CH₂CH(Br)COBr)</li>
<li>두 번째 물음표(물 넣은 후): <b>2-브로모뷰탄산</b> (CH₃CH₂CH(Br)COOH)</li></ul></li>
<li><b>(d) 아세토페논(PhCOCH₃) + NaOH, H₂O, I₂</b> (할로폼 반응): 메틸기가 잘려 노란 침전이 됨 → <b>벤조산염(PhCOO⁻ Na⁺) + 아이오도폼(CHI₃)</b></li></ul>

<h3>4. 문제 22-54: 빠진 시약 a~c 채우기 — 종합 문제 <span class="pg">(p.52 ~ p.54)</span></h3>
<ul><li><b>시약 a</b> (고리형 β-케토 에스터의 두 카르보닐 사이에 메틸기 장착): <span class="ans">1. NaOCH₃, CH₃OH / 2. CH₃I</span> (출발 물질이 메틸 에스터 –CO₂CH₃이므로 에스터 교환을 막기 위해 NaOCH₃ 사용)</li>
<li><b>시약 b</b> (길 안내 도우미였던 –CO₂CH₃를 가수분해 후 CO₂로 날려버림): <span class="ans">H₃O⁺, Heat(가열)</span></li>
<li><b>시약 c</b> (2-메틸사이클로헥사논의 덜 붐비는 반대쪽 C6 위치에 선택적으로 메틸기 장착): <span class="ans">1. LDA, THF / 2. CH₃I</span> (뚱보 염기 LDA를 이용한 속도론적 직접 알킬화!)</li></ul>
"""

html = f'<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>CH22 단권화 노트</title><style>{CSS}</style></head><body>{BODY}</body></html>'
open(os.path.join(HERE, "index.html"), "w").write(html)
print("ok")
