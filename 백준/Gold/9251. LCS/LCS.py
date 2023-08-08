import sys
input = sys.stdin.readline

s1 = list(input().strip())
s2 = list(input().strip())
l1 = len(s1)
l2 = len(s2)

dp = [[0 for _ in range(l2+1)] for _ in range(l1+1)]

for i in range(1, l1+1):
    for j in range(1, l2+1):
        if s1[i-1] == s2[j-1]:    # dp의 행, 열 길이보다 s1, s2의 길이가 1만큼 작음
            dp[i][j] = dp[i-1][j-1] + 1    # 같은 문자면 + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[l1][l2])     # LCS는 각 문자가 연속하지 않아도 됨       