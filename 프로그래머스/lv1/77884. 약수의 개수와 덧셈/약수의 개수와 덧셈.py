def solution(left, right):
    answer = 0
    c = 0
    summ = 0
    for i in range(left, right + 1):
        c = 0
        for j in range(1, i + 1):
            if i % j == 0:                
                c += 1
        if c % 2 == 0:
            summ += i
        else:
            summ -= i
    return summ