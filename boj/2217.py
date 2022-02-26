import sys

n = int(sys.stdin.readline())
l=[]

for i in range(n):
    a=int(sys.stdin.readline())
    l.append(a)

l.sort()
l.reverse()
max = 0
for i in range(n):
    if max < l[i]*(i+1):
        max = l[i]*(i+1)
print(max)