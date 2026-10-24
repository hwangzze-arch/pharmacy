# Chap19_20 시험대비 요약노트(TB추가) 제작 파일

결과물: `약품생화학/Chap19_20_시험대비 요약노트(TB추가).pdf` (A4 가로, 185쪽)
디자인 엔진은 `의약품 분석학/_제작파일/중간고사_마스터요약`을 가져와 고친 것.

## 구성
- 표지(분석학 마스터 노트 스타일) → 시험 형식·사용법 → 한 장 큰 그림
- PART 1–6마다: 개념 페이지(💡📖📐✍️🧠) → 개념확인·원서 문제 → 교수님 테스트뱅크
- FINAL: 혼동 쌍 · 숫자/공식 카드 · 약어 총정리 2쪽

## 파일
| 파일 | 내용 |
|---|---|
| `build.py` | CSS·페이지 틀, 테스트뱅크를 각 PART 끝에 끼워 넣음 → `index.html` |
| `parts.py` | PART 이름, 보기·O/X 헬퍼, 테스트뱅크 헬퍼 `tbm`(객관식)·`tbs`(주관식) |
| `c00_front.py` / `c90_final.py` | 표지·안내·큰 그림 / 혼동 쌍·숫자 카드·약어 |
| `c10_etc.py` … `c60_calvin.py` | PART별 개념(`t="c"`)과 개념확인·원서 문제(`t="q"`) |
| `tb19a.py`, `tb19b.py`, `tb20.py` | 교수님 테스트뱅크 (ch19 76문제, ch20 21문제) |
| `render.js` | 넘치는 쪽 글자 자동 축소 후 PDF 출력 |

## 규칙
- 테스트뱅크: 강의 범위 밖(광호흡·C4/CAM·녹말/수크로스 합성·셀룰로스·펩티도글리칸·작용 스펙트럼·광합성 진화·Q3)과 중복(Q42)은 제외
- 정답이 의심스러운 문항은 `warn=`으로 ⚠️ 상자 (19-29, 19-30, 19-62, 19-64)
- 원서 문제 출처는 5판 번호(솔루션 `solutionsch19/20.pdf`로 답 확인)

## 다시 만들기
```sh
cd "약품생화학/_제작파일/ch19_20_요약노트"
sh make_img.sh          # 슬라이드 그림(img/S-001.jpg …), 저장소에는 안 올림
python3 build.py        # index.html
NODE_PATH=$(npm root -g) node render.js "$PWD/out.pdf"
```
필요: Python 3, Node + playwright(Chromium), poppler-utils, ImageMagick, 폰트 Noto Sans KR · Noto Serif.
