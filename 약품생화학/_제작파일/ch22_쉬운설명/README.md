# Chap22_note 쉬운 설명 제작 파일

결과물: `약품생화학/Chap22_note_쉬운 설명.pdf` (슬라이드 94장 = 94쪽, A4 가로)
엔진은 `ch21_쉬운설명`과 같은 형식.

- `c1.py`–`c4.py`: 슬라이드별 내용 (핵심 키워드 · 한 줄 요약 · 한글 번역 · 상세 설명)
  - c1 22.1 질소 대사 · 22.2 앞부분(1–24), c2 Ser·Cys·Asp 가족·방향족·His·조절(25–48),
    c3 22.3 헴·빌리루빈·신경전달물질·크레아틴·GSH·NO·폴리아민 + 22.4 퓨린 합성(49–72),
    c4 AMP/GMP·피리미딘·RNR·dTMP·항암제·구제 경로·요산·통풍·세포벽(73–94)

```sh
cd "약품생화학/_제작파일/ch22_쉬운설명"
sh make_img.sh "../../Chap22_note.pdf"   # img/s-01.jpg … (저장소에는 안 올림)
python3 build.py
NODE_PATH=$(npm root -g) node render.js "$PWD/out.pdf"
```
