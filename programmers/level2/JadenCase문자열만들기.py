def solution(s):
    s = s.split(' ')
    capital = []
    for i in s:
      capital.append(i.capitalize())
    answer=' '.join(capital)
    return answer

print(solution("for the last week"))