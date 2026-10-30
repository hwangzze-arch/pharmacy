# 사용자 오버레이에서 '동그라미' 같은 표시만 골라내기 (글자 상자는 제외)
import pymupdf as fitz, numpy as np, sys
from collections import deque
F='/home/user/pharmacy/유기화학/중간고사_1721장_교수님포인트판_삼성노트 21장 설명 추가.pdf'

def comps(mask):
    h,w=mask.shape; seen=np.zeros_like(mask,bool); out=[]
    ys,xs=np.nonzero(mask)
    for y0,x0 in zip(ys,xs):
        if seen[y0,x0]: continue
        q=deque([(y0,x0)]); seen[y0,x0]=True; pts=[]
        while q:
            y,x=q.popleft(); pts.append((y,x))
            for dy in (-1,0,1):
                for dx in (-1,0,1):
                    yy,xx=y+dy,x+dx
                    if 0<=yy<h and 0<=xx<w and mask[yy,xx] and not seen[yy,xx]:
                        seen[yy,xx]=True; q.append((yy,xx))
        a=np.array(pts); out.append((a[:,1].min(),a[:,0].min(),a[:,1].max(),a[:,0].max(),len(pts)))
    return out

def overlays(d,i):
    p=d[i]; res=[]
    for info in p.get_image_info(xrefs=True):
        b=info['bbox']
        if info['xref'] and b[2]-b[0]>1100 and b[3]-b[1]>600 and info['width']>100:
            x=info['xref']; pix=fitz.Pixmap(d,x)
            sm=d.extract_image(x).get('smask',0)
            if sm: pix=fitz.Pixmap(pix,fitz.Pixmap(d,sm))
            a=np.frombuffer(pix.samples,dtype=np.uint8).reshape(pix.h,pix.w,pix.n).copy()
            res.append((x,b,a))
    return res

if __name__=='__main__':
    d=fitz.open(F)
    for pg in map(int,sys.argv[1:]):
        for x,b,a in overlays(d,pg-1):
            sc=(b[2]-b[0])/a.shape[1]
            m=a[::2,::2,3]>40
            for c in comps(m):
                x0,y0,x1,y1,n=c; W=(x1-x0+1)*2*sc; Hh=(y1-y0+1)*2*sc
                if W>7 and Hh>7:
                    fill=n/((x1-x0+1)*(y1-y0+1))
                    col=a[y0*2:(y1+1)*2,x0*2:(x1+1)*2,:3][a[y0*2:(y1+1)*2,x0*2:(x1+1)*2,3]>40].mean(0).astype(int)
                    print(pg,x,[round(v) for v in (x0*2*sc,y0*2*sc+b[1],x1*2*sc,y1*2*sc+b[1])],round(W),round(Hh),round(fill,2),col)
