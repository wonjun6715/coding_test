import math
def solution(n):
    answer = 0
    prime = [True for i in range(n + 1)]
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if prime[i] == True:
            j = 2
            while i * j <= n:
                prime[i * j] = False
                j += 1
                
    for i in range(2, n + 1):
        if prime[i] == True:
            answer += 1
    return answer