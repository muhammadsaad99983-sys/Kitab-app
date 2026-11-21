import os,json,hashlib,math
from PIL import Image,ImageDraw
d='www/books';os.makedirs(d,exist_ok=True);os.makedirs('assets',exist_ok=True)
cols=['#0f766e','#166534','#115e59','#14532d','#0e7490','#155e75','#365314','#064e3b','#134e4a','#1e3a8a','#4d7c0f']
out=[]
for f in sorted(x for x in os.listdir(d) if x.lower().endswith('.pdf')):
    n=f[:-4];t,a=(n.split(' - ',1)+[''])[:2]
    c=cols[int(hashlib.md5(n.encode()).hexdigest(),16)%len(cols)]
    out.append({'id':f,'title':t.strip(),'author':a.strip(),'file':'books/'+f,'color':c})
json.dump(out,open('www/books.json','w'),ensure_ascii=False)
S=1024
bg=Image.new('RGB',(S,S));px=bg.load()
for y in range(S):
    for x in range(S):
        t=min(((x-512)**2+(y-420)**2)**.5/760,1)
        px[x,y]=(int(22-14*t),int(125-78*t),int(105-66*t))
ImageDraw.Draw(bg).ellipse((70,70,954,954),outline=(212,175,90),width=8)
fg=Image.new('RGBA',(S,S),(0,0,0,0));d=ImageDraw.Draw(fg)
G=(214,175,85,255);C=(250,244,228,255);dy=40
P=lambda p:[(x,y+dy) for x,y in p]
M=lambda p:[(1024-x,y) for x,y in p]
L=[(512,375),(512,690),(235,640),(235,330)]
l=[(500,398),(500,668),(256,622),(256,352)]
for p,c in((L,G),(l,C)):
    d.polygon(P(p),fill=c);d.polygon(P(M(p)),fill=c)
for k in range(5):
    o=60+k*48;a=[(290,358+o),(470,393+o)]
    d.line(P(a),fill=G,width=8);d.line(P(M(a)),fill=G,width=8)
d.line(P([(512,375),(512,690)]),fill=G,width=10)
d.ellipse((432,140,592,300),fill=G);d.ellipse((470,125,630,285),fill=(0,0,0,0))
star=[(572+30*math.cos(math.pi/5*i-math.pi/2)*(1 if i%2==0 else .45),205+30*math.sin(math.pi/5*i-math.pi/2)*(1 if i%2==0 else .45)) for i in range(10)]
d.polygon(star,fill=G)
f2=fg.resize((860,860));fg2=Image.new('RGBA',(S,S),(0,0,0,0));fg2.paste(f2,(82,82))
bg.save('assets/icon-background.png');fg2.save('assets/icon-foreground.png')
ic=bg.convert('RGBA');ic.alpha_composite(fg2);ic.save('assets/icon-only.png')
