import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M, R = map(int, input().split())
visited = [False] * (N+1)
A = [[] for _ in range(N+1)] # 인접 리스트
visit_order = 0
order_list = [0] * (N+1)

for _ in range(M):
    u, v = map(int, input().split())
    A[u].append(v)
    A[v].append(u)

for i in range(1, N+1):
    A[i].sort(reverse=True)

def DFS(i):
    global visit_order

    visited[i] = True
    visit_order += 1
    order_list[i] = visit_order

    for k in A[i]:
        if not visited[k]:
            DFS(k)

DFS(R)

for i in order_list[1:]:
    print(i)