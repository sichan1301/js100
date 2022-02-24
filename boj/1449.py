import sys

n,k = list(map(int,sys.stdin.readline().split()))

l = list(map(int,sys.stdin.readline().split()))
l.sort()   
count =1
start = l[0]+k-0.5
for i in l: 
    if start > i:
        continue
    else:
        start = i + k-0.5
        count+=1

print(count)