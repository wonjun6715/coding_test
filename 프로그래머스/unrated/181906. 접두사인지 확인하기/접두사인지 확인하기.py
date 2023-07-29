def solution(my_string, is_prefix):
    answer = 0
    if len(is_prefix) < len(my_string):
        for i in range(len(is_prefix)):
            if is_prefix[i] == my_string[i]:
                continue
            else:
                return 0
    else:
         return 0       
    return 1