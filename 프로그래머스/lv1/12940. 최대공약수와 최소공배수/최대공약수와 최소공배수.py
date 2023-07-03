def solution(n, m):
    answer = []
    answer.append(gcd(n,m))
    a = n / gcd(n,m)
    b = m / gcd(n,m)
    answer.append(a * b * answer[0])
    return answer

def gcd(n, m):
    if m == 0:
        return n
    else:
        return gcd(m, n % m)