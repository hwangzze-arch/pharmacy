# -*- coding: utf-8 -*-
"""22장 핵심판 (약 25쪽): 녹취 강조 · 과제 · 수업 중 문제 · 중간고사 형식에 맞는 것만.
전체판(c00–c90)의 내용을 골라 합친다 — 고칠 때는 전체판 파일을 고치면 둘 다 바뀐다."""
import copy
from parts import *
import c00_front, c10_p1, c20_p2, c30_p3, c90_final

ALL = c00_front.E + c10_p1.E + c20_p2.E + c30_p3.E + c90_final.E


def g(key):
    return copy.deepcopy(next(e for e in ALL if e.get("id") == key))


def q(text):
    return copy.deepcopy(next(e for e in ALL if e["t"] == "q" and (text in e.get("title", "") or text in e.get("src", ""))))


def side(e, *kinds):
    return [x for x in e.get("side", []) if x[0] in kinds]


# ── 앞쪽 1쪽: 반응 지도 + 사용법
front = g("f-map")
front["html"] = front["html"].replace("읽기 전에 ③", "22장 핵심판").replace("22장 한 장 지도 · 4대 직관 공식", "22장 한 장 지도 · 4대 직관 공식 · 이 노트 쓰는 법")
front["html"] = front["html"].replace('<div class="card tip"><div class="ct">📌 문제 읽는 법</div>',
    '<div class="card"><div class="ct">🎯 핵심판 기준</div>녹취 강조 · 과제 22-37·38·42·54 · 수업 중 푼 문제(부프로피온·페노바르비탈) · 중간고사 형식(시약+출발물질 메커니즘, 시약 쓰기, 산 세기 순서)만 남겼어. 나머지는 전체판(61쪽)에.</div><div class="card tip"><div class="ct">📌 문제 읽는 법</div>')

# ── 개념 10쪽
taut, enolrx = g("c-taut"), g("c-enolrx")
k1 = taut
k1.update(title="엔올 — 토토머화(산·염기)와 α-치환의 틀", sub="Keto–enol tautomerism · reactivity of enols · 슬라이드 2–7",
          core="엔올은 극미량이지만 <b>반응하려고</b> 만든다. 산: O 양성자화 → α-H 제거 / 염기: α-H 제거 → O 양성자화. 엔올이 E⁺를 잡고 H⁺를 버리면 <b>α-치환</b>.",
          detail=taut["detail"] + '<p><b>α-치환 틀</b>(슬 7): 엔올 C=C가 E⁺ 공격 → O–H의 H⁺ 제거 → C=O 복귀. E = Br₂, D₃O⁺, (HVZ) Br₂/PBr₃.</p>',
          side=side(taut, "img", "rec") + side(enolrx, "my"),
          one="산은 ‘O 먼저’, 염기는 ‘α-H 먼저’. 엔올은 E⁺ 잡고 → H⁺ 버리고 → C=O 복귀!")

acidbr, rate = g("c-acidbr"), g("c-rate")
k2 = acidbr
k2.update(title="산성 α-할로젠화 + 속도론", sub="Acid-catalyzed α-halogenation · rate law · 슬라이드 8–10",
          detail=acidbr["detail"] + '<p><b>속도론</b>(슬 10): 속도 = k[케톤][H⁺], <y>[X₂] 없음</y> + D₃O⁺ 교환 속도 = 할로젠화 속도 → 느린 단계 = <g>엔올 형성</g>(공통 중간체).</p>',
          side=side(acidbr, "img", "my") + side(rate, "ana"))

acid, pka = g("c-acid"), g("c-pka")
k6 = pka
k6.update(title="엔올레이트 — 강염기(NaH·LDA)와 pKa 사다리", sub="Enolate formation · LDA · Table 22.1 · 슬라이드 15–18",
          core="케톤 α-H 19 → NaOEt(16)로는 일부만, <b>NaH·LDA</b>로 완전히. 두 C=O 사이 H는 9–13이라 <b>NaOEt로 충분</b>.",
          detail=pka["detail"] + '<p><b>LDA</b> = 다이아이소프로필아민 + BuLi. 강함(36) · 부피 큼(C=O 공격 ✗, H만) · −78 °C에서 <y>덜 붐비는 쪽</y>.</p>',
          side=side(pka, "img") + side(acid, "rec", "my"), mech=MSR(16, 1))

alk, mal, dec = g("c-alk"), g("c-mal"), g("c-decarb")
k8 = mal
k8.update(title="말론산 에스터 합성 — S<sub>N</sub>2 제약 · NaOEt · 탈카르복실화", sub="Alkylation · malonic ester synthesis · decarboxylation · 슬라이드 22–30",
          core="R–X → <b>R–CH₂–COOH</b>: ① NaOEt ② R–X (S<sub>N</sub>2) ③ H₃O⁺, 가열(가수분해 + <b>β-카르보닐</b> 6원 고리로 −CO₂).",
          detail="""<ul><li><b>S<sub>N</sub>2 제약</b>: CH₃·1°·알릴·벤질 ○, 2° △, <pk>3°(E2)·바이닐·아릴 ✗</pk>. 이탈기 OTs &gt; I &gt; Br &gt; Cl.</li>
<li><b>NaOEt</b>: pKa 13 &lt; 16 → 완전 전환. NaOH는 <pk>가수분해</pk>, NaOMe는 에스터 교환 → 같은 알콕사이드.</li>
<li>α-H 2개 → 알킬화 <b>최대 2번</b>. Br(CH₂)ₙBr + 2 NaOEt → (n+1)원 고리.</li>
<li><b>탈카르복실화</b>: COOH의 H가 β 위치 C=O 산소로 → 화살표 3개 → CO₂ + 엔올 → 토토머화. β 카르보닐 없으면(γ, 단순 산) ✗.</li>
<li><b>역합성</b>: 목표 산의 α 탄소 + COOH = 말론산, α의 가지 = R–X.</li></ul>""",
          side=side(mal, "img", "rec"), mech=MSR(25, 0, 1) + MSR(27, 1).replace("④ 가열", "③ 가열"),
          one="말론산 = NaOEt → R–X → H₃O⁺/Δ. NaOH 금지, 3°·아릴 금지, β-카르보닐 있어야 −CO₂!")

phb, lda = g("c-phb"), g("c-lda")
k10 = phb
k10.update(title="페노바르비탈 · LDA 직접 알킬화", sub="Phenobarbital · direct alkylation · 슬라이드 33–35",
           core="페닐은 S<sub>N</sub>2 불가 → <b>처음부터 페닐</b>을 갖고 시작(→ 전체 메커니즘 다음 쪽). 단일 카르보닐은 <b>1. LDA 2. R–X</b>, 비대칭 케톤은 <b>덜 붐비는 쪽</b>.",
           detail=phb["detail"] + '<p><b>LDA 직접 알킬화</b>(슬 34–35): 2-메틸사이클로헥사논 → 2,6-다이메틸(56 %) ≫ 2,2-(6 %). 산성 브로민화(더 치환된 쪽)와 반대.</p>',
           side=side(phb, "img", "rec") + side(lda, "my"), mech=MSR(35, 0, 1))

bup_m = next(copy.deepcopy(e) for e in c10_p1.E if e.get("cls") == "mfull")
bup_m["id"] = "m-bup"
phb_m = [copy.deepcopy(e) for e in c30_p3.E if e.get("cls") == "mfull" and "페노바르비탈 — 전체" in e["html"]]
phb_m[0]["id"] = "m-phb"
concepts = [k1, k2, g("c-e2"), g("c-hvz"), g("c-bup"), bup_m, k6, g("c-haloform"), k8, g("c-aae"), k10] + phb_m
for e in concepts:
    if e["t"] == "c":
        e["part"] = "핵심 개념"
    else:
        e["html"] = e["html"].replace(P1, "핵심 개념").replace(P3, "핵심 개념")

# ── 문제 11개
probs = [q("22-37"), q("22-38"), q("과제 22-42"), q("과제 22-54"),
         q("강의 슬라이드 14"), q("강의 슬라이드 33"),
         q("Problem 22-4 "), q("Problem 22-6 "), q("Problem 22-10 "), q("Problem 22-14 "),
         q("처음부터 끝까지")]
for e in probs:
    e["part"] = "핵심 문제"
probs[4]["extra"] = probs[4].get("extra", "") + '<p style="margin-top:6px"><b>→ 전체 메커니즘(니트릴부터): p.{PAGE:m-bup}</b></p>'
probs[5]["extra"] = probs[5].get("extra", "") + '<p style="margin-top:6px"><b>→ 전체 메커니즘(벤질 사이아나이드부터): p.{PAGE:m-phb}</b></p>'

# ── 마지막 1쪽: 시약 치트시트 + pKa + 직전 10줄
fin = g("f-reag")
ten = g("f-pairs")["html"]
ten_card = ten[ten.index('<div class="card tip"><div class="ct">🧠 시험 직전 10줄</div>'):ten.rindex('</div></div>')]
fin["html"] = fin["html"].replace("최종 정리 ①", "최종 정리").replace("시약 치트시트 — 시약을 보면 반응이 떠오르게", "시약 치트시트 · pKa · 시험 직전 10줄")
fin["html"] = fin["html"][:fin["html"].rindex('</div></div>')] + ten_card + '</div></div>'

E = [front] + concepts + probs + [fin]
