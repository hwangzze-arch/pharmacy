# 제22장 핵심 킬러 TOP 10 — 단번에 이해하는 최종 실전 마스터북

`유기화학/CH22_핵심킬러TOP10_마스터북.pdf` (A4 가로 · 본문 2단)

- 내용: `content.py` (PART 0 대시보드 + TOP 1~10 각 장: 1초 직관 → 문제 → 원자 이동 타임라인 → 답안지)
- 디자인: `book.css`, 조립: `build_book.py`, 출력: `render_book.js` (표지는 쪽 번호 없이 따로 뽑아 합침)
- 그림 `img/*.png`: 54쪽 마스터요약(삼성노트 펜 표시가 얹힌 상태)에서 요소 단위로 잘라 온 것.
  다시 자르려면 마스터요약 폴더에서 `SHOTS=목록.json SHOTDIR=폴더 node render.js x.pdf`
  (목록 = [[이름, 쪽, CSS 선택자, n번째], ...]).

```bash
python3 build_book.py && node render_book.js ../../CH22_핵심킬러TOP10_마스터북.pdf
```
