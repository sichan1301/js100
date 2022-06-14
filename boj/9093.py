import sys
n = int(input())

for i in range(n):
    m = list(sys.stdin.readline().split())
    for j in m:
        print(j[::-1])
