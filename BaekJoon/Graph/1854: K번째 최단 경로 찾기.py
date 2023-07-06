import sys
import heapq
input = sys.stdin.readline

n, m, k = map(int, input().split())  # 도시 개수, 도로 개수, k
adjList = [[] for _ in range(n+1)]
distance = [[sys.maxsize] * k for _ in range(n+1)]
distance[1][0] = 0
visited = [False] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())     # a -> b 이동할 때 c 시간 소요
    adjList[a].append((b, c))

Q = [(0, 1)]    # (시간, 노드)

while Q:
    sTime, sNode = heapq.heappop(Q)
    for connect in adjList[sNode]:
        nNode, nTime = connect
        newTime = nTime + sTime
        if distance[nNode][k-1] > newTime:
            distance[nNode][k-1] = newTime
            distance[nNode].sort()  # 바로 정렬
            heapq.heappush(Q, (newTime, nNode))

for i in range(1, n+1):
    if distance[i][k-1] == sys.maxsize:
        print(-1)
    else:
        print(distance[i][k-1])