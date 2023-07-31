import sys
input = sys.stdin.readline

n, k = map(int, input().split())
dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(1, n+1):
    dp[i][1] = i    # i개 중 1개를 뽑는 경우의 수 = i
    dp[i][0] = 1    # i개 중 0개를 뽑는 경우의 수 = 1
    dp[i][i] = 1    # i개 중 i개를 뽑는 경우의 수 = 1
    
for i in range(2, n+1):
    for j in range(2, i):
        dp[i][j] = dp[i-1][j] + dp[i-1][j-1]    # i개 중 j개 뽑기 = i-1개 중 j개 뽑기 + i-1개 중 j-1개 뽑기
        
print(dp[n][k])