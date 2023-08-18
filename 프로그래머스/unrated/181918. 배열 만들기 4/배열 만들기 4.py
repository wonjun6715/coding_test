def solution(arr):
    stk = []
    i = 0
    top = -1
    while i < len(arr):
        if top < 0:
            stk.append(arr[i])
            i += 1
            top += 1
        elif top >= 0 and stk[top] < arr[i]:
            stk.append(arr[i])
            i += 1
            top += 1
        elif top >= 0 and stk[top] >= arr[i]:
            stk.remove(stk[top])
            top -= 1
    return stk[0:top+1]