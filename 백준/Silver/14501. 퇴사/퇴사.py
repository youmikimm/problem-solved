import sys
input = sys.stdin.readline

N = int(input())
days = [0] * (N+1)
income = [0] * (N+1)
dp = [0] * (N+2)    # i번째 날부터 퇴사일까지 벌 수 있는 최대 수입

for i in range(1, N+1):
    days[i], income[i] = map(int, input().split())
    
for i in range(N, 0, -1):
    if days[i] > N + 1 - i:    # 퇴사까지 남은 일수
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], income[i] + dp[i + days[i]])    # (다음날 ~ 퇴사일 수입), (현재 상담 수입 + 상담 끝난 이후 수입) 중 큰 값

print(dp[1])