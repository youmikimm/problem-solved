import sys
input = sys.stdin.readline

mCnt = int(input())  # 행렬 개수
matrices = [(0, 0)]
dp = [[0] * (mCnt+1) for _ in range(mCnt+1)]

for i in range(mCnt):
    a, b = map(int, input().split())
    matrices.append((a, b))


for gap in range(1, mCnt):
    for i in range(1, mCnt-gap+1):
        j = i + gap
        dp[i][j] = sys.maxsize
        for k in range(i, j):
            dp[i][j] = min(dp[i][j], (dp[i][k] + dp[k + 1][j] + (matrices[i][0] * matrices[k][1] * matrices[j][1])))
print(dp[1][mCnt])