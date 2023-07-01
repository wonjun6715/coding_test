def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        a = commands[i][0]
        b = commands[i][1]
        c = commands[i][2]
        result = array[a - 1:b]
        n = len(result)
        for k in range(n - 1):
            for j in range(n - 1, k, -1):
                if result[j - 1] > result[j]:
                    result[j - 1], result[j] = result[j], result[j - 1]
        answer.append(result[c - 1])
    return answer