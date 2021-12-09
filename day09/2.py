import math
m=[[*map(int,l[:-1])]for l in open(0)]
def f(r,c):
 if m[r][c]==9:return 0
 m[r][c]=9;return sum((f(r+i,c+j)for(i,j)in((0,-1),(0,1),(-1,0),(1,0))if 0<=r+i<len(m)and 0<=c+j<len(m[0])))+1
print(math.prod(sorted(f(r,c)for r in range(len(m))for c in range(len(m[0]))if m[r][c]-9)[-3:]))
