def solution(a, b, c):
    answer = 0
    if a != b and a != c and b != c:
        return a + b + c
    elif (a == b and b != c) or (a == c and a != b) or(b == c and c != a):
        return (a + b + c) * (a**2 + b**2 + c**2)
    else:
        return (a + b + c) * (a*a + b*b + c*c) * (a**3 + b**3 + c**3)