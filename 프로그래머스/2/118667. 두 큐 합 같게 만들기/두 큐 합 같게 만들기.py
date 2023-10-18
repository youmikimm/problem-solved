from collections import deque
def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    tot1 = sum(q1)
    tot2 = sum(q2)
    length = len(q1) + len(q2)
    
    if (tot1 + tot2) % 2 != 0:
        return -1
    
    times = 0
    while tot1 != tot2:
        if times == length * 2:
            return -1
        
        if tot1 > tot2:
            elem = q1.popleft()
            q2.append(elem)
            tot1 -= elem
            tot2 += elem
        
        elif tot1 < tot2:
            elem = q2.popleft()
            q1.append(elem)
            tot2 -= elem
            tot1 += elem
        
        times += 1
    
    return times