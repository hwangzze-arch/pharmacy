# 레닌저 장별 예제·문제 풀이노트 생성 소스

`python3 render.py` → `final.pdf` (HTML → Chromium PDF)

## 고정 규칙 (생화학 전 장 공통, 사용자 요청)
- **가로 16:10 (320×200 mm), 한 문제 = 한 페이지** — 삼성노트(갤럭시 탭)에서 보기 좋게
  - 왼쪽: 원문 → 번역 → 풀이 빈칸 / 오른쪽: 정답 → 해설
  - 넘치면 열(column)별로 글자·그림 크기를 자동 축소해 한 페이지에 맞춤 (render.py가 축소 비율 출력)
- **난이도 ★★★ 문제는 제외** (`build.py`에서 `level < 3`만 포함)
- 강의 자료(ChapXX_note)와 관련된 예제·문제만 선별, DATA ANALYSIS PROBLEM 제외
- 해설은 고1도 이해할 수 있게: 핵심 한 줄 → 단계별 풀이 → 비유/함정 박스, 그림 적극 사용

## 파일
- `content_a.py`, `content_b.py`: 문제별 원문/번역/정답/해설 데이터 (`level` = 난이도 1–3)
- `helpers.py`: 수식·반응식·SVG 그림(환원전위 사다리, 로그축, 에너지 계단) 헬퍼
- `build.py`: 표지·가이드·공식 키트·표·차례 + CSS + 자동 맞춤 JS
- 필요: `pip install playwright pymupdf`, Noto Sans KR / Noto Serif / JetBrains Mono 폰트
