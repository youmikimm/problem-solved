# 1번 도시에서 출발해서 나머지 도시로 가는 가장 빠른 시간을 구하는 프로그램
import sys
input = sys.stdin.readline
inf = sys.maxsize
N, M = map(int, input().split())    # 도시 개수, 버스 노선 개수
edgeList = []
distance = [inf] * (N+1)
distance[1] = 0

for i in range(M):
    A, B, C = map(int, input().split()) # 출발지, 도착지, 시간
    edgeList.append((A, B, C))

for _ in range(N-1):    # (노드 개수 - 1) 만큼 반복
    for s, e, t in edgeList:
        if distance[s] != inf and distance[e] > distance[s] + t:
            distance[e] = distance[s] + t

minus = False   # 음수 사이클 존재 여부

for s, e, t in edgeList:    # 음수 가중치가 있는지 확인
    if distance[s] != inf and distance[e] > distance[s] + t:
        minus = True

if not minus:
    for i in range(2, N+1):
        if distance[i] != inf:
            print(distance[i])
        else:
            print(-1)
else:
    print(-1)