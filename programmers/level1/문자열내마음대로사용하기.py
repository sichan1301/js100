def solution(strings, n):
    list=[] 
    answer=[]
    for i in strings:
      list.append(i[n]+i)
    list.sort()
    for i in list:
      answer.append(i[1:])
    return answer
