L=[[[int(y)for y in x.split(',')]for x in l.strip().split('->')]for l in open(0)]
M=max(sum(sum(L,[]),[]))+1
D=[[0]*M for _ in range(M)]
R=lambda a,A:range(min(a,A),max(a,A)+1)
for l in L:
 s,e=l;x,y=s;X,Y=e
 if x==X:
  for j in R(y,Y):D[j][x]+=1
 elif y==Y:
  for i in R(x,X):D[y][i]+=1
 else:
  p=int(X>x)or-1;q=int(Y>y)or-1
  for x,y in zip(range(x,X+p,p),range(y,Y+q,q)):D[y][x]+=1
print(len([c for r in D for c in r if c>1]))
