import sys
input = sys.stdin.readline

N = int(input())
D = [0, 0, 1]   # 1명 있을 때는 선물 교환 불가, 2명 있을 때는 서로 교환 -> D[1] = 0, D[2] = 1

for i in range(3, N+1):
    D.append((i-1) * (D[i-2] + D[i-1]) % 1000000000)

print(D[N])