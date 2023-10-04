import sys
input = sys.stdin.readline

n, m = map(int, input().split())
balls = [i for i in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    
    tmp = balls[a]
    balls[a] = balls[b]
    balls[b] = tmp
    
for i in range(1, n+1):
    print(balls[i], end=' ')