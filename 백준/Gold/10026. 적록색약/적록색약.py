import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
squareMap = []
answer = []
moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
count1 = 0
count2 = 0
visited = [[False] * N for _ in range(N)]

for _ in range(N):
    squareMap.append(list(input().strip()))

def DFS(y, x):
    visited[y][x] = True
    nowColor = squareMap[y][x]
    for dy, dx in moves:
        ny, nx = y + dy, x + dx
        if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx] and squareMap[ny][nx] == nowColor:
            DFS(ny, nx)

def countRegion():
    result = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                DFS(i, j)
                result += 1
    return result

count1 = countRegion()

visited = [[False] * N for _ in range(N)]
for i in range(N):
    squareMap[i] = list(map(lambda x: x.replace('G', 'R'), squareMap[i]))

count2 = countRegion()
print(count1, count2)