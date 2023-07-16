'''
방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.
입력: 첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2) 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.
출력: 첫째 줄에 연결 요소의 개수를 출력한다.
'''
import sys
input = sys.stdin.readline

def DFS(n):
    visited[n] = True
    for x in adjList[n]:
        if not visited[x]:
            DFS(x)

n, m = map(int,input().split())
adjList = [[] for x in range(n+1)]
visited = [False for _ in range(n+1)]
cnt = 0   # 연결 요소의 개수

for i in range(m):  # 인접 리스트 생성
    a, b = map(int, input().split())
    adjList[a].append(b)
    adjList[b].append(a)

for i in range(1, n+1):    # 방문하지 않았던 노드를 찾아서 방문, 0번은 없으므로 1번 노드부터 방문
    if not visited[i]:
        DFS(i)
        cnt += 1    # 방문하지 않았던 곳이므로 연결요소 1개 추가

print(cnt)