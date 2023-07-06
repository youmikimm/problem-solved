# 방향 그래프가 주어지면 주어진 시작점에서 다른 모든 정점으로의 최단 경로를 구하는 프로그램
import sys
from queue import PriorityQueue
input = sys.stdin.readline

V, E = map(int, input().split())    # 노드, 에지의 개수
S = int(input())    # 출발 노드 번호
adjList = [[] for _ in range(V+1)]  # 인접 리스트
distance = [sys.maxsize] * (V+1)   # 최단 거리 리스트
distance[S] = 0 # 출발 노드는 최단 거리가 0
visited = [False] * (V+1)   # 방문 여부
Q = PriorityQueue()

for _ in range(E):
    u, v, w = map(int, input().split()) # u -> v, 가중치 w (두 노드 사이에 가중치 w가 있을 수 있음)
    adjList[u].append((v, w))   # 인접 리스트에 (도착노드, 가중치) 추가

Q.put((0, S))   # 출발 노드 <- 우선순위큐는 앞의 값이 작은 값부터 리턴하므로 가중치가 앞에 있어야 함

while Q.qsize() > 0:
    now = Q.get()
    nowNode = now[1]    # 현재 노드
    if visited[nowNode]:    # 방문한 적 없는 노드만
        continue
    visited[nowNode] = True
    for connect in adjList[nowNode]:
        node = connect[0]
        weight = connect[1]
        if distance[node] > (distance[nowNode] + weight):
            distance[node] = distance[nowNode] + weight
            Q.put((distance[node], node))


for i in range(1, V+1):
    if visited[i]:
        print(distance[i])
    else:
        print("INF")