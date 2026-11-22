# Chap23_note 쉬운 설명 제작 파일

결과물: `약품생화학/Chap23_note_쉬운 설명.pdf` (슬라이드 107장 = 107쪽, A4 가로)
엔진은 `ch22_쉬운설명`과 같은 형식 (이미지 파일명만 3자리 `img/s-001.jpg`).

- `c1.py`–`c4.py`: 슬라이드별 내용 (핵심 키워드 · 한 줄 요약 · 한글 번역 · 상세 설명)
  - c1 23.1 호르몬 (1–30), c2 23.2 조직별 대사 · 23.3 인슐린 (31–54),
    c3 글루카곤 · 굶주림 · 에피네프린 · 코르티솔 · 23.4 렙틴 · PYY (55–78),
    c4 GLP-1 · 그렐린 · 아디포넥틴/AMPK · mTORC1 · PPAR · TZD · 23.5 당뇨 · 지질 부담 가설 · 치료 (79–107)

```sh
cd "약품생화학/_제작파일/ch23_쉬운설명"
sh make_img.sh "../../Chap23_note.pdf"   # img/s-001.jpg … (저장소에는 안 올림)
python3 build.py
NODE_PATH=$(npm root -g) node render.js "$PWD/out.pdf"
```
