def solution(rank, attendance):
    answer = list(zip(rank, attendance))
    result = []
    for i in range(len(answer)):
        if answer[i][1] == True:
            result.append(answer[i])
    tmp = sorted(result, key=lambda x:x[0])
    a = rank.index(tmp[0][0])
    b = rank.index(tmp[1][0])
    c = rank.index(tmp[2][0])
    return 10000 * a + 100 * b + c