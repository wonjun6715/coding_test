def solution(x):
    n = int(x)
    arr = str(n)
    sum = 0
    for i in range(len(arr)):
        sum += int(arr[i])
    
    if x % sum == 0:
        return True
    else:
        return False
    