def solution(my_string):
    answer = []
    my_string += 'a'
    key = ''
    i = 0
    summ = 0
    while i != len(my_string):
        key = ''
        while my_string[i].isdigit():
            key += my_string[i]
            i += 1
            if my_string[i].isalpha():
                if key != '':
                    answer.append(key)
        i += 1
    for num in answer:
        summ += int(num)
    return summ