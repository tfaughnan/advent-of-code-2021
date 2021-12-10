S=[]
for l in open(0):
 k=[]
 for c in l[:-1]:
  if 5922%(ord(c)+1):k=[c]+k
  elif abs(ord(c)-ord(k.pop(0)))>2:k=[];break
 if k:
  e=''.join(chr(ord(c)+(1 if c=='('else 2))for c in k);s=0
  for c in e:s*=5;s+={1:1,3:2,0:3,2:4}[ord(c)%5]
  S.append(s)
print(sorted(S)[len(S)//2])
