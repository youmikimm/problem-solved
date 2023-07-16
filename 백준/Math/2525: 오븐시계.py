# 훈제오리구이를 시작하는 시각과 오븐구이를 하는 데 필요한 시간이 분단위로 주어졌을 때, 오븐구이가 끝나는 시각을 계산하는 프로그램
import sys
input = sys.stdin.readline

hh, mm = map(int, input().split())
time = int(input())
tmp = mm + time

if time == 60:
    print((hh + 1) % 60, mm)
elif tmp < 60:
    print(hh, mm + time)
else:
    print((hh + tmp // 60) % 24, tmp % 60)