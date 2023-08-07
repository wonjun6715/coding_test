def solution(board, k):
    answer = 0
    leng = len(board[0])
    for i in range(len(board)):
        for j in range(leng):
            if i + j <= k:
                answer = answer + board[i][j]
    return answer