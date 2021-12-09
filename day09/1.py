m=[[*map(int,l[:-1])]for l in open(0)]
print(sum((1+m[r][c]for r in range(len(m))for c in range(len(m[0]))if all(0>r+i or r+i>=len(m)or 0>c+j or c+j>=len(m[0])or m[r+i][c+j]>m[r][c]for i,j in((0,-1),(0,1),(-1,0),(1,0))))))
