import sys
input = sys.stdin.readline

stack = []
N = int(input())

for _ in range(N):
    order = list(map(int, input().split()))
    
    if order[0] == 1:    # push
        stack.append(order[1])
    elif order[0] == 2:    # pop
        print(stack.pop()) if len(stack) != 0 else print(-1)
    elif order[0] == 3:    # size
        print(len(stack))
    elif order[0] == 4:
        print(0) if len(stack) != 0 else print(1)
    elif order[0] == 5:
        print(stack[-1]) if len(stack) != 0 else print(-1)
        