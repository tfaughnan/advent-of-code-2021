exec(f'p={input()}')
n=sum(p)//len(p)
c=lambda d:d*(d+1)//2
print(sum(c(abs(x-n+n%2-1))for x in p))
