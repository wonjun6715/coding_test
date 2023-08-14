def solution(arr):
    answer = []
    i = 0
    while True:
        if len(arr) <= 2**i:
            break
        i += 1
    n = (2**i) - len(arr)
    if n == 0:
        return arr
    else:
        for i in range(n):
            arr.append(0)
    return arr