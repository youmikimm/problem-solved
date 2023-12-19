import sys
input = sys.stdin.readline

count = int(input())
stack = []

for i in range(count):
    num = int(input())
    if(num == 0):
        stack.pop()
    else:
        stack.append(num)

print(sum(stack))