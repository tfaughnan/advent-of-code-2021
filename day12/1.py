p={}
g=('start','end')
for l in open(0):x,y=l[:-1].split('-');p[x]=p[x]+[y]if x in p else[y];p[y]=p[y]+[x]if y in p else[x]
def f(p,x,y,u,v):
 if x==y:return 1
 n=0
 for a in p[x]:
  V=v
  if a==a.lower() and a in u:
   if v or a in g:continue
   else:V=1
  n+=f(p,a,y,u|{x},1)
 return n
print(f(p,*g,set(),0))
