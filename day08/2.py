s=0
p=lambda h:[''.join(sorted(d))for d in h.split()]
b=lambda x:sum(2**'gfedcba'.index(y)for y in x)
e=lambda n:filter(lambda d:len(d)==n,l)
for line in open(0):l,r=map(p,line.split('|'));m={};o,f=[b([*e(w)][0])for w in (2,4)];[m.update({b(d):6 if o&b(d)-o else(0 if f&b(d)-f else 9)})for d in e(6)];[m.update({b(d):3 if o&b(d)==o else(2 if o|f|b(d)==127 else 5)})for d in e(5)];s+=sum([10**i*{2:1,3:7,4:4,7:8}.get(len(d),m.get(b(d)))for i,d in enumerate(r[::-1])])
print(s)
