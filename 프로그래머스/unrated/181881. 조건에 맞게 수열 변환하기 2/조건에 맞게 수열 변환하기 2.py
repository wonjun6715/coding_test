def solution(arr):
    answer = []
    cnt = 0
    while True:
        answer = arr.copy()
        for i in range(len(arr)):
            if arr[i] >= 50 and arr[i] % 2 == 0:
                arr[i] //= 2
            elif arr[i] < 50 and arr[i] % 2 == 1:
                arr[i] = (arr[i]*2) + 1
        cnt += 1
        if answer == arr:
            return cnt - 1
        