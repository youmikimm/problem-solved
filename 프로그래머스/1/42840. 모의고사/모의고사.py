def solution(answers):
    answer = []
    p1_answer = [1,2,3,4,5] * 2000
    p2_answer = [2,1,2,3,2,4,2,5] * 1250
    p3_answer = [3,3,1,1,2,2,4,4,5,5] * 1000
    count = {'1':0, '2':0, '3':0}
    
    for i in range(len(answers)):
        if answers[i] == p1_answer[i]:
            count['1'] += 1
        if answers[i] == p2_answer[i]:
            count['2'] += 1
        if answers[i] == p3_answer[i]:
            count['3'] += 1
    
    highest_score = max(count.values())
    
    for k,v in count.items():
        if v == highest_score:
            answer.append(int(k))
    
    return sorted(answer)