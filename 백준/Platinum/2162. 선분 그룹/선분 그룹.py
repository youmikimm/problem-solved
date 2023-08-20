import sys
input = sys.stdin.readline
N = int(input())    # 선분 개수
parent = [-1] * 3001    # 부모 선분

def ccw(x1, y1, x2, y2, x3, y3):
    tmp = (x1 * y2 + x2 * y3 + x3 * y1) - (x2 * y1 + x3 * y2 + x1 * y3)
    if tmp > 0:
        return 1
    elif tmp < 0:
        return -1
    return 0


def isOverlapped(x1, y1, x2, y2, x3, y3, x4, y4):
    if min(x1, x2) <= max(x3, x4) and min(x3, x4) <= max(x1, x2) and min(y1, y2) <= max(y3, y4) and min(y3, y4) <= max(y1, y2):
        return True
    return False


def isCrossed(x1, y1, x2, y2, x3, y3, x4, y4):
    abc = ccw(x1, y1, x2, y2, x3, y3)
    abd = ccw(x1, y1, x2, y2, x4, y4)
    cda = ccw(x3, y3, x4, y4, x1, y1)
    cdb = ccw(x3, y3, x4, y4, x2, y2)
    if abc * abd == 0 and cda * cdb == 0:
        return isOverlapped(x1, y1, x2, y2, x3, y3, x4, y4)
    elif abc * abd <= 0 and cda * cdb <= 0:
        return True
    return False

def find(a):
    if parent[a] < 0:
        return a
    parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    p = find(a)
    q = find(b)
    if p == q:
        return
    parent[p] += parent[q]
    parent[q] = p
    
L = []
L.append([])

for i in range(1, N+1):
    L.append([])
    L[i] = list(map(int, input().split()))
    for j in range(1, i):
        if isCrossed(L[i][0], L[i][1], L[i][2], L[i][3], L[j][0], L[j][1], L[j][2], L[j][3]):
            union(i, j)
            
            
groups = 0
cnt = 0

for i in range(1, N+1):
    if parent[i] < 0:    # 음수이면 대표 부모 노드
        groups += 1
        cnt = min(cnt, parent[i])    # 음수의 절댓값이 선분 그룹의 선분 개수
        
print(groups)
print(-cnt)