def solution(num, k):
    if str(k) not in str(num):
        return -1
    else:
        return str(num).find(str(k)) + 1