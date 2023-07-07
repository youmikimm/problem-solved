# 케빈 베이컨의 수가 가장 작은 사람을 구하는 프로그램
import sys
input = sys.stdin.readline
inf = sys.maxsize

n, m = map(int, input().split())    # 유저의 수(노드), 친구 관계의 수(에지)
adjMat = [[inf for _ in range(n+1)] for _ in range(n+1)]

for i in range(1, n+1):
    adjMat[i][i] = 0

kCount = []     # 각 유저 별 케빈 베이컨 수

for _ in range(m):      # 친구 관계 정보 저장
    a, b = map(int, input().split())
    adjMat[a][b] = 1
    adjMat[b][a] = 1

for k in range(1, n+1):      # 최단 거리 리스트 완성
    for i in range(1, n+1):
        for j in range(1, n+1):
            if adjMat[i][j] > adjMat[i][k] + adjMat[k][j]:
                adjMat[i][j] = adjMat[i][k] + adjMat[k][j]

for i in range(1, n+1):
    tmp = sum(adjMat[i]) - inf    # 각 행의 합이 곧 해당 유저의 케빈 베이컨 수 (0열은 max값이니 빼기)
    kCount.append(tmp)

minimum = min(kCount)

for i in range(n):
    if kCount[i] == minimum:
        print(i+1)
        break