I=*map(int,open(0).readline()[:-1].split(',')),
F=[I.count(i)for i in range(9)]
for d in range(256):F=F[1:7]+[F[0]+F[7],F[8],F[0]]
print(sum(F))
