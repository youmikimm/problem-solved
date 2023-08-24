def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
    
    
def solution(n, m):
    g = gcd(n, m)
    return [g, (n * m) // g]