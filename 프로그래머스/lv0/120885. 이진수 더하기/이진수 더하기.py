def solution(bin1, bin2):
    answer1 = '0b' + bin1
    answer2 = '0b' + bin2
    result1 = int(answer1,2)
    result2 = int(answer2, 2)
    
    return bin(result1+result2)[2:]