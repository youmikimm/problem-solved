import sys
from collections import deque
input = sys.stdin.readline

N, M, R = map(int, input().split())
queue = deque()
visited = [0] * (N+1)
adjList = [[] for _ in range(N+1)]
order = 1

for _ in range(M):
    a, b = map(int, input().split())
    adjList[a].append(b)
    adjList[b].append(a)

for i in range(1, N+1):
    adjList[i].sort()

def BFS(start):
    global order
    queue.append(start)
    visited[start] = order
    while queue:
        node = queue.popleft()
        for next in adjList[node]:
            if visited[next] == 0:
                order += 1
                queue.append(next)
                visited[next] = order


BFS(R)

for i in range(1, N+1):
    print(visited[i])