import sys
input = sys.stdin.readline

N, M = map(int, input().split())    # N=리프 노드 개수, M=질의 개수
height = 1
leaf = N

while leaf > 0:
    leaf //= 2
    height += 1

treeSize = (2 ** height) - 1
tree = [sys.maxsize] * (treeSize + 1)  # 트리 배열의 인덱스는 1부터 시작
leafStartIdx = 2 ** (height - 1)


for i in range(leafStartIdx, leafStartIdx + N):
    tree[i] = int(input())


# 최솟값 트리 채우기
idx = treeSize - 1
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