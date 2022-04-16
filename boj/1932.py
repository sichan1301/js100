import sys

n = int(sys.stdin.readline())
l =[]
d = []
for i in range(n):
    m = list(map(int,sys.stdin.readline().split()))
    l.append(m)
    d.append([0 for j in range(len(m))])

d[0][0] = l[0][0]

for i in range(1,n):
    for j in range(len(l[i])):
        left = d[i-1][j-1] if j>0 else 0
        right = d[i-1][j] if j<len(l[i-1]) else 0
        d[i][j] = max(left,right) + l[i][j]
ans = max(d[n-1])
print(ans)