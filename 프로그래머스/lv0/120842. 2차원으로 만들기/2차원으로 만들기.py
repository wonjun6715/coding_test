def solution(num_list, n):
    answer = [[None] * n for _ in range(len(num_list) // n)]
    position = 0
    for i in range(len(num_list) // n):
        for j in range(n):
            answer[i][j] = (num_list[position])
            position += 1
    return answer