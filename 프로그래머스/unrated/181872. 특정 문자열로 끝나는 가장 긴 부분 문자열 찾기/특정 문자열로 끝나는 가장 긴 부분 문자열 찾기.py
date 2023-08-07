def solution(myString, pat):
    answer = myString[::-1]
    pat1 = pat[::-1]
    result = answer.find(pat1)
    return myString[:len(myString) - result]
    