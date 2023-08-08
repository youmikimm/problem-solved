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

if dp[l1][l2] != 0:
    subseq = []
    x = l1
    y = l2
    while x > 0 and y > 0:    # 최초로 바뀐 곳을 lcs문자열에 추가할 것
        if dp[x][y-1] == dp[x][y]:    # 위로 이동
            y -= 1
        elif dp[x-1][y] == dp[x][y]:    # 왼쪽으로 이동
            x -= 1
        else:
            subseq.append(s1[x-1])
            x -= 1
            y -= 1
        
    subseq.reverse()
    print(''.join(subseq))
        