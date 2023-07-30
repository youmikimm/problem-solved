import sys
from collections import deque
import math
input = sys.stdin.readline

N = int(input())    # 노드 개수
tree = [[] for _ in range(N+1)] # 인접 리스트 형태
visited = [False] * (N+1)
depth = [0] * (N+1)


for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

k = int(math.log2(N) + 1)   # k = (2^k < 트리 깊이)를 만족하는 최댓값
parent = [[0 for j in range(N+1)] for i in range(k+1)]  # 부모 정보 - parent[k][n] = n번 노드의 2^k번째 부모


def BFS(x):
    q = deque()
    q.append(x)
    visited[x] = True

    tmpCnt = 0
    thisCnt = 1
    d = 1

    while q:
        this = q.popleft()
        visited[this] = True

        for node in tree[this]:
            if not visited[node]:
                q.append(node)
                visited[node] = True
                depth[node] = d
                parent[0][node] = this  # 부모 노드 저장(=2^0번째 부모)

        tmpCnt += 1
        if tmpCnt == thisCnt:
            d += 1
            tmpCnt = 0
            thisCnt = len(q)


BFS(1)

for i in range(1, k+1):
    for j in range(1, N+1):
        parent[i][j] = parent[i-1][parent[i-1][j]]  # parent 점화식


def LCA(n1, n2):
    if depth[n1] < depth[n2]:   # n1이 더 깊도록
        n1, n2 = n2, n1

    for i in range(k, -1, -1):  # 깊이 맞춰주기
        if pow(2, i) <= depth[n1] - depth[n2]:  # 2^i <= 깊이 차
            if depth[parent[i][n1]] >= depth[n2]:   # n1의 2^i번째 부모의 깊이가 더 깊거나 같도록 <- 반복할 수 있게
                n1 = parent[i][n1]  # 2^i번재 부모 노드로 대체 => 깊이를 끌어 올리기

    for i in range(k, -1, -1):
        if n1 == n2:    # 같은 노드라면 조상 찾기 끝
            return n1
        if parent[i][n1] != parent[i][n2]:  # 같은 조상이 나올 때까지
            n1 = parent[i][n1]
            n2 = parent[i][n2]

    return parent[0][n1]    # 끝내 부모노드가 일치하지 않는다면


M = int(input())    # 질의 개수
for _ in range(M):
    a, b = map(int, input().split())
    print(LCA(a, b))
