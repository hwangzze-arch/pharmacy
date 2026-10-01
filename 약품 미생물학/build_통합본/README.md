# 통합본 빌드 소스

`약품미생물학_그람양성균·바이러스_통합본.pdf`를 만드는 소스입니다.

- `c00_intro.py` 표지·사용법·기초 / `c10_gp.py` 그람양성균 / `c20~c50` 바이러스
- `core.py` 페이지 레이아웃(문제 페이지 `Q`, 요약 페이지 `S`), `svgs.py` 직접 그린 그림, `img/` 강의자료에서 잘라 낸 그림
- 빌드: `python3 build.py && node render.js ../약품미생물학_그람양성균·바이러스_통합본.pdf`
  (Pretendard 폰트와 Playwright Chromium이 있어야 합니다)
