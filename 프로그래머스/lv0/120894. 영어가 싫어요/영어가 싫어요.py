def solution(numbers):
    result = ''
    tmp = ''
    num_dict = {'zero': '0', 'one' : '1', 'two' : '2', 'three' : '3', 'four' : '4', 
                'five' : '5', 'six' : '6', 'seven' : '7', 'eight' : '8', 'nine' : '9'}
    for i in range(len(numbers)):
        tmp += numbers[i]
        for key, value in num_dict.items():
            if tmp == key:
                result += value
                tmp = ''
    
    return int(result)