import sys

n = int(sys.stdin.readline().strip())
start, end, sum, cnt = 1, 1, 1, 1          # n 자신 하나는 cnt에 세고 시작

while end != n:
  
  if sum == n:
    cnt += 1
    end += 1
    sum += end

  elif sum > n:      # sum이 큰 경우
    sum -= start
    start += 1

  else:              # sum이 작은 경우
    end += 1
    sum += end

print(cnt)