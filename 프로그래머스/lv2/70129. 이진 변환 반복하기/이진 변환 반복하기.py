def solution(s):
    times = 0
    zeroCnt = 0
    
    while s != '1':
        zeroCnt += s.count('0')
        oneCnt = s.count('1')
        s = bin(oneCnt)[2:]
                
        times += 1
    
    return [times, zeroCnt]