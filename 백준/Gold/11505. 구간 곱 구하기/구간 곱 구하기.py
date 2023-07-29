import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())  # N개의 수, M번 변경 발생, K번 구간의 곱 구하기
MOD = 1000000007
height = 1
leaf = N

while leaf > 0:
    leaf //= 2
    height += 1

treeSize = (2 ** height) - 1
tree = [1] * (treeSize + 1)  # 트리 배열의 인덱스는 1부터 시작
leafStartIdx = 2 ** (height - 1)

for i in range(leafStartIdx, leafStartIdx + N):  # 리프 노드 채우기
    tree[i] = int(input())

# 트리 초기 세팅
idx = len(tree) - 1  # 곱셈으로 트리 세팅: 부모노드 = 자식노드1 * 자식노드2
while idx > 1:
    tree[idx // 2] = (tree[idx] % MOD) * (tree[idx - 1] % MOD) % MOD
    idx -= 2


def mul(start, end):  # b번째 수 ~ c번째 수 곱
    answer = 1

    s = start + leafStartIdx - 1
    e = end + leafStartIdx - 1

    while s <= e:
        if s % 2 == 1:
            answer = answer * tree[s] % MOD
            s += 1
        if e % 2 == 0:
            answer = answer * tree[e] % MOD
            e -= 1
        s //= 2
        e //= 2

    return answer


def update(loc, val):
    k = loc + leafStartIdx - 1
    tree[k] = val
    while k > 1:
        k //= 2  # 변경된 노드의 부모 노드 선택
        tree[k] = tree[k * 2] % MOD * tree[k * 2 + 1] % MOD


for _ in range(M + K):
    a, b, c = map(int, input().split())
    if a == 1:
        update(b, c)
    else:
        print(mul(b, c))
