import sys;i=0;o=sys.maxsize
for l in sys.stdin:
 n=int(l);i+=n>o;o=n
print(i)
