import sys

n = int(sys.stdin.readline())
m = list(map(int,sys.stdin.readline().split()))
m.sort()

sum = 0
for i in range (0, len(m)):
    for j in range(i+1):
        sum += m[j] 

print(sum)
