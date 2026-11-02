import pymupdf as fitz, json, sys
from PIL import Image, ImageDraw
S=sys.argv[1]
files={17:'CH17_알코올과페놀_통합풀이.pdf',18:'CH18_에터와에폭사이드_통합풀이.pdf',19:'CH19_알데하이드와케톤_통합풀이.pdf',20:'CH20_카복실산과나이트릴_통합풀이.pdf',21:'CH21_카복실산유도체_통합풀이.pdf'}
keep={17:range(5,32),18:range(6,32),19:range(5,39),20:range(6,29),21:range(5,45)}
info={}
tiles=[]
for ch,fn in files.items():
  d=fitz.open(fn)
  for pn in keep[ch]:
    p=d[pn-1]
    ims=[]
    for ii in p.get_image_info(xrefs=True):
      b=ii['bbox']
      if b[2]-b[0]>1000 and b[3]-b[1]>600: continue
      ims.append([round(v,1) for v in b]+[ii['xref'],ii['width'],ii['height']])
    info[f'{ch}-{pn}']=ims
    top=[b for b in ims if b[1]<200 and b[2]-b[0]<1000]
    for b in top:
      pix=p.get_pixmap(dpi=110,clip=fitz.Rect(b[0]-4,b[1]-4,b[2]+4,b[3]+4))
      fn2=f'{S}/figs/{ch}-{pn:02d}_{int(b[0])}.png'; pix.save(fn2); tiles.append(fn2)
json.dump(info,open(f'{S}/imginfo.json','w'))
# sheets
W,H=1000,330
for k in range(0,len(tiles),12):
  sh=Image.new('RGB',(2*W,6*H),'white'); dr=ImageDraw.Draw(sh)
  for j,f in enumerate(tiles[k:k+12]):
    im=Image.open(f); im.thumbnail((W-10,H-25))
    x,y=(j%2)*W,(j//2)*H
    sh.paste(im,(x+5,y+20)); dr.text((x+5,y+3),f.split('/')[-1],fill='red'); dr.rectangle((x,y,x+W-1,y+H-1),outline='#ccc')
  sh.save(f'{S}/fsheet{k//12:02d}.png')
print(len(tiles))
