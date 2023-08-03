def solution(my_string):
    answer = []
    for key in my_string:
        if key not in answer:
            answer.append(key)
    return ''.join(answer)