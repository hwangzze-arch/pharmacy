# 분석학실험 노트 제작 파일

`실험1_요약정리/`는 `실험1_뷰렛의 검정_요약정리.pdf`의 원본이야.
디자인은 `의약품 분석학/_제작파일/중간고사_마스터요약`과 같아 (A4 가로, 표지·헤더 배지·💡핵심·카드형 레이아웃, 글자 크기 자동 맞춤).

- `c_summary.py` 페이지 내용 (`pg()` 한 페이지 = 왼쪽 본문 + 오른쪽 카드)
- `build.py` 디자인(CSS)·페이지 틀, `render.js` 자동 맞춤 후 PDF 출력
- `svgs.py` 직접 그린 그림(검정곡선·시차오차·흐름도)과 우리 조 데이터

```sh
cd "분석학실험/_제작파일/실험1_요약정리"
python3 build.py
NODE_PATH=$(npm root -g) node render.js "$PWD/../../실험1_뷰렛의 검정_요약정리.pdf"
```
필요: Python 3, Node + playwright(Chromium), 한글 폰트 Noto Sans KR(또는 Pretendard).

## 실험1_실험노트/
`실험1_실험노트_부착용표그래프_초안.pdf`(오려 붙일 Table I·II·Figure 1 + 노트 초안)와 `실험1_뷰렛의 검정_결과.xlsx`의 원본.
- `make_pdf.py` → `note.html`, `render.js`로 PDF 출력 (그래프는 `../실험1_요약정리/svgs.py` 사용)
- `make_xlsx.py 출력.xlsx` → 측정값(파란 글자)과 수식, 검정곡선 차트
