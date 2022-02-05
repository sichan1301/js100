import sys

n = int(sys.stdin.readline())
list = []
for i in range(2*n):
    if 2*n % (i+1) == 0:
        list.append(i+1)
for j in range(len(list)):
    if list[j]-list[j-1]==1:
        print(list[j])

