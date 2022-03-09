import sys

n,k = list(map(int,sys.stdin.readline().split()))
l=[]
for i in range(n):
    m = int(sys.stdin.readline())
    l.append(m)

result = 0
count = 0
for i in range(n,0,-1):
    if l[i-1]>k:
        continue
    result = k // l[i-1]
    count += result
    k = k % l[i-1]
    if k == 0:
        break

print(count)   
