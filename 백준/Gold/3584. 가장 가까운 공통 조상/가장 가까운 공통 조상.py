import sys
input = sys.stdin.readline

def find_parent(parent, child):
    result = [child]
    while parent[child]:
        result.append(parent[child])
        child = parent[child]
    return result


def lca():
    nodeCount = int(input())
    parent = [0 for _ in range(nodeCount + 1)]

    for _ in range(nodeCount - 1):
        pNode, cNode = map(int, input().split())
        parent[cNode] = pNode

    node1, node2 = map(int, input().split())
    node1_parent = find_parent(parent, node1)
    node2_parent = find_parent(parent, node2)

    i, j = 0, 0
    if len(node1_parent) > len(node2_parent):
        i = len(node1_parent) - len(node2_parent)
    else:
        j = len(node2_parent) - len(node1_parent)

    while node1_parent[i] != node2_parent[j]:
        i += 1
        j += 1

    print(node1_parent[i])


def solve():
    testCase = int(input())
    for _ in range(testCase):
        lca()
        
solve()