def solution(num_list):
    answer = 0
    for num in num_list:
        if num < 0:
            answer += 1
            return num_list.index(num)
    if answer == 0:
        return -1
    return answer