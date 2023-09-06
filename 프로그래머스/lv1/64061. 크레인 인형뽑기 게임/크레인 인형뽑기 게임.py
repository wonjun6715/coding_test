def solution(board, moves):
    answer = []
    cnt = 0
    n = len(board)
    
    for move in moves:
        move -= 1  # 1-based index를 0-based index로 변환
        for i in range(n):
            if board[i][move] != 0:
                doll = board[i][move]
                board[i][move] = 0  # 인형을 뽑았으므로 0으로 설정
                if answer and answer[-1] == doll:
                    answer.pop()  # 인형 두 개가 연속으로 같으면 제거
                    cnt += 2
                else:
                    answer.append(doll)
                break

    return cnt