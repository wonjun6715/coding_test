def solution(dartResult):
    answer = 0
    result = []
    num = ''
    for i in range(len(dartResult)):
        if dartResult[i].isdigit():
            num += dartResult[i]
        elif dartResult[i].isalpha():
            if dartResult[i] == 'S':
                result.append(int(num)**1)
                num = ''
            elif dartResult[i] == 'D':
                result.append(int(num)**2)
                num = ''
            elif dartResult[i] == 'T':
                result.append(int(num)**3)
                num = ''
        else:
            if dartResult[i] == '*':
                if len(result) == 1:
                    result[0] = result[0] * 2
                elif len(result) == 2:
                    result[0] = result[0] * 2
                    result[1] = result[1] * 2
                else:
                    result[1] = result[1] * 2
                    result[2] = result[2] * 2
            else:
                if len(result) == 1:
                    result[0] = result[0] * (-1)
                elif len(result) == 2:
                    result[1] = result[1] * (-1)
                else:
                    result[2] = result[2] * (-1)
    return sum(result)