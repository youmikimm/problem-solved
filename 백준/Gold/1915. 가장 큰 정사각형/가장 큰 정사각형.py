import sys

input = sys.stdin.readline

N, M = map(int, input().split())
map = [[0 for _ in range(M+1)] for _ in range(N+1)]
length = 0

for i in range(1, N+1):
    tmp = [0] + list(input().strip())
    for j in range(1, M+1):
        map[i][j] = int(tmp[j])
        if map[i][j] == 1:
            map[i][j] = min(map[i-1][j-1], map[i][j-1], map[i-1][j]) + 1
        if length < map[i][j]:
            length = map[i][j]

print(length * length)