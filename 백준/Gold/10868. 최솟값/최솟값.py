import sys
input = sys.stdin.readline

N, M = map(int, input().split())    # N=리프 노드 개수, M=질의 개수
height = 1
leaf = N

while leaf > 0:
    leaf //= 2
    height += 1

size = 2 ** (height + 1)  # 높이가 h인 트리의 노드 개수는 2^h - 1이지만 h의 오차 때문에 넉넉하게
tree = [sys.maxsize] * (size + 1)  # 트리에서 인덱스는 1부터 시작하니까 트리 배열 개수에 +1
leafStartIdx = size // 2


for i in range(leafStartIdx, leafStartIdx + N):
    tree[i] = int(input())


# 최솟값 트리 채우기
idx = size - 1
while idx > 1:
    if tree[idx//2] > tree[idx]:
        tree[idx//2] = tree[idx]
    idx -= 1

def getMin(start, end):     # 세그먼트 트리 업데이트 방식
    myMin = sys.maxsize
    while start <= end:
        if start % 2 == 1:  # start index가 홀수일 때 해당 노드 선택
            myMin = min(myMin, tree[start])
            start += 1
        if end % 2 == 0:    # end index가 짝수일 때 해당 노드 선택
            myMin = min(myMin, tree[end])
            end -= 1
        start = start // 2
        end = end // 2
    return myMin

for _ in range(M):
    s, e = map(int, input().split())
    s += leafStartIdx - 1
    e += leafStartIdx - 1
    print(getMin(s, e))