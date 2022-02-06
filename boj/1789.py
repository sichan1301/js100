import sys
n = int(sys.stdin.readline())

a=0
while a*(a+1)/2 <= n:
    a+=1

print(a-1)