import sys
input = sys.stdin.readline

T = int(input())

def computer(a, b):
    if a == 1 or a == 5 or a == 6:
        return a
    elif a == 0:    # a = 10, 20, 30, ...
        return 10
    elif a == 2:
        tmp = [6, 2, 4, 8]
        return tmp[b % 4]
    elif a == 3:
        tmp = [1, 3, 9, 7]
        return tmp[b % 4]
    elif a == 4:
        tmp = [6, 4]
        return tmp[b % 2]
    elif a == 7:
        tmp = [1, 7, 9, 3]
        return tmp[b % 4]
    elif a == 8:
        tmp = [6, 8, 4, 2]
        return tmp[b % 4]
    elif a == 9:
        tmp = [1, 9]
        return tmp[b % 2]

for _ in range(T):
    a, b = map(int, input().split())
    print(computer(a % 10, b))
    