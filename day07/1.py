exec(f'p={input()}')
print(sum(abs(x-sorted(p)[len(p)//2])for x in p))
