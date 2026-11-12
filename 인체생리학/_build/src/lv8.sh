B=$(cd "$(dirname "$0")" && pwd); cd $B
echo '{}' > levels8.json
for it in 1 2 3 4 5; do python3 -I build8.py >/dev/null && node pdf.js $B/out8.html > ov8.txt; python3 -I - <<'P'
import json,re
lv=json.load(open('levels8.json'))
for line in open('ov8.txt'):
    m=re.match(r'BODY (\d+)',line)
    if m: k=m.group(1); lv[k]=min(lv.get(k,-1)+1,3)
json.dump(lv,open('levels8.json','w'))
P
done; cat ov8.txt
