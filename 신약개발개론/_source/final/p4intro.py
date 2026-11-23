# ★ 실전문제 표지
from lib import page


def add():
    page('''<div class="body" style="display:flex;flex-direction:column;justify-content:center;padding:0 10mm">
  <div style="font-size:10pt;font-weight:900;letter-spacing:.2em;color:#5b3fd1">FINAL PRACTICE</div>
  <div style="font-size:28pt;font-weight:900;letter-spacing:-.03em;line-height:1.2;margin:2mm 0 5mm;color:#17142b">기말 대비 실전문제<br><span style="font-size:14pt;font-weight:500;color:#5d5a72">9·11·12·13주차 섞어서 · 객관식 12 · O/X 3 · 단답 9 · 서술 2</span></div>
  <div class="row" style="max-width:255mm">
    <div class="callout trap" style="flex:1"><div class="t">실전처럼</div><div class="small">정답 칸은 종이로 가리고 → 끝까지 푼 뒤 채점. 틀리면 해당 PART 요약으로.</div></div>
    <div class="callout tip" style="flex:1"><div class="t">비중 = 객관식 &gt; 단답 &gt; O/X</div><div class="small">중간고사가 객관식 26·단답 14·서술 0이었던 걸 반영. 서술은 “5개 쓰기”형만 대비.</div></div>
    <div class="callout memo" style="flex:1"><div class="t">보기 스타일</div><div class="small">중간고사처럼 <b>두 개념을 맞바꾸거나 한 단어를 뒤집은</b> 보기 중심.</div></div>
  </div>
</div>''', style='background:linear-gradient(135deg,#f7f5ff,#fff)')
