import sys
input = sys.stdin.readline

N = int(input())
dp = [0] * (N+1)
dp[1] = 0

for i in range(2, N+1):
    dp[i] = dp[i-1] + 1    # -1 연산 1회 카운트
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)    # /2 연산 1회 카운트
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)    # /3 연산 1회 카운트
        
print(dp[N])