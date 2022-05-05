def solution(d, budget):
    d.sort()
    count=0
    for i in d:
        budget = budget-i
        if budget >=0:
            count+=1
    return count