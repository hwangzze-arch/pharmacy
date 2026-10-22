# 의약품분석학 노트 제작 파일

Claude가 PDF 노트를 만들 때 쓴 원본이야. 새 채팅에서 "의약품 분석학/_제작파일 써서 ○○ 만들어줘"라고 하면 같은 디자인으로 바로 만들 수 있어.

## 폴더
| 폴더 | 만든 PDF | 구성 |
|---|---|---|
| `중간고사_마스터요약/` | 의약품분석학II_중간고사_마스터요약_개념문제Lecture2-4_필기반영.pdf | 표지·개념 페이지(💡📖📐✍️🧠)·문제 페이지(왼쪽 문제/풀이칸, 오른쪽 정답·해설) |
| `강의_번역상세설명/` | 의약품분석학II-Lecture5_질량분석법_번역_상세설명.pdf | 슬라이드 1장 = 1쪽, 한글 번역 + 상세 설명 |

## 중간고사_마스터요약 파일 역할
- `build.py` — 디자인(CSS)과 페이지 틀. 개념/문제 페이지 모양을 바꾸려면 여기.
- `c00_front.py` — 표지·시험 정보·족보 체크리스트·수학 페이지
- `c10…c61_*.py` — PART별 내용 (`t="c"` 개념, `t="q"` 문제)
- `c90_final.py` — 혼동 쌍 총정리·숫자 카드
- `annot.py` — 삼성노트 필기 반영(빨간 박스 `REPL`, ★중요 `FLAGS`, 내 필기 `NOTES`, 삭제 `EXCLUDE`)
- `render.js` — 글자가 넘치지 않게 자동 맞춤 후 PDF 출력

## 다시 만들기
```sh
cd "의약품 분석학/_제작파일/중간고사_마스터요약"
sh make_img.sh            # 슬라이드 그림 생성(용량이 커서 저장소에는 안 올림)
python3 build.py          # index.html 생성
NODE_PATH=$(npm root -g) node render.js "$PWD/out.pdf"
```
필요: Python 3, Node + playwright(Chromium), poppler-utils(pdftoppm), ImageMagick, 한글 폰트 Noto Sans KR.

## 모의고사/
- `mock.py` — 문제·정답·해설(객관식 `MC`, 주관식 `SA`)과 시험지 디자인. 정답 위치는 `TARGET`으로 고르게 분산.
- `ids.json` — 마스터 요약의 개념 번호·쪽수(해설의 📍 표시). 마스터 요약을 다시 만들면 `build.py`의 `ids`로 갱신.
- 실행: `python3 mock.py && NODE_PATH=$(npm root -g) node r.js` → `mock.pdf`
