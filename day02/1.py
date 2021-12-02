import sys;x=y=0
for l in sys.stdin:
 r,M=l.split();m=int(M)
 if r[0]=='f':
  x+=m
 elif r[0]=='d':
  y+=m
 else:
  y-=m
print(x*y)
