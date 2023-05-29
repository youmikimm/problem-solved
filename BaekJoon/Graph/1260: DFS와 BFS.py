'''
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.
입력: 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.
출력: 첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.
'''
import sys
from collections import deque
input = sys.stdin.readline

# 노드의 개수, 에지의 개수, 시작 노드 번호
N, M, V = map(int, input().split())
adjList = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
queue = deque()

def DFS(x):
  visited[x] = True
  print(x, end = " ")
  for i in adjList[x]:
    if not visited[i]:
      DFS(i)

def BFS(x):
    queue.append(x)
    visited[x] = True

    while queue:
        f = queue.popleft()
        print(f, end=" ")
        for i in adjList[f]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 인접 리스트 채우기
for _ in range(M):
  a, b = map(int, input().split())
  adjList[a].append(b)
  adjList[b].append(a)

for i in range(N+1):
  adjList[i].sort()    # 노드 번호가 작은 것부터 방문해야 하므로

DFS(V)  # DFS 결과 출력
print()
visited = [False for _ in range(N+1)]   # BFS를 위해 방문 여부 리스트 초기화
BFS(V)  # BFS 결과 출력