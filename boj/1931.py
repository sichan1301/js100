import sys

n = int(sys.stdin.readline())
l=[]
for i in range(n):
    m,k = map(int,sys.stdin.readline().split())
    l.append([m,k])
l = sorted(l, key=lambda x: x[0])
l = sorted(l, key=lambda x: x[1])
behind = 0
count = 0

for i,j in l:
    if i>=behind:
        count += 1
        behind = j
print(count)
