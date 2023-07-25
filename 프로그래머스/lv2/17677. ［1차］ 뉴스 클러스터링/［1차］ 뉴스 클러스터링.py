def solution(str1, str2):
    answer = []
    answer2 = []
    str1 = str1.upper()
    str2 = str2.upper()
    intersection = 0
    for i in range(len(str1) - 1):
        if str1[i:i+2].isalpha():
            answer.append(str1[i:i+2])
    for i in range(len(str2) - 1):
        if str2[i:i+2].isalpha():
            answer2.append(str2[i:i+2])
    result = list(set(answer))
    for i in result:
        if answer.count(i) > answer2.count(i):          
            intersection += answer2.count(i)
        else:
            intersection += answer.count(i)
    union = len(answer) + len(answer2) - intersection
    if intersection == 0 and union == 0:
        return 65536
    else:
        return int((intersection / union) * 65536)