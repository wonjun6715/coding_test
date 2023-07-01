def solution(n, arr1, arr2):
    tmp1 = ''
    tmp2 = ''
    answer = ''
    result1 = []
    result2 = []
    correct = []
    for i in range(len(arr1)):
        tmp1 = ''
        tmp2 = ''
        for _ in range(n):
            remainder1 = arr1[i] % 2
            arr1[i] = arr1[i] // 2
            tmp1 = tmp1 + str(remainder1)
            
            remainder2 = arr2[i] % 2
            arr2[i] = arr2[i] // 2
            tmp2 = tmp2 + str(remainder2)
            
        result1.append(tmp1[::-1])
        result2.append(tmp2[::-1])
        
    for i in range(n):
        answer = ''
        for j in range(n):
            if result1[i][j] == '0' and result2[i][j] == '0':
                answer += ' '
            else:
                answer += '#'
        correct.append(answer)
    return correct