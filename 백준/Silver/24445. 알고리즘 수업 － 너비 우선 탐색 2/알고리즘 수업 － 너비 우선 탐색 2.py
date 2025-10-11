import sys
from collections import deque
input = sys.stdin.readline

N, M, R = map(int, input().split())
A = [[] for _ in range(N+1)]
visited = [False] * (N+1)
order = 1
answer = [0] * (N+1)

for _ in range(M):
    u, v = map(int, input().split())
    A[u].append(v)
    A[v].append(u)

for i in range(1, N+1):
    A[i].sort(reverse=True)

def BFS(n):
    global order, answer
    q = deque()
    q.append(n)
    visited[n] = True
    answer[n] = order

    while q:
        node = q.popleft()
        for k in A[node]:
            if not visited[k]:
                visited[k] = True
                q.append(k)
                order += 1
                answer[k] = order


BFS(R)

for i in range(1, N+1):
    print(answer[i])