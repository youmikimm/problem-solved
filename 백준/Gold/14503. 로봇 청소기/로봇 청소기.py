import sys
input = sys.stdin.readline

N, M = map(int, input().split())
start_r, start_c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
clean_count = 0

def DFS(x, y, d):
    global clean_count

    if room[x][y] == 0:
        room[x][y] = 2    # 청소 완료
        clean_count += 1
    
    for _ in range(4):
        nd = (d + 3) % 4
        nx, ny = x + direction[nd][0], y + direction[nd][1]
        
        if room[nx][ny] == 0:
            DFS(nx, ny, nd)
            return
            
        d = nd

    nd = (d + 2) % 4    # 후진
    nx, ny = x + direction[nd][0], y + direction[nd][1]
    
    if room[nx][ny] == 1:
        return

    DFS(nx, ny, d)

DFS(start_r, start_c, d)
print(clean_count)