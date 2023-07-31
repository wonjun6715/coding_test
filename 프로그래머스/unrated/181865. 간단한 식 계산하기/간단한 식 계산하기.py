def solution(binomial):
    answer = binomial.split()
    a = int(answer[0])
    b = int(answer[2])
    if answer[1] == '+':
        return a + b
    elif answer[1] == '-':
        return a - b
    else:
        return a * b