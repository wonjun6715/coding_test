def solution(my_string, s, e):
    answer = ''
    result = list(my_string[s:e + 1])[::-1]
    
    return my_string[0:s] + ''.join(result) + my_string[e + 1:len(my_string)]