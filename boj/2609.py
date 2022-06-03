import sys

n,m = list(map(int,sys.stdin.readline().split()))

def gcd(n,m): 
    return gcd(m,n%m) if m else n

def lcm(n,m):
    g = gcd(n,m)
    return int(g*(n/g)*(m/g))

print(gcd(n,m))
print(lcm(n,m))
