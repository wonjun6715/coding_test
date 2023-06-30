def solution(number):
    answer = 0
    for i in range(len(number)):
        for k in range(i + 1, len(number)):
            for j in range(k + 1, len(number)):
                if number[i] + number[k] + number[j] == 0:
                    answer += 1
    return answer