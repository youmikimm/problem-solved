import sys
input = sys.stdin.readline

money = int(input())
twoCnt = 0
fiveCnt = 0

while True:
  if money % 5 == 0:
    fiveCnt = money // 5
    break
  else:
    money -= 2
    twoCnt += 1

if money < 0:
    print(-1)
else:
    print(twoCnt + fiveCnt)