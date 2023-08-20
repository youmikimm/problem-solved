import sys
input = sys.stdin.readline

total = int(input())
N = int(input())
mySum = 0
for _ in range(N):
    cost, cnt = map(int, input().split())
    mySum += cost * cnt
    
if total == mySum:
    print('Yes')
else:
    print('No')