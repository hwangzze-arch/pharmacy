# 노트 빌드 소스
주차별 HTML/CSS → Chromium(Playwright)으로 PDF 변환. 폰트(Noto Sans KR, 나눔펜)는 용량 때문에 커밋하지 않음 — 빌드 시 Google Fonts에서 받아 `_fonts/`에 둘 것.

9주차(`week9/`, 7주차 휴강·8주차 중간고사)는 슬라이드 5~32가 6주차 31~58과 같아서 6주차 요약정리 PDF 페이지를 재사용함: `python3 build.py && node build.js && python3 merge.py` (6주차 요약정리 PDF 필요).
