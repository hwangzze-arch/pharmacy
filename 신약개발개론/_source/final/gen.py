# 기말 통합 상세요약 + 문제 — 매주 새 주차를 이어 붙여 전체를 다시 생성
#   python3 gen.py && NODE_PATH=$(npm root -g) node build.js
#   → final.pdf 를 ../../신약개발개론_기말_통합 상세요약+문제.pdf 로 복사
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lib
import p0_front, p1_ch32, p2_ch4, p3_ch5, p4_exam, p5_cards

starts = {}
p0_front.add_cover()
starts['00'] = len(lib.pages) + 1; p0_front.add_strategy()
starts['01'] = len(lib.pages) + 1; p1_ch32.add()
starts['02'] = len(lib.pages) + 1; p2_ch4.add()
starts['03'] = len(lib.pages) + 1; p3_ch5.add()
starts['ex'] = len(lib.pages) + 1; p4_exam.add()
starts['ck'] = len(lib.pages) + 1; p5_cards.add()

# 표지 목차 쪽수 채우기
cls, style, inner = lib.pages[0]
for k, v in starts.items():
    inner = inner.replace('{' + k + '}', str(v))
lib.pages[0] = (cls, style, inner)

here = os.path.dirname(os.path.abspath(__file__))
n = lib.render(os.path.join(here, 'final.html'), '신약개발개론 기말 통합 상세요약+문제')
print(n, 'pages', starts)
