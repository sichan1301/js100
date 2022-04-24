import sys

n = int(sys.stdin.readline())

inf = 99999999

d = [ inf for i in range(3*n+1) ]
d[n] = 0

for i in range(n-1,0,-1):
    d[i] = min( d[i*2], d[i*3], d[i+1] ) +1
print(d[1])