# 도착 도시에 도착할 때 지니고 있는 돈의 액수를 최대로 하고자 할 때, 이 최댓값을 구하는 프로그램
import sys
input = sys.stdin.readline
N, sCity, eCity, M = map(int, input().split())
edgeList = []
distance = [-sys.maxsize] * N   # 최단 거리 리스트

for _ in range(M):
    start, end ,price = map(int, input().split())
    edgeList.append((start, end, price))

money = list(map(int, input().split()))

distance[sCity] = money[sCity]

for i in range(N+101):
    for start, end, price in edgeList:
        if distance[start] == -sys.maxsize:     # 출발노드가 미방문 노드
            continue
        elif distance[start] == sys.maxsize:
            distance[end] = sys.maxsize
        elif distance[end] < distance[start] + money[end] - price:  # 더 많은 돈을 벌 수 있는 새로운 경로가 있을 때
            distance[end] = distance[start] + money[end] - price
            if i >= N-1:
                distance[end] = sys.maxsize

if distance[eCity] == -sys.maxsize:     # 도착 불가능
    print("gg")
elif distance[eCity] == sys.maxsize:    # 돈을 무한히 벌 수 있는 경우
    print("Gee")
else:
    print(distance[eCity])