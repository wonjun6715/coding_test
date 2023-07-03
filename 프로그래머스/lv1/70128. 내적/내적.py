def solution(a, b):
    answer = 1234567890
    result = 0
    for i in range(len(a)):
        answer = a[i] * b[i]
        result += answer
    return result