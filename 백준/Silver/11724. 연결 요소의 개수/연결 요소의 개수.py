import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

# 정점, 간선의 개수
v, e = map(int,input().split())
adjacent = [[] for _ in range(v+1)]
visited = [False for _ in range(v+1)]
component = 0    # 연결 요소 개수

# 간선의 양 끝 정점이 주어짐 -> 인접 리스트 만들기
for i in range(e):
    a, b = map(int, input().split())  # 두 정점 a, b
    adjacent[a].append(b)          # 방향이 없는 그래프이므로 두 정점 서로를 추가
    adjacent[b].append(a)

def DFS(n):
    visited[n] = True  # 현재 방문한 노드 기록
    for x in adjacent[n]:
        if not visited[x]:
            DFS(x)
  
for i in range(1, v+1):  # 방문하지 않은 노드를 찾아서 방문
    if not visited[i]:
        component += 1
        DFS(i)              # 시작은 1번 노드부터

# 연결 요소의 개수
print(component)