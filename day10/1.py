s=0
for l in open(0):
 k=[]
 for c in l[:-1]:
  if 5922%(ord(c)+1):k+=[c]
  elif abs(ord(c)-ord(k.pop()))>2:s+={1:3,3:57,0:1197,2:25137}[ord(c)%5]
print(s)
