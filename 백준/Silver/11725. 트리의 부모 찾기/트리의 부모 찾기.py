# 각 노드의 부모 구하기. 루트는 1번
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
adjList = [[] for _ in range(N+1)]
visited = [False] * (N+1)
answer = [0] * (N+1)    # 정답 리스트(부모 노드 저장)

for _ in range(N-1):
    a, b = map(int, input().split())
    adjList[a].append(b)
    adjList[b].append(a)

def DFS(n):
    visited[n] = True
    for node in adjList[n]:
        if not visited[node]:   # 미방문일 때만
            answer[node] = n
            DFS(node)

DFS(1)
for i in range(2, N+1):
    print(answer[i])