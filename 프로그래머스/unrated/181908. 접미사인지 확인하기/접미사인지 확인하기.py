def solution(my_string, is_suffix):
    answer = 0
    position = 0
    for i in range(len(my_string)):
        if is_suffix[position] == my_string[i]:
            if is_suffix[0:] == my_string[i:]:
                return 1
    return 0