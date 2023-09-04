import sys
input = sys.stdin.readline

colors = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']

first = input().strip()
second = input().strip()
third = input().strip()

num1 = str(colors.index(first))
num2 = str(colors.index(second))
mult = 10 ** colors.index(third)

print(int(num1 + num2) * mult)