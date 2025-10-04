import sys
input = sys.stdin.readline

N, M = list(map(int, input().split())) # N x N 배열, M개의 질의
A = [[0] * (N+1)]
D = [[0] * (N+1) for _ in range(N+1)]

# 2차원 배열(원 데이터) 만들기
for _ in range(N):
    A_row = [0] + list(map(int, input().split()))
    A.append(A_row)

# 덧셈 배열 만들기
for i in range(1, N+1):
    for j in range(1, N+1):
        D[i][j] = D[i-1][j] + D[i][j-1] - D[i-1][j-1] + A[i][j]

# 질의에 대한 답 리턴
for _ in range(M):
	sx, sy, ex, ey = map(int, input().split())
	print(D[ex][ey] - D[sx-1][ey] - D[ex][sy-1] + D[sx-1][sy-1])
