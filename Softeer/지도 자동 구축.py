import sys
input = sys.stdin.readline

n = int(input())    # n단계의 점의 개수를 구하고자 함.
linePoint = 2   # 0단계에서 한 변에 위치한 점의 개수는 2개

for _ in range(1, n+1):
    linePoint = 2 * linePoint - 1
print(linePoint ** 2)