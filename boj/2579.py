import sys

n = int(sys.stdin.readline())
l = []
for i in range(n):
    l.append(int(sys.stdin.readline()))

d=[0 for i in range(n) ]

if n>2:
    d[0] = l[0]
    d[1] = l[0] + l[1]
    d[2] = l[2] + max(l[0],l[1])

    for i in range(3,n):
        d[i] = max(d[i-2], d[i-3] + l[i-1]) +l[i]
    print(d[n-1])
    
elif n==2:
    print(max(l[0]+l[1], l[1]))
else: 
    print(l[0])