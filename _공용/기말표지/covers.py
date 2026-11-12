"""기말 마스터 노트 공용 표지를 만들어 각 과목 PDF 맨 앞에 넣는다.

    python3 covers.py            # 5개 전부 적용
    python3 covers.py orgo22     # 하나만 (id는 아래 COVERS 참고)
    python3 covers.py --preview  # 미리보기.html + 기말표지_모음.pdf(표지 5장) 만들기

과목 빌드로 PDF를 다시 만들면 표지가 예전 것으로 돌아가니, 빌드 뒤에 이 스크립트를 한 번 더 돌린다.
같은 PDF에 여러 번 돌려도 표지가 겹쳐 쌓이지 않는다 (PDF 정보의 /FinalCover 표시로 구분).

mode
- replace : 1쪽(옛 표지)을 새 표지로 바꾼다. (인체생리학 · 약품미생물학)
- toc     : 1쪽이 '색 패널 + 목차'라서 목차는 살린다. 새 표지를 맨 앞에 넣고,
            옛 1쪽의 색 패널 자리만 새 디자인 띠(strip)로 덮는다. (유기화학 · 약품생화학)
"""
import html, os, subprocess, sys, tempfile
from pypdf import PdfReader, PdfWriter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
MARK = "/FinalCover"
FONTS = ('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500'
         '&family=Inter+Tight:wght@500;600;700;800&family=Noto+Sans+KR:wght@400;500;700;800&display=swap">')
W169, H169, HA4 = 841.92, 527.04, 594.96

COVERS = [
  dict(id="orgo22", s="orgo", k="유기", file="유기화학/CH22_기말대비_마스터요약.pdf", mode="toc", strip=222, h=HA4,
       code="Organic Chemistry II", en="Organic Chemistry II", subject="유기화학", lab="Chapter", num="22",
       title="카르보닐 알파 치환 반응", flow=["케토–엔올", "α-할로젠화", "엔올레이트", "알킬화"],
       facts=[("15", "개념"), ("28", "문제"), ("58", "쪽")], lot="ORG2 · F22",
       toc=[("엔올과 산성 α-치환", "p.6 · 케토–엔올 · α-할로젠화 · HVZ"),
            ("α-H 산성도와 엔올레이트", "p.20 · pKa 비교 · NaH · LDA"),
            ("엔올레이트 알킬화", "p.29 · 말론산 · 아세토아세트산 에스터 합성")]),
  dict(id="orgo23", s="orgo", k="유기", file="유기화학/CH23_기말대비_마스터요약.pdf", mode="toc", strip=222, h=HA4,
       code="Organic Chemistry II", en="Organic Chemistry II", subject="유기화학", lab="Chapter", num="23",
       title="카르보닐 축합 반응", flow=["알돌", "E1cB 탈수", "클라이젠", "마이클"],
       facts=[("13", "개념"), ("32", "문제"), ("48", "쪽")], lot="ORG2 · F23",
       toc=[("알돌 반응", "p.3 · E1cB 탈수 · 혼합/분자 내 알돌"),
            ("클라이젠 · 디크만", "p.23 · β-케토 에스터 · 고리화"),
            ("마이클 · 스토크 · 로빈슨", "p.33 · 1,4-첨가 · 엔아민 · 로빈슨 고리화")]),
  dict(id="phys", s="phys", k="생리", file="인체생리학/인체생리학_기말_8-10장_마스터요약_개념문제.pdf", mode="replace", h=H169,
       code="PHAR272 · Human Physiology", en="Human Physiology", subject="인체생리학", lab="Chapters", num="8–10", long=1,
       title="근육 · 심장 · 혈관", flow=["근육 수축", "심장 펌프", "MAP = CO × TPR"],
       facts=[("44", "개념문제"), ("45", "T/F"), ("5", "녹취"), ("48", "쪽")], lot="PHYS · F08",
       toc=[("근육 생리학", "Ch 8 · p.2"), ("심장 생리학", "Ch 9 · p.27"),
            ("혈관과 혈압", "Ch 10 · p.39"), ("혈액", "Ch 11 · 강의 후 추가")]),
  dict(id="micro", s="micro", k="미생", file="약품 미생물학/약품미생물학_기말_바이러스_학습자료.pdf", mode="replace", h=H169,
       code="Medical Microbiology", en="Medical Microbiology", subject="약품미생물학", lab="Viruses · p.120–", num="Virus", word=1,
       title="바이러스 병원성", flow=["(−)ssRNA", "오르토믹소", "레트로", "HBV"],
       facts=[("13", "요약"), ("7", "실전 세트"), ("37", "문항"), ("31", "쪽")], lot="MICRO · FV",
       toc=[("파라믹소 · 랍도 · 번야", "p.4 · 홍역 · RSV · 광견병 · 한타"),
            ("오르토믹소", "p.8 · 인플루엔자 · 소/대변이"),
            ("레트로 · HIV · HBV", "p.12 · 역전사 · HAART · 데인 입자"),
            ("실전 세트 1–7", "p.16 · 37문항 + 해설")]),
  dict(id="bio", s="bio", k="생화", file="약품생화학/Chap19_20_시험대비 요약노트(TB추가).pdf", mode="toc", strip=262, h=HA4,
       code="Pharmaceutical Biochemistry", en="Pharmaceutical Biochemistry", subject="약품생화학", lab="Chapters", num="19–20", long=1,
       title="산화적 인산화 · 광인산화 · 탄소 고정", flow=["전자전달", "ATP 합성", "광인산화", "캘빈 회로"],
       facts=[("38", "개념"), ("117", "문제"), ("168", "쪽")], lot="BIO · F19",
       toc=[("전자전달 · ATP 합성", "19.1–19.2 · p.10"), ("조절 · 미토콘드리아의 다른 얼굴", "19.3–19.5 · p.75"),
            ("광합성 명반응 (광인산화)", "20 · p.102"), ("캘빈 회로 (탄소 고정)", "20.1 · p.136")]),
]

e = lambda s: html.escape(str(s))


def cover_html(d):
    cls = "cv-num" + (" long" if d.get("long") else "") + (" word" if d.get("word") else "")
    return f"""<div class="cover s-{d['s']}" style="width:100%;height:100%"><div class="cv">
 <div class="cv-meta"><span><b>{e(d['code'])}</b></span><span>2026 · 2학기 기말고사</span></div>
 <div class="cv-left">
  <div class="cv-kick">기말고사 마스터 노트</div>
  <div class="cv-head">
   <h1 class="cv-subject">{e(d['subject'])}</h1>
   <div class="cv-en">{e(d['en'])}</div>
   <p class="cv-title">{e(d['title'])}</p>
   <div class="cv-flow">{''.join(f'<span>{e(f)}</span>' for f in d['flow'])}</div>
  </div>
 </div>
 <div class="cv-right">
  <div><div class="cv-lab">{e(d['lab'])}</div><p class="{cls}">{e(d['num'])}</p></div>
  <span></span>
  <ol class="cv-toc">{''.join(f'<li><i>{i+1:02d}</i><b>{e(b)}</b><span>{e(s)}</span></li>' for i, (b, s) in enumerate(d['toc']))}</ol>
 </div>
 <div class="cv-foot">
  <dl class="cv-facts">{''.join(f'<div><dd>{e(v)}</dd><dt>{e(k)}</dt></div>' for v, k in d['facts'])}</dl>
  <span class="cv-code">{e(d['lot'])} · 2026.11</span>
 </div>
</div><div class="cv-tab" data-k="{e(d['k'])}"></div></div>"""


def strip_html(d):
    """목차 쪽 덮개: 왼쪽 띠 + 오른쪽 끝 탭. 나머지는 투명."""
    cls = "s-num" + (" long" if d.get("long") else "")
    return f"""<div class="cover s-{d['s']}" style="width:100%;height:100%;background:transparent">
 <div class="strip" style="width:{d['strip']}pt">
  <div class="cv-kick">목차 · 기말고사 마스터 노트</div>
  <div class="s-lab">{e(d['lab'])}</div><div class="{cls}">{e(d['num'])}</div>
  <div class="s-subj">{e(d['subject'])}</div><div class="s-en">{e(d['en'])}</div>
  <div class="s-title">{e(d['title'])}</div>
  <dl class="s-facts">{''.join(f'<div><dd>{e(v)}</dd><dt>{e(k)}</dt></div>' for v, k in d['facts'])}</dl>
  <div class="s-code">{e(d['lot'])} · 2026.11</div>
 </div>
 <div class="cv-tab" data-k="{e(d['k'])}"></div>
</div>"""


def page(body, w, h, bg="#FAFAF8"):
    css = open(os.path.join(HERE, "cover.css"), encoding="utf-8").read()
    return f"""<!doctype html><html lang="ko"><head><meta charset="utf-8">{FONTS}<style>{css}
@page{{size:{w}pt {h}pt;margin:0}} html,body{{margin:0;width:{w}pt;height:{h}pt;background:{bg};overflow:hidden}}</style></head>
<body>{body}</body></html>"""


def render(doc, w, h, tmp, name):
    hp, pp = os.path.join(tmp, name + ".html"), os.path.join(tmp, name + ".pdf")
    open(hp, "w", encoding="utf-8").write(doc)
    subprocess.run(["node", os.path.join(HERE, "render.js"), hp, pp, str(w), str(h)], check=True)
    return PdfReader(pp).pages[0]


def apply(d, tmp):
    src = os.path.join(ROOT, d["file"])
    r = PdfReader(src)
    pages = list(r.pages)
    meta = {k: v for k, v in (r.metadata or {}).items()}
    if meta.get(MARK):          # 이미 새 표지가 들어간 파일 → 앞의 표지를 빼고 다시
        pages = pages[1:]
    pw, ph = float(pages[0].mediabox.width), float(pages[0].mediabox.height)
    assert abs(ph - d["h"]) < 1, f"{d['id']}: 쪽 크기가 예상과 다름 {pw}×{ph}"
    cov = render(page(cover_html(d), W169, ph), W169, ph, tmp, d["id"] + "_cover")
    w = PdfWriter()
    w.add_page(cov)
    if d["mode"] == "toc":
        over = render(page(strip_html(d), W169, ph, bg="transparent"), W169, ph, tmp, d["id"] + "_strip")
        toc = pages[0]
        toc.merge_page(over)
        w.add_page(toc)
        rest = pages[1:]
    else:
        rest = pages[1:]
    for p in rest:
        w.add_page(p)
    meta[MARK] = "2026-2"
    w.add_metadata(meta)
    with open(src, "wb") as f:
        w.write(f)
    print(f"{d['id']}: {len(r.pages)}쪽 → {len(w.pages)}쪽  {d['file']}")


def preview():
    body = "".join(f'<figure>{cover_html(d)}<figcaption>{e(d["file"])}</figcaption></figure>' for d in COVERS)
    css = open(os.path.join(HERE, "cover.css"), encoding="utf-8").read()
    out = f"""<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>기말 마스터 노트 표지</title>{FONTS}<style>{css}
body{{margin:0;padding:40px 24px;background:#ECEDEF;font-family:var(--f-kr)}}
main{{max-width:1100px;margin:0 auto;display:grid;gap:36px}} figure{{margin:0}}
figure .cover{{aspect-ratio:16/10;width:100%!important;height:auto!important;box-shadow:0 18px 40px -18px rgba(0,0,0,.3)}}
figcaption{{margin-top:8px;font:12px var(--f-mono);color:#5E646C}}</style></head>
<body><main><h1 style="margin:0;font-weight:800;letter-spacing:-.03em">기말 마스터 노트 표지</h1>{body}</main></body></html>"""
    p = os.path.join(HERE, "미리보기.html")
    open(p, "w", encoding="utf-8").write(out)
    print("→", p)
    # 각 PDF의 새 표지(1쪽)만 모은 PDF
    w = PdfWriter()
    for d in COVERS:
        r = PdfReader(os.path.join(ROOT, d["file"]))
        if (r.metadata or {}).get(MARK):
            w.add_page(r.pages[0])
    p2 = os.path.join(HERE, "기말표지_모음.pdf")
    with open(p2, "wb") as f:
        w.write(f)
    print("→", p2, len(w.pages), "쪽")


if __name__ == "__main__":
    args = sys.argv[1:]
    if "--preview" in args:
        preview(); sys.exit()
    todo = [d for d in COVERS if not args or d["id"] in args]
    with tempfile.TemporaryDirectory() as tmp:
        for d in todo:
            apply(d, tmp)
