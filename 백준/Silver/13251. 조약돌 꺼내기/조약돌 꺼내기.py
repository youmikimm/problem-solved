import sys, math
input = sys.stdin.readline

M = int(input())    # 색깔 개수
stoneCnt = list(map(int, input().strip().split()))
K = int(input())    # N개의 조약돌 중 K개를 뽑았을 때 모두 같은 색일 확률을 구하고자 함

N = sum(stoneCnt)   # 조약돌 총 개수
sameColorCase = 0
for i in range(M):
    num = stoneCnt[i]   # 특정 색 조약돌 중 K개를 뽑는 경우의 수
    if num >= K:
        tmp = math.comb(num, K)
        sameColorCase += tmp
totalCase = math.comb(N, K)

print(sameColorCase / totalCase)