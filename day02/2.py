import sys;x=y=a=0
for l in sys.stdin:
 r,M=l.split();m=int(M)
 if r[0]<'f':a+=m
 elif r[0]<'u':x+=m;y+=a*m
 else:a-=m
print(x*y)
