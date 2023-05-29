import sys
input = sys.stdin.readline

N, K = map(int, input().split())
scores = list(map(int, input().split()))
sumScores = [scores[0]]
for i in range(1, N):
    sumScores.append(sumScores[i-1] + scores[i])

for _ in range(K):
    start, end = map(int, input().split())
    total = 0

    if start == 1:
        total = sumScores[end-1]
    else:
        total = sumScores[end-1] - sumScores[start - 2]
    print(format(total / (end - start + 1), ".2f")) # 소수점 아래 두자리로 포맷팅