def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        cnt = divisorCount(i)
        if isEven(cnt):
            answer += i
        else:
            answer -= i
    return answer


def divisorCount(num):  # 약수의 개수
    if num == 1:
        return 1
    cnt = 2
    for x in range(2, num):
        if num % x == 0:
            cnt += 1
            
    return cnt


def isEven(cnt):    # 짝수 or 홀수
    if cnt % 2 == 0:
        return True
    else:
        return False