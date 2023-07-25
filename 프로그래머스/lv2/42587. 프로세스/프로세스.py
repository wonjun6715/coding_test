def solution(priorities, location):
    answer = 0
    cnt = 0
    queue = list(enumerate(priorities))
    while queue:
        cur_doc = queue.pop(0)
        if any(cur_doc[1] < doc[1] for doc in queue):
            queue.append(cur_doc)
        else:
            cnt += 1
            if cur_doc[0] == location:
                return cnt
            
    return answer