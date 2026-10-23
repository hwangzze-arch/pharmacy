# 물리약학 자료 제작 도구

지금까지 만든 PDF(최종 요약, 통합 마스터 요약본, 한 장 정리 + 문제풀이, 모의고사)를 만든 프로그램이에요.
HTML을 만들고 Playwright(Chromium)로 PDF를 뽑아요.

## 폴더
| 폴더 | 내용 |
|---|---|
| `int/` | **2–7주차 통합 도구 (기본으로 쓸 곳)** |
| `diff/` | 4–6주차 확산 최종 요약 (SVG 그림 함수: 정상상태, 다층, 정적층, pH, 그래프) — `int/p3.py`가 불러 씀 |
| `final/` | 7주차 최종 요약 (방출 그림 SVG 함수) — `int/p4.py`가 불러 씀 |

폴더 구조(`int`, `diff`, `final`이 나란히)를 그대로 유지해야 해요.

## int/ 주요 파일
- `lib.py`: 공통 함수 — `prob(part, 제목, 출처, 문제, 보기, 정답, 사고의흐름, 한줄)`, `concept(...)`, `flow([('see'|'ask'|'link'|'calc'|'chk'|'done', 문장)])`, `J()`, `tbl()`, `fbox()`, `warn()`, `fixnote()`, `img()`
- `p1.py`–`p4.py`: 2주차 / 3주차 / 4–6주차 / 7주차 개념·문제 (소그룹 문제 포함), `p5.py`: 한 장 정리(`CS`) · 헷갈리는 짝, `p6.py`: 속도론 + 2024 리뷰 재구성
- `style4.css`: 기본 디자인 · `build3css.py`: 13px 압축판 CSS
- `build3.py`: 한 장 정리 + 문제풀이 → `out3.html`
- `mock.py` + `mockbuild.py` + `mock.css`: 모의고사(문제지 2단 → 정답표 → 해설) → `mock.html`
- `measure.js`: 블록 높이 측정 (페이지 꽉 채우기용) · `render.js`: PDF 출력 + 넘침 검사
- `img/`: 강의 그림

## 실행
```bash
cd int
python3 mockbuild.py                         # 또는 build3.py
node render.js "$PWD" mock.html "$PWD/mock.pdf"   # "overflow: []" 이면 정상
```
- `measure.js`, `render.js`는 `/opt/node-tools/node_modules/playwright`를 씀 (클라우드 세션 기본 경로)
- 글꼴: Pretendard를 `~/.fonts`에 설치 (`npm pack pretendard@1.3.9` → 압축 풀어서 otf 복사 → `fc-cache -f`), Noto CJK + Noto Color Emoji 필요

## 디자인 규칙 (사용자 선호)
- 본문 **13px** (키우지 말 것), A4 가로, 페이지 아래 여백 없이 꽉 채우기
- 문제: 왼쪽 = 문제 + 작은 풀이칸, 오른쪽 = 정답 + **🧭 사고의 흐름**(👀단서 🤔질문 💡연결 🧮계산 🔍함정체크 ✅결론) — 번호 단계 X
- 약어 풀이, 영어·한글 병기, [즉, ~] 설명, 비유
- 시험 형식은 `../시험 출제 형식 메모.md` 참고 (OX 90 × 1점 + 객관식 5 × 2점)
