import sys

input = sys.stdin.readline

N = int(input())  # 재료 가짓수
visited = [False] * N
adjList = [[] for _ in range(N)]
amount = [0] * N  # 각 재료의 양
lcm = 1  # 최소공배수


def gcd(a, b):  # 최대공약수
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def dfs(x):
    visited[x] = True
    for node in adjList[x]:
        num = node[0]  # num번 재료
        if not visited[num]:
            amount[num] = amount[x] * node[2] // node[1]
            # x번 재료: num번 재료 = node[1] : node[2] 비율
            dfs(num)


for _ in range(N - 1):
    a, b, p, q = map(int, input().split())
    adjList[a].append((b, p, q))  # 비율까지 저장. a번:b번 = p:q
    adjList[b].append((a, q, p))  # b번:a번 = q:p
    lcm *= (p * q // gcd(p, q))

amount[0] = lcm
dfs(0)  # 0에서부터 탐색 시작. 0번 노드의 양을 최소공배수로 가정
newGcd = amount[0]

for i in range(1, N):
    newGcd = gcd(newGcd, amount[i])  # 최대공약수 다시 업데이트

for i in range(N):
    print(amount[i] // newGcd, end=' ')