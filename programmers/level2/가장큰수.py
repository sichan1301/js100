# from itertools import permutations

# def solutions(numbers):
#   permute = list(permutations(numbers,len(numbers)))
#   list_permute = [map(str,i) for i in permute]
#   return list_permute

# print(solutions([3, 30, 34, 5, 9]))
#  시간초과

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x : x*3, reverse = True)   
    return str(int(''.join(numbers)))