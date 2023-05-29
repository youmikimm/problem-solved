import sys
input = sys.stdin.readline

n = int(input())  # 지도 n * n 크기
visited = [[False for _ in range(n)] for _ in range(n)]
cnt = []   # 각 장애물의 블록 개수
block = 0
myMap = [list(map(int, input().strip())) for _ in range(n)]  # 지도 입력 받기

def DFS(x, y):
    global block
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return
    if not visited[x][y]:
        visited[x][y] = True
        if myMap[x][y] == 1:    # 장애물 블록
            block += 1  # 현 장애물의 블록 개수 추가
            DFS(x,y+1)  # 우, 하, 좌, 상 순으로 호출
            DFS(x+1,y)
            DFS(x,y-1)
            DFS(x-1,y)

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            DFS(i, j)
            if block != 0:
                cnt.append(block)
                block = 0   # 블록 개수 0으로 초기화

print(len(cnt)) # 장애물의 개수
cnt.sort()
for c in cnt:
    print(c)