import sys,heapq

input = sys.stdin.readline

N = int(input())
times = []
for _ in range(N):
    start, end = map(int, input().split())
    times.append((start, end))

times.sort(key=lambda x: x[0])
Q = []
heapq.heappush(Q, times[0][1])

for i in range(1, N):
    if times[i][0] >= Q[0]:
        heapq.heappop(Q)
    heapq.heappush(Q, times[i][1])

print(len(Q))