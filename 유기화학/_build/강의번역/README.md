# 강의자료 번역·설명 PDF 만들기

`CH21_약품유기화학2_번역본.pdf`와 같은 형식(A4 가로, 슬라이드 1장 = 1쪽)으로 교수님 강의 슬라이드를 번역·설명한다.
의약품분석학 `_제작파일/강의_번역상세설명`과 같은 템플릿이다.

## 쪽 구성
머리(번호 · 한글 제목 · 영문 부제 · 원본 슬라이드 번호) → 핵심 키워드 · 슬라이드 그림 · 한 줄 요약 → 한글 번역 | 상세 설명·풀이.
형광펜: 노랑 = 핵심 개념, 초록 = 공식·정의·결론, 분홍 = 시험 포인트.
연습문제 슬라이드는 문제마다 "문제 쪽(접근 방법)" + "풀이 쪽(RDKit 정답 그림)" 2쪽으로 나눈다.

## 실행
```bash
pip install rdkit pymupdf
sh make_img.sh "../../CH22_약품유기화학2.pdf"    # img/s-01.jpg …
python3 build.py                                 # index.html
node render.js "../../CH22_약품유기화학2_번역본.pdf"   # 넘치는 쪽은 글자 크기 자동 축소
```
- `ch22_1.py`–`ch22_3.py`: 쪽 내용 (dict: img/fig, title, sub, kw, sum, tr, ex …)
- `fig.py`: SMILES → 구조식 SVG, 반응식 줄(`row`). `[H:1]`로 쓴 원자는 분홍 강조.
- `fonts/`: Noto Sans KR (woff2, OFL)
- 다음 장은 `ch23_*.py`를 만들고 `build.py`의 import와 `FOOT`만 바꾸면 된다.
