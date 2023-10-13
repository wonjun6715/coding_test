def solution(numbers):
    answer = list(map(str, numbers))
    answer.sort(key = lambda x: x * 3, reverse = True) 
    # x * 3을 하는 이유는 numbers의 원소가 최대 1000이하니까 최소 자릿수인 한자리 수를
    # 세자리 수까지 끌어 올리기 위해 666, 101010, 222
    # 333 303030 343434 555 999
    # 999 555 343434 333 303030
    result = str(int(''.join(answer)))
    return result