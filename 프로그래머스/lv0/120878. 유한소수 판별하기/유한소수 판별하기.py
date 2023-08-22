def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)
def solution(a, b):
    b = b // gcd(a,b)
    while b % 2 == 0:
        b = b // 2
    while b % 5 == 0:
        b = b // 5
    return 1 if b == 1 else 2
    