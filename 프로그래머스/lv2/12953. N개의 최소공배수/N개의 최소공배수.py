def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
def solution(arr):
    answer = gcd(arr[0], arr[1])
    a = arr[0] // answer
    b = arr[1] // answer
    l = answer * a * b
    for i in range(2, len(arr)):
        answer = gcd(l, arr[i])
        a = l // answer
        b = arr[i] // answer
        l = answer * a * b
    return l