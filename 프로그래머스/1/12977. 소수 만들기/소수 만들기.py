from itertools import combinations
def solution(nums):
    answer = 0
    allCases = list(combinations(nums, 3))
    for i in range(len(allCases)):
        total = sum(allCases[i])
        if(is_prime(total)):
            answer += 1
    
    return answer

def is_prime(num):
    rootNum = int(num ** 0.5)
    for i in range(2, rootNum + 1):
        if num % i == 0:
            return False
    return True