import sys

input = sys.stdin.readline

w, n = map(int, input().split())
jewels = []
leftSpace = w   # 배낭에 남은 공간
totPrice = 0

for i in range(n):
    weight, price = map(int, input().split())
    jewels.append([weight, price])

jewels.sort(lambda x: -x[1])  # 가격을 기준으로 내림차순 정렬

for i in range(n):
    if leftSpace == 0:
        break
    if (leftSpace - jewels[i][0]) >= 0:
        leftSpace -= jewels[i][0]
        totPrice += jewels[i][1] * jewels[i][0]
    else:  # 귀금속을 쪼개야 하는 경우
        totPrice += jewels[i][1] * leftSpace
        leftSpace = 0

print(totPrice)