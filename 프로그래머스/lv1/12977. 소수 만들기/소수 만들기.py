import itertools

def prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True         

def solution(nums):
    answer = 0
    result = list(itertools.combinations(nums, 3))
    for i in range(len(result)):
        if prime(sum(result[i])) == True:
            answer += 1
    return answer