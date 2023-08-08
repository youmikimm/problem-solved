import sys
input = sys.stdin.readline

N, L, R = map(int, input().split())
dp = [[[0 for _ in range(101)] for _ in range(101)] for _ in range(101)]
dp[1][1][1] = 1    # 건물이 총 1개이면 왼쪽, 오른쪽에서 각각 1개씩 보임

for i in range(2, N+1):
    for j in range(1, L+1):
        for k in range(1, R+1):
            dp[i][j][k] = (dp[i-1][j][k-1] + dp[i-1][j-1][k] + dp[i-1][j][k] * (i-2)) % 1000000007

            # 가정: 가장 낮은 빌딩을 마지막에 세운다
# 왼쪽에 세우면 L+1, 오른쪽에 세우면 R+1, 가운데 세우는 경우의 수는 N-2가지
print(dp[N][L][R])