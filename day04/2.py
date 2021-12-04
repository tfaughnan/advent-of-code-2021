I=[*map(str.strip,open(0))]
N=I.pop(0).split(',')
B=[[*map(str.split,I[i:i+5])]for i in range(1,len(I),6)]
R=*range(5),
m=lambda b,n:[[''if b[r][c]==n else b[r][c]for c in R]for r in R]
k=lambda b:any([not any(r)for r in b]+[not any([b[r][c]for r in R])for c in R])
for i in range(len(N)):
 B=filter(None,B);B=[m(b,N[i])for b in B];w=[k(b)for b in B]
 if any(w)and len(B)-1:
  for j in range(sum(w)):t=w.index(1);B[t]=w[t]=0
 elif w[0]:break
W=B[w.index(1)]
print(sum([sum([int(W[r][c])for c in R if W[r][c]])for r in R])*int(N[i]))
