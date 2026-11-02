import pymupdf as fitz, sys, numpy as np
from PIL import Image
S=sys.argv[1]
files={17:'CH17_알코올과페놀_통합풀이.pdf',18:'CH18_에터와에폭사이드_통합풀이.pdf',19:'CH19_알데하이드와케톤_통합풀이.pdf',20:'CH20_카복실산과나이트릴_통합풀이.pdf',21:'CH21_카복실산유도체_통합풀이.pdf'}
for ch,fn in files.items():
  d=fitz.open(fn)
  for i,p in enumerate(d):
    found=[]
    for info in p.get_image_info(xrefs=True):
      b=info['bbox']
      if info['xref'] and b[2]-b[0]>1100 and b[3]-b[1]>700:
        x=info['xref']
        pix=fitz.Pixmap(d,x)
        sm=d.extract_image(x).get('smask',0)
        if sm:
          m=fitz.Pixmap(d,sm)
          pix=fitz.Pixmap(pix,m)
        arr=np.frombuffer(pix.samples,dtype=np.uint8).reshape(pix.h,pix.w,pix.n)
        a=arr[:,:,3] if pix.n==4 else None
        cov=(a>20).mean() if a is not None else 1
        found.append((x,cov))
        if a is not None and cov>0:
          Image.fromarray(arr.copy(),'RGBA').save(f'{S}/ov/{ch}-{i+1:02d}.png')
    print(ch,i+1,[(x,round(c,4)) for x,c in found])
