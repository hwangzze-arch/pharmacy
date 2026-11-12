#!/bin/sh
# 빌드 → (1) 2문제 쪽에서 칸이 넘치는 문제는 혼자 쪽(왼쪽 문제 / 오른쪽 정답)으로
#        (2) 혼자 쪽에서 넘치면 render.js가 글자·그림을 같이 줄여 한 쪽에 → PDF
OUT="${1:-../../CH23_기말대비_마스터요약.pdf}"
echo '{}' > _qsplit.json; echo '[]' > _qsolo.json; echo '[]' > _qflow.json
for k in 1 2 3 4 5 6 7 8; do
  python3 build.py >/dev/null && node render.js "$OUT" >/dev/null
  python3 - <<'PY' || break
import json, sys
rep = json.load(open('_report.json')); sp = json.load(open('_qsplit.json')); so = set(json.load(open('_qsolo.json'))); fl = set(json.load(open('_qflow.json')))
ch = False
for r in rep:
    if r.get('qp'):
        for q, o in zip(r['qp'], r['over']):
            if o and q not in so: so.add(q); ch = True
    if r.get('q1') and r.get('ik', 1) < 0.65 and r['q1'] not in fl:
        fl.add(r['q1']); ch = True
if not ch: sys.exit(1)
json.dump(sorted(fl), open('_qflow.json', 'w'))
json.dump(sp, open('_qsplit.json', 'w')); json.dump(sorted(so), open('_qsolo.json', 'w')); print('solo', sorted(so), 'split', sp)
PY
done
python3 build.py && node render.js "$OUT"
