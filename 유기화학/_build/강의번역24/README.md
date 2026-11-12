# 24장 강의 번역본 (빌드)

`CH24_약품유기화학2.pdf`(55쪽) → `CH24_약품유기화학2_번역본.pdf`. 23장 번역본 엔진을 복사.

```
sh make_img.sh "../../CH24_약품유기화학2.pdf"     # img/s-01.jpg …
python3 build.py                                   # index.html
node render.js "../../CH24_약품유기화학2_번역본.pdf"
```

- `ch24_1.py` 슬라이드 1–20 · `ch24_2.py` 21–40 · `ch24_3.py` 41–55 (번역·설명)
- `mslides24.py` 슬라이드 옆 메커니즘·반응식
