import sys
from math import sqrt

m,k = map(int,sys.stdin.readline().split())

def primeNumber(n):
    if n<=1 :
        return False
    for i in range(2,int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True


for i in range(m,k+1):
    if primeNumber(i):
        print(i)
