exec(f'p={input()}')
m=sorted(p)[len(p)//2]
print(sum(abs(x-m)for x in p))
