import sys
N = int(sys.stdin.readline())
answer = 665

while N > 0:
    answer += 1
    if '666' in str(answer):
        N -= 1
print(answer)