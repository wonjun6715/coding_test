def solution(my_string):
    answer = [0] * 52
    for i in range(len(my_string)):
        if my_string[i].isupper():
            answer[ord(my_string[i]) - 65] += 1
        elif my_string[i].islower():
            answer[ord(my_string[i]) - 71] += 1
    
    return answer