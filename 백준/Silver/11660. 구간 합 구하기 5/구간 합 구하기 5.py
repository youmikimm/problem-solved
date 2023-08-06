import sys
n, m = map(int, sys.stdin.readline().split())   # n은 표의 크기, m은 합을 구해야 하는 횟수
table = [[0 for i in range(n+1)] for j in range(n+1)]
sumTable = [[0 for i in range(n+1)] for j in range(n+1)]

for i in range(1, n+1):
    table[i] = [0] + list(map(int, sys.stdin.readline().split()))

for i in range(1, n+1):  # 구간 합 sumTable 채우기
    for j in range(1, n+1):
        sumTable[i][j] = table[i][j] + sumTable[i][j-1] + sumTable[i-1][j] - sumTable[i-1][j-1]

for i in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    print(sumTable[x2][y2]-sumTable[x2][y1-1]-sumTable[x1-1][y2] + sumTable[x1-1][y1-1])