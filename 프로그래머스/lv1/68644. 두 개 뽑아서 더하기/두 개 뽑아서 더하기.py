from itertools import combinations
def solution(numbers):
    comb = list(combinations(numbers, 2))
    sumSet = set()
    
    for c in comb:
        total = sum(c)
        sumSet.add(total)
        
    answer = list(sumSet)

    return sorted(answer)