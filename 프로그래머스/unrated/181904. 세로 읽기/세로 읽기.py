def solution(my_string, m, c):
    answer = ''
    """
    i h r h 
    b a k r
    f p n d
    o p l j
    h y g c
    """
    for i in range(c - 1, len(my_string), m):
        answer += my_string[i]    
    return answer