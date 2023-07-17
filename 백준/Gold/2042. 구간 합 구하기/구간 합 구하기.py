import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
height = 1
cnt = N

while cnt > 0:
    cnt //= 2
    height += 1

size = 2 ** height - 1  # 트리 노드 개수는 2^h - 1
tree = [0] * (size + 1)  # 트리에서 인덱스는 1부터 시작
leafStartIdx = 2 ** (height-1)

for i in range(leafStartIdx, leafStartIdx + N):
    tree[i] = int(input())  # 주어진 데이터로 리프노드 채우기

# 구간합 트리 초기화
idx = size
while idx > 1:
    tree[idx//2] = tree[idx-1] + tree[idx]
    idx -= 2

def update(idx, val):   # 주어진 데이터에서 idx번째 값을 val로 바꾸기
    loc = leafStartIdx + idx - 1    # idx번째 값의 실제 트리 상 위치
    diff = val - tree[loc]  # (새로운 값 - 현재 값) 차이
    tree[loc] = val     # 값 업데이트

    for _ in range(height-1):
        loc //= 2
        tree[loc] += diff

def rangeSum(start, end): # start번째 ~ end번째 값 구간 합 구하기
    startIdx = leafStartIdx + start - 1
    endIdx = leafStartIdx + end - 1
    result = 0

    while endIdx >= startIdx:
        if startIdx % 2 == 1:
            result += tree[startIdx]
        if endIdx % 2 == 0:
            result += tree[endIdx]

        startIdx = (startIdx + 1) // 2
        endIdx = (endIdx - 1) // 2

    print(result)


for _ in range(K+M):
    a, b, c = map(int, input().split())
    if a == 1:
        update(b, c)
    else:
        rangeSum(b, c)