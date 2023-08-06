import sys
input = sys.stdin.readline

N = int(input())
dp = [[0 for _ in range(2)] for _ in range(N+1)]

dp[1][0] = 0    # 1의 길이에서 0으로 끝나는 이친수 개수
dp[1][1] = 1    # 1의 길이에서 1으로 끝나는 이친수 개수

for i in range(2, N+1):
    dp[i][0] = dp[i-1][0] + dp[i-1][1]
    dp[i][1] = dp[i-1][0]

print(dp[N][0] + dp[N][1])