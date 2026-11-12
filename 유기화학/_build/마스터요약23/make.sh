#!/bin/sh
# 빌드 → 넘치는 문제 쪽은 오른쪽 뒤 블록을 '계속' 쪽으로 하나씩 넘기며 다시 빌드 (최대 4번) → PDF
OUT="${1:-../../CH23_기말대비_마스터요약.pdf}"
echo '{}' > _qsplit.json
for k in 1 2 3 4; do
  python3 build.py >/dev/null && node render.js "$OUT" >/dev/null
  python3 - <<'PY' || break
import json, sys
rep = json.load(open('_report.json')); sp = json.load(open('_qsplit.json'))
bad = {r['q2'] for r in rep if r.get('q2') and r['part'] == 'a' and r.get('overR')}
if not bad: sys.exit(1)
for q in bad: sp[q] = sp.get(q, 0) + 1
json.dump(sp, open('_qsplit.json', 'w')); print('split', sp)
PY
done
python3 build.py && node render.js "$OUT"
