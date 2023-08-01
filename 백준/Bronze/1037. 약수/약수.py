import sys
N = int(sys.stdin.readline())    # 진짜 약수의 개수(진짜 약수 = 약수 중 1, N을 뺀 약수)
lst = sorted(list(map(int, input().split())))
print(lst[0] * lst[-1])