def solution(n):
    k = 1
    result = 0
    summ = 0                                              
    while True:
        for i in range(k, n + 1):
            summ += i
            if summ == n:
                result += 1
                break
            elif summ > n:
                break
        summ = 0
        k += 1
        if k == n + 1:
            break
    return result