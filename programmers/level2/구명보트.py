def solution(people, limit):
    s=0
    e= len(people)-1
    answer = len(people)
    p = sorted(people,reverse=True)
    while s<e:
        if p[s]+p[e]<=limit:
            e-=1 
            answer-=1
        s+=1
    return answer