def solution(n):
    changed_n = convert(n, 3)
    return int(changed_n, 3)

def convert(n, base):
    result = ''

    while n > 0:
        n, r = divmod(n, base)
        result += str(r)

    return result
    