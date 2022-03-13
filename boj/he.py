def solution(S, interval):
    list = ['a','b','c','d','e']
    tmp = 0
    for i in range (0,len(interval)):
        if interval[i][1] - interval[i][0] > 2:
            tmp = list[interval[i][0]-1]
            list[interval[i][0]-1] = list[interval[i][1]-1]
            list[interval[i][1]-1] = tmp
            tmp = list[interval[i][0]] 
            list[interval[i][0]] = list[interval[i][1]-2]
            list[interval[i][1]-2] = tmp
        else:
            tmp = list[interval[i][0]-1]
            list[interval[i][0]-1] = list[interval[i][1]-1]
            list[interval[i][1]-1] = tmp
    result = ""
    for s in list:
        result += s + " "

solution('abcde',[[1,3],[1,4],[4,5]])