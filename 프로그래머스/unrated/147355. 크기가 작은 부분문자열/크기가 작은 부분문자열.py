def solution(t, p):
    cnt = 0
    size = len(p)
    
    for i in range(len(t)-size+1):
        if int(t[i:i+size]) <= int(p):
            cnt += 1
    
    return cnt