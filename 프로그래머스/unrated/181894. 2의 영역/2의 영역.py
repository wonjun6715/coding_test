def solution(arr):
    a = -1
    b = -1
    for i in range(len(arr)):
        if arr[i] == 2:
            a = i
            break
    for j in range(len(arr) - 1, -1, -1):
        if arr[j] == 2:
            b = j
            break
    if a == -1:
        return [-1]
    return arr[a:b + 1]