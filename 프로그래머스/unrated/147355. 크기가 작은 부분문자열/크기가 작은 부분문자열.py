def solution(t, p):
    cnt = 0
    arr = list(t)

    size = len(p)
    idx = 0
    while idx + size <= len(t):
        tmp = int(''.join(arr[idx:idx+size]))
        if tmp <= int(p):
            cnt += 1
        idx += 1
    
    return cnt