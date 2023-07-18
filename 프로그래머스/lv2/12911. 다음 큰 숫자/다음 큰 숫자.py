def solution(n):
    answer = 0
    binary = bin(n)[2:]
    one_count = binary.count('1')
    result = 0
    for i in range(n + 1, 1000001):
        binary2 = bin(i)[2:]
        if one_count == binary2.count('1'):
            result = i
            break
    return result