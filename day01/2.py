import sys;i=0;o=[0]*3
for l in sys.stdin:
 n=o[1:]+[int(l)];i+=all(o)and sum(n)>sum(o);o=n
print(i)
