import sys, math
input = sys.stdin.readline

tc = int(input())   # 테스트 케이스 개수

for _ in range(tc):
    cnt = 0     # 진입/이탈 횟수
    x1, y1, x2, y2 = map(int, input().split())  # 출발지 좌표, 도착지 좌표
    pnum = int(input())     # 행성계 개수
    for _ in range(pnum):
        cx, cy, r = map(int, input().split())   # 행성계 중점좌표, 반지름
        dd = math.sqrt((x1-cx)**2 + (y1-cy)**2)
        da = math.sqrt((x2-cx)**2 + (y2-cy)**2)
        if dd < r and da < r:   # 둘다 안에 있음
            pass
        elif dd < r:    # 출발지만 원 안에 있음
            cnt += 1
        elif da < r:    # 도착지만 원 안에 있음
            cnt += 1
    print(cnt)