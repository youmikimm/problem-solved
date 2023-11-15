import sys
input = sys.stdin.readline

numberOfStairs = int(input())
points = [0] * (numberOfStairs + 1)
dp = [0] * (numberOfStairs + 1)

for i in range(1, numberOfStairs + 1):
    points[i] = int(input())
    
if numberOfStairs == 1:
    print(points[1])
    exit()
elif numberOfStairs == 2:
    print(points[1] + points[2])
    exit()
    
dp[1] = points[1]
dp[2] = points[1] + points[2]

for i in range(3, numberOfStairs + 1):
    dp[i] = max(dp[i-3] + points[i-1] + points[i], dp[i-2] + points[i])
    
print(dp[-1])