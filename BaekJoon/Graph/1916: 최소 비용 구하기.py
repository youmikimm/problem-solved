# N개의 도시가 있다. 그리고 한 도시에서 출발하여 다른 도시에 도착하는 M개의 버스가 있다.
# 우리는 A번째 도시에서 B번째 도시까지 가는데 드는 버스 비용을 최소화 시키려고 한다.
# A번째 도시에서 B번째 도시까지 가는데 드는 최소비용을 출력하여라. 도시의 번호는 1부터 N까지이다.
import sys
from queue import PriorityQueue
input = sys.stdin.readline

city = int(input()) # 도시 개수
bus = int(input())  # 버스 개수
distance = [sys.maxsize] * (city+1)
visited = [False] * (city+1)
adjList = [[] for _ in range(city+1)]

for _ in range(bus):
    d, a, c = map(int, input().split())
    adjList[d].append((a, c))

departure, arrival = map(int, input().split())  # 출발지, 도착지
distance[departure] = 0

Q = PriorityQueue()
Q.put((0, departure))

while Q.qsize() > 0:
    select = Q.get()
    selectedNode = select[1]
    if not visited[selectedNode]:    # 방문한 적이 없는 노드만
        visited[selectedNode] = True
        for tmp in adjList[selectedNode]:
            nowNode = tmp[0]
            cost = tmp[1]
            if distance[nowNode] > (distance[selectedNode] + cost):
                distance[nowNode] = distance[selectedNode] + cost
                Q.put((distance[nowNode], nowNode))

print(distance[arrival])