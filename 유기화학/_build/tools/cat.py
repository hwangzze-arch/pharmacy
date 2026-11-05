import pymupdf as fitz, json
files={17:'CH17_알코올과페놀_통합풀이.pdf',18:'CH18_에터와에폭사이드_통합풀이.pdf',19:'CH19_알데하이드와케톤_통합풀이.pdf',20:'CH20_카복실산과나이트릴_통합풀이.pdf',21:'CH21_카복실산유도체_통합풀이.pdf'}
out=[]
for ch,fn in files.items():
  d=fitz.open(fn)
  for i,p in enumerate(d):
    blocks=[]
    for b in p.get_text('dict')['blocks']:
      if b['type']!=0: continue
      t=''.join(s['text'] for l in b['lines'] for s in l['spans'])
      blocks.append((b['bbox'],t))
    top=[t for bb,t in blocks if bb[1]<70]
    badge=' | '.join(t for bb,t in blocks if bb[1]<70 and bb[0]<140)
    title=' | '.join(t for bb,t in blocks if bb[1]<70 and 140<=bb[0]<700)
    out.append(dict(ch=ch,pg=i+1,badge=badge,title=title))
    print(ch,i+1,'#',badge[:30],'#',title[:90])
json.dump(out,open('/tmp/claude-0/-home-user-pharmacy/43d5f9b8-203d-5621-b120-742ee7e1ee2a/scratchpad/cat.json','w'),ensure_ascii=False)
