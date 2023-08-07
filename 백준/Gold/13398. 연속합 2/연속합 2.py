import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

left = [arr[0]] + [0] * (N-1)

for i in range(1, N):
    left[i] = max(arr[i], arr[i] + left[i-1])
    
result = max(left)    # 제거하지 않았을 때의 연속합의 최댓값

right = [0] * (N-1) + [arr[N-1]]

for i in range(N-2, -1, -1):
    right[i] = max(arr[i], arr[i] + right[i+1])
    
for i in range(1, N-1):
    omit = left[i-1] + right[i+1]    # i를 제외한 연속합의 최댓값
    result = max(result, omit)
    
print(result)