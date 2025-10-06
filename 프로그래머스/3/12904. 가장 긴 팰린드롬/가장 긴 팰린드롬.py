def solution(s):
    answer = 1
    if len(s) == 1:
        return 1

    # s1, e1 = 팰린드롬 길이가 홀수일 때 인덱스
    s1, e1 = 0, 0
    # s2, e2 = 팰린드롬 길이가 짝수일 때 인덱스
    s2, e2 = 0, 0

    for i in range(len(s)):
        s1 = i - 1
        e1 = i + 1
        while s1 >= 0 and e1 < len(s) and s[s1] == s[e1]:
            answer = max(answer, e1-s1+1)
            s1 -= 1
            e1 += 1

        s2 = i
        e2 = i + 1
        while s2 >= 0 and e2 < len(s) and s[s2] == s[e2]:
            answer = max(answer, e2-s2+1)
            s2 -= 1
            e2 += 1

    return answer