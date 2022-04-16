import sys

n = int(sys.stdin.readline())

colors=[]
inf = 99999999
d=[]

for i in range(n):
    r,g,b= list(map(int,sys.stdin.readline().split()))
    colors.append([r,g,b])
    d.append([inf,inf,inf])

d[0][0] = colors[0][0]
d[0][1] = colors[0][1]
d[0][2] = colors[0][2]

for i in range(1, n):
    d[i][0] = min( d[i-1][1], d[i-1][2] )  + colors[i][0]
    d[i][1] = min( d[i-1][0], d[i-1][2] )  + colors[i][1]
    d[i][2] = min( d[i-1][0], d[i-1][1] )  + colors[i][2]

ans = min( d[n-1][0], d[n-1][1], d[n-1][2] )
print(ans)
