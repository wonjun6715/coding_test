def solution(my_strings, parts):
    answer = ''
    for string, pair in zip(my_strings, parts):
        answer += string[pair[0]:pair[1] + 1]
    return answer