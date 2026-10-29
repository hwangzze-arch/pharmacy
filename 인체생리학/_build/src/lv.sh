B=$(cd "$(dirname "$0")" && pwd); cd $B
echo '{}' > levels.json
for it in 1 2 3 4; do python3 -I build.py >/dev/null && node pdf.js $B/out.html > ov.txt; python3 -I - <<'P'
import json,re
lv=json.load(open('levels.json'))
for line in open('ov.txt'):
    m=re.match(r'BODY (\d+)',line)
    if m: k=m.group(1); lv[k]=min(lv.get(k,-1)+1,2)
json.dump(lv,open('levels.json','w'))
P
done; cat ov.txt
