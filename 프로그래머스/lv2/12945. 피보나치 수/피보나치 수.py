def solution(n):
    num = 0
    num1 = 1
    summ = 0
    for i in range(2, n+1):
        summ = num + num1
        num = num1
        num1 = summ
    return summ % 1234567