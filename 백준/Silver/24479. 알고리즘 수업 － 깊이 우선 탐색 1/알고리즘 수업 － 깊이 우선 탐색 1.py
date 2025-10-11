import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M, R = map(int, input().split())
A = [[] for _ in range(N+1)]
visited = [False] * (N+1)
answer = [0] * (N+1)
order = 0

for _ in range(M):
    u, v = map(int, input().split())
    A[u].append(v)
    A[v].append(u)

for i in range(1, N+1):
    A[i].sort()

def DFS(n):
    global order, answer
    visited[n] = True
    order += 1
    answer[n] = order
    for i in A[n]:
        if not visited[i]:
            DFS(i)

DFS(R)

for i in range(1, N+1):
    print(answer[i])