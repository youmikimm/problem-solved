import sys
input = sys.stdin.readline

a, b = input().strip().split()
lA = list(map(int, a))
lB = list(map(int, b))

print(sum(lA) * sum(lB))