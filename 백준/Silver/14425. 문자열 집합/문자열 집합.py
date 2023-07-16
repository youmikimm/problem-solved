import sys
input = sys.stdin.readline
N, M = map(int, input().split())
tmp = []
cnt = 0

for _ in range(N):
    tmp.append(input())
S = set(tmp)

for _ in range(M):
    if input() in S:
        cnt += 1
        
print(cnt)