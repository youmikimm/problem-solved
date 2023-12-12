# dp[x] = x를 만드는 1,2,3의 합의 개수
# dp[1] = 1, dp[2] = 2(1+1, 2), dp[3] = 4(1+1+1, 1+2, 2+1, 3)
# 4 = 1+3, 2+2, 3+1이므로 dp[4] = dp[3] + dp[2] + dp[1] = 7
# 5 = 1+4, 2+3, 3+2이므로 dp[5] = dp[4] + dp[3] + dp[2] = 13

import sys
input = sys.stdin.readline

T = int(input())
dp = [0] * 11
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 11):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for _ in range(T):
    N = int(input())
    print(dp[N])