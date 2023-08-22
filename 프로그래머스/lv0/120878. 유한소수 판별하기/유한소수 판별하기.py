def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)
def solution(a, b):
    answer = []
    d = 2
    common = gcd(a, b)
    a_1 = a // common
    b_1 = b // common
    
    while d <= b_1:
        if b_1 % d == 0:
            b_1 = b_1 // d
            answer.append(d)
        else:
            d += 1   
    result = list(set(answer))
    if len(result) == 2 and 2 in result and 5 in result:
        return 1
    elif len(result) == 1 and result[0] == 2:
        return 1
    elif len(result) == 1 and result[0] == 5:
        return 1
    elif a  % b == 0:
        return 1
    else:
        return 2
    