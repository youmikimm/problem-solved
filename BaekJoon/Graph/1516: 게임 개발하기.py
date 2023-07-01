# 위상정렬 - N개의 각 건물이 완성되기까지 걸리는 최소 시간
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())    # 건물의 종류 수
adjList = [[] for _ in range(N+1)]
time = [0] * (N+1)  # 건물 짓는 데 걸리는 시간
inDegree = [0] * (N+1)

for i in range(1, N+1):  # 각 건물을 짓는 데 걸리는 시간, 그 건물을 짓기 위해 먼저 지어야 하는 건물들의 번호
    myInput = list(map(int, input().split()))
    time[i] = myInput[0]
    for j in range(1, len(myInput)-1):
        pre = myInput[j]    # 먼저 지어야 하는 건물 번호
        adjList[pre].append(i)
        inDegree[i] += 1

Q = deque()

for i in range(1, N+1):
    if inDegree[i] == 0:
        Q.append(i)

result = [0] * (N+1)

while Q:
    now = Q.popleft()
    for n in adjList[now]:
        inDegree[n] -= 1
        result[n] = max(result[n], result[now] + time[now])
        if inDegree[n] == 0:
            Q.append(n)

for i in range(1, N+1):
    print(result[i] + time[i])