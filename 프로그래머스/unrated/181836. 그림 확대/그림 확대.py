def solution(picture, k):
    answer = []
    word = ''
    for i in range(len(picture)):
        for j in range(len(picture[i])):
            for n in range(k):
                word += picture[i][j]
        for q in range(k):
            answer.append(word)
        word = ''
    return answer