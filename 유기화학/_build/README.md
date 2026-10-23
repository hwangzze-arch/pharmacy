# 유기화학 PDF 빌드 도구

`유기화학/` 폴더의 중간고사 PDF들(교수님포인트판, 초압축 51문항, 예상문제 14제, 21장 필기 정리본)을 만든 스크립트와 내용 데이터.
새 채팅에서 **"유기화학/_build 써서 같은 형식으로 만들어줘"** 라고 하면 이어서 쓸 수 있다.

## 환경 준비 (새 클라우드 세션마다 1번)

```bash
pip install pymupdf rdkit
# 한글 폰트 (Pretendard)
cd ~ && npm pack pretendard@1.3.9 && tar xzf pretendard-1.3.9.tgz \
  && mkdir -p ~/.fonts && cp package/dist/public/static/*.otf ~/.fonts/ && fc-cache -f
```
Chromium/Playwright는 컨테이너에 이미 있음 (`render.js`가 `/opt/node22/lib/node_modules/playwright` 사용).

## 경로 주의
스크립트는 원래 세션 임시 폴더 기준으로 짜여 있다:
- `HERE` = 이 `_build` 폴더, `SCR = HERE/..` 에서 `grid.json`, `final_v3.pdf`, `final_v4.pdf` 등을 찾는다.
- 다시 돌리려면 작업 폴더를 하나 만들고 `build/` 아래에 이 폴더 내용을, 그 상위에 `data/grid.json`·`data/imginfo.json`과 `유기화학/중간고사_17-21장_교수님포인트판.pdf`(= final_v4.pdf) 사본을 두면 된다. `data/*.json`은 `build/`로도 복사.

## 파일 역할

| 파일 | 역할 |
|---|---|
| `chemdraw.py` | SMILES → 구조식 SVG (RDKit) |
| `render.js`, `render2.js` | HTML → PDF (Chromium). render2는 그림 자리 좌표도 JSON으로 출력 |
| `content_notes.py` | 문항별 **📝 내 필기** (삼성노트 텍스트상자 재조판). 끝에서 `notes21.py`(21장 추가 필기) 합침 |
| `notes21.py` | 21장 삼성노트 추가 필기 (빨간 글씨) |
| `content_cheat.py` | 문항별 **⚡ 치트키** (제미나이 정리본 + 추가 꿀팁), 산화·환원 일방통행 박스 |
| `selection.py` | 교수님포인트판에 남길 문항(KEEP) + 🎯 교수님 강조 문구(PROF) |
| `make_slots.py` | '내 풀이' 칸 자리에 들어갈 [필기 + 교수님 강조 + 치트키 + 메모] 블록 HTML |
| `compose.py` | 원본 통합풀이 PDF(벡터) + 새 블록 + 잘린 그림 교정 → 교수님포인트판 |
| `make_front.py`, `front_css.py` | 표지 · 시험 안내 · 장 표지 · 21장 수업 핵심 페이지 |
| `marks21.py`, `apply_marks.py` | 삼성노트 오버레이에서 동그라미만 골라 다시 얹기, 빨간 네모 문제 '제외' 도장 |
| `make_final29.py` | 막판 문항 목록·표지·해설 쪽 꼬리말 (공통 함수) |
| `exam2col.py` | **초압축 모의고사** — 한 쪽 2문제(왼·오), 줄 없는 풀이 칸, 칸 밑 그림 정답, 뒤에 해설 |
| `ansvis.py` | 풀이 칸 밑 **그림 정답** (구조식 + 시약 화살표 + 한 줄 설명). `V29`(51문항), `V14`(예상 14제) |
| `ans29.py` | 텍스트 정답 (예전 판) |
| `predict_content.py`, `predict14.py` | **예상문제 14제** 내용과 빌드 |
| `tools/` | 원본 분석용 (삼성노트 오버레이 추출 `ov.py`, 페이지 썸네일 `sheet.py` 등) |
| `data/` | 페이지 배치 정보 (`grid.json` = 원본 '내 풀이' 칸 위치, `plan*.json` = 최종 쪽 번호 등) |
| `img/` | 솔루션 매뉴얼에서 다시 오린 그림 |

## 스타일 약속
- 가로 1134×709pt (삼성노트 가로 보기), 폰트 Pretendard
- 색: 17장 #2a6f97 · 18장 #2a9d8f · 19장 #7b5cd6 · 20장 #e76f51 · 21장 #d1495b
- 문항 구성: 문제 → 📝 내 필기 → 🎯 교수님 강조(분홍) → ⚡ 치트키(보라=제미나이, 초록=추가 꿀팁) → ✍ 메모 → 정답과 해설
- 구조식은 모두 RDKit으로 그리고 `ansvis.check()`로 SMILES 검증
- 같은 페이지에 여러 HTML 조각을 합칠 때 CSS 클래스 이름 충돌 주의 (`.r`, `.hd`, `.g`, `.ck` 에서 실제로 깨졌던 적 있음)
