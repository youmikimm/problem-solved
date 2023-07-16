# 노드를 하나 제거했을 때 남아있는 리프 노드의 개수 구하기
import sys
input = sys.stdin.readline

N = int(input())    # 노드 개수
tmp = list(map(int, input().split()))   # 각 노드(0번~N-1번)의 부모 노드 저장
removedNode = int(input())  # 제거되는 노드
adjList = [[] for _ in range(N)]
visited = [False] * N
root = -1
leaf = 0    # 리프노드 개수

for i in range(N):
    if tmp[i] == -1:
        root = i
        continue
    adjList[i].append(tmp[i])
    adjList[tmp[i]].append(i)


def DFS(n):
    global leaf
    visited[n] = True
    child = 0
    for x in adjList[n]:
        if not visited[x] and x != removedNode:
            child += 1
            DFS(x)
    if child == 0:
        leaf += 1


if root == removedNode:
    leaf = 0
else:
    DFS(root)
print(leaf)