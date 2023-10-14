import math

def solution(r1, r2):
    ans = 0
    
    for x in range(1, r2 + 1):
        maxY = math.floor(math.sqrt(r2 * r2 - x * x))
        minY = 0
        if x <= r1:
            minY = math.ceil(math.sqrt(r1 * r1 - x * x))
        ans += maxY - minY + 1
        
    return ans * 4