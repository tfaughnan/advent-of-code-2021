import sys
from collections import defaultdict as d
S=1
r=*range(10),
I=[[*map(int,[*l.strip()])]for l in open(0)]
C=d(lambda:-sys.maxsize,{(x,y):I[y][x]for x in r for y in r})
def g(c):
 f=[];[c.update({(x,y):c[(x,y)]+1})or(f.append((x,y))if c[(x,y)]==10 else 0)for y in r for x in r];s=0
 while len(f)>0:
  s+=len(f);F=[]
  for x,y in f:
   for i,j in((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)):
    c.update({(x+i,y+j):c[(x+i,y+j)]+1})or(F.append((x+i,y+j))if c[(x+i,y+j)]==10 else 0)
  f=F
 [c.update({(x,y):0})for y in r for x in r if c[(x,y)]>9];return s
while g(C)-100:S+=1
print(S)
