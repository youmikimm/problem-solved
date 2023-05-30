import sys
input = sys.stdin.readline
section = [0] * 101

n, m = map(int, input().split())
start = 1
for _ in range(n):
    length, limit = map(int,input().split())
    for i in range(start, start + length):
        section[i] = limit
    start += length

speeding = 0    # 과속한 정도
start = 1
for _ in range(m):
    length, speed = map(int, input().split())
    for i in range(start, start + length):
        speeding = max(speeding, speed - section[i])    # 과속한 정도
    start += length

print(speeding)