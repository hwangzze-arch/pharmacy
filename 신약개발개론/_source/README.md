# 노트 빌드 소스
주차별 HTML/CSS → Chromium(Playwright)으로 PDF 변환. 폰트(Noto Sans KR, 나눔펜)는 용량 때문에 커밋하지 않음 — 빌드 시 Google Fonts에서 받아 `_fonts/`에 둘 것.

9주차(`week9/`, 7주차 휴강·8주차 중간고사)는 슬라이드 5~32가 6주차 31~58과 같아서 6주차 요약정리 PDF 페이지를 재사용함: `python3 build.py && node build.js && python3 merge.py` (6주차 요약정리 PDF 필요).

11주차(`week11/`, 10주차 휴강)는 슬라이드 7·9~24가 6주차와 같아서 같은 방식으로 재사용(번호는 띄엄띄엄 — `content.py`의 reuse 표 참고)하고, 새 내용(Q&A·Chapter 4 약물대사)은 `content.py`에 작성: `python3 build.py && node build.js && python3 merge.py`.

12주차(`week12/`)는 슬라이드 14~35가 11주차 44~65와 같아서 11주차 요약정리 PDF를 재사용하고, 새 내용(Q&A·PD 심화·Chapter 5 전임상·GLP)은 `content_a/b/c.py`에 작성: `python3 build.py && node build.js && python3 merge.py` (11주차 요약정리 PDF 필요).

`final/` = 기말 통합 상세요약+문제. 주차가 추가되면 `pN_*.py`를 더해 `gen.py`에서 이어 붙임: `python3 gen.py && node build.js` → `final.pdf`를 `신약개발개론_기말_통합 상세요약+문제.pdf`로 복사. 표지는 밝은 보라 톤(삼성노트는 기말 완성 후 한 번에 이전).
