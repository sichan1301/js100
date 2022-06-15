import sys

MOD = 10007
sys.setrecursionlimit(10 ** 7)

cache = [[0] * 1001 for _ in range(1001)]
N,K = map(int,sys.stdin.readline().split())

def bino(n,k):
  if cache[n][k]:
    return cache[n][k]
  if k == 0  or k == n:
    cache[n][k] = 1
  else:
    cache[n][k] = bino(n-1,k-1)+bino(n-1,k)
    cache[n][k] %= MOD
  return cache[n][k]

print(bino(N,K))