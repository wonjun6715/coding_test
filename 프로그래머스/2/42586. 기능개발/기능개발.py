from collections import deque
def solution(progresses, speeds):
    cnt = 1
    answer = []
    dq = deque()
    for i in range(len(speeds)):
        if ((100 - progresses[i]) % speeds[i] != 0):
            dq.append(((100 - progresses[i]) // speeds[i]) + 1)
        else:
            dq.append((100 - progresses[i]) // speeds[i])   
    while dq:
        a = dq.popleft()
        cnt = 1
        while len(dq) > 0:
            if a >= dq[0]:
                dq.popleft()
                cnt += 1
            else:
                break
        answer.append(cnt)
    return answer