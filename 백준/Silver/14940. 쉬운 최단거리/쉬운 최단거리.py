import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
land = [list(map(int, input().split())) for _ in range(n)]
distance = [[-1] * m for _ in range(n)]
move = [(0, 1), (0, -1), (-1, 0), (1, 0)]

def BFS(i, j):
    queue = deque()
    queue.append((i, j))
    
    distance[i][j] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + move[i][0], y + move[i][1]
            if 0 <= nx < n and 0 <= ny < m and distance[nx][ny] == -1:
                if land[nx][ny] == 0:
                    distance[nx][ny] = 0
                elif land[nx][ny] == 1:
                    distance[nx][ny] = distance[x][y] + 1
                    queue.append((nx, ny))

for i in range(n):
    for j in range(m):
        if land[i][j] == 2 and distance[i][j] == -1:
            BFS(i, j)

for i in range(n):
    for j in range(m):
        if land[i][j] == 0:
            print(0, end = ' ')
        else:
            print(distance[i][j], end = ' ')
    print()