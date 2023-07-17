def solution(s):
    answer = []
    num_zero = 0
    cnt = 0
    while s != '1':
        num_zero += s.count('0')
        s = s.replace('0', '')
        length = len(s)
        s = bin(length)[2:]
        cnt += 1
    answer = [cnt, num_zero]
    return answer