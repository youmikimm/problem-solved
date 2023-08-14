import sys
input = sys.stdin.readline

orderList = list(map(int, input().split()))
dp = [[[sys.maxsize for _ in range(5)] for _ in range(5)] for _ in range(100001)]
dp[0][0][0] = 0    # dp[N][L][R] = N개의 번호를 밟은 후 왼발이 L, 오른발이 R에 있을 때 최소 누적 힘

force = [[0, 2, 2, 2, 2],
        [2, 1, 3, 4, 3],
        [2, 3, 1, 3, 4],
        [2, 4, 3, 1, 3],
        [2, 3, 4, 3, 1]]    # i -> j로 옮길 때 드는 힘

idx = 0
n = 1
while orderList[idx] != 0:
    order = orderList[idx]    # 밟아야 하는 위치
    for i in range(5):
        if order != i:    
            for j in range(5):    # 오른발을 order 위치로 옮기기
                dp[n][i][order] = min(dp[n-1][i][j] + force[j][order], dp[n][i][order])
            
    for i in range(5):
        if order != i:
            for j in range(5):    # 왼발을 order 위치로 옮기기
                dp[n][order][i] = min(dp[n-1][j][i] + force[j][order], dp[n][order][i])
                
    n += 1
    idx += 1
    
n -= 1    # 0 때문에 늘어난 n 줄이기
result = sys.maxsize
for i in range(5):
    for j in range(5):
        result = min(result, dp[n][i][j])    # n개를 밟았을 때 가능한 모든 경우의 수 중 최솟값
        
print(result)