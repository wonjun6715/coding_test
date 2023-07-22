def solution(people, limit):
    answer = 0
    cnt = 0
    people.sort(reverse = True)
    for i in people:
        if i + people[-1] > limit:
            cnt += 1
        else:
            people.pop(-1)
            cnt += 1
    return cnt