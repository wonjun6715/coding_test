def solution(n):
    n = int(n)
    arr = list(str(n))
    
    return int("".join(sorted(arr, reverse = True)))