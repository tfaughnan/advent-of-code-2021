r=*map(str.strip,open(0)),
F=lambda f:int(''.join([f(x,key=x.count)for x in zip(*r)]),2)
print(F(max)*F(min))
