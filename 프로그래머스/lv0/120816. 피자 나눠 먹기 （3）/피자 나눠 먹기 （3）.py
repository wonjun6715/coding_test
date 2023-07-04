def solution(slice, n):
    answer = 0
    a = n // slice
    if slice * a < n:
        answer = a + 1
    else:
        answer = a
    return answer