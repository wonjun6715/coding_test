def solution(my_string):
    my_string = my_string.lower()
    answer = sorted(my_string)
    answer = ''.join(answer)
    
    return answer