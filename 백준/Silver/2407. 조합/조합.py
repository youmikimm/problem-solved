import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dp = [[0 for _ in range(101)] for _ in range(101)]
dp[0][0] = 1

for i in range(1, 101):
    dp[i][0] = 1
    dp[i][i] = 1
for i in range(2, 101):
    for j in range(1, i):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
            
print(dp[n][m])