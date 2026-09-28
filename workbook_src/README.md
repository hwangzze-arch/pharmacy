# 레닌저 장별 예제·문제 풀이노트 생성 소스

`python3 render.py` → `final.pdf` (HTML → Chromium PDF, 2-pass로 차례 쪽번호 자동 기입)

- `content_a.py`, `content_b.py`: 문제별 원문/번역/정답/해설 데이터
- `helpers.py`: 수식·반응식·SVG 그림(사다리, 로그축, 에너지 계단) 헬퍼
- `build.py`: 표지·가이드·공식 키트·표·차례 + CSS
- 필요: `pip install playwright pymupdf`, Noto Sans KR / Noto Serif / JetBrains Mono 폰트
