import sys
input = sys.stdin.readline

numberOfPerson = int(input())
person1, person2 = map(int, input().split())
relationshipsCount = int(input())
relationships = [[] for _ in range(numberOfPerson + 1)]
visited = [False] * (numberOfPerson + 1)
chonCount = [0] * (numberOfPerson + 1)

for _ in range(relationshipsCount):
    p1, p2 = map(int, input().split())
    relationships[p1].append(p2)
    relationships[p2].append(p1)

def dfs(person):
    visited[person] = True
    for i in relationships[person]:
        if not visited[i]:
            chonCount[i] = chonCount[person] + 1
            dfs(i)

dfs(person1)
if chonCount[person2] == 0:
    print(-1)
else:
    print(chonCount[person2])