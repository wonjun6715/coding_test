def solution(age):
    answer = {'0' : 'a', '1' : 'b', '2' : 'c', '3' : 'd', '4' : 'e',
             '5' : 'f', '6' : 'g', '7' : 'h', '8' : 'i', '9' : 'j'}
    age1 = str(age)
    result = ''
    for word in age1:
        for key, value in answer.items():
            if word == key:
                result += value
    return result