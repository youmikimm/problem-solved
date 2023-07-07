# 모든 도시의 쌍 (A, B)에 대해서 도시 A에서 B로 가는데 필요한 비용의 최솟값을 구하는 프로그램
# 도시의 최대 개수가 100개로 매우 작으므로 플로이드-워셜 사용 가능
import sys
input = sys.stdin.readline
inf = sys.maxsize

n = int(input())    # 도시 개수
m = int(input())    # 버스 개수
adjMat = [[inf for _ in range(n+1)] for _ in range(n+1)]     # 인접 행렬
for i in range(1, n+1):
    adjMat[i][i] = 0

for _ in range(m):
    s, e, c = map(int, input().split()) # 출발지, 도착지, 비용
    if adjMat[s][e] > c:
        adjMat[s][e] = c

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if adjMat[i][j] > adjMat[i][k] + adjMat[k][j]:
                adjMat[i][j] = adjMat[i][k] + adjMat[k][j]

for i in range(1, n+1):
    for j in range(1, n+1):
        if adjMat[i][j] == inf:     # 도달할 수 없는 경우
            print(0, end=' ')
        else:
            print(adjMat[i][j], end=' ')
    print()