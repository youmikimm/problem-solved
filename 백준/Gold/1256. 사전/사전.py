import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
dp = [[1 for _ in range(N+1)] for _ in range(N+M+1)]

for i in range(2, N+M+1):
    dp[i][1] = i
    for j in range(2, i+1):
        if j > N:
            break
        if i == j:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

if dp[N+M][N] < K:  # 만들 수 있는 문자열의 개수 < K라면 -1 출력
    print(-1)
else:
    result = ''
    while N > 0 and M > 0:
        if dp[N+M-1][N-1] >= K:     # a를 선택했다는 가정 하에 (남은 a,z로 문자열을 만들 수 있는 경우의 수) >= K라면 a를 선택해야
            result += 'a'
            N -= 1                  # a의 개수--
        else:
            result += 'z'
            K -= dp[N+M-1][N-1]
            M -= 1                  # z의 개수--

    if N > 0:
        result += 'a' * N
    elif M > 0:
        result += 'z' * M

    print(result)