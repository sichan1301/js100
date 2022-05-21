from collections import defaultdict
 
def solution(id_list, report, k):
    answer = []

    report_to_from = defaultdict(set) 
    report_from_to = defaultdict(set) 
    for r in report:
        report_from, report_to = r.split(' ') 
        report_to_from[report_to].add(report_from) 
        report_from_to[report_from].add(report_to) 
    
    for _id in id_list:
        cnt = 0
        for r_to in report_from_to[_id]: 
            if len(report_to_from[r_to]) >= k: 
                cnt += 1
        answer.append(cnt)
    return answer