from itertools import combinations
def solution(numbers):
    combi = []
    for i in combinations(numbers,2):
        combi.append(sum(i))
    return sorted(list(set(combi)))


print(solution([2,1,3,4,1]))