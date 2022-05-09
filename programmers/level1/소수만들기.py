from itertools import combinations
import math
def isPrime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True
  
def solution(nums):
    list = []
    ans = 0
    for i in combinations(nums,3):
        list.append(sum(i))
    for i in list:
        if isPrime(i):
            ans+=1
    return ans
