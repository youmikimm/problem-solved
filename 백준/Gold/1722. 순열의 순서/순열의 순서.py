import math
import sys
input = sys.stdin.readline

N = int(input())
inputData = list(map(int, input().split()))
query = inputData.pop(0)
def printPermutation(n, order):
    order -= 1
    numList = [x for x in range(1, n+1)]
    index = order   # 인덱스 계산용
    tmpOrder = 0
    result = ''

    while tmpOrder != order:
        fac = math.factorial(n-1)
        quotient = index // fac
        index %= fac
        result += str(numList.pop(quotient)) + ' '
        tmpOrder += quotient * fac
        n -= 1

    if len(numList) > 0:
        for x in numList:
            result += str(x) + ' '

    print(result)


def printOrder(n, lst):
    result = 0
    numList = [x for x in range(1, n+1)]
    k = n - 1

    for i in range(n):
        fac = math.factorial(k)
        idx = numList.index(lst[i])
        numList.pop(idx)
        result += idx * fac
        k -= 1

    print(result + 1)

if query == 1:
    printPermutation(N, inputData[0])   # 1~N으로 이루어진 순열 중 inputData[0]번째 순열을 출력
elif query == 2:
    printOrder(N, inputData)