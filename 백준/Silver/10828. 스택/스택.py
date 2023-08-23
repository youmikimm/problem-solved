import sys
input = sys.stdin.readline

N = int(input())
stack = []

for _ in range(N):
    order = input()

    if 'push' in order:
        num = int(order[5:])
        stack.append(num)
    elif 'pop' in order:
        print(-1) if len(stack) == 0 else print(stack.pop())
    elif 'size' in order:
        print(len(stack))
    elif 'empty' in order:
        print(1) if len(stack) == 0 else print(0)
    elif 'top' in order:
        print(-1) if len(stack) == 0 else print(stack[-1])