import sys
input = sys.stdin.readline

T = int(input())    # 테스트 케이스 개수
dp = [[0 for _ in range(15)] for _ in range(15)]

# a층의 b호에 살려면 자신의 아래(a-1)층의 1호부터 b호까지 사람들의 수의 합만큼 사람들을 데려와 살아야 한다
for i in range(1, len(dp)):
    dp[0][i] = i    # 0층의 i호에는 i명 거주
    dp[i][1] = 1    # i층의 1호에는 1명 거주

# k층에 n호에는 몇 명이 살고 있는지 출력
for i in range(1, 15):
    for j in range(2, 15):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
for _ in range(T):
    n = int(input())
    k = int(input())
    print(dp[n][k])