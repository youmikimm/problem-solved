import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

M, N, K = map(int, input().split())
squareMap = [[0 for _ in range(N)] for _ in range(M)]
moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
visited = [[False] * N for _ in range(M)]
region = 0
count = 0
area = []

for _ in range(K):
    sx, sy, ex, ey = map(int, input().split())
    for i in range(sy, ey):
        for j in range(sx, ex):
            squareMap[i][j] += 1

def DFS(y, x):
    global count
    visited[y][x] = True
    for dy, dx in moves:
        ny, nx = y + dy, x + dx
        if 0<=ny<M and 0<=nx<N and not visited[ny][nx] and squareMap[ny][nx] == 0:
            count += 1
            DFS(ny, nx)
    

for i in range(M):
    for j in range(N):
        if not visited[i][j] and squareMap[i][j] == 0:
            count += 1
            DFS(i, j)
            region += 1
            area.append(count)
        count = 0

area.sort()
print(region)
print(*area)