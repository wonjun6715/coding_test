def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        map = ''
        for j in range(n):
            if arr1[i] & (1 << j) | arr2[i] & (1 << j):
                map += '#'
            else:
                map += ' '
                
        answer.append(map[::-1])
    return answer