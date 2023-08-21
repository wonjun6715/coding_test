def solution(keyinput, board):
    answer = [0,0]
    for word in keyinput:
        if word == "left":
            if answer[0] == -(board[0] // 2):
                continue
            answer[0] -= 1
        elif word == "right":
            if answer[0] == board[0] // 2:
                continue
            answer[0] += 1
        elif word == "up":
            if answer[1] == board[1] // 2:
                continue
            answer[1] += 1
        else:
            if answer[1] == -(board[1] // 2):
                continue
            answer[1] -= 1
    return answer