import sys

n = int(sys.stdin.readline())

def gcd(a,b):
    return gcd(b,a%b) if b else a


for i in range(n):
    l = list(map(int,sys.stdin.readline().split()))
    l = l[1:]
    ans = 0
    for j in range(len(l)-1):
        for k in range(j+1,len(l)):
            ans += gcd(l[j],l[k])
    print(ans)