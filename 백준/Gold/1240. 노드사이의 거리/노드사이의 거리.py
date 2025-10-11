import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
A = [[] for _ in range(N+1)]

def BFS(n, destination):
    q = deque()
    q.append((n, 0))
    visited = [False] * (N + 1)
    visited[n] = True

    while q:
        node, dist = q.popleft()

        if node == destination:
            return dist

        for i, d in A[node]:
            if not visited[i]:
                q.append((i, dist + d))
                visited[i] = True
                

for _ in range(N-1):
    u, v, d = map(int, input().split())
    A[u].append((v, d)) # (상대 노드, 거리)
    A[v].append((u, d))


for _ in range(M):
    i, j = map(int, input().split())
    print(BFS(i, j))