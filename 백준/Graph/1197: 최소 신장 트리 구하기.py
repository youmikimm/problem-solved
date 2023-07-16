# 최소 신장 트리 구하기
import sys
from queue import PriorityQueue
input = sys.stdin.readline

v, e = map(int, input().split())
Q = PriorityQueue()
parent = [0] * (v+1)    # 대표 노드 저장

for i in range(v+1):
    parent[i] = i

for _ in range(e):
    a, b, c = map(int, input().split())
    Q.put((c, a, b))    # 가중치 순으로 정렬해야 하므로 가중치부터

def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

edge = 0
result = 0  # 최소 신장 트리의 가중치

while edge < v-1:
    c, a, b = Q.get()
    if find(a) != find(b):  # 부모가 다른 경우에만 연결
        union(a, b)
        result += c
        edge += 1

print(result)