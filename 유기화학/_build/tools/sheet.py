import sys,glob
from PIL import Image,ImageDraw
d,out,cols=sys.argv[1],sys.argv[2],int(sys.argv[3])
fs=sorted(glob.glob(d+'/p-*.png'))
per=cols*3
for k in range(0,len(fs),per):
    ims=[Image.open(f) for f in fs[k:k+per]]
    w,h=ims[0].size
    sh=Image.new('RGB',(cols*w,((len(ims)+cols-1)//cols)*h),'white')
    for i,im in enumerate(ims):
        sh.paste(im,((i%cols)*w,(i//cols)*h))
        ImageDraw.Draw(sh).text(((i%cols)*w+5,(i//cols)*h+5),str(k+i+1),fill='red')
    sh.save(f'{out}-{k//per:02d}.png')
