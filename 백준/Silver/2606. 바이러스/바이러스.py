import sys
input = sys.stdin.readline

n = int(input())
couples = int(input())
visited = [False] * (n+1)
adjList = [[] for _ in range(n+1)]
computers = 0

for i in range(couples):
    a, b = map(int, input().split())
    adjList[a].append(b)
    adjList[b].append(a)

def dfs(node):
    global computers
    visited[node] = True
    for next in adjList[node]:
        if not visited[next]:
            computers += 1
            dfs(next)

dfs(1)
print(computers)