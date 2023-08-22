def solution(n):
    a = 1
    b = 1
    while a != n:     
        a += 1  
        b += 1
        while '3' in str(b) or b % 3 == 0:  
            b += 1             
    return b
