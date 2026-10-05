# 레닌저 장별 예제·문제 풀이노트 생성 소스

`CH=14 python3 render.py` → `final_ch14.pdf` (HTML → Chromium PDF). 장마다 `chNN.py` 하나를 추가하면 된다.

## 고정 규칙 (생화학 전 장 공통, 사용자 요청)
- **가로 16:10 (320×200 mm), 한 문제 = 한 페이지** — 삼성노트(갤럭시 탭)에서 보기 좋게
  - 왼쪽: 원문 → 번역 → 풀이 빈칸 / 오른쪽: 정답 → 해설
  - 넘치면 열(column)별로 글자·그림 크기를 자동 축소해 한 페이지에 맞춤 (render.py가 축소 비율 출력)
- **난이도 ★★★ 문제는 제외** (`build.py`에서 `level < 3`만 포함)
- 링크·북마크 넣지 않음 (삼성노트에서 동작 안 함) — 차례는 쪽수만 표시
- 강의 자료(ChapXX_note)와 관련된 예제·문제만 선별, DATA ANALYSIS PROBLEM 제외
- 해설은 고1도 이해할 수 있게: 핵심 한 줄 → 단계별 풀이 → 비유/함정 박스, 그림 적극 사용

## 파일
- `chNN.py`: 장별 설정(제목·범위·포함/제외 목록), 앞부분 요약 페이지(`front_pages()`), 문제 데이터 `ALL_ITEMS` (`level` = 난이도 1–3, 3은 자동 제외)
- `content_a.py`, `content_b.py`: 13장 문제 데이터 (`ch13.py`가 불러옴)
- `img/`: 원서에서 잘라 낸 문제 그림
- `helpers.py`: 수식·반응식·SVG 그림(환원전위 사다리, 로그축, 에너지 계단) 헬퍼
- `build.py`: 공통 표지·가이드·차례 + CSS + 자동 맞춤 JS
- 필요: `pip install playwright pymupdf`, Noto Sans KR / Noto Serif / JetBrains Mono 폰트

## 요약+문제 통합 에디션 (물리약학 최종요약 스타일)
`CH=13 python3 sbuild.py` → `summary_ch13.pdf`
- 구성: 표지 → 기초 → PART 표지 → 개념 요약 페이지 → 그 PART의 문제 → 한 장 정리 → 교과서 표
- 문제 페이지: 위(원문 | 쉬운 말 번역) → 가운데 풀이 빈칸(점 격자) → 아래(정답·풀이 | 그림·비유·함정)
- 장별 데이터 `sNN.py`: PARTS(개념 페이지 html + 문제 배치), BASICS, ENDING. 문제 내용은 `chNN.py`/`content_*.py` 재사용
