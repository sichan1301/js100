import sys

n = int(sys.stdin.readline())
t = 0

a = list(map(int,sys.stdin.readline().split()))
b = list(map(int,sys.stdin.readline().split()))


a.sort()
b.sort(reverse = True)
for i in range(n):
    t += a[i]*b[i]

print(t)    