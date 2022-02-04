n = list(input())
n.sort(reverse=True)
sum = 0
zero = 0
for i in n:
    sum += int(i)
    if i == '0':
        zero+=1
    
if sum % 3 != 0 or zero == 0:
    print(-1)
else:
    print("".join(n))