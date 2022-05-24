import math
def solution(progresses, speeds):
    answer = []
    index = 0
    list = []
    
    for i in range(len(progresses)):
        list.append(math.ceil((100-progresses[i])/speeds[i]))
        
    for i in range(len(list)):
        if list[index]<list[i]:
            answer.append(i-index)
            index = i
    answer.append(len(list)-index)
    return answer