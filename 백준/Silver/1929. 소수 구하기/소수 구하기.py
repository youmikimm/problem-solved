import math
import sys
input = sys.stdin.readline

M, N = map(int, input().split())    # M 이상 N 이하인 소수 일렬로 출력하기

for num in range(M, N+1):
    isPrime = True
    for x in range(2, int(math.sqrt(num) + 1)):
        if num % x == 0:    # 소수가 아님
            isPrime = False
            break

    if isPrime and num != 1:
        print(num)