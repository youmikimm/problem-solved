import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
lst = list(map(int,sys.stdin.readline().split()))
cnt = 0
i = 0
j = n - 1

lst.sort()

while i < j:
  if lst[i] + lst[j] < m:    # 합이 작다면 작은 쪽 인덱스 증가
    i += 1
  elif lst[i] + lst[j] > m:  # 합이 크다면 큰 쪽 인덱스 감소
    j -= 1
  else:                      # 합이 같은 경우 양쪽 인덱스 변경
    cnt += 1
    i += 1
    j -= 1

print(cnt)