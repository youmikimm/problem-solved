import math
from collections import deque
def solution(progresses, speeds):
    answer = [] # 배포할 작업 개수 배열
    days_count = [] # 작업완료까지 남은 날짜 배열
    q = deque()
    
    for p, s in zip(progresses, speeds):
        days_count.append(math.ceil((100-p) / s))
        
    for day in days_count:
        if len(q) == 0:
            q.append(day)
            answer.append(0)
        else:
            if q[0] < day:
                while q:
                    q.popleft()
                    answer[-1] += 1
                q.append(day)
                answer.append(0)
            else:
                q.append(day)
                    
    while q:
        q.popleft()
        answer[-1] += 1
    
    return answer