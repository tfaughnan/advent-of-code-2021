r=*map(str.strip,open(0)),
def F(f,R,i):c=[*zip(*R)][i];R=[x for x in R if x[i]==(f(r[0])if 2*c.count('0')==len(c)else f(c,key=c.count))];return F(f,R,i+1)if len(R)-1 else int(R[0],2)
print(F(max,r,0)*F(min,r,0))
