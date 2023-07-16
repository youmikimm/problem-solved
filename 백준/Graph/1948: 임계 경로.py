# 위상 정렬 - 도착 도시에서 모두 만나기까지 걸리는 최소 시간, 1분도 쉬지 않고 달려야 하는 사람들이 지나는 도로의 수
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())    # 도시 수
M = int(input())    # 도로 수
adjList = [[] for _ in range(N+1)]
invAdjList = [[] for _ in range(N+1)]
inDegree = [0] * (N+1)

for i in range(M):
    s, e, t = map(int, input().split())
    adjList[s].append((e, t))
    invAdjList[e].append((s, t))
    inDegree[e] += 1

start, end = map(int, input().split())

Q = deque()
Q.append(start)
result = [0] * (N+1)

while Q:
    now = Q.popleft()
    for n in adjList[now]:
        inDegree[n[0]] -= 1
        result[n[0]] = max(result[n[0]], result[now] + n[1])
        if inDegree[n[0]] == 0:
            Q.append(n[0])

resultCount = 0
visited = [False] * (N+1)
Q.clear()

Q.append(end)
visited[end] = True

while Q:    # 위상정렬 역방향
    now = Q.popleft()
    for n in invAdjList[now]:   # 1분도 쉬지 않는 도로
        if result[n[0]] + n[1] == result[now]:
            resultCount += 1
            if not visited[n[0]]:
                visited[n[0]] = True
                Q.append(n[0])

print(result[end])  # 만나는 시간
print(resultCount)  # 1분도 쉬지 않고 달려야 하는 도로의 수