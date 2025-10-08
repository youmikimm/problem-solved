from collections import Counter
def solution(clothes):
    answer = 1
    closet = Counter([c for _, c in clothes]) # {의상종류: 가짓수}
    
    for i in closet.values():
        answer *= (i + 1)

    return answer - 1 # 아무것도 선택하지 않는 경우의 수 빼기