# 가중치 없는 방향 그래프 G가 주어졌을 때 모든 노드 (i, j)에 관해 i에서 j로 가는 경로가 있는지 여부를 구하는 프로그램
import sys
input = sys.stdin.readline

n = int(input())
adjMat = []

for _ in range(n):
    tmp = list(map(int, input().split()))
    adjMat.append(tmp)

for k in range(n):
    for i in range(n):
        for j in range(n):
            if adjMat[i][k] == 1 and adjMat[k][j] == 1: # 중간에 연결 요소가 있다
                adjMat[i][j] = 1

for i in range(n):
    for j in range(n):
        print(adjMat[i][j], end=' ')
    print()