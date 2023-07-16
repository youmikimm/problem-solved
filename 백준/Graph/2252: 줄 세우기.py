# 일부 학생들의 키를 비교한 결과가 주어졌을 때 줄을 세우는 프로그램
# 위상정렬
import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())    # N = 학생 수, M = 비교한 횟수
adjList = [[] for _ in range(N+1)]
inDegree = [0 for _ in range(N+1)]

for _ in range(M):      # 인접 리스트 및 진입차수 배열 업데이트
    h1, h2 = map(int, input().split())
    adjList[h1].append(h2)
    inDegree[h2] += 1

Q = deque()     # 위상정렬 수행
for i in range(1, N+1):     # 진입차수 배열에서 0인 인덱스를 큐에 저장
    if inDegree[i] == 0:
        Q.append(i)

while Q:
    now = Q.popleft()
    print(now, end=' ')
    for n in adjList[now]:
        inDegree[n] -= 1
        if inDegree[n] == 0:
            Q.append(n)