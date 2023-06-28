def solution(keymap, targets):
    answer = []
    for target in targets:
        minkey = 0
        for i in target:
            count = []
            for k in range(len(keymap)):
                key = keymap[k].find(i)
                if key > -1:
                    count.append(key)
            if count:
                minkey += min(count) + 1
            else:
                minkey = -1
                break
        answer.append(minkey)
    return answer