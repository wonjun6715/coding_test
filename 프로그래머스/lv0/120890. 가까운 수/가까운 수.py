def solution(array, n):
    answer = []
    array.sort()
    for i in range(len(array)):
        answer.append(abs(n - array[i]))   
    return array[answer.index(min(answer))]