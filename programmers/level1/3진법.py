def solution(n):
    list = []
    sum = 0
    while n>=1:
        list.append(int(n%3))
        if n==1:
          break;
        n = n/3
    for i in range(len(list)):
        sum += (3**i) * list[len(list)-i-1] 
    return sum

print(solution(125))