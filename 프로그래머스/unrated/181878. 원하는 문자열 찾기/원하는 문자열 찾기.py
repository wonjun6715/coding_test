def solution(myString, pat):
    answer = 0
    myString = myString.upper()
    pat = pat.upper()
    if pat in myString:
        return 1
    else:
        return 0
    return 