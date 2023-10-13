global ok
ok = []
from itertools import permutations
def is_prime(number):
    number = list(number)
    number = int(''.join(s for s in number))
    if number == 1 or number == 0:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    if number in ok:
        return False
    else: ok.append(number)
    return True

def solution(numbers):
    cnt = 0
    for i in range(1, len(numbers) + 1):
        for j in permutations(numbers,i):
            result = is_prime(j)
            if result == True:
                cnt += 1    
    return cnt