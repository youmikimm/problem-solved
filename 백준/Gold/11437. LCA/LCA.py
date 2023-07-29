import sys
from collections import deque
input = sys.stdin.readline

N = int(input())    # 노드 개수
tree = [[] for _ in range(N+1)]
depth = [0] * (N+1)
parent = [0] * (N+1)
visited = [False] * (N+1)

for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

def BFS(x):
    q = deque()
    q.append(x)
    visited[x] = True
    d = 1   # 깊이
    thisCnt = 1    # 트리에서 d의 깊이에 위치한 노드의 개수
    tmpCnt = 0     # d의 깊이에서 살펴본 노드의 개수

    while q:
        this = q.popleft()
        for node in tree[this]:
            if not visited[node]:
                q.append(node)
                visited[node] = True
                parent[node] = this
                depth[node] = d

        tmpCnt += 1
        if thisCnt == tmpCnt:   # 현재 깊이에 위치한 노드를 모두 살펴봄
            thisCnt = len(q)
            tmpCnt = 0
            d += 1


BFS(1)


def LCA(n1, n2):  # a, b의 공통 조상
    while depth[n1] != depth[n2]:   # depth 일치하도록
        if depth[n1] > depth[n2]:
            n1 = parent[n1]
        else:
            n2 = parent[n2]

    while n1 != n2:
        n1 = parent[n1]
        n2 = parent[n2]

    return n1


M = int(input())    # 질의 개수
for _ in range(M):
    a, b = map(int, input().split())    # a, b의 공통 조상 노드를 찾고 싶음
    print(LCA(a, b))
