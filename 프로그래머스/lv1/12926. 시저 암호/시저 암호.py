import string
def solution(s, n):
    answer = []
    lower = list(string.ascii_lowercase)
    upper = list(string.ascii_uppercase)
    
    for x in s:
        if x.isspace():
            answer.append(' ')
            continue
        elif x.isupper():
            idx = (upper.index(x) + n) % 26
            answer.append(upper[idx])
        else:
            idx = (lower.index(x) + n) % 26
            answer.append(lower[idx])

    return ''.join(answer)