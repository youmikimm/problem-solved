import sys
input = sys.stdin.readline

cnt = int(input())
lst = list(map(int, input().split()))
value = int(input())
answer = 0

for num in lst:
    if num == value:
        answer += 1
        
print(answer)