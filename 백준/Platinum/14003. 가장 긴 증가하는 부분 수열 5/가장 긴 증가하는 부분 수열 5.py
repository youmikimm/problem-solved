import sys, bisect
input = sys.stdin.readline

num = int(input())
inputArr = list(map(int, input().split()))
stack = []
record = []    # 증가하는 수열의 길이 저장
for x in inputArr:
    if not stack or stack[-1] < x:  # 현재 수열이 큰 경우 -> 증가하는 수열에 원소 추가
        stack.append(x)
        record.append((len(stack)-1, x))   # (인덱스, 값) 형태로 저장
    else:                           # 현재 수열이 작은 경우 -> 적절한 위치 찾기
        idx = bisect.bisect_left(stack, x)
        stack[idx] = x
        record.append((idx, x))

answer = [0] * 1000001
index = len(stack) - 1
for i in range(len(record)-1, -1, -1):  # 뒤에서부터 추적
    if record[i][0] == index:
        answer[index] = record[i][1]
        index -= 1

print(len(stack))

for i in range(len(stack)):
    print(answer[i], end=' ')